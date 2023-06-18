"""CSP

Revision ID: 27c6b9f1d559
Revises: 32a4a838d6a6
Create Date: 2023-06-18 10:25:01.169589

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27c6b9f1d559'
down_revision = '32a4a838d6a6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    csp = sa.table("CSP",sa.column("id_categorie", sa.Integer),sa.column("nom_categorie", sa.String))
    op.create_table('CSP', sa.Column('id_categorie', sa.Integer, primary_key=True), sa.Column('nom_categorie', sa.String(100)))
    op.bulk_insert(csp, [{"id_categorie":1, "nom_categorie":"Ouvriers"},{"id_categorie":2, "nom_categorie":"Employés"}])

def downgrade() -> None:
    op.drop_table('CSP')
