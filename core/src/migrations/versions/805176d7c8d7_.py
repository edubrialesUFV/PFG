"""empty message

Revision ID: 805176d7c8d7
Revises: f9e6b4fd015e
Create Date: 2023-06-29 00:02:28.934318

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '805176d7c8d7'
down_revision = 'f9e6b4fd015e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('code', schema=None) as batch_op:
        batch_op.add_column(sa.Column('nombre', sa.String(length=100), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('code', schema=None) as batch_op:
        batch_op.drop_column('nombre')

    # ### end Alembic commands ###
