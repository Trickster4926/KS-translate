label th_L1:

window hide None

scene black
with dissolve

play sound sfx_alarmclock

with Pause(2.0)

scene bg school_dormhisao
with openeye

window show

# "I wake to the annoying din of my alarm clock, its bright red numerals lighting up my face."
"เสียงอันน่ารำคาญจากนาฬิกาปลุกดังขึ้นทำให้ต้องลืมตาตื่น แสงสีแดงจากตัวเลขบนหน้าปัดส่องมากระทบใบหน้า"

play music music_dreamy fadein 2.0

# "It's the same alarm clock I had at home, one of the few remaining artifacts from my days before coming to Yamaku. I'd hoped that using it would help ease my transition into this new life."
"เป็นนาฬิกาปลุกเรือนเดียวกับที่ฉันเคยใช้ตอนอยู่ที่บ้านและเป็นหนึ่งในสิ่งของไม่กี่อย่างที่หลงเหลือจากชีวิตเก่า\nก่อนที่จะย้ายมาที่ยามากุ ฉันพกติดตัวมาด้วยหวังว่าจะช่วยให้ปรับตัวเข้ากับชีวิตใหม่นี้ได้ง่ายขึ้น"

# "No such luck, though."
"โชคไม่ดีที่มันไม่ได้ช่วยอะไร"

# "Groggily dragging myself out of bed, I wipe the sleep out of my eyes, then reach over to my desk. I open a couple of the bottles of medication strewn across it, and swallow a few pills dry."
"ฉันลุกขึ้นจากเตียงนอนอย่างเชื่องช้าขยี้ตาให้หายงัวเงียก่อนจะเอื้อมไปเปิดฝาขวดยาที่เรียงรายอยู่บนโต๊ะแล้วเท\nเม็ดยาออกมาโยนเข้าปากกลืนไปทั้งอย่างนั้น"

# "By now, the process is starting to become automatic - something I should be glad for, given their purpose."
"ฉันทำแบบนี้ทุกวันจนตอนนี้เริ่มทำโดยอัตโนมัติไปแล้ว ซึ่งควรยินดีที่ทำได้โดยอัตโนมัติ เพราะถ้าไม่ทำก็คงไม่ได้\nมีชีวิตอยู่แล้ว"

$ renpy.music.set_volume(0.5, 2.0, channel="music")

scene bg school_dormbathroom
with locationskip

# "Feeling much more awake than before, I wander into the bathroom."
"พอหายง่วงแล้วฉันก็เดินไปเข้าห้องน้ำ"

play ambient sfx_shower fadein 8.0

show steam
with charaenter

# "While the shower warms up, my mind begins to wander as my new daily routine begins once again."
"ขณะที่น้ำอุ่นจากฝักบัวไหลลงมาบนหัว ใจของฉันก็เริ่มลอยออกไปในตอนที่กิจวัตรประจำวันใหม่ได้เริ่มต้นอีกครั้ง"

# "The bright colors of the fireworks fill my mind, as do the two girls with whom I spent my time watching them. It feels strange to be moved so much by people I know so little about."
"ภาพของดอกไม้ไฟหลากสีสันเป็นประกายประดับฟ้ากับเด็กสาวสองคนที่ฉันได้ใช้เวลาร่วมกันก็ปรากฏขึ้นในใจ\nแปลกดี ทั้งที่เจอกันได้ไม่นานแต่ยังรู้สึกประทับใจได้ขนาดนี้"

# "Then again, I suppose these aren't normal circumstances. At least I have someone to talk to, now, aside from my schoolmate next door."
"อาจเป็นเพราะสถานการณ์ไม่ปกติ แต่อย่างน้อยตอนนี้ฉันก็มีคนที่สามารถพูดคุยด้วยได้แล้ว\nนอกจากนายเพื่อนร่วมสถาบันที่อาศัยอยู่ห้องข้าง ๆ คนนั้น"

stop ambient fadeout 2.0

hide steam
with charaexit

# "With the time left before school begins today waning, I begin to get ready for class."
"เวลาที่เหลือก่อนเข้าเรียนวันนี้หมดไปทุกขณะ ฉันรีบเตรียมตัวไปเรียน"

$ renpy.music.set_volume(1.0, 3.0, channel="music")

scene bg school_scienceroom
with shorttimeskip

# "Walking through the door into the classroom, I notice that I'm still somewhat early. I see about five or six students milling around, most of them looking as if they'd rather be still in bed."
"เมื่อเดินผ่านประตูเข้ามาในห้องเรียนแล้วถึงรู้ตัวว่ามาค่อนข้างเช้า มองไปในห้องก็เห็นนักเรียนคนอื่นอีกประมาณ\nห้าหกคนมีสีหน้าเหมือนยังไม่อยากลุกขึ้นจากเตียงกันเกือบทุกคน"

# "It's at times like this that I appreciate being a morning person. That said, two students in particular seem just as perky as always."
"เพราะอะไรแบบนี้นี่แหละที่ทำให้ฉันรู้สึกขอบคุณที่ตัวเองเป็นคนตื่นเช้า แต่ถึงอย่างนั้นในห้องก็ยังมีนักเรียนอยู่สองคน\nที่มีท่าทีกระปรี้กระเปร่าอยู่เช่นเคย"

# hi "Hi Shizune, hi Misha."
hi "ไง ชิซูเนะ ไง มิช่า"

show shizu behind_blank at tworight
show misha perky_smile at twoleft
with charaenter

# "I suddenly realize that my greeting would be lost on the former, so I quickly follow it up with a wave. She doesn't seem overly bothered."
"ฉันนึกขึ้นได้ว่าคนที่ฉันทักเป็นคนแรกคงไม่ได้ยินคำทักทายนั้นจึงรีบยกมือขึ้นโบกทักทายตามไป แต่ก็เหมือนว่าเธอ\nจะไม่ได้คิดมากอะไร"

# "Or interested, for that matter."
"หรือไม่ได้สนใจเลยด้วยซ้ำ"

show shizu basic_normal
with charachange

shi "…"

show misha hips_grin
with charachange

# mi "Hello, Hicchan~! Are you feeling well?"
mi "สวัสดีฮิจัง~! สบายดีมั้ยเอ่ย"

# "I can only assume her greeting comes from Shizune. It's hard to tell if she's speaking as herself or Shizune, sometimes."
"ชิซูเนะน่าจะเป็นคนทักทายแหละ เดาเอาน่ะนะ เพราะบางครั้งก็ดูไม่ออกว่าที่พูดคือมิช่าพูดเองหรือแปลมาจากชิซูเนะ\nกันแน่"

# hi "Better than most everyone else, I guess. You two seem bright and chipper."
hi "ก็คงดีกว่าคนอื่น ๆ อยู่ละมั้ง พวกเธอเองก็ดูร่าเริงสดใสดีนี่"

show misha sign_smile
with charachange

show misha perky_smile
show shizu basic_frown
with charachange

# "Misha signs this back to Shizune as I say it, eliciting a somewhat terse answer, if her sharp and rapid arm movements are any indication."
"พอฉันพูดแล้วมิช่าก็แปลเป็นภาษามือไปตาม ดูจากการขยับแขนที่รวดเร็วและปุบปับนั้นแล้วก็น่าจะเป็นการแปล\nแบบรวบรัด"

# "Considering that these two made such a big deal out of the festival preparations, I probably should've chosen my words more carefully."
"แต่ฉันน่าจะระวังคำพูดหน่อย เพราะสองคนนี้ก็เป็นคนที่ลงแรงทุ่มเตรียมงานเทศกาลไปมาก"

show shizu behind_frown
with charachange

shi "…!"

show misha hips_grin
with charachange

# mi "Since you're a new student, we've been cutting you some slack. Please don't expect this kind of task-dodging to be allowed in the future."
mi "ที่พวกเราปล่อยนายไปเพราะนายเป็นนักเรียนใหม่หรอกนะ แต่หลังจากนี้อย่าคิดว่าพวกเราจะให้นายอู้งานแบบนี้อีก"

# "Misha looks as if she's about to add her own comment, but quickly goes back to interpreting as Shizune continues, unabated."
"มิช่าเหมือนจะอยากพูดอะไรเสริมอีก แต่ก็ต้องแปลภาษามือจากชิซูเนะต่อทันที"

show shizu basic_frown
show misha sign_smile
with charachange

# mi "While your contribution to class 3-2's stall is appreciated—"
mi "พวกเรายินดีที่นายช่วยแผงห้อง 3-2 แต่—"

# "Huh. Word sure got around quickly. That, or these two have their fingers on the pulse of the school."
"หืม ข่าวแพร่เร็วอยู่นะเนี่ย หรือไม่ก็สองคนนี้รู้ความเป็นไปของโรงเรียนเป็นเรื่องปกติอยู่แล้ว"

show misha hips_frown
with charachange

# mi "—we would prefer your efforts to be focused on the task at hand. Namely, your own class."
mi "—พวกเราอยากให้นายมาจัดการภาระหน้าที่ที่ต้องทำมากกว่า หรือก็คือ ห้องตัวเอง"

# "As much as I hate to admit it, they do have a point. Before I can respond, though, Shizune adds something more, which draws a smile from Misha."
"ถึงจะไม่อยากยอมรับสักเท่าไหร่ แต่ก็จริงของพวกเธอ แต่ชิซูเนะก็เสริมอะไรอีกสักอย่างก่อนฉันจะทันได้ตอบ พอมิช่าได้เห็นก็ทำหน้ายิ้ม ๆ"

show shizu behind_blank
with charachange

shi "…"

show misha perky_smile
with charachange

# mi "Did you enjoy the festival, then~?"
mi "แล้วงานเทศกาลสนุกมั้ย~"

# "Lecture over, I guess."
"เทศน์เสร็จแล้วมั้ง"

# hi "Yeah, it was good. Did you two enjoy it?"
hi "อื้ม สนุกดี เธอสองคนล่ะ"

show shizu behind_smile
show misha hips_grin
with charachange

# "Shizune gives a short nod as Misha grins and bounces her head up and down. The contrast, side-by-side, is amusing."
"ชิซูเนะพยักหน้าน้อย ๆ ส่วนมิช่าโยกหัวขึ้นลงแรง ๆ พอได้เห็นสองท่าทีที่ขัดกันอยู่อย่างนี้แล้วก็ตลกดี"

# "Out of the corner of my eye, I notice more students starting to trickle into the classroom. A quick glance at my watch confirms that they're a few minutes late."
"ภาพคนที่เริ่มทยอยเข้าห้องมาขยับอยู่ตรงหางตาฉัน พอเหลือบมองนาฬิกาก็เห็นว่าคาบเรียนเริ่มไปแล้วสองสามนาที"

show hanako emb_downtimid at offscreenright
with None

show misha hips_grin at left
show shizu behind_smile at Transform(xpos=0.48)
show hanako emb_downsmile at Transform(xpos=1.0, xanchor=0.7)
show bg school_scienceroom at bgleft
with charamove

# "I look over to Hanako's seat and realize that she's already there, and contentedly reading a book. It makes me wonder just how long she's been there without me noticing."
"พอมองไปที่โต๊ะของฮานาโกะก็เห็นเธอนั่งอ่านหนังสืออย่างสบายใจอยู่ตรงนั้น มานั่งนานหรือยังเนี่ย ไม่ทันสังเกตเลย"

show misha hips_grin:
    ease 1.0 xpos 0.2
show shizu behind_smile:
    ease 1.0 tworight
show hanako emb_downsmile:
    ease 1.0 offscreenright
show bg school_scienceroom:
    ease 1.0 center
with None

hide misha
hide shizu
hide hanako
with Dissolve(1.0)

# "With heavy footsteps coming up the hallway signaling Mutou's arrival, our idle talking comes to an end and I take my seat next to Misha."
"เสียงฝีเท้าหนัก ๆ เป็นสัญญาณการมาถึงของมุโต้ บทสนทนาเรื่องเปื่อยของพวกเราเป็นอันต้องจบลง ฉันมานั่งอยู่\nข้างมิช่า"

# "As the door slides open, he strides through with a ponderous gait. His posture is even worse than usual, and his eyes are barely staying open. I guess my quip to Lilly and Hanako about the staff was misplaced."
"ครูเลื่อนเปิดประตูเข้ามาด้วยท่าทีเอื่อยเฉื่อย ท่ายืนของครูดูแย่กว่าทุกทีอีก ตาก็ปรือแทบไม่เปิดแล้ว สงสัยที่ฉันบ่น\nกับลิลลี่กับฮานาโกะเรื่องคนในโรงเรียนคงจะแรงไปหน่อย"

play ambient sfx_paperruffling

# "Everyone opens their books as he reaches his desk, and the first class of the new week begins."
"พอครูนั่งที่แล้วทุกคนก็เปิดหนังสือ และคาบเรียนแรกของสัปดาห์ก็เริ่มขึ้น"

stop music fadeout 3.0
stop ambient fadeout 0.5

with shorttimeskip

play sound sfx_normalbell

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 2.0

# "I rub my eyes as the lunch bell rings out, glad for the temporary reprieve from work."
"ฉันขยี้ตาเมื่อได้ยินเสียงระฆังพักเที่ยง อย่างน้อยก็ได้พักจากการทำงานสักหน่อยละนะ"

show lilly basic_smileclosed at offscreenleft
with None

show bg school_scienceroom at bgright
show lilly cane_smileclosed at Transform(xanchor=0.2)
with charamove

# "I'm entirely unsurprised when I look over to the door and see Lilly standing there, cane in hand, patiently waiting for Hanako."
"เมื่อมองไปทางประตูก็เห็นลิลลี่ยืนอยู่ตรงนั้น ซึ่งฉันไม่แปลกใจเลย เธอยืนถือไม้เท้ารอฮานาโกะอย่างใจเย็น"

# "Considering her acceptance of my request to join them yesterday, I decide to spend my lunchtime with them rather than eat alone."
"ไหน ๆ เมื่อวานก็ตกลงให้อยู่ด้วยได้แล้ว ฉันจึงตัดสินใจไปกินข้าวเที่ยงกับพวกเธอแทนที่จะไปกินคนเดียว"

show hanako emb_smile at Alphain(0.5), Slide(0.5,0.5,0.4,0.5,0.5)
with Pause(0.5)

hide hanako
hide lilly
with charaexit

# "Hanako moves surprisingly fast to meet her companion, and the two enter the hallway before I can catch up."
"ฮานาโกะเดินไปหาเพื่อนของเธออย่างรวดเร็วจนน่าตกใจ ทั้งสองคนเดินไปตามโถงทางเดินก่อนฉันจะทันได้ตามไป"

stop ambient fadeout 1.0

scene bg school_hallway3
show lilly back_listen at twoleft
show lillyprop back_cane at twoleft
show hanako emb_downsmile at tworight
with locationchange

show hanako def_shock
with vpunch

# "Lilly's head turns slightly, registering the sound of footsteps behind her. As Hanako notices and follows her lead, she almost jumps in surprise."
"ลิลลี่หันหน้ามาเล็กน้อยคอยฟังเสียงฝีเท้าที่ตามเธอมา พอฮานาโกะหันหน้ามามองตามก็แทบสะดุ้งด้วยความตกใจ"

show hanako defarms_strain
with charachange

# ha "Hi… Hisao?"
hi "ฮิ… ฮิซาโอะ?"

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play music music_normal fadein 2.0

show hanako emb_blushtimid
with charachange

# ha "I mean… um… hello, Hisao…"
hi "ไม่สิ… เอ่อ… สวัสดี ฮิซาโอะ…"

# hi "Hi. Sorry if I startled you."
hi "ไง ถ้าตกใจก็ขอโทษทีนะ"

show lilly cane_smile
hide lillyprop
with charachange

# "Lilly turns to greet me, helped in her orientation by Hanako."
"ลิลลี่หันมาทักทายโดยมีฮานาโกะคอยนำทิศ"

show lilly cane_smileclosed
with charachange

# li "Good afternoon, Hisao. Are you joining us?"
li "ทิวาสวัสดิ์จ้ะฮิซาโอะ จะมาด้วยเหรอจ๊ะ"

# hi "If it's no trouble. There's not much else to do, really."
hi "ถ้าไม่เป็นการรบกวนน่ะนะ ยังไงก็ไม่มีอะไรทำเท่าไหร่อยู่แล้ว"

show lilly cane_smile
with charachange

# "Lilly gives a small nod, as if to silently brush away any idea that it would be troubling in the least."
"ลิลลี่พยักหน้าน้อย ๆ ราวกับจะสื่อว่าไม่เป็นการรบกวนเลยแม้แต่น้อย"

scene bg school_staircase2
with locationchange

with Pause(0.3)

scene bg school_hallway2
with locationchange

# "We descend one set of stairs and walk down the hallway to the usual room, our pace somewhat quicker than usual thanks to Lilly using Hanako for direction, rather than her cane and the railings."
"พวกเราเดินลงบันไดและมาตามโถงทางเดินมายังห้องประจำโดยใช้เวลาค่อนข้างน้อยเพราะลิลลี่มีฮานาโกะคอย\nนำทางอยู่ ไม่ได้ใช้เพียงไม้เท้าและราวเหล็กตามกำแพง"

scene bg school_miyagi
with locationchange

# "As expected, it's deserted. The sounds of the other clubs can only barely be heard as sunlight streams into the room from outside."
"ซึ่งโล่งตามคาด เสียงชมรมอื่นแว่วมาไกล ๆ แสงแดดสาดส่องห้องผ่านหน้าต่างมา"

# "Looking around the room, I notice a couple of empty easels propped up against a wall that I don't think were there before. The art club must use this room as extra storage."
"พอมองไปรอบ ๆ ห้องก็เห็นขาตั้งรูปวาดตั้งอยู่ตามกำแพงอยู่สองสามตัว เหมือนก่อนหน้านี้จะไม่มี ชมรมศิลปะ\nคงใช้ห้องนี้เป็นห้องเก็บของเพิ่มมั้ง"

show hanako emb_smile
with charaenter

# ha "Should I get the chess set out?"
ha "ให้ไปหยิบชุดหมากรุกมาให้มั้ย"

# "Hanako's voice seems less tense when she's directly addressing Lilly."
"เสียงฮานาโกะดูเกร็งน้อยลงเมื่อเธอพูดกับลิลลี่"

show hanako emb_smile at tworight
show bg school_miyagi at bgright
with charamove

show lilly cane_weaksmile at twoleft
with charaenter

# li "Yes. I'll make tea while you sort the pieces."
li "จ้ะ เดี๋ยวฉันจะไปชงชาให้ระหว่างที่เธอจัดกระดานนะ"

# hi "Ah, I can do that for you, if you'd like."
hi "เอ้อ ให้ฉันชงให้ก็ได้นะ ถ้าเธอไม่ว่าอะไร"

show lilly cane_surprised
with charachange

with Pause(0.3)

show lilly cane_planned
with charachange

# "She ponders the offer for a moment before smiling, confirming that I've made the right choice. Her face is remarkably easy to read."
"เธอคิดอยู่เงียบ ๆ ก่อนจะยิ้มเป็นการยืนยันว่าฉันคิดถูกแล้วที่เสนอตัวช่วย สีหน้าเธอนั้นดูออกง่ายทีเดียว"

show lilly cane_satisfied
with charachange

# li "Very well. Thank you."
li "ได้เลยจ้ะ ขอบคุณนะจ๊ะ"

show lilly cane_satisfied:
    ease 0.5 ypos 1.3
    "lilly basic_cheerful" with Dissolve(0.5, alpha=True)
    ease 0.5 ypos 1.0
with Pause(1.0)

hide lilly
hide hanako
with charaexit

# "She slides her retracted cane into the handle of her bag and sets it against one of the table legs, before taking a seat opposite Hanako."
"เธอถือไม้เท้าไว้กับมือจับกระเป๋าหิ้วก่อนจะหดไม้เท้าเข้ามาแล้ววางกระเป๋าไว้ที่ขาโต๊ะขาหนึ่ง ก่อนจะนั่งลงที่ฝั่งตรงข้าม\nฮานาโกะ"

# "As I prepare tea for the three of us, I can hear the small wooden pieces being set on the board. I wonder how good Lilly is at chess, given her circumstances."
"เสียงหมากไม้ที่ถูกจัดอยู่บนกระดานแว่วเข้าหูมาระหว่างที่ฉันชงชาให้พวกเราสามคน ลิลลี่จะเล่นหมากรุกได้เก่ง\nขนาดไหนกันนะ ยิ่งมองไม่เห็นหมากด้วย"

# "By the time I place the steaming teacups onto the table, Lilly and Hanako have already moved their first pieces as they nibble on sandwiches and rice balls from their respective bags."
"กว่าฉันจะได้มาวางน้ำชาร้อน ๆ ที่ควันลอยฉุย ลิลลี่กับฮานาโกะต่างก็ขยับหมากตัวแรกกันไปแล้ว ทั้งสองคนต่าง\nกัดกินแซนด์วิชและข้าวปั้นที่แต่ละคนเตรียมมากัน"

$ renpy.music.set_volume(0.5, 2.0, channel="music")

show chessboard:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

# "I note that the chessboard they're using has holes in the middle of each square and pegs on the bottom of the pieces, and has each dark square slightly raised."
"ฉันสังเกตเห็นว่าแต่ละช่องบนกระดานจะมีรูอยู่ ส่วนข้างใต้หมากแต่ละตัวจะมีหมุดที่นูนออกมา และช่องที่เป็นสีดำ\nจะนูนขึ้นมาเล็กน้อย"

# "Watching Lilly's fingers skating over the board, tracing out the positions of the pieces, makes me marvel a little at the simple ingenuity of the design. It must be specifically made for blind players."
"เมื่อได้เห็นลิลลี่กวาดนิ้วไปตามกระดานคลำหาตำแหน่งหมากแล้วฉันก็ทึ่งอยู่หน่อย ๆ กับการออกแบบที่เรียบง่ายแต่\nชาญฉลาดนี้ คงทำมาสำหรับคนตาบอดโดยเฉพาะ"

$ renpy.music.set_volume(1.0, 5.0, channel="music")

show chessboard:
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide chessboard
with None

# hi "Here you go."
hi "เอ้านี่"

scene bg tearoom_everyone_noon
show tearoom_hanae happy
show tearoom_lillye smileclosed
show tearoom_hisaoe hsmile
show tearoom_chess
with locationskip

# "Hanako gives a small nod as I put down the cup next to her side of the board. Lilly's hand ventures sideways slightly, so I gently place the cup touching the tips of her fingers; a gesture she seems to appreciate."
"เมื่อฉันวางถ้วยน้ำชาไว้ที่ข้างกระดานฝั่งฮานาโกะแล้วเธอก็พยักหน้าให้น้อย ๆ มือของลิลลี่เคลื่อนไปด้านข้างเล็กน้อย\nคล้ายเป็นการขอบคุณ ฉันจึงวางถ้วยน้ำชาเบา ๆ ให้แตะเข้ากับปลายนิ้วของเธอ "

show tearoom_hisaoe outside
with charachange

# "I finally take a seat and silently sip my tea as the two play. The contrast in their appearances while playing is interesting to watch."
"และฉันก็นั่งลงดูทั้งสองคนเล่นหมากรุก สีหน้าพวกเธอที่แตกต่างกันตอนเล่นนั้นดูน่าสนใจทีเดียว"

show tearoom_hanae open
with charachange

# "Hanako looks closely at the board, her face one of focused concentration. Lilly, on the other hand, keeps her head level and maintains her calm neutrality."
"ฮานาโกะมองกระดานใกล้ ๆ ทำสีหน้าจดจ่อเต็มที่ ส่วนลิลลี่นั้นวางหน้าคล้ายมองตรงดูเรียบนิ่ง"

# "Lilly's gentle voice addresses both of us as she continues to play."
"ลิลลี่ทักฉันกับฮานาโกะขึ้นมาระหว่างที่เธอเดินหมาก"

show tearoom_lillye smile
with charachange

# li "How was class, now that the festival's over?"
li "เลิกงานเทศกาลแล้วที่ห้องเป็นยังไงบ้างจ๊ะ"

show tearoom_hanae shy
show tearoom_hisaoe hthink
with charachange

# "I look to Hanako to see whether she'll answer first, but see that she's doing the same."
"ฉันหันไปดูว่าฮานาโกะจะตอบก่อนหรือเปล่า แต่เธอก็หันมาทางฉันเหมือนกัน"

show tearoom_hisaoe sigh
with charachange

# hi "Not… great. Half the class seemed to be dozing off, even including the teacher. Not to mention a test on top of all that."
hi "ไม่ค่อย… ดีเท่าไหร่ คนเกือบครึ่งห้องเหมือนจะนั่งสัปหงกกัน ครูก็ด้วย แล้วไหนจะมีสอบอีก"

show tearoom_hanae happy
with charachange

# "Hanako quietly adds her own agreement with this."
"ฮานาโกะทำท่าว่าเห็นด้วย"

show tearoom_lillye ara
with charachange

# li "I could imagine that being a bit difficult for you, being a transfer student."
li "เธอเป็นนักเรียนใหม่ด้วย คงลำบากหน่อยนะจ๊ะ"

show tearoom_hisaoe lsmile
with charachange

# hi "Well, I think I did fine. Other than the shock of a test coming so early, science is probably my best subject."
hi "อืม ก็พอไหวอยู่นะ อาจจะมีตกใจที่ว่าสอบเร็วขนาดนี้ วิทย์นี่ฉันน่าจะถนัดสุดแล้วมั้ง"

show tearoom_hisaoe hsmile
with charachange

# hi "How'd you do, Hanako?"
hi "แล้วเธอล่ะฮานาโกะ"

show tearoom_hanae open
with charachange

# ha "Me? Ah… okay… I guess…"
ha "ฉัน? เอ่อ… โอเค… ละมั้งนะ…"

# "Hanako's too sincere to be able to pull off lying very well. That much is obvious."
"เห็นได้ชัดว่าฮานาโกะนั้นเป็นคนซื่อเกินไปจนโกหกไม่เนียนเท่าไหร่"

show tearoom_lillye thinking
with charachange

# "Lilly's smile slips very slightly. From her reaction, Hanako mustn't be skilled enough at academics to do very well without preparation."
"ลิลลี่ยิ้มบาง ๆ ดูจากสีหน้าแล้วฮานาโกะคงเป็นจำพวกที่ถ้าไม่ได้เตรียมตัวอะไรแล้วคงเรียนหรือสอบไม่ค่อยได้เท่าไหร่"

show tearoom_hisaoe lsmile
with charachange

# hi "How did your class handle it, Lilly?"
hi "แล้วห้องเธอล่ะลิลลี่"

show tearoom_lillye giggle
with charachange

# li "It went surprisingly well, actually. Only one student was absent, which was better than what the teacher expected."
li "ที่จริงก็ดีเหลือเชื่อเลยจ้ะ มีนักเรียนไม่มาหนึ่งคน ซึ่งก็ยังดีกว่าที่คุณครูเขาคิดไว้"

show tearoom_hanae shy
show tearoom_lillye smileclosed
with charachange

# "With the topic all but run dry, the two concentrate on their chess game once again."
"พอหมดเรื่องจะคุยแล้วทั้งสองคนก็จดจ่ออยู่กับหมากรุกอีกครั้ง"

show tearoom_hisaoe relief
with charachange

# "I can't say I've ever liked the idea of chess as a spectator sport, but given its unique nature, for once I'm rapt in watching the game unfold."
"ฉันเองก็ไม่เคยคิดมาก่อนว่าการดูหมากรุกนั้นจะสนุกได้ แต่เอกลักษณ์ของเกมนี้ก็ดึงดูดให้ฉันคอยจับตาดูกระดาน\nที่ดำเนินไปเรื่อย ๆ"

show tearoom_hisaoe outside
show tearoom_hanae sad
with shorttimeskip

# "As time wears on, both of them demonstrate decent skill at playing the game. Having captured two more pawns than Hanako, Lilly has the upper hand, but only slightly."
"ยิ่งเวลาผ่านไปฉันก็ได้เห็นทักษะของทั้งสองคนซึ่งดีในระดับหนึ่ง ลิลลี่ได้เปรียบกว่าฮานาโกะเล็กน้อยเนื่องจากเธอ\nได้กินเบี้ยมากกว่าอีกฝ่ายอยู่สองตัว"

show tearoom_hanae open
show tearoom_hisaoe hunsure
with charachange

# "…until Hanako makes a strange move with her queen. Seizing upon this lapse in judgment, Lilly takes the piece with her knight."
"…ซึ่งก็ได้เปรียบไปจนกระทั่งฮานาโกะเดินควีนมาแบบแปลก ๆ ลิลลี่ใช้ช่องโหว่จากการที่ฮานาโกะตัดสินใจพลาดนี้\nเข้ากินควีนด้วยม้าของเธอ"

show tearoom_hanae shy
with charachange

# "Without hesitation, Hanako moves a pawn to take Lilly's rook on the opposite side of the board, and promotes it to queen."
"และฮานาโกะก็เข้ากินเรือของลิลลี่ที่อยู่อีกฝั่งกระดานทันทีก่อนจะเลื่อนขั้นเป็นควีน"

show tearoom_lillye thinking
show tearoom_hisaoe lunsure
with charachange

# "Lilly's face falters as her fingers move over the pieces and she realizes that she just fell to Hanako's trap. It's a little distracting to have the board traced out after each move, even if it's out of necessity."
"ลิลลี่ผงะไปเมื่อเธอคลำกระดานแล้วรู้ตัวว่าตัวเองเข้าติดกับของฮานาโกะแล้ว การที่ต้องมาคลำกระดานทุกตาเดิน\nอย่างนี้แล้วก็คงเสียสมาธิอยู่หน่อย ๆ ถึงจะจำเป็นต้องทำก็เถอะ"

# "Judging by Hanako's lack of reaction, she must be used to this. She and Lilly must have played at least a few games of chess against each other, after all."
"ฮานาโกะน่าจะชินแล้ว ดูจากท่าทางของเธอที่ไม่เปลี่ยนไปเลย ก็ทั้งสองคนคงเลยเล่นหมากรุกด้วยกันมาบ้างแล้วนี่นะ"

# ha "Check."
ha "รุก"

show tearoom_hisaoe hsmile
with charachange

# hi "That's not bad at all. Nice, Hanako."
hi "ไม่เลวเลยนี่ เยี่ยมเลย ฮานาโกะ"

show tearoom_hanae happy
with charachange

# "The compliment causes her to flower into a surprised blush."
"คำชมนั้นทำให้เธอตกใจจนหน้าแดง"

# ha "Th-thank you. I didn't… think it would work."
ha "ขะ ขอบคุณนะ ฉันไม่คิด… ว่าจะดักได้"

show tearoom_hisaoe lsmile
with charachange

# "I look over to Lilly, her fingers having just finished tracing out the position of her remaining pieces in an attempt to extricate her king from this bind."
"ฉันมองไปทางลิลลี่ที่เพิ่งยกมือจากการคลำหมากที่เหลืออยู่เพื่อหาทางออกให้คิงพ้นจากการบุกนี้"

# li "I think this is checkmate…"
li "เหมือนจะรุกจนแล้วนะ…"

show tearoom_hisaoe loops
with charachange

# hi "Hmm?"
hi "หืม?"

show tearoom_hisaoe relief
with charachange

# "I take another look at the board to confirm."
"ฉันมองกระดานอีกครั้งเป็นการยืนยัน"

# "Sure enough, her king has nowhere to escape without being threatened by another piece. My earlier question as to which of them is better at this has just been answered."
"ก็ใช่ คิงของลิลลี่หนีไปโดยไม่ติดตาเดินของหมากของฮานาโกะไม่ได้แล้ว จากที่ฉันนึกสงสัยเมื่อครู่ คราวนี้ฉันก็ได้รู้\nว่าใครเก่งกว่าใคร"

show tearoom_hisaoe sigh
with charachange

# hi "So it is."
hi "ใช่แล้ว"

show tearoom_lillye weaksmile
with charachange

# "Lilly gives a small sigh as Hanako smiles. From their reactions, this seems like a fairly usual result."
"ลิลลี่ถอนหายใจเบา ๆ ส่วนฮานาโกะก็ยิ้ม ดูจากสีหน้าแต่ละคนแล้ว ผลคงจะออกมาเป็นอย่างนี้อยู่บ่อย ๆ"

show tearoom_hisaoe lsmile
with charachange

# hi "How long have you two been playing?"
hi "เธอสองคนเล่นมานานแค่ไหนกันแล้วเหรอ"

show tearoom_hisaoe hsmile
show tearoom_hanae sad

with charachange

# ha "Since… I was young."
ha "ตั้งแต่… ตอนฉันเป็นเด็ก"

show tearoom_lillye smileclosed
show tearoom_hisaoe lsmile
with charachange

# "Lilly nods at Hanako's brief answer."
"ลิลลี่พยักหน้ากับคำตอบสั้น ๆ นั้นของฮานาโกะ"

show tearoom_lillye smile
with charachange

# li "Hanako taught me how to play soon after I met her. I can beat her every now and then… but that's a rarity. I don't seem to have the right mindset for it."
li "พอมาเจอกันได้สักพักฮานาโกะก็สอนฉันจ้ะ บางทีฉันก็ชนะเธอบ้าง… แต่ก็นาน ๆ ทีน่ะนะ ดูท่าว่าแนวคิดของฉัน\nจะนำทางให้เล่นไปจนชนะไม่ได้เท่าไหร่"

# "If Lilly came to Yamaku at the start of high school, and met Hanako when she moved to the dorms, that'd mean she's only been playing for about one year."
"ถ้าลิลลี่มาเรียนที่ยามากุตั้งแต่สมัยมัธยมปลายแล้วมาเจอฮานาโกะตอนย้ายมาอยู่ที่หอ แปลว่าคงเล่นมาได้ประมาณ\nปีเดียวเอง"

# "After seeing Hanako's level of play, I'm not too surprised Lilly has trouble beating her."
"ดูจากฝีมือการเล่นของฮานาโกะแล้ว ก็คงเป็นธรรมดาที่ลิลลี่จะเอาชนะฮานาโกะได้ยาก"

show tearoom_hanae happy
show tearoom_hisaoe hthink
with charachange

# ha "But… she's better at languages than I am, so…"
ha "แต่ว่า… ลิลลี่เก่งภาษากว่าฉัน เพราะงั้น…"

show tearoom_lillye ara
show tearoom_hisaoe lthink
with charachange

# "Lilly gives an appreciative, if slightly amused, smile at Hanako's quick reversal of her compliment."
"ลิลลี่ยิ้ม ๆ เหมือนขอบคุณที่ฮานาโกะชมย้อนได้เร็วขนาดนั้น"

show tearoom_lillye weaksmile
with charachange

# li "Well, that's how it is."
li "แหม คงงั้นแหละมั้งจ๊ะ"

stop music fadeout 3.0
play sound sfx_warningbell

# "Much to everyone's surprise, the bell suddenly rings, heralding an end to the lunch break."
"ทุกคนต่างตกใจที่อยู่ ๆ ระฆังที่ส่งสัญญาณว่าหมดพักเที่ยงดัง"

show tearoom_lillye thinking
show tearoom_hisaoe loops
with charachange

# li "Hmm, that game lasted longer than I thought it did."
li "อืมม เล่นนานกว่าที่คิดเลยนะเนี่ย"

# hi "Same. I guess we'd better get back to class."
hi "นั่นสิ คงต้องกลับไปเรียนแล้วละนะ"

show tearoom_hanae shy
show tearoom_lillye weaksmile
show tearoom_hisaoe thinkclosed
with charachange

# "Hanako's already in the middle of packing up, so I take Lilly's bag and offer it to her. To my surprise, she takes it and nods, but then places it back down on the table."
"ฮานาโกะเริ่มเก็บข้าวของของตัวเองแล้ว ฉันจึงหยิบกระเป๋าส่งให้ลิลลี่ ฉันแปลกใจที่เธอพยักหน้ารับไว้แล้ววางกระเป๋า\nลงกับโต๊ะ"

play music music_daily fadein 2.0

scene bg school_miyagi
show lilly basic_smileclosed at twoleft
show hanako basic_normal at tworight
with locationskip

