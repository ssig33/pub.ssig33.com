"""Add webmentions count

Revision ID: 69ce9fbdc483
Revises: 1647cef23e9b
Create Date: 2022-07-14 15:35:01.716133

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = '69ce9fbdc483'
down_revision = '1647cef23e9b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('outbox', sa.Column('webmentions_count', sa.Integer(), server_default='0', nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('outbox', 'webmentions_count')
    # ### end Alembic commands ###
