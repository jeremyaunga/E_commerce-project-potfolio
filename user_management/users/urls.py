from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',views.homepage,name='start'),
    path('login/',views.login_user,name='login'),
    path('signup/',views.signup,name='signup'),
    path('users_list/',views.users_list,name='users_list'),
    path("homepage/",views.homepage,name='homepage'),    
    path('logout/',views.logout_user,name='logout'),
    path("user_profile/",views.user_profile,name="user_profile"),   
    path("register_product/",views.register_product,name="register_product"),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path("view_cart/",views.view_cart,name="view_cart"),    
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)