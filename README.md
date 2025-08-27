📘 Quiz API

A RESTful API built with Django + Django REST Framework (DRF) that allows users to take quizzes, submit answers, and track results.
The database design follows the ERD with entities: User, Category, Quiz, Question, Choice, Answer, Result.

🛠 Tech Stack

Backend: Django, Django REST Framework

Database: SQLite (default) or PostgreSQL/MySQL

Authentication: Django’s built-in User model

📂 Database Design (ERD)
Entities

User → provided by Django’s auth.User

Category → groups quizzes (e.g., Math, Science)

Quiz → belongs to a category, contains questions

Question → belongs to a quiz, has multiple choices

Choice → possible answers for a question (one is correct)

Answer → stores a user’s selected choice for a question

Result → stores a user’s overall score for a quiz

Relationships

Category → Quiz → Question → Choice

User → Answer → Question

User → Result → Quiz

📌 API Endpoints (planned)
Method	Endpoint	Description
GET	/api/categories/	List all categories
POST	/api/categories/	Create a new category
GET	/api/quizzes/	List quizzes (optionally by category)
POST	/api/quizzes/	Create a new quiz
GET	/api/questions/	List questions for a quiz
POST	/api/questions/	Create a question
GET	/api/choices/	List choices for a question
POST	/api/choices/	Add a choice to a question
POST	/api/answers/	Submit an answer to a question
GET	/api/results/	View quiz results for a user