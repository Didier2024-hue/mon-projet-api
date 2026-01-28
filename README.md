📖 Description
Cette API permet de générer des questionnaires (QCM) à partir d'une base de données de questions. Elle est développée avec FastAPI et offre une documentation interactive via OpenAPI/Swagger.

✨ Fonctionnalités
✅ Vérification de l'état de l'API

🎯 Génération de QCM personnalisés avec paramètres:

Type de test

Catégories de questions

Nombre de questions

🔐 Authentification basique pour sécuriser les endpoints

📝 Création de nouvelles questions (réservé aux administrateurs)

🎲 Randomisation des questions pour varier les QCM

🚀 Installation
Prérequis
Python 3.8+

pip

Installation des dépendances
bash
pip install fastapi uvicorn python-multipart
Structure des fichiers
text
fastapi_exam/
├── main.py              # Point d'entrée de l'application
├── questions.csv        # Base de données des questions
├── optional_archi.txt   # Documentation d'architecture (optionnel)
└── README.md           # Ce fichier
📊 Structure des données
Le fichier questions.csv contient les champs suivants:

question: Intitulé de la question

subject: Catégorie de la question

correct: Liste des réponses correctes

use: Type de QCM

responseA, responseB, responseC, responseD: Réponses possibles

🔑 Authentification
L'API utilise l'authentification HTTP Basic avec les identifiants suivants:

Utilisateur	Mot de passe
alice	wonderland
bob	builder
clementine	mandarine
admin	4dm1N
Les identifiants doivent être encodés en Base64 et inclus dans les headers:

text
Authorization: Basic dXNlcjpwYXNz
🌐 Endpoints
1. GET /verify
Vérifie que l'API est fonctionnelle.

Exemple de réponse:

json
{"message": "L'API est fonctionnelle."}
2. POST /generate_quiz
Génère un QCM basé sur les paramètres fournis.

Headers requis:

text
Authorization: Basic <base64_credentials>
Content-Type: application/json
Body (JSON):

json
{
  "test_type": "multiple_choice",
  "categories": ["math", "history"],
  "number_of_questions": 10
}
Réponse: Liste de questions au format JSON.

3. POST /create_question
Crée une nouvelle question (réservé aux administrateurs).

Body (JSON):

json
{
  "admin_username": "admin",
  "admin_password": "4dm1N",
  "question": "Quelle est la capitale de la France ?",
  "subject": "geography",
  "correct": ["Paris"],
  "use": "multiple_choice",
  "responseA": "Londres",
  "responseB": "Paris",
  "responseC": "Berlin",
  "responseD": "Madrid"
}
Réponse:

json
{"message": "Question créée avec succès."}
🏃‍♂️ Démarrage
Lancer le serveur
bash
uvicorn main:app --reload
Accéder à la documentation
Swagger UI: http://localhost:8000/docs

Redoc: http://localhost:8000/redoc

🧪 Tests
La documentation interactive (Swagger UI) permet de tester directement les endpoints depuis le navigateur.
