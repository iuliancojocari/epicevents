from django import forms
from django.core.exceptions import ValidationError
from .models import User


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={"class": "vTextField"})
    )
    confirm_password = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={"class": "vTextField"}),
    )

    class Meta:
        model = User
        fields = "__all__"

    def clean_confirm_password(self):
        password = self.cleaned_data["password"]
        confirm_password = self.cleaned_data["confirm_password"]
        if password != confirm_password:
            raise ValidationError("Password don't match.")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
