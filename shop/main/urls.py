from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from cart import views as views_cart

app_name = 'main'

urlpatterns = [
    path('', views.base, name='base'),
    path('cheap/', views.cheap, name='cheap'),
    path('expensive/', views.exp, name='expensive'),
    path('item/<int:item_id>/', views.detail, name='detail'),
    path('add/', views.add, name='add'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)