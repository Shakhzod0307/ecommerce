from django.urls import path
from . import views
from .forms import LoginForm, MyPasswordResetForm, MyPasswordChangeForm, MySetPasswordForm
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contactus_view, name='contact'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('update/address/<int:pk>', views.updateAddress.as_view(), name='updateaddress'),
    # category urls here
    path('category/<slug:val>', views.CategoryView.as_view(), name='category'),
    path('category-title/<val>>', views.CategoryTitle.as_view(), name='category-title'),
    path('product-detail/<int:pk>', views.ProductDetail.as_view(), name='product-detail'),
    # cart urls here
    path('addtocart/', views.add_to_cart, name='addtocart'),
    path('cart/', views.show_cart, name='showcart'),
    path('checkout/', views.checkout.as_view(), name='checkout'),

    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart,name='removecart'),

    path('orders/', views.orders,name='orders'),


    path('search/', views.search,name='search'),

    # here urls for login and registration
    path('registration/', views.CustomerRegistrationView.as_view(), name='registration'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html',
                                                         authentication_form=LoginForm),
         name='login'),

    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='password_change.html',
                                                                  form_class=MyPasswordChangeForm,
                                                                  success_url='/passwordchangedone'),
         name='password_change'),

    path('passwordchangedone/',
         auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
         name='passwordchangedone'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # password reset urls here
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html',
                                                                 form_class=MyPasswordResetForm),
         name='password_reset'),

    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html',
                                                     form_class=MySetPasswordForm),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),

]
