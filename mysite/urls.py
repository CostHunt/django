from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import path, include

schema_view = get_schema_view(
    openapi.Info(
        title="Cost hunt API",
        default_version='v1',
        description="Cost hunt API dev hunt 2024",
        terms_of_service="https://www.costhunt.com/terms/",
        contact=openapi.Contact(email="rafranckyam04@gmail.com"),
        license=openapi.License(name="Cost hunt license"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('costhunt/api/', include('render.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
