import os
from django.shortcuts import render
from django.http import FileResponse, Http404
from screenshot_api.utilities import good_url, save_image
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from screenshot_api import constants
import requests
from eyequant_api_project.settings import base
from screenshot_api.models import Screenshot
from screenshot_api.serializers import ScreenshotSerializer


class FetchScreenshotView(APIView):
    """Grab the Screenshot using thum.io."""

    def get(self, request):
        """
        Fetch the screenshot using thum.io.

        ARGS:
            request(Request Object)
        """
        params = request.query_params
        url = params.get('url')
        description = params.get('description')
        new = params.get('new')
        view = params.get('view')
        viewport = params.get('viewport', 'desktop')

        if not good_url(url) or url is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        thum_image_url = constants.THUM_URL.format(url)
        try:
            image = Screenshot.objects.get(
                website_url=url)
            if not new:
                if view:
                    return render(
                        request,
                        'screenshot.html', {
                            'screenshot_url': os.path.join(
                                base.MEDIA_URL, image.image_url.name
                            ),
                            'screenshot': image
                        })
                else:
                    serializer = ScreenshotSerializer(image)
                    return Response(serializer.data)

            else:
                image.delete()
                raise Screenshot.DoesNotExist

        except Screenshot.DoesNotExist:
            response = requests.get(thum_image_url)

            if response.status_code == 200:
                image = save_image(url,
                                   description,
                                   viewport,
                                   response)

                if view:
                    return render(request, 'screenshot.html', {
                        'screenshot_url': os.path.join(
                            base.MEDIA_URL, image.image_url.name
                        ),
                        'screenshot': image
                    })
                else:
                    serializer = ScreenshotSerializer(image)
                    return Response(serializer.data)


class ListScreenshotView(APIView):
    """List all the screenshot in chronological order."""

    def get(self, request):
        """
        List the screenshots chronologically.

        ARGS:
            request(Request Object)
        """
        screenshots = Screenshot.objects.filter().order_by(
            '-created')
        return render(request, 'list_screenshot.html', {
            'screenshots': screenshots
        })


class MediaView(APIView):
    """View to serve the static media files in production."""

    def get(self, request, name):
        """
        Fetch the fileresponse for serving the static files.

        ARGS:
            name(str)
        """
        path = ''.join([base.BASE_DIR, base.MEDIA_URL, name])
        try:
            media_file = open(path, 'rb')
            return FileResponse(media_file)
        except FileNotFoundError:
            raise Http404


class ScreenshotViewSet(mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    """List of Screenshots for the Screenshot."""

    queryset = Screenshot.objects.all().order_by('-created')
    serializer_class = ScreenshotSerializer
