from money.models import Expense
from django.shortcuts import render, redirect


def create_expense(request):
    return render(request, template_name='expense/create.html')
