from django.urls import include, path
from rest_framework import routers
from quotes.quotes_api import views

router = routers.DefaultRouter()
router.register(r'quotes', views.QuoteViewSet)
router.register(r'characters', views.CharacterViewSet)
router.register(r'tv_shows', views.TVShowViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]