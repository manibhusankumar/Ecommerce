from django.template.defaulttags import url
from django.urls import path, re_path
from app import views
from app.views import MainView, PostJsonListView

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # path('product-detail/', views.product_detail, name='product-detail'),
    # re_path('detail/(?P<pk>\d+)/', views.Detail.as_view(), name='product-detail'),
    path('pruduct-details/<slug:slug>/', views.SingleDetail.as_view(), name='product-detail'),
    path('trending-details/<slug:slug>/', views.TrendingDetailsView.as_view(), name='Trending-product'),

    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_card, name='showcart'),
    path('pluscart/', views.plus_cart, name='pluscart'),
    path('minuscart/', views.minus_cart, name='minuscart'),
    path('removecart/', views.remove_cart,name='removecart'),

    # path('add-to-cart/', views.AddToCartView.as_view, name='add_to_cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('login/', views.login, name='login'),
    path('registration/', views.customerregistration, name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    path('mani/', MainView.as_view(), name='main-view'),
    path('posts-json/<int:num_posts>/', PostJsonListView.as_view(), name='posts-json-view'),
    # path('serch/', views.index, name='in'),

]
