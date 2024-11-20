from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import AnswerChoice, Question, PracticeHistory
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


class QuestionListAPI(APIView):
    """
    API to retrieve a list of all questions and their answer choices.
    """
    permission_classes = [AllowAny]

    def get(self, request):
        questions = Question.objects.prefetch_related('answerchoice_set').all()
        data = [
            {
                "id": question.id,
                "title": question.title,
                "description": question.description,
                "choices": [
                    {"id": choice.id, "text": choice.choice_text}
                    for choice in question.answerchoice_set.all()
                ],
            }
            for question in questions
        ]
        return Response(data, status=status.HTTP_200_OK)


class QuestionDetailAPI(APIView):
    """
    API to retrieve details of a specific question by ID.
    """
    permission_classes = [AllowAny]

    def get(self, request, question_id):
        question = get_object_or_404(Question, id=question_id)
        choices = question.answerchoice_set.all()

        data = {
            "id": question.id,
            "title": question.title,
            "description": question.description,
            "choices": [
                {"id": choice.id, "text": choice.choice_text}
                for choice in choices
            ],
            "created_at": question.created_at,
        }
        return Response(data, status=status.HTTP_200_OK)


class SubmitAnswerAPI(APIView):
    """
    API to submit an answer for a specific question.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, question_id):
        question = get_object_or_404(Question, id=question_id)
        submitted_choice_id = request.data.get('submitted_answer_id')

        if not submitted_choice_id:
            return Response({"error": "Submitted answer ID is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            submitted_choice = AnswerChoice.objects.get(id=submitted_choice_id, question=question)
        except AnswerChoice.DoesNotExist:
            return Response({"error": "Invalid answer choice for this question."}, status=status.HTTP_400_BAD_REQUEST)

        is_correct = submitted_choice == question.answer
        PracticeHistory.objects.create(
            user=request.user,
            question=question,
            submitted_answer=submitted_choice.choice_text,
            is_correct=is_correct,
        )
        return Response({"is_correct": is_correct}, status=status.HTTP_200_OK)


class UserPracticeHistoryAPI(APIView):
    """
    API to retrieve the practice history of the authenticated user.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        history = PracticeHistory.objects.filter(user=request.user).values(
            'question__title', 'submitted_answer', 'is_correct', 'submitted_at'
        )
        return Response(list(history), status=status.HTTP_200_OK)


class RegisterUserAPI(APIView):
    """
    API to register a new user.
    """
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
    """
    API to log in an existing user.
    """
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
