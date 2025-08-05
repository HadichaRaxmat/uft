from rest_framework import serializers
from django.conf import settings
from .models import Vacancy, Skill, ClientFeedback, JobApplication

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name']


class VacancySerializer(serializers.ModelSerializer):
    requirements = SkillSerializer(many=True)


    class Meta:
        model = Vacancy
        fields = ['id', 'job', 'requirements',]



class JobApplicationSerializer(serializers.ModelSerializer):
    type_developer = serializers.ChoiceField(
        choices=JobApplication.DeveloperType.choices,
        label="Choose position"
    )
    work_type = serializers.ChoiceField(
        choices=JobApplication.WorkType.choices,
        label="Work type"
    )

    class Meta:
        model = JobApplication
        fields = [
            'id',
            'type_developer',
            'work_type',
            'first_name',
            'last_name',
            'phone_number',
            'resume',
        ]



class ClientFeedbackSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=True)
    feedback_file = serializers.FileField(required=True)
    feedback_file_url = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = ClientFeedback
        fields = [
            'id',
            'first_name',
            'last_name',
            'position',
            'company_name',
            'comment',
            'image',
            'feedback_file',
            'image_url',
            'feedback_file_url'
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        lang = request.headers.get('Accept-Language', settings.MODELTRANSLATION_DEFAULT_LANGUAGE) if request else settings.MODELTRANSLATION_DEFAULT_LANGUAGE
        lang = lang.split(',')[0]

        if lang in settings.MODELTRANSLATION_LANGUAGES:
            for field in ['comment', 'position', 'company_name']:
                translated = getattr(instance, f"{field}_{lang}", None)
                if translated:
                    data[field] = translated

        return data

    def get_feedback_file_url(self, obj):
        request = self.context.get('request')
        if obj.feedback_file and request:
            return request.build_absolute_uri(obj.feedback_file.url)
        return None

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None
