"""add not null

Revision ID: a708bb82de39
Revises: f84458600a8e
Create Date: 2023-11-02 21:32:28.225102

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a708bb82de39'
down_revision: Union[str, None] = 'f84458600a8e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('contacts', 'student_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('contacts', 'student_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
