from django.contrib import admin

from models import WeddingRSVP


class WeddingRSVPAdmin(admin.ModelAdmin):
	pass

admin.site.register(WeddingRSVP)
