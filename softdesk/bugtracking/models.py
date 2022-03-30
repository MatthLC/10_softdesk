from django.db import models 
from django.conf import settings

"""
{id} is the id's database of previous object.
ex : projects/1/ is the project with id = 1

API bugtracking Pattern : 
	- projects/
	- project/{id}/
	- project/{id}/issues/
	- project/{id}/issues/{id}/
	- project/{id}/issues/{id}/comments/
	- project/{id}/issues/{id}/comments/{id}
	- projects/users/
	- projects/users/{id}
"""

class Project(models.Model):
	TYPE_CHOICE = [
		('BE', 'back-end'),
		('FE', 'front-end'),
		('IOS', 'ios'),
		('AND', 'android'),
	]
	title = models.CharField(max_length=255, verbose_name='Titre')
	description = models.CharField(max_length=2048, verbose_name='Description')
	type = models.CharField(max_length=8, choices=TYPE_CHOICE)
	author_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	contributors = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Contributor', related_name='contributions')


class Contributor(models.Model):

	PERMISSION_CHOICE = [
		('AUT','auteur'),
		('COL','collaborateur')
	]

	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='contributor')
	project = models.ForeignKey('bugtracking.Project', on_delete=models.CASCADE, related_name='contributor_project')
	permissions = models.CharField(max_length=8, choices=PERMISSION_CHOICE)
	role = models.CharField(max_length=128, null=True)

	class Meta:
		unique_together = ('user', 'project')


class Issue(models.Model):
	PRIORITY_CHOICE = [
		('LOW','Faible'),
		('MED','Moyen'),
		('HIG','Elevée'),
	]

	TAG_CHOICE = [
		('BUG','Bug'),
		('IMP','Amélioration'),
		('TAS','Tâche'),
	]

	STATUS_CHOICE = [
        ('TODO', 'À faire'),
        ('PROG', 'En cours'),
        ('DONE', 'Terminé'),
    ]

	title = models.CharField(max_length=255, verbose_name='Titre')
	desc = models.CharField(max_length=2048, verbose_name='Description')
	tag = models.CharField(max_length=8, choices=TAG_CHOICE)
	priority = models.CharField(max_length=8, choices=PRIORITY_CHOICE)
	project = models.ForeignKey('bugtracking.Project', on_delete=models.CASCADE, null=True, related_name='issues')
	status = models.CharField(max_length=8, choices= STATUS_CHOICE, verbose_name='Status')
	author_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	assignee_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='assignee_user')
	created_time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
	description = models.CharField(max_length=2048)
	author_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	issue = models.ForeignKey('bugtracking.Issue', on_delete=models.CASCADE, null=True, related_name = 'comments')
	created_time = models.DateTimeField(auto_now_add=True)



