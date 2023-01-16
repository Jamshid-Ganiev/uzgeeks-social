from django.urls import path
from .views import ListGroups, CreateGroup, SingleGroup, JoinGroup, LeaveGroup

app_name = 'groups'

urlpatterns = [
    path('', ListGroups.as_view(), name="all"),
    path("new/", CreateGroup.as_view(), name="create"),
    path("posts/in/<slug>/", SingleGroup.as_view(), name="single"),
    path("join/<slug>/", JoinGroup.as_view(), name="join"),
    path("leave/<slug>/", LeaveGroup.as_view(), name="leave"),
]
