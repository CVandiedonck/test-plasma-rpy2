import subprocess
import rpy2
import rpy2.robjects as ro

print("rpy2 :", rpy2.__version__)
print("R    :", ro.r("R.version.string")[0])
print("R_HOME :", subprocess.check_output(["R", "RHOME"], text=True).strip())
print("plink :", subprocess.run(["plink", "--version"], capture_output=True, text=True).stdout.strip())
