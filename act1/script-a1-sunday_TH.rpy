label th_A38:
#Dawn of the Final Day

window hide None

scene black
with dissolve

scene bg school_dormhisao
with openeye

play music music_daily fadein 4.0

window show

"วันถัดมาฉันตื่นมาพร้อมความรู้สึกมึนหัวเล็กน้อย เกือบเที่ยงแล้ว"

$ renpy.music.set_volume(1.0,0.0, "ambient")

"เมื่อคืนนอนดึกเพราะวันนี้วันอาทิตย์ แถมไม่มีเรียนอีกต่างหาก"

"แต่วันนี้ไม่ใช่วันอาทิตย์ธรรมดา ๆ ยังมีงานด้วย"

"พอมองผ่านหน้าต่างไปก็เห็นคนที่แผงบะหมี่โซบะจัดจานให้คนที่กำลังมองหาอาหารขยะอยู่"

"ฉันกินยารอบเช้าแล้วนั่งคิดว่าวันนี้จะทำอะไรดี"

"สัปดาห์หน้าก็จะมีสอบ แต่ฉันก็ไม่ได้คิดว่าหนักหนาอะไรอย่างคนอื่น เลยไม่ได้พะวงเรื่องนั้นมากมาย"

"เมื่อไม่มีหน้าที่ที่ต้องไปเข้าชั้นเรียน วันนี้ทั้งวันก็คงไปสนุกกับงานเทศกาลได้เต็มที่"

scene bg school_dormhallway
with locationchange

"พอทำกิจวัตรยามเช้าเสร็จฉันก็ออกมาที่โถงทางเดิน หมายมั่นว่าจะไปหาอะไรกิน"

"อยู่ ๆ ก็นึกอยากรู้ขึ้นมาว่าวันนี้เคนจิจะทำอะไรเมื่อเดินผ่านประตูห้องของเขา"
   
"จะมีแพลนอะไรหรือเปล่า เพราะคนอื่นต่างก็มีอะไรให้ทำทั้งนั้น"

"แต่ก็พอนึกภาพออกอยู่ว่าห้องของเขาคงบุฉนวนกันเสียงเอาไว้"

"หรือไม่ก็ปราการสักอย่างที่แปะป้ายว่า “ผู้หญิงห้ามเข้า” เอาไว้"

"…แล้วก็มีรอยขีดฆ่าคำว่า “ผู้หญิง” แล้วมีตัวหนังสือยุกยิกเขียนว่า “คน” เอาไว้ข้างล่างแทน"

stop music fadeout 2.0

play sound sfx_doorknock2

"ฉันเคาะประตู ยังดีที่ไม่มีป้ายอะไรแปะไว้ แล้วฉันก็ได้ยินเสียงปลดล็อกสักสิบชั้นอันน่าขนลุกขั้น ประตูเปิดดังเอี๊ยด"

show kenji neutral at Slide(0.0,0.3,0.0,0.2,0.5)
with Dissolve(.5)

ke "ใครน่ะ"

hi "อันนั้นต้องถามก่อนเปิดเปล่า"

show kenji neutral at center
show bg school_dormhallway at bgright
with charamove

play music music_kenji fadein 1.0

ke "อ้อ นายนี่เอง โห มาแต่เช้า"

hi "ก็ไม่ได้เช้าขนาดนั้นนะ"

show kenji happy
with charachange

ke "แล้วมีไร"

hi "เปล่า แค่จะมาถามว่าวันนี้นายจะทำอะไรมั้ย"

hi "ข้างนอกนั่นมีคนค่อนโรงเรียนได้มั้ง"

show kenji rage
with charachange

ke "ข้างนอกไหน ทำไม"
   
hi "ฮะ?"

ke "ฮะอะไร วันนี้มีอะไรพิเศษ ทำไมถึงอยู่ข้างนอก ใครอยู่"

show kenji tsun
with charachange

ke "เหมือนได้ยินเสียง ดังชะมัด…นี่อย่าบอกนะ…ว่าเริ่มบุกแล้ว"

"จู่ ๆ เขาก็ตื่นตัวขึ้นมา"
   
show kenji neutral
with charachange

ke "แล้ววันนี้วันอะไร"
   
hi "อ่อ นายคงไม่เห็นแผงไม้ที่มีคนขายของที่อยู่ข้างนอกสินะ…"

ke "พูดเรื่องไรวะ ฉันปิดม่านไว้ตลอดกันพวกซุ่มยิงนะเฮ้ย"

hi "เอ่อ งานเทศกาลไง นายรู้…ใช่มั้ย"

show kenji tsun
with charachange

ke "เชี่ย วันนี้แล้วเหรอวะ โอ๊ย แม่ง โอ๊ย…แม่ง แม่งเอ๊ย"

ke "ลืมไปได้ไงเนี่ย ยังทำป้อมไม่เสร็จเลย แย่แน่"

ke "วันนี้ต้องเป็นวันที่แย่มากแน่ ๆ …ดีนะที่นายมาบอกก่อน วันนี้เป็นวันที่แย่แน่"

hi "ทำไม"

show kenji neutral
with charachange

ke "โอย ต้องอยู่กันเต็มข้างนอกนั่นแน่ คนน่ะ อยู่นอกหน้าต่าง ปฏิสัมพันธ์กัน!"

"เคนจินวดหน้าผากด้วยความลนลานพร้อมทำหน้าเสียขึ้นมา"

show kenji tsun
with charachange

ke "ดังฉิบหายวายวอดแน่ ๆ แม่ง วันนี้กะจะออกไปข้างนอก แผนเสียหมด ทุกอย่างเสียหมดแล้ว"

ke "แย่โคตร โคตรแย่ แย่!"

ke "อะไรวะเนี่ย โคตรจะแย่ ไปไหนก็ไม่ได้แล้ว หนีไปไหนไม่ได้แล้ว"

"เคนจิดูลนลาน จะว่าตื่นตระหนกเลยก็ยังได้"

show kenji neutral
with charachange

ke "ไม่อยากจะเชื่อ วันนี้คืออย่างนี้นี่เอง"

ke "แม่ง แล้วไม่ได้เตรียมอะไรไว้เลย"

show kenji tsun
with charachange

ke "ฉันยังไม่ได้เตรียมใจไว้ด้วยซ้ำ แล้วก็ถึงวันนี้แล้ว แล้วก็ทำอะไรไม่ได้เลย นายน่าจะมาบอกให้เร็วกว่านี้นะ คือ อย่างน้อย\nก็รู้แหละ แต่…น่าจะได้รู้ให้เร็วกว่านี้สิ! ไม่งั้นนะคง…"

hi "โทษที นึกว่ารู้แล้ว"

hi "สรุปก็คือจะไม่ทำอะไร?"
 
hi "อากาศก็ดีนะ เมื่อวานลมพัดแรงมากจนนึกว่าวันนี้จะหนาว แต่ก็ไม่ จะอุดอู้อยู่แต่ในห้องไปทำไม เออ มาเดินดูงาน\nเถอะน่า"

"เคนจิครวญแล้วใช้มือปิดหน้า"

ke "อ๊าก ไม่ ไม่! ฉันทำไม่ได้ ออกไปโดนจับกินแน่ ฉันรู้"
    
"พูดเล่นแน่ ๆ แต่ที่พูดเมื่อกี้ก็ทำหน้าซื่อ ๆ ซื่อที่สุดถ้าเทียบกับหน้าแบบอื่นอะนะ"
    
show kenji happy
with charachange

ke "แล้วนายจะทำอะไร มาอยู่กับฉันช่วยสร้างป้อมนี่มา ถ้าช่วยกันทำอาจจะยังทันนะ"



label th_A38a:
#If on Shizune's route

hi "ฉันจะไปอยู่กับพวกสภานักเรียนอะ พอดีแพ้พนันมา"

"ฉันนึกขึ้นได้ว่ายังไม่ได้ตกลงกันเลยว่าจะเจอที่ไหนเมื่อไหร่ อยู่คอยพวกเธอคงดีกว่าไปคลาดกับฝูงชนข้างนอก ยังไง\nก็อาจจะกำลังวุ่นวายกับการจัดการงานด้วย"

"ก็ตลกดี นึกว่าถ้าแพ้เกมโง่ ๆ ของชิซูเนะแล้วจะเจออะไรหนัก ๆ เสียอีก อันนี้แค่ข้ออ้างอยากอยู่ด้วยกันมากกว่า ถ้างั้น\nเธอก็คงแค่อยากให้ฉันได้สนุกแหละ"

"แม้เธอจะไม่ได้พูดเจตนาออกมาตรง ๆ แต่อย่างไรก็คงเป็นเจตนาที่ดีแหละนะ ชักชอบเธอขึ้นมาแล้วสิ"

hi "จะไม่ไปก็ได้อะนะ แต่คงเสียดายแย่ แล้วฉันก็อยากไปด้วย แบบ วันนี้ก็ดูน่าตื่นเต้นดี น่าสนใจอะไรงี้"

show kenji tsun
with charachange

stop music fadeout 1.0

ke "สภานักเรียน? ฮะ? ยังมีอยู่เหรอ"

ke "เหมือนจะมีกันแค่สองตัวไม่ใช่เรอะ"

hi "คน ไม่ใช่ตัว"

play music music_tension

show kenji rage
with charachange

ke "เรอะ? แล้วน่ารักมั้ย โห ไม่ เดี๋ยว…น่ารักมั้ยอะ"

ke "ไม่สิ! ไม่สำคัญ! ฉันได้ยินมาว่าประธานนักเรียนเขาน่ะบ้า…ไม่เคยมีใครได้คุยด้วย สั่งอะไรก็สั่งผ่านลิ่วล้อหมด"

show kenji tsun
with charachange

ke "เชี่ย เป็นเหมือนกันทุกที่เลย…ฟังดูแล้วคงเป็นยัยเย็นชา มีแต่คนยัยแบบนั้นเต็มไปหมด"

ke "ถ้าเป็นผู้หญิงสองคน นายก็แพ้หนึ่งต่อสอง อันตรายนะเว้ย ใครจะไปรู้ว่าอะไรจะเกิดขึ้น"

ke "แม่ง สภานักเรียนมีอยู่แค่สองคน แต่มีพลังขนาดนี้"

ke "ต้องหยุดยั้งไว้ให้ได้"

ke "ฉันนึกภาพออกเลย เวลานั่งวางแผนกันเพื่อผลักดันแนวคิดสตรีนิยม ฉันวางใจองค์กรแบบนั้นไม่ลงหรอก"

ke "ไม่ดีเลย ไม่ดี!"

show kenji rage
with charachange

ke "โธ่ แม่ง! แม่ง!"



label th_A38b:
#If on Lilly or Hanako's route

hi "I don't know. I'm pretty hungry so I thought I'd get some food first and then check out the attractions."

hi "Your class project seemed pretty cool, and I gave a hand with it so I want to see at least that one and chat with Lilly I guess."

hi "Speaking of that, don't you have any obligation for the project?"

show kenji rage
with charachange

ke "Are you out of your mind?"

ke "That blind broad is up to no good; I can feel it in my spleen, man. Her presence is like a dark shadow that's in the way of my great vision."

ke "As expected of blind people."

hi "What."

hi "Besides, I thought that you were also…"

show kenji neutral
with charachange

"He holds up his hand to interrupt me."

ke "Only legally."

ke "Metaphorically, I can see farther than any man before me has seen."

"Kenji looks stoically into the metaphorical distance to emphasize his statement, thrusting his chin forward to look manlier. Actually it's just the corridor wall two meters away but it's all the same."

show kenji tsun
with charachange

ke "I can see the future of mankind, and it's a dark one unless the threat of women is stifled."

ke "They are everywhere."



label th_A38c:
#If on Rin's route

hi "อืม พอดีฉันเข้าชมรมศิลปะแล้ว ก็คงไปอยู่กับพวกนั้นนั่นแหละ"

show kenji rage
with charachange

ke "นายทำอะไรนะ"

hi "เข้าชมรมศิลปะ"

show kenji tsun
with charachange

ke "พลาดละ พลาดมาก นายไม่รู้หรอกในชมรมศิลปะจะมีผู้หญิงแบบไหนบ้าง อาจจะมีพวกหน้าซื่อใจเศร้าที่จะกระซวก\nอกนายควักหัวใจออกมากิน"

"ฉันก็รู้จักสมาชิกชมรมศิลปะอยู่คนหนึ่งอะนะ แล้วรินก็คงไม่แบบวันดีคืนดีกลายเป็นฆาตกรโรคจิตอย่างนั้น"

hi "ดูจะเป็นไปไม่ได้นะ"

ke "อย่าพูดงั้นสิ อย่าหลอกตัวเองเลย นายไม่รู้หรอกตอนนี้นายเจอกับอะไรอยู่ พวกนี้น่ะสุด ๆ แล้ว"

show kenji neutral
with charachange

ke "พวกนั้นจะใช้ฉากสดใสบังหน้าล่อนายให้เข้าไป แล้วพอนายไม่ทันระวังตัวเมื่อไหร่ละก็ ตึ้ง!"

hi "ตึ้ง นี่คือ?"

"เคนจิดูงง ๆ กับคำถามของฉัน แต่ก็ไม่ได้ทำให้เขาดูบ้าน้อยลงเท่าไหร่"

show kenji tsun
with charachange

ke "ไม่สำคัญหรอก"

ke "ระวังตัวเอาไว้ ระวังตัวเอาไว้"    



label th_A38d:
#If on Emi's route

hi "นั่นสิ…ฉันก็หิว ๆ แล้ว แต่ฉันก็ตกลงไปแล้วว่าจะดูแลตัวเองให้ดีขึ้น แบบว่าให้สุขภาพดีอะไรงี้"

hi "ไม่รู้ว่าจะเลี่ยงทาโกยากิหรือจะกิน ๆ ไปเลยดี"

show kenji tsun
with charachange

ke "ตกลง? ฟังดูไม่ดีเลยนะ แล้วนายจะได้อะไร"

hi "ก็ไม่ได้อะไรมั้ง ไม่ใช่ข้อตกลงแบบนั้นสักหน่อย"

hi "นายรู้จักเอมิที่อยู่รุ่นเดียวกับเรามั้ย นั่นแหละ ก็ตกลงกันว่าจะคอยดูกัน แล้วก็…"

show kenji rage
with charachange

ke "อ๊าาาาาาาก!"

"เสียงกรีดร้องกับสีหน้ากลัวสุดขีดของเคนจิเล่นเอาตัวฉันชาวาบ ราวกับฉันบอกหลวงพ่อที่โบสถ์ว่าขายวิญญาณ\nให้ปีศาจไปแล้วก็มิปาน"

ke "เธอคนนั้น! นายขายวิญญาณให้ปีศาจ แล้วไม่ได้อะไรตอบแทนเลยอะนะ"

ke "นายเป็นอะไรไปแล้วเนี่ย"

ke "นายรู้มั้ยว่านายไปตกลงกับใครน่ะ"

ke "เธอน่ะคือภัยต่อประชาชีเลยนะ นายไม่รู้เหรอว่าแต่ละเดือนมีตั้งกี่คนที่โดนเธอเอาตัวเข้ากระแทกแบบแม่นมาก\nจนต้องนอนโรงพยาบาลน่ะ"

show kenji tsun
with charachange

ke "เธอคือพวกนั้น! ตัวการสำคัญในทฤษฎีสมคบคิดนี้ที่จะทำให้ทุกความเป็นชายชาตรีต้องยอมสยบ"

ke "ไม่อยากเชื่อหูตัวเองเลย อุตส่าห์ไว้ใจการตัดสินใจของนาย นึกว่าจะเป็นพวกกัน"

ke "นายต้องรีบถอนตัวก่อนสายไปนะ"

ke "งานนี้ก็ด้วย เป็นแค่แผนหนึ่งของพวกนั้น"



label th_A38e:

"He fingers his scarf nervously, faster and faster like he is trying to start a fire, then slowly begins to calm down once the panic attack finishes running its course."

show kenji neutral
with charachange

ke "I'm going to have to find some place to hide in, a safe haven. And then knock the lights out of myself so that I don't have to experience this horrible day."

ke "I have the perfect thing for that. I must prepare now."

show kenji tsun
with charachange

ke "Don't go to the festival."

hi "Okay."

show kenji neutral
with charachange

ke "Later, dude."

stop music fadeout 2.0

hide kenji
with charaexit

"The door slowly closes with a low creak and I don't know how to feel about what Kenji just said."




label th_A44:

show bg school_dormhallway at bgright
with None

"ฉันคิดอยู่ว่าจะทำอะไรตอนอยู่กับชิซูเนะและมิช่าดี พอคิดได้ว่าเตรียมไว้ก่อนจะดีที่สุดฉันก็กลับเข้าห้องไปเอาเงิน\nตุนเข้ากระเป๋าสตางค์"

scene bg school_dormhisao
with locationchange

"จะมีเกมนั้นมั้ยนะ ที่ให้เอาที่ตักกระดาษช้อนปลาทองขึ้นมา"

"เป็นเกมที่ดูไม่ได้ยากอย่างที่เห็น แต่ว่าต่อให้ได้ปลาทองมาแล้วก็ไม่รู้จะเก็บไว้ทำไมเหมือนกัน"

"ห้องเล็ก ๆ แบบนี้จะเอาปลามาทำอะไร เอามาทำกับข้าวกินงี้เหรอ"

"จะเอาให้ชิซูเนะก็ได้แหละ แต่ก็คงจะล้ำเส้นไป"

"นั่นแหละคือปัญหา ทั้งสองคนก็น่ารัก แต่ฉันไม่คิดว่าจะตกใครสักคนได้หรอก แต่ถึงงั้นฉันก็มาคิดดูอีกทีอยู่ดีว่าถ้า\nคืนนี้ให้ของขวัญอย่างปลาไม่ก็ตุ๊กตาไปแล้วสองคนนั้นจะตอบรับยังไงนะ"

"มิช่าอาจจะหัวเราะอย่างเคย ส่วนชิซูเนะก็คงปัดทิ้ง"

"อาจจะไม่ใช่ความคิดที่ดีสักเท่าไหร่"

"โอเค น่าจะลงตัวละ"

with shorttimeskip

"ผ่านไปสักพักฉันก็คิดว่านี่คงเป็นอีกแผนที่ชิซูเนะวางไว้หลอกฉันอีก หรือต่อให้ไม่ใช่ ตอนนี้ก็เริ่มเย็นแล้ว"

"ฉันตัดสินใจออกไปหาพวกเธอ ถึงจะยังไม่รู้ก็เถอะว่าต้องไปหาที่ไหน วันนี้อาจจะตามตัวยากมากด้วย"

scene bg school_dormhallway
show shizu behind_blank_close at center
with locationchange

"พอเดินออกมาก็เกือบชนเข้ากับชิซูเนะ"

hi "ไง ชิซูเนะ มิช่าอยู่ไหนเหรอ"

show shizu behind_frustrated_close
with locationchange

"ฉันพยายามทำภาษามือสุดความสามารถ แต่ก็แค่ทำไปมั่ว ๆ นั่นแหละ ไว้ต้องขอให้มิช่าสอนบ้างแล้ว"

mi "อยู่นี่!"

play music music_comedy

show shizu behind_frustrated_close at Slide(0.5,0.5,0.7,0.5,1.0, time_warp=_ease_time_warp)
with None

show misha hips_grin behind shizu at Slide(0.5,0.5,0.3,0.5,1.0)
show shizu behind_frustrated_close at Slide(0.5,0.5,0.7,0.5,1.0,time_warp=_ease_time_warp)
with Dissolve(0.7)

"มิช่าโผล่มาจากข้างหลังชิซูเนะแล้วฉีกยิ้มกว้าง"

mi "พวกเรามารับนายให้ไปที่งานเทศกาลด้วยกัน"

show shizu basic_angry_close at tworight
with charachange

shi "…"

show misha sign_smile at twoleft
with charachange

mi "อย่าคิดผิดสัญญาเชียว~!"

hi "สัญญาเหรอ ฉันว่าฉันไม่ได้สัญญาอะไรไว้นะ"

show shizu cross_angry_close
with charachange

shi "…"

show misha hips_frown
with charachange

mi "เลิกเล่นตัวได้แล้วน่า!"

show misha perky_sad
with charachange

mi "เถอะน่า ฮิจัง สนุกแน่! นายต้องมานะ ไม่งั้นก็กลายเป็นคนไม่เอาถ่านหรอก!"

show misha perky_smile
with charachange

mi "นายคงไม่ได้อยากเป็นคนที่เอาแต่นั่งระแวงอุดอู้อยู่ในห้องทั้งวันหรอกใช่มั้ย"

"ฉันมองข้ามไหล่เธอไปยังประตูห้องของเคนจิที่อยู่อีกฟาก"

"หวังว่าเขาจะไม่ได้ยินนะ แต่มิช่าคงอยากให้ได้ยินน่ะแหละ"

hi "ไม่ ไม่เลย ฉันแค่หยอกนิดหน่อยหรอก กำลังจะออกไปแล้วเนี่ย เธอสองคนไม่ต้องมานี่ก็ได้"

show misha cross_laugh
with charachange

mi "จริงเหรอ อะฮ่าฮ่าฮ่า! ชิจังก็นึกว่านายจะเผ่นไปก่อนแล้ว!"

show misha hips_grin
with charachange

mi "พวกเราต้องการนายนะฮิจัง~!"

hi "หา?"

"เมื่อกี้รู้สึกเหมือนหัวใจกระตุกวูบไปเลย"

show misha perky_smile
with charachange

mi "พอดีมันมีอยู่เกมนึง แล้วฉันปาบอลไม่แม่นพอที่จะให้ตุ๊กตาล้มน่ะ…แล้วชิจังก็ไม่ยอมปาของด้วย"

hi "อ้อ"

"ชิซูเนะจ้องมาทางฉันแล้วเห็นสีหน้าที่ผิดหวังของฉันทันที เธอคลายแขนที่กอดอกอยู่ออกแล้วดันแว่น"

show shizu adjust_happy_close
with charachange

shi "…"

mi "นายคิดอะไรอยู่น่ะ ฉันไม่ปาของหรอกนะ"

show misha perky_confused
with charachange

mi "ทำไมล่ะชิจัง แปลก ๆ นะ…"

show misha perky_smile
with charachange

mi "เอาเถอะ ฮิจัง นายเคยปาบอลมาก่อนใช่มั้ย~ ใช่มั้ย~ นั่นแหละ! นายต้องมากับพวกเรา!"

"ทึ่งกับตรรกะของพวกเธอจริง ๆ ไม่รู้ว่านี่พูดเล่นหรือพูดจริงเลย"

hi "ฮะ ๆ ถ้าไม่ติดว่าพวกเธอพูดเล่นนี่ฉันโกรธไปแล้วนะเนี่ย"

hi "พูดเล่นใช่มั้ย"

show shizu behind_frown_close
with charachange

shi "…"

mi "มันก็เป็นตามนั้นแหละฮิจัง~! เป็นตามนั้นตามนี่ตามนู่นตามนั่น!"

hi "ค่อยโล่งหน่อย"

show shizu basic_normal2_close
with charachange

shi "…"

show misha hips_smile_close at closeleft
with characlose

mi "มาเถอะ ไปกัน! นอกห้องนายวงหูหนวกเขากำลังเตรียมจัดกันเลยนะ"

"มิช่าคว้าแขนฉันแล้วพยายามลากให้ฉันออกมาจากประตู แต่ชัดว่าเธอจงใจไม่ใส่แรงเลย"

hide shizu
with None

show shizu basic_normal2_close behind misha at tworight
with None

show shizu adjust_blush_close
with charachange

stop music fadeout 3.0

"ชิซูเนะมองมาทางพวกเราทั้งสองคน แก้มเธอแดงเล็กน้อย มือเธอจับแว่นดูร้อนรน"

"ไม่ค่อยชินกับการทำตัวสบาย ๆ ไม่ทางการอย่างนี้เลย แต่ก็ไม่ได้มีปัญหาอะไรหรอก จะให้ปฏิเสธยังไงลง"

play ambient sfx_crowd_outdoors fadein 1.0

scene bg school_courtyard
show crowd
with locationskip

play music music_running

"ข้างนอกยังมีแดดอยู่ แต่พระอาทิตย์ก็เริ่มคล้อยต่ำลงหลังต้นไม้แล้ว"

"ดูเหมือนคนค่อนโรงเรียนจะมาออกันที่นี่ ฉันเห็นพนักงานบางคนยืนอยู่ตามข้างทางซื้อน้ำผลไม้กันอยู่"

"น้ำผลไม้จะหมดถังแล้ว สาวที่ขายอยู่ก็ดูลนลาน"

"แม่หมอบางคนก็คุยเรื่อยเปื่อยอยู่กับเพื่อน คนอื่นที่ทายทักเรื่องดวงชะตาราศีกับคนที่เดินผ่านไปมาบ้างก็มี"

