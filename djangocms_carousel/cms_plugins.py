from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from djangocms_carousel.models import Carousel, Slide
from django.utils.translation import ugettext_lazy as _
from djangocms_carousel.forms import CarouselForm
from cms.models import CMSPlugin

class CarouselPlugin(CMSPluginBase):
    model = Carousel
    module = _("Carousel")
    name = _("Carousel")
    render_template = "cms/plugins/carousel.html"
    allow_children = True
    child_classes = ["CarouselPlugin"]
    form = CarouselForm

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder':placeholder,
        })
        return context

    def save_model(self, request, obj, form, change):
        response = super(CarouselPlugin, self).save_model(request, obj, form, change)
        for x in xrange(int(form.cleaned_data['create'])):
            col = Slide(parent=obj, placeholder=obj.placeholder, language=obj.language, position=CMSPlugin.objects.filter(parent=obj).count(), plugin_type=SlidePlugin.__name__)
            col.save()
        return response

class SlidePlugin(CMSPluginBase):
    model = Slide
    module = _("Carousel")
    name = _("Slide")
    render_template = "cms/plugins/slide.html"
    parent_classes = ["CarouselPlugin"]
    allow_children = True

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder':placeholder,
            })
        return context

plugin_pool.register_plugin(CarouselPlugin)
plugin_pool.register_plugin(SlidePlugin)
