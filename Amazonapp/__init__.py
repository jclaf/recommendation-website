import os
from flask import Flask
from .views import main as main_blueprint
from flask_sqlalchemy import SQLAlchemy
from .extensions import db
import pandas as pd
import click


def create_app():
    base_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    app = Flask(__name__, template_folder=os.path.join(base_dir, 'templates'), static_folder=os.path.join(base_dir, 'static'))
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config.py')
    app.config.from_pyfile(config_path)
    db.init_app(app)
    
    app.register_blueprint(main_blueprint)
    @app.cli.command("init-db")
    def init_db_command():
        from . import models
        """Initialize the database."""
        models.init_db()
        print("Initialized the database.")
        
    @app.cli.command("import-csv")
    @click.option('--csv-path', default='products.csv', help='Chemin du fichier CSV à importer.')
    def import_csv(csv_path):
        from .models import Product
        """Importe les produits à partir d'un fichier CSV spécifié."""
        df = pd.read_csv(csv_path, encoding='utf-8')
        df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
        products = [
            Product(
                name=row['name'],
                description=row['description'],
                price=row['price'],
                stock=row['stock'],
                category=row['category'],
                image_url=row['image_url'],
                rating=row.get('rating', 0.0),
                review_count=row.get('review_count', 0)
            )
            for _, row in df.iterrows()
        ]

        db.session.bulk_save_objects(products)
        db.session.commit()
        print(f"{len(products)} produits importés depuis {csv_path}")    
    
    return app