"รู้สึกจะเป็นวิธีที่รุกหนักไปหน่อย แต่ก็แสดงให้เห็นว่าใจรักจริง เป็นภาพที่แปลกตาดี ไม่รู้ว่าจะชินได้หรือเปล่า"

show shizu basic_normal2 at tworight
show misha perky_smile at twoleft
with charaenter

shi "…"

show misha sign_smile
with charachange

mi "ไปหาอะไรกินกันดีกว่า หิวมั้ยฮิจัง"

"จะว่าไปวันนี้ทั้งวันก็ยังไม่ได้กินอะไรเลย"

hi "ไม่ค่อยอยากกินผัดหมี่เท่าไหร่อะ"

show misha hips_grin
with charachange

mi "ไม่เป็นไรน่า ของผัดของทอดอื่นก็มี"

hi "ไม่มีอย่างอื่นนอกจากพวกผัดทอดแล้วเหรอ"

show shizu adjust_smug
with charachange

shi "…"

mi "ขนมไง เลี้ยงฉลองก็ต้องกินอาหารขยะสิ!"

show misha cross_laugh
with charachange

mi "วะฮ่าฮ่าฮ่าฮ่า!"

show shizu behind_smile
with charachange

shi "…"

show misha hips_grin
with charachange

mi "เถอะน่า เดี๋ยวฉัน—เอ่อ หมายถึงชิจังนะ—จะเลี้ยงให้อย่างนึงเอง~!"

mi "อย่างนึงเหรอ"

show shizu adjust_smug
with charachange

shi "…!"

show misha sign_smile
with charachange

mi "แค่อย่างเดียว~! จะได้มีแรงไปเหวี่ยงแขนปาของ!"

show misha perky_smile
with charachange

mi "อ๊ะ แต่บางแผงก็เหมือนจะยังจัดไม่เสร็จนะ อาจจะยังมีบางอย่างที่นายอยากกินแต่ยังไม่ขายด้วย"

"เมื่อมองไปรอบ ๆ ก็ต้องตะลึงกับจำนวนแผงในงาน เหลือเชื่อมาก เป็นงานที่ดูใหญ่กว่าที่เห็นตามเมืองจริง ๆ เสียอีก"

"ถึงมิช่าจะบอกอย่างนั้น แต่ดูเหมือนว่าคนค่อนโรงเรียนก็มาฉลองกันแล้ว"

"จำนวนนักเรียนที่ว่านั้นเติมเต็มบรรยากาศด้วยเสียงเซ็งแซ่"

"กลิ่นอาหารก็โชยมา ยิ่งได้กลิ่นก็ยิ่งหิว"

show shizu behind_frustrated
with charachange

shi "…"

show misha perky_confused
with charachange

mi "เร็วสิฮิจัง อาหารมันหมดลงเรื่อย ๆ แล้วนะ! ถ้าอยากกินทาโกยากิก็รีบไปกันได้แล้ว!"

show misha hips_grin
with charachange

mi "อยากกินทาโกยากิบ้างจังเลยนะ~! มาสิ กินกัน!"

hi "ก็ได้ ไม่ได้กินเป็นชาติแล้วด้วย ตกลง"

hide shizu
with charaexit

hide misha
with charaexit

"ชิซูเนะเดินออกไปก่อนมิช่าจะทันทำภาษามือให้ทันด้วยซ้ำ เธอก้าวฉับ ๆ ไปที่แผงทาโกยากิ ส่วนฉันกับมิช่าก็เดิน\nตามไป"

scene bg school_stalls1
with locationchange

"มิช่าหัวเราะพลางโลดเต้นไปหาชิซูเนะที่กำลังชูสามนิ้วสั่งทาโกยากิสามที่"

"เพิ่งสังเกต แต่รู้สึกแปลกหน่อย ๆ ที่คนอย่างชิซูเนะที่จุกจิกกับเรื่องชาชั้นสูงขนาดนั้นจะสนใจอาหารขยะอย่างนี้"

"ฉันรับจานทาโกยากิที่เธอยื่นมาพลางคิดว่าจะกินเลยดีหรือเปล่า ดูจะยังร้อน ๆ อยู่"

"ยังเห็นควันฉุย ๆ กับน้ำมันที่เดือดอยู่เลย"

show misha hips_smile at Slide(0.2,0.5,0.3,0.5,1.0)
show shizu behind_blank at Slide(0.8,0.5,0.7,0.5,1.0)
with Dissolve(1.0)

"ชิซูเนะกับมิช่ามองมาทางฉันราวกับจะรอให้ฉันกินเปิดก่อน"

"จะถอยก็ไม่ได้แล้ว ฉันหยิบส้อมพลาสติกอันเล็กที่ปักตั้งโด่อยู่ที่มุมหนึ่งของจานขึ้นมา"

show misha hips_grin at twoleft
show shizu basic_normal at tworight
with charachange

stop music fadeout 12.0

"แต่ยังไม่ทันได้เอาเข้าปาก ชิซูเนะกับมิช่าก็เริ่มกินกันไปก่อนแล้ว ชิซูเนะคอยละเลียดกินทาโกะยากิ ส่วนมิช่า\nก็กินอย่างเอร็ดอร่อยอย่างเด็กเล็ก ๆ "

"ยังไงเสีย พวกเธอสองคนก็เป็นเด็กอย่างคนอื่น ๆ ที่นี่ละนะ"

"ดีเหมือนกันแฮะ รู้สึกไม่ได้ออกมาเที่ยวกับใครแล้วสนุกกันไปตามประสาอย่างนี้นานมากแล้ว"

"ปีก่อนย้ายมาที่นี่ก็เป็นปีที่ยุ่งมาก ยุ่งมากเสียจนไม่ทันรู้ตัวว่าพลาดอะไรไปบ้าง"

"พอได้อยู่ที่นี่แล้วก็รู้สึกสบายใจ"

"เป็นบรรยากาศที่ชวนให้ผ่อนคลาย ไม่ยักรู้เลยว่างานแบบนี้ยังมีจัดกันอยู่ด้วย"

show misha perky_confused
with charachange

mi "อ้าว ฮิจัง ไม่กินเหรอ"

hi "กิน กินสิ"

show shizu adjust_smug
with charachange

shi "…"

show misha sign_smile
with charachange

mi "หวังว่านายคงไม่ได้ป๊อดไปก่อนเพราะกลัวร้อนหรอกนะ"

hi "ไม่ใช่อย่างนั้นสักหน่อย"

"แม้แต่ที่พวกเธอแซวก็เริ่มรู้สึกว่าเอ็นดูขึ้นมา"

$ renpy.music.set_volume(0.6, 2.0, "ambient")

scene bg school_stalls1_ss
with shorttimeskip

play music music_tranquil fadein 1.0

"ฉันรีบกินก่อนที่มันจะเย็นชืด คิดไปพลางว่าโคมกระดาษที่ส่องแสงนวลสลัวตัดกับพระอาทิตย์ยามเย็นนั้นช่างเป็นภาพ\nที่งดงาม"

show shizu behind_smile_close_ss at center
with charaenter

"ก่อนที่จะกินทาโกยากิคำสุดท้ายจนหมดชิซูเนะก็มายืนอยู่ตรงหน้าตัวตรงเด่เอามือไพล่หลัง"

"คงจะทำท่าให้ดูจริงจังที่สุดเท่าที่ทำได้ แต่ก็ปิดตัวเธอที่อารมณ์ดีไว้ได้ไม่มิดหรอก เพราะยังมีรอยยิ้มจาง ๆ อยู่\nบนใบหน้าเธอ"

show bg school_stalls1_ss at bgright
show shizu behind_smile_close_ss at closeright
with charamove

show misha cross_laugh_ss at twoleft
with charaenter

mi "อะฮ่าฮ่าฮ่า~! มา ๆ ฮิจัง มาเล่นเกมกัน!"

hi "ตั้งแผงกันเสร็จแล้วเหรอ"

show shizu adjust_happy_close_ss
with charachange

shi "…"

show misha cross_grin_ss
with charachange

mi "ไม่อะ แต่ไม่สำคัญหรอก ไม่สำคัญ~! เถอะน่า ฮิจัง เดี๋ยวคนก็เยอะหรอก!"

show misha hips_grin_close_ss at closeleft
with characlose

"มิช่าตบบ่าฉันแล้วหัวเราะเสียงดังมาก"

show misha perky_smile_close_ss
with characlose

mi "มา! มา! ปีนี้รางวัลดูใหญ่มาก ม้ากมาก~! ไม่อยากสอยสักอย่างมาให้สาวน้อยน่ารักสองคนอย่างพวกเราบ้างเหรอ"

"มิช่าทำหน้า “น่ารัก” ที่สุดขึ้นมา ซึ่งก็น่ารักเอาการ ฉันหันมองชิซูเนะด้วยคาดหวังว่าจะทำเช่นเดียวกัน แต่เธอมองมา\nเหมือนฉันสติไม่ดีไปแล้ว"

show shizu cross_wut_close_ss
with charachange

shi "…"

show misha hips_grin_close_ss
with characlose

mi "มิช่า เลิกทำอย่างนั้นเลยนะ!"

show misha perky_confused_close_ss
with charachange

mi "เดี๋ยวนะ…ฉันคือมิช่า…"

show shizu basic_normal2_close_ss
with charachange

shi "…"

show misha sign_smile_close_ss
with charachange

mi "ฮิจัง เร็วหน่อย นายถือทาโกยากิอันนั้นมาเป็นพันปีแล้วนะ!"

show misha cross_laugh_close_ss
with charachange

mi "ฮ่าฮ่าฮ่าฮ่าฮ่า!"

show misha cross_smile_close_ss
with charachange

hi "ฉันเป็นคนที่กินอะไรแล้วต้องดื่มด่ำไปกับรสชาติน่ะ แม้แต่เจ้านี่ก็ด้วย"

show shizu basic_sparkle_close_ss
with charachange

show shizu adjust_smug_close_ss
with charachange

"แล้วชิซูเนะก็หยิบทาโกยากิที่อยู่ในมือฉันแล้วเอาเข้าปากไปด้วยรอยยิ้มอย่างไม่มีปี่มีขลุ่ย"

"มันเกิดขึ้นเร็วมากจนฉันไม่มีทางที่จะหยุดเธอได้ทัน"

show misha cross_laugh_close_ss
show shizu behind_smile_close_ss
with charachange

"สมองยังไม่ทันประมวลผลสิ่งที่เกิดขึ้น มิช่าก็หัวเราะก่อนแล้ว ส่วนชิซูเนะก็ยิ้มให้ฉัน คงเป็นครั้งแรกที่เธอยิ้มจนเกือบ\nจะหัวเราะอย่างนี้"

show shizu adjust_happy_close_ss
with charachange

shi "…!"

mi "โอเค ทีนี้ก็จบเรื่อง~! วะฮ่าฮ่า! ฮ่าฮ่าฮ่าฮ่า!"

stop music fadeout 6.0

"ชิซูเนะจับมือขวาฉันไว้ ส่วนมิช่าจับมือซ้าย"

show shizu behind_smile_close_ss
with charachange

shi "…"

show misha hips_grin_close_ss
with charachange

mi "มานี่เลย! คืนนี้ยังมีอะไรให้ทำอีกเยอะ นายต้องมาสนุกให้สุดกว่านี้!"

show misha cross_laugh_close_ss
with charachange

mi "ฮ่าฮ่าฮ่าฮ่า~!"

$ renpy.music.set_volume(1.0,2.0, "ambient")

scene bg school_courtyard_ss
show crowd_ss
with shorttimeskip

play music music_ease fadein 6.0

"พวกเราฝ่าฝูงชนที่แน่นขนัดไปเล่นเกมนั้นเกมนี้ โยนห่วง ทุบตัวตุ่น แม้แต่เกมที่ฉันไม่เคยได้ยินมาก่อนก็มี"

"ก็แทบไม่ได้ของหรอก แต่ก็สนุกดี"

hi "นี่ ที่งานนี้มีเกมตักปลาทองนั้นมั้ย"

show shizu behind_smile_ss at tworight
show misha hips_smile_ss at twoleft
with charaenter

shi "…"

mi "มีสิ! ไม่ยักรู้ว่านายชอบเกมนั้นนะฮิจัง!"

hi "พอดีอยากลองมานานแล้วน่ะ ก็เห็นไม่ยากมาก"

show misha hips_grin_ss
with charachange

mi "แน่ใจนะฮิจัง~"

show misha cross_laugh_ss
with charachange

mi "วะฮ่าฮ่าฮ่า~! โอเค ๆ ! เดี๋ยวรู้กัน! น่าจะอยู่แถวนี้แหละนะ!"

show shizu basic_normal_ss
with charachange

shi "…"

show misha perky_smile_ss
with charachange

mi "ว่าแต่ได้ปลามาแล้วจะเอาไปเก็บที่ไหน มีโหลใส่เหรอ"

hi "ก็ ไม่มี…"

show misha hips_grin_ss
with charachange

mi "คงเอาไปกินมั้ง!"

show shizu adjust_smug_ss
with charachange

shi "…"

show misha cross_laugh_ss
with charachange

mi "ฮ่าฮ่าฮ่าฮ่าฮ่าฮ่า! อะฮ่าฮ่าฮ่าฮ่าฮ่าฮ่า!!"

show misha cross_grin_ss
with charachange

mi "ได้ ฮิจัง ถ้าพวกเราตักได้สักตัวก็จะยกให้นาย!"

hi "เอ๊ะ จริงเหรอ เล่นอีกเกมเหรอ งั้นก็ได้"

show shizu basic_happy_ss
with charachange

"ชิซูเนะดันหลังฉันให้ไปที่แผงอย่างตื่นเต้นพลางเก็บงำความกระตือรือร้นที่ฉายในแววตา"

scene bg school_stalls2_ss at bgright
with locationchange

"โชคดีที่ทั้งคู่ตักไม่ได้สักตัวเลย แต่ฉันก็ไม่ต่างกันเท่าไหร่"

show bg school_stalls2_ss at bgleft
with charamove

$ renpy.music.set_volume(0.6,2.0, "ambient")

"หลังจากนั้นฉันก็อดหัวเราะไม่ได้ พวกเธอลากฉันให้ไปที่แผงใหญ่ ๆ หลากสีแผงหนึ่งที่ฉันช่วยทำ"

"ฉันยังจำได้ว่ากว่าจะทำขึ้นมาได้ลำบากไปแค่ไหน"

"คนเฝ้าแผงหน้าตาบ้าน ๆ ที่ย้อมผมสีน้ำตาลหันมาให้ความสนใจเมื่อเห็นพวกเราเดินมา ฉันสังเกตเห็นสองอย่าง"

"อย่างแรก เกมนี้เป็นเกมที่ให้ปาบอลใส่กองขวดใสเพื่อล้มขวดให้ได้มากที่สุด"

"สี่ลูกห้าสิบเยน ก็คุ้มใช้ได้"

"อย่างที่สองคือมีวิธีการเล่นเขียนเป็นอักษรเบรลล์ไว้ด้วย ฉันนึกอยากจะพูดอะไรสักอย่างพลางหันมองว่าชิซูเนะ\nกับมิช่าจะมองเห็นด้วยหรือเปล่า"

"อาจจะไม่เห็น หรือไม่ได้รู้สึกแปลกอะไร"

thname(คนเฝ้าซุ้ม) "ไง! มาจนได้นะคุณฮากามิจิ! ขอบคุณที่มาช่วยเรื่องซุ้มนี้นะ สนุกกันดีมั้ย"

"ชิซูเนะเหลือบมองมิช่าที่แปลทุกอย่างให้ด้วยความเร็วแสง จากนั้นเธอก็ส่งยิ้มให้คนเฝ้าซุ้ม"

show shizu behind_smile_ss at Slide(0.8,0.5,0.7,0.5,1.0)
show misha perky_smile_ss at Slide(0.2,0.5,0.3,0.5,1.0)
with Dissolve(1.0)

shi "…"

show misha hips_grin_ss at twoleft
with charachange

mi "ฮ่าฮ่า~! ไม่เป็นไร ไม่เป็นไรเลย~! อื้ม เยี่ยมจริง ๆ ครั้งนี้คงเป็นงานที่จัดออกมาได้ดีที่สุดแล้วละ!"

show misha perky_smile_ss
with charachange

mi "ชิรากิ ขอเล่นหน่อยได้มั้ย"

show misha hips_grin_ss
with charachange

mi "แน่อยู่แล้ว~ ทุ่มเวลาทั้งหมดสร้างนี่ขึ้นมาทั้งที ตกรางวัลให้ตัวแทนสภานักเรียนสุดน่ารักและขยันสักหน่อยก็คงดีนะ!"

thname(ชิรากิ) "ฮ่าฮ่าฮ่า ฮะ ๆ …ไม่"

"พ่อหนุ่มชิรากินี่ใจแข็งเหมือนบอลทีเดียว"

hi "เฮ้ย ฉันทำแผงนี้ขึ้นมานะ งานหนักแทบหลังเดาะเนี่ย เปลืองเวลาชีวิตไปตั้งสองชั่วโมง ให้เล่นฟรีสักชุดก็ยังดีน่า"

show misha hips_frown_ss
with charachange

mi "ฉันด้วย!"

show shizu basic_angry_ss at tworight
with charachange

shi "…"

mi "ฉันก็ด้วย!"

show misha perky_confused_ss
with charachange

mi "อ่า…"

"เขาอึกอักอยู่พักหนึ่งจนสุดท้ายก็ยอมยื่นบอลให้คนละสี่ลูกแล้วยักไหล่"

show misha hips_grin_ss
show shizu behind_blank_ss
with charachange

"ยังไม่ทันพ้นวินาทีนับจากนั้น ชิซูเนะและมิช่าก็ยัดเยียดบอลของตัวเองมาให้"

hi "มีอะไร"

hi "อย่าบอกนะว่าลงทุนตื๊อมาขนาดนี้แล้วจะไม่เล่นน่ะ"

hi "แล้วไปรุมชิรากิอย่างนั้นอีก"

thname(ชิรากิ) "นั่นสิ…"

show shizu basic_frown_ss
with charachange

shi "…"

show misha sign_smile_ss
with charachange

mi "นายไม่ต้องสอดเลย~!"

show shizu adjust_happy_ss
with charachange

"ชิซูเนะหันมาทางฉันแล้วเริ่มขยับมืออย่างไม่ใส่ใจ มิช่าดูจะลังเลว่าจะแปลหรือปลอบคนเฝ้าซุ้มดี"

show shizu adjust_smug_ss
with charachange

shi "…!"

show misha hips_grin_ss
with charachange

mi "อะฮ่าฮ่าฮ่า! ฮิจัง ความเป็นอัศวินของนายไปไหนหมด อีกอย่าง ฉัน - ชิจังเขาถือเรื่องปาบอลน่ะ!"

show misha hips_smile_ss
with charachange

mi "เอ่อ โทษทีนะฮิจัง ฉันก็ไม่รู้เหมือนกันว่าจะปาแม่นขนาดนั้นมั้ย แต่นายคงเก่งอะไรแบบนี้ใช่มั้ย ใช่มั้ย อย่างนาย\nทำได้สบายมาก!"

stop music fadeout 3.0

"ก็ดูง่ายอยู่ ขวดก็ไม่ได้ตั้งไกล ปัญหาเดียวคือบอลพวกนี้เป็นบอลวิฟเฟิลที่ข้างในมันกลวง ๆ "

play sound sfx_impact

"ฉันปาเข้าที่กองขวดแรง ๆ และบอลก็เด้งกลับมาดื้อ ๆ "

show shizu behind_blank_ss
show misha perky_confused_ss
with charachange

hi "ไรเนี่ย"

thname(ชิรากิ) "อ้อ ใช่ ไม่ได้ง่ายอย่างที่เห็นหรอกนะ ในขวดมีน้ำอยู่ด้วย ความลับทางการค้าละ"

show misha hips_frown_ss
with charachange

mi "ขี้โกงนี่นา!"

hi "มิน่าถึงได้ให้ตั้งสี่ลูกกับห้าสิบเยน ร้ายจริง ๆ "

show shizu basic_angry_ss
with charachange

shi "…"

show misha hips_smile_ss
with charachange

mi "นี่ ฮิจัง นายล้มได้อยู่แล้ว! นายยังเหลือโอกาสอีกตั้งสิบเอ็ดครั้งนะ! เอาเลย!"

hi "เธอมาปามั้ยล่ะ"

hi "ชิซูเนะ จะลองดูมั้ย"

show shizu behind_blank_ss
with charachange

"ชิซูเนะสั่นหัวไปมาเน้นชัด"

"ฉันหัวเราะ สนุกดีเหมือนกันแฮะ"

play sound sfx_impact
play music music_soothing fadein 3.0

"ฉันง้างแขนปาบอลอีกลูกใส่กองขวดแล้วทำให้ขวดเริ่มเคลื่อนเล็กน้อย"

show shizu basic_normal_ss
show misha perky_smile_ss
with charachange

"ทั้งชิซูเนะและมิช่าต่างเฝ้ามองตุ๊กตารูปแมวด้วยสายตาโหยหา"

"เอาเข้าจริง ๆ แล้วพวกเธอก็ไม่ได้ต่างกันนัก"

"บางครั้งฉันก็นึกสงสัยว่าถ้าชิซูเนะพูดได้จะเป็นเหมือนมิช่าหรือเปล่า"

"ไม่สิ ไม่ได้เหมือนกันขนาดนั้น"

play sound sfx_impact

"ฉันปาอีกลูก ก็ค่อนข้างง่ายเหมือนกัน ถ้าปาให้สองขวดที่อยู่แถวล่างล้มได้ก็ได้กินง่าย ๆ เลย"

"คนก็เริ่มมามุงกันส่งแรงกดดันมาถึงฉัน เหลืออีกเก้าลูก"

play sound sfx_dropstuff

"ฉันง้างแขนอย่างมือขว้างในกีฬาเบสบอลแล้วปาสุดแรงเกิดจนกองขวดล้มระเนระนาด"

show shizu behind_blank_ss
show misha cross_laugh_ss
with charachange

show stuffedcat:
    alpha 0.0 yalign 0.5 xanchor 0.5 xpos 0.6 subpixel True
    easein 1.0 xpos 0.5 alpha 1.0
with Pause (1.0)

"ฉันรับตุ๊กตาแมวหวานแหววนั้นอย่างผู้มีชัย ส่วนมิช่าก็หัวเราะลั่นราวกับว่าเป็นคนปาจนล้มเอง"

"ชิซูเนะจ้องมาด้วยหน้าตายอย่างทุกที ชัดว่าเธอเองก็อยากได้ตุ๊กตา"

show stuffedcat:
    easeout 1.0 xpos 0.4 alpha 0.0
with Pause (1.0)

hide stuffedcat
with None

show shizu basic_normal2_ss
with charachange

shi "…"

show misha hips_grin_ss
with charachange

mi "ยินดีด้วยนะฮิจัง~! จะเอาตุ๊กตาไปทำอะไรเหรอ"

"ไม่มีคำตอบที่ถูก ต้องระวังตัวให้ดี"

hi "ไม่…รู้สิ"

mi "งั้นนนนนน~ ถ้านายไม่เอา ฉันขอนะ…"

show shizu adjust_smug_ss
with charachange

shi "…"

show misha cross_grin_ss
with charachange

mi "หรือนายจะอยากเก็บไว้ก็ตามใจนะฮิจัง ไม่ยักรู้ว่านายก็ชอบตุ๊กตา นายนี่นุ่มนิ่มจัง"

hi "ไม่อะ เอาไปก็ไม่ได้ใช้ทำอะไร"

show misha cross_smile_ss
with charachange

mi "งั้นก็ขอหน่อย"

show shizu behind_blank_ss
with charachange

shi "…"

"สายตาของพวกเธอจ้องจนทะลุเข้ามาในใจ"

"ไม่อยากเลือกเลย ฉันหันกลับไปที่ซุ้ม"

hi "นี่ มีตุ๊กตาแบบนี้อีกตัวมั้ย"

thname(ชิรากิ) "ก็ มีแหละ อีกตัวเดียว"

hi "โอเค งั้นจัดใหม่หน่อย พอดีอยากลองเอาอีกตัวด้วย"

"ยังปาได้อีกแปดครั้ง"

play sound sfx_pillow

"พอกองขวดถูกจัดขึ้นมาใหม่ ฉันก็ปาจนสุดแรงเกิดอีกครั้ง ทว่าพลาด"

show misha hips_grin_ss
with charachange

mi "ฮ่าฮ่าฮ่า! จะเอาอีกตัวเหรอ คิดจะหาทางหนีง่าย ๆ อย่างนี้เหรอฮิจัง"

hi "ถ้าง่ายนักก็มาปาเองมั้ย"

mi "ไม่เป็นไร ขอบใจ~!"

show misha perky_smile_ss
with charachange

