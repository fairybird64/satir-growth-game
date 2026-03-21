with open('satir-growth-game-v30.html', 'r', encoding='utf-8') as f:
    c = f.read()

old = """          {text:'บอกเพื่อนกลุ่มนั้นตรงๆ ด้วยความห่วงใย ว่าเป็นห่วงพวกเขาและบอกว่ามีครูแนะแนวให้คุยได้',type:'good'},
          {text:'ห่างจากกลุ่มนั้นเงียบๆ โดยไม่พูดอะไร',type:'ok'},
        ],
        outcomes:{
          good:"""

new = """          {text:'บอกเพื่อนกลุ่มนั้นตรงๆ ด้วยความห่วงใย ว่าเป็นห่วงพวกเขาและบอกว่ามีครูแนะแนวให้คุยได้',type:'good'},
          {text:'ห่างจากกลุ่มนั้นเงียบๆ โดยไม่พูดอะไร',type:'ok'},
          {text:'เขียนความรู้สึกลงในสมุดว่าเป็นห่วงเพื่อน แต่ยังไม่พร้อมพูดตรงๆ',type:'ok2'},
        ],
        outcomes:{
          good:"""

assert old in c, "ERROR: old string not found in file!"
c2 = c.replace(old, new, 1)
assert c2 != c, "ERROR: no replacement made!"

# Also add ok2 outcome after the ok outcome
old2 = """          ok:{type:'ok',title:'💙 รักษาตัวเองก่อน',text:'มินนาเลือกห่างออกมา บางครั้งการปกป้องตัวเองก็คือสิ่งที่ถูกต้องที่สุด',satir:'**การรักษาขอบเขตของตัวเอง** ก็เป็นการดูแลตัวเองที่สำคัญ — เราไม่สามารถช่วยคนอื่นได้ถ้าเราตัวเองยังไม่ปลอดภัย'},
        },
        chooserNote:'มินนาไม่ต้องช่วยทุกคน"""

new2 = """          ok:{type:'ok',title:'💙 รักษาตัวเองก่อน',text:'มินนาเลือกห่างออกมา บางครั้งการปกป้องตัวเองก็คือสิ่งที่ถูกต้องที่สุด',satir:'**การรักษาขอบเขตของตัวเอง** ก็เป็นการดูแลตัวเองที่สำคัญ — เราไม่สามารถช่วยคนอื่นได้ถ้าเราตัวเองยังไม่ปลอดภัย'},
          ok2:{type:'ok',title:'📓 ดูแลใจตัวเองก่อน',text:'มินนาเขียนออกมาได้ว่า "ฉันเป็นห่วงพวกเขา แต่ฉันก็ต้องดูแลตัวเองด้วย" แค่นั้นก็เพียงพอสำหรับวันนี้',satir:'**การ process ภายใน** ก็คือการดูแลตัวเองแบบหนึ่ง — ไม่ต้องพูดออกมาเสมอไป แค่รู้ว่าตัวเองรู้สึกอะไรและเขียนมันออกมา ก็คือก้าวสำคัญแล้ว'},
        },
        chooserNote:'มินนาไม่ต้องช่วยทุกคน"""

assert old2 in c2, "ERROR: old2 string not found in file!"
c3 = c2.replace(old2, new2, 1)
assert c3 != c2, "ERROR: no replacement made for outcome!"

with open('satir-growth-game-v31.html', 'w', encoding='utf-8') as f:
    f.write(c3)

print("Done! satir-growth-game-v31.html written successfully.")
