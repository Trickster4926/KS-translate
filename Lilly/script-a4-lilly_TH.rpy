label th_L21:

window hide None

scene bg school_scienceroom
with locationchange

nvl clear
nvl show dissolve

$ renpy.music.set_volume(0.5, 1.0, channel="music")
play music music_normal fadein 1.0

# n "\n\n\nAfter the excitement of our trip to Hokkaido, it seems strange to be right back to the usual daily routine so soon. Indeed, it feels like a normal day, the same as any other."
n "\n\n\nหลังจากที่ได้สนุกกับการไปเที่ยวที่ฮกไกโดแล้ว การได้กลับมาใช้ชีวิตตามกิจวัตรประจำวันปกติได้เร็วขนาดนี้นั้นชวนให้\nรู้สึกแปลก แม้จะจริงอยู่ว่าวันนี้ก็รู้สึกเหมือนเป็นวันธรรมดา ๆ วันหนึ่ง"

# n "\nWell, that's what I'd like to think, anyway."
n "\nก็อยากคิดอย่างนั้นอยู่อะนะ"

# n "\nTo tell the truth, the atmosphere of the entire class, no, the entire school has changed."
n "\nแต่ว่าตามตรง บรรยากาศในห้อง ไม่สิ ทั้งโรงเรียนนั้นเปลี่ยนไปหมดเลย"

# n "While an undercurrent of subdued trepidation had previously pervaded the class, now that the exams are in sight it's boiled over into frantic studying rarely seen otherwise."
n "ก่อนหน้านี้อารมณ์ของคนในห้องจะเป็นทำนองว่าใกล้สอบแล้วแต่ยังพอมีเวลา ไม่ได้ร้อนรนมากมาย แต่เมื่อถึงตอนนี้\nที่เป็นช่วงใกล้สอบแบบไม่มีเวลาเหลือมากแล้วแทบทุกคนต่างก้มหน้าก้มตาอ่านหนังสือกัน"

# n "One day until exams start. It's horrific, really, that instead of studying we went and wasted our time up north. We were such model students, too."
n "อีกหนึ่งวันก็จะสอบแล้ว เอาจริง ๆ ก็ใช้ไม่ได้เหมือนกันที่ขึ้นเหนือไปเที่ยวช่วงวันหยุดแทนที่จะเอาเวลาไปอ่านหนังสือ\nแถมพวกเรายังถือว่าเป็นนักเรียนดีเด่นของห้องด้วย"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

show misha invis_close:
    xanchor 0.5 xpos -0.1
with None

show misha perky_confused_close:
    xpos 0.1
show bg school_scienceroom at bgright
with dissolvecharamove

window show

# "Glancing around the class, even the bubbly, ever-energetic Misha seems oddly deflated. She sits at her desk, nervously chewing a pen while Mutou lectures from the front of the class."
"พอมองไปรอบห้องก็เห็นมิช่าที่ทุกทีจะร่าเริงสดใสแรงเหลือล้นเสมอนั่งห่อเหี่ยวอยู่แปลกตาเคี้ยวปากกาฟังครูที่สอน\nอยู่หน้าห้อง"

# "Wait… on closer inspection, I do believe she's eating it."
"เดี๋ยวนะ… พอดูดี ๆ แล้ว นี่มิช่ากินปากกาอยู่นี่นา"

show misha invis_close:
    xpos -0.1
show bg school_scienceroom at center
with dissolvecharamove

hide misha
with None

# "Tearing my eyes from the sorry spectacle, I turn my attention elsewhere."
"ฉันละสายตาจากภาพอันน่าหดหู่แล้วหันไปมองทางอื่น"

show hanako invis:
    xanchor 0.5 xpos 1.1
with None

show hanako defarms_strain:
    xpos 0.94
show bg school_scienceroom at bgleft
with dissolvecharamove

# "Hanako sits frantically scribbling in her notebook, her face mere inches away from the page, seemingly trying to record every word that leaves Mutou's mouth."
"ฮานาโกะก้มหน้าก้มตาจดอยู่แบบหน้าแทบจะติดกับสมุดอยู่แล้ว ดูอย่างกับว่าจะจดทุกอย่างที่ครูพูดออกมางั้นแหละ"

show shizu invis:
    xanchor 0.5 xpos 0.0
show misha invis_close:
    xanchor 0.5 xpos -0.1
with None

show shizu basic_normal:
    xanchor 0.5 xpos 0.3
show misha perky_confused_close:
    xpos 0.1
show hanako invis:
    xpos 1.1
show bg school_scienceroom at bgright
with dissolvecharamove

hide hanako
with None

# "Shizune's, well… Shizune. Cool as a cucumber, she sits diligently taking notes with her attention wholly focused on the front of the class."
"ส่วนชิซูเนะ ก็… ชิซูเนะอะนะ เธอนั่งจดอย่างขะมักเขม้นอยู่ด้วยใจเยือกเย็นตั้งสมาธิไปยังบริเวณหน้าห้องเต็มที่"

# "Truth be told, it's what I should be doing as well, if not for the fact that I feel like I have a pretty good handle on what's being covered already."
"เอาจริง ๆ ฉันก็ควรที่จะนั่งจดแบบนั้นเหมือนกันนั่นแหละ แต่ที่ไม่จดก็เพราะในใจฉันก็รู้สึกว่าพอจะเข้าใจสิ่งที่กำลัง\nเรียนอยู่พอสมควรแล้ว"

# "I wonder how Lilly's doing. While she does have a good head on her, she has plenty on her plate, unlike me. Her class representative duties, taking care of Hanako, her other social contacts, her extra English studies… that girl really does take on a lot."
"ลิลลี่จะเป็นยังไงบ้างนะ ถึงลิลลี่จะหัวดีก็จริง แต่ก็มีภาระอะไรที่ต้องทำมากมาย ไหนจะเป็นหัวหน้าห้อง ไหนจะต้องดูแล\nฮานาโกะ ไหนจะเรื่องเพื่อนคนอื่น ไหนจะเรียนพิเศษภาษาอังกฤษ ไม่เหมือนฉันที่อยู่ว่าง ๆ … ลิลลี่นี่หน้าที่เยอะจริง ๆ"

scene bg school_scienceroom
with shorttimeskip

play sound sfx_normalbell

# "The lunchtime bell brings a sigh of relief from the entire class, Mutou being no exception. I get the feeling he much prefers the more laid-back atmosphere of his normal classes to the frantic pace of exam preparation we're subjected to right now."
"ทั้งห้องต่างถอนหายใจโล่งอกเมื่อระฆังพักเที่ยงดัง แม้แต่ครูก็ถอนหายใจตามด้วย ครูคงจะชอบให้ห้องเรียนมีบรรยากาศ\nแบบสบาย ๆ มากกว่าการที่จะต้องมาเห็นแต่ละคนในห้องต้องมาหน้าดำคร่ำเครียดกับการเตรียมสอบเหมือนอย่างตอนนี้"

# mi "Hicchan~…"
mi "ฮิจัง~…"

show misha invis_close:
    xanchor 0.5 xpos 0.1
with None

show misha perky_sad_close at twoleft
show bg school_scienceroom at bgright
with dissolvecharamove

# mi "Help me~…"
mi "ช่วยด้วย~…"

# "I lower my eyelids to half-mast, making clear my intention of doing quite the opposite."
"ฉันหรี่ตาลงครึ่งหนึ่งเป็นการบอกเจตนาชัดว่ายังไงเสียฉันก็ไม่ช่วย"

# mi "Help me, help me, help me~…"
mi "ช่วยด้วย ช่วยด้วย ช่วยด้วย~…"

# hi "Not going well?"
hi "จะตายแล้วเหรอ"

show misha perky_confused_close
with charachange

# mi "Shicchan's going to be fine, but I think I might die. Am I going to die, Hicchan? Will you let me die from all this work?"
mi "ชิจังน่ะไม่ตายหรอก แต่ฉันเนี่ยแหละจะตาย นี่ฉันจะตายแล้วเหรอฮิจัง นายจะปล่อยให้ฉันตายไปกับงานพวกนี้จริงเหรอ"

# "How maudlin. Given that she's neither the brightest student in the class, nor the most diligent, it isn't a great surprise that she's finding it hard to cope with the workload."
"ฟังแล้วน้ำตาจะไหล ดูจากสภาพของมิช่าที่ไม่ได้หัวดีขนาดนั้น แล้วยังไม่ได้ขยันขนาดนั้นด้วย จะเครียดกับภาระงาน\nขนาดนี้ก็ไม่แปลก"

# hi "Sorry Misha, but I've got my own work to do. I thought you and Shizune would be studying together over the long weekend, anyway?"
hi "ขอโทษทีนะมิช่า แต่ฉันก็มีงานของตัวเองที่ต้องทำอยู่เหมือนกัน แล้ววันหยุดที่ผ่านมานี่ไม่ใช่ว่าเธอสองคน\nไปอ่านหนังสือสอบมาด้วยกันเหรอ"

show misha sign_sad_close
with charachange

# mi "Studying's too boring to waste a holiday on, Hicchan! Shopping together was much more fun, wasn't it, Shicchan?"
mi "วันหยุดทั้งทีแต่ดันจะให้ไปอ่านหนังสือสอบเนี่ยนะฮิจัง น่าเบื่อตายเลย! ไปซื้อของด้วยกันสนุกกว่าเยอะ เนอะ ชิจัง"

show shizu behind_blank at tworight behind misha
with charaenter

# "It's only now that I realize Shizune's been looking over to us, and that Misha's arms have been moving likely all this time. I must be really zoned out to not have noticed."
"และฉันก็เพิ่งสังเกตว่าชิซูเนะกำลังมองมาทางพวกเราอยู่ และเพิ่งสังเกตด้วยว่ามิช่าขยับแขนอยู่ตลอด สงสัยคงเหม่อ\nมากไปถึงไม่ทันสังเกต"

# hi "What is it with girls and shopping, anyway? Even Lilly and Hanako have dragged me out with them a couple of times."
hi "แล้วผู้หญิงมันเป็นอะไรกับการซื้อของนักหนาฮะ ขนาดลิลลี่กับฮานาโกะยังเคยลากฉันไปซื้อของแล้วด้วยครั้งสองครั้ง\nเลย"

show misha hips_grin_close
with charachange

# mi "But you went anyway? It's so rare to see a guy that likes going shopping~…"
mi "แต่นายก็ไปนี่ ไม่ค่อยได้เห็นผู้ชายที่ชอบไปเดินซื้อของเลยนะ~…"

# hi "Well, my role would probably be best described as “pack mule”. I can't say I share your enthusiasm about the experience."
hi "ก็นะ ถ้าจะพูดให้ถูก หน้าที่ฉันคือ “เบ๊หาบของ” มากกว่า ฉันไม่ได้ตื่นเต้นอะไรกับการเดินซื้อของขนาดนั้น\nเหมือนอย่างพวกเธอหรอก"

# hi "Back to the exams; you studied after you got back from the days off, didn't you, Shizune?"
hi "พูดถึงเรื่องสอบ ชิซูเนะ เธอเที่ยวเสร็จกับมาแล้วก็ยังอ่านหนังสืออยู่ใช่มั้ย"

show shizu basic_normal2
with charachange

shi "…"

show misha sign_smile_close
with charachange

# mi "Of course, Hicchan. It's only sensible to study in the days before…"
mi "แหงสิฮิจัง ใคร ๆ ก็ต้องคิดได้หรือเปล่าว่าควรอ่านหนังสือสอบตอนใกล้…"

show misha perky_sad_close
with charachange

# mi "U~rgh."
mi "โอ๊~ ย"

# "Misha makes a sound vaguely similar to a dying cow as she realizes her folly and unceremoniously flops onto her desk, betrayed even by her best friend."
"มิช่าที่ถูกแม้กระทั่งเพื่อนรักของเธอทรยศร้องเสียงละม้ายคล้ายวัวโดนเชือดเมื่อรู้ตัวถึงความโง่เง่าของตัวเองแล้วฟุบ\nไปกับโต๊ะด้วยสภาพหมดอาลัยตายอยาก"

show shizu basic_angry
with charachange

# "Judging from Shizune's quite frustrated look at Misha, she probably told her to study as she did."
"ดูจากสีหน้าหงุดหงิดของชิซูเนะที่มองมิช่าแล้ว เธอก็คงบอกให้มิช่าอ่านหนังสือสอบเหมือนตัวเองเหมือนกัน"

# hi "Don't worry, you can still gain some grades if you start studying now."
hi "อย่าห่วงไปเลย ถ้าอ่านหนังสือตอนนี้ก็ยังพอเพิ่มคะแนนได้ทันนะ"

# hi "Maybe."
hi "อาจจะ"

# "Misha does not seem overly amused. It seems the bubbly balloon of everlasting cheerfulness has been cruelly popped."
"มิช่าดูไม่ได้สบายใจขึ้นเท่าไหร่ ดูท่าว่าลูกโป่งความสดใสเหลือล้นอันยืนยงจะถูกเจาะจนแตกดังปังไปอย่างโหดร้าย\nเสียแล้ว"

show shizu behind_blank
with charachange

shi "…"

show shizu behind_blank_close
with characlose

with Pause(0.3)

show shizu adjust_frown_close
show misha perky_confused_close
with vpunch

# "Shizune's signing goes unnoticed by the moping Misha, earning her a quick poke in the shoulder. It takes barely a moment for Misha to get back into form."
"มิช่าที่คร่ำครวญอยู่ไม่ทันได้สังเกตเห็นที่ชิซูเนะทำภาษามือจนชิซูเนะต้องสะกิดไหล่มิช่า แต่แค่ชั่วไม่กี่อึดใจมิช่า\nก็กลับมาสภาพเดิม"

show misha hips_smile_close
with charachange

# mi "Oh, ah, so what did you do over the weekend, Hicchan?"
mi "อ้อ เอ้อ แล้ววันตอนหยุดนายไปทำอะไรมาล่ะ ฮิจัง"

# hi "Just took a trip up north with Lilly and Hanako. It was pretty nice."
hi "เพิ่งขึ้นเหนือไปเที่ยวกับลิลลี่แล้วก็ฮานาโกะมาเลย ก็สนุกดี"

show misha perky_smile_close
show shizu behind_blank_close
with charachange

# "I see both of them narrowing their eyes at me, their minds surely in the gutter. The fact that their suspicions are founded makes the situation all the more awkward."
"ทั้งสองคนหรี่ตามองฉัน ชัดว่าคิดอะไรไปไกลแล้วแน่ ๆ แล้วที่ยิ่งชวนให้อึดอัดไปกว่านั้นคือการคิดไปไกลที่ว่า\nของพวกเธอนั้นมีมูล ไม่ใช่คิดไปเองแบบลอย ๆ"

# hi "We just studied and went sightseeing; there's nothing more to it."
hi "ก็แค่ไปเที่ยวที่นั่นที่นี่แล้วก็อ่านหนังสือสอบกันเฉย ๆ ไม่มีอะไรมากกว่านั้นเลย"

show misha cross_smile_close
with charachange

# mi "Hmm~…"
mi "อืมม~…"

# "After such a flagrant lie, I realize that it may not have been the best step, considering Shizune's connections and her total lack of restraint when it comes to questioning someone she suspects of telling untruths."
"พอโกหกหน้าด้าน ๆ ไปอย่างนั้นแล้วก็ถึงนึกได้ว่าไม่น่าพูดไปอย่างนั้นเลย ชิซูเนะก็พอจะรู้จักคนอยู่เหมือนกัน แล้วยิ่ง\nเป็นคนที่ถ้าได้สงสัยว่าใครสักคนโกหกแล้วเธอก็จะคาดคั้นเอาคำตอบมาจนได้"

# "I really have no idea of how she's going to take it, but she'll find out eventually anyway. It isn't as if it's really her business whom I date, in any case."
"นึกภาพไม่ออกเลยว่าถ้าได้รู้แล้วชิซูเนะจะทำตัวยังไง แต่ยังไงสักวันก็คงได้รู้แหละ ซึ่งยังไงเสีย แฟนฉันจะเป็นใครมันก็\nไม่ใช่กงการอะไรของเธอสักหน่อย"

# hi "And yes, Lilly and I are going out now."
hi "แล้วก็นั่นแหละ ลิลลี่กับฉันเป็นแฟนกันแล้ว"

show misha hips_grin_close
show shizu basic_normal2_close
with charachange

# "While Misha receives the news with an enthusiastic smile, Shizune gives a look of mild surprise somewhat masked by her cool demeanor."
"มิช่ารับฟังข่าวนั้นพร้อมรอยยิ้มปิติยินดียิ่ง ส่วนชิซูเนะดูจะแปลกใจเล็กน้อยแต่ยังคงทำหน้านิ่งตามปกติกลบเกลื่อน"

show shizu behind_blank_close
with charachange

shi "…"

show misha sign_smile_close
with charachange

# mi "Whoever you date is your business. I hope you two go well together."
mi "นายจะไปคบกับใครก็เรื่องของนาย ขอให้รักกันนาน ๆ นะ"

# "Misha gives a look that says this is the most quarter I could possibly receive on the matter. It's all I wanted, really."
"มิช่าทำหน้าเป็นสัญญาณทำนองว่าฉันจะไม่ได้รับความเห็นอะไรเพิ่มเติมจากชิซูเนะอีก แต่แค่นี้ฉันก็พอใจแล้วละ"

show shizu basic_normal2_close
with charachange

# "After she says this, though, Shizune begins to sign something else, then stops herself and shakes her head at Misha to prevent her from translating."
"แต่พอชิซูเนะพูดจบแล้วเธอก็ทำภาษามืออะไรอย่างอื่นต่อแล้วเว้นจังหวะไปก่อนจะส่ายหัวเป็นการบอกให้มิช่า\nหยุดการแปลไว้"

hide shizu
with charaexit

hide misha
with charaexit

# "Normally I'd think this strange enough, but the awkwardly casual wave Shizune gives before walking off with Misha in tow adds to my confusion. Shizune's hardly the kind of person to pull a punch or communicate without forethought."
"ตอนนี้ฉันก็รู้สึกแปลก ๆ อยู่แล้ว แต่ยิ่งได้เห็นชิซูเนะที่โบกมือสบาย ๆ แบบผิดสังเกตก่อนจะเดินออกไปโดยมีมิช่าตามไป\nด้วยแล้วฉันก็ยิ่งงงหนักไปใหญ่ ชิซูเนะนั้นไม่ใช่คนที่จะพูดอะไรตรง ๆ จะพูดอะไรก็ต้องคิดก่อนเสมอ"

# "I shrug my shoulders at the duo's odd behavior and look towards Hanako's desk, but see that her chair's empty. She was definitely here before, so I guess she just didn't feel like waiting."
"ฉันยักไหล่ให้กับสองคนนั้นที่ทำตัวแปลก ๆ แล้วหันไปมองที่โต๊ะฮานาโกะซึ่งไม่มีคนนั่งอยู่ เมื่อกี้ยังเห็นอยู่นี่นา สงสัย\nคงขี้เกียจรอแล้วมั้ง"

# "I'll go grab some food alone, then."
"งั้นเดี๋ยวไปซื้อข้าวเองก็ได้"

stop music fadeout 2.0

scene bg school_hallway2
with shorttimeskip

# "Walking down the hallway to the unused room that's become a second home to three students in particular, I mournfully look down at the plastic-wrapped salad roll and juice box in my hand."
"ฉันเดินไปตามโถงทางเดินไปยังห้องที่ไม่มีใครใช้แล้วซึ่งได้แปรสภาพเป็นบ้านหลังที่สองของนักเรียนสามคนกลุ่มหนึ่ง\nระหว่างนั้นก็ก้มมองสลัดโรลที่ห่อพลาสติกกับกล่องน้ำผลไม้ที่ถือมา"

# "The cafeteria's food really is unappetizing. Maybe I'll consider this my penance for my recent indiscretions."
"อาหารที่โรงอาหารนี่ไม่น่ากินเอาเสียเลย ถือเสียว่าเป็นบทลงโทษกับการที่ฉันพลั้งปากอะไรไปแบบไม่คิดเมื่อกี้แล้วกัน"

# "Opening the door, I notice one less quiet figure than I'd expected."
"พอเปิดประตูก็เห็นว่ามีคนที่เงียบ ๆ คนหนึ่งหายไป"

scene ev lilly_tearoom
with whiteout

play music music_lilly fadein 3.0

# "It's strange. Despite having known Lilly for months, I can't help thinking back to the very first time I opened this door and saw her silently sitting in the sunlight."
"แปลกดี รู้จักลิลลี่มาก็สองสามเดือนแล้ว แต่ก็อดไม่ได้ที่จะคิดถึงครั้งแรกที่เปิดประตูมาเห็นลิลลี่ที่นั่งให้แดดส่องอยู่เงียบ ๆ\nในห้องนี้"

show ev lilly_tearoom_open
with charachange

# "Just as she did then, she slowly opens her eyes, unmoving as they are, and calmly addresses me."
"ลิลลี่ลืมตาขึ้นช้า ๆ เหมือนตอนที่ฉันเจอเธอเป็นครั้งแรก เธอยังนั่งนิ่งอยู่แล้วทักทายฉันด้วยน้ำเสียงอันเยือกเย็น"

# li "Good morning, Hisao."
li "อรุณสวัสด์จ้ะฮิซาโอะ"

# hi "It's afternoon, I think."
hi "เหมือนจะบ่ายแล้วนะ"

# hi "Has Hanako been around? She skittered out of class without me even noticing."
hi "ฮานาโกะมาที่นี่มั้ย เมื่อกี้ออกห้องไปไม่ทันสังเกตเลย"

scene bg school_miyagi
show lilly basic_listen_close:
    center
    ypos 1.1
with locationchange

# "Lilly cradles her cheek thoughtfully as I take a seat, my bag taking its place against the closest leg of the table and my unsatisfying meal neatly set out in front of me."
"ลิลลี่จับแก้มตัวเองครุ่นคิด ระหว่างนั้นฉันก็นั่งลงวางกระเป๋าไว้กับขาโต๊ะที่อยู่ใกล้ ๆ ก่อนจะวางมื้ออาหารอัน\nไม่เป็นที่น่าพอใจเลยนั้นลงตรงหน้า"

show lilly basic_reminisce_close
with charachange

# li "She did appear… for a time. She said she had to study for the upcoming exams, and left for the library."
li "ฮานาโกะมา… อยู่พักหนึ่งนะ แล้วก็บอกว่าต้องไปอ่านหนังสือเตรียมสอบที่ห้องสมุดน่ะ"

# "We find ourselves not entirely believing her words."
"พวกเราต่างไม่มีใครเชื่อคำพูดของฮานาโกะ"

# hi "Well, at least her intentions are in the right place."
hi "เอาเถอะ อย่างน้อยก็เจตนาดีละนะ"

show lilly basic_concerned_close
with charachange

# li "She is sweet, but she needn't go this far to let us have our space. I might talk to her about it sometime."
li "ฮานาโกะน่ะน่ารักนะ แต่ไม่เห็นต้องกันที่ไว้ให้พวกเราขนาดนี้เลย ไว้เดี๋ยวต้องไปคุยเรื่องนี้กับฮานาโกะแล้ว"

# hi "Probably for the best."
hi "ก็คงต้องเป็นอย่างนั้นละนะ"

show lilly basic_weaksmile_close
with charachange

# "For a while we quietly eat our meals, Lilly elegantly nibbling on her sandwiches and sipping her tea as I eat what tastes like a garden sandwiched in dry dough."
"พวกเรากินมื้อเที่ยงของตัวเองกันไปเงียบ ๆ ลิลลี่ละเลียดกินแซนด์วิชไปพลางจิบชาไป ส่วนฉันก็นั่งกินไอ้ของที่รสชาติ\nเหมือนแป้งแห้ง ๆ ที่ยัดด้วยรสชาติของเรือกสวน"

# "The atmosphere feels slightly strained, neither of us knowing quite what to say to each other now that our small talk has dried up."
"บรรยากาศนั้นชวนให้อึดอัดเล็กน้อย ต่างคนต่างไม่รู้จะพูดอะไรเพราะไม่มีอะไรให้คุยเรื่อยเปื่อยอีก"

# "Eventually we both finish our food, with no conversation forthcoming for quite some time. Eventually, though, Lilly's soft voice breaks the silence."
"สุดท้ายพวกเราก็นั่งกินอาหารกันเงียบ ๆ อยู่พักใหญ่จนต่างคนต่างอิ่ม แต่หลังจากนั้นลิลลี่ก็พูดขึ้นมาก่อนด้วยเสียง\nอันนุ่มนวล"

show lilly basic_reminisce_close
with charachange

# li "A lot happened back there… didn't it?"
li "ตอนที่ไปเที่ยวนี่มีเรื่องอะไรหลายอย่าง… เลยเนอะ"

# hi "Mm."
hi "อื้ม"

# "Again, silence. With both our minds on the same topic, though, I think I have my feelings on that sorted out."
"แล้วก็เงียบอีกครั้ง แต่คราวนี้เมื่อเราทั้งสองคนต่างคิดถึงเรื่องเดียวกันอยู่ ฉันคิดว่าฉันจัดการกับความรู้สึกของตัวเองได้แล้ว"

# hi "I know everything happened in kind of a hurry, but… I don't regret anything that happened in Hokkaido. Not one thing."
hi "ฉันรู้ว่าอะไรหลายอย่างมันออกจะกะทันหันไปหน่อย แต่ว่า… ฉันไม่นึกเสียใจกับสิ่งที่เกิดขึ้นที่ฮกไกโดเลยนะ ไม่นึก\nเสียใจอะไรเลยแม้แต่อย่างเดียว"

show lilly basic_oops_close
with charachange

# li "Hisao…?"
li "ฮิซาโอะ…?"

# "Slightly tense, I take her hands in mine; half to feel her, half to settle my own nerves."
"ฉันจับมือลิลลี่ไว้ด้วยความเกร็งเล็กน้อย ส่วนหนึ่งก็เพราะอยากสัมผัสเธอ อีกส่วนก็เพื่อให้ตัวเองใจเย็นลง"

# hi "I stand by my words back there, Lilly. I love you, and I won't leave you. I only wish for you to think the same."
hi "ฉันจะขอย้ำคำเดิมที่ฉันเคยพูดไปแล้วนะลิลลี่ ฉันรักเธอ และจะไม่ทิ้งเธอไปไหนเลย ฉันหวังแค่เธอให้คิดเหมือนกับ\nที่ฉันคิด"

show lilly basic_weaksmile_close
with charachange

# "She silently reflects for a long time, which feels like an eternity."
"ลิลลี่เงียบใคร่ครวญอยู่เสียนาน นานเสียจนรู้สึกเหมือนต้องรออยู่ชั่วนิรันดร์"

show lilly invis_close at center
with dissolvecharamove

# "Her reverie comes to an end as she takes one hand from mine, placing it over them as she leans her body forwards and stands out of her chair."
"แล้วเธอก็หลุดจากภวังค์มาเลื่อนมือออกจากฝ่ามือของฉันแล้วมาทับมือฉันไว้แทน ก่อนจะลุกขึ้นยืนแล้วโน้มตัวเข้ามา"

# "After a moment's hesitation, her face slightly pensive, her lips meet mine for a brief moment."
"ลิลลี่นึกลังเลทำหน้าครุ่นคิดอยู่ครู่หนึ่งก่อนจะทาบทับริมฝีปากเธอลงมาที่ริมฝีปากฉันเป็นชั่วระยะสั้น ๆ"

show lilly behind_cheerful_close:
   ypos 1.1
with dissolvecharamove

# "My mind feels as if it briefly stopped at that moment, barely registering Lilly sitting back in her chair and smiling back at me with ever so slightly reddened cheeks."
"สมองฉันหยุดทำงานไปชั่วขณะและแทบไม่ได้รับรู้ถึงลิลลี่ที่กลับไปนั่งตามเดิมแล้วยิ้มให้พร้อมแก้มที่ขึ้นสีแดงเรื่อจาง ๆ"

show lilly basic_smileclosed_close
with charachange

# li "Hearing that makes me very happy, Hisao. I would be glad to stay with you."
li "ฮิซาโอะ ฉันดีใจมากเลยละจ้ะที่ได้ยินเธอพูดอย่างนั้น ฉันยินดีที่จะได้อยู่กับเธอนะ"

# hi "Maybe it would be good to slow things down a bit, compared to before. We still have school, after all, and our exams."
hi "ค่อยเป็นค่อยไปน่าจะดีกว่านะ ไม่ต้องรีบเหมือนอย่างก่อนหน้านี้แล้ว เรายังต้องเรียนต้องสอบกันอยู่"

show lilly basic_giggle_close
with charachange

# "She gives a mischievous giggle, which proves to be contagious."
"ลิลลี่หัวเราะซุกซนที่พาให้ฉันอดหัวเราะตามไปด้วยไม่ได้"

show lilly basic_smileclosed_close
with charachange

# li "That might be a good idea indeed."
li "นั่นสินะจ๊ะ แบบนั้นน่าจะดีที่สุดแล้ว"

show lilly basic_smile_close
with charachange

# li "Do you think you'll fare well in your exams? It's only one day until they arrive, as you say."
li "คิดว่าตัวเองจะพอทำข้อสอบไหวหรือเปล่า อีกหนึ่งวันก็จะถึงวันสอบอย่างที่เธอพูดแล้วนีี่นะ"

# hi "I probably should have studied more, but I think I've got a good enough head to manage."
hi "ที่จริงอาจจะต้องอ่านหนังสือให้เยอะกว่านี้น่ะนะ แต่ก็น่าจะพอไหวอยู่"

# hi "That said, I had to bat off Misha and Shizune. Is your class as worried about the exams as mine?"
hi "แต่ถึงงั้นก็เถอะ ฉันต้องคอยไล่ ๆ มิช่ากับชิซูเนะไม่ให้มากวนด้วย ห้องเธอเครียดเรื่องสอบเหมือนห้องฉันหรือเปล่า"

show lilly basic_weaksmile_close
with charachange

# "She lets out an exasperated sigh, all but confirming it. I'm thankful for the atmosphere becoming a bit lighter."
"ลิลลี่ถอนหายใจห่อเหี่ยวเป็นการบอกว่าฉันเดาถูก โล่งไปทีที่บรรยากาศตอนนี้ผ่อนคลายลงแล้ว"

# li "I think so. I've already been asked for help by two of my classmates, and there'll no doubt be more."
li "คิดว่านะ เพื่อนร่วมห้องฉันก็มาขอให้ฉันสอนนั่นนี่ให้สองคนแล้ว เดี๋ยวคงต้องมีอีกแน่เลย"

# hi "Think of it as your first training in being a teacher, maybe?"
hi "คิดเสียว่าเป็นก้าวแรกของการฝึกเป็นครูไง"

show lilly basic_smile_close
with charachange

# li "That's probably a good way to think of it."
li "คิดอย่างนั้นก็ดีเหมือนกันนะจ๊ะ"

show lilly basic_smileclosed_close
with charachange

# li "On that note, how are you faring in your English studies? I remember it was far from your strongest subject, and the few sentences you memorized to speak to my mother aren't likely to help."
li "จะว่าไป วิชาภาษาอังกฤษเธอเป็นยังไงบ้าง เหมือนจำได้ว่าเป็นวิชาที่เธอไม่ถนัดเลย แล้วประโยคสองสามประโยค\nที่เธอจำไปคุยกับแม่ฉันน่าจะช่วยอะไรได้ไม่มากด้วย"

# "Damn, right on the mark."
"ให้ตาย ถูกต้องตรงเผงเลย"

# hi "You got me. If you don't mind, would you be able to possibly help in that regard? Please?"
hi "ตามนั้น งั้นถ้าเธอไม่ว่าอะไร รบกวนช่วยฉันเรื่องนี้ให้หน่อยได้มั้ย ขอร้องละ"

show lilly basic_planned_close
with charachange

# li "It would be my pleasure to help you, Hisao. But in exchange…"
li "ฉันยินดีช่วยเธอจ้ะฮิซาโอะ แต่มีข้อแม้…"

# "She lowers her eyebrows at me, her coquettish nature tentatively coming to the fore."
"ลิลลี่หรี่ตาลง ตัวตนของเธอที่ชอบยั่วเย้าปรากฏออกมาอยู่แวบหนึ่ง"

# hi "No problem at all. You'd probably be better off with some help in your studies, though."
hi "ย่อมได้ แต่ถ้าขอให้ฉันสอนเธอเป็นการตอบแทนน่าจะดีกว่านะ"

show lilly behind_cheerful_close
with charachange

# "She beams a smile at me, one of girlish victory that nearly makes me blush. I get the feeling she's aware of how to use her face to twist my judgment, so I should probably be more on guard."
"ลิลลี่ส่งยิ้มหญิงสาวอย่างผู้ชนะมาให้จนฉันหน้าแดง น่าจะรู้อยู่ว่าสีหน้าตัวเองมีผลกับความรู้สึกฉัน สงสัยต้องระวังตัว\nให้มากกว่านี้แล้ว"

# "Here and now though, a study group seems like an expedient way for both of us to shore up our more lacking skills."
"แต่เอาเป็นว่า การจับคู่ช่วยกันอ่านหนังสือก็ดูจะเป็นวิธีดี ๆ ที่เราสองคนจะได้เสริมจุดที่ยังอ่อนกันอยู่"

play sound sfx_warningbell

# "The school bell rings out, reminding us that time isn't going to stand still."
"ระฆังโรงเรียนดัง ย้ำเตือนว่าเวลาไม่เคยคอยใคร"

# hi "Huh, lunchtime's over already. It sure is easy to lose track of the time here."
hi "หืม หมดพักเที่ยงแล้วเหรอเนี่ย อยู่ที่นี่ทีไรเพลินจนลืมเวลาตลอดเลย"

show lilly basic_weaksmile_close
with charachange

# li "This room's so far from the other clubs and activities, not much sound can reach us. That's probably most of the reason why."
li "หลัก ๆ ที่รู้สึกอย่างนั้นก็คงเพราะห้องนี้ค่อนข้างเงียบเพราะอยู่ห่างจากชมรมกับห้องเรียนอื่น ๆ มาไกลเลย"

show lilly basic_weaksmile_close at center
with charamove

# "A place far from all the others, alone with just one person whom she loves. As Lilly stands and collects her bag and cane, my thoughts are cast back to the time we spent in Hokkaido."
"ที่ที่ห่างจากผู้คน ที่ที่เธอได้อยู่ตามลำพังด้วยกันกับคนที่เธอรัก ระหว่างที่ลิลลี่ลุกขึ้นยืนเก็บกระเป๋ากับไม้เท้าฉันก็หวน\nนึกถึงช่วงเวลาที่เราไปอยู่ที่ฮกไกโด"

show lilly basic_satisfied_close
with charachange

# li "Ah, before I go; Akira and I are having a homecoming party in my room tomorrow. Will you be able to come?"
li "อ้อ ก่อนไป พรุ่งนี้พี่กับฉันจะจัดงานเลี้ยงฉลองที่ได้กลับมาญี่ปุ่นกัน เธอสะดวกมามั้ยจ๊ะ"

# "…and back again."
"…และกลับมาอีกครั้ง"

# hi "My schedule is free, so I should be able to make enough room in my study time to make it."
hi "ไม่ได้มีอะไรที่ต้องทำอยู่แล้ว น่าจะพอเจียดเวลาจากการอ่านหนังสือไปได้อยู่นะ"

show lilly basic_smileclosed_close
with charachange

# li "Good to hear, Hisao."
li "ดีเลยจ้ะฮิซาโอะ"

# hi "For what it's worth, I'm glad you're back from Scotland. Once exams are over, we should have some more time to ourselves."
hi "แล้วก็นะ ฉันดีใจมากที่เธอกลับมาจากสกอตแลนด์แล้ว ไว้สอบเสร็จหาเวลามาอยู่ด้วยกันสองคนอีกดีไหม"

show lilly basic_smile_close
with charachange

# li "Mm. Holidays start soon after, too."
li "อื้ม เดี๋ยวก็จะปิดเทอมแล้วนี่เนอะ"

# hi "We can start the holidays with Tanabata then, just as we promised at the school festival."
hi "งั้นปิดเทอมแล้วไปเที่ยวงานวันทานาบาตะกันมั้ย ที่เคยสัญญาไว้ตอนอยู่งานเทศกาลโรงเรียนนั่นไง"

show lilly basic_arablush_close
with charachange

# "She brings her hand to her cheek and laughs slightly nervously, recalling the event as I silently thank myself for managing to remember."
"ลิลลี่จับแก้มตัวเองพลางหัวเราะดูประหม่าย้อนนึกถึงเหตุการณ์ครั้งนั้น ฉันนึกขอบคุณตัวเองในใจที่ยังอุตส่าห์จำได้"

# "It seems odd to see her react in such a way, though it's not like I never saw her embarrassed before."
"รู้สึกแปลกอยู่เหมือนกันที่ได้เห็นลิลลี่ทำท่าทางอย่างนี้ ถึงจะเคยเห็นเธอตอนอายแล้วก็เถอะ"

show lilly basic_weaksmile_close
with charachange

# li "I'd… better be going. Farewell, Hisao."
li "ฉัน… ขอตัวก่อนนะจ๊ะ ลาก่อนจ้ะฮิซาโอะ"

# hi "Bye."
hi "บาย"

hide lilly
with charaexit

stop music fadeout 6.0

# "Whether it's out of habit or just a stubborn desire for one small fragment of normality, I hold my hand up in farewell just as I always do. At least I'm consciously aware that I'm doing it now."
"ฉันโบกมือลาอย่างทุกที ไม่รู้เหมือนกันว่าทำไปเพราะความเคยชินหรือเพราะแค่ความต้องการที่จะให้อะไร ๆ\nเป็นไปอย่างปกติแม้เพียงเล็กน้อยก็ตาม แต่อย่างน้อยตอนนี้ก็รู้ตัวแล้วน่ะนะว่าทำอะไรอยู่"

# "I think I'm beginning to see a bigger picture than I ever have before, not only with Lilly but also my life ahead."
"ฉันว่าฉันพอจะเห็นภาพรวมได้กว้างกว่าที่เคยเห็นมาแล้วละ ไม่ใช่แค่กับเรื่องลิลลี่ แต่กับเรื่องชีวิตในอนาคตด้วย"

# "The chains of my past are finally breaking."
"ในที่สุด ตรวนแห่งอดีตของฉันก็เริ่มขาดลงแล้ว"

scene black
with dissolve

#****************************


label th_L22:

$ renpy.music.set_volume(0.8, 0.0, channel="music")
play music music_ease fadein 4.0

scene bg school_girlsdormhall
with locationchange

# "Walking up the now slightly more familiar corridor of the girls' dormitories, I can hear the faint sound of laughter coming from up ahead."
"ฉันเดินไปตามโถงทางเดินหอหญิงที่ฉันคุ้นชินขึ้นมาบ้างเล็กน้อยแล้ว จากนั้นก็ได้ยินเสียงหัวเราะแว่วมาไกล ๆ"

show bg school_girlsdormhall at bgleft
with charamove

# "It doesn't take long to identify the source as Lilly's room, though the deep timbre of the female voice unmistakably belongs not to her, but to her sister."
"ไม่นานนักก็รู้ว่าเสียงนั้นมาจากห้องของลิลลี่ แต่เสียงผู้หญิงที่ฟังดูทุ้ม ๆ นั้นไม่ใช่เสียงของเจ้าตัวอย่างแน่นอน เสียงนั้น\nเป็นเสียงของพี่สาวเธอ"

play sound sfx_doorknock2

# "I rap my knuckles on the door with the usual three light taps, my hand barely retreating as the door swings open."
"ฉันเคาะประตูสามครั้งเบา ๆ อย่างเคย ประตูเปิดออกก่อนที่ฉันจะทันได้ละมือจากการเคาะครั้งสุดท้าย"

show akira invis:
    xanchor 0.5 xpos 1.0
with None

show akira basic_smile:
    xpos 0.9
with dissolvecharamove

# aki "Hey, Hisao."
aki "ไง ฮิซาโอะ"

# hi "Hey. Hello Lilly, Hanako."
hi "ครับ ลิลลี่ ฮานาโกะ สวัสดี"

scene ev lilly_bedroom:
    truecenter
    zoom 1.0 subpixel True
    acdc_warp 8.0 zoom 1.03
with locationchange

# "Hanako looks up tentatively, her hands buried in her oversized pink nightgown. From her side, Lilly turns sideways towards the direction of my voice and smiles."
"ฮานาโกะเงยหน้ามองด้วยความลังเล เธอเอามือตัวเองซุกไว้กับชุดนอนสีชมพูที่ดูหลวมโพรกนั้น ส่วนลิลลี่ที่นั่งอยู่\nข้าง ๆ หันหน้ามาตามเสียงฉันแล้วยิ้มให้"

# "It would be a flagrant lie to say I dislike the sight of her in those pajamas."
"ถ้าจะให้บอกว่าไม่ชอบเธอยามใส่ชุดนอนแล้วก็คงเป็นการโกหกคำโต"

# "I catch Akira giving me a sidelong look with a knowing grin, to which I reply with a sharp glare."
"ฉันเห็นอากิระที่ยิ้มกรุ้มกริ่มเหลือบมองอยู่ฉันจึงจ้องเขม็งใส่กลับ"

scene bg school_dormlilly at bgleft
with locationchange

# "She takes the hint, shrugs and walks back to the low table in the center of the room. As I go to join her, Lilly gives me a nod of greeting and starts pouring me a cup of tea."
"อากิระทำท่ารับรู้ยักไหล่แล้วเดินกลับไปที่โต๊ะเตี้ยกลางห้อง พอฉันเข้าไปร่วมวงด้วยลิลลี่ก็พยักหน้าทักทายแล้วรินน้ำชา\nให้ฉันหนึ่งถ้วย"

show hanagown distant:
    twoleft
    ypos 1.14
show akira basic_smile:
    tworight
    ypos 1.14
with charaenter

# hi "It's nice to see you again, Hanako. You've been getting around recently."
hi "ฮานาโกะ ดีใจจังที่ได้เจอเธออีก ช่วงนี้เธอไปไหนมาไหนบ่อยขึ้นนะ"

# "Lilly wears a look of concentration as the light brown liquid, carefully measured by her finger as always, flows from the teapot into the cup."
"ลิลลี่ทำหน้าจดจ่อขณะที่กำลังเทของเหลวสีน้ำตาลอ่อนนั้นให้ไหลจากกาน้ำชาลงถ้วยน้ำชาโดยมีนิ้วมือเธอเป็นตัววัด\nเช่นเคย"

# li "It seems Hanako has taken up helping one of the people in your class with the newspaper club. Naomi, I think?"
li "เหมือนฮานาโกะเขาจะไปช่วยคนในห้องเธอที่อยู่ชมรมหนังสือพิมพ์นะ ชื่อนาโอมิมั้ง"

show hanagown normal
with charachange

# "Hanako gives an affirmative nod."
"ฮานาโกะพยักหน้ายืนยัน"

# "Even after spending about two months in the class, I still have trouble remembering the names of those students I rarely talk with."
"ถึงจะมาเรียนได้สองเดือนแล้ว แต่ฉันก็ยังจำชื่อนักเรียนคนที่ฉันไม่ค่อยได้คุยด้วยไม่ได้มากเท่าไหร่"

# "It takes me a few mental contortions to connect the name with a face, but I eventually remember the girl that sits beside Hanako at the back of the class."
"ฉันต้องขุดคุ้ยในสมองหาใบหน้าที่ตรงกับชื่อนั้น สุดท้ายก็นึกออกว่าเป็นผู้หญิงคนนั้นที่นั่งหลังห้องอยู่ข้างฮานาโกะ"

# "Naomi Inoue. A fairly average-looking girl, except for her bleached blonde hair."
"นาโอมิ อิโนอูเอะ หน้าตาก็ค่อนข้างเหมือนเด็กผู้หญิงทั่ว ๆ ไป ยกเว้นก็แต่ผมสีบลอนด์จาง"

# "Given her upbeat and straightforward personality, Naomi may have seen an opening to poach Hanako for her club when she enquired about joining one."
"นาโอมิเป็นคนร่าเริงและตรงไปตรงมา คงจะถือเอาจังหวะที่ฮานาโกะถามเรื่องชมรมมาเป็นช่องให้ตัวเองได้ดึงฮานาโกะ\nเข้าชมรมตัวเองเสียเลย"

# "Either way, it's nice to see Hanako broadening her horizons. When I first met her, the idea of her joining a club with anyone but Lilly would have seemed utterly laughable."
"แต่จะอะไรก็แล้วแต่ ได้เห็นฮานาโกะเปิดโลกตัวเองให้กว้างขึ้นอย่างนี้แล้วก็ดีใจ ถ้าเป็นตอนที่เจอครั้งแรก ฉันคงคิดว่า\nยังไงก็เป็นไปไม่ได้ที่ฮานาโกะจะไปเข้าชมรมอื่นที่ไม่มีลิลลี่อยู่ด้วย"

# hi "That'd explain how busy you've been. Enjoying it?"
hi "มิน่าล่ะหมู่นี้เธอถึงยุ่ง ๆ แล้วสนุกมั้ย"

show hanagown smile
with charachange

# ha "Mm. It's… really interesting."
ha "อื้ม น่า… สนใจมากเลยละ"

# "As always, Hanako's far from being talkative. Some things never change, and it seems that Hanako's personality is one of them; she'll likely always be one to shy away from being overly social."
"ฮานาโกะยังคงพูดน้อยคำอย่างเคย บางสิ่งบางอย่างก็จะเหมือนเดิมอยู่อย่างนั้นวันยังค่ำ ซึ่งบางสิ่งนั้นคงจะรวมถึงนิสัย\nของฮานาโกะด้วย ฮานาโกะจะเป็นคนที่ไม่ชอบการเข้าสังคมขนาดนั้น"

show hanagown smile:
    center
    ypos 1.14
show akira basic_smile:
    right
    ypos 1.14
show bg school_dormlilly at center
with charamove

show lilly invis at left
with None

show lilly basic_smileclosed_paj:
    ypos 1.17
with dissolvecharamove

# "Warned by the sound of crockery against the table as Lilly gently places my drink in front on me, I thank her and take a long sip. Hanako and Lilly are attending to their own, and Akira is quaffing a mug of strong-smelling black coffee."
"พอได้ยินเสียงถ้วยชาที่กระทบกับโต๊ะเมื่อลิลลี่นำน้ำชามาวางให้ตรงหน้าแล้วฉันก็หันไปขอบคุณลิลลี่แล้วยกถ้วยชา\nขึ้นจิบพักหนึ่ง ส่วนฮานาโกะกับลิลลี่ต่างก็ดื่มชากับถ้วยของตัวเองกัน อากิระนั้นกำลังกระดกแก้วดื่มกาแฟดำ\nกลิ่นแรงอยู่"

show akira basic_laugh
with charachange

# aki "You're a lucky bastard, Hisao."
aki "เอ็งนี่มันคนถูกหวยชัด ๆ เลยนะฮิซาโอะ"

# hi "Huh?"
hi "ครับ?"

# "I can't help grimacing at her teasing smile, still visible around the edges of the mug pressed to her lips."
"พอเห็นอากิระที่ยิ้มน้อยยิ้มใหญ่อยู่หลังแก้วกาแฟที่บังปากอยู่แล้วก็รู้สึกใจคอไม่ดีชอบกล"

show akira basic_ending
with charachange

# aki "Seeing my sister in her pajamas, there's a lotta men out there who'd like to be where you are."
aki "ได้เห็นน้องฉันใส่ชุดนอนนี่ ความฝันชายชาตรีหลายคนเลยนะรู้เปล่า"

# "I've seen a lot more than that of her, not that I'd admit it."
"จริง ๆ ก็เห็นมาเยอะกว่านั้นแล้วด้วยอะนะ แต่ไม่บอกหรอก"

show lilly basic_emb_paj
with charachange

# li "Akira!"
li "พี่!"

show akira basic_smile
with charachange

# aki "Hey, I'm just teasing."
aki "น่า ๆ หยอก ๆ"

# "She leans over to me as much as she can, whispering with a sly grin written on her face."
"อากิระเอี้ยวตัวมาเต็มที่แล้วกระซิบพลางยิ้มกรุ้มกริ่ม"

show akira basic_kill
with charachange

# aki "And Hanako, too. You perv."
aki "ไหนจะฮานาโกะอีก ร้ายจริงนะ"

# hi "Hey, it was her idea."
hi "เดี๋ยว งานฉลองนี่ลิลลี่เป็นคนชวนจัดเองนะครับ"

show hanagown distant_blush
with charachange

# ha "Um, I… uh…"
ha "เอ่อ ฉัน… อ่า…"

# "We both look over to her, her face turned to the ground and her hands fidgeting in the lap of her nightgown."
"เราสองคนมองฮานาโกะที่ก้มหน้างุดพลางบิดมือที่ซุกอยู่กับชุดนอนไปมา"

show hanagown smile
with charachange

# ha "If… it's Hisao… I don't mind…"
ha "ถ้า… กับฮิซาโอะแล้ว… ฉันไม่ถือนะ…"

# "Ah, this could be bad. I know Hanako's altogether too innocent to bother reading too much into such a thing, but the expression Akira directs at me is positively stormy."
"เอ่อ แย่แล้วสิ ฮานาโกะอาจจะเป็นคนที่ใสซื่อเกินกว่าจะมองอะไรอย่างนั้นออกก็จริง แต่สีหน้าของอากิระที่มองมา\nทางฉันนั้นช่างน่ากลัวเหลือเกิน"

show lilly basic_concerned_paj
show hanagown normal
with charachange

# li "Um… Akira… please…"
li "เอ่อ… พี่… ขอร้องละ…"

# "It seems Lilly can sense Akira's sudden change in aura just as well as I, even without seeing it for herself."
"ดูท่าว่าลิลลี่เองก็รู้สึกได้ถึงบรรยากาศของอากิระที่เปลี่ยนไปเหมือนอย่างฉัน แม้เธอจะมองไม่เห็นก็ตาม"

show akira basic_boo
with charachange

# "Akira slowly looks away from me, like an attack dog leashed by its owner in the nick of time. I breathe a sigh of relief."
"อากิระเบือนหน้าหนีไปจากฉัน สภาพคล้ายสุนัขที่เตรียมกัดแต่เจ้าของตามมาล่ามไว้ได้ทันพอดี ฉันถอนหายใจ\nด้วยความโล่งอก"

# "I can't think of a more appropriate time to try and change topics than around now."
"ตอนนี้แหละเหมาะที่สุดแล้วที่จะเปลี่ยนเรื่องคุย"

# hi "If you don't mind me asking, Akira, what do you do for a living? I've never seen you out of that suit."
hi "พี่อากิระ ขอถามอะไรหน่อยนะครับ พี่ทำงานอะไรเหรอ เห็นใส่ชุดสูทนั้นตลอดเลย"

show akira basic_laugh
with charachange

# aki "Thinking about what to do with yourself after school's over, eh?"
aki "คิดอยู่ละสิว่าเรียนจบแล้วจะทำอะไรน่ะ"

show akira basic_smile
with charachange

# aki "I'm a lawyer. For the most part, I work in the legal department of the Japanese branch of our family's company."
aki "ทนายน่ะ ส่วนมากก็ทำงานเป็นฝ่ายกฎหมายประจำอยู่ที่บริษัทของครอบครัวฉันสาขาญี่ปุ่นน่ะ"

# aki "The most boring possible answer, I suppose. Law's a pretty dry topic to most people."
aki "คงเป็นคำตอบที่ไม่น่าสนใจที่สุดละมั้ง คนส่วนมากก็คงไม่ค่อยชอบกฎหมายกันเท่าไหร่"

# hi "Kinda."
hi "ก็ประมาณนั้นครับ"

show akira basic_lost
with charachange

# aki "Oi, you're not supposed to agree."
aki "เดี๋ยว ไม่ได้ให้เห็นด้วยเฮ้ย"

show lilly basic_giggle_paj
show hanagown normal
show akira basic_smile
with charachange

# "Lilly gives an amused giggle while holding her teacup and saucer, Hanako quickly joining her."
"ลิลลี่ถือถ้วยชากับจานรองหัวเราะคิกคักชอบใจและฮานาโกะก็หัวเราะตาม"

# "This friendly atmosphere between everyone is something I'd missed while Lilly and Akira were on their trip. While the dealings I had with Hanako didn't help, I think just not having Lilly around changed the mood."
"บรรยากาศเป็นมิตรของทุกคนอย่างนี้นั้นเป็นสิ่งที่ฉันโหยหาเมื่อครั้งที่ลิลลี่กับอากิระไปสกอตแลนด์ ถึงจะมีเรื่อง\nฮานาโกะด้วยก็จริง แต่ยังไงฉันก็คิดว่าที่บรรยากาศเปลี่ยนไปก็แค่เพราะลิลลี่ไม่อยู่นั่นแหละ"

show lilly basic_smileclosed_paj
with charachange

# li "It's nice to be back. I missed you, Hisao, and you too, Hanako."
li "ดีใจจังที่ได้กลับมา ฉันคิดถึงเธอนะฮิซาโอะ คิดถึงเธอด้วยนะฮานาโกะ"

# hi "Same goes for the both of us. I'm guessing your classmates were happy to see you back."
hi "เราสองคนก็คิดถึงเธอเหมือนกันนั่นแหละ คนในห้องเธอก็ดีใจที่เห็นเธอกลับมาใช่มั้ย"

show lilly basic_ara_paj
with charachange

# li "In a manner of speaking, yes."
li "จะว่าดีใจก็ดีใจจ้ะ"

show akira basic_laugh
with charachange

# "Akira's amused snort shows she's well aware of Lilly's attitude towards such figures of speech. I imagine she'd have to be, given how long they've been together."
"เสียงหัวเราะขึ้นจมูกของอากิระบอกชัดว่าเธอรู้ว่าลิลลี่คิดยังไงกับคำพูดเชิงเปรียบเปรยอย่างนั้น ยังไงก็คงรู้แหละ\nเพราะอยู่ด้วยกันมานานแล้วนี่นะ"

show hanagown normal
with charachange

# ha "Did you have fun in Scotland?"
ha "เที่ยวสกอตแลนด์สนุกมั้ย"

$ renpy.music.set_volume(0.1, 2.0, channel="music")

# "For a moment I wonder why she's asking, it having been quite a while since they came back, but then I remember everything that happened. We've simply not had time to look back, what with the exams and our Hokkaido trip."
"ฉันนึกสงสัยอยู่แวบหนึ่งว่าถามทำไม เพราะสองคนนั้นก็กลับมาได้สักพักแล้ว แต่ก็นึกได้ว่าก่อนหน้านี้มีอะไรหลายอย่าง\nเกิดขึ้นจนไม่ทันได้มีเวลาย้อนนึกอะไร ทั้งที่ไปเที่ยวฮกไกโดกับเรื่องสอบ"

show lilly basic_reminisce_paj
show akira basic_annoyed
with charachange

# "Lilly's face goes distant for a moment, and the fact that Akira's first reaction is to look over to her sister doesn't escape me. Nonetheless, she quickly collects herself."
"ลิลลี่ทำหน้าเหม่ออยู่ครู่หนึ่ง และฉันก็สังเกตเห็นด้วยว่าสิ่งแรกที่อากิระทำคือการมองไปทางน้องสาวของเธอ แต่ลิลลี่\nก็ตั้งสติกลับมาเป็นปกติอย่างรวดเร็ว"

$ renpy.music.set_volume(0.8, 0.4, channel="music")

show akira basic_smile
show lilly basic_weaksmile_paj
with charachange

# li "It was… nice. I… we… hadn't met our family in such a long time, so it was a wonderful reunion."
li "ก็… ดีจ้ะ ฉัน… เรา… ไม่ได้อยู่กับครอบครัวมานานแล้ว ถือว่าเป็นการได้อยู่ด้วยกันอีกครั้งที่ยอดเยี่ยมไปเลยละจ้ะ"

show akira basic_boo
with charachange

# aki "Yeah, I guess that's right. Their house being beachside was the best part, though."
aki "อืม ก็คงประมาณนั้น แต่ที่สุดยอดเลยก็คือทะเลที่อยู่ติดบ้านนี่แหละ"

# "From her dismissive tone, I get the feeling Akira doesn't like their family as much as Lilly does."
"ฟังจากน้ำเสียงที่เหมือนไม่ยี่หระอย่างนั้นแล้ว อากิระคงไม่ค่อยชอบคนที่บ้านเหมือนอย่างลิลลี่สักเท่าไหร่"

show lilly basic_giggle_paj
with charachange

# li "You only liked that because you finally had time to play around."
li "ที่พี่ชอบก็แค่เพราะมีเวลาได้เล่นสักทีหรือเปล่า"

show akira basic_ending
with charachange

# aki "Just 'cause I'm the better swimmer…"
aki "เห็นพี่ว่ายน้ำเก่งกว่าหน่อยนี่…"

show lilly basic_smileclosed_paj
with charachange

# li "I don't take after the athletic side of the family, that's all."
li "หนูก็แค่ไม่มีเชื้อออกกำลังกายเหมือนคนในบ้านเอง"

show akira basic_laugh
with charachange

# aki "Well, you can take heart in the fact that you got the height genes at least."
aki "น่า อย่างน้อยเธอก็ยังมีเชื้อส่วนสูงให้ดีใจนะ"

show akira basic_boo
with charachange

# aki "And the bust genes…"
aki "แล้วก็เชื้อหน้าอก…"

show lilly basic_weaksmile_paj
with charachange

# li "That's not really the right kind of thing to say around others…"
li "ของแบบนี้มันใช่เรื่องที่ควรพูดต่อหน้าคนอื่นที่ไหนล่ะพี่…"

# "Though Lilly pretends to scold Akira, she does so with an unmistakable, slightly cheeky grin on her face."
"ถึงลิลลี่จะทำเป็นดุอากิระ แต่ฉันก็เห็นชัดว่าลิลลี่กำลังแสยะยิ้มอยู่เล็กน้อย"

show hanagown distant_blush
with charachange

# "I doubt Akira really minds that, judging from her nonchalant expression. While I don't either, Hanako's looking down and blushing furiously beside me."
"อากิระคงไม่ได้คิดมากอะไรหรอก เห็นทำหน้าสบาย ๆ อย่างนั้น ฉันเองก็ไม่ได้คิดมากเหมือนกัน แต่ฮานาโกะที่นั่ง\nก้มหน้าอยู่ข้าง ๆ กำลังหน้าแดงก่ำอยู่"

# "The sisters' antics aside, their parents really do lead a bourgeois lifestyle."
"พี่น้องคู่นี้ก็ดูตลกดีเหมือนกัน จะว่าไป พ่อแม่ของสองคนนี้ก็ใช้ชีวิตแบบอู้ฟู่อยู่เหมือนกันแฮะ"

# "It seems utterly divorced from the life that Lilly and Akira have lived until now. I suppose practicality must have made the decision for them."
"ถ้าให้เทียบกับวิถีชีวิตของลิลลี่กับอากิระที่ได้อยู่มาจนตอนนี้แล้วดูเหมือนเป็นคนละโลกกันเลย สองคนนี้คง\nให้ความสำคัญกับชีวิตที่ใกล้กับโลกความเป็นจริงมากกว่าละมั้ง"

# "To have come from such a wealthy and well-connected lineage only adds to the almost noble air Lilly seems to have, though. It's a small wonder none of it seems to have rubbed off onto Akira."
"แต่ยังไงการที่มาจากครอบครัวที่ร่ำรวยมีชาติตระกูลอย่างนั้นก็ทำให้ความรู้สึกที่ลิลลี่ดูจะเป็นคนสูงศักดิ์นั้นยิ่งมีมากขึ้น\nซึ่งฉันก็แอบแปลกใจอยู่เหมือนกันว่าทำไมความรู้สึกอย่างนั้นถึงส่งมาไม่ถึงอากิระเลย"

# "They really are as little alike as siblings could be. Their only similarity seems to be their shared confidence, which can be both endearing and a headache at times."
"พี่น้องคู่นี้แทบไม่มีอะไรที่เหมือนกันอย่างพี่น้องตามปกติเลย ที่เหมือนกันก็มีแค่ความมั่นใจ ซึ่งบางทีก็น่าเอ็นดู บางที\nก็น่าปวดหัว"

stop music fadeout 2.0

scene bg school_dormlilly
show lilly basic_smileclosed_paj:
    twoleft
    ypos 1.17
show akira basic_smile:
    tworight
    ypos 1.14
with shorttimeskip

# "Most of the night continues much the same, with Hanako eventually leaving the Satou sisters and me to ourselves as she heads back to her dorm room for a rest."
"เวลาในคืนนั้นไหลผ่านไปตามปกติ จนกระทั่งฮานาโกะขอตัวกลับห้องตัวเองไปนอน ทิ้งไว้เพียงคู่พี่น้องซาโต้กับฉันให้อยู่\nกันตามลำพัง"

# "For a while, only the barely audible sound from Lilly's teacup and saucer can occasionally be heard as she slowly drinks. The silence is strained as Lilly and I wait for the elephant in the room to be addressed."
"มีเพียงความเงียบกับเสียงถ้วยชาลิลลี่ที่กระทบกับจานรองเป็นระยะ ๆ จากการที่เธอค่อย ๆ จิบอยู่พักหนึ่ง เป็น\nความเงียบอันตึงเครียดที่ทั้งลิลลี่ทั้งฉันต่างรอให้เรื่องใหญ่เรื่องนั้นปรากฎขึ้นในบทสนทนา"

show akira basic_boo
with charachange

# aki "So…"
aki "เอาละ…"

$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_dreamy fadein 4.0

show lilly basic_weaksmile_paj
with charachange

# "Lilly dutifully puts her cup down, giving her sister her undivided attention."
"ลิลลี่วางถ้วยชาลงอย่างมีมารยาทให้ความสนใจกับพี่สาวเธอเต็มที่"

# "With Lilly and me on one side of the low table and Akira at the other, this almost feels like a judge passing down a verdict."
"ดูจากสภาพที่ฉันกับลิลลี่นั่งด้วยกันอยู่ฝั่งตรงข้ามกับอากิระแล้ว รู้สึกเหมือนกำลังมานั่งรอผู้พิพากษาลงคำตัดสินเลย"

show akira basic_smile
with charachange

# aki "I hear that you two are going out now?"
aki "ได้ข่าวว่าพวกเธอสองคนคบกันแล้วนี่"

# "I glance sideways at Lilly to confirm her as the source of Akira's knowledge. She gives a gentle nod to Akira, which I mirror in affirmation."
"ฉันเหลือบมองลิลลี่เป็นการยืนยันว่าแหล่งข่าวนั้นใช่เธอหรือไม่ ลิลลี่พยักหน้าเบา ๆ ให้อากิระ ซึ่งฉันก็พยักหน้าตาม\nเป็นการยืนยัน"

# "Deciding that this is the proper time and place to do so, and Akira being the closest figure to a parent Lilly's had for much of her life, I bow deeply with my hands on the floor before me and my head very nearly the same."
"ฉันโค้งต่ำเอามือกับหน้าผากแนบกับพื้นด้วยเห็นว่าตอนนี้นั้นเป็นจังหวะอันดี ทั้งอากิระยังนับได้ว่าเป็นผู้ปกครองที่อยู่\nกับลิลลี่มาค่อนชีวิตอีกด้วย"

# hi "I'll take good care of your sister, Akira. I promise you."
hi "พี่อากิระครับ ผมสัญญาว่าผมจะดูแลน้องสาวของพี่เป็นอย่างดีเลย"

show lilly basic_smile_paj
with charachange

# li "See? He's a lovely young gentleman."
li "เห็นมั้ย ฮิซาโอะเขาก็เป็นสุภาพบุรุษที่แสนดีออก"

# "She must've heard my voice coming from a lower position than usual."
"คงจะได้ยินว่าต้นเสียงมาจากจุดที่ต่ำกว่าปกติ"

# "I slowly bring myself back up, my eyes tentatively looking to Akira from under my brow."
"ฉันเงยหน้าขึ้นช้า ๆ พลางเหลือบมองอากิระที่อยู่เหนือระดับสายตาด้วยความลังเล"

# "To tell the truth, I very much doubt my suited judge will raise any objections. She's very definitely the type to make her disapproval with others well known, something that lends her a measure of respect in my eyes."
"ว่าตามตรง ฉันคิดว่าผู้พิพากษาใส่สูทที่อยู่ตรงหน้าคนนี้คงไม่มีคำคัดค้านอะไรหรอก ฉันมั่นใจว่าอากิระเป็นคนจำพวกที่\nถ้าไม่เห็นด้วยอะไรยังไงก็จะบอกตรง ๆ ไปเลย ซึ่งฉันให้ความนับถือกับอากิระตรงจุดนี้อยู่พอสมควร"

show akira basic_laugh
with charachange

# aki "The old-fashioned kind, huh? Well, he's the kind of person I guessed you'd go for."
aki "พวกหัวโบราณเหรอ อืม ยังไงพี่ก็พอเดาไว้แล้วอะนะว่าเธอคงจะชอบแนวนี้"

show akira basic_smile
with charachange

# aki "I don't have a problem with it, and I wish you two the best. Even if I didn't like it, I couldn't really do anything anyway."
aki "ฉันไม่มีปัญหาหรอก แล้วก็ขอให้มีความสุขกันดีนะ แต่ต่อให้ฉันไม่เอาด้วยจริง ๆ ก็ทำอะไรไม่ได้อยู่ดี"

# "I offer a nod of appreciation to her as Lilly gives a small sigh of relief, likely more out of duty than any actual belief Akira might have had any problems with us being together."
"ฉันพยักหน้าให้อากิระเป็นการขอบคุณพลางถอนหายใจเบา ๆ ซึ่งก็คงเป็นการถอนหายใจไปแบบพอเป็นพิธีนั่นแหละ\nไม่ได้มาจากความโล่งใจว่าอากิระให้เราสองคนคบกันได้หรอก"

show akira basic_evil
with charachange

# aki "I do wonder though… how's the rest of the family taking it, particularly the part residing at Yamaku? Have you told her?"
aki "แต่ฉันอยากรู้ว่า… คนในครอบครัวคนอื่นจะว่ายังไงบ้าง โดยเฉพาะคนที่อยู่ยามากุน่ะ บอกคนนั้นไปหรือยัง"

show lilly basic_listen_paj
with charachange

# "Smiles turn to grimaces as Akira grins downright evilly. Those closest know how to twist the knife best, after all."
"รอยยิ้มของฉันหดหายไปด้วยความสยองทันทีที่อากิระแสยะยิ้มชั่วร้าย คนใกล้ตัวนี่แหละนะที่จะรู้จุดอ่อนเป็นอย่างดี"

show lilly basic_weaksmile_paj
with charachange

# li "“Putting up with it” may be the best term for the situation. Don't you agree, Hisao?"
li "ใช้คำว่า “พอทนได้” น่าจะเข้ากับอารมณ์นั้นที่สุดนะ เธอว่างั้นมั้ยฮิซาโอะ"

# hi "Yeah, that sounds about right. At least she's being reasonable about it."
hi "อื้ม คงประมาณนั้น อย่างน้อยก็ยอมรับฟังด้วยความเข้าใจละนะ"

show akira basic_boo
with charachange

# aki "Good to hear. That girl can be a handful at the best of times."
aki "งั้นก็ดี รายนั้นบางทีก็รับมือยากเหมือนกันนะ"

show akira basic_smile
with charachange

# aki "We sent a few messages back and forth during and just after the trip, and she was already busting my chops for seeing my boyfriend when we came back, after leaving Hideaki for so long. She really does care for the little guy."
aki "ตอนที่ไปเที่ยวกับตอนกลับมาใหม่ ๆ ฉันกับชิซูเนะก็ส่งข้อความหากันอยู่บ้าง แล้วพอตอนกลับมาเห็นแฟนฉันมาด้วย\nก็ดุฉันยกใหญ่เลย หาว่าทิ้งฮิเดอากิไปตั้งนานงี้ ชิซูเนะน่ะเป็นห่วงเจ้าเตี้ยจริงเลยนะ"

# "I cast my mind back to Shizune's odd reaction after telling her about our relationship, but decide not to bring it up. It's no doubt simply born of their mutual antipathy, and Akira's comments only back that up."
"ฉันย้อนนึกไปถึงตอนที่ชิซูเนะทำท่าแปลก ๆ ตอนบอกเรื่องที่ฉันกับลิลลี่คบกัน แต่ฉันก็ตัดใจไม่ยกเรื่องนี้ขึ้นมาคุย ยังไง\nสาเหตุก็คงมาจากการที่สองคนนั้นไม่ถูกกันนั่นแหละ แล้วยิ่งได้ฟังที่อากิระพูดแล้วฉันก็ยิ่งมั่นใจ"

show akira basic_boo
with charachange

# aki "Well then, that's settled. Gotta get to work early tomorrow, so I'd better be off."
aki "โอเค งั้นก็ตามนั้น ไปก่อนละนะ เดี๋ยวพรุ่งนี้ต้องไปทำงานแต่เช้า"

show akira basic_smile at tworight
with charamove

# "She rises from the table with a grunt, her hand on her knee to push herself up. I just notice Akira's eyes lingering on Lilly for a couple of seconds before turning away, as she begins to take her leave."
"อากิระหยัดตัวกับเข่าลุกขึ้นยืนพร้อมส่งเสียงโอดโอย ฉันเพิ่งสังเกตเห็นว่าอากิระยังมองลิลลี่อยู่อีกสักระยะหนึ่งแล้ว\nหันหน้าเดินออกไป"

hide akira
with charaexit

# "After she walks out the door, she stops and looks up thoughtfully before turning to us one last time."
"พอเดินผ่านประตูออกไปแล้วอากิระก็หยุดยืนแหงนหน้ามองครุ่นคิดก่อนจะหันมามองทิ้งทวน"

show akira invis:
    xanchor 0.5 xpos 1.0
with None

show akira basic_lost:
    xpos 0.9
with dissolvecharamove

# aki "Oh yeah, I almost forgot to tell you."
aki "อ้อ จริงสิ เกือบลืมบอก"

show akira basic_ending
with charachange

# aki "Use protection. Every time."
aki "ป้องกันด้วยนะ ทุกครั้งเลย"

# "I gag violently on the tea in my mouth. Contrary to my own, Lilly's composure holds perfectly as she seems entirely unfazed. I'm kind of impressed."
"ฉันสำลักแทบเป็นแทบตายกับน้ำชาที่อยู่ในปาก ส่วนลิลลี่ยังคงนิ่งสงบไม่สะทกสะท้านใด ๆ ต่างจากฉัน น่าทึ่ง\nอยู่เหมือนกันนะเนี่ย"

show lilly basic_smile_paj
with charachange

# li "We are, don't worry."
li "แน่นอนอยู่แล้ว พี่ไม่ต้องห่วง"

show akira basic_smile
with charachange

# aki "'Atta girl. Seeyas."
aki "ต้องงี้สิ เจอกัน ๆ"

show akira invis:
    xanchor 0.5 xpos 1.0
with dissolvecharamove

hide akira
with None

# "And with that she turns and strides away, a hand held high as she disappears into the darkened hallway, closing the door behind her."
"แล้วอากิระก็หันหลังกลับก้าวฉับ ๆ ออกไปพลางยกมือบอกลาหายไปกับโถงทางเดินอันมืดมิดหลังจากที่ปิดประตูไปแล้ว"

show lilly basic_smile_paj:
    center
    ypos 1.17
show bg school_dormlilly at bgright
with charamove

# "The most reaction I can muster is flopping forwards onto the table, completely drained of energy and truly exhausted by her. Lilly's ability to hold her own against that suited devil is something I admire."
"ฉันได้แต่ฟุบตัวลงกับโต๊ะด้วยความเหนื่อยอ่อนเพราะถูกอากิระสูบพลังไปจนเกลี้ยงแล้ว ฉันละนับถือจริง ๆ ที่ลิลลี่รับมือ\nกับปีศาจในชุดสูทคนนั้นได้ดีเหลือเกิน"

# hi "She really is incredibly blunt. I don't think I'll ever be able to keep up with your sister's energy."
hi "เป็นคนตรงไปตรงมามากเลยนะ ฉันว่าฉันรับมือกับนิสัยของพี่เธอไม่ได้แน่ ๆ"

show lilly basic_smileclosed_paj_close:
    center
    ypos 1.1
with characlose

# "As I feel Lilly's soft hand come to rest on my own, I roll my head to the side to see her gently smiling. For a long time, we simply sit beside each other silently."
"พอรู้สึกได้ถึงสัมผัสจากมือของลิลลี่ที่อยู่หลังมือฉันก็เอียงคอมองจนเห็นรอยยิ้มอันอ่อนโยนของเธอ พวกเรานั่งเงียบ ๆ\nเคียงกันอยู่เนิ่นนาน"

# "Given her unquestionably unusual height, she is pretty much exactly as tall as I am; probably a couple of centimeters higher if anything. Like this, she appears even taller."
"ปกติลิลลี่ก็เป็นคนตัวสูงมากอยู่แล้ว สูงพอ ๆ กับฉันหรือไม่ก็สูงกว่าฉันไปสักสองสามเซนติเมตรเลยด้วยซ้ำ แล้วพออยู่\nแบบนี้ลิลลี่ยิ่งดูตัวสูงขึ้นไปอีก"

# "The feeling of her pale, soft hand against mine is a pleasant one, as is the sight of the thin silken pajamas she wears, showing her curves and collarbone."
"สัมผัสอันอ่อนนุ่มจากมือขาวนวลที่ต้องมือฉันอยู่นั้นชวนให้ผ่อนคลาย เช่นเดียวกับภาพเธอที่ใส่ชุดนอนผ้าไหมซึ่ง\nเผยส่วนโค้งเว้ากับกระดูกไหปลาร้าของเธอ"

show lilly basic_smile_paj_close
with charachange

# li "You do get on well though, even if you do say that."
li "ถึงเธอจะพูดอย่างนั้น แต่เธอสองคนก็เข้ากันดีอยู่นะ"

# hi "I guess. You know, you two are a lot more alike than I first thought when I met you."
hi "มั้งนะ เออ เธอสองคนนี่เหมือนกันกว่าที่ฉันเคยคิดตอนที่เจอพวกเธอครั้งแรกเสียอีกนะ"

show lilly basic_cheerful_paj_close
with charachange

# li "Then it's a good thing I quickly stopped you from going after her, isn't it?"
li "งั้นก็นับว่าดีแล้วใช่ไหมล่ะที่ฉันรีบห้ามเธอไม่ให้ไปตามจีบพี่น่ะ"

# "Though she jokes about it, my assessment of my inability to keep up with Akira, either physically or mentally, was quite in earnest."
"ถึงลิลลี่จะพูดหยอกอย่างนั้น แต่ที่ประเมินว่าตัวเองตามอากิระไม่ทัน—ไม่ว่าจะพลังกายหรือพลังใจก็ตาม—นั้นฉันพูด\nด้วยความจริงจัง"

# "Lilly's slow-paced and ladylike, almost motherly, nature is perhaps the single thing that helped me most in my first weeks at Yamaku."
"ลิลลี่นั้นเป็นคนที่ทำอะไรอย่างค่อยเป็นค่อยไป มีความเป็นสุภาพสตรีจนคลับคล้ายความเป็นแม่ด้วยซ้ำ เหล่านี้เอง\nคงจะเป็นสิ่งหลัก ๆ ที่ช่วยให้ฉันผ่านสัปดาห์แรกที่ยามากุมาได้"

# "Come to think of it…"
"จะว่าไปแล้ว…"

# hi "Wait… since when were we using protection?"
hi "เดี๋ยว… เราป้องกันตอนไหนนะ"

show lilly basic_pout_paj_close
with charachange

# "As I give a curious look to my side, Lilly's cheeks puff out as she huffs at me."
"ฉันหันมองลิลลี่ด้วยความสงสัย เธอทำแก้มป่องพร้อมทำเสียงฮึดฮัด"

# li "Unlike you, I remembered. The packet is in the cupboard next to the sink."
li "ฉันไม่ได้ลืมเหมือนเธอสักหน่อย ยาอยู่ในตู้ข้างอ่างล้างหน้าแน่ะ"

# "So, I'm not the only one of us that takes a pill. In hindsight, I feel rather thoughtless for not remembering at all and leaving it to Lilly."
"สรุปว่าฉันไม่ได้กินยาอยู่คนเดียวสินะ แต่พอลองย้อนคิดดูแล้ว ตัวฉันเองก็ประมาทอยู่เหมือนกันที่ไม่ได้นึกอะไรเลย\nแล้วปล่อยให้เป็นหน้าที่ของลิลลี่ทั้งหมดอย่างนั้น"

# "Looking over to the cupboard she mentions, I notice again the knee-high piles of books around us that were here the other times I'd visited. For the most part, they're lined up against the wall to give a little more room around the table."
"พอมองไปทางตู้ที่ลิลลี่พูดถึงแล้วก็ไปสะดุดตาเข้ากับกองหนังสือความสูงประมาณหัวเข่าที่ตั้งอยู่รอบตัวเหมือนอย่าง\nที่ฉันมาห้องนี้เมื่อคราวที่แล้วอีกครั้ง ซึ่งส่วนมากก็เรียงชิดกำแพงเผื่อพื้นที่ที่อยู่รอบ ๆ โต๊ะ"

# hi "Why don't you get a bookshelf for your books? It's odd to see books just piled around, especially given that your room looks so neat and orderly otherwise."
hi "ทำไมไม่หาตู้หนังสือมาสักใบล่ะ เห็นหนังสือกอง ๆ กันอย่างนี้แล้วก็แปลก ๆ อยู่นะ เพราะนอกนั้นห้องเธอก็ออกจะ\nเป็นระเบียบสะอาดตาดีอยู่แล้วแท้ ๆ"

show lilly basic_smileclosed_paj_close
with charachange

# li "They're easier to find this way; I know exactly which pile each book is in."
li "เรียงแบบนี้มันหาง่ายกว่าน่ะจ้ะ ฉันจำได้ว่ากองไหนมีหนังสืออะไรบ้าง"

# hi "Wouldn't you still know that after putting each set on a different shelf?"
hi "ก็ถ้าเอาไปเรียงเป็นชุด ๆ ไว้กับชั้นหนังสือก็น่าจะยังจำได้เหมือนเดิมนี่"

show lilly basic_weaksmile_paj_close
with charachange

# li "That may be, but…"
li "ก็น่าจะ แต่ว่า…"

# "So she's not immune to bouts of laziness after all."
"ลิลลี่เองก็มีจังหวะที่ขี้เกียจเหมือนกันสินะ"

# hi "You have so many of them, it's kind of a shame we can't share our book sets despite both of us reading so much."
hi "หนังสือเธอเยอะนะ แต่เสียดายที่แลกกันอ่านไม่ได้ ทั้งที่เป็นคนชอบอ่านเหมือนกันแท้ ๆ"

show lilly basic_giggle_paj_close
with charachange

# "She gives a short giggle."
"ลิลลี่หัวเราะน้อย ๆ"

# hi "Come to think of it, why do you order your books through Yuuko? I imagine there'd be plenty of sites that you could order books in Braille from, especially in English Braille. There are a lot of text-to-speech programs, too."
hi "จะว่าไป ทำไมเธอถึงสั่งหนังสือกับยูโกะล่ะ น่าจะมีหลายเว็บอยู่นะที่ขายหนังสืออักษรเบรลล์น่ะ ยิ่งฉบับภาษาอังกฤษ\nนี่น่าจะมีเยอะเป็นพิเศษเลย แถมโปรแกรมแปลงข้อความเป็นเสียงก็มีถมไป"

show lilly basic_displeased_paj_close
with charachange

# "She turns her head slightly away from me, which strikes me as somewhat surprising."
"ลิลลี่เบือนหน้าหนีไปจากฉันเล็กน้อยจนฉันรู้สึกแปลกใจพอสมควร"

# li "I'm just… not all that good with computers. I'm all right with typewriters and braillers… but that's about it."
li "พอดีฉัน… ไม่ค่อยสันทัดเรื่องคอมพิวเตอร์สักเท่าไหร่น่ะ ฉันใช้พิมพ์ดีดกับเครื่องพิมพ์ดีดอักษรเบรลล์เป็นก็จริง…\nแต่ก็เป็นแค่นั้นแหละ"

# "Her tone almost makes me chuckle. She's a prideful person, so admitting something like that must be difficult."
"น้ำเสียงลิลลี่นั้นทำให้ฉันนึกแค่นหัวเราะ ลิลลี่เป็นคนที่ภาคภูมิในตัวเองมาก การที่จะยอมรับเรื่องทำนองนั้นคงเป็นอะไร\nที่ลำบากใจน่าดู"

# "So, Lilly's the low-tech kind of person. Given her old-fashioned personality, it's not really a stunning surprise."
"ลิลลี่เป็นคนจำพวกที่ไม่ถนัดกับเทคโนโลยีนี่เอง ซึ่งดูจากลักษณะนิสัยที่เป็นคนยึดถืออะไรแบบดั้งเดิมแล้วก็ไม่น่า\nแปลกใจสักเท่าไหร่"

# hi "I wouldn't worry about it. A lot of people aren't really that good with them, so it's not that unusual."
hi "ไม่เป็นไรหรอก คนที่ไม่ถนัดกับของพวกนี้ก็มีเยอะแยะ ไม่ได้แปลกอะไรขนาดนั้น"

show lilly basic_concerned_paj_close
with charachange

# li "“That” unusual…"
li "แปลก “ขนาดนั้น”…"

# "Now she's even more depressed. It feels like I'm twisting the knife, rather than healing her wounds."
"ทีนี้ก็หดหู่กว่าเดิมอีก รู้สึกเหมือนที่พูดไปนี่ไม่ได้ช่วยอะไรเลย ยิ่งเป็นการซ้ำเติมอีกต่างหาก"

show lilly basic_weaksmile_paj_close
with charachange

# "With a bit of squirming I shuffle my way closer to her, tentatively putting one hand around her waist to hug her. I'm still not really used to this kind of physical affection, but Lilly seems to like it."
"ฉันขยับตัวยุกยิกเข้าไปหาลิลลี่แล้วโอบเอวกอดลิลลี่ไว้ด้วยท่าทางเก้ ๆ กัง ๆ ฉันยังไม่ค่อยชินกับการแสดงความรัก\nทางกายแบบนี้เท่าไหร่ แต่ดูเหมือนลิลลี่จะชอบ"

scene ev lilly_kissing
with whiteout

# "Lilly smiles as she turns to face me, a kiss being the reward for giving in to her. She draws me in, brushing my upper lip with hers before pressing against both."
"ลิลลี่หันหน้ามายิ้มให้ฉันแล้วจูบเป็นรางวัลที่ฉันยอมง้อเธอ เธอดึงตัวฉันเข้าไปแล้วแตะริมฝีปากบนเข้ากับฉัน\nก่อนจะทาบทับเข้ามาจนเต็มปาก"

# "This way, every one of my senses is filled with her. The barely perceptible scent of her hair, her taste as her tongue fleetingly touches mine, the tenderness of her lips, the image of her filling my mind, the total silence apart from her faint breath…"
"พอทำเช่นนี้แล้วทุกประสาทสัมผัสของฉันก็ถูกเติมเต็มด้วยเธอ กลิ่นหอมจาง ๆ จากผมที่จางจนแทบไม่ได้กลิ่น\nรสของเธอจากลิ้นที่เข้ามาสัมผัสกับลิ้นฉันอยู่เพียงชั่วแล่น ความอ่อนนุ่มของริมฝีปากเธอ ภาพของเธอที่หลั่งไหล\nเข้ามาในความคิด ความเงียบสงัดที่มีเพียงเสียงหายใจแผ่วของเธอแทรก…"

# "We may have kissed before, but even if this is more a kiss of simple affection than anything, it's still a new and pleasant sensation."
"เราเคยจูบกันแล้วก็จริง แต่จูบครั้งนี้นั้นไม่ใช่เพียงการจูบเพื่อแสดงความรักเท่านั้น เป็นความรู้สึกที่ไม่เคยสัมผัสมาก่อน\nและช่างเป็นความรู้สึกที่ดี"

scene bg school_dormlilly at bgright
show lilly basic_cheerfulblush_paj_close:
    center
    ypos 1.1
with locationchange

# "Judging from her vivid blush as she pulls back, it's obvious she feels the same as I do; even if we're entirely alone, it still feels a little embarrassing to open up to each other this much. "
"ดูจากใบหน้าของลิลลี่ที่แดงก่ำอย่างเห็นได้ชัดตอนที่เธอผละออกแล้ว เธอคงจะคิดเหมือนอย่างเดียวกันกับฉัน ต่อให้เรา\nอยู่ด้วยกันสองต่อสองก็จริง แต่การจะเปิดใจทำอะไรอย่างนี้กันก็ยังชวนให้รู้สึกขัดเขินอยู่เล็กน้อย"

show lilly basic_smileclosed_paj_close
with charachange

# li "If we take everything day by day, I think that would be for the best. Small steps, right?"
li "ถ้าเราค่อย ๆ ทำอะไรไปด้วยกันทุก ๆ วัน แบบนั้นน่าจะดีที่สุดนะ ค่อยเป็นค่อยไป เนอะ"

# hi "Yeah. Just small steps."
hi "อื้ม ค่อยเป็นค่อยไป"

# "We have plenty of time to be together, even after the school year is over. As long as we move together, I think everything will work out okay; neither of us is going anywhere soon, after all."
"เรายังมีเวลาให้อยู่ด้วยกันอีกมาก แม้แต่ช่วงหลังเรียนจบแล้วก็ด้วย ตราบใดที่เราได้อยู่ที่เดียวกัน ทุกอย่างก็น่าจะลงตัว\nยังไงเสีย เราสองคนก็ไม่มีใครที่จะไปไหนกันอยู่แล้ว"

# "For now, I'm just thankful for this small moment in time we can spend together."
"ตอนนี้ฉันเพียงรู้สึกยินดีกับช่วงเวลาเล็ก ๆ น้อย ๆ ที่เราได้อยู่ร่วมกันในตอนนี้"

stop music fadeout 2.0

scene black
with dissolve

#***********************


label th_L23:

scene bg school_nursehall
with locationchange

# "I stand unmoving in front of the door to the nurse's office for what feels like at least a dozen minutes or so."
"ฉันยืนนิ่งอยู่หน้าประตูห้องพยาบาลอยู่นานสักสิบนาทีกว่า ๆ เห็นจะได้"

# "It's not like I never entered the small, beige room before, nor is it because of any feeling of childlike anxiety over the visit."
"ก็ไม่ใช่ว่าเพิ่งมาได้เข้าห้องแคบ ๆ สีเบจเป็นครั้งแรกสักหน่อย แล้วก็ไม่ใช่ความรู้สึกกลัวหมอเหมือนอย่างเด็ก ๆ ด้วย"

# "Maybe it's because the nurse's office is akin to a confessional, an admission that my body is flawed. The knowledge that such a fact is kept entirely confidential between the nurse and me hardly lessens the feeling."
"อาจจะเพราะการมายังห้องพยาบาลนั้นก็เปรียบได้กับการยอมรับสารภาพว่าร่างกายฉันนั้นบกพร่อง แม้จะเป็นสิ่งที่เป็น\nความลับระหว่างฉันกับคุณพยาบาล แต่ฉันก็ไม่ได้รู้สึกสบายใจขึ้นเลย"

# "Remembering that the bell to signal the end of lunch break will sound soon, I give a sigh and open the door. The burden will stay with me just this while longer."
"พอนึกได้ว่าอีกไม่นานระฆังหมดพักเที่ยงจะดังแล้วฉันจึงถอนหายใจยอมเปิดประตูเข้าไป ฉันคงต้องแบกรับภาระนี้\nต่อไปอีกหน่อย"

play music music_nurse fadein 0.5

scene bg school_nurseoffice
show nurse neutral at center
with locationchange

# nk "Well now, if it isn't Nakai. Good to see you."
nk "อ้าว นากาอิหรือ สวัสดี"

show nurse grin
with charachange

# nk "Or bad, I guess, considering that I'm a nurse."
nk "หรือไม่ดี ก็ฉันเป็นพยาบาลนี่นะ"

# "He gives a small laugh, amused at his little joke. I find his humor lacking and somewhat off, but the fact that he can make light of such a situation is perhaps comforting, or at least distracting."
"คุณพยาบาลแค่นหัวเราะกับมุกฝืด ๆ ของตัวเอง รู้สึกว่ามุกแต่ละอย่างของเขานั้นทั้งฝืน ๆ ทั้งแปลก ๆ แต่เอาเป็นว่า\nการที่ทำให้บรรยากาศผ่อนคลายได้อย่างนี้ก็คงเป็นเรื่องที่ชวนให้สบายใจดี หรืออย่างน้อยก็จะได้ไม่ต้องคิดมาก"

show nurse neutral
with charachange

# "His brief episode of entertainment over, he claps his hands together and gets down to business. I take a seat as he gestures for me to do so."
"หมดเวลาสนุกของแล้ว คุณพยาบาลตบมือแล้วทำท่าจริงจัง ฉันนั่งลงไปตามที่เขาผายมือเชิญชวน"

# "I wish the classrooms had seats this comfortable. I can feel my mind wandering as my eyes quickly scan the room, distracted by all the small changes since I last came."
"ถ้าเก้าอี้ที่ห้องเรียนนั่งสบายอย่างนี้ก็ดีสิ จิตใจฉันเริ่มล่องลอย สายตากวาดมองรอบห้องดูสิ่งเล็ก ๆ ที่เปลี่ยนไปนับจาก\nตอนที่ฉันมาครั้งล่าสุด"

show nurse fabulous
with charachange

# nk "Alrighty, so what brings you here? I haven't seen you often, so I assume your health's been good so far?"
nk "เอาละ แล้วมีอะไรเหรอถึงได้มาหา ไม่ค่อยได้เจอหน้าเธออย่างนี้ แปลว่าที่ผ่านมาสุขภาพก็ปกติดีสินะ"

# hi "Well, mostly."
hi "ก็พอสมควรครับ"

show nurse neutral
with charachange

# nk "I see."
nk "อย่างนี้นี่เอง"

# "His smile drops as I trail off. I feel slightly guilty about it. It's these moments where I can't rationally call myself “normal” that make me so reluctant to see the nurse. They're an admission that I'm different from everyone else."
"รอยยิ้มของเขาหายไปเมื่อเสียงฉันอ่อยลง รู้สึกผิดอยู่หน่อย ๆ แฮะ จังหวะที่ตามหลักแล้วฉันบอกว่าตัวเอง “ปกติ” ไม่ได้\nแบบนี้นี่แหละที่ทำให้ฉันไม่อยากมาหาคุณพยาบาลเลย เพราะเป็นการยอมรับว่าฉันนั้นแตกต่างจากคนอื่น"

stop music fadeout 5.0

# hi "While I was on a trip during the long weekend, I had a few problems with my heart."
hi "ช่วงที่ผมไปเที่ยววันหยุดยาวผมมีปัญหาเรื่องหัวใจนิดหน่อยน่ะครับ"

# "He hums very seriously and nods as he does so, urging me to go on."
"คุณพยาบาลพยักหน้าทำเสียงฮึมฮัมจริงจังให้ฉันพูดต่อ"

# hi "I think it was… yeah, it was as I was walking a fairly long distance. I think the right term for it is a heart flutter."
hi "ผมว่าน่าจะเพราะ… อืม เพราะผมเดินไกลพอสมควรเลย น่าจะเป็นอาการหัวใจเต้นผิดจังหวะนะครับ"

# hi "I suddenly went weak at the knees and felt almost like I was having a small heart attack, but it passed in about half a minute. Even afterward though, I felt pretty fatigued and nauseous."
hi "อยู่ ๆ เข่าผมก็อ่อน แล้วก็แน่นหน้าอกเหมือนหัวใจวายอยู่แวบหนึ่ง แต่ไม่ถึงนาทีก็หาย แต่ว่าหลังจากนั้นผมก็ยังรู้สึก\nเพลีย ๆ กับคลื่นไส้อยู่"

show nurse concern
with charachange

# nk "Hrm. Not good. Not good at all."
nk "อืม ไม่ดี ไม่ดีเลยนะ"

# nk "That was how many days ago, exactly? Did you do anything unusual, aside from exerting yourself, before the episode? Were you taking your medication properly?"
nk "แล้วผ่านมากี่วันแล้วนับตั้งแต่ที่เป็น ก่อนเป็นได้ไปทำอะไรแปลก ๆ มามั้ย นอกจากออกแรงหนักที่เธอว่าน่ะ กินยา\nเรียบร้อยดีหรือเปล่า"

# "The nurse switches from awkward jokester to serious health professional mode, rattling off questions, making notes, and calling up stuff on his computer."
"คุณพยาบาลเปลี่ยนโหมดจากคนเล่นมุกแบบแห้ง ๆ เป็นบุคลากรทางการแพทย์ผู้จริงจังคอยยิงคำถาม จดนั่นนี่ เรียก\nข้อมูลทั้งหลายจากคอมพิวเตอร์"

# "I tell him about my forgetting to take my pills that morning, and the preceding evening. It was a stupid thing to do, but I can't change anything about it now, except answer honestly and bite the bullet."
"ฉันบอกคุณพยาบาลไปว่าเย็นก่อนวันนั้นกับเช้าวันนั้นฉันลืมกินยา ซึ่งเป็นอะไรที่บ้าบอ แต่จะให้แก้ไขอะไรก็คงไม่ทัน\nแล้ว คงได้แต่ตอบไปตามจริงแล้วก็รับผลกรรมไปนั่นแหละ"

# "His seriousness evolves into a frown, and the talk evolves into an instant checkup."
"ความจริงจังของคุณพยาบาลแปลงออกมาเป็นสีหน้าที่มีคิ้วขมวดอยู่ จากการคุยก็แปรเป็นการตรวจร่างกายแบบคร่าว ๆ"

hide nurse
with shorttimeskip

# "I finish buttoning up my shirt and again get motioned to take a seat in front of the nurse."
"พอติดกระดุมเสร็จคุณพยาบาลก็ผายมือให้มานั่งตรงหน้าอีกรอบ"

show nurse concern at center
with charaenter

# nk "Is this the first heart problem you've had since coming to Yamaku?"
nk "ตั้งแต่มาเรียนที่นี่ ครั้งนี้ครั้งแรกเลยหรือเปล่าที่มีปัญหาเรื่องหัวใจน่ะ"

# hi "I've had short pains in my chest before, just a couple of times, but they were more discomfort than anything like this."
hi "ก่อนหน้านั้นก็มีปวดจี๊ด ๆ อยู่บ้างครั้งสองครั้งครับ แต่ก็แค่รู้สึกแน่น ๆ นิดหน่อย ไม่ได้หนักเหมือนครั้งนี้"

# "He leans back in his chair, briefly resembling a white-coated Poirot as he mulls over the mysterious case of the heart flutter."
"คุณพยาบาลเอนตัวพิงพนักเก้าอี้ แวบหนึ่งลักษณะเขาดูคล้ายนักสืบปัวโรต์ที่ใส่ชุดขาวผู้ซึ่งกำลังพิเคราห์คดีปริศนา\nเรื่องหัวใจเต้นผิดจังหวะ"

# "Moving his lips from side to side to show he's thinking, his nonexistent mustache wiggling, he eventually comes to a conclusion."
"เขาเม้มปากไปมาทำท่าครุ่นคิดพลางกระดิกหนวดที่มองไม่เห็นอยู่ จนในที่สุดเขาก็ได้ข้อสรุป"

show nurse fabulous
with charachange

play music music_nurse fadein 1.0

# nk "Well, you survived it. That's always on the plus side."
nk "อืม เธอก็ยังรอดมาได้ ซึ่งนับว่าดีแล้วละ"

# "I blink at this one, then notice the nurse wearing his “got you” face."
"ฉันกะพริบตาปริบ ๆ จนกระทั่งเห็นสีหน้าทำนองว่า “ไงละ” ของคุณพยาบาล"

# "It's actually somewhat reassuring. I don't think he would crack jokes if things were really serious, so I keep silent and take my lumps."
"ก็ค่อยใจชื้นขึ้นมาหน่อย เพราะถ้าหนักจริงคุณพยาบาลคงไม่พูดหยอกเล่นอะไรอย่างนี้ ฉันจึงนั่งทนฟังเขาบ่นอยู่เงียบ ๆ"

show nurse neutral
with charachange

# nk "I'll have a talk with your doctor, but right now I suspect it's simply due to physical exertion."
nk "เดี๋ยวฉันต้องคุยกับหมอประจำตัวเธอหน่อย แต่ตอนนี้ฉันคิดว่าน่าจะเป็นแค่อาการจากการออกแรงมากไปเฉย ๆ นะ"

# nk "Have you been keeping up with regular light exercise like I directed you to?"
nk "แล้วได้คอยออกกำลังกายเบา ๆ อย่างที่ฉันแนะนำไปหรือเปล่า"

# hi "I make sure to walk a reasonable amount every day. It's usually enough to work up a bit of a sweat, but then again I'm not really as fit as I used to be."
hi "ผมคอยเดินเป็นประจำอยู่ทุกวันครับ ปกติก็เดินจนได้เหงื่อเลย แต่ก็นะครับ เดี๋ยวนี้ผมไม่ค่อยฟิตเหมือนแต่ก่อนแล้ว"

# nk "That should be enough, then. The main thing to keep in mind is to do regular low-stress exercise, not short bursts of sprinting and such."
nk "งั้นแค่นั้นก็น่าจะพอแล้วละ หลัก ๆ คือพยายามออกกำลังกายเบา ๆ ให้สม่ำเสมอ ไม่ใช่อยู่ ๆ ก็ไปวิ่งสี่คูณร้อยงี้"

# hi "I understand. Since leaving the hospital I've been a lot more focused on my studies, partly to take my mind off not being able to do more physical things."
hi "รับทราบครับ ตั้งแต่ออกโรงพยาบาลมาส่วนมากผมก็จดจ่ออยู่กับการเรียนอย่างเดียวเลย ส่วนหนึ่งก็เพราะจะได้\nลืม ๆ ไปว่าตัวเองไปออกแรงทำอะไรหนัก ๆ ไม่ได้แล้ว"

show nurse grin
with charachange

# nk "It's good to hear you're coping well. Sudden lifestyle changes can be hard at the best of times, so I'm pleased to hear that you sound like you have everything in order. Almost everything, that is."
nk "ปรับตัวได้ดีอย่างนี้ก็ดีแล้วละ บางทีการต้องมาเปลี่ยนแนวทางการใช้ชีวิตแบบกะทันหันมันก็ลำบากเหมือนกัน ต่อให้\nสภาพแวดล้อมอะไรทั้งหลายจะดีก็เถอะ เพราะงั้นพอเธอเล่าเหมือนทุกอย่างลงตัวแล้วฉันก็เลยโล่งใจ ไม่ทุกอย่างหรอก\nแต่ก็เกือบ"

show nurse neutral
with charachange

# nk "Nevertheless, I want to keep a close eye on you for a while, just for observation's sake. Just to make sure things aren't going downhill, you understand."
nk "แต่ยังไงฉันก็ขอจับตาดูเธออีกสักระยะนะ แค่สังเกตการณ์เฉย ๆ ประมาณว่าดูให้แน่ใจว่าอะไร ๆ จะไม่แย่ลงไปอีกน่ะ\nเธอคงเข้าใจ"

# "That's something I really didn't want to hear. Since coming to Yamaku, all I've wanted to do is live as normal a life as possible."
"ไม่ค่อยอยากได้ยินคำนี้เลยแฮะ ตั้งแต่ที่ได้ย้ายมาอยู่ที่ยามากุ สิ่งเดียวที่ฉันหวังเลยก็คือการใช้ชีวิตให้เหมือนอย่างปกติ\nที่สุด"

# "“Observation” was one of the words I came to hate most during my hospital stay. For so long I felt as if I could have just walked straight out the hospital doors, if not for that “observation” the doctors wanted so dearly."
"ฉันอยู่โรงพยาบาลมาจนเกลียดคำว่า “สังเกตการณ์” เข้าไส้ ฉันคิดอยากเดินดุ่ม ๆ ออกจากโรงพยาบาลไปเสียทั้ง\nอย่างนั้นมาตลอด ถ้าไม่ติดตรงที่ว่าคุณหมออยากจะ “สังเกตการณ์” ฉันเหลือเกิน"

# hi "Sure. Should I come in more often?"
hi "ได้ครับ แล้วจะให้ผมมาหาบ่อยขึ้นอีกยังไงเหรอครับ"

# "He checks the calendar next to his computer, which seems to inflict on him a nasty case of furrowed brow. He spins back towards me after that."
"คุณพยาบาลดูปฏิทินที่อยู่ข้างคอมพิวเตอร์แล้วทำหน้านิ่วคิ้วขมวด พอดูเสร็จก็หันมาหาฉัน"

show nurse concern
with charachange

# nk "The summer holidays are a bit of a pain, considering the timing…"
nk "ปิดเทอมฤดูร้อนคงลำบากหน่อย จังหวะน่าจะไม่ค่อยลงตัว…"

# nk "I'll check with your doctor to try and get a better handle on the situation and see how he wants to proceed, but I think you should just take things slowly and carefully for now."
nk "เดี๋ยวฉันถามหมอของเธอให้อีกที จะได้ดูว่าสถานการณ์ตอนนี้เป็นยังไงบ้าง แล้วก็จะได้ถามด้วยว่าจะเอายังไงต่อ\nแต่ตอนนี้เอาเป็นว่าเธออย่าเพิ่งไปบุ่มบ่ามทำอะไรแล้วกัน"

# nk "What you're describing doesn't immediately sound like a recurring event, but it won't hurt to slow down a bit for a while, just to make sure."
nk "ที่เธอเล่ามาเหมือนจะไม่ใช่อะไรที่จะเกิดขึ้นซ้ำ ๆ ได้ แต่อย่างน้อย เพื่อความแน่ใจ ค่อย ๆ ดูอาการไปสักระยะ\nก็ไม่เสียหาย"

# hi "What should I do for today?"
hi "แล้ววันนี้ผมต้องทำอะไรยังไงต่อเหรอครับ"

# "He looks over my shoulder at a clock hanging over the door. I'd never have noticed it if I hadn't followed his gaze."
"คุณพยาบาลมองผ่านฉันไปทางนาฬิกาที่แขวนอยู่ตรงประตู ถ้าไม่มองตามฉันคงไม่รู้ว่ามีนาฬิกาอยู่ตรงนั้นด้วย"

show nurse fabulous
with charachange

# nk "It's nearly time for school to be over, so you may as well just leave early."
nk "โรงเรียนใกล้เลิกแล้ว งั้นลาเลยแล้วกัน"

# "He gives me a sly wink, making sure that I understand he's doing me a favor."
"คุณพยาบาลขยิบตาส่งซิกเป็นการบอกให้เข้าใจตรงกันว่ากำลังช่วยฉันอยู่"

# hi "Well, nurse's orders. Thanks."
hi "พยาบาลสั่งให้ลาสินะครับ ขอบคุณครับ"

show nurse grin
with charachange

# nk "That's what I'm here for, after all."
nk "ก็นั่นมันหน้าที่ฉันเลยนี่"

show nurse neutral
with charachange

# nk "I know you might not want to hear this, but you can't ignore your condition. Don't hesitate to see me if you have any further problems, or if you just have anything you want to ask. Bye."
nk "เธออาจจะไม่อยากได้ยินคำนี้สักเท่าไหร่ แต่เธอจะเมินอาการตัวเองไม่ได้นะ ถ้าเป็นอะไรอีกหรือมีอะไรอยากถาม\nก็มาหาฉันได้เลยไม่ต้องเกรงใจ บาย"

hide nurse
with charaexit

# "He spins around and gets back to typing on the computer in front of him. I suppose I'll just read before waiting for Lilly by the gate, considering I don't have much else to do."
"คุณพยาบาลหมุนตัวไปพรมนิ้วลงบนแป้นพิมพ์ตรงคอมพิวเตอร์ต่อ งั้นก็อ่านหนังสือก่อนไปรอลิลลี่ที่ประตูหน้าโรงเรียน\nแล้วกัน ยังไงก็ไม่มีอะไรให้ทำอยู่แล้ว"

stop music fadeout 3.0

# "Even as I leave, his words echo in my mind. My condition isn't something as limiting as many of the others here in Yamaku, and I don't want to burden Lilly with thinking about it."
"คำพูดของคุณพยาบาลยังดังก้องอยู่ในหัวแม้จะออกจากห้องมาแล้ว อาการของฉันไม่ใช่อะไรที่เป็นปัญหากับการ\nใช้ชีวิตมากเท่าคนอื่นที่อยู่ที่นี่ขนาดนั้น แล้วฉันก็ไม่อยากเป็นภาระให้ลิลลี่ต้องมาเป็นห่วงกับเรื่องนี้ด้วย"

# "If I just live life normally and avoid any short, sharp shocks, I should be okay. I won't let my condition rule me."
"ตราบใดที่ฉันใช้ชีวิตตามปกติแล้วไม่ไปเจออะไรที่ทำให้รู้สึกตื้อ ติด ตึงก็น่าจะไม่เป็นไร ฉันจะปล่อยให้อาการนี้บงการ\nชีวิตฉันไม่ได้"

scene bg school_gate_ss
show lilly cane_smileclosed_ss at center
with shorttimeskip

play music music_tranquil fadein 3.0

play sound sfx_normalbell

# "Lilly comes into view soon after the bells heralding the end of the school day ring out. She says farewell to a number of her classmates headed in the other direction, before beginning her weekly trip to the convenience store."
"หลังจากที่ระฆังซึ่งประกาศเวลาเลิกเรียนดังได้ไม่นานฉันก็เห็นลิลลี่ที่เดินออกมา เธอบอกลาเพื่อนร่วมชั้นกลุ่มหนึ่ง\nที่เดินไปอีกทางก่อนจะเริ่มกิจวัตรที่เธอต้องเดินไปซื้อของที่ร้านสะดวกซื้อทุกสัปดาห์"

# hi "Afternoon, Lilly."
hi "ทิวาสวัสดิ์ ลิลลี่"

show lilly cane_smile_ss
with charachange

# "The immediate warm smile and relaxed demeanor she assumes upon noticing my presence are unexpectedly welcome."
"รู้สึกอุ่นใจอย่างบอกไม่ถูกเมื่อลิลลี่ยิ้มอบอุ่นให้และทำท่าผ่อนคลายลงเมื่อรู้ว่าเป็นฉัน"

# li "Hello, Hisao. Good afternoon to you too."
li "สวัสดีจ้ะฮิซาโอะ ทิวาสวัสดิ์เช่นกันนะ"

show lilly cane_smileclosed_close_ss
with characlose

# "She hesitates for a second, but eventually deigns to tilt her face forward and close her eyes. My lips meet hers with a measure of slight trepidation before we move off, hand in hand."
"ลิลลี่ลังเลอยู่แวบหนึ่ง แต่สุดท้ายก็ยอมหลับตาแล้วโน้มหัวเข้ามา ริมฝีปากพวกเราแตะกันด้วยความประหม่าเล็กน้อย\nแล้วผละออกจากกัน จากนั้นพวกเราจึงจับมือกัน"

# "The fact that we're so close in height is somewhat useful at times, there being no need for either of us to turn our head upwards nor downwards in order to meet the other's."
"บางครั้งการที่ส่วนสูงของเราสองคนต่างกันไม่มากนั้นก็เป็นข้อดีอย่างหนึ่ง เช่นว่าเวลาหันหน้าเข้าหากันแล้วจะคุย\nหรืออะไรพวกเราไม่จำเป็นต้องเงยหน้าขึ้นหรือก้มหน้าลง"

scene bg school_road_ss
with locationchange

# "It doesn't take much time to leave the noise of the other students far behind us, the tapping of Lilly's cane in her free hand the only sound to be heard."
"ไม่นานพวกเราก็เดินพ้นมาจากกลุ่มนักเรียนที่ส่งเสียงอื้ออึง ขณะนี้มีเพียงเสียงจากไม้เท้าลิลลี่ที่กระทบกับพื้นเท่านั้น"

# "Silence, blissful silence, is all that greets us while we slowly walk in the setting sun's light."
"ความเงียบ—ความเงียบอันชวนให้สุขใจ—เป็นเพียงสิ่งเดียวที่อยู่เคียงพวกเราพร้อมแสงอาทิตย์อัสดง"

# hi "I think I'm coming to really like this town. The huge, green, hilly expanse, the trees everywhere, the somewhat rustic little buildings…"
hi "ฉันว่าฉันชักชอบเมืองนี้แล้วสิ ป่าเขากว้างใหญ่ ต้นไม้ห้อมล้อม สิ่งปลูกสร้างที่ดูเก่า ๆ …"

show lilly cane_smile_close_ss at center
with charaenter

# li "So you've come to appreciate the tranquility of it as well?"
li "ชอบความเงียบสงบของที่นี่ขึ้นมาบ้างแล้วหรือจ๊ะ"

# hi "I think so. I came from a metropolitan city near Tokyo, so the quiet of this town really alienated me when I first arrived."
hi "คิดว่านะ พอดีฉันมาจากเมืองใหญ่ที่อยู่แถว ๆ โตเกียวน่ะ ตอนที่ฉันย้ายมาใหม่ ๆ ก็เลยรู้สึกแปลกหูแปลกตามาก"

# hi "After a while it became really nice, though. I think I prefer it to the hustle and bustle of my home city now."
hi "แต่พออยู่ไปสักพักแล้วก็รู้สึกว่าเมืองนี้มันก็ดีเหมือนกัน ตอนนี้ฉันน่าจะชอบแบบนี้มากกว่าความวุ่นวายของเมือง\nที่ฉันอยู่แล้ว"

show lilly cane_smileclosed_close_ss
with charachange

# li "While I preferred the quiet of such a rural town even when I first arrived, I suppose I had the advantage of growing up in a quiet area before I came."
li "ฉันชอบความเงียบของเมืองชนบทอย่างนี้มาตั้งแต่ตอนที่มาอยู่แรก ๆ แล้วละ แต่ส่วนหนึ่งก็น่าจะเพราะก่อนหน้านี้\nฉันโตมากับพื้นที่ที่เงียบ ๆ ด้วย"

show lilly cane_weaksmile_close_ss
with charachange

# li "Hanako said the surroundings are very pretty, too."
li "ฮานาโกะเองก็บอกว่าทิวทัศน์แถวนี้ก็สวยดีด้วย"

# "Lilly may say such a thing quite easily, but each time she mentions how others describe sights around her as beautiful or pretty, I feel a little put off."
"ลิลลี่อาจจะพูดได้แบบไม่กระดากปากเท่าไหร่ก็จริง แต่ฉันก็รู้สึกแปลกหน่อย ๆ อยู่ดีเวลาที่ลิลลี่บอกว่าสภาพแวดล้อม\nที่อยู่รอบตัวเธอนั้นสวย"

# "I notice her expression becoming one of anticipation for some question or another. She always had a good sense for when somebody's not saying something that's on their mind, so I may as well speak up."
"ลิลลี่ทำสีหน้าคล้ายกำลังรอคำถามหรือคำพูดอะไรอยู่ เธอเป็นคนที่ประสาทไวมากเวลามีคนที่คิดอะไรอยู่แต่ไม่ได้พูด\nออกมา งั้นก็พูด ๆ ไปเลยแล้วกัน"

# hi "I was kind of wondering… uh, how to put this…"
hi "คือฉันอยากรู้ว่า… เอ่อ จะว่ายังไงดี…"

# hi "Do you ever… regret that you can't see what things look like for yourself? It's just something I've been thinking about."
hi "เธอเคย… นึกเสียใจมั้ยที่ไม่ได้เห็นอะไร ๆ กับตาตัวเอง พอดีฉันคิดเรื่องนี้มาสักพักแล้วน่ะ"

show lilly cane_listen_close_ss
with charachange

# "She thinks carefully for a time."
"ลิลลี่คิดพิจารณาอยู่ครู่หนึ่ง"

show lilly cane_smileclosed_close_ss
with charachange

# li "Do you ever regret that you can't hear people whispering on the other side of a room?"
li "เธอเคยนึกเสียใจหรือเปล่าที่เธอไม่ได้ยินเสียงกระซิบของคนที่อยู่ข้างห้องน่ะ"

show lilly cane_smile_close_ss
with charachange

# li "I can only speak for myself, but the fact that I can't see is the only way I've experienced life. Just as I cannot do something you can, you can't do something that I'm capable of."
li "ฉันอาจจะไม่ได้เป็นตัวแทนของคนทุกคนนะ แต่ฉันก็ใช้ชีวิตมากับความตาบอดโดยตลอด เธอมีสิ่งที่เธอทำได้\nแต่ฉันทำไม่ได้ ฉันเองก็มีสิ่งที่ฉันทำได้แต่เธอทำไม่ได้"

show lilly cane_weaksmile_close_ss
with charachange

# li "The fact that the world is made for those who are sighted can be a pain sometimes, but there are many, many people who suffer much more than I because of the way the world is."
li "บางครั้งฉันเองก็ลำบากกับการที่โลกนี้ถูกสร้างมาเพื่อคนสายตาปกติ แต่ก็ยังมีคนอีกมากมายที่ต้องลำบากกว่าฉัน\nหลายเท่ากับการที่โลกถูกสร้างมาอย่างนี้"

# hi "That does make sense, but still, it just feels kind of bad to describe something that you can't experience to you."
hi "ก็เข้าใจได้ แต่ก็นะ มันก็รู้สึกแย่อยู่เหมือนกันที่ต้องบรรยายอะไรที่ตัวเองสัมผัสไม่ได้ให้ตัวเองฟัง"

show lilly cane_surprised_close_ss
with charachange

# "She tilts her head quizzically, as if I'd just said something that makes very little sense at all."
"ลิลลี่เอียงคอสงสัยราวกับว่าสิ่งที่ฉันพูดนั้นไม่สมเหตุสมผลเอาเสียเลย"

# li "But I can experience it."
li "แต่ฉันสัมผัสได้นะ"

show lilly cane_smile_close_ss
with charachange

# li "You just said yourself that you like this area because of the way the surroundings are. I like this area for the very same reason."
li "เธอบอกว่าเธอชอบแถวนี้เพราะสภาพแวดล้อมดี ฉันก็ชอบแถวนี้เพราะเรื่องนั้นเหมือนกัน"

show lilly cane_smileclosed_close_ss
with charachange

# li "Thanks to the fact that this is a small rustic town surrounded by trees, it gives some peace and quiet away from the din at school and the bustle, not to mention the smells, of the city."
li "เพราะเมืองนี้เป็นเมืองเก่า ๆ ที่มีต้นไม้ล้อมรอบ ถึงได้มีที่ให้หลบจากเสียงจอแจในโรงเรียน ได้หลบจากความวุ่นวาย\nในเมือง แถมไม่ต้องทนสูดกลิ่นสูดควันในเมืองด้วย"

# "I suppose it would also be much like the home she shared with Akira, as well."
"แสดงว่าที่นี่ก็คงคล้าย ๆ บ้านที่ลิลลี่เคยอยู่กับอากิระด้วยสินะ"

# "Her outlook on it seems pretty sensible, and I'm not surprised that she's got a much better handle on her particular condition than I do on mine."
"มุมมองของลิลลี่ก็ฟังดูสมเหตุสมผลดี แล้วก็ไม่แปลกใจด้วยว่าทำไมลิลลี่ถึงดูปรับตัวเข้ากับสภาพร่างกายของเธอเอง\nได้ดีกว่าฉัน"

# "Just like how her coming from a location somewhat similar to Yamaku's surroundings let her become more acclimatized in a shorter time, being born blind affected her stance, by her own admission."
"เธอยอมรับความตาบอดซึ่งติดตัวเธอมาแต่กำเนิดจนมุมมองต่อสิ่งต่าง ๆ นั้นเปลี่ยนตาม ไม่ต่างอะไรกับการที่เธอ\nปรับตัวได้เร็วกว่าฉันเพราะเคยใช้ชีวิตอยู่กับสถานที่ที่สภาพแวดล้อมคล้ายกับโรงเรียนยามากุ"

# "I should stop being so annoyed with myself over it, but I can't shake the feeling that I've depended on Lilly far too much, given the circumstances most have had to deal with in Yamaku."
"ฉันควรจะเลิกหงุดหงิดตัวเองกับเรื่องนี้ได้แล้ว แต่ฉันก็ไม่อาจปัดความรู้สึกที่ว่าตัวเองพึ่งลิลลี่มากไปออกจากหัวไม่ได้\nเพราะฉันต้องเจอกับอะไรหลายอย่างตอนที่อยู่ยามากุ"

# hi "That makes a lot of sense. You're pretty good at explaining, as always."
hi "อย่างนี้นี่เอง เข้าใจละ เธอนี่อธิบายอะไรได้ดีเหมือนเคยเลยนะ"

# hi "Come to think of it, where is Hanako anyway? She was with us for lunch."
hi "จะว่าไป ฮานาโกะอยู่ไหนเนี่ย ตอนเที่ยงยังมากินข้าวด้วยกันอยู่เลย"

show lilly cane_weaksmile_close_ss
with charachange

# li "It seems she's busy studying. The exams are far from over, and she said she wants to do better this year than the last."
li "เหมือนจะอ่านหนังสือเตรียมสอบอยู่น่ะจ้ะ ยังเหลือวิชาที่ต้องสอบอีกหลายวิชานี่นะ ได้ยินว่าปีนี้อยากทำคะแนนให้ได้\nเยอะกว่าปีก่อนด้วย"

# hi "While I admire her work ethic, she's really been trying to give us a lot of room alone recently."
hi "มุ่งมั่นน่าประทับใจมาก แต่ช่วงนี้รู้สึกเหมือนจะให้ช่องพวกเรามาอยู่ด้วยกันสองคนได้บ่อยขึ้นนะ"

show lilly cane_reminisce_close_ss
with charachange

# li "She's that type of person, I think; the kind that puts others' needs above her own at every chance. She's a sweet girl, even though so much has hurt her in the past."
li "ฮานาโกะเป็นคนอย่างนั้นแหละจ้ะ จะต้องทำอะไรเพื่อคนอื่นทุกครั้งที่มีโอกาส เป็นคนใจดีนะ ทั้งที่อดีตต้องเจอกับอะไร\nมาตั้งหลายอย่าง"

show lilly cane_weaksmile_close_ss
with charachange

# li "I don't know… I feel like it's only now, when she's less close to me than ever, that she's truly finding herself."
li "ไม่รู้สิ… แต่รู้สึกเหมือนจะต้องเป็นช่วงที่ออกห่างจากฉันแล้วที่ฮานาโกะถึงได้เริ่มค้นหาตัวเองอย่างจริงจังขึ้นมา"

show lilly cane_smile_close_ss
with charachange

# li "It was thanks to you that she began to become more confident, after all, not me."
li "ที่จริงก็เพราะเธอนี่นะฮานาโกะถึงได้มีความมั่นใจขึ้นมา ไม่ใช่เพราะฉันเลย"

# "I take my hand from hers and gently place it on her head."
"ฉันปล่อยมือจากลิลลี่แล้วลูบหัวเธอเบา ๆ"

# hi "The important thing is that you were there for her. I can't even imagine what she'd be like without having found someone like you. That much became obvious while you were in Scotland."
hi "สิ่งสำคัญคือการที่เธอคอยอยู่เคียงข้างฮานาโกะต่างหาก ฉันนึกภาพไม่ออกเลยว่าถ้าฮานาโกะไม่ได้มาเจอคนอย่างเธอ\nแล้วจะเป็นยังไง ดูอย่างตอนที่เธออยู่สกอตแลนด์ก็ได้"

# hi "We're all still friends, so we've just got to have faith in her. I think she'll become a good person, and that much is thanks to you being there for her when she most needed it, just as you were there for me."
hi "พวกเรายังเป็นเพื่อนกันอยู่ เราต้องเชื่อใจฮานาโกะสิ ยังไงฮานาโกะจะต้องเป็นคนที่ดีแน่นอน ซึ่งการที่ฮานาโกะเป็นคนดีได้\nก็เพราะมีเธอคอยอยู่เคียงข้างในยามลำบาก เหมือนอย่างที่เธอคอยอยู่เคียงข้างฉันนั่นแหละ"

show lilly cane_weaksmile_close_ss
with charachange

# li "It makes me feel a bit childish when you sound so wise."
li "พอเธอพูดอะไรเป็นผู้ใหญ่อย่างนี้แล้วเหมือนฉันเป็นเด็กไปหน่อย ๆ เลย"

# hi "Well, I try."
hi "อืม ฉันก็พยายามทำตัวอย่างนั้นแหละ"

# hi "Are you doing anything on the weekend, by any chance?"
hi "ว่าแต่ว่าสุดสัปดาห์นี้เธอมีธุระอะไรหรือเปล่า"

show lilly cane_surprised_close_ss
with charachange

# li "Nothing that comes to mind. Why?"
li "เหมือนจะไม่นะ ทำไมเหรอจ๊ะ"

# hi "Then how about a date on Sunday? It'd be something to do besides exam preparation."
hi "งั้นวันอาทิตย์นี้ไปเดตด้วยกันมั้ย จะได้ไม่ต้องมัวแต่นั่งอ่านหนังสือเตรียมสอบกัน"

show lilly cane_smileclosed_close_ss
with charachange

# "Countering my rapidly beating heart, she simply smiles and nods."
"ลิลลี่เพียงยิ้มและพยักหน้า ต่างจากฉันซึ่งหัวใจเต้นรัว"

# li "That would be lovely."
li "ดีเลยจ้ะ"

# hi "Where would you like to go?"
hi "เธออยากไปที่ไหนมั้ย"

show lilly cane_displeased_close_ss
with charachange

# "Her face suddenly changes to one of disapproval."
"อยู่ ๆ ลิลลี่ก็ทำหน้าไม่พอใจ"

# li "You can't do that, Hisao. That's cheating."
li "ไม่ได้นะฮิซาโอะ ขี้โกง"

# hi "Do what?"
hi "อะไร"

# li "A gentleman should never ask a lady where to have a date."
li "สุภาพบุรุษเขาไม่ถามสุภาพสตรีกันนะจ๊ะว่าจะไปเดตที่ไหนกันดี"

# hi "Ah… oh."
hi "อ่า… อ้อ"

show lilly cane_smile_close_ss
with charachange

# "Her smile quickly comes back, assuring me that she's far from serious."
"ลิลลี่กลับมายิ้มตามเดิมในทันทีเป็นการยืนยันว่าเธอเพียงพูดหยอกล้อไปเท่านั้นเอง"

show lilly cane_smileclosed_close_ss
with charachange

# li "Don't worry about it. I'll think about where we could go."
li "ไม่ต้องคิดมากหรอกจ้ะ เดี๋ยวฉันไปคิดเองว่าจะไปที่ไหนกันดี"

# hi "I'll leave it to you, then. I promise to decide on the next date, though."
hi "งั้นก็ฝากเธอด้วยแล้วกัน แต่เดตรอบหน้าฉันสัญญาว่าจะเป็นคนเลือกให้นะ"

stop music fadeout 4.0

# "With our plans for the weekend made, the rest of the walk down the hill continues in silence."
"พอตกลงกันเรื่องนัดเดตเรียบร้อยแล้วพวกเราก็เดินลงเขากันต่อไปเงียบ ๆ"

# "The prospect of that lasting for any length of time, however, is shattered as I catch sight of a familiar figure waiting for us, her hand held high."
"แต่ความคาดหวังว่าจะได้อยู่เงียบ ๆ แบบนี้ไปอีกสักระยะเป็นอันต้องแตกสลายเมื่อฉันเห็นเงาอันคุ้นเคยที่โบกมือทักทาย\nรอพวกเราอยู่"

show lilly cane_smileclosed_close_ss at twoleft
show bg school_road_ss at bgleft
with charamove

show akira basic_smile_ss at tworight
with charaenter

# aki "Yo."
aki "ไง"

scene bg suburb_konbiniint
with shorttimeskip

play music music_daily fadein 0.5

# "Storewoman" "Thank you, please come again!"
thname("พนักงานหญิง") "ขอบคุณค่ะ โอกาสหน้าเชิญใหม่นะคะ!"

scene bg suburb_konbiniext_ss
with locationchange

# "The change in temperature as I step outside from the convenience store sends a chill up my spine. It feels like summer's starting to wind down."
"เมื่อสัมผัสกับความต่างของอุณหภูมิระหว่างในร้านกับนอกร้านแล้วก็รู้สึกหนาว ๆ ขึ้นมา เหมือนใกล้จะหมดฤดูร้อน\nเต็มทีแล้ว"

show lilly cane_weaksmile_ss at center
with charaenter

# "Looking to my side, the same feeling seems to affect Lilly as well, though unlike me she doesn't manage to hide the fact. Something I didn't realize at first was how physically delicate she is, even compared to the likes of Hanako."
"พอมองไปด้านข้างก็เห็นว่าลิลลี่เองก็หนาว ๆ เหมือนกัน เพียงแต่เธอไม่เก็บอาการเหมือนอย่างฉัน สิ่งที่ฉันไม่ทันได้คิด\nเมื่อได้รู้จักกับลิลลี่แรก ๆ นั้นคือความบอบบางของร่างกายเธอ ซึ่งแม้จะเทียบกับคนอย่างฮานาโกะแล้วก็ยังดูบอบบางอยู่ดี"

# "If I had to describe her, I'd have to say that she reminds me of a china doll."
"ถ้าจะให้บรรยายลักษณะของลิลลี่ ฉันก็คงจะบอกว่าเธอนั้นเหมือนอย่างตุ๊กตากระเบื้องเคลือบ"

show akira basic_ending_ss at center behind lilly
with charaenter

show lilly cane_surprised_ss
with vpunch

show lilly cane_reminisce_ss at twoleft
show akira basic_ending_ss at tworight
show bg suburb_konbiniext_ss at bgleft
with dissolvecharamove

# "Akira walks up behind her and gives a couple of hard pats on her shoulder, much to Lilly's consternation. For a moment she looks as envious of my status as an only child as I am of their close relationship."
"อากิระเดินเข้ามาข้างหลังลิลลี่ซึ่งทำหน้าเอือม ๆ อยู่แล้วตบบ่าสองที แวบหนึ่งลิลลี่ทำหน้าเหมือนอิจฉาที่ฉันเป็น\nลูกคนเดียวเหมือนอย่างที่ฉันอิจฉาที่สองคนนี้สนิทกันเหลือเกิน"

show lilly cane_listen_ss
show akira basic_boo_ss
with charachange

# "They talk between themselves for a few moments as I sort out my bags, their voices too low for me to catch, but eventually they break off and we begin the walk back to school."
"ทั้งสองคนคุยกันเสียงเบาเกินกว่าที่ฉันจะได้ยินอยู่ครู่หนึ่งระหว่างที่ฉันจัดแจงถุงข้าวของตัวเอง สุดท้ายทั้งสองคนก็ผละ\nจากกันก่อนที่พวกเราจะเริ่มเดินเพื่อกลับโรงเรียน"

scene bg school_road_ss
show akira basic_smile_ss at tworight
with locationskip

# aki "Ah, it feels good to be out of that damned office. You kids don't know how good you have it here."
aki "เฮ้อ ได้ออกมาจากออฟฟิศเส็งเคร็งนั่นสักทีนี่สดชื่นดีจริง เด็กอย่างพวกเธอคงไม่เข้าใจหรอกว่าสภาพตัวเองตอนนี้น่ะ\nสบายแค่ไหน"

show lilly cane_displeased_ss at twoleft
with charaenter

# li "Kids…"
li "เด็ก…"

show akira basic_laugh_ss
with charachange

# aki "Tsch. “You two,” then. Kids grow up so fast, nowadays."
aki "ชิ “พวกเธอสองคน” ก็ได้ เด็กสมัยนี้โตไวจริง"

show lilly cane_pout_ss
with charachange

# li "You're not old enough to say that."
li "แต่พี่ยังไม่แก่ขนาดนั้นเลย"

show akira basic_lost_ss
with charachange

# aki "I don't know. Being around Hideaki makes me feel damned old; he's so precocious he reminds me of you when you were younger."
aki "ไม่รู้ดิ อยู่กับไอ้ฮิเดอากิมันแล้วรู้สึกว่าตัวเองแก่โคตร แก่เกินตัวเหมือนกับเธอตอนเด็ก ๆ เลย"

show lilly cane_weaksmile_ss
with charachange

# li "He's a nice boy. It would be a shame if Shizune comes to have too much of an influence on him."
li "ฮิเดอากิเขาน่ารักนะ ถ้าเกิดสักวันติดนิสัยชิซูเนะมาคงน่าเสียดายแย่เลย"

show akira basic_laugh_ss
with charachange

# "Akira gives an amused snort at her sister's antipathy. She really doesn't seem to regard it as anything to make a serious fuss about, treating it more like a childhood spat."
"อากิระแค่นหัวเราะชอบใจที่น้องสาวตัวเองเกลียดคนนั้นถึงขนาดนั้น คงจะเห็นว่าไม่ใช่เรื่องจริงจังวุ่นวายมากมาย เหมือน\nเด็กตีกันมากกว่า อะไรทำนองนั้น"

show akira basic_smile_ss
with charachange

# "She looks over to me, apparently only just remembering that I'm here, and gives a small grin as she reaches towards her back pocket."
"เธอหันมามองฉันเหมือนเพิ่งนึกได้ว่ามีฉันยืนหัวโด่อยู่ตรงนี้ด้วยก่อนจะยิ้มน้อย ๆ แล้วล้วงกระเป๋ากางเกงตัวเอง"

# hi "What is it?"
hi "มีอะไรเหรอครับ"

show akira basic_ending_ss
with charachange

# aki "Just a sec, let me dig it out…"
aki "แป๊บนะ ขอหาก่อน…"

# "After quite some difficulty, she manages to retrieve her black leather wallet from her back pocket, quickly fishing out what looks to be a folded square of paper."
"อากิระงัดแงะกระเป๋ากางเกงด้านหลังอยู่พักหนึ่งก่อนจะคว้ากระเป๋าสตางค์หนังสีดำออกมาได้แล้วหยิบอะไรสักอย่าง\nที่ดูเหมือนเป็นแผ่นกระดาษสี่เหลี่ยมที่พับเอาไว้"

# "With Lilly all but unaware of what's happening, Akira unfolds the scrap and hands it to me."
"ลิลลี่ยังคงไม่รับรู้ว่าเกิดอะไรขึ้น อากิระคลี่กระดาษแผ่นนั้นออกแล้วยื่นมาให้ฉัน"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

show stallphoto_insert:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

# "An old photo of… what looks to be a younger Lilly and Shizune operating a noodle stall, with some other girl in the background. She looks vaguely familiar, but I can't quite pinpoint why."
"เป็นรูปเก่า ๆ เหมือนจะเป็นรูป… ลิลลี่กับชิซูเนะตอนเด็กที่กำลังตั้งแผงขายบะหมี่กับผู้หญิงอีกหนึ่งคนที่อยู่ข้างหลัง ซึ่ง\nพอดูแล้วก็รู้สึกคุ้น ๆ แต่ก็บอกไม่ถูกเหมือนกันว่าเคยเห็นที่ไหน"

show lilly cane_smile_ss
with None

$ renpy.music.set_volume(1.0, 1.0, channel="music")

show stallphoto_insert:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide stallphoto_insert
with None

# li "What is it, Akira?"
li "อะไรเหรอพี่"

show akira basic_boo_ss
with charachange

# aki "I think you know."
aki "เธอน่าจะรู้นะ"

show lilly cane_listen_ss
with charachange

# "Lilly mulls this over for a few moments before realization dawns on her."
"ลิลลี่ครุ่นคิดอยู่ครู่หนึ่งก่อนจะนึกขึ้นได้"

show lilly cane_surprised_ss
with charachange

# li "Akira… you really needn't…"
li "พี่… พี่ไม่เห็นต้อง…"

show akira basic_smile_ss
with charachange

# aki "It's fine, isn't it? Besides, it's like the only photo I have of you two since you entered Yamaku where you're not at each other's throats."
aki "ก็ไม่เห็นเป็นไรเลยนี่ อีกอย่าง เป็นรูปเดียวเลยมั้งที่ได้ถ่ายตอนที่เธอสองคนอยู่ที่ยามากุแล้วยังรักกันดีน่ะ"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

show stallphoto_insert:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

# "I look back down to the photo in my hand."
"ฉันหันกลับมามองรูปในมือ"

# "It does seem strange to see Lilly and Shizune working together so dilligently without any sign of animosity. If the photo's of them during Yamaku's festival, that means it must have been taken one or two years ago."
"ซึ่งก็รู้สึกแปลก ๆ เหมือนกันที่ได้เห็็นลิลลี่กับชิซูเนะทำงานด้วยกันอย่างขยันขันแข็งขนาดนี้โดยที่ไม่มีทีท่าว่าจะ\nระหองระแหงอะไรกันเลย ถ้ารูปนี้ถ่ายตอนวันงานเทศกาลโรงเรียนยามากุ แปลว่ารูปนี้ถ่ายเมื่อหนึ่งหรือสองปีที่แล้ว"

# "In other words, the time when they were both in the Student Council together."
"หรือก็คือ ช่วงที่ทั้งสองคนยังอยู่สภานักเรียนด้วยกันนั่นเอง"

# hi "Who's the girl in the back? She looks kind of familiar."
hi "ผู้หญิงที่อยู่ข้างหลังนั่นใครเหรอครับ หน้าคุ้น ๆ"

# aki "Hah, I knew you wouldn't recognize her. It's Misha before she went and dyed her hair pink."
aki "เฮอะ กะแล้วว่าเธอต้องจำไม่ได้ นั่นมิช่าสมัยที่ยังไม่ได้ย้อมผมสีชมพูน่ะ"

# hi "That's Misha? No way…"
hi "มิช่าเหรอครับ บ้าน่า…"

# "It feels extremely strange to see Misha without her so very distinctive hairstyle. Judging from Akira's tone, she doesn't take favorably to Misha's idea of fashion."
"ได้เห็นมิช่าที่ไม่ได้ทำผมอันโดดเด่นเป็นเอกลักษณ์แล้วก็รู้สึกแปลกตามาก ๆ ซึ่งฟังจากน้ำเสียงแล้ว อากิระคง\nไม่ค่อยชอบที่มิช่าทำผมอย่างนี้สักเท่าไหร่"

# "I suppose that fact just accentuates how odd the situation looks. To think they were so friendly in the past… I wish I could do something to mend their relationship."
"การที่มิช่าทำผมอย่างนั้นก็คงนับเป็นการย้ำเตือนได้มั้งว่าสถานการณ์ตอนนี้มันแปลกขนาดไหน ทั้งที่เคยสนิทกันดี\nแท้ ๆ … อยากหาทางช่วยให้สองคนนี้กลับมาคืนดีกันจัง"

# li "You're being very quiet, Hisao."
li "เธอเงียบน่าดูเลยนะฮิซาโอะ"

# hi "It just feels kinda strange to see you all so friendly like this."
hi "แค่รู้สึกแปลก ๆ ที่เห็นพวกเธอสนิทกันอย่างนี้น่ะ"

# "Lilly moves to say something, but stops herself. In the end, this isn't a matter for me; it's between Shizune and Lilly, and nobody else."
"ลิลลี่ทำท่าเหมือนจะพูดอะไรแล้วก็ชะงักไป เอาเข้าจริงแล้ว เรื่องนี้ก็ไม่ได้เกี่ยวกับฉันเลย เป็นเรื่องของสองคนนั้นเท่านั้น\nไม่เกี่ยวกับใครคนอื่น"

# li "Things change. Unfortunately."
li "เวลาเปลี่ยนได้ทุกอย่างจ้ะ ต่อให้จะไม่อยากให้เปลี่ยนก็เถอะ"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

stop music fadeout 6.0

show akira basic_resigned_ss
show lilly cane_reminisce_ss
with None

show stallphoto_insert:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide stallphoto_insert
with None

# "I hand the photo back to Akira, who sighs as she folds it up and slides it back into her wallet. A little memory, quietly hidden away, to be pulled out again some time later."
"ฉันยื่นรูปคืนให้อากิระ เธอถอนหายใจแล้วพับใส่กระเป๋าสตางค์ตามเดิม ความทรงจำแผ่นเล็ก ๆ ที่ถูกซ่อนไว้อย่างเงียบงัน\nรอวันเปิดออกมาอีกครั้ง"

# aki "Yeah, that they do."
aki "อืม นั่นสินะ"

# "Initially I think Akira's reaction to be simply in response to the situation between Lilly and Shizune, but she looks oddly glum compared to what I'd expect. Lilly's expression has clouded as well."
"ทีแรกฉันคิดว่าอากิระตอบเป็นการเห็นด้วยกับเรื่องระหว่างลิลลี่กับชิซูเนะเท่านั้น แต่สีหน้าเธอดูหมองแปลก ๆ ซึ่งผิด\nไปจากที่ฉันคาด สีหน้าลิลลี่เองก็ดูหม่น ๆ ตามไปด้วย"

# hi "What's wrong?"
hi "มีอะไรเหรอครับ"

show akira basic_boo_ss
with charachange

# aki "Ah, it's just that I'll be going to Scotland fairly soon."
aki "อ้อ แค่ว่าอีกเดี๋ยวฉันจะต้องไปสกอตแลนด์แล้วน่ะ"

# hi "You're leaving for Scotland again?"
hi "จะไปสกอตแลนด์อีกแล้วเหรอครับ"

show akira basic_lost_ss
with charachange

# "For a long moment, Akira looks surprised. It's an ill-fitting expression for her."
"อากิระทำหน้าตกใจอยู่พักใหญ่ เป็นสีหน้าที่ไม่เหมาะกับเธอเอาเสียเลย"

# "After a glance at Lilly, she turns back to me as if she'd never done so."
"พอหันไปมองลิลลี่แล้วเธอก็กลับมามองฉันราวกับไม่มีอะไรเกิดขึ้น"

show akira basic_resigned_ss
with charachange

# aki "Yeah. In a couple of weeks I'll be leaving for Inverness to work at the company's headquarters. It's a pretty big jump in corporate position, and it's not a chance that's going to come again."
aki "อื้ม อีกสองสัปดาห์เดี๋ยวต้องไปทำงานที่สำนักงานใหญ่ของบริษัทที่อินเวอร์เนสส์น่ะ เลื่อนขั้นครั้งใหญ่น่าดูเลยแหละ\nโอกาสอย่างนี้คงไม่มีอีกแล้ว"

# "So Akira's going to leave Japan, on what seems to be a permanent basis…"
"ก็คืออากิระจะไปสกอตแลนด์ แล้วเหมือนจะไปอยู่ถาวรด้วย…"

# "I can't help feeling that my assumption that we could all happily while away our days, having fun in this isolated little world, is coming to an end. It's unsettling."
"ฉันหวั่นใจว่าวันเวลาที่ฉันคิดว่าพวกเราจะได้อยู่ด้วยกันอย่างมีความสุขในโลกใบเล็กซึ่งสันโดษนี้ใกล้สิ้นสุดลง รู้สึก\nใจคอไม่ดีเลยแฮะ"

# "I look at Lilly, mildly surprised that she hasn't told me such a thing despite usually being so forthcoming."
"ฉันหันไปมองลิลลี่ด้วยความประหลาดใจเล็กน้อยที่เธอไม่ได้บอกอะไรเลย ทั้งที่ปกติเธอเป็นคนเปิดเผยแท้ ๆ"

# "She continues to walk with her face fixedly pointed ahead. I can't read her expression, nor can I even guess what's on her mind, which is discomforting given how it's usually easy for me to do both."
"ลิลลี่ยังคงตั้งหน้าตรงเดินไปเรื่อย ๆ อ่านสีหน้าไม่ออกเลยแฮะ ไม่รู้ด้วยว่าคิดอะไรอยู่ ซึ่งก็ชวนให้รู้สึกอึดอัด เพราะปกติ\nฉันจะอ่านสีหน้าหรือเดาสิ่งที่ลิลลี่คิดอยู่ได้ไม่ยาก"

# "It reminds me of the time when we met at the Shanghai, just before what could be called our first date. At the time, all I could do was comfort her without knowing the cause, and now feels no different."
"นึกถึงตอนเจอกันที่ร้านเซี่ยงไฮ้เลย ตอนก่อนที่จะได้เที่ยวงานด้วยกันคล้ายเป็นเดตแรก ตอนนั้นฉันได้แต่ปลอบลิลลี่\nโดยที่ไม่รู้ว่าเธอเป็นอะไรกันแน่ และตอนนี้ก็ไม่ต่างอะไรกันเลย"

scene bg school_dormext_full_ni
show akira basic_resigned_ni at tworight
show lilly cane_reminisce_ni at twoleft
with shorttimeskip

# "As we finally reach the school dormitories once again, there's a somewhat awkward silence. I don't think I'm the only one who feels it."
"เมื่อมาถึงที่หอในอีกครั้งพวกเราก็เงียบกันไปจนชวนให้อึดอัด คงไม่ได้มีแค่ฉันแน่ ๆ ละที่รู้สึกอย่างนี้"

# hi "See you tomorrow then, Lilly. Bye, Akira."
hi "งั้นก็เจอกันพรุ่งนี้นะลิลลี่ บายครับพี่อากิระ"

show lilly cane_weaksmile_ni
with charachange

# li "Good night, Hisao."
li "ราตรีสวัสดิ์จ้ะฮิซาโอะ"

show akira basic_smile_ni
with charachange

# aki "Seeya."
aki "เจอกัน"

hide lilly
hide akira
with charaexit

# "And with that, they walk to the female dormitories."
"แล้วสองคนนั้นก็เดินไปที่หอหญิง"

# "Opening the door to the male dormitories, I stop and look back at them just moments before their figures disappear behind the heavy wooden door."
"ฉันเปิดประตูหอชายพลางมองไล่หลังสองคนนั้นก่อนที่เงาทั้งคู่จะหายลับไปตรงเบื้องหลังประตูไม้บานใหญ่บานนั้น"

# "That was… a strange moment when Akira said she was leaving. While that wasn't the first time when my thoughts regarding my new life have been called into question, it's perhaps the first time to do it quite so profoundly."
"ตอนที่อากิระบอกว่าจะต้องไปสกอตแลนด์นั้นเป็นช่วงเวลาที่… แปลกประหลาด ถึงฉันจะเคยตั้งคำถามกับชีวิตใหม่\nของตัวเองมาแล้วก็จริง แต่ตอนนั้นอาจจะเป็นครั้งแรกเลยที่ฉันเพิ่งได้มาไตร่ตรองให้จริงจัง"

# "I still don't know what to make of Akira's reaction, much less of Lilly's."
"ฉันยังคิดไม่ออกว่าสีหน้าท่าทางของอากิระนั้นหมายความว่าอย่างไร แล้วยิ่งไม่ต้องพูดถึงฝั่งลิลลี่เลย"

# "The night's chill reminds me to get back to my room before I catch something, my bags pulling down on my arms with seemingly redoubled weight."
"อากาศเย็น ๆ ยามค่ำคืนบอกเตือนให้ฉันรีบเข้าห้องตัวเองก่อนที่จะไม่สบายไปเสียก่อน ถุงข้าวของที่ฉันถือมารู้สึกเหมือน\nหนักขึ้นเป็นสองเท่า"

# "If nothing else, I have a date with her set up for the weekend. I just need to stop overthinking stuff and get on with things as they are."
"ถ้าไม่มีอะไรผิดพลาด สุดสัปดาห์นี้ฉันก็จะได้ไปเดตกับลิลลี่ ฉันแค่ต้องเลิกคิดมากแล้วคอยดูอะไรไปเรื่อย ๆ ก่อน"

# "The exams are still ongoing, after all, and with the trimester's end and the summer holidays beginning soon, there'll be plenty to keep me busy for a while."
"ไหนจะยังเหลือวิชาที่ต้องสอบอยู่อีก แล้วเดี๋ยวก็จะได้ปิดเทอมฤดูร้อนแล้ว คงจะมีอะไรให้ชีวิตวุ่นวายอีกพักใหญ่เลย"

# "As I give a yawn and retreat inside, my thoughts turn to what Lilly will decide to set as the location of our weekend rendezvous."
"ฉันหาวเดินเข้าห้องพลางคิดไปว่าลิลลี่จะเลือกที่ไหนเป็นสถานที่สำหรับนัดของเราสุดสัปดาห์นี้"

scene black
with dissolve

#***********

label th_L24:

scene bg city_restaurant at Fullpan(10.0)
with dissolve

play music music_jazz

# "I'm pretty sure this is about the last thing I had in mind when Lilly said she'd decide where to have our date."
"ตอนที่ลิลลี่บอกว่าจะเลือกสถานที่ให้นั้นฉันไม่ได้คิดเลยว่าจะเป็นที่อย่างนี้"

# "No man nor woman is dressed in anything but their finest, their formality only matched by that of their surroundings; rich red wallpaper adorns the walls as the city lights far below flicker and glow."
"ไม่ว่าจะผู้ชายหรือผู้หญิงต่างแต่งตัวกันอย่างหรูหราเต็มที่ มีเพียงงานตกแต่งภายในร้านที่เรียบร้อยสวยงามกว่าเสื้อผ้า\nเหล่านั้น ผนังร้านปิดด้วยวอลล์เปเปอร์สีแดงเข้ม เบื้องล่างมีแสงไฟจากตัวเมืองวูบไหวอยู่เรือง ๆ"

# "Combined with the ambient hum of quiet speech and the high-pitched clattering of cutlery and wineglasses, the mood is very formal, yet relaxed enough for me not to feel too uptight despite this being our first real date."
"บรรยากาศภายในร้านนั้นให้ความรู้สึกเป็นพิธีรีตองยิ่งขึ้นไปอีกด้วยเสียงพึมพำจากผู้คนที่คุยกันเสียงเบาซึ่งเคล้า\nกับเสียงแหลม ๆ จากเครื่องเงินหรือแก้วไวน์ที่กระทบกัน ทว่ายังผ่อนคลายพอที่จะทำให้ฉันรู้สึกสบาย ๆ ทั้งที่เป็นเดต\nจริง ๆ ครั้งแรกของพวกเรา"

# "Once we get seated, our waiter leaves to attend to others with a quick bow, after an appreciative nod from Lilly."
"พอพวกเรานั่งลงและลิลลี่พยักหน้าเป็นการขอบคุณให้แล้วบริกรที่นำทางพวกเรามาก็โค้งตัวเล็กน้อยก่อนจะไปบริการ\nลูกค้าคนอื่นต่อ"

# "Far from depending on my help, Lilly's managed to navigate herself around surprisingly easily so far, despite the unfamiliar environment. A light brush here and there, and she's generally quite deft at orienting herself as needed."
"แม้จะเป็นสถานที่ที่ไม่คุ้นเคย แต่ลิลลี่ก็จัดการอะไรด้วยตัวเองได้อย่างง่ายดายเหลือเชื่อโดยไม่ต้องพึ่งความช่วยเหลือ\nจากฉันเลย เพียงแตะนู่นนิดนี่หน่อยเธอก็สามารถจัดแจงตัวเองอย่างคล่องแคล่วได้ดังใจต้องการแล้ว"

$ ksgallery_unlock("evul lilly_restaurant_listen")
scene ev lilly_restaurant_listen at restaurant_out
with whiteout

# "My eyes look to Lilly's. I can tell from her face that she's listening to her surroundings just as hard as I'm looking."
"ฉันมองตาลิลลี่ ดูจากสีหน้าแล้วเธอเองก็คงกำลังเงี่ยหูฟังสภาพแวดล้อมไม่ต่างจากฉันที่จ้องมองไปรอบ ๆ"

# "Though truth be told, my eyes are lingering on her each time they sweep across the room. The red cheongsam she's wearing accentuates her figure very well and shows off her legs. Even her hair is done up, and the scent of perfume is just noticeable."
"แต่ว่าตามตรง ทุกครั้งที่กวาดตามองสภาพในร้าน ฉันก็เป็นต้องหยุดมองอ้อยอิ่งที่ลิลลี่ทุกครั้ง ชุดกี่เพ้าสีแดงนั้นขับเน้น\nรูปร่างของเธอได้เป็นอย่างดี และยังเผยให้เห็นขาของเธอ เธอรวบผมและใส่น้ำหอมมาอ่อน ๆ พอให้ได้กลิ่นอีกด้วย"

# "While my black suit may be a rental, I managed to select an appropriate one. It feels surprisingly comfortable considering I've so rarely worn one, and fits the setting just as well as Lilly's attire."
"ส่วนฉันก็ยังพอหาเช่าชุดสูทที่ดูเหมาะ ๆ มาได้อยู่ ซึ่งใส่สบายผิดคาด เพราะฉันแทบไม่ได้ใส่ชุดสูทเลย และยังเข้ากับ\nบรรยากาศได้ไม่ยิ่งหย่อนไปกว่าการแต่งตัวของลิลลี่"

# hi "I guess this is a new experience for both of us, then?"
hi "สรุปก็เป็นประสบการณ์ใหม่ของเราทั้งคู่เลยสินะ"

$ ksgallery_unlock("evul lilly_restaurant_sheepish")
show ev lilly_restaurant_sheepish at restaurant_out
with charachange

# "She turns somewhat sheepish."
"ลิลลี่ทำท่าอาย ๆ"

# li "I've never come to a place such as this before, no."
li "ใช่จ้ะ ฉันไม่เคยมาร้านอย่างนี้มาก่อนเลย"

# hi "One hell of a first date, that's for sure. It's going to be pretty hard for me to top this."
hi "ที่แน่ ๆ คือเป็นเดตแรกที่หรูเอาเรื่อง เดตรอบหน้านี่ฉันชักหนักใจแล้วสิ"

# "A small giggle. Even now, our nervousness is dissipating."
"เธอหัวเราะคิกคัก แม้ตอนนี้จะดูเหมือนอึดอัด แต่พวกเราสองคนก็เริ่มหายเกร็งกันแล้ว"

# "Her hand skates along the center of the table until it touches the menu, which she takes in both hands and brings to her face."
"ลิลลี่เลื่อนมือไปตามพื้นที่ตรงกลางโต๊ะจนเจอเข้ากับรายการอาหาร เธอใช้ทั้งสองมือจับขึ้นมากางตรงหน้า"

# li "Um, Hisao?"
li "เอ่อ ฮิซาโอะ"

# "As she lowers the beige, laminated sheet just below her eyes, I can see another sheepish look."
"เธอลดแผ่นกระดาษสีเบจเคลือบนั้นลงมาอยู่เหนือโหนกแก้มเธอเผยให้เห็นสีหน้าอาย ๆ อีกครั้ง"

# "I doubt asking the waiter for a menu in Braille would be productive."
"ถ้าจะให้ขอรายการอาหารที่พิมพ์ด้วยอักษรเบรลล์กับบริกรก็คงจะไม่ได้ความสักเท่าไหร่"

# hi "I can read it out for you, no problem."
hi "เดี๋ยวฉันอ่านรายการอาหารให้ฟังเอง ไม่มีปัญหา"

scene bg city_restaurant at right
with locationchange

# "I take mine and give it a quick read, my small grin faltering."
"ฉันหยิบรายการอาหารของตัวเองขึ้นมา พอกวาดตาอ่านดูแล้วฉันก็หุบยิ้มทันที"

# hi "Er, perhaps there is."
hi "เอ่อ หรือจะมี"

show lilly basic_weaksmile_che_close:
    center
    ypos 1.1
with charaenter

# li "What's wrong?"
li "มีอะไรเหรอ"

# hi "There are quite a few items on here… and I'm not completely sure how to pronounce a couple of them."
hi "รายการอาหารในนี้มันมีไม่เยอะเท่าไหร่… แล้วก็มีบางรายการที่ฉันไม่แน่ใจด้วยว่าจะต้องอ่านว่ายังไง"

# "One fine cuisine after another is listed. Most may be in Japanese, but a few are in English and French. I guess it's to be expected, but I have no idea what's in some of these."
"อาหารจานหรูเรียงชื่อติด ๆ กันมา ส่วนใหญ่เป็นภาษาญี่ปุ่นก็จริง แต่บางรายการก็เป็นภาษาอังกฤษแล้วก็ภาษาฝรั่งเศส\nจริง ๆ ก็คงเป็นเรื่องปกติแหละ แต่กับบางรายการฉันไม่รู้ด้วยซ้ำว่าใส่อะไรบ้าง"

# "Oh, this one I recognize. Wait, hang on…"
"อ้อ อันนี้ฉันรู้จัก ไม่สิ เดี๋ยวนะ…"

# hi "…You can cook that?"
hi "…อันนั้นเขาเอามาทำอาหารได้ด้วยเหรอ"

show lilly basic_giggle_che_close
with charachange

# "A small giggle of amusement comes from behind the paper sheet."
"ลิลลี่หัวเราะคิกคักชอบใจอยู่หลังแผ่นกระดาษนั้น"

# hi "Well, I could read them all out, but it'd take a few hours."
hi "คือ ก็อ่านทุกรายการให้ฟังได้แหละ แต่คงต้องใช้เวลาสักสองสามชั่วโมงกว่าจะอ่านหมด"

show lilly basic_smile_che_close
with charachange

# li "Is there anything with some kind of fish in it?"
li "มีรายการไหนที่มีปลาหรืออะไรแบบนั้นหรือเปล่าจ๊ะ"

# hi "Let's see…"
hi "ไหนดูซิ…"

# "No. No. No. No. Aren't those poisonous? No. No. No. They eat that stuff? No. No. No. No… Ah, here we go."
"ไม่มี ไม่มี ไม่มี ไม่มี อันนี้มันมีพิษไม่ใช่เหรอ ไม่มี ไม่มี ไม่มี อันนี้เขากินกันด้วยเหรอ ไม่มี ไม่มี ไม่มี ไม่มี… อ่า นี่ไง"

# hi "A tuna salad seems to be a good bet. From the picture, it looks like it'd be pretty filling as well."
hi "สลัดทูน่าก็น่าจะดีนะ ดูจากรูปแล้วเหมือนจะได้เยอะด้วย"

show lilly basic_smileclosed_che_close
with charachange

# li "That seems to be a reasonably safe option."
li "ก็ฟังดูเป็นตัวเลือกที่ปลอดภัยดีใช้ได้จ้ะ"

# hi "Let's order two, then. I'm pretty sure a couple of these dishes are from poisonous animals. I've had enough deadly run-ins for now."
hi "งั้นเดี๋ยวสั่งสองที่นะ เหมือนมีสองรายการในนี้ที่ทำจากสัตว์มีพิษด้วย แค่นี้ฉันก็เฉียดตายมาหลายครั้งพอละ"

show lilly basic_weaksmile_che_close
with charachange

# "Lilly maintains a smile, but there's a distinct lack of laughter. Black humor mustn't be her cup of tea, though to be honest I don't find it exceedingly funny either."
"ลิลลี่ยังคงยิ้ม แต่ไม่มีเสียงหัวเราะตามมา สงสัยจะไม่ชอบมุกตลกร้ายอย่างนี้เท่าไหร่ แต่เอาจริง ๆ ฉันก็รู้สึกว่าที่เล่นไป\nมันก็ไม่ได้ตลกขนาดนั้นด้วย"

# li "There are certainly quite a few interesting smells wafting about. The same is true of the sights, I assume."
li "ในนี้มีกลิ่นน่าสนใจอวลอยู่สองสามกลิ่นเลย เธอเองก็คงเห็นอะไรน่าสนใจด้วยใช่มั้ยจ๊ะ"

# hi "I've never been anywhere quite like this. A fancy Japanese teahouse on an occasion or two, but never anything this lavish nor European in styling."
hi "ฉันไม่เคยมาร้านอย่างนี้มาก่อนเลย เคยไปพวกโรงน้ำชาญี่ปุ่นหรู ๆ อยู่ครั้งสองครั้งนะ แต่ไม่เคยมาภัตตาคารหรือ\nร้านสไตล์ยุโรปอย่างนี้เลย"

# "Before another word can be said, a portly waiter in a distressingly tight vest appears at our table to take our orders."
"ก่อนที่ฉันจะทันได้พูดอะไรต่อก็มีบริกรร่างท้วมซึ่งใส่เสื้อกั๊กที่เห็นแล้วอึดอัดแทนเดินมารับรายการที่โต๊ะเรา"

# hi "Provençal Tuna Salade Niçoise, please. Two."
hi "‘{i}Provençal Tuna Salade Niçoise{/i}’ (สลัดนิสปลาทูน่าแบบพรอว็องส์) สองที่ครับ"

# "I hope I didn't mess up the pronunciation of that too badly. Even if I did, he doesn't show it."
"หวังว่าจะไม่ได้ออกเสียงเพี้ยนมากนะ หรือถ้าเพี้ยนจริงก็แปลว่าบริกรเก็บอาการได้เก่งมาก"

show lilly behind_cheerful_che_close
with charachange

# li "And may I have a glass of Chardonnay, please. Hisao?"
li "แล้วก็ไวน์ชาร์ดอแนหนึ่งแก้วค่ะ ฮิซาโอะล่ะ"

# hi "Oh, uh, the same."
hi "อ้อ เอ่อ เหมือนกันครับ"

# "As the waiter nods and leaves, I suddenly realize what I said by absentmindedly mimicking Lilly's answer. I regret it pretty quickly."
"บริกรพยักหน้าแล้วเดินออกไป และฉันก็นึกได้ทันทีว่าฉันเผลอสั่งอะไรตามลิลลี่ไปโดยไม่รู้ตัว ไม่น่าสั่งตามไปเลย"

# hi "Alcohol…"
hi "แอลกอฮอล์…"

show lilly basic_pout_che_close
with charachange

# li "Only a bit."
li "นิดหน่อยจ้ะ"

# "This girl has an odd propensity to getting hooked on things, I swear."
"เธอนี่ชอบมาติดใจอะไรแปลก ๆ ดีเหลือเกินนะ"

# hi "Surprising that they didn't ask for identification."
hi "แต่แปลกนะที่เขาไม่ได้ขอตรวจบัตรน่ะ"

# hi "Then again, I guess we both do look mature for our age."
hi "แต่ก็นะ สงสัยเราสองคนหน้าแก่มั้ง"

show lilly basic_smileclosed_che_close
with charachange

# li "I'll have to take your word for it. I'll add that this isn't what I'd call the type of place to ask such things, though."
li "ฉันจะเชื่อเธอนะ แต่ก็ขอเสริมด้วยว่าร้านอาหารอย่างนี้ปกติเขาไม่ขอตรวจบัตรอะไรอย่างนั้นกันหรอก"

# hi "Good point."
hi "ก็จริง"

# "We both relax a little into our seats, trying to take our minds off the choking formality of the surroundings."
"พวกเราปรับตัวนั่งกับเก้าอี้ให้สบายอีกเล็กน้อยเพื่อที่จะได้ไม่ต้องคิดมากกับความเป็นพิธีรีตองอันน่าอึดอัดของบรรยากาศ\nโดยรอบ"

# "As soon as we do, the same waiter reappears at our table with two empty glasses and a bottle, the contents of which are quickly and professionally poured into the former."
"พอนั่งจนเข้าที่แล้วบริกรคนเดิมก็เดินถือแก้วเปล่าสองใบกับขวดไวน์หนึ่งขวดมาที่โต๊ะเราอีกครั้ง จากนั้นจึงเทไวน์ใส่แก้ว\nให้พวกเราด้วยความชำนิชำนาญอย่างรวดเร็ว"

scene ev lilly_restaurant_wine:
   zoom 1.05 xalign 0.0 yalign 0.5 subpixel True
   easeout 8.0 zoom 1.0
with flash

# "We both nod politely as he leaves, Lilly taking her glass and gently moving it from side to side. The liquid inside glistens as it moves around in the glass, and I have to admit it makes me a little less regretful for ordering the same."
"เราสองคนพยักหน้าตอบอย่างสุภาพก่อนที่บริกรคนนั้นจะเดินออกไป ลิลลี่หยิบแก้วไวน์ขึ้นมาแกว่งช้า ๆ ของเหลวที่\nเคลื่อนวนไปมาในแก้วนั้นเปล่งแสงวิบวับ ซึ่งต้องยอมรับว่าพอได้มองแล้วก็ค่อยรู้สึกดีขึ้นมาหน่อยที่สั่งตามไปด้วย"

# "I guess it must take effort to judge how the liquid inside is acting based only on its center of balance. Maybe it's like her origami; taking every little chance to practice her dexterity."
"การที่จะรับรู้ว่าของเหลวภายในแก้วนั้นมีสภาพเป็นอย่างไรจากการจับแค่เพียงจุดศูนย์ถ่วงนั้นคงต้องใช้ความพยายาม\nมากทีเดียว ลิลลี่อาจจะถือว่าเรื่องนี้เป็นอีกจุดเล็ก ๆ น้อย ๆ จุดหนึ่งที่ใช้ฝึกความคล่องแคล่วของเธอได้เหมือนอย่าง\nการพับกระดาษ"

# hi "I guess I'm not surprised that you know about a place like this. Those who have money would, I suppose."
hi "ก็คงไม่แปลกมั้งที่เธอจะรู้จักร้านแบบนี้ คนมีเงินเขาก็คงรู้จักร้านอย่างนี้กันนี่นะ"

# "This reminds me of just how completely different our upbringings were. In Yamaku, it's easy to forget about social and economic disparity between students all wearing the same uniforms, living in the same dormitories."
"ซึ่งก็ทำให้นึกได้ว่าเราสองคนนั้นโตกันมาคนละแบบโดยสิ้นเชิง เมื่ออยู่ยามากุแล้วบางครั้งก็อาจเผลอลืมไปได้ว่านักเรียน\nทุกคนที่ใส่เครื่องแบบชุดเดียวกันและอยู่หอที่เดียวกันนั้นต่างมีสถานภาพทางสังคมกับฐานะทางการเงินที่ไม่เหมือนกัน"

scene bg city_restaurant at right
show lilly basic_smile_che_close:
    center
    ypos 1.1
with flash

# li "Well, Akira was the one to tell me of it. She's come here before, apparently."
li "ก็นะ พี่เป็นคนแนะนำมาเองแหละ เหมือนว่าจะเคยมาน่ะ"

# "So that's what they were conspiring about on Friday."
"สรุปที่ซุบซิบกันเมื่อวันศุกร์ก็เรื่องนี้น่ะเอง"

# hi "And you chastise me for cheating?"
hi "แล้วมาบอกฉันว่าอย่าโกงเนี่ยนะ"

show lilly basic_displeased_che_close
with charachange

# li "That's not cheating. It's simply making use of personal contacts."
li "เปล่าโกงสักหน่อย ฉันก็แค่ใช้ประโยชน์จากคนรู้จักเท่านั้นเอง"

# hi "If you say so. Still, I get the feeling that you're more familiar with this kind of restaurant than I am."
hi "ไม่โกงก็ไม่โกง แต่นั่นแหละ ฉันรู้สึกว่าเธอน่าจะคุ้นเคยกับร้านอาหารแบบนี้ดีกว่าฉันนะ"

show lilly basic_reminisce_che_close
with charachange

with Pause(0.5)

show lilly basic_smileclosed_che_close
with charachange

# "She pauses a moment, a wistful look on her face, before softly smiling. The compliment seems to brighten her mood."
"ลิลลี่ทำหน้าเศร้าสร้อยเงียบไปครู่หนึ่งก่อนจะยิ้มหวาน ดูท่าว่าคำชมนั้นจะทำให้เธออารมณ์ดีขึ้น"

show lilly basic_planned_che_close
with charachange

# li "You can thank my former school for that. If I were to appear any less, they'd be gravely disappointed."
li "ก็ต้องขอบคุณโรงเรียนเก่าฉันเลยจ้ะ ที่โรงเรียนคงผิดหวังแย่ถ้าฉันยังทำอะไรไม่ถูกต้องตามขั้นตอนน่ะ"

# "She has mentioned her previous schooling before, but now I'm kind of curious. She seems to think a lot about her past, so I don't see any problem in asking."
"ก่อนหน้านี้ลิลลี่เคยพูดถึงเรื่องชีวิตที่โรงเรียนเก่ามาแล้ว แต่ตอนนี้ชักอยากรู้แล้วสิ ถามหน่อยคงไม่เสียหายอะไร ยังไง\nเธอก็ดูจะคิดถึงเรื่องอดีตอยู่บ่อย ๆ ด้วย"

# hi "What was that like?"
hi "ที่โรงเรียนเก่าเธอมันอารมณ์ประมาณไหนเหรอ"

show lilly basic_smile_che_close
with charachange

# li "It was prestigious, all-girls and Catholic; these facts made my parents choose it for me. Many wealthy families sent their daughters there."
li "เป็นโรงเรียนหญิงล้วนคาทอลิกที่มีชื่อเสียงน่ะจ้ะ ที่พ่อแม่ท่านเลือกให้ฉันเรียนที่นั่นก็เพราะแบบนั้นเลย ครอบครัว\nที่มีฐานะหลายครอบครัวก็ส่งลูกสาวตัวเองไปเรียนที่นั่นด้วยเหมือนกัน"

# hi "From how it sounds, life there must've been pretty strict."
hi "ฟังดูแล้วชีวิตในนั้นคงเคร่งน่าดูเลยนะ"

show lilly basic_weaksmile_che_close
with charachange

# li "I wouldn't say it was a bad experience… but you're quite right; it was very strict. Thankfully, I managed to adapt well enough and make a number of friends."
li "ก็ไม่ได้แย่หรอกจ้ะ… แต่เธอก็พูดถูก ที่นั่นน่ะเคร่งมากเลย ซึ่งยังดีที่ฉันปรับตัวได้ดีจนได้เพื่อนมากลุ่มหนึ่ง"

show lilly basic_reminisce_che_close
with charachange

# li "Unfortunately, the same can't be said for my sister. She found the atmosphere and religious aspect suffocating, and ended up leaving for a job as soon as she was able to."
li "แต่น่าเสียดายที่พี่ไม่ได้เป็นเหมือนอย่างฉัน พี่อึดอัดกับบรรยากาศของโรงเรียนกับความที่โรงเรียนนั้นเป็นโรงเรียนคริสต์\nจนสุดท้ายพอสบโอกาสพี่ก็รีบออกมาหางานทำทันทีเลย"

show lilly basic_weaksmile_che_close
with charachange

# "She gives a small, self-deprecating chuckle."
"ลิลลี่แค่นหัวเราะเย้ยตัวเอง"

# li "I shouldn't complain about it though. Not many even have the chance to go to such a school."
li "แต่ฉันก็คงบ่นอะไรไม่ได้หรอก โรงเรียนแบบนั้นน่ะใช่ว่าทุกคนจะมีโอกาสได้เข้าไปเรียนนะ"

# hi "Do you… resent your parents for sending you there, then leaving?"
hi "เธอเคย… โกรธพ่อแม่ตัวเองที่ส่งเธอให้ไปเรียนที่โรงเรียนนั้นแล้วบินไปสกอตแลนด์มั้ย"

# "She gently shakes her head."
"เธอสั่นหัวเบา ๆ"

show lilly basic_reminisce_che_close
with charachange

# li "My family is highly patriarchal. My father, business always on his mind, was entirely lost as to what to do with me."
li "ครอบครัวฉันน่ะเป็นพวกปิตาธิปไตยมาก พ่อฉันที่เอาแต่คิดถึงเรื่องธุรกิจก็เลยไม่รู้ว่าจะเอายังไงกับฉันดี"

show lilly basic_weaksmile_che_close
with charachange

# li "In the end, he made the decision that my education was of higher priority than staying with the family."
li "สุดท้ายท่านก็ตัดสินใจให้การศึกษาของฉันสำคัญกว่าการที่ฉันจะได้อยู่กับครอบครัว"

# li "He simply did what he thought was best."
li "ท่านก็แค่ทำในสิ่งที่ท่านคิดว่าดีที่สุดนั่นแหละจ้ะ"

# "To say such things so easily. What an unbelievable girl. That said, I'm a little surprised she doesn't think her blindness played any part at all… though maybe I'm being too harsh on her family."
"พูดอะไรอย่างนั้นได้หน้าตาเฉยเลยแฮะ เหลือเชื่อจริง ๆ แต่ก็แปลกใจอยู่หน่อย ๆ เหมือนกันที่ลิลลี่ไม่ได้นับเลยว่าการที่\nตัวเองตาบอดจะเป็นอีกหนึ่งปัจจัยต่อเรื่องเหล่านั้น… หรือฉันอาจจะมองครอบครัวลิลลี่ในแง่ร้ายเกินไปก็ได้"

# hi "You're too kind-hearted, you know that?"
hi "เธอเป็นคนจิตใจดีมาก ๆ เลยนะ รู้ตัวหรือเปล่า"

show lilly basic_surprised_che_close
with charachange

# li "Hmm?"
li "หืม"

# hi "Most would hate their parents for something like that."
hi "ถ้าเป็นคนอื่นนี่คงเกลียดพ่อแม่ตัวเองไปแล้วมั้ง"

show lilly basic_weaksmile_che_close
with charachange

# li "Well, some do…"
li "อืม บางคนก็เกลียดแหละจ้ะ…"

# "Oblivious to my raised eyebrow, she takes a sip from her glass. The wine slips down effortlessly, her fondness for it evidently helping her deal with the flavor of alcohol. I can't say the same goes for me."
"ลิลลี่จิบไวน์โดยที่ไม่ได้รับรู้ว่าฉันเลิกคิ้วขึ้นอยู่ เธอดื่มไวน์ได้อย่างง่ายดาย ความชอบของเธอคงจะเป็นส่วนหนึ่งที่ทำให้\nเธอทานกับรสของแอลกอฮอล์ได้ ซึ่งต่างจากฉันที่รับกับรสของแอลกอฮอล์ไม่ค่อยได้"

show lilly basic_smile_che_close
with charachange

# li "What of yourself? What was your schooling like?"
li "แล้วเธอล่ะ ที่โรงเรียนเก่าเธอเป็นยังไงบ้างเหรอ"

# hi "Mine? Let's see…"
hi "ฉันเหรอ นึกก่อนนะ…"

# hi "It was a fairly normal public school, I suppose, maybe a bit busier than the norm."
hi "ก็เป็นโรงเรียนรัฐทั่ว ๆ ไปละมั้ง อาจจะมีกิจกรรมอะไรเยอะกว่าที่อื่นหน่อย"

# hi "I did quite well in class and played in the soccer club. Since I am an only child and my parents both worked a lot, I wasted most of my free time and money at the arcade with my three friends."
hi "เรื่องเรียนก็พอใช้ได้ แล้วฉันก็เคยอยู่ชมรมฟุตบอลด้วย ด้วยความที่ฉันเป็นลูกคนเดียว พ่อแม่ก็งานยุ่ง ส่วนใหญ่\nเลยหมดเงินกับเวลาไปกับการเล่นเกมตู้กับเพื่อนอีกสามคนนี่ละ"

# hi "No matter how much I played, though, I never did manage to beat Mai at any of those machines. Even Takumi and Shin lost to her whenever they tried. Then I'd be left trying to be the responsible adult when Shin and Mai fought. Again."
hi "แต่เล่นให้ตายยังไงฉันก็ไม่เคยชนะคนที่ชื่อไมเลย จะเกมไหนก็ช่างเถอะ ขนาดทาคุมิกับชินไปลองเล่นกับไมบ้างยังแพ้เลย\nแล้วพอชินกับไมตีกันขึ้นมาทีฉันก็ต้องรับบทเป็นผู้ใหญ่ห้ามทัพอีก"

# hi "Just the four of us, aimlessly enjoying our childhood. Those were some pretty silly times."
hi "ก็สี่หน่อสนุกกันตามประสาเด็กไปเรื่อยเปื่อยน่ะแหละ เป็นอะไรที่ไร้สาระดี"

# "I catch myself as I realize that I'm starting to zone out, the days of my old school disappearing to the night sky and bright city lights outside the window."
"ฉันรีบกลับมาตั้งสติก่อนที่ตัวเองจะเหม่อไปไกลกว่านี้ ภาพวันวานจากโรงเรียนเก่าเลือนหายไป ภาพท้องฟ้ายามค่ำคืน\nที่อยู่เหนือตัวเมืองอันสว่างไสวซึ่งอยู่นอกหน้าต่างเข้ามาแทน"

# "Lilly's face is an odd mixture of curiosity and sympathy. Given her strict schooling, I suppose something like this would seem an interesting contrast to the only life she's known."
"ลิลลี่ทำหน้าสงสัยใครรู้ ทว่ายังทำท่าคล้ายเข้าใจ ถ้าดูจากความเคร่งของโรงเรียนเก่าลิลลี่แล้ว เธอคงจะสนใจเรื่องอะไร\nอย่างนี้ซึ่งไม่เหมือนกับชีวิตแบบเดียวที่เธอเคยได้สัมผัสมา"

show lilly basic_satisfied_che_close
with charachange

# li "It sounds like your previous school was a lot of fun."
li "โรงเรียนเก่าเธอฟังดูสนุกน่าดูเลยนะจ๊ะ"

# hi "I'm not really sure how much of it is nostalgia, but there are some nice memories."
hi "ก็เป็นความทรงจำที่ดีนะ ถึงจะไม่ค่อยแน่ใจก็เถอะว่าที่คิดอย่างนี้มันเป็นเพราะความคิดถึงล้วน ๆ เลยหรือเปล่า"

# hi "That's in the past though. I can't go back there now, but through my accident I found a new life I'd never have imagined leading."
hi "แต่มันก็เป็นอดีตไปแล้วน่ะนะ จะให้กลับไปอยู่ตรงนั้นก็ไม่ได้แล้ว แต่อุบัติเหตุครั้งนั้นก็ทำให้ฉันได้มาเจอกับชีวิตใหม่ที่\nตัวฉันในอดีตคงคิดไม่ถึงเลยว่าจะต้องมาเจอ"

# hi "The peace and calm of Yamaku, a new direction for my future in science, the friendship of Shizune, Misha and Hanako, and most of all, you."
hi "ทั้งความเงียบสงบของยามากุ ทั้งเส้นทางอนาคตใหม่ของฉันในเส้นทางวิทยาศาสตร์ ทั้งมิตรภาพกับชิซูเนะ มิช่า\nฮานาโกะ และที่สำคัญที่สุดเลยก็คือเธอ"

scene ev lilly_touch_cheong
with whiteout

# "She gives a deep, genuine smile as she moves her hands towards me, her fingers just lightly searching out my face before softly caressing my cheek."
"ลิลลี่ระบายยิ้มกว้างอย่างจริงใจพลางยื่นมือมาหาฉัน เธอแตะหน้าฉันเบา ๆ ก่อนจะเลื่อนมาจับแก้มฉันเอาไว้\nอย่างนุ่มนวล"

scene bg city_restaurant at right
show lilly basic_smileclosed_che_close:
    center
    ypos 1.1
with whiteout

# "Her hand reluctantly retreats after a second of warm silence, as we notice the waiter arriving with our meals."
"มีเพียงความเงียบแสนอบอุ่นอยู่ชั่วขณะ เธอถอนมือกลับละล้าละลังเมื่อสังเกตว่าบริกรกำลังนำรายการที่เราสั่งมาเสิร์ฟ"

# "Lilly does a deft job of covering her condition, except for the fact that her nod to him is slightly misaligned due to his silence."
"ลิลลี่นั้นทำตัวราวกับว่าตัวเองเป็นคนที่สายตาปกติดีได้ดีทีเดียว จะติดนิดหน่อยก็ตรงที่ว่าเธอพยักหน้าให้บริกร\nไปผิดทางเล็กน้อยเพราะไม่มีสุ้มเสียงช่วยนำทาง"

# "She really seems to work hard at appearing as normal as possible in public. While I noticed it long ago, I still can't quite gauge whether it's a want to not be treated differently, a slight sense of vanity, or some mixture of both."
"เธอพยายามอย่างมากที่จะทำให้ตัวเองดูเหมือนเป็นคนปกติเมื่อต้องอยู่กับคนอื่น แม้ฉันจะสังเกตได้มานานแล้ว แต่ก็ยัง\nไม่แน่ใจนักว่าที่เธอทำเช่นนี้เพราะเธออยากให้คนปฏิบัติกับเธอเหมือนอย่างคนปกติ เพราะเรื่องศักดิ์ศรีส่วนตัว\nหรือทั้งสองอย่างรวม ๆ กัน"

scene ev lilly_restaurant_eat
with shorttimeskip

# "The dish served lives up to the salad name, and the portion's pleasantly large. With sliced eggs and tomato, it looks very enticing indeed."
"สลัดที่ถูกนำมาเสิร์ฟนั้นหรูสมชื่อ แถมยังได้เยอะจุใจด้วย มีมะเขือเทศกับไข่ต้มหั่นชวนน้ำลายสอ"

# "Lilly takes her knife in one hand and fork in the other, quickly getting to work on the dish as I do. It's later than when we usually have dinner, so we're both eager to dig in."
"ลิลลี่ใช้มือข้างหนึ่งหยิบมีดแล้วใช้มืออีกข้างหยิบส้อมรีบจัดการกับอาหารตรงหน้าพร้อม ๆ กันกับฉัน พวกเราต่างหิว\nเพราะตอนนี้เลยเวลาปกติที่จะกินข้าวเย็นกันแล้ว"

scene ev lilly_restaurant_chew
with locationchange

# "My cautious skewering of leaves and vaguely meat-like squares with my fork is matched by Lilly's silent and measured prodding and chewing."
"ฉันค่อย ๆ ใช้ส้อมจิ้มผักกับก้อนเหลี่ยม ๆ ที่คล้ายเนื้อในจานกิน ส่วนลิลลี่ก็จิ้มอาหารในจานขึ้นมาใส่ปากเคี้ยวกิน\nอย่างเป็นกระบวนการอยู่เงียบ ๆ"

# "An occasional tap around the sides of a piece of the food to work out its edges is the only giveaway to her lack of sight."
"อย่างเดียวที่เป็นตัวบอกว่าลิลลี่มองไม่เห็นคือการที่บางครั้งเธอจะแตะตามขอบอาหารในจานเพื่อหาว่าขอบนอก\nอยู่ตรงไหน"

scene bg city_restaurant at right
with locationchange

# "I'm done with my meal in little time, Lilly taking the last few bites as I sit observing her."
"ไม่นานฉันก็กินจนหมด ฉันนั่งมองลิลลี่ที่กำลังกินคำสองคำสุดท้ายจนหมด"

show lilly basic_smile_che_close:
    center
    ypos 1.1
with charaenter

# li "Finished, Hisao?"
li "กินหมดแล้วเหรอฮิซาโอะ"

# hi "Yeah. It was pretty nice."
hi "อื้ม อร่อยดีนะ"

# "That much is very true. I never thought a simple salad could be so tasty and filling, but then again, I suppose that's why it costs so much to eat here."
"ซึ่งก็อร่อยอย่างที่พูดจริง ๆ ไม่คิดเลยว่าสลัดพื้น ๆ อย่างนี้จะทั้งอร่อยและกินจนอิ่มได้ แต่ก็นะ คงจะสมกับราคานั่นแหละ"

show lilly basic_smileclosed_che_close
with charachange

# "Content with my appraisal, and evidently agreeing, Lilly gives a small nod."
"ลิลลี่พยักหน้าน้อย ๆ ด้วยความพอใจและทำท่าเห็นด้วยกับคำชมนั้น"

# hi "You know, given that you're part foreign, exotic-looking and quite pretty, I'm surprised that nobody's ever confessed to you before."
hi "เนี่ย ฉันแปลกใจเหมือนกันนะที่ไม่เคยมีใครมาสารภาพรักกับเธอมาก่อนเลย ทั้งที่เธอเป็นลูกครึ่งหน้าตาสะสวยอย่างนี้\nแท้ ๆ"

show lilly basic_planned_che_close
with charachange

# li "You're assuming nobody did."
li "เธอคิดไปเองว่าไม่มี"

# "The simple statement takes me off guard. I shouldn't be surprised, given that I was complimenting her just moments before."
"คำพูดเรียบ ๆ นั้นมาแบบไม่ทันให้ฉันได้ตั้งตัว ก็คงไม่แปลกละมั้ง ก็เมื่อกี้ฉันยังชมเธออยู่เลย"

# hi "Really?"
hi "จริงเหรอ"

show lilly basic_smile_che_close
with charachange

# li "I've received several confessions, both in this school and my previous one."
li "มีคนมาสารภาพรักกับฉันหลายคนเลยจ้ะ ทั้งที่โรงเรียนเก่า ทั้งที่ยามากุด้วย"

show lilly basic_weaksmile_che_close
with charachange

# li "Adolescence is a funny time."
li "ช่วงวัยรุ่นน่ะเป็นช่วงที่ประหลาดดีนะ"

# "She's kinda talking as if she's above it herself…"
"พูดเหมือนอย่างกับว่าตัวเองไม่เคยเป็นวัยรุ่นมาก่อนงั้นแหละ…"

# hi "Huh. How easily you say such a thing."
hi "หืม เธอพูดอะไรอย่างนั้นได้ด้วยเหรอ"

show lilly basic_surprised_che_close
with charachange

with Pause(0.5)

show lilly basic_cheerful_che_close
with charachange

# "Lilly looks surprised for a moment, before a playful smirk covers her face."
"ลิลลี่ทำท่าตกใจอยู่ครู่หนึ่งก่อนจะยิ้มซุกซน"

# li "Is that… jealousy?"
li "นี่เธอ… หึงเหรอ"

# hi "What? No. It isn't."
hi "ฮะ? เปล่า ไม่ได้หึง"

show lilly basic_giggle_che_close
with charachange

# li "You're a bad liar, Hisao. You should take that into account."
li "เธอเป็นคนที่โกหกไม่เนียนเลยนะฮิซาโอะ รู้ตัวหน่อยก็ดีนะจ๊ะ"

show lilly basic_smileclosed_che_close
with charachange

# li "Then again, I do appreciate how sincere you are. Even if you don't intend to be, sometimes."
li "แต่ฉันก็ยินดีที่เธอเป็นคนจริงใจอย่างนี้นะ ถึงบางครั้งเธอไม่ได้จงใจที่จะทำตัวอย่างนั้นก็เถอะ"

# li "I think your honesty will always serve you well when dealing with others."
li "ฉันว่าความซื่อสัตย์ของเธอที่แหละที่จะช่วยให้เธอรับมือกับใครต่อใครได้ดีเลย"

# "I clear my throat in mock disapproval of this whole business and try to steer the conversation elsewhere."
"ฉันทำเป็นกระแอมไม่พอใจกับเรื่องที่กำลังคุยกันอยู่นี้พลางหาทางเปลี่ยนเรื่อง"

# hi "To tell the truth, though, I do prefer solitude to being surrounded by others. I don't think I could maintain a social circle like you do."
hi "แต่ว่าตามตรงนะ ฉันชอบอยู่คนเดียวมากกว่า จะให้ไปเข้าสังคมอะไรเหมือนอย่างเธอนี่คงไม่ไหว"

show lilly basic_listen_che_close
with charachange

# "She contemplates this for a moment."
"ลิลลี่ครุ่นคิดอยู่ครู่หนึ่ง"

show lilly basic_smile_che_close
with charachange

# li "I don't think that's true either."
li "ฉันว่าไม่จริงเลยนะ"

show lilly basic_smileclosed_che_close
with charachange

# li "I've seen how gentle and caring you are around Hanako, and you get on marvelously well with others, even those whom you hardly know. I think you're quite adept at social situations."
li "เวลาอยู่กับฮานาโกะเธอก็ทำตัวดีจะตายไป แถมยังเข้ากับคนอื่นได้ดีมากด้วย ขนาดกับบางคนที่เธอแทบไม่รู้จักก็ยัง\nเข้ากันได้เลย ฉันว่าเธอก็ปรับตัวไปกับสังคมอะไรได้ดีพอสมควรเลยนะ"

show lilly basic_cheerful_che_close
with charachange

# li "But on that note, what of your confessions, Hisao? I'm sure someone like you must have had at least one admirer."
li "แต่จะว่าไป แล้วเธอล่ะจ๊ะฮิซาโอะ เคยมีใครมาสารภาพรักหรือเปล่า คนอย่างเธอต้องมีคนมาชอบสักคนแหละ"

# "As I open my mouth to speak, I can feel my face turn slightly dour. At times like this, I secretly appreciate the fact that she can't see my expressions."
"จังหวะที่กำลังจะเปิดปากพูดก็รู้สึกได้ว่าตัวเองหน้าเบ้ไปเล็กน้อย กับเรื่องอะไรแบบนี้นี่แหละที่ฉันจะนึกยินดีอยู่ในใจ\nที่ลิลลี่มองไม่เห็นสีหน้าฉัน"

# hi "Just… one. Her name was Iwanako."
hi "แค่… คนเดียว ชื่ออิวานาโกะน่ะ"

# hi "It was when she confessed to me that I had my heart attack. There in the woods, during winter."
hi "ตอนที่ฉันหัวใจวายก็ตอนที่อิวานาโกะมาสารภาพรักนั่นแหละ กลางป่าฤดูหนาวเลย"

show lilly basic_oops_che_close
with charachange

# "Lilly finds herself speechless, not expecting for the topic to move into such an area."
"ลิลลี่อึ้งไปด้วยไม่คิดว่าเรื่องที่คุยจะมาแนวนี้ได้"

# "My condition has always been something of a concern for her, something that I strive to minimize despite my body's best efforts to the contrary."
"เธอเป็นห่วงเรื่องอาการของฉันมาตลอด ซึ่งฉันก็พยายามไม่ทำให้เธอต้องเป็นห่วง แม้ร่างกายจะไม่เอื้อให้ทำอย่างนั้น\nสักเท่าไหร่"

# hi "Afterwards, she visited me for a while when I was in the hospital. For weeks she came in and talked. It was usually just smalltalk or classroom gossip, but that was enough."
hi "หลังจากนั้นตอนที่ฉันเข้าโรงพยาบาลอิวานาโกะก็มาเยี่ยมอยู่อยู่พักหนึ่งนะ มาเยี่ยมมาคุยอยู่สักสองสามสัปดาห์ได้มั้ง\nก็คุยกันเรื่อยเปื่อยบ้าง ไม่ก็เรื่องที่โรงเรียนบ้าง ซึ่งแค่นั้นฉันก็พอใจแล้วละ"

# hi "But eventually… she just stopped coming."
hi "แต่สุดท้าย… ก็ไม่มาเยี่ยมอีกเลย"

# hi "She was there every day. Then every other day. Then once a week. Then finally, one day, she just stopped visiting entirely."
hi "ทีแรกก็มาทุกวัน แล้วก็มาวันเว้นวัน แล้วก็มาสัปดาห์ละวัน จนในที่สุดวันหนึ่งก็ไม่มาอีกเลย"

show lilly basic_sleepy_che_close
with charachange

# li "Did you ever… see her again?"
li "แล้วหลังจากนั้นเธอ… ได้เจออิวานาโกะอีกมั้ย"


label th_choiceL24:
menu:
    with menueffect

    # "Wrapped in my own little world, I shake my head before remembering the futility of the gesture."
    "ฉันมัวแต่จมอยู่กับเรื่องราวของตัวเองจนเผลอสั่นหัวลืมไปว่าทำท่าปฏิเสธไปอีกฝ่ายก็ไม่ได้รับรู้ด้วย"

    # "Mention the letter.":
    "พูดถึงเรื่องจดหมาย":
        return m1

    # "Drop the subject.":
    "ตัดบท":
        return m2

#[1]
# +1 Good End

label th_L24a:

# "The memory of that single letter Iwanako sent me comes back to my mind."
"ความทรงจำเรื่องจดหมายจากอิวานาโกะฉบับนั้นแล่นเข้ามาในความคิด"

# hi "I never saw her again, but after I was sent to Yamaku… she wrote me one letter."
hi "ไม่ได้เจอกันอีกเลย แต่หลังจากที่ฉันมาเรียนที่ยามากุ… อิวานาโกะเขียนจดหมายฉบับหนึ่งส่งมา"

# "Lilly's face shows an expression I know well. I've piqued her interest. I'd be slightly offended that it's simply a matter of curiosity for her, but she's never been very good at masking her reactions."
"ลิลลี่ทำสีหน้าที่ฉันคุ้นเคยดี เธอสนใจอยากรู้ขึ้นมาแล้ว ก็แอบรู้สึกเคืองอยู่นิดหน่อยเหมือนกันที่ลิลลี่สนใจเรื่องนี้ด้วย\nความอยากรู้ส่วนตัวเท่านั้น แต่ลิลลี่ก็เป็นคนที่เก็บอาการไม่เก่งอยู่แล้วละนะ"

# hi "In hindsight, it really didn't say much. What was going on in my old class, how she was faring, and, almost as an afterthought, that it was probably best for the both of us that we don't see each other again."
hi "พอลองคิดดูแล้วจดหมายมันก็ไม่ได้มีอะไรหรอก ทำนองว่าที่โรงเรียนนู่นเป็นยังไงบ้าง ตัวเองสบายดีหรือเปล่า แล้วก็\nบอกเหมือนทิ้งทวนว่าถ้าเราสองคนไม่ได้เจอกันอีกเลยคงจะดีกว่า"

# hi "After reading it, I ended up reassessing a lot of things I thought I'd managed to work out. For the most part, that letter reminded me that the world around me was still moving, and just how much I'd become isolated from it."
hi "พออ่านแล้วฉันก็มานั่งคิดอะไรหลายอย่างที่ฉันคิดว่าจัดการไปเรียบร้อยแล้วนะ ซึ่งหลัก ๆ จดหมายฉบับนั้นก็เตือนฉัน\nว่าโลกรอบตัวฉันยังหมุนต่อไป แล้วเตือนด้วยว่าฉันปลีกห่างจากโลกนั้นมาไกลแค่ไหนแล้ว"

# hi "And… I guess it also reminded me of what I'd lost."
hi "แล้วก็… เตือนว่าฉันเสียอะไรไปด้วยละมั้ง"

show lilly basic_emb_che_close
with charachange

# "She gives the information some thought before her face lights up in realization. No doubt she's worked out that it was this letter which had contributed to my angst during that lunch on the rooftop."
"ลิลลี่พินิจสิ่งที่ฉันเล่าก่อนจะทำหน้าเหมือนนึกอะไรได้ คงจะรู้แล้วแหละว่าจดหมายฉบับนี้แหละคือตัวการที่ทำให้ฉัน\nอารมณ์ไม่ค่อยดีตอนที่กินข้าวเที่ยงด้วยกันบนดาดฟ้าตอนนั้น"

# "It's a rare sight to see Lilly quite so lost for words, her entire persona is a little deflated from her earlier rapt interest. As charismatic as she is, in the end that isn't any replacement for life nor relationship experience."
"ซึ่งฉันก็ไม่ค่อยได้เห็นลิลลี่อึ้งจนเงียบไปอย่างนี้บ่อย ๆ เท่าไหร่ ท่าทีเมื่อครู่ที่ดูสนใจนั้นหมองลงไปเล็กน้อย ยังไงเสีย\nเสน่ห์มากล้นของเธอก็คงเอามาชดเชยชีวิตหรือประสบการณ์ในความสัมพันธ์ไม่ได้อยู่ดีละนะ"

show lilly basic_reminisce_che_close
with charachange

# li "Perhaps… it is better she sent it than not."
li "บางที… การที่ส่งจดหมายมาอย่างนั้นก็อาจจะดีกว่าการไม่ส่งมาเลยก็ได้นะ"

# hi "How's that?"
hi "ยังไงเหรอ"

show lilly basic_weaksmile_che_close
with charachange

# li "It can be difficult to work out how best to communicate with those you haven't met in a long time. All the more so, considering your separate situations."
li "บางทีมันก็ลำบากใจเหมือนกันว่าจะสื่อสารกับคนที่ไม่ได้เจอกันมานานยังไงดีน่ะจ้ะ แล้วยิ่งกับเธอกับอิวานาโกะที่มีเรื่อง\nระยะห่างอะไรอีก"

# li "Instead of doing what was easiest, she built up the courage to talk to you one last time; not only for her sake but, from how it sounds, for yours as well."
li "แทนที่จะเลือกหายไปเงียบ ๆ ให้สะดวกตัวเองที่สุด อิวานาโกะเขาก็เลือกที่จะรวบรวมความกล้ามาคุยกับเธอเป็น\nครั้งสุดท้าย ซึ่งเท่าที่ฟังดูแล้ว ที่ทำไปน่ะไม่ใช่แค่เพื่อตัวเอง แต่ก็เพื่อเธอด้วย"

# hi "Maybe. I don't hate her for it, not that I really ever did, but… I don't know."
hi "มั้งนะ ฉันก็ไม่ได้โกรธอิวานาโกะที่เขียนจดหมายมาหรอก ซึ่งฉันก็ไม่เคยโกรธอยู่แล้วด้วยอะนะ แต่ว่า… ไม่รู้สิ"

# "Probably a more noncommittal answer than I should give, but it isn't without cause. I've never looked at the situation from Iwanako's perspective like that before."
"อาจจะเป็นคำตอบที่ฟังดูเลื่อนลอยเกินสมควร ซึ่งที่ตอบไปอย่างนั้นก็เพราะฉันไม่เคยมองเรื่องนี้จากมุมของตัว\nอิวานาโกะจริง ๆ"

#[2]

label th_L24b:

# "I really don't want to bring up Iwanako any more than necessary. This date is, after all, for me and Lilly. I don't want to think about a previous relationship at a time like this."
"ฉันไม่อยากพูดถึงเรื่องอิวานาโกะเกินความจำเป็นสักเท่าไหร่ ยังไงเสีย เดตนี้ก็เป็นเดตของฉันกับลิลลี่ ฉันไม่อยากมานั่ง\nฟื้นฝอยเรื่องความสัมพันธ์เก่าเอาในจังหวะอย่างนี้"

# hi "No, that was the last I saw of her. We never talked again, either."
hi "ไม่ได้เจอเลย ฉันได้เห็นหน้าอิวานาโกะเป็นครั้งสุดท้ายก็ตอนนั้นแหละ จากนั้นก็ไม่ได้คุยกันอีกเลย"

# End split

label th_L24c:

# "Seconds pass in silence before Lilly speaks again."
"มีเพียงความเงียบอยู่ครู่หนึ่งก่อนลิลลี่จะพูดขึ้นมาอีกครั้ง"

show lilly basic_sad_che_close
with charachange

# li "Moving to Yamaku must have been hard for you, having your friends and even your girlfriend taken from you for no fault of your own."
li "เธอคงลำบากน่าดูเลยนะจ๊ะที่ต้องย้ายมาที่ยามากุ ต้องเสียทั้งเพื่อนทั้งแฟนไปทั้งที่ไม่ใช่ความผิดของตัวเองเลยแท้ ๆ"

# hi "The worst of it passed while I was in the hospital. When all that surrounds you is four white walls and a small television, your mind takes on a life of its own."
hi "ช่วงที่หนักที่สุดก็เป็นตอนที่อยู่โรงพยาบาลนี่แหละ พอรอบตัวมีแต่ผนังขาวสี่ด้านกับโทรทัศน์เครื่องเล็ก ๆ แล้วสมอง\nมันก็ล่องลอยคิดอะไรไปหลายอย่างเลย"

# hi "It's like my old school, I guess. I just try not to dwell on what's happened and keep thinking ahead."
hi "ที่นี่ก็คงเหมือนที่โรงเรียนเก่าละมั้ง แค่ห้ามใจไม่ให้จมอยู่กับอดีตแล้วคอยมองไปข้างหน้าต่อไป"

# hi "All that reminiscing does is get me down, and it's largely thanks to you that it feels like things are finally getting back on track."
hi "มัวแต่ย้อนรำพึงไปก็เสียสุขภาพจิตเปล่า ๆ ซึ่งหลัก ๆ ก็เพราะเธอเลยนะที่ฉันมีความรู้สึกว่าอะไร ๆ เริ่มกลับมา\nเข้ารูปเข้ารอยแล้ว"

show lilly basic_veryemb_che_close
with charachange

# li "That's… pleasing to hear, Hisao."
li "เธอพูดอย่างนี้… ฉันก็ดีใจจ้ะ"

# "She lowers her face slightly, her expression pensive. I guess I went too far and embarrassed her."
"ลิลลี่ก้มหน้าลงเล็กน้อยพลางทำหน้าเหมือนคิดอะไรอยู่ สงสัยคงพูดเกินไปจนอายแน่เลย"

# hi "I suppose you went through something a bit like what I did when you entered Yamaku anyway, right? I imagine the vast majority of our school's students did, after all."
hi "ตอนที่เธอย้ายมาอยู่ที่ยามากุก็คงเจออะไรเหมือนกับฉันใช่มั้ยล่ะ หลายคนที่มาเรียนที่นี่ก็คงมีเรื่องอะไรอย่างนี้\nคล้าย ๆ กันแหละนะ"

# hi "You said yourself that you made friends in your old school. I can't imagine many followed you."
hi "เธอเล่าว่าเธอมีเพื่อนที่โรงเรียนเก่าด้วยนี่ คงมีไม่กี่คนใช่มั้ยที่ยังติดต่อกับเธออยู่"

show lilly basic_displeased_che_close
with charachange

# "Lilly's deep smile drops, her expression unexpectedly darkening. Even her hands retreat to her lap."
"ลิลลี่หุบยิ้มทำหน้าหมองผิดคาด ทั้งยังเลื่อนมือกลับมาวางที่ตักตัวเองด้วย"

# "After a long while, she speaks."
"ผ่านไปพักใหญ่เธอก็พูดขึ้น"

show lilly basic_reminisce_che_close
with charachange

# li "Hisao… can you promise not to tell anyone else what I'm about to—"
li "ฮิซาโอะ… เธอรับปากกับฉันได้มั้ยว่าจะไม่เอาเรื่องนี้ไปบอก—"

# hi "I promise."
hi "สัญญา"

# "She looks slightly taken aback by my serious tone, but then relents and smiles weakly before continuing."
"ลิลลี่ดูตกใจเล็กน้อยกับน้ำเสียงจริงจังของฉัน แต่จากนั้นก็ทำท่าโล่งใจแล้วยิ้มเหงา ๆ ก่อนจะพูดต่อ"

show lilly basic_weaksmile_che_close
with charachange

# li "When I moved to Yamaku, I did regret losing the friends I'd had at my other school."
li "ฉันก็เสียใจอยู่เหมือนกันที่ต้องเสียเพื่อนไปตอนที่ย้ายมาอยู่ที่ยามากุ"

show lilly basic_reminisce_che_close
with charachange

# li "But there was one person whom I most regretted not seeing again. He was the reason I took up English as a future career."
li "แต่มีอยู่คนหนึ่งที่ฉันเสียใจที่สุดว่าจะไม่ได้เจอกันอีกแล้ว เขาเป็นคนที่ทำให้ฉันเลือกภาษาอังกฤษเป็นเส้นทางอาชีพ\nในอนาคตเลยละจ้ะ"

# "“He?” Considering she came from an all-girls school, that can't have been a schoolmate then…"
"“เขา”? ถ้าโรงเรียนเก่าลิลลี่เป็นโรงเรียนหญิงล้วนก็แปลว่าไม่ใช่เพื่อนที่โรงเรียน ถ้างั้น…"

# li "I rejected the confessions I'd received until then for him. Every time I improved my English skills, his praise was my most treasured reward."
li "ตอนนั้นที่ฉันปฏิเสธทุกคนที่มาสารภาพรักเพื่อเขาเลย ทุกครั้งที่ทักษะภาษาอังกฤษของฉันดีขึ้น คำชมของเขา\nจะเป็นเหมือนดั่งรางวัลล้ำค่าของฉัน"

show lilly basic_weaksmile_che_close
with charachange

# li "It's funny, isn't it? Someone like me, able to boast about the people who have set eyes on me, liking someone so utterly unattainable as my tutor."
li "ตลกดีเนอะ คนอย่างฉันที่กล้าอวดว่ามีคนมากมายหมายตามองฉันอยู่ แต่กลับมาชอบคุณครูที่ไม่ว่าจะยังไงก็คง\nคว้าไม่ได้"

# li "It truly is the most ridiculous thing…"
li "เป็นอะไรที่งี่เง่าที่สุดเลยละจ้ะ…"

# hi "Did you…?"
hi "แล้วเธอ…?"

# "She quickly shakes her head from side to side."
"เธอรีบสั่นหัวไปมา"

show lilly basic_displeased_che_close
with charachange

# li "I couldn't. Even then, I knew it was impossible."
li "ไม่ได้หรอกจ้ะ ขนาดตัวฉันตอนนั้นยังรู้เลยว่าเป็นไปไม่ได้"

# "A silence reigns over both of us."
"เราสองคนเงียบกันไป"

# "This does seem to explain her ardent focus on her future in teaching English, but I can't help thinking of her confession to me."
"พอได้ฟังแล้วก็เข้าใจว่าทำไมลิลลี่ถึงมุ่งมั่นกับอาชีพการสอนภาษาอังกฤษขนาดนั้น แต่ก็อดไม่ได้ที่จะย้อนนึกไปถึง\nตอนที่เธอสารภาพรักกับฉัน"

# "She lost him without ever letting her feelings be known… did she somehow fear that would happen again, but with me?"
"ลิลลี่เสียเขาไปโดยที่ไม่เคยบอกความรู้สึกตัวเองให้ได้รับรู้… หรือเธอกลัวว่าเรื่องจะซ้ำรอยเดิมกับฉันอีก?"

# "I don't really know what to make of it. I've heard of such relationships before; taboos born of such things as puberty and youth. The fact that she had the good judgment not to act on it, though, is heartening."
"ไม่รู้จะว่ายังไงดีเหมือนกัน ฉันก็เคยได้ยินเรื่องความสัมพันธ์ต้องห้ามทำนองนี้ที่เป็นเรื่องระหว่างวัยมาก่อน แต่ฉันก็\nใจชื้นที่เธอยังมีสติพอที่จะไม่ไปไกลกว่านั้น"

show lilly basic_emb_che_close
with charachange

# li "I know this must sound strange, but please… don't think of me…"
li "ฉันรู้ดีว่าคงฟังดูแปลก แต่ได้โปรด… อย่ามองฉันว่า…"

# hi "Why would I think any less of you for that?"
hi "เรื่องแค่นี้ ทำไมฉันจะต้องมองเธอไม่ดีด้วย"

# hi "To be honest, I think he must have been a very nice person if you liked him so much. Not only that, but you stopped yourself before going too far."
hi "ว่าตามตรง ฉันว่าเขาต้องเป็นคนที่ดีมาก ๆ เธอถึงได้ชอบ แล้วไม่พอ เธอยังห้ามตัวเองไม่ให้ถลำลึกไปกว่านั้นได้ด้วย"

with Pause(1.0)

show lilly basic_arablush_che_close
with charachange

# "For a moment, she looks somewhat lost. Most unexpectedly though, it isn't a second before she starts to laugh. The sound takes me off guard. It's not a giggle, nor a restrained chuckle, but honest and genuine laughter."
"ลิลลี่ทำหน้าสับสนอยู่แวบหนึ่ง แต่ไม่นานเธอก็เริ่มหัวเราะผิดไปจากความคาดหมายของฉันโดยสิ้นเชิงจนไม่ทันได้ตั้งตัว\nเป็นเสียงหัวเราะที่ไม่ได้เป็นการหัวเราะคิกคักหรือแค่นหัวเราะ แต่เป็นการหัวเราะจริง ๆ จากใจ"

# "I find myself smiling, and not just at her display of relief and happiness, but for her to trust me enough to let me see this most private of secrets."
"ฉันยิ้ม แต่ไม่ได้ยิ้มให้กับท่าทีซึ่งโล่งใจหรือมีความสุขของเธอ หากแต่ยิ้มให้กับเธอที่ไว้ใจฉันมากพอที่จะเล่าความลับ\nซึ่งเป็นเรื่องลับสุดยอดนี้ให้ฉันฟัง"

scene ev lilly_touch_cheong
with whiteout

# "Before I realize it, I feel her palm touching my face. Her touch is gentle as ever, with her thumb slowly stroking my cheek."
"พอรู้ตัวอีกทีลิลลี่ก็มาจับหน้าฉันแล้ว เป็นสัมผัสอันอ่อนโยนอย่างเคย เธอไล้นิ้วไปตามแก้มฉันช้า ๆ"

# li "You're kind, Hisao. I really do love you."
li "เธอน่ะแสนดีนะฮิซาโอะ ฉันละรักเธอจริง ๆ"

# "Seeing her face like this, with her palm gently caressing my face… I think tonight has been a wonderful night."
"พอได้เห็นใบหน้าเธอและได้รับสัมผัสอันอ่อนโยนจากฝ่ามือด้วยใบหน้าของฉันอย่างนี้แล้ว… ก็รู้สึกว่าค่ำคืนนี้ช่างเป็น\nค่ำคืนที่วิเศษเหลือเกิน"

# hi "I guess we've both had pretty weird pasts, eh?"
hi "เราสองคนนี่มีอดีตอะไรที่พิลึกดีเนอะ"

# li "I think by most standards, our present is rather odd as well."
li "ฉันว่าคนส่วนมากก็คงมองว่าปัจจุบันของเราก็พิลึกเหมือนกันแหละจ้ะ"

# "I smile and hang my head. This woman can easily run rings around me, of that I'm quite sure."
"ฉันยิ้มก้มหน้าลง ที่แน่ ๆ คือเธอคนนี้สามารถไล่ต้อนฉันให้จนมุมได้ง่าย ๆ เลย"

scene bg city_restaurant at right
with whiteout

# "I look back around the room with its continuing quiet hum of patrons."
"ฉันมองไปรอบ ๆ ร้านที่มีเสียงลูกค้าคุยกันดังอยู่เบา ๆ"

# hi "This place probably fits into the “odd” category, too."
hi "ร้านนี้ก็คงนับได้ว่า “แปลก” เหมือนกันนะ"

show lilly basic_weaksmile_che_close:
    center
    ypos 1.1
with charaenter

# li "It is a tad… overbearing."
li "ออกจะ… เกินรับไหวไปหน่อย"

# hi "That's one word for it, yes."
hi "นั่นแหละ ๆ ประมาณนั้น"

# "I catch the eye of a scurrying waiter, a short, scrawny guy no older than twenty. He kind of reminds me of Kenji, though unlike him the waiter isn't dressed for winter during midsummer."
"ฉันหันไปสบตากับบริกรผอมกะหร่องตัวเตี้ยที่อายุไม่น่าเกินยี่สิบซึ่งเดินก้าวฉับ ๆ อยู่ เห็นแล้วก็นึกถึงเคนจิ จะไม่เหมือน\nก็ตรงที่บริกรคนนี้ไม่ได้ใส่ชุดกันหนาวตอนหน้าร้อน"

show lilly basic_smileclosed_che_close
with charachange

# "After a curt bow and an offer to remove our plates, Lilly asks for the bill politely and softly."
"พอบริกรคนนั้นมาโค้งตัวตามมารยาทเพื่อเตรียมจะเก็บจานแล้วลิลลี่ก็ขอใบเสร็จอย่างสุภาพด้วยน้ำเสียงนุ่มนวล"

# "With expert coordination, he maneuvers around the tables, our plates in hand, to retrieve our bill."
"เขาขยับตัวมาเก็บจานอย่างเชี่ยวชาญแล้วเดินเพื่อไปรับใบเสร็จของพวกเรา"

# "In no time he reappears through the doors, smartly handing our bill to Lilly."
"ไม่นานเขาก็เดินออกมาจากประตูอีกครั้งแล้วยื่นใบเสร็จให้ลิลลี่อย่างฉับไว"

show lilly basic_smile_che_close
with charachange

# "…who promptly hands it to me, causing him to raise an eyebrow."
"…และลิลลี่ก็ส่งต่อใบเสร็จมาให้ฉันจนบริกรคนนั้นเลิกคิ้วสงสัย"

# "As I read the small computer-printed leaflet, the cost is considerably more than I expected."
"ฉันดูรายการตัวเล็ก ๆ ในใบเสร็จซึ่งพิมพ์มาจากเครื่องคอมพิวเตอร์ แพงกว่าที่คิดพอสมควรเลยแฮะ"

show lilly basic_surprised_che_close
with charachange

# li "Hisao?"
li "ฮิซาโอะ"

# hi "Oh… uh…"
hi "อ้อ… เอ่อ…"

show lilly basic_smileclosed_che_close
with charachange

# "I quickly stammer out the amount, to which Lilly merely nods and reaches for her purse."
"ฉันลนลานอึกอักพูดตัวเลขออกไป ลิลลี่เพียงพยักหน้ารับแล้วหยิบกระเป๋าสตางค์ของเธอออกมา"

# "Giving her card to the waiter, he disappears once again."
"ลิลลี่ยื่นบัตรให้บริกร จากนั้นเขาก็เดินหายไปอีกครั้ง"

# hi "That was… a disproportionately large amount of money."
hi "มันก็… หลายสตางค์อยู่นะนั่นน่ะ"

show lilly basic_emb_che_close
with charachange

# "The statement seems to make Lilly slightly uncomfortable."
"ดูท่าว่าคำพูดนั้นจะทำให้ลิลลี่อึดอัดเล็กน้อย"

show lilly basic_weaksmile_che_close
with charachange

# li "My family leaves me more than enough for my education. The same goes for my sister, though she dislikes being reminded of that fact."
li "ครอบครัวฉันส่งเงินมาให้กับเรื่องเรียนของฉันเยอะแบบเหลือ ๆ เลยละจ้ะ พี่ฉันก็ได้เหมือนกัน แต่พี่จะไม่ชอบให้ใคร\nมาพูดถึงเรื่องนั้นเลย"

show lilly behind_cheerful_che_close
with charachange

# li "That said, I too dislike throwing money about. But this one time I think I can make an exception. Just for you."
li "ซึ่งฉันก็ไม่ชอบการผลาญเงินไปทั่วเหมือนกันนั่นละจ้ะ แต่ครั้งนี้ถือว่าเป็นข้อยกเว้นเพื่อเธอโดยเฉพาะเลยแล้วกัน"

# hi "Not only did you choose our date, but you paid for both of us as well…"
hi "เลือกร้านนัดเดตให้ไม่พอ แล้วยังเลี้ยงอีกต่างหาก…"

# "I take the bridge of my nose in my fingers."
"ฉันใช้ข้อนิ้วบีบสันจมูกตัวเอง"

# hi "I can't believe how high you have set the bar for our next date."
hi "ไม่อยากเชื่อเลยว่าเธอจะตั้งมาตรฐานกับการเดตครั้งหน้าของเราให้สูงขนาดนี้"

show lilly basic_giggle_che_close
with charachange

# "She gives a small giggle."
"ลิลลี่หัวเราะคิกคัก"

show lilly basic_smileclosed_che_close
with charachange

# li "I'll be looking forward to it, Hisao."
li "จะตั้งตาคอยนะจ๊ะฮิซาโอะ"

# "The waiter reappears beside us, as if by magic, and hands Lilly's card back to her. Evidently picking up on her lack of sight, he places the card in her hand with an extra, perhaps unneeded, amount of firmness to make sure of her grip."
"บริกรคนนั้นโผล่มาที่โต๊ะเราอีกครั้งราวกับใช้เวทมนตร์แล้วยื่นบัตรคืนให้ลิลลี่ ซึ่งดูท่าจะรู้แล้วว่าลิลลี่นั้นมองไม่เห็น\nเพราะเขาวางบัตรให้แบบย้ำชัดจนออกจะเกินความจำเป็นไปสักหน่อยเพื่อที่จะได้แน่ใจว่าลิลลี่จับบัตรไว้แน่นแล้วจริง ๆ"

# "Leaving, he exercises a measure of diplomacy by keeping a neutral face despite my own expression."
"เขาแสดงความเป็นมืออาชีพด้วยการทำหน้าเรียบนิ่งขณะเดินออกไปโดยที่ไม่ได้สนใจสีหน้าของฉันเลย"

# "Clapping my hands together, I stand up from my seat in order to bring an end to our night out."
"ฉันตบมือแล้วลุกขึ้นยืนเป็นอันปิดการทานอาหารนอกโรงเรียนของพวกเรา"

# hi "Shall we be off then, m'lady?"
hi "งั้นไปกันเลยไหมครับคุณผู้หญิง"

stop music fadeout 2.0

scene black
with dissolve

#*************


label th_L25:

scene black
with Dissolve(2.0)

scene bg school_dormhisao_ni
with vpunch

# hi "Gyah!"
hi "เอื๊อก!"

# "I snap upwards out of my sheets and sit bolt upright in bed, as if an electric shock had just run through my entire body."
"ฉันทะลึ่งตัวขึ้นจากเตียงรู้สึกราวกับมีกระแสไฟฟ้าแล่นผ่านทั่วร่าง"

# "The night air feels cold against the sweat on my bare skin, my breathing short and rugged nearly to the point of hyperventilation."
"อากาศตอนกลางคืนทำให้เหงื่อที่ติดกับผิวนั้นรู้สึกเย็น ฉันหายใจหอบถี่จนคล้ายจะเป็นการหายใจเกิน"

# "Mind racing, I bring my hand to my head in an attempt to soothe my body's panicked state. It takes me a number of seconds to realize my hand is shaking violently, even as I press it against my face."
"ฉันยกมือขึ้นมาจับ ๆ หัวเพื่อให้ร่างกายที่กระสับกระส่ายอยู่นั้นสงบลงพลางคิดไปต่าง ๆ นานา ผ่านไปสักพักถึงรู้ตัวว่า\nมือฉันก็กำลังสั่นอย่างหนักหน่วง แม้จะกำลังจับหน้าตัวเองอยู่ก็ตาม"

# "More seconds pass in complete silence, my desperate attempts to subdue my body and mind slowly, thankfully, working."
"เวลาผ่านไปอีกครู่หนึ่งพร้อมความเงียบงัน โชคดีที่ความพยายามอย่างหนักของฉันที่จะค่อย ๆ สงบกายสงบใจตัวเองลง\nนั้นเป็นผล"

# "Gathering myself, I start taking measure of the state I'm in. It feels like I've run a marathon, every muscle feeling tensed and sweat practically pouring off me."
"ฉันตั้งสติแล้วเริ่มพิจารณาร่างกายตัวเอง รู้สึกเหมือนวิ่งมาราธอนมาเลย กล้ามเนื้อทุกมัดเกร็งไปหมด เหงื่อก็ไหล\nเป็นก๊อกน้ำ"

# "I carefully direct my attention to the beating in my chest, measuring out the rhythm in my head. Sure enough, my unreliable heart is functioning properly, for once."
"ฉันคอยฟังเสียงหัวใจที่เต้นอยู่ในอกอย่างตั้งใจแล้วจับจังหวะในหัว โอเค หัวใจที่พึ่งพาไม่ได้ของฉันยังทำงานปกติอยู่"

# "Just… what the hell was that?"
"เมืื่อกี้… มันอะไรกัน"

# "A heart attack? A bad nightmare? Medicine side-effects? I've heard about panic attacks, and this does seem to have the hallmarks of one…"
"หัวใจวาย? ฝันร้าย? ผลข้างเคียงจากยา? ฉันเคยได้ยินเรื่องอาการแพนิกกำเริบอยู่ ซึ่งเมื่อกี้ก็ดูคล้าย ๆ เหมือนกัน…"

# "I can't even be bothered thinking about it right now. I feel utterly exhausted yet completely awake, after this experience."
"ตอนนี้ฉันไม่มีอารมณ์จะมานั่งคิดแล้วด้วยซ้ำ เรื่องเมื่อกี้ทำฉันอ่อนเพลียเปลี้ยแรงแต่ก็ตื่นเต็มตาเลย"

# "I look over to the other side of my bed, the pale white of the silent figure's face almost glowing in the nighttime darkness of the room. Just the sight of her is enough to calm me down significantly."
"ฉันหันมองไปทางอีกฝั่งเตียง ใบหน้าขาวนวลของเธอซึ่งกำลังนอนอยู่อย่างเงียบ ๆ นั้นดูคล้ายจะเปล่งแสงได้ใน\nความมืดมิดยามราตรีที่อยู่ภายในห้องนี้ เพียงได้เห็นเธอใจฉันก็สงบลงไปได้มาก"

scene ev lilly_sleeping_smile:
    truecenter
    zoom 1.0 subpixel True
    acdc_warp 20.0 zoom 1.05
with locationchange

# "Her graceful demeanor persists even while she's asleep, her perfectly measured breathing and gentle face making it impossible to tell whether she's awake or truly sleeping."
"แม้ยามหลับเธอก็ยังคงรักษาท่าทีอันงดงาม เมื่อดูลมหายใจซึ่งสม่ำเสมอกับใบหน้าอันอ่อนโยนนั้นแล้วฉันก็ไม่แน่ใจ\nเลยว่าเธอหลับอยู่จริง ๆ หรือตื่นแล้ว"

# "Giving in to temptation, I delicately run my fingertips over her hand. Her skin is soft to the touch, as it always has been, yet warm even in the cold night."
"ฉันอดใจไม่ไหวจึงยื่นนิ้วเข้าไปไล้ตามมือของเธอเบา ๆ ผิวของเธอนั้นอ่อนนุ่มอย่างเคย ทั้งยังอุ่นแม้ค่ำคืนนี้จะเย็นเยือก"

# "It's at times like this, silently appreciating each other's presence, that I feel we're closest."
"ช่วงเวลาที่ได้รับรู้ถึงตัวตนของกันและกันอย่างนี้นี่แหละที่ฉันรู้สึกว่าเราได้อยู่ใกล้ชิดกันที่สุด"

# "My fingers stop at her wrist and I bring my hand back down to the bed beside me."
"พอเลื่อนนิ้วมาถึงตรงข้อมือฉันก็ถอนมือออกแล้วมาวางไว้ข้างตัว"

# "I'm not entirely sure why, but as we became ever closer to each other, it felt as if something grew between us. I'm not entirely sure what it is, nor whether it existed before we'd fallen in love."
"ยิ่งเราได้ใกล้ชิดกัน ฉันยิ่งรู้สึกราวกับว่ามีบางสิ่งที่ผุดขึ้นระหว่างเรา ฉันก็ไม่แน่ใจเหมือนกันว่าทำไม ไม่แน่ใจว่าสิ่งนั้น\nคืออะไร และไม่แน่ใจด้วยว่าสิ่งนั้นมีมาตั้งแต่ก่อนที่เราจะตกหลุมรักกันแล้วหรือเปล่า"

# "Everything is moving so fast. I don't mind it at all, but it feels unlike Lilly to be pushing things this much."
"ทุกอย่างเคลื่อนไปอย่างรวดเร็ว ซึ่งฉันก็ไม่ได้ถือหรอก เพียงแต่รู้สึกว่าคนอย่างลิลลี่คงไม่รีบเร่งอะไรอย่างนี้"

scene bg school_dormhallway
with shorttimeskip

play music music_dreamy fadein 2.0

# "Thankfully, there aren't any students milling around in the hallways at this hour of the morning, lest I be interrogated on why I'm carrying two plates of breakfast to my room while dressed in an obviously hastily-donned uniform."
"โชคดีที่เวลาเช้าตรู่อย่างนี้ยังไม่มีนักเรียนออกมาเดินเพ่นพ่านตามโถงทางเดิน ไม่อย่างนั้นฉันคงถูกถามว่าทำไมถึง\nถือมื้อเช้ามาสองจานกลับห้องตัวเองด้วยสภาพที่ใส่ชุดนักเรียนลวก ๆ แบบนี้"

# "That isn't to say things like this never happen, of course. A single security guard patrolling between two sets of bedrooms situated right next to each other is a very small force, compared to adolescent hormones."
"แต่ก็ใช่ว่าจะไม่มีคนถามเลยน่ะนะ ทว่าถ้าว่ากันเรื่องพลังแล้ว ยามหนึ่งคนที่อยู่โยงเฝ้าหอทั้งสองหลังที่อยู่ติดกันนั้น\nเทียบกับวัยรุ่นซึ่งฮอร์โมนพุ่งพล่านแทบไม่ติด"

# "Come to think of it, the fact that it's Monday morning probably helps. I'm not really sure why, but Mondays seem to bother me less than they do most others."
"จะว่าไปแล้ว ส่วนหนึ่งก็น่าจะเพราะวันนี้เป็นวันจันทร์ด้วย ฉันก็ไม่รู้เหมือนกันว่าทำไมวันจันทร์ถึงมีผลกับฉันน้อยกว่า\nคนอื่น ๆ ส่วนมาก"

# "It takes a little creative use of my hands and elbow, but eventually I manage to work the door to my dormitory room open."
"ฉันต้องพลิกแพลงหาวิธีในการใช้มือกับข้อศอกอยู่เล็กน้อยถึงเปิดประตูห้องตัวเองได้สำเร็จ"

scene bg school_dormhisao
show lilly basic_sleepy_paj at center
with locationchange

# "Stepping inside, I see Lilly just getting up from the bed and tiredly rubbing her eyes. She looks a mess, just like most other times I've seen her soon after she wakes. She really isn't a morning person."
"พอเดินเข้าห้องมาก็เห็นลิลลี่ที่เพิ่งตื่นแล้วขยี้ตาเพลีย ๆ สภาพเธอนั้นดูไม่ได้ไม่ต่างอะไรกับทุกครั้งที่ฉันเห็นเธอ\nตอนตื่นเลย ลิลลี่เป็นคนที่ไม่ชอบตื่นเช้าเลยจริง ๆ"

# hi "Sorry, I didn't mean to wake you."
hi "ขอโทษที ไม่ได้ตั้งใจจะปลุกเลยนะ"

show lilly basic_displeased_paj
with charachange

# "She groggily shakes her head. The morning light illuminating her makes for a very pleasant sight."
"ลิลลี่สั่นหัวด้วยความงัวเงีย เธอที่ถูกแดดยามเช้าส่องกระทบนั้นช่างเป็นภาพที่งามตาเหลือเกิน"

show lilly basic_weaksmile_paj
with charachange

# li "It's okay, I needed to get up anyway. What time is it?"
li "ไม่เป็นไรหรอก ยังไงก็ต้องตื่นเช้าอยู่แล้ว ตอนนี้กี่โมงแล้วเหรอ"

# "I put my plate down on my desk and turn the clock around to check the time."
"ฉันวางจานของตัวเองลงกับโต๊ะแล้วหันไปมองนาฬิกาเพื่อดูเวลา"

# hi "Still early. Don't worry, there's plenty of time left before school."
hi "ยังเช้าอยู่ ไม่ต้องห่วงหรอก ยังเหลือเวลาก่อนเข้าเรียนอีกเยอะ"

show lilly basic_smileclosed_paj:
    ypos 1.2
with dissolvecharamove

# "She sits on the side of the bed and begins to sniff the air. As she does so, I quickly move her plate away and put it on the desk beside mine."
"ลิลลี่ขยับมานั่งริมเตียงแล้วดมกลิ่นฟุดฟิด ระหว่างนั้นฉันก็รีบวางจานของลิลลี่ลงกับโต๊ะที่ข้าง ๆ จานของฉัน"

# hi "Yes, I got us some breakfast. Shower and clothes come first, though."
hi "อื้ม ฉันไปเอาข้าวเช้ามาให้แล้ว แต่ไปอาบน้ำกับเปลี่ยนเสื้อผ้าก่อนนะ"

scene ev lilly_kissing
with flash

# "She stands still for a moment with her chin pointed slightly out. I gladly acquiesce and press my lips to hers, savoring the soft feeling before breaking off."
"ลิลลี่ยืนนิ่งยื่นคางออกมาเล็กน้อยอยู่ครู่หนึ่ง ฉันยอมรับนำริมฝีปากเข้าไปแตะกับริมฝีปากเธออย่างเต็มใจดูดดื่มสัมผัส\nอ่อนนุ่มก่อนจะผละออกมา"

scene bg school_dormhisao
with locationchange

# "With a small, sweet smile, apparently quite satisfied, she slowly makes her way to the showers."
"ลิลลี่ยิ้มบาง ๆ อย่างอบอุ่นเป็นเชิงพอใจแล้วค่อย ๆ เดินไปอาบน้ำ"

# "I stretch to try and wake myself up a little more, briefly looking at the steaming dishes on the desk. Rice, fish, miso soup and some vegetables; a standard breakfast for a somewhat unusual day."
"ฉันยืดเส้นยืดสายให้หายงัวเงียอีกสักเล็กน้อยพลางเหลือบมองอาหารบนโต๊ะที่มีควันลอยฉุย มีข้าว ปลา ซุปมิโซะ แล้วก็\nผักอีกสองสามอย่าง เป็นอาหารเช้าสูตรมาตรฐานสำหรับเช้าที่ออกจะแปลกไปจากปกตินี้"

# "I grab the bottles from my desk and start taking my daily regimen of pills."
"ฉันหยิบขวดยาบนโต๊ะมากินตามปริมาณที่ต้องกินเป็นประจำทุกวัน"

show pills:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

# "Sometimes I wonder what these things are even good for, given all the troubles I've had since the initial accident. I can't even say that it doesn't hurt to take them, considering the side effects so far."
"ดูจากเรื่องทั้งหลายที่ต้องเจอมาหลังจากอุบัติเหตุครั้งนั้น บางทีฉันก็สงสัยว่ายาพวกนี้ช่วยอะไรได้จริง ๆ หรือเปล่า\nจะบอกว่ากิน ๆ ไปก็ไม่เสียหายก็ไม่ได้ เพราะผลข้างเคียงก็ทำให้รู้สึกว่ากินไปแล้วเหมือนจะเสียหายเหมือนกัน"

# "Well, whatever. Doctor's orders are that I have to take them, and rationality suggests that I'd be well served to trust his judgment over mine."
"แต่เอาเถอะ หมอสั่งให้กินก็ต้องกินละนะ แล้วความเป็นเหตุผลในตัวก็บอกฉันด้วยว่าเชื่อเขาจะดีกับตัวกว่าเชื่อตัวเอง"

show pills:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide pills
with None

# "It doesn't take long for the noise of the shower to cease, a quick one apparently being fine for Lilly given the circumstances."
"ไม่นานเสียงน้ำจากฝักบัวก็เงียบไป ดูจากสถานการณ์แล้ว ลิลลี่คงจะไม่ได้จะอยากอาบแบบพิถีพิถันขนาดนั้น"

show lilly basic_smile_paj:
    center
    xpos 0.55
    easein 0.5 xpos 0.5
with charaenter

# "Emerging from the bathroom, she looks significantly more awake, having had the chance to collect herself."
"ลิลลี่เดินออกมาจากห้องน้ำด้วยท่าทีที่หายง่วงไปหลายเท่าตัวด้วยมีเวลาให้ตั้งสติแล้ว"

show lilly basic_smile_paj_close at center
with characlose

show lilly basic_smileclosed_paj_close:
    ypos 1.1
with dissolvecharamove

# "Without a word, I gently take her hand in mine and guide her to my desk. Considering I don't have a table in my room as she does, it'll have to do."
"ฉันจับมือลิลลี่แล้วนำทางไปที่โต๊ะฉันโดยที่ไม่พูดอะไร ฉันไม่ได้มีโต๊ะเตี้ยโดยเฉพาะเหมือนอย่างที่ห้องลิลลี่ แต่เท่านี้\nก็น่าจะพอใช้ได้แล้ว"

# li "Thank you, Hisao. What did you prepare for breakfast?"
li "ขอบคุณจ้ะฮิซาโอะ เช้านี้มีอะไรเหรอ"

# hi "Just rice and some vegetables. Something fast."
hi "แค่ข้าวกับผักน่ะ ของง่าย ๆ"

show lilly basic_ara_paj_close
with charachange

# "Her face lights up at the revelation."
"พอลิลลี่ได้ฟังแล้วเธอก็ยิ้มออกมา"

show lilly basic_satisfied_paj_close
with charachange

# li "That's quite a breakfast. This is normal for you?"
li "เป็นมื้อเช้าที่ดีน่าดูเลยนะจ๊ะ กินแบบนี้ทุกวันเลยเหรอ"

# "Now she's just being nice. I have little doubt, considering her past, that this isn't exactly a high class meal by her standards."
"อันนี้ก็ชมเกินไปมั้ง ฉันแอบไม่เชื่อเพราะถ้าว่าตามชีวิตของลิลลี่แล้ว ของพวกนี้ไม่ใช่อาหารที่หรูหราอะไรสำหรับเธอเลย"

# hi "Breakfast is the most important meal of the day. Just because we're students, doesn't mean we can take it lightly."
hi "มื้อเช้าน่ะเป็นมื้อที่สำคัญที่สุดของวันนะ ใช่ว่าเป็นนักเรียนแล้วจะมองว่าเป็นสิ่งไม่สำคัญได้สักหน่อย"

# "That's my belief, anyway. From what others I've talked to have said, I might be in the minority."
"ซึ่งก็เป็นแค่ความเชื่อส่วนตัวอะนะ เพราะเท่าที่ได้คุยกับคนอื่นมา เหมือนว่าฉันจะเป็นฝั่งเสียงส่วนน้อย"

show lilly basic_smileclosed_paj_close
with charachange

# "I take a seat on the side of my bed and begin eating together with Lilly, her chopsticks lightly tapping out the outlines of the vegetables just as I'd noticed her do during our date."
"ฉันนั่งที่ริมเตียงแล้วกินข้าวไปพร้อม ๆ กับลิลลี่ เธอใช้ตะเกียบแตะตามส่วนนอกของผักเบา ๆ เหมือนอย่างที่ฉัน\nเห็นเธอทำตอนไปเดตด้วยกัน"

show lilly basic_smile_paj_close
with charachange

# li "This is quite nice, Hisao. I had no idea you could cook this well."
li "อร่อยเหมือนกันนะจ๊ะฮิซาโอะ ไม่ยักรู้ว่าเธอทำอาหารเก่งขนาดนี้"

# "This time she's much more genuine, I can tell that much. That said, cooking really isn't anything special at all; after a bit of practice it's pretty easy to make a simple dish."
"แต่คราวนี้ฉันรู้ว่าลิลลี่ชมจากใจจริง แต่ถึงอย่างนั้น การทำอาหารก็ไม่ใช่เรื่องที่พิเศษอะไรมากมาย ถ้าลองหัดทำ\nสักหน่อยแล้วก็จะพอทำอาหารอะไรง่าย ๆ ได้แน่นอน"

# hi "Most of the credit goes to modern technology; still, after years of cooking for myself, I should hope so."
hi "ก็ต้องขอบคุณเทคโนโลยีสมัยใหม่เลย แต่ก็นะ ทำมาตั้งหลายปีมันก็คงอร่อยแหละ"

# hi "I got bored of eating instant noodles and ordering pizza every time my parents were both working, so I taught myself how to make a few meals. I'm still trying to get the knack of it, though."
hi "ตอนเด็ก ๆ ฉันเบื่อการที่ต้องกินบะหมี่กึ่งฯ กับการสั่งพิซซ่ามากินตอนที่ทั้งพ่อทั้งแม่ไปทำงานก็เลยหัดทำอาหาร\nไว้บ้างน่ะ แต่ตอนนี้ก็ยังคอยฝึกฝีมือให้ใช้ได้อยู่อะนะ"

show lilly basic_cheerful_paj_close
with charachange

# li "You'll make a good wife someday, Hisao."
li "เธอต้องเป็นแม่ศรีเรือนที่ดีได้แน่ ๆ เลยจ้ะฮิซาโอะ"

# "I take a grain of rice and place it onto my thumb, before carefully taking aim and giving it a good flick."
"ฉันหยิบเมล็ดข้าวมาวางที่นิ้วโป้งก่อนจะเล็งให้แม่นแล้วดีดผึง"

show lilly basic_surprised_paj_close
with vpunch

# "Lilly jumps a little as it hits her cheek, right on target."
"ลิลลี่สะดุ้งเล็กน้อยเมื่อเมล็ดข้าวนั้นถูกเข้าเป้าที่แก้มเธอพอดิบพอดี"

show lilly basic_pout_paj_close
with charachange

# "I can't help chuckling a little at her expense as she lowers her brow and tries her best to assume a harsh and serious expression."
"ฉันอดไม่ได้ที่จะหัวเราะกับลิลลี่ที่หรี่ตาต่ำทำท่าให้ดูขึงขังจริงจังที่สุดเท่าที่จะทำได้"

show lilly basic_sleepy_paj_close
with charachange

# li "Oh, that's right…"
li "อ้อ จริงสิ…"

# hi "What is it?"
hi "อะไรเหรอ"

show lilly basic_concerned_paj_close
with charachange

$ renpy.music.set_volume(0.5, 1.0, channel="music")

# li "Did you have any problem sleeping last night? You seemed restless."
li "เมื่อคืนหลับสบายดีหรือเปล่า เหมือนเธอนอนไม่ค่อยหลับนะ"

# "So she was awake back then, or at least partly so. Whether it was my heart or a nightmare caused by the side effects of my medicine, the last thing I want is for her to be worrying about me even more."
"แสดงว่าตอนนั้นตื่นอยู่ หรืออาจจะพอรู้สึกตัวบ้าง ซึ่งไม่ว่าจะเป็นเพราะหัวใจของฉันหรือฝันร้ายที่มากับผลข้างเคียง\nของยา ฉันก็ไม่อยากให้ลิลลี่ต้องเป็นห่วงฉันไปมากกว่านี้อีกเลย"

# "Even before my relationship with Lilly, I'd felt my body was a drag on everything I did. My body is my burden alone, so as long as I'm with her, I'll continue to act as normally as possible."
"ฉันรู้สึกว่าร่างกายตัวเป็นเป็นตัวฉุดรั้งจากทุกอย่างในชีวิตมาตั้งแต่ก่อนที่จะได้คบกับลิลลี่แล้ว ร่างกายของฉันนั้น\nเป็นภาระของฉันเพียงผู้เดียว ตราบใดที่ฉันยังอยู่กับลิลลี่ ฉันจะต้องคอยทำตัวให้ปกติที่สุดเท่าที่จะทำได้"

# hi "No, not particularly."
hi "ก็พอจะหลับสบายอยู่"

show lilly basic_reminisce_paj_close
with charachange

# li "Is that so… that's good, then."
li "เหรอ… งั้นก็ดีแล้วละจ้ะ"

$ renpy.music.set_volume(1.0, 4.0, channel="music")

# "Luckily, she seems to take me at my word."
"โชคดีที่ลิลลี่เหมือนจะเชื่อ"

show lilly basic_weaksmile_paj_close
with charachange

# li "Come to think of it, there was something else I wanted to ask."
li "จะว่าไป ฉันมีอีกอย่างที่อยากถามด้วย"

# hi "Oh?"
hi "ว่า?"

show lilly basic_smileclosed_paj_close
with charachange

# li "How should I put it…"
li "จะว่ายังไงดี…"

show lilly basic_smile_paj_close
with charachange

# li "When you dream… do you see people and objects?"
li "ตอนเธอฝัน… เธอเห็นคนกับสิ่งของหรือเปล่า"

# hi "Yes, of course I… oh."
hi "ก็เห็นอยู่แล้… อ๊ะ"

# "I feel more than a little sheepish for that slip of the tongue, however earnest it may be. Lilly looks unperturbed, though."
"ฉันแอบอายเล็กน้อยที่หลุดปากไปอย่างนั้นถึงจะไม่ได้จงใจเลยก็ตาม แต่ลิลลี่ก็ดูจะไม่ถืออะไร"

show lilly basic_smileclosed_paj_close
with charachange

# li "But you don't taste, feel, nor smell things?"
li "แต่ไม่ได้รับรส กลิ่น หรือสัมผัสใช่มั้ย"

# "I move to answer, but find myself stuck before thinking about it. The more I mull it over, the more I realize that her hypothesis is correct."
"ฉันเตรียมจะตอบ ทว่าพอคิดดูก็ไม่มีคำตอบ ยิ่งคิดก็ยิ่งรู้สึกว่าที่เธอตั้งข้อสมมุติฐานนั้นถูกต้อง"

# hi "That's… true, I guess. I never looked at it that way. Are you saying that you do?"
hi "ก็… คงงั้นมั้ง ฉันไม่เคยคิดอย่างนั้นเลย เธอจะบอกว่าเธอรับสัมผัสพวกนั้นได้เหรอ"

show lilly basic_smile_paj_close
with charachange

# li "For the most part I only hear in dreams, but yes, sometimes I touch and smell things as well."
li "ส่วนใหญ่ฝันฉันจะเป็นเสียงน่ะจ้ะ แต่บางครั้งก็มีสัมผัสหรือกลิ่นด้วยเหมือนกัน"

show lilly basic_planned_paj_close
with charachange

# li "I'm just asking since Akira thought it very strange that I did when I brought it up with her. If you don't either, then maybe it's due to my blindness."
li "ที่ถามเพราะพี่บอกว่าแปลกมากตอนที่ฉันเอาเรื่องนี้ไปคุยกับพี่ ถ้าเธอไม่ได้รับสัมผัสพวกนั้นเหมือนกันก็แปลว่า\nที่ฉันฝันอย่างนี้ก็อาจเป็นเพราะฉันตาบอด"

# hi "That would make sense. You rely on your other senses more than me, so maybe that affects your dreams as well."
hi "ก็น่าจะเป็นอย่างนั้นนะ เพราะเธอต้องพึ่งประสาทสัมผัสอื่นเยอะกว่าฉัน เลยอาจจะมีผลกับฝันด้วย"

# "The wonders of the human body, I guess."
"นี่ละมั้งความมหัศจรรย์ของร่างกายมนุษย์"

# "For the rest of the time before school, we quietly eat the hearty breakfast in front of us, exchanging a few small pieces of smalltalk as we do."
"จากนั้นพวกเราก็กินมื้อเช้าแสนอิ่มอร่อยกันไปเงียบ ๆ พลางคุยเรื่อยเปื่อยบ้างไปจนกระทั่งถึงเวลาเข้าเรียน"

stop music fadeout 2.0

scene bg school_dormext_full
with shorttimeskip

# "A quick peek out of the door assures nobody's looking directly at the entrance for the boys' dormitories, so we walk out with the path clear."
"พอกวาดตามองดูให้แน่ใจแล้วว่าไม่มีใครมองที่ทางเข้าหอชายอยู่พวกเราก็เดินออกมา"

play music music_soothing fadein 4.0

# hi "Ah, the weather's good today."
hi "เฮ้อ วันนี้อากาศดีจังเลยนะ"

# "I stretch as Lilly and I make our way outside, the bright morning's sun beaming down on us."
"ฉันยืดเส้นยืดสายพลางเดินออกมาพร้อมลิลลี่ แดดยามเช้าอันเจิดจ้าส่องกระทบเรา"

# "By now a few students can be seen doing the same, making their way to the main school building either from the dorms or through the main gate."
"เวลานี้ก็เริ่มมีนักเรียนที่เดินมาที่อาคารหลักกันแล้ว โดยมีทั้งคนที่เดินมาจากหอและคนที่เดินผ่านประตูหลักเข้ามา"

show lilly cane_smile_close at center
with charaenter

# li "It does feel nice and warm."
li "รู้สึกอบอุ่นสบายดีจริงจ้ะ"

# "Our hands linked and her cane tapping the ground, we begin in earnest our trip to the school building and join the chatting throngs of students around us."
"พวกเราเดินจับมือกัน—มืออีกข้างของลิลลี่ก็ถือไม้เท้าเคาะไปตามทาง—โดยที่มุ่งหน้าไปยังอาคารหลักกลืนไปกับ\nกลุ่มนักเรียนรอบ ๆ ซึ่งคุยกันจ้อกแจ้ก"

show lilly cane_smileclosed_close
with charachange

# li "This would be the last day of exams, no?"
li "วันนี้สอบวันสุดท้ายแล้วใช่มั้ยจ๊ะ"

# hi "Yeah. How're you going in them?"
hi "อื้ม แล้ววิชาที่ผ่าน ๆ มาเป็นยังไงบ้าง"

show lilly cane_concerned_close
with charachange

# li "Fairly well, all things considered. You seem a bit stressed by them, though."
li "เท่าที่รู้สึกก็ค่อนข้างดีจ้ะ แต่เธอดูเครียดหน่อย ๆ นะ"

# hi "It's that obvious, huh?"
hi "ชัดขนาดนั้นเลยเหรอ"

# hi "I don't think it's just the exams, though. A lot of stuff's been happening in a short amount of time, and I'm not doing that well on the humanities subjects."
hi "แต่น่าจะไม่ใช่แค่เครียดเรื่องสอบหรอก ช่วงนี้อะไร ๆ มันปุบปับหลายอย่างไปหมด แล้ววิชาจำพวกสายมนุษยศาสตร์\nฉันก็ทำไม่ค่อยได้ด้วย"

show lilly cane_smileclosed_close
with charachange

# li "You're doing well in science though, aren't you?"
li "แต่เธอก็ทำวิชาวิทยาศาสตร์ได้นี่"

# hi "Well, it would be hard not to do well in science for me. Come to think of it, didn't you say before that you weren't very good at science and maths?"
hi "ก็นะ ถ้าฉันทำวิชานั้นไม่ได้ก็คงลำบากหน่อย จะว่าไป ก่อนหน้านี้เธอบอกใช่มั้ยว่าไม่ค่อยเก่งวิชาวิทยาศาสตร์กับ\nคณิตศาสตร์น่ะ"

show lilly cane_oops_close
with charachange

# "She suddenly looks very sheepish, my remark no doubt hitting home. Lilly's sense of pride really can be a double-edged sword."
"อยู่ ๆ ลิลลี่ก็ทำท่าอาย ๆ ดูท่าว่าที่พูดไปจะจี้ใจดำทีเดียว ศักดิ์ศรีของลิลลี่นี่นับว่าเป็นดาบสองคมได้เลยนะเนี่ย"

show lilly cane_smile_close
with charachange

# li "Well, aside from that… have you ever given thought to what you might do with that ability? It seems a pity to waste it."
li "เอาเถอะจ้ะ ว่าแต่ว่า… เธอเคยคิดมั้ยว่าจะเอาความถนัดตรงนั้นไปทำอะไรต่อ ปล่อยไว้เฉย ๆ คงน่าเสียดายแย่"

# hi "A bit, mostly at Mutou's prompting."
hi "ก็นิดหน่อย หลัก ๆ ก็ได้ครูนี่แหละคอยบอก"

# hi "In any case, I'll probably end up doing science as a career in some form."
hi "แต่นั่นแหละ อาจจะไปทำงานที่เกี่ยวกับวิทยาศาสตร์สักอย่างละมั้ง"

show lilly cane_smileclosed_close
with charachange

# li "That's good to hear, Hisao."
li "งั้นก็ดีแล้วจ้ะฮิซาโอะ"

scene bg school_gardens at bgleft
with locationchange

stop music fadeout 0.3
with vpunch

# "As we enter the gardens, I suddenly receive an unsolicited pat on the back."
"พอเดินมาถึงสวนก็มีแขกที่ไม่ได้รับเชิญมาตบหลัง"

# "The green-dressed culprit dances around to meet me, evidently not paying any heed to Lilly at my side."
"ผู้ร้ายที่ใส่ชุดสีเขียวเดินอ้อมมาหน้าฉันโดยที่ไม่ได้สนใจลิลลี่ซึ่งอยู่ข้าง ๆ"

play music music_kenji fadein 0.5

show kenji neutral:
    center
    xpos 0.55
    easein 0.5 center
with charaenter

# ke "Hey man, what's up? Haven't seen you in a while."
ke "ไงพวก สบายดีเปล่า ไม่เห็นหน้าได้สักพักเลย"

# hi "Hey. Just been busy lately with the exams and stuff."
hi "ไง พอดีช่วงนี้ยุ่ง ๆ กับสอบกับอะไรอยู่น่ะ"

show kenji tsun at center
with charachange

# ke "Exams, ekshmams. A true Renaissance man needs no study to excel in such things."
ke "สอบ ศ๊อบ ชายยุคเรอแนซ็องส์ตัวจริงเขาไม่ต้องอ่านหนังสือสอบอย่างนั้นกันหรอกเว้ย"

# "Kenji does strike me as the kind of person that does well in school, even if he has a horrid attendance record and poor work ethic, so I've little reason to doubt his ability."
"เคนจิก็ดูจะเป็นคนที่เรียนเก่งอยู่เหมือนกัน ถึงสถิติการเข้าเรียนกับจริยธรรมในการทำงานจะต่ำเตี้ยก็เถอะ ฉันเลย\nไม่ได้นึกเคลือบแคลงอะไรกับความเก่งของเขา"

# "To be honest, I'm a little envious of him; between studying for exams and my time with Lilly, I've had practically no time to myself. Maybe this is a bit like how Yuuko feels."
"ว่าตามตรงก็แอบอิจฉาเคนจิอยู่หน่อย ๆ เวลาของฉันหมดไปกับการอ่านหนังสือสอบกับการอยู่กับลิลลี่จนแทบไม่ได้\nมีเวลาให้ตัวเองเลย ความรู้สึกยูโกะก็คงประมาณนี้ละมั้ง"

show kenji tsun at tworight
show bg school_gardens at center
with charamove

show lilly cane_smile_close at twoleft
with charaenter

# li "Good morning, Setou. It's good to hear you're doing well."
li "อรุณสวัสดิ์จ้ะเซโต้ เรื่องสอบของเธอเหมือนจะราบรื่นดีนะ"

# "It feels slightly odd to see Lilly speaking so formally. She's come to address me more casually over the months, though I have seen her speak more formally to classmates from time to time as well."
"ฉันรู้สึกแปลก ๆ เล็กน้อยที่เห็นลิลลี่พูดแบบทางการอย่างนี้เพราะช่วงเดือนสองเดือนที่ผ่านมาลิลลี่ก็คุยกับฉันแบบ\nสบาย ๆ ถึงบางทีจะเคยเห็นเธอพูดแบบทางการกับเพื่อนร่วมชั้นเรียนของเธอมาแล้วก็เถอะ"

# "Some people never change, I guess. Not that I'd say her calm and polite manner is a bad thing; it was one of the reasons I liked being around her to begin with, after all."
"นิสัยบางคนคงเปลี่ยนกันยากละมั้ง ซึ่งฉันก็ไม่ได้มองว่ากิริยามารยาทเรียบร้อยเยือกเย็นของลิลลี่เป็นสิ่งที่ไม่ดีหรอก\nเป็นหนึ่งในเหตุผลที่ฉันชอบอยู่กับเธอด้วยซ้ำ"

# "Kenji seems to take a moment to work out who it is beside me, and probably hasn't noticed us holding hands either. I wonder if those glasses of his actually do anything."
"เคนจิเพ่งอยู่สักพักว่าฉันมากับใคร แล้วคงไม่เห็นด้วยว่าพวกเราจับมือกันอยู่ แว่นที่ใส่อยู่นั่นได้ช่วยให้มองเห็นจริง ๆ\nหรือเปล่าเนี่ย"

show kenji neutral at tworight
with charachange

# ke "Oh, hey Lilly. Good luck on your exams, too."
ke "อ้าว ไง ลิลลี่ ขอให้โชคดีกับการสอบเช่นกันนะ"

show kenji tsun at tworight
with charachange

# ke "I'll see you after school then, man."
ke "งั้นเดี๋ยวเลิกเรียนเจอกัน"

# "The slight edge to his voice makes me think those words are meant to be an imperative rather than a casual farewell. I guess I'll have to smooth things over later."
"ความขุ่นเล็กน้อยในน้ำเสียงเคนจิทำให้ฉันรู้สึกว่าที่พูดนั้นคือคำสั่งมากกว่า ไม่ใช่การบอกลาแบบเปล่า ๆ เดี๋ยวไว้คงต้อง\nไปจัดการคุยอะไร ๆ ให้มันเรียบร้อย"

# hi "Sure. Seeya."
hi "ได้ เจอกัน"

#changestart

show kenji invis:
   xpos 0.6
with dissolvecharamove

hide kenji
with None

# "Kenji nods curtly. He moves to pass by us, but he's too busy glaring in Lilly's general direction to take notice of her cane."
"เคนจิพยักหน้าหงึกแล้วเดินผ่านเราไป แต่ด้วยความที่มัวแต่มองลิลลี่จึงไม่ทันได้สังเกตเห็นไม้เท้าของเธอ"

show lilly cane_surprised_close at twoleft
with charachange

# "Before I can try to react and save the situation, Kenji trips and reflexively reaches out for a handhold. Unfortunately, said handhold turns out to be Lilly's arm."
"ฉันยังไม่ทันได้เข้าไปทำอะไรเคนจิก็สะดุดล้มแล้วพยายามหาอะไรมาคว้าเอาไว้ ซึ่งโชคไม่ดีที่สิ่งนั้นคือแขนของลิลลี่"

show lilly cane_surprised_close:
   easeout 0.3 ypos 1.2 alpha 0.0
with Pause(0.5)

play sound sfx_pillow
hide lilly
with vpunch

# $doublespeak(ke,li,"Whoa!", "Ah!")
$doublespeak(ke,li,"โอ๊ะ!", "อ๊ะ!")

# "Both fall to the ground in a sprawling heap, with me left feeling rather helpless."
"ทั้งคู่ล้มทับกันแขนขาไปคนละทิศละทาง ฉันได้แต่ยืนมองด้วยความรู้สึกแย่ที่ทำอะไรไม่ได้"

# hi "Ah, damn. Are you two okay?"
hi "โอย แม่ง เธอสองคนเป็นอะไรมั้ย"

show kenji invis:
    center
    ypos 1.2
with None

show kenji neutral:
    ypos 1.0
with dissolvecharamove

# "Kenji quickly rises back up, seemingly unfazed by the accident."
"เคนจิลุกขึ้นมาด้วยความรวดเร็วราวกับไม่มีอะไรเกิดขึ้น"

# ke "No problem, man, no problem. This is nothing, my body can take much worse abuse."
ke "ไม่เป็นไรพวก ไม่เป็นไร แค่นี้เอง ร่างกายฉันยังรับอะไรได้มากกว่านี้เยอะ"

# "Lilly lies facedown on the grass. She doesn't look hurt by the incident; more startled than anything. I move closer to offer her my help."
"ลิลลี่ล้มหน้าคว่ำกับพื้นหญ้า ดูจะไม่ได้บาดเจ็บอะไร เหมือนจะตกใจมากกว่า ฉันเดินเข้าไปช่วยเธอ"

# hi "Are you all right, Lilly?"
hi "เป็นอะไรหรือเปล่าลิลลี่"

show kenji happy
with charachange

# ke "Hey, Satou?"
ke "นี่ ซาโต้"

# "Kenji offers her a hand, tentatively touching hers to let her know what he's doing."
"เคนจิยื่นมือพลางแตะลิลลี่แบบกล้า ๆ กลัว ๆ เพื่อให้รู้ตัวว่าจะช่วย"

# "He says some odious things sometimes, but I do think he may be a genuinely good person at heart. I imagine he feels pretty bad about this."
"ถึงบางครั้งจะปากไม่ดี แต่ลึก ๆ แล้วเคนจิก็คงเป็นคนดีอยู่เหมือนกัน คงรู้สึกแย่ทีเดียวที่ตัวเองก่อเรื่องแบบนี้"

stop music fadeout 2.0

# "To his surprise and mine, though, Lilly pounds on the ground with her fist without warning."
"แต่ทั้งฉันกับเคนจิเป็นต้องตกใจเมื่อลิลลี่กำหมัดแล้วทุบลงกับพื้น"

play sound sfx_impact
with vpunch

# li "Dammit!"
li "โธ่เอ๊ย!"

show kenji tsun
with charachange

# "Kenji freezes, entirely caught by surprise at her outburst. I'm just as shocked; she never acted like this before, not even around Shizune."
"เคนจิผงะไปที่อยู่ ๆ ลิลลี่ก็โมโหขึ้นมา ฉันเองก็ตกใจไม่ต่างกัน ลิลลี่ไม่เคยเป็นอย่างนี้เลย แม้แต่กับชิซูเนะก็ตาม"

# ke "Uh…"
ke "เอ่อ…"

show lilly invis_close:
    twoleft
    ypos 1.2
with None
show lilly cane_mad_close at twoleft
#replace this with angry expression
with dissolvecharamove

# "Seemingly only now remembering that there are people around her, Lilly slowly climbs to her feet. Her face as she does so makes me retreat a little."
"เหมือนลิลลี่จะเพิ่งรู้ตัวว่ามีคนอยู่ด้วยจึงค่อย ๆ หยัดตัวลุกขึ้นยืน พอได้เห็นสีหน้าของเธอแล้วฉันก็ค่อย ๆ ถอยออกมา"

show lilly back_listen_close
show lillyprop back_cane_close at twoleft
with charachange

# "I only catch a glimpse of her expression before she turns away, but it's not something I'll forget soon."
"เป็นเพียงชั่วขณะเท่านั้นที่ฉันได้เห็นสีหน้าของลิลลี่ก่อนที่เธอจะเบือนหน้าหนีไป แต่สีหน้านั้นคงฝังใจฉันไปอีกนาน\nพอดู"

# "She showed plenty of annoyance during her clashes with Shizune, but this flash of anger was something else. There's no way that this is just about this petty incident."
"ตอนที่ลิลลี่ตีกับชิซูเนะนั้นเธอแสดงความหงุดหงิดอยู่มากก็จริง แต่ความโกรธครั้งนี้เป็นอะไรที่ไม่เหมือนกับความรู้สึก\nเหล่านั้นเลย ที่โกรธคงไม่ใช่แค่เพราะเรื่องอุบัติเหตุเล็ก ๆ น้อย ๆ นี้แน่"

hide lilly
hide lillyprop
with charaexit

# "She pauses for a moment before sighing and walking on ahead. I really don't know what to make of this."
"ลิลลี่เงียบไปครู่หนึ่งก่อนจะถอนหายใจแล้วออกเดินต่อ ฉันไม่รู้จริง ๆ ว่าสิ่งนี้หมายความว่าอะไร"

# hi "I'll, uh… talk to you later, dude. See you."
hi "ไว้ฉัน เอ่อ… คุยกับนายอีกทีนะพวก เจอกัน"

# ke "Yeah, seeya."
ke "เออ เจอกัน"

hide kenji
with charaexit

# "Kenji scratches the back of his head trying to find something to say, then shrugs and walks away, giving us a wide berth."
"เคนจิเกาท้ายทอยเหมือนอยากจะพูดอะไรอีก แต่สุดท้ายก็เพียงยักไหล่แล้วเดินทิ้งห่างออกไป"

show bg school_gardens at right
with charamove

show lilly back_listen at center
show lillyprop back_cane at center
with charaenter

# "I quickly catch up to Lilly. She turns her head a little to acknowledge my presence, but nothing else."
"ฉันรีบตามลิลลี่ไป เธอหันหน้ามาเล็กน้อยเป็นการรับรู้ว่าฉันอยู่ด้วย แต่ก็ไม่ทำอะไรอีก"

# "I should probably scold her for lashing out like that, but I also don't want to get into a shouting match with her. She's still very obviously annoyed."
"ฉันอาจต้องต่อว่าที่เธอโมโหเดือดไปอย่างนั้น แต่ฉันก็ไม่อยากต้องมาแหกปากเถียงกับลิลลี่ เพราะชัดว่าเธอยัง\nหงุดหงิดอยู่"

# "In the end, I keep my mouth shut and wait for her to cool off."
"สุดท้ายฉันก็ได้แต่เงียบปากรอให้ลิลลี่ใจเย็นลง"

scene bg school_hallway3
with shorttimeskip

# "After a quiet walk in, we eventually reach the top of the third floor stairs and the junction where we part every day."
"พอเดินมาเงียบ ๆ สักพักแล้วเราก็มาถึงบันไดขั้นสุดท้ายที่อยู่ติดชั้นสามซึ่งเป็นจุดที่เราแยกกันทุกวัน"

show lilly cane_listen_close at center
with charaenter

# "I turn to Lilly before she leaves. While I do like the comfortable and warm silences we usually share, this was anything but. I don't want to leave things like this."
"ฉันหันไปมองลิลลี่ที่กำลังจะเดินแยกไป ฉันชอบความเงียบที่ชวนให้อุ่นใจเวลาอยู่ด้วยกันก็จริง แต่ความเงียบคราวนี้\nไม่ใช่แบบนั้นเลย ฉันไม่อยากให้เรื่องมันค้างคาอยู่อย่างนี้"

# hi "You seem… quieter than usual recently. Is anything wrong?"
hi "ช่วงนี้เธอดู… เงียบกว่าปกตินะ มีอะไรหรือเปล่า"

show lilly cane_displeased_close
with charachange

# "She shakes her head almost automatically, as if to dispel any notion that I need to worry about her."
"ลิลลี่สั่นหัวแทบจะในทันทีราวกับจะบอกว่าไม่ต้องเป็นห่วงเธอเลย"

# li "It's just the exams taking their toll. I'll be fine."
li "แค่เครียดเรื่องสอบแหละ ไม่เป็นไรหรอก"

# "I don't think that's the reason. I very nearly say so, but decide against it. There's no point trying to draw it out of her if she doesn't want to tell me, especially when she's in a foul mood like this."
"ฉันว่าไม่น่าใช่เรื่องนั้นนะ ฉันเกือบจะบอกอย่างนั้นแล้ว แต่ก็ตัดใจไม่พูดออกไป ถ้าลิลลี่ไม่อยากบอกฉัน จะเค้นความไป\nก็คงไม่ได้อะไรขึ้นมา แล้วยิ่งเธออารมณ์ไม่ดีอย่างนี้ด้วย"

# hi "If you're sure. I'll see you later, then."
hi "ไม่เป็นไรก็ไม่เป็นไร งั้นไว้เจอกันนะ"

hide lilly
with charaexit

# "As I turn down the hall to go to my classroom, Lilly's soft voice rings out from behind me."
"จังหวะที่กำลังจะเลี้ยวเดินไปที่ห้องเรียนฉัน ลิลลี่ก็เรียกไล่หลังฉันมาด้วยเสียงอันอ่อนโยน"

show lilly cane_concerned
with charaenter

# li "Hisao, um…"
li "ฮิซาโอะ เอ่อ…"

# hi "Yeah?"
hi "หืม"

li "…"

# li "I'm sorry."
li "ขอโทษนะ"

hide lilly
with charaexit

#changeend

# "With that, Lilly makes off down the hallway to her own classroom, her hand skating along the metal railings."
"แล้วเธอก็เดินจับราวเหล็กตามผนังไปที่ห้องเรียนของตัวเอง"

# "I stand still and watch her until she turns into her classroom and out of sight, before going to my own class with a fair measure of reluctance."
"ฉันยืนมองจนลิลลี่เดินหายเข้าไปในห้องเรียนเธอก่อนจะกลับไปที่ห้องเรียนของฉันด้วยความละล้าละลัง"

scene bg school_scienceroom at left
with locationchange

play music music_normal fadein 4.0

# "As usual, I'm early. Mutou is fiddling with folders and papers on his desk as he prepares for the day while a handful of students mill about, chatting away."
"ฉันมาเช้าเช่นเคย ครูกำลังจัดการแฟ้มกับเอกสารที่กองอยู่บนโต๊ะเตรียมการสอนอยู่ ในห้องมีนักเรียนบางส่วน\nเดินไปมาพูดคุยกัน"

# "While my feelings about Lilly haven't dissipated, far from it, her mention of my exam performance did remind me that I have my own life's journey to attend to."
"ความรู้สึกของฉันที่มีกับลิลลี่เมื่อครู่ยังไม่จางหาย—ไม่เลย—แต่การที่เธอพูดถึงเรื่องสอบของฉันก็ทำให้นึกขึ้นได้\nว่าฉันเองก็มีเส้นทางชีวิตของฉันที่ต้องเดินต่อ"

# "After thinking about it, I have realized that I do genuinely want to pursue science in some form as a career, rather than it simply being the path of least resistance."
"พอมาลองคิด ๆ ดูแล้วก็ถึงได้รู้ว่าที่เลือกวิทยาศาสตร์เป็นเส้นทางอาชีพนั้นเป็นเพราะฉันมีใจรักจริง ๆ ไม่ใช่เลือกเพียง\nเพราะเป็นสิ่งที่ถนัดที่สุด"

# "Until now though, I didn't have much of an idea of where in the field I wanted to go. Just “science” is a pretty broad category of jobs."
"แต่จนตอนนี้ฉันก็ยังไม่รู้แน่ชัดเหมือนกันว่าฉันอยากไปทางไหนกันแน่ เพราะคำว่า “วิทยาศาสตร์” นั้นสามารถแตกไป\nได้หลายกลุ่มอาชีพ"

# "Something Lilly mentioned earlier focused my thoughts. Something I'd only idly pondered about before, I'd not seriously considered following this specific path."
"พอลิลลี่พูดแล้วฉันก็รู้สึกสนใจขึ้นมา ก่อนหน้านี้ฉันแค่คิดเล่น ๆ ไว้เท่านั้น แต่ยังไม่ได้คิดจริงจังว่าจะมาตามเส้นทางนี้"

show bg school_scienceroom at right
with charamove

# "I walk up to Mutou's desk, his attention too focused on preparing for the day's lessons to notice my approach. It's the same every day."
"ฉันเดินไปที่โต๊ะครู ครูซึ่งง่วนอยู่กับการเตรียมการสอนไม่ทันได้สังเกตว่าฉันมาหา เห็นเป็นอย่างนี้ทุกวันเลยแฮะ"

# hi "Good morning."
hi "อรุณสวัสดิ์ครับ"

show muto normal at center
with charaenter

# "He looks up with an expression of mild surprise that's quickly replaced by his typical awkward smile."
"ครูเงยหน้ามองฉันด้วยสีหน้าแปลกใจเล็กน้อยก่อนจะยิ้มแห้ง ๆ แบบที่ทำประจำ"

show muto smile
with charachange

# mu "Good morning, Nakai. Can I help you?"
mu "อรุณสวัสดิ์นากาอิ มีอะไรหรือเปล่า"

# hi "Do you mind if I ask you something?"
hi "ขอถามอะไรหน่อยได้ไหมครับ"

# "He looks down at his messy pile of books on the desk, before putting down the papers in his hand and standing up with some difficulty to properly address me."
"ครูก้มมองหนังสือที่กองเกะกะอยู่บนโต๊ะก่อนจะวางกระดาษที่ถืออยู่แล้วขยับตัวลุกขึ้นยืนมาคุยกับฉันให้เป็นเรื่องเป็นราว"

# mu "That's what I'm here for, after all. Ask away."
mu "ก็นั่นมันหน้าที่ครูเลยนี่ ถามมาสิ"

# hi "I was just wondering… what would you say is the motivation behind teaching?"
hi "พอดีผมสงสัยว่า… แรงบันดาลใจในการสอนของครูคืออะไรเหรอครับ"

# "He thinks on this question for a few moments before responding, evidently far from having a prepared answer."
"ครูครุ่นคิดกับคำถามนั้นอยู่ครู่หนึ่งก่อนจะตอบคล้ายไม่ได้เตรียมคำตอบสำหรับคำถามนั้นมาเลย"

show muto normal
with charachange

# mu "If you talk to ten different teachers, I think you'll get ten different answers to that question."
mu "ถ้าเธอไปถามครูอีกสิบคน เธอก็จะได้คำตอบมาอีกสิบแบบ"

# mu "While I can only speak for myself, I'd say that I teach because… hmm…"
mu "อันนี้ก็เป็นความเห็นส่วนตัวของครูนะ แต่ที่ครูมาเป็นครูก็เพราะ… อืม…"

# "He sinks into thought again, carefully assessing the way he wishes to present his idea."
"ครูจมอยู่กับความคิดตัวเองอีกครั้งคอยเรียบเรียงคำพูดให้แทนความคิดออกมาได้ดีที่สุด"

show muto smile
with charachange

# mu "Think of it this way; when you were a child, you probably played with sticks and pebbles in moving water such as the gutter or puddles, right?"
mu "ลองมองอย่างนี้ ตอนเด็กเธอคงจะเคยเอากิ่งไม้หรือไม่ก็เศษหินไปเขี่ยในน้ำไหลอย่างรางน้ำทิ้งหรือแอ่งน้ำเล่นใช่มั้ย"

# hi "Yeah. I think a lot of people do that when they're young."
hi "ครับ หลายคนตอนเด็กก็คงเคยเล่นอย่างนั้น"

show muto normal
with charachange

# mu "Well, it's not just when they're young for some, though it does take on another form. My point is, though, that when one is doing that, they're curious about how the water will flow or be changed."
mu "นั่นแหละ บางคนก็ไม่ใช่แค่ตอนเด็กหรอก เพียงแต่ว่าพอโตแล้วก็เปลี่ยนเป็นการเล่นหรืออะไรอย่างอื่น แต่สิ่งที่ครู\nจะบอกคือ ที่เด็กไปเล่นอย่างนั้นก็เพราะเขาอยากรู้ว่ากระแสน้ำมันจะเปลี่ยนไปยังไงบ้าง"

# mu "Everyone, even at that young age, possesses an intense wonderment about how the world around them works, even in its smallest forms."
mu "คนเราต่างมีความอยากรู้อยากเห็นกับระบบของโลกรอบตัวมาตั้งแต่ยังเล็กแล้ว ต่อให้ระบบที่ว่านั้นจะเป็นระบบที่เล็ก\nแค่ไหนก็ตาม"

# mu "I still feel that sense of wonderment about the universe. Even just reading about new discoveries or classic experiments gives me a renewed sense of awe at how marvelous everything is, from the farthest stars to the smallest puddle."
mu "ครูยังมีความรู้สึกอยากรู้อยากเห็นนั้นกับจักรวาลนี้อยู่ แค่ได้อ่านการค้นพบใหม่ ๆ หรือการทดลองดั้งเดิมก็ทำให้\nครูรู้สึกทึ่งกับความมหัศจรรย์ของสิ่งรอบตัวได้แล้ว ตั้งแต่ดาวที่อยู่สุดขอบจักรวาลยันแอ่งน้ำกระจิ๋วหลิวเลย"

show muto smile
with charachange

# mu "I just hope that I can give others even a small piece of that wonderment I feel. If I can do that, even if it's just for one person, I think that I can be happy as a teacher."
mu "ครูก็แค่หวังใจว่าครูจะถ่ายทอดความรู้สึกอยากรู้อยากเห็นนั้นให้คนอื่นได้บ้าง สักเสี้ยวหนึ่งก็ยังดี ถ้าครูทำให้\nใครสักคนรู้สึกอย่างนั้นได้ ครูก็มีความสุขในฐานะคนเป็นครูแล้วละ"

# "He scratches his head as he mentally reviews what he's said."
"ครูเกาหัวพลางคิดทบทวนสิ่งที่ตัวเองพูดออกไป"

# "I feel like I understand him better now. Even if he's awkward around others, he does have a genuine want to be around them and offer them a piece of his self that he values."
"เริ่มเข้าใจครูขึ้นมาแล้วละ ถึงครูจะทำตัวไม่ค่อยถูกเวลาอยู่กับคนอื่น แต่ครูก็อยากอยู่แบ่งปันตัวตนส่วนหนึ่งที่ตัวเอง\nให้ค่ากับพวกเขาจริง ๆ"

# "What Lilly told me yesterday rings in my ears. “I think you get on well with others,” huh. She always did say I was unusually curious…"
"แล้วสิ่งที่ลิลลี่พูดเมื่อวานก็ดังก้องอยู่ในหู “ฉันว่าเธอเข้ากับคนอื่นได้ดีเลยละ” เหรอ แถมพูดบ่อย ๆ ด้วยว่าฉันเป็นคน\nขี้สงสัยเป็นพิเศษ…"

show muto normal
with charachange

# mu "Sorry if that was a little meandering. Does it answer your question?"
mu "ถ้ามันวกวนไปหน่อยครูก็ขอโทษด้วยนะ เธอได้คำตอบแล้วใช่ไหม"

# hi "It does, thank you."
hi "ครับ ขอบคุณครับ"

# hi "I also had another question, actually."
hi "จริง ๆ ผมมีเรื่องจะถามอีกอย่างด้วย"

# mu "Oh? What might that be?"
mu "อ้อ ถามเรื่องอะไรล่ะ"

# hi "Um… do you have any college brochures or guides? It's about time I started getting some applications in."
hi "เอ่อ… ครูพอจะมีใบแนะแนวหรือใบปลิวของมหาวิทยาลัยหรือเปล่าครับ ช่วงนี้ผมคงต้องเริ่มไปสมัครแล้ว"

# "He nods and bends down to look inside his desk. As he does so, I notice that he is wearing a remarkably genuine smile. I don't think I've ever really seen him act this natural around others."
"ครูพยักหน้าแล้วก้มมองใต้โต๊ะ ฉันสังเกตเห็นว่าเขายิ้มจริงใจโดดเด่นด้วย ครั้งแรกเลยมั้งที่เห็นครูทำตัวเป็นธรรมชาติ\nเวลาอยู่กับคนอื่นอย่างนี้"

# "Perhaps this isn't Mutou, the teacher, but rather Mutou, the person."
"หรือคนตรงหน้านี้อาจจะไม่ใช่ครู หากแต่เป็นคนที่ชื่อมุโต้"

show muto smile
with charachange

# mu "Here. If you need any more, feel free to ask."
mu "เอ้านี่ ถ้าจะเอาอีกก็มาขอครูได้นะ"

# "He hands me about half a dozen brochures and booklets of various colors and sizes, which I take eagerly."
"ครูยื่นปึกใบปลิวกับหนังสือเล่มเล็กหลากสีหลากขนาดมาให้ ซึ่งฉันรับไว้ด้วยความยินดี"

# "Yes, it will be this information which I'll use to forge my own future. I think now, after all this time and all these trials, I can finally start to see the big picture of my life ahead of me."
"นี่แหละ นี่จะเป็นข้อมูลที่ฉันจะใช้สร้างอนาคตของฉัน หลังจากที่ผ่านบททดสอบหลากหลายมานานแล้ว ในที่สุด\nภาพรวมของชีวิตในอนาคตของฉันก็เริ่มปรากฏแล้ว"

# "My body may be like this, but my mind is still very much able."
"ร่างกายฉันอาจจะไม่แข็งแรงดี แต่จิตใจฉันยังเต็มร้อย"

# hi "Thank you."
hi "ขอบคุณครับ"

stop music fadeout 2.0

scene black
with dissolve

$ suppress_window_after_timeskip = True

#*******************

label th_L26:

window hide None

scene black
with dissolve

nvl clear
nvl show dissolve

# n "\n\n“This is strange.”"
n "\n\n“แปลก”"

play music music_pearly fadein 5.0

$ ksgallery_unlock("evul hisao_teacup")
show ev hisao_teacup:
    truecenter
    alpha 0.0 subpixel True
    linear 30.0 alpha 0.5
with None

# n "\n\nThat single thought has graced my mind a countless number of times since my life here began."
n "\n\nคำเดียวคำนั้นเป็นคำที่แล่นผ่านความคิดฉันหลายครั้งนับตั้งแต่ฉันได้เริ่มใช้ชีวิตที่นี่"

# n "It feels like an easy way to discard a troubling question, as if simply labeling something with those three words will make it go away, or at least not worth thinking about any further."
n "ราวกับว่าคำนั้นเป็นคำสั้น ๆ ที่ใช้ปัดคำถามชวนรำคาญใจ ราวกับว่าหากแปะป้ายว่าแปลกแล้วคำถามนั้นจะหายไป\nหรืออย่างน้อยก็จะได้ไม่ต้องคิดอะไรต่อ"

# n "My life before my heart attack feels more blurry every time I try to remember it, and my mind struggles to keep up with all the events suddenly happening around me since."
n "ยิ่งฉันหวนนึกถึงชีวิตก่อนเกิดเหตุการณ์หัวใจวายนั้นภาพก็ยิ่งเลือนรางไปทุกที และสมองฉันก็ไม่ค่อยจะรับรู้ถึงเหตุการณ์\nต่าง ๆ รอบตัวหลังจากนั้นด้วย"

# n "I heard somewhere that this is what it feels like to be left stranded in a country with only the most basic understanding of the local language."
n "ฉันได้ยินมาว่าความรู้สึกนี้เหมือนกับการที่ถูกทิ้งให้อยู่ตัวคนเดียวในต่างประเทศโดยที่พูดภาษาของประเทศนั้นได้แบบ\nขั้นพื้นฐานสุด ๆ เท่านั้น"

# n "Indeed, when I think about it, that seems a marvelously apt analogy for what's happened to me."
n "ซึ่งเมื่อลองคิดดูแล้วก็จริง ช่างเป็นการเปรียบเปรยซึ่งเข้ากับสิ่งที่เกิดขึ้นกับตัวฉันได้ดีมาก"

nvl clear

# n "\n\nBut such situations are also supposed to make you very capable in that language very fast, as you're forced to learn it in order to survive. Put another way, the situation becomes “sink or swim.”"
n "\n\nแต่สถานการณ์อย่างนั้นควรที่จะทำให้เก่งภาษาขึ้นได้เร็วด้วย เพราะจะเอาตัวรอดได้ก็ต้องเรียนรู้ภาษา หรือจะพูดอีกแบบ\nก็คือ เป็นสถานการณ์ที่ “ไม่อยู่ก็ตาย”"

# n "\nI wonder if I've really managed to swim, after all this time."
n "\nแล้วที่ผ่านมานี่ฉันอยู่รอดมาจริง ๆ หรือเปล่านะ"

# n "The exams are stressing me out a lot, even though they're finally coming to an end, but I have remained in Mutou's favor, and I have some sort of direction for my future now."
n "ฉันเครียดกับเรื่องสอบมาก ถึงจะใกล้สอบเสร็จแล้วก็เถอะ แต่ตอนนี้ฉันยังเป็นนักเรียนดีเด่นของครูมุโต้อยู่ และเริ่มมี\nเส้นทางอนาคตของตัวเองแล้ว"

# n "But I keep using that stupid, meaningless phrase."
n "แต่ฉันก็ยังเอาแต่ใช้คำงี่เง่าไร้ความหมายคำนั้นอยู่ดี"

# n "\n\n“This is strange.”"
n "\n\n“แปลก”"

nvl clear

# n "\n\nIt really is amazing how fast one comes to accept being surrounded by people with sometimes incredibly jarring disabilities and conditions."
n "\n\nน่าทึ่งจริง ๆ ที่คนเราปรับตัวอยู่กับกลุ่มคนที่มีบางคนพิการหรือมีอาการซึ่งเห็นแล้วชวนให้ใจคอไม่ดีได้รวดเร็วขนาดนี้"

# n "So much so, that I really wonder why I feel so much like a foreigner."
n "รวดเร็วเสียจนฉันสงสัยว่าทำไมฉันถึงยังรู้สึกเหมือนเป็นคนนอกขนาดนี้"

# n "\nIt certainly isn't for lack of socialization or friends. I've come to know most of my classmates on first-name terms, and know a few others around the school. Whether they're missing an arm or a leg, the students here are just like anyone else of their age."
n "\nคงไม่ใช่เพราะเรื่องสังคมหรือเพื่อนหรอก ฉันเองก็เป็นเพื่อนกับคนในห้องหลายคนแบบที่ไม่ต้องเรียกนามสกุลกันแล้ว\nและยังพอจะรู้จักคนอื่น ๆ ในโรงเรียนอยู่บ้าง แม้บางคนจะไม่มีแขนหรือขา แต่นักเรียนที่นี่ก็เหมือนกับคนอื่น ๆ\nในวัยเดียวกันโดยทั่วไป"

# n "\n\nI can navigate the halls that I once lost myself in with an ease I'd not expected to ever have, thanks to the school's logical layout, and can engage my teachers in comfortable discussion."
n "\n\nด้วยความที่ผังโรงเรียนนี้นั้นถูกออกแบบมาอย่างสมเหตุสมผล ฉันจึงเดินเข้าตึกนั้นออกตึกนี้ได้โดยที่ไม่หลงอย่างเคย\nซึ่งชินชนิดที่ว่าฉันคาดไม่ถึงเลย และยังคุยกับครูหลาย ๆ ท่านได้แบบไม่อึดอัด"

nvl clear
nvl hide dissolve

scene ev hisao_teacup:
    truecenter
    zoom 1.0 subpixel True alpha 1.0
    acdc_warp 20.0 zoom 0.8
with locationchange

window show

# "I swirl around gently the tea in my cup, the reflected image of my face becoming distorted by the moving liquid."
"ฉันแกว่งชาในถ้วยเบา ๆ ภาพสะท้อนของฉันบิดเบี้ยวไปตามรูปร่างของเหลวที่เคลื่อนตัวอยู่"

# "This is strange… I used to hate drinking tea."
"แปลก… ฉันไม่ชอบดื่มชานี่นา"

# hi "Maybe I'm thinking too much."
hi "ฉันคงคิดมากไปมั้ง"

play sound sfx_teacup

# "The familiar sound of china rattling from a teacup touching an accompanying saucer rings out."
"ถ้วยชากระทบกับจานรองส่งเสียงกรุ๋งกริ๋งอย่างเครื่องกระเบื้องอันคุ้นเคย"

# li "Is something the matter?"
li "มีอะไรหรือเปล่าจ๊ะ"

# hi "Don't worry, it's nothing."
hi "เปล่า ๆ ไม่มีอะไรหรอก"

scene bg school_dormlilly
show hanagown normal:
    tworight
    ypos 1.15
show lilly basic_smileclosed_paj:
    twoleft
    ypos 1.2
with whiteout

# "I take a long sip of the tea in front of me as the girls do."
"ฉันยกถ้วยชาขึ้นจิบพร้อม ๆ กับสองสาว"

# "Just whiling away the time in Lilly's room sipping tea with her and Hanako. It feels familiar, almost nostalgic."
"การได้อยู่จิบชาแบบสบาย ๆ ในห้องของลิลลี่กับลิลลี่แล้วก็ฮานาโกะอย่างนี้นั้นช่างเป็นความรู้สึกที่คุ้นเคยคลับคล้าย\nความคิดถึง"

# hi "So how's your work in the newspaper club going, Hanako?"
hi "แล้วชมรมหนังสือพิมพ์เธอเป็นยังไงบ้างฮานาโกะ"

show lilly basic_satisfied_paj
with charachange

# li "I want to know too, it sounds like it would be quite interesting."
li "ฉันก็อยากรู้เหมือนกัน ฟังดูน่าสนใจดีนะจ๊ะ"

show hanagown distant
with charachange

# "Hanako's face turns down at the attention placed upon her, though her smile belies the fact that she genuinely likes being the center of interest for the two of us."
"ฮานาโกะหลุบตามองต่ำเมื่อความสนใจของพวกเราสองคนเบนไปที่เธอ แต่รอยยิ้มของเธอก็แสดงให้เห็นว่าเธอชอบ\nเมื่อได้เป็นจุดสนใจของพวกเราจริง ๆ"

# ha "It's… good. I think I'm getting better at it."
ha "ก็… ดีนะ คิดว่าเริ่มคล่องแล้วละ"

# ha "Naomi and a couple of her friends handle most of the jobs… getting stories and stuff."
ha "ส่วนมากนาโอมิกับเพื่อนนาโอมิอีกสองคนก็เป็นคนจัดการ… อย่างการหาข่าวหรืออะไรแบบนั้น"

show hanagown smile
with charachange

# ha "I just do the computer things, like putting the stories together and getting it printed. I-it's nice, since I can sit and concentrate."
ha "ฉันแค่ทำงานอยู่กับคอมพิวเตอร์น่ะ อย่างการเรียบเรียงหรือพิมพ์ข่าว ซะ ซึ่งก็ดีนะ เพราะฉันจะได้นั่งจดจ่อกับงาน"

# "I see Lilly's low-tech nature isn't shared by Hanako. While sitting in a room compiling other people's newspaper articles into documents doesn't strike me as overly outgoing, it is heartening to see her widening her circle of friends."
"แสดงว่ามีแค่ลิลลี่สินะที่ไม่ถนัดเรื่องคอมพิวเตอร์ ถึงการนั่งอยู่ในห้องรวมรวบบทความหนังสือพิมพ์ของคนอื่นออกมา\nเป็นเอกสารนั้นจะไม่ใช่การพบปะผู้คนมากมายขนาดนั้น แต่พอได้เห็นว่าฮานาโกะมีเพื่อนใหม่อย่างนี้บ้างแล้วก็ใจชื้น\nอยู่เหมือนกัน"

# "Baby steps, I guess. It's probably a bit much to be expecting her to become a socialite like Lilly."
"ก็นับเป็นก้าวเล็ก ๆ ละนะ จะให้คาดหวังไปเป็นคนชอบเข้าสังคมอย่างลิลลี่ก็คงเกินไปหน่อย"

show lilly basic_oops_paj
with charachange

# li "How are you finding Naomi? I've heard she can be quite troublesome at times."
li "แล้วนาโอมิเขาเป็นยังไงบ้าง เหมือนได้ยินมาว่าบางทีก็มีเรื่องให้ปวดหัวเหมือนกัน"

# "And Lilly's going into her mothering mode over Hanako. Letting go of her is something she's had to learn."
"แล้วลิลลี่ก็เปิดโหมดคุณแม่ใส่ฮานาโกะอีกครั้ง หัดเรียนรู้ที่จะปล่อยฮานาโกะไปบ้างได้แล้วนะ"

show hanagown worry
with charachange

# "Hanako scratches her cheek, thinking on her answer."
"ฮานาโกะเกาแก้มคิดคำตอบ"

show hanagown smile
with charachange

# ha "Naomi's… nice. She's a bit loud sometimes, and a bit tiring… but she's really helpful. Her friends are nice, too."
ha "นาโอมิก็… เป็นคนดีนะ บางครั้งก็เสียงดังไปหน่อย อยู่ด้วยแล้วเหมือนหมดแรง… แต่ก็พึ่งพาได้มากเลย เพื่อนนาโอมิ\nก็ใจดีเหมือนกัน"

show lilly basic_cheerful_paj
with charachange

# li "That's wonderful to hear, Hanako. I'm glad you've found a source of such enjoyment."
li "งั้นก็ดีแล้วละจ้ะฮานาโกะ ยินดีด้วยนะที่เธอได้เจออะไรที่ชอบอย่างนี้"

# "Lilly's smile is warm and genuine, but I can sense a touch of wistfulness to it as well. Hanako seems to miss that entirely, but I don't think for a second that I'm imagining it."
"รอยยิ้มของลิลลี่นั้นทั้งอบอุ่นและจริงใจ แต่ฉันก็สัมผัสได้ถึงความเศร้าสร้อยในรอยยิ้มนั้นด้วย ถึงฮานาโกะเหมือนจะ\nไม่ได้สังเกตเลย แต่ฉันไม่ได้คิดไปเองหรอกว่าเป็นรอยยิ้มอย่างนั้น"

# "I suppose it's because I've slowly come to pay more and more attention to everything going on around me. With things seemingly happening faster and faster, it feels like I'll miss something if I'm not as observant as possible."
"คงจะเพราะฉันเริ่มให้ความสนใจกับสิ่งต่าง ๆ รอบตัวมากขึ้นเรื่อย ๆ ทุกอย่างเกิดขึ้นด้วยความเร็วที่เพิ่มขึ้นเรื่อย ๆ จน\nฉันรู้สึกราวกับว่าหากมองไม่ละเอียดพอแล้วฉันจะพลาดบางอย่างไป"

# "With the exams, my newfound love life, trying to fit in some studying regarding my options for college and university, and my heart condition applying the brakes on everything at irritatingly random times, my brain's been in overdrive recently."
"ช่วงนี้สมองของฉันต้องทำงานหนัก ด้วยว่ามีทั้งเรื่องสอบ ชีวิตรักที่เพิ่มเริ่มต้น การหาเวลาศึกษาเส้นทางการเรียนต่อ\nพร้อมหัวใจของฉันที่จะมาหยุดให้ฉันสะดุดเป็นพัก ๆ อย่างน่าหงุดหงิด"

# "It makes me appreciate the rare quiet times such as these."
"จนฉันรู้สึกยินดีเหลือเกินที่ได้มีเวลาสงบ ๆ ซึ่งหาได้ยากเช่นนี้"

# "I guess this is why Lilly came to appreciate her weekly walks to the convenience store and her tea parties with Hanako, despite her like of being surrounded by others; they gave her a moment of peace in a chaotic and busy life."
"คงจะเพราะอย่างนี้ละมั้งลิลลี่ถึงได้ชอบการเดินไปร้านสะดวกซื้อทุกสัปดาห์กับการจัดงานเลี้ยงน้ำชากับฮานาโกะทั้งที่\nเธอเองก็ชอบการอยู่กับคนอื่น เพราะเหล่านี้เป็นช่วงเวลาที่ลิลลี่จะได้อยู่อย่างสงบปลีกตัวจากชีวิตอันสับสนวุ่นวาย\nของเธอ"

# hi "Thank god the exams are over, eh?"
hi "ดีจังเลยเนอะที่สอบเสร็จสักที"

show lilly basic_giggle_paj
with charachange

# "The comment draws an earnest chuckle from both of the girls. It seems like everybody's been a lot happier since the exams ended, last week."
"สองสาวแค่นหัวเราะกับคำพูดของฉัน ดูเหมือนว่าทุกคนจะมีความสุขกันมากขึ้นนับตั้งแต่สัปดาห์ก่อนที่สอบเสร็จ\nกันไป"
#Exams finished on a Monday, and now is the next Monday's evening. Also, exams started on a Wednesday (there's a reference at the very start of Act 3). -SC

# hi "So what're you doing for the summer holidays, Hanako? Only…"
hi "แล้วปิดเทอมนี้เธอจะทำอะไรเหรอฮานาโกะ เหลืออีกแค่…"

# "I quickly count the days in my head. Today's Monday, and school finishes on Saturday…"
"ฉันนับวันในหัวแบบคร่าว ๆ วันนี้วันจันทร์ มีเรียนวันสุดท้ายวันเสาร์…"

# hi "…five days to go, after all."
hi "…ห้าวันก็จะปิดเทอมแล้วนี่"

show hanagown normal
with charachange

# ha "I was thinking of… traveling. Just… around a bit."
ha "ฉันกะว่าจะ… ไปเที่ยวน่ะ ไป… เที่ยวดูอะไรหน่อย"

show hanagown smile
with charachange

# ha "There's a lot of places I want to see, and… I think I have enough money to pay for the bus and train rides. Naomi and one of the other girls in the newspaper club said they might come along, too."
ha "มีหลายที่เลยที่ฉันอยากไปเที่ยว แล้วก็… น่าจะมีเงินพอขึ้นรถบัสกับรถไฟอยู่ นาโอมิกับคนอื่นในชมรมหนังสือพิมพ์\nก็บอกด้วยว่าเดี๋ยวอาจจะไปด้วย"

# "Her look indicates she's given the matter quite a lot of thought. I'm kind of surprised that she's contemplating something like this."
"ฮานาโกะทำสีหน้าว่าคิดเรื่องนี้มาอย่างจริงจังแล้ว แปลกใจอยู่เหมือนกันที่ฮานาโกะวางแผนเที่ยวอะไรอย่างนี้"

# "It seems she's really become intent on striking out on her own."
"ดูเหมือนว่าฮานาโกะตัดสินใจแล้วว่าจะออกมุ่งหน้าไปด้วยตัวของเธอเอง"

show lilly basic_smile_paj
with charachange

# li "Is there anywhere in particular you're thinking of going?"
li "มีที่ไหนที่คิดไว้ว่าจะไปโดยเฉพาะเลยหรือเปล่าจ๊ะ"

show hanagown distant_blush
with charachange

# ha "I was thinking that… Kyoto sounds nice. I-I think I'll try to go to a few places… though."
ha "คิดอยู่ว่า… เกียวโตก็น่าจะดีนะ ตะ แต่เดี๋ยวจะไปลองดู… ที่อื่นด้วย"

show lilly basic_cheerful_paj
with charachange

# "Lilly nods in approval, happy with Hanako's plans."
"ลิลลี่พยักหน้าพอใจเห็นด้วยกับแผนของฮานาโกะ"

# "While I cast my eyes to Lilly, I refrain from asking her the same question. She's been evasive with her plans for the future for a long time now, but I never seem to get a good time to broach the subject alone with her."
"ฉันมองไปทางลิลลี่ด้วยคำถามเดียวกันในใจที่ไม่ได้ถามออกไป เธอเลี่ยงที่จะคุยเรื่องแผนในอนาคตของตัวเองมานานแล้ว\nและฉันก็ยังหาจังหวะเหมาะ ๆ ที่จะยกเรื่องนี้ขึ้นมาคุยกับเธอไม่ได้เสียที"

# "Every time it comes up in conversation, it feels like she's either unsure of herself or simply dodging the question. It's troubling."
"ทุกครั้งที่มีเรื่องนี้เข้ามาในบทสนทนา ลิลลี่ก็จะทำท่าเหมือนไม่แน่ใจหรือไม่ก็เลี่ยงคำถามไปเลย ซึ่งทำให้ฉันหงุดหงิด"

# hi "Be sure to call sometime while you're out and about. I gave you my number before, right?"
hi "ตอนไปเที่ยวก็โทร. มาหาบ้างนะ ฉันเคยให้เบอร์ไปแล้วใช่มั้ย"

show hanagown smile
with charachange

# "Hanako gives a quick nod, a happy smile on her face."
"ฮานาโกะพยักหน้าน้อย ๆ พร้อมรอยยิ้ม"

# "It's strange to see how happy people seem to become when they have a goal to work towards. Yuuko seems to brighten whenever her university aspirations are brought up, and now Hanako is just the same."
"แปลกดีเหมือนกันที่พอมีเป้าหมายแล้วคนเราจะมีความสุขได้ขนาดนี้ ยูโกะดูจะดีใจทุกครั้งที่ได้คุยเรื่องความมุ่งมั่นต่อ\nชีวิตมหาวิทยาลัยของตัวเอง ตอนนี้ฮานาโกะก็ไม่ต่างกันเลย"

# "So why do I still feel this uncertainty? And why Lilly, too?"
"แล้วทำไมฉันถึงยังรู้สึกไม่แน่ใจอีกล่ะ แล้วทำไมลิลลี่ถึงรู้สึกเหมือนฉันด้วย"

# "Relationships really can be irritatingly troublesome, sometimes."
"บางครั้งความสัมพันธ์ก็เป็นอะไรที่ชวนให้หงุดหงิดปวดหัว"

show hanagown worry
with charachange

# ha "Oh, um… wh-what time is it?"
ha "อ๊ะ เอ่อ… ตะ ตอนนี้กี่โมงแล้วเหรอ"

# hi "Hmm? Oh…"
hi "หืม? อ้อ…"

# "It takes me a second to remember that Lilly's clock doesn't have any visual feedback. I really should know, given how many times I've been in her room."
"สักพักฉันถึงนึกได้ว่านาฬิกาของลิลลี่นั้นไม่มีการแสดงผลอะไรให้เห็นเลย ซึ่งที่จริงก็น่าจะรู้แต่แรกเพราะฉันมาห้องลิลลี่\nหลายครั้งแล้ว"
#Flagging this, it's double-referenced elsewhere, so if it gets changed it has to be mirrored. -SC

# "Nevertheless, I take my watch from my bag and quickly check it, the reason for her asking becoming clear."
"แต่ถึงอย่างนั้นฉันก็คว้านาฬิกาที่อยู่ในกระเป๋าออกมา พอดูก็รู้ว่าทำไมฮานาโกะถึงถาม"

# hi "It's about twenty past ten. Nearly curfew."
hi "ประมาณสี่ทุ่มยี่สิบได้ ใกล้ถึงเวลาปิดประตูหอแล้ว"

show hanagown normal:
   ypos 1.0
with dissolvecharamove

# "Hanako rises to her feet, dusting herself off and neatening her gown after doing so."
"ฮานาโกะลุกขึ้นยืนแล้วปัดเนื้อปัดตัวจัดแจงชุดนอนตัวเอง"

show hanagown smile
with charachange

# ha "I'd… better be going, then. Good night Lilly, Hisao."
ha "งั้นฉัน… ไปก่อนนะ ราตรีสวัสดิ์นะลิลลี่ ฮิซาโอะ"

stop music fadeout 5.0

show lilly basic_smileclosed_paj
with charachange

# li "Sleep well, Hanako."
li "ฝันดีจ้ะฮานาโกะ"

# hi "Seeya tomorrow."
hi "เจอกันพรุ่งนี้"

hide hanagown
with dissolve

# "With that, she walks to the door and quietly makes her exit."
"แล้วเธอก็เดินออกไปเงียบ ๆ"

show lilly basic_smileclosed_paj:
    xpos 0.5
show bg school_dormlilly at bgright
with charamove

"…"

# "Silence."
"เงียบ"

# "This seems to be happening more and more between Lilly and me, recently. After a few seconds, I finally find something to talk about."
"ช่วงนี้เหมือนลิลลี่กับฉันจะเงียบใส่กันบ่อยขึ้นเรื่อย ๆ ผ่านไปสักพักฉันถึงนึกเรื่องคุยได้"

play music music_another fadein 4.0

# hi "Oh yeah, I talked to Mutou on Friday, and finally checked out some guides on college and how to apply for it."
hi "อ้อ เออ วันศุกร์ฉันไปคุยกับครูมาแล้วนะ ไปดูเรื่องเรียนต่อกับการสมัครมาแล้วด้วย"

show lilly basic_smile_paj
with charachange

# li "That's good news. If you're going to be applying for colleges, I assume you have some idea in mind of what you might do in the future?"
li "ดีเลยจ้ะ ถ้าเธอจะเรียนต่อ แปลว่ามีอาชีพที่คิดจะทำในอนาคตแล้วใช่ไหม"

# hi "I think I've settled on becoming a science teacher. It's going to take a while to get through university and everything to be qualified, but I think it'll be worth it."
hi "ฉันว่าน่าจะเป็นครูสอนวิทยาศาสตร์นี่แหละ อาจจะนานหน่อยกว่าจะจัดการเรื่องใบรับรองอะไรหลังเรียนจบจนเสร็จ\nแต่ก็น่าจะคุ้มกันอยู่"

show lilly basic_satisfied_paj
with charachange

# "Lilly's face brightens considerably at the news. I suppose, with her wish to become a teacher, she's delighted I'd take the same kind of path."
"ลิลลี่ทำท่าสดใสขึ้นพอตัวเมื่อได้ยินเช่นนั้น ก็คงจะดีใจละมั้งที่ฉันเลือกจะไปเส้นทางการเป็นครูเหมือนอย่างเธอ"

# li "So, you've decided on a career of teaching…"
li "แปลว่าเธอตัดสินใจที่จะเป็นครูแล้ว…"

show lilly basic_smile_paj
with charachange

# li "I think that path suits you most excellently, Hisao."
li "เป็นเส้นทางที่เหมาะกับเธอดีนะจ๊ะฮิซาโอะ"

# "I smile and nod. This time, even if I know she can't see me doing so, I know she feels it."
"ฉันยิ้มและพยักหน้า แม้เธอจะมองไม่เห็น แต่ฉันรู้ว่าเธอสัมผัสได้"

show lilly basic_planned_paj
with charachange

# li "I imagine Mutou would have taken to the news well?"
li "ครูก็คงดีใจใช่มั้ยที่เธอเลือกอย่างนี้"

# hi "That's one word for it."
hi "ก็ดีใจแหละนะ"

# hi "Hey Lilly?"
hi "นี่ ลิลลี่"

show lilly basic_smile_paj
with charachange

# li "Yes?"
li "อะไรเหรอจ๊ะ"

# hi "I know you want to be a teacher, but…"
hi "ฉันรู้แหละว่าเธออยากเป็นครู แต่…"

# "For a second, I wonder whether I should really ask her the question on my mind, but that's quickly brushed aside by the fact that this is rather late to have second thoughts."
"แวบหนึ่งฉันชั่งใจว่าจะถามดีหรือไม่ แต่ก็ไม่คิดต่อเพราะพูดมาถึงขนาดนี้แล้ว จะให้ย้อนคิดอะไรอีกก็คงสายไปแล้ว"

show lilly basic_smileclosed_paj
with charachange

# li "Surely you don't still think I'd be offended by something regarding my blindness."
li "ป่านนี้แล้วเธอยังจะกลัวว่าฉันจะไม่พอใจที่ฉันตาบอดอีกเหรอ"

# "Her accusing tone is betrayed by her grinning face, amused at my awkwardness in raising the topic. Some things never change."
"ลิลลี่ทำน้ำเสียงต่อว่าขัดกับรอยยิ้มชอบใจที่ฉันยังอึกอักกับการคุยเรื่องนี้ บางอย่างมันก็เหมือนเดิมอยู่เสมอจริง ๆ"

# hi "Good point, I guess."
hi "ก็กลัวแหละ"

# hi "I was just thinking whether or not being blind would be a hindrance, what with your ambitions to become a teacher and all."
hi "พอดีฉันคิดอยู่ว่าถ้าตาบอดแล้วมันจะมีปัญหาหรือเปล่า ก็เธอมุ่งมั่นอยากเป็นครูอยากอะไรขนาดนี้"

show lilly basic_surprised_paj
with charachange

# "She looks mildly surprised before giving the question some thought. I refuse to think she's never actually pondered this issue before."
"ลิลลี่ดูแปลกใจเล็กน้อยก่อนครุ่นคิดถึงคำตอบ แต่ยังไงเธอก็คงต้องเคยคิดเรื่องนี้มาก่อนอยู่แล้วแหละ"

show lilly basic_emb_paj
with charachange

# li "I wonder… Hisao, could you close your eyes for a moment?"
li "นั่นสินะ… ฮิซาโอะ หลับตาสักแป๊บหนึ่งได้ไหมจ๊ะ"

# hi "O… kay?"
hi "โอ… เค?"

# "Raising an eyebrow, I do as she requests."
"ฉันเลิกคิ้วแล้วหลับตาตามลิลลี่สั่ง"

$ renpy.music.set_volume(0.5, 2.0, channel="music")

scene black
with shuteye

# "I have no idea what she has in mind, and my questions only increase as I peek out from one eye."
"ฉันไม่รู้ว่าลิลลี่คิดอะไรอยู่ และยิ่งมีคำถามในหัวมากขึ้นเมื่อได้แอบมองด้วยตาข้างหนึ่ง"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

show bg school_dormlilly at bgright
show lilly basic_smileclosed_paj_close at center
with openeye

# "Taking the black ribbon she usually wears in her hair from the cabinet beside her bed, she advances towards me while running it through her fingers to remove any stray hairs remaining on the piece of cloth."
"ลิลลี่หยิบแถบผ้ามัดผมสีดำที่เธอใช้เป็นประจำออกมาจากตู้ที่อยู่ข้างเตียงก่อนจะขยับเข้ามาหาฉันพลางรีดแถบผ้า\nเอาเศษผมที่ติดอยู่ออก"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene black
with softwipedown

# "I suddenly click on to her intentions as I feel the black strip make contact with my face, wrapping around my head and over my eyes."
"และฉันก็รู้ทันทีว่าลิลลี่จะทำอะไรเมื่อแถบสีดำนั้นพาดเข้ามาที่ตาแล้วคาดหัวฉัน"

# hi "Um… what exactly is this for?"
hi "เอ่อ… ทำทำไมเหรอ"

# li "It's a little test, Hisao. Since you seem to be wondering, I'll let you see things as I do for a time."
li "แบบทดสอบเล็ก ๆ น้อย ๆ น่ะฮิซาโอะ เห็นเธอสงสัยเลยจะให้ลองมองอะไรอย่างที่ฉันเห็นสักหน่อย"

# "Huh, so that's what this is about."
"หืม อย่างนี้นี่เอง"

# "To be honest, this actually sounds kind of fun. Childish and rather silly to anyone who would be watching, but a bit of silly fun never hurt anyone."
"ว่าตามตรงก็ฟังดูสนุกดี คนอื่นอาจจะมองว่าทำอะไรงี่เง่าเป็นเด็ก ๆ แต่ทำอะไรสนุก ๆ ไร้สาระสักหน่อยก็ไม่เสียหาย\nนี่นา"

# "I stand up with a heave, my hands quickly moving out in front of me to warn me of any obstacles."
"ฉันสูดลมหายใจลุกขึ้นยืนแล้วรีบยื่นมือไปข้างหน้าเพื่อสัมผัสว่ามีอะไรขวางทางอยู่หรือเปล่า"

# hi "Okay, now what?"
hi "โอเค แล้วยังไงต่อ"

# li "Now, touch me."
li "ทีนี้ก็แตะฉัน"

# hi "If you say so. Now then…"
hi "แตะก็แตะ เอาละ…"

# "I slowly make my way forwards, towards the sound of Lilly's voice."
"ฉันค่อย ๆ เดินไปข้างหน้าตามเสียงลิลลี่"

# "My walking speed could barely even be called a shuffle, the entire experience feeling alien enough that I don't want to risk inadvertently tripping over anything, such as her table or her haphazard piles of books."
"ฉันเดินช้าจนเหมือนไม่ได้ขยับขาด้วยซ้ำ เป็นประสบการณ์ที่ประหลาด ประหลาดจนฉันไม่อยากเผลอไปสะดุดอะไร\nอย่างโต๊ะหรือกองหนังสือที่วางไว้ลวก ๆ เข้า"

play sound sfx_rustling

# "Something soft, yet solid, brushes against my left leg. Further inspection reveals it to be Lilly's bed."
"บางอย่างนุ่ม ๆ แข็ง ๆ ถูกเข้ากับขาซ้ายฉัน พอลองจับดูดี ๆ ถึงได้รู้ว่าเป็นเตียงของลิลลี่"

# "I move onwards, finding myself thankful that Lilly's room is so neat and tidy. Even the piles of books she has are generally kept close to the wall, well out of harm's way."
"ฉันเดินต่อพลางนึกยินดีในใจที่ห้องลิลลี่นั้นแสนจะเป็นระเบียบเรียบร้อย กองหนังสือของเธอส่วนใหญ่ก็วางไว้ชิดกำแพง\nไม่เป็นอุปสรรคอะไร"

play sound sfx_pillow

# "The hard wall pressing against my outstretched hands makes me furrow my brow in frustration."
"พอยื่นมือออกไปจับโดนกำแพงแข็ง ๆ แล้วฉันก็ขมวดคิ้วด้วยความหงุดหงิด"

# hi "Hey Lilly, where are you?"
hi "นี่ ลิลลี่ อยู่ไหนเนี่ย"

# li "What are you doing over there? I'm over here."
li "ไปทำอะไรตรงนั้น ฉันอยู่ตรงนี้ต่างหาก"

# "Lilly's voice comes from the other side of the room, far from where it was before, even to my untrained ears. If she's going out of her way to avoid me reaching her, then is this just a game to her?"
"แม้จะไม่ได้ฝึกการได้ยินมา แต่ฉันก็รับรู้ได้ถึงเสียงของลิลลี่ดังมาจากอีกฝั่งหนึ่งของห้อง ซึ่งไกลจากที่ที่ฉันได้ยินเมื่อครู่\nมาก ถ้าจะจงใจหนีกันขนาดนี้ ก็แปลว่าตอนนี้ลิลลี่แค่เล่นสนุกเฉย ๆ งั้นเหรอ"

# "…Of course it is. Compared to a life where even the concept of sight is an abstract one, a few minutes in a blindfold are nothing."
"…ก็แหงอยู่แล้ว กับชีวิตที่แม้แต่การมองเห็นยังเป็นได้แค่ความคิดเชิงนามธรรม การปิดตาแค่สองสามนาทีจะไปเทียบ\nอะไรได้"

# "I guess she's made her point; she's more than capable of navigating her room, and further, I've seen how independent she is even when compared to many of the others in Yamaku."
"สิ่งที่ลิลลี่จะสื่อนั้นก็คงถูกแล้วละ เธอสามารถเดินไปมาในห้องได้สบาย ๆ แล้วยิ่งไปกว่านั้น ถ้าให้เทียบกับอีกหลายคน\nในยามากุ ฉันก็ได้เห็นแล้วว่าลิลลี่แทบไม่ต้องพึ่งคนอื่นเลย"

# "Well, even if this is just a game, I may as well play it wholeheartedly."
"แต่เอาเถอะ ถ้าอยากจะเล่นสนุกเฉย ๆ ก็เล่นให้มันเต็มที่เลยแล้วกัน"

# "With a pace much quicker than before I move towards the source of her voice, deftly sidestepping the table in the center of her room thanks to remembering its position."
"ฉันเดินไปทางต้นเสียงด้วยฝีเท้าที่เร็วกว่าเมื่อครู่มากและหลบโต๊ะที่อยู่กลางห้องได้อย่างคล่องแคล่วเพราะจำตำแหน่งได้"

# hi "I've got you now!"
hi "รอเดี๋ยวเถอะ!"

# "She gives an impish giggle, one just long enough to work out that she's passing just beside me."
"ลิลลี่หัวเราะคิกคักซุกซน หัวเราะอยู่นานจนฉันรู้ตัวว่าเธอเดินสวนฉันไป"

play sound sfx_impact2
with vpunch

# "I quickly turn around to face the new directio— the table wasn't there before!"
"ฉันหันไปอีกทางอย่างเงี— เมื่อกี้โต๊ะไม่ได้อยู่ตรงนี้นี่นา!"

# hi "Ow… ow… ow…"
hi "โอ๊ย… โอย… โอย…"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

show bg school_dormlilly
with softwipeup

# "I slowly sit up next to the table, raising my blindfold as I rub my aching head."
"ฉันขยับตัวช้า ๆ มานั่งข้างโต๊ะแล้วถกผ้าปิดตาออกพลางลูบหัวที่ปวด ๆ"

play sound sfx_impact
with vpunch

# "I give an irritated kick to the table that's sitting just in front of where I fell. Utterly pointless, but the thing deserved it."
"ฉันเตะโต๊ะที่อยู่ตรงหน้าจุดที่ฉันสะดุดด้วยความหงุดหงิด ก็ไม่ได้อะไรขึ้นมาหรอก แต่โต๊ะนี่ก็สมควรโดนสักที"

show lilly basic_oops_paj_close at center
with charaenter

# li "Hisao?"
li "ฮิซาโอะ"

# "Lilly's still standing just to my side, obviously unsure of what's befallen me."
"ลิลลี่ยืนนิ่งอยู่ข้างฉันไม่แน่ใจว่าฉันสะดุดกับอะไร"

# hi "Sorry. I kinda fell over."
hi "ขอโทษที สะดุดนิดหน่อย"

show lilly basic_concerned_paj_close
with charachange

# li "Are you hurt?"
li "เจ็บตรงไหนมั้ย"

# hi "My head hurts, but I think I'm okay. I think the table moved in order to trip me over."
hi "ปวดหัวนิดหน่อย แต่ไม่น่าเป็นไร ฉันว่าโต๊ะมันเดินมาขัดขาฉันนะ"

show lilly basic_giggle_paj_close:
    ypos 1.1
with dissolvecharamove

# "She giggles as she walks over and takes a seat beside me, her hand resting on my own."
"ลิลลี่หัวเราะคิกคักเดินมานั่งข้าง ๆ แล้วจับมือฉัน"

show lilly basic_weaksmile_paj_close
with charachange

# li "I suppose that's the end of that then?"
li "งั้นก็พอแค่นี้นะจ๊ะ"

# hi "I think so."
hi "ก็คงต้องพอละนะ"

# hi "But I also think I get the point. Though I do wish it hadn't involved such a headache."
hi "แต่ฉันว่าฉันเข้าใจสิ่งที่เธอจะสื่อแล้วละ แต่ก็ไม่อยากต้องมาเจ็บตัวอย่างนี้เลยนะ"

show lilly basic_surprised_paj_close
with charachange

# "Lilly suddenly looks blank."
"อยู่ ๆ ลิลลี่ก็ทำหน้างง"

# li "Point?"
li "สิ่งที่จะสื่อ?"

# "And I return an extraordinarily flat look."
"และฉันก็ทำหน้างงสุดขีดพอกันตอบกลับไป"

# hi "That was just for fun?"
hi "สรุปคือเล่นสนุกเฉย ๆ ?"

show lilly basic_reminisce_paj_close
with charachange

# li "I just thought it might ease you up a little about the subject. You always seem to tiptoe around it, after all."
li "ฉันแค่คิดว่าทำอย่างนี้แล้วเธอจะได้หายอึดอัดกับเรื่องนี้หน่อยน่ะจ้ะ เหมือนจะพูดทีไรก็เอาแต่อ้อมไปอ้อมมาตลอดเลย"

show lilly basic_smileclosed_paj_close
with charachange

# li "In regard to teaching, sight isn't that important. There are plenty of classes taught by entirely blind teachers, and more than enough resources for me to learn the subject."
li "ส่วนเรื่องการสอนที่เธอถาม การมองเห็นน่ะไม่สำคัญหรอก หลายที่ก็มีชั้นเรียนที่ครูเป็นคนตาบอด แล้วก็มีหนังสือ\nมีอะไรให้ฉันเรียนรู้ได้อีกเยอะ"

show lilly basic_smile_paj_close
with charachange

# li "It's as simple as that, really."
li "ไม่ได้ยากอะไรเลย"

# "I slump my shoulders and give a snort of amusement."
"ฉันหย่อนไหล่ลงแล้วแค่นหัวเราะชอบใจ"

# hi "Yeah, I understand. I guess we'll both just have to work hard to reach our goals, then."
hi "อื้ม เข้าใจแล้ว งั้นเราสองคนก็ต้องมาพยายามเพื่อเดินไปให้ถึงฝันด้วยกันสินะ"

stop music fadeout 4.0

show lilly basic_cheerful_paj_close
with charachange

# li "Hmm…"
li "อืมม…"

# hi "What is it?"
hi "มีอะไรเหรอ"

# "With a little hesitation, Lilly pushes forward her chin and closes her eyes in an unmistakable gesture."
"ลิลลี่ยื่นคางมาพลางหลับตาด้วยความลังเลเล็กน้อยอันเป็นท่าทางที่ฉันจำได้ดี"

scene ev lilly_kissing
with whiteout

play music music_one fadein 1.0

# "I accept gladly, our lips touching. As they do, I suddenly feel her hand snaking up my chest from underneath my shirt. The feeling of her hand against my bare skin is enough to make my heart suddenly accelerate."
"ฉันประกบริมฝีปากรับไว้ด้วยความยินดี ทันใดนั้นเองมือของลิลลี่ก็ล้วงเข้ามาในสาบเสื้อของฉัน เพียงแค่มือเธอสัมผัส\nกับผิวของฉันก็ทำให้ใจฉันเต้นแรงขึ้นมาในทันที"

# "So she's in that kind of mood again?"
"นี่เธออยากทำอีกแล้วเหรอ"

# "Well, I'm hardly one to complain. She does genuinely like this, and even with all my medications, my libido is thankfully still intact."
"อืม ก็ว่าอะไรไม่ได้หรอก ลิลลี่เองก็ชอบจริง ๆ และโชคดีที่ความอยากของฉันยังคงมีเต็มเปี่ยม ทั้งที่ต้องกินยาเยอะ\nขนาดนั้นแท้ ๆ"

# "I lean into the kiss further, holding her hand tightly as I feel it tracing the contours of my chest."
"ฉันโน้มตัวเข้าไปจูบให้หนักหน่วงอีกแล้วจับมือเธอที่กำลังลูบไปตามผิวบนหน้าอกของฉัน"

scene bg school_dormlilly
show lilly basic_smileclosed_paj_close:
    center
    ypos 1.1
with whiteout

# "Eventually we break off from one another, the room silent but for our breathing."
"จนสุดท้ายเราก็ผละออกจากกัน ทั้งห้องนั้นเงียบสนิท มีเพียงเสียงหายใจของพวกเราเท่านั้น"

show lilly basic_surprised_paj_close
with charachange

# li "Hey, Hisao?"
li "นี่ ฮิซาโอะ"

# hi "Yeah?"
hi "ว่า"

show lilly basic_emb_paj_close
with charachange

# li "I don't suppose… you could wear the blindfold again?"
li "เธอ… ใส่ผ้าปิดตาอีกรอบได้หรือเปล่า"

# "Her tentative suggestion takes me by surprise."
"คำขอแบบอึกอักของลิลลี่นั้นมาโดยที่ฉันไม่ทันได้ตั้งตัว"

# "I suppose she wants to introduce me to sex through her eyes as well. Or just wants to find out what I'll be like during the act while hampered by the blindfold."
"คงจะอยากให้ฉันได้รู้จักสิ่งนี้ผ่านมุมมองของเธอด้วยละมั้ง หรือไม่ก็แค่อยากรู้เฉย ๆ ว่าถ้าฉันทำตอนปิดตาแล้วจะเป็น\nยังไง"

$ renpy.music.set_volume(0.5, 0.0, channel="music")


scene black
with softwipedown

# "With a measure of unease tempered by curiosity, I do as she says and lower the blindfold over my eyes. The world becomes dark once again."
"แม้จะยังอึดอัดอยู่บ้าง แต่ฉันก็พ่ายแพ้ให้กับความอยากรู้ของตัวเอง ฉันจึงเลื่อนผ้าปิดตาที่คาดหัวอยู่ลงมาปิดตา ทั้งโลก\nดับมืดไปอีกครั้ง"

# "I reflexively tense as I feel Lilly's hand gently brush the side of my face, entirely unable to anticipate her touch."
"พอลิลลี่ยื่นมือมาแตะที่แก้มฉันเบา ๆ แล้วฉันก็เกร็งไปโดยอัตโนมัติเพราะเดาไม่ถูกว่าเธอจะมาแตะ"

# "I really need to get more used to contact like this. Even after the weeks we've been going out, it isn't as natural for me as it is for her."
"ต้องทำตัวให้ชินกับสัมผัสอย่างนี้ได้แล้วสิ ถึงจะคบกันมาได้สัปดาห์สองสัปดาห์แล้ว ฉันก็ยังไม่ชินกับสัมผัสแบบนี้\nเท่าลิลลี่เลย"

# "…Silence?"
"…เงียบ?"

# hi "Hey, Lilly…"
hi "นี่ ลิลลี่…"

# li "Shh."
li "ชู่"

# "I obediently follow her instruction and quietly listen, trying to make out something, anything, that's happening around me."
"ฉันทำตามเธอสั่งเงียบไปอย่างว่าง่ายแล้วเงี่ยหูฟังว่ามีอะไรเกิดขึ้นบ้าง"

# "Compared to before when I was chasing Lilly, the need to carefully navigate the room's obstacles now gone, I can take my time and concentrate much harder on listening."
"ตอนนี้ฉันไม่ต้องคอยกังวลเรื่องสิ่งของในห้องลิลลี่ที่จะมาขวางทางตอนเดินเหมือนอย่างตอนที่ไล่จับลิลลี่เมื่อครู่แล้ว\nมีเวลาให้ตั้งสมาธิจดจ่อไปกับการฟังได้เต็มที่"

# "It takes a while, but I can eventually pick out the soft sound of her breathing in the otherwise dead silent room."
"นั่งฟังอยู่พักหนึ่งถึงได้ยินเสียงลมหายใจอ่อน ๆ ของลิลลี่ในห้องซึ่งเงียบงันนี้"

# "In… out… in… out…"
"เข้า… ออก… เข้า… ออก…"

# "Measuring it against my own breathing, I realize it's definitely deeper than normal, especially for her."
"พอลองเทียบกับลมหายใจของตัวเองแล้วถึงได้รับรู้ว่าลมหายใจนั้นยาวกว่าปกติ โดยเฉพาะถ้าให้เทียบกับจังหวะหายใจ\nตามปกติของลิลลี่"

# "Another sound makes its way to my ears, one that I can't identify immediately. I don't think I've heard it before, but…"
"แล้วก็มีอีกเสียงหนึ่งตามมา เป็นเสียงที่ฉันยังฟังไม่ออกว่าเป็นเสียงอะไร เหมือนไม่เคยได้ยินมาก่อน แต่ว่า…"

# "My heart skips a beat as I realize the source, my hand almost reflexively reaching out towards it. Her face feels softer than usual under my touch, her head just barely turning in acknowledgment towards the fingers on her cheek."
"เมื่อได้รู้ว่าเสียงนั้นมาจากไหนใจฉันก็เต้นไม่เป็นส่ำ ฉันยื่นมือไปตามเสียงนั้นโดยแทบจะอัตโนมัติ ใบหน้าของเธอที่\nถูกมือฉันนั้นอ่อนนุ่มกว่าปกติ ลิลลี่หันหน้าเล็กน้อยเมื่อรับรู้ถึงสัมผัสจากนิ้วฉันที่แตะแก้มเธอ"

# li "Hisao…"
li "ฮิซาโอะ…"

# "I gulp and take a moment to try and calm down. I need all the concentration I can muster while I'm like this in order to fully take in my surroundings."
"ฉันกลืนน้ำลายแล้วสงบใจตัวเอง ตอนนี้ฉันอยู่ในสภาพที่ต้องตั้งสมาธิให้มากที่สุดเท่าที่ทำได้เพื่อจะได้รับรู้ถึง\nสิ่งรอบตัวอย่างเต็มที่"

# "After a few deep breaths, I think I've managed to collect myself. With a touch so light that it wouldn't disturb a feather, I start to move my hand down her body."
"พอสูดหายใจลึก ๆ อยู่สองสามครั้งก็เหมือนจะตั้งสติได้แล้ว ฉันเลื่อนมือไปตามร่างกายของเธอด้วยสัมผัสอันแผ่วเบา\nดุจขนนก"

# "…and I can feel myself losing focus again, thanks to those thin silken pajamas of hers resting so perfectly over the curves of her body."
"…และสมาธิฉันก็กระเจิงอีกครั้งเมื่อแตะมาถึงชุดนอนที่รับกับส่วนโค้งเว้าของร่างกายเธอเป็นอย่างดี"

# "If she's like this, then that means she has to be sitting against her bed and facing me. Now, to continue."
"ถ้าอยู่ท่านี้ แปลว่าลิลลี่กำลังนั่งบนเตียงหันหน้ามาทางฉันอยู่ เอาละ ทีนี้ก็ไปต่อ"

# "…All right, this must be her hip. If I just move slowly downwards…"
"…โอเค ตรงนี้ต้องเป็นเอวแน่ ๆ ถ้าเลื่อนลงมาช้า ๆ …"

label th_L26h:

# "Lilly's breath catches as my hand comes over hers, tentatively following her fingers between her legs and losing them as they go underneath her underwear."
"ลิลลี่สะดุ้งเฮือกเมื่อมือฉันเข้ามาทาบทับมือเธอ ฉันขยับมือไปตามนิ้วลิลลี่ด้วยความอึกอักไปที่หว่างขา เธอผละมือออก\nเมื่อฉันเริ่มสอดมือเข้าไปใต้กางเกงในของเธอ"

# "Just the slightest moisture touches my fingertips, but it's enough to easily work out what she's doing."
"ความชื้นแฉะน้อยนิดถูกกับปลายนิ้วของฉัน แต่เพียงเท่านั้นฉันก็รับรู้ได้ว่าเธอทำอะไรอยู่"

# "My mind suddenly fills with visions of what she must be like in front of me right now. I'd never even imagined her doing this before, and being unable to see her doing the act only enhances the mood."
"ภาพจินตนาการถึงสภาพของลิลลี่ที่อยู่ตรงหน้าปรากฏขึ้นในความคิดทันที ฉันไม่เคยนึกภาพลิลลี่ตอนทำอย่างนี้\nด้วยซ้ำ และการที่มองไม่เห็นก็ยิ่งเร้าอารมณ์ฉันขึ้นไปอีก"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

scene bg school_dormlilly
with softwipeup

# "I work the blindfold upwards, brushing out of my eyes a couple of hairs that were stuck to the ribbon before."
"ฉันถกผ้าปิดตาขึ้นแล้วปัด ๆ เส้นผมที่ติดอยู่กับตาซึ่งก่อนหน้านี้ติดมากับผ้า"

# "For a period of time I can only guess at, my mind goes completely blank. All I can do is stare as my newly-freed eyes take in everything in front of them."
"สมองฉันว่างเปล่าไปนานเท่าไหร่ไม่อาจทราบได้แน่ชัด ฉันได้แต่จ้องมองภาพตรงหน้าด้วยตาที่ถูกปลดพันธนาการออก\nมาหมาด ๆ"

scene evh lilly_masturbate:
    truecenter
    subpixel True zoom 1.1
    acdc_warp 10.0 zoom 1.0
with flash

# "Just as I'd worked out, Lilly sits in front of me."
"ลิลลี่นั่งอยู่ตรงหน้าอย่างที่ฉันคิดเอาไว้"

# "With one hand on the ground to steady herself, and the other's fingers lightly brushing between her legs, hidden by her dark blue underwear, I think it's the most erotic sight I've ever seen."
"เธอนั่งใช้มือข้างหนึ่งยันตัวเองไว้ ส่วนนิ้วของมืออีกข้างนั้นไล้อยู่ตรงหว่างขาของเธอที่ถูกปกปิดด้วยชั้นในสีน้ำเงินเข้ม\nภาพตรงหน้าตอนนี้คงเป็นภาพที่ยั่วเย้าที่สุดเท่าที่ฉันเคยเห็นมาเลย"

# "Once again I reach out and brush her hair from her face, her chin tilting outwards as she fills her pleasure-wrapped body with another breath of air."
"ฉันยื่นมือไปปัดผมที่ระหน้าลิลลี่อยู่อีกครั้ง เธอยื่นคางออกมาสูดลมหายใจเข้าไปยังข้างในร่างกายเธอที่อาบไล้ด้วย\nความรู้สึกดี"

# hi "Lilly…"
hi "ลิลลี่…"

# "Lilly looks oddly cute as she smiles at my calling of her name. It always seems like it's at the moments when she's least attentive that she lets her most interesting emotions slip out."
"พอยิ้มที่ฉันเรียกชื่ออย่างนี้แล้วก็ดูน่ารักพิกล ดูเหมือนว่าเธอจะปล่อยให้อารมณ์ของเธอที่ดูน่าสนใจที่สุดหลุดออกมา\nทุกครั้งที่เธอไม่ได้จดจ่อกับอะไร"

# "It's not long before she works her fingers over herself faster than before, her excitement evidently rising, the scent of her sweat in the air only echoing that fact."
"ไม่นานลิลลี่ก็เร่งนิ้วตัวเอง ความรู้สึกของเธอเพิ่มมากขึ้นเรื่อย ๆ กลิ่นเหงื่อของเธอที่อวลอยู่ยิ่งย้ำชัด"

# "I sit in front of her. It's hardly as if my own arousal's holding still; it's taking every fiber of my being to let her continue by herself instead of pushing myself on top of her."
"ฉันนั่งมองเธอและกดความตื่นตัวของตัวเองไว้ห้ามใจอย่างหนักไม่ให้จู่โจมเธอแล้วปล่อยให้เธอทำด้วยตัวเอง"

scene evh lilly_masturbate_come_face
with flash

# "It's strange… I'd initially found her clouded blue eyes to be distracting, almost disturbing in their lack of focus. That bothers me far less than it used to, now."
"แปลก… ฉันเคยคิดว่าตาขุ่น ๆ ของลิลลี่นั้นเป็นตัวดึงสมาธิ บางทีก็ชวนให้รู้สึกอึดอัดเพราะเป็นตาที่ไม่ได้มองอะไรอยู่\nแต่ตอนนี้เรื่องนั้นไม่ได้มากวนใจฉันมากเหมือนเมื่อก่อนแล้ว"

# "My attention refocuses on her as she lets out a whimper, her breath coming much faster than before and her hips subtly rocking."
"ฉันกลับมาสนใจลิลลี่อีกครั้งเมื่อเธอครางออกมา เธอขยับเอวเบา ๆ พร้อมลมหายใจที่หอบกระชั้นกว่าเมื่อครู่"

scene evh lilly_masturbate_come
with flash

# "No sooner do I realize how close to the edge Lilly's become, that her breath catches. Her eyes clasp shut as every muscle in her body seems to contract, and she unmistakably reaches her climax."
"ไม่นานฉันก็เห็นว่าลิลลี่เข้าใกล้มากแล้ว และเธอก็สะอึกไปแล้วหลับตาแน่นทั้งตัวหดเกร็งชัดว่าเธอไปถึงฝั่งแล้ว"

# "For only a scant few seconds she tightens, huddled in ecstasy before her body relaxes and a long, drained sigh comes from her lips."
"ตัวของลิลลี่เกร็งอยู่ด้วยความรู้สึกอันวามไหวได้ชั่วขณะ จากนั้นเธอจึงคลายตัวพ่นลมหายใจยาวจากริมฝีปากเธอ"

scene bg school_dormlilly
with locationchange

# "I… just have no idea what to say. Silence reigns while I simply watch her, hair hanging over her face as she sits exhausted."
"ฉัน… ไม่รู้จะพูดอะไรดี ฉันได้แต่มองลิลลี่ที่นั่งอยู่ด้วยความเหนื่อยอ่อนปล่อยให้ผมปรกหน้าอยู่เงียบ ๆ"

show lilly basic_emb_paj_close:
    center
    ypos 1.1
with charaenter

# li "Hisao…"
li "ฮิซาโอะ…"

# "When she reaches out to brush my face, my urges take complete control of my body. Without so much as a second thought, I push myself over her frame."
"พอลิลลี่ยื่นมือมาแตะหน้าฉัน ความอยากก็เข้าครอบงำร่างกายของฉัน ฉันผลักตัวลิลลี่ขึ้นคร่อมเธอโดยไม่คิดอะไร\nทั้งสิ้น"

# "It's an unusual feeling, being like this. I feel oddly powerful, holding myself above her blank face. As though, for the first time since the accident so long ago, I feel physically strong."
"พออยู่อย่างนี้แล้วก็รู้สึกประหลาดดี เมื่อได้อยู่เหนือใบหน้าเรียบนิ่งของลิลลี่แล้วฉันก็รู้สึกมีพลังขึ้นมาพิลึก ราวกับว่า\nเป็นครั้งแรกที่รู้สึกแข็งแกร่งขนาดนี้นับตั้งแต่อุบัติเหตุครั้งนั้นเมื่อนานมาแล้ว"

# hi "Lilly… I want you."
hi "ลิลลี่… ฉันต้องการเธอ"

show lilly basic_weaksmile_paj_close
with charachange

# "To my surprise, she smiles weakly before reaching upwards to feel the side of my face. It's an almost cheeky expression, of the kind which she usually gives only after getting something out of me."
"ลิลลี่ยิ้มบาง ๆ แล้วยื่นมือมาจับแก้ม ซึ่งผิดจากที่ฉันคาดไว้ เธอทำสีหน้าซุกซนเหมือนเวลาที่คาดเค้นเอาอะไรบางอย่าง\nจากฉันได้"

# hi "You… wanted me to do this?"
hi "เธอ… อยากให้ฉันทำแบบนี้เหรอ"

show lilly basic_smileclosed_paj_close
with charachange

# "She holds her smile and gives a silent nod. I guess it was an effective way to make me take the initiative for once."
"เธอยังคงยิ้มแล้วพยักหน้าเงียบ ๆ คงเป็นวิธีของเธอที่ทำให้ฉันได้เป็นฝ่ายนำละมั้ง ซึ่งได้ผลดีด้วย"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene black
with softwipedown

# "And, again to my surprise, she gives the ribbon still around my head a sharp tug downwards. Once again, I'm lost in complete blackness."
"และฉันต้องแปลกใจอีกครั้งเมื่อลิลลี่จับแถบผ้าคาดผมที่คาดหัวฉันอยู่ลงมาปิดตา ฉันถูกทิ้งให้อยู่ในความมืดมิดอีกครั้ง"

# li "I told you… to keep it on… didn't I?"
li "ฉันบอกให้… ปิดไว้… ไม่ใช่เหรอ"

# "That teasing edge to Lilly's voice, punctuated by her breathing… she never seems to lose her ability to take control of a situation."
"ลิลลี่ทำน้ำเสียงหยอกล้อซึ่งมาพร้อมกับคำพูดที่แทรกด้วยจังหวะหายใจ… ไม่ว่าจะสถานการณ์ไหน ๆ เธอก็เอาอยู่จริง ๆ"

# "But this time… this one time…"
"แต่คราวนี้… แค่คราวนี้แหละ…"

# li "Ah, Hisao!? What are you—?"
li "อ๊ะ ฮิซาโอะ!? นี่เธอ—?"

# "I slide my hands underneath her, soft silk and skin pressing into my hands as I gently raise her body, with a measure of difficulty."
"ฉันเลื่อนมือไปสอดตัวเธอไว้ น้ำหนักของเธอกดทับผิวและผ้าไหมอ่อนนุ่มกับมือและแขนฉัน ตัวเธอนั้นยกลำบาก\nพอสมควร"

# "While I wouldn't describe her as heavy… her height makes her more than a handful to try and lift."
"แม้ลิลลี่จะไม่ได้หนักมาก… แต่ส่วนสูงของเธอนั้นทำให้ยกตัวเธอได้ลำบาก"

# "It only takes a couple of carefully placed steps to feel the edge of her bed against my legs, my lowering of Lilly onto her sheets just as gentle as when I raised her."
"เมื่อค่อย ๆ เดินมาได้สองสามก้าวเท้าฉันก็แตะเข้ากับขอบเตียงของลิลลี่ ฉันวางตัวลิลลี่ลงนอนกับเตียงอย่างเบามือ\nเช่นเดียวกันกับตอนที่ฉันยกตัวเธอมา"

#"The game earlier came in handy; without it, I wouldn't have remembered how many steps it was to Lilly's bed, and in what direction."

# hi "Your bed will be more comfortable than the floor, right?"
hi "เตียงน่าจะสบายกว่าพื้นนะ"

# li "Always the gentleman, aren't you?"
li "เป็นสุภาพบุรุษเสมอเลยนะ"

# "I quickly run my hands down Lilly's long, shapely legs, their allure far from diminished without the luxury of sight, and pull off her pajama shorts and underwear from her ankle."
"ฉันรีบเลื่อนมือไปตามขายาวได้รูปของลิลลี่ แม้จะไม่มีตาให้ได้เชยชม แต่เสน่ห์ของขาคู่นั้นก็ไม่ได้ลดลงไปแม้แต่น้อย\nจากนั้นฉันก็ถกกางเกงขาสั้นและชั้นในที่อยู่ตรงข้อเท้าลิลลี่ออก"

# "I have no idea where those just went…"
"ฉันไม่รู้ว่าเมื่อกี้ฉันโยนไปทางไหน…"

# "Well, I guess it doesn't matter. They'll be somewhere around."
"แต่ก็คงไม่สำคัญ น่าจะอยู่แถวนี้แหละ"

# "With a minimum of fuss, I shuffle down my own pajama trousers and underwear, positioning myself between her legs. Or at least, where I think is between her legs."
"ฉันถอดกางเกงและชั้นในของตัวเองออกอย่างง่ายดาย ก่อนจะขยับตัวเข้าไปอยู่ตรงระหว่างขาสองข้างของเธอ ซึ่งฉัน\nก็คิดว่าน่าจะเป็นตรงนี้แหละ"

# "With one hand on her bed to steady myself, my right moves tentatively downwards."
"ฉันใช้มือข้างซ้ายยันตัวเองไว้กับเตียงแล้วใช้มืออีกข้างยื่นไปด้วยความลังเล"

# "Uh, whoops. My first contact with her is my palm clumsily meeting the front of her nose."
"โอ๊ะ ตายละ ดันไปแตะเข้ากับจมูกลิลลี่แบบเก้ ๆ กัง ๆ เสียได้"

# "She giggles a little before turning her head sideways. Taking my cue, I gently cradle her cheek and use my thumb to feel the contours of her face as she so often does with me."
"ลิลลี่หัวเราะคิกคักแล้วเบือนหน้าออก ฉันจับแก้มเธอไว้เบามืออย่างรู้งานแล้วไล้นิ้วโป้งไปตามรอยโค้งเว้าบนใบหน้า\nอย่างที่เธอทำกับฉันเป็นประจำ"

# "This would be a lot easier if she wasn't moving her face into my hand, but the feeling of her nuzzling into it is nice."
"ถ้าลิลลี่ตั้งหน้าตรงมาน่าจะจับได้ง่ายหน่อย แต่สัมผัสจากการที่เธอเอาแก้มมาแนบมือฉันก็ชวนให้รู้สึกดีเหมือนกัน"

# "I swallow to try and steady myself, take my other hand from the bed and use it to guide myself into her."
"ฉันกลืนน้ำลายแล้วจัดแจงท่าตัวเองก่อนจะใช้มือข้างที่ยันตัวเองไว้มานำทางตัวเองเข้าไปในตัวเธอ"

# "As soon as I feel her warmth around me, I quickly realize just how turned on I am."
"ทันทีที่ความอบอุ่นจากเธอโอบอุ้มฉันไว้ก็ถึงรู้ตัวว่าฉันตื่นตัวเพียงใด"

# "With my sight gone I'm free to concentrate far more on my other senses, including tactile feeling. The entire experience feels more vivid, more intense than it's been before."
"เมื่อมองไม่เห็นแล้วฉันก็จดจ่อกับประสาทสัมผัสส่วนอื่น—รวมถึงผิวสัมผัส—ได้มากขึ้น เป็นความรู้สึกที่จัดจ้านชัดเจน\nกว่าทุกครั้งที่เคยรู้สึกมา"

# "I slowly start to move my hips back and forth, my heart beating wildly in excitement."
"ฉันขยับเอวเข้าออกช้า ๆ หัวใจเต้นรัวด้วยความตื่นเต้น"

# "I feel Lilly's eyes clenching shut, the movement of her cheek under my thumb reminding me of the gentle hold I have on the side of her face."
"ฉันสัมผัสได้ว่าลิลลี่หลับตาแน่นอยู่ แก้มของเธอที่ขยับถูกกับนิ้วโป้งของฉัน ซึ่งทำให้รู้ตัวว่าฉันยังจับแก้มเธอไว้อยู่"

# "It's hard to stop myself from being completely overwhelmed. It's hard to think that this is what sex is usually like for her, experienced through every sense but the one I hold dearest."
"ความรู้สึกเหล่านี้เป็นความรู้สึกอันมากล้นที่ฉันแทบรับไม่ไหว พอคิดว่าเธอจะต้องรับรู้ถึงสิ่งนี้ผ่านทุกประสาทสัมผัส\n—เว้นเสียก็แต่การมองเห็นซึ่งฉันให้ค่าสูงสุด—ทุกครั้งที่เราทำด้วยกันแล้วฉันก็รู้สึกทึ่งเหลือเกิน"

# "From her cheek to her neck, I begin to slide my hand downwards to take in the feeling of her body."
"ฉันเลื่อนมือที่อยู่ตรงแก้มเธอลงมาที่คอ ก่อนจะลงไปอีกเพื่อสัมผัสกับร่างกายของเธอ"

# "The contours of her collarbone… the light dew resting on her skin…"
"รอยนูนจากกระดูกไหปลาร้า… หยาดน้ำที่เกาะอยู่บนผิวของเธอ…"

# "My sense of smell is stimulated by the scent of her sweat and mine hanging in the air. Even the ambient smell, noticeably different from that of my own room, adds to the feeling."
"ประสาทสัมผัสทางจมูกของฉันรับรู้ถึงกลิ่นเหงื่อของเธอและฉันซึ่งอวลอยู่ในอากาศ เสริมด้วยกลิ่นอากาศภายในห้อง\nซึ่งรับรู้ได้ว่าต่างไปจากกลิ่นห้องฉัน"

# "When I move my hand to her supple breast, her soft mewling fills my ears, along with the sound of our act."
"ฉันเลื่อนมือมาจับที่อกอิ่มของเธอ เสียงครางของลิลลี่ดังระคนกับเสียงเนื้อที่กระทบกัน"

# "The skin under my hand moves back and forth with each thrust, my grip on it tightening as my lust for the near-naked body of Lilly before me grows."
"ร่างกายซึ่งฉันสัมผัสอยู่นั้นขยับตามแรงกระแทก ฉันออกแรงบีบหนักขึ้นเมื่อความใคร่ต่อร่างกายที่เปลือยครึ่งล่าง\nของเธอนั้นมีมากขึ้น"

# "I can even feel her small nipple against my palm. My hand slides further and my fingers pluck it through the thin silk of her pajama top."
"ฝ่ามือฉันสัมผัสเข้ากับหัวนมเล็ก ๆ ของเธอ ฉันเลื่อนมือลงต่ำอีกเพื่อใช้นิ้วมาจับแล้วออกแรงดึงผ่านชุดนอนผ้าไหม\nบาง ๆ นั้น"

# "Her whimpering sounds turn to moans as she fills with the same pleasure as I.
# I can feel my heart beating loudly in my chest, and her own beating underneath my hand."
"ลิลลี่เริ่มร้องครางดังขึ้นด้วยความรู้สึกดีเช่นเดียวกับฉัน หัวใจฉันเต้นเสียงดังอยู่ในอก และสัมผัสจากหัวใจเธอที่เต้นอยู่\nก็ส่งผ่านมือของฉันมา"

# "I can feel her hands clasp my wrists, their grip surprisingly tight as her chest rises in overwhelming pleasure."
"ลิลลี่กำข้อมือฉันแน่นเหลือเชื่อ เธอยืดอกขึ้นด้วยความรู้สึกดีที่มากล้นเกินรับไหว"

label th_L26x:

scene black
with dissolve

# "More… I want more…"
"ขออีก… ขออีก…"

window hide

play sound sfx_heartslow
show heartattack alpha 
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.7)

window show

# "I can feel my chest tightening as I rock back and forth frantically, both of us entirely taken with ourselves."
"ยิ่งฉันขยับเข้าออกแรง ๆ ก็ยิ่งรู้สึกได้ถึงหน้าอกที่แน่นขึ้นมา เราทั้งสองคนต่างจมอยู่กับอารมณ์ตัวเอง"

$ renpy.music.set_volume(0.4, 0.5, channel="music")

window hide

play sound sfx_heartslow
show heartattack alpha 
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.7)

window show

# "Nothing… that unusual… I just need to take deeper breaths to steady… myself…"
"ไม่แปลก… ขนาดนั้น… แค่หายใจลึก ๆ … ตั้งสติ…"

$ renpy.music.set_volume(0.3, 0.5, channel="music")

window hide

play sound sfx_heartslow
show heartattack alpha 
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.7)

with Pause(0.7)

play sound sfx_heartfast
show heartattack alpha 
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

window show

# "This feeling is just… normal…"
"ความรู้สึกนี้… ไม่ได้แปลกเลย…"

$ renpy.music.set_volume(0.2, 0.5, channel="music")

window hide

play sound sfx_heartfast
show heartattack alpha 
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

with Pause(0.7)

play sound sfx_heartfast
show heartattack alpha 
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

window show

# hi "Aah… aaaaaaaah…"
hi "โอยย… โอยยยยยยยย…"

window hide

play sound sfx_heartfast
show heartattack alpha 
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

with Pause(0.7)

play sound sfx_heartfast
show heartattack alpha 
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

window show

# "This isn't… I can't… this pain is too much…!"
"ไม่ใช่… ไม่ไหว… ปวดเกินไปแล้ว…!"

window hide

play sound sfx_heartstop
show heartattack alpha 
with Dissolve (0.1)

stop music fadeout 0.3

show heartattack residual
with Dissolve (0.8)

window show

# hi "AAAAARGH!"
hi "ว้าาาาาก!!"

with vpunch

# "I stumble backwards from Lilly with unseemly haste, clumsily hitting the back of my foot against the table and falling to the ground with an unceremonious crash."
"ฉันผละตัวออกจากลิลลี่ด้วยความรีบผิดวิสัยจนเผลอเอาหลังเท้ากระแทกเข้ากับโต๊ะแล้วล้มลงกับพื้นอย่างกะทันหัน"

# "Breathing wildly, I frantically scrape at the ribbon over my eyes as I lay on my back. I have to get this off, I have to get this off…"
"ฉันนอนหงายหอบหนักพลางเอาผ้าคาดตาออก ต้องรีบเอาออก ต้องรีบเอาออก…"

scene white
with softwipeup

scene bg misc_ceiling
show heartattack residual
with locationchange

# "For a moment, everything goes blank. As the rush of newfound light assaults my eyes, my breathing slows from the brink of hyperventilation."
"ภาพตรงหน้าขาวโพลนไปชั่วขณะ แสงส่องเข้ามาแยงตาหลังเอาผ้าคาดตาออก จังหวะหายใจของฉันเริ่มช้าลงจาก\nเมื่อครู่ที่หอบจนคล้ายหายใจเกิน"

window hide

$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_tragic fadein 4.0

hide heartattack
with Dissolve(3.0)

window show

# "Seconds pass, and I carefully measure out the rhythm of my heartbeats with every ounce of concentration I can muster."
"ผ่านไปอีกครู่หนึ่งฉันจึงคอยรวมรวมสมาธิเท่าทีมีอยู่มาจดจ่อกับจังหวะการเต้นของหัวใจฉัน"

# "My heart is… normal. It's back to normal."
"หัวใจฉัน… ปกติแล้ว กลับมาเป็นปกติแล้ว"

# "My body feels utterly bizarre as I lay dazed on the floor looking at the ceiling. The adrenaline from before is still pouring through my veins, but my mind is completely exhausted."
"ฉันนอนเหม่อมองเพดานด้วยความรู้สึกสุดวิปลาส อะดรีนาลินส่วนเมื่อครู่ยังคงไหลเวียนอยู่ในกระแสเลือด แต่สมอง\nนั้นหมดแรงสิ้นแล้ว"

# "I prop myself up as I hear Lilly getting off the bed and coming towards me."
"ฉันผลุงตัวลุกขึ้นนั่งเมื่อได้ยินเสียงลิลลี่ลงจากเตียงเดินมาหาฉัน"

show bg misc_ceiling_blur as bg2:
    center
    alpha 0.0
    linear 1.0 alpha 1.0
show lilly superclose_shock:
    xalign 0.5 yanchor 0.5 ypos 0.15 alpha 0.0
    subpixel True rotate 180
    easein 1.0 alpha 1.0 ypos 0.3
with Pause(1.0)

# li "Hisao? Are you okay? Hisao!?"
li "ฮิซาโอะ? เป็นอะไรหรือเปล่า ฮิซาโอะ!?"

# hi "I'm fine, Lilly. I'm… fine."
hi "ไม่เป็นไร ลิลลี่ ไม่… เป็นไร"

show lilly superclose:
    xalign 0.5 yanchor 0.5 ypos 0.3 alpha 1.0
    subpixel True rotate 180
with charachange

# "She gives a sigh of relief, her worried expression collapsing."
"ลิลลี่ถอนหายใจโล่งอกคลายสีหน้ากังวล"

# "Her face afterward is the very last I'd ever wanted to see from her. It's a face I'd detested when I first saw my parents in the hospital all those months ago."
"แต่สีหน้าของเธอหลังจากนั้นเป็นสีหน้าที่ฉันไม่อยากเห็นเลย เป็นสีหน้าที่ฉันเกลียดมาตั้งแต่ตอนที่ฉันได้เห็นหน้า\nพ่อแม่เป็นครั้งแรกหลังจากเข้าโรงพยาบาลเมื่อหลายเดือนที่แล้ว"

# "Pity. Lilly… pities me."
"สงสาร ลิลลี่… สงสารฉัน"

scene black
with shuteye

# "I just close my eyes and turn away, powerless. I feel like throwing up."
"ฉันหลับตาแล้วเบือนหน้าหนีด้วยความรู้สึกแย่ที่ทำอะไรไม่ได้ เหมือนจะคลื่นไส้ขึ้นมาเลย"

play sound sfx_rustling

# "I can hear the sound of Lilly moving away and quickly attending to herself, the ruffling of her clothing being pulled back on after a moment of searching just barely audible."
"ฉันได้ยินเสียงลิลลี่ที่เดินไปใส่เสื้อผ้า แต่แทบไม่ได้ยินเสียงตอนเธอใส่เสื้อผ้าหลังจากที่เธอหาชุดอยู่พักหนึ่ง"

# hi "Sorry…"
hi "ขอโทษนะ…"

scene bg school_dormlilly
show lilly basic_concerned_paj at center
with openeye

# "She slowly shakes her head as she finishes buttoning up her top. Her kind smile looks so fragile, so delicate, that it makes my heart sink."
"ลิลลี่สั่นหัวช้า ๆ พลางติดกระดุมเม็ดสุดท้าย รอยยิ้มอบอุ่นของเธอนั้นแสนเปราะบาง บอบบางเสียจนฉันเห็นแล้ว\nปวดใจ"

show lilly basic_concerned_paj_close
with characlose

show lilly basic_concerned_paj_close:
    ypos 1.1
with charamove

# "Approaching carefully, she feels out the edge of the low table before taking a seat next to me, putting her arms around my chest."
"ลิลลี่เดินมาช้า ๆ ก่อนจะจับขอบโต๊ะเตี้ยมานั่งข้าง ๆ แล้วโอบแขนเข้ากับหน้าอกของฉัน"

# li "I'm sorry, Hisao. I shouldn't have pushed my desires onto you."
li "ขอโทษนะฮิซาโอะ ฉันไม่น่าไปฝืนเธออย่างนั้นเลย"

# hi "You don't need to apologize. I'd normally be fine, you've seen that much before."
hi "ไม่ต้องขอโทษหรอกน่า เธอก็เห็นแล้วนี่ว่าปกติฉันก็ไม่ได้เป็นอะไร"

# hi "I guess I shouldn't have tried to push myself so far."
hi "ฉันเองแหละที่น่าจะฝืนตัวเองเกินไป"

# "My eyelids feel heavy. Calmly sitting next to her like this is probably letting the adrenaline work itself out of my system, and letting my mind relax."
"เปลือกตาของฉันหนักอึ้ง การได้นั่งอยู่ข้างลิลลี่เฉย ๆ อย่างนี้ก็คงนับได้ว่าเป็นการปล่อยให้อะดรีนาลินในร่างกายฉัน\nซาลง และอาจเป็นการสงบใจตัวเองได้ด้วย"

show lilly basic_oops_paj_close
with charachange

# li "So that's… why you never took the lead…?"
li "เพราะแบบนี้หรือเปล่า… เธอถึงได้ไม่เคยเป็นฝ่ายนำเลย…"

# hi "Yeah. I guess it's a good thing you like to, huh?"
hi "อื้ม ก็ถือว่าโชคดีไปแหละที่เธอชอบนำด้วย เนอะ"

show lilly basic_weaksmile_paj_close
with charachange

# "The joke seems to lighten her expression a little, a fact which helps let me feel less unease about my unreliable self."
"เหมือนว่าที่พูดติดตลกไปอย่างนั้นจะทำให้ลิลลี่หายหมองลงไปได้บ้าง ซึ่งพอได้รู้อย่างนี้แล้วก็ค่อยสบายใจกับตัวฉัน\nซึ่งพึ่งพาไม่ได้ขึ้นมา"

# "Lilly's head comes to rest on my shoulder as I struggle to keep my eyes open, with more difficulty after each blink. I feel completely drained."
"ลิลลี่เอาหัวมาหนุนไหล่ฉันที่ตาแทบจะปิดอยู่แล้ว ยิ่งกะพริบตาหลายครั้งเข้าตาก็แทบไม่เปิด เรี่ยวแรงของฉันไม่เหลือ\nอยู่เลย"

# li "It's okay, Hisao. It's all okay."
li "ไม่เป็นไรนะฮิซาโอะ ไม่เป็นไรเลย"

stop music fadeout 5.0

# "No sooner does she say this than a small, quiet tune escapes her lips. Entirely too tired to think, all I can do is listen to her soft humming."
"พอลิลลี่พูดจบเธอก็ฮัมเพลงเสียงแผ่วเบา ฉันไม่มีแรงแม้แต่จะนึกถึงอะไรแล้วจึงได้แต่คอยฟังเธอฮัมเพลง"

# "It's a soft, almost melancholic tune. It sounds familiar, but the more I try to remember its origin the less I seem able to concentrate."
"เป็นท่วงทำนองอ่อนหวานคลับคล้ายหม่นหมอง เป็นเสียงที่ฟังดูคุ้นหู แต่ยิ่งคิดว่าเคยได้ยินที่ไหนก็ยิ่งเหมือนจะสมาธิ\nหลุดไปเท่านั้น"

# "The feeling and scent of her head gently resting on my shoulder and her warm body against my side are soothing. The soft humming of her voice, too, relaxes my mind as much as her warmth relaxes my muscles."
"ทั้งสัมผัสกับกลิ่นจากศีรษะของเธอที่อิงไหล่ฉัน ทั้งสัมผัสจากร่างกายเธอที่แนบฉันนั้นต่างชวนให้ผ่อนคลาย เสียง\nอันอ่อนหวานของเธอเองก็ช่วยผ่อนคลายจิตใจได้ไม่ต่างอะไรกับการที่ความอบอุ่นของเธอช่วยผ่อนคลายกายฉัน"

# "This singular, quiet moment… after all this fracas, it makes me realize just how exhausted I've become. I can feel my eyelids slowly becoming heavier and heavier."
"ช่วงเวลาอันเงียบงันหนึ่งนี้… หลังจากที่ผ่านความปั่นป่วนทั้งหลายมา ทำให้รู้ตัวว่าฉันเหนื่อยอ่อนเพียงใด เปลือกตา\nของฉันเริ่มหนักขึ้นเรื่อย ๆ"

# "Even with the chaos of before, I wish this moment would last forever."
"แม้ก่อนหน้านี้จะมีเรื่องวุ่นวาย แต่ฉันก็อยากให้ช่วงเวลานี้คงอยู่ตราบชั่วนิรันดร์"

# "Lilly and I together, sharing a single, solitary occasion together, just as we used to."
"ลิลลี่กับฉันอยู่ด้วยกัน ใช้เวลาอันสันโดษซึ่งมีบางครั้งด้วยกันอย่างที่ทำประจำ"

# "But if that's the case… why does she feel… further away than she's ever felt before?"
"แต่ถ้าอย่างนั้น… ทำไมถึงได้รู้สึกว่าลิลลี่… อยู่ห่างไปจากฉันกว่าทุกทีกัน"

scene black
with dissolve

#****************



label th_L27:

scene bg school_library
with locationchange

play sound sfx_doorslam
play music music_happiness fadein 2.0

# "The loud clatter of books falling into the return slot abruptly breaks the grip of silence over the school library."
"เสียงหนังสือซึ่งหล่นลงจากช่องคืนหนังสือดังก้องทำลายความเงียบซึ่งยึดพื้นที่ในห้องสมุดโรงเรียนแห่งนี้ไว้"

# "It's become a habit for me to come to the library at least once a week. Not only does the reading itself keep me busy, but discussing books with Hanako and Lilly also does."
"ฉันมาห้องสมุดสัปดาห์ละครั้งจนติดเป็นนิสัยไปแล้ว ฉันใช้เวลาไปทั้งกับการอ่านและพูดคุยเรื่องหนังสือกับลิลลี่กับ\nฮานาโกะ"

show yuuko panic_up at center
with charaenter

# "Obviously startled, Yuuko suddenly twists towards the direction of the noise. I'd have thought her used to people dropping books by now, since she does work here."
"ยูโกะหันมาทางต้นเสียงนั้นทันทีด้วยความตกใจ ก็นึกว่าทำงานอยู่ที่นี่จนชินกับเสียงคนเอาหนังสือมาคืนแล้วเสียอีก"

show yuuko neutral_down
with charachange

# yu "Oh, hello Hisao. Back again?"
yu "อ้าว สวัสดีฮิซาโอะ มาอีกแล้วเหรอ"

# "It takes me a moment to respond, my mind still distracted by the familiar melody of Lilly's humming that's hardly left my ears in the several days it's been since I fell asleep to it."
"ฉันนิ่งไปพักหนึ่งก่อนตอบเพราะยังมัวแต่นึกถึงท่วงทำนองติดหูอันคุ้นเคยจากครั้งที่ลิลลี่ฮัมให้ฟังจนฉันหลับไปเมื่อ\nหลายวันที่แล้ว"

# hi "Hmm? Oh, yeah. Just returning some books I borrowed."
hi "หือ อ้อ ครับ พอดีเอาหนังสือที่ยืมมาคืนน่ะ"

# "She casts her eyes downwards, presumably to the bin the books dropped into."
"ยูโกะก้มมองบางอย่าง ซึ่งน่าจะมองกล่องที่หนังสือหล่นไปนั่นแหละ"

show yuuko closedhappy_down
with charachange

# yu "You're a very heavy reader, aren't you?"
yu "อ่านเยอะน่าดูเลยนะ"

# hi "It's become a bit of a routine now. Passes the time, at least."
hi "เดี๋ยวนี้อ่านจนเป็นกิจวัตรไปแล้วน่ะครับ อย่างน้อยก็ช่วยฆ่าเวลาได้"

show yuuko worried_up
with charachange

# yu "I wish I had free time to pass…"
yu "อยากมีเวลาว่างให้ฆ่าบ้างจังเลยนะ…"

# "From smalltalk to depression in less than five seconds. I think that's a new record for her. She seems a bit down in general today, even compared to normal."
"จากคุยเรื่อยเปื่อยเป็นความเครียดได้ในเวลาไม่ถึงห้าวินาที รอบนี้น่าจะเป็นสถิติใหม่เลย แต่วันนี้ยูโกะก็ดูหมองกว่าทุกที\nผิดวิสัยด้วย"

# "Considering she has to work two jobs just to support herself, I could see how that would take a toll on her lifestyle."
"เธอเองก็ทำงานสองที่เพื่อหาเงินให้ตัวเอง การใช้ชีวิตของเธอก็คงเสียไปตาม ๆ กันนั่นแหละ"

# "Come to think of it, the pay for her job here can't be all that bad. The idea of staff in such a prestigious private school going hungry strikes me as counterintuitive."
"จะว่าไปแล้ว เงินเดือนที่นี่ก็น่าจะไม่ได้น้อยขนาดนั้นมั้ง โรงเรียนเอกชนระดับสูงขนาดนี้คงไม่น่าหน้าเลือดขนาดนั้น"

# hi "Working two jobs must take a lot of time. I'd probably never manage it."
hi "ทำงานสองที่นี่คงกินเวลาเยอะน่าดูเลยนะครับ เป็นผมคงไม่ไหว"

show yuuko neutral_up
with charachange

# yu "You're lucky, being a student. Do you think you'll be able to go to university?"
yu "เธอยังโชคดีนะที่เป็นนักเรียน แล้วนี่กะจะเรียนต่อมหาวิทยาลัยหรือเปล่า"

# "If she's asking, then I guess that's the expected result of having this kind of education. Private schools like this don't exactly come cheap."
"ถ้าถามแบบนี้ก็แปลว่าการเรียนต่อเป็นเรื่องปกติของการมาเรียนเส้นทางนี้ โรงเรียนเอกชนแบบนี้ค่าใช้จ่ายก็ใช่ว่า\nจะถูก ๆ"

# hi "I… guess. I have the money, I think."
hi "ก็… น่าจะนะครับ คิดว่าเงินน่าจะพออยู่"

# hi "I've got plans which will require going to one, and my grades are good enough. It's more a matter of how I'll pay to do so."
hi "ผมวางแผนที่ที่จะไปไว้แล้ว ผลการเรียนผมก็ดีใช้ได้ด้วย ที่เหลือก็อยู่ที่ว่าผมจะเอาเงินไปใช้ยังไงมากกว่า"

show yuuko worried_down
with charachange

# yu "University costs so much that I'm having to work two jobs to afford to enter it… paying for daily expenses too makes it a lot harder."
yu "ค่าเทอมมหาวิทยาลัยน่ะแพงมากจนฉันต้องทำงานสองที่กว่าจะมีเงินพอจ่าย… แล้วไหนจะค่ากินค่าอยู่อีก"

show yuuko neutral_down
with charachange

# yu "If you're reading this much though, that means you're doing well in school, right?"
yu "แต่ถ้าอ่านเยอะแบบนี้ก็แปลว่าเธอเรียนเก่งสินะ"

# "Interesting logical jump. Not an altogether wrong one, though."
"โยงเหตุผลได้น่าสนใจดี แต่ก็ไม่ได้ผิดเสียทีเดียวน่ะนะ"

# hi "I suppose so. I didn't find any of the exams very hard, aside from maybe one or two."
hi "มั้งนะครับ ผมก็รู้สึกว่าข้อสอบไม่ได้ยากมาก ถ้าไม่นับวิชาสองวิชา"

# hi "Do you mind if I ask what studies you're pursuing in university?"
hi "ถามหน่อยได้มั้ยครับว่าคุณเรียนอะไรอยู่"

show yuuko happy_up
with charachange

# "Yuuko appears to genuinely brighten at the question."
"ยูโกะดูจะดีใจขึ้นมาจริง ๆ ที่มีคนถาม"

show yuuko closedhappy_up
with charachange

# yu "Anthropology. To be specific, I'm specializing in the history of classical era Athenian civilization and democracy."
yu "มานุษยวิทยาน่ะ แต่ที่ฉันเรียนแบบเจาะจงจริง ๆ คือประวัติศาสตร์อารยธรรมกับประชาธิปไตยของเอเธนส์\nยุคคลาสสิก"

# "She really seems to know her stuff. Such enthusiasm is to be admired, and it's nice to see her genuinely excited about something."
"ดูท่าจะเก่งเรื่องนี้น่าดู ฉันนึกชื่นชมที่ยูโกะกระตือรือร้นขนาดนี้ ได้เห็นเธอตื่นเต้นแบบจริงจังกับอะไรสักอย่างแบบนี้\nก็ดีเหมือนกัน"

# "I guess even somebody like Yuuko can be happy if she has a visible road ahead of her."
"ถ้ามีเส้นทางข้างหน้าที่ชัดเจนแล้ว แม้แต่คนอย่างยูโกะก็ยังมีความสุขได้สินะ"

# hi "That's good to hear. If you—{w=0.6}{nw}"
hi "ดีแล้วละครับ ถ้าคุณ—{w=0.6}{nw}"

stop music fadeout 0.5
play sound sfx_phone

show yuuko panic_up
with vpunch

# "Both of us jump at the sudden interruption coming from my pocket."
"เราทั้งคู่ต่างตกใจกับเสียงจากกระเป๋ากางเกงฉันที่ดังมาขัดจังหวะแบบกะทันหัน"

scene bg school_hallway3
with locationchange

# "Apologizing profusely and quickly shuffling into the hallway as I fumble with the cover of my mobile phone, I glance at the screen."
"ฉันขอโทษขอโพยแล้วรีบเดินฉับ ๆ ออกมาที่โถงทางเดินพลางจับเงอะ ๆ งะ ๆ อยู่กับฝาโทรศัพท์ก่อนจะเปิดออกมาดูจอ"

# "…Weird. It's a mobile number I don't recognize. Considering I can count the number of people with my number on one hand, I briefly wonder whether it's some telemarketer that lucked out."
"…แปลก เบอร์แปลกแฮะ คนที่รู้เบอร์โทร. ของฉันนั้นนับด้วยมือข้างเดียวก็หมดแล้ว ฉันนึกสงสัยอยู่ครู่หนึ่งว่าหรือจะ\nเป็นเบอร์ที่โทร. มาขายของซึ่งบังเอิญมาลงที่เบอร์ฉันพอดี"

scene bg school_hallway3_blurred
show phone mobile:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with locationchange
with Pause (0.5)

# hi "Hello, Hisao Nakai speaking."
hi "ฮัลโหลครับ ฮิซาโอะ นากาอิครับ"

# mystery "Geez, pick up faster next time. Anyway, guess who?"
mystery "ปัดโธ่ คราวหน้ารับสายให้มันเร็ว ๆ หน่อย เออ ทายซิใคร"

play music music_comedy fadein 1.0

# "It only takes me a second to recognize the distinctively deep, brusque voice."
"แวบเดียวฉันก็รู้ว่าเจ้าของเสียงทุ้มต่ำห้าว ๆ เป็นเอกลักษณ์นั้นคือใคร"

# hi "Hey, Misha. Didn't expect you to call me."
hi "อ้าวมิช่า ไม่นึกเลยนะว่าจะโทร. มาหาเนี่ย"

# aki "Huh!? Ya actually think I sound like her?"
aki "ฮะ!? นี่คิดว่าฉันเสียงเหมือนยัยนั่นจริงดิ"

# hi "Not at all, Akira. I don't remember giving you my number though, so I thought I'd mess with you."
hi "ไม่ได้คิดหรอกครับพี่อากิระ แต่ผมจำได้ว่าเคยไม่เคยให้เบอร์พี่ไปเลยกะจะแกล้งสักหน่อย"

# aki "Oh, that? I got Lilly to give it to me. Not hard."
aki "อ้อ เบอร์นายน่ะเหรอ ไปขอลิลลี่มา ไม่ยากหรอก"

# "She positively brims with pride at the statement. She's trying to get me caught up in her pace, I know it."
"อากิระพูดด้วยน้ำเสียงอันภาคภูมิ ฉันรู้หรอกว่ากะจะให้ฉันไหลตามน้ำซักไซ้ต่อ"

# "I suppose I shouldn't be surprised that the two would share my number though, given how close they are."
"แต่สนิทกันขนาดนี้ จะมีเบอร์ฉันทั้งพี่ทั้งน้องเลยก็คงไม่แปลก"

# hi "So, what's up?"
hi "แล้วนี่มีอะไรเหรอครับ"

# aki "You free right now?"
aki "ตอนนี้ว่างเปล่า"

# hi "I… guess? Why?"
hi "ก็… ว่างนะครับ? ทำไมเหรอ"

# aki "Could you meet me at the park in town? I just want to talk to you about some stuff."
aki "มาหาที่สวนสาธารณะในเมืองหน่อยได้มั้ย มีเรื่องจะคุยด้วยหน่อย"

# hi "Is that an invitation to a date?"
hi "นี่ชวนไปเดตเหรอครับ"

# aki "What? Of course not…"
aki "ฮะ? ใช่ที่ไหน…"

stop music fadeout 5.0

# "She sounds suddenly crestfallen, her previous teasing nature having instantaneously left. It seems strange for her."
"อยู่ ๆ น้ำเสียงของอากิระก็หมองไป นิสัยที่ปกติจะชอบหยอกเล่นก็หายไปในทันที ซึ่งดูไม่ใช่ตัวเธอเลย"

# hi "Anyway, I don't see why not. When do you want to meet?"
hi "แต่นั่นแหละครับ ก็ไปหาได้อยู่ จะให้ไปกี่โมงเหรอครับ"

# aki "Kind of… now. Ish."
aki "ก็สัก… เดี๋ยวนี้ โมง"

# hi "Wait, right now? But it's—"
hi "เดี๋ยว ตอนนี้เหรอครับ แต่—"

# "The dead silence suddenly coming from the phone announces the fact that she has unceremoniously hung up."
"เสียงปลายสายที่หายไปจากโทรศัพท์บ่งบอกว่าอากิระตัดสายทิ้งไปดื้อ ๆ แล้ว"

show phone mobile:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with None

scene bg school_hallway3
show phone mobile:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with locationchange
with Pause (0.5)

hide phone
with None

# "For a long time I just stand there, staring at the “CALL ENDED” message on the screen while replaying the conversation in my head."
"ฉันยืนนิ่งมองจอที่ขึ้นคำว่า “วางสายแล้ว” อยู่พักใหญ่พลางย้อนนึกถึงบทสนทนาเมื่อครู่ในหัว"

# hi "What the hell, Akira?"
hi "อะไรของพี่เขาวะเนี่ย"

scene bg suburb_park_ss
with shorttimeskip

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_parkambience fadein 2.0

# "Throwing a glance up and down the street, I cross the road and step into the park."
"ฉันมองซ้ายมองขวาก่อนจะเดินข้ามถนนไปที่สวนสาธารณะ"

# "I've learned to pace myself on such walks, mostly because Lilly's slower speed during our forays into town means I have to consciously slow myself down."
"ฉันเดินด้วยฝีก้าวเช่นนี้จนติดเป็นนิสัยแล้ว หลัก ๆ ก็เป็นเพราะตอนไปเดินเข้าเมืองกับลิลลี่ฉันต้องลดความเร็วฝีเท้า\nตัวเองลงให้เสมอกับฝีเท้าของลิลลี่"

# "That aside, I hope Akira didn't expect me to be immediately prompt."
"เรื่องนั้นช่างก่อน แต่หวังว่าอากิระจะไม่ได้คิดว่าฉันจะมาแบบปุบปับทันใจได้เลยนะ"

$ ksgallery_unlock("evul akira_park")
scene ev akira_park:
    subpixel True xalign 1.0 yalign 0.0 zoom 1.0
    acdc_warp 15.0 zoom 0.8
with whiteout

play music music_night

# "It takes only a couple of seconds to spot her, waiting on a bench with a can of beer in her hand."
"ไม่นานฉันก็หาอากิระที่ยืนถือกระป๋องเบียร์รออยู่ตรงม้านั่งเจอ"

# "The look she gives me as I walk up lacks any hint of acknowledgment or greeting."
"อากิระมองมาทางฉันด้วยสีหน้าที่ไร้ซึ่งการทักทายหรือรับรู้ถึงตัวตนของฉัน"

# hi "What's with that look? I needn't have come, you know."
hi "ทำหน้าแบบนั้นนี่คืออะไรเหรอครับ รู้มั้ยว่าจริง ๆ ผมจะไม่มาก็ยังได้"

# aki "I knew you would. You're that kind of person, after all."
aki "ฉันรู้น่าว่ายังไงนายก็ต้องมา ก็นายเป็นคนแบบนั้นนี่นะ"

scene bg suburb_park_ss
with locationchange

play sound sfx_can_clatter

# "I lower my brow at her remark as she disposes of the can, emptied by the time I arrived, and a metallic clatter rings out. Akira takes a seat on the old wooden bench, and I follow her lead."
"ฉันหรี่ตามองตามอากิระที่ทิ้งกระป๋องเบียร์ซึ่งเธอดื่มไปจนหมดตอนที่ฉันมาถึงพอดี เสียงกระป๋องถูกเคาะดังตามมา\nอากิระเดินมานั่งที่ม้านั่งไม้เก่า ๆ ส่วนฉันก็นั่งลงข้าง ๆ"

play sound sfx_can

# "She takes another can of beer from beside her and opens it before speaking, taking a large gulp. She seems to really like that stuff."
"เธอหยิบเบียร์อีกกระป๋องที่วางอยู่ข้าง ๆ มาเปิดก่อนจะพูดอะไรแล้วดื่มเข้าไปอึกใหญ่ ดูท่าจะชอบจริง ๆ"

# hi "I suppose I don't need to ask what this is about, or rather, who it's about?"
hi "ผมคงไม่ต้องถามว่าเรื่องอะไรหรือใครใช่มั้ยครับ"

show akira basic_resigned_close_ss at tworight
with charaenter

# aki "I heard from Lilly that you asked about our family."
aki "ได้ยินลิลลี่บอกว่านายถามเรื่องครอบครัว"

# "They share more than phone numbers, that's for sure. I'd probably be very worried right now if it weren't for the total lack of malice in her voice. Rather, her tone sounds almost wistful."
"คงมีเรื่องอื่นนอกจากเบอร์โทร. ที่รู้กันทั้งคู่แน่ ๆ ละ เพราะน้ำเสียงตอนพูดไม่ได้มีเจตนาร้ายอะไรหรอกฉันถึงได้ไม่เป็น\nกังวลอะไร เป็นน้ำเสียงที่ฟังดูเศร้าสร้อยด้วยซ้ำ"

# hi "Idle curiosity, mostly."
hi "ก็แค่อยากรู้เฉย ๆ แหละครับ"

# hi "…I have to admit, I'd never have guessed you two were half Scottish."
hi "…แต่ต้องยอมรับว่าให้ตายผมก็เดาไม่ถูกว่าพวกพี่เป็นคนสกอตแลนด์"

show akira basic_ending_close_ss
with charachange

# "She gives a wry chuckle of amusement."
"อากิระแค่นหัวเราะแห้ง ๆ ชอบใจ"

show akira basic_smile_close_ss
with charachange

# aki "I've heard that before, trust me."
aki "ใคร ๆ ก็พูดงั้นแหละ บอกเลย"

show akira basic_distant_close_ss
with charachange

# "The small smile falls from her face, her eyes looking ahead distantly."
"รอยยิ้มจาง ๆ นั้นหายไป เธอเหม่อมองไกล ๆ"

# "Aside from the occasional elderly couple talking as they slowly walk the meandering paths, and the odd aging car, it's pleasantly quiet."
"มีเพียงความเงียบที่ชวนให้รื่นใจ รอบตัวไม่มีเสียงใดนอกจากคู่ผู้สูงอายุที่คุยกันเดินช้า ๆ ไปตามถนนคดเคี้ยวกับรถเก่า ๆ\nที่แล่นผ่านเป็นระยะ ๆ"

show akira basic_lost_close_ss
with charachange

# aki "She didn't tell you everything though, did she?"
aki "แต่ลิลลี่ไม่ได้เล่าอะไรมากใช่มั้ย"

# hi "It was pretty brief. Your parents live in Scotland, she hasn't met them since she was twelve, and she wants to meet them again."
hi "ก็เล่าแบบคร่าว ๆ น่ะครับ อย่างเรื่องที่พ่อแม่ของพี่อยู่สกอตแลนด์ เรื่องที่ว่าไม่ได้เจอกันตั้งแต่อายุสิบสอง แล้วก็\nบอกว่าอยากกลับไปหาอีก"

show akira basic_annoyed_close_ss
with charachange

# aki "It's always surprised me how devoted she is to our parents, for all the good they did us."
aki "ฉันละทึ่งจริง ๆ ที่ลิลลี่กตัญญูตอบแทนพ่อแม่ดีขนาดนั้นน่ะ"

# "The way she says it sounds almost derisive. She gives a small sigh, as if to quickly brush the feelings away."
"น้ำเสียงอากิระฟังดูคล้ายการเย้ยหยัน เธอถอนหายใจเบา ๆ ราวกับจะรีบปัดความรู้สึกนั้นทิ้งไป"

show akira basic_resigned_close_ss
with charachange

# aki "Why do you think they left, Hisao?"
aki "นายว่าทำไมพ่อแม่พวกฉันถึงย้ายไปอยู่สกอตแลนด์ ฮิซาโอะ"

# hi "Why do I think they left?"
hi "เหตุผลว่าทำไมพ่อแม่พวกพี่ถึงไปสกอตแลนด์น่ะเหรอครับ"

# hi "From what Lilly told me, it was because of work. I guess a pretty decently-paying job was involved as well, given the way your parents seem to live."
hi "ถ้าเท่าที่ลิลลี่บอกมา ก็คิดว่าเรื่องงานแหละครับ แล้วก็น่าจะเป็นงานที่ได้เงินดีพอสมควรเลย ดูจากการใช้ชีวิตของ\nพ่อแม่พวกพี่"

# hi "So Lilly went to a private school, and that's why she carries herself with the airs and graces of the upper class."
hi "เพราะงั้นลิลลี่ถึงได้ไปเรียนที่โรงเรียนเอกชน แล้วก็เลยได้บรรยากาศอย่างลูกผู้ดีติดตัวมาด้วย"

# aki "Yeah. Since the business in Inverness boomed, our father decided to move directly to the same city as its headquarters."
aki "อืม พอธุรกิจที่อินเวอร์เนสส์เริ่มรุ่ง พ่อก็ย้ายไปอยู่ที่สำนักงานใหญ่โดยตรงเลย"

show akira basic_smile_close_ss
with charachange

# aki "That's just the conclusion I'd thought you'd come to, though. You're too good-natured."
aki "ซึ่งนายก็คงจะได้ข้อสรุปแบบนั้นใช่มั้ยล่ะ นายน่ะซื่อเกินไปนะ"

# hi "You don't think they left for their career?"
hi "พี่คิดว่าที่พ่อแม่พี่ย้ายไปไม่ใช่เพราะเรื่องงานเหรอครับ"

show akira basic_resigned_close_ss
with charachange

# aki "I'm sitting here bitching to you about it. What do you think?"
aki "ก็ฉันมานั่งบ่นอยู่กับนายเนี่ย คิดว่าไงล่ะ"

show akira basic_lost_close_ss
with charachange

# aki "Yamaku Academy. I've always felt that place was kinda creepy; like it was an isolated hideaway for those “proper society” doesn't want to see nor hear."
aki "โรงเรียนยามากุ เห็นทีไรก็ขนลุก สภาพเหมือนที่สันโดษเอาไว้ซ่อนของที่พวก “สังคมสมบูรณ์” ไม่อยากเห็น\nไม่อยากได้ยิน"

show akira basic_annoyed_close_ss
with charachange

# aki "They probably just rue the fact that Lilly wasn't old enough to be shoved there by the time they left."
aki "ตอนที่ย้ายไปน่ะ คงเสียดายด้วยซ้ำมั้งที่โยนลิลลี่ทิ้งไว้กับโรงเรียนนั้นไม่ได้เพราะตอนนั้นยังเด็กเกิน"

# "A long silence follows her abrupt and very harsh criticism of her own parents, and Yamaku."
"หลังจากคำวิจารณ์ของอากิระอันเสียดแทงที่มีต่อพ่อแม่ของเธอเองกับยามากุซึ่งมาแบบกะทันหันผ่านไปแล้วก็มีเพียง\nความเงียบเนิ่นนาน"

# "Lilly's blindness is hardly something that could be simply ignored for a high-class family attempting to keep up appearances, much less so when a lucrative offer is on the table."
"กับครอบครัวชนชั้นสูงที่ให้ความสำคัญกับเรื่องหน้าตาในสังคมแล้ว การที่ลิลลี่ตาบอดนั้นไม่ใช่เรื่องที่จะตัดทิ้งไปได้\nง่าย ๆ แล้วยิ่งมีตัวเลือกซึ่งให้ผลตอบแทนงามเข้ามาเกี่ยวข้องอีก"

# "Eventually Akira gives a derisive snort, her feelings coming to a head."
"ในที่สุดอากิระก็แค่นหัวเราะเย้ยหยันเผยความรู้สึกขึ้นมา"

# aki "Moving to secure our financial future with his new job posting. Even at the time I hardly believed it."
aki "ย้ายไปที่ทำงานใหม่เพื่อความมั่นคงทางการเงินในอนาคตงั้นเหรอ ขนาดตัวฉันตอนนั้นยังแทบไม่อยากเชื่อเลย"

# "Not wanting to simply be an avenue for her venting, I gently try to steer the discussion."
"ฉันไม่อยากรับบทเป็นกระโถนท้องพระโรงอยู่ฝ่ายเดียวจึงค่อย ๆ เปลี่ยนเรื่องไปเสียหน่อย"

# hi "So you stayed in Japan with Lilly, then?"
hi "พี่ก็เลยอยู่กับลิลลี่ที่ญี่ปุ่นเหรอครับ"

show akira basic_resigned_close_ss
with charachange

# aki "Either I stayed with her, or she went to live with an ailing grandmother and grandfather."
aki "ถ้าไม่อยู่ด้วยลิลลี่ก็ต้องไปอยู่กับปู่ย่าที่เจ็บออด ๆ แอด ๆ นั่นน่ะ"

# hi "What about Shizune's family? If you're cousins, then…"
hi "แล้วครอบครัวชิซูเนะล่ะครับ ถ้าเป็นลูกพี่ลูกน้องกันก็น่าจะ…"

show akira basic_annoyed_close_ss
with charachange

# aki "Our fathers hate each other. I'd have been more than happy to tell them to go screw themselves and live with them anyway, but Lilly wouldn't have wanted that."
aki "พ่อกับลุงน่ะเกลียดกันยิ่งกว่าอะไรดี ไอ้ฉันน่ะไม่ติดเลยนะ จะบอกเลยว่าเรื่องของเอ็งสิ จะอยู่ด้วย มีปัญหามั้ย แต่ลิลลี่\nคงไม่เอาด้วยหรอก"

show akira basic_resigned_close_ss
with charachange

# aki "I'd also had an offer for a job by then, so we did our best to keep our parents' house in proper shape, and tried to continue our lives as if they'd never left."
aki "พอดีตอนนั้นฉันได้งานด้วย เราสองคนก็เลยคอยดูแลบ้านพ่อแม่ให้ แล้วก็ใช้ชีวิตเหมือนกับว่าพ่อแม่ยังอยู่นี่แหละ"

# hi "So you just lived by yourselves?"
hi "ก็คืออยู่ด้วยกันแค่สองคนเหรอครับ"

show akira basic_lost_close_ss
with charachange

# aki "Basically. Lilly had school and I had my job, so we weren't exactly languishing."
aki "ประมาณนั้น ลิลลี่ไปโรงเรียน ส่วนฉันก็ไปทำงาน ก็เลยไม่ได้มีปัญหาอะไรมาก"

# aki "With her schooling, her study, and having to do chores while I worked, though, I can't help feeling like I failed her. In the end, I tried to be there for her, and screwed it up."
aki "แต่พอให้ลิลลี่มาทำงานบ้านช่วงที่ฉันไปทำงานทั้ง ๆ ที่ลิลลี่ก็ต้องเรียนต้องอ่านหนังสืออยู่แล้วก็อดรู้สึกผิดไม่ได้ว่าตัวเอง\nพึ่งพาไม่ได้เลย แล้วสุดท้ายพอจะลองเป็นที่พึ่งให้ฉันก็ยังทำพลาดอีก"

show akira basic_annoyed_close_ss
with charachange

# aki "…Expecting a nineteen-year-old to be a mother for a blind child. It's ridiculous."
aki "…จะให้เด็กอายุสิบเก้ามาเป็นแม่ของคนตาบอดเนี่ยนะ บ้าหรือเปล่า"

# "So… Lilly and Akira lived alone after their parents moved, with Lilly largely taking care of herself. I guess that explains her apparent independence, compared to many in Yamaku."
"ก็คือ… ลิลลี่กับอากิระอยู่ด้วยกันสองคนตามลำพังหลังจากที่พ่อแม่ย้ายออกไปแล้ว โดยที่ส่วนมากลิลลี่ก็จะต้องดูแล\nตัวเอง ซึ่งก็น่าจะเพราะอย่างนี้ลิลลี่ถึงได้ดูไม่ต้องพึ่งพาคนอื่นมากเมื่อเทียบกับคนอื่นที่ยามากุ"

# "I may have lived alone much of the time since my parents both worked, but that's… just something else entirely."
"ฉันเคยอยู่ตัวคนเดียวช่วงที่พ่อแม่ไปทำงานก็จริง แต่… เทียบไม่ได้เลยกับสิ่งที่ลิลลี่เจอ"

show akira basic_resigned_close_ss
with charachange

# aki "Sorry for making you listen to my moaning, Hisao."
aki "ขอโทษที่ให้มานั่งฟังฉันพล่ามอย่างนี้นะฮิซาโอะ"

# hi "I don't mind at all, but… do you mind if I ask why you're telling me all this?"
hi "ผมไม่ถือหรอกครับ แต่ว่า… ถามหน่อยได้มั้ยครับว่ามาเล่าให้ผมฟังทำไม"

show akira basic_smile_close_ss
with charachange

# aki "Hmph. You always were curious."
aki "ฮึ นายนี่ขี้สงสัยตลอดเลยนะ"

show akira basic_distant_close_ss
with charachange

# aki "Context, I suppose."
aki "เล่าเป็นบริบทละมั้ง"

# aki "Life isn't a fairytale, Hisao. Some people have to learn that the hard way."
aki "ชีวิตมันไม่สวยงามเหมือนนิยายนะฮิซาโอะ บางคนก็ต้องเจ็บมากว่าจะได้รู้ซึ้ง"

# "She takes a long drink from the can in her hand, her face becoming more depressed than distant."
"อากิระยกกระป๋องขึ้นดื่มอึกยาวพร้อมสีหน้าที่ดูเหมือนเครียดมากกว่าเหม่อลอย"

stop music fadeout 2.0

show akira basic_resigned_close_ss
with charachange

# aki "I broke up with my boyfriend a few days ago. After I leave, we're not going to be able to see each other again."
aki "สองสามวันก่อนฉันเพิ่งเลิกกับแฟนมา ถ้าฉันไปแล้วเราก็จะไม่ได้เจอหน้ากันอีก"

# aki "But that's how life is. You can't just set your life up and expect it to stay that way forever; sometimes stuff happens that you have to roll with, even if it means hurting yourself or others."
aki "แต่ชีวิตก็งี้แหละ คนเราจะหวังให้ชีวิตมันเป็นอย่างนั้นไปตลอดไม่ได้ บางครั้งอะไรจะเกิดเราก็ต้องไหลตามมันไป ต่อให้\nไหลไปแล้วตัวเองหรือคนอื่นจะเจ็บด้วยก็เถอะ"

# "She takes a long breath before looking up at the bright orange sky."
"เธอถอนหายใจยาวเงยหน้ามองฟ้าสีแสดสว่าง"

show akira basic_distant_close_ss
with charachange

# aki "Damn… if I smoked, I could take a nice, long drag right about now and look kinda cool."
aki "แม่ง… ถ้ามีบุหรี่ด้วยก็จะได้สูบปื้ดยาว ๆ เน้น ๆ ทำเท่สักหน่อย"

# "I want to respond, to help her in whatever way I can, but I feel utterly useless. This kind of situation is one I've never been in, and I simply don't have the experience to say anything meaningful to comfort her."
"ฉันอยากจะหาอะไรก็ได้มาตอบให้อากิระรู้สึกดีขึ้น แต่ก็คิดอะไรไม่ออกเลย สถานการณ์นั้นเป็นสถานการณ์ที่ฉันไม่เคย\nเจอมาก่อน แล้วฉันก็ไม่มีประสบการณ์พอที่จะเอาอะไรที่มีความหมายมาพูดปลอบเธอได้"

# "Akira looks over and evidently picks up on this, much to my embarrassment."
"อากิระหันมามองเหมือนรับรู้เจตนาของฉัน ถึงฉันจะไม่อยากยอมรับเลยก็เถอะ"

show akira basic_lost_close_ss
with charachange

# aki "I must look pretty pathetic right now, whining about this to someone I barely know."
aki "สภาพฉันตอนนี้คงสมเพชน่าดูเลยสินะ มานั่งงอแงเรื่องนี้กับคนที่แทบไม่ได้รู้จักกันเนี่ย"

# hi "Hardly, and I'm pretty much an expert on looking pathetic."
hi "ไม่หรอกครับ อันนี้ผมพูดในฐานะคนที่ทำตัวน่าสมเพชได้เก่งเลยนะ"

show akira basic_ending_close_ss
with charachange

# "She gives a chuckle, the act feeling like a personal victory for me."
"เธอแค่นหัวเราะ ซึ่งทำให้ฉันรู้สึกเหมือนได้ประสบความสำเร็จโดยส่วนตัวแล้ว"

show akira basic_smile_close_ss
with charachange

# aki "You're a good kid, Hisao. When I said that I approved of you being with my sister, I wasn't joking or just being nice."
aki "นายน่ะเป็นคนดีนะฮิซาโอะ ตอนที่ฉันยอมรับให้นายเป็นแฟนกับน้องฉันน่ะ ฉันไม่ได้พูดเล่นหรือพูดไปงั้น ๆ นะ"

show akira basic_smile_ss:
    tworight
    ypos 1.1
    ease 0.5 ypos 1.0
with charadistant

play sound sfx_can_clatter

# "She picks herself up off the seat with a grunt, one that seems ill-fitting given her age, and throws the now empty can into the bin after one last swig."
"อากิระลุกขึ้นยืนพร้อมเสียงโอดโอยที่ฟังดูไม่สมอายุแล้วกระดกเบียร์อึกสุดท้ายก่อนจะโยนกระป๋องเปล่าลงถังขยะ"

show akira basic_boo_ss at tworight
with charachange

# aki "It's just unfortunate that doesn't really count for much in this world."
aki "แค่บังเอิญว่าโชคไม่ดีที่การเป็นคนดีมันไม่ได้มีความหมายอะไรมากกับโลกนี้น่ะ"

show akira basic_resigned_ss
with charachange

# aki "When I said that I was leaving for Scotland, I was doing it because a good position opened up in our company's headquarters."
aki "ที่บอกว่าฉันจะไปสกอตแลนด์คือฉันไปเพราะมีตำแหน่งดี ๆ ที่สำนักงานใหญ่ที่ว่างอยู่"

# aki "When our folks told me that when we were at their place, though, they also gave Lilly a summons to rejoin them in Inverness."
aki "แต่ตอนที่ฉันรู้เรื่องนี้จากคนที่บ้านตอนอยู่สกอตแลนด์น่ะ เขาชวนให้ลิลลี่กลับไปอยู่ด้วยกันที่อินเวอร์เนสส์ด้วย"

play music music_sadness fadein 0.5

# "No way…"
"บ้าน่า…"

# "Her evasiveness when asked about her future… that awkwardness that had steadily grown between us… that uncharacteristic outburst of anger…"
"งั้นที่ลิลลี่เลี่ยงตอนถามเรื่องอนาคต… งั้นความอึดอัดที่เริ่มเกิดขึ้นระหว่างเรา… งั้นการที่อยู่ ๆ ลิลลี่เดือดอย่างนั้น…"

# "All of them suddenly fit into place."
"ทันใดนั้นเองทุกอย่างก็ลงล็อกพอดี"

# "The same family that she reminisced about after Hanako's birthday party, the same family that left her and Akira to themselves after taking flight to greener pastures…"
"ครอบครัวที่เธอหวนรำลึกตอนที่จัดงานเลี้ยงให้ฮานาโกะ… ครอบครัวที่ทิ้งให้ลิลลี่กับอากิระต้องอยู่ตามลำพังหลังจาก\nที่ตัวเองบินไปแสวงหาสิ่งที่ดีกว่า…"

# "Now I feel stupid for never cornering Lilly on what was bugging her. I'd never even considered if something had happened during her trip to her family's home at Inverness."
"แล้วฉันก็รู้สึกโง่เง่าขึ้นมาทันทีที่ไม่เคยเค้นถามลิลลี่เลยว่าคิดมากเรื่องอะไรอยู่ ไม่เคยคิดเลยด้วยซ้ำว่าจะมีเรื่องอะไร\nเกิดขึ้นช่วงที่ลิลลี่ไปเที่ยวที่บ้านของครอบครัวเธอที่อินเวอร์เนสส์หรือเปล่า"

# "And now, a sense of unease grows in my chest. If her family has summoned her to join them in Scotland, all the way on the other side of the Earth…"
"และตอนนี้ฉันก็รู้สึกจุกอกขึ้นมา ถ้าครอบครัวชวนให้ลิลลี่ไปอยู่ด้วยกันที่สกอตแลนด์ซึ่งอยู่คนละฟากโลกกับญี่ปุ่น\nแล้ว…"

# hi "Has she… accepted?"
hi "แล้วลิลลี่… จะไปมั้ยครับ"

show akira basic_lost_ss
with charachange

# aki "Lilly hasn't told me whether she plans to accept, and it seems she hasn't told you, either."
aki "ลิลลี่ยังไม่ได้บอกฉันเลยว่าจะไปหรือเปล่า แล้วก็คงไม่ได้บอกนายด้วยเหมือนกันสินะ"

# aki "That's why I called you down here to talk, Hisao."
aki "นั่นแหละฉันถึงได้เรียกนายมาคุยด้วย ฮิซาโอะ"

# hi "Context, huh…"
hi "บริบทเหรอ…"

# "I sit back, my feelings of worry and frustration no doubt written all over my face."
"ฉันเอนตัวพิงพนัก ตอนนี้ทั้งความกังวลและความหงุดหงิดคงแสดงออกทางสีหน้าหมดแล้ว"

show akira basic_resigned_ss
with charachange

# aki "Lilly's a strong person, Hisao, but she's not infallible."
aki "ลิลลี่เป็นคนแข็งแกร่งนะฮิซาโอะ แต่ก็ใช่ว่าจะสมบูรณ์แบบไปเสียทุกอย่าง"

# aki "I guess it's my job to worry about her, being her older sister, but I think that you deserve to know."
aki "ก็คงเป็นหน้าที่ของฉันในฐานะพี่สาวละนะที่ต้องคอยเป็นห่วงลิลลี่ แต่ฉันคิดว่านายก็มีสิทธิ์ที่จะรู้เหมือนกัน"

# hi "I understand."
hi "เข้าใจครับ"

show akira basic_lost_ss
with charachange

# aki "You okay? You sound depressed."
aki "ไหวมั้ย ฟังดูนายเครียด ๆ นะ"

# hi "No, I'm just… thinking."
hi "ไหวครับ ผมแค่… กำลังคิดอยู่"

show akira basic_ending_ss
with charachange

# aki "That's good. Thinking is good. Being rash won't get you anywhere."
aki "ดีแล้ว คิดก็ดีแล้ว บุ่มบ่ามไปก็ไม่ได้อะไรขึ้นมาหรอก"

show akira basic_boo_ss
with charachange

# "She looks at her watch, barely moving her wrist."
"อากิระก้มมองนาฬิกาโดยที่แทบไม่ขยับข้อมือ"

show akira basic_lost_ss
with charachange

# aki "I've got to go. Will you be okay?"
aki "ต้องไปแล้วละ นายยังไหวอยู่นะ"

# hi "I'll be fine, don't worry. I'll have to talk to Lilly about it and get everything sorted out."
hi "ไหวครับ ไม่ต้องห่วง เดี๋ยวผมไปคุยกับลิลลี่แล้วจัดการอะไรให้เรียบร้อยเอง"

show akira basic_smile_ss
with charachange

# "She gives a smile, but it doesn't feel all that genuine or sincere."
"อากิระยิ้มให้ แต่ก็ดูไม่ใช่ยิ้มที่มาจากใจจริง ๆ"

# "Really, both of us are dancing around the fact that Lilly's on the precipice of the biggest decision of her life and is trying to take the entire burden on herself."
"ให้ตายเถอะ เราสองคนก็ได้แต่อ้อมไปอ้อมมาไม่พูดตรง ๆ ว่าตอนนี้ตอนนี้ลิลลี่กำลังอยู่ที่จุดพลิกผันกับการตัดสินใจ\nครั้งใหญ่ที่สุดในชีวิตของเธอ แล้วยังจะหาทางรับภาระทั้งหมดไว้ด้วยตัวเองอีก"

# "And part of that burden is the matter of our relationship."
"แล้วส่วนหนึ่งของภาระนั้นคือเรื่องความสัมพันธ์ของฉันกับลิลลี่ด้วย"

stop music fadeout 5.0
hide akira
with charaexit

# "By the time I look up, Akira's already walking off with her hand held up."
"พอเงยหน้าขึ้นมองก็เห็นว่าอากิระเดินชูมือลาออกไปแล้ว"

# "For the first time in a long while, I finally have an answer to something. Perhaps not even that. But at least I now have the right question to ask."
"ในที่สุดฉันก็มีคำตอบ หลังจากที่ไม่ได้มีมาแสนนาน อาจจะไม่ใช่คำตอบจริง ๆ หรอก แต่อย่างน้อยตอนนี้ฉันก็รู้แล้ว\nว่าต้องถามอะไร"

# "“Will you leave, or stay?”"
"“เธอจะอยู่ หรือไป”"

stop ambient fadeout 2.0

scene black
with dissolve


#*********************

label th_L28:

scene bg suburb_roadcenter_rn
show rain normal
with locationchange

play ambient sfx_rain fadein 4.0

# hi "Hurry, Lilly!"
hi "เร็วหน่อยลิลลี่!"

show lilly basic_concerned_cas_close_rn behind rain at center
with charaenter

# li "I'm moving as fast as I can!"
li "ก็เร็วสุดแล้วเนี่ย!"

# "I can barely make out Lilly's voice over the deafening pounding of the rain. Even though I dislike pulling her around, the situation calls for it."
"เสียงฝนตกดังกลบจนแทบไม่ได้ยินเสียงลิลลี่ ถึงจะไม่ชอบลากลิลลี่ไปไหนมาไหน แต่ตอนนี้จำเป็นจริง ๆ"

# "I turn forward, my free hand over my head in a futile attempt to keep at least my hair dry. My vision seems to be in grayscale. This really is rotten weather for summer, and the last kind of climate I'd want for a date."
"ฉันหันหน้าไปพลางยกมือขึ้นมาป้องหัวเพื่ออย่างน้อยหัวจะได้ไม่เปียก ซึ่งไม่เป็นผลนัก ภาพตรงหน้าหมองหม่น เป็น\nสภาพอากาศที่ไม่เหมาะกับหน้าร้อนเอาเสียเลย แล้วยังเป็นสภาพอากาศที่ไม่อยากเห็นตอนมาเดตมาก ๆ"

# "A pity. I'd even checked the weather forecast beforehand, one of the very few times I've ever done so, only for it to say that Sunday afternoon would be fine."
"น่าเสียดายจริง ๆ อุตส่าห์ดูพยากรณ์อากาศมาล่วงหน้าแล้ว ปกติก็ไม่ค่อยจะได้ดูด้วย แต่พยากรณ์อากาศก็ดันมาบอก\nว่าบ่ายวันอาทิตย์ท้องฟ้าจะปลอดโปร่งดี"

# "Looking to Lilly, her shoulders are by now completely drenched, with her right hand holding tightly to mine and her left gripping her retracted cane."
"พอหันไปมองก็เห็นว่าไหล่ลิลลี่เปียกฝนหมดแล้ว เธอใช้มือขวาจับมือฉันไว้แน่น ส่วนมือข้างซ้ายจับไม้เท้าที่หดเก็บไว้"

# "This horrid downpour came on just as we were between our destination and Yamaku, so we decided to try rushing the rest of the distance rather than doubling back."
"ฝนห่านี้กระหน่ำเทลงมาจังหวะที่เราเดินออกมาจากยามากุแล้วอยู่กลางทางพอดี พวกเราจึงเลือกที่จะรีบวิ่งไปจนถึง\nปลายทางแทนที่จะต้องเดินกลับไปอีกรอบ"

# "Entirely unused to running this fast, Lilly's using all her concentration just to avoid tripping over."
"ลิลลี่ตั้งสติอย่างหนักเพื่อไม่ให้ตัวเองสะดุดล้มเพราะไม่เคยต้องวิ่งเร็วขนาดนี้มาก่อน"

show lilly basic_oops_cas_close_rn
with charachange

# li "Hisao, do you know where we're going!?"
li "ฮิซาโอะ มีที่ที่จะไปแล้วเหรอ!"

# "Even she's reduced to shouting to try and be heard over the combined noise of the wind and the rain."
"แม้แต่ลิลลี่ยังต้องยอมตะโกนเพื่อให้เสียงดังแข่งกับเสียงลมเสียงฝนได้"

# hi "The Sha—"
hi "ร้านเซี่ย—"

# "The rest of my voice is completely drowned out by an even heavier burst of rain."
"ประโยคส่วนที่เหลือถูกกลบด้วยเสียงฝนที่ซัดสาดลงมาหนักกว่าเด่า"

show lilly basic_sad_cas_close_rn
with charachange

# li "The what!?"
li "ร้านอะไรนะ!"

# hi "The Shanghai!"
hi "ร้านเซี่ยงไฮ้!"

show lilly basic_concerned_cas_close_rn
with charachange

# li "How far is it!?"
li "อีกไกลมั้ย!"

# hi "It shouldn't be far now!"
hi "อีกไม่ไกลแล้ว!"

show bg suburb_shanghaiext_rn
show lilly basic_concerned_cas_close_rn
with shorttimeskip

# "It doesn't take long before I call out to her once again."
"ไม่นานฉันก็ได้เรียกลิลลี่อีกครั้ง"

# hi "It looks like we're safe, it's just up ahead!"
hi "ดูท่าจะปลอดภัยแล้วละ ร้านอยู่ข้างหน้านี่แล้ว!"

# "I quickly pull up to a stop just in front of the familiar exterior, the lantern outside still giving off its reliable glow, and wait for Lilly to catch her breath before going in."
"ฉันรีบวิ่งมาหยุดอยู่ที่หน้าร้านอันคุ้นเคยแล้วรอให้ลิลลี่ได้พักหายใจก่อนเข้าร้าน โคมไฟซึ่งแขวนอยู่นอกร้านยังคง\nส่องสว่างทำหน้าที่ของมัน "

# hi "Ladies first."
hi "เชิญสุภาพสตรีก่อนครับ"

play sound sfx_storebell

show lilly basic_smileclosed_cas_close_rn at center
with charachange

with Pause(0.5)

hide lilly
with charaexit

# "The tiny bell inside rings out when I hold the door open for her, a smile and a polite nod being my reward before entering myself."
"กระดิ่งใบเล็กดังกรุ๋งกริ๋งตอนที่ฉันเปิดประตูให้ลิลลี่ เธอยิ้มพยักหน้าอย่างสุภาพเป็นการขอบคุณก่อนที่ฉันจะได้เดิน\nตามเข้าไป"

$ renpy.music.set_volume(0.1, 1.0, channel="ambient")
play music music_dreamy fadein 3.0

scene bg suburb_shanghaiint
show lilly basic_smileclosed_cas at center
with locationchange

# "As I step in behind her and wipe my feet, only a quick glance is necessary to notice the distinct lack of activity. The Shanghai doesn't seem to get much in the way of patronage, and today is no different. Only a couple of tables are occupied."
"ฉันเดินตามลิลลี่ไปพลางเช็ดเท้า เพียงมองผ่าน ๆ ก็สังเกตได้ว่าในร้านแทบไม่มีลูกค้าเลย ร้านเซี่ยงไฮ้ดูเหมือนจะเป็น\nร้านที่ลูกค้าไม่ค่อยเยอะเท่าไหร่ และวันนี้ก็เช่นกัน มีแค่สองโต๊ะที่มีลูกค้านั่งอยู่"

# "Summoned by the bell's ringing, a most expected person comes to greet us."
"เสียงกระดิ่งนั้นเรียกให้คนคนหนึ่งออกมาทักทายเราตามคาด"

show bg suburb_shanghaiint at bgleft
show lilly basic_smileclosed_cas at twoleft
with charamove

show yuukoshang happy_up at tworight
with charaenter

# yu "Welcome to the Shanghai!"
yu "ยินดีต้อนรับสู่ร้านเซี่ยงไฮ้ค่ะ!"

# "Yuuko looks chipper today. Trying to predict her moods is pretty hard, but it's a nice change from the norm."
"วันนี้ยูโกะดูอารมณ์ดีแฮะ เดาอารมณ์ยากจริง แต่มีอะไรนอกจากเดิม ๆ บ้างก็ดีแล้วละนะ"

show lilly basic_smile_cas
with charachange

# li "Hello, Yuuko."
li "สวัสดีค่ะคุณยูโกะ"

# hi "Hey."
hi "สวัสดีครับ"

show yuukoshang closedhappy_down
with charachange

# yu "Good afternoon, you two."
yu "ทิวาสวัสดิ์นะทั้งสองคน"

show yuukoshang neutral_down:
    ypos 1.25
with Dissolvemove(0.2)

with Pause(0.2)

show yuukoshang neutral_down at tworight
with charamove

# "She takes a deep bow, somewhat taken aback as she rights herself again and gets a better look at us."
"ยูโกะโค้งตัวต่ำ พอกลับมายืนตามปกติได้ดูสภาพพวกเราชัด ๆ แล้วเธอก็เหมือนผงะไป"

show yuukoshang worried_down
with charachange

# yu "What happened to you? You both look…"
yu "มีอะไรหรือเปล่า เธอสองคนดู…"

# "Her eyes drift towards the glass of the door behind us."
"เธอเหล่ตาไปมองบานกระจกตรงประตูที่อยู่ข้างหลังพวกเรา"

show yuukoshang panic_up
with charachange

# yu "Oh. Oh dear."
yu "โอ๊ะ ตายจริง"

# hi "We're inside now, at least. I think that's the most important thing."
hi "อย่างน้อยตอนนี้ก็ได้ที่หลบฝนแล้วละครับ แค่นั้นก็พอแล้ว"

show lilly basic_weaksmile_cas
with charachange

# li "It's nice and cozy. You're lucky to be working inside today."
li "ในนี้อุ่นสบายดีจังเลยนะคะ โชคดีจังที่วันนี้คุณได้ทำงานในร่ม"

show yuukoshang smile_down
with charachange

# yu "It has been nice and quiet. I like days like this."
yu "เงียบสบายดีมากเลยละ ฉันชอบวันอย่างนี้มากเลย"

show yuukoshang worried_down
with charachange

# yu "Oh wait, um, sorry… is there anything you'd like?"
yu "โอ๊ะ เดี๋ยว เอ่อ ขอโทษค่ะ… จะรับอะไรดีคะ"

show lilly basic_smile_cas
with charachange

# li "French vanilla tea, please."
li "ชาเฟรนช์วานิลลาค่ะ"

# hi "I'll have the same."
hi "เหมือนกันครับ"

show yuukoshang closedhappy_up
with charachange

# yu "Right. Coming right up."
yu "ค่ะ สักครู่นะคะ"

hide yuukoshang
with charaexit

# "She quickly skitters off with a determined look on her face, trying very hard not to forget our orders. If nothing else, she is at least dedicated to her jobs."
"ยูโกะรีบพุ่งตัวออกไปด้วยสีหน้าอันมุ่งมั่นจำสิ่งที่เราสั่งไปให้ขึ้นใจ เอาเถอะ อย่างน้อยก็มุ่งมั่นกับงานดีละนะ"

show bg suburb_shanghaiint at center
show lilly basic_smileclosed_cas_close at center
with dissolvecharamove

show lilly basic_smileclosed_cas_close:
   ypos 1.1
with charamove

# "I lead Lilly to an empty seat before the two of us settle down. As usual, there's a large difference between my exhausted flopping down into my seat and Lilly's delicate sliding into hers, her cane set beside her."
"ฉันนำทางลิลลี่ไปยังโต๊ะที่ว่างอยู่ตรงหน้าเพื่อพักขา และเช่นเคย สภาพฉันที่ทิ้งตัวลงนั่งด้วยความเหนื่อยอ่อนนั้นต่าง\nจากลิลลี่ซึ่งค่อย ๆ ขยับตัวเข้าไปนั่งวางไม้เท้าลงข้าง ๆ โดยสิ้นเชิง"

# "For a while I just idly watch the rain falling outside. The occasional person runs down the street trying to stay as dry as possible, hands often tightly gripping a rain-soaked umbrella."
"ฉันนั่งเหม่อมองฝนนอกหน้าต่างอยู่พักใหญ่ บางทีก็มีคนที่วิ่งอยู่บนถนนที่กำลังรีบหาที่หลบฝนให้เร็วที่สุดผ่านไปมา\nซึ่งส่วนใหญ่ในมือก็ถือร่มซึ่งโชกไปด้วยฝนไว้แน่น"

# "Lilly sits just as quietly as I, her eyes closed as she intently listens to all that's happening."
"ลิลลี่ก็นั่งเงียบไม่ต่างจากฉัน เธอหลับตาเงี่ยหูฟังสิ่งต่าง ๆ ที่เกิดขึ้นรอบตัว"

# "It's a comfortable, relaxing silence that exists between us; just the type that we'd so often shared together in the past months."
"ระหว่างเรานั้นเป็นความเงียบซึ่งอยู่สบายและชวนให้ผ่อนคลาย เป็นความเงียบแบบที่เรามักได้ใช้เวลาอยู่ด้วยกันในช่วง\nเดือนสองเดือนที่ผ่านมา"

stop music fadeout 5.0

# "For Lilly, at least."
"อย่างน้อยก็เป็นความเงียบแบบที่ว่าสำหรับลิลลี่น่ะนะ"

# "I can't help replaying the words of her sister in my mind, at times contrasting them to both our time spent together since I entered Yamaku, and to the way we've been since we started dating."
"ฉันกรอคำพูดของพี่สาวเธออยู่ในหัว บางครั้งก็เอามาเทียบกับช่วงเวลาที่เราได้อยู่ด้วยกันตั้งแต่ที่ฉันได้ย้ายมาอยู่ที่\nยามากุ และเอามาเทียบกับความสัมพันธ์ของเรานับตั้งแต่เราเริ่มคบกัน"

# "No matter how much I try, I can't work Lilly out. It's as if the harder I try to second-guess her emotions and her potential decision, the more difficult it becomes to reach a clear conclusion."
"ไม่ว่าจะคิดยังไงฉันก็อ่านใจลิลลี่ไม่ออกเลย รู้สึกเหมือนว่ายิ่งฉันพยายามเดาความรู้สึกกับทางที่เธออาจเลือกเท่าไหร่\nข้อสรุปที่ชัดเจนก็ยิ่งเลือนรางไปมากขึ้นเท่านั้น"

# "It makes me doubt whether I'd ever really understood her. In the end, I'm going to have to ask, even though I very much want to avoid doing so."
"จนฉันนึกสงสัยว่าฉันเคยเข้าใจลิลลี่จริง ๆ หรือเปล่า สุดท้ายแล้วฉันก็ต้องออกปากถาม ถึงฉันจะอยากเลี่ยงไม่ถามเลย\nก็เถอะ"

show lilly basic_smile_cas_close
with charachange

# li "You seem quiet today, Hisao."
li "วันนี้เธอดูเงียบ ๆ ไปนะฮิซาโอะ"

# hi "Really?"
hi "จริงเหรอ"

show lilly basic_ara_cas_close
with charachange

# li "You seemed so enthusiastic about taking me out on a date, I'd assumed you had something specific you wanted to do."
li "เห็นเธออยากพาฉันมาเดตขนาดนั้น คงมีอะไรที่อยากทำเป็นพิเศษอยู่แล้วใช่มั้ย"

# hi "No, not really. Just wanted to spend some time with you."
hi "ไม่อะ ไม่หรอก แค่อยากใช้เวลาอยู่ด้วยกันกับเธอแค่นั้นแหละ"

show lilly basic_weaksmile_cas_close
with charachange

# li "Is that so…"
li "งั้นเหรอ…"

# hi "Fine. There was one thing."
hi "ก็ได้ มีอย่างนึง"

show lilly basic_cheerful_cas_close
with charachange

# "A little grin finds its way onto Lilly's face, her knowing full well that she's bested me. It makes what I want to say all the more awkward."
"ลิลลี่แสยะยิ้มออกมาเล็กน้อยเพราะรู้ดีว่าไล่ต้อนฉันให้จนมุมสำเร็จแล้ว ซึ่งทำให้ฉันยิ่งลำบากใจที่จะพูดประโยคถัดไป\nขึ้นไปอีก"

# hi "It was just… Akira and I were talking."
hi "คือ… ฉันไปคุยกับอากิระมา"

show lilly basic_surprised_cas_close
with charachange

# li "Oh?"
li "อ้าว"

# hi "What's with that tone?"
hi "อ้าวนี่คืออะไร"

show lilly basic_weaksmile_cas_close
with charachange

# li "You two do seem to get on well, don't you?"
li "เธอสองคนดูเข้ากันดีจังเลยนะ"

# hi "Well, I do think she's a pretty cool person to talk with. It'd be nice if any of the teachers were anything like her."
hi "ก็ เป็นคนที่คุยด้วยสนุกดีนะ ถ้ามีครูสักคนในโรงเรียนเป็นอย่างสักเสี้ยวอากิระได้คงดี"

show lilly basic_sleepy_cas_close
with charachange

# li "“Cool…”"
li "“สนุก…”"

# "For a moment I try to place her tone of voice, my mouth curling into a smirk as I realize it."
"ฉันนึกอยู่ครู่หนึ่งว่าน้ำเสียงนั้นหมายความว่าอะไร พอนึกออกฉันก็ยกยิ้ม"

# hi "You're not jealous, are you?"
hi "นี่คงไม่ได้หึงกันใช่มั้ย"

show lilly basic_pout_cas_close
with charachange

# li "I'm not jealous!"
li "เปล่าหึงสักหน่อย!"

# "After her teasing me over such a thing on our first date, I don't feel too bad having a little laugh at her expense this time around."
"เห็นเดตแรกแหย่ฉันเรื่องนั้นไป ฉันจึงไม่ได้รู้สึกผิดอะไรมากที่คราวนี้แหย่เธอกลับบ้าง"

# "As we settle down though, it's only a minor distraction from the real point of why I brought Lilly here."
"แต่หลังจากนี้ฉันก็ต้องเผชิญหน้ากับจุดประสงค์จริง ๆ ที่ฉันพาลิลลี่มาที่นี่"

# hi "Don't worry, it was mostly just everyday stuff. That said, there was something Akira mentioned that I wanted to talk to you about."
hi "ไม่ต้องห่วงหรอก ส่วนมากก็แค่คุยเรื่องดินฟ้าอากาศกันนั่นแหละ แต่เรื่องนี้ฉันได้ยินอากิระเล่ามาเลยอยากเอามา\nคุยกับเธอ"

# hi "When you went to see your family in Inverness a while back, she said…"
hi "ตอนที่เธอไปหาครอบครัวเธอที่อินเวอร์เนสส์น่ะ อากิระเล่าว่า…"

show lilly basic_reminisce_cas_close
with charachange

# li "Akira told you about my family's summons, hasn't she?"
li "พี่บอกเธอเรื่องที่ครอบครัวชวนให้ฉันไปอยู่ด้วยใช่มั้ย"

play music music_drama fadein 2.0

# "Seconds tick by while I try to read Lilly's face, an odd mixture of feelings written on it. She seems annoyed, but also somewhat confused."
"ฉันนั่งอ่านสีหน้าลิลลี่พร้อมเวลาที่ไหลผ่านไป เป็นสีหน้าที่มีอารมณ์ปะปนอยู่อย่างประหลาด ดูรำคาญ แต่ก็เหมือน\nสับสน"

show bg suburb_shanghaiint at bgleft
show lilly basic_reminisce_cas_close:
    twoleft
    ypos 1.1
with charamove

show yuukoshang neutral_up at tworight
with charaenter

# yu "Um… here…"
yu "เอ่อ… นี่ค่ะ…"

# "Yuuko tentatively slides our drinks onto the table, her presence oddly small."
"ยูโกะวางเครื่องดื่มของพวกเราลงกับโต๊ะกล้า ๆ กลัว ๆ เธอดูตัวเล็กไปถนัดตา"

hide yuukoshang
with charaexit

show bg suburb_shanghaiint at center
show lilly basic_reminisce_cas_close:
    center
    ypos 1.1
with charamove

# "As she walks back to the counter after a quick, polite nod, I realize the air between me and Lilly is thick and our expressions are both somewhat pensive."
"เธอพยักหน้าให้แล้วเดินกลับไปที่เคาน์เตอร์ และฉันก็เพิ่งรู้ตัวว่าบรรยากาศระหว่างฉันกับลิลลี่นั้นมาคุ เราทั้งคู่ต่าง\nทำสีหน้าตึงเครียด"

show lilly basic_displeased_cas_close
with charachange

# li "Even though she says I should lead my own life, she still interferes at the worst times…"
li "บอกให้ฉันเดินด้วยตัวเองแท้ ๆ แต่ชอบมาขัดจังหวะแบบนี้อยู่เรื่อยเลย…"

# hi "I don't think you should blame Akira here. She's just looking out for you, and it's not like I can't understand her concern over this."
hi "ฉันว่ามันไม่ใช่ความผิดของอากิระเลยนะ อากิระก็แค่เป็นห่วงเธอ ซึ่งฉันก็พอจะเข้าใจนะว่าทำไมถึงเป็นห่วง"

show lilly basic_weaksmile_cas_close
with charachange

# "Lilly's irritation gives way to an awkward, and largely unsuccessful, attempt to mask her feelings. She really doesn't deal well with being cornered on personal topics."
"แม้ลิลลี่จะพยายามปกปิดความรู้สึกของตัวเองอย่างฝืน ๆ แล้ว ทว่าความหงุดหงิดของเธอยังเผยอารมณ์ให้เห็นได้ชัด\nเธอนั้นรับมือเวลาที่มีคนมาซักไซ้เรื่องส่วนตัวไม่เป็นเลย"

# li "I know, but… I just wanted some more time. I knew you'd have figured it out eventually, but…"
li "ฉันรู้ ฉันแค่… ต้องการเวลาอีกสักหน่อย ฉันรู้ว่าสุดท้ายเดี๋ยวเธอก็รู้อยู่ดี แต่ว่า…"

# hi "You were intentionally hiding this from me? For how long were you planning to do so?"
hi "นี่เธอจงใจปกปิดกันเหรอ แล้วกะจะปกปิดไปอีกนานแค่ไหน"

show lilly basic_displeased_cas_close
with charachange

# li "As I said, I simply wanted more time to think it through. I wanted to be sure of my decision before telling you."
li "ก็อย่างที่บอก ฉันแค่ต้องการเวลาคิดให้ดีอีกหน่อย ฉันจะรอให้แน่ใจก่อนว่าฉันจะเอายังไงแล้วค่อยบอกเธอ"

# hi "What did you decide to do, in the end?"
hi "แล้วสรุปเธอจะเอายังไง"

# "I know what I want her to say, but an awful feeling refuses to leave my gut."
"ฉันรู้ว่าฉันคาดหวังคำตอบอะไรจากเธออยู่ แต่ฉันก็ปัดความรู้สึกไม่ดีนี้ออกไปจากใจไม่ได้"

show lilly basic_sleepy_cas_close
with charachange

# li "My family does dearly want me to return to them, and Akira will be going as well. I could still teach as a career, whether it be here or there."
li "ครอบครัวฉันอยากให้ฉันกลับไปอยู่ด้วยมาก ๆ แล้วพี่ก็จะไปด้วย แล้วไม่ว่าจะอยู่ที่นี่หรือที่นั่นฉันก็ยังยึดการสอน\nเป็นอาชีพเหมือนกัน"

# hi "So… you're going."
hi "ก็คือ… เธอจะไป"

# hi "How long have you known? I already know you were asked when you first went to Scotland, about a month ago."
hi "แล้วตัดสินใจมานานหรือยัง คือฉันรู้มาแล้วว่าที่บ้านชวนเธอตอนที่เธอไปสกอตแลนด์ครั้งแรกเมื่อเดือนก่อน"

show lilly basic_concerned_cas_close
with charachange

# li "Some… time."
li "สัก… พักแล้ว"

# "My frustration very nearly boils over. The fact that she's done this affects me more than it should."
"ฉันหงุดหงิดจนแทบทนไม่ไหวแล้ว สิ่งที่ลิลลี่ทำนั้นมีผลกับความรู้สึกมากเกินสมควร"

# "For her to not only be leaving but to have been actively hiding her own plans from me, and after seeming for so long to be the one solid pillar of support and reliability I could depend on…"
"จะไปไม่พอ แล้วยังปกปิดแผนของตัวเองจากฉันมาตลอด แล้วยังทำตัวเหมือนเป็นเสาหลักที่ฉันคอยพึ่งพิงพักพิงได้\nมาตั้งนาน…"

# "It feels as if the foundation underneath me is suddenly shifting drastically, much faster than I can adapt to. Perhaps this isn't so much frustration as sheer unease."
"เป็นความรู้สึกที่เหมือนอยู่ ๆ พื้นที่ยืนก็เลื่อนที่ออกไปอย่างรุนแรง รวดเร็วเกินกว่าที่ฉันจะปรับตัวทัน บางที ที่ฉันรู้สึก\nตอนนี้คงไม่ใช่ความหงุดหงิด หากแต่เป็นความรู้สึกว่างโหวงในใจมากกว่า"

# hi "Lilly…"
hi "ลิลลี่…"

show lilly basic_sad_cas_close
with charachange

# li "I'm sorry, I just… I wanted to think this through completely. I wasn't trying to take advantage of you, please—"
li "ฉันขอโทษ ฉันแค่… อยากคิดให้มันถี่ถ้วนน่ะ ฉันไม่ได้จะหลอกเธอเลยนะ ได้โปรด—"

# hi "I know, Lilly. I know. This is just really sudden."
hi "ฉันรู้ ลิลลี่ ฉันรู้ แค่ว่าเรื่องมันกะทันหันมาก ๆ"

# hi "I guess this means that once you go, we'll be breaking up?"
hi "งั้นก็แปลว่าถ้าเธอไปแล้วเราก็จะเลิกกันใช่มั้ย"

# "For one of the few times I've seen since I met her, she's genuinely lost for words."
"ครั้งนี้เป็นหนึ่งในไม่กี่ครั้งที่ลิลลี่นึกหาคำมาพูดไม่ออกจริง ๆ"

# "She doesn't look surprised, no doubt because the fact had dawned on her once she became sure of her decision, but rather, she appears genuinely unsure of how to deal with the situation now that it's in front of her."
"ลิลลี่ไม่ได้ดูตกใจเลย แน่แท้ว่าเธอคงรู้ว่าต้องเป็นอย่างนั้นมาตั้งแต่ตอนที่ตัดสินใจแล้ว ที่เธอเงียบไปเพราะไม่แน่ใจจริง ๆ\nว่าจะรับมือกับสถานการณ์ตรงหน้าตอนนี้อย่างไรดี"

show lilly basic_oops_cas_close
with charachange

# li "W-we could try pursuing a long-distance relationship. They're getting more and more common these days, after all…"
li "ระ เราจะลองคบกันทางไกลก็ได้นะ สมัยนี้คนที่คบกันทางไกลก็เริ่มมีเยอะขึ้นแล้ว…"

# "Even as she says it, the tone of her voice gives away that she doesn't truly believe what she's saying."
"ถึงจะพูดอย่างนั้น แต่น้ำเสียงก็บอกชัดว่าเธอไม่ได้เชื่อมั่นในสิ่งที่ตัวเองพูดเลย"

$ renpy.music.set_volume(0.5, 1.0, channel="music")
$ renpy.music.set_volume(0.05, 1.0, channel="ambient")

window hide
nvl clear
nvl show dissolve

# n "\n\n\nLilly is far too old-fashioned to be able to cope with a relationship without any kind of physical presence, and even I am, to an extent. All we would ever be to each other would be a voice from the other side of the world."
n "\n\n\nลิลลี่นั้นเป็นคนหัวโบราณเกินกว่าที่จะรับความสัมพันธ์ซึ่งไร้ตัวตนทางกายได้ และฉันก็เป็นคล้าย ๆ เธอด้วยเหมือนกัน\nเราจะเป็นได้เพียงแค่เสียงซึ่งดังมาจากคนละฟากโลกต่อกันเท่านั้น"

# n "In the end, trying to rationalize everything is futile. Any attempts to try and connect what's happening with the future or past just seem to get more difficult the more I concentrate." 
n "สุดท้ายแล้วการที่จะเอาความเป็นเหตุผลไปใส่กับทุกอย่างนั้นเปล่าประโยชน์ ยิ่งจดจ่อพยายามจะโยงสิ่งที่เกิดขึ้น\nในอนาคตหรืออดีตให้ถึงกันมากเท่าไหร่ก็ยิ่งเหมือนจะโยงไม่ได้มากเท่านั้น"

# n "Those quiet moments when we just walked side by side, the precious time we spent with Hanako and Akira, the casual chatter we had during lunchtimes, the times we made love, the confessions of our feelings to each other…"
n "ชั่วขณะอันเงียบงันที่เราเดินเคียงกันเหล่านั้น ช่วงเวลาอันล้ำค่าที่เราได้อยู่ด้วยกันกับฮานาโกะกับอากิระ บทสนทนา\nเรื่อยเปื่อยของเราตอนพักเที่ยง ช่วงเวลาที่เราแอบแนบชิดกาย คำสารภาพความรู้สึกของเราที่มีต่อกัน…"

# n "\n\n\nAll pointless. All just a fleeting moment in our young lives."
n "\n\n\nล้วนไร้ความหมาย ล้วนเป็นเพียงเสี้ยวขณะในช่วงชีวิตวัยรุ่นของพวกเราเท่านั้น"

$ renpy.music.set_volume(0.1, 1.0, channel="ambient")
$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear
window show

# hi "We're just two children pretending to be adults, aren't we?"
hi "เราสองคนมันก็แค่เด็กที่ทำตัวเป็นผู้ใหญ่เนอะ"

show lilly basic_sad_cas_close
with charachange

# "A long, long silence hangs in the air between us. The noise of the other patrons drinking and talking only makes the situation feel more strange and disconnected."
"ความเงียบลอยค้างอยู่ในอากาศระหว่างเราเนิ่นนานนานแสนนาน เสียงลูกค้าคนอื่นในร้านที่ดื่มกันคุยกันยิ่งทำให้\nสถานการณ์นั้นดูประหลาดและหลุดคลาดจากความเป็นจริง"

# "Lilly's face remains low, her dejected expression clouding it."
"ลิลลี่ยังคงก้มหน้างุดพร้อมสีหน้าอันหม่นหมอง"

stop music fadeout 4.0

show lilly basic_concerned_cas_close
with charachange

# li "I'm sorry, Hisao."
li "ฉันขอโทษ ฮิซาโอะ"

# "A simple apology, and no more. She's left entirely without any further response or comment."
"คำขอโทษสั้น ๆ ดาด ๆ และลิลลี่ก็ไม่ตอบสนองหรือพูดอะไรอีก"

# "With a long sigh, I gather what's left of my thoughts and ask the final question I have for her."
"ฉันถอนหายใจยืดยาวพลางค้นหาว่าในความคิดยังมีอะไรคงค้างอยู่ก่อนจะถามคำถามสุดท้ายกับเธอไป"

# hi "When will you be going?"
hi "จะไปเมื่อไหร่"

show lilly basic_sad_cas_close
with charachange

# li "I'll be leaving with Akira, so it'll be a little less than a week."
li "ฉันจะไปกับพี่ เพราะงั้นก็อีกไม่ถึงสัปดาห์"

# hi "The beginning of summer holidays?"
hi "ปิดเทอมฤดูร้อนวันแรก?"

show lilly basic_sleepy_cas_close
with charachange

# li "Just a little afterward, yes."
li "ประมาณนั้น แต่หลังจากนั้นอีกหน่อย"

# "Her tone is unusually slow and steady, her apologetic and depressed mood all the more written to her face as she tries to hide it in her voice."
"น้ำเสียงลิลลี่ราบเรียบและต่ำผิดวิสัย แม้เธอจะพยายามซ่อนความรู้สึกผิดและความเครียดไปจากน้ำเสียง แต่สีหน้า\nของเธอบอกอารมณ์เหล่านั้นเด่นชัด"

# "In the end, I can't even keep my promise of going to Tanabata with her before she leaves."
"สุดท้ายก็ไม่แม้แต่จะได้ไปงานทานาบาตะด้วยกันก่อนเธอไปอย่างที่สัญญาไว้ด้วยซ้ำ"

stop ambient fadeout 14.0
$ ksgallery_unlock("evul hisao_teacup")
show ev hisao_teacup:
    truecenter
    zoom 0.85 subpixel True
    acdc_warp 15.0 zoom 0.8
with locationchange

# "I look down, seeing my face reflected in the by now lukewarm cup of neglected tea sitting in front of me."
"ฉันก้มมองเงาตัวเองที่สะท้อนในผิวน้ำชาที่อยู่ตรงหน้าซึ่งถูกทิ้งไว้จนเริ่มเย็นลงแล้ว"

# "I really thought I'd left this kind of expression behind."
"ก็นึกว่าฉันทิ้งสีหน้าแบบนี้ไปแล้วเสียอีก"

# "For a while I just stare down into the still surface, trying to sort through my emotions to get at what course of action I should take, whether it be right now or in the future."
"ฉันนั่งจ้องผิวน้ำชาเรียบนิ่งอยู่ครู่หนึ่งพลางจัดแจงอารมณ์เรียบเรียงความคิดว่าตอนนี้และนับจากนี้ฉันควรทำอย่างไร"

# "But, just as before, the effort is wasted."
"แต่ความพยายามนั้นก็สูญเปล่าเช่นเคย"

hide ev
show lilly basic_reminisce_cas_close
with locationchange

# "I glance up to see Lilly gently sipping her cooled tea without complaint, her face drawn and shoulders slumped. She looks to be deep in thought too, a strangely cold atmosphere coming between us as we isolate ourselves to mull things over."
"พอเงยหน้ามองก็เห็นลิลลี่ที่จิบชาซึ่งเย็นแล้วอยู่นิ่ง ๆ ไม่พูดไม่จา เธอทำหน้าหมองพร้อมหย่อนไหล่ ดูท่าว่าจะกำลังคิด\nอะไรอยู่เหมือนกัน บรรยากาศเยือกเย็นพิลึกนี้คั่นระหว่างเราที่ต่างคนต่างปลีกตัวออกมาใคร่ครวญหลายสิ่งอย่าง"

# "Even as Lilly's cup slowly empties, mine remains untouched."
"น้ำชาของลิลลี่นั้นพร่องลงไปช้า ๆ ส่วนของฉันยังคงอยู่เช่นเดิม"

# "It's a long time before I notice the rain dying down outside and the few other patrons of the Shanghai having left."
"อีกพักใหญ่ฉันถึงรู้ตัวว่าฝนเริ่มซาลงและลูกค้าในร้านเซี่ยงไฮ้บางคนเริ่มออกจากร้านไปแล้ว"

scene bg school_dormhallway
with shorttimeskip

stop ambient
play music music_moonlight fadein 0.5

# "The chill of the rapidly darkening evening permeates the dormitory hallways. While trudging down the corridor to my room, I see an unwelcome movement from up ahead."
"อากาศเย็นจากยามค่ำซึ่งมืดลงอย่างรวดเร็วแทรกตัวไปทั่วโถงทางเดินในหอ ระหว่างที่เดินไปตามทางเพื่อกลับห้องก็เห็น\nอะไรบางอย่างที่ขยับอยู่ชวนให้นึกรำคาญ"

show kenji happy:
    center
    xpos 0.4
    easein 0.5 xpos 0.5
with charaenter

# "Sure enough, the opening of the door opposite mine heralds the arrival of a bespectacled Kenji."
"ตามคาด ประตูห้องตรงข้ามที่เปิดนั้นเป็นการป่าวร้องการมาถึงของเคนจิผู้สวมแว่น"

# ke "Hey man, what's…"
ke "ไงพวก สบา…"

show kenji tsun at center
with charachange

# ke "Woah dude, you look awful, I think. You okay?"
ke "โหพวก สภาพดูไม่ได้เลยนะ เหมือนจะนะ ไหวเปล่า"

# "He really has a knack for making any situation better."
"หมอนี่มันเก่งเรื่องการคลายบรรยากาศจริง ๆ"

# hi "I… don't really want to go into it. It's late."
hi "คือฉัน… ไม่อยากเล่าเท่าไหร่ ดึกแล้ว"

show kenji neutral
with charachange

# ke "Okay. That's cool."
ke "โอเค ไม่เป็นไร"

# ke "If you ever want to talk about it, I'm, you know, here."
ke "ถ้าอยากเล่า ฉันก็ เนี่ย จะอยู่เป็นเพื่อน"

# "I look at him for a moment before surrendering my stern front and awkwardly scratching the back of my neck, embarrassed by my standoffish response to him."
"ฉันมองเคนจิอยู่ครู่หนึ่งก่อนจะเลิกทำท่าเคร่งเครียดแล้วเกาท้ายทอยแก้เก้อเพราะอายที่ตอบไปแบบทื่อ ๆ"

# hi "Thanks, Kenji."
hi "ขอบใจนะเคนจิ"

show kenji happy
with charachange

# ke "Hey, it's cool. That's what friends are for, right?"
ke "เออ ๆ ไม่เป็นไร เพื่อนกันก็ต้องงี้อยู่แล้วเปล่า"

# hi "Yeah, you're right. Um, seeya."
hi "เออ ถูกของนาย เอ่อ เจอกัน"

scene bg school_dormhisao_ni
with locationchange

# "I open the door to my own dorm room and close it behind me as he quickly waves me off."
"ฉันเปิดประตูเข้าห้องตัวเองแล้วปิดประตูให้กับเคนจิที่โบกมือลา"

play sound sfx_doorslam

# "The solid thud the door makes against the door frame sounds out a final call for the life I've led since coming to Yamaku."
"เสียงประตูกระทบกับวงกบดังปึงเป็นสัญญาณบอกว่าชีวิตที่ฉันเคยใช้มาตั้งแต่ได้มาอยู่ที่ยามากุใกล้สิ้นสุดลงแล้ว"

# "I just stand in my darkened room, fruitlessly attempting to work out what I should do from this point onwards."
"ฉันยืนอยู่ในห้องมืดมิด ตะเกียกตะกายในความคิดค้นหาว่าฉันควรทำอย่างไรต่อจากนี้"

# "Just what should I do…?"
"แล้วฉันจะต้องทำยังไงกัน…"

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
stop music fadeout 2.0

scene black
with dissolve

#********************

label th_L29:

scene bg school_scienceroom
with locationchange

"As class ends, I simply rest my head on my hand and stare out of the window to pass the time."

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_normal fadein 2.0

window hide
nvl clear
nvl show dissolve

n "\n\nIt's been a few days since Lilly told me her plans. I haven't been to our ordinary lunchtime haunt since then, not that there would be much point."

n "Hanako's been busy with the newspaper club she's newly joined, and has even begun talking in class with Naomi every now and then."

n "Even Lilly, aside from the fact that a meeting between us would've been awkward in any case, has been run off her feet with class representative duties as the summer holidays approach."

n "And now, they're just about here. With the end of today's bell, the summer holidays will have begun."

n "\n\n\nI suppose that all I'll end up doing will be visiting my parents for the duration and lazing about my old home, now that my previous plans are entirely askew."

nvl clear

n "\n\nMeanwhile, Akira and Lilly will be en route to Scotland, to live out the rest of their lives there."

n "No matter how hard I try to rationalize the idea that once the summer holidays begin, my life will return to the way it was, it simply refuses to happen."

n "Everyone's moving on with their lives. Lilly's rejoining her family, Akira's moving up in her father's business, Hanako's gaining new friends and hobbies, and even Yuuko's moving ahead with her university aspirations."

n "Even I'm moving forward, in the end. With the grades I've gotten so far in Yamaku, much less after such a rocky beginning, the path to get into teaching science as a career seems straightforward."

n "\n\nI suppose I should at least be happy about that much, but it doesn't really seem to help."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

window show

mi "Hicchan~!"

"I quickly stop my ruminating and turn to face the bubbly voice beside me, putting on the most upbeat expression I can muster."

show misha hips_smile at twoleft
show shizu behind_smile at tworight
with charaenter

"As expected, Shizune stands flanking her. I have a sneaking suspicion they want something from me."

hi "Hey Misha, Shizune. What's up?"

show misha hips_grin
with charachange

mi "Well~…"

show misha perky_smile
with charachange

mi "Shicchan and I were thinking~…"

show misha sign_smile
with charachange

mi "Since we're just two poor little girls that need help with all the work we've been given just before the holidays begin~…"

hi "Sure, I can help."

show misha perky_sad
with charachange

mi "But Hicchan, we're really nee—"

stop music fadeout 0.2

show misha perky_confused
with charachange

mi "What?"

"I think I broke Misha."

show shizu behind_blank
with charachange

"Even Shizune raises an eyebrow at her accomplice's shuddering stop in her tracks."

show misha hips_grin
with charachange

mi "So you'll help us, Hicchan?"

hi "I just said I would, didn't I?"

"It's hardly like I have anything better to do. Maybe helping them with their work will help take my mind off the situation."

"Misha seems genuinely ecstatic with my response, but Shizune's expression is clouded and difficult to read. I find myself quickly averting my eyes from her own, as it almost looks like a face of pity. No doubt, it must just be my imagination."

scene bg school_council
with shorttimeskip

play music music_daily fadein 0.5

"This is hardly the first time I've been in the student council room. Indeed, I've found myself down here often, either to help Lilly with class rep work, or to sort out one thing or another with the Student Council itself."

"Now, though, it's quite a different place."

show sc_comp:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

"Papers and folders are strewn across every table in the room, only a solitary little black laptop atop a single desk sticking out from the mess."

"It looks positively ancient, and I'd guess it has been valiantly serving its task in archiving information for years and years."

show sc_comp:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide sc_comp
with None

hi "So, what needs doing? This looks like a lot to do."

show misha hips_smile at twoleft
show shizu  behind_frown at tworight
with charaenter

shi "…"

"Shizune's expression becomes determined as she signs. It's a worrying look."

show misha hips_grin
with charachange

mi "Everything, Hicchan!"

"My worry was well placed."

hi "Everything… you say?"

show shizu basic_normal
with charachange

shi "…"

show misha sign_smile
with charachange

mi "What's left on the desks is what needs to be done."

show misha perky_smile
with charachange

mi "It all needs to be digitally recorded, which is what the laptop is for."

hi "And I'm guessing that I'll be the one doing this?"

show shizu behind_smile
with charachange

shi "…"

show misha hips_smile
with charachange

mi "Shicchan says she saw you with the computers in the library a few days ago, and that you seemed really good with them~."

"Good with computers? I can touch-type, I guess, but it still seems like an overestimation of my skills."

hi "I was just typing up homework…"

hi "Wait, Shizune was watching me do that?"

show shizu adjust_smug
with charachange

shi "…"

show misha sign_smile
with charachange

mi "One must know their allies before they can know their enemies, of course~."

show misha cross_grin
with charachange

mi "Wow, that's pretty wise…"

"For once, it's not very hard to work out who said what."

"Nonetheless, it doesn't seem worth fighting over. Sitting at a computer doing some typing hardly seems onerous, as far as tasks to help Shizune and Misha go."

show shizu basic_normal
with charachange

shi "…"

show misha perky_smile
with charachange

mi "Besides, it will help to take your mind off things~."

hi "Take my mind off things? Take my mind off what things?"

show misha perky_confused
with charachange

"Misha's face goes blank as she translates this for Shizune, though the latter's response is only to glance away towards the window after briefly signing."

show shizu behind_blank
with charachange

shi "…"

show misha sign_smile
with charachange

show shizu basic_normal2
with charachange

"Misha's face quickly returns to a smile as she translates back. She was confused, I guess, but Shizune is harder to pin down."

show misha cross_smile
with charachange

mi "I was just thinking you may like to get your mind off the exams, of course~."

hi "Either way, we may as well get into it sooner rather than later. I'll go along with you."

show misha hips_smile
with charachange

mi "That's the spirit, Hicchan~!"

#hi "Even if it is, I don't really see how we're going to get all this done in one lunchtime."

#show misha hips_grin
#with charachange

#mi "Oh, that? We have next period off. Once we finish we can go home for the holidays~."

#hi "You managed to get off last period? But that's when all the students will be helping to pack up the tables and chairs for the term."

#show misha sign_smile
#with charachange

#show shizu behind_smile
#with charachange

#"As Misha translates what I say, Shizune proudly puffs her chest and gives a victorious beaming grin. It makes me wonder just how much leverage she has over our teachers."

#"I feel somewhat guilty over this, but we are going to be doing work of some kind, after all."

scene bg school_council
with shorttimeskip

"And that's the fifth spreadsheet compiled and saved. Time for the next month's…"

"After a little bit of fussing around, we all managed to get a bit more organized."

"Shizune's been gathering up the loose sheets and, thankfully, sorting them into a neat pile next to me. Meanwhile, Misha's been handling the manual writing work, her girly pink pen leaving its unmistakable mark on paper after paper."

"Once I got myself into a rhythm, this really wasn't so bad. Shizune and Misha also seem to be in the swing of things, wordlessly communicating as they go about their business with fervor."

"I periodically glance at the sheet beside the laptop, apparently a list of student names and matching addresses, as I dutifully enter the data written on it. I don't pay a lot of attention to what I'm typing in until I reach about midway down the page."

"Hakamichi… class 3-3… Huh. Her family's home is in Saitama."

"My idle curiosity is ended abruptly as three light taps can be heard rapping on the door."

show misha perky_smile:
    twoleft
    xpos 0.4
    easein 0.5 twoleft
with charaenter

"Misha quickly skips over to check who it is, tapping Shizune's shoulder on the way past to let her companion know what's happening."

show misha hips_grin at twoleft
with charachange

mi "Ah, you're here~."

hi "Hmm? Who is it?"

"With a slight pause to enter Shizune's data into the file along with all the others, I look up to check who's at the door."

stop music fadeout 0.5

show lilly invis:
    left
    xpos -0.2
with None

show bg school_council at bgright
show misha hips_grin at center
show lilly basic_weaksmile_cas at left
with dissolvecharamove

"…Lilly?"

"After giving a cursory nod to Misha in greeting, she perks her head up in her trademark manner."

show lilly basic_surprised_cas
with charachange

li "Is that Hisao?"

"She's pretty darned good at working out my voice from the smallest of phrases nowadays."

hi "Yeah, it's me. Um… hey."

show lilly basic_reminisce_cas
with charachange

"The atmosphere feels slightly awkward as she bows. Neither of us knows quite how intimate we should be around each other, given she's leaving in just a matter of hours."

"This is a fact that, thankfully, neither the oblivious Misha nor the hardworking Shizune pick up on."

hi "So… you've got work to do as well?"

show lilly basic_sleepy_cas
with charachange

li "Unfortunately. I arrived as soon as I could, but my class held me up with a surprise farewell party, and I had to get changed."

"I glance down at the laptop's clock. It's pretty much the end of lunchtime, so I'm guessing Lilly managed to wrangle the last period off as well."

show lilly basic_weaksmile_cas
with charachange

li "I take it Shizune is here as well?"

play music music_shizune fadein 3.0

show shizu behind_blank at right
with charaenter

shi "…"

show misha cross_smile
with charachange

mi "Of course!"

show shizu adjust_smug at right
with charachange

shi "…"

show misha sign_smile
with charachange

mi "And I've been here during all of lunchtime as well!"

"That last comment was really not needed. Shizune's baiting Lilly into another argument, I can feel it."

show lilly basic_displeased_cas
with charachange

li "I'm sorry I can't be as hardworking as you, Shizune. I'll endeavor to hire more lackeys to do my work in future, I assure you."

"And Lilly just took the bait, escalating things further."

show shizu basic_frown
with charachange

shi "…"

show misha hips_frown
with charachange

mi "But aren't you the one always outsourcing work to your classmates~?"

show lilly basic_listen_cas
with charachange

li "The difference is that they choose to help, unlike your tyrannical grip on your own class."

show shizu behind_frown
with charachange

shi "…"

show misha cross_smile
with charachange

mi "Tyranny works~! Even if we did things differently, we still got the same results, right~?"

show lilly basic_displeased_cas
with charachange

li "This is school, not a police state. You will have to remind me when you were appointed class monarch, I'm afraid."

show shizu cross_angry
with charachange

shi "…"

show misha cross_frown
with charachange

mi "You have to seize power, it's not as good if it's just handed to you~! But I guess you wouldn't really understand that, right~?"

show shizu adjust_angry
with charachange

shi "…"

show misha hips_smile
with charachange

mi "You'll also have to remind me when monarchs were elected into their positions~."

"Lilly positively bristles at this. Shizune's two-hit combo forces her onto defense."

show lilly basic_displeased_cas
with charachange

li "Yet for all your vaunted power, you cannot get one person to help you without forcing him."

show shizu behind_frustrated
with charachange

shi "…"

show misha sign_smile
with charachange

mi "But Hisao volunteered~! He's such a hard worker, he's doing this instead of meaningless socialization, right~?"

show lilly basic_listen_cas
with charachange

li "Is that so. Hisao?"

"Ah, this is bad. I've really ended up between a rock and a hard place."

"As much as it may pain me to do this, the truth has at least a chance of stopping this argument here and now."

hi "It's okay, Lilly, they didn't harass me to come or anything."

show lilly basic_displeased_cas
with charachange

"Lilly gives me a disapproving grimace, silently radiating her strong feelings of displeasure in my general direction."

"She can be quite scary when she wants to be, though thankfully that isn't often."

show shizu cross_angry
with charachange

shi "…"

show misha hips_frown
with charachange

mi "Hicchan, you make that sound like it's a regular occurrence~…"

hi "It isn't?"

hi "In the end, it doesn't matter so long as everything's getting done at a good pace. Let's just get this work over with so we can go home."

hide shizu
with charaexit

hide lilly
with charaexit

hide misha
with charaexit

"Shizune snorts derisively and gets back to marking off the sheet in front of her, while Lilly sighs and finds her way along the room with her hand following the filing cabinets lined along the wall."

"This would mark the only time I've managed to successfully defuse one of these situations, but the grudging ceasefire built around mutual fear and respect makes this feel more like the Cold War than any real peace."

"I can't take all the credit though; Lilly's leaving has surely affected Shizune to some extent, to make her give up so easily."

show bg school_council at center
with charamove

show lilly basic_listen_cas at center
with charaenter

"Moments before getting back to my work, I notice Lilly reaching up to grab something from above a filing cabinet. I almost offer to help, but her height gives her ample ability to take it down safely."

show lilly basic_displeased_cas:
    ypos 1.15
with dissolvecharamove

"Once she sets the strangely shaped device on the desk beside me, I realize just what it is… sort of… as she takes the old green covering off and sits down."

show brailler:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

"At first glance it seems to be an old metallic blue typewriter, but it doesn't take me long to realize it's far from ordinary."

"It has far fewer keys than expected, and those it has show no lettering printed on them. Only the shadows cast by the tiny Braille dots on them give a hint to the thing's purpose."

hi "Blind typewriter?"

show lilly basic_smile_cas
with None 

show brailler:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide brailler
with None

li "Oh, this? Well, you're not far off."

li "It's normally called a Perkins Brailler, but it's basically a typewriter for the blind, yes. It presses Braille into the page rather than text, which is why it has fewer keys."

hi "Huh… that's really neat."

show lilly basic_cheerful_cas
with charachange

"She gives a lighthearted grin at my curiosity over it. I have to admit that it appeals to my sense of novelty."

hide lilly
with charaexit

"Without further ado, we each get back to our allotted tasks. The loud clunking of the mechanics in Lilly's Brailler and the tapping of the laptop's old and weary keyboard quickly fill the room."

"It's a nice atmosphere, really. Everyone knows what they have to do, and Lilly and I get to sit beside each other and exchange the odd word as we work away."

"Nostalgic. That's what it feels like."

"It's pleasant, but just slightly stained with the knowledge that our time together is nearing its end."

show lilly basic_smile_cas:
    center
    ypos 1.15
with charaenter

li "Excuse me, Misha?"

show bg school_council at bgleft
show lilly basic_smile_cas:
    twoleft
    ypos 1.15
with charamove

show misha hips_smile at tworight
with charaenter

"To properly address her, Misha bounces over from the filing cabinet she's peering into, in spite of Lilly's lack of sight. For a moment I think it strange, but then realize it's exactly what I do."

mi "What's up?"

show lilly basic_weaksmile_cas
with charachange

li "Could you ask Shizune where the attendance records for class 3-2 are? I think they've been moved."

show misha hips_grin
with charachange

mi "Okie dokie!"

hide misha
with charaexit

stop music fadeout 8.0

"And with that, she flitters off to Shizune, who's working at a table behind us."

"Lilly's familiarity with the council room, and the efficiency with which she works, remind me that she, Misha and Shizune used to all work together in the Student Council."

"Maybe this is a fitting end for her stay in Yamaku; working away just like she used to, surrounded by those she loves and, at least, liked."

"I look up, getting taken off-guard by Shizune sorting through a drawer, rather than Misha."

show shizu behind_blank at tworight
with charaenter

"Sure enough, she plucks out a manila folder, entirely blank save for the just barely visible bumps on its front, and holds it in front of Lilly."

"Lilly's hand flits over it to check what it is, her fingers feeling out the dots of Braille and confirming it's what she asked for."

show lilly basic_smile_cas
with charachange

li "Thank you, Misha."

"No reply."

show shizu behind_smile
with charachange

"No reply, that is, save for an odd grin… no… smile… on Shizune's face."

show ev lilly_sheets:
    truecenter
    zoom 1.05 subpixel True
    easein 10.0 zoom 1.0
with whiteout

"A couple of seconds pass before Lilly clicks that it isn't Misha behind her, but Shizune. Her momentary look of surprise is replaced by a slightly bashful smile."

"For a few moments, the room is all but still and silent."

"Eventually, though, Shizune strides back to her workstation and Lilly begins typing once again."

"It only lasted a handful of seconds in all, but it feels like years of communication were made up for in that one silent exchange."

scene bg school_council_ss at right
with shorttimeskip

play music music_tranquil fadein 3.0

hi "There, finished."

"I lean my head back and rub my eyes to try and work away their weariness. Staring at that small and rather poor screen has taken its toll."

show lilly basic_smile_cas_ss:
    center
    ypos 1.15
with charaenter

li "Excellent timing; the only thing left is to file these away and I'll have my workload finished as well."

hi "Good. I can pack up the Brailler and put it away while you do that."

show lilly basic_smileclosed_cas_ss
with charachange

li "Thank you, Hisao."

hi "Misha, are you and Shizune far from being done?"

"I look around for the two as I replace the cover over the Brailler, only to see them waiting at the door. I guess they must be waiting for us."

scene bg school_council_ss at left
show misha hips_smile_ss at center
show shizu behind_blank_ss at right
show lilly basic_smileclosed_cas_ss at left
with shorttimeskip

"With a minimum of wasted time, we file and pack up everything that remains and join them."

hi "Thanks for waiting, you two."

show misha hips_grin_ss
with charachange

mi "We couldn't just take off without you, Hicchan, you've been a great help!"

show shizu behind_smile_ss
with charachange

"Shizune nods approvingly, pleased with my efforts."

hi "I guess… that's the last class representative work done and over with, then."

show lilly basic_smile_cas_ss
with charachange

li "That's right."

show misha perky_sad_ss
with charachange

mi "I'll miss you, Lilly. I think it was fun working with you."

show lilly basic_weaksmile_cas_ss
with charachange

li "Thank you, Misha. It's been good working with you… and Shizune."

show shizu basic_normal_ss
with charachange

"Shizune thinks for a moment before formulating her response. It's not that she often communicates without thinking, quite the opposite, but this time it's even more considered than usual."

show shizu adjust_smug_ss
with charachange

shi "…"

show misha perky_confused_ss
with charachange

"Misha looks a little surprised before passing on the message."

show misha hips_smile_ss
with charachange

mi "Shizune says… you'd better do your work over there better than you did it here."

show lilly basic_giggle_cas_ss
with charachange

"Far from taking offense, Lilly giggles into her hand."

show lilly basic_smileclosed_cas_ss
with charachange

li "If that's the case, then please tell Shizune to give those still here a little more understanding in the future."

"Competitive until the last. Maybe Shizune and Lilly aren't so different after all."

show shizu behind_smile_ss
with charachange

shi "…"

show misha hips_grin_ss
with charachange

mi "Shicchan says that she'll be checking to make sure you live up to your end of the promise."

show lilly basic_cheerful_cas_ss
with charachange

li "Then that's how it will be."

show lilly basic_smile_cas_ss
with charachange

li "I'd better be off, then. Goodbye, Shizune. Goodbye, Misha."

show lilly basic_smileclosed_cas_close_ss
with characlose

li "Hisao?"

"Lilly takes a hold of my arm in hers, there being no need for a cane if I'm here to guide her. With a nod of farewell to the two, we set off out the door and make our way to the school grounds."

"As I turn to wave goodbye to them, I notice Shizune's gaze lingering on Lilly. They may annoy each other, but family bonds aren't easily broken."

scene bg school_courtyard_ss
with locationskip

hi "Got all your papers sorted, then?"

show lilly basic_smileclosed_cas_ss at center
with charaenter

li "Yes, they've all been filled out and handed in."

hi "On top of things as always, aren't you?"

show lilly basic_weaksmile_cas_ss
with charachange

stop music fadeout 4.0

"She gives an earnest smile at the compliment, but it feels as if her happiness is just a veneer over the fact that she's fully aware of how much she's leaving behind."

"It reminds me of how she was like when I first met her; always smiling, always that little bit aloof, always that little distance away from everybody."

"Even now, she still maintains that air around many others, especially those she's not close to. I had hoped that our time together would have changed that fact."

scene bg school_gardens_ss
with locationchange

"Our pace slows, the two of us coming to a halt in the all but empty school gardens."

show lilly basic_weaksmile_cas_ss at center
with charaenter

li "Hisao? Is something the…"

play music music_comfort

show lilly basic_surprised_cas_close_ss
with vpunch

"Lilly's words are cut short as I turn and wrap my arms around her, pulling her tight. I may not usually be given to such impulsive actions, but I just want to be close to her, even if it's the last time I'll be able to."

"All the other students have retreated to their dormitories and homes, only the ruffling of leaves in the breeze making any sound whatsoever."

show ev lilly_touch_cas
with charachange

"As I draw back, I can see she has dropped her carefully maintained smile."

"Her hand hesitates, wanting neither to leave nor to stay on my features."

"She is putting up a brave show, but her slight trembling gives her away. Lilly may be able to control herself well, but even she can't hold her composure together now."

"This is the woman I've come to love, but also the one who in all too short a time will leave the country forever."

li "I'm sorry, Hisao."

hi "It's okay. You've got your own life to lead, after all."

scene bg school_girlsdormhall
with shorttimeskip

"We walk up the hallway in the girls' dormitory hand in hand, our emotions by now largely quelled. Nevertheless, our hands grip each other's much more tightly than before."

"Faint, muffled voices can be heard from Lilly's room, the origins of which aren't difficult to guess."

scene bg school_dormlilly

show hanako invis at tworight
show lilly invis at twoleft
with locationchange

show lilly basic_weaksmile_cas at twoleft
show hanako emb_downsad:
    xpos 0.4 xanchor 0.5
with dissolvecharamove

show lilly basic_surprised_cas
with vpunch

"The moment she opens the door, Hanako bursts through and wraps her arms around Lilly, taking her very obviously by surprise."

ha "Lilly! Lilly!"

show lilly basic_oops_cas
with charachange

li "Ha-Hanako…?"

show hanako emb_downtimid
with charachange

ha "I'm going to miss you… Lilly…"

show lilly basic_weaksmile_cas
with charachange

"As expected, she's on the verge of tears. Lilly gently rubs Hanako's hair with her hand in response, then pulls back and gives a warm, reassuring smile."

show akira invis:
    right
    ypos 1.15
with None

show akira basic_lost at right
with dissolvecharamove

"Looking beyond Hanako, Akira can be seen getting up from the side of Lilly's bed and scratching her head."

show akira basic_smile
with charachange

"Her eyes turn from Lilly and Hanako to me, a stilted, weak smile hanging on her face. I try to return a more genuinely happy look, but the result is probably just the same."

show akira basic_boo
with charachange

aki "So, everything set? Managed to hold back from killing Shizune?"

show lilly basic_giggle_cas
with charachange

"The comment draws an amused giggle from her sister."

li "Yes, I have everything in order, and yes, I managed not to. Have you packed everything you need?"

show akira basic_smile
with charachange

aki "Got the two bags right here, but there's still some stuff left at the Hakamichis' home. I can pick that up while we wait there for tomorrow evening's flight, though."

"Akira gives the two large black traveling bags on the floor a hearty pat. She probably came to help pack and make sure everything was in order on Lilly's end, before going together with her."

show hanako cover_worry at center
with dissolvecharamove

ha "Lilly… will you be okay… over there?"

show lilly basic_smileclosed_cas
with charachange

li "I'll be all right, I assure you. I'll have Akira looking after me as well, and you know that she's reliable."

show hanako basic_worry
with charachange

ha "But…"

show lilly basic_smile_cas
with charachange

li "Don't worry, Hanako. I have your phone number after all, so we can stay in touch. With Akira's help, I could send you things over the Internet as well."

show akira basic_boo
with charachange

aki "Hey, don't use me just because you won't learn how to use a computer."

show lilly basic_giggle_cas
show hanako basic_smile
with charachange

"Hanako and Lilly both giggle briefly, the mood lightening ever so little."

show lilly basic_smileclosed_cas
with charachange

li "That goes for you too though, Hisao. I promise I'll contact you once I'm in Scotland."

hi "I know. I'll be looking forward to it."

"Her offer may be kind, but we both know that this is tantamount to breaking up. Neither of us has any illusions as to how well we'd manage a long-distance relationship."

"With nary a word of prompting, the four of us begin the long, solemn walk to the school gate."

scene bg school_gate_ni at bgleft
with shorttimeskip

"The numerous lamps scattered around the Yamaku grounds fail to do much more than provide pinpoints of light in an otherwise dense darkness."

"A car parked on the road just outside the school grounds comes into view, its shining black exterior reflecting the dimly lit lamps of Yamaku. I call out to Akira in an effort to alleviate a bit the heavy atmosphere."

hi "That your car? What kind is it?"

show akira basic_smile_ni at center
with charaenter

aki "Don't know much about cars, do you? It's a Lancer Evo. Solid and speedy."

"Well, it's not as if her comment on my knowledge is off the mark. I've never really taken an interest in them."

show akira basic_resigned_ni
with charachange

"She gives a small sigh."

show akira basic_lost_ni
with charachange

aki "She's been good. Pity I have to part with it tomorrow, just like the summerhouse. You guys were the last to visit it before it changed hands."

"Turning back from my rather faulty attempt at smalltalk, I glance at Hanako and Lilly, following behind us."

show akira basic_lost_ni at tworight
show bg school_gate_ni at center
with charamove

show hanako emb_downtimid_ni:
    xpos 0.4 xanchor 0.5
show lilly basic_weaksmile_cas_ni at twoleft
with charaenter

"By rights, Hanako should be leading Lilly, but it's rather definitely the other way around as she clings tightly to Lilly's arm."

"It's a depressing sight."

show akira basic_resigned_ni
with charachange

aki "So… I guess this is it."

show lilly basic_reminisce_cas_ni
with charachange

li "Indeed."

"Although the time for everyone to say their farewells is now, nobody really wants to take the first step. It's as if the longer nobody speaks, the better the chances of them simply not leaving."

show hanako emb_downsad_ni
with charachange

ha "Lilly… do you really have to go?"

show lilly basic_concerned_cas_ni
with charachange

li "I'm sorry, Hanako. I won't be leaving you forever, though; I can still call you. Hisao will still be here as well."

"I nod, but Hanako just clutches all the tighter to Lilly's arm."

"After spending so long without anyone to call family, it must be excruciating to have to say goodbye to the one person that was as close to a mother as anyone could have been in her life."

show lilly basic_sad_cas_ni
with charachange

"Lilly lets out a long, sad breath. All Akira and I can really do is stand by quietly on the sidelines, since the only person that can solve this would be Lilly herself."

"Eventually, Lilly pulls her arm from Hanako's grip and holds both of her shoulders gently, a much more decisive way of address than I've ever seen Lilly take with her."

show lilly basic_reminisce_cas_ni
with charachange

li "Hanako, remember when we first met?"

show lilly basic_weaksmile_cas_ni
with charachange

li "When you entered my room for the first time after overhearing my consoling of a friend, you didn't say a single word for the entire night. Even as I poured you tea and talked, you sat silently and simply listened to what I said."

li "It took many quiet meetings like that before you began to open up to me, but as you began to, I felt some of the happiest moments I've ever felt."

show lilly basic_sleepy_cas_ni
with charachange

li "I didn't become your friend because I pitied you, Hanako. I became your friend because I knew you were hiding not just from me, but from everyone."

li "Your ambitions, personality, interests, tastes… I didn't know any of them, and neither did anybody else."

show lilly basic_weaksmile_cas_ni
with charachange

li "As you showed yourself to me though, I began to realize the person that you were, and became sure that our meeting was a very special moment."

show hanako emb_blushtimid_ni
with charachange

ha "But I…"

"Lilly cuts her words short as she brings her hand to Hanako's head and brushes her bangs to the side, gently pressing her lips to Hanako's forehead."

show lilly basic_smile_cas_ni
with charachange

"As she pulls her head back, leaving Hanako all but speechless and her eyes moist, Lilly beams a wide smile."

li "I believe you are a very beautiful person, Hanako, and I am certain that you will become a strong and confident woman."

li "You are a very dear friend, and someone whom I love very much. Just like Hisao, I will never forget you for as long as I live."

show lilly basic_smileclosed_cas_ni
with charachange

li "I may be leaving, but you have your own life here to lead. Just as I do, you have your own friends and hobbies, and your own hopes after graduation. I want you to devote yourself to them, even after I'm not around any more."

show lilly basic_smile_cas_ni
with charachange

li "That is why I think you will be okay. Because you are your own self, with your own life. You yourself proved that to me."

show hanako emb_downtimid_ni
with charachange

"Hanako lowers her head in embarrassment, but nods as she does so."

ha "I… I understand…"

ha "I know I have to say goodbye… I know you have to go your own way…"

show hanako emb_smile_ni
with charachange

ha "But… thank you, Lilly. For everything."

show lilly basic_reminisce_cas_ni
with charachange

li "Thank you, Hanako. Will you be okay?"

"There are a few seconds of silence before the answer comes."

show hanako cover_smile_ni
with charachange

ha "I will."

show lilly basic_smile_cas_ni
with charachange

"Lilly smiles, undoubtedly at least partly in relief."

show lilly basic_smileclosed_cas_ni
with charachange

li "That makes me very happy, then. Goodbye."

show hanako basic_bashful_ni
with charachange

ha "Goodbye… Lilly."

show lilly basic_weaksmile_cas_ni
with charachange

li "And farewell to you as well, Hisao."

hi "Goodbye. I'll miss you."

show lilly basic_weaksmile_cas_close_ni
with characlose

"She pauses for a moment before walking up to me. Her right hand, outstretched in front of her, takes a hold of my shoulder."

"Her left hand slowly and daintily reaches towards my face, taking my cheek in her palm."

show lilly basic_smile_cas_close_ni
with charachange

"For a while she simply holds my face, her fingers just slightly moving to take in its contours. Usually her hand would be warm when doing such a thing, but the night air's given her skin a cool edge."

"I'm not sure how long we stay like this, her clouded eyes pointed just below my own as she wears a wistful, almost distant smile. Eventually, though, I take her cold hand in mine."

"It's difficult to do so, but with a slight sigh I gently remove her hand from my cheek."

hi "I hope you have a long and happy life, Lilly, no matter where you might go."

show lilly basic_weaksmile_cas_close_ni
with charachange

li "Thank you. I'll make sure to."

"She takes a long, trembling breath before turning slightly towards Akira's direction."

show lilly back_sad_cas_close_ni at twoleft
with charachange

li "Akira…"

show akira basic_lost_ni
with charachange

aki "Okay."

show hanako basic_bashful_ni at left
show lilly back_sad_cas_ni at center
show bg school_gate_ni at right
with dissolvecharamove

"With a nod, she takes Lilly's hand and begins to guide her to the car parked outside the gates. They both walk slowly and deliberately, as if their movements had been rehearsed in advance."

"It's strange to feel like this now, watching somebody leave Yamaku. The feeling of unease I have now reminds me of the first time I walked through those black wrought iron gates, that always looked far too pompous for what they were."

"As they leave, all of us know full well that our lives are irreversibly changing. I'd always told myself that I just have to take life as it comes, but everything's changing so fast, so suddenly."

"In the end, Lilly's an irreplaceable part of the lives of both Hanako and me."

"The noise of Akira opening the passenger door for Lilly brings me out of my thoughts, her hand waving back as Lilly gets in."

show akira basic_smile_ni
with charachange

aki "Seeya guys! Take care of yourselves!"

show lilly basic_weaksmile_cas_ni
with charachange

li "Goodbye Hanako, goodbye Hisao!"

show hanako cover_smile_ni
with charachange

"Hanako's hand quickly shoots up, her face brightened by her enthusiastic farewell."

ha "Goodbye Lilly! Goodbye!"

hi "See you, Akira, and goodbye Lilly!"

hide lilly
hide akira
with charaexit

"The door shuts as we all put on our best happy farewell faces, Akira getting in the car herself and starting it up in short measure."

"Lilly's hand can just be seen waving through the tinted windows, both of our hands waving high as well."

"Just as every other time I've done such things, I can't quite work out precisely why I, or Hanako, wave to her given that she'd never see us doing so. But it doesn't matter."

"Even after that black, shiny car goes down the hill and disappears into the dark night, we carry on waving and seeing Akira and Lilly off."

stop music fadeout 5.0

"And then… they're gone."

show bg school_gate_ni at center
show hanako basic_normal_ni at center
with dissolvecharamove

"A strange stillness takes over as our hands return to our sides."

"I don't quite know what I should do or how I should feel. In the end, we just stand there silently staring down at where the car disappeared from sight."

ha "Goodbye… Lilly."

show hanako basic_normal_close_ni
with characlose

"All I can do in response to her quiet, mournful goodbye is to place a hand on her shoulder."

show hanako basic_distant_close_ni
with charachange

"She looks at me for a few moments before looking back down the hill, secure in the knowledge that I'm still around for her."

"What we'll do from now doesn't seem all that uncertain. We all have our own ambitions now, just as Lilly said."

"But even so, it feels like there's a certain missing part in both of our lives now. Something that can never be replaced."

# Bad End means the path ends here
window hide Dissolve(1.0)
$ suppress_window_before_timeskip = True

scene black
with Dissolve(2.0)

#********************************

label th_L30:

# This scene onwards is only seen if the player tripped all three +1 Good End choices

scene bg school_hallway2
with locationchange

play music music_daily fadein 1.0

"The snap of my mobile phone's closing contrasts with the ambient chatter and noise audible even in the hallway outside the library."

"It's the first day of the summer holidays. A time that had perpetually seemed so far away, and yet it's now not only here but also made painfully obvious by the students, or lack thereof, left in the school."

"Most students have returned home to spend the holidays with relatives by now. The few that are left are mostly chatting between themselves, usually about what they intend to do in the coming weeks."

"It makes me feel like the odd one out, for taking advantage of the school library being open for the first several days of the holidays."

"Ostensibly it's for students to drop off any books they've borrowed and have yet to return, and for those who'll have their parents pick them up, to help pass the time until they get whisked away."

"Thanks to the recent lengthy phone call from my parents, which had so rudely woken me from my sleeping on a beanbag at the back of the library, I'm now in the latter category."

"Sliding my phone back into my pocket, this time remembering to set it to silent, I go back into the quiet and wholly placid room."

scene bg school_library_ss
with locationchange

"It's a nostalgic sight. Just as when Lilly first led me to the library, the orange tint of sunset bathes the room in its light while Hanako sits on a beanbag silently reading and Yuuko fusses, just barely visible behind the counter."

"Hanako especially has been noticeably more quiet than usual since yesterday's happenings, but I can't really blame her."

"It wasn't just me that depended on that person, after all."

"I quietly walk back to the beanbag near her where I'd sat before, being doubly careful not to make any unnecessary noise."

scene ev hana_library
with locationchange

show ev hana_library_read
with charachange

"The soft puff it gives as the bag takes my weight makes Hanako's eyes flick towards me, but only for a second."

"I get the feeling that Hanako's been quiet only partly out of sadness following Lilly's departure."

"Rather, she seems more thoughtful and measured than I'd expected; perhaps due to her desire of working out how to deal with Lilly's leaving rather than just being depressed over it. It makes me a little proud of her."

hi "Hey, Hanako?"

show ev hana_library
with charachange

ha "Y-yeah?"

hi "Still going ahead with your idea of traveling?"

"She gives a determined nod."

ha "I'll be starting in a day or two. Naomi's decided to come with me, too."

hi "Wow, quick start. Where're you two headed to first?"

ha "I think we're going to start by going north… then loop down and go southward."

hi "So… Hokkaido's going to be first?"

"She gives another nod, more tentative than the last. The significance of that place is not lost on either of us."

hi "Do you know how you're going to handle the traveling expenses and accommodations?"

ha "Yeah, I've worked everything out. I think it should be okay. Naomi says she has her side worked out, too."

hi "You know that if you need anything you can just call, right? I gave you my number before. Any time of the day is fine."

show ev hana_library_smile
with charachange

"She gives a smile, which in itself feels like a small personal victory."

ha "I know."

ha "Th-thanks… Hisao."

"Maybe Lilly was right. Although I may offer Hanako any help I can possibly give, I feel as if I know she doesn't need it."

"She really has grown."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\n\nHanako's plans for her holidays are in sharp contrast to my simple following of my parents' suggestion to stay with them."

n "Holidays had always made me feel less excited than most, though, so maybe this is just a return to the status quo."

n "\nBefore my heart attack, I'd always lived so aimlessly that holidays weren't all that much different from my everyday life anyway."

n "After school I'd wander around a bit in the city, often hanging out with some friends, before making my way home to eat dinner with usually one of my parents, but rarely both."

n "Their work schedules didn't leave much time for them to be home, and going there straight from school would just have meant I'd end up feeling bored. I was an urbanite through and through."

nvl clear

n "\n\n\nSince coming to Yamaku though, it feels like I've fundamentally changed as a person. The phone call with my parents erased any traces of doubt I might have held on that, in any case."

n "While before I had exercised a fairly normal level of independence for a teenager, that being not a whole lot, my parents were more than pleased to hear of my newfound ability in taking care of myself."

n "Laundry, cooking for myself, cleaning, all in addition to other general chores that come from living without parents around… just little menial things I've had to pick up, but with relative ease."

n "\nWhen I think about it, I'd always depended on them, even if they hadn't been at home all the time. To say I never depended on anyone after moving to the Yamaku dormitories would be far from the truth, though."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve
window show

yu "Um… excuse me…"

stop music fadeout 3.0

scene bg school_library_ss
show yuuko worried_down_ss at center
with locationchange

"The two of us look up at the awkwardly fidgeting figure in front of us. Some things never change."

show yuuko worried_up_ss
with charachange

yu "It's getting close to closing time, so um…"

"Oh, right. I'd forgotten that the library closes earlier during the holidays."

"Hanako and I both get up and dust ourselves off, placing our books back on the shelf behind us. The fact that our tastes in reading material have a fair amount of overlap is useful at times."

"With a bow to Yuuko to apologize for taking so much time, Hanako takes her leave of us."

show bg school_library_ss at bgleft
show yuuko worried_down_ss at twoleft
with dissolvecharamove

show hanako basic_normal_ss at tworight
with charaenter

ha "See you tomorrow, Hisao."

hi "Bye."

hide hanako
with charaexit

"And with that, she walks out of the large, wooden, aging doors that herald the entrance to the library."

play music music_happiness fadein 3.0

show bg school_library_ss at center
show yuuko neutral_down_ss at center
with dissolvecharamove

yu "She's a quiet person, isn't she?"

"I suppose I should be surprised at a staff member sharing personal opinions like this, but after knowing Yuuko for a while it's largely expected. Our relationship is more personal, rather than one with her acting as an authority figure."

hi "Yeah, I think that's just how she is."

hi "She's got a lot more confidence in herself these days, though."

show yuuko smile_down_ss
with charachange

yu "I don't know her as well as you do, but I think I agree. It's nice to see her talking to people here; she never used to do that before."

hi "Hey, Yuuko… you know about Lilly's leaving, right?"

show yuuko worried_down_ss
with charachange

yu "She told me herself a few days ago. It must be hard, leaving everyone behind like she is."

"She quickly looks back to me after she says this, probably remembering that I went to her for advice on the relationship between Lilly and me before."

show yuuko worried_up_ss
with charachange

yu "Are you going to be okay?"

"That's… a difficult question. It's something I'd rather not think about for now, though, given more pressing issues."

hi "Something seems kind of off about this whole deal, don't you think?"

"Yuuko appears to think for a while, absentmindedly scrunching her face up in a variety of creative ways as she does so."

show yuuko worried_down_ss
with charachange

yu "I don't think I really know her well enough to make that kind of judgment."
#STILL thinking about judgment/judgement and whether it's even worth it to bother in the first place. -SC

yu "I'm sorry I can't be more help."

hi "Nah, that's fine. I'm just sort of thinking aloud."

"I give a deep sigh and scratch my head in frustration."

hi "There's just so much stuff happening at once that I have no control over… it feels like I'm being swamped."

show yuuko neutral_down_ss
with charachange

yu "I think everyone goes through times like that."

yu "What's important is to concentrate on what you can do, rather than what you can't do. At least, that's how I see it."

show yuuko smile_down_ss
with charachange

yu "If I didn't think like that, I don't think I'd be able to manage my life as it is."

"She says it with a smile and a light tone, but her words are far from any kind of joke. Being pulled between two jobs as she is, just to hopefully make enough money not only to live, but also for university, must be exhausting."

"Perhaps that's why, coming from her, this feels like it has more meaning than if it had come from most others."

hi "I guess you've got a point there."

hi "Thank you for your advice once again, Yuuko."

show yuuko smile_down_ss:
   ease 0.5 ypos 1.2
with None

show yuuko closedhappy_down_ss:
   ease 0.5 ypos 1.2
with charachange

with Pause(0.2)

show yuuko closedhappy_down_ss:
   ease 0.5 ypos 1.0
   linear 0.5 alpha 0.0 
with charamove

"She bows deeply and smiles again, before making her way back to the counter where she spends so much of her time."

stop music fadeout 2.0

scene bg school_dormhisao_ni
with shorttimeskip

"The tiny wings of the cardboard crane in my fingers are only just visible in the dim light of my room, just a little of the moonlight being able to peek through the curtains and around their edges."

show origami_hand:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with None

show origami_hand:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
show bg school_dormhisao_blurred_ni
with Dissolve (1.0)

play music music_twinkle fadein 10.0

"I lie still in my dark bed for a long time, idly looking up at the little origami bird."

"It feels like a lot's happened since Lilly folded this, but at the same time it feels like very little has changed."

"Compared to everyone else, I'm back to square one. I might have a newfound idea of where I want to go in life, but that's hardly something that affects me now."

"Hanako changed, I know that much. If anything, she just makes me feel like I've got no excuse to be like this, considering her previous situation."

"Lilly, though…"

"I turn the bird in my fingers another way, looking at it from yet another angle."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\nWhen I first met her, she seemed aloof and perhaps somewhat distant. Her actions were always careful, measured and precise, and her carefully maintained composure always gave the appearance of unerring confidence and serenity."

n "In time, she became less formal. Just a bit, but enough. It felt good to see her lowering her inhibitions around me, and opening up, even just a little, of her own accord; it felt as if I was seeing her real self slowly become more vibrant and visible."

n "\nNow, though, I'm beginning to have doubts."

n "\nPerhaps they're to be expected after what is, effectively, the two of us breaking up. They don't feel new or strange though, but rather like an old book being found and dusted off."

n "I soon realized after meeting Lilly that she saw me as she did Hanako; as someone who needed help and care. At first, I simply thought that we'd be fine as friends, helping each other through our limited time together in school."

nvl clear

n "\n\nBut then I began to treasure our moments together more and more, from our quiet walks to our talking over lunch. The good sides of her personality became ever more obvious, and ever more likable."

n "The absence caused by Lilly's trip to Scotland to visit her long-distant family and sick aunt only made me realize how much I liked just being around her, and I had thought that she felt a similar way."

n "\nFor her, though, maybe that wasn't everything to our relationship."

n "\nEven after she returned to Japan, that just meant she lost her family once again after meeting them for such a brief time."

n "She lived so much of her life without her family around, not to mention with Akira working long hours, that she had little choice but to be like that."

nvl clear

n "\n\nI had thought her sense of independence to be a good and admirable trait. It was in stark difference to my reliance on my parents before my heart attack, as reluctant as I may have been to admit it."

n "However, it also meant that she never let people get too close to her."

n "She lost her family likely due to her blindness, went to a different school from anybody she knew because of it, and worked all the harder to make sure she didn't end up a burden on her sister and those around her."

n "\nAnd now, Akira's going to Inverness, just like the family she thought she'd lost."

n "She never told me of her plans, as conflicted as she was about them."

n "Lilly didn't want to be a burden on anyone, including me."

n "\n\n…I'm an idiot."

nvl clear

n "\n\nI never questioned it. I never tried to be there or asked when she needed me to."

n "I just set my life up and expected it to stay that way forever, with the two of us having a nice long relationship where we pushed forwards towards our future together."

n "\nA small pit of frustration and anger at myself wells up in my chest."

n "\nI just let everything happen, never even trying to help Lilly."

n "\nJust her being there was enough. I thought I could keep going on if that were true."

n "But that could never have been enough. It was a childlike dependence on somebody, without any attempt to understand or help their situation."

n "Thanks to that, I lost Lilly. I lost the one person I loved most because I wasn't there for her when she needed me."

stop music fadeout 5.0

nvl clear
nvl hide dissolve

show origami_hand:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with None

show origami_hand:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
show bg school_dormhisao_ni
with Dissolve (1.0)

hide origami_hand
with None

window show

"With an increasingly angry feeling washing over me, I turn over and set the crane back on the desk next to my clock, the place where it has lived since that day when she folded it for me."

"Since that day when she herself said that my burdens needn't be my own."

"The obnoxious bright red numerals of my alarm clock shine through the darkness of the room onto my tired eyes."

"Ten o'clock. Evening. Curfew will be soon."

hi "I wonder…"

"Akira mentioned they'd be leaving this evening."

"I've no idea exactly when their flight is… but that means there's a chance, however small, that they might not have already left."

"Adrenaline starts to move through my body as I sit up on my bed, my eyes suddenly wide with possibility."

"There's no guarantee they haven't left, indeed it's likely that they already have, but there's also a chance they haven't, however small it may be."

"Just this once, just as I should have before…"

play sound sfx_switch

show bg school_dormhisao
with Dissolve(0.2)

$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_friendship fadein 9.0

"I stand up and rush over to my cabinet, throwing out some clothes as fast as I can and sliding them on in quick succession."

"Each second that goes by is a second that I can't regain, a second that may mean the difference between catching them and losing them forever."

"Even if I fail, I have to try. I can't let her leave everything behind without even trying to stop her. Without, just this once, being there for her."

"With the last of my clothes slipped on, I hastily grab the phone off the desk. Luckily, the number for a local taxi company is still in my call history."

show bg school_dormhisao_blurred
show phone mobile:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with locationchange
with Pause (0.5)

"A gruff, unenthusiastic voice announces the name of the company while I pace around the room. It takes some effort to slow down my voice and keep it clear over the phone."

scene bg school_dormext_full_ni
with locationskip

"The chilly night air sweeps against me as I open the dormitory door, but nevertheless I keep up my brisk speed as I half-jog, half-run out to the school gates."

"It may not be curfew just yet, but it's precariously close. If there were a guard around they'd no doubt have some questions for me, but it looks like I've managed to come out just before they arrive, or they're around a corner."

scene bg school_gardens_ni
with locationchange

"My pace picks up as I make my way through the school gardens, their night-time allure all but lost when I begin to run to the school gate."

scene bg school_courtyard_ni
with locationchange

"The lamps of the courtyard, dim as they are, provide just enough illumination to light the way and prevent me from tripping over. The buildings themselves take on a rustic, almost antique-looking edge when I glance at them."

"Looking back, it seems strange that they once appeared so dark and looming to me. Now they just look to be somewhat anachronistic school buildings, the same as any others bar their age."

scene bg school_gate_ni
with locationchange

"Leaving the gates behind me, I pull up to a stop just before the taxi. Parked just as Akira's car had been, its gaudy and brightly lit sign looks out of place in the quiet country backdrop."

"I impatiently squeeze myself through the door, giving the driver the address for where the two should hopefully be staying."

scene bg shizu_houseext_ni
with shorttimeskip

"By the time the taxi pulls up after its trip at maddeningly casual speed, it's well and truly deep into the night."

"The house is truly enormous, its sheer size much larger than I'd expected, and ominously still. Fearing the worst, I ask the driver to stay just in case my efforts are for naught."

"A single press on the fancy intercom system outside the gate produces a short electronic melody in the otherwise silent road. It's not long before a somewhat deep, gruff voice can be heard from it."

mystery "This is the Hakamichi residence. Please state your name and why you're bothering us this late."

"I press on despite inwardly wincing at the reasonable annoyance audible in his voice."

hi "It's Hisao Nakai. I was hoping to meet Lilly or Akira, if they're still here."

"Surprisingly, I manage to summon quite some energy to my voice, enough to make the other side of the intercom silent."

show bg shizu_houseext_lights
with Dissolve(0.2)

"A few seconds pass, but just before I press the button again and ask what's going on, a light turns on outside the front door."

"I strain my eyes to try and make out who is coming through, but as he comes past a large parked car with fishing rods sticking out the back, his identity becomes clear."

"His face is typically placid and emotionless as he saunters up to the gate. He's still childlike in his mannerisms, despite his demeanor. With the press of a few buttons from behind the fence, the gate slowly opens."

show hideaki surprise_ni at center
with charaenter

hh "Hisao? What are you doing here?"

"I think this is the most emotion I've ever heard from his voice, not that it would be hard to reach that mark."

hi "Akira told me that she and Lilly would be staying here before they left for their flight."

hi "I need to talk to Lilly, just one last time. Are they still here?"

show hideaki sad_ni
with charachange

"The look on his face says everything."

"I failed. I was too late. The one time when I actually needed to act quickly, and…"

show hideaki serious_up_ni
with charachange

hh "Actually… it's possible…"

hi "What? What is it?"

show hideaki confused_ni
with charachange

"He's a bit taken aback by my fervor, but I can't help it at this point."

show hideaki normal_ni
with charachange

hh "They left not long ago; only a few minutes before you arrived, in fact. If you go straight to the airport, you might be able to… Hisao!?"

"I dart back towards the waiting taxi, grabbing what little money is left in my pocket as I go."

hi "Thanks, Hideaki!"

"With that I take a seat, and in short order bark out my destination."

scene bg city_street4_ni
show crowd_ni
with shorttimeskip

play ambient sfx_crowd_outdoors fadein 2.0

"My chest beats wildly as I tear down the street, my body twisting this way and that to slip between the pedestrians walking back and forth beside me."

"With the road solidly blocked by taxis and other cars, dropping off passengers and picking up others in the time they have to wait, we ended up having to stop almost a block away."

"But that's in the past now. What matters is reaching Lilly."

"One foot hits the ground, the other quickly following without the slightest thought, as if my legs have taken on a life of their own and all my mind can do is concentrate on the view ahead of me."

"Just one glimpse of that long hair of hers. That long, yellow hair that was the same color as the wheat that stretched as far as the eye could see."

"In the end, I depended on Lilly, just like Hanako did. Even after we started going out, it still doesn't feel like she really ever let herself depend on me."

"Except for one moment. That one moment where we held each other tightly on that bright yellow field."

"At that time she must have feared losing me just as she did everyone else. That's why, just this once…"

"The night air wraps around me, draining every last remnant of warmth out of my body, to the extent that it feels more like midwinter than a summer night."

"My fingers, my hands, my feet… they all feel increasingly cold."

"The sound of the passing crowds is reduced to no more than a background hum while the sound of my shoes hitting the pavement echoes loudly, every step surging towards the person I have to catch."

"Forced by my chest tightening in response to the cold of the night, I rest an arm over it to try and settle it down."

window hide

scene bg hosp_ext_ni
show crowd_ni
with locationchange

play sound sfx_heartslow
show heartattack alpha 
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.7)

window show

"When the airport comes into view, though, I realize this feeling as one I've felt before."

"Not now… of all the times for this, please not now."

"I take a gulp and soldier on regardless, pushing my body as far as it will go."

"Sweat pours off me as I hurtle forward, my shoulder hitting someone's side and my mind suddenly flooding with emotions and memories."

"I continue on without an apology. I have to keep moving now. If I stop, I'm not sure I could begin again, and even if I could it would all be for naught if I'm not in time."

with vpunch

"I hit another person, then another, offering little resistance to getting bounced about."

"My feet feel numb. My arms are losing all feeling. My chest forces me to hunch over awkwardly, tightening ever more."

window hide

play sound sfx_heartslow
show heartattack alpha 
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

window show

"That afternoon in the snow… that time when my life irreversibly changed…  images of Iwanako and that damned letter flash over and over in my mind, the first love I'd lost thanks to my condition."

"I can't let that happen again. I don't care what happens to me any more, I just need to see her one last time."

"…There!"

scene ev lilly_airport
with flash

"A sliver of yellow and white comes into view some distance down the road, her figure silhouetted by the lights emanating from the airport entrance."

hi "Lilly! Lilly!"

hi "Lilly! Stop, please! Lilly!"

"Come on Lilly, I know your hearing's far beyond nor—"

scene bg hosp_ext_ni:
    xalign 0.5 yalign 0.52 rotate 0 zoom 1.0
    linear 0.1 rotate -6 zoom 1.2
show crowd_ni:
    xalign 0.5 yalign 0.52 rotate 0 zoom 1.0
    linear 0.1 rotate -6 zoom 1.2
with vpunch

play sound sfx_impact

hi "Gah!"

"My view suddenly spins out of control and ends up on the ground, my body haphazardly sprawled after hitting someone and stumbling over."

window hide

play sound sfx_heartslow
show heartattack alpha 
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

window show

"Before I can assess the damage, an unbelievable pain ignites in my body. All my thoughts are blanked as I curl up and frantically clutch at my chest."

mystery "Hey, are you okay? That was a really bad fall."

"This pain… I can't…"

hi "Argh… aaaaaargh!"

window hide

play sound sfx_heartslow
show heartattack alpha 
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

window show

"Any sharp knock could do me in. Any overexertion. I thought I could overcome my limits this once…"

mystery "Something's wrong with him!"

window hide

play sound sfx_heartslow
show heartattack alpha 
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.8)

window show

mystery "What's the matter, are…"

window hide

play sound sfx_heartslow
show heartattack alpha 
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

with Pause(0.7)

play sound sfx_heartfast
show heartattack alpha 
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.8)

window show

"The voices of those gathering around me are gradually replaced by a loud ringing in my ears. By now I'm unable to move my head, my eyes turn upwards to see the mute moving of their lips."

window hide

play sound sfx_heartfast
show heartattack alpha 
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.8)

with Pause(0.15)

play sound sfx_heartslow
show heartattack alpha 
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.8)

play sound sfx_heartfast
show heartattack alpha 
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.8)

with Pause(0.05)

play sound sfx_heartstop
show heartattack alpha 
with Dissolve (0.1)

stop ambient fadeout 0.3

show heartattack residual
with Dissolve (0.8)

window show

"Even as I clutch my chest, I realize I can't feel my fingers any more, nor my feet. It feels like my entire body is shutting down, starting from my extremities."

scene ev lilly_airport_end:
    truecenter
    zoom 1.2 rotate -8 subpixel True
    easein 12.0 zoom 1.0 rotate 0
with slowfade

"With one last effort, I turn my head down the road towards the airport entrance that's casting its light over me."

"Lilly is there, behind the crowd. Her head is tilted, but only just slightly."

show passoutOP1
with None

"I can feel my vision dimming as I try to yell out, but nothing emerges from my mouth despite my best efforts. Slowly but surely, my vision begins to black out the scene before me."

"So… this is how it ends."

"I failed. I was so close, so very close, but at the very last moment my condition seized my chance at a new life and dragged me back."

"Now I'm going to die, sprawled out just meters from an airport, with a crowd of babbling people surrounding me and with Lilly leaving for Scotland just a little distance ahead."

hi "Li… lly…"

stop music fadeout 4.0

"That last word extinguishes the last of my energy. The world falls into a deep, inescapable blackness as every muscle in my body shuts down."

"I'm sorry, Lilly."

"I was too late."

scene black
with dissolve


#**********************

label th_L31:

scene white
with dissolve


"…"

"……"

"………"

"What's… going on…?"

"As I slowly open my eyes, a bright, white light assaults my retinas."

"For minutes I just lay where I am, mindlessly staring ahead while my scattered thoughts coalesce in my slowly waking mind."

show bg hosp_ceiling:
    alpha 0.0
    linear 5.0 alpha 1.0
with None

"Slowly but surely, the white begins to come into focus as a bare expanse begins to be drawn across my field of vision."

"It's only when the light fixture comes into view that my mind clicks that this is the ceiling above me."

scene bg hosp_room2
with locationchange

"Slowly levering myself up, I silently absorb through all my senses the details of the room I'm in."

"The smell and taste of strong bleach hang in the air, lending the impression of a place just slightly too clean to be natural."

"Inoffensive pale peach-colored walls, all perfectly painted without a crack, stain or imperfection. A single framed painting hangs on the wall, perfectly straightened. Like the walls, it's as boring and inoffensive as can be."

"My attention's grabbed by the translucent curtain waving across my vision, my eyes following it to the open window it covers."

"When I move my right arm to try to lift myself up and look through it, I feel the catheter dig in uncomfortably. It's only now, too, that I notice the cannula tubes winding around my cheeks and into my nose."

"After some fidgeting, I settle for just looking around the corner of the window."

scene ev lilly_hospitalwindow
with whiteout

"Beyond the thick leaves of several large trees, I can see the greenery below, backing out onto a field. A customary island of green on the outskirts of the city."

"Judging by the sun outside, it's noon. Of which day, though, I'm not sure."

"So… I'm in a hospital once again."

"I let out a long, tired breath as I try to collect my scattered thoughts, my mind seemingly cast in a dozen directions all at once with as many emotions running through me."

scene bg hosp_room2
with locationchange

"After slowly lying back down, I decide to start at the beginning; why I'm here."

"I cast my mind back, but I can't work out a smooth recollection of what happened. The events of last night… or whichever night it was… come back more as a series of snapshots than any cohesive memory."

scene bg school_dormhisao_ni_fb
show origami_fb at center
show noiseoverlay
with flash

"Lying on my bed looking at the origami bird."

scene bg shizu_houseext_lights_fb
show hideaki serious_up_fb at center
show noiseoverlay
with flash

"Talking to Hideaki outside the Hakamichi residence."

scene bg hosp_ext_fb
show crowd_still1_fb at center
show noiseoverlay
with flash

"Running down the street, passing pedestrians and bumping into more and more of them."

scene bg hosp_ext_fb:
    xalign 0.5 yalign 0.52 rotate -6 zoom 1.2
show crowd_still2_fb:
    xalign 0.5 yalign 0.52 rotate -6 zoom 1.2
show noiseoverlay
with flash

"Falling."

scene ev lilly_airport_end_fb
show noiseoverlay
with flash

"Looking up at the searingly bright airport entrance, seeing Lilly's back as I lay on the ground…"

"…"

scene bg hosp_room2
with fade

"The silence of the private room suddenly feels overwhelming."

play music music_rain fadein 2.0

window hide
nvl clear
nvl show dissolve

n "\nSo that's it. I had my chance to correct my mistake, and I blew it."

n "Whether I was at fault for neglecting my medication and disregarding to pace myself, or my body was for giving out so soon, it doesn't matter now."

n "All that matters is that, once again, I'm alone."

n "The pastel blue pillow yields with little resistance as I let myself fall back onto the bed, its starchy case, along with the starchy sheets, providing little comfort."

n "Compared to the darkness of last night's events, the bright light of the room around me is striking. All it does, though, is emphasize how otherworldly places like this are."

n "\nArrhythmia."

n "\nA strange word. A foreign, alien one. One that you don't want to be in the same room with."

n "A rare condition. It causes the heart to act erratically and occasionally beat way too fast. It can be fatal."

nvl clear

n "\n“It was a miracle that you were able to go on so long without anything happening,” they said."

n "And then, it did. My condition had taken away everything; my old school was of no importance any more. My home was reduced to a faraway place. Both my friends and my first love simply stopped visiting after a length of time."

n "I became cynical and embittered. Distant and subdued. In my defense, no person could avoid that after such a thing happening to them, but nonetheless I left the hospital as a very definitely changed person."

n "Things changed. I made new friends in Hanako, Shizune and Misha. I found a new sense of “home” in my dormitory, a new interest in science and the world around me, and I found a direction to my life that I had never felt before."

n "\nBut I'd also discovered other things."

n "The sense of isolation in Yamaku and its surrounds was not entirely unwelcome, the quiet giving a peace of mind I might not have found elsewhere, but it gave the area a feeling of being pushed out of the way, of being kept out of sight."

nvl clear

n "\n\nPeople in the streets would sometimes glance awkwardly, or quickly turn their heads as they realized they were staring. Even if my condition wasn't visible, my uniform was."

n "Even if it weren't, I was still different. I took seventeen pills a day, morning, midday and night. My scar, though hidden behind clothing, was still a permanent mark of my condition. And most of all, there was the very real possibility of death."

n "A bad fall. An absentminded hard hit on the back. A simple sprint taken too far. Anything could have set my heart off, and several times I teetered on the edge of the abyss even with all the care I took of myself."

n "\nBut that was fine. I could have lived with all that."

n "Because there was one final thing I'd found, or rather refound, after entering Yamaku."

n "\nWhich was once again snatched away before my eyes."

nvl clear

n "\nIt's only now that I realize just how delicate my newfound sense of happiness was. Everything depended on her, the linchpin of my life since I first entered Yamaku as a sullen, confused and aimless transfer student."

n "Lilly Satou was the one person I could depend upon above all others, and who reciprocated the love that I felt for her. But I failed her, and only realized it all too late."

n "I thought that I could just set my life up and continue that way forever, but the real world doesn't work like that. I finally realized the meaning of those words, only to be struck down as I confronted my failure to do so in time."

n "\n…"

n "\nThe surroundings I'm in now are all too familiar. It's as if Yamaku was but a dream, and I'm still recovering from my first major heart attack."

n "Maybe that's why I feel so tired. It feels almost as if I've lived the entire last few months of my life in the space of minutes."

nvl hide dissolve
nvl clear

scene black
with shuteye

window show

"The weight of my eyelids closes my eyes, my physical and mental exhaustion letting me offer no resistance."

window hide
with Pause(1.0)
with shorttimeskip
with Pause(1.0)
window show

"Unintelligible mumbling from ahead of the bed stirs me out of my sleep."

"With my eyes still closed, I can focus and make out someone, presumably a nurse, bidding farewell to a doctor."

scene bg hosp_room2
with openeye

"As I open my eyes, I notice the door closing in my peripheral vision."

"The doctor stands reading some notes off a clipboard held in his hand, carefully looking over the pages."

"After consulting his obviously very important documents, he looks up and notices my gaze. It's now that I notice something slightly odd about his expression and general disposition, but I can't quite put my finger on it."

"Doctor" "Ah, I see you're awake… Mr. Nakai."

"His quick glance to my bed end, to verify my name, shows that his documents obviously didn't have it written on them."

"Doctor" "I must admit this is a bit unfortunate; your parents visited just earlier while you were asleep. I could notify them you're awake now, if you'd like."

hi "Um… thanks. That would be good."

"I give a somewhat dazed reply, most likely the one he'd expect, before really thinking about what I'm saying."

"Doctor" "Not a problem."

"Doctor" "If you have any questions you'd like to ask, I'll be happy to answer them. That is, unless you'd prefer to rest; the anaesthetic's still going to be affecting you a bit, I'm afraid."

"The anaesthetic… of course. That'd be why I felt so strange the first time I woke up."

"I slowly shake my head, not wanting to dislodge any pipes or cause myself any more discomfort than necessary. The doctor politely puts down his clipboard in response."

hi "I guess my main question is… what exactly happened?"

"Doctor" "To put it simply, you've unfortunately had another heart attack. While not as severe as your first, you were very lucky it occurred so close to a hospital."

"Doctor" "After being stabilized, you were taken to the operating room. What followed was keyhole surgery in order to insert a temporary pacemaker."

"Doctor" "All in all, the incident happened two days ago, with emergency treatment being carried out very soon afterward. Since then, we've kept you under close observation while you were asleep."

hi "Will I be all right? Are there any lasting problems?"

"Doctor" "Compared to the procedure carried out for your first heart attack, this was relatively minor."

"Doctor" "While you will have to undergo surgery once more in a few days' time to remove the pacemaker, assuming there are no complications, there should be no lasting implications."

"He continues talking, the subject shifting to a repetition of facts about arrhythmia and my medications that I already know for the most part. I start to nod and feign interest, while my mind drifts."

"I begin to think about how perfectly hung the inoffensive painting hanging on the wall behind his shoulder is, and how neat and sterile the surroundings are, even including the doctor himself."

"Doctor" "If my mumbling bores you, you are quite welcome to say so, Mr. Nakai. Lord knows, I lose track of myself sometimes."

"He gives a short chuckle at his self-deprecating joke as I grimace awkwardly, having been rather badly caught out."

"The doctor's chuckle sounds different from that of the nurse at Yamaku though, come to think of it. As I ponder why, I realize why the man in front of me feels just that little bit “off”."

"His smile is neat and sterile. He delivers his little joke perfectly, with a customary inoffensive chuckle."

"It is like, rather than talking to the man whose name is neatly printed on the nametag pinned to his lab coat, I'm merely interacting with an actor reading off a prerehearsed script, every action having been choreographed beforehand."

"I suppose he has to be this way though, being a doctor."

"He has to keep his neat and sterile smile when chatting to the girl with cancer slowly spreading through her body, when reassuring the woman who'll surely die from childbirth, and with every other terminally and critically ill patient."

"That little bit of distance. That little bit of aloofness."

"It makes me wonder if I've been too harsh, especially considering it's a disposition far from being adopted only by people in his profession."

"After all, the one I loved kept that same distance from others herself."

"Looking up to the doctor again, I realize I've been in thought with my head bowed for some time."

"Doctor" "I understand you must still be tired. You've been through a lot, and as I mentioned before, the anaesthetic would still be affecting you."

"Doctor" "If you don't mind, I'll let you get some rest and tell your parents you've woken up for you."

hi "I think… that would be good. Thank you."

stop music fadeout 6.0

"He gives a curt nod before picking up his clipboard and making his way to the large white door in the corner of the room, closing it behind him with a thud."

"In the end, I'm alone again."

"Lilly's gone. Akira's gone. Hanako would be traveling, and even my parents have already left the hospital."

"Four pale peach walls, one white ceiling, and a single open window to look out towards the world outside."

"It's hard to think of the future when the past is crowded around you, claustrophobic in its neat, sterile, starchy, bleach-smelling grip."

"Lost for what to do or focus on, I content myself with sleeping the time away as if this were all just another dream like Yamaku had been."

scene black
with dissolve

#**************************

label th_L32:

scene white
with dissolve

"White."

"A sterile, clean white for a sterile, clean room."

$ renpy.music.set_volume(0.05, 0.0, channel="music")
play music music_musicbox fadein 10.0

show bg hosp_ceiling:
    alpha 0.0
    linear 5.0 alpha 1.0
with None

"My eyes open, and I simply stare at the ceiling for some time. It's about as interesting as the television would be, mounted in its metal rack hanging off the ceiling ahead of the bed."

"Indeed, the television saw its entire use during the time my parents were here. Left on quietly as they waited for me to wake, it was about as banal as it had been the first time I'd ended up in the hospital."

"Earlier today an attending nurse had offered to turn off the EKG's speakers. I refused simply because the sound is so entirely normal to me now."

"It's almost comforting, in a way. The metronome-like regularity gives at least some feeling that time is moving, even in a place such as this."

"After some time of listening to its beeping while I fully awaken, though, I realize there's another sound in the room."

$ renpy.music.set_volume(0.1, 5.0, channel="music")

"Concentrating all my efforts on listening, a task made rather easy by the lack of distractions, a tiny tinny melody can be heard."

"Light and quiet, the music sounds almost fragile as it's dwarfed by the EKG's pulses."

scene bg hosp_room2
with locationchange

"Tilting my head just slightly to the side in an effort to see the source of the melody without dislodging any of the sensors and pipes stuck onto me, I notice a little wooden box sitting on the nightstand next to the bed."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

show musicbox open:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

"My mouth opens just slightly while I silently watch the tiny yellow metal drum slowly rotate inside, the little bumps on its surface gradually moving in and out of sight."

"This music box… it's the one I gave…"

show musicbox open:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide musicbox
with None

"The creaking of the door breaks me out of my reverie, my head and heart remaining still as my eyes turn to see who comes through."

"Long tan skirt… peach off-the-shoulder sweater… pale, almost porcelain skin… blue clouded eyes and long, yellow hair…"

show lilly basic_reminisce_cas at center
with charaenter

"All I can do is stare as Lilly slowly walks into the room, her fingers lightly running over the wall for orientation, and my mind comes to a shuddering halt."

hi "L… Lilly…?"

show lilly basic_oops_cas
with charachange

"She stops midstride, her entire body tensing."

li "Hisao? Was that you?"

"Her voice is quiet and pensive, echoing her expression."

hi "I thought you were…"

show lilly basic_sad_cas
with charachange

"Lilly takes one tentative step forward, then another, as if she were holding herself back."

show lilly basic_sad_cas_close
with characlose

"Her control over her composure is for naught though, and she finally rushes over to where I lay as the last of her resistance falls."

$ ksgallery_unlock("unlock_ev lilly_hospitalclosed")
scene ev lilly_hospitalclosed at l_hosp_out
with whiteout

"I'm slightly taken aback when she grabs hold of me, hunching over as tears begin to fall from her cheeks, since only minutes ago I thought she was on the other side of the world. After a moment of hesitation, I rest my right hand on her soft shoulder."

li "Hisao! Hisao!"

"Lilly's body trembles as her tears blot the pale green sheets, her emotions flooding through her carefully maintained exterior."

"With her face now closer, and made easier to see for her pale skin being lit by the sunlight from the window, I notice her cheeks being redder than they should be."

hi "It's okay, Lilly. I'm okay. You don't need to—"

$ ksgallery_unlock("unlock_ev lilly_hospital")
show ev lilly_hospital at l_hosp_out
with charachange

"She rights herself quickly, her crying forcefully stifled with both sadness and stubbornness remaining in her moistened eyes. Her prideful nature, always having been something to contend with, takes me off guard."

li "Stop telling me not to worry about you, Hisao!"

li "Just this once… let me cry…"

"I'm caught speechless. She waits for a response, but her composure breaks again after a handful of seconds."

show ev lilly_hospitalclosed at l_hosp_out
with charachange

"I swallow hard to try and settle my own emotions while she weeps onto my bed, a strange mixture of relief and depression welling up."

"Lilly's… here. She's really here. If I couldn't feel her skin under my hand, I'd hardly believe my own eyes. My efforts weren't for nothing; my body's attempt to take away everything that was important to me once again has been foiled."

"But now… I don't feel as happy about it as I thought I would."

"Seeing her here, crying like this over me… this is the one thing I'd wanted to avoid since coming to love her, no, even since leaving the hospital."

hi "I'm sorry, Lilly. It's my fault I'm here; I shouldn't have tried to push myself so far."

"I give a self-deprecating snort."

hi "After months of keeping myself together so nobody'd worry over me, I went and did something like this. I guess I'm pretty dumb."

scene bg hosp_room2
show lilly basic_weaksmile_cas_close at center
with whiteout

"With a couple of sniffs and a long breath, Lilly manages to pull herself together and calm down a little."

"Despite her red cheeks, moist eyes and the lines of her tears still visible, she delicately wears that weak smile she seemed to so often give."

li "You needn't blame yourself. I heard later that it happened as you were running down the road after me, right?"

hi "Still…"

"She wipes her eyes with the back of her hand, returning more to her old self as the rush of emotions wears off."

show lilly basic_reminisce_cas_close
with charachange

li "Why did you run after me, Hisao?"

show lilly basic_concerned_cas_close
with charachange

"I move to respond, but notice her face tightening."

li "Even after I'd said goodbye, and I'd left Yamaku Academy…"

"She takes a moment to steady herself, her emotions almost bubbling up once again."

hi "I just wanted to say that I'm sorry."

show lilly basic_surprised_cas_close
with charachange

li "Sorry?"

hi "For the times when I wasn't there when you needed me."

hi "Until now, I thought you just being there would be enough. I only needed you by my side to make any day feel better."

hi "Even if my body may be like this, I want to help you, Lilly; to be there when you need someone."

show lilly basic_weaksmile_cas_close
with charachange

li "But you always were there, Hisao…"

hi "Why did you want to go to Scotland, Lilly?"

show lilly basic_sleepy_cas_close
with charachange

li "Why…? I told you before: because Akira was going, and because of my family's summons to their home."

hi "Why didn't you say that you wanted to go?"

show lilly basic_oops_cas_close
with charachange

li "I—"

hi "I'm not stubborn often, but this one time I think I need to be. I want you to stay here, Lilly."

hi "I want you to stay where everyone you know lives, and where all your dreams and ambitions were made. If you choose to stay, I'll never leave your side. I won't let you lose another person."

hi "When I had my heart attack, I was snatched away from everyone and everywhere I knew. You showed me a new life after I came to Yamaku. I'd lost my past, but you showed me a future."

hi "It's true that I haven't always been there for you. I'm unreliable, sometimes I lied, and I thought I'd come to understand you when I hadn't even understood myself."

hi "Be that as it may, I want to give you a future as well. I want to be there for you, to share both your burdens and your happiness, just like I promised back in Hokkaido."

hi "I want you to trust me. I know I had problems coming to put my trust in you, after losing so many people I'd known after my heart attack, but that's how I know that being unable to trust others can feel awful."

hi "That's why I can't watch you just throw everything away like this. I never want you to go through what I did. I would do anything to stop that."

show lilly basic_weaksmile_cas_close
with charachange

li "You can be quite steadfast when you want to be, can't you?"

hi "As I said, it isn't often."

"My weak smile drops, though, as the IV in my arm digs in a little. It's a harsh reminder of my tether to my condition."

show lilly basic_concerned_cas_close
with charachange

"Lilly's face tenses as I let out a small gasp of pain, immediately making me wish I'd stifled it better. All I can do is sigh in defeat."

hi "I tried to not let anyone worry over me for the entire time since I left the hospital, but I can't even stop the one person I love most from crying over me."

hi "Even if I might finally be able to put my feelings into words, I feel pretty useless with a body like this."

hi "Every time I tried to reach towards something, it was just snatched away, and even now things only turned out for the better due to luck."

hi "I guess that's something else I should apologize for. All I can ever do is make you worry. Even now, there's very little chance I'll live anywhere near a full life."

"The feeling of Lilly's warm, soft hand moving over my left cheek makes me lift my head up, her smile gentle and warm as she touches me."

show lilly basic_smileclosed_cas_close
with charachange

li "I think that is something very natural for you to say. You were always so sincere and self-conscious."

show lilly basic_smile_cas_close
with charachange

li "You were also reserved and mild-mannered, and patient to a fault with Hanako, yet curious about everything and everyone."

show lilly basic_weaksmile_cas_close
with charachange

li "When I said I missed you while I was with my family, I wasn't lying or exaggerating. The thought of you was never far from my mind, and helped me through that time."

show lilly basic_reminisce_cas_close
with charachange

li "That's why I was so confused about what to do when my family summoned me. Even after I thought I had made my decision, you tried your hardest to challenge me about it."

show lilly basic_weaksmile_cas_close
with charachange

li "I didn't confess to you out of pity or believing you were somehow different from what you are. I confessed because I never want to lose you, and want you to always be a part of my life, no matter what might change."

show lilly basic_smileclosed_cas_close
with charachange

li "You are a very beautiful person, Hisao. Your heart changes none of that, so please, don't apologize for yourself any more."

"For a long time, silence reigns in the room."

"I'm not really sure what this newly born feeling inside of me is, but it pales into insignificance as I wordlessly gaze at Lilly's smiling face, warm and gentle as it has always been."

"It's only as her thumb crosses my cheek, wiping away a single drop of moisture, that I realize this is all I've ever wanted."

"For what feels like the first time, I give an earnest, wide smile. As Lilly feels it against her palm, she returns the gesture."

"More time passes before either of us says a word, neither of us needing speech to communicate our feelings to each other."

hi "I know I can't promise you that I'll always be around, or that we'll be together forever."

"With some difficulty I slowly lift my hand, placing it on her pale shoulder."

hi "But… I think I can at least take you to next year's Tanabata festival, to make up for making you miss this year's."

show lilly basic_emb_cas_close
with charachange

"Lilly's expression is one of surprise, though I can't say I blame her."

li "You… remembered that?"

hi "I've got a pretty good memory. Sometimes."

show lilly basic_giggle_cas_close
with charachange

"She raises her head a little and takes her hand from my cheek, giving a small, amused giggle. I smile absentmindedly at how earnest it is, almost girlish in its lightness."

show lilly basic_cheerful_cas
with charadistant

"Still smiling warmly, she collects herself and stands upright with a hand resting on my chest."

"It feels like I'm seeing her for the first time, the sun from the window glowing behind her just as it did when I first walked into that room where she was drinking tea."

show lilly basic_smile_cas
with charachange

li "Very well then. Shall we make it a promise between the both of us to go to next year's Tanabata together?"

"Even if she can't see me doing so, I nod approvingly."

hi "I promise."

show lilly basic_smileclosed_cas
with charachange

li "I promise."

window hide

stop music fadeout 4.0

#*****************************


label th_L33:

window hide None

play ambient sfx_parkambience fadein 6.0

scene bg lilly_hilltop
with Dissolve(3.0)

play music music_lilly fadein 5.0

window show

"Akira, Lilly and I silently sit on the grassy embankment high above the local town, the breeze gently blowing through the cloudless sky."

"We may be just a few minutes' walk from town, on a hill just outside its limits, but the view is entirely unexpected."

show lilly basic_smileclosed_cas_close:
    left
    ypos 1.1
with charaenter

"Lilly sits beside me, her eyes closed, as the gentle breeze flows through her hair."

li "This is a nice area."

hi "Yeah. I never knew a place like this was anywhere near Yamaku."

show akira basic_ending_close:
    right
    ypos 1.1
with charaenter

aki "And I had to be the one to find it, of course."

"Akira's grin is genuine, but her tone is slightly different from her usual carefree nature."

show akira basic_smile_close
with charachange

aki "It's good that you're outta the hospital though, Hisao."

hi "Nobody's more glad than I am. I can't stand hospitals."

aki "So, you two going back to the school tomorrow?"

$ doublespeak(hi, li, "Yup.", "Yup.")

show akira basic_ending_close
with charachange

"Akira chuckles in amusement before looking back out to the town below, the trees between the buildings swaying in the wind."

hi "Pity we couldn't go up north for the summer holidays, or get to Tanabata."

show lilly basic_weaksmile_cas_close
with charachange

li "I wouldn't worry, there's always next time."

show akira basic_smile_close
with charachange

aki "You'll be graduating before the next summer vacation, won't ya?"

hi "Yeah. There'll still be college after that, mind."

aki "Going to the same one?"

show lilly basic_smile_cas_close
with charachange

li "Likely. We both have high enough scores to meet the entry requirements."

hi "You sound so sure…"

show lilly basic_cheerful_cas_close
with charachange

li "Don't worry, you're better than I in most subjects."

hi "I guess we'll work it out in due time."

show akira basic_laugh_close
with charachange

aki "That's the way. Just enjoy yourselves in Yamaku while you're there."

show lilly basic_weaksmile_cas_close
with charachange

"Lilly gives a sad sigh at the distinction made between Akira and the two of us."

show lilly basic_reminisce_cas_close
with charachange

li "Do you really need to go back to Scotland?"

show akira basic_resigned_close
with charachange

aki "Yeah. The folks are already out for my blood as it is."

hi "You weren't meant to stay this long?"

show akira basic_ending_close
with charachange

"She gives her trademark wide grin."

aki "Setting my boyfriend up with a passport took some time."

hi "You're taking him with you?"

show akira basic_smile_close
with charachange

aki "Just for a while at first. He's a surprisingly worldly guy, so I think he'll do just fine."

show akira basic_lost_close
with charachange

"Akira gives an amused snort."

aki "If our father had his way, I'd have gone a long while ago."

show akira basic_laugh_close
with charachange

aki "I just couldn't pass up an excuse to stay with my favorite little sister a little while longer though."

show lilly basic_smileclosed_cas_close
with charachange

"She leans right and gives Lilly a tight playful hug, cheering her up considerably."

li "It's nice to be with you one last time, though."

hi "For what it's worth, I'm in the same boat."

show akira basic_smile_close
with charachange

aki "Heh, thanks you two. I'll try and come back sometime, don't worry."

show lilly basic_reminisce_cas_close
with charachange

li "It's a shame that the business keeps you so busy."

show akira basic_lost_close
with charachange

aki "The place won't run itself, I'm afraid, and I think it's going to be just the same over there."

show akira basic_smile_close
with charachange

aki "Considering that, I'd better get going."

hi "Have fun over there, Akira."

show akira basic_laugh_close
with charachange

aki "Haha, will do."

show akira basic_smile_close at right
with dissolvecharamove

"With a slight grunt, she lifts herself with her hands and stands up, dusting herself off as she does so."

show akira basic_lost_close at right
with charachange

aki "Well, I'd better be off. The plane won't wait for me, after all."

"She has a certain unusual wistfulness in the tone of her voice, her eyes firmly planted on her sister."

show lilly basic_weaksmile_cas_close
with charachange

li "I'll be okay, Akira."

show akira basic_resigned_close
with charachange

aki "Yeah, I know."

show lilly basic_smileclosed_cas_close
with charachange

li "Come now, it isn't that bad. You'll be able to see us again soon."

"It is strange to have Lilly reassuring a doubting Akira for once. She really has changed."

show lilly basic_smile_cas_close
with charachange

li "Goodbye, Akira."

hi "'Bye."

show akira basic_smile_close
with charachange

"For a second, the dark-clad figure looks down at the both of us, smiling widely. Perhaps more widely than I've ever seen her do before."

show akira basic_boo at tworight
with charadistant

"She lets out a long, slightly wavering breath to steady herself before leaving, but eventually slips her hand in her pocket and turns on her heel."

"And with that she walks away, one hand held in the air as she goes."

show akira basic_ending
with charachange

aki "Seeya later, you two!"

hide akira
with charaexit

"A jazz tune with no beat, melody or direction to the very end."

show bg lilly_hilltop at bgright
show lilly basic_smileclosed_cas_close at center
with dissolvecharamove

"After a few moments of sitting silently, Lilly and I pick ourselves up and dust ourselves off."

"Turning towards her with a broad smile, I hold out my hand."

hi "Shall we be off, then?"

"She takes my hand in hers, with a gentle nod and a smile as beautiful and warm as ever."

show lilly basic_cheerful_cas_close
with charachange

li "Indeed we shall, Hisao."

scene unlock_ev lilly_goodend
show evbg lilly_goodend:
    truecenter
    zoom 3.0 subpixel True
    1.0
    linear 0.5 zoom 0.9
    easein 12.0 zoom 0.8
show evfg lilly_goodend:
    truecenter
    zoom 6.0 subpixel True
    1.0
    linear 0.5 zoom 1.2
    easein 12.0 zoom 0.8
with whiteout

"As we set off towards the school, that wonderful smile engraves itself onto my memory. That wonderful smile that we both share."

"Our pasts may be scattered and at times overshadowed by sadness, but they're also an irrevocable part of our lives and personalities. Even if I could change a single thing, I wouldn't, because my past was what led me here."

"That's why, even with all that's happened to us before, and all that may well befall us… together, we'll keep walking forwards."

"Forwards… towards the future. Our future."

window hide Dissolve(1.0)

stop ambient fadeout 2.0
stop music fadeout 2.0

scene black
with Dissolve(1.0)

with Pause(1.0)

return