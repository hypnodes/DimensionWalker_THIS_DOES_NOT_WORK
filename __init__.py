from .dimension_walker import DimensionWalker
import os
import folder_paths

# Get the directory of the current file
NODE_DIR = os.path.dirname(os.path.realpath(__file__))

# Register the js/ folder as a js path
WEB_DIRECTORY = os.path.join(NODE_DIR, "js")

NODE_CLASS_MAPPINGS = {
    "DimensionWalker": DimensionWalker
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DimensionWalker": "Dimension Walker 🌀👣"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'WEB_DIRECTORY']
