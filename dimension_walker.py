# Function that generates coordinates in n-dimensional space
def generate_coordinates(*, current: int, max: int, dimensions: int) -> tuple[float, ...]:
    coordinates: list[float] = []

    # Get total number of possible states and wrap current frame if needed
    total_states = (max + 1) ** dimensions
    current = current % total_states

    # Treat current frame like a number in base (max+1)
    # and convert it to coordinates in each dimension
    for dim in range(dimensions):
        value = (current // ((max + 1) ** dim)) % (max + 1)
        normalized_value = value / max
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
