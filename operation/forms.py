
from django import forms

class ResgisterationForm(forms.Form):

    email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control mb-2"}))

    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-2"}))

    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mb-2"}))

    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mb-2"}))

    ROLE_CHOICES=(
        ("admin","admin"),
        ("staff","staff")
    )

    role=forms.ChoiceField(choices=ROLE_CHOICES,widget=forms.Select(attrs={"class":"form-control form-select"}))

    GENDER_OPTIONS=(
        ("male","male"),
        ("female","female")
    )
    



class BmiForm(forms.Form):

    height=forms.IntegerField()

    weight=forms.IntegerField()

class MilageForm(forms.Form):

    distance=forms.IntegerField()

    consumption=forms.IntegerField()

    

class CalorieForm(forms.Form):

    weight=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))

    height=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))

    age=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))

    GENDER_CHOICES=(
        ("male","MALE"),
        ("female","FEMALE"),

    )

    gender=forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.Select(attrs={"class":"form-control form-select mb-2"}))

    ACTIVITY_CHOICES=(
        (1.2,"SEDENTARY"),
        (1.375,"LIGHTLY ACTIVE"),
        (1.55,"MODERATLY ACTIVE"),
        (1.725,"VERY ACTIVE"),
        (1.9,"EXTRA ACTIVE")
    )

    activity=forms.ChoiceField(choices=ACTIVITY_CHOICES,widget=forms.Select(attrs={"class":"form-control form-select mb-2"}))
