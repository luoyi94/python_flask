"""ly02

Revision ID: 3c23c87d4640
Revises: bc15549f4766
Create Date: 2018-06-09 17:45:45.686716

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c23c87d4640'
down_revision = 'bc15549f4766'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('title02', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('roles', 'title02')
    # ### end Alembic commands ###
