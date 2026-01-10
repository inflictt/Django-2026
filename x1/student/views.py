from django.shortcuts import render,redirect,HttpResponse
from .forms import StudentForm
from .models import Student
# Create your views here.
def student_create(request):    
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'student/student_sucess.html', {'form': form})
    else:
        form = StudentForm() 
    return render(request, 'student/student_form.html', {'form': form})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student/student_list.html', {'students': students})

def student_edit(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
        return redirect('student_list')
    
def student_delete(request, pk):
    if request.method == 'POST':
        student = Student.objects.get(pk=pk)
        student.delete()
        return redirect('student_list') 