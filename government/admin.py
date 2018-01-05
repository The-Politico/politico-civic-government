from django.contrib import admin

from .models import Body, Jurisdiction, Office, Party

admin.site.register(Body)
admin.site.register(Jurisdiction)
admin.site.register(Office)
admin.site.register(Party)
