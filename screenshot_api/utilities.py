from urllib.parse import urlparse
from screenshot_api.models import Screenshot
from django.core.files.base import ContentFile
import uuid


def good_url(url):
    """
    Check the coming URL is valid or not.

    ARGS:
        url(str): Given URL
    """
    parsed_url = urlparse(url)
    if parsed_url.scheme not in ['http', 'https']:
        return False
    if parsed_url.netloc is None or parsed_url == '':
        return False
    return True


def save_image(url, description, viewport, response):
    """
    Save the response content as image in File System and DB.

    ARGS:
        url(str): URL from User.
        description(str): description for the image.
        viewport(str): viewport of the image.
        response(request.models.response object)
    """
    image_name = str(uuid.uuid4())
    screenshot = Screenshot.objects.create(
        description=description if description else "",
        image_url=url,
        viewport=viewport)

    screenshot.image.save(image_name,
                          ContentFile(response.content),
                          save=True)

    return screenshot
