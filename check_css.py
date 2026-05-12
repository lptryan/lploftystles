import re

file_path = r'd:\devcode\lploftystles\lofty-styles.css'

with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Check brackets
open_braces = content.count('{')
close_braces = content.count('}')
print(f"Open braces: {open_braces}")
print(f"Close braces: {close_braces}")

if open_braces != close_braces:
    print("ERROR: Unbalanced braces!")

# Check comments
open_comments = len(re.findall(r'/\*', content))
close_comments = len(re.findall(r'\*/', content))
print(f"Open comments: {open_comments}")
print(f"Close comments: {close_comments}")

if open_comments != close_comments:
    print("ERROR: Unbalanced comments!")

# Look for suspicious strings
suspicious = re.findall(r'[^\x00-\x7F]', content)
if suspicious:
    print(f"Found {len(suspicious)} non-ASCII characters.")
