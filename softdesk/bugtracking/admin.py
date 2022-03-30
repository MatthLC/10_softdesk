from django.contrib import admin


from bugtracking.models import Project, Issue, Comment, Contributor


admin.site.register(Project)
admin.site.register(Issue)
admin.site.register(Comment)
admin.site.register(Contributor)