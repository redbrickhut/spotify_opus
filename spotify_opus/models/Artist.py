from sqlalchemy import ForeignKey

from spotify_opus import db
from spotify_opus.models.Composer import Composer
from spotify_opus.models.ContextObject import ContextObject


class Artist(ContextObject):
    __tablename__ = "artists"
    artist_id = db.Column(db.Integer(), ForeignKey(
        "context_objects.context_id"), primary_key=True)
    external_id = db.Column(db.String(), nullable=False)
    composer = db.relationship(
        Composer, backref="artist", uselist=False,
        foreign_keys=[Composer.artist_id],
        lazy="raise")

    __mapper_args__ = {
        "polymorphic_identity": "artist"
    }

    def __repr__(self):
        return f"<Artist: {self.name}>"
