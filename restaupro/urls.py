from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from restaupro import settings

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'host_management.views.home', name='home'),
    url(r'^profile/$', 'host_management.views.profile', name='profile'),
    url(r'^table_form/$', 'host_management.views.table_form', name='table_form'),
    url(r'^party_form/$', 'host_management.views.party_form', name='party_form'),
    url(r'^end_party/(?P<party_id>\w+)/$', 'host_management.views.end_party', name='end_party'),
    url(r'^profile/make_reservation_at_table/(?P<table_id>\w+)/$', 'host_management.views.make_reservation_at_table', name='make_reservation_at_table'),

    url(r'^register/$', 'host_management.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)