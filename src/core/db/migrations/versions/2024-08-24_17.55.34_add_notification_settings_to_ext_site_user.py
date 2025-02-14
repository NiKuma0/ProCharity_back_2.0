"""Add notification settings to ExternalSiteUser

Revision ID: b155a83b9476
Revises: 1277f5f5b2f1
Create Date: 2024-08-24 17:55:34.695567

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "b155a83b9476"
down_revision = "1277f5f5b2f1"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("external_site_users", sa.Column("has_mailing_new_tasks", sa.Boolean(), nullable=True))
    op.add_column("external_site_users", sa.Column("has_mailing_profile", sa.Boolean(), nullable=True))
    op.add_column("external_site_users", sa.Column("has_mailing_my_tasks", sa.Boolean(), nullable=True))
    op.add_column("external_site_users", sa.Column("has_mailing_procharity", sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("external_site_users", "has_mailing_procharity")
    op.drop_column("external_site_users", "has_mailing_my_tasks")
    op.drop_column("external_site_users", "has_mailing_profile")
    op.drop_column("external_site_users", "has_mailing_new_tasks")
    # ### end Alembic commands ###
