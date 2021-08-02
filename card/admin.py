from django.contrib import admin
from .models import PersonalCard, Skills, Project, Country, Region, ProjectImages

admin.site.register(PersonalCard)
admin.site.register(Skills)
admin.site.register(Project)
admin.site.register(Country)
admin.site.register(Region)
admin.site.register(ProjectImages)