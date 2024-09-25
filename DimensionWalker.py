import comfy.model_nodes as nodes
from typing import List

# Function that generates coordinates in n-dimensional space
def generate_coordinates(*, current: int, max: int, dimensions: int) -> List[float]:
    # Calculate granularity to evenly distribute points across the dimensions
    granularity = max + 1  # Minimum granularity to span the frames
    coordinates: List[float] = []

    # Spread the current frame across dimensions more evenly
    for i in range(dimensions):
        step_size = i / dimensions  # Spread across dimensions
        value = (current + step_size) % granularity  # Use step size for smoother distribution
        normalized_value = value / max  # Normalize the result to [0, 1]
        coordinates.append(normalized_value)

    return coordinates

# Custom Node definition
class DimensionWalker(nodes.Node):
    @classmethod
    def INPUT_TYPES(s):
      return {"required": {
            "current_frame": int,
            "max_frames": int,
            "dimensions": int
        },}
    RETURN_TYPES = (float,)  # Change depending on how many outputs you need
    FUNCTION = "process"

    HELP_TEXT = "Generates coordinates in n-dimensional space based on current_frame and max_frames."

    def __init__(self):
        super().__init__()

        # Add widget to select the number of dimensions
        self.dimensions = self.addWidget("Dimensions", nodes.Int, default=3)

    def process(self, current_frame, max_frames, dimensions=None):
        if dimensions is None:
            dimensions = self.dimensions.getValue()  # Get number of dimensions from widget

        # Handle cases where dimensions > max_frames
        coords = generate_coordinates(current=current_frame, max=max_frames, dimensions=dimensions)

        # Output each coordinate element (return first coordinate as example)
        return coords[0]

# Register the custom node
nodes.register_node(DimensionWalker, "DimensionWalker")
