import sys
import json
import gzip
import re
import os

def process_file(file_path):
    texts = []
    with gzip.open(file_path, 'rt', encoding='utf8') as input:
        for line in input:
            text = json.loads(line)['text']
            if not text.startswith("RT"):
                texts.append(text)

    return texts

directory = r"/Users/jessedanoesastro/tweets13-23/2022"  

texts = []

for file in os.listdir(directory):
    if file.endswith(".gz"):
        file_path = os.path.join(directory, file)
        texts.extend(process_file(file_path))

total_count = len(texts)

# Count occurrences of politeness markers
politeness_markers_count = 0
for text in texts:
    if re.search(r"\b(alstublieft|dankuwel)\b", text, flags=re.IGNORECASE):
        politeness_markers_count += 1

# Calculate ratio of tweets with politeness markers
ratio_politeness_markers = politeness_markers_count / total_count
ratio_no_politeness_markers = 1 - ratio_politeness_markers

print(f"Total count of tweets: {total_count}")
print(f"Count of tweets containing politeness markers 'alstublieft' or 'dankuwel': {politeness_markers_count}")
print(f"Ratio of tweets with politeness markers: {ratio_politeness_markers:.2%}")
print(f"Ratio of tweets without politeness markers: {ratio_no_politeness_markers:.2%}")
