import numpy as np
import pyecharts.options as opts
from pyecharts.charts import Surface3D
# ----------------- The plot ---------------------
# Get the data of the drawn image
def create_data():
    data = []
    for i in np.arange(-10, 10, 0.1):
        for j in np.arange(-10, 10, 0.1):
            x = i
            y = j
            z = 0.5 - (np.sin(np.sqrt(x**2+y**2))**2 - 0.5) / (1 + 0.001*(x**2 + y**2)**2)
            data.append([x, y, z])
            # If there is no downlink code, it will not be displayed
    data = [[item[1], item[0], item[2]] for item in data]
    return data
# Use pyecharts The plot
def draw():
    (
    # Surface3D(init_opts=opts.InitOpts(width="1600px", height="800px"))
    Surface3D()
    .add(
    series_name="f(x,y)",
    shading="color",
    data=list(create_data()),
    xaxis3d_opts=opts.Axis3DOpts(type_="value"),
    yaxis3d_opts=opts.Axis3DOpts(type_="value"),
    grid3d_opts=opts.Grid3DOpts(width=100, height=40, depth=100),
    )
    .set_global_opts(
    title_opts=opts.TitleOpts(title="z=f(x,y)"),
    visualmap_opts=opts.VisualMapOpts(
    dimension=2,
    max_=1,
    min_=-1,
    range_color=[
    "#313695",
    "#4575b4",
    "#74add1",
    "#abd9e9",
    "#e0f3f8",
    "#ffffbf",
    "#fee090",
    "#fdae61",
    "#f46d43",
    "#d73027",
    "#a50026",
    ],
    )
    )
    .render("res.html")
    )
