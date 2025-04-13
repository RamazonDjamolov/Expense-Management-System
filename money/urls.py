from django.shortcuts import render
from django.urls import path
from .views import income_list_view, income_create_view, Income_update, create_expense, list_expenses, CategoryCreate, \
    Income_delete, Category_delete, Category_edit, UploadFilesView, ListFilesView, UpdateFileView, DeleteFileView

app_name = 'money'


def default_view(request):
    return render(request, template_name='base.html')


urlpatterns = [
    path("", income_list_view, name="income_list"),
    path("income_create/", income_create_view, name="income_create"),
    path('income_edit/<int:income_id>/', Income_update, name='income_update'),
    path("income_delete/<int:income_id>/", Income_delete, name="income_delete"),
    # expense

    path('expense_create/', create_expense, name='expense_create'),
    path('expense_list/', list_expenses, name='expense_list'),

    #     category
    path('category_create/', CategoryCreate, name='category_create'),
    path('category_delete/<int:category_id>/', Category_delete, name='category_delete'),
    path('category_edit/<int:category_id>/', Category_edit, name='category_edit'),

    #     files
    path('upload_file/', UploadFilesView.as_view(), name='upload_file'),
    path('list_file/', ListFilesView.as_view(), name='list_file'),
    path('update_file/<int:file_id>/', UpdateFileView.as_view(), name='update_file'),
    path('delete_file/<int:file_id>/', DeleteFileView.as_view(), name='delete_file'),

]
