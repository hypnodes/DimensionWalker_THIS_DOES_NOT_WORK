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
    """
    A node that generates n-dimensional coordinates between 0-1,
    distributed evenly across frames
    """
    CATEGORY = "hypnodes"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "current": ("INT", {"default": 0, "min": 0}),
                "max": ("INT", {"default": 10, "min": 1}),
                "dimensions": ("INT", {"default": 3, "min": 1, "max": 10})
            }
        }

    def RETURN_TYPES(self):
        # Dynamic return types based on dimensions
        return ("FLOAT",) * self.dimensions

    FUNCTION = "process"

    def __init__(self):
        self.dimensions = 3  # Default value

    def process(self, current, max, dimensions):
        self.dimensions = dimensions  # Store for RETURN_TYPES
        coords = []

        # For each dimension, create a different frequency of oscillation
        for i in range(dimensions):
            # Use different frequencies to ensure good coverage
            frequency = (i + 1) / dimensions
            # Calculate the position in this dimension
            value = (current * frequency) % max
            # Normalize to 0-1 range
            normalized_value = value / max
            coords.append(normalized_value)

        return tuple(coords)
