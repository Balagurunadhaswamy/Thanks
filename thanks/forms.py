# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm


# class UserForm(UserCreationForm):
#     first_name = forms.CharField()
#     last_name = forms.CharField()
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ('first_name', 'email' )


from django.forms import ModelForm
from .models import customer

class CustomerForm(ModelForm):
    class Meta:
        model = customer
        fields = '__all__'