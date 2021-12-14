from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from retzepee.views import RecipeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipe/<int:pk>/', RecipeView.as_view(), name='recipe-detail'),
    path('recipe/<int:pk>/<slug:slug>/', RecipeView.as_view(), name='recipe-detail-with-slug'),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))
