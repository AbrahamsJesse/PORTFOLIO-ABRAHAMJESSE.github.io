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







#image
st.markdown("""
    <style>
        div.image-container {
            display: flex;
            justify-content: center;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="image-container">
        <img src='https://www.riotgames.com/darkroom/original/8555d01d04f01417a3841097d0e06634:1f5570fa1c7996228cfd110872dafb3c/lol-logo-rgb-small-copy.PNG' style="width: 400px;">
    </div>
""", unsafe_allow_html=True)



    
# Title
for title in ["Victory Predictor Project"]:
    st.markdown(f"<div style='font-size: 40px; font-weight: bold; text-align: center; padding: 10px; background-color: rgba(64, 224, 208, 0.6);'>{title}</div>", unsafe_allow_html=True)
st.markdown('<hr style="border:1.5px solid white;">', unsafe_allow_html=True)

#Image
image_url = "https://blogoflegends.com/files/2016/07/League-Of-Legends-Champions-08.jpg"
# Set the image width
image_width = 700
# Center the image using HTML/CSS
centered_image_html = f'<div style="display: flex; justify-content: center;"><img src="{image_url}" width="{image_width}"></div>'
# Display the centered image
st.markdown(centered_image_html, unsafe_allow_html=True)



# Survey for the sidebar
st.sidebar.header("Survey")

# Survey questions 
user_experience = st.sidebar.radio("How would you rate your experience with the predictor?", ["Excellent", "Good", "Average", "Poor"])
feedback = st.sidebar.text_area("Any additional feedback?", "")

# Survey results
st.sidebar.header("Survey Results")
st.sidebar.write(f"User Experience: {user_experience}")
st.sidebar.write(f"Feedback: {feedback}")



#Text
for title in ["The Project"]:
    st.markdown(f"<div style='font-size: 32px; font-weight: bold; text-align: center; padding: 10px; background-color: rgba(64, 224, 208, 0.5); width: 50%; margin: 0 auto;'>{title}</div>", unsafe_allow_html=True)

st.markdown('<hr style="border:1.5px solid white;">', unsafe_allow_html=True)

paragraphs = [
    "The aim of this project is to create a victory predictor for the PC game League of Legends. I will achieve this by using a dataset containing data in-game parameters for 10,000 games in the Diamond division after 10 minutes of game. ",
    "After requesting the user's input on some key in-game parameters, I will predict the victory with a 70% accuracy using machine learning in Python. Finally, I used streamlit to present the resulting project."
]

for paragraph in paragraphs:
    st.markdown(f"<div style='font-size: 21px; text-align: justify; padding: 10px; background-color: rgba(255, 255, 255, 0.5);'>{paragraph}</div>", unsafe_allow_html=True)

    
    


    
    
    







#EXPLAIN THE GAME
#Title
for title in ["The Game"]:
    st.markdown(f"<div style='font-size: 32px; font-weight: bold; text-align: center; padding: 10px; background-color: rgba(64, 224, 208, 0.5); width: 50%; margin: 0 auto;'>{title}</div>", unsafe_allow_html=True)
st.markdown('<hr style="border:1.5px solid white;">', unsafe_allow_html=True)


#Text
paragraphs = [

    "To better understand the context and the parameters requested from the user and used in the model, let's see how the game actually works.",
    "League of Legends is a multiplayer online battle arena where 2 teams (blue and red) face off. There are 3 lanes and the goal is to take down the enemy Nexus to win the game.",
    "The final goal is to destroy the enemy nexus located in the enemy base. To get there, you need to move through the map, achieving some goals that level up your character and team:",
    "- Warding the map - to gain visibility",
    "- Killing minions -  to earn gold",
    "- First blood - to earn gold and experience",
    "- Number of kills and deaths - to earn gold",
    "- Destroying the enemy tower - to advance in the map",
    "- Defeating legendary creatures: the Herald, Dragons, and Baron Nashor."
]

for paragraph in paragraphs:
    st.markdown(f"<div style='font-size: 21px; text-align: justify; padding: 10px; background-color: rgba(255, 255, 255, 0.5);'>{paragraph}</div>", unsafe_allow_html=True)
   
    #Image
