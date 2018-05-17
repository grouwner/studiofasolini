from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

categories = (
    ('residenziale','Residenziale'),
    ('hotel','Hotel'),
    ('interni','Interni'),
    ('ristrutturazione','Ristrutturazione'),
    ('villa','Villa'),
    ('commerciale','Commerciale'),
)


class Intervento(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titolo_intervento = models.CharField(max_length=200, default='')
    categoria = models.CharField(max_length=200, choices=categories, default='residenziale')
    anno = models.DateTimeField(blank=True,default=timezone.now)
    inizio_lavori = models.CharField(blank=True,max_length=200, default='')
    inizio_lavori_active = models.BooleanField(('Attiva inizio lavori'), default=True, help_text=('If is checked show the inizio lavori'))
    fine_lavori = models.CharField(blank=True,max_length=200, default='')
    fine_lavori_active = models.BooleanField(('Attiva fine lavori'), default=True, help_text=('If is checked show the fine lavori'))
    committente = models.CharField(blank=True,max_length=200, default='')
    committente_active = models.BooleanField(('Attiva committente'), default=True, help_text=('If is checked show the committente'))
    commercializzazione = models.CharField(blank=True,max_length=200, default='')
    commercializzazione_active = models.BooleanField(('Attiva commercializzazione'), default=True, help_text=('If is checked show the commercializzazione'))
    url_committente = models.CharField(blank=True,max_length=200, default='')
    url_committente_active = models.BooleanField(('Attiva url commitente'), default=True, help_text=('If is checked show the url commitente'))
    sito_intervento = models.CharField(blank=True,max_length=200, default='')
    sito_intervento_active = models.BooleanField(('Attiva sito intervento'), default=True, help_text=('If is checked show sito intervento'))
    impresa = models.CharField(blank=True,max_length=200, default='')
    impresa_active = models.BooleanField(('Attiva impresa'), default=True, help_text=('If is checked show impresa'))
    strutture = models.CharField(blank=True,max_length=200, default='')
    strutture_active = models.BooleanField(('Attiva strutture'), default=True, help_text=('If is checked show strutture'))
    impianti = models.CharField(blank=True,max_length=200, default='')
    impianti_active = models.BooleanField(('Attiva impianti'), default=True, help_text=('If is checked show impianti'))
    progetto_del_verde = models.CharField(blank=True,max_length=200, default='')
    progetto_del_verde_active = models.BooleanField(('Attiva progetto del verde'), default=True, help_text=('If is checked show progetto del verde'))
    video = models.CharField(blank=True,max_length=200, default='')
    descrizione = models.TextField(blank=True,default='')
    sinonimi = models.TextField(default='')
    thumb_intervento = models.FileField(upload_to="", default='', blank=True)
    latitudine = models.CharField(max_length=200, default='')
    longitudine = models.CharField(max_length=200, default='')
    slug = models.SlugField(max_length=200, default='', )
    published_date = models.DateTimeField(blank=True, null=True)
    photo_active = models.BooleanField(('Attiva Photo Album'), default=True, help_text=('If is checked show the Photo Album'))
    info_active = models.BooleanField(('Attiva Info Project'), default=True,help_text=('If is checked show the Info Project'))
    thumb_active = models.BooleanField(('Attiva Thumb Project'), default=True,help_text=('If is checked show the Thumb Project'))
    video_active = models.BooleanField(('Attiva Video Project'), default=True,help_text=('If is checked show the Video Project'))

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titolo_intervento


class photo(models.Model):
    author = models.ForeignKey(Intervento, on_delete=models.CASCADE)
    photo = models.FileField(upload_to="", default='', blank=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()