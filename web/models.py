from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='categorythumbs', blank=True)

    def __unicode__(self):
        return "%s" % (self.name)



class Project(models.Model):
    title = models.CharField(max_length=200)
    thumbImage = models.ImageField(upload_to='projects/thumb', blank=True)
    video = models.URLField(blank=True)
    body = models.TextField()
    date = models.DateField()
    category = models.ManyToManyField('Category', blank=True)
    url = models.URLField(blank=True)

    def get_absolute_url(self):
        return "/project/%s" % (self.id)

    def __unicode__(self):
        return "%s" % (self.title)

class ProjectImage(models.Model):
    image = models.ImageField(upload_to='projects/images')
    altText = models.CharField(max_length=200, blank=True)
    projectId = models.ForeignKey('Project')

    thumbnail = models.BooleanField()

    def __unicode__(self):
        return "%s" % (self.image)