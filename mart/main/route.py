from flask import *
from mart.constant.appConstant import Constant
from flask_login import login_required
from mart.models import SubCategories


main = Blueprint('main', __name__)


@main.route('/', methods=[Constant.GET, Constant.POST])
@login_required
def home():
    # sub_cat = SubCategories.query.filter_by(deleted=True)
    sub_cat = SubCategories.query.all()
    return render_template('home.html', sub_cat=sub_cat)
