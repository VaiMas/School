from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
# from .forms import CustomUserChangeForm, ProfileUpdateForm
from django.contrib import messages
from django . http import HttpResponse
from . models import Teacher_subject, Subject_grade, Lesson
from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
User = get_user_model()

def index(request):
    return render(request, 'index.html')

# @login_required
# def profile(request):
#     if request.method == "POST":
#         u_form = CustomUserChangeForm(request.POST, instance=request.user)
#         p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             messages.success(request, f"Profile updated")
#             return redirect('profile')
#     else:
#         u_form = CustomUserChangeForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)
#
#     context = {
#         'u_form': u_form,
#         'p_form': p_form,
#     }
#     return render(request, 'profile.html', context)

class TeachersListView(generic.ListView):
    model = User
    template_name = 'teachers.html'
    context_object_name = 'teachers_list'
    paginate_by = 1
    queryset = User.objects.filter(user_type='T')
#
#
# def students(request):
#    students = Student.objects.all()
#    context = {
#          'students': students
#      }
#    return render(request, 'student.html', context=context)

# def teachers(request):
#     teachers = Teacher.objects.all()
#     subjects = Teacher_subject.objects.all()
#     context = {
#         'teachers': teachers,
#         'subjects': subjects
#     }
#     return render(request, 'teachers.html', context=context)
#
# def teacher(request, teacher_id):
#     single_teacher = get_object_or_404(Teacher, pk=teacher_id)
#     return render(request, 'teacher.html', {'teacher': single_teacher})
#
class LessonListView(generic.ListView):
    model = Lesson
    paginate_by = 1
    template_name = 'lessons.html'
#
# class SubjectgradeListView(generic.ListView):
#     model = Subject_grade
#     template_name = 'subject_grade.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(SubjectgradeListView, self).get_context_data(**kwargs)
#         context['teacher'] = Teacher.objects.all().first()
#         # And so on for more models
#         return context
#
#
#
# class StudentDetailView(generic.DetailView):
#     model = Student
#     paginate_by = 1
#     template_name = 'student.html'
#
#     # def get_context_data(self, **kwargs):
#     #     # Call the base implementation first to get a context
#     #     context = super().get_context_data(**kwargs)
#     #     # Add in a QuerySet of all the books
#     #     context['parent_list'] = Parent.objects.all()
#     #     return context
#
# def search(request):
#     query = request.GET.get('query')
#     search_results = Student.objects.filter(Q(fname__icontains=query) | Q(lname__icontains=query))
#     return render(request, 'search.html', {'students': search_results, 'query': query})
#
class GradesByUserListView(LoginRequiredMixin, generic.ListView):
    model = Subject_grade
    template_name = 'user_grades.html'

    def get_queryset(self):
        return Subject_grade.objects.filter(student=self.request.user).filter()


    def get_context_data(self, **kwargs):
        context = super(GradesByUserListView, self).get_context_data(**kwargs)
        context['teacher'] = User.objects.filter(user_type='T').first().lname
        # And so on for more models
        return context

