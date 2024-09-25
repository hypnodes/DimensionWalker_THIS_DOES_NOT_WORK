import comfy.model_nodes as nodes
from typing import List

# Function that generates coordinates in n-dimensional space
def generate_coordinates(*, current: int, max: int, dimensions: int) -> List[float]:
    assert current <= max, "The current frame cannot be greater than maxFrames."

    scaleFactor = 1 / max
    coordinates: List[float] = []

    for i in range(dimensions):
        value = (current + i * (max / dimensions)) % (max + 1)
        normalized_value = value * scaleFactor
        coordinates.append(normalized_value)

    return coordinates

# Custom Node definition
class DimensionWalker(nodes.Node):
    def __init__(self):
        super().__init__()

        # Inputs for 'current_frame' and 'max_frames'
        self.input("current_frame", nodes.Int)
        self.input("max_frames", nodes.Int)

        # Add widget to select the number of dimensions
        self.dimensions = self.addWidget("Dimensions", nodes.Int, default=3)

        # Dynamically create outputs based on number of dimensions
        self.outputs = []
        for i in range(self.dimensions):
            self.outputs.append(self.addOutput(f"coord_{i}", nodes.Float))

        # Add a widget to display the help link (non-clickable)
        self.help_link = self.addWidget(
            "Help Link", nodes.String, default="https://github.com/yourusername/your-repo", display_only=True
        )

    def process(self):
        # Get the inputs from the node
        current_frame = self.getInput("current_frame")
        max_frames = self.getInput("max_frames")
        dimensions = self.dimensions.getValue()  # Get number of dimensions from widget

        # Generate coordinates using the function
        coords = generate_coordinates(current=current_frame, max=max_frames, dimensions=dimensions)

        # Output each coordinate element to the respective output
        for i in range(dimensions):
            self.setOutput(f"coord_{i}", coords[i])

# Register the custom node
nodes.register_node(DimensionWalker, "DimensionWalker")
