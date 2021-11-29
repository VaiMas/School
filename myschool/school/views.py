from django.shortcuts import render, get_object_or_404
from django . http import HttpResponse
from . models import Student, Teacher, Teacher_subject, Subject_grade, Lesson, Parent
from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    return render(request, 'index.html')


def students(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'student.html', context=context)

def teachers(request):
    teachers = Teacher.objects.all()
    subjects = Teacher_subject.objects.all()
    context = {
        'teachers': teachers,
        'subjects': subjects
    }
    return render(request, 'teachers.html', context=context)

def teacher(request, teacher_id):
    single_teacher = get_object_or_404(Teacher, pk=teacher_id)
    return render(request, 'teacher.html', {'teacher': single_teacher})

class LessonListView(generic.ListView):
    model = Lesson
    paginate_by = 1
    template_name = 'lessons.html'

class SubjectgradeListView(generic.ListView):
    model = Subject_grade
    template_name = 'subject_grade.html'

class StudentDetailView(generic.DetailView):
    model = Student
    paginate_by = 1
    template_name = 'student.html'

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     context['parent_list'] = Parent.objects.all()
    #     return context

def search(request):
    query = request.GET.get('query')
    search_results = Student.objects.filter(Q(fname__icontains=query) | Q(lname__icontains=query))
    return render(request, 'search.html', {'students': search_results, 'query': query})

class GradesByUserListView(LoginRequiredMixin, generic.ListView):
    model = Subject_grade
    template_name = 'user_grades.html'

    def get_queryset(self):
        return Subject_grade.objects.filter(student__email=self.request.user).filter()

