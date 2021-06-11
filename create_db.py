from wahlanwendung import models


models.db.create_all()
#models.db.session.commit()
models.db.drop_all()

