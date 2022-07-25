import json
import hashlib
import gzip
import collections
import tqdm

# break the data into 16 even pieces
new_data = collections.defaultdict(list)
with gzip.open("gender_wgnd2.jsonl.gz", "rb") as f:
	for line in tqdm.tqdm(f.readlines()):
		line = line.strip()
		data = json.loads(line)
		name_hash = hashlib.md5(data["name"].encode("utf-8")).hexdigest()[0]
		new_data[name_hash].append(line)

for k,v in new_data.items():
	with gzip.open(f"gender_wgnd2.{k}.jsonl.gz", "wb") as f:
		for line in v:
			f.write(line+b"\n")
	print("finished",k, "--", len(v), "records")
