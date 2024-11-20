import sqlalchemy
from sqlalchemy.util.preloaded import orm

from .db_session import SqlAlchemyBase


class Nature(SqlAlchemyBase):
    __tablename__ = 'nature_reserves'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    id_region = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("regions.id"))
    title = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    year_f = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    square = sqlalchemy.Column(sqlalchemy.Text, nullable=True)

    nature = orm.relationship('Region')