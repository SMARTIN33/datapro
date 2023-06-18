"""Jeux de donnnés

Revision ID: 788190a6b1d9
Revises: 
Create Date: 2023-06-18 09:37:38.566865

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '788190a6b1d9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    produit = sa.table("Produit",sa.column("id", sa.Integer),sa.column("nom_produit", sa.String))
    op.create_table('Produit', sa.Column('id', sa.Integer, primary_key=True), sa.Column('nom_produit', sa.String(100)))
    op.bulk_insert(produit, [{"id":1, "nom_produit":"Mutimédia"},{"id":2, "nom_produit":"Alimentaire"}])

def downgrade() -> None:
    op.drop_table('Produit')

