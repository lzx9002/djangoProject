from django.contrib import admin

from api.models import User_role_list, User_name_list


# Register your models here.
@admin.register(User_role_list)
class name_role_listAdmin(admin.ModelAdmin):
    list_display = ('id', 'role_name', 'limits', 'descr', 'checks',)
    search_fields = ('id', 'role_name', 'limits', 'descr', 'checks',)
    ordering = ('id',)


@admin.register(User_name_list)
class name_listAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password', 'nickname', 'sex', 'cellphone', 'email',)
    search_fields = ('id', 'username', 'password', 'nickname', 'sex', 'cellphone', 'email',)
    ordering = ('username', 'role',)


# admin.site.register([name_list, role_list])
# admin.site.register(name_listAdmin, name_listAdmin)
