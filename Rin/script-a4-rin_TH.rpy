label th_R30:

window hide None

scene bg school_scienceroom
with locationchange

window show

play music music_normal fadein 3.0

# "I make it in time for class, though not in time for breakfast."
"ฉันมาทันเข้าเรียน แต่ไม่ทันกินข้าวเช้า"

# "The classroom is bathing in the gentle light of the sun."
"แสงแดดอันอ่อนโยนอาบไล้ทั่วห้องเรียน"

# "This means that it's going to be intolerably hot in the afternoon. For now, though, it's pleasant."
"ซึ่งแปลว่าถ้าบ่ายแล้วอากาศต้องร้อนแทบตายแน่นอน แต่ตอนนี้ยังถือว่ากำลังดีอยู่"

# "I look at Misha and Shizune's animated discussion about whatever, Hanako staring out of the classroom window, Mutou stumbling into the classroom four minutes late and with no recollection of what he's supposed to be teaching today."
"ฉันมองไปทางมิช่าและชิซูเนะที่ขยับมือไม้คุยกันอยู่ มองฮานาโกะที่มองออกไปนอกหน้าต่าง มองมุโต้ที่เดินโซเซเข้า\nห้องเรียนมาช้าไปสี่นาทีโดยไม่รู้เลยว่าวันนี้ตัวเองจะต้องมาสอนอะไร"

# "I could never imagine dropping out of school just like that, even if it's only for a few weeks."
"นึกสภาพตัวเองลาเรียนไปดื้อ ๆ อย่างนั้นไม่ออกเลย ถึงจะแค่ไม่กี่สัปดาห์ก็เถอะ"

# "On the other hand, Rin doesn't seem to have a problem with the idea, or going through with it."
"แต่อีกด้านหนึ่ง รินดูจะไม่ขัดอะไรกับการที่คิดจะลาเรียน หรือจะลาเรียนไปจริง ๆ ก็ไม่ขัด"

# "Then again, somehow I got caught along in her insane isolation, even if we ended up hurting each other."
"แต่ก็นะ ฉันเองก็กลายเป็นว่าได้กลายเป็นส่วนหนึ่งกับการปลีกตัวเกินคนของเธอไปแล้ว ถึงสุดท้ายเราจะทำร้ายกัน\nจนต่างคนต่างเจ็บ"

# "Or did we? Maybe only I got hurt."
"ต่างคนต่างเจ็บ? อาจจะมีแค่ฉันที่เจ็บ"

scene bg school_scienceroom_ss
with shorttimeskip

# "It takes me until late in the afternoon to realize that today is Monday. The art club meets today."
"จนบ่ายแก่ ๆ ฉันก็ถึงนึกได้ว่าวันนี้วันจันทร์ และมีกิจกรรมชมรมศิลปะ"

# "Not just that. Due to the exams, this will be the last art club meeting before summer vacation."
"ไม่ใช่แค่นั้น ยังเป็นกิจกรรมชมรมศิลปะครั้งสุดท้ายก่อนปิดเทอมฤดูร้อนเพราะใกล้สอบแล้ว"


#If seen R16d/R20:
#R20 depends on R16d anyway
label th_R30x:

# "I have no real business going there…"
"ฉันก็ไม่มีธุระอะไรจะต้องไปหรอก…"

# "But I want to talk with the teacher."
"แต่อยากจะคุยกับโนมิยะ"

scene bg school_hallway3
with locationchange

# "So, I end up loitering awkwardly in front of the art room, waiting for the meeting to end."
"ฉันจึงเดินไปเดินมาอยู่หน้าห้องศิลปะรอชมรมเลิก"

# no "That's it for this trimester, everyone!"
no "เทอมนี้ก็เท่านี้นะทุกคน!"

# "His voice is loud enough to be heard through the door and way too enthusiastic for it to be genuine."
"เสียงของเขาดังจนได้ยินผ่านประตู และฟังดูกระตือรือร้นเกินกว่าจะมาจากใจจริง"

# no "The next meeting is after summer vacations, on the Monday of the first week of next term."
no "กิจกรรมชมรมครั้งถัดไปคือจันทร์แรกของเทอมหน้าหลังปิดเทอมฤดูร้อนนะ"

# no "I hope to see everyone there again!"
no "หวังว่าจะได้เจอกับทุกคนอีกนะ!"

# no "Have a nice vacation!"
no "เที่ยวให้สนุก!"

play ambient sfx_crowd_indoors fadein 1.0
stop music fadeout 4.0

show crowd
with charaenter

# "There's a confused answering chorus of voices, and the door to the classroom opens, releasing a flow of students."
"เสียงตอบรับอื้ออึงอู้อี้ตามมา จากนั้นประตูห้องศิลปะก็เปิดออก เหล่านักเรียนต่างกรูกันออกมา"

# "I wait for everyone else to leave, so that I can talk to Nomiya alone. It's almost dinnertime, so I don't have to wait too long."
"ฉันรอให้ทุกคนออกไปก่อนเพื่อที่จะได้คุยกับโนมิยะเป็นการส่วนตัว และยิ่งใกล้เวลามื้อเย็นอย่างนี้แล้วฉันก็ไม่ต้อง\nรอนาน"

stop ambient fadeout 2.0

scene bg school_classroomart_ss
with locationchange


#if not seen R16d/r20:
#R20 depends on R16d anyway
label th_R30y:

# "Without Rin, it feels pretty pointless to go there, but I want to talk with the teacher."
"พอไม่มีรินแล้วก็ไม่รู้จะไปทำไม แต่อยากจะคุยกับโนมิยะสักหน่อย"

scene bg school_classroomart_ss
with locationskip

# "The meeting itself isn't noteworthy, just as my skills with water colors are not worth mentioning."
"ตัวกิจกรรมก็ไม่ได้ดีเด่อะไร ไม่ต่างอะไรกับการที่ทักษะการใช้สีน้ำของฉันนั้นไม่ได้ดีเด่"

# "Nomiya tries to encourage and advise me without sounding too condescending, but he's not doing a very good job of it."
"โนมิยะคอยสนับสนุนและให้คำแนะนำฉันโดยพยายามไม่ให้ฟังดูข่ม แต่ก็ดูจะไม่เป็นผลเท่าไหร่"

# "If nothing else, joining the art club has taught me that I like art. It would be nice if I could actually try and make some art in the art club, though."
"เอาเข้าจริง ๆ พอได้เข้าร่วมชมรมศิลปะแล้วก็รู้ตัวว่าชอบศิลปะ แต่ถ้าได้มีผลงานอะไรเป็นชิ้นเป็นอันอะไรกับชมรมศิลปะ\nสักอย่างก็คงดี"

# "After the fruits of everyone's labor have been piled into a neat stack on the teacher's desk, he clears his throat to give a little speech."
"พอผลงานจากความพยายามของทุกคนกองอยู่บนโต๊ะครูอย่างเป็นระเบียบแล้วโนมิยะก็กระแอมเตรียมกล่าวปิดท้าย"

show nomiya talk at center
with charaenter

# no "That's it for this trimester, everyone!"
no "เทอมนี้ก็เท่านี้นะทุกคน!"

# "His voice is pretty loud and way too enthusiastic for it to be genuine."
"เสียงของเขาค่อนข้างดังและฟังดูกระตือรือร้นเกินกว่าจะมาจากใจจริง"

show nomiya smile
with charachange

# no "The next meeting is after summer vacations, on the Monday of the first week of next term."
no "กิจกรรมชมรมครั้งถัดไปคือจันทร์แรกของเทอมหน้าหลังปิดเทอมฤดูร้อนนะ"

# no "I hope to see everyone there again!"
no "หวังว่าจะได้เจอกับทุกคนอีกนะ!"

show nomiya veryhappy
with charachange

# no "Have a nice vacation!"
no "เที่ยวให้สนุก!"

hide nomiya
with charaexit

stop music fadeout 4.0

# "Everyone wishes him a nice vacation back as they file out the door."
"ทุกคนขานรับคำอวยพรขณะกรูกันออกประตูห้องศิลปะไป"

# "I stay behind, waiting until the two of us are alone. It's almost dinnertime, so I don't have to wait long."
"ฉันรออยู่จนทั้งห้องเหลือแค่ครูกับฉัน และยิ่งใกล้เวลามื้อเย็นอย่างนี้แล้วฉันก็ไม่ต้องรอนาน"

#end split
label th_R30z:

# "Nomiya is looking through the paintings, some of which are actually pretty nice."
"โนมิยะกำลังดูผลงานของทุกคนอยู่ บางชิ้นก็สวยทีเดียว"

# "Rin might outclass everyone else in the art club, but she isn't the only one with talent."
"รินอาจจะเก่งกว่าใครในชมรมนี้ แต่เธอก็ไม่ได้เป็นคนเดียวที่มีพรสวรรค์"

# hi "Excuse me, teacher…"
hi "ครูครับ…"

play music music_happiness fadein 2.0

show nomiya smile at center
with charaenter

# no "Hmm? What is it, Nakai?"
no "หืม มีอะไรเหรอ นากาอิ"

# "He raises his eyebrows questioningly, smiling widely."
"เขาเลิกคิ้วขึ้นด้วยความสงสัยพลางยิ้มกว้าง"

# hi "It's about Rin…"
hi "เรื่องรินน่ะครับ…"

show nomiya frown
with charachange

# no "Oh? Is something wrong with Tezuka?"
no "อ้าว เทซูกะเป็นอะไรเหรอ"

# hi "No, but…"
hi "เปล่าครับ แต่ว่า…"

# "I hesitate for a split second, not certain how to say what I want to say, giving Nomiya enough time to start blabbering by himself."
"เสี้ยววินาทีหนึ่งฉันลังเลนึกไม่ออกว่าจะพูดสิ่งที่อยากพูดยังไงดี จนโนมิยะได้โอกาสพล่ามแทรกขึ้นมาเอง"

show nomiya smile
with charachange

# no "I saw her a few days ago when I was passing by at Sae's gallery."
no "สองสามวันก่อนไปเห็นตอนที่ผ่านหอศิลป์ของซาเอะอยู่"

# no "She said she'd get one or two more paintings done for the exhibition."
no "เห็นบอกว่าเดี๋ยวจะวาดอีกรูปสองรูปไปจัดแสดงในงานนิทรรศการ"

show nomiya talk
with charachange

# no "I was quite pleased, she's a surprisingly hard worker. I'd always thought she was a bit lazy, doing what she wants instead of the assignments…"
no "ฉันดีใจนะ ขยันเกินคาดเลย นึกว่าเป็นคนเฉื่อย ๆ มาตลอด ไม่ยอมทำงานที่สั่งแล้วไปทำอะไรที่อยากทำเอง…"

# "He seems to notice my anxiety and realizes he is digressing, shutting up before finishing the thought."
"คุณครูเห็นฉันที่มีท่าทีร้อนรนจนรู้ตัวว่ากำลังนอกเรื่องอยู่ จึงตัดบทไปก่อนจะได้พูดอะไรต่อจากนั้นให้เสร็จสิ้น"

show nomiya smile
with charachange

# no "Ah, but you had something to talk about. What is it?"
no "อ้อ เธอมีเรื่องจะคุยนี่ เรื่องอะไรเหรอ"

# hi "I don't know… she feels detached from everything, as if she can't think of anything but the exhibition."
hi "ไม่รู้สิครับ… คือรินดูจะตัดขาดจากทุกอย่างจนหัวสมองมีแต่เรื่องงานนิทรรศการแล้วน่ะครับ"

show nomiya frown
with charachange

# no "Well, isn't that good? She is focused on her painting, as she should be."
no "ก็ดีแล้วไม่ใช่เหรอ ได้ตั้งใจกับการวาดรูปเนี่ย"

# hi "Yeah, but this is different. It's like she's obsessed. I went to see her, and…"
hi "ครับ แต่คือมันไม่ใช่อย่างนั้น คราวนี้เหมือนหมกมุ่นเลย คือผมไปหาริน แล้ว…"

show nomiya serious
with charachange

# no "Have you been bothering her?"
no "ไปกวนเทซูกะเขาเหรอ"

# "He cuts in before I finish saying what I meant to say, instantly looking quite irritated."
"คุณครูพูดแทรกก่อนฉันจะทันได้พูดจบพร้อมท่าทีที่ดูหงุดหงิดขึ้นมาทันที"

# hi "No… I don't… think so."
hi "ไม่… ไม่… น่านะครับ"

# hi "I'm just concerned because she's stopped coming to school completely. She feels strange, too."
hi "ผมแค่เป็นห่วงเพราะรินไม่มาโรงเรียนเลย แถมยังดูแปลก ๆ ด้วย"

# hi "Stranger than usual, at the very least."
hi "อย่างน้อย ๆ ก็แปลกกว่าปกติน่ะนะครับ"

show nomiya stern
with charachange

# no "Humbug! This is much more important for her than some lousy math class, or physics, or whatever."
no "เหลวไหล! เรื่องนี้น่ะสำคัญกับตัวเทซูกะยิ่งกว่าคาบคณิต ฟิสิกส์ หรืออะไรบ้า ๆ พวกนั้นอีก"

# no "This is exactly why this school is so flexible, to give every student a chance to fulfill themselves."
no "ก็นี่แหละโรงเรียนนี้ถึงได้ยืดหยุ่นขนาดนี้ ก็เพื่อที่จะให้โอกาสให้นักเรียนทุกคนได้เติมเต็มตามฝันตัวเองน่ะ"

show nomiya serious
with charachange

# no "Tezuka is a painter, so she should paint, no? And have an exhibition. That's what artists do. She should be allowed to concentrate on that, not these other frivolous classes. She should be encouraged."
no "เทซูกะเขาเป็นนักวาด ก็ต้องวาด ถูกไหม แล้วก็จัดงานนิทรรศการ นั่นแหละคือสิ่งที่ศิลปินทำกัน เทซูกะต้องได้จดจ่ออยู่\nกับสิ่งนั้น ต้องคอยสนับสนุนไว้ ไม่ใช่กับวิชาขี้ปะติ๋วอะไรพวกนั้น"

# no "If you think about it, it's really quite obvious."
no "ถ้าเธอลองคิด ๆ ดูมันก็ชัดอยู่นะ"

# "His counterarguments are not very convincing, but I'm having a hard time trying to make any kind of rebuttal."
"คำโต้แย้งของคุณครูฟังไม่ค่อยขึ้นเท่าไหร่ แต่ฉันก็ไม่รู้จะค้านกลับยังไงดี"

# "My grudging silence is interpreted as assent, and Nomiya turns to shuffle the stack of turned-in assignments on his desk like a deck of cards."
"โนมิยะถือเอาว่าความเงียบที่แฝงความหงุดหงิดจากฉันเป็นการยอมรับ คุณครูสับกองงานที่สมาชิกชมรมส่ง\nเหมือนสับไพ่"

show nomiya smile
with charachange

# no "I have to say, while we're talking about Tezuka's exhibition…"
no "แต่พูดถึงงานนิทรรศการของเทซูกะ…"

# no "I'm very excited to see how it turns out."
no "ฉันตื่นเต้นอยากเห็นจริง ๆ ว่าจะออกมาเป็นยังไง"

show nomiya dreamy
with charachange

# no "She's still so young, yet has such wonderful skill, and style!"
no "ทั้งที่อายุยังน้อย แต่มีทักษะและลายเส้นที่สุดยอดขนาดนี้!"

# "He's talking to the air, to relax the mood that got a bit too negative."
"เขาพูดลอย ๆ เพื่อจะคลายบรรยากาศที่ตึงเครียดไปเล็กน้อย"

show nomiya talk
with charachange

# no "I take it that you will be attending?"
no "เธอก็จะไปด้วยใช่มั้ย"

# hi "Yeah, I guess so."
hi "คงงั้นละนะครับ"

show nomiya smile
with charachange

# no "Well, we'll meet there next."
no "โอเค ไว้เจอกันที่นั่นแล้วกัน"

stop music fadeout 3.0

scene bg school_hallway3
with locationchange

# "I take that as my cue to leave. And I do, although I'm not happy about it."
"เป็นสัญญาณว่าฉันต้องไปได้แล้ว และฉันก็ออกมา แม้จะไม่พอใจสักเท่าไหร่ก็ตาม"

# "My message didn't get through, to say the least."
"ที่แน่ ๆ คือสิ่งที่ฉันจะสื่อนั้นส่งไปไม่ถึง"


$ suppress_window_after_timeskip = True

scene black
with dissolve


label th_R31:

window hide None
nvl clear

scene bg school_scienceroom_bw
with locationchange

nvl show dissolve

play music music_night fadein 1.0

# n "\n\n\n\n\n\n\n\n\nThe day after that, all the missed opportunities and things I should have said come crashing down on me. There's nothing left to do afterwards but brood."
n "\n\n\n\n\n\n\n\n\nหนึ่งวันให้หลัง ทั้งโอกาสที่พลาดไป ทั้งสิ่งที่ควรจะพูดแต่ไม่ควรได้พูด เหล่านั้นล้มครืนลงทับตัวฉัน ฉันทำอะไรไม่ได้แล้ว\nนอกจากนึกคร่ำครวญ"

nvl clear
nvl hide dissolve

with shorttimeskip

nvl show dissolve

# n "\n\n\n\n\n\n\n\n\nSecond day. I begin to feel anxious. I start doubting my doubt and it feels stupid, especially since I still can't think about anything else than Rin."
n "\n\n\n\n\n\n\n\n\nสองวันให้หลัง ฉันชักร้อนรน เริ่มนึกกังขาข้อกังขาของตัวเองจนรู้สึกเหมือนเป็นบ้า เพราะฉันคิดถึงอะไรอย่างอื่น\nนอกจากรินไม่ได้แล้ว"

nvl clear
nvl hide dissolve

with shorttimeskip

nvl show dissolve

# n "\n\n\n\n\n\n\n\n\nThird day. Japanese exam, {b}and{/b} world history exam. Great. The thing I hate most about her is that she can make me feel this awful even though I should be focusing on entirely different stuff right now."
n "\n\n\n\n\n\n\n\n\nสามวันให้หลัง มีสอบภาษาญี่ปุ่น{b}และ{/b}ประวัติศาสตร์โลก เยี่ยม ฉันเกลียดรินก็ตรงที่เธอทำให้ฉันรู้สึกแย่ได้\nขนาดนี้ ทั้ง ๆ ที่ตอนนี้ฉันควรจะจดจ่ออยู่กับเรื่องอื่นอยู่แท้ ๆ"

nvl clear
nvl hide dissolve

with shorttimeskip

nvl show dissolve

# n "\n\n\n\n\n\n\n\n\nFourth day. Math exam. We have a math exam. It goes how it goes. I don't care."
n "\n\n\n\n\n\n\n\n\nสี่วันให้หลัง มีสอบคณิตศาสตร์ พวกเราสอบคณิตศาสตร์ เป็นอย่างนั้น ฉันไม่สนหรอก"

nvl clear
nvl hide dissolve

with shorttimeskip

nvl show dissolve

# n "\n\n\n\n\n\n\n\n\nFifth day. Nomiya asks me again if I will attend the exhibition opening. I can't say no to him even though I seriously want to. I just don't want to discuss with him anything Rin-related so it's just better to take the path of least resistance."
n "\n\n\n\n\n\n\n\n\nห้าวันให้หลัง โนมิยะมาถามอีกว่าจะไปงานเปิดตัวนิทรรศการหรือเปล่า ใจอยากจะปฏิเสธเหลือเกินแต่ก็ทำไม่ได้ ฉัน\nไม่อยากคุยเรื่องรินกับโนมิยะให้ยืดยาวอีก ตาม ๆ น้ำไปเลยน่าจะดีกว่า"

nvl clear
nvl hide dissolve

stop music fadeout 2.0

scene bg school_dormhallway
show rin basic_absent at center
with shorttimeskip

window show

# "On the sixth day, the day before the exhibition opening, I find Rin standing in the hallway in front of my room when I return to the dorms after dinner."
"หกวันให้หลัง วันนี้เป็นวันก่อนวันงานเปิดตัวนิทรรศการ พอกินข้าวเย็นเสร็จแล้วกลับมาที่หอก็เห็นรินยืนอยู่ที่\nโถงทางเดินตรงหน้าประตูห้องฉัน"

play music music_rain fadein 6.0 

# hi "What are you doing here?"
hi "มาทำอะไร"

# "My tone is angrier than I intended. I'm a little disappointed that I was unable to restrain myself, but it can't be helped."
"น้ำเสียงฉันฟังดูโกรธกว่าที่ตั้งใจไว้ ฉันผิดหวังกับตัวเองเล็กน้อยที่คุมตัวเองไม่อยู่ แต่ก็ช่วยไม่ได้"

# "Rin just stands there, like she just happened to coincidentally be standing around here where she has no business being. The way she reacts so coolly to everything annoys me now."
"รินยืนอยู่เฉย ๆ เหมือนบังเอิญมายืนอยู่แถวนี้ที่เธอไม่มีธุระจำเป็นอะไรต้องมา ตอนนี้ท่าทีสบาย ๆ ของเธอต่ออะไร ๆ\nทำฉันรำคาญแทนแล้ว"

# "This is not good. It's been six days, and the sight of her has me boiling. She hasn't even opened her mouth yet."
"ไม่ดีแน่ ผ่านมาหกวันแล้ว แค่เห็นรินฉันก็เลือดเดือดขึ้นมา ทั้งที่เธอยังไม่ได้เปิดปากพูดอะไรเลย"

show rin basic_deadpan
with charachange

# rin "Finished painting."
rin "วาดเสร็จแล้ว"

# hi "Shouldn't you be at the gallery? Preparing?"
hi "ไม่ไปอยู่เตรียมอะไรที่หอศิลป์นู่นหรือไง"

show rin basic_awayabsent
with charachange

# rin "They said no."
rin "เขาบอกว่าไม่"

# "I guess the gallery owner does that part then, getting the paintings framed, hung on the walls and whatnot."
"งั้นก็คงเป็นหน้าที่ของเจ้าของหอศิลป์มั้ง อัดรูปใส่กรอบเอย เอารูปแขวนผนังเอย อะไรทั้งหลายแหล่เทือกนั้น"

# hi "So, why are you here?"
hi "แล้วมาทำไม"

show rin basic_deadpannormal
with charachange

# rin "Felt like it."
rin "อยากมา"

# "This same old stupid pattern emerges again; me asking her questions to which she replies with answers that don't answer anything, because it's the only way we can converse."
"สุดท้ายก็เข้าอีหรอบเดิม ที่พอฉันถามแล้วเธอก็จะตอบแบบที่ไม่ได้ตอบอะไรเลย เพราะพวกเราก็สนทนากันได้แต่อย่างนี้"

# "Apart from me listening to her blabbering about whatever, which isn't really a conversation."
"ถ้าไม่นับที่ฉันนั่งฟังเธอพล่ามอะไรไปเรื่อยน่ะนะ ซึ่งก็ไม่นับว่าเป็นบทสนทนาหรอก"

# "Is this a play? Are there some unseen roles that we have unknowingly set ourselves into, dictating the rules of engagement whenever we see each other, inevitably leading to us hurting each other?"
"หรือนี่คือละคร มีตัวบทล่องหนอะไรที่เราเล่นอยู่แบบไม่รู้ตัวหรือเปล่า บทที่ชี้นำว่าเวลาเจอหน้ากันแล้วพวกเราจะต้อง\nปฏิสัมพันธ์กันยังไงจนท้ายที่สุดก็ต้องทำร้ายกันเอง"

# "Her nonchalant answers accompanied by even more nonchalant shrugs leave me none the wiser. I guess I should be happy that the exhibition preparations are complete."
"คำตอบแบบไม่ยี่หระที่มาพร้อมกับการยักไหล่แบบไม่ยี่หระของเธอไม่ได้ทำให้ฉันรู้อะไรขึ้นมาเลย แต่ในเมื่อเตรียม\nงานนิทรรศการเสร็จแล้วฉันก็คงต้องดีใจแหละมั้ง"

play sound sfx_dooropen

scene bg school_dormhisao
with locationchange

# "When I walk into my room, I hear her footsteps following me in."
"พอฉันเดินเข้าห้องมาก็ได้ยินเสียงฝีเท้าของรินตามมาด้วย"

# "I didn't invite her in. I won't ask her to leave."
"ฉันไม่ได้ชวนเธอเข้ามา แต่ก็ไม่ไล่หรอก"

show rin basic_awayabsent:
    center
    alpha 0.0
    ease 0.5 ypos 1.15 alpha 1.0
    parallel:
        ease 0.3 center
    parallel:
        "rin basic_absent" with Dissolve(0.3, alpha=True)
with Pause(0.5)

stop music fadeout 6.0

# "She claims my bed without asking permission, making me wish that I had taken the time to make it before I left in the morning, then stands up again as though she sat on hot coals."
"เธอยึดเตียงฉันไปโดยพลการ รู้งี้น่าจะเก็บที่นอนก่อนออกห้องไปตอนเช้าดีกว่า แล้วเธอก็เด้งตัวลุกขึ้นยืนราวกับว่า\nเมื่อกี้นั่งลงกับถ่านร้อน ๆ"

# "I half-lean against the single corner of my desktop that isn't cluttered with stuff, to rest my legs at least a little bit."
"ฉันยืนหลังชิดกับขอบโต๊ะตัวหนึ่งที่ไม่ได้มีข้าวของวางระเกะระกะเพื่อพักขาสักหน่อย"

show rin basic_awayabsent:
    center
    alpha 1.0
with charachange

# "Rin spends a few moments glancing curiously around my room. It makes me realize that she's never seen it before."
"รินมองไปรอบ ๆ ห้องฉันด้วยความสงสัยอยู่ครู่หนึ่ง เห็นแล้วก็นึกได้ว่าเธอยังไม่เคยเห็นห้องฉันเลย"

# "For a moment, she actually looks like she's concentrating. Trying to get everything. This must be the eye for detail that makes her an artist."
"ครู่หนึ่งเธอดูเหมือนจดจ่ออยู่จริง ๆ เธอจับจ้องทุกอย่าง เป็นศิลปินตาก็คงแหลมคมอย่างนี้สินะ"

show rin basic_absent
with charachange

# "Since the room is small, she quickly runs out of things to look at, but nothing else transpires, allowing the uncomfortable silence to take over the atmosphere."
"เธอมองได้ไม่นานก็ดูจนทั่วเพราะห้องนั้นเล็ก และไม่มีอะไรเกิดขึ้นอีกจนความเงียบอันน่าอึดอัดเข้าปกคลุม"

# "The mood is chilly to say the least, and both of us are on guard, waiting for the other to make the first move."
"เป็นบรรยากาศที่เย็นเยียบ เราทั้งสองคนต่างก็กันท่ารอให้ใครสักคนเปิดก่อน"

# "Of course, Rin could play this game forever. So it has to be me."
"แน่นอนว่ารินอยู่อย่างนี้ได้ตลอดไปอยู่แล้ว ก็ต้องเป็นฉันที่เปิด"

# hi "So…"
hi "แล้ว…"

# "I give up because she'd never try to open conversation, and because it seems that she wants to say something, and I want to get it over with."
"ฉันยอมแพ้เพราะเธอไม่เคยพยายามเปิดบทสนทนาเลย แล้วดูเหมือนเธอก็อยากจะพูดอะไรด้วย ฉันก็อยากให้มัน\nจบ ๆ ไป"

# "Why else would she be here if she didn't want to talk?"
"ถ้าไม่ได้อยากคุยแล้วเธอจะมาทำไม"

# "I don't know what to say myself. I want to be angry, but I can't bring myself to yell at her or anything."
"ฉันหมดคำจะพูด ฉันอยากจะโกรธ แต่ฉันก็ตะคอกหรืออะไรใส่เธอไม่ลง"

# "My voice catches her attention, and she tries to search for words as well, but it seems that she is not entirely certain as to why she's here either."
"เสียงฉันทำให้เธอหันมา เธอเองก็กำลังเลือกเฟ้นคำอยู่เหมือนกัน แต่ดูเหมือนเธอก็ไม่แน่ใจเหมือนกันว่ามาอยู่ที่นี่ทำไม"

show rin basic_absent_close:
    center
    ypos 1.05
    easein 0.5 ypos 1.0
with characlose

# "And so, Rin simply takes a few steps to close the distance between us and rises on the tips of her toes to even out the height difference…"
"และจากนั้นรินก็เดินสองสามก้าวเข้าประชิดฉันก่อนจะเขย่งเท้าเพื่อให้ส่วนสูงพอดีกัน…"

window hide

show rin basic_lucid_superclose at center
with charachange

# centered "“It was a bad idea.”"
centered "“เป็นอะไรที่ไม่ดี”"

# centered "“Maybe you should forget about it, and I will too.”"
centered "“หรือนายจะลืมไปเลยก็ได้ ฉันก็จะลืมด้วย”"

window show

# "It's a reflex, and almost as an afterthought, the words “no,” “yes” and “maybe” simultaneously surface inside my mind."
"เป็นปฏิกิริยาตอบสนองอัตโนมัติ ทั้งคำว่า “ไม่” “ใช่” และ “มั้งนะ” ต่างผุดขึ้นในหัวคล้ายนึกทิ้งทวน"

# "My hand is between her lips and mine, a wall that I raised to guard against… something."
"มือฉันคั่นกลางระหว่างริมฝีปากเธอและฉัน เป็นกำแพงที่ฉันตั้งขึ้นมาป้องกัน… บางอย่าง"

# "Her breath feels warm against my fingers. The scent of her skin lingers about, the mysterious indescribable sensation that captures me and draws my eyes deep into hers."
"ลมหายใจอุ่น ๆ เธอรดนิ้วฉัน กลิ่นจากผิวกายเธอลอยอบอวล ความรู้สึกลึกลับที่บรรยายไม่ถูกสะกดฉันและดึงดูดให้ฉัน\nมองเข้าไปในตาเธอ"

show rin basic_surprised_close
with charachange

play music music_moonlight fadein 0.5

# "The look in her eyes is surprised, quizzical as to why the impertinent hand prevented her advances."
"แววตาเธอดูประหลาดใจและสงสัยว่าทำไมมือที่ไม่รู้จักกาลเทศะนี้ถึงได้ขัดขวางเธอ"

# "Her eyes are really big and glistening with moisture, and staring right into my own with a soft gaze that I'm having a hard time to match."
"นัยน์ตาเธอกลมโตและฉ่ำวาว เธอจ้องตาฉันด้วยสายตาอ่อนโยนที่ฉันไม่กล้าสบตาด้วยตรง ๆ"

# "Rin's half-open mouth makes her look even more confused, although the sensual way her lips are arching is signaling something completely different."
"ปากรินที่เผยอยิ่งทำให้เธอดูสับสน ถึงด้วยรูปปากที่ยั่วเย้านั้นจะทำให้รู้ว่าเจตนาที่แท้จริงคืออะไรก็ตาม"

show rin basic_upset_close
with charachange

# rin "Please."
rin "ขอร้องละ"

show rin negative_angry_close
with charachange

# rin "I need you."
rin "ฉันต้องการนาย"

# "The words come from her throat as a coarse whisper meant only for me, bypassing her tongue and teeth without giving them any chance to interrupt."
"คำพูดที่ส่งมาด้วยเสียงกระซิบแผ่วอันแหบแห้งนั้นผ่านออกปากเธอมาโดยที่ลิ้นและฟันของเธอไม่ทันได้ยับยั้ง"

show rin negative_angry
with Dissolve(0.15)
with vpunch

# "They sober me in an instant, and I clumsily flinch back to get a little bit of distance between us, painfully scraping against my desk in the process."
"คำพูดเหล่านั้นทำฉันสร่างทันที ฉันผงะถอยด้วยท่าทางเก้ ๆ กัง ๆ เพื่อให้มีระยะห่างขึ้นมาเล็กน้อย ตัวฉันก็ครูดเข้า\nกับโต๊ะจนได้เจ็บอีกต่างหาก"

# "Maybe it's her choice of words, maybe the way she says it, but something in it puts me off."
"ไม่รู้ทำไม—อาจจะเพราะคำพูดที่เธอเลือกมา อาจจะเพราะน้ำเสียงเธอ—แต่พอได้ฟังแล้วก็รู้สึกไม่ดี"

# "Something is wrong, something is terribly wrong again."
"มีบางอย่างผิดปกติ มีบางอย่างผิดปกติไปโดยมหันต์อีกแล้ว"

# hi "Need me for what?"
hi "ต้องการฉันไปทำไม"

# "All the unpleasant feelings emerge again, and I feel my heartbeat suddenly increasing at least tenfold."
"ความรู้สึกไม่ดีทั้งหลายแหล่ผุดขึ้นในตัวอีกครั้ง อยู่ ๆ ก็รู้สึกเหมือนใจเต้นเร็วขึ้นสักสิบเท่าได้"

show rin basic_absent
with charachange

# "Rin's eyes go out of focus and back again as her body relaxes from its tensed state, and she stands upright again."
"รินเลิกเพ่งสายตาแล้วกลับมาเพ่งใหม่ จากที่เธอตัวเกร็งอยู่ก็คลายลง แล้วเธอก็ยืนตัวตรงอีกครั้ง"

show rin basic_deadpanupset
with charachange

# rin "I don't think I was thinking about anything. Why do you draw patterns in that dust on your night table?"
rin "ฉันไม่คิดว่าฉันคิดอะไรอยู่ ทำไมนายถึงวาดลายกับฝุ่นบนโต๊ะหัวเตียงนั้นล่ะ"

show rin basic_awayabsent
with charachange

# rin "There is a word for that kind of thing but I can't remember…"
rin "มีคำเรียกนะ แต่ฉันจำไม่ได้…"

# "Her remark almost throws me off track and I glance over her shoulder at the small table next to my bed, but I can't see anything from this distance."
"คำพูดของเธอทำให้ฉันเบนความสนใจแล้วมองข้ามไหล่เธอไปที่โต๊ะตัวเล็ก ๆ ข้างเตียงฉัน แต่ไม่เห็นอะไรเลยเพราะอยู่ไกลเกิน"

# "So she needs me for nothing specific?"
"ก็คือไม่ได้ต้องการฉันเพื่ออะไรเป็นพิเศษ?"

# "Just happened to come by because she thought I'd be glad to see her after she shut me out, no complaints accepted, for a week."
"แค่แวะมาเพราะคิดว่าฉันคงดีใจที่ฉันได้เจอเธอหลังเธอปัดฉันทิ้งไปโดยไม่รับข้ออุทธรณ์ใด ๆ เป็นเวลาหนึ่งสัปดาห์"

# "Completely altruistic motives?"
"ทำไปโดยไม่หวังผลตอบแทนเลย?"

# "Felt like it?"
"อยากมา?"

# hi "Bullshit. I can answer myself."
hi "ตอแหล ฉันตอบเองได้"

# hi "To play mind games with whenever you want, to kiss whenever you want, to ignore whenever you want, to fulfill your whims whenever you want?"
hi "ต้องการฉันมาปั่นหัวเมื่อไหร่ก็ได้ตามใจอยาก จูบเมื่อไหร่ก็ได้ตามใจอยาก เมินเมื่อไหร่ก็ได้ตามใจอยาก ทำอะไรเมื่อไหร่ก็ได้\nตามใจอยาก?"

# hi "Is that it? What you need me for?"
hi "แค่นั้นใช่มั้ย ที่เธอต้องการฉันน่ะ"

# "My voice is sounding very angry again, even to myself."
"น้ำเสียงฉันโกรธจัดขึ้นมาอีกครั้งจนแม้แต่ฉันยังรู้สึกได้"

# extend " Good."
extend " เยี่ยม"

show rin basic_absent
with charachange

# "Rin too finally catches the mood and her curious expression changes instantly to something more uncharacteristic."
"รินเองก็สัมผัสได้ถึงบรรยากาศแล้ว สีหน้าของเธอเปลี่ยนจากความสงสัยเป็นอีกสีหน้าที่ดูไม่สมเป็นตัวเธอ"

show rin negative_sad
with charachange

# rin "No—"
rin "ไม่—"

# "She leaves it at that, her eyes restlessly wandering around, searching the room as if the words she tries to find were written in the tapestries of my walls."
"เธอพูดแค่นั้น ตาเธอล่อกแล่กมองไปรอบ ๆ ห้องราวกับว่าคำพูดที่เธอต้องการนั้นเขียนอยู่บนภาพแขวนผนังในห้องนี้"

# hi "Then what?"
hi "แล้วมันยังไง"

show rin negative_confused
with charachange

stop music fadeout 2.0

# rin "I needed to paint"
rin "ฉันต้องวาดรูป"

# "Paint."
"วาด"

# "Of course. That's what artists do."
"แหงอยู่แล้ว เป็นศิลปินก็ต้องวาด"

# "The words reverberate through my being, beating in my blood over the piercing whistle of my anger."
"คำพูดเหล่านั้นสะท้อนก้องไปทั่วร่างฉัน ดังอยู่ในเลือดควบคู่ไปกับความโกรธที่พุ่งพล่าน"

play music music_tragic fadein 2.0

# hi "Don't give me that, Rin! I am not some damn muse of yours, free to be abused for the sake of painting!"
hi "พอได้แล้ว ริน! ฉันไม่ใช่เทพประทานแรงบันดาลใจที่เธอจะย่ำยีเพื่อเอาไปวาดรูปยังไงก็ได้นะ!"

# hi "I am not some medium for whatever you aspire to, I am me!"
hi "ฉันไม่ใช่ทางผ่านที่เธอจะใช้ข้ามไปหาสิ่งที่เธอฝันนะ ฉันก็คือฉัน!"

# hi "So what if I don't know anything about my future?"
hi "ฉันไม่รู้อนาคตของตัวเองแล้วมันทำไม?"

# hi "There's things I want, and things I care about! Even I can dream of things other than nightmares!"
hi "ฉันก็มีสิ่งที่ฉันอยาก ฉันก็มีสิ่งที่ฉันสนใจ! ฉันก็มีฝันอย่างอื่นที่ไม่ใช่ฝันร้ายด้วยเหมือนกัน!"

# "I'm yelling, but I'm way past the point of caring about things like that."
"ฉันขึ้นเสียง แต่ฉันก็เลยจุดที่จะต้องสนใจอะไรอย่างนั้นมาไกลแล้ว"

show rin negative_sad
with charachange

# "Rin looks down at her toes and wiggles them a little melancholically while she takes in my outburst without saying anything to defend herself."
"รินก้มมองพื้นแล้วงอนิ้วเท้าตัวเองอย่างเศร้า ๆ ขณะที่เธอคอยฟังฉันระเบิดอารมณ์โดยไม่พูดอะไรโต้ตอบเลย"

# "Only after I have finished does she try to respond somehow."
"กระทั่งฉันพูดจบเธอก็ถึงพอจะตอบอะไรบ้าง"

show rin basic_sad
with charachange

# rin "I can't do anything else. Or I can do all sorts of things, but I… can't… do."
rin "ฉันทำอย่างอื่นไม่ได้ ไม่สิ ฉันทำได้หมดเลย แต่ฉัน… ทำ… ไม่ได้"

show rin basic_upset
with charachange

# rin "It's the only thing I sort of do properly. Most of the time."
rin "เป็นอย่างเดียวที่ฉันทำได้ดี ส่วนมาก"

# "I understand completely. Art first, everything else second, or thousandth."
"ฉันเข้าใจดี ศิลปะมาเป็นอันดับแรก อย่างอื่นอันดับที่สอง ไม่ก็อันดับที่พันนู่นแหละ"

# hi "What about me? Am I nothing? When I was interested in art, did that make you feel like I was a little interesting, for a little while?"
hi "แล้วฉันล่ะ ฉันไม่มีค่าเลย? ตอนที่ฉันสนใจศิลปะน่ะ เธอเคยรู้สึกว่าฉันน่าสนใจขึ้นมาสักหน่อยหนึ่ง สักเวลาหนึ่งมั้ย"

# hi "Tell me. I really want to know. Did you ever think about my perspective, or is it just all you?"
hi "บอกมาสิ ฉันอยากรู้จริง ๆ เธอเคยคิดถึงใจฉันบ้างมั้ย หรือคิดถึงแค่ใจตัวเอง?"

# "The words rise like bile in my throat."
"คำพูดเหล่านั้นทิ้งรสสัมผัสอันขมเฝื่อน"

show rin basic_surprised
with charachange

# "She looks alarmed. And also completely uncomprehending, as if she just doesn't understand what I'm angry about."
"รินดูตื่นตกใจและสับสนหนัก เหมือนไม่เข้าใจว่าฉันโกรธอะไร"

# "I can't believe even she could be so stupid."
"จะโง่ได้ถึงขนาดนี้เลยเหรอ"

show rin negative_sad
with charachange

# rin "I didn't want to—"
rin "ฉันไม่อยาก—"

# "This time it's Rin who interrupts herself in midsentence."
"คราวนี้เป็นเธอเองที่ตัดบทตัวเอง"

show rin basic_upset
with charachange

# rin "Don't you understand? I can't."
rin "นายไม่เข้าใจเหรอ ฉันทำไม่ได้"

# hi "Can't what?"
hi "ทำอะไรไม่ได้?"

# "She doesn't get a word out of her mouth."
"แล้วเธอก็ไม่พูดอะไรสักคำ"

# hi "You never explain yourself! How am I supposed to understand anything if you never say anything?"
hi "เธอไม่เคยอธิบายอะไรเลย! ก็ในเมื่อเธอไม่พูดอะไรเลยแล้วฉันจะไปเข้าใจอะไรด้วยหา"

# hi "Why don't you ever talk?"
hi "ทำไมเธอถึงไม่คุยเลย"

# hi "Say something!"
hi "พูดอะไรหน่อยสิ!"

# "But she doesn't."
"แต่เธอก็ไม่พูด"

# "Venting my anger at her feels satisfying. It feels wrong to take so much satisfaction in it, but I can't stop."
"พอได้ระบายความโกรธแล้วก็โล่ง รู้สึกผิดที่ทำแล้วโล่งขนาดนี้ แต่ฉันห้ามตัวเองไว้ไม่อยู่แล้ว"

show rin negative_annoyed
with charachange

# "Not wanting to face my anger head-on, Rin turns around to steadfastly look out of my window even though there is nothing to look at."
"รินหันไปมองทางหน้าต่างด้วยไม่อยากจะเผชิญหน้ากับความโกรธฉันตรง ๆ แม้นอกหน้าต่างนั้นจะไม่มีอะไรให้มอง\nก็ตาม"

# "The worst of my ire gone, I shut up as I can't be bothered to keep on yelling at the back of her head, so silence finally returns."
"ความโกรธขีดสุดของฉันระเบิดหายไปแล้ว ฉันเงียบปากไปเพราะไม่มีอารมณ์จะตะคอกใส่ท้ายทอยเธอ ความเงียบจึง\nกลับมาในที่สุด"

# "I try to discern some hints of her reaction through my adrenaline-distorted vision."
"ฉันเพ่งสายตาที่พร่าเลือนเพราะอะดรีนาลินเพื่อดูว่าเธอทำสีหน้ายังไงอยู่"

# "My feedback was not the best kind, but I hope Rin got the clue that she just can't ignore everything else whenever she feels like it."
"สิ่งที่ฉันพูดออกไปก็ไม่ได้ดีหรอก แต่ก็หวังว่ารินจะรู้ตัวบ้างว่าเธอนึกจะเมินอะไรตามใจไม่ได้"

# "I'd hate it if she didn't. She never ever listens to anything, she's so unaffected by the world around her."
"ถ้าไม่รู้ตัวก็พอที เธอไม่เคยฟังอะไรเลย สิ่งรอบตัวไม่อาจทำให้เธอสะทกสะท้านได้"

# "Not this time, it seems."
"แต่ดูเหมือนว่าจะไม่ใช่กับครั้งนี้"

# "Her body is shaking like from holding back tears, but I already know that Rin is not crying."
"ตัวเธอสั่นคล้ายว่ากำลังกลั้นน้ำตา แต่ฉันรู้แล้วว่ารินไม่ได้ร้องไห้"

# "Her indifference made me so furious. Now that it's gone, I'm at a loss. I wonder…"
"ท่าทีที่ไม่สนอะไรของเธอทำฉันเดือดดาล แต่ตอนนี้ท่าทีที่ว่านั้นไม่มีแล้ว ฉันสับสน นี่ฉัน…"

# "Did I go too far?"
"ทำเกินไปหรือเปล่่า"

# hi "Look, I—"
hi "คือ ฉัน—"

show rin negative_angry
with charachange

# rin "Go away."
rin "ไปเลย"

# rin "Go away, Hisao."
rin "ไปเลย ฮิซาโอะ"

# "Her voice is tiny and tired as she says this, but I hear the words clear as day."
"เธอพูดด้วยเสียงอันแผ่วเบาและอ่อนล้า แต่คำพูดเหล่านั้นชัดแจ้งแก่ฉันยิ่งกว่าอะไร"

"…"

# "What is there to say any more?"
"มีอะไรให้พูดอีกล่ะ"

# hi "This is my room."
hi "นี่ห้องฉัน"

# "The blunt, hollow remark is a fitting conclusion for this unpleasant discussion that became an even more unpleasant and very one-sided yelling match."
"คำพูดห้วน ๆ และเปล่ากลวงนั้นช่างเป็นจุดจบอันเหมาะเจาะกับบทสนทนาอันไม่น่าอภิรมย์นี้ที่นานเข้าก็ยิ่งไม่น่าอภิรมย์\nไปใหญ่จนกลายเป็นการแข่งตะคอกที่มีฉันแหวอยู่ฝ่ายเดียว"

show rin basic_lucid
with charachange

# "After a moment of collecting herself Rin just gives up, I can see it from the way she slumps her shoulders, and walks out."
"รินตั้งสติอยู่พักหนึ่งก่อนจะหย่อนไหล่ลงยอมแพ้แล้วเดินออกไป"

hide rin
with charaexit

# "Even though she deliberately looks to the other direction, I can see how she's biting the corner of her lip so hard it might start bleeding if she won't stop."
"ถึงเธอจะจงใจมองทางอื่นอยู่ แต่ฉันก็เห็นว่าเธอกัดริมฝีปากแน่นชนิดที่ว่าถ้ายังกัดเรื่อย ๆ แล้วปากอาจจะแตกได้"

# "As she makes her exit, I realize that she left the door open when she came in and my yelling must've echoed around the dorm hallways."
"ระหว่างที่เธอเดินออกไปฉันก็เห็นว่าตอนเธอเข้ามาเธอไม่ได้ปิดประตู ที่ฉันตะคอกไปคงดังลั่นไปทั่วโถงทางเดินแน่ ๆ"

# "I sigh. Now that she's gone, I am left alone with my guilt."
"ฉันถอนหายใจ พอเธอไม่อยู่แล้วก็เหลือแค่ฉันที่ต้องอยู่กับความรู้สึกผิดของตัวเอง"

# "As the thumping in my chest slowly subdues, anxiety replaces it."
"จังหวะหัวใจที่ค่อย ๆ เต้นช้าลงถูกแทนที่ด้วยความกังวลใจ"

# "Somehow, I feel that none of this would've ever happened if not for me."
"ไม่รู้ทำไม แต่รู้สึกว่าถ้าไม่มีฉันแล้วเรื่องก็คงไม่เป็นอย่างนี้"

# "No matter how infuriating, unbearable and outrageous Rin is, she is not the Rin I thought I knew."
"ไม่ว่ารินจะทำตัวน่าโมโหจนเกินทนหรือหลุดโลกแค่ไหน เธอก็ไม่ใช่รินที่ฉันคิดว่าฉันเคยรู้จัก"

# "The Rin that I expected Rin to be."
"รินที่ฉันคาดหวังว่ารินจะเป็น"

"…"

# "Was it me who caused all this by talking Rin into taking her chances with the exhibition?"
"ทั้งหมดนี้เป็นเพราะฉันที่เกลี้ยกล่อมให้เธอรับโอกาสที่จะได้จัดงานนิทรรศการนี้หรือเปล่า"

# "Am I directly responsible for Rin becoming like she has been for the past weeks?"
"เป็นเพราะฉันเองหรือเปล่าที่สองสามสัปดาห์ที่ผ่านมารินทำตัวอย่างนี้?"

# "I can't think of any other explanation for her weird behavior than the exhibition and all the things that came along with it."
"ฉันนึกเหตุผลอื่นที่เธอทำตัวแปลก ๆ ไม่ออกแล้วนอกจากเรื่องงานนิทรรศการพวกนี้"

# "Maybe it was the only way that could have brought us closer, but all it did was separate us further away from each other, and now beyond the reach of either of us."
"อาจจะเป็นทางเดียวที่ทำให้เราได้ใกล้ชิดกัน แต่สุดท้ายกลับทำพวกเราออกห่างกัน จนกระทั่งตอนนี้ระยะนั้นไกล\nเกินกว่าที่เราสองคนจะเอื้อมถึงกันแล้ว"

play sound sfx_impact2
with vpunch

# "I bang my head hard against the wall."
"ฉันโขกหัวกับกำแพงแรง ๆ"

play sound sfx_impact2
with vpunch

stop music fadeout 4.0

# "Twice, to make sure it hurts."
"สองครั้ง ให้แน่ใจว่าเจ็บจริง ๆ"

scene black
with dissolve



label th_R32:

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_traffic fadein 0.5

scene bg gallery_ext
with locationchange

# "A headache is relentlessly thumping against the back of my head as I push open the door to the 22nd Corner."
"ฉันเปิดประตูเข้าหอศิลป์ซอย 22 ไปทั้งที่ในหัวยังปวดตุบ ๆ ไม่หยุด"

# "Apart from that, I'm perfectly calm."
"แต่ถ้าไม่นับเรื่องปวดหัว ฉันก็สบายดี"

$ renpy.music.set_volume(0.1, 1.0, channel="ambient")

window hide
nvl clear
nvl show dissolve

# n "\n\nAfter venting on Rin all that anger that I had bottled inside, it felt like a great weight had been lifted from my heart."
n "\n\nหลังจากที่ระบายความโกรธที่อัดอั้นใส่รินไปจนหมดแล้วก็โล่งเหมือนยกภูเขาออกจากอก"

# n "The tension that had grasped my mind for the past few weeks faded away without leaving even a shadow behind."
n "ความตึงเครียดที่เกาะกินจิตใจมาสองสามสัปดาห์หายไปอย่างไร้ร่องรอย"

# n "In this nearly Zen-like state of enlightenment I realized that perhaps it was a bad idea to yell at her like that."
n "พอปลอดโปร่งจนสงบเช่นนี้แล้วฉันก็รู้สึกผิดที่ตะคอกใส่รินไปอย่างนั้น"

# n "\nI really meant it, but what good does blowing up like that do? Nothing."
n "\nสิ่งที่ฉันพูดนั้นก็จริงอยู่ แต่ไประเบิดใส่รินอย่างนั้นแล้วจะได้อะไรขึ้นมา ไม่มี"

# n "I am not like that. I don't normally yell at people. I don't know why I did yesterday."
n "ฉันไม่ใช่คนอย่างนั้น ปกติฉันไม่ได้ตะคอกใส่ใคร ไม่รู้ทำไมเมื่อวานถึงทำไป"

# n "So I keep feeling really guilty about it and wanting to take my words back."
n "ฉันจึงได้แต่รู้สึกผิดจนอยากจะถอนคำพูด"

# n "\n\nRin is probably upset too. Even more than my own behavior, her reaction shocked me."
n "\n\nรินเองก็คงอารมณ์ไม่ดี ฉันตกใจกับปฏิกิริยาของเธอมากกว่าพฤติกรรมของตัวฉันเองเสียอีก"

nvl clear

# n "\nI've always thought of her as unchanging, detached from her surroundings so that seeing my yelling get her so upset felt… out of place."
n "\nฉันคิดมาเสมอว่าเธอเป็นคนเฉย ๆ ไม่อะไรกับโลกโดยรอบ พอได้เห็นที่เธออารมณ์ไม่ดีตอนโดนฉันตะคอกใส่แล้วจึง\nทำให้รู้สึก… แปลก ๆ"

# n "\nI wonder if she understands how I feel?"
n "\nเธอจะเข้าใจความรู้สึกฉันไหมนะ"

# n "In Rin's world everything seems to be so absolute and subjective… absolutely subjective, as if she was completely unable to see things from other points of view than her own."
n "ฉันคิดว่ารินคงจะมองโลกแบบหนึ่งด้าน… ตายตัว ราวกับว่าเธอจะมองอะไร ๆ จากมุมอื่น ๆ นอกจากมุมของตัวเอง\nไม่ได้เลย"

# n "But ultimately, is anyone able to do it? Maybe objectivity and altruism are just illusions for people who like to think of themselves as compassionate."
n "แต่เอาเข้าจริง ๆ แล้ว จะมีใครที่ทำอย่างนั้นได้ด้วยเหรอ บางทีการมองอะไรให้เป็นกลางกับการทำอะไรโดยไม่หวังผล\nก็คงเป็นเพียงภาพฝันมายาสำหรับคนที่คิดว่าตัวเองเป็นพวกเข้าอกเข้าใจคนอื่น"

# n "Just like art is an illusion for people who think reality is merely a veil for something greater."
n "เหมือนอย่างที่ศิลปะคือภาพฝันเพื่อผู้คนที่คิดว่าความเป็นจริงเป็นเพียงเปลือกห่อสิ่งที่ดีกว่า"

# n "Even when you stop thinking that the world revolves around you or start thinking outside of the mythical box, you are just inside another, bigger box that you can't escape."
n "ต่อให้จะเลิกคิดว่าโลกหมุนรอบตัวเองหรือคิดอะไรนอกกล่องในตำนานแล้ว ก็จะยังได้มาอยู่ในกล่องใหญ่กว่าอีกกล่องที่\nหนีออกไปไม่ได้แทน"

# n "\nMaybe that, ultimately, makes her like the rest of us."
n "\nบางที หากเป็นอย่างนั้นแล้ว ท้ายที่สุด เธอก็คงไม่ต่างจากเราทุกคน"

stop ambient fadeout 1.0

nvl clear
nvl hide dissolve

play sound sfx_storebell
$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 0.5

scene bg gallery_int
show crowd
with locationchange

window show

play music music_ease fadein 3.0

# "I step through the door to find a gallery full of illusioned people."
"พอเดินผ่านประตูเข้ามาก็พบกับผู้คนที่ถูกภาพฝันลวงมากมาย"

# "Despite Sae's remarks during my earlier visits I always thought it was very spacious, but now when it's crowded like this it looks positively cramped."
"ถึงซาเอะจะเคยบอกตอนที่ฉันมาครั้งแรกแล้วว่าหอศิลป์นั้นเล็ก แต่ฉันก็รู้สึกว่าภายในนั้นกว้างมาตลอด แต่พอตอนนี้\nมีคนแน่นขนัดแล้วก็ดูแคบไปถนัดตา"

show sae smile at center behind crowd
with charaenter

# "I immediately notice Sae standing in the middle of a lively discussion, busily chattering with some old gentlemen."
"ฉันเห็นซาเอะที่ยืนเด่นอยู่กลางวงสนทนา เธอกำลังคุยอย่างออกรสอยู่กับสุภาพบุรุษที่ดูมีอายุคนหนึ่ง"

# "She's actually pretty tall and kind of cool-looking, so she stands out in the crowd."
"ทั้งส่วนสูงและรูปลักษณ์ที่ดูดีนั้นทำให้เธอโดดเด่นเห็นชัดท่ามกลางกลุ่มคน"

# "There are a few dozen wine glasses laid on the tables along the back wall, filled with burgundy liquid. A vast majority of the guests are sipping from their own glasses."
"โต๊ะที่วางอยู่ตามกำแพงนั้นมีแก้วไวน์วางอยู่สองสามโหล ภายในมีของเหลวสีแดงเลือดหมูบรรจุอยู่ แขกเหรื่อส่วนใหญ่\nต่างก็จิบจากแก้วของตัวเองกัน"

# "The socialites and art connoisseurs are mingling happily, exchanging mild opinions about Rin's art which seems to be a secondary object of interest for most."
"เหล่าคนเข้าสังคมและผู้เชี่ยวชาญศิลปะต่างเสวนากันอย่างมีความสุขพลางพูดถึงงานของรินบ้าง ซึ่งตัวงานศิลปะนั้น\nดูจะเป็นวัตถุประสงค์รองสำหรับคนส่วนใหญ่"

# "I feel distanced, excluded from the other people here."
"ฉันรู้สึกแปลกแยกและแตกต่างไปจากคนอื่น ๆ ที่อยู่ที่นี่"

# "I can't claim even at a stretch to be a social chameleon, so this situation is quite unnerving."
"ฉันไม่ใช่คนที่เข้าสังคมเก่งอะไรเลย สถานการณ์เช่นนี้ทำให้ฉันกระอักกระอ่วนทีเดียว"

# "Since I don't blend into the crowd at all, I just fake that I do, trying to look as cool and smooth as I can."
"และในเมื่อฉันไม่ได้เข้าพวกกับกลุ่มคนในนี้ ฉันจึงแสร้งทำตัวเองให้ดูดีและเนียนที่สุดเท่าที่จะทำได้"

# "I wonder how Rin is handling all this. If it was me, I would be quite freaked out."
"รินจะรับมือยังไงนะ เป็นฉันคงตื่นตระหนกน่าดู"

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

scene bg gallery_exhibition
show crowd
with locationchange

# "Throwing the anxiety aside, I try to carefully navigate through the crowd, stealing peeks at the framed paintings now hanging on the walls."
"ฉันปัดความกังวลทิ้งไปแล้วค่อย ๆ เดินฝ่าฝูงชนไปอย่างระมัดระวังพลางเหลือบมองภาพวาดที่อัดกรอบแขวนอยู่บนผนัง"

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

scene rin_exhibition_paintings
with locationchange

# "Rin's exhibition takes about half of the gallery's wall space. Some paintings are less familiar than others, but I recognize most of them."
"งานนิทรรศการของรินกินที่ไปประมาณครึ่งหนึ่งของผนังหอศิลป์ บางภาพก็ดูไม่ค่อยคุ้นตาเท่าภาพอื่น แต่ฉัน\nพอจะจำภาพส่วนใหญ่ได้"

# "Some I've seen being created at the club meetings after all, or remember from the time when Rin was choosing her portfolio."
"ยังไงเสีย บางรูปฉันก็เคยเห็นมาแล้วที่ชมรมศิลปะ หรือไม่ก็เคยเห็นมาตอนที่รินเลือกภาพใส่แฟ้มผลงาน"

# "I note that a couple of the unfinished paintings are framed and on the wall as well. Maybe that's what they call coincidental art?"
"ฉันเห็นว่าบนผนังนั้นมีอยู่สองรูปที่ยังวาดไม่เสร็จที่แขวนไว้ด้วย นี่หรือเปล่านะคือศิลปะแบบไม่ได้ตั้งใจ"

# "Even Rin's failures, if you can call them that, became exhibits of her skill. Quite paradoxical."
"แม้แต่ความล้มเหลวของริน—ถ้านับว่าล้มเหลวได้น่ะนะ—ยังแสดงถึงฝีมือของเธอ ย้อนแย้งดี"

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

scene bg gallery_exhibition
show crowd
with locationchange

# "She herself is nowhere to be seen, which is strange because even though it's crowded, the gallery {b}is{/b} pretty small."
"ส่วนเจ้าตัวนั้นฉันไม่เห็น ซึ่งแปลก ถึงคนจะเยอะ แต่หอศิลป์{b}นั้น{/b}ค่อนข้างเล็ก"

# "It's fine, sort of. I don't know how to face her after yesterday. Maybe I shouldn't have even come."
"ไม่เป็นไร แหละ พอมีเรื่องเมื่อวานแล้วก็ไม่รู้จะไปสู้หน้ารินยังไง ที่จริงฉันไม่น่ามาด้วยซ้ำ"

# "But I promised various people, Rin included, that I would, so…"
"แต่ฉันก็สัญญาไว้กับหลายคน—รวมถึงริน—แล้วว่าจะมา เพราะงั้น…"

# "Damn, it sounds like I do the things I do because some kind of instinctual properness compels me to, not because it would be sensible (or not)."
"ให้ตาย ฟังแล้วก็เหมือนว่าฉันทำอะไรเพราะสัญชาตญาณบอกว่าจำเป็นต้องทำ ไม่ใช่ทำเพราะว่า(ไม่)มีเหตุผลที่จะ\nต้องทำ"

scene bg gallery_int at right
show sae smile at center
show crowd at right
with locationchange

# "I sneak closer to Sae to wait for a lull in the conversation so I can chat her up too."
"ฉันเข้าไปใกล้ ๆ ซาเอะแล้วรอสบจังหวะเพื่อที่จะได้คุยกับเธอด้วย"

# "Even though her voice is almost completely buried under the general background noise, I hear bits and pieces of her talking about Rin."
"ถึงแม้เสียงเธอจะโดนเสียงที่คนอื่น ๆ คุยกันกลบจนเกือบหมด ฉันก็ยังพอจะได้ยินที่เธอพูดถึงรินบ้าง"

# sa "Yes, she is a high schooler at a local school… even though she's graduating next year I'm sure various art schools would be interested in…"
sa "ใช่ เธอเรียนอยู่ที่โรงเรียนมัธยมท้องถิ่นน่ะ… ถึงปีหน้าจะจบแล้ว แต่ฉันมั่นใจว่าโรงเรียนศิลปะหลายที่คงสนใจ…"

# sa "…I thought it'd be interesting to have an exhibition of someone who is still in early stages of development…"
sa "…ฉันคิดว่าการที่ได้จัดงานนิทรรศการให้คนที่กำลังเริ่มพัฒนาตัวเองอยู่ก็คงน่าสนใจดี…"

# "It's so strange, it's like Rin is some kind of mini-celebrity even though this is nothing but a small exhibition opening at a small art gallery of a small town."
"แปลก เหมือนรินได้กลายเป็นคนดังขนาดย่อม ๆ ไปแล้ว ถึงแม้จะเป็นแค่งานเปิดตัวนิทรรศการเล็ก ๆ ในหอศิลป์\nเล็ก ๆ ของเมืองเล็ก ๆ แบบนี้"

# sa "In fact, there is a friend of mine from…"
sa "ที่จริง ฉันมีเพื่อนคนหนึ่ง…"

play sound sfx_impact
with vpunch

# mystery "It's Hisao!"
mystery "ฮิซาโอะน่ะเอง!"

# "My eavesdropping is interrupted by a familiar voice and a familiar slap to the back. I don't need to guess the source of either, even without turning around."
"เสียงอันคุ้นเคยและแรงตบที่กระทบหลังฉันอันคุ้นเคยนั้นเข้ามาขัดจังหวะการดักฟังของฉัน ไม่ต้องเดาหรือหันไปมอง\nก็รู้ว่าใคร"

# hi "Hi Emi."
hi "ไงเอมิ"

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

show emicas invis:
    center
    xpos 0.15
with None

show bg gallery_int at left
show sae invis:
    xpos 0.75
show crowd at left
show emicas happy at center
with dissolvecharamove

hide sae
with None

# emi "Hi! Are you like, a representative of the art club or something? I don't see anyone else from the school here…"
emi "ไง! นายเป็นตัวแทนชมรมศิลปะไรงี้เหรอ ไม่เห็นมีนักเรียนจากโรงเรียนเรามาเลย…"

# hi "Umm… I don't know, really. I guess I am if that's the case."
hi "เอ่อ… ไม่รู้เลย ถ้างั้นก็คงใช่แหละมั้ง"

# hi "What about you?"
hi "แล้วเธอ?"

show emicas neutral
with charachange

# emi "What about me?"
emi "แล้วฉัน?"

# hi "Err…"
hi "เอ้อ…"

show emicas angry_up
with charachange

# emi "You didn't think I'm interested in art? Is that it, Hisao?"
emi "นายคิดว่าฉันไม่สนใจศิลปะใช่มั้ยล่ะฮิซาโอะ"

# hi "No, that's not what I… well, maybe a little, if you put it that way."
hi "ไม่ ไม่ได้… ก็ อาจจะนิดหน่อยแหละ ถ้าจะว่างั้นแล้ว"

# hi "I mean, even though you hang out with Rin I've never heard you talk about art with her so…"
hi "คือเห็นเธออยู่กับรินบ่อย ๆ ก็จริง แต่ฉันไม่เคยได้ยินเธอคุยกับรินเรื่องศิลปะเลย…"

show emicas awayfrown_up
with charachange

# "Emi huffs and looks around her, looking discontented."
"เอมิทำเสียงฮึดฮัดมองไปรอบ ๆ ทำท่าไม่พอใจ"

show emicas closedsmile
with charachange

# emi "It's true, I don't get it at all, but she came to my track meet so I thought it's only fair to return the favor."
emi "ก็จริง ฉันไม่เข้าใจเลย แต่รินมาดูฉันแข่งวิ่ง ก็เลยกะจะมาดูเป็นการตอบแทนบ้างน่ะแหละ"

show emicas wink_close
with characlose

# "She leans closer, trying to look confidential but only managing to look conspiring."
"เธอโน้มตัวเขาใกล้เต๊ะท่าให้ดูมั่นใจ แต่ดูยังไงก็เหมือนจะมีแผนร้ายอะไรมากกว่า"

# emi "Do you {b}get{/b} art?"
emi "นาย{b}เข้าใจ{/b}ศิลปะเหรอ"

# hi "No. No, I don't."
hi "ไม่ ไม่เข้าใจ"

# hi "At all."
hi "ไม่เลย"

show emicas closedsmile_close
with charachange

# "My emphasizing headshake draws a giggle and a cheery headshake of her own out of Emi."
"พอฉันสั่นหัวแรง ๆ เป็นการเน้นย้ำแล้วเอมิก็หัวเราะคิกคักพลางสั่นหัวร่าเริง"

show emicas happy_close
with charachange

# emi "Me neither!"
emi "ฉันก็ไม่!"

show emicas wink_close
with charachange

# emi "Hey, let's go talk with Rin! I bet you haven't yet, because I haven't either."
emi "นี่ ไปคุยกับรินกัน! นายคงยังไม่ได้คุยกับรินสิท่า เพราะฉันก็ยัง"

show emicas happy_up_close
with charachange

# emi "Come on!"
emi "ปะ!"

show nomiya invis behind emicas:
    center
    xpos 0.8
show rin invis:
    center
    xpos 1.1
with None


show bg gallery_int at center
show crowd at center
show emicas neutral_close:
    xpos 0.15
show nomiya smile:
    xpos 0.55
show rin basic_awayabsent:
    xpos 0.85
with dissolvecharamove

# "Before she has a chance to forcefully drag me to Rin, Nomiya appears behind her with Rin in his tow."
"ก่อนที่เธอจะทันลากฉันไปหาริน โนมิยะก็โผล่มาทางด้านหลังเธอพร้อมรินที่ประกบมาด้วย"

# "She's not dressed for the occasion, instead opting for the usual school uniform and unkempt hair."
"รินไม่ได้แต่งตัวให้ดูดีสมกับงาน เธอมาในสภาพชุดนักเรียนพร้อมผมยุ่ง ๆ อย่างเคย"

# "Maybe her natural look is what suits her the best."
"บางทีตัวเธอที่เป็นธรรมชาติอย่างนี้ก็คงเหมาะกับเธอที่สุดแล้ว"

show emicas happy_close
with charachange

# emi "Hello, teacher! Hi, Rin!"
emi "สวัสดีค่ะครู! ไงริน!"

# "Unfazed, Emi greets the teacher cheerfully, causing him to turn around and look down confusedly."
"เอมิทักทายคุณครูอย่างร่าเริงโดยไม่มีท่าทีสับสนแม้แต่น้อย โนมิยะหันมองรอบ ๆ แล้วก้มมองด้วยความงงงวย"

show nomiya frown
with charachange

# no "Who are you?"
no "เธอเป็นใครเหรอ"

show emicas frown_up_close
with charachange

# emi "I'm Emi, from school, class 3-4. Don't you remember?"
emi "หนูเอมิค่ะ เรียนอยู่ที่ยามากุ อยู่ห้อง 3-4 จำไม่ได้เหรอคะ"

# "She looks positively shocked at the prospect that there could be a person who doesn't know her."
"เธอตกใจทีเดียวที่ดูเหมือนว่าจะยังมีคนที่ไม่รู้จักเธออยู่ด้วย"

show nomiya talk
with charachange

# no "Oh, sorry. You are in the same class as Tezuka is, right?"
no "โอ้ ขอโทษที เรียนอยู่ห้องเดียวกันกับเทซูกะใช่มั้ย"

show emicas wink_close
with charachange

# emi "Yeah!"
emi "ค่ะ!"

show nomiya smile
with charachange

# no "You'll have to pardon me, I have trouble remembering students who don't take art."
no "ยกโทษให้ฉันด้วยนะ พอดีฉันจำคนที่ไม่ได้เรียนศิลปะไม่ค่อยได้"

show emicas closedsmile_up_close
with charachange

# emi "Don't mind, don't mind!"
emi "ไม่เป็นไรค่ะ ๆ !"

show emicas happy_close
with charachange

# emi "Hi Rin!"
emi "ไงริน!"

show rin basic_deadpan
with charachange

# rin "Hello."
rin "สวัสดี"

show emicas happy_up_close
with charachange

# emi "Congratulations for your super cool art thing! I'm sure you'll be a big hit!"
emi "ยินดีด้วยกับงานศิลปะสุดเจ๋งนี่นะ! เธอต้องประสบความสำเร็จแน่!"

# "She throws her arms into the air for boisterous emphasis, almost hitting me in the face."
"เธออ้าแขนออกเน้นย้ำคำพูดนั้นจนแขนแทบฟาดเข้ากับหน้าฉัน"

show emicas wink_up_close
with charachange

# emi "And look, Hisao came too!"
emi "เนี่ย ๆ ฮิซาโอะก็มาด้วยนะ!"

show rin relaxed_nonchalant
with charachange

# "Rin doesn't look at me, nor does she greet me."
"รินไม่มองหรือทักทายฉัน"

# hi "Congratulations, Rin."
hi "ยินดีด้วยนะริน"

# "She keeps averting her gaze, pointedly looking at her sandals."
"เธอไม่สบตาฉันและเอาแต่มองรองเท้าแตะตัวเอง"

show emicas closedsmile_close
with charachange

# "Oblivious to the tension between us and ignorant of what happened yesterday, Emi keeps on blabbering about this and that to an unresponsive Rin."
"เอมิที่ยังไม่รู้เรื่องระหว่างเราเมื่อวานไม่ได้รับรู้ถึงบรรยากาศที่ยังคุกรุ่นอยู่ เธอยังคงพล่ามเรื่องนั้นเรื่องนี้กับรินที่\nไม่ตอบสนองอะไร"

# "I guess she's used to not getting much out of her at times."
"บางทีเอมิก็คงชินแล้วละมั้งที่รินไม่หือไม่อืออะไร"

stop music fadeout 5.0
$ renpy.music.set_volume(1.0, 3.0, channel="ambient")

#event CG spot

show sae invis behind rin:
    center
    xpos 1.25
with None

show bg gallery_int at right
show crowd at right
show emicas invis:
    xpos -0.35
show nomiya smile:
    xpos 0.25
show rin relaxed_nonchalant:
    xpos 0.55
show sae neutral:
    xpos 0.8
with dissolvecharamove

hide emicas
with None

# "Before long, Nomiya and Sae turn to Rin, introducing her."
"ไม่นานโนมิยะและซาเอะก็หันมาทางรินและแนะนำตัวเธอ"

# "Expecting it, I catch the second of confusion when the guests see her arms."
"ตามคาด ฉันเห็นแขกที่ดูสับสนอยู่แวบหนึ่งเมื่อพวกเขาได้เห็นแขนของริน"

show sae smile
with charachange

# "Sae is luckily on the ball and briefly explains about our school."
"โชคดีที่ซาเอะไหวพริบดี เธออธิบายเรื่องโรงเรียนของเราให้ฟังคร่าว ๆ"

# "Doubtful faces quickly change to curious."
"ใบหน้าที่เคลือบแคลงเปลี่ยนเป็นสงสัย"

# "Man" "Would you mind telling us something about your art?"
thname("ชาย") "เล่าถึงผลงานศิลปะของเธอให้ฟังหน่อยได้ไหม"

# "Man" "I thought the development is quite easily noticeable, what do you yourself think of the differences between the older and more current works?"
thname("ชาย") "ตัวพัฒนาการของผลงานน่ะเห็นได้ชัดทีเดียวเลยนะ เธอคิดว่าผลงานเก่า ๆ กับผลงานปัจจุบันต่างกันยังไงบ้างเหรอ"

# "Man" "It's quite rare for someone so young to dabble into abstraction."
thname("ชาย") "หายากเหมือนกันนะเนี่ย คนที่จะมาเล่นพวกงานนามธรรมตั้งแต่อายุยังน้อยเนี่ย"

# "Woman" "It would've been interesting to see how you work!"
thname("หญิง") "อยากเห็นเธอวาดจังเลย ต้องน่าสนใจแน่!"

# "Man" "Oh, definitely! I assume you use your feet? Must've been a great trouble to learn it, you should be proud."
thname("ชาย") "นั่นสิ ๆ ! เธอใช้เท้าวาดใช่มั้ย คงหัดใช้ลำบากน่าดูเลย ภูมิใจเข้าไว้นะ"

show rin basic_surprised
with charachange

# rin "I… ummm…"
rin "ฉัน… เอ่อ…"

play music music_rain fadein 8.0

# "Man" "Will you be pursuing a career as an artist after school?"
thname("ชาย") "เรียนจบแล้วจะทำอาชีพเป็นศิลปินเลยหรือเปล่า"

# "She is bombarded with so many questions she can't even hope to answer all of them."
"เธอถูกยิงคำถามใส่รัว ๆ จนดูแล้วไม่น่าจะตอบได้หมดแน่ ๆ"

# "Maybe that's for the best, Rin tends to talk nonsense more than occasionally."
"ซึ่งก็น่าจะดีแล้ว เพราะรินก็พูดอะไรเรื่อยเปื่อยอยู่ไม่น้อยครั้ง"

# "Man" "So where do you get your ideas?"
thname("ชาย") "แล้วไปเอาไอเดียมาจากไหนเหรอ"

show rin relaxed_boredom
with charachange

# rin "That's the fourth, I mean fifth worst…"
rin "อันนั้นเป็นสิ่งแย่ที่สุดอันดับที่สี่ ไม่สิ อันดับที่ห้าที่…"

# "Rin keeps stumbling with her words, looking more and more vexed by the expectant inquiries."
"รินพูดตะกุกตะกัก ดูอึดอัดเข้าไปทุกทีกับแต่ละคำถามที่คาดหวังคำตอบนั้น"

show rin negative_annoyed
with charachange

# rin "Ah…"
rin "อ๊ะ…"

# "Everyone is waiting for her to say something, but she looks like a cat got her tongue."
"ทุกคนต่างรอให้เธอพูดอะไรสักอย่าง แต่ดูเหมือนว่าเธอจะพูดไม่ออกแล้ว"

# "Each question piling up just adds to her distress."
"แต่ละคำถามยิ่งกดดันเธอหนักเรื่อย ๆ"

show rin basic_sad
with charachange

# "I fail to hear the question that is the proverbial one too many."
"ฉันยังไม่ได้ยินคำถามที่จะมาเข้าสำนวนฟางเส้นสุดท้าย"

# "It's like a motor stalling."
"เหมือนเครื่องยนต์ที่หยุดค้าง"

show rin basic_sad:
    1.2
    parallel:
        easeout 0.5 ypos 1.2
    parallel:
        "rin basic_lucid" with Dissolve(0.3, alpha=True)
with Pause(1.5)

stop ambient fadeout 7.0

scene ev rin_gallery:
    truecenter
    zoom 0.9 subpixel True
    easein 30.0 zoom 1.0
with Dissolve(0.2)
play sound sfx_pillow
with vpunch

# "Rin just freezes for a long, long second until she falls on her knees, hitting the floor ungracefully like a sack of potatoes."
"รินยืนตัวแข็งทื่ออยู่นานหลายวินาที จนกระทั่งเธอทรุดลงกับพื้นด้วยท่าทีไม่น่าดูเหมือนกระสอบมันฝรั่งที่ตกพื้น"

# "Woman" "Are you all right?"
thname("หญิง") "เป็นอะไรหรือเปล่า"

# rin "I don't know…"
rin "ไม่รู้…"

# no "Tezuka? What's wrong, girl?"
no "เทซูกะ ไหวมั้ยหนู"

# rin "I don't know what's wrong…"
rin "ไม่รู้ว่าเป็นอะไร…"

# "A terrible silence falls upon the people gathered around Rin."
"คนรอบ ๆ ตัวรินเงียบไปจนฉันใจคอไม่ดี"

# "Everyone is petrified, not knowing how to react to her sudden… seizure, or something."
"ทุกคนต่างชะงักงัน ต่างไม่รู้ว่าจะทำยังไงกับ… อาการตกใจหรืออะไรสักอย่างของเธอที่อยู่ ๆ ก็เป็นขึ้นมา"

# "She breathes with deep, trembling gasps as if she was running out of air, staring ahead of herself with hollow eyes."
"เธอหายใจเข้าลึก ๆ ลมหายใจเธอสั่น ๆ คล้ายหายใจไม่ทัน เธอมองไปข้างหน้าด้วยสายตาว่างเปล่า"

play sound sfx_rustling
stop music fadeout 1.0

scene bg gallery_int at right
show crowd at right
show nomiya serious:
    center
    xpos 0.25
show rin negative_sad_close:
    center
    xpos 0.55 ypos 1.2
    ease 0.8 ypos 1.0
show sae scowl:
    center
    xpos 0.8
with locationchange

# "Seeing that nobody does anything, I force myself to step to Rin and lift her up from the floor, letting her lean against me to keep standing."
"ในเมื่อไม่มีใครทำอะไรฉันจึงเบียดตัวเองเข้ามาหารินแล้วดึงเธอให้ลุกขึ้น ก่อนจะให้เธอพยุงตัวพิงกับฉันไว้"

# hi "Would you like some fresh air? OK, let's go outside for a bit."
hi "ออกไปสูดอากาศก่อนมั้ย โอเค งั้นออกไปข้างนอกกัน"

# "I don't even wait for her to answer before grasping her shoulder and pulling her past the stunned-looking Nomiya, Sae, Emi and guests."
"ฉันไม่รอคำตอบจากเธอแล้วคว้าไหล่ดึงเธอเดินผ่านแขก เอมิ ซาเอะ และโนมิยะที่ดูอึ้งไป"

# hi "Excuse us."
hi "ขอตัวนะครับ"

play sound sfx_storebell
$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_traffic fadein 1.0

scene bg gallery_ext
with locationchange

# "The cool evening breeze hits my face at the door."
"ลมยามเย็นปะทะเข้ากับหน้าฉันเมื่อเดินผ่านประตูออกมา"

show rin negative_sad_close_ni at center
with charaenter

# "I let go of Rin and she leans against the stone wall, trying to catch her breath."
"ฉันปล่อยรินยืนพิงผนังหินให้เธอได้พักหายใจ"

# hi "Are you all right?"
hi "เป็นอะไรหรือเปล่า"

show rin negative_confused_close_ni
with charachange

# rin "I couldn't say anything…"
rin "ฉันพูดอะไรไม่ออกเลย…"

# "Rin is still not looking at me, so I look away too."
"รินยังไม่ได้มองมาที่ฉัน ฉันจึงมองไปทางอื่นด้วย"

play music music_dreamy fadein 4.0

# "The streetlights and colored neon signs twist my vision into a blur of near-blindness, forcing me to look back."
"ไฟถนนและป้ายไฟนีออนแยงตาจนตาพร่าแทบมองไม่เห็น ทำให้ฉันต้องเบือนหน้าหนี"

# "At least she talks, even if she's not directing her words to me."
"อย่างน้อยรินก็พูดแล้ว ถึงจะไม่ได้พูดกับฉันก็เถอะ"

# hi "What did you want to say?"
hi "อยากพูดอะไรล่ะ"

# "Maybe both of us can imagine that we are talking to an invisible friend."
"บางทีเราสองคนก็คงจินตนาการเอาได้ว่าคุยกับเพื่อนล่องหนอยู่"

show rin basic_sad_close_ni
with charachange

# rin "I don't know."
rin "ไม่รู้"

show rin negative_sad_close_ni
with charachange

# rin "Something that would have meant something."
rin "อะไรสักอย่างที่หมายความว่าอะไรสักอย่าง"

"…"

# "The silence lasts for a long time."
"ความเงียบกินเวลาเนิ่นนาน"

# "I don't feel comfortable being alone with Rin. I am not good at imagining things that don't exist, do… or that things that exist, don't."
"ฉันรู้สึกอึดอัดที่ได้อยู่แค่สองคนกับริน ฉันจินตนาการถึงสิ่งที่ไม่มีอยู่จริง…หรือสิ่งนั้นที่มีอยู่จริงไม่เก่ง"

# hi "We should go back in."
hi "กลับเข้าไปกันดีกว่านะ"

# hi "The guests Sae invited are in there, they probably want to meet you and talk with you."
hi "แขกที่ซาเอะเชิญมาก็อยู่ในนั้นนะ คงอยากเจออยากคุยกับเธอนั่นแหละ"

# hi "You know, ask you questions and stuff. About those paintings you worked so hard for."
hi "แบบ ถามเธออะไรงี้ เรื่องภาพวาดที่เธอทุ่มเทมาอย่างหนักน่ะ"

show rin negative_angry_close_ni
with charachange

# rin "I don't want them to ask me questions like that. I can never say the right things."
rin "ฉันไม่อยากให้พวกเขาถามคำถามอย่างนั้น ฉันพูดอะไรดี ๆ ไม่ได้เลย"

# hi "What do you want then?"
hi "แล้วเธอจะเอายังไง"

"…"

show rin relaxed_doubt_close_ni
with charachange


label th_choiceR32:
menu:
    with menueffect

    #choice:
    # rin "That someone wouldn't have to ask questions from me."
    rin "ฉันอยากได้คนที่ไม่ถามคำถามอะไรกับฉัน"

    # "But aren't you happy people are interested in your paintings?":
    "แล้วเธอไม่ดีใจเหรอที่คนสนใจภาพที่เธอวาดน่ะ":
        return m1

    # "But if you found someone like that, then what?":
    "แล้วถ้าเจอคนอย่างที่ว่านั้นแล้วยังไงต่อ":
        return m2

label th_R32a:

$ renpy.music.set_volume(0.2, 0.2, channel="ambient")

# hi "But aren't you happy people are interested in your paintings?"
hi "แล้วเธอไม่ดีใจเหรอที่คนสนใจภาพที่เธอวาดน่ะ"

# hi "I mean, isn't that why you went ahead with having the exhibition and all?"
hi "ก็เพราะอย่างนั้นไม่ใช่เหรอเธอถึงได้ยอมจัดงานนิทรรศการน่ะ"

# hi "Of course they would ask you questions, if they think it's interesting."
hi "ก็ไม่แปลกที่มีคนจะถามคำถาม เพราะคนเขามองว่าน่าสนใจไง"

show rin negative_annoyed_close_ni
with charachange

# rin "It's like having sunrise twice in a row when you want to bathe naked in moonlight."
rin "เหมือนพระอาทิตย์ขึ้นสองครั้งติดกันทั้งที่อยากเปลือยอาบแสงจันทร์"

show rin negative_angry_close_ni
with charachange

# rin "Nice, but…"
rin "ดี แต่…"

# "…it's not good enough, I complete the sentence for her even though I don't understand her inappropriate metaphor."
"…ยังดีไม่พอ ฉันต่อประโยคให้เธอจนจบแม้ฉันจะไม่เข้าใจคำเปรียบเทียบที่ไม่เหมาะสมนั้น"

# hi "I don't get it."
hi "ฉันไม่เข้าใจ"

# hi "You should try to be happier. It's your big night, after all."
hi "เธอต้องทำตัวให้มีความสุขกว่านี้สิ คืนนี้คืนสำคัญนี่"

# hi "All these people are here to see your paintings. I think it's awesome."
hi "คนก็แห่มาดูภาพที่เธอวาดกัน ฉันว่าสุดยอดไปเลยนะ"

# "I wait for her to say something, either for or against, but Rin keeps brooding."
"ฉันรอให้รินพูดอะไรสักอย่าง ไม่ว่าจะเห็นด้วยหรือคัดค้าน แต่เธอยังคงเอาแต่นิ่งคิด"

# "She doesn't want to answer questions, or explain to me what's wrong."
"เธอไม่อยากตอบคำถามหรืออธิบายกับฉันว่าเป็นอะไรไป"

# "If she had something to say, the words are left unspoken."
"ถ้าเธอมีอะไรจะพูด คำพูดเหล่านั้นจะไม่ได้พูดออกมา"

# "The words that she cannot say."
"คำพูดที่เธอพูดไม่ได้"

# "I shudder against the chill wind that blows in the streets, and its howling fills the silence."
"ลมเย็นที่พัดวูบมาจากถนนทำฉันตัวสั่น เสียงหวีดหวิวของสายลมเติมเต็มความเงียบงัน"

# hi "We should go back in."
hi "กลับเข้าไปกันดีกว่านะ"

# hi "You've got everyone worried."
hi "ทุกคนเป็นห่วงเธอแย่แล้ว"

stop ambient fadeout 0.5
play sound sfx_storebell

scene bg gallery_int
show crowd
show nomiya talk at twoleft
show sae neutral at tworight
with locationchange

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 2.0

# no "Ah, there you are! Feeling better? It can get pretty hot in here, a dizzy spell can catch you off guard."
no "อ้าว มาจนได้! รู้สึกดีขึ้นหรือยัง ในนี้บางทีมันก็ร้อน ๆ จะเป็นลมเป็นแล้งไปก็ไม่แปลก"

show nomiya veryhappy
with charachange

# "He laughs brashly, almost obnoxiously."
"เขาหัวเราะเต็มที่จนค่อนไปทางหยาบคาย"

show nomiya talk
with charachange

# no "You should drink something if you're feeling weak, Tezuka."
no "ถ้าไม่มีแรงก็หาอะไรดื่มหน่อยนะ เทซูกะ"

show nomiya talk:
    center
    xpos 0.25
show sae neutral:
    center
    xpos 0.8
with charamove

show rin basic_lucid:
    center
    xpos 0.55
with charaenter

# "Rin nods weakly, but it seems to be enough to convince Nomiya that she is fine."
"รินพยักหน้าอ่อนแรง แต่ก็ดูเพียงพอที่จะทำให้โนมิยะเชื่อแล้วว่าไม่เป็นอะไร"

# "He pushes Rin a bit forward to introduce her to the person he was conversing with before."
"เขาดันตัวรินไปแนะนำเธอให้กับคนที่เขาคุยอยู่ด้วยเมื่อครู่"

show nomiya smile
with charachange

# no "So, about what we were talking about before…"
no "เอ้อ เรื่องที่คุยกันเมื่อกี้…"

# "Man" "Ah yes, I'm very excited to meet…"
thname("ชาย") "อ้อ ครับ ผมตื่นเต้นมากที่ได้พบ…"

stop music fadeout 8.0

# "I am shut out of the conversation, and the background noise of dozens of other discussions fills my ears with indistinct buzz."
"ฉันถูกเตะออกจากวงสนทนาทันที เสียงอื้ออึงของคนที่คุยกันจนฟังไม่ออกนั้นไหลเข้ามาในหูฉัน"

# "Even Emi has disappeared somewhere."
"เอมิก็หายไปไหนแล้วไม่รู้"

# "Standing in the middle of a crowd is a surprisingly lonely feeling."
"การยืนอยู่ท่ามกลางผู้คนนั้นทำให้เกิดความรู้สึกโดดเดี่ยวได้อย่างเหลือเชื่อ"

# "Not only Rin, but everyone else here seems to be a part of something I am not a part of."
"ไม่ใช่แค่ริน แต่ทุกคนที่นี่ต่างก็เป็นส่วนหนึ่งของบางอย่างที่ฉันไม่ได้เป็นอยู่ด้วย"

# "I am happy for her, I really am, but it makes me feel that I haven't accomplished anything yet."
"ฉันยินดีไปกับริน ยินดีจริง ๆ แต่ฉันก็กลับมารู้สึกเหมือนไม่ได้ทำอะไรเลยเหมือนกัน"

# "Rin is living proof of the potential of a human being. She overcame her disability, even made it a strength."
"รินคือประจักษ์พยานที่แสดงให้เห็นถึงศักยภาพของมนุษย์ เธอก้าวข้ามความพิการของเธอ ทั้งยังนำมาเป็นจุดแข็ง"

stop ambient fadeout 4.0

# "She should be happy."
"เธอควรจะมีความสุข"

# "What is my potential?"
"ศักยภาพของฉันคืออะไร"

# "Rin made it this far, but how far can I go?"
"รินมาได้ไกลขนาดนี้ แต่ฉันไปได้ไกลขนาดไหน"

scene black
with dissolve


label th_R32b:

$ renpy.music.set_volume(0.2, 0.2, channel="ambient")

# hi "But if you found someone like that, then what?"
hi "แล้วถ้าเจอคนอย่างที่ว่านั้นแล้วยังไงต่อ"

# hi "Do you really think that it would be some kind of be-all, end-all thing, star-crossed lovers and happily ever after?"
hi "เธอคิดเหรอว่าถ้าเจอแล้วจะเป็นทุกสิ่งอย่าง เป็นโลกทั้งใบ เป็นคนรักที่พรหมลิขิตบันดาลชักพามาให้ครองรักกันไป\nตลอดกาลน่ะ"

show rin basic_absent_close_ni
with charachange

# "My question is met with a blank stare, the darkness in her eyes unfazed by the thinly veiled bitterness."
"เธอตอบคำถามฉันด้วยสายตาว่างเปล่า ความมืดมิดในดวงตาเธอไม่สะทกสะท้านกับความขมขื่นในคำพูดที่แทบ\nปิดไม่มิดนั้น"

show rin negative_worried_close_ni
with charachange

# rin "No, I don't think that."
rin "ไม่ ฉันไม่คิดว่าอย่างนั้น"

show rin negative_annoyed_close_ni
with charachange

# rin "But at least then I wouldn't have to be alone."
rin "แต่อย่างน้อยฉันก็จะไม่ต้องอยู่ตัวคนเดียว"

# "She whispers the words to the lights of the town but I hear them anyway."
"เธอกระซิบคำพูดอยู่กับแสงสว่างจากเมือง แต่ฉันก็ได้ยิน"

show rin negative_sad_close_ni
with charachange

# rin "I shouldn't have done this. Not yet."
rin "ฉันไม่น่าทำเลย ยังไม่ควร"

# hi "The exhibition?"
hi "งานนิทรรศการ?"

show rin basic_lucid_close_ni
with charachange

# "She nods and closes her eyes, breathing calmly out as if to prove she can, and then continues talking to herself."
"เธอพยักหน้าแล้วหลับตาหายใจช้า ๆ ราวกับจะพิสูจน์ว่าตัวเองก็ทำได้แล้วคุยกับตัวเองต่อ"

# hi "Why? Wrong conjunction of the planets?"
hi "ทำไม ฤกษ์ไม่ดี?"

show rin basic_sad_close_ni
with charachange

# rin "No, not that. I double-checked, and I got up with the right, I mean left, foot and did everything else left, I mean right."
rin "ไม่ ไม่ใช่อันนั้น ฉันดูสองรอบแล้ว ตอนตื่นมาฉันก็ใช้เท้าซ้ายลงเตียงก่อน แล้วทำอย่างอื่นด้วยเท้าขวา"

show rin negative_sad_close_ni
with charachange

# rin "It's me."
rin "ฉันเอง"

show rin negative_worried_close_ni
with charachange

# rin "I was wrong."
rin "ที่ผิด"

hide rin
with charaexit

# "She stands straight and stretches before stepping past me out into the street."
"เธอยืดตัวยืนตรงก่อนจะเดินผ่านฉันออกไปที่ถนน"

# hi "Wait, where are you going?"
hi "เดี๋ยว จะไปไหนน่ะ"

show rin basic_absent_ni
with charaenter

# "She stops on her tracks and turns around, looking at me quizzically."
"เธอชะงักแล้วหมุนตัวมามองฉันด้วยความสงสัย"

show rin basic_awayabsent_ni
with charachange

# rin "School. I'm leaving."
rin "โรงเรียน ไปละ"

# hi "What… why?"
hi "อะไร… ทำไม"

show rin basic_absent_ni
with charachange

# rin "Because I want to be me."
rin "เพราะฉันอยากเป็นฉัน"

$ renpy.music.set_volume(0.4, 1.0, channel="ambient")

hide rin
with charaexit

# "Rin walks off, leaving me behind utterly confused."
"รินเดินจากไป ทิ้งฉันให้งงงวย"

# hi "Rin!"
hi "ริน!"

# "But… something she said really touched me, or maybe it was the way she said it."
"แต่… ฉันรู้สึกประทับใจกับคำพูดเธอ หรืออาจจะเป็นเพราะการเลือกใช้คำของเธอ"

# "Maybe it was the fact that {b}she{/b} said it."
"หรืออาจจะเป็นเพราะ{b}เธอ{/b}เป็นคนพูด"

# "I want to say something back to her, before I forget this feeling again."
"ฉันอยากพูดอะไรตอบก่อนที่ฉันจะลืมความรู้สึกนี้อีกครั้ง"

# "As if granting me a wish, Rin stops in her tracks. She doesn't turn around, just keeps waiting for me to say what I want to even though I didn't have time to think what…"
"รินหยุดเดินไปราวกับตอบรับคำขอของฉัน เธอไม่หันมา เพียงแต่รอให้ฉันพูดสิ่งที่อยากพูด ถึงฉันไม่มีเวลาคิดว่าจะพูด\nอะไรดี…"

# hi "Rin… listen. I… I don't believe you have to be alone, even if you never meet anyone like that."
hi "ริน… ฟังนะ ฉัน… ฉันเชื่อว่าต่อให้เธอไม่เจอคนอย่างนั้น เธอก็ไม่จำเป็นต้องอยู่ตัวคนเดียวหรอก"

# "I don't know if she heard my words, but either way, she doesn't react in any way."
"ไม่รู้ว่าเธอได้ยินหรือเปล่า แต่จะได้ยินหรือไม่ได้ยิน เธอก็ไม่ตอบสนองอะไรอยู่ดี"

# "For the final time, she starts walking away from the gallery."
"และเธอก็เดินออกห่างจากหอศิลป์ไปเป็นครั้งสุดท้าย"

play sound sfx_storebell
stop ambient fadeout 0.5

scene bg gallery_int
show crowd at center
show nomiya frown at twoleft
show sae doubt at tworight
with locationchange

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 2.0

# no "So? Where's Tezuka?"
no "แล้วเทซูกะอยู่ไหน"

# "I can only shake my head, but as it doesn't seem to be a sufficient answer I have to say something."
"ฉันได้แต่สั่นหัว แต่เมื่อเห็นว่าทำแค่นี้คงตอบไม่หมด ฉันจึงต้องพูดอะไรอีก"

# hi "She ran away."
hi "หนีไปครับ"

show nomiya stern
with charachange

# no "What?"
no "อะไรนะ"

# "The horrific realization spreads on his face like wildfire."
"ข่าวร้ายนี้แพร่แสดงออกบนสีหน้าคุณครูราวไฟป่า"

show nomiya serious
with charachange

# no "This is a fiasco! Catastrophe!"
no "น่าอับอายยิ่งนัก! พังไม่เหลือชิ้นดี!"

# no "What is that girl thinking, the most important event of her life, and she just runs off?"
no "นี่แม่นั่นคิดอะไรอยู่เนี่ย นี่มันงานสำคัญที่สุดในชีวิตเลยนะ หนีไปอย่างนี้เลยเหรอ"

show nomiya stern
with charachange

# no "And you! Why didn't you stop her? I'm going to hold you personally responsible…"
no "แล้วเธอ! ทำไมเธอไม่ห้าม ฉันจะให้เธอรับผิดชอบ…"

show sae neutral
with charachange

# "Sae interrupts him, holding her hands up calmingly."
"ซาเอะเข้ามาขัดทำท่าปางห้ามญาติ"

# "It's good she intervened; the teacher was starting to get a few weird looks from the nearby guests."
"ยังดีที่เข้ามาขัด เพราะแขกที่อยู่ใกล้ ๆ บางคนก็เริ่มมองคุณครูด้วยสายตาแปลก ๆ แล้ว"

show sae smile
with charachange

# sa "Now, now, Shinichi. She probably just had stage fright. I don't know her as well as you people do, but I did get the image that she is somewhat peculiar."
sa "เอ้า ๆ ชินอิจิ แม่หนูคนนั้นอาจจะแค่ตื่นเวทีก็ได้ ฉันก็ไม่ได้รู้จักแม่หนูดีเท่าพวกเธอหรอกนะ แต่ก็พอจะเข้าใจอยู่ว่า\nเป็นคนที่ค่อนข้างแปลกน่ะ"

# sa "This kind of thing can happen."
sa "เรื่องแบบนี้มันก็เกิดกันได้"

show sae neutral
with charachange

# sa "It'll be fine. I'll explain that she suddenly became ill. The guests will surely understand."
sa "ไม่เป็นไรหรอก ฉันจะบอกเองว่าอยู่ ๆ แม่หนูเขาก็ป่วย แขกเขาต้องเข้าใจแน่นอน"

show nomiya frown
with charachange

# no "But…"
no "แต่…"

show sae smile
with charachange

# sa "Look around you, everyone seems to be rather happy with their free wine and chitchat."
sa "ดูแต่ละคนสิ ทุกคนก็ดูจะพอใจที่ได้คุยกันไปพลางจิบไวน์ฟรีไปพลางกันทั้งนั้น"

show nomiya serious
with charachange

# no "The guests will be fine, but we are missing on opportunities here! Networking, making contacts and acquaintances!"
no "แขกน่ะไม่เป็นไรหรอก แต่จะพลาดโอกาสเอานะ! ทำความรู้จักกัน สร้างคอนเนกชันกันไง!"

show emicas invis_close:
    center
    xpos -0.35
with None

show bg gallery_int at left
show crowd at left
show nomiya serious:
    xpos 0.5
show sae smile:
    xpos 0.9
show emicas frown_close:
    xpos 0.15
with dissolvecharamove

# "As the adults keep arguing about something that can't be helped, Emi tugs my sleeve to get my attention."
"ระหว่างที่พวกผู้ใหญ่เถียงกันเรื่องที่ช่วยไม่ได้นั้น เอมิก็กระตุกแขนเสื้อเพื่อดึงความสนใจฉัน"

# "She doesn't look very happy either."
"เธอก็ดูไม่สบอารมณ์สักเท่าไหร่เหมือนกัน"

show emicas awayfrown_close
with charachange

# emi "Come on."
emi "ปะ"

# hi "Where?"
hi "ไปไหน"

show emicas frown_up_close
with charachange

# emi "We are going to find Rin and kick her ass."
emi "ตามหารินแล้วสั่งสอน"

# hi "What?"
hi "อะไรนะ"

show emicas angry_close
with charachange

# emi "I can't believe it, she is so stupid!"
emi "ไม่อยากจะเชื่อเลยว่าจะโง่ได้ขนาดนี้!"

# emi "That Rin, how can she do this? I'm telling you, she doesn't have a bit of common sense in her head!"
emi "รินนะริน ทำอย่างนี้ได้ไง บอกให้เลยนะ ยัยนั่นน่ะในหัวไม่มีคำว่าสามัญสำนึกเลยสักเสี้ยวเดียว!"

# "Emi is seriously angry, only missing steam rising from her ears."
"เอมิโกรธจริงจัง ขาดก็แต่ควันออกหู"

# "I guess I understand Emi, she is {b}that{/b} kind of a person."
"ก็พอจะเข้าใจละนะ เอมิก็เป็นคน{b}อย่างนั้น{/b}แหละ"

# "“Give up” has never felt like a part of her vocabulary, and maybe she feels it shouldn't be a part of anyone's vocabulary."
"คำว่า “ยอมแพ้” ไม่มีในพจนานุกรมของเธอ และบางทีเธอก็คงไม่อยากให้มีอยู่ในพจนานุกรมใครด้วย"

# hi "It's probably best to leave her alone for tonight."
hi "คืนนี้ให้รินอยู่คนเดียวไปน่าจะดีกว่านะ"

show emicas angry_up_close
with charachange

# emi "What? Are you a Rin expert now?"
emi "อะไร? นี่เป็นผู้เชี่ยวชาญรินแล้วเหรอ"

# "She takes a firm stance and puts her hands on her hips confrontationally."
"เธอยืนเท้าสะเอวประจันหน้าฉัน"

# "It's like she wants to pick a fight with me too."
"อย่างกับว่าจะหาเรื่องฉันด้วยอีกคน"

# hi "No, I don't think that's even possible in the first place."
hi "ไม่ แต่เอาจริง ๆ ฉันว่าเป็นไปไม่ได้หรอกนะที่จะเป็นผู้เชี่ยวชาญรินน่ะ"

# hi "I just don't think kicking her ass would do her any good."
hi "ฉันแค่คิดว่าสั่งสอนรินไปก็คงไม่ได้อะไรขึ้นมา"

show emicas frown_close
with charachange

# "My melancholic remark surprisingly works, as Emi slumps her shoulders a little and sighs."
"คำพูดเศร้า ๆ ของฉันนั้นได้ผลเหลือเชื่อ เอมิหย่อนไหล่ลงเล็กน้อยแล้วถอนหายใจ"

# emi "I know that."
emi "ฉันรู้"

# hi "You do?"
hi "เธอรู้?"

stop music fadeout 2.0

show emicas awayfrown_close
with charachange

# emi "The last time I did that, it changed nothing."
emi "ล่าสุดที่สั่งสอนไปก็ไม่ได้เปลี่ยนอะไรเลย"

stop ambient fadeout 1.0

scene ev busride_ni
with locationskip

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")
play ambient sfx_businterior fadein 2.0

# "The ride back to school in an empty late-night bus is silent."
"มีเพียงความเงียบระหว่างที่นั่งรถบัสรอบดึกที่ไม่มีใคร"

# "Both of us keep staring at the lights flashing past the windows without saying a word."
"เราสองคนเอาแต่มองแสงไฟที่วูบวาบผ่านหน้าต่างไปโดยไม่พูดอะไร"

stop ambient fadeout 1.0

scene bg school_dormext_full_ni
with locationskip

play music music_soothing fadein 0.5

# "The nightly grounds are quiet, lit only by the wan moon and yellow lamp posts."
"โรงเรียนตอนกลางคืนนั้นเงียบสงัด มีเพียงแสงจากจันทร์ข้างแรมและเสาไฟสีเหลืองที่ส่องสว่าง"

# "We say our goodnights in front of my dormitory."
"พวกเราแยกทางราตรีสวัสดิ์กันอยู่หน้าหอพัก"

show emicas awayfrown_up_ni at center
with charaenter

# "Emi reflexively clenching her fists compels me to ensure that she won't assault Rin the moment I let her out of my sight."
"พอเห็นเอมิที่กำหมัดโดยอัตโนมัติแล้วฉันก็ต้องย้ำให้แน่ใจว่าเธอจะไม่ทำอะไรรินทันทีที่เธอลับสายตาฉันไปแล้ว"

# hi "Promise me to not go scold her?"
hi "สัญญานะว่าจะไม่ดุริน?"

show emicas angry_up_ni
with charachange

# "She looks up at me, her eyes again flaring with anger that I match with as calming a stare as I can."
"เธอมองฉันด้วยสายตาโกรธเกรี้ยว ฉันรับสายตานั้นด้วยสายตาอันเยือกเย็นเท่าที่ฉันจะปั้นได้"

# "It's only easy to face an angry woman if you are not the target of her ire."
"ถ้าไม่ได้เป็นสาเหตุที่ไปทำให้ผู้หญิงโกรธตรง ๆ แล้ว จะเผชิญหน้าก็ง่ายหน่อย"

# "After a minute of the mismatched staring contest, she sighs and shakes her head in defeat."
"พอแข่งจ้องตาแบบไม่ลงตัวกันได้สักหนึ่งนาทีเธอก็ถอนหายใจแล้วส่ายหน้ายอมแพ้"

show emicas closedsmile_ni
with charachange

# emi "You are too nice, Hisao."
emi "นายน่ะแสนดีเกินไปนะ ฮิซาโอะ"

show emicas weaksmile_ni
with charachange

# emi "Did you know that?"
emi "รู้ตัวมั้ย"

# "Hints of a smile are tugging the corners of her mouth as she says that, and she seems a lot more relaxed."
"เธอหยักยิ้มมุมปากเล็กน้อย ท่าทีเธอดูผ่อนคลายลงมาก"

# "What a sudden change of mood."
"เปลี่ยนอารมณ์ไวจริง"

# "Maybe she wasn't as angry as it seemed to begin with."
"อาจจะไม่ได้โกรธเหมือนอย่างที่เห็นแต่แรกก็ได้"

# "Maybe her moods change easily."
"อาจจะอารมณ์เปลี่ยนง่ายก็ได้"

# hi "If I was, I would've let you have your way."
hi "ถ้าแสนดีจริงฉันคงปล่อยให้เธอใช้ฉันไปแล้ว"

show emicas wink_ni
with charachange

# emi "Does that mean you are only nice to Rin?"
emi "หมายความว่านายแสนดีแค่กับรินคนเดียว?"

# "Both of us are hiding our concern behind empty jokes, but at least it puts me in a good mood."
"พวกเราต่างใช้คำหยอกล้ออันเปล่ากลวงปกปิดความเป็นห่วง แต่อย่างน้อยฉันก็อารมณ์ดีได้แล้วละนะ"

# "Emi waggles her eyebrows with a half-amused smirk, trying to push my buttons. Not gonna work."
"เธอยักคิ้วยิ้ม ๆ กะจะยั่วโมโหฉันสิท่า ไม่มีวันซะละ"

# hi "No, it just means I'm not nice only to you."
hi "เปล่า หมายความว่าฉันไม่ได้แสนดีแค่กับเธอคนเดียว"

show emicas angry_up_ni
with charachange

# emi "HEY!"
emi "เดี๋ยวเถอะ!!"

stop music fadeout 2.0

# hi "Good night, Emi."
hi "ราตรีสวัสดิ์ เอมิ"

scene black
with dissolve


label th_R33:

play music music_daily fadein 0.5

scene bg school_scienceroom
with locationchange

# "The last day before summer vacations is waning slowly."
"วันสุดท้ายก่อนปิดเทอมฤดูร้อนเคลื่อนคล้อยไปอย่างเชื่องช้า"

# "Science is the final exam of the trimester and then we are free."
"วิชาที่ได้สอบเป็นวิชาสุดท้ายของเทอมนี้คือวิชาวิทยาศาสตร์ จากนั้นพวกเราก็จะเป็นอิสระ"

# "The collective yearning for liberty is almost palpable in the classroom, even though the weather seems a tad cloudy."
"ความกระหายอิสรภาพลอยกรุ่นอยู่ในห้องจนแทบสัมผัสได้ แม้วันนี้ฟ้าจะครึ้มเล็กน้อยก็ตาม"

# "It might rain today, who knows."
"วันนี้ฝนอาจจะตกก็ได้ ใครจะไปรู้"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene ev rin_doodle
with locationchange

# "I've already finished the test because it was pretty easy, so I'm doodling lazily on the flip side of the paper, waiting for Mutou to call time."
"ฉันทำข้อสอบเสร็จแล้วเพราะค่อนข้างง่าย ฉันจึงวาดเล่นที่อีกหน้ากระดาษรอจนกว่ามุโต้จะบอกว่าหมดเวลา"

# "It also prevents Misha from trying to covertly look at my answers over my shoulder."
"เป็นการป้องกันไม่ให้มิช่าแอบชะเง้อดูคำตอบของฉันด้วย"

# "She might fool the inattentive teacher, but I can tell that she is trying to look."
"อาจจะหลอกครูที่ไม่สนใจอยู่ได้ แต่ฉันเห็นว่าเธอคอยมองอยู่"

# "I guess it's her best bet at passing the test. Doesn't make me feel any mercy though, so I just ignore her and look around me."
"คงเป็นที่พึ่งหวังเดียวที่จะทำให้สอบผ่านละมั้ง แต่ก็ไม่ได้สงสารอยู่ดี ฉันจึงเมินเธอแล้วมองไปรอบ ๆ"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

scene bg school_scienceroom
with locationskip

# "It's quiet."
"เงียบ"

# "The only sounds in the classroom are the quiet shuffling of papers and Mutou's constant coughing."
"เสียงที่ได้ยินมีเพียงเสียงกระดาษกับเสียงมุโต้ที่ไอไม่หยุด"

# "It makes my awareness of the surroundings slowly drift to the backstage of consciousness, giving room to other things."
"เงียบเสียจนการรับรู้สภาพโดยรอบของฉันค่อย ๆ จมลึกลงไปในจิตใต้สำนึกจนเหลือพื้นที่ให้คิดเรื่องอื่น"

#jump to R35 if Rin didn't run away in R32, otherwise fallthrough
#both scenes attach directly
#this is solved differently in practice


label th_R34:
scene bg school_scienceroom
with None

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

# n "\nVacation, huh?"
n "\nปิดเทอมเหรอ"

# n "Some people will stay at the school even over the holidays, some will go back to their families."
n "ต่อให้โรงเรียนปิดแล้วบางคนก็จะยังอยู่ที่หอต่อ แต่ก็มีบางคนที่จะกลับไปหาครอบครัว"

# n "I don't know what to do. I should go buy a train ticket for my trip back home, but I can't bring myself to do it."
n "ฉันไม่รู้จะทำอะไรดี จริง ๆ ก็ควรไปซื้อตั๋วรถไฟกลับบ้าน แต่ก็ไม่มีกะจิตกะใจจะไปเลย"

# n "I bet I'm going to get a call from home again. Mom's going to pester me about when I'm coming back, and I'm not going to know what to answer."
n "เดี๋ยวที่บ้านต้องโทรตามอีกแน่ แม่ก็จะตามจิกว่าเมื่อไหร่จะกลับ แล้วฉันก็จะไม่มีคำตอบให้"

# n "\nThis is really lousy. In the current state of things with Rin, it feels like I can't just bail out of here and pretend we are through."
n "\nไม่เอาไหนชะมัด พอสถานะกับรินเป็นอย่างนี้แล้วจะให้ทำเป็นจบ ๆ กันแล้วหนีไปก็ยังไงอยู่"

# n "\nAnd now, she has other problems of her own. I thought that the exhibition opening would give her a breather, but I was sorely mistaken."
n "\nแล้วตอนนี้เธอก็มีเรื่องของเธอเองด้วย ก็นึกว่าเปิดงานนิทรรศการแล้วเธอจะได้พักหายใจหายคอบ้างแท้ ๆ แต่ฉัน\nคิดผิดมหันต์"

# n "\n\nThe tangle just seems to thicken."
n "\n\nเรื่องดูจะยิ่งพันกันยุ่งเข้าไปอีก"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

play sound sfx_doorknock

window show

# "A sharp knock on the door interrupts the quiet but frantic mood of the last 15 minutes of the exam."
"เสียงเคาะประตูเข้ามาขัดจังหวะความเงียบอันรีบเร่งของช่วงสิบห้านาทีสุดท้ายก่อนหมดเวลาสอบ"

show muto normal at center
with charaenter

$ renpy.music.set_volume(0.2, 0.0, channel="sound")

# mu "Come in."
mu "เข้ามา"

stop music fadeout 1.0
$ renpy.music.set_volume(1.0, 8.0, channel="sound")
play sound sfx_footsteps_hard

show bg school_scienceroom at bgleft
show muto normal at twoleft
with charamove

show nomiya serious at tworight
with charaenter

# "The opening door reveals the art teacher, who steps in with his jacket swirling around him as though in a gust of wind."
"คุณครูศิลปะเปิดประตูเดินเข้ามาพร้อมเสื้อคลุมที่พลิ้วตามตัวราวกับว่ามีลมโบกพัด"

# "He glances at Mutou, who glances back at him."
"โนมิยะจ้องมุโต้ ส่วนมุโต้ก็จ้องกลับ"

play music music_tension

show muto irritated
show nomiya stern
with charachange

# "A frown spreads simultaneously on both of their faces as the men measure each other with their gazes."
"ทั้งคู่ทำหน้านิ่วคิ้วขมวดพลางประเมินกันและกัน"

# no "Excuse me, could I borrow Mr. Nakai for a moment?"
no "ขอประทานโทษนะ ขอยืมตัวนายนากาอิหน่อยได้มั้ย"

# mu "Excuse {b}me{/b}, Mr. Nomiya, but we are in the middle of an exam here."
mu "{b}ขอ{/b}ประทานโทษนะ คุณโนมิยะ แต่พวกเรากำลังสอบกันอยู่"

# "A chilly atmosphere suddenly spreads in the middle of the summer afternoon as the two men try to stare each other down."
"บรรยากาศเย็นเยือกแผ่ไปทั่วแทนที่อากาศยามบ่ายหน้าร้อน ทั้งสองคนจ้องตากันเขม็ง"

show nomiya serious
with charachange

# no "This is urgent, and it seems that Nakai has already finished."
no "พอดีมีเรื่องด่วนน่ะ แล้วก็ดูเหมือนว่านากาอิจะทำข้อสอบเสร็จแล้วด้วยนะ"

# "Both men turn to look at me, staring at me like a pair of basilisks trying to petrify a tasty snack."
"ทั้งสองคนหันมามองฉัน จ้องตาราวกับว่าเป็นตัวบาสิลิสก์ที่กำลังจะทำให้เหยื่ออันโอชะของมันแข็งเป็นหิน"

# "It's true that I've been idle for a good while now, so Nomiya is right, but…"
"ก็จริงอย่างที่โนมิยะบอก ฉันอยู่ว่าง ๆ มาได้สักพักแล้ว แต่ว่า…"

show muto normal
with charachange

# mu "Nakai, would you like to check your answers one more time?"
mu "นากาอิ อยากจะตรวจคำตอบตัวเองดูอีกครั้งไหม"

# "Mutou speaks with an odd intonation, weighting certain words as if trying to send a message."
"มุโต้พูดเน้นเสียงเน้นคำแปลก ๆ ราวกับว่าจะสื่อสารอะไรบางอย่าง"

# "The pressure from their stares makes me rapidly shake my head, which is apparently interpreted as an answer of some sort."
"แรงกดดันจากสายตาที่จับจ้องนั้นทำให้ฉันสั่นหัวรัว ๆ ซึ่งเหมือนจะถูกตีความไปเป็นคำตอบอะไรสักอย่างแล้ว"

stop music fadeout 6.0

show muto irritated
with charachange

# mu "Very well. Nakai, go with Mr. Nomiya, if you please."
mu "โอเค นากาอิ งั้นก็เชิญไปกับคุณโนมิยะได้เลย"

# mu "Take your bag with you and bring your test paper to my desk."
mu "เก็บกระเป๋าให้เรียบร้อย แล้วเอาข้อสอบมาวางไว้ที่โต๊ะครูนะ"

show muto smile
with charachange

# mu "You have a nice vacation."
mu "เที่ยวให้สนุก"

# hi "Umm. Er, you too, teacher."
hi "อ่า เอ้อ ครูก็ด้วยนะครับ"

# "The entire world… well, at least the classroom seems to hold its breath just for me, putting the exam on hold until I stand up, collect my stuff and walk to the door."
"ราวกับว่าทั้งโลก… อย่างน้อยก็ห้องฉันน่ะนะ ได้หยุดหายใจไว้เพื่อฉันและหยุดทำข้อสอบรอจนกว่าฉันจะยืนขึ้นเก็บ\nข้าวของเดินออกจากประตูไป"

# "I can feel the stares in the back of my neck. My classmates probably think I'm in for some detention or something, on the last day of the school before summer vacation."
"เหมือนมีสายตาที่จับจ้องไล่หลังมาเลย คนในห้องคงคิดว่าฉันโดนกักบริเวณหรืออะไรในวันสุดท้ายก่อนปิดเทอมฤดูร้อน\nแน่ ๆ"

# "I don't know what the teacher wants from me, but I can guess it probably is not detention and also that it probably has something to do with Rin again."
"ฉันไม่รู้ว่าคุณครูต้องการอะไรจากฉัน แต่ก็พอจะเดาได้ว่าคงไม่ใช่การกักบริเวณ แล้วก็คงจะเป็นเรื่องรินอีกตามเคย"

scene bg school_hallway3
with locationchange

play sound sfx_doorslam
with vpunch

# "Nomiya doesn't take me anywhere, contenting himself with the hallway as it's completely abandoned."
"โนมิยะไม่ได้นำฉันเดินไปที่ไหน เพราะแค่โถงทางเดินที่ไม่มีคนนี้ก็พอแล้ว"

show nomiya serious at center
with charaenter

play music music_pearly fadein 1.0

# no "Do you know where Tezuka is?"
no "รู้มั้ยว่าเทซูกะอยู่ไหน"

# "So she is trying to avoid the teacher… par for the course, probably."
"สรุปรินก็หลบหน้าคุณครู… ก็คงไม่น่าแปลกใจเท่าไหร่ละนะ"

# "I wonder if she realizes that she can't avoid dealing with this indefinitely."
"เธอจะรู้มั้ยนะว่าจะหนีปัญหานี้ไปเรื่อย ๆ ไม่ได้"

# hi "I have no idea."
hi "ไม่รู้เลยครับ"

# hi "You have probably asked in her homeroom next door."
hi "ไปถามครูประจำชั้นที่อยู่ห้องข้าง ๆ มาแล้วสินะครับ"

show nomiya stern
with charachange

# no "Of course I have! I have searched every nook and cranny of this blasted school and the girls' dorm."
no "ถามมาแล้วสิ! ฉันหาจนทั่วทุกซอกทุกมุมของโรงเรียนนี้แล้ว ทั้งหอหญิงด้วย"

# no "You are the last one to see her since yesterday and you are her friend."
no "เธอเป็นคนสุดท้ายที่เจอกับเทซูกะนับตั้งแต่เมื่อวาน แล้วก็เป็นเพื่อนด้วย"

show nomiya serious
with charachange

# no "Work with me here. Aren't you worried?"
no "ช่วยกันหน่อยสิ ไม่เป็นห่วงเทซูกะเหรอ"

# "I am, but I don't know what I could do."
"ก็ห่วง แต่ฉันไม่รู้ว่าจะทำอะไรได้"

# "Rin did something incomprehensible yesterday, even for her."
"เมื่อวานรินทำอะไรที่ยากจะเข้าใจ แม้แต่ตัวเธอก็ไม่เข้าใจ"

# "She seemed really confused."
"เธอดูสับสนมาก ๆ"

# hi "Maybe she just wants some time to think then. I got the feeling that she had second thoughts about having that exhibition."
hi "รินคงอยากได้เวลาไปคิดมั้งครับ รู้สึกเหมือนจะอยากไปคิดทบทวนอีกทีเรื่องงานนิทรรศการนั้น"

# "Or something. She really didn't explain what was wrong."
"หรืออะไรสักอย่าง เพราะเจ้าตัวก็ไม่ได้อธิบายว่าเป็นอะไร"

show nomiya frown
with charachange

# no "What second thoughts?"
no "มีอะไรให้คิดทบทวน?"

# hi "I dunno. Just got that feeling."
hi "ไม่รู้สิครับ แค่รู้สึกว่า"

# "I am being a little dishonest with the teacher, but this is not something I should be meddling with."
"ฉันโกหกกับคุณครูไปเล็กน้อย แต่เรื่องนี้ไม่ใช่อะไรที่ฉันจะต้องเข้าไปยุ่ง"

# "He came to me… yes, why? Maybe he thinks I'm some kind of confidant of Rin's, but I don't think I can help with this matter."
"คุณครูมาหาฉัน… ใช่ แต่ทำไม คงคิดว่าฉันเป็นผู้รักษาความลับอะไรของรินมั้ง แต่ฉันคงช่วยคุณครูเรื่องนี้ไม่ได้หรอก"

show nomiya serious
with charachange

# "The teacher huffs and scratches his head in confusion."
"คุณครูทำเสียงฮึดฮัดพลางเกาหัวด้วยความสับสน"

# no "What's up with that girl? This is so unlike her, she's always been so goal-driven."
no "แม่นั่นเป็นอะไรเนี่ย ปกติไม่เป็นอย่างนี้นี่ ออกจะเป็นคนมุ่งมั่นในเป้าหมายจะตาย"

# "“Goal-driven?” Those don't really strike me as words to describe Rin with."
"“มุ่งมั่นในเป้าหมาย”? ฟังดูไม่เหมือนคำที่จะใช้อธิบายรินเลย"

# "To me, she always felt obsessive at best."
"สำหรับฉัน อย่างมากเธอก็แค่เป็นคนหมกมุ่น"

# hi "Er, I don't mean to be rude, but wasn't it you who pushed Rin to that direction in the first place?"
hi "เอ้อ ว่าก็ว่าเถอะนะครับ แต่คนที่ ‘ผลัก’ รินให้ไปทิศทางนั้นแต่แรกก็ครูไม่ใช่เหรอครับ"

show nomiya dreamy
with charachange

# no "Her goal is my goal. That is a mentor's job."
no "เป้าหมายของเทซูกะก็คือเป้าหมายของฉัน นั่นละคืองานของที่ปรึกษา"

# hi "I guess so. I just don't know if painting can make her happy."
hi "คงงั้นมั้งครับ ผมแค่ไม่รู้ว่าการวาดรูปจะทำให้รินมีความสุขหรือเปล่า"

show nomiya stern
with charachange

# no "That's pretty preposterous of you to say, Nakai."
no "พูดอะไรไร้สาระนะเธอเนี่ยนากาอิ"

# "He suddenly sounds pretty irate. Did I say something stupid?"
"อยู่ ๆ เขาก็เสียงเขียวขึ้นมา นี่ฉันพูดอะไรโง่ ๆ ออกไปหรือเปล่า"

show nomiya serious
with charachange

# no "You don't understand, do you? It is not a question of happiness. For every gain there is a sacrifice to be made."
no "เธอไม่เข้าใจเลยใช่มั้ย ความสุขน่ะไม่ใช่ประเด็น ทุกอย่างที่ได้มาย่อมต้องเสียอะไรบางอย่างไป"

show nomiya stern
with charachange

# no "There is no free lunch, but could I… would I let that girl waste away her talent if she has a moment of doubt? Never!"
no "ของฟรีไม่มีในโลกหรอก แต่ฉันจะ… จะให้ฉันเอาความสามารถของคนคนหนึ่งไปทิ้งขว้างเพราะคนนั้นนึกลังเลขึ้นมา\nได้ไง ไม่มีทาง!"

# no "Painting is work just like any other. Tezuka might make it look like child's play to you, but she works hard every day to make her art."
no "การวาดรูปน่ะก็เป็นงานเหมือนกันนะ เทซูกะอาจจะวาดจนเธอเห็นเป็นเหมือนของเด็กเล่นก็จริง แต่ทุกวันเทซูกะ\nก็ทุ่มเทเพื่อผลงานของตัวเอง"

# no "To become extraordinary, one has to make an extraordinary effort."
no "คนเราจะเป็นคนที่ไม่ธรรมดาได้ ก็ต้องทุ่มเทให้มากเกินธรรมดา"

# "The more the teacher talks, the more I feel that Rin doesn't think like that, even though I have no idea how she thinks."
"ยิ่งคุณครูพูดก็ยิ่งรู้สึกว่ารินไม่ได้คิดอย่างนั้นเลย ถึงจะไม่รู้เลยว่ารินจะคิดยังไงก็เถอะ"

show nomiya serious
with charachange

# no "I can very well understand why she would sacrifice her summer vacation and make up for the lost classes and exams to get a chance at showing her art."
no "ฉันเข้าใจดีว่าทำไมเทซูกะถึงยอมสละช่วงปิดเทอมฤดูร้อนมาเรียนมาสอบทดช่วงที่ขาดไป แลกกับการที่จะได้มีโอกาส\nเอางานศิลปะของตัวเองออกมาแสดง"

# no "This is the path she has taken, and to go all the way, that's not easy."
no "นี่คือเส้นทางที่เทซูกะเลือก แล้วการที่จะไปให้ถึงที่สุดนั้นก็ไม่ง่าย"

# no "I know she is young, and things are hard for her just like for all the kids here in this school, but that's no excuse."
no "ฉันรู้ว่าเทซูกะอายุยังน้อย และลำบากเหมือน ๆ กับเด็กทุกคนในโรงเรียนนี้ แต่นั่นไม่ใช่ข้ออ้าง"

# "He is finished."
"เขาพูดจบแล้ว"

# hi "But—"
hi "แต่—"

show nomiya smile
with charachange

# no "Do you have anything like what art is to Tezuka?"
no "เธอมีอะไรเป็นสิ่งนั้นสำหรับเธออย่างที่ศิลปะเป็นสำหรับเทซูกะไหมล่ะ"

# hi "No…"
hi "ไม่ครับ…"

# "That's right. I have only vague ideas of my future, no goal to shoot for, no dream to blindly reach for."
"ใช่แล้ว ฉันมีเพียงภาพอนาคตแบบราง ๆ ไม่ได้มีเป้าหมายให้พุ่งไป ไม่ได้มีฝันให้ทะยานไปคว้า"

# "I joined the art club in search of something I could be interested in, to get inspired by."
"ฉันเข้าร่วมชมรมศิลปะมาเพื่อค้นหาบางอย่างที่ฉันอาจจะสนใจหรือมีแรงบันดาลใจให้ไล่ตาม"

# "Did I find something like that?"
"ฉันเจออะไรอย่างนั้นหรือเปล่า"

# "All I found in the end… was Rin."
"สุดท้าย สิ่งที่ฉันเจอ… คือริน"

# hi "No, I don't have a passion like that."
hi "ไม่ครับ ผมไม่ได้มีความหลงใหลอย่างนั้น"

show nomiya serious
with charachange

# no "Then you can't understand."
no "งั้นเธอก็ไม่เข้าใจหรอก"

# "His flat statement allows no counterargument."
"คำพูดเรียบ ๆ ของเขาไม่มีช่องให้แย้งได้"

# hi "But… she might not understand even herself."
hi "แต่… แม้แต่รินเองก็อาจจะยังไม่เข้าใจตัวเองเลยนะครับ"

# "Still, I carry on arguing, out of spite if for nothing else."
"แต่ฉันก็ยังคงเถียงข้าง ๆ คู ๆ ต่อไป"

show nomiya stern
with charachange

# no "How could she not? She's been at it so hard for the past few weeks that she put off even coming to school, not to say anything about attending class. Don't be ridiculous."
no "จะเป็นอย่างนั้นได้ไง สองสามสัปดาห์มานี้เทซูกะตั้งใจทำจนไม่มาโรงเรียนเลยด้วยซ้ำ ไม่ต้องพูดถึงเรื่องเข้าเรียนเลย\nอย่ามาพูดอะไรบ้า ๆ"

# "I don't think I'm being ridiculous, but as I have no rebuttal, Nomiya seems to consider this one his win."
"ฉันว่าฉันไม่ได้พูดบ้า ๆ นะ แต่ในเมื่อฉันไม่มีอะไรจะย้อน โนมิยะก็ดูจะนับไปว่าตัวเองชนะแล้ว"

show nomiya smile
with charachange

# no "At any rate, the opening was quite successful despite Tezuka hardly showing up."
no "แต่เอาเถอะ งานเปิดตัวประสบความสำเร็จทีเดียว ถึงเทซูกะจะไม่ค่อยได้อยู่งานก็เถอะ"

# no "Many people were interested in her work and one piece was even sold for a reasonable price."
no "หลายคนต่างก็สนใจผลงานของเทซูกะ มีภาพหนึ่งที่ขายได้ราคาพอตัวเลย"

# hi "Well, that's nice isn't it?"
hi "ก็ดีแล้วนี่ครับ"

show nomiya veryhappy
with charachange

# no "Yes, it's fantastic news! I hoped that Tezuka would come to her senses when she heard about this, but…"
no "ใช่ ข่าวดีมากเลยละ! หวังว่าถ้าเทซูกะได้รับข่าวนี้แล้วจะตื่นสักทีนะ แต่ว่า…"

# "He sighs and takes off his glasses, cleaning them against his jacket before putting them on his nose again."
"เขาถอนหายใจแล้วถอดแว่นมาเช็ดกับเสื้อคลุมก่อนจะใส่กลับอีกครั้ง"

show nomiya smile
with charachange

# no "At any rate, I should be going. There is this mess to be settled with Sae and everyone."
no "แต่เอาเถอะ ฉันต้องไปละ มีเรื่องต้องจัดการกับซาเอะแล้วก็คนอื่นอีก"

# no "If you see Tezuka, please ask her to come see me. Otherwise, have a nice vacation."
no "ถ้าเห็นเทซูกะก็บอกให้มาคุยกับฉันทีนะ แล้วก็ เที่ยวให้สนุก"

# hi "Thanks…"
hi "ขอบคุณครับ…"

stop music fadeout 6.0
play sound sfx_footsteps_hard
$ renpy.music.set_volume(0.0, 4.0, channel="sound")

hide nomiya
with charaexit

# "After he has disappeared around the corner, I ponder where Rin could really be."
"พอเขาลับตาหายไปแล้วฉันก็คิดว่ารินจะไปอยู่ที่ไหน"

# "It feels like she has not one, but at least half a dozen of these “secret places.”"
"เหมือนเธอจะไม่ได้มี “ที่ลับ” แค่หนึ่งที่ อย่างน้อย ๆ ก็คงมีสักหกเจ็ดที่ได้"

# "I balance between the desire to solve this tangle and to drop it for good."
"ฉันชั่งใจอยู่ว่าจะคิดแก้ปัญหานี้ต่อหรือจะล้มเลิกไปเลยดี"

# "The disused classroom is just a few feet away."
"ห้องเรียนที่ไม่มีคนใช้แล้วอยู่ห่างออกไปไม่ไกลนัก"

# "What to do?"
"ทำยังไงดี"

"…"

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_dooropen

scene bg school_room34
with locationchange

# "As I push open the door, only the shadows greet me from the inside."
"พอเปิดประตูเข้าไปก็มีเพียงเงาทั้งหลายในห้องที่ต้อนรับฉัน"

# hi "Hey there."
hi "นี่—"

#go to R38 (good end) from here

label th_R35:
#continued from R33
scene bg school_scienceroom
with None

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

# n "\n\nVacation, huh?"
n "\n\nปิดเทอมเหรอ"

# n "Some people will stay at the school even over the holidays, some will go back to their families."
n "ต่อให้โรงเรียนปิดแล้วบางคนก็จะยังอยู่ที่หอต่อ แต่ก็มีบางคนที่จะกลับไปหาครอบครัว"

# n "I probably should make the trip back home and report to my parents that I'm alive and well."
n "ฉันคงต้องกลับบ้านไปรายงานพ่อแม่ว่ายังสบายดีมีชีิวิตอยู่"

# n "\nNot much to do at the school anyway, I suppose."
n "\nอยู่โรงเรียนไปก็คงไม่มีอะไรให้ทำเท่าไหร่"

# n "Next trimester will be stressful. Everyone will have to seriously start thinking about what to do after graduation."
n "เทอมหน้าได้เครียดหนักแน่ ทุกคนจะต้องคิดอย่างจริงจังแล้วว่าจบไปแล้วจะทำอะไรต่อ"

# n "\n\nIncluding me…"
n "\n\nรวมถึงฉันด้วย…"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

scene ev rin_doodle_all
with silentwhiteout

window show

# "A look at my doodles convinces me to stop trying to salvage them. It's a mess of lifeless lines, a waste of paper if it wasn't the flip side of my exam."
"พอได้เห็นรูปที่เขียนเล่นแล้วก็ทำใจให้เลิกแก้ต่อได้สักที มีแต่เส้นไร้ซึ่งชีวิตที่ขีดทับกันไปมา ถ้าไม่ใช่ว่าเป็นหน้าหลัง\nของข้อสอบก็คงเสียดายกระดาษน่าดู"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

# n "\n\n\nMaybe it's because I didn't really set out to draw anything in particular."
n "\n\n\nบางทีอาจจะเพราะฉันไม่ได้ตั้งใจวาดอะไรแต่แรก"

# n "I just wanted to kill some time, so the drawing became exactly like I am."
n "ฉันแค่อยากวาดฆ่าเวลาเฉย ๆ รูปก็เลยออกมาเป็นเหมือนอย่างฉัน"

# n "Without a direction to go to."
n "ที่ไร้ซึ่งทิศทาง"

# n "\n\nIt'd be easier if I had some special talent, like Rin."
n "\n\nถ้าฉันมีพรสวรรค์อะไรอย่างรินบ้าง อะไร ๆ ก็คงง่ายกว่านี้"

# n "She has it easy."
n "รินน่ะเกิดมาสบาย"

# n "It makes me kind of jealous."
n "ฉันแอบอิจฉาอยู่เหมือนกัน"

# n "It pisses me off that she herself can't seem to be happy about it."
n "คิดแล้วก็หงุดหงิด ทำไมรินถึงดูไม่มีความสุขกับเรื่องนั้นเลยกันนะ"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

scene bg school_scienceroom
show muto smile at center
with locationskip

window show

# mu "Aaaand… time!"
mu "หมด… เวลา!"

# "Mutou's call for the end of the exam draws groans of displeasure from half the class."
"เสียงบอกหมดเวลาจากมุโต้ทำให้เกือบครึ่งห้องร้องโอดโอย"

# "I don't blame them, the exam was kinda tricky."
"ก็ว่าไม่ได้หรอก ข้อสอบมันเล่นแง่พอตัว"

# "Mutou expects a lot from our class, even though he's not strict at all. I guess he'd like all of us to become scientists."
"มุโต้คาดหวังกับห้องเราสูงมาก ถึงจะไม่ได้เคร่งก็เถอะ สงสัยคงอยากให้ทุกคนได้เป็นนักวิทยาศาสตร์ละมั้ง"

show muto normal
with charachange

# mu "Put down your pencils and turn in your papers please."
mu "วางดินสอลงแล้วมาส่งข้อสอบด้วย"

# "The biggest groan comes from the desk to my side."
"เสียงโอดโอยที่ดังที่สุดดังมาจากโต๊ะข้าง ๆ"

show misha invis_close:
    center
    xpos -0.2
    ypos 1.13
with None

show bg school_scienceroom at bgright
show muto normal at tworight
show misha perky_sad_close:
    xpos 0.15
with dissolvecharamove

# "Misha's despair is almost tangible."
"ความสิ้นหวังของมิช่านั้นแทบจะจับต้องได้"

# "The dark aura of lost hope emanating from her seat makes me simultaneously frightened of and sympathetic to her."
"รังสีมืดมนที่แผ่ออกมาจากโต๊ะเธอนั้นทำฉันทั้งกลัวและทั้งสงสารไปพร้อม ๆ กัน"

show muto smile
with charachange

# mu "Now then, there should be homeroom before you are free, but I only have a few announcements to make so this should be over quickly…"
mu "เอาละ จริง ๆ จะมีคาบโฮมรูมก่อนปล่อย แต่ฉันมีเรื่องจะแจ้งไม่มาก เพราะงั้นก็คงไม่นาน…"

# "His announcements are never important, so I listen to him only with one ear."
"เรื่องที่เขาแจ้งนั้นไม่เคยสำคัญอยู่แล้ว ฉันจึงใช้หูข้างเดียวฟัง"

# "Misha seems to be too down in the dumps to even pretend attentiveness."
"มิช่าดูจะซึมกะทือเกินกว่าจะทำเป็นฟังอยู่ได้ด้วยซ้ำ"

# "She slumps her head against the desktop, looking stricken."
"เธอก้มหัวฟุบโต๊ะดูหดหู่"

# hi "Cheer up, Misha."
hi "ร่าเริงหน่อยมิช่า"

# hi "It's vacation! Don't worry about the test."
hi "ปิดเทอมแล้ว! อย่าคิดมากเรื่องสอบเลย"

show misha sign_smile_close
with charachange

# mi "Thanks, Hicchan."
mi "ขอบใจนะฮิจัง"

# "Her frown becomes a small smile, and a sparkle of excitement lights in her eyes."
"คิ้วที่ขมวดของเธอคลายลงเป็นรอยยิ้ม พร้อมประกายความตื่นเต้นในแววตา"

show misha perky_smile_close
with charachange

# mi "What're you going to do over your summer vacation, Hicchan?"
mi "ปิดเทอมนี้นายจะทำอะไรเหรอฮิจัง"

show misha hips_smile_close
with charachange

# mi "I'm going to Shicchan's place, they have this awesome and super cool mansion! I'm so excited~!"
mi "ฉันจะไปบ้านชิจังละ เป็นคฤหาสน์หรู ๆ สุดเจ๋งด้วย! ตื่นเต้นจัง~!"

show misha hips_grin_close
with charachange

# mi "I'm sure it'll be the bestest summer vacation ever~!"
mi "ต้องเป็นปิดเทอมฤดูร้อนแสนยอดสุดแน่ ๆ ~!"

# "She seems to have forgotten all about her misery in a few seconds and bounces up and down on her seat as if to pump up her excitement."
"ดูท่าว่าจะลืมความหดหู่อะไรไปแล้วได้ภายในสองสามวินาที เธอเด้งตัวขึ้นลงกับที่นั่งราวกับจะปั๊มลมความตื่นเต้นเข้าตัว"

# hi "I don't really have any plans, I guess…"
hi "ฉันก็ไม่มีอะไรเป็นพิเศษละมั้ง…"

show misha sign_smile_close
with charachange

# mi "Is that so~? Maybe you should—"
mi "งั้นเหรอ~ หรือว่านาย—"

show misha perky_confused_close
with charachange

# "A finger tapping her shoulder steals Misha's attention away from me."
"นิ้วที่แตะ ๆ ไหล่มิช่าดึงความสนใจเธอไปจากฉัน"

show muto irritated
with charachange

# "Shizune points to Mutou, who is expectantly looking back at the two of them."
"ชิซูเนะชี้ไปทางมุโต้ที่มองมาทางสองคนนั้นเหมือนรออะไรอยู่"

show misha sign_confused_close
with charachange

# mi "Oops! Sorry, Shicchan, I didn't notice teacher finished already, ehehe~."
mi "โอ๊ะ! ขอโทษทีนะชิจัง ฉันไม่ทันสังเกตน่ะว่าครูพูดจบแล้ว เอะเฮะ ๆ ~"

# "She clears her throat and takes a deep breath…"
"มิช่ากระแอมแล้วสูดหายใจเข้าลึก ๆ …"

show misha hips_grin_close:
    ypos 1.0
with dissolvecharamove

# mi "Stand!"
mi "ทุกคน ลุก!"

# "I stand up with everyone."
"ฉันยืนขึ้นพร้อมทุกคน"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

# n "\n\nSince I came here, I've always wondered about something."
n "\n\nตั้งแต่ฉันได้มาเรียนที่นี่ ฉันสงสัยอยู่อย่างหนึ่งมาตลอด"

# n "What do the wheelchair-bound students think about this daily tradition, being unable to do it “properly?”"
n "ว่านักเรียนที่นั่งวีลแชร์จะคิดยังไงกับธรรมเนียมการทำความเคารพประจำวันนี้ เพราะตัวเองนั้นทำอย่าง “ถูกต้อง” ไม่ได้"

# n "Is it a faux pas to keep to this tradition in a place that bypasses many others for convenience?"
n "เขาถือหรือเปล่ากับการที่รักษาธรรมเนียมแบบนี้ไว้เพื่อความสะดวก ทั้งที่เป็นธรรมเนียมที่มองข้ามหลายคนไป"

# n "Even though I never asked anyone, during these short weeks here I've come to the conclusion that they definitely are not insulted."
n "ถึงฉันจะไม่เคยถามใคร แต่พอดูจากสองสามสัปดาห์ที่ผ่านมาแล้ว ฉันก็คิดได้ว่าพวกเขาไม่ถือแน่นอน"

# n "They understand."
n "พวกเขาเข้าใจ"

# n "That's what I like about this school. Nobody is too uptight about anything, everyone is so… considerate and understanding of each other."
n "เพราะอย่างนี้ฉันถึงได้ชอบยามากุ ไม่มีใครเคร่งอะไรจนเกินไป ทุกคนต่าง… คิดถึงใจของกันและกันและเข้าใจกัน"

stop music fadeout 4.0

# n "\n\nI wish the whole world could be like this."
n "\n\nฉันอยากให้ทั้งโลกเป็นอย่างนี้บ้าง"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

scene black
with locationchange

window show

# mi "Booooow!"
mi "ทำความเคาาารพ!"

scene bg school_dormhisao
with shorttimeskip

play sound sfx_paper
play music music_tranquil fadein 3.0

# "I turn the page slowly, listening to the rustling sound the paper makes when my fingers grasp it."
"ฉันพลิกหน้ากระดาษไปช้า ๆ คอยฟังเสียงกรอบแกรบเวลาฉันจับหน้ากระดาษ"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

# n "\nI'm restless."
n "\nกระวนกระวายใจเหลือเกิน"

# n "It's the summer vacation."
n "ปิดเทอมฤดูร้อน"

# n "No class, no homework, no art club meetings. Just free time to spend however I want."
n "ไม่มีเรียน ไม่มีการบ้าน ไม่มีกิจกรรมชมรมศิลปะ มีแต่เวลาว่างที่ฉันจะเอาไปทำอะไรก็ได้"

# n "It doesn't feel like anything."
n "ไม่ได้รู้สึกพิเศษอะไรเลย"

# n "I tried to cheer up Misha, but I'm not feeling too cheery myself."
n "ฉันบอกให้มิช่าร่าเริง แต่ตัวฉันไม่ได้ร่าเริงเท่าไหร่"

# n "To be honest, the free time is intimidating. It reminds me of the hospital and the long, meaningless days that had to be filled somehow."
n "เอาจริง ๆ เวลาว่างแบบนี้ก็น่ากลัว ชวนให้นึกถึงวัน ๆ อันยืดยาวไร้จุดหมายในโรงพยาบาลที่ฉันต้องคอยใช้ให้หมด"

# n "The only difference is that there I was bound to the ward, guarded by the Cerberus-like nurses."
n "ความต่างเดียวคือตอนอยู่ที่นั่นฉันถูกกักให้อยู่ติดวอร์ดโดยมีพยาบาลที่เป็นเหมือนหมาที่เฝ้าประตูนรกคอยคุ้มกันอยู่"

# n "Reading was a good solution back then, but the thought of spending my summer vacation reading books feels… nerdy."
n "ตอนนั้นการอ่านถือเป็นทางออกที่ดี แต่พอคิดว่าต้องมาอ่านหนังสือตอนปิดเทอมแล้วก็รู้สึกเหมือน… พวกเด็กเรียน"

# n "That has nothing to do with the fact that I'm reading even now… I'm just killing time and trying to fight my anxiety."
n "แต่ไม่เกี่ยวกับการที่ตอนนี้ฉันอ่านหนังสือหรอกนะ… ฉันแค่ฆ่าเวลาไปไม่ให้ตัวเองเป็นกังวล"

# n "Besides, my mind is on other matters, stretching in too many directions to make sense of any of them."
n "อีกอย่าง สมองฉันคิดเรื่องอื่นอยู่ ลอยไปคนละทิศละทางจนเกินกว่าจะเข้าใจได้"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

window show

# "Thus, the book I've been on since Tuesday is progressing s{w=0.3}l{w=0.3}o{w=0.3}w{w=0.3}l{w=0.3}y{w=0.3}."
"และเหตุเช่นนั้นเอง หนังสือที่ฉันอ่านมาตั้งแต่เมื่อวันอังคารจึงดำเนินไปอย่าง{w=0.3}เ{w=0.3}ชื่{w=0.3}อ{w=0.3}ง{w=0.3}ช้{w=0.3}า"

# "It feels like this book is taking me longer to read than it took the author to write."
"รู้สึกเหมือนจะอ่านช้ากว่าที่คนเขียนเขียนได้อีก"

# "I try to put it down for a while, then read some again, start all over from the beginning, read each page twice."
"ฉันพักไว้สักพัก แล้วก็อ่านต่อ เริ่มใหม่ตั้งแต่ต้น อ่านแต่ละหน้าซ้ำสองรอบ"

# "Nothing works, I have zero concentration."
"ไม่มีอะไรที่ได้ผลเลย สมาธิจดจ่อฉันเป็นศูนย์"

# "Taking it with me just in case, I head out to get some fresh air and inspiration as to what to do."
"ฉันหยิบหนังสือติดมือมาแล้วออกมาสูดอากาศข้างนอกเผื่อนึกหาอะไรทำออก"

scene bg school_courtyard
with locationskip

# "I make my way to the quad, passing by students heading for the gates."
"ฉันเดินไปยังลานหน้าโรงเรียน เดินผ่านนักเรียนสองสามคนที่ออกประตูหน้าไป"

# "The hastiest ones are leaving for their homes already, judging from the luggage some are dragging with them."
"คนที่รีบก็คงเตรียมตัวกลับบ้านกันแล้ว ดูจากกระเป๋าสัมภาระที่บางคนลากไปด้วย"

# "I guess that no matter how hospitable Yamaku is, home is still home. Still, I heard some people will be staying here over the vacation."
"ไม่ว่ายามากุจะมีบริการที่ดีแค่ไหน แต่บ้านก็คือบ้านละนะ แต่ก็ได้ยินมาเหมือนกันว่าบางคนจะอยู่ที่นี่ตอนปิดเทอมด้วย"

# "The quad is big enough for its center to be shadowless no matter how high or low the sun is."
"ลานหน้าโรงเรียนนั้นกว้างพอที่จะไม่ให้มีเงาส่อง ไม่ว่าแดดจะอยู่สูงหรือต่ำแค่ไหนก็ตาม"

# "I stop in the middle and bask in the warmth."
"ฉันหยุดยืนอยู่กลางลานแล้วซึมซับความอบอุ่น"

# "The brightness makes me squint my eyes when I look towards the main building."
"แสงจ้าจนต้องหรี่ตาตอนมองไปที่อาคารหลัก"

# "It looks all but abandoned already."
"ดูแล้วก็ไม่มีใครเลย"

# "Yuuko wasn't at work today, so the next time I can get books from the school library is after vacation."
"ยูโกะไม่มาทำงานวันนี้ เพราะงั้นจะไปหาหนังสือจากห้องสมุดโรงเรียนได้อีกทีก็คงเปิดเทอมเลย"

# "There is a public library somewhere, I'm sure, but I'm feeling too lethargic to find out where it is."
"ฉันมั่นใจว่าแถวนี้ต้องมีห้องสมุดประชาชนแน่ ๆ แต่ก็ขี้เกียจเกินกว่าจะไปหาว่าอยู่ที่ไหน"

scene bg school_lobby
with locationskip

# "The hall is equally dead so I have to content myself with returning to the dorms, ending my leisurely walk sooner than I expected."
"ที่โถงทางเดินก็เงียบพอกัน ฉันจึงจำใจต้องกลับหอ การเดินเล่นวันนี้ของฉันจบลงเร็วกว่าที่คาด"

# "Then again, I wasn't quite sure what I was expecting in the first place."
"แต่ก็นะ ไม่รู้เหมือนกันว่าคาดหวังอะไรอยู่"

scene bg school_girlsdormhall
with locationskip

# "On a moment's impulse I enter the girls' dorm to see if Rin or Emi are there."
"แวบหนึ่งฉันนึกเดินเข้าหอหญิงเพื่อไปดูว่ารินหรือเอมิอยู่หรือเปล่า"

# "Neither is, so I go back to my own room to dwell on my lethargy."
"ทั้งสองคนที่ว่าไม่อยู่ ฉันจึงได้แต่กลับมานอนอืดอยู่ในห้องตัวเอง"

window hide

scene bg school_dormhisao
with locationskip

$ renpy.music.set_volume(0.5, 1.0, channel="music")

nvl clear
nvl show dissolve

# n "\n\nI should talk things through with Rin."
n "\n\nฉันต้องจบเรื่องกับริน"

# n "She really bothers me."
n "รินกวนใจฉันมาก ๆ"

# n "\n\nDefying the conceptual equivalent of gravity, she balances on the thin line zigzagging between insanity, incomprehensibility and instability."
n "\n\nรินยืนอยู่บนเส้นด้ายประคองตัวเองไม่ให้ล้มไปกับสิ่งที่เหมือนกับแรงโน้มถ่วงโดยเดินสลับไปมาระหว่างความบ้า\nความเข้าใจยาก และความไม่สมดุล"

# n "Rin affects me too. She challenges me in ways that I didn't know… or more accurately, didn't hope existed."
n "รินก็มีผลกับฉันด้วย เธอท้าทายฉันในแบบที่ฉันไม่เคยรู้มาก่อน… หรือจะพูดให้ถูกก็คือ แบบที่ฉันไม่หวังจะให้มี"

# n "\n\nI've started to wonder whether these feelings are really love, or I was just fooling myself."
n "\n\nฉันชักสงสัยว่าความรู้สึกเหล่านี้คือความรักจริง หรือฉันหลอกตัวเองอยู่"

# n "Surely, it would be insanity to consider that?"
n "ฉันคงบ้าน่าดูที่คิดอะไรอย่างนั้น"

nvl clear

# n "\n\nFor the rest of the day, Rin, the hospital, Yamaku and vacation swirl through my head."
n "\n\nวันนั้นทั้งวันที่เหลือ เรื่องริน โรงพยาบาล ยามากุ และปิดเทอมต่างวนเวียนอยู่ในหัว"

# n "\nI can't concentrate even on concentrating."
n "\nจะให้จดจ่อกับการจดจ่อยังไม่ได้เลย"

# n "\nThoughts seem to come and go haphazardly, fragmented into too-small pieces of cognition."
n "\nความคิดผ่านมาแล้วก็ผ่านไปแบบชั่วแวบหนึ่ง เป็นเพียงเศษความรำลึกชิ้นเล็ก ๆ"

# n "\nI pick up the book and manage to read a hundred pages, but I'm sure by tomorrow I'll have no recollection of what happened in the story."
n "\nฉันหยิบหนังสือมาอ่านได้หนึ่งร้อยหน้า แต่วันพรุ่งนี้ฉันคงจำไม่ได้แล้วว่าเรื่องเป็นยังไงบ้าง"

# n "\nI try to clean up my room, but even that proves to be too bothersome, too time-consuming and requiring too much attention to detail."
n "\nฉันลุกขึ้นมาเก็บกวาดห้อง แต่แล้วก็ขี้เกียจ แถมยังต้องใช้เวลาและความใส่ใจในรายละเอียดอีก"

# n "It's usually like this. When you have “nothing to do,” you do nothing even if you could."
n "เป็นอย่างนี้ประจำเวลา “ไม่มีอะไรทำ” ที่ต่อให้มีอะไรทำก็จะไม่ทำ"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

scene bg school_dormhisao_blurred_ss
show phone mobile at center
with shorttimeskip

window show

# "As expected, mom calls me and I end up promising to see if I can get a train ticket for tomorrow, or failing that, the day after."
"ตามคาด แม่โทรมาหา แล้วฉันก็รับปากไปแล้วด้วยว่าวันพรุ่งนี้จะไปหาซื้อตั๋วรถไฟ หรือถ้าไม่ได้ก็จะไปหาซื้ออีกที\nวันมะรืนนี้"

window hide
nvl clear

show phone mobile:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with None

scene bg school_dormhisao_ss
show phone mobile:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with locationchange
with Pause (0.5)

hide phone
with None

$ renpy.music.set_volume(0.5, 1.0, channel="music")

nvl show dissolve

# n "\n\nMaybe I'll go downtown tomorrow anyway. I could do some shopping or something."
n "\n\nวันพรุ่งนี้ไปเข้าตัวเมืองแล้วกัน เผื่อไปแวะซื้อของไปอะไรด้วย"

# n "It's not that I need anything, but maybe there are summer sales, and I could pick up… something."
n "ไม่ได้มีอะไรที่ต้องซื้อหรอก แต่เผื่อว่ามีของลดราคาหน้าร้อน แล้วก็อาจจะไปแวะซื้อ… อะไรสักอย่าง"

stop music fadeout 10.0

# n "\n\n…Why am I trying to force myself?"
n "\n\n…ทำไมต้องฝืนตัวเองขนาดนี้"

# n "Before, I was content with having nothing to do, save for kicking the ball every now and then at the field."
n "ก่อนหน้านี้เวลาไม่มีอะไรทำก็ไม่เป็นอะไรแท้ ๆ ถ้าไม่นับที่ว่านาน ๆ ทีจะไปเตะบอลที่สนามน่ะนะ"

# n "Now it seems that I can't settle down at all."
n "ตอนนี้ฉันสงบใจไม่ได้เลย"

# n "\nIs it because I have changed, or because my world has changed?"
n "\nเพราะฉันเปลี่ยนไป หรือเพราะโลกของฉันเปลี่ยนไป?"

nvl hide dissolve
nvl clear

scene bg school_dormhisao_ni
with shorttimeskip

window show

# "By eleven, the darkness bids me to sleep."
"พอถึงห้าทุ่มความมืดมิดก็ส่งสัญญาณว่าฉันควรนอน"

window hide

show pills:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

window show

# "The medication bottles are innocuously arranged on my night table, not at all beckoning, rather pointedly reminding me of the reality instead."
"ขวดยาที่วางเรียงรายอยู่บนโต๊ะหัวเตียงดูไร้พิษภัยเหล่านั้นไม่ได้กวักมือเรียกฉัน หากแต่ชี้นิ้วใส่ย้ำเตือนถึงความเป็นจริง"

# "It's evening so I have to open three bottles, extract one large oval-shaped one, two small round ones and one large flat that has to be cut into half, close the bottles and chug down the medications with a chaser of fresh tap water."
"ตอนนี้ตอนค่ำ ฉันต้องเปิดสามขวด เขย่าแต่ละขวดให้เม็ดยาที่เป็นเม็ดรี ๆ ออกมาหนึ่งเม็ด เม็ดกลม ๆ สองเม็ด แล้วก็\nเม็ดแบน ๆ หนึ่งเม็ดที่ต้องหักครึ่งก่อนกิน จากนั้นฉันปิดฝาแต่ละขวดแล้วกินยาทั้งหมดเข้าไปพร้อมกระดก\nน้ำประปาตาม"

window hide

show pills:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide pills
with None

window show

# "The water tastes metallic on my tongue."
"น้ำนั้นรสเฝื่อน ๆ"

# "I swallow it along with the pills anyway and head to the bathroom."
"ฉันกลืนน้ำไปพร้อมกับยาแล้วเดินไปที่ห้องน้ำ"

scene bg school_dormbathroom
with locationskip

# "The mindless job of brushing my teeth is fit for trying to sort my thoughts."
"การแปรงฟันนั้นเป็นไปโดยอัตโนมัติ จึงเหลือพื้นที่สมองให้ฉันได้จัดระเบียบความคิด"

# "One emerges from the mass, clearly rising above the others."
"มีความคิดหนึ่งที่โผล่ลอยเด่นเห็นชัดขึ้นมาจากกอง"

window hide
nvl clear
nvl show dissolve

# n "\n\n\n\n\n\n\n\n\nI want to see Rin."
n "\n\n\n\n\n\n\n\n\nฉันอยากไปเจอกับริน"

# n "I can't let my outburst of anger be the last thing between us before the vacation."
n "ฉันจะให้ความโกรธของฉันที่ระเบิดออกเป็นสิ่งสุดท้ายที่ค้างคาระหว่างเราก่อนปิดเทอมไม่ได้"

nvl hide dissolve
nvl clear

scene bg school_dormhisao_ni
with locationskip

nvl show dissolve

# n "\n\n\n\n\n\n\n\nI have to see her, tomorrow."
n "\n\n\n\n\n\n\n\nฉันต้องไปเจอกับริน พรุ่งนี้"

# n "Sleep overcomes my confused mind with more ease than it should."
n "ฉันหลับไปพร้อมความสับสนได้ง่ายกว่าอย่างที่ควรจะเป็น"

nvl hide dissolve
nvl clear

$ suppress_window_before_timeskip = True

scene black
with shuteye


label th_R36:


$ renpy.music.set_volume(1.0, 0.0, channel="music")
$ renpy.music.set_volume(0.7, 0.0, channel="ambient")
play ambient sfx_rain fadein 1.0

scene bg misc_sky_rn
show rain normal
show hisaowindow
with locationchange

# "Rain is falling on my summer vacation like an uncountable number of small bad omens."
"ฝนตกในวันปิดเทอมฤดูร้อน จำนวนเม็ดฝนมากมายคล้ายลางบอกเหตุร้ายเล็ก ๆ หลายอย่าง"

# "Luckily I'm not superstitious, but the bad weather makes me downcast too."
"โชคดีที่ฉันไม่เชื่อเรื่องอะไรอย่างนั้น แต่อากาศที่แย่อย่างนี้ก็ทำฉันหมองเหมือนกัน"

# "It's been like this since morning and there is no end in sight."
"ฝนตกมาตั้งแต่เช้าโดยไม่มีทีท่าว่าจะหยุด"

# "An impenetrable gray mass of clouds shadows the sky as much as it shadows my mood."
"เมฆใหญ่สีเทาทะมึนบดบังท้องฟ้าให้มืดหม่นไม่ต่างอะไรกับอารมณ์ของฉัน"

# "In a bout of defiance, I finished cleaning up this morning, but after that was done I ended up staring out of the window in hope of the weather clearing."
"เช้านี้ฉันลองเปลี่ยนอารมณ์มาเก็บกวาดห้องบ้าง แต่พอทำเสร็จแล้วก็ได้แต่มานั่งมองหน้าต่างรอให้อากาศดีขึ้น"

# "The incessant drumming of rainfall against the roof and the pavement is mesmerizing, a droning background noise to lose your mind into."
"เสียงฝนโปรยปรายกระทบกับหลังคาและทางเดินนั้นชวนฟัง เป็นเสียงกล่อมที่ปล่อยให้ใจลอยไปได้ดี"

"…"

"… …"

$ renpy.music.set_volume(0.4, 1.0, channel="ambient")

scene bg school_dormhisao_rn
with locationchange

# "This won't do, I have to get a move on."
"ไม่ดีแน่ ต้องทำอะไรสักอย่าง"

# "Should I pack now, or later?"
"เก็บของตอนนี้ดีเลยมั้ยนะ หรือยังก่อน"

$ renpy.music.set_volume(0.2, 1.0, channel="ambient")

scene bg school_dormhallway
with locationchange

# "I decide on the latter and make my way outside, pausing briefly at Kenji's door to listen to the odd clunking sounds from the other side."
"ฉันเลือกที่จะพักเรื่องเก็บของไว้ก่อนแล้วเดินออกมาข้างนอก จากนั้นก็มาหยุดยืนอยู่หน้าห้องเคนจิครู่หนึ่ง ในห้อง\nมีเสียงกุกกักแปลก ๆ อยู่"

show rain normal behind bg 
with None

# "I don't dare to knock, out of the fear of finding out what he is doing."
"ฉันไม่กล้าเคาะเพราะกลัวจะไปเห็นเข้าว่าเขาทำอะไรอยู่"

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

show bg school_dormext_full_rn as bg2 behind rain
hide bg
with locationskip

# "Braving the rain from under my trusty umbrella, I cross the space to the girls' dorm."
"ฉันกางร่มเดินฝ่าฝนไปยังหอหญิง"

$ renpy.music.set_volume(0.2, 1.0, channel="ambient")

scene bg school_girlsdormhall
with locationskip

play sound sfx_doorknock2

# "Knocking on Rin's door yields no answer, but the door behind me opens instead."
"ไม่มีเสียงตอบรับหลังเคาะประตูห้องริน แต่ประตูห้องที่อยู่ข้างหลังฉันเปิดออกแทน"

play sound sfx_dooropen

show emicas invis:
    center
    xpos 0.3
with None

show emicas happy at center
with dissolvecharamove

play music music_emi fadein 0.5

# emi "Hisao? Hi!"
emi "ฮิซาโอะเหรอ ไง!"

show emicas awayfrown
with charachange

# emi "Terrible weather. I even missed my morning jog."
emi "อากาศแย่เนอะ ฉันอดไปวิ่งรอบเช้าเลย"

# "She frowns, but I would be glad if I was her. Emi's morning jogs are anything but leisurely."
"เธอขมวดคิ้ว แต่ถ้าเป็นฉันคงดีใจ วิ่งรอบเช้าของเอมิเป็นอะไรที่หนักหนาเหลือเกิน"

# hi "Oh, hi, I was—"
hi "อ้อ ไง พอดีฉัน—"

show emicas neutral
with charachange

# emi "If you're looking for Rin, I don't think she is there."
emi "ถ้าจะมาหาริน ฉันว่าไม่น่าอยู่นะ"

# hi "Have you seen her recently?"
hi "ช่วงนี้เจอรินมั้ย"

show emicas grin_up
with charachange

# emi "Yeah, just this morning when I woke her up."
emi "อื้ม เพิ่งปลุกให้เมื่อเช้านี่เอง"

# "The mention of waking up makes Emi yawn like a cat, and makes me feel silly."
"พอพูดถึงปลุกแล้วเอมิก็หาวเหมือนแมว ดูแล้วก็ขำดี"

# "Of course she has seen Rin. Emi wakes her up and helps her get dressed on most mornings, even makes her lunch boxes every now and then."
"แหงอยู่แล้วว่าเอมิต้องเจอริน เอมิมาปลุกรินแล้วก็ช่วยแต่งตัวให้ทุกเช้า แถมบางทีก็ห่อข้าวเที่ยงไปให้ด้วย"

# "They are like sisters, even though they seem to have nothing in common."
"เหมือนเป็นพี่น้องกันเลย ถึงจะดูไม่มีอะไรที่เหมือนกันก็เถอะ"


label th_R36a:
#If not seen R19a:
# "I wonder which one is the elder sister? Probably Emi, against all odds."
"ใครจะเป็นคนพี่นะ อาจจะเหมือนไม่ใช่ แต่ก็คงจะเอมิละมั้ง"

# "She is really diligent, even though she gives the feeling of someone who would be a total airhead."
"เอมิเป็นคนขยันจริง ๆ ถึงดูแล้วเหมือนจะเป็นพวกซื่อบื้อมากกว่าก็เถอะ"

# "Why does it feel odd that she is so dutiful under that cheery grin of hers?"
"ทำไมพอได้เห็นความขยันที่อยู่ภายใต้รอยยิ้มร่าเริงของเธอแล้วถึงรู้สึกแปลก ๆ กันนะ"
#End split. -SC


label th_R36x:

show emicas frown_up
with charachange

# emi "She left for the gallery a few hours ago… hey, are you listening?"
emi "เห็นสองสามชั่วโมงก่อนออกไปหอศิลป์… นี่ ฟังอยู่หรือเปล่า"

# "Maybe I'm making a funny face or something, since Emi tilts her face quizzically, looking at me with her eyes round and inquisitive."
"สงสัยฉันคงทำหน้าตลกหรืออะไร เอมิเอียงคอมองด้วยดวงตากลมโตคู่นั้นด้วยความสงสัยใคร่รู้"

show emicas neutral
with charachange

# emi "Hmm?"
emi "หืมม?"

# "Her innocent face seems to request my attention."
"ใบหน้าอันใสซื่อของเธอคล้ายเรียกความสนใจจากฉันอยู่"

# hi "Yeah, I'm listening…"
hi "อื้ม ฟังอยู่…"

show emicas weaksmile
with charachange

# emi "Can I ask you a question?"
emi "ขอถามอะไรอย่างสิ"

# hi "Yeah, of course."
hi "อ่าฮะ ว่ามา"

show emicas awayfrown
with charachange

# "She furrows her brow, licking her lips as if to prepare for something."
"เธอขมวดคิ้วแล้วเลียริมฝีปากคล้ายเตรียมการอะไรอยู่"

show emicas frown
with charachange

# emi "Why do you care so much about Rin?"
emi "ทำไมถึงเป็นห่วงรินขนาดนี้"

show emicas neutral
with charachange

# emi "I mean, you probably hang around her more than I do, and we even slept in the same bed sometimes until, er, lately."
emi "คือ นายก็คงได้อยู่กับรินบ่อยกว่าฉันแหละ ขนาดบางทีฉันกับรินยังนอนเตียงเดียวกันเลยนะ แต่เอ่อ ช่วงนี้ไม่ได้นอน\nด้วยกันแล้ว"

# hi "After she banned you because you ravaged her hair?"
hi "ที่รินห้ามเธอนอนด้วยเพราะไปยีผมเล่นใช่มั้ย"

show emicas blush
with charachange

# "A shock of horror widens Emi's eyes at least twofold, making them seem even more saucer-like than usual, while a healthy blush rises on her cheeks and ears."
"ตาเอมิเบิกโพลงใหญ่ขึ้นด้วยความตกใจสักสองเท่าเห็นจะได้ ดูแล้วยิ่งตาโตกว่าปกติเข้าไปอีก แก้มเธอแดงอมชมพูไป\nจนถึงหู"

show emicas angry_up
with charachange

# emi "She told?! Ohhh… I'm going to strangle that Rin or something other horrible…"
emi "นี่รินบอกเหรอ! หน็อย… สักวันต้องไปบีบคอรินหรืออะไรหนัก ๆ แล้ว…"
#Not 100% grammatical, but leaving as is to represent unfolding thought processes. -SC

# "I hold back my laughter, lest she direct her disdain at me."
"ฉันกลั้นขำไม่ให้เธอพาลโกรธฉันไปด้วยอีกคน"

show emicas closedsmile
with charachange

# "Emi recuperates quickly from the embarrassment and seems to forgive Rin in the same instant, getting her focus back on me."
"เอมิรักษาหน้าจากความอับอายได้ทันที และดูเหมือนจะให้อภัยรินไปแล้วด้วย เธอหันกลับมามองฉัน"

show emicas smile
with charachange

# emi "Anyway, are you in love with her or something?"
emi "แต่นั่นแหละ นี่นายไปตกหลุมรักรินเข้าแล้วหรืออะไร"

# "Uh oh. This really feels like an elder sister questioning a suitor. Emi is kinda nosy, and not in a good happy way, if there even is one to begin with."
"เอ่อ อ่า เหมือนพี่สาวที่ถามคนที่มาตามจีบน้องเลย เอมิเป็นคนสอดรู้พอตัว แล้วก็ไม่ใช่สอดรู้แบบดี ๆ ด้วย ถ้ามันมี\nแบบนั้นน่ะนะ"

# "She'd make a good partner for Misha, to be honest. The horror."
"เอาจริง ๆ ถ้าได้อยู่กับมิช่านี่คงเข้าขากันดี แค่คิดก็สยอง"

# hi "That's already your second question, so I don't think I have to answer."
hi "เธอถามครบหนึ่งอย่างไปแล้ว อันนั้นคำถามที่สอง ฉันคงไม่ต้องตอบหรอก"

# "I try to conjure up a front made of pure, crystallized cool and uninvolvement."
"ฉันปั้นสีหน้าให้ดูใสซื่อบริสุทธิ์ผุดผ่องไม่ข้องเกี่ยวใด ๆ"

# "I wonder whether I manage to fool even myself."
"เผลอ ๆ จะหลอกตัวเองไปแล้วด้วย"

show emicas evil
with charachange

# "At least Emi is waggling her eyebrows dangerously, with a nasty smirk on her lips."
"แต่เอมิก็ยักคิ้วดูอันตราย ประดับพร้อมรอยยิ้มเจ้าเล่ห์ที่อยู่บนใบหน้าเธอ"

# emi "Is that a yes?"
emi "แปลว่าใช่ละสิ"

# hi "No, it's not a yes."
hi "ไม่ ไม่ได้แปลว่าใช่"

show emicas neutral
with charachange

# "Obviously unsatisfied at my refusal to answer her way-too-intimate question, she has enough sense to back off."
"เอมิดูไม่พอใจกับคำปฏิเสธของฉันต่อคำถามที่ละลาบละล้วงนั้น แต่อย่างน้อยเธอก็เข้าใจว่าควรถอย"

show emicas wink
with charachange

# "Doesn't stop her from sticking out her tongue at me like a kid, and giggling again."
"แต่ก็ไม่วายจะแลบลิ้นใส่ฉันเป็นเด็ก ๆ แล้วหัวเราะคิกคัก"

show emicas closedsmile
with charachange

# emi "If that's your answer, I don't think I have to talk with you any more."
emi "ถ้านายตอบอย่างนั้น ฉันไม่คุยกับนายด้วยแล้ว"

# "It's easy to see that she's not really angry."
"เห็นชัดว่าเธอไม่ได้โกรธจริง ๆ"

show emicas happy
with charachange

# emi "Besides, I have to go pack now. Mom will be worried if I miss my bus."
emi "อีกอย่าง ฉันต้องไปเก็บของละ ขืนตกรถเดี๋ยวแม่เป็นห่วง"

# emi "Seeya!"
emi "เจอกัน!"

# hi "Yeah, bye."
hi "อื้ม บาย"

stop music fadeout 4.0

hide emicas
with charaexit

play sound sfx_doorclose

# "She retreats back into her room, leaving me alone in the hallway."
"เธอล่าถอยกลับเข้าห้องไปและทิ้งให้ฉันยืนตัวคนเดียวกลางโถงทางเดิน"

# "What's between me and Rin is not her business, right?"
"เรื่องระหว่างฉันกับรินก็ไม่ใช่เรื่องของเอมินี่"

# "That's why I ended up not saying anything about our fight to Emi. Rin must have not said anything either."
"เพราะงั้นฉันถึงไม่ได้เล่าเรื่องที่ทะเลาะกันให้เอมิฟังเลย รินก็คงไม่ได้บอกอะไรเหมือนกัน"

# "I guess… even though they are friends, there are things they don't talk about."
"ต่อให้เป็นเพื่อน ก็คงมีเรื่องที่ไม่ได้คุยกันอยู่… ละมั้ง"

"…"

# "So, if Rin is at the gallery, I'd have to go all the way there."
"ถ้ารินอยู่ที่หอศิลป์ ฉันก็ต้องถ่อไปที่นั่น"

# "Now that I managed to get out of my room, I suppose it's not that much of a bother to go downtown."
"ไหน ๆ ก็ออกห้องมาแล้ว จะไปตัวเมืองด้วยเลยก็คงไม่เสียหาย"

# "I could go get a ticket, but the train back home will have to wait, at least until tomorrow."
"แล้วก็จะได้ไปซื้อตั๋วด้วย แต่เรื่องขึ้นรถไฟกลับบ้านคงต้องเอาไว้ก่อน อย่างน้อย ๆ ก็ต้องพรุ่งนี้"

show rain normal behind bg
with None

# "No way I'm going to carry baggage to the train station in this rain, even if there's not that much of it."
"จะให้ขนสัมภาระฝ่าฝนไปทั้งอย่างนี้ก็ไม่ไหวหรอก ถึงจะไม่ได้มีของเยอะขนาดนั้นก็เถอะ"

$ renpy.music.set_volume(1.0, 3.0, channel="ambient")

show bg city_street4_rn as bg2 behind rain
hide bg
with shorttimeskip

# "Rain makes all outlines seem very unstable, as if they were fading away."
"ฝนทำให้ขอบนอกของสิ่งต่าง ๆ ดูไม่คงที่คล้ายเลือนหาย"

# "The townscape turns into a shapeless collection of various fuzzy tones of gray, instead of distinct forms of buildings and cars."
"ทิวทัศน์ของเมืองเปลี่ยนเป็นก้อนสีเทาไร้รูปทรงหลายก้อนกองรวมกันแทนที่จะเป็นรูปร่างของตึกหรือรถที่ชัดเจน"

# "Those poor souls who are forced into the downpour try to make as much haste as they possibly can, pitying each other for their shared misery."
"เหล่าคนน่าสงสารที่ถูกฝนสาดต้องรีบหาที่หลบฝนและส่งความสงสารให้คนที่ต้องมาเปียกฝนด้วยกัน"

show bg gallery_ext_rn as bg2
with locationchange

# "I turn the final corner, the twenty-second corner so to say, and immediately feel stupid for being amused by my own pun."
"ฉันเดินเลี้ยวมาที่ซอยสุดท้ายตรงซอยที่ 22 รู้สึกบ้าดีที่ขำกับมุกตัวเอง"

# "The door beckons me with promises of warmth."
"ประตูอันอบอุ่นนั้นดูเชื้อเชิญ"

$ renpy.music.set_volume(0.2, 1.0, channel="ambient")
play sound sfx_storebell 
play music music_soothing fadein 0.5

scene bg gallery_int
with locationchange

# "The rainwater dripping from my umbrella makes interesting, almost artistic patterns on the floor."
"หยดน้ำฝนที่ตกพื้นนั้นแผ่เป็นรูปร่างที่ดูเป็นศิลปะน่าสนใจ"

# "I am not wet, apart from my shoes that leave small puddles in my wake, completing the rainwater-artwork."
"ตัวฉันไม่ได้เปียก ที่เปียกก็มีแค่รองเท้าที่พอเดินย่ำเข้ามาแล้วก็เป็นรอยน้ำที่เติมเต็มงานศิลป์จากน้ำฝนที่อยู่บนพื้น"

show nomiya smile at twoleft
show sae neutral at tworight
with charaenter

# "Nomiya is here too, chatting with Sae at the back of the gallery. Rin's nowhere to be seen, though."
"โนมิยะก็อยู่ด้วย คุณครูกำลังคุยกับซาเอะอยู่ที่ด้านหลังหอศิลป์ แต่ไม่เห็นรินเลย"

# "Maybe she's upstairs."
"สงสัยอยู่ชั้นบนมั้ง"

# "There are no customers though, which figures, considering the bucketloads of water dropping on the neck of anyone daring to brave the weather today."
"แต่ไม่มีลูกค้าเลย ซึ่งก็ถูกแล้ว ดูจากสภาพฝนที่เทลงมาพร้อมสาดใส่คนที่อาจหาญมาลุยฝนวันนี้น่ะนะ"

show sae smile
with charachange

# sa "Welcome."
sa "ยินดีต้อนรับ"

# hi "Hello. Sorry to interrupt…"
hi "สวัสดีครับ ขอโทษที่รบกวน…"

show nomiya talk
with charachange

# no "Ah, good afternoon Nakai."
no "อ้าว ทิวาสวัสดิ์ นากาอิ"

show nomiya smile
with charachange

# no "Came all the way here for a visit?"
no "ถ่อมาหาถึงนี่เลยเหรอ"

# hi "Ah… no, I think it was just an impulse. I was around the neighborhood, shopping, and decided to stop by."
hi "อ่า… เปล่าครับ แค่ขาพามามั้งครับ พอดีมาซื้อของแถว ๆ นี้เลยแวะมา"

# "My reflexive reaction is a white lie, which surprises myself."
"ฉันโกหกตอบเลี่ยงไปโดยอัตโนมัติ ซึ่งฉันก็แปลกใจ"

# "Maybe I just don't want to say that I came specifically to see Rin, even though that much must be obvious."
"คงไม่อยากบอกมั้งว่าที่มาหาก็คือจะมาหาริน ถึงน่าจะเป็นอะไรที่ดูก็รู้เลยก็เถอะ"

show sae doubt
with charachange

# sa "My, you chose a bad day for shopping. Would you like some tea to warm you up?"
sa "ตายจริง เลือกวันซื้อของได้ผิดวันจริง ๆ เลยนะ ชาอุ่น ๆ สักหน่อยไหม"

# hi "Thank you but I'm fine, really."
hi "ขอบคุณครับ แต่ไม่ต้องก็ได้"

# hi "The weather could be better though. Rain on the first day of vacations is a bit depressing."
hi "ฝนไม่น่าตกเลยนะครับ มาตกวันปิดเทอมวันแรกอย่างนี้ทำเอาซึมหน่อย ๆ เลย"

show nomiya veryhappy
show sae neutral
with charachange

# no "Hahaha! Well, I'm sure it'll get better."
no "ฮ่าฮ่าฮ่า! เดี๋ยวฟ้าก็โปร่งแหละ"

# "Nomiya offers his hearty laughter, bordering on abrasive."
"โนมิยะหัวเราะอารมณ์ดีจนแทบจะระคายหู"

# hi "Rain doesn't get you down, teacher?"
hi "คุณครูไม่ซึมไปกับฝนเหรอครับ"

show nomiya smile
with charachange

# no "Well, I do prefer clear weather as well. I was actually leaving just now to meet someone, and I'd prefer not getting my jacket soaked. It's very expensive."
no "อืม ฉันก็ชอบตอนฟ้าโปร่งแหละนะ จริง ๆ เพิ่งออกมาเมื่อกี้เพราะนัดคนไว้น่ะ แล้วไม่อยากให้เสื้อคลุมแพง ๆ ตัวนี้\nเปียกด้วย"

show nomiya talk
with charachange

# no "But of course I'm in a good mood!"
no "แต่แน่ละว่าฉันอารมณ์ดี!"

show nomiya smile
with charachange

# no "What did you think about the exhibition? It was wonderful, wasn't it?"
no "เธอว่างานนิทรรศการเป็นไง สุดยอดไปเลยใช่มั้ยล่ะ"

# hi "Yeah, it was very fancy."
hi "ครับ หรูหรามาก ๆ"

# "My unenthusiastic answer only spurs him to carry on, walking around the gallery while blabbering about the opening."
"คำตอบไร้เรี่ยวแรงของฉันทำให้คุณครูพูดต่อพลางเดินไปรอบ ๆ หอศิลป์และพล่ามเรื่องงานเปิดตัว"

# "He talks more and louder when he is moving. It's something I noticed at the club meetings too."
"พอขยับตัวแล้วพูดเสียงดังกว่าเดิมอีก ที่ชมรมศิลปะก็เป็น"

show nomiya veryhappy
with charachange

# no "We got to talk with many good people and make valuable contacts."
no "ได้คุยกับคนดี ๆ เยอะแยะ แถมได้รู้จักคนชั้นเยี่ยมด้วย"

show nomiya smile
with charachange

# no "One of Tezuka's paintings even got sold, to a collector from Osaka."
no "มีภาพที่เทซูกะวาดภาพหนึ่งขายออกด้วยละ นักสะสมจากโอซากะมาซื้อไปแน่ะ"

$ renpy.music.set_volume(0.1, 1.0, channel="ambient")

show rin_exhibition_sold at center
with locationchange

# "I follow his eyes to an empty space in the wall. I can't even remember which painting was hanging on that spot."
"ฉันมองตามสายตาเขาไปที่พื้นที่ว่างบนผนัง ฉันจำไม่ได้ด้วยซ้ำว่าตรงนั้นเคยมีภาพอะไรอยู่"

# "Well, it's gone now."
"ก็ไม่มีแล้วอะนะ"

$ renpy.music.set_volume(0.2, 1.0, channel="ambient")

hide rin_exhibition_sold
show nomiya talk
with charachange

# no "It was lucky that she was all right despite that dizzy spell."
no "โชคดีไปนะที่แค่เวียนหัวนิดหน่อยแล้วก็ไม่เป็นอะไรมาก"

show nomiya smile
with charachange

# no "She got a little quiet though, so I told her to rest well. Then again she's always been pretty shy."
no "แต่เห็นเงียบ ๆ ไปเลยบอกให้ไปพักผ่อนเยอะ ๆ แต่เทซูกะก็เป็นคนขี้อายแต่ไหนแต่ไรแล้วนี่นะ"

# "Shy? Whatever, I just nod along with the teacher."
"ขี้อาย? เอาเถอะ ฉันพยักหน้าเออออตามน้ำไป"

show nomiya talktongue
with charachange

# no "The reception was very positive in general. I might be able to get one of my friends to write a little article on a magazine to—"
no "เสียงตอบรับดีทีเดียวละ เดี๋ยวอาจจะไปขอให้เพื่อนฉันคนหนึ่งเขียนบทความเล็ก ๆ ลงในนิตยสาร—"

# sa "Shinichi, your meeting. You're making Mr. Takahashi wait."
sa "ชินอิจิ คุณมีนัดนี่ คุณทาคาฮาชิเขาคงรอแย่แล้ว"

show nomiya serious
with charachange

# "Sae's remark makes him stop in his tracks and check his watch."
"คำพูดของซาเอะทำเอาคุณครูชะงักแล้วก้มมองนาฬิกา"

# "Nomiya frowns in displeasure at the interruption to his tirade."
"โนมิยะขมวดคิ้วไม่พอใจที่มีอะไรมาขัดจังหวะการสาธยายของเขา"

show nomiya smile
with charachange

# no "Oh, right. Yes, well, I'll be off then. We'll meet in September, Nakai."
no "อ้อ จริงสิ อื้ม เดี๋ยวไปละ เจอกันเดือนกันยายนนะนากาอิ"

# hi "Bye."
hi "บายครับ"

hide nomiya
with charaexit

play sound sfx_storebell
stop music fadeout 4.0

# "Wow. Teacher really doesn't hold back when it comes to Rin's budding artist career."
"โห คุณครูทุ่มสุดตัวกับเส้นทางศิลปินของรินที่กำลังแตกหน่อจริง ๆ"

# "I guess it takes a lot to succeed, but I suppose his job would be easier if Rin was more cooperative."
"จะประสบความสำเร็จได้ก็คงต้องทุ่มเทหน่อย แต่ถ้ารินให้ความร่วมมือกว่านี้น่าจะง่ายหน่อยน่ะนะ"

$ renpy.music.set_volume(0.1, 1.0, channel="ambient")
$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

# n "\nShe's too indecisive even though she's doing just fine. Like that “dizzy spell” from the night before."
n "\nรินโลเลทั้งที่ความสามารถก็ใช้ได้ เหมือนเรื่อง “เวียนหัว” เมื่อคืนนั้น"

# n "She just got freaked out or something, and I didn't do anything to help her."
n "เธอตกใจกลัวหรืออะไรสักอย่าง ส่วนฉันก็ไม่ได้ช่วยอะไรเธอเลย"

# n "\nI sigh."
n "\nฉันถอนหายใจ"

# n "It feels like the gap between me and Rin is only widening."
n "ยิ่งรู้สึกเหมือนระยะระหว่างฉันและรินจะออกห่างเรื่อย ๆ"

# n "She's going to become something great while I'm still feeling like I'm bogged down, despite promising myself to try and make something of my life."
n "เธอจะได้เติบโตจนยิ่งใหญ่ ส่วนฉันก็ยังรู้สึกเหมือนติดหล่มอยู่อย่างนี้ ถึงจะสัญญากับตัวเองแล้วว่าจะพยายามหาเส้นทาง\nให้ชีวิตตัวเองแล้วก็เถอะ"

# n "On top of that, we had that fight and the longer we keep not talking, the harder the wounds become to heal."
n "ยิ่งไปกว่านั้น พวกเราก็ทะเลาะกันอีก แล้วยิ่งทำมึนตึงใส่กันไปนานเท่าไหร่ บาดแผลก็ยิ่งยากจะลบเลือนไปเรื่อย ๆ"

# n "If that even is what we want. I never found out what Rin felt, and now I'm not sure what I feel myself."
n "พวกเราอยากให้เป็นอย่างนี้เหรอ ฉันไม่เคยรู้เลยว่ารินรู้สึกอย่างไร แล้วตอนนี้ฉันก็ไม่แน่ใจแล้วว่าฉันรู้สึกอย่างไร"

# n "I wish I could understand her. But Rin is not very open for interpretation."
n "ฉันอยากเข้าใจริน แต่รินก็ไม่ได้เป็นคนที่จะตีความให้เข้าใจได้ง่ายมากนัก"

# n "Not that she's hiding anything, she just seems to defy my attempts at making sense of what she is talking about on any given day."
n "ไม่ใช่ว่าเธอปกปิดอะไร แค่เหมือนว่าฉันจะล้มเหลวทุกครั้งที่พยายามจะทำความเข้าใจกับสิ่งที่เธอพูดในแต่ละวัน"

$ renpy.music.set_volume(0.2, 1.0, channel="ambient")
$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

show sae smile
with charachange

window show

# sa "Something on your mind?"
sa "คิดอะไรอยู่เหรอ"

# "I realize I've been spacing out in the middle of the gallery for who knows how long."
"ฉันเพิ่งรู้ตัวว่ายืนเหม่ออยู่กลางหอศิลป์มานานมากแล้ว"

# hi "Ahh… nothing special…"
hi "เอ่ออ… ไม่มีอะไรหรอกครับ…"

# "I pretend to study the closest paintings to distract her."
"ฉันทำท่าเป็นยืนพินิจรูปที่อยู่ใกล้ ๆ เพื่อเบนความสนใจซาเอะ"

$ renpy.music.set_volume(0.1, 1.0, channel="ambient")
play music music_another fadein 0.5

scene rin_exhibition_c:
    truecenter
    zoom 1.0 subpixel True
    ease 30.0 zoom 1.1
with locationchange

# "I've seen it before."
"ฉันเคยเห็นรูปนี้มาก่อน"

# "The now all-too-familiar strokes of color, twisting and melting into each other seemingly randomly still manage to feel like there is something happening behind the scenes, so to speak."
"ฝีแปรงการลงสีที่บัดนี้ฉันคุ้นตาดีแล้วต่างบิดงอและหลอมรวมเข้าด้วยกันอย่างสะเปะสะปะ ทว่าก็ทำให้รู้สึกเหมือนมี\nอะไรบางอย่างโดยรวมอยู่เบื้องหลัง"

# "Rin's style is so much like her. Abstract, incomprehensible, colorful."
"ลักษณะการวาดของรินนั้นช่างเหมือนเธอ นามธรรม เข้าใจยาก หลากสีสัน"

# "Mysterious."
"ลึกลับ"

# "I wonder if to understand an artist, one must understand art?"
"ถ้าจะเข้าใจศิลปิน ต้องเข้าใจศิลปะก่อนหรือเปล่านะ"

$ renpy.music.set_volume(0.2, 1.0, channel="ambient")

scene bg gallery_int
with locationchange

# hi "Umm… I may have a question."
hi "เอ่อ… ผมมีคำถามครับ"

show sae smile at center
with charaenter

# sa "Oh?"
sa "หืม?"

# "She looks up from the magazine she was idly leafing through, seeming delighted at my display of unspecified interest."
"เธอเงยหน้าขึ้นมาจากนิตยสารที่เธอพลิกหน้าไปเรื่อย ๆ อยู่ ดูท่าว่าจะพอใจที่ฉันสนใจบางอย่างขึ้นมา"

# hi "How do you interpret art?"
hi "ศิลปะเขาตีความกันยังไงเหรอครับ"

show sae doubt
with charachange

# sa "What do you mean?"
sa "หมายความว่าไง"

# "Her eyebrows rise high into questioning arcs, as if the question was too complicated to even begin to answer without clarification."
"เธอเลิกคิ้วขึ้นด้วยความสงสัยราวกับว่าคำถามนั้นซับซ้อนเกินกว่าที่จะตอบโดยไม่มีการแจกแจงให้ละเอียดก่อนได้"

# hi "Sorry if I'm asking something stupid."
hi "ขอโทษถ้าคำถามฟังดูโง่นะครับ"

# hi "I don't think I really understand art like the pros do."
hi "ผมว่าผมไม่เข้าใจศิลปะเหมือนอย่างมืออาชีพสักเท่าไหร่"

show sae smile
with charachange

# sa "Oh, there's no trick to it."
sa "โอ๊ย ของแบบนี้ไม่มีกลเม็ดเคล็ดลับอะไรหรอก"

# "Sae waves my question away with a simple but efficient flick of her wrist."
"ซาเอะสะบัดข้อมือเบา ๆ ปัดคำถามของฉันทิ้ง"

show sae neutral
with charachange

# sa "Everyone interprets art as they will, and interpretation is as much in the eye of the beholder as in the intentions of the creator."
sa "ทุกคนก็ตีความศิลปะไปตามที่ตัวเองคิดนั่นแหละ การตีความมันก็ขึ้นอยู่กับคนที่มอง ไม่ต่างอะไรกับการที่เจตนาขึ้นอยู่\nกับคนที่สร้างผลงานขึ้นมาหรอก"

# sa "“Pros” have their own way, because there is this thing called art theory."
sa "“มืออาชีพ” มีวิธีการตีความของตัวเอง เพราะมีสิ่งที่เรียกว่าทฤษฎีศิลป์อยู่"

# sa "There are patterns in art, just like in everything, and we assume that it's possible to draw some conclusions from observing those patterns."
sa "ศิลปะก็มีรูปแบบเหมือนอะไรอย่างอื่นนั่นแหละ แล้วเราก็ตั้งข้อสมมติฐานว่าถ้าจับสังเกตรูปแบบพวกนั้นได้แล้ว เราก็จะได้\nข้อสรุปบางอย่างออกมา"

# "Her voice is like a teacher's, lecturing and adding emphasis on random words to keep the listeners on their toes."
"น้ำเสียงเธอเหมือนอย่างคุณครูที่สอนโดยเน้นเสียงที่คำบางคำให้คนฟังคอยสนใจ"

show sae smile
with charachange

# sa "In the end, I suppose it's pretty meaningless."
sa "ซึ่งสุดท้ายแล้ว ฉันว่ามันก็ค่อนข้างเปล่าประโยชน์น่ะนะ"

# "She moves to musing seemingly to herself, muttering loud enough for me to clearly hear."
"เธอพูดอยู่กับตัวเองยิ้ม ๆ พึมพำดังพอให้ฉันได้ยินชัด ๆ"

# sa "A good piece of art will make you feel something and that's all there is to it."
sa "ผลงานศิลปะที่ดีจะทำให้คนดูรู้สึกบางอย่าง ซึ่งเรื่องมันก็แค่นั้นแหละ"

# sa "Feelings change and they affect the art we create and the art we see."
sa "ความรู้สึกน่ะเปลี่ยนแปลงเสมอ และความรู้สึกก็มีผลกับศิลปะที่เราสร้างและศิลปะที่เราเห็น"

# hi "But…"
hi "แต่ว่า…"

show sae neutral
with charachange

# sa "I'll tell you a story."
sa "ฉันมีเรื่องจะเล่าให้ฟัง"

# hi "Do you have to? The last one was depressing…"
hi "ต้องเล่าด้วยเหรอครับ เรื่องที่เล่าครั้งที่แล้วมันออกจะหดหู่…"

# sa "It's important. Listen…"
sa "เรื่องสำคัญ ฟังนะ…"

# sa "About a hundred years ago a little known painter got news that his friend, a man called Casagemas, had committed suicide."
sa "ประมาณร้อยปีที่แล้ว มีศิลปินตัวเล็ก ๆ คนหนึ่งได้ข่าวว่าเพื่อนของเขาที่ชื่อกาซาเฆมัสได้ฆ่าตัวตาย"
#http://en.wikipedia.org/wiki/Picasso's_Blue_Period -SC

# sa "This happened while he was away and hadn't seen his friend for a while."
sa "เรื่องนี้เกิดขึ้นตอนที่เขาไม่ได้อยู่กับเพื่อนคนนั้น แล้วเขาก็ไม่ได้เจอกับเพื่อนมาสักพักแล้วด้วย"

# sa "So obviously he must have felt even more conflicted than you normally would after hearing of such a thing."
sa "ซึ่งแน่นอนว่าเขาคงต้องสับสนหนักยิ่งกว่าเวลาที่คนปกติได้รับข่าวอย่างนั้นเสียอีก"

# sa "For four years after that, our main character did nothing but monochromatic paintings because he was so deeply affected by the news."
sa "สี่ปีหลังจากนั้น ตัวเอกของเรื่องเราก็ใช้แค่สีโทนเดียววาดรูปเพราะสะเทือนใจกับข่าวนั้นมาก"

# sa "Whatever he did, he always kept returning to that same color until it let him out of its grasp."
sa "ไม่ว่าเขาจะทำอะไร เขาก็จะกลับมาใช้สีเดิม ๆ จนกว่าสีนั้นจะยอมปล่อยตัวเขาไป"

# "She takes a little pause to check whether I'm still following."
"เธอหยุดไปเพื่อดูว่าฉันยังตามทันหรือไม่"

# "I am, to an extent, so I give her the prompt that storytellers seem to live for."
"ซึ่งฉันก็พอจะตามทันอยู่ ฉันจึงโยนคำหนึ่งที่พวกเล่าเรื่องดูจะชอบฟังกันไปให้"

# hi "So…"
hi "แล้ว…"

# "It's hard to continue from that, as I can't seem to come up with the question she wants me to come up with."
"ฉันไม่รู้จะพูดต่อยังไง เพราะฉันคิดคำถามที่เธอน่าจะอยากให้ฉันถามไม่ออก"

# "Like a half-baked Socrates, she thought she laid out all the tools for revelation in front of me."
"เธอทำตัวอย่างโสกราตีสครึ่ง ๆ กลาง ๆ ที่คิดว่าได้เฉลยกุญแจที่ทำให้รู้แจ้งไปแล้ว"

show sae doubt
with charachange

# sa "Don't you see the point yet?"
sa "ยังไม่เข้าใจอีกเหรอ"

# "Only, her student proved to be too dense to get it."
"ซึ่งนักเรียนของเธอนั้นหัวทึบเกินกว่าจะมองเห็น"

show sae scowl
with charachange

# "She looks discontent at my slowness."
"เธอดูหงุดหงิดที่ฉันหัวช้า"

# sa "Picasso's Blue Period is one of the most lauded in the history of art, but who knows what he felt when he worked on those masterpieces?"
sa "ยุคบลูพีเรียดของปิกัสโซน่ะเป็นยุคที่ได้รับการยกย่องมากในประวัติศาสตร์ศิลปะ แต่ใครจะไปรู้ว่าเจ้าตัวจะรู้สึกยังไงตอนที่\nกำลังวาดผลงานชิ้นเอกเหล่านั้นอยู่"

# sa "Sadness? Longing? Regret?"
sa "เศร้า? โหยหา? เสียใจ?"

# sa "Nobody can tell."
sa "ไม่มีใครรู้"

# sa "If you now see one of his Blue Period paintings, you'd probably interpret it differently from before you knew about Picasso's friend Casagemas."
sa "ถ้าตอนนี้เธอได้เห็นภาพวาดสักหนึ่งภาพจากยุคบลูพีเรียด เธออาจจะตีความไปคนละแบบกับตอนก่อนที่เธอจะได้รู้เรื่อง\nเพื่อนของปิกัสโซที่ชื่อกาซาเฆมัสก็ได้"

show sae neutral
with charachange

# sa "Experiencing art is always personal, only interactive by chance or circumstances."
sa "การสัมผัสศิลปะน่ะเป็นอะไรที่เป็นปัจเจกเสมอ ขึ้นอยู่กับโอกาสหรือสถานการณ์เท่านั้น"

# sa "There are a million explanations for any given piece of art, but it might be that none of them are what the creator intended."
sa "งานศิลปะชิ้นหนึ่งอาจจะมีคำมาอธิบายได้ล้านอย่าง แต่ก็เป็นไปได้ว่าจะไม่มีอย่างไหนเลยที่ตรงกับเจตนาของผู้สร้าง"

show sae smile
with charachange

# sa "No man is an island, you know?"
sa "ไม่มีใครเป็นเกาะเดียวดายหรอกนะ"

# "I nod without understanding what that last remark meant."
"ฉันพยักหน้าไปทั้ง ๆ ที่ไม่เข้าใจว่าประโยคปิดท้ายนั้นหมายความว่าอะไร"

# "What she said made sense otherwise, except for one thing."
"แต่นอกนั้นก็เข้าใจอยู่ ยกเว้นอยู่หนึ่งอย่าง"

# "If art is communication like Rin said, but everyone is talking their own secret language like Sae said, what can anyone ever hope to communicate?"
"ถ้าศิลปะคือการสื่อสารอย่างที่รินบอก แต่ทุกคนก็คุยกันด้วยภาษาลับของตัวเองอย่างที่ซาเอะบอก แล้วจะสื่อสารอะไร\nกันได้?"

# "It seems so futile, and pointless."
"ดูทั้งเปล่าประโยชน์และไม่มีความหมาย"

# "Art really is not a thing for me."
"ศิลปะไม่ใช่ทางฉันเลยจริง ๆ"

$ renpy.music.set_volume(0.1, 1.0, channel="ambient")

scene bg gallery_exhibition
with locationchange

# "Sae returns to her art magazine, and I make a round in the gallery, trying to see what Rin can see in her own paintings."
"ซาเอะหันกลับไปดูนิตยสารต่อ ส่วนฉันก็เดินไปรอบ ๆ หอศิลป์เพื่อดูว่ารินจะเห็นอะไรในผลงานตัวเอง"

# "A soothing mood takes hold of the gallery surrounded by the rainstorm, the big windows making the transparent isolation feel more comfortable."
"อารมณ์อันผ่อนคลายลอยอวลอยู่ในหอศิลป์แห่งนี้ที่พายุฝนซัดสาด หน้าต่างบานใหญ่ทำให้อยู่คนเดียวได้ไม่อึดอัด"

play sound sfx_storebell
stop music fadeout 2.0

# "A tinkle of the bell disrupts the tranquil mood."
"เสียงกริ๊งของกระดิ่งเข้ามาขัดความสงัดงัน"

$ renpy.music.set_volume(0.2, 1.0, channel="ambient")

scene bg gallery_int
with locationchange

show rin relaxed_nonchalant at center
with charaenter

# "Rin pushes the door open with her shoulder and steps in."
"รินใช้ไหล่ผลักประตูเข้ามา"

# "I had almost forgotten that she was the reason why I came to the gallery in the first place."
"ฉันแทบจะลืมไปแล้วว่าที่มาหอศิลป์ก็เพื่อจะมาหาเธอ"

show rin relaxed_boredom
with charachange

# rin "I think I'm ready—{w=0.3}{nw}"
rin "คิดว่าพร้อมแล้ว—{w=0.3}{nw}"

show rin relaxed_surprised
with charachange

# "She pauses mid-sentence, noticing my presence."
"พอเธอเห็นฉันก็ชะงักไปทันที"

# "The needle-dropping silence lasts for exactly one and a half seconds, not enough for either me or Sae to open our mouths, but enough for Rin to react."
"ความเงียบเป็นเป่าสากนั้นอยู่ได้นานหนึ่งวินาทีครึ่งพอดิบพอดี ไม่นานพอที่จะให้ฉันหรือซาเอะได้เปิดปาก แต่นานพอ\nที่จะให้รินตอบสนอง"

show rin negative_annoyed
with charachange

# rin "I'm going for a walk."
rin "ขอไปเดินเล่นค่ะ"

hide rin
with charaexit

play sound sfx_storebell

# "Heading back outside with a reckless pace uncharacteristic of herself, Rin seems to forget that it's still raining."
"เธอรีบรุดออกไปไม่สมกับเป็นริน และดูเหมือนจะลืมไปแล้วว่าฝนยังตกอยู่"

show rain normal behind bg

# "Without giving it any real thought, I grab my umbrella and hurry after her."
"ฉันคว้าร่มแล้วรีบตามเธอไปไม่คิดอะไรทั้งสิ้น"

play sound sfx_storebell
$ renpy.music.set_volume(1.0, 2.0, channel="ambient")

hide bg
show bg city_street4_rn as bg2 behind rain
show rin negative_spaciness_close_rn
with locationskip

# "I catch Rin around the corner, open the umbrella and lift it above the two of us while still having to almost run to keep up with her."
"พอถึงหัวมุมถนนหนึ่งฉันก็มาทันริน ฉันกางร่มแล้วยกกันฝนให้ทั้งฉันและเธอพลางตามไปด้วยความเร็วที่ฉันแทบจะ\nต้องวิ่ง"

# "She doesn't protest me running after her nor me giving her shelter against the rain, eventually slowing her pace down so I can match it without an immediate danger of overexerting myself."
"เธอไม่ได้ขัดขืนที่ฉันวิ่งตามหรือกางร่มให้ จนสุดท้ายเธอก็ผ่อนฝีเท้าลงจนฉันเดินตามได้โดยไม่ต้องฝืนให้ตัวเอง\nเสี่ยงอันตราย"

# "I relax from the rush, assessing the situation."
"ฉันปรับจังหวะการหายใจพลางประเมินสถานการณ์"

# "The last time I held my umbrella to guard both of us against the rain, I didn't think too much about it."
"ครั้งล่าสุดที่ฉันกางร่มให้เธอ ฉันไม่ได้คิดอะไรมากมาย"

# "But now, all the things that happened since then are gathering into a freezing cold ball around my stomach."
"แต่ตอนนี้ ทุกอย่างที่เกิดขึ้นตั้งแต่ตอนนั้นอัดเป็นก้อนหนักหน่วงอยู่ในท้องฉัน"

# "Being close to her makes me uncomfortable, and I feel myself flustering slightly."
"พอได้อยู่ใกล้แล้วก็อึดอัด แถมยังแอบกระอักกระอ่วนด้วย"

# "It's hard to get words out of my mouth, as it feels suddenly very, very dry."
"อยู่ ๆ ปากก็แห้ง แห้งผากจนพูดอะไรแทบไม่ออก"

# "Still, it's not like I can back off."
"แต่ก็ใช่ว่าจะถอยได้แล้ว"

# hi "Why do you keep running away?"
hi "ทำไมเธอถึงเอาแต่หนี"

show rin negative_annoyed_close_rn
with charachange

# rin "I don't want to talk to you."
rin "ฉันไม่อยากคุยกับนาย"

# hi "I want to talk to you."
hi "ฉันอยากคุยกับเธอ"

show rin negative_confused_close_rn
with charachange

# rin "It hurts every time I do."
rin "ฉันคุยทีไรก็เจ็บทุกที"

# hi "Sometimes it can't be helped."
hi "บางทีมันก็ช่วยไม่ได้"

show rin negative_sad_close_rn
with charachange

# rin "I don't want to hurt."
rin "ฉันไม่อยากเจ็บ"

# hi "Fine. We don't have to talk."
hi "ได้ งั้นก็ไม่ต้องคุยกัน"

show rin relaxed_doubt_close_rn
with charachange

# rin "What should we do?"
rin "แล้วทำอะไรดี"

# hi "Let's just keep walking."
hi "เดินต่อไปเฉย ๆ กันเถอะ"

show rin relaxed_surprised_close_rn
with charachange

# rin "Just walking?"
rin "เดินเฉย ๆ ?"

# hi "Just walking."
hi "เดินเฉย ๆ"

show rin basic_absent_close_rn
with charachange

# rin "Okay."
rin "โอเค"


label th_R37:

play music music_dreamy fadein 2.0
$ renpy.music.set_volume(1.0, 2.0, channel="ambient")
$ renpy.music.play(sfx_rain, fadein=2.0, if_changed=True, channel="ambient")

play sound sfx_whiteout

scene white
with Dissolve(1.0)

show rain normal behind white
with None

hide white
show ev rin_rain_away_close behind rain at Fullpan(20.0,dir="up")
with Dissolve(1.0)

# "Our footsteps go “splish splash” in the shallow puddles forming on the streets as we walk through the rainfall."
"ก้าวเดินของเราส่งเสียงจ๋อมแจ๋มไปตามแอ่งน้ำบนถนนที่เราเดินลุยฝนไป"

# "Rin, now walking beside me in her unhurried and relaxed manner, doesn't seem to be even a bit bothered by the fact that she is getting wet even though she needn't to."
"รินเดินเคียงฉันอยู่สบาย ๆ ไม่เร่งรีบ ไม่ร้อนใจอะไรที่ตัวเองเปียกฝนโดยไม่จำเป็น"

# "She is partially out of the protective shelter of my umbrella, despite it being more than big enough for the two of us."
"ยังมีตัวเธอบางส่วนที่เลยออกนอกร่มไปอยู่ ถึงร่มจะใหญ่พอสำหรับเราสองคนก็เถอะ"

# "It's as if she doesn't even notice the rain drenching her shirt."
"ราวกับไม่รู้ตัวเลยว่าเสื้อเปียกฝนอยู่"

"…"

# "Rin's demeanor always evokes mental images of meditative calm, even when she might be in inner turmoil."
"ท่าทางของรินทำให้นึกถึงคนที่ทำสมาธิจนสงบ ถึงภายในเธออาจจะกำลังว้าวุ่นก็ตาม"

# "But I don't think that is meditation. That is just getting soaked in rain."
"แต่ฉันว่านี่ไม่ใช่การทำสมาธิหรอก แค่ตากฝนจนเปียกเฉย ๆ นี่แหละ"

# "I wish I could be more calm too."
"ฉันก็อยากใจเย็นกว่านี้บ้าง"

# "I've become too involved with Rin to retain my usual aloofness."
"ฉันสนใจรินไปเกินกว่าที่จะทำทีห่างเหินอย่างปกติแล้ว"

# "It feels like I have become one of those people who fool themselves into thinking they are objective, only to find out they are the worst kind of liars."
"รู้สึกเหมือนกับว่าฉันเป็นพวกที่หลอกตัวเองว่ามองอะไรอย่างเป็นกลาง แล้วถึงมารู้ทีหลังว่าตัวเองนั้นเป็นคนที่โกหก\nไม่เก่งเอาเสียเลย"

# "Illusions to fool ourselves, what better way to make one feel like a good person?"
"ภาพลวงที่ลวงตัวเราเอง จะมีวิธีไหนที่ดีกว่านี้อีกที่จะทำให้รู้สึกว่าตัวเองนั้นเป็นคนดี"

# "It might be better to lose that illusion."
"สลายภาพลวงนั้นทิ้งคงจะเป็นวิธีที่ดีกว่า"

show ev rin_rain_away_close at Position(yalign=0.0)
show ovl rin_rain_hisaotowards_close behind rain at Position(xalign=1.0, yalign=0.0)
with charachange

# hi "I'll be going back home for some time so I thought I'd come to see you before that."
hi "เดี๋ยวฉันจะกลับบ้านสักพัก เลยกะว่าจะแวะมาหาเธอก่อนไป"

# "I could have thought of a better conversation opener, but Rin actively refusing to talk makes it hard."
"ฉันคงจะหาคำพูดเปิดบทสนทนาที่ดีกว่านี้ได้อยู่ แต่รินก็ไม่ยอมคุยด้วยจนไม่รู้จะคุยอะไร"

# rin "That's good. I might have thought that you'd have been kidnapped otherwise."
rin "ก็ดีแล้ว ไม่งั้นฉันคงนึกว่านายโดนลักพาตัวไป"

# hi "You can't keep running away from everything. Not even from me trying to talk seriously."
hi "เธอจะเอาแต่หนีจากทุกอย่างไปไม่ได้นะ หนีจากฉันที่จะคุยกับเธออย่างจริงจังไม่ได้ด้วย"

# rin "I'm always serious. Also I seem to be running very slowly right now."
rin "ฉันจริงจังเสมอ แล้วก็ตอนนี้เหมือนฉันจะวิ่งช้าลงมาก"

# rin "Maybe I should take lessons from Emi."
rin "คงต้องหัดเอาอย่างเอมิบ้างแล้ว"

# "It's futile. Like talking to a brick wall that randomly spouts sarcastic nonsense back at you."
"เปล่าประโยชน์ เหมือนคุยกับกำแพงอิฐที่เอาแต่พ่นอะไรไร้สาระไม่รู้เรื่องใส่"

# hi "Think of your exhibition opening. What if you had run away?"
hi "ลองคิดเรื่องวันงานเปิดตัวงานนิทรรศการดูสิ ถ้าเธอหนีไปจะเกิดอะไรขึ้น"

# "Rin doesn't answer to that, she just keeps walking. Or running slowly, escaping from me into her silence."
"รินไม่ตอบ เธอเดินต่อไปเรื่อย ๆ หรือไม่ก็วิ่งอยู่อย่างเชื่องช้าคอยหนีจากฉันไปยังความเงียบเชียบของเธอเอง"

# "She has a knack for being alone in company, I've noticed."
"ฉันสังเกตว่าเธออยู่คนเดียวเวลาอยู่ด้วยกันเก่ง"

show bg city_street3_rn behind rain
hide ev
hide ovl
with locationchange

# "We head down the street, then turn left, then three times right, then left again."
"พวกเราเดินไปตามถนน เลี้ยวซ้าย เลี้ยวขวาสามครั้ง แล้วก็เลี้ยวซ้ายอีกครั้ง"

# "It's like that night from some time ago, we keep choosing directions randomly because it doesn't matter where we are going."
"เหมือนเมื่อคืนวันนั้นเลย ที่พวกเราเดินไปแบบสุ่ม ๆ เพราะไม่ว่าจะไปที่ไหนก็เหมือน ๆ กัน"
#In R25. -SC

# "All that matters is walking and the sound of raindrops drumming against the umbrella."
"สิ่งที่สำคัญมีเพียงการเดินและเสียงฝนที่ตกเปาะแปะใส่ร่ม"

# "Water flows down from the roofs of the buildings and into the storm drains in wide rivers."
"น้ำไหลจากหลังคาตึกลงมาที่ทางน้ำทิ้งไปสู่แม่น้ำกว้าง"

# "Even though I try to step over them, my feet are getting wet through my shoes."
"ถึงจะแยกขาเดินข้ามแล้วแต่เท้าฉันก็ยังเปียกจนรองเท้าชุ่ม"

# "We keep walking in silence that just begs to be broken again. I'm sure I am the only one feeling like this, though."
"พวกเราเดินไปพร้อมความเงียบงันที่กดดันให้ต้องมีการพูดแทรก แต่ฉันมั่นใจว่ามีแค่ฉันที่รู้สึกถึงความกดดันนั้น"

hide bg
show ev rin_rain_away behind rain
show ovl rin_rain_hisaotowards at Position(xalign=1.0, yalign=0.0) behind rain
with locationchange

# hi "Why did you have the exhibition?"
hi "ทำไมเธอถึงจัดงานนิทรรศการ"

# "Rin just shrugs sullenly and looks in the other direction. I give up at this point."
"รินยักไหล่ด้วยความหม่นหมองแล้วมองไปทางอื่น ฉันขอยอมแพ้"

window hide

hide ovl
with charachange

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")
$ renpy.music.set_volume(0.5, 1.0, channel="music")

nvl clear
nvl show dissolve

# n "\n\n\nIt's pointless."
n "\n\n\nไม่มีความหมาย"

# n "\nWhat did she want to accomplish? What she said at the night of the opening made me feel that there was something… something special she wanted."
n "\nเธอทำไปเพื่ออะไร คืนวันเปิดตัวเธอบอกว่ามีบางอย่าง… บางอย่างแสนพิเศษที่เธอต้องการ"

# n "It felt to me that Rin hoped for something unattainable."
n "ฉันรู้สึกว่ารินคาดหวังอะไรที่ไม่อาจคว้าเอาไว้ได้อยู่"

# n "She set the bar high and inside her own head she failed, no matter how much people liked her works."
n "เธอตั้งมาตรฐานสูงไป แล้วก็คิดว่าตัวเองล้มเหลว ไม่ว่าคนจะชอบงานเธอมากแค่ไหนก็ตาม"

# n "It's understandable to lack realism; most people do, even if not quite on the extreme level Rin takes it to."
n "การไม่คิดถึงความเป็นจริงนั้นก็เข้าใจได้ หลายคนก็เป็นอย่างนั้น ถึงอาจจะไม่ได้ถึงขั้นสุดอย่างรินก็เถอะ"

# n "\nBut it's not a reason to live in your private world that accepts no visitors."
n "\nแต่นั่นก็ไม่ใช่เหตุผลที่จะต้องไปอยู่ในโลกส่วนตัวของตัวเองแล้วไม่เปิดรับใครเลย"

nvl clear

# n "\n\n\nYou can't bend the world to fit your twisted, megalomaniac cosmology where everything works just like you want."
n "\n\n\nจะมาบิดโลกให้ทุกอย่างเป็นไปดั่งใจนึกนั้นย่อมเป็นไปไม่ได้"

# n "\nThat's what frustrates me the most in Rin."
n "\nที่ฉันหงุดหงิดกับรินก็อย่างนี้"

# n "\nShe wants the world to live by her rules, disregarding everything that conflicts with those as irrelevant or unnecessary."
n "\nเธอต้องการให้โลกเป็นไปตามกฎเกณฑ์ของเธอ เธอเมินทุกอย่างที่ไม่เป็นไปตามนั้นแล้วปัดทิ้งว่าไม่เกี่ยวข้องกัน\nหรือไม่สำคัญ"

# n "I can't believe how anyone in Yamaku could not have the bare minimum perception to understand that the world can sometimes be very unfair."
n "เป็นนักเรียนยามากุอย่างน้อยก็ต้องเข้าใจบ้างว่าบางทีโลกมันก็ไม่ยุติธรรม ไม่อยากจะเชื่อเลยว่าจะมีคนที่ไม่เข้าใจอยู่"

# n "I'm sure she's not the only one who wishes some things were different, but we can at least grasp the facts as they are."
n "ฉันเชื่อว่ารินไม่ใช่คนเดียวที่อยากให้อะไร ๆ นั้นต่างออกไป แต่อย่างน้อยพวกเราก็ยังยอมรับความจริงอย่างที่เป็นอยู่ได้"

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")
$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

hide ev
show bg city_street4_rn behind rain
show rin negative_spaciness_close_rn at center
with locationchange

window show

# "I take a sideways glance at Rin, who is looking up at our dome-shaped cover. It is a poor replacement for a real sky in its monochrome bleakness."
"ฉันเหลือบมองริน เธอมองหลังคาที่คุ้มกันเราที่เป็นทรงโดมอยู่ เป็นของที่ใช้มองแทนท้องฟ้าอันอึมครึมที่ไม่ดีเท่าไหร่"

# "The rain just keeps falling."
"ฝนยังคงโปรยปราย"

# "Just like the clouds today, Rin doesn't really give the feeling of wanting to be watched."
"รินดูจะไม่อยากให้ใครมอง เหมือนอย่างเหล่าก้อนเมฆในวันนี้"

# "She sulks, in unison with the sky that she loves so."
"เธออารมณ์ไม่ดี เหมือนอย่างท้องฟ้าที่เธอแสนรัก"

# "I shouldn't have come. Her presence only reminds me of how angry I got because of these exact same reasons, and how those reasons probably can't ever change."
"ไม่น่ามาเลย ตัวตนเธอยิ่งเป็นเครื่องย้ำเตือนว่าฉันโกรธเธอก็เพราะอย่างนั้น แล้วเหตุผลพวกนั้นก็คงไม่มีทางเปลี่ยนไป"

# "Even though I want to say I'm sorry, even though I don't want us to break apart, I can't bring myself to say either of these things."
"ถึงฉันจะอยากขอโทษ ถึงฉันจะไม่อยากให้เราต้องแยกทางกัน แต่ฉันก็ไม่อาจพูดอะไรสักอย่างได้เลย"

show bg misc_sky_rn
hide rin
with locationchange

# "We keep measuring the rain-drenched streets one step at a time."
"พวกเราเดินวัดถนนที่นองฝนไปทีละก้าว"

# "Often, when you walk with someone else, your steps become synchronized as if through some weird subconscious pact."
"บ่อยครั้งเวลาที่เดินกับใคร จังหวะการเดินก็จะเข้าที่จนเท่ากันราวกับว่าได้ทำข้อตกลงอะไรแปลก ๆ ในจิตใต้สำนึก\nด้วยกันไว้"

# "I noticed that ours never do."
"ฉันสังเกตว่าจังหวะการเดินของฉันและรินไม่เคยเสมอกันเลย"

window hide

stop music fadeout 5.0
$ renpy.music.set_volume(0.3, 3.0, channel="ambient")

show bg misc_sky_rays
show rain light
with Dissolve(3.0)

window show

# "Time passes, and the strikes against the drumskin of my umbrella fade as the clouds above slowly disperse to reveal a cerulean blue."
"เวลาผ่านไป เสียงฝนที่ตกกระทบกับร่มค่อย ๆ ซาลงไปพร้อม ๆ กับกลุ่มก้อนเมฆที่สลายลงไปอย่างช้า ๆ จนเผยให้เห็น\nสีครามหม่นหมอง"

show rain light:
    alpha 1.0
    linear 5.0 alpha 0.0
with None

stop ambient fadeout 9.0

# "Eventually the rain yields enough for me to close the umbrella, shaking the excess water off before I do."
"จนในที่สุดฝนก็ซาพอที่จะให้หุบร่มได้ ฉันสะบัด ๆ น้ำฝนทิ้งก่อนหุบร่ม"

# "While I wrestle with the mechanism, Rin stops so abruptly that I take five steps before realizing that she's not with me any more."
"ระหว่างที่ฉันกำลังสู้รบตบมืออยู่กับการเก็บร่ม จู่ ๆ รินก็หยุดเดินจนฉันเดินเลยมาห้าก้าวแล้วถึงเห็นว่าเธอไม่ได้\nอยู่ข้าง ๆ ด้วย"

# "Stupid umbrella seems to be jammed."
"เหมือนร่มงี่เง่านี่จะติดไม่ยอมหุบ"

play music music_innocence fadein 6.0

scene ev rin_trueend_normal:
    truecenter
    zoom 1.2 rotate -6 subpixel True
    easein 6.0 zoom 1.0 rotate 0
with locationchange

# "When I turn around, I find her staring at me with an impassive face."
"พอฉันหันไปก็เห็นเธอที่จ้องฉันอยู่ด้วยสีหน้านิ่ง ๆ"

# rin "I wanted someone to say “I understand how you feel.”"
rin "ฉันอยากมีคนที่จะบอกกับฉันว่า “ฉันเข้าใจว่าเธอรู้สึกยังไง”"

# rin "Wouldn't that be great?"
rin "คงจะดีมากเลยนะ"

# "Is that an answer to the question from before? I'm not sure."
"คำตอบของคำถามที่ฉันถามไปหรือเปล่า ฉันไม่แน่ใจ"

# hi "Yeah… but why is it so important?"
hi "อืม… แต่ทำไมถึงได้สำคัญขนาดนั้นล่ะ"

scene ev rin_trueend_sad:
    truecenter
    zoom 1.0 rotate 0 subpixel False
with locationchange

# rin "Because otherwise… I don't know if I can bear this."
rin "เพราะไม่งั้นแล้ว… ฉันไม่รู้ว่าฉันจะรับไหวหรือเปล่า"

# "I was still in the middle of folding my umbrella so I just answered something to get the conversation going, but what she says now freezes my blood."
"ฉันกำลังเก็บร่มอยู่จึงตอบส่ง ๆ ไปพอให้คุยได้ แต่สิ่งที่เธอเพิ่งพูดออกมานั้นทำใจฉันชาวาบ"

scene ev rin_trueend_closed
with locationchange

# rin "If someone says a joke and laughs, you laugh with them, right? Because a joy doubled is a joy tripled, right?"
rin "ถ้ามีคนเล่าอะไรตลกให้ฟังแล้วขำ นายก็ขำด้วย ใช่มั้ย เพราะเวลามีสุขต้องร่วมสุก ใช่มั้ย"
#Should have been "a joy shared is a joy doubled", but Rin. -SC

scene ev rin_trueend_smile
with locationchange

# rin "If someone is hurt and sad, you comfort and hug them, right? Because that way—"
rin "ถ้ามีคนที่กำลังเจ็บปวดและเศร้า นายก็จะปลอบโยนและกอด ใช่มั้ย เพราะเวลา—"

rin "…"

# "She pauses, her mouth still halfway open, then remembers to close it."
"เธอชะงักไปทั้งที่ยังอ้าปากค้าง ก่อนจะรู้ตัวแล้วหุบปากลง"

scene ev rin_trueend_normal
with locationchange

# "A gloom sets on her face and simultaneously on my heart."
"ความมืดหม่นฉายบนใบหน้าเธอพร้อม ๆ กับในใจฉัน"

# rin "I don't know why the right words never come out."
rin "ฉันไม่รู้ว่าทำไมถึงหาคำพูดที่ตรงใจไม่ได้เลย"

# rin "I don't know why I can laugh only when I make myself."
rin "ฉันไม่รู้ว่าทำไมฉันถึงจะหัวเราะได้ก็ต่อเมื่อบังคับให้ตัวเองหัวเราะ"

# rin "I don't know why everything stays only inside me, even when it feels like I'm going to burst."
rin "ฉันไม่รู้ว่าทำไมทุกอย่างถึงอยู่แต่ในตัวฉัน ถึงแม้ตัวฉันจะอัดแน่นจนเหมือนจะระเบิดก็ตาม"

# "Her flat, expressionless face does not waver even when she says that."
"สีหน้าอันเรียบนิ่งของเธอไม่เปลี่ยนแปลงแม้จะพูดประโยคนั้นออกมา"

# "Her usual steady voice becomes only slightly quieter than normal."
"เสียงเรียบนิ่งของเธอเพียงแต่ค่อยลงไปเล็กน้อยเท่านั้น"

# rin "But who… who would ever want to feel like that?"
rin "แต่ใคร… ใครจะอยากรู้สึกอย่างนั้น"

# "Rin looks at me and I imagine the sadness reflecting from her eyes, whether it really is there or not."
"รินมองมาที่ฉัน ฉันจินตนาการถึงความเศร้าที่สะท้อนในแววตาเธอ ไม่ว่าความเศร้าที่ว่าจะมีในแววตาจริง ๆ หรือไม่"

# rin "I don't."
rin "ฉันไม่อยาก"

# rin "I don't want to feel like that."
rin "ฉันไม่อยากรู้สึกอย่างนั้น"

# "We stay silent for a little while after that."
"หลังจากนั้นพวกเราก็เงียบกันไปสักพักหนึ่ง"

# "Rin because she said all she has to say at once, I because I have no clue how to process what she just said."
"ทางรินเป็นเพราะเธอพูดสิ่งที่จะพูดออกไปทีเดียวจนหมด ทางฉันเป็นเพราะไม่รู้จะประมวลผลสิ่งที่เธอเพิ่งบอกอย่างไรดี"

# "I don't understand what Rin is saying. Or I do, but I don't want to."
"ฉันไม่เข้าใจสิ่งที่รินพูด หรือเข้าใจ แต่ไม่อยากเข้าใจ"

# "For the first time both of these things happen, and it has to be simultaneously."
"เป็นครั้งแรกที่ทั้งสองอย่างนั้นเกิดขึ้น และดันเกิดขึ้นพร้อมกัน"

# "The irony is not lost on me."
"นึกแล้วก็ตลกเหลือเกิน"

# hi "I… think everyone wants to be understood. That's universal."
hi "ฉัน… ว่าทุกคนต่างก็อยากให้คนเข้าใจตัวเองทั้งนั้นแหละ"

# hi "But… that is impossible. Not only for me, but for anyone."
hi "แต่… มันเป็นไปไม่ได้ ไม่ใช่แค่กับฉัน แต่กับทุกคน"

# hi "Sae said so too."
hi "ซาเอะก็พูดอย่างนั้น"

# hi "You affect other people and are affected by them, but in the end, you see everything the way only you do."
hi "เธอมีผลกับคนอื่น คนอื่นก็มีผลกับเธอ แต่ท้ายที่สุดแล้ว เธอจะมองอะไรในแบบที่ตัวเองมองเท่านั้น"

# hi "All people… are alone. We just use each other to alleviate that loneliness."
hi "ทุกคน… ล้วนโดดเดี่ยว พวกเราต่างพึ่งพากันและกันเพื่อบรรเทาความโดดเดี่ยวนั้น"

# "I wonder why I put it like that. It just felt that what Sae told me rang true, as if I had always thought like that without knowing it."
"ทำไมฉันถึงใช้คำพูดอย่างนั้นนะ ฉันแค่รู้สึกว่าสิ่งที่ซาเอะพูดมันจริง ราวกับว่าฉันคิดอย่างนั้นมาตั้งนานแล้วโดยไม่รู้ตัว"

# "It feels like she articulated my thoughts in clear, simple words and that stupid story about Picasso."
"ราวกับว่าเธอพูดสิ่งที่ฉันคิดออกมาได้อย่างชัดเจนโดยใช้คำง่าย ๆ และเรื่องโง่ ๆ ของปิกัสโซนั่น"

scene ev rin_trueend_closed
with locationchange

# "Rin droops her head like a withering flower, letting her bangs fall in front of her eyes so that I can't see them."
"รินก้มหัวลงเหมือนดอกไม้ที่เหี่ยวแห้ง หน้าม้าปรกตาเธอจนฉันมองไม่เห็น"

# rin "Why do you say that when you made me feel otherwise?"
rin "นายพูดอย่างนั้น แต่ทำไมนายถึงทำให้ฉันรู้สึกคนละแบบกันเลยล่ะ"

# rin "It's unfair."
rin "ไม่ยุติธรรมเลย"

# "The shaky voice that says those words does not belong to Rin."
"เสียงสั่นเครือที่มาพร้อมคำพูดนั้นไม่ใช่ของริน"

scene ev rin_trueend_sad
with locationchange

# rin "I really thought you could be different. That I wouldn't have to be alone."
rin "ฉันคิดว่านายจะต่างออกไป ว่าฉันจะไม่ต้องอยู่ตัวคนเดียว"

# "It's a bitter voice of disappointment, spoken through clenched teeth and a quivering chest."
"เป็นน้ำเสียงอันขมขื่นที่แสดงความผิดหวังที่ลอดไรฟันออกมาพร้อมหน้าอกที่สั่นระริก"

# hi "I'm sorry…"
hi "ฉันขอโทษ…"

# rin "If you are, why do you say something unfair like that?"
rin "ถ้านายจะขอโทษ ทำไมนายถึงพูดอะไรที่ไม่ยุติธรรมอย่างนั้น"

# "Her demanding tone invokes no particular feeling in me, apart from sadness that has been there since yesterday evening."
"น้ำเสียงอ้อนวอนของเธอไม่ได้ทำให้ฉันรู้สึกอะไรเป็นพิเศษ นอกจากความรู้สึกเศร้าที่อยู่ในใจมาตั้งแต่เย็นเมื่อวาน"

# "She doesn't intimidate me at all. Not any more."
"ฉันไม่กลัวเธอแล้ว ไม่กลัวอีกต่อไป"

# "Rin is not a prodigal art genius, nor an unpredictable idiot savant who could tear the logic lobe of my brain into shreds whenever she opened her mouth."
"รินไม่ใช่ศิลปินอัจฉริยะ ไม่ใช่คนมีความสามารถโง่เง่าเดาใจไม่ถูกที่เปิดปากทีไรก็สามารถพังสมองส่วนตรรกะของฉัน\nได้ทุกเมื่อ"

# "She is just a girl that I thought I loved, a loved one who wanted to be my friend, a friend whom I let down."
"เธอก็เป็นเพียงผู้หญิงคนหนึ่งที่ฉันคิดว่าฉันรัก คนที่ฉันรักที่อยากเป็นเพื่อนกับฉัน เพื่อนที่ฉันทำให้ผิดหวัง"

# hi "I say that, because saying otherwise would feel like lying."
hi "ถ้าฉันไม่พูดอย่างนั้นมันก็จะเป็นการโกหกน่ะสิ"

scene ev rin_trueend_normal
with locationchange

# rin "Why?"
rin "ทำไม"

# "Simple questions are the hardest ones. I have to close my eyes so I can focus my thoughts enough to answer her."
"คำถามสั้น ๆ นั้นยากเสมอ ฉันต้องหลับตาลงเพื่อตั้งสมาธิจดจ่อให้พอที่จะตอบคำถามเธอ"

# hi "I'm no artist. I can never be on the same level with you."
hi "ฉันไม่ใช่ศิลปิน ฉันยืนอยู่ข้างเธอไม่ได้"

# hi "There is a world only you can see, and to be part of it I would have to become you."
hi "เธอจะมีโลกที่มีแค่เธอมองเห็น และถ้าฉันจะเป็นส่วนหนึ่งของโลกใบนั้นฉันก็ต้องเป็นเธอ"

# hi "That's something I can't do, no matter how much you wish me to."
hi "ซึ่งฉันทำไม่ได้ ไม่ว่าเธอจะอยากให้ฉันเป็นแค่ไหนก็ตาม"

# "Rin takes in my explanation without batting an eyelash."
"รินฟังคำอธิบายของฉันตาไม่กะพริบ"

# rin "I'm not a real artist either."
rin "ฉันก็ไม่ใช่ศิลปินตัวจริงเหมือนกัน"

# rin "I just paint because it makes me feel like I can really feel something."
rin "ฉันแค่วาดเพราะพอวาดแล้วฉันจะรู้สึกว่ารู้สึกอะไรได้จริง ๆ"

scene ev rin_trueend_weaksmile
with locationchange

# "She holds her breath for a while before releasing it in a long, sigh-like flow."
"เธอกลั้นหายใจครู่หนึ่งก่อนจะปล่อยลมพรูออกมาคล้ายถอนหายใจ"

scene ev rin_trueend_closed
with locationchange

# rin "That's why I'll do it."
rin "เพราะงั้นฉันจะทำ"

# rin "I have decided. I'll do it. If even Hisao says that, then that's what I will do."
rin "ฉันตัดสินใจแล้ว ฉันจะทำ ต่อให้ฮิซาโอะพูดอย่างนั้น ฉันก็จะทำอย่างนั้น"
#Leaving "Hisao says" in rather than "you say". -SC

# hi "Do what?"
hi "ทำอะไร"

# "Rin starting a little shows that she had regressed into talking to herself again, but I'm glad I can snap her back even now."
"รินที่สะดุ้งเล็กน้อยทำให้ฉันรู้ว่าเธอกลับไปคุยกับตัวเองอีกแล้ว แต่ก็ดีใจที่แม้แต่ตอนนี้ฉันก็ยังดึงให้รินสนใจกันได้"

scene ev rin_trueend_normal
with locationchange

# rin "Teacher and Sae have talked with someone who is a very important person. I got a scholarship for a big art school in Tokyo."
rin "คุณครูกับซาเอะคุยกับคนหนึ่งที่เป็นคนสำคัญมาก ฉันได้ทุนไปเรียนต่อโรงเรียนศิลปะใหญ่ในโตเกียว"

# rin "He said I could transfer there and start after the summer is over, if I wanted to."
rin "เขาบอกว่าถ้าอยากจะย้ายไปเริ่มเรียนที่นั่นหลังหมดช่วงปิดเทอมฤดูร้อนแล้วเลยก็ได้"

# rin "I don't really get why—"
rin "ฉันไม่เข้าใจจริง ๆ ว่าทำไม—"

stop music fadeout 10.0

# hi "Hold on, what? Why didn't you tell?"
hi "เดี๋ยว อะไรนะ ทำไมเธอถึงไม่บอกกันเลย"

scene ev rin_trueend_smile
with locationchange

# rin "I just did. You are the first one I told because I decided it just now."
rin "ก็เพิ่งบอกไปนี่ไง ฉันบอกนายเป็นคนแรกเพราะฉันเพิ่งตัดสินใจได้เมื่อกี้"

# "She keeps her cool, looking only mildly surprised at my shocked interjection."
"เธอยังคงทำทีสบาย ๆ ดูแปลกใจเล็กน้อยที่ฉันอุทานด้วยความตกตะลึง"

# "It's ridiculous how easily she can say something so life-changing."
"บ้าไปแล้ว พูดอะไรที่พลิกชีวิตอย่างนั้นออกมาได้ง่าย ๆ ได้ยังไง"

# "I can't believe it. After what happened in February, I have had enough change for this year."
"ไม่อยากจะเชื่อเลย แค่เรื่องเมื่อเดือนกุมภาพันธ์ก็เป็นการเปลี่ยนแปลงที่เกินทนแล้ว"

# "Even if things are going badly right now, I don't want everything to change."
"ถึงตอนนี้อะไร ๆ จะไม่ราบรื่น แต่ฉันก็ไม่อยากให้ทุกอย่างเปลี่ยนไป"

# hi "But what about Yamaku? Don't you want to graduate with everyone?"
hi "แล้วยามากุล่ะ เธอไม่อยากจบพร้อมทุกคนเหรอ"

# "My plea evokes no emotion."
"คำอุทธรณ์ของฉันไร้ซึ่งอารมณ์ใดตอบกลับ"

# rin "Everyone who?"
rin "ทุกคนใคร?"

# hi "Emi, me, everyone!"
hi "เอมิ ฉัน ทุกคนไง!"

# "I feel my pulse rising unnervingly, and my breathing becomes fast and shallow."
"ฉันสัมผัสได้ถึงชีพจรของฉันที่เต้นรัวเร็วพร้อมลมหายใจที่หอบกระชั้น"

# "I don't want this to happen."
"ฉันไม่อยากให้เป็นอย่างนี้"

# rin "Their life is not mine."
rin "ชีวิตเขาไม่ใช่ชีวิตฉัน"

# rin "You just said that everyone is alone."
rin "นายก็เพิ่งพูดเองว่าทุกคนล้วนโดดเดี่ยว"

# hi "I didn't mean it like that—"
hi "ฉันไม่ได้หมายความอย่างนั้น—"

# rin "You always said that you'd have to seize the day and start living your life."
rin "นายพูดมาตลอดว่าต้องทำวันนี้ให้ดีที่สุดแล้วใช้ชีวิตของตัวเองต่อ"

# rin "I have to live my life too."
rin "ฉันก็ต้องใช้ชีวิตของฉัน"

# "Rin is twisting my words to justify running away again. It makes me angry."
"รินบิดเบือนคำพูดฉันเพื่อทำให้การที่ตัวเองหนีไปนั้นไม่ใช่เรื่องที่ผิดอีกแล้ว โมโหเหลือเกิน"

# "Her ease, finality and seriousness in announcing this is unacceptable."
"การที่เธอสั่งลาส่งท้ายด้วยความจริงจังง่าย ๆ อย่างนั้นนั้นเกินจะให้อภัย"

# "As if changing your life is something you can do on a moment's whim! No!"
"ทำอย่างกับว่าการเปลี่ยนชีวิตเป็นอะไรที่นึกจะทำก็ทำได้งั้นแหละ! ไม่เลย!"

# hi "How can you say that? Why don't you even try to belong?"
hi "เธอพูดอย่างนั้นได้ยังไง ทำไมเธอไม่พยายามทำตัวให้เข้ากับคนอื่นบ้าง"

# "The desperate accusation has no effect. It feels like I am once again out of weapons, that I can't reach through to her no matter what I try."
"คำกล่าวโทษอันกระเสือกกระสนนั้นไร้ผลใด ๆ  เหมือนฉันไม่มีอะไรจะสู้ด้วยอีกแล้ว ไม่ว่าจะทำยังไงก็ส่งอะไรไปถึงเธอ\nไม่ได้เลย"

# "Rin is so frustratingly absolute in her own judgment that it might make me hate her if I didn't love her, even though I don't know which way I am feeling any more."
"รินนั้นแน่วแน่กับการตัดสินใจตัวเองเสียจนฉันหงุดหงิด ฉันคงเกลียดเธอไปแล้วถ้าฉันไม่ได้รักเธอ ถึงตอนนี้จะไม่รู้แล้ว\nก็เถอะว่ารู้สึกอย่างไหน"

scene ev rin_trueend_normal
with locationchange

# rin "Maybe I am that kind of a person. The kind that belongs only to herself."
rin "บางทีฉันคงเป็นคนอย่างนั้น คนที่เข้ากับได้แค่ตัวเอง"

# hi "I won't accept that."
hi "ฉันไม่เอาด้วยหรอก"

# "Her nonchalant eyes do not seem to care whether I accept her decision or not."
"สายตาไม่ยี่หระของเธอดูจะไม่สนใจเลยว่าฉันจะเอาด้วยการตัดสินใจของเธอหรือเปล่า"

"…"

# "The pause lets me cool down, to find my sensibilities."
"ช่วงที่หยุดพูดไปนั้นฉันค่อย ๆ สงบใจให้ความเป็นเหตุผลกลับเข้าตัว"

# "While I do, the parting rainclouds reveal a setting sun that still has time to shine its last few warming rays before calling it a day."
"ระหว่างนั้นเหล่าเมฆที่แยกออกจากกันเผยให้อาทิตย์อัสดงที่เหลือแสงอันอบอุ่นอีกไม่มากก่อนที่จะลาลับไปปรากฏ"

# "A mosaic of light and shadow spreads on the walls of the buildings, on the street and the fence circling a park on the other side of the street."
"แสงวอมแวมและเงาแผ่ไปทั่วกำแพงตึกรามบ้านช่อง แผ่ไปทั่วถนนและทั่วรั้วที่ล้อมสวนสาธารณะที่อยู่อีกฟากถนน"

# "Rin's shadow is long enough to reach my feet."
"เงารินนั้นทอดยาวมาจนถึงเท้าฉัน"

# "It's like one of those western movies, with two cowboys staring each other down, ready to sling their guns at each other."
"บรรยากาศเหมือนหนังตะวันตกพวกนั้นที่มีคาวบอยสองคนจ้องกันโดยหันปืนเข้าหากันและกัน"

# "The one who loses his nerve will eat lead."
"ใครตาขาวไปก่อนจะต้องกินลูกตะกั่ว"

# "I realize I would have the disadvantage because the sun is behind Rin, stinging my eyes."
"แล้วฉันก็รู้ว่าฉันคงเสียเปรียบเพราะรินหันหลังให้พระอาทิตย์อยู่ แสงอาทิตย์นั้นแยงตาฉัน"

scene ev rin_trueend_sad
with locationchange

# rin "Do you hate me?"
rin "เกลียดฉันเหรอ"

# "She draws first and I have no counter."
"เธอชักปืนออกมาก่อนโดยที่ฉันไม่มีอะไรตอบโต้"

# hi "I don't know."
hi "ไม่รู้สิ"

# "Did I lose?"
"ฉันแพ้แล้วเหรอ"

# hi "Even if I did, what would it matter?"
hi "เกลียดหรือเปล่าสำคัญด้วยเหรอ"

# "I scramble for words, words that could salvage this. I find none."
"ฉันควานหาคำพูดที่พอจะประคับประคองสถานการณ์นี้ได้ ฉันหาไม่เจอเลย"

# hi "You are my friend, I promised you that. I am not the kind of guy who forgets about promises."
hi "เธอเป็นเพื่อนฉัน ฉันสัญญาแล้ว ฉันไม่ใช่พวกที่ลืมสัญญาหรอก"

# hi "I think that is the most important thing. We could try to—"
hi "ฉันว่านั่นแหละคือสิ่งที่สำคัญที่สุด พวกเรายัง—"

scene ev rin_trueend_normal
with locationchange

# rin "Don't say it."
rin "อย่าพูด"

scene ev rin_trueend_hug
with locationchange

play music music_friendship fadein 4.0

# "Predicting what I was going to say, Rin throws herself into my arms, pressing her body against mine."
"รินทายว่าฉันจะพูดอะไรต่อแล้วทิ้งตัวเข้ามาในอ้อมกอดฉันพลางกดตัวเธอเข้ากับหน้าอกฉัน"

# "I feel her rising to her tiptoes to match my height and snuggle closer."
"ฉันสัมผัสได้ว่าเธอเขย่งเท้าขึ้นมาทดความสูงฉันให้ซุกตัวเข้ามาใกล้ขึ้น"

# "The scent of her hair is that of rain and paint thinner. Her body feels as cold as always. Her breathing against my neck is as hot as always."
"ฉันได้กลิ่นฝนและทินเนอร์จากผมเธอ ตัวเธอเย็นอย่างเคย ลมหายใจเธอที่รดคอฉันร้อนอย่างเคย"

# "It's funny how all of those feel so familiar even though Rin, as a whole, does not."
"แปลกดีที่พอแยกสัมผัสแต่ละอย่างแล้วชวนให้คุ้นเคยเหลือเกิน แต่พอมองรินรวม ๆ แล้วไม่รู้สึกเลย"

scene ev rin_trueend_hugclosed
with locationchange

# rin "Are you sure you can't hate me?"
rin "แน่ใจนะว่าไม่เกลียดฉัน"

# "Rin whispers into my ear so close I can feel the movements of her lips against my earlobe."
"รินกระซิบอยู่ข้างหูฉันจนสัมผัสได้ถึงริมฝีปากเธอที่ขยับอยู่ตรงติ่งหูฉัน"

# "It's teasing, taunting. If this was some other kind of situation I'm sure it would tickle tantalizingly and I would giggle even though I'm a guy."
"ราวเป็นการหยอกล้อและล่อหลอก ถ้าไม่ใช่ว่าเป็นอย่างนี้ฉันคงจั๊กจี้จนหลุดขำไปแล้ว ถึงฉันจะเป็นผู้ชายก็เถอะ"

# rin "It would be easier if you did."
rin "ถ้าเกลียดฉันแล้วจะง่ายขึ้นนะ"

# hi "Dunno. It's pretty hard when you are hugging me like that."
hi "ไม่รู้สิ กอดกันอย่างนี้แล้วจะให้ทำใจเกลียดยังไงลง"

scene ev rin_trueend_sad
with locationchange

# "I wonder if it's because of my sullen voice, but she takes a step back, looking wistfully at her short arms."
"ไม่แน่ใจว่าเป็นเพราะเสียงฉันฟังดูอารมณ์ไม่ดีหรือเปล่าเธอถึงได้ผละตัวออกแล้วมองแขนสั้น ๆ ของตัวเองอย่าง\nเศร้าสร้อย"

# "I wish she hadn't done that."
"เธอไม่น่าทำอย่างนั้นเลย"

# rin "I can't hug anyone, Hisao."
rin "ฉันกอดใครไม่ได้ ฮิซาโอะ"

# rin "I'm a bad person like that."
rin "ฉันเป็นคนไม่ดีอย่างนั้นแหละ"

scene ev rin_trueend_normal
with locationchange

# rin "That's why I have to go."
rin "ฉันถึงต้องไป"

# "She disarms me completely with three simple sentences, rendering me unable to argue any more."
"เพียงสามประโยคง่าย ๆ นั้นเธอก็ปลดอาวุธฉันทิ้งได้จนหมดไม่เหลืออะไรให้สู้หรือเถียงกลับ"

# "And since I can't, Rin is free to continue as she wills, shifting her weight from one foot to the other before she does."
"และเมื่อฉันตอบโต้ไม่ได้รินจึงพูดต่อไปตามใจอยาก เธอยืนสลับเท้าเอนตัวโงนเงนไปมา"

scene ev rin_trueend_smile
with locationchange

# rin "I will learn to hug people in my own way."
rin "ฉันจะหัดกอดคนในแบบของฉัน"

# rin "I'm sure I can become a real artist."
rin "ฉันมั่นใจว่าฉันเป็นศิลปินตัวจริงได้"

# rin "But if I do… I might not be able to be me any more."
rin "แต่ถ้าฉันได้เป็น… ฉันคงเป็นฉันไม่ได้อีกต่อไป"

# "The hint of a smile on her lips is a betrayal, a false sign of self-confidence in a future that even Rin can't foresee."
"รอยยิ้มบนริมฝีปากเธอทรยศคำพูดนั้น เป็นสัญญาณถึงความมั่นใจแบบปลอม ๆ ที่มีต่ออนาคตที่แม้แต่ตัวรินก็ไม่อาจ\nทำนายได้"

# "I'd want to interpret it as a sign of hope, but I know better."
"ฉันอยากจะตีความไปว่ารอยยิ้มนั้นเป็นความหวัง แต่ใจฉันรู้ดี"

# "Rin just keeps smiling that awkward, forced smile of hers."
"รินเอาแต่ยิ้มแกน ๆ ฝืน ๆ อยู่อย่างนั้น"

# rin "That's why… please forget about me, and I will forget about you too."
rin "เพราะอย่างนั้น… ได้โปรดลืมฉัน แล้วฉันก็จะลืมนายด้วย"

# rin "I'm sure that—{w=0.5}{nw}"
rin "ฉันมั่นใจว่า—{w=0.5}{nw}"

scene ev rin_trueend_sad
with locationchange

# "She chokes in the middle of saying something I would never come to hear."
"เธอสะอื้นขึ้นมากลางทางกับคำพูดนั้นที่ฉันคงไม่มีวันได้ยิน"

# "I don't think I'd wanted to hear it anyway."
"ฉันก็คงไม่อยากได้ยินอยู่ดีนั่นแหละ"

# "This is not fair."
"ไม่ยุติธรรมเลย"

# "Rin is not joking. Rin is always serious. But I can't accept it, I can't."
"รินไม่ได้ล้อเล่น รินจริงจังเสมอ แต่ฉันยอมรับไม่ได้ ไม่"

# "Forget about you? How could I ever…?"
"ลืมเธอเหรอ จะให้ลืมยังไงลง…?"

# "That's what I'd like to say. But I don't know how I would continue. I can't come up with anything good to say, so I have to challenge her."
"ฉันอยากจะพูดอย่างนั้น แต่ฉันไม่รู้จะพูดต่อยังไง ฉันหาอะไรที่ตรงใจมาพูดไม่ได้เลย ฉันจึงต้องท้าทายเธอ"

# hi "How can you say such a thing?"
hi "เธอพูดอย่างนั้นออกมาได้ยังไง"

scene ev rin_trueend_normal
with locationchange

# "Rin raises her eyes to meet mine, they are serious and deep, a perfect image of the uncharted territory I always thought they were."
"รินเงยหน้าขึ้นมามองฉัน สายตาเธอจริงจังและลึกล้ำ เหมือนอย่างกับพื้นที่ที่ยังไม่มีการสำรวจบนแผนที่อย่างที่ฉัน\nเคยคิดไว้เลย"

# "Even now, I can't read her emotions from those unblinking, jade irises that never could reflect what they saw."
"ขนาดตอนนี้ฉันก็ยังดูอารมณ์เธอจากม่านตาสีหยกที่ไม่กะพริบนั้นไม่ออก เป็นม่านตาที่ไม่อาจสะท้อนสิ่งที่เห็นอยู่"

# rin "It's easy. After all, I am good at forgetting things."
rin "ง่ายจะตายไป ฉันลืมเก่งนี่นา"

"…"

# "Her unfairness is choking my throat, but I manage to utter the question burning my mind."
"ความไม่ยุติธรรมจากเธอนั้นทำฉันจุกคอหอย แต่ฉันยังเค้นคำถามหนึ่งที่สุมอยู่ในอกให้ออกมาจากปากได้"

# hi "So, is this it? Is this goodbye?"
hi "แล้วจบกันแค่นี้เหรอ ต้องลากันตรงนี้เหรอ"

"…"

# "Rin kept looking at me gently, without answering my question."
"รินเอาแต่มองฉันอย่างอ่อนโยนโดยไม่ตอบคำถามนั้น"

# "From her eyes I could see that she didn't even need to say anything."
"แค่มองตาฉันก็รู้ว่าเธอไม่ต้องพูดอะไรแล้วหรอก"

# "There were no more words for us."
"ระหว่างเราจะไม่มีคำพูดต่อกันอีกแล้ว"

stop music fadeout 12.0

scene ev rin_trueend_gone
with locationchange

# "She turned around and walked off without looking back."
"เธอหันหลังแล้วเดินออกไปไม่กลับมามอง"

# "All around me, the world kept changing, little by little, but I was left standing there."
"โลกรอบตัวฉันเปลี่ยนแปลงไปทีละเล็กละน้อยโดยทิ้งให้ฉันยืนอยู่ตรงนี้"

scene ev rin_trueend_gone:
    "ev rin_trueend_gone_ni" with Dissolve(10.0)
with None

# "The sun dropped below the horizon, casting long and thin shadows across the street."
"พระอาทิตย์ลับขอบฟ้า เงาทอดยาวไกลพาดไปตามถนน"

# "In the waning light, Rin's distancing back seemed to be like from a faraway dream."
"แผ่นหลังของรินที่อยู่ไกล ๆ ในแสงอาทิตย์ที่โรยราลงนั้นดูราวกับว่าเธออยู่ในฝันอันไกลห่าง"

# "The gap between us grew slowly."
"ช่องว่างระหว่างเราค่อย ๆ แยกออก"

# "The ripples on the puddles she stepped on expanded until they met the limits of their tiny existence and disappeared without a trace."
"คลื่นบนแผ่นน้ำที่กระเพื่อมจากฝีเท้าเธอกระจายออกเป็นวงกว้างกระทั่งจนถึงขีดจำกัดอันเล็กจ้อยของมันก่อนจะ\nหายไปอย่างไร้ร่องรอย"

# "Her words stayed frozen deep inside my heart."
"คำพูดของรินติดค้างอยู่ในใจเบื้องลึกของฉัน"

window hide


label th_R38:

#this scene picks up from the end of R34, as you might've guessed.
scene bg school_room34
with None

show rin negative_spaciness
with charaenter

play music music_drama fadein 6.0

# "She's standing in the middle of the sunlit room, peering through the gaps of the curtains out into the yard."
"เธอยืนอยู่กลางห้องที่แดดสาดส่องมองผ่านช่องระหว่างผ้าม่านออกไปยังสวน"

# "Like so often before, she doesn't start or jump, just calmly waits for me to make the first move."
"และเหมือนอย่างทุกที เธอไม่ตกใจหรือสะดุ้งเลย แค่รออยู่นิ่ง ๆ ให้ฉันเป็นคนเริ่มก่อน"

# "It's as if she is trying to become a permanent part of the furniture."
"ราวกับว่าเธอจะทำตัวเป็นส่วนหนึ่งไปกับเฟอร์นิเจอร์ในห้อง"

# hi "The teacher is looking for you."
hi "ครูตามหาตัวเธออยู่"

# "A blank look over her shoulder is all I get, accompanied by a cryptic nonexpression on her face."
"เธอเพียงหันมามองฉันนิ่ง ๆ ด้วยใบหน้าเรียบเฉยเข้าใจยาก"

# rin "Are you looking for me too?"
rin "นายตามหาฉันอยู่ด้วยเหรอ"

# hi "Nah, I already found you, didn't I?"
hi "ไม่อะ ก็เจอเธอแล้วนี่"

# rin "Did you?"
rin "เหรอ?"

show rin negative_annoyed
with charachange

# "She furrows her brow, looking so puzzled that it makes me wonder if the question was asked in all seriousness."
"เธอขมวดคิ้วดูสับสนจนฉันคิดแล้วว่าคำถามของเธอนั้นถามจริงจังหรือเปล่า"

# "Maybe it was."
"อาจจะใช่"

# hi "Are you talking metaphorically now?"
hi "เมื่อกี้หมายถึงเจอแบบเปรียบเปรยเหรอ"

show rin negative_spaciness
with charachange

# rin "Do you mean like eels, caves and dark, stormy nights?"
rin "หมายถึงแบบปลาไหล ถ้ำ กับคืนพายุมืดมิด?"

show rin negative_sad
with charachange

# rin "I am bad at talking like that."
rin "ฉันคุยแบบนั้นไม่เก่ง"

"…"

play sound sfx_doorclose

# "The abruptly-ended greetings give me the chance to close the door behind me and sit down on a dust-covered desktop."
"การทักทายที่จบลงอย่างกะทันหันเปิดช่องให้ฉันได้ปิดประตู จากนั้นฉันจึงมานั่งบนโต๊ะที่มีฝุ่นเกาะอยู่"

show rin basic_absent
with charachange

# "Rin stays standing, but at least she turns around."
"รินยังยืนเหมือนเดิม แต่อย่างน้อยก็หันมามองแล้ว"

# "I soon wish she didn't though, so oppressive is her expectant stare."
"แต่ไม่อยากให้มองเลย สายตาเฝ้ารอของเธอนั้นกดดันเหลือเกิน"

# "This is her place and I'm an intruder, although a tolerated one. Despite that, she still waits for me to say something."
"ห้องนี้เป็นห้องของเธอ ส่วนฉันเป็นผู้บุกรุก ถึงเธอจะไม่ว่าอะไรก็เถอะ แต่ถึงอย่างนั้นเธอก็รอให้ฉันพูดอะไรสักอย่าง"

# "If I only knew what."
"ถ้าฉันรู้ว่าต้องพูดอะไรน่ะนะ"

"…"

# "The sunlit silence presses me towards decisions."
"แสงอาทิตย์กดดันให้ฉันต้องคิด"

# "I came here without really thinking what I would do, apart from delivering Nomiya's short message in case Rin was here."
"ฉันมาโดยไม่ได้คิดมาก่อนว่าจะทำอะไรต่อ นอกจากการส่งข้อความสั้น ๆ ที่โนมิยะฝากบอกถ้าเจอริน"

# "She was, and now I don't know what else I want to say… what else I should say?"
"ซึ่งเจอแล้ว แล้วตอนนี้ฉันก็ไม่รู้จะพูดอะไรอีก… ฉันควรจะพูดอะไรอีกดี"

# "I hover between my two options for a moment."
"ตอนนี้ฉันชั่งใจอยู่ระหว่างสองตัวเลือก"

# "Rin being troubled troubles me too. It's a surprising revelation, almost as big as realizing that she really is troubled was."
"พอรินไม่สบายใจแล้วฉันก็พลอยไม่สบายใจด้วย พอรู้ตัวอย่างนั้นแล้วฉันก็รู้สึกประหลาดใจ ประหลาดใจพอ ๆ กับการ\nที่ได้รู้ว่าเธอไม่สบายใจ"

# "Nothing I can do would probably help, and I might be partially to blame too."
"ฉันคงช่วยอะไรเธอไม่ได้เลย เผลอ ๆ ส่วนหนึ่งจะเป็นความผิดฉันด้วย"

# "Does it mean I should just wash my hands of her?"
"หมายความว่าฉันควรจะวางมือกับเธอเสียทีงั้นหรือ"

# "Didn't think so."
"ฉันไม่คิดว่าอย่างนั้น"

# hi "So… what's wrong?"
hi "แล้ว… เป็นอะไร"

"…"

show rin relaxed_nonchalant
with charachange

# rin "Nothing."
rin "ไม่มีอะไร"

# "She starts to turn away again, as if trying to physically exit a conversation she doesn't want to have."
"เธอหันหน้าหนีอีกแล้ว เหมือนเป็นการทำท่าเพื่อออกไปจากบทสนทนาที่เธอไม่อยากมีส่วนร่วมด้วย"

# hi "Rin, stop trying to dodge me or I'll leave."
hi "ริน เลิกหลบหน้าฉัน ไม่งั้นฉันจะไปละนะ"

show rin relaxed_boredom
with charachange

# rin "Okay."
rin "โอเค"

# hi "Do you want me to leave?"
hi "อยากให้ฉันไปเหรอ"

show rin relaxed_doubt
with charachange

# rin "Are you still angry?"
rin "นายยังโกรธอยู่เหรอ"

# "It took us - or was it only me? - ten seconds to swamp the conversation into this."
"พวกเรา—หรือแค่ฉัน?—ใช้เวลาไปสิบวินาทีถึงวกเข้ามาเรื่องนี้ได้"

# "I wish we could erase the past, or failing that, forget all about it."
"ฉันอยากจะลบอดีต หรือถ้าลบไม่ได้ก็อยากจะลืมไปให้หมด"

# "I've wished for that more than once in the last few months."
"ช่วงสองสามเดือนมานี้ฉันคิดอย่างนั้นมามากกว่าหนึ่งครั้งแล้ว"

# hi "Let's put that aside for the time being, all right?"
hi "เรื่องนั้นเอาไว้ก่อน นะ?"

show rin basic_absent
with charachange

# rin "If you say so."
rin "ถ้านายว่าอย่างนั้น"

# hi "I do. So… what's wrong?"
hi "ฉันว่าอย่างนั้น แล้ว… เป็นอะไร"

# hi "Sae and Nomiya were not too happy that you just ran off yesterday."
hi "ซาเอะกับโนมิยะไม่ค่อยปลื้มเลยนะที่เธอหนีไปเมื่อวานน่ะ"

# hi "You left them in quite a pinch, and I suppose the teacher wants some kind of an explanation."
hi "เล่นเอาสองคนนั้นลำบากเลย ครูเองก็คงอยากได้คำอธิบายด้วย"

# hi "It seemed like you just threw out everything you had worked for. And I don't get why."
hi "ดู ๆ แล้วมันเหมือนว่าเธอทิ้งทุกอย่างที่เธอลงแรงมาตลอดเลย ซึ่งฉันไม่เข้าใจว่าทำไม"

show rin basic_deadpanupset
with charachange

# rin "Did I make a mistake?"
rin "ฉันทำผิดเหรอ"

# "My reprimanding and her flat answer go so much against the usual expectations and presumed interactions that it might just as well be somebody else talking."
"ทั้งการที่ฉันดุ ทั้งคำตอบเรียบ ๆ ของเธอนั้นช่างผิดแผกไปจากการปฏิสัมพันธ์โดยปกติและยังหลุดไปจาก\nความคาดหมายที่คิดว่าจะเป็นเหมือนอย่างทุกทีจนให้ความรู้สึกเหมือนว่าที่คุยกันอยู่ตรงนี้เป็นคนอื่น"

# "Neither of us is like we used to be, this stiff, constricting feeling I get every time I look at Rin nowadays seems to be mirrored in her own behavior."
"พวกเราทั้งสองคนไม่มีใครเป็นอย่างที่เคยเป็น ความรู้สึกเกร็ง ๆ และอึดอัดรัดแน่นทุกครั้งที่ได้มองรินทุกวันนี้ดูจะมีเหตุ\nมาจากพฤติกรรมของเธอ"

# "I hate things that go irreparably wrong. Ever since February, I have hated them."
"ฉันไม่ชอบอะไรที่ผิดพลาดจนยากจะแก้ไข ฉันเกลียดสิ่งเหล่านั้นมาตั้งแต่เมื่อเดือนกุมภาพันธ์นั้นแล้ว"

# "What can I say?"
"จะให้ว่ายังไงเล่า"

# "Her question is trailed by a compelling, quizzical stare that makes me sigh and frown."
"คำถามของเธอตามมาด้วยสายตาสงสัยอันดึงดูดที่ทำให้ฉันต้องถอนหายใจพร้อมขมวดคิ้ว"

# "Conversations nobody wants to have are the worst."
"บทสนทนาที่ไม่มีใครอยากมีส่วนร่วมนั้นแย่ที่สุดในสามโลก"

# hi "I don't know. I mean, it's not the end of the world but it probably was pretty stupid."
hi "ไม่รู้สิ คือ มันก็ไม่ใช่เรื่องคอขาดบาดตายอะไรขนาดนั้นหรอก แต่มันก็คงงี่เง่าพอตัวแหละ"

show rin relaxed_nonchalant
with charachange

# "She responds with a sigh of her own, although hers is not nearly as heavy as mine was."
"เธอถอนหายใจตอบบ้าง ถึงจะไม่ได้ถอนหายใจแรงเท่าฉันก็เถอะ"

show rin relaxed_sleepy
with charachange

# rin "I just couldn't do it."
rin "ไม่ว่าจะยังไงฉันก็ทำไม่ได้"

# hi "But… why? What's wrong?"
hi "แต่… ทำไม? เป็นอะไร"

show rin negative_annoyed
with charachange

# "A pause, a furrowed brow, a quiet voice."
"หยุดชะงัก ขมวดคิ้ว เสียงแผ่วเบา"

# rin "Let it be, Hisao."
rin "ช่างมันสิ ฮิซาโอะ"

# rin "I don't think I can really explain it in a way that would make sense."
rin "ฉันว่าฉันอธิบายให้ใครเข้าใจไม่ได้หรอก"

# "Yeah, Rin doesn't want to have this conversation either. That may be for the better."
"อืม รินก็ไม่อยากมีส่วนร่วมกับบทสนทนานี้ด้วยเหมือนกัน ซึ่งก็คงจะดีแล้ว"

# "But how rare of her, to admit that even she has some kind of limits."
"แต่ไม่ค่อยได้เห็นเท่าไหร่ที่เธอจะยอมรับว่าแม้แต่เธอเองก็มีขีดจำกัดเหมือนกัน"

# "I always thought Rin was all but ignorant of her tendency to get distracted, so much that she inadvertently obfuscates everything she says."
"ฉันคิดมาตลอดว่ารินนั้นทำเป็นไม่สนใจว่าสมาธิเธอหลุดได้ง่าย "

"…"

# hi "You never explain {b}anything{/b} in a way that would make sense."
hi "เธอไม่เคยอธิบาย{b}อะไร{/b}ให้ใครเข้าใจได้เลย"

show rin basic_absent
with charachange

# rin "Nobody else has ever asked me to."
rin "ไม่เคยมีใครขอฉัน"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

# n "I guess that's how it is."
n "ก็คงเป็นอย่างนั้น"

# n "But I always wanted to make sense of you, to find out who you are."
n "แต่ฉันอยากจะเข้าใจเธอมาตลอด อยากจะรู้ว่าเธอเป็นใคร"

# n "I still want to, can't you see?"
n "และฉันยังอยากรู้อยู่ เธอไม่เห็นหรือไง"

n "…"

# n "I know you can't."
n "ฉันรู้ว่าเธอไม่เห็น"

# n "But I do."
n "แต่ฉันเห็น"

# n "Is that why I keep this up? It pains you as much as it pains me. It's unlikely to be of any use to either."
n "เพราะแบบนี้หรือเปล่าฉันถึงได้ไม่ยอม ยิ่งอยู่เธอยิ่งเจ็บ แต่ฉันก็เจ็บพอกัน ดูแล้วไม่น่าจะได้อะไรขึ้นมาด้วยซ้ำ"

# n "We did things and said things that can't be undone."
n "พวกเราต่างได้ทำและพูดในสิ่งที่ย้อนกลับไปแก้ไขไม่ได้แล้ว"

# n "It's as if… you and me being close to each other just hurts us both, but we still deliberately keep doing it."
n "เหมือนกับว่า… ทั้งที่เธอกับฉันพออยู่ใกล้กันแล้วก็ต้องเจ็บตัวกันทั้งคู่ แต่พวกเราก็ยังตั้งใจจะอยู่ต่อไป"

# n "Isn't that silly?"
n "งี่เง่าเนอะ"

# n "Even now, I can see how you force yourself to respond even though you owe me nothing."
n "ขนาดตอนนี้ฉันยังดูออกเลยว่าเธอฝืนตัวเองแค่ไหนเพื่อที่จะตอบฉัน ทั้งที่เธอไม่ได้ติดค้างอะไรกับฉันแท้ ๆ"

# n "Even if it's hard to talk about things like this."
n "ขนาดว่าการคุยอะไรอย่างนี้มันลำบากปากแท้ ๆ"

# n "Why?"
n "ทำไม"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear
window show

# hi "Why is it that you paint?"
hi "ทำไมเธอถึงวาด"

show rin basic_awayabsent
with charachange

# rin "I… because I don't know what else I could do."
rin "ฉัน… เพราะฉันไม่รู้แล้วว่าจะทำอะไรอย่างอื่นได้อีก"

# rin "It's like this feeling that there is no choice, that it's the only possibility."
rin "เหมือนความรู้สึกที่ไม่มีทางเลือก เหมือนเป็นความเป็นไปได้เดียว"

show rin basic_sad
with charachange

# rin "Like when there are only watermelon-flavored popsicles left in the store but you need to eat a popsicle."
rin "เหมือนร้านเหลือแค่ไอติมรสแตงโมแต่อยากกินไอติม"

# "Her poor metaphor aside, she didn't really answer anything. If possible, this makes even less sense than not knowing."
"ถ้าไม่นับการเปรียบเทียบห่วย ๆ นั่นแล้ว เธอไม่ได้ตอบอะไรเลย เผลอ ๆ จะยิ่งพาให้งงหนักกว่าการที่ไม่รู้อีก"

# hi "But… if you don't want to paint…"
hi "แต่… ถ้าเธอไม่อยากวาด…"

show rin negative_spaciness
with charachange

# rin "Not like that. You had to come to this school even though you probably didn't want to have a heart attack."
rin "ไม่ใช่อย่างนั้น นายต้องมาโรงเรียนนี้ต่อให้นายอาจจะไม่อยากหัวใจวาย"

show rin negative_annoyed
with charachange

# "She pauses, frowning as if something in what she said didn't please her."
"เธอชะงักไปแล้วขมวดคิ้วเหมือนสิ่งที่เธอพูดนั้นไม่ค่อยเป็นที่น่าพอใจเท่าไหร่"

show rin basic_lucid
with charachange

# rin "At least I think you wouldn't."
rin "อย่างน้อยฉันก็คิดว่านายคงไม่อยาก"

# "Her careful follow-up is followed in turn by another, shorter pause with another, smaller frown."
"เธอพูดต่ออย่างระมัดระวังก่อนจะชะงักแล้วขมวดคิ้ว แต่ไม่ได้ขมวดคิ้วแน่นเท่ารอบเมื่อครู่"

show rin basic_deadpanupset
with charachange

# rin "Would you like to have a heart attack?"
rin "นายอยากหัวใจวายมั้ย"

# hi "No, I wouldn't and I didn't want to."
hi "ไม่ ไม่อยาก ไม่เอาแล้ว"

show rin basic_deadpansurprised
with charachange

# rin "But you're doing fine, aren't you? Or are you still sad about it?"
rin "แต่นายก็ยังอยู่ได้สบายดีนี่ หรือนายยังเศร้าอยู่"

# "Rin's question makes me realize that I haven't really thought about my illness for weeks."
"คำถามของรินทำให้ฉันนึกได้ว่าฉันไม่ได้คิดเรื่องอาการของฉันมาหลายสัปดาห์แล้ว"

# "Aside from chugging down my medication every day there has been no need to concern myself with my broken heart, which I'm only thankful for, really."
"นอกจากเรื่องที่ต้องกระเดือกยาอยู่ทุกวันแล้วฉันก็ไม่ต้องคิดมากเรื่องหัวใจพัง ๆ ของฉัน ซึ่งฉันก็ยินดีเหลือแสน"

# "Getting to know new people, a new school, a new town… a new life, it all has caught me and made the past fade away."
"ทั้งการได้รู้จักคนใหม่ ๆ ทั้งโรงเรียนใหม่ ๆ ทั้งเมืองใหม่ ๆ … ทั้งชีวิตใหม่ เหล่านั้นอยู่ติดกับตัวฉันจนทำให้อดีตลบเลือน"

# hi "No… heh, I guess even I can't dwell on the past indefinitely."
hi "ไม่… ฮะ ๆ ฉันคงจะเอาแต่จมอยู่กับอดีตไปเรื่อย ๆ ไม่ได้ละนะ"

show rin basic_awayabsent
with charachange

# rin "See? Even watermelon doesn't really taste bad if you have to eat it."
rin "เห็นมั้ย ขนาดแตงโมก็ไม่ได้ไม่อร่อยถ้าต้องกิน"

# "Her half-nonsensical closure seems to put an end to the subject in Rin's mind, so I just nod in uncertain confirmation."
"คำปิดท้ายที่ออกจะไม่รู้เรื่องนั้นดูท่าจะเป็นการจบสิ่งที่รินคิดอยู่ ฉันจึงพยักหน้าไปกึ่ง ๆ ไม่แน่ใจ"

"…"

"…"

# "There are two kinds of silences: awkward ones that you want to break, and comfortable ones that you don't mind."
"ความเงียบมีสองแบบ คือแบบที่ชวนให้อึดอัดจนอยากพูด กับแบบไม่อึดอัดที่อยู่ได้สบาย ๆ"

# "The first kind is bad, because it makes your thoughts go awry. Like mine do, now."
"แบบแรกนั้นไม่ดีเพราะทำให้จิตใจฟุ้งซ่าน เหมือนอย่างฉันตอนนี้"

# "Looking at Rin makes me feel bad."
"พอมองรินแล้วฉันก็รู้สึกแย่"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

# n "\nI don't want to feel like this."
n "\nฉันไม่อยากรู้สึกอย่างนี้"

# n "Looking at Rin makes me feel… exhausted. I really tried my best, she tried to… I have no idea."
n "พอได้มองรินแล้วฉันก็รู้สึก… หมดแรง ฉันพยายามเต็มที่แล้ว ส่วนเธอก็พยายาม… ฉันไม่รู้เลย"

# n "But we ended up like this, and she ended up screwing up her exhibition opening."
n "แต่เราอยู่มาจนเป็นอย่างนี้ และเธอก็ทำงานเปิดตัวงานนิทรรศการพัง"

# n "It feels like we are at a dead end."
n "รู้สึกเหมือนพวกเรามาถึงทางตัน"

# n "There is no direction to continue to."
n "ไม่มีทางให้ไปต่อ"

# n "I reached out for her yesterday, thinking it would be the last time."
n "เมื่อวานฉันก็เข้าหาเธอเพราะคิดว่าคงจะเป็นครั้งสุดท้าย"

# n "She walked away."
n "เธอเดินหนี"

# n "“I want to be me.”"
n "“ฉันอยากเป็นฉัน”"

# n "What the heck does that even mean? Rin, if anyone, is most definitely herself."
n "หมายความว่ายังไงกันแน่ ถ้าให้เทียบกับคนอื่น ๆ แล้ว รินนั่นแหละที่เป็นตัวเองที่สุด"

# n "I feel kinda relieved that I am not the one to blame, but this still grates on my mind."
n "ฉันค่อนข้างโล่งใจที่ฉันไม่ได้เป็นคนผิด แต่ก็ยังติดใจสงสัยอยู่ดี"

# n "Why did she run away? It didn't make sense yesterday. It doesn't make sense today."
n "ทำไมเธอถึงหนีไป เมื่อวานไม่เข้าใจ วันนี้ไม่เข้าใจ"

# n "The things she said feel like they should make sense but they just don't, to me."
n "ฉันรู้สึกเหมือนว่าพอเธอพูดอย่างนั้นแล้วใคร ๆ จะต้องเข้าใจทันที แต่ไม่เลย ฉันไม่เข้าใจ"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear
window show

# hi "You know, about that thing you just said…"
hi "เนี่ย เรื่องที่เธอบอก…"

show rin basic_absent
with charachange

# rin "Which one of them?"
rin "เรื่องไหน"

# hi "Umm… painting… Sae said something like that to me before… that a true artist does not paint because she wants to, but because she {b}must{/b}."
hi "เอ่อ… เรื่องวาด… ซาเอะก็เคยบอกอะไรอย่างนั้นกับฉันเหมือนกัน… ว่าศิลปินตัวจริงไม่ได้วาดเพราะอยาก แต่วาดเพราะ\n{b}ต้อง{/b}วาด"

# hi "And I've been wondering about what she said. Why do artists {b}have{/b} to paint?"
hi "แล้วฉันก็สงสัยมาตลอด ว่าทำไมศิลปินถึง{b}ต้อง{/b}วาด"

# "My question is probably pretty stupid. At least Rin looks at me in the blank way that seems to say so."
"คำถามของฉันอาจจะดูโง่ ๆ เพราะอย่างน้อยรินก็มองฉันนิ่ง ๆ คล้ายจะบอกว่าอย่างนั้น"

show rin basic_deadpannormal
with charachange

# rin "I don't know. Am I an artist?"
rin "ไม่รู้สิ ฉันเป็นศิลปินหรือเปล่า"

# hi "Well, you paint stuff and you have an exhibition too. I'd say you qualify."
hi "ก็ เธอวาดรูป แล้วก็จัดงานนิทรรศการด้วย ฉันว่าคงนับได้แหละ"

show rin basic_deadpancontemplation
with charachange

# rin "I think I still don't know, but okay."
rin "ฉันคิดว่าฉันยังไม่รู้ แต่โอเค"

# "The thinking pause that follows seems to last for half an eternity."
"เธอหยุดพลางคิดไปนานอย่างน้อย ๆ น่าจะสักครึ่งชาติได้"

# "Unlike most people, Rin doesn't flavor her thinking pauses by body language or saying “like” or “umm” or anything."
"รินไม่ได้เหมือนอย่างคนส่วนมากที่เวลาหยุดพลางคิดจะใส่ท่าทางหรือคำพูดอย่าง “แบบ” หรือ “อืมม” ประกอบด้วย"

# "I've noticed that I might prefer her way. The usual way even annoys me, as if people were so infatuated by the sound of their own voice they just have to keep making some noise even when they are just thinking what they could say next."
"ฉันรู้สึกว่าฉันชอบอย่างของรินมากกว่า เพราะแบบปกติจะให้ความรู้สึกรำคาญว่าคนเรานั้นหลงเสียงตัวเองเหลือเกิน\nจนขนาดเวลาหยุดไปคิดว่าจะพูดอะไรต่อยังต้องเปล่งเสียงอะไรสักอย่างออกมา"

# "Rin just… comes to a full stop while she is thinking. It's disconcerting, because reacting to people spacing out is always hard, but she comes off as less obnoxious."
"รินแค่… หยุดไปเลยเวลาที่เธอกำลังคิดอยู่ ซึ่งชวนให้กระอักกระอ่วนเหมือนกันเพราะเวลามีคนเหม่อแล้วก็ไม่รู้จะต้อง\nตอบสนองยังไง แต่เธอก็ไม่ได้น่ารำคาญขนาดนั้น"

show rin basic_lucid
with charachange

# rin "I think I want someone to see what's inside me. Not the way doctors and serial killers do."
rin "ฉันคิดว่าฉันอยากให้คนเห็นว่าอะไรอยู่ในตัวฉัน ไม่ได้หมายถึงแบบอย่างหมอหรือฆาตกรต่อเนื่องนะ"

show rin basic_absent
with charachange

# rin "The way that doesn't make me feel lonely."
rin "แบบอย่างที่จะไม่ทำให้ฉันโดดเดี่ยว"

show rin relaxed_boredom
with charachange

# rin "This is what you call metaphorical, you see."
rin "นี่แหละที่เขาเรียกว่าการเปรียบเปรยนะ"

# hi "Please don't lecture me about self-evident things."
hi "อย่ามาสอนฉันเรื่องอะไรที่เห็นได้ชัดอย่างนั้นเลย"

show rin basic_deadpansurprised
with charachange

# rin "It's not self-evident that this is self-evident."
rin "ไม่ได้เห็นได้ชัดว่าเรื่องนี้เห็นได้ชัดสักหน่อย"

# hi "So, you present a painting to someone and expect him to magically see a glimpse of your soul?"
hi "แล้วเธอก็จะเอารูปวาดไปให้ใครสักคนดู แล้วก็คาดหวังให้คนนั้นเห็นจิตวิญญาณของเธอได้โดยอัศจรรย์เลยน่ะนะ"

show rin negative_angry
with charachange

# rin "It's not like that. It's just a little like that but not really. Don't you understand?"
rin "ไม่ใช่อย่างนั้น ก็อย่างนั้นนิดหน่อยแต่ไม่เท่าไหร่ นายไม่เข้าใจเหรอ"

# hi "I do… and I don't."
hi "เข้าใจ… และไม่เข้าใจ"

# hi "You know, I feel a little bit of despair every time you ask that question."
hi "รู้มั้ยว่าฉันแอบหดหู่ทุกครั้งที่เธอถามคำถามนั้น"

show rin basic_absent
with charachange

# rin "What question?"
rin "คำถามไหน"

# hi "About whether I understand you or not."
hi "ที่ถามว่าฉันเข้าใจเธอหรือเปล่าน่ะ"

# "She seems almost surprised at my clarification."
"รินดูจะตกใจที่ฉันบอกอย่างนั้น"

show rin basic_lucid
with charachange

# rin "Oh, it's not really a question. It's one of those kind that you don't have to answer."
rin "อ้อ ไม่ใช่คำถามเท่าไหร่หรอก เป็นคำถามเชิงนั้นที่ไม่ต้องตอบ"

# hi "Rhetorical."
hi "เชิงวาทศิลป์"

show rin basic_absent
with charachange

# rin "Yeah, that's the word, a question that is not a question is a rhetorical question. How nice."
rin "อืม คำนั้นแหละ คำถามที่ไม่ใช่คำถามเรียกว่าคำถามเชิงวาทศิลป์ ดีจัง"

# rin "That reminds me, it doesn't really make sense. What kind of a question is one that isn't a question?"
rin "ซึ่งจะว่าไปแล้ว ไม่เห็นสมเหตุสมผลเลย คำถามอะไรที่ไม่ใช่คำถาม?"

# hi "A rhetorical one."
hi "คำถามเชิงวาทศิลป์"

# rin "What kind of an answer is an answer that doesn't answer anything?"
rin "คำตอบอะไรที่ไม่ได้ตอบอะไรเลย"

# hi "Is that a rhetorical question?"
hi "อันนั้นคำถามเชิงวาทศิลป์หรือเปล่า"

show rin basic_deadpanupset
with charachange

# rin "You are not funny."
rin "นายนี่ไม่ตลกเลย"

show rin basic_awayabsent
with charachange

# rin "But if you don't like it, would you like me to say something else instead?"
rin "แต่ถ้านายไม่ชอบ อยากให้ฉันพูดอะไรอย่างอื่นแทนมั้ย"

show rin basic_lucid
with charachange

# rin "I don't have any good ones though. How about… “Your pants are on fire?”"
rin "แต่ฉันไม่มีอะไรดี ๆ จะพูดนะ เอาเป็นว่า… “กางเกงนายติดไฟ”?"

show rin basic_absent
with charachange

# rin "This can be our secret language."
rin "เป็นภาษาลับระหว่างเราได้นะ"

# "Rin's honest-to-goodness silliness, made twice more ridiculous by the fact that I know she is dead serious, derails me like it always does."
"ความติ๊งต๊องแบบซื่อ ๆ ของรินที่ยิ่งดูไร้สาระไปใหญ่เพราะฉันรู้ว่าเธอจริงจังนั้นทำให้ฉันตามเธอไม่ทันตลอด"

# "It's like some kind of a safety lock to prevent me from becoming too much of a worrywart, dragging even my own thoughts off the ground where they should be."
"ราวกับว่าเป็นระบบนิรภัยที่ป้องกันไม่ให้ฉันเป็นคนขี้กังวล เพราะความคิดฉันจะถูกลากไปจากพื้นที่ที่มันควรจะอยู่"

# "It makes me smile confusedly, but only on the inside."
"ทำให้ฉันยิ้ม—แต่แค่ในใจ—อย่างสับสน"

# "Even though the corners of my mouth are not drawing into a grin, I'm still impressed by her ease of wrecking any attempt at being too serious."
"ถึงปากฉันจะไม่ได้ยิ้ม แต่ฉันก็ประทับใจที่เธอทำลายความพยายามที่จะทำให้เรื่องจริงจังได้อย่างง่ายดาย"

# "Could she (should she will so) forget and ignore things that bug her, things that bother her?"
"(หากเธอต้องการ) เธอจะลืมและเมินสิ่งต่าง ๆ ที่คอยกวนใจเธอได้หรือเปล่า"

# "Could she (should she will so) be free of whatever burden being her means?"
"(หากเธอต้องการ) เธอจะเป็นอิสระจากภาระที่เกิดจากการเป็นตัวเธอได้หรือเปล่า"

# "Or am I the only one who feels burdened by being myself?"
"หรือมีแค่ฉันที่รู้สึกเหมือนแบกภาระจากการเป็นตัวเองอยู่?"

# hi "No thanks."
hi "ไม่ละ ขอบใจ"

# hi "But still, the times when I feel that I am on the same page as you are pretty rare."
hi "แต่ก็นะ ฉันไม่ค่อยจะเห็นตรงกันกับเธอเท่าไหร่เลย"

# hi "It feels like… there is this huge gap and sometimes you just go to the other side, and I don't… have any way to reach to you from where I am."
hi "รู้สึกเหมือน… มีช่องว่างกว้าง ๆ อยู่ช่องหนึ่ง แล้วบางทีเธอก็จะไปอยู่อีกฟาก แล้วถ้าให้เริ่มจากจุดที่ฉันยืนอยู่ ฉันก็จะ\nไม่… มีวิธีที่จะไปถึงเธอเลย"

# hi "It's like you are in some completely different place at times."
hi "บางทีก็เหมือนว่าเธออยู่คนละที่กันเลย"

# hi "Even though you are right here."
hi "ถึงเธอจะอยู่ตรงนี้เลยก็เถอะ"

# "That's right."
"ใช่แล้ว"

# "There is an insurmountable discontinuity, an imaginary glass wall that blocks comprehension from happening."
"มีจุดไม่ต่อเนื่องอันกว้างใหญ่อยู่ เป็นกำแพงแก้วที่มองไม่เห็นที่คอยป้องกันไม่ให้เกิดความเข้าใจกันได้"

# "There might be such a gap between any two people, but with Rin, it feels more tangible."
"ระหว่างคนสองคนใด ๆ ก็อาจจะมีช่องว่างอย่างนั้นอยู่ แต่กับรินแล้วช่องว่างนั้นจะรู้สึกเหมือนจับต้องได้ขึ้นมา"

# "Rin does not react to my thoughts, not to the ones I uttered aloud nor the ones I did not."
"รินไม่ตอบสนองใด ๆ กับความคิดฉัน ไม่ว่าจะเป็นความคิดที่ถูกเปล่งเสียงออกมา หรือความคิดที่อยู่ในใจก็ตาม"

# hi "It's even worse with art."
hi "กับศิลปะยิ่งแล้วใหญ่"

# hi "I'm not very good at art, I admit it."
hi "ฉันยอมรับว่าฉันไม่เก่งเรื่องศิลปะ"

# hi "I joined the art club 'cause I thought it could be interesting."
hi "ฉันเข้าชมรมศิลปะเพราะคิดว่าคงน่าสนใจดี"

# hi "And I guess it is. I like art, I like your art too, but just like with you, I can't comprehend it."
hi "ซึ่งก็น่าสนใจดีละมั้ง ฉันชอบผลงานเธอด้วย แต่ก็เหมือนอย่างเธอนั่นแหละ ฉันไม่เข้าใจ"

# hi "And I'm pretty sure nobody really can."
hi "แล้วฉันก็ค่อนข้างแน่ใจด้วยว่าคงไม่มีใครเข้าใจหรอก"

show rin relaxed_doubt
with charachange

# "This seems to worry her slightly."
"ดูท่าว่าเธอจะคิดมากหน่อย ๆ แล้ว"

# rin "Do you think so?"
rin "คิดว่าอย่างนั้นเหรอ"

# hi "Yeah. I guess that art is meant to be interpreted, not understood. That's how I'd put it."
hi "อืม ศิลปะเอาไว้ตีความมากกว่าที่จะให้ใครมาเข้าใจมากกว่าละมั้ง ฉันว่าอย่างนั้นนะ"

show rin relaxed_sleepy
with charachange

# rin "That's a sad thought."
rin "เป็นความคิดที่หดหู่จัง"

# hi "I guess it might feel like one."
hi "ก็คงงั้นแหละมั้ง"

# hi "Does it make you feel sad for yourself?"
hi "ได้ฟังแล้วหดหู่กับตัวเองมั้ยล่ะ"

show rin basic_lucid
with charachange

# "Rin thinks about this for a while, and then shakes her head surprisingly vehemently."
"รินคิดอยู่พักหนึ่งก่อนจะส่ายหน้าแรงผิดคาด"

show rin basic_deadpannormal
with charachange

# "The first thing she focuses her eyes on afterward is me."
"สิ่งที่ตาเธอจับจ้องเป็นสิ่งแรกหลังจากนั้นคือฉัน"

# "Both of these things make me glad, and relieved."
"ทั้งสองการกระทำนั้นให้ฉันดีใจและโล่งใจ"

# hi "That's good, isn't it? Anyway, you should go see the teacher and apologize properly."
hi "ก็ดีแล้วนี่ แต่นั่นแหละ ไปขอโทษครูให้เป็นเรื่องเป็นราวดีกว่านะ"

# hi "I think he is worried about you."
hi "ครูคงเป็นห่วงเธอ"

# hi "Can you do that?"
hi "ทำได้มั้ย"

show rin basic_absent
with charachange

# "This time, she nods her head."
"คราวนี้เธอพยักหน้า"

stop music fadeout 4.0

# "Only, it's not as vehement."
"เพียงแต่ไม่ได้แรงเท่า"


label th_R39:

scene bg school_hallway3
with locationchange

# "The hallway is empty, almost intimidating."
"โถงทางเดินนั้นเงียบสงัดจนน่าขนลุก"

# "Nomiya's “office” is the art classroom at the other end of the third floor hallway."
"“ห้องทำงาน” ของโนมิยะคือห้องเรียนศิลปะที่อยู่สุดโถงทางเดินชั้นสามอีกฟาก"

show rin basic_absent at center
with charaenter

# "Our steps echo disturbingly. The atmosphere is unlike on a normal afternoon. It feels like the school knows that nobody will be coming back for a month, too."
"เสียงฝีเท้าของเราก้องจนน่ากลัว บรรยากาศโดยรอบไม่เหมือนอย่างยามบ่ายยามปกติ ราวกับว่าอาคารโรงเรียนก็รู้\nเหมือนกันว่าจะไม่มีใครมาอีกเป็นเวลาหนึ่งเดือน"

# "The door is open, but not very inviting."
"ประตูเปิดไว้อยู่ แต่ดูไม่น่าเข้าเลย"

# hi "I'll… um, wait outside."
hi "ฉันจะ… เอ่อ รออยู่ข้างนอกนะ"

show rin relaxed_nonchalant
with charachange

with Pause(0.2)

show rin invis at tworight
with dissolvecharamove

hide rin
with None

# "Nodding barely noticeably, Rin strides in without stopping, and naturally, without knocking."
"รินพยักหน้าเล็กน้อยจนแทบดูไม่ออก เธอไม่หยุดแล้วเดินต่อเข้าไปโดยไม่เคาะประตู"

# "Maybe that's why it takes a few seconds before I hear the teacher's voice from inside."
"คงเพราะอย่างนี้ถึงต้องรอสักสองสามวินาทีกว่าจะได้ยินเสียงคุณครูที่อยู่ในห้อง"

# no "There you are!"
no "มาจนได้!"

# rin "Hello."
rin "สวัสดี"

# "A conflict arises: should I stay here or go somewhere else?"
"แล้วฉันก็ต้องเลือก ว่าจะอยู่หรือไปที่อื่นก่อน"

# "I'm not sure if I even want to eavesdrop on them."
"ฉันไม่แน่ใจด้วยซ้ำว่าจะอยากอยู่แอบฟังหรือเปล่า"

"…"

show bg school_hallway3 at right
with charamove

# "Manners lose to curiosity, and so I stay close enough to listen in."
"ความอยากรู้หนักกว่ามารยาท ฉันจึงเข้าไปให้ใกล้พอที่จะได้ยินด้วย"

# "Their voices echo in the hallway, but no matter."
"เสียงสองคนนั้นดังก้องไปทั่วโถงทางเดิน แต่ไม่สำคัญ"

# "There is nobody around, save for me."
"แถวนี้ไม่มีใครเลยนอกจากฉัน"

play music music_tragic fadein 8.0

# no "Dear girl, what on Earth were you thinking, leaving like that on the big night?"
no "นี่เธอคิดอะไรอยู่ถึงได้ทิ้งงานใหญ่ไว้อย่างนั้นแล้วหนีไปน่ะ"

# rin "I couldn't say anything."
rin "พูดอะไรไม่ได้เลย"

# "Compared to Nomiya's scolding tone, Rin sounds awfully quiet and withdrawn."
"ให้เทียบกับน้ำเสียงดุ ๆ ของโนมิยะแล้ว เสียงรินนั้นค่อยและฟังดูหงิม ๆ"

# "Her words seem to drown under his."
"ฟังดูเหมือนคำพูดของรินจะโดนคำพูดคุณครูกลบหมด"

# no "I have to say, I am very disappointed in you, Tezuka."
no "ฉันต้องขอบอกว่าฉันผิดหวังในตัวเธอมากนะ เทซูกะ"

# rin "It was no good at all."
rin "ใช้ไม่ได้เลยค่ะ"

# no "Never mind all the things I did for you, but what about Sae? What about all the guests who wanted to meet you?"
no "เอาเป็นว่าหลายอย่างที่ฉันทำไปเพื่อเธอน่ะช่างก่อน แต่ซาเอะล่ะ แขกที่อยากมาเจอเธอล่ะ"

# rin "There was nobody. Even Hisao…"
rin "ไม่มีใครเลย แม้แต่ฮิซาโอะ…"

# no "You have embarrassed us very badly, Tezuka."
no "เธอทำพวกฉันขายหน้ามากนะ เทซูกะ"

# no "Reputation is what counts, surely you know that?"
no "ชื่อเสียงน่ะสำคัญ เธอคงรู้ใช่มั้ย"

# rin "It's all right. I don't need it."
rin "ไม่เป็นไรค่ะ ไม่ต้องการค่ะ"

# no "“Don't need!” What do you think you know?"
no "“ไม่ต้องการ!” เธอจะไปรู้อะไร"

# "Rin's replies only seem to agitate the teacher more, his voice rising with every sentence."
"คำตอบของรินยิ่งทำให้คุณครูฉุนหนักจนขึ้นเสียงดังขึ้นทุกประโยค"

# no "The path of an artist is a thorny one, I'll tell you that! Thorny!"
no "เส้นทางศิลปินน่ะเต็มไปด้วยขวากหนาม จะบอกให้! เต็มไปด้วยขวากหนาม!"

# no "You have to see the big picture! There will be bad times and good times!"
no "เธอต้องมองภาพรวมนะ! มันก็มีทั้งช่วงที่ไม่ดีและช่วงที่ดี!"

# rin "Things are like they are. It'll be all right even—"
rin "อะไรก็เป็นของมันอย่างนั้นแหละค่ะ ไม่เป็นไรหรอกค่ะ ถึง—"

# no "You might now think that it's oh so wonderful and easy, but how far would you have gotten without me?"
no "เธออาจจะคิดว่าชีวิตมันช่างแสนสบายเหลือเกิน แต่ถ้าไม่มีฉันแล้วเธอจะไปได้ไกลสักแค่ไหนกันเชียว"

# no "I won't always be there for you!"
no "ฉันไม่ได้อยู่ค้ำฟ้านะ!"

# no "When you lie on the floor of your minuscule room, your rent three weeks late, your mind blank for the fourth week straight, then you will wish that you had listened to old Nomiya a bit more."
no "สักวันเถอะ วันที่เธอนอนอยู่ในห้องแคบ ๆ ที่เธอค้างค่าเช่ามาสามสัปดาห์โดยที่หัวสมองไม่มีอะไรเลยมาสี่สัปดาห์แล้ว\nวันนั้นเธอจะสำนึกว่าน่าจะฟังตาแก่โนมิยะเอาไว้บ้าง"

# no "When you keep measuring how the shadow of your chair becomes longer over the spring because that's all your lethargy allows, maybe that's when you will start caring about your career!"
no "วันที่เธอขี้เกียจจนได้แต่นั่งวัดเงาเก้าอี้ที่ยาวขึ้นตลอดช่วงฤดูใบไม้ผลิ วันนั้นเธอคงจะหันมาคิดเรื่องอาชีพของตัวเอง\nบ้าง!"

# rin "That doesn't matter."
rin "ไม่สำคัญค่ะ"

# no "Your resolve is not enough."
no "เธอไม่เด็ดเดี่ยวพอ"

# rin "I am not a resolved person."
rin "พอดีไม่ได้เป็นคนเด็ดเดี่ยวค่ะ"

# no "You are not a resolved person…"
no "เธอไม่ได้เป็นคนเด็ดเดี่ยว…"

play sound sfx_impact2
with vpunch

# no "Then tell me, why… why… WHY DID WE GO THROUGH ALL THIS TROUBLE IF IT AMOUNTS TO A MOSQUITO'S SHIT?"
no "งั้นบอกหน่อยสิ ทำไม… ทำไม… ทำไมพวกเราถึงได้ทุ่มเทกันขนาดนี้ ถ้าผลมันจะออกมาเล็กเท่าขี้มดอย่างนี้น่ะ!!"

# "Oh dear, the teacher blew a fuse."
"ตาย ๆ คุณครูปรี๊ดแตกแล้ว"

# "Him yelling at Rin makes me feel bystander's guilt. If I had gone with her, maybe he wouldn't have gotten so angry."
"พอได้ยินคุณครูตะคอกใส่รินแล้วก็ทำให้ฉันรู้สึกผิดขึ้นมาด้วยเลย ถ้าฉันไปประกบด้วยคงไม่โกรธขนาดนี้"

# "If I had not let her run away, he wouldn't have gotten angry in the first place."
"ถ้าฉันไม่ปล่อยให้เธอหนีไปแต่แรกก็คงไม่โกรธเลยด้วยซ้ำ"

# "I still could go and save her… I don't think I can."
"ฉันยังเข้าไปช่วยรินไว้ได้ทันอยู่… ฉันว่าฉันทำไม่ได้หรอก"

# "I was the same. I yelled at Rin too, and I'm feeling all the more embarrassed about it now."
"ฉันก็เหมือนกัน ฉันก็ตะคอกใส่ริน แล้วตอนนี้ก็ยิ่งรู้สึกอับอายไปใหญ่"

# "I felt justified to vent my anger at her face just because… just because I felt it was her fault that I was so frustrated."
"ที่ฉันคิดว่าตัวเองทำถูกที่ระเบิดอารมณ์ใส่รินไปจัง ๆ อย่างนั้นก็เพราะ… ก็เพราะฉันรู้สึกว่ารินเป็นคนทำให้ฉันหงุดหงิด"

# "I was no more justified than the teacher is."
"ฉันไม่ได้ทำถูกไปกว่าคุณครูเลย"

"…"

# "A terrible silence sets upon the hallway."
"ความเงียบที่ชวนให้ขนลุกปกคลุมทั่วโถงทางเดิน"

# "Rin does not have anything to say to Nomiya."
"รินไม่มีอะไรจะพูดกับโนมิยะอีก"

# "Whether she has run out of answers or she knows that arguing would only make him angrier is anyone's guess."
"ไม่มีใครอาจทราบว่าเธอไม่ตอบเพราะไม่รู้จะตอบอะไรหรือเพราะรู้ว่ายิ่งเถียงไปก็ยิ่งทำให้คุณครูโกรธ"

# "The teacher has nothing more to say either, it seems, or maybe he just ran out of breath."
"คุณครูก็ไม่มีอะไรจะพูดเหมือนกัน ดูทรงแล้ว หรือไม่ก็แค่หายใจไม่ทัน"

# "For a moment, I imagine the two of them just staring at each other, one full of red-hot anger, the other full of… yes, what?"
"แวบหนึ่งฉันนึกภาพทั้งสองคนจ้องตากัน คนหนึ่งโมโหเลือดขึ้นหน้า อีกคน… นั่นสิ รู้สึกยังไง"

# "I can't tell how Rin feels, not before, not now."
"ฉันไม่รู้ว่ารินรู้สึกยังไง ไม่ว่าจะก่อนหน้านี้ หรือตอนนี้"

# "Teacher seems to expect Rin to say something too, but since she doesn't he finally continues in a quieter, but not less angry voice."
"คุณครูก็เหมือนจะรอให้รินพูดอะไรด้วย แต่เมื่อเธอไม่ตอบ คุณครูจึงพูดต่อด้วยเสียงที่เบาลง แต่ความโกรธไม่ได้เบาลง\nด้วยเลย"

# no "What worth is there in doing so much work if the outcome is… nothing?"
no "แล้วจะทุ่มเทกันไปทำไมถ้าผลลัพธ์มันจะออกมา… เป็นศูนย์น่ะ"

# "Still, Rin will not say anything."
"และรินก็ยังจะไม่พูดอะไร"

# no "I'm sorry. I shouldn't have gotten so excited."
no "ขอโทษนะ ฉันไม่น่าไปบ้าขนาดนั้นเลย"

# "He does not sound sorry at all. Rather, his tone is cold and sharp, like he was spitting the words out of his mouth."
"น้ำเสียงเขาไม่ได้สำนึกเลย เป็นน้ำเสียงเย็นเยียบและทิ่มแทงราวกับว่าเป็นคำพูดที่ถ่มถุยออกมา"

# no "It seems that I was expecting too much. You are not an artist after all."
no "ฉันคงคาดหวังมากไป เธอไม่ใช่ศิลปินจริง ๆ ด้วย"

# "Yeah, not sorry at all."
"อืม ไม่ได้สำนึกเลย"

show nomiya serious:
    tworight
    alpha 0.0
    parallel:
        linear 1.0 center
    parallel:
        linear 0.4 alpha 1.0
        0.2
        linear 0.4 alpha 0.0
with Pause(1.0)

stop music fadeout 4.0

# "He storms out of the club room and down the stairs without noticing me."
"คุณครูก้าวฉับ ๆ ออกห้องลงบันไดไปโดยไม่ทันสังเกตเห็นฉัน"

# "After he is gone, I peek carefully inside the classroom."
"พอคุณครูออกไปแล้วฉันก็แอบมองเข้าไปในห้องเรียน"

scene bg school_nomiya at right
show rin basic_awayabsent at center
with locationchange

# "Rin is left standing there, in front of the teacher's desk."
"รินยังยืนอยู่หน้าโต๊ะครูตรงนั้น"

show rin negative_spaciness
with charachange

# rin "I couldn't say I am sorry."
rin "ฉันพูดขอโทษไม่ออก"

# "She says it into the humid air of the classroom, not to me."
"เธอไม่ได้พูดกับฉัน แต่พูดอยู่กับอากาศอันอับชื้นในห้อง"

# "But since the room won't answer her, I will have to."
"แต่ในเมื่อห้องไม่ตอบ ฉันจึงต้องตอบ"

# hi "That was unfair of him… He was angry, but still…"
hi "ไม่ยุติธรรมเลย… รู้แหละว่าโกรธ แต่ก็…"

# "I can't decide how to end my sentence. Disdaining the teacher feels like disdaining my own behavior from two days ago."
"ฉันไม่รู้จะลงท้ายประโยคยังไงดี ถ้าดูถูกคุณครู ก็จะเหมือนเป็นการดูถูกพฤติกรรมของฉันเมื่อสองวันก่อนด้วย"

# "Stupid, but correct in hindsight."
"โง่ แต่ย้อนคิดแล้วก็จริง"

show rin negative_spaciness_close
with characlose

# "Rin won't answer, staying petrified where she stands, so I walk up to her."
"รินไม่ตอบ เธอยังยืนนิ่งอยู่ที่เดิม ฉันจึงเดินเข้าไปหาเธอ"

# "She stood up for herself. In a way. I didn't expect that."
"ในแง่หนึ่งเธอก็ได้ยืนหยัดสู้ ซึ่งฉันไม่ได้คาดคิดเลย"

# "I can't determine whether it's unbecoming or not, but either way, she did it."
"ฉันไม่แน่ใจว่าจะเป็นไปได้หรือเปล่า แต่นั่นแหละ เธอทำได้แล้ว"

# "Against me, she never did."
"ซึ่งเธอไม่เคยทำอย่างนั้นกับฉันเลย"

# "I sort of wish she had, maybe I would not feel this bad then."
"ก็แอบหวังว่าตอนนั้นเธอจะทำอย่างนั้นบ้างน่ะนะ ฉันอาจจะไม่ต้องมารู้สึกผิดขนาดนี้ก็ได้"

# "Lately, it really seems that I've been wishing for all kinds of things."
"ดูเหมือนว่าช่วงนี้ฉันหวังนั่นอยากนี่หลายอย่างไปหมด"

# hi "Rin?"
hi "ริน?"

show rin negative_annoyed_close
with charachange

# rin "Go away."
rin "ไปเลย"


label th_R40:

scene bg school_nomiya at right
show rin negative_annoyed_close at center
with None

play music music_sadness fadein 6.0

# hi "Why… what are you saying?"
hi "ทำไม… เธอว่ายังไงนะ"

show rin negative_angry_close
with charachange

# rin "You're angry with me too, right?"
rin "นายก็โกรธฉันเหมือนกันใช่มั้ย"

# rin "I thought you were my friend. I thought he was, too."
rin "ฉันนึกว่านายเป็นเพื่อนฉัน นึกว่าครูเป็นด้วย"

# "Her voice is unlike I've ever heard it, it's bitter, sharp like needles, and she keeps staring pointedly at her toes."
"ฉันไม่เคยได้ยินเสียงเธอเป็นอย่างนี้ เป็นเสียงที่ขมขื่นและทิ่มแทงเหมือนเข็มแหลม เธอเอาแต่จ้องมองนิ้วเท้าเธอ"

# hi "I don't think it's about that."
hi "ฉันว่าไม่ใช่เรื่องนั้นหรอก"

# hi "He wanted you to be something you are not. And…"
hi "ครูอยากให้เธอเป็นอะไรที่ไม่ใช่เธอ แล้ว…"

show rin basic_surprised_close
with charachange

# "I take a deep breath and finally catch her eyes in my own, locking our gazes."
"ฉันสูดหายใจลึก ๆ ในที่สุดเธอก็เงยหน้าขึ้นมามองจนตาประสานตา"

# hi "…I'm sorry. I wanted us to be something else too… more than friends."
hi "…ฉันขอโทษ ฉันก็อยากให้เราเป็นอย่างอื่นเหมือนกัน… มากกว่าเพื่อน"

# hi "Maybe that's why I couldn't contain myself and became so frustrated, just like the teacher did."
hi "คงเพราะอย่างนั้นฉันถึงได้ทนไม่ไหวจนหงุดหงิดขึ้นมาเหมือนอย่างครู"

show rin relaxed_doubt_close
with charachange

# rin "What more? There is nothing more to me than me, that's all I am. I don't understand that."
rin "มากกว่าอะไร? ฉันเป็นอะไรที่มากกว่าฉันไม่ได้แล้ว ฉันก็มีอยู่แค่นี้ ฉันไม่เข้าใจ"

# "Well… the answer should be obvious, right?"
"ก็… คำตอบน่าจะชัดแล้วนี่ ใช่มั้ย"

# "I remember myself, thinking of the purpose of friendship. To put up with everything and anything, to be there for your friend."
"ฉันจำได้ว่าตัวเองเคยคิดถึงจุดประสงค์ของมิตรภาพระหว่างเรา เพื่อทำใจยอมรับทุกสิ่งและทุกอย่าง เพื่ออยู่เคียงข้าง\nกันและกัน"

# "Did I fail as a friend, thinking it could be a stepping stone for something else?"
"ฉันล้มเหลวในฐานะเพื่อนหรือเปล่าที่คิดว่าเพื่อนคือขั้นหนึ่งที่จะพาไปสู่สิ่งอื่น"

# "Maybe because of those thoughts, I didn't manage to put up with things, to keep it together."
"อาจจะเพราะความคิดพวกนั้น ฉันถึงได้ทำใจยอมรับอะไรไม่ได้ จนกระทั่งรักษามิตรภาพเอาไว้ไม่ได้"

# "As outrageous as Rin is and was, I shouldn't have let myself get caught into that, especially when I started feeling the way I did towards her."
"รินอาจจะเป็นคนหลุดโลกอย่างนั้นอย่างนี้ก็จริง ฉันก็ไม่น่าหลวมตัวปล่อยให้ตัวเองโมโหไปอย่างนั้นเลย แล้วยิ่งฉันมี\nความรู้สึกอย่างนี้ต่อเธออีก"

# "So, did I fail?"
"สรุป ฉันล้มเหลวแล้วเหรอ"

# "That's what her eyes seem to ask."
"นั่นคือสิ่งที่สายตาเธอดูอยากถาม"

"…"

# hi "I'm sorry, Rin."
hi "ฉันขอโทษนะริน"

# hi "I might not be able to be your friend."
hi "ฉันคงเป็นเพื่อนเธอไม่ได้"

# hi "I don't think I could ever be a good friend to you."
hi "ฉันคิดว่าฉันคงเป็นเพื่อนที่ดีต่อเธอไม่ได้"

# "I say these things because they are true, not because one of us would like to hear them."
"ฉันพูดเช่นนั้นเพราะสิ่งนั้นคือความจริง ไม่ใช่พูดเพราะใครคนใดคนหนึ่งอยากได้ยินสิ่งนั้น"

# "But they are something that must be said."
"แต่สิ่งนั้นเป็นสิ่งที่ต้องพูด"

# "The finality of my words creates a shaking silence, for what could either of us add to that?"
"คำพูดของฉันที่ฟังดูเป็นการปิดท้ายนั้นทำให้เกิดความเงียบที่แทบทำตัวสั่น เพราะคงไม่มีอะไรให้พูดต่อได้อีก"

"…"

show rin negative_confused_close
with charachange

# rin "Why? Why does all this happen?"
rin "ทำไม ทำไมถึงเป็นอย่างนี้"

show rin negative_sad_close
with charachange

# rin "People are doing things I don't ask for and don't want and everyone keeps getting angry at me, I have no idea what is going on any more and can't stop feeling like I want to run away from everything…"
rin "ทุกคนทำอะไรที่ฉันไม่ได้ขอและไม่ได้ต้องการ แล้วทุกคนก็โกรธฉัน ฉันไม่รู้เลยว่าเกิดอะไรขึ้น ฉันอดไม่ได้ที่จะอยากหนี\nไปจากทุกอย่าง…"

show rin basic_lucid_close
with charachange

# "She shuts her eyes tight and breathes out deeply, calmly."
"เธอหลับตาปี๋แล้วหายใจออกยืดยาวอย่างใจเย็น"

show rin basic_upset_close
with charachange

# "When the eyelids open, all I can see is dark green desperation."
"เมื่อเปลือกตาเปิด ฉันเห็นแต่เพียงสีเขียวเข้มแห่งความสิ้นหวัง"

# rin "{b}I have no idea what's wrong with me!{/b}"
rin "ฉันไม่รู้ว่าฉันเป็นอะไร!!!"

# "Her frenetic outburst stupefies me for a moment, and for a heartbeat we just gaze into each other's face."
"อารมณ์ของเธอที่ระเบิดออกมาอย่างบ้าคลั่งทำให้ฉันตัวแข็งทื่อไปครู่หนึ่ง พวกเราจ้องตากันอยู่ชั่วหัวใจเต้น"

# "Seeing her confused eyes desperately looking for answers from mine only makes me sad, because I know I have none."
"ยิ่งได้เห็นสายตาอันสับสนของเธอที่พยายามค้นหาคำตอบจากในสายตาฉันแล้วฉันยิ่งเศร้า เพราะฉันรู้ดีว่าฉันไม่มี\nคำตอบเลย"

# hi "I don't know either."
hi "ฉันก็ไม่รู้เหมือนกัน"

# hi "But you know, you yourself said that things are not right nor wrong."
hi "แต่ก็เนี่ย เธอพูดเองไม่ใช่เหรอว่าอะไร ๆ ไม่ได้มีถูกหรือผิด"

# hi "They just are."
hi "มันก็เป็นของมันอย่างนั้น"

# hi "You either accept them, work to change them or give up."
hi "จะยอมรับ จะลงแรงเปลี่ยนแปลง จะยอมแพ้ ก็สุดแท้แต่จะเลือก"

# hi "It's not that I hate you, or that teacher Nomiya does."
hi "ไม่ใช่ว่าฉันหรือโนมิยะเกลียดเธอหรอก"

# hi "I just… think that I am the kind of person who gives up when he feels he can't go on."
hi "ฉันแค่… คิดว่าตัวเองเป็นพวกที่จะยอมแพ้ถ้ารู้สึกว่าไปต่อไม่ไหวแล้ว"

# hi "And even if you hate it, this… this is… how things are."
hi "และต่อให้จะไม่อยาก มัน… มันก็… เป็นอย่างนี้แหละ"

# "I'm saying pretty cruel things but I can't stop myself, the words keep rolling off my tongue with slow, hard certainty."
"สิ่งที่ฉันพูดนั้นค่อนข้างโหดร้าย แต่ฉันหยุดตัวเองไว้ไม่อยู่ คำพูดเหล่านั้นไหลผ่านลิ้นฉันออกมาอย่างช้า ๆ และมั่นคง"

show rin basic_surprised_close
with charachange

# "I can see them hitting Rin almost like physical blows."
"ฉันเห็นคำพูดเหล่านั้นเข้ากระทบกระเทือนกับรินเหมือนเธอถูกต่อยจริง ๆ"

# "As the wetness gathers into the corners of her eyes, they are still wide with the shock of rejection."
"น้ำตาเธอรื้นอยู่ขอบตาที่เบิกโพลงด้วยอารมณ์ที่ไม่อยากยอมรับ"

show rin basic_crying_close
with charachange

# "As the tears start rolling down her pale cheeks, she does nothing to stop them."
"เธอปล่อยให้น้ำตาไหลอาบแก้มสีซีดของเธอ"

# "As they fall down on the floor one by one, she stands still, staring at me with a gaze full of hollow disbelief."
"เธอยืนอยู่นิ่ง ๆ ปล่อยให้น้ำตาหยดลงพื้นทีละหยด ทีละหยด สายตาเธอที่จ้องฉันนั้นเปล่ากลวงด้วยอารมณ์ที่ไม่อยากเชื่อ"

rin "…"

# "But reality catches up."
"แต่แล้วความเป็นจริงก็เข้าประดัง"

show rin negative_crying_superclose
with vpunch

# "Rin slumps forward as if she was deflating, and buries her face as deep in my shirt as she can."
"รินเอนตัวล้มลงใส่ฉันราวลูกโป่งที่หมดลม เธอซุกหน้าเข้ากับหน้าอกฉันแรง ๆ"

# "Rin is heavy and featherlight when I support her weight."
"เมื่อต้องประคองตัวรินแล้วตัวเธอนั้นหนักแต่ก็เบาดุจขนนก"

# "She doesn't really sob or bawl, just leans against me, letting her tears burn through my shirt into the skin underneath."
"เธอไม่ได้สะอึกสะอื้นหรือร้องไห้โฮ เธอแค่ฟุบอยู่กับฉันแล้วปล่อยให้น้ำตาซึมผ่านเสื้อเข้ามาถูกกับผิวที่อยู่ใต้สาบเสื้อนั้น"

# "And I let her, bringing my hand around her shoulders in a clumsy hug that does no good to comfort her."
"และฉันก็ปล่อยให้เธอพิงอยู่อย่างนั้น ฉันโอบแขนเข้ากับไหล่เธอด้วยท่าทีเก้ ๆ กัง ๆ เป็นกอดที่ปลอบเธอได้ไม่ดี\nเอาเสียเลย"

# "I can feel Rin's vertebrae against my fingertips, like hard and jagged reminders of how messed up things are."
"ปลายนิ้วฉันสัมผัสได้ถึงกระดูกสันหลังของริน ทั้งแข็งทื่อและสลับซับซ้อน ราวกับเป็นสิ่งเตือนถึงความวุ่นวายของ\nอะไร ๆ ในตอนนี้"

# "Her slim shoulder quivering against my palm is a pitiable sight, and the hopelessness of being part of the cause for Rin's sadness keeps shredding my heart."
"ไหล่บางของเธอที่สั่นอยู่ในอุ้งมือฉันนั้นช่างน่าเวทนา ความสิ้นหวังที่อยู่ในท่าทีก็เป็นส่วนหนึ่งที่ทำให้รู้สึกเช่นนั้น\nเพราะความเศร้าของรินนั้นทำจิตใจฉันแหลกสลาย"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

# n "\n\n\n\nTo make a girl cry is the most despicable thing to do."
n "\n\n\n\nการทำให้ผู้หญิงร้องไห้นั้นเป็นสิ่งที่ต่ำช้าที่สุด"

# n "\nEven Rin. Especially Rin."
n "\nแม้แต่ริน โดยเฉพาะริน"

# n "\nBehind that veil of aloofness, Rin is just a human being too."
n "\nเบื้องหลังฉากความเหินห่างนั้น รินก็เป็นมนุษย์คนหนึ่ง"

# n "Just as confused, scared and lost as any of us is."
n "สับสน หวาดกลัว หลงทาง ไม่ต่างไปจากพวกเรา"

# n "Most of the time it seems that there is no rhyme or reason for what Rin does and says, but for once, I think I really understand how she feels."
n "หลายครั้งที่สิ่งที่เธอทำและพูดนั้นดูจะไม่มีความเข้ากันหรือเหตุผลอะไร แต่อย่างน้อยครั้งนี้ฉันก็คิดว่าฉันเข้าใจว่าเธอ\nรู้สึกอย่างไร"

# n "\n\nBut no words can express it, and no words can make it better."
n "\n\nแต่ไม่อาจมีคำพูดใดมาอธิบาย และไม่อาจมีคำพูดใดมารักษาได้"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear

show bg school_nomiya:
    "bg school_nomiya_ss" with Dissolve(8.0)
show rin negative_crying_superclose:
    "rin negative_crying_superclose_ss" with Dissolve(8.0, alpha=True)
with None

stop music fadeout 5.0

# n "\n\n\n\n\nSo wordless we stay, quietly waiting for her tears to run out."
n "\n\n\n\n\nเราจึงอยู่กับเงียบ ๆ รอให้น้ำตาเธอแห้งหาย"

# n "Time passes agonizingly slowly, even the lazy specks of dust floating in the air seem to pause into a standstill."
n "เวลาผ่านไปช้าเหลือทน แม้แต่เศษฝุ่นหนึ่งที่ลอยเอื่อยเฉื่อยอยู่ในอากาศก็ดูจะหยุดค้างไปดื้อ ๆ"

# n "The obligatory wall clock is ticking distractingly from above the door."
n "เข็มที่อยู่ในนาฬิกาที่มีทุกห้องส่งเสียงรบกวนขณะเดินอยู่เหนือประตู"

# n "I decide against counting the seconds, because it would make them feel longer."
n "ฉันตัดใจไม่นับวินาที เพราะยิ่งจะทำให้รู้สึกว่าเวลายิ่งนาน"

n "\n\n…"

play music music_serene fadein 9.0

nvl hide dissolve
nvl clear

show rin basic_crying_superclose_ss
with charachange

window show

# "Eventually Rin stirs a little and still smothering herself against my chest, mutters into my shirt."
"จนในที่สุดรินก็ดิ้นยุกยิกโดยที่ยังฝังหน้าตัวเองอยู่กับหน้าอกฉันอยู่ เธอพึมพำอยู่กับเสื้อฉัน"

# rin "Let me be here for a while."
rin "ขอฉันอยู่ตรงนี้สักพัก"

show rin negative_crying_superclose_ss
with charachange

# rin "Please, Hisao."
rin "ขอร้องละ ฮิซาโอะ"

# rin "Just give me a little while."
rin "ขอเวลาฉันสักหน่อย"

# "A soothing deluge spreads into my consciousness, the knowledge that while being here for Rin is all I can do for her, that's all she wants right now, even after all we've gone through."
"ความเบาใจถาโถมเข้าในสำนึก แม้สิ่งที่ฉันทำได้มีเพียงการอยู่เคียงข้างเธอตรงนี้ แต่นั่นก็เป็นสิ่งที่เธอต้องการในตอนนี้\nแม้เราจะผ่านอะไรมากมายมาก่อนหน้าแล้วก็ตาม"

# hi "Sure."
hi "ได้สิ"

# "So she stays there."
"เธอจึงอยู่อย่างนั้น"

# "But I still can't bring myself to draw her closer so I could embrace her properly."
"แต่ฉันไม่กล้าที่จะขยับตัวเธอให้เข้ามาใกล้ ๆ ให้กอดได้ถนัด ๆ"

# "It's because doing it would just make me so sad that I don't know if I could bear it."
"เพราะหากทำอย่างนั้นแล้วจะยิ่งทำให้ฉันต้องเศร้าอีก ซึ่งไม่รู้ว่าฉันจะทนไหวหรือเปล่า"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

# n "\n\nThe realization that we might never really be able to become what we want to be for the other crystallizes into my mind as a diamond-hard enlightenment."
n "\n\nฉันตกผลึกอย่างหนึ่งได้ ว่าพวกเรานั้นไม่มีวันที่จะเป็นอย่างที่อยากเป็นเพื่ออีกฝ่าย ผลึกที่ได้มานั้นแข็งดุจเพชร"

# n "A pang surges through my heart like an electric shock."
n "ความเจ็บนั้นเสียดแทงหัวใจราวไฟฟ้าช็อต"

# n "It's painful."
n "เจ็บ"

# n "This clarity… hurts."
n "ชัดแจ้ง… จนเจ็บ"

# n "What can we be for each other? What meaning is there for us to desperately cling to each other even though it seems so futile?"
n "เราจะเป็นอะไรเพื่ออีกฝ่ายได้? เราจะกระเสือกกระสนยึดติดกันและกันไปทำไม ทั้งที่ดูแล้วก็ป่วยการจะทำ?"

# n "What should I say to Rin? How can I make her feel better?"
n "ฉันจะพูดอะไรกับรินดี ฉันจะทำให้เธอรู้สึกดีขึ้นได้ยังไง"

# n "I do not know any of those things, and I fear knowing them would only hurt more."
n "ฉันไม่อยากรู้อะไรเหล่านั้น และฉันกลัวว่ายิ่งรู้แล้วจะยิ่งเจ็บ"

# n "Forcefully, I push all of that out of my mind because I don't want to be thinking of hurtful truths."
n "ฉันฝืนใจกีดเรื่องนั้นออกจากหัวไป ฉันไม่อยากคิดถึงความเป็นจริงอันเจ็บปวด"

# n "My thoughts calm down soon enough, the sadness disperses until all that is left is me and Rin and the tender feeling of her warmth and softness against my chest."
n "จนฉันสงบใจลงได้ ความเศร้าจางลงจนสิ่งที่เหลืออยู่มีเพียงฉันและรินและความอบอุ่นอันอ่อนโยนและความนุ่มนวลที่แนบ\nอยู่กับหน้าอกฉัน"

nvl clear

# n "\n\nWhen did I fall in love with her?"
n "\n\nฉันตกหลุมรักเธอไปตั้งแต่ตอนไหน"

# n "I can't remember, but I'm certain it was way before the warm touch of her lips on my own, on that orange-colored afternoon when she was sick with cold and I went to see her because of unclear reasons."
n "ฉันจำไม่ได้ แต่ฉันมั่นใจว่าเป็นตอนก่อนที่ความอบอุ่นจากริมฝีปากเธอจะแตะเข้ากับริมฝีปากฉันในบ่ายสีส้มวันนั้นที่เธอ\nเป็นหวัดที่ฉันไปเยี่ยมเธอด้วยเหตุผลที่ไม่แน่ชัด"

# n "Her carefree attitude, the air of otherness around her, all the things that make Rin herself… those things captured me with irresistible force."
n "ท่าทีไม่สนโลกของเธอ บรรยากาศอันแตกต่างของเธอ ทุกอย่างที่เป็นริน… เหล่านั้นดึงดูดฉันด้วยแรงที่ไม่อาจ\nต้านทาน"

# n "The way she could take in anything and everything giving it only the value she herself placed, weighing all things fairly and without prejudice, seeing the world as she wanted."
n "การที่เธอยอมรับทุกสิ่งและทุกอย่างโดยให้ค่าเท่าที่เธอกำหนดไว้ การที่เธอชั่งน้ำหนักทุก ๆ อย่างอย่างยุติธรรมโดยไร้ซึ่ง\nอคติ การที่เธอมองโลกอย่างที่เธออยากมอง"

# n "This is something I could never do, and Rin was probably more of a muse to me than anything ever was to her."
n "เป็นสิ่งที่ฉันไม่มีวันจะทำได้ และรินคงทำให้ฉันมีแรงบันดาลใจได้เยอะกว่าการที่ฉันเป็นแรงบันดาลใจให้เธอเสียอีก"

# n "She seemed so free to me, truly a free spirit. While I, constantly worrying about everything, seemed so inhibited that it was almost embarrassing."
n "เธอดูเป็นอิสระมาก เป็นคนที่เป็นอิสระโดยแท้จริง ในขณะที่ฉันซึ่งเอาแต่เป็นกังวลไปหมดนั้นดูจะไร้อิสระอย่างน่าอาย"

# n "Maybe that's why I latched so tightly on to Rin, trying to get inside her world that was so different from my own bleak life."
n "คงเพราะอย่างนั้นฉันถึงได้ติดรินแจ เพราะพยายามจะเข้าไปในโลกของเธอที่ช่างแตกต่างจากชีวิตของฉันอันร้างไร้"

nvl clear

# n "\n\nBefore I noticed it, that irresistible force had pulled me dangerously close to her, but it turned out to be way too alien for me."
n "\n\nกว่าจะรู้สึกตัว แรงที่ฉันต้านทานไม่อยู่ก็ดึงให้ฉันเข้าใกล้เธอจนอยู่ในระยะอันตราย แต่แล้วฉันก็เห็นว่าโลกนั้นแปลกต่าง\nเกินไปสำหรับฉัน"

# n "And I had forgotten Newton, of all things."
n "แล้วลืมอะไรไม่ลืม ดันลืมกฎของนิวตันไปเสียได้"

# n "The gravitational force is inversely proportional to the square of the distance between the objects…"
n "แรงดึงดูดระหว่างมวลเป็นสัดส่วนผกผันกับค่ากำลังสองของระยะห่างระหว่างสองวัตถุ…"

# n "So if two people feel something for each other…"
n "ดังนั้น ถ้าสองคนมีความรู้สึกต่อกัน…"

# n "Heh."
n "ฮะ ๆ"

# n "Even though feelings are not governed by the constants of the universe, I can't help thinking that for some time now I've been a satellite to Rin's brightly shining planet."
n "ถึงความรู้สึกจะไม่ได้มีกฎของจักรวาลคอยควบคุม แต่ฉันก็อดคิดไม่ได้ว่าช่วงนี้ฉันก็เป็นดาวเทียมที่โคจรรอบดาวเคราห์\nของรินที่สุกสว่าง"

# n "\nPlanet Rin."
n "\nดาวเคราห์ริน"

# n "\nThe thought makes me almost laugh, she really does seem to be from another planet at times, minus green skin and possibly some tentacles."
n "\nคิดแล้วก็แทบหลุดขำ บางทีเธอก็เหมือนมาจากต่างดาวจริง ๆ ไม่นับเรื่องผิวสีเขียว ๆ แล้วก็หนวดหยึย ๆ น่ะนะ"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

show rin negative_sad_close_ss
with charadistant

window show

# "Perhaps because of my stifled laughter, Rin pulls away and I let her go, feeling the cold when her warmth goes away, and slight embarrassment for letting my thoughts run wild like that."
"ไม่แน่ใจว่าเพราะฉันกลั้นขำหรืออะไรรินถึงได้ถอนตัวออก ฉันก็ปล่อยเธอไป พอไม่มีความอบอุ่นของเธอแล้วความเย็นก็\nเข้ามาแทนที่ แอบอายแฮะที่คิดอะไรฟุ้งซ่านไปขนาดนั้น"

# "I credit that as Rin being a bad influence on me, while being glad at the same time that she can't read thoughts for real."
"เอาเป็นว่าเพราะรินนั่นแหละที่มีผลกับใจฉันอย่างนั้น แต่ก็โล่งไปที่รินอ่านใจไม่ได้จริง ๆ"

# "Rin's bitter tears have dried up, and she looks a little more like herself again."
"น้ำตาอันขื่นขมของรินเหือดหายไป ท่าทีเธอดูกลับมาเป็นตัวเองขึ้นมาบ้างแล้ว"

show rin basic_sad_close_ss
with charachange

# "The lost look in her eyes is still there though. Her gaze wanders around restlessly before stopping at me."
"แต่สายตาสับสนเธอยังไม่ไปไหน ตาเธอหลุกหลิกมองไปรอบ ๆ ห้องก่อนจะมาหยุดอยู่ที่ฉัน"

# rin "What happened just now?"
rin "เมื่อกี้เกิดอะไรขึ้น"

# rin "Can you tell me?"
rin "บอกหน่อยได้มั้ย"

# hi "What? What do you mean?"
hi "ฮะ? หมายความว่ายังไง"

show rin basic_upset_close_ss
with charachange

# rin "I cried."
rin "ฉันร้องไห้"

# "She says that hesitantly, as if not believing it herself."
"น้ำเสียงเธอฟังดูลังเลราวกับว่าไม่อยากจะเชื่อ"

# hi "Yes…"
hi "ใช่…"

"…"

# "She keeps staring at me, as if pleading guidance so that she wouldn't have to feel so lost."
"เธอเอาแต่จ้องฉันคล้ายอ้อนวอนให้ฉันนำทาง เธอจะได้ไม่ต้องหลงทางอยู่อย่างนี้"

"…"

show rin basic_sad_close_ss
with charachange

# rin "Why?"
rin "ทำไม"

# hi "You were sad."
hi "เธอเศร้า"

# hi "Is that what you want me to say? But isn't that obvious?"
hi "นั่นน่ะเหรอที่เธออยากให้ฉันพูด แต่ก็น่าจะชัดแล้วนี่"

show rin negative_confused_close_ss
with charachange

# rin "I don't know. It feels weird to cry."
rin "ไม่รู้สิ ร้องไห้แล้วรู้สึกแปลก"

# hi "What? I don't believe it. I mean, everyone does that. It's nor—"
hi "ฮะ? ไม่อยากจะเชื่อเลย คือ ทุกคนก็ร้องไห้ มันเป็นเรื่องปก—"

# "I bite my tongue before I finish my argument about normality."
"ฉันกัดลิ้นตัวเองตัดคำแย้งเรื่องความปกตินั้นทิ้ง"

# "Norms do not apply to the person I'm talking to."
"คนที่ฉันคุยด้วยเอาความปกติมาคุยด้วยไม่ได้"

show rin negative_worried_close_ss
with charachange

# rin "It always felt so wrong, different from what is in me. Like I couldn't really tell what I felt."
rin "รู้สึกผิดแผกแตกต่างไปจากสิ่งในตัวฉัน เหมือนฉันไม่ค่อยรู้เท่าไหร่ว่าฉันรู้สึกยังไง"

# rin "So I started thinking that maybe I don't know what I'm feeling. Maybe it's me who is wrong—"
rin "ฉันเลยเริ่มคิดว่าหรือฉันจะไม่รู้ว่าฉันรู้สึกยังไง หรือเป็นฉันที่ผิดปกติ—"

# rin "I thought those kinds of things."
rin "ฉันคิดอะไรอย่างนั้น"

show rin negative_sad_close_ss
with charachange

# rin "I thought… that painting was enough because it felt that I did at least that right."
rin "ฉันคิด… ว่าวาดก็พอแล้ว เพราะรู้สึกว่าอย่างน้อยฉันก็วาดได้ถูกต้อง"

# rin "That all that is inside me could become a picture if I tried really hard. And it could."
rin "ว่าถ้าฉันพยายามอย่างหนักแล้วทุกอย่างในตัวฉันจะออกมาเป็นรูปได้ แล้วก็เป็นได้"

# rin "But it doesn't feel like it's enough any more. Because if nobody else can see that, I will still be alone."
rin "แต่รู้สึกว่าไม่พออีกต่อไปแล้ว เพราะถ้าไม่มีใครเห็น ฉันก็จะยังโดดเดีี่ยว"

show rin basic_absent_close_ss
with charachange

# rin "Was it wrong to try? Everyone got really angry at me for that."
rin "ผิดเหรอที่จะลอง? ทุกคนโกรธที่ฉันลอง"

stop music fadeout 6.0

# "I've rarely heard Rin say this much at once before."
"ฉันแทบไม่เคยเห็นรินพูดเยอะขนาดนี้"

# "Once she finishes, she simply shuts up, looking so neutral that it's hard to believe she just said what she did."
"พอเธอพูดจบแล้วเธอก็เงียบปากไป ดูไม่เหมือนกับว่าเธอเพิ่งพูดอะไรอย่างเมื่อกี้ออกมา"

# "I don't know what to think."
"ฉันไม่รู้ว่าจะคิดยังไง"

"…"

# "Rin was desperate for someone to look at her paintings, and somehow see right through them into her soul, to understand her feelings…"
"รินอยากให้คนได้เห็นภาพวาดของเธอมาก ๆ ให้เห็นไปถึงจิตวิญญาณเธอจนเข้าใจความรู้สึกเธอ…"

# "Because… she felt she could not express them in any other way?"
"เพราะ… เธอรู้สึกว่าจะแสดงออกด้วยวิธีอื่นไม่ได้แล้ว?"

# "How can one say whether that is right or wrong?"
"ใครจะมาชี้นิ้วได้ว่าถูกหรือผิด?"

# "Could it be that all this time she's been trying to reach out to me like I've tried to reach out to her?"
"หรือจริง ๆ แล้วที่ผ่านมาเธอก็พยายามเข้าหาฉันอย่างที่ฉันพยายามเข้าหาเธอ?"

"…"

# "I sit down on a desk to think, and to rest my legs that kept us both standing for a long while."
"ฉันนั่งลงกับโต๊ะแล้วคิดพลางพักขาที่ค้ำให้พวกเราสองคนยืนอยู่พักใหญ่"

play music music_innocence fadein 12.0

# hi "You know, when I read a good book or look at a starry sky or whatever, sometimes I too feel something… profound, like a… shoot, I don't know how to describe it."
hi "รู้มั้ย เวลาที่ฉันได้อ่านหนังสือดี ๆ หรือได้มองฟ้าที่มีดาวหรืออะไรก็ช่าง บางครั้งฉันเองก็รู้สึกอะไรที่… ลึกล้ำเหมือนกัน\nเหมือน… โอย ไม่รู้จะอธิบายยังไงดี"

# hi "But the instant I try to put it into words I feel that I lose something, it doesn't feel as real, as true as it did inside my head."
hi "แต่ทันทีที่ฉันจะเอาออกมาเป็นคำพูด ฉันก็รู้สึกเหมือนเสียอะไรไป รู้สึกเหมือนมันไม่ได้จริงแท้เท่าตอนที่อยู่ในหัว"

# hi "It feels a bit phony. Damn, even what I just said felt phony."
hi "รู้สึกปลอม ๆ ให้ตาย ขนาดที่พูดเมื่อกี้ยังรู้สึกปลอมเลย"

# "I offer a smile that is meant to be between funny and self-deprecating, but Rin doesn't react."
"ฉันยิ้มกึ่ง ๆ ขำกึ่ง ๆ ล้อเลียนตัวเอง แต่รินก็ไม่ตอบสนองอะไร"

# hi "Anyway…"
hi "แต่นั่นแหละ…"

# hi "It might be that nobody can ever express their true feelings so that others understand."
hi "คนเราอาจจะแสดงความรู้สึกตัวเองออกมาให้คนอื่นเข้าใจไม่ได้หรอก"

# hi "Reality has no chance of living up to what someone has inside their head."
hi "ความเป็นจริงไม่มีวันที่จะเทียบได้กับสิ่งที่อยู่ในหัวคนคนหนึ่ง"

# hi "Nothing can match that. Not even your paintings, except maybe for you."
hi "ไม่มีอะไรที่จะเทียบได้เลย ไม่แม้แต่ภาพวาดของเธอ หรือบางทีเธออาจจะมองว่าเทียบได้อยู่"

# hi "But I suppose you can't keep everything inside, you'd explode for real then."
hi "แต่ก็คงเก็บทุกอย่างเอาไว้ข้างในไม่ได้ละนะ ไม่งั้นคงได้ระเบิดจริง ๆ"

# hi "What I'm trying to say is… I don't think it's wrong to express your feelings, even if you use painting as your conduit."
hi "ที่ฉันจะบอกก็คือ… ฉันว่าการที่แสดงความรู้สึกออกมาน่ะไม่ได้ผิดหรอก ต่อให้จะใช้ภาพวาดเป็นสื่อกลางก็เถอะ"

# hi "You just can't expect people to understand you any better than they would if you did it any other way."
hi "ไม่มีวิธีใดวิธีหนึ่งที่จะมาคาดหวังได้ว่าใช้แสดงออกไปแล้วคนจะเข้าใจได้มากกว่าวิธีอื่น ๆ"

# hi "In fact, you can't expect people to understand you at all."
hi "อันที่จริง จะมาคาดหวังให้คนเข้าใจตัวเองไม่ได้หรอก"

# hi "It's because everything is so subjective. You see the world the way you do, but it's different from everyone else."
hi "เพราะทุกอย่างมันเป็นปัจเจกมาก ๆ เธอมองโลกในแบบของเธอ แต่ก็ต่างจากแบบที่คนอื่น ๆ มองเหมือนกัน"

show rin basic_sad_close_ss
with charachange

# rin "But isn't that terrible?"
rin "ถ้างั้นก็แย่สิ"

# hi "I guess it is, in a way."
hi "ในแง่หนึ่งก็คงแย่นั่นแหละ"

"…"

show rin relaxed_doubt_close_ss
with charachange

# "She frowns, looking probably as stricken as she can. Which is not much, but it's enough for me to understand that Rin is not particularly happy."
"เธอขมวดคิ้วให้ดูเคร่งเครียดที่สุดเท่าที่จะทำได้ ซึ่งก็ไม่ได้ดูเคร่งเครียดเท่าไหร่ แต่ก็มากพอที่จะให้ฉันเข้าใจได้ว่า\nเธอนั้นไม่ได้อารมณ์ดีเท่าไหร่"

# rin "I think it might make me sad after all."
rin "ฉันคิดว่าฉันอาจจะหดหู่กับคำพูดนั้นจริง ๆ"

# hi "Yeah. I know."
hi "อืม รู้"

# hi "I wish I could do something to help it."
hi "ฉันอยากจะช่วยอยู่นะ"

# "I don't think I sound bitter, even though I am, a little."
"ฉันว่าน้ำเสียงฉันไม่ได้ฟังดูขมขื่น ถึงจะขมขื่นอยู่นิด ๆ ก็เถอะ"

# "This is my problem. I cannot be what Rin wants for her. And for the same reason, she can't do the same for me either."
"นี่แหละคือปัญหาของฉัน ฉันเป็นอะไรอย่างที่รินต้องการไม่ได้ และด้วยเหตุผลเดียวกันนั้น เธอก็ทำอย่างนั้นเพื่อฉัน\nไม่ได้เช่นกัน"

"…"

show rin negative_worried_close_ss
with charachange

# "She makes a difficult face, carefully trying to pick the words she wants to say."
"เธอทำสีหน้าปั้นยากพลางค่อย ๆ คิดหาคำที่เธอต้องการจะพูด"

# "So Rin has times when it's hard to say anything, too."
"แม้แต่รินก็ยังมีเวลาที่ไม่รู้จะพูดอะไรเหมือนกันสินะ"

show rin basic_sad_close_ss
with charachange

# rin "It can't be helped, I think."
rin "ก็ช่วยไม่ได้ ฉันคิดว่านะ"

show rin basic_absent_close_ss
with charachange

# rin "…but… if you say that…"
rin "…แต่… ถ้านายพูดอย่างนั้น…"

show rin basic_awayabsent_close_ss
with charachange

# rin "It makes me feel a little better."
rin "ฉันก็รู้สึกดีขึ้นมานิดหน่อย"

"…"

# "It's funny how some seemingly irrelevant things are the most significant ones at times like this."
"ตลกดีที่อะไรที่ดูไม่เกี่ยวข้องดันมาสำคัญเอาเวลาเรื่องเป็นอย่างนี้"

# "Like how Rin's voice is very very small, barely audible when she says that."
"อย่างเช่นเสียงรินที่ค่อยมากแบบมาก ๆ จนแทบไม่ได้ยินที่พูด"

# "And how even her short bangs can cover her eyes when she looks downwards."
"และหน้าม้าเธอที่ยาวพอที่จะปรกตาเธอพอเธอก้มหัว"

show rin basic_blush_close_ss
with charachange

# "And how they can't cover the deep red color rising on her cheeks and all the way to the tips of her ears."
"และหน้าม้าเธอที่ยาวไม่พอที่จะปกปิดสีแดงก่ำที่แผ่ทั่วบนแก้มเธอยาวไปจนถึงปลายใบหู"

# "They turn into a very interesting shade of red."
"เป็นโทนสีแดงที่น่าสนใจดี"

# "A deafening silence follows."
"ความเงียบที่ชวนให้หูอื้อตามมา"

# "It's very awkward, as if I saw something that wasn't meant to be seen, even if it wasn't on purpose."
"กระอักกระอ่วนเอามาก ๆ ราวกับว่าฉันได้ไปเห็นอะไรที่ฉันไม่ควรเห็นเข้า ถึงจะไม่ได้ตั้งใจก็เถอะ"

# "I don't know what to say to that, but I keep feeling like I should know."
"ฉันไม่รู้จะตอบยังไง แต่ฉันก็รู้สึกว่าฉันน่าจะรู้"

# "She doesn't either."
"เธอก็ไม่พูดอะไรต่อ"

# "Still, it feels like there is no momentum to lose even if we keep silent."
"แต่ก็ไม่ได้รู้สึกว่าเงียบไปแล้วจะเสียสมดุลอะไร"

# "Like we have some weird, wordless connection that would hold even so."
"เหมือนกับว่าเรามีสายเชื่อมต่อไร้คำพูดแปลก ๆ ที่ต่อให้เงียบก็ยังเชื่อมถึงกัน"

show rin relaxed_nonchalant_close_ss
with charachange

# "Rin keeps shifting her weight from one foot to the other restlessly, looking everywhere around the room except at me."
"รินโยกตัวยืนสลับเท้าไปมามองไปรอบ ๆ ห้องยกเว้นที่ฉัน"

# "She is the one who finally breaks the spell."
"จนในที่สุดเธอก็เป็นคนทำลายพันธะเงียบนี้ลง"

show rin basic_deadpan_close_ss
with charachange

# rin "Can we go? I don't want to stay here."
rin "ไปกันได้หรือยัง ฉันไม่อยากอยู่ที่นี่"

# hi "Oh, yeah, of course. Where?"
hi "อ้อ อืม ได้สิ ไปไหน"

# "My reply is covering my nervousness as badly as her question is covering hers."
"คำตอบของฉันปกปิดความลนลานได้แย่พอ ๆ กันกับการที่คำถามของรินปกปิดความลนลานของเธอ"

show rin relaxed_sleepy_close_ss
with charachange

# rin "You can go wherever you like. I want to sleep. I haven't really slept for a few weeks."
rin "อยากไปที่ไหนก็ตามใจนาย ฉันอยากหลับ ฉันไม่ได้หลับมาสองสามสัปดาห์แล้ว"

show rin basic_lucid_close_ss
with charachange

# rin "It feels like there is a flock of light blue butterflies inside my head. It makes it hard to think properly."
rin "รู้สึกเหมือนในหัวมีกลุ่มผีเสื้อสีฟ้าอยู่ ฉันคิดอะไรไม่ค่อยออก"

show rin basic_deadpannormal_close_ss
with charachange

# rin "The kind that you think is too blue to really exist, like Emi's panties this morning."
rin "เป็นผีเสื้อแบบที่เป็นสีฟ้าจนดูไม่น่ามีจริง เหมือนกางเกงในเอมิเมื่อเช้านี้"

show rin negative_spaciness_close_ss
with Dissolve(0.1)

show rin basic_absent_close_ss
with Dissolve(0.1)

show rin negative_spaciness_close_ss
with Dissolve(0.05)

show rin basic_absent_close_ss
with Dissolve(0.05)

show rin negative_spaciness_close_ss
with Dissolve(0.05)

show rin basic_absent_close_ss
with Dissolve(0.05)

show rin negative_spaciness_close_ss
with Dissolve(0.1)

show rin basic_deadpannormal_close_ss
with Dissolve(0.2)

# "She shakes her head, and I almost expect a couple of ultramarine-colored Morphos to pop out of her ears."
"เธอสั่นหัวจนเหมือนกับว่าจะมีผีเสื้อสีฟ้า ๆ หลุดออกมาจากหูเธอสักสองตัวเลยจริง ๆ"

show rin basic_deadpanamused_close_ss
with charachange

# "A small smile tugs upwards the corners of her mouth."
"เธอหยักยิ้มขึ้นเล็กน้อย"

# rin "That reminds me. The blue, not the panties."
rin "จะว่าไปแล้ว เรื่องสีฟ้า ไม่ใช่เรื่องกางเกงในนะ"

show rin basic_deadpandelight_close_ss
with charachange

# rin "The word for a flock of butterflies is a swarm. I looked it up."
rin "คำสำหรับกลุ่มผีเสื้อเขาเรียกว่าฝูงผีเสื้อ ฉันไปหามาแล้ว"

# "That makes my eyebrow rise into a questioning arch."
"ได้ฟังแล้วฉันก็เลิกคิ้วขึ้นด้วยความสงสัย"

# hi "Why don't you use it then?"
hi "แล้วทำไมเธอไม่ใช้คำนั้นล่ะ"

show rin basic_absent_close_ss
with charachange

# rin "I like the other word better."
rin "ฉันชอบอีกคำมากกว่า"

# "Why look it up in the first place, then?"
"แล้วจะไปหามาทำไมแต่แรก"

# hi "Then you should use it, right?"
hi "งั้นเธอก็ต้องใช้คำนั้นนะ จริงมั้ย"

show rin basic_awayabsent_close_ss
with charachange

# "She nods and falls silent, her gaze escaping mine to the side, attracted by the dark orange sunlight refracting from the windows."
"เธอพยักหน้าเงียบไปก่อนจะเสตามองไปทางแสงอาทิตย์สีส้มแก่ที่หักเหผ่านหน้าต่าง"

# "We stay like that for a little while: me silently looking at her silently looking out of the window."
"พวกเราอยู่กันอย่างนั้นพักหนึ่ง ฉันยืนมองเธอที่มองออกไปนอกหน้าต่างเงียบ ๆ"

# hi "Hey… you all right now?"
hi "นี่… ไม่เป็นไรแล้วใช่มั้ย"

show rin basic_absent_close_ss
with charachange

# "She glances at me from the corner of her eye, looking wistful again. The sunlight's reflection doesn't betray any more of her inner feelings."
"เธอเหลือบมองด้วยหางตาดูเศร้าสร้อยอีกครั้ง แสงสะท้อนจากดวงอาทิตย์ไม่อาจทรยศความรู้สึกภายในตัวเธอได้"

# rin "I'll need to think about that."
rin "ฉันจะต้องไปคิดก่อน"

# "I want to continue this conversation, grasping at those straws that she finally revealed to even exist."
"ฉันอยากจะต่อบทสนทนานี้อีก ฉันควานหาคำพูดเปิดที่ในที่สุดเธอก็เผยให้เห็นว่ามีอยู่จริง ๆ"

show rin basic_awayabsent_close_ss
with charachange

# "But Rin is looking out of the window so absentmindedly that I know she won't be responsive in any way that would make sense."
"แต่รินก็มองไปนอกหน้าต่างเหม่อ ๆ ฉันรู้เลยว่าเธอคงไม่ตอบอะไรที่ฟังแล้วจะเข้าใจได้แน่นอน"

# "It's like some kind of defense mechanism of hers, to avoid being sensible."
"เหมือนเป็นกลไกการป้องกันตัวของเธอที่ใช้เพื่อเลี่ยงความเป็นเหตุเป็นผล"

# "Her mind is like a butterfly in itself, always fluttering somewhere away whenever it's stirred."
"ความคิดของเธอก็เป็นอย่างผีเสื้อที่จะกระพือปีกบินหนีไปสักที่หนึ่ง ๆ ทุกครั้งที่ถูกรบกวน"

# "Just when I thought I could see behind her veil, she jumps out of my reach again."
"ทั้งที่คิดว่าเห็นตัวเธอที่อยู่หลังม่านได้แล้วแท้ ๆ แต่เธอก็โดดหนีไปจากฉันเสียได้"

# "Maybe that's just how Rin is."
"รินก็คงเป็นอย่างนั้นแหละมั้ง"

# "Maybe that's something I should just accept to get some peace of mind."
"ฉันก็คงต้องยอมรับแหละมั้ง จะได้ไม่ต้องมาว้าวุ่นใจ"

# hi "Okay."
hi "โอเค"

# hi "I'll walk you back to the dorms then."
hi "งั้นฉันจะเดินไปส่งเธอที่หอนะ"

show rin basic_absent_close_ss
with charachange

# rin "Thanks."
rin "ขอบใจ"

show rin basic_lucid_close_ss
with charachange

# rin "Really."
rin "จริง ๆ"

stop music fadeout 12.0

scene bg school_hallway3
with locationchange

# "The empty hallways of the school devoid of its students feel very lonely."
"โถงทางเดินว่างเปล่าของโรงเรียนที่ปลอดนักเรียนนั้นช่างเงียบเหงา"

# "Less than one hour after the summer vacation began, the building seems to be deserted, and all that intrudes on the stillness of the hallways are our footsteps."
"แม้จะเพิ่งปิดเทอมได้หนึ่งชั่วโมง แต่ในตัวอาคารนั้นก็ไม่เหลือใครแล้ว สิ่งที่ดังก้องรบกวนความสงบภายในโถงทางเดินนี้\nคือเสียงก้าวเดินของพวกเรา"

# "The change is sudden, but it shows how the building is just an empty shell, dead without its students and teachers."
"แม้จะเป็นการเปลี่ยนแค่ชั่วระยะสั้น ๆ แต่ก็แสดงให้เห็นว่าหากไม่มีเหล่านักเรียนและคุณครูแล้วตัวอาคารนั้นก็เป็นเพียง\nเปลือกนอกที่ตายซาก"

# "It's as though the school has become a private world for only the two of us, a desolate place filled with silence and chalk dust."
"ราวกับว่าทั้งโรงเรียนได้กลายเป็นโลกส่วนตัวที่มีเพียงเราสองคน เป็นที่รกร้างที่มีเพียงความเงียบงันและผงชอล์ก"

scene bg school_staircase2_ss
show rin relaxed_sleepy_close_ss at twoleft
with locationchange

# rin "I think I have to change."
rin "ฉันคิดว่าฉันต้องเปลี่ยน"

# "She says it out of the blue while we walk down the staircase from the third floor, still managing to feel like she is mirroring what I was thinking just before."
"ระหว่างที่เดินลงบันไดจากชั้นสามมาเธอก็พูดขึ้นมาแบบไม่มีปี่มีขลุ่ย เธอพูดเหมือนสะท้อนสิ่งที่ฉันคิดเมื่อก่อนหน้านี้\nออกมาได้พอดี"

# hi "That's what people must do, sometimes."
hi "บางที คนเราก็ต้องเปลี่ยน"

window hide
nvl clear
nvl show dissolve

# n "\n\n\n\n\n\n\n\nThat's the last thing we say to each other that day, even though there would be so much to talk about."
n "\n\n\n\n\n\n\n\nและนั่นคือคือคำพูดสุดท้ายของพวกเราในวันนั้น ถึงแม้จะมีเรื่องให้คุยอีกมากมายก็ตาม"

# n "And even those words drown in the all-encompassing silence, disappearing into the stagnant air as if they were never said."
n "คำพูดเหล่านั้นถูกทับถมโดยความเงียบที่ครอบคลุมทุกสิ่ง และอันตรธานหายไปกับอากาศเอื่อยเฉื่อยราวไม่ได้ถูกเอ่ย\nออกมา"

nvl clear
nvl hide dissolve

$ suppress_window_before_timeskip = True

scene black
with dissolve



label th_R41:

play music music_dreamy fadein 2.0

scene bg school_dormhisao_rn
with charachange

$ renpy.music.set_volume(0.4, 0.0, channel="ambient")
play ambient sfx_rain fadein 1.0

# "The first day of summer vacation is a disappointment."
"วันแรกของการปิดเทอมฤดูร้อนนั้นช่างน่าผิดหวัง"

# "I woke up. Water came down from the leaden sky in Biblical proportions."
"ฉันตื่นมาพบกับฝนห่าใหญ่ที่ตกลงมาจากท้องฟ้าสีเงินราวจะตกให้ท่วมโลก"

# "I was optimistic at the time."
"ตอนนั้นฉันคิดบวกไป"

# "A quick summer shower, I thought. Torrents of rain for a few minutes, then it's gone."
"ว่าคงแค่ตกเป็นฝนไล่ช้าง ว่าตกสาดลงมาสักสองสามนาทีเดี๋ยวก็หยุด"

show rain normal behind bg
with None

# "No such luck."
"ไม่เลย"

$ renpy.music.set_volume(0.7, 1.0, channel="ambient")

hide bg
show bg misc_sky_rn as bg2 behind rain
show hisaowindow
with locationchange

# "Rainwater is relentlessly pouring down from the blue-gray sky outside, streaming down the glass of my window in small brooks and rivers and gathering together to form miniature ponds on the walkways."
"น้ำฝนที่ตกลงมาไม่หยุดหย่อนจากท้องฟ้าสีฟ้าเทาภายนอกรวมตัวกันไหลเป็นสายน้ำเล็กน้ำใหญ่อยู่บนหน้าต่าง\nห้องฉัน และยังสะสมเป็นแอ่งอยู่บนทางเท้า"

# "Just like it has done for the past two and a half hours."
"เป็นอย่างนั้นมาแล้วสองชั่วโมงครึ่ง"

$ renpy.music.set_volume(0.4, 1.0, channel="ambient")

scene bg school_dormhisao_rn
with charachange

# "So I've been half-assedly cleaning up in between half-assedly reading a book, packing my stuff on the side when I get bored of the first two."
"ฉันจึงเก็บกวาดห้องไปแบบลวก ๆ เป็นการพักระหว่างที่กำลังอ่านหนังสือไปแบบลวก ๆ ถ้าเบื่อจากสองอย่างนั้นแล้วฉัน\nก็หันมาเก็บข้าวของใส่กระเป๋า"

# "The weather drags my spirits pretty down too, making it harder to do anything properly."
"อากาศอย่างนี้ทำให้ฉันไม่ค่อยมีเรี่ยวแรงด้วย จะทำอะไรก็ไม่ค่อยอยากทำ"

play sound sfx_impact2

# "Something bumping quite loudly against my door rouses me from my apathy."
"เสียงเคาะดัง ๆ จากประตูปลุกฉันให้ตื่นจากความเหนื่อยหน่ายนี้"

# "I hope it's not Kenji and his crazy indoors bowling alley."
"หวังว่าคงไม่ใช่เคนจิมาชวนไปโบว์ลิงในร่มบ้า ๆ อะไรนั่นนะ"

"…"

# "I hear no more sounds from the corridor until I walk to the door and open it."
"ไม่มีเสียงใดอีกจนกระทั่งฉันเดินไปเปิดประตู"

play sound sfx_dooropen
$ renpy.music.set_volume(0.2, 1.0, channel="ambient")
stop music fadeout 2.0

scene bg school_dormhallway
show rin basic_absent
with locationchange

# "Rin."
"ริน"

# "I wish seeing her would evoke some more emotion in me, but for one, I'm too surprised that she came to see me and for two, she is soaking wet."
"ก็คาดหวังไว้อยู่หรอกว่าถ้าได้เจอหน้าเธอแล้วฉันจะรู้สึกอะไรขึ้นมาบ้าง แต่ก่อนอื่น ฉันแปลกใจที่เธอเป็นคนมาหาฉัน\nและก่อนอื่นที่สอง ตัวเธอเปียกโชก"

# "Her uniform shirt is drenched and she is standing in a self-created puddle."
"เธอใส่ชุดนักเรียนที่ชุ่มน้ำยืนอยู่กลางแอ่งน้ำที่ไหลออกมาจากตัวเธอ"

# "Droplets of rainwater are dripping from her short bangs and sliding down her nose until they fall down from the tip."
"หยดน้ำไหลลงจากหน้าม้าเธอลงมาที่จมูกก่อนจะร่วงหลุดจากปลายจมูกไป"

# "One.{w=0.7} By.{w=0.7} One."
"ที{w=0.7}ละ{w=0.7}หยด{w=0.7} ที{w=0.7}ละ{w=0.7}หยด"

# hi "Umm… hi."
hi "เอ่ออ… ไง"

# hi "How are you feeling?"
hi "เป็นยังไงบ้าง"

show rin basic_deadpannormal
with charachange

# rin "Medium normal."
rin "ครึ่ง ๆ กลาง ๆ เฉย ๆ"

play music music_rin fadein 2.0

# "The relative questionability of her statement aside, she sure doesn't look too good."
"เรื่องความงงในคำตอบนั้นเอาไว้ก่อน ที่แน่ ๆ คือสภาพเธอดูไม่ค่อยดีเท่าไหร่เลย"

# hi "You're all wet."
hi "เปียกหมดแล้วนะ"

show rin basic_absent
with charachange

# rin "It's because I come from the outside. Do you know it?"
rin "เพราะฉันเดินจากข้างนอกมา นายรู้มั้ย"

# hi "Why'd you be outside? It's raining buckets out there, if you haven't noticed."
hi "แล้วจะไปอยู่ข้างนอกทำไม เผื่อเธอไม่ทันสังเกต ข้างนอกนั่นฝนตกหนักอยู่นะ"

show rin basic_deadpancontemplation
with charachange

# rin "I haven't. It's raining pretty hard though. I was on a walk."
rin "ไม่ทันสังเกต แต่ตกหนักใช้ได้เลย ฉันเดินอยู่"

# hi "Is this what you call “wallowing in self-pity?”"
hi "หรือว่านี่คือการ “เวทนาตัวเองให้สมใจ”?"

show rin basic_deadpanupset
with charachange

# rin "Do you think I'm pitiful?"
rin "นายคิดว่าฉันน่าเวทนาเหรอ"

# hi "No, I implied that you think you are."
hi "ไม่ ฉันแค่บอกอ้อม ๆ ไปว่าเธอคิดว่าตัวเองน่าเวทนา"

show rin basic_awayabsent
with charachange

# rin "I'm not, and rain is not a sad thing."
rin "ไม่นะ แล้วฝนก็ไม่ใช่อะไรน่าเศร้าด้วย"

show rin basic_absent
with charachange

# rin "Don't you ever walk in the rain?"
rin "นายไม่เคยคิดอยากเดินตากฝนเหรอ"

# hi "I do, but only with proper equipment, like an umbrella."
hi "ก็คิด แต่ก็ต้องเตรียมพร้อมดี ๆ ก่อน อย่างเช่นร่ม"

show rin basic_lucid
with charachange

# rin "You just need to imagine you have a blue umbrella with white stripes."
rin "นายก็แค่ต้องจินตนาการว่านายมีร่มสีฟ้าที่มีลายทางสีขาว"

# hi "It might be tough when rain is falling on my head."
hi "มีฝนตกใส่หัวอยู่ก็คงนึกยากหน่อยนะ"

show rin basic_deadpannormal
with charachange

# rin "Just imagine harder."
rin "ก็แค่ออกแรงจินตนาการให้มากขึ้น"

"…"

# "Yeah, she definitely is back to normal."
"อืม กลับเป็นปกติแล้วจริง ๆ"

# "Those half-sarcastic, inconsiderate remarks that really push my buttons even though she doesn't mean it, that vacant, spaced-out stare that always expects more than it gives."
"คำพูดลอย ๆ ที่กึ่ง ๆ เสียดสีพวกนั้นที่ยุให้ฉันโมโหได้ถึงเธอจะไม่ได้ตั้งใจก็ตาม สายตานั้นที่ว่างเปล่าและเหม่อลอยที่\nจ้องมาเหมือนคาดหวังเสมอว่าจะได้รับอะไรที่มากกว่าตัวมันเองจะให้ได้"

# "It's so… very much like her."
"เหล่านั้นช่าง… สมเป็นเธอเหลือเกิน"

show rin basic_deadpan
with charachange

# rin "I may need to come in. I need some help with this water and clothes I'm wearing."
rin "ฉันคงต้องขอเข้าห้องหน่อย ฉันอยากให้คนมาจัดการเรื่องน้ำกับเสื้อผ้าที่ฉันใส่อยู่"

# "My brain quickly solves this equation, and I stumble with my words, a stark display of contrast against Rin's easygoing self-invitation."
"สมองฉันไขสมการนี้อย่างรวดเร็วจนฉันพูดตะกุกตะกัก ซึ่งขัดกับรินที่พูดเชิญตัวเองเข้าห้องฉันได้อย่างสบาย ๆ"

# hi "But, Emi…"
hi "แต่เอมิ…"

show rin basic_lucid
with charachange

# "Rin shakes her head vehemently, causing water to sprinkle everywhere."
"เธอสั่นหัวแรง ๆ จนน้ำกระเซ็นไปทั่ว"

# rin "She left."
rin "ไปแล้ว"

show rin basic_awayabsent
with charachange

# rin "Besides she would just worry and fuss until she could not worry or fuss any more, which always takes a troublesomely long time."
rin "อีกอย่าง เอมิจะเป็นห่วงแล้วก็บ่นจุกจิกจนเป็นห่วงแล้วก็บ่นจุกจิกไม่ไหว ซึ่งกว่าจะไม่ไหวก็กินเวลานานจนน่ารำคาญ\nตลอด"

show rin basic_absent
show rain normal behind bg
with charachange

# rin "It's in fact longer than I want to hear her fussing, and I thought you probably are not the fussing kind."
rin "ซึ่งที่จริงก็นานกว่าเวลาที่ฉันอยากจะฟังเธอบ่นจุกจิก แล้วฉันก็คิดว่านายคงไม่ใช่พวกบ่นจุกจิก"

#scene bg school_dormhisao_rn
#show rin invis at center
#with locationchange

$ renpy.music.set_volume(0.4, 1.0, channel="ambient")

hide bg
show rin invis_close at center
show bg misc_sky_rn as bg2 behind rain
show hisaowindow behind rin
with locationchange

show rin relaxed_nonchalant_close_rn:
    ypos 1.1
with Dissolvemove(0.5)

stop music fadeout 8.0
play sound sfx_rustling

# "She slumps down on my desk with a squishy sound."
"เธอนั่งลงกับโต๊ะฉันพร้อมเสียงเสื้อผ้าที่เปียกน้ำ"

# "Her soaked clothes are making the desk and everything on it wet but she doesn't care."
"ซึ่งทำให้ทั้งโต๊ะและทุกอย่างที่วางอยู่บนโต๊ะเปียกหมด แต่เธอก็ไม่สนใจ"

"…"

# hi "Okay. Fine. I'll help you out."
hi "โอเค ได้ เดี๋ยวช่วย"

# hi "I have a towel somewhere. Do you want dry clothes? Is a uniform fine? I'm taller than you, but…"
hi "ฉันมีผ้าขนหนูอยู่ เปลี่ยนเป็นชุดที่แห้งมั้ย ชุดนักเรียนจะเป็นอะไรมั้ย ฉันตัวสูงกว่าเธอแหละ แต่…"

show rin basic_lucid_close_rn
with charachange

# rin "Everything is fine."
rin "อะไรก็ได้"

show bg school_dormhisao_rn
with locationchange

# "With a little searching I find a fresh uniform and a fluffy towel from the depths of my closet."
"พอค้นดูสักหน่อยก็เจอชุดนักเรียนเอี่ยมอ่องหนึ่งชุดกับผ้าขนหนูฟู ๆ ที่อยู่ในหลืบตู้เสื้อผ้า"

hide bg
with locationchange

# "The towel in one hand and the uniform in the other, I turn to face Rin again, uncertain of the next step."
"ฉันถือผ้าขนหนูไว้กับมือข้างหนึ่ง มืออีกข้างถือชุดนักเรียน ก่อนจะหันไปหารินอีกครั้งพลางนึกลังเลว่าจะทำยังไงต่อ"

# "There is something wrong with me, a normal guy would just—{w=1.0}{nw}"
"ฉันต้องเป็นอะไรแน่ ๆ คนปกติคง—{w=1.0}{nw}"

show rin basic_absent_close_rn
with charachange

# rin "Stop worrying. It is not a problem."
rin "เลิกคิดมาก ไม่เป็นอะไรเลย"

# "She probably could see right through my hesitant demeanor."
"คงจะดูท่าทางที่ลังเลของฉันออก"

# "As if I was completely transparent to her."
"ราวกับว่าเธอมองฉันได้อย่างทะลุปรุโปร่ง"

# "I push my anxiety away and concentrate on the eight buttons lined on her shirt, just like mine has."
"ฉันทำใจลืม ๆ ความกังวลไปแล้วจดจ่ออยู่กับกระดุมแปดเม็ดที่เรียงตัวอยู่บนเสื้อเธอเหมือนอย่างเสื้อฉัน"

# "Only the first button is an obstacle, and after getting it over I undo the others with slightly less shaking hands."
"ที่ลำบากคือกระดุมเม็ดแรก แต่พอปลดกระดุมเม็ดแรกเสร็จแล้ว เม็ดต่อ ๆ ไปมือก็เริ่มสั่นน้อยลงเล็กน้อย"

$ renpy.music.set_volume(0.2, 1.0, channel="ambient")
play music music_heart fadein 0.5

scene ev rin_wet_pan_down:
    center
    yalign 1.0 subpixel True
    easein 20.0 yalign 0.0
with whiteout

# "Throwing the soaked shirt aside, I reveal Rin's pale upper body, shrouded only in her light blue brassiere which instantly reminds me of her saying it's her favorite color."
"เมื่อทิ้งเสื้อที่เปียกน้ำไปแล้วก็เผยให้เห็นร่างท่อนบนอันขาวซีดของริน ยกทรงสีฟ้าที่ปกคลุมร่างเธอไว้บางส่วนทำให้\nฉันนึกถึงที่เธอเคยบอกว่าสีนี้เป็นสีโปรดเธอ"

# "I try not to think too much about… stuff, but it's hard not to look at her body with what I can only think of as mixed feelings."
"ฉันห้ามใจตัวเองไม่ให้คิดถึง… อะไร ๆ แต่พอได้มองร่างกายรินแล้วฉันก็อดใจไม่ได้ที่จะไม่ให้รู้สึกอะไรหลายอย่างปนเป"

# "I don't know what to think of this, so I just watch her. Rin looks… brittle."
"ฉันไม่รู้จะคิดกับสิ่งนี้ยังไง จึงมองเธออยู่เฉย ๆ รินนั้นดู… เปราะบาง"

# "She is like a shell, a fragile thing just barely holding together."
"เหมือนเป็นเปลือกแสนเปราะบางที่ประคับประคองตัวเองไว้แทบไม่อยู่"

# "Her ribs, each of them visible under her pale skin, are moving up and down in the rhythm of her breaths."
"ซึ่โครงเธอแต่ละซี่ที่นูนขึ้นมาตามผิวขาวซีดนั้นขยับขึ้นลงตามจังหวะการหายใจของเธอ"

# "Rin always struck me as quite thin, but I realize now that the manic creative period before the exhibition opening might've caused her to lose weight."
"รินนั้นดูเป็นคนผอม ๆ อยู่แล้ว แต่ฉันก็ฉุกคิดได้ว่าที่เธอผอมลงไปอีกส่วนหนึ่งก็คงเป็นเพราะช่วงก่อนวันงานเปิดตัว\nงานนิทรรศการนั้นเธอสร้างสรรค์งานอยู่อย่างบ้าคลั่ง"

# "Did she eat properly and enough? Definitely not and probably not."
"เรื่องข้าวปลาอาหารตอนนั้นเป็นยังไงบ้างเนี่ย ไม่ได้กินให้เป็นเรื่องเป็นราวแน่ ๆ เผลอ ๆ จะกินไม่พอด้วย"

# "This ugly, yet beautiful bare minimum of a human body that belongs to someone I care about is a contradiction of aesthetics in itself, oddly becoming of her."
"เนื้อตัวที่ได้มาตรฐานแบบคาบเส้นอันน่าเกลียดทว่าสวยงามที่เป็นของคนที่ฉันเป็นห่วงนั้นช่างเป็นความย้อนแย้งทาง\nสุนทรียะ ดูสมเป็นตัวรินอย่างประหลาด"

# "My eyes follow her collarbone to her shoulder and down her arm until the abrupt end."
"สายตาฉันลากเริ่มตั้งแต่กระดูกไหปลาร้าของเธอมายังไหล่และมายังแขนของเธอจนถึงส่วนปลาย"

# "No, it's less than the bare minimum, I think with a passing pang of sadness and some guilt for thinking like that."
"ไม่สิ ต่ำกว่ามาตรฐานขั้นต่ำเสียอีก คิดแล้วความเศร้าก็แล่นขึ้นมาพร้อม ๆ กับความรู้สึกผิดที่คิดไปเช่นนั้น"

scene ev rin_wet_arms:
    center
    xalign 0.0 subpixel True
    linear 20.0 xalign 1.0
with flash

# "Her arms, degenerated into almost nothing but bone and skin due to lack of use, look very short now that the long sleeves of her uniform are not covering them:"
"แขนของเธอที่เสื่อมสภาพไปจากการที่ไม่ได้ใช้งานจนเหลือแค่กระดูกและหนังหุ้มนั้นดูสั้นมากเมื่อไม่มีแขนเสื้อยาว ๆ\nของชุดนักเรียนคอยปกปิดอยู่"

# "My lack of any negative reaction makes me think that I've actually grown pretty accustomed of the various physical abnormalities of my schoolmates."
"ฉันไม่ได้รู้สึกไม่ดีอะไรแล้ว ฉันคงจะชินกับความผิดปกติทางร่างกายทั้งหลายแหล่ของเพื่อนร่วมโรงเรียนไปแล้วพอตัว"

#needs a way to express Hisao changing trains of thought here, visual maybe, or maybe I write a transitional line.. scene black is a basic solution
# A CG of Rin sitting? With zoom-in to her stump? - Raide

# "I always wondered why Rin keeps her shirt sleeves long, only tying them in a simple knot at where the elbow would be."
"ฉันสงสัยมาตลอดว่าทำไมรินถึงปล่อยแขนเสื้อเธอให้ยาวแล้วผูกหลวม ๆ ไว้ที่ความยาวประมาณข้อศอก"

# "It seems a bit impractical, but then again she is not exactly the pinnacle of practicality."
"เพราะดูแล้วก็ไม่น่ามีไว้เพื่อทำอะไรได้จริง แต่ก็นะ รินไม่ใช่คนที่จะเอาเรื่องทำได้จริงมาคุยด้วยได้เท่าไหร่"

# "Maybe she likes it, maybe it is somehow important to her. Maybe there is no deeper meaning to it."
"อาจจะชอบ อาจจะสำคัญต่อตัวเธอ อาจจะไม่ได้มีความหมายอะไรไปมากกว่านั้น"

# "I feel like asking, and almost do, but Rin's miserable state requires a higher priority of my attention."
"ฉันอยากจะถามจนแทบจะออกปากถามแล้ว แต่สภาพอันน่าสงสารของรินนั้นเป็นสิ่งต้องการความสนใจจากฉันมากกว่า"

scene ev rin_wet_face_down:
   center
   yalign 0.0
with flash

# "She's stopped talking too, after we ran out of spiky greetings."
"เมื่อหมดคำทักทายแบบตะกุกตะกักแล้วเธอก็หยุดพูดไปเหมือนกัน"

# "I guess there is no need for chitchat then."
"คงไม่ต้องคุยอะไรเรื่อยเปื่อยแล้วละนะ"

scene ev rin_wet_towel_down
with charachange

# "I pick up the towel from the bed and wrap it around her head, rumpling it all over her hair until most of the rainwater is hopefully soaked into the fabric."
"ฉันหยิบผ้าขนหนูที่วางอยู่บนเตียงมาคลุมหัวเธอแล้วเช็ด ๆ ไปทั่ว ๆ ด้วยหวังว่าน้ำฝนจะซึมเข้าผ้าให้ได้มากที่สุด"

scene ev rin_wet_towel_up
with charachange

# "She peeks from below the towel at me, looking up with impassive eyes."
"เธอเหลือบมองฉันอยู่ใต้ผ้าขนหนูด้วยสีหน้าเรียบ ๆ"

# "It looks like she wants to say something without saying it."
"เหมือนอยากจะพูดอะไรโดยที่ไม่ต้องพูด"

# "It's that kind of a look."
"เป็นสายตาเช่นนั้น"

# "But I can't read what she is thinking about from her face, so I just keep on fussing with the towel around her shoulders and hair."
"แต่ฉันอ่านใจเธอด้วยสีหน้าไม่ออก ฉันจึงคอยใช้ผ้าขนหนูเช็ดตามไหล่และผมเธอไปเรื่อย ๆ"

# "The silence is oppressive, terrifying."
"ความเงียบนั้นช่างกดดันและน่ากลัว"

# "Communication between us has suddenly been reduced to the movements of my hands and the towel, and Rin swaying her body to and fro."
"การสื่อสารระหว่างเรากลายเป็นเพียงการขยับมือที่ถือผ้าขนหนูของฉันและการโยกตัวไปมาของริน"

# "My jagged breathing and her quiet breaths, trying to find a common rhythm that just is not there."
"ลมหายใจหอบของฉันและลมหายใจเธอที่แผ่วเบาพยายามประสานให้เป็นจังหวะที่ไม่มีวันลงตัว"

# "I think I can hear her heartbeats, or maybe they are just mine redoubled."
"เหมือนจะได้ยินเสียงหัวใจเธอด้วย หรือไม่ก็เป็นเสียงหัวใจฉันนี่แหละที่ดังขึ้น"

# "As I brush a rogue strand of hair aside from her ear, Rin suddenly presses her cheek against the back of my hand."
"ระหว่างที่ทัดผมยุ่งเส้นหนึ่งเข้าที่หูเธอนั้นรินก็แนบแก้มเข้ากับหลังมือฉัน"

# "The contact is electric, a jolt of current surging through me."
"สัมผัสนั้นส่งกระแสไฟฟ้าไปทั่วร่างฉัน"

scene ev rin_wet_towel_touch
with charachange

# "Whether she seeks comfort, warmth or just my touch I wouldn't know, but I can't help touching her back, caressing her soft cheek with my hand."
"ไม่ว่าเธอจะอยากได้ความสบาย ความอบอุ่น หรือสัมผัสของฉัน ฉันคงไม่รู้ แต่ฉันอดใจไม่ไหวที่จะแตะเธอกลับบ้าง\nโดยการใช้มือฉันโอบอุ้มแก้มนุ่มเธอไว้"

# "And with closed eyes, she kisses me, on the fingers, counting the joints with her lips…"
"เธอหลับตาแล้วจูบนิ้วฉันพลางใช้ริมฝีปากเธอไล่นับข้อนิ้วฉัน…"

# "I am saddened beyond my expressive capability."
"ฉันเศร้าใจเกินกว่าที่ฉันจะแสดงออกได้"

# "Here we are, a boy and girl, both in love or something like that with each other, or maybe not… and yet…"
"ชายหญิงที่ตกหลุมรักหรืออะไรประมาณนั้นกันและกัน หรืออาจจะไม่ใช่… แต่กลับ…"

$ renpy.music.set_volume(0.1, 1.0, channel="ambient")
$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

# n "\nSomething is broken, I can feel it in me and in Rin; in the way our gazes merely brush against each other, shying away from contact; in her closed, timid posture and in my way of touching her like a china doll, afraid of shattering her delicate form."
n "\nฉันรู้สึกถึงบางอย่างในตัวฉันและรินที่แหลกสลาย ดูจากการที่สายตาของเราสบกันเพียงครู่สั้น ๆ ไม่ยอมจดจ้อง ดูจาก\nท่าทางเหนียมอายปกปิดของเธอ และดูจากการที่ฉันแตะต้องเธอราวกับกลัวว่าจะทำให้ร่างกายอันบอบบางของเธอที่\nคล้ายตุ๊กตาดินเผานั้นแตกสลาย"

# n "In how we are closer than we have ever been, yet I'm not feeling happy. It's like yesterday."
n "ดูจากการที่พวกเราได้ใกล้ชิดกันกว่าที่เคยแต่ฉันกลับไม่มีความสุข เหมือนอย่างเมื่อวาน"

# n "When did tenderness and forlornness become one and the same word, acts of affection start invoking only longing? …How, why did we end up like this?"
n "ความอ่อนโยนและความเดียวดายกลายเป็นคำเดียวกันไปตั้งแต่ตอนไหนกัน การแสดงความรักทำให้เกิดความโหยหา\nไปตั้งแต่ตอนไหนกัน …พวกเรากลายเป็นอย่างนี้ไปได้อย่างไร—เพราะอะไรกัน"

# n "“No, don't answer that,” I'd like to say to myself, but fighting against the omniscience of self-awareness is a lost cause."
n "“ไม่ อย่าหาคำตอบเลย” ฉันอยากจะบอกตัวเองอย่างนั้น แต่ฝืนทนความรู้สึกระลึกตัวอันทรงพลังไปก็เหนื่อยเปล่า"

# n "Still, I am here, and Rin is here, and it feels like she might be able to solve whatever problems she has."
n "แต่ ฉันก็อยู่ตรงนี้ และรินก็อยู่ตรงนี้ และรู้สึกเหมือนว่าเธออาจจะแก้ไขปัญหาอะไรก็ตามที่เธอมีอยู่ได้"

# n "And if she can, why couldn't I? Why couldn't we?"
n "และถ้าเธอแก้ได้ ทำไมฉันแก้ไม่ได้ ทำไมเราแก้ไม่ได้"

# n "It feels like taking that step is too much, too difficult, too uncertain."
n "เหมือนว่าการก้าวก้าวนั้นจะลำบากเกินไป ยากเกินไป ไม่แน่ใจเกินไป"

# n "So for now, all I can do is dry her up so she won't get a cold again."
n "เพราะฉะนั้น สิ่งที่ฉันทำได้ตอนนี้มีเพียงการเช็ดตัวรินให้แห้งไม่ให้เธอเป็นหวัดอีก"

$ renpy.music.set_volume(0.2, 1.0, channel="ambient")
$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

scene ev rin_wet_face_up
with charachange

window show

# "I pet her head, trying to sort out the hair that refuses to be sorted out even when wet."
"ฉันลูบ ๆ หัวรินจัดระเบียบผมบางเส้นของเธอที่ไม่ยอมลู่แม้จะเปียกน้ำ"

# "A pair of dark, glazed eyes follows my every movement."
"ตาสีเข้มเนือย ๆ คู่นั้นตามมองทุกการเคลื่อนไหวของฉัน"

# hi "Pants too?"
hi "กางเกงด้วยมั้ย"

scene ev rin_wet_face_down
with charachange

# "She nods an answer, leans back and spreads her legs, with a grotesquely inviting gesture that makes a nasty feeling crawl up and down my spine like a bad premonition."
"เธอพยักหน้าตกลงก่อนจะเอนตัวแล้วอ้าขาออก เป็นท่าทางเชื้อชวนอันเย้ายั่วชวนให้รู้สึกยอกแขยงขึ้นมาไปทั่วร่าง\nเหมือนมีลางร้ายบางอย่าง"

# "It's not enough to sober me though, as the silence is starting to make me feel detached from myself."
"แต่ก็ยังไม่หนักพอที่จะปลุกฉันให้สร่างได้ เพราะความเงียบนี้นั้นเริ่มทำให้ฉันสติหลุดแล้ว"

# "I move automatically, without thinking even though I should; I should talk to her about this, or at least about something."
"ฉันขยับไปโดยอัตโนมัติโดยไม่คิดอะไรทั้ง ๆ ที่ควรคิด ฉันน่าจะคุยกับเธอเรื่องนี้ หรืออย่างน้อยก็สักเรื่อง"

# "The silence is a spell, a pact that has bound us to this private world made of the dull sound of rainfall and the soft feel of her skin against my fingers."
"ความเงียบนั้นเป็นมนตร์สะกด เป็นข้อตกลงที่ผูกมัดให้เราอยู่ในโลกใบนี้ที่กอปรด้วยเสียงฝนสาดทึบตันและสัมผัส\nอันนุ่มนวลของผิวเธอที่ถูกนิ้วฉัน"

# "The button of her trousers is fastened tight, but it opens surprisingly easily."
"กระดุมกางเกงเธอนั้นติดแน่น แต่ก็ปลดออกได้ง่ายกว่าที่คิด"

# "Slipping them off is hard, mostly because she is sitting on them, with no intention of standing up to ease my task."
"จะถอดออกมาก็ยากเพราะเธอนั่งทับอยู่โดยไม่มีท่าทีว่าจะลุกให้ฉันจัดการได้ง่าย ๆ เลย"

scene unlock_evh rin_h2_pan_surprise 
show evh rin_h2_pan_surprise:
     xalign 0.5 yalign 0.0
with whiteout

# "I kneel down uncomfortably and titillatingly between her legs so I can quickly dry her bare feet, remembering that they are as important to her as hands are to me."
"ฉันคุกเข่าลงตรงระหว่างขาเธออย่างอึดอัดและหมิ่นเหม่เพื่อที่จะได้เช็ดเท้าเปล่าเธอให้แห้งเร็ว ๆ เพราะเห็นว่าเท้าเธอนั้น\nก็สำคัญพอ ๆ กันกับการที่มือนั้นสำคัญกับฉัน"

# "As I work the towel up from her ankles, Rin brushes her thigh against my cheek and nudges the small of my back with her heel to make me come closer."
"ระหว่างที่ฉันไล่เช็ดจากข้อเท้าเธอขึ้นไปรินก็แนบต้นขาเข้ากับแก้มฉันพลางใช้ส้นเท้ากดหลังฉันให้ขยับเข้าไปใกล้ ๆ"

# "I look up to meet her silent stare that was waiting for me to look up."
"พอเงยหน้ามองก็เห็นเธอที่มองเงียบ ๆ รอให้ฉันเงยหน้าขึ้นไปมองอยู่"

# "That unassuming, expectant stare seems to say that the ball is in my court."
"สายตาเรียบนิ่งที่จ้องมาเหมือนคาดหวังบางอย่างนั้นดูราวกับจะบอกว่าเป็นตาของฉันที่ต้องเดินเกมต่อแล้ว"

"…"

# "I fleetingly brush my hand against her inner thigh."
"ฉันลูบต้นขาด้านในของเธอเบา ๆ"

show unlock_evh rin_h2_pan_away
show evh rin_h2_pan_away
with charachange

# "The touch makes her gasp sharply, as if she was trying to hold back breathing."
"เธอสะดุ้งเฮือกทันทีที่ฉันแตะคล้ายว่ากลั้นหายใจอยู่"

# "What if I do this, then?"
"แล้วถ้าทำอย่างนี้ล่ะ"

show unlock_evh rin_h2_pan_closed
show evh rin_h2_pan_closed
with charachange

# "The small kiss I place on her thigh is enough to make Rin lose her composure, to shut her eyes, to squeal almost inaudibly."
"เพียงฉันประทับจูบเข้าที่ต้นขาเธอก็ทำให้เธอควบคุมตัวเองไม่อยู่ ทำให้เธอหลับตา ทำให้เธอครางเบา ๆ"

# "…Is that what you want too? Would it be all right now? To take this step?"
"…เธอก็ต้องการอย่างนี้ด้วยหรือเปล่า ตอนนี้จะให้ทำอย่างนี้ไปเลยได้หรือเปล่า"

show evh rin_h2_pan_closed:
    subpixel True
    acdc_warp 8.0 yalign 1.0
with None

# "…What if? Maybe if…"
"…ถ้าเกิดว่า บางที ถ้า…"

# "Hazy thoughts float somewhere in the back of my unfocused mind."
"ความคิดอันเลือนรางลอยคว้างอยู่สักที่หนึ่งในสมองที่ไร้ซึ่งการจดจ่อของฉัน"

# "Somehow, this whole situation is making it hard to think, as if my head was full of cotton fluff."
"ไม่รู้ทำไม แต่สถานการณ์ตรงหน้านี้ทำให้ฉันคิดอะไรไม่ค่อยออกแล้ว ในสมองมีแต่ก้อนฝ้ายฟู ๆ อัดแน่นเต็มไปหมด"

# "But that's all right. It seems thinking is not something we need right now."
"แต่ไม่เป็นไรหรอก ดูท่าว่าการคิดจะไม่ใช่อะไรที่พวกเราต้องการในตอนนี้"

label th_R41h:
show evh rin_h2_nopan_closed:
     yalign 1.0
with Dissolvemove(0.5)

$ renpy.music.play(music_heart, fadein=0.5, if_changed=True)

# "By the grace of vastly smaller amount of fabric, slipping off Rin's panties is considerably easier than her trousers."
"กางเกงในของรินนั้นถอดง่ายกว่ากางเกงพอสมควร ด้วยความที่กางเกงในนั้นมีพื้นที่ของเนื้อผ้าน้อยกว่ากางเกง\nเป็นอย่างมาก"
# Such sitting CG could be used up to this point. - Raide
#Nudged up the scene header by one line, and it may well be nudged up a LOT more. -SC

# "They disappear past my field of vision, sliding somewhere away down her legs."
"และกางเกงในนั้นเลื่อนลงตามขาเธอไปสักที่ลับสายตาฉันไป"

# "It seems I did a poor job with the towel, since Rin's legs are still wet from the rain."
"ดูเหมือนว่าฉันจะยังใช้ผ้าขนหนูเช็ดได้ไม่ดีเท่าไหร่ เพราะขารินยังเปียกฝนอยู่เลย"

# "Well, whatever."
"แต่เอาเถอะ"

show evh rin_h2_hisao_closed
with charachange

# "Guided by instinct more than rationality, I move closer and taste the different kind of wetness."
"ฉันปล่อยให้สัญชาตญาณนำทางแทนเหตุผลแล้วขยับเข้าไปลิ้มรสอีกความชื้นแฉะหนึ่ง"

# "She responds to me, to the slow movements of my tongue on her skin, to my kisses on her flesh."
"เธอตอบสนองต่อลิ้นของฉันที่เคลื่อนไหวช้า ๆ อยู่บนผิวเธอ และตอบสนองต่อริมฝีปากฉันที่สัมผัสกับเนื้อเธอ"

# "Her muscles tense and relax in the rhythm, as if what I am doing was uncomfortable."
"กล้ามเนื้อเธอเกร็งและคลายเป็นจังหวะ ราวกับว่าสิ่งที่ฉันทำอยู่นั้นชวนให้อึดอัด"

# "To hear Rin trying not to make a sound when I suck on her is… unreal."
"การที่ได้ฟังเสียงรินที่พยายามกลั้นเสียงตัวเองตอนฉันกำลังดูดดื่มเธอนั้นทำให้รู้สึกเหมือน… หลุดไปจากความเป็นจริง"

# "This whole morning has been so unreal, like the surreal intangibility of an awakening dream."
"ตลอดเช้านี้นั้นเหมือนหลุดไปจากความเป็นจริง เหมือนความเหนือจริงที่แตะต้องไม่ได้ของฝันเมื่อก่อนลืมตาตื่น"

# "I can't believe I am doing this, to her, now. But I am going with the flow."
"ไม่อยากจะเชื่อเลยว่าฉันมาทำแบบนี้ให้เธอ แต่ฉันก็ปล่อยตัวให้ไหลไปตามอารมณ์"

# "Besides, the point of no return was a thousand miles ago."
"อีกอย่าง จะให้หันหลังกลับเอาป่านนี้ก็สายไปมากแล้ว"

# "I move around, try to do things to her, to find the places where her weakness lies, to tease her, to drive her mad with pleasure because I want to, I want to do this to her."
"ฉันขยับไปมาทำนั่นนี่กับเธอ เพื่อจะหาว่าจุดอ่อนเธออยู่ตรงไหน เพื่อจะเย้าหยอกเธอ เพื่อจะทำให้เธอบ้าคลั่งด้วย\nความรู้สึกดีเพราะฉันอยากทำ ฉันอยากทำอย่างนี้กับเธอ"

# "But she doesn't squeal, she doesn't squirm, for maybe I can't make Rin any madder than she already is, whatever I do."
"แต่เธอไม่หวีดร้อง เธอไม่ดีดดิ้น อาจจะเพราะฉันคงทำให้เธอบ้าไปกว่าที่เธอเป็นอยู่ไม่ได้แล้ว ไม่ว่าฉันจะทำอะไรก็ตาม"

# "Her ragged, heavy breathing mixed with unintelligible moans is that of a lunatic, but I do not cause it."
"เธอหายใจหอบถี่ครางกระเส่าไม่ได้ความอย่างคนคลั่ง แต่ฉันไม่ได้เป็นคนสร้างขึ้นมา"

# "I only release that from her."
"ฉันเพียงแต่ปล่อยด้านนั้นออกมาจากตัวเธอ"

# "She becomes more and more moist, and I drink from her, feeling a heat growing inside myself."
"เธอยิ่งชื้นแฉะหนักขึ้นเรื่อย ๆ ฉันดูดดื่มจากตัวเธอ ในกายฉันร้อนรุ่มขึ้นทุกที"

# "I try to reach her deepest places, to feel all of her I can this way."
"ฉันควานเข้าไปให้ถึงข้างในสุดตัวเธอ สัมผัสเธอให้มากเท่าที่ทำได้ด้วยวิธีนี้"

# "My every action is met with a different reaction, but all of those are out of pure lust."
"ทุกกิริยาของฉันมีปฏิกิริยาที่ตอบกลับต่างกัน แต่เหล่านั้นก็เกิดเพียงด้วยราคะ"

show evh rin_h2_hisao_closed:
    subpixel True
    acdc_warp 16.0 yalign 0.0
with None

# "Rin is lost in desire, willing to let anything happen to her if I do it right now."
"รินจมจ่อมไปกับความปรารถนาของตัวเธอและปล่อยให้ตัวเองถูกกระทำตามใจฉันอยาก"

# "She becomes closer and closer to the moment of release, but the way to that is an uphill slope of madness."
"เธอเคลื่อนเข้าใกล้ถึงการปลดปล่อยขึ้นไปเรื่อย ๆ แม้เส้นทางข้างหน้านั้นจะทำให้เธอต้องคลั่งก็ตามที"

# "Still, she is going that way."
"เธอก็ยังจะไปตามทางนั้น"

# "The muscles don't relax any more between the waves of ecstatic spasms."
"กล้ามเนื้อเธอไม่คลายลงอีก ยิ่งกระตุกเกร็งไปตามความสุขสมทุกขณะ"

# "Rin just becomes tenser and tenser, contracting so much that it must be physically painful, but I do not let go."
"เธอเกร็งหนักขึ้นเรื่อย ๆ จนดูเหมือนจะยิ่งทำให้เธอเจ็บแทน แต่ฉันไม่ยอมปล่อย"

# "I keep going, and I know she wants it too, she desperately wants me to do this to her."
"ฉันยังทำต่อไป และฉันก็รู้ว่าเธอต้องการ เธออยากให้ฉันทำอย่างนี้กับเธอเหลือเกิน"

# "A leg curls around my shoulders and draws me closer, so close that I think that I'm going to choke."
"เธอหุบขาพาดไหล่รั้งฉันให้เข้าใกล้จนแทบสำลัก"

# "I keep going because it's the only possibility."
"ฉันยังคงทำต่อเพราะไม่มีทางเลือกอื่นแล้ว"

stop music fadeout 8.0
stop ambient fadeout 12.0

# "As I push the button that drives her into gasping for breath, locking her leg into a cramp against my back, losing her mind in the sensation, at that precise moment I seem to forget all that was meant to be, all that should be."
"ณ ขณะนั้น—ตอนที่ฉันกระตุ้นจุดที่ทำให้เธอต้องหอบฮักและรัดขาแนบกับหลังฉันแน่นปล่อยให้อารมณ์โถมเข้าซัด\nตัวเธอ—ฉันคล้ายว่าจะลืมเป้าหมายทุกสิ่งอย่าง ลืมว่าทุกอย่างควรจะเป็นอย่างไร"

# "All I know is that she came here and… I think there was a towel at some point, too."
"สิ่งที่ฉันรู้มีเพียงว่าเธอมาที่นี่และ… ฉันว่าเหมือนจะมีผ้าขนหนูด้วย"

# "None of it matters, all that matters is this, what we have now."
"ไม่มีสิ่งใดสำคัญ สิ่งสำคัญมีเพียงสิ่งนี้ที่เราทำอยู่ในตอนนี้"

# "Her orgasm surges through me too, exciting me in a completely new way."
"จุดสุดยอดของเธอส่งผ่านมาถึงตัวฉันจนทำให้ฉันตื่นเต้นขึ้นมาในแบบที่ฉันไม่เคยรู้สึกมาก่อน"

# "It makes me feel anxious, nervous. Bothered."
"เป็นความรู้สึกที่ทำให้ฉันร้อนใจ ร้อนรน ร้อนรุ่ม"

show evh rin_h2_hisao_away:
    yalign 0.0
with Dissolvemove(0.5)

# "As her body relaxes, I try to kiss her down there again, but it startles her, causing her to jump."
"จังหวะที่เธอหายเกร็งฉันเข้าจูบส่วนล่างเธออีกครั้ง แต่เธอก็ตกใจจนสะดุ้ง"

show evh rin_h2_hisao_surprise
with charachange

# rin "No… Hisao… Enough."
rin "ไม่… ฮิซาโอะ… พอแล้ว"

# rin "Come here."
rin "มานี่"

scene bg school_dormhisao_rn
with locationchange

# "I stand up to remove the last piece of clothing Rin has."
"ฉันยืนขึ้นแล้วถอดสิ่งสุดท้ายที่ปกปิดกายเธออยู่"

# "She leans against me to catch her breath, tickling me with warm air exhaled into my shirt."
"เธอพิงกับฉันเพื่อพักหายใจ ลมหายใจเธอรดเสื้อฉันจนฉันจักจี้"

# "Blindly, I reach behind her back to feel my way below her shoulder blades, to find the contraption that fastens her bra."
"ฉันคลำไปตามกระดูกสะบักของเธอแล้วเลื่อนไปอีกเพื่อตามหาตะขอที่รั้งยกทรงของเธออยู่"

# "It opens more easily than I thought, falling to the floor somewhere."
"ซึ่งแกะง่ายกว่าที่คิด ยกทรงนั้นหล่นไปกับพื้นสักที่"

play music music_romance fadein 10.0

scene ev rin_pair_base_clothes
show rp_hisao normal at truecenter
show rp_rin normal at truecenter
with whiteout

# "Her bare skin against me is a sensation so wonderful that I want to have more of it, and I do, embracing her."
"สัมผัสจากร่างเปลือยของเธอที่แนบฉันนั้นรู้สึกดีเสียจนฉันอยากสัมผัสอีก และฉันก็สัมผัสอีกโดยการโอบกอดเธอ"

# "Rin's hair smells of rain, and I realize that I'm not hearing the sound of rainfall any more."
"ผมของรินนั้นมีกลิ่นฝน และฉันก็เพิ่งรู้สึกตัวว่าไม่มีเสียงฝนแล้ว"

# "It's a sobering thing. The cushion that enveloped us into a reality of our own is now gone, and I realize more clearly what is happening."
"เมื่อไม่มีแล้วก็ชวนให้สร่าง สิ่งห่อหุ้มที่กั้นพวกเราออกจากความเป็นจริงนั้นไม่มีอีกต่อไป สิ่งที่เกิดขึ้นตรงหน้าเข้ากระทบ\nประสาทการรับรู้ได้แจ่มแจ้งขึ้น"

show rp_hisao frown
with charachange

# hi "You know, this really is not what friends should be doing."
hi "เนี่ย เพื่อนกันเขาไม่ทำอย่างนี้กันเลยนะ"

# "I whisper, once again noticing how such a simple matter as talking can be overbearingly difficult at times."
"ฉันกระซิบแผ่ว เป็นอีกครั้งที่ฉันรู้ตัวว่าสิ่งที่พูดได้ง่าย ๆ นั้นบางทีก็พูดยากจนเกินรับได้เหมือนกัน"

show rp_rin talk
with charachange

# rin "Will you stop being my friend?"
rin "นายจะไม่เป็นเพื่อนฉันแล้วเหรอ"

#"She whispers it so close to my ear that it tickles."

# "That wasn't what I meant, but her serious tone and the layers of connotations behind Rin's question give me pause."
"ไม่ได้หมายความว่าอย่างนั้น แต่น้ำเสียงจริงจังของเธอและความหมายแฝงที่อยู่ในคำถามนั้นทำให้ฉันต้องชะงัก"

show rp_hisao smile
with charachange

# hi "Nah."
hi "ไม่อะ"

show rp_rin smile
with charachange

# rin "I… think it might be all right. Even if you did."
rin "ฉัน… คิดว่าคงไม่เป็นอะไรหรอก ต่อให้เป็นอย่างนั้น"

# "I hug her and smile into her hair, understanding Rin perfectly for once."
"ฉันกอดเธอแล้วยิ้มกับผมเธอ เข้าใจในสิ่งที่รินพูดได้แจ่มแจ้งได้สักที"

show rp_rin frown
with charachange

# rin "You are wet."
rin "นายเปียก"

# "The remnants of water on her skin have drained into my shirt."
"น้ำที่ชุ่มอยู่กับตัวเธอซึมเข้ามาที่เสื้อฉัน"

# "Somehow, even her statements of the obvious make me glad right now."
"ไม่รู้ทำไม แต่แม้แต่คำพูดเธอที่บอกสิ่งที่เห็น ๆ กันอยู่นั้นก็ทำให้ฉันดีใจได้"

show rp_hisao normal
with charachange

# hi "You're right. I am. But that's your fault."
hi "เธอพูดถูก ฉันเปียก แต่ก็ความผิดเธอนั่นแหละ"

show rp_rin normal
with charachange

# rin "I want to see you."
rin "ฉันอยากเห็นนาย"

play sound sfx_rustling

scene ev rin_pair_base
with charachange

# "I comply, standing back to open the buttons of my shirt, much more quickly than when I undid Rin's buttons."
"ฉันทำตามโดยการถอยออกมาแล้วปลดกระดุมเสื้อตัวเองออก ซึ่งปลดได้เร็วกว่าตอนที่ฉันปลดกระดุมเสื้อรินอีก"

# "A sudden sense of haste strikes me, spurring me to rush forward."
"อยู่ ๆ ฉันก็รู้สึกรีบร้อนขึ้นมาจนต้องเร่งตัวเองขึ้นเรื่อย ๆ"

# "Every second I'm not touching Rin is a second wasted, a chance lost."
"ทุกวินาทีที่ไม่ได้สัมผัสรินคือทุกวินาทีที่จะเสียเปล่า เป็นโอกาสที่เสียไป"

# "My belt buckle proves an obstacle despite my ability to open it in an eyeblink under normal circumstances."
"แม้แต่หัวเข็มขัดก็ปลดยากขึ้นมา ทั้ง ๆ ที่ปกติก็แกะออกได้ในพริบตาเดียวแท้ ๆ"

show rp_rin closed
with charachange

# "While I fumble with it, I don't notice Rin bringing her foot up between us until she starts tracing my chest with her toe."
"ระหว่างที่ฉันกำลังวุ่นวายอยู่กับหัวเข็มขัดก็ไม่ทันได้สังเกตเห็นรินที่ยกเท้าขึ้นมาจนกระทั่งเท้าเธอแตะเข้ากับหน้าอกฉัน"

show rp_hisao frown
with charachange

# "I look down to see what she's looking at…"
"ฉันก้มมองว่าเธอมองอะไรอยู่"

# hi "My heart…"
hi "ใจฉัน…"

# "I reflexively flinch back, covering the scar tissue in the middle of my chest."
"ฉันผงะไปโดยอัตโนมัติแล้วเอามือลูบหน้าอกตัวเอง"

# "The shallow mark that the surgery following my heart attack left on my body has healed already but… well, it's not a particularly pretty sight if not overly repulsive either."
"รอยแผลตื้น ๆ ที่ได้มาจากการผ่าตัดเมื่อครั้งที่หัวใจวายตอนนั้นก็หายดีแล้ว แต่ว่า… ก็ไม่ได้เป็นภาพที่น่าดูเท่าไหร่\nแต่ก็ไม่ได้น่าเกลียดขนาดนั้น"

# "It's barely noticeable, but she does have an eye for detail. Is this why she said she wanted to see me?"
"แทบจะมองไม่เห็นด้วยซ้ำ แต่ตาเธอจับรายละเอียดได้ดี หรือที่บอกว่าอยากเห็นคืออย่างนี้?"

# "I had sorta forgotten about this because of all this mess with Rin, but now all the unpleasant things connected to my condition surface at once, rushing through my mind like a flash flood."
"ฉันก็ลืม ๆ เรื่องนี้ไปแล้วเพราะมัวแต่วุ่นวายอยู่กับริน แต่ตอนนี้สิ่งไม่พึงประสงค์ทั้งหลายที่โยงอยู่กับโรคของฉันซัดสาด\nเข้ามาในความคิดเหมือนอย่างน้ำหลากทะลัก"

# "And oh God all the stories about old guys getting heart attacks when having sex, what if…"
"แล้วก็ ให้ตายเถอะ พวกเรื่องที่ว่าคนแก่ ๆ ตายเพราะหัวใจวายตอนมีอะไรกันก็มา ถ้าเกิดว่า…"

show rp_rin talk
with charachange

# rin "Hisao."
rin "ฮิซาโอะ"

"…"

# "Realizing that I might just have spoiled the mood, I stumble to explain myself."
"พอนึกได้ว่าคงทำอารมณ์กร่อยไปฉันจึงรีบแก้ตัวด้วยความตะกุกตะกัก"

show rp_hisao normal
with charachange

# hi "Ah… sorry, it's just that…"
hi "อ่า… ขอโทษที พอดีว่า…"

show rp_rin smile
with charachange

# rin "Let me touch you."
rin "ขอแตะหน่อยสิ"

# "Her eyes are sultry, inviting as she sits there bare naked without an inkling of shame. I never thought Rin could look like that."
"ดวงตารัญจวนเธอเชื้อเชิญ เธอนั่งเปลือยอยู่อย่างนั้นโดยไม่มีแม้ยางอาย ไม่เคยคิดเลยว่ารินจะเป็นอย่างนี้ได้ด้วย"

$ renpy.music.set_volume(0.1, 1.0, channel="ambient")
$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

# n "\n\nYeah, I know this is not how it should go."
n "\n\nอืม ฉันรู้ว่าอะไร ๆ ไม่ควรเป็นอย่างนี้"

# n "Even though Rin is right here, even though there should be no more questions, no obstacles, not this maddening feeling that something is constantly wrong…"
n "แม้รินจะอยู่ตรงนี้ แม้ไม่น่ามีคำถาม ไม่น่ามีสิ่งกีดขวาง ไม่น่ามีความรู้สึกที่ว่าบางอย่างผิดแผกไปตลอดที่ทำให้แทบบ้า\nแล้ว…"

# n "The same feeling that clutched my heart yesterday makes its appearance."
n "แต่ความรู้สึกที่เกาะกุมใจฉันอยู่เมื่อวานกลับปรากฏ"

# n "We are together. In a way that is difficult to define, it eludes description as stubbornly as it evades change."
n "พวกเราอยู่ด้วยกัน ในแบบที่ยากจะนิยาม แบบที่ไม่ยอมให้อะไรมาอธิบายได้ แบบที่ไม่ยอมเปลี่ยนแปลง"

# n "\nWould a relationship like this be all right? Could we ever change to become closer?"
n "\nความสัมพันธ์อย่างนี้จะใช้ได้หรือเปล่า พวกเราจะเปลี่ยนเพื่อให้ใกล้ชิดกันไปอีกได้หรือเปล่า"

# n "Even though we would stay together for all of eternity, we might never find our mutual understanding."
n "ต่อให้เราจะอยู่ด้วยกันตราบชั่วฟ้าดินสลาย พวกเราก็อาจจะหาจุดเข้าใจร่วมกันไม่เจอเลย"

# n "But there is no such thing as eternity. This may mean that we will not be together forever."
n "แต่ตราบชั่วฟ้าดินสลายนั้นไม่มีจริง ซึ่งแปลว่าเราอาจจะไม่ได้อยู่ด้วยกันไปตลอดกาล"

# n "If not our differences, then the flow of time will pull us apart with irresistible force."
n "ต่อให้เราก้าวข้ามผ่านเรื่องความแตกต่างไปได้แล้ว สายธารเวลาก็จะยังเป็นอีกสิ่งที่จะพรากเราจากกันด้วยแรงที่ไม่อาจ\nมีสิ่งใดต้านทาน"

nvl clear

# n "\n\nRin is a creature of the moment, of whim and of impulse."
n "\n\nรินเป็นสิ่งมีชีวิตแห่งขณะปัจจุบัน แห่งความคิดชั่วแล่น และแห่งแรงกระตุ้น"

# n "\nI am nothing of the sort."
n "\nฉันไม่ใช่อะไรอย่างนั้นเลย"

# n "\nThis is a fact that I can understand very clearly."
n "\nเป็นความจริงที่ฉันเข้าใจอย่างชัดแจ้ง"

# n "If for no other reason, for this reason I should grasp this moment. Even if it's the only moment we will ever have, I should not let myself spoil it."
n "ถ้าไม่ใช่เพราะเหตุผลอย่างอื่น เหตุผลนี้ก็จะเป็นเหตุผลที่ฉันต้องอยู่กับปัจจุบัน ต่อให้พวกเราจะได้อยู่ด้วยกันเพียง\nชั่วขณะเดียว ฉันก็ไม่ควรปล่อยให้ตัวเองต้องทำมันพัง"

# n "Even if I can't escape myself. Rin can't either, I know it now."
n "ต่อให้ตัวฉันเองจะหนีไปไม่ได้ก็ตาม รินก็หนีไม่ได้เช่นกัน ตอนนี้ฉันรู้แล้ว"

# n "\nWe both have things we can't let go, things we can't not think."
n "\nพวกเราต่างก็มีสิ่งที่พวกเราปล่อยไปไม่ได้ สิ่งที่พวกเราละทิ้งไม่คิดถึงไม่ได้"

# n "Feelings we can't not feel."
n "ความรู้สึกที่พวกเราไม่รู้สึกไม่ได้"

# n "But she allows herself to want me without any restraint. Here and now."
n "แต่เธอปล่อยให้ตัวเองไหลไปตามอารมณ์ที่ต้องการฉันโดยไม่มีการปิดกั้นใด ๆ ณ ตรงนี้ ณ ตอนนี้"

$ renpy.music.set_volume(0.2, 1.0, channel="ambient")
$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

show rp_hisao frown
with charachange

window show

# hi "I'm sorry, you know…"
hi "ฉันขอโทษ คือ…"

show rp_rin closed
with charachange

# rin "Hisao, you really have to stop worrying."
rin "ฮิซาโอะ นายต้องเลิกคิดมากได้แล้วนะ"

# "Rin interrupts me before I get further, which is good because I don't know what I could have said."
"รินขัดจังหวะไม่ให้ฉันได้พูดอะไรต่อ แต่ก็ดี เพราะฉันไม่รู้ว่าฉันจะพูดออกไรออกไปอีก"

# "Her voice, void of its usual spaciness, scolds me softly, without an edge."
"เสียงเธอที่ไม่มีความเหม่อลอยอย่างทุกทีดุฉันด้วยความอ่อนโยนอย่างไม่ทิ่มแทง"

show rp_rin smile
with charachange

# rin "You really have to learn to let go."
rin "นายต้องหัดปล่อยวางบ้างนะ"

# "She scans me calmly, almost calculatingly."
"เธอกวาดตามองฉันอย่างใจเย็นคล้ายกะเกณฑ์บางอย่าง"

# "I wonder what I look like through her eyes."
"เธอจะมองฉันเป็นยังไงนะ"

# "Damn. They are so green it almost hurts."
"ให้ตาย เขียวเสียจนใจเจ็บ"

# "I always was so enchanted by her eyes, those mysterious, captivating eyes that always were too restless for their own good."
"ฉันหลงใหลในดวงตาคู่นั้นมาเสมอ ดวงตาอันลึกลับและตรึงใจที่ไม่เคยจะอยู่เฉย ๆ ได้ ซึ่งก็ดีแล้ว"

# "But I was also always intimidated by them."
"แต่ฉันก็กลัวมาตลอด"

# "Yeah. Rin is intimidating, on more than one level and especially right now."
"ใช่ รินน่ะน่ากลัว ในหลาย ๆ ความหมาย โดยเฉพาะตอนนี้"

# "She is frighteningly lucid, the goosebumps on her skin giving away that she is cold, or scared too."
"ที่เธอดูออกง่ายจนน่ากลัว ขนบนผิวเธอที่ตั้งชันบอกว่าเธอกำลังหนาวไม่ก็กลัวด้วย"

# "Either way, I steel myself and step back to Rin, embracing her to feel her in my arms again and to banish my doubts."
"แต่เอาเถอะ ฉันเดินกลับเข้าไปหารินแล้วรับเธอเข้ามาในโอบกอดอีกครั้งเพื่อขับไล่ความเคลือบแคลงทั้งหลาย\nของตัวเอง"

# "The sight of her gentle, loving eyes seems to melt those doubts away like the last snow of winter."
"พอได้มองดวงตาอันอ่อนโยนที่เต็มไปด้วยความรักของเธอแล้วความเคลือบแคลงก็ละลายหายไปเหมือนอย่างหิมะ\nเมื่อสิ้นฤดูหนาว"

scene evh rin_h_closed
with whiteout

# "She presses her head against my shoulder, seeking a place to rest herself in, leaning against me like I lean against her."
"เธอกดหัวเข้ากับไหล่ฉันเพื่อหาที่พักพิง เธอพิงตัวฉันเหมือนอย่างที่ฉันพิงตัวเธอ"

# rin "Let go."
rin "ปล่อย"

# "Yes."
"นั่นสินะ"

scene evh rin_h_left
with charachange

# rin "You should forget about stuff like future and past, it's not like you can change those kinds of things."
rin "นายต้องลืมอนาคตหรืออดีตอะไรไป ใช่ว่านายจะเปลี่ยนแปลงอะไรอย่างนั้นได้สักหน่อย"

# "I wanted to say something to her, but I have lost my voice so I just mumble something unintelligible at her."
"ฉันอยากจะพูดอะไรเพื่อตัวเธอบ้าง แต่เสียงฉันไม่มีแล้ว ฉันจึงได้แต่พึมพำอะไรบางอย่างที่จับใจความไม่ได้ออกไป"

# rin "You should just be with me now."
rin "ตอนนี้นายต้องอยู่กับฉันเท่านั้น"

# "Maybe she understood what I wanted to say even if I didn't."
"บางทีเธอคงจะเข้าใจในสิ่งที่ฉันอยากบอก ต่อให้ฉันจะไม่ได้บอกก็ตาม"

# rin "Come here."
rin "มานี่"

# hi "I am here."
hi "ฉันก็อยู่นี่"

scene evh rin_h_normal
with charachange

# rin "Come closer."
rin "มาใกล้ ๆ"

# "My entire body is thinking only in positives now so I do, hugging her more tightly."
"ความคิดที่มองไปข้างหน้าอยู่เต็มทั่วตัวฉัน ฉันจึงเข้าไปกอดเธอเอาไว้แน่น ๆ"

scene evh rin_h_right
with charachange

# rin "Closer."
rin "ใกล้อีก"

# "I press my lower body against hers."
"ฉันแนบร่างกายท่อนล่างเข้ากับเธอ"

# "She tenses a little. Just a little."
"เธอเกร็งเล็กน้อย แค่เล็กน้อยเท่านั้น"

scene evh rin_h_closed_close
with characlose

# rin "Closer."
rin "ใกล้อีก"

# "Her final plead is more like a prayer."
"คำร้องขอสุดท้ายของเธอนั้นคล้ายคำวิงวอนมากกว่า"

# "There is only one way to be any closer than this."
"มีทางเดียวที่จะเข้าใกล้ให้มากกว่านี้"

# "I reach down between us and guide myself, sinking myself into her."
"ฉันย้ายมือไปยังร่างกายท่อนล่างเพื่อนำทางตัวเอง ก่อนจะแนบชิดเข้าไปข้างในตัวเธอ"

scene evh rin_h_strain_close
with charachange

# "Every muscle in Rin's body stiffens at the same time."
"กล้ามเนื้อทั้งตัวเธอเกร็งขึ้นมาพร้อม ๆ กัน"

scene evh rin_h_strain
with charadistant

# "She doesn't say anything, or wince, so I push deeper, eventually moving out."
"เธอไม่พูดอะไร ไม่มีอาการผงะ ฉันจึงเข้าไปให้ลึกขึ้นก่อนจะขยับออกมา"

# "And again. And she moves with me."
"และเข้าไปอีกครั้ง และเธอก็ขยับตามฉัน"

# "Our movements melt together into one continuous string of back and forth, in and out."
"การเคลื่อนไหวของเราหลอมรวมเป็นสายความต่อเนื่องหนึ่งที่ร้อยการขยับเข้าและออกเข้าด้วยกัน"

# "All sensations become sharper, amplified tenfold."
"ทุกสัมผัสรู้สึกได้อย่างชัดเจน ทวีขึ้นเป็นสิบเท่า"

# "My brain gave up interpreting all this stimulation ages ago, and now I am left with no choice but to feel all of this with my entire body."
"สมองฉันละทิ้งการตีความสัญญาณกระตุ้นเหล่านั้นไปนานมากแล้ว ฉันจึงต้องสัมผัสความรู้สึกทั้งหมดเหล่านี้ด้วย\nทั้งกายของฉัน"

# "It's like that for Rin too, I know it. I can see it. I can feel it."
"รินก็เป็นอย่างนั้นเหมือนกัน ฉันรู้ ฉันดูออก ฉันสัมผัสได้"

# "She breathes sharply in and out, losing all composure and grace, breathes warmly against my shoulder."
"เธอคุมตัวเองไม่อยู่แล้ว ทั้งยังหอบแรงจนดูไม่เรียบร้อย ลมหายใจอุ่น ๆ นั้นรดหัวไหล่ฉัน"

# "Between those fragile breaths, she sometimes kisses me tenderly, gently, as if she was unsure how to do it properly."
"ช่วงระหว่างจังหวะการหายใจอันเปราะบางของเธอนั้นบางทีรินก็จูบฉันอย่างอ่อนโยนและแผ่วเบาคล้ายไม่รู้จะต้อง\nทำยังไงดี"

# "But there is no hesitation."
"แต่จะมามัวชะงักไม่ได้แล้ว"

# "Desperately clinging to me, drawing me closer so that I can fill all of her, she moves against me, around me so that it's hard to say where I stop and she begins."
"เธอพยายามเหนี่ยวรั้งฉันเอาไว้ให้ฉันได้เข้าใกล้เพื่อเติมเต็มตัวเธอให้เต็มที่ เธอเกี่ยวตัวฉันและขยับเข้าหาฉันจน\nยากจะแยกว่าส่วนไหนเป็นฉันหรือเธอ"

# "We take it slowly, excruciatingly slowly, as if we had all the time in the world even though we have only this moment and nothing beyond that."
"พวกเราทำไปอย่างช้า ๆ ช้าจนทรมาน ราวกับว่าเรามีเวลาเหลือมากมาย ถึงแม้เวลาที่เรามีอยู่จะมีเพียงแค่ขณะนี้\nเพียงเท่านั้น"

# "That feeling is—{w=0.7}{nw}"
"รู้สึกราวกับ—{w=0.7}{nw}"

scene evh rin_h_normal_close
with characlose

# rin "Wait…"
rin "เดี๋ยว…"

# "I stop moving, slightly alarmed."
"ฉันหยุดด้วยความตกใจเล็กน้อย"

# "Maybe it hurts, or…"
"เจ็บเหรอ หรือว่า…"

scene evh rin_h_right_close
with charachange

# "She looks at me in a way that I can't really begin to interpret."
"เธอมองฉันด้วยสายตาที่ฉันไม่อาจตีความได้"

# rin "Is this it?"
rin "นี่น่ะเหรอ"

# hi "…Huh?"
hi "…หืม?"

# rin "You said I don't have to be alone."
rin "นายบอกว่าฉันไม่จำเป็นต้องอยู่ตัวคนเดียว"

scene evh rin_h_left_close
with charachange

# "Her eyes are full of an innocent, fuzzyheaded confusion that makes me chuckle a little and pet the back of her head."
"สายตาเธอช่างใสซื่อและสับสนงุนงง ฉันแค่นหัวเราะแล้วลูบ ๆ ท้ายทอยเธอ"

# hi "Yeah. This is what I meant."
hi "อื้ม ฉันหมายความอย่างนี้แหละ"

# hi "That you have someone you can come to when you get soaked in a rain."
hi "ว่าเธอจะมีคนนั้นที่มาหาในวันที่เธอเปียกฝนได้"

# hi "It means you are not alone."
hi "หมายความว่าเธอไม่ได้อยู่ตัวคนเดียว"

# hi "If there is such a person for you."
hi "ถ้าเธอมีคนอย่างนั้น"

scene evh rin_h_closed_close
with charachange

# "She answers with a kiss, reminding me that we have stopped moving for no real reason."
"เธอตอบด้วยจูบจนฉันนึกได้ว่าพวกเราหยุดขยับกันไปโดยไม่มีเหตุผลอะไร"

# "So we start from the top, almost at the same time, each mirroring the rhythm of the other."
"พวกเราจึงเริ่มกันใหม่แทบจะพร้อม ๆ กันและลอกเลียนประสานจังหวะของกันและกัน"

# "I move faster, faster in and out of her, my sweat mixing with hers, glistening on our shared skin like diamonds and pearls."
"ฉันขยับเข้าออกตัวเธอให้เร็วขึ้น เหงื่อของฉันปนกับเหงื่อของเธอ เม็ดเหงื่อเหล่านั้นวาวแสงอย่างเพชรและไข่มุกอยู่บน\nตัวฉันและเธอที่กลืนเป็นเนื้อเดียวกัน"

scene evh rin_h_strain:
    truecenter
    zoom 1.2 subpixel True
    easein 20.0 zoom 1.0
with charadistant

# "She moves faster, grinding herself against me in the throes of our desire."
"เธอขยับเร็วขึ้นพลางบดคลึงตัวเธอเข้ากับตัวฉัน พวกเราต่างถูกความปรารถนารุนแรงกลืนกิน"

# "The intoxicating scent of her lust, the mind-blanking feeling that connects our bodies, the sense of all rational thought draining from my mind."
"กลิ่นราคะของเธอที่ชวนให้มึนเมา ความรู้สึกที่ทำให้สมองว่างเปล่าที่เชื่อมต่อร่างกายเรา ความคิดตรรกะทั้งหลายที่ไหล\nออกไปจากสมองฉัน"

# "All those burn my consciousness just like the compelling feeling in my body burns my instincts."
"เหล่านั้นแผดเผาสำนึกฉันเหมือนอย่างที่ความรู้สึกที่ไม่อาจต้านทานในตัวแผดเผาสัญชาตญาณฉัน"

# "As those feelings grow, Rin makes no signs of stopping."
"ความรู้สึกเหล่านั้นรุนแรงขึ้นเรื่อย ๆ ส่วนรินก็ไม่มีท่าทีว่าจะหยุด"

# "She curls her feet behind my lower back, forcing me to drive myself inside her as deep as physically possible, each millimeter sending waves through my spine."
"นิ้วเท้าเธอที่งออยู่ที่หลังส่วนล่างของฉันบังคับให้ฉันต้องดันตัวเองเข้าไปในเธอให้ลึกที่สุดเท่าที่จะทำได้ ทุก ๆ ระยะ\nเพียงเล็กน้อยที่เข้าไปทำเอาฉันเสียวซ่านขึ้นทุกที"

# "My mind blacks out as the world erupts into a flash of bright white blindness."
"สมองฉันดับลง ภาพตรงหน้ามีเพียงสีขาวโพลนที่สว่างจ้าขึ้นมาจนตาพร่า"

stop music fadeout 2.0
stop ambient fadeout 2.0

window hide

scene white
with Dissolve(2.0)

$ suppress_window_after_timeskip = True

with Pause(4.0)


label th_R42:

window hide None

scene white
with None

$ renpy.music.set_volume(0.1, 0.0, channel="music")
play music music_timeskip fadein 4.0

# centered_b "Present{fast}" with Dissolve(4.0)
centered_b "ปัจจุบัน{fast}" with Dissolve(4.0)


# nb "“Present” is a fleeting and vague concept at best.\n"
nb "“ปัจจุบัน” เป็นคำที่ไม่มีความจีรังและยังคลุมเครือ\n"

# extend "The moment between the past and the future?\n"
extend "ช่วงระหว่างอดีตและอนาคต?\n"

# extend "That doesn't really mean anything.\n"
extend "ก็ไม่ได้มีความหมายอะไรเท่าไหร่\n"

# extend "Thinking too much about things that don't make sense is a waste of time.\n"
extend "คิดอะไรที่ไม่สมเหตุสมผลมากไปก็เสียเวลาเปล่า\n"

# extend "That's why living through the present is always the best option.\n"
extend "เพราะฉะนั้น การใช้ชีวิตอยู่กับปัจจุบันจึงเป็นตัวเลือกที่ดีที่สุด\n"

# extend "Besides, for us who can't foresee the future and who forget the past too easily, present is really the only proof of our existence.\n"
extend "อีกอย่าง สำหรับพวกเราที่ไม่อาจทำนายอนาคตหรือลืมอดีตได้อย่างง่ายดายแล้ว ปัจจุบันเป็นเพียงสิ่งเดียวที่เป็น\nหลักฐานถึงตัวตนของพวกเรา\n"

# extend "Even though existence will go on even if you forget about it for a while, it's good to seize the day at least every once in a while.\n"
extend "ต่อให้ตัวตนยังคงอยู่แม้จะลืมไปสักพักหนึ่ง นาน ๆ ทีลุกมาทำวันนี้ให้ดีที่สุดก็ยังดี\n"

#this is so that the text appears properly
# centered_alive "That way… you can confirm that you are, in fact…"
centered_alive "เพราะเช่นนั้นแล้ว… เราจะได้แน่ใจว่าพวกเรานั้น จริง ๆ แล้ว…"

#this is so that the text stays after being dismissed
# show alivetext "That way… you can confirm that you are, in fact…"
show alivetext "เพราะเช่นนั้นแล้ว… เราจะได้แน่ใจว่าพวกเรานั้น จริง ๆ แล้ว…"
with None

#and this is so that the "alive" fades in properly. Damn I hate Ren'Py sometimes.
# show alivetext "That way… you can confirm that you are, in fact… alive."
show alivetext "เพราะเช่นนั้นแล้ว… เราจะได้แน่ใจว่าพวกเรานั้น จริง ๆ แล้ว… ยังมีชีวิตอยู่"
with Dissolve(3.0)

$ renpy.pause()

stop music fadeout 4.0

scene bg school_dormhisao
with Dissolve(4.0)

window show Dissolve(2.0)

$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_dreamy fadein 4.0

# "I am pretty sure that the girl who is standing there half-naked, staring out of the window of my room, has a much better grasp of “present” than I do."
"ฉันค่อนข้างมั่นใจว่าสาวที่ยืนกึ่งเปลือยมองหน้าต่างห้องฉันอยู่ตรงนั้นเข้าใจ “ปัจจุบัน” ได้ดีกว่าฉันเสียอีก"

# "As for me… well, right now I'm somewhat confused by my present state, since I should try to locate my shirt and not stare at Rin's butt."
"ส่วนฉัน… อืม ตอนนี้ฉันค่อนข้างสับสนกับสภาพปัจจุบันของตัวเองอยู่ เพราะฉันต้องตามหาเสื้อฉัน ไม่ใช่มาจ้อง\nก้นรินอยู่อย่างนี้"

# "But I just can't stop looking at her."
"แต่ฉันละสายตาไปจากเธอไม่ได้เลย"

scene bg misc_sky
show hisaowindow
show rinpan relaxed_nonchalant_close at center
with locationchange

# "She is so close to the glass that her nose is probably going to leave a mark."
"เธอยืนอยู่ชิดหน้าต่างจนเหมือนหน้าต่างจะเป็นรอยจมูกเธอไปด้วย"

# "At least her breathing does, when it condenses on the rain-cooled window glass before quickly disappearing again."
"แต่ลมหายใจเธอเป็นรอยอยู่ เป็นรอยไอน้ำที่ควบแน่นอยู่บนแผ่นกระจกที่เย็นด้วยน้ำฝน รอยนั้นอยู่ไม่นานก็หายไป"

# "My shuffling around to get dressed doesn't rouse Rin from her contemplation, which is fine, really. I don't mind the silences as much as I used to."
"เสียงสวบสาบจากฉันที่เปลี่ยนเสื้อผ้าอยู่ไม่ได้ทำให้รินหลุดจากภวังค์ความคิดของเธอ ซึ่งจริง ๆ ก็ไม่ได้อะไรหรอก\nฉันก็ชินกับความเงียบไปแล้วละ"

# "Only after I'm almost finished with buttoning up my shirt does Rin say something, still without turning to look at me."
"กว่าฉันจะติดกระดุมใกล้เสร็จนั่นแหละรินถึงได้พูดอะไรขึ้นมา แต่เธอยังไม่หันมามองฉัน"

show rinpan relaxed_boredom_close
with charachange

# rin "Let's go somewhere."
rin "ไปสักที่กันเถอะ"

# hi "Where?"
hi "ไปไหน"

# "I can only assume she is inviting me and not the windowsill, but it's a fair guess."
"เดา ๆ แล้วก็คงจะชวนฉันแหละ ไม่ได้ชวนขอบหน้าต่างหรอก"

show rinpan basic_lucid_close
with charachange

# rin "I know."
rin "รู้"

# hi "What?"
hi "ฮะ?"

show rinpan basic_deadpan_close
with charachange

# rin "Help me get dressed."
rin "ช่วยฉันใส่เสื้อผ้าหน่อย"

show rinpan basic_awayabsent_close
with charachange

# rin "I think today is the day."
rin "ฉันคิดว่าวันนี้คือวันสำคัญ"

show rinpan basic_deadpanupset_close
with charachange

# rin "Come on, clothes."
rin "เร็ว เสื้อผ้า"

# "Clothes, clothes… what an impatient tone."
"เสื้อผ้า เสื้อผ้า… น้ำเสียงฟังดูรีบ ๆ แฮะ"

# "I crouch down to pick up her bra from the floor where it had fallen, discarded in the haste of undressing and forgotten there."
"ฉันย่อตัวลงเก็บยกทรงที่ตกอยู่กับพื้นที่ถูกทิ้งให้ลืมด้วยความรีบถอดตอนนั้น"

# "Hanging it from between my fingers like a dead fish, the same hesitation that grasped me when I was undressing Rin is creeping inside my head again."
"ฉันใช้นิ้วเกี่ยวขึ้นมาเหมือนปลายตาย อยู่ ๆ ก็นึกลังเลขึ้นมาเหมือนอย่างเมื่อตอนนั้น ตอนที่ฉันกำลังถอดเสื้อผ้ารินอยู่"

# "Is intimacy really something this difficult for me to handle?"
"ทำอะไรใกล้ชิดมันยากสำหรับฉันขนาดนี้เลยเหรอ"

show rinpan basic_deadpancontemplation_close
with charachange

# rin "Come on, you got it off just fine. This is the same but the other way around. It's like talking backwards."
rin "เร็ว ตอนถอดนายยังถอดได้ ตอนใส่ก็เหมือนกันแหละ แค่กลับด้าน เหมือนพูดกลับด้าน"

show rinpan basic_deadpan_close
with charachange

# rin "Ysae s'ti tub, drah smees."
rin "เดียวนิดง่ายแต่ นะยากดู"

# "Perplexed by her sudden and prodigious display of mental processing capacity, I forget to attempt reversing her gibberish back."
"ฉันมัวแต่ทึ่งกับสมองเธอที่ประมวลผลได้อย่างรวดเร็วและฉลาดล้ำจนลืมกลับคำพูดเพี้ยน ๆ ของเธอให้เป็นข้อความปกติ"

# "I'm pretty sure I couldn't switch to talking backwards that fluidly even with some practice."
"ฉันค่อนข้างมั่นใจว่าต่อให้ฉันฝึกมาก็พูดกลับด้านได้ไม่คล่องขนาดนั้นแน่ ๆ"

# hi "Umm, could you repeat that?"
hi "เอ่ออ ขออีกที?"

show rinpan basic_lucid_close
with charachange

# rin "Ysae s'ti tub, drah smees."
rin "เดียวนิดง่ายแต่ นะยากดู"

"…"

# hi "Got it. Fine, I'll give it a try."
hi "โอเค ได้ เดี๋ยวลองดู"

# "Rin was right, the locking mechanism is simple enough, and I get the little plastic hooks right on the third attempt."
"รินพูดถูก ตัวคล้องไม่ได้ซับซ้อนมาก ลองดูแค่สามรอบก็คล้องขอเกี่ยวพลาสติกอันเล็ก ๆ เข้าได้แล้ว"

# hi "There."
hi "เอ้า"

show rinpan basic_deadpandelight_close
with charachange

# rin "Ti tsujda ot evah uoy won."
rin "ปรับต้องก็นายนี้ทีแล้ว"

# hi "What? Please stop that, I don't speak backwardese."
hi "ฮะ? พอก่อนได้มั้ย ฉันไม่ได้พูดภาษากลับด้านนะ"

show rinpan basic_lucid_close
with charachange

# "She shakes her head as if needing to banish the backwards way of thinking with a physical gesture."
"เธอสั่นหัวคล้ายจะทำท่าให้วิธีคิดแบบกลับด้านออกจากหัวไป"

# "I know a few people who could benefit from that kind of ability."
"ฉันพอจะรู้จักคนที่น่าจะเอาทักษะภาษากลับด้านไปใช้ประโยชน์ได้"

show rinpan relaxed_nonchalant_close
with charachange

# rin "I got stuck. Now you have to adjust it."
rin "มันติด แล้วทีนี้นายก็ต้องปรับ"

# hi "Adjust?"
hi "ปรับ?"

show rinpan basic_deadpan_close
with charachange

# rin "That's what I said."
rin "ตามนั้น"

# hi "No, I asked what you meant."
hi "ไม่ ฉันถามเธอว่าหมายความว่ายังไง"

show rinpan basic_lucid_close
with charachange

# rin "You know, so that they are… fine."
rin "ก็เนี่ย ปรับให้มัน… เข้าที่"

# "Oh. Fine, you say?"
"อ้อ เข้าที่เหรอ"

"…"

# "As I have no idea when her breasts are supposed to be “fine,” I end up fumbling around her chest for a good while without really getting anywhere."
"เพราะฉันไม่รู้ว่า “เข้าที่” ของหน้าอกรินคืออะไร ฉันจึงได้แต่จับ ๆ คลำ ๆ อยู่ตามหน้าอกรินอยู่พักใหญ่โดยที่ไม่ได้อะไร\nขึ้นมาเท่าไหร่"

# "Not that I would complain, but Rin does."
"ซึ่งฉันก็ว่าไม่ได้หรอก แต่รินว่า"

show rinpan basic_deadpanupset_close
with charachange

# rin "Emi is better than you at this."
rin "เอมิทำเก่งกว่านายอีก"

# "Her impatient tone ticks me off, even though I can't really disagree. Rin suddenly seems to be in an awful hurry."
"น้ำเสียงเร่งของเธอทำฉันหงุดหงิด ถึงจะเถียงไม่ออกก็เถอะ อยู่ ๆ รินก็ดูจะรีบขึ้นมาเสียอย่างนั้น"

# hi "Yeah well excuse me, could that be because she is a {b}girl{/b} and can actually relate?"
hi "เออ ๆ ขอโทษที เธอว่าเพราะเอมิเป็น{b}ผู้หญิง{/b}หรือเปล่าเลยรู้ว่าแบบไหนเข้าที่"

show rinpan basic_deadpanamused_close
with charachange

# rin "I don't think so, she has just about as much chest as you do."
rin "ฉันไม่คิดว่าอย่างนั้นนะ หน้าอกเอมิก็มีพอ ๆ กับหน้าอกนาย"

"…"

stop music fadeout 5.0

hide rinpan
show rin basic_absent_close
with shorttimeskip

# "With her bra and breasts eventually “fine” as they should, the rest of her clothes are considerably easier to put on."
"เมื่อยกทรงนั้น “เข้าที่” อย่างที่ควรจะเป็นแล้ว เสื้อผ้าชิ้นที่เหลือก็ใส่ให้ได้ง่ายหน่อย"

hide rin
with charaexit

# "Rin launches towards the door even though her shirt is not even buttoned up all the way yet."
"รินพุ่งตัวไปที่ประตูทั้ง ๆ ที่เสื้อยังไม่ได้ติดกระดุมครบทุกเม็ด"

# "Left with little choice, I run after her."
"เมื่อไม่มีทางเลือกอื่นมากฉันจึงรีบตามเธอไป"

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_soothing fadein 2.0
play ambient sfx_parkambience fadein 0.5

scene bg school_gardens
with locationskip

# "As soon as I realize that we are heading for the side entrance leading to the forest, I think I know where Rin wanted to go, although I couldn't say why she'd want to go there."
"ทันทีที่รู้ว่ากำลังจะไปที่ประตูที่อยู่ปากทางเข้าป่าฉันก็พอจะรู้ทันทีว่ารินอยากไปที่ไหน ถึงจะไม่รู้ว่าทำไมถึงอยากไป\nก็เถอะ"

# "Then again, I can't really assume my guesses to be anywhere near correct when Rin is concerned, not even for a quite generous definition of “correct.”"
"แต่ก็นะ ถ้ามีรินเข้ามาเกี่ยวข้องแล้วฉันก็เดาอะไรให้ถูกไม่ได้เลยหรอก ต่อให้จะอะลุ่มอล่วยเอาคำว่า “ถูก” ให้ตีความไป\nได้กว้างแค่ไหนก็ตาม"

$ renpy.music.set_volume(0.6, 0.5, channel="ambient")
$ renpy.music.set_volume(0.8, 0.5, channel="music")

scene bg school_forest1
with locationskip

# "The forest behind the walls smells of rain, the last raindrops are still dripping from the wet undergrowth into the earth despite the rain being gone for a while already."
"ป่าที่อยู่เบื้องหลังกำแพงนั้นอวลไปด้วยกลิ่นฝน ถึงแม้ฝนจะหยุดไปสักพักแล้วก็ยังเหลือน้ำฝนหยดสุดท้ายให้หยดจาก\nพืชพื้นป่าลงสู่ดิน"

# "We stroll along with an unhurried pace that Rin sets, giving me time to take in the calming atmosphere."
"พวกเราเดินไปด้วยฝีเท้าที่ไม่รีบเร่งของริน พอจะมีเวลาให้ฉันได้ดื่มด่ำไปกับบรรยากาศอันเงียบสงบบ้าง"

# "I think I can hear Rin saying hello to at least three different trees while she walks past them, but I ignore it, just like the trees do."
"เหมือนจะได้ยินรินทักทายต้นไม้อย่างน้อยก็สักสามต้นตอนที่เดินผ่านแต่ละต้น แต่ฉันก็เมินเหมือนอย่างที่ต้นไม้เหล่านั้น\nเมิน"

# "She leads me to the narrow side path leading up to the hilltops, as I guessed."
"ตามคาด เธอเดินนำมาที่ทางแคบ ๆ ที่ทอดขึ้นไปยังยอดเขา"

scene bg worrytree:
   truecenter
   yalign 1.0
with locationchange

# "I peek through the canopy trying to find a rainbow, but there doesn't seem to be one."
"ฉันส่องผ่านหลังคาป่าดูเผื่อว่าจะมีสายรุ้ง แต่ก็เหมือนว่าจะไม่มี"

# "It's perfect weather for rainbows. The sun is shining low, and rain has passed not too long ago."
"เป็นอากาศที่เหมาะแก่การเกิดสายรุ้งทีเดียว พระอาทิตย์ก็คล้อยต่ำ ฝนก็เพิ่งหยุดตกไป"

# "Well, whatever."
"แต่เอาเหอะ"

$ renpy.music.set_volume(0.7, 0.5, channel="ambient")
$ renpy.music.set_volume(0.6, 0.5, channel="music")

scene bg school_forest2
with locationchange

# "I lower my eyes from the treetops to see the gaunt back of the girl who is climbing up the hill slowly, without losing her balance."
"พอละสายตาจากด้านบนลงมาก็เห็นแผ่นหลังซูบ ๆ ของสาวที่กำลังรักษาสมดุลเดินขึ้นเขาไปอย่างช้า ๆ อยู่"

# "A few steps ahead of me on the path, but still within my reach."
"อยู่ห่างไปไม่กี่ก้าว แต่ยังเอื้อมถึง"

# "I don't think I ever could reach a rainbow, but reaching Rin… it seems less impossible than it used to seem."
"ฉันคงไม่มีวันเอื้อมถึงสายรุ้ง แต่เอื้อมให้ถึงริน… ดูจะเป็นไปได้ขึ้นมากว่าที่ฉันเคยคิด"

$ renpy.music.set_volume(1.0, 0.5, channel="ambient")
$ renpy.music.set_volume(0.4, 0.5, channel="music")

scene bg school_hilltop_border_summer
with locationchange

# "The clear sky greeting us from above the meadow clearing seems vast and beautiful."
"ท้องฟ้าโปร่งทักทายพวกเราอยู่บนทุ่งหญ้าบนยอดเขาอันสวยงามและกว้างไกล"

# "A strong wind is herding the rainclouds away from the town, to the other side of the mountains in the distance."
"ลมแรงพัดให้เมฆฝนเลื่อนพ้นจากเมืองไปยังภูเขาอีกฟากที่เห็นอยู่ลิบ ๆ"

# "The sight is pretty, but…"
"เป็นทิวทัศน์ที่สวยดี แต่…"

"…"

stop music fadeout 6.0

show dandelionsbg thin
show dandelionsfg thin
with None

# "A speck of white flies past the edge my peripheral vision, but when I turn to look, it's already gone."
"จุดสีขาว ๆ ลอยผ่านอยู่แถว ๆ หางตาฉันออกไป แต่เมื่อหันไปมองก็ไม่มีอีกแล้ว"

# "Another follows, then a third."
"อีกจุดตามมา และจุดที่สามก็ตามมา"

# "Before I realize it, dozens of almost invisible small tufts of white are flying all around us."
"รู้ตัวอีกทีพวกเราก็ถูกรายล้อมไปด้วยกลุ่มเส้นเล็ก ๆ ที่แทบมองไม่เห็นหลายสิบเส้นที่ลอยอยู่"

show rin basic_delight behind dandelionsfg at center
with charaenter

# rin "Look, the flowers."
rin "ดูสิ ดอกไม้"

# "Ah. I see it now."
"อา เข้าใจแล้ว"

$ renpy.music.set_volume(1.5, 0.5, channel="ambient")
$ renpy.music.set_volume(1.0, 0.0, channel="music")

scene bg school_hilltop_summer
show dandelionsbg dense
show dandelionsfg dense
with locationchange

play music music_comfort fadein 0.5

# "The sea of dandelions that covered the hilltop on our last visit has changed over the days."
"วันคืนผันแปรให้ทะเลดอกแดนดิไลออนที่พวกเรามาดูครั้งก่อนบนยอดเขานี้นั้นเปลี่ยนไป"

# "Where there was bright yellow before, there is now fluffy white."
"จากที่เคยเป็นสีเหลืองอร่าม ตอนนี้กลายมาเป็นสีขาวฟูฟ่อง"

# "Some of the flowers have already shed their seeds, but many are still waiting for a suitable gust of wind."
"บางดอกก็สลัดเมล็ดของตัวเองไปแล้ว แต่ก็ยังมีอีกหลายดอกที่กำลังคอยจังหวะลมพัดที่เหมาะสม"

# "Today those gusts are not in short demand, every now and then they shake the grass thoroughly, and suddenly the air is thick with dandelion seeds."
"วันนี้ลมที่ว่านั้นพัดมาไม่ขาดสาย บางครั้งก็จะพัดวูบจนต้นหญ้านั้นสั่นไหว และในอากาศก็จะถูกเติมเต็มด้วยเหล่า\nเมล็ดแดนดีไลออน"

# "One by one, the seeds separate from the flower heads and are lifted away."
"เมล็ดนั้นแยกตัวออกจากเกสรทีละเมล็ดก่อนจะถูกพัดพาไป"

# "A commonplace event, but one that seems to fascinate Rin for some reason."
"เป็นภาพที่หาชมได้ไม่ยาก แต่เป็นภาพที่ดูเหมือนจะดึงดูดริน"

$ renpy.music.set_volume(1.0, 0.5, channel="ambient")

show rin negative_spaciness behind dandelionsfg at center
with charaenter

# "She's turning her head from side to side, marveling at the change happening all around her as the seeds fly away."
"เธอหันซ้ายหันขวาด้วยความตื่นตะลึงกับการเปลี่ยนแปลงรอบตัวเธอโดยมีเหล่าเมล็ดที่ปลิดปลิวล้อมรอบ"

# "I watch them too, following the white tufts floating with the wind towards the horizon, and imagine that I can see them even after they disappear from my sight."
"ฉันก็มองด้วยเหมือนกัน สายตาฉันมองตามกลุ่มเส้นสีขาวนั้นที่ถูกลมพัดพาไปยังเส้นขอบฟ้า แม้จะลับตาไปแล้ว\nฉันก็จินตนาการเอาว่ายังคงมองเห็นอยู่"

"…"

show rin basic_awayabsent
with charachange

# rin "Hisao."
rin "ฮิซาโอะ"

# hi "What is it?"
hi "มีอะไรเหรอ"

show rin basic_absent
with charachange

# rin "Do you love me?"
rin "นายรักฉันมั้ย"

# "I snap to attention, to meet her suddenly very serious face that is not looking only at the flowers any more."
"ฉันหันมาสนใจเธอทันที เธอทำสีหน้าจริงจังมาก ๆ และไม่ได้มองเหล่าดอกไม้แล้วด้วย"

# "What a tough question, asked just like that, out of the blue."
"ตอบยากจัง ถามขึ้นมาลอย ๆ แบบไม่มีปี่มีขลุ่ยเลย"

# "Still, her bluntness compels me to answer rapidly."
"แต่หมัดตรงของเธอทำให้ฉันต้องตอบอย่างรัวเร็ว"

# hi "I don't know. Maybe I do."
hi "ไม่รู้สิ อาจจะมั้ง"

# "Maybe too rapidly."
"อาจจะรัวเร็วไป"

show rin basic_deadpannormal
with charachange

# rin "What does that mean?"
rin "หมายความว่ายังไง"

# hi "…I don't know."
hi "…ไม่รู้สิ"

show rin basic_lucid
with charachange

# "Rin sighs, perhaps unhappy with my wishy-washy answer. I would be too."
"รินถอนหายใจ คงจะไม่พอใจเท่าไหร่ที่ฉันตอบไปแบบใจโลเลอย่างนั้น เป็นฉันก็คงไม่พอใจเหมือนกัน"

show rin relaxed_nonchalant
with charachange

# rin "Me neither."
rin "ฉันก็เหมือนกัน"

show rin relaxed_boredom
with charachange

# rin "I don't think I know much about love."
rin "ฉันไม่คิดว่าฉันรู้เรื่องความรักเท่าไหร่"

hi "…"

# hi "…It's fine, isn't it?"
hi "…ก็ไม่เห็นจะเป็นไรเลยนี่"

show rin basic_lucid
with charachange

# "“How should I know?”, the shrug of her shoulders seems to say, hesitating to give a firmer answer."
"“ฉันจะไปรู้ได้ยังไง” เธอยักไหล่คล้ายจะบอกเช่นนั้นและไม่ได้ตอบอะไรที่ชัดเจนไปกว่านั้น"

# "She stays silent for only a second too long, but even that second isn't long enough for me to think ahead…"
"เธออยู่เงียบ ๆ นานเกินไปหนึ่งวินาที แต่แม้แต่หนึ่งวินาทีนั้นก็ยังไม่พอที่จะให้ฉันคิดคิดอะไรไปไกล…"

show rin basic_absent
with charachange

# rin "I love you."
rin "ฉันรักนาย"

# "Those three words freeze me in place like a rabbit staring into headlights, but I'm not a rabbit and I'm just staring into Rin's eyes that seem far, far too impassive for what she just let out of her mouth."
"สามคำนั้นทำฉันผงะไปไม่ต่างอะไรกับกระต่ายที่กำลังมองไฟหน้ารถยนต์ ต่างก็แต่ที่ฉันไม่ใช่กระต่าย และสิ่งที่ฉัน\nมองอยู่คือตาของรินที่นิ่งมากแบบมาก ๆ ไม่เข้ากับสิ่งที่เพิ่งออกจากปากเธอมาเลย"

show rin basic_deadpanupset
with charachange

# "Rin looks pretty serious though, until she sticks out her tongue, frowns a little and confuses me even more than her words did."
"แต่เธอก็ดูจริงจังทีเดียว ก็จนกระทั่งเธอแลบลิ้นออกมาพลางขมวดคิ้วจนทำฉันงงหนักกว่าการได้ฟังสิ่งที่เธอพูดเสียอีก"

# "Why does she look mildly unhappy?"
"ทำไมเธอถึงดูไม่มีความสุขหน่อย ๆ นะ"

# "Was it a confession of her deepest feelings, a test to see how I would react, a test to see how she would react?"
"เป็นการสารภาพความรู้สึกในใจเบื้องลึกของเธอเหรอ เป็นแบบทดสอบเพื่อดูว่าฉันจะตอบสนองยังไงเหรอ เป็น\nแบบทดสอบเพื่อดูว่าเธอจะตอบสนองยังไงเหรอ"

show rin basic_awayabsent
with charachange

# rin "It tastes weird."
rin "รสชาติแปลก ๆ"

# hi "…Tastes?"
hi "…รสชาติ?"

show rin basic_lucid
with charachange

# rin "Yeah. So weird."
rin "อืม แปลกมาก"

# "She laughs, maybe nervously or so I want to think, but stops midway when she notices how strange it sounds."
"เธอหัวเราะด้วยความอาย ๆ หรืออะไรสักอย่าง—หวังว่าจะเพราะอย่างนั้นนะ—แต่เธอก็หยุดกลางคันไปเมื่อเห็นว่าเสียง\nฟังดูแปร่ง ๆ"

show rin negative_spaciness
with charachange

# rin "Like… I don't know what, I… don't think there is a word for this."
rin "แบบ… ฉัันไม่รู้ ฉัน… คิดว่าไม่มีคำเรียกสิ่งนี้นะ"

# "Rin keeps on talking as though there was no meaning behind her words, steady and careless words dropping from the same tongue that formed the more important ones."
"รินยังคงพูดต่อไปราวกับว่าคำพูดที่เธอพูดนั้นไม่ได้มีความหมายอะไรอยู่เบื้องหลัง คำพูดที่ไม่ได้มีการกลั่นกรองไหล\nออกมาเรื่อย ๆ จากลิ้นที่เคยสร้างคำพูดที่สำคัญ ๆ นั้น"

show rin negative_worried
with charachange

# rin "A word for… ummm…"
rin "คำที่เอาไว้เรียก… อืมมม…"

# "Except."
"แต่"

show rin negative_annoyed
with charachange

# rin "…it's like…"
rin "…มันเหมือน…"

# "She can't."
"เธอ"

show rin basic_deadpanupset
with charachange

rin "…"

# "Find the words."
"หาคำนั้นไม่เจอ"

show rin basic_sad
with charachange

rin "…"

# "Rin just keeps staring at me, stumbling with her words as if her brain suddenly ground to a halt."
"รินเอาแต่จ้องฉันนึกลำบากใจกับคำพูดราวกับว่าจู่ ๆ สมองเธอก็หยุดทำงานไป"

# "She looks awfully confused, much like how I feel right now as I wait for her to explain."
"เธอดูสับสนหนักไม่ต่างจากฉันที่กำลังรอเธอให้อธิบาย"

# "But she doesn't, she just blinks a few times, the flutter of her long lashes catching my fancy because she looks like she is petrified otherwise."
"แต่เธอก็ไม่อธิบาย เธอเพียงกะพริบตาสองสามครั้ง ขนตายาว ๆ ที่กระพือนั้นทำให้ฉันจับสังเกตเธอ เพราะทั้งตัวเธอ\nนิ่งค้างไป"

# "Until I realize what they were fighting against."
"และฉันก็ได้รู้ว่าตาที่กะพริบนั้นกำลังฝืนอะไรอยู่"

show rin basic_crying
with charachange

# "It's those weird tears again, not associated with sadness or happiness, not pitiable sobbing nor laughter of joy."
"เป็นน้ำตาแปลก ๆ เหล่านั้นอีกแล้ว ที่ไม่ได้เกี่ยวกับความเศร้าหรือความสุข ไม่ได้ร้องไห้น่าสงสารหรือหัวเราะด้วย\nความยินดี"

# "Just tears, spontaneously and without a warning, like that one time in her classroom."
"แค่น้ำตาที่ไหลออกมาโดยไม่บอกกล่าว เหมือนตอนนั้นที่อยู่ในห้องเรียนของเธอ"

# rin "Ah."
rin "อ๊ะ"

# "Just a few of them, not enough to make a fuss about, so Rin doesn't make a move to hide them even after noticing."
"มีเพียงไม่กี่หยด ไม่ได้มากมายที่จะทำให้วุ่นวายอะไร รินจึงไม่ได้ซ่อนน้ำตานั้นแม้เธอจะรู้สึกตัวแล้วก็ตาม"

# "Rin cries, looking like she has no idea why, and somehow a great uneasiness grows in my chest when I look into her watery eyes that stare right back at me."
"รินร้องไห้ ท่าทางเธอดูเหมือนจะไม่รู้ว่าร้องไห้เพราะอะไร และเมื่อได้มองน้ำตาเธอที่รื้นขึ้นมาในดวงตาที่จ้องมองฉันแล้ว\nฉันก็รู้สึกอึดอัดในอกเหลือเกิน"

# "It petrifies me too, the shock of the incomprehensibility of this situation."
"ฉันก็นิ่งค้างไปเหมือนกันเพราะตกใจและไม่เข้าใจสถานการณ์ตรงหน้านี้"

# "I just don't know what is happening any more."
"ฉันไม่รู้แล้วว่าเกิดอะไรขึ้นกันแน่"

# hi "Rin? What's wrong?"
hi "ริน? เป็นอะไร?"

# rin "I…"
rin "ฉัน…"

show rin negative_crying
with charachange

# "She shakes her head in confusion, stumbling to get the words out of her mouth."
"เธอส่ายหัวด้วยความสับสน คำพูดออกจากปากเธอมาอย่างตะกุกตะกัก"

show rin basic_crying
with charachange

# rin "Sorry…"
rin "ขอโทษ…"

# rin "I might be a little afraid of you."
rin "ฉันคงกลัวนายหน่อย ๆ"

# "The words are muttered slowly, with a small voice that is as disbelieving of what it's saying as I am."
"คำพูดเหล่านั้นถูกพึมพำออกมาอย่างช้า ๆ แผ่วเบาเหมือนไม่อยากจะเชื่อว่าตัวเองจะถูกส่งออกมาได้ ฉันก็แทบ\nไม่อยากจะเชื่อเหมือนกัน"

# hi "What? Why?"
hi "ฮะ? ทำไม"

show rin basic_sad
with charachange

# rin "I don't know. Saying that just made me feel like that."
rin "ไม่รู้ พอพูดอย่างนั้นแล้วฉันก็รู้สึกอย่างนั้น"

show rin basic_absent
with charachange

# rin "People cry when they are afraid, right?"
rin "คนเราร้องไห้เพราะกลัวใช่มั้ย"

show rin basic_awayabsent
with charachange

# rin "See? I can do it too."
rin "เห็นมั้ย ฉันก็ทำได้"

# "She's averting her gaze now, deliberately not looking at me. It bewilders me, at least as much as what she is saying."
"เธอเสตามองทางอื่นไม่ยอมมองฉัน ฉันงงงัน อย่างน้อยก็งงพอ ๆ กับความงงของสิ่งที่เธอพูด"

show rin negative_annoyed
with charachange

# rin "I… I sometimes, with you, want to run away so badly but I can't move it's like my legs turn into lemon panna cotta pudding and my heart feels like it's going to explode and…"
rin "ฉัน… ฉัน บางทีนะ กับนาย ฉันอยากวิ่งหนีมากแต่ฉันขยับไม่ได้เหมือนขาฉันกลายเป็นพุดดิงพานาค็อตตาเลมอนแล้ว\nใจฉันก็เหมือนจะระเบิดแล้ว…"

show rin negative_sad
with charachange

# "She slumps her shoulders melancholically."
"เธอหย่อนไหล่ลงอย่างห่อเหี่ยว"

# rin "Has a thing like this ever happened to you?"
rin "นายเคยเป็นอย่างนี้มั้ย"

# "…I remember the leaden sky above the frozen forest and the sound of the leafless branches clacking against each other."
"…ฉันยังจำท้องฟ้าสีเงินที่อยู่เหนือป่าอันหนาวเหน็บและเสียงกิ่งไม้ไร้ใบที่กระทบกันได้"

# "It's like a memory from another life."
"เหมือนเป็นความทรงจำจากอีกชาติหนึ่งเลย"

# hi "Yeah. Once."
hi "อืม เคยครั้งหนึ่ง"

# hi "My heart hurt a lot back then, too."
hi "ตอนนั้นใจฉันเจ็บมากด้วย"

show rin basic_surprised
with charachange

# rin "But I thought your thing was not contagious."
rin "แต่ฉันจำได้ว่าของนายไม่ใช่โรคติดต่อ"

# "I shake my head and a tiny, slightly forced smile rises on my lips."
"ฉันส่ายหน้าพลางหยักยิ้มแกน ๆ เล็กน้อย"

# "The other ailment of my heart could very well be contagious and I wouldn't care a bit."
"โรคอื่น ๆ ในใจฉันก็คงจะเป็นโรคติดต่อละนะ ซึ่งฉันไม่สนใจหรอก"

# hi "What are you afraid of? I never thought I was scary."
hi "เธอกลัวอะไรล่ะ ฉันไม่เคยคิดเลยนะว่าฉันน่ากลัว"

show rin negative_confused
with charachange

# "Rin shakes her head desperately, as if knowing that the tangle inside her mind won't be undone with just that."
"รินสั่นหัวแรง ๆ เหมือนรู้ว่าถ้าไม่แรงพอสิ่งที่พันกันยุ่งเหยิงในหัวเธอคงไม่คลายออก"

# rin "You make me feel that I should be someone else than me."
rin "นายทำให้ฉันรู้สึกเหมือนว่าฉันควรจะเป็นคนอื่นที่ไม่ใช่ฉัน"

show rin negative_sad
with charachange

# rin "It's a scary thing."
rin "มันน่ากลัว"

show rin negative_worried
with charachange

# rin "It happens when you are being nice to me. Like yesterday."
rin "จะเป็นก็ตอนที่นายทำตัวแสนดีกับฉัน เหมือนเมื่อวาน"

# rin "I never know what to do at times like that. It's hard."
rin "ฉันไม่รู้ว่าพอเป็นอย่างนั้นแล้วต้องทำยังไง ยาก"

# "Her voice is barely audible, a whispered admission of something that is too embarrassing to even think, not to mention to say aloud."
"เสียงเธอนั้นค่อยจนแทบไม่ได้ยิน เป็นเสียงกระซิบแห่งคำสารภาพที่แค่คิดก็คงอายไม่ไหว ยิ่งพูดออกมาก็คงอายไปใหญ่"

# "Rin has never been one to be embarrassed so she does utter it aloud, only timidly as if by instinct."
"รินเป็นคนไม่เคยอาย เธอจึงเปล่งเสียงพูดออกมา แต่ก็พูดด้วยความกระมิดกระเมี้ยนราวกับว่าเป็นไปโดยสัญชาตญาณ"

show rin basic_upset
with charachange

# rin "But I want to do something. But I don't know if this me can."
rin "แต่ฉันอยากทำอะไรบางอย่าง แต่ฉันไม่รู้ว่าตัวฉันคนนี้ทำได้หรือเปล่า"

# "For a moment, we just stare at each other as if waiting for the other to say something."
"เราจ้องตากันอยู่ครู่หนึ่งราวกับจะรอให้อีกฝ่ายพูดอะไรบางอย่าง"

"…"

hide rin
show rin basic_upset_close as rin2
with characlose

# hi "You are so stupid."
hi "เธอนี่บ๊องจริง ๆ"

hide rin2
show rin relaxed_surprised_superclose at center
with characlose

# "Rin's lips taste salty and scared against mine."
"ริมฝีปากรินนั้นมีรสเค็มและยังกลัว ๆ ที่จะสัมผัสกับริมฝีปากฉัน"

window hide

play sound sfx_heartslow
show heartattack alpha 
with Dissolve (0.1)

hide heartattack
with Dissolve (0.4)

window show

# "As I grasp her into an embrace, I feel my heart thumping in my chest painfully."
"ฉันรู้สึกได้ถึงใจที่เต้นอยู่ในอกจนเสียดขึ้นมาขณะที่ฉันโอบกอดเธอเอาไว้"

window hide

play sound sfx_heartslow
show heartattack alpha 
with Dissolve (0.1)

hide heartattack
with Dissolve (0.4)

$ renpy.music.set_volume(0.5, 1.0, channel="music")
$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

nvl clear
nvl show dissolve

# n "\n\nEven though I am glad that she can say things like that, they make me sad after all."
n "\n\nถึงฉันจะดีใจที่เธอพูดอะไรอย่างนั้นได้ แต่ฉันก็หดหู่กับสิ่งเหล่านั้นเหมือนกัน"

# n "Rin's spirit, her passion, her strength. All those things that I hold dear are the ones I don't want to change."
n "จิตวิญญาณของริน ความหลงใหลของริน ความเข้มแข็งของริน เหล่านั้นที่ฉันทะนุถนอมคือสิ่งที่ฉันไม่อยากเปลี่ยน"

# n "How should I treat them? Where are they headed to? Is that future irrevocably different from mine?"
n "ฉันจะต้องรับมือสิ่งเหล่านั้นยังไง สิ่งเหล่านั้นกำลังมุ่งหน้าไปที่ไหน อนาคตนั้นต่างไปจากอนาคตของฉันอย่างแน่แท้\nหรือเปล่า"

# n "That anxiety will never loose its grip on my heart, but I think I could learn to live with it."
n "ความกังวลนั้นจะคอยเกาะกุมจิตใจฉันอยู่อย่างแน่นหนา แต่ฉันคิดว่าฉันเรียนรู้ที่จะอยู่ร่วมกับมันได้"

# n "Slowly, the pain in my heart dies out, and it settles into the same rhythm as Rin's."
n "อาการเจ็บที่หัวใจฉันค่อย ๆ ทุเลาลงก่อนจะกลับมาเต้นเข้ากับจังหวะหัวใจของริน"

# n "\n\nWe listen to that for some time."
n "\n\nพวกเราฟังเสียงหัวใจเต้นอยู่สักพักหนึ่ง"

n "…"

$ renpy.music.set_volume(1.0, 1.0, channel="music")
$ renpy.music.set_volume(1.0, 1.0, channel="ambient")
stop music fadeout 8.0

nvl hide dissolve
nvl clear

hide rin2
show rin basic_blush_close behind dandelionsfg at center
with charadistant

window show

# "After our lips break apart, it takes a while for either of us to realize that we can say something now."
"เมื่อผละริมฝีปากจากกันแล้วก็ยังต้องรออีกครู่หนึ่งกว่าพวกเราสักคนจะรู้ตัวว่าตอนนี้พูดอะไรได้แล้ว"

"…"

show rin basic_sad_close
with charachange

# rin "See?"
rin "เห็นมั้ย"

show rin relaxed_doubt_close
with charachange

# rin "You are a really kind person, even when you are not."
rin "นายเป็นคนแสนดีมาก ๆ แม้แต่ตอนที่นายไม่แสนดี"

# rin "It's the most scariest thing ever."
rin "เป็นอะไรที่น่ากลัวที่สุดเลย"

show rin relaxed_sleepy_close
with charachange

# rin "I think… that all I was ever afraid of is your kindness."
rin "ฉันคิด… ว่าสิ่งที่ฉันกลัวมาตลอดคือความใจดีของนาย"

"…"

# hi "Is it bad? Even if you are afraid?"
hi "ไม่ดีเหรอ เห็นบอกว่ากลัว"

show rin basic_lucid_close
with charachange

# "She thinks about this for a while, furrowing her brow as though this was some kind of hard math problem."
"เธอคิดอยู่พักหนึ่งพลางขมวดคิ้วราวกับว่าคำถามนั้นคือโจทย์ปัญหาคณิตศาสตร์ยาก ๆ ข้อหนึ่ง"

show rin basic_deadpanamused_close
with charachange

# rin "No. I'm all right with it. It's fine, if it's you."
rin "ไม่ ฉันไม่เป็นอะไร ถ้าเป็นนายแล้วก็ไม่เป็นอะไร"

# "Like a weight lifted from my chest, her words elate my heart, filling it with… I don't know, happiness?"
"โล่งราวกับยกภูเขาออกจากอก คำพูดเธอทำให้ใจฉันลอยและพองโตด้วย… ไม่รู้สิ ความสุขมั้ง"

# "What else could it be?"
"จะเป็นอะไรไปได้อีก"

# "This time my smile is genuine."
"คราวนี้รอยยิ้มของฉันมาจากใจจริง"

hide rin
show rin basic_deadpanamused as rin2 behind dandelionsfg
with charadistant

# "Rin steps back, still smiling gently at me like I do at her."
"รินถอยไปพร้อมยิ้มให้ฉันอย่างอ่อนโยนอย่างที่ฉันยิ้มให้เธอ"

show dandelion full:
    alpha 0.0 xalign 0.5 yanchor 1.0 ypos 1.2 subpixel True
    easein 1.0 ypos 1.0 alpha 1.0
with None
show dandelionbg behind dandelion
show dandelions_blurbg behind dandelion
show dandelions_blurfg behind dandelion
hide dandelionsfg
hide dandelionsbg
with Dissolve(1.0)

hide rin2
show rin basic_deadpanamused behind dandelionbg
with None

# "While she wipes her face on her shoulder, I pick up a round, plump dandelion clock and bring it to my pursed lips."
"ระหว่างที่เธอกำลังเช็ดหน้าอยู่กับหัวไหล่ฉันก็เด็ดดอกแดนดีไลออนกลม ๆ ฟู ๆ ดอกหนึ่งขึ้นมาจ่อปากฉันที่ยู่อยู่"

show dandelion gone
with Dissolve(1.0)

# "Pfff…"
"ฟู่…"

# "They spread out into the wind that picks them up to carry them to a new home."
"เมล็ดเหล่านั้นกระจายไปตามสายลมที่จะพาพวกมันไปยังบ้านหลังใหม่"

# "To think, only a few short weeks ago they were so different."
"คิดดูแล้วก็นะ ที่เห็นเมื่อไม่กี่สัปดาห์ก่อนยังไม่เป็นอย่างนี้เลย"

# "This is change."
"นี่คือการเปลี่ยนแปลง"

"…"

show dandelion gone:
    easeout 1.0 alpha 0.0 yanchor 1.0 ypos 1.2
with None

hide dandelionbg
hide dandelions_blurbg
hide dandelions_blurfg
show dandelionsbg dense behind rin
show dandelionsfg dense
with Dissolve(1.0)

# hi "Hey, so the flowers became what they were meant to become, like you said the last time."
hi "นี่ ดอกไม้มันกลายเป็นสิ่งที่มันควรจะเป็นอย่างที่เธอบอกคราวที่แล้วแล้วนะ"

# hi "What about you? Did you become a true artist? Or did you not, because you ran away?"
hi "แล้วเธอล่ะ เธอได้เป็นศิลปินตัวจริงหรือยัง หรือไม่ได้เป็นเพราะหนีมาก่อน"

show rin basic_deadpancontemplation
with charachange

# "She pauses for a while to ponder my question…"
"เธอคิดอยู่พักหนึ่งเพื่อใคร่ครวญกับคำถามของฉัน…"

show rin relaxed_nonchalant
with charachange

# "…and shrugs her shoulders."
"…แล้วยักไหล่"

# "It almost makes me laugh."
"ฉันเกือบจะหลุดขำ"

# "The carefree easiness of her gesture is a lovely thing, a sign of how Rin can, truly and really, without any restraints whatsoever, shed the entire weight of the world from her shoulders, should she will so."
"ท่าทีสบาย ๆ ของเธอนั้นแสนจะน่าเอ็นดู เป็นสิ่งที่บอกว่ารินนั้นสามารถที่จะทิ้งน้ำหนักของโลกไปจากบ่าของเธอ\nได้จริง ๆ และโดยแท้จริงหากเธอต้องการโดยไม่มีอะไรอาจเหนี่ยวรั้ง"

# "She is, in every possible and probably a few impossible ways… free."
"เธอนั้น—ในทุก ๆ ทางที่เป็นไปได้และอาจจะบางทางที่เป็นไปไม่ได้…—เป็นอิสระ"

# "And I think I might love her for that."
"และฉันก็คิดว่าฉันคงจะรักเธอเพราะเหตุเช่นนั้น"

show rin basic_absent
with charachange

# rin "I don't think it matters."
rin "ฉันคิดว่าไม่สำคัญหรอก"

show rin basic_deadpandelight
with charachange

# rin "Let's just watch the clouds for today."
rin "วันนี้ดูเมฆเฉย ๆ กันเถอะ"

play music music_twinkle fadein 2.0

scene ev rin_goodend_1
show evbg rin_goodend_base:
    center
    subpixel True xalign 0.0
    1.0
    easein 20.0 xalign 1.0
show dandelionsbg dense
show rin goodend_1:
    center
    subpixel True xalign -0.5
    1.0
    easein 20.0 xalign 1.0
show dandelionsfg dense
show evfg rin_goodend:
    center
    subpixel True xalign -1.0
    1.0
    easein 20.0 xalign 1.0
with whiteout

# "She takes five steps to climb on a large rock so she can rise as high as it's possible here, and stands on tiptoes."
"เธอเดินไปอีกห้าก้าวขึ้นไปบนก้อนหินเพื่อที่จะได้อยู่จุดสูงสุดที่เป็นไปได้ของยอดเขานี้ และยังเขย่งเท้าด้วย"

# "When you reach for the clouds, every inch counts."
"เมื่อจะเอื้อมมือคว้าเมฆ ทุก ๆ เซนติเมตรนั้นสำคัญ"

# hi "Sure, let's watch the clouds. It's good to do something you really want to do, every now and then."
hi "ได้ ดูเมฆกัน ได้ทำอะไรที่อยากทำก็ดีเหมือนกัน นาน ๆ ที"

# rin "Yeah. You are probably right."
rin "อืม คงจะถูกของนาย"

# "I glance upwards at the blue sky opening high above us."
"ฉันแหงนหน้ามองท้องฟ้าที่แผ่กว้างอยู่เหนือเรา"

# "It's a deep, cerulean vastness that spreads to fill my entire field of vision and beyond."
"เป็นผืนสีครามกว้างไกลที่เข้ามาเติมเต็มวิสัยทัศน์ของฉันไปจนมากล้น"

# "Yet Rin stays on her rock, peering at the distant horizon where the rain clouds are drifting farther away from us."
"แต่รินก็ยังยืนอยู่บนก้อนหินคอยมองเส้นขอบฟ้าไกลที่มีเมฆฝนมุ่งหน้าหนีห่างไปจากพวกเรา"

# rin "I have decided something."
rin "ฉันตัดสินใจอะไรบางอย่างได้แล้ว"

# "That dreaming voice of hers, spoken to the wind that carries it to my ears, is lacking resolve in tone but is full of it in meaning."
"เสียงชวนฝันของเธอนั้นมากับสายลมที่พัดเข้ามาให้หูฉันได้ยิน แม้จะไม่มีความเด็ดเดี่ยวในน้ำเสียง แต่ก็เป็นคำที่มาก\nด้วยความหมาย"

# rin "It's all right to be me after all."
rin "เป็นฉันก็ไม่เห็นเป็นอะไร"

$ renpy.music.set_volume(0.5, 1.0, channel="music")
$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

window hide
nvl clear
nvl show dissolve

# n "\n\n\nIt's all right? Her decisions always seem to be pretty… far out."
n "\n\n\nไม่เป็นอะไร? การตัดสินใจแต่ละอย่างของเธอนั้นค่อนข้าง… แหวกแนว"

# n "Well, I suppose that is an important realization."
n "ก็นะ คงจะเป็นการระลึกได้ที่สำคัญแหละ"

# n "Coming to terms with oneself, accepting yourself, being fine with what you are."
n "เข้ากับตัวเอง ยอมรับตัวเอง เป็นอย่างที่ตัวเองเป็น"

# n "A simple resolution of heart that for some people is overbearingly hard to do, if not impossible."
n "เป็นการตัดสินใจที่ดูง่าย ทว่าสำหรับบางคนแล้วนั้นเป็นสิ่งที่ทำได้ยากเกินรับไหว หรืออาจจะทำไม่ได้เลยด้วยซ้ำ"

# n "I do realize well enough that I might also be one of those people."
n "ฉันรู้ดีว่าฉันเองก็คงเป็นหนึ่งในคนเหล่านั้นด้วย"

# n "Rin too… "
n "รินก็ด้วย…"

# n "Maybe we are not that different after all."
n "บางที พวกเราก็คงไม่ได้ต่างกันขนาดนั้นหรอก"

# n "Maybe to accept someone else, you must first accept yourself."
n "บางที ก่อนที่จะยอมรับใคร ก็ต้องยอมรับตัวเองก่อน"

# n "Maybe that is a necessary step, which we didn't take until now."
n "บางที นั่นก็เป็นก้าวหนึ่งที่จำเป็นต้องเดิน ซึ่งก่อนหน้านี้พวกเราไม่ได้ก้าวไป"

$ renpy.music.set_volume(1.0, 1.0, channel="music")
$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

nvl hide dissolve
nvl clear
window show

# "Looking at her standing on that rock, I believe that she can find whatever she is looking for."
"พอได้เห็นเธอที่ยืนอยู่บนหินก้อนนั้นแล้วฉันก็เชื่อว่าเธอสามารถที่จะหาสิ่งที่เธอตามหาอยู่ได้จนเจอเสมอ"

# "And so can I."
"ฉันก็เช่นกัน"

show ev rin_goodend_1b
show evbg rin_goodend_base:
    subpixel False xalign 1.0
show rin goodend_1b:
    subpixel False xalign 1.0
show evfg rin_goodend:
    subpixel False xalign 1.0
with charachange

# "The wind catches her hair and clothes, and Rin spreads her short arms into an embrace that is so very very tiny, but as wide as she can ever do."
"ลมพัดให้ผมและเสื้อผ้าเธอพลิ้วไหว รินกางแขนออกเป็นโอบกอดหนึ่งที่เล็กมาก ๆ แต่ก็เป็นโอบที่กว้างที่สุดเท่าที่เธอ\nจะโอบได้"

# "For a moment it looks like she herself might take flight, and I have to hold myself back to not reach for her shoulder, to not drag her back to me."
"แวบหนึ่งดูคล้ายกับว่าเธอจะออกโผบิน แล้วฉันก็ต้องรั้งตัวเองไว้ไม่ให้พุ่งไปคว้าไหล่เธอลากให้เธอกลับมาอยู่กับฉัน"

# "But this picture is something I can only watch, it is something for me to remember."
"แต่ภาพนี้เป็นสิ่งที่ฉันได้แต่เพียงมอง เป็นสิ่งที่ให้ฉันเก็บไว้เป็นความทรงจำ"

# "Rin's sleeves are flapping freely in the wind, her hair wildly tousled by it, her skin touched by the setting sun."
"แขนเสื้อรินโบกสะบัดอย่างอิสระไปตามสายลม ผมของเธอถูกผมยีจนยุ่งเหยิง ผิวของเธอถูกอาทิตย์อัสดงอาบไล้"

# "Her sleek form that I've come to adore is quivering in the cool wind that carries the small white specks past her, each a beginning of a new flower."
"รูปร่างผอมเรียวที่ฉันเอ็นดูนั้นสั่นอยู่ในสายลมเย็นที่พัดพาให้จุดขาว ๆ ปลิวผ่านตัวเธอไป โดยแต่ละจุดนั้นจะกลาย\nไปเป็นดอกไม้ดอกใหม่"

# "All that is engraved inside my heart."
"เหล่านั้นถูกสลักไว้ในใจฉัน"

# "Like those tiny seeds scattered into the wind, I'm sure that Rin too can take her place in this world without the need to create her own inside of it."
"ฉันมั่นใจว่ารินสามารถที่จะยืนอยู่ในโลกใบนี้ได้โดยที่ไม่ต้องสร้างโลกของเธอเองขึ้นมาอีกชั้นหนึ่ง เหมือนอย่าง\nเมล็ดเล็ก ๆ เหล่านั้นที่ปลิดปลิวไปตามสายลม"

# "Maybe she believes it too, and standing as close to heaven as possible, she is giving the world a big hug."
"บางทีเธออาจจะเชื่อเช่นนั้นเหมือนกัน จึงยืนให้ใกล้สวรรค์ให้มากที่สุดเท่าทีี่จะทำได้เพื่อที่จะโอบกอดโลกเอาไว้แน่น ๆ"

# "To me it seems like the entire world really could fit there, between those small arms of hers, inside of her all-encompassing embrace."
"ฉันรู้สึกเหมือนว่าทั้งโลกสามารถที่จะอยู่ในอ้อมกอดเธอได้จริง ๆ เป็นอ้อมกอดที่ครอบคลุมทุกสิ่งเอาไว้ด้วยแขน\nเล็ก ๆ ของเธอ"

show ev rin_goodend_2
show rin goodend_2
with charachange

# rin "Hisao?"
rin "ฮิซาโอะ?"

# "She looks at me in the same way she calls my name, carelessly over her shoulder with a strange happiness in her voice and in her eyes."
"เธอหันมามองฉันและเรียกชื่อฉันด้วยท่าทีแสนสบาย น้ำเสียงและแววตาเธอแฝงด้วยความสุขแปลก ๆ อยู่"

show evbg rin_goodend_base:
    subpixel True yalign 0.0
    acdc_warp 12.0 zoom 1.15
show rin goodend_2_hires:
    subpixel True yalign 0.0 xalign 1.0 zoom 0.769
    acdc_warp 12.0 zoom 1.0
    subpixel False
show evfg rin_goodend:
    subpixel True yalign 0.0
    acdc_warp 12.0 zoom 1.45
with None

# "I gaze into those mysterious, dark eyes that are curiously twinkling from below her auburn hair."
"ฉันจ้องเข้าไปในดวงตาสีเข้มลึกลับคู่นั้นที่วอมแวมด้วยความสงสัยอยู่ใต้ผมสีแดงของเธอ"

# "Although I'm too far from her to see it, I'm sure they are reflecting my image."
"แม้ฉันจะอยู่ไกลเกินกว่าที่จะเห็นในดวงตาเธอ แต่ฉันมั่นใจว่าดวงตานั้นสะท้อนภาพของฉันอยู่"

# hi "What is it?"
hi "อะไรเหรอ"

# rin "What's the word for when it feels inside your heart that everything in the world is all right?"
rin "คำที่เอาไว้เรียกเวลาในใจรู้สึกว่าทุกอย่างในโลกนี้มันเป็นไปด้วยดีคืออะไร?"

stop music fadeout 4.0
stop ambient fadeout 4.0

window hide

return
