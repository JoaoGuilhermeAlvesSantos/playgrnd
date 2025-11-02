import json
import itertools

read_chunk_size = 1

input_path = "data/input.jsonl"
output_path = "data/output_2.jsonl"

with open(input_path, "r", encoding="utf-8") as f_in, open(output_path, "w", encoding="utf-8") as f_out:
    while True:
        lines = list(itertools.islice(f_in, read_chunk_size))
        if not lines:
            break
        
        for line in lines:
            try:
                item = json.loads(line)
                if item[1] == 1:  # filter
                    f_out.write(line)
            except Exception as e:
                print(f"Error: {e}")
