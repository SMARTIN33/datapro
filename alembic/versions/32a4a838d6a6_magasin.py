"""Magasin

Revision ID: 32a4a838d6a6
Revises: 788190a6b1d9
Create Date: 2023-06-18 10:16:24.799056

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32a4a838d6a6'
down_revision = '788190a6b1d9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    magasin = sa.table("Magasin",sa.column("id_numero_magasin", sa.Integer),sa.column("nom_magasin", sa.String),sa.column("ville_magasin", sa.String))
    op.create_table('Magasin', sa.Column('id_numero_magasin', sa.Integer, primary_key=True), sa.Column('nom_magasin', sa.String(100)),sa.Column('ville_magasin', sa.String(100)))
    op.bulk_insert(magasin, [{"id_numero_magasin":1, "nom_magasin":"Goldenline & CO","ville_magasin":"Lyon"},{"id_numero_magasin":2, "nom_magasin":"Goldenline & CO","ville_magasin":"Nice"}])

def downgrade() -> None:
    op.drop_table('Magasin')
