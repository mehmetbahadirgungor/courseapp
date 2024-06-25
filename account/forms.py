from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import TextInput, PasswordInput

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].widget = TextInput(attrs={'class': 'form-control mb-3',})
        self.fields['password'].widget = PasswordInput(attrs={'class': 'form-control mb-4',})

class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].widget = TextInput(attrs={'class': 'form-control mb-3',})
        self.fields['username'].help_text = ""
        self.fields['password1'].widget = PasswordInput(attrs={'class': 'form-control',})
        self.fields['password2'].widget = PasswordInput(attrs={'class': 'form-control mb-4',})
        self.fields['password2'].help_text = ""