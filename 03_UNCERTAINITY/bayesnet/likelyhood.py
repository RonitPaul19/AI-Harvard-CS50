import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

from model import model
from pgmpy.inference import VariableElimination

# Create inference object
inference = VariableElimination(model)

# Calculate probability of:
# Rain = none
# Maintenance = no
# Train = on time
# Appointment = attend

result = inference.query(
    variables=["Appointment"],
    evidence={
        "Rain": "none",
        "Maintenance": "no",
        "Train": "on time"
    }
)

# Probability of Appointment = attend
probability = result.values[0]

print(probability)
