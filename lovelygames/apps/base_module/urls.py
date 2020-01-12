from django.urls import path, include
from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
	path('', views.base, name = 'base'),
	path('article/<int:pk>', views.article, name = 'article'),
	url(r'^ckeditor/', include('ckeditor_uploader.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)