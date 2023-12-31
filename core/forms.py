from django.contrib.auth.forms import UserCreationForm
from core.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']