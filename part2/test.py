import os, subprocess

# Settings
TEST_DIR = "/tests"     # Directory with out program
CODE_FILE ="main.c"     # Our C code
COMPILER_TIMEOUT = 10.0 # Compiler timout (seconds)
RUN_TIMEOUT = 10.0      # Run timout (seconds)
 
# Create absolute pahts
code_path = os.path.join(TEST_DIR, CODE_FILE)
app_path = os.path.join(TEST_DIR, "app")

# Compile the program
print("Building...")
try:
    ret = subprocess.run(["gcc", code_path, "-o", app_path],
                            stdout=subprocess.PIPE, # Capture stdout stderr to our return variable.
                            stderr=subprocess.PIPE,
                            timeout=COMPILER_TIMEOUT)
except Exception as e:
    print("ERROR: Compilation failed.", str(e))
    exit(1)

# Parse output
output = ret.stdout.decode("utf-8")
print(output)
output = ret.stderr.decode("utf-8")
print(output)

if ret.returncode != 0:
    print("Compilation failed.")
    exit(1)

# Run the compiled program
print("Running...")
try:
    ret = subprocess.run([app_path],
                            stdout=subprocess.PIPE, 
                            timeout=COMPILER_TIMEOUT)
except Exception as e:
    print("ERROR: Runtime failed.", str(e))
    exit(1)

# Parse output
output = ret.stdout.decode("utf-8")
print("Output: ", output)

# All tests passed! Exit gracefully
print("All tests pasted!")
exit(0)