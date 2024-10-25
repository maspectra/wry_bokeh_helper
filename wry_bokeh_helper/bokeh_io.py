from __future__ import annotations

import io
import json
import urllib.request
from typing import TYPE_CHECKING, Any

from PIL import Image

from wry_bokeh_helper._wry_bokeh_helper import render_bokeh

if TYPE_CHECKING:
    from wry_bokeh_helper._wry_bokeh_helper import ResourceType


def bokeh_to_image(
    bokeh_json_item: dict[str, Any],
    resource: tuple[ResourceType, str] | None = None,
) -> Image.Image:
    """Make bokeh plot to PIL.Image."""

    png = render_bokeh(json.dumps(bokeh_json_item), resource)
    response = urllib.request.urlopen(png)
    return Image.open(io.BytesIO(response.read()))
