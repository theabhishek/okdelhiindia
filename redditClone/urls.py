from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('users/', include('users.urls')),
    path('posts/', include('posts.urls')),
    path('subreddits/', include('subreddits.urls')),
    path('pg-rental/', include('pg_rental.urls')),
    path('delhi-wiki/', include('delhi_wiki.urls')),
    path('bus/', include('bus_service.urls')),
    path('coupons/', include('coupon_service.urls')),
    path('metro/', include('metro.urls')),
    path('medical/', include('medical.urls')),
    path('hotel/', include('hotel_service.urls')),
    path('jobs/', include('job_portal.urls')),
    path('lost-and-found/', include('lost_and_found.urls')),
    path('storytelling/', include('storytelling.urls')),
    path('news/', include('news.urls')),
    path('notifications/', include('notifications.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 