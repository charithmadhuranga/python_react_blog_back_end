"""empty message

Revision ID: dd6bd8d02abe
Revises: b71115992c0b
Create Date: 2017-04-07 12:11:56.968044

"""

# revision identifiers, used by Alembic.
revision = 'dd6bd8d02abe'
down_revision = 'b71115992c0b'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('reply_to_comment_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comments', 'reply_to_comment_id')
    # ### end Alembic commands ###
