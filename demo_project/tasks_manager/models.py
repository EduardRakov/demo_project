from django.db import models

class Project(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(max_length = 150, blank = True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length = 80)
    mark_complete = models.BooleanField(blank = True)
    project = models.ForeignKey(Project)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name