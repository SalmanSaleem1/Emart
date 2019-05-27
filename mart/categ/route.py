from flask import *
from mart.constant.appConstant import Constant
from mart.models import Categories
from mart import db
from mart.categ.forms import CategoryForm, SubCategoryForm

categ = Blueprint('categ', __name__)


@categ.route('/add_cat', methods=[Constant.GET, Constant.POST])
def add_cat():
    form = CategoryForm()
    if form.validate_on_submit():
        cat = Categories(name=form.name.data)
        db.session.add(cat)
        db.session.commit()
        return redirect(url_for('main.home'))
    return render_template('add_category.html', form=form)


@categ.route('/add_sub_cat', methods=[Constant.GET, Constant.POST])
def add_sub_cat():
    form = SubCategoryForm()
    if form.validate_on_submit():
        cat = Categories(name=form.name.data)
        db.session.add(cat)
        db.session.commit()
        return redirect(url_for('main.home'))
    return render_template('add_sub_cat.html', form=form)
