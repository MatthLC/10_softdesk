from django.shortcuts import render, get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.db.models import Q

from bugtracking.models import Project, Issue, Contributor, Comment
from bugtracking.serializers import (
	ProjectListSerializer, ProjectDetailSerializer,
	IssueListSerializer, IssueDetailSerializer,
	ContributorSerializer,
	CommentSerializer
)

from bugtracking.permissions import IsAdminOrAuthorOrContributorAuthenticated


"""
Mixin : Display detail of object
Ex : projects/{id}/
"""
class MultipleSerializerMixin:

	detail_serializer_class = None

	def get_serializer_class(self):
		if self.action == 'retrieve' and self.detail_serializer_class is not None:
			return self.detail_serializer_class
		return super().get_serializer_class()

"""
display 'projects' informations
/projects/
/projects/{id}/
"""
class ProjectViewset(MultipleSerializerMixin, ModelViewSet):

	serializer_class = ProjectListSerializer
	detail_serializer_class = ProjectDetailSerializer

	permission_classes = [IsAuthenticated]

	def get_queryset(self):
		# Display all project if logged user is contributor
		return Project.objects.filter(contributors=self.request.user)

	def perform_create(self, serializer):
		# Save project with the current logged user
		project = serializer.save(author_user=self.request.user)

		# Feeding contributor database (ManyToMany) with the new project
		# Initialize permissions to AUT : author
		# So the user is automatically author of his own project
		contributor = Contributor.objects.create(
			user=self.request.user,
			project=project,
			permissions = 'AUT',
			role=''
		)

"""
Display users informations
/projects/{id}/users/
"""
class ContributorViewset(ModelViewSet):

	serializer_class = ContributorSerializer

	permission_classes = [IsAdminOrAuthorOrContributorAuthenticated]

	def get_queryset(self):
		# Check if logged user is contributor
		try:
			contributor_exist = Contributor.objects.get(
				Q(project=self.kwargs['project_pk']) & Q(user=self.request.user)
			)

			return Contributor.objects.filter(project=self.kwargs['project_pk'])

		except :
			print('Aucun résultat.')
		
	def perform_create(self, serializer):
		# get project object projects/{id}/
		project = get_object_or_404(Project, id=self.kwargs['project_pk'])	
		# save contributor information with the current projects/{id}/
		contributor = serializer.save(project=project)
		
"""
Display Issues informations
projects/{id}/issues/
projects/{id}/issues/{id}/
"""
class IssueViewset(MultipleSerializerMixin, ModelViewSet):

	serializer_class = IssueListSerializer
	detail_serializer_class = IssueDetailSerializer

	permission_classes = [IsAdminOrAuthorOrContributorAuthenticated]

	def get_queryset(self):
		return Issue.objects.filter(project_id=self.kwargs['project_pk'])

	def perform_create(self, serializer):
		# get project object projects/{id}/
		project = get_object_or_404(Project, id=self.kwargs['project_pk'])

		# when the user create an issue, he is automatically author and asignee
		issue = serializer.save(project=project, author_user=self.request.user, assignee_user=self.request.user)

"""
Display comments informations
projects/{id}/issues/{id}/comments/
projects/{id}/issues/{id}/comments/{id}
"""
class CommentViewset(ModelViewSet):

	serializer_class = CommentSerializer

	permission_classes = [IsAdminOrAuthorOrContributorAuthenticated]

	def get_queryset(self):
		return Comment.objects.filter(issue=self.kwargs['issue_pk'])

	def perform_create(self, serializer):
		# get project object projects/{id}/
		issue = get_object_or_404(Issue, id=self.kwargs['issue_pk'])

		# save issue with user as author
		serializer.save(issue=issue, author_user=self.request.user)
