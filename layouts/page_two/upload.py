import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc

def get_upload_layout():
    """
    """
    return html.Div(
        id = "upload-container",
        className = "col",
        children = [
            steps_one(),
            steps_two()
        ]
    )

def steps_one():
    """ Return the layout for the upload page.
    """
    return html.Div(
        className = "col",
        id = "steps-one-container",
        children = [
            html.H2(
                className = "main-font",
                id = "upload-title",
                children = ["How to Download Your Messenger Data"]
            ), 
            html.H6(
                className = "side-font indv-steps",
                children = ["1. Go to settings in Facebook."]
            ),
            # html.Div(
            #     id = "mes-step-one-img-container",
            #     className = "row",
            #     children = [
            #         html.Div(
            #             className = "img-container",
            #             children = [
            #                 html.Img(
            #                     id = "mes-step-one",
            #                     src = "assets/imgs/mes_step_one.png"
            #                 ),
            #             ]
            #         ),
            #         html.Div(
            #             className = "img-container",
            #             children = [
            #                 html.Img(
            #                     id = "mes-step-two",
            #                     src = "assets/imgs/mes_step_two.png"
            #                 ),
            #             ]
            #         ),
            #     ]
            # ),
            html.H6(
                className = "side-font indv-steps",
                children = ["2. On the left side bar, select 'Your Facebook Information'."]
            ),
            # html.Div(
            #     className = "img-container",
            #     children = [
            #         html.Img(
            #             id = "mes-step-three",
            #             src = "assets/imgs/mes_step_three.png"
            #         ),
            #     ]
            # ),
            html.H6(
                className = "side-font indv-steps",
                children = ["3. Under 'Download Your Information, click 'View'."]
            ),
            # html.Img(
            #     id = "mes-step-four",
            #     src = "assets/imgs/mes_step_four.png"
            # ),
            html.H6(
                className = "side-font indv-steps",
                children = ["4. Deselect all and select 'Messages'."]
            ),
            # html.Img(
            #     id = "mes-step-five",
            #     src = "assets/imgs/mes_step_five.png"
            # ),
            html.H6(
                className = "side-font indv-steps",
                children = ["4. Select the time range you would like to analyze. For 'Format' change to JSON. For 'Media Quality' change to Low."]
            ),
            html.H6(
                className = "side-font indv-steps",
                children = ["5. Download your data. It might take up to a day for FB to approve your download request."]
            ),
            # html.Img(
            #     id = "mes-step-six",
            #     src = "assets/imgs/mes_step_six.png"
            # ),
        ]
    )

def steps_two():
    """
    """
    return html.Div(
        className = "col",
        id = "steps-two-container",
        children = [
            html.H2(
                className = "main-font indv-steps",
                children = ["How To Upload Your Data"]
            ),
            html.H6(
                className = "side-font indv-steps",
                children = ["1. Make sure to unzip the downloaded file first."]
            ),
            html.H6(
                className = "side-font indv-steps",
                children = ["2. Upload the entire folder or else it will not work."]
            ),
            html.B(
                className = "side-font indv-steps",
                children = ["*Input your full name exactly as how it is shown on FB. Ex: 'Christine Nguyen'"]
            ),
            dcc.Upload(html.Button('Upload File')),
            dbc.Input(id = "upload-name-input", placeholder = "Enter your name", type = "text"),
            dbc.Button("Let's Go!", color = "primary", id = "upload-go-button")
        ]
    )