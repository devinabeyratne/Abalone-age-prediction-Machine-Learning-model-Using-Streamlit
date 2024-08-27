README

Abalone Age Prediction Application

This Streamlit application allows users to predict the age of abalone based on various physical measurements. The prediction model is trained on the abalone dataset and deployed using fast API and Streamlit for an interactive user experience.

Files Included:

01. main.py: This file contains the FastAPI application code. It includes the logic for loading the trained model, defining API endpoints, processing input data, and returning the predicted abalone age.

02. app.py: This file contains the Streamlit application code. It includes the logic for loading the model, taking user input, and displaying the predicted age.

03. best_model.joblib : The trained machine learning model serialized using job lib. It is loaded when the Streamlit app starts using the fast API.

04. requirements.txt: This file lists all the dependencies required to run the Streamlit application. You can install them using `pip install -r requirements.txt`.

 05. Test.csv / Train.csv: These files contain the dataset used to train and test the abalone age prediction model.

    • Train.csv: This file includes the training data, with features and corresponding age labels. It is used to train the machine learning model.

    • Test.csv: This file includes the testing data, which is used to evaluate the performance of the trained model. It contains similar features as the training data but is used solely for validation purposes.


Instructions for Usage:


 01. Setting up the Environment:

IMPORTANT - Ensure you have Python installed on your system. Ensure that all these terminal codes are running under the IDE you are using and make sure you have loaded all the files in the folder including the trained model to the IDE.

* Install the required dependencies by running: 
    ```bash
    pip install -r requirements.txt
    ```


02. Running the FastAPI App:
    • *Execute the following command in your terminal:
    •  ```bash
    • uvicorn main:app --reload
    •     ``` 
    • This will start the FastAPI development server, and you can access the API documentation at http://127.0.0.1:8000/docs and the application endpoints at http://127.0.0.1:8000/.
    • 
You can use the fast api front end to predict the above age too. But for the application I have built a frontend using streamlit.


 03. Running the Streamlit App:

* Execute the following command in your terminal: 
    ```bash
    streamlit run app.py
    ```

* This will start the Streamlit server, and you will be automatically redirect to the relevant server most of the tiem it is http://localhost:8501/ when running the terminal command above, so you can use the application to predict abalone age.



04. Using the Application:
Upon accessing the dashboard, you will see three pages:
    
Home: This page introduces the application and provides an overview of its purpose and functionality.
        
About Abalone and the Dataset: Here, you can learn more about abalones, their significance, and the dataset used for training the model.
        
Age Prediction: This page allows you to input the physical measurements of the abalone (e.g., length, diameter, height, etc.). Once you fill in the required fields and submit the form, the application processes the input data, makes a prediction using the trained model, and displays the predicted age of the abalone.



This README provides a clear guide on setting up and using your abalone age prediction application with Fast API & Streamlit.
