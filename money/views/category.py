from django.shortcuts import render, redirect

from money.forms import CategoryCreateForm
from money.models import Category


def CategoryCreate(request):
    if request.method == 'POST':
        form = CategoryCreateForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            user = request.user
            Category.objects.create(user_id=user, name=form.cleaned_data['name'])
            return redirect("money:income_list")

        return render(request, 'category/create.html', {'form': form})
    form = CategoryCreateForm
    return render(request, template_name='category/create.html', context={'form': form})
