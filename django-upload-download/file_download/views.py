import os

from django.http import Http404, FileResponse


# Limit file download type
def file_response_download(request, file_path: str) -> FileResponse:
    ext = os.path.basename(file_path).split(".")[-1].lower()
    # cannot be used to download py, db and sqlite3 files.
    if ext not in ["py", "db", "sqlite3"]:
        response = FileResponse(open(file_path, "rb"))
        response["content_type"] = "application/octet-stream"
        response["Content-Disposition"] = "attachment; filename=" + os.path.basename(
            file_path
        )
        return response
    else:
        raise Http404
