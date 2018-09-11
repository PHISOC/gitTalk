# api/urls.py

from django.urls import path
from django.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
# from .views import CreateView
from . import views

urlpatterns = {
    # path('bucketlists/', CreateView.as_view(), name="create"),

    path('api',views.pinnacleScraper , name="pinnacleScraper"),
	
	path('api/baseball/',views.baseballPinnacleScraper , name="baseballPinnacleScraper"),

	path('api/proper-si/',views.baseballSportsInteractionScraper , name="baseballSportsInteractionScraper"),

	path('api/baseball3/',views.baseballBodogScraper , name="baseballBodogScraper"),

	path('api/proper-williamhill/',views.williamHillScraper , name="williamHillScraper"),

	path('api/proper-bet365/',views.bet365Scraper , name="bet365Scraper"),

	path('api/proper-bodog/',views.bodogScraper , name="bodogScraper"),

	path('api/test/',views.test , name="test"),

    path('api2',views.Scraper888 , name="Scraper888"),
}

urlpatterns = format_suffix_patterns(urlpatterns)