import os
import re
import yaml

cards_dir = '_cards-copy'
for filename in os.listdir(cards_dir):
    if filename.endswith('.md'):
        path = os.path.join(cards_dir, filename)
        with open(path, 'r') as f:
            content = f.read()
        # Extract YAML front matter
        match = re.match(r'---\n(.*?)\n---\n', content, re.DOTALL)
        if match:
            front_matter = yaml.safe_load(match.group(1))
            if 'keywords' in front_matter:
                keywords = front_matter['keywords']
                if not keywords:
                    keywords = []
                elif isinstance(keywords, str):
                    keywords = [k.strip() for k in keywords.split(',')]
                keywords = list(set(k.lower().strip() for k in keywords if k))
                keywords.sort()
                front_matter['keywords'] = keywords
                # Replace front matter in file
                new_front = yaml.dump(front_matter, sort_keys=False)
                new_content = f'---\n{new_front}---\n' + content[match.end():]
                with open(path, 'w') as f:
                    f.write(new_content)
