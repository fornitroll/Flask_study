"""users table

Revision ID: a8652d576ac2
Revises: 
Create Date: 2021-01-06 19:52:26.341697

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a8652d576ac2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('used',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('password_hash', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_used_email'), 'used', ['email'], unique=True)
    op.create_index(op.f('ix_used_username'), 'used', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_used_username'), table_name='used')
    op.drop_index(op.f('ix_used_email'), table_name='used')
    op.drop_table('used')
    # ### end Alembic commands ###
