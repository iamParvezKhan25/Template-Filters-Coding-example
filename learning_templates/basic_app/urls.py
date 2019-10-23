from django.urls import path
from basic_app import views

# Template Tagging
# global varible 'app_name'
app_name = 'basic_app'

urlpatterns = [
    path('relative/',views.relative,name='relative'),
    path('others/',views.other,name='other')
]
