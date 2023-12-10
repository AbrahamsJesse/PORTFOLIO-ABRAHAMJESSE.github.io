import streamlit as st


# Set the background image
background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://steamuserimages-a.akamaihd.net/ugc/957483070093055113/DABA77BF74CE845A1F1DA8A3A1ABA5FA54479C9A/?imw=5000&imh=5000&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false");
    background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;
    background-repeat: no-repeat;
}
</style>
"""
st.markdown(background_image, unsafe_allow_html=True)



for title in ["League of Legends Video Samples"]:
    st.markdown(f"<div style='font-size: 40px; font-weight: bold; text-align: center; padding: 10px; background-color:  rgba(64, 224, 208, 0.6);'>{title}</div>", unsafe_allow_html=True)

    
    
#Videos
col1, col2 = st.columns(2)
# Video 1
with col1:
    st.video('https://youtu.be/O4PDzBnBMU4?si=_U3CtCer8g0CRnV9')

# Video 2
with col2:
    st.video('https://www.youtube.com/watch?v=lGL4UgWjNN0')






st.markdown("<h1 style='text-align: right; font-size: 14px; padding: 10px; background-color:  rgba(64, 224, 208, 0.6);'>Created by Abraham Jesse</h1>", unsafe_allow_html=True)
