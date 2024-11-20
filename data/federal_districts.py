import sqlalchemy
from sqlalchemy.util.preloaded import orm
from .db_session import SqlAlchemyBase


class Federal(SqlAlchemyBase):
    __tablename__ = 'federal_districts'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    reduction = sqlalchemy.Column(sqlalchemy.Text, nullable=True)

    regions = orm.relationship("Region", back_populates='federal')