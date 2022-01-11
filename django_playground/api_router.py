import dataclasses
import pprint
from enum import Enum
from django.db.migrations.executor import MigrationExecutor
from django.db import connections, DEFAULT_DB_ALIAS
from django.db.utils import OperationalError
from rest_framework.routers import DefaultRouter

from common.models import APIsObject
from iris.views import IrisViewSet

def is_database_synchronized(database):
    connection = connections[database]
    connection.prepare_database()
    executor = MigrationExecutor(connection)
    targets = executor.loader.graph.leaf_nodes()
    return not executor.migration_plan(targets)

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


@dataclasses.dataclass
class APINameData:
    basename: str = None
    displayname: str = None


class APIRouterEnum(APINameData, Enum):
    iris = ('iris', "鳶尾花")


router = DefaultRouters()
router.register(r'iris', IrisViewSet, APIRouterEnum.iris.basename)
app_name = "api"
urlpatterns = router.urls
url_base_name = list(set([url.name.rsplit("-", 1)[0] for url in urlpatterns]))
for api_name in url_base_name:
    get_display_name = getattr(APIRouterEnum, api_name, None)
    display_name = api_name if get_display_name is None else get_display_name.displayname
    if is_database_synchronized(DEFAULT_DB_ALIAS):
        try:
            APIsObject.objects.update_or_create(viewsets_name=api_name, defaults={'display_name': f"{display_name} API"}, )
        except OperationalError:
            pass
