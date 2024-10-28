from __future__ import annotations

import io
import json
import os
import pathlib
import urllib.request
from typing import TYPE_CHECKING, Any, overload

from PIL import Image

from wry_bokeh_helper._wry_bokeh_helper import render_bokeh

if TYPE_CHECKING:
    from wry_bokeh_helper._wry_bokeh_helper import ResourceType

    try:
        from bokeh.embed.standalone import StandaloneEmbedJson
        from bokeh.models import Model

    except ImportError:
        Model = Any
        StandaloneEmbedJson = dict[str, Any]

    BokehFigureOrStandaloneJson = Model | StandaloneEmbedJson


@overload
def bokeh_to_image(
    bokeh_figure_or_bokeh_standalone_json: BokehFigureOrStandaloneJson,
    *,
    resource: tuple[ResourceType, str] | None = None,
) -> Image.Image:
    """
    Converts a Bokeh figure or standalone JSON to an image.

    Args:
        bokeh_figure_or_bokeh_standalone_json (BokehFigureOrStandaloneJson):
            The Bokeh figure or standalone JSON to convert.
        resource (tuple[ResourceType, str] | None, optional):
            Additional resources required for the conversion. Defaults to None.

    Returns:
        Image.Image: The resulting image.
    """
    ...


@overload
def bokeh_to_image(
    bokeh_figure_or_bokeh_standalone_json: BokehFigureOrStandaloneJson,
    filepath: os.PathLike[str] | str,
    *,
    dpi: int = 300,
    resource: tuple[ResourceType, str] | None = None,
) -> None:
    """
    Save a Bokeh plot to a specified file path.

    Parameters:
        bokeh_figure_or_bokeh_standalone_json (BokehFigureOrStandaloneJson):
            The Bokeh figure or standalone JSON to be saved as an image.
        filepath (os.PathLike[str] | str):
            The file path where the image will be saved.
        dpi (int, optional):
            The resolution of the saved image in dots per inch. Default is 300.
        resource (tuple[ResourceType, str] | None, optional):
            Additional resources required for saving the image. Default is None.

    Returns:
        None
    """
    ...


def bokeh_to_image(
    bokeh_figure_or_bokeh_standalone_json: BokehFigureOrStandaloneJson,
    filepath: os.PathLike[str] | str | None = None,
    *,
    dpi: int = 300,
    resource: tuple[ResourceType, str] | None = None,
) -> Image.Image | None:
    if isinstance(bokeh_figure_or_bokeh_standalone_json, dict):
        bokeh_json_item = bokeh_figure_or_bokeh_standalone_json

    else:
        try:
            from bokeh.embed.standalone import json_item
            from bokeh.models import Model
        except ImportError:
            raise ImportError("bokeh is not installed.")
        if not isinstance(bokeh_figure_or_bokeh_standalone_json, Model):
            raise TypeError(
                "bokeh_figure_or_bokeh_standalone_json must be a Bokeh Model."
            )
        bokeh_json_item = json_item(bokeh_figure_or_bokeh_standalone_json)

    png = render_bokeh(json.dumps(bokeh_json_item), dpi, resource)
    response = urllib.request.urlopen(png)
    img = Image.open(io.BytesIO(response.read()))

    if filepath:
        # if want jpg, convert RGBA to RGB
        filepath = pathlib.Path(filepath)
        if filepath.suffix == ".jpg" or filepath.suffix == ".jpeg":
            img = img.convert("RGB")
        return img.save(filepath, dpi=(dpi, dpi))
    return img
