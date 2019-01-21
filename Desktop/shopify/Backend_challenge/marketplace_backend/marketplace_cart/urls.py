# api/urls.py
# api/urls.py

from django.urls import path
from django.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = {
	path('create/', views.create_cart, name="create_cart"),

	# path('events/<str:event_id>', views.get_event_details, name="get_event_details")

}
urlpatterns = format_suffix_patterns(urlpatterns)