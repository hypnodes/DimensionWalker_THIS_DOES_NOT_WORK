from .dimension_walker import DimensionWalker
import os
import folder_paths

# Get the directory of the current file
NODE_DIR = os.path.dirname(os.path.realpath(__file__))

# Register the js/ folder as a js path
folder_paths.add_javascript_path("dimension_walker", os.path.join(NODE_DIR, "js"))

NODE_CLASS_MAPPINGS = {
    "Dimension Walker 🌀👣": DimensionWalker,
}

__all__ = ['NODE_CLASS_MAPPINGS']
