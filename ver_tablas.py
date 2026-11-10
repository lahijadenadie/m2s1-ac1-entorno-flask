from sqlalchemy import inspect
from app import app, db

with app.app_context():
    inspector = inspect(db.engine)
    print("Tablas existentes:", inspector.get_table_names())