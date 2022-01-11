from rest_framework.routers import DefaultRouter

from iris.views import IrisViewSet


class DefaultRouters(DefaultRouter):
    """
    Extends `DefaultRouter` class to add a method for extending url routes from another router.
    """

    def extend(self, router):
        """
        Extend the routes with url routes of the passed in router.

        Args:
             router: DefaultRouter instance containing route definitions.
        """
        self.registry.extend(router.registry)


router = DefaultRouters()
router.register(r'iris', IrisViewSet)
app_name = "api"
urlpatterns = router.urls
