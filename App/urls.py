from django.urls import path

from App import views

urlpatterns = [
    path ('',views.inicio, name="inicio"),
    path ('',views.modelo1, name=""),
    path ('',views.modelo2, name=""),
    path ('',views.modelo3, name=""),
]
