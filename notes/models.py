from django.db import models 

class Tag(models.Model):
    tag = models.CharField(max_length=15)

    def __str__(self):
        return "%s" % (self.tag)
class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=400)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}. {self.title}"

