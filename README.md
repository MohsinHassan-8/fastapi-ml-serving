# FastAPI: from basics to a containerised ML endpoint

A progression of small projects showing how I learned to serve a model with FastAPI and Pydantic.

## What is inside

| Folder / file | What it shows |
|---|---|
| `main.py` + `patients.json` | CRUD-style patient API: Pydantic models, computed fields (BMI, verdict), validated sort parameters, 404 handling |
| `Pydantic/` | Seven short scripts: computed fields, field and model validators, nested models, serialisation, constrained types, email/URL types |
| `Insurance/` | Notebook that builds the features and trains a Random Forest pipeline that predicts an insurance-premium category (Low / Medium / High) |
| `app.py` + `frontend.py` | Flat version: FastAPI endpoint plus a Streamlit form |
| `Insurance_Prediction/` | Modular version: schemas, config, model loader, `/health`, response schema with confidence and class probabilities, and a Dockerfile |

## Run the prediction API

```bash
cd Insurance_Prediction
pip install -r requirements.txt
uvicorn app:app --port 8000
```

Example request:

```json
POST /predict
{"age": 24, "weight": 62, "height": 1.72, "income_lpa": 4, "smoker": false, "city": "Pune", "occupation": "student"}
```

Response:

```json
{"predicted_category": "Low", "confidence": 0.74, "class_probabilities": {"High": 0.0, "Low": 0.74, "Medium": 0.26}}
```

Derived features (BMI, lifestyle risk, age group, city tier) are computed by the API from the raw inputs, so clients send only the raw fields.

Docker: `docker build -t insurance-api . && docker run -p 8000:8000 insurance-api` (from `Insurance_Prediction/`).

## Note on the model

The model is trained on a 100-row sample dataset. This repository is about serving, validation and packaging, not model accuracy. The saved model needs **scikit-learn 1.7.2** (pinned).

---
**Author:** Mohsin Hassan · [GitHub](https://github.com/MohsinHassan-8) · [LinkedIn](https://linkedin.com/in/mohsin-hassan-gen-ai)
