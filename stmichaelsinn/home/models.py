from django.db import models

from wagtail.core.models import Page

from uwkm_streamfields.blocks import GridBlock

class HomePage(Page):
    some_content = StreamField(
        [('fixed_width', blocks.ListBlock(
            GridBlock(),
            template = 'streamfields/fixed_grid.html',
            icon='fa-th-large',
            label='Boxed'))
        ,('full_width', blocks.ListBlock(
            GridBlock(),
            template = 'streamfields/full_grid.html',
            icon='fa-th',
            label='Full'))
        ],
        null = True,
        blank = True
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('some_content'),
    ]