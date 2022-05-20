from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrganizationLestCreateAPI.as_view()),
    path('<int:pk>', views.OrganizationRetriveUpdateDestroyAPI.as_view())
]
