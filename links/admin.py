from django.contrib import admin
from links.models import Link
# Register your models here.

class LinkAdmin(admin.ModelAdmin):
	list_display = ('title', 'url', 'submitted',)

admin.site.register(Link, LinkAdmin)
