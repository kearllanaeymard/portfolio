from django.contrib import admin
from .models import Experience, Skill, Service, Project, Event


class ExperienceAdmin(admin.ModelAdmin):
    list_display = [
        'company_name',
        'position',
        'date_hired',
    ]

class SkillAdmin(admin.ModelAdmin):
    list_display = [
        'skill_name',
    ]

class ServiceAdmin(admin.ModelAdmin):
    list_display = [
        'image_tag',
        'service_name',
        'service_description',
    ]

class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        'image_tag',
        'project_name',
        'client_name',
        'project_description',
    ]

class EventAdmin(admin.ModelAdmin):
    list_display = [
        'image_tag',
        'event_name',
        'participants',
        'event_description',
        'event_date',
    ]

admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Event, EventAdmin)