mi "เนี่ย ฮิจัง ตอนปาบอลก็วางตุ๊กตาก่อนก็ได้"

hi "ไม่"

show shizu adjust_smug_ss
with charachange

shi "…"

mi "เหลืออีกตัวเดียวนะ นายต้องคว้ามาให้ได้! ถ้าไม่สำเร็จละก็ฉันเอานายตายแน่~!"

show shizu behind_smile_ss
with charachange

shi "…"

mi "แต่แหม เป็นแผนแบ่งตุ๊กตาให้ฉันที่ฉลาดดีนะ! แล้วฉันที่ว่าก็คือฉันนี่แหละ~!"

show shizu adjust_happy_ss
with charachange

shi "!"

show misha cross_laugh_ss
with charachange

mi "อะฮ่าฮ่าฮ่าฮ่า~! ล้อเล่นน่า!"

"มิช่าก็ไม่ได้มีเจตนาร้ายอะไร ชิซูเนะก็ดูจะยิ้มขำกับที่เธอพูดเล่นอยู่ แต่ก็ดูซึมไปนิด ๆ "

"ฉันให้เธอถือตุ๊กตาไว้ อย่างน้อยก็ตอนที่กำลังเล็งเอาอีกตัวน่ะนะ พออุ้มตุ๊กตาแมวตัวใหญ่ไปด้วยแล้วเล็งลำบาก"

show shizu behind_smile_ss
show misha perky_smile_ss
with charachange

shi "…"

mi "ขอบคุณนะฮิจัง ชิจังดูมีความสุขเลยละฮิจัง~! แต่นายจะเอาอีกตัวมาให้ฉันด้วยใช่มั้ย"

hi "ก็กำลังปาอยู่นี่ไง"

stop music fadeout 5.0

show shizu behind_smile_ss at Slide(0.7,0.5,0.8,0.5,1.0, time_warp=_ease_out_time_warp)
show misha perky_smile_ss at Slide(0.3,0.5,0.2,0.5,1.0, time_warp=_ease_out_time_warp)
with None

hide shizu
hide misha
with Dissolve(1.0)

play sound sfx_pillow

"ฉันปาอีกครั้ง แต่รอบนี้เล็งพลาด"

"แขนก็เมื่อยแล้วด้วย เหมือนเลือดไม่ค่อยเดิน"

"ฉันนึกด่าตัวเองอยู่ในใจว่าน่าสมเพช แค่นี้ก็เหนื่อยแล้ว"

"จนนึกได้ว่าอาจจะเพราะหัวใจฉัน ซึ่งถ้าเป็นอย่างนั้นจริงก็ไม่รู้จะคิดยังไงต่อเหมือนกัน"

play sound sfx_impact

"แค่คิดว่าอะไรแค่นี้ก็ทำให้ฉันรู้ซึ้งถึงความเป็นความตายของฉันได้ก็เครียดแล้ว"

"วันที่ฉันจะลืมเรื่องนี้ไปได้คงไม่มี"

"แม้แต่วันนี้—วันที่ฉันคิดว่าจะได้ออกมาสนุกในสถานที่อันสวยสดในคืนอันงดงามนี้—ฉันก็ยังหนีไปจากเหตุผล\nที่ทำให้ฉันมาอยู่ที่นี่ไม่พ้น"

"ฉันไม่เคยรู้สึกสบายใจขนาดนี้มาก่อน ณ ที่นี่ที่ไม่เหมือนที่ใดที่ฉันเคยอยู่"

play sound sfx_pillow
play music music_sadness fadein 2.0

"ฉันหนีความคิดที่เลี่ยงไม่พ้นนั้นไม่ได้"

"ว่าฉันอาจถูกส่งมาที่นี่เพื่อตาย"

"สองสามวันมานี้เป็นช่วงที่ดีที่สุดในชีวิตฉัน เป็นครั้งแรกหลังผ่านมาเนิ่นนานที่รู้สึกว่าได้มีชีวิตอยู่จริง ๆ "

"แต่ท้ายที่สุดแล้ว ฉันก็ยังเป็นฉันที่จะถูกระลึกเสมอว่าฉันอาจตาย ณ วินาทีไหนก็ได้ทุกครั้งที่ต้องเดินขึ้นบันไดหลายขั้น\nหรือปาบอลแรงเกินไป"

play sound sfx_pillow

"ฉันจะถูกขีดเส้นจำกัดโดยสิ่งนี้เสมอ"

"คิดแล้วก็ทั้งเครียดและโมโห เพราะสุดท้าย ฉันยังรักชีวิตตัวเอง ฉันยังสนุกอยู่ และชีวิตฉันก็กลายเป็นสิ่งที่ไม่เที่ยง\nไปยิ่งกว่าครั้งไหน"

"ฉันคิดว่าสุดท้ายแล้วฉันจะต้องจบลงกับอะไร อาจจะเป็นอะไรก็ได้ถ้าฉันทั้งอ่อนแอและน่าสมเพชอย่างนี้ อาจจะ\nสะดุดล้มแรง ๆ โดนต่อยหน้าอก หรือลูกเบสบอลที่หลุดมา"

"ฉันหมดอารมณ์จะเล่นเกมนี้แล้ว แต่ก็ยังเล่นต่อ"

stop music
$ renpy.music.set_volume(0.0,0.0, "ambient")
play sound sfx_heartfast

show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.7)

"อยู่ ๆ ความปวดก็แล่นจี๊ดเข้ามาที่หน้าอก มาได้แวบหนึ่งแล้วก็หายไป แต่ก็เล่นเอาฉันเซไปเล็กน้อย"

$ renpy.music.set_volume(0.4,10.0, "ambient")

show shizu adjust_blush_close_ss at Slide(0.8,0.5,0.7,0.5,0.5)
show misha perky_confused_close_ss at Slide(0.2,0.5,0.3,0.5,0.5)
with Dissolve(0.5)

"ชิซูเนะสะดุ้งโหยงแล้วเข้ามาหา สายตามองมาด้วยความเป็นห่วง มิช่าเอามือจับไหล่ฉันไว้"

play music music_pearly

mi "นี่ ฮิจัง เป็นอะไรหรือเปล่า"

hi "อืม ไม่เป็นไรหรอก ตอนนี้รู้สึกไม่ค่อยสบายเท่าไหร่ น่าจะป่วย คงต่อไม่ไหวแล้วละ"

show misha hips_frown_close_ss at twoleft
with charachange

"มิช่าขมวดคิ้ว"

mi "อย่าฝืนตัวเองเลย ถ้าไม่สบายขนาดนั้นเดี๋ยวฝืนอีกก็หนักกว่าเดิมหรอก"

show shizu basic_normal2_close_ss at tworight
with charachange

shi "…"

show misha hips_smile_close_ss
with charachange

mi "เนี่ย งานเทศกาลเพิ่งเริ่มเองนะ แถมเล่นเกมกันมาสักพักแล้วด้วย ถ้าเหนื่อยก็พักก่อนสักหน่อยก็ได้"

show misha sign_smile_close_ss
with charachange

mi "ดีเลยชิจัง ฉันเองก็เหนื่อย ๆ แล้วเหมือนกัน! ฉันว่าพวกเราน่าจะเดินทั่วโรงเรียนจนล้ากันบ้างแล้วนะฮิจัง!"

"ฉันพยักหน้า พวกเธอดูจะยังไม่ได้จับสังเกตอะไรที่แปลกไปได้ ซึ่งก็ดีแล้ว"

scene bg school_courtyard_ni
show crowd_ni
with shorttimeskip

$ renpy.music.set_volume(1.0,2.0, "ambient")

"พวกเราเดินแหวกทะเลผู้คน มิช่าก็ชี้คนนั้นคนนี้ที่เธอรู้จักทุกคนอย่างร่าเริง ชิซูเนะกอดตุ๊กตาแมวตัวนั้นไว้\nในอ้อมแขนไปเรื่อยเปื่อย ดูท่าจะสนุกกัน"

"จู่ ๆ ฉันก็รู้สึกผิดขึ้นมา"

"ว่าพวกเราต้องหยุดเพราะสุขภาพอันย่ำแย่ของฉัน"

show shizu behind_smile_ni at tworight
show misha perky_smile_ni at twoleft
with charaenter

shi "…"

mi "ฮิจัง พวกเราชักหิวแล้วสิ นายหิวมั้ย"

hi "ไม่ได้หิวขนาดนั้น แต่ก็อยากหาอะไรกินอยู่"

show misha hips_smile_ni
with charachange

mi "แค่หิวก็โอเคแล้วน่าฮิจัง~! แล้วจะกินอะไรกันดี"

hi "ฉันอะไรก็ได้หมด"

show shizu adjust_happy_ni
with charachange

shi "…"

show misha hips_grin_ni
with charachange

mi "อ๊ะ! งั้นแซนด์วิชเป็นไง แล้วก็หาอะไรดื่มด้วย! เดี๋ยวมิช่าไปซื้อให้เอง!"

show misha perky_confused_ni
with charachange

mi "อะไรนะ"

show shizu behind_smile_ni
with charachange

"ชิซูเนะหันมามองทางฉันแล้วยิ้ม คงจะหยอกเล่นหวังให้ฉันร่าเริงขึ้น ฉันก็หัวเราะไป"

show shizu adjust_happy_ni
with charachange

shi "…"

show misha perky_smile_ni
with charachange

mi "ฮิจัง คนเริ่มเยอะแล้ว กินที่นี่คงไม่ได้แล้วละ เสียงก็เริ่มดังแล้วด้วย"

show misha sign_smile_ni
with charachange

mi "ไปกินที่ดาดฟ้าดีกว่านะ"

hi "ก็ได้ วิวคงสวยดี น่าจะมีลมพัดด้วย"

show misha hips_grin_ni
with charachange

mi "งั้นก็ตกลง! เดี๋ยวฉันคงต้องไปซื้อของกินก่อน…ไว้เดี๋ยวเจอพวกเธอสองคนอีกทีนะ~!"

hide misha
with charaexit

stop music fadeout 6.0

"มิช่าโบกมือลวก ๆ แล้ววิ่งไป"

"ก่อนหน้านี้ไม่ทันได้สังเกตโคมกระดาษที่แต่งแต้มยามค่ำคืนมืดมิด แต่พอได้เห็นแล้วก็รู้สึกทึ่งจริง ๆ "

"หิ่งห้อยบินอยู่เหนือหัว แสงนวลของมันทำให้ดูราวกับว่าหิมะกำลังตกบนผืนท้องฟ้าราตรี"

"หากเป็นในเมืองใหญ่แล้วละก็คงไม่ได้เห็นอะไรอย่างนี้"

show shizu adjust_happy_ni at Slide(0.7,0.5,0.5,0.5,0.5,time_warp=_ease_time_warp)
with None

show shizu cross_angry_close_ni at Slide(0.7,0.5,0.5,0.5,0.5,time_warp=_ease_time_warp)
with Dissolve(0.5)

"ชิซูเนะดึงแขนเสื้ออย่างร้อนใจแล้วกอดอก ขมวดคิ้วราวแสดงความไม่พอใจของเธอที่ฉันหันไปสนใจอย่างอื่น"

show shizu basic_angry_close_ni at center
with charachange

shi "…"

hi "เธอก็รู้ว่าฉันอ่านภาษามือไม่ออก"

show shizu behind_frown_close_ni
with charachange

shi "…"

"จะว่าไปแล้ว นี่ฉันต้องโง่ขนาดไหนถึงพูดอยู่กับคนหูหนวกเนี่ย เธอคงไม่ได้ยินหรอก"

show shizu behind_blank_close_ni
with charachange

"ฉันยักไหล่หวังให้เธอรับรู้ว่าฉันไม่เข้าใจ ชิซูเนะส่ายหน้าแล้วโบกมือปัด ๆ เป็นเชิงว่าช่างมัน"

"ไว้ต้องขอให้มิช่าสอนภาษามือให้แล้ว"

$ renpy.music.set_volume(0.3, 1.0, "ambient")

scene bg school_roof_ni
with locationskip

"พอขึ้นมาที่ดาดฟ้าฉันก็ต้องทึ่งกับขนาดของโรงเรียนนี้อีกครั้ง แทบไม่อยากเชื่อว่าฉันจะไม่ทันสังเกตว่าพื้นที่\nในตัวโรงเรียนนั้นกว้างมาก"

"ฉันอดไม่ได้ที่จะแหงนหน้ามองดาวที่ส่องประกายอยู่บนฟากฟ้าเมื่อฉันเดินตามชิซูเนะอยู่บนดาดฟ้า"

show shizu behind_smile_close_ni at center
with charaenter

"ชิซูเนะและฉันนั่งลงที่ม้านั่ง เธอยิ้มอย่างอ่อนโยนดูอารมณ์ดี ลมพัดสางผมเธอ"

"พวกเรามองลงไปที่งานเทศกาลเบื้องล่างที่ดูเหมือนทะเลโคมกระดาษส่องระยิบระยับและพัดที่โบกไปมาที่เต็มไปด้วยผู้คน\nบางคนก็แต่งชุดยูกาตะมาอย่างดี"

"ที่จริงผู้หญิงส่วนใหญ่ก็แต่งชุดยูกาตะกัน ฉันนึกสงสัยว่าทำไมชิซูเนะและมิช่าถึงไม่ใส่มาบ้าง"

"ชุดยูกาตะคงจะเข้ากับเธอสองคนดี ฉันจินตนาการว่าพวกเธอจะใส่แบบไหนกัน"

"ชิซูเนะคงเลือกอะไรที่เป็นแบบตามตำรับ แต่พอนึกถึงมิช่าแล้วก็นึกภาพไม่ค่อยออก"

"มิช่าวิ่งหอบมาถึงคอยประคองไม่ให้ของกินที่ขนมาหกกระจาย"

"พอวางทุกอย่างลงกับพื้นแล้วเธอก็นอนแผ่หลากับพื้น"

show shizu behind_smile_close_ni at tworight
show bg school_roof_ni at bgright
with charamove

show misha hips_grin_ni behind shizu at twoleft
with charaenter

mi "อะฮ่าฮ่าฮ่าฮ่าฮ่าฮ่าฮ่าฮ่าฮ่า~! นานมาก! มา ๆ เห็นเธอสองคนไม่ได้สั่งอะไรกันฉันเลยเอาน้ำข้าวกับแซนด์วิชมา\nแล้วก็ขนมด้วย! ของกินนั่นนี่อีก!"

hi "ดี ๆ งั้นกินกันเลย"

"มิช่ากัดแซนด์วิชสามเหลี่ยมคำเล็ก ๆ "

show misha hips_smile_ni
with charachange

mi "นี่ ฮิจัง งานเทศกาลเป็นไงบ้าง สนุกดีใช่มั้ย"

hi "อื้ม"

show shizu adjust_happy_close_ni
with charachange

shi "…"

mi "คืนนี้ดาวสวยนะ เป็นวันที่ดีมาก ๆ เลย"

play music music_serene fadein 5.0
$ renpy.music.set_volume(0.1, 2.0, "ambient")

scene black
show bg misc_sky_ni at Fullpan(30.0)
with locationchange

"เสียงผู้คนชุกชุมที่อยู่กันข้างล่างฟังดูรื่นหู เคล้าไปกับเสียงจิ้งหรีดที่แว่วมาไกล ๆ "

"ฉันดื่มน้ำข้าวแบบกระป๋องแล้วมองไปทางมิช่าที่นอนยืดหลังหลับสบายโดยมีกระป๋องน้ำแอปเปิลที่เหลืออยู่ครึ่งหนึ่ง\nตั้งอยู่บนหน้าท้องเธอ"

"ชิซูเนะแนบขาเข้าชิดกันแล้วโยกตัวเบา ๆ เหมือนเด็กที่อยู่ไม่สุขแล้วมองขึ้นไปยังท้องฟ้า"

"เธอสองคนก็น่ารักดี พอมองไปรอบ ๆ ก็เห็นนักเรียนหลายคนจับมือถือแขนกันกับแฟนสาวบ้าง แฟนหนุ่มบ้าง"

"บนดาดฟ้านี้ไม่ไกลจากพวกเรานักมีคู่รักอยู่สองสามคู่ดูดาวไม่ก็ดูงานเทศกาลข้างล่างกันพลางจับมือกัน"

"ใจหนึ่งฉันอยากมีอย่างนั้นบ้าง"

"ฉันมองชิซูเนะและมิช่าพลางคิดว่าสักวันจะขอใครสักคนคบได้ไหมนะ คุ้มที่จะเสี่ยงหรือเปล่า"

"ฉันสะดุดตาเข้ากับเข็มนาฬิกาสีทองที่เดินอยู่บนหน้าปัดนาฬิกาเรือนงามของชิซูเนะ นี่ก็เริ่มดึกแล้ว แต่งานเทศกาล\nยังคงดำเนินต่อไปไม่ซาลงเลย"

"ชิซูเนะจับแขนตุ๊กตาแมวนั้นไว้ เธอเห็นว่าฉันมองอยู่"

shi "…?"

"เธอยื่นมาให้แบบส่ง ๆ ฉันยิ้มนึกอยากถามว่าอยากให้ฉันทำอะไร แต่เธอคงไม่เข้าใจ"

"ฉันสั่นหัวแล้วพยายามทำท่าเป็นเชิงว่าให้เธอเก็บไว้เถอะ หวังว่าจะเข้าใจนะ"

"พอมองไปทางโรงเรียนก็เห็นคนมากมายที่ทั้งมีความสุขและสนุกกันอยู่"

"พอได้ดูแล้วก็อิ่มใจ"

"รู้สึกพิเศษดีจริง ๆ คุ้มแล้วที่ออกมาวันนี้"

"แต่ความรู้สึกผิดกับความหมองเมื่อกี้ยังไม่หายไป ยังคงวนเวียนอยู่ในใจ ปล่อยไปก็ไม่ได้"

"ชิซูเนะทำภาษามือบางอย่างให้ฉัน ฉันอ่านไม่ออก และไม่ว่าฉันจะพูดอะไรเธอก็จะไม่ได้ยิน"

hi "บอกว่าอะไรน่ะชิซูเนะ"

hi "เอาเหอะ จะว่าผิดกันทั้งคู่ดีมั้ยเนี่ย แต่ก็นะ ขอโทษแล้วกันที่ฉันอ่านไม่ออก"

hi "เนี่ย ฉันค่อนข้างดีใจนะที่เธอลากฉันให้มาที่นี่เนี่ย แต่ถ้าฉันนึกอยากคบเธอเมื่อไหร่ก็คงต้องคิดถึงนิสัยนี้ของเธอ\nให้มากกว่านี้"

hi "ไม่สิ จริง ๆ แล้ว…ฉันดีใจนะ วันนี้สนุกมากเลย"

hi "ถ้าเธอยิ้มให้มากกว่านี้ก็คงดี เธอยิ้มสวยนะ"

stop music fadeout 5.0

show shizu behind_frustrated_close_ni at center
show bg misc_sky_ni at right
with charaenter

"เธอยืนขึ้นด้วยความหงุดหงิดแล้วเอามือไพล่หลัง ท่าทางดูองอาจและมีอำนาจนั้นยืนอยู่ต่อหน้าผืนฟ้าดวงดาว"

stop ambient fadeout 2.0

show shizu out_serious_close_ni
with charachange

"อยู่ ๆ เธอก็อ้าแขนออกกว้างราวกับจะคว้าท้องฟ้าผืนนั้นไว้กับตัว"

"ราวกับจะบอกให้ฉันมองทุกอย่างที่อยู่เบื้องหน้าของฉัน"

show shizu epictransition
show cityscape zoom behind shizu
show hill enter behind shizu

"โรงเรียนที่เต็มไปด้วยแสงสีของงานเทศกาลและชุดยูกาตะ ดาดฟ้าหิ่งห้อยประดับแสง ท้องฟ้ากว้างไกลที่ทำให้รู้สึกทึ่ง"

"เธอจะสื่ออะไร แล้วฉันก็ค่อย ๆ นึกได้ขึ้นมา ว่าภาพอันงดงามต่อหน้านี้คือเครื่องพิสูจน์ว่าการที่มัวแต่เอาอารมณ์\nหม่นหมองมาบดบังนั้นเป็นเรื่องร้ายเกินให้อภัย"

"และลักษณะนิสัยของชิซูเนะก็ยิ่งเป็นตัวตอกย้ำประเด็นนั้น"

hi "ต้องขอบใจ สินะ"

hide shizu
show hill pairtouch at center
with charachange

"ฉันเสมองทางอื่น แต่ชิซูเนะก็เข้ามาคว้าไหล่ฉันไว้ นาฬิกาของเธอแตะแก้มฉัน"

"มือซ้ายของเธอชี้ไปบนท้องฟ้า"

play ambient sfx_fireworks fadein 1.0

show fireworks behind hill
with None
show fw_screen behind fireworks
with Dissolve(5.0)

"เสียงปุ้งปั้งมาพร้อมกับพลุที่ถูกยิงขึ้นฟ้า แต่ละลูกต่างแผ่ประกายสีสดใสที่ไม่นานก็เลือนหายไปกับความมืดมิด"

"ฉันจำไม่ได้แล้วว่าครั้งล่าสุดที่ได้ดูพลุคือเมื่อไหร่ ยิ่งพลุดอกใหญ่อย่างนี้อีก แถมยิงมาจากโรงเรียนด้วย เป็นอะไรที่\nสุดจะเหลือเชื่อมาก ๆ "

"แสงที่ค่อย ๆ เลือนหายในท้องฟ้าถูกเติมแต่งอีกครั้งด้วยดอกที่สองจากเมืองข้างล่าง ราวกับจับจังหวะกันมาเพื่อเสริมกัน\nคล้ายเพลงคู่"

"ผ่านไปสักประมาณสิบห้านาทีได้พลุก็หมด"

"ชิซูเนะเธอเห็นว่ามือยังจับไหล่ฉันไว้อยู่จึงค่อย ๆ เอาออกอย่างระมัดระวัง ท่าทางดูอึดอัดเล็กน้อย"

stop ambient fadeout 5.0
hide fireworks
hide fw_screen
show hill pairnotouch
with Dissolve(5.0)

"พอเธอตั้งสติได้ก็ยิ้มยืนเท้าสะเอวพลางยืดอก"

"ตัวเธอเช่นนี้แหละที่ทำให้เธอดูเหมือนสาววัยรุ่นทั่ว ๆ ไป ร่าเริง มีความสุข ปล่อยตัวตามสบาย"

"ฉันครุ่นคิดไปพลางกินของกินกับชิซูเนะ สองเรามองผู้คนที่เริ่มบางตาลงอย่างเงียบ ๆ "

"เธอเอนตัวไปข้างหน้าเล็กน้อยทำท่ามือเท้าคาง สีหน้าดูพึงใจ ระคนเศษเสี้ยวความหวนคำนึง"

"โดยในมือยังถืออุ้งมือตุ๊กตาแมวเอาไว้"

"ฉันเริ่มรู้สึกเพลีย ๆ ขึ้นมาจึงบอกไปว่าจะมาเจอเธอกับมิช่าวันพรุ่งนี้โดยยังไม่ทันนึกได้ว่าเธอไม่ได้ยินด้วยซ้ำแล้วเดิน\nกลับหอ"

"ในใจรู้สึกอบอุ่นและมีชีวิตขึ้นมาแม้อากาศยามค่ำคืนจะเย็นเยียบ"

stop music fadeout 4.0

"ภาพของชิซูเนะที่ยืนอยู่ต่อหน้าผืนดวงดาวอย่างองอาจที่ลบเลือนความสมเพชในใจฉันนั้นไม่จางไปจากใจได้ง่ายดาย"

"ถ้า…ถ้าหากว่าความรักเกิดได้ในเพียงเสี้ยววินาที ฉันคงตกหลุมรักเธอเข้าให้แล้ว"

"เพียงเล็กน้อย"

window hide

        
#******************

#Emi Path
label th_A39:

show bg school_dormhallway at bgright
with None

"รู้สึกไม่ค่อยดีเท่าไหร่ ตอนนี้ฉันก็นึกสงสัยขึ้นมาแล้วด้วย"

"จะไปดีหรือเปล่า"

"ฉันมีหนังสือที่กะไว้ว่าจะอ่านอยู่"

"เป็นเรื่องระบบไปรษณีย์ใต้ดินที่อาจมีหรือไม่มีจริงก็ได้"

"สั้นดีด้วย อ่านจบในวันเดียวน่าจะไหว"

"แต่ใช้เวลาแบบนั้นจะคุ้มเหรอ"

"ก็ อืม คุ้มแหละ"

"แต่ออกไปข้างนอกคงดีกว่า"

"ไปดูงานเทศกาล"

"ไปดูว่างานแสดงแผงอื่น ๆ มีอะไรกันบ้าง"

"เอาจริง ๆ อย่างน้อยฉันควรจะรักษาภาพลักษณ์ที่ดูเป็นมิตรที่ทำมาตลอดสัปดาห์นี้ด้วย"

