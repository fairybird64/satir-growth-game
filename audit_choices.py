import re
with open('satir-growth-game-v30.html', 'r', encoding='utf-8') as f:
    content = f.read()
# Find all choice arrays in OPENING_VARIANTS and SCENES
# Look for sc.choices = [ or choices: [ blocks
results = []
# Pattern: find choices arrays
pattern = r'(choices\s*[=:]\s*\[)(.*?)(\])'
matches = list(re.finditer(pattern, content, re.DOTALL))
for m in matches:
    choices_text = m.group(2)
    # Count items by counting 'text:' or '{ text'
    count = choices_text.count('text:')
    if count < 3:
        line_no = content[:m.start()].count('\n') + 1
        context = content[max(0,m.start()-150):m.start()+200]
        results.append({
            'line': line_no,
            'count': count,
            'context': context.strip()
        })
print(f"Scenes with fewer than 3 choices: {len(results)}\n")
for r in results:
    print(f"Line {r['line']}: {r['count']} choices")
    print(r['context'][:300])
    print("---")
with open('choices_audit.txt', 'w', encoding='utf-8') as f:
    for r in results:
        f.write(f"Line {r['line']}: {r['count']} choices\n")
        f.write(r['context'][:300] + "\n---\n")
print("Saved: choices_audit.txt")
