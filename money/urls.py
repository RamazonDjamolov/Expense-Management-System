from django.shortcuts import render
from django.urls import path
from .views import income_list_view, income_create_view, Income_update

app_name = 'money'


def default_view(request):
    return render(request, template_name='base.html')


urlpatterns = [
    path('', default_view, name='default_view'),
    path("income_list/", income_list_view, name="income_list"),
    path("income_create/", income_create_view, name="income_create"),
    path('income_edit/<int:income_id>/', Income_update, name='income_update'),

]
