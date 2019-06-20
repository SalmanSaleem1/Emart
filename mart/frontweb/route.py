from flask import *
from mart.models import Categories, Subcategories, Products
from mart.constant.appConstant import Constant
from mart.frontweb.forms import UserPost
from mart.models import PostUser
from mart import db

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


@front_web.route('/post_front', methods=[Constant.GET, Constant.POST])
def front_post():
    form = UserPost()
    user_post = PostUser.query.all()
    if form.validate_on_submit():
        post_user = PostUser(title=form.title.data, content=form.content.data)
        db.session.add(post_user)
        db.session.commit()
        return redirect(url_for('main.home'))
    return render_template('add_front_post.html', form=form, user_post=user_post)


@front_web.route('/show_user_post', methods=[Constant.GET, Constant.POST])
def show_user_post():
    user_post = PostUser.query.all()
    return render_template('show_user_post.html', user_post=user_post)


@front_web.route('/post_front/<int:id>', methods=[Constant.GET, Constant.POST])
def active_post_user(id):
    post_user = PostUser.query.get_or_404(id)

    if post_user.status == False:
        post_user.status = True
        db.session.commit()
    else:
        post_user.status = False
        db.session.commit()
    return redirect(url_for('front_web.front_post'))
