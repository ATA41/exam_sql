from django.db import models
from datetime import timedelta


class Language(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    month_to_learn = models.IntegerField()

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class AbstractPerson(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(unique=True)
    phone = models.CharField(max_length=13)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if len(self.phone) == 10 and self.phone.startswith("0"):
            self.phone = "+996" + self.phone[1:]
        super().save(*args, **kwargs)


class Student(AbstractPerson):
    work_study_place = models.CharField(max_length=50, null=True, blank=True)
    has_own_notebook = models.BooleanField()
    preferred_os = models.CharField(choices=(
        ("windows", "Windows"),
        ("linux", "Linux"),
        ("mac", "Mac"),
    ))

    def __str__(self):
        return self.name


class Mentor(AbstractPerson):
    main_work = models.CharField(max_length=50, null=True, blank=True)
    experience = models.DateField()
    students = models.ManyToManyField(Student, through="Course")

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    date_started = models.DateField()
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def get_end_field(self):
        month = self.language.month_to_learn
        return self.date_started + timedelta(days=30 * month)

    def __str__(self):
        return self.name



