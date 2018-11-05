from django.db import models

# Create your models here.

class PostType(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Posts(models.Model):
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    logo = models.ImageField(null=False, blank=False, width_field='width', height_field='height')
    Posting_title = models.CharField(max_length=100)
    slug = models.SlugField()
    comp_name=models.CharField(max_length=30)
    Internship_discription = models.TextField()
    Location = models.CharField(max_length=50)
    job_type = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    deadline = models.CharField(max_length=50)
    type = models.ForeignKey(PostType, on_delete=models.CASCADE)

    def __str__(self):
        return self.comp_name
