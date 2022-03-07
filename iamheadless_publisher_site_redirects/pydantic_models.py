from typing import List, Optional

from django.shortcuts import reverse

from iamheadless_publisher_site.pydantic_models import BaseItemContentsPydanticModel, BaseItemDataPydanticModel, BaseItemPydanticModel

from .conf import settings



class RedirectDataPydanticModel(BaseItemDataPydanticModel):
    source_url: str
    destination_url: str


class RedirectPydanticModel(BaseItemPydanticModel):
    _data_model = RedirectDataPydanticModel
    _display_name_plural = 'redirects'
    _display_name_singular = 'redirect'
    _item_type = 'redirect'

    data: RedirectDataPydanticModel
