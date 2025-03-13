from django.urls import path
from .views import income_list_view

urlpatterns = [
    path("income_list/", income_list_view, name="index")
]
