"""rename department

Revision ID: 0d89300e4d8d
Revises: 66ab7325b90b
Create Date: 2025-02-20 09:33:04.347857

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d89300e4d8d'
down_revision = '66ab7325b90b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department', 'departments')
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('departments', 'department')
    # ### end Alembic commands ###
