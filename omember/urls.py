from django.urls import path, include
from . import views
app_name = 'membership'
urlpatterns = [
       path('memberships/', views.MembershipView.as_view(), name='select'),
       path("signup", views.SignUpView.as_view(),name='signup'),
       path('index',views.index,name='index'),
       path('landing',views.ContactView.as_view(),name='landing')
]