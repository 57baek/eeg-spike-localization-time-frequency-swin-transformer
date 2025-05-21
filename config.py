import os
from dotenv import load_dotenv


load_dotevn()

OUTPUT_DIR = os.getenv("OUTPUT_DIR")

os.makedirs(OUTPUT_DIR, exist_ok=True)
