# Function that generates coordinates in n-dimensional space
def generate_coordinates(*, current: int, max: int, dimensions: int) -> tuple[float, ...]:
    # Calculate granularity to evenly distribute points across the dimensions
    granularity = max + 1  # Minimum granularity to span the frames
    coordinates: list[float] = []
    # Spread the current frame across dimensions more evenly
    for i in range(dimensions):
        step_size = i / dimensions  # Spread across dimensions
        value = (current + step_size) % granularity  # Use step size for smoother distribution
        normalized_value = value / max  # Normalize the result to [0, 1]
        coordinates.append(normalized_value)

    return tuple(coordinates)

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

    def __init__(self):
        self.dimensions = 3

    @classmethod
    def IS_CHANGED(s, current, max, dimensions):
        # This gets called when dimensions changes in UI
        s.update_dimensions(dimensions)
        return dimensions

    @classmethod
    def update_dimensions(s, dimensions):
        # Update return types based on dimensions
        s.RETURN_TYPES = tuple("FLOAT" for _ in range(dimensions))
        s.RETURN_NAMES = tuple(f"dim_{i+1}" for i in range(dimensions))

    # Initialize with default dimensions
    RETURN_TYPES = tuple("FLOAT" for _ in range(3))
    RETURN_NAMES = tuple(f"dim_{i+1}" for i in range(3))
    FUNCTION = "process"

    def process(self, current, max, dimensions):
        self.__class__.update_dimensions(dimensions)
        coordinates = generate_coordinates(current=current, max=max, dimensions=dimensions)
        return coordinates  # Return the tuple directly to unpack it into separate outputs
