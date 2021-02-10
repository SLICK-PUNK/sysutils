import subprocess
print("Installing pip dependencies.....")
try:
    subprocess.run(["python3", "-m",  "pip", "install", "--upgrade", "pip"])
    subprocess.run(["pip3", "install", "wheel"])
    subprocess.run(["pip3", "install", "colorama"])
except:
    print("whoops something went wrong. Send me a screenshot so I can debug :D")
else:
    print("Installation Finished :D")    