# li "Hisao, may I make a request?"
li "ฮิซาโอะ ขออะไรอย่างได้มั้ยจ๊ะ"

# hi "Sure, go ahead."
hi "อื้ม ได้สิ"

show lilly basic_smile at twoleft
with charachange

# li "Would you mind if I were to quickly feel your face?"
li "เธอจะว่าอะไรมั้ยถ้าฉันขอจับหน้าเธอหน่อย"

# hi "Oh, uh… no, go ahead. I don't mind."
hi "อ้อ เอ่อ… ได้ จับเลย ฉันไม่ว่า"

# "The question takes me severely off guard, but once I regain my composure it seems sensible enough. So far Lilly's had no idea what I actually look like, and this would be her only way to find out."
"แวบแรกฉันตกใจกับคำขอนั้น แต่พอใจเย็นลงแล้วก็คิดได้ว่าเป็นคำขอที่ไม่ได้แปลกขนาดนั้น ตอนนี้ลิลลี่ยังไม่รู้ว่า\nหน้าตาฉันเป็นอย่างไร ซึ่งนี่เป็นวิธีเดียวที่เธอจะได้รู้"


$ renpy.music.set_volume(0.5, 1.0, channel="music")

show ev lilly_touch_uni
with GenericWhiteout(0.5,0.1,3.0)

# "Lilly raises her right hand, which I take in mine and guide to my face before letting go."
"ลิลลี่ยกมือขวาขึ้นมือ ฉันจับมือเธอดึงมาแตะที่หน้าฉันเบา ๆ แล้วปล่อยมือ"

# "The room is entirely silent as Lilly's hand moves over and around my features, from my chin, to my cheeks, to everywhere else."
"มีเพียงความเงียบในห้อง มือของลิลลี่ขยับไปรอบ ๆ ใบหน้าของฉัน ตั้งแต่คาง ขึ้นมาที่จมูก และที่อื่น ๆ บนใบหน้า"

# "I expected this to feel a lot more disquieting than it does.
# I suppose that's because the action is entirely a matter of practicality, being functionally no different to simply looking at someone's face."
"ทีแรกนึกว่าจะอึดอัดกว่านี้อีก แต่ที่ไม่อึดอัดก็คงเพราะการจับหน้าเป็นแค่วิธีการเท่านั้น ซึ่งเมื่อเทียบกันแล้วก็ไม่ต่าง\nอะไรกับการที่มองหน้าใครสักคนเฉย ๆ"

# "Her hand is soft, but what takes me by surprise is the length of her fingers, not to mention how sure even the slightest of her movements are. I have no doubt that her level of tactile feeling would be far beyond mine."
"มือของเธอนั้นนิ่ม แต่ที่ทำให้ฉันตกใจคือความยาวนิ้วเธอ และเธอสัมผัสได้แผ่วเบามากเสียจนไม่รู้ว่าเธอรู้สึกจริง ๆ\nหรือเปล่า ไม่ต้องสงสัยเลยว่าประสาทการสัมผัสของเธอนั้นคงดีกว่าฉันหลายเท่าตัว"

# "Her hand briefly runs once through my hair before retreating. I'm sure that every inch of my face has been committed to her memory. It's only now, too, that I realize Hanako has been silently watching the entire time."
"เธอสางผมฉันหนึ่งครั้งก่อนจะถอนมือออกไป ทุกตารางนิ้วบนใบหน้าฉันคงถูกบนทึกไว้ในความทรงจำเธอหมดแล้วเป็นแน่แท้ และฉันก็เพิ่งจะรู้ตัวว่าเมื่อกี้ฮานาโกะคอยมองอยู่เงียบ ๆ มาตลอด"

$ renpy.music.set_volume(1.0, 2.0, channel="music")

scene bg school_miyagi
show hanako basic_distant at tworight
show lilly basic_weaksmile_close at twoleft
with whiteout

# li "Thank you for letting me do that, Hisao."
li "ขอบคุณที่ให้ฉันจับหน้านะฮิซาโอะ"

show lilly basic_smile_close at twoleft
with charachange

# li "And if I might add, I think you are quite handsome."
li "แล้วก็ขอชมหน่อยว่าเธอหล่อใช้ได้เลยนะ"

# "I blush a little at her remark, before raising a questioning eyebrow."
"ฉันหน้าแดงเล็กน้อยกับคำชมนั้นก่อนจะยักคิ้วด้วยความสงสัย"

# hi "But if you can't see, how…"
hi "แต่ว่า เธอมองไม่เห็นนี่นา แล้ว…"

show lilly basic_pout_close at twoleft
with charachange

# li "Just because I can't see, that doesn't mean I don't have my own preferences."
li "การที่ฉันมองไม่เห็นไม่ได้แปลว่าฉันจะไม่มีแนวที่ชอบหรอกนะจ๊ะ"

show hanako emb_timid at tworight
with charachange

# ha "Um, we'd better go now…"
ha "เอ่อ เราต้องรีบไปกันได้แล้วนะ…"

# hi "Yeah, that's a good point. I guess we'll see you later then, Lilly."
hi "อื้ม นั่นสินะ งั้นเจอกันนะลิลลี่"

scene bg school_hallway2
show lilly basic_smile at twoleft
show hanako emb_smile at tworight
with locationskip

# "Walking through the hallways back to our classrooms, I notice that Hanako seems quieter than before, but also more comfortable."
"ระหว่างที่เดินไปตามโถงทางเดินฉันก็สังเกตเห็นว่าฮานาโกะดูเงียบกว่าปกติ แต่ก็ดูสบายใจขึ้นด้วย"

# "Lilly, her hand on Hanako's shoulder, seems to pick up on her assured pace as well, smiling as they walk."
"ลิลลี่จับไหล่ฮานาโกะไว้ เหมือนว่าเธอเองก็จับจังหวะเดินให้สบายได้แล้วเช่นกัน เธอเดินไปพลางยิ้ม"

# "If I could spend the rest of my time at Yamaku like this, I don't think it'd be so bad. All that's needed for joy are small exchanges of happiness, after all."
"การที่ต้องใช้เวลาที่เหลืออยู่ในรั้วยามากุเช่นนี้ไปจนจบก็คงไม่ใช่เรื่องที่แย่อะไร ยังไงเสีย แค่ได้ใช้เวลาอยู่ร่วมกัน\nอย่างมีความสุขเช่นนี้ฉันก็ยินดีมากแล้ว"

scene bg school_scienceroom
with locationskip

play sound sfx_rumble

# "As I reach my desk and set my bag beside it, I realize something. Or rather, my stomach does."
"พอฉันเดินมาถึงโต๊ะตัวเองแล้ววางกระเป๋าลงข้างโต๊ะก็นึกบางอย่างขึ้นได้ ไม่สิ เป็นท้องฉันที่นึกขึ้นได้มากกว่า"

# "I was so busy with those two, I forgot to buy lunch…"
"ฉันอยู่กับสองคนนั้นจนลืมซื้อข้าวเที่ยงไปเลย…"

stop music fadeout 2.0

scene black
with dissolve

#**************************************

label th_L2:

scene bg school_dormhisao
with locationchange

# "Saturday. My second most favorite day of the week."
"วันเสาร์ วันที่ฉันชอบเป็นอันดับสอง"

# "This is almost entirely due to the fact that it is the day with the second least amount of school, with class ending at the beginning of lunch."
"หลัก ๆ ที่ชอบก็เพราะวันนี้เป็นวันที่มีเรียนน้อยที่สุดเป็นอันดับสอง โดยจะเลิกเรียนก่อนพักเที่ยง"

scene bg school_dormhallway
with locationchange

# "I open my door confidently, myself being more than confident of being able to get enjoyment out of the fine weather and shorter class length."
"ฉันเปิดประตูด้วยความมั่นใจเป็นอย่างยิ่งว่าวันที่มีเรียนน้อยและอากาศดีเช่นนี้จะเป็นวันที่ดี"

scene bg school_dormhallground
with locationchange

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_footsteps_hard

# "I confidently stride down the hallway and down the stairs to the lobby of the male dorms."
"ฉันเดินอาด ๆ ไปตามโถงทางเดินลงบันไดไปที่โถงหอชายอย่างมั่นใจ"

$ renpy.music.set_volume(0.6, 4.0, channel="ambient")

# "I confidently look behind me to see whose footsteps are approaching."
"ฉันหันไปมองว่าเสียงฝีเท้าที่ตามมาว่าเป็นใครอย่างมั่นใจ"

$ renpy.music.set_volume(1.0, 4.0, channel="ambient")

# "I… lose my confidence in this day being enjoyable."
"ฉัน… ไม่มั่นใจแล้วว่าวันนี้จะเป็นวันที่ดี"

stop ambient
play music music_kenji fadein 0.5

show kenji happy:
    center
    xpos 0.4
    easein 0.5 xpos 0.5
with charaenter

# ke "Hey man. Sup?"
ke "ไงพวก ทำไร"

# hi "Not much I guess, just looking forward to the afternoon. You?"
hi "ไม่ทำไรมั้ง รอพักเที่ยงแหละ นายอะ"

show kenji happy_close at center
with characlose

# "He wraps an arm around my slumped shoulders far too comfortably. Something's up."
"เขาจับไหล่ฉันที่หย่อนลงด้วยความคุ้นเคยที่ออกจะมากเกินไป ชักจะแปลก ๆ แล้ว"

show kenji neutral_close
with charachange

# ke "Let's step outside, shall we?"
ke "ไปข้างนอกกัน"

# hi "I was just about to, before you stopped me."
hi "ก็กำลังจะไปเนี่ย แต่นายมาทักก่อน"

show kenji tsun_close
with charachange

scene bg school_dormext_full
with locationchange

# "He doesn't take my reaction to his theatrics well. Ignoring him, I walk outside and start down the steps."
"เคนจิไม่ได้สนใจที่ฉันตอบไปเลยแม้แต่น้อย ฉันเมินเขาแล้วเดินมาตามบันได"

# "It doesn't take too long for him to catch up with me again. I wonder if he wants money, or to rant about another conspiracy. Maybe both."
"ไม่นานนักเขาก็ตามมาจนทันกับฉัน นี่จะมายืมเงินหรือพล่ามเรื่องทฤษฎีสมคบคิดอีกล่ะเนี่ย คงจะทั้งสองอย่างมั้ง"

show kenji tsun:
    center
    xpos 0.6
    easein 0.5 xpos 0.5
with charaenter

# ke "I've got a bone to pick with you."
ke "ฉันอยากจะท้วงอะไรนายหน่อย"

# hi "Uh huh."
hi "อาฮะ"

# ke "It's about that blonde. You know who I'm talking about."
ke "เรื่องยัยผมสีบลอนด์นั่น นายรู้ใช่มั้ยว่าฉันพูดถึงใคร"

# "Conspiracy it is. For a moment I contemplate feigning ignorance, but realize this will go quicker if I just let him get it all out."
"ทฤษฎีสมคบคิดสินะ ฉันนึกชั่งใจอยู่ครู่หนึ่งว่าจะทำเป็นไขสือไปเลยดีไหม แต่บอก ๆ ไปเลยน่าจะจบเรื่องได้เร็วกว่า"

# hi "Lilly? The one from your class?"
hi "ลิลลี่ที่อยู่ห้องนายอะนะ"

show kenji rage at center
with vpunch

# ke "You're on first name terms with her?!"
ke "นี่สนิทถึงขั้นเรียกชื่อกันแล้วเหรอ!"

# "He looks positively shocked at this development. Did he not expect me to be able to answer?"
"เขาตกตะลึงพรึงเพริดไปเมื่อได้ยินเช่นนั้น นี่คิดว่าฉันจะไม่ตอบหรือไง"

show kenji tsun
with charachange

# "He gathers himself and coughs into his fist. Dramatically, like everything he does."
"เขาตั้งสติแล้วกระแอมใส่กำปั้นตัวเองอย่างเล่นใหญ่ ตามปกติที่ทำอะไรก็เวอร์หมดนั่นแหละ"

# ke "Well, never mind that. I'm here to warn you. You know. Man to man."
ke "เออ ช่างเหอะ ฉันมาเตือนนาย เนี่ย ในฐานะลูกผู้ชายด้วยกันไง"

# hi "Warn me about what? Lilly?"
hi "เตือนเรื่องอะไร ลิลลี่เหรอ"

# ke "Yeah. You don't know her, man."
ke "เออ นายจะไปรู้จักอะไรยัยนั่น"

# "It's mostly true. I've only known her and Hanako for less than two weeks, and even then we've just been exchanging banal chatter about school as we while away lunch."
"ก็จริงอยู่ ฉันรู้จักลิลลี่กับฮานาโกะมาได้ยังไม่ถึงสองสัปดาห์เลย แล้วที่คุยกันแต่ละทีก็คุยแต่อะไรพื้น ๆ เรื่องโรงเรียน\nไปเรื่อยเปื่อยตอนกินข้าวเที่ยงด้วยกัน"

# hi "I'm pretty sure you don't either."
hi "ฉันว่านายก็ไม่น่ารู้จักเหมือนกันนะ"

# ke "That's not the point. You're the one spending inordinate amounts of time with her."
ke "ฉันจะรู้จักมั้ยไม่ใช่ประเด็น นายนั่นแหละคือคนที่ใช้เวลามากเกินปกติกับยัยนั่น"

# "It distresses me that someone like Kenji, who's probably as far out of the loop as one could possibly get, knows about such a trivial fact as who I choose to befriend."
"คิดแล้วก็หดหู่ คนอย่างเคนจิที่สภาพน่าจะไม่รับรู้เรื่องข่าวสารบ้านเมืองอะไรสุด ๆ แล้วดันมารู้เรื่องหยุมหยิมอย่างเช่น\nว่าฉันไปเป็นเพื่อนกับใครคนไหนเนี่ย"

# "Then again… I am a transfer student, and she's not only the representative of their class, but also a tall blonde."
"แต่ก็นะ… ฉันย้ายมาใหม่ อีกฝั่งก็เป็นหัวหน้าห้อง แถมเป็นคนผมสีบลอนด์ที่ตัวสูงอีก"

# "Maybe I should appreciate this ranting as a warning that the rumor mill exists in this school, and that I'm firmly within it."
"บางทีการที่เขาพล่ามก็คงจะนับเป็นการเตือนได้ว่าโรงเรียนนี้ยังมีพวกเรื่องข่าวลืออยู่ แถมกระสุนก็ตกใส่หัวฉันได้แน่ ๆ"

# hi "It's just lunch. Nothing special."
hi "ก็แค่กินข้าวเที่ยงน่า ไม่มีอะไรเป็นพิเศษหรอก"

show kenji neutral
with charachange

# ke "Look, man, under the bridge. See this bridge? You're under it. A man's gotta do what a man's gotta do to get intel."
ke "เนี่ย พวก ที่ลับไง เห็นที่ลับตรงสะพานนั้นมั้ย นายอยู่ตรงที่ลับนั้นแหละ คนเราถ้าอยากได้ความลับต้องไปล้วงจากที่ลับเว้ย"

show kenji tsun
with charachange

# ke "I just want to make sure you don't end up too far under the bridge."
ke "ฉันแค่จะเตือนไม่ให้นายหลงในที่ลับจนลึกเกินไป"

# hi "You're losing me, Kenji."
hi "ยังไงนะเคนจิ ฉันตามไม่ทันละ"

show kenji happy
with charachange

# ke "That's okay, lots of people get lost. That's why I'm here to help."
ke "ไม่เป็นไร มีหลายคนแหละที่ตามอะไรไม่ทัน ฉันถึงได้มาช่วยยังไงละ"

scene bg school_gardens
show kenji neutral
with locationskip

# ke "Just be careful around her, okay? She looks all harmless on the outside, but I've heard shit. Bad shit."
ke "แค่ระวังตัวไว้ตอนอยู่กับยัยนั่นก็พอ ภายนอกอาจะดูไม่มีพิษภัย แต่ฉันได้ยินอะไรแย่ ๆ มาเยอะ"

show kenji tsun
with charachange

# ke "You know the Student Council, right?"
ke "นายรู้จักพวกสภานักเรียนใช่มั้ย"

# "He seems to involuntarily shudder as he says the words. Putting him and Shizune together in a room is an amusing mental exercise. I wonder if they've met."
"พอเขาพูดแล้วก็ตัวสั่นไปเหมือนไม่รู้ตัว คิดแล้วก็คงตลกดีถ้าจับเคนจิไปอยู่ในห้องเดียวกันกับชิซูเนะ สองคนนี้เคย\nเจอกันหรือยังนะ"

# hi "Yeah, Shizune and Misha are in my class. I seem to have dodged the draft, though."
hi "อืม ชิซูเนะกับมิช่าเรียนอยู่ห้องเดียวกันกับฉัน แต่เหมือนฉันจะหนีความตายมาได้น่ะนะ"

show kenji happy
with charachange

# ke "Good man. Good man."
ke "ดีแล้ว ดีแล้ว"

show kenji tsun
with charachange

# ke "But this blonde? She was there. In the Student Council. Right. Damn. There."
ke "แต่ยัยผมสีบลอนด์นั่นน่ะนะเคยเป็นสภานักเรียน เป็น สภา นักเรียน"

# hi "I see. And?"
hi "อ้อ แล้ว?"

# ke "And she's not there now."
ke "แล้วก็ไม่ได้เป็นแล้ว"

stop music fadeout 3.0

hi "…"

# ke "Seriously, think about it. Something must have gone down."
ke "เฮ้ย ลองคิดดูสิ มันต้องมีอะไรเกิดขึ้นแน่ ๆ"

# "I stop walking for a moment, giving the idea more thought than I probably should."
"ฉันหยุดยืนอยู่ครู่หนึ่งพลางคิด ซึ่งคิดแล้วก็น่าจะเปลืองสมองไปเหมือนกัน"

# "It would explain that fight the two had, at least in part. Wait, no, not really. Even leaving the Student Council would need a catalyst."
"ซึ่งถ้าเป็นอย่างนั้น การที่สองคนนั้นทะเลาะกันส่วนหนึ่งก็คงมาจากเรื่องสภานักเรียน เดี๋ยว ไม่สิ ไม่น่าใช่นะ เพราะการ\nที่จะลาออกจากสภานักเรียนได้มันต้องมีจุดเปลี่ยนสักอย่าง"

# "In the end, it doesn't explain much at all. Other than the fact that their feud goes back some ways."
"สุดท้ายแล้วก็ไม่ได้ความอะไรขึ้นมาเท่าไหร่ นอกจากได้รู้ว่าสองคนนี้ไม่ถูกกันมาแต่ไหนแต่ไรแล้ว"

# hi "I guess you have a point. I'm not seeing how that really affects me, though."
hi "ก็คงถูกของนายมั้ง แต่ก็ไม่เห็นว่าจะเกี่ยวอะไรกับฉันสักหน่อย"

show kenji neutral
with charachange

# ke "Okay, now field this one. Lilly's foreign, obviously."
ke "โอเค งั้นลองคิดตามนี้ดูนะ ลิลลี่เป็นคนต่างชาติ เห็น ๆ กันอยู่"

# hi "Obviously."
hi "เห็น"

# ke "Now, what nationality is she?"
ke "แล้วเป็นคนสัญชาติอะไร"

# "I open my mouth to give the answer, but realize that I have none. In fact, I've given the matter very little thought."
"ฉันอ้าปากเตรียมตอบ แต่แล้วก็นึกได้ว่าไม่มีคำตอบจะพูด ที่จริงฉันแทบไม่เคยคิดเรื่องนี้ด้วยซ้ำ"

# "Given that she has no accent and acts perfectly Japanese, I suppose it never really seemed important. Now that he mentions it though, I am rather curious."
"ฉันไม่ได้คิดว่าจะเป็นเรื่องสำคัญอะไรเพราะเห็นว่าลิลลี่ก็พูดไม่ติดสำเนียงต่างชาติ แถมทำตัวเป็นคนญี่ปุ่นตามปกติหมด\n แต่พอเคนจิถามแล้วก็อยากรู้ขึ้นมาเลยแฮะ"

# hi "To be honest, I don't know. Maybe English? They like tea."
hi "ว่าตามตรงฉันก็ไม่รู้เหมือนกัน อังกฤษมั้ง คนอังกฤษชอบชานี่"

# "I probably shouldn't resort to stereotypes, but that's the only lead I have."
"จริง ๆ ก็ไม่ควรใช้การเหมารวมอะไรอย่างนั้นมาเดาน่ะนะ แต่ก็พอจะเดาได้แค่นี้แหละ"

show kenji happy
with charachange

play music music_kenji fadein 1.0

# ke "You're not thinking. Luckily, you have me here to think for you."
ke "นายได้ใช้สมองมั้ยเนี่ย โชคยังดีนะที่นายมีสมองฉันให้ใช้อยู่"

# hi "Gee, thanks."
hi "เออ ขอบใจ"

# "He brushes off the quip effortlessly."
"เขาไม่ได้รู้ตัวเลยว่าฉันประชดไป"

show kenji neutral
with charachange

# ke "Now answer me this: who has lots of social power, is filthy stinking rich - you know blondes are all rich, right? - has a long history of disputes and used to belong to a much larger organization?"
ke "งั้นฉันจะถามก่อน คนที่ทั้งมีอำนาจ ทั้งรวย—นายรู้ใช่มั้ยว่าพวกผมสีบลอนด์น่ะรวยกันทั้งนั้น—ทั้งเคยมีเรื่องพิพาท\nทั้งหลายมายาวนาน ทั้งเคยอยู่องค์กรขนาดใหญ่ คือใคร"

# hi "The Roman Catholic Church?"
hi "พวกโรมันคาทอลิก?"

show kenji tsun
with charachange

# ke "…Well okay, there's that."
ke "…เอ่อ โอเค อันนั้นก็ใช่"

show kenji neutral
with charachange

# ke "But there's also the Mafia. Come on. Rich, foreign, there's no way she doesn't have connections to them."
ke "แต่อีกกลุ่มคือมาเฟียไง เนี่ย รวย เป็นคนต่างชาติ ยังไงยัยนั่นก็ต้องเกี่ยวกับพวกมาเฟียแน่ ๆ"

# "I have reason to doubt the logic of his deductions, but he shows no sign of stopping."
"ฉันว่าตรรกะการเชื่อมโยงของเขามันมีอะไรน่าสงสัยอยู่นะ แต่เขาก็ไม่มีทีท่าว่าจะหยุดพล่าม"

scene bg school_hallway3
show kenji neutral
with locationskip

# ke "So do you know where I think she's from?"
ke "แล้วรู้หรือยังว่าฉันคิดว่ายัยนั่นเป็นคนที่ไหน"

# hi "Italy?"
hi "อิตาลี?"

show kenji tsun
with charachange

# ke "Mainland Italy's small-time, dude. She has to be from Sicily. All those mafioso types come from there."
ke "อิตาลีแผ่นดินใหญ่น่ะจิ๊บจ๊อยมาก ยัยนั่นน่ะต้องเป็นคนซิซิลีแน่ ๆ พวกมาเฟียจะอยู่กันที่นั่นหมด"

show kenji happy
with charachange

# ke "Wait, no, Russia. Damn, this could be bad. The Mafia there is serious business, man; Ex-KGB everywhere, paramilitaries, hardcore smuggling, and—"
ke "เดี๋ยว ไม่สิ รัสเซียสิ ตายละ แย่แน่ ๆ ขบวนการมาเฟียในรัสเซียน่ะจริงจังกันมาก ไหนจะพวกที่เคยเป็นเคจีบี ไหนจะ\nพวกกำลังกึ่งทหาร ไหนจะพวกขนของเถื่อน แล้ว—"

# hi "Wait, wait, stop, just slow down a sec. What point are you trying to get at here?"
hi "เดี๋ยว เดี๋ยว หยุด ช้าก่อน นี่นายกำลังจะสื่อว่าอะไร"

show kenji neutral
with charachange

# ke "You don't know what she'll do, man. I won't get in your way - agents don't operate like that - but I just want you to be careful."
ke "นายไม่รู้หรอกว่ายัยนั่นคิดจะทำอะไร ฉันจะไม่เข้าไปขัดขวางนายหรอก เพราะพวกตัวแทนไม่ได้ทำงานกันอย่างนั้น\nแต่ฉันแค่อยากให้นายระวังตัวไว้"

show kenji tsun
with charachange

# ke "When the time comes, we'll need all the help we can get. I don't want to lose you, comrade."
ke "พอถึงเวลานั้น เราจะต้องรวบรวมกำลังมาให้ได้มากที่สุดเท่าที่จะหาได้ ฉันไม่อยากเสียนายไปหรอกนะสหาย"

# "Well, at least he's concerned for me. Kinda."
"เอาเหอะ อย่างน้อยก็นับได้ว่าเขาห่วงฉันแหละ"

stop music fadeout 4.0

show kenji tsun:
    center
    easeout 0.5 xpos 0.6 alpha 0.0
with None

# "I wave goodbye to him as we separate out to our respective classes, but I'm not sure that he sees the gesture."
"ฉันโบกมือลาเคนจิแยกย้ายกันไปเรียน แต่ฉันก็ไม่แน่ใจว่าเขาเห็นที่ฉันโบกมือหรือเปล่า"

scene bg school_scienceroom
with shorttimeskip

play ambient sfx_crowd_indoors fadein 2.0

# "Piling my books into my bag, I catch a glimpse of the library books I'd borrowed last week. I might as well return them, considering they took all of two days to finish."
"พอจัดหนังสือใส่กระเป๋าก็เหลือบไปเห็นหนังสือที่ยืมมาจากห้องสมุดเมื่อสัปดาห์ที่แล้ว เอาไปคืนดีกว่า ยังไงอ่านแค่\nสองวันก็จบแล้ว"

# "I briefly consider inviting Hanako along to the library, but she's already gone. It'll probably be better for my studying if I'm alone anyway."
"แวบหนึ่งฉันนึกจะชวนฮานาโกะไปห้องสมุดด้วย แต่เธอก็ไม่อยู่แล้ว แต่ยังไงอยู่คนเดียวน่าจะจดจ่อกับอ่านหนังสือเรียน\nได้ดีกว่าอยู่แล้วละนะ"

# "With a quick stretch and a wave to a couple of classmates who give the same to me, I make my way out of the classroom."
"ฉันบิดขี้เกียจแล้วโบกมือลาเพื่อนร่วมชั้นสองคนที่โบกมือตอบแล้วเดินออกมาจากห้องเรียน"

stop ambient fadeout 1.0

scene bg school_library
with locationskip

# "As I open my bag and shove the books through the returns slot in the front counter, I notice a strange person behind the desk. Old and graying, she must be Yuuko's replacement when she's working at the café."
"จังหวะที่เปิดกระเป๋าหยิบหนังสือเตรียมหย่อนตรงกล่องคืนหนังสือก็เหลือบไปเห็นคนมีอายุผมสีดอกเลาที่ดูแปลกตา\nคนหนึ่ง คงเป็นคนที่มาอยู่แทนช่วงที่ยูโกะทำงานที่คาเฟละมั้ง"

# "I begin looking for a free table, a task made somewhat difficult considering that, despite there not being many students in here, they're all sitting at their own tables."
"ฉันกวาดตามองหาโต๊ะว่าง ซึ่งหาแทบไม่เจอทั้งที่คนน้อยเพราะทุกคนต่างนั่งโต๊ะใครโต๊ะมันกันหมด"

# "Noticing a familiar head of hair, I walk over to one near the Braille section."
"พอเห็นทรงและสีผมที่คุ้นเคยฉันก็เดินไปที่ส่วนหนังสืออักษรเบรลล์"

show lilly basic_smileclosed
with charaenter

# "It's hard to tell whether Lilly's concentrating hard or not, her placid expression holding perfectly still as her finger slides across the dot-filled pages of her book."
"ฉันดูแทบไม่ออกว่าลิลลี่ตั้งสมาธิอยู่หรือเปล่า เพราะเธอยังทำสีหน้าเรียบนิ่งพลางคลำไปตามหน้าหนังสือที่มีจุด\nตะปุ่มตะป่ำ"

# hi "Hi. Mind if I sit here?"
hi "ไง ขอนั่งด้วยได้หรือเปล่า"

show lilly basic_surprised
with charachange

# li "Hmm? Oh, no problem at all…"
li "หืม อ้อ ได้สิ นั่งเลย…"

# "She trails off, evidently still focused on her business at hand."
"เสียงเธอแผ่วลงแสดงให้เห็นว่ากำลังตั้งใจอ่านอยู่"

play music music_lilly fadein 10.0

show lilly basic_smile
with charachange

# li "Ah, Hisao."
li "อ้อ ฮิซาโอะ"

show lilly basic_smileclosed
with charachange

# "She gives a nod of greeting as I sit opposite her at the table, pluck a chemistry textbook out of my bag and quickly thumb to the chapter we're covering in class."
"เธอพยักหน้าทักทายระหว่างที่ฉันหย่อนตัวลงนั่งที่เก้าอี้ฝั่งตรงข้ามเธอ ฉันหยิบหนังสือวิชาเคมีออกมาจากกระเป๋า\nแล้วกรีดหน้าหาบทที่กำลังเรียนอยู่"

# "For a while, we sit there and read, each in our own way."
"เราต่างนั่งอ่านหนังสือของตัวเองกันอยู่พักหนึ่ง"

# "Seeing her reminds me of what Kenji said this morning, though. That and the fact that I've never seen someone read in Braille before makes me keep throwing glances at her."
"แต่พอมองลิลลี่แล้วก็นึกถึงที่เคนจิพูดเมื่อเช้า แถมไม่เคยเห็นใครอ่านหนังสืออักษรเบรลล์มาก่อนด้วย ฉันจึงคอย\nเหลือบมองเธอเป็นระยะ ๆ"

# "I kind of feel guilty about it, given that she has no way to realize I'm doing so, so I decide to just ask her about it. Her lineage isn't exactly a state secret, after all, and there is another thing I've only just noticed from her movements."
"รู้สึกผิดอยู่เหมือนกันแฮะ เพราะมองยังไงลิลลี่ก็ไม่รู้ตัวอยู่แล้ว ถาม ๆ ไปเลยดีกว่า ยังไงเรื่องสายเลือดของลิลลี่ก็คงไม่ใช่\nความลับระดับชาติขนาดนั้น แล้วก็มีอีกอย่างที่เพิ่งสังเกตได้จากท่าทางด้วยเหมือนกัน"

# hi "Hey Lilly, mind if I ask a question?"
hi "นี่ ลิลลี่ ขอถามอะไรหน่อยได้ไหม"

show lilly basic_smile
with charachange

# li "Not at all. Is anything wrong?"
li "ถามได้เลยจ้ะ มีอะไรหรือเปล่า"

# hi "I was just wondering… you're at least part foreign, right?"
hi "ฉันแค่สงสัยว่า… อย่างน้อย ๆ เธอก็ต้องมีเชื้อทางต่างชาติบ้างแหละ ใช่มั้ย"

show lilly basic_giggle
with charachange

# "She gives a small giggle before setting down her book."
"เธอหัวเราะน้อย ๆ ก่อนจะวางหนังสือลง"

show lilly basic_cheerful
with charachange

# li "I've always been amused at how squeamish people are about that. Akira's mentioned how much she and I look different from most others before."
li "ฉันละแปลกใจจริง ๆ ที่พอมีคนถามเรื่องนี้ทีไรก็ชอบถามแบบอ้อม ๆ กัน พี่ก็เคยพูดอยู่เหมือนกันว่าเราสองคนลักษณะ\nดูไม่ค่อยเหมือนคนอื่นเท่าไหร่"

show lilly basic_smile
with charachange

# li "The details are a bit complicated, but I'm half Japanese, half Scottish."
li "รายละเอียดจริง ๆ ซับซ้อนอยู่นิดหน่อยนะ แต่ฉันเป็นลูกครึ่งญี่ปุ่น-สกอตแลนด์จ้ะ"

# "…Scottish? That was not exactly my first guess. It takes some effort to not blurt it out loud."
"…สกอตแลนด์เหรอ ผิดคาดไปหน่อยแฮะ ฉันต้องยั้งปากไว้ไม่ให้พูดออกไป"

# "I try to conjure images of the place in my mind. I think as far as the UK goes, Scotland isn't bad to live in… but I'm not really sure."
"ฉันลองนึกภาพประเทศสกอตแลนด์ดู ถ้าอิงจากสหราชอาณาจักรแล้ว สกอตแลนด์ก็ไม่ได้แย่เท่าไหร่… แต่ไม่รู้สิ"

# "My first guess of England was surprisingly close, at least geographically. That does leave another question though."
"ที่เดาไปทีแรกว่าอังกฤษนั้นนับว่าใกล้เกินคาดทีเดียว ถ้านับตามแผนที่น่ะนะ แต่ก็ยังมีอีกเรื่องที่คาใจอยู่"

# hi "But you have no accent…?"
hi "แต่ตอนเธอพูดก็ไม่ติดสำเนียงต่างชาติเลยนะ…?"

show lilly basic_weaksmile
with charachange

# li "That's where the details begin. I was born and raised in Japan, despite my mother being foreign."
li "นี่แหละรายละเอียดที่ว่า แม่ฉันเป็นชาวต่างชาติก็จริง แต่ฉันเกิดและโตที่ญี่ปุ่นนี่แหละจ้ะ"

# hi "Ah, I get it."
hi "อ้อ อย่างนี้นี่เอง"

# "Hold on, if she moved to the dorms simply due to Akira working longer hours…"
"เดี๋ยวนะ ถ้าสาเหตุที่ลิลลี่ย้ายมาอยู่หอมีแค่เรื่องที่อากิระทำงานเยอะขึ้น…"

# hi "So they don't live near the school?"
hi "แปลว่าพ่อแม่เธอไม่ได้อยู่แถวนี้เหรอ"

show lilly basic_reminisce
with charachange

# "She gives a small sigh, as if she didn't expect me to go any deeper. Was her previous frankness just a front?"
"เธอถอนหายใจเล็กน้อยคล้ายไม่คิดว่าฉันจะถามต่อ ที่บอกอะไรตรง ๆ เมื่อกี้คือบอกเฉย ๆ โดยที่ไม่ได้อยากบอกจริง ๆ\nเหรอ"

# li "Not… exactly. It's been a long time since we've actually met."
li "ไม่… เชิงจ้ะ ฉันเองก็ไม่ได้เจอพวกท่านนานแล้ว"

# "I feel like I'm not getting the whole story, but I don't really want to go unduly prying into her situation. Her about-face shows she feels kind of awkward about it."
"เหมือนลิลลี่ยังปิดบังอะไรไว้อยู่ แต่ฉันเองก็ไม่อยากซักไซ้เรื่องของเธออะไรให้มากเกินจำเป็นเหมือนกัน การที่ท่าที\nของเธอเปลี่ยนไปแบบกะทันหันนั้นก็แปลว่าเธอไม่ค่อยสบายใจจะเล่าเท่าไหร่"

# hi "So… do you speak much English? To be honest I don't know that much about Scotland, but at least I know that's the main language there."
hi "แล้ว… เธอได้พูดภาษาอังกฤษบ่อยมั้ย ว่าตามตรง ฉันก็ไม่รู้เรื่องประเทศสกอตแลนด์เท่าไหร่ แต่พอรู้อยู่ว่าที่นู่นเขาใช้\nภาษาอังกฤษเป็นภาษาราชการกัน"

# "It takes her a moment to collect herself, appreciating the change in topic."
"ลิลลี่รวมรวมความคิดอยู่สักพัก ดูเหมือนเธอจะยินดีที่ฉันเปลี่ยนเรื่อง"

show lilly basic_smileclosed
with charachange

# li "That's right. My family mostly used Japanese around the house when I was young, but they made sure Akira and I knew our Scottish side just as well."
li "ใช่จ้ะ ตอนฉันยังเด็ก ที่บ้านใช้ภาษาญี่ปุ่นก็เป็นส่วนใหญ่ก็จริง แต่พวกท่านก็คอยสอนฉันกับพี่ให้รู้จักวัฒนธรรม\nฝั่งสกอตแลนด์ด้วยเหมือนกัน"

