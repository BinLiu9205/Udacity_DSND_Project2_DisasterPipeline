# Disaster Response Pipeline Project

### Project Background:

This is the second project from Udacity - Data Scientist Nanodegree. The application analyze disaster data from Figure Eight to build a model for an API that classifies disaster messages.

In the data folder, you'll find a data set containing real messages that were sent during disaster events. A machine learning pipeline was built to categorize these events so that you can send the messages to an appropriate disaster relief agency.

The final project include a web app where an emergency worker can input a new message and get classification results in several categories. The web app will also display visualizations of the data. Using the visualization dashboard, it can help the emergency understand the most frequently encountered classification results. 

The code was adapted from Udacity Nanodegree Project. The code is welcomed to be shared/reused etc. under MIT license. 

### Project Component:

There are three main components in the folder:

1. ETL Pipeline
In a Python script, process_data.py, write a data cleaning pipeline that:

Loads the messages and categories datasets
Merges the two datasets
Cleans the data
Stores it in a SQLite database

-- A database was already added into the folder. It's directly usable in the employed pipeline. 

2. ML Pipeline
In a Python script, train_classifier.py, write a machine learning pipeline that:

Loads data from the SQLite database
Splits the dataset into training and test sets
Builds a text processing and machine learning pipeline
Trains and tunes a model using GridSearchCV
Outputs results on the test set
Exports the final model as a pickle file

-- The trained ML model is available under ./models folder, with the name classifier.pkl. The current model is trained and grid searched by the randomForest model. You can also train your own model by adapting the train_classifier.py, e.g. you can try LinearSVC as estimator inside MultiOutputClassifier (thanks to you the reviewer for the suggestion). 

3. Flask Web App
We are providing much of the flask web app for you, but feel free to add extra features depending on your knowledge of flask, html, css and javascript. For this part, you'll need to:

Modify file paths for database and model as needed
Add data visualizations using Plotly in the web app. 

-- Data visualizations are important components in the Flask Web App. We currently have the 5 top frequently encounted categories available in the webApp. All visualizations are performed by plotly.


### Instructions to deployment:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/
