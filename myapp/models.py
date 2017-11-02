from mongoengine import *


class Metadata(EmbeddedDocument):                   # class that inherits from
    tags = ListField(StringField())                 # Document.
    revisions = ListField(IntField())
    # Fields are specified by


class WikiPage(Document):                           # adding field objects as
    title = StringField(required=True)              # class attributes to the
    text = StringField()                            # document class.
    metadata = EmbeddedDocumentField(Metadata)
