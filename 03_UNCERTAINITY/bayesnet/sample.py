import random
from collections import Counter

from model import model

# Get CPDs
cpd_rain = model.get_cpds("Rain")
cpd_maintenance = model.get_cpds("Maintenance")
cpd_train = model.get_cpds("Train")
cpd_appointment = model.get_cpds("Appointment")


def weighted_choice(states, probabilities):
    """
    Randomly choose one state based on probabilities.
    """
    return random.choices(states, weights=probabilities)[0]


def generate_sample():

    sample = {}

    # -------------------------
    # Sample Rain
    # -------------------------
    rain_states = cpd_rain.state_names["Rain"]
    rain_probs = cpd_rain.values

    sample["Rain"] = weighted_choice(
        rain_states,
        rain_probs
    )

    # -------------------------
    # Sample Maintenance | Rain
    # -------------------------
    maintenance_states = cpd_maintenance.state_names["Maintenance"]

    maintenance_probs = [
        cpd_maintenance.get_value(
            Maintenance=state,
            Rain=sample["Rain"]
        )
        for state in maintenance_states
    ]

    sample["Maintenance"] = weighted_choice(
        maintenance_states,
        maintenance_probs
    )

    # -------------------------
    # Sample Train | Rain, Maintenance
    # -------------------------
    train_states = cpd_train.state_names["Train"]

    train_probs = [
        cpd_train.get_value(
            Train=state,
            Rain=sample["Rain"],
            Maintenance=sample["Maintenance"]
        )
        for state in train_states
    ]

    sample["Train"] = weighted_choice(
        train_states,
        train_probs
    )

    # -------------------------
    # Sample Appointment | Train
    # -------------------------
    appointment_states = cpd_appointment.state_names["Appointment"]

    appointment_probs = [
        cpd_appointment.get_value(
            Appointment=state,
            Train=sample["Train"]
        )
        for state in appointment_states
    ]

    sample["Appointment"] = weighted_choice(
        appointment_states,
        appointment_probs
    )

    return sample


# -----------------------------------
# Rejection Sampling
# P(Appointment | Train = delayed)
# -----------------------------------

N = 10000
data = []

for _ in range(N):

    sample = generate_sample()

    if sample["Train"] == "delayed":
        data.append(sample["Appointment"])

print(Counter(data))
