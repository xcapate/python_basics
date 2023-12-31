from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views

#Login urls
urlpatterns = [
    url(r'^login/$',auth_views.LoginView.as_view(),name='login'),
    url(r'^logout/$',auth_views.LogoutView.as_view(),name='logout'),
]

#Password Change
urlpatterns+=[
    url(r'^password-change/$',auth_views.PasswordChangeView.as_view(),name='password_change'),
    url(r'^password-change/done/$',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),
]

#Password Reset
urlpatterns+=[
    url(r'^password-reset/$',auth_views.PasswordResetView.as_view(),name='password_reset'),
    url(r'^password-reset/done/$',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^password-reset/complete/$',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]

#User Registration
urlpatterns+=[
    url(r'^register/$', views.register, name='register'),
]

#App urls
urlpatterns+=[
    url(r'^$', views.dashboard, name='dashboard'),   
]

#Profile urls
urlpatterns+=[
    url(r'^edit/$', views.edit, name='edit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
