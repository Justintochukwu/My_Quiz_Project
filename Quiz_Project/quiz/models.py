from django.db import models
from django.contrib.auth.models import User


# Extend User with a role (optional helper, still uses Django Groups/Permissions)
class Profile(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Admin'),      # Can create/manage quizzes
        ('student', 'Student'),  # Can take quizzes
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')

    def __str__(self):
        return f"{self.user.username} ({self.role})"


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Quiz(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="quizzes")
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="created_quizzes",
        null=True,   # ✅ allow null for old rows
        blank=True,  # ✅ allow blank in forms
    )

    class Meta:
        permissions = [
            ("can_create_quiz", "Can create a new quiz"),
            ("can_edit_quiz", "Can edit an existing quiz"),
        ]

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
    content = models.TextField()

    class Meta:
        permissions = [
            ("can_add_question", "Can add questions to a quiz"),
        ]

    def __str__(self):
        return self.content[:50]


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
    content = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.content


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="answers")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    selected_choice = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name="answers")
    answered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} → {self.question.content[:30]}"


class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="results")
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="results")
    score = models.IntegerField()
    date_taken = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.quiz.title}: {self.score}"
