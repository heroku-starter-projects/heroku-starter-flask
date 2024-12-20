"""Add food_truck table

Revision ID: c3a7534891d0
Revises: c87a6351ea3c
Create Date: 2024-12-20 09:18:22.482172

"""

from alembic import op
import sqlalchemy as sa
import geoalchemy2


# revision identifiers, used by Alembic.
revision = "c3a7534891d0"
down_revision = "c87a6351ea3c"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "food_trucks",
        sa.Column("locationid", sa.Integer(), nullable=False),
        sa.Column("applicant", sa.Text(), nullable=True),
        sa.Column("facility_type", sa.String(length=50), nullable=True),
        sa.Column("location_description", sa.Text(), nullable=True),
        sa.Column("address", sa.Text(), nullable=True),
        sa.Column("blocklot", sa.String(length=20), nullable=True),
        sa.Column("block", sa.String(length=20), nullable=True),
        sa.Column("lot", sa.String(length=20), nullable=True),
        sa.Column("permit", sa.String(length=50), nullable=True),
        sa.Column("status", sa.String(length=50), nullable=True),
        sa.Column("food_items", sa.Text(), nullable=True),
        sa.Column(
            "coordinates",
            geoalchemy2.types.Geometry(
                geometry_type="POINT", from_text="ST_GeomFromEWKT", name="geometry"
            ),
            nullable=True,
        ),
        sa.Column("schedule", sa.Text(), nullable=True),
        sa.Column("dayshours", sa.String(length=100), nullable=True),
        sa.Column("noise_sent", sa.DateTime(), nullable=True),
        sa.Column("approved", sa.DateTime(), nullable=True),
        sa.Column("received", sa.DateTime(), nullable=True),
        sa.Column("prior_permit", sa.Integer(), nullable=True),
        sa.Column("expiration_date", sa.DateTime(), nullable=True),
        sa.Column("location_geo", sa.Text(), nullable=True),
        sa.Column("fire_prevention_districts", sa.Integer(), nullable=True),
        sa.Column("police_districts", sa.Integer(), nullable=True),
        sa.Column("supervisor_districts", sa.Integer(), nullable=True),
        sa.Column("zip_codes", sa.Integer(), nullable=True),
        sa.Column("neighborhoods_old", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("locationid"),
    )
    # Postgis automatically creates it
    # op.create_index(
    #     "idx_food_trucks_coordinates",
    #     "food_trucks",
    #     ["coordinates"],
    #     unique=False,
    #     postgresql_using="gist",
    # )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(
        "idx_food_trucks_coordinates",
        table_name="food_trucks",
        postgresql_using="gist",
    )
    op.drop_table("food_trucks")
    # ### end Alembic commands ###
