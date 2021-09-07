from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in




# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50,null=True, blank=True)

    def __str__(self):
        return self.name


class Job(models.Model):
    job_type = models.ForeignKey(Category, on_delete= models.CASCADE, null=True,blank=True)
    title = models.CharField(max_length=50,null=True, blank=True)
    description = models.TextField(max_length=50,null=True, blank=True)
    start_data = models.DateField(null=True, blank=True)
    education = models.CharField(max_length=50,null=True, blank=True)
    experience = models.CharField(max_length=50,null=True, blank=True)
    external_title = models.CharField(max_length=50,null=True, blank=True)

    def __str__(self):
        return self.title


# def job_field(sender, created, instance , update_fields=["external_title"], **kwargs):
#     job = Job.objects.get(id = instance.id)
#     exfield = handlers.create_extrnal(job.title, job.id)
#     job.update(external_title = exfield)

# post_save.connect(job_field, sender=Job)



@receiver(post_save, sender=Job)
def attach_catalog(sender, **kwargs):
    if kwargs.get('created', False):
        print("Akash sharma")
        b = Job.objects.latest('id')
        Job.objects.filter(pk=b.id).update(external_title=kwargs.get('external_title'))
