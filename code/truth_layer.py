# truth_layer.py - Building the Truth Layer of the Framework

# Defining perspectives and biases
truth_layer = {
    "Perspective_A": "Government Narrative",
    "Perspective_B": "Opposition Narrative",
    "Perspective_C": "International Media Perspective",
    "Biases": [
        "Hidden Agendas",
        "Cultural Contexts",
        "Media Spin",
        "Selective Reporting"
    ]
}

# Function to display the Truth Layer
def show_truth_layer(layer):
    print("Truth Layer Analysis:")
    for key, value in layer.items():
        print(f"{key}: {value}")

# Running the Truth Layer
if __name__ == "__main__":
    show_truth_layer(truth_layer)
