from flask import *
from mart.constant.appConstant import Constant
from mart.models import Categories, SubCategories
from mart import db
from mart.categ.forms import CategoryForm, SubCategoryForm

categ = Blueprint('categ', __name__)


@categ.route('/add_cat', methods=[Constant.GET, Constant.POST])
def add_cat():
    form = CategoryForm()
    categories = Categories.query.all()
    if form.validate_on_submit():
        cat = Categories(name=form.name.data)
        db.session.add(cat)
        db.session.commit()
        return redirect(url_for('categ.add_cat'))
    return render_template('add_category.html', form=form, categories=categories)


@categ.route('/add_cat/<int:id>', methods=[Constant.GET, Constant.POST])
def active_action(id):
    sub_id = Categories.query.get_or_404(id)

    if sub_id.deleted == False:
        sub_id.deleted = True
        db.session.commit()
    else:
        sub_id.deleted = False
        db.session.commit()
    return redirect(url_for('categ.add_cat'))


@categ.route('/add_sub_cat', methods=[Constant.GET, Constant.POST])
def add_sub_cat():
    if request.method == Constant.POST:
        cat = request.form.get('select_value')
    else:
        cat = None
    print(cat)
    form = SubCategoryForm()
    categories = Categories.query.all()
    sub_catagories = SubCategories.query.all()

    for one_cat in categories:
        if cat == one_cat.name:
            cat_id = one_cat.name
            print(cat_id)
            break
    if form.validate_on_submit():
        cat = SubCategories(name=form.subcat_name.data, categories_id=cat_id)
        db.session.add(cat)
        db.session.commit()
        return redirect(url_for('categ.add_cat'))
    return render_template('add_sub_cat.html', form=form, categories=categories, sub_catagories=sub_catagories)


@categ.route('/add_sub_cat/<int:id>', methods=[Constant.GET, Constant.POST])
def active_sub_cat(id):
    sub_id = SubCategories.query.get_or_404(id)

    if sub_id.deleted == False:
        sub_id.deleted = True
        db.session.commit()
    else:
        sub_id.deleted = False
        db.session.commit()
    return redirect(url_for('categ.add_sub_cat'))


@categ.route('/add_sub_cat/delete/<int:id>', methods=[Constant.GET, Constant.POST])
def delete_sub_cat(id):
    sub_id = SubCategories.query.get_or_404(id)
    db.session.delete(sub_id)
    db.session.commit()
    flash(f'{Constant.DELETE_SUCCESSFULLY}', f'{Constant.SUCCESS}')
    return redirect(url_for('categ.add_sub_cat'))
