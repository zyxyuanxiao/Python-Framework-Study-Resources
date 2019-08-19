"""empty message

Revision ID: 20470654da08
Revises: 17d3ab4193ed
Create Date: 2018-01-23 15:31:26.904616

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20470654da08'
down_revision = '17d3ab4193ed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('push', sa.Column('describe', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('push', 'describe')
    # ### end Alembic commands ###
