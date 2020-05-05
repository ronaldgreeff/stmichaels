from wagtail.core import blocks

from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField


class HomeFacetBlock(blocks.StructBlock):
    """ Main home page blocks for each facet (restuarant, hotel, functions) """

    image = ImageChooserBlock(required=True)
    title = blocks.CharBlock(max_length=24)
    subtitle = blocks.CharBlock(max_length=32)
    paragraph = blocks.TextBlock(max_length=255)
    page = blocks.PageChooserBlock(required=False)

    class Meta:
        template = "streams/home_facet_block.html"
        icon = "edit"
        label = "Home Facet"


class FooterBlock(blocks.StructBlock):
    title = blocks.CharBlock(null=True, blank=True, max_length=24)
    text = RichTextField(null=True, blank=True)

    template = "streams/footer_block.html"
    icon = "edit"
    label = "Footer Block"