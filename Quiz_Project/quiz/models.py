from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Quiz(models.Model):
    title = models.CharField(max_length=100)
    decription = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="quizzes")
    
    def __str__(self):
        return self.title
    
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
    content = models.TextField()
    
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
