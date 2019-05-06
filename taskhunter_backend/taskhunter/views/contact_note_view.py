from taskhunter.serializers.contact_note_serializer import ContactNoteSerializer
from taskhunter.models import ContactNote
from . import CommonViewSet


class ContactNoteViewSet(CommonViewSet):
    queryset = ContactNote.objects.all()
    serializer_class = ContactNoteSerializer