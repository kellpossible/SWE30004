from app import app
import os

from app.models import db
db.create_all()

if __name__ == "__main__":
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT",2227)), threaded=True)

