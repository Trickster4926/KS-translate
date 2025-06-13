label th_A25:

window hide None
scene black
with dissolve

play sound sfx_alarmclock

scene bg school_dormhisao
with openeye

window show

"นาฬิกาปลุกดังแล้ว ฉันนอนพลิกไปมาอยู่พักหนึ่งจนนึกได้ว่าวันนี้จะลองวิ่งดูอีกครั้ง"

"ไม่รู้ว่าคิดถูกแล้วจริง ๆ หรือเปล่า แต่ก็อยากทำต่อ"

"เพื่อสุขภาพนี่นะ"

"ก็ใช่ว่าช่วงนี้อะไรจะราบรื่นไปหมดหรอก แต่ก็ไม่ได้ลำบากลำบนถึงขั้นไม่อยากลุกขึ้นมารักษาสุขภาพสักหน่อย"

"อีกอย่าง ทำแบบนี้ก็คงพอช่วยให้อาการนี้ดีขึ้นบ้างแหละนะ"

"ถ้าทำเรื่องนี้ได้ ก็ทำอะไรก็ได้หมด"

"At least that's what I keep telling myself."

scene bg school_track
with locationskip

play ambient sfx_emirunning fadein 0.3

"อย่างน้อยฉันก็บอกตัวเองอย่างนั้น"

"เอมิเหมือนจะมาก่อนสักพักแล้ว"

"เหมือนจะพอได้เหงื่อแล้วด้วย"

"มาถึงนี่กี่โมงกันแน่เนี่ย"

stop ambient fadeout 0.3

show emi basic_grin_gym at center
with charaenter

play music music_emi fadein 0.5

emi "อ๊ะ นายน่ะเอง!"

show emi basic_closedgrin_gym
with charachange

emi "ไม่คิดว่านายจะมาอีกนะเนี่ย!"

hi "ทำไมล่ะ"

show emi basic_grin_gym
with charachange

emi "ก็ มีไม่กี่คนหรอกที่จะมาซ้ำน่ะ"

show emi basic_annoyed_gym
with charachange

"เธอขมวดคิ้วดูอารมณ์เสียกับเรื่องนั้น"

emi "อย่างคนในชมรมวิ่งงี้"

emi "แต่ก็ใช้ระบบสมัครใจน่ะนะ ก็ไม่แปลกใจเท่าไหร่หรอก"

emi "แถมยังเช้าขนาดนี้…"

"เธอยักไหล่ และเหมือนอยู่ ๆ ก็ลืมว่าพูดเรื่องอะไรอยู่"

show emi basic_happy_gym
with charachange

"คิ้วที่ขมวดคลายลงคล้ายปัดความคิดพวกนั้นทิ้งไปแล้ว"

emi "เอาละ! งั้นก็มาเลย!"

hi "หา?"

show emi excited_proud_gym
with charachange

emi "นายมาวิ่งอีกใช่ไหมล่ะ"

hi "ก็ ใช่"

show emi basic_closedhappy_gym
with charachange

emi "ก็มาเลย!"

scene bg school_track_on
with locationchange

"อยู่ ๆ ฉันก็ถูกลากตัวไปยังลู่วิ่ง"

play ambient sfx_emijogging fadein 0.3

scene bg school_track_running
with locationchange

"เหมือนกับที่วิ่งเมื่อวานเลย"

"ซึ่งก็คือ ฉันดูจะกระหืดกระหอบ ในขณะที่เอมิพุ่งตัวไปสบายฉิวจนฉันอิจฉา"

"รำคาญตัวเองที่เหนื่อยง่ายอย่างนี้"

"รู้อยู่ว่าฉันควรอดทน ค่อยเป็นค่อยไป แต่ว่า…"

"ฉันไม่รู้จะเอากำลังใจมาจากไหนต่อ"

"พอวนครบรอบแล้วก็เตรียมวิ่งรอบที่สอง"

play ambient sfx_emirunning

"เอมิเหมือนจะอดทนลดความเร็วฝีเท้าให้เท่าฉันไม่ไหวจนนำออกไปก่อนแล้ว"

"เมื่อวานฉันก็หยุดไปตอนวิ่งได้ประมาณนี้"


label th_choiceA25:
menu:
    with menueffect

    "จะต่ออีกไหวมั้ยนะ"

    "ไปต่ออีก":
        return m1

    "ไปแบบสบาย ๆ ":
        return m2

label th_A25a:

# if C72

stop music fadeout 10.0

"ฉันปล่อยให้เอมิวิ่งไปด้วยความเร็วของเธอ และเธอก็ดูจะไม่ลดละเลย วิ่งนำฉันไปได้ครึ่งรอบสนามแล้ว"

"ก็ว่าไม่ได้หรอก"

"ไม่ได้มาแข่งเอาเป็นเอาตายสักหน่อยนี่นะ"

"ฉันคอยวิ่งไปเรื่อย ๆ ด้วยจังหวะสม่ำเสมอ ซึ่งฉันก็ต้องทำอย่างนี้อยู่แล้วนี่"

"เพิ่งเริ่มก็ไม่ต้องฝืนขีดจำกัดของตัวเองหรอก"

"ให้ตาย คุ้มค่ามั้ยเนี่ย"

scene bg school_track_on
with locationchange

"พอวิ่งได้สองรอบฉันก็หยุดอีก"

"เอมิยังวิ่งต่อ และเหมือนฉันจะเห็นว่าเธอผิดหวังด้วย"

"เหอะ บ้าหรือเปล่า"

"ฉันไม่มีหลักฐานอะไรจะพิสูจน์ให้เธอเห็น จะว่าไปแล้วฉันก็ไม่มีอะไรพิสูจน์ให้ตัวเองเห็นเหมือนกัน"

"ฉันอยู่อย่างนี้ก็ดีอยู่แล้ว"

"แล้วฉันก็ไม่ใช่นักวิ่ง"

"สงสัยจะคิดผิด"

"อาจจะมีอย่างอื่นที่พอให้ทำแทนได้"

"อีกอย่าง ต้องตื่นเช้าขนาดนี้ก็ไม่ไหวหรอก จะรักษาสุขภาพอาจจะมีวิธีอื่นก็ได้"

"เดิน มั้ง เดินเล่นช่วงบ่ายสบาย ๆ "

"อืม ก็ฟังดูดี ฉันวิ่งไม่ไหวหรอก"

stop ambient fadeout 2.0

scene bg school_track
with locationchange

"ฉันโบกมือให้เอมิแล้วกลับห้อง"

"ไว้ค่อยคิดแล้วกัน"



#if C71

label th_A25b:

"นี่ฉันมัวทำอะไรอยู่"

"จะยอมแพ้แล้วให้เอมินำไปเฉย ๆ เหรอ"

scene bg school_track_running
with locationchange

"ฉันเร่งฝีเท้าขึ้น"

"รอบที่สองผ่านไปอย่างรวดเร็ว ฉันไปต่อโดยไม่สนเลขรอบแล้ว"

"เอมิหันมามองแล้วยกยิ้ม"

show emi excited_proud_gym at twoleft
with charaenter

emi "ยังไหวอยู่เหรอ"

hi "เดี๋ยว *แฮ่ก* เธอหา *แฮ่ก* ว่าฉันไม่ฟิต *แฮ่ก*"

show emi excited_laugh_gym
with charachange

hide emi
with charamoveoutleft

play ambient sfx_emipacing

"เอมิหัวเราะ—ซ้ำยังไม่ลดฝีเท้าเธอลงเลย—แล้วเพิ่มความเร็วอีก"

"ได้ ถ้าจะเล่นแบบนี้ละก็…"

"ฉันเร่งฝีเท้าตัวเองบ้าง"

"รู้สึกเหมือนปอดจะไหม้ ขาก็เริ่มส่งสัญญาณว่านี่ทำอะไรอยู่วะ"

"กรดแลกติกต่างกรีดร้องอยู่ในกล้ามเนื้อ แต่ฉันทำหูทวนลม"

"ฉันจะมัวรั้งท้ายไม่ได้ ไม่งั้นฉันก็แพ้สิ"

"แต่สมองด้านตรรกะของฉันก็เริ่มถามว่านี่แข่งกันไปตอนไหน"

"ก็อยากตอบอยู่หรอก แต่ตอนนี้ไม่มีสมองจะคิดแล้ว"

"เธอ{b}เร็ว{/b}มาก"

"นี่วิ่งไหวไปได้ยั—{w=.5}{nw}"

stop music fadeout 0.2

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

"รู้สึกเหมือนหน้าอกถูกรัด อึดอัดจนทรมาน"

"สองเท้าของฉันเสียหลักแม้แต่ก่อนจะทันได้คิดแค่ว่า “ฉิบหาย”"

scene bg school_track_on:
    xalign 0.5 yalign 0.52 rotate 0 zoom 1.0
    linear 0.1 rotate -6 zoom 1.2
with vpunch

"ฉันสะดุดล้ม มือข้างหนึ่งกุมหน้าอกเอาไว้ อีกข้างกระแทกเข้ากับลู่วิ่งไม่ให้หน้าทิ่มพื้น"

stop ambient fadeout 0.2

"เอมิหันขวับมาแล้วมองตาโต"

emi "ฮิซาโอะ!"

play ambient sfx_emisprinting

"เธอร้องเรียกฉันแล้ววิ่งมาจากอีกฟากของลู่วิ่ง"

show emi basic_shock_gym:
    xalign 0.5 yalign 0.7 rotate -6 zoom 1.2
with charamoveinright

stop ambient fadeout 0.1

emi "เป็นอะไรหรือเปล่า"

hi "อึก—เปล่า แค่…"

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

"หายใจช้า ๆ "

"ใจเย็น ๆ อย่าล่กไป"

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

"อย่าล่ก"

show emi basic_shock_gym:
    parallel:
        linear 0.2 rotate -12 zoom 1.5
    parallel:
        "emi basic_hes_gym" with Dissolve(0.2, alpha=True)
with None

emi "ให้ไปเรียกพยาบาลมั้ย"

show black
with shuteyefast

scene black
with None

"ฉันหลับตาตัดขาดจากโลกภายนอก"

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.3)

with Pause(1.0)

play sound sfx_heartslow
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.7)

"หัวใจของฉันพยายามกลับมาเต้นให้ปกติ"

"ความรู้สึกเจ็บที่อยู่ในหน้าอกค่อย ๆ บรรเทาลง"

"แล้วก็หายไปเหมือนไม่มีอะไรเกิดขึ้น"

"ก็…ไม่มีอะไร? ไม่สิ มีแหละ"

play music music_rain fadein 2.0

scene bg school_track_on
show emi basic_hes_gym_close at center
with openeye

"ฉันลืมตาขึ้นอีกครั้งแล้วมองเอมิที่ดูเป็นห่วงมาก"

hi "น่าจะไม่เป็นอะไร"

"เสียงของฉันฟังดูประหลาดจนแม้แต่ตัวฉันเองยังรู้สึก เป็นน้ำเสียงเรียบนิ่งพิกลที่ทำเอมิขมวดคิ้ว"

show emi sad_annoyed_gym_close
with charachange

emi "ฉันว่าไม่น่าใช่นะ"

"เธอพยักหน้ากับตัวเองเหมือนตัดสินใจบางอย่างได้"

show emi basic_annoyed_gym_close
with charachange

emi "เอาละ นายมากับฉันเลย"

emi "นายต้องไปหาคุณพยาบาล"

with vpunch

"เอมิจับแขนฉันแล้วดึงตัวให้ลุกขึ้น ยังรู้สึกตัวโยกนิดหน่อย แต่ก็ไม่ได้ขอพึ่งไหล่ของเอมิไป"

"เอาจริง ๆ ฉันก็แอบอายกับความอ่อนแอของตัวเองเหมือนกัน"

"ไม่อยากให้เอมิต้องมาเป็นห่วงเลย แต่เหมือนจะสายไปแล้ว"

"ไม่สิ ไม่อยากให้ใครมาเป็นห่วงอาการฉันทั้งนั้นแหละ ถึงป่านนี้จะสายไปแล้วเหมือนกันก็เถอะ"

"ฉันอยากจะจัดการกับสิ่งเหล่านั้นด้วยตัวเองโดยไม่ต้องรบกวนใคร"

"แม้จะขอเช่นนั้น แต่ยังไงไม่เป็นโรคนี้เลยจะดีที่สุด"

stop music fadeout 1.0

scene bg school_nurseoffice at bgleft
with locationskip

show emi basic_shock_gym at tworight
with easeinright

emi "คุณพยาบาลคะ!"

"เอมิพุ่งตัวเข้าไปในห้องทำงานของคุณพยาบาลโดยไม่เคาะประตู แต่เขาไม่ตกใจเลย"

play music music_nurse fadein 0.5

show nurse grin at twoleft
with charaenter

nk "อรุณสวัสดิ์จ้ะสาวน้อย มีอะไรเหรอ"

"สาวน้อย? เอาเถอะ เขาจิบกาแฟอย่างใจเย็น แต่ก็วางลงหลังมองตามสายตาของเอมิมาเจอเข้ากับฉันที่ยืนทะมึนอยู่ตรงประตู" 

show nurse fabulous
with charachange

nk "ฮิซาโอะ มาทำไมเหรอ"

show emi excited_sad_gym
with charachange

emi "พอดีพวกเราวิ่งด้วยกันอยู่แล้วเขาก็สะดุดล้มมือกุมอยู่ที่หน้าอกค่ะ ทีแรกหนูตั้งใจว่าจะมาเรียกคุณพยาบาลแล้วให้เขา\nรอก่อน แต่เขาก็บอกว่าไม่เป็นไร แล้วหนูก็คิดได้ว่ายังไงหมอก็ต้องมาเห็นหน้าเขาอยู่ดีน่ะค่ะ แล้ว—{w=1.5}{nw}"

show nurse concern
with charachange

nk "ค่อย ๆ นะเอมิ ใจเย็น ๆ ก่อน"

show nurse neutral
with charachange

nk "ฮิซาโอะ เกิดอะไรขึ้น"

hi "ไม่รู้สิครับ ผมวิ่งอยู่แล้วอยู่ ๆ ก็เจ็บหน้าอกขึ้นมาเหมือนตอนนั้น แต่ไม่กี่วินาทีมันก็หายไปเอง"

hi "หัวใจคงเต้นผิดจังหวะนิดหน่อยละมั้งครับ"

show nurse concern
with charachange

"คุณพยาบาลขมวดคิ้วคล้ายบอกว่าคำว่า “เต้นผิดจังหวะ” กับ “นิดหน่อย” ไม่น่าอยู่ด้วยกันได้"

nk "ที่ฉันบอกให้ออกกำลังกายไม่ได้บอกให้ถึงขนาดนี้นะ ระวังหน่อยแล้วกันนะฮิซาโอะ"

hi "ผมก็ระวังอยู่นะครับ แค่…"

"พอมานึกดูแล้ว เหตุผลว่า “ไปวิ่งแข่งกับคนในชมรมวิ่ง” ก็ไม่ได้ฟังดูดีอย่างที่คิดเท่าไหร่"

nk "แค่อะไร"

hi "เอ้อ…คือ…"

hi "ผมวิ่งแข่งกับเอมิน่ะครับ"

nk "จริงเหรอเอมิ"

show emi basic_hes_gym
with charachange

"เอมิทำท่ากระมิดกระเมี้ยน ดูสำนึกผิดอย่างน่ารัก"

emi "เอ่อ ก็…"

show emi basic_closedsweat_gym
with charachange

"สุดท้ายเธอก็ไม่กล้าพูดออกมาแล้วได้แต่พยักหน้า"

"คุณพยาบาลถอนหายใจแล้วนวดหน้าผากด้วยมือข้างหนึ่งด้วยความหน่ายใจ"

nk "เอมิ เธอต้องคิดถึงเรื่องขีดจำกัดของคนอื่นด้วยสิ!"

nk "ไม่รู้ว่าเขาบอกเธอไปหรือยัง แต่หัวใจฮิซาโอะเขาไม่ค่อยแข็งแรง เธอสะเพร่ามากนะที่ให้เขามาวิ่งแข่งด้วยเนี่ย"

hi "เอ่อ ที่จริง ผมเป็นคนเริ่มเองครับ"

"คุณพยาบาลได้ฟังแล้วอึ้งไป"

nk "{b}ว่าไงนะ{/b}?"

hi "พวกเราก็วิ่งกันอยู่ แล้วเอมิก็นำไป ผมเลย เอ่อ เร่งเท้าให้วิ่งทัน"

"คุณพยาบาลมองเพดาน คงสวดขอขันติจากพระเจ้าหรืออะไรสักอย่าง แล้วมองกลับมาที่พวกเราสองคน"

nk "โอเค สรุปโง่{b}แพ็กคู่{/b}"

nk "ก็ค่อยยังชั่วหน่อยละมั้ง"

nk "เอ้า ฮิซาโอะ ขอตรวจดูให้แน่ใจหน่อยว่าหัวใจเธอจะไม่ระเบิดหรืออะไรไปก่อนแล้วกัน"

show bg school_nurseoffice at left
show nurse concern at center
show emi basic_closedsweat_gym at Alphaout(1.0), offscreenright
with charamove

hide emi
with None

"ฉันตามเขาอย่างว่าง่ายไปที่ห้องข้าง ๆ เพื่อดูว่าฉันจะไม่ได้ล้มพับแล้วตายไปจริง ๆ "

nk "แล้วเป็นยังไงบ้าง"

hi "ไม่รู้สิครับ ไม่มีอะไรมาก ก็เหนื่อย แต่ก็แค่คงเพราะออกกำลังกาย"

nk "เธอพักอยู่ที่นี่สักสองสามชั่วโมงก่อนนะ แล้วจะดูอาการอีกที"

