from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from model.predict import predict

app = FastAPI()

# for non-conscious being         
@app.get('/health')
def health_check():
    return{
        "Status" : "OK"
    }

# for conscious being        
@app.get('/')
def home():
    return {"Content" : "API for insurance premium prediction"}

@app.post('/predict')
def predict_premium(data: UserInput):

    user_input = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }
    try:
        prediction = predict(user_input)
        return JSONResponse(status_code=200, content={'predicted_category': prediction})
     
    except Exception as ex:
        return JSONResponse(status_code= 500, content=str(ex))





