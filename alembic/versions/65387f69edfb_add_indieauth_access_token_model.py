"""Add IndieAuth access token model

Revision ID: 65387f69edfb
Revises: 192aff8bc1e2
Create Date: 2022-07-10 10:21:23.652014

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = '65387f69edfb'
down_revision = '192aff8bc1e2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('indieauth_access_token',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('indieauth_authorization_request_id', sa.Integer(), nullable=True),
    sa.Column('access_token', sa.String(), nullable=False),
    sa.Column('expires_in', sa.Integer(), nullable=False),
    sa.Column('scope', sa.String(), nullable=False),
    sa.Column('is_revoked', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['indieauth_authorization_request_id'], ['indieauth_authorization_request.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_indieauth_access_token_access_token'), 'indieauth_access_token', ['access_token'], unique=True)
    op.create_index(op.f('ix_indieauth_access_token_id'), 'indieauth_access_token', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_indieauth_access_token_id'), table_name='indieauth_access_token')
    op.drop_index(op.f('ix_indieauth_access_token_access_token'), table_name='indieauth_access_token')
    op.drop_table('indieauth_access_token')
    # ### end Alembic commands ###