export BACKEND_ACCESS_KEY=AKIAQWZD6A6Y5ZVOHSJR
export BACKEND_SECRET_KEY=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
if [ $# -eq 0 ]
then
  echo "Please give hash key as argument."
else
  backend.ai run --exec "python test.py fahrenheit_converter.py $1" python3 test.py fahrenheit_converter.py unit_test_fahrenheit_converter.py
fi
