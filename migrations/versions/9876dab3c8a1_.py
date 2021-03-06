"""empty message

Revision ID: 9876dab3c8a1
Revises: 3a2c8293219d
Create Date: 2017-07-03 23:26:57.102724

"""

# revision identifiers, used by Alembic.
revision = '9876dab3c8a1'
down_revision = '3a2c8293219d'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('chess', 'chess_board')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('chess', sa.Column('chess_board', mysql.VARCHAR(length=200), nullable=True))
    # ### end Alembic commands ###
