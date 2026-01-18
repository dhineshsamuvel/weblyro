from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from website import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name="home"),
    path('services/', views.services, name="services"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('get-quote/', views.get_quote, name="get_quote"),
    path('thank-you/', views.thank_you, name="thank_you"),

    path('services/website-design/', views.website_design, name="website_design"),
    path('services/shopify/', views.shopify, name="shopify"),
    path('services/wordpress/', views.wordpress, name="wordpress"),
    path('services/redesign/', views.redesign, name="redesign"),
    path('services/speed/', views.speed, name="speed"),
    path('services/maintenance/', views.maintenance, name="maintenance"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
