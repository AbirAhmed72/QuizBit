from django.urls import path
from .views import LoginUserAPI, QuestionListAPI, QuestionDetailAPI, RegisterUserAPI, SubmitAnswerAPI, UserPracticeHistoryAPI

urlpatterns = [
    path('register/', RegisterUserAPI.as_view(), name='register_user'),
    path('login/', LoginUserAPI.as_view(), name='login_user'),
    path('questions/', QuestionListAPI.as_view(), name='question-list'),
    path('questions/<int:question_id>/', QuestionDetailAPI.as_view(), name='question-detail'),
    path('questions/<int:question_id>/submit/', SubmitAnswerAPI.as_view(), name='submit-answer'),
    path('practice-history/', UserPracticeHistoryAPI.as_view(), name='practice-history'),
]


# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import QuestionViewSet, PracticeHistoryViewSet

# # Create a router and register viewsets
# router = DefaultRouter()
# router.register(r'questions', QuestionViewSet, basename='question')
# router.register(r'practice-history', PracticeHistoryViewSet, basename='practice-history')

# urlpatterns = [
#     # Include router URLs
#     path('', include(router.urls)),
# ]

# Example additional configuration in project's main urls.py
# from django.urls import path, include
# 
# urlpatterns = [
#     path('api/v1/', include('quizbit.urls')),
# ]