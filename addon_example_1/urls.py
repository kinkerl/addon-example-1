from django.urls import path

from .views import index

app_name = "addon_example_1"

urlpatterns = [
    path('', index, name='index')
]
