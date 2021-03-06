from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import (FieldPanel, StreamFieldPanel)
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from streams import blocks as stream_blocks


class HomePage(Page):

    # main company info, usually a hero image
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Large image on the home page.")
    hero_name = models.CharField(
        max_length=255,
        help_text="Place name. Shown if no logo image.")
    hero_logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Place logo. If none, defaults to place name.")

    # business has 3 facets and should come after hero image.
    facets = StreamField([
            ('facet', stream_blocks.HomeFacetBlock(
                required=False,
                max_length=650,
                help_text='E.g. Restuarant, Hotel, Function Hall')),
        ])

    # extra streamfields
    # body =  StreamField([])

    footer = models.ForeignKey(
        'webbase.Footer',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+')

    content_panels = Page.content_panels + [
        FieldPanel('hero_image'),
        FieldPanel('hero_name'),
        FieldPanel('hero_logo'),
        StreamFieldPanel('facets'),
        # StreamFieldPanel('body'),
        SnippetChooserPanel("footer"),
    ]


    class Meta:
        verbose_name = "homepage"