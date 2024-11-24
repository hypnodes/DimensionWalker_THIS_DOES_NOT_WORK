# Function that generates coordinates in n-dimensional space
def generate_coordinates(*, current: int, max: int, dimensions: int) -> tuple[float, ...]:
    if max <= 1:
        raise ValueError("`max` must be greater than 1 to generate valid coordinates.")
    if dimensions < 1:
        raise ValueError("`dimensions` must be at least 1.")

    coordinates: list[float] = []

    # Get total number of possible states and wrap current frame if needed
    total_states = max ** dimensions
    current = current % total_states  # Ensure `current` wraps around

    # Generate coordinates for each dimension
    for dim in range(dimensions):
        # Calculate the value in the current dimension
        value = (current // (max ** dim)) % max
        normalized_value = value / (max - 1)  # Normalize to [0, 1]
        coordinates.append(normalized_value)

    return tuple(coordinates)
class DimensionWalker:
    """
    A node that generates n-dimensional coordinates between 0-1,
    distributed evenly across frames.
    """
    CATEGORY = "hypnodes"
    FUNCTION = "process"
    OUTPUT_NODE = True  # Allows dynamic outputs

    # Initialize RETURN_TYPES and RETURN_NAMES with defaults for 3 dimensions
    RETURN_TYPES = ("FLOAT", "FLOAT", "FLOAT")  # Default to three outputs
    RETURN_NAMES = ("coord_1", "coord_2", "coord_3")  # Default names for three dimensions

    # Inputs for the node
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "current": ("INT", {"default": 0, "min": 0}),
                "max": ("INT", {"default": 10, "min": 1}),
                "dimensions": ("INT", {"default": 3, "min": 1, "max": 10})
            }
        }

    # Called whenever inputs change in UI
    @classmethod
    def IS_CHANGED(cls, current, max, dimensions):
        cls.RETURN_TYPES = tuple("FLOAT" for _ in range(dimensions))
        cls.RETURN_NAMES = tuple(f"coord_{i+1}" for i in range(dimensions))
        return True  # Indicates outputs have changed

    def process(self, current, max, dimensions):
        # Ensure RETURN_TYPES and RETURN_NAMES are updated
        self.__class__.RETURN_TYPES = tuple("FLOAT" for _ in range(dimensions))
        self.__class__.RETURN_NAMES = tuple(f"coord_{i+1}" for i in range(dimensions))

        # Generate coordinates
        coords = generate_coordinates(current=current, max=max, dimensions=dimensions)

        # Return each coordinate as a separate output
        return tuple(coords)
