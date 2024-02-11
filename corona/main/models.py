from django.db import models
from django.utils.translation import gettext_lazy as _


class MainCarousel(models.Model):
    title = models.CharField(_("title"), max_length=50)
    desctiption = models.TextField(_("desctiption"))
    image = models.ImageField(_("image"), upload_to="main_carosel/images")

    def __str__(self):
        return self.title
