from django.urls import path
from . import views
from . import admin_views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path('course/', views.predict_course, name='course'),
    path(
        "admin/retrain-model/<int:model_id>/",
        admin_views.retrain_model_view,
        name="retrain_model",
    ),
]