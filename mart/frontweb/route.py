from datetime import timedelta
import datetime
import sys
import time

from celery import Celery
from flask import *

from mart import db, app
from mart.constant.appConstant import Constant
from mart.frontweb.forms import UserPost
from mart.models import Categories, Subcategories, Products
from mart.models import PostUser

celery = Celery('hello', broker="redis://guest@localhost//", backend='redis')

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
    # print(countdown(60))
    one_day_interval_before = datetime.datetime.now() - timedelta(minutes=1)
    print(one_day_interval_before)
    now = datetime.datetime.now()
    new_now = datetime.datetime.strftime(now, '%a, %d %b %Y %H:%M:%S %Z')
    # print(new_now)
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


# here celery tasks


def countdown(totalTime):
    try:
        while totalTime >= 0:
            mins, secs = divmod(totalTime, 60)
            sys.stdout.write("\rWaiting for {:02d}:{:02d}  minutes...".format(mins, secs))
            sys.stdout.flush()
            time.sleep(1)
            totalTime -= 1
            if totalTime <= -1:
                print
                "\n"
                break
    except KeyboardInterrupt:
        exit("\n^C Detected!\nExiting...")


@celery.task
def index():
    try:
        now = datetime.datetime.now()
        before = timedelta(minutes=1)
        now = now.replace(microsecond=0)
        before = (now + before)
        now = (now.strftime("%b %d %X"))
        # before = (before.strftime("%b %d %X"))
        # print('Before ' + before)
        # print('Now ' +now)
        since = datetime.datetime.now()-timedelta(minutes=5)
        print(since)
        post = PostUser.query.filter_by(status=False).first()

        db.session.delete(post)
        db.session.commit()
    except:
        print('empty table')
    return 'sent'


@celery.task
def create_db():
    db.create_all()
    return 'create'


@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        timedelta(seconds=30),
        index,
    )
