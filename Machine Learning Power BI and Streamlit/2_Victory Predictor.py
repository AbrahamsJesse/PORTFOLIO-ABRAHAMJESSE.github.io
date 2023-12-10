import streamlit as st
st.set_page_config(page_title= 'LoL - Predictor', page_icon=':video_game:',layout='wide')


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





# Title with bright light turquoise background
for title in ["Victory Predictor"]:
    st.markdown(f"<div style='font-size: 40px; font-weight: bold; text-align: center; padding: 10px; background-color:  rgba(64, 224, 208, 0.6);'>{title}</div>", unsafe_allow_html=True)

    
    
    


# Image 
image_url = "https://loltracker.com/images/easyblog_articles/5765/keyart.jpg"
image_width = 950
image_height = 450
centered_image_html = f'<div style="display: flex; justify-content: center;"><img src="{image_url}" width="{image_width}" height="{image_height}"></div>'
st.markdown(centered_image_html, unsafe_allow_html=True)




#Text
for title in ["How does it Work?"]:
    st.markdown(f"<div style='font-size: 32px; font-weight: bold; text-align: center; padding: 10px; background-color: rgba(64, 224, 208, 0.5); width: 50%; margin: 0 auto;'>{title}</div>", unsafe_allow_html=True)
st.markdown('<hr style="border:1.5px solid white;">', unsafe_allow_html=True)



# Text
paragraphs = [
    "Lets calibrate your victory prediction! After the initial 10 minutes of gameplay, share a set of key parameters with us. We will leverage this information to provide you with a personalized prediction for the outcome of your game!",
]
for paragraph in paragraphs:
    st.markdown(f"<div style='font-size: 21px; text-align: justify; padding: 10px; background-color: rgba(0, 0, 0, 0.6); color: white;'>{paragraph}</div>", unsafe_allow_html=True)

  
    #Text
paragraphs = [
    "Below you can see the crucial in-game elements that significantly impact victory predictions. While other in-game elements also play a role, focus on these key parameters to reach the victory.",   
]
for paragraph in paragraphs:
    st.markdown(f"<div style='font-size: 21px; text-align: justify; padding: 10px; background-color: rgba(0, 0, 0, 0.6);'>{paragraph}</div>", unsafe_allow_html=True)
  

    st.markdown("""
    <div style="display: flex; justify-content: center; align-items: center;">
        <img src='https://i.pinimg.com/originals/f8/67/72/f867728bf6bea9c762a37ab8d46de931.gif' alt='Centered Image' />
    </div>
""", unsafe_allow_html=True)
   
    
#Title
for title in ["Disclaimer!"]:
    st.markdown(f"<div style='font-size: 40px; font-weight: bold; text-align: center; padding: 10px; background-color: rgba(64, 224, 208, 0.6);'>{title}</div>", unsafe_allow_html=True)
st.markdown('<hr style="border:1.5px solid white;">', unsafe_allow_html=True)




#Text
paragraphs = [
    "Take into account that this predictor is an approximation. We have not developed (yet) a 100% accurate prediction model. Also, consider that external factors, such as your Wi-Fi connection, external distractions (e.g., your parents complaining), or the performance of your computer, that can contribute to the defeat or victory of your team.",   
]
for paragraph in paragraphs:
    st.markdown(f"<div style='font-size: 21px; text-align: justify; padding: 10px; background-color: rgba(0, 0, 0, 0.5);'>{paragraph}</div>", unsafe_allow_html=True)
  




    #Text
for title in ["General Information"]:
    st.markdown(f"<div style='font-size: 32px; font-weight: bold; text-align: center; padding: 10px; background-color: rgba(64, 224, 208, 0.5); width: 50%; margin: 0 auto;'>{title}</div>", unsafe_allow_html=True)
st.markdown('<hr style="border:1.5px solid white;">', unsafe_allow_html=True)



    

    
    

