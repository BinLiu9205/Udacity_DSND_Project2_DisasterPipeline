import sys
import pandas as pd
from sqlalchemy import create_engine
import re
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import classification_report
import pickle
from sklearn.neighbors import KNeighborsClassifier
from sklearn.multioutput import MultiOutputClassifier
import nltk
nltk.download('stopwords')

def load_data(database_filepath):
    engine = create_engine('sqlite:///' + database_filepath)
    df = pd.read_sql_table('DisasterResponseUdacity', engine)
    X = df['message']
    Y = df.iloc[:,4:]
    category_name = list(df.columns[4:])
    return X,Y,category_name

def tokenize(text):
    text = re.sub(r"[^a-zA-Z0-9]", ' ', text.lower()) # Normalize
    words = word_tokenize(text)
    words = [w for w in words if w not in stopwords.words('english')]
    lemm = WordNetLemmatizer()
    lemm_res = [lemm.lemmatize(w, pos='n').strip() for w in words]
    lemm_res = [lemm.lemmatize(w, pos='v').strip() for w in lemm_res]
    
    return lemm_res


def build_model(X_train,y_train):
    pipeline = Pipeline([
        ('vect', CountVectorizer(tokenizer=tokenize)),
        ('tfidf', TfidfTransformer()),
        ('clf', MultiOutputClassifier(RandomForestClassifier()))
    ])
    
    parameters = {  
        'clf__estimator__min_samples_split': [2, 4],
        'clf__estimator__criterion': ['gini', 'entropy'],
        'clf__estimator__n_estimators': [50, 100]
    }
    cv = GridSearchCV(estimator=pipeline, param_grid=parameters)
    cv.fit(X_train,y_train)
    return cv    


def evaluate_model(model, X_test, Y_test, category_names):
    y_pred = pipeline.predict(X_test)
    print(classification_report(Y_test, y_pred, target_names=Y_test.keys()))



def save_model(model, model_filepath):
    temp_pickle = open(model_filepath, 'wb')
    pickle.dump(model, temp_pickle)
    temp_pickle.close()    


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model(X_train,Y_train)
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()