import re

with open('text.txt', 'rt') as f:
	text = f.read()

text = re.sub(r'\s+', ' ', text)
m = re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])', text.replace('\n', ' '))

with open('output.txt', 'wt') as f:
	for i in m:
		f.write(i + "\n\n")
