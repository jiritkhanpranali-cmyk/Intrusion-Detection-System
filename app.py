import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt

from sqlalchemy import create_engine
from database import save_result

# Load models

nsl_model = pickle.load(
    open(
        "intrusion_model.pkl",
        "rb"
    )
)
# Load CICIDS model

cicids_model = pickle.load(
    open(
        "models/cicids_model.pkl",
        "rb"
    )
)


st.title(
    "🛡️ Multi Dataset AI Intrusion Detection System"
)


st.write(
    "Supports NSL-KDD and CICIDS2017 Network Traffic"
)



# NSL-KDD columns

nsl_columns = [

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




file = st.file_uploader(

    "Upload Network Dataset",

    type=["txt","csv"]

)




if file:



    # =========================
    # NSL-KDD Detection
    # =========================


    if file.name.endswith(".txt"):

        dataset = "NSL-KDD"
        st.info(
            "NSL-KDD Dataset Detected"
        )


        data = pd.read_csv(

            file,

            names=nsl_columns
           
        )


        X = data.drop(

            "label",

            axis=1

        )


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



        X = X.fillna(0)



        prediction = nsl_model.predict(X)



        data["Prediction"] = prediction




        data["Result"] = data["Prediction"].apply(

            lambda x:

            "Normal"

            if x=="normal"

            else

            "Attack"

        )





    # =========================
    # CICIDS Detection
    # =========================


    else:

        dataset = "CICIDS2017"

        st.info(

            "CICIDS2017 Dataset Detected"

        )



        data = pd.read_csv(file)



        data.columns = data.columns.str.strip()



        X = data.drop(

            "Label",

            axis=1

        )



        X = X.replace(

            [float("inf"),-float("inf")],

            0

        )


        X = X.fillna(0)



        for col in X.columns:


            if X[col].dtype=="object":


                X[col] = pd.factorize(

                    X[col]

                )[0]



        prediction = cicids_model.predict(X)



        data["Prediction"] = prediction




        data["Result"] = data["Prediction"].apply(

            lambda x:

            "Normal"

            if x==0

            else

            "Attack"

        )






    # =========================
    # Dashboard
    # =========================


    normal = len(

        data[data["Result"]=="Normal"]

    )


    attack = len(

        data[data["Result"]=="Attack"]

    )
    save_result(

       dataset,

       normal,

       attack

    )



    col1,col2 = st.columns(2)



    with col1:

        st.success(

            f"Normal Traffic : {normal}"

        )



    with col2:

        st.error(

            f"Attack Traffic : {attack}"

        )




    st.subheader(
        "Traffic Analysis"
    )



    chart = pd.DataFrame(

        {

        "Type":

        [

        "Normal",

        "Attack"

        ],


        "Count":

        [

        normal,

        attack

        ]

        }

    )



    fig,ax = plt.subplots()



    ax.bar(

        chart["Type"],

        chart["Count"]

    )



    st.pyplot(fig)



    st.subheader(

        "Prediction Sample"

    )


    st.dataframe(

        data[

            [

            "Prediction",

            "Result"

            ]

        ].head(50)

    )
    from sqlalchemy import create_engine


st.subheader(
    "📊 Detection History"
)


engine = create_engine(
    "sqlite:///intrusion.db"
)


history = pd.read_sql(
    "SELECT * FROM detections",
    engine
)


st.dataframe(
    history
)