"ท้องฉันบอกว่าไปหาอะไรกินก็น่าจะได้"

"จะถึงเวลามื้อเที่ยงแล้ว…ไปหาซื้ออะไรมากินจากแผงข้างนอกดีกว่า"

play music music_soothing fadein 1.0
play ambient sfx_crowd_outdoors fadein 1.0

scene bg school_courtyard
show crowd
with locationskip

"ฉันย้ายตัวมาข้างนอกทันที นักเรียนและผู้คนที่อาจจะใช่หรือไม่ใช่ผู้ปกครองต่างรายล้อมไปหมด"

"บางครั้งก็เห็นบางคนที่ดูออกเลยว่ามาจากเมืองเพื่อมางานเทศกาลนี้"

"ดูออกง่ายมาก"

"จะเป็นคนที่เอาแต่จ้อง ดูออกว่าเบื้องหลังสายตาพวกนั้นคือความคิดว่า “แล้วคน ‘นี้’ เป็นอะไรนะ”"

"อยากตะคอกใส่แทบตาย"

"แต่ตลอดสัปดาห์ที่ผ่านมาฉันเองก็ทำอย่างเดียวกันไม่ใช่หรือไง"

"ความรู้สึกคล้ายความรังเกียจเข้าครอบงำ เป็นความรู้สึกผิดที่ฉันใจแคบ"

"…"

$ renpy.music.set_volume(0.6,2.0, "ambient")

scene bg school_stalls1
with locationchange

"ฉันปัดความคิดนั้นทิ้งแล้วหันมาสนใจกับความหิวที่แผดเผาราวไฟสุมกระเพาะ"

"กลิ่นน้ำมันหอม ๆ พาฉันไปยังดินแดนแห่งพันธสัญญา ที่ที่ฉันจะได้กินมื้อเที่ยง"

stop music fadeout 0.6

"จังหวะที่ฉันกำลังสั่งนั้นเองก็มีเสียงดังมาขัด"

show emi basic_annoyed at Slide(0.7,0.5,0.5,0.5,0.5)
with charaenter

emi "นี่ ทำอะไรของนายเนี่ย"

play music music_comedy fadein 0.5

hi "กินข้าวเช้— เอ่อ เที่ยง"

show emi sad_annoyed at center
with charachange

emi "ข้าวเช้า?"

show emi sad_angry
with charachange

emi "นายเพิ่งตื่นเหรอ"

hi "เอ้อ…"

"อยู่ ๆ ก็รู้สึกว่าการนอนจนหมดช่วงเช้าเป็นความผิดบาป"

hi "ไม่ ข้าวเที่ยง…จริง ๆ นะ"

"เธอไม่เชื่อ"

hi "มื้อควบงี้"

show emi basic_annoyed_close
with characlose

emi "เป็นมื้อเช้าที่ไม่ดีต่อสุขภาพเลยนะ!"

"เธอฉวยของกินไปจากมือฉันแล้วจ้องจี่"

"นี่ยัยนี่ทำอะไรเนี่ย"

hi "เฮ้ย นั่นข้าวเช้าฉันนะ!"

show emi sad_annoyed_close
with charachange

emi "ไหนบอกข้าวเที่ยง"

hi "นั่นข้าว…เออเอาเหอะ นั่นของกินของฉัน!"

"เอมิยืนเท้าสะเอวแล้วเทศน์ฉัน"

show emi basic_annoyed_close
with charachange

emi "นี่ลืมแผนการกินไปแล้วเหรอ"

emi "นายต้องคิดถึงสุขภาพของตัวเองให้มากกว่านี้นะฮิซาโอะ!"

show emi sad_angry_close
with charachange

emi "แล้วหัวใจนายอีก"

hi "หัวใจฉันก็ไม่เห็นจะเป็นอะไรเลย! ส่วนมากอะนะ"

"เธอเพียงกลอกตาตอบ"

show emi basic_annoyed_close
with charachange

emi "อ้อเหรอ"

show emi basic_closedgrin_close
with charachange

emi "ถ้างั้นนายคงไม่ต้องมาอยู่ที่นี่หรอก จริงมั้ย"

"แน่นอนว่าเธอพูดถูก"

"แต่ฉันไม่ยอมถอยหรอก"

hi "ก็ไม่ได้ไม่ดีต่อหัวใจขนาดนั้นสักหน่อย!"

hi "กินมันนิด ๆ หน่อย ๆ บ้างก็คงไม่เป็นไรหรอก!"

"อืม ใช่แล้ว แถมวิ่งนิด ๆ หน่อย ๆ ก็ได้ด้วย"

show emi basic_annoyed_close
with charachange

"เอมิยังดูไม่เชื่อ"

"ก็ไม่แปลก ขนาดฉันยังไม่เชื่อตัวเองเลย"    

emi "ก็คงงั้น แต่ถ้านอนตื่นสายขนาดนี้ตลอดก็คงไม่ไหวหรอก!"

"แล้วเธอก็แสยะยิ้มชั่วร้ายขึ้นมา"

show emi basic_grin_close
with charachange

emi "แต่แน่นอน ถ้านายทำตามตารางกิจวัตรแต่แรกนายก็คงไม่มาอยู่ในสภาพนี้หรอก…"

stop music fadeout 6.0

hi "เฮ้ย สัปดาห์นี้ฉันก็เจอเรื่องหนักมาเยอะนะ!"

hi "อย่างเนี่ย ฉันเกือบตายเลยนะ! แล้วต้องเจอคนนั้นคนนี้อีก แล้วก็ไปอยู่บนดาดฟ้า…"

show emi sad_annoyed_close
with charachange

emi "ซึ่งก็ไม่ใช่ข้ออ้างที่จะมาทำตัวสบายแฮอย่างนี้หรอกนะ"

emi "แค่เกือบตายใช่ว่าจะมาทำอ้างไม่ออกกำลังกายแบบง่าย ๆ หรอก"

show emi basic_closedgrin_close
with charachange

emi "อย่างการวิ่งรอบเช้า"

"เธอพยักหน้าราวตัดสินใจอะไรสำคัญได้แล้ว"

show emi basic_happy_close
with charachange

play music music_emi fadein 0.5

emi "งั้นก็เป็นอันตกลง!"

show emi excited_proud_close
with charachange

emi "นายยอมรับข้อผิดพลาดของตัวเอง แล้วจะยอมทำตามตารางกิจวัตรของฉันใช่มั้ย"

emi "ฉันจะได้เห็นหน้านายแต่เช้าตรู่ใช่มั้ย"

show emi excited_happy_close
with charachange

emi "เราจะได้เป็นคู่วิ่งด้วยกันใช่มั้ย"

hi "คือเมื่อวานเธอก็ขอให้ฉันเชื่อได้แล้วไม่ใช่เหรอว่าทำอย่างนี้ก็ดีเหมือนกัน"

hi "ไม่ต้องมาขออีกรอบหรอกน่า"   
    
"แต่ก็ใช่ว่าฉันจะเชื่อฟังได้ดีขนาดนั้นอะนะ"
 
"เพราะยังไงเธอก็พูดถูกเรื่องการกินให้มันดีต่อสุขภาพมากขึ้น ฉันกลับมาซื้อของกินที่ไม่ดีต่อสุขภาพอย่างน่ารังเกียจ\nอย่างนี้"

"แต่ก็อร่อยนะ!"
    
"แต่ก็มีอย่างอื่นที่สำคัญกว่าความอร่อยอยู่แหละมั้ง"

"อย่างการมีชีวิตอยู่งี้"
    
"ถ้าเอมิไม่มาตามจู้จี้ที่ฉันทำแต่อะไรแย่ ๆ อย่างนี้ละก็ ฉันคง…"

"เอ๊ะ เดี๋ยวนะ"
    
"อยู่ ๆ คำถามหนึ่งก็โผล่ขึ้นมาในหัว"

hi "นี่ แล้วไหงอยู่ ๆ เธอถึงมาใส่ใจเรื่องสุขภาพของฉันขนาดนี้หา"

show emi basic_closedgrin_close
with charachange

"เธอยักไหล่แล้วแสยะยิ้มให้"

show emi basic_grin_close
with charachange

emi "ก็นายมาใหม่"

emi "คงยังไม่มีเพื่อนเลยใช่มั้ยล่ะ"

show emi sad_grin_close
with charachange

emi "อีกอย่าง ฉันเอาแต่สร้างเรื่องให้นายตลอดสัปดาห์ที่ผ่านมาอีก"

emi "นายอุตส่าห์ไม่โกรธฉัน ฉันก็ต้องตอบแทน"

show emi basic_happy_close
with charachange

emi "แล้วฉันก็รับปากกับคุณพยาบาลว่าจะดูแลให้ด้วยนั่นแหละ"

"อ่า…ฮะ สาวน้อยนักวิ่งที่อยากให้ฉันมีสุขภาพดี"

"แต่ก็คงมีอะไรที่แย่กว่านี้อีกเยอะ"

hi "โอเค ก็ฟังดู…ใช้ได้"

hi "ขอบคุณที่เป็นห่วงนะ"

hi "งั้นพรุ่งนี้เช้าเนอะ"

stop music fadeout 1.0

hide emi
with charaexit

"เมื่อเห็นว่าบทสนทนาจบลงฉันจึงหันหลังเตรียมเดินออกไป"

emi "จะรีบไปไหน!" 

play music music_running

with vpunch

"ฉันถูกดึงคอเสื้อจนทั้งตัวถูกกระชากกลับภายในอึดใจ"

hi "นี่ ไม่เห็นต้องรุนแรงกันเลย!"

hi "คราวนี้อะไรอีกล่ะ"

show emi sad_shy_close at center
with charaenter

"เอมิดูคล้ายจะเจ็บปวดที่ถูกฉันถามอย่างรำคาญอย่างนั้น"

emi "ให้ฉันอยู่เป็นเพื่อนนายก็ได้นี่นา"

show emi basic_annoyed_close
with charachange

"เธอหรี่ตา"

emi "อีกอย่าง นายจะแอบไปหาของมัน ๆ นั่นกินอีกแล้วใช่มั้ย"

"จริง ๆ ก็ไม่ แต่พอพูดแล้วก็ฟังดูเป็นความคิดที่ดี"

hi "เปล่าสักหน่อย!"

show emi sad_annoyed_close
with charachange

"จ้องอีก"

hi "โอเค ก็จะไปหากินบ้างแหละ…"
    
"ยังจ้องต่อ"
    
hi "โอเค ไปหากินเยอะ ๆ "
    
"โห นี่ฉันเป็นภัยทั้งต่อตัวเองและคนอื่นเลยสินะ"

"ทั้งที่รับปากแล้วว่าจะทำตัวให้สุขภาพดีขึ้น แล้วก็คิดจะทำอะไรที่ไม่ดีต่อสุขภาพทันทีที่คิดได้"

show emi basic_closedgrin_close
with charachange

emi "กะแล้ว! นายนี่เชื่อไม่ได้เลยจริง ๆ "

show emi basic_grin_close
with charachange

emi "โอเค ฉันต้องตามติดนายละ"

"สถานการณ์ตอนนี้รู้สึกจะฮา ๆ ดี"

"นึกสภาพไม่ออกเลยว่าคนที่ผ่านไปผ่านมาจะมองยังไงที่ฉันโดนสาวที่ตัวเล็กเกือบครึ่งตัวฉันบ่นเนี่ย"

"ยอม ๆ ไปก่อนก็ได้"

hi "ได้ จะทำอะไรก็เชิญ"

"ฉันถอนหายใจ"

"ไหน ๆ ก็ไหน ๆ แล้วน่ะนะ"

hi "เธออยากทำอะไรล่ะ"

show emi basic_confused_close
with charachange

"เอมิคิดอยู่พักหนึ่ง"

emi "อืม ฉันสัญญากับรินไว้แล้วว่าจะไปดูภาพเขียนผนังของเธอ…"

show emi basic_grin_close
with charachange

emi "ไปกัน!"

"ขอยอมรับว่าฉันเองก็อยากรู้เหมือนกันว่าภาพเขียนนั้นจะเป็นยังไง เป็นอีกครั้งที่ฉันคิดว่าคงมีอะไรที่แย่กว่านี้อีกเยอะ"

$ renpy.music.set_volume(1.0,2.0, "ambient")
                                               
scene bg school_courtyard
show crowd
with locationchange

"ฉันพยักหน้าเออออไปแล้วร่างก็ถูกลากฝ่าฝูงชนไปขณะที่เอมิเธอมุ่งหน้าไปยังเป้าหมาย"

stop music fadeout 6.0
stop ambient fadeout 2.0

scene bg school_dormext_full at bgright
with locationchange

"พอมาถึงที่หอใจฉันก็เต้นแรง"

"มาแค่นี้ไม่น่าเต้นแรงมากสิ"

"ฉันสูดหายใจลึก ๆ คอยให้ฉันสงบลง"

"ฉันเป็นคนหนึ่งในโรงเรียนนี้ที่ดูปกติที่สุด แต่ฉันก็ยังต้องมาเรียนที่นี่"

"บางครั้งฉันก็แทบจะคิดอยากให้ฉันแขนขาดไปเลยหรืออะไรสักอย่าง"

"เพราะอย่างน้อยก็จะได้ให้เห็นชัดว่าฉันควรมาอยู่ที่นี่"

"แต่ฉันกลับไม่ได้ดูผิดปกติอะไรเลย"

"ขนาดตอนนี้ที่ฉันกำลังหอบยังดูเหมือนแค่คนที่ไม่ได้ออกกำลังกายเท่านั้น"

"เอมิหันกลับมาแล้วเห็นว่าฉันกำลังเครียดอยู่"

show emi basic_hes at Slide(0.4,0.5,0.5,0.5,0.5)
with charaenter

emi "นายจะไม่ตายใส่ฉันใช่มั้ย"

show emi basic_shock at center
with charachange

emi "อย่านะ ขอร้อง!"

show emi sad_depressed
with charachange

emi "ไม่งั้นเดี๋ยวเป็นความผิดฉันอีก แล้วฉันก็ไม่อยากรู้สึกผิดกับอะไรอย่างนั้นด้วย"

emi "อีกอย่าง ฉันไม่เอาอะไรแบบคราวที่แล้วแล้วนะ เดี๋ยวคุณพยาบาลต้องพูดแน่ว่าเป็นความผิดฉันน่ะ"

play music music_soothing fadein 8.0

hi "มะ…ไม่ ไม่เป็นไรหรอก"

hi "ฉันคงต้องเริ่มวิ่งจริง ๆ แล้วแหละ"

show emi basic_closedgrin
with charachange

emi "เนี่ย แล้วนายก็อยากกิน…อะไรของนายที่มัน ๆ นั่นน่ะ"

show emi excited_proud
with charachange

emi "เห็นมั้ย ดีนะที่ฉันมาเห็นนายก่อน"

"ใช่ ดี"

hi "มั้ง"

show emi basic_grin
with charachange

"แน่นอนว่าฉันไม่ได้เสริมว่าถ้าเธอไม่ได้ลากฉันผ่านงานเทศกาลมาแบบนั้นฉันคงไม่มาอยู่ในสภาพนี้"

"บทสนทนาต่อใด ๆ ถูกขัดเมื่อรินโผล่มา"

show rin basic_absent at Slide(1.0,0.5,1.0,1.0,1.0)
with Dissolve(1.0)

rin "อ้าว พวกเธอน่ะเอง"

show rin basic_absent at tworight
show emi basic_grin at twoleft
show bg school_dormext_full at center
with charamove

show rin basic_awayabsent
with charachange

rin "สวัสดี เอมิ"

show emi basic_closedhappy
with charachange

emi "ไงริน! เห็นฮิซาโอะเขาหัวใจจะวายเลยพามาด้วยน่ะ!"

show rin basic_absent
with charachange

hi "ใช่ที่ไหนเล่า!"

"คำปฏิเสธของฉันถูกเมิน"

show emi basic_grin
with charachange

emi "เรามาแวะดูว่าภาพเขียนผนังเป็นไงน่ะ!"

"รินพยักหน้าช้า ๆ "

show rin basic_awayabsent
with charachange

rin "ก็อยู่ตรงนั้นน่ะ"

show rin basic_deadpan
with charachange

rin "เห็นชัดอยู่นะ"

"ฉันนึกสงสัยว่ารินยืนอยู่หน้าภาพเขียนนั้นนานแค่ไหนแล้ว"

"มีใครมาแวะดูบ้างไหมนะ"

"พวกเรามาคนแรกเหรอ"

"แต่ไม่ใช่คนที่เห็นเป็นคนแรกแน่ ๆ ละ"

"ก็ใหญ่ขนาดนี้น่ะ"

"เดินผ่านยังไงก็ต้องหันมอง"

"แต่ก็คงไม่ได้มีใครมาคุยกับรินเรื่องภาพเขียนนี้"

"นอกจากพวกเราน่ะนะ"

"รู้สึกเหมือนต้องพูดอะไร"

hi "สวยดีนะ"

show rin negative_spaciness
with charachange

rin "ฉันยังไม่ค่อยพอใจกับงานนี้เท่าไหร่"

rin "แต่แบบนี้ก็คงใช้ได้แล้ว"

"เธอทำท่าคลับคล้ายยอมแพ้"

"ไม่รู้เหมือนกันว่าเธออยากให้ออกมาอย่างไหน แต่คงไม่ได้ตามที่วาดหวังไว้เท่าไหร่"

scene bg mural at Fullpan(100.0, dir="left")
with Dissolve(2.0)

"พวกเรายืนอยู่ต่อหน้าภาพเขียนผนังนั้นแล้วมองให้เต็มตา"

"ฉันเพ่งสมาธิจดจ่ออยู่กับองค์ประกอบของภาพ"

"ค่อนข้างน่าสนใจเหมือนกัน"

"สีสันปราดเปรียวกลมกลืนลากให้ฉันเวียนตาม"

"เป็นภาพที่ดูให้ชวนฝันจนฉันรู้สึกแทบง่วงนอน"

"ฉันลองหาสีที่ฉันกับเอมิคอยขนมาให้"

"แต่หาเท่าไหร่ก็หาสีปรัสเซียนบลูไม่เจอเลย"

"เอาเถอะ"

"คงอยู่ในนั้นสักที่แหละ"

scene bg school_dormext_full
show rin basic_awayabsent at tworight
show emi basic_closedgrin at twoleft
with Dissolve(2.0)

"ฉันเริ่มเจ็บเท้าแล้ว แต่รินก็ยังไม่มีทีท่าว่าจะขยับ"

"เอมิพูดขึ้นมา"

show emi basic_confused
with charachange

emi "นี่ ริน กินอะไรแล้วหรือยัง"

show rin basic_deadpan
with charachange

rin "กินสิ ไม่กินก็ตายกันพอดี"

show emi basic_hes
with charachange

emi "แล้วในรอบห้าชั่วโมงที่ผ่านมานี้ล่ะ"

show rin relaxed_nonchalant
with charachange

rin "กินแล้วมั้ง แต่หิวอีกแล้ว น่าจะจำผิด"

show emi basic_closedgrin
with charachange

"เอมิยิ้มแล้วตบมือ"

show emi basic_grin
with charachange

emi "เยี่ยม! งั้นไปหาอะไรกินด้วยกัน!"

"รินพยักหน้าเออออ"

show rin basic_deadpannormal
with charachange

rin "โอเค แต่รีบ ๆ หน่อยแล้วกัน เดี๋ยวพวกเขาเห็นว่าฉันไม่อยู่"

"ไม่รู้ทำไม แต่พวกเขาไม่น่าจะสนใจหรอก"

"พวกไหนก็ช่าง"

stop music fadeout 3.0
$ renpy.music.set_volume(0.6,0.0, "ambient")
play ambient sfx_crowd_outdoors fadein 1.0

scene bg school_stalls1 at Fullpan(8.0)
with locationskip

"ระหว่างที่กลับไปยังแผงขายอาหาร ฉันก็มองเหล่าของทอดตาละห้อย"

"ไม่ อย่าเลย"

"ยังไงเอมิก็คงไม่ให้กินอยู่แล้ว"

stop ambient fadeout 1.0

scene bg school_gardens
show emi basic_closedgrin at twoleft
show rin basic_awayabsent at tworight
with locationchange

play music music_ease fadein 9.0

"พวกเรามาหามุมเหมาะ ๆ บนสนามหญ้าแล้วลงนั่งกินของที่ซื้อมา"

"ของที่ฉันซื้อมาอะนะ อยู่ ๆ ก็ได้จ่ายค่าของกินหมดนี่เองซะงั้น"

"แต่ของกิน (ไม่ทอด) ที่ฉันซื้อมาอร่อยเกินคาด"

"ความเงียบเข้าปกคลุมเมื่อเอมิกับฉันกินกันอยู่ ส่วนรินมอง…อะไรสักอย่าง แล้วหันมากินของกินตัวเองคำสองคำ"

"ฉันกินหมดก่อนแล้วเอนหลังนอนลงกับพื้น"

"เอมิหยุดกินแล้วมองฉัน"

show emi basic_confused
with charachange

emi "เหนื่อยเหรอฮิซาโอะ"

hi "ก็นิดหน่อยละมั้ง"

show emi basic_annoyed
with charachange

emi "งั้นพรุ่งนี้เช้าก็อย่าตื่นสายแล้วกัน"

show emi excited_proud
with charachange

emi "เราจะมาเริ่มวิ่งรอบเช้ากันแล้วนะ จำได้ใช่มั้ย"

"จริง ๆ ก็ลืมไปแล้ว"

"ฉันก็สนุกไปเรื่อยเปื่อย"

"เดินดูงานเทศกาลกับสองคนนี้ก็สนุกดีเหมือนกัน"

hi "อืม เดี๋ยวตั้งปลุก"

show emi basic_annoyed
with charachange

emi "นายต้องมานะ!"

show emi basic_closedgrin
with charachange

emi "ถ้าไม่มาฉันโกรธแน่!"

hi "หวังว่า"

show rin basic_lucid
with charachange

rin "แล้วจะหวังกับใครล่ะ"

show rin basic_deadpan
with charachange

rin "ถ้าจะหวังกับพระเจ้า พรุ่งนี้อาจมีเรื่องแปลก ๆ อะไรที่ทำให้นาฬิกาปลุกนายเสียก็ได้"

show rin basic_deadpannormal
with charachange

rin "แบบว่าอยู่ ๆ พระเจ้าที่นายหวังก็ทำให้เป็นอย่างนั้น"

show emi basic_grin
with charachange

emi "งั้นก็อย่าให้พระเจ้าทำอย่างนั้นแล้วกัน"

"ในหัวฉันเริ่มคิดแผนขึ้นมา"

"เป็นแผนที่ค่อนข้างทำให้ฉันรู้สึกผิด แต่ก็จะทำอยู่ดี"
 
"แม่ง ฉันต้องกินของทอดสักหน่อย"

"แล้วยังไงวิ่งที่ว่าก็เริ่มพรุ่งนี้นี่นา"

"เพราะฉะนั้นตารางกิจวัตรจริง ๆ ก็เริ่มพรุ่งนี้ ไม่ใช่ตอนนี้"

"เหตุฉะนั้นแล้ว เรื่องอาหารการกินจึงเริ่มพรุ่งนี้ด้วย และด้วยประการฉะนี้เอง วันนี้ฉันจึงกินอะไรที่เสียสุขภาพได้อยู่"

"ประมาณว่ากินสั่งลาของทั้งหลายที่ฉันสวาปามกินดะไปเมื่อก่อนเข้าโรงพยาบาล"

hi "เอ้อ ฉันกลับห้องก่อนดีกว่า"

hi "พอดีมีการบ้านต้องทำน่ะ จะได้นอนไว ๆ แล้วเดี๋ยวพรุ่งนี้ต้องตื่นเช้ามาวิ่งด้วย"

show emi basic_annoyed
with charachange

"หรี่ตามองอีกแล้ว"

show emi sad_annoyed
with charachange

emi "นายคงไม่ได้จะแอบไปหาซื้อของทอดตรงนั้นกินอีกใช่มั้ย"

hi "ไม่อะ อิ่มแล้ว"

"ฉันทำท่าลูบท้องไปด้วย"

hi "แล้วอีกอย่าง เธอสองคนผลาญเงินฉันเกลี้ยงเลย"

show emi basic_closedhappy
with charachange

"เอมิหัวเราะคิกคักเป็นเสียงรื่นหูน่าฟัง"

"รู้สึกผิดขึ้นมาอีกแล้ว"
    
"เธอคงรู้ใช่มั้ยว่าฉันโกหกอยู่น่ะ"
    
"หรือเชื่อใจกันจริง ๆ "
    
"รู้สึกเหมือนเป็นปีศาจเลยแฮะ"

show emi excited_proud
with charachange

emi "เพราะคิดมาแล้วยังไงละฮิซาโอะ"

