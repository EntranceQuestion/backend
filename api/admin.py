from django.contrib import admin
from . import models

admin.site.register(models.ModelQuestion)

# change headlines
admin.site.site_header = "EntranceQuestion.com admin portal"
admin.site.site_title = "EntranceQuestion"
admin.site.index_title = "Administration"
