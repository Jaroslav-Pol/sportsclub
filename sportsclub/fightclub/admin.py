from django.contrib import admin

# Register your models here.
from .models import Group, Membership, UserMembership, UserSportResult, SportTest


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


class SportTestAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'result_exp', 'result_sport')


class UserSportResultAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'date', 'result', 'comment')
    list_filter = ('name', 'date')
    search_fields = ('user__username',)


admin.site.register(Group, GroupAdmin)
admin.site.register(Membership, MembershipAdmin)
admin.site.register(UserMembership, UserMembershipAdmin)
admin.site.register(SportTest, SportTestAdmin)
admin.site.register(UserSportResult, UserSportResultAdmin)
