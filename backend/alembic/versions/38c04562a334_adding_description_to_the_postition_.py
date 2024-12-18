"""adding description to the postition table

Revision ID: 38c04562a334
Revises: b19dc403e3bc
Create Date: 2024-12-12 15:17:03.913099

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes


# revision identifiers, used by Alembic.
revision: str = '38c04562a334'
down_revision: Union[str, None] = 'b19dc403e3bc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('positions', sa.Column('description', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('positions', 'description')
    # ### end Alembic commands ###
