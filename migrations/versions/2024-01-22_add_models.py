"""add models

Revision ID: 736d62b56fe2
Revises: 
Create Date: 2024-01-22 18:52:56.701344

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '736d62b56fe2'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pipeline',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_pipeline_id'), 'pipeline', ['id'], unique=False)
    op.create_table('step',
    sa.Column('step_id', sa.BigInteger(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('step_parameters', sa.String(), nullable=False),
    sa.Column('pipeline_id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['pipeline_id'], ['pipeline.id'], ),
    sa.PrimaryKeyConstraint('step_id')
    )
    op.create_index(op.f('ix_step_step_id'), 'step', ['step_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_step_step_id'), table_name='step')
    op.drop_table('step')
    op.drop_index(op.f('ix_pipeline_id'), table_name='pipeline')
    op.drop_table('pipeline')
    # ### end Alembic commands ###