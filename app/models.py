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


class AnalyticsModel(Document):
    clicked_at = DateTimeField(default = datetime.now())
    shorturl = StringField(required = True)
    ip_address = StringField()
    city = StringField()
    latlng = ListField()

    meta = {
        'collection' : 'ClickAnalytics',
        'indexes' : ['shorturl']
    }