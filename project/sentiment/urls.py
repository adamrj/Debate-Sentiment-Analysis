from django.conf.urls import url
from sentiment.views import IndexView, BarChartView, SecondView, LineChartView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^bar_chart$', BarChartView.as_view(), name='bar_chart'),
    url(r'^second$', SecondView.as_view(),name="second" ),
    url(r'^line_chart$', LineChartView.as_view(), name='line_chart'),


]