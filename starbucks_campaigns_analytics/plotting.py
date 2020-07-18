import pandas as pd
import plotly_express as px

from plotly.graph_objects import Figure


def funnel_plot(df_to_plot: pd.DataFrame,
                x: str,
                y: str,
                color: str = None,
                color_discrete_map: dict = {},
                color_discrete_sequence: list = px.colors.qualitative.Plotly) \
        -> Figure:
    """Plots a funnel for `df_to_plot` data using `x` as volume,
    `y` as the steps column and `color` to differentiate by
    another column if necessary (optional).

    it's also possible to use parameters color_discrete_map and
    color_discrete_sequence (optional).
    """
    return px.funnel(df_to_plot, x=x, y=y, color=color,
                     color_discrete_map=color_discrete_map,
                     color_discrete_sequence=color_discrete_sequence)