from user.models import *

python = Language(name="Python", month_to_learn=6)
python.save()
javascript = Language(name="JavaScript", month_to_learn=6)
javascript.save()
uiux = Language(name="UI-UX design", month_to_learn=2)
uiux.save()
student = Student(name="Amanov Aman", email="aman@mail.ru", phone="+996700989898", work_study_place="Shool #13",
                  has_own_notebook=True, preferred_os="Windows")
student.save()
student2 = Student(name="Apina Alena", email="aapina@bk.ru", phone="0550888888", work_study_place="TV",
                   has_own_notebook=True, preferred_os="Mac")
student2.save()
student3 = Student(name="Phil Spencer", email="spencer@microsoft.com", phone="0508312312",
                   work_study_place="Microsoft Gaming", has_own_notebook=False, preferred_os="Linux")
student3.save()
mentor = Mentor(name="Ilona Maskova", email="imask@gmail.com", phone="0500545454", main_work="",
                experience="2021-10-23")
mentor.save()
mentor2 = Mentor(name="Halil Nurmuhametov", email="halil@gmail.com", phone="0709989876",
                 main_work="University of Fort Collins", experience="2021-09-18")
mentor2.save()
student1 = Student.objects.get(name="Amanov Aman")
student2 = Student.objects.get(name="Apina Alena")
mentor = Mentor.objects.get(name="Halil Nurmuhametov")
python = Language.objects.get(name="Python")
course = Course(name="Python-21", language=python, date_started="2022-08-01", mentor=mentor, student=student1)
course.save()
course = Course(name="Python-21", language=python, date_started="2022-08-01", mentor=mentor, student=student2)
course.save()
mentor2 = Mentor.objects.get(name="Ilona Maskova")
student3 = Student.objects.get(name="Phil Spencer")
ux = Language.objects.get(name="Ui-Ux Design")
course2 = Course(name="UXUI design-43", language=ux, date_started="2022-08-22", mentor=mentor2, student=student3)
course2.save()
