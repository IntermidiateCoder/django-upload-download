from django.db import models
import os
import uuid


def user_directory_path(filename: str):
    ext = filename.split(".")[-1]
    filename = "{}.{}".format(uuid.uuid4().hex[:10], ext)
    return os.path.join("files", filename)


class File(models.Model):
    file = models.FileField(upload_to='uploads/')
    # Important to add index
    file_name = models.CharField(max_length=255, db_index=True, default='')
    file_size = models.IntegerField(db_index=True, default=0)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
