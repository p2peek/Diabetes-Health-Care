# import streamlit as st
# from web_functions import load_data

# from Tabs import diagnosis, home, result,  kc, talk2doc

# # Configure the app
# st.set_page_config(
#     page_title = 'Diabetes Prediction System',
#     page_icon = '🥯',
#     layout = 'wide',
#     initial_sidebar_state = 'auto'
# )

# Tabs = {
#     "Home":home,
#     "Ask Queries":talk2doc,
#     "Diagnosis":diagnosis,
#     "Result":result,
#     "Knowledge Center":kc
# }

# st.sidebar.title('Navigation')

# page = st.sidebar.radio("Page", list(Tabs.keys()))
# st.sidebar.info('Made with 💙 by Gagan')

# df, X, y = load_data()

# if page in ["Diagnosis"]:
#     Tabs[page].app(df, X, y)
# else:



#     Tabs[page].app()




import streamlit as st
from web_functions import load_data
from Tabs import diagnosis, home, result, kc, talk2doc

------------------- Page Configuration -------------------
st.set_page_config(
    page_title='Diabetes Prediction System',
    page_icon='🥯',
    layout='wide',
    initial_sidebar_state='auto'
)

------------------- Hide Default Streamlit UI Elements -------------------
hide_streamlit_style = """
    <style>
    /* Hide the default Streamlit menu, footer, header, and deploy buttons */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}
    [data-testid="stActionButtonIcon"] {display: none;}
    [data-testid="stToolbar"] {display: none !important;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

------------------- Define Tabs -------------------
Tabs = {
    "Home": home,
    "Ask Queries": talk2doc,
    "Diagnosis": diagnosis,
    "Result": result,
    "Knowledge Center": kc
}

------------------- Sidebar Navigation -------------------
st.sidebar.title('Navigation')
page = st.sidebar.radio("Page", list(Tabs.keys()))
st.sidebar.info('Made with 💙 by Gagan')

------------------- Load Data -------------------
df, X, y = load_data()

------------------- Page Rendering -------------------
if page == "Diagnosis":
    Tabs[page].app(df, X, y)
else:
    Tabs[page].app()
