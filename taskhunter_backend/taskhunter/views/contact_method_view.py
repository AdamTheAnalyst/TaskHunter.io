from taskhunter.serializers.contact_method_serializer import ContactMethodSerializer
from taskhunter.models import ContactMethod
from . import CommonViewSet


class ContactMethodViewSet(CommonViewSet):
    queryset = ContactMethod.objects.all()
    serializer_class = ContactMethodSerializer