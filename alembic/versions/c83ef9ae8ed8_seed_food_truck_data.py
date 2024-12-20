"""Seed food truck data

Revision ID: c83ef9ae8ed8
Revises: c3a7534891d0
Create Date: 2024-12-20 09:46:09.966801

"""

from alembic import op
import sqlalchemy as sa
import csv
from sqlalchemy.sql import text

# revision identifiers, used by Alembic.
revision = "c83ef9ae8ed8"
down_revision = "c3a7534891d0"
branch_labels = None
depends_on = None


def upgrade():
    # Path to the CSV file
    csv_path = "./alembic/seed/food-truck-data.csv"

    # Open and read the CSV file
    with open(csv_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        conn = op.get_bind()

        # Iterate over rows and insert into the database
        for row in reader:
            # Convert latitude and longitude into a PostGIS POINT
            latitude = float(row["Latitude"])
            longitude = float(row["Longitude"])
            coordinates = f"SRID=4326;POINT({longitude} {latitude})"

            # Prepare and execute the SQL statement
            conn.execute(
                text(
                    """
                    INSERT INTO food_trucks (
                        locationid, applicant, facility_type, location_description,
                        address, blocklot, block, lot, permit, status, food_items,
                        coordinates, schedule, dayshours, noise_sent, approved,
                        received, prior_permit, expiration_date, fire_prevention_districts,
                        police_districts, supervisor_districts, zip_codes, neighborhoods_old
                    )
                    VALUES (
                        :locationid, :applicant, :facility_type, :location_description,
                        :address, :blocklot, :block, :lot, :permit, :status, :food_items,
                        ST_GeomFromText(:coordinates), :schedule, :dayshours, :noise_sent, :approved,
                        :received, :prior_permit, :expiration_date, :fire_prevention_districts,
                        :police_districts, :supervisor_districts, :zip_codes, :neighborhoods_old
                    )
                """
                ),
                {
                    "locationid": int(row["locationid"]),
                    "applicant": row["Applicant"],
                    "facility_type": row["FacilityType"],
                    "location_description": row["LocationDescription"],
                    "address": row["Address"],
                    "blocklot": row["blocklot"],
                    "block": row["block"],
                    "lot": row["lot"],
                    "permit": row["permit"],
                    "status": row["Status"],
                    "food_items": row["FoodItems"],
                    "coordinates": coordinates,
                    "schedule": row["Schedule"],
                    "dayshours": row["dayshours"],
                    "noise_sent": None if row["NOISent"] == "" else row["NOISent"],
                    "approved": None if row["Approved"] == "" else row["Approved"],
                    "received": None if row["Received"] == "" else row["Received"],
                    "prior_permit": (
                        int(row["PriorPermit"])
                        if row["PriorPermit"].isdigit()
                        else None
                    ),
                    "expiration_date": (
                        None if row["ExpirationDate"] == "" else row["ExpirationDate"]
                    ),
                    "fire_prevention_districts": (
                        int(row["Fire Prevention Districts"])
                        if row["Fire Prevention Districts"].isdigit()
                        else None
                    ),
                    "police_districts": (
                        int(row["Police Districts"])
                        if row["Police Districts"].isdigit()
                        else None
                    ),
                    "supervisor_districts": (
                        int(row["Supervisor Districts"])
                        if row["Supervisor Districts"].isdigit()
                        else None
                    ),
                    "zip_codes": (
                        int(row["Zip Codes"]) if row["Zip Codes"].isdigit() else None
                    ),
                    "neighborhoods_old": (
                        int(row["Neighborhoods (old)"])
                        if row["Neighborhoods (old)"].isdigit()
                        else None
                    ),
                },
            )


def downgrade():
    # Optionally delete all rows inserted during the upgrade
    op.execute("DELETE FROM food_trucks")
