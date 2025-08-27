from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class quiz(models.Model):
    title = models.CharField(max_length=100)
    decription = models.TextField(blank=True)
    category = models.ForeignKey(category, on_delete=models.CASCADE, related_name="quizzes")
    
    def __str__(self):
        return self.title
    
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
    content = models.TextField()
    
    def __str__(self):
        return self.content[:50]