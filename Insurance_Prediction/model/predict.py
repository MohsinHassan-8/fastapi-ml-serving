import pickle
import pandas as pd

with open('model/model.pkl', 'rb') as f:
       model = pickle.load(f)

MODEL_VERISON = '1.0.0' #ML Flow

class_labels = model.classes_.tolist()

def predict_output(user_input : dict):
       df = pd.DataFrame([ user_input ])
       predicted_class = model.predict(df)[0]
       probs = model.predict_proba(df)[0]
       confidence = max(probs)

       class_probs = dict(zip(class_labels, map(lambda p: round(p,4), probs)))

       return {
              'predicted_category' : predicted_class,
              'confidence' : round(confidence, 4),
              'class_probabilities' : class_probs
       }


