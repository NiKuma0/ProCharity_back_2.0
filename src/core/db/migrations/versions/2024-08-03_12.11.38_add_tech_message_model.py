"""add_tech_message_model

Revision ID: 1277f5f5b2f1
Revises: a58802257c7e
Create Date: 2024-08-03 12:11:38.650140

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "1277f5f5b2f1"
down_revision = "a58802257c7e"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "tech_messages",
        sa.Column("text", sa.String(length=4096), nullable=False),
        sa.Column("was_read", sa.Boolean(), server_default=sa.text("false"), nullable=False),
        sa.Column("is_archived", sa.Boolean(), server_default=sa.text("false"), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("created_at", sa.DateTime(), server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False),
        sa.Column("updated_at", sa.DateTime(), server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("tech_messages")
    # ### end Alembic commands ###
