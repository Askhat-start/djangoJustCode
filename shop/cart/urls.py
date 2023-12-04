from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

app_name = 'cart'
urlpatterns = [
    path('add/<int:product_id>/', cart_add, name='cart_add'),
    path('cart_detail/', cart_detail, name='cart_detail')
    # Other cart URLs go here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
