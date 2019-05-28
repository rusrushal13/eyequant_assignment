import os
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from screenshot_api.utilities import good_url, save_image
from rest_framework.views import APIView
from screenshot_api import constants
import requests
from eyequant_api_project.settings import base
from screenshot_api.models import Screenshot


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
            return JsonResponse(
                {
                    'status': constants.STATUS_400,
                    'message': constants.BAD_REQUEST_MESSAGE,
                    'data': []
                }
            )

        image_url = constants.THUM_URL.format(url)
        try:
            image = Screenshot.objects.get(
                image_url=url)
            if not new:
                if view:
                    return render(
                        request,
                        'screenshot.html', {
                            'screenshot_url': os.path.join(
                                base.MEDIA_URL, image.image.name
                            ),
                            'screenshot': image
                        })
                else:
                    return JsonResponse(image.json())

            else:
                image.delete()
                raise Screenshot.DoesNotExist

        except Screenshot.DoesNotExist:
            response = requests.get(image_url)

            if response.status_code == 200:
                image = save_image(url,
                                   description,
                                   viewport,
                                   response)

                if view:
                    s_url = os.path.join(base.MEDIA_URL, image.image.name)
                    print(s_url)
                    return render(request, 'screenshot.html', {
                        'screenshot_url': os.path.join(
                            base.MEDIA_URL, image.image.name
                        ),
                        'screenshot': image
                    })
                else:
                    return JsonResponse(image.json())


class ListScreenshotView(APIView):
    """List all the screenshot in chronological order."""

    def get(self, request):
        """
        List the screenshots chronologically.

        ARGS:
            request(Request Object)
        """
        params = request.query_params
        view = params.get('view')

        screenshots = Screenshot.objects.filter().order_by(
            '-created')
        if view:
            return render(request, 'list_screenshot.html', {
                'screenshots': screenshots
            })
        else:
            result = {}
            data = []
            for screenshot in screenshots:
                data.append(screenshot.json())

            result['message'] = constants.LIST_MESSAGE
            result['data'] = data
            result['status'] = constants.STATUS_200
            return JsonResponse(result)
