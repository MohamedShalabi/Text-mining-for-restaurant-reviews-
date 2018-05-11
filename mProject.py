import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
#importing Data 
textset = pd.read_csv('Restaurant_Reviews.tsv', delimiter = '\t', quoting = 3)
#cleaniing Dataset 
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = []
for i in range(0,1000):
    review = re.sub('[^a-zA-Z]',' ',textset['Review'][i])
    review=review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)   
    corpus.append(review)   
#Creating the Bag of Words
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1000)
X= cv.fit_transform(corpus).toarray()
y = textset.iloc[:,1].values
# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

# Fitting Naive Bayes to the Training set
from sklearn.ensemble import RandomForestClassifier
classifier =RandomForestClassifier(n_estimators =10 , criterion = 'entropy' , random_state = 0 )
classifier.fit(X_train , y_train)


# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)    
          
