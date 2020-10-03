from django import forms
from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField
from django.contrib.auth import authenticate
from phonenumber_field.formfields import PhoneNumberField

from .phone_backend import PhoneBackend
from .models import Product, Account


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [ 'name', 'description', 'price', 'qty', 'color', 'size']


class RegistrationForm(UserCreationForm):
        phone = PhoneNumberField()

        class Meta:
            model = Account
            fields = ['username', 'phone', 'password1', 'password2']

        def save(self, commit=True):
            user = super(RegistrationForm, self).save(commit=False)
            user.username = self.cleaned_data['username']
            user.phone = self.cleaned_data['phone']
            user.set_password(self.cleaned_data["password1"])
            if commit:
                user.save()
            return user


class AccountAuthenticationForm(forms.ModelForm):
        password = forms.CharField(label='Password', widget=forms.PasswordInput)

        class Meta:
            model = Account
            fields = ['username', 'password']

        def clean(self):
            if self.is_valid():
                username = self.cleaned_data['username']
                password = self.cleaned_data['password']
                if not authenticate(username=username, password=password):
                    raise forms.ValidationError("Invalid login")


class CustomerAccountAuthenticationForm(forms.ModelForm):
        otp     = forms.IntegerField(label='OTP', widget=forms.NumberInput)
        phone   = PhoneNumberField()

        class Meta:
            model = Account
            fields = ['phone', 'otp']

        def clean(self):
            if self.is_valid():
                phone = self.cleaned_data['phone']
                otp = self.cleaned_data['otp']
                #print ("Forms view {} {}".format(phone,otp))
                if not PhoneBackend.authenticate(username=phone, input_OTP=otp, actual_OTP=otp):
                    raise forms.ValidationError("Invalid login")


class UserAdminCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    #phone = PhoneNumberField()
    #phone = forms.CharField(label='Phone', widget=forms.NumberInput)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('username', 'password')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Account
        fields = ('username', 'phone', 'password', 'is_active', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
