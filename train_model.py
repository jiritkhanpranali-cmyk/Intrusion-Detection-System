import pandas as pd
import pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline


print("Loading dataset...")


columns = [
"duration",
"protocol_type",
"service",
"flag",
"src_bytes",
"dst_bytes",
"land",
"wrong_fragment",
"urgent",
"hot",
"num_failed_logins",
"logged_in",
"num_compromised",
"root_shell",
"su_attempted",
"num_root",
"num_file_creations",
"num_shells",
"num_access_files",
"num_outbound_cmds",
"is_host_login",
"is_guest_login",
"count",
"srv_count",
"serror_rate",
"srv_serror_rate",
"rerror_rate",
"srv_rerror_rate",
"same_srv_rate",
"diff_srv_rate",
"srv_diff_host_rate",
"dst_host_count",
"dst_host_srv_count",
"dst_host_same_srv_rate",
"dst_host_diff_srv_rate",
"dst_host_same_src_port_rate",
"dst_host_srv_diff_host_rate",
"dst_host_serror_rate",
"dst_host_srv_serror_rate",
"dst_host_rerror_rate",
"dst_host_srv_rerror_rate",
"label"
]


data = pd.read_csv(
    "KDDTrain+.txt",
    names=columns
)


# Remove label

X = data.drop(
    "label",
    axis=1
)


y = data["label"]



# Convert all feature columns except text

for col in X.columns:

    if col not in [
        "protocol_type",
        "service",
        "flag"
    ]:

        X[col] = pd.to_numeric(
            X[col],
            errors="coerce"
        )



# Fill missing values

X = X.fillna(0)



print("Features:", X.shape)



categorical_features = [
    "protocol_type",
    "service",
    "flag"
]


preprocessor = ColumnTransformer(

    transformers=[

        (
            "cat",
            OneHotEncoder(
                handle_unknown="ignore"
            ),
            categorical_features
        )

    ],

    remainder="passthrough"

)



pipeline = Pipeline(

    [

        (
        "preprocessor",
        preprocessor
        ),

        (
        "model",
        RandomForestClassifier(
            n_estimators=50,
            n_jobs=-1
        )
        )

    ]

)



print("Training model...")


pipeline.fit(
    X,
    y
)



pickle.dump(

    pipeline,

    open(
        "intrusion_model.pkl",
        "wb"
    )

)



print("Model saved successfully")