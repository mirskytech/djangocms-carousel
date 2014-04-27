djangocms-carousel
==================

A Carousel for django CMS.


Installation
------------

This plugin requires `django CMS` 2.4 or higher to be properly installed.

* In your projects `virtualenv`_, run ``pip install djangocms-carousel``.
* Add ``'djangocms_carousel'`` to your ``INSTALLED_APPS`` setting.
* Run ``manage.py migrate cmsplugin_carousel``.


Usage
-----

There are 2 plugins: Carousel and Slide
The first is Carousel that should be added to your placeholder conf.
Carousel only allows one plugin as a child: the Slide plugin.




