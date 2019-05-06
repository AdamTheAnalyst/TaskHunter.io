from taskhunter.serializers.task_serializer import TaskSerializer
from rest_framework.exceptions import PermissionDenied
from taskhunter.models import Task
from . import CommonViewSet


class TaskViewSet(CommonViewSet):

    serializer_class = TaskSerializer

    def get_queryset(self):

        if self.request.user.is_authenticated:
            return Task.objects.filter(
                completed_date__isnull=True,
                created_by=self.request.user,
                deleted_at__isnull=True).order_by('due_date')
        else:
            raise PermissionDenied({"message": "Please log in"})
