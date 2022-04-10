# web crawler for gathering URLs
import os
import subprocess

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get(target_url):
    pre_output = subprocess.getoutput(
        f"waybackurls {target_url}"
    
    )
    print("Wayback Loaded")
    if pre_output != "":
        result = pre_output.split("\n")
        return result

    else:
        return None
