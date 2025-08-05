from .models import Vacancy, JobApplication, ClientFeedback
from .serializers import VacancySerializer, JobApplicationSerializer, ClientFeedbackSerializer
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class VacancyViewSet(ViewSet):
    def list(self, request):
        queryset = Vacancy.objects.all()
        serializer = VacancySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            vacancy = Vacancy.objects.get(pk=pk)
        except Vacancy.DoesNotExist:
            return Response({"error": "Vacancy not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)




class JobApplicationViewSet(ViewSet):
    def list(self, request):
        applications = JobApplication.objects.all()
        serializer = JobApplicationSerializer(applications, many=True, context={"request": request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        application = get_object_or_404(JobApplication, pk=pk)
        serializer = JobApplicationSerializer(application, context={"request": request})
        return Response(serializer.data)


class ClientFeedbackViewSet(ViewSet):
    def list(self, request):
        feedbacks = ClientFeedback.objects.all()
        serializer = ClientFeedbackSerializer(feedbacks, many=True, context={"request": request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        feedback = get_object_or_404(ClientFeedback, pk=pk)
        serializer = ClientFeedbackSerializer(feedback, context={"request": request})
        return Response(serializer.data)