# AI Based Multi-Dataset Network Intrusion Detection System


## Abstract

Network security has become a critical challenge due to the increasing number of cyber attacks and unauthorized access attempts. This project presents an AI-based Multi-Dataset Network Intrusion Detection System (IDS) that uses Machine Learning techniques to identify malicious network traffic. The system analyzes network flow data and classifies it as normal traffic or intrusion activity.

The proposed system supports multiple benchmark datasets including NSL-KDD and CICIDS2017. A Random Forest Machine Learning algorithm is used for classification because of its high accuracy and ability to handle complex network patterns. A Streamlit-based interface provides an interactive dashboard where users can upload network traffic datasets and visualize detection results.

The system also integrates an SQLite database to store intrusion analysis history, allowing users to maintain records of previous detection activities.

## Keywords

Intrusion Detection System, Machine Learning, Network Security, Random Forest, NSL-KDD, CICIDS2017, Streamlit, Cyber Security


# 1. Introduction

## 1.1 Problem Statement

With the rapid growth of internet usage, cyber attacks such as Denial of Service (DoS), Probe attacks, Botnet activities, and unauthorized access attempts are increasing. Traditional signature-based intrusion detection systems are limited because they cannot effectively detect unknown attack patterns.

Therefore, an intelligent intrusion detection system is required that can automatically analyze network traffic and identify suspicious activities using Machine Learning.


## 1.2 Objective

The main objectives of this project are:

- To develop an AI-based intrusion detection system.
- To classify network traffic into normal and attack categories.
- To support multiple network security datasets.
- To provide a user-friendly visualization dashboard.
- To store detection results for future analysis.


# 2. Methodology

The proposed system follows a Machine Learning based approach.

## Dataset Collection

The system uses:

1. NSL-KDD Dataset
2. CICIDS2017 Dataset


## Data Preprocessing

The following preprocessing steps are performed:

- Handling missing values
- Converting categorical values into numerical format
- Removing unwanted data
- Feature preparation


## Machine Learning Model

Random Forest Classifier is used because:

- It provides high classification accuracy.
- It handles large feature spaces.
- It reduces overfitting.
- It works efficiently with network traffic data.


## Detection Process

The uploaded dataset is automatically identified:

NSL-KDD:
KDDTest+.txt
|
↓
NSL-KDD Model
|
↓
Normal / Attack



CICIDS2017:


CICIDS2017.csv
|
↓
CICIDS Model
|
↓
Normal / Attack




# 3. Tools and Technologies Used

## Programming Language

Python

## Libraries

- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Streamlit
- SQLAlchemy


## Database

SQLite


## Development Tools

- VS Code
- GitHub
- PowerShell



# 4. Literature Review

Existing intrusion detection systems mainly depend on:

- Signature-based detection
- Rule-based detection
- Traditional statistical methods


Previous research shows that Machine Learning approaches improve intrusion detection performance by learning hidden patterns from network traffic data.

However, many existing systems focus on a single dataset and lack flexible testing environments.


# 5. Comparison


| Feature | Traditional IDS | Proposed IDS |
|---|---|---|
| Detection Method | Rules | Machine Learning |
| Dataset Support | Single Dataset | Multi Dataset |
| Unknown Attack Detection | Limited | Better |
| Visualization | Not Available | Streamlit Dashboard |
| Storage | Limited | SQLite Database |
| User Interface | Complex | Simple Upload System |



# 6. Advantages and Superiority

The proposed system is superior because:

- Supports multiple datasets.
- Automatically detects dataset type.
- Uses Machine Learning classification.
- Provides visual analysis.
- Maintains detection history.
- Easy to use through web interface.


# 7. Implementation

The system is implemented using Python and Streamlit.

## Why Streamlit?

Streamlit is used because:

- It quickly creates interactive web applications.
- No complex frontend development is required.
- It supports data visualization.
- It integrates easily with Machine Learning models.


## System Components

### Frontend

Streamlit interface is used for:

- Dataset upload
- Result display
- Graph visualization


### Backend

Python handles:

- Data preprocessing
- Model prediction
- Database operations


### Machine Learning

Random Forest model performs intrusion classification.


# 8. Results

The system successfully detects network traffic from:

- NSL-KDD Dataset
- CICIDS2017 Dataset


The output includes:

- Normal traffic count
- Attack traffic count
- Prediction results
- Traffic visualization graph



# 9. Conclusion

This project demonstrates an AI-based Multi-Dataset Intrusion Detection System capable of detecting malicious network activities using Machine Learning.

The integration of multiple datasets, visualization dashboard, and database storage makes the system more flexible and practical for security monitoring applications.


# 10. Future Scope

Future improvements include:

- Real-time packet monitoring.
- Deep Learning based detection.
- Cloud deployment.
- Automatic attack type classification.
- Real-time security alerts.


# References / Bibliography

[1] M. Tavallaee et al., "A Detailed Analysis of the KDD CUP 99 Data Set," IEEE Symposium on Computational Intelligence for Security and Defense Applications, 2009.

[2] I. Sharafaldin, A. Lashkari, and A. Ghorbani, "Toward Generating a New Intrusion Detection Dataset and Intrusion Traffic Characterization," ICISSP, 2018.

[3] L. Breiman, "Random Forests," Machine Learning Journal, 2001.

[4] Scikit-learn Documentation, Machine Learning Library.

[5] Streamlit Documentation, Data Application Framework.
