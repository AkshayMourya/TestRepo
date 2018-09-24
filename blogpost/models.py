from django.db import models


class blog_post(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    created_by = models.CharField(max_length=30)
    created_at = models.CharField(max_length=20)

    class Meta:
        db_table = "blog_details"