"ฉันไม่ปฏิเสธแล้วนอนลงกับเตียงพยาบาล"

stop music fadeout 2.0

scene bg school_nurseoffice at left
with shorttimeskip

"เอมิเข้ามาหาด้วยท่าทางซึมกะทือหลังจากที่โดนคุณพยาบาลว่าไปชุดใหญ่อยู่อีกห้อง"

"เพราะประตูปิดอยู่ก็เลยไม่ได้ยินว่าพูดอะไร แต่คงไม่ใช่เรื่องดีแน่ ๆ ละ"

show emi sad_depressed_gym at center
with charaenter

play music music_dreamy fadein 0.5

emi "คือ ฉันขอโทษ ขอโทษจริง ๆ นะ"

emi "ฉันน่าจะระวังให้มากกว่านี้"

hi "น่า เธอไม่รู้นี่ เธอไม่ผิดหรอก"

"เธอดูหงอยและรู้สึกผิดมาก แม้แต่คำตอบของฉันก็ไม่ได้ช่วยให้เธอร่าเริงขึ้น"

emi "ฉันอยากชดใช้ให้นาย"

"พยักหน้าเหมือนตัดสินใจอะไรได้แบบนั้นอีกแล้ว"

show emi sad_shy_gym
with charachange

emi "นายต้องมากินข้าวเที่ยงกับฉันนะ"

emi "ฉันจะเอามาเผื่อนายด้วย อร่อยมาก ๆ เลยละ!"

"ฉันกำลังพูดว่า “ไม่ต้องก็…” แต่พอเห็นหน้าเธอแล้วก็ต้องหุบปากแล้วพยักหน้ารับไป"

show emi excited_proud_gym
with charachange

emi "ดีเลย!"

show emi basic_grin_gym
with charachange

emi "เรามาเจอกันที่ดาดฟ้านะ"

hi "เรา?"

show emi basic_closedgrin_gym
with charachange

emi "ช่าย! อากาศก็ดี ดาดฟ้านี่แหละเหมาะกับข้าวเที่ยงเลยนะ"

hi "อย่างงี้นี่เอง"

show emi sad_shy_gym
with charachange

emi "นายจะมาใช่มั้ย"

emi "นายจะไม่ปฏิเสธโอกาสที่จะให้ฉันได้ชดใช้นี้ใช่มั้ย"

hi "ไม่หรอกน่า"

show emi excited_joy_gym
with charachange

emi "เยี่ยม! ไว้เจอกัน!"

hide emi
with charaexit

with shorttimeskip

"สติฉันอยู่ในสภาพสะลึมสะลือพร้อมความรู้สึกอ่อนเปลี้ยเพลียแรง"

"ไม่ใช่แค่ตัว แต่ทั้งร่างอ่อนยวบกับชาไปหมดจนไม่รู้สึกอะไร"

"ฉันกลืนน้ำลายด้วยความยากลำบากแล้วนอนให้นิ่งที่สุด ซึ่งพออยู่ในสภาพนี้แล้วก็ทำได้ไม่ยาก"

"คุณพยาบาลดูวุ่นอยู่ข้างหลังม่านที่เขารูดมาบังเพื่อความเป็นส่วนตัวของฉัน ฉันเห็นเงาของเขาวูบไหวไปมาในแสงแดด"

"เขาเปิดหน้าต่างห้องทำงานของเขา และข้างนอกมีลมพัด"

"ผ้าม่านสีขาวสะอาดโบกพลิ้วไปกับสายลมอย่างเอื่อยเฉื่อยเหนื่อยหน่ายคล้ายคลื่น แสงลอดผ่านเข้ามาช้า ๆ ครึ่งหนึ่งถูก\nผ้าม่านซับไป"

stop music fadeout 5.0

scene darkgrey
with shuteye

"ฉันหลับตาลง สายลมพัดโบกกับใบหน้าฉันเหมือนกับที่พัดผ่านผ้าม่านอันนุ่มนวล"

"ฉันฟังเสียงหัวใจตัวเองอยู่ครู่หนึ่งเพื่อกลบเสียงพยาบาลที่นั่งพิมพ์กับคอมพิวเตอร์อยู่ และกลบเสียงหอบของฉันเองด้วย"

"ก็คงที่ดี"

"ให้ตายเถอะ มาได้ไม่ถึงอาทิตย์ก็อยู่ในสภาพนี้อีกแล้ว รอบนี้ทำพลาดจริง ๆ ไม่น่าไปทำหล่อเป็นนักกีฬาต่อหน้าของจริง\nอย่างนั้นเลย"

"แล้วทำไมต้องทำเป็นเท่ เหมือนว่าที่หัวใจเต้นผิดจังหวะนั้นไม่ใช่เรื่องใหญ่ด้วย ทั้งที่ดูก็รู้แล้วว่าเป็นเรื่องใหญ่"

"ก็แค่ปฏิกิริยาตอบสนองอัตโนมัติแหละ เพื่อจะได้ปัดให้พ้นไป เก็บเอาไว้ภายใน"

"ฉันไม่อยากให้เป็นอย่างนั้น"

"ฉันไม่อยากให้เอมิมาเห็น"

"โอยยย…"

"โง่โง่โง่"

"ฉันต้องระวังให้มากกว่านี้ ไม่งั้นได้กลับไปนอนโรงพยาบาลอีกแน่ หรืออาจจะแย่กว่านั้น"

"…"

"เป็นความคิดสุดท้ายก่อนที่ฉันจะปล่อยให้ความเหนื่อยล้าครอบครองร่างกาย"

scene black
with Dissolve(1.0)

window hide Dissolve(2.0)

with Pause(2.0)

scene bg school_nurseoffice at left
with openeye

window show

play music music_daily fadein 6.0

"ฉันหลับไป ว่าแต่นานแค่ไหน กี่โมงแล้วเนี่ย"

"หัวก็รู้สึกเบลอ ๆ นิดหน่อย ตาก็กะพริบอยู่อย่างนั้น"

show bg school_nurseoffice at center
with charamove

"ฉันรูดผ้าม่านเก็บกลับไป หรี่ตามองแสงที่สาดจ้าเข้ามาจากทางหน้าต่าง สัมผัสของพื้นที่รับรู้ด้วยเท้าต่างกับที่ลมพัดเมื่อครู่ลิบลับ"

"พยาบาลผละจากงานของเขามามองโดยยังนั่งที่เดิม"

show nurse fabulous at center
with charaenter

nk "เป็นยังไงบ้าง"

"ฉันไม่ได้ตอบเพราะไม่รู้จะบอกยังไงดี ยังรู้สึกอึน ๆ ที่มานอนเอาเวลานี้ หวังว่าจะพอดูปกติบ้างนะ"

hi "กี่โมงแล้วครับ"

"ฉันถามเสียงต่ำเพื่อจูนสมองกลับ คุณพยาบาลดูนาฬิกาข้อมือแล้วตอบ"

"ทุกอย่างดูเคลื่อนไหวอย่างเฉื่อยชา"

show nurse neutral
with charachange

nk "สิบสิบห้า"

"ฉันคิดอยู่ว่าแปลว่ากี่โมง แต่ก็ไม่แน่ใจ"

show nurse concern
with charachange

nk "เธอยังไม่ได้ตอบฉันเลยนะฮิซาโอะ"

hi "อ้อ สบายดีครับ"

show nurse neutral
with charachange

nk "งั้นก็ลุกมา จะดูว่าเป็นยังไงบ้าง อย่า…"

$ renpy.music.set_volume(0.5, 0.2, channel="music")

show bg school_nurseoffice as dizzy_bg behind nurse:
    xalign 0.5 yalign 0.5 rotate 0 zoom 1.0 alpha 0.0
    ease 0.4 rotate 6 zoom 1.05 alpha 0.5

show nurse neutral as dizzy_fg:
    xalign 0.5 yalign 0.5 rotate 0 zoom 1.0 alpha 0.0
    ease 0.4 rotate -4 zoom 1.05 alpha 0.5
with Pause(0.4)

show bg school_nurseoffice as dizzy_bg behind nurse:
    ease 1.0 rotate 0 zoom 1.0 alpha 0.0

show nurse neutral as dizzy_fg:
    ease 1.0 rotate 0 zoom 1.0 alpha 0.0

"พอฉันลุกขึ้นตามสั่งก็รู้สึกตัวโงนเงนเพราะขยับตัวเร็วเกินไป คุณพยาบาลเข้ามาช่วยประคองแขนแล้วถอนหายใจ"

show nurse concern
hide dizzy_bg
hide dizzy_fg
with charachange

nk "…ลุกเร็วเกินไป นั่นแหละที่จะเตือนเมื่อกี้ นั่งอยู่ตรงนั้นแหละ เดี๋ยววัดความดันให้แน่ใจก่อน"

$ renpy.music.set_volume(1.0, 2.0, channel="music")

"ไม่น่าหวังดีเล้ย ฉันเงียบไปเพราะอายตัวเอง ส่วนคุณพยาบาลก็ง่วนอยู่กับการเตรียมอุปกรณ์ที่ดูเก่ากับแขนฉัน ผ่านไป\nสองสามนาทีเขาก็เก็บ ไม่ได้ดูดีใจหรืออารมณ์เสีย"

show nurse neutral
with charachange

nk "โอเค ก็สบายดีนะ หายเวียนหัวหรือยัง"

hi "ครับ"

nk "แล้วหัวใจเธอเป็นไงบ้าง"

show nurse concern
with charachange

nk "เธอสะเพร่ามากเลยนะฮิซาโอะ"

"ฉันเก็บคำเถียงที่จะตอบกลับไป ที่เขาบอกก็เคยคิดเองอยู่ แต่พอได้ยินคนอื่นพูดแล้วก็อยากจะต่อต้าน"

"สิ่งที่เขาพูดไม่ได้รื่นหูมากนัก แต่ก็ใช่ว่าจะผิด"

hi "ครับ"

show nurse neutral
with charachange

"เขาพยักหน้าด้วยสีหน้าเรียบ ๆ เหมือนเมื่อครู่"

"ถ้าเขาบอกว่า “บอกแล้ว เห็นไหม” อีกฉันก็คงโกรธ แต่เขาก็ไม่ได้พูด"

nk "ฉันคอยช่วยรักษาสุขภาพเธอให้ได้ แต่ยังไงสุดท้ายก็อยู่ที่ตัวเธออยู่ดีนะ หวังว่าเหตุการณ์ครั้งนี้จะเป็นเครื่องเตือนใจเธอ"

show nurse fabulous
with charachange

nk "เอ้านี่ เอาไปให้ครูนะ จะได้ไม่ต้องคุยให้ยืดยาว"

"ฉันหยิบแผ่นกระดาษที่เขายื่นให้แล้วเดินออกมาเพราะไม่รู้จะพูดอะไรต่อ แล้วก็ไม่ได้อยากพูดด้วย"

show nurse neutral
with charachange

nk "อย่าไปมีเรื่องอะไรอีก รับทราบนะ ฉันว่ารอบนี้เธออาจจะแค่ตกใจเฉย ๆ แต่รอบหน้าอาจจะไม่ใช่แล้วก็ได้นะ"

"รับทราบ"

scene bg school_nursehall
with locationchange

stop music fadeout 4.0

"ทางไปอาคารหลักจากอาคารรองนั้นพอจะมีทางอื่นอยู่บ้าง แต่ฉันก็ไม่ได้อยากรู้ แถมอาจไปหลงได้อีก จึงมาตามทางออก\nที่ฉันจำได้"

scene bg school_courtyard
with locationchange

"ฉันหยุดยืนอยู่ที่บันไดอาคารรอง คิดอยู่พักหนึ่งว่าจะกลับหอไปเอาหนังสือกับข้าวของหรือจะตรงดิ่งไปห้องเรียนเลยดี"

"แสงแดดแยงตาพาให้ฉันเดินกลับหอ"


#******************************

label th_A26:

window hide None
scene black
with dissolve

scene bg school_dormhisao
with openeye

with Pause(0.2)

scene bg school_dormbathroom
with locationskip

window show

"ฉันตื่นมาอาบน้ำอุ่น"

label th_A26a:

scene bg school_dormhisao
with locationskip

"สิ่งที่เห็นเมื่ออยู่ในห้องเป็นสิ่งแรกคือขวดยาที่เรียงรายดูคุ้นตาอยู่บนโต๊ะ เห็นแล้วก็หดหู่อย่างเคย"

"หงุดหงิดชะมัด นึกว่าจะโอเคแล้ว นึกว่าจะทำใจยอมรับได้แล้ว"

"แต่สิ่งที่ฉันทำจริง ๆ นั้น… คือการปล่อยให้ตัวเองลืมถึงปัญหาที่มีอยู่ การได้มาอยู่ที่นี่คือเครื่องเตือนถึงความเป็นจริง และยิ่งฝืนต่อต้านไปก็เจ็บปวด"

"นั่งทบทวนไปก็เท่านั้น เพราะฉันเคยทำมาแล้วเป็นเดือน ๆ คงถึงเวลาที่ต้องก้าวข้ามผ่านไปเสียที"

"ถ้าฉันปล่อยให้ตัวเองลืมไปว่าฉันจะอยู่ได้ไม่นานเท่าคนอื่น ๆ ก็คงไม่ได้อะไรขึ้นมา"

"ชีวิตฉันอาจต่างจากคนอื่น แต่ก็เป็นชีวิตที่กำลังเดิน"

"ฉันจะคอยคิดเช่นนั้น"

"ฉันกินยาที่มีมากมายในมือจนหมดแล้วปัดอารมณ์หม่นหมองนี้ออกไปจากหัว จากนั้นเตรียมตัวไปเข้าเรียนแต่เช้าเช่นเคย"

scene bg school_dormhallway
with locationchange

"พอเดินออกมาจากห้องก็เห็นเคนจิที่โผล่มาจากปลายโถงทางเดินย่องมาทางห้องของเขาโดยในมือมีถุงขนาดใหญ่อยู่\nเขาเดินผ่านฉันไปอย่างเงียบเชียบเหมือนนินจาที่พรางตัวอยู่ ฉันทักเขา"

hi "ไง"

show kenji neutral at center
with charaenter

play music music_kenji fadein 0.5

"เขาสะดุ้งที่ฉันทัก"

ke "โอ้ ไง พวก ไม่ยักรู้ว่านายอยู่ตรงนี้ พอดีเพลียมาก"

"ไม่เห็นมากกว่ามั้ง แต่นั่นไม่ใช่ประเด็น"

hi "ออกไปไหนแต่เช้าเนี่ย ไปซื้อของ?"

show kenji tsun
with charachange

ke "เปล่า ไม่ได้ไปซื้อของ พอดีฉันต้องไปหา…ครูคณิตบ้างน่ะ อืม พอดีนึกได้ว่าถ้าถามไว้ก่อนว่าสอบคราวหน้าเมื่อไหร่\nก็ดีเหมือนกัน เพราะถ้าขอเขาก็บอกให้"

hi "แล้วในถุงนั่นมีอะไร"

show kenji neutral
with charachange

ke "ไหน ๆ ก็ออกมาแล้วเลยกะว่าไปซื้อของด้วยก็ดี พอดีต้องการข้าวของมาเพื่อใช้ต่อสู้กับทฤษฎีสมคบคิดสตรีนิยมน่ะ"

hi "เอ่อ อ่าฮะ"

hi "นายไม่ออกไปข้างนอกไม่ใช่เหรอ"

show kenji happy
with charachange

ke "ฉันใส่หมวกอยู่ไง"

"ฉันคิดที่จะไม่บอกว่าเขาไม่ได้สวมหมวกอยู่"

"ความเงียบอันน่ากระอักกระอ่วนที่เข้าปกคลุมพวกเราสองคนถูกทำลายด้วยเสียงประตูที่ถูกเคนจิเปิดช้า ๆ ส่งเสียงเอี๊ยด\nจนบรรยากาศดูกระอักกระอ่วนกว่าเดิม เขาวางถุงนั้นไว้ในห้องแล้วปิดประตู"

hi "ทึ่งนะเนี่ยที่นายถึงขั้นไปถามวันสอบ ขยันดีนะที่ใช้ประโยชน์หาโอกาสมาอ่านหนังสือน่ะ"

show kenji tsun
with charachange

ke "ฉันไม่อ่านหนังสือสอบหรอก"

hi "อ่า…"

show kenji neutral
with charachange

ke "แค่อยากรู้เฉย ๆ ว่าสอบรอบถัดไปวันไหน ยังไงก็ต้องสอบอยู่แล้วนี่ ที่อยากรู้คือวันไหนที่โดดเรียนไม่ได้ ปกติไอ้วันสอบนี่\nเขาบอกทางโทรศัพท์น่ะ ก็เลยต้องออกไปถาม"

hi "ก็ถ้าบอกทางโทรศัพท์แล้วจะออกไปทำเพื่อ"

show kenji tsun
with charachange

ke "ฉันไม่มีโทรศัพท์"

hi "ไม่มีนี่คืออะไร ลืมไว้ที่บ้าน?"

show kenji neutral
with charachange

ke "เปล่า ฉันไม่ใช้โทรศัพท์น่ะ ฉันไม่มีโทรศัพท์ โทรศัพท์ ไม่มีโทรศัพท์"

hi "แล้วไหงถึงไม่มี ไม่มีได้ไง ไม่ใช้โทรศัพท์เลย ไม่มีโทรศัพท์อะนะ"

show kenji tsun
with charachange

ke "ฉันแค่ไม่ชอบโทรศัพท์น่ะ จริง ๆ กลัวด้วย ไม่รู้ทำไม สงสัยเป็นความกลัวในจิตใต้สำนึกงี้มั้ง"

