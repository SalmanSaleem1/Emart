from mart import app, db
from mart.models import Users, Categories, SubCategories


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Users': Users, 'Categories': Categories, 'SubCategories': SubCategories}
