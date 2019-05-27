from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

from mart.config import Config

app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)
db = SQLAlchemy(app)
admin = Admin(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
mail = Mail(app)

login = LoginManager(app)
login.login_view = 'user.login'
login.login_message_category = 'info'

from mart.models import Users

admin.add_view(ModelView(Users, db.session))

# BluePrints route here
from mart.user.route import user
from mart.main.route import main
from mart.categ.route import categ

app.register_blueprint(user)
app.register_blueprint(main)
app.register_blueprint(categ)