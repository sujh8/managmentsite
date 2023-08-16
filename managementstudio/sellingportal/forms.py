from tkinter.tix import Form
from django import forms 
    
class UserRegistrar(forms.Form):  
    first_name= forms.CharField(required=True, widget=forms.TextInput())
    last_name= forms.CharField(required=True, widget=forms.TextInput())
    age= forms.CharField(required=True,widget=forms.TextInput())
    date_birth= forms.CharField(required=True,widget=forms.TextInput())
    
class DegreeRegistrar(forms.Form):  
    student_degree= forms.CharField(required=True, widget=forms.TextInput())
    