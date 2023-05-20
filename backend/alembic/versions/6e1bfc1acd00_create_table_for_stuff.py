"""create table for 'stuff'

Revision ID: 6e1bfc1acd00
Revises: 
Create Date: 2023-05-20 11:34:31.245107

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e1bfc1acd00'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "stuff",
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('description', sa.String(200), nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=sa.sql.func.Now()),
        sa.Column('processed_at', sa.DateTime)
    )
    

def downgrade() -> None:
        op.drop_table("stuff")
