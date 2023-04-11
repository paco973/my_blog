import debug_toolbar
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.utils.text import gettext_lazy as _


urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('froala_editor/', include('froala_editor.urls')),
    
    path('', include('app.urls')),
    path('', include('user_profile.urls')),
    path('', include('dashboard.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



admin.site.site_header = _('Lawa Zone Admin')
admin.site.site_title = _('Lawa Zone Admin Portail')
admin.site.index_title = _('Welcome to the Lawa Zone Portail')

handler404 = 'my_blog.views.handler404'
handler500 = 'my_blog.views.handler500'