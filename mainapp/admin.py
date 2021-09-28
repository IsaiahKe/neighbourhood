from django.contrib import admin
from .models import Alert, Category, Neighbourhood,Profile,Business

# Register your models here.
admin.site.register(Neighbourhood)
admin.site.register(Profile)
admin.site.register(Business)
admin.site.register(Alert)
admin.site.register(Category)