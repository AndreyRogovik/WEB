from mongoengine import Document
from mongoengine.fields import ReferenceField, DateTimeField, ListField, StringField, BooleanField


class Author(Document):
    fullname = StringField(required=True)
    born_date = DateTimeField()
    born_location = StringField()
    description = StringField()


class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField('Author', required=True)
    quote = StringField(required=True)