show emi basic_closedgrin
with charachange

emi "โอเค เจอกันเช้าพรุ่งนี้นะ"

show emi basic_grin
with charachange

emi "ขอบคุณที่เลี้ยงนะ! ขอบคุณที่อยู่เป็นเพื่อนด้วย!"

"ไหนบอกว่าคิดมาเพื่อฉันไง"

show rin relaxed_surprised
with charachange

"รินพยักหน้าตาม"

rin "ฉันจะไม่พูดว่า “เจอกันพรุ่งนี้” เพราะถ้าพูดแล้วจะเหมือนการทำนายอนาคต แล้วฉันก็ค่อนข้างแน่ใจด้วยว่าฉัน\nทำนายอนาคตไม่ได้"

hi "…"

hi "โอเค"

hi "ลาก่อนนะทั้งสองคน"

"รู้สึกดีใจแปลก ๆ ที่เลือกที่จะออกมาจากห้องในวันนี้"

"ก็คงเป็นการเริ่มต้นสัปดาห์ที่สองที่ไม่แย่เท่าไหร่นัก"

stop music fadeout 9.0
play ambient sfx_crowd_outdoors fadein 1.0

scene bg school_stalls1
with locationchange

"พอแน่ใจว่าพ้นสายตาเอมิมาแล้วฉันก็ไปต่อแถวที่แผงหนึ่งเพื่อซื้อเค้ก"

"อย่างน้อยก็ไม่ใช่ของทอดนี่ ใช่มั้ย"
    
"ดีกว่าที่คิดจะซื้อทีแรกนิดหน่อย"
    
"แต่ก็ยังรู้สึกแย่หน่อย ๆ ที่โกหกเอมิไปอย่างนั้น"
 
"เธอดูจะเป็นห่วงสุขภาพฉันจริง ๆ "

"ต้องตอบแทนเธอสักทาง"
    
"กลับห้องดีกว่า"

"เออ ฉันยัง{i}มี{\i}เรื่องที่ต้องทำนี่นา"

stop ambient fadeout 1.0

scene bg school_dormhisao
with locationskip

"หนังสือรอฉันอยู่ ฉันกระโจนเข้าหาเตียงแล้วอ่านหนังสือเคล้าภาพพลุที่ถูกจุด"

$ renpy.music.set_volume(0.1,0.0, "ambient")
play ambient sfx_cicadas fadein 2.0

scene bg school_dormhisao_ni
with Dissolve(2.0)

"จนสุดท้ายจากการที่เดินเล่น (หรือจะพูดให้ถูกก็คือ วิ่งเล่น) ก็ทำให้ฉันล้าเต็มทน"

"ฉันนี่ไม่ไหวเลยจริง ๆ "

"การที่เอมิลากฉันให้มาวิ่งแต่เช้าก็คงเป็นเรื่องที่ดีจริง ๆ นั่นแหละ"

"เป็นเรื่องที่ชวนให้ตั้งตาคอย"

stop ambient fadeout 2.0

window hide



#######################
#Rin Path

label th_A40:

play ambient sfx_crowd_outdoors fadein 0.3
play music music_soothing fadein 0.5

scene bg school_dormext_full
show crowd
with locationskip

"พอเดินออกมาจากประตูหลักก็พบกับเสียงจ้อกแจ้กจอแจของผู้คน"

"เมื่อวานและเช้าวันนี้มีการแปลงพื้นที่ในโรงเรียนให้กลายเป็นพื้นที่ของงานเทศกาล"

"แผงหลากสีสันตั้งเรียงรายไปตามทางเดินหลักที่ทอดจากประตูทางเข้าไปยังอาคารหลัก"

"ยังมีคนที่ขนของเดินกันขวักไขว่ แต่ด้านหลังแผงส่วนใหญ่ก็มีเหล่านักเรียนที่รอเตรียมพร้อมอย่างสบาย ๆ แล้ว"

"ส่วนใหญ่ก็ตื่นเช้ากันมาเตรียมของให้แล้วเสร็จ"

"ความรู้สึกผิดแล่นผ่านเข้ามา แต่ไม่นานก็หายไป"

"ฉันเป็นแค่นักเรียนที่เพิ่งมาใหม่อันต้อยต่ำนี่นะ"

"คนที่มาเที่ยวก็เริ่มเดินตามงานกันแล้ว"

"บางกลุ่มก็เป็นครอบครัวหนุ่มสาวที่พะวงอยู่กับลูกหลานตัวเองที่มีพลังเหลือล้น…"

"…นักเรียนของที่นี่บางคนก็มีพ่อแม่มาด้วย…" 

"…แล้วก็เด็กกับคนแก่ที่มางานนี้ด้วยเหตุผลที่ฉันไม่อาจคาดเดาได้"

play sound sfx_warningbell

"เสียงระฆังดังขึ้น ตามด้วยเสียงแหลม ๆ ของผู้อำนวยการที่กล่าวเปิดงานที่มากับเสียงตามสาย"

"ทุกคนปรบมือไปตามมารยาท ออกจะเนือย ๆ "

"งานเทศกาลโรงเรียน…ที่โรงเรียนเก่าของฉันไม่ได้จัดงานเทศกาลอะไรกัน ยิ่งมองจากมุมของโรงเรียนที่ฉันย้ายมาแล้ว\nจะรู้สึกว่างานอย่างนี้ค่อนข้างตกยุค แต่ก็ยังน่าตื่นเต้นอยู่ดีแหละนะ"

"ได้หยุดวันหนึ่งหลังผ่านสัปดาห์อันหนักหน่วงมาแล้วก็รู้สึกสบายเหลือเกิน ถึงสี่เดือนที่ผ่านมาจะเอาแต่นอนแบ็บอยู่\nที่โรงพยาบาลก็เถอะ"

"จำได้เลยว่าตอนกักตัวอยู่ที่โรงพยาบาลยังอยากมาเรียนคาบคณิตเลยด้วยซ้ำ"

"ฉันจำไม่ได้ว่าในงานเทศกาลจะมีจัดอะไรบ้าง ถึงวันก่อนมุโต้จะบอกไปแล้วในคาบก็เถอะ"

"ฉันเดินลงบันไดของหอมา ตั้งใจว่าจะไปเดินดูแผงในงานทั้งหลายแหล่ที่จัดกัน แต่ฉันก็มาถึงแค่ที่ตีนบันไดเท่านั้น"

stop ambient fadeout 1.0

hide crowd
show rin relaxed_boredom at tworight
with Dissolve(2.0)

"มีคนอยู่สองสามคนกำลังดูภาพเขียนผนังของรินอยู่ ส่วนเจ้าตัวก็พิงกำแพงอยู่ข้าง ๆ ท่าทางเบื่อสุดขีด และเหมือนจะ\nไม่สบายหน่อย ๆ ด้วย"

hi "อรุณสวัสดิ์"

show rin relaxed_surprised
with charachange

rin "สวัสดี"

hi "งานถึงไหนแล้วเหรอ"

show rin relaxed_nonchalant
with charachange

rin "ไม่ถึงไหน"

rin "ฉันติดอยู่"

hi "ติดอยู่นี่คือ?"

rin "หมายถึงว่าขามันติดเดินไม่ได้น่ะ น่าจะเพราะเมื่อวานขาฉันเลยพังไป"

hi "เจ็บมั้ย"

show rin relaxed_sleepy
with charachange

rin "บอกยากแฮะ มั้ง"

"อาการปวดขาจากการวาดของเธอคงหนักกว่าที่เธอแสดงออก ทีแรกก็นึกว่าแค่กล้ามเนื้อล้าหรืออะไรอย่างนั้น ฉัน\nหมายจะถามต่อ แต่รินก็เปลี่ยนเรื่องไปอย่างหน้าตาเฉย"

show rin basic_awayabsent
with charachange

rin "เพื่อนของครูเขามาแวะดู"

show rin basic_absent
with charachange

rin "แล้วก็ชวนฉันไปกินข้าวเที่ยงในเมืองด้วยกัน ดีนะที่ฉันเจ็บขาอยู่"

hi "แต่เธอก็ได้แต่ติดแหง็กนั่งอยู่ตรงนี้อะนะ ไม่เห็นจะดียังไงเลย"

show rin basic_lucid
with charachange

rin "ก็รอจนกว่าฉันจะเดินได้นั่นแหละ ไม่ช้าก็นาน ถ้าคิดถึงมันอยู่สักพัก"

rin "ครูเขาดีใจที่ฉันวาดเสร็จจนได้"

hi "ก็ควรจะแหละนะ"

show rin basic_awayabsent
with charachange

stop music fadeout 5.0

rin "แต่ฉันยังไม่รู้เลยว่านี่คือเสร็จแล้วหรือยัง"

hi "หืม"

show rin basic_deadpanupset
with charachange

rin "เมื่อวานฉันคิดว่าทำอะไรเสร็จหมดแล้ว แต่ตอนนี้ดันไม่แน่ใจอีก น่าจะเติมรายละเอียดอีกหน่อย มั้งนะ อาจจะ เลือก\nไม่ถูกเหมือนกัน"

"จะเสร็จหรือไม่เสร็จก็ตาม ภาพเขียนผนังที่ต้องแสงแดดนั้นสวยมาก"

play music music_another fadein 2.0

scene bg mural at Transform(xalign=0.05)
with Dissolve(2.0)

"อวัยวะมนุษย์หลายส่วนที่สลับซับซ้อนบิดเบี้ยวกันอยู่หลายชิ้นเป็นองค์ประกอบหลัก"

"ออกจะหยาบ ๆ คล้ายว่าแค่ลงสีไปแบบพื้น ๆ แต่ทุกฝีแปรงนั้นผ่านกระบวนการคิดและความเอาใจใส่มาเป็นอย่างดี"

show bg mural at Transform(xalign=0.25)
with charamove

hi "ที่ออกมาจากหัวอันนี้คือกบเหรอ"

rin "ปลาทองต่างหาก"

show bg mural at Transform(xalign=0.45)
with charamove

hi "นั่นอะไรน่ะ"

rin "ไม่ใช่อะไร"

show bg mural at Slide(0.45,0.45,.6,0.6,25.0, time_warp=acdc_warp)
with None

"แต่เอาเถอะ…"

"กำแพงนั้นกว้างมากจนฉันต้องหันหน้าไปมาเพื่อดูภาพทั้งหมด"

"ภาพนี้นั้นมองให้เป็นภาพเดียวกันยาก เพราะแต่ละองค์ประกอบดูจะไม่เข้ากัน แต่ก็คงมีความเป็นเอกลักษณ์อยู่"

"และเพราะภาพนั้นดูค่อนข้างนามธรรม ฉันจึงไม่รู้ว่าภาพนี้จะสื่ออะไร แต่สำหรับฉันแค่สวยก็พอแล้วละ"

"ฉันลงนั่งข้าง ๆ รินแล้วพิงกำแพงอย่างเธอ"

"เสียงคึกคักจากงานเทศกาลนั้นดังขึ้นเรื่อย ๆ เมื่อผู้คนเริ่มหลั่งไหลมา"

"หอนั้นค่อนข้างไกลจากจุดจัดงานใหญ่ที่อยู่ที่อาคารหลักกับแผงตามสวน คนส่วนใหญ่จึงยังไม่มาที่นี่"

show rin negative_spaciness_close at offscreenright
with None

show rin negative_spaciness_close at tworight
show bg mural at Transform(xalign=0.6)
with MoveTransition(3.0, factory=MoveFactory(time_warp=_ease_time_warp))

"รินทำสีหน้าเบื่อหน่ายจนดูเหมือนถูกตัดขาดจากโลกรอบ ๆ ตัวเธอ"

"เงียบสนิทเลยแฮะ เจ็บอยู่หรือเปล่า"

hi "แล้วคนที่มาดูภาพเขียนเธอว่าไงบ้าง"

show rin basic_deadpannormal_close at tworight
with Dissolve(1.5)

"คำถามของฉันเรียกให้เธอหลุดจากภวังค์ เธอหันหน้ามาทางฉันอย่างเอื่อย ๆ "

show rin basic_deadpan_close
with charachange

rin "ไม่แน่ใจเหมือนกัน"

show rin basic_awayabsent_close
with charachange

rin "คงชอบละมั้ง น่าจะนะ"

hi "แล้วเธอล่ะ พอใจกับงานของตัวเองหรือเปล่า คือฉันเองก็เป็นผู้ช่วยด้วย ถ้าเธอไม่มีความสุขคงแย่เลย"

"เธอเอียงคอแล้วกัดริมฝีปากตัวเอง"

show rin negative_sad_close
with charachange

rin "ก็ใช้ได้นะ ไม่ได้แย่ แต่ก็ไม่ได้ดี มันก็…เป็นงั้นแหละ ฉันอยู่แบบไม่คิดอะไรแบบนี้ก็คงไม่เป็นไร"

hi "ขอถามอย่างอื่นด้วยได้มั้ย ภาพนี้จะสื่ออะไรเหรอ คือเมื่อวานตอนที่เธอบอกว่าไม่ได้สื่ออะไรฉันก็เก็บไปคิด"

hi "แต่มันก็ย้อนแย้งกันใช่มั้ยล่ะ เวลาจะสร้างอะไรสักอย่างขึ้นมามันต้องมีตัวตั้ง แม้แต่ศิลปะก็ด้วย"

show rin negative_annoyed_close
with charachange

"เธอขมวดคิ้วแล้วหันกลับไปมองหมู่เมฆ"

rin "ไม่รู้สิ ฉันอธิบายไม่เก่ง มันก็แค่ภาพเขียนผนัง ไม่ได้มีอะไรพิเศษ ฉันก็บอกไปแล้ว"

"เธอดูรำคาญที่ฉันถาม"

rin "ฉันไม่รู้จะวาดอะไรดี ก็เลยจะวาดแค่ภาพเขียนผนัง"

rin "เป็นภาพเขียนผนังที่แทนภาพเขียนผนัง"

show rin basic_deadpancontemplation_close
with charachange

rin  "ไม่สิ เดี๋ยวนะ นึกคำที่ดีกว่าออกแล้ว ก็คือ ภาพนี้แทนตัวมันเอง"

show rin basic_deadpannormal_close
with charachange

rin "เพราะงั้น…ภาพนี้ถึงได้มีความเป็นภาพเขียนผนังแบบเต็มขั้น เท่าที่ฉันทำได้น่ะนะ ถ้านายคิดว่ามันมีความหมายอะไร\nฉันว่าก็คงมีเหมือนที่ภาพนี้มีแหละ"

"ไม่เห็นเข้าใจเลย"

"ความหมายเหรอ…ฉันมุมปากฉันยกยิ้มเจื่อน ๆ เล็กน้อย"

stop music fadeout 5.0

scene mural all
with flash

"ฉันไม่เคยเข้าถึงคำว่าศิลปะอย่างแท้จริง"

"พื้นฐานที่ว่าศิลปะนั้นคือสื่อในการแลกเปลี่ยนความคิดและแนวคิดนั้นพอเข้าใจ"

scene bg mural at Slide(1.0,1.0,0.6,0.6,40.0, time_warp=acdc_warp)
with flash

"แต่ฉันไม่เคยหัดตีความงานศิลปะแล้วทายดูว่าศิลปินต้องการจะสื่ออะไรเลย"

"รู้อยู่ว่าการคิดอย่างนั้นไม่ใช่ทักษะที่พิเศษอะไร แต่สมองฉันไม่อาจเชื่อมโยงสิ่งที่เห็นไปยังสิ่งอื่นนอกเหนือจากสิ่งที่อยู่\nตรงหน้าได้ ฉันก็เห็นเพียงแค่ว่าเป็นภาพเขียนผนังหนึ่งเท่านั้น"

"แต่ฉันก็ชื่นชมความสวยงามของมันได้ เพราะยังไงแม้แต่ฉันยังแยกออกว่าแบบไหนคือวาดห่วย วาดใช้ได้ หรือวาดสวย"

"แต่ก็ได้แค่นั้นแหละ เพราะงั้นอย่าถามฉันเรื่องความหมายเลยนะริน"

"คำตอบของเธอทำให้ฉันนึกลังเลใจที่จะถามอะไรอีก"

hi "แล้วถ้ายืนไหวแล้วเธอจะทำอะไรต่อ"

play music music_happiness fadein 4.0

scene bg mural at Transform(xalign=0.6)
show rin negative_spaciness_close at tworight
with flash

rin "ไม่ทำอะไร"

hi "ไม่ทำอะไร? แต่วันนี้มีงานเทศกาลนะ ไม่อยากไปสนุกหน่อยเหรอ"

show rin basic_absent_close
with charachange

rin "อยู่แบบนี้ก็สบายดี"

hi "เธอคงไม่ค่อยชอบเข้าสังคมสินะ"

"ฉันรู้สึกเหมือนจะแก้ต่างให้เธอมากกว่าตัวของฉันเอง แต่ก็ใช่ว่าฉันตื่นเต้นกับงานเทศกาลอะไรขนาดนั้นหรอก แค่\nอยากรู้ว่างานมันเป็นยังไงก็แค่นั้น"

"คำตอบของเธอก็ไม่ได้แปลกไปจากที่คิด"

show rin basic_awayabsent_close
with charachange

rin "ไม่ ไม่อะ"
   
hi "ฉันเองก็คง…ไม่"

show rin basic_deadpan_close
with charachange

rin "ถ้านายอยากไปก็ไปสิ"

hi "รู้น่า แต่อยู่เป็นเพื่อนเธอก็ได้ ฉันยังไม่ค่อยชินกับที่นี่เท่าไหร่ ค่อยเป็นค่อยไปก็ไม่เป็นไรหรอก"

hi "แต่ถ้าเธออยากอยู่คนเดียวฉันก็จะไป"

show rin basic_deadpannormal_close
with charachange

rin "ฉันอยากให้นายอยู่นี่"

"พวกเราพูดกันวกไปวนมา แต่สุดท้ายก็หาทางลงได้ พอได้ยินเธอพูดอย่างนั้นแล้วก็รู้สึกดีแปลก ๆ ฉันจึงอยู่ต่อ"

"ฉันเองก็อยากให้เธออยู่ด้วย บรรยากาศอันอบอุ่นพิลึกที่มาจากตัวเธอทำให้อยู่เงียบ ๆ ได้อย่างสบายใจ ฉันชอบมาก"

"พวกเราสองคนเดินดูผู้คนที่เดินผ่านไปมากันอย่างเงียบ ๆ คนอื่นก็พูดคุยกันสนุกสนาน"

"มีนักเรียนที่พาครอบครัวมาดูที่หอพักของตัวเอง พวกเขาเดินผ่านภาพเขียนผนังแล้วเหลือบตามองสักครั้งสองครั้ง\nเห็นจะได้"

"ฉันละความสนใจจากพวกเขาหันมาทางคนที่อยู่ข้าง ๆ แล้วพยายามมองผ่านสีหน้าอันลึกลับยากเกินเข้าใจของเธอ\nเข้าไปข้างใน"

show rin basic_awayabsent_close
with charachange

show rin basic_absent_close
with charachange

show rin basic_awayabsent_close
with charachange

"ตาของเธอเคลื่อนไหวจากคนนั้นไปคนนี้ที่เดินผ่าน"

"รอใครสักคนให้มาแวะที่ภาพเขียนหรือเปล่านะ หรือแอบหวังว่าจะมีคนมาติชมอะไร"

"คงไม่มีใครคิดว่าเธอเป็นคนวาดหรอก พวกเราทั้งคู่มานั่งอยู่ด้วยกันอย่างกับคนไร้บ้าน แล้วเธอไม่ก็มีมืออีกต่างหาก"

"รินจะเป็นพวกที่อยากได้คำชมด้วยเหรอ เป็นคนที่ทื่อ ๆ ขนาดนี้"

"คนที่เดินผ่านเริ่มเยอะขึ้น บางคนก็ชี้มาทางที่ภาพเขียนแล้วคุยอะไรสักอย่างกันที่ฉันฟังไม่รู้เรื่อง มีคนทำไอศกรีม\nตกใส่รองเท้าด้วย น่าสงสาร"

hi "ทุกคนดูจะชอบนะ"

"ฉันเปรย ๆ ขึ้นมากลางอากาศหน้าร้อนอันอบอ้าวที่แบ่งกั้นพวกเราอยู่"

"เธอไม่ตอบในทันที แต่ตอนนี้ฉันก็ค่อนข้างชินแล้วที่บางครั้งเธอจะพูดอะไรช้าไปบ้าง เหมือนเธอคอยเลือกสรรคำ\nอย่างถี่ถ้วนอยู่ ซึ่งออกจะเหลือเชื่อถ้าดูจากอะไรแต่ละอย่างที่ออกมาจากปากของเธอ"

show rin basic_lucid_close
with charachange

rin "ฉันวาดแล้วอยากให้ออกมาเป็นภาพที่ดูได้โดยไม่ต้องคิดอะไร แต่ฉันก็นึกได้ว่าแบบนั้นคงแปลกพิลึก ก็เลยผสมนั่นนี่\nออกมาเป็นอย่างนี้แหละ"

show rin negative_spaciness_close
with charachange

rin "พอมองจากไกล ๆ แล้วเหมือนมีคนมาขย้อนกลุ่มผีเสื้อไว้บนกำแพงเลย ซึ่งตรงกับสิ่งที่คุณประธานน่ารำคาญนั่น\nไม่ต้องการพอดี ใช่คำนั้นมั้ย"

hi "คำไหน"

show rin basic_deadpannormal_close
with charachange

rin "คำนั้น ผีเสื้อมากกว่าหนึ่งตัวเขาเรียกอะไร"

hi "ผีเสื้อหลายตัว?"

show rin basic_deadpanupset_close
with charachange

rin "ไม่ อย่างคำว่ากลุ่ม ฝูง โขลง"

hi "อ้อ ไม่รู้สิ ฝูงมั้ง"

rin "คนคงชอบอ้วกผีเสื้อกันมั้ง"

show rin negative_confused_close
with charachange

"รินมองภาพเขียนนั้นดูไม่พอใจผิดคาด"

rin "ตรงกลางทำให้สวยกว่านี้ได้อยู่นะเนี่ย"

show rin negative_annoyed_close
with charachange

rin "ปกติฉันชอบส่วนตรงกลางนะ แต่รอบนี้ทำแล้วมันรู้สึกตึง ๆ น่ะ ไม่ได้หมายถึงกล้ามเนื้อตึงจริง ๆ นะ…แต่กล้ามเนื้อ\nมันก็ตึงด้วย น่าจะตึงจริง ๆ นั่นแหละ"

hi "อย่าว่าตัวเองอย่างนั้นสิ"

show rin basic_deadpannormal_close
with charachange

"เธอมองมาทางฉันทำสีหน้าชวนขัน แต่ก็ไม่พูดอะไร"

scene bg school_dormext_full at bgright
with locationchange

"จนตอนนี้ฉันก็เริ่มคิดแล้วว่าหรือจะออกไปทำอะไรให้มันเป็นชิ้นเป็นอันกับวันอาทิตย์นี้ดี"

"แบบนี้มันคนไม่เอาถ่านของแท้เลย วันว่างทั้งวัน งานเทศกาลก็อยู่ใกล้แค่เอื้อม แล้วดูสิ่งที่ฉันทำ"

"มานั่งกับรินอยู่ตรงนี้ เป็นคนดูสองคนที่ไม่มีอะไรทำนอกจากการคิดว่าได้เป็นแค่คนดูมันน่าอดสูแค่ไหน"

"แต่ถึงจะรู้ตัวว่าสมเพชขนาดนั้นฉันก็ไม่ทำอะไรอยู่ดี ฉันไม่ได้ลุกออกไปสนุกกับงานวันนี้"

stop music fadeout 5.0

play sound sfx_rustling

centered "*ฟึ่บฟั่บฟึ่บฟั่บ*"

"…"

centered "*ยุกยิก*"

play sound sfx_rustling

centered "*ฟึ่บฟั่บ*"

"…"

scene bg mural at Transform(xalign=0.6)
show rin negative_annoyed_close at tworight
with locationchange

"รินยุกยิกไปมาอย่างร้อนรน เอาแต่แกว่งขาข้างหนึ่งพาดหัวเข่าอีกข้างสลับไปมา"

"เธอทำสีหน้าดูหงุดหงิดเอามาก ๆ "

hi "มีอะไรหรือเปล่า"

show rin basic_deadpanupset_close
with charachange

rin "ใช่ ไม่ ใช่"

scene bg school_dormext_full at bgright
show rin basic_deadpanupset:
    xpos 0.7 ypos 1.0 xanchor 0.5 yanchor 0.8
    easein 0.5 yanchor 1.0
with locationchange

"จู่ ๆ เธอก็เด้งตัวลุกขึ้นยืน ฉันตกใจเพราะนึกว่าเธอยังปวดขาเดินไม่ได้อยู่ แต่ดูเหมือนจะหายแล้ว"

