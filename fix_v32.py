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
# Fix 2: Depth normalization — แก้ทุกที่ที่ใช้ tuningCount*2+1 (both spacing variants)
import re
# showFinalScore() uses spaces: "const d = Math.min(10, tuningCount*2+1);"
old2a = "const d = Math.min(10, tuningCount*2+1);"
new2a = "const d = Math.min(10, Math.round((tuningCount / Math.max(n, 1)) * 10));"
count2a = c.count(old2a)
if count2a:
    c = c.replace(old2a, new2a)
    print(f"✅ Fix 2a: depth normalization showFinalScore ({count2a}x)")
else:
    print("⚠️ Fix 2a not found")
# showEnd() uses no spaces: "const d=Math.min(10,tuningCount*2+1);"
old2b = "const d=Math.min(10,tuningCount*2+1);"
new2b = "const d=Math.min(10,Math.round((tuningCount/Math.max(n,1))*10));"
count2b = c.count(old2b)
if count2b:
    c = c.replace(old2b, new2b)
    print(f"✅ Fix 2b: depth normalization showEnd ({count2b}x)")
else:
    print("⚠️ Fix 2b not found")
with open('satir-growth-game-v32.html', 'w', encoding='utf-8') as f:
    f.write(c)
print(f"DONE: {len(c):,} bytes")