ke "แต่เอาง่าย ๆ คือเวลาได้ยินเสียงโทรศัพท์แล้วจะเริ่มลนลาน เป็นความลับดำมืดที่สุดของฉันเลย"

show kenji neutral
with charachange

ke "ฉันคิดไว้สองทฤษฎี คือถ้าไม่ใช่ว่าฉันกลัวการรับสายที่เป็นลางร้ายที่จะพลิกชีวิตฉันอย่างบอกไม่ถูกแล้ว ก็คงเป็นว่า\nเมื่อก่อนฉันเคยโดนทุบด้วยโทรศัพท์ ประมาณว่าทุบแรงจนจำไม่ได้"

hi "ทุบเข้าที่หัวอะดิ"

show kenji tsun
with charachange

ke "เออดิ คิดว่าโดนตรงไหนถึงจะลืมได้อีก ตูดเหรอ"

"เออว่ะ เครียดเลยทีนี้ เคนจิเปิดประตูอีกครั้งเมื่อเห็นว่าบทสนทนาจบแล้วและเตรียมเข้าไปในห้อง"

show kenji neutral
with charachange

ke "เออ ไปนอนละ ฝันดี"

hi "อีกยี่สิบนาทีจะเข้าเรียนแล้วนะเฮ้ย"

show kenji tsun
with charachange

ke "พอดีใช้แรงมาแล้วอะ ขี้เกียจเข้าเรียนละ"

show kenji happy_close
with characlose

ke "เอ้อ เอาลิปมันเปล่า พอดีซื้อมาสองอัน นึกว่าร้านเอาถ่าน AA มาขายแยกก้อนอะ"

hi "ขอบใจ แต่ไม่ต้อง"



label th_A26b:

scene bg school_dormhallway
show kenji happy_close at center
with None

stop music fadeout 0.3

play sound sfx_doorslam

show kenji tsun_close
with vpunch

"ประตูที่ปลายโถงทางเดินเปิดออกด้วยเสียงดังโครมเนื่องจากถูกเปิดด้วยความรุนแรงเกินไปและชนเข้ากับกำแพง\nตามด้วยเสียงหัวเราะเริงร่าที่ดังลั่น ฉันรู้ทันทีว่าใครมา"

play music music_comedy fadein 0.3

show misha perky_smile at center behind kenji
show shizu basic_normal2 at center behind kenji
with zoomin


show shizu basic_normal2:
    easein 1.0 tworight
show misha perky_smile:
    easein 1.0 twoleft
show kenji tsun_close:
    0.25
    easeout 0.5 offscreenleft alpha 0.0
with Pause(1.0)

hide kenji
with None

play sound sfx_impact2

"เคนจิหายตัวเข้าไปในห้องราวนินจาพร้อมกับเสียงนั้น ปิดประตูดังปึงขณะที่ชิซูเนะและมิช่ากำลังเดินมา คนที่เดินนำนั้น\nเดินตรงเข้ามาหาฉัน ส่วนคนตามเดินเล่นเลาะไปตามกำแพง"

show misha hips_smile_close at twoleft
with characlose

"ฉันจะทำอย่างเคนจิบ้าง ทว่าสายไปแล้ว มิช่ายื่นเท้ามาขัดที่ประตูไม่ให้ปิดได้ จึงต้องจำใจให้พวกเธอเข้ามา"

scene bg school_dormhisao
with locationskip

show shizu behind_smile at center
with charaenter

shi "…"

show shizu behind_smile at tworight
with charamove

show misha hips_grin at twoleft
with charaenter

mi "ไงฮิจัง~! ดีจ้า~ ดี~!"

hi "ดี"

hi "มาทำอะไรกัน"

"สองประโยคเมื่อกี้เว้นวรรคนานพอให้ดูสุภาพหรือยังนะ"

show shizu basic_normal
with charachange

shi "…"

show misha hips_frown
with charachange

mi "ฮิจังหยาบคายจัง~! นี่พวกเรามารับนายนะ!"

show misha hips_smile
with charachange

mi "คิดว่าพวกเรามาหาเพราะกลัวจะหนีไปก่อนละสิ คงไม่ใช่มั้ยฮิจัง~!"

hi "เอ้ย ยังไม่ได้พูดงั้นเลยนะ"

"แต่ทีนี้ก็รู้แล้วแหละว่ามาเพราะเรื่องนั้นจริง ๆ"

show misha sign_smile
with charachange

mi "ถึงเวลางานสภานักเรียนแล้วนะ ช่าย~!"

show misha hips_grin
with charachange

mi "ไม่ดีใจเหรอฮิจังที่จะได้ช่วยทั้ง~ โรงเรียน~! เหมือนเป็น วีรบุรุษ~! ลูกหลานต้องบอกเล่าต่อกันสืบไป!"

"น่าสนใจ ไม่เคยคิดมาก่อนเลยว่าการเข้าร่วมสภานักเรียนนี่เป็นภาระอันทรงเกียรติที่เทียบเท่าได้กับสิบสองภารกิจ\nของเฮอร์คิวลีสแบบนี้"

hi "ก็นะ…รับปากไว้อยู่แหละ เพราะงั้น…"

show shizu adjust_happy
with charachange

stop music fadeout 7.0

"เมื่อกี้ฉันเมินชิซูเนะจนเพิ่งมาสังเกตเอาตอนนี้ เธอมองผ่านฉันไปรอบ ๆ ห้องดูสิ่งนั้นสิ่งนี้ไปมาด้วยสายตาช่างคิดของเธอ"

"ให้ว่าแล้วก็สอดรู้เหมือนกันนะเนี่ย ความรู้สึกที่เหมือนโดนแก้ผ้าตัวเปล่าทำเอาตามเป้ารู้สึกยุบยิบ ยังดีที่ว่าตามพื้นไม่มี\nเสื้อผ้าที่ใส่แล้วหรืออะไรแบบนั้น"

show shizu behind_smile
with charachange

shi "…"

show misha perky_confused
with charachange

mi "หืม~ มีอะไรเหรอชิจัง"

show misha hips_smile
with charachange

mi "ช่าย นี่ห้องฮิจัง~! เพิ่งนึกได้เหมือนกันว่าไม่เคยเห็นมาก่อนเลย!"

show misha hips_grin
with charachange

mi "เรียบ ๆ จืด ๆ แต่ฮิจังคงยังไม่ว่างมาตกแต่งแหละ ใช่มั้ย~"

show misha sign_smile
with charachange

mi "นั่นอะไรเหรอ"

"เธอชี้ไปที่กองยาที่อยู่บนโต๊ะ"


label th_choiceA26:
menu:
    with menueffect

    "ไม่ค่อยอยากคุยเรื่องนี้กับสองคนนี้เลย"

    "พยายามเบี่ยงหัวข้อ":
        return m1

    "ไล่ทั้งสองคนออกจากห้อง":
        return m2


label th_A26c:

hi "ไม่มีอะไรหรอก"

show shizu basic_normal2
with charachange

"ฉันไปยืนบังของเหล่านั้นต่อหน้าทั้งสองคนไว้ ชิซูเนะผงะถอยดูท่าทีสงสัย แต่ก็มีความเป็นห่วงเจืออยู่"

"หวังว่าเธอจะเข้าใจว่าถ้าฉันเลี่ยงจะคุยแล้วคือฉันไม่อยากให้ซักไซ้ต่อ"

show shizu behind_blank
with charachange

shi "…"

show misha perky_confused
with charachange

mi "จริงเหรอ ซ่อนอะไรไว้น่ะฮิจัง~?"

hi "ไม่มีหรอก"

show shizu basic_normal
with charachange

shi "…"

show misha sign_confused
with charachange

mi "เหรอ~"

"ฉันรู้ทันทีว่าหนีไม่ได้แน่ ๆ ทั้งสองคนต่างก็อยากรู้อยากเห็นอยู่แล้ว ยิ่งซ่อนก็ยิ่งทำให้อยากรู้ไปอีก"

hi "อืม ก็ได้ ใช่ {b}มี{/b}นั่นแหละ แต่ฉันไม่อยากคุยเรื่องนี้ ไม่อยากคุย…ตอนนี้"

hi "เอาไว้ก่อนได้มั้ย"

show misha perky_smile
with charachange

"ระหว่างที่มิช่าแปลชิซูเนะก็หันมามองฉันด้วยสายตาครุ่นคิดของเธอ แววความอยากรู้อยากเห็นส่องลอดแว่นมา"

"เธอชนนิ้วเข้าด้วยกันราวใช้ความคิดชั่งใจว่าถ้าตามซักไซ้ฉันต่อแล้วจะคุ้มกับความหยาบคายที่ทำให้ฉันรำคาญหรือไม่"

"จนสุดท้ายเธอก็แรระบายรอยยิ้มออกมาแล้วทำภาษามือบางอย่างให้มิช่า"

play music music_dreamy fadein 2.0

show shizu adjust_happy
with charachange

shi "…"

show misha hips_smile
with charachange

mi "โอเค~! งั้นพวกเราจะรอจนกว่าสนิทกันกว่านี้ แล้วสักวันถ้านายอยากเล่าก็เล่าได้เลย~!"

"ทั้งสองคนยิ้มกว้างให้ ฉันทั้งรู้สึกทึ่งและรู้สึกว่าตัวเองงี่เง่าที่ทำตัวอย่างนั้น"

"สองคนนั้นก็ไม่ได้โง่สักหน่อย คงพอจะเดาได้แหละว่าฉันเป็นอะไร แถม…"

"เป็นคำง่าย ๆ ที่แสนอ่อนโยน รู้สึกโล่งใจที่ไม่ได้มองฉันไม่ดีแม้จะเป็นเช่นนี้ แม้ฉันจะไม่เหมือนคนอื่นที่นี่ แม้ฉัน\nจะทำตัวให้ชินไม่ได้"

"เบื้องหลังความซื่อบื้อและซุกซนเหล่านั้นแล้วเธอทั้งสองคนก็เป็นคนที่ใจดีและแสนดี ฉันคิดเช่นนั้น"

hi "ขอบใจ"

hi "สรุปคือเพราะฉันเป็นพวกกับเธอแล้ว วันนี้จะให้ไปช่วยใช่มั้ย"

show misha hips_grin
with charachange

mi "ช่าย~!"

hi "หลังเลิกเรียนเหรอ"

show misha sign_smile
with charachange

mi "ไม่ ๆ ๆ ~! ตอนนี้!"

hi "ตอนนี้อะนะ แล้วจะโดดเรียนอีกเหรอ"

show shizu adjust_smug
with charachange

shi "…"

show misha cross_laugh
with charachange

mi "ฮ่าฮ่าฮ่า~! เพื่อผลประโยชน์ส่วนรวม เราจึงสละคาบคณิต แล้วก็อาจจะคาบสังคมด้วย~!"

hi "อืม ก็ได้แหละมั้ง"

show shizu behind_smile
with charachange

shi "…"

show misha sign_smile
with charachange

mi "เยี่ยมเลยฮิจัง~! นายบอกเองนะว่า “จะช่วยก็ได้~” ว่างั้นใช่มั้ย~"

hi "อืม"

"น้ำเสียงนั่น…ว่าแล้วก็ไม่น่าพูดอย่างนั้นเลย"

show shizu basic_normal2
with charachange

shi "…"

show misha hips_grin
with charachange

mi "โอเค~! งั้นพร้อมหรือยัง ไปที่ห้องสภาฯ ด้วยกันได้นะ~!"

hi "ไม่อะ เดี๋ยวเธอก็ใช้ให้ฉันขนของหรืออะไรอีก"

show shizu adjust_happy
with charachange

shi "…"

show misha perky_smile
with charachange

mi "พูดบ้า ๆ น่าฮิจัง"

show misha hips_smile
with charachange

mi "เรายังไม่เคยเดินไปโรงเรียนด้วยกันเลยนะฮิจัง~"

"ฉันกำลังจะถามว่าทำไมแล้วก็นึกขึ้นได้ ทั้งสองคนมองว่าฉันเป็นเพื่อนอย่างที่มิช่าเคยพูด แล้วอยากสนิทขึ้นอีกด้วยซ้ำ"

"แปลก เพราะฉันไม่เคยมองอย่างนั้นเลย คนที่เคยเจอมาตลอดสัปดาห์นี้ก็ด้วย จะง่ายขนาดนั้นเลยเหรอ"

"เป็นเพื่อนกันง่าย ๆ เลย…"

hi "โอเค งั้นก็ไปกัน"

show shizu behind_smile
with charachange

"ชิซูเนะยิ้มเจ้าเล่ห์แล้วเอามือไพล่หลังไว้"

show misha hips_grin
with charachange

mi "ฮ่าฮ่าฮ่า~! เยี่ยมเลยฮิจัง~! โอเค ๆ แต่ก่อนอื่น~! ความคิดนายน่าสนใจดี ชิจังชอบมากเลยละ…เพราะงั้น~!\nมาเล่นเกมกัน!"

hi "ไม่นะ"

show misha hips_smile
with charachange

mi "ตอนนี้ชิจังถือแบงก์พันเยนไว้ในมืออยู่ละฮิจัง~! ถ้านายเดาถูกว่าข้างไหนก็เอาไปเลย! แต่ถ้าตอบผิด…"

show misha hips_grin
with charachange

mi "นายต้องขนหนังสือของพวกเราไปโรงเรียนให้ด้วยนะ~! ใช่มั้ยชิจัง~ ช่าย~!"

"เธอกับชิซูเนะพยักหน้าให้กัน"

show misha sign_smile
with charachange

mi "เอาละฮิจัง~! เตรียมตัว~!"

stop music fadeout 7.0

scene bg school_courtyard
with shorttimeskip

"ฉันแบกกระเป๋ามาสามใบพลางคิดถึงสิ่งที่รออยู่ในวันนี้ของฉัน ของพวกเรา"

"พอจะเห็นนักเรียนเดินไปมาตามลานหน้าอาคารบ้าง คงจะเตรียมงานของตัวเองกันอยู่"

"งานเทศกาลก็เตรียมแทบใกล้จะเสร็จแล้ว ซึ่งแปลว่ามีอยู่สองสาเหตุที่พอจะเป็นไปได้ที่ต้องขอให้ฉันช่วย"

"หนึ่งคือเหลือแค่งานเล็ก ๆ น้อย ๆ แล้วอยากให้ช่วยเก็บงานส่วนที่เป็นการตรวจขั้นสุดท้ายสุดซ้ำซากที่พวกเธอต้องทำ"

"สองคือมีงานเหลืออีกเป็นพันแล้วชิซูเนะทำนิ่งไปทั้งที่ดินที่พอกหางหมูกำลังจะกลิ้งมาทับพวกเราจนตายกันหมด"



label th_A26d:

play music music_rain fadein 4.0

"ถึงงั้น คราวนี้มันก็ล้ำเส้นเกินไปแล้ว สอดรู้จนน่ารำคาญ"

hi "ไม่มีอะไรหรอก"

show misha perky_smile
with charachange

mi "จริงเหรอ~ ฮิจัง แต่ที่เห็นนี่มันมีแน่ ๆ เลยนะ"

show shizu adjust_smug
with charachange

shi "…"

show misha hips_smile
with charachange

mi "ขวดเยอะเลยใช่มั้ย~ ช่าย~! ของพวกนั้นคืออะไรเหรอฮิจัง"

hi "ของนิดหน่อยน่ะ"

show shizu basic_normal2
with charachange

shi "…"

show misha perky_confused
with charachange

mi "เยอะขนาดนั้นมันไม่น่าใช่ “ของนิดหน่อย” แล้วนะ…"

"จะว่าพวกเธอที่เป็นอย่างนี้ก็ว่าไม่ได้ มิช่าก็แค่พูดแทนชิซูเนะ ส่วนชิซูเนะก็เป็นคนอยากรู้อยากเห็นอยู่แล้ว แต่ก็อยากให้\nสองคนนี้เลิกตื๊อแล้วรู้ตัวที่จะสื่อสักที แต่มิช่าก็จะไม่เข้าใจ ส่วนชิซูเนะก็ไม่มีทางที่จะรับรู้ได้"

"และเพราะเช่นนั้นทั้งสองคนจึงยังซักไซ้ไม่เลิก"

hi "ไม่ใช่เรื่องของพวกเธอสักหน่อย"

hi "ไปได้แล้ว ห้องพักเขาต้องการความเป็นส่วนตัวนะ"

"ดูเหมือนชิซูเนะจะเห็นว่าเป็นคำท้า"

show shizu behind_frown
with charachange

shi "…"

show misha hips_frown
with charachange

mi "พูดงี้หมายความว่าไงฮิจัง เวลาคนเราเห็นอะไรที่น่าสนใจก็ต้องถามว่ามันคืออะไรโดยสัญชาตญาณอยู่แล้วไม่ใช่เหรอ\nแล้วมันไม่ดีตรงไหนล่ะ"

hi "ก็บอกเมื่อกี้แล้วไงว่ามันไม่มีอะไร"

show misha perky_confused
with charachange

mi "ฮิจัง ฉันว่าชิจังเขาแค่เป็นห่วงนะ"

hi "อะไรจะอยู่ในห้องฉันมันก็ไม่เกี่ยวกับพวกเธอ แค่นั้นแหละ"

show misha sign_confused
with charachange

mi "แต่ว่า…"

hi "โถไอ้! ฉันละอยากให้พวกเธอสองคนเลิกทำอะไรเป็นเล่นตลอดสักที บางทีมันก็ไม่สนุกเลยนะ รู้ตัวใช่มั้ย"

"ฉันพูดไปแรงกว่าที่คิดเอาไว้ แทบจะตะคอกใส่หน้ามิช่าด้วยซ้ำ เธอผงะไปโดยมือที่ทำภาษามือยังค้างอยู่ แม้แต่ชิซูเนะ\nยังตอบสนองแม้ว่าเธอจะไม่ได้ยิน"

