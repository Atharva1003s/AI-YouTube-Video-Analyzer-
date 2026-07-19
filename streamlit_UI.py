import streamlit as st
from Youtube_Analyzer import build_agent


import pandas as pd
import numpy as np

# st.write("Here's our first attempt at using data to create a table:")
# st.write(pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# }))

# chart_data = pd.DataFrame(
#      np.random.randn(20, 3),
#      columns=['a', 'b', 'c'])

# st.line_chart(chart_data)


# x = st.slider('x')  # 👈 this is a widget
# st.write(x, 'squared is', x * x)






st.set_page_config(
    page_title="YouTube Video Analyzer", 
    layout="centered",
    initial_sidebar_state="expanded" 
)


st.title("AI YouTube Video Analyzer 🎥")


# caching the agent to avoid rebuilding it on every interaction
@st.cache_resource
def get_agent():
    return build_agent()




yt_agent = get_agent()



# Now defining the input
video_link = st.text_input("Enter YouTube Video Link:", "") # Input goes in String format


# Submit button to trigger the analysiss
submit_button = st.button("Analyze Video") # Button takes True or False value



if video_link and submit_button:
    with st.spinner("Analyzing the video..."):
        response = yt_agent.run(
            f"Analyze this video {video_link}"
        )

    st.markdown("### Analysis Result:")
    st.markdown(response.content)
       
