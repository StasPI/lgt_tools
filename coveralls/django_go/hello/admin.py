from django.contrib import admin

from hello.models import Staff, Supp1, Supp2, JobTitles, Supplier, ClothingSize, TypeOfClothing, Clothes


admin.site.register(Staff)

# ------------------------------------------------------------------------------------------
# Clothes
# ------------------------------------------------------------------------------------------

admin.site.register(Supplier)
admin.site.register(ClothingSize)
admin.site.register(TypeOfClothing)
admin.site.register(Clothes)

# ------------------------------------------------------------------------------------------
# Test
# ------------------------------------------------------------------------------------------

admin.site.register(Supp1)
admin.site.register(Supp2)
admin.site.register(JobTitles)