stop music fadeout 6.0

"สีหน้าที่โกรธของฉันคงบอกอะไรที่อยากบอกไปหมดแล้วละนะ"

show misha perky_sad
show shizu behind_blank
with charachange

"พอมิช่าค่อย ๆ แปลจนจบแล้วทั้งสองคนก็มองหน้ากันด้วยความรู้สึกเสียใจ"

show shizu behind_sad
with charachange

shi "…"

mi "โอเค ฮิจัง พวกเราจะไม่รบกวนแล้ว"

"เป็นครั้งแรกที่ได้ยินมิช่าพูดโดยไม่มีน้ำเสียงขึ้นลงอย่างเคยจนฟังดูแปร่งหู นึกแล้วก็อยากขอโทษ ทว่าพวกเธอก็หันหลัง\nจากไปแล้ว"

"ยิ่งเมื่อความเงียบมาเยือนยิ่งทำให้ฉันรู้สึกผิดกับสิ่งที่พูดออกไป"

hide shizu
hide misha
with charaexit

"สองสาวออกไปอย่างเงียบเชียบ ฉันยืนนิ่งอยู่ในห้องพักหนึ่งแล้วแต่งตัวตามพวกเธอออกไป"



label th_A26e:

show kenji tsun_close
with charachange

ke "เออ ๆ เอาเหอะ"

stop music fadeout 2.0

hide kenji
with charaexit

"เขาปราดเข้าถ้ำตัวเองไปแล้วปล่อยให้ฉันไปเรียน"

#*************************

label th_A27:

scene bg school_hallway3
with shorttimeskip

"โถงทางเดินนั้นเงียบงันไม่ต่างจากที่ลานหน้าอาคาร ซึ่งก็ปกติเพราะทุกคนเรียนอยู่ ฉันเคาะประตูห้อง 3-3 เบา ๆ \nแล้วเปิดประตูเข้าไปหลังมุโต้เรียกกลับจากอีกฟากประตู"

scene bg school_scienceroom
with locationchange

hi "ขอโทษที่มาสายครับ"

"สายตาสิบห้าคู่จับจ้องมาที่ฉัน"

show muto irritated at center
with charaenter

mu "อรุณสวัสดิ์ นากาอิ"

"มุโต้ดูจะยังงงงันเล็กน้อยที่ฉันเข้าห้องสาย คล้ายว่าฉันไปขัดจังหวะของเขา"

"ซึ่งพอนึกถึงที่เขาชอบพูดยืดยาวเวลาสอนแล้วก็คงเป็นอย่างนั้น"

"ฉันยื่นกระดาษที่ได้มาจากคุณพยาบาลให้ มุโต้พยักหน้ารับไปแล้วกวาดตาอ่าน"

show muto normal
with charachange

"เขายักคิ้วแล้วมองฉันด้วยสีหน้าเคร่งเครียดแต่ไม่พูดอะไร เพียงพยักหน้าให้อย่างหนักแน่น"

"ฉันยักไหล่แล้วกลับไปนั่งที่ตามที่เขาบุ้ยใบ้ให้ไป"


label th_A27a:

scene bg school_scienceroom
show muto normal at center
with None

#so if you have joined SC, you see this
hide muto
with charaexit

"มีเพียงสายตาสองคู่ที่ยังจับจ้องฉันที่เดินมานั่งที่"

"ฉันไม่แปลกใจเลยแม้แต่น้อยที่หลังจากหย่อนก้นได้สิบห้าวินาทีก็มีปลายเล็บของมิช่ามาสะกิด"

show misha perky_smile_close at offscreenleft
with None

show bg school_scienceroom at bgright
show misha perky_smile_close  at Transform(xalign=-0.3)
with charamove

play music music_another fadein 2.0

mi "นี่! ไปไหนมา"

hi "ไม่ใช่เรื่องของเธอ"

"คงจะเป็นคำตอบที่แย่ที่สุดแล้ว เพราะถ้าตอบงั้นก็ยิ่งชวนให้สงสัยอีก แต่ตอนนี้ก็ไม่มีแรงจะเล่าอะไรแก้ตัวแล้ว"

show misha perky_confused_close
with charachange

show bg school_scienceroom at center
show misha perky_confused_close at offscreenleft
with charamove

"แต่มิช่าก็ยอมถอย วันนี้ยอมง่ายผิดคาด"

"…"

"แต่ไม่ถึงนาทีเธอก็ใช้นิ้วสะกิดอีก"

show misha hips_grin_close
with None

show bg school_scienceroom at bgright
show misha hips_grin_close  at Transform(xalign=-0.3)
with charamove

mi "บอกมาเถอะน่า! ชิจังก็อยากรู้มากด้วย!"

"ฉันคงฝันมากไปสินะ เธอหันไปคุยกับชิซูเนะ คงจะหาทางหลอกล่อให้ฉันเล่าให้ได้"

hi "ไม่"

show misha perky_sad_close
with charachange

show bg school_scienceroom at center
show misha perky_sad_close at offscreenleft
with charamove

"เธอล่าถอยไปปรึกษากันอีกครั้ง"

show misha sign_smile_close
with None

show bg school_scienceroom at bgright
show misha sign_smile_close  at Transform(xalign=-0.3)
with charamove

label th_choiceA27:
menu:
    with menueffect

    mi "ในฐานะสภานักเรียน หน้าที่ของนายคือการบอกว่าทำไมนายถึงโดดเรียนนะ! โดยเฉพาะถ้าเป็นเรื่องที่สนุกสนุ๊กสนุกน่ะ~!"

    "อืม ไปห้องพยาบาลมา สนุกสนุ๊กสนุกมากเลย…":
    #to A27b
        return m1

    "คือยังไม่อยากคุยเรื่องนี้ โอเคนะ":
    #to A27c
        return m2

label th_A27b:

stop music fadeout 4.0

"ให้ตายเถอะแม่ง ไม่รู้จักหยุดบ้างเลยหรือไง"

hi "เออ ๆ ก็ได้ สนุกมากจะบอกให้"

hi "เช้านี้มาถึงก็หัวใจวายเลย แถมได้ไปเล่นสนุกกับคุณพยาบาลอยู่สองสามชั่วโมงอีกต่างหาก"

hi "เป็นเช้าที่ดีที่สุดในชีวิตเลยบอกตรง ๆ "

"ฉันทำน้ำเสียงล้อเธอที่ชอบพูดเป็นทำนองแบบเสียงเบาไม่ให้คนอื่นได้ยินโดยมีความกระแทกกระทั้นอยู่ในที"

show misha perky_confused_close
with charachange

mi "ฮิจัง นายอะไรนะ จริงเหรอเนี่ย"

hi "พอเหอะ ก็ตามนั้นแหละ"

show misha perky_sad_close
with charachange

mi "แต่ว่าฮิจัง นี่เรื่องสำคัญนะ!"

hi "ไม่ ปล่อยฉันไปสักที แล้วนี่ก็กำลังเรียนอยู่ด้วย"

show misha sign_sad_close
with charachange

mi "แต่ว่า ฮิจัง!"

"มิช่าดูจะเป็นห่วง ไม่ก็กำลังร้อนใจ นี่รู้ตัวมั้ยเนี่ยว่าการทำตัวขี้เสือกแบบนี้มันใช้ไม่ได้"

"…"

"ฉันปล่อยให้เธอสำนึกกับการกระทำของตัวเองสักพักแล้วตอบ ซึ่งอาจจะส่งไม่ถึงชิซูเนะด้วย แต่ช่างมัน"

hi "ไสหัวไปเลยมิช่า"

hi "แล้วบอกต่อให้ชิซูเนะด้วย"

"ฉันรู้สึกผิดขึ้นมาทันที่ที่คำพูดหลุดออกจากปากไป แต่จะให้ถอนคำพูดก็คงไม่ได้แล้ว"

show misha perky_sad_close
with charachange

show bg school_scienceroom at center
show misha perky_sad_close at offscreenleft
with charamove

hide misha
with None

"แอบแปลกใจเหมือนกันที่มิช่าเงียบไปจริง ๆ แต่ฉันก็ไม่ได้ดูว่าเธอส่งต่อที่ฉันพูดให้ชิซูเนะด้วยหรือเปล่า ซึ่งจะบอก\nหรือไม่บอกก็ไม่สำคัญหรอก"

"มุโต้คุยเรื่อยเปื่อยถึงงานเทศกาลที่จะมาถึงในอีกสองวันนี้แล้วเลิกชั้น"

#to A29, needs a conditional about Emi making Hisao feel better



label th_A27c:

hi "ยอมแพ้เถอะน่า ไม่บอกหรอก"

show misha hips_grin_close
with charachange

mi "เหรอ~"

hi "อืม"

show misha perky_confused_close
with charachange

"เธอคิดอยู่ครู่หนึ่ง"

show misha hips_frown_close
with charachange

mi "ฮิจังขี้เหนียว~!"

"น้ำเสียงของเธอดูงอนและหงอยไป"

show bg school_scienceroom at center
show misha hips_frown_close at offscreenleft
with charamove

"เธอล่าถอยไปปรึกษาคู่หูของเธอที่เป็นตัวขับเคลื่อนทางสมองของมิตรภาพนี้แล้วกลับมา"

show misha hips_smile_close
with None

show bg school_scienceroom at bgright
show misha hips_smile_close  at Transform(xalign=-0.3)
with charamove

mi "ฉันว่าเราควรไปกินข้าวเที่ยงแล้วคุยเรื่องนี้ด้วยกัน…ชิจังว่างั้น"

show misha hips_grin_close
with charachange

mi "เดี๋ยวพวกเราเลี้ยงเอง"

show misha sign_smile_close
with charachange

mi "อีกอย่าง นายต้องมาชดเชยค่าที่นายไม่ได้มาช่วยงานเราเช้านี้ด้วย~!"

"คนอื่นในห้องเริ่มหันมอง คงเพราะมิช่าโน้มตัวข้ามโต๊ะมาจนหัวจะชนกับฉันอยู่แล้ว ผมม้วนของเธอถูกเข้ากับคอของฉัน"

"มีกลิ่นแชมพูกับกลิ่นอะไรสักอย่างที่เธอใช้ให้ผมอยู่ทรงอย่างนั้น"

"เหมือนผู้หญิงที่นั่งตรงหน้าฉันจะเงี่ยหูฟังอยู่ หวังว่าจะไม่มีใครเข้าใจผิดอะไรไปนะ ถึงจะไม่รู้ก็เถอะว่ามีอะไรให้เข้าใจผิด\nได้อีก"

"โชคดีที่ตอนนี้มุโต้ยังไม่รู้ตัว หรือไม่ก็จงใจเมินมิช่า"

"คราวนี้คงหนีไม่ได้จริง ๆ สินะ"



label th_choice2A27:
menu:
    with menueffect

    "รับปากไว้แล้วด้วยว่าจะไปกินข้าวเที่ยงกับเอมิ แต่จะแยกร่างไปทั้งสองที่พร้อมกันก็ไม่ได้"

    "ไปกินข้าวเที่ยงกับเอมิกับเพื่อนของเธอแล้วกัน":
        return m1

    "ไปกับชิซูเนะแล้วกัน ก็เข้าสภานักเรียนแล้วนี่นะ":
        return m2


label th_A27h:
#lol label order

hi "โทษที แต่ไปไม่ได้แล้วละ พอดีรับปากกับคนอื่นไว้แล้วว่าจะกินข้าวเที่ยงด้วยน่ะ"

show misha perky_confused_close
with charachange

mi "หืมมม ใครเหรอ ผู้หญิงหรือเปล่า~"

hi "อืม…"

show misha hips_grin_close
with charachange

"เสียงเธอหัวเราคิกคักบีบฉันให้ต้องพูดอะไรต่อเพื่อไม่ให้เธอเข้าใจผิด"

hi "ไม่ใช่อย่างนั้นนะ! เรื่องมัน…ซับซ้อนนิดหน่อย"

show misha perky_smile_close
with charachange

"ซับซ้อน…ใช่ นั่นแหละชีวิตฉัน ถึงจะกลับมาใช้ชีวิตตามปกติในรั้วโรงเรียนได้แล้วก็เถอะ"

"ชีวิตที่สองนี้ต้องมองจากมุมใหม่ จากมุมมองของตัวฉันคนใหม่"

"ตัวฉันที่อยู่กับใจพัง ๆ"

hi "แล้วก็ ฉันไม่รู้นะว่าจะมาที่สภานักเรียนได้มั้ย"

hi "ก็ดูก่อนแหละ ช่วงนี้มีอะไรอย่างอื่นให้สนใจอยู่น่ะ"

"ใช่แล้ว ฉันต้องจัดลำดับความสำคัญใหม่ ตั้งแต่ที่พยาบาลคุยกับฉันเมื่อเช้าฉันก็คิดมาตลอด ฉันจะทำเหมือนว่าฉัน\nยังสบายดีไม่เป็นโรคนี้ไม่ได้"

"ฉันนึกแปลกใจที่คิดได้เป็นเรื่องเป็นราวขนาดนี้ แต่ตอนนี้ก็ปล่อยตัวตามน้ำไปก่อน"

hi "ฉันสัญญาว่าเดี๋ยวจะเล่าให้ละเอียดทีหลัง แต่ไม่ใช่ตอนนี้ นะ? ฝากบอกชิซูเนะด้วยว่าขอโทษที่ปฏิเสธ"

show misha perky_confused_close
with charachange

mi "ถ้าฮิจังว่างั้นแล้วก็ได้"

"น้ำเสียงเธอดูตกใจและจริงจังซึ่งฉันน่าจะไม่เคยได้ยินมาก่อน"

show bg school_scienceroom at center
show misha perky_confused_close at offscreenleft
with charamove

hide misha
with None

stop music fadeout 3.0

"โชคดีที่มิช่าเข้าใจว่าฉันจริงจัง ครั้งนี้ลงตัวที่ฉันบอกอะไรให้ชัดเจนได้พอดีจนแม้แต่เธอยังเข้าใจ เธอล่าถอยกลับไปแล้ว\nแปลที่คุยกันเมื่อกี้ให้ชิซูเนะ"

"หลังจากนั้นทั้งสองคนก็ไม่คุยกับฉันอีก"



label th_A27i:

hi "ไปก็ได้ แต่ภายในคาบนี้ห้ามมากวนอีกนะ"

show misha hips_grin_close
with charachange

mi "ได้เลยฮิจัง ตกลงตามนั้น"

stop music fadeout 2.0

show bg school_scienceroom at center
show misha hips_grin_close at offscreenleft
with charamove

scene bg school_scienceroom
with shorttimeskip

play sound sfx_normalbell

with Pause(7.0)

play ambient sfx_crowd_indoors fadein 0.3

scene bg school_hallway3
show crowd
with locationchange

"ระหว่างที่เดินไปห้องสภานักเรียนก็พอจะเห็นนักเรียนเดินไปมาตามโถงทางเดินบ้าง คงจะเตรียมงานของตัวเองกันอยู่"

"งานเทศกาลก็เตรียมแทบใกล้จะเสร็จแล้ว ซึ่งแปลว่ามีอยู่สองสาเหตุที่พอจะเป็นไปได้ที่ต้องขอให้ฉันช่วย"

"หนึ่งคือเหลือแค่งานเล็ก ๆ น้อย ๆ แล้วอยากให้ช่วยเก็บงานส่วนที่เป็นการตรวจขั้นสุดท้ายสุดซ้ำซากที่พวกเธอต้องทำ"

"สองคือมีงานเหลืออีกเป็นพันแล้วชิซูเนะทำนิ่งไปทั้งที่ดินที่พอกหางหมูกำลังจะกลิ้งมาทับพวกเราจนตายกันหมด"

stop ambient fadeout 1.0


label th_A27d:

#if you are not SC member and did not get a heartattack OR if you blew Shizune and Misha off in A26, you come straight to this, the day begins with it in some cases.

scene bg school_scienceroom
with locationskip

"คราวนี้ฉันไม่ได้มาเข้าห้องเป็นคนแรก"

"ดูเหมือนทุกคนมากันเกือบครบแล้ว ฉันพอจะจำหน้าคนในห้องส่วนใหญ่ได้บ้าง ถึงจะจำชื่อไม่ได้ก็เถอะ"



label th_A27e:

#If you have not joined SC, you see this instead of A27a, this is also a followup on A27e

scene bg school_scienceroom
with shorttimeskip

play music music_normal fadein 3.0

"คาบเรียนดำเนินไปอย่างเอื่อยเฉื่อย ฉันว่าฉันพอจะเข้ากับชีวิตที่โรงเรียนนี้ได้แล้ว"

"ฉันเลิกคร่ำเครียดกับการจดสิ่งที่เรียนกับการจดจ่อจนเกินไปแล้ว วันแรก ๆ ที่มาฉันยังค่อนข้างเกร็ง"

"มุโต้เลิกคาบที่เขากำลังสอนเรื่องไฟฟ้าอยู่ให้เร็วกว่าปกติ แต่ก็พูดเรื่องงานโรงเรียนต่อทันที"

show muto normal at center
with charaenter

mu "เอาละ อย่างที่รู้กันว่างานโรงเรียนจะจัดมะรืนนี้แล้ว หวังว่างานปีนี้ของทุกคนจะประสบความสำเร็จนะ"

show muto smile
with charachange

mu "ขอให้สนุกนะ แต่เมื่อถึงวันอาทิตย์แล้วก็ขออย่าลืมความหมายของงานเทศกาลนี้…"

mi "เกมงานวัดและของทอด!"

