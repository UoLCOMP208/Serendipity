"""empty message

Revision ID: 631fdd409aa3
Revises: 3979b3ebce03
Create Date: 2023-02-27 23:32:08.143587

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '631fdd409aa3'
down_revision = '3979b3ebce03'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cms_user', sa.Column('_password', sa.String(length=100), nullable=False))
    op.drop_column('cms_user', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cms_user', sa.Column('password', mysql.VARCHAR(length=100), nullable=False))
    op.drop_column('cms_user', '_password')
    # ### end Alembic commands ###
