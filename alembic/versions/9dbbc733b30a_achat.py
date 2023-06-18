"""Achat

Revision ID: 9dbbc733b30a
Revises: 27c6b9f1d559
Create Date: 2023-06-18 10:30:04.534044

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9dbbc733b30a'
down_revision = '27c6b9f1d559'
branch_labels = None
depends_on = None


def upgrade() -> None:
    achat = sa.table("Achat",sa.column("id_achat", sa.Integer),sa.column("nombre_enfant_client", sa.Integer), sa.column("id_csp", sa.Integer), sa.column("id_collecte", sa.Integer), sa.column("total_achat", sa.DECIMAL), sa.column("date_achat", sa.TIMESTAMP))
    op.create_table('Achat', sa.Column('id_achat', sa.Integer, primary_key=True), sa.Column('nombre_enfant_client', sa.Integer), sa.column('id_csp', sa.Integer), sa.column('id_collecte', sa.Integer), sa.column('total_achat', sa.DECIMAL))
    #op.bulk_insert(achat, [{"id_achat":1, "nombre_enfant_client":5, "id_csp" :4}])

def downgrade() -> None:
    op.drop_table('Achat')