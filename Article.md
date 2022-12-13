Deploying Machine Learning Models Using Gradio
The last stage of the CRISP-DM model is deployment. Building a machine learning model is important for practical business decision-making. A machine learning model in a jupyter Notebook or other development tools however does not fully deliver value to users. For a machine learning model to be of practical importance and deliver value to decision-makers, it must be deployed to production. This allows non-technical users to interact with the model for practical decision-making. One of the ways to deploy a machine learning model is to embed it into a web app. 

Gradio is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning. Embedding a machine learning model into a web app usually requires familiarity with Javascript, HTML, and CSS or other web frameworks such as Django and Flask. Gradio is the fastest way to demo your machine learning model with a friendly web interface so that anyone can use it anywhere. Creating a Gradio interface only requires adding a few lines of code to your project. It allows users to choose from a variety of interface types to interface their function.

This article will explain how to deploy a machine-learning model using gradio app. A detailed description of the process and the code can be found in the project repository on GitHub

Building your model
Before starting the deployment process, it is important to have a trained model ready. We will not explain how to build a model in this article. We will use the classification model for predicting customer churn we created earlier. You can read how to create the classification model and have access to the python notebook here.

Saving your model and other ML items
After the model is ready, we need to save it so that we can load it into our app. We will also save other machine-learning items such as the feature encoder and scaler. Saving the model and other items to file is known as serialization while accessing or opening it is known as deserialization. There are different methods for saving a model and other ML items (serialization) such as pickle, joblib, json, PMML, and others. We will be using pickle for serialization and deserialization.
To save our machine learning model using pickle, we have to import pickle and use the pickle.dump() method. This method takes two arguments: the model you want to save and a file-like object where the model will be saved. We use this method to save our LogisticRegression model, OneHotEncoder(), and MinMaxScaler().

Install gradio and Build the application
Once the classification model is trained and saved, the next step is to install gradio. This can be done by running the "pip install gradio" command on the command line. Detailed instructions on installing gradio can be found on the app website.
 Once gradio is installed, we can start building the deployment application. The first step is to import the necessary libraries and load our saved LogisticRegression model, OneHotEncoder(), and MinMaxScaler().
Next, we need to create the user interface for the classification model. gradio provides a simple and intuitive syntax for building user interfaces. In this example, we will create a simple form where the user can enter the input features for the classification model and submit the form to get the prediction. The gradio.Block class was preferred because it offers more flexibility and control 
Loading your model and other items
After our interface is ready, we import the necessary libraries and load the saved LogisticRegression model, OneHotEncoder(), and MinMaxScaler(). We open our model and other machine learning items that have been saved with pickle using the pickle.load() method. This method takes a file-like object that points to the saved model and returns the model.
Next, we create a function that accepts the user input, encodes the categorical features by fitting them to the OneHotEncoder(), scaling the features by fitting them to the MinMaxScaler(), and predicting using the LogisticRegression model.
Once the user interface and the function are ready, we run the gradio application. This will start the gradio server and open the application in the user's default web browser. The user can now enter the input values and get the prediction from the LogisticRegression model.

In conclusion, deploying any model using gradio is a simple and efficient way to provide users access to ML models for practical business decision making. The intuitive syntax and user-friendly interface make it a great choice for the deployment of models and other data applications.
