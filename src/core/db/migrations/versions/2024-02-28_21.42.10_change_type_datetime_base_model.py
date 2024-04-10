"""change_type_datetime_base_model

Revision ID: 02fda211f87e
Revises: 08c51fddecef
Create Date: 2024-02-28 21:42:10.403435

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "02fda211f87e"
down_revision = "08c51fddecef"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "admin_token_requests",
        "created_at",
        existing_type=sa.DATE(),
        type_=sa.DateTime(),
        existing_nullable=False,
        existing_server_default=sa.text("CURRENT_TIMESTAMP"),
    )
    op.alter_column(
        "admin_token_requests",
        "updated_at",
        existing_type=sa.DATE(),
        type_=sa.DateTime(),
        existing_nullable=False,
        existing_server_default=sa.text("CURRENT_TIMESTAMP"),
    )
    op.alter_column(
        "admin_users",
        "created_at",
        existing_type=sa.DATE(),
        type_=sa.DateTime(),
        existing_nullable=False,
        existing_server_default=sa.text("CURRENT_TIMESTAMP"),
    )
    op.alter_column(
        "admin_users",
        "updated_at",
        existing_type=sa.DATE(),
        type_=sa.DateTime(),
        existing_nullable=False,
        existing_server_default=sa.text("CURRENT_TIMESTAMP"),
    )
    op.alter_column(
        "categories",
        "created_at",
        existing_type=sa.DATE(),
        type_=sa.DateTime(),
        existing_nullable=False,
        existing_server_default=sa.text("CURRENT_TIMESTAMP"),
    )
    op.alter_column(
        "categories",
        "updated_at",
        existing_type=sa.DATE(),
        type_=sa.DateTime(),
        existing_nullable=False,
        existing_server_default=sa.text("CURRENT_TIMESTAMP"),
    )
    op.alter_column(
        "external_site_users",
        "created_at",
        existing_type=sa.DATE(),
        type_=sa.DateTime(),
        existing_nullable=False,
        existing_server_default=sa.text("CURRENT_TIMESTAMP"),
    )
    op.alter_column(
        "external_site_users",
        "updated_at",
        existing_type=sa.DATE(),
        type_=sa.DateTime(),
        existing_nullable=False,
        existing_server_default=sa.text("CURRENT_TIMESTAMP"),
    )
    op.alter_column(
        "notifications",
        "created_at",
        existing_type=sa.DATE(),
        type_=sa.DateTime(),
        existing_nullable=False,
        existing_server_default=sa.text("CURRENT_TIMESTAMP"),
    )
    op.alter_column(
        "notifications",
        "updated_at",
        existing_type=sa.DATE(),
        type_=sa.DateTime(),
        existing_nullable=False,
        existing_server_default=sa.text("CURRENT_TIMESTAMP"),
    )
    op.alter_column(
        "tasks",
        "created_at",
        existing_type=sa.DATE(),
        type_=sa.DateTime(),
        existing_nullable=False,
        existing_server_default=sa.text("CURRENT_TIMESTAMP"),
    )
    op.alter_column(
        "tasks",
        "updated_at",
        existing_type=sa.DATE(),
        type_=sa.DateTime(),
        existing_nullable=False,
        existing_server_default=sa.text("CURRENT_TIMESTAMP"),
    )
    op.alter_column(
        "unsubscribe_reason",
        "created_at",
        existing_type=sa.DATE(),
        type_=sa.DateTime(),
        existing_nullable=False,
        existing_server_default=sa.text("CURRENT_TIMESTAMP"),
    )
    op.alter_column(
        "unsubscribe_reason",
        "updated_at",
        existing_type=sa.DATE(),
        type_=sa.DateTime(),
        existing_nullable=False,
        existing_server_default=sa.text("CURRENT_TIMESTAMP"),
    )
    op.alter_column(
        "users",
        "created_at",
        existing_type=sa.DATE(),
        type_=sa.DateTime(),
        existing_nullable=False,
        existing_server_default=sa.text("CURRENT_TIMESTAMP"),
    )
    op.alter_column(
        "users",
        "updated_at",
        existing_type=sa.DATE(),
        type_=sa.DateTime(),
        existing_nullable=False,
        existing_server_default=sa.text("CURRENT_TIMESTAMP"),
    )
    op.alter_column(
        "users_categories",
        "created_at",
        existing_type=sa.DATE(),
        type_=sa.DateTime(),
        existing_nullable=False,
        existing_server_default=sa.text("CURRENT_TIMESTAMP"),
    )
    op.alter_column(
        "users_categories",
        "updated_at",
        existing_type=sa.DATE(),
        type_=sa.DateTime(),
        existing_nullable=False,
        existing_server_default=sa.text("CURRENT_TIMESTAMP"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "users_categories",
        "updated_at",
        existing_type=sa.DateTime(),
        type_=sa.DATE(),
        existing_nullable=False,
        existing_server_default=sa.text("CURRENT_TIMESTAMP"),
    )
    op.alter_column(
        "users_categories",
        "created_at",
        existing_type=sa.DateTime(),
        type_=sa.DATE(),
        existing_nullable=False,
        existing_server_default=sa.text("CURRENT_TIMESTAMP"),
    )
    op.alter_column(
        "users",
        "updated_at",
        existing_type=sa.DateTime(),
        type_=sa.DATE(),
        existing_nullable=False,
        existing_server_default=sa.text("CURRENT_TIMESTAMP"),
    )
    op.alter_column(
        "users",
        "created_at",
        existing_type=sa.DateTime(),
        type_=sa.DATE(),
        existing_nullable=False,
        existing_server_default=sa.text("CURRENT_TIMESTAMP"),
    )
    op.alter_column(
        "unsubscribe_reason",
        "updated_at",
        existing_type=sa.DateTime(),
        type_=sa.DATE(),
        existing_nullable=False,
        existing_server_default=sa.text("CURRENT_TIMESTAMP"),
    )
    op.alter_column(
        "unsubscribe_reason",
        "created_at",
        existing_type=sa.DateTime(),
        type_=sa.DATE(),
        existing_nullable=False,
        existing_server_default=sa.text("CURRENT_TIMESTAMP"),
    )
    op.alter_column(
        "tasks",
        "updated_at",
        existing_type=sa.DateTime(),
        type_=sa.DATE(),
        existing_nullable=False,
        existing_server_default=sa.text("CURRENT_TIMESTAMP"),
    )
    op.alter_column(
        "tasks",
        "created_at",
        existing_type=sa.DateTime(),
        type_=sa.DATE(),
        existing_nullable=False,
        existing_server_default=sa.text("CURRENT_TIMESTAMP"),
    )
    op.alter_column(
        "notifications",
        "updated_at",
        existing_type=sa.DateTime(),
        type_=sa.DATE(),
        existing_nullable=False,
        existing_server_default=sa.text("CURRENT_TIMESTAMP"),
    )
    op.alter_column(
        "notifications",
        "created_at",
        existing_type=sa.DateTime(),
        type_=sa.DATE(),
        existing_nullable=False,
        existing_server_default=sa.text("CURRENT_TIMESTAMP"),
    )
    op.alter_column(
        "external_site_users",
        "updated_at",
        existing_type=sa.DateTime(),
        type_=sa.DATE(),
        existing_nullable=False,
        existing_server_default=sa.text("CURRENT_TIMESTAMP"),
    )
    op.alter_column(
        "external_site_users",
        "created_at",
        existing_type=sa.DateTime(),
        type_=sa.DATE(),
        existing_nullable=False,
        existing_server_default=sa.text("CURRENT_TIMESTAMP"),
    )
    op.alter_column(
        "categories",
        "updated_at",
        existing_type=sa.DateTime(),
        type_=sa.DATE(),
        existing_nullable=False,
        existing_server_default=sa.text("CURRENT_TIMESTAMP"),
    )
    op.alter_column(
        "categories",
        "created_at",
        existing_type=sa.DateTime(),
        type_=sa.DATE(),
        existing_nullable=False,
        existing_server_default=sa.text("CURRENT_TIMESTAMP"),
    )
    op.alter_column(
        "admin_users",
        "updated_at",
        existing_type=sa.DateTime(),
        type_=sa.DATE(),
        existing_nullable=False,
        existing_server_default=sa.text("CURRENT_TIMESTAMP"),
    )
    op.alter_column(
        "admin_users",
        "created_at",
        existing_type=sa.DateTime(),
        type_=sa.DATE(),
        existing_nullable=False,
        existing_server_default=sa.text("CURRENT_TIMESTAMP"),
    )
    op.alter_column(
        "admin_token_requests",
        "updated_at",
        existing_type=sa.DateTime(),
        type_=sa.DATE(),
        existing_nullable=False,
        existing_server_default=sa.text("CURRENT_TIMESTAMP"),
    )
    op.alter_column(
        "admin_token_requests",
        "created_at",
        existing_type=sa.DateTime(),
        type_=sa.DATE(),
        existing_nullable=False,
        existing_server_default=sa.text("CURRENT_TIMESTAMP"),
    )
    # ### end Alembic commands ###
