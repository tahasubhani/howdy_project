
from django import forms
from  ..models import Order
CITY_CHOICES=[
    ('', 'Select City'),
    ('lhr','lahore'),
    ('isl','islamabad'),
    ('mul','multan'),
    ('rwal','rawalpindy'),
]
class Orderform(forms.ModelForm):
    city = forms.ChoiceField(choices=CITY_CHOICES)

    class Meta:
        model= Order
        fields =('__all__')
        exclude = ('user','oders_amount','payment_mode','city')

    def __init__(self, *args, **kwargs):
        super(Orderform,self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'first_name'
        self.fields['first_name'].widget.attrs['class'] ='form-control py-3 bg-body-tertiary '

        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['email'].widget.attrs['class'] ='form-control py-3 bg-body-tertiary  input-borderr'

        self.fields['city'].widget.attrs['class'] ='form-select form-control   py-3  bg-body-tertiary  select_oder' 
        
        self.fields['phone'].widget.attrs['placeholder'] = 'phone*'
        self.fields['phone'].widget.attrs['class'] ='form-control  py-3 bg-body-tertiary  input-borderr'

        self.fields['address'].widget.attrs['placeholder'] = 'Full-address'
        self.fields['address'].widget.attrs['class'] ='form-control   py-3 bg-body-tertiary  input-borderr'

        self.fields['Special_Instructions'].widget.attrs['placeholder'] = 'special Instruction'

        self.fields['Special_Instructions'].widget.attrs['class'] ='form-control   py-3 bg-body-tertiary  input-borderr'
