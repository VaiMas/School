from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('students/', views.students, name='students'),
    path('teachers/', views.teachers, name='teachers'),
    path('teachers/<int:teacher_id>', views.teacher, name='teacher'),
    path('lessons/', views.LessonListView.as_view(), name='lessons'),
    path('subjectgrades/', views.SubjectgradeListView.as_view(), name='subjectgrades'),

]
