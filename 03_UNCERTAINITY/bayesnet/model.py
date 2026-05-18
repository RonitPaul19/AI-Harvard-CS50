from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Create Bayesian Network structure
model = DiscreteBayesianNetwork([
    ("Rain", "Maintenance"),
    ("Rain", "Train"),
    ("Maintenance", "Train"),
    ("Train", "Appointment")
])

# Rain node (prior probabilities)
cpd_rain = TabularCPD(
    variable="Rain",
    variable_card=3,
    values=[[0.7], [0.2], [0.1]],
    state_names={
        "Rain": ["none", "light", "heavy"]
    }
)

# Maintenance node conditional on Rain
cpd_maintenance = TabularCPD(
    variable="Maintenance",
    variable_card=2,
    values=[
        [0.4, 0.2, 0.1],  # yes
        [0.6, 0.8, 0.9]   # no
    ],
    evidence=["Rain"],
    evidence_card=[3],
    state_names={
        "Maintenance": ["yes", "no"],
        "Rain": ["none", "light", "heavy"]
    }
)

# Train node conditional on Rain and Maintenance
cpd_train = TabularCPD(
    variable="Train",
    variable_card=2,
    values=[
        # on time
        [0.8, 0.9, 0.6, 0.7, 0.4, 0.5],

        # delayed
        [0.2, 0.1, 0.4, 0.3, 0.6, 0.5]
    ],
    evidence=["Rain", "Maintenance"],
    evidence_card=[3, 2],
    state_names={
        "Train": ["on time", "delayed"],
        "Rain": ["none", "light", "heavy"],
        "Maintenance": ["yes", "no"]
    }
)

# Appointment node conditional on Train
cpd_appointment = TabularCPD(
    variable="Appointment",
    variable_card=2,
    values=[
        [0.9, 0.6],  # attend
        [0.1, 0.4]   # miss
    ],
    evidence=["Train"],
    evidence_card=[2],
    state_names={
        "Appointment": ["attend", "miss"],
        "Train": ["on time", "delayed"]
    }
)

# Add CPDs to model
model.add_cpds(
    cpd_rain,
    cpd_maintenance,
    cpd_train,
    cpd_appointment
)

# Validate model
print("Model valid:", model.check_model())

# Create inference object
inference = VariableElimination(model)

# Query 1: P(Appointment)
print("\nP(Appointment):")
result1 = inference.query(variables=["Appointment"])
print(result1)

# Query 2: P(Appointment | Rain = heavy)
print("\nP(Appointment | Rain = heavy):")
result2 = inference.query(
    variables=["Appointment"],
    evidence={"Rain": "heavy"}
)
print(result2)

# Query 3: P(Train | Rain = light, Maintenance = no)
print("\nP(Train | Rain = light, Maintenance = no):")
result3 = inference.query(
    variables=["Train"],
    evidence={
        "Rain": "light",
        "Maintenance": "no"
    }
)
print(result3)
