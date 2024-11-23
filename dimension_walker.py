# Function that generates coordinates in n-dimensional space
def generate_coordinates(*, current: int, max: int, dimensions: int) -> list[float]:
    # Calculate granularity to evenly distribute points across the dimensions
    granularity = max + 1  # Minimum granularity to span the frames
    coordinates: list[float] = []

    # Spread the current frame across dimensions more evenly
    for i in range(dimensions):
        step_size = i / dimensions  # Spread across dimensions
        value = (current + step_size) % granularity  # Use step size for smoother distribution
        normalized_value = value / max  # Normalize the result to [0, 1]
        coordinates.append(normalized_value)

    return coordinates

# Custom Node definition
class DimensionWalker:
    CATEGORY = "hypnodes"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "name": ("STRING", {"default": "name"}),
                "default_value": ("FLOAT", {"default": 0.0}),
            },
        }

    # Change return type to tuple of floats
    RETURN_TYPES = ("FLOAT",) * 1  # Adjust the multiplication based on how many coordinates you want to output
    FUNCTION = "process"

    # Remove __init__ as ComfyUI handles widget creation differently
    # def __init__(self): ...

    def process(self, current_frame, max_frames, dimensions):
        # Remove widget reference since we're using input parameters
        coords = generate_coordinates(current=current_frame, max=max_frames, dimensions=dimensions)

        # Return as tuple for ComfyUI
        return (coords[0],)
