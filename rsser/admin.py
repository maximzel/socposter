from django.contrib import admin
from django.forms import Textarea
from django.db import models
from rsser.models import Rss, Autoparsed


@admin.register(Rss)
class YourModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': Textarea(attrs={'rows': 4, 'cols': 75})},
    }


admin.site.register(Autoparsed)
