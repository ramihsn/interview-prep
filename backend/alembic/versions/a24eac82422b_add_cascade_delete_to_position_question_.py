"""Add cascade delete to Position-Question relationship

Revision ID: a24eac82422b
Revises: b50fdeca22c3
Create Date: 2024-12-17 16:24:36.972437

"""
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = 'a24eac82422b'
down_revision: Union[str, None] = 'b50fdeca22c3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Drop the existing foreign key constraint
    op.drop_constraint('questions_position_id_fkey', 'questions', type_='foreignkey')

    # Add a new foreign key constraint with ON DELETE CASCADE
    op.create_foreign_key(
        "questions_position_id_fkey",  # Constraint name
        "questions",                   # Table with the foreign key
        "positions",                   # Referenced table
        ["position_id"],               # Column in 'questions'
        ["id"],                        # Column in 'positions'
        ondelete="CASCADE"             # Enable ON DELETE CASCADE
    )


def downgrade():
    # Drop the foreign key constraint with ON DELETE CASCADE
    op.drop_constraint('questions_position_id_fkey', 'questions', type_='foreignkey')

    # Recreate the original foreign key without cascade
    op.create_foreign_key(
        "questions_position_id_fkey",
        "questions",
        "positions",
        ["position_id"],
        ["id"]
    )
