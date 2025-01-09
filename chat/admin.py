from django.contrib import admin

# Register your models here.
from .models import  Message,Chat

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('roomname', 'get_members')  # نمایش نام اتاق و اعضا
    search_fields = ('roomname',)  # قابلیت جستجو بر اساس نام اتاق
    filter_horizontal = ('members',)  # اضافه کردن رابط گرافیکی برای مدیریت اعضا

    def get_members(self, obj):
        return ", ".join([member.username for member in obj.members.all()])  # نمایش اعضا به صورت لیست
    get_members.short_description = 'اعضا'

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('author', 'related_chat', 'time', 'short_text')  # نمایش اطلاعات پیام
    search_fields = ('author__username', 'related_chat__roomname', 'text')  # جستجو بر اساس نویسنده، نام چت و متن پیام
    list_filter = ('time', 'related_chat')  # فیلتر بر اساس زمان و چت مرتبط
    list_editable = ('related_chat',)  # امکان ویرایش سریع چت مرتبط از لیست

    def short_text(self, obj):
        return obj.text[:50] + "..." if len(obj.text) > 50 else obj.text  # نمایش کوتاه شده متن پیام
    short_text.short_description = 'متن کوتاه'
