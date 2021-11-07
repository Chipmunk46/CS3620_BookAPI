"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from books.views import BookViewSet, HorrorViewSet, ComedyViewSet, RomanceViewSet, MysteryViewSet, FantasyViewSet, HistoricalViewSet, ScienceFictionViewSet, BiographyViewSet, PoetryViewSet, ClassicsViewSet
from django.conf.urls.static import static
from django.conf import settings
from books import views

router = routers.SimpleRouter()
router.register('books', BookViewSet)
router.register('horror', HorrorViewSet)
router.register('comedy', ComedyViewSet)
router.register('romance', RomanceViewSet)
router.register('mystery', MysteryViewSet)
router.register('fantasy', FantasyViewSet)
router.register('historical', HistoricalViewSet)
router.register('sciencefiction', ScienceFictionViewSet)
router.register('biography', BiographyViewSet)
router.register('poetry', PoetryViewSet)
router.register('classics', ClassicsViewSet)

urlpatterns = [
    path('books/', views.book_list, name="book_list"),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)