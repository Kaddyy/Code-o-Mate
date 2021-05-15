from flask_admin.contrib.sqla import ModelView
from wahlanwendung import admin, db, models

admin.add_view(ModelView(models.progr_spr, db.session))
admin.add_view(ModelView(models.fragenkatalog, db.session))
admin.add_view(ModelView(models.antwortkatalog, db.session))

models.db.create_all()
