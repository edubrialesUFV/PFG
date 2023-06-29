"""empty message

Revision ID: 11ea849aba1c
Revises: 2351f4904a3c
Create Date: 2023-06-28 23:45:53.226930

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '11ea849aba1c'
down_revision = '2351f4904a3c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vm', schema=None) as batch_op:
        batch_op.add_column(sa.Column('ui', sa.Boolean(), nullable=True))
        batch_op.drop_column('port')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vm', schema=None) as batch_op:
        batch_op.add_column(sa.Column('port', mysql.INTEGER(), autoincrement=False, nullable=True))
        batch_op.drop_column('ui')

    # ### end Alembic commands ###