show rin negative_confused at tworight
with charachange

rin "ฉันต้องไปหาเอมิหรือใครสักคนให้มาช่วย"

hi "ให้ฉันช่วยได้นะ"

show rin relaxed_nonchalant
with charachange

rin "ไม่ ไม่เป็นไร ต้องมีสักคนอยู่เฝ้าตรงนี้ไว้เผื่อมีอะไรเกิดขึ้น"

hi "อย่ามาพูดอะไรบ้า ๆ น่า ตั้งแต่ฉันมานี่ยังไม่ได้มีอะไรที่น่าสนใจเกิดขึ้นนอกจากคนที่ทำไอติมตกใส่เท้าตัวเองนั่นเลยนะ\nให้ฉันช่วยเถอะน่า ฉันก็เบื่อ ๆ เหมือนกัน"

hi "แล้วนี่มีอะไรเหรอ"

show rin negative_annoyed
with charachange

"รินเม้มริมฝีปากแน่นจนแทบจะกลายเป็นเส้นตรง"

show rin basic_lucid
with charachange

"เธอหลับตาแล้วสูดหายใจเข้าลึก ๆ "

"เมื่อเธอลืมตาขึ้นมา นัยน์ตาสีเข้มอันเรียบนิ่งน่ากลัวนั้นทำฉันผงะไป"

play music music_rin fadein 0.5

show rin negative_angry
with charachange

rin "ฮิซาโอะ ฉันไม่รู้หรอกนะว่านายจะไม่อยากหรืออยากฟังสิ่งที่ฉันจะพูดต่อไปนี้ แต่ฉันไม่สนหรอก หรือต่อให้ฉันต้องสน\nนายเองนั่นแหละที่ทำให้ฉันไม่มีทางเลือก"

rin "ประจำเดือนฉันมา แล้วฉันต้องให้คนช่วย แต่ฉันคิดว่าความสัมพันธ์ของเรายังไม่ถึงขั้นนั้นที่ฉันจะให้นายมาถก\nชุดชั้นในฉันลงในห้องน้ำหญิงได้ ต่อให้นายจะเสนอตัวก็เถอะ"

rin "นั่นคือเหตุผลว่าทำไมนายควรรออยู่ตรงนี้ระหว่างที่ฉันไปตามหาเอมิ"

"เลือดแล่นขึ้นมาที่แก้มฉันราวน้ำทะเลที่สูงขึ้น ในสมองนึกตะกุยตะกายหาคำพูดเพื่อตอบกลับ แต่ก็คิดได้แค่เพียงว่า\nสิ่งที่ออกมาจากปากรินเมื่อกี้คือสิ่งที่ฟังรู้เรื่องที่สุดตลอดสี่วันที่ผ่านมาที่ได้รู้จักเธอ"

hi "ครับ"

hide rin
with charaexit

stop music fadeout 4.0

"ฉันเบือนหน้าหนีด้วยไม่อยากสบตาเธอ ทำทีเป็นมองพ่อแม่คนอื่นอยู่"

"ฉันเห็นรินหันขวับแล้วเดินออกไปไม่รีรออยู่ที่หางตา"

"ฉันอายจนแทบจะแทรกแผ่นดินหนี"

"รินจะไปนานแค่ไหนนะ…จะกลับมาหรือเปล่าเถอะ"

scene bg mural at Transform(xalign=0.6)
with shorttimeskip

play music music_dreamy fadein 3.0

"สุดท้ายก็กลับมา อยู่ ๆ เธอก็โผล่มาแล้วมานั่งลงที่เดิมข้าง ๆ ฉัน"

show rin basic_deadpannormal_close at Slide(0.8,0.5,0.7,0.5,1.0)
with Dissolve(1.0)

rin "กลับมาแล้ว"

"น้ำเสียงเธอราบเรียบราวที่ฉันทำเด๋อไปไม่เคยเกิดขึ้น ฉันเองก็อยากลืม ๆ ไปเหมือนกันจึงเงียบไว้"

scene bg mural_ss at Transform(xalign=0.6)
show rin basic_deadpannormal_close_ss at tworight
show rin_shadow basic behind rin:
    xpos 0.7 ypos 1.0 xanchor 0.5 yanchor 0.85
    easein 3.0 xpos 0.8 yanchor 0.9
with Dissolve(3.0)

"เวลาผ่านไปอย่างเชื่องช้า แสงอาทิตย์ส่องผ่านเหนืออาคารหลักมาต้องเข้าตาฉันพอดี แต่ฉันก็หรี่ตาไว้ไม่ยอมขยับตัว"

"พอหรี่ตาไปไม่นานก็เริ่มปวดตา แล้วก็ปวดขมับขึ้นมาด้วย"

hi "ปวดหัว เธอเชื่อมั้ยว่าวันนี้เป็นวันที่ปวดหัวมาก"

show rin basic_deadpan_close_ss
with charachange

rin "หิวมั้ย"

hi "แล้วมันเกี่ยวกับที่บ่นปวดหัวยังไง"

show rin basic_deadpansurprised_close_ss
with charachange

rin "ก็ไม่ ที่ฉันถามคือฉันหิว"

"…"

"ความไร้สาระในความจริงจังที่แสนซื่อนั้นทำเอาฉันคลายหงุดหงิดทันที ฉันรู้สึกว่าตัวเองยิ้มอยู่มุมปากอีกแล้ว"

hi "เอาจริงฉันก็หิวเหมือนกัน"

hi "เดี๋ยวไปซื้อของกินให้ เธอจะเอาอะไร ฉันเลี้ยงเอง"

show rin basic_lucid_close_ss
with charachange

rin "อะไรก็ได้"

show rin basic_deadpannormal_close_ss
with shorttimeskip

"พอซื้อมาแล้วฉันก็แบ่งส่วนหนึ่งให้ริน อีกส่วนเก็บไว้ให้ตัวเอง จากนั้นพวกเราก็กินกันไม่คุยอะไร"

show rin negative_spaciness_close_ss
show rin_shadow negative at Transform(xpos=0.8,ypos=1.0,xanchor=0.5,yanchor=0.9)
with charachange

"รินแหงนหน้ามองโดยยังคาบส้อมไว้ที่มุมปาก"

rin "เมฆคืออะไรเหรอ ฉันคิดมาตลอดว่าเป็นความคิดของท้องฟ้าหรืออะไรอย่างนั้น เพราะเป็นสิ่งแตะต้องไม่ได้"

hi "เธอเคยคิดงั้นตอนเป็นเด็กเหรอ"

rin "เปล่า สัปดาห์ที่แล้ว"

rin "อาจจะเพราะบางทีฉันรู้สึกเหมือนความคิดตัวเองเป็นก้อนเมฆ นุ่มฟู ขาว เชื่องช้า"

rin "เหมือนในหัวฉันมีท้องฟ้าอยู่ เหมือนในหัวฉันคือท้องฟ้า"

hi "ท้องฟ้าในหัวเธอเหรอ"

rin "หลับตาแล้วคิดถึงท้องฟ้าสิ นายจะคิดอะไรอย่างอื่นต่อไม่ได้เลยจนกว่าจะหยุดคิดเรื่องนั้น"

scene black
with shuteye

"ฉันลองทำดู เออแฮะ จริง เวทมนตร์เหรอ"

scene bg mural_ss at Transform(xalign=0.6)
show rin basic_deadpannormal_close_ss at tworight
show rin_shadow basic behind rin at Transform(xpos=0.8,ypos=1.0,xanchor=0.5,yanchor=0.9)
with openeye

"พอลืมตามาก็เห็นสายตาของรินจ้องมองฉันอยู่จนรู้สึกอึดอัดเพราะเธอไม่พูดอะไรเลย ฉันเบือนหน้าหนี"

scene bg misc_sky_ss at Fullpan(20.0)
with locationchange

hi "เมฆคือน้ำ เป็นไอน้ำ"

hi "คนเขาว่ากันว่าน้ำแทบทุกหยดบนโลกใบนี้ล้วนเคยเป็นเมฆมาก่อนทั้งนั้น"

hi "ทั้งน้ำตา ทั้งเหงื่อ ทั้งเลือดทุกหยดที่ออกมาจากร่างกายก็จะกลายเป็นก้อนเมฆ พอตายไปแล้วน้ำที่อยู่ในตัวก็จะขึ้นไป\nอยู่บนนั้นเหมือนกัน แต่อาจจะใช้เวลาหน่อย"

rin "นายอธิบายได้ดีกว่าทุกอันที่ฉันคิดไว้อีก"

hi "เพราะมันจริงไง"

rin "งั้นก็คงจริงแหละ"

"ฉันกินต่อก่อนที่ของกินจะเย็นชืด"

"กำแพงคอยเป็นร่มเงาให้ยามตะวันเคลื่อนคล้อยไปตามผืนฟ้า"

"แต่ยามเย็นก็ค่อย ๆ คืบคลานเข้ามาทับยามบ่ายแล้ว มื้อเที่ยงของเราจึงดูจะเป็นมื้อเย็นไปเสียมากกว่า หรือมื้ออะไร\nสักอย่างที่เอาไว้เรียกเวลามากินช่วงนี้"

"จะเรียกว่าอะไรก็ช่าง แต่ได้กินแล้วรู้สึกดีสุด ๆ เพราะไม่มีอะไรตกถึงท้องมาแต่เช้าแล้ว"

"…"

"พอท้องอิ่มฉันก็ถอนหายใจ รินยังกินไม่หมดแต่ก็ดูอิ่มแล้วเหมือนกัน"

"ฉันเอนหลังดื่มด่ำไปกับบรรยากาศ ฝูงชนบางตาลงแล้ว แต่กิจกรรมยังดำเนินต่อ ทุกคนดูจะสนุกกัน"

"ซึ่งก็ไม่แปลก เป็นอากาศอบอุ่นอย่างวันอันลงตัวในฤดูร้อนที่ร้อนแต่พอดี ไม่ได้ร้อนจนอยู่ไม่ได้"

"พระอาทิตย์จะตกแล้ว เวลาผ่านไปไวเหลือเกิน"

scene bg mural_ss at Transform(xalign=0.6)
show rin basic_deadpannormal_close_ss at tworight
show rin_shadow basic behind rin at Transform(xpos=0.8,ypos=1.0,xanchor=0.5,yanchor=0.9)
with locationchange

hi "เรานั่งกันมาหกชั่วโมงแล้วนะ"

show rin basic_deadpansurprised_close_ss
with charachange

rin "ใช่แล้ว"

show rin basic_deadpancontemplation_close_ss
with charachange

rin "นายอยากทำอะไรอย่างอื่นบ้างแล้วหรือไง"

hi "ก็ไม่ ไม่หรอก"

show rin basic_deadpannormal_close_ss
with charachange

rin "ฉันก็ไม่"

show rin basic_lucid_close_ss
with charachange

"เธอปรับท่านั่งแล้วเอนกับกำแพง ฉันก็ทำตัวให้สบายอย่างเธอบ้าง"

"เรานั่งเงียบไม่พูดไม่จากันอยู่หลายนาที"

"ฉันลองจับอารมณ์ของรินดูจากท่าทาง ความเกร็งของกล้ามเนื้อ เศษเสี้ยวสีหน้าอารมณ์ที่โผล่มาได้แวบหนึ่ง แต่ก็\nเปล่าประโยชน์ ยังเป็นคนที่ดูไม่ออกเหมือนเดิม"

$ renpy.music.set_volume(0.5, 0.0, "ambient")
play music sfx_crowd_outdoors channel 6 fadein 1.0

scene bg school_dormext_full_ss
show crowd_ss
with locationchange

"ผู้คนเดินกันขวักไขว่คุยกันจอแจ มีน้อยคนที่จะสนใจภาพเขียนผนังจริง ๆ ไม่ต้องนับว่ามีคนที่สนใจเราด้วยหรือเปล่า\nด้วยซ้ำไป"

"ฉันคลำก้อนกรวดสองสามก้อนเล่นเหม่อ ๆ "

"หาอะไรทำเพื่อให้มีอะไรทำ เป็นความว่างโดยแท้จริง"

"พระอาทิตย์คล้องลงลับหลังต้นไม้ไปทีละน้อยเปลี่ยนสีท้องฟ้าตามเส้นขอบฟ้าจากสีเหลืองทองให้เป็นสีส้มและสีแดงไป\nตามเวลาที่พระอาทิตย์ใกล้จะลับขอบฟ้า"

"กินเยอะขนาดนั้นแล้วรู้สึกหนักท้องเหมือนกินตะกั่วเข้าไปเลยแฮะ แต่ผนังอิฐนี่ก็เอนสบายดีเกินคาด"

"ฉันถ่างตาฝืนความง่วงงุนที่เข้าทับถม แต่ก็เปล่าประโยชน์"

scene black
with shuteye

stop music fadeout 4.0
$ renpy.music.stop(channel=6,fadeout=2.0)

with Pause(4)
$ renpy.music.set_volume(1.0, 0.2, "ambient")
play ambient sfx_fireworks fadein 1.0

scene bg misc_sky_ni
with openeye

"ฉันสะดุ้งตื่น"

"แรงสะเทือนเบา ๆ สั่นไปทั่วพื้นที่โรงเรียน ภาพประกายสีสดใสจาง ๆ ผ่านเข้ามาในสายตาอย่างดวงดาว"

"มีบางอย่างพุ่งออกมาจากสนามกีฬาขึ้นไปยังท้องฟ้า"

"เส้นแสงลากตามขึ้นไปจนแตกออกเป็นแสงไฟสีแดงและสีเหลืองอยู่บนท้องฟ้าเหนือโรงเรียนพร้อมเสียงดังสนั่นอีกครั้ง"

show fireworks
with dissolve

"พลุ"

"แสงที่ประกายอยู่บนผืนผ้าท้องฟ้ายามราตรีทำให้ฉันรู้ตัวว่าตอนนี้ค่ำแล้ว"

"นี่หลับไปนานแค่ไหนแล้วเนี่ย ตรงแขนขวาก็รู้สึกหนัก ๆ "

"พอจะลองยืดเส้นดูก็พบสาเหตุ"

play music music_twinkle fadein 1.0

show rin basic_lucid_close_ni:
    xpos 1.0 ypos 1.1 xanchor 0.5 yanchor 1.0
    easein 1.0 xpos 0.9
with Dissolve(1.0)

"รินนอนพิงไหล่ฉันจนแทบจะไหลลงตักแล้ว"

"เธอหลับสนิทไม่มีทีท่าว่าจะตื่นพลุเลย"

"เธอหลับตาพริ้มปากเผยอเล็กน้อย เป็นใบหน้ายามหลับที่ดูใสซื่ออย่างเด็ก ๆ "

"ฉันใช้แขนข้างที่ว่างเขย่าตัวรินเบา ๆ หวังให้ตื่น หรือถ้าไม่ตื่นอย่างน้อยก็ขยับตัวเธอให้แขนฉันได้เป็นอิสระ"

"เธอทำหน้าเคร่งขึ้นมาคล้ายไม่อยากตื่น"

show rin basic_deadpanupset_close_ni at Transform(xpos=0.9, xanchor=0.5, ypos=1.1)
with charachange

"เธอลืมตาขึ้นมาช้า ๆ แต่ก็ยังไม่เบิกเต็มที่ เปิดเพียงพอให้แสงสว่างจ้าจากพลุที่แตกลอดผ่านขนตาเธอมาสะท้อน\nกับนัยน์ตาสีเขียวของเธอได้ เธอมองมาทางฉันแล้วขมวดคิ้ว"

show rin basic_deadpan_close_ni
with charachange

rin "ขออีกหน่อยนะ"

"เสียงรินทั้งงัวเงียและเอื่อยเฉื่อย เธอปล่อยให้คำพูดพึมพำที่แทบจะฟังไม่รู้เรื่องนั้นลอยค้างอยู่ในอากาศ"

"เหมือนเธอจะยังไม่รู้ตัวดีว่าเกิดอะไรขึ้น"

show rin basic_lucid_close_ni
with charachange

"รินทิ้งตัวพิงไหล่ฉันอีกครั้ง"

"เธอยุกยิกไปมาปรับท่าให้นอนสบายจนฉันรู้สึกไม่สบายตัวเอามาก ๆ ไปด้วย"

"จนฉันรู้สึกถึงร่างกายอันอบอุ่นของเธอและหน้าอกของเธอที่ขยับไปมาและถูกแขนฉันได้แบบชัดเกินไป ไม่นาน\nลมหายใจของเธอก็กลับมาเข้าที่"

"ฉันอดไม่ได้ที่จะชื่นชมพรสวรรค์ในการหลับของเธอ หรือพรสวรรค์ในการวางใจใช้คนที่เธอเพิ่งรู้จักมาไม่ถึงสัปดาห์\nมาเป็นหมอนหนุนนอน"

"พลุทยอยขึ้นท้องฟ้าทีละดอก แตกออกมาเป็นดอกไม้สีแดง เขียว และทอง ตามมาด้วยเสียงโห่ร้องของผู้ชม"

"ฉันฝืนใจไม่นึกถึงความใกล้เกินไปของริน เพราะคิดไปแล้วจะทำอะไรได้ หวังว่าที่บอกว่าอีกหน่อยนั่นคืออีกหน่อยจริง ๆ "

"แสงระยับโผล่มาแล้วดับไปในพริบตาทีละดอกแต่งแต้มท้องฟ้าราตรีให้เป็นภาพวาดนามธรรมที่ไม่อยู่นิ่ง"

"ฉันฟังเสียงสนั่นที่ส่งมาไกล ๆ นั้นกับเสียงหายใจของรินพลางทำใจให้สบายไม่คิดถึงความไม่สบายตัวที่เป็นหลังตื่นมานี้"

"โชคดีที่อีกหน่อยนั้นคืออีกหน่อยจริง ๆ รินตื่นจากนิทรามาก่อนพลุจะหมดพอดี"

show rin relaxed_sleepy_close_ni
with charachange

rin "ฉันหลับไป"

show rin basic_awayabsent_close_ni
with charachange

show rin basic_lucid_close_ni
with charachange

show rin basic_awayabsent_close_ni
with charachange

"เธอลืมตาขึ้นมาแล้วกะพริบตาอยู่สองสามครั้ง"

hi "เธอนอนหนุนฉันหลับ สองครั้ง"

show rin basic_absent_close_ni
with charachange

rin "ไม่ชอบเหรอ"

hi "เอ้อ…ก็…"

show rin basic_absent_close_ni:
    ease 1.0 ypos 1.0

"แม้ฉันจะยังพูดอ้ำอึ้งไม่จบประโยค เธอยืดตัวนั่งตรงแล้วกระเถิบตัวห่าง"

hi "ก็เธอหนักอะ"

"โกหกหรอก เธอเบายิ่งกว่าอะไร แต่ขอแซวสักหน่อย ถึงจะเล่นขี้โกงก็เถอะ คำบ่นแบบหยอก ๆ นั้นของฉันไม่อาจทำให้\nรินตอบสนองอะไรเพราะเธอหันมองไปยังแสงพลุที่อยู่บนท้องฟ้า"

show rin negative_spaciness_close_ni at Transform(xpos=0.9, xanchor=0.5)
with charachange

"คล้ายว่าเธอถูกแสงสีอันหลากหลายของพลุนั้นดึงดูด"

"แขนฉันรู้สึกยุบยิบขึ้นมาเมื่อเลือดเริ่มเดิน รู้สึกไม่ดีเท่าไหร่ แต่ก็จะได้หายเวียนหัวสักที"

"พลุดอกแล้วดอกเล่าแล่นขึ้นไปบนท้องฟ้า หมู่เมฆสะท้อนสีสันอันสดใส"

"เราทั้งสองคนจ้องมองอยู่เหนือต้นไม้ตกตะลึงไปกับการแสดงนี้"

"ถ้าขยับไปอีกหน่อยก็จะได้เห็นท้องฟ้าแบบชัด ๆ เต็มตา แต่เราสองคนก็ไม่มีใครสนใจจะชวนขยับ"

show rin negative_worried_close_ni
with charachange

rin "ฉันชอบพลุมากเลยนะ ถึงเวลาดูแล้วจะรู้สึกเศร้า ๆ ก็เถอะ มั้งนะ เหมือนพลุมันทำตัวให้เสียงดังกับมีแสงจ้าเพื่อให้คน\nสนใจมอง แต่พอมีคนมองตัวมันก็หายไปแล้ว"

show rin negative_sad_close_ni
with charachange

rin "เหมือนไม่ใช่ของที่มีอยู่จริงเลย"

"…"

hi "มีอยู่จริงสิ จริง ๆ นะ"

hi "ทุกอย่าง…มีอยู่จริงนะ รู้มั้ย"

hi "ถ้าลองมาคิดดี ๆ ไม่มีอะไรที่อยู่ได้นานหรอก แม้แต่ชีวิตของฉันหรือเธอก็จะเป็นเพียงชั่วพริบตาถ้าเทียบกับช่วง\nประวัติศาสตร์ที่ยาวนาน เหมือนพลุพวกนั้นไง แตกตุ้บแล้วเราก็หายไป"

hi "แต่พวกเราก็มีอยู่จริง อยู่ตรงนี้"

"ใช่แล้ว นี่คือความเป็นจริง รินที่นั่งข้างฉัน เสียงสนั่นของพลุ ท้องฟ้ากว้างไกล เหล่านี้มีอยู่จริงแน่แท้ ถึงแม้เราจะไม่ได้\nอยู่ตรงนี้ไปตลอดกาลก็ตาม"

"ในใจพลันรู้สึกอบอุ่น ฉันนึกสงสัยว่าเพราะรินที่อยู่ใกล้ขนาดนี้หรือแค่เพราะความรู้สึกที่ได้มีชีวิตอยู่"

show rin negative_spaciness_close_ni
with charachange

rin "ฉันไม่รู้ว่าจะพูดอะไรต่อดี"

hi "ไม่เป็นไรหรอก…ฉันก็คงแค่พูดกับตัวเองนั่นแหละ"

hi "แต่ก็ พลุน่ะสวยนะ…แต่ไม่รู้สึกว่าไร้สาระไปหน่อยเหรอที่ทุ่มเงินไปตั้งเยอะเพื่อประกายไฟสวย ๆ ที่โผล่มาเสี้ยววินาที\nอย่างนี้น่ะ"

show rin negative_sad_close_ni at Slide(0.9,0.5,0.7,0.5,1.0)
with None

show rin relaxed_doubt_close_ni at Slide(0.9,0.5,0.7,0.5,1.0)
with Dissolve(1.0)

"รินละสายตาจากพลุที่ยังจุดอย่างต่อเนื่องนั้นแล้วเอนหลังมองฉันพลางทำหน้าเบ้"

rin "โห ไม่ยักรู้ว่านายเป็นพวกขวางโลก"

hi "จะว่าขวางโลกก็แรงไปหน่อยมั้ง ฉันว่าฉันเป็นพวกอยู่กับความเป็นจริงมากกว่า"

show rin relaxed_surprised_close_ni at tworight
with charachange

rin "คนขวางโลกเขาก็เรียกตัวเองกันอย่างนั้นไม่ใช่เหรอ"

stop ambient fadeout 1.0
hide fireworks
with dissolve

"พลุดอกสุดท้ายประกายสีเงินและน้ำเงินแล้วดับไป ทิ้งไว้เพียงความเงียบอันวังเวงครู่หนึ่งก่อนคนจะทยอยกันออกไปที่\nประตูหลักอย่างฝูงวัวควาย"

"ควันสีเทาคลอยคว้างอยู่ตามหอและสนามกีฬา กลิ่นดินปืนฉุน ๆ ที่ลอยมาตามควันนั้นเหม็นจนเหมือนติดอยู่กับผม\nและเสื้อผ้า"

hi "งานเลิกแล้วเหรอ"

show rin negative_spaciness_close_ni
with charachange

rin "คิดว่านะ"

scene bg school_dormext_full_ni
with locationchange

"ฉันลุกขึ้นยืนยืดหลังที่ปวดหนึบ นอนพิงกำแพงอิฐก็ไม่ใช่ความคิดที่ดีเท่าไหร่แฮะ"

show rin negative_spaciness_ni:
    xpos 0.7 ypos 1.0 xanchor 0.5 yanchor 0.8
    easein 1.0 yanchor 1.0
with Dissolve(1.0)

show rin basic_absent_ni at tworight
with charachange

"รินลุกขึ้นบ้างแล้วมองหน้าฉันด้วยสายตาคาดหวังบางอย่างที่มากับใบหน้าอันอ่อนเปลี้ย"

"แม้ตาเธอจะจับจ้องได้ไม่ค่อยดี แต่เธอก็มองตรงมาที่ฉัน เป็นอะไรที่เธอทำไม่บ่อยนักในรอบสัปดาห์ที่ผ่านมานี้"

hi "เอ่อ…แล้ว…"

