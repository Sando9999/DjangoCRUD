from django.conf.urls import url
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    url(r'^$',views.OfficeListView.as_view(),name='list'),
    url(r'^(?P<pk>\d+)/$',views.OfficeDetailView.as_view(),name='detail'),
    url(r'^create/$',views.OfficeCreateView.as_view(),name='create'),
    url(r'^update/(?P<pk>\d+)/$',views.OfficeUpdateView.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)/$',views.OfficeDeleteView.as_view(),name='delete'),




    ]
