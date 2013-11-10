from django.contrib import admin

from models import WeddingRSVP


class WeddingRSVPAdmin(admin.ModelAdmin):
	readonly_fields = ('names', 'attending','dietary_restrictions', )

admin.site.register(WeddingRSVP, WeddingRSVPAdmin)
