from django.contrib import admin
from fish.models import HairMaster, Locks, Hairdress, Color, Haircut, Category

class HairMasterInline (admin.ModelAdmin):  #(admin.TabularInline)
    #inlines = [CategoryInline]
    model = HairMaster
    extra = 3

    def __str__(self):
        return self.name

admin.site.register(HairMaster)
admin.site.register(Hairdress)
admin.site.register(Color)
admin.site.register(Haircut)
admin.site.register(Category)
admin.site.register(Locks)