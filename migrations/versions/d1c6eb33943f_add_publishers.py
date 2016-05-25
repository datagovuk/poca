"""Add publishers

Revision ID: d1c6eb33943f
Revises: 900cc0763bda
Create Date: 2016-05-25 12:29:11.035363

"""

# revision identifiers, used by Alembic.
revision = 'd1c6eb33943f'
down_revision = '900cc0763bda'

from alembic import op
import sqlalchemy as sa
import geoalchemy2


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('publisher',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Unicode(), nullable=False),
    sa.Column('title', sa.Unicode(), nullable=True),
    sa.Column('category', sa.Unicode(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_publisher_name'), 'publisher', ['name'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_publisher_name'), table_name='publisher')
    op.drop_table('publisher')
    ### end Alembic commands ###
