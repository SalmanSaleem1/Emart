from flask import *
from mart.constant.appConstant import Constant
from flask_login import login_required

main = Blueprint('main', __name__)


@main.route('/', methods=[Constant.GET, Constant.POST])
@login_required
def home():
    return render_template('home.html')
