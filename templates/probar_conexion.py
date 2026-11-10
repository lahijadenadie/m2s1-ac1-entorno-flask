from app import app, db

with app.app_context():
    version = db.session.execute(db.text("SELECT sqlite_version()")).scalar()
    print("Conexión exitosa. Versión de SQLite:", version)