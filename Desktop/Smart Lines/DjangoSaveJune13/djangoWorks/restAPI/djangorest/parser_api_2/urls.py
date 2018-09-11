# api/urls.py
# api/urls.py

from django.urls import path
from django.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
# from .views import CreateView
from . import views

urlpatterns = {
    # path('bucketlists/', CreateView.as_view(), name="create"),

	path('bodog/',views.bodogScraper , name="bodogScraper"),

	path('pinnacle/',views.bodogScraper , name="pinnacleScraper"),

}

urlpatterns = format_suffix_patterns(urlpatterns)