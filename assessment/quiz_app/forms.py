from django.forms import ModelForm
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from .models import QuesModel

class CreateUserForm(ModelForm):
   class Meta:
      model= User
      fields=['username', 'password']

class AddQuesForm(ModelForm):
   class Meta:
      model= QuesModel
      fields="__all__"




