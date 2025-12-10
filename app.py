import streamlit as st
import pandas as pd
import joblib as jl
Model_data = jl.load(r"Model.pkl")

columns = Model_data["Columns"]
LabelEncoder = Model_data["Encoder"]
Scaler = Model_data["Scaler"]
model = Model_data["Model"]

st.markdown("""
    <style>
    h1 > a, h2 > a, h3 > a, h4 > a, h5 > a, h6 > a {
        display: none !important;
    }
    [data-testid="stMarkdownContainer"] h1 a {
        display: none !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🔮 Telco Customer Churn")
st.subheader("Enter Customer Details Below...",anchor=False)
st.write("This App Predicts If Customer Leaves Your Comapany Or Not.")

gender = st.selectbox("Select Gender",("Male","Female"),index=0,placeholder="Choose Gender ⬇")
senior_citezen = st.selectbox("Are You Senior Citezen?",("Yes","No"),index=0,placeholder="Choose From Below ⬇")
partener = st.radio("Do You Have Partner?",["Yes","No"],index=0)
dependents=st.radio("Has Any One Dependent On You?",["Yes","No"],index=0)
tenure=st.number_input("Since How Many Months You Are With The Company",value=1,placeholder="Enter Number Of Month",min_value=1,max_value=75)
PhoneService=st.radio("Do You Have Phone Service ?",["Yes","No"],index=1)
MultipleLines="No phone service"
if PhoneService=="Yes":
    MultipleLines = st.radio("Do You Have MultipleLine Phone Service ?",["Yes","No"],index=1)
InternetService=st.radio("Do You Have Internet Service ? If Yes Then Which ?",["Fiber optic","DSL","No"],index=1)
OnlineSecurity=st.radio("Do You Have Online Security ?",["Yes","No","No internet service"],index=1)
OnlineBackup=st.radio("Do You Have Online Backup ?",["Yes","No","No internet service"],index=1)
DeviceProtection=st.radio("Do You Have Device Protection ?",["Yes","No","No internet service"],index=1)
TechSupport=st.radio("Do You Have TechSupport ?",["Yes","No","No internet service"],index=1)
StreamingTV=st.radio("Do You Have Streaming TV ?",["Yes","No","No internet service"],index=1)
StreamingMovies=st.radio("Do You Have Streaming Movies ?",["Yes","No","No internet service"],index=1)
Contract=st.radio("What Is The Contract Term ?",["Month-to-month","Two year","One year"],index=1)
PaperlessBilling=st.radio("Do You Have Paperless Billing ?",["Yes","No"],index=1)
PaymentMethod=st.radio("Which Payment Method Do You Have ?",["Electronic check","Mailed check","Bank transfer (automatic)","Credit card (automatic)"],index=1)
MonthlyCharge = st.number_input("Amount Of Monthly Charges?",placeholder="Enter Amount",min_value=1.0)
TotalCharges = MonthlyCharge * tenure

if st.button("Submit",type="primary"):
    input_features = [[gender,senior_citezen,partener,dependents,tenure,PhoneService,MultipleLines,InternetService,OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,StreamingTV,StreamingMovies,Contract,PaperlessBilling,PaymentMethod,MonthlyCharge,TotalCharges]]
    data = pd.DataFrame(input_features,columns=columns)
    data_for_encode = data
    data["gender"]=data["gender"].map({"Male":1,"Female":0})
    data["SeniorCitizen"]=data["SeniorCitizen"].map({"Yes":1,"No":0})
    data["Partner"]=data["Partner"].map({"Yes":1,"No":0})
    data["Dependents"]=data["Dependents"].map({"Yes":1,"No":0})
    data["PhoneService"]=data["PhoneService"].map({"Yes":1,"No":0})
    data["MultipleLines"]=data["MultipleLines"].map({"Yes":2,"No phone service":1,"No":0})
    data["InternetService"]=data["InternetService"].map({"Fiber optic":1,"DSL":0,"No":2})
    data["OnlineSecurity"]=data["OnlineSecurity"].map({"Yes":2,"No internet service":1,"No":0})
    data["OnlineBackup"]=data["OnlineBackup"].map({"Yes":2,"No internet service":1,"No":0})
    data["DeviceProtection"]=data["DeviceProtection"].map({"Yes":2,"No internet service":1,"No":0})
    data["TechSupport"]=data["TechSupport"].map({"Yes":2,"No internet service":1,"No":0})
    data["StreamingTV"]=data["StreamingTV"].map({"Yes":2,"No internet service":1,"No":0})
    data["StreamingMovies"]=data["StreamingMovies"].map({"Yes":2,"No internet service":1,"No":0})
    data["Contract"]=data["Contract"].map({"Month-to-month":0,"Two year":2,"One year":1})
    data["PaperlessBilling"]=data["PaperlessBilling"].map({"Yes":1,"No":0})
    data["PaymentMethod"]=data["PaymentMethod"].map({"Electronic check":2,"Mailed check":3,"Bank transfer (automatic)":0,"Credit card (automatic)":1})
    scaled_data = Scaler.transform(data)
    print(scaled_data)
    pred = model.predict(scaled_data)[0]
    if pred==1:
        st.warning("Churned(Cancel Survice)")
    else:
        st.success("Loyal Customer")