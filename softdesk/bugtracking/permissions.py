from rest_framework.permissions import BasePermission
from bugtracking.models import Contributor
from django.db.models import Q


class IsAdminOrAuthorOrContributorAuthenticated(BasePermission):

    """
    user type :
        - AUT : author
        - COL : contributor

    Define the access of user type for the current LIST view (ex : http://127.0.0.1:8000/projects/):
        - AUT : all access
        - COL : GET POST
    """

    # LIST permissions : ex : http://127.0.0.1:8000/projects/
    def has_permission(self, request, view):
        granted_method = ('GET', 'POST')

        # Check if logged user is contributor
        try:
            # The logged user must be in contributor database for the selected project
            user = Contributor.objects.get(
                Q(project_id=view.kwargs['project_pk']) & Q(user=request.user)
            )

            # SuperUser have all access granted
            if request.user.is_authenticated and request.user.is_superuser:
                True

            # AUT have all access granted
            if request.user.is_authenticated and user.permissions == 'AUT':
                return True

            # COL have only GET and POST granted
            if (
                request.user.is_authenticated
                and user.permissions == 'COL'
                and request.method in granted_method
            ):
                return True

        except Contributor.DoesNotExist:
            print('pas de données correspondantes')

    # DETAIL permissions : ex : http://127.0.0.1:8000/projects/{id}/
    def has_object_permission(self, request, view, obj):

        # Check if logged user is contributor
        try:
            granted_method = ('GET')

            # The logged user must be in contributor database
            user = Contributor.objects.get(
                Q(project_id=view.kwargs['project_pk']) & Q(user=request.user)
            )

            # SuperUser have all access granted
            if request.user.is_authenticated and request.user.is_superuser:
                True

            # AUT have all access granted
            if request.user.is_authenticated and user.permissions == 'AUT':
                return True

            # COL have only GET granted
            if (
                request.user.is_authenticated
                and user.permissions == 'COL'
                and request.method in granted_method
            ):
                return True
        except Contributor.DoesNotExist:
            print('pas de données correspondantes')
