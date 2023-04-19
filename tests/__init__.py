import os
from pathlib import Path


os.environ["TEST_PATH"] = str(Path(__file__).parent)
