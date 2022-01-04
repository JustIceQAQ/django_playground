from health_check.backends import BaseHealthCheckBackend
from health_check.exceptions import HealthCheckException

from iris.models import Iris


class IrisTableCheckBackend(BaseHealthCheckBackend):
    #: The status endpoints will respond with a 200 status code
    #: even if the check errors.
    critical_service = False

    def check_status(self):
        data = Iris.objects.all()
        if not data.exists():
            raise HealthCheckException("Iris table is empty")

    def identifier(self):
        return self.__class__.__name__  # Display name on the endpoint.
