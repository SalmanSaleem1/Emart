from flask import *
from mart.constant.appConstant import Constant
from flask_login import login_required
from mart.models import Subcategories, Categories


main = Blueprint('main', __name__)


@main.route('/', methods=[Constant.GET, Constant.POST])
@login_required
def home():
    sub_cat = Subcategories.query.all()
    cat = Categories.query.all()
    return render_template('home.html', cat=cat, sub_cat=sub_cat)