show lilly basic_smile
with charachange

# li "I'm fluent in the language, but I'm also studying it in school. To keep my skills up and to have the qualifications on paper, mainly."
li "ฉันใช้ภาษาอังกฤษได้คล่องแล้ว แต่ก็มาเรียนที่โรงเรียนด้วย หลัก ๆ ที่เรียนก็เพราะจะได้เสริมทักษะแล้วก็จะได้ผ่าน\nการรับรองแบบเป็นรูปธรรมน่ะจ้ะ"

# hi "So you're bilingual? That's pretty impressive."
hi "แปลว่าเธอพูดได้สองภาษาเลยงั้นสิ น่าทึ่งจัง"

show lilly basic_weaksmile
with charachange

# li "I wouldn't go that far. Having parents who can speak the language is a large advantage, and English books in Braille aren't too hard to buy or import. With Yuuko's help, at least."
li "ไม่ขนาดนั้นหรอกจ้ะ ที่ฉันได้หลัก ๆ ก็เพราะมีพ่อแม่ที่พูดภาษาอังกฤษได้มากกว่า หนังสืออักษรเบรลล์ภาษาอังกฤษ\nก็หาซื้อหรือนำเข้าได้ไม่ยากเพราะมีคุณยูโกะช่วยจัดการให้ด้วยน่ะจ้ะ"

show lilly basic_smileclosed
with charachange

# li "There's a relatively high demand for local English teachers here anyway, which also helps give me some motivation to learn it well."
li "ยังไงถ้าเทียบ ๆ ดูแล้ว ครูภาษาอังกฤษดูจะเป็นที่ต้องการของที่นี่มากกว่าที่อื่นด้วย ซึ่งก็เป็นแรงใจให้ฉันตั้งใจเรียน\nได้ด้วยแหละจ้ะ"

# "Demand for English teachers? For a moment, I wonder why she brought this up."
"ครูภาษาอังกฤษเป็นที่ต้องการเหรอ ฉันนึกสงสัยอยู่แวบหนึ่งว่าทำไมถึงพูดเรื่องนี้"

# hi "You're planning to be an English teacher?"
hi "เธออยากเป็นครูภาษาอังกฤษเหรอ"

show lilly basic_cheerful
with charachange

# "She gives an enthusiastic nod."
"เธอพยักหน้าอย่างอารมณ์ดี"

# "It must be nice, having such a definite future in mind. I've never really given much thought to mine, so I'm kind of envious."
"มีเป้าหมายในอนาคตที่ชัดเจนแบบนี้นี่ดีจังเลยนะ ฉันไม่ค่อยได้คิดถึงอนาคตตัวเองเท่าไหร่เลยนึกอิจฉาอยู่หน่อย ๆ"

# hi "Hmm…"
hi "อืมม…"

show lilly basic_smile
with charachange

# li "What's wrong?"
li "มีอะไรเหรอจ๊ะ"

# hi "It's just… I could see you as a teacher pretty easily. It suits you."
hi "แบบว่า… ฉันนึกภาพเธอเป็นครูได้ชัดเลยนะ เหมาะดี"

show lilly basic_emb
with charachange

# "For a moment, she's speechless. She lowers her face a little and lets out a nervous giggle, something I've never seen her do before."
"เธออึ้งไปครู่หนึ่งก่อนจะก้มหน้าหัวเราะคิกคักอาย ๆ อย่างที่ฉันไม่เคยเห็นมาก่อน"

# "With Lilly's role as a class representative and her dependable nature, teaching does seem to be a line of work fitting her personality."
"เป็นทั้งหัวหน้าห้อง แถมยังเป็นคนพึ่งพาได้ การเป็นครูก็ดูจะเหมาะกับลักษณะนิสัยของลิลลี่ดี"

# hi "Sorry, that was probably a little much. It is true, though."
hi "ขอโทษทีนะ คงพูดเกินไปหน่อย แต่จริงนะ"

show lilly basic_weaksmile
with charachange

# "Waving her hand in front of her face dismissively, she quickly recovers."
"เธอโบกมือปัด ๆ กลับมาทำหน้าตามปกติได้อย่างรวดเร็ว"

# li "It's not that, it's just that… only one person's ever said that to me before."
li "ไม่ใช่อย่างนั้นหรอกจ้ะ แค่ว่า… เคยมีคนพูดอย่างนั้นกับฉันแค่คนเดียวเอง"

stop music fadeout 8.0

# "A short, somewhat awkward silence follows the discussion. Without knowing it, I ended up steering into a troublesome topic again."
"ความเงียบอันน่าอึดอัดชั่วครู่ผ่านเข้ามา เผลอลากไปเข้าเรื่องวุ่นวายโดยไม่รู้ตัวอีกแล้วสิ"

# "I should try to cheer her up a little. It was me who went and got her brooding, after all."
"ทำอะไรให้ลิลลี่สดใสขึ้นหน่อยดีกว่า ก็ฉันเป็นคนทำให้หมองเองนี่นะ"

# hi "Want to go grab lunch at the cafeteria after this?"
hi "เดี๋ยวไปกินข้าวเที่ยงที่โรงอาหารกันมั้ย"

# "It might perk her up a bit, or at least take her mind off her apparently complicated family situation."
"อาจจะพอช่วยให้อารมณ์ดีขึ้นหน่อย หรืออย่างน้อยความคิดก็จะได้ไม่ต้องจมอยู่กับเรื่องที่บ้านที่ดูจะซับซ้อนนั่น"

show lilly basic_planned
with charachange

# "Going by her smile, it seems to have the intended effect."
"ยิ้มอย่างนี้แล้วแปลว่าแผนของฉันได้ผล"

show lilly basic_ara
with charachange

# li "I appreciate the thought, but the food there…"
li "ขอบคุณที่ชวนจ้ะ แต่อาหารที่โรงอาหารมันออกจะ…"

# "Quite a quick redirection of the conversation. She does have a point though - the food there isn't the greatest."
"เปลี่ยนเรื่องเร็วเหมือนกัน แต่ก็ถูกของเธอ กับข้าวที่โรงอาหารก็ไม่ค่อยอร่อยเท่าไหร่"

# hi "Maybe the Shanghai? We could ask Hanako if she wants to come as well."
hi "งั้นไปร้านเซี่ยงไฮ้กันมั้ย เดี๋ยวไปชวนฮานาโกะด้วยก็ได้"

show lilly basic_surprised
with charachange

# li "Ah…"
li "อ๊ะ…"

# hi "What is it?"
hi "มีอะไรเหรอ"

show lilly basic_weaksmile
with charachange

# li "I almost forgot, until you reminded me. Hanako's birthday is coming up soon, and I was going to go shopping in the city for a present tomorrow."
li "เกือบลืมไปเลย เธอพูดเมื่อกี้ฉันถึงนึกได้พอดี เดี๋ยวจะถึงวันเกิดฮานาโกะแล้ว แล้วพรุ่งนี้ฉันกะว่าจะเข้าตัวเมืองไปซื้อ\nของขวัญด้วย"

# hi "If that's an invitation, I'd be happy to accompany you."
hi "จะชวนฉันไปด้วยเหรอ ถ้าชวนฉันก็ยินดีจะไปด้วยนะ"

# "The ability to get more used to the layout of the city would probably be a good thing. I have barely set foot in there, so I'd be hopelessly lost by myself."
"ทำความคุ้นเคยกับผังเมืองที่นี่ไว้ก็น่าจะดีเหมือนกัน ฉันเองก็เพิ่งมาได้ไม่นาน ถ้าไปตัวคนเดียวคงหลงแน่"

show lilly basic_smile
with charachange

# "She gives a nod, signaling that she happily approves of this plan for Sunday."
"เธอพยักหน้าเป็นสัญญาณว่าตกลงให้ฉันไปด้วยกับเธอในวันอาทิตย์นี้"

# "We eventually get back to our books, though before I begin reading again I steal one last glance at her."
"สุดท้ายเราก็อ่านหนังสือของตัวเองก่อนต่อ ฉันเหลือบมองลิลลี่อีกหนึ่งครั้งก่อนจะกลับมามองหนังสือตัวเอง"

# "Maybe I've been thinking on my situation too much. After all, everybody here would have their own unique circumstances."
"ฉันคงจะคิดมากไปกับสภาพตัวเองตอนนี้ ยังไงเสีย ทุกคนที่นี่ต่างก็มีเรื่องอะไรหลายอย่างแตกต่างกันไปของใครของมัน\nทั้งนั้น"

# "The chance to get outside and clear my head will probably do me good."
"ได้ออกไปสัมผัสอากาศข้างนอกให้หัวสมองโล่งก็คงดีเหมือนกัน"

scene black
with dissolve

#**************************************

label th_L3:

play ambient sfx_traffic fadein 10.0

scene black
with None

scene bg city_street1 at Fullpan(16.0, "left")
with locationchange

# "Bored of standing in place and watching the television in a shop window, I pull myself away from the tacky display with little effort."
"ฉันเบื่อกับการยืนอยู่เฉย ๆ ดูโทรทัศน์ที่ตั้งอยู่ในร้านผ่านกระจกจึงเดินเอื่อย ๆ ปลีกตัวออกมา"

# "After living at Yamaku, the city seems like an entirely different world."
"พอได้อยู่ที่โรงเรียนยามากุแล้ว เมืองใหญ่ก็ดูเป็นอะไรที่เป็นเหมือนโลกอีกใบหนึ่งไปเลย"

# "No running in the halls. Calm and orderly conduct is to be used at all times in the classrooms. Students are to exit rooms after checking both directions for oncomers. Elevators are reserved for movement-impaired students. Single file on stairs."
"ห้ามวิ่งตามโถงทางเดิน ต้องทำตัวสงบเสงี่ยมเรียบร้อยตลอดเวลาแม้กระทั่งตอนอยู่ในห้องเรียน เวลาจะออกจากห้อง\nต้องดูซ้ายขวาว่ามีคนมาหรือไม่ มีเพียงผู้พิการทางการเคลื่อนไหวเท่านั้นที่ใช้ลิฟต์ได้ เวลาขึ้นลงบันไดต้องเดินเป็นแถว\nเรียงเดี่ยว"

# "Compared to such strict, almost regimental, standards, the city's shopping arcade might as well be a strange country."
"ถ้าให้เทียบกับมาตรฐานที่เคร่งครัดจนดูละม้ายคล้ายพวกกองทัพเช่นนั้นแล้ว ย่านการค้าในเมืองใหญ่นี้ก็เรียกได้ว่าเป็น\nแดนสนธยาเลยทีเดียว"

# "While the school may have its fair share of hustle and bustle during the festival, the outside world is much different."
"แม้ช่วงเทศกาลโรงเรียนจะดูมีความวุ่นวายบ้างก็จริง แต่สภาพโลกภายนอกนั้นต่างจากที่โรงเรียนมาก"

# "It's strange. Having lived in a metropolitan city before my accident, this should feel more natural than Yamaku and the surrounding town ever could."
"แปลกดี ทั้งที่ก่อนเกิดเรื่องครั้งนั้นฉันก็ใช้ชีวิตอยู่ในเมืองใหญ่มาตลอด ฉันต้องคุ้นเคยกับบรรยากาศอย่างนี้มากกว่าที่\nโรงเรียนยามากุสิ"

# "Yet it feels foreign, somehow. The elevated walkways and tall buildings, each adorned with billboards taller than any three people, don't do anything to distract me from the passing crowd's reactions."
"แต่ไม่รู้ทำไมถึงรู้สึกไม่คุ้นชิน ทั้งทางเดินลอยฟ้า ตึกสูงแต่ละแห่งที่มีป้ายโฆษณาที่ติดอยู่สูงไปจากพื้นสักสามช่วงคน\nซึ่งไม่ได้ทำให้ฉันละความสนใจไปจากท่าทีของคนรอบ ๆ ตัวได้เลย"

$ renpy.music.set_volume(0.7, 0.5, channel="ambient")

show lilly cane_smileclosed_cas_close:
    center
    xpos 0.2
    easein 1.0 twoleft
show bg city_street1 at left
with Dissolve(1.0)

# "Lilly keeps one hand on my shoulder, the other holding her cane which taps the ground with a metronome-like steadiness. Looking over to her, that neutral smile of hers still holds."
"มือของลิลลี่ข้างหนึ่งจับไหล่ฉันไว้ ส่วนมืออีกข้างนั้นถือไม้เท้าที่แตะไปตามทางเดินเป็นจังหวะสม่ำเสมออย่างเมโทรโนม\nพอหันไปมองก็เห็นว่าเธอยังยิ้มเรียบ ๆ เช่นเคย"

# "Having only seen her in school uniform, I'd not have recognized her as she sat on a bench waiting for me to come, if not for her cane propped up against it and her distinctive hair."
"ด้วยความที่เคยเห็นเธอแค่ตอนใส่ชุดนักเรียน ถ้าไม่เห็นไม้เท้ากับผมอันเป็นเอกลักษณ์นั้นฉันคงจำเธอที่นั่งรอฉันอยู่\nตรงม้านั่งไม่ได้แน่"

# "I can't tell whether they're glancing at her due to her height, her foreign looks, her obvious blindness, or all three. Not that any of those would make the situation any less uncomfortable than it is."
"ฉันไม่รู้ว่าที่คนมองลิลลี่นั้นเป็นเพราะความสูง เพราะหน้าตาที่เป็นฝรั่ง เพราะเธอตาบอด หรือเพราะทั้งสามอย่างนั้นกันแน่\nแต่จะเพราะอะไรฉันก็อึดอัดที่คนมองอยู่ดีนั่นแหละ"

show lilly cane_smile_cas_close
with charachange

# li "Do you have any ideas of where to look first, Hisao?"
li "อยากไปดูที่ไหนก่อนมั้ยจ๊ะฮิซาโอะ"

# "Her soft voice breaks me out of my line of thought."
"เสียงอันนุ่มนวลของเธอดึงสติฉันออกมาจากความคิดเหล่านั้น"

# "I can't imagine that she's failing to notice the attention she garners, but she seems unfazed by it. I get the feeling she's the type to enjoy walking outside, so she might be used to it by now."
"ยังไงเธอก็คงรู้ตัวแหละว่าคนต่างมองเธอกันอยู่ แต่เธอก็ดูไม่ร้อนใจอะไร ลิลลี่คงจะชอบออกมาเดินเล่นข้างนอกอยู่แล้ว\nถึงได้ชิน"

# hi "Not really. This is my first time in this city, so I've got no idea of where to go."
hi "ก็ไม่หรอก ฉันเพิ่งเคยมาเมืองนี้เป็นครั้งแรกเลยไม่รู้ว่าจะไปที่ไหนดี"

show lilly cane_listen_cas_close
with charachange

# "She furrows her brow in thought, planning a route for us to take. And, come to think of it, a way to communicate it."
"เธอขมวดคิ้วครุ่นคิดวางแผนเส้นทางที่จะเดินไปด้วยกัน และ—จะว่าไปแล้ว—ก็น่าจะคิดอยู่ด้วยว่าจะบอกเส้นทางนั้น\nยังไง"

# "Something I'd noticed in the time I've been with her is how, when deep in thought, she lacks close to any form of body language to show it."
"เท่าที่อยู่กับลิลลี่มา อย่างหนึ่งที่ฉันสังเกตได้ก็คือเวลาที่เธอคิดจะไม่มีภาษากายอะไรแสดงออกมาเลย"

# "Her expression may change, but not a hint of movement shows. She seems to have little in the way of sweeping physical gestures in general though, so I've assumed it's part of her reserved nature."
"สีหน้าเปลี่ยนก็จริง แต่จะไม่มีการเคลื่อนไหวใด ๆ เลย แต่ก็ดูเหมือนว่าเธอจะไม่ขยับตัวแสดงท่าทางอะไรแบบมาก ๆ\nอยู่แล้ว ก็คงจะเป็นความเรียบร้อยด้วยนิสัยของเธอนั่นแหละ"

show lilly cane_weaksmile_cas_close
with charachange

# li "Is there a large electronics store near here?"
li "แถวนี้มีร้านเครื่องใช้ไฟฟ้าร้านใหญ่ ๆ มั้ยจ๊ะ"

# "I take a quick look around, mostly finding clothing stores. After a few seconds I notice a store with a bright blue sign some distance away that fits her description."
"พอกวาดตามองรอบ ๆ ก็เห็นแต่ร้านขายเสื้อผ้าเป็นส่วนใหญ่ แต่ไม่นานฉันก็เห็นร้านที่มีป้ายสีฟ้าสว่าง ๆ อยู่ไกล ๆ\nที่น่าจะเป็นร้านที่ลิลลี่พูดถึง"

# hi "Yep, it's just a bit ahead of us. Should we go in that direction?"
hi "อื้ม อยู่ใกล้ ๆ นี่เอง ไปทางนั้นกันมั้ย"

show lilly cane_smile_cas_close
with charachange

# "Thankfully, it's just the information she needed. With a nod we start off and head towards Lilly's unknown destination, landmarks being our guide."
"โชคดีที่ลิลลี่ถามเพียงเท่านั้น เธอพยักหน้าแล้วพวกเราก็เดินไปยังจุดหมายของเธอที่ฉันไม่อาจทราบโดยมีร้านนั้น\nเป็นหมุดนำทาง"

stop ambient fadeout 2.0

scene ev icecream
with shorttimeskip

play music music_happiness fadein 2.0

# "Storeowner" "Here you go. One vanilla, one chocolate."
thname("เจ้าของร้าน") "ได้แล้ว รสวานิลลาหนึ่ง รสช็อกโกแลตหนึ่ง"

scene bg city_street2 at center
with locationchange

# "I hand the money over the counter and take the cones to the railing that Lilly's sitting on."
"ฉันวางเงินไว้ที่เคาน์เตอร์หยิบไอศกรีมทั้งสองโคนนั้นแล้วเดินมายังราวเหล็กที่ลิลลี่นั่งอยู่"

# "I can't believe I let her trick me like this. She not only led me to an ice cream stall, but also got me to buy her some. At least she gave me the money for hers."
"ไม่อยากจะเชื่อเลยว่าจะหลงกลอะไรอย่างนี้ หลอกพามาร้านขายไอศกรีมไม่พอแล้วยังฝากซื้ออีก ยังดีที่ว่าเธอให้เงิน\nค่าไอศกรีมของตัวเองมาด้วย"

show lilly cane_smileclosed_cas at Transform(xanchor=0.5, xpos=0.2, ypos=0.2, yanchor=0.0)
with charaenter

# "Sure enough, she's patiently waiting where I'd left her. I guess she was planning on making the day an event, rather than a simple shopping trip."
"และแน่นอนว่าเธอก็รอฉันอย่างใจเย็นอยู่ตรงที่ฉันปลีกตัวออกมา คงวางแผนจะมาเที่ยวมากกว่า ไม่ได้กะจะมาซื้อของ\nเฉย ๆ หรอก"

show lilly cane_smileclosed_cas:
    ease 1.0 xpos 0.5 xanchor 0.5 ypos 0.15
show bg city_street2:
   ease 1.0 left
with None

show lilly basic_satisfied_cas_close:
    xanchor 0.5 xpos 0.2 ypos 0.2 yanchor 0.0
    ease 1.0 xpos 0.5 xanchor 0.5 ypos 0.15
show bg city_street2:
   ease 1.0 left
with Dissolve(1.0)

# "I call out to her and slowly place the vanilla cone in her outstretched hands, being careful to make sure she has a good hold of it before letting go."
"ฉันเรียกลิลลี่แล้วค่อย ๆ ส่งไอศกรีมรสวานิลลาให้เธอที่ยื่นมือออกมา พอแน่ใจแล้วว่าเธอถือเต็มไม้เต็มมือฉันจึงผละมือ"

# "At least her tastes are fairly normal. I was worried she'd ask for some weird flavor when she first asked."
"อย่างน้อยก็กินรสอะไรปกติละนะ ทีแรกก็คิดมากว่าจะสั่งให้ซื้อรสอะไรแปลก ๆ หรือเปล่า"

# hi "Here's the change."
hi "นี่เงินทอน"

show lilly basic_smileclosed_cas_close at Transform(xalign=0.5, ypos=0.15)
with charachange

# li "It's okay, keep it."
li "ไม่เป็นไรจ้ะ เธอเอาไปเถอะ"

# "I move to protest, but realize the futility of doing so over such a small amount. I slip the coin into my pocket, supplementing my meager allowance ever so slightly."
"ฉันเตรียมจะยัดเยียดเงินนั้นกลับไป แต่ด้วยเศษเงินแค่นี้จะฝืนคืนไปก็คงเหนื่อยเปล่า ฉันเก็บเหรียญใส่กระเป๋ากางเกง\nซึ่งมีส่วนช่วยให้ค่าขนมอันนิดน้อยของฉันเพิ่มขึ้นมากระผีกหนึ่ง"

show lilly basic_smileclosed_cas_close
with charachange

# "Lilly shows no signs of wanting to get up, so I take a seat beside her and start eating my own ice cream."
"เมื่อลิลลี่ไม่มีท่าทีว่าจะลุกขึ้นฉันจึงนั่งลงข้างเธอแล้วกินไอศกรีมของตัวเองบ้าง"

# hi "The summer weather's nice. Hopefully it will hold out for a while."
hi "อากาศหน้าร้อนนี่ดีเนอะ อยากให้เป็นอย่างนี้ไปอีกสักพักเลย"

show lilly basic_weaksmile_cas_close
with charachange

# li "You too? I'm beginning to think I'm the only person who prefers winter."
li "เธอก็อีกคนเหรอเนี่ย หรือจะมีแค่ฉันคนเดียวจริง ๆ ที่ชอบหน้าหนาว"

# "I contemplate her statement for a long moment."
"ฉันครุ่นคิดกับคำพูดของเธออยู่ครู่ใหญ่ ๆ"

# hi "Yeah, I think you might be."
hi "อื้ม คงงั้นแหละ"

show lilly basic_pout_cas_close
with charachange

# "It draws the intended reaction. She's cute when she's pouting."
"และได้ผลดังคาด พอลิลลี่ทำแก้มป่องแล้วน่ารักดี"

# hi "Still, I can't really imagine what's so good about winter. You can't go out without bundling up, and you still freeze anyway."
hi "แต่เอาจริง ๆ ฉันก็นึกไม่ออกเหมือนกันว่าหน้าหนาวมันดีตรงไหน ไปไหนทีก็ต้องใส่ชุดเป็นร้อย ๆ ชั้น แถมใส่แล้วใช่ว่า\nจะอุ่นขึ้นนะ"

show lilly basic_reminisce_cas_close
with charachange

# li "I used to live further north, where there'd be plenty of snow to play in, so it's a little nostalgic. I don't like the heat very much, either."
li "ฉันเคยอยู่ทางเหนือที่มีหิมะตกเยอะ ๆ น่ะจ้ะ หน้าหนาวก็เลยเป็นอะไรที่ชวนให้คิดถึงขึ้นมา แถมฉันเองก็ไม่ค่อยชอบ\nอากาศร้อนเท่าไหร่ด้วย"

# hi "At least you can wear a skirt, so don't complain about that."
hi "อย่างน้อยพอเป็นหน้าร้อนก็ใส่กระโปรงได้นะ จะบ่นก็คงไม่ได้หรอก"

show lilly basic_giggle_cas_close
with charachange

# "She gives an amused giggle as we both get back to finishing off our already melting cones."
"เธอยิ้มหัวเราะคิกคัก พวกเราต่างกินไอศกรีมที่เริ่มละลายแล้วของตัวเองกัน"

play ambient sfx_crowd_outdoors fadein 2.0

hide lilly
show crowd at left
with shorttimeskip

# "I idly sit and watch the crowds going by as we eat, catching bits and pieces of conversation."
"ฉันนั่งมองผู้คนที่เดินผ่านไปมาพลางกินไอศกรีมโดยมีบทสนทนากระท่อนกระแท่นลอยผ่านหู"

show lilly basic_satisfied_cas_close at Transform(xalign=0.5, ypos=0.15)
with charaenter

# "Looking to Lilly, I see her dutifully licking her ice cream from the top downwards, blissfully unaware of the fact that it's beginning to melt."
"พอหันไปมองก็เห็นลิลลี่ที่ยังคงเลียไอศกรีมกินจากบนลงล่างอย่างตั้งอกตั้งใจโดยไม่รู้เลยว่าตัวไอศกรีมนั้นเริ่มละลายแล้ว"

# hi "It's melting."
hi "ละลายแล้วแน่ะ"

show lilly basic_surprised_cas_close
with charachange

# li "Where?"
li "ตรงไหนเหรอ"

# hi "Um… down a bit?"
hi "เอ่อ… ล่าง ๆ หน่อย?"

show lilly basic_listen_cas_close
with charachange

# "She lowers her mouth from the top of the cone, but has no idea of exactly where the ice cream's dripping. What follows is a game of guiding her left and right until she finally finds it."
"เธอขยับปากลงมาด้านล่างโคนแต่ยังไม่รู้ว่าส่วนที่ละลายจนหยดนั้นอยู่ตรงไหน หลังจากนั้นก็ต้องคอยบอกซ้ายขวา\nนำทางลิลลี่ไปจนถึงจุดนั้น"

# "To any onlooker, it must seem absolutely bizarre - a girl with her eyes closed turning her cone over and over as the guy next to her gives instructions. A strange variant of childhood blindfold games, maybe."
"ใครมองก็คงเห็นว่าประหลาดที่มีผู้หญิงหลับตาหมุนโคนไอศกรีมไปเรื่อย ๆ โดยที่มีผู้ชายที่นั่งอยู่ข้าง ๆ คอยบอกทาง\nคงจะเหมือนเกมปิดตาที่เล่นกันสมัยเด็กแต่เป็นในรูปแบบที่แปลก ๆ ละมั้ง"

show lilly basic_smileclosed_cas_close
with shorttimeskip

# "In good time we finally finish our treats, and while away the time conversing casually."
"ไม่เร็วไม่ช้าเราก็กินไอศกรีมกันจนหมดพลางคุยอะไรฆ่าเวลาไปเรื่อยเปื่อย"

stop music fadeout 3.0

show lilly back_listen_cas_close
with charachange

# "Caught mid-sentence, Lilly perks her head in her trademark manner. It's an unmistakable sign that something's caught her attention."
"ระหว่างที่คุยลิลลี่ก็เงยหน้าขึ้น เป็นท่าที่คล้ายท่าประจำตัวของเธอเวลามีอะไรสักอย่างที่ดึงความสนใจเธอไป"

show lilly back_smileclosed_cas_close
with charachange

# li "Ah…"
li "อ๊ะ…"

# hi "What is it?"
hi "มีอะไรเหรอ"

show lilly back_smile_cas_close
with charachange

# li "Is Akira somewhere over there? I think I heard her."
li "พี่ฉันอยู่แถวนั้นหรือเปล่า เหมือนได้ยินเสียงอยู่นะ"

show lilly back_smile_cas_close at Transform(xpos=0.25)
show crowd:
    bgright
    xpos 0.55
show bg city_street2:
    bgright
    xpos 0.55
with dissolvecharamove

#bgright: xpos 0.6 xanchor 0.5 ypos 1.0 yanchor 1.0


# "I raise an eyebrow as I look in the direction she's facing, somewhat doubtful of her ability to pick out Akira's lone voice in the din."
"ฉันเลิกคิ้วขึ้นพลางหันไปมองทางที่ลิลลี่หันหน้าไป ในใจยังนึกสงสัยว่าเธอจะหูดีถึงขั้นได้ยินเสียงอากิระที่ปะปนอยู่กับ\nเสียงอื้ออึงเหล่านี้ได้จริงหรือไม่"

show akira basic_boo behind crowd:
    tworight
    xpos 0.78 ypos 1.13
with charaenter

# "Sure enough though, a blonde girl in a suit can be seen through the tiny gaps between people walking every which way."
"แต่ที่เห็นนั่นไม่ผิดแน่ มีผู้หญิงผมบลอนด์ใส่ชุดสูทที่อยู่ท่ามกลางฝูงชนที่คลาคล่ำอยู่"

# "I raise a hand and wave, trying to catch her attention."
"ฉันยกมือโบกให้อากิระหันมา"

# hi "Satou! Hey, Satou!"
hi "ซาโต้! นี่ ซาโต้!"

show akira basic_smile
with charachange

# "She stops in her tracks and looks towards me, evidently noticing my calls. As she does, I notice someone walking beside her."
"อากิระชะงักแล้วหันมามองเพราะได้ยินฉันเรียก เธอเดินมาพร้อมอีกคนที่ประกบมาด้วย"

# "I can't get a good look at whoever it is though, before the two begin walking towards where we are."
"แต่ตอนที่มองไกล ๆ แล้วยังมองไม่ค่อยออกว่าคนนั้นเป็นใครกันแน่"

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")
play music music_ease fadein 4.0

show akira basic_smile:
    ease 1.0 ypos 1.0 alpha 0.0
with None

show akira basic_smile as akira2 behind lilly:
    tworight
    xpos 0.78 ypos 1.13 alpha 0.0
    ease 1.0 ypos 1.0 alpha 1.0
with Pause(1.0)

hide akira
with None

show lilly back_smile_cas_close at Transform(yalign=1.0)
with charamove

# "As they reach us, Lilly and I stand and dust ourselves off."
"พอสองคนนั้นเดินมาถึง ลิลลี่กับฉันก็ลุกขึ้นแล้วปัด ๆ ฝุ่นตามตัว"

show lilly back_giggle_cas_close
with charachange

# li "Akira?"
li "พี่?"

hide akira2
show akira basic_laugh behind lilly:
    tworight
    xpos 0.78 ypos 1.0
with charachange

# aki "Hey, you two."
aki "ไงพวกเธอ"

show lilly back_giggle_cas_close at Transform(xpos=0.1)
show akira basic_smile at Transform(xanchor=0.5, xpos=0.6)
show crowd at center
show bg city_street2 at center
with dissolvecharamove

show hideaki bored at right behind akira
with charaenter

# "She nods towards me, a gesture which I quickly return. My gaze shifts towards the young girl next to her, and our eyes meet. As they do, Akira plops a hand onto her head, a move which doesn't seem to faze her."
"อากิระพยักหน้าให้ฉัน ซึ่งฉันก็พยักหน้าตอบ สายตาฉันเลื่อนไปทางเด็กผู้หญิงที่อยู่ข้าง ๆ จนเราสองคนสบตากัน\nจังหวะนั้นอากิระก็เอามือวางไว้บนหัวเธอ แต่เธอดูจะไม่ยี่หระอะไร"

show hideaki normal
with charachange

# hh "I don't believe we've met. I'm Hideaki. Pleased to meet you, Hisao."
hh "คงจะเพิ่งได้เจอกันเป็นครั้งแรกเลยสินะครับ ผมฮิเดอากิครับ ยินดีที่ได้พบนะครับพี่ฮิซาโอะ"

# "A guy's name, huh? Guess I just dodged a bullet there. He bows, somewhat restrained by Akira's hand being on his head."
"ชื่อผู้ชายเหรอ เกือบไปแล้วมั้ยล่ะ เขาโค้งตัวด้วยความเก้ ๆ กัง ๆ เล็กน้อยเพราะอากิระจับหัวไว้อยู่"

show lilly basic_smileclosed_cas_close at Transform(xpos=0.18)
with charachange

# li "Oh, Hideaki's here too? Are you well?"
li "อ้าว ฮิเดอากิก็มาด้วยเหรอ สบายดีหรือเปล่า"

show hideaki thinking
with charachange

# hh "Akira's been taking very good care of me, thank you."
hh "พี่อากิระดูแลผมดีมากเลยครับ ขอบคุณครับ"

show akira basic_laugh
show hideaki sad
with charachange

# "Akira grins as if to affirm the point and rubs his head hard, dragging it around in a circular motion. His dreary face during this is somewhat amusing."
"อากิระยิ้มราวกับยืนยันคำพูดนั้นพลางยีหัวฮิเดอากิแรง ๆ แบบวนเป็นวงกลม เห็นหน้าแหย ๆ ของฮิเดอากิตอนนี้แล้วก็\nตลกดีเหมือนกัน"

show akira basic_smile
with charachange

# aki "Uncle's out on business again, so I'm just taking him around town for today."
aki "คุณลุงเขาออกไปทำธุระอีกแล้วน่ะ วันนี้เลยพาน้องมันมาเที่ยว"

show akira basic_boo
with charachange

# aki "I'd have preferred to be spending the day on a date with my boyfriend, but…"
aki "ใจจริงก็อยากไปเดตกับแฟนมากกว่านะ แต่ว่า…"

show hideaki closed_up
with charachange

# "Hideaki gives a cough to try and redirect Akira's thoughts."
"ฮิเดอากิกระแอมคล้ายจะเบี่ยงประเด็นอากิระ"

# "As he does so, though, I find mine wandering. They're related? And further, as first cousins? I suppose that explains why she's taking care of him in any case."
"แต่ประเด็นในหัวฉันก็เบี่ยงไปแล้วเหมือนกัน สองคนนี้เป็นพี่น้องกันเหรอ หรือเป็นลูกพี่ลูกน้อง แต่ต้องเป็นอะไรกัน\nนั่นแหละอากิระถึงได้มาดูแลอย่างนี้"

# hi "Come to think of it, Hideaki, how did you know my name?"
hi "จะว่าไป ฮิเดอากิ นี่นายรู้ชื่อฉันได้ยังไง"

show hideaki serious
with charachange

# hh "Akira told me. Being a Yamaku student, I suppose you're disabled in some way?"
hh "พี่อากิระบอกผม และการที่พี่ฮิซาโอะเรียนที่ยามากุ แปลว่าต้องพิการอะไรสักอย่างสินะครับ"

# hi "Not everyone in Yamaku's disabled…"
hi "ใช่ว่าทุกคนในยามากุจะพิการสักหน่อย…"

# "Which I only learned a handful of days ago. I give silent thanks to Shizune and Misha for their stream of information about how the school works."
"ซึ่งฉันก็เพิ่งรู้มาเมื่อไม่กี่วันมานี้เอง ในใจฉันนึกขอบคุณชิซูเนะและมิช่าที่แบ่งปันข้อมูลเรื่องนอกในของโรงเรียน"

# "Because of them, I found out that since the school will accept practically anybody suffering from non-mental disabilities, it doesn't discriminate against healthy people either."
"เพราะสองคนนั้นฉันถึงได้รู้ว่าโรงเรียนนี้ไม่ได้กีดกันคนที่แข็งแรงดีออกไปด้วย เพราะยังไงโรงเรียนนี้ก็เปิดกว้างรับทุกคน\nที่พิการทางร่างกายอยู่แล้ว"

# "It seems unlikely that many in good health would enroll there though. While the standard of education is pretty high, it's extremely isolated and very much focused on helping disabled students."
"แต่คนที่ร่างกายสมบูรณ์ดีก็คงไม่ค่อยไปเรียนที่ยามากุกันหรอก มาตรฐานการศึกษาในโรงเรียนสูงก็จริง แต่ตัวโรงเรียน\nค่อนข้างอยู่ไกลคน แถมโรงเรียนเองก็เน้นการให้ความช่วยเหลือกับนักเรียนที่พิการมากกว่า"

show hideaki angry_up
with charachange

# hh "You're dodging the question."
hh "เลี่ยงคำถามเหรอครับ"

# "Damn, he's sharp."
"หัวไวเกินไปละ"

# "Before I can say another word though, he decides to take a stab at it himself."
"แต่ก่อนที่ฉันจะทันได้พูดอะไรเขาก็เปิดมาก่อน"

show hideaki evil
with charachange

# hh "If I were to call it myself… your heart?"
hh "ถ้าให้ผมเดา… หัวใจใช่มั้ยครับ"

$ renpy.music.set_volume(0.5, 0.5, channel="music")
$ renpy.music.set_volume(0.0, 0.5, channel="ambient")

show akira basic_lost
show lilly basic_listen_cas_close
with charachange

# "Akira looks mildly curiously at me, her interest piqued as well. That sure was a lucky guess."
"อากิระมองฉันด้วยความสนใจเพราะเธอเองก็อยากรู้เหมือนกัน เดาแม่นจริง"

