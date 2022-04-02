from django.contrib import admin
from django.urls import path, include

from school.views import students_list

admin.site.site_header = 'Моя админка'
admin.site.index_title = 'Супер админка'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', students_list, name='students'),
    path('__debug__/', include('debug_toolbar.urls')),

]
