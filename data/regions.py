import sqlalchemy
from sqlalchemy.util.preloaded import orm
from .db_session import SqlAlchemyBase


class Region(SqlAlchemyBase):
    __tablename__ = 'regions'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    id_fd = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("federal_districts.id"))
    title = sqlalchemy.Column(sqlalchemy.Text, nullable=True)

    federal = orm.relationship('Federal')
    region = orm.relationship("City", back_populates='region')
    region_Mv = orm.relationship("Movie", back_populates='region_Mv')