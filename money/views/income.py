from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from money.forms import IncomeCreateForm
from money.models import Income
from django.db.models import Q
from django.core.paginator import Paginator


# Create your views here.

@login_required(login_url='account:login')
def income_list_view(request):
    incomes = Income.objects.all().filter(user_id=request.user.id)
    q = request.GET.get('q', "")

    if q:
        incomes = Income.objects.filter(
            Q(amount__icontains=q) | Q(category__name__icontains=q) & Q(user_id=request.user.id))

    paginator = Paginator(incomes, 5)
    page = request.GET.get('page')
    incomes = paginator.get_page(page)

    return render(request, template_name='income/list.html', context={
        'incomes': incomes,
        'q': q

    })


def income_create_view(request):
    if request.method == "POST":
        form = IncomeCreateForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            Income.objects.create(amount=form.cleaned_data['amount'], category=form.cleaned_data['category'],
                                  description=form.cleaned_data['description'], user_id=request.user)
            return redirect('money:income_list')
        return render(request, template_name='income/create.html', context={
            'form': form,
        })
    form = IncomeCreateForm()
    return render(request, template_name='income/create.html', context={
        'form': form,
    })


def Income_update(request, income_id):
    if request.method == "POST":
        income = Income.objects.get(id=income_id)
        form = IncomeCreateForm(request.POST, instance=income)
        print(form.is_valid(), "my validatsiya")
        if form.is_valid():
            form.save()
            return redirect('money:income_list')
        return render(request, template_name='income/edit.html', context={
            'form': form,
            'income': income,
        })

    income = Income.objects.get(id=income_id)
    form = IncomeCreateForm(instance=income)
    return render(request, template_name='income/edit.html', context={
        'form': form,
        'income': income,
    })


def Income_delete(request, income_id):
    income = Income.objects.get(id=income_id).delete()
    return redirect('money:income_list')
