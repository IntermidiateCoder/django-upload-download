from django.urls import re_path, path
from . import views

# namespace
app_name = "file_upload"

urlpatterns = [
    # Upload File
    re_path(r"^upload/$", views.file_upload, name="file_upload"),
    # View File List
    path("", views.file_list, name="file_list"),
]