"จู่ ๆ ฉันก็รู้สึกตัวขึ้นมาว่าที่มาวันนี้เหมือนมาเดตกัน ถึงจะโดยไม่ตั้งใจก็เถอะ แถมไม่ได้ทำอะไรด้วย"

"แต่ถ้าไม่…ทำไมเลือดถึงแล่นมาที่แก้มฉัน ทำไมฉันถึงอ้ำอึ้ง"

"ฉันไม่รู้ว่าจะพูดอะไรดี ยิ่งเหมือนรินรอให้ฉันพูดอะไรด้วย แต่โชคดีที่เธอชิงพูดตัดปัญหาขึ้นมาก่อน"

show rin basic_deadpannormal_ni
with charachange

rin "ฝันดี ฮิซาโอะ"

hide rin
with charaexit

"เธอมองฉันหัวจรดเท้าแบบผ่าน ๆ อีกครั้งแล้วหมุนส้นเท้าเดินออกไป หายไปกับกลุ่มคน"

stop music fadeout 7.0

"…"

hi "โอเค…ฝันดี"

"ฉันถูกทิ้งให้ยืนอยู่ที่เดิม ตอบกลับกับอากาศยามค่ำคืนอันเย็นเยียบ"

"เฮ้อ"

"งานเทศกาลไม่เหมือนที่คิดไว้เลย"

"สุดท้ายก็อยู่ที่เดิมกับรินทั้งวัน ถึงเราสองคนจะไม่มีใครตกลงหรือชวนกันไปทำอะไรก็เถอะ"

"ฉันก็แค่ไม่รู้จะทำอะไรแล้วดี และดูเหมือนเธอก็คิดเหมือนกัน"

"ความอบอุ่นจากร่างกายรินยังคงตกค้างอยู่กับตัวฉัน ก่อนจะอันตรธานไปในค่ำคืน"

window hide

    
#******************
#Lilly/Hanako path start

label th_A41b:
#lol label hackery. Yeah...

scene bg school_gardens
with shorttimeskip

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_crowd_outdoors fadein 0.5
play music music_soothing fadein 0.5

"After buying a plastic plate of takoyaki from a stall belonging to the class next to ours, I take a seat in the school gardens and watch people pass as I tentatively nibble away at the rather bland-tasting item."

"I guess I shouldn't complain. It's better than nothing and didn't cost much."

"As I look out towards the school, watching the people coming and going proves a surprisingly entertaining way of passing the time as I eat."

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

show bg school_courtyard
show crowd
with locationchange

"Little children accompanied by parents or grandparents scamper about in the din from event to event; one hand dragging their company and the other bearing an oversized, colorful snack."

"I can't help but notice the age range among the people here is skewed towards the elderly, something that I'd also noticed when I was walking around town."
#If he's on Hanako's path, has he actually walked around town at that point?

"This must be one of those towns where the only people left are those that lived here their whole lives and ardently refuse to leave, and those wanting to live out the rest of their days in one of the increasingly few tranquil places."

"I guess that also goes a way to explaining how conservative Yamaku's school culture seems to be."

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

scene bg school_gardens at Fullpan(8.0)
with locationchange

"Not that I mind one bit. I kind of like how calm Yamaku and its surroundings are."

"The heat, though, is another matter entirely. Sitting in one place for so long has focused my mind on how annoyingly humid it's getting, now that the hottest part of the day is here."

"I'd better get moving if I—{w=.5}{nw}"

play sound sfx_warningbell

"Gah!"

"The sound of the carillon bells takes me completely by surprise as I stand up, a reaction shared by a few of the people strolling around as well."

"The PA system crackles to life after the tolling bells end. Its age shows as the principal makes a barely intelligible announcement over it, officially opening the festival that's very much in full swing."

"It's quite amusing to contrast the pleasant smiles of the older folk against the alternatively pained and bored grimaces of their younger charges. The students, on the other hand, seem to pay it little heed."

"Nevertheless, as the address finally ends, all are united in polite - if not overly enthusiastic - applause, and then get back to business."

"Slipping a hand in my pocket to look as relaxed as possible, I casually glance around for something to do."

"…It's somewhat difficult to see very far with all the people around."

"I decide to fall back on a tried and trusted rule: go where everyone else seems to be gathering. Right now, that's the school courtyard and surroundings."

play sound sfx_can_clatter

"Throwing the used plate into a trash can, I make my way towards the school building."

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

scene bg school_courtyard
show crowd
with locationchange

"Seeing the number of stalls around the perimeter of the school building surprises me. Quite a few of the classes must have opted to have multiple stalls."

"In deciding which to visit first, I catch sight of a familiar banner with a blue patterned border and red text."

"Lilly's stall is as good a place to start as any. I'm curious as to how it's going, after all of the work she and her class have been doing for it."

$ renpy.music.set_volume(0.5, 2.0, channel="ambient")

scene bg school_stalls2 at Fullpan(8.0, dir="left")
with locationchange

"Stepping up to it, I begin to see why the class took so long to organize everything."

"Easily twice as wide as many of the other stalls and with equipment for cooking strewn everywhere, it's closer to an outdoor restaurant than a festival event."

"As a student in front of me takes a bowl of noodles and leaves, I walk up to the counter."

"The girl behind it seems quite exasperated, and asks me to wait a moment before she disappears underneath the counter."

"Seizing the moment, I take a quick glance around."

"Steam seems to be rising from everywhere, as pots and pans simmer away. The most blind of the students are unpacking ingredients while being helped by someone who is probably the teacher of 3-2."

"It doesn't take long to notice Lilly among them, talking with the teacher as she quickly counts out the boxes and packets with her fingers."

"From her expression and the fact that both she and the teacher seem to be in a state of mild confusion, it appears that there's been some problem in coordination."

"Before I can stare any longer, the girl behind the counter pops up again, only to look back and ask where the spare change box is."

"Lilly pauses for a moment, before she and the girl switch places at the counter and the teacher quickly walks off somewhere."

stop music fadeout 2.0

show bg school_stalls2 at left
show lilly basic_smileclosed at center
with charaenter

li "Sorry about that, we're having a few problems. What would you like?"

"It takes me a second to remember what I'd come here for. My eyes quickly dart to the side to read the menu sitting on the counter."

hi "Oh, uh, I guess some… miso soup?"

show lilly basic_surprised
with charachange

li "Ah, is that Hisao?"

hi "Yep. Looks like you're pretty busy."

play music music_ease fadein 6.0

show lilly basic_weaksmile
with charachange

"Her face all but confirms it as she drops her waitress facade."

li "Somewhere along the line, our order got mixed up. We're trying to fix it now, but it looks like we only have half of what we needed."

hi "Wouldn't serving smaller portions cover over the problem?"

show lilly basic_sad
with charachange

li "It seems like that's what we'll have to do, though I wish we didn't. The fact that a good half of our class is gone doesn't help, either."

"I glance behind her to see how many people are actually operating the stall."

"It couldn't be over about eight."

hi "I take it that's why your teacher left?"

show lilly basic_weaksmile
with charachange

li "That's right. She's going to try and round up a few more of our classmates to help."

"Hearing the sound of footsteps behind me, I stealthily glance backwards to see an elderly couple taking a place in the line. I guess I'd better stop loitering around and chatting."

hi "Here's the money for the soup."

show lilly basic_smile
with charachange

li "Soup… oh, right, coming right up."

"Lilly turns and calls for a bowl of miso soup as I hand over the money for it."

show lilly basic_reminisce
with charachange

"Taking the coins in her palm, I can't help but notice how efficiently she counts them out with her long, pale fingers. Eventually satisfied that I've handed over correct change, she puts it into a small metal tray."

show lilly basic_smileclosed
with charachange

"It isn't long before the soup is made and carefully handed to her, after which she turns and subsequently passes it to me."

hi "Thanks. I'll come back to drop off the bowl."

show lilly basic_smile
with charachange

li "Thank you, Hisao. Oh, there is one other thing. Have you seen Hanako?"

hi "Hanako… no, not today. Why?"

show lilly basic_sad
with charachange

"She gives a small sigh of abject disappointment."

li "It's okay. I was just wondering what she was doing for the festival."

show lilly basic_weaksmile
with charachange

li "You'll come back when you're done, then?"

hi "Sure. I'll keep an eye out for Hanako, too."

li "Thank you, Hisao."

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

scene bg school_courtyard
show crowd
with locationchange

"I walk off from the stall and find a seat, carefully cradling the steaming wooden bowl in both hands."

"Compared to the dumplings from before, this is quite nice. A little cool compared to what it probably should be, perhaps, but the flavor is enough to cover for that reasonably well."

"As I drink, I can't help but feel somewhat guilty for not being as involved in the festival as the others."

"It can't really be helped, considering I was dropped into the school only a week ago, but it still weighs heavily on my mind."

"That, and the fact that a few students don't really seem to be enjoying the festival as much as the visitors."

"Eventually I finish my bowl and leave for the stall, to drop it off."

"Considering that there seems to be no line at all, I take my time walking up."

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

scene bg school_stalls2
with locationchange

"It seems the teacher's mission paid off: there are now over a dozen students helping, and much of the unpacking has been done."

"Despite most of them seeming quite relaxed as they work, Lilly still appears to be somewhat stressed."

# This is where K1 and L1 would split



label th_A41a:
#Lilly Path Festival scene.

stop music fadeout 4.0

"…Right. I know what I'll do. Even if it's just one person, I'll make the festival more enjoyable for her."

"As I place the bowl on the counter, I call out to Lilly."

show lilly basic_smile at center
with charaenter

li "Ah, Hisao. You brought it back?"

hi "Yeah, here."

hide lilly
with charaexit

"I slide it into her hands, and she takes it over to someone who is apparently on cleaning duty. Considering that I didn't see them here before, it's probably a penalty for their tardiness."

hi "Hey, Lilly?"

show lilly basic_smileclosed at center
with charaenter

"She perks up and returns to the counter as she hears my voice again, realizing that I'm still here."

hi "Want to go see some more of the festival?"

play music music_another fadein 0.5

show lilly basic_pout
with charachange

"She puffs her cheeks disapprovingly. It looks kind of cute, and in complete contradiction to her usually reserved nature."

"It takes a few seconds for me to get what she's taking issue with. Whoops."

hi "Ah… um, I didn't mean to…"

show lilly basic_giggle
with charachange

"Lilly giggles at me, exposing her teasing for what it is."

li "You're still not used to the school, are you?"

"She got me."

show lilly basic_reminisce
with charachange

li "Still… I kind of need to stay with our stall. It's taken until just now to even get everything unpacked."

"I guess her reluctance shouldn't overly surprise me, considering how much work she's put into this."

hi "Everything seems to be running fine now, though. Besides, you've got extra help on hand, anyway."

show lilly basic_surprised
with charachange

"A boy in the middle of cooking some soba noodles turns towards us, grinning."

"Student" "Go on Lils, you've earned yourself a break. We can hold down the fort, for now."

show lilly basic_displeased
with charachange

li "If you say it's okay, then I suppose so…"

show lilly basic_reminisce
with charachange

li "But, if you need any help—"

"Student" "Then we'll call you. Go on, we'll be fine."

hide lilly
with charaexit

"Lilly finally gives up her resistance as he waves a spatula at her. She feels her way around the back of the stall, and picks up her cane on the way."

"I guess the first thing we should do is look for Hanako. Lilly seems kind of worried about her, and I doubt she'd be the kind of person to enjoy milling about in crowds like this, all alone."

hi "So, I guess we should search for Hanako. Where to, first?"

show lilly cane_reminisce at center
with charaenter

li "Hmm…"

"The both of us go quiet for a moment to think."

hi "Maybe she's in her dorm room?"

li "I doubt it. She doesn't keep too many things in there, so she'd have nothing to do."

show lilly cane_satisfied
with charachange

li "…Ah! The library?"

"As good a place as any to search for an avid reader, I suppose."

hi "The library it is. We'll check there first, then."

$ renpy.music.set_volume(0.2, 1.0, channel="ambient")

scene bg school_lobby
with locationskip

"Aside from the muffled sounds of the crowd seeping in from outside, the inside of the school seems almost deserted."

"In order to make sure everyone had enough room, I guess all the events were organized to be held outside, on school grounds. They're definitely quite large, by any other school's standards."

show lilly cane_smileclosed at center
with charaenter

li "It's nice and quiet in here, isn't it?"

hi "Yeah. Much nicer than the hustle and bustle outside."

stop ambient fadeout 3.0

scene bg school_staircase2
with locationchange

"We take our time and slowly walk through the first floor of the school, eventually reaching the stairs to the second floor."

scene bg school_hallway2
show lilly cane_smileclosed
with locationchange

"I can't help but notice how Lilly anticipates every door and obstacle, her cane remaining still and her hand skating along the hallway railings."

hi "You really know the school well, don't you?"

show lilly cane_smile at center
with charaenter

"She smiles and nods straight ahead."

li "I've been here for a few years now, so I know where everything is."

show lilly cane_sad
with charachange

li "The dorms still trip me up though, sometimes. I haven't been there as long, and they're not as well laid-out as the main building."

li "If I'm remembering right, they used to be unused buildings before being renovated and used as dormitories."

"That explains why the male and female dorms looked different from the outside, and why their rooms seem kind of unusual for sleeping quarters."

"I'd assumed she'd been living in the dormitories since she began attending the school, but now I'm reminded of what she said yesterday."

#"She must've moved in partway through her stay here. No wonder she isn't as familiar with the layout."

hi "That's right, you mentioned that before."

hi "I'd assumed that most of the students here lived in the dormitories once they enrolled. A lot of them seem to, in any case."

show lilly cane_reminisce
with charachange

"Lilly's expression becomes somewhat harder to read, my questioning evidently touching on a delicate point."

li "Well… How should I say…"

show lilly cane_weaksmile
with charachange

li "Everyone… has their reasons."

"Something tells me that one of those with “reasons” is Hanako, hence her tiptoeing around the answer. My own predicament is yet another such case."

"I guess it's a choice everyone here would have to make for themselves… or, in my instance, have made for them."

hi "It can't be helped, I suppose. At least Yamaku itself seems like a nice place."

show lilly cane_smile
with charachange

li "It's good to hear you say that. I'd thought you were coming to dislike it."

hi "What about you, though?"

show lilly cane_surprised
with charachange

"My reversal of Lilly's statement takes her by surprise."

li "I've been here for a while, so…"

hi "It's not that. You just seemed pretty depressed about Akira."

show lilly cane_smileclosed
with charachange

li "Hmm~"

hi "What's with that look?"

show lilly cane_smile
with charachange

li "Akira's taken. Sorry, Hisao."

"Lilly never sees how fast my palm meets my face at her sly accusation."

hi "Hey, I was worried about you. That's no way to respond to concern."

show lilly cane_cheerful
with charachange

"While she gives an amused grin, we round the corner of the hallway and enter the library."

scene ev hana_library_read_std
with locationskip

"As we do so, it isn't hard to spot Hanako, considering that the room is completely devoid of anyone else."

scene bg school_library
with locationchange

"Given that there are no staff around, I guess there's no need to heed the usual library rules. I call out to her."

hi "Hey, Hanako."

show lilly cane_surprised at center
with charaenter

li "Hanako is here?"

"As she hears our voices, Hanako's head flicks up from behind a book, probably the same one she'd been reading on Friday."

show lilly cane_surprised at twoleft
show bg school_library at bgleft
with charamove
show lilly cane_smile at twoleft
show hanako basic_normal at tworight
with charaenter

ha "Hisao… Lilly?"

hi "Just thought we'd drop by. Lilly just managed to escape from the noodle stall, with a little help."

show lilly cane_pout
with charachange

li "That wasn't really an escape…"

show hanako emb_downsmile
show lilly cane_surprised
with charachange

"Hanako gives a small giggle, briefly surprising both of us."

show hanako basic_bashful
with charachange

ha "I just thought that… Lilly might not be enjoying the festival."

hi "Well, now we can enjoy it together, right?"

show lilly cane_smileclosed
with charachange

"The two nod happily before we set out of the library and towards the festivities."

stop music fadeout 2.0

scene bg school_stalls1_ni
with shorttimeskip

$ renpy.music.set_volume(0.5,0.0, "ambient")

play ambient sfx_cicadas fadein 0.3

"I hand over some change to the girl behind the counter, and take the two styrofoam cups of tea. I try to accentuate my bow a bit to cover for the fact that she's quite obviously deaf."

"Come to think of it, I probably should have asked for help instead of leaving those two in the gardens while I bought drinks."

"Trying to juggle the two cups of hot tea (for them) and a can of coffee (for myself, out of a vending machine) isn't exactly easy."

"With some careful maneuvering, though, I manage to keep everything stable and upright as I walk over to the bench where Lilly and Hanako are sitting and chatting."

scene bg school_gardens2_ni
show lilly basic_smileclosed_ni at twoleft
show hanako basic_distant_ni at tworight
with locationchange

"It's actually quite a nice place. Lit only by moonlight, it's tucked away some distance from the main events."

"Compared to how hot it had been during the day, this spot is also pleasantly cool by now."

"Not that it matters all that much. Most of the visitors have moved to areas that are either closer to the fireworks, or higher on the hill in order to view the display apparently planned."

show lilly basic_smile_ni
with charachange

li "Welcome back, Hisao."

show hanako basic_normal_ni
with charachange

"Her ears are good. I'm not exactly close and even Hanako hadn't noticed me."

hi "Here you go. Sorry it's instant, but that's all they had left by now."

"Hanako gingerly takes a cup from my right hand, and I gently place the other into Lilly's outstretched hands."

show hanako basic_smile_ni
show lilly basic_smileclosed_ni
with charachange

li "Did you enjoy the festival then, Hisao?"

hi "Yeah, it was pretty fun."

"An honest answer. Much of the food may have been somewhat subpar, but it was a lot of fun in the end, especially with Hanako and Lilly."

"In fact, I think those two may have enjoyed themselves even more than I did. With both Lilly and me around, much of Hanako's withdrawn nature around others died down enough for her to enjoy herself."

stop ambient fadeout 1.0

$ renpy.music.set_volume(1.0,0.0, "ambient")

play ambient sfx_fireworks
play music music_twinkle fadein 12.0

scene bg misc_sky_ni
show fireworks
with dissolve

"As we sit drinking, the whistle of the first firework rings out before it explodes into a vibrant shower of blue against the night sky, heralding the beginning of the end for the festival."

"Enthusiastic shouts can be heard from the crowds scattered around the school grounds celebrating them."

"For minutes on end, Hanako and I watch the fireworks overhead as Lilly blissfully listens to them with her eyes shut."

"Red, green, yellow, star-shaped, circular and patterned, and all manner of shapes and colors fill the air, one after the other, and dance across the sky."

"No place near where I lived put on such lavish displays. Festivals like this were a thing of the past in such a metropolitan area."

"To be seeing such a sight with these two… it's probably the happiest I've been in a long while."

scene bg school_gardens2_ni
show lilly basic_weaksmile_ni at twoleft
show hanako basic_distant_ni at tworight
show fireshine
with charachange

li "So… that's it. The festival's finally ending."

hi "Yeah."

"She gives a delicate, wistful sigh."

show lilly basic_concerned_ni
with charachange

li "As much as I might complain about all the stuff we have to do, it's still sad that we'll have graduated before the next Yamaku festival."

show lilly basic_concerned_close_ni
with characlose

"I walk forwards and stand beside Lilly, gently resting a hand on her shoulder."

hi "Don't worry. We still have Tanabata later in the year, right?"

show lilly basic_smile_close_ni
with charachange

li "You're right. It would be nice to go there when it comes."

"Minutes of silence pass, with only the blasts of the fireworks to be heard."

"Seeing these two reminds me of those words of advice Lilly had given me as we walked into town together."

"“Cherish the opportunity to make new friends”, huh?"

hi "Hey, Lilly?"

show lilly basic_smileclosed_close_ni
with charachange

"She turns her head slightly to show that she's listening, Hanako's gaze still firmly fixed on the technicolor fireworks bursting overhead."

hi "You mind if I join you two for tea every now and again?"

"The smile on her face is more than enough to see her answer."

show lilly behind_cheerful_close_ni
with charachange

li "It would be a pleasure, Hisao."

stop music fadeout 2.0
stop ambient fadeout 2.0
window hide


###################
#Hanako Path
label th_A42:

#This is the "real" version of H1, edited to fit with the split marked in L1

# Hanako/Lilly festival

scene bg school_stalls2
with None

show lilly basic_reminisce at center
with charaenter

"Lilly doesn’t look impressed at all, and I can't really blame her."

"On top of her issues with her stall, she still seems to be worried about Hanako."

"I can't really help her with the former, so I guess the only way I can help is by trying to take her mind off our shy mutual friend."

"Placing the bowl back on the counter, I call out to Lilly."

hi "Hey, Lilly, don't worry about Hanako. I'll go find her and hang out with her, okay?"

show lilly basic_weaksmile
with charachange

"I can see Lilly's relief plainly written across her face."

li "Thanks Hisao. And if you see anyone from my class, can you tell them to come back here please?"

hi "Will do. Have a good one. And make sure you take a break, okay?"

show lilly basic_smile
with charachange

li "I will if I can. See you later, Hisao."

stop music fadeout 10.0
$ renpy.music.set_volume(1.0,1.0, "ambient")

scene bg school_courtyard
show crowd
with locationchange

"I leave Lilly in the stall and head out in search of Hanako."

"In a way, I feel bad for leaving her with the crowds, but even though she was clearly under pressure, I can't help but think that she is enjoying herself."

stop ambient fadeout 0.5

scene bg school_hallway2
show crowd
with locationskip

play ambient sfx_crowd_indoors fadein 0.5

"The halls are packed with swaying crowds meandering throughout the festival."

"If there's one thing I know about Hanako, it's that she's not going to be anywhere near this."

"And with the students showing their friends and family their dorms, I doubt she'll be there either."

"Following blind intuition, I move against the grain of the crowd."

"Thankfully, this crowd seems to be slightly less festive than your usual festival crowd; I assume this is out of consideration for the student body."

stop ambient fadeout 5.0

"As I force my way through the masses, it doesn't take long for them to thin down into nothingness."

hide crowd
with Dissolve(2.0)

"This is not surprising, since I am standing before the library."

"Even the most eager of students don't bother to show anyone this section of the school."

play music music_happiness fadein 2.0
scene bg school_library
with locationchange

"As I enter the library, the noise of the festival fades into a dull background noise, and soon I am in the reading area at the rear of the room."

"Behind one of the partitioned desks I see the top of a head, with straight, dark hair catching my eye."

hi "Hey, Hanako. I had a feeling I'd find you here…"

show hanako def_shock:
    xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 0.9
    easein 0.5 yanchor 1.0
with charaenter

"The head jumps a little in shock before slowly peeping over the partition."

ha "H-Hisao?"

hi "Hey. Lilly's pretty busy, so she sent me to find you."

show hanako basic_normal at center
with charachange

ha "O-oh. Do you want to sit down?"

hi "Actually, I am feeling a little hungry. Would you like to get something to eat from one of the stands?"

show hanako defarms_worry
with charachange

ha "Um… I… I brought some food so…"

"I shouldn't be surprised, but it was worth a try. Expecting her to go outside today was a long shot."

hi "How about we eat in the tea room? I passed by it on the way here, and no one was around."

hi "We can make some food there, and it'll be a little more comfortable. What do you say?"

show hanako cover_distant
with charachange

ha "S-sure. Let's go."

show hanako basic_distant
with charachange

"Hanako closes her book and puts it away with deliberate, practiced movements."

hi "Good to go?"

show hanako basic_normal
with charachange

ha "Y…yeah."

stop music fadeout 2.0

scene bg school_hallway2
with locationchange

"We walk side-by-side from the library to the tea room."

"As expected, there is barely a soul around."

"If it weren't for the murmurs through the walls, you wouldn't tell that there was a huge festival going on outside."

show hanako emb_downtimid at tworight
with charaenter

"Hanako carries her bag in both hands and focuses on just the floor ahead of her."

show hanako emb_downsmile
with charaenter

show hanako emb_downtimid
with charaenter

"Every now and again, she seems to break her pace a little and steps in slightly shorter paces."

"The first time it happened, I gave it no mind, but I soon notice that she does it on a regular basis."

hi "Are you all right?"

show hanako defarms_worry
with charachange

"She stops dead in her tracks."

ha "W-what?"

hi "I dunno… it looked like you were tripping or something…"

play music music_another fadein 0.5

show hanako emb_blushing
with charachange

"A pink blush rises into her cheeks as her gaze returns to the floor."

show hanako emb_downtimid
with charachange

ha "It… it's nothing."

hi "You know, when you say “nothing” like that, people are inspired to ask further questions."

"For a second I don't think she is going to answer."

"Prepared to leave it be, I almost set off walking again, when…"

show hanako emb_emb
with charachange

ha "It's a… a game."

hi "Game?"

