import plotly 
import plotly.graph_objs as go

import pandas as pd

def graph_msg_exchanged_month():
    """ Return a barchart figure that shows how many messages you sent and received per month.
    """
    fig = go.Figure()

    dates = pd.date_range('2018-01', '2018-12', freq = 'MS')
    fig.add_bar(x = dates, y = msgs_received_per_month_df['count'], name = 'messages received')
    fig.add_bar(x = dates, y = counts_per_month_df['count'], name = 'messages sent')
    fig.layout.xaxis.tickvals = pd.date_range('2018-01', '2018-12', freq = 'MS')
    fig.layout.xaxis.tickformat = '%b'
    fig.update_layout(
        title = 'Messages Exchanged per Month',
        xaxis_title = 'Month',
        yaxis_title = 'Count'
    )
    return fig 