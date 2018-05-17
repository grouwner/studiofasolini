from django.contrib import admin
from .models import Intervento, photo

class upload_photo(admin.StackedInline):
    model = photo
    extra = 0
    classes = ['collapse']

    fieldsets = (
        ('', {'fields': (
            ('published_date', 'photo',),
        ),
        }),
    )

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("titolo_intervento",)}
    inlines = [upload_photo]

    fieldsets = (
        ('Info Generale', {'fields': (
            ('author', 'titolo_intervento', 'categoria',),
        ),
        }),

        ('Info Lavori', {'fields': (
            ('inizio_lavori', 'fine_lavori'),
            ('inizio_lavori_active', 'fine_lavori_active'),
        ),
        }),
        ('Info committenze', {'fields': (
            ('committente', 'commercializzazione',),
            ('committente_active', 'commercializzazione_active',),
        ),
        }),
        ('Info URL', {'fields': (
            ('url_committente', 'sito_intervento',),
            ('url_committente_active', 'sito_intervento_active',),
        ),
        }),
        ('Info collaboratori', {'fields': (
            ('impresa', 'strutture', 'impianti',),
            ('impresa_active', 'strutture_active', 'impianti_active',),
        ),
        }),
        ('Info Extra', {'fields': (
            ('progetto_del_verde', 'video',),
            ('progetto_del_verde_active', 'video_active',),
        ),
        }),

        ('Attivazioni Progetto', {'fields': (
            ('photo_active', 'info_active', 'thumb_active',),
        ),
        }),
        ('Info Progetto', {'fields': (
            ('descrizione',),
            ('sinonimi',),
            ('thumb_intervento'),
            ('latitudine', 'longitudine',),
            ('slug',),
            ('anno', 'published_date',),
        )
        }),
    )


admin.site.register(Intervento, ProjectAdmin)