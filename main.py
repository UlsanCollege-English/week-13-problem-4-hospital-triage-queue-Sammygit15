def select_patients(patients, k):
    # Edge cases
    if k == 0 or not patients:
        return []

    # Sort patients by (severity, arrival_order)
    sorted_patients = sorted(
        patients,
        key=lambda p: (p["severity"], p["arrival_order"])
    )

    # Take the first k names (or fewer if fewer exist)
    selected = sorted_patients[:k]

    # Return list of names only
    return [p["name"] for p in selected]


if __name__ == "__main__":
    # Optional manual test
    sample_patients = [
        {"name": "Alex", "severity": 3, "arrival_order": 5},
        {"name": "Bella", "severity": 1, "arrival_order": 6},
        {"name": "Chris", "severity": 1, "arrival_order": 2},
    ]
    print(select_patients(sample_patients, 2))  # Expected: ['Chris', 'Bella']
