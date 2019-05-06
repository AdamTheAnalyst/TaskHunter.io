from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from taskhunter.views.contact_view import ContactViewSet
from taskhunter.views.contact_method_view import ContactMethodViewSet
from taskhunter.views.contact_note_view import ContactNoteViewSet
from taskhunter.views.task_view import TaskViewSet
from taskhunter.views.user_view import UserViewSet


router = routers.DefaultRouter()

# Contacts
# router.register(r'contacts', ContactViewSet)
# router.register(r'contact_methods', ContactMethodViewSet)
# router.register(r'contact_notes', ContactNoteViewSet)

# Tasks
router.register(r'tasks', TaskViewSet, basename="tasks")
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^api-token-auth/', obtain_auth_token, name='api_token_auth')
]
