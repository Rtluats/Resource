import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_file_size(value):
    valid_size = 2 * 1024 ** 2
    if value.size > valid_size:
        raise ValidationError(_("File too large. Max size 2 MB"))


def validate_file_type(value):
    if not value.name.endswith(".txt"):
        raise ValidationError(_("This type of file is not supported"))


def validate_date(value):
    now = datetime.date.today()
    if now <= value:
        raise ValidationError(_("Date must be in future or present, not in past"))




