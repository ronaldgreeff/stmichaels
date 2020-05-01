from wagtail.core import blocks

from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField


class LinkStructValue(blocks.StructValue):
    """ Get the page url else button url """

    def url(self):
        button_page = self.get("button_page")
        button_url = self.get("button_url")
        if button_page:
            return button_page.url
        elif button_url:
            return button_url
        return None


class HomeFacetBlock(blocks.StructBlock):
    """ Main home page blocks for each facet (restuarant, hotel, functions) """

    title = blocks.CharBlock(max_length=24)
    subtitle = blocks.CharBlock(max_length=32)
    paragraph = blocks.TextBlock(max_length=255)
    image = ImageChooserBlock(required=True)

    class Meta:
        template = "streams/home_facet_block.html"
        icon = "edit"
        label = "Home Facet"
        value_class = LinkStructValue


class FooterBlock(blocks.StructBlock):
    title = blocks.CharBlock(null=True, blank=True, max_length=24)
    text = RichTextField(null=True, blank=True)

    template = "streams/footer_block.html"
    icon = "edit"
    label = "Footer Block"