"ทั้งห้องหัวเราะครืน และฉันก็ผสมโรงด้วย"

show muto irritated
with charachange

mu "ก็ถูก ขอบคุณมาก มิคาโดะ"

show muto normal
with charachange

mu "แต่สิ่งที่ครูอยากบอกคือ—{w=.5}{nw}"

play sound sfx_normalbell

"ส่วนที่เหลือของประโยคเขาถูกเสียงระฆังพักเที่ยงกลบ ทุกคนก็เริ่มเก็บข้าวของกัน"

"มุโต้ใช้ความคิดอยู่พักหนึ่ง แต่เมื่อไม่มีใครสนใจแล้วเขาจึงยอมแพ้และนั่งลง"

stop music fadeout 2.0

scene bg school_hallway3
show crowd
with locationchange

play ambient sfx_crowd_indoors fadein 0.3

"ที่โถงทางเดินคนแน่นขนัด…แน่นเท่าที่โถงทางเดินโรงเรียนจะแน่นได้ นักเรียนส่วนใหญ่ดูจะตรงไปที่โรงอาหารกัน"


#to A29



label th_A27f:

scene bg school_scienceroom
with shorttimeskip

stop music fadeout 2.0

"ตลอดช่วงเช้านั้นมิช่าไม่กวนฉันอีก ซึ่งแปลว่ารวมถึงชิซูเนะด้วย"

play sound sfx_normalbell

"เมื่อระฆังดังฉันก็เดินออกจากห้องโดยไม่แม้แต่เหลียวมองทั้งสองคน"

scene bg school_hallway3
show crowd
with locationchange

play ambient sfx_crowd_indoors fadein 0.3

"ที่โถงทางเดินคนแน่นขนัด…แน่นเท่าที่โถงทางเดินโรงเรียนจะแน่นได้ นักเรียนส่วนใหญ่ดูจะตรงไปที่โรงอาหารกัน"



#***************

label th_A28:

scene bg school_council
with locationchange

show misha perky_smile at twoleft
show shizu behind_smile at tworight
with charaenter

"เมื่อเข้ามาในห้องและมองไปรอบ ๆ แล้วก็เห็นว่าไม่มีใคร"

hi "คงเหลืองานไม่เยอะแล้วสิเนี่ย ไม่เห็นมีใครอะไรเลย"

show misha sign_smile
with charachange

mi "มันก็เป็นงี้ตลอดแหละฮิจัง~!"

"เท่านี้ก็เป็นการยืนยันสิ่งที่ฉันสงสัยแต่ฟันธงไม่ได้มาตลอด เรื่องที่ว่าชิซูเนะและมิช่าคือ{b}ทั้ง{/b}สภานักเรียน"

hi "โห่ สรุปทั้งสภาก็มีแค่เธอสองคนจริง ๆ "

play music music_ease fadein 4.0

show misha hips_grin
show shizu cross_wut
with charachange

"ดูเหมือนชิซูเนะยังเลือกไม่ถูกว่าจะรู้สึกอับอายหรือโกรธจนระเบิดลงตอนนี้เลยดี มิช่าก็เลือกไม่ถูกพอกันว่าจะขำ\nหรือเข้าไปห้ามเธอดี"

show shizu behind_frustrated
with charachange

shi "…"

show misha sign_smile
with charachange

mi "เอาละ ๆ ฮิจัง นายต้องมีความสุขแน่ที่งานเราจะเยอะเพราะมีกันแค่สามคนน่ะ! เยอะ~! มาก~ ม๊าก~ มาก~…"

hi "ไม่เห็นจะมีความสุขตรงไหน"

show shizu adjust_happy
with charachange

"แต่เหมือนว่าชิซูเนะจะมีความสุขมาก ๆ "

show misha cross_laugh
with charachange

mi "วะฮ่าฮ่า~!"

show misha hips_grin
with charachange

mi "หยอกน่า!"

label th_A28a:
#you see this if you have been spending the morning in the infirmary

scene bg school_council
with shorttimeskip

"งานก็เป็นการจัดแจงกับตรวจสอบเอกสารสำหรับการจัดงานอย่างงานเทศกาลโรงเรียน ซึ่งเยอะพอตัว"

"กระบวนการอะไรพวกนี้เป็นเรื่องที่ไม่เข้าใจเลยจริง ๆ "

play sound sfx_normalbell

"แต่พวกเราก็ทำเสร็จทันก่อนระฆังพักเที่ยงดังพอดี"

show misha hips_grin at twoleft
show shizu adjust_happy at tworight
with charaenter

mi "โอเค~ งานเสร็จแล้วก็พักกันสักหน่อยก็ได้! แต่อย่าพักมากละ ตอนบ่ายยังเหลืองานอีกเยอะ~!"

label th_A28b:

$ renpy.music.play(music_ease, fadein=4.0, if_changed=True)

show shizu behind_smile
with charachange

shi "…"

show misha sign_smile
with charachange

mi "เยอะขนาดนั้นเลยแหละฮิจัง~ เพราะงั้น~ มากินข้าวเที่ยงอร่อย ๆ กันก่อนดีกว่า"

show misha cross_laugh
with charachange

mi "ฮ่าฮ่าฮ่า~!"

"อยู่ ๆ ทั้งคู่ก็ควักกล่องพลาสติกออกมาจากไหนก็ไม่รู้เป็นชุด"

show misha hips_grin
with charachange

mi "ฮืม~ ฮื้ม~… ไก่ชุบแป้งทอด พร้อมมะเขือเทศกับถั่วงอกหัวโตละ~! คงอร่อยน่าดูเลยเนอะฮิจัง"

mi "ไก่ก็เพิ่งทอดสด ๆ มาเมื่อเช้านี้ ยังอุ่นอยู่เลย มามามา มากิน~!"

"ฉันหยิบมากล่องหนึ่งแล้วเปิดออกดู หน้าตาใช้ได้ กลิ่นก็หอม แถมตอนนี้ก็หิวแล้วด้วย"

hi "โห ดูน่าอร่อยแฮะ ไปซื้อที่ไหนมาเหรอ"

show shizu basic_normal
with charachange

shi "…"

show misha hips_smile
with charachange

mi "ไม่สำคัญหรอกน่าฮิจัง!"

show misha sign_smile
with charachange

mi "ที่จริงในงานจะมีแผงขายข้าวเที่ยงด้วย แต่อยู่ ๆ คนที่รับผิดชอบก็มาบอกว่าทำไม่ได้แล้ว ชิจังเลยบอก “เสียดายแฮะ\nอุตส่าห์ล่อให้ฮิซาโอะมาทำได้แล้วแท้ ๆ "

hi "เฮ้ย อะไรเนี่ย…"

show misha hips_grin
with charachange

mi "…ชิจังก็เลย~! อยากลองดูว่าจะมาทำแทนได้มั้ย แต่แล้วก็ยอมแพ้ เนอะ ชิจัง~"

show shizu basic_angry
with charachange

"ชิซูเนะทำแก้มป่องมองมิช่าด้วยความไม่พอใจ รู้สึกว่าเป็นเรื่องที่ฉันไม่ควรได้ยินยังไงไม่รู้"

hi "อันนี้คือที่ลองทำเหรอ"

show shizu behind_frown
with charachange

shi "…"

show misha sign_smile
with charachange

mi "ฉันกินด้วยนะฮิจัง~!"

show misha hips_grin
with charachange

mi "ชิจังก็ด้วย~!"

"ไม่เห็นมีคำตอบเลยเฮ้ย!"

"แต่ฉันก็หักตะเกียบที่ชิซูเนะยื่นให้แล้วคีบไก่ทอดเข้าปากกินทันที"

hi "อร่อยนะเนี่ย ไม่ยักรู้ว่าชิซูเนะทำกับข้าวเก่งขนาดนี้"

show shizu basic_frown
with charachange

"ชิซูเนะวางตะเกียบลงแล้วทำภาษามือสั้น ๆ ให้มิช่าที่ดูจะกลืนชิ้นไก่ทอดด้วยความยากลำบากก่อนที่จะพูดแปลให้"

show misha sign_smile
with charachange

mi "ฮิจัง~! ข้าวเต็มปากอยู่ก็อย่าเพิ่งพูดสิ~!"

hi "ฉันก็ไม่ได้อยากทำสักหน่อย แต่แหม มาสอนเรื่องแบบนี้นี่เหมือนแม่เลย…"

show shizu behind_frown
with charachange

shi "…"

show misha hips_frown
with charachange

mi "ก็แค่จะบอกว่า~! กินให้มันดี ๆ ยังไม่ได้เลยฮิจังน่ะ~!"

show misha perky_sad
with charachange

"รู้สึกเหมือนตกอยู่ในสภาพหมากอับเลยแฮะ ฉันก็กินไม่ได้เพราะต้องคุยกับชิซูเนะ เธอก็กินไม่ได้เพราะต้องว่าฉันเรื่องที่\nไม่มีมารยาทในการกิน ส่วนมิช่าที่โดนหางเลขไปด้วยก็เหมือนกันและดูจะหน่ายใจที่สุดที่เรื่องเป็นแบบนี้"

show shizu behind_blank
show misha perky_smile
with charachange

"แต่นั่นแหละ ข้าวก็จะเย็นชืดไปทุกที แถมไม่ได้มาในสภาพสด ๆ ร้อน ๆ ขนาดนั้นอยู่แล้วด้วย สุดท้ายพอพวกเรารู้ตัว\nก็ยอมจบเรื่องแล้วกินตามปกติ"

play sound sfx_warningbell

"ระฆังดังได้สักพักแล้ว แต่มิช่าก็ไม่ได้บอกชิซูเนะ สงสัยคงกะจะโดดเรียนแล้วแช่อยู่ที่นี่ทั้งบ่ายอีกแน่ ๆ "

show shizu adjust_smug
with charachange

shi "…"

show misha sign_smile
with charachange

mi "ฮิจัง คิดไว้หรือยังว่าจะทำอะไรในงานเทศกาลน่ะ"

hi "ไม่อะ ไม่ได้คิด เพิ่งมาได้สัปดาห์เดียวจะให้ทำอะไรได้"

show misha cross_laugh
with charachange

mi "วะฮ่าฮ่า~! ฮิจัง นายช่วยพวกเรามาตั้งเยอะ อย่าด้อยค่าตัวเองไปเลยน่า!"

hi "โอเค"

show shizu basic_angry
with charachange

shi "…"

show misha hips_frown
with charachange

mi "นี่จริงจังนะ~!"

hi "โอเค!"

"สองคนนี้ดูจะจู้จี้กับอะไรแปลก ๆ ตลอด"

show shizu adjust_happy
with charachange

shi "…"

show misha hips_smile
with charachange

mi "แต่นายจะมางานอยู่ใช่มั้ยฮิจัง อย่างน้อยก็มาดูว่าพวกเราทำอะไรลุ–ล่วง…? ไปแล้วบ้าง คนเราทำอะไรแล้วก็ต้อง\nมาดูผลงานตัวเองให้เข้าใจจริง ๆ ฉันเชื่ออย่างนั้นนะ~! ฮิจังก็ด้วย!"

show misha perky_smile
with charachange

mi "ฮิจัง นายต้องมาให้ได้เลยนะ~! ถ้านายไม่ได้มีแพลนอะไรก็มาด้วยกันยังได้เลย~!"

show shizu adjust_blush
with charachange

hi "ให้ฉันช่วยมั้ยล่ะ มีอะไรให้ช่วยได้ก็จะช่วย ฉันได้หมด"

"ฉันรู้สึกสบายใจขึ้นกว่าเมื่อครู่ ทุกความกังวลและความกลัวหายไปหมด พอได้มาสนุกอยู่กับชิซูเนะอย่างนี้แล้วก็ลืม\nความไม่สบายใจที่เกิดตั้งแต่เมื่อเช้าจนตอนนี้ไปจนหมด"

"สนุกอยู่กับชิซูเนะ…อาจจะเป็นคำที่ดูไม่ค่อยลงตัวกันเท่าไหร่ แต่พอมาคิดดูแล้วสองสามวันที่ผ่านมาที่ได้อยู่กับชิซูเนะ\nและมิช่าก็รู้สึกเพลินดี แม้จะมีเรื่องอื่นเข้ามาก็ตาม"

"ไหน ๆ ก็จะไปด้วยกันอยู่แล้ว อยู่ต่อสักหน่อยแล้วกัน คงสนุกกว่านั่งอยู่ในห้องเรียนด้วย"

show shizu behind_blank
with charachange

shi "…"

show misha hips_smile
with charachange

mi "จริงเหรอฮิจัง ก็ได้~! งั้นจะถือว่าเป็นค่าตอบแทนที่เลี้ยงข้าวเที่ยงฟรีแล้วกัน~!"

show misha cross_laugh
with charachange

mi "เยี่ยม เยี่ยมจริง ๆ ~ เยี่ยมจริง ๆ ~ เยี่ยมจริง ๆ ~! ชิจังก็กะว่าจะเอามาทวงอยู่แล้วอะนะ! อะฮ่าฮ่าฮ่า~!\nวะฮ่าฮ่าฮ่าฮ่าฮ่าฮ่า~!"

"แล้วมันจะนับว่าข้าวเที่ยงฟรียังไง ปกติก็คงโกรธหรือหงุดหงิดนิดหน่อย แต่เมื่อกี้อารมณ์ดีขึ้นแล้ว หยวน ๆ ไปแล้วกัน"

"ช่วยงานคราวนี้เป็นงานให้ปั๊มเอกสารกับถ่ายเอกสารรายงานงบประมาณห้าสิบฉบับที่รู้สึกเหมือนจะได้ถ่ายแต่ละฉบับ\nมาเป็นแสนชุด"

"งานไม่ได้ยาก แต่น่าเบื่อเอามาก ๆ และมิช่าบอกว่าพวกนี้เป็นงานที่ง่ายที่สุดที่พวกเธอทำ"

"รู้สึกตัวเองยิ่งล้าไปเรื่อย ๆ จนความรู้สึกอยากกลับไปเข้าเรียนก็หดหายตาม ซึ่งยิ่งแย่ไปอีกเพราะยิ่งได้อยู่นอกห้อง\nมากเท่าไหร่ก็ยิ่งจะลากตัวเองให้กลับไปนั่งเรียนได้ยากขึ้นเท่านั้น"

"สองคนนี้เป็นตัวอย่างที่ไม่ดีพาฉันเสียคน แต่ก็ใช่ว่าฉันจะคิดมากอะไรอยู่แล้ว ยังไงก็คงไม่มีใครนับถือพวกเธอเท่าไหร่ด้วย\nแต่อย่างน้อยมันก็คือสิ่งที่ควรทำน่ะนะ…"

show shizu adjust_happy
with charachange

shi "…"

show misha hips_grin
with charachange

mi "เสร็จแล้ว~!"

hi "โอ๊ะ เร็วจัง เดี๋ยวฉันน่าจะเสร็จก่อนคาบนี้เลิกแหละ"

show misha sign_smile
with charachange

mi "ไม่ ๆ ฮิจัง ทุกอย่างเสร็จหมดแล้ว นายก็เสร็จแล้วด้วย~!"

hi "แบบนี้ก็ได้เหรอ นี่จะบอกว่าทั้งหมดนี่คือทำตามใจไปเรื่อยแล้วจะยื้อกันไว้เฉย ๆ ว่างั้น"

show misha hips_grin
with charachange

mi "เปล่า~…"

show shizu basic_normal
with charachange

shi "…"

show misha perky_smile
with charachange

mi "แต่เรารั้งนายไว้นานแล้ว~! นายก็กลับไปเรียนได้แล้วนะฮิจัง~! เข้าคาบนี้ยังพอทันอยู่นะ!"

hi "แล้วพวกเธอล่ะ"

show shizu behind_blank
with charachange

shi "…"

show misha hips_smile
with charachange

mi "ก็ไปสิ เดี๋ยวจะตามนายไปนั่นแหละ!"

stop music fadeout 6.0

scene bg school_hallway3
with locationchange

"ฉันกลับเข้าห้องเรียนด้วยความสบายใจ แต่คาบเรียนผ่านมาแล้วเกือบครึ่งทาง เลยคิดไปว่าหรือจะเอาเวลาที่เหลือ\nไปหาซื้อน้ำผลไม้มาดื่มรอคาบต่อไปที่โถงทางเดินไปเลย"

"ฉันยืนจ้องประตูห้องสภานักเรียนอยู่ ทว่าก็ไม่มีใครเปิด ทำไมนานอย่างนี้นะ หรือกำลังเก็บงานส่วนที่เหลือของฉันอยู่\nจริง ๆ ก็ไม่น่านาน ยกเว้นว่าจะมีงานเหลืออีกแล้วอยากปล่อยฉันมาก่อนเฉย ๆ "

"ยิ่งคิดก็ยิ่งดูเป็นไปได้"

"ชิซูเนะก็…ไม่ได้โง่หรอก แต่ที่ชัดก็คือไม่เก่งเรื่องการสื่อสาร"

"อาจจะเพราะเธอพูดไม่ได้ถึงได้สื่อสารอะไรลำบาก มีมิช่าอยู่ก็จริง แต่ยังไงไม่ว่าจะดูลื่นไหลขนาดไหน ภาษาพูดแบบกันเอง\nกับภาษามือนั้นไม่เหมือนกันอยู่แล้ว"

play sound sfx_normalbell

"ฉันชั่งใจว่าจะกลับเข้าไปหาทั้งสองคนอีกทีดีไหม แต่แล้วกระดิ่งก็ดัง ต้องกลับไปเข้าเรียนแล้ว"

scene bg school_scienceroom
with locationchange

"สองสามนาทีให้หลังพวกเธอก็ตามมา ความคิดอะไรที่เคยอยู่ในหัวถูกกลืนหายไปกับกิจวิตรในรั้วโรงเรียน"

