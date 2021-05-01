from django.contrib import admin
from .models import Post,Category,PotographyPost,Signup
# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(PotographyPost)
admin.site.register(Signup)
