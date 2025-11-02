import json

block_size = 10_000_000  # 10 MB 
buffer = ""

input_file = "data/input.jsonl"
output_file = "data/output.jsonl"

with open(input_file, "r", encoding="utf-8") as f_in, \
     open(output_file, "w", encoding="utf-8") as f_out:

    while True:
        data = f_in.read(block_size)
        if not data:
            break
        buffer += data
        lines = buffer.split("\n")
        buffer = lines.pop()  # May be incomplete line

        for line in lines:
            line = line.strip()
            if not line:
                continue
            try:
                item = json.loads(line)
            except json.JSONDecodeError:
                continue
            if item[1] == 1: # Filter by 1
                f_out.write(json.dumps(item, ensure_ascii=False) + "\n")

    # process buffer
    if buffer.strip():
        try:
            item = json.loads(buffer)
            if item[1] == 1:
                f_out.write(json.dumps(item, ensure_ascii=False) + "\n")
        except json.JSONDecodeError:
            pass
