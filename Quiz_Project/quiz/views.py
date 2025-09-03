from rest_framework import viewsets
from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import Category, Quiz, Question, Choice, Answer, Result
from .serializers import (
    CategorySerializer,
    QuizSerializer,
    QuestionSerializer,
    ChoiceSerializer,
    AnswerSerializer,
    ResultSerializer
)


# ---- Custom Permissions ---- #
class IsAdminOrReadOnly(BasePermission):
    """Allow only Admins (Profile.role='admin') to create/update/delete.
    Students can only read (GET, HEAD, OPTIONS)."""

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:  # GET, HEAD, OPTIONS
            return True
        return (
            request.user.is_authenticated
            and hasattr(request.user, "profile")
            and request.user.profile.role == "admin"
        )


class IsStudentOnly(BasePermission):
    """Allow only Students to create answers/results (taking quizzes)."""

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and hasattr(request.user, "profile")
            and request.user.profile.role == "student"
        )


# ---- ViewSets ---- #
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsAdminOrReadOnly]


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAdminOrReadOnly]


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = [IsAdminOrReadOnly]


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsStudentOnly]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and hasattr(user, "profile") and user.profile.role == "admin":
            return Answer.objects.all()  # Admin sees all
        return Answer.objects.filter(user=user)  # Student sees only their answers

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    permission_classes = [IsStudentOnly]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and hasattr(user, "profile") and user.profile.role == "admin":
            return Result.objects.all()  # Admin sees all
        return Result.objects.filter(user=user)  # Student sees only their results

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
