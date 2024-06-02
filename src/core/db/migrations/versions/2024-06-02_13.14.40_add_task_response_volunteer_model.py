"""add_task_response_volunteer_model

Revision ID: 03553b3c5019
Revises: 6eb0ef45ad86
Create Date: 2024-06-02 13:14:40.427334

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "03553b3c5019"
down_revision = "6eb0ef45ad86"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "task_response_volunteer",
        sa.Column("task_id", sa.Integer(), nullable=False),
        sa.Column("external_site_user_id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False),
        sa.Column("updated_at", sa.DateTime(), server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False),
        sa.ForeignKeyConstraint(
            ["external_site_user_id"],
            ["external_site_users.id"],
        ),
        sa.ForeignKeyConstraint(
            ["task_id"],
            ["tasks.id"],
        ),
        sa.PrimaryKeyConstraint("task_id", "external_site_user_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("task_response_volunteer")
    # ### end Alembic commands ###
