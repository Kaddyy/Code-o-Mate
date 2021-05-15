from wahlanwendung import db

class progr_spr(db.Model):
    __table_args__ = {'extend_existing': True}
    pk_sprache = db.Column(db.String, primary_key=True)
    beschreibung = db.Column(db.String, unique=True, nullable=False)
    absolutes_erg = db.Column(db.Integer, unique=False, nullable=False, default=0)
    relatives_erg = db.Column(db.Integer, unique=False, nullable=False, default=0)
    link1 = db.Column(db.String, unique=False, nullable=False)
    link2 = db.Column(db.String, unique=False, nullable=True)
    link3 = db.Column(db.String, unique=False, nullable=True)

class fragenkatalog(db.Model):
    __table_args__ = {'extend_existing': True}
    pk_frage_id = db.Column(db.Integer, primary_key=True)
    frage = db.Column(db.String, unique=False, nullable=False)


class antwortkatalog(db.Model):
    __table_args__ = {'extend_existing': True}
    pk_antwort_id = db.Column(db.String, primary_key=True)
    fragennummer = db.Column(db.Integer, unique=False, nullable=False)
    antwort = db.Column(db.String, unique=False, nullable=False)
    java = db.Column(db.Integer, unique=False, nullable=False, default=0)
    python = db.Column(db.Integer, unique=False, nullable=False, default=0)
    swift = db.Column(db.Integer, unique=False, nullable=False, default=0)
    cplusplus = db.Column(db.Integer, unique=False, nullable=False, default=0)
    csharp = db.Column(db.Integer, unique=False, nullable=False, default=0)
    javascript = db.Column(db.Integer, unique=False, nullable=False, default=0)
    matlab = db.Column(db.Integer, unique=False, nullable=False, default=0)
    go = db.Column(db.Integer, unique=False, nullable=False, default=0)
    htmlcss = db.Column(db.Integer, unique=False, nullable=False, default=0)
    sql = db.Column(db.Integer, unique=False, nullable=False, default=0)
    php = db.Column(db.Integer, unique=False, nullable=False, default=0)
    r = db.Column(db.Integer, unique=False, nullable=False, default=0)
    typescript = db.Column(db.Integer, unique=False, nullable=False, default=0)
    kotlin = db.Column(db.Integer, unique=False, nullable=False, default=0)
    abap = db.Column(db.Integer, unique=False, nullable=False, default=0)





