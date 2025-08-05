from .models import Vacancy, JobApplication, ClientFeedback
from .serializers import VacancySerializer, JobApplicationSerializer, ClientFeedbackSerializer
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema



class VacancyViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary="List of Vacancies",
        responses={200: VacancySerializer(many=True)},
        tags=["Vacancy"],
    )

    def list(self, request):
        queryset = Vacancy.objects.all()
        serializer = VacancySerializer(queryset, many=True)
        return Response(serializer.data)




class JobApplicationViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary="List of job applications",
        responses={200: JobApplicationSerializer(many=True)},
        tags=["Job applications"]
    )

    def list(self, request):
        applications = JobApplication.objects.all()
        serializer = JobApplicationSerializer(applications, many=True, context={"request": request})
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Create a job application",
        request_body=JobApplicationSerializer,
        responses={
            201: JobApplicationSerializer,
            400: "Validation error"
        },
        tags=["Job applications"]
    )

    def post(self, request):
        serializer = JobApplicationSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)




class ClientFeedbackViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary="List of customer feedback",
        responses={200: ClientFeedbackSerializer(many=True)},
        tags=["Feedback"]
    )

    def list(self, request):
        feedbacks = ClientFeedback.objects.all()
        serializer = ClientFeedbackSerializer(feedbacks, many=True, context={"request": request})
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Create a customer feedback",
        request_body=ClientFeedbackSerializer,
        responses={
            201: ClientFeedbackSerializer,
            400: "Validation error"
        },
        tags=["Feedback"]
    )

    def post(self, request):
        serializer = ClientFeedbackSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

