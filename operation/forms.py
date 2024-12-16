
from django import forms

class ResgisterationForm(forms.Form):

    email=forms.EmailField()

    username=forms.CharField()

    password1=forms.CharField()

    password2=forms.CharField()

    ROLE_CHOICES=(
        ("admin","admin"),
        ("staff","staff")
    )

    role=forms.ChoiceField(choices=ROLE_CHOICES)

    GENDER_OPTIONS=(
        ("male","male"),
        ("female","female")
    )
    



class BmiForm(forms.Form):

    height=forms.IntegerField()

    weight=forms.IntegerField()