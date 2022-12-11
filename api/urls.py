from django.urls import path
from .views import CountryListView,CountryDetailView
urlpatterns = [
   path('', CountryListView.as_view(), name='countries_list'),
   path('<int:pk>', CountryDetailView.as_view(),name='country_detail')
]