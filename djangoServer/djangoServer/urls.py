from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

# # Default
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url('MYC_App/', include('MYC_App.urls')),
# ]

# Now the home page will direct to the index file in AUT AR web app
urlpatterns = [
    url('', include('autarWebApp.urls')),
]
