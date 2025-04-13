from django import forms
from django.core.exceptions import ValidationError

from money.models import Income, Expense, Category, Files


class IncomeCreateForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['amount', 'category', 'description']

    widgets = {
        'amount': forms.NumberInput(attrs={'class': 'form-control'}),
        'category': forms.Select(attrs={'class': 'form-control'}),
        'description': forms.Textarea(attrs={'class': 'form-control'}),
    }

    def clean(self):
        if 0 >= self.cleaned_data['amount']:
            raise ValidationError('0 dan katta qiymat kiritng ')


class ExpenseCreateForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['amount', 'category', 'description']
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class FilesCreateForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ['name', 'file']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
        }
