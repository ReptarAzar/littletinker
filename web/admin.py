from PIL import Image
from django.contrib import admin
from web.models import Category, Project, ProjectImage

class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ['image', 'projectId', 'thumbnail']
    ordering = ['id']
    actions = ['generate_thumbnails']

    def generate_thumbnails(self, request, queryset):
        size = 128, 128
        for largeImage in queryset:
            image = Image.open(largeImage.image.path)
            image.thumbnail(size, Image.ANTIALIAS)
            image.save(largeImage.image.path[:-4] + "_thumb.jpg", "JPEG")

        rows_updated = queryset.update(thumbnail = True)
        if rows_updated == 1:
            message_bit = "1 image thumbnail was"
        else:
            message_bit = "%s image thumbnails were" % rows_updated
        self.message_user(request, "%s generated." % message_bit)
    generate_thumbnails.short_description = "Generate thumbnails for selected images"

admin.site.register(Category)
admin.site.register(Project)
admin.site.register(ProjectImage,ProjectImageAdmin)