# from rest_framework import serializers
# from .models import Question, PracticeHistory
# from django.contrib.auth.models import User

# class QuestionSerializer(serializers.ModelSerializer):
#     """Serializer for Question model"""
#     class Meta:
#         model = Question
#         fields = ['id', 'title', 'description', 'choices', 'created_at']
#         read_only_fields = ['created_at']

# class QuestionSubmitAnswerSerializer(serializers.Serializer):
#     """Serializer for submitting an answer to a question"""
#     submitted_answer = serializers.CharField(max_length=255)

#     def validate_submitted_answer(self, value):
#         """
#         Validate that the submitted answer is one of the valid choices
#         """
#         question = self.context.get('question')
#         if not question:
#             raise serializers.ValidationError("Question context is missing")
        
#         # Validate against the choices in the question
#         if value not in question.choices:
#             raise serializers.ValidationError("Invalid answer choice")
        
#         return value

# class PracticeHistorySerializer(serializers.ModelSerializer):
#     """Serializer for PracticeHistory model"""
#     question_title = serializers.CharField(source='question.title', read_only=True)
    
#     class Meta:
#         model = PracticeHistory
#         fields = ['id', 'question', 'question_title', 'submitted_answer', 'is_correct', 'submitted_at']
#         read_only_fields = ['is_correct', 'submitted_at']
        
        
# # class AnswerSerializer(serializers.Serializer):
# #     choice = serializers.CharField()
    
    