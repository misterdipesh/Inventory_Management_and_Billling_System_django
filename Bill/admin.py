from django.contrib import admin

from .models import Bill,TemporatyStorage,SoldItem
admin.site.register(Bill)
admin.site.register(TemporatyStorage)
admin.site.register(SoldItem)
