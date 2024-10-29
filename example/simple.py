import numpy as np
from bokeh.plotting import figure, show

from wry_bokeh_helper import bokeh_to_image

if __name__ == "__main__":
    p = figure()
    x = np.linspace(0, 4 * np.pi, 100)
    y = np.sin(x)
    p.line(x, y, line_color="#1f77b4")
    p.height_policy = "max"
    p.width_policy = "max"

    p.height = 400
    p.width = 400
    show(p)

    bokeh_to_image(
        p,
        "a.png",
        dpi=300,
    )

    bokeh_to_image(
        p,
        "b.png",
        dpi=96,
    )
