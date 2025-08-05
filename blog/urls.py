from django.urls import path
from .views import VacancyViewSet, JobApplicationViewSet, ClientFeedbackViewSet

urlpatterns = [
    path('vacancies/', VacancyViewSet.as_view({'get': 'list'}), name='vacancies'),
    path('vacancy/<int:pk>/', VacancyViewSet.as_view({'get': 'retrieve'}), name='vacancy'),

    path('applications/', JobApplicationViewSet.as_view({'get': 'list'}), name='job_applications'),
    path('application/<int:pk>/', JobApplicationViewSet.as_view({'get': 'retrieve'}), name='job_application'),

    path('client_feedbacks/', ClientFeedbackViewSet.as_view({'get': 'list'}), name='client_feedbacks'),
    path('client_feedback/<int:pk>/', ClientFeedbackViewSet.as_view({'get': 'retrieve'}), name='client_feedback'),
]