with shorttimeskip

"เมื่อรู้ตัวอีกทีก็เลิกเรียนแล้ว ฉันเหนื่อยเกินกว่าที่จะทำอะไรนอกจากการตรงดิ่งกลับห้อง ทำการบ้าน และนอน"

$ suppress_window_after_timeskip = True

scene black
with Dissolve(3.0)


#***************

label th_A29:

scene bg school_hallway3
show crowd
with None

play ambient sfx_crowd_indoors fadein 0.3
play music music_emi fadein 0.3

show emi basic_happy at center
with charaenter

emi "ฮิซาโอะ!"

show emi excited_proud
with charachange

emi "ฉันขอมอบข้อเสนอข้าวเที่ยงสุดพิเศษที่มีเพียงครั้งเดียวเท่านั้น!"

show emi excited_laugh
with charachange

emi "นั่นคือกล่องข้าวเที่ยงทำมือโดยเอมิ และสิทธิพิเศษกับการได้ดื่มด่ำมื้อนี้กับสาวสวยระเบิดสองคน!"

"การขายตรงของเธอที่ออกจะเป็นการจีบมากไปหน่อยนั้นดังก้องทั่วโถงทางเดิน ซึ่งน่าทึ่งมากเพราะที่นี่มีแต่คนเต็มไปหมด"

show emi basic_closedgrin
with charachange

"เอมิเต๊ะท่าที่ดูแสนมั่นใจเพื่อกลบเกลื่อนความบ๊องของการกระทำของเธอ ยืดอกที่มีแต่พอดีนั้นขึ้นพลางชูสองนิ้ว"

hi "ฟังดูน่าอร่อยดีนี่ ว่าแต่ด้วยเกียรติอันใดที่ข้าพเจ้าสมควรรับคำเชิญนี้หรือ"

show emi excited_proud
with charachange

emi "เห็นยืนเด๋อหงอยเป็นส้วมซึมอยู่ตรงนั้นเลยกะจะชวนมาเป็นเพื่อนแน่ะ"

"เป็นเหตุผลที่คิดแล้วเครียดหนักจริง ๆ"

show emi basic_closedgrin
with charachange

emi "ว่าไงล่ะ ไม่งั้นนายก็คงตัวคนเดียวไปกินข้าวโรงอาหารเห่ย ๆ อยู่แบบเหงา ๆ นะ"

hi "เอ่อออ…"

show emi excited_proud
with charachange

emi "หยอก ๆ น่า!"

hi "ได้ ขอรับข้อเสนอมื้อเที่ยงของเธอไว้ด้วยความยินดี"

show emi basic_happy
with charachange

emi "ไปดาดฟ้ากัน!"

hi "ดาดฟ้า?"

hi "ทำไมต้องที่ดาดฟ้า"

show emi basic_closedgrin
with charachange

emi "ก็ไปกินข้าวเที่ยงที่นั่นไง!"

emi "แล้วถ้าไม่รีบไปเดี๋ยวเธอคนนั้นก็หนีไปเดินเล่นอีก แล้วเดี๋ยวก็จะหิวเพราะไม่เคยห่อข้าวเที่ยงมาเองเลย!"

hi "เธอคนนั้นที่ว่านี่ใคร"

show emi basic_closedhappy
with charachange

emi "มาเถอะน่า!"

"เธอลากแขนฉันไปตามโถงทางเดินโดยไม่ตอบคำถามหรือรอคำตอบใด ๆ "

"ระหว่างทางฉันก็หาเรื่องคุย"

hi "ทำไมถึงทำมาเยอะขนาดนี้"

show emi sad_grin
with charachange

"เอมิยิ้มแหย ๆ "

emi "จริง ๆ แล้วอันนี้คือข้าวเที่ยงของเมื่อวานน่ะ"

emi "พอดีตอนพักเที่ยงไปวิ่งแล้วก็ลืมกินเลย"

"หืม"

# The line above will go wherever the scene changes from out of the hallway, I guess.


label th_A29x:

"สีหน้าของเธอดูตลกจนฉันแทบหลุดขำ"

"เธอหัวเราะคิกคัก ไม่รู้หัวเราะกับตัวเองหรือเรื่องอื่นกันแน่ หรือไม่ก็ขำลอย ๆ เป็นเสียงหัวเราะที่ฉันชอบ"

"พลังอันเหลือล้นและความสดใสของเธอช่วยบรรเทาความรู้สึกอันหนักอึ้งหลังทะเลาะกับชิซูเนะและมิช่าที่ติดตรึงอยู่ในหัว"

"ฉันปล่อยให้เรื่องนั้นลอยหายไปจากหัวและยิ้มเป็นครั้งแรกของวัน"



label th_A29a:

#and this is what happens if you had a heart flutter:
scene bg school_hallway3
show crowd
with None

play ambient sfx_crowd_indoors fadein 0.3

"ปกติฉันคงไหลไปตามผู้คนและหาซื้อข้าวเที่ยงบ้าง แต่วันนี้ไม่เหมือนเดิม"

"วันนี้มีคนชวนฉันไปกินข้าวเที่ยงที่ดาดฟ้า"

"ถึงจะเป็นสถานที่ที่แปลก แต่ก็ได้ยินมาอย่างนั้น"

"โชคดีที่มีประตูห้องเรียนให้มาหลบรอกระแสคนไหลออกไปก่อน"

stop ambient fadeout 1.0

hide crowd
with Dissolve(2.0)

"พอคนเริ่มซาลงแล้วฉันก็ออกมาที่โถงทางเดิน"

"และเจอกับเอมิที่ทะยานมาตามโถงทางเดินราวกับลูกปืนใหญ่"

play music music_emi fadein 0.3

show emi basic_happy at center
with charaenter

emi "นี่! ไง ฮิซาโอะ! มาพอดีเลย!"

show emi excited_proud
with charachange

emi "ฉันเอาข้าวเที่ยงแสนพิเศษตามสัญญามาแล้วนะ! ไปข้างบนกัน!"



label th_A29b:

#Finally, this is where the two join up again

stop music fadeout 2.0
stop ambient fadeout 1.0

scene bg school_staircase1
with locationchange

"บันไดทางเดินไปดาดฟ้าดูโทรมเล็กน้อย แต่มีรอยเดินใหม่อยู่"

"ปลายทางเป็นประตูที่ไม่มีกุญแจล็อก"

"ใครช่างกล้าปลดกุญแจกันนะ"

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_rooftop fadein 2.0

scene bg school_roof at bgright
show emi basic_closedgrin at center
with Fade(0.5,0.3,1.0,color="#FFF")

"เอมิเปิดประตูออกแล้วเดินไปรับแสงแดดที่สาดส่อง"

show rin silhouette at offscreenright
with None

show bg school_roof at center
show emi basic_closedgrin at left
show rin silhouette at tworight
with ease

show emi basic_shock
with vpunch

"จู่ ๆ ก็มีเงามืดของใครบางคนยืนทะมึนอยู่ตรงหน้า เอมิผงะไปจนเกือบตกบันได"

$ doublespeak (emi, rin_, "ว้าย!", "สวัสดี")

show emi basic_hes
with charachange

show emi basic_hes at twoleft
with charamove

emi "โธ่! ริน ตกใจหมดเลย!"

"เดี๋ยวนะ เธอคนนี้…"

show rin relaxed_surprised
with charachange

play music music_rin fadein 2.0

rin "สวัสดี"

"เอมิมองมาทางฉันด้วยความสงสัยเมื่อเห็นว่ารินคุยกับฉัน"

show emi basic_confused
with charachange

emi "เธอสองคนรู้จักกันเหรอ"

"ฉันมองงง ๆ ไปทางเอมิ"

hi "คนนี้เหรอเพื่อนเธอที่ว่า"

show rin relaxed_nonchalant
with charachange

"รินละสายตากลับไปมองเมฆที่เลื่อนลอยอยู่เหนือโรงเรียน"

rin "ไม่เห็นรู้ว่าเธอรู้จักเขาด้วยนะเอมิ"

stop music fadeout 2.0

"…"

"ความเงียบอันน่าอึดอัดเกิดขึ้นได้ไม่กี่วินาทีก็ถูกทำลายโดยเสียงหัวเราะน้อย ๆ ของเอมิที่ไม่ได้ใส่ใจความบังเอิญนี้"

show emi basic_closedgrin
with charachange

emi "ฉันชวนเขามากินข้าวเที่ยงน่ะ ถ้ารู้จักกันก็ดีเลย"

show rin basic_deadpan
with charachange

rin "อ้อ งี้ก็แปลว่าฉันไม่ได้กินแล้วน่ะสิ หรือชวนเขามากินข้าวเที่ยงแบบไม่มีข้าวเที่ยง"

show emi basic_grin
with charachange

emi "เอ่อ ไม่อะ ฉันมีข้าวพอสำหรับสามคนเลย"

show rin basic_deadpanamused
with charachange

rin "วางแผนดีนี่"

hide rin
hide emi
with charaexit

"ทั้งสองคนเดินไปอีกฟากของดาดฟ้าขณะที่ฉันดื่มด่ำกับบรรยากาศอยู่บริเวณหอนาฬิกา"

play music music_soothing fadein 0.5

"ที่นี่ไม่มีใครนอกจากพวกเรา ดาดฟ้าที่โรงเรียนนี้คงไม่ได้เป็นที่นิยมเหมือนที่อื่น"

"มีม้านั่งกับโต๊ะเก่า ๆ กระจัดกระจายอยู่ตามริมดาดฟ้า คงเอามาวางไม่ให้ดูร้างเกินไป"

"ก้อนกรวดที่ปูพื้นดาดฟ้าส่งเสียงกรอบแกรบอยู่ใต้เท้า"

"ฉันมองลานโรงเรียนและละแวกโดยรอบผ่านรั้วตาข่ายเหล็ก"

"มีนักเรียนเดินอยู่ทั้งเป็นคู่และเป็นกลุ่มอยู่บริเวณลานกว้างและโรงอาหาร"

"มีรถบรรทุกสองสามคันขับผ่านโรงเรียนไปยังร้านสะดวกซื้อที่อยู่ไม่ไกลจากที่นี่"

"มีหมาเฝ้ายามเห่าคนที่เดินผ่าน"

"ไม่รู้ทำไม แต่พอได้มองไปที่ใจกลางเมืองแล้วก็ทำให้รู้สึกถึงความเล็กของเมืองนี้อย่างชัดเจนจนแทบสัมผัสได้"

"บรรยากาศชีวิตอันเร่งรีบในเมืองใหญ่ดูจะเป็นเรื่องที่ไกลตัวสำหรับคนที่นี่ ไม่มีใครต้องรีบมาให้ทันรถประจำทาง\nอย่างเอาเป็นเอาตาย ไม่มีแสงสีหรือรถติดที่ทำให้ประสาทมึนชา"

"ฉันรู้สึกดีขึ้นกับชีวิตใหม่ที่นี่อย่างน่าประหลาดเมื่อได้มองเมืองใหม่ของฉันที่แม้อาจจะได้อยู่เพียงแค่หนึ่งปี"

"ทั้งตอนที่ได้รู้ตัวเรื่องโรคนี้กับตอนที่ได้ย้ายจากบ้านมานั้นเป็นไปอย่างกะทันหันจนไม่มีเวลาให้คิดถึงความรู้สึกตัวเอง"

"เมื่อเดินออกมาจากเงาของหอนาฬิกาแล้วก็มีความอบอุ่นจากแสงแดดสาดส่องเข้าที่หลัง"

"พระอาทิตย์เจิดจ้าท่ามกลางฟ้าใสกระจ่างสีคราม"

"ลมเย็นพัดวูบพาให้ตัวสั่น แต่ก็เพียงครู่"

"สายลมพัดพากลิ่นดอกไม้ใบหญ้า ไม่ใช่หมอกควันอย่างที่คุ้นเคยเมื่อสองสามสัปดาห์ก่อน"

"เอมินั่งอยู่เคียงรินแล้วหยิบกล่องข้าวเที่ยงขนาดใหญ่หนึ่งกล่องและขนาดเล็กสองกล่องออกมาจากกระเป๋าของเธอ"

show rin basic_deadpannormal at tworight
show emi basic_happy at twoleft
with charaenter

emi "มานี่สิฮิซาโอะ! รออะไรอยู่ได้"

"เธอกวักมือเรียกฉันพลางกระเถิบให้พอมีที่บนม้านั่งแคบ ๆ นั้น"

hide emi
hide rin
show bg school_roof at bgleft
with charamoveoutleft

show emi basic_happy_close at closeleft
show rin basic_deadpannormal_close at closeright
show bg school_roof at center
with charamoveinleft


"ฉันนั่งลงที่ริมสุดม้านั่งให้กินที่น้อยสุด เบียดกันพอตัวแต่ก็พอนั่งสามคนได้"

hi "วิวสวยดี"

show emi basic_closedhappy_close
with charachange

"เธอกลั้นขำน้อย ๆ แล้ววางข้าวกล่องตรงหน้ารินและยื่นอีกกล่องให้ฉัน"

show emi excited_proud_close
with charachange

emi "เอ้านี่! ข้าวเที่ยงตามสัญญา!"

"ทำมืออีกต่างหาก ทึ่งจริง ๆ "

hi "โห น่าอร่อยจัง"

show emi excited_amused_close
with charachange

emi "ขอบใจนะ! คือถ้าพอมีเวลาฉันก็จะทำน่ะ"

"บทสนทนาถูกตัดจบเมื่อฉันเริ่มหันมาสนใจการกิน"

show rin basic_awayabsent_close
with charachange

"เมื่อกินไปได้สองสามคำฉันก็เหลือบมองรินที่ใช้แค่เท้าเปิดกล่องอย่างคล่องแคล่วและใช้ส้อมจิ้มอาหารเข้าปากเธอ"

"ถึงจะเคยเห็นมาแล้วก็ยังอดทึ่งไม่ได้กับความคล่องของเธอ"

"ถือเป็นสิ่งที่ทำให้ฉันระลึกถึงที่ที่ฉันกำลังอยู่ตอนนี้ด้วย"

"ฉันจะชินกับภาพแบบนี้ได้เมื่อไหร่กันนะ"

"ฉันเองก็ไม่รู้ว่าการชินกับอะไรแบบนี้จะเป็นเรื่องที่ดีหรือไม่"

"ถ้าฉันชินก็หมายความว่าฉันยอมแพ้กับการจะเป็นคนปกติแล้วหรือเปล่า"

"หรืออาจจะหมายความแค่ว่าฉันเข้าใจคนรอบตัวมากขึ้นแล้วหรือเปล่า"

"ฉันหลุดจากภวังค์เมื่อเห็นเอมิจ้วงกินข้าวเที่ยงเอาอย่างกับว่ามันไปด่าพ่อล้อแม่เธอ"

show rin basic_absent_close
with charachange

hi "เธอดูหิวนะ"

show emi basic_grin_close
with charachange

"เอมิมองมาโดยข้าวยังอยู่ในปาก เธอกลืนข้าวลงไปก่อนพยักหน้า"

emi "พอวิ่งรอบเช้าแล้วมันหิวน่ะ"

show emi basic_closedhappy_close
with charachange

emi "ซึ่งก็ดี เพราะจะได้เอาข้าวเที่ยงไปเผาผลาญให้หมดเร็ว ๆ ด้วย"

show emi excited_proud_close
with charachange

emi "เป็นการรักษาหุ่นสาวน้อยของฉัน"

show rin basic_deadpan_close
with charachange

rin "ถ้าไม่เป็นหุ่นสาวน้อยแล้วมันยังไงต่อ จะกลายเป็นหุ่นหนุ่มน้อยงี้เหรอ"

"ฉันกลั้นขำจนแทบสำลักข้าวเที่ยง"

show emi basic_annoyed_close
with charachange

emi "แค่เปรียบเทียบหรอกย่ะ"

show rin basic_deadpandelight_close
with charachange

rin "หุ่นของเธอไปวิ่งรอบเช้าด้วยเหรอ"

hi "นี่คุยกันอย่างนี้ตลอดเลยเหรอ"

show rin relaxed_surprised_close
show emi basic_confused_close
with charachange

$ doublespeak(emi, rin, "คุยแบบไหน", "แบบไหน")

"โอเค ได้คำตอบละ"

hi "เอ้อ ช่างเถอะ"

hi "แล้ว เอ่อ…"

"ฉันเค้นสมองนึกหาเรื่องคุยเรื่อยเปื่อยแล้วเลือกคำถามง่าย ๆ ขึ้นมา"

hi "เธอสองคนมาเจอกันได้ยังไง"

show rin basic_awayabsent_close
with charachange

"รินดูจะยอมยกให้เอมิตอบคำถามนี้ให้"

show emi basic_grin_close
with charachange

emi "คนที่จัดห้องเห็นว่าพวกเราคงเติมเต็มกันและกันได้ดีเลยให้อยู่ห้องติดกันน่ะ"

hi "เติมเต็มกันและกัน?"

show rin basic_deadpannormal_close
with charachange

rin "เหมือนเสื้อกับรองเท้า"

hi "หา?"

show emi basic_closedgrin_close
with charachange

"เอมิหัวเราะน้อย ๆ เมื่อเห็นว่าฉันยังงงอยู่"

emi "ก็เอามาประกอบกันก็ได้แขนขาครบส่วนเลยไง"

hi "อ้อ"

show emi basic_happy_close
with charachange

emi "ฉันก็เลยเคยคอยช่วยแต่งตัวอะไรให้รินตอนเช้า ก็ประมาณนั้นแหละ!"

show emi basic_grin_close
with charachange

