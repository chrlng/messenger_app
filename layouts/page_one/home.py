import dash_bootstrap_components as dbc
import dash_html_components as html

def get_home_layout():
    """ Return the layout for the landing page.
    """
    return html.Div(
        className = "col",
        id = "home-container",
        children = [
            html.Div(
                id = "home-row-subcontainer",
                className = "row",
                children = [
                    html.Div(
                        id = "home-left-subcontainer",
                        className = "col",
                        children = [
                            html.H3(
                                id = "home-subtitle",
                                children = ["let's see how you stay"]
                            ),
                            html.H1(
                                id = "home-title",
                                children = ["connected"]
                            ),
                            html.A(
                                children = [
                                    dbc.Button(
                                        "Learn More",
                                        color = "primary",
                                        id = "home-button"
                                    ),
                                ],
                                href = "#info-container"
                            ),
                        ]
                    ),
                    html.Img(
                        className = "floating",
                        id = "home-picture",
                        src = "assets/imgs/girl_pink_phone.svg"
                    )
                ]
            ), 
            html.Img(
                id = "blue-wave",
                src = "assets/imgs/blue_wave.png"
            ),
            html.Img(
                id = "purple-wave",
                src = "assets/imgs/purple_wave.png"
            ),
        ]
    )