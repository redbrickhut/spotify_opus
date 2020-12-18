"""missing attributes added

Revision ID: ee5879c3a9f8
Revises: 6cf53d93d96b
Create Date: 2020-12-18 12:01:00.617214

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ee5879c3a9f8'
down_revision = '6cf53d93d96b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('composers', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('composers', schema=None) as batch_op:
        batch_op.drop_column('name')

    # ### end Alembic commands ###
