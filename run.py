from wahlanwendung import app
from wahlanwendung.models import progr_sprache

app.run(host='0.0.0.0', debug=True)

progr_sprache.query.all()