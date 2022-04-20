import subprocess

def pip_install(packageName):
    subprocess.call(["pip", "install", packageName])