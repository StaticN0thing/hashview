"""empty message

Revision ID: cd03cec8ab09
Revises: 8f8e3c12623c
Create Date: 2021-10-23 14:46:52.635792

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd03cec8ab09'
down_revision = '8f8e3c12623c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hashfiles', sa.Column('owner_id', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('hashfiles', 'owner_id')
    # ### end Alembic commands ###
