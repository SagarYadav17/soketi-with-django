from django.contrib import admin
from django.urls import path


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.conf import settings


class HelloView(APIView):
    def get(self, request):
        json_data = {}

        settings.pusher_client.trigger(
            channels=["my-channel"],
            event_name="my-event",
            data=json_data,
        )

        return Response(data={"hello": "world"}, status=status.HTTP_200_OK)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HelloView.as_view()),
]
