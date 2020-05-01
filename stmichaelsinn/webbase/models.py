from django.db import models
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.snippets.models import register_snippet

from streams import blocks as stream_blocks

class Footer(models.Model):

    footer_block = StreamField(
        [
            ("footer_block", stream_blocks.FooterBlock(
                required=False,
                help_text='title and text'))
        ],
        null=True, blank=True
    )

    panels = [
        StreamFieldPanel('footer_block')
    ]

    def __str__(self):
        return self.footer_block.title

register_snippet(Footer)