"""Collecte

Revision ID: 943e151fa372
Revises: 9dbbc733b30a
Create Date: 2023-06-18 10:56:14.785041

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '943e151fa372'
down_revision = '9dbbc733b30a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    collecte = sa.table("Collecte",sa.column("id_categorie", sa.Integer),sa.column("nom_categorie", sa.String))
    op.create_table('Collecte', sa.Column('id_categorie', sa.Integer, primary_key=True), sa.Column('nom_categorie', sa.String(100)))
    op.bulk_insert(collecte, [{"id_categorie":1, "nom_categorie":"Ouvriers"},{"id_categorie":2, "nom_categorie":"Employés"}])

def downgrade() -> None:
    op.drop_table('CSP')