from taskhunter.models import ContactNote
from . import CommonSerializer


class ContactNoteSerializer(CommonSerializer):

    class Meta:
        model = ContactNote
        fields = ['id',
                  'type',
                  'note',
                  'contact'
                  ] + CommonSerializer.common_fields

    def __str__(self):
        return "{} - {}".format(self.type, self.note)