emi "ช่วยแต่งตัวให้ทุกเช้ายังไงก็ต้องสนิทกันเป็นธรรมดาแหละ"

hi "อย่างนี้นี่เอง"

"รินถือจังหวะนี้เข้าเสริม"

show rin basic_deadpan_close
with charachange

rin "ฉันใส่เสื้อไม่ค่อยสะดวกน่ะ"

hi "นั่นสินะ ก็…ชัดอยู่"

show rin basic_surprised_close
with charachange

rin "จริงเหรอ"

hi "ก็พอจะชัด…?"

"ไม่ไหว แต่อย่างน้อยเอมิก็ดูจะขำที่คุยกันดี"

"แล้วก็อีกอย่าง ที่รินถามคือเธอสงสัยจริง ๆ จนทำให้ฉันรู้สึกดีขึ้นนิดหน่อย แต่ก็ยังงง ๆ "

hi "ก็ เธอไม่มีแขนนี่"

hi "แล้วแบบ เอ่อ ถ้าจะใส่เสื้อหรืออะไรแบบนั้นก็คงเป็นอะไรที่ดู…ลำบาก"

"ฉันว่า ฉันเลิกคุยดีกว่า"

"จะได้ไม่ต้องปวดหัวให้ยืดเยื้อ"

"รินพยักหน้าในแบบที่ฉันคิดว่าเธอคงจะทำท่าให้เหมือนคิดอะไรลึกซึ้งอยู่"

show rin basic_lucid_close
with charachange

rin "อย่างนี้นี่เอง"

show rin basic_absent_close
with charachange

"บทสนทนาถูกตัดจบเมื่อฉันกลับมากินข้าวต่อ"

"อร่อยใช้ได้"

"เอมิกินหมดเป็นคนแรก เธอทำเสียงท่าทางอิ่มออกมา"

show emi excited_laugh_close
with charachange

emi "อ่า อร่อยจัง"

"ขณะเธอง่วนกับการเก็บกวาดส่วนของเธอรินก็พูดขึ้นมา"

show rin basic_deadpan_close
with charachange

rin "หิวน้ำอะ"

show emi basic_shock_close
with charachange

emi "โอ๊ะ! เกือบลืมแน่ะ! โทษทีนะ!"

show emi basic_closedgrin_close
with charachange

"เธอหยิบน้ำผลไม้ออกมาจากกระเป๋าของเธอสามกล่องด้วยท่าทางที่ดูเน้นชัด"

"เธอโยนกล่องหนึ่งมาให้ น่าจะเป็นน้ำแครนเบอร์รี ส่วนของรินเหมือนจะเป็นนมสตรอว์เบอร์รี (กล่องเน้นสีชมพูด้วย)\nส่วนของเธอเองเป็นน้ำพันช์ผลไม้อะไรสักอย่าง (ที่มีสีชมพูพอกัน)"

show rin basic_awayabsent_close
with charachange

"รินใช้หลอดปักเข้าที่กล่องอย่างคล่องแคล่วแล้วดื่ม"

"เป็นอีกครั้งที่ฉันทึ่งกับการปรับตัวของเธอ แต่คราวนี้ฉันเก็บคำพูดนั้นไว้ในใจแทน"

"ไม่รู้ทำไม แต่ฉันว่าทั้งเอมิกับรินไม่ใช่คนที่จะมาคิดมากอะไรกับการที่หาทางปรับตัวอยู่กับความพิการของตัวเองกัน"

"โดยเฉพาะริน"

"เธอเป็นคนที่ดูจะไม่รู้สึกตัวเลยว่าเธอนั้นไม่มีแขน"

"แต่เธอจะจงใจคิดอย่างนั้นหรือไม่ก็อีกเรื่องหนึ่ง"

"ฉันก็ไม่แน่ใจเหมือนกัน"

show emi basic_grin_close
with charachange

emi "นี่ ฮิซาโอะ ที่ดาดฟ้านี่เป็นไงบ้าง"

show rin basic_absent_close
with charachange

hi "หืม?"

hi "ก็ใช้ได้เลยนะ ฉันชอบวิวที่สูง ๆ น่ะ"

hi "ขอบคุณที่ชวนมานะ"

hi "แล้วก็ขอบคุณที่เลี้ยงข้าวเที่ยงด้วย"

show emi excited_amused_close
with charachange

"เอมิยิ้มแฉ่งปล่อยพลังงานแสนวัตต์ คงพอใจกับคำตอบฉันแหละ"

emi "ด้วยความยินดีจ้า!"

show emi excited_proud_close
with charachange

emi "คราวหน้าถ้าอยากมากินด้วยก็ตามสบายเลยนะ"

emi "ก็ไม่ทำมาเผื่อนายหรอก แต่เอาของนายมากินที่นี่ได้นะ"

hi "ไม่มีบริการข้าวเที่ยงเหรอ ยังไงดีนะ…"

show emi basic_annoyed_close
with charachange

"เอมิทำท่าโกรธแบบหยอก ๆ "

emi "เห็นฉันใจดีหน่อยนี่ย่ามใจเลยนะ"

emi "ช่างกล้า!"

show emi basic_closedgrin_close
with charachange

"เธอทำเสียงคิกคัก"

show emi sad_depressed_close
with charachange

emi "อืม ถ้านายว่าอย่างนั้น ฉันกับรินก็คงต้องกินข้าวกันสองคนเหงา ๆ สินะ…"

"ฉันถูกจู่โจมเข้าอย่างกะทันหันเมื่อเอมิทำแก้มป่องพร้อมแววตาอย่างหมาน้อยที่ทำเอาเจ็บจี๊ดไปถึงข้างใน"

hi "ล้อเล่นน่า! ล้อเล่น!"

hi "ฉันมากินข้าวเที่ยงที่นี่อีกแน่นอน"

hi "สถานที่ก็ดี เพื่อนกินก็ดี"

show emi basic_grin_close
with charachange

"เอมิขมวดคิ้วเล็กน้อยกับคำตอบ “ตกลง” ของฉัน แต่ก็ดูดีใจที่ฉันรับคำชวนของเธอ"

"แบบนี้ก็เป็นเพื่อนกันแล้วสินะ"

"หรืออย่างน้อยก็คนรู้จัก"

play sound sfx_warningbell

"ระฆังดังเป็นสัญญาณให้กลับลงไป"

show emi basic_hes_close
with charachange

emi "ริน เธอกินข้าวเหลืออีกแล้วนะ!"

show rin basic_deadpan_close
with charachange

rin "ก็ไม่ได้หิวขนาดนั้น"

show emi basic_annoyed_close
with charachange

emi "ขืนไม่กินให้เยอะกว่านี้เดี๋ยวตัวเธอก็หายไปหรอก!"

show rin relaxed_boredom_close
with charachange

"รินยักไหล่ราวกับไม่กลัวว่าจะหายไป"

stop music fadeout 4.0

hi "เถอะน่า ไปกันได้แล้ว"

stop ambient fadeout 2.0

scene bg school_staircase1
with locationchange

"พวกเราทั้งสามคนเดินลงบันไดไปด้วยกัน"

scene bg school_scienceroom
with shorttimeskip

"คาบบ่ายผ่านไป และฉันก็ไม่มีอะไรทำหลังเลิกเรียนอีกแล้ว จึงจะไปห้องสมุดเพื่อคืนหนังสือสองเล่มที่อ่านจบแล้ว"

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")

scene bg school_library
with locationskip

"Walking inside, I see that there are about as many students here as there were on Tuesday, all the more evident from the almost total silence enveloping the room."

play sound sfx_impact2
with vpunch

show yuuko panic_up at center
with easeinbottom

play music music_happiness fadein 2.0

"As I drop the books I'd borrowed into the returns slot in the counter, Yuuko suddenly pops up from behind it, quite startled from the banging they make as they hit the trolley next to her."

hi "Ah, sorry Yuuko. Didn't mean to startle you."

show yuuko worried_up
with charachange

yu "No, no. That's fine. It happens… a lot. I'm used to it by now."

show yuuko neurotic_up
with charachange

yu "Um, can I help you?"

hi "It's okay, I think I know where everything is. Thanks anyway."

hide yuuko
with charaexit

"I suppose I'll grab another book or two while I'm here. There's not much else to do, and after reading so much during my stay in the hospital, it's become a hard habit to break."

stop music fadeout 5.0

"I wander down to the fiction section towards the back of the library, scanning the bookshelves for anything that catches my eye."

"As I do, I look over to the corner where Hanako had been the last time I was here, not really expecting anything to come of it."

scene ev hana_library_read_std
with locationskip

"…surprisingly, though, she's there, absorbed completely in a fairly thick book. I decide against intruding on her like last time and get back to finding reading material."

scene bg school_library_ss
with shorttimeskip

play music music_tranquil fadein 6.0

"After an indiscernible amount of time spent perusing the aisles, I finally decide on a couple of books to get and slide them off the shelf."

"With a minimum of fuss, I quickly walk over to the counter, check out my books and pop them into my bag as I walk out."

scene bg school_courtyard_ss
with locationskip

"By the time I leave the main building, sunset isn't too far away. A small trickle of students remain, but the majority have left; presumably to their homes and dorms."



label th_A29c:

scene bg school_dormhisao_ss
with locationskip

"Feeling utterly drained, I head to my room to read the books I borrowed. There's been enough action and excitement for one day already."

"The first is “Alice's Adventures in Wonderland”. I know the story, of course, but I've never actually read the original book."

"It's just as trippy as I remember the story to be, with the wacky characters and nonsense plot."

"I start thinking of myself as some kind of an Alice too, haplessly tumbling down the rabbit hole into this Cripple Wonderland."

"…Okay, that's a rather strong expression. Still, the isolated location and the overt way the school accommodates to absolutely everything is unsettling. It is like another world."

"I wonder why I can't shake the feeling of being an outsider like Alice, despite most everyone being so hospitable and friendly with me."

"Turning another page, my mind starts drifting further away from the book. It's quiet, I can hear my heartbeat thumping against the fabric of my shirt."

"For some reason, it makes me feel really bad like it has since that time in the forest with Iwanako. Like I was locked in a cage with something nasty and scary."

stop music fadeout 5.0

scene bg school_dormhisao_ni
with Dissolve(3.0)

"I put the book down for a while and stare at the ceiling, taking my time to shake off the feeling."

"200 pages later, I fall asleep."

scene black
with shuteye


#*********************

label th_A30:

scene bg school_courtyard_ss
with None

$ renpy.music.play(music_tranquil, fadein=3.0, if_changed=True)

"I guess I need to buy some supplies. I can't live off cafeteria food and eating out for my entire stay here."

scene bg school_gate_ss
with locationchange

"As I leave for the gate, I make a few loud stretches to try and stave off the tiredness that's accumulated over the week."

scene bg school_road_ss
show lilly back_smileclosed_ss at center
show lillyprop back_cane_ss at center
with locationchange

#stop music fadeout 4.0

"After passing through and rounding the corner, though, I see a solitary figure walking downhill towards the small town below. The color of her hair and tapping of her cane are unmistakable."

show lilly cane_surprised_ss
hide lillyprop
with charachange

"I quickly walk up to her, which seems to catch her attention without a word needing to be said."

hi "Hi, Lilly."

show lilly cane_weaksmile_ss
with charachange

"She takes a moment to place the voice, slightly adjusting her head to face a bit more towards the source of my voice as she does."

#play music music_lilly fadein 3.0

show lilly cane_smile_ss
with charachange

li "…Hisao?"

hi "Yep, that's me."

"She seems to have a good memory for voices. The fact that she actually remembered is a pleasant surprise."

li "Good evening. What brings you here?"

show lilly cane_weaksmile_ss
with charachange

"Once again, she gives a small polite bow. And, once again, I reply in kind before realizing that I needn't do so."

hi "Just going into town. You?"

show lilly cane_ara_ss
with charachange

li "My my, what a coincidence."

hi "Doing the same thing, eh?"

show lilly cane_smile_ss
with charachange

li "Mm. I usually go shopping on Fridays."

show lilly cane_surprised_ss
with charachange

"She pauses for a moment, suddenly looking a little lost."

li "That said, Hanako usually comes into town with me…"

"Ah. Not lost, but worried. The two do seem to keep pretty close tabs on one another. It's kind of surprising that Hanako would just forget Lilly like that."

hi "I noticed her reading in the library. She probably just got caught up in a book."

show lilly cane_weaksmile_ss
with charachange

"She lets out a small sigh of relief."

li "Thank you. She has a habit of doing that."

hi "Avid reader?"

show lilly cane_smile_ss
with charachange

li "Right. She doesn't like being around crowds of people, so reading away from everyone lets her relax a bit."

"Although she probably didn't intend it, I can't help but grimace as I recall my first meeting with her."

show lilly cane_smileclosed_ss
with charachange

"Hardly wanting to bring it up, I remain silent as we quietly continue to walk down the quiet road."

"Tack, tack. Tack, tack."

"With the road bereft of cars and the students of Yamaku increasingly far behind us, the quiet rustling of the leaves and the measured tapping of Lilly's cane against the sidewalk are all that can be heard."

"It's kind of nice, especially compared to the hustle and bustle of where I used to live."

"Before I know it, I've relaxed so much that a loud yawn escapes before I can control it."

show lilly cane_giggle_ss
with charachange

li "Tired?"

hi "Yeah, been running ragged these past few days."

"That's an understatement, to be sure. Transferring into a different school would be bad enough, but nothing like this…"

show lilly cane_smile_ss
with charachange

li "Well, hopefully everything should settle down for you. The festival's got everyone in a spin right now, and you've been plopped right in the middle of things."

"For a moment I hesitate, but given her apparent tolerance for frankness I decide to give my full thoughts."

hi "I guess. Yamaku's kind of different though. I mean, the formality surrounding everything, the isolation around it… not to mention the most obvious difference."

hi "It's kind of a whole different mindset. I suppose I'll get used to it though, in time."

show lilly cane_smileclosed_ss
with charachange

"She gives a matter-of-fact nod, apparently pleased with my answer. It feels almost as if she's included me in the flock of students she's shepherding, along with class 3-2 and Hanako."

"Well, not that I mind. It's nice to get the thoughts off my chest in any case."

show lilly cane_smile_ss
with charachange

li "Looking on the bright side, one could see it as a chance for a new beginning. You should cherish the ability to make new friends."

"That's optimistic. Nonetheless, it's good to have a positive attitude about such things, I suppose."

hi "I guess that's a good take on it."

scene bg suburb_roadcenter_ss
show lilly cane_reminisce_ss at center
with shorttimeskip

stop music fadeout 6.0

"Walking on down the road, she seems to become somewhat unsettled. Before I can ask what's on her mind, she seems to collect herself and speaks up about something else."

show lilly cane_weaksmile_ss
with charachange

li "So, where in town were you going?"

"That's actually a pretty good question. I'd come in to buy food, but the layout of the place is still totally foreign to me."

"I had intended to just wander around and see what I could find, but with sunset already approaching and nightfall not too far away, that doesn't seem very wise."

"I'm going to have to ask her for directions. Again."

hi "I was just going to get some food… but now that you mention it, I don't really know the way."

show lilly cane_planned_ss
with charachange

li "Well now, this is quite lucky. I was just about to go to the convenience store myself."

hi "Looks like I'll be in your care again, then. Thanks."

"Together we walk to the store, my paces carefully slowed to remain beside her. Compared to my usual walking pace, hers is quite a bit slower. Not that it's without reason."

scene bg suburb_konbiniext_ss
with shorttimeskip

play music music_daily fadein 2.0

"After what couldn't be more than several minutes, I catch sight of our objective. This town really is pretty small."

scene bg suburb_konbiniint
with locationchange

"Without further ado, we make our way inside with a greeting from the counter."

show lilly cane_weaksmile at center
with charaenter

li "Mind if I tag along with you? Usually Hanako would help me, but seeing as she's not here…"

"It takes a moment before I realize what she means."

"Considering she wouldn't be able to read any of the labels, shopping without any help would be a big pain for her."

"That said, I can't shake the feeling that she'd had this idea since I said I was coming here."

hi "Sure. It'd be my pleasure."

"I grab two well-used red baskets from the small stack beside the entrance, handing one to Lilly."

show lilly cane_weaksmile at Transform(ypos=800)
with charamove

show lilly basic_smileclosed at Transform(ypos=800)
with charachange

show lilly basic_smileclosed at center
with charamove

"She lays it on the ground, putting her schoolbag in, retracting her cane and sliding it through the basket's handles before picking it back up in her right hand."

"Wait, if she doesn't use her cane…"

show lilly basic_smileclosed at Slide(0.5,0.5,0.3,0.5,1.0, time_warp=_ease_time_warp)
with None

show lilly basic_smileclosed_close at Slide(0.5,0.5,0.3,0.5,1.0, time_warp=_ease_time_warp)
with Dissolve(1.0)

"Before I can complete the thought, she comes beside me and pinches the cuff of my uniform in her slender fingers."

show lilly basic_concerned_close at twoleft
with characlose

li "Is this all right?"

hi "Ah, sure."

show lilly basic_smileclosed_close
with characlose

"I have no reason not to accept. I can think of worse things than shopping with a pretty girl holding onto me, even if it is out of necessity."

"We navigate our way through the store, with not one of the occasional passing customers seeming to bat an eyelid."

"Considering how close Yamaku is, I guess seeing students from there must be entirely normal for the local residents."

"As we reach each aisle, I quickly check with Lilly and find out what she needs. I grab it along with what I'm looking for, and put our items into their respective baskets."

"I guess this is the same routine she and Hanako follow every Friday."

hi "Right, all that's left is the bread and that should be my shopping done. Do you need anything else, Lilly?"

show lilly basic_smile_close
with characlose

li "No, this should be everything."