st.image("https://miro.medium.com/v2/resize:fit:1400/format:webp/1*mxgYMb2jPI3fFwX25q_W7Q.jpeg")

#Video  
video_url = 'https://www.leagueoflegends.com/static/hero-c35bd03ceaa5f919e98b20c905044a3d.webm'
st.video(video_url)







#EXPLAIN THE LEAGUE
#Title
for title in ["The League"]:
    st.markdown(f"<div style='font-size: 32px; font-weight: bold; text-align: center; padding: 10px; background-color: rgba(64, 224, 208, 0.5); width: 50%; margin: 0 auto;'>{title}</div>", unsafe_allow_html=True)
st.markdown('<hr style="border:1.5px solid white;">', unsafe_allow_html=True)

    

# Centered and larger image
st.markdown("""
    <style>
        .center {
            display: flex;
            justify-content: center;
            align-items: center;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="center">
        <img src='https://www.ncta.com/sites/default/files/styles/article_detail/public/2019-11/774-header-esports.gif?h=39a0b4c9&itok=Dd_D1lf1' style="width: 1000px;">
    </div>
""", unsafe_allow_html=True)






    
#Text
paragraphs = [
    "League of Legends has a game mode called 'ranked,' where the league is divided into different levels, with Iron being the lowest category and Challenger being the highest. In this case scenario, I will focus on the Diamond division.",
    
]
for paragraph in paragraphs:
    st.markdown(f"<div style='font-size: 21px; text-align: justify; padding: 10px; background-color: rgba(255, 255, 255, 0.5);'>{paragraph}</div>", unsafe_allow_html=True)

#Image
st.markdown("""
    <div style="display: flex; justify-content: center; align-items: center;">
        <img src='https://www.noypigeeks.com/wp-content/uploads/2020/11/League-of-Legends-Wild-Rift-Ranks.jpg' alt='Centered Image' />
    </div>
""", unsafe_allow_html=True)


    
    


#Explain dataset

#Text
for title in ["The Dataset"]:
    st.markdown(f"<div style='font-size: 32px; font-weight: bold; text-align: center; padding: 10px; background-color: rgba(64, 224, 208, 0.5); width: 50%; margin: 0 auto;'>{title}</div>", unsafe_allow_html=True)
st.markdown('<hr style="border:1.5px solid white;">', unsafe_allow_html=True)


#Text
paragraphs = [
    "As previously mentioned, the dataset contains data related to games from the Diamond division. Taking a look at the dataset and using some simple visualizations on Power BI, we can see that most of the data is balanced. The reason for this is that players are professionals. Below some examples of balanced data. ",  
]
for paragraph in paragraphs:
    st.markdown(f"<div style='font-size: 21px; text-align: justify; padding: 10px; background-color: rgba(255, 255, 255, 0.5);'>{paragraph}</div>", unsafe_allow_html=True)
    
    
#Image
local_image_path = "Screenshot 2023-12-09 at 22.51.29.png"  
st.image(local_image_path, caption='', use_column_width=True)


#Text
paragraphs = [
    "After studying the dataset more in depth we found some data which percentage of balance is not that high. Therefore, this is the data that has been used to predict the victory since are determining parameters.",   
]
for paragraph in paragraphs:
    st.markdown(f"<div style='font-size: 21px; text-align: justify; padding: 10px; background-color:rgba(255, 255, 255, 0.5);'>{paragraph}</div>", unsafe_allow_html=True)
  

    #Image
local_image_path = "Screenshot 2023-12-09 at 22.59.23.png"  # Replace with the actual path
st.image(local_image_path, caption='', use_column_width=True)





# Centered and narrower background
st.markdown("<h3 style='text-align: center; color: #000000; background-color: rgba(255, 255, 255, 0.5); font-size: 16px; width: 20%; margin: auto;'>Data Visualization by Power BI</h3>", unsafe_allow_html=True)




#Signature
st.markdown('<hr style="border:2px solid white;">', unsafe_allow_html=True)


st.markdown("<h1 style='text-align: right; font-size: 14px; padding: 10px; background-color:  rgba(64, 224, 208, 0.6);'>Created by Abraham Jesse</h1>", unsafe_allow_html=True)
