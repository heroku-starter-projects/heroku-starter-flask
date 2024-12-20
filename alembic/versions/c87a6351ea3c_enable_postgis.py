"""Enable PostGIS

Revision ID: c87a6351ea3c
Revises: 2799ac377780
Create Date: 2024-12-20 09:40:12.061279

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "c87a6351ea3c"
down_revision = "2799ac377780"
branch_labels = None
depends_on = None


def upgrade():
    op.execute("CREATE EXTENSION IF NOT EXISTS postgis;")


def downgrade():
    op.execute("DROP EXTENSION IF EXISTS postgis;")
