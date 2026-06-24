from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    # Importamos las rutas de login/logout nativas de Django
    path('accounts/', include('django.contrib.auth.urls')), 
    # Redirigimos la raíz de la página directamente al login
    path('', RedirectView.as_view(url='accounts/login/', permanent=False)),
]
