from django.contrib import admin

# Register your models here.
from .models import Group, Membership, UserMembership

admin.site.register(Group)
admin.site.register(Membership)
admin.site.register(UserMembership)