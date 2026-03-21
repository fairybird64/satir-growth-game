with open('satir-growth-game-v31.html', 'r', encoding='utf-8') as f:
    c = f.read()
# Fix 1: Graph single-session — guard line drawing
old1 = """    ctx.beginPath();
    let started = false;
    sessions.forEach((s, i) => {
      const v = s[dim.key];
      if (v == null || isNaN(v)) { started = false; return; }
      const px = xOf(i), py = yOf(v);
      if (!started) { ctx.moveTo(px, py); started = true; }
      else ctx.lineTo(px, py);
    });
    ctx.stroke();"""
new1 = """    if (n > 1) {
      ctx.beginPath();
      let started = false;
      sessions.forEach((s, i) => {
        const v = s[dim.key];
        if (v == null || isNaN(v)) { started = false; return; }
        const px = xOf(i), py = yOf(v);
        if (!started) { ctx.moveTo(px, py); started = true; }
        else ctx.lineTo(px, py);
      });
      ctx.stroke();
    }"""
if old1 in c:
    c = c.replace(old1, new1)
    print("✅ Fix 1: single-session line guard")
else:
    print("⚠️ Fix 1 not found")
# Fix 2: Depth normalization — แก้ทุกที่ที่ใช้ tuningCount*2+1
import re
old2 = "const d = Math.min(10, tuningCount*2+1);"
new2 = "const d = Math.min(10, Math.round((tuningCount / Math.max(n, 1)) * 10));"
count2 = c.count(old2)
if count2:
    c = c.replace(old2, new2)
    print(f"✅ Fix 2: depth normalization ({count2}x)")
else:
    print("⚠️ Fix 2 not found")
with open('satir-growth-game-v32.html', 'w', encoding='utf-8') as f:
    f.write(c)
print(f"DONE: {len(c):,} bytes")
