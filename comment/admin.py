from django.contrib import admin

# Register your models here.

from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('course', 'customer_name', 'date', 'happy',)
    list_filter = ('course', 'date',)
    search_fields = ('course__name', 'details',)

    class Meta:
        model = Feedback


admin.site.register(Feedback, FeedbackAdmin)