hi "Off we go, then."

show lilly basic_smileclosed_close
with characlose

"With a quick side trip to the bakery section, we make our way to the registers."

"The line, thankfully, is almost nonexistent. It's not long before we've both paid for our food and are out the door."

scene bg misc_sky_ni at Fullpan(15.0)
with locationchange

"As Lilly retrieves her cane and extends it to full length, I waste a minute looking upwards at the night sky while holding both our bags."

"For a moment I try to make clouds with my breath, but the summer's heat doesn't seem to cooperate."

"Eventually she rights herself, taking a quick stretch before taking her bag and leaving me to my two."

scene bg suburb_konbiniext_ni
show lilly cane_listen_ni at center
with locationchange

hi "You tired as well?"

show lilly cane_sleepy_ni
with charachange

li "The festival preparations have been complete chaos. Shizune breathing down my neck doesn't exactly help things, either."

hi "Hey, she's only trying to get everything organized. Better now than later, right?"

show lilly cane_weaksmile_ni
with charachange

li "I suppose. I'm going to enjoy relaxing in town tomorrow, that's for certain."

"I guess the festival preparations must be taking their toll on both of them."

scene bg suburb_roadcenter_ni at bgright
with locationchange

"We walk out into the quiet street, talking between ourselves as we carry our bags of food and supplies from the store."

"…Wait, what's that?"

"I notice a very distinctive figure making its way towards us, silhouetted by the streetlamps."

"For a second I think it's another male student from my class, but as he, or should I say she, gets closer I recognize her quickly."

show bg suburb_roadcenter_ni at center
show rin relaxed_nonchalant_ni at right
with charamoveinright

stop music fadeout 8.0

hi "Rin? What're you doing out here so late?"

show lilly cane_surprised_ni at center
with charaenter

li "Rin?"

"Lilly perks her head, looking like she's trying to focus on listening more keenly. It suddenly comes to me that I should probably interpret the scene for her."

hi "It's Rin… Tezuka, I think was her last name, from our school."

show lilly cane_weaksmile_ni
with charachange

"She stiffens at the name and gives a complicated-looking expression, something like a forced fusion of a composed smile and a painful cringe."

li "Ah. I understand."

"I guess Lilly knows Rin too."

show rin basic_awayabsent_ni
with charachange

show bg suburb_roadcenter_ni at bgleft
show rin basic_awayabsent_ni at tworight
show lilly cane_weaksmile_ni at twoleft
with charamove

"Rin turns to look at us, looking terribly out of it. I'm not entirely sure if she recognizes either of us or at least she doesn't acknowledge it if she does."

"She looks like a zombie. Or a statue. A statue of a zombie."

"But slowly, some symptoms of understanding seem to light in her dark eyes: this is something she must react to."

show rin basic_lucid_ni
with charachange

show rin basic_awayabsent_ni
with charachange

"Rin blinks once. Very thoroughly."

show rin basic_absent_ni
with charachange

rin "Hello."

"…"

"There is an awkward pause, everyone waiting for someone else to say something."

hi "What are you doing here this late?"

"…"

rin "I…"

show rin basic_deadpan_ni
with charachange

rin "I was wondering about that myself too. Just now."

play music music_rin fadein 0.5

show rin basic_deadpannormal_ni
with charachange

rin "Some people asked that just before. I assume they were wondering the same."

rin "I didn't know. They didn't know either. I asked. That's why I'm wondering."

rin "So that was pretty much it. It's a murder mystery without a murder."

"…"

show rin negative_spaciness_ni
with charachange

rin "They were going that way."

show rin basic_absent_ni
with charachange

"She turns facing to her right in order to demonstrate the direction the other people went to as if that was important, then rotates back like a mechanical puppet in one of those overly complicated clockworks."

"For a person who gives an impression of being the quiet type, Rin really does use a lot of words to say things that don't need a lot to be said."

"Unsure if she's finished, I say nothing. Neither does Lilly, who seems equally robbed of words for the time being."

"I think that both of us are in fact just scared that any response might provoke her to continue."

"Our stupefied lack of reaction doesn't faze Rin at all. She keeps looking at us expectantly, a calm hint of expression on her blank face."

"She seems to be that kind of person. Always so relaxed."

"As if bull elephant-grade sedatives were flowing in her veins in the place of blood."

show lilly cane_concerned_ni
with charachange

li "Do you have amnesia? I don't recall you having anything of the sort, though…"

hi "No, I don't think it's that."

hi "The other passersby were probably just worried, though. You do look really lost, the way you're standing in the middle of the street."

show rin basic_deadpan_ni
with charachange

rin "Oh, I see."

show rin relaxed_nonchalant_ni
with charachange

rin "Maybe I should've taken some other kind of pose in that case."

"I ponder for a while whether I should chase this angle further, or give up for the sake of my own sanity."

"I decide on the latter."

"It seems that most of the time, it's better to not read too deeply into what Rin is babbling about."

"Talking with Rin is like playing chess with a supercomputer who does seemingly completely random moves as if to mock everything you know about chess. It's like that, except with human interaction."

"And even if I win, it feels like losing."

"Damn, it's just like Kenji said. Even when I win, I lose. Is this the power of the girls of Yamaku?"

"…"

"I push the thought aside as too dangerous to consider further. It's probably just Kenji's anti-female propaganda getting to me during a moment of weakness."

hi "Yeah, maybe taking another pose might have worked."

hi "So anyway, you have no idea what you're doing here?"

show rin negative_annoyed_ni
with charachange

"She frowns, looking extremely displeased at either my question, its consequences, or the answer she's about to give."

rin "I do have. Some idea. I can't really tell what kind of an idea."

show lilly cane_smile_ni
with charachange

li "That sounds like progress, at least."

"Lilly sounds as if she's spotted an opening for some kind of discernibly normal conversation. I can't say I share her optimism."

rin "Yes, there is some. Definitely. The rest will come later."

show rin basic_deadpanupset_ni
show lilly cane_weaksmile_ni
with charachange

rin "I'm sure of it. I always have… reasons."

"The ensuing silence kills Lilly's hopes all too visibly. That didn't last long."

"Rin's, as far as I can tell unbased, assurances aside… what should be done?"

"We could just leave her to her own devices, whatever those are… but it's late and I don't think we'll be getting any thanks if Rin is found standing here in the middle of the night."

"Which she probably will, unless she manages to remember what she was doing here in the first place."

"As for me trying to guess what might've been going on in her mind when she decided to embark on this adventure, the chances seem to be on par with winning the lottery."

"Several times in a row."

"Lilly is oddly quiet too. I'd appreciate some support from the sidelines here, especially if she's more familiar with Rin than I am."

"But it can't be helped. It seems her familiarity with Rin is exactly why she's staying subdued."

hi "So, I assume you were going somewhere, not coming back to the school… any idea where?"

show rin relaxed_surprised_ni
show lilly cane_surprised_ni
with charachange

"Her eyes widen in shock and she jolts back in a somewhat artificial way, making it seem like an act rehearsed for situations like this."

rin "Are you a mind reader? Is that your disability? How unique!"

hi "No… What? Why would you think that?"

show rin relaxed_disgust_ni
show lilly cane_listen_ni
with charachange

rin "You knew what I was doing."

show lilly cane_displeased_ni
with charachange

hi "Eh, it was just an educated guess. We walked this same street in the other direction just before, to get to the store."

hi "If you were going to school, we would've met you on the way."

show rin basic_deadpanupset_ni
with charachange

rin "Oh."

"She looks a little disappointed."

"Like Kenji, Rin appears quick to jump to completely irrational conclusions."

"Maybe it's something in the water here. I make a mental note to stock up on soft drinks."

hi "You know, that is the second time this week that someone asked if I was a mind reader."

hi "Do I really give off that impression?"

show rin basic_deadpannormal_ni
with charachange

"Rin shrugs her shoulders, which is all the answer I get."

hi "You know—{w=0.3}{nw}"

show lilly cane_smile_ni
with charachange

li "Maybe you should come with us back to the school?"

"Lilly interjects just as I am about to further debunk my alleged mind-reading capabilities. She sounds rather concerned, the paper-thin smile on her face badly disguising that fact."

"Maybe she came to the same conclusion as I did. For everyone's sake, I decide to let the mind-reading topic drop, as it's entirely inane anyway."

hi "Yeah, Lilly's right. If you can't remember, there's no point staying here."

show rin basic_awayabsent_ni
with charachange

"Rin considers this rather simple deduction for a moment, then nods."

show rin basic_absent_ni
with charachange

stop music fadeout 2.0

rin "Okay."

scene bg school_road_ni
with shorttimeskip

$ renpy.music.set_volume(0.1, 0.0, channel="ambient")
play ambient sfx_cicadas
play music music_dreamy fadein 2.0

"We start towards the school again, having wasted way more time than necessary with this episode."

show rin basic_awayabsent_ni at tworight
show lilly cane_smileclosed_ni at twoleft
with charaenter

"Rin walks along the edge of the sidewalk in her arrhythmic way, looking like a mix of sleepwalker and rope dancer, while Lilly keeps one hand on my shoulder, tapping at the ground with her cane."

"Tap step step tap tap step step step."

"Apart from that and a few fragmented beginnings of conversation, it's quiet. A quiet quite apart from the relaxing one into town, at that."

hi "So how's the mural going?"

show rin basic_deadpan_ni
with charachange

rin "We are going to get bad luck. Never talk about works in progress."

show lilly cane_weaksmile_ni
with charachange

li "I'm sure it'll be wonderful."

show rin basic_deadpannormal_ni
with charachange

rin "Bad luck."

"Tap step tap step. She doesn't care to talk about it. Lilly's politeness feels out of place, for the first time. Step step step."

"The hill Yamaku rests on top of is surprisingly steep, going uphill. We slow the pace, but I still feel my pulse rising and breathing getting heavier."

"Almost there, I can see the gates already."

"More than that, though, I notice that Lilly's hand slightly tightens on my shoulder. Interpreting it as a gesture that she wants to ask something, I speak up."

hi "Anything wrong, Lilly?"

"I resist the urge to say “Aside from our traveling companion?” But only just."

"For a moment she seems to debate whether she should even bring it up, but goes for it anyway."

show lilly cane_concerned_ni
with charachange

li "Is everything… all right?"

hi "All right? How do you mean?"

"The fact I can't interpret her incredibly vague question puts her off, for a second."

li "It's just… you seem unusually tired, I guess."

"Now that she brings it up, I notice that my breathing is strangely heavy. The uphill walk has really done a job on me."


label th_choiceA30:
menu:
    with menueffect

    "Lilly noticed it all too quickly…"

    "Sorry, I'm not in very good condition.":
        return m1

    "I don't really want to talk about it.":
        return m2

label th_A30a:

$ renpy.music.set_volume(0.1, 1.0, channel="ambient")
stop music fadeout 5.0

hi "I… I'm fine."

hi "There's nothing to worry about, the hill is just surprisingly steep, don't you think?"

hi "I wonder what they have the school so high up here for anyway, don't we have students in wheelchairs and everything?"

show lilly cane_sad_ni
with charachange

li "Indeed."

show lilly cane_concerned_ni
with charachange

"Lilly's forehead wrinkles in concern, and I don't really want her to have that kind of an expression over me. We barely know each other."

hi "Yeah, my thoughts exactly. Not that you can find a place like this wherever, I guess, but it makes me wonder what they were thinking."

"My voice is overly calm, it sounds weird to my own ear and I speak way too fast. I briefly wonder how much Lilly can sense from someone's voice alone."

li "Mmm…"

hi "Let's continue. We're almost there anyway."

hide lilly
hide rin
with charaexit

"For the rest of the way back to the school, we all remain silent."

stop ambient fadeout 3.0

scene black
with Dissolve(3.0)


label th_A30b:

$ renpy.music.set_volume(0.1, 1.0, channel="ambient")

hi "It's all right, I just need to catch my breath. My condition isn't the best, these days."

show lilly cane_oops_ni
with charachange

li "Oh."

li "Is it something that… is related to you being transferred here? I mean…"

show lilly cane_concerned_ni
with charachange

"She cuts herself off rather abruptly, maybe realizing she was being a bit intrusive. Her instincts are sharp though, and while I don't like the subject it's not like I should lie about it."

"If it's Lilly, I don't think I mind."

hi "I'm just a little weak for the time being."

show lilly cane_oops_ni
with charachange

li "Hanako said you look fairly… healthy, so I naturally thought…"

show lilly cane_sad_ni
with charachange

"Lilly doesn't finish her sentence again, letting it trail off with a measure of concern."

"As she furrows her brow, Lilly's uncomfortable expression spurs me to say at least something to ease her feelings."

"It's surprising she's this flustered, considering her straightforward attitude with her own blindness. She must know that not all share her own comfort about such things."

hi "No, it's okay."

hi "I have a pretty… I guess the best way to put it would be messed-up… heart. Arrhythmia."

hi "I had a bad heart attack a while ago because of it, and spent most of the spring in a hospital. Ended in Yamaku on doctor's orders."

"She silently nods her head in acknowledgment."

"My answer, though, only seems to make Lilly furrow her brow even further. She doesn't seem to quite know how to react, given we don't really know each other that well."

"I can't really fault her for it, given I have the exact same reaction."


label th_A30c:

"To my surprise, in a moment's time her face shows that she comes to some sort of realization."

show lilly cane_oops_ni
with charachange

li "Wait… so the time when Emi and you collided in the hallway…?"

"I grimace slightly. Her ability to connect the dots quite so fast is unexpected."

hi "Yeah. I guess I'm a textbook example of why those rules about running in the corridors exist."

show lilly cane_sad_ni
with charachange

"That was a lot more dry than I'd intended. Lilly visibly shies away from continuing the topic."


label th_A30d:

"While I do want to assuage her concern, I really don't want to dwell on this either."

hi "Don't worry about it."

show lilly cane_weaksmile_ni
with charachange

"I try to offer a reassuring smile but then I realize the futility. Without knowing this, Lilly smiles at me reassuringly but doesn't say anything further."

$ renpy.music.set_volume(0.5, 5.0, channel="ambient")
stop music fadeout 2.0

scene bg school_dormext_half_ni
show rin relaxed_surprised_ni at tworight
show lilly cane_weaksmile_ni at twoleft
with shorttimeskip

"Arriving at the dorms, Rin stops in front of her mural as if lightning struck her. She had been so quiet for almost all of the walk back that I had all but forgotten she was here."

show rin relaxed_disgust_ni
with charachange

rin "It's Friday, isn't it?"

show lilly cane_smile_ni
with charachange

li "Yes… Friday, the eighth of June."

show rin basic_upset_ni
with charachange

play music music_rin fadein 0.5

rin "This is bad."

show lilly cane_surprised_ni
with charachange

li "Bad? Why?"

show rin negative_annoyed_ni
with charachange

rin "I think I am going to go in a fetal position and throw up. Possibly in reverse order."

show lilly cane_concerned_ni
with charachange

li "Is something wrong?"

show rin negative_confused_ni
with charachange

rin "No. Nothing is wrong. It's Friday and nothing is wrong yet. This mural, it's going to need to be finished by Sunday. So everything's all right."

show rin negative_worried_ni
with charachange

rin "Do you have any drugs? Or a time machine?"

show rin negative_confused_ni
with charachange

rin "This is not good. Not good."

"So she's behind her schedule. Recalling Shizune's exasperation at Rin's carefree attitude several days ago, I don't know what to think."

"She has left herself open for a “told you so” unless she can pull off whatever she needs to pull off by Sunday morning."

"Rin keeps staring at her mural looking as mortified as she can."

show rin negative_annoyed_ni
with charachange

rin "Leave me. I'm going to need to work for a while."

"I glance at Lilly, expecting her to share an incredulous look with me as I roll my eyes, but then I realize she's not one to do that kind of thing."

show rin negative_angry_ni
with charachange

rin "Leave me."

stop music fadeout 2.0

hide rin
with charaexit

show lilly cane_concerned_ni at center
show bg school_dormext_half_ni at bgright
with charamove

"We do, of course, not wanting to aggravate her any more than she already is."

"There is a churning bad feeling in my gut. Rin sure has a knack of making people feel worried about her."

"She seems like a person who should never be left alone."

hi "Maybe we should call someone? She sounded like she was going into shock or something."

show lilly cane_oops_ni
with charachange

li "I'm sure she will be just fine. She's just a… eeeh… how to say…"

"Lilly cocks her head a little, trying to find a polite way of calling Rin crazy without calling her crazy."

hi "Unique?"

show lilly cane_weaksmile_ni
with charachange

li "Yes, a very unique person."

hi "I guess you could say that."

show lilly cane_giggle_ni
with charachange

"She giggles at the notion melodiously, nodding in agreement."

show lilly cane_weaksmile_ni
with charachange

li "Sorry about leaving you stranded as you talked to her. I… don't really understand her, so I keep my distance."

"So my guess was right. Lilly offers a slight, apologetic smile as if she was sorry that her own shortcomings have prevented her from becoming closer to Rin."

"I'm not one to blame her. At all."

"Lilly lets slip a long breath, probably a disguised yawn. I imagine she's as exhausted by all this as I am."

show lilly cane_cheerful_ni
with charachange

li "I'd better leave now and give these to Hanako. Thank you for the company, Hisao."

"She smiles very sweetly at me. It feels different than normal, despite the fact that she seems to be smiling so often."

"I can't put my finger on what the difference is. It's just different."

"Relaxed, I'd say, but that's probably just relief over getting rid of Rin. Maybe."

hi "Yeah… good night. Say hi to Hanako for me."

show lilly cane_smile_ni
with charachange

li "I will. Good night."

hide lilly

stop ambient fadeout 2.7

scene black
with Dissolve(3.0)

return

