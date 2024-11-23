# Function that generates coordinates in n-dimensional space
def generate_coordinates(*, current: int, max: int, dimensions: int) -> tuple[float, ...]:
    # Calculate granularity to evenly distribute points across the dimensions
    granularity = max + 1  # Minimum granularity to span the frames
    coordinates: tuple[float, ...] = tuple()
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

    OUTPUT_NODE = True

    @classmethod
    def IS_CHANGED(s, current, max, dimensions):
        return dimensions

    def RETURN_TYPES(self):
        return ("FLOAT",) * self.dimensions

    FUNCTION = "process"

    def __init__(self):
        self.dimensions = 3  # Default value

    def process(self, current, max, dimensions):
        self.dimensions = dimensions  # Store for RETURN_TYPES
        return generate_coordinates(current=current, max=max, dimensions=dimensions)
