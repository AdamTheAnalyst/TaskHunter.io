from taskhunter.serializers.contact_serializer import ContactSerializer
from taskhunter.models import Contact
from . import CommonViewSet


class ContactViewSet(CommonViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer