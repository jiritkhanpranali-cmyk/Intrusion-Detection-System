import pandas as pd


files = [

"Benign-Monday-no-metadata.parquet",

"DoS-Wednesday-no-metadata.parquet",

"DDoS-Friday-no-metadata.parquet",

"Portscan-Friday-no-metadata.parquet"

]


dataframes=[]


for file in files:

    print("Loading",file)

    df=pd.read_parquet(file)

    dataframes.append(df)



final=pd.concat(
    dataframes,
    ignore_index=True
)



print(final.head())

print(final.shape)



final.to_csv(
"CICIDS2017.csv",
index=False
)



print("CSV created successfully")