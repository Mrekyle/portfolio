from django.contrib import admin
from .models import Offerings, Skill_Cards, Work_History, Current_Projects

# Register your models here.


class Offerings_Admin(admin.ModelAdmin):
    """
        Offerings Admin Panel
    """

    list_display = (
        'name',
        'friendly_name',
    )

class Skill_Cards_Admin(admin.ModelAdmin):
    """
        Skill Cards Admin
    """

    list_display = (
        'name',
        'friendly_name',
        'image',
        'image_url',
    )

class Work_History_Admin(admin.ModelAdmin):
    """
        Work History Admin
    """

    list_display = (
        'name',
        'image',
        'bio',
        'dates',
    )

class Current_Projects_Admin(admin.ModelAdmin):
    """
        Current Projects Admin
    """

    list_display = (
        'name', 
        'friendly_name',
        'live_site',            
    )

admin.site.register(Offerings, Offerings_Admin)
admin.site.register(Skill_Cards, Skill_Cards_Admin)
admin.site.register(Work_History, Work_History_Admin)
admin.site.register(Current_Projects, Current_Projects_Admin)