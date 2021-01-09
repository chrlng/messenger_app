import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc

def get_footer_layout():
    """ Return the layout for the footer.
    """
    return html.Div(
        className = "col",
        id = "footer-container",
        children = [
            html.P(
                className = "white-font",
                children = [
                    "Made By ",
                    html.A(
                        href = "https://chrlng.github.io/", 
                        className = "side-font white-font",
                        id = "link-to-me",
                        children = [
                            "Christine Nguyen", 
                        ]
                    )
                ],
            ),
        ]
    )