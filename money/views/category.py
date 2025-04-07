from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect

from money.forms import CategoryCreateForm
from money.models import Category

@permission_required('money.category_client', raise_exception=True )
def CategoryCreate(request):
    category = Category.objects.all().filter(user_id=request.user.id)
    if request.method == 'POST':
        form = CategoryCreateForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            user = request.user
            Category.objects.create(user_id=user, name=form.cleaned_data['name'])
            return redirect("money:income_list")

        return render(request, 'category/create.html', {
            'form': form,
            'category': category
        })
    form = CategoryCreateForm
    return render(request, template_name='category/create.html', context={
        'form': form,
        'category': category

    })

@permission_required('money.category_client', raise_exception=True )
def Category_delete(request, category_id):
    category = Category.objects.filter(user_id=request.user.id, id=category_id).first()
    category.delete()
    return redirect("money:category_create")

@permission_required('money.category_client', raise_exception=True )
def Category_edit(request, category_id):
    category = Category.objects.filter(user_id=request.user.id, id=category_id).first()
    if request.method == 'POST':
        form = CategoryCreateForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('money:category_create')

        return render(request, 'category/edit.html', {
            'form': form,
            'category': category
        })
    form = CategoryCreateForm(instance=category)
    return render(request, template_name='category/edit.html', context={
        'form': form,
        'category': category
    })
