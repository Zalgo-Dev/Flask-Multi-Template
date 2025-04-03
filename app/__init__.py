from datetime import datetime
from flask import Flask
from includes.config import Config
from app.routes import main_bp
import logging

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Logging configuré dynamiquement
    if app.config.get("ENABLE_LOGGING"):
        log_level = getattr(logging, app.config["LOG_LEVEL"].upper(), logging.INFO)
        logging.basicConfig(level=log_level)
        app.logger.setLevel(log_level)
        app.logger.info("Logging activé.")

    # Blueprints
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    # Variables globales dans Jinja
    from includes.constants import APP_NAME
    from datetime import datetime

    @app.context_processor
    def inject_globals():
        return dict(
            config=dict(APP_NAME=APP_NAME),
            now=lambda: datetime.now()
        )

    return app
