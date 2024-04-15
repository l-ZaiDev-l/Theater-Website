from django.db import models

class ConcertType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Space(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class ParticipantType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Participant(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='participants/')
    participant_type = models.ForeignKey(ParticipantType, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Concert(models.Model):
    title = models.CharField(max_length=100)
    normal_image = models.ImageField(upload_to='concerts/')
    png_image = models.ImageField(upload_to='concerts/', blank=True, null=True)
    date = models.DateField()
    description = models.TextField()
    concert_type = models.ForeignKey(ConcertType, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    ticket_available = models.BooleanField()
    ticket_link = models.URLField()
    space = models.ForeignKey(Space, on_delete=models.CASCADE)
    # participants = models.ManyToManyField(Participant, related_name='concerts')
    participants = models.ManyToManyField(Participant, related_name='concerts', blank=True)


    def __str__(self):
        return self.title

class Media(models.Model):
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='concert_media/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Media for {self.concert.title}"
    



class NostalgiaConcert(models.Model):
    title = models.CharField(max_length=100)
    normal_image = models.ImageField(upload_to='concerts/',null=True)
    date = models.DateField()
    description = models.TextField()
    participants = models.ManyToManyField(Participant, related_name='nostalgia_concerts')

    def __str__(self):
        return self.title

class Media_Nostalgie(models.Model):
    nostalgie = models.ForeignKey(NostalgiaConcert, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='nostalgie_media/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Media for {self.nostalgie.title}"

class Actualite(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='concert_media/', blank=True, null=False)
    
    def __str__(self):
        return self.title


class Subscriber(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email