# hi "How did you…?"
hi "นี่นาย…"

$ renpy.music.set_volume(1.0, 10.0, channel="music")
$ renpy.music.set_volume(0.5, 10.0, channel="ambient")

show hideaki thinking
with charachange

# hh "You show no missing limbs or deformities, so external disabilities are out."
hh "แขนขาพี่ยังอยู่ครบ ร่างกายไม่มีบิดเบี้ยว เพราะงั้นตัดความพิการพวกนั้นออกไปได้"

show hideaki serious
with charachange

# hh "Considering the lack of any strange mannerisms, it's also unlikely that you'd have any mental disability."
hh "แล้วพี่ก็ทำตัวปกติดี เพราะงั้นคงไม่ใช่ความพิการทางจิตด้วย"

show lilly basic_planned_cas_close
with charachange

# li "But Yamaku doesn't take mentally disabled students."
li "แต่ยามากุไม่รับนักเรียนพิการทางจิตนะจ๊ะ"

show hideaki bored
with charachange

# hh "I know."
hh "ผมรู้ครับ"

show hideaki serious_up
with charachange

# hh "Leaving that aside, the only possibility left is that of internal disabilities."
hh "พอตัดเรื่องนั้นออกไปด้วยแล้ว ความเป็นไปได้เดียวคือความพิการกับอวัยวะภายใน"

show hideaki happy
with charachange

# hh "I didn't know which one you might bear, so I guessed. Correctly, as it turns out. And your reaction confirmed my guess."
hh "ผมไม่รู้ว่าพี่เป็นอะไรก็เลยเดา แล้วก็เดาถูก ปฏิกิริยาของพี่ก็ยืนยันด้วยว่าใช่"

show akira basic_smile
with charachange

# "More than a little bemused, I look to Akira. She grins and shrugs, obviously taking some enjoyment out of her partner's deductions."
"ฉันหันไปมองอากิระด้วยสีหน้าที่ไม่สบอารมณ์มากนัก เธอยิ้มแล้วยักไหล่ดูสนุกกับการอนุมานของอีกฝ่าย"

# "He's sharp, yes, but more than a little unsympathetic. Logical, but lacking in tact. His attitude reminds me of Shizune, in a way, as do his looks."
"ก็ฉลาดจริงแหละ แต่ออกจะขวานผ่าซากไปหน่อย มีเหตุผลดี แต่ยังขาดไหวพริบ เห็นการทำตัวอย่างนี้แล้วก็นึกถึง\nชิซูเนะเหมือนกัน หน้าตาก็คล้ายด้วย"

show hideaki disapproves
with charachange

# hh "May I ask why you're staring at me? Surely I'm not that unusual a specimen."
hh "แล้วนี่จ้องผมทำไมเหรอครับ ผมไม่ใช่ตัวอย่างพิเศษนะครับ"

# "Does he not know how unusual he looks? I could overlook the spats and clothing as just being coincidental, but the ribbon in his hair really is too much."
"นี่ไม่รู้ตัวเลยเหรอว่าตัวเองทำตัวเด่นแค่ไหนน่ะ ไอ้เสื้อผ้ากับถุงน่องน่ะพอเข้าใจได้ว่าอาจจะบังเอิญ แต่โบว์บนหัวนี่\nไม่ไหวเลยจริง ๆ"

# "This is entirely beside the point, though."
"ซึ่งการแต่งตัวก็ไม่ได้เกี่ยวอะไรกับประเด็นจริง ๆ อะนะ"

# hi "Sorry. You just remind me of someone."
hi "โทษที พอดีเห็นนายแล้วนึกถึงใครบางคน"

play sound sfx_impact

show akira basic_boo
show hideaki surprise_up
with vpunch

# "Akira gives him a sharp jab with her elbow."
"อากิระถองศอกใส่ฮิเดอากิ"

show akira basic_laugh
with charachange

# aki "Told ya you're not that much different from her."
aki "บอกแล้วไงว่านายก็เหมือน ๆ กับพี่นายน่ะแหละ"

show hideaki closed_up
with charachange

# "He coughs into his hand to try and maintain an upright and serious demeanor."
"เขากระแอมใส่กำปั้นแล้วทำท่าให้ดูจริงจังขึงขังไว้"

# hh "I see you've met my sister, then. Perhaps my full name might help you."
hh "แสดงว่าเจอพี่ผมแล้วด้วยสินะครับ งั้นถ้ารู้นามสกุลผมแล้วคงนึกออก"

show hideaki serious
with charachange

# hh "I am Hideaki Hakamichi. You are probably thinking of my sister, Shizune Hakamichi."
hh "ผมฮิเดอากิ ฮากามิจิครับ คงจะนึกถึงพี่สาวของผมที่ชื่อชิซูเนะ ฮากามิจิอยู่สินะครับ"

# "Oh, so he's Shizune's brother."
"อ้อ น้องชิซูเนะนี่เอง"

# "Wait a minute, if Hideaki is the son of Akira's uncle, and Shizune is his sister, then that means Lilly and Shizune's fathers are brothers-in-law. Therefore…"
"เดี๋ยวนะ ถ้าฮิเดอากิเป็นลูกชายของลุงอากิระ แล้วชิซูเนะเป็นพี่ฮิเดอากิ แปลว่าพ่อของลิลลี่กับชิซูเนะเป็น\nพี่เขยน้องเขยกัน ดังนั้น…"

# hi "Lilly and Shizune are first cousins?"
hi "ลิลลี่กับชิซูเนะเป็นลูกพี่ลูกน้องกัน?"

show lilly basic_concerned_cas_close
show akira basic_smile
with charachange

# "Lilly groans in an uncharacteristically unrestrained manner. The reaction earns an amused smirk from her sister."
"ลิลลี่ทำเสียงโอดครวญแบบเต็มที่ผิดวิสัย พออากิระเห็นปฏิกิริยาของลิลลี่แล้วก็ยิ้ม ๆ"

# "The enmity between the two just took on another meaning. I had thought it simply a matter of difficulty of communication between the two, but a family feud makes things much more complicated."
"ก็แปลว่าเรื่องที่สองคนนั้นไม่ถูกกันยังมีอีกด้านที่ไม่เคยเห็นอยู่ ทีแรกก็นึกว่าแค่มีปัญหาเรื่องการสื่อสารกัน แต่พอมี\nเรื่องครอบครัวมาเกี่ยวแล้วยิ่งทำให้อะไร ๆ ซับซ้อนขึ้นกว่าเดิม"


show akira basic_laugh
with charachange

# aki "You can choose your friends, but you can't choose your family."
aki "คนเราน่ะเลือกเพื่อนได้ แต่เลือกครอบครัวไม่ได้นะ"

show akira basic_boo
with charachange

# "She gives a halfhearted shrug. She mustn't give as much weight to the two's conflict as I do."
"อากิระยักไหล่เนือย ๆ คงไม่ได้คิดมากเรื่องสองคนนั้นเท่าฉันละมั้ง"

show akira basic_smile
with charachange

# aki "Well, that's how it is. What're you two up to anyway on this fine day?"
aki "เอาเหอะ ก็ตามนั้นแหละ ว่าแต่เธอสองคนออกมาทำอะไรกันในวันฟ้าใสอย่างนี้"

show lilly basic_smileclosed_cas_close
with charachange

# li "We're shopping for Hanako's birthday present. The day will be coming up soon, so this is the last chance we'll have before school starts again for the week."
li "พอดีหนูออกมาหาซื้อของขวัญให้ฮานาโกะ ใกล้ถึงวันแล้วด้วย ถ้าพ้นวันนี้ไปก็จะไม่มีโอกาสได้ออกมาซื้อของแล้ว\nเพราะต้องกลับไปเรียน"

stop music fadeout 7.0

show akira basic_lost
with charachange

# "Akira makes a strange face, as if Lilly had just said that the sky wasn't blue and the clouds not white."
"อากิระทำหน้าเหวอราวกับลิลลี่เพิ่งบอกว่าท้องฟ้าไม่ได้เป็นสีฟ้า ก้อนเมฆไม่ได้เป็นสีขาว"

# aki "Isn't her birthday on the tenth next month?"
aki "วันเกิดฮานาโกะมันวันที่สิบเดือนหน้านู่นเลยไม่ใช่เหรอ"

show lilly basic_surprised_cas_close
with charachange

# li "Yes… Why? Is something wrong?"
li "อื้ม… ทำไมเหรอ มีอะไรหรือเปล่า"

show akira basic_resigned
with charachange

# "Akira's face seems to collapse. It's an utterly unbefitting expression for someone so rowdy and headstrong."
"อากิระทำสีหน้าเครียดหนัก เป็นสีหน้าที่ไม่เหมาะกับเธอซึ่งเป็นคนเฮฮาและหัวแข็งเอามาก ๆ"

# aki "The folks didn't call you yet?"
aki "ที่บ้านยังไม่ได้ติดต่อมาเหรอ"

show lilly basic_oops_cas_close
show hideaki confused
with charachange

# "As Lilly shakes her head cluelessly, I look at Hideaki to see if he knows anything about this. A simple shrug is his only answer."
"ลิลลี่สั่นหัวเป็นเชิงว่าไม่รู้เรื่อง ฉันเหลือบมองไปทางฮิเดอากิเผื่อจะรู้ว่ามีเรื่องอะไรกัน แต่เขาก็ยักไหล่ตอบ"

show akira basic_boo
with charachange

# "For a moment, Akira ponders what to do before smiling once again. The fact that she can hide her emotions so quickly and effectively is unsettling."
"อากิระคิดอยู่ครู่หนึ่งว่าจะเอายังไงต่อก่อนจะยิ้มอีกครั้ง ซ่อนอารมณ์ได้เก่งและแนบเนียนจนฉันใจคอไม่ดีขึ้นมาเลย"

show akira basic_smile
with charachange

# aki "Hey Shortie, sorry, but could you hang with Hisao for a while?"
aki "เฮ้ย โทษทีนะเจ้าเตี้ย อยู่กับฮิซาโอะไปก่อนนะ"

$ renpy.music.set_volume(0.7, 2.0, channel="ambient")

show hideaki normal
with charachange

show lilly basic_oops_cas_close:
    parallel:
        easeout 1.0 xpos -0.5
    parallel:
        linear 0.7 alpha 0.0
show akira basic_smile:
    parallel:
        easeout 1.0 xanchor 1.0 xpos 0.0
    parallel:
        linear 0.7 alpha 0.0
show hideaki normal:
    ease 1.0 center
show bg city_street2:
    ease 1.0 right
show crowd:
    ease 1.0 right
with Pause(1.0)

hide lilly
hide akira
with None

# "He nods and waves her off, Akira placing an arm on Lilly's shoulder as she guides her away and out of earshot."
"ฮิเดอากิพยักหน้าแล้วโบกมือลา อากิระโอบไหล่ลิลลี่นำทางไปให้พ้นระยะที่พวกเราจะได้ยิน"

# "And so, I'm alone with “Shortie.”"
"และฉันก็ถูกทิ้งให้อยู่กับ “เจ้าเตี้ย”"

# hi "So… nice weather, isn't it?"
hi "อากาศ… ดีเนอะ ว่ามั้ย"

show hideaki thinking at center
with charachange

# hh "It seems so."
hh "ก็ดีนะครับ"

"…"

# hi "I guess they dumped us."
hi "โดนทิ้งแล้วสิ"

show hideaki serious
with charachange

# hh "Indeed."
hh "ครับ"

# "What a farcical attempt at smalltalk. I've got no idea of how to talk to this guy, and his robotic responses aren't helping. Blood and a stone come to mind."
"เหมือนมาเล่นตลกกันสองคนเลย จะคุยกับเขายังไงดีเนี่ย ถามคำตอบคำเป็นหุ่นยนต์ไปได้ ไม่รู้จะเอายังไงต่อดี"

show hideaki triangle
with charachange

# "Without another word, he begins to rock on his feet in an obvious gesture of boredom with this discussion. He really is like a little kid, despite his serious demeanor."
"แล้วเขาก็แกว่งขาเล่น เห็นได้ชัดว่าเบื่อที่ต้องคุย ทำตัวเป็นเด็กจริง ๆ ถึงท่าทางจะดูจริงจังก็เถอะ"

# "Suspecting the conversation over, I decide to accomplish what I came here to do in the first place."
"พอเห็นว่าหมดเรื่องจะคุยแล้วฉันก็นึกจะไปทำสิ่งที่ได้ตั้งเป้าไว้แต่แรก"

# hi "I'm going to go search for a present. Coming?"
hi "เดี๋ยวจะไปซื้อของขวัญ ไปด้วยมั้ย"

show hideaki normal
with charachange

# hh "Not much else to do."
hh "ไม่มีอะไรทำอยู่แล้วครับ"

stop ambient fadeout 0.5

scene bg city_street3
with shorttimeskip

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_traffic fadein 2.0

# "In a little while, we come to a small shop beside a convenience store."
"ไม่นานเราก็มาถึงร้านเล็ก ๆ ที่ตั้งอยู่ข้างร้านสะดวกซื้อ"

# "For once the store windows aren't filled with electronics and computer games, but dolls, stuffed bears and all manners of wood-crafted oddities."
"เป็นร้านที่ตามหน้าต่างไม่ได้มีเครื่องใช้ไฟฟ้าหรือเกมคอมพิวเตอร์ แต่เป็นหุ่น ตุ๊กตาหมี และของเบ็ดเตล็ดทำมือ\nที่ทำด้วยไม้ทั้งหลาย"

# hi "Othello's… Antiques?"
hi "ร้านขายของเก่า… โอเทลโล่?"

# "An antique store? Well, if there's anything in this town that'd suit Hanako, I guess it'd be here."
"ร้านขายของเก่าเหรอ อืม ถ้าให้เทียบกับร้านอื่น ร้านนี้น่าจะเหมาะกับฮานาโกะที่สุดแล้วละมั้ง"

# "I reach for the old-looking door handle, but pull back at the last minute as I realize my companion's gone adrift."
"ฉันยื่นมือเตรียมจับมือจับประตูที่ดูเก่า แต่ก็ไม่ได้จับเมื่อเห็นว่าคนที่มาด้วยไม่ได้ตามมา"

# hi "Not coming in?"
hi "ไม่เข้ามาด้วยเหรอ"

show hideaki triangle at center
with charaenter

# hh "I'll just be in the newsstand for a while. Don't mind me."
hh "ผมจะไปดูแผงหนังสือพิมพ์สักหน่อย พี่ไปเถอะ"

# "His voice makes it painfully clear he has zero interest in what's in the store, and that he doesn't feel obligated to follow me."
"น้ำเสียงฮิเดอากิบอกชัดจนฉันซึมว่าเขาไม่ได้สนใจของในร้านเลย แถมไม่ได้มีใจจะตามมาด้วย"

hide hideaki
with charaexit

# "As he wanders off without another word, I push the thick wooden door and enter the store, a bell above me ringing out."
"พอเขาเดินออกไปแบบเงียบ ๆ แล้วฉันก็ผลักประตูไม้บานหนาเข้าร้านมา เสียงกระดิ่งที่อยู่บนหัวดังกริ๊ง"

stop ambient fadeout 0.5
play sound sfx_storebell

scene bg city_othello at Fullpan(10.0, dir="left")
with locationskip

play music music_soothing fadein 0.5

# "The musty smell of old books and wooden shelves is distinctly anachronistic."
"กลิ่นอับของหนังสือกับชั้นไม้ให้ความรู้สึกเหมือนร้านนี้อยู่คนละยุค"

# "I look to the counter beside the door. The graying man behind it sits there silently, reading a tattered book. He certainly fits the look of the place."
"ฉันมองไปทางเคาน์เตอร์ที่อยู่ข้างประตูซึ่งมีชายผมสีดอกเลาที่นั่งอ่านหนังสือเก่า ๆ อยู่เงียบ ๆ ท่าทางเขาดูเข้ากับ\nร้านนี้เป็นอย่างดี"

# "Slowly wandering through the aisles, the person I'm reminded of as I inspect each handcrafted or imported oddity in turn isn't Hanako."
"ฉันเดินดูตามชั้นวางของไปเอื่อย ๆ คนที่ฉันนึกถึงเมื่อได้พินิจดูของทำมือหรือของเบ็ดเตล็ดนำเข้าแต่ละชิ้นกลับไม่ใช่\nฮานาโกะ"

# "Crouching down, I examine the ancient oak desk inside the shop window."
"ฉันย่อตัวลงมองที่โต๊ะไม้โอ๊กโบราณที่อยู่ตรงหน้าต่างร้าน"

# "At least thirty dolls, all varying wildly in size and make. The only similarity between them is the long Victorian dresses they wear."
"มีตุ๊กตาอยู่อย่างน้อยสามสิบตัว แต่ละตัวต่างมีขนาดและลักษณะที่ไม่เหมือนกัน ลักษณะเดียวที่แต่ละตัวมีเหมือนกันคือ\nชุดเดรสวิกตอเรียนแบบยาว"

# "I turn the price tag of one that looks to be about waist-height."
"ฉันพลิกป้ายราคาที่ติดอยู่บริเวณเอวของตุ๊กตาดู"

# "…It's not in my price bracket. At all."
"…ไม่ได้อยู่ในกรอบราคาที่ตั้งเป้าไว้เลย แม้แต่น้อย"

# "I do the same to each of them, getting more and more depressed as they get smaller and smaller in size."
"ฉันไล่พลิกดูแต่ละตัวที่เหลือ ยิ่งขนาดของตุ๊กตาที่ดูแต่ละตัวเล็กลงเรื่อย ๆ ก็ยิ่งเครียด"

# "That is, until I reach the very smallest one. It's affordable, just, yet of quality make and with long, auburn hair and a little blue dress."
"และฉันก็ไล่ดูราคามาจนถึงตัวที่เล็กที่สุด ซึ่งเป็นราคาที่จับต้องได้ แถมคุณภาพดี ตุ๊กตาตัวนั้นมีผมสีแดง ใส่ชุดเดรส\nสีฟ้าตัวเล็ก ๆ"

# "I decide that it's the kind of present Hanako would appreciate. Pretty-looking, and far from gaudy."
"ฮานาโกะต้องชอบของขวัญชิ้นนี้แน่นอน ดูน่ารัก และไม่ได้ดูฉูดฉาดรุงรังเกินไป"

# "After I carefully pick it up, I decide to keep looking around the store. I'm not sure whether it's because I like the atmosphere or out of simple curiosity."
"พอค่อย ๆ หยิบตุ๊กตาตัวนั้นมาแล้วฉันก็เดินดูของในร้านต่อ ไม่แน่ใจเหมือนกันว่าอยากดูเพราะชอบบรรยากาศร้าน\nหรือเพราะความอยากรู้เฉย ๆ"

stop music fadeout 2.0

show bg city_othello at left
with None

# "Peeking around the corner before I go to the next aisle, I see that the shelves in this one are stocked with wooden toys; from toy cars to intricate automatons."
"เมื่อหันมองไปรอบ ๆ ก่อนจะไปที่ชั้นวางของอีกที่ก็เห็นว่าชั้นวางของตรงนี้เป็นส่วนสำหรับของเล่นที่ทำด้วยไม้ มีตั้งแต่\nรถของเล่นไปจนถึงหุ่นที่มีกลไกใส่ไว้อย่างละเอียด"

show musicbox closed:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

# "Tucked behind a line of nutcrackers, I notice a little plain wooden box. It feels surprisingly light as I pick it up with my free hand."
"ข้างหลังหุ่นนัตแครกเกอร์มีกล่องไม้เรียบ ๆ เล็ก ๆ วางอยู่หนึ่งกล่อง เมื่อใช้มือข้างที่ว่างจับมายกดูก็พบว่าเบากว่าที่คิด\nไว้มาก"

show musicbox open:
    ypos 0.5 alpha 1.0
with charachange

play music music_musicbox

# "The lid only needs the smallest movement to pop open, the little metal drum inside beginning to rotate immediately."
"ฝากล่องเปิดออกได้อย่างง่ายดาย จานโลหะแผ่นเล็ก ๆ ที่อยู่ในกล่องเริ่มหมุนทันที"

# "For seconds on end, I simply stand there listening to the palm-sized melody."
"ฉันยืนนิ่งฟังท่วงทำนองที่ออกมาจากกล่องขนาดเท่าฝ่ามือนี้อยู่หลายวินาที"

# "As it plays, I take the tiny price tag in my fingers and bring it up to my face, the minuscule cursive writing taking some effort to read."
"ระหว่างที่กล่องดนตรีนั้นเล่นอยู่ฉันก็พลิกดูป้ายราคา ตัวเลขที่เขียนด้วยลายมือแบบหวัดนั้นอ่านยากเล็กน้อย"

# "It's affordable… sort of."
"ราคาก็… พอรับได้อยู่นะ"

show musicbox closed
with charachange

play sound sfx_switch
stop music

show musicbox closed:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide musicbox
with None

# "Grimacing slightly, I close the lid and make my way to the counter with doll and music box in hand."
"ฉันทำหน้าเบ้เล็กน้อยก่อนจะปิดกล่องดนตรีแล้วหยิบไปพร้อมกับตุ๊กตาที่ถือมาด้วยไปที่เคาน์เตอร์"

show shopkeep surprised at center
with charaenter

# "When I lay the two on the counter, the man behind it sits up and takes stock of them. He doesn't hide very well his surprise at someone of my age buying them."
"พอเอาของสองอย่างนั้นมาวางที่เคาน์เตอร์แล้วคนที่นั่งอยู่ก็ลุกขึ้นมาดู ดูสีหน้าก็รู้ว่าแปลกใจที่คนรุ่นฉันมาซื้อของ\nอย่างนี้"

show shopkeep thinking
with charachange

# "It's painful, but I hand over the money for the two and leave the store with a small opaque bag in hand."
"ฉันจำใจยื่นเงินตามราคาของสองอย่างนั้นแล้วออกจากร้านมาพร้อมถุงทึบแสงใบเล็กในมือ"

play ambient sfx_traffic fadein 0.5

scene bg city_street3
show hideaki serious at center
with locationchange

# "Hideaki being there takes me by surprise."
"ฉันแปลกใจที่เห็นฮิเดอากิยืนอยู่ตรงหน้า"

# hi "Oh… hi. I thought you'd be at the newsstand."
hi "อ้าว… ไง ไหนบอกจะไปแผงหนังสือพิมพ์"

show hideaki bored
with charachange

# hh "Akira gave me a call. She's waiting for us at the fountain with Lilly."
hh "พี่อากิระโทร. มา บอกว่ารออยู่ที่น้ำพุกับลิลลี่"

# "At least that solves the issue of trying to find them again."
"อย่างน้อยก็ไม่ต้องไปเดินหาอีกรอบละนะ"

$ renpy.music.set_volume(0.4, 0.5, channel="ambient")

scene bg city_street2
with locationskip

# "We head off back to the fountain. Hideaki's immaculate posture and presentation despite his appearance makes for a strange contrast even as we walk."
"พวกเราเดินกลับไปที่น้ำพุ ท่าทางและการแสดงออกอันเรียบร้อยของฮิเดอากินั้นดูขัดกับรูปลักษณ์ของเขาอย่าง\nประหลาด"

show lilly cane_reminisce_cas at twoleft
show akira basic_boo at tworight
with charaenter

# "Lilly and Akira stand there waiting for us, their faces hard to read."
"ลิลลี่กับอากิระทำหน้านิ่ง ๆ ยืนรอพวกเราอยู๋"

show akira basic_smile at tworight
with charachange

# aki "Hey. You ready to go, Shortie?"
aki "ไง พร้อมไปกันยัง เจ้าเตี้ย"

show bg city_street2 at bgleft
show lilly cane_reminisce_cas at left
show akira basic_smile at Transform(xpos=0.55)
with charamove

show hideaki happy at right
with charaenter

# "Hideaki's mood seems to improve as he rejoins her."
"ฮิเดอากิดูจะอารมณ์ดีขึ้นเมื่อได้กลับมาอยู่กับอากิระอีกครั้ง"

show hideaki happy_up
with charachange

# aki "Seeya Lilly, Hisao. Tell Hanako I said happy birthday."
aki "เจอกันลิลลี่ ฮิซาโอะ ฝากบอกสุขสันต์วันเกิดให้ฮานาโกะด้วย"

# hi "We will. Bye."
hi "ได้ครับ เจอกัน"

show lilly cane_weaksmile_cas
with charachange

# li "Goodbye, Akira."
li "ลาก่อนนะพี่"

hide akira
hide hideaki
show lilly cane_reminisce_cas
with charaexit

show lilly cane_reminisce_cas at center
show bg city_street2 at bgright
with charamove

# "And with that, the two disappear into the fracas of the afternoon city crowd."
"และสองคนนั้นก็กลืนหายไปกับฝูงชนอันอื้ออึงในยามบ่าย"

# "Turning to Lilly, I notice she's carrying a small bag. It's now that I realize why her disposition felt different from before; while Lilly's typically the type to wear her emotions on her sleeve, her expression and tone are clouded and difficult to read."
"เมื่อหันไปมองลิลลี่ก็พบว่าเธอถือถุงใบเล็ก ๆ อยู่ และฉันก็เพิ่งรู้ตัวว่าทำไมท่าทีของเธอถึงดูแปลกไปจากทุกที ปกติลิลลี่\nจะเป็นคนที่รู้สึกยังไงก็แสดงออกอย่างนั้น แต่สีหน้าและน้ำเสียงของเธอนั้นจับอารมณ์ได้ยาก"

# "It's more than a little off-putting, but given the effort she's making to hide her emotions, I doubt she wants to be cornered on why she's feeling this way."
"ซึ่งฉันก็ค่อนข้างหงุดหงิดอยู่เหมือนกัน แต่การที่เธอพยายามซ่อนอารมณ์ขนาดนี้ก็แปลว่าคงไม่อยากให้ใครมาซักไซ้\nถามหาเหตุผลว่าทำไมต้องทำอย่างนี้หรอก"

# hi "Already bought Hanako a present?"
hi "ได้ของขวัญให้ฮานาโกะแล้วเหรอ"

show lilly cane_weaksmile_cas
with charachange

# li "Yes. Have you?"
li "จ้ะ เธอล่ะ"

# hi "Yeah."
hi "อื้ม"

show lilly cane_sleepy_cas
with charachange

# li "Shall we head back to the bus stop then?"
li "งั้นไปที่ป้ายจอดรถกันเลยมั้ย"

# hi "Okay. There should be a bus back to Yamaku pretty soon."
hi "ได้ เดี๋ยวรถเที่ยวที่ไปยามากุน่าจะมาแล้วละ"

# "And with that, we begin to walk."
"แล้วเราสองคนก็ออกเดิน"

$ renpy.music.set_volume(0.7, 0.5, channel="ambient")

scene bg city_street1
show lilly cane_concerned_cas_close at twoleft
with locationskip

# "It feels strange compared to before. Lilly's hand on my forearm feels unusually tense, and the whole atmosphere is extraordinarily awkward."
"รู้สึกไม่เหมือนกับเมื่อกี้เลย ลิลลี่กำต้นแขนฉันแรงผิดปกติ บรรยากาศก็ชวนให้อึดอัดเอามาก ๆ"

# "The silence continues for a long while. I really don't like seeing her like this."
"ความเงียบยังคงดำเนินไปอีกสักระยะหนึ่ง ไม่อยากเห็นลิลลี่เป็นอย่างนี้เลย"

show lilly cane_sleepy_cas_close
with charachange

# li "Hanako's birthday party is going to have to be held earlier. Is the fourth going to be all right for you?"
li "เดี๋ยวจะจัดงานวันเกิดให้ฮานาโกะเร็วหน่อย วันที่สี่ได้มั้ยจ๊ะฮิซาโอะ"

# "I have no other possible obligations anyway, so I reflexively nod. Only afterwards do I remember that doing so is pointless, and quickly answer so by speech."
"ยังไงฉันก็ปฏิเสธไม่ได้อยู่แล้วละ ฉันพยักหน้าตอบไปโดยอัตโนมัติ แต่ก็เพิ่งมาคิดได้ว่าพยักหน้าไปก็ยังไม่ใช่การตอบ\nจึงรีบออกปากตอบตกลงไปทันที"

# "She tries to collect herself, a task that looks almost pitiable in how plain it is to see how distant her thoughts are."
"เธอทำตัวให้ดูปกติที่สุด ซึ่งออกจะยากสักหน่อย เพราะเห็นได้ชัดว่าใจเธอตอนนี้ไม่ได้อยู่กับตัวเลย"

show lilly cane_weaksmile_cas_close
with charachange

# li "Sorry, Hisao. You said the bus would be coming soon, right?"
li "ขอโทษทีนะฮิซาโอะ เธอบอกว่าเดี๋ยวรถจะมาแล้วใช่มั้ย"

# hi "That's right."
hi "ใช่"

# "But now that she says that, I have an idea."
"แต่พอลิลลี่ทักอย่างนั้นแล้วฉันก็นึกอะไรได้"

# hi "Actually, do you have anything to do later today?"
hi "เออนี่ บ่ายวันนี้เธอมีธุระอะไรมั้ย"

show lilly cane_oops_cas_close
with charachange

# li "I… don't believe so. Why do you ask?"
li "เหมือนจะ… ไม่นะ ถามทำไมเหรอจ๊ะ"

# hi "This is the point where I'd normally take your hand and rush you somewhere, but even without that, you'll have to trust me. Okay?"
hi "ปกติตอนนี้ฉันคงจูงมือเธอรีบพาไปที่ไหนสักที่ แต่ฉันจะไม่รีบแล้วกัน แต่เชื่อฉันแล้วตามมาหน่อยนะ"

show lilly cane_surprised_cas_close
with charachange

# "I take her hand and gently lead her on, her distant face replaced by one of mild surprise and curiosity."
"ฉันจับมือเธอไว้แล้วเดินนำทางเธอไปอย่างช้า ๆ สีหน้าเหม่อลอยของเธอแปรเปลี่ยนเป็นสีหน้าอันสงสัยและแปลกใจ\nเล็กน้อย"

stop ambient fadeout 2.0

scene bg city_karaokeint
with shorttimeskip

$ renpy.music.set_volume(1.0, 10.0, channel="ambient")
play music music_another fadein 2.0

# "As the waitress sets the cup of tea and cup of coffee that I'd ordered onto the table, I thank her before she takes her leave."
"ฉันขอบคุณพนักงานเสิร์ฟที่นำชุดถ้วยชาและกาแฟที่ฉันสั่งไปมาวางที่โต๊ะ"

# "Truth be told, I really lucked out in finding this café. I didn't really know where I was going, rather I was just looking for any café that looked relatively nice."
"ว่ากันตามจริง ที่ฉันมาเจอคาเฟนี้ก็เป็นความบังเอิญหรอก ฉันไม่ได้มีเป้าหมายด้วยซ้ำว่าจะไปไหน แค่กะว่าจะหาคาเฟ\nที่ดูบรรยากาศดี ๆ"

# "Having managed to recover a little, Lilly tentatively sips at her cup as I take a long gulp of the coffee in front of me."
"ลิลลี่ที่พอตั้งตัวได้บ้างแล้วค่อย ๆ จิบน้ำชาไปพร้อม ๆ กับฉันที่กระดกกาแฟดื่ม"

# "As I hoped, her face lights up as she realizes what flavor it is."
"และลิลลี่ก็ยิ้มออกมาอย่างที่ฉันหวังเมื่อเธอรู้ว่าเป็นชาอะไร"

show lilly basic_weaksmile_cas_close at Transform(xalign=0.5, ypos=0.15, yanchor=0.0)
with charaenter

# li "Ah… this is wonderful!"
li "อื้ม… เยี่ยมเลย!"

show lilly basic_surprised_cas_close
with charachange

# li "Hisao, how did you know that this was…?"
li "ฮิซาโอะ… เธอรู้ได้ไงว่าฉัน…"

# "I'd asked for French vanilla black tea, hedging my bets that it would be her favorite flavor, or at least one she liked. While I don't really know much about tea, it sounded like one she might appreciate."
"ฉันสั่งชาดำวานิลลาฝรั่งเศสเป็นการหยั่งเชิงว่าอาจจะเป็นรสที่ลิลลี่ชอบที่สุด หรืออย่างน้อยก็อาจจะพอเป็นรสที่เธอ\nชอบดื่ม ถึงฉันไม่ได้เชี่ยวชาญเรื่องชา แต่ชื่อก็ฟังดูเป็นอะไรที่ลิลลี่น่าจะชอบ"

# "…on the basis of her liking vanilla ice cream. A tea connoisseur I am definitely not."
"…เดาจากการที่เธอสั่งไอศกรีมรสวานิลลา ฉันไม่ใช่ผู้คร่ำหวอดในวงการชาเลยสักนิด"

# hi "It was a lucky guess. You really like tea, don't you?"
hi "แค่เดามั่ว ๆ แล้วถูกน่ะ เธอนี่ชอบชาจริงเลยนะ"

show lilly basic_smileclosed_cas_close
with charachange

# "She puts her teacup down and gives a tiny nod, that familiar small smile thankfully perched on her face once again."
"เธอวางถ้วยชาลงแล้วพยักหน้าน้อย ๆ ฉันโล่งใจที่รอยยิ้มอันคุ้นเคยนั้นปรากฏขึ้นบนใบหน้าลิลลี่อีกครั้ง"

show lilly basic_smile_cas_close
with charachange

# li "Drinking tea is… calming, I think."
li "พอได้ดื่มชาแล้ว… เหมือนใจมันสงบน่ะจ้ะ"

# hi "With the amount you drink, are you sure you're not addicted to it? Caffeine addiction's pretty common nowadays."
hi "ดื่มขนาดนี้แน่ใจนะว่าไม่ได้ติดชาน่ะ เดี๋ยวนี้คนติดกาเฟอีนก็มีกันเยอะแยะ"

show lilly basic_giggle_cas_close
with charachange

# li "Did I ever say I wasn't?"
li "แล้วฉันบอกเหรอว่าฉันไม่ได้ติดน่ะ"

# "She lets out a giggle as my head drops. We all have our vices, I suppose, and there are worse things to be addicted to."
"เธอหัวเราะคิกคักจังหวะที่ฉันห้อยหัวลง คนเราต่างก็มีข้อเสียกันทั้งนั้นแหละมั้ง แถมยังมีอะไรอย่างอื่นที่แย่กว่าให้ติด\nอีกเยอะ"

# hi "French vanilla black tea, huh? I'll have to remember that."
hi "ชาดำวานิลลาฝรั่งเศสเหรอ จะจำไว้นะ"

show lilly basic_smileclosed_cas_close
with charachange

# "For a while, we both silently drink. It's comforting to have someone like her nearby in such new surroundings, even if it's just the two of us sitting in silence."
"พวกเรานั่งดื่มกันไปเงียบ ๆ พอมีคนอย่างลิลลี่อยู่ด้วยในสภาพแวดล้อมใหม่อย่างนี้แล้วก็อุ่นใจดี ถึงแค่จะมานั่งเงียบ ๆ\nกันสองคนเฉย ๆ ก็เถอะ"

# "I begin to wonder if this feeling is the same for her, until she sets down her cup."
"ชักอยากรู้แล้วสิว่าลิลลี่จะรู้สึกอย่างนี้เหมือนกันหรือเปล่า และเธอก็วางถ้วยชาลง"

show lilly basic_emb_cas_close
with charachange

# li "Hisao, do you mind if I ask you a slightly odd question?"
li "ฮิซาโอะ ขอถามอะไรแปลก ๆ หน่อยได้มั้ยจ๊ะ"

# hi "That depends on the question, I guess."
hi "ก็อยู่ที่ว่าเธอจะถามอะไรละมั้ง"

show lilly basic_weaksmile_cas_close
with charachange

# li "I was wondering… what your favorite color is. Everyone has one, after all."
li "ฉันอยากรู้ว่า… สีที่เธอชอบที่สุดคือสีอะไรน่ะ ทุกคนต่างก็มีสีที่ชอบกันทั้งนั้นนี่นะ"

# "I almost reply before realizing why the seemingly mundane question is actually quite strange."
"จังหวะที่ฉันกำลังจะตอบก็ฉุกคิดได้ว่าทำไมคำถามที่ดูจืด ๆ อย่างนี้ถึงได้ค่อนข้างแปลก"

# hi "My favorite color? But…"
hi "สีที่ฉันชอบที่สุดเหรอ แต่ว่า…"

show lilly basic_pout_cas_close
with charachange

# "She gives a pouting look, wanting me to answer anyway. While the answer seems unavoidably wasted on her, there isn't any harm in giving it."
"เธอทำแก้มป่องคาดคั้นคำตอบจากฉัน ถึงจะตอบไปแล้วไม่มีค่าอะไร แต่ก็ไม่เสียหายอะไรหรอก"

# hi "I've always had a thing for green. I'd say that's my favorite."
hi "ฉันรู้สึกว่าชอบสีเขียวน่ะ นั่นแหละสีที่ฉันชอบที่สุด"

show lilly basic_satisfied_cas_close
with charachange

# li "Green, is it? What things do you think of when contemplating that color?"
li "สีเขียวเหรอ พอคิดถึงสีเขียวแล้วจะนึกถึงอะไรเหรอจ๊ะ"

# hi "I suppose… grass fields and trees in summer. The Army as well, with camouflage."
hi "ก็คง… ทุ่งหญ้ากับต้นไม้ในฤดูร้อนละมั้ง แล้วก็ทหารด้วย พวกชุดลายพราง"

show lilly basic_planned_cas_close
with charachange

# li "Men always seem to like the military."
li "ผู้ชายดูจะชอบเรื่องทหารกันทุกคนเลยนะ"

show lilly basic_smile_cas_close
with charachange

# li "But… that sounds like a nice color. A very nice color."
li "แต่ว่า… ฟังดูเป็นสีที่ดีจังเลยนะ เป็นสีที่ดีมาก ๆ"

# "She nods her head a little, as if approving of the choice. Considering how foreign the concept of color is to her mind, labeling it by association seems reasonable enough."
"เธอพยักหน้าน้อย ๆ ราวกับเห็นด้วย ก็คงไม่แปลกอะไรกับการผูกสีไว้กับอะไรอย่างอื่น เพราะคำว่าสีนั้นนับได้ว่า\nเป็นอะไรที่ลิลลี่แทบไม่รู้จัก"

# hi "If everyone has a favorite color, then what's yours?"
hi "ถ้าทุกคนมีสีที่ชอบที่สุดแล้ว เธอชอบสีอะไรล่ะ"

show lilly basic_smileclosed_cas_close
with charachange

# li "White. I'm told that's the color of snow, and of ice cream."
li "สีขาวจ้ะ ฉันรู้มาว่าสีขาวเป็นสีของหิมะ แล้วก็ไอศกรีม"

# hi "You're no better than me then, if you only like that color because of a favorite food. I guess white is nice too, though."
hi "เนี่ย เธอก็ไม่ต่างจากฉันหรอก ชอบสีแค่เพราะเป็นของที่ชอบกินเนี่ย แต่สีขาวก็ดีเหมือนกันละนะ"

# hi "And speaking of colors, it'll be getting dark soon. Let me help you up."
hi "พูดถึงสี เดี๋ยวจะมืดแล้ว ให้ฉันช่วยนะ"

show lilly basic_smile_cas_close
with charachange

show lilly basic_smile_cas_close at center
with charamove

# "Lilly offers her hand, which I take in mine to help lever her up from her seat at the table. Its softness compared to mine takes me off guard, as I'm really not used to such casual contact."
"ลิลลี่ยื่นมือมาให้ฉันจับดึงตัวเธอลุกขึ้นมาจากเก้าอี้ ฉันนึกตกใจกับความนุ่มของมือเธอที่สัมผัสกับมือของฉัน\nด้วยความที่ฉันไม่ชินกับการถูกเนื้อต้องตัวอย่างนี้เท่าไหร่"

# "It doesn't seem to bother her at all though. While it seems obvious why, it feels like just one more ladylike aspect to her."
"แต่ลิลลี่ก็ดูไม่ได้คิดมากอะไร และแม้เหตุผลจะเห็นได้ชัด ฉันก็ยังรู้สึกว่าสิ่งนี้เป็นแค่ความเป็นกุลสตรีอย่างหนึ่งของเธอ\nมากกว่า"

# "As her hand moves to her pocket, I quickly cut her off."
"ทันทีที่ลิลลี่เตรียมจับกระเป๋าสตางค์ของตัวเองฉันก็ตัดบททันที"

# hi "Don't worry, I'll pay for this."
hi "ไม่เป็นไร ฉันเลี้ยงเอง"

show lilly basic_cheerful_cas_close at center
with charachange

# li "Oh. Thank you, Hisao."
li "อ้าว ขอบคุณนะจ๊ะฮิซาโอะ"

# "She gives an earnest smile at the gesture, a reward much greater than that of her words."
"เธอยิ้มจริงใจให้ฉันที่ปรามไว้ ซึ่งเป็นรางวัลที่มีค่ามากกว่าคำพูดของเธอเสียอีก"

stop music fadeout 2.0

scene bg suburb_roadcenter_ni
with shorttimeskip

$ renpy.music.set_volume(0.2, 0.5, channel="ambient")
play ambient sfx_cicadas fadein 0.5

# "By the time we step off the bus, it's well and truly dark."
"กว่าจะได้ลงจากรถบัสก็มืดค่ำเต็มที่แล้ว"

$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

scene bg school_road_ni
with locationskip

# "We make our way up the hill in silence, both of us behaving a little awkwardly, probably because of the day's events."
"พวกเราเดินขึ้นเขากันไปเงียบ ๆ ด้วยความอึดอัดเล็กน้อย คงเพราะเรื่องที่เกิดวันนี้แหละ"

# "While I'm still concerned over Lilly's withdrawn nature after meeting with her sister, the fact I managed to cheer her up even slightly feels like a personal victory."
"ถึงจะยังห่วงที่ลิลลี่ดูเว้นระยะจากฉันหลังจากที่เธอได้คุยกับพี่สาวของเธอแล้ว แต่ฉันก็รู้สึกประสบความสำเร็จที่พอจะ\nทำให้ลิลลี่ร่าเริงขึ้นได้บ้าง"

# "But… it feels like the air between us has changed. Maybe it's only a bit, but it's something I don't think either of us realized before."
"แต่… รู้สึกเหมือนบรรยากาศระหว่างเราเปลี่ยนไป อาจจะเปลี่ยนไปเล็กน้อย แต่เป็นอะไรบางอย่างที่ฉันคิดว่าเราสองคน\nคงไม่เคยรู้ตัวมาก่อนเลย"

show lilly cane_weaksmile_cas_ni at center
with charaenter

# li "That was… a date, wasn't it?"
li "สรุปวันนี้เรา… ไปเดตกันมาใช่มั้ยจ๊ะ"

# "It was. That doesn't elude either of us, the question's answer being so self-evident as to be rhetorical."
"ใช่ เราสองคนต่างก็รู้ดี คำตอบของคำถามนั้นชัดเสียจนเหมือนถามแบบรำพึงมากกว่า"

# "Awkward as it may be, I don't think this feeling is bad. In fact, quite the opposite. I don't know what it is, I certainly can't be sure, but it feels like something a little more than friendship."
"ถึงจะอึดอัด แต่ก็ไม่ใช่ความรู้สึกที่แย่อะไร กลับตรงกันข้ามด้วยซ้ำ ฉันไม่รู้ว่าสิ่งนี้คืออะไร ฉันไม่อาจรู้ได้แน่ แต่รู้สึก\nเหมือนเป็นอะไรที่ขยับขึ้นมาจากมิตรภาพเล็กน้อย"

# "Understanding? Empathy? Searching for words to adequately describe it is difficult. Nonetheless…"
"ความเข้าใจ? ความเห็นใจ? การจะหาคำที่เหมาะสมเพื่อมาอธิบายนั้นยากยิ่ง แต่แม้กระนั้นก็ตาม…"

# hi "Would you like do this again sometime, Lilly? Without shopping for presents?"
hi "ไว้ไปด้วยกันอีกดีมั้ยลิลลี่ แบบที่ไม่ต้องไปหาซื้อของขวัญแล้วน่ะ?"

show lilly cane_emb_cas_ni
with charachange

# "The tentative question is met with the same look from Lilly as before. Her pale skin makes the rosy tint of her cheeks just slightly more noticeable and her face, though still pointed to the street ahead of her, lowers. Just a little."
"ลิลลี่ยังทำสีหน้าเช่นเดิมกับฉันที่โยนหินถามทางไปอย่างนั้น ใบหน้าขาวนวลของเธอทำให้สีแดงเรื่อนั้นเห็นได้ชัดขึ้น\nนิดหนึ่ง เธอยังคงมองทางข้างหน้าก้มหน้าต่ำเล็กน้อย"

show lilly cane_cheerful_cas_ni
with charachange

# li "…Okay."
li "…ได้สิ"

stop ambient fadeout 2.0

scene black
with dissolve


#**************************************

label th_L4:

scene bg school_girlsdormhall
with locationchange

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")

# "I walk down the hall of the girls' dormitories, my schoolbag in hand."
"ฉันเดินไปตามโถงทางเดินหอหญิงพร้อมกระเป๋านักเรียนในมือ"

# "A doll lies inside, carefully placed on top of a small box. I've been carrying the box in there for a while now, still not sure of what to do with it."
"ข้างในกระเป๋ามีตุ๊กตาที่ถูกวางบนกล่องใบเล็ก ๆ อยู่ ฉันเอากล่องใส่กระเป๋ามาสักพักแล้วเพราะไม่รู้เหมือนกันว่าจะเอาไป\nทำอะไรดี"

# "This whole situation, come to think of it, is bizarre."
"พอมาลองคิด ๆ ดูแล้ว สถานการณ์เหล่านี้ดูออกจะประหลาด"

# "While I've known of Hanako's upcoming birthday party for a while now, I had no idea of exactly what the celebrations would be until I found a single note left in the abandoned tea room earlier today."
"ถึงจะรู้ว่าเดี๋ยวจะจัดงานวันเกิดฮานาโกะกันก็จริง แต่ก่อนหน้านี้ฉันไม่รู้เลยว่าจะจัดยังไงกัน มารู้อีกทีก็วันนี้ตอนที่เจอ\nกระดาษโน้ตที่วางไว้ในห้องน้ำชาที่ไม่มีใครอยู่"

# "I hold it up and read it again, doublechecking the instructions. The plain black handwriting's fairly legible despite Lilly's blindness, clearly thanks to considerable effort and care."
"ฉันหยิบกระดาษโน้ตนั้นขึ้นมาอ่านอีกรอบแล้วดูรายละเอียดที่เป็นตัวอักษรสีดำนั้นให้แน่ใจ เป็นลายมือที่อ่านค่อนข้าง\nง่ายแม้คนเขียนจะตาบอดก็ตาม ซึ่งแสดงให้เห็นได้ชัดถึงความพยายามและเอาใจใส่ของลิลลี่"

window hide

# $ written_note(u"Hisao,\n\nWe'll be holding a party at my place. Please come at six o'clock to room 225 in the girls' dormitory.\nSorry for notifying you this way, but I have class representative duties.\n\n- Lilly Satou", text_args={"color":"#000000"})
$ written_note(u"ฮิซาโอะ\n\nพวกเราจะจัดงานเลี้ยงกันที่ห้องของฉัน\nมาหาที่หอหญิงห้อง 225 ณ เวลา 18:00 น.\nขอโทษที่ต้องเขียนบอกอย่างนี้นะจ๊ะ\nพอดีฉันติดธุระหัวหน้าห้อง\n\n\n- ลิลลี่ ซาโต้", text_args={"color":"#000000"})

window show

# "Not reassured, I continue walking down the hallway until I reach Lilly's dormitory room. I hesitate for a second, but eventually give three sharp taps on the door."
"ฉันเดินตามโถงทางเดินไปเรื่อย ๆ จนถึงห้องลิลลี่ด้วยความยังไม่มั่นใจ ฉันนึกลังเลอยู่แวบหนึ่ง แต่สุดท้ายก็เคาะประตูไป\nสามรอบ"

play sound sfx_doorknock2
with Pause(0.5)

# "A brief and muffled exchange of words can be heard from the other side. Listening closer, I can just pick out Hanako and Lilly's voices."
"มีเสียงคุยกันอู้อี้อยู่ในห้องครู่หนึ่ง พอฟังดี ๆ แล้วก็ได้ยินแต่เสียงฮานาโกะกับลิลลี่"

# "As they finish, Lilly calls out."
"พอคุยกันเสร็จลิลลี่ก็เรียก"

# li "Might that be Hisao?"
li "ฮิซาโอะหรือเปล่าจ๊ะ"

# hi "Yep. I got the note you left for me."
hi "อื้ม อ่านโน้ตที่เขียนทิ้งไว้แล้วนะ"

# li "You can come in, the door is unlocked."
li "เข้ามาได้เลยจ้ะ ประตูไม่ได้ล็อก"

# "Glad that I managed to get the right room, I press down on the handle and let myself in."
"โล่งไปที่มาถูกห้อง ฉันจับมือจับประตูแล้วบิดเปิดเข้าไป"

play sound sfx_dooropen

# "As the door swings open, my greeting to them is stolen from my mouth."
"พอเปิดประตูฉันก็ลืมคำทักทายทั้งหลายสิ้น"

window hide

play music music_one fadein 10.0

scene ev lilly_bedroom:
    truecenter
    zoom 1.1 subpixel True
    ease 15.0 zoom 1.0
with GenericWhiteout(0.5,0.1,4.0)

window show

# "Lilly sits at a low table in the center of the room in her pajamas, while on the other side sits Hanako in a nightgown. Being dressed in only my normal school clothes, I feel quite out of place."
"ลิลลี่ใส่ชุดนอนนั่งอยู่ที่โต๊ะเตี้ยกลางห้อง ส่วนฮานาโกะใส่ชุดโปร่ง ๆ นั่งอยู่ฝั่งตรงข้าม รู้สึกแปลกแยกขึ้นมาเลยที่ใส่\nชุดนักเรียนมาคนเดียว"

# "I steal a quick glance at the lovely sight of the two, my eyes tearing themselves from Lilly's long, thin and pale legs only with a measure of reluctance."
"ฉันกวาดตามองสองคนตรงหน้าซึ่งดูน่ารักก่อนจะเบนสายตาออกจากขาเรียวยาวขาวนวลของลิลลี่ทั้งที่ยังไม่อยาก\nละสายตาอยู่เหมือนกัน"

# hi "H-hi. I… think I brought everything that was needed."
hi "งะ ไง ของ… ที่เอามาน่าจะครบแล้วนะ"

scene ev lilly_bedroom_large:
    xpos -130 ypos -400 subpixel True
    acdc_warp 12.0 ypos -800
with flash

# "She smiles and nods. I wonder if she's even aware of the pleasant sight she makes. The thin dark blue silk of her pajamas really suits her, accentuating both her eyes and her curves."
"เธอยิ้มพยักหน้า จะรู้ตัวมั้ยนะว่าตัวเองน่ะน่ารักขนาดไหน ชุดนอนบาง ๆ สีน้ำเงินที่ทำจากผ้าไหมนั้นเหมาะกับเธอจริง ๆ\nเพราะช่วยขับเน้นทั้งตาและส่วนโค้งเว้าของเธอ"

# "The look of her last night, that tentative and almost shy demeanor, seems all but replaced by her coy nature. It's nice to see her confidence returned, though I can't help casting my mind back to how she looked back then."
"ตัวเธอเมื่อคืนวานที่ดูเป็นคนลังเลและเขินอายนั้นถูกแทนที่ด้วยความขี้เล่น ฉันดีใจที่เห็นเธอมั่นใจขึ้นมาอย่างนี้ แต่ก็\nอดคิดถึงท่าทางของเธอเมื่อตอนนั้นไม่ได้อยู่ดี"

scene ev lilly_bedroom_large:
    xpos -830 ypos -200 subpixel True
    acdc_warp 12.0 ypos 0
with flash

# "I look to Hanako, who nervously sits opposite her in her gown. It isn't a surprise that she'd wear something so conservative, though it definitely looks cute."
"ฉันหันไปมองทางฮานาโกะที่ใส่ชุดนอนนั่งเกร็ง ๆ อยู่ฝั่งตรงข้าม ไม่แปลกใจเท่าไหร่ที่ชุดนอนของเธอเป็นแบบเรียบ ๆ\nแต่ก็ดูน่ารักดี"

# hi "Hi, Hanako. Happy birthday."
hi "ไง ฮานาโกะ สุขสันต์วันเกิด"

# ha "Ah… th-thank you."
ha "อ๊ะ… ขะ ขอบคุณนะ"

# "She's unusually skittish, despite the fact that she's warmed up to me considerably over the weeks we've come to know each other. This is a pretty unusual situation, I guess."
"เธอดูประหม่ากว่าปกติ ทั้งที่เธอเปิดใจให้ฉันบ้างแล้วตลอดระยะเวลาหนึ่งสัปดาห์ที่เราได้รู้จักกัน แต่ก็คงเพราะสถานการณ์\nตอนนี้ออกจะพิเศษสักหน่อยละนะ"

scene ev lilly_bedroom
with flash

# li "Feel free to take a seat, Hisao. I'll just pour you two some tea."
li "เชิญนั่งได้ตามสบายเลยจ้ะฮิซาโอะ เดี๋ยวฉันรินชาให้"

# hi "Sure thing."
hi "ได้"

$ renpy.music.set_volume(0.8, 2.0, channel="music")

scene bg school_dormlilly
with locationchange

# "Lilly takes the steaming red teapot from the side of the table and gently pours its contents into our teacups as I take a seat beside them, setting my bag against the nearby wall."
"ลิลลี่ยกกาน้ำชาสีแดงมาจากข้างโต๊ะแล้วรินน้ำชาใส่ถ้วยชาของพวกเราให้ช้า ๆ ไประหว่างที่ฉันกำลังนั่งลงพร้อมวาง\nกระเป๋าไว้ที่กำแพงข้าง ๆ"

# "With my senses returned and hormones somewhat calmer, I realize that this is the first time I've ever been in Lilly's room."
"พอตั้งสติและตั้งตัวได้บ้างแล้วก็ถึงนึกได้ว่าครั้งนี้เป็นครั้งแรกที่ได้มาห้องลิลลี่"

# "The first thing I notice is the ambient smell, just slightly different from that in mine… probably faint perfume, or nail polish. It could be anything of a girl's, really."
"อย่างแรกที่ฉันสัมผัสได้คือกลิ่นอ่อน ๆ ที่ต่างจากห้องของฉันไปเล็กน้อย… อาจจะเป็นกลิ่นน้ำหอมไม่ก็น้ำยาทาเล็บ\nจริง ๆ ก็เป็นกลิ่นอะไรของผู้หญิงนั่นแหละ"

# "Another is the plain nature of the room, visually. Beige walls, a smart yet unadorned cabinet, the lack of posters or wall hangings. It's distinctly utilitarian, something I should have anticipated given her blindness."
"อีกอย่างคือสภาพห้องที่ดูเรียบ ๆ กำแพงสีเบจ ตู้เรียบโก้ไร้การตกแต่ง ตามกำแพงไม่มีโปสเตอร์หรือภาพแขวนใด ๆ\nเป็นห้องที่เน้นการใช้สอยโดยแท้จริง ซึ่งก็ควรเดาได้แต่แรกแล้วเพราะลิลลี่ตาบอด"

# "The only thing that really seems out of the ordinary is several piles of books sitting on the floor, each reaching from roughly knee height to waist height. Some of them have printed titles, others are entirely blank except for dots of Braille."
"อย่างเดียวที่ดูเด่นสะดุดตาคือกองหนังสือที่วางอยู่บนพื้น แต่ละกองสูงประมาณเข่าไม่ก็ประมาณเอว บางเล่มมีปกพิมพ์\nตัวอักษรไว้อยู่ ส่วนเล่มอื่นนั้นมีแต่จุดอักษรเบรลล์"

# "The fact that the ones with printed titles are uniformly in English is interesting, though not completely unexpected. She did mention her parents impressing the language upon her and Akira, after all."
"ซึ่งน่าสนใจดีที่เล่มที่มีพิมพ์ตัวอักษรนั้นเป็นภาษาอังกฤษล้วน แต่ก็ไม่ได้แปลกใจอะไร ลิลลี่เองก็เคยเล่าแล้วว่าที่บ้าน\nเสริมภาษาอังกฤษให้ตัวเองกับอากิระด้วย"

# hi "Your room looks nice, Lilly."
hi "ห้องสวยดีนะลิลลี่"

show hanagown distant:
    center
    ypos 1.15
with charaenter

# "I hear a call of thanks from beside my shoulder. Looking back to Hanako, her gaze is fixed on her lap and her hands are nervously clutching her gown."
"ฉันได้ยินคำขอบคุณลอยมาจากข้าง ๆ ไหล่ฉัน พอหันไปมองฮานาโกะก็เห็นว่าเธอจ้องตักกำชุดนอนตัวเอง\nด้วยความเกร็งอยู่"

# "It's now that I notice why. With these clothes on, the extent of her scarring is far more visible; reaching down her neck and out to cover her right shoulder."
"และฉันก็เพิ่งรู้ตัวว่าเพราะอะไร พอฮานาโกะใส่ชุดแบบนี้แล้วจะเห็นแผลเป็นได้มากขึ้น ซึ่งลากยาวตั้งแต่คอลงมาจนถึง\nตามไหล่ขวา"

# "Considering this is a party for her, she doesn't really look like she's enjoying the experience now that I'm here."
"ทั้งที่เป็นงานเลี้ยงจัดเพื่อเธอแท้ ๆ แต่พอฉันมาด้วยแล้วเหมือนฮานาโกะจะสนุกได้ไม่เต็มที่เลย"

# hi "So how old are you turning? Eighteen?"
hi "แล้วปีนี้อายุเท่าไหร่แล้วล่ะ สิบแปด?"

show hanagown worry
with charachange

# "Her look of surprise, not at all helped by her total lack of skill at hiding her feelings, shows that she was trying to mentally tune me out. This is really quite awkward."
"สีหน้าฮานาโกะที่ดูตกใจอย่างเห็นได้ชัดด้วยความที่เธอนั้นซ่อนอารมณ์ไม่เก่งทำให้รู้ได้ว่าเธอกำลังพยายาม\nทำเหมือนว่าฉันไม่ได้อยู่ตรงนี้ อึดอัดแฮะ"

# ha "Y-yes."
ha "ชะ ใช่"

# hi "On the plus side, there's only two more years till you can drink. So who's older? You or Lilly?"
hi "ถ้ามองในแง่ดี อีกสองปีก็ดื่มได้แล้วนะ แล้วเธอกับลิลลี่ใครแก่กว่ากันเหรอ"

show hanagown normal
with charachange

# ha "Lilly. She had her birthday in… F-February. What about… yours?"
ha "ลิลลี่ ลิลลี่เกิดเดือน… กะ กุมภาฯ แล้ว… นายล่ะ"

# hi "Earlier this year, so it's already passed."
hi "ช่วงต้นปีนู่น ผ่านมาแล้วน่ะ"

# "Unstated is that it passed while I was stuck in the hospital. That was… a particularly low point of the experience."
"ฉันปกปิดส่วนที่ว่าวันเกิดนั้นเป็นช่วงที่เข้าโรงพยาบาลพอดี ตอนนั้น… เป็นช่วงที่ตกต่ำเป็นพิเศษเลย"

show hanagown distant
with charachange

show hanagown distant:
    tworight
    ypos 1.15
show bg school_dormlilly at bgright
with charamove

show lilly basic_smileclosed_paj:
    twoleft
    ypos 1.2
with charaenter

play sound sfx_teacup

# "Conversation with her dries up as quickly as expected. It isn't long before Lilly's finished preparing our drinks, setting down the three teacups in front of us."
"เรื่องที่จะคุยนั้นหมดลงเร็วตามคาด ไม่นานลิลลี่ก็จัดแจงชาวางถ้วยน้ำชาสามถ้วยให้แต่ละคนจนเสร็จเรียบร้อย"

# "I pick mine up, immediately noticing a much stronger aroma and taste than the tea we've been having."
"พอยกถ้วยชาขึ้นดื่มก็รู้สึกถึงกลิ่นและรสชาติที่เข้มกว่าชาที่ดื่มด้วยกันทุกที"

# hi "Huh, it tastes different than the tea we have in school."
hi "หืม ไม่เหมือนชาที่กินด้วยกันในห้องน้ำชาเลย"

show lilly basic_smile_paj
with charachange

# li "It's a different variety, rather than the kind we've been having there. You've never tasted Orange Jaipur before?"
li "เป็นรสอีกแบบหนึ่งน่ะจ้ะ ไม่เหมือนที่ดื่มกันที่ห้องน้ำชา เธอไม่เคยดื่ม ‘{i}Orange Jaipur{/i} (ชาดำกลิ่นส้ม)’\nใช่มั้ยจ๊ะ"

# hi "Not… that I can remember. I usually drink coffee after all, like when we were in town. This is nice, though."
hi "เหมือนจะ… ไม่ ปกติฉันก็ดื่มแต่กาแฟนี่นะ เหมือนตอนที่ไปเข้าตัวเมืองวันนั้น แต่อันนี้ก็อร่อยดีนะ"

show hanagown normal
with charachange

# "As we settle down and sip, Hanako seems to become more relaxed, or at least a bit less tense about my presence."
"พอดื่มชากันสบาย ๆ แล้วแล้วฮานาโกะก็ดูจะหายเกร็งไปบ้าง อาจจะไม่ขนาดนั้น แต่ก็ไม่ได้เกร็งที่ฉันอยู่ด้วยเท่าไหร่แล้ว"

# "We all finish our cups at about the same time, with Hanako failing rather badly at hiding her anticipation for the cake that's sitting to the side, begging to be eaten."
"พวกเราดื่มชากันหมดแทบจะพร้อมกัน ท่าทางฮานาโกะแสดงชัดว่าอยากกินเค้กที่ตั้งอยู่บนโต๊ะคอยยั่วน้ำลายนั้นเต็มที"

stop music fadeout 4.0

# "Come to think of it, I'm feeling very eager myself. First things first, though."
"จะว่าไปฉันเองก็อยากกินแล้วเหมือนกัน แต่ก่อนอื่นเลย"

# hi "Lilly?"
hi "ลิลลี่?"

show lilly basic_planned_paj
with charachange

# li "Yes, now is good."
li "จ้ะ ตอนนี้แหละ"

# "Each of us knowing exactly what the other means, I lean sideways and dig around in my bag for the doll I bought Hanako as Lilly gets up and retrieves her gift."
"พวกเราสองคนต่างรู้กันว่าพูดถึงเรื่องอะไรอยู่ ฉันเอี้ยวตัวไปคุ้ยหาตุ๊กตาที่ซื้อมาให้ฮานาโกะซึ่งอยู่ในกระเป๋า ส่วนลิลลี่\nลุกไปหยิบของขวัญที่ตัวเองซื้อมา"

# "Hiding our gifts in our hands, we present them both on the table at the same time."
"พวกเราซ่อนของขวัญไว้ในมือก่อนจะเอามาวางไว้บนโต๊ะพร้อมกัน"

show lilly basic_cheerful_paj
show hanagown normal_blush
with charachange

# $ doublespeak (li, hi, "Happy birthday!")
doublespeak (li,hi "สุขสันต์วันเกิด!")

# "Hanako silently sits looking at them for seconds on end, out of sheer surprise."
"ฮานาโกะนั่งนิ่งมองของขวัญอยู่นานหลายวินาทีด้วยความประหลาดใจ"

# "My little wooden doll, replete with Victorian-era dress and little hat, lies next to a light brown and fluffy stuffed bear from Lilly."
"ตุ๊กตาไม้ที่ใส่ชุดยุควิกตอเรียนกับหมวกใบเล็ก ๆ ของฉันวางอยู่ข้างตุ๊กตาหมีนุ่มฟูสีน้ำตาลอ่อนของลิลลี่"

show hanagown distant
with charachange

# "She clutches at her gown as she moves to speak, not taking her eyes off the modest presents."
"ฮานาโกะกำชุดนอนแน่นพลางพูดโดยที่ไม่ละสายตาไปจากของขวัญเล็ก ๆ น้อย ๆ ของพวกเรา"

show hanagown distant_blush
with charachange

# ha "Th… thank you… Lilly and… Hisao…"
ha "ขะ… ขอบคุณนะ… ลิลลี่… ฮิซาโอะ"

play music music_serene fadein 6.0

scene unlock_ev lilly_hanako_hug_end
show black
show ev lilly_hanako_hug:
    xalign 0.5 yalign 1.0 alpha 0.0 subpixel True
    parallel:
        linear 5.0 alpha 1.0
    parallel:
        easein 15.0 yanchor 0.0 ypos -0.15

with locationskip

# "Her voice begins to crack as Lilly reaches forward, wrapping her in a soft embrace."
"เสียงฮานาโกะเริ่มสะอื้นจังหวะเดียวกับตอนที่ลิลลี่เข้าไปโอบไว้"

# "The sight of Hanako holding Lilly so tightly is heartwarming, so much so that I couldn't wipe the smile off my face even if I wanted to."
"ภาพที่ฮานาโกะนั้นกอดลิลลี่แน่นช่างอบอุ่นหัวใจเสียจนฉันฝืนหุบยิ้มไม่ได้เลย"

# "As Lilly gently rests her face on Hanako's head, she speaks so quietly and softly that I can barely hear."
"ลิลลี่แนบหน้าเข้ากับหัวฮานาโกะพลางกระซิบแผ่วเบาเสียจนฉันแทบไม่ได้ยิน"

# li "Happy birthday, Hanako."
li "สุขสันต์วันเกิดจ้ะฮานาโกะ"

# hi "Happy birthday."
hi "สุขสันต์วันเกิด"

# "Hanako gives a small nod, holding on to Lilly for a time before breaking off and wiping an eye."
"ฮานาโกะพยักหน้าน้อย ๆ กอดลิลลี่อยู่อีกพักหนึ่งก่อนจะผละออกแล้วเช็ดน้ำตา"

# "I guess that for Hanako simply having someone, anyone, to be there and love her would be special. The fact that Lilly and I can now share that role for her is something I think I will always be grateful for."
"สำหรับฮานาโกะ ขอแค่มีใครก็ได้อยู่เคียงข้างคอยรักเธอก็คงเป็นอะไรที่พิเศษแล้วละนะ ฉันคงปลื้มไปอีกนานที่ฉัน\nกับลิลลี่ได้เป็นคนที่ว่านั้นสำหรับเธอ"

scene ev hanako_presents1
with locationskip

# "Hanako gently takes the doll and teddy bear, holding them both to her chest as she warmly smiles."
"ฮานาโกะคว้าตุ๊กตาสองตัวนั้นขึ้นมาเบา ๆ แล้วกอดไว้พลางยิ้มอบอุ่น"

# "For a long time, all three of us simply sit in happy silence. The quiet is not broken until Lilly's soft voice beckons."
"พวกเราสามคนนั่งกันเงียบ ๆ อย่างมีความสุขอยู่นานสองนาน จนกระทั่งลิลลี่พูดขึ้นมา"

# li "Shall we have at the cake, then?"
li "งั้นทานเค้กกันเลยมั้ยจ๊ะ"

scene bg school_dormlilly
show lilly basic_smile_paj:
    twoleft
    ypos 1.2
show hanagown smile:
    tworight
    ypos 1.15
with locationskip

# "Her proposal is met with two looks of unhidden anticipation."
"คำตอบของคำชวนนั้นเป็นสีหน้าที่แสดงความอยากเต็มที่ของสองคน"

# hi "No argument from me."
hi "ไม่ขัด"

# ha "Okay."
ha "ได้"

stop music fadeout 2.0

scene bg school_dormlilly
show lilly basic_smileclosed_paj:
    twoleft
    ypos 1.2
show hanagown normal:
    tworight
    ypos 1.15
with shorttimeskip

# hi "Phew, that was good."
ha "ฮู่ว อร่อย"

play music music_dreamy fadein 4.0

# "I contentedly sit back, both Lilly and Hanako looking just as satisfied with the food as I. It took some effort, but we managed to finish off the cake in one go."
"ฉันนั่งเอนตัวด้วยความอิ่มหนำ ทั้งลิลลี่และฮานาโกะก็ไม่ต่างกันกับฉัน เค้กเยอะไปหน่อย แต่พวกเราสามคนก็ช่วยกัน\nกินจนหมดจนได้"

show hanagown normal_blush
with charachange

# ha "I don't think I could fit any more in."
ha "อิ่มจนกินอะไรไม่ไหวแล้วละ"

show lilly basic_weaksmile_paj
with charachange

# li "I think next time I'll buy a smaller cake."
li "คราวหน้าคงต้องซื้อก้อนที่เล็กลงมาหน่อยสิเนี่ย"

show hanagown smile
with charachange

# "Hanako and I give a chuckle, but I can't help noticing that, come this time next year, we'll have graduated from Yamaku."
"ฮานาโกะกับฉันแค่นหัวเราะ แต่ก็อดคิดไม่ได้ว่ากว่าจะถึงวันเกิดอีกทีปีหน้าพวกเราก็เรียนจบกันแล้ว"

# "That fact is somewhat depressing, since I finally feel as if my life is starting to get back into some kind of order."
"คิดแล้วก็หดหู่เหมือนกัน ทั้งที่ตอนนี้เหมือนอะไร ๆ ในชีวิตฉันจะเริ่มเข้าที่เข้าทางแล้วแท้ ๆ"

# "Idly looking around Lilly's neat and orderly room, her books catch my eye once again."
"ฉันมองไปรอบห้องที่เป็นระเบียบเรียบร้อยของลิลลี่เล่น ๆ และฉันก็สะดุดตากับกองหนังสือเหล่านั้นอีกครั้ง"

# "This may be a little impetuous, but my curiosity gets the better of me. Besides, I don't think she'll mind in any case."
"อาจจะเป็นคำถามที่โพล่งขึ้นมาแบบไม่ได้คิดอะไร แต่ฉันก็อยากรู้อยู่ดี อีกอย่าง ลิลลี่คงไม่ถือหรอก"

# hi "Hey Lilly, do you mind if I take a look at one of your books?"
hi "นี่ ลิลลี่ ขอดูหนังสือเธอหน่อยได้มั้ย"

show lilly basic_smile_paj
with charachange

# li "You're quite welcome to, Hisao."
li "ได้เลยจ้ะฮิซาโอะ"

show lilly basic_planned_paj
with charachange

# li "That said, if you can overcome two language barriers I will be quite impressed."
li "แต่ถึงอย่างนั้น ถ้าเธอผ่านกำแพงภาษาสองชั้นไปได้ ฉันคงประทับใจทีเดียว"

# hi "Two? Braille and… oh right, English."
hi "สองชั้น? อักษรเบรลล์กับ… อ้อ จริงสิ ภาษาอังกฤษ"

show lilly basic_smile_paj
with charachange

# "She gives a nod."
"ลิลลี่พยักหน้า"

# hi "I knew you were studying English, but I'm still amazed that you're this proficient at it."
hi "คือรู้แหละว่าเรียนภาษาอังกฤษอยู่ แต่ก็อดทึ่งไม่ได้แฮะที่เธอเก่งขนาดนี้"

show lilly basic_giggle_paj
with charachange

# li "One could say it's a perfect way to avoid people borrowing my collection."
li "จะว่าเป็นวิธีกันไม่ให้คนอื่นยืมหนังสือของฉันก็ได้แหละนะ"

# "She says it in jest, but I am a little disappointed. Having all these books around me with no way of reading them feels like one big tease."
"เธอพูดติดตลก แต่แอบผิดหวังหน่อย ๆ แฮะ มีหนังสือเยอะขนาดนี้แต่อ่านไม่ออกสักอย่างแล้วรู้สึกเหมือนโดนแกล้งเลย"

