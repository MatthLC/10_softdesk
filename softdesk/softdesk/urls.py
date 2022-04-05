"""softdesk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework_nested import routers

from bugtracking.views import ProjectViewset, IssueViewset, ContributorViewset, CommentViewset
from authentication.views import SignupViewset, UserListViewset

"""
router :
    - /projects/
    - /projects/{id}
    - /signup/
    - /userlist/
"""
router = routers.SimpleRouter()
router.register(r'projects', ProjectViewset, basename='projects')
router.register('signup', SignupViewset, basename='signup')
router.register('userlist', UserListViewset, basename='userlist')

"""
Nested router after projects for users and issues :
    - /projects/{id}/users/
    - /projects/{id}/users/{id}/

    - /projects/{id}/issues/
    - /projects/{id}/issues/{id}/
"""
projects_router = routers.NestedSimpleRouter(router, r'projects', lookup='project')
projects_router.register(r'users', ContributorViewset, basename='project-users')
projects_router.register(r'issues', IssueViewset, basename='project-issues')

"""
Nested router after issues for comments :
    - /projects/{id}/issues/{id}/comments/
    - /projects/{id}/issues/{id}/comments/{id}
"""
issues_router = routers.NestedSimpleRouter(projects_router, r'issues', lookup='issue')
issues_router.register(r'comments', CommentViewset, basename='comment')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
    path('', include(projects_router.urls)),
    path('', include(issues_router.urls)),
]
