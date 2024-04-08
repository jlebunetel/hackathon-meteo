"""View definitions for the 'core' application."""

import logging
from typing import Any

from django.views.generic.base import TemplateView

logger = logging.getLogger(__name__)

UPCOMING_DAYS: int = 15


class LandingPageView(TemplateView):
    """The landing page."""

    template_name = "core/landing.html"

    def get_context_data(self, **kwargs: int) -> dict[str, Any]:
        """Returns a dictionary representing the template context."""
        context = super().get_context_data(**kwargs)

        # Add context data for stats:
        context["stats"] = {}

        return context
