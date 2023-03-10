import pandas as pd
from xgboost import XGBClassifier
import pickle
from sklearn.model_selection import StratifiedKFold
# Load the csv file
df = pd.read_excel("Final.xlsx")

X_OS = df[['Ge', 'Al', 'OH', 'H2O', 'F', 'OSDA', "B", "Na2O", "Cl", "Temperature", "time", "AR", "Area", "CN", "rpm"]]
Y_OS= df['RC2']
cv = StratifiedKFold(n_splits=10, random_state=1, shuffle=True)
for train_index, test_index in cv.split(X_OS, Y_OS):
    X_Train, X_Test= X_OS.iloc[train_index], X_OS.iloc[test_index]
    Y_Train, Y_Test= Y_OS[train_index], Y_OS[test_index]

XGB = XGBClassifier(random_state=1,  n_estimators=1970, learning_rate=0.291,  alpha=0.0001)
xg_model=XGB.fit(X_Train.values, Y_Train)

pickle.dump(xg_model, open("model.pkl", "wb"))