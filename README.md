# 🚀 Flask-Multi-Template

Flask-Multi-Template est une **base Flask modulaire**, légère et propre, conçue pour démarrer rapidement n’importe quel projet web Flask.

## 📁 Structure du projet

```
Template/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── templates/
│   │   ├── includes/
│   │   │   ├── base.html
│   │   │   ├── navbar.html
│   │   │   └── footer.html
│   │   └── index.html
│   └── static/
│       ├── css/
│       ├── js/
│       └── images/
├── includes/
│   ├── config.py
│   └── constants.py
├── LICENSE.md
├── README.md
├── requirements.txt
└── run.py
```

---

## ⚙️ Configuration (`includes/constants.py`)

```python
APP_NAME = "Flask-Multi-Template"       # Nom de l'app
DEBUG_MODE = True                       # Mode debug actif
ENV = "development"                     # Modes possibles : development, production, testing
SECRET_KEY = "supersecretkey"           # À changer en production

HOST = "127.0.0.1"                      # IP du serveur (0.0.0.0 pour rendre public)
PORT = 5000                             # Port utilisé par Flask
SITE_URL = f"http://{HOST}:{PORT}"      # URL complète

LANG = "fr"                             # Langue principale
TIMEZONE = "Europe/Paris"               # Fuseau horaire

ENABLE_API_MODE = False                 # Active un mode API si besoin

UPLOAD_FOLDER = "uploads/"              # Dossier d’upload
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}  # Types de fichiers acceptés

ENABLE_LOGGING = True                   # Active les logs
LOG_LEVEL = "DEBUG"                     # Niveaux : DEBUG, INFO, WARNING, ERROR, CRITICAL
```

---

## ▶️ Lancer le projet

```bash
# Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate sous Windows

# Installer les dépendances
pip install -r requirements.txt

# Lancer le serveur Flask
python run.py
```

---

## 🌐 Interface de base

- `base.html` extensible avec `navbar` et `footer` inclus
- Tailwind CSS via CDN intégré
- `index.html` comme point d'entrée
- Organisation prête pour composants réutilisables

---

## 📦 Prévu pour évoluer

- Prise en charge future d’une API Flask (activable)
- Uploads et internationalisation
- Ajout facile de blueprints supplémentaires

---

## 🛠️ Dépendances

```
Flask==3.0.2
```

---

## 🧪 À venir (idées d'amélioration)

- Passage à Tailwind CLI pour purge et build auto
- Support `.env` avec `python-dotenv`
- Dockerisation
- Authentification simple

---

## 🧑‍💻 Auteur

Made with ❤️ by [ZalgoDev](https://github.com/Zalgo-Dev)
