from django.contrib import admin

from api.models import Foods_opt, NE_Record, Pee_opt, Poop_opt

# Register your models here.

admin.site.register( NE_Record )
admin.site.register( Foods_opt )
admin.site.register( Pee_opt   )
admin.site.register( Poop_opt  )