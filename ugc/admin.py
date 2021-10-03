from django.contrib import admin

from .forms import ProfileForm
from .models import Profile, DeepLinking


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'external_id', 'name')
    form = ProfileForm


@admin.register(DeepLinking)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('referral_id', 'user_id', 'user_name')
