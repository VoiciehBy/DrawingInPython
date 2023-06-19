from subprocess import call as subprocess_call


def pip_install(packageName):
    subprocess_call(["pip", "install", packageName])
