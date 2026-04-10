from pathlib import Path
from typing import Final

_ROOT_DIRECTORY: Final[str] = str(Path(__file__).parent)

__version__ = "0.1.0"
__all__ = ["_ROOT_DIRECTORY"]
