"""Adding devise to destination

Revision ID: 24aaaf9a928e
Revises: 34ca3cc9a91d
Create Date: 2022-10-18 22:09:49.187275

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24aaaf9a928e'
down_revision = '34ca3cc9a91d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('destination', sa.Column('devise', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('destination', 'devise')
    # ### end Alembic commands ###
