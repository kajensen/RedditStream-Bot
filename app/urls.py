from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import bot.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^threads/update', bot.views.update, name='update'),
    url(r'^threads/live', bot.views.get, name='live'),
    url(r'^admin/', include(admin.site.urls)),
]
