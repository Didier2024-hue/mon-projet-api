from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from typing import List, Optional
import pandas as pd

app = FastAPI()

# -------------------
# Utilisateurs
# -------------------
USERS = {
    "alice": "wonderland",
    "bob": "builder",
    "clementine": "mandarine"
}
ADMIN_USER = "admin"
ADMIN_PASS = "4dm1N"

security = HTTPBasic()

# -------------------
# Charger CSV
# -------------------
try:
    df = pd.read_csv("questions.csv").fillna("")  # remplace NaN par vide
except:
    df = pd.DataFrame(columns=[
        "question", "subject", "use", "correct",
        "responseA", "responseB", "responseC", "responseD", "remark"
    ])

# -------------------
# Authentification
# -------------------
def verify_user(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username not in USERS:
        raise HTTPException(status_code=401, detail="Nom d'utilisateur inconnu")
    if USERS[credentials.username] != credentials.password:
        raise HTTPException(status_code=401, detail="Mot de passe incorrect")
    return credentials.username

# -------------------
# Utilitaire réponse correcte
# -------------------
def get_correct_answer(row):
    mapping = {
        "A": row.get("responseA"),
        "B": row.get("responseB"),
        "C": row.get("responseC"),
        "D": row.get("responseD")
    }
    correct_letter = str(row.get("correct", "")).strip()
    return [mapping.get(correct_letter)] if correct_letter in mapping else []

# -------------------
# Modèles Pydantic
# -------------------
class QuizRequest(BaseModel):
    test_type: str
    categories: List[str]
    number_of_questions: int

class QuestionRequest(BaseModel):
    admin_username: str
    admin_password: str
    question: str
    subject: str
    correct: str
    use: str
    responseA: str
    responseB: str
    responseC: str
    responseD: Optional[str] = ""
    remark: Optional[str] = ""

# -------------------
# Endpoints
# -------------------
@app.get("/verify")
def verify():
    return {"message": "L'API est fonctionnelle."}

@app.post("/generate_quiz")
def generate_quiz(request: QuizRequest, username: str = Depends(verify_user)):
    global df
    filtered = df[
        (df["use"] == request.test_type) &
        (df["subject"].isin(request.categories))
    ]

    if filtered.empty:
        raise HTTPException(status_code=404, detail="Aucune question trouvée.")

    if request.number_of_questions not in [5, 10, 20]:
        raise HTTPException(status_code=400, detail="Le nombre de questions doit être 5, 10 ou 20.")

    sample = filtered.sample(n=min(request.number_of_questions, len(filtered)))

    results = []
    for _, row in sample.iterrows():
        row_dict = row.to_dict()
        # Nettoyer NaN → None
        clean_row = {k: (None if pd.isna(v) or v == "" else v) for k, v in row_dict.items()}

        results.append({
            "question": clean_row.get("question"),
            "subject": clean_row.get("subject"),
            "use": clean_row.get("use"),
            "correct": get_correct_answer(clean_row),
            "responseA": clean_row.get("responseA"),
            "responseB": clean_row.get("responseB"),
            "responseC": clean_row.get("responseC"),
            "responseD": clean_row.get("responseD"),
            "remark": clean_row.get("remark")
        })
    return results

@app.post("/create_question")
def create_question(request: QuestionRequest):
    if request.admin_username != ADMIN_USER or request.admin_password != ADMIN_PASS:
        raise HTTPException(status_code=403, detail="Accès refusé : admin requis.")

    new_row = {
        "question": request.question,
        "subject": request.subject,
        "use": request.use,
        "correct": request.correct,
        "responseA": request.responseA,
        "responseB": request.responseB,
        "responseC": request.responseC,
        "responseD": request.responseD,
        "remark": request.remark
    }

    global df
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv("questions.csv", index=False)

    return {"message": "Question créée avec succès."}
