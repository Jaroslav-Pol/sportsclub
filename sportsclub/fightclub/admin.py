from django.contrib import admin

# Register your models here.
from .models import Group, Membership, UserMembership

class UserMembershipInline(admin.TabularInline):
    model = UserMembership
    extra = 0


class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'week_day', 'start_time')


class MembershipAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    inlines = [UserMembershipInline]


class UserMembershipAdmin(admin.ModelAdmin):
    list_display = ('member', 'membership', 'display_group')
    # filtravimas pagal narystes ir grupes
    list_filter = ('membership', 'group')
    search_fields = ('member__username', 'membership__name')




admin.site.register(Group, GroupAdmin)
admin.site.register(Membership, MembershipAdmin)
admin.site.register(UserMembership, UserMembershipAdmin)
