"""Robust input-processing functions for the car-rental Lab 7 assignment."""

import math


INVALID_RECORD = "Invalid rental record"


def sanitize_license_plate(plate):
    """Remove the supported delimiters and uppercase a license plate.

    Non-string input is treated as invalid and returns an empty string.
    """
    if not isinstance(plate, str):
        return ""

    cleaned = plate.strip()
    for delimiter in ("-", " ", "_", "#"):
        cleaned = cleaned.replace(delimiter, "")
    return cleaned.upper()


def parse_trip_mileage(mileage_csv):
    """Parse comma-separated mileages.

    Returns an empty list for empty input or invalid data. Every returned
    mileage is a finite, non-negative float. Invalid tokens reject the
    complete input instead of silently producing a partial result.
    """
    if not isinstance(mileage_csv, str):
        return []

    if not mileage_csv.strip():
        return []

    parts = mileage_csv.split(",")
    mileages = []

    try:
        for part in parts:
            token = part.strip()
            if not token:
                return []

            mileage = float(token)
            if not math.isfinite(mileage) or mileage < 0:
                return []

            mileages.append(mileage)
    except (TypeError, ValueError, OverflowError):
        return []

    return mileages


def format_rental_invoice(record):
    """Format Driver:Days:Category input into an invoice.

    Valid records require a non-empty driver, a positive integer number of
    days, and a non-empty category. SUV rentals retain the original $50/day
    rate; all other categories retain the original $30/day rate.
    """
    if not isinstance(record, str):
        return INVALID_RECORD

    parts = record.split(":")
    if len(parts) != 3:
        return INVALID_RECORD

    driver = parts[0].strip()
    days_text = parts[1].strip()
    category = parts[2].strip()

    if not driver or not days_text or not category:
        return INVALID_RECORD

    try:
        days = int(days_text)
    except (TypeError, ValueError, OverflowError):
        return INVALID_RECORD

    if days <= 0:
        return INVALID_RECORD

    daily_rate = 50.0 if category.lower() == "suv" else 30.0
    total = days * daily_rate
    return f"Driver {driver} booked {category} for {days} days: Total ${total:.2f}"


def main():
    print("==== Running sanitize_license_plate ====")
    raw_plate = input("Enter license plate with delimiters (-, _, #): ")
    clean_plate = sanitize_license_plate(raw_plate)
    print("Sanitized Plate:", clean_plate)

    print("\n==== Running parse_trip_mileage ====")
    csv_input = input("Enter CSV of mileages (e.g. 100.5, 45.2, 80.0): ")
    mileage_list = parse_trip_mileage(csv_input)
    print("Parsed Mileage List:", mileage_list)

    print("\n==== Running format_rental_invoice ====")
    record_input = input("Enter rental record (Driver:Days:Category): ")
    invoice = format_rental_invoice(record_input)
    print("Rental Invoice:", invoice)


if __name__ == "__main__":
    main()
