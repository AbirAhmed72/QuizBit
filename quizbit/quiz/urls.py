from django.urls import path
from .views import QuestionListAPI, QuestionDetailAPI, SubmitAnswerAPI, UserPracticeHistoryAPI

urlpatterns = [
    path('questions/', QuestionListAPI.as_view(), name='question-list'),
    path('questions/<int:question_id>/', QuestionDetailAPI.as_view(), name='question-detail'),
    path('questions/<int:question_id>/submit/', SubmitAnswerAPI.as_view(), name='submit-answer'),
    path('practice-history/', UserPracticeHistoryAPI.as_view(), name='practice-history'),
]
