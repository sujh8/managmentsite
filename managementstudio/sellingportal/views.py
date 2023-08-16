from django.shortcuts import render
from django.http import HttpResponse
from sellingportal import models
from sellingportal import forms
#from sellingportal import addStudentForm 
# Create your views here.
def Index(request):
    context={'name':'mona',
             'age':25,
             'jobs': ['eng','dev']
             }
    return render(request,'index.html',context)
    #return HttpResponse('welcome')


def Student(request):
    students=models.Student.objects.all()
    context={
        'students' :students
    }
    return render(request,'students.html',context)


def StudentDegree(request, student_id):
     degrees=models.Degree.objects.filter(student_id=student_id)
     students=models.Student.objects.get(id=student_id)
     form_data = forms.DegreeRegistrar(request.POST or None)
     msg=''
     if form_data.is_valid():
             degree=models.Degree()
             degree.student_degree=form_data.cleaned_data['student_degree']
             degree.student_id=students
             degree.save()
             msg='data is saved'
     context={
        'degrees' :degrees,
        'formregister':form_data,
        'msg':msg
             }
     return render(request,'degrees.html',context)  
 
def Register(request):
     form_data = forms.UserRegistrar(request.POST or None)
     msg=''
     if form_data.is_valid():
             student=models.Student()
             student.first_name=form_data.cleaned_data['first_name']
             student.last_name=form_data.cleaned_data['last_name']
             student.age=form_data.cleaned_data['age']
             student.date_birth=form_data.cleaned_data['date_birth']
             student.save()
             msg='data is saved'
     context={
         'formregister':form_data,
         'msg':msg
     }
     return render(request,'Regiester.html',context)
     '''
     if form_data.is_valid():
             student=models.Student()
             student.first_name=form_data.cleaned_data['first_name']
             student.last_name=form_data.cleaned_data['last_name']
             student.age=form_data.cleaned_data['age']
             student.date_birth=form_data.cleaned_data['date_birth']
             student.save();
        '''     
         