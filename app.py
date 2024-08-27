import streamlit as st
import requests
import json

# Define a function for the Abalone Rings Prediction page
def abalone_rings_prediction():
    st.title("Abalone Rings Prediction")

    # Define input fields for user
    sex = st.selectbox("Sex", options=["male", "female", "infant"])
    length = st.number_input("Length (mm)", format="%.4f")
    diameter = st.number_input("Diameter (mm)", format="%.4f")
    height = st.number_input("Height (mm)", format="%.4f")
    whole_weight = st.number_input("Whole Weight (grams)", format="%.4f")
    whole_weight1 = st.number_input("Whole Weight1 (grams)", format="%.4f")
    whole_weight2 = st.number_input("Whole Weight2 (grams)", format="%.4f")
    shell_weight = st.number_input("Shell Weight (grams)", format="%.4f")

    # Define a function to call the FastAPI endpoint
    def predict_rings():
        url = "http://127.0.0.1:8000/predict/"
        data = {
            "Sex": sex,
            "Length": length,
            "Diameter": diameter,
            "Height": height,
            "WholeWeight": whole_weight,
            "WholeWeight1": whole_weight1,
            "WholeWeight2": whole_weight2,
            "ShellWeight": shell_weight,
        }
        try:
            response = requests.post(url, json=data)
            response.raise_for_status()
            result = response.json()
            return result["Predicted number of rings"]
        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred: {e}")

    # Button to trigger prediction
    if st.button("Predict"):
        rings = predict_rings()
        if rings is not None:
            st.write(f"Predicted number of rings: {rings}")

# Define functions for other pages
def home():
    st.title("ABALONE AGE PREDICTION SYSTEM")

    # Add an abalone picture
    image_path = "abalone.jpg"  # Update this to your image path if necessary
    st.image(image_path, caption="Abalone: The Enchanting Gem of the Sea", use_column_width=True)

    st.markdown("""Welcome to the Abalone Rings Prediction App! 🐚🔍

Our goal is to accurately predict the age of abalones based on their physical measurements. By providing detailed data about abalones, 
our app uses sophisticated algorithms to estimate the number of rings, which corresponds to their age. 
Let's work together to gain valuable insights into abalone growth and enhance our understanding of these fascinating mollusks!

### How It Works
1.**Provide Measurements:** Go to the Abalone Age Prediction page and enter the physical measurements of the abalone,
 including length, diameter, height, and weights.

2.**Submit Data:** Once you've entered all the required information, click the "Predict" button. 
Our system will process the data using a trained machine learning model.

3.**Receive Prediction:** View the estimated number of rings, which indicates the abalone's age. 
This prediction is based on advanced statistical techniques and historical data.
        """)


def about():
    st.title("About Abalone & Dataset")
    st.write("""
    ### About Abalone
    Abalone is a common name for a group of small to very large sea snails, 
    marine gastropod mollusks in the family Haliotidae. These snails have a large,
     flattened, ear-shaped shell with a row of holes along the outer edge. 
     The inner surface of the shell is iridescent and is highly prized for its beauty and used in jewelry and 
     decorative items.""")

    image_path = "1.jpg"  # Update this to your image path if necessary
    st.image(image_path, caption="Abalone: The Enchanting Gem of the Sea", use_column_width=True)

    st.write("""Abalone is also a popular food source in many cultures, 
    particularly in Asia and North America. The meat is considered a delicacy and is often used in 
    sushi, salads, and other dishes. Because of its popularity as a food and the high demand for its shells,
     many species of abalone have been overfished and are now endangered. """)

    st.write("""
    
    ### About DataSet   
    The Abalone dataset is a popular machine learning dataset that contains measurements of physical characteristics of abalone,
     a type of sea snail. The dataset is often used as a benchmark for regression tasks in machine learning.""")

    st.write("""

The dataset includes the following features or variables for each abalone:

1.**Sex:** categorical variable (M for male, F for female, and I for infant)


2.**Length:** continuous variable representing the longest shell measurement in mm


3.**Diameter:** continuous variable representing the diameter of the shell in mm


4.**Height:** continuous variable representing the height of the shell in mm


5.**Whole weight:** continuous variable representing the weight of the whole abalone (shell+meat) in grams


6.**Shucked weight:**(named as Whole weight.1)  continuous variable representing the weight of the meat in grams


7.**Viscera weight:** (named as Whole weight.2)continuous variable representing the weight of the gut (after bleeding) 
in grams


8.**Shell weight:** continuous variable representing the weight of the shell in grams


9.**Rings:** integer variable representing the age of the abalone (the number of rings on the shell)

In the training dataset, there are 90615 entries of data. The goal of the dataset is to predict the age of the abalone (i.e., the number of rings) based on its physical characteristics.
 This is a regression task, as the target variable (age) is a continuous variable.
    """)



# Create a sidebar with navigation options
st.sidebar.title("Navigation")
option = st.sidebar.selectbox(
    "Choose a page",
    ["Home", "About Abalone & Dataset", "Abalone Age Prediction"]
)

# Render the selected page
if option == "Home":
    home()
elif option == "About Abalone & Dataset":
    about()
elif option == "Abalone Age Prediction":
    abalone_rings_prediction()


# streamlit run app.py