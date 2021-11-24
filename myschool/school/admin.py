from django.contrib import admin
from .models import Student, Teacher, Parent, Grade, Lesson, Student_lessons, Subject, Subject_grade, Teacher_subject

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'email', 'parent')

class ParentAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'email')

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'email')

admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Parent, ParentAdmin)
admin.site.register(Grade)
admin.site.register(Lesson)
admin.site.register(Subject)
admin.site.register(Student_lessons)
admin.site.register(Subject_grade)
admin.site.register(Teacher_subject)
