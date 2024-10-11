"""Initial migration

Revision ID: f2faafa037f6
Revises: 
Create Date: 2024-10-09 14:28:13.944640

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'f2faafa037f6'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dragons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('color', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('alignment', sa.Integer(), nullable=False),
    sa.Column('size', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('breath_weapon', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('source', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_dragons_id'), 'dragons', ['id'], unique=False)
    op.create_table('riders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('species', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('dragon_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['dragon_id'], ['dragons.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_riders_id'), 'riders', ['id'], unique=False)
    op.create_table('treasures',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('value', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('dragon_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['dragon_id'], ['dragons.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_treasures_id'), 'treasures', ['id'], unique=False)

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    
    op.drop_index(op.f('ix_treasures_id'), table_name='treasures')
    op.drop_table('treasures')
    op.drop_index(op.f('ix_riders_id'), table_name='riders')
    op.drop_table('riders')
    op.drop_index(op.f('ix_dragons_id'), table_name='dragons')
    op.drop_table('dragons')
    # ### end Alembic commands ###
