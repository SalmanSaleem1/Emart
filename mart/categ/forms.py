from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError
from mart.models import Categories
from mart.constant.appConstant import Constant
from wtforms.validators import DataRequired


class CategoryForm(FlaskForm):
    name = StringField(f'{Constant.NAME}', validators=[DataRequired()])
    submit = SubmitField(f'{Constant.SUBMIT}')

    def validate_name(self, name):
        cat = Categories.query.filter_by(name=name.data).first()
        if cat:
            raise ValidationError(f'{Constant.NAME_ALREADY_EXIST}', f'{Constant.INFO_FLASH_MESSAGE}')


class SubCategoryForm(FlaskForm):
    subcat_name = StringField(f'{Constant.NAME}')
    submit = SubmitField(f'{Constant.SUBMIT}')
