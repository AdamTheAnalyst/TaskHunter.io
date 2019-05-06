from taskhunter.models import Contact
from . import CommonSerializer


class ContactSerializer(CommonSerializer):

    class Meta:
        model = Contact
        fields = ['id',
                  'name',
                  'relation',
                  'birthday',
                  'employer'
                  ] + CommonSerializer.common_fields

    def __str__(self):
        return "{}".format(self.name)
