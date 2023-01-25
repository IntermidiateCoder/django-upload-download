import os
import uuid

from django.shortcuts import render, redirect

from .forms import FileUploadForm
from .models import File


# Show file list
def file_list(request):
    files = File.objects.all().order_by("-id")
    return render(request, "file_upload/file_list.html", {"files": files})


# Regular file upload without using ModelForm
def file_upload(request):
    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # get cleaned data
            raw_file = form.cleaned_data.get("file")
            # Limit file size to 10MB
            if raw_file.size < 1024 * 1024 * 10:
                new_file = File()
                new_file.file = handle_uploaded_file(raw_file)
                new_file.file_name = raw_file.name
                new_file.file_size = raw_file.size
                new_file.save()
                return redirect("/file/")
    else:
        form = FileUploadForm()

    return render(
        request,
        "file_upload/upload_form.html",
        {"form": form, "heading": "Upload files with Regular Form"},
    )


def handle_uploaded_file(file):
    ext = file.name.split(".")[-1]
    file_name = "{}.{}".format(uuid.uuid4().hex[:10], ext)
    # file path relative to 'media' folder
    file_path = os.path.join("files", file_name)
    absolute_file_path = os.path.join("media", "files", file_name)

    directory = os.path.dirname(absolute_file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(absolute_file_path, "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    return file_path
