import unittest
import urllib.parse
import urllib.request
import json
import argparse
import os
import types
import sys


parser = argparse.ArgumentParser(description="Autoscorer")
parser.add_argument("filename", help="File to submit")
parser.add_argument("hash", help="Hash key")

args = parser.parse_args()
if args.hash:
    hashkey = args.hash
if args.filename:
    filename = args.filename


class TestResult(unittest.TextTestResult):
    _previousTestClass = None
    _testRunEntered = False
    _moduleSetUpFailed = False

    def __init__(self, stream=None, descriptions=None, verbosity=1):
        super().__init__(
            stream=stream, descriptions=descriptions, verbosity=verbosity)
        self.tests_run = []

    def getTestsReport(self):
        """Returns the run tests as a list of the form [test_id, result]"""
        return self.tests_run

    def addError(self, test, err):
        """Called when an error has occurred. 'err' is a tuple of values as
        returned by sys.exc_info().
        """
        super().addError(test, err)
        self.errors.append((test, self._exc_info_to_string(err, test)))
        self._mirrorOutput = True
        self.tests_run.append([test.id(), 0])

    def addFailure(self, test, err):
        """Called when an error has occurred. 'err' is a tuple of values as
        returned by sys.exc_info()."""
        super().addFailure(test, err)
        self.failures.append((test, self._exc_info_to_string(err, test)))
        self._mirrorOutput = True
        self.tests_run.append([test.id(), 0])

    def addSuccess(self, test):
        "Called when a test has completed successfully"
        super().addSuccess(test)
        self.tests_run.append([test.id(), 1])


with urllib.request.urlopen('http://datasets.lablup.ai/private/python-tests/unit_test_morsecode.py') as response:
    test_code = response.read()

test_module = types.ModuleType(
    'test_code',
    doc='Test case')

exec(test_code, test_module.__dict__)
sys.modules['test_code'] = test_module

import test_code as tc
loader = unittest.loader.defaultTestLoader
null_stream = open(os.devnull, "w")
test_suite = loader.loadTestsFromModule(tc)
result = unittest.TextTestRunner(
    stream=null_stream, verbosity=2, resultclass=TestResult).run(test_suite)

print("Generating result sheet...")
print("-------------------------------------------------------------------")
print("                 Test Case |  Passed? |   Feedback")
print("-------------------------------------------------------------------")
for c, r in result.tests_run:
    print("{0:s} |  {1:s}  | {2} ".format(
        c.rsplit('.', 1)[1].rjust(26),
        "PASSED" if r == 1 else "FAILED",
        "Good Job".rjust(10) if r == 1 else "Failed".rjust(10)))

# print(json.dumps(result.tests_run))
print("Reading source file...")

file = open(filename, "r")
print("Transferring results to server...")
payload = {
    'hashkey': hashkey,
    'result': result.tests_run,
    'code': file.read()
}
try:
    data = urllib.parse.urlencode(payload)
    data = data.encode('ascii')
    req = urllib.request.Request('http://report.inflearn.com/submit', data)
    with urllib.request.urlopen(req) as response:
        resp = response.read()

    if json.loads(resp)['result'] == 0:
        print("Transfer failed: hash key is already used.")
    else:
        print("Transfer completed.")

except Exception as e:
    print("Error occurred on transferring.", e)
