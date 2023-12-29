from django.contrib import admin

from users.models import User


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('last_name', 'email')
    list_filter = ('email', 'first_name')


admin.site.register(User, UserAdmin)
