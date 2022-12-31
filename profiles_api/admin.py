from django.contrib import admin

from profiles_api import models
from profiles_api.models import ProfileFeedItem
# Register your models here.

admin.site.register(models.UserProfile)

#admin.site.register(models.ProfileFeedItem)
class ProfileFeedItemAdmin(admin.ModelAdmin):
    list_display = ('id','status_text','created_on','user_profile',)

admin.site.register(ProfileFeedItem, ProfileFeedItemAdmin)
