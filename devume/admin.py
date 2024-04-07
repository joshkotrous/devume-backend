from django.contrib import admin
from devume.models.profile import Profile
from devume.models.skill import Skill
from devume.models.city import City
from devume.models.country import Country
from devume.models.state import State
from devume.models.work_experience import WorkExperience
from devume.models.education import Education

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['uuid']}),
        (None, {'fields': ['user_id']}),
        (None, {'fields': ['birth_date']}),
        (None, {'fields': ['bio']}),
        (None, {'fields': ['city']}),
        (None, {'fields': ['created_at']}),
        (None, {'fields': ['modified_at']})
    ]
    list_display = ('uuid', 'user_id', 'birth_date', 'bio', 'city')

class CityAdmin(admin.ModelAdmin):
    fieldSets = [
        (None, {'fields': ['id']}),
        (None, {'fields': ['name']}),
        (None, {'fields': ['state']})
    ]

class StateAdmin(admin.ModelAdmin):
    fieldSets = [
        (None, {'fields': ['id']}),
        (None, {'fields': ['name']}),
        (None, {'fields': ['state_code']}),
        (None, {'fields': ['country']})

    ]
    
class CountryAdmin(admin.ModelAdmin):
    fieldSets = [
        # (None, {'fields': ['id']}),
        (None, {'fields': ['name']}),
        (None, {'fields': ['country_code']}),

    ]

class SkillAdmin(admin.ModelAdmin):
    fieldSets = [
        (None, {'fields': ['id']}),
        (None, {'fields': ['name']})

    ]

class WorkExperienceAdmin(admin.ModelAdmin):
    fieldSets = [
        (None, {'fields': ['id']}),
        (None, {'fields': ['profile']}),
        (None, {'fields': ['company']}),
        (None, {'fields': ['description']}),
        (None, {'fields': ['skills']}),
        (None, {'fields': ['start_date']}),
        (None, {'fields': ['end_date']})
    ]

class EducationAdmin(admin.ModelAdmin):
    fieldSets = [
        (None, {'fields': ['id']}),
        (None, {'fields': ['profile']}),
        (None, {'fields': ['school_name']}),
        (None, {'fields': ['degree']})
    ]



admin.site.register(Profile, ProfileAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(WorkExperience, WorkExperienceAdmin)
admin.site.register(Education, EducationAdmin)