from django.db import models


class Screenshot(models.Model):
    """
    Class for storing the screenshots.

    ARGS:
    """

    description = models.TextField(blank=True,
                                   null=True)
    image = models.ImageField('Label')
    image_url = models.TextField(blank=True,
                                 null=True,
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

    def json(self):
        """
        Return the JSON dict of the object.

        ARGS:
        """
        return {
            'Description': self.description,
            'image_name': str(self.image),
            'image_url': self.image_url,
            'viewport': self.viewport,
            'timestamp': self.created
        }
