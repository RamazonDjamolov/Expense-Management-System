from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView

from account.forms import ProfileForm
# from account.forms import ProfileEditForm
from account.models import Profile


class ProfileDetailView(View):

    def get(self, request, *args, **kwargs):
        profile = Profile.objects.filter(user=request.user)
        return render(request, template_name='accounts/profile.html', context={'profile': profile})


class EditProfileView(View):

    def get(self, request, profile_id, *args, **kwargs):
        profile = Profile.objects.get(id=profile_id)
        form = ProfileForm(instance=profile)
        return render(request, template_name='accounts/profil2.html', context={'form': form, 'profile': profile})

    def post(self, request, profile_id, *args, **kwargs):
        profile = Profile.objects.get(id=profile_id)
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account:profile')
        return render(request, template_name='accounts/profil2.html', context={'form': form, 'profile': profile})
