
import pytest
from car_rental_rate import process_rental_fleet, check_fleet_telematics


def test_normal_economy_rental():
    rentals = [{
        "is_confirmed": True,
        "vehicle_type": "economy",
        "driver_age": 30,
        "days": 2,
        "trip_segments": [100]
    }]
    result = process_rental_fleet(rentals, 10.0)
    assert result == {"total_revenue": 110.0, "status": "STANDARD"}


def test_luxury_rental_young_driver():
    rentals = [{
        "is_confirmed": True,
        "vehicle_type": "luxury",
        "driver_age": 20,
        "days": 2,
        "trip_segments": []
    }]
    result = process_rental_fleet(rentals, 10.0)
    assert result == {"total_revenue": 350.0, "status": "STANDARD"}


def test_suv_rental():
    rentals = [{
        "is_confirmed": True,
        "vehicle_type": "suv",
        "driver_age": 30,
        "days": 1,
        "trip_segments": [350]
    }]
    result = process_rental_fleet(rentals, 10.0)
    assert result["total_revenue"] == 220.0


def test_unconfirmed_rental():
    rentals = [{"is_confirmed": False}]
    result = process_rental_fleet(rentals, 10.0)
    assert result["status"] == "EMPTY_BATCH"


def test_invalid_rentals():
    with pytest.raises(ValueError):
        process_rental_fleet("invalid", 10.0)


def test_negative_admin_fee():
    with pytest.raises(ValueError):
        process_rental_fleet([], -10.0)


def test_invalid_rental_days():
    rentals = [{
        "is_confirmed": True,
        "days": 0
    }]
    result = process_rental_fleet(rentals, 10.0)
    assert result["status"] == "EMPTY_BATCH"


def test_negative_mileage():
    rentals = [{
        "is_confirmed": True,
        "days": 1,
        "trip_segments": [-50]
    }]
    result = process_rental_fleet(rentals, 10.0)
    assert result["status"] == "STANDARD"


def test_young_driver_long_trip():
    rentals = [{
        "is_confirmed": True,
        "vehicle_type": "economy",
        "driver_age": 19,
        "days": 1,
        "trip_segments": [350]
    }]
    result = process_rental_fleet(rentals, 10.0)
    assert result["total_revenue"] == 320.0


def test_high_risk_audit():
    rentals = [
        {"is_confirmed": True, "days": 0}
        for _ in range(5)
    ]
    result = process_rental_fleet(rentals, 10.0)
    assert result["status"] == "HIGH_RISK_AUDIT"


def test_safe_telematics():
    assert check_fleet_telematics([[60, 80, 90]]) == "SAFE"


def test_no_telematics_data():
    assert check_fleet_telematics([]) == "NO_DATA"


def test_ground_vehicle_detection():
    assert check_fleet_telematics([[110, 120]]) == "GROUND_VEHICLE"
