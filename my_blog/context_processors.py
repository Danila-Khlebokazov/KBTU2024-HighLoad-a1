from django.conf import settings


def base_site_processor(request):
    return {
        'main_site_name': settings.SITE_NAME
    }
