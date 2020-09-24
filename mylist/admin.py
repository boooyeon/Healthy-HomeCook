from django.contrib import admin
# from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin

from .models import Channel,Cart
from django.conf import settings


# Register your models here.

class ChannelAdmin(admin.ModelAdmin):
    list_display = ('food_name', 'video_title', 'video_link')

# class CartInline(admin.StackedInline): # 로또 프로젝트에서 썼던 방식으로 유저 밑에 프로필 을 붙여서 보여주려고 이를 상속받음
#     model = Profile
#     con_delete = False     

# class CustomUserAdmin(UserAdmin):
#     inlines = (CartInline,)


admin.site.register(Channel, ChannelAdmin)
admin.site.register(Cart)
# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)