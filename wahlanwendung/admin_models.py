from flask_admin.contrib.sqla import ModelView
from wahlanwendung import admin, db, models

admin.add_view(ModelView(models.fragenkat, db.session))
admin.add_view(ModelView(models.antwortkat, db.session))
admin.add_view(ModelView(models.progrSpr, db.session))

#models.db.create_all()
