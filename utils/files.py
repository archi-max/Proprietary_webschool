from django.core.exceptions import ValidationError
import uuid
import os


def filename_generator(instance, filename, folder_name):
    """Generate filenames. They are stored inside in the given folder_name folder in UploadedFiles folder =."""
    folder = f"UploadedFiles\\{folder_name}"
    try:
        os.makedirs(folder)
    except FileExistsError:
        pass
    return f"{folder}\\{uuid.uuid4().hex}{filename}"


def document_fileextension_validator(value, valid_extensions=['.pdf', '.doc', '.docx']):
    """Validate the file extension of the uploaded file."""
    import os
    ext = os.path.splitext(value.name)[1]
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')
