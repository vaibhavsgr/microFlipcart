from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Product, Account
from .forms import UserAdminChangeForm, UserAdminCreationForm



class AccountAdmin(UserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    list_display = ('username', 'phone', 'date_joined', 'last_login', 'is_admin','is_staff')
    list_filter = ('is_admin',)

    readonly_fields=('date_joined', 'last_login')
	#fieldsets = ((None,
    #{'fields': ('username', 'phone', 'password')}),
    #('Personal info', {'fields': ()}),
    #('Permissions', {'fields': ('admin',)}))

    fieldsets = ()
    search_fields = ('username', 'phone')
    filter_horizontal = ()


admin.site.register(Account, AccountAdmin)
admin.site.register(Product)
