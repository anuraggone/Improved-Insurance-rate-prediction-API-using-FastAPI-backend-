import pandas as pd
import pickle

# import the ml model
with open('model/insurance_model.pkl', 'rb') as f:
    model = pickle.load(f)  

# variable that stores all the classes 

class_labels = model.classes_.tolist()

def predict(user_input : dict):
    
    # took the input which was a dictionary and convert it into a list 
    input_df= pd.DataFrame([user_input])
    
    # Predict the class and return the first value 
    prediction_class = model.predict(input_df)[0]
    
    
    # probabilities for all the classes
    probabilities = model.predict_proba(input_df)[0]
    confidence = max(probabilities)
    
    # Creating mapps : {class name : probabality}    
    class_probs = dict(zip(class_labels, map(lambda p: round(p,4), probabilities)))
    
    return {
        "predicted category" : prediction_class ,
        "confidance" :round(confidence , 4),
        "class_probabilities": class_probs
    }