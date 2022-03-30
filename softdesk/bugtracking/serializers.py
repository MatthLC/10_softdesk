from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from bugtracking.models import Project, Issue, Contributor, Comment
from authentication.serializers import UserListSerializer


class IssueListSerializer(ModelSerializer):

	class Meta:
		model = Issue
		fields = ['id', 'title','desc','tag','priority']


class IssueDetailSerializer(ModelSerializer):

	class Meta:
		model = Issue
		fields = ['id', 'title','desc','tag','priority','author_user','assignee_user', 'created_time']


class ProjectListSerializer(ModelSerializer):

		class Meta:
			model = Project
			fields = ['id', 'title', 'description']


class ProjectDetailSerializer(ModelSerializer):
	"""
	Display issues information inside project detail to read quickly the current situation
	"""
	issues = IssueListSerializer(many=True)

	class Meta:
		model = Project
		fields = ['id', 'title','description','type', 'contributors', 'issues']


class ContributorSerializer(ModelSerializer):
	class Meta:
		model = Contributor
		fields = ['id', 'user', 'permissions', 'role']


class CommentSerializer(ModelSerializer):
	class Meta:
		model = Comment
		fields = ['id', 'description' ]