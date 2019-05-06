from taskhunter.models import Task
from . import CommonSerializer


class TaskSerializer(CommonSerializer):

    class Meta:
        model = Task
        fields = ['id',
                  'title',
                  'due_date',
                  'completed_date'
                  ] + CommonSerializer.common_fields

    def __str__(self):
        return "{}".format(self.title)
