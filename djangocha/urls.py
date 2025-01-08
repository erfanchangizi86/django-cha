from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
# from django.conf.urls import url 

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('home/', include('panel_sms.urls')),
    path('chat/', include('chat.urls')),
    # سایر URLهای عمومی
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# اضافه کردن URLهای مربوط به زبان‌ها
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    # سایر URLها که می‌خواهید به i18n اضافه شوند
)

# اضافه کردن URL مربوط به set_language
urlpatterns += [
    path('set_language/', include('django.conf.urls.i18n')),
]
