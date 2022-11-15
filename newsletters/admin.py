from django.contrib import admin

from .models import NewsletterSubscriber


class NewslettersAdmin(admin.ModelAdmin):
    list_display = ('email', 'signup_date')


admin.site.register(NewsletterSubscriber, NewslettersAdmin)
