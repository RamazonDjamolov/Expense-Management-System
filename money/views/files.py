from django.contrib.auth.decorators import permission_required
from django.contrib.sessions.backends import file
from django.utils.decorators import method_decorator

from money.models import Files
from django.shortcuts import render, redirect
from django.views import View
from money.forms import FilesCreateForm


class ListFilesView(View):
    @method_decorator(permission_required('money.files_client', raise_exception=True))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        files = Files.objects.filter(user=request.user)
        return render(request, 'files/list.html', {'files': files})


class UploadFilesView(View):

    @method_decorator(permission_required('money.files_client', raise_exception=True))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = FilesCreateForm()
        return render(request, template_name='accounts/file_upload.html', context={'form': form})

    def post(self, request):
        form = FilesCreateForm(request.POST, request.FILES)
        if form.is_valid():
            file_instance = form.save(commit=False)
            file_instance.user = request.user
            file_instance.save()
            return redirect('account:profile')
        return render(request, template_name='accounts/file_upload.html', context={'form': form})


class UpdateFileView(View):

    @method_decorator(permission_required('money.files_client', raise_exception=True))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, file_id):
        file = Files.objects.get(id=file_id)
        form = FilesCreateForm(instance=file)
        return render(request, template_name='files/update.html', context={'form': form, 'file': file})

    def post(self, request, file_id):
        file = Files.objects.get(id=file_id)
        form = FilesCreateForm(request.POST, request.FILES, instance=file)
        if form.is_valid():
            file_instance = form.save(commit=False)
            file_instance.user = request.user
            file_instance.save()
            return redirect('money:list_file')
        return render(request, template_name='files/update.html', context={'form': form, 'file': file})


class DeleteFileView(View):
    @method_decorator(permission_required('money.files_client', raise_exception=True))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, file_id):
        file = Files.objects.get(id=file_id).delete()
        return redirect('money:list_file')