# "Hanako giggles quietly as I reach over the closest pile, plucking the topmost book with only a cursory glance. “Death on the Nile,” in large letters on the cover, is the only printed text to be seen."
"ฮานาโกะหัวเราะคิกคัก ฉันมองคร่าว ๆ แล้วเอื้อมไปคว้าหนังสือเล่มที่อยู่ด้านบนกองที่อยู่ใกล้มือสุด บนปกมีแค่\nตัวอักษรตัวใหญ่ที่พิมพ์ว่า ‘{i}Death on the Nile{/i}’"

$ renpy.music.set_volume(0.5, 0.5, channel="music")
play sound sfx_paper
show ev braille at Fullpan(10.0, dir="right")
with locationskip

# "I sit down for a while with the book open on my lap as Lilly and Hanako talk."
"ฉันนั่งเปิดหนังสือดูพักหนึ่งระหว่างที่ลิลลี่กับฮานาโกะคุยกัน"

# "Try as I might to feel out the dots of Braille printed on each page, they seem to blend into one another and become indistinct."
"ถึงจะพยายามลูบตัวอักษรเบรลล์ที่พิมพ์อยู่แต่ละหน้าสักเท่าไหร่ก็รู้สึกเหมือนแต่ละจุดนั้นกลืนไปด้วยกันหมดจนแยก\nไม่ออกเลย"

# "I'd thought this to be a lot easier than it actually is. With some practice though, I could see someone with a better sense of touch than mine managing to read at a pretty fast speed."
"ทีแรกก็นึกว่าจะอ่านง่ายกว่านี้เสียอีก แต่ถ้าคนที่ประสาทสัมผัสดีกว่าฉันได้ฝึกสักหน่อยก็น่าจะอ่านได้เร็วพอตัวเลย"

$ renpy.music.set_volume(1.0, 0.5, channel="music")

scene bg school_dormlilly
show lilly basic_smileclosed_paj:
    twoleft
    ypos 1.2
show hanagown normal:
    tworight
    ypos 1.15
with locationskip

# "Noticing a silence that had probably begun earlier, I look up from the dotted pages to see Lilly smiling as Hanako sips another cup of tea."
"พอรู้สึกตัวว่าเหมือนเงียบมาสักพักแล้วฉันจึงเงยหน้าขึ้นจากหน้าที่พิมพ์จุดเหล่านั้น ลิลลี่ยิ้มให้ฉัน ส่วนฮานาโกะกำลัง\nดื่มชาอีกถ้วยอยู่"

# hi "Is something wrong?"
hi "มีอะไรเหรอ"

show lilly basic_smile_paj
with charachange

# li "Quite the opposite, your curiosity's quite endearing."
li "ไม่หรอกจ้ะ แค่ว่าความอยากรู้ของเธอมันน่าเอ็นดูดี"

# "I am inordinately pleased by the praise, though I can feel my cheeks heating up a little."
"พอได้ยินอย่างนั้นแล้วก็รู้สึกดีแปลก ๆ แต่ก็รู้สึกเหมือนแก้มตัวเองแดงขึ้นมาหน่อย ๆ ด้วย"

# hi "Thanks, but I don't know how else I could act."
hi "ขอบใจ แต่คือฉันแค่ไม่รู้จะทำตัวยังไงดี"

show lilly basic_weaksmile_paj
with charachange

# li "To be honest, I wasn't altogether sure of how you saw us, since you were a new transfer student from another school."
li "ว่าตามตรง ฉันเองก็ไม่แน่ใจเหมือนกันว่าเธอมองพวกเรายังไง เพราะเธอเองก็เพิ่งย้ายมาใหม่"

stop music fadeout 12.0

show lilly basic_reminisce_paj
with charachange

# li "If you'd pitied us, I would have been quite offended."
li "ถ้าเธอมองว่าพวกเราน่าสงสาร ฉันคงไม่พอใจทีเดียว"

show hanagown distant
with charachange

# "There's a certain edge to Lilly's voice, one that I'd quite possibly place as pride. Glancing over to Hanako, she seems even more subdued than usual, looking towards Lilly rather than me."
"น้ำเสียงลิลลี่แฝงอารมณ์บางอย่างที่คงไม่น่าเกี่ยวกับศักดิ์ศรี พอเหลือบมองฮานาโกะก็เห็นว่าเธอดูผ่อนคลายกว่าทุกที\nสายตาไม่ได้มองมาที่ฉันแต่มองไปที่ลิลลี่"

# hi "I wouldn't worry about that. Considering the position I've found myself in, I'm perhaps the last person that should be dispensing pity on others."
hi "ฉันไม่คิดอะไรอย่างนั้นหรอก ดูสภาพแล้วฉันคงไม่มีหน้าไปสงสารใครคนอื่นหรอก"

# hi "My parents' first interactions with me after my heart attack… I wouldn't want anyone to see that kind of face."
hi "ท่าทีของพ่อแม่ตอนที่รู้เรื่องหัวใจของฉัน… ฉันไม่อยากให้ใครต้องเห็นหน้าแบบนั้นเลย"

show lilly basic_oops_paj
show hanagown distant_blush
with charachange

# "I catch myself from going any further, but not soon enough. Both of the girls seem to be put off, Lilly especially."
"ฉันยั้งตัวเองไว้ไม่ให้เล่าอะไรไปไกลกว่านี้อีก แต่เหมือนจะช้าไป เพราะเธอทั้งสองคนดูจะไม่สบายใจเท่าไหร่ โดยเฉพาะ\nลิลลี่"

show lilly basic_emb_paj
show hanagown worry
with charachange

# li "I'm… sorry. I shouldn't have gone that far…"
li "ขอ… โทษทีนะ ฉันไม่น่าพูดอย่างนั้นเลย…"

show lilly basic_listen_paj
with charachange

$ renpy.music.set_volume(0.5, 0.0, channel="sound")
play sound sfx_doorknock2

# "An awkward silence reigns for a few beats, thankfully ended as Lilly's head perks up in a gesture I've come to easily recognize."
"ความเงียบเข้าครอบงำอยู่ชั่วขณะ ซึ่งยังดีที่ไม่นานลิลลี่ก็เงยหน้าขึ้น เป็นท่าทางที่ฉันเห็นจนคุ้นตาแล้ว"

# hi "Hear something?"
hi "ได้ยินอะไรหรือเปล่า"

show lilly basic_surprised_paj
with charachange

# li "The door…"
li "ประตู…"

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_dooropen

show lilly basic_surprised_paj:
    left
    ypos 1.2
show hanagown distant_blush at Transform(xpos=0.4)
show bg school_dormlilly at bgleft
with charamove

# "Everyone looks towards it, trusting in Lilly's senses. True enough, the door handle shudders and turns, a flash of yellow and black slipping through."
"ทุกคนต่างหันมองไปทางประตูเพราะเชื่อในประสาทสัมผัสของลิลลี่ ซึ่งจริงอย่างที่ลิลลี่ว่า มือจับประตูกระตุกแล้วบิดลง\nเผยให้เห็นคู่สีเหลืองและดำที่โผล่มา"

show akira basic_laugh at right
with easeinright

play music music_running

show lilly basic_listen_paj
show hanagown worry
with vpunch

# aki "Akira Satou is in the house! Happy birthday, Hanako!"
aki "อากิระ ซาโต้ มาเยือนจ้า! สุขสันต์วันเกิดนะฮานาโกะ!"

show hanagown worry_blush
with charachange

# ha "Ah… thank you…"
ha "อ๊ะ… ขอบคุณ…"

show akira basic_smile at Transform(ypos=1.15, xpos=0.8, xanchor=0.5)
with dissolvecharamove

# "Akira takes a seat at the table as she plops her tall bag beside her. She has her trademark boisterous air about her, making no small deal of her entrance."
"อากิระลงนั่งที่โต๊ะแล้วโยนกระเป๋าลงวางข้าง ๆ บรรยากาศรอบตัวเธอนั้นมีความกระฉับกระเฉงเป็นเอกลักษณ์ ทำให้\nการปรากฏตัวของเธอดูอลังการ"

show hanagown distant
with charachange

# "Hanako clutches her gown to steady herself, but doesn't appear too shaken after she settles down. I guess she must have met Akira before, not a huge surprise given how close Akira and Lilly are."
"ฮานาโกะกำชุดนอนตัวเองตั้งสติ แต่พอดูสงบลงแล้วตัวก็ไม่สั่นเท่าไหร่ คงจะเคยเจอกับอากิระมาก่อนแล้วละนะ ซึ่งพอ\nเห็นอากิระกับลิลลี่สนิทกันขนาดนี้แล้วก็ไม่แปลกใจเท่าไหร่"

# "Akira doesn't seem to be the least bit put off by Hanako's scarring, despite its prominence, but she also doesn't pull any punches in how she acts despite Hanako's shy nature."
"อากิระดูจะไม่ได้เครียดอะไรที่เห็นฮานาโกะตกใจขนาดนั้น ยังคงทำตัวตามปกติไม่มีการเกร็งอะไร แม้ฮานาโกะจะเป็น\nคนขี้อายก็ตาม"

show lilly basic_weaksmile_paj
with charachange

# li "I thought you said you'd have to work, Akira. Did you manage to get off for a while?"
li "ไหนพี่บอกว่ามีงานไง หาเวลาว่างออกมาได้เหรอ"

show akira basic_boo:
    ypos 1.15
with charachange

# aki "Eh, kinda. I feel bad about ditching the guys doing overtime, so I gotta get back soon."
aki "อ่า ประมาณนั้น แต่ก็รู้สึกผิดที่ทิ้งพวกที่ทำล่วงเวลาไว้อย่างนั้น เดี๋ยวต้องกลับไปละ"

show akira basic_smile
with charachange

# aki "But I felt bad about not coming to your cute little Hanako's birthday too, so for now I'm here."
aki "แต่ถ้าไม่มางานวันเกิดฮานาโกะตัวน้อยสุดน่ารักของเธอฉันก็จะรู้สึกผิดเหมือนกัน พี่เลยแวบมาแป๊บหนึ่ง"

show hanagown smile
with charachange

# "She grins widely at Hanako, who flowers into a full blush as she pins her eyes downwards toward her lap. Her mouth seems to widen and retract over and over, as if she was trying to suppress a smile out of embarrassment."
"อากิระยิ้มแฉ่งให้ฮานาโกะที่นั่งจ้องตักตัวเองหน้าแดงแจ๋อยู่ ปากก็หุบ ๆ เกร็ง ๆ ราวกับกลั้นยิ้มไว้ด้วยความอายอยู่"

# "It's a little strange how her reaction seems to be more immediate and forceful than when she's embarrassed by the way she looks. All she manages to give in return is a tiny nod, failing to hide her appreciation to any great extent."
"แปลกเหมือนกันที่ท่าทีของฮานาโกะดูจะตรงไปตรงมา ทั้งที่เธอจะอายกับรูปลักษณ์ตัวเอง ฮานาโกะได้แต่พยักหน้า\nน้อย ๆ ตอบโดยที่ซ่อนความดีใจไว้แทบไม่มิดเลย"

# "Not that many people give her positive attention, I suppose. It makes me respect how well Akira can handle her, making her so happy, compared to what little I could do."
"คงไม่ค่อยมีใครที่ให้ความสนใจกับฮานาโกะในแง่บวกอย่างนี้มากละมั้ง เห็นแล้วก็นับถืออากิระเลยแฮะที่ทำให้ฮานาโกะ\nดีใจได้ขนาดนี้ อย่างฉันนี่เทียบแทบไม่ติดเลย"

show akira basic_laugh
with charachange

# aki "Now then, before I go…"
aki "เอาละ ก่อนไป…"

play sound sfx_rustling

# "She reaches into the bag beside her and grandly displays its contents."
"เธอเปิดกระเป๋าตัวเองที่อยู่ข้าง ๆ แล้วเอาของที่อยู่ข้างในออกมาให้ดูแบบเล่นใหญ่"

show wine:
    yalign 0.5 xanchor 0.0 xpos 1.0 alpha 0.0
    easein 1.0 alpha 1.0 xanchor 1.0
with Pause(1.0)

# "Out come two large glass bottles, both with long French names on the labels."
"ของที่ว่านั้นเป็นขวดแก้วใหญ่สองใบ แต่ละขวดมีชื่อภาษาฝรั่งเศสยาว ๆ พิมพ์ไว้บนฉลากอยู่"

show hanagown normal
with charachange

# "Hanako's expression is an odd mix of surprise and curiosity, and I suspect mine's no different. Lilly, not seeing the proceedings, is oblivious to what's going on."
"ฮานาโกะทำหน้าทั้งแปลกใจและสงสัย ฉันเองก็คงไม่ต่างกัน ส่วนลิลลี่ที่มองไม่เห็นนั้นยังไม่รู้ว่าเกิดอะไรขึ้น"

show hanagown normal_blush
with charachange

# ha "Akira… this isn't…"
ha "พี่อากิระ… อันนี้มัน…"

show lilly basic_surprised_paj
with charachange

# li "What is it?"
li "อะไรเหรอ"

# hi "Wine. One red, one white."
hi "ไวน์น่ะ ขวดนึงไวน์แดง อีกขวดไวน์ขาว"

show lilly basic_pout_paj
with charachange

# li "A-Akira! That's…!"
li "พะ พี่! แต่ว่า…!"

show akira basic_smile
with None

show wine:
    easeout 1.0 alpha 0.0 xanchor 0.0
with Pause(1.0)

hide wine
with None

# aki "Relax, relax, it's not like Shizune's here to scold you."
aki "ใจเย็น ๆ ใช่ว่าชิซูเนะจะตามมาเทศน์ถึงนี่ได้ที่ไหน"

# hi "Lilly has a point, that's not exactly allowed on campus."
hi "แต่ที่ลิลลี่พูดก็ถูกนะครับ จริง ๆ โรงเรียนเขาก็น่าจะห้ามของพวกนี้อยู่แล้ว"

# hi "…or anywhere, really. We're still short of the legal drinking age, remember?"
hi "…แต่เอาจริง ๆ จะที่ไหนก็ดื่มไม่ได้หรอกครับ พวกเรายังอายุไม่ถึงกันเลย"

show akira basic_laugh
with charachange

# aki "Rich words for someone practically drooling as he examines a bottle."
aki "ไอ้คนพูดน่ะเห็นขวดละน้ำลายสอเลยนะ"

# "She got me there. I am genuinely interested in trying some, even just a little. While Hanako may not be handling one herself, her look does tell me that she's far from opposed to the notion as well."
"ไปต่อไม่ถูกเลยทีนี้ เอาเข้าจริง ๆ ก็อยากลองแหละ สักนิดก็ยังดี และถึงฮานาโกะจะดูเหมือนไม่ได้อยากลองอย่างฉัน\nแต่ก็เหมือนจะไม่ขัดอะไรเหมือนกัน"

show lilly basic_displeased_paj
with charachange

# "Lilly rubs her forehead, giving up the fight that she knows Akira would win due to simply not caring enough about those funny “rules” and “regulations.”"
"ลิลลี่นวดหน้าผากเพราะรู้ว่าเถียงกับอากิระไปก็เปล่าประโยชน์ ยังไงอากิระก็ไม่สนคำพูดลอย ๆ อย่างคำว่า “กฎ” หรือ\n“ระเบียบ” อะไรพวกนั้นอยู่แล้ว"

show lilly basic_displeased_paj
with charachange

# li "Just don't breathe a word of this to anyone in the school, please. I beg of you."
li "พี่อย่าเอาเรื่องนี้ไปแพร่งพรายให้ใครในโรงเรียนรู้เลยนะ ขอร้องละ"

show akira basic_smile
with charachange

# aki "I'm not stupid, don't worry."
aki "ไม่ต้องห่วง พี่ไม่โง่ขนาดนั้น"

show akira basic_boo
with charachange

# aki "That said, I gotta get back to work pretty soon."
aki "แต่นั่นแหละ เดี๋ยวพี่ต้องกลับไปทำงานละ"

show lilly basic_oops_paj
with charachange

# li "So soon? But you only just arrived…"
li "จะไปแล้วเหรอ แต่พี่พึ่งมา…"

show akira basic_resigned
with charachange

# aki "Sorry, Lilly. Good to see you two again though, and you Hisao."
aki "ขอโทษทีนะลิลลี่ แต่ได้เห็นหน้าเธอสองคนอีกครั้งก็ดีแล้วละ นายด้วยฮิซาโอะ"

# hi "See you later, then."
hi "งั้นก็ไว้เจอกันครับ"

# ha "Um… g-goodbye… Akira…"
ha "เอ่อ ละ ลาก่อนนะ… พี่อากิระ…"

show akira basic_resigned at Transform(yalign=1.0)
with charamove

hide akira
with charaexit

# "She levers herself up with a grunt and waltzes out of the room, leaving us alone with the two items on the table."
"อากิระหยัดตัวลุกขึ้นยืนพร้อมเสียงโอดโอยแล้วเดินนวยนาดออกห้องไป ทิ้งให้เราสามคนอยู่กับไวน์สองขวดที่ตั้งอยู่\nบนโต๊ะ"

show lilly basic_oops_paj:
    twoleft
    ypos 1.2
show hanagown normal_blush:
    tworight
    ypos 1.15
show bg school_dormlilly at center
with charamove

# hi "…Interesting."
hi "…น่าสนใจ"

show lilly basic_arablush_paj
show hanagown normal
with charachange

# "Lilly gives a nervous giggle at her sister's antics as Hanako takes a wine bottle."
"ลิลลี่หัวเราะเจื่อน ๆ กับท่าทีของพี่สาวตัวเอง ส่วนฮานาโกะก็หยิบขวดไวน์ขึ้นมา"

show hanagown distant_blush
with charachange

# ha "So…"
ha "แล้ว…"

# hi "What do you think, Lilly?"
hi "เอาไงลิลลี่"

show lilly basic_weaksmile_paj
with charachange

# "She rests her elbow on the table and pinches the bridge of her nose, thinking things through. She really doesn't seem to be able to keep up with her sister."
"ลิลลี่นั่งเท้าศอกกับโต๊ะแล้วบีบสันจมูกตัวเองคิดอะไรให้ถี่ถ้วน ดูท่าว่าลิลลี่จะตามพี่สาวตัวเองไม่ทันเท่าไหร่"

show lilly basic_smile_paj
with charachange

stop music fadeout 3.0

# li "Well… it's already here. We may as well have some."
li "ก็… ขวดมันอยู่ตรงนี้แล้ว ดื่มสักหน่อยเลยก็ได้"

# "No sooner does she say it that I take a quick glance around the room for glasses."
"พอลิลลี่พูดอย่างนั้นแล้วฉันก็กวาดตามองรอบห้องหาแก้วทันที"

scene bg school_dormlilly_ni
with shorttimeskip

play music music_night fadein 0.5

# "A small groan above me reminds me that Lilly retired to rest on her bed for a bit a few minutes ago."
"เสียงโอดโอยที่ดังอยู่บนหัวทำให้ฉันระลึกได้ว่าสองสามนาทีก่อนลิลลี่หนีไปนอนบนเตียง"

# "Almost completely drained of energy, I manage to stand up and drag myself to the side of the bed, sitting down and leaning my back against it."
"ฉันลากสังขารตัวเองที่แรงแทบไม่เหลือแล้วลุกขึ้นเดินมานั่งพิงหลังอยู่กับเตียง"

show bg school_dormlilly_ni as ovl1:
    xalign 0.5 alpha 0.4 yalign 0.5 zoom 1.0
    ease 1.0 xalign 0.55 alpha 0.5 rotate 1 zoom 1.05
    ease 1.0 xalign 0.5 yalign 0.5 alpha 0.0 rotate 0 zoom 1.0

show bg school_dormlilly_ni as ovl2:
    xalign 0.5 alpha 0.4 yalign 0.5 zoom 1.0
    ease 1.0 xalign 0.45 alpha 0.5 rotate -1 zoom 1.05
    ease 1.0 xalign 0.5 yalign 0.5 alpha 0.0 rotate 0 zoom 1.0

# hi "Good God."
hi "โอ้"

show lilly basic_listen_paj_ni:
    center
    ypos 1.2
with charaenter

# li "Eugh…"
li "โอย…"

# "Lilly's groan sounds lifeless."
"เสียงครวญลิลลี่ฟังดูตายซาก"

# hi "Too much to drink?"
hi "ดื่มเยอะไปเหรอ"

show lilly basic_concerned_paj_ni
with charachange

# li "My head hurts."
li "ปวดหัว"

# hi "Yeah, too much to drink."
hi "อืม ดื่มเยอะไป"

# "I rest my head back and idly stare at the ceiling. What an unmitigated disaster."
"ฉันเอาหัวพิงกับเตียงแล้วเหม่อมองเพดาน สภาพตอนนี้เละไม่เหลือซากเลย"

# "Like proper idiots, we all drank the night away with one glass after another. Hanako simply fell to the side asleep, and it's a miracle I don't feel as ill as Lilly."
"เอาแต่นั่งดื่มกันทั้งคืน หมดก็เติมใหม่เรื่อย ๆ ทำกันอย่างกับคนสติไม่ดี ฮานาโกะล้มตัวลงหลับไปดาด ๆ ปาฏิหาริย์มาก\nที่ฉันไม่ได้เมาหนักเท่าลิลลี่"

show lilly basic_sad_paj_ni
with charachange

# li "Hey, Hisao? I'm sorry about today. I… didn't think this would happen."
li "นี่ ฮิซาโอะ ขอโทษเรื่องวันนี้ด้วยนะ ฉัน… ไม่คิดว่าเรื่องมันจะเป็นอย่างนี้"

# hi "It's fine, Lilly. To tell the truth, I had a lot of fun today."
hi "ไม่เป็นไรหรอกลิลลี่ ว่าตามตรงนะ สนุกมากด้วยซ้ำ"

show lilly basic_weaksmile_paj_ni
with charachange

# li "Really?"
li "จริงเหรอ"

# hi "Mmm. I think Hanako did too. No, she certainly did."
hi "อื้ม ฮานาโกะก็น่าจะสนุกเหมือนกันนะ ไม่สิ สนุกแน่ ๆ"

show lilly basic_reminisce_paj_ni
with charachange

# "There's a short silence, before another groan resounds from the supine Lilly."
"และเราก็เงียบกันไปครู่หนึ่ง ก่อนจะมีเสียงโอดโอยดังมาจากลิลลี่ที่นอนอยู่อีกรอบ"

# hi "You okay?"
hi "ไหวมั้ย"

show lilly basic_weaksmile_paj_ni
with charachange

# li "As you said, I just drank too much. What's the time?"
li "ดื่มมากไปอย่างที่เธอว่านั่นแหละ แล้วนี่กี่โมงแล้ว"

# hi "The time? Uh, it's…"
hi "กี่โมงแล้ว? เอ่อ ตอนนี้…"

# "I quickly look at my wristwatch, its numerals barely legible in the gloom."
"ฉันเหลือบมองนาฬิกาข้อมือ ห้องที่มืดทำให้แทบไม่เห็นตัวเลขเลย"

# hi "About midnight."
hi "สักเที่ยงคืนได้"

show lilly basic_concerned_paj_ni
with charachange

# li "Curfew's in effect, then."
li "งั้นก็เลยเวลาปิดประตูหอแล้ว"

# hi "Yeah, guessed as much. We'll all have to sleep here for tonight."
hi "อืม ก็นะ สงสัยคืนนี้ต้องค้างที่นี่กันก่อน"

# "As soon as I say it, I hear the sheets moving as Lilly starts to sit up."
"พอฉันพูดจบก็มีเสียงผ้าที่ขยับเมื่อลิลลี่เปลี่ยนท่ามาลุกขึ้นนั่ง"

show lilly basic_oops_paj_ni
with charachange

# li "Hanako…"
li "ฮานาโกะ…"

# hi "Ah, no, go back to sleep, don't try to get up."
hi "เดี๋ยว ไม่ ๆ นอนเถอะ อย่าฝืนลุกเลย"

show lilly basic_displeased_paj_ni
with charachange

# li "Hisao, I have to…"
li "ฮิซาโอะ ฉันต้อง…"

# hi "You're in worse shape than me by any stretch. Get some rest."
hi "ดูยังไงสภาพเธอก็หนักกว่าฉันอีก พักก่อนเถอะ"

show lilly basic_oops_paj_ni
with charachange

# li "But what about…"
li "ถ้างั้น แล้ว…"

# hi "I'll grab some spare blankets and put them over her, don't worry."
hi "เดี๋ยวฉันไปหาผ้าห่มมาห่มให้ฮานาโกะเอง ไม่ต้องห่วง"

hide lilly
with charaexit

# "As I give a deep yawn and stand to retrieve them, I hear her lie back down with a soft thud."
"พอฉันหาวหวอดใหญ่แล้วลุกขึ้นไปหยิบผ้าห่มก็มีเสียงลิลลี่เอนตัวลงกับที่นอนดังปุ"

# li "Thank you, Hisao."
li "ขอบคุณนะฮิซาโอะ"

# hi "No problem, it's the least I can do. You look outright wasted."
hi "ไม่เป็นไร เรื่องแค่นี้เอง สภาพตอนนี้เธอเมาไม่ไหวเลยนะ"

# li "I'm not… wasted… just a little bit… tired."
li "ไม่ได้… เมา… แค่… เหนื่อยนิดหน่อย"

# "She starts pouting, a slight slur beginning to distort her words as the alcohol takes hold of her again. I grab a couple of blankets rolled up at the end of her bed."
"ลิลลี่ทำแก้มป่อง คำพูดก็เริ่มฟังดูอ้อแอ้ด้วยฤทธิ์แอลกอฮอล์ที่เล่นงานเธออีกครั้ง ฉันคว้าผ้าห่มสองผืนที่ม้วนอยู่\nตรงปลายเตียงขึ้นมา"

# "Quietly walking over to Hanako, I carefully lay the blankets over her peacefully sleeping figure, making sure not to wake her up."
"ฉันเดินย่องไปหาฮานาโกะแล้วห่มผ้าห่มให้เธอที่กำลังนอนหลับสบายอย่างเบามือด้วยเกรงว่าจะทำให้เธอตื่น"

# "The thick smell of alcohol coming off her breath makes me doubt she'd wake up no matter what I did, though."
"แต่ดูจากกลิ่นฉุนแอลกอฮอล์จากลมหายใจที่พ่นออกมาแล้ว ให้ตายก็คงไม่ตื่นหรอกมั้ง"

# "I stand and take one last measure of the room."
"ฉันลุกขึ้นยืนแล้วมองไปรอบ ๆ ห้องอีกครั้งเป็นการปิดท้าย"

stop music fadeout 4.0

# "Two girls, both very drunk, and one guy sleeping overnight with them in the female students' dorm. What a scandal that'd be if it broke out."
"หญิงสองคนที่เมาหยำเปกับชายหนึ่งคนที่นอนค้างคืนด้วยกันอยู่ในหอหญิง ถ้าเรื่องนี้หลุดไปคนเอาไปลือกันให้แซ่ดแน่"

# "As I move to sit back down at the side of the bed, I steal one last glance at Lilly."
"ระหว่างที่เดินกลับมานั่งที่ข้างเตียงก็เหลือบมองลิลลี่อีกครั้งปิดท้าย"

# "Her sprawling, disheveled figure lies resting peacefully, slightly turned to the side."
"ลิลลี่นอนตะแคงนิด ๆ อ้าขาผมกระเซิงอยู่ดูหลับสบาย"

# "I crouch down to get a better look."
"ฉันย่อตัวลงดูใกล้ ๆ"

play music music_comfort

scene ev lilly_sleeping:
    truecenter zoom 1.05 subpixel True
    acdc_warp 20.0 zoom 1.0
with locationchange

# "Her white skin blends in with the white pillow of the bed, a look of slumber-born peacefulness on her face."
"ผิวขาวเธอกลืนไปกับหมอนสีขาวบนที่นอน ความสงบที่เกิดจากนิทราปรากฏบนใบหน้า"

# "Usually she seems so confident and forward, always there and caring for Hanako. Now, though, she seems painfully delicate."
"ปกติลิลลี่จะดูมั่นใจและมุ่งมั่น คอยดูแลอยู่เคียงข้างฮานาโกะเสมอ ทว่าตอนนี้ลิลลี่ดูเปราะบางเหลือทน"

# "I think back to Hanako's presents."
"ฉันย้อนนึกถึงของขวัญของฮานาโกะ"

# "I thought it'd be a nice occasion for her, but I'd hardly expected it to be so moving."
"ก็คิดไว้อยู่หรอกว่าคงเป็นโอกาสอันดีของฮานาโกะ แต่ไม่คิดเลยว่าเธอจะซาบซึ้งขนาดนี้"

# "One birthday after another, year after year."
"วันเกิดปีแล้วปีเล่า"

# "Just she and Lilly, all alone."
"ที่มีเธอและลิลลี่สองคนเพียงลำพัง"

# "…I guess it wasn't just the presents she liked."
"…ฮานาโกะคงไม่ได้ชอบแค่ของขวัญหรอก"

scene bg school_dormlilly_ni
with locationchange

# "Resigning myself to an uncomfortable sleep, I sit down at the side of the bed once again and rest my tired arms beside me."
"ฉันจำใจยอมนอนแบบไม่สบายตัวแล้วนั่งที่ข้างเตียงอีกครั้งก่อนจะห้อยแขนที่หมดแรงลงลู่ข้างตัว"

# li "Hey, Hisao."
li "นี่ ฮิซาโอะ"

# "Lilly's voice is so quiet I can barely hear it. She must be on the verge of sleep."
"เสียงลิลลี่นั้นเบามากจนฉันแทบไม่ได้ยิน คงใกล้หลับแล้วแน่ ๆ"

scene ev lilly_sleeping:
with locationchange

# hi "Yeah?"
hi "ว่า"

scene ev lilly_sleeping_smile
with charachange

# li "Thank you."
li "ขอบคุณนะ"

# hi "Thank you? For what?"
hi "ขอบคุณ? เรื่อง?"

# li "For being here."
li "ที่เธออยู่ตรงนี้"

# hi "…That's okay."
hi "…ไม่เป็นไร"

scene bg school_dormlilly_ni
with locationchange

# "As I hear a deep breath, it's obvious Lilly's gone to sleep."
"เสียงหายใจยาว ๆ ที่ตามมาเป็นสัญญาณบอกชัดว่าลิลลี่หลับไปแล้ว"

# "After closing my eyes, it doesn't take long for slumber to take me as well."
"ไม่นานพอหลับตาฉันเองก็เข้าสู่นิทราไปตามกัน"

stop music fadeout 2.0

window hide

scene black
with shuteye

#**************************************

label th_L5:

window hide None

scene black
with Pause(4.0)

stop music

window show

mystery "Hisao?"

mystery "Hisao, are you…?"

"The soft, barely audible voice lingering in my ears slowly wakes me. I wish I could be awoken like this more often."

"With a mumble, I slowly open my…"

scene bg school_dormlilly
show lilly superclose
with openeye_shock

show lilly superclose_shock
with Dissolve(0.2)

$ doublespeak(hi, li, "Whoa!", "Ah!")

play sound sfx_impact2

show lilly superclose_ouch
with vpunch

show lilly basic_concerned_paj:
    xalign 0.5 yanchor 1.0 ypos 1.2
    ease 0.4 ypos 1.4
with Dissolve(0.2)

"Taken by surprise at the face hovering curiously mere millimeters from mine, I make our heads collide with a harsh thud. The impact of our foreheads causes both of us to fall backwards and yelp in pain, Lilly sounding more like a squeak toy than a person."

hi "Ow, ow, ow."

play music music_happiness fadein 6.0

"I slowly rub my forehead with one hand, supporting myself with the other. Lilly lies a few feet ahead doing just the same, her face obviously pained."

hi "Ah… sorry. Your face was kinda close and I acted on reflex. You okay?"

show lilly basic_concerned_paj:
    ease 1.0 ypos 1.2
with Pause(0.5)

li "My head…"

"It seems she's not actually okay. Come to think of it, I doubt that the impact alone is what's causing her head so much pain."

hi "Hangover? You drank a fair bit, last night."

show lilly basic_sad_paj:
    ypos 1.2
with charachange

"She silently nods in confirmation as I lever myself up."

show lilly basic_concerned_paj:
    ease 1.0 ypos 1.0
with Pause(0.5)

"I offer a hand to her, and help her back onto her feet. Glancing behind her, I find that Hanako's still fast asleep."

show lilly basic_reminisce_paj at center
with charachange

li "It's not fair… I only drank as much as you did…"

hi "That's very different from what I remember. And anyway, girls have a lower tolerance than men."

show lilly basic_displeased_paj
with charachange

li "That doesn't help."

hi "Fine, I'll get you a glass of water. Just be careful not to trip over Hanako."

hide lilly
with charaexit

"I rub the sleep out of my eyes, or at least some of it, as I walk to the counter. Tending to someone with a hangover isn't the way I like to spend a morning."

"It only takes a few seconds for the glass to fill, the clear water reflecting the sliver of light that makes it through the thin curtains."

"It looks like Lilly's taken a seat on the side of the bed. I walk over to her while taking care to step over the peacefully sleeping Hanako, and place the glass into her outstretched hands."

show lilly basic_weaksmile_paj_close:
    center
    ypos 1.2
with charaenter

li "Thank you."

hi "No problem."

stop music fadeout 12.0

"I take a seat next to her, the soft bed having a surprising amount of give."

"She drinks slowly and methodically. A long silence passes with only Hanako's soft breathing to be heard."

show lilly basic_reminisce_paj_close
with charachange

"With some measure of guilt, I look at Lilly's face and attempt to read her expression. Her brow is furrowed, and she looks to be lost in thought."

show lilly basic_emb_paj_close
with charachange

"For a moment I hesitate, but eventually place a hand on her shoulder in an attempt to reassure her. I didn't expect her to flinch rather noticeably at that, though."

hi "Ah, sorry. I didn't mean to—"

show lilly basic_sad_paj_close
with charachange

"Lilly quickly shakes her head, in a manner somewhat more violent than usual for her."

"She takes a long breath to steady herself before letting her head sink."

show lilly basic_weaksmile_paj_close
with charachange

li "I must look terrible right now…"

"I move to protest, but quickly realize that it would be futile to do so. That said, I want her to open up more."

hi "If you want to talk about anything, I'm here."

show lilly basic_displeased_paj_close
with charachange

"Lilly gives a self-deprecating snort, as if to mock her own emotions."

show lilly basic_reminisce_paj_close
with charachange

li "There's just… a lot happening right now."

show lilly basic_sad_paj_close
with charachange

li "I'm sorry for being so strange recently, especially back when we were in town. Even now I'm a bit confused about everything."

hi "Believe me, I know how that feels."

show lilly basic_weaksmile_paj_close
with charachange

"She smiles wistfully, resting a cheek on the backs of her fingers."

li "We're a couple of broken young fools, aren't we?"

hi "Come on, don't say that. Come graduation, we'll be back out into the real world."

"The real world? Sometimes I surprise myself with the way I think about things. I guess the strange, divorced feeling of Yamaku and the surrounding town compared to the outside world still hasn't become natural."

"Maybe it never will. It's strange, in hindsight; being isolated from society like this doesn't feel as bad as it probably should. A wry grin on her face, Lilly seems to share the same sense of amusement at the idea."

"Eventually, though, her smile drops."

show lilly basic_displeased_paj_close
with charachange

li "I'll be going back to Scotland for a week or two, soon."

hi "Is that why we had to reschedule Hanako's birthday party?"

"She gives an affirmative nod."

hi "You'll be able to see your family again, at least. You're not looking forward to it?"

show lilly basic_concerned_paj_close
with charachange

li "I haven't met my family in six years. I don't even know how to act around them any more."

"Wait… what? My mouth hangs open as I try to process what she said."

play music music_moonlight fadein 6.0

"If she's eighteen, that means she'd have been only twelve when they left. I may have seen very little of my parents, what with them both working long hours, but that's…"

"I feel utterly useless as I struggle to find some way to respond."

hi "That's… but, why?"

