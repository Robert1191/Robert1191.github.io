from django.conf.urls import url, include
from django.contrib import admin


# # Default
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url('MYC_App/', include('MYC_App.urls')),
# ]

# Now the home page will direct to the index file in AUT AR web app
urlpatterns = [
    url('', include('autarWebApp.urls')),
    url('assets/', include('autarWebApp.urls')),
    url('images/', include('autarWebApp.urls')),
]