from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
from CoderShop.models import Avatar, Producto, Vendedor, Cliente, Post

# Register your models here.


admin.site.register(Producto)

admin.site.register(Vendedor)

admin.site.register(Cliente)

admin.site.register(Avatar)

class DimensionesForm(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':20})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }

admin.site.register(Post, DimensionesForm)