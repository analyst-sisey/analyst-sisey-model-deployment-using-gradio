
#Import the required Libraries
import gradio as gr
import pickle
import pandas as pd
import numpy as np

scaler2 = pickle.load(open('scaler2.pkl','rb'))
# load the model

def load_model():
   with open('logi_reg1.pkl','rb') as file:
      logi_reg1 = pickle.load(file)
      return logi_reg1


#function to load encoder
def load_label_encoder():
   with open("encoder2.pkl", 'rb') as file:
      encoder2 = pickle.load(file) 
      return encoder2

label_encoder = load_label_encoder()
model = load_model()



# seprate features and target

def predict_model(tenure,gender,Partner,Dependents,MonthlyCharges,PhoneService,MultipleLines,InternetService,OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,PaymentMethod,PaperlessBilling,Contract):        
   
    categorical_features= [gender,Partner,Dependents,PhoneService,MultipleLines,InternetService,OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,PaymentMethod,PaperlessBilling,Contract]
    numeric_features =[tenure,MonthlyCharges]
    df_new = pd.DataFrame([numeric_features],columns=[tenure,MonthlyCharges])
    df_new1 = pd.DataFrame([categorical_features],columns=[gender,Partner,Dependents,PhoneService,MultipleLines,InternetService,OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,PaymentMethod,PaperlessBilling,Contract])
    
    encoded_features1 =  pd.DataFrame([encoded_features1], columns= [gender,Partner,Dependents,PhoneService,MultipleLines,InternetService,OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,PaymentMethod,PaperlessBilling,Contract])
    X_test1 = pd.concat([df_new, encoded_features1],axis=1)
    
    predict = model.predict(X_test1)
    return predict

    # app interface using blocks
with gr.Blocks(css=".gradio-container {background-color: powderblue}") as demo:
    
    gr.Markdown("Classification Model that Predicts Customer Churn")
    with gr.Row():
        tenure = gr.Slider(0, 100)
        Contract = gr.Dropdown(['Month-to-month','One year','Two year'], label="Select Contract Type")
        gender = gr.Dropdown(['Male','Female'], label="Select Customer Gender")
    with gr.Row():
        MonthlyCharges = gr.Textbox(label="Input Monthly Charge")
        PaymentMethod = gr.Dropdown(['Credit card (automatic)','Bank transfer (automatic)','Mailed check','Electronic check'  ], label="Select Payment Method")
        PaperlessBilling = gr.Dropdown(['Paperless','Other'], label="Select Billing Type")
        
    with gr.Row():
        Dependents = gr.Radio(["Yes", "No"], label="Customer has Dependants?")
        Partner = gr.Radio(["Yes", "No"], label="Customer has Partner?")
        OnlineBackup = gr.Radio(["Yes", "No"], label="Customer have backup services?")
    with gr.Row():
        TechSupport = gr.Radio(["Yes", "No"], label="Customer has Techical support?")
        PhoneService = gr.Radio(["Yes", "No"], label="Customer has Phone services?")
        OnlineSecurity = gr.Radio(["Yes", "No"], label="Customer has Online security?")
    with gr.Row():
        DeviceProtection =  gr.Radio(["Yes", "No"], label="Customer has device protection?")
        InternetService =  gr.Radio(["Yes", "No"], label="Customer has internet services?")
        MultipleLines =  gr.Radio(["Yes", "No"], label="Customer has multiple lines?")
    with gr.Row():
        #inbtw = gr.Button("Between")
        btn = gr.Button("Predict").style(full_width=True)
        output = gr.Textbox(label="Classification Result")

        btn.click(predict_model, inputs=[tenure,gender,Partner,Dependents,MonthlyCharges,PhoneService,MultipleLines,InternetService,OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,PaymentMethod,PaperlessBilling,Contract], outputs=output)   

demo.launch()
