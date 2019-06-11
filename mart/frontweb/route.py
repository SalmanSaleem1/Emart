from flask import *
from mart.models import Categories, Subcategories, Products
from mart.constant.appConstant import Constant

front_web = Blueprint('front_web', __name__)


@front_web.route('/', methods=[Constant.GET, Constant.POST])
def front_home():
    all_cat = Categories.query.all()
    return render_template('frontHome.html', all_cat=all_cat)


@front_web.route('/sub/<string:sub_id>', methods=[Constant.GET, Constant.POST])
def show_sub_cat(sub_id):
    sub_cat = Subcategories.query.filter_by(categories_id=sub_id)
    return render_template('front_sub_cat.html', sub_cat=sub_cat)


@front_web.route('/product/<string:pro_id>', methods=[Constant.GET, Constant.POST])
def show_pro_id(pro_id):
    pro_item = Products.query.filter_by(sub_cat_id=pro_id)
    return render_template('front_products.html', pro_item=pro_item)
