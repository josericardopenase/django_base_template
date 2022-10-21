from django.core.exceptions import NON_FIELD_ERRORS
from django.forms.utils import ErrorList
from rest_framework import serializers
from django.core.files.base import ContentFile
import base64
import six
import uuid

from rest_framework.exceptions import ValidationError


class TimestampField(serializers.Field):
    def to_representation(self, value):
        return value.timestamp()


class RelatedIdField(serializers.Field):
    def to_representation(self, value):
        return value.id


class BaseSerializer(serializers.ModelSerializer):
    error_class = ErrorList

    def __init__(self, *args, **kwargs):
        self.user = None
        super().__init__(*args, **kwargs)

    @property
    def verbose_errors(self):
        return self.errors

    def get_user(self):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        return user

    def remove_spaces(self, data, field):
        try:
            data[field] = data[field].replace(" ", "")
        except KeyError:
            pass
        except AttributeError:
            pass

    def add_error(self, error):
        if not isinstance(error, ValidationError):
            # Normalize to ValidationError and let its constructor
            # do the hard work of making sense of the input.
            error = ValidationError(error)

        if hasattr(error, "error_dict"):
            error = error.error_dict
        else:
            error = {NON_FIELD_ERRORS: error.error_list}

        for field, error_list in error.items():
            if field not in self.errors:
                if field == NON_FIELD_ERRORS:
                    self._errors[field] = self.error_class(error_class="nonfield")
                else:
                    self._errors[field] = self.error_class()
            self._errors[field].extend(error_list)
            if field in self.validated_data:
                del self.validated_data[field]


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):

        if isinstance(data, six.string_types):
            if "data:" in data and ";base64," in data:
                header, data = data.split(";base64,")

            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail("invalid_image")

            file_name = str(uuid.uuid4())[:12]
            file_extension = self.get_file_extension(file_name, decoded_file)
            complete_file_name = "%s.%s" % (
                file_name,
                file_extension,
            )
            data = ContentFile(decoded_file, name=complete_file_name)
        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension


class Base64PDFField(serializers.FileField):
    def to_internal_value(self, data):
        if isinstance(data, six.string_types):
            if "data:" in data and ";base64," in data:
                header, data = data.split(";base64,")
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail("invalid_pdf")

            file_name = str(uuid.uuid4())[:12]
            file_extension = self.get_file_extension(file_name, decoded_file)
            complete_file_name = "%s.%s" % (
                file_name,
                file_extension,
            )
            data = ContentFile(decoded_file, name=complete_file_name)
        return super(Base64PDFField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        return "pdf"
