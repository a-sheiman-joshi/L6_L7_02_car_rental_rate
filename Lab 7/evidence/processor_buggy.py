def sanitize_license_plate(plate):
    plate = plate.strip()
    for ch in ['-', ' ', '_', '#']:
        plate = plate.replace(ch, '')
    return plate.upper()

def parse_trip_mileage(mileage_csv):
    parts = mileage_csv.split(',')
    return [float(m) for m in parts]

def format_rental_invoice(record):
    parts = record.split(':')
    driver = parts[0].strip()
    days = int(parts[1])
    category = parts[2].strip()
    daily_rate = 50.0 if category.lower() == "suv" else 30.0
    total = days * daily_rate
    return f"Driver {driver} booked {category} for {days} days: Total ${total:.2f}"
