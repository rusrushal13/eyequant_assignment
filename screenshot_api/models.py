from django.db import models


class Screenshot(models.Model):
    """
    Class for storing the screenshots.

    ARGS:
    """

    description = models.TextField(blank=True,
                                   null=True)
    image_url = models.ImageField('Label')
    website_url = models.TextField(blank=True,
                                 unique=True)
    viewport = models.CharField(blank=True,
                                null=True,
                                max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Dunder method for the description.

        ARGS:
        """
        return self.description or ""
