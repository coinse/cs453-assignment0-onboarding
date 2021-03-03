import os.path
import subprocess

def test_hello():
	cmd = ["python3", "hello.py"]
	ret = subprocess.run(cmd, stdout=subprocess.PIPE, text=True)
	assert ret.stdout == "Hello!"

def test_info():
	with open("info.txt", "r") as f:
		line = f.readlines()[0].strip()
		tokens = [t.strip() for t in line.split(",")]
		
		slack_id = tokens[-1]
		expected_slack_id = "{} ({})".format(tokens[1], tokens[0])
		assert len(tokens) == 5
		assert slack_id == expected_slack_id

def test_honorcode():
	with open("info.txt", "r") as f:
		line = f.readlines()[0].strip()
		tokens = [t.strip() for t in line.split(",")]
		
		honor_code_scan = "{}-honor-code-signed.pdf".format(tokens[0])
		assert os.path.exists(honor_code_scan)