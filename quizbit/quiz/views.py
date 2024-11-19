from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Question, PracticeHistory
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny


class QuestionListAPI(APIView):
    def get(self, request):
        questions = Question.objects.all().values('id', 'title', 'choices')
        return Response(list(questions), status=status.HTTP_200_OK)

class QuestionDetailAPI(APIView):
    def get(self, request, question_id):
        question = get_object_or_404(Question, id=question_id)
        data = {
            "id": question.id,
            "title": question.title,
            "description": question.description,
            "choices": question.choices,
        }
        return Response(data, status=status.HTTP_200_OK)

class SubmitAnswerAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, question_id):
        question = get_object_or_404(Question, id=question_id)
        submitted_answer = request.data.get('submitted_answer')
        if not submitted_answer:
            return Response({"error": "Submitted answer is required."}, status=status.HTTP_400_BAD_REQUEST)

        is_correct = submitted_answer == question.correct_answer
        PracticeHistory.objects.create(
            user=request.user,
            question=question,
            submitted_answer=submitted_answer,
            is_correct=is_correct,
        )
        return Response({"is_correct": is_correct}, status=status.HTTP_200_OK)

class UserPracticeHistoryAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        history = PracticeHistory.objects.filter(user=request.user).values(
            'question__title', 'submitted_answer', 'is_correct', 'submitted_at'
        )
        return Response(list(history), status=status.HTTP_200_OK)

class RegisterUserAPI(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response({"error": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists."}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password)
        token, _ = Token.objects.get_or_create(user=user)

        return Response(
            {"message": "User created successfully!", "token": token.key},
            status=status.HTTP_201_CREATED,
        )




class LoginUserAPI(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response({"error": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)

        if not user:
            return Response({"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)

        token, _ = Token.objects.get_or_create(user=user)

        return Response({"message": "Login successful!", "token": token.key}, status=status.HTTP_200_OK)








# from rest_framework import viewsets, status
# from rest_framework.decorators import action
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response

# from .models import Question, PracticeHistory
# from .serializers import (
#     QuestionSerializer, 
#     QuestionSubmitAnswerSerializer,
#     PracticeHistorySerializer
# )

# class QuestionViewSet(viewsets.ReadOnlyModelViewSet):
#     """ViewSet for handling question-related operations"""
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer
#     # permission_classes = [IsAuthenticated]

#     @action(detail=True, methods=['POST'], serializer_class=QuestionSubmitAnswerSerializer)
#     def submit_answer(self, request, pk=None):
#         """
#         Submit an answer for a specific question
#         """
#         # Get the question
#         question = self.get_object()

#         # Validate the submitted answer
#         serializer = self.get_serializer(data=request.data, context={'question': question})
#         serializer.is_valid(raise_exception=True)

#         # Check if the submitted answer is correct
#         submitted_answer = serializer.validated_data['submitted_answer']
#         is_correct = submitted_answer == question.correct_answer

#         # Create practice history record
#         practice_history = PracticeHistory.objects.create(
#             user=request.user,
#             question=question,
#             submitted_answer=submitted_answer,
#             is_correct=is_correct
#         )

#         # Prepare response
#         return Response({
#             'is_correct': is_correct,
#             'correct_answer': question.correct_answer
#         }, status=status.HTTP_200_OK)

# class PracticeHistoryViewSet(viewsets.ReadOnlyModelViewSet):
#     """
#     ViewSet for retrieving user's practice history
#     """
#     serializer_class = PracticeHistorySerializer
#     # permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         """
#         Return practice history only for the authenticated user
#         """
#         return PracticeHistory.objects.filter(user=self.request.user)

#     @action(detail=False, methods=['GET'])
#     def performance_summary(self, request):
#         """
#         Get a summary of the user's performance
#         """
#         # Get all practice history for the user
#         practice_history = PracticeHistory.objects.filter(user=request.user)
        
#         # Calculate performance metrics
#         total_attempts = practice_history.count()
#         correct_attempts = practice_history.filter(is_correct=True).count()
        
#         # Calculate accuracy
#         accuracy = (correct_attempts / total_attempts * 100) if total_attempts > 0 else 0

#         return Response({
#             'total_attempts': total_attempts,
#             'correct_attempts': correct_attempts,
#             'accuracy_percentage': round(accuracy, 2)
#         })