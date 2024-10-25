from wry_bokeh_helper import export_bokeh_to_png

img = export_bokeh_to_png(
    {
        "target_id": None,
        "root_id": "p1001",
        "doc": {
            "version": "3.4.3",
            "title": "",
            "roots": [
                {
                    "type": "object",
                    "name": "Figure",
                    "id": "p1001",
                    "attributes": {
                        "x_range": {
                            "type": "object",
                            "name": "DataRange1d",
                            "id": "p1002",
                        },
                        "y_range": {
                            "type": "object",
                            "name": "DataRange1d",
                            "id": "p1003",
                        },
                        "x_scale": {
                            "type": "object",
                            "name": "LinearScale",
                            "id": "p1010",
                        },
                        "y_scale": {
                            "type": "object",
                            "name": "LinearScale",
                            "id": "p1011",
                        },
                        "title": {"type": "object", "name": "Title", "id": "p1008"},
                        "renderers": [
                            {
                                "type": "object",
                                "name": "GlyphRenderer",
                                "id": "p1039",
                                "attributes": {
                                    "data_source": {
                                        "type": "object",
                                        "name": "ColumnDataSource",
                                        "id": "p1033",
                                        "attributes": {
                                            "selected": {
                                                "type": "object",
                                                "name": "Selection",
                                                "id": "p1034",
                                                "attributes": {
                                                    "indices": [],
                                                    "line_indices": [],
                                                },
                                            },
                                            "selection_policy": {
                                                "type": "object",
                                                "name": "UnionRenderers",
                                                "id": "p1035",
                                            },
                                            "data": {
                                                "type": "map",
                                                "entries": [
                                                    [
                                                        "x",
                                                        {
                                                            "type": "ndarray",
                                                            "array": {
                                                                "type": "bytes",
                                                                "data": "qIcBvBUc3T/5AmhjuaroPwxaHHb+ke4/CVM3Jd+/4D9HExbxgPHrPwBuYg2fibQ/0l+PFWpb1T+JX1fj/W3oPwBA6EU5Zks/YeqsQ2K+5T8=",
                                                            },
                                                            "shape": [10],
                                                            "dtype": "float64",
                                                            "order": "little",
                                                        },
                                                    ],
                                                    [
                                                        "y",
                                                        {
                                                            "type": "ndarray",
                                                            "array": {
                                                                "type": "bytes",
                                                                "data": "1PH9S//hwz/3aRoCMpjtP2gOtMgkfLI/iCpb1RTC7z+JL5tvNUXiP9A6xwykDMc/IsoFOpEp4D/j9ibUCjvmP54HOJulMOw/bnnYNXuk6T8=",
                                                            },
                                                            "shape": [10],
                                                            "dtype": "float64",
                                                            "order": "little",
                                                        },
                                                    ],
                                                ],
                                            },
                                        },
                                    },
                                    "view": {
                                        "type": "object",
                                        "name": "CDSView",
                                        "id": "p1040",
                                        "attributes": {
                                            "filter": {
                                                "type": "object",
                                                "name": "AllIndices",
                                                "id": "p1041",
                                            }
                                        },
                                    },
                                    "glyph": {
                                        "type": "object",
                                        "name": "Line",
                                        "id": "p1036",
                                        "attributes": {
                                            "x": {"type": "field", "field": "x"},
                                            "y": {"type": "field", "field": "y"},
                                            "line_color": "#1f77b4",
                                        },
                                    },
                                    "nonselection_glyph": {
                                        "type": "object",
                                        "name": "Line",
                                        "id": "p1037",
                                        "attributes": {
                                            "x": {"type": "field", "field": "x"},
                                            "y": {"type": "field", "field": "y"},
                                            "line_color": "#1f77b4",
                                            "line_alpha": 0.1,
                                        },
                                    },
                                    "muted_glyph": {
                                        "type": "object",
                                        "name": "Line",
                                        "id": "p1038",
                                        "attributes": {
                                            "x": {"type": "field", "field": "x"},
                                            "y": {"type": "field", "field": "y"},
                                            "line_color": "#1f77b4",
                                            "line_alpha": 0.2,
                                        },
                                    },
                                },
                            }
                        ],
                        "toolbar": {
                            "type": "object",
                            "name": "Toolbar",
                            "id": "p1009",
                            "attributes": {
                                "tools": [
                                    {
                                        "type": "object",
                                        "name": "PanTool",
                                        "id": "p1022",
                                    },
                                    {
                                        "type": "object",
                                        "name": "WheelZoomTool",
                                        "id": "p1023",
                                        "attributes": {"renderers": "auto"},
                                    },
                                    {
                                        "type": "object",
                                        "name": "BoxZoomTool",
                                        "id": "p1024",
                                        "attributes": {
                                            "overlay": {
                                                "type": "object",
                                                "name": "BoxAnnotation",
                                                "id": "p1025",
                                                "attributes": {
                                                    "syncable": False,
                                                    "level": "overlay",
                                                    "visible": False,
                                                    "left": {
                                                        "type": "number",
                                                        "value": "nan",
                                                    },
                                                    "right": {
                                                        "type": "number",
                                                        "value": "nan",
                                                    },
                                                    "top": {
                                                        "type": "number",
                                                        "value": "nan",
                                                    },
                                                    "bottom": {
                                                        "type": "number",
                                                        "value": "nan",
                                                    },
                                                    "left_units": "canvas",
                                                    "right_units": "canvas",
                                                    "top_units": "canvas",
                                                    "bottom_units": "canvas",
                                                    "line_color": "black",
                                                    "line_alpha": 1.0,
                                                    "line_width": 2,
                                                    "line_dash": [4, 4],
                                                    "fill_color": "lightgrey",
                                                    "fill_alpha": 0.5,
                                                },
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "name": "SaveTool",
                                        "id": "p1030",
                                    },
                                    {
                                        "type": "object",
                                        "name": "ResetTool",
                                        "id": "p1031",
                                    },
                                    {
                                        "type": "object",
                                        "name": "HelpTool",
                                        "id": "p1032",
                                    },
                                ]
                            },
                        },
                        "left": [
                            {
                                "type": "object",
                                "name": "LinearAxis",
                                "id": "p1017",
                                "attributes": {
                                    "ticker": {
                                        "type": "object",
                                        "name": "BasicTicker",
                                        "id": "p1018",
                                        "attributes": {"mantissas": [1, 2, 5]},
                                    },
                                    "formatter": {
                                        "type": "object",
                                        "name": "BasicTickFormatter",
                                        "id": "p1019",
                                    },
                                    "major_label_policy": {
                                        "type": "object",
                                        "name": "AllLabels",
                                        "id": "p1020",
                                    },
                                },
                            }
                        ],
                        "below": [
                            {
                                "type": "object",
                                "name": "LinearAxis",
                                "id": "p1012",
                                "attributes": {
                                    "ticker": {
                                        "type": "object",
                                        "name": "BasicTicker",
                                        "id": "p1013",
                                        "attributes": {"mantissas": [1, 2, 5]},
                                    },
                                    "formatter": {
                                        "type": "object",
                                        "name": "BasicTickFormatter",
                                        "id": "p1014",
                                    },
                                    "major_label_policy": {
                                        "type": "object",
                                        "name": "AllLabels",
                                        "id": "p1015",
                                    },
                                },
                            }
                        ],
                        "center": [
                            {
                                "type": "object",
                                "name": "Grid",
                                "id": "p1016",
                                "attributes": {"axis": {"id": "p1012"}},
                            },
                            {
                                "type": "object",
                                "name": "Grid",
                                "id": "p1021",
                                "attributes": {"dimension": 1, "axis": {"id": "p1017"}},
                            },
                        ],
                    },
                }
            ],
        },
        "version": "3.4.3",
    },
    resource=(
        "local",
        "/Users/johnnyxcy/Workspace/mas/repositories/plotting-prototype/.venv/lib/python3.10/site-packages/bokeh/server/static/js",
    ),
)

img.show()
