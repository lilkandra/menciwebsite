from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('products', views.products, name='products'),
    path('product/<str:id>', views.product, name='product'),
    path('bag', views.bag, name='bag'),
    path('remove_item/<str:id>', views.remove_item, name='remove_item'),
    path('order', views.order, name='order'),
    path('validated', views.validated, name='validated'),
    path('contact', views.contact, name='contact'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)