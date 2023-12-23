import os.path
import subprocess

def test_hello():
	cmd = ["python3", "hello.py"]
	ret = subprocess.run(cmd, stdout=subprocess.PIPE, encoding="UTF-8")
	assert ret.stdout == "Hello!"

def test_info():
	with open("info.txt", "r") as f:
		line = f.readlines()[0].strip()
		tokens = [t.strip() for t in line.split(",")]
		
		slack_id = tokens[-1]
		expected_slack_id = "{} ({})".format(tokens[1], tokens[0])
		assert len(tokens) == 5
		assert slack_id == expected_slack_id