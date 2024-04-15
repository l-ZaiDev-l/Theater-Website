from django.shortcuts import render, get_object_or_404, redirect
from django.db.models.signals import post_save
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.http import JsonResponse
from django.dispatch import receiver
from datetime import date
from .models import *
import json



# Create your views here.

def index(request):
    today = date.today()
    closest_concerts = Concert.objects.filter(date__gte=today).order_by('date')[:3]
    concert = Concert.objects.all()
    concert_types = ConcertType.objects.all()  # Récupérez tous les types de concerts
    
    actualite = Actualite.objects.all()
    
    context = {
        "concert": concert,
        "closest_concerts": closest_concerts,
        "Actualite": actualite,
        "concert_types": concert_types,  # Ajoutez cette ligne
    }
    return render(request, "pages/index.html", context)

# def index(request):
#     today = date.today()
#     closest_concerts = Concert.objects.filter(date__gte=today).order_by('date')[:3]
#     concert = Concert.objects.all()
#     actualite = Actualite.objects.all()
#     context ={"concert": concert,'closest_concerts': closest_concerts,"Actualite": actualite}
#     return render(request, "pages/index.html",context)


def calendrier(request):
    concerts = Concert.objects.all()
    
    # Transformez les données des concerts en un format compatible avec les événements du calendrier
    events = []

    for concert in concerts:
        event = {
            "eventName": concert.title,
            "calendar": "Concerts",
            "color": "blue",
            "date": concert.date.strftime('%Y-%m-%d'),
        }
        events.append(event)

    context = {"concerts": concerts, "events_json": json.dumps(events)}
    return render(request, "pages/calendrier.html", context)

def nostalgie(request):
    nostalgies = NostalgiaConcert.objects.all()
    context = {'nostalgies': nostalgies}
    return render(request, "pages/nostalgie.html", context)

def nostalgie_detail(request, nostalgie_id):  # Ajoutez nostalgie_id comme argument
    nostalgie = get_object_or_404(NostalgiaConcert, id=nostalgie_id)
    nostalgie_all = NostalgiaConcert.objects.all()
    nostalgie_media = Media_Nostalgie.objects.filter(nostalgie=nostalgie)
    context = {'nostalgie': nostalgie, 'consert_all': nostalgie_all,'nostalgie_media': nostalgie_media}
    return render(request, "pages/nostalgie_detail.html", context)


def concert_detail(request, concert_id):
    concert = get_object_or_404(Concert, id=concert_id)
    consert_all = Concert.objects.all()
    concert_media = Media.objects.filter(concert=concert)
    context = {'concert': concert,'consert_all':consert_all,'concert_media': concert_media}
    return render(request, 'pages/concert_detail.html', context)

def actualite_detail(request, actualite_id):
    actualite = Actualite.objects.get(id=actualite_id)
    context = {'actualite': actualite}
    return render(request, 'pages/actualite_detail.html', context)

def search_result(request):
    if request.method == "POST":
        searched = request.POST['q']
        concert = Concert.objects.filter(title__contains = searched)
        concert_types = ConcertType.objects.all()
        context ={"concert": concert,"searched":searched,"concert_types": concert_types}
        return render(request, "pages/search_result.html",context)
    else:   
        return render(request, "pages/search_result.html")
    

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            subscriber, created = Subscriber.objects.get_or_create(email=email)
            return redirect('index') 
    return render(request, 'pages/index.html')

#/************************************************************************/

@receiver(post_save, sender=Concert)
def send_email_to_subscribers(sender, instance, created, **kwargs):
    if created:
        subject = 'Nouvelle annonce de concert'
        message = f'Un nouveau concert a été annoncé :\n\n'
        message += f'Titre : {instance.title}\n'
        message += f'Date : {instance.date}\n'
        message += f'Heure : {instance.start_time} - {instance.end_time}\n'
        message += f'Description : {instance.description}\n'
        message += f'Lien pour les billets : {instance.ticket_link}\n\n'
        message += 'Consultez notre site Web pour plus de détails !'
        
        from_name = 'Theatre M5'
        from_email = 'zaid2016hankrii@gmail.com'  # Replace with your from email address
        subscriber_emails = Subscriber.objects.values_list('email', flat=True)
        recipient_list = list(subscriber_emails)
        
        email = EmailMessage(subject, message, from_email, recipient_list)
        
        # Attach the concert image
        concert_image_path = instance.normal_image.path  # Update this based on your model field
        email.attach_file(concert_image_path)
        
        # Send the email
        email.send(fail_silently=False)

# Connect the signal directly inside your views.py
post_save.connect(send_email_to_subscribers, sender=Concert)
