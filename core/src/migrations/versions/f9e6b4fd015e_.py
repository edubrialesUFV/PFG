"""empty message

Revision ID: f9e6b4fd015e
Revises: 11ea849aba1c
Create Date: 2023-06-28 23:57:46.897344

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9e6b4fd015e'
down_revision = '11ea849aba1c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('code',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('leng', sa.Enum('Python', 'C', 'Java', name='leng'), nullable=False),
    sa.Column('usuario_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('code')
    # ### end Alembic commands ###