from django.db import models
from django.utils.translation import gettext_lazy as _


class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name=_("Skill"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Skill')
        verbose_name_plural = _('Skills')





class Vacancy(models.Model):
    requirements = models.ManyToManyField(Skill, related_name='vacancies', verbose_name=_("Requirement"))
    job = models.CharField(max_length=250, verbose_name=_("Job title"))

    def __str__(self):
        return self.job

    class Meta:
        verbose_name = _('Vacancy')
        verbose_name_plural = _('Vacancies')




class JobApplication(models.Model):
    class DeveloperType(models.TextChoices):
        BACKEND = 'backend', _('Backend разработчик')
        FRONTEND = 'frontend', _('Frontend разработчик')
        DEVOPS = 'devops', _('DevOps инженер')
        UI_UX = 'uiux', _('UI/UX дизайнер')

    class WorkType(models.TextChoices):
        FULL_TIME = 'full_time', _('Full Time')
        PART_TIME = 'part_time', _('Part Time')
        ONLINE = 'online', _('Online')

    type_developer = models.CharField(
        max_length=20,
        choices=DeveloperType.choices,
        verbose_name=_("Choose position")
    )

    work_type = models.CharField(
        max_length=20,
        choices=WorkType.choices,
        verbose_name=_("Work type")
    )

    first_name = models.CharField(max_length=100, verbose_name=_("Name"))
    last_name = models.CharField(max_length=100, verbose_name=_("Last name"))
    phone_number = models.CharField(max_length=20, verbose_name=_("Phone number"))
    resume = models.FileField(upload_to='resumes/', verbose_name=_("Resume / CV"))

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.get_type_developer_display()} ({self.get_work_type_display()})"

    class Meta:
        verbose_name = _("Job application")
        verbose_name_plural = _("Job applications")


class ClientFeedback(models.Model):
    first_name = models.CharField(max_length=100, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=100, verbose_name=_("Last Name"))
    position = models.CharField(max_length=150, verbose_name=_("Position"))
    company_name = models.CharField(max_length=200, verbose_name=_("Company Name"))
    comment = models.TextField(verbose_name=_("Comment"))
    image = models.ImageField(upload_to='client_images/', verbose_name=_("Client Image"))
    feedback_file = models.FileField(upload_to='feedback_files/', verbose_name=_("Feedback File"))

    def __str__(self):
        return f"{self.first_name} {self.last_name} — {self.company_name}"

    class Meta:
        verbose_name = _("Client Feedback")
        verbose_name_plural = _("Client Feedbacks")
