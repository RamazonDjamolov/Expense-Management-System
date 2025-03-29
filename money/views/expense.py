from django.contrib.auth.decorators import login_required

from money.forms import ExpenseCreateForm
from money.models import Expense
from django.shortcuts import render, redirect


@login_required(login_url='account:login')
def create_expense(request):
    if request.method == "POST":
        form = ExpenseCreateForm(request.POST)
        if form.is_valid():
            form.save(commit=False)

            Expense.objects.create(amount=form.cleaned_data['amount'], category=form.cleaned_data['category'],
                                   description=form.cleaned_data['description'], user_id=request.user)
            return redirect('money:expense_list')
        return render(request, template_name='expense/create.html', context={
            'form': form
        })
    form = ExpenseCreateForm()
    return render(request, template_name='expense/create.html', context={
        'form': form
    })


def list_expenses(request):
    expense = Expense.objects.all().filter(user_id=request.user)
    return render(request, template_name='expense/list.html', context={
        'expense': expense
    })
