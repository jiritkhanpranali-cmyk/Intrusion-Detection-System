import pandas as pd
import pickle
import os

from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split


print("Loading CICIDS dataset...")


data = pd.read_csv(
    "CICIDS2017.csv"
)


print("Dataset loaded")
print(data.shape)



# Remove spaces from column names

data.columns = data.columns.str.strip()



# Remove empty columns

data = data.dropna(
    axis=1
)



print("Columns:")
print(data.columns)



# Separate features and label

X = data.drop(
    "Label",
    axis=1
)


y = data["Label"]



# Convert text columns to numbers

for col in X.columns:

    if X[col].dtype == "object":

        encoder = LabelEncoder()

        X[col] = encoder.fit_transform(
            X[col].astype(str)
        )



# Encode labels

label_encoder = LabelEncoder()

y = label_encoder.fit_transform(
    y
)



# Replace infinity values

X = X.replace(
    [float("inf"), -float("inf")],
    0
)



# Fill missing values

X = X.fillna(0)



print("Training data:")
print(X.shape)



X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,

    test_size=0.2,

    random_state=42

)



print("Training model...")


model = RandomForestClassifier(

    n_estimators=100,

    n_jobs=-1,

    random_state=42

)



model.fit(

    X_train,

    y_train

)



accuracy = model.score(

    X_test,

    y_test

)


print(
    "Accuracy:",
    accuracy
)



# Create models folder

os.makedirs(
    "models",
    exist_ok=True
)



pickle.dump(

    model,

    open(
        "models/cicids_model.pkl",
        "wb"
    )

)



print("CICIDS model saved successfully")