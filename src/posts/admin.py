from django.contrib import admin

# Register your models here.
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title","__str__","timestamp"]
	list_filter = ["title","updated","timestamp"]
	search_fields = ["title","content"]
	class Meta:
		model = Post


admin.site.register(Post,PostModelAdmin)