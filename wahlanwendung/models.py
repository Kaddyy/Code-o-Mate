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

   # def __init__(self, pk_sprache, beschreibung, absolutes_erg, relatives_erg, link1, link2, link3):
    #    self.pk_sprache = pk_sprache
     #   self.beschreibung = beschreibung
      #  self.absolutes_erg = absolutes_erg
       # self.relatives_erg = relatives_erg
        #self.link1 = link1
        #self.link2 = link2
        #self.link3 = link3



class sessionergebnis(db.Model):
    __table_args__ = {'extend_existing': True}
    pk_session_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fk_java = db.Column(db.Integer, db.ForeignKey('progr_spr.pk_sprache'), nullable=False, default=0)
    fk_python = db.Column(db.Integer, db.ForeignKey('progr_spr.pk_sprache'), nullable=False, default=0)
    fk_swift = db.Column(db.Integer, db.ForeignKey('progr_spr.pk_sprache'), nullable=False, default=0)
    fk_cplusplus = db.Column(db.Integer, db.ForeignKey('progr_spr.pk_sprache'), nullable=False, default=0)
    fk_csharp = db.Column(db.Integer, db.ForeignKey('progr_spr.pk_sprache'), nullable=False, default=0)
    fk_javascript = db.Column(db.Integer, db.ForeignKey('progr_spr.pk_sprache'), nullable=False, default=0)
    fk_matlab = db.Column(db.Integer, db.ForeignKey('progr_spr.pk_sprache'), nullable=False, default=0)
    fk_go = db.Column(db.Integer, db.ForeignKey('progr_spr.pk_sprache'), nullable=False, default=0)
    fk_htmlcss = db.Column(db.Integer, db.ForeignKey('progr_spr.pk_sprache'), nullable=False, default=0)
    fk_sql = db.Column(db.Integer, db.ForeignKey('progr_spr.pk_sprache'), nullable=False, default=0)
    fk_php = db.Column(db.Integer, db.ForeignKey('progr_spr.pk_sprache'), nullable=False, default=0)
    fk_r = db.Column(db.Integer, db.ForeignKey('progr_spr.pk_sprache'), nullable=False, default=0)
    fk_typescript = db.Column(db.Integer, db.ForeignKey('progr_spr.pk_sprache'), nullable=False, default=0)
    fk_kotlin = db.Column(db.Integer, db.ForeignKey('progr_spr.pk_sprache'), nullable=False, default=0)
    fk_abap = db.Column(db.Integer, db.ForeignKey('progr_spr.pk_sprache'), nullable=False, default=0)





