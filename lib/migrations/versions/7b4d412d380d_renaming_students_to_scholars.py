"""Renaming students to scholars

Revision ID: 7b4d412d380d
Revises: 791279dd0760
Create Date: 2023-10-30 20:31:47.539810

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b4d412d380d'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
