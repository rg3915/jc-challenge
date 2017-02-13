from django import forms
from .models import Company, Person, Status, Product


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = '__all__'


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = '__all__'


class StatusForm(forms.ModelForm):

    class Meta:
        model = Status
        fields = '__all__'


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
