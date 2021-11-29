from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('students/', views.students, name='students'),
    path('teachers/', views.teachers, name='teachers'),
    path('teachers/<int:teacher_id>', views.teacher, name='teacher'),
    path('search/', views.search, name='search'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('lessons/', views.LessonListView.as_view(), name='lessons'),
    path('subjectgrades/', views.SubjectgradeListView.as_view(), name='subjectgrades'),
    path('mygrades/', views.GradesByUserListView.as_view(), name='my-grades'),

]
