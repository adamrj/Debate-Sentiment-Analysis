from django.conf.urls import url
from sentiment.views import IndexView, BarChartView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^bar_chart$', BarChartView.as_view(), name='bar_chart'),

]