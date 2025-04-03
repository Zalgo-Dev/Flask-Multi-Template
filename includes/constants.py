# Nom de l'application affiché dans le titre et le header
APP_NAME = "TemplateFlask"

# Active ou désactive le mode debug (rechargement automatique, affichage des erreurs)
DEBUG_MODE = True

# Mode de l'application : 
# - development : pour coder en local
# - production : pour déployer en ligne
# - testing : pour les tests automatisés
ENV = "development"

# Clé secrète utilisée pour sécuriser les sessions et cookies (à changer en prod !)
SECRET_KEY = "supersecretkey"

# Adresse IP sur laquelle le serveur Flask va tourner
# - "127.0.0.1" : uniquement en local
# - "0.0.0.0" : accessible depuis l'extérieur (public)
HOST = "127.0.0.1"

# Port sur lequel le serveur tourne
PORT = 5000

# URL complète du site (utilisée pour les redirections, liens absolus, etc.)
SITE_URL = f"http://{HOST}:{PORT}"

# Langue par défaut de l'app
LANG = "fr"

# Fuseau horaire utilisé (exemples : "Europe/Paris", "UTC", "America/New_York")
TIMEZONE = "Europe/Paris"

# Active ou désactive le mode API (si tu veux proposer des routes /api plus tard)
ENABLE_API_MODE = False

# Dossier où les fichiers uploadés seront enregistrés
UPLOAD_FOLDER = "uploads/"

# Extensions de fichiers autorisées pour l'upload
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Active ou désactive les logs dans la console
ENABLE_LOGGING = True

# Niveau de log :
# - DEBUG : détails complets (pour développement)
# - INFO : informations normales (pour production)
# - WARNING : avertissements
# - ERROR : erreurs
# - CRITICAL : erreurs très graves
LOG_LEVEL = "DEBUG"
