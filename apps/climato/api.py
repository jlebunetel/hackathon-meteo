"""API definitions for the 'climato' application."""

from climato.viewsets import MesureViewSet, PosteViewSet
from rest_framework.routers import APIRootView, DefaultRouter

app_name = "climato_api"


class ClimatoAPIRootView(APIRootView):
    """Application root view."""


class ClimatoRouter(DefaultRouter):
    """Application rooter"""

    APIRootView = ClimatoAPIRootView


router = ClimatoRouter()
router.register("mesures", MesureViewSet, basename="mesures")
router.register("postes", PosteViewSet, basename="postes")
urlpatterns = router.urls
