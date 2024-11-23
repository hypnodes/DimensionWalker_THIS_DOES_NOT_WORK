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
                "current": ("INT", {"default": 0, "min": 0}),
                "max": ("INT", {"default": 10, "min": 1}),
                "dimensions": ("INT", {"default": 3, "min": 1, "max": 10})
            },
        }

    # Dynamically create return types based on dimensions
    def RETURN_TYPES(self):
        return ("FLOAT",) * self.dimensions

    FUNCTION = "process"

    def __init__(self):
        self.dimensions = 3  # Default value

    def process(self, current, max, dimensions):
        self.dimensions = dimensions  # Store for RETURN_TYPES
        coords = generate_coordinates(current=current, max=max, dimensions=dimensions)
        return tuple(coords)  # Return all coordinates
