"""
Master Project Execution Script

Author: Chaithanya K
"""

import subprocess

print("Starting Mutual Fund Analytics Pipeline...")

subprocess.run(["python", "recommender.py"])

print("Pipeline Execution Completed Successfully.")