from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from users.models import UserProfile


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(required=True,
                                label=_('Password', ),
                                strip=False,
                                help_text=password_validation.password_validators_help_text_html(),
                                widget=forms.PasswordInput(
                                    attrs={"class": "form-control", "autocomplete": "new-password"}), )
    password2 = forms.CharField(required=True,
                                label=_("Password confirmation"),
                                strip=False,
                                help_text=_("Enter the same password as before, for verification."),
                                widget=forms.PasswordInput(
                                    attrs={"class": "form-control", "autocomplete": "new-password"}), )

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.error_messages["already_taken"] = _("This account is already taken.")

    def get_already_taken_error(self):
        return ValidationError(self.error_messages['already_taken'],
                               code='already_taken',
                               params={'email': UserProfile._meta.get_field(UserProfile.USERNAME_FIELD)})

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if UserProfile.objects.filter(email=email).exists():
            raise self.get_already_taken_error()
        return email

    def _post_clean(self):
        super()._post_clean()
        password = self.cleaned_data.get("password2")
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error("password1", error)

    class Meta:
        model = UserProfile
        fields = ("email",)
