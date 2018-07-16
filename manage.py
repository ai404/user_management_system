from Settings import Settings
from app import manager as app

if __name__=="__main__":
    settings = Settings()
    settings.populate_db()
    app.run()