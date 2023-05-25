"""empty message

Revision ID: d0f3769dffe6
Revises: 6443fec82a4c
Create Date: 2023-05-25 17:38:15.069746

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd0f3769dffe6'
down_revision = '6443fec82a4c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('stuff', 'in_item')


def downgrade() -> None:
    op.rename_table('in_item', 'stuff')
