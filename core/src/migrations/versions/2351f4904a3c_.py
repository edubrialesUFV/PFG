"""empty message

Revision ID: 2351f4904a3c
Revises: 97a7e1a74b80
Create Date: 2023-05-29 21:07:57.341700

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2351f4904a3c'
down_revision = '97a7e1a74b80'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vm', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=mysql.VARCHAR(length=50),
               type_=sa.String(length=100),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vm', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.String(length=100),
               type_=mysql.VARCHAR(length=50),
               existing_nullable=False)

    # ### end Alembic commands ###