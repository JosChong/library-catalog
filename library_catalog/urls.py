"""library_catalog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin

from libapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^view/$', views.BookListView.as_view(), name = 'book_list_view'),
    url(r'^view/(?P<pk>\d{13})/$',views.BookDetailView.as_view(), name = 'book_detail_view'),

    url(r'^add/$', views.BookAddView.as_view(), name = 'book_add_view'),
    url(r'^update/(?P<pk>\d{13})/$', views.BookUpdateView.as_view(), name = 'book_update_view'),
    url(r'^update_what/$', views.update_what_view, name = 'update_what_view'),
    url(r'^remove/(?P<pk>\d{13})/$', views.BookRemoveView.as_view(), name = 'book_remove_view'),
    url(r'^remove_what/$', views.remove_what_view, name = 'remove_what_view'),

    url(r'^accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
