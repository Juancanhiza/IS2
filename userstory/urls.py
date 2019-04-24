from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.UserStoryListView.as_view(),name = 'userstory_list'),
    url(r'^create/$',views.CreateUserStoryView.as_view(),name = 'create_userstory'),
    path(route= 'update_userstory/<int:pk>/', view = views.UpdateUserStoryView.as_view(),name = 'update_userstory'),
    url(r'^productbacklog/$',views.ProductBacklogListView.as_view(), name = 'product_backog'),
]