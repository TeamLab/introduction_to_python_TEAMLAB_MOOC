@ECHO OFF

set BACKEND_ACCESS_KEY=AKIAQWZD6A6Y5ZVOHSJR
set BACKEND_SECRET_KEY=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

set tmp="%1"
if "%tmp:"=.%"==".." (
    echo "Please give hash key as argument."
) else (
    backend.ai run --exec "python test.py factorial_calculator.py %tmp%" python3 test.py factorial_calculator.py
)
