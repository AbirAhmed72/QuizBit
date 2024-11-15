from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Question, PracticeHistory
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

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
