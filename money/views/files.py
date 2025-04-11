from urllib import request

from money.models import Files

from django.shortcuts import render, redirect
from django.views import View
from money.forms import FilesCreateForm


class CreateFileView(View):
    def get(self, request):
        form = FilesCreateForm()
        return render(request, "accounts/file_upload.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = FilesCreateForm(request.POST, request.FILES)
        if form.is_valid():
            file_instance = form.save(commit=False)
            file_instance.user = request.user  # MUHIM!
            file_instance.save()
            return redirect('account:profile')
        return render(request, "accounts/file_upload.html", {"form": form})


class ListFileView(View):
    def get(self, request):
        file = Files.objects.filter(user=request.user)
        return render(request, template_name="files/file_upload.html", context={"files": file})
