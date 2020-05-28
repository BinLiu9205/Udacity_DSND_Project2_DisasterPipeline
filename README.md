# Disaster Response Pipeline Project

### Project Background:

This is the second project from Udacity - Data Scientist Nanodegree. The application analyze disaster data from Figure Eight to build a model for an API that classifies disaster messages.

In the data folder, you'll find a data set containing real messages that were sent during disaster events. A machine learning pipeline was built to categorize these events so that you can send the messages to an appropriate disaster relief agency.

The final project include a web app where an emergency worker can input a new message and get classification results in several categories. The web app will also display visualizations of the data. Using the visualization dashboard, it can help the emergency understand the most frequently encountered classification results. 

The code was adapted from Udacity Nanodegree Project. The code is welcomed to be shared/reused etc. under MIT license. 


### Instructions to deployment:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/
