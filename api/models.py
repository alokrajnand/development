from django.db import models

# Create your models here.


class jobline(models.Model):
    job_id = models.IntegerField()
    job_name = models.CharField(max_length=10)
    job_by_company = models.CharField(max_length=10)

    def __str__(self):
        return self.job_name
