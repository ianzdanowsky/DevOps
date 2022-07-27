import os

print(os.getcwd()) # Current Working Dir

print(os.listdir()) # List directories

os.walk(os.getcwd()) # List folder, subfolder and files in all the tree inside the current dir