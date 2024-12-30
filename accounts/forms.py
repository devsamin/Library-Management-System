from django import forms
from accounts.constants import GENDER_TYPE
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from accounts.models import UserAccountsModel, UserAddressModel
class UserRegistrationForm(UserCreationForm):
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type' : 'date'}))
    street_address = forms.CharField(max_length=30)
    city = forms.CharField(max_length=20)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2',
                  'birth_date', 'gender', 'street_address', 'city', 'postal_code', 'country']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].help_text = None
                
    def save(self, commit = True):
        our_user = super().save(commit=False)

        if commit == True:
            our_user.save()
            birth_date = self.cleaned_data.get('birth_date')
            gender = self.cleaned_data.get('gender')
            street_address = self.cleaned_data.get('street_address')
            city = self.cleaned_data.get('city')
            postal_code = self.cleaned_data.get('postal_code')
            country = self.cleaned_data.get('country')

            UserAccountsModel.objects.create(
                user = our_user,
                birth_date = birth_date,
                gender = gender
            ),

            UserAddressModel.objects.create(
                user = our_user,
                street_address = street_address,
                city = city,
                postal_code = postal_code,
                country = country
            )
        return our_user



