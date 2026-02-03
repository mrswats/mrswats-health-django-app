from django.urls import path

from health import views

urlpatterns = [
    path("_health/", views.health_endpoint, name="health"),
]
