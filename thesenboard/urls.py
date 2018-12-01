from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from start import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('admin/', admin.site.urls),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('new_thesis/', views.NewThesisView.as_view(), name='newThesis'),
    path('thesis/<int:thesis_id>/', views.ThesisView.as_view(), name='thesis'),
    path('user/', views.UserDetail.as_view()),
    path('discussion/<int:pk>/', views.ThesisEntryView.as_view({'get': 'list'})),
    path('discussions/', views.AllThesenView.as_view({'get': 'list'})),
    path('abstimmung/<int:pk>/', views.ThesenAbstimmungView.as_view({'get': 'list'})),
]
