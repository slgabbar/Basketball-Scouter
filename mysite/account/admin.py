from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account

class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'team_name', 'team_location',
                    'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username', 'team_name', 'team_location')
    readonly_fields = ('date_joined', 'last_login')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)