show hanako emb_downsmile
with charachange

ha "Do you… see the floor here?"

"What a bizarre question. The floor looks just like any other floor; covered in those tiles made up from squares of linoleum."

"Nothing noteworthy."

hi "Well, yes. What about it?"

show hanako emb_downtimid
with charachange

ha "Sometimes… when there's no one around… I only step on the darker ones…"

"Hanako's voice trails off as her explanation continues, until I can barely hear her voice over the roaring silence of the empty hall."

hi "Darker ones?"

"Shuffling her feet, Hanako points the toe of her shoe at a tile that is barely a shade darker than the others."

show hanako emb_downsmile
with charachange

ha "L-like these ones."

hi "Oh, right, so these ones are no good?"

"I point out a nearby tile."

show hanako emb_emb
with charachange

ha "Y-yeah. Something… something like that."

hi "Oh, I see. Do you play this game a lot?"

show hanako emb_downsad
with charachange

"Hanako shakes her head."

hi "Just when the halls are empty?"

show hanako emb_emb
with charachange

"She nods."

hi "Well then, no point in stopping, I'm beginning to get really hungry."

show hanako emb_smile
with charachange

"She nods again, this time with a little more enthusiasm."

hi "Well then, let's go."

hide hanako
with charaexit

stop music fadeout 5.0

"We set off down the hall, and this time I notice that Hanako is paying a little less attention to the floor."

"I wonder; just how lonely does someone have to be to come up with a game like that?"

"But, before I realize what I'm doing, I find myself trying to aim each step so it lands on the correct tiles."

play music music_dreamy fadein 2.0

scene bg school_miyagi
with locationchange

"The noise of the festival is slightly louder inside the tea room, but the breeze coming through the open window makes it worth it."

"Without thinking, I walk to the windowsill and inhale deeply. I sometimes forget how clean the air is here compared to back home."

show hanako basic_bashful at center
with charaenter

ha "Do… would you like some tea?"

hi "That would be great, thanks."

hide hanako
with charaexit

"It occurs to me that this is the first time I've been alone with Hanako without her trying to be somewhere else."

"Turning from the window, I watch as she makes a simple pot of tea and arranges some sandwiches onto a plate."

"I've seen her do this before a number of times, but this time she seems slightly different."

"It's like she's…{w} calm."

"Eventually she places the small tray on the table and pours two cups of tea."

"The fresh scent of brewed tea mingles with the breeze, and for a second I feel like I'm the only one in the world."

hi "I think I know why you like this room now."

show hanako defarms_worry at center
with charaenter

ha "Um… I don't know what you mean."

hi "Well, there are quite a few people out there, but in here it's like another world."

hi "You can pretend that there's no one around for miles."

show hanako emb_downtimid
with charachange

ha "Y-you're right."

ha "It's like the world has forgotten this room."

show hanako emb_emb
with charachange

ha "And b-because of that, you can forget about the outside."

"That would be appealing in some cases."

"As far as I can tell, conventional bullying doesn't exist in this school."

"But then again, I haven't seen a single person talk to Hanako besides Lilly."

"If you're ignored by the world, a place where you can forget its existence would hold a special appeal."

hi "That's a good point. It's like this room gives you some kind of complete freedom."

show hanako emb_smile
with charachange

ha "Y-yeah."

show hanako basic_bashful
with charachange

ha "Say… do you play chess?"

hi "Chess? I've played it a bit, I guess."

hi "I take it you've played before?"

show hanako basic_distant
with charachange

ha "A little…"

hide hanako
with charaexit

"Without saying anything more, Hanako moves to one of the cupboards and digs out a small chess set."

ha "Do… do you want…"

hi "Sure, why not?"

"I cut her off, but she doesn't seem to mind it."

scene bg school_miyagi
show hanako basic_normal_close at center
with shorttimeskip

"We arrange the pieces, and before long we are sending pawns charging to their inevitable fates."

"I take my time and intently examine each move and its consequences, nostalgia for the game taking second place to the matters at hand."

"For a time the game is a lengthy battle of attrition, but I spot an opening and tear a line in her defense."

show hanako basic_worry_close
with charachange

"A few moves later, her king is cornered by several of my pieces."

hi "Checkmate."

hi "You're not bad at this, are you?"

"An honest appraisal. Her technique is pretty good, but several times I was able to exploit her lack of prediction."

"I pick up a piece and examine it. It looks relatively new, yet worn for its age."

show hanako basic_smile_close
with charachange

ha "I… I guess not."

hi "Does Lilly play?"

show hanako def_worry_close
with charachange

"The absence of Hanako's answer causes me to think about my question."

ha "A… A bit…"

ha "T-this is the first time I've played against someone… other than her, or…"

show hanako emb_downsad_close
with charachange

"Or…?"

"She cuts herself off abruptly, leaving the answer hanging in the air. Someone she knew before coming to Yamaku, maybe."

hi "Well then, I'm honored to have played against you."

show hanako emb_smile_close
with charachange

ha "Um… can we play again?"

"She asks as if she were asking me to cut off my own hands. The spirit of competition's gotten into her?"

hi "Sure. Though don't expect me to go easy on you this time…"

"Not that I was before, mind. She seems to appreciate the competitive tone."

show hanako emb_downsmile_close
with charachange

ha "S… same here…"

stop music fadeout 2.0

#scene willl flow into K2 with Lilly finishing her time at the café and collecting the
#two to go to the Shanghai



#******************

label th_A43:
#Kenji rou-- er, Deep-Six

scene bg school_dormhallway at bgright
show kenji happy at center
with None

stop music fadeout 2.0

"What am I going to do? I don't have any plans. In hindsight, that's really stupid."

"Maybe I should've asked a girl out? Then again, all things considered, I don't think I could've done anything like that. It's only my first week." 

"A week that I have wasted being awkward around almost everyone, stumbling all over myself trying to get the hang of this place."

"Thinking about it, what have I accomplished?"

"Who would I have even asked?"

"Damn, it seems that Kenji is my only realistic option for a date today."

"This is the most depressing thing that has happened to me since I had a heart attack because a girl confessed her love to me."

"It can't be helped."

play music music_kenji fadein 0.5

hi "I don't know really. I don't have anything I guess, but a fort seems a bit excessive."

hi "You sure you don't want to go outside? It's not like visitors won't come to the dorms today."

show kenji tsun
with charachange

"He looks thunderstruck by this revelation."

ke "Damn, you may have a point. This place is not safe today."

ke "We must find somewhere to hide in."

"He falls silent for a moment, thinking."

show kenji neutral
with charachange

ke "The roof."

hi "What about it?"

show kenji happy
with charachange

ke "We are going to hide out on the roof for today."

ke "It's the perfect place, nobody ever goes up there."

show kenji neutral
with charachange

ke "Meet me there in one hour. I have to prepare."

stop music fadeout 1.0

show kenji neutral at Slide(0.5,0.5,0.4,0.5,0.5, time_warp=_ease_out_time_warp)
with None

hide kenji
with charaexit

play sound sfx_doorslam
with vpunch

"He slams the door shut and the locks click closed."

"Damn, what the hell is wrong with Kenji?"

"And to think I'm now going along with his craziness. It really makes me depressed."

"I feel like a failure."

play ambient sfx_crowd_outdoors fadein 0.3

scene bg school_courtyard
show crowd
with locationskip

"Once I step outside, the din of the crowd greets me."

"The whole school is bustling with activity." 

"There are stalls everywhere, and the crowd swarming between them is considerable."

"I didn't expect the festival would attract so many visitors."

"I have to admit that the people in charge of decorating the place put a lot of effort into it, and it really shows."

"People seem to be enjoying themselves, and the atmosphere is colorful, bright, and happy."

play music music_rain fadein 1.0

"That is, if I weren't suddenly in such a foul mood."

"At the moment, it's more annoying than anything else."

"Well, it can't be helped. I decide to stick with my original plan and eat, then I guess I have to at least see what Kenji is up to on the roof."

"…"

scene bg school_stalls2 at Fullpan(8.0)
with locationchange

"I do a slow circle around the grounds to kill some time, looking at the stalls, but not feeling like playing any of the games any more."

"The garish colors grind my eyes and I feel more and more ill by the minute."

"I can't even decide what I want to eat, and the large selection combined with the masses of energetic festival visitors isn't helping."

scene bg school_stalls1 at bgright
with locationchange

"I just head towards the nearest stall that seems to offer something halfway edible and get in line."

"It turns out to be noodles."

"It also turns out to be not very good."

"Well, at least it's nourishment. It's not like I demand anything else, at this point."

scene bg misc_sky at Fullpan(25.0)
with locationchange

"As I stir my disagreeable noodles, I idly wonder what the others are doing right now."

"Shizune and Misha are definitely somewhere organizing things."

"I'd better steer clear of them. I guess they wouldn't forgive me so easily for leaving them alone with this thing."

"I expect Emi to be buzzing all over the place, being depressingly cheerful."

"There's no chance to find her, but no chance to avoid her either, so it doesn't matter."

"Lilly would probably be helping her class with that festival event, and entirely too busy for another's company."

"Hanako wouldn't want to talk to anyone anyway, either keeping to herself or helping Lilly."

"Rin should be tending to her mural and is probably being unhelpful to any hypothetical interested parties."

"Going there for some peace and quiet seems like the nicest option of the above, but then again, I can't see having art forced on me raising my mood either, so I'll pass."

scene bg school_stalls1 at bgright
with locationchange

"While I was lost in thought, my food seems to have disappeared, and so has my hunger."

"I guess I just blocked out the experience of eating, which should be a good thing."

"Satiated but unsatisfied, I turn to walk towards the main school building. An hour has almost passed already."

play ambient sfx_crowd_indoors fadein 0.3

scene bg school_lobby
show crowd
with locationskip

"The crowd is even thicker in here than it was outside."

scene bg school_hallway3
show crowd
with locationchange

"The hallways are almost unbearable, and I don't even dare to think what's it like inside the classrooms."

stop ambient fadeout 1.0

scene bg school_staircase1
with locationchange

"I head up the stairs to my destination."

"The roof."

"Thankfully, the door at the top isn't locked, but now there's a handwritten sign on it."

window hide

$ written_note("{size=55}{b}OFF LIMITS{/b}{/size}", quiet=True)

window show

"Don't mind if I don't."

scene bg school_roof at bgright
with locationchange

"The festival noise is surprisingly muted up here, and the rooftop looks deserted, as expected."

"Near a place where the cyclone fence has collapsed, there is a pile of blankets that seems oddly out of place."

stop music fadeout 3.0

"Wait."

play sound sfx_rustling

"Did that pile just move a little?"

"That would be strange, as there is no wind at all."

"I carefully stick my hand out and give it an experimental prod."

play sound sfx_impact
show kenji rage_close:
    alpha 0.0 xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 0.7
    easein 0.2 yanchor 1.0 alpha 1.0

with vpunch

$ doublespeak(ke, hi, "AHHHHHHHHHHHHH!")

play music music_comedy fadein 2.0

show kenji rage:
    center alpha 1.0
with charadistant

"Startled, I jump back."

ke "Who is it?"

hi "God damn it, Kenji. It's me."

show kenji tsun at center
with charachange

ke "Oh damn, you scared me, man."

hi "So what are we doing up here?" 

show kenji neutral
with charachange

ke "We're having a picnic."

hi "What?"

show kenji happy
with charachange

ke "Yeah. I have blankets, pretzels and whiskey. This is the ultimate setup, man."

hi "Whiskey?"

hi "Aren't you a bit too young to drink alcohol?"

show kenji tsun
with charachange

ke "I'm 20, y'know."

hi "…you're not."

show kenji neutral
with charachange

ke "I am and so are you."

hi "What? That's absurd."

show kenji tsun
with charachange

ke "Hey, at least YOU get something out of it, all I get is this bottle of whiskey…"

"He's rambling incoherently, but I decide to play along."

hi "So why do you have a bottle of whiskey?"

show kenji happy
with charachange

ke "My mom couldn't come visit for the festival, so she sent me some expensive Single Malt instead."

hi "A likely story."

ke "Want some?"

hi "…"

"It's not like I have anything to lose. This day can't possibly get worse."

hi "…why not."

hide kenji
with charaexit

show bg school_roof at center
with charamove_accel

show kenji happy_close at offscreenleft
with None

show kenji happy_close at twoleft
show bg school_roof at bgleft
with charamove_decel

"We sit down on the pile of blankets Kenji apparently dragged up here."

"He produces an almost full bottle of whiskey and passes it to me."

hi "You didn't even bring glasses?"

show kenji tsun_close
with charachange

ke "No, this is not some romantic princess picnic. What the hell, man?"

show kenji neutral_close
with charachange

ke "This is a manly picnic."

ke "No glasses."

ke "No napkins."

ke "Whiskey only. The beverage of true men."

hi "Whatever."

show kenji happy_close
with charachange

ke "And pretzels."

"I take a closer look at the bottle."

"12 year old single malt whiskey, as he said."

"Shrugging my shoulders, I take a swig. It burns my throat like acid, but the taste isn't unpleasant."

"I feel it going straight into my head, and the aftertaste lingers in the back of my mouth, craving for another swig."

show kenji neutral_close
with charachange

ke "We should outline our counteroffensive and trashtalk women here, where they can't hear us."

show kenji tsun_close
with charachange

ke "Damn, I forgot to bring my graphs."

"I decide to play a drinking game with myself. Every time Kenji mentions “female conspiracy”, I'll take a swig."

$wdt_off(False)

stop music fadeout 2.0

scene black
with delayblinds

centered "Four or five hours, or possibly several days later:\n{w}(I lost track)"

play music music_kenji fadein 0.5

scene ev kenji_rooftop
with delayblinds

window show

ke "You shouldn't feel bad, man! Ease the fuck up! Seriously, seriously!"

hi "I am relaxed, god damn it!"

ke "I'm telling it as I see it!"

scene ev kenji_rooftop_kenji
with flash

ke "Think about it. When did housing and land start becoming more and more expensive? When women began entering the work force, because it created two-income nuclear families."

ke "Yeah I forgot my graphs, but, and you'll just have to take my word for it, women are connected to the decay of all society."

show ev kenji_rooftop_large:
    crop (288, 376, 800, 600)
    ease 1.0 crop (1024, 260, 800, 600)

hi "I see. That is kind of hard to believe."

"Even if I say that, somehow, everything Kenji says seems to make more sense now."

"It all fits together but I don't know if it's because he can explain things more clearly when drunk, or because I understand everything better when drunk."

show ev kenji_rooftop_large:
    ease 1.0 crop (288, 376, 800, 600)

ke "No man, think. Think! Think of the deeper implications!"

ke "People could afford to start saying “Oh well, since two members of the family are now earning money as opposed to one, they can surely afford something like rising costs of ownership.”"

show ev kenji_rooftop_large:
    ease 1.0 crop (1024, 260, 800, 600)

hi "I see your point. But land in Japan has always been expensive."

show ev kenji_rooftop_large:
    ease 1.0 crop (288, 376, 800, 600)

ke "…And the price of land generally goes up when a country starts undergoing industrialization. …But no! It's because of women! Correlation equals causation, you know."

show ev kenji_rooftop_large:
    ease 1.0 crop (1024, 260, 800, 600)

hi "I thought correlation didn't equal causation. Well, whatever, maybe you're right."

show ev kenji_rooftop_large:
    ease 1.0 crop (288, 376, 800, 600)

ke "I am always right. Yeah, I bet women created industrialization, too, to cover their tracks."

ke "How diabolical."

ke "So yeah, everyone can go fuck themselves!"

scene bg school_roof_ni
show kenji rage_ni:
    xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 0.9
    easein 1.0 yanchor 1.0
with locationchange

"He stands up, impressing me because I'm fairly sure I couldn't even if I wanted. He yells extremely loudly as if he's lost the concept of volume. I wince and almost want to cover my ears."

stop music fadeout 2.0

ke "Aaagh, how nice it would have been if I could have been down there… But no. You see, thinking like that is a trap, you think you're missing out on something, but at the end of that road is nothing but despair…"

show kenji tsun_ni at center
with charachange

play music music_sadness fadein 1.5

"Kenji snatches back the bottle and leans back his head, attempting to pour the alcohol into his mouth, but just ends up drenching himself in it."

show kenji rage_ni
with charachange

ke "Dammit! See, my aim is terrible, and the bad thing about drinking is that it only gets worse the longer you go!"

show kenji tsun_ni
with charachange

ke "Today is the day of despair."

"His voice immediately drops to almost a whisper, but he starts talking much faster than before, slightly slurring his words from the whiskey."

"As he talks, he waves the bottle around, spilling some of it here and there."

ke "Yeah, you know what was the most shocking event of my life?"

"I have a hazy recollection of him telling about the second most shocking event in his life, which was a bird pooping on his head."

"I don't have particularly great expectations of this, but I nod at him to continue anyway."

show kenji neutral_ni
with charachange

ke "You wouldn't think it, but I had a girlfriend here once, I think it was last year."

ke "Yeah, I just blew your mind, huh? See, I have never told that to anyone."

"It's true, the thought does blow my mind. Suddenly, I want the bottle. I take it from Kenji and knock back as much as I can."

show kenji tsun_ni
with charachange

ke "I was more innocent back then, and I thought she was sane, unlike most women. But then one day, we engaged in… sexual intercourse."

ke "It was pretty okay, but then immediately following the event that is the point of all such things, something strange and scary happened."

show kenji tsun_ni at tworight
show bg school_roof_ni at bgleft
with charamove

"He throws himself up against the fence, leaning on it, his eyes narrowed."

ke "I started feeling incredibly tired and sleepy! That isn't normal, man! What the fuck?"

ke "I mean, normally, that would be a high-tension, adrenaline-pumping moment of anyone's life, but my energy levels were dropping like a brick!"

ke "Something sinister was in the works, I could feel it."

ke "That is when I knew… that women are dangerous, sapping the life force of all men through the one commodity that is almost solely theirs to control!"

ke "Sickening."

show kenji neutral_ni
with charachange

ke "Yeah, you're better off, dude…"

"Kenji was right, this really is the day of despair. I drink more to avoid having to process what he just said."

ke "Now I am the last sane man in an insane world… when other people realize it, there will be a war, a great war between men and the forces of feminism."

ke "But the problem is that not all men would fight on my side… shit sucks. I could set the bar kinda low, any men are fine. But not the dudes raised by their mom or their sister, that's for sure."

show kenji tsun_ni
with charachange

ke "And nobody into dickgirl porn."

hi "Ha… That situation seems unlikely to me, like it wouldn't happen, like… like it's not very likely to happen."

"The alcohol must be working."

"Regardless, I still feel depressed that I'm up here today."

"I wasn't really looking forward to the festival with the same excitement as the rest of the school, but still."

"It would have been nice to have gone with someone. From up here, it certainly sounded like everyone's having fun. Maybe I am missing out."

"It's just that there was no one I could have gone with."

"Or maybe there was. So many opportunities, looking back on it now, and I must have squandered so many of them."

ke "Damn, this is true despair… The worst part is that sometimes I feel like I have no choices in my life, you know?"

ke "Like I never have a chance to make a decision, shit just happens."

ke "Like it was all preprogrammed. Like fate… or something. Like there is no way I can have a say in what I do."

stop music fadeout 0.2

show kenji rage_ni
with vpunch

ke "Quick, ask me a question!"

hi "Uh…"

ke "Now!"

hi "I can't really…"

show kenji tsun_ni
with charachange

ke "See? This is just another example of it! Damn! Shit! Damn! Do you see? Now, when I'm trying to go against my destiny and take charge of my life, the opportunity isn't even there."

ke "Damn, man, you have failed me. Failed me for the last time. Jerk."

show kenji tsun_ni:
    xpos 0.7 ypos 1.0 xanchor 0.5 yanchor 1.0
    easeout 0.7 ypos 0.9 yanchor 0.5
with Pause(0.8)

show kenji tsun_ni:
    rotate 0
    easeout 0.7 rotate 90 ypos 1.0 yanchor 0.3

with Pause(.7)


play sound sfx_impact
with vpunch

hide kenji
with None

"He slides to his knees and then falls over onto his side, lying on the gravel of the roof."

hi "Hey, are you okay?"

ke "No, I'm not okay, can't you see I'm in despair?"

"He's speaking in a sarcastic tone."

show kenji neutral_ni:
    xpos 0.7 ypos 1.0 xanchor 0.5 yanchor 0.0
    easein 0.5 ypos 1.0 yanchor 0.7
with Pause(0.5)

"Suddenly, Kenji sits up, clumsily pats himself clean, and puts his hand out towards me to reach for the bottle. I put it in his hand."

show kenji tsun_ni at Transform(xpos=0.7, xanchor=0.5, ypos=1.0, yanchor=0.7)
with charachange

ke "What the hell? Damn, you killed almost the entire bottle. See, it's like I have no options in life…"

ke "Is this how it's going to be for the rest of time?"

hi "Well, I'm pretty sure it's not going to be like that for the rest of time."

"Whatever he's talking about. My head is spinning. I get up and lean against the fence, hoping it'll help me focus a little."

show kenji tsun_ni at center
show bg school_roof_ni at center
with charamove

ke "Yeah, I know. We have to fight the power with all we got. It's the only way to live."

play music music_one fadein 6.0

show kenji neutral_ni
with charachange

ke "You're an all right guy."

show kenji happy_ni
with charachange

ke "This brotherly bond is what keeps me going in these dark times."

show kenji neutral_ni
with charachange

ke "We should go trolling women."

hi "Rolling women? What?"

show kenji neutral_close_ni
with characlose

ke "Trolling women. Trolling for women. But we have to do it now, before I lose this alcohol-related courage."

"He's gesturing wildly. Madly, even."

show bg school_roof_ni at Slide(0.5,0.5,0.75,0.75,0.5, time_warp=_ease_time_warp)
show kenji neutral_close_ni at Slide(0.5,0.5,0.3,0.5,0.5, time_warp=_ease_time_warp)
with None

show kenji neutral_ni at Slide(0.5,0.5,0.3,0.5,0.5, time_warp=_ease_time_warp)
show bg school_roof_ni at Slide(0.5,0.5,0.75,0.75,0.5, time_warp=_ease_time_warp)
with charadistant

"I take a step backward."

show kenji neutral_ni at Slide(0.3,0.5,0.5,0.5,0.5, time_warp=_ease_time_warp)
with None

show kenji neutral_close_ni at Slide(0.3,0.5,0.5,0.5,0.5, time_warp=_ease_time_warp)
with characlose

"He takes a step forward."

show kenji happy_close_ni
with charachange

ke "What's the matter with you? Not in the mood for love?"

hi "To be frank… no."

show bg school_roof_ni at Slide(0.75,0.75,1.0,1.0,0.5, time_warp=_ease_time_warp)
show kenji happy_close_ni at Slide(0.5,0.5,0.3,0.5,0.5, time_warp=_ease_time_warp)
with None

show kenji happy_ni at Slide(0.5,0.5,0.3,0.5,0.5)
show bg school_roof_ni at Slide(0.75,0.75,1.0,1.0,0.5, time_warp=_ease_time_warp)
with charadistant

"I take another step backward."

show kenji happy_ni at Slide(0.3,0.5,0.5,0.5,0.5, time_warp=_ease_time_warp)
with None

show kenji happy_close_ni at Slide(0.3,0.5,0.5,0.5,0.5, time_warp=_ease_time_warp)
with characlose

"He takes another step forward."

"He leans in extremely, uncomfortably close."

hi "What the hell, stop leaning in like that, it bothers me."

ke "Leaning in like what? Hey, you shouldn't lean against the fence like that, it's kind of unsafe."

"I try to move away from Kenji, but my balance isn't so good."

"Reeling from the dizziness, I grab at one of the fenceposts, but then feel it give way as soon as I put my weight on it."

"…This isn't good. Though my alcohol-addled brain doesn't seem to be quite capable of registering why."

show black behind bg
with None

show n_vignette:
    xalign 0.5 yalign 0.5 zoom 4.0
    linear 0.2 zoom 1.2
with Pause(0.2)

show n_vignette:
    zoom 1.2
    linear 8.0 zoom 0.001
show kenji happy_close_ni:
    xalign 0.5 yalign 0.5
    linear 8.0 zoom 0.001
show bg school_roof_ni_crop:
    xalign 0.5 yalign 0.5
    linear 8.0 zoom 0.001

"Kenji's face seems to be becoming smaller though, which is a bit of a relief."

"Much smaller, in fact. And rapidly so."

show nightsky rotation
with None

"There seems to be a bit of wind now. Somehow it makes me feel almost weightless."

"I feel dazed, like my mind has gone blank."

hi "I am… falling…?"

"I can see the night sky as I turn over in the air. The bottle floats out of my fingertips and disappears into thin air as I fall."

"I realize that this is the fitting end to a truly, truly bad day."

window hide

stop music fadeout 0.1
play sound sfx_crunchydeath

return


