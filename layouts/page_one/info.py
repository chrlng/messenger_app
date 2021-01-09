import dash_bootstrap_components as dbc
import dash_html_components as html


def get_info_layout():
    """ Return the layout for the upload page.
    """
    return html.Div(
        id = "info-container",
        className = "col",
        children = [
            html.Div(
                id = "info-content-container",
                className = "row",
                children = [
                    html.Img(
                        id = "info-pic",
                        src = "assets/imgs/blue_phone_person.svg",
                    ), 
                    html.Div(
                        className = "col",
                        id = "info-text-subcontainer", 
                        children = [
                            html.H4(
                                className = "side-font",
                                id = "info-subtitle", 
                                children = ["What is this?"]
                            ),
                            html.H1(
                                className = "main-font",
                                id = "info-title",
                                children = ["Analyze your Facebook Messenger Data"]
                            ),
                            html.H6(
                                className = "side-font",
                                id = "info-text-one",
                                children = "See some trends in the way you message people on Facebook Messenger"
                            ),
                            html.H6(
                                className = "side-font",
                                id = "info-text-two",
                                children = ["Don't worry! None of your information is being stored."]
                            ),
                            html.A(
                                children = [
                                    dbc.Button(
                                        "Still Interested?",
                                        color = "primary",
                                        id = "info-button"
                                    ),
                                ],
                                href = "/analyze"
                            ),
                        ]
                    )
                ]
            ),
            # html.Img(
            #     id = "info-border",
            #     src = "/assets/imgs/border.png"
            # )
        
        ]
    )