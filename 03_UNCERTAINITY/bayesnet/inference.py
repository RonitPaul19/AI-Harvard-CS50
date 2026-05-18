from model import model
from pgmpy.inference import VariableElimination

# Create inference object
inference = VariableElimination(model)

# Evidence
evidence = {
    "Train": "delayed"
}

# Nodes in the network
nodes = ["Rain", "Maintenance", "Train", "Appointment"]

# Predict probabilities for each node
for node in nodes:

    # If node already given as evidence
    if node in evidence:
        print(f"{node}: {evidence[node]}")

    else:
        print(f"{node}")

        # Query probability distribution
        result = inference.query(
            variables=[node],
            evidence=evidence
        )

        # Print probabilities
        states = result.state_names[node]

        for i, state in enumerate(states):
            probability = result.values[i]
            print(f"    {state}: {probability:.4f}")
