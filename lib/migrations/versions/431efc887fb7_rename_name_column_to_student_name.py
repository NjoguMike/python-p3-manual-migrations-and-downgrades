"""Rename name_column to student_name

Revision ID: 431efc887fb7
Revises: 7b4d412d380d
Create Date: 2023-10-30 20:44:48.909431

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '431efc887fb7'
down_revision = '7b4d412d380d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'name', new_column_name = 'student_name')


def downgrade() -> None:
    op.alter_column('students', 'student_name', new_column_name = 'name')
