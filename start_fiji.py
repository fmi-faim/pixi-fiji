import imagej
import sys

print(f"Starting Fiji version {sys.argv[1]}")

ij = imagej.init(f"sc.fiji:fiji:{sys.argv[1]}", mode="interactive")
ij.ui().showUI()
print(ij.getApp().getInfo(True))

script = """
#@output String result

result = "Hello from Groovy!"
"""

result = ij.py.run_script("Groovy", script)
print(result.getOutput("result"))
while ij.ui().isVisible():
    pass
ij.dispose()