show lilly basic_reminisce_paj_close
with charachange

li "Why did they leave, or why are they inviting Akira and me back?"

hi "Both, I suppose."

show lilly basic_sleepy_paj_close
with charachange

li "My father's business has its headquarters in Scotland, and an executive position became available for him there. In the end, he had to move permanently."

li "My mother followed him, but Akira and I stayed in Japan for the sake of both Akira's job within the Japanese branch of my father's company, and my education."

show lilly basic_concerned_paj_close
with charachange

li "As for the latter… one of my aunts is gravely sick."

hi "Ah. I'm… sorry."

show lilly basic_weaksmile_paj_close
with charachange

li "Don't be. It feels strange, really. We're being summoned there for her, yet we've barely met before. I can't even remember the sound of her voice."

"Equally strange is the total lack of antipathy she feels towards her family for doing such a thing. I can't help feeling slightly humbled."

"That said, her wistful exterior is just hiding her emotions. Seeing her like this is depressing."

stop music fadeout 5.0

"Knowing what to do, I lift myself off the bed. Lilly notices the bed's movements, her head perking up and her hand reaching sideways to feel where I was."

show lilly basic_oops_paj_close
with charachange

li "Hisao…?"

play sound sfx_rustling

"I walk over to my bag, still leaning against the wall. Unbuckling the front flap and retrieving the opaque bag from within, I take the small, plain box in my hands."

hi "Hold your hands out, Lilly."

show lilly basic_surprised_paj_close
with charachange

"She looks surprised for a moment, but eventually acquiesces."

show lilly basic_surprised_paj_close:
    ease 1.0 xpos 0.4
show bg school_dormlilly:
    center
    ease 1.0 xpos 0.4
with Pause (1.0)

show musicbox closed behind lilly:
    alpha 0.0  zoom 0.5  xanchor 0.0 xpos 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.6 alpha 1.0
show boxstrip behind lilly:
    alpha 0.0  zoom 0.5  xanchor 1.0 xpos 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.6 alpha 1.0
with Pause (1.0)

"I'm amused by her look of curiosity when I place the music box into her open palms, her typically delicate way of handling it making it seem as if it were fragile enough to break if breathed on."

stop music fadeout 2.0

"She wordlessly brings it in front of her face, her slender fingers feeling out its contours and patterning."

"Eventually her fingers find the recessed line between the lid and body of the box, and her thumb effortlessly pops open the lid."

show musicbox open:
    xpos 0.5 ypos 0.6 alpha 1.0
with charachange

play music music_musicbox

"I take a seat on the bed next to her, watching her face silently and intently."

"She sits completely motionless as she listens to the diminutive tinny melody, her mouth just slightly open."

show musicbox closed
show lilly basic_smileclosed_paj_close:
    xpos 0.4
with charachange

play sound sfx_switch
stop music

show musicbox closed:
    ease 1.0 ypos 0.7 alpha 0.0
show boxstrip:
    ease 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

show lilly basic_smileclosed_paj_close:
    ease 1.0 xpos 0.5
show bg school_dormlilly:
    ease 1.0 center
with Pause (1.0)

hide musicbox
hide boxstrip

"It takes a long while before she closes the lid with a small snap, bringing the curtain down on the miniature performance playing in her hands."

"The smile on her face, gentle and wistful, shows that I made the right decision."

hi "Think of it as a going away present for your trip to Scotland."

show lilly basic_smile_paj_close:
    xpos 0.5
with charachange

li "I will…"

play sound sfx_rustling

show lilly basic_smile_paj_close:
    twoleft
    ypos 1.2
show bg school_dormlilly at bgleft
with charamove

"A restless shuffling can be heard from the floor in front of us, the sound having woken Hanako."

show hanagown distant:
    tworight
    ypos 1.3
    easein 1.0 ypos 1.1
with Dissolve(1.0)

"She climbs out of the blankets I put over her, looking befuddled and wiping the sleep from her eyes."

hi "I see you're finally up."

show hanagown normal:
    ypos 1.1
with charachange

ha "Hmm? What?"

show lilly basic_planned_paj_close
with charachange

"Hanako looks around the room with her eyes only half open, her mind far from being as awake as her body. Her dazed state makes me and Lilly chuckle."

show lilly basic_planned_paj_close:
    ease 1.0 twoleft
with Pause(1.0)

show lilly basic_planned_paj at twoleft
with charadistant

"As Lilly gets off the bed and tends to Hanako, I take one last look around the room."

hi "I guess I'd better get going, then. There'll be questions if I am seen leaving the girls' dormitories in the morning."

show lilly basic_smile_paj
with charachange

li "Goodbye, Hisao."

show hanagown smile
with charachange

ha "Oh… goodbye."

"I stand and walk to the door, picking up my somewhat lighter bag along the way."

scene bg school_girlsdormhall
with locationchange

"After I leave the room and enter the hallway, though, I hear Lilly's footsteps behind me."

hi "Hmm? What's wrong?"

show lilly basic_smileclosed_paj_close:
    yalign 1.0 xpos 0.3 xanchor 0.5
    easein 1.0 xpos 0.5
with Dissolve(1.0)

"Without a word, she strides up to me. I freeze as I feel her hand slide onto my cheek, seemingly every nerve taking in the feeling of her fingers and palm upon it."

play music music_romance

"Immediately after, her face slowly moves next to mine, a light, momentary touch of her lips brushing against my other cheek."

"For a moment, everything seems to stand still. I absentmindedly bring my fingers to my cheek, as if to try and recapture that fleeting feeling."

hi "Lilly…"

show lilly basic_smile_paj_close at center
with charachange

li "That's my thank you, Hisao."

hi "Thank you…?"

show lilly basic_cheerful_paj_close
with charachange

li "For your present. Have a nice day in school."

show lilly basic_cheerful_paj_close:
    easeout 1.0 xpos 0.3 alpha 0.0
with Pause(1.0)

hide lilly
with None

"And with that, she disappears behind her door and gently closes it, the muffled voices of her and Hanako audible through it much as they were yesterday night."

"…"

"…I think I'd be hard pressed not to have a nice day, after that."

show bg school_courtyard
with locationskip

"I walk away with a certain spring to my step. I think there were some people around that glanced at me emerging from the girl's dormitory building, but I find it difficult to care."

stop music fadeout 2.0

scene black
with dissolve

#**************************************

label th_L6i:

scene black
with None

mi "Hicchan~."

hi "Go away."

mi "Hicchan~."

hi "Leave me alone."

mi "Come on, Hicchan~."

hi "Hmph, let me sleep."

"After two nights of not being able to sleep at all, the last thing I want is to be woken when I finally manage to."

"It may be the last period of class, with a textbook as my pillow, but I'll take whatever sleep I can get by this point."

mi "See Hicchan, even Shicchan wants you to get up~!"

"I don't care what Shizune wants, leave me alone."

mi "Geez, Hicchan, I'll just have to wake…"

"Wait, Misha's going to…?"

mi "…you…"

"This is bad!"

play music music_running

scene bg school_scienceroom
show misha hips_grin_close at center
with vpunch

hi "I'M UP!, I'M UP! YOU DON'T… have to…"

"I can feel my face flowering into a scarlet red blush."

"The students still in class are sitting bolt upright and staring at the shouting fool who was sleeping just moments before."

hi "…Dammit."

play sound sfx_impact2
with vpunch

"I let my head smack back down on the table with a noticeable thud."

show misha cross_laugh_close
with charachange

mi "Wahahahahaha~!"

"Misha's trademark uncontrolled laughter reverberates through the classroom."

show shizu invis behind misha:
    center
    xpos 0.95
with None

show misha hips_grin_close at twoleft
show shizu adjust_happy at tworight
show bg school_scienceroom at bgleft
with dissolvecharamove

"As I turn my mournful eyes to the bespectacled Shizune beside her, she carefully adjusts her glasses, desperately trying to maintain a look of serious disapproval."

"Narrowing my eyes, I can see the badly-hidden grin spreading across her face."

hi "Et tu, Shizune?"

show shizu behind_blank
with Dissolve(0.3)

"Shizune looks away quickly as she crosses her arms tightly, barely on the edge of her control."

show misha cross_laugh_close
with charachange

mi "Wahahahahahaha~!"

"Misha's laughter doubles in volume as she glances at Shizune. All I can do is drag my hand down my face in resignation."

hi "You two…"

show misha sign_smile_close
with charachange

mi "Who was the one who slept in class, Hicchan~?"

hi "Yeah, yeah, it was me."

show misha hips_frown_close
with charachange

mi "Poor Shicchan was having a fit trying to wake you up. Weren't you?"

show shizu basic_angry
with charachange

"I move my eyes back to the standoffish Shizune, who with a single huff of confirmation returns to looking away with her arms crossed."

hi "Why was Shizune trying to wake me up?"

show misha hips_smile_close
with charachange

mi "Shicchan wanted to give you the handouts the substitute teacher gave out while Hicchan was sleeping."

hi "Handouts?"

play sound sfx_paper
show shizu behind_frown_close
show misha hips_frown_close
show blanknote at truecenter
with vpunch

"I suddenly find two sheets of paper thrust down in front of my face."

show blanknote at Transform(xpos=0.3)
with charamove

"Following the hand holding them, I see the still-pouting figure looking down at me with a distinct scowl. I guess I really am in the wrong here."

hi "…Ah. Um, sorry about that."

stop music fadeout 8.0

"No dice. Her irritated face still holds. I clasp my hands together and flick my head downwards in apology."

hi "Very, very sorry."

show shizu behind_frustrated_close
with charachange

show blanknote:
    easeout 0.5 ypos 0.8 alpha 0.0
with Pause(0.5)

hide blanknote
with None

"She huffs and simply drops the papers on the desk."

hi "Damn."

show shizu adjust_angry_close
show misha sign_smile_close
with charachange

"I look up over my hands to see Shizune and Misha signing frantically to each other, a look of frustration on Shizune's face."

show shizu basic_angry_close
with charachange

shi "…!"

"It looks to be less of a dialogue and more of a tirade, punctuated with sidelong glances at me. To say it's unsettling is an understatement."

hi "Um…"

show shizu behind_frown_close
show misha hips_frown_close
with Dissolve(0.3)

"The two suddenly stop signing and look at me in unison, both having exactly the same look of disapproval. In one fluid motion, Misha's hand suddenly extends high above me and comes rocketing down."

scene black
with None

play sound sfx_impact2
play music music_running

"Before I can even hope to react, my head is sent bouncing up and down like a jack-in-the-box." with vpunch

"I quickly bring my hands to my head, more out of reflex than actual pain."

hi "Ow! What was that for!?"

scene bg school_scienceroom at bgleft
show shizu adjust_smug_close at tworight
show misha hips_grin_close at twoleft
with openeye

"I open my eyes to see the two grinning at each other while exchanging an enthusiastic thumbs-up."

show misha hips_smile_close
show shizu behind_smile_close
with charachange

mi "Shicchan says she forgives you now, Hicchan~!"

hi "Could you forgive me with a little less force next time?"

show misha cross_laugh_close
with charachange

mi "Wahahahaha~!"

"I look at the two with a blank face. Misha and Shizune: one, Hisao: nil."

show shizu adjust_happy_close
with charachange

shi "…"

show misha hips_grin_close
with charachange

mi "Oh, Shicchan also says that you should check your student mail more often~!"

show letter_insert:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

"She produces a bright yellow envelope and hands it over with an exuberant grin."

"Strange. Who could have written me a letter? Now is not the time and most definitely not the place to find out, though."

show letter_insert:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide letter_insert
with None

"Giving up on the nap so cruelly stolen from me, I rub my forehead and slowly get up, putting the sheets and envelope in my bag before swinging it over my shoulder."

show misha cross_laugh at Transform(yalign=1.0, xanchor=0.5, xpos=0.355)
show shizu behind_smile at Transform(yalign=1.0, xanchor=0.5, xpos=0.615)
with charadistant

"I take a step back and move to depart with a small bow, while Misha clutches her sides laughing and Shizune nods back in a curt farewell."

stop music fadeout 3.0
play ambient sfx_crowd_indoors fadein 0.5

scene bg school_hallway3
show crowd
with locationchange

"I join the flow of students exiting the open door, and turn the corner into the hallway."

$ renpy.music.set_volume(0.7, 0.5, channel="ambient")

show hanako emb_downtimid at center
with charaenter

"…only to end up face to face with Hanako."

hi "Whoa. Uh, hey Hanako."

show hanako emb_timid
with charachange

ha "Good afternoon… Hisao."

show hanako emb_downtimid
with charachange

"Silence falls between us as busily chatting students pass us by. She's fidgeting constantly, her eyes drawn to her rather unremarkable footwear."

"I take the bridge of my nose in my fingers while I blink my eyes heavily in an attempt to make things seem clearer. I'm barely staying awake as it is."

hi "Hanako, you want to say something. What is it?"

show hanako emb_blushing
with charachange

ha "U-um… I wanted to… give you this…"

hi "Hmm?"

show hanako basic_worry
with charachange

"She holds out a small rectangular piece of paper. I blink again to make out the text through barely open eyes, slowly starting to make out what's written."

window hide

$ written_note("\nEggs x2\nBread loaf x1\nWhole-grain cereal x1\nThyme x1\n")

window show

play music music_happiness fadein 0.5

hi "…A shopping list?"

"I look upwards, raising an eyebrow."

show hanako emb_timid
with charachange

ha "I usually go shopping with Lilly but I can't come, so…"

hi "You want me to run errands for you?"

show hanako defarms_shock
with charachange

ha "I-it's okay if you don't want to! I just thought that, maybe, um…"

"She's panicking. I sigh. Yet another battle lost, though this time by a weakly-fought surrender."

"I smile tiredly and rest a hand on her head to calm her down."

hi "It's fine, I was going to go anyway. Just the stuff on this list?"

show hanako def_worry
with charachange

"She nods then bows deeply, twice, as if to make her gratitude perfectly clear."

show hanako cover_distant
with charachange

ha "W-we were going to meet outside the school gates at six… thank you, I was going to get it, but I need to study for the test tomorrow."

hi "Test? Ah, that's right, science. How're you doing with it?"

show hanako cover_bashful
with charachange

"She brightens ever so slightly."

show hanako basic_bashful
with charachange

ha "I've been… spending more time on it than before. I think I can do… okay."

hi "Good work, then."

show hanako basic_smile
with charachange

"She too starts smiling, and much more earnestly than I at that."

"I have full confidence that I can do fine in it without any extra studying, but the fact that she's putting in the effort instead of just reading in the library is heartening."

hi "I'll grab your stuff and take it to your dorm in the evening. Seeya."

stop music fadeout 3.0
$ renpy.music.set_volume(1.0, 3.0, channel="ambient")

hide hanako
with charaexit

"With a small wave, we part ways."

"I'll go do my homework before meeting Lilly. I should be able to take care of it in time."

stop ambient fadeout 1.0

scene bg school_gate_ss
with shorttimeskip

play music music_soothing fadein 2.0

"Wrangling with a particularly complicated math problem has caused me to be a little bit late for my meeting with Lilly."

"Only a couple of minutes, but enough to make me step smartly out into the courtyard and to the school gate."

scene bg school_road_ss
with locationchange

"I make a right turn and start my way towards the small town below, leaving a few students turning the other way to the bus station."

"I slip my right hand into my pocket as I walk in the orange sunlight of dusk."

"Thankfully the sweltering summer heat's started to die down, making way for a pleasant cool breeze."

show lilly back_listen_ss at center
show lillyprop back_cane_ss at center
with charaenter

"When I stretch my hands high above my head, a familiar figure takes form, cane in her right hand."

hi "Ah, Lilly."

show lilly cane_listen_ss
hide lillyprop
with charachange

"She stops and turns around, swiveling her head slightly to try and work out exactly where the voice came from."

hi "Hey. It's me."

"I quickly catch up to her, coming in beside her and matching her slow pace as we resume walking."

show lilly cane_smile_ss
with charachange

li "Good afternoon, Hisao."

hi "Hi there."

scene bg misc_sky_ss at Fullpan(10.0, dir="right")
with locationchange

"I glance up at the sky."

"A distinct tinge of orange discolors the clouds, washing the footpath in its light. Long shadows from the trees fall across the wide road down the hill."

scene bg school_road_ss
show lilly cane_smileclosed_ss
with charachange

li "So, Hisao, what brings you here?"

hi "Just going to town to grab some groceries. Hanako sent me."

show lilly cane_surprised_ss
with charachange

li "Hanako sent you?"

hi "Yeah, said she needed to study for a test tomorrow. I was going to come down anyway, so I'll just buy her stuff as well."

"Unspoken is that Lilly really could use some help to get food, but it's an obvious fact that neither of us needs to state."

show lilly cane_weaksmile_ss
with charachange

li "It's good to hear she's studying for it."

hi "I thought the same thing when she asked me to come with you."

hide lilly
with charaexit

"We continue walking down the street, the familiar sound of her cane echoing through the air as we go. Except for the occasional passing car and the leaves whispering in the branches, there's a blissful silence."

"Thank God I can finally relax for the first time today."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene evbg lilly_sunsetwalk:
    truecenter subpixel True zoom 0.9
    acdc_warp 20.0 zoom 1.0
show evfg lilly_sunsetwalk:
    truecenter subpixel True zoom 0.85
    acdc_warp 20.0 zoom 1.0
with locationskip

"I glance over at Lilly."

"That porcelain face of hers never seems to lack that air of relaxed confidence. I guess the same could be said of her personality, too."

"As she silently walks, her face remaining pointed to the street ahead of her, I look ahead and savor the cool air blowing over my face."

"This is probably the calmest moment I've had since the about-face my life took so recently."

"To have it while walking to get some groceries. What a weird life."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

scene bg school_road_ss
with locationskip

"I feel the crumpled-up note rubbing against my hand in my pocket, and pull it out to check its contents."

hi "Let's see here… eggs, bread, cereal, thyme, lettuce, shaved ham…"

show lilly cane_weaksmile_ss
with charaenter

li "That sounds like quite a bit to carry back along with your own."

hi "Yeah. Just how much does this girl eat anyway?"

"My mind suddenly clicks that yes, there actually is a person beside me."

hi "W-wait, I mean…"

show lilly cane_giggle_ss
with charachange

"She laughs wholeheartedly."

show lilly cane_planned_ss
with charachange

li "My my, Hisao."

"Her giggles punctuate her words, though she's making little effort to suppress them."

show lilly cane_satisfied_ss
with charachange

li "Quite direct today, aren't we?"

hi "Yeah, you got me there. Still, it is quite a bit."

show lilly cane_smileclosed_ss
with charachange

li "Usually I go shopping with Hanako, so I know what she buys. It's the same thing every week."

hi "Huh. She a good cook?"

show lilly cane_weaksmile_ss
with charachange

"She gives a nervous giggle."

li "It's usually me who ends up cooking. I used to do so for Akira, so it's no problem doing it for Hanako as well."

hi "You can cook? But…"

show lilly cane_cheerful_ss
with charachange

"A short hum with an amused lilt emanates from beside me. I wonder if the fact that she seems amused by my comments so often is actually genuine, or rather just from a want to make me more comfortable in addressing her blindness?"

show lilly cane_smileclosed_ss
with charachange

li "There are ways around it. Some meals are more difficult to cook than others because of being unable to see what I'm doing, but it usually only takes a little more time. Fingers can double as very useful measurement tools, for example."

"It makes sense, but she'd have to be pretty careful not to hurt herself. I wonder how many times that's happened, given that it sounds like she's cooked alone for possibly years while Akira worked and her parents were gone."

"With that, the conversation trails off."

"Compared to the awkward silences of Hanako, Lilly seems genuinely content to say what she thinks and stay quiet when there's nothing to say."

"The slick road under my feet is bathed in an orange glow, the occasional fallen leaf crunching underfoot as we walk. I let out a deep yawn, my lack of sleep coming back to haunt me."

show lilly cane_smile_ss
with charachange

li "Did you not get much sleep last night?"

hi "I couldn't sleep at all for the last two nights. Probably insomnia."

stop music fadeout 8.0

show lilly cane_oops_ss
with charachange

"Lilly's face suddenly becomes worried. It feels like a personal failure every time she gets worried about my well-being, even if it's genuinely nice to know someone cares."

li "You have insomnia? Aren't you going to see the nurse about it?"

hi "Nah, no real need. It's happened before a few times. My meds screw with my sleeping occasionally."

show lilly cane_concerned_ss
with charachange

li "…Ah. I'm… sorry."

hi "Come on, it's not your fault. At least I shouldn't have any trouble getting to sleep tonight."

show lilly cane_sleepy_ss
with charachange

li "You do worry me sometimes."

hi "I… worry you?"

"I reach around and scratch the back of my neck. I kind of want to address this."

hi "Hey, Lilly…"

show lilly cane_smile_ss
with charachange

li "Hmm?"

hi "I don't mean to sound weird, but… please try to forget about my heart condition."

show lilly cane_oops_ss
with charachange

"She looks kind of lost. I hardly blame her."

hi "I guess what I'm trying to get at is… just don't treat me differently because of it."

show lilly cane_emb_ss
with charachange

"She bows her head slightly, her white cheeks reddening almost imperceptibly."

li "It's only natural to worry about those around you…"

hi "Well, it's still nice to know there's someone like that out there."

show lilly cane_smileclosed_ss
with charachange

"It may be somewhat embarrassing to say, but it's the truth. Lilly takes a breath to regain her composure and manages a gentle smile, though her cheeks remain flushed."

"The final downhill walk to the store passes in silence."

scene bg suburb_konbiniint
with shorttimeskip

play music music_daily fadein 4.0

"Storewoman" "Welcome!"

hi "I suppose I'll get my stuff first and Hanako's on the second round."

show lilly cane_smileclosed at center
with charaenter

"I grab two well-worn red baskets from the stack beside the entrance and pass one to Lilly."

show lilly cane_smileclosed at Transform(ypos=800)
with charamove

show lilly basic_smileclosed at Transform(ypos=800)
with charachange

show lilly basic_smileclosed at center
with charamove

"Just as she did before, she lays it on the ground and slides her retracted cane between the basket's handles before picking it back up with her right hand."

$ renpy.music.set_volume(0.5, 0.5, channel="music")

show lilly basic_smileclosed at Slide(0.5,0.5,0.3,0.5,1.0, time_warp=_ease_time_warp)
with None

show lilly basic_smileclosed_close at Slide(0.5,0.5,0.3,0.5,1.0, time_warp=_ease_time_warp)
with Dissolve(1.0)

"When she takes hold of my arm in her own, I'm surprised at just how fast this kind of casual contact became so natural. Mostly due to necessity, no doubt."

show lilly basic_smile_close at twoleft
with charachange

li "Shall we?"

$ renpy.music.set_volume(1.0, 2.0, channel="music")

hi "Sure."

"While we navigate around the store, the odd person occasionally passing us pays us no heed at all. It's nice, compared to the stares and whispers around the city."

show lilly basic_smileclosed_close
with charachange

"As we reach each aisle, I quickly check with Lilly what she needs and grab it along with what I want, putting our items into their respective baskets."

"It's an odd feeling, to be depended on so much for something so basic as shopping. Hanako would be practically a necessity for her to pick out what she wants, after all."

hi "Right, I'm pretty much done with both my stuff and Hanako's. You needing anything else, Lilly?"

show lilly basic_smile_close
with charachange

li "No, this should be everything."

hi "Off we go, then."

"Oddly, there's a queue a mile long. Considering the store's only large enough to warrant one counter, seems like it'll take a while."

hi "Damn."

show lilly basic_surprised_close
with charachange

"Lilly gives an inquisitive look, unable to see the reason for my complaint."

hi "The queue's really long. Looks like we'll have to wait."

show lilly basic_weaksmile_close
with charachange

li "How strange."

"Sharing the same mood of resignation, we reluctantly take our place at the end of the line."

$ renpy.music.set_volume(0.5, 10.0, channel="music")

"One person finishes, the line moves up. Another person finishes, the line moves up."

"By the time we finally reach the head of the line, I'm so close to dozing off that Lilly has to gently pat me on the back for me to move up."

show lilly basic_oops_close
with charachange

li "Hisao… Hisao!"

$ renpy.music.set_volume(1.0, 0.3, channel="music")

hi "Hmm? Ah, sorry."

show lilly basic_displeased_close
with charachange

"She gives a short sigh of consternation as I move up, getting the groceries for Hanako and me put into separate bags."

"Storewoman" "Thank you, please come again!"

stop music fadeout 5.0

scene bg suburb_konbiniext_ni
show lilly basic_smileclosed_ni
with locationskip

"By the time we emerge from the store, Lilly's holding a single bag while I struggle to carry four, both hands well and truly full. It's a lot of work, but thankfully the items in them are light."

"Even without looking skyward it's obvious that a surprising amount of time's passed, the road outside being dark and lit by streetlamps."

show lilly cane_smile_ni
with charachange

"Once Lilly retrieves her cane, we set out back to the dormitories the way we came, leaving the welcoming warm glow of the store."

scene bg school_road_ni
with locationskip

play music music_dreamy fadein 8.0

"Despite the road being empty of cars, the full bags abundantly make up for the lack of noise, constantly clunking and squeaking together."

show lilly cane_ara_ni
with charaenter

li "My my, Hisao, it's good to find that you're eating well."

hi "I'm a growing guy after all, I need to eat all I can!"

show lilly cane_weaksmile_ni
with charachange

li "Hmm… it must be nice, being a man."

hi "W-what?"

"Seemingly not noticing, or ignoring, my surprise at the completely out-of-left-field comment, she continues on without missing a beat."

show lilly cane_smile_ni
with charachange

li "Weight doesn't really bother you when eating, most of the time."

hi "I get what you mean. Women tend to worry about stuff like that more than we do, I guess."

show lilly cane_smileclosed_ni
with charachange

li "Exactly. It makes me somewhat envious, to be honest."

hi "Well, it's not like we can outright ignore it."

"With an affirmative nod, we continue on our walk."

hi "Huh, that's right."

show lilly cane_smile_ni
with charachange

li "What is it?"

hi "Hanako mentioned your birthday was earlier this year. Do anything special for it?"

show lilly cane_listen_ni
with charachange

"She gives a long pause, lost in thought for a few seconds as she recalls the event."

show lilly cane_weaksmile_ni
with charachange

li "Not really. It was just Hanako and me having a little party during the night after school."

hi "Your birthday's supposed to be a big event, you know."

"Sounds like a pretty lonely way to spend a birthday, just her and Hanako staying overnight."

"Birthdays always felt like a family occasion for me. They were a time when, in spite of their full-time jobs, both my parents would make an effort to be there for the day or at least for a party beforehand."

"It reminds me of how Lilly mentioned she hadn't seen her family in such a long time, and even ended up moving away from Akira's house afterwards."

"But I guess it's the same in situations as mundane as these. Considering her inability to read the packaging, just getting groceries would be a pain without somebody else around."

"In the end, she just has Hanako and me, and Akira when she's off from work."

"Be that as it may, she still seems to have many more distant friends among the students, not to mention people like Yuuko."

"It seems to be her own choice that there's such a separation between those who are close to her, and those who she only socializes with."

"It humbles me a little to see how much Lilly seems to have her life set up and going just as she wants."

"Yet Hanako is there for her to celebrate her birthday, and I'm here helping her with shopping. It's a weird kind of symbiosis, I suppose."

show lilly cane_oops_ni
with charachange

li "Are you all right, Hisao?"

hi "Sorry?"

li "You just seemed to go very quiet, that's all."

hi "Ah, sorry. I was just thinking."

show lilly cane_smileclosed_ni
with charachange

li "Oh?"

label th_choiceL6_1:
menu:
    with menueffect

    "Ah, now I've piqued her curiosity. It feels kind of overly personal to talk about though…"

    "Avoid the subject.":
        return m1

    "Tell the truth.":
        return m2

label th_L6a:
#Choice [1]

hi "I was just thinking about some of the stuff that's happened, don't worry."

stop music fadeout 2.0

show lilly cane_listen_close_ni
with characlose

li "Hmm?"

"She leans in even closer, forcing me to move sideways."

hi "Come on, don't you ever do that as well?"

show lilly cane_cheerful_close_ni
with charadistant

li "You make it sound as if you're hiding something…"

play music music_lilly fadein 4.0

"Erk. Why must this girl be so perceptive?"

"Glancing back at her face though, she wears a cute, playful smile."

"She's… playing with me? Even so, I'd rather not pursue this with her."

hi "I told you, it's nothing."

show lilly cane_displeased_close_ni
with charachange

"Lilly furrows her brow in disapproval."

li "Is that so?"

hi "Yes, it is."

show lilly cane_surprised_close_ni
with charachange

li "You're a very bad liar, Hisao."

hi "That's true, but that's why I'm not lying. I'm a very trustworthy person."

show lilly cane_weaksmile_close_ni
with charachange

li "I'm sure you are. I think I can forgive you just this once, though."

hi "Forgive? What for, exactly?"

show lilly cane_giggle_close_ni
with charachange

with Pause(0.2)

show lilly cane_smile_ni
with charadistant

"She giggles a little before resuming her quiet walking. Just what is she thinking now?"

stop music fadeout 4.0

"I look up to the dark sky as I slump my shoulders."

"I think this is something I have to sort out for myself, rather than relying on her for everything."

label th_L6b:
#[2]

hi "It was just kind of… I was thinking about how you seem to have everything so sorted out, even with Hanako relying on you. I can admit that even I kind of relied on you when I first transferred in."

hi "I think it's a good quality to have."

"I turn to Lilly, surveying her reaction."

stop music fadeout 2.0

show lilly cane_listen_close_ni
with characlose

"She's forcing herself to look forward and furrowing her brow quite a bit. Her face looks a bit awkward, as if she was trying to find just the right words."

hi "…Lilly?"

show lilly cane_weaksmile_close_ni
with charachange

li "I would thank you, but… assuming that I don't rely on the presence of others is too much. You'd be wrong to think that Hanako simply depends on me with nothing in return."

"She seems to have a bit of trouble saying it, even though it's largely what I'd thought already."

"If she's tried so hard to maintain her independence, as anyone would have had to in her position, sighted or not, maybe she finds it hard to talk about her own needs."

"It's only now that I realize an omission in what she says, though. I decide to follow it up, largely in jest, to avoid things getting too personal."

hi "Oh? And what about me?"

play music music_lilly fadein 2.0

show lilly cane_smile_ni
with charadistant

"She suddenly runs ahead of me and turns, blocking me off."

show lilly behind_cheerful_ni
with charachange

"With a smile, she holds her hands behind her as she leans forwards."

li "You're different."

show lilly back_giggle_ni
show lillyprop back_cane_ni
with charachange

"And with that, she turns back and continues to walk ahead of me, a newfound spring in her step."

"All I can do is raise an eyebrow and give a dazed grin. I don't think I've ever seen this playful and teasing side of her before."

"So… I'm “different”. It's hard to work out the exact context, but knowing her, this ambiguity was intended."

"Our relationship has been changing, at the very least simply because I've begun to stand on my own feet more and started getting more curious about the situation of those around me."

"As to why… probably a mix of personal curiosity, and a want to try and work out how to deal with my situation."

"I'm less sure of Lilly, though. That's why her own statement, so similar to my own feelings towards her, throws me off so much."

"Watching her make her way up the street, cane tapping from left to right, I decide to settle the matter later, and just smile. This is a nice side to her, and I don't want to forget it."

stop music fadeout 2.0

label th_L6c:
#End choice sections

scene bg school_girlsdormhall
with shorttimeskip

play music music_normal fadein 4.0

"Eventually we get to the girl's dormitories, both my arms aching from the weight of two sets of groceries."

hi "Hah… we're finally here. Phew."

show lilly invis:
    right
    xpos 0.95
with None

show lilly cane_smileclosed at right
with dissolvecharamove

"I bend down to wipe my forehead with the back of my hand. Lilly stops in front of her door and sets down her bag, fishing around in her pocket for the key."

show lilly cane_smile
with charachange

li "Thank you, Hisao. I really appreciate your help."

hi "Ah, this is nothing."

show lilly cane_smileclosed
with charachange

li "It might be nothing to you, but it's… definitely something for me."

show lilly invis:
    right
    xpos 1.05
with dissolvecharamove

play sound sfx_doorclose

hide lilly
with None

"And with that, she steps through her door, closing it behind her."

"I blink. Those were nothing but honest thanks, but I can't help feeling something different about them."

"Anyway, I have something else to do before I can mull on that at my leisure."

scene bg school_dormhanako_ni
show hanako emb_timid_close:
    center
    xpos 0.45
show hanako_door_base at right
show hanako_door_door at left
with locationchange

play sound sfx_doorknock2

"I turn back to the door to Hanako's room and proceed to knock twice in quick succession, the bags still in my hand rustling together."

play sound sfx_dooropen

show hanako_door_door:
   xpos -0.05
with charamove

"After a couple of seconds, the door slowly opens. If one weren't looking closely, they could be forgiven for thinking it hadn't moved at all."

"I twist my head to the side to try and peer through the tiny sliver of a gap between the door and the doorframe."

hi "Hey Hanako, I've got your stuff."

show hanako basic_normal_close at Position(xpos=0.4)
with charachange

ha "Ah!"

show hanako_door_door:
   xpos -0.3
show bg school_dormhanako
with dissolvecharamove

"With that, she opens the door completely, making her plain room visible over her shoulder. Sparsely decorated, it's probably even more unremarkable than my room."

"I hold out my right arm, both bags almost pulling it straight back down with their weight."

show hanako emb_smile_close
with charachange

ha "Th-thank you, Hisao."

show hanako emb_downtimid_close
with charachange

ha "I'm sorry to make you… carry them all this way."

hi "It's fine, don't worry. Just don't make me do it every day, okay?"

show hanako basic_normal_close
with charachange

"I pass the bags to her as I give a lighthearted chuckle. After the initial transfer of weight she manages to take them easily."

hi "I'll be off then. 'Night, Hanako."

show hanako cover_bashful_close
with charachange

ha "Good night. Um, s-see you in class… tomorrow…"

show hanako_door_door at left
with charamove

play sound sfx_doorclose

"With a deep bow, her groceries still held in both hands, she steps back and shuts the door."

stop music fadeout 5.0

scene bg school_dormext_full_ni
with locationskip

"Making my way back to my own dorm, I put one bag into my other hand to balance them out."

"Even as I do so, I can't get Lilly's lighthearted smile out of my mind. When I'd first met her, it would have been nearly impossible to imagine her like that."

"Indeed, it feels like we've become closer in the past few weeks since I first got to know both her and Hanako."

"The time that I spend with her each day. The small exchanges of happiness we share. Those small moments of joy as I get closer to her."

"I'm far from certain, but I don't think these are just the normal feelings of friendship."

scene bg school_dormhisao
with locationskip

"Once I return to my room, I store away my groceries and begin getting ready for the night."

show letter_insert:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

"I swap the school books in my bag for those I'll need tomorrow, pulling out the yellow envelope Misha gave me earlier in the process."

"I got so sidetracked by one thing after another that I couldn't deal with it earlier. Who could have written me, I wonder?"

"The name neatly adorning the back of the envelope freezes me in my tracks. It's been so long since I've seen her writing, there's little chance I could have identified it as hers otherwise."

"“Iwanako.”"

"Why… should she have written me? I can't think of any good reason for her to do this."

"I almost don't open the letter, but there'd be little point to that. If I just left it alone, its mere existence would gnaw at me until I did something about it."

scene ev hisao_letter_open
with shorttimeskip

play music music_rain fadein 6.0

"I look down at the piece of paper on my desk, its bright and summery decoration beaming happily at me."

"The lettering is in pink, jarring badly with the yellow sunflower border on the card. The handwriting is neat, the characters having been written thoughtfully and with an unusual amount of care."

"I'd barely given the letter a second thought when it was given to me, but now I can't get its contents out of my mind."

window hide
nvl clear
nvl show dissolve

n "\n\n\nWhile I'd like to say that I don't know why she used such an old-fashioned method of communication, considering a phone call or an email would be both much faster and easier, the answer feels obvious enough given the content."

