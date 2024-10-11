"""Changed to treasure_type

Revision ID: 3088b38a9750
Revises: f2faafa037f6
Create Date: 2024-10-09 15:02:15.962584

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '3088b38a9750'
down_revision: Union[str, None] = 'f2faafa037f6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_rider_id', table_name='riders')
    op.create_index(op.f('ix_riders_id'), 'riders', ['id'], unique=False)
    op.add_column('treasures', sa.Column('treasure_type', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    op.drop_column('treasures', 'type')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('treasures', sa.Column('type', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('treasures', 'treasure_type')
    op.drop_index(op.f('ix_riders_id'), table_name='riders')
    op.create_index('ix_rider_id', 'riders', ['id'], unique=False)
    # ### end Alembic commands ###
