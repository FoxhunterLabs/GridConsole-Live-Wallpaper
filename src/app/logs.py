import random

HEADERS = [
    "PATTERN RECOGNITION",
    "BACKPROPAGATION",
    "ARCHITECTURE MODELING",
    "DATA STREAMING",
    "BATCH PREPARATION",
    "TRAINING",
    "IMAGE PROCESSING",
    "DOWNLOADING MODEL",
]

SUBHEADS = [
    "SETTING UP BATCH GENERATION",
    "ANALYZING PATTERNS WITH CONVOLUTION",
    "EDITING VERTEX POINTS",
    "TESTING TRAINING RESULTS",
    "PREPARING STYLEGAN DATASET",
    "CLUSTERING FEATURES ACROSS THE DATASET",
]

def rand_log_line():
    pkgs = ["torch", "numpy", "opencv-python", "transformers", "kornia", "diffusers", "nvidia-cuda"]
    pkg = random.choice(pkgs)
    ver = f"{random.randint(0,2)}.{random.randint(0,20)}.{random.randint(0,20)}"

    templates = [
        f"Requirement already satisfied: {pkg}=={ver} in /usr/local/lib/python3/dist-packages",
        f"Collecting {pkg}=={ver} (from pypi)",
        f"Downloading {pkg}-{ver}-py3-none-any.whl ({random.randint(12,9000)} kB)",
        f"Installing collected packages: {pkg}",
        f"Successfully installed {pkg}-{ver}",
        "WARNING: Running pip as the 'root' user can result in broken permissions",
    ]
    return random.choice(templates)
