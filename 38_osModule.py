# Dont run this program
import os
os.mkdir("data")

# We can make multiple folder in one command
for i in range(1,100):
    os.mkdir(f"data/Day{i}")

# Read documentary 
# imp os.path,exists
# imp os.listdir