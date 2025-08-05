from django.urls import path
from .views import VacancyViewSet, JobApplicationViewSet, ClientFeedbackViewSet
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
    openapi.Info(
        title="Ваш API",
        default_version='v1',
        description="Описание API",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),


    path('vacancies/', VacancyViewSet.as_view({'get': 'list'}), name='vacancies'),

    path('applications/', JobApplicationViewSet.as_view({'get': 'list'}), name='job_applications'),
    path('application/create/', JobApplicationViewSet.as_view({'post': 'post'}), name='job_application_create'),

    path('client_feedbacks/', ClientFeedbackViewSet.as_view({'get': 'list'}), name='client_feedbacks'),
    path('client_feedback/create/', ClientFeedbackViewSet.as_view({'post': 'post'}), name='client_feedback_create'),
]