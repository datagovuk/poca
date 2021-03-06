"""carpark column rename

Revision ID: ce1e9e57e829
Revises: 8eefc70c0433
Create Date: 2016-05-25 13:28:22.787987

"""

# revision identifiers, used by Alembic.
revision = 'ce1e9e57e829'
down_revision = '8eefc70c0433'

from alembic import op
import sqlalchemy as sa
import geoalchemy2


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('carpark', sa.Column('street', sa.Unicode(), nullable=True))
    op.drop_column('carpark', 'street_1')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('carpark', sa.Column('street_1', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('carpark', 'street')
    ### end Alembic commands ###
