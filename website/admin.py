from django.contrib import admin
from .models import Event, Report, Home_image, Gallery, Gallery_image, Visitor_counter
# Register your models here.

admin.site.register(Event)
admin.site.register(Report)
admin.site.register(Home_image)
admin.site.register(Gallery)
admin.site.register(Gallery_image)
admin.site.register(Visitor_counter)