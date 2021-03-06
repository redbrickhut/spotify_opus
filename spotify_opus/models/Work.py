from sqlalchemy import ForeignKey

from spotify_opus import db
from spotify_opus.models.Performance import Performance


class Work(db.Model):
    __tablename__ = "works"

    work_id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(), nullable=False)
    composer_id = db.Column(
        db.Integer, ForeignKey("composers.composer_id"
                               ""), nullable=False)

    catalog_no = db.Column(db.String(), nullable=True)
    opus_no = db.Column(db.String(), nullable=True)
    date_written = db.Column(db.Date, nullable=True)
    more_info = db.Column(db.String(), nullable=True)
    performances = db.relationship(Performance, backref="work")

    def __init__(self):
        self.album = None
        self.composer = None

    def __repr__(self):
        return f"<Work: {self.composer.name}: {self.name}>"

    def __eq__(self, other):

        if not isinstance(other, Work):
            return False
        else:

            return self.composer_id == other.composer_id and \
                   self.opus_no == other.opus_no and \
                   self.catalog_no == other.catalog_no

    def __hash__(self):

        return hash((self.composer_id, self.opus_no, self.catalog_no))
