from django.shortcuts import render
from .models import Income
from django.db.models import Q
from django.core.paginator import Paginator


# Create your views here.


def income_list_view(request):
    incomes = Income.objects.all().filter(user_id=request.user.id)
    q = request.GET.get('q', "")

    if q:
        incomes = Income.objects.filter(
            Q(amount__icontains=q) | Q(category__name__icontains=q) & Q(user_id=request.user.id))

    paginator = Paginator(incomes, 3)
    page = request.GET.get('page')
    incomes = paginator.get_page(page)

    return render(request, template_name='income/list.html', context={
        'incomes': incomes,
        'q': q

    })
