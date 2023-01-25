from django import forms


ALLOWED_EXTENSIONS = ["jpg", "jpeg", "png", "gif", "pdf", "doc", "docx", "xls", "xlsx", "log", "txt"]


# Regular form
class FileUploadForm(forms.Form):
    file = forms.FileField(
        widget=forms.ClearableFileInput(attrs={"class": "form-control"})
    )

    def clean_file(self):
        file = self.cleaned_data["file"]
        ext = file.name.split(".")[-1].lower()
        # Check file extension, limiting file extenstions for security
        if ext not in ALLOWED_EXTENSIONS:
            raise forms.ValidationError(f"{ext} files are not allowed.")
        # return cleaned data is very important.
        return file
