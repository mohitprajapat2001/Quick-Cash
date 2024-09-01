from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static
from schema_graph.views import Schema
from quickcash.views import InfoView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", RedirectView.as_view(url="dashboard"), name="index"),
    path("accounts/", include("accounts.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("banking/", include("banking.urls")),
    path("quickcash/info/", InfoView.as_view(), name="info"),
    path("schema/", Schema.as_view(), name="models-schema"),
] + debug_toolbar_urls()

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
