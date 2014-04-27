from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

class Carousel(CMSPlugin):
    """
    A plugin that has sub Slide classes
    """
    def __unicode__(self):
        return _(u"%s slides") % self.cmsplugin_set.all().count()


class Slide(CMSPlugin):
    """
    A Column for the Carousel Plugin
    """

    def __unicode__(self):
        return u"Slide %s" % self.get_position_in_placeholder()

