from django.contrib import admin
from .models import Group, Membership, UserMembership, UserSportResult, SportTest, UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin


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


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    max_num = 1
    can_delete = False


class UserAdmin(AuthUserAdmin):
    def add_view(self, *args, **kwargs):
        self.inlines = []
        return super(UserAdmin, self).add_view(*args, **kwargs)

    def change_view(self, *args, **kwargs):
        self.inlines = [UserProfileInline]
        return super(UserAdmin, self).change_view(*args, **kwargs)


admin.site.register(Group, GroupAdmin)
admin.site.register(Membership, MembershipAdmin)
admin.site.register(UserMembership, UserMembershipAdmin)
admin.site.register(SportTest, SportTestAdmin)
admin.site.register(UserSportResult, UserSportResultAdmin)
admin.site.register(UserProfile)
# unregister old user admin
admin.site.unregister(User)
# register new user admin
admin.site.register(User, UserAdmin)
