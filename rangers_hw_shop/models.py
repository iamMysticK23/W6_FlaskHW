from werkzeug.security import generate_password_hash # generates hashed pw
from flask_sqlalchemy import SQLAlchemy # allows DB to read classes/objects as tables/rows
from flask_login import UserMixin, LoginManager # load a current logged in user
from datetime import datetime
import uuid # generates a unique id


db = SQLAlchemy() # instantiate DB
login_manager = LoginManager() # instantiate Login Manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id) # queries DB and brings back a user with the same id


class User(db.Model, UserMixin):
    user_id = db.Column(db.String, primary_key=True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    date_added = db.Column(db.DateTime, default= datetime.utcnow)

# similar to INSERT INTO
    def __init__(self, username, email, password, first_name="", last_name=""):
        self.user_id = self.set_id() # creates a unique id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = self.set_password(password) # hash pw for security

    def set_id(self):
        return str(uuid.uuid4())

    def set_password(self, password):
        return generate_password_hash(password)
    
    def __repr__(self):
        return f"<USER: {self.username}"
    


