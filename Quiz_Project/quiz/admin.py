from django.contrib import admin
from .models import Category, Quiz, Question, Choice, Answer, Result


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ("title", "category")
    search_fields = ("title",)
    list_filter = ("category",)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("content", "quiz")
    search_fields = ("content",)
    list_filter = ("quiz",)


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("content", "question", "is_correct")
    search_fields = ("content",)
    list_filter = ("question", "is_correct")


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("user", "question", "selected_choice", "answered_at")
    list_filter = ("user", "question")


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ("user", "quiz", "score", "date_taken")
    list_filter = ("user", "quiz")
