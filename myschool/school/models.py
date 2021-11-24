from django.db import models
from django.urls import reverse

# Create your models here.
class Subject(models.Model):
    name = models.CharField(verbose_name="Name", max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'

class Grade(models.Model):
    grade = models.IntegerField(verbose_name='Grade')

    class Meta:
        verbose_name = 'Grade'
        verbose_name_plural = 'Grades'

class Parent(models.Model):
    fname = models.CharField(verbose_name="First name", max_length=150)
    lname = models.CharField(verbose_name="Last name", max_length=150)
    email = models.EmailField(verbose_name="Email")
    # image = models.ImageField(verbose_name="Picture", upload_to='covers', null=True)

    class Meta:
        verbose_name = 'Patent'
        verbose_name_plural = 'Parents'

class Student(models.Model):
    fname = models.CharField(verbose_name="First name", max_length=150)
    lname = models.CharField(verbose_name="Last name", max_length=150)
    email = models.EmailField(verbose_name="Email")
    # image = models.ImageField(verbose_name="Picture", upload_to='covers', null=True)
    parent = models.ForeignKey('Parent', verbose_name='Patent', on_delete=models.SET_NULL, null=True, blank=True, related_name='student')

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

class Teacher(models.Model):
    fname = models.CharField(verbose_name="First name", max_length=150)
    lname = models.CharField(verbose_name="Last name", max_length=150)
    email = models.EmailField(verbose_name="Email")
    # image = models.ImageField(verbose_name="Picture", upload_to='covers', null=True)

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

class Teacher_subject(models.Model):
    teacher = models.ForeignKey('Teacher', verbose_name='Teacher', on_delete=models.CASCADE, null=True, blank=True, related_name='subjects')
    subject = models.ForeignKey('Subject', verbose_name='Subject', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Teacher's subject"
        verbose_name_plural = "Teacher's subjects"

class Subject_grade(models.Model):
    subject = models.ForeignKey('Subject', verbose_name='Subject', on_delete=models.CASCADE, null=True, blank=True)
    grade = models.ForeignKey('Grade', verbose_name='Grade', on_delete=models.CASCADE, null=True, blank=True)
    student = models.ForeignKey('Student', verbose_name='Student', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Subject grade"
        verbose_name_plural = 'Subject grades'

    def get_absolute_url(self):
        """Nurodo konkretaus aprašymo galinį adresą"""
        return reverse('subject-detail', args=[str(self.id)])

class Lesson(models.Model):
    teacher_subject = models.ForeignKey('Teacher_subject', verbose_name='Teacher subject', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'

class Student_lessons(models.Model):
    lesson = models.ForeignKey('Lesson', verbose_name='Lesson', on_delete=models.CASCADE, null=True, blank=True)
    student = models.ForeignKey('Student', verbose_name='Student', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Student lesson'
        verbose_name_plural = 'Student lesssons'




