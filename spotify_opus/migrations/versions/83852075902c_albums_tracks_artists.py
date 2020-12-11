"""albums tracks artists

Revision ID: 83852075902c
Revises: 8671126c7b86
Create Date: 2020-12-11 14:57:35.337612

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83852075902c'
down_revision = '8671126c7b86'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('albums',
    sa.Column('album_id', sa.Integer(), nullable=False),
    sa.Column('album_type', sa.Enum('single', 'album', 'compilation', name='albumtype'), nullable=False),
    sa.Column('release_date', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['album_id'], ['context_objects.context_id'], ),
    sa.PrimaryKeyConstraint('album_id')
    )
    op.create_table('artists',
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['context_objects.context_id'], ),
    sa.PrimaryKeyConstraint('artist_id')
    )
    op.create_table('tracks',
    sa.Column('track_id', sa.Integer(), nullable=False),
    sa.Column('album_id', sa.Integer(), nullable=False),
    sa.Column('duration_ms', sa.Integer(), nullable=False),
    sa.Column('disc_no', sa.Integer(), nullable=False),
    sa.Column('explicit', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['album_id'], ['albums.album_id'], ),
    sa.ForeignKeyConstraint(['track_id'], ['context_objects.context_id'], ),
    sa.PrimaryKeyConstraint('track_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tracks')
    op.drop_table('artists')
    op.drop_table('albums')
    # ### end Alembic commands ###
