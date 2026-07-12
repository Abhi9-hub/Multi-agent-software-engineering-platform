import subprocess
import sys

class CodeRunner:
    def run(self, file_path):
        try:
            result = subprocess.run(
                [sys.executable, str(file_path)],
                capture_output=True,
                text=True,
                timeout=30
            )

            return {
                "success": result.returncode ==0,
                "stdout": result.stdout,
                "stderr": result.stderr
            }
        except Exception as e:
            return{
                "success":False,
                "stdout": "",
                "stderr": str(e)
            }