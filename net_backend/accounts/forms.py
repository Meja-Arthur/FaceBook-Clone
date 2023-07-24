# creating a form so that django can handle the validation of the signup

from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'name','password1','password2')