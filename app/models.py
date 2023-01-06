from mongoengine import *
from datetime import datetime


class ShortUrlModel(Document):
    created_at = DateTimeField(default = datetime.now())
    longurl = StringField(required = True)
    shorturl = StringField(required = True)

    meta = {
        'collection' : 'ShortUrls',
        'indexes' : ['shorturl']
    }