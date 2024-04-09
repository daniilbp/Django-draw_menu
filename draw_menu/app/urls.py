from django.urls import path

from .views import main, draw_menu


app_name = "app"

urlpatterns = [
    path('', main, name="main"),
    path('<path:path>/', draw_menu, name="draw_menu"),
]
