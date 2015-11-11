from django.conf.urls import url
from api.views import DetailUpdateTodo
urlpatterns = [
    url(r'^todos/(?P<pk>\d+)', DetailUpdateTodo.as_view(), name='api_todo_detail_update'),
    url(r'^todos/', 'api.views.list_create_todo'),
]
