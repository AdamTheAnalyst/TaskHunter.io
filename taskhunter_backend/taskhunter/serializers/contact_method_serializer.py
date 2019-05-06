from taskhunter.models import ContactMethod
from . import CommonSerializer


class ContactMethodSerializer(CommonSerializer):

    class Meta:
        model = ContactMethod
        fields = ['id',
                  'type',
                  'value',
                  'contact'
                  ] + CommonSerializer.common_fields

    def __str__(self):
        return "{} - {}".format(self.type, self.value)
