from sklearn import tree

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
def model(src_csv):
    df = pd.read_csv(src_csv, delimiter='|')
    #print(df.describe())
    df_X = df.drop(['row','playlist','indexInPlaylistFile', 'song_id', 'song_name', 'artist_name'], axis=1) 
    df_Y = df['playlist']
    df_Y = df_Y.astype('category')
    df_Y = df_Y.cat.codes
    #print(df_Y)
    
    x_train, x_test, y_train, y_test = train_test_split(df_X, df_Y, test_size=.2)
    print(x_train.describe())
    
    reg = LinearRegression().fit(x_train, y_train)
    y_pred = reg.predict(x_test)
    #print(y_pred)
    print("r2 score: ", r2_score(y_test, y_pred, multioutput='raw_values'))
    
    
'''
train, test = train_test_split(dataframe, test_size=0.2)
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)
'''

model("playlist_data_scaled_final11_30am.csv")