from django import forms
from djangocms_slide.models import Carousel
from django.utils.translation import ugettext_lazy as _

class CarouselForm(forms.ModelForm):
    NUM_SLIDES = (
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
        (6, "6"),
        (7, "7"),
        (8, "8"),
        (9, "9"),
        (10, "10"),
    )


    create = forms.ChoiceField(choices=NUM_SLIDE, label=_("Create Carousel"), help_text=_("Create this number of slides"))


    class Meta:
        model = Slider
        exclude = ('page', 'position', 'placeholder', 'language', 'plugin_type')
