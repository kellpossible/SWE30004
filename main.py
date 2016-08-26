from app import app

from app.models import db
db.create_all()

if __name__ == "__main__":
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.run(host="0.0.0.0", debug=True, threaded=True)
