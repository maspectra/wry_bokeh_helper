from typing import Literal

ResourceType = Literal["cdn", "local"]

def render_bokeh(json: str, resource: tuple[ResourceType, str] | None = None) -> str:
    """Render Bokeh JSON to a PNG or SVG image."""
    ...
