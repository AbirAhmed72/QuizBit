from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from quiz.models import Question, AnswerChoice, PracticeHistory


class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **kwargs):
        # Create a test user (check if it already exists)
        user, created = User.objects.get_or_create(username="testuser")
        if created:
            user.set_password("testpassword")
            user.save()
            self.stdout.write(self.style.SUCCESS(f"User 'testuser' created."))
        else:
            self.stdout.write(self.style.WARNING(f"User 'testuser' already exists."))

        # Check and create questions
        q1, created = Question.objects.get_or_create(
            title="What is the capital of France?",
            defaults={"description": "Select the correct capital city."}
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f"Question '{q1.title}' created."))
        else:
            self.stdout.write(self.style.WARNING(f"Question '{q1.title}' already exists."))

        q2, created = Question.objects.get_or_create(
            title="What is 2 + 2?",
            defaults={"description": "Choose the correct answer."}
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f"Question '{q2.title}' created."))
        else:
            self.stdout.write(self.style.WARNING(f"Question '{q2.title}' already exists."))

        # Check and create answer choices for Question 1
        a1, _ = AnswerChoice.objects.get_or_create(question=q1, choice_text="Paris")
        a2, _ = AnswerChoice.objects.get_or_create(question=q1, choice_text="London")
        a3, _ = AnswerChoice.objects.get_or_create(question=q1, choice_text="Berlin")

        # Check and create answer choices for Question 2
        a4, _ = AnswerChoice.objects.get_or_create(question=q2, choice_text="3")
        a5, _ = AnswerChoice.objects.get_or_create(question=q2, choice_text="4")
        a6, _ = AnswerChoice.objects.get_or_create(question=q2, choice_text="5")

        # Assign correct answers (only if not already assigned)
        if q1.answer is None:
            q1.answer = a1
            q1.save()
            self.stdout.write(self.style.SUCCESS(f"Assigned correct answer '{a1.choice_text}' to question '{q1.title}'."))
        else:
            self.stdout.write(self.style.WARNING(f"Question '{q1.title}' already has a correct answer."))

        if q2.answer is None:
            q2.answer = a5
            q2.save()
            self.stdout.write(self.style.SUCCESS(f"Assigned correct answer '{a5.choice_text}' to question '{q2.title}'."))
        else:
            self.stdout.write(self.style.WARNING(f"Question '{q2.title}' already has a correct answer."))

        # Check and create practice history
        ph1, created = PracticeHistory.objects.get_or_create(
            user=user,
            question=q1,
            defaults={"submitted_answer": "London", "is_correct": False}
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f"Practice history for question '{q1.title}' created."))
        else:
            self.stdout.write(self.style.WARNING(f"Practice history for question '{q1.title}' already exists."))

        ph2, created = PracticeHistory.objects.get_or_create(
            user=user,
            question=q2,
            defaults={"submitted_answer": "4", "is_correct": True}
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f"Practice history for question '{q2.title}' created."))
        else:
            self.stdout.write(self.style.WARNING(f"Practice history for question '{q2.title}' already exists."))

        self.stdout.write(self.style.SUCCESS("Database seeding completed."))
