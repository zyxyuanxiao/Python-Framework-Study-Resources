"""empty message

Revision ID: 57a1c8753851
Revises: cb55a30fe001
Create Date: 2018-01-29 14:16:11.795781

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57a1c8753851'
down_revision = 'cb55a30fe001'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('niub',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('vs', sa.String(length=128), nullable=False),
    sa.Column('victory', sa.String(length=128), nullable=False),
    sa.Column('ping', sa.String(length=128), nullable=False),
    sa.Column('fail', sa.String(length=128), nullable=False),
    sa.Column('victory_code', sa.String(length=128), nullable=False),
    sa.Column('ping_code', sa.String(length=128), nullable=False),
    sa.Column('fail_code', sa.String(length=128), nullable=False),
    sa.Column('let_ball', sa.String(length=128), nullable=False),
    sa.Column('pusher', sa.String(length=128), nullable=False),
    sa.Column('main_push', sa.String(length=128), nullable=False),
    sa.Column('cost', sa.String(length=64), nullable=True),
    sa.Column('describe', sa.Text(), nullable=True),
    sa.Column('cea_time', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('niub')
    # ### end Alembic commands ###
