"""make user name not null

Revision ID: dc61b42759b9
Revises: 23f4273a2757
Create Date: 2026-07-29 01:12:27.675588

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dc61b42759b9'
down_revision: Union[str, Sequence[str], None] = '23f4273a2757'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.alter_column(
        "users",
        "name",
        existing_type=sa.String(length=100),
        nullable=False
    )


def downgrade():
    op.alter_column(
        "users",
        "name",
        existing_type=sa.String(length=100),
        nullable=True
    )
