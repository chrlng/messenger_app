import dash_bootstrap_components as dbc
import dash_html_components as html

from .page_one.home import get_home_layout
from .page_one.info import get_info_layout
from .footer import get_footer_layout

def get_page_one_layout():
    """ Return the layout for page one.
    """
    return html.Div(
        children = [
            get_home_layout(),
            get_info_layout(),
            get_footer_layout()
        ]
    )