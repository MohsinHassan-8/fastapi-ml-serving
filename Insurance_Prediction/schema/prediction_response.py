from pydantic import BaseModel, Field
from typing import Dict

class PredictionResponse(BaseModel):
       predicted_category : str = Field(..., description='Predicted Insurance Category', example='High')
       confidence : float = Field(..., description="Model's confidence score for predicted class", example=0.8473)
       class_probabilities : Dict[str, float] = Field(..., description="Prob distribution across all possible classes", example={'Low' : 0.52, 'Medium' : 0.38, 'High' : 0.10})
