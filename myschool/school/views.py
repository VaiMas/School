from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, permission_required
from .forms import UserUpdateForm, ProfileUpdateForm, NewGradeForm
from django.contrib import messages
from django.http import HttpResponse
from .models import Subject_grade, Lesson, CustomUser, Subject
from django.views import generic
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q, F
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
import json


User = get_user_model()


def index(request):
    return render(request, 'index.html')


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Profile updated")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'profile.html', context)


class TeachersListView(generic.ListView):
    model = User
    template_name = 'teachers.html'
    context_object_name = 'teachers_list'
    paginate_by = 5
    queryset = User.objects.filter(user_type='T')

def teacher(request, teacher_id):
    single_car = get_object_or_404(User.objects.filter(user_type='T'), pk=teacher_id)
    return render(request, 'teacher.html', {'teacher': single_car})


class LessonListView(generic.ListView):
    model = Lesson
    paginate_by = 1
    template_name = 'lessons.html'


def search(request):
    query = request.GET.get('query')
    search_results = User.objects.filter(Q(fname__icontains=query) | Q(lname__icontains=query))
    return render(request, 'search.html', {'users': search_results, 'query': query})


class GradesByUserListView(LoginRequiredMixin, generic.ListView):
    model = Subject_grade
    template_name = 'user_grades.html'
    paginate_by = 5

    def get_queryset(self):
        return Subject_grade.objects.filter(student=self.request.user)


class GradeByUserCreateView(LoginRequiredMixin, generic.CreateView):
    model = Subject_grade
    success_url = "/school/mylessons/"
    template_name = 'new_grade.html'
    form_class = NewGradeForm

class GradeByUserUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Subject_grade
    success_url = "/school/mylessons/"
    template_name = 'edit_grade.html'
    form_class = NewGradeForm


    def test_func(self):
        return self.request.user

class GradeByUserDelateView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Subject_grade
    success_url = "/school/mylessons/"
    template_name = 'delete_grade.html'


    def test_func(self):
        return self.request.user

from collections import defaultdict

class LessonsByUserListView(LoginRequiredMixin, generic.ListView):
    model = User
    template_name = 'user_lessons.html'
    context_object_name = "subject_list"
    queryset = Subject_grade.objects.all()
    # paginate_by = Paginator(Subject_grade.objects.all(), 5)

    # def listing(request):
    #     contact_list = Subject_grade.objects.all()
    #     print(contact_list)
    #     print('abs')
    #     paginator = Paginator(contact_list, 5)  # Show 25 contacts per page.
    #
    #     page_number = request.GET.get('page')
    #     page_obj = paginator.get_page(page_number)
    #     return render(request, 'user_lessons', {'page_obj': page_obj})

    # def get_queryset(self):
    #     return Subject_grade.objects.all()
    #
    # def get_paginate_by(self, queryset):
    #     paginator = Paginator(queryset, 5)
    #     print(paginator)
    #     return 5

    paginate_by = 5

    def get_paginate_by(self, queryset):
        return self.request.GET.get("paginate_by", self.paginate_by)

    # def get(self, request):
    #
    #     data = Subject_grade.objects.all()
    #
    #     paginator = Paginator(data, 5)
    #     page = request.GET.get('page')
    #
    #     try:
    #         paginated = paginator.get_page(page)
    #     except PageNotAnInteger:
    #         paginated = paginator.get_page(1)
    #     except EmptyPage:
    #         paginated = paginator.page(paginator.num_pages)
    #
    #     return render(request, self.template_name, {'DataPaginated': paginated, 'paginate_by': 5})

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teacher'] = self.request.user
        return context


# def get_subject(request):
#     if request.method == "POST":
#         id_subject = {}
#         subjects = Subject.objects.filter(user=request.POST['user_pk'])
#         for each in subjects:
#             id_subject[each.id] = each.subject
#         return HttpResponse(json.dumps(id_subject), content_type='application/json')



