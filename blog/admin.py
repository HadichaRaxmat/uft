from django.contrib import admin
from .models import Skill, Vacancy, JobApplication, ClientFeedback

admin.site.register(Skill)
admin.site.register(Vacancy)
admin.site.register(JobApplication)



@admin.register(ClientFeedback)
class ClientFeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment')
