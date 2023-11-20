from django import forms
from django.contrib.auth.forms import UserCreationForm 
from ..models import User
CITY_CHOICES=[
    ('', 'Select City'),
    ('lhr','lahore'),
    ('isl','islamabad'),
    ('mul','multan'),
    ('rwal','rawalpindy'),
]
class createform(UserCreationForm):
    city = forms.ChoiceField(choices=CITY_CHOICES)

    class Meta:
        model = User
        fields = ('username','password1', 'password2','email','phone','city')

    def __init__(self, *args, **kwargs):
        super(createform,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'FullName'
        self.fields['username'].widget.attrs['class'] = 'form-control  py-3 bg-body-tertiary  '

        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['email'].widget.attrs['class'] = 'form-control  py-3 bg-body-tertiary  '

        self.fields['city'].widget.attrs['class'] = 'form-select form-control   py-3  bg-body-tertiary select_oder'

        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].widget.attrs['class'] = 'form-control  py-3 bg-body-tertiary    maxlength="10"'
        
        self.fields['password2'].widget.attrs['placeholder'] = 'confirm_Password'
        self.fields['password2'].widget.attrs['class'] = 'form-control  py-3 bg-body-tertiary   maxlength="10"'

        self.fields['phone'].widget.attrs['placeholder'] = 'contact no*'
        self.fields['phone'].widget.attrs['class'] = 'form-control  py-3 bg-body-tertiary'