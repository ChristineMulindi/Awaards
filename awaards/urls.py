from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$',views.home,name = 'home'),
    url(r'^profile/(\d+)', views.profile, name='profile'),
    url(r'^update/profile/(\d+)$', views.update_profile, name='update-profile'),
    url(r'^search/',views.search_by_site, name='search_by_site'),
    url(r'^post/project/(\d+)$', views.post_project, name='post_project'),
    url(r'^main/(\d+)$', views.main, name='main'),
    url(r'^rating/(\d+)$', views.rating, name='rating'),
    url(r'^project/(\d+)$', views.project, name='project'),
    url(r'^api/profile/$', views.ProfileList.as_view()),  
    url(r'^api/project/$', views.ProjectList.as_view()),
    url(r'api/profile/profile-id/(?P<pk>[0-9]+)/$',
        views.ProjectDescription.as_view()),
    url(r'api/project/project-id/(?P<pk>[0-9]+)/$',
        views.ProjectDescription.as_view())

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