n "A letter leaves a comfortable distance between the sender and the recipient. Unlike a phone, it isn't required that you engage in conversation, and unlike email, there is less expectation of an immediate reply."

n "\nStatements such as “the third-years seem to be very anxious about the final exams,” and “it's so weird to think we are already seniors, isn't it?” are just smalltalk. Smalltalk that could have been achieved by simply replying to any of the messages I'd sent her while in hospital."

n "The ending, though, is the true reason she sent this. The last couple of lines, added almost as an afterthought."

nvl clear
nvl hide dissolve

play sound sfx_paper

scene ev hisao_letter_open_2
with locationchange

nvl show dissolve

n "\n\n\n\n\n\n\n“I wonder if we will meet again. Perhaps it's for the best if we don't?”"

n "It's a statement that should hurt. I've always heard breakups are nasty stuff, but it feels like this is simply a reaffirmation of what we both already knew instead."

n "It's the preceding text, no more than smalltalk, that makes me feel most uneasy. I can't figure out why, no matter how long I sit here and look down at this bright and summery piece of paper."

nvl clear

n "\n\n\n\n\n\n\n\n“If you would like to correspond with me, by all means write me back.”"

n "It's plainly obvious that this is not the type of letter to be replied to. In the end, this letter is no more than a simple abdication of responsibility; a final statement to reassure herself that our relationship is over."

stop music fadeout 3.0

nvl hide dissolve
nvl clear

scene bg school_dormhisao
with locationchange

window show

"As such, I find I have little problem in scrunching the letter and envelope into a ball and tossing it into the wastebin, ridding myself of its existence."

"I go to bed with mixed feelings, cheated out of a pleasant evening by this intruder from the past."

"Ironically, it takes a while before I can manage to sleep."

scene black
with dissolve

$ suppress_window_after_timeskip = True

label th_L7:

window hide None

scene black
with dissolve

nvl show dissolve

n "\n\n\n\nI sweat profusely, awaiting the dreaded moment."
#For some reason, this line doesn't seem to be justified to the left like the others, and for the life of me I can't figure out why. Halp? -SC

$ renpy.music.set_volume(0.7, 0.0, channel="music")
play music music_tension fadein 6.0

n "Each tick of the clock tenses my muscles that much more, every minute making more hairs stand on end."

n "It's coming for me, I can feel it."

play sound sfx_slide

n "\n\n{image=vfx/reddash.png}{color=#FF0000}{b}Death.{/b}{/color}"

n "\n\nDeath in the form of a single sheet of paper."

$ renpy.music.set_volume(1.0, 0.5, channel="music")

nvl clear
nvl hide dissolve

scene bg school_scienceroom at bgright
with locationchange

window show

"I take the small pile of papers from the student in front of me and pass it backwards after plucking off the top piece."

"Looking to the top right of the page, I find my fears realized within that small red circle."

stop music
play sound sfx_thunder
with vpunch

"Forty-three."

"I hang my head and sigh in resignation. Cursing under my breath, I can feel the aura of a similar sentiment rising from the entire class. It's strange, but that fact lifts my mood by a minuscule amount."

"Misery loves company, I suppose."

"As the teacher opens her mouth, the room braces for the inevitable onslaught…"

play music music_normal fadein 1.0

play sound sfx_normalbell

"…only to be saved at the last minute."

"We quickly move to collect our bags and leave for lunch post-haste, but the teacher delivers a parting broadside."

"Teacher" "We'll be discussing the test scores next lesson. Needless to say, there will be quite some discussion to be had."

"A collective groan resounds from the class, now reduced to shuffling out dejectedly."

scene bg school_hallway3 at bgright
with locationchange

"I push the sheet into my bag as I walk along the hallway, crumpling it in the process. It's enough that such a troublesome letter ended up on my desk yesterday, and now this."

hi "I hate English…"

stop music fadeout 0.7

mystery "HI—{w=0.3}SA—{w=0.3}O!"

"A stern female voice gruffly calls out from behind me."

play music music_tension

"I freeze on the spot, my face becoming like stone. It's as if I can feel my brain disconnecting from my body."

"My eyes slowly shift right, trying to catch a glimpse of the disembodied voice."

stop music fadeout 0.3

"…nothing?"

"My face begins to slip as time passes, and I decide to risk turning my head. Ever so slowly, I twist it to the—"

play sound sfx_impact

hi "GYAAAAH!" with vpunch

"I jump into the air and drop my bag, yelling out in surprise."

"As I recover and regain my composure, I turn to see… I should have known."

hi "Emi."

play music music_running

show emi excited_proud at center
with charaenter

emi "Gotcha, Hisao."

"She stands there with a mischievous grin on her face, hands forward and fingers pointed inwards. She was the one who jabbed my ribs with her fingers."

"I look down at her with a grimace, rubbing my hair in frustration."

hi "That's no way to greet someone, you know."

show emi sad_pout
with charachange

emi "You have no sense of humor."

hi "I left my sense of humor in my English class. Complain to the teacher if you want it given back to me."

show emi sad_shy
with charachange

"She pulls her best puppy-dog eyes on me as she pouts. Lilly's managed to build up my resistance to the tactic, but Emi's short stature adds enough to the effect to make me relent."

hi "So, how are things? I haven't seen you around for a while."

show emi basic_closedgrin
with charachange

emi "Same old, same old. I run so fast, nobody wants to join me on my morning runs."

show emi basic_annoyed
with charachange

emi "It's a real pain."

"Her modesty never fails to amuse me."

show emi basic_grin
with charachange

emi "Although…"

"Uh oh."

show emi sad_shy
with charachange

emi "You know what I'm thinking, don't you Hisao?"

"Wearing my emotions on my sleeve is one of my worst habits. She's seen right through me."

"Fortunately, I see somebody else approaching us that will give me an out."

hi "Oh, hi Hanako."

show emi sad_shy at twoleft
show bg school_hallway3 at center
with charamove

show hanako emb_downtimid at tworight
with charaenter

"I give her a welcoming wave, and try my best at looking like I haven't noticed Emi's pouting face. She gives a small wave back."

show hanako emb_smile
with charachange

ha "H-hello, Hisao… Emi."

show emi basic_closedgrin
with charachange

emi "Hey Hanako."

hi "I'll join you and Lilly in a sec."

hi "Actually, speaking of lunchtime company, it's odd to see you without Rin, Emi."

show emi basic_shock
show hanako defarms_shock
with vpunch

emi "Ah! Rin!"

stop music fadeout 3.0

hide emi
with easeoutleft

"Without a second word, she forgets all about us and bolts off up the hallway. She must've forgotten she was waiting for her."

"Hanako and I stand speechless, only able to helplessly stand and watch this ball of seemingly boundless energy dash off."

play music music_running

show emi basic_closedgrin at left
with easeinleft

emi "Oh yeah, Hisao…"

"She suddenly stops herself just before vanishing around the corner to the rooftop staircase, spinning around to meet our bemused faces."

show emi excited_proud
with charachange

emi "I hate English too."

stop music fadeout 4.0

hide emi
with easeoutleft

"And with that, she disappears."

"All I can do is hang my head and give a long sigh, thoroughly left in the dust."

show hanako basic_smile
with charachange

"As I hear a short giggle coming from behind me, I turn to see Hanako smiling at the corner my attacker rounded."

play music music_daily fadein 4.0

show hanako basic_smile at center
show bg school_hallway3 at bgleft
with charamove

"I pick up my dropped bag from the floor and quickly dust it off."

hi "Afternoon. Been busy?"

show hanako def_worry
with charachange

ha "You don't… like English?"

hi "Hmm? Oh, uh, nah. I had a test on it a while back, and Emi caught me brooding about the results."

show hanako emb_downsad
with charachange

ha "Ah, sorry…"

"She averts her gaze, guilt written onto her face. A casual observer would think she'd just accidentally reminded me of a dead relative."

hi "Come on, it's not your fault. How're you doing in it?"

show hanako emb_sad
with charachange

"She looks up, though still avoids meeting my eyes."

show hanako basic_worry
with charachange

ha "All right, I… suppose."

"An awkward silence passes. They seem all too common around Hanako."

show hanako basic_bashful
with charachange

ha "Oh, Lilly asked if… you'd like to join us for lunch on the roof."

"I guess I don't exactly have any pressing engagements to attend to."

hi "Sure, I'll be right up."

show hanako cover_distant
with charachange

ha "Um, I'll… go get my lunch from the cafeteria now… then."

hi "Go on. You don't need my approval to leave, you know."

show hanako basic_smile
with charachange

ha "O-okay. I'll… be going then."

hide hanako
with charaexit

stop music fadeout 5.0

"She gives a skittish reply, a small nod and quickly makes off towards the cafeteria."

play ambient sfx_crowd_indoors fadein 2.0

show crowd:
    bgleft
    alpha 0.0
    parallel:
        ease 1.0 center
    parallel:
        linear 2.0 alpha 1.0
with None

show bg school_hallway3 at center
with dissolvecharamove

"I guess she must've forgotten to bring lunch today. As I walk through the hallways, more and more students start to come out of classrooms and pass me, going in the same direction as Hanako went."

"By the time I manage to make it to the stairs, I'm having to push my way past a busily chatting throng of students."

stop ambient fadeout 0.5

scene bg school_staircase1
with locationchange

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_rooftop

"I finally manage to get past the last of the crowd and round the staircase, slumping slightly in relief and slowing my pace before I open the door to the roof."

play sound sfx_door_creak
$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

scene bg school_roof
show white
with locationchange

hi "Ah, damn!"

"I momentarily avert my eyes, all but blinded by the harsh summer sun."

show white:
    alpha 1.0
    linear 10.0 alpha 0.0

show lilly basic_smile behind white:
    left
    ypos 1.2
show emi basic_grin behind white:
    center
    ypos 1.15
show rin basic_absent behind white:
    right
    ypos 1.17
with charaenter

mystery "Hmm?"

play music music_soothing fadein 8.0

"As I slowly regain my vision, the surroundings finally take form."

"Lilly, Emi and Rin sit together on the rooftop, the top of the hilltop forest around Yamaku visible past the fence around them, as if to frame the view."

show emi basic_closedgrin
with charachange

emi "Ah, Hisao!"

show lilly basic_smileclosed
show rin basic_deadpannormal
with charachange

"Lilly and Rin give a quick nod of acknowledgment and a deep nod of greeting respectively."
#Not the reverse, Suriko? -SC

"I start walking towards the rather mismatched trio, and can't help marveling at the speed with which Emi devours the rest of her half-eaten banana."

hi "Hey. Strange to see you three together like this."

show lilly basic_weaksmile
with charachange

li "It seems to have been quite the day of coincidences; Emi and Rin decided to eat on the roof just as Hanako and I decided to."

show emi basic_annoyed
with charachange

emi "You stole it! This spot was ours!"

hi "Simmer down, you can't steal a place in the school."

"I plonk myself down beside Lilly, the four of us creating a semicircle."

show rin basic_deadpanupset
with charachange

rin "I think she is right."

hi "You too?"

show rin basic_deadpan
with charachange

rin "The butterfly is her accomplice."

hi "The butter…"

"As I glance around, sure enough, a small yellow butterfly floats across my field of vision."

hi "So tell me, how did this butterfly help Lilly “steal” this spot?"

show rin basic_lucid
with charachange

rin "It scouted out our conversation and told her."

"I should've known better than to expect sound reasoning from Rin. Regardless, I guess it wouldn't hurt to play along."

hi "You're telling me she can talk to butterflies?"

show rin basic_awayabsent
with charachange

rin "There are people who can talk to horses, called horse whisperers."

show rin basic_deadpanamused
with charachange

rin "Lilly must be a butterfly whisperer."

"I bury my head in my hands as Emi rounds on her strange companion. She doesn't seem to share Rin's sense of humor."

show emi basic_confused
with charachange

emi "Whisperers don't work like that."

"Emi and Rin continue their banter as I turn to Lilly, who's busily finishing off her small box of curry and rice."

hi "So what brought you up here, anyway?"

show lilly basic_smile
with charachange

li "A little fresh air every now and again doesn't hurt."

show emi basic_shock
with charachange

emi "Ah!"

"Emi breaks off from her vain attempts to introduce the concept of logic to Rin."

show emi sad_annoyed
with charachange

emi "That was why we came up here too!"

"Something tells me it was her idea alone, and that Rin only got dragged up here on Emi's whim. Then again, the same could probably be said of Lilly and Hanako."

show lilly basic_weaksmile
with charachange

li "Now, now. We can share."

$ renpy.music.set_volume(0.001, 1.0, channel="music")

play sound sfx_door_creak


show lilly basic_surprised
show emi basic_hes
show rin basic_awayabsent
with charachange

"The creaking of the door to the roof can be heard as soon as she says the words. A moment of silence falls over us as everyone's attention focuses on the figure appearing from it."

show lilly basic_surprised:
    xanchor 0.5 xpos 0.4
show emi basic_hes:
    xpos 0.68
show rin basic_awayabsent:
    xpos 1.08
show bg school_roof at bgright
hide white
with charamove

show hanako basic_distant:
    xanchor 1.0 xpos 0.0 yalign 1.0
    easein 3.0 xanchor 0.0 xpos -0.06
    ease 1.0 ypos 1.17
with None

"Hanako slowly walks over to us, her eyes pinned to the ground, silently ruing the attention she's attracting. She tenses, just barely, when her eyes meet Rin's."

"I can't help raising an eyebrow as she walks over to us and sits next to me, doing her utmost to avoid looking up even as she brings her cafeteria bread to her mouth."

show rin basic_absent
show emi basic_grin
show hanako basic_normal:
    xanchor 0.0 xpos -0.06 ypos 1.17
with charachange

hi "So how do you and Emi know each other, anyways?"

$ renpy.music.set_volume(1.0, 8.0, channel="music")

show lilly basic_smileclosed
show rin basic_awayabsent
with charachange

li "Emi's somewhat well known around the school for her athletic ability. She's the fastest member of the track and field club by some margin, even beating Miki Miura at the track meet last week."

"Miki Miura… ah, that tanned girl from the front of my class. Considering her height and toned body, being able to beat her is quite an accomplishment."

show emi excited_amused
with charachange

"Looking over to Emi, it's very clear she's well aware of this fact as she beams proudly."

show emi excited_happy
with charachange

emi "So, Hisao. What was your score in English?"

"Ouch."

show rin basic_absent
with charachange

hi "No comment."

show emi basic_annoyed
show rin basic_awayabsent
with charachange

emi "Boo~."

"She puffs her cheeks and pouts, but it doesn't take long for her to bounce back."

show emi excited_proud
with charachange

emi "All right, if I tell you mine, you have to tell me yours. Deal?"

stop music fadeout 4.0

show rin basic_absent
with charachange

hi "Fine, fine."

show emi basic_closedhappy
show rin basic_awayabsent
with charachange

emi "Okay, on the count of three, we both say our results."

show emi excited_joy
with charachange

emi "One…{w=1.0} Two…{w=1.0} Three!{w=1.0}{nw}"

show emi basic_closedgrin
with charachange

$ doublespeak (hi, emi, "…", "Thirty-two!")

"I beam a mischievous grin."

play music music_comedy

show hanako cover_smile
show lilly basic_cheerful
show rin basic_amused
show emi excited_sad
with charachange
with vpunch
play sound sfx_impact

emi "Ah! Evil! Evil, evil, evil, evil!"

show rin basic_absent
with charachange

hi "You said it, not me. Still, the fact that you managed an even lower score than me is kind of amazing."

show emi sad_grit
show rin basic_awayabsent
with charachange

emi "Grr~!"

"She looks and sounds like a small terrier growling at an intruder. I can't say it's the most threatening sight I've seen."

show lilly basic_displeased
show hanako basic_normal
with charachange

li "Either way, scoring higher than thirty-two isn't something to boast about, much less scoring below it. For any subject."

show rin basic_absent
with charachange

hi "Yes, Lilly."

show rin basic_awayabsent
show emi sad_shy
with charachange

emi "Sorry, Lilly."

show lilly basic_smile
with charachange

li "I could help you with your English, if you'd like. It would be my pleasure to—"

show emi basic_closedgrin
with charachange

emi "No, no, that's fine. But I appreciate the thought. Really."

show lilly basic_reminisce
show hanako basic_smile
show rin basic_deadpanamused
with charachange

"Lilly looks slightly deflated, her hopes of imparting her knowledge dashed. Judging from the badly hidden laughter of the rest of us, neither she nor Emi seem to have garnered too much pity."

stop music fadeout 0.5
$ renpy.music.set_volume(0.0, 4.0, channel="ambient")

window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.7)

window show

"As I sit happily laughing though, I feel my voice suddenly cut off as my chest clenches."

window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.7)

window show

"I sit in silence for a few seconds, all my concentration forced on my heartbeat. It's only a small pain, but the ache feels like it's growing."

play music music_tragic fadein 0.5

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
with Dissolve (0.2)

window show

"Breathe deeply… breathe deeply…"

window hide

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

window show

"I glance upward to try and keep at least some of my attention on my surroundings, to see Emi suddenly freezing when she notices the expression of pain on my face out of the corner of her eye."

show emi basic_hes
with charachange

emi "Hey, Hisao… are you okay?"

show hanako def_worry
show lilly basic_surprised
show rin basic_deadpanupset
with charachange

hi "Yeah, I'm… fine…"

window hide

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

window show

"I look back down and redouble my efforts to try and stay calm, clenching my fists to try and dull the pain."

window hide

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

with Pause (0.7)

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

stop music fadeout 4.0

window show

"It takes a short time, but the pain, thankfully, begins to fade."

$ renpy.music.set_volume(0.5, 4.0, channel="ambient")

"When I look back up, there's only silence and pensive faces to be seen. I guess I'd better explain myself."

play music music_rain fadein 10.0

hi "Arrhythmia. I'm fine, it's… just a heart flutter."

show lilly basic_listen
with charachange

li "Are you sure? Should we get the nurse?"

show hanako def_worry:
    ypos 1.0
with ease

"Taking her cue, Hanako quickly picks herself up and begins to dash to the door."

hi "Hanako, stop. Lilly, I'm fine."

show rin basic_deadpan
with charachange

rin "You look like a wet, wrinkled tomato."

hi "Huh?"

"As I bring my hand to my forehead, I can feel the beads of sweat gathered on it and dab them off with my cuff."

hi "Thanks. I told you, I'm fine. I'm just kind of… fragile, I guess."

show hanako basic_worry
with charachange

show hanako basic_worry:
    ypos 1.17
with charamove

show emi sad_shy
show rin basic_deadpanupset
show lilly basic_sleepy
with charachange

"The entire atmosphere's changed from one of gaiety to downcast faces, the situation being too awkward for anyone to know exactly how to react."

"And of course, the whole thing is thanks to me. It just had to happen now, around others."

stop music fadeout 8.0

show lilly basic_weaksmile
with charachange

li "Oh, Emi?"

show emi basic_hes
show rin basic_awayabsent
with charachange

emi "Hmm?"

"She looks up, a box of juice halfway to her mouth."

show lilly basic_smileclosed
with charachange

li "I haven't told you of my score yet, have I?"

show emi basic_annoyed
with charachange

emi "Yeah, well. You're half-foreign, so your score doesn't count anyway."

"Lifting an eyebrow, I inquisitively turn to Lilly."

show rin basic_absent
with charachange

hi "What was your test result, anyway?"

show lilly basic_cheerful

"She gives a cheeky grin."

show rin basic_awayabsent
show lilly basic_planned
with charachange

li "One hundred percent. Perfect score."

play music music_lilly fadein 0.5

"No way. All I can do is hang my mouth open in wonder."

"Considering those tests are insane even for some native speakers, I can only imagine she's gone and done something like committing to mind part of the dictionary. A gift for rote memorization, maybe."

show rin basic_absent
with charachange

hi "That's…"

show rin basic_awayabsent
show emi sad_pout
with charachange

emi "See! Only someone part-foreign could get a score that good."

show rin basic_absent
with charachange

hi "“See”…"

show rin basic_awayabsent
show emi basic_closedsweat
with charachange

emi "Er…"

show lilly basic_giggle
show hanako basic_smile
with charachange

"Lilly and I grin at Emi's expense, her reaction identical to mine when I'd first tripped on that little landmine. Lilly's foreign ancestry does raise a point, though."

show rin basic_absent
with charachange

hi "Ah, that's right. You leave tomorrow for Scotland, don't you?"

show rin basic_awayabsent
show lilly basic_smile
with charachange

li "That's correct. Emi heard some rumors about it; it seems word's spreading quickly, considering I only told a friend in my class a couple of days ago."

show emi sad_grin
with charachange

emi "It must be so nice to go halfway around the world on a holiday."

show emi excited_happy
with charachange

emi "Hey, could you buy me something while you're there?"

show rin basic_absent
with charachange

hi "Don't be too shy now."

show lilly basic_giggle
with charachange

"Lilly gives a lighthearted giggle, evidently fully expecting Emi's bluntness."

"The rest of the lunch continues much the same as before, the jauntiness from before my heart flutter thankfully returning in full."

stop music fadeout 8.0

scene bg school_roof
show lilly basic_smileclosed:
    center
    ypos 1.2
with shorttimeskip

"As everyone files off with the appropriate farewells, only Lilly and I are left."

hi "Hey, Lilly?"

"She packs the last of her things into her bag and clips it shut, before perking her head up slightly."

show lilly basic_smile
with charachange

li "Hmm?"

hi "Um… thanks for breaking the silence back there. I kind of wanted to stop it, but didn't really know how to."

"As much as I'd like to sound less morose about it, the letter from yesterday, screwing up a test so badly in class, and now my heart make things very hard indeed."

show lilly basic_weaksmile
with charachange

"She gives an indulgent smile and nods. I hope she hasn't picked up on it, but knowing her, it's unlikely that she hasn't."

li "Emi's strong, but only human. We do worry about you, Hisao."

hi "Hold on, why would I worry you?"

$ renpy.music.set_volume(0.5, 2.0, channel="ambient")

show lilly basic_displeased
with charachange

"Her smiling face collapses, becoming uncomfortably serious."

li "Hisao, we are not ignorant of your situation."

li "Unli…"

show lilly basic_concerned
with charachange

"She suddenly cuts herself short, unsure of whether she should say what she intends to. I give a weak smile and rest my hand on her shoulder."

play music music_twinkle fadein 10.0

hi "Don't. It's enough that I worry about it. I don't want you all to shoulder my burden."

show lilly basic_oops
with charachange

li "But…"

hi "If you all worry about it, I have to worry about your worrying. If… that makes sense."

hi "I'm fine, okay?"

show lilly basic_reminisce
with charachange

"For a moment she looks to be lost in thought, carefully pondering how to react."

show lilly basic_weaksmile
with charachange

li "Hisao, do you have any paper left from your food's packaging?"

hi "I… think so? I'll just check."

play sound sfx_rustling

"I rummage around in my bag for the leftovers from lunch, eventually finding a paper square from my sandwich's package."

"My eyebrow raised and my expression rather quizzical, I gently place the square into Lilly's hand. Without another word, she brings her fingers around it to feel out its edges."

show lilly basic_smile
with charachange

li "This should be large enough…"

"With both of us seated on the roof, the minutes to the lesson ticking away, she proceeds to lay the item on the ground and begin her work in earnest."

show lilly basic_smileclosed
with charachange

"Wrapped in silence, I watch her fingers move about on the small square with amazing dexterity. A small fold here, a larger fold there, her fingertips keep a slow but sure pace."

"Looking up, her expression is calm and placid. The fact her face is pointed well above the sheet in front of her makes the sight of her work all the more curious."

"Her shoulders slump a bit after finishing one final fold, her work apparently done. It's only when she holds the item up in her hands that I realize what it is."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene white
with dissolve

with Pause(0.1)

scene ev lilly_crane:
    truecenter
    zoom 1.1 subpixel True
    ease 15.0 zoom 1.0
with Dissolve(4.0)

"A small origami crane."

"Light brown thanks to the packaging used, the result looks quite delicate and precise."

hi "You can do origami?"

li "I taught myself how to do it when I was younger. It improved my dexterity a bit."

hi "Huh…"

"A little baffled, I carefully take the small bird from her pale cupped hands as if it would break from the slightest breath. It seems to be folded quite well, and holds its shape easily."

$ renpy.music.set_volume(1.0, 2.0, channel="music")

scene bg school_roof
show lilly cane_smile at center
with locationskip

"We both grab our bags and head out the door, Lilly extending her cane as she does so."

stop ambient fadeout 2.0

scene bg school_hallway3
with locationskip

"I hold Lilly's handiwork up to my face for further inspection while we walk down the hallway, her hand running along the silver handrails for orientation."

"If she taught herself origami to improve her dexterity, with the use of her hands meaning so much to her given her condition… ah, so that's it."

"I smile as I realize the bird's meaning."

"“Everyone here has had to find their own ways of dealing with their conditions. You aren't alone here when you have problems.”"

hi "Thanks, Lilly. I appreciate this."

show lilly cane_cheerful
with charaenter

"She gives a sweet smile and a nod, not using words where none need be used, in her typical manner."

show lilly cane_smileclosed
with charachange

li "All I ask is that you take care of yourself, Hisao."

hi "Don't worry, I will."

show lilly cane_smile
with charachange

li "Promise?"

hi "Promise."

hide lilly
with charaexit

stop music fadeout 7.0

"And with that, we part ways."

"To be honest, I don't know what annoys me more - the fact that I could die at any moment, or the fact that everyone knows that."

"I guess I'll just take each day as it comes. As the unexpected present in my hand reminds me, I'm not alone here. Even though I may be like this, I'm not alone."

"If they worry, if anyone worries, I'll smile."

"I'll smile enough for all their worries to go away."

scene black
with dissolve

#**************************************

label th_L8:

scene black
with dissolve

play sound sfx_normalbell

scene bg school_scienceroom
show muto normal at center
with locationchange

"The moment the bell rings out, a collective sigh of relief comes from everyone."

play music music_happiness fadein 2.0

"Much of the morning's been taken up by a droning lecture on stoichiometry, a topic entirely unbefitting of the insufferable heat permeating the classroom."

hide muto
with charaexit

"Knowing that attempting to teach anything more would be an exercise in futility, Mutou gives up and begins clearing the teaching materials from his desk for the day."

$ renpy.music.set_volume(0.7, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 0.5

show hanako basic_normal at center
with charaenter

"As meaningless banter starts filling the classroom, I notice Hanako getting up and coming to my desk. She's been a lot less withdrawn lately, something which gives me a small measure of satisfaction."

show hanako basic_smile
with charachange

ha "Hello, Hisao."

hi "Hey. Want to go pick up Lilly, then? It's close to the time when she'd need to get going if she's going to make the flight."

show hanako cover_worry
with charachange

ha "Um… about that…"

show hanako basic_worry
with charachange

ha "She said she might be held up a bit by her classmates."

"I suppose that makes sense. Her class usually gets off a little earlier than ours, so Lilly would normally have just come to our classroom. Her class must be sending her off."

hi "Well, never mind. We can wait outside her classroom for once, right?"

show hanako emb_smile
with charachange

"She gives a small giggle before nodding, the two of us taking our things and leaving for 3-2's classroom."

stop ambient fadeout 1.0

scene bg school_hallway3
with locationchange

"When we reach our destination, I stop in idle amusement at the scene inside."

"One of the shorter girls from the class has Lilly wrapped in an enthusiastic hug, her head no higher than Lilly's chin. Her other friends, of which there are several, are gathered around her as well. Lilly simply smiles kindly and hugs her back."

"I guess Lilly must be pretty popular. Compared to Shizune's harsh but fair dictatorship of 3-3, Lilly seems more like a mother figure for 3-2, to say nothing of her height and looks."

"Kenji's pointedly cool demeanor as he packs up his things at his seat in the back corner of the classroom is expected. He's no doubt far from a fan of the fuss being made about Lilly's leaving."

"Looking beside me and seeing Hanako following my gaze, I decide to finally enter the room."

$ renpy.music.set_volume(0.7, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 0.5

scene bg school_room32
show crowd at center
show lilly basic_surprised at center
with locationchange

hi "'Afternoon, Lilly. It's just me and Hanako."

show lilly basic_surprised at twoleft
show crowd at bgleft
show bg school_room32 at bgleft
with dissolvecharamove

show hanako emb_downtimid at tworight
with charaenter

"Hanako withers noticeably when exposed to the din being made around Lilly. Try as she might, I doubt she'll ever completely get over her social anxiety."

show hanako emb_emb at tworight
with charaenter

ha "Hello…"

"Lilly manages to work out our position reasonably well, her classmate detaching herself without a second word. A look of slight exasperation is written on Lilly's face, though I can't say I blame her."

show lilly basic_smileclosed
with charachange

li "Hello Hisao, Hanako. Do we have much time before the flight leaves?"

"I give a quick glance at my watch. Taking the trip to the airport into account, there's a good ten, maybe fifteen minutes left while still allowing for contingencies."

hi "Yeah, we still have a few minutes to kill. I wouldn't worry about missing it yet."

"Classmate" "Ah, is this Hanako?"

"Uh oh. I think we've just inadvertently become entangled in Lilly's social web."

"The girl is probably part of the legally-blind faction of the class like Kenji, given her almost windowpane-like spectacles. Her short, roughly-cut hair gives her a look that fits her excitable expression."

show hanako def_shock
with charachange

ha "H-hello… um…"

"She takes Hanako's hand and pulls it up and down enthusiastically. I really don't get how girls can be so social to someone they only know as the friend of a friend."

"While Hanako exchanges nervous greetings, I look around the room for my short and overdressed next-door neighbor. Try as I might, he seems to have slipped out of the classroom without anyone noticing."

"For a moment I try to think of possible career paths that could reasonably benefit from his single skill, before putting my mind to more pertinent matters."

show lilly basic_smile
show hanako cover_distant
with charachange

"Lilly seems pleased, if somewhat guarded, about the enthusiasm Hanako's suddenly excited from those around her. She might not see it, but Hanako's much less panicked about the affair than I'd anticipated."

"Shuffling my way through the gaggle of classmates, I eventually manage to reach her."

hi "Don't worry, Hanako's fine."

show lilly basic_weaksmile
with charachange

li "Thank you. I thought she might be overwhelmed by them."

"Classmate" "Don't worry, we'll be gentle!"

show lilly basic_concerned
with charachange

"Both of us grimace in unison. Hanako's nervous grin stays plastered on her face as another couple of girls moves in to meet her."

"It's kind of amazing that even just a month ago she'd never have been able to cope with a situation such as this. Even when I first met her, the two of us completely alone, she sprinted from the library."

hi "So, got everything you need?"

show lilly basic_smile
with charachange

li "It's all packed. I just have to go by my room to pick it up on the way, and Hanako and I need to change."

hi "I guess we'd better get going, then. Hanako?"

show hanako cover_bashful
with charachange

"Hanako's head flicks up towards us in a flash, her face rather unmistakably appreciating the chance to extricate herself from the small group gathered around her."

show hanako basic_bashful
with charachange

stop music fadeout 2.0

ha "C-coming!"

stop ambient fadeout 0.5

scene bg hosp_ext
with shorttimeskip

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_rooftop fadein 1.0
play music music_tranquil fadein 3.0

"The long taxi ride to the airport is surprisingly pleasant, despite the three of us being rather squashed together to fit in the small back seat. On the other hand, maybe “despite” isn't the right word."

"Lilly pays the fare to the driver as we file out, Hanako's eyes flittering left and right. Thankfully there aren't too many people around, most of them being inside the main building rather than milling around outside."

show akira basic_boo at tworight
show hideaki bored:
    yalign 1.0 xanchor 0.5 xpos 0.9
with charaenter

"It isn't hard to spot Akira and Hideaki leaning against a fence while talking to pass the time. A large black travel bag, complete with wheels and travel handle, leans against the fence alongside them."

show hideaki surprise_up
with charachange

"Hideaki's the first to notice us, pointing us out to Akira who gives an overenthusiastic wave."

show akira basic_laugh
with charachange

aki "Hey! He~y!"

"I grab Lilly's travel bag for her as we go to meet the two, earning a nod of appreciation."

show akira basic_smile
show hideaki normal
with charachange

aki "I've got all my stuff here, you got yours? Plane ticket as well?"

show lilly basic_smileclosed_cas at twoleft
with charaenter

li "Don't worry, I have everything. You?"

show akira basic_laugh
with charachange

aki "Yep. All ready to go."

show hideaki evil
with charachange

hh "Not without some problems along the way, I might add."

play sound sfx_impact

show akira basic_kill
show hideaki ohshit
with vpunch

"The snide remark has his head roughly dragged around by a very firmly clamped-on hand."

show akira basic_boo
show hideaki sad
with charachange

aki "Haha yeah, I kinda sorta forgot it was in my trousers' pocket. Trousers that I'd put in the wash…"

show lilly basic_concerned_cas
with charachange

li "Oh no…"

show akira basic_laugh
with charachange

aki "Don't worry, don't worry. Did you know you can print out tickets if you order online nowadays? It's really cool."

show hideaki bored
with charachange

"Hideaki's pained expression says that this wasn't a solution found quickly. It could have been worse, I guess."

show lilly basic_weaksmile_cas
with charachange

li "We'd better start off then. Check-in should be ready by now."

show akira basic_lost
with charachange

stop music fadeout 2.0

aki "Yeah, you're right."

"There's a certain amount of wistfulness in both their voices. To say nothing of the people left behind, meeting their family again after all these years would be big for them."

show hanako emb_sad_cas at center
with charaenter

play music music_serene fadein 4.0

ha "Lilly…"

"Hanako wraps Lilly in a gentle hug to say goodbye, one which is warmly reciprocated. Lilly and I share a brief hug afterward, each of us saying our goodbyes."

"Beside us, Akira and Hideaki break off from a small hug and a word or two between them. It would probably look quite nice if not for the almost comical height difference between the two."

show lilly basic_smile_cas
show akira basic_smile
show hanako emb_downtimid_cas
show hideaki normal
with charachange

"Lilly takes ahold of her sister's arm once all that needs to be said in farewells is said, the two walking past the huge glass doors."

show lilly back_smileclosed_cas
with charachange

li "Goodbye Hisao, Hanako!"

show akira basic_laugh
with charachange

aki "Seeya! Don't do anything stupid, Shortie!"

hide lilly
hide akira
with charaexit

"We wave at them until they disappear from sight in the throng of people moving about inside."

"And then… we're alone."

hi "Well… that's that."

show hideaki bored
with charachange

"I turn to see Hideaki already beginning to walk off."

hi "Seeya."

show hideaki bored_up
with charachange

show hideaki invis:
    xpos 1.0
with dissolvecharamove

hide hideaki
with None

"He throws a hand into the air, in a manner I'd expect of Akira. In the end, it's just Hanako and me left standing outside."

show hanako emb_timid_cas
with charachange

"I rest my hand on her shoulder. She absentmindedly gazes towards the front doors of the building, as if she might catch a glimpse of either of the two before they disappear."

hi "Don't worry, the time'll pass fast."

show hanako basic_normal_cas
with charachange

"She hesitates for a moment, but eventually nods."

"With the scorching heat of the summer sun beaming down on us, we make our way to the nearby bus stop."

hide hanako
with charaexit

"It's strange, really. Just when I'd begun to see Lilly differently, she leaves on what almost feels like a pilgrimage to the past."

"In a way, though, that's just what I've been doing since coming to Yamaku."

"As much as I may reflect on everything that's happened to me, I really am hardly unique. Everyone has their own circumstances and separate paths to get where they are now."

"Yet I still can't really work out how I should proceed. My life may have practically been reset, and I still can't find anything that satisfactorily fills the hole I still feel in myself."

"Maybe Lilly's leaving will be a good thing for me. Without her to lean on, I'll need to do more for myself. I'll have to be there for Hanako as well."

"It feels strange to have so much changing so quickly after my months in that hospital that seemed to exist so separately from reality, but that's all the more reason for me to keep focused."

"I can't let any opportunity slip out of my fingers in my attempt to rebuild my life."

stop music fadeout 3.0
stop ambient fadeout 3.0

window hide

return