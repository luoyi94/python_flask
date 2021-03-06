"""ly03

Revision ID: fe8b73017aa0
Revises: 3c23c87d4640
Create Date: 2018-06-09 17:47:32.455366

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'fe8b73017aa0'
down_revision = '3c23c87d4640'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('roles', 'title02')
    op.drop_column('roles', 'title')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('title', mysql.VARCHAR(length=128), nullable=True))
    op.add_column('roles', sa.Column('title02', mysql.VARCHAR(length=128), nullable=True))
    # ### end Alembic commands ###