# Create columns
col1, col2 = st.columns(2)
# Text input with white font color
col1.text_input("Nickname", key="nickname", value="", type="default")
# Multiselect with default font color
region_selection = col2.multiselect(
    'Region',
    ['LEC: Europe, the Middle East and Africa', 'LCS: North America', 'PCS: TW, HK, MC, SEA and Oceania'],
    key="region_selection",
    default=None
)

# Apply white font color to the text input
st.markdown(
    """
    <style>
        .stTextInput {
            color: white !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)





    
#Text
for title in ["Required Parameters"]:
    st.markdown(f"<div style='font-size: 32px; font-weight: bold; text-align: center; padding: 10px; background-color: rgba(64, 224, 208, 0.5); width: 50%; margin: 0 auto;'>{title}</div>", unsafe_allow_html=True)
st.markdown('<hr style="border:1.5px solid white;">', unsafe_allow_html=True)


    # Input boxes
game_type = st.multiselect('Type of Game', ['Summoners Rift Blind Pick', 'Summoners Rift  Draft Pick', 'Ranked solo or duo', 'Ranked Flex', 'ARAM'])
col1, col2 = st.columns(2)


#Parameter
first_blood_result = None
blue_deaths = None
red_deaths = None
herald_result = None
dragon_result = None




# 'blueFistitBlood', 'redFirstblood'
first_blood = st.text_input("Did your team get the first blood?", key="first_blood")
if first_blood:
    if first_blood.lower() == 'yes':
        first_blood_result = int(1)  # Directly use a float without converting
    elif first_blood.lower() == 'no':
        first_blood_result = int(0)  # Directly use a float without converting
    else:
        st.error("Please enter 'yes' or 'no'.")

        
        
        # 'blueDeaths', 'redDeaths'
blue_deaths1 = col1.text_input("How many deaths does your team have?") #(number)
if blue_deaths1:
    blue_deaths= blue_deaths1
    
red_deaths1 = col1.text_input("How many deaths does the enemy have?") #(number) 
if red_deaths1:
    red_deaths= red_deaths1
    

    
    
        #'blueHeralds', 'redHeralds'
herald = col1.text_input("Did your team kill the Herald?") #1-0
if first_blood:
    if herald.lower() == 'yes':
        herald_result = 1.0  # Directly use a float without converting
    elif herald.lower() == 'no':
        herald_result = 0.0  # Directly use a float without converting
    else:
        st.error("Please enter 'yes' or 'no'.")

        
        
        #'blueDragons', 'redDragons'
dragon = col1.text_input("Did your team kill the Dragon?") #1-0
if dragon:
    if dragon.lower() == 'yes':
        dragon_result = 1.0  # Directly use a float without converting
    elif dragon.lower() == 'no':
        dragon_result = 0.0  # Directly use a float without converting
    else:
        st.error("Please enter 'yes' or 'no'.")

        
prediction_features = [first_blood_result, blue_deaths, red_deaths, herald_result, dragon_result]


#MODEL
gradient_background = """
    linear-gradient(45deg, #ff80bf, #66a3ff);
    background-clip: text;
    -webkit-background-clip: text;
    color: transparent;
    font-weight: bold;
    font-size: 28px;  /* Adjust the font size as needed */
    text-decoration: underline;
"""

if st.button('Predict my chances of winning!'):
    try:
        import pickle
        import numpy as np

        with open('Model.pkl', 'rb') as model_file:
            loaded_model = pickle.load(model_file)


            input_data_as_numpy_array = np.asarray(prediction_features)
            input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
            prediction = loaded_model.predict(input_data_reshaped)
            result= prediction[0] # return the prediction value only

            
            
            if result == 1:
                result = 'Congratulations, you have a 70% chance of winning!'
            if result == 0:
                result ='Oh-oh... It doesnt look like you are gonna win this one...'
            #final_result= st.success(result)
            final_result = st.markdown(f'<p style="background: {gradient_background}">{result}</p>', unsafe_allow_html=True)

            
        
    except:
        result ="Could not make prediction"




#Signature
st.markdown("<h1 style='text-align: right; font-size: 14px; padding: 10px; background-color:  rgba(64, 224, 208, 0.6);'>Created by Abraham Jesse</h1>", unsafe_allow_html=True)

