from flask_admin.contrib.sqla import ModelView
from wahlanwendung import admin, db, models

admin.add_view(ModelView(models.progr_spr, db.session))
admin.add_view(ModelView(models.sessionergebnis, db.session))

models.db.create_all()
