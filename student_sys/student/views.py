from django.shortcuts import render
from .models import Student
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import StudentForm


# Create your views here.

def index(request):
    # words = "World!"
    students = Student.get_all()
    if request.method == "POST":
        form = StudentForm(request.POST)
        print(form)
        if form.is_valid():
            # cleaned_data = form.cleaned_data
            # print(cleaned_data)
            # student = Student()
            # student.name = cleaned_data['name']
            # student.sex = cleaned_data['sex']
            # student.email = cleaned_data['email']
            # student.profession = cleaned_data['profession']
            # student.qq = cleaned_data['qq']
            # student.phone = cleaned_data['phone']
            # student.save()

            form.save()
            print(reverse("index"))
            return HttpResponseRedirect(reverse("index"))
    else:
        form = StudentForm()
    context = {
        "students": students,
        'form': form,
    }
    return render(request, 'student/index.html', context=context)
