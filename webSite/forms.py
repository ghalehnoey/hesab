from django import forms
#from captcha.fields import ReCaptchaField

class RegistrationForm(forms.Form):
    # Your form fields...
#    captcha = ReCaptchaField()
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    # Add any other fields you want for registration
