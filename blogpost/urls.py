from django.conf.urls import url
from . import views
from django.conf.urls import url, include


urlpatterns = [
    url(r'^blog/', views.blog_post_post.as_view())

]