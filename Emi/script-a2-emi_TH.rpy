########################################################
label th_E3:

window hide None

scene black
with dissolve

$ renpy.music.set_volume(1.0,0.0, "ambient")
play sound sfx_alarmclock

window show

# "My alarm's beeping shatters the early morning quiet, and I find myself wondering where to find the motivation to rise."
"เสียงนาฬิกาปลุกดังทำลายความเงียบสงบของยามเช้าลง และฉันก็กำลังคิดอยู่ว่าจะหาแรงจูงใจ\nในการลุกขึ้นจากเตียงให้ได้จากที่ไหน"

window hide

scene bg school_dormhisao
with openeye

window show

# "Class is still quite far off, but I agreed to run with Emi in the mornings."
"ยังอีกนานกว่าจะถึงเวลาเรียน แต่ฉันก็สัญญากับเอมิไว้แล้วว่าจะไปวิ่งกับเธอในตอนเช้า"

# "Really, I'm not that interested in running as a hobby, or even as a possible life-lengthening exercise."
"ที่จริงแล้วฉันก็ไม่ได้สนใจการวิ่งนักหรอก ไม่ได้สนใจเป็นงานอดิเรกหรือกิจกรรมที่ทำเพื่อต่ออายุอะไรด้วยซ้ำ"

# "However, I feel obligated to follow through on my promise to Emi yesterday, which is why I find myself throwing on some running shorts and a light tee-shirt."
"แต่เพราะรู้สึกว่าต้องทำตามที่สัญญากับเอมิไว้เมื่อวาน ฉันจึงลุกขึ้นมาแต่งตัวลวก ๆ ด้วยกางเกงวิ่งขาสั้นหนึ่งตัวกับเสื้อยืดบาง ๆ"

scene bg school_courtyard
with locationskip

# "The cool morning air caresses my face as the morning sunshine causes the dew on the grass to sparkle, nearly blinding me at first."
"อากาศเย็นของยามเช้าไล้ผ่านใบหน้าไปในขณะที่ดวงอาทิตย์ฉายแสงลงมากระทบกับหยาดน้ำค้างบนใบหญ้า\nสะท้อนแสงระยิบระยับส่องมาเสียจนตาแทบพร่า"

# "As I make my way down to the track, an ugly thought strikes me."
"ขณะกำลังเดินไปลู่วิ่งฉันก็เริ่มคิดในแง่ร้ายขึ้นมา"

# "What if this is some sort of joke that Emi's playing on me?"
"ถ้าเกิดว่าเอมิแค่แกล้งอำกันเล่น และพอไปถึงแล้วกลับไม่มีใครรออยู่เลยล่ะ"

# "Would that surprise me, really?"
"ต่อให้เป็นอย่างนั้นจริงแล้วฉันจะยังรู้สึกประหลาดใจอยู่ไหมนะ"

# "Hell, I'd probably do it to the new guy, too."
"เหอะ เป็นฉันก็คงจะแกล้งรับน้องใหม่แบบนี้เหมือนกัน"

# "At the very least, I'm sure Emi and Rin made a bet on whether or not I'd actually show up."
"แต่อย่างน้อยฉันก็มั่นใจว่าเอมิกับรินพนันกันว่าฉันจะโผล่ไปจริง ๆ หรือเปล่า"

scene bg school_track
with locationchange

# "I feel a sense of trepidation as the track comes into view."
"พอสนามวิ่งปรากฏสู่สายตาก็ยิ่งรู้สึกกังวลใจ"

show emi basic_annoyed_gym at center
with charaenter

play music music_emi fadein 1.0

# emi "You're late!"
emi "นายมาสาย!"

# "It would seem that Emi is already there. What a relief."
"ดูเหมือนว่าเอมิจะมาถึงก่อนแล้ว ค่อยยังชั่ว"

# hi "Not according to my watch. We both are early, in fact."
hi "นาฬิกาข้อมือฉันขอคัดค้าน และที่จริงเราก็มาถึงก่อนเวลากันทั้งคู่นะ"

show emi basic_closedhappy_gym
with charachange

# emi "Damn. You've got me there."
emi "แย่จริง โดนจับได้ซะแล้ว"

# "Emi is sitting on the bleachers, decked out in her running gear, waiting somewhat patiently for me."
"เอมิกำลังนั่งรอฉันอย่างอดทนอยู่บนสแตนด์เชียร์ในสภาพเตรียมพร้อมอย่างเต็มที่"

# hi "I'm glad you're actually here. I was afraid that this was a joke or something."
hi "ฉันดีใจนะที่เธอโผล่มาจริง ๆ น่ะ กลัวว่าจะแกล้งอำกันเล่นแล้วซะอีก"

show emi basic_grin_gym
with charachange

# emi "Nah, I'd never make someone get up early for nothing."
emi "ไม่ละ ฉันไม่มีทางบอกให้ใครตื่นแต่เช้ามาโดยไม่มีเหตุผลหรอก"

show emi excited_proud_gym
with charachange

# emi "Plus, Rin owes me 500 yen now. She didn't think you'd actually show up."
emi "แล้วอีกอย่าง ตอนนี้รินติดเงินฉันอยู่ 500 เยนแล้วเพราะรินคิดว่านายจะไม่มา"

# "I knew it!"
"ว่าแล้วเชียว!"

# "Nice to know Emi was on my side, at least."
"อย่างน้อยก็ยังดีที่ได้รู้ว่าเอมิเชื่อว่าฉันจะมา"

show emi gymbounce_once
with Dissolve(0.1)

# "Emi hops off of the bleachers and begins stretching out."
"เอมิกระโดดลงมาจากสแตนด์เชียร์แล้วเริ่มยืดเส้นยืดสาย"

play sound sfx_gymbounce

show emi gymbounce
with Dissolve(0.05)

# "She's remarkably lithe, almost like a dancer."
"พอเห็นอย่างนั้นแล้วถึงได้รู้สึกว่าตัวเธออ่อนมากเสียจนเหมือนกับเป็นนักเต้น"

# "I set out to stretch as well, but then realize that I don't exactly remember how to stretch properly."
"ฉันตั้งท่าจะทำตามบ้าง แต่ก็จำท่ายืดเส้นยืดสายแบบถูกวิธีไม่ค่อยได้แล้ว"

# "It's been ages since I stretched for anything, if you don't count my one stint at running last week."
"คงเพราะไม่ได้ออกกำลังกายมานานแล้วก็เลยไม่คิดว่าจำเป็นต้องทำ ถ้าไม่นับตอนเมื่อสัปดาห์ก่อนน่ะนะ"

# "And even then, I don't think I actually stretched beforehand."
"แต่ตอนนั้นเองก็ไม่คิดว่าตัวเองได้ยืดเหยียดอะไรก่อนออกวิ่งเหมือนกัน"

# "The specter of my long hospital stay rises up again."
"เจ้ากรรมนายเวรจากช่วงที่อยู่ในโรงพยาบาลเริ่มตามทันแล้วสิ"

# "I can't say I was all that active before the hospital stay, though, so maybe I'm just being morose."
"จะบอกว่าตัวเองเป็นพวกชอบเคลื่อนไหวร่างกายตั้งแต่ก่อนจะถูกหามเข้าโรงพยาบาลก็คงไม่ได้เหมือนกัน\nตอนนี้ฉันอาจจะแค่อารมณ์เสียเฉย ๆ แหละ"

show emi basic_closedgrin_gym at center
with charachange

# "Emi giggles as she watches me stretch out."
"เอมิมองดูฉันที่กำลังยืดเส้นยืดสายอยู่แล้วหัวเราะคิกคัก"

show emi basic_grin_gym
with charachange

# emi "No no no Hisao, you've got to hold it for longer than that!"
emi "ไม่ใช่แบบนั้นสิฮิซาโอะ นายต้องค้างท่านั้นไว้นานกว่านี้นะ!"

# hi "I'm trying! It kinda hurts a little."
hi "พยายามอยู่! ชักเจ็บแล้วแฮะ"

show emi excited_proud_gym
with charachange

# emi "Ha! That's because you're out of shape. You've got to get some flexibility in you, like this."
emi "ฮ่า! ก็เพราะว่านายไม่ชอบออกกำลังกายไง ต้องทำให้ร่างกายตัวเองยืดหยุ่นขึ้นกว่านี้นะ แบบนี้"

hide emi
with charamoveoutbottom

# "To demonstrate, Emi reaches down and puts her head through her legs."
"เอมิก้มลงไปแล้วเอาหัวลอดหว่างขาตัวเองให้ดูเป็นตัวอย่าง"

# "God bless you, Emi."
"คุณพระช่วยเธอเถอะเอมิ"

# hi "I see. Is that the sort of thing I should strive for?"
hi "อะไรแบบนั้นคือเป้าหมายที่ฉันควรจะบรรลุให้ได้เหรอ"

show emi basic_closedgrin_gym
with charamoveinbottom

# emi "Of course! Flexibility is important for any runner. You'll be able to go faster the more you stretch out."
emi "แหงสิ! ความยืดหยุ่นของร่างกายน่ะสำคัญต่อการเป็นนักวิ่งมากนะ เพราะยิ่งร่างกายยืดหยุ่นมากเท่าไหร่\nก็ยิ่งวิ่งได้เร็วมากขึ้นเท่านั้น"

# "That makes no sense to me, but Emi seems to believe it's true."
"ไม่เห็นจะสมเหตุสมผลตรงไหน แต่เอมิดูจะเชื่อความคิดนั้นเอามาก ๆ"

# "With Emi's help, I manage to stretch myself out properly."
"หลังจากนั้นฉันก็ยืดเส้นยืดสายได้อย่างถูกต้องจนสำเร็จด้วยความช่วยเหลือจากเอมิ"

show emi basic_grin_gym
with charachange

# "I can't help but notice that when she thinks about how to explain things to me, her mouth scrunches up in concentration."
"ฉันอดไม่ได้ที่จะสังเกตเห็นว่าเอมิชอบเม้มปากขึ้นเวลาคิดว่าจะอธิบายอะไรให้ฉันเข้าใจยังไงดี"

# "It's adorable."
"ซึ่งน่ารักดี"

show emi excited_proud_gym
with charachange

# emi "Not bad, Hisao. Come on, we'd better start running."
emi "ไม่เลวเลยนี่ฮิซาโอะ งั้นเดี๋ยวเรามาเริ่มวิ่งกันเลยดีกว่า"

show emi excited_happy_gym
with charachange

# emi "We'll start off with just a mile, okay?"
emi "เริ่มด้วยระยะทางสักพันหกร้อยเมตรก่อนเป็นไง"

show emi basic_happy_gym
with charachange

# emi "That's four laps around the track, got it?"
emi "หรือก็คือประมาณสี่รอบลู่วิ่ง ไหวมั้ย"

# hi "That sounds fine to me."
hi "ไหว"

show emi basic_happy_gym:
    center
    easeout 0.5 xpos 0.4 alpha 0.0
with None

stop music fadeout 2.0

# "This shouldn't be too hard, right?"
"คงจะไม่ยากเกินไปหรอกใช่มั้ยนะ"

scene bg school_track_on
with locationchange

# "A hazy memory of running a mile for gym class surfaces in my mind."
"ฉันนึกย้อนกลับไปถึงประสบการณ์ที่แสนเลือนรางของการวิ่งสี่รอบลู่วิ่งในคาบพละศึกษาจากในอดีต"

# "Yeah, it wasn't that bad."
"อืม ก็ไม่ได้แย่ขนาดนั้น"

play music music_running fadein 0.5

scene bg school_track_running
with Dissolve(2.0)

$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

play ambient sfx_emijogging fadein 1.0

# "Emi sets a pretty good pace, and I fall in behind her."
"เอมิรักษาเพซการวิ่งได้ดีพอสมควร ส่วนฉันก็ตามหลังเธออยู่"

$ renpy.music.set_volume(1.0, 0.5, channel="ambient")

show emi basic_grin_gym at left
with charamoveinleft

# emi "Try to keep up, okay Hisao?"
emi "คอยตามให้ทันนะ โอเคมั้ยฮิซาโอะ"

# hi "Roger."
hi "รับทราบ"

$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

hide emi
with charamoveoutleft

# "We round the first curve without incident, though I can already feel my heart rate increasing slightly."
"โค้งแรกผ่านไปได้ด้วยดี แม้ฉันจะเริ่มรู้สึกได้แล้วว่าหัวใจของตัวเองค่อย ๆ เต้นเร็วขึ้น"

# "By the second curve, I've started to breathe through my mouth."
"เมื่อถึงโค้งที่สอง ฉันก็เริ่มหอบหายใจทางปาก"

# "Emi doesn't even seem to be breaking a sweat."
"ส่วนเอมินั้นแม้แต่เหงื่อสักหยดก็ยังไม่เห็น"

# "As if to punctuate her superiority, she turns around and starts running backwards."
"เธอหันกลับมาแล้วเริ่มวิ่งถอยหลังราวกับจะแสดงให้เห็นถึงความเหนือกว่าของตัวเอง"

$ renpy.music.set_volume(1.0, 0.5, channel="ambient")

show emi basic_closedgrin_gym at center
with charaenter

# emi "Are you doing okay, Hisao?"
emi "ไหวรึเปล่าเนี่ยฮิซาโอะ"

# hi "Never… better."
hi "ซำ… บาย…"

show emi excited_proud_gym
with charachange

# emi "Oh really? Maybe I should speed up then, hmm?"
emi "จริงเหรอ งั้นฉันก็ต้องเร่งฝีเท้าขึ้นสินะ หืม"

# hi "Oh… no, …wouldn't want you…"
hi "อย่า… เลย… ไม่อยากให้เธอ…"

# hi "…to… overex…ert yourself."
hit "…ฝืน… ตัวเอง… เกินไป"

# "My heavy panting and wheezing makes the statement less convincing than I had hoped. Emi simply smiles and turns around again."
"เสียงหอบหายอันใจหนักหน่วงและแหลมสูงทำให้คำพูดของฉันฟังดูไม่น่าเชื่อถือเท่าที่หวังไว้ แต่เอมิก็แค่ส่งยิ้มให้\nแล้วหันกลับไปตามเดิม"

show emi excited_proud_gym at left
with charamove

# emi "You're the boss, Hisao. We'll stay at this pace."
emi "นายว่ายังไงก็อย่างนั้นเลย ฮิซาโอะ งั้นเราจะคงความเร็วไว้เท่านี้นะ"

$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

hide emi
with easeoutleft

# "I get the feeling that I'm being mocked."
"เหมือนโดนล้ออยู่ชอบกล"

# "If I weren't in such terrible shape, I'd probably feel offended."
"ถ้าไม่ได้อยู่ในสภาพที่ดูไม่ได้อย่างนี้ก็คงโมโหไปแล้ว"

# "By the third lap, my breath is coming in ragged gasps."
"พอถึงรอบที่สามจังหวะการหอบหายใจของฉันก็ยิ่งเพี้ยนไปใหญ่"

# "I'm also awash in my own sweat. Gross."
"แถมยังเหงื่อโชกจนรู้สึกตัวเหนียวเหนอะหนะ"

# "We round the curve to start our fourth lap, and Emi looks back at me with a grin."
"พอเราวิ่งเข้าโค้งสุดท้ายเพื่อเริ่มรอบที่สี่ เอมิก็มองกลับมาหาฉันพร้อมยิ้มกว้าง"

$ renpy.music.set_volume(1.0, 0.5, channel="ambient")

show emi basic_closedgrin_gym at left
with charamoveinleft

# emi "Here we go!"
emi "ไปกันเลย!"

play ambient sfx_emisprinting

hide emi
with easeoutleft

$ renpy.music.set_volume(0.3, 0.5, channel="ambient")

# "She takes off at blinding speed while I stubbornly stick to my slower pace."
"เธอพุ่งทะยานออกไปด้วยความเร็วราวกับติดจรวดในขณะที่ฉันยังคงความเร็วไว้เท่าเดิม"

# "By the time I get to the first turn, she's already rounding the second."
"ตอนที่ฉันเพิ่งไปถึงโค้งแรก เอมิก็วิ่งเข้าโค้งที่สองไปแล้ว"

# "As I struggle across the back stretch, Emi continues running and catches up to me."
"ตอนที่ฉันกำลังพยายามพาตัวเองไปให้พ้นจากลู่ส่วนที่อยู่อีกฟากกับเส้นชัยนั้นเอมิก็ตามมา"

play ambient sfx_emijogging

$ renpy.music.set_volume(1.0, 0.5, channel="ambient")

show emi excited_proud_gym
with charamoveinright

# emi "Come on, Hisao! You can do it!"
emi "สู้ ๆ นะฮิซาโอะ! นายทำได้!"

$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

hide emi
with charamoveoutleft

# "I'd answer her, but I'm too focused on getting air into my lungs and ignoring the burning in my leg muscles."
"ฉันอยากตอบกลับไป แต่แค่จะหายใจให้ทันกับทนความเจ็บปวดของกล้ามเนื้อขาที่กำลังร้อนผ่าวให้ได้ก็เต็มกลืนแล้ว"

# "Part of me wants to say something like “Maybe {b}you{/b} can, but I'm about to die here.”"
"ใจหนึ่งก็อยากสวนกลับไปว่า “{b}เธอ{/b}น่ะอาจทำได้ ส่วนฉันจะตายแล้วเนี่ย” อะไรแบบนี้อยู่เหมือนกัน"

# "But again, I doubt I can actually form words right now."
"แต่ก็นะ ตอนนี้จะพูดออกมาเป็นภาษาให้ได้สักคำยังจะไม่ไหวเลย"

# "Emi keeps pace with me as I round the second turn and cross the finish line."
"เอมิวิ่งเลี้ยวเข้าโค้งที่สองพร้อมผ่อนฝีเท้าให้เท่ากับฉันแล้วเราก็ผ่านเข้าเส้นชัยไป"

stop ambient fadeout 1.5

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")

stop music fadeout 5.0

show bg school_track_on
show emi basic_happy_gym
with locationchange

# "Her sprint seems to have gotten her sweating."
"ดูเหมือนว่าการวิ่งเต็มฝีเท้าเมื่อกี้พอจะทำให้เธอเสียเหงื่อได้"

# "It's actually caused her shirt to turn slightly translucent. It seems she wears a black sports bra."
"ส่งผลให้เสื้อที่สวมอยู่โปร่งขึ้นเล็กน้อยจนเห็นสปอร์ตบราสีดำที่เธอสวมอยู่"

# "I feel a vague stab of guilt for being the sort of guy who stares at a girl's chest, but my legs and chest are burning so badly I can't bring myself to care that much."
"ฉันรู้สึกผิดนิด ๆ ที่เผลอไปมองเข้า แต่ความเจ็บปวดจากขากับหน้าอกที่ร้อนราวไฟสุมก็กินพื้นที่ในสมองไปเกือบหมด\nจนไม่เหลือที่ให้ความรู้สึกผิดแล้ว"

show emi excited_proud_gym
with charachange

# emi "Not bad for a first effort, Hisao."
emi "ถึงจะเป็นครั้งแรกแต่ก็ทำได้ไม่เลวเลยนี่ ฮิซาโอะ"

play music music_happiness fadein 0.5

# hi "Ki— …kind of you… to say… so."
hi "ขะ …ขอบคุณ… ที่… ชม"

# "Emi seems to be, if not out of breath, at least breathing a little more heavily than she was before we started running."
"เอมิหายใจแรงขึ้น แม้ว่าจะไม่ถึงกับเหนื่อยหอบ แต่อย่างน้อยก็หายใจแรงกว่าตอนก่อนที่เราจะเริ่มวิ่ง"

# "It must have been the sprint that did it."
"คงเป็นผลจากการวิ่งเต็มฝีเท้าเมื่อกี้นี้"

show emi basic_grin_gym
with charachange

# emi "Hey, I've got to get a few sprints in. You should walk around the track to cool down."
emi "ฉันขอไปวิ่งต่ออีกหน่อย ส่วนนายก็ไปเดินรอบสนามเป็นการคูลดาวน์เถอะ"

# emi "Then we can stretch out, and we'll be all done, okay?"
emi "จากนั้นค่อยมายืดเส้นยืดสายกันอีกรอบก่อนจบ โอเคมั้ย"

# hi "Sounds great."
hi "ได้เลย"

# "My legs are on fire, and my breathing is still heavy, but surprisingly my heart seems to be taking the strain well."
"ขาทั้งสองยังร้อนจนเหมือนโดนไฟไหม้ ลมหายใจก็ยังไม่กลับมาเป็นปกติ แต่ดูเหมือนว่าหัวใจของฉันจะยังทนไหว"

# "Another triumph of medical science, I suppose."
"เป็นวิทยาศาสตร์การแพทย์ที่ได้ชัยไปอีกครา"

show emi basic_closedhappy_gym
with charachange

# emi "You should put your hands behind your head. It makes it easier to catch your breath."
emi "ยกมือขึ้นแล้ววางไว้ที่ท้ายทอยสิ จะได้หายใจสะดวกขึ้น"

$ renpy.music.set_volume(0.3, 1.0, channel="ambient")

play ambient sfx_emipacing

hide emi
with charamoveoutleft

# "Surprisingly, she's right. I begin to stroll around the track, happy to feel my breath coming back to me."
"คำแนะนำของเอมิได้ผลอย่างน่าประหลาด ฉันเริ่มเดินทอดน่องไปรอบสนามวิ่งด้วยความรู้สึกดีที่ลมหายใจค่อย ๆ\nกลับมาเป็นปกติ"

$ renpy.music.set_volume(1.0, 0.5, channel="ambient")

show emi blur at offscreenright
with None

show emi blur at offscreenleft
with move

$ renpy.music.set_volume(0.3, 0.5, channel="ambient")

hide emi
with None

# "There's a blur as Emi sprints by me."
"เอมิวิ่งผ่านฉันไปจนเห็นเป็นภาพมัว ๆ"

# "Watching her run is absolutely fascinating."
"การได้เห็นเอมิวิ่งนั้นเป็นอะไรที่น่าทึ่งมากจริง ๆ"

# "It's not just because she's on prosthetics, though that is interesting."
"ไม่ใช่เพราะว่าเธอวิ่งโดยสวมขาเทียมหรอก แต่ตรงนั้นก็น่าสนใจเหมือนกัน"

show ev emi_run_face_zoomin
show ev emi_run_face as unlockstub behind ev
with dissolve

# "The really interesting thing is the way her face changes."
"ทว่ายังไม่เท่ากับการที่สีหน้าของเธอเปลี่ยนไป"

# "I can only catch glimpses of it as she runs by, but her eyes seem to come alive with a sort of fierce joy."
"ฉันทันสังเกตเห็นสิ่งนั้นได้เพียงแวบเดียวในตอนที่เธอวิ่งผ่านไป เห็นแววตาของเธอที่เปี่ยมไปด้วยพลังความสุข"

# "It's as if there's nothing else in the world but her and the track."
"ราวกับทุกสิ่งบนโลกปลาสนาการไปสิ้น และเหลือเพียงเธอกับสนามวิ่ง"

stop ambient fadeout 0.5

$ renpy.music.set_volume(1.0, 0.5, channel="ambient")

scene bg school_track_on
with locationchange

# "By the time I've gotten to the final stretch, Emi seems to have finished her sprinting."
"พอฉันเดินมาถึงช่วงก่อนเข้าเส้นชัยเอมิก็เหมือนจะวิ่งเสร็จแล้ว"

# "She's breathing heavily now, but she's wearing a satisfied grin on her face. She waves to me cheerily as I near her."
"เอมิหอบหนัก แต่ใบหน้ากลับประดับด้วยรอยยิ้มกว้างอย่างพึงพอใจ เธอโบกมือให้ตอนที่ฉันเดินไปหา"

show emi basic_grin_gym at center
with charaenter

# emi "Feeling better, right?"
emi "รู้สึกดีขึ้นแล้วใช่มั้ย"

# hi "Actually, yeah."
hi "อืม ดีขึ้นแล้ว"

show emi sad_grin_gym
with charachange

# emi "D'you want to take another lap around with me? I've got to cool down too, you know."
emi "มาเดินรอบสนามอีกรอบเป็นเพื่อนฉันมั้ย ฉันก็ต้องคูลดาวน์เหมือนกัน"

# "Part of me would rather sit down, and not move, but something tells me that would be a bad idea."
"ใจหนึ่งฉันก็อยากนั่งอยู่เฉย ๆ แต่อะไรบางอย่างบอกฉันว่านั่งไม่ได้แน่"

# "Besides, if I sit down, there may be no getting back up again."
"ราวกับว่าถ้านั่งแล้วจะลุกขึ้นไม่ได้อีก"

# hi "Sure, why not?"
hi "ได้สิ"

# "Emi's got her hands behind her head now as well, which makes her seem very relaxed."
"เอมิยกมือขึ้นวางไว้ที่ท้ายทอยด้วย ซึ่งทำให้ดูผ่อนคลายมาก"

# "The positioning of her arms also pulls her shirt upwards ever-so-slightly so that I can see a small strip of her belly."
"แขนของเอมิที่ยกขึ้นรั้งเสื้อขึ้นแบบเหลื่อม ๆ ให้เห็นหน้าท้องอยู่เล็กน้อย"

# "I do my best to act the gentleman and not look, but the contrast of her skin against her red running shorts is rather arresting."
"ฉันพยายามทำตัวให้เป็นสุภาพบุรุษด้วยการไม่มอง แต่ผิวเนื้อเรียบเนียนที่ตัดกับกางเกงวิ่งสีแดงที่เธอสวมอยู่ก็ช่างน่าดูชม"

show emi basic_grin_gym
with charachange

# emi "So how do you feel, Hisao?"
emi "แล้วนายรู้สึกยังไงบ้างล่ะฮิซาโอะ"

# hi "Surprisingly good, actually. I'm sore and tired, but… surprisingly good."
hi "ถึงจะยังปวดขาแล้วก็เหนื่อยอยู่ แต่ก็… รู้สึกดีผิดคาดเลย"

# "As soon as I say it, I realize that it's true."
"พอพูดออกไปแล้วถึงได้รู้สึกว่าเป็นอย่างนั้นจริง"

# "Sure, part of me wants to lay down and die, but I feel like I've accomplished something."
"แน่ละว่าใจหนึ่งก็อยากจะล้มลงไปนอนสิ้นชีพเดี๋ยวนั้นเลยเสียให้ได้ แต่อีกใจก็รู้สึกเหมือนตัวเองได้ประสบความสำเร็จ\nในการทำอะไรสักอย่าง"

# "It's almost like a glow throughout my body that persists despite the soreness."
"ราวกับมีพลังงานบางอย่างปกคลุมอยู่ทั่วร่างกายแม้จะยังรู้สึกปวดร้าวอยู่ด้วยก็ตาม"

show emi excited_proud_gym
with charachange

# emi "Yeah, that's the runner's high."
emi "นั่นแหละคือภาวะอารมณ์ดีหลังวิ่งล่ะ"

# hi "Runner's high?"
hi "ภาวะอารมณ์ดีหลังวิ่ง?"

show emi basic_hes_gym
with charachange

# emi "Yeah, it has something to do with… adrenaline?"
emi "อื้ม เหมือนจะเกี่ยวกับ… สารอะดรีนาลินมั้ง"

# "Emi thinks for a moment as we walk, trying to remember."
"เอมิเค้นสมองนึกอยู่สักพักระหว่างที่เรากำลังเดินไปด้วยกัน"

show emi basic_closedgrin_gym
with charachange

# "Then she shrugs and grins at me."
"แต่สุดท้ายเอมิก็ยักไหล่แล้วหันมาส่งยิ้มให้"

show emi basic_grin_gym
with charachange

# emi "I don't actually remember. It's a good feeling though, isn't it?"
emi "นึกไม่ออกอะ เอาเป็นรู้แค่ว่ามันทำให้รู้สึกดีก็พอแล้วกัน"

show emi basic_happy_gym
with charachange

stop music fadeout 0.5
play sound sfx_heartstop

# emi "Better than sex, right?"
emi "ดีกว่ามีอะไรกันเสียอีก เนอะ"

# "I open my mouth to respond shortly before processing what she's just said."
"ฉันอ้าปากค้างไว้เพื่อจะพูดตอบ แต่ผ่านไปพักหนึ่งสมองถึงจะประมวลผลสิ่งที่เธอเพิ่งพูดออกมาได้"

hi "…"

# "Emi watches my face for a few moments before bursting into laughter."
"เอมิมองใบหน้าของฉันชั่วครู่ก่อนจะหัวเราะออกมาเสียงดัง"

play music music_comedy fadein 1.0

show emi excited_laugh_gym
with charachange

# emi "Sorry, sorry! I couldn't resist! You're just too easy!"
emi "ขอโทษนะ ขอโทษ! พอดีอดใจไม่ไหว! ก็นายน่าแกล้งเกินไปนี่นา!"

# hi "Why did I agree to run with you again?"
hi "ทำไมฉันถึงยอมมาวิ่งกับเธอกันนะ"

# "Emi just laughs harder. She takes a hold of my forearm and tilts it, allowing her to get a better view of my watch. Her face changes the moment she sees the time."
"เอมิหัวเราะเสียงดังกว่าเก่า เธอจับปลายแขนฉันบิดดูเวลาจากนาฬิกาข้อมือ ก่อนที่สีหน้าจะเปลี่ยนไปทันทีที่เห็น\nตัวเลขบนหน้าปัด"

show emi basic_shock_gym
with charachange

# emi "Oh no! We'd better get a move on, Hisao!"
emi "แย่แล้ว! เราต้องรีบแล้วละฮิซาโอะ!"

show emi basic_closedsweat_gym
with charachange

# emi "Class is in an hour, and I need to shower!"
emi "อีกแค่ชั่วโมงเดียวก็จะเข้าเรียนแล้ว และฉันก็ต้องอาบน้ำก่อนด้วย!"

# hi "I should probably do that as well…"
hi "นั่นสินะ ฉันเองก็คงต้องอาบด้วย…"

show emi basic_hes_gym
with charachange

# emi "I need to see the nurse, too… maybe he'll write me a note for being late!"
emi "แถมยังต้องไปหาคุณพยาบาลด้วยอีก… เดี๋ยวเขาต้องบันทึกว่าไปสายแน่เลย!"

# hi "Why do you need to see the nurse?"
hi "ทำไมต้องไปหาคุณพยาบาลด้วยล่ะ"

show emi basic_closedgrin_gym
with charachange

# "Emi points to her prosthetics, as if that would explain everything."
"แล้วเอมิก็ชี้นิ้วไปที่ขาเทียมทั้งสองของตนเองอย่างกับว่าฉันจะตรัสรู้เองได้"

show emi basic_grin_gym
with charachange

# emi "It's important to check for irritation."
emi "ต้องไปตรวจสภาพเผื่อมีการระคายเคืองน่ะ"

# emi "You know, from sweat or friction, or anything."
emi "แบบว่าระคายจากเหงื่อ การเสียดสี หรืออะไรประมาณนั้น"

show emi excited_amused_gym
with charachange

# emi "Normally I only go after practice, but if we're going to be doing these morning runs then I guess I'll see him twice a day."
emi "ปกติฉันจะไปหาคุณพยาบาลเฉพาะหลังซ้อมน่ะ แต่ถ้าจะเริ่มวิ่งตอนเช้าด้วยกันแบบนี้ก็คงต้องไปหาวันละ\nสองครั้งแล้ว"

# "Wait, so Emi has only started doing these runs since I showed up?"
"เดี๋ยวสิ เอมิเองก็เพิ่งเริ่มวิ่งตอนเช้าแบบนี้เพราะฉันเหรอ"

# hi "If it's more convenient for you to run with me at a later time…"
hi "ถ้าไม่สะดวกเดี๋ยวเราวิ่งกันแค่ตอนบ่าย ๆ ก็ได้นะ…"

show emi sad_grin_gym
with charachange

# emi "Don't be silly! I've been meaning to start running in the morning for a while now."
emi "ไม่เป็นไรหรอกน่า! ฉันเองก็กะจะเริ่มวิ่งตอนเช้าแบบนี้มาสักพักแล้ว"

# emi "But if I didn't have a partner to run with, I'd be less likely to keep up a routine."
emi "แต่ถ้าไม่มีคนมาวิ่งด้วยก็รู้สึกเหมือนจะไม่มีวินัยสักเท่าไหร่"

show emi basic_grin_gym
with charachange

# emi "It's always harder to blow off a commitment if you're going to let someone else down, you know?"
emi "พอทำอะไรด้วยกันแล้ว ถ้าจะถอนตัวแล้วต้องทิ้งอีกคนไปแล้วก็จะหนักใจขึ้นเยอะเลย"

show emi basic_closedgrin_gym
with charachange

# emi "So you'll be my running partner for the mornings!"
emi "งั้นนายก็กลายเป็นคู่วิ่งของฉันในตอนเช้าแล้วนะ!"

show emi excited_proud_gym
with charachange

# emi "We both need the exercise, so it all works out, don't you think?"
emi "เราต้องออกกำลังกายกันทั้งคู่อยู่แล้ว เหมือนยิงปืนนัดเดียวได้นกสองตัวเลยว่ามั้ย"

# hi "Yeah, perfect."
hi "อืม สมบูรณ์แบบเลย"

# "Did it have to be me, though?"
"แต่ว่าคนคนนั้นจำเป็นจะต้องเป็นฉันด้วยเหรอ?"

# "Well, I guess I can't complain too much. Emi's pretty fun to hang out with."
"แต่ก็คงว่าอะไรไม่ได้ละนะ เอมินั้นเป็นคนที่อยู่ด้วยแล้วสนุกจริง ๆ"

# "And she's right. I do need the exercise. Doctor's orders, even."
"และเธอก็พูดถูก ฉันจำเป็นต้องออกกำลังกาย หมอสั่งมาเลยด้วยซ้ำ"

show emi basic_happy_gym
with charachange

# "Emi waves a quick goodbye to me."
"เอมิโบกมือลาฉันหย็อย ๆ"

# emi "Right, I'm off! Come have lunch with us, okay?"
emi "งั้นฉันไปก่อนนะ! แล้วก็มากินข้าวเที่ยงด้วยกันนะ โอเคมั้ย"

# hi "What?"
hi "อะไร"

show emi basic_closedhappy_gym
with charachange

# emi "Lunch! You know, the meal? In the middle of the day? Come have it with us!"
emi "ข้าวเที่ยงไง! ที่เป็นมื้ออาหาร? กินกันตอนเที่ยง? มากินกับพวกเราสิ!"

# hi "Where?"
hi "ที่ไหน"

show emi basic_grin_gym
with charachange

# emi "The rooftop. Rin likes it up there."
emi "บนดาดฟ้า รินชอบอยู่ที่ดาดฟ้า"

# hi "When?"
hi "เมื่อไหร่"

show emi basic_annoyed_gym
with charachange

# emi "Lunchtime, when else? That was a silly question."
emi "จะเป็นตอนไหนได้ล่ะ ก็ต้องตอนพักเที่ยงน่ะสิ ถามอะไรแปลก ๆ"

# hi "Yeah, but I sort of felt the need to ask all three for completeness' sake."
hi "เปล่าหรอก แค่รู้สึกว่าควรจะถามให้ครบทั้งสามคำถามเพื่อความสมบูรณ์น่ะ"

show emi excited_laugh_gym
with charachange

# "Emi laughs and grins. I don't think I've ever seen a girl smile so much before."
"เอมิหัวเราะและฉีกยิ้มกว้าง ฉันไม่เคยเห็นเด็กผู้หญิงคนไหนชอบยิ้มขนาดนี้มาก่อนเลย"

show emi excited_happy_gym
with charachange

# emi "Not bad, Hisao. See ya!"
emi "ใช้ได้นี่ฮิซาโอะ แล้วเจอกันนะ!"

play ambient sfx_emisprinting

hide emi
with easeoutleft

stop ambient fadeout 2.0
stop music fadeout 8.0

# "With that, she takes off like a shot for the school building."
"แล้วเธอก็ทะยานไปที่อาคารเรียนราวกับลูกปืนหลุดจากแล่ง"

# "I guess she's going to see the nurse first."
"เดาว่าเจ้าตัวคงจะไปหาคุณพยาบาลก่อน"

scene bg school_dormbathroom
with locationskip

# "I hurry back to my room and hop in the shower, only to find that the water takes a while to heat up."
"ฉันรีบกลับไปที่ห้องแล้วเดินไปอาบน้ำต่อโดยไม่รอช้า ถึงได้รู้ว่ากว่าน้ำจะอุ่นก็ต้องใช้เวลารอสักพัก"

play ambient sfx_shower
with vpunch

# "The shock of the cold water nearly kills me."
"หัวใจแทบหยุดเต้นเพราะโดนน้ำเย็นราดหัว"

show steam
with Dissolve(2.0)

# "I manage to warm the water a bit and spend some quality time feeling my muscles loosen."
"ฉันรอให้น้ำอุ่นขึ้นอีกสักหน่อยแล้วใช้เวลาไปกับการสัมผัสถึงความรู้สึกของการที่กล้ามเนื้อกำลังคลายตัวอย่างเชื่องช้าโดยไม่รีบร้อน"

# "My heart, surprisingly, feels the least bothered by the run."
"น่าทึ่งดีที่หัวใจฉันแทบไม่เป็นอะไรเลยกับการวิ่ง"

# "I suppose that's a good thing, even if it does make me feel like a bit of a wuss."
"ก็ดีแหละ แต่พอรู้ว่าจริง ๆ ก็ไม่เป็นไรแล้วรู้สึกเหมือนตัวเองเป็นพวกพะวงเกินเหตุไปหน่อย"

# "I mean at least I'd have an excuse beyond “I am out of shape” if my heart were bothering me."
"ก็ถ้าเกิดหัวใจเป็นอะไรขึ้นมาจริง ๆ อย่างน้อยก็จะได้อ้างอย่างอื่นนอกจากว่า “รู้สึกไม่ค่อยฟิตเท่าไหร่” แล้วไม่ต้อง\nไปวิ่ง"

# "Guess I'll have to keep this running thing up, otherwise I'm sure Emi won't let me hear the end of it."
"ฉันคงต้องมีวินัยในการไปวิ่งเข้าไว้ ไม่งั้นเดี๋ยวได้โดนเอมิบ่นจนหูชาแหง"

# "It's only after I get out and dry myself off that I realize that I've only ten minutes left to put my clothes on and get to class."
"พอออกมาจากห้องน้ำและเช็ดตัวให้แห้งแล้วถึงค่อยรู้ว่าเหลือเวลาอีกแค่สิบนาทีให้แต่งตัวและรีบไปเรียน"

# "Crap."
"ซวยแล้วสิ"

########################################################
label th_E4:

scene bg school_dormbathroom
show steam
with None

stop ambient fadeout 1.0

scene bg school_scienceroom
with shorttimeskip

window show

play sound sfx_normalbell

# "The hands on the clock finally set me free from the tedium of yet another fun-filled class."
"เข็มนาฬิกาที่คอยกำหนดเวลาในที่สุดก็ได้ปลดปล่อยฉันให้เป็นอิสระจากชั้นเรียนอันสนุกสนาน\nแต่ก็แสนจะน่าเบื่อหน่ายนี้เสียที "

# "Getting up from my seat proves to be more of a problem than I anticipated."
"เพียงแต่การจะลุกขึ้นจากเก้าอี้ให้ได้นั้นกลับเป็นปัญหากว่าที่คิด"

# "My legs are killing me from the morning's run."
"ขาของฉันยังคงระบมจากการวิ่งในตอนเช้า"

# "Maybe doing these with Emi isn't such a hot idea after all."
"ดูท่าว่าการออกไปวิ่งกับเอมิจะไม่ใช่ความคิดที่ดีสักเท่าไหร่"

# "Still, the run's given me a hell of an appetite."
"แต่ที่รู้สึกอยากอาหารขึ้นมาได้มากขนาดนี้ก็เป็นผลจากการวิ่งเหมือนกัน"

play ambient sfx_crowd_indoors fadein 1.0

scene bg school_hallway3
show crowd
with locationchange

# "I'm halfway down the hallway to the cafeteria when I remember that I've got my lunch with me."
"ฉันเดินมาได้ครึ่งทางแล้วถึงนึกขึ้นได้ว่ามีข้าวเที่ยงอยู่กับตัว"

# "My parents saw fit to provide me with some prepackaged stuff when I moved in, and a good thing too."
"เป็นของที่พ่อแม่คิดว่าจำเป็นเลยเตรียมไว้ให้ตอนที่ย้ายมาอยู่ที่นี่ ซึ่งก็เป็นเรื่องที่ดี"

# "The hallway is packed with students headed for the cafeteria."
"โถงทางเดินเต็มไปด้วยเหล่านักเรียนที่กำลังมุ่งหน้าไปยังโรงอาหาร"

# "Going back is like swimming upstream - but I've got an appointment to keep on the rooftop."
"จะให้เดินสวนกระแสฝูงชนไปก็ดูลำบาก แต่ฉันก็มีนัดที่ต้องไปอยู่บนดาดฟ้า"

stop ambient fadeout 4.0

scene bg school_staircase1
with locationchange

# "It takes me a moment to find the staircase leading up to the rooftop, but I'm willing to bet that Emi and Rin aren't up there by now anyway."
"ฉันใช้เวลาอยู่พักหนึ่งในการตามหาบันไดเพื่อขึ้นไปบนดาดฟ้า แต่เชื่อว่ายังไงเอมิกับรินก็น่าจะยังไม่มาเหมือนกัน"

# "In fact, I think I saw Emi among the bodies in the hallway headed for the cafeteria."
"อันที่จริง เหมือนเมื่อกี้เห็นเอมิอยู่กลางกลุ่มคนในโถงทางเดินที่มุ่งหน้าไปยังโรงอาหารด้วยซ้ำ"

play sound sfx_door_creak
$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_rooftop fadein 0.5

scene bg school_roof at bgright
with locationchange

# "I step out of the door to the roof and take a deep breath."
"ฉันก้าวผ่านประตูออกไปสู่ดาดฟ้าแล้วสูดลมหายใจเข้าลึก"

# "The fresh air blowing against my face and body almost makes my legs hurt less."
"อากาศสดชื่นที่พัดมาปะทะกับร่างกายและใบหน้าแทบทำให้ความเจ็บปวดจากขาทั้งสองข้างบรรเทาลงไปได้"

show rin basic_awayabsent at center
with charaenter

# rin "Maybe if I'm upside down…"
rin "บางทีถ้าลองกลับหัวดู…"

$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_rin fadein 1.0

# "Part of me wants to be surprised that Rin's already up here."
"ใจหนึ่งก็อยากตกใจอยู่นะที่เห็นรินขึ้นมาก่อนแล้ว"

# hi "What's that going to accomplish?"
hi "ทำแบบนั้นไปแล้วจะได้อะไรขึ้นมา"

show rin basic_deadpan
with charachange

# rin "Things in the clouds."
rin "สิ่งที่อยู่ในเมฆ"

# hi "Couldn't you just… look at them right-side up?"
hi "แค่… เงยขึ้นไปมองแบบปกติเอาไม่ได้เหรอ"

show rin basic_deadpanupset
with charachange

# "Rin rolls her eyes in something approaching exasperation."
"รินกลอกตาด้วยอารมณ์ละม้ายระอาใจ"

# rin "Then I wouldn't get a new perspective."
rin "งั้นฉันก็จะไม่ได้มุมมองแบบใหม่สิ"

# hi "Is upside down really a new perspective?"
hi "แค่การกลับหัวก็นับว่าเป็นมุมมองแบบใหม่แล้วเหรอ"

show rin basic_delight
with charachange

# "Ah ha! That caught her off guard. Rin looks pensive."
"ไงล่ะ! คาดไม่ถึงละสิ รินทำหน้าครุ่นคิด"

# rin "You may have a point. Maybe sideways."
rin "ก็คงจะถูกของนาย งั้นก็อาจลองมองจากด้านข้าง"

hide rin
with charamoveoutbottom

# "As Rin lays down on the bench to look at the sky, I give up."
"รินนอนลงบนม้านั่งเพื่อมองท้องฟ้า ส่วนฉันก็ยอมแพ้"

play sound sfx_impact2
with vpunch

show emi basic_closedgrin at center
with charaenter

# "Fortunately Emi chooses that moment to burst through the door carrying two bags."
"โชคดีที่เอมิเลือกเวลาโผล่ออกมาจากประตูได้อย่างถูกจังหวะพร้อมกับถุงทั้งสองที่ถือไว้ในมือ"

# "She nearly takes the door off the hinges."
"ตอนเปิดออกมาทำเอาบานประตูแทบหลุดจากบานพับ"

show emi basic_hes
with charachange

# emi "Sorry it took me so long! There were a ton of people in line."
emi "ขอโทษด้วยที่มาช้า! ในโรงอาหารมีคนต่อแถวยาวเต็มไปหมดเลย!"

show emi basic_grin
with charachange

show emi basic_grin at twoleft
show bg school_roof at center
with charamove

# "She drops the first bag in front of Rin and takes a seat on the bench next to her."
"เธอวางถุงแรกลงด้านหน้ารินก่อนจะนั่งลงข้าง ๆ บนม้านั่งตัวเดียวกัน"

# hi "You buy Rin's lunch for her?"
hi "เธอซื้อข้าวเที่ยงให้รินด้วยเหรอ"

show emi basic_closedgrin
with charachange

# emi "Sometimes, yeah. I'd have Rin buy my lunch for me in return, but I'm not sure how she'd carry it."
emi "ซื้อให้เป็นบางครั้งน่ะ เดี๋ยวค่อยให้รินซื้อให้คืน ถึงจะไม่รู้ว่าจะถือมายังไงก็เถอะ"

show rin basic_deadpan at tworight
with charamoveinbottom

# rin "Plus I'd never buy her lunch."
rin "อีกอย่าง ฉันคงไม่ซื้อข้าวเที่ยงให้เอมิหรอก"

# "If Rin's offended by Emi's comment, she doesn't show it. Emi sniffs."
"รินไม่แสดงอาการที่เอมิล้อ ส่วนเอมิทำท่าสะอื้น"

show emi basic_annoyed
with charachange

# emi "How ungrateful of you."
emi "อกตัญญูจริงนะเธอ"

# "I'm not sure whether the two are joking with one another or if I'm witnessing the beginnings of a cat fight."
"ฉันไม่แน่ใจแล้วว่าทั้งสองคนล้อกันเล่นเฉย ๆ หรือว่าอีกเดี๋ยวจะทะเลาะกันจริง"

show emi basic_closedgrin
show rin basic_amused
with charachange

# "The two girls stare at one another for a few tense moments before breaking into smiles."
"เด็กสาวทั้งสองหันมาจ้องหน้ากันครู่หนึ่งก่อนจะยิ้มออกมา"

show rin basic_awayabsent
with charachange

# rin "Hey Emi, do you think being upside down is a new perspective on things?"
rin "นี่ เอมิ คิดว่าการกลับหัวถือว่าเป็นมุมมองแบบใหม่ต่อสิ่งต่าง ๆ หรือเปล่า"

# "Didn't I already have this conversation?"
"ไม่ใช่ว่าเราคุยเรื่องนี้กันไปแล้วหรือไง"

show emi basic_hes
with charachange

# "Emi looks thoughtful, apparently giving the question some thought."
"เอมิทำท่าทางครุ่นคิดกับคำถามนั้นอย่างเห็นได้ชัด"

# "After a deep and profound pause, she speaks."
"หลังจากนิ่งเงียบไปเพื่อใช้ความคิดอยู่สักพักเอมิก็พูดออกมา"

show emi basic_closedsweat
with charachange

# emi "I have no idea."
emi "ไม่รู้สิ"

# "Well, at least she's as lost as I am."
"อืม อย่างน้อยก็งงพอกันกับฉันแหละ"

stop music fadeout 4.0

show emi excited_happy
with charachange

# emi "Hey Hisao, you're coming to the track meet, right?"
emi "นี่ ฮิซาโอะ นายก็จะมาดูงานแข่งวิ่งด้วยใช่มั้ย"

# "The question comes out of the blue and catches me off guard."
"คำถามที่หลุดออกมาอย่างไม่มีปี่มีขลุ่ยนั้นทำให้ฉันไม่ทันตั้งตัว"

# hi "Um… I don't know yet?"
hi "เอิ่ม… ยังไม่รู้สิ?"

show rin basic_absent
show emi sad_annoyed
with charachange

# emi "Honestly, Hisao, after I went through all the trouble of letting you run with me in the morning, you won't even show up at my track meet?"
emi "เอาตามตรงนะฮิซาโอะ ฉันอุตส่าห์ลำบากตรากตรำยอมไปวิ่งกับนายตอนเช้า แต่ใจคอจะไม่มาดูงานแข่งวิ่ง\nกันหน่อยเลยเหรอ"

show rin basic_awayabsent
with charachange

# "Wasn't she the one that asked me to run with her?"
"ไม่ใช่ว่าหล่อนเป็นคนชวนฉันไปวิ่งเองแต่แรกไม่ใช่หรือไง"

# "Actually, she didn't even give me a choice in the matter."
"แต่เรื่องนั้นเจ้าตัวเองก็ไม่ได้ให้ทางเลือกอะไรกับฉันด้วยซ้ำไป"

# hi "Wait, no, I didn't say that…"
hi "เดี๋ยวสิ ฉันก็ไม่ได้บอกว่าจะไม่ไปสักหน่อย…"

play music music_ease fadein 3.0

show emi basic_closedgrin
show rin basic_absent
with charachange

# "She beams at me as if I'd just agreed to give her a million dollars."
"เธอยิ้มแฉ่งอย่างกับว่าฉันเพิ่งจะตกลงยกเงินล้านให้เธอ"

show emi basic_closedhappy
with charachange

# emi "So you will come after all! That's great!"
emi "งั้นนายก็จะมาสินะ! ดีเลย!"

# "I didn't say that either!"
"ฉันก็ไม่ได้บอกว่าจะไปเหมือนกัน!"

show rin basic_deadpan
with charachange

# rin "I'll be going too, so I'll make sure he comes, Emi."
rin "ฉันจะไปเหมือนกัน เดี๋ยวฉันจะลากฮิซาโอะมาให้ได้เลยเอมิ"

show emi basic_grin
show rin basic_absent
with charachange

# emi "Good idea, Rin! Maybe we can get some food or something after the meet's over?"
emi "ความคิดเยี่ยมไปเลยริน! งั้นเสร็จงานแล้วเราไปหาอะไรกินหรือหาอะไรทำด้วยกันดีมั้ย"

# "I feel like I've just been conned, but not by these two."
"ฉันรู้สึกเหมือนตัวเองกำลังถูกชักจูงอยู่ แต่ไม่ใช่ด้วยฝีมือของทั้งสองคนนี้"

# "More like by some outside force, pushing me irrevocably toward my destiny."
"แต่เหมือนกับมีพลังงานบางอย่างจากภายนอกที่กำลังผลักดันฉันให้มุ่งเข้าหาโชคชะตาที่ไม่อาจเลี่ยงนี้"

# "…Or maybe I shouldn't read books that feature conspiracy theories so heavily. Otherwise I might wind up sounding like Kenji."
"…หรือฉันควรจะเลิกอ่านหนังสือที่มีเรื่องสมคบคิดสักที เพราะเดี๋ยวจะกลายเป็นแบบเคนจิเอาได้"

# "Still, I suppose that I've got to show up now."
"ก็นะ ตกลงไว้แล้วก็คงต้องไป"

# "I don't think that I could stand against both of them being disappointed."
"ฉันว่าฉันคงปล่อยให้สองคนนี้ผิดหวังไม่ได้หรอก"

# "I'd never hear the end of it."
"ไม่งั้นได้โดนบ่นจนหูชาแน่"

# hi "When is it again?"
hi "แล้วไปวันไหนนะ"

show emi basic_annoyed
with charachange

# emi "Next week, silly! I just told you a few days ago."
emi "สัปดาห์หน้าไงนายคนความจำสั้น! ฉันเพิ่งจะบอกนายไปเมื่อไม่กี่วันก่อนเอง"

# hi "No you didn't."
hi "ไม่อะ เธอไม่ได้บอก"

show emi sad_shy
with charachange

# emi "I forgot? Well, you won't forget to come though, will you?"
emi "หรอกเหรอ? แต่นายคงจะไม่ลืมหรอกใช่มั้ย?"

# hi "Of course I won't! I'll even make a note on a calendar or something!"
hi "ฉันไม่ลืมหรอกน่า! เดี๋ยวจะจดไว้ในโน้ตไม่ก็เขียนลงบนปฏิทินเลยเอ้า!"

show rin basic_lucid
with charachange

# "Rin nods sagely."
"รินพยักหน้าอย่างสุขุม"

show rin basic_deadpancontemplation
with charachange

# rin "That's probably a good idea, you know. Unless time changes its course."
rin "นั่นเป็นความคิดที่ดี เว้นเสียแต่ว่ากาลเวลาจะเกิดการบิดเบือน"

show emi basic_confused
with charachange

# emi "It can do that?"
emi "เวลามันบิดได้ด้วยเหรอ"

show rin relaxed_nonchalant
with charachange

# "Rin gives a noncommittal shrug."
"รินยักไหล่ไม่ยี่หระ"

show rin negative_spaciness
with charachange

# rin "It hasn't yet, but you never know…"
rin "ยังไม่เกิด แต่เราก็ไม่มีทางรู้…"

show emi basic_closedgrin
with charachange

# "This time it's Emi who gives a shrug."
"คราวนี้เอมิเป็นฝ่ายยักไหล่"

show emi basic_closedhappy
with charachange

# emi "I suppose it can't be helped if it happens."
emi "ถ้าเกิดเรื่องแบบนั้นขึ้นจริงก็คงช่วยไม่ได้"

show rin basic_deadpannormal
with charachange

# rin "Not unless you're a time traveler or something."
rin "เว้นแต่ว่าเธอจะเป็นนักท่องเวลาหรืออะไรสักอย่าง"

# hi "You don't actually think that could happen, do you?"
hi "นี่คงไม่ได้คิดกันจริง ๆ ใช่มั้ยว่าจะเกิดเรื่องแบบนั้นได้"

show emi basic_confused
with charachange

# emi "I don't think we do… do we?"
emi "ก็คงไม่… รึเปล่านะ"

show rin relaxed_nonchalant
with charachange

# "Rin shrugs again. That seems to be her default response to everything."
"รินยักไหล่อีกครั้ง เหมือนการยักไหล่จะเป็นท่าตอบสนองโดยอัตโนมัติต่อทุกสิ่งของรินไปแล้ว"

show rin basic_deadpandelight
with charachange

# rin "I suppose not. But I reserve the right to change my opinion at a moment's notice."
rin "ฉันคิดว่าไม่ แต่ฉันขอเผื่อสิทธิ์ในการเปลี่ยนแปลงความคิดเห็นของตัวเองโดยไม่ต้องแจ้งเตือนล่วงหน้าไว้"

# "For Rin, this statement makes a disturbing amount of sense."
"ช่างเป็นประโยคจากปากรินที่ฟังดูสมเหตุสมผลอย่างน่าประหลาด"

# "The fact that I realize this now frightens me a bit."
"ฉันขนลุกขึ้นมาเมื่อรู้ตัวว่าเพิ่งฉุกคิดขึ้นได้แบบนั้น"

# "I wonder if Emi gets this feeling all the time."
"เอมิจะรู้สึกแบบนี้อยู่ตลอดเลยหรือเปล่านะ"

show emi basic_closedgrin
with charachange

# "If she does she's not showing it, though. Emi merely nods."
"แต่ถ้าเธอรู้สึกจริงก็คงไม่แสดงอาการ เอมิแค่พยักหน้าเบา ๆ"

show emi basic_grin
with charachange

# emi "As expected."
emi "ตามคาด"

show rin basic_deadpanupset
with charachange

# rin "What's that supposed to mean?"
rin "หมายความว่ายังไง"

show emi sad_grin
with charachange

# "This time, it's Emi who shrugs."
"คราวนี้เอมิเป็นฝ่ายยักไหล่"

# "It's like she's using Rin's own weapons against her."
"เหมือนใช้อาวุธของรินเองในการกำราบเจ้าตัว"

show emi excited_proud
with charachange

# emi "Your response is the sort of thing I'd expect from you, that's all."
emi "ก็แค่คิดไว้แล้วว่าเธอจะตอบแบบนี้เท่านั้นเอง"

show rin negative_worried
with charachange

# rin "Am I really that predictable?"
rin "ฉันเป็นคนเดาใจได้ง่ายขนาดนั้นเลยเหรอ"

show emi basic_closedgrin
with charachange

# "Emi's smile seems to border on gloating."
"รอยยิ้มของเอมิกว้างขึ้นด้วยความพอใจ"

# emi "Nah, it's just that your unpredictability is pretty predictable."
emi "เปล่า แค่ว่าความเดาใจไม่ได้ของเธอมันเดาได้อยู่เหมือนกัน"

show rin relaxed_nonchalant
with charachange

# rin "Well that's all right then."
rin "ถ้าอย่างนั้นก็แล้วไป"

play sound sfx_warningbell

# "I don't get the chance to see whether Rin's being serious or not, as the bell rings."
"ฉันไม่ทันได้เห็นว่ารินจริงจังอยู่หรือเปล่าเพราะเสียงระฆังดังขึ้นแล้ว"

# "I didn't notice the lunch period slipping by at all."
"ไม่รู้ตัวเลยสักนิดว่าเวลาพักเที่ยงจบลงแล้ว"

# "Hanging out with these two was far too interesting."
"การได้อยู่กับสองคนนี้เป็นเรื่องที่น่าสนใจมากเกินไป"

show emi basic_shock
with vpunch

# "Emi jumps up, a look of panic on her face."
"เอมิลุกขึ้นยืนอย่างรวดเร็วด้วยสีหน้าตื่นตระหนก"

# emi "Oh no! I needed to stop by my room to pick up my notebook for the next class!"
emi "แย่แล้ว! ฉันต้องแวะไปเอาสมุดบันทึกที่ห้องก่อนเริ่มเรียนวิชาถัดไป!"

show rin basic_deadpandelight
with charachange

# rin "Don't you wish you had a time machine now?"
rin "ทีนี้อยากได้ไทม์แมชชีนขึ้นมาบ้างแล้วหรือยัง"

# "Rin seems rather smug as she delivers this line; like she'd just won an argument."
"รินมีสีหน้าพอใจที่ได้พูดประโยคนั้นออกไปอย่างกับว่าตัวเองเถียงชนะแล้ว"

# "Emi ignores Rin's comment."
"แต่เอมิไม่สนใจรินเลย"

show emi basic_hes
with charachange

# emi "Sorry Hisao, but could you make sure our garbage gets thrown away?"
emi "ขอโทษด้วยนะฮิซาโอะ แต่รบกวนนายช่วยเอาขยะไปทิ้งหน่อยได้มั้ย"

show emi basic_closedsweat
with charachange

# emi "I usually clean up myself, but I've got to run!"
emi "ปกติฉันจะเป็นคนจัดการ แต่ตอนนี้ต้องรีบแล้ว!"

# hi "Sure, no problem."
hi "ได้สิ ไม่มีปัญหา"

hide emi
with easeoutleft

# "Emi darts away with an urgency I'm starting to expect from her."
"เอมิพุ่งไปด้วยความเร่งรีบ ซึ่งฉันเริ่มชินแล้ว"

hide rin
with charaexit

# "I don't bother asking Rin why she couldn't help. She already seems to be preoccupied with something else entirely as she wanders off."
"ฉันไม่คิดจะเอ่ยถามความช่วยเหลือจากริน เธอดูมีเรื่องที่คิดจะทำอยู่ในหัวและก็เดินจากไปแล้ว"

# "She's probably used to Emi taking care of cleanup, and for some reason I doubt Emi's ever raised the issue with her."
"คงจะชินกับการที่เอมิเป็นคนคอยทำความสะอาดแล้ว และฉันก็รู้สึกว่าเอมิก็คงไม่ได้ว่าอะไรรินเรื่องนี้"

# "Cleaning up from lunch doesn't take long, so I have plenty of time to toss our garbage and get to class."
"ฉันใช้เวลาเก็บกวาดไม่นานนักก่อนจะใช้เวลาเหลือ ๆ นั้นไปทิ้งขยะและกลับไปเข้าเรียน"

stop ambient fadeout 1.0

scene bg school_scienceroom
with locationskip

# "Misha greets me with a wave and a devious grin as I walk through the door."
"มิช่าทักทายฉันที่กำลังเดินเข้ามาในห้องด้วยการโบกมือพร้อมยิ้มมีเลศนัย"

show misha cross_grin at center
with charaenter

# mi "Didn't see you in the cafeteria, Hicchan."
mi "ไม่เห็นนายที่โรงอาหารเลยนะฮิจัง"

# hi "Yeah, I decided it was too crowded there."
hi "อืม รู้สึกคนแออัดไปหน่อย"

show misha hips_grin
with charachange

# "Misha's grin gets even wider."
"มิช่ายิ้มกว้างขึ้นกว่าเดิม"

# mi "Oh really? Are you sure you weren't participating in an illicit ren—dez—vous?"
mi "จริงเหรอ แน่ใจนะว่าแค่ไม่ได้ไป—แอบ—เจอใครคนอื่นน่ะ"

# hi "W… what? What are you talking about?"
hi "หะ… หา? พูดอะไรของเธอน่ะ"

show misha sign_smile
with charachange

# mi "You were on the roof, right? With both Rin and Emi, no less! You Casanova, you!"
mi "นายน่ะขึ้นไปอยู่กับรินแล้วก็เอมิบนดาดฟ้ามาใช่มั้ยล่ะ! พ่อหนุ่มคาสโนว่า!"

# hi "We… we just had lunch, that's all!"
hi "กะ… ก็แค่กินข้าวเที่ยงด้วยกันเท่านั้นแหละน่า!"

show misha cross_laugh
with charachange

# "Misha bursts into laughter, drawing the attention of several of my classmates."
"มิช่าหัวเราะออกมาเสียงดังจนหลายคนที่อยู่ในห้องหันมามอง"

# mi "Wahahaha! You're so adorable when you blush like that, Hicchan!"
mi "วะฮ่าฮ่าฮ่า! พอฮิจังหน้าแดงแล้วน่ารักจัง!"

show misha cross_grin
with charachange

# "She gives me a conspiratorial wink."
"แล้วเธอก็ขยิบตาให้ฉันราวกับเราเป็นผู้สมรู้ร่วมคิด"

show misha cross_smile
with charachange

# mi "Don't worry, your secret's safe with me."
mi "ไม่ต้องห่วงหรอก อยู่กับฉันแล้วความลับนายปลอดภัยแน่นอน"

# hi "There's no secret!"
hi "ไม่มีความลับอะไรทั้งนั้นแหละ!"

show misha perky_confused
with charachange

# mi "Oh?"
mi "เหรอ"

# "Misha seems disappointed and then brightens up again."
"มิช่าดูผิดหวังไปเพียงชั่วครู่ก่อนที่จะกลับมาเป็นปกติ"

show misha hips_grin
with charachange

# mi "Time will tell~!"
mi "เดี๋ยวก็ได้รู้กัน~!"

# "I don't know what the hell she's talking about, but blessedly our teacher comes in, and the class starts."
"ไม่เข้าใจเลยว่ามิช่าพูดอะไรอยุ่ แต่ในที่สุดคุณครูก็เดินเข้ามาในห้องแล้วเริ่มสอนเสียที"

stop music fadeout 2.0



########################################################
label th_E5:

scene bg school_scienceroom
with shorttimeskip

play sound sfx_normalbell

# "Another day of class has finally dragged itself to a close."
"คาบเรียนของวันนี้หมดลงอีกครั้ง"

# "Unexpectedly, I managed to stay awake for the whole day."
"ไม่คิดไม่ฝันเลยว่าตัวเองจะลืมตาตื่นได้จนหมดวัน"

# "I'm pretty sure that counts as a miracle."
"ให้เรียกว่าเป็นปาฏิหาริย์ได้เลย"

# "My legs seem unwilling to stand up for a moment."
"ขาทั้งสองของฉันเหมือนขัดขืนที่จะยืนขึ้น"

# "I guess the run took a lot out of me."
"การวิ่งคงดึงเอาแรงออกไปจากฉันจนหมดแล้ว"

scene bg school_hallway3
with locationchange

# "I head down the hallway and make my way to my room."
"ฉันเดินไปตามโถงทางทางเดินมุ่งหน้าไปยังห้องของตัวเอง"

scene bg school_dormhisao
with locationskip

# "I sit down and half-heartedly chip away at my homework for a while, feeling like a vulture picking at a particularly unsavory carcass."
"ฉันนั่งทำการบ้านอย่างไม่มีอารมณ์ร่วมนัก รู้สึกเหมือนตัวเองเป็นอีแร้งที่กำลังเลือกสรรกินซากที่ต่างก็ไม่น่าพิสมัยทั้งสิ้น\nแม้แต่ชิ้นเดียว"

# "It knows this is what it eats, but it's not sure that it shouldn't be ordering takeout instead."
"ซึ่งก็รู้ว่าสิ่งนี้คือสิ่งที่ควรจะกิน แต่ไม่แน่ใจว่าควรเอากลับไปกินที่บ้านด้วยหรือเปล่า"

# "I don't think I can take this, but it's important to get my work done."
"ฉันก็คงทนทำไม่ไหวหรอก แต่ต้องทำให้เสร็จ"

# hi "Now let's see… what was I supposed to be looking over again?"
hi "ไหนซิ… ต้องอ่านตรงไหนนะ"

# "I know it's a losing battle, but I fight it anyway."
"ฉันรู้ว่าฝืนสู้ไปยังไงก็ไม่ชนะ แต่ก็ฝืนต่อไป"

# "Halfway through my math homework, I put my pencil down."
"พอทำการบ้านวิชาคณิตศาสตร์ไปได้ครึ่งทางฉันก็วางดินสอลง"

# "This isn't working. I need a distraction."
"ไม่ไหว ฉันต้องการสิ่งบันเทิงใจอย่างยิ่งยวด"

# "Unfortunately, my options for distractions are rather slim."
"โชคไม่ดีที่ฉันมีตัวเลือกไม่มากนัก"

# "I'm not in the mood to read, right now."
"ตอนนี้ก็ไม่รู้สึกอยากอ่านหนังสือด้วย"

# "Kenji is, unusually, out of his room at the moment."
"ส่วนเคนจิก็ออกไปข้างนอก"

# "If I go to the student council room, I'll just end up doing work for those two."
"ถ้าไปที่ห้องสภานักเรียนก็คงหนีชะตาต้องช่วยงานสองคนนั้นไม่พ้น"

# "And heaven only knows where everyone else is, except for…"
"ส่วนคนอื่นฉันก็ไม่รู้ว่าอยู่ที่ไหนกัน เว้นก็แต่…"

# "Well, I suppose that's an option."
"อืม คิดว่าเป็นตัวเลือกหนึ่งได้อยู่แหละ"

# "I grab my shoes and head for the track. Emi's probably down there."
"ฉันสวมรองเท้าแล้วมุ่งหน้าไปยังลู่วิ่ง เอมิน่าจะอยู่ที่นั่นแหละ"

play music music_tranquil fadein 3.0

scene bg school_track_ss
with locationskip

# "Track practice is just ending as I arrive at the track."
"การซ้อมวื่งเพิ่งจบลงพอดีกับตอนที่ฉันเดินมาถึงที่สนาม"

# "The sun's beginning to dip low in the sky."
"ดวงอาทิตย์บนฟ้าเริ่มคล้อยต่ำลงแล้ว"

# "Has it really gotten that late already?"
"เย็นขนาดนี้แล้วเหรอเนี่ย"

show emi basic_grin_gym_ss at center
with charaenter

# emi "What are you doing down here, Hisao?"
emi "มาทำอะไรถึงนี่ล่ะฮิซาโอะ"

show emi excited_proud_gym_ss
with charachange

# emi "Come to spy on me, have you?"
emi "แอบมาส่องฉันเหรอ"

# "I give a shrug. To be honest, I'm not sure why I'm down here."
"ฉันยักไหล่ตอบกลับไป ที่จริงก็ไม่รู้ด้วยซ้ำว่ามาที่นี่ทำไม"

# hi "I didn't have anything better to do."
hi "ก็ไม่มีอะไรจะทำ"

# "I figure that's about right."
"พูดอย่างนั้นก็คงไม่ผิดนัก"

# "At the moment, Emi's the only person I can think of who I could visit."
"เอมิเป็นเพียงคนเดียวที่ฉันคิดว่าจะมาหาได้ในเวลานี้"

show emi basic_annoyed_gym_ss
with charachange

# emi "So I'm your last resort, am I?"
emi "ฉันคือตัวเลือกสุดท้ายของนายสินะ"

show emi sad_angry_gym_ss
with charachange

# emi "Nobody cool around, so I'll just go see Emi, is that what you thought?"
emi "ไม่มีใครให้เล่นด้วย ไปหาเอมิแล้วกัน คิดงี้อยู่ละสิ"

# "She actually looks angry."
"ดูเอมิจะโกรธจริง ๆ"

# "A chance for some teasing of my own presents itself."
"ได้โอกาสฉันแกล้งเธอบ้างล่ะ"

# hi "Actually, yeah, I guess you are."
hi "ก็ใช่แหละ คงงั้น"

show emi sad_annoyed_gym_ss
with charachange

# "Emi pouts, widening her eyes to give the maximum amount of puppy-dog resemblance."
"เอมิทำแก้มป่องพร้อมตาโตให้ดูเหมือนลูกหมาน้อยอย่างถึงที่สุด"

# hi "Kidding! I was kidding!"
hi "ล้อเล่น! ฉันล้อเล่น!"

show emi basic_closedgrin_gym_ss
with charachange

# emi "So you are down here to stalk me!"
emi "เนี่ย นายมาตามสตอล์กฉันจริงด้วย!"

# "Wait, what?"
"เดี่ยว อะไร"

# hi "That's not what I meant!"
hi "ไม่ได้หมายความว่าอย่างนั้น!"

# hi "Why would I stalk you anyway? It's not like you require stalking."
hi "ฉันจะตามสตอล์กเธอทำไม ใช่ว่าเธอจะต้องให้ใครมาตามดูที่ไหน"

# hi "If you're not asleep or in class, you're down here, right?"
hi "เธอน่ะ ถ้าไม่หลับหรือเรียนอยู่ก็ต้องอยู่ที่นี่แหละ ใช่มั้ยล่ะ"

# "Emi laughs at this comment."
"เอมิหัวเราะที่ฉันบอกไปอย่างนั้น"

show emi basic_happy_gym_ss
with charachange

# emi "Well, you're not all wrong, I suppose - but you forgot about eating. I do that too, you know."
emi "ก็ไม่ผิดเสียทีเดียวละนะ แต่นายลืมเรื่องกินไป ฉันก็กินข้าวนะ"

# "I nod, conceding the point."
"ฉันพยักหน้าเห็นด้วย"

show emi sad_grin_gym_ss
with charachange

# emi "Plus I hang out with Rin sometimes too… so really I might take some effort to stalk."
emi "อีกอย่าง บางทีฉันก็ไปอยู่กับรินเหมือนกัน… เพราะงั้นจะตามตัวฉันก็ไม่ได้ง่ายขนาดนั้น"

# hi "What do you two do together anyway? You don't seem to have a lot in common."
hi "แล้วเธอสองคนทำอะไรกัน เหมือนนิสัยจะเป็นคนละแบบกันเลยนะ"

show emi basic_closedgrin_gym_ss
with charachange

# "She puts her hands on her hips and assumes a superior air."
"เอมิยืนเท้าสะเอวทำท่าเหนือกว่า"

show emi basic_grin_gym_ss
with charachange

# emi "That's what you think. I've got all sorts of hidden hobbies, you know."
emi "นายคิดไปเองไงล่ะ ฉันมีงานอดิเรกลับเยอะแยะเลยนะ"

# hi "Oh really? Like what?"
hi "จริงเหรอ เช่นอะไรล่ะ"

show emi sad_grin_gym_ss
with charachange

# "Emi puts her head to one side, as if she's trying to remember what it is she does in her free time."
"เอมิเอียงคอคิดราวกับกำลังนึกอยู่ว่าเวลาว่างตัวเองทำอะไร"

show emi basic_closedgrin_gym_ss
with charachange

# emi "Well, Rin and I go out shopping sometimes."
emi "ก็ บางทีรินกับฉันก็ไปซื้อของด้วยกัน"

# "I guess that makes sense. Emi's a girl, after all. But Rin?"
"ก็สมเหตุสมผลแหละ เอมิเป็นผู้หญิงนี่นะ แต่รินเนี่ยนะจะซื้อของ"

# hi "Rin comes with you?"
hi "รินไปด้วยเหรอ"

show emi basic_grin_gym_ss
with charachange

# emi "We usually swing by the art supply store."
emi "ปกติไปร้านขายอุปกรณ์ศิลปะน่ะ"

# emi "Plus she likes this music store that sells all kinds of weird sounding stuff."
emi "แล้วรินก็ชอบไปร้านดนตรีที่มีเครื่องดนตรีแปลก ๆ เยอะแยะเลย"

show emi basic_closedhappy_gym_ss
with charachange

# emi "She says it helps focus her."
emi "เห็นบอกว่าช่วยให้มีสมาธิขึ้นน่ะ"

# "That makes a little more sense."
"ก็ดูฟังขึ้นขึ้นมาหน่อย"

# hi "I see. Any other hidden hobbies?"
hi "อย่างนี้นี่เอง มีงานอดิเรกลับอื่นอีกมั้ย"

show emi excited_proud_gym_ss
with charachange

# "Emi wags a finger at me."
"เอมิส่ายนิ้ว"

# emi "Now now, why would I go and reveal all my dark secrets to you? We hardly know one another!"
emi "เอ้า ๆ ทำไมฉันจะต้องมาเปิดความลับดำมืดทั้งหมดให้นายเห็นด้วย เราเพิ่งจะมารู้จักกันเองนะ!"

# "Somehow I think that's all that Emi has in the way of hobbies."
"ไม่รู้ทำไมถึงรู้สึกว่าเอมิก็มีงานอดิเรกอยู่แค่นี้แหละ"

# "Still, I don't think my question's been answered."
"แต่เหมือนที่ถามไปจะยังไม่ได้คำตอบเลย"

# hi "Even if you do have a few hobbies, I still don't see why you hang out with Rin so much."
hi "ต่อให้มีงานอดิเรกน้อย ฉันก็ยังไม่เข้าใจอยู่ดีว่าทำไมเธอถึงอยู่กับรินบ่อยขนาดนั้น"

# hi "I mean, she's kind of weird, isn't she?"
hi "ก็รินเป็นคนแปลก ๆ นี่ ใช่มั้ย"

# "This comment causes Emi to laugh loudly."
"คำพูดนั้นทำให้เอมิหัวเราะออกมาดัง ๆ"

show emi basic_closedhappy_gym_ss
with charachange

# emi "Ha! That's the understatement of the year!"
emi "ฮ่า! แค่ว่าแปลกยังน้อยไปเลยนะ!"

# hi "So why? I mean, you're a lot better at conversation and stuff, so I figure you'd hang out with a lot of people, but I think I've only ever seen you with Rin."
hi "สรุปเพราะอะไรล่ะ คือเธอก็เป็นคนคุยเก่งมาก เลยนึกว่าจะไปเป็นเพื่อนกับใครหลายคน แต่เหมือนจะเห็นเธออยู่\nแค่กับรินเองมั้ง"

show emi sad_annoyed_gym_ss
with charachange

# "Emi seems unusually defensive."
"เอมิดูไม่พอใจผิดวิสัย"

# emi "Hey, I hang out with plenty of people that aren't Rin! You just don't see me doing it because I'm not in your classes."
emi "นี่ ฉันก็อยู่กับคนอื่นที่ไม่ใช่รินเหมือนกันนะ! นายแค่ไม่เห็นเพราะอยู่คนละห้องกันต่างหาก"

# hi "Okay, but that still doesn't explain why you hang out with Rin."
hi "โอเค แต่ก็ยังไม่ได้คำตอบอยู่ดีว่าทำไมเธอถึงอยู่กับริน"

# "I'm not even sure why I want to know this."
"ฉันก็ไม่แน่ใจเหมือนกันว่าทำไมถึงอยากรู้"

# "I guess it is because lunch was so strange."
"เพราะมื้อเที่ยงที่ผ่านมามันแปลกมากมั้ง"

show emi basic_confused_gym_ss
with charachange

# "Emi shrugs, looking for a moment very Rin-ish."
"เอมิยักไหล่ เห็นแล้วทำให้นึกถึงริน"

stop music fadeout 4.0

# emi "It's because we have similar outlooks."
emi "เพราะเรามีอะไรคล้ายกันไง"

# "If you were to ask me the least likely answer to my question, that would be it."
"ถ้าจะบอกว่าคำตอบที่ฉันคาดไม่ถึงเลยคืออะไรก็คงเป็นประโยคนี้แหละ"

# hi "What do you mean?"
้hi "หมายความว่าไง"

# emi "It's like…"
emi "ก็แบบว่า…"

play music music_emi fadein 1.0

show emi basic_grin_gym_ss
with charachange

# emi "Okay, Rin paints and stuff, right?"
emi "รินน่ะวาดรูปใช่มั้ย"

# hi "Yes…"
hi "ใช่…"

# "I'm not sure where this is going."
"ยังดูไม่ออกว่าจะพูดยังไงต่อ"

show emi basic_closedgrin_gym_ss
with charachange

# emi "Well, I run."
emi "ส่วนฉันก็วิ่ง"

# hi "And?"
hi "แล้ว?"

show emi basic_happy_gym_ss
with charachange

# emi "And… that's why we're similar."
emi "และ… นั่นแหละเราถึงได้คล้ายกัน"

hi "…"

# hi "You lost me."
hi "ยังไงนะ"

show emi basic_annoyed_gym_ss
with charachange

# "Emi frowns, as if trying to figure out her answer."
"เอมิขมวดคิ้วราวกับกำลังคิดหาคำตอบ"

# emi "Well, maybe it's that we do things for the same reasons."
emi "ก็อาจจะเป็นเพราะว่าเราทำอะไร ๆ ด้วยเหตุผลที่เหมือนกันน่ะ"

# hi "Huh?"
hi "หือ?"

show emi sad_grin_gym_ss
with charachange

# emi "You know, we follow our passions."
emi "ก็แบบ เราทำอะไรตามความอยากของตัวเองน่ะ"

# hi "So you're passionate about running and Rin's passionate about art, is that it?"
hi "ก็คือเธอสนใจการวิ่ง ส่วนรินก็สนใจศิลปะ แค่นั้น?"

# emi "Well, sort of. Let me think…"
emi "อืม ก็ประมาณนั้น ขอคิดก่อนนะ…"

show emi basic_closedgrin_gym_ss
with charachange

# emi "Well, Rin explained it to me once, but I don't know how much of it I followed."
emi "คือรินเคยอธิบายให้ฟังอยู่หนหนึ่งนะ แต่ไม่รู้ว่าฉันเข้าใจมากแค่ไหน"

# "Not surprising. I think any explanation from Rin would probably confuse anyone."
"ไม่แปลก ฉันว่าใครได้ฟังคำอธิบายของรินก็ต้องงงกันทั้งนั้น"

show emi basic_grin_gym_ss
with charachange

# emi "She says we both chase after an extreme."
emi "รินบอกว่าเราต่างไขว่คว้าหาจุดปลายสุด"

# emi "Like, she's always trying to find a new way to show a particular feeling or something."
emi "แบบ รินก็จะสรรหาวิธีใหม่ ๆ ในการแสดงความรู้สึกหรืออะไรประมาณนั้นตลอด"

show emi sad_grin_gym_ss
with charachange

# emi "And I run because of the feeling I get from it."
emi "และฉันก็วิ่งเพราะฉันชอบความรู้สึกตอนวิ่ง"

# emi "And since we don't allow ourselves to be slowed down by anything, we make a connection based on that."
emi "และเพราะเราต่างไม่ยอมให้อะไรมาฉุดรั้งตัวเอง เราถึงเชื่อมต่อถึงกันได้"

# hi "What do you mean “slowed down by anything?”"
hi "“ไม่ยอมให้อะไรมาฉุดรั้ง” นี่คืออะไรเหรอ"

show emi basic_confused_gym_ss
with charachange

# "Emi looks surprised and points to her legs."
"เอมิทำหน้าประหลาดใจก่อนจะชี้ไปที่ขา"

# emi "You know, because I'm a runner. And Rin's a painter even without arms."
emi "ก็เนี่ย เพราะฉันเป็นนักวิ่ง ส่วนรินก็เป็นศิลปินโดยไม่มีแขน"

# emi "So we respect each other's determination."
emi "เราถึงได้นับถือความมุ่งมั่นของกันและกัน"

show emi basic_closedhappy_gym_ss
with charachange

# emi "And that's why we hang out."
emi "และเพราะแบบนี้เราถึงได้อยู่ด้วยกัน"

show emi sad_grin_gym_ss
with charachange

# emi "I think."
emi "คิดว่านะ"

# "Well, I'm not sure that made any sense to me… but from Emi's sheepish expression, she's not sure about it either."
"อืม ฉันก็ไม่แน่ใจเท่าไหร่ว่าเข้าใจหรือเปล่า… แต่ดูจากสีหน้าแหย ๆ ของเอมิแล้วเจ้าตัวเองก็คงไม่แน่ใจเหมือนกัน"

# emi "Honestly, it's not something I think about much."
emi "เอาตรง ๆ นะ ฉันก็ไม่ได้มานั่งคิดอะไรแบบนี้หรอก"

# emi "We just get along - I think that's really all that matters."
emi "ฉันว่าขอแค่เราเข้ากันได้ก็พอแล้วละ"

# "I suppose she's got a point there."
"ก็คงจริงอย่างเอมิว่า"

# "Another question strikes me, and since I've got nothing better to do, I ask it."
"แล้วฉันก็นึกสงสัยขึ้นมาอีกอย่าง และเพราะไม่มีอะไรจะทำแล้วจึงถามออกไป"

# hi "So what got you so into running, anyway?"
hi "แล้วไปไงมาไงถึงได้มาวิ่ง"

show emi basic_closedgrin_gym_ss
with charachange

# emi "Oh, I've been running since I was really little!"
emi "อ๋อ ฉันวิ่งมาตั้งแต่ยังเป็นเด็กตัวเล็ก ๆ แล้วล่ะ!"

show emi basic_grin_gym_ss
with charachange

# emi "My dad was a runner, and so as soon as I could walk, he started teaching me how to run."
emi "พ่อของฉันเป็นนักวิ่ง แล้วพอฉันเดินได้ปุ๊บ พ่อก็หัดให้ฉันวิ่งปั๊บ"

show emi sad_grin_gym_ss
with charachange

# emi "It was our father/daughter thing, you know?"
emi "แบบพ่อสอนลูกอะไรแบบนี้ไง"

show emi sad_depressed_gym_ss
with charachange

stop music fadeout 10.0

# emi "Our own mutual hobby."
emi "เป็นงานอดิเรกร่วมของเรา"

# "A shadow crosses her face, and I'm shocked to see her looking… sad."
"เอมิทำหน้าหม่นไป ซึ่งฉันก็ตกใจที่เห็นเอมิทำหน้า… เศร้า"

# "Did something happen between them?"
"มีเรื่องอะไรเกิดขึ้นงั้นเหรอ"

show emi basic_shock_gym_ss
with charachange

# emi "Man, I don't have a lot of time left."
emi "ตายละ เหลือเวลาไม่มากแล้ว"

show emi basic_closedsweat_gym_ss
with charachange

# emi "Sorry, but I've got to get a few more laps in before I go see the nurse!"
emi "ขอโทษที เดี๋ยวต้องวิ่งต่ออีกสักสองสามรอบก่อนไปหาคุณพยาบาลแล้วละ"

play ambient sfx_emipacing

hide emi
with easeoutleft

$ renpy.music.set_volume(0.3, 1.0, channel="ambient")

# "She races off around the track, hair streaming in the wind."
"เอมิพุ่งตัวไปที่ลู่พร้อมผมที่พลิ้วไสวไปตามสายลม"

# "It seems to me she's going a lot faster than she was this morning."
"เหมือนจะเร็วขึ้นกว่าเมื่อเช้าเยอะเลย"

# "As she rounds the track, I catch a glimpse of her face."
"พอเอมิออกวิ่งฉันก็เห็นสีหน้าเธออยู่ไว ๆ"

scene ev emi_run_face_zoomout_ss
with locationchange

# "It's much the same as it was this morning, but her eyes seem to have taken on a harder edge."
"เป็นสีหน้าเหมือนอย่างเมื่อเช้า แต่ดวงตาเธอดูจริงจังขึ้น"

# "I guess she's right."
"คงจะจริง"

# "I don't really know much about her."
"ที่ว่าฉันไม่ค่อยรู้เรื่องของเอมิเท่าไหร่"

scene bg school_track_ss
with locationchange

# "I watch her run for a little while and then stand up to head back to my room."
"ฉันนั่งดูเธอวิ่งอยู่อีกพักหนึ่งก่อนจะยืนขึ้นแล้วเตรียมเดินกลับห้อง"

# emi "Hey!"
emi "นี่!"

# "She spots me leaving and waves to catch my attention."
"เอมิเห็นฉันลุกขึ้นจึงโบกมือเรียก"

# emi "Don't forget! Same time tomorrow morning, got it?"
emi "พรุ่งนี้เช้าเวลาเดิม อย่าลืมล่ะ!"

# hi "Got it."
hi "เข้าใจแล้ว"

stop ambient fadeout 2.0

# "I head back to my room."
"ฉันกลับไปที่ห้อง"

# "Homework beckons."
"ที่ที่ซึ่งมีการบ้านรออยู่"

########################################################
label th_E6:

scene bg school_track_ss
with None

scene bg school_dormhisao_ni
with shorttimeskip

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")

# "I can't sleep."
"นอนไม่หลับ"

# "My body's tired, but my mind is kept awake, staring at the ceiling in the hollow darkness of my room."
"ร่างกายอ่อนเพลีย แต่สมองยังตื่นอยู่ ฉันนอนมองเพดานมืดสนิทในห้อง"

# "I grasp desperately for a thread of thought, hoping that I can run my brain into the ground."
"ฉันเค้นสมองหาเรื่องคิดด้วยหวังว่าจะหาอะไรให้สมองคิดเพลิน ๆ ได้"

# "All I can think of is how I can't think of anything."
"แต่ก็คิดได้แต่ว่าฉันคิดอะไรไม่ออก"

# "This is not productive at all."
"ไม่ได้อะไรขึ้นมาเลย"

# "I wonder if this is a side effect of my medication, though it seems odd for it to take so long to show up."
"หรือจะเป็นผลข้างเคียงของยา แต่เพิ่งแสดงผลเอาป่านนี้ก็คงไม่ใช่"

# "Then again, maybe I'm just not as used to my new surroundings as I'd like to think."
"แต่ก็นะ ฉันยังไม่ได้ชินกับสภาพแวดล้อมใหม่ขนาดนั้นอย่างที่คิด"

# "I don't know, but for whatever reason, I'm awake and I shouldn't be."
"ไม่รู้สิ ไม่รู้ว่าเพราะอะไรฉันถึงได้ไม่หลับทั้งที่ควรจะหลับไปแล้ว"

# "This is ridiculous."
"บ้าไปแล้ว"

play sound sfx_switch

scene bg school_dormhisao
with Dissolve(0.2)

# "Ignoring my body's stiffness, I get out of bed and look at my clock."
"ฉันลุกออกจากเตียงมาดูนาฬิกาโดยไม่สนร่างกายที่ยังขยับไม่คล่องนัก"

# "Four in the morning. Last time I checked it was only one, so maybe I slept a little."
"ตีสี่ ที่มาดูล่าสุดเป็นตอนตีหนึ่ง คงจะได้นอนไปนิดเดียว"

# "I don't know."
"ไม่รู้สิ"

# "I throw on some clothes and head out of my room."
"ฉันใส่เสื้อผ้าแล้วออกมาจากห้อง"

# "A walk might do me some good."
"เดินสักหน่อยน่าจะดี"

scene bg school_courtyard_ni
with locationskip

# "I'm surprised at how chill the air is compared to the relative warmth of the day."
"ฉันนึกแปลกใจกับอากาศที่เย็นเยือกผิดกับความอบอุ่นเมื่อตอนกลางวัน"

# "I can almost see my breath as I wander the campus, waiting for the sun to come up or for me to fall asleep."
"ฉันเห็นลมหายใจของตัวเองเป็นไอสีขาวระหว่างที่เดินตระเวนในโรงเรียนรอให้พระอาทิตย์ขึ้นไม่ก็รอให้หลับก่อน"

# "At this point, either option works for me."
"อย่างไหนจะเกิดก่อนก็ได้ทั้งนั้นแหละ"

scene bg school_track_ni at left
with locationchange

# "I find myself at the track - where for the first time, Emi's not out running."
"ฉันเดินมาถึงลู่วิ่ง ซึ่งเป็นครั้งแรกที่ไม่เห็นเอมิมาวิ่ง"

# "I suppose that makes sense; it's too early, even for her."
"ก็คงไม่แปลก ตอนนี้ยังเช้ามาก แม้แต่กับเอมิด้วย"

# "The bleacher seats are cold, but at this point I welcome the sensation."
"ที่นั่งบนสแตนด์เชียร์นั้นเย็นเยียบ แต่ตอนนี้นั่งเย็น ๆ แบบนี้ก็ดี"

show bg school_track as overlay:
    left
    alpha 0.0
    linear 15.0 alpha 0.5
with None

# "The sun is starting to show its face over the horizon, and I know with an awful certainty that I'll get no more sleep tonight."
"พระอาทิตย์เคลื่อนพ้นขอบฟ้าขึ้นมาแล้ว และฉันก็รู้ดีเหลือเกินว่าคืนนี้ฉันจะไม่ได้หลับอีกแน่นอน"

# "The sun's steadily strengthening rays start to warm me up, and I watch the dew on the ground begin to steam slightly."
"พระอาทิตย์ฉายแสงแรงขึ้นเรื่อย ๆ จนตัวฉันอุ่น ฉันมองน้ำค้างบนพื้นที่เริ่มระเหยไป"

# "My mind calms down, a little."
"ใจฉันสงบลงบ้าง"

stop music fadeout 2.0

scene black
with shuteye

window hide

with Pause(3.0)

play sound sfx_rustling

window show hpunch

# "Someone's shaking me."
"มีคนมาเขย่าตัวฉัน"

# emi "Hey, wake up!"
emi "นี่ ตื่นสิ!"

# hi "Huh? Where? Wha?"
hi "เหอ? ที่ไหน ฮะ?"

scene bg school_track
show emi basic_shock_gym_close at center
with openeyefast

# "I guess I fell asleep after all."
"สงสัยจะผล็อยหลับไปจริง ๆ"

show emi basic_annoyed_gym_close
with charachange

# emi "What are you doing out here? You're going to catch a cold or something!"
emi "นี่นายออกมาทำอะไรเนี่ย เดี๋ยวก็เป็นหวัดเอาหรอก"

play music music_dreamy fadein 4.0

# "I rub my eyes and am confronted by Emi, who bends over me with a worried expression."
"ฉันขยี้ตา เอมิมองฉันอยู่ด้วยสีหน้าเป็นกังวล"

# "I'm still a little groggy, so my response comes out in a mumble."
"ฉันยังงัวเงียอยู่เล็กน้อยจึงได้เพียงพึมพำตอบไป"

# hi "Couldn't sleep. Watched the sun come up."
hi "นอนไม่หลับ ดูพระอาทิตย์ขึ้น"

show emi basic_confused_gym_close
with charachange

# emi "Sounds like something Rin would say."
emi "พูดอะไรเป็นรินไปได้"

# "I shrug, feeling the stiffness that comes with sleeping on a bench for a few hours."
"ฉันยักไหล่พร้อมกล้ามเนื้อที่ยังยึดจากการหลับบนที่นั่งอยู่สองสามชั่วโมง"

# hi "Is it? I wouldn't know."
hi "เหรอ ไม่ยักรู้"

show emi basic_grin_gym_close
with charachange

# "Emi grins a little at my (somewhat cranky) response."
"เอมิยิ้มน้อย ๆ ให้คำตอบ (ที่ฟังดูอ้อแอ้) นั้น"

show emi basic_closedgrin_gym_close
with charachange

# emi "So, couldn't sleep, eh? Obviously we need to run you harder today!"
emi "นอนไม่หลับงั้นเหรอ งั้นวันนี้ต้องวิ่งให้หนักกว่าเก่าแล้ว!"

# "Even though I've only known her for about a week, this seems a very Emi-ish response to the problem."
"ถึงจะเพิ่งรู้จักกันมาได้สัปดาห์เดียว แต่ก็ฟังดูเป็นการแก้ปัญหาที่สมเป็นเอมิดี"

# hi "Hey, my body was plenty exhausted after yesterday!"
hi "เฮ้ย เมื่อวานฉันก็เพลียจะตายอยู่แล้ว"

# hi "My mind was just racing, that's all."
hi "แค่สมองฉันมันไม่ยอมหลับเฉย ๆ"

show emi basic_confused_gym_close
with charachange

# emi "I don't see the difference. If you run hard enough, your brain will get tired too."
emi "ก็เหมือนกันนี่ ถ้าวิ่งหนัก ๆ เข้าเดี๋ยวสมองก็จะเพลียเอง"

# "I'm seriously questioning the wisdom of doing this first thing in the morning."
"ฉันชักจะไม่แน่ใจแล้วว่าดีจริง ๆ เหรอที่มาวิ่งกันแต่เช้าเนี่ย"

# "I don't know if my grades will be able to handle me tiring my brain out like that."
"ไม่รู้ว่าถ้าสมองเพลียไปแล้วจะยังรักษาผลการเรียนไหวหรือเปล่า"

show emi basic_closedgrin_gym_close
with charachange

with vpunch

show emi basic_closedgrin_gym
with charadistant

# "Emi pulls me up from the bleachers with surprising strength for someone her size."
"เอมิลากฉันออกจากสแตนด์เชียร์ด้วยแรงที่เยอะผิดขนาดตัว"

# emi "Now come on, Hisao! We've got work to do!"
emi "ไม่เอาน่าฮิซาโอะ! เรายังมีเรื่องที่ต้องทำกันอยู่นะ!"

# "I don't actually know if I'm up to this today, to be honest."
"เอาตรง ๆ ฉันก็ไม่แน่ใจว่าวันนี้ฉันพร้อมวิ่งหรือเปล่า"

# "I mean I obviously didn't get much sleep… and what sleep I got was on the bleachers!"
"คือชัดอยู่ว่าฉันนอนน้อย… แล้วแถมที่นอนไปก็มานอนบนสแตนด์เชียร์เนี่ย"

# hi "I don't know… should I really be running?"
hi "ไม่รู้สิ… ฉันต้องวิ่งด้วยเหรอ"

show emi basic_annoyed_gym
with charachange

# "Emi glares at me."
"เอมิจ้องฉันเขม็ง"

# "Good heavens."
"ให้ตายเถอะ"

show emi sad_annoyed_gym
with charachange

# emi "What are you talking about? Of course you should be running!"
emi "พูดอะไรของนาย นายต้องวิ่งอยู่แล้วสิ!"

# emi "How else do you expect to work out the kinks?"
emi "ไม่งั้นปัญหามันจะหายไปได้ยังไง"

show emi basic_annoyed_gym
with charachange

# emi "You've been sleeping on the bleachers, for heaven's sake!"
emi "นายมาหลับอยู่บนสแตนด์เชียร์เนี่ยนะ จะบ้าตาย!"

# emi "The best way to get that soreness out is to run around a little."
emi "ถ้าจะให้หายเมื่อยก็ต้องวิ่งกันสักหน่อยนี่แหละ"

# emi "Now stop hiding in the bleachers and get down here!"
emi "ทีนี้ก็เลิกซ่อนตัวอยู่กับสแตนด์เชียร์แล้วลงมาได้แล้ว!"

# "There's no arguing that. I'm pretty sure she'd kill me if I didn't do as she said."
"ไม่เถียง ฉันว่าถ้าไม่ทำตามที่บอกเอมิคงเอาฉันตายแน่"

# "I get to my feet and hop down to the track."
"ฉันลุกขึ้นยืนแล้วโดดลงมาที่ลู่"

scene bg school_track_on
with locationchange

# "The sun is warming things up rather nicely, I think."
"พระอาทิตย์ส่องแสงให้อะไร ๆ อุ่นขึ้นแล้วละนะ"

# "Emi and I begin to stretch out, and I find myself once again hard pressed not to stare."
"เอมิกับฉันเริ่มยืดเส้นยืดสายกัน และฉันก็ต้องห้ามใจอย่างหนักไม่ให้มองเหมือนเดิม"

# "If this is how I have to wake up every day, I might be able to get used to this."
"ถ้าต้องตื่นแบบนี้ทุกวันฉันอาจจะชินก็ได้"

show emi basic_annoyed_gym
with charachange

# emi "You know Hisao, it's not polite to stare."
emi "เนี่ยนะฮิซาโอะ จ้องคนอื่นมันหยาบคายนะ"

# hi "I wasn't staring! I swear!"
hi "ไม่ได้จ้อง! สาบานเลย!"

# "Emi raises an eyebrow and considers me for a minute, as if evaluating my response."
"เอมิเลิกคิ้วพินิจฉันอยู่ครู่หนึ่งคล้ายประเมินคำตอบฉันอยู่"

# "There's a brief moment where I'm afraid for my life."
"แวบหนึ่งฉันกลัวตายขึ้นมา"

show emi basic_closedhappy_gym
with charachange

# "But then she smiles and laughs, shaking her head slowly."
"แต่เอมิก็ยิ้มแล้วหัวเราะพลางส่ายหน้าช้า ๆ"

show emi basic_grin_gym
with charachange

# emi "Honestly, you didn't have to deny it so strenuously."
emi "เอาตรง ๆ นะ ไม่ต้องปฏิเสธจริงจังขนาดนั้นหรอก"

stop music fadeout 5.0

# "In response, I clap my hands together and go for a change of subject."
"ฉันตบมือเปลี่ยนเรื่องต่อ"

# hi "So! That's enough stretching, right?"
hi "โอเค! ยืดเส้นกันพอแล้วเนอะ"

show emi sad_grin_gym
with charachange

# "Emi gives a casual shrug."
"เอมิยักไหล่สบาย ๆ"

# emi "Do you feel stretched? That's really how you tell."
emi "รู้สึกได้ยืดบ้างหรือยังล่ะ ปกติจะดูว่ายืดพอหรือยังก็ดูแบบนั้นแหละ"

# "Well, I do feel up to the run, if that's what she means."
"อืม ก็รู้สึกพร้อมวิ่งแล้วนะ ถ้าหมายความว่าอย่างนั้น"

# hi "Yeah, I feel ready to go."
hi "อื้ม พร้อมแล้ว"

show emi basic_grin_gym
with charachange

# emi "Same as yesterday, okay?"
emi "เหมือนเมื่อวานนะ"

# emi "We'll just run for a mile at a steady pace."
emi "วิ่งให้สม่ำเสมอให้ครบหนึ่งพันหกร้อยเมตร"

show emi basic_closedhappy_gym
with charachange

# emi "Don't worry about going really fast, just worry about keeping the pace, got it?"
emi "ไม่ต้องห่วงเรื่องความเร็วหรอก แค่คอยรักษาฝีเท้าให้คงที่ก็พอ โอเคนะ"

# hi "You're the boss."
hi "เธอว่าไงก็ว่างั้น"

play music music_running fadein 0.5

show emi basic_grin_gym
with charachange

play ambient sfx_emijogging

hide emi
with charamoveoutleft

$ renpy.music.set_volume(0.5, 2.0, channel="ambient")

# "Emi grins again, and we take off around the track."
"เอมิยิ้มอีกครั้งก่อนที่เราจะออกวิ่ง"

scene bg school_track_running
with Dissolve(2.0)

"…"

"…"

# "I think I'm going to die."
"ฉันว่าฉันจะตายแล้ว"

# "We're not even done with the first lap, and my legs are on fire."
"ยังไม่ถึงหนึ่งรอบเลย แต่ขาฉันเหมือนจะสุกแล้ว"

# "My breath is coming in ragged gasps."
"ลมหายใจฉันเริ่มหอบถี่"

# "I can feel sweat pouring down my brow, and we've only just now rounded the second turn."
"เหงื่อผุดขึ้นที่คิ้ว ตอนนี้เพิ่งผ่านโค้งที่สองมาเอง"

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

show emi basic_closedgrin_gym at left
with charamoveinleft

# emi "Come on, Hisao! You've got three more laps to go!"
emi "มาสิฮิซาโอะ! ยังเหลืออีกสามรอบนะ!"

$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

hide emi
with easeoutleft

# "I can't do this…"
"ไม่ไหวแล้ว…"

# "I can't do this."
"ไม่ไหวแล้ว"

# "I can't do this!"
"ไม่ไหวแล้ว!"

# "I think I might hurl."
"เหมือนจะอ้วก"

# "Somehow we're on the second lap. Emi's not even sweating."
"เข้าสู่รอบที่สองแล้ว เอมิยังไม่เหงื่อออกเลยด้วยซ้ำ"

# "How can she do this so effortlessly?"
"ทำไมวิ่งได้สบายขนาดนั้นนะ"

# "For some reason I'm still moving."
"ไม่รู้ทำไมขาฉันถึงยังขยับได้"

# "She's like a machine."
"เอมิเหมือนเครื่องจักรกลเลย"

# "Third lap. What happened to the second?"
"รอบที่สาม เกิดอะไรขึ้นในรอบที่สองนะ?"

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

show emi excited_proud_gym at left
with charamoveinleft

# emi "Almost there, Hisao!"
emi "อีกนิด ฮิซาโอะ!"

$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

hide emi
with easeoutleft

# "Liar! We've got another two!"
"โกหก! เหลืออีกตั้งสองรอบ!"

# "Nothing to be done."
"ทำอะไรไม่ได้แล้ว"

# hi "I… ca… can't… do… this."
hi "ไม่… วะ… ไหว… แล้ว"

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

show emi basic_annoyed_gym
with charamoveinleft

# "Emi whirls around and begins running backwards."
"เอมิหมุนตัวแล้วออกวิ่งถอยหลัง"

# "Her face is a mask of anger that surprises me."
"สีหน้าของเธอเป็นความโกรธที่ทำให้ฉันแปลกใจ"

show emi sad_angry_gym
with charachange

# emi "Never say that!"
emi "ห้ามพูดอย่างนั้น!"

# emi "If you say that, you'll have already lost."
emi "ถ้าพูดอย่างนั้นก็แปลว่านายแพ้แล้ว"

show emi sad_angry_gym at left
with charamove

# emi "Keep moving! If you're alive, you can keep moving, dammit!"
emi "ไปเรื่อย ๆ ! ถ้ายังไม่ตายก็ไปต่อได้นะ ปัดโธ่!"

$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

hide emi
with easeoutleft

# "Whoa, language. We're on the fourth lap now."
"คำพูดคำจา รอบที่สี่แล้ว"

# "She really seems to want me to keep going."
"ดูท่าจะอยากให้ฉันไปต่อจริง ๆ"

# "Legs move. Move. Move. They feel so sluggish."
"ขยับขา ขยับ ขยับ หน่วงเหลือเกิน"

# "I'm in mud, or molasses, or tar."
"เหมือนติดโคลน น้ำตาลหนืด ทาร์"

# "I can't go on."
"ไปต่อไม่ได้แล้ว"

# "I'll go on."
"ฉันจะไปต่อ"

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

show emi basic_grin_gym at left
with charamoveinleft

# emi "Final stretch, Hisao! Give it all you've got!"
emi "โค้งสุดท้ายแล้วฮิซาโอะ! ใส่เต็มที่เลย!"

$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

hide emi
with easeoutleft

# "I pump my legs as fast as they'll go."
"ฉันออกแรงขาไปให้เร็วที่สุดเท่าที่ทำได้"

# "They keep refusing to obey my commands."
"ขายังไม่ยอมเชื่อฟังที่ฉันสั่ง"

# "Somehow, I keep moving."
"ไม่รู้ทำไมฉันถึงยังไปต่อได้"

# "Somehow, I finish."
"ไม่รู้ทำไมฉันถึงเข้าเส้นชัยได้"

stop ambient fadeout 0.5

show emi excited_happy_gym at center
with charaenter

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")

# emi "That's it, Hisao! I knew you had it in you!"
emi "นั่นแหละฮิซาโอะ! ว่าแล้วเชียวว่านายต้องทำได้!"

# "The anger Emi showed a lap ago is gone, replaced with pride."
"ความโกรธที่เอมิแสดงให้เห็นเมื่อรอบที่แล้วนั้นหายไปและถูกแทนที่ด้วยความภาคภูมิ"

# "She's positively radiant, like she just won the gold medal or something."
"สีหน้าดูสดใสเหมือนเพิ่งชนะรางวัลเหรียญทองหรืออะไรมา"

scene bg school_track_on
show emi excited_happy_gym at center
with vpunch

# "I stagger to a stop and fall to my hands and knees, gasping for air."
"ฉันโซซัดโซเซมาแล้วทรุดตัวลงใช้มือกับเข่ายันตัวไว้พลางอ้าปากหายใจ"

# "My heart is pounding far harder than it has in a long time."
"ใจฉันเต้นแรงกว่าทุกทีมากอย่างที่ไม่เคยรู้สึกมาแสนนาน"

stop music fadeout 1.0

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack
with Dissolve (0.2)

# "I don't think it's done this since…"
"ฉันว่าไม่ได้ทำแบบนี้มาตั้งแต่…"

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack
with Dissolve (0.2)

# "Oh God."
"ตายแล้ว"

scene black
with shuteyefast

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.2)

# "Please slow down, heart."
"ช้า ๆ ก่อนนะหัวใจฉัน"

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.5)

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.2)

# "Just slow down. Stop racing."
"ช้า ๆ หน่อย เลิกเต้นแรงได้แล้ว"

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.5)

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.2)

# "I cough, and for some reason, feel a grin crossing my face."
"ฉันไอ และไม่รู้ทำไมถึงได้เหยียดยิ้มออกมา"

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.5)

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.2)

# "So this is how I die, huh?"
"ฉันต้องตายแบบนี้สินะ"

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.5)

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.2)

# "Trying to stay healthy?"
"จะรักษาสุขภาพเหรอ"

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.5)

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.2)

# "How ironic."
"ย้อนแย้งเป็นบ้า"

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.5)

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.5)

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.2)

# "I'm all ready to give up right there."
"ฉันพร้อมจะสิ้นลมเสียตรงนี้แล้ว"

play sound sfx_heartslow
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.8)

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack
with Dissolve (0.8)

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack
with Dissolve (0.2)

# "But then, I feel my heart slow down."
"แต่แล้วหัวใจฉันก็เต้นช้าลง"

# "Two hands grab under my arms and tug upwards."
"มีสองมือมาจับแขนดึงฉันขึ้น"

scene bg school_track_on
show emi basic_confused_gym_close at center
with openeye

# "I look up and see Emi standing over me, with a mixture of delight and worry."
"พอเงยหน้ามองก็เห็นเอมิที่ยืนค้ำหัวอยู่พร้อมสีหน้าพึงใจและเป็นห่วง"

# emi "On your feet!"
emi "ยืนขึ้น!"

show emi sad_grin_gym_close
with charachange

# emi "Come on, you'll never catch your breath that way."
emi "เร็ว มัวแต่อยู่แบบนั้นแล้วยังไงก็หายใจไม่ทันแน่"

# "Somehow, I manage to stand. I try to raise my arms above my head, but they feel like lead."
"ไม่รู้ทำไมฉันถึงยืนขึ้นได้ ฉันจะยกแขนขึ้นเหนือหัว แต่ก็หนักเหมือนมีตะกั่วถ่วง"

# "I start to walk around the track while Emi keeps close to me, like she's afraid I'll fall over or something."
"ฉันเดินไปรอบลู่วิ่งโดยมีเอมิคอยประกบเหมือนกลัวฉันสะดุดล้มหรืออะไร"

# "She may not be far off."
"ซึ่งก็คงคิดถูกแล้วแหละ"

# "I feel terrible, and say so."
"รู้สึกไม่ไหวเลย ฉันพูดออกไป"

show emi basic_closedhappy_gym_close
with charachange

# "Emi laughs."
"เอมิหัวเราะ"

show emi basic_happy_gym_close
with charachange

# emi "But you finished, didn't you?"
emi "แต่ก็วิ่งจนครบได้นี่"

show emi basic_grin_gym_close
with charachange

# emi "You said you couldn't, but you did."
emi "นายบอกว่าไม่ไหว แต่สุดท้ายก็ไหว"

# emi "Isn't that worth it?"
emi "เท่านี้ก็คุ้มแล้วนี่นา"

# "I'm not sure, and I don't really have the breath to say so."
"ไม่แน่ใจ แต่ฉันหายใจไม่ทันพอที่จะพูดได้แล้ว"

# "But that small grin I felt on my face earlier hasn't left."
"แต่รอยยิ้มบนใบหน้าฉันเมื่อครู่นั้นยังไม่หายไป"

# "So what if my heart's weak?"
"หัวใจอ่อนแอแล้วไง"

# "I still survived this morning."
"เช้านี้ฉันยังไม่ตาย"

# "Maybe I'll survive tomorrow, too."
"พรุ่งนี้ฉันก็คงไม่ตาย"

scene bg school_track
with shorttimeskip

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")

play ambient sfx_emisprinting

# "As soon as it becomes apparent that I'm not going to suddenly keel over, Emi takes off on her sprints."
"พอชัดแล้วว่าฉันอาการไม่หนักถึงขั้นที่จะล้มลงไปแบบกะทันหันเอมิก็ออกวิ่ง"

# "I don't know how the hell she can manage to sprint after running a mile, but I guess she's in much better shape than me."
"ไม่รู้ว่าวิ่งต่อไหวได้ยังไงทั้งที่วิ่งมาหลายเมตรขนาดนั้นแล้ว แต่เอมิน่าจะฟิตกว่าฉันเยอะ"

# "Once again, as I walk around the track, I can't help watching Emi sprint."
"ระหว่างที่เดินไปรอบลู่ฉันก็อดมองเอมิวิ่งอีกครั้งไม่ได้"

#maybe need a third variation here, or reuse the second one?

scene ev emi_run_face_zoomin
with locationchange

# "It's weird, but she's like a different person when she's pushing herself."
"แปลก แต่เวลาที่เอมิพยายามแล้วเหมือนเธอกลายเป็นคนละคนเลย"

# "Last time I noticed her eyes, but this time it's her mouth that catches my attention."
"ครั้งก่อนฉันมองตา แต่คราวนี้ฉันสะดุดตากับปาก"

# "She's not wearing her normal grin."
"เอมิไม่ได้ยิ้มอย่างทุกที"

# "She's still smiling, but there's a tightness to it."
"เธอยังยิ้ม แต่มีการเม้มริมฝีปากแน่น"

# "It's almost grim, like she's fighting a losing battle but doesn't care."
"ดูแล้วก็ชวนให้หวั่น ๆ เหมือนกำลังสู้ในศึกที่ไม่ว่าอย่างไรเธอก็จะแพ้แต่ไม่สนใจ"

# "She seems to be running harder, like she did yesterday."
"เหมือนจะวิ่งหนักกว่าเดิมเหมือนอย่างเมื่อวาน"

# "Sweat has started to pour down her face, but she keeps going."
"หน้าเธอเริ่มมีเหงื่อออกแล้ว แต่เอมิยังวิ่งต่อ"

# "Her mouth finally opens as she can no longer get enough air through her nose."
"เอมิอ้าปากออกในที่สุดเมื่อลมหายใจจากทางจมูกไม่พอ"

# "As she passes me once more, legs pumping, arms swinging in time, and her lips slightly parted…"
"เอมิวิ่งผ่านฉันไปอีกครั้ง ขาโจนทะยาน แขนแกว่งตามจังหวะ ริมฝีปากเผยอเล็กน้อย"

# "She looks beautiful."
"งดงามเหลือเกิน"

stop ambient fadeout 2.0

scene bg school_track
with shorttimeskip

play music music_normal fadein 3.0
$ renpy.music.set_volume(1.0, 0.0, channel="ambient")

# "After we've both taken some laps around the track to cool down, Emi changes back to her usual self."
"หลังจากที่เดินรอบลู่วิ่งคูลดาวน์กันแล้วเอมิก็กลับไปเป็นตัวเธอคนเดิม"

# "The transformation I saw in her is gone."
"ความเปลี่ยนแปลงในตัวเธอที่ฉันเห็นเมื่อครู่นั้นหายไปแล้ว"

show emi basic_happy_gym at center
with charaenter

# emi "Not bad today, Hisao."
emi "ไม่เลวเลยนะวันนี้ ฮิซาโอะ"

# "There's almost admiration in her voice."
"น้ำเสียงเอมิเจือความชื่นชม"

# hi "What do you mean? I would have stopped if you hadn't yelled at me."
hi "หมายความว่าไง ถ้าเธอไม่ตะโกนใส่ฉันก็คงหยุดไปแล้ว"

show emi sad_shyblush_gym
with charachange

# "Emi colors a little, seemingly embarrassed about her outburst."
"หน้าเอมิขึ้นสีแดงเรื่อดูจะอาย ๆ ที่ทำตัวอย่างนั้นไป"

# emi "Sorry about that, I just… can't stand to see people give up."
emi "ขอโทษทีนะ คือฉัน… ทนเห็นคนยอมแพ้ไม่ได้น่ะ"

# emi "Especially about something like this."
emi "แล้วยิ่งกับอะไรแบบนี้ด้วย"

show emi sad_grin_gym
with charachange

# emi "Saying “I can't go on” is silly when you're obviously going on while you're saying it."
emi "บอกว่า “ไม่ไหวแล้ว” ทั้งที่เห็น ๆ กันอยู่ว่ายังไปต่อน่ะมันบ้าบอนะ"

# emi "That's what this is all about."
emi "หลัก ๆ แล้วประเด็นก็คือตรงนี้แหละ"

# hi "What, saying silly things?"
hi "คืออะไร พูดอะไรที่บ้าบอเหรอ"

show emi basic_annoyed_gym
with charachange

# "Emi sticks her tongue out at me."
"เอมิแลบลิ้นใส่"

# emi "Idiot. I mean showing that you're alive."
emi "บ้า หมายถึงการที่แสดงให้เห็นว่ายังมีชีวิตอยู่ไง"

# "Showing I'm alive, huh? I didn't know it had to be so painful."
"แสดงให้เห็นว่ายังมีชีวิตอยู่งั้นเหรอ ไม่ยักรู้ว่ามันจะทรมานขนาดนี้"

# "But it does feel pretty good, despite that."
"แต่ถึงจะทรมานก็รู้สึกดีเหมือนกัน"

show emi excited_proud_gym
with charachange

# emi "Besides, this is one of the hardest days."
emi "อีกอย่าง นี่แหละคือวันที่ลำบากที่สุด"

# hi "What do you mean?"
hi "หมายความว่าไง"

show emi basic_grin_gym
with charachange

# emi "Whenever you start a workout, it's difficult the first day, really hard the second day, and then the third day is easier."
emi "พอเริ่มออกกำลังกายแล้ว วันแรกจะยาก วันที่สองจะยากมาก แต่พอวันที่สามแล้วก็จะง่าย"

# emi "You'll still get days that are really hard, but they'll pop up less and less."
emi "ก็ยังมีวันที่ยากมากอยู่ แต่จะค่อย ๆ หายไปเรื่อย ๆ"

# hi "So this will eventually get really easy, huh?"
hi "แล้วสักวันก็จะง่ายมากงั้นเหรอ"

show emi basic_closedhappy_gym
with charachange

# emi "Yeah, of course."
emi "อื้ม แหงสิ"

show emi basic_closedgrin_gym
with charachange

# emi "But then you have to increase the difficulty, or you'll never get ahead."
emi "แต่ต้องเพิ่มความยากไปเรื่อย ๆ นะ ไม่งั้นก็จะไม่พัฒนา"

# emi "You'll just get complacent, and you'll lose the sense of accomplishment."
emi "ไม่งั้นก็จะอิ่มตัว ไม่รู้สึกว่าประสบความสำเร็จอะไรอีก"

# hi "So I'll have to run more than just four laps, huh?"
hi "เพราะงั้นก็จะได้วิ่งมากกว่าสี่รอบสินะ"

show emi excited_proud_gym
with charachange

# emi "Yep! But not for a while - you'll have to be careful, you know."
emi "อื้ม! แต่ก็อีกสักพักแหละ ต้องคอยระวัง ๆ นี่นะ"

# "A thought strikes Emi, and her face lights up."
"เอมิทำหน้าเหมือนนึกอะไรออก"

show emi basic_closedhappy_gym
with charachange

# emi "Got it!"
emi "รู้แล้ว!"

# hi "Got what?"
hi "รู้อะไร"

show emi basic_happy_gym
with charachange

# emi "You can come with me to see the nurse! That way you won't fall over dead or anything!"
emi "มาหาคุณพยาบาลพร้อมกับฉันสิ! จะได้แน่ใจว่านายจะไม่ล้มตายไปเฉย ๆ หรืออะไรน่ะ!"

# "How charming."
"น่าสนมาก ๆ"

# hi "Um… when?"
hi "เอ่อ… ตอนไหนล่ะ"

show emi basic_grin_gym
with charachange

# emi "Right now, of course! You'll need a shower and everything, right? We don't have much time, then!"
emi "ก็ต้องตอนนี้สิ! เดี๋ยวต้องไปอาบน้ำไปอะไรอีกใช่มั้ย งั้นก็เหลือเวลาไม่มากแล้ว!"

# "Grabbing my hand, she's off, pulling me along with her."
"เอมิคว้าแขนฉันลากให้ตามไปด้วย"

stop music fadeout 2.0

########################################################
label th_E7:

scene bg school_nurseoffice
show nurse neutral at center
with shorttimeskip

# nk "My goodness, but you're in a hurry today, aren't you, Emi?"
nk "ตายจริง วันนี้รีบน่าดูเลยนะเอมิ"

play music music_nurse fadein 2.0

# "I have no idea how we got to the nurse's office so fast, but here we are."
"ฉันไม่รู้เลยว่ามาถึงห้องพยาบาลได้เร็วขนาดนี้ได้ยังไง แต่ก็นั่นแหละ"

show nurse neutral at twoleft
show bg school_nurseoffice at bgleft
with charamove

show emi basic_grin_gym at tworight
with charaenter

# "The nurse grins at Emi and seems to completely ignore me."
"คุณพยาบาลยิ้มให้เอมิ เหมือนจะเมินฉันไปเลย"

show nurse grin
with charachange

# nk "You've got plenty of time to take a shower and get to class, you know."
nk "ยังเหลือเวลาให้อาบน้ำก่อนไปเข้าเรียนอีกเยอะเลยนี่"

show nurse concern
with charachange

# nk "There's no need to run through the hallways like that. I could hear you coming a mile away!"
nk "ไม่ต้องวิ่งตามโถงทางเดินมาอย่างนั้นหรอก ฉันได้ยินเสียงเธอวิ่งมาตั้งไกล!"

# "Somehow, it doesn't seem like he's actually scolding Emi at all."
"ไม่รู้ทำไมถึงรู้สึกว่าไม่ได้ดุเอมิเลย"

# "It's like this is a sort of routine between the two of them."
"เหมือนเป็นกิจวัตรของสองคนนี้มากกว่า"

# "Emi does a passable imitation of remorse."
"เอมิทำท่าหงอย ๆ ที่พอใช้ได้"

show emi excited_sad_gym
with charachange

# emi "I'm sorry! I won't ever do it again!"
emi "ขอโทษค่ะ! หนูจะไม่ทำอีกแล้ว!"

show nurse grin
show emi basic_closedhappy_gym
with charachange

# "The nurse and Emi both laugh at some private joke."
"ทั้งคุณพยาบาลทั้งเอมิหัวเราะกับมุกที่รู้กันสองคนนั้น"

show emi basic_grin_gym
show nurse neutral
with charachange

# "Suddenly, it seems that he notices me."
"อยู่ ๆ คุณพยาบาลก็เหมือนเห็นฉัน"

show nurse fabulous
with charachange

# nk "Ah, hello Hisao."
nk "อ้าว สวัสดีฮิซาโอะ"

show nurse neutral
with charachange

# nk "What brings you here?"
nk "ลมอะไรหอบมาถึงนี่ล่ะ"

# hi "Well, I've been—{w=.3}{nw}"
hi "คือผม—{w=.3}{nw}"

show emi basic_closedgrin_gym
with charachange

# emi "Hisao's officially joined me on my morning runs."
emi "ฮิซาโอะมาร่วมเป็นคู่วิ่งยามเช้ากับหนูอย่างเป็นทางการแล้ว"

# "I start to explain, but Emi cuts me off."
"ฉันเตรียมจะอธิบายแต่เอมิก็ตัดบทไปก่อน"

show emi basic_happy_gym
with charachange

# emi "I thought he might need to visit you so that he doesn't die or anything."
emi "พอดีคิดว่าต้องพามาหาคุณพยาบาลให้แน่ใจว่าจะไม่ตายหรืออะไรแบบนั้นน่ะค่ะ"

show nurse fabulous
with charachange

# "The nurse raises his eyebrows in mock horror."
"คุณพยาบาลเลิกคิ้วขึ้นแสร้งทำเป็นกลัว"

# nk "Yes, that would certainly put me out of a job fast, wouldn't it?"
nk "อืม ขืนเป็นงั้นฉันตกงานแน่เลยเนอะ"

show nurse neutral
show emi basic_grin_gym
with charachange

# nk "Well then Hisao, let's have a look at you."
nk "เอาละฮิซาโอะ มาตรวจร่างกายกัน"

# nk "Lift up your shirt, would you?"
nk "เลิกเสื้อขึ้นหน่อย"

# "I'm suddenly very conscious of the fact that Emi's in the room with me and blush in spite of myself."
"อยู่ ๆ ก็นึกอายขึ้นมาที่เอมิอยู่ในห้องด้วยและหน้าแดงขึ้นมาโดยไม่รู้ตัว"

# "The nurse seems to sense my discomfort, but it only seems to amuse him."
"คุณพยาบาลก็เหมือนจะเห็นว่าฉันเกร็ง แต่ดูจะยิ่งชอบใจ"

show nurse grin
with charachange

# nk "A bit shy, are we?"
nk "ขี้อายนะเรา"

# "He makes an apologetic bow to Emi."
"คุณพยาบาลหันไปพยักหน้าให้เอมิเป็นเชิงขอโทษ"

# nk "Sorry Emi, I tried to get you a free show, but it doesn't seem to have worked."
nk "ขอโทษนะเอมิ ฉันกะจะให้เธอได้ดูของดีเสียหน่อย แต่ดูท่าว่าจะไม่ได้ผล"

show emi basic_annoyed_gym
with charachange

# "Emi stiffens slightly and fires a look of annoyance at him."
"เอมิสะดุ้งเล็กน้อยแล้วมองคุณพยาบาลเอือม ๆ"

# emi "You're an asshole."
emi "คุณพยาบาลนี่แย่จริง ๆ"

show emi excited_proud_gym
with charachange

# "Emi bows to me apologetically."
"เอมิค้อมตัวให้ฉันอย่างรู้สึกผิด"

# emi "I'll wait outside, okay Hisao?"
emi "เดี๋ยวไปรอข้างนอกนะฮิซาโอะ"

hide emi
with charaexit

show nurse grin at center
show bg school_nurseoffice at center
with charamove

# "I begin to stammer that it's not really a big deal, she doesn't have to leave, but she's already out the door, and the nurse is laughing as he watches her go."
"ฉันอ้ำอึ้งจะบอกไปว่าไม่เป็นไร ไม่ต้องออกไปก็ได้ แต่เอมิก็เดินออกประตูไปแล้ว คุณพยาบาลหัวเราะไปพลาง\nมองไล่หลังเธอ"

show nurse fabulous
with charachange

# nk "Still got it! Ha!"
nk "ยังใช้ได้นะเราเนี่ย! ฮ่า!"

# hi "I don't follow."
hi "ยังไงนะครับ"

show nurse grin
with charachange

# "He laughs again, like he's in on some joke that's over my head."
"คุณพยาบาลหัวเราะอีกครั้งเหมือนตลกกับมุกที่ฉันยังไม่เข้าใจ"

# nk "I can still get her flustered. It's a competition of sorts we've had going on for a while now."
nk "ฉันยังทำให้เอมิเขินได้ ช่วงนี้เราแข่งกันอะไรประมาณนี้อยู่น่ะ"

# "That sounds incredibly sinister to me, and it seems as if the nurse realizes that too."
"ฟังดูชวนขนลุกเอามาก ๆ และเหมือนคุณพยาบาลก็รู้ตัวเหมือนกัน"

show nurse concern
with charachange

# nk "Er. That sounded a lot worse than it actually is, come to think of it."
nk "เอ่อ จริง ๆ ก็ไม่ใช่เรื่องอะไรขนาดนั้นหรอก จะว่าไปแล้ว"

# hi "I wasn't going to say anything…"
hi "ผมก็ไม่ได้ว่าอะไร…"

# nk "No no, you're right. I should fill you in so that you don't get the wrong idea."
nk "ไม่ ๆ เธอพูดถูก ต้องอธิบายหน่อย เดี๋ยวเธอเข้าใจผิด"

show nurse neutral
with charachange

# nk "I'm actually relatively new here, you see. I got hired on the same year Emi started going here."
nk "คือว่าจริง ๆ แล้วฉันเพิ่งมาใหม่น่ะ มาทำงานที่นี่พร้อม ๆ กับตอนที่เอมิเข้ามาเรียนเลย"

# nk "Before that, I worked with Emi during her initial rehab following her accident."
nk "ก่อนหน้านั้นฉันดูแลเอมิช่วงที่กำลังฟื้นฟูจากอุบัติเหตุน่ะ"

# "Hold on, what?"
"เดี๋ยว อะไรนะ"

show nurse concern
with charachange

# nk "We had to amputate her legs after a really nasty car wreck. It nearly killed her, and succeeded—"
nk "เราต้องตัดขาเอมิเพราะเอมิประสบอุบัติเหตุรถชนอย่างหนักน่ะ ซึ่งเอมิก็เกือบตายแล้ว แต่เราผ่าตัดสำเร็จ—"

# "He shuts up abruptly. I blink at receiving this unexpected piece of news."
"คุณพยาบาลเงียบไปทันที ฉันกะพริบตาปริบ ๆ กับข้อมูลที่ไม่คิดว่าจะได้รับรู้นี้"

# nk "Well, that's not my place to say. Anyway, we've known each other for quite a while."
nk "อืม ฉันก็ไม่ได้มีสิทธิ์จะพูดหรอก แต่นั่นแหละ เรารู้จักกันมาสักพักแล้ว"

# nk "So we have a slightly more familiar relationship than is strictly professional."
nk "ก็เลยมีความคุ้นเคยกันบ้างนิดหน่อย ไม่ใช่แค่ในฐานะหมอกับคนไข้น่ะ"

# "He seems embarrassed, like he's done something stupid."
"คุณพยาบาลดูอายราวกับว่าเพิ่งทำอะไรไม่ดีลงไป"

# "I guess he's really worried about that. I wave a hand to let him know it's not a big deal."
"สงสัยคงจะคิดมากจริง ๆ ฉันโบกมือให้เป็นเชิงบอกว่าไม่เป็นไร"

# hi "Don't worry, sir. I promise I'm going to be discreet."
hi "ไม่ต้องห่วงหรอกครับ ผมสัญญาว่าจะเงียบไว้"

# "I had been wondering about what caused Emi to lose her legs, and that was one of the scenarios I thought of."
"ฉันนึกสงสัยอยู่ว่าเอมิต้องสูญเสียขาไปด้วยเหตุอะไร ซึ่งเหตุการณ์นั้นก็เป็นอย่างหนึ่งที่ฉันเคยคิดไว้เหมือนกัน"

# "There were only so many ways that could have happened, but actually hearing about the facts… it's still a little shocking."
"เพราะจริง ๆ ก็มีหลายทางอยู่ที่จะเกิดเรื่องแบบนั้นได้ แต่พอมาได้ยินกับหูแล้ว… ก็ตกใจเหมือนกัน"

show nurse neutral
with charachange

# nk "Well, thanks. You're a good kid, Hisao."
nk "ขอบคุณนะ เธอนี่เป็นเด็กดีจริง ๆ ฮิซาโอะ"

# nk "I can see why Emi became friends with you."
nk "มิน่าล่ะเอมิถึงได้มาสนิทกับเธอ"

show nurse fabulous
with charachange

# nk "She's quite indomitable, you know."
nk "เอมิน่ะเป็นคนที่ไม่ย่อท้อนะ"

# hi "What do you mean?"
hi "หมายความว่าไงครับ"

# nk "You didn't see her learning to walk. She'd go for so much longer than the others in the hospital. She refused to quit."
nk "เธอไม่ได้อยู่ดูตอนเอมิหัดเดิน เอมิน่ะหัดอยู่นานกว่าใครคนอื่นในโรงพยาบาลเลยเพราะไม่ยอมเลิกสักที"

# nk "Normally it takes years to get to a point where you can even think about running again. Emi did it all in about a year."
nk "ปกติต้องใช้เวลาเป็นปี ๆ กว่าจะกลับมาวิ่งได้ แต่เอมิใช้เวลาแค่ปีเดียวเท่านั้น"

# "He almost seems proud of her, like a father who watches his daughter win a competition or something."
"คุณพยาบาลดูจะภูมิใจมาก ๆ เหมือนพ่อที่เห็นลูกชนะงานแข่งหรืออะไรสักอย่าง"

show nurse neutral
with charachange

# nk "Hell, she'd probably have done it faster if not for the fact that we wouldn't let her."
nk "ไม่สิ อาจจะเร็วกว่าหนึ่งปีด้วยซ้ำถ้าไม่ห้ามไว้"

# hi "Wouldn't let her? Why not?"
hi "ห้ามเหรอครับ ทำไมถึงห้ามล่ะ"

show nurse concern
with charachange

stop music fadeout 4.0

# nk "Because she'd go for so long that her legs would start bleeding where they met her prosthetics."
nk "เพราะจะใช้ขาอยู่นานจนตรงที่ต่อเข้ากับขาเทียมเลือดออกน่ะสิ"

# nk "It's a real concern - it's why she comes by every day after she runs."
nk "เป็นเรื่องที่ต้องจับตาดูเลยนะ เพราะแบบนี้แหละเอมิถึงได้มาหาทุกวันหลังวิ่ง"

# nk "To say nothing of the risk of infection if her legs get cut up and her prosthetics are dirty."
nk "แล้วไหนจะเสี่ยงติดเชื้อถ้าเกิดว่ามีแผลแล้วขาเทียมสกปรกอีก"

show nurse neutral
with charachange

# nk "But enough about that."
nk "แต่เรื่องนั้นไว้ก่อน"

show nurse fabulous
with charachange

play music music_nurse fadein 2.0

# nk "If we don't get you on your way soon, Emi will think we're up to something."
nk "ถ้าไม่รีบจัดการกับเธอเดี๋ยวเอมิจะคิดว่าวางแผนทำอะไรกันอีก"

# "As he says this, he gives a wink and begins checking my heartbeat."
"คุณพยาบาลพูดพลางขยิบตาให้ก่อนจะตรวจหัวใจฉัน"

# "The stethoscope is way too cold."
"เครื่องฟังตรวจนั้นเย็นเฉียบ"

# "He really should have heated it up or something before he used it."
"น่าจะเอาไปอุ่นหรืออะไรก่อนมาใช้"

# "After a few moments he leans back, satisfied."
"ผ่านไปสักพักคุณพยาบาลก็ผละออกด้วยความพอใจ"

show nurse neutral
with charachange

# nk "Well, you sound pretty good to me, Hisao. You didn't have any chest pains while you were running, did you?"
nk "ก็ฟังดูปกติดีนะฮิซาโอะ ตอนวิ่งไม่ได้มีอาการเจ็บหน้าอกใช่มั้ย"

# hi "No, not really. I had some trouble catching my breath, though - and my heart was racing by the end, too."
hi "ก็ไม่นะครับ แต่ผมหายใจไม่ค่อยทัน แล้วตอนวิ่งใกล้ครบรอบหัวใจก็เต้นแรงมาก"

show nurse concern at center
with charachange

# "The nurse frowns as I say this, but then shrugs."
"คุณพยาบาลขมวดคิ้วเมื่อได้ฟัง แต่ก็ยักไหล่"

show nurse neutral at center
with charachange

# nk "It's probably just because you're out of shape… but if you don't improve, then you should let me know, okay?"
nk "อาจจะเพราะไม่ฟิตมั้ง… แต่ถ้าไม่ดีขึ้นก็มาบอกกันนะ"

# nk "Don't push yourself too much - and of course if you have any chest pains, come to me immediately, right?"
nk "อย่าฝืนมากไป แล้วก็ถ้าเจ็บหน้าอกขึ้นมาก็ให้มาหาฉันทันที โอเคนะ"

# "I put my shirt back on, and the nurse leans out of the doorway to call in Emi."
"ฉันใส่เสื้อกลับเหมือนเดิม คุณพยาบาลเดินออกไปอยู่ที่ประตูเรียกเอมิ"

show nurse neutral at twoleft
show bg school_nurseoffice at bgleft
with charamove

show emi basic_annoyed_gym at tworight
with charaenter

# emi "What took you so long? Now I'm going to be late!"
emi "ทำไมนานจัง สายแล้วเนี่ย!"

stop music fadeout 2.0

show nurse fabulous
with charachange

# "The nurse gives me a significant look."
"คุณพยาบาลส่งสายตาให้อย่างมีเลศนัย"

show nurse grin
with charachange

# nk "I was just seducing Hisao, that's all."
nk "พอดีล่อหลอกฮิซาโอะอยู่น่ะ"

play music music_comedy fadein 0.5

show emi sad_annoyed_gym
with charachange

# emi "What!? Come on, what have I told you about seducing my friends?"
emi "คะ!? ไม่เอาน่า หนูบอกแล้วไงว่าห้ามล่อหลอกเพื่อนหนูน่ะ"

# "I'd expected Emi to be shocked by this, but instead she seems merely annoyed, scolding the nurse as if he were a child stealing cookies."
"ฉันนึกว่าเอมิคงจะตกใจ ทว่าเธอแค่ดูเอือม ๆ พลางดุคุณพยาบาลเหมือนดุเด็กที่ขโมยคุกกี้"

# "Meanwhile, I try hard not to blush at the nurse's innuendo."
"ระหว่างนั้นฉันก็ห้ามตัวเองไม่ให้หน้าแดงกับคำพูดสองแง่สองง่ามนั้น"

show nurse fabulous
with charachange

# nk "I'll try not to do it again, though I fear young Hisao may be lost to the female gender forever!"
nk "จะไม่ทำอีกแล้ว แต่ฉันเกรงว่าพ่อหนุ่มฮิซาโอะเขาคงจะไม่สนใจผู้หญิงไปอีกตลอดกาลแล้วละ!"

stop music fadeout 0.5

# hi "Not freaking likely."
hi "ไม่มีวันซะละ"

with Pause(3.0)

play music music_comedy fadein 0.5

show nurse grin
show emi excited_laugh_gym
with charachange

# "I didn't mean to say that out loud, but both the nurse and Emi regard me for a moment before bursting into laughter again."
"ฉันไม่ได้กะจะพูดออกมา แต่คุณพยาบาลกับเอมิก็หันมาทางฉันก่อนจะหัวเราะอีกรอบ"

show emi basic_happy_gym
with charachange

# emi "Told you he was funny, didn't I?"
emi "หนูบอกแล้วว่าฮิซาโอะเขาเป็นคนตลก"

# "Huh. I guess Emi does talk to the nurse about a lot of stuff."
"เหอ? สงสัยเอมิคุยอะไรหลายอย่างกับคุณพยาบาลจริงแหละ"

show nurse fabulous
show emi basic_grin_gym
with charachange

# nk "Well Hisao, you should probably get moving. You still need a shower before class starts, don't you?"
nk "เอาละฮิซาโอะ เธอไปเถอะ เดี๋ยวต้องอาบน้ำก่อนไปเข้าเรียนนี่"

# "Crap! He's got a point, and it looks like I've only got a half hour!"
"ตายแล้ว! ก็จริง แล้วเหมือนจะเหลือเวลาอีกแค่ครึ่งชั่วโมงด้วย!"

# hi "Thanks for your time. I'll see you later, Emi!"
hi "ขอบคุณนะครับ แล้วก็เจอกันนะเอมิ!"

scene bg school_nursehall
with locationchange

stop music fadeout 5.0

# "I dash out of the room as the nurse begins to remove Emi's prosthetics."
"ฉันพุ่งตัวออกจากห้องไประหว่างที่คุณพยาบาลเริ่มถอดขาเทียมเอมิ"

# "As I head down the hallway, I can just barely hear his voice drifting after me."
"ระหว่างที่เดินไปตามโถงทางเดินก็ได้ยินเสียงคุณพยาบาลแว่ว ๆ มา"

# nk "Emi, you've got to be more careful…"
nk "เอมิ เธอต้องระวังหน่อย…"

scene bg school_dormhisao
with locationskip

# "I make it back to my room and shower in record time. It occurs to me that I've already been up for four hours, and class hasn't even started yet."
"ฉันกลับถึงห้องแล้วอาบน้ำด้วยความเร็วแสง และฉันก็เพิ่งระลึกได้ว่าฉันตื่นมาสี่ชั่วโมงแล้วโดยที่ยังไม่ได้เข้าเรียน"

# "This is going to be a really, really long day."
"วันนี้จะต้องเป็นวันที่แสนเหนื่อยแน่ ๆ"

# "I hope I don't fall asleep in class."
"หวังว่าจะไม่หลับไปตอนเรียนนะ"

$ suppress_window_after_timeskip = True

scene black
with dissolve

########################################################
label th_E8:

window hide None

scene black
with dissolve

show bg school_dormhisao
with openeye

window show

play music music_pearly fadein 5.0

# "The morning sunlight streaming through my window wakes me up instead of my alarm, and I realize that it must be Sunday."
"แสงแดดยามเช้าที่ส่องลอดหน้าต่างมาปลุกฉันแทนนาฬิกาปลุก และฉันก็นึกได้ว่าวันนี้วันอาทิตย์"

# "Emi has kindly deigned to give me weekends off from our morning runs."
"เอมิยังมีเมตตาที่กรุณาให้ฉันได้พักการวิ่งยามเช้าในวันสุดสัปดาห์"

# "I don't actually know if I woke up at all yesterday, or if I just slept through the entire day."
"ฉันไม่รู้ว่าเมื่อวานตื่นอยู่หรือหลับอยู่ทั้งวันกันแน่"

# "My legs groan in protest as I lever myself out of bed."
"ขาฉันร้องประท้วงเมื่อฉันลุกจากเตียง"

# "All this running has really taken it out of me."
"วิ่งจนแรงแทบไม่เหลือแหล่"

# "Still, I can't deny that Emi wasn't lying to me."
"แต่ก็ปฏิเสธไม่ได้ว่าเอมิพูดจริง"

# "It has gotten a little easier."
"เพราะเริ่มชินขึ้นมาหน่อย ๆ แล้ว"

# "I'd been worried that the runs would start to wear on my nerves, but thus far I haven't minded them that much."
"ฉันเคยกลัวว่าพอวิ่งหลายวันเข้าแล้วจะเริ่มไม่อยากมา แต่เท่าที่ผ่านมาฉันก็ไม่ได้อะไรมากมาย"

# "Well, it's only been a week."
"แต่ก็เพิ่งสัปดาห์เดียวเอง"

# "I suppose there's plenty of time for me to start dreading the sound of my alarm in the morning."
"คงจะมีเวลาอีกหลายวันให้ฉันเริ่มรู้สึกหวาดผวากับเสียงนาฬิกาปลุกยามเช้า"

# "Not that I could ever skip out now."
"แต่ใช่ว่าจะถอนตัวตอนนี้ได้อะนะ"

# "As Emi said, it's harder to stop a routine when there's another person."
"อย่างที่เอมิบอกนั่นแหละว่าพอมีอีกคนร่วมด้วยแล้วจะล้มเลิกกิจวัตรยาก"

# "And frankly, I don't think I'm equipped to deal with a disappointed Emi."
"และว่าตามตรง ฉันรับไม่ได้หรอกถ้าต้องทำให้เอมิผิดหวัง"

# "She'd probably give me those puppy-dog eyes and I'd feel terrible about myself."
"คงจะมองฉันด้วยแววตาลูกหมาน้อยที่ทำให้ฉันรู้สึกผิดขึ้นมาแน่ ๆ"

# "Which reminds me… wasn't I supposed to be somewhere today?"
"ซึ่งจะว่าไปแล้ว… เหมือนวันนี้ฉันจะต้องไปที่ไหนสักที่อยู่นะ"

$ renpy.music.set_volume(0.3,2.0,channel="music")

scene bg school_track_fb
show emi basic_closedhappy_gym_fb at center
show noiseoverlay
with flashback

# emi "Hey, you're coming to my track meet on Sunday, right?"
emi "นี่ วันอาทิตย์นี้จะมาดูงานแข่งวิ่งใช่มั้ย"

show emi basic_grin_gym_fb
with charachange

# emi "What am I talking about, of course you are."
emi "ฉันนี่ถามอะไรแปลก ๆ นายต้องมาอยู่แล้วสิ"

show emi sad_grin_gym_fb
with charachange

# emi "Right?"
emi "ใช่มั้ย"

# "Those puppy-dog eyes again."
"ตาลูกหมาน้อยนั้นอีกแล้ว"

# hi "Of course I'm going!"
hi "ไปอยู่แล้วสิ!"

# hi "I owe you, right?"
hi "ฉันติดหนี้เธอนี่"

show emi excited_proud_gym_fb
with charachange

# emi "Exactly! So don't forget, okay?"
emi "ใช่! เพราะงั้นอย่าลืมนะ"

$ renpy.music.set_volume(1.0,2.0,channel="music")

scene bg school_dormhisao
with flashforward

# "Crap, Emi's track meet!"
"ฉิบ งานแข่งวิ่งเอมิ!"

# "I'd better get a move on if I don't want to miss her running, since she's the only reason I'm even considering going."
"ถ้าไม่อยากพลาดที่เอมิลงแข่งแล้วก็ต้องรีบไป เพราะยังไงที่ไปดูก็แค่ไปดูเอมิอยู่แล้ว"

# "Otherwise, it would defeat the whole purpose of going."
"ไม่งั้นก็ไม่รู้จะไปทำไม"

scene bg school_courtyard
show crowd
with shorttimeskip

play ambient sfx_crowd_outdoors fadein 3.0

# "And so, I soon find myself quite suddenly surrounded by a crowd of people, all turning out to see our track team compete with another school like this one."
"แล้วอยู่ ๆ ฉันก็มาอยู่ท่ามกลางผู้คนที่มาดูทีมกรีฑาของโรงเรียนเราแข่งกับโรงเรียนอื่น"

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")
$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide

nvl clear

nvl show dissolve

# n "\nI'll admit it, it's almost comforting to know we're not the only school like this."
n "\nต้องยอมรับว่าฉันพอจะสบายใจขึ้นเมื่อได้รู้ว่าเราไม่ได้เป็นแค่โรงเรียนเดียวที่เป็นอย่างนี้"

# n "After you see that there can be {b}two{/b} schools with a bunch of… defective kids, well."
n "พอได้รู้ว่ามีโรงเรียน{b}สอง{/b}แห่งที่นักเรียน… เป็นคนพิการแล้ว"

# n "…You stop feeling so defective."
n "…ก็จะรู้สึกว่าไม่ได้ผิดปกติขนาดนั้น"

# n "You also stop feeling unique, which in most cases would be a bad thing, but in this case it sure as hell isn't."
n "แล้วก็จะไม่รู้สึกว่าเป็นเอกลักษณ์ ที่หลายครั้งจะเป็นในแง่ลบ แต่ความเป็นเอกลักษณ์นี้ไม่ใช่แง่ลบแน่นอน"

# n "That's part of Yamaku's appeal, I guess."
n "ก็คงเป็นเสน่ห์อย่างหนึ่งของยามากุละมั้งนะ"

# n "Learn that you're not unique - hell, learn there's a lot of others who would kill to be saddled with your problem instead of whatever they're dealing with."
n "การได้รู้ว่าตัวเองไม่ใช่คนพิเศษ ไม่สิ ได้รู้ว่ามีอีกหลายคนที่อยากจะมารับปัญหาของตัวเองแทนที่จะต้องมารับมือ\nกับอะไรก็ช่างที่พวกเขาต้องเผชิญ"

# n "Some of the kids here aren't here because they're missing a leg or they have a heart condition."
n "บางคนไม่ได้มาเรียนที่นี่เพราะขาขาดหรือเป็นโรคหัวใจ"

# n "Some of them might be here because they're as good as dead in two, maybe three years if they're lucky."
n "บางคนที่มาเรียนที่นี่ก็เพราะในอีกสองปี—หรือถ้าโชคดีก็สามปี—ก็ไม่ต่างอะไรกับการตายทั้งเป็น"

# n "And that's only if they get the right sort of care."
n "และที่อยู่แบบธรรมดาได้นานขนาดนั้นก็เพราะได้รับการดูแลที่ถูกต้อง"

# n "It's a bitter sort of comfort to be able to say “Well, at least I've got a chance of being alive through college,” but there it is."
n "เป็นความสบายใจเจือรสขมที่ได้คิดว่า “ก็นะ อย่างน้อยฉันก็จะมีชีวิตรอดไปจนเรียนมหาวิทยาลัย” แต่ก็เท่านั้น"

$ renpy.music.set_volume(1.0, 2.0, channel="ambient")
$ renpy.music.set_volume(1.0, 2.0, channel="music")
nvl clear

nvl hide dissolve

window show

stop music fadeout 3.0

# "I'm brought out of my rather morbid musings by the appearance of Rin near the entrance to the bleachers."
"ฉันโดนดึงสติออกจากความคิดที่ออกจะบิดเบี้ยวนั้นเมื่อเห็นรินที่อยู่ตรงข้าง ๆ ทางเข้าสแตนด์เชียร์"

show rin basic_deadpannormal at center
with charaenter

# rin "You came."
rin "มาจนได้"

# hi "Of course. I said I would, didn't I?"
hi "แหงสิ ก็รับปากไว้แล้วนี่ว่าจะมา"

show rin basic_deadpanamused
with charachange

# rin "That doesn't necessarily imply that you had to follow through."
rin "แต่ก็ไม่ได้หมายความว่านายจำเป็นจะต้องทำตามที่พูดไว้นี่"

show rin basic_awayabsent
with charachange

# rin "Lots of people say things and don't mean them."
rin "คนที่ชอบพูดเลื่อนลอยก็มีถมไป"

# hi "Well, I don't."
hi "อืม ฉันไม่พูดอะไรอย่างนั้นหรอก"

play music music_soothing fadein 0.5

show rin relaxed_boredom
with charachange

# "Rin shrugs. Seemingly bored with our conversation, she turns on her heel and heads back toward the stands."
"รินยักไหล่ พอเหมือนจะเบื่อกับบทสนทนานี้แล้วเธอก็หมุนส้นเท้าแล้วเดินไปที่สแตนด์เชียร์ต่อ"

# rin "I owe Emi money now."
rin "ทีนี้ฉันก็ติดเงินเอมิแล้ว"

# hi "Why's that?"
hi "ทำไมล่ะ"

show rin basic_absent
with charachange

# rin "I didn't think you'd show up."
rin "ฉันคิดว่านายจะไม่มา"

# rin "Emi did."
rin "เอมิคิดว่ามา"

show rin basic_awayabsent
with charachange

# rin "So I owe her 500 yen."
rin "ฉันเลยติดเงินเอมิ 500 เยน"

# hi "You two bet an awful lot, don't you?"
hi "พนันกันหลายครั้งน่าดูเลยนะ"

# "Another shrug from my armless companion."
"เพื่อนไร้แขนของฉันยักไหล่อีกครั้ง"

show rin basic_deadpan
with charachange

# rin "I don't think so."
rin "ฉันว่าไม่น่านะ"

scene bg school_track
show crowd
show rin basic_deadpan
with locationchange

# "We enter the bleachers, and Rin nods upwards."
"พอมาถึงที่สแตนด์เชียร์แล้วรินก็บุ้ยใบ้ไปข้างบน"

show rin negative_spaciness at center
with charaenter

# rin "Up there."
rin "บนนั้น"

show rin basic_deadpancontemplation
with charachange

# rin "I came out to see if you'd come."
rin "ฉันมาดูว่านายจะมามั้ย"

# "For the bet, I presume."
"เพราะพนันกันไว้สินะ"

# "Rin leads the way, and soon we've settled down on an almost-empty bench."
"รินนำทางขึ้นไป ไม่นานพวกเราก็มานั่งตรงที่นั่งแถวที่โล่ง ๆ"

$ renpy.music.set_volume(0.3, 3.0, channel="ambient")

show rin basic_deadpancontemplation at tworight
show bg school_track at bgright
show crowd:
    linear 1.0 alpha 0.0
with charamove

hide crowd
show meiko smile at twoleft
with charaenter

# "There's an older woman sitting next to Rin - someone's mother, I assume."
"ข้าง ๆ รินมีผู้หญิงวัยกลางคนอยู่คนหนึ่ง คงจะเป็นแม่ใครสักคนละมั้ง"

# "She's got rather long hair done up in a braid. On seeing Rin, she gives her an oddly familiar-seeming grin."
"ผมเธอที่ถักเปียค่อนข้างยาว พอเธอเห็นรินก็ยิ้มให้ด้วยความคุ้นเคยอย่างประหลาด"

show meiko happy
with charachange

# emm_ "Well, this is surprising."
emm_ "แหม ตกใจจัง"

show meiko wink
with charachange

# emm_ "I thought you went to get a snack, not a boy."
emm_ "นึกว่าไปหาขนมกินเสียอีก เป็นผู้ชายหรอกเหรอ"

# hi "Huh?"
hi "ฮะ?"

show rin basic_surprised
with charachange

# rin "A snack?"
rin "ขนม?"

show rin relaxed_nonchalant
with charachange

# rin "I wondered why I was down there."
rin "ก็ว่าอยู่ลงไปทำไม"

show meiko happy
show rin basic_awayabsent
with charachange

# "The woman laughs, again in a way that seems familiar."
"เธอหัวเราะอีกครั้งด้วยท่าทีที่ดูคุ้นเคย"

# "Where have I seen her before?"
"เคยเห็นที่ไหนนะ"

show meiko smile
with charachange

# emm_ "Well, I suppose you've always been one to go out for one thing and bring back another."
emm_ "อืม เธอก็คงเป็นคนที่ชอบออกไปหยิบของอย่างหนึ่งแล้วได้อีกอย่างมาแทนอยู่แล้วละมั้งจ๊ะ"

# emm_ "But I'm being rude! I haven't introduced myself."
emm_ "ตายละ หยาบคายจัง! ยังไม่ได้แนะนำตัวเลย"

# emm_ "I'm Meiko Ibarazaki, Emi's mother."
emm_ "ฉัน เมอิโกะ อิบาราซากิ แม่เอมิจ้ะ"

show meiko happy
with charachange

# emm "Pleased to meet you."
emm "ยินดีที่ได้รู้จักจ้ะ"

# "Well, that explains it."
"อ้อ มิน่าล่ะ"

# "She's like a taller, older and better endowed Emi."
"ดูเหมือนเอมิในแบบที่สูงกว่า แก่กว่า และเจนโลกกว่า"

# "Apart from her hair being a darker shade than Emi's, there's really no mistaking the resemblance."
"นอกจากสีผมที่เข้มกว่าลูกสาวเธอแล้วที่เหลือก็คล้ายกันมาก"

show rin basic_absent
show meiko smile
with charachange

# hi "Sorry, I'm Hisao. Hisao Nakai."
hi "ขอโทษครับ ผมฮิซาโอะ ฮิซาโอะ นากาอิ"

# hi "And really, you don't have to apologize for not introducing yourself, Mrs. Ibarazaki."
hi "แล้วก็ไม่ต้องขอโทษที่ไม่ได้แนะนำตัวกับผมหรอกครับคุณนายอิบาราซากิ"

# hi "That's really Rin's job in this situation, isn't it?"
hi "เพราะแบบนี้น่าจะเป็นหน้าที่รินมากกว่าที่ต้องแนะนำตัวให้"

show meiko happy
show rin basic_awayabsent
with charachange

# "Another laugh from Emi's mother."
"แม่เอมิหัวเราะอีกรอบ"

# emm "I take it you've not known Rin for that long, then."
emm "แปลว่ายังรู้จักรินมาไม่นานสินะจ๊ะ"

show meiko smile
with charachange

# emm "It's best not to expect her to remember something like that."
emm "อย่าไปคาดหวังว่ารินเขาจะจำอะไรแบบนั้นได้เลยจ้ะ"

show meiko wink
with charachange

# emm "She's got other things to think about, I assume."
emm "เพราะคงมีอะไรอย่างอื่นให้ต้องคิดเยอะแยะ"

show rin basic_deadpannormal
with charachange

# "Rin nods, seeming pleased by this assessment."
"รินพยักหน้าดูพอใจกับคำประเมินนั้น"

show rin basic_deadpan
with charachange

# rin "She's right."
rin "ถูกแล้ว"

show rin basic_lucid
with charachange

# rin "I was thinking about sunsets."
rin "ฉันคิดถึงเรื่องพระอาทิตย์ตกดินอยู่"

show meiko happy
show rin basic_awayabsent
with charachange

# emm "You see? It's really up to us to make introductions and the like."
emm "เห็นไหม หน้าที่เราทั้งนั้นแหละที่ต้องแนะนำตัวอะไรกัน"

# "For lack of any better response, I nod."
"ฉันพยักหน้าด้วยไม่รู้จะตอบอย่างไร"

# "Mrs. Ibarazaki leans back a little on her seat and raises an eyebrow."
"คุณนายอิบาราซากินั่งเอนตัวเล็กน้อยแล้วเลิกคิ้วขึ้น"

$ renpy.music.set_volume(0.0, 0.5, channel="ambient")

show meiko serious
with charachange

stop music fadeout 0.8

# emm "So, how long have you and Rin been dating?"
emm "แล้วเธอสองคนคบกันมานานหรือยัง"

# "My response consists of silence as my brain suddenly lurches into gear. But just before I can begin to utter a hastily babbled explanation, Emi's mother bursts into laughter again."
"ฉันนิ่งเงียบไปขณะที่สมองกำลังทำงานอยู่ แต่ก่อนที่ฉันทันจะได้รีบโพล่งอธิบายอะไรออกไปแม่ของเอมิก็หัวเราะขึ้นมา\nอีกครั้ง"

play music music_soothing fadein 0.5
$ renpy.music.set_volume(0.3, 0.5, channel="ambient")

show meiko happy
with charachange

# emm "Ha! You're a blusher, aren't you?"
emm "แหม! ขี้อายสินะจ๊ะเนี่ย"

# "I don't know if there's any way to keep my dignity in this situation, so I settle for a mumbled response."
"ฉันไม่รู้ว่าจะพูดอะไรยังไงเพื่อรักษาหน้าได้อยู่หรือเปล่า จึงเลือกที่จะตอบแบบเสียงอ่อย ๆ"

show meiko smile
show rin basic_absent
with charachange

# hi "Maybe."
hi "มั้งครับ"

show rin basic_awayabsent
with charachange

# emm "So this must be a new romance then, mustn't it?"
emm "งั้นก็แปลว่าเป็นรักครั้งใหม่สินะจ๊ะ"

show rin basic_absent
with charachange

# hi "Wait, that's not the question that—"
hi "เดี๋ยวครับ ผมไม่ได้ตอบคำถามนั้—"

show meiko happy
show rin basic_awayabsent
with charachange

# "Another laugh."
"และหัวเราะอีกรอบ"

show meiko smile
with charachange

# emm "I know, but it's funny to watch you squirm."
emm "รู้จ้ะ แต่เห็นเธออายแล้วตลกดี"

show meiko wink
with charachange

# emm "I'm sorry. Forgive an old woman her amusements."
emm "ขอโทษทีนะจ๊ะ อย่าถือสาคนรุ่นป้าเลยจ้ะ"

# "Old woman?"
"ป้า?"

# "She sure doesn't look that old to me."
"ก็ดูไม่แก่ขนาดนั้นนะ"

# "Clearly Emi gets her youthful features from her mother."
"ที่เอมิดูเด็กเพราะได้แม่มาด้วยซ้ำ"

show rin basic_absent
with charachange

# hi "I suppose I can let it go."
hi "ผมก็ไม่ได้อะไรขนาดนั้นหรอกครับ"

show meiko happy
show rin basic_awayabsent
with charachange

# emm "How kind of you."
emm "ขอบคุณจ้ะ"

stop music fadeout 6.0

show rin basic_deadpan
with charachange

# rin "It's starting."
rin "เริ่มแล้ว"

stop ambient fadeout 2.0

scene ev emitrack_blocks at Fullpan(12.0, dir="left", time_warp=_ease_in_time_warp)
with locationskip

# "I direct my attention to the track, where they're preparing for the first sprint."
"ฉันหันเหความสนใจมายังลู่วิ่งที่กำลังเตรียมแข่งวิ่งรอบแรกกัน"

# "It looks like the 400 meter dash."
"เหมือนจะเป็นแข่งวิ่ง 400 เมตร"

# "My eyes scan the runners, before finding Emi."
"ฉันทอดตามองตามนักวิ่งจนเจอเอมิ"

scene ev emitrack_blocks_close
with flash

# "She's smiling, with an almost cocky look on her face."
"เธอยิ้มจนดูออกจะมั่นใจเกินไปหน่อย"

show insert startpistol at right
with easeinright

# "The starter raises his pistol."
"ผู้ปล่อยตัวยกกระบอกปืนขึ้น"

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")

play sound sfx_startpistol
play ambient sfx_emisprinting

scene ev emitrack_running at Fullpan(1.0, dir="left", time_warp=_ease_in_time_warp)
with silentflash

# "Emi explodes off the block, disappearing from the starting line in a blur."
"เอมิพุ่งตัวออกจากสตาร์ตติงบล็อกก่อนจะหายวับไปจากเส้นเริ่ม"

# "It's amazing. Even as the other sprinters converge on the lanes closest to the inside line, Emi surges to the front of the pack."
"สุดยอด ขนาดนักวิ่งคนอื่นที่อยู่ช่องวิ่งที่ชิดกับขอบในกว่าเอมิก็ยังวิ่งนำออกมาได้"

# "By the time she rounds the final turn, some of the other runners have caught up with her."
"พอเธอวิ่งจนมาถึงโค้งสุดท้ายก็มีนักวิ่งสองสามคนที่ตามมาทันแล้ว"

# "Their efforts come to naught though, since a final burst of speed from Emi leaves them at least a half second behind."
"ทว่าตามมาทันไปก็เท่านั้น เพราะเธอก็พุ่งตัวปิดท้ายจนทิ้งห่างจากคนที่ว่าสักครึ่งวินาทีเห็นจะได้"

scene ev emitrack_finishtop:
    xalign 0.5 yalign 0.0 zoom 4.0 subpixel True
    0.2
    linear 0.3 zoom 1.05
    easein 8.0 zoom 1.0
with flash

stop ambient fadeout 1.0
play sound sfx_crowd_cheer

# "Mrs. Ibarazaki whoops and shouts, applauding wildly, and generally looking like any other parent cheering on their child."
"คุณนายอิบาราซากิกรี๊ดกร๊าดพลางปรบมือใหญ่ ดูไม่ต่างไปจากพ่อแม่ที่มาเอาใจช่วยลูกตัวเองที่ลงแข่งโดยทั่วไป"

# "Emi bounds off the track, looking pleased with herself."
"เอมิออกมาจากลู่วิ่งดูพอใจกับตัวเอง"

scene bg school_track at bgright
show meiko happy at twoleft
show rin basic_deadpandelight at tworight
with locationchange

play music music_daily fadein 2.0

# "I cheer right along with the rest of them."
"ฉันก็ผสมโรงเฮไปกับเขาด้วย"

# "The announcer (sounding suspiciously like Misha) gleefully gives the results."
"ผู้ประกาศ (ที่เสียงคล้ายมิช่าอย่างน่าสงสัย) รายงานผลการแข่งขันด้วยความยินดียิ่ง"

show meiko smile
show rin basic_awayabsent
with charachange

# emm "I think she's gotten faster since the last time."
emm "เหมือนจะเร็วขึ้นกว่าครั้งที่แล้วนะจ๊ะเนี่ย"

show rin basic_absent
with charachange

# hi "That was incredible."
hi "สุดยอดเลยครับ"

show meiko happy
show rin basic_awayabsent
with charachange

# "Mrs. Ibarazaki grins proudly."
"คุณนายอิบาราซากิยิ้มอย่างภาคภูมิ"

# emm "Emi's a heck of a runner."
emm "เอมิเขาวิ่งเก่งมาก"

show meiko smile
with charachange

# "We fall silent as the next event is being prepared."
"พวกเราเงียบกันไประหว่างรองานแข่งต่อไปเริ่ม"

# "I'm surprised to see Emi striding out onto the track again."
"ฉันนึกแปลกใจที่เห็นเอมิกลับเข้าลู่วิ่งอีกครั้ง"

show rin basic_absent
with charachange

# hi "Wait, didn't she just run?"
hi "เดี๋ยวนะครับ เพิ่งวิ่งไปไม่ใช่เหรอ"

# "Emi's mother nods."
"แม่เอมิพยักหน้า"

show rin basic_awayabsent
with charachange

# emm "Yes, but she runs multiple events for the team. Especially the sprints."
emm "จ้ะ แต่เธอวิ่งให้ทีมหลายประเภทเลย โดยเฉพาะวิ่งระยะสั้น"

show meiko happy
with charachange

# emm "It's a lot of running, but Emi can handle it."
emm "ก็เยอะแหละจ้ะ แต่เอมิเขาวิ่งไหวอยู่แล้ว"

# "From the looks of things, she's right."
"ดูจากสภาพแล้วก็คงจริง"

# "Emi doesn't appear to be tired, as if she hadn't run the previous event at all."
"เอมิดูไม่เหนื่อยเลย เหมือนไม่ได้วิ่งแข่งรอบเมื่อกี้มาด้วยซ้ำ"

# "If not for the sweat visible on her shirt, you'd never know."
"ถ้าไม่มีเหงื่อที่ซึมเสื้ออยู่คงไม่มีทางรู้แน่ ๆ"

show rin basic_absent
with charachange

# hi "Which event is this?"
hi "อันนี้ประเภทอะไรเหรอครับ"

show meiko smile
show rin basic_awayabsent
with charachange

# emm "It's the 200 meter dash."
emm "วิ่ง 200 เมตรจ้ะ"

# emm "She'll do this one, the 100-meter, and the relay."
emm "วิ่งอันนี้ วิ่ง 100 เมตร แล้วก็วิ่งผลัดด้วย"

show rin basic_absent
with charachange

# hi "I see."
hi "อย่างนี้นี่เอง"

show rin negative_spaciness
with charachange

play sound sfx_startpistol
play ambient sfx_emisprinting

# "Once again the pistol sounds, and once again Emi flies off the block."
"เมื่อเสียงปืนดังขึ้นอีกหน เธอก็ดีดตัวออกจากสตาร์ตติงบล็อกอีกครา"

# "A thumping sound draws my attention away from the race."
"เสียงตุบตับดึงความสนใจฉันไปจากการแข่งวิ่ง"

# "It's Rin's foot."
"เสียงเท้าริน"

# "She seems completely absorbed in the race."
"เธอดูจะจดจ่ออยู่กับการแข่ง"

show meiko happy
with charachange

stop ambient fadeout 1.0
play sound sfx_crowd_cheer

# "Emi's mother cheers again, and I assume that the race is over."
"แม่เอมิร้องเฮขึ้นมาอีกครั้ง น่าจะแข่งเสร็จแล้ว"

# "Sprints don't seem to me like they'd take very long to complete."
"แข่งวิ่งระยะสั้นดูจะใช้เวลาไม่นาน"

# hi "Your foot."
hi "เท้า"

show rin relaxed_surprised
show meiko smile
with charachange

# rin "Hmm?"
rin "หืม"

# hi "Your foot was bouncing on the bleachers."
hi "เท้าเธอเตะสแตนด์อยู่"

show rin basic_deadpan
with charachange

# rin "Oh."
rin "อ้อ"

# hi "You seem pretty into this stuff. I'm surprised."
hi "เธอดูสนใจนะ แปลก"

show rin basic_deadpansurprised
with charachange

# "Rin looks at me quizzically."
"รินมองฉันด้วยความฉงน"

# rin "Why wouldn't I be?"
rin "ทำไมถึงคิดว่าไม่สนใจ"

# hi "No reason, I just thought stuff like sports wouldn't interest you."
hi "ไม่รู้สิ ก็คิดว่าเธอคงไม่สนใจกีฬาอะไรแบบนี้"

show rin relaxed_nonchalant
with charachange

# rin "Hmm, I suppose you're right."
rin "อืมม ก็คงงั้น"

# rin "It's not that interesting."
rin "ก็ไม่ได้น่าสนใจขนาดนั้นหรอก"

show rin basic_deadpannormal
with charachange

# rin "But I'm watching Emi, not the sport."
rin "แต่ฉันดูเอมิอยู่ ไม่ได้ดูการแข่ง"

# hi "I don't follow."
hi "ไม่เข้าใจ"

show rin basic_lucid
with charachange

# rin "Emi's the most Emi when she runs."
rin "เอมิจะเป็นเอมิที่สุดก็ตอนที่เธอวิ่ง"

# rin "You don't get to see Emi at her Emiest very often."
rin "นายจะไม่ได้เห็นเอมิที่เป็นเอมิ๊เอมิบ่อย ๆ หรอกนะ"

show rin basic_deadpanamused
with charachange

# rin "But here, you can. See?"
rin "แต่ตอนนี้ได้เห็นแล้ว เห็นมั้ย"

# "She directs my attention toward the track again, where the 100-meter dash is about to start."
"เธอให้ฉันกลับไปมองที่ลู่วิ่งอีกครั้ง ที่ที่การแข่งวิ่ง 100 เมตรกำลังจะเริ่มขึ้น"

stop music fadeout 6.0
stop sound fadeout 2.0

scene ev emitrack_blocks_close
with locationskip

# "I watch Emi closely."
"ฉันจับจ้องเอมิ"

# "As she gets onto the starter blocks, her whole body seems to relax, but it's a false relaxation."
"เธอตั้งท่าอยู่ที่สตาร์ตติงบล็อกดูผ่อนคลาย แต่ก็เป็นความผ่อนคลายแบบหลอกเท่านั้น"

# "I can see that she's actually like a coiled spring."
"ฉันดูออกว่าในตัวเธอนั้นมีแรงเหมือนสปริงที่ถูกกดอยู่"

scene ev emitrack_blocks_close_grin
with locationchange

# "As the starter tells everyone to get set, her head snaps up, and her eyes narrow slightly."
"เมื่อผู้ปล่อยตัวบอก “ระวัง” เธอก็เงยหน้าขึ้นแล้วหรี่ตาลงเล็กน้อย"

# "Her mouth curls upward in what could be a grin and could be a growl."
"ปากเธอหยักขึ้นดูเป็นได้ทั้งรอยยิ้มและเสียงฮึด"

play sound sfx_startpistol
play ambient sfx_emisprinting

scene ev emi_run_face_zoomin
with locationskip

# "When the pistol goes off, it's as if she's been unleashed from a cage, like she was always moving at this blinding speed, but we couldn't see it happening until the starter's pistol dispelled the illusion of motionlessness."
"เสียงปืนดังขึ้น ท่าทีเธอราวกับว่าถูกปล่อยจากกรง ราวกับว่าจริง ๆ แล้วก่อนหน้านี้เป็นภาพลวงตาว่าเธออยู่นิ่ง ๆ\nจนเสียงปืนดังทำให้เห็นความเป็นจริงว่าเธอกำลังเคลื่อนที่มาอย่างรวดเร็วจนมองไม่ทันอยู่แล้วแต่แรก"

# "It's all over in a few seconds, but in those few seconds I feel like I just witnessed something very personal for Emi."
"เพียงไม่กี่วินาทีทุกอย่างก็สิ้นสุดลง แต่ในไม่กี่วินาทีนั้นฉันรู้สึกราวกับว่าได้เห็นบางอย่างที่เป็นตัวตนของเอมิมาก ๆ"

stop ambient fadeout 1.0
play sound sfx_crowd_cheer

# "As soon as she crossed the finish line, the fierce look was replaced by her normal grin."
"ทันทีที่เธอเข้าเส้นชัย รอยยิ้มอย่างเคยของเธอก็ผุดขึ้นแทนที่สีหน้าอันมุ่งมั่น"

# "The conquering general returning to his farm."
"เหมือนนายพลอันเก่งกล้าที่กลับมาใช้ชีวิตอยู่บ้านนอก"

# hi "Amazing."
hi "สุดยอด"

# hi "She's really amazing. I've never seen anyone move that fast."
hi "สุดยอดจริง ๆ ครับ ผมไม่เคยเห็นใครเร็วขนาดนั้นมาก่อนเลย"

scene bg school_track at bgright
show meiko smile at twoleft
show rin basic_deadpanamused at tworight
with locationchange

# emm "Well, don't look at me, I'm far too relaxed to run that fast."
emm "แหม ไม่ต้องมองฉันหรอกจ้ะ ฉันเอื่อยเกินจะวิ่งเร็วขนาดนั้นแล้ว"

show meiko worry
show rin basic_awayabsent
with charachange

# emm "No, I think Emi's prowess all came from her father's side."
emm "ไม่หรอกจ้ะ ฉันว่าความสามารถเอมิเขาได้พ่อมามากกว่า"

# "At the mention of Emi's father, Mrs. Ibarazaki looks wistful, almost sad."
"พอพูดถึงสามีของเธอขึ้นมาแล้วคุณนายอิบาราซากิก็ดูเศร้าสร้อยขึ้นมา"

# emm "He got her into running, you know."
emm "ที่สนใจเรื่องวิ่งก็เพราะพ่อนี่แหละจ้ะ"

show rin basic_absent
with charachange

# hi "Yeah, she told me."
hi "ครับ เอมิเคยเล่าให้ฟังอยู่"

# "I'm uncertain as to whether or not it would be rude of me to ask after Emi's father."
"ฉันไม่แน่ใจนักว่าจะเป็นการหยาบคายหรือเปล่าถ้าจะถามเรื่องพ่อของเอมิ"

# "But after that look on her face a few days ago, I feel compelled to ask."
"แต่พอนึกถึงหน้าที่เห็นเมื่อสองสามวันที่แล้วก็รู้สึกอยากถามขึ้นมา"

# hi "Where is her father now, if I might ask?"
hi "ขอถามหน่อยได้มั้ยครับว่าตอนนี้พ่อเอมิอยู่ไหน"

# "Emi's mother hesitates, clearly not willing to answer the question but at the same time not wishing to appear rude."
"แม่เอมิลังเล เห็นชัดว่าไม่เต็มใจจะตอบคำถาม แต่ก็ไม่อยากทำตัวหยาบคาย"

show meiko serious
show rin basic_awayabsent
with charachange

# emm "He… isn't around any more."
emm "เขา… ไม่อยู่แล้วจ้ะ"

# hi "I'm sorry, I didn't mean to bring up bad memories."
hi "ขอโทษนะครับ ผมไม่ได้ตั้งใจจะไปขุดคุ้ยเรื่องไม่ดี"

show rin basic_absent
with charachange

# hi "Emi just seemed a little sad when she mentioned him earlier."
hi "แค่ว่าตอนเอมิเล่าเรื่องพ่อตัวเองผมเห็นทำหน้าเศร้า ๆ"

show meiko worry
show rin basic_awayabsent
with charachange

# emm "That's not surprising, considering."
emm "ก็ไม่แปลกหรอกจ้ะ เพราะ"

# hi "Hmm?"
hi "ครับ?"

# emm "They were very close."
emm "เอมิสนิทกับเขามาก"

show rin basic_absent
with charachange

# hi "I see."
hi "อย่างนี้นี่เอง"

play sound sfx_cellphone

# "A beeping noise suddenly emanates from Mrs. Ibarazaki's pocket. Reaching into it, she pulls out a cell phone and looks at it."
"จู่ ๆ เสียงโทรศัพท์ก็ดังขึ้นมาจากกระเป๋ากางเกงของเธอ เธอควักขึ้นมาเปิดหน้าจอดู"

show meiko serious
show rin basic_awayabsent
with charachange

# emm "…Honestly, text messages?"
emm "…ส่งข้อความมาเนี่ยนะ"

# emm "What is he, sixteen?"
emm "นี่เขาคิดว่าตัวเองเป็นวัยรุ่นอายุสิบหกหรืออะไร"

# hi "Hmm?"
hi "ครับ?"

show meiko smile
with charachange

# emm "Oh, nothing."
emm "โอ๊ะ ไม่มีอะไรจ้ะ"

show meiko wink
with charachange

# emm "I've got to go meet up with a friend of mine."
emm "เดี๋ยวฉันต้องไปหาเพื่อนแล้ว"

show meiko happy
with charachange

# emm "Will you tell Emi I'm very proud of her and that I'll call her later tonight?"
emm "ฝากบอกเอมิหน่อยได้ไหมจ๊ะว่าแม่ภูมิใจในตัวลูกมาก ฝากบอกด้วยว่าเดี๋ยวคืนนี้จะโทร. ไปหาอีกที"

show rin basic_absent
with charachange

# hi "Of course."
hi "ได้ครับ"

hide meiko
with charaexit

show rin basic_absent at center
show bg school_track at center
with charamove

show rin basic_awayabsent
with shorttimeskip

play music music_tranquil fadein 2.0

# "I'll admit that I zone out for a while."
"ยอมรับว่าเมื่อกี้เหม่อไปพักหนึ่ง"

# "I almost don't notice that the relay's about to begin. But when I look, I can't find Emi."
"ฉันแทบจะไม่ทันสังเกตว่าจะเริ่มวิ่งผลัดแล้ว แต่พอมองก็ไม่เห็นเอมิ"

# hi "I thought that Emi would be running the relay."
hi "เอมิวิ่งผลัดด้วยไม่ใช่เหรอ"

show rin basic_deadpan
with charachange

# rin "She runs anchor."
rin "วิ่งผลัดสุดท้ายน่ะ"

show rin basic_deadpannormal
with charachange

# rin "So she won't be running for a while yet."
rin "ก็อีกสักพักกว่าจะได้วิ่ง"

# hi "Ah."
hi "อ้อ"

show rin basic_deadpandelight
with charachange

# rin "Did you see it?"
rin "นายเห็นมั้ย"

# hi "Huh?"
hi "หืม"

# rin "Emi at her Emiest."
rin "เอมิที่เป็นเอมิ๊เอมิ"

# hi "Maybe."
hi "มั้งนะ"

show rin basic_deadpanupset
with charachange

# rin "Hmm. Maybe this time."
rin "อืมม คราวนี้น่าจะเห็น"

play sound sfx_startpistol

# "The race begins, and I cheer Emi's teammates along as they pass the baton."
"การแข่งขันเริ่มขึ้นแล้ว ฉันคอยส่งเสียงเอาใจช่วยทีมเอมิที่กำลังส่งคทากันอยู่"

play ambient sfx_emisprinting

scene ev emitrack_running:
    truecenter zoom 1.0 subpixel True
    ease 20.0 zoom 1.05 xalign 0.0 yalign 0.0
with locationskip

# "Finally, I see Emi sprinting onto the track to take the final handoff."
"ในที่สุดก็ได้เห็นเอมิที่สับเท้าไปตามลู่ในฐานะผลัดสุดท้าย"

# "Once again I'm taken aback by how graceful she looks when she runs."
"เป็นอีกครั้งที่ฉันต้องทึ่งกับความงดงามยามเธอวิ่ง"

# "It really is beautiful."
"สวยจริง ๆ"

# "The look of determination and fearlessness on her face only adds to the picture."
"สีหน้าอันมุ่งมั่นและไร้ซึ่งความเกรงกลัวใด ๆ ของเธอยิ่งทำให้ดูดีขึ้นไปอีก"

# "Emi at her Emiest, I suppose."
"นี่แหละมั้ง เอมิที่เป็นเอมิ๊เอมิ"

stop ambient fadeout 1.0
play sound sfx_crowd_cheer

show ev emitrack_finish
with locationskip

# "But then, as she crosses the finish line, I see her stumble slightly."
"แต่จังหวะที่เอมิกำลังข้ามเส้นชัยฉันก็เห็นว่าเธอสะดุดเล็กน้อย"

# "It's only barely, but it's a definite stumble."
"แทบจะมองไม่เห็น แต่ก็สะดุดแน่ ๆ ละ"

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")

scene bg school_track
show rin negative_worried at center
with locationskip

# "Rin inhales sharply, and actually looks concerned for a second."
"รินสะดุ้งเฮือกและดูเป็นห่วงจริง ๆ อยู่แวบหนึ่ง"

# rin "Aw, Emi…"
rin "โธ่เอมิ…"

# hi "Did she hurt herself, do you think?"
hi "เธอว่าเอมิบาดเจ็บมั้ย"

show rin basic_surprised
with charachange

# rin "You noticed it too?"
rin "เห็นด้วยเหรอ"

show rin negative_confused
with charachange

# rin "It must be bad."
rin "ไม่ดีแน่"

show rin negative_annoyed
with charachange

# "She frowns, as if deciding on the next course of action."
"รินขมวดคิ้วราวกับคิดว่าจะทำอย่างไรต่อดี"

# "Eventually that proves to be too tiresome, and she shrugs again."
"สุดท้ายก็ขี้เกียจคิดแล้วยักไหล่"

show rin basic_deadpanupset
with charachange

# rin "Well, let's go down."
rin "อะ ลงไปกัน"

# rin "Gotta crown the victor."
rin "ต้องไปสวมมงกุฎให้ผู้ชนะ"

show rin basic_deadpanamused
with charachange

# rin "See if you can find a laurel branch."
rin "ไปหามงกุฎช่อมะกอกมาที"

# hi "That's not going to be easy."
hi "ยากหน่อยนะ"

show rin basic_deadpannormal
with charachange

# "Rin shrugs."
"รินยักไหล่"

show rin basic_deadpan
with charachange

# rin "At least we tried."
rin "อย่างน้อยก็ได้ลองแล้ว"

# "Well, we didn't really try all that hard."
"ก็ยังไม่ได้พยายามลองกันขนาดนั้น"

# "Or at all. But hey, whatever."
"หรือไม่ได้ลอง แต่เออ ช่างเหอะ"

stop music fadeout 5.0
stop sound fadeout 5.0
play ambient sfx_crowd_outdoors fadein 2.0

scene bg school_track_on
show crowd
show rin basic_awayabsent at center
with locationskip

# "Emi is surrounded by her teammates, all of them congratulating her on the run."
"เพื่อนร่วมทีมเอมิห้อมล้อมเธอฉลองชัยที่วิ่งได้มา"

# "Rin seems to be waiting for Emi to notice that she's arrived."
"ดูเหมือนรินจะรอให้เอมิเห็นอยู่ว่ามาแล้ว"

# "Oh yeah, I guess she can't exactly wave Emi over."
"จริงสิ ยังไงรินก็คงโบกมือให้เอมิไม่ได้อยู่แล้วนี่นะ"

# "Then again, I'm not sure that Rin would do such a thing even if she had arms."
"แต่ก็นะ ต่อให้มีแขนฉันก็ไม่รู้ว่ารินจะโบกหรือเปล่า"

# "It doesn't seem her style to draw attention to herself. Or to emote beyond shrugging."
"เธอดูจะไม่ใช่คนที่เรียกความสนใจจากใครเอง ไม่ใช่คนที่จะแสดงอารมณ์อะไรนอกจากการยักไหล่"

# "Either way, I'm not willing to wait, so I wave to Emi, who looks up and grins happily at me - er, us."
"แต่จะยังไงก็เถอะ ฉันไม่ยอมรอหรอก ฉันโบกมือให้เอมิแล้วส่งยิ้มมีความสุขมาให้ฉัน เอ้อ พวกเรา"

show bg school_track_on at bgright
show crowd at bgright
show rin basic_awayabsent at tworight
with charamove

play music music_emi fadein 1.0

show emi basic_closedhappy_gym at twoleft
with charaenter

# emi "Hey, you showed up!"
emi "ไง มาจนได้นะ!"

show emi excited_proud_gym
with charachange

# emi "Guess Rin owes me money, huh?"
emi "ทีนี้รินก็ติดเงินฉันแล้วสินะ"

show rin basic_deadpanupset
with charachange

# rin "We would have brought you a crown of laurels, but Hisao didn't find one."
rin "จริง ๆ จะมีมงกุฎช่อมะกอกมาให้เธอด้วย แต่ฮิซาโอะหาไม่เจอ"

show emi basic_grin_gym
with charachange

# hi "Hey, neither did you."
hi "เฮ้ย เธอก็หาไม่เจอหรอก"

show rin basic_deadpan
with charachange

# rin "It wasn't my job to look."
rin "ไม่ใช่หน้าที่ฉันสักหน่อย"

# hi "When did we assign jobs?"
hi "นี่ไปแบ่งหน้าที่กันตอนไหน"

show rin basic_deadpannormal
with charachange

# rin "When I said “See if you can find a laurel branch.”"
rin "ตอนที่ฉันบอกว่า “ไปหามงกุฎช่อมะกอกมาที”"

show rin basic_deadpandelight
with charachange

# rin "Try to keep up."
rin "ฟังบ้างสิ"

# "I shrug. Guess Rin's rubbing off on me."
"ฉันยักไหล่ สงสัยติดนิสัยรินมาแล้ว"

# hi "Seems it's my fault after all, Emi."
hi "เหมือนจะเป็นความผิดฉันแหละนะเอมิ"

show emi basic_closedhappy_gym
show rin basic_awayabsent
with charachange

# "Emi laughs at Rin and me."
"เอมิหัวเราะใส่ฉันกับริน"

show emi basic_happy_gym
with charachange

# emi "It's okay, I'm sure you'll make it up to me somehow."
emi "ไม่เป็นไรน่า เดี๋ยวก็คงมาชดใช้ให้ได้อยู่ดีแหละ"

show rin basic_absent
with charachange

# hi "Uh, sure."
hi "อ่า อื้ม"

show rin basic_awayabsent
show emi excited_amused_gym
with charachange

# emi "Good! So, how'd I look?"
emi "ดี! แล้วฉันเป็นไงบ้าง"

show rin basic_absent
with charachange

# "I stop myself from blurting out “beautiful” or “amazing” and settle for the substantially safer “very impressive.”"
"ฉันยั้งปากตัวเองไม่ให้พูดว่า “งดงาม” หรือ “สุดยอด” แล้วใช้คำว่า “ประทับใจมาก” ที่ดูปลอดภัยกว่า"

show emi basic_closedgrin_gym
with charachange

# "Emi seems pleased with this assessment."
"เอมิดูจะพอใจกับคำประเมินที่ว่า"

# "I don't mention how much more impressive her performance is given her lack of legs. I figure she knows that already."
"ฉันไม่พูดต่อว่ายิ่งไม่มีขาแล้วยิ่งน่าประทับใจไปใหญ่เพราะเธอคงรู้อยู่แล้ว"

# "Besides, it seems like it would take away from her efforts, somehow."
"อีกอย่าง เหมือนไปบั่นทอนความพยายามของเธอเองด้วย"

show emi basic_grin_gym
show rin basic_awayabsent
with charachange

# emi "Great to hear! I was worried that I looked a little slow on the relay, but I guess I did fine, huh?"
emi "เยี่ยมเลย! ฉันก็กลัวว่าตอนวิ่งผลัดจะดูช้าไปหน่อย แต่ก็น่าจะใช้ได้แล้วแหละนะ"

show rin basic_absent
with charachange

# hi "Actually, I noticed—{w=.4}{nw}"
hi "ที่จริง ฉันเห็นว่า—{w=.4}{nw}"

play sound sfx_impact

show rin basic_deadpanupset
with vpunch

# "Rin kicks me and keeps me from finishing my sentence."
"รินเตะฉันเป็นการตัดบท"

show emi basic_confused_gym
with charachange

# emi "What was that all about?"
emi "อะไรเหรอ"

show rin basic_deadpancontemplation
with charachange

# rin "He noticed it. At the end."
rin "ฮิซาโอะเห็น ตอนท้าย"

show emi basic_annoyed_gym
with charachange

# emi "Hmm, that's no good."
emi "อืมม แย่แล้วสิ"

show emi sad_grin_gym
with charachange

# emi "Guess the nurse will look at it for me later."
emi "เดี๋ยวไปให้คุณพยาบาลดูแล้วกัน"

show emi sad_grit_gym
with Dissolve(0.2)

show emi sad_grin_gym
with charachange

# "There's a carelessness in her voice, as if it isn't a big deal, but I suddenly notice a slight twitch on her face."
"น้ำเสียงเอมิฟังดูไม่ยี่หระเหมือนไม่ใช่เรื่องใหญ่ แต่อยู่ ๆ ฉันก็เห็นว่าเธอหน้าเสียไปเล็กน้อย"

# "Like she's trying to hide the fact that she's in pain."
"เหมือนกับกำลังปกปิดว่าตัวเองเจ็บอยู่"

# "It's then that I notice her breathing is a little shallow, too."
"และตอนนั้นเองฉันก็เห็นด้วยว่าเอมิหายใจถี่ขึ้นเล็กน้อย"

# "I guess she really is hurt."
"คงจะเจ็บจริง ๆ"

# "She must notice my concern, because she skips up to me and gives me a friendly pat on the shoulder."
"เอมิคงเห็นว่าฉันเป็นห่วงถึงได้โดดมาหาฉันแล้วตบบ่าอย่างเป็นมิตร"

show emi basic_closedgrin_gym_close
show rin basic_deadpannormal
with characlose

# emi "Hey, you look a little worried!"
emi "นี่ นายดูกังวล ๆ นะ!"

show emi basic_grin_gym_close
with charachange

# emi "I'm fine, really!"
emi "ฉันไม่เป็นไรจริง ๆ !"

# emi "Just sore from all the running, is all."
emi "แค่วิ่งจนล้าเท่านั้นเอง"

show emi excited_proud_gym_close
with charachange

# emi "And come on, a little pain isn't going to stop me."
emi "แล้วก็เนี่ย ความเจ็บแค่นี้ทำอะไรฉันไม่ได้หรอก"

# hi "Oh no?"
hi "ไม่นะ?"

show emi basic_closedgrin_gym_close
with charachange

# "Emi grins, and for a moment she looks like she did during her sprint, fierce and unconquerable."
"เอมิยิ้มพร้อมทำหน้ามุ่งมั่นและไม่อาจมีใครทัดเทียมเหมือนอย่างตอนที่วิ่งนั้นอยู่แวบหนึ่ง"

# "Or to put it another way, really beautiful."
"หรือจะพูดง่าย ๆ ก็คือ สวยมาก ๆ"

show emi basic_grin_gym_close
with charachange

# emi "Hasn't yet."
emi "ยังหรอกน่า"

# hi "Well then. I guess I shouldn't worry, huh?"
hi "เอาเถอะ งั้นก็คงไม่ต้องเป็นห่วงสินะ"

show emi basic_closedhappy_gym_close
with charachange

# emi "Damn right! I'm Emi Ibarazaki, fastest thing on no legs! I don't stop for anything!"
emi "ใช่เลย! ฉันคือเอมิ อิบาราซากิ สิ่งไม่มีขาที่เร็วที่สุด! ไม่มีอะไรมาหยุดยั้งฉันได้!"

# hi "Impressive."
hi "ช่างน่าประทับใจ"

show emi basic_closedgrin_gym_close
with charachange

# "Emi giggles, and then seems to remember something."
"เอมิหัวเราะคิกคักแล้วทำท่าเหมือนนึกอะไรขึ้นได้"

show emi basic_grin_gym_close
with charachange

# emi "Oh, before I forget…"
emi "อ้อ ก่อนจะลืม…"

# emi "Rin and I are going to do something next Sunday as a post-track meet celebration!"
emi "รินกับฉันจะไปฉลองที่แข่งวิ่งเสร็จกันวันอาทิตย์หน้าละ!"

show emi excited_proud_gym_close
with charachange

# emi "You should come along!"
emi "นายมาด้วยก็ดีนะ!"

show emi sad_grin_gym_close
with charachange

# emi "Normally we do it the day after, but since the track meet was on a Sunday, I've got homework and class and all that stuff to take care of."
emi "ปกติจะไปฉลองหลังวันแข่งเลย แต่พอดีวันนี้วันอาทิตย์ เดี๋ยวมีการบ้านมีเรียนมีอะไรอีก"

show emi basic_closedgrin_gym_close
with charachange

# emi "Plus our morning run, of course."
emi "แล้วก็แน่นอนว่ามีวิ่งตอนเช้าของเราด้วย"

# hi "Right, of course."
hi "อืม ตามนั้น"

# hi "Oh, right. Your mom wanted to say she's proud of you."
hi "เอ้อ จริงสิ แม่เธอฝากบอกว่าภูมิใจในตัวเธอมาก"

# hi "She'll call you later tonight."
hi "แล้วก็คืนนี้แม่เธอจะโทร. ไปหาอีกที"

show emi basic_happy_gym_close
with charachange

# emi "I thought I saw her in the stands!"
emi "ก็ว่าเหมือนเห็นที่สแตนด์อยู่!"

show emi basic_closedhappy_gym_close
with charachange

# emi "I'm glad she made it!"
emi "ดีใจจังที่แม่มาดูจนได้!"

show emi sad_grin_gym_close
with charachange

# emi "Used to be my dad who showed up to my meets, but Mom's done a pretty good job of taking over."
emi "ปกติตอนงานแข่งวิ่งพ่อฉันจะมาดู แต่แม่ก็มาทำหน้าที่แทนได้ดีเหมือนกัน"

show emi sad_shy_gym_close at Transform(function=tf_lefttremble)
with Dissolve(0.1)

# "She shivers slightly, and I realize that she's still all sweaty."
"เอมิตัวสั่นน้อย ๆ ฉันเห็นว่าเธอยังเหงื่อโชกอยู่"

# "A breeze has started to blow, too."
"ลมก็เริ่มพัดแล้วด้วย"

# "I'm not cold at all, and I've got my jacket with me, so without a word I throw it around her shoulders."
"เพราะฉันไม่หนาวเลยและเอาเสื้อแจ็กเก็ตมาด้วย ฉันจึงเอาเสื้อแจ็กเก็ตตัวนั้นคลุมไหล่เอมิไว้โดยไม่พูดอะไร"

play sound sfx_rustling

show emi basic_shock_gym_close at twoleft
with vpunch

with Pause(0.5)

show emi basic_grin_gym_close
with charachange

# "Emi jumps slightly and then grins at me."
"เอมิสะดุ้งเล็กน้อยก่อนจะหันมาส่งยิ้มให้"

show emi basic_closedhappy_gym_close
with charachange

# emi "Hey, thanks!"
emi "อ้าว ขอบคุณนะ!"

show emi sad_grin_gym_close
with charachange

# emi "It's getting a little cold, I guess."
emi "ชักเย็น ๆ ยังไงไม่รู้"

# hi "Yeah, looked like it."
hi "อืม เหมือนจะนะ"

# "Just as I begin to wonder whether or not giving Emi my jacket could be taken the wrong way, a boy in a track uniform approaches."
"ระหว่างที่คิดอยู่ว่าการให้เสื้อแจ็กเก็ตกับเอมินั้นจะชวนให้เข้าใจผิดหรือเปล่าก็มีเด็กชายในชุดพละเดินเข้ามา"

# "Teammate" "Hey, Emi! You're going to miss the medal ceremony!"
thname("เพื่อนร่วมทีม") "นี่ เอมิ! เดี๋ยวก็ไม่ทันไปรับเหรียญรางวัลหรอก!"

show emi basic_closedgrin_gym_close
with charachange

# emi "Oh yeah, thanks!"
emi "อ้อ จริงด้วย ขอบใจนะ!"

show emi basic_grin_gym
show rin basic_awayabsent
with charadistant

# "She turns to Rin and myself."
"เธอหันมาหารินและฉัน"

# emi "You don't have to stick around for this part. It takes forever."
emi "ไม่ต้องอยู่รอก็ได้นะ พิธีนานเป็นชาติเลย"

show emi basic_closedgrin_gym
with charachange

# emi "Besides, you should get cracking on your homework now if you don't want to be up late, Hisao."
emi "อีกอย่าง ถ้าไม่อยากนอนดึกก็รีบไปทำการบ้านได้แล้วนะฮิซาโอะ"

show emi excited_proud_gym
with charachange

# emi "Morning run tomorrow! Don't forget!"
emi "วิ่งพรุ่งนี้เช้าอีก! อย่าลืมนะ!"

show rin basic_absent
with charachange

# hi "How could I?"
hi "จะลืมได้ไงลง"

show emi basic_closedhappy_gym
show rin basic_awayabsent
with charachange

# emi "Good point. I mean, it's spending time with {b}me{/b}, after all."
emi "ก็จริง ได้มาใช้เวลาอยู่กับ{b}ฉัน{/b}นี่นะ"

play sound sfx_emirunning

hide emi
with easeoutleft

stop sound fadeout 3.0

show bg school_track_on at center
show crowd at center
show rin basic_awayabsent at center
with charamove

# "With this, she waves quickly and dashes off to receive her medals, or whatever they pass off as a medal these days."
"แล้วเอมิก็โบกมือหย็อย ๆ ก่อนจะพุ่งตัวไปรับเหรียญรางวัลของเธอ หรือรับอะไรก็ช่างที่เดี๋ยวนี้เขาให้เป็นรางวัลกัน"

scene bg school_courtyard
show crowd
show rin relaxed_nonchalant at center
with locationskip

stop music fadeout 7.0

# "Rin and I head away from the track, Rin remaining deep in whatever thoughts she has for most of the walk back to her dorm."
"รินกับฉันเดินออกมาจากลู่ โดยตลอดทางที่เดินรินก็เหมือนจะครุ่นคิดอะไรอยู่อย่างจริงจัง"

# "As I see her off, she speaks up."
"พอจะบอกลารินก็พูดขึ้นมา"

show rin basic_deadpan
with charachange

# rin "You're probably not getting that coat back, I think."
rin "นายคงจะไม่ได้เสื้อตัวนั้นคืนแล้วแหละ คิดว่านะ"

# hi "I'm sure I'll get it back eventually."
hi "ฉันมั่นใจว่าสักวันก็ได้คืนน่า"

show rin basic_deadpannormal
with charachange

# rin "Interesting. Take it as it comes, huh?"
rin "น่าสนใจ รอดูไปเรื่อย ๆ งั้นเหรอ"

show rin basic_deadpandelight
with charachange

# rin "Very Emi-ish."
rin "มีความเป็นเอมิมาก ๆ"

hide rin
with charaexit

# "With this odd statement, she turns and heads into the building."
"รินพูดคำแปลก ๆ นั้นแล้วหมุนตัวกลับไปที่หอ"

# "Honestly, was it that big a deal?"
"เอาจริง ๆ มันเรื่องใหญ่ขนาดนั้นเลยเหรอ"

# "Emi was cold and, unless I'm mistaken, in pain."
"เอมิก็หนาวและเจ็บด้วย ถ้าดูไม่ผิดน่ะนะ"

# "Giving her a solution to at least one of those problems seems like an obvious reaction."
"ก็ไม่แปลกหรือเปล่าที่จะตอบสนองด้วยการแก้ปัญหาให้อย่างน้อยก็อย่างหนึ่ง"

# "Though I guess there is a chance I could lose my jacket if Emi never remembers to return it."
"แต่ก็มีโอกาสที่ฉันจะไม่ได้เสื้อแจ็กเก็ตคืนเหมือนกันถ้าเอมิลืม"

# "I guess Rin has a point."
"ก็คงถูกของริน"

# "Still, I can't bring myself to muster much worry over the whole thing."
"แต่ก็นะ ฉันไม่อยากจะมานั่งคิดพะวงกับเรื่องนี้หรอก"

# "After all, it's been getting warmer lately."
"ช่วงนี้อากาศก็เริ่มอุ่นขึ้นแล้วด้วย"

# "I don't need a jacket."
"ไม่ต้องใส่เสื้อแจ็กเก็ตหรอก"

# "Odd. I think I used to be a little more responsible with my stuff."
"แปลก ฉันว่าปกติฉันมีความรับผิดชอบกับของของตัวเองมากกว่านี้นะ"

# "“Emi-ish,” huh?"
"“ความเป็นเอมิ” เหรอ"

# "Maybe that's not really a bad thing."
"ก็คงไม่ได้แย่ขนาดนั้น"

stop ambient fadeout 2.0

scene black
with dissolve

########################################################
label th_E9:

scene bg school_nurseoffice
show nurse concern at center
with locationchange

# nk "You haven't been forgetting to take your medicine, have you?"
nk "ช่วงนี้ยังกินยาตามปกติอยู่ใช่มั้ย"

play music music_nurse fadein 0.5

# nk "I'm catching a little murmur."
nk "ไม่ค่อยได้ยินเลยนะ"

# nk "You should take it easy for a few days."
nk "สักสองสามวันนี้เพลา ๆ บ้างก็ได้"

# "The nurse's words hurt me far more than the exhaustion of the morning run ever could."
"คำพูดของคุณพยาบาลทำร้ายจิตใจฉันหนักกว่าการวิ่งยามเช้าอีก"

# "Take it easy for a few days?"
"สักสองสามวันนี้เพลา ๆ บ้างก็ได้เหรอ"

# "I knew I should have kept quiet."
"ไม่น่าบอกเลย"

# "I keep my eyes on the floor, feeling like a complete idiot."
"ฉันก้มมองพื้นด้วยความรู้สึกเหมือนเป็นคนโง่"

# "Of course I hadn't been remembering to take my medicine."
"แหงละว่าฉันลืมกินยา"

# "I've been rushing out of my room to get to the track before Emi."
"ช่วงนี้ฉันรีบออกจากห้องไปหาเอมิที่ลู่วิ่ง"

# "After the track meet a few days ago, I felt… inspired."
"พอได้ดูงานแข่งเมื่อสองสามวันที่ผ่านมาแล้ว ฉันก็… มีแรงบันดาลใจขึ้นมา"

# "So I've been running warm-up laps in the morning before Emi shows up."
"ฉันเลยวิ่งรอบเช้าเป็นการวอร์มอัพรอเอมิมา"

# "But then today while she and I were running, I felt a little pain in my chest."
"แต่วันนี้ตอนที่เราวิ่งด้วยกันฉันก็เจ็บหน้าอกขึ้นมา"

# "It was only slight, and it was only for a second, so I mentioned it to the nurse."
"เจ็บแปลบ ๆ อยู่แวบหนึ่ง ฉันถึงได้เอามาเล่าให้คุณพยาบาลฟัง"

# hi "Honestly, it wasn't that bad."
hi "จริง ๆ ก็ไม่ได้หนักขนาดนั้นหรอกครับ"

# hi "I mean I kept running and finished just fine, so really it couldn't have been that bad…"
hi "คือผมก็วิ่งต่อจนครบรอบได้ปกติดี น่าจะไม่หนักมาก…"

# "Why do I feel like I'm making excuses to the nurse?"
"ทำไมถึงรู้สึกเหมือนแก้ตัวอยู่กับคุณพยาบาลเลยนะ"

# "Moreover, why do I feel a need to justify continuing to run despite the pain?"
"แล้วทำไมฉันถึงต้องหาข้ออ้างมาวิ่งต่อทั้งที่เจ็บหน้าอกด้วย"

# "Really, it comes down to my being unwilling to concern Emi, who seemed concerned anyway."
"ลึึก ๆ แล้วก็คงเป็นเพราะไม่อยากให้เอมิเป็นห่วงนั่นแหละ ซึ่งเธอก็ดูจะเป็นห่วงอยู่ดี"

# "I'm not sure how she was able to tell there was anything wrong, but she claims I stumbled a little."
"ฉันไม่แน่ใจว่าเอมิจับสังเกตความผิดปกติได้ยังไง แต่เห็นบอกว่าฉันสะดุด"

# "She's the one who insisted I tell the nurse, so now I feel bad for worrying her at all."
"เอมิเป็นคนที่คะยั้นคะยอให้ฉันมาบอกคุณพยาบาล ตอนนี้ฉันเลยรู้สึกแย่ที่ทำให้เธอต้องเป็นห่วง"

# "The nurse is shaking his head ruefully while Emi paces outside the room."
"คุณพยาบาลส่ายหัวเศร้า ๆ ระหว่างที่เอมิเดินออกจากห้องไป"

# nk "Hisao, I know it's difficult for you get into a new routine, but if you don't want to find yourself in a lot of trouble you're going to have to try harder."
nk "ฮิซาโอะ ฉันรู้ว่ากว่าจะทำตัวให้ชินกับกิจวัตรได้มันลำบาก แต่ถ้าไม่อยากให้ตัวเองต้องเจออะไรที่หนักกว่านี้อีก\nเธอก็ต้องพยายามหน่อยนะ"

# nk "You can't afford to forget your pills, and you can't push yourself too hard."
nk "ห้ามลืมกินยา แล้วก็ห้ามฝืนตัวเองมากไปด้วย"

# hi "But if I don't push myself, how will I improve?"
hi "แต่ถ้าผมไม่ฝืนตัวเองแล้วผมจะพัฒนาได้ยังไงล่ะครับ"

# "I don't know where that came from."
"ฉันไม่รู้ว่าอะไรดลใจให้ฉันพูดอย่างนั้น"

# "The nurse seems to have an idea."
"คุณพยาบาลทำท่าเหมือนนึกอะไรออก"

show nurse fabulous
with charachange

# nk "Now where have I heard that before?"
nk "เหมือนเคยได้ยินที่ไหนมาก่อนนะ"

show nurse grin
with charachange

# "He laughs and pats me on the shoulder."
"คุณพยาบาลหัวเราะแล้วตบบ่าฉัน"

# nk "Ha! She's rubbing off on you, I guess."
nk "ฮ่า! ติดนิสัยเขามาแล้วละสิ"

show nurse concern
with charachange

# "His expression changes again, and he's back in serious mode."
"สีหน้าคุณพยาบาลเปลี่ยนไปอีกรอบกลับเข้าสู่โหมดจริงจัง"

# nk "Look, I'm not saying you shouldn't push yourself."
nk "นี่นะ ฉันก็ไม่ได้บอกว่าเธอไม่ควรฝืนตัวเอง"

# nk "But that doesn't mean you shouldn't be taking your medication, and it doesn't mean you shouldn't stop if your chest starts to bother you."
nk "แต่ก็ไม่ได้แปลว่าจะไม่กินยาได้นะ แล้วก็ไม่ได้แปลว่าเธอควรไปต่อถ้าเริ่มรู้สึกเจ็บหน้าอกขึ้นมา"

# nk "I'd prefer not to have any fatalities while I'm on staff here."
nk "ฉันไม่อยากให้ใครต้องมาตายตอนที่ฉันยังทำงานอยู่"

show nurse neutral
with charachange

# nk "A bit of a lofty goal, to be sure, but I'm always up for a challenge."
nk "เป็นเป้าหมายที่สูงไปหน่อยก็จริง แต่ฉันชอบความท้าทายนะ"

# "I hate to admit it, but I think he's right."
"ไม่อยากยอมรับเท่าไหร่ แต่คุณพยาบาลก็พูดถูก"

# "I've got to remember to take my medication."
"ฉันต้องห้ามลืมกินยา"

# hi "You're right. I'm sorry to worry you."
hi "นั่นสินะครับ ขอโทษที่ทำให้เป็นห่วง"

show nurse fabulous
with charachange

# nk "Who's worried? You're a smart kid, right?"
nk "ใครเป็นห่วง ไม่มี เธอฉลาดนี่ ใช่มั้ย"

show nurse neutral
with charachange

# nk "I know you can be responsible, Hisao. A situation like yours, you've got to learn to be responsible fast."
nk "ฉันรู้ว่าเธอก็มีความรับผิดชอบเหมือนกันนะฮิซาโอะ ใครมาเป็นอย่างเธอก็ต้องหัดมีความรับผิดชอบกันทั้งนั้นแหละ"

# hi "I know, I know."
hi "ทราบครับ ๆ"

# "His expression suddenly becomes devious."
"อยู่ ๆ คุณพยาบาลก็ทำหน้าชั่วร้ายขึ้นมา"

show nurse fabulous
with charachange

# nk "I suppose you've started to enjoy your runs with Emi then, eh?"
nk "แปลว่าสนุกที่ได้วิ่งกับเอมิแล้วสินะ"

# hi "Yeah, they've really been helping me."
hi "ครับ ช่วยได้เยอะเลย"

# hi "I mean, until today I was feeling a lot more healthy."
hi "คือช่วงนี้ผมรู้สึกแข็งแรงดีขึ้นมา"

# hi "Plus it's really impressive to see Emi run. Did you see her at the track meet?"
hi "อีกอย่าง ผมประทับใจมากที่ได้เห็นเอมิวิ่ง คุณพยาบาลเห็นตอนงานแข่งวิ่งนั้นมั้ยครับ"

# hi "She was incredible!"
hi "เอมิน่ะสุดยอดไปเลย!"

show nurse grin
with charachange

# "The nurse nods, grinning all the while."
"คุณพยาบาลพยักหน้ายิ้มน้อยยิ้มใหญ่"

# nk "That she was, Hisao. I watched her first couple of races before I had some business to take care of, but she told me all about it."
nk "สุดยอดจริงแหละนะฮิซาโอะ งานแข่งสองสามครั้งแรกฉันก็ได้ดูอยู่ หลังจากนั้นก็มีธุระเลยไปไม่ได้ แต่เอมิ\nเล่าให้ฟังหมดนะ"

show nurse fabulous
with charachange

# nk "Kind of you to loan her your jacket, by the way."
nk "เธอนี่ก็ใจกว้างเหมือนกันนะที่ให้เอมิยืมเสื้อแจ็กเก็ตน่ะ"

# hi "Huh? Oh yeah, it wasn't that big of a deal."
hi "ครับ? อ้อ ครับ แต่ก็เรื่องแค่นี้เอง"

# "I had honestly forgotten all about that. I still haven't gotten it back."
"ว่าตามตรงก็ลืมไปเสียสนิท ฉันยังไม่ได้เสื้อตัวนั้นคืนเลย"

show nurse neutral
with charachange

# "The nurse gets a smile that makes me feel like he's just made a joke."
"คุณพยาบาลยิ้มชวนให้รู้สึกเหมือนกำลังเล่นมุกตลกอะไรอยู่"

# nk "Not to you, but Emi certainly appreciated it."
nk "ฉันไม่ได้ขอบคุณเธอนะ แต่เอมิเขาขอบคุณแน่ ๆ ละ"

# nk "And I know she appreciates your running with her in the mornings."
nk "และรู้ด้วยเอมิก็ขอบคุณที่เธอไปวิ่งตอนเช้าด้วย"

# "This one catches me off guard a little. Sure, she mentioned that it's easier to keep to a schedule with an extra person, but I didn't think that I was doing her a favor at all."
"อย่างหลังนี่มาไม่ทันตั้งตัวเลยแฮะ จริงอยู่ว่าเอมิเคยบอกว่าพอทำอะไรกับใครอีกคนเป็นประจำแล้วจะมีแรงทำต่อขึ้นมา\nแต่ไม่เคยคิดเลยว่าฉันได้ช่วยอะไรเอมิ"

# hi "I thought she was doing me the favor of helping me follow the doctor's orders."
hi "ผมคิดว่าเอมิเขาแค่มาช่วยผมทำตามหมอสั่งเฉย ๆ"

# nk "She tries harder when you're around."
nk "พอมีเธอแล้วเอมิก็ทุ่มเทขึ้นนะ"

# nk "If there's someone else running with her, she's going to push herself more."
nk "ถ้ามีคนมาวิ่งด้วยแล้วเอมิก็จะผลักดันตัวเองให้มากขึ้น"

# nk "And she tries even harder when you're around because, well, it's you."
nk "แล้วก็ยิ่งทุ่มเทขึ้นไปอีกพอมีเธออยู่ด้วยเพราะ ก็เนี่ย คนที่ว่าคือเธอ"

# hi "What the heck does that mean?"
hi "หมายความว่าอะไรเนี่ยครับ"

show nurse grin
with charachange

# nk "Oh ho, you'd love to know, wouldn't you?"
nk "อ้าว ๆ อยากรู้ละสิเรา"

# "He laughs in the style of evil megalomaniacs."
"คุณพยาบาลหัวเราะเหมือนตัวร้ายในหนังที่จะครองโลก"

show nurse neutral
with charachange

# nk "No seriously, it's because you're her friend."
nk "ไม่ จริง ๆ เพราะเธอเป็นเพื่อนเอมิต่างหาก"

# nk "If Rin ran with her, I'm sure she'd do the same."
nk "ถ้ารินวิ่งด้วยฉันว่าก็ได้ผลเหมือนกันแหละ"

# nk "Well, probably."
nk "มั้งนะ"

# nk "But that's not the point."
nk "แต่ประเด็นไม่ได้อยู่ตรงนั้น"

# nk "The point is, you're helping her, even if you don't know you are."
nk "ประเด็นคือเธอช่วยเอมิอยู่ ต่อให้เธอจะไม่รู้ตัวก็เถอะ"

show nurse fabulous
with charachange

# nk "And she's grateful for that, even if she never says it."
nk "ซึ่งเอมิก็ยินดีนะ ต่อให้เจ้าตัวจะไม่เคยพูดเลยก็เถอะ"

# hi "What do you mean “even if she never says it?”"
hi "ที่ว่า “เจ้าตัวไม่เคยพูดเลย” นี่หมายความว่ายังไงครับ"

show nurse neutral
with charachange

# nk "Emi doesn't talk a lot, but she and I have known each other long enough that I can read her most of the time."
nk "เอมิเป็นคนพูดน้อยนะ แต่ฉันก็รู้จักกับเอมิมานานพอที่จะอ่านใจเอมิได้บ้าง"

# "I'll admit it. I have no idea what he's talking about."
"ยอมรับเลยว่าฉันไม่เข้าใจที่คุณพยาบาลพูดเลย"

# "Emi always seems pretty talkative to me."
"ฉันว่าเอมิก็ดูเป็นคนพูดมากนะ"

# hi "I see."
hi "อย่างนี้นี่เอง"

# "The nurse suddenly realizes that he's been rambling and stops talking, looking a little embarrassed."
"อยู่ ๆ คุณพยาบาลก็นึกได้ว่าพล่ามอะไรยืดยาวแล้วหยุดพูดไปดูเขิน ๆ"

show nurse fabulous
with charachange

# nk "Anyway, you don't have to stop your morning exercise."
nk "แต่นั่นแหละ ไม่ต้องเลิกวิ่งรอบเช้าหรอก"

show nurse neutral
with charachange

# nk "Just walk the track instead of running for a few days. Let things calm down."
nk "สองสามวันนี้ก็เดินรอบลู่เฉย ๆ ก็พอ ให้อะไร ๆ มันสงบลงก่อน"

show nurse concern
with charachange

# nk "And take your damned medicine!"
nk "แล้วก็กินยาด้วยนะ!"

scene bg school_nursehall
with locationchange

stop music fadeout 0.3
play sound sfx_impact

show emi basic_confused_gym_close
with vpunch

# "I laugh as I exit the office, bumping straight into Emi."
"ฉันออกจากห้องพยาบาลมาพลางหัวเราะแล้วชนเข้ากับเอมิ"

show emi basic_confused_gym
with charadistant

# hi "Whoops, sorry about that."
hi "โอ๊ะ ขอโทษที"

show emi basic_hes_gym
with charachange

# emi "Are you okay? What did the nurse say?"
emi "ไหวมั้ย คุณพยาบาลว่ายังไงบ้าง"

# emi "Do you need to go to a hospital?"
emi "ต้องไปโรงพยาบาลหรือเปล่า"

show emi basic_shock_gym
with charachange

# emi "Omigosh, it was my fault, wasn't it?"
emi "ตายแล้ว ๆ ฉันผิดสินะเนี่ย"

show emi basic_closedsweat_gym
with charachange

# emi "I've been pushing you too hard, haven't I?"
emi "ฉันฝืนนายมากไปใช่มั้ย"

show emi excited_sad_gym
with charachange

# emi "I'm a horrible person!"
emi "ฉันนี่แย่จริง ๆ !"

# "The words pour forth like a torrent. She's really agitated."
"คำพูดไหลบ่ามาราวน้ำเชี่ยว เอมิตื่นตระหนกมาก"

# "I didn't expect her to be this concerned about me, to be honest."
"ไม่คิดเลยว่าจะเป็นห่วงกันขนาดนี้ ถ้าให้ว่ากันตรง ๆ"

# "Gotta calm her down… but how the hell do I do that?"
"ต้องปลอบเอมิก่อน… แต่จะทำยังไงดีวะ"

# "I do the only thing I can think of."
"มีอย่างเดียวที่ฉันนึกขึ้นได้"

show emi basic_shock_gym_close
with characlose

play music music_serene fadein 6.0

# "I give her a hug. Emi tenses up slightly, so I pat her head in what I hope is a reassuring manner."
"ฉันกอดเอมิ ตัวเธอเกร็งเล็กน้อย ฉันจึงลูบหัวด้วยหวังว่าพอจะปลอบใจเธอได้บ้าง"

# hi "Hey, settle down!"
hi "นี่ ใจเย็นก่อน!"

# hi "I'm fine, okay? No worries."
hi "ฉันไม่เป็นไรน่า อย่าห่วงเลย"

show emi basic_hes_gym_close
with charachange

# "I can feel Emi's body relax as I continue to assure her I'm fine."
"ระหว่างที่ปลอบว่าไม่เป็นไรอะไรแล้วนั้นก็รู้สึกว่าตัวเอมิผ่อนคลายลง"

# "Her arms wrap around me, as if she's trying to confirm that I'm not about to fall over dead."
"เอมิโอบฉันไว้ราวกับจะรั้งให้แน่ใจว่าฉันจะไม่ล้มพับตายไปเสียดื้อ ๆ"

# "I catch a whiff of her hair. It smells like sweat, or how adrenaline should smell. It's the scent of activity."
"ฉันได้กลิ่นผมเอมิ เหมือนเป็นกลิ่นเหงื่อ หรืออาจจะมาจากสารอะดรีนาลิน เป็นกลิ่นของคนที่ไม่อยู่นิ่ง"

# "And a hint of strawberries. From her shampoo, I suspect."
"แล้วก็มีกลิ่นสตรอว์เบอร์รีอ่อน ๆ น่าจะกลิ่นแชมพู"

# hi "I just need to remember to take my medicine, that's all."
hi "แค่ต้องเตือนตัวเองไม่ให้ลืมกินยา แค่นั้นแหละ"

# hi "Don't worry about it. It's not your fault."
hi "ไม่ต้องห่วงน่า ไม่ใช่ความผิดเธอเลย"

show emi sad_depressed_gym_close
with charachange

# emi "You're sure?"
emi "แน่ใจนะ"

# "Her voice is muffled, mostly because at the moment her face is pressed into my chest."
"เสียงเอมิอู้อี้ ซึ่งหลัก ๆ ก็เพราะตอนนี้เธอซุกหน้าอกฉันอยุ่"

# hi "Yeah, I'm sure. I just need to take it a little easy for the next few days."
hi "อื้ม แน่ใจสิ แค่สองสามวันนี้ต้องเพลา ๆ บ้าง"

# "It suddenly occurs to me how close the two of us are."
"ฉันฉุกคิดขึ้นมาได้ว่าเราสองคนสนิทกันขนาดไหน"

# "It also occurs to me how nice being this close feels."
"และฉุกคิดได้ด้วยว่าการได้อยู่ใกล้กันขนาดนี้รู้สึกดีเพียงไร"

# "I can feel Emi's heartbeat calming down, and I have to resist the urge to rest my chin on the top of her head."
"ฉันสัมผัสได้ว่าหัวใจเอมิเต้นช้าลงแล้ว และต้องหักห้ามใจตัวเองไม่ให้เอาคางไปเกยหัวเอมิ"

show emi sad_grin_gym_close
with charachange

# emi "Thank goodness."
emi "โล่งไปที"

# emi "You really had me worried there, Hisao."
emi "ฉันเป็นห่วงนายแทบแย่ ฮิซาโอะ"

stop music fadeout 1.5

show nurse concern behind emi:
    center
    xpos 0.0 xanchor 0.3
    easein 0.5 xanchor 0.2
with Dissolve(0.5)

# nk "Emi, you going to come in here any time soon?"
nk "เอมิ เมื่อไหร่เธอจะเข้ามาสักที"

show nurse grin
with charachange

# nk "…Oh, I'm sorry. Was I interrupting?"
nk "…อ้าว ขอโทษที มาขัดหรือเปล่า"

show emi basic_shock_gym
with vpunch

# "The two of us spring apart as if the other just caught on fire."
"เราเด้งผละตัวออกจากกันราวกับว่าต่างคนต่างมีไฟติดตัวอยู่"

show emi basic_hes_gym
with charachange

# "Emi brushes her hair back nervously and laughs."
"เอมิปัด ๆ ผมตัวเองด้วยความประหม่าแล้วหัวเราะ"

play music music_emi fadein 1.0

# emi "'Course not!"
emi "ขัดอะไรเล่า!"

show emi sad_shy_gym
show nurse fabulous
with charachange

# emi "I'll uh… see you later, okay?"
emi "เดี๋ยว เอ่อ… ไว้เจอกัน โอเคนะ"

show emi basic_closedgrin_gym
with charachange

# emi "Oh, and Hisao?"
emi "อ้อ แล้วก็นะฮิซาโอะ"

# hi "Hmm?"
hi "หืม"

show emi basic_annoyed_gym_close
with characlose

with hpunch

# emi "Take your damn medicine!"
emi "กินยาด้วยนะ!"

# "This last phrase is punctuated by a punch to the shoulder."
"ประโยคปิดท้ายนั้นมาพร้อมกับการต่อยไหล่เน้นย้ำ"

# hi "Yeah, yeah, I'll remember."
hi "อืม ๆ จะพยายามไม่ลืม"

# hi "See you later."
hi "เจอกัน"

show nurse grin
with charachange

# "The nurse smiles again like he's in on some joke I don't know about and waves to me as I head for my room, feeling a burning in my cheeks."
"คุณพยาบาลยิ้มเหมือนเตรียมเล่นตลกอะไรที่ฉันไม่อาจรู้ได้แล้วโบกมือให้ระหว่างที่ฉันกลับห้องพร้อมแก้มที่ร้อนผ่าว"

stop music fadeout 8.0

scene bg school_dormhisao
with locationskip

# "I need a shower."
"ต้องอาบน้ำ"

# "A cold one, if the thoughts running through my head now are any indication."
"ดูจากความคิดที่แล่นอยู่ในหัวแล้วต้องอาบน้ำเย็นด้วย"

# "She was really soft."
"เอมิตัวนิ่มจริง ๆ"

# "My pills are waiting for me when I make it to my room."
"พอกลับถึงห้องยาก็รอฉันอยู่แล้ว"

# "I swallow them without a second thought."
"ฉันกลืนยาลงไปทันทีไม่คิดอะไร"

# "I don't know why I didn't think of waiting until after the runs to take them. For some reason I figured it was when I woke up or not at all."
"ไม่รู้ทำไมถึงไม่เคยคิดจะมากินยาหลังวิ่ง เหมือนถ้าไม่ได้กินตอนตื่นมาแล้วก็จะไม่กินไปเลย"

# "But no, they only need to be taken every twenty-four hours. The exact time of day doesn't factor into it."
"แต่ไม่เลย ยานี้ต้องกินทุก ๆ ยี่สิบสี่ชั่วโมง ไม่เกี่ยวว่าจะต้องกินตอนกี่โมงของแต่ละวัน"

# "My thoughts drift back to the hug in the hallway."
"ฉันย้อนนึกไปถึงอ้อมกอดที่โถงทางเดินนั้น"

# "It's weird, you'd expect someone to smell foul after a run, but for some reason, Emi smelled… right. That tinge of sweat just seemed to fit her."
"แปลก ปกติถ้าคนเพิ่งวิ่งมาแล้วจะรู้สึกว่ากลิ่นต้องเหม็น แต่ไม่รู้ทำไม กลิ่นของเอมิถึงได้… ลงตัว กลิ่นเหงื่อที่เจืออยู่นั้น\nดูจะเข้ากับตัวเอมิดี"

# "I really need that shower."
"ฉันต้องไปอาบน้ำแล้วแหละ"

scene black
with dissolve

$ suppress_window_after_timeskip = True

########################################################
label th_E10:

window hide None

scene bg school_roof
with locationchange

nvl clear

nvl show dissolve

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_rooftop fadein 1.0

# n "\n\nStrange that it feels so natural for me to go up to the roof these days."
n "\n\nแปลกดีที่ช่วงสองสามวันมานี้ฉันชินกับการขึ้นมาดาดฟ้าแล้ว"

# n "I never would have done such a thing at my old school."
n "ถ้าเป็นที่โรงเรียนเก่าละก็ฉันแทบไม่มาทำอะไรแบบนี้เลย"

# n "In those days I liked to eat alone… no, that's not quite true. Though I liked to sit alone, I also liked to watch people."
n "สมัยนั้นฉันชอบกินข้าวคนเดียว… ไม่สิ ก็ไม่เชิง ถึงจะชอบนั่งคนเดียวแต่ก็ชอบดูผู้คนไปด้งบ"

# n "I always figured that was the sort of person I was, but it appears I was wrong."
n "ฉันคิดมาตลอดว่าตัวเองเป็นคนแบบนั้น แต่เหมือนจะคิดผิด"

# n "Then again, I also thought I was the sort of person who had a normal heart, so there you have it."
n "แต่ก็นะ ฉันเคยคิดเหมือนกันว่าฉันเป็นคนที่หัวใจปกติ นั่นแหละ"

# n "I don't know myself that well."
n "ฉันไม่ได้รู้จักตัวเองดีขนาดนั้น"

# n "Now I'm on the roof so that I can have lunch with a couple of people."
n "ตอนนี้ฉันมาอยู่ที่ดาดฟ้าเพื่อกินข้าวเที่ยงกับคนอีกสองคน"

# n "And they are both girls, which is even stranger."
n "และทั้งสองคนก็เป็นผู้หญิง ซึ่งแปลกไปใหญ่"

# n "Oddly enough, I feel closer to Emi and Rin than I felt to anyone at my old school."
n "และยังแปลกที่ว่าฉันสนิทกับเอมิกับรินยิ่งกว่าคนที่โรงเรียนเก่าด้วยซ้ำ"

# n "Somehow I get the feeling they'd at least visit me if I wound up in the hospital."
n "ไม่รู้ทำไมถึงรู้สึกได้ว่าถ้าฉันเข้าโรงพยาบาลแล้วอย่างไรสองคนนี้ก็ต้องมาเยี่ยม"

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

nvl hide dissolve

nvl clear

window show

# "I focus on the view from the roof, banishing such thoughts from my head."
"ฉันจดจ่ออยู่กับทิวทัศน์จากดาดฟ้านี้พลางปัดความคิดเหล่านั้นออกจากหัว"

# "There's a light breeze blowing, and the sun is shining high in the sky."
"สายลมโชย แสงแดดส่องจากฟ้า"

# "The sky itself is a deep blue, with hardly a cloud in it. It's gotten pleasantly warm, and as I sit down to wait for my friends, I close my eyes and enjoy the feeling of the sun seeping into my skin."
"ท้องฟ้าที่เป็นสีน้ำเงินเข้มนั้นแทบไม่มีหมู่เมฆ ช่วงนี้เริ่มอุ่นสบายขึ้นมาแล้ว พอนั่งลงรอเพื่อนของฉันมาฉันก็หลับตา\nกำซาบความรู้สึกถึงแสงแดดที่สาดส่องผิวฉัน"

$ renpy.music.set_volume(0.1, 2.0, channel="ambient")

window hide

scene black
with shuteye

with Pause(4.0)

window show

# "Voices intrude upon the edge of hearing."
"มีเสียงแว่วเข้าหูมา"

# emi "—seems to have fallen asleep on us, Rin."
emi "—ดูท่าจะหลับใส่เราแล้วละริน"

# rin "Maybe he's faking, to lull us into a false sense of security."
rin "อาจจะแกล้งหลับ หลอกให้เราตายใจ"

# emi "Why would he do that?"
emi "แล้วฮิซาโอะจะทำแบบนั้นไปทำไม"

# rin "No idea."
rin "ไม่รู้สิ"

# emi "Still, you make a good point."
emi "แต่ก็ถูกของเธอ"

# emi "We should kick him or something to make sure he's really asleep."
emi "ต้องเตะหรือทำอะไรสักอย่างให้แน่ใจว่าหลับจริง ๆ"

stop music fadeout 1.0

# hi "Huh? What?"
hi "ฮะ? อะไรนะ"

$ renpy.music.set_volume(0.5, 5.0, channel="ambient")

scene bg school_roof
show rin basic_absent at tworight
show emi excited_happy_close at twoleft
with openeye

play music music_ease fadein 3.0

# "Emi looms over me like only a short girl can, peering at me intently."
"เอมิยืนบังแดดฉันในแบบที่มีแต่คนตัวเตี้ยจะทำได้พลางจดจ้องมองฉัน"

show emi basic_closedgrin_close
with charachange

# emi "Oh, you're awake. I guess we don't have to kick you then."
emi "อ้าว ตื่นแล้ว งั้นก็คงไม่ต้องเตะแล้วละ"

show rin basic_deadpan
with charachange

# rin "Was it part of your master plan?"
rin "นายวางแผนไว้แล้วใช่มั้ย"

# hi "What are you talking about?"
hi "พูดอะไรของเธอ"

show emi basic_grin_close
with charachange

# "Emi shrugs, her twin tails bouncing with the motion."
"เอมิยักไหล่จนผมหางม้าเด้งตามไป"

show emi basic_closedhappy_close
with charachange

# emi "I'm not sure either."
emi "ฉันก็ไม่แน่ใจเหมือนกัน"

show emi sad_grin_close
with charachange

# emi "You must be pretty tired to fall asleep out here."
emi "มาหลับอยู่ตรงนี้คงเพลียน่าดู"

show emi basic_closedgrin_close
with charachange

# emi "Although it's pretty comfortable, I suppose."
emi "แต่บรรยากาศก็น่านอนดีเหมือนกัน"

show emi basic_closedgrin_close:
    yanchor 0.9
with ease
with vpunch

# "She plops down next to me and begins to eat."
"เอมิผลุบตัวลงนั่งแล้วเริ่มกิน"

show rin basic_absent
with charachange

show rin basic_absent:
    yanchor 0.77
with charamove

# "Rin sits opposite from the two of us, a move which only makes me more aware of the girl sitting next to me."
"รินนั่งอยู่ตรงข้ามกับเราสองคน ซึ่งยิ่งทำให้ฉันประหม่ากับคนข้าง ๆ เข้าไปอีก"

# "If I didn't know any better, I'd swear Rin did it on purpose."
"ถ้าฉันไม่ได้รู้จักรินจริง ๆ แล้วละก็คงคิดว่าจงใจนั่งตรงนั้นด้วยซ้ำ"

# "I concentrate on my food, trying to tune out the majority of the conversation that Rin and Emi are having."
"ฉันจดจ่ออยู่กับการกินอาหารพลางตัดเสียงบทสนทนาหลายอย่างที่รินกับเอมิคุยกัน"

# "Despite my best efforts, however, I still find myself glancing over at Emi whenever she speaks."
"แต่ถึงอย่างนั้นฉันก็ยังเหลือบมองไปทางเอมิทุกครั้งที่เธอพูดอยู่ดี"

show emi basic_grin_close
with charachange

# "I notice how she purses her lips when she's thinking about something, squinting slightly as if that would improve her thinking ability."
"ฉันเห็นว่าเวลาเอมิคิดอะไรแล้วเธอจะเม้มปากขมวดคิ้วเล็กน้อยราวกับว่าทำแล้วจะคิดออกง่ายขึ้น"

show rin basic_deadpan
with charachange

show emi basic_grin_close at Transform(function=tf_leftrock)
with None

show emi basic_closedhappy_close at Transform(function=tf_leftrock)
with charachange

# "Rin says something that makes Emi laugh, and I notice, perhaps for the first time, how she laughs with her whole body, rocking back and forth, head thrown back, almost like she's about to fall over."
"รินพูดอะไรสักอย่างจนทำให้เอมิหัวเราะ และฉันก็เห็น—น่าจะเพิ่งเห็นเป็นครั้งแรกเลย—ว่าเอมิหัวเราะแบบ\nตัวโยกตัวโยนแหงนหน้าขึ้นเหมือนจะหงายหลังล้มไป"

# "I probably look like a creep."
"สงสัยตอนนี้ฉันกลายเป็นคนน่าขยะแขยงไปแล้ว"

show emi basic_confused_close
with charachange

# "It's about this time that I realize Emi's looking at me. Her voice raised slightly, so she's probably just asked me a question."
"เป็นจังหวะนี้เองที่ฉันรู้ตัวว่าเอมิมองฉันอยู่ เธอขึ้นเสียงเล็กน้อย น่าจะเพิ่งถามอะไรไป"

# hi "Huh? Sorry, I kinda zoned out for a moment there."
hi "หือ ขอโทษที พอดีเมื่อกี้เหม่อ ๆ"

show rin basic_deadpannormal
show emi basic_annoyed_close
with charachange

# "Emi rolls her eyes, while a slight quirk of the eyebrow is the only sign that Rin's even paying attention."
"เอมิกลอกตา สิ่งเดียวที่บ่งบอกว่ารินสนใจอยู่คือคิ้วที่เลิกขึ้นเล็กน้อย"

# emi "I said, did you get a career survey in your class too?"
emi "ฉันถามว่าห้องนายมีแจกแบบสอบถามเรื่องเส้นทางอาชีพด้วยมั้ย"

show emi basic_grin_close
with charachange

# emi "You know, one of those “What do you want to do after high school?” things?"
emi "แบบ ที่ถามประมาณว่า “เรียนจบแล้วจะทำอะไรต่อ” น่ะ"

# hi "I don't… think so. Maybe we'll get one tomorrow."
hi "ไม่… น่านะ ห้องฉันอาจจะได้พรุ่งนี้มั้ง"

show emi excited_happy_close
with charachange

# emi "What are you going to put down?"
emi "นายจะเขียนว่าอะไร"

# "That's a really good question."
"ถามได้ดีมาก"

# "I guess I always figured I'd go to college after high school, but I've no idea what I'd do once I got there."
"เหมือนฉันจะกะไว้แล้วว่าเรียนจบแล้วคงต่อมหาวิทยาลัย แต่ก็ยังไม่รู้เลยว่าจะเข้าไปเรียนอะไร"

# "And with the heart attack and all, I'd really been concentrating on each day as it came rather than making long-term plans."
"แล้วยิ่งมีเรื่องหัวใจวายอะไรนี่อีก ฉันเลยได้แต่จดจ่ออยู่กับเรื่องในแต่ละวันไป ไม่ได้วางแผนระยะยาวอะไร"

# "I suppose I can safely start planning ahead, again."
"ตอนนี้น่าจะพอวางแผนอะไรได้แล้วละนะ"

# "I've always liked having at least a vague plan for my future, so it'll be nice to come up with one again."
"ปกติฉันชอบคิดแผนคร่าว ๆ สำหรับอนาคตไว้ตลอด เพราะงั้นกลับมาคิดอีกทีก็คงดีเหมือนกัน"

# "Of course, that doesn't change the fact that right now I've got absolutely…"
"แต่ก็แน่ละว่าตอนนี้ฉันน่ะยัง…"

# hi "…No clue."
hi "…ไม่รู้เลย"

# hi "I always kind of assumed I'd figure it out in college. That or just become a salaryman. That's pretty popular."
hi "ฉันคิดไว้ว่าพอเข้ามหา’ลัยแล้วเดี๋ยวก็คงเห็นเส้นทางเอง หรือไม่ก็ไปเป็นพนักงานเงินเดือน เห็นคนทำกันเยอะเลย"

# "But do I really want to? That's a tough question."
"แต่ถ้าถามว่าอยากจริง ๆ มั้ยอันนี้ก็ตอบยาก"

# "I guess I don't really want to do anything."
"ฉันก็คงอยากทำอะไรได้หมดน่ะแหละ"

show emi basic_closedhappy_close
with charachange

# emi "You don't sound very excited about that one, do you?"
emi "ฟังดูนายไม่ค่อยตื่นเต้นกับแผนนั้นเท่าไหร่เลยนะ"

show emi basic_closedhappy_close at Transform(function=tf_leftrock)
with None

# "She laughs as she says this, and I'm caught up in her laugh again."
"เอมิพูดพลางหัวเราะ และฉันก็สนใจกับการหัวเราะของเธออีกแล้ว"

# "It's so… girlish. High and giggly, like a… well, pardon the cliché - like a babbling brook."
"ช่าง… สมเป็นเด็กผู้หญิง เสียงแหลมสูงคิกคัก เหมือน… ขอประทานอภัยที่ใช้คำเฝือ ๆ เหมือนหยาดทิพย์ชโลมใจ"

# "It bubbles out of her, starting in her belly and working its way up her throat."
"ที่หลั่งออกมาจากปากเธอโดยต้นน้ำอยู่ในท้องแล้วไหลผ่านคอออกมา"

# "I can't help but laugh myself - it's infectious."
"ฉันอดหัวเราะตามไม่ได้ เป็นเสียงหัวเราะที่ชวนให้หัวเราะตาม"

# hi "Yeah, I guess I'm pretty unhappy with the salaryman idea."
hi "อืม ฉันก็คงไม่ได้อยากเป็นพนักงานเงินเดือนขนาดนั้นแหละ"

# hi "But to be honest, I haven't given much thought to the future recently."
hi "แต่เอาตรง ๆ ช่วงนี้ฉันก็ไม่ค่อยได้คิดถึงเรื่องอนาคตเท่าไหร่"

# hi "I suppose that, these days, I've been more concerned with living one day at a time."
hi "อาจจะเพราะเดี๋ยวนี้ฉันคิดแต่เรื่องใช้ชีวิตแบบวันต่อวันมากกว่ามั้ง"

show emi basic_grin_close
with charachange

# "Emi considers this for a moment and grins."
"เอมิคิดอยู่ครู่หนึ่งแล้วยกยิ้ม"

# emi "That's a pretty good idea, Hisao!"
emi "ก็เป็นความคิดที่ดีเหมือนกันนะฮิซาโอะ!"

show emi excited_proud_close
with charachange

# emi "I just wrote down, “Pirate.”"
emi "ส่วนฉันเขียนไปว่า “โจรสลัด”"

# "I'm momentarily stunned, then I start laughing."
"ฉันผงะไปแวบหนึ่ง แต่ก็หัวเราะออกมา"

# "I stop myself and manage to gasp out a question."
"ฉันหยุดหัวเราะแล้วเปิดปากถาม"

# hi "You're… you're not actually serious, are you?"
hi "เธอ… เธอพูดเล่น ใช่มั้ย"

show emi sad_annoyed_close
with charachange

# "Emi looks mock offended."
"เอมิแสร้งทำท่าไม่พอใจ"

# emi "Well I've got the legs for it already, so I just kind of figured…"
emi "นี่ไง ขาฉันก็เหมือนโจรสลัดแล้ว ก็เลยคิด ๆ อยู่…"

show rin basic_amused
with charachange

# "Even Rin seems amused by this."
"แม้แต่รินยังดูชอบใจ"

show emi basic_annoyed_close
with charachange

# emi "Just you wait, I'll be the terror of the high seas!"
emi "คอยดูเธอ ฉันจะเป็นจ้าวเหนือน่านน้ำให้ได้เลย!"

# emi "I'll show you all!"
emi "คอยดูเถิด!"

show emi basic_closedhappy_close
with charachange

# emi "I've even been working on my pirate voice!"
emi "เดี๋ยวนี้ฉันหัดทำเสียงแบบโจรสลัดด้วยนะ!"

show emi basic_closedhappy_close at offscreenleft
with ease

hide emi
with None

show emi basic_closedhappy at offscreenleft behind rin
with None

show emi basic_annoyed at left
with ease

# "She suddenly springs up and begins swaggering up and down the rooftop shouting orders."
"อยู่ ๆ เอมิก็เด้งตัวลุกขึ้นแล้วเดินอาด ๆ วางมาดไปตามดาดฟ้าตะโกนออกคำสั่ง"

show emi basic_annoyed at center
with ease

# emi "Yarr, me hearties, give 'em a broadside with the long guns!"
emi "เฮ้ย ไอ้เพื่อนยาก เอาปืนใหญ่ไปสั่งสอนเจ้าพวกนั้นหน่อย!"

show emi basic_annoyed at twoleft
with ease

# emi "We'll wear their guts for garters!"
emi "เราจะแล่เนื้อเถือหนังล่ามันให้สิ้นซาก"

show rin basic_deadpanamused
with charachange

# rin "Do you even know what that means?"
rin "รู้หรือเปล่าว่าที่พูดหมายความว่ายังไง"

show emi basic_confused
with charachange

# "Rin's unexpected interruption stops Emi in her tracks."
"เอมิชะงักเมื่ออยู่ ๆ รินก็ขัดขึ้นมาแบบไม่คาดหมาย"

show emi sad_shy
with charachange

# emi "Not really."
emi "ไม่ค่อย"

show emi basic_closedgrin
with charachange

# emi "But it's all in the delivery!"
emi "แต่สิ่งสำคัญคือการนำเสนอไง!"

play sound sfx_warningbell

show emi basic_hes
show rin basic_awayabsent
with charachange

# "The ringing of the bell prevents her from demonstrating her point further."
"เสียงระฆังดังปรามไม่ให้เอมิได้พิสูจน์ถึงสิ่งที่พูดให้เห็นอีก"

hide emi
with easeoutleft

# "Emi dashes off immediately, leaving Rin and myself alone on the roof."
"เอมิพุ่งตัวไปทันที ทิ้งให้ฉันกับรินอยู่ตามลำพังบนดาดฟ้า"

show rin basic_awayabsent:
    xpos 0.5
show bg school_roof at bgleft
with charamove

show rin basic_deadpancontemplation
with charachange

# "Rin stares at me intently for a few moments."
"รินจ้องฉันไม่วางตาอยู่ขณะหนึ่ง"

# hi "Is there… something wrong?"
hi "มี… อะไรหรือเปล่า"

show rin basic_lucid
with charachange

# "Rin considers this question closely for a moment."
"รินพินิจคำถามนี้พักหนึ่ง"

# "After a lengthy pause, she shakes her head."
"รินเว้นช่วงไปนานก่อนจะสั่นหัว"

show rin basic_deadpannormal
with charachange

# rin "Nope."
rin "ไม่"

# hi "Oh, um…"
hi "อ้อ เอ่อ…"

# extend " why the staring, then?"
extend " แล้วจ้องทำไม"

show rin basic_awayabsent
with charachange

# "Rin shakes her head again."
"รินสั่นหัวอีกรอบ"

# rin "Nope, I don't get it."
rin "ไม่ ไม่เข้าใจ"

# hi "Get what?"
hi "เข้าใจอะไร"

show rin basic_deadpan
with charachange

# rin "The staring thing. You two seem to, but I don't."
rin "ที่จ้องน่ะ เธอสองคนดูเข้าใจ แต่ฉันไม่เข้าใจ"

# "Great. She saw me staring. Now she probably thinks I'm a pervert or something."
"ยอดเยี่ยม รินเห็นที่ฉันจ้องสินะ แล้วเดี๋ยวก็คิดว่าฉันเป็นคนวิปริตหรืออะไรอีก"

# "Actually, probably not. This is Rin we're talking about, after all."
"ไม่สิ อาจจะไม่คิด คนอย่างรินคงไม่คิดแบบนั้นหรอก"

# "Still, I feel the need to defend myself."
"แต่ก็รู้สึกว่าต้องแก้ต่างอยู่"

# hi "I wasn't staring, I was just tired."
hi "เปล่าจ้อง ฉันแค่เพลีย"

show rin basic_deadpancontemplation
with charachange

# "Rin actually snorts at this, but she doesn't say anything."
"รินหัวเราะหึแต่ก็ไม่พูดอะไร"

# hi "No, really! I was just… distracted, is all."
hi "ไม่ จริง ๆ นะ! ฉันแค่… เหม่ออยู่"

show rin basic_lucid
with charachange

# rin "Mmm."
rin "อื้มม"

stop music fadeout 4.0

# "Eager to end this conversation, I head back down to class."
"ฉันกลับไปเข้าเรียนด้วยไม่อยากคุยต่อ"

stop ambient fadeout 2.0

scene bg school_scienceroom
show misha cross_grin at twoleft
show shizu behind_blank at tworight
with locationskip

# "I'm greeted by the twin specters of Shizune and Misha, looking like they mean business."
"ผู้สังเกตการณ์ที่ชื่อชิซูเนะกับมิช่าทักทายฉันด้วยท่าทีเหมือนมีธุระอะไรกับฉัน"

# "Well, Shizune looks like she means business, anyway."
"ไม่หรอก มีแค่ชิซูเนะที่เหมือนจะมีธุระ"

# "Misha just looks like she's about to start laughing at any minute."
"ส่วนมิช่าก็ทำท่าเหมือนจะหัวเราะเลยเสียเดี๋ยวนั้น"

play music music_shizune fadein 3.0

show misha perky_smile
with charachange

# mi "Up on the roof again, Hicchan?"
mi "ไปอยู่บนดาดฟ้าอีกแล้วเหรอฮิจัง"

show misha hips_frown
with charachange

# mi "You know that's dangerous, don't you~?"
mi "รู้ใช่มั้ยว่ามันอันตรายน่ะ~"

show shizu basic_angry
with charachange

shi "…"

show misha sign_smile
with charachange

# mi "That's right~!"
mi "จริงสิ~!"

show misha hips_smile
with charachange

# mi "The school cannot be held responsible for any injury that comes from being up there, you know!"
mi "ถ้าไปอยู่บนดาดฟ้าแล้วบาดเจ็บอะไรขึ้นมาทางโรงเรียนจะไม่รับผิดชอบนะรู้มั้ย!"

show misha cross_frown
with charachange

# mi "Furthermore, we could report you for breaking the rules~!"
mi "และยิ่งไปกว่านั้นเราก็เอาไปฟ้องได้ด้วยว่าพวกเธอทำผิดกฎ~"

show misha cross_frown_close
with characlose

# "Misha leans in and whispers conspiratorially."
"มิช่าโน้มตัวเข้ามาซุบซิบเหมือนมีแผนอะไร"

show misha sign_smile_close
show shizu behind_smile
with charachange

# mi "But we won't, Hicchan!"
mi "แต่เราไม่ฟ้องหรอกนะฮิจัง"

show misha hips_grin_close
with charachange

# mi "You three are too cute together~!"
mi "เธอสามคนอยู่ด้วยกันแล้วน่าร้าก~!"

show misha cross_laugh
with charadistant

# "She straightens up again, laughing at my sudden blush."
"มิช่ายืดหลังตรงอีกครั้งแล้วหัวเราะเมื่อเห็นฉันหน้าแดง"

# mi "Wahahaha~!"
mi "วะฮ่าฮ่าฮ่า~!"

show misha cross_grin
with charachange

# mi "You're too easy to tease, Hicchan~!"
mi "ฮิซาโอะนี่น่าแกล้งจัง~!"

# hi "Hey, come on."
hi "เฮ้ย ไม่เอาดิ"

# hi "I'm still new here, sort of."
hi "ฉันเป็นเด็กใหม่อยู่"

# hi "Isn't it mean to pick on the newcomer like this?"
hi "แกล้งเด็กใหม่แบบนี้มันไม่ดีนะ"

show misha hips_grin
with charachange

# mi "Nope~!"
mi "ไม่~!"

show misha sign_smile
with charachange

# mi "It's to help you get acclimated to your new surroundings!"
mi "นายจะได้ปรับตัวกับสภาพแวดล้อมใหม่ได้ง่ายขึ้นไง"

# hi "Ah, I see."
hi "อ้อ อย่างนี้นี่เอง"

# hi "Well…do you have to be so overzealous about it?"
hi "แล้ว… จำเป็นต้องทำด้วยความเริงร่าขนาดนี้ด้วยเหรอ"

show misha hips_grin
with charachange

# mi "Yep!"
mi "ช่าย!"

show misha hips_smile
with charachange

# mi "Ah! That aside, Hicchan, we were looking for you this morning, but you weren't in your room!"
mi "อ้อ! จะว่าไปฮิจัง เช้านี้เราไปหานายแต่นายไม่อยู่ห้อง!"

# hi "Of course I wasn't. I was out for my morning exercise, or here in class, bright and early."
hi "ก็ไม่อยู่น่ะสิ ต้องไปวิ่งรอบเช้านี่ แล้วแป๊บ ๆ ก็ต้องมาเข้าเรียนแต่เช้าตรู่อีก"

# hi "Unlike you."
hi "ไม่เหมือนเธอ"

show shizu basic_angry
show misha hips_frown
with charachange

# "Shizune looks peeved, and a beat later, so does Misha. Or she tries to, at any rate."
"ชิซูเนะดูไม่พอใจ อีกพักหนึ่งมิช่าก็ดูไม่พอใจ หรือไม่ก็แค่ทำท่าเหมือนไม่พอใจเฉย ๆ"

# mi "That was because of student council business! You should be grateful that we work so hard for you~!"
mi "เพราะเรามีธุระเรื่องสภานักเรียนต่างหาก! นายต้องขอบคุณพวกเรานะที่เราทำงานหนักขนาดนี้~!"

# hi "Oh, I am, I am. So what did you need me for?"
hi "เออ ขอบคุณ ๆ แล้วมีธุระอะไรกับฉันล่ะ"

# "Not another attempt to rope me in to do their dirty work, I hope."
"คงไม่ใช่ว่าจะลากฉันไปทำงานสกปรกอะไรอีกนะ หวังว่า"

show misha sign_smile
with charachange

# mi "We had to give you something~ but since you weren't around, we dropped it off in your room!"
mi "เรามีของจะให้~ แต่นายไม่อยู่เราเลยทิ้งไว้ให้ในห้อง!"

# hi "Something? Like what?"
hi "ของ? เช่นอะไร"

show misha hips_grin
with charachange

# mi "Oh, you'll find out when you get back, Hicchan~! Wahahaha~!"
mi "เดี๋ยวกลับไปดูก็รู้น่าฮิจัง~! วะฮ่าฮ่าฮ่า~!"

hide misha
hide shizu
with charaexit

# "Mutou entering the room ends our conversation, and we all head to our seats."
"ครูเข้ามาในห้องจนเราต้องหยุดคุยกันแล้วกลับไปนั่งที่"

stop music fadeout 10.0

# "It's only after I've settled down at my desk and the teacher's started talking about something or other that something odd strikes me."
"เมื่อมานั่งที่แล้วและครูเริ่มคุยเรื่องนั้นเรื่องนี้ฉันก็ถึงนึกได้ว่ามีอะไรแปลกไป"

# "What did Rin mean, “You two seem to?”"
"ที่รินบอกว่า “เธอสองคนดูเข้าใจ” นี่คือยังไง"

# "Was Emi staring at something too?"
"เอมิก็จ้องอะไรอยู่เหมือนกันเหรอ"

# "For a brief moment, I consider the possibility that Emi was staring at me the way I was staring at her."
"แวบหนึ่งฉันคิดว่าเอมิอาจจะจ้องฉันเหมือนกันกับที่ฉันจ้องเธอ"

# "Of course, that's ridiculous."
"ซึ่งแน่ละว่าเป็นไปไม่ได้"

# "Still, I can't deny that I wouldn't mind if it were true…"
"แต่ก็ปฏิเสธไม่ได้เหมือนกันว่าถ้าเป็นงั้นจริงฉันคงไม่ถือ…"

# "But it's best not to think of that. No need to get my hopes up."
"แต่อย่าไปคิดเลยจะดีกว่า อย่าไปหวังอะไรเลย"

# "Come to think of it, when did I start having hopes like that anyway?"
"จะว่าไปแล้ว ฉันมาหวังอะไรแบบนี้ตั้งแต่เมื่อไหร่"

# "I shake my head in an attempt to clear it, and focus on the lesson."
"ฉันสั่นหัวปัดความคิดนั้นออกไปแล้วตั้งใจเรียน"

scene bg school_dormhallway
with shorttimeskip

# "After class, I make my way to my room. Mutou really piled on the homework today."
"พอเลิกเรียนฉันก็กลับมาที่ห้อง วันนี้ครูสั่งการบ้านมาเป็นตั้งเลย"

play sound sfx_impact2

show kenji tsun at left
with vpunch

# "Before I can open my door, however, I am suddenly intercepted by Kenji, who has just exploded out of his own room in a flurry of papers."
"แต่ก่อนที่ทันจะได้เปิดประตูเคนจิก็เข้ามาขัดขวางเสียก่อน เขาพุ่งตัวออกจากห้องมาพร้อมกระดาษพรึ่บพรั่บ"

# ke "Hey, we need to talk."
ke "เฮ้ย เราต้องคุยกันหน่อย"

play music music_kenji fadein 1.0

# ke "These rooftop shenanigans of yours, man."
ke "ไอ้เรื่องดาดฟ้าอะไรของนายเนี่ย"

# ke "They've gotta stop."
ke "เลิกได้แล้วนะ"

# hi "What?"
hi "ฮะ?"

# ke "Your running around on the rooftop with the limbless wonders!"
ke "นายไปป้วนเปี้ยนอยู่บนดาดฟ้ากับสองหน่อไร้รยางค์นั่นน่ะ!"

# ke "They're women, man! You'll get yourself killed running around like that!"
ke "ผู้หญิงนะเว้ย! ขืนไปอยู่อย่างนั้นเดี๋ยวก็โดนฆ่าตายหรอก!"

# hi "I don't follow."
hi "ไม่เข้าใจ"

show kenji neutral
with charachange

# "Kenji sighs and adjusts his glasses, before what could be understood as an attempt at explaining himself patiently."
"เคนจิถอนหายใจแล้วดันแว่นก่อนจะพูดอะไรที่เหมือนกำลังแจงรายละเอียดให้ฟังอย่างใจเย็น"

# ke "Look, we're friends so I'm telling you this for your own good."
ke "เนี่ย ที่ฉันมาบอกนายก็เพราะเราเป็นเพื่อนกันหรอกนะ"

# ke "But if I were going to kill someone, I'd do it by throwing them off the roof and making it look like an accident."
ke "ถ้าฉันจะฆ่าใครสักคนฉันก็คงใช้วิธีการผลักให้ตกจากดาดฟ้าแล้วจัดฉากว่าเป็นอุบัติเหตุ"

show kenji tsun
with charachange

# ke "And if I've thought of it, you can be sure they've thought of it too."
ke "ซึ่งถ้าฉันคิดได้ แปลว่าพวกนั้นก็คิดได้เหมือนกัน"

# ke "They're crafty - almost as crafty as I am."
ke "พวกนั้นน่ะเจ้าเล่ห์แสนกลมากพอ ๆ กันกับฉันเลย"

# hi "I see."
hi "เข้าใจละ"

show kenji happy
with charachange

# ke "Good!"
ke "ดี!"

# ke "I'm glad we had this chat."
ke "ดีใจนะที่ได้คุยกัน"

show kenji neutral
with charachange

# ke "Loan me 500 yen."
ke "ขอยืม 500 เยนดิ"

# hi "…I'm sorry?"
hi "…อะไรนะ"

show kenji tsun
with charachange

# ke "I need to get a drink, man!"
ke "ฉันก็ต้องหาอะไรดื่มเหมือนกันนะพวก!"

# ke "I've been inside all day and the tap water's been compromised, as I'm sure you know."
ke "ฉันอยู่ในห้องทั้งวัน และนายก็คงรู้ว่าน้ำประปาใช้ดื่มไม่ได้"

# ke "So I need to stock up on something canned, got it? But to do that, I need 500 yen."
ke "เพราะงั้นฉันก็ต้องตุนอาหารกระป๋องไว้ เข้าใจมั้ย แต่จะทำแบบนั้นได้ฉันต้องมีเงิน 500 เยนก่อน"

show kenji neutral
with charachange

# ke "And since I've just saved your life with my timely advice, you can at least spare me 500 yen."
ke "และฉันก็เพิ่งให้คำแนะนำให้นายรอดชีวิตมาได้อย่างถูกจังหวะ เจียดเงินสัก 500 เยนคงไม่เป็นไรมั้ง"

# "You know, if it'll make him go away, 500 yen is a bargain."
"อืมนะ ถ้าต้องจ่าย 500 เยนเพื่อให้เคนจิไสหัวไปแล้วก็นับว่าคุ้ม"

stop music fadeout 6.0

show kenji happy
with charachange

show kenji happy:
    easeout 0.5 alpha 0.0 xanchor 0.2
with None

# "I hand the money over to Kenji, who nods in thanks and dashes off down the hallway, but not before he locks his door."
"ฉันยื่นเงินให้เคนจิ เขาพยักหน้าขอบคุณแล้วพุ่งตัวไปตามโถงทางเดินโดยล็อกประตูห้องตัวเองก่อน"

# "What an exhausting person. I'd better go, in case he changes his mind."
"อยู่ด้วยแล้วเหนื่อยชะมัด ไปดีกว่า เดี๋ยวเคนจิเปลี่ยนใจกลับมาแล้วจะยุ่ง"

scene bg school_dormhisao
with locationchange

# "Hm?"
"หืม"

# "As I close the door, my heel taps against something lying on the floor."
"พอปิดประตูส้นเท้าฉันก็แตะเข้ากับบางอย่างที่วางอยู่กับพื้น"

# "It's a brightly-colored rectangle of paper. Ah, this must be the “something” Misha mentioned before."
"เป็นกระดาษทรงสี่เหลี่ยมผืนผ้าสีสันสดใส อ้อ นี่สินะ “ของ” ที่มิช่าว่า"

# "Probably a student council leaflet she slid under the door."
"อาจจะเป็นใบปลิวจากสภานักเรียนที่เอามาสอดไว้ให้"

# "However, when I pick it up, I find that I couldn't have been more wrong."
"แต่พอหยิบขึ้นมาก็รู้ว่าคิดผิดไปไกลโข"

# "Someone actually wrote me an old-fashioned, hand-written paper letter."
"มีคนเขียนจดหมายด้วยมือแบบเชย ๆ ส่งมาให้ฉันจริง ๆ"

# "Who bothers doing something like that in this day and age, anyway? Yet, as unlikely as the prospect of receiving one sounds, this is definitely a letter I have in my hands."
"ยุคสมัยป่านนี้แล้วใครจะมานั่งเขียนจดหมายส่งหากันแบบนี้ แต่แม้จะฟังดูเป็นไปไม่ได้เพียงใด สิ่งที่อยู่ในมือฉันตอนนี้\nคือจดหมายแน่ ๆ"

# "I was planning on finishing my homework, getting some dinner, and going to bed in order to be ready for tomorrow morning's run."
"ฉันเตรียมจะทำการบ้านให้เสร็จ ไปหาข้าวเย็นกิน แล้วนอนเตรียมไปวิ่งพรุ่งนี้เช้า"

# "However, the letter has naturally caught my interest. I sit at my desk to examine it properly."
"ทว่าจดหมายที่อยู่ในมือนี้ก็สะดุดตาเข้า ฉันนั่งลงกับโต๊ะพินิจอย่างถี่ถ้วน"

scene ev hisao_letter_closed:
     xalign 0.5 yalign 0.5 zoom 1.1 subpixel True
     acdc_warp 10.0 zoom 1.0
with locationchange

play music music_rain fadein 5.0

# "It's the first piece of mail I've received here at Yamaku, so it'd feel special even if it wasn't something as rare as a handwritten letter."
"เป็นของอย่างแรกที่ฉันได้รับนับตั้งแต่ที่ฉันมาเข้าเรียนที่ยามากุ เพราะงั้นถึงต่อให้ไม่ใช่จดหมายเขียนมือก็จะเป็นอะไร\nที่รู้สึกว่าพิเศษอยู่ดี"

# "What causes me even more trepidation is the name of the sender, written neatly on the back of the envelope."
"สิ่งที่ทำให้ฉันสังหรณ์ใจขึ้นมายิ่งกว่านั้นคือชื่อของผู้ส่งที่เขียนไว้ด้วยลายมือเรียบร้อยอยู่หลังซอง"

# "“Iwanako.”"
"“อิวานาโกะ”"

# "I have no idea why she would write to me. I haven't been in contact with anyone from my old school since I transferred, and Iwanako is the last person I'd expect to want to write me a letter."
"ฉันไม่รู้ว่าเธอจะมีอะไรเขียนถึงฉัน ตั้งแต่ย้ายมาฉันก็ไม่ได้ติดต่อกับใครที่โรงเรียนเก่าแล้ว แล้วอิวานาโกะยิ่งไม่ใช่ใคร\nที่ฉันจะคาดฝันว่าจะเขียนจดหมายส่งมาเลย"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

# n "\n\n\n\n\nThe last time I saw Iwanako was terribly awkward; embarrassingly so. She came to my hospital room, peeled me an apple out of courtesy and then we practically sat in silence for half an hour."
n "\n\n\n\n\nครั้งสุดท้ายที่ได้เจอกันนั้นทั้งแสนอึดอัดและน่าอาย เธอมาเยี่ยมที่ห้องฉันแล้วปอกแอปเปิลให้เป็นมารยาท แล้วก็อยู่กัน\nเงียบ ๆ ได้ครึ่งชั่วโมง"

# n "She said “goodbye” and didn't look me in the eye when she closed the door."
n "เธอบอกว่า “ลาก่อนนะ” แล้วปิดประตูไปไม่แม้แต่จะมองตากัน"

# n "It might've been a natural end to the series of visits that were probably pretty painful for both of us."
n "การเยี่ยมไข้คงจะทำเราทั้งคู่ค่อนข้างทรมาน อาจจะเป็นธรรมดาที่จบลงไปอย่างนั้น"

# n "Every time she visited me in the hospital I wanted to talk to her, but something stopped me every time."
n "ทุกครั้งที่เธอมาเยี่ยมฉันนึกอยากคุยกับเธอตลอด แต่บางอย่างก็ยั้งปากฉันไว้"

# n "Every time that I didn't speak made the next time even harder."
n "แล้วยิ่งไม่ได้พูดครั้งหนึ่ง ครั้งถัดไปก็ยิ่งพูดยากขึ้นไปอีก"

nvl clear

# n "\n\n\n\nShe looked so guilty that I didn't want to say anything that might upset her, and I never could figure out the right words to say."
n "\n\n\n\nเธอดูรู้สึกผิดเสียจนฉันไม่อยากพูดอะไรที่ไปทำให้เธอเครียดอีก แล้วฉันก็ไม่เคยเฟ้นหาอะไรดี ๆ มาพูดได้เลย"

# n "I think Iwanako blamed herself for my heart attack. That's ridiculous, of course, but knowing it and believing it are two very different things."
n "ฉันคิดว่าอิวานาโกะคงโทษตัวเองที่ฉันหัวใจวาย ซึ่งแน่ละว่าไร้สาระ แต่สมองกับหัวใจนั้นทำงานแยกส่วนกัน"

# n "I told her that it wasn't her fault, she nodded and I really think she understood that if it hadn't been that, then sooner or later something else would've made my heart give out."
n "ฉันบอกเธอไปว่าไม่ใช่ความผิดเธอเลย เธอพยักหน้า ฉันคิดว่าเธอคงเข้าใจแล้วว่าถ้าไม่เกิดเรื่องเมื่อวันนั้นขึ้นมา\nไม่ช้าก็นานสักวันหัวใจฉันก็จะอาการกำเริบอยู่ดี"

# n "Yet she looked so hopelessly sad every time she opened that door and entered my room."
n "ทว่าเธอดูเศร้าโศกทุกครั้งที่เปิดประตูห้องเข้ามาหาฉัน"

# n "So I never managed to say the things I wanted to say. In the end, that might've hurt her even more."
n "ฉันไม่เคยพูดอะไรที่อยากจะพูดได้เลย ซึ่งท้ายที่สุดพอทำอย่างนั้นแล้วเธอคงจะเจ็บหนักกว่าเดิมด้วยซ้ำ"

$ renpy.music.set_volume(1.0, 2.0, channel="music")

nvl hide dissolve
nvl clear

scene ev hisao_letter_open
with locationchange

window show

# "Carefully, I open the envelope and draw out the folded letter from within."
"ฉันแกะซองจดหมายอย่างทะนุถนอมแล้วเปิดจดหมายที่อยู่ข้างในออกอ่าน"

window hide

# $ written_note("Dear Hisao,\n\nHow are you? I hope you are well and happy at your new school. Everyone here misses you. Almost all of our second-year class got put together in class 3-1 for the final year, so we are pretty comfortable right from the beginning of the year. I'm sure you would've been assigned to this class as well.")
$ written_note("ถึง ฮิซาโอะ\n\nเป็นยังไงบ้าง หวังว่านายจะสบายดีมีความสุขกับ\nโรงเรียนใหม่นะ คนที่นี่คิดถึงนายกัน พวก\nนักเรียนม. 5 พอได้ขึ้นชั้นมาอยู่ม. 6 ก็ได้ย้ายมาอยู่\nห้อง 3-1 กันเกือบหมด ก็เลยอยู่กันอย่างอบอุ่น\nแต่ต้นปีการศึกษาเลย ถ้านายยังอยู่ก็คงได้มาเรียน\nห้องเดียวกันเหมือนกัน")
 
# $ written_note("The mood among the third-years seems to be very anxious about the final exams, even though they are so far away. The teachers are badgering us about it all the time - even old Mr. Tachibana who is, by the way, our homeroom teacher this year. Would you believe it? I was sure that he'd retire after our second year, but here he is, nagging everyone about studying for exams.\n")
$ written_note("นักเรียนม. 6 ดูจะเครียดเรื่องสอบปลายภาคกัน\nถึงจะยังอีกนานก็เถอะ คุณครูก็เอาแต่ตามย้ำอยู่\nนั่นแหละ ขนาดครูทาจิบานะยังเป็นไปกับเขาเลย\nแล้วก็เนี่ย เชื่อมั้ยว่าปีนี้แกได้เป็นครูประจำชั้นห้อง\nของเราด้วยนะ ฉันก็กะไว้แล้วแท้ ๆ ว่ายังไงพอ\nขึ้นชั้นมา แกก็คงเกษียณไปแล้ว แต่ก็ไม่\nมายืนจิกหัวให้อ่านหนังสือสอบอยู่เนี่ย\n")

# $ written_note("I think things like that are the main reason why the mood among the third-years is so nervous. I must admit that I'm somehow losing confidence in myself as well, even though I've always fared reasonably well in exams.\n\n\n\n\n")
$ written_note("ฉันว่าเพราะอย่างนั้นแหละพวกม. 6 เลยร้อนรน\nกัน ฉันก็ต้องยอมรับเหมือนกันว่าฉันเองก็ชักจะ\nไม่มั่นใจขึ้นมาแล้ว ถึงปกติจะสอบได้คะแนนเยอะ\nพอตัวตลอดก็เถอะ\n\n\n\n\n")

# $ written_note("It's so weird to think we are already seniors, isn't it? Time has really flown past. I wonder where it went. The new first-years seem so young and somehow really innocent. I keep wondering if I was like them in my first year. I've been feeling nostalgic like this for the whole first trimester.\n\n\n")
$ written_note("แปลกเนอะ รู้ตัวอีกทีก็ม. 6 แล้ว เวลาผ่านไปไว\nจริง ๆ ผ่านไปไหนกันนะ นักเรียนม. 4 น่ะดูทั้ง\nยังเด็กแล้วก็ใสซื่อดี ตลอดเทอมแรกนี้ฉันเอาแต่\nย้อนคิดตลอดเลยแหละว่าสมัยอยู่ม. 4 ฉันก็เป็น\nอย่างนั้นด้วยหรือเปล่า\n\n\n")

# $ written_note("There are other things I want to say. I'm writing to you because I felt that there are things I should've said after the incident back in winter. I really regret that I wasn't able to say them in person, and I have no excuse for it…\n\n\n\n\n")
$ written_note("ยังมีอย่างอื่นที่ฉันอยากพูดถึงอีก ฉันเขียนจดหมาย\nส่งมาหานายเพราะรู้สึกเหมือนพอเกิดเรื่องนั้นแล้ว\nฉันคงต้องพูดอะไรหน่อย ฉันเสียใจจริง ๆ ที่ฉันมา\nพูดกับนายต่อหน้าตรง ๆ ไม่ได้ และฉันก็ไม่มี\nข้อแก้ตัวอะไรทั้งนั้น…\n\n\n\n\n")

window show

# "Yeah, I think I have had quite enough of this."
"อืม ไม่อ่านต่อละ"

scene bg school_dormhisao
with locationchange

# "I crumple up the sheet of paper and toss it across the room. My aim is off, so the letter rolls under my nightstand instead of going into my wastebasket."
"ฉันขยำกระดาษแผ่นนั้นแล้วปาไปอีกฟากของห้อง ฉันเล็งพลาดจนจดหมายกลิ้งไปอยู่ใต้โต๊ะหัวเตียงแทนที่จะลง\nถังขยะ"

# "That was an apology for abandoning me. Except I don't know that I really need it any more, at this point."
"ส่งมาขอโทษที่ทิ้งกันไปนี่เอง ซึ่งตอนนี้ฉันก็ไม่รู้ว่าตัวเองยังต้องการคำขอโทษอยู่หรือเปล่า"

# "The hospital seems like a lifetime ago, and here, now, I've got other things on my mind."
"ชีวิตในโรงพยาบาลนานเหมือนเป็นชาติที่แล้ว แถมตอนนี้ในหัวฉันก็มีเรื่องอื่นแล้วด้วย"

stop music fadeout 8.0

# "Emi, for starters."
"เอมิ เป็นต้น"

# "It wasn't great to be abandoned during my stay, but it's not something I'm worried about any more."
"ถูกทิ้งตอนอยู่โรงพยาบาลชวนให้รู้สึกแย่ก็จริง แต่ตอนนี้ฉันไม่ได้คิดมากแล้ว"

# "In fact, I hadn't even thought about the hospital in what feels like forever until this letter came in. It's almost annoying to have received it."
"ที่จริง ฉันไม่ได้คิดถึงเรื่องที่โรงพยาบาลมานานมากแล้วจนมาเจอจดหมายฉบับนี้แหละ พอได้รับแล้วก็รำคาญ"

# "I've got exams to study for, myself. I have no time for the past."
"ฉันก็ต้องอ่านหนังสือสอบด้วย ไม่มีเวลามาจมกับอดีตแล้ว"

# "Now, about that homework…"
"ไหนซิ การบ้าน…"

scene black
with dissolve


########################################################
label th_E11a:

scene black
with None

# hi "So what's the plan for today anyway?"
hi "แล้ววันนี้จะทำอะไรกัน"

play music music_daily fadein 1.0

scene bg school_girlsdormhall
with dissolve

# "I'm waiting patiently in the hallway of the girls' dormitory just outside of Emi and Rin's rooms."
"ฉันรออย่างใจเย็นอยู่ที่โถงทางเดินหน้าห้องเอมิกับห้องริน"

# "Emi is apparently helping Rin with getting dressed."
"เหมือนเอมิจะช่วยรินแต่งตัวอยู่"

# "I suppose that makes perfect sense, as I've no idea how Rin would get dressed otherwise."
"ซึ่งก็คงสมเหตุสมผลดีแล้ว ไม่งั้นฉันก็นึกไม่ออกเหมือนกันว่ารินจะแต่งตัวได้ยังไง"

# emi "Picnic!"
emi "ปิกนิก!"

# hi "Picnic?"
hi "ปิกนิก?"

# emi "That's what I said!"
emi "ใช่แล้วละ"

# hi "Sounds pretty exciting."
hi "ฟังดูน่าตื่นเต้นดี"

# emi "I know, right?"
emi "ใช่มั้ยล่ะ"

# "Rin chooses this moment to make an observation."
"รินอาศัยจังหวะนี้แทรกบทพูด"

# rin "The sky seems threatening today."
rin "วันนี้ฟ้าดูไม่ดีเลยนะ"

# "Actually, I noticed that, too, on my way over. Despite the sunshine of the early morning, the afternoon seems to have taken a turn for the gloomy."
"จริง ๆ ตอนที่เดินมาฉันก็เห็นเหมือนอย่างรินว่า ตอนเช้าแดดออกก็จริง แต่บ่าย ๆ มาฟ้าก็เริ่มครึ้มแล้ว"

# "There's a heaviness to the air as well that usually heralds a rainstorm."
"อากาศก็อบอ้าวเหมือนพายุฝนจะมาด้วย"

# "I wonder if I should have brought my umbrella…"
"หรือจะพกร่มไปด้วยดี…"

# hi "She's got a point."
hi "รินพูดถูก"

# hi "Emi, you sure that you still want to risk getting caught in the rain?"
hi "เอมิ ฝนจะตกอย่างนี้แล้วแน่ใจเหรอว่ายังจะไปน่ะ"

# "I don't even know why I bothered asking."
"ไม่รู้จะถามทำไม"

show emi basic_shock:
    center
    xpos 0.9
    easein 0.5 xpos 0.7
with charaenter

# "Emi pops out of Rin's room into the hallway looking shocked that I'd even suggest canceling our plans."
"เอมิโผล่ออกมาจากห้องรินมาที่โถงทางเดินพร้อมสีหน้าตกใจที่ฉันกล้าเสนอให้ยกเลิกแผนนี้"

# emi "Of course!"
emi "แหงสิ!"

show emi basic_annoyed
with charachange

# emi "What, the threat of rain's supposed to stop me?"
emi "แล้วไง ฝนจะตกแล้วฉันต้องกลัวเหรอ"

# "I can't help but grin at her belligerent response. It's almost like she's daring the rain to come."
"ฉันอดยิ้มให้กับคำตอบสุดดื้อรั้นนั้นไม่ได้ เหมือนท้าให้ฝนตกเลย"

# "If Mother Nature were walking down the street, I think Emi would probably start a fight with her."
"ถ้าพระพิรุณมาเดินแบบตัวเป็น ๆ เอมิคงหาเรื่องต่อยไปแล้ว"

# "Or at the least challenge her to a race."
"หรือไม่ก็ท้าให้มาแข่งวิ่งกัน"

# "In fact, Emi seems almost aggressively cheerful today."
"จริง ๆ วันนี้เอมิดูจะคึกคักเป็นพิเศษเลย"

show rin basic_absent:
    center
    xpos 0.9 alpha 0.0
    ease 1.0 xpos 0.7 alpha 1.0
show emi basic_annoyed at twoleft
show bg school_girlsdormhall at bgleft
with charamove

# "Rin wanders out into the hallway, looking her usual self."
"รินเดินออกมาที่โถงทางเดินด้วยท่าทีประจำ"

# hi "Well then, are we all ready to go?"
hi "โอเค งั้นพร้อมกันแล้วนะ"

show emi basic_closedhappy
with charachange

# emi "I'm ready!"
emi "พร้อมแล้ว!"

show rin basic_deadpannormal:
    tworight alpha 1.0
with charachange

# "Rin nods and says a single word."
"รินพยักหน้าแล้วพูดหนึ่งคำ"

show rin basic_deadpan
with charachange

# rin "Basket."
rin "ตะกร้า"

# hi "Beg pardon?"
hi "อะไรนะ"

show rin basic_deadpannormal
with charachange

# rin "The basket. In Emi's room. You should carry it."
rin "ตะกร้า ในห้องเอมิ นายถือไปสิ"

show emi basic_hes
with charachange

# "Emi claps a hand to her mouth, embarrassed."
"เอมิยกมือขึ้นมาตบปากด้วยความอาย"

show emi basic_closedsweat
with charachange

# emi "Omigosh! I almost forgot all about it! Nice save, Rin!"
emi "ตายจริง! เกือบลืมไปแล้วนะเนี่ย! ขอบคุณที่เตือนนะริน!"

show emi basic_closedsweat at offscreenleft
with ease

with Pause(0.3)

show emi basic_closedgrin at twoleft
with ease

# "Emi darts into her room and emerges with what looks like a very well-stocked picnic basket."
"เอมิพุ่งตัวไปในห้องแล้วกลับออกมาพร้อมตะกร้าที่ดูมีของกินครบครัน"

with vpunch

# "As she hands it over to me, I note that it feels heavy enough to be one, too. Good Lord, how much food did she pack?"
"เอมิยื่นตะกร้าให้ฉัน หนัก ๆ ผิดจากลักษณะตะกร้าแฮะ ให้ตายเถอะ นี่ยัดของกินไปเท่าไหร่เนี่ย"

# "…More to the point, where'd she get the money for all of this?"
"…แล้วที่สำคัญ ไปเอาเงินที่ไหนมาซื้อ"

# hi "So, are we set to head out?"
hi "โอเค พร้อมออกละนะ"

show emi basic_grin
with charachange

# emi "Yep!"
emi "อื้ม!"

show rin basic_awayabsent
with charachange

# "Rin gives another nod, and we head out of the dormitory."
"รินพยักหน้าอีกรอบ เราเดินออกมาจากหอ"

scene bg school_courtyard_rn
with locationskip

# "I can't help but frown when I notice how gray the sky's gotten in the ten minutes I was inside."
"ฉันสะดุดตาเข้ากับท้องฟ้าที่สีมืดครึ้มขึ้นกว่าเดิมนับจากตอนก่อนที่ฉันจะเข้าไปอยู่ในอาคารซึ่งผ่านมาราวสิบนาที"

# "Still, Emi does not seem concerned by such petty concerns as the color of the sky. She's positively skipping as we walk."
"แต่เอมิก็ดูจะไม่ยี่หระอะไรกับเรื่องเล็ก ๆ น้อย ๆ อย่างสีของท้องฟ้าตอนนี้เลย เธอเดินไปแบบโดด ๆ ด้วยซ้ำ"

# "Which reminds me…"
"ซึ่งจะว่าไปแล้ว…"

# hi "Where are we going?"
hi "เราจะไปไหนกันนะ"

# "This brings Emi up short and she shoots me an embarrassed look."
"เอมิชะงักกึกแล้วหันมามองฉันอาย ๆ"

show emi sad_shy_rn at center
with charaenter

# emi "You know, I hadn't really thought of that."
emi "ก็นะ ฉันยังไม่ได้คิดไว้เลย"

# emi "What do you think, Hisao?"
emi "ฮิซาโอะว่าไงล่ะ"

# "Well, there's the spot where we ate during the festival, but it might be nice to leave the campus for a while. However, I'm not sure if there's any good places to do that in town."
"ก็นะ ที่นึกออกก็ที่ที่ไปนั่งกินด้วยกันตอนวันงานเทศกาล แต่ออกจากโรงเรียนไปสักพักก็ดีเหมือนกัน ทว่าก็ไม่รู้ว่า\nในเมืองมีที่ดี ๆ ให้ไปปิกนิกหรือเปล่า"

# "Just as I'm about to open my mouth, Rin unexpectedly interjects with a suggestion."
"จังหวะที่กำลังจะเปิดปากนั้นรินก็แทรกเสนอขึ้นมาโดยไม่คาดฝัน"

show emi sad_shy_rn at twoleft
show bg school_courtyard_rn at bgleft
with charamove

show rin basic_deadpan_rn at tworight
with charaenter

# rin "There's a park in town near the art shop."
rin "ใกล้ ๆ ร้านขายอุปกรณ์ศิลปะมีสวนสาธารณะอยู่"

show emi basic_closedhappy_rn
with charachange

# emi "Great idea, Rin! I totally forgot all about that place!"
emi "ความคิดเยี่ยมนี่ริน! ฉันลืมเสียสนิทเลย!"

# "Crisis averted."
"พ้นภัยแล้ว"

# hi "Do you know how to get there, Rin?"
hi "เธอรู้ทางไปมั้ยริน"

show rin basic_deadpannormal_rn
with charachange

# "Rin shrugs."
"รินยักไหล่"

show rin basic_awayabsent_rn
with charachange

# rin "It's pretty likely."
rin "ก็เป็นไปได้"

show emi excited_amused_rn
with charachange

# emi "Good enough for me!"
emi "แค่นั้นก็พอแล้ว!"

# "I would prefer knowing for sure… but, what the hell."
"ถ้ารู้ทางไปแน่ ๆ เลยน่าจะดีกว่านะ… แต่อะไรเนี่ย"

# hi "Lead on, Rin."
hi "นำไปเลยริน"

scene bg school_gate_rn
with locationchange

# "The three of us quickly make our way off campus and take the road down into town."
"เราสามคนรีบเดินออกมาจากโรงเรียนแล้วเดินไปตามถนนเข้าเมือง"

scene bg school_road_rn
with locationchange

# "This basket's a bit heavy. I hope that the park is close by."
"ตะกร้าก็หนัก ๆ เหมือนกัน หวังว่าสวนสาธารณะนั้นจะอยู่ไม่ไกลนะ"

scene bg suburb_roadcenter_rn
with locationchange

# "We pass the art supply store, Rin slowing her pace slightly as we go by."
"เราเดินผ่านร้านขายอุปกรณ์ศิลปะ รินผ่อนฝีเท้าลงพอเดินผ่าน"

# "Emi notices Rin's change of pace and stops."
"เอมิเห็นว่ารินเดินช้าลงจึงหยุด"

show emi basic_grin_rn at twoleft
show rin relaxed_nonchalant_rn at tworight
with charaenter

# emi "You wanna go in, Rin?"
emi "อยากแวะเหรอริน"

show rin basic_awayabsent_rn
with charachange

# "Rin shrugs."
"รินยักไหล่"

show rin basic_deadpan_rn
with charachange

# rin "Nothing I need."
rin "ไม่มีของที่ต้องใช้"

show emi excited_proud_rn
with charachange

# emi "Are you suuure?"
emi "แน่ใจน้าาาาา"

show rin basic_delight_rn
with charachange

show rin basic_deadpandelight_rn
with charachange

# "There's the slightest flutter of a smile on Rin's face, quickly replaced with her usual expression."
"รินยิ้มเขิน ๆ อยู่แวบหนึ่งก่อนรอยยิ้มนั้นจะถูกแทนที่ด้วยสีหน้าตามปกติ"

show rin basic_deadpan_rn
with charachange

# rin "Life's uncertain, but on this at least I am pretty sure."
rin "ชีวิตไม่แน่นอน แต่อย่างน้อยฉันก็มั่นใจกับเรื่องนี้"

show rin basic_deadpanamused_rn
with charachange

# rin "Nice of you to offer."
rin "ขอบคุณที่เสนอ"

show emi basic_closedhappy_rn
with charachange

# emi "Well it's not like I'm the one carrying the basket."
emi "ก็ฉันไม่ได้เป็นคนถือตะกร้านี่นา"

show emi basic_grin_rn
with charachange

# emi "But I'll bet Hisao wouldn't have minded anyway, right?"
emi "แต่ยังไงฮิซาโอะก็คงไม่ว่าใช่มั้ย"

# hi "Oh, of course not. This is hardly a heavy load."
hi "โอ๊ย ไม่ว่าเลย ตะกร้าเบามาก"

# "I flex for emphasis."
"ฉันเบ่งกล้ามเน้นย้ำ"

show emi excited_laugh_rn
with charachange

# "Emi stifles a snort of laughter by pointing to the park at which we've suddenly arrived."
"เอมิกลั้นขำด้วยการชี้ไปที่สวนสาธารณะที่อยู่ ๆ พวกเราก็มาถึง"

$ renpy.music.set_volume(0.02, 0.0, channel="ambient")
play ambient sfx_rain fadein 15.0

scene bg suburb_park_rn at bgright
with locationchange

# emi "Oh, I remember this place!"
emi "อ้อ ฉันจำได้!"

show emi basic_closedhappy_rn
with charachange

# emi "I ran into you here that one time, didn't I, Rin?"
emi "ที่นี่ที่ตอนนั้นฉันมาเจอกับเธอใช่มั้ยริน"

show emi basic_closedhappy_rn at twoleft
show bg suburb_park_rn
with charamove

show rin basic_deadpannormal_rn at tworight
with charaenter

# "Rin's eyebrow raises slightly."
"รินเลิกคิ้วขึ้นเล็กน้อย"

show rin basic_deadpan_rn
with charachange

# rin "Maybe."
rin "มั้งนะ"

show rin relaxed_boredom_rn
with charachange

# rin "I'm unwilling to say for certain one way or the other."
rin "ฉันไม่อยากยืนยันว่าใช่หรือไม่"

show rin relaxed_nonchalant_rn
with charachange

# rin "Memory's a tricky thing, you know."
rin "ความจำคนเราน่ะมันหลอกเราได้นะ"

# "Well I'll be. We made it in one piece after all."
"อ้าว มาถึงกันโดยสวัสดิภาพจนได้"

# "The sun's still nowhere to be seen, but neither Emi nor Rin seem to mind."
"ยังไม่เห็นพระอาทิตย์ แต่เอมิกับรินก็เหมือนจะไม่สนใจอะไร"

scene ev picnic_normal:
    yalign 1.0 subpixel True
    easein 8.0 yalign 0.0
with whiteout

#show emi basic_grin_rn:
#    ypos 1.15
#show rin basic_absent_rn:
#    ypos 1.2
#with dissolvecharamove

# "We find a spot to sit on the grass and I set the basket down gratefully."
"เราหาที่นั่งบนพื้นหญ้ากัน ฉันค่อย ๆ วางตะกร้าลง"

# "There's a surprising amount of food prepared. Maybe we were supposed to be joined by some of Emi's teammates or something?"
"มีของกินเตรียมไว้เยอะเกินคาด หรือจริง ๆ แล้วจะมีเพื่อนร่วมทีมเอมิมาร่วมวงด้วยหรือเปล่า"

#show emi excited_laugh_rn
#with charachange

# emi "I'm starving! Dig in!"
emi "หิวแล้ว! กินกันเลยดีกว่า!"

# "She attacks the food as if she's had nothing to eat for years."
"เอมิจู่โจมอาหารเหมือนไม่ได้กินอะไรมาหลายปีดีดักแล้ว"

stop music fadeout 2.0

play sound sfx_thunder

show ev picnic_rain:
    yalign 0.0
with charachange

#show emi excited_circle_rn
#show rin basic_deadpanupset_rn
#with charachange

$ renpy.music.set_volume(0.2, 0.5, channel="ambient")

show rain light
with dissolve

# "I'm just reaching for the food myself when I feel the first drop of rain land on the back of my hand."
"เมื่อเอื้อมไปจะหยิบของกินให้ตัวเองบ้างก็เหมือนมีหยดน้ำฝนตกใส่หลังมือ"

# hi "Uh oh."
hi "ชะอ้าว"

# hi "Looks like the weather's not going to cooperate with us after all."
hi "ดูท่าว่าฟ้าฝนจะไม่ให้ความร่วมมือกับเราเสียแล้ว"

hide ev
show bg suburb_park_rn behind rain
show emi sad_grit_rn behind rain:
    twoleft
    ypos 1.15
show rin basic_absent_rn behind rain:
    tworight
    ypos 1.2
with flash

# "Emi glares at the sky as if that alone will hold back the rain."
"เอมิจ้องท้องฟ้าเหมือนว่าจ้องแล้วจะห้ามฝนได้"

# "I very nearly believe she can do it. It's one heck of a glare."
"ฉันก็เกือบจะเชื่อแล้วว่าห้ามได้จริงเพราะจ้องหนักมาก"

show emi basic_annoyed_rn
with charachange

# emi "It had better cooperate."
emi "ต้องให้ร่วมมือสิ"

show emi sad_angry_rn
with charachange

# emi "You hear me sky? You stop that raining right this instant!"
emi "ได้ยินมั้ยท้องฟ้า เลิกปล่อยฝนเดี๋ยวนี้นะ!"

# "The sky doesn't seem inclined to listen to her, despite the commanding tone she's taken with it."
"ดูท่าว่าท้องฟ้าจะไม่อยากฟังเอมิเท่าไหร่ แม้น้ำเสียงของเธอนั้นจะขึงขังมาก"

$ renpy.music.set_volume(0.5, 4.0, channel="ambient")

show rain medium
with dissolve

# "Instead, the rain seems to increase. Rin wrinkles her nose in distaste at this turn of events."
"ฝนกลับตกหนักขึ้นแทน รินย่นจมูกเมื่อเหตุการณ์ย่ำแย่ลงเช่นนี้"

show rin basic_deadpan_rn
with charachange

# rin "Regrettable."
rin "น่าเสียใจ"

show emi basic_confused_rn
with charachange

# emi "What do you mean?"
emi "หมายความว่าไง"

show rin basic_deadpannormal_rn
with charachange

# "Rin shrugs."
"รินยักไหล่"

show rin relaxed_nonchalant_rn
with charachange

# rin "I could paint this if I weren't out here. Shame to miss it, is all."
rin "ถ้าไม่ได้อยู่ตรงนี้ฉันคงวาดภาพตอนนี้ได้ แค่เสียดายที่ไม่ได้วาด"

# "She doesn't seem angry or annoyed about it, just a little disappointed."
"รินไม่ได้ดูโกรธหรือหงุดหงิด แค่ผิดหวังเล็กน้อย"

show emi basic_closedhappy_rn
with charachange

# "Emi laughs in response to Rin's comment."
"เอมิหัวเราะที่รินพูดแบบนั้น"

show emi basic_grin_rn
with charachange

# emi "Guess we should have stopped in that art supply store after all, huh?"
emi "เมื่อกี้ถ้าแวะที่ร้านขายอุปกรณ์ศิลปะนั้นคงดีเนอะ"

$ renpy.music.set_volume(1.0, 6.0, channel="ambient")

show rain normal
with dissolve

# "The rain increases a little more, offended that we haven't fled yet."
"ฝนตกหนักขึ้นอีกเล็กน้อยเหมือนไม่พอใจที่เรายังไม่หนีกันสักที"

# "Despite the warm temperatures we've been enjoying, the rain is rather cold. I wish I'd brought my umbrella."
"ถึงอากาศจะอบอุ่น แต่น้ำฝนนั้นเย็นพอตัว รู้งี้พกร่มมาด้วยดีกว่า"

# hi "Hey, we should probably head inside to keep dry."
hi "นี่ ไปหาที่หลบฝนไม่ให้ตัวเปียกกันก่อนเถอะ"

show emi basic_confused_rn
show rin basic_absent_rn
with charachange

# emi "We're already pretty wet, Hisao."
emi "ตอนนี้เราก็ตัวเปียกกันแล้วนะฮิซาโอะ"

# hi "Yeah, but we can dry off this way and maybe wait out the storm. You don't want to catch a cold or anything, do you?"
hi "ก็ใช่ แต่หลบฝนแล้วจะได้อยู่ให้ตัวแห้งรอพายุหยุดก่อนไง เธอคงไม่อยากเป็นหวัดหรอกนะ"

show emi basic_annoyed_rn
with charachange

# "Emi considers this for a moment. I can tell that part of her wants to stay out in the rain just to spite the weather."
"เอมิครุ่นคิดอยู่ครู่หนึ่ง ฉันดูออกว่าใจหนึ่งเอมิก็อยากตากฝนอยู่อย่างนี้เป็นการประท้วงสภาพอากาศ"

# "Unfortunately for her, the weather hardly cares about what we do."
"ซึ่งโชคไม่ดีที่ฟ้าฝนไม่ได้สนใจหรอกว่าเราจะทำอะไร"

show emi basic_closedgrin_rn
with charachange

# emi "I suppose you're right."
emi "ก็คงถูกของนาย"

show emi sad_grin_rn
with charachange

# emi "Where could we go?"
emi "ไปไหนกันดีล่ะ"

# "I don't have an answer for her. The area's still pretty new to me."
"ฉันไม่มีคำตอบเพราะยังไม่คุ้นกับพื้นที่"

# "Though I guess I'm slowly getting used to the school itself, the surrounding town remains a mystery."
"ถึงฉันจะเริ่มชินกับโรงเรียนขึ้นมาแล้ว แต่เมืองที่อยู่โดยรอบยังคงเป็นปริศนาสำหรับฉัน"

# "All I know is the art supply store, and that's only because we've just passed it."
"ฉันรู้แค่ว่ามีร้านขายอุปกรณ์ศิลปะ แต่ที่รู้ก็เพราะเพิ่งเดินผ่านมากัน"

show emi basic_closedgrin_rn
with charachange

# "Fortunately, Emi soon snaps her fingers in triumph."
"โชคดีที่ไม่นานเอมิก็ดีดนิ้วอย่างผู้มีชัย"

show emi basic_happy_rn
with charachange

# emi "That's it! There's a tea shop nearby!"
emi "จริงด้วย! แถวนี้มีร้านน้ำชาอยู่!"

# emi "We could have some tea and dry out, no problem!"
emi "ไปดื่มชารอให้ตัวแห้งได้สบายเลย!"

# "That doesn't sound like a bad idea."
"ก็ฟังดูไม่เลว"

# hi "Great! You know where it is?"
hi "แจ๋ว! เธอรู้ใช่มั้ยว่าร้านอยู่ไหน"

show emi basic_grin_rn
with charachange

# "Emi nods, looking fairly confident."
"เอมิพยักหน้าด้วยความมั่นใจ"

show emi basic_closedgrin_rn
with charachange

# emi "Sure do!"
emi "รู้!"

show emi basic_hes_rn
with charachange

# emi "I think."
emi "คิดว่านะ"

show emi excited_laugh_rn
with charachange

# emi "But it'll be an adventure either way, right?"
emi "แต่ก็จะได้ผจญภัยไง ใข่มั้ย"

# hi "Adventure, huh? Well, I suppose we could use a little adventure."
hi "ผจญภัยเหรอ อืม ผจญภัยกันหน่อยก็ดีมั้ง"

# "I think as long as we get out of the rain I'll be happy."
"ขอแค่ได้หลบฝนฉันก็พอใจแล้ว"

show emi basic_grin_rn at twoleft
show rin basic_absent_rn at tworight
with dissolvecharamove

# "The picnic basket is a little lighter now, at least."
"อย่างน้อยตอนนี้ตะกร้าปิกนิกก็เบาลงบ้าง"

# hi "Lead on!"
hi "นำไปเลย!"

show bg suburb_roadcenter_rn # scene is somehow bugged for the rain
hide rin
hide emi
with locationchange

# "Rin and I follow Emi as she weaves through the streets with something approaching confidence."
"รินกับฉันตามเอมิที่เดินไปตามถนนด้วยความอะไรบางอย่างที่คล้ายความมั่นใจ"

show emi basic_confused_rn at center behind rain
with charaenter

# emi "Now, a left here…"
emi "ทีนี้ก็เลี้ยวซ้าย…"

show emi excited_joy_rn
with charachange

# emi "There! The Shanghai!"
emi "นั่นไง! ร้านเซี่ยงไฮ้!"

# "Emi beams triumphantly as she points to the tea shop."
"เอมิยิ้มกระหยิ่มชี้ไปที่ร้านน้ำชา"

show bg suburb_shanghaiext_rn
hide emi
with locationchange

#If you have been at the Shanghai during Act 1
label th_E11x:

# "Come to think of it, I have been here before. It seems fairly crowded inside; entirely the fault of the sudden rain, I'm sure."
"จะว่าไปแล้วฉันก็เคยมาแล้วนี่นา ข้างในดูมีคนอยู่พอสมควร ซึ่งก็เป็นเพราะฝนตกนั่นแหละ"

play sound sfx_storebell
stop ambient fadeout 0.5
play music music_jazz fadein 2.0

scene bg suburb_shanghaiint
with locationchange

$ renpy.music.set_volume(0.7, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 2.0

with Pause(1.0)

show yuukoshang neutral_down at center
with charaenter

# yu "Welcome! Can I—"
yu "ยินดีต้อนรับค่ะ! รับ—"

show yuukoshang happy_down
with charachange

# yu "Oh, it's you."
yu "อ้าว เธอนี่เอง"

# "Yuuko seems to know Emi."
"ดูท่าว่ายูโกะจะรู้จักเอมิ"

show yuukoshang happy_down at tworight
show bg suburb_shanghaiint at bgright
with charamove

show emi basic_closedhappy at twoleft
with charaenter

# "Emi grins brightly, pleased to be remembered."
"เอมิยิ้มแฉ่งดีใจที่ยูโกะจำได้"

show emi basic_grin
with charachange

# emi "Hey Yuuko! Got room to seat us?"
emi "ไงคะคุณยูโกะ! มีที่นั่งว่างให้พวกหนูมั้ยคะ"

show yuukoshang neutral_down
with charachange

######

#If you have NOT been at the Shanghai during Act 1
label th_E11y:

# "It seems fairly crowded inside; a symptom of the sudden rain, I'm sure."
"ข้างในดูมีคนอยู่พอสมควร ซึ่งเป็นเพราะอยู่ ๆ ฝนก็เทลงมานั่นแหละ"

play sound sfx_storebell
stop ambient fadeout 0.5
play music music_jazz fadein 2.0

scene bg suburb_shanghaiint
with locationchange

$ renpy.music.set_volume(0.7, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 2.0

with Pause(1.0)

show yuukoshang neutral_down at center
with charaenter

# yu "Welcome! Can I—"
yu "ยินดีต้อนรับค่ะ! รับ—"

# "I'm surprised to find out that our waitress is none other than Yuuko."
"ฉันนึกแปลกใจที่เห็นว่าบริกรนั้นเป็นยูโกะ"

# "She sure looks the part in her uniform. It's hard to believe this is the same librarian from our school."
"ใส่ชุดนี้แล้วดูสมเป็นบริกรจริง ๆ แทบไม่อยากเชื่อว่านี่คือบรรณารักษ์จากโรงเรียนของเรา"

# "Does she work two jobs? I guess that must be it."
"ทำงานควบสองที่เหรอ คงเป็นงั้นแหละ"

show yuukoshang happy_down
with charachange

# yu "Oh, it's you."
yu "อ้าว เธอนี่เอง"

# "Yuuko seems to know Emi."
"ดูท่าว่ายูโกะจะรู้จักเอมิ"

show yuukoshang happy_down at tworight
show bg suburb_shanghaiint at bgright
with charamove

show emi basic_closedhappy at twoleft
with charaenter

# "Emi grins brightly, pleased to be remembered."
"เอมิยิ้มแฉ่งดีใจที่ยูโกะจำได้"

show emi basic_grin
with charachange

# emi "Hey Yuuko!"
emi "ไงคะคุณยูโกะ!"

# hi "Hi, Yuuko. I didn't know you worked here too."
hi "ไงครับคุณยูโกะ ไม่ยักรู้ว่าทำงานที่นี่ด้วย"

show yuukoshang worried_down
with charachange

# yu "Do I know you?"
yu "เรารู้จักกันเหรอ"

show yuukoshang worried_up
with charachange

# yu "You seem awfully familiar, but I don't think I've ever seen you in here."
yu "หน้าคุ้นมากเลยนะ แต่เหมือนไม่เคยเจอกันที่นี่เลย"

# hi "Er, we met at your other job. At the Yamaku library. Remember?"
hi "เอ่อ เราเจอกันคนละที่ครับ ที่ห้องสมุดยามากุไง จำได้มั้ยครับ"

show yuukoshang happy_up
with charachange

# "Her eyes widen in memory."
"พอนึกออกยูโกะก็ทำตาโต"

show yuukoshang closedhappy_down
with charachange

# yu "Yeah, that's it! Nice to see you again…"
yu "อ้อใช่! ยินดีที่ได้เจอกันอีกครั้ง…"

show yuukoshang panic_down
with charachange

# yu "Oh no, this is bad!"
yu "ไม่นะ แย่แล้ว!"

show yuukoshang panic_up
with charachange

# yu "I should have remembered a customer's face! I'm sorry… I'm terribly sorry!"
yu "ฉันต้องจำหน้าลูกค้าได้สิ! ขอโทษค่ะ… ขอโทษจริง ๆ !"

# "Yuuko goes from realization to panic in a split second, performing a series of high-speed bows. I narrowly avoid getting headbutted in the process."
"พอนึกออกปุ๊บยูโกะก็ตื่นตระหนกปั๊บพลางโค้งตัวขอโทษรัว ๆ ฉันแทบหลบหัวยูโกะไม่ทัน"

# hi "Whoa, hey, calm down!"
hi "เอ้ย เดี๋ยว ใจเย็นครับ!"

# hi "Listen, I wasn't a customer when we first met, in fact I hadn't ever been to the Shanghai, so it's all right."
hi "ฟังนะครับ ตอนเจอกันครั้งแรกผมไม่ใช่ลูกค้า แล้วผมก็ไม่เคยมาร้านเซี่ยงไฮ้เลยด้วยซ้ำ ไม่เป็นไรหรอกครับ"

# "Not the best display of logic, but it seems to relax her a little."
"ไม่ใช่ตรรกะที่ดีเท่าไหร่ แต่ยูโกะดูจะผ่อนคลายลง"

show yuukoshang worried_down
with charachange

# yu "Do you really think so?"
yu "เธอคิดว่างั้นเหรอ"

# hi "Uh, yeah, I'm sure. Positive. Isn't that right, girls?"
hi "เอ้อ อืม ครับ ใช่ ใช่มั้ยสาว ๆ"

show emi basic_closedgrin
with charachange

# "Emi has been watching this little drama unfold with considerable amusement."
"เอมิดูจะชอบใจที่ได้เห็นเราวุ่นวายกันเล็ก ๆ น้อย ๆ แบบนี้"

show emi excited_proud
with charachange

# emi "Yep, it sure is!"
emi "อื้ม ใช่เลย!"

show yuukoshang neutral_up
with charachange

# yu "Well, okay…"
yu "เอ่อ โอเค…"

show emi basic_happy
with charachange

# emi "So Yuuko, got room to seat us?"
emi "จะว่าไปคุณยูโกะ มีที่นั่งว่างให้พวกหนูมั้ยคะ"

show yuukoshang neutral_down
with charachange

#end split
label th_E11z:

$ renpy.music.set_volume(0.3, 3.0, channel="ambient")

# "Yuuko nods and leads us to a corner booth, providing us with some small towels before taking our order."
"ยูโกะพยักหน้าแล้วนำเราไปที่โต๊ะมุมด้านในแล้วนำผ้าขนหนูผืนเล็ก ๆ มาให้ก่อนจะรับรายการจากพวกเรา"

show yuukoshang happy_down
with charachange

# yu "What will you have?"
yu "รับอะไรดีคะ"

show emi basic_closedhappy
with charachange

# emi "Cake! And some tea too, I guess."
emi "เค้กค่ะ! แล้วชาด้วยก็ดี"

show yuukoshang neutral_down
with charachange

# yu "What kind of cake?"
yu "เค้กอะไรดีคะ"

show emi excited_proud
with charachange

# emi "Surprise me!"
emi "ตามใจคนทำเลยค่ะ!"

show yuukoshang worried_up
with charachange

# "Yuuko looks uncomfortable at the thought of surprising anyone, but she gives a nod and turns to Rin."
"ยูโกะดูจะอึดอัดที่ไม่ได้ตามใจลูกค้า แต่เธอก็พยักหน้าแล้วหันไปทางริน"

show rin invis:
    yalign 1.0 xpos 1.0 xanchor 0.6
with None

show yuukoshang neutral_down:
    xpos 0.55
show emi basic_grin at left
show rin basic_absent at right
show bg suburb_shanghaiint at center
with dissolvecharamove

# yu "And for you?"
yu "ทางนี้ล่ะคะ"

show rin negative_spaciness:
    right alpha 1.0
with charachange

# rin "I'll take a straw. My feet are all wet."
rin "ขอหลอดแล้วกัน เท้าเปียกหมดแล้ว"

show yuukoshang worried_up
with charachange

# yu "Sorry?"
yu "คะ?"

show rin basic_awayabsent
with charachange

# rin "The drinking kind of straw. One, please."
rin "หลอดดูด หนึ่ง ค่ะ"

show yuukoshang worried_down
with charachange

# "Yuuko is obviously uncertain of what to think about this. She fiddles with her pen and stationery for a moment, looking like she's about to cry, before turning in my direction."
"ยูโกะทำหน้าเหลอหลา เธอจับปากกากับกระดาษเล่นอยู่ครู่หนึ่งทำหน้าเบ้เหมือนจะร้องไห้ ก่อนจะหันมาทางฉัน"

show yuukoshang neutral_down
with charachange

# yu "And you, sir?"
yu "ทางนี้ล่ะคะ"

# hi "Just tea, I think."
hi "ขอเป็นชาแล้วกันครับ"

# "Emi would probably yell at me if I ordered cake."
"ขืนสั่งเค้กเอมิคงได้ดุฉันแหง"

show emi sad_depressed
with charachange

# emi "Aw, come on Hisao! Don't let me be the only one with food, I'll feel like a pig!"
emi "ไม่เอาน่าฮิซาโอะ! ปล่อยให้ฉันสั่งของกินคนเดียวได้ไง เหมือนตัวเองเป็นหมูตอนเลยเนี่ย!"

# hi "Just trying to eat healthy."
hi "ก็แค่รักษาสุขภาพเฉย ๆ"

# hi "Your orders, after all."
hi "เธอสั่งไว้นี่"

show emi basic_closedgrin
with charachange

# emi "Well… today is your day off! You can be healthy tomorrow!"
emi "เอ่อ… วันนี้วันพักผ่อนของนายนะ! เดี๋ยวค่อยรักษาสุขภาพพรุ่งนี้!"

# hi "Well then, I suppose I will have some cake after all."
hi "เอ่อ งั้นผมขอเค้กด้วยแล้วกันครับ"

show yuukoshang neurotic_up
with charachange

# "Yuuko seems slightly irritated that I'm changing my mind."
"ยูโกะดูจะหงุดหงิดเล็กน้อยที่ฉันเปลี่ยนใจ"

# yu "What kind?"
yu "เค้กอะไรดีคะ"

# "I glance at Emi and grin."
"ฉันเหลือบมองเอมิพลางแสยะยิ้ม"

# hi "Surprise me."
hi "ตามใจคนทำเลยครับ!"

show yuukoshang smile_down
with charachange

# "Yuuko sighs and nods."
"ยูโกะถอนหายใจพยักหน้า"

# yu "Very well. Your order will be out soon."
yu "ได้เลยค่ะ รอสักครู่นะคะ"

show emi basic_grin at left
show yuukoshang neutral_down
show rin basic_awayabsent
with shorttimeskip

# "Despite the crowd, our order does indeed arrive quickly."
"ถึงคนจะแน่นร้านแต่ของที่เราสั่งไปก็มาถึงอย่างรวดเร็ว"

show emi excited_joy
with charachange

# emi "Thanks, Yuuko!"
emi "ขอบคุณค่ะคุณยูโกะ!"

# "Yuuko nods in appreciation."
"ยูโกะพยักหน้าด้วยความยินดี"

stop music fadeout 4.0

show yuukoshang happy_down
with charachange

# yu "This is a different guy than usual, isn't it?"
yu "ผู้ชายคนนี้คนละคนกับคนที่มาด้วยทุกทีใช่มั้ย"

# "What? Different guy?"
"อะไรนะ คนละคน?"

show emi basic_hes
with charachange

# "Emi must notice my confusion, because she seems a little embarrassed."
"เอมิคงเห็นฉันที่ทำหน้างง ๆ เพราะเธอดูเขิน ๆ"

# emi "W-what? Oh, yeah, I guess he is."
emi "คะ คะ? เอ่อ ค่ะ มั้งคะ"

show emi sad_grin
with charachange

# emi "This is my friend Hisao."
emi "คนนี้เพื่อนหนูเอง ชื่อฮิซาโอะ"

# hi "We've met."
hi "เคยเจอกันแล้ว"

show yuukoshang smile_down
with charachange

# yu "Huh. Small world."
yu "หืม โลกกลมจัง"

show yuukoshang neutral_down
with charachange

# yu "Well, let me know if you need anything."
yu "อืม ถ้ามีอะไรอีกก็เรียกได้นะ"

hide yuukoshang
with charaexit

show emi sad_grin at twoleft
show rin basic_awayabsent at tworight
with charamove

# "With that, Yuuko takes off like a shot to wait on some other tables, leaving me to ponder her comment."
"แล้วยูโกะก็เคลื่อนตัวออกไปหาโต๊ะอื่นทิ้งให้ฉันคิดอยู่กับคำพูดนั้น"

# "Different guy, huh? I guess it makes sense, right? Emi's pretty popular, or so I've been told."
"คนละคนเหรอ ก็คงปกติสินะ เอมิก็เนื้อหอมพอสมควร เท่าที่ได้ยินมาอะนะ"

# "It's probably that kid from the track team."
"อาจจะเป็นคนนั้นที่เห็นในทีมกรีฑา"

# "This is stupid. I can just ask Emi."
"บ้าบอ ถามเอมิก็จบ"

show rin basic_absent
with charachange

play music music_comedy fadein 0.5

# hi "So who's this other guy, huh? You got a secret lover or something?"
hi "แล้วผู้ชายคนที่ว่านี่ใครเหรอ แอบซุกกิ๊กหรืออะไรเนี่ยเธอ"

show emi basic_closedhappy
show rin basic_awayabsent
with charachange

# "Emi laughs again, only I get the feeling it's from nervousness as much as anything else."
"เอมิหัวเราะอีกครั้ง แต่ก็เหมือนหัวเราะเพราะประหม่าหรืออะไรแบบนั้นมากกว่า"

show emi basic_grin
with charachange

# emi "It's just the track team captain. He likes coming down here after practice sometimes."
emi "หัวหน้าทีมกรีฑาน่ะ ซ้อมเสร็จบางทีเขาก็ชอบมาแวะร้านนี้"

show emi basic_closedgrin
with charachange

# emi "So if we have anything to discuss I tag along."
emi "แล้วพอมีอะไรที่ต้องคุยกันฉันก็ต้องตามมาด้วย"

# "Hmm, sounds mighty suspicious to me…"
"อืม ฟังดูน่าสงสัยมาก ๆ …"

show rin basic_absent
with charachange

# hi "Oh, I see."
hi "อ้อ อย่างนี้นี่เอง"

# "I could let the matter drop, but I can't resist at least getting another dig in."
"จะปล่อยเรื่องนี้ไปก็ได้ แต่ก็อดใจซักไซ้ต่อไม่ไหว"

# hi "So it {b}is{/b} a secret lover!"
hi "สรุปคือเธอซุกกิ๊กไว้{b}จริง ๆ{/b} ด้วย"

# hi "I knew it!"
hi "ว่าแล้วเชียว!"

show rin basic_deadpanamused
with charachange

# "Rin watches our play, seeming mildly amused before muttering something that I don't quite catch."
"รินดูเราสองคนด้วยความชอบใจเล็กน้อยก่อนพึมพำอะไรบางอย่างที่ฉันฟังไม่ค่อยถนัด"

# rin "… y'anyway"
rin "… แต่ก็นะ"

show emi basic_confused
with charachange

# $doublespeak(emi,hi,"What?", "Huh?")
$doublespeak(emi,hi,"อะไรนะ", "ฮะ?")

show rin basic_surprised
with charachange

# "Rin jerks back from wherever her mind wandered off to."
"รินได้สติหลุดจากภวังค์ที่เธอลอยไปอยู่เมื่อครู่"

# rin "Huh?"
rin "ฮะ?"

# hi "What did you just say?"
hi "เมื่อกี้เธอว่าไงนะ"

show rin basic_deadpan
with charachange

# rin "Huh."
rin "ฮะ"

# hi "No, before that."
hi "ไม่ ก่อนนั้นสิ"

show rin relaxed_nonchalant
with charachange

# rin "No idea."
rin "ไม่รู้"

# hi "Oh. Well."
hi "เออ ช่างเหอะ"

# hi "Okay."
hi "โอเค"

show emi basic_grin
show rin basic_deadpannormal
with charachange

# "I let the matter drop, but I can't help notice that Emi seems relieved that Rin interrupted the conversation."
"ฉันยอมปล่อยไป แต่ก็อดสังเกตไม่ได้ว่าเอมิดูโล่งใจที่รินเข้ามาขัดบทสนทนา"

# "Maybe I went a little too far…"
"สงสัยจะหยอกแรงไป…"

# "Conversation dies down for a moment as Emi and I busy ourselves with cake."
"ไม่มีใครพูดอะไรอยู่พักหนึ่งระหว่างที่เอมิกับฉันกินเค้กกัน"

# "Mine is strawberry, and surprisingly good."
"ของฉันเป็นเค้กสตรอว์เบอร์รี ซึ่งอร่อยผิดคาด"

play sound sfx_slide2

show emi excited_happy_close
with characlose

show emi basic_closedgrin
with charadistant

# "Emi seems to think so too, as she suddenly reaches over with her fork and steals a bit."
"เอมิคงจะคิดเหมือนกันถึงได้อยู่ ๆ ก็ยื่นส้อมมาตัดขโมยไปกิน"

# hi "Thief!"
hi "ขโมย!"

show emi excited_proud
with charadistant

# emi "Pirate. There's a difference."
emi "โจรสลัดต่างหาก ไม่เหมือนกันสักหน่อย"

# hi "We're not on water!"
hi "เราไม่ได้อยู่บนน้ำนะ!"

show emi basic_closedgrin
with charadistant

# emi "Well, no. But there's a lot of water outside, so it still works, right?"
emi "ก็จริง แต่ข้างนอกมีน้ำเยอะแยะเหมือนกันนี่ นับได้แหละ ใช่มั้ย"

show emi sad_grin
with charadistant

# emi "Besides, you can have some of mine. I think it's cranberry or something."
emi "อีกอย่าง นายจะกินของฉันด้วยก็ได้ เหมือนจะเป็นแครนเบอร์รีหรืออะไรนี่แหละมั้ง"

show emi sad_depressed
with charadistant

# emi "I should have asked for the strawberry. I like strawberries."
emi "รู้งี้สั่งสตรอว์เบอร์รีดีกว่า ฉันชอบสตรอว์เบอร์รี"

# hi "Feel free to help yourself to mine, if you really must."
hi "ถ้าอยากขนาดนั้นก็เต็มที่เธอเลยเถอะ"

# "For some reason, I feel compelled to add:"
"ไม่รู้ทำไมถึงได้อยากพูดต่อว่า"

# hi "Seeing as how you've already done it once, and all."
hi "ไหน ๆ ก็เอาไปหนึ่งคำแล้วนี่"

show emi basic_closedgrin
with charadistant

# "Emi sticks her tongue out at me, but that doesn't stop her from appropriating my cake. I try some of hers, as well."
"เอมิแลบลิ้นใส่ ทว่ายังไม่หยุดมือที่คอยฉวยเค้กฉัน ฉันชิมเค้กของเอมิบ้าง"

# "It's raspberry, and pretty good."
"ราสป์เบอร์รี ซึ่งก็อร่อยดี"

show rin relaxed_boredom
with charachange

# rin "The rain's let up."
rin "ฝนซาแล้ว"

# "It would appear that Rin is correct."
"เหมือนจะเป็นอย่างที่รินพูด"

# "Good timing, too. I've finished my food, and it looks like Emi has as well."
"ได้จังหวะพอดีด้วย ฉันกินของฉันหมดแล้ว เอมิก็กินหมดแล้วเหมือนกัน"

# hi "Well, we'd better pay and get a move on before it starts raining again."
hi "โอเค งั้นรีบจ่ายเงินแล้วออกจากร้านไปก่อนที่ฝนจะตกอีกรอบกัน"

stop ambient fadeout 1.0

scene bg suburb_shanghaiext_rn
with locationchange

# "It takes a few minutes to get Yuuko's attention, but we pay and get out pretty quickly."
"ผ่านไปสักสองสามนาทีถึงเรียกยูโกะได้ แต่เราก็จ่ายเงินแล้วออกจากร้านมาด้วยความรวดเร็ว"

show emi basic_grin_rn at center
with charaenter

# emi "So, do you want to return to the park?"
emi "แล้วอยากกลับไปที่สวนสาธารณะกันอยู่มั้ย"

# "My jaw nearly drops."
"ฉันอ้าปากหวอ"

# hi "Are you kidding? It's probably going to rain again!"
hi "ล้อเล่นปะเนี่ย เดี๋ยวฝนตกอีกรอบทำไง!"

# "In fact, I think I just felt some raindrops."
"เอาจริง ๆ ตอนนี้ก็เหมือนมีฝนหยดใส่แล้วด้วย"

show emi sad_grin_rn
with charachange

# emi "Hmm… you may be right."
emi "อืมม… ก็คงจริงของนาย"

show emi basic_closedgrin_rn
with charachange

# emi "Well okay, I'll let you off the hook this time, but you owe me a picnic now. Got it?"
emi "โอเค รอบนี้ฉันจะยอมปล่อยไป แต่ทีนี้ก็นับว่าติดหนี้ปิกนิกกับฉันแล้วนะ"

# "I don't know if she's addressing me, Rin, or the both of us."
"ไม่รู้ว่าเอมิพูดถึงฉันหรือริน หรือเราทั้งสองคน"

# hi "Fine, fine."
hi "ก็ได้ ๆ"

show emi excited_proud_rn
with charachange

# emi "Now hurry up! I wanted to get some laps in at the track, and it would be nice to do it without the rain."
emi "รีบไปกันได้แล้ว! ฉันอยากวิ่งที่ลู่สักสองสามรอบ ถ้าฝนตกใส่คงไม่ดีแน่"

# hi "I thought this was your day off!"
hi "ไหนบอกวันนี้พักผ่อนไง!"

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
stop music fadeout 6.0

show emi sad_depressed_rn
with charachange

# emi "Well…"
emi "เอ่อ…"

# "Emi suddenly seems reluctant to explain herself."
"อยู่ ๆ เอมิก็ดูอ้ำอึ้งไปไม่อยากแก้ต่าง"

show emi sad_grin_rn
with charachange

# emi "I need the practice."
emi "ฉันต้องซ้อม"

show emi basic_grin_rn
with charachange

# emi "And I need to burn off that cake, anyway."
emi "จะได้เป็นการออกกำลังกายเอาเค้กออกด้วย"

# "Why do I get the feeling that she's leaving something out?"
"ทำไมถึงรู้สึกเหมือนเอมิไม่ได้บอกอะไรให้หมดกันนะ"

# hi "Are you sure? It wasn't that much cake…"
hi "แน่ใจนะ ก็ไม่ได้กินเยอะขนาดนั้น…"

show emi basic_closedgrin_rn
with charachange

# emi "No, it wasn't that much cake for {b}you{/b}. I ate most of it."
emi "{b}นาย{/b}น่ะกินไม่เยอะ แต่ฉันเนี่ยกินไปเกือบหมด"

# "She's got a point there."
"ก็ถูกของเอมิ"

label th_choiceE11:
menu:
    with menueffect

    # "Still, I feel like I should at least offer to run with her…"
    "แต่ก็รู้สึกเหมือนอย่างน้อยก็ควรเสนอตัวไปวิ่งด้วย…"

    #Choice split: Offer to run with Emi/Keep quiet.

    # "Offer to run with Emi.":
    "เสนอตัวจะไปวิ่งกับเอมิ":
        return m1

    # "Keep quiet.":
    "ไม่พูดอะไร":
        return m2

label th_E11b:

#If you offer to run with Emi
# hi "Hey, I'll run with you."
hi "นี่ เดี๋ยวไปวิ่งด้วย"

# hi "I might as well, right?"
hi "ไหน ๆ ก็ไหน ๆ แล้วนี่นะ"

show emi basic_annoyed_rn
with charachange

# "Emi shakes her head emphatically."
"เอมิสั่นหัวด้วยความสงสาร"

# emi "No you won't, Hisao. Rest is critical for you, remember?"
emi "ไม่ ไม่ได้นะฮิซาโอะ นายต้องพักก่อน ลืมแล้วเหรอ"

# emi "I won't allow you to push yourself too hard."
emi "ฉันไม่ยอมให้นายฝืนตัวเองหรอกนะ"

# "I guess she's better at giving advice than taking it."
"คงจะเป็นคนจำพวกที่ให้คำแนะนำเก่งกว่าการรับฟังไว้เองสินะ"

# hi "Whatever you say, Emi."
hi "ตามเธอว่าเลยเอมิ"

# "I think it's probably best not to press the issue."
"อย่าไปตื๊อต่อเลยดีกว่า"

label th_E11c:

#If you selected to keep quiet, skip to here.

# "Come to think of it, she looks like she'd rather be alone right now."
"จะว่าไปแล้ว ตอนนี้เอมิก็เหมือนอยากอยู่คนเดียวด้วย"

# "I decide to keep my offer to myself."
"ฉันตัดใจเก็บข้อเสนอนั้นไว้กับตัวเอง"

label th_E11d:

#End split

stop music fadeout 12.0

scene bg school_dormext_full_rn
with locationskip


play ambient sfx_rain fadein 2.0
show rain normal
with Dissolve(2.0)

# "As we approach the girls' dormitory, it starts to rain again."
"พอมาถึงที่หอหญิงฝนก็เริ่มตกอีกรอบ"

show emi sad_annoyed_rn at center behind rain
with charaenter

# "Emi's expression sours slightly."
"เอมิทำหน้าไม่พอใจเล็กน้อย"

# emi "Aw, man…"
emi "โธ่เอ๊ย…"

# emi "Stupid rain."
emi "เจ้าฝนบ้า"

# hi "Hey, it'll let up soon enough. You can go running then, right?"
hi "เดี๋ยวก็หยุดตกน่า ไว้หยุดตกแล้วค่อยไปวิ่งก็ได้"

show emi basic_grin_rn
with charachange

# "Emi snorts, seemingly amused."
"เอมิหัวเราะหึดูชอบใจ"

show emi excited_proud_rn
with charachange

# emi "Like I'm not going to run in the rain."
emi "พูดเหมือนถ้าฝนตกแล้วฉันจะไม่วิ่งงั้นแหละ"

# hi "Well you shouldn't! You could catch a cold!"
hi "อย่านะเฮ้ย! เดี๋ยวก็เป็นหวัดหรอก!"

show emi basic_grin_rn
with charachange

# "Emi waves her hand airily."
"เอมิโบกไม้โบกมือเหมือนไม่ใช่เรื่องใหญ่"

# emi "Ridiculous! I don't get colds."
emi "ไร้สาระ! ฉันน่ะไม่เป็นหวัดหรอก"

show emi basic_closedgrin_rn
with charachange

# emi "My immune system is far too strong for something like that."
emi "ระบบภูมิคุ้มกันของฉันมันแข็งแกร่งเกินกว่าที่จะเป็นหวัดได้"

# "I can't help but laugh."
"ฉันอดหัวเราะไม่ได้"

# hi "Well, I'll see you tomorrow then, okay?"
hi "อืม งั้นก็เจอกันพรุ่งนี้นะ"

show emi basic_happy_rn
with charachange

# emi "Yeah!"
emi "อื้ม!"

show emi basic_grin_rn
with charachange

# emi "Thanks for coming! Oh, and for carrying the picnic basket!"
emi "ขอบคุณที่มาด้วยนะ! อ้อ แล้วก็ขอบคุณที่ช่วยถือตะกร้าด้วย!"

show emi excited_amused_rn
with charachange

# emi "I'll bring it for lunch tomorrow. We can have our picnic on the roof!"
emi "เดี๋ยวพรุ่งนี้จะเอาข้าวเที่ยงไปเผื่อ ปิกนิกกันที่ดาดฟ้าไง!"

# hi "Sounds good to me. See you then!"
hi "เยี่ยมเลย เจอกัน!"

hide emi
with charaexit

# "Emi grabs the basket from me and shoots through the door."
"เอมิหยิบตะกร้าไปแล้วพุ่งไปที่ประตู"

# "Rin gives me a sort of half-nod and ambles inside as well."
"รินกึ่ง ๆ พยักหน้าก่อนจะเดินนวยนาดเข้าไปข้างใน"

# "Damn, it's wet out here."
"เปียกไปหมดเลย"

# "I need to get back to my room and into some dry clothes."
"เดี๋ยวต้องกลับไปเปลี่ยนเสื้อผ้าที่ห้อง"

stop ambient fadeout 2.0

scene bg school_dormhallway
with locationskip

# "I'm soon in front of my door, but I am intercepted by the sudden appearance of Kenji, who appears to be carrying a stack of books."
"ไม่นานฉันก็มาถึงที่หน้าห้องตัวเอง แต่อยู่ ๆ เคนจิก็เข้ามาขัดขวางเสียก่อน เหมือนจะขนกองหนังสืออะไรมาด้วย"

show kenji neutral at center
with charaenter

# ke "Hey man, give me a hand, would you?"
ke "เฮ้ยพวก ช่วยหน่อยได้ปะ"

# hi "Huh?"
hi "ฮะ?"

play music music_kenji fadein 0.5

with vpunch

# "The books are unceremoniously dumped into my arms as Kenji fumbles with his room key."
"เคนจิโยนกองหนังสือใส่อ้อมแขนฉันโดยที๋ฉันไม่เต็มใจนัก เขาคุ้ยหากุญแจห้องตัวเอง"

show kenji happy
with charachange

# ke "Thanks, you're a lifesaver."
ke "ขอบใจ ช่วยได้เยอะเลย"

# ke "If you weren't around I'd have to keep my door unlocked, and that's just begging for trouble."
ke "ถ้าไม่มีนายฉันก็คงไม่ได้ปลดล็อกห้องแน่ ซึ่งก็จะยิ่งเป็นปัญหาไปอีก"

show kenji tsun
with charachange

# ke "The perfect opportunity to set up an ambush, or maybe just plant a bomb if they don't want to get their hands too dirty."
ke "เป็นจังหวะเหมาะที่จะได้ซุ่มโจมตี หรืออาจจะวางระเบิดไว้ถ้าไม่อยากให้มือต้องเปื้อนเลือดมากไป"

# ke "Probably don't."
ke "ซึ่งคงจะไม่อยาก"

# ke "Afraid they'll break a nail or something if they have to stab me."
ke "เพราะกลัวว่าพอแทบฉันแล้วเล็บจะหักหรืออะไรแบบนั้น"

# ke "Women."
ke "ผู้หญิง"

# "My mind thinks about digesting the verbal torrent that's just been unleashed, but elects to remain comfortably in the dark."
"สมองฉันกำลังประมวลผลกับกระแสคำพูดที่ถูกปลดปล่อยออกมานั้น ทว่าก็ยอมทิ้งหน้าที่ไม่คิดอะไรต่อแล้วอยู่\nแบบไม่รู้เรื่องนั่นแหละ"

# hi "Uh… huh."
hi "อ่า… ฮะ"

show kenji happy
with charachange

# ke "Anyway, where have you been, man?"
ke "แล้วสรุปไปไหนมาเนี่ย"

show kenji neutral
with charachange

# ke "I could have used some help carrying these back from the library!"
ke "แทนที่ฉันจะได้ให้นายช่วยขนหนังสือพวกนี้จากห้องสมุด!"

# ke "I knocked on your door, but you weren't there."
ke "ฉันมาเคาะประตูแล้วนายก็ไม่อยู่"

# hi "Oh, sorry."
hi "อ้อ ขอโทษที"

# "Not really. You appear to think I'm some kind of pack mule."
"ก็ไม่ได้รู้สึกผิดเท่าไหร่หรอก นี่เห็นเป็นเบ๊หรืออะไร"

# hi "I was out with Emi and Rin."
hi "พอดีออกไปข้างนอกกับเอมิแล้วก็รินน่ะ"

show kenji rage
with charachange

# "Kenji staggers back in shock."
"เคนจิถอยกรูดไปด้วยความสะพรึง"

# "It looks like I just shot his dog, if he had a dog."
"ทำหน้าเหมือนฉันไปยิงหมาของเขา ถ้าเขาเลี้ยงอะนะ"

# ke "The limbless ladies again?"
ke "สาวไร้รยางค์อีกแล้วเหรอ"

show kenji tsun
with charachange

# ke "What'd you do this time?"
ke "คราวนี้ไปทำอะไร"

# hi "Well, we wound up at the Shanghai—"
hi "ก็ไปร้านเซี่ยงไฮ้—"

# "I'm prevented from continuing by a sudden exclamation of despair."
"อยู่ ๆ เคนจิก็อุทานด้วยความสิ้นหวังขึ้นมาไม่ให้ฉันได้พูดต่อ"

show kenji rage
with vpunch

# ke "The Shanghai?"
ke "ร้านเซี่ยงไฮ้?"

# ke "Why the Shanghai?"
ke "ทำไมต้องเป็นร้านเซี่ยงไฮ้"

# ke "No no no no, man, you can't just go to the damn Shanghai!"
ke "ไม่ ๆ ๆ ๆ พวก ไปร้านเซี่ยงไฮ้ไม่ได้นะเว้ย"

# ke "It's the most dangerous place in the city!"
ke "ร้านนั้นคือที่ที่อันตรายที่สุดในเมืองนี้แล้ว!"

# ke "A veritable stronghold of their best agents!"
ke "เป็นฐานที่มั่นอย่างแท้จริงของตัวแทนระดับสูง ๆ เลยนะ!"

# ke "I know! I've met them!"
ke "ฉันรู้! ฉันเคยเจอ!"

# ke "They'll stop at nothing to lull you into a false sense of security, and then BAM!"
ke "พวกนั้นจะทำทุกวิถีทางเพื่อล่อหลอกให้นายตายใจ แล้วก็ตู้ม!"

play sound sfx_impact2
with vpunch

# "He hits his door for emphasis."
"เคนจิทุบประตูเป็นการเน้นย้ำ"

# ke "Wallet's gone. Bus pass? Gone. Identity? Fuckin' {b}gone{/b}, man!"
ke "กระเป๋าสตางค์หาย ตั๋วรถบัส? หาย บัตรประจำตัว? {b}หาย{/b} เฮ้ย!"

show kenji tsun
with charachange

# ke "Promise me you won't go there again!"
ke "สัญญาได้มั้ยว่าจะไม่ไปที่ร้านเซี่ยงไฮ้อีก!"

# "He seems so vehemently opposed to the idea of the Shanghai that I'm willing to lie a little in order to get to my room."
"เคนจิดูจะเคียดแค้นกับร้านเซี่ยงไฮ้เสียจนฉันนึกยอมโกหกสักหน่อยเพื่อที่จะได้เข้าห้องตัวเอง"

# hi "Sure, I won't go there again."
hi "ได้ จะไม่ไปอีกแล้ว"

# "Or at least, I won't ever tell you I've gone there again."
"หรืออย่างน้อยถ้าได้ไปอีกฉันก็จะไม่บอกนาย"

# "This seems to mollify my bespectacled companion."
"เพื่อนผู้สวมแว่นคนนี้ดูจะพึงใจที่ฉันตอบไปแบบนั้น"

show kenji neutral
with charachange

# ke "Good, good."
ke "ดี ๆ"

show kenji happy
with charachange

# ke "Sorry to come on so strong, but I know the danger there too well to let you just wander into the lion's den again."
ke "ขอโทษที่ทำตัวรุนแรง แต่ฉันรู้ดีว่าร้านนั้นอันตรายขนาดไหนถึงได้ไม่อยากให้นายต้องไปเพ่นพ่านอยู่ในถ้ำเสือ\nอย่างนั้นน่ะ"

# ke "You got out of there alive once, but twice is pushing it."
ke "นายไปครั้งเดียวแล้วรอดออกมาได้ แต่จะรอดออกมาได้อีกครั้งคงยากมาก"

# hi "Yeah, well I need to get changed and uh, do homework. So… I'll see you later."
hi "เออ คือฉันต้องไปเปลี่ยนเสื้อผ้าแล้วก็ เอ่อ ทำการบ้าน เพราะงั้น… เจอกัน"

show kenji tsun
with charachange

# ke "Huh?"
ke "ฮะ?"

show kenji neutral
with charachange

# ke "Oh, sure. Whatever."
ke "อ้อ เอ้อ เอาเหอะ"

# "I suddenly remember that I'm still holding his books."
"เหมือนเคนจิเพิ่งนึกได้ว่าหนังสือยังอยู่ในมือฉันอยู่"

# hi "You'd better take these."
hi "นายเอาหนังสือคืนไปได้แล้ว"

# "I catch a glimpse of one of titles, something about cryptography."
"ฉันเหลือบไปเห็นชื่อหนังสือเล่มหนึ่ง เหมือนจะเป็นเรื่องวิทยาการรหัสลับหรืออะไร"

# "What a weirdo."
"พิลึกคน"

stop music fadeout 6.0

show kenji neutral:
    center
    easeout 0.5 xpos 0.3 alpha 0.0
with None

# "Kenji grabs his precious cargo from me and disappears through his doorway."
"เคนจิรับของบรรทุกสุดล้ำค่าของตัวเองแล้วหายลับไปหลังประตูห้อง"

$ renpy.music.set_volume(0.1, 0.0, channel="ambient")
play ambient sfx_rain fadein 1.0

scene bg school_dormhisao
with locationchange

# "I open my own door and walk in, grateful to get out of my soaking wet clothes."
"ฉันเปิดประตูเดินเข้าห้องด้วยความดีใจที่จะได้ถอดเสื้อเปียก ๆ สักที"

# "The rain outside picks up, and I find myself hoping that Emi's not out running in this weather. She seemed so adamant about doing the run alone, I can't help but wonder if her leg's still bothering her."
"ฝนตกหนักขึ้น หวังว่าเอมิจะไม่วิ่งกลางแจ้งด้วยสภาพอากาศอย่างนี้นะ ดูจะอยากวิ่งคนเดียวเหลือเกิน\nฉันอดสงสัยไม่ได้ว่าเอมิยังเจ็บขาอยู่หรือเปล่า"

# "I try to remember whether or not I've seen her limping at all today, but I can't. Guess I was too caught up in enjoying the day, even if it did rain on us."
"ฉันเค้นสมองนึกว่าวันนี้เห็นเอมิขากะเผลกหรือเปล่า แต่ก็นึกไม่ออก สงสัยมัวแต่เพลินกับเรื่องวันนี้ ถึงจะฝนตกก็เถอะ"

# "And as I think back over the events of today, I keep finding myself focusing on my running partner."
"และระหว่างที่ย้อนนึกถึงเหตุการณ์วันนี้จิตใจฉันก็จดจ่ออยู่กับเพื่อนวิ่งของฉัน"

# "Her complete refusal to allow the rain to spoil her plans was incredibly cute."
"น่ารักดีที่ไม่ยอมให้ฝนมาทำแผนตัวเองล่ม"

# "But there was something else there, too."
"แต่ก็มีอีกเรื่องด้วยเหมือนกัน"

# "Sort of an unflappable attitude when it comes to enjoying the day as it comes."
"ท่าทีที่ไม่ย่อท้อกับการใช้ชีวิตไปแบบวันต่อวันให้สนุก"

# "I really like that quality."
"ฉันชอบตรงนั้นมาก"

# "Maybe I need to do a little of that myself."
"หรือฉันจะเอามาปรับใช้บ้างดีนะ"

stop ambient fadeout 2.0
scene black
with dissolve

$ suppress_window_after_timeskip = True


########################################################
label th_E12a:

window hide None

scene black
with dissolve

play sound sfx_alarmclock

with Pause(2.0)

scene bg school_dormhisao
with openeye

window show

# "The sound of my alarm brings me out of a dream involving pirates and some other stuff I can't really remember."
"เสียงนาฬิกาปลุกปลุกให้ฉันตื่นจากฝันเรื่องโจรสลัดกับเรื่องอื่น ๆ ที่ฉันจำไม่ค่อยได้"

scene bg school_track
with locationskip

play music music_pearly

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")

# "I'm a little bleary-eyed, and it feels like it takes me longer than usual to get dressed and down to the track."
"ตาฉันยังมัว ๆ อยู่ รู้สึกว่ากว่าจะแต่งตัวเสร็จแล้วมาที่ลู่ก็กินเวลาไปนานกว่าปกติ"

# "A glance at my watch reveals that I was right, and I am in fact running a little late."
"เมื่อเหลือบมองนาฬิกาก็เห็นว่าฉันคิดถูก และมาสายหน่อย ๆ ด้วย"

# "The thing is…"
"เรื่องคือ…"

# "There's no Emi."
"เอมิไม่อยู่"

# "That's odd. She should be here."
"แปลก เอมิควรจะมาแล้วสิ"

# "She definitely should be here."
"ต้องมาแล้ว"

# "I mean, I was {b}late{/b}."
"ก็ฉันมา{b}สาย{/b}"

# "I guess I wasn't the only one who had trouble getting up this morning."
"คงไม่ได้มีแค่ฉันละมั้งที่เช้านี้ลุกไม่ค่อยขึ้น"

# "The thought crosses my mind that it never quite stopped raining yesterday. Did she go running anyway?"
"ฉันเพิ่งนึกได้ว่าเหมือนเมื่อวานฝนจะไม่หยุดตกเลย นี่เมื่อวานเอมิยังออกไปวิ่งอยู่หรือเปล่า"

label th_E12b:

#if you offered to run with her

# "It seems likely. Emi's a lot of things, but cautious isn't one of them. She probably figured the rain wouldn't stop, and that's why she was so adamant about running alone."
"น่าจะใช่ คำว่ารอบคอบนั้นไม่ใช่ตัวเอมิเลย คงจะคิดว่ายังไงฝนก็ไม่หยุดถึงได้รั้นจะวิ่งคนเดียวขนาดนั้น"

# "Still, I would have gladly run with her, even if it was in the rain."
"แต่ฉันก็ยินดีวิ่งกับเอมินะ ต่อให้ต้องตากฝนก็เถอะ"

# "Heck, if anything I would have been able to convince her to come in once it got really bad. That would be why she didn't want me along, of course."
"ไม่สิ ถ้าฝนตกหนักจริง ๆ ก็ฉันนี่แหละจะชวนให้มาหลบฝนก่อน ซึ่งก็แน่ละว่าเพราะแบบนี้ถึงได้ไม่อยากให้ฉันไปวิ่งด้วย"

label th_E12c:

#If you kept quiet

# "I should have offered to run with her."
"รู้งี้เสนอตัวไปวิ่งด้วยก็ดี"

# "Then I could have talked her out of the idea, or at the least known that she was okay. What if she got struck by lightning or something?"
"จะได้เกลี้ยกล่อมให้ล้มเลิกความคิด หรืออย่างน้อยก็จะได้ดูให้แน่ใจได้ว่ายังสบายดี เกิดฟ้าผ่งฟ้าผ่าไปทำไง"

# "I'd never forgive myself."
"ฉันคงไม่ให้อภัยตัวเองแน่"

"…"

# "Okay, that's probably a little stupid."
"โอเค อันนี้ชักจะไร้สาระละ"

# "Emi's a resourceful girl. I doubt even she'd stay out in a thunderstorm."
"เอมิหัวดีจะตาย พายุฝนอย่างนี้ยังไงก็ไม่ออกมาวิ่งหรอก"

# "I trust her judgment on that matter, at least."
"อย่างน้อยฉันก็เชื่อใจเอมิเรื่องนี้นะ"

label th_E12d:

#end split

# "Even so, I can't help wanting to know where she is."
"แต่ถึงอย่างนั้นก็อดสงสัยไม่ได้อยู่ดีว่าตอนนี้เอมิอยู่ไหน"

# "…Well, nothing for it. I'd better stretch and run, and hope that Emi shows up with a grin and an excuse."
"…แต่เอาเถอะ สงสัยไปก็ไม่ได้อะไรขึ้นมา ยืดหยุ่นร่างกายไปออกวิ่งแล้วหวังว่าเอมิจะยิ้มร่ามาพร้อมข้ออ้างอะไรดีกว่า"

scene bg school_track_running
with shorttimeskip

show bg school_track_on
with Dissolve(3.0)

# "On my cool down lap, I am forced to admit that Emi isn't showing up."
"พอถึงช่วงคูลดาวน์ฉันก็ต้องจำใจยอมรับว่าเอมิไม่มาแล้ว"

# "Furthermore, I have no idea where she is. Anxiety gnaws at me while at the same time I wonder just why I'm so worried over her."
"ยิ่งไปกว่านั้นยังไม่รู้ด้วยว่าอยู่ไหน ฉันเป็นกังวลไปพร้อม ๆ กับคิดว่าทำไมถึงได้ห่วงเอมิขนาดนี้"

# "The run helped to take my mind off it for a little while, but now that I'm finished I'm back to worrying."
"ตอนวิ่งก็เลิกคิดไปได้พักหนึ่ง แต่พอวิ่งเสร็จก็กลับมาคิดมากอีกแล้ว"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

nvl clear

nvl show dissolve

# n "\n\nIt was weird not having her here."
n "\n\nพอเอมิไม่อยู่ด้วยแล้วแปลก ๆ"

# n "Downright unnerving."
n "ชวนให้ใจคอไม่ดีด้วยซ้ำ"

# n "It suddenly dawns on me that I've been running to hang out with Emi as much as I've been running to stay healthy - probably more to be with Emi, now that I think of it."
n "แล้วฉันก็ระลึกได้ว่าที่มาวิ่งก็ด้วยความอยากสองอย่างที่มีเท่า ๆ กัน คืออยากอยู่กับเอมิกับอยากรักษาสุขภาพ\nซึ่งพอมาคิดดูแล้วก็น่าจะเพราะอยากอยู่กับเอมิมากกว่า"

# n "It's one of those things that are completely obvious yet somehow, I never realized it."
n "เป็นเหมือนอย่างที่เขาเรียกว่าเส้นผมบังภูเขา"

# n "She really is someone I enjoy being with."
n "เอมิเป็นคนที่ฉันอยู่ด้วยแล้วสนุกจริง ๆ"

# n "As revelations go, it's hardly world-shaking."
n "ซึ่งพอคิดได้แล้วฉันก็ไม่ได้ตื่นเต้นอะไรขนาดนั้น"

# n "All the same, I find myself feeling slightly shocked."
n "และในขณะเดียวกันฉันก็ตกใจเล็กน้อย"

# n "When did this happen?"
n "เป็นแบบนี้ไปตั้งแต่ตอนไหน"

# n "Well, no time to think about this - though I want to ponder this new development, I have a greater desire to find out what's happened to Emi."
n "เอาเถอะ ไม่มีเวลามาคิดแล้ว ถึงจะอยากคิดเรื่องนี้ต่อ แต่ฉันอยากรู้มากกว่าว่าเกิดอะไรขึ้นกับเอมิ"

# n "I'll ask the nurse when I stop in to see him."
n "ไว้ถามคุณพยาบาลตอนไปแวะหาก็แล้วกัน"

$ renpy.music.set_volume(1.0, 2.0, channel="music")
stop music fadeout 2.0

nvl clear

nvl hide dissolve

scene bg school_nurseoffice
show nurse neutral at center
with shorttimeskip

# nk "Well, you seem to be in good shape, Hisao."
nk "ก็ดูแข็งแรงดีนะฮิซาโอะ"

# hi "That's good to hear."
hi "โล่งไปที"

# "I replace my shirt and stand to leave, as usual."
"ฉันใส่เสื้อแล้วยืนตั้งท่าจะเดินออกไปตามปกติ"

# "Except instead of leaving, I ask a question."
"แต่แทนที่จะออกไปฉันกลับถาม"

# hi "Hey, where's Emi? She didn't show up this morning."
hi "เอ่อ เอมิอยู่ไหนเหรอครับ เช้านี้ไม่เห็นไปวิ่ง"

# hi "Is she okay?"
hi "เอมิไม่เป็นอะไรใช่มั้ยครับ"

show nurse concern
with charachange

# "While I try valiantly to conceal the anxiety in my voice, the nurse's expression suggests that I've failed miserably."
"ฉันฝืนปกปิดไม่ให้น้ำเสียงมีความเป็นกังวลไปด้วย แต่สีหน้าคุณพยาบาลบอกว่าฉันปิดได้ไม่มิดเลย"

# nk "You mean she didn't tell you?"
nk "นี่เอมิไม่ได้บอกเธอเหรอ"

# nk "She's sick in bed."
nk "เอมิไม่สบายแล้วนอนพักอยู่น่ะ"

# hi "What? Sick?"
hi "ครับ? ไม่สบาย?"

show nurse neutral
with charachange

# "The nurse shrugs."
"คุณพยาบาลยักไหล่"

# nk "Yeah, she came to my office early this morning with a fever."
nk "อื้ม เช้านี้เอมิไข้ขึ้นเลยมาหาฉันน่ะ"

# nk "To be honest I'm surprised she made it here."
nk "เอาจริง ๆ ฉันก็แปลกใจเหมือนกันที่เอมิมาถึงนี่ได้"

show nurse concern
with charachange

# nk "She was burning up when she arrived."
nk "ตอนมาถึงตัวร้อนจี๋เลย"

# nk "I believe she'd planned to let you know, but she asked me to tell you - oh shoot!"
nk "ฉันคิดว่ายังไงเอมิก็คงจะเอาไปบอกเธออีกที แต่เห็นขอไว้ให้บอกเธอ… ตายละ!"

stop music fadeout 2.0

show nurse neutral
with charachange

# "The nurse gives me a sheepish smile that seems at least partially sincere."
"คุณพยาบาลยิ้มแหย ๆ ซึ่งเหมือนจะมาจากใจจริงอยู่"

# nk "I told her I'd stop by the track to let you know in case she forgot to. Sorry about that."
nk "ฉันบอกเอมิไปว่าจะไปแวะบอกให้เธอรู้เผื่อเจ้าตัวลืมบอกน่ะ ขอโทษทีนะ"

play music music_nurse fadein 1.0

show nurse fabulous
with charachange

# nk "But we don't need to tell Emi I forgot, right?"
nk "แต่เราจะไม่บอกเอมิเนอะว่าฉันลืม"

# "I return the nurse's smile with a devious one of my own."
"ฉันส่งยิ้มชั่วร้ายของฉันกลับไปให้คุณพยาบาลบ้าง"

# hi "Oh, of course not."
hi "โอ้ ไม่บอกหรอกครับ"

# hi "This is fine blackmail material."
hi "ขอเก็บไว้ขู่นะครับ"

# hi "I'll save it for whenever I need a favor from you."
hi "เผื่อว่าผมอยากให้คุณพยาบาลช่วยอะไร"

show nurse grin
with charachange

# "The nurse laughs."
"คุณพยาบาลหัวเราะ"

# nk "Well, I guess I deserve that."
nk "อืม ก็คงสมควรแล้วละ"

# nk "But you know, I've got tons of blackmail on you that you're not even aware of."
nk "แต่นี่นะ ฉันก็มีอะไรที่แม้แต่เธอก็ไม่รู้เอาไว้ขู่เธอได้เยอะเหมือนกัน"

show nurse fabulous
with charachange

# nk "So don't push your luck, okay?"
nk "เพราะงั้นก็อย่าหมายลองเชียว"

# "My expression earns another laugh from the nurse."
"สีหน้าฉันทำคุณพยาบาลหัวเราะอีกรอบ"

show nurse grin
with charachange

# nk "I'm just kidding, Hisao."
nk "ล้อเล่นหรอกน่าฮิซาโอะ"

show nurse concern
with charachange

# nk "But seriously - don't tell Emi I forgot, okay?"
nk "แต่จริงจัง ห้ามเอาไปบอกเอมินะว่าฉันลืม"

# hi "Your secret is safe with me."
hi "วางใจได้เลยครับ"

show nurse neutral
with charachange

# nk "Oh good. Now go on, get out of here."
nk "ดี ๆ ทีนี้ก็ไปได้แล้ว"

# hi "Wait, I've got one more question."
hi "เดี๋ยวครับ ผมมีอีกคำถาม"

show nurse fabulous
with charachange

# nk "Shoot."
nk "ให้ตาย"

# hi "Is she going to be okay?"
hi "เอมิจะไม่เป็นอะไรใช่มั้ยครับ"

show nurse grin
with charachange

# nk "Oh yeah, definitely."
nk "อ้อ ไม่เป็นหรอก"

show nurse neutral
with charachange

# nk "Her fever was high, but it was already starting to go down by the time she came by my office."
nk "ไข้สูงก็จริง แต่ตอนมาถึงห้องพยาบาลไข้ก็ลดไปเยอะแล้ว"

# nk "I'll probably check up on her again at lunch to be sure, but I expect she'll be up and about by the evening no matter what I tell her."
nk "เดี๋ยวสักเที่ยง ๆ ฉันจะไปดูเอมิอีกทีเพื่อความแน่ใจ แต่ต่อให้บอกอะไรไปเดี๋ยวเย็น ๆ ก็คงออกมาวิ่งเหมือนเดิมแหละ"

# hi "Hmm, maybe I should visit her after class."
hi "อืมม เดี๋ยวเลิกเรียนแล้วไปแวะหาดีกว่า"

# "It takes me a second to realize I've spoken aloud."
"ผ่านไปสองสามวินาทีฉันถึงรู้ตัวว่าฉันปล่อยให้ตัวเองหลุดพูดประโยคเมื่อกี้ไป"

show nurse fabulous
with charachange

# "The nurse raises an eyebrow and gives me a searching glance for a moment."
"คุณพยาบาลเลิกคิ้วขึ้นแล้วส่งสายตาเหมือนพิจารณาอะไรอยู่ครู่หนึ่ง"

# nk "Hmm…"
nk "อืมม…"

show nurse neutral
with charachange

# nk "Well, it might not be a bad idea."
nk "ก็ ได้อยู่นะ"

# nk "You could let me know if she'd taken a turn for the worse, I guess."
nk "ถ้าเกิดว่าเอมิอาการทรุดหรืออะไรก็มาบอกฉันแล้วกัน"

show nurse concern
with charachange

# nk "But no funny business, you got it? I know what meds you're on, after all."
nk "แต่ห้ามเล่นตุกติกนะ ฉันรู้ว่าเธอต้องกินยาอะไรบ้าง"

# "I think that's a threat against my life, but I'm not sure."
"อันนี้คือขู่เอาชีวิตกันหรือเปล่า ไม่แน่ใจ"

stop music fadeout 7.0

scene bg school_nursehall
with locationchange

# "Either way, I assure the nurse that my intentions are chaste and exit the office."
"แต่จะยังไงก็เถอะ ฉันบอกคุณพยาบาลไปว่าเจตนาฉันบริสุทธิ์แล้วออกมาจากห้องพยาบาล"

# "Interesting that the nurse sees me as some sort of potential suitor to Emi."
"น่าสนใจดีที่ว่าคุณพยาบาลเห็นว่าฉันจะเป็นคนที่มาตามจีบเอมิ"

# "Even more interesting is how pleased that makes me feel."
"และที่น่าสนใจกว่านั้นคือฉันดีใจมากที่คุณพยาบาลคิดแบบนั้น"

# "I need a shower."
"ต้องไปอาบน้ำก่อน"

scene bg school_scienceroom
with shorttimeskip

play sound sfx_normalbell

# "The lunch bell rings, and I find myself disinclined to make my way up to the roof."
"ระฆังพักเที่ยงดัง และฉันก็ไม่ได้อยากขึ้นไปที่ดาดฟ้าเลย"

# "After all, I'm betting Rin knows where Emi is, and if that's the case then I doubt she'd bother going up there."
"รินต้องรู้แหละว่าเอมิอยู่ไหน ซึ่งถ้ารู้แล้วรินก็คงไม่อยากไปที่ดาดฟ้าเหมือนกัน"

# "More to the point, I doubt we'd have any sort of scintillating conversation if she did. Chances are she'd prefer to be alone up there anyway, so I don't accidentally ruin her train of thought or something."
"ยิ่งไปกว่านั้น ต่อให้รินไปที่ดาดฟ้าจริง ๆ เราก็คงไม่ได้สนทนาอะไรที่น่าสนใจกันขนาดนั้น คงจะอยากอยู่ตัวคนเดียว\nมากกว่า ขืนไปเดี๋ยวจะไปขัดกระแสความคิดของรินหรืออะไรเข้าอีก"

# "Unfortunately, I don't really feel like heading to the cafeteria either."
"แต่โชคไม่ดีที่ฉันก็ไม่อยากไปโรงอาหารด้วยเหมือนกัน"

# "Guess I'll go to the library instead."
"ไปห้องสมุดก็แล้วกัน"

# "I need a new book to read anyway, having finished my other one yesterday before bed. Maybe I can find more by the same author."
"ฉันต้องไปหาหนังสือเล่มใหม่อ่านด้วย เพราะอ่านอีกเล่มจบไปเมื่อวานตอนก่อนนอนแล้ว อาจจะไปหาเล่มอื่น\nที่คนเดียวกันเขียน"

scene bg school_library
with locationskip

play music music_happiness fadein 2.0

# "I love libraries."
"ฉันรักห้องสมุด"

# "They smell like dust and paper and ink."
"ห้องสมุดนั้นมีกลิ่นฝุ่น กลิ่นกระดาษ กับกลิ่นหมึก"

# "All these stories and facts and opinions crowded together in one place makes the air come alive with potential."
"บรรยากาศมีชีวิตชีวาขึ้นมาด้วยพลังแห่งเรื่องราว ข้อเท็จจริง ข้อคิดเห็นทั้งหลายแหล่ที่มาอัดแน่นรวมตัวอยู่กัน\nในที่ที่เดียว"

# "I'm not sure how to navigate Yamaku's library yet, having mostly stuck to books I brought with me, so I search for the librarian to ask for help."
"เพราะยังไม่ค่อยแน่ใจกับผังห้องสมุดของยามากุเพราะที่ผ่านมาอ่านแต่หนังสือที่เอาติดตัวมาด้วย ฉันจึงหันไป\nขอความช่วยเหลือจากบรรณารักษ์"

"…"

# "Hmm. I suppose she's not arou—{w=0.5}{nw}"
"อืมม สงสัยจะไม่อ—{w=0.5}{nw}"

show yuuko smile_down:
    center
    xpos 0.4
    easein 0.5 center
with charaenter

# yu "…can't believe it."
yu "…ไม่อยากจะเชื่อเลย"

# "Yuuko, looking rather distracted, suddenly emerges from one of the aisles."
"ยูโกะที่ดูเหม่อ ๆ นั้นอยู่ ๆ ก็โผล่ออกมาจากทางเดินฟากหนึ่ง"

# hi "Er, excuse me."
hi "เอ่อ ขอโทษนะครับ"

show yuuko neutral_down
with charachange

# yu "Oh, can I help you?"
yu "อ้าว มีอะไรให้ช่วยมั้ย"

# hi "Actually, I was looking for a book…"
hi "คือผมมาหาหนังสือ…"

show yuuko panic_up
with charachange

# yu "So am I!"
yu "ฉันก็หาอยู่เหมือนกัน!"

show yuuko smile_down
with charachange

# yu "“Advanced Cryptography.” We just got it in, and now it's gone missing."
yu "“วิทยาการรหัสลับขั้นสูง” เพิ่งได้มาแท้ ๆ แต่หายไปแล้ว"

show yuuko worried_up
with charachange

# yu "I really, really wanted to read that one!"
yu "ฉันอยากอ่านเล่มนั้นมาก!"

# hi "Cryptography?"
hi "วิทยาการรหัสลับ?"

show yuuko neurotic_up
with charachange

# yu "Yeah, my… er, that is…"
yu "อื้ม คือ… เอ่อ คือว่า…"

# yu "This guy I knew. Know. Um."
yu "คนที่ฉันเคย ไม่เคยสิ รู้จัก เอ่อ"

# yu "Not sure how to describe it…"
yu "ไม่รู้จะว่ายังไงดี…"

# hi "Skip to the end."
hi "ขอตอนจบมาเลยครับ"

show yuuko smile_down
with charachange

# yu "He got me interested in cryptography only now the book's gone, and I think it's been stolen!"
yu "ฉันมาสนใจวิทยาการรหัสลับเพราะคนนั้น แล้วหนังสือเล่มนั้นก็หายไปแล้ว ฉันว่าต้องมีคนขโมยไปแน่ ๆ !"

# hi "Sounds pretty terrible."
hi "ลำบากน่าดูเลยนะครับ"

show yuuko worried_up
with charachange

# yu "Yeah, especially because now I have to search the whole library for it!"
yu "อื้ม แล้วตอนนี้ฉันต้องมาพลิกห้องสมุดหาอยู่เนี่ย"

# yu "Even though it's probably not even here!"
yu "ทั้งที่อาจจะไม่ได้อยู่ที่ห้องสมุดด้วยซ้ำ!"

# hi "You seem… busy."
hi "ดู… ยุ่ง ๆ นะครับ"

show yuuko neurotic_up
with charachange

# yu "A little."
yu "นิดหน่อย"

show yuuko neurotic_up:
    center
    easeout 0.5 alpha 0.0 xpos 0.6
with None

# "She dashes off down another aisle, and I resign myself to finding my own damn book."
"ยูโกะพุ่งตัวไปที่ทางเดินอื่น ส่วนฉันก็ต้องยอมมาหาหนังสือด้วยตัวเอง"

# "Hmm, plenty of choices."
"อืมม มีให้เลือกหลายเล่มเลย"

stop music fadeout 2.0

hide yuuko
with shorttimeskip

# "Oh come on, how did I get lost?"
"ให้ตายเถอะ หลงได้ไงเนี่ย"

# "These aren't even printed books! They're all in Braille."
"แถบนี้ไม่มีหนังสือพิมพ์ตัวอักษรด้วยซ้ำ เป็นอักษรเบรลล์หมดเลย"

# "I guess that makes sense in a school like this, but honestly, it's a little annoying."
"คงไม่แปลกแหละที่โรงเรียนแบบนี้จะมีหนังสืออักษรเบรลล์ แต่เอาตรง ๆ ก็แอบหงุดหงิดเหมือนกัน"

# li "I'm sorry, is someone there?"
li "ขอโทษนะคะ มีใครอยู่ตรงนั้นหรือเปล่า"

# "A lilting voice drifts out from behind one of the cubicles set up for research."
"น้ำเสียงชวนฟังนั้นดังมาจากโต๊ะล้อมกรอบที่ตั้งไว้สำหรับการค้นคว้าตัวหนึ่งที่อยู่ข้างหลัง"

show lilly basic_displeased at center
with charaenter

# "As I approach, I see that Lilly's been reading a book while I've been stomping about the aisles."
"พอเดินไปดูก็เห็นว่าลิลลี่กำลังอ่านหนังสืออยู่ระหว่างที่ฉันเดินไปมาตามทางเดิน"

# hi "Oh no, I should be apologizing. I didn't mean to make so much noise."
hi "ไม่เลย ฉันสิต้องขอโทษที่ส่งเสียงดังไปแบบนั้นน่ะ"

show lilly basic_ara
with charachange

# li "My, is that you Hisao?"
li "ตายจริง ฮิซาโอะเหรอ"

show lilly basic_smile
with charachange

# li "I've not heard from you in quite some time."
li "ไม่ได้ยินเสียงเธอมาสักพักแล้ว"

show lilly basic_pout
with charachange

# li "I was beginning to think you'd forgotten all about me."
li "คิดว่าเธอจะลืมฉันไปแล้วเสียอีก"

# hi "Er, sorry."
hi "เอ่อ ขอโทษที"

play music music_lilly fadein 4.0

show lilly basic_giggle
with charachange

# "Lilly laughs in that refined manner of hers and shakes her head."
"ลิลลี่หัวเราะตามท่าทีมีมารยาทประจำตัวแล้วสั่นหัว"

show lilly basic_smile
with charachange

# li "I'm only teasing you, Hisao."
li "แค่หยอกเล่นน่าฮิซาโอะ"

# li "From what I hear, you've been busy."
li "ได้ยินมาว่าช่วงนี้เธอยุ่ง"

show lilly basic_cheerful
with charachange

# li "Morning runs with Emi Ibarazaki {b}and{/b} lunch on the rooftop, if I'm not mistaken."
li "ต้องวิ่งยามเช้ากับเอมิ อิบาราซากิ {b}แล้วไหนจะ{/b}ต้องกินข้าวเที่ยงที่ดาดฟ้าอีก ถ้าจำไม่ผิดนะ"

# hi "Heh, yeah."
hi "ฮะ ๆ อื้ม"

# hi "Guess word gets around pretty quickly."
hi "ข่าวแพร่เร็วน่าดูเลยเนอะ"

show lilly basic_weaksmile
with charachange

# li "That and I can't coax poor Hanako on the roof any more."
li "ก็ใช่จ้ะ แล้วฉันก็ชวนให้ฮานาโกะผู้น่าสงสารไปที่ดาดฟ้าด้วยไม่ได้แล้ว"

show lilly basic_displeased
with charachange

# li "You three are always up there, claiming the spot for yourselves."
li "เธอสามคนอยู่บนดาดฟ้ายึดที่ไว้เองตลอดเลย"

# "She chides me gently, though it's pretty clear she's just teasing me again."
"ลิลลี่ดุฉันอย่างอ่อนโยน ถึงจะชัดก็เถอะว่าแค่หยอกเหมือนกัน"

# "Still, I feel an odd need to apologize."
"แต่ก็รู้สึกเหมือนต้องขอโทษยังไงไม่รู้"

# hi "Sorry, we could eat lunch somewhere else if it's a real problem—"
hi "ขอโทษนะ ถ้ามีปัญหาจริง ๆ เดี๋ยวเราไปกินข้าวเที่ยงกันที่อื่—"

show lilly basic_ara
with charachange

# li "Oh no, I wouldn't worry about it."
li "ไม่เลยจ้ะ ฉันไม่ถือหรอก"

show lilly basic_smile
with charachange

# li "Hanako and I have other things to do at lunch, too."
li "ตอนเที่ยงฮานาโกะกับฉันก็มีอย่างอื่นให้ทำด้วยเหมือนกัน"

# li "Such as read in the library, as you can see."
li "เช่นการอ่านหนังสือในห้องสมุดอย่างที่เห็นนี่แหละจ้ะ"

# hi "Oh, Hanako's here too? I didn't see her."
hi "อ้าว ฮานาโกะก็อยู่ด้วยเหรอ ไม่เห็นเลย"

show lilly basic_smileclosed
with charachange

# "Lilly smiles, a bit enigmatically."
"ลิลลี่ยิ้มเหมือนแฝงนัยอะไรไว้"

# li "Oh, she's around somewhere."
li "อืม ฮานาโกะเขาอยู่ไม่ไกลหรอกจ้ะ"

show lilly basic_smile
with charachange

# li "But I'm surprised, Hisao. You're in here, instead of up there."
li "แต่แปลกจะในฮิซาโอะที่เธอมาที่นี่แทนที่จะขึ้นไปบนนั้น"

# li "What brings you to the library?"
li "ลมอะไรหอบมาที่ห้องสมุดจ๊ะ"

# hi "Well, Emi's ill, so there's no lunch on the rooftop to keep me occupied…"
hi "ก็ เอมิไม่สบายน่ะ แล้วก็ไม่มีธุระต้องไปกินข้าวเที่ยงที่ดาดฟ้าด้วย…"

show lilly basic_giggle
with charachange

# "Lilly raises an eyebrow at my statement before giving another chuckle."
"ลิลลี่เลิกคิ้วขึ้นที่ได้ยินฉันพูดแบบนั้นก่อนจะแค่นหัวเราะอีกครั้ง"

# li "My, poor Rin must feel left out."
li "ตายจริง รินผู้น่าสงสารคงเหงาแย่เลย"

# hi "It's not like that!"
hi "ไม่ใช่อย่างนั้นนะ!"

show lilly basic_weaksmile
with charachange

# li "Ah, but I'm sure it isn't. Emi tends to be the life of whatever group she's in."
li "อืม แต่ฉันว่าใช่นะ เอมิน่ะไปอยู่กับกลุ่มไหนก็เป็นคนที่คอยทำให้กลุ่มมีชีวิตชีวาขึ้นมา"

show lilly basic_sad
with charachange

# li "It's a shame to hear she's fallen ill. Will she be okay?"
li "น่าสงสารจังที่เอมิไม่สบาย จะไม่เป็นอะไรใช่มั้ย"

# "Somehow I get the feeling that Lilly's just inquiring out of politeness, but I respond anyway."
"รู้สึกเหมือนแค่ถามตามมารยาทยังไงไม่รู้ แต่ฉันก็ตอบ ๆ ไป"

# hi "The nurse thinks so. I'm going to swing by and see how she's doing after school myself."
hi "คุณพยาบาลว่างั้นนะ เดี๋ยวเลิกเรียนแล้วฉันว่าจะไปแวะหาอีกทีเหมือนกัน"

show lilly basic_smileclosed
with charachange

# "Another raised eyebrow."
"ลิลลี่เลิกคิ้วขึ้นอีกครั้ง"

# li "My, what a noble gentleman you are, Hisao."
li "ตายจริง ช่างมีความเป็นสุภาพบุรุษเสียจริงนะฮิซาโอะ"

# hi "It's nothing, really. Just checking up on my friend, after all."
hi "เรื่องแค่นี้เอง แค่ไปหาเพื่อนที่ไม่สบายเฉย ๆ น่า"

show lilly basic_planned
with charachange

# li "Ah, so it's just friends, is it? How disappointing."
li "อ้อ แค่เพื่อนเหรอ น่าผิดหวังจริง"

# "I blush, glad that Lilly can't see it."
"ฉันหน้าแดงขึ้นมาพลางนึกโล่งใจที่ลิลลี่ไม่เห็น"

show lilly basic_giggle
with charachange

# "But somehow she knows that I've been flustered by her comment anyway, and laughs."
"แต่เหมือนลิลลี่จะรู้อยู่ดีว่าฉันเขิน เธอหัวเราะ"

# li "I'm sorry, Hisao. I'm teasing you again."
li "ขอโทษนะจ๊ะฮิซาโอะที่หยอกเธออีกแล้ว"

show lilly basic_smile
with charachange

# li "Please do tell Emi that I hope she feels better, won't you?"
li "ฝากอวยพรให้เอมิหายไว ๆ ทีนะ"

# "A glance at my watch reveals that I'm very nearly out of time to find my book."
"ฉันเหลือบมองนาฬิกา เวลาในการหาหนังสือของฉันจวนจะหมดลงแล้ว"

# hi "Of course."
hi "ได้"

# hi "Hey, I've got to find a book before lunch is over, so I'd better get moving."
hi "เออ ต้องไปแล้วละ พอดีต้องไปหาหนังสือก่อนหมดพักเที่ยง"

# hi "See you later."
hi "เจอกันนะ"

# "That was probably not the best phrase to use."
"อาจจะเป็นวลีที่ไม่เหมาะสักเท่าไหร่"

# "Lilly, however, takes my gaffe in stride."
"แต่ลิลลี่ก็ไม่ถืออะไรที่ฉันหลุดปากไป"

show lilly basic_weaksmile
with charachange

stop music fadeout 3.0

# li "Until we meet again, Hisao."
li "ไว้พบกันอีกจ้ะฮิซาโอะ"

scene bg school_hallway2
with shorttimeskip

# "I never do find the book I was looking for, but I walk out with something else instead."
"ฉันไม่เจอหนังสือที่หาอยู่ แต่ก็ได้อย่างอื่นติดมือออกมาแทน"

# "My stomach growls slightly, letting me know that I should have had something for lunch."
"ท้องฉันร้องเบา ๆ เตือนให้กินอะไรบ้างเป็นมื้อเที่ยง"

# "Oh well."
"เอาเถอะ"

# "I'll grab something before I visit Emi later."
"ไว้ค่อยหาอะไรกินก่อนไปเยี่ยมเอมิแล้วกัน"

########################################################
label th_E13:

scene bg school_hallway2
with None

scene bg school_scienceroom
with shorttimeskip

play music music_normal fadein 3.0

# "It seems as if time has decided to slow down for the express purpose of annoying the hell out of me."
"เหมือนว่าเวลาจะช้าลงเพื่อทำให้ฉันหงุดหงิดโดยเฉพาะ"

# "Class feels like it drags on for ages."
"คาบเรียนยืดยาวเหมือนนานเป็นชาติ"

# "I suspect that my being consumed with worry probably has something to do with it."
"ส่วนหนึ่งน่าจะเพราะความกังวลที่เกาะกุมในจิตใจ"

play sound sfx_normalbell

# "Blessedly the bell rings and I dash out of class, drawing a few raised eyebrows, I'm sure."
"พอระฆังมาโปรดแล้วฉันก็พุ่งตัวออกจากห้องเรียน ซึ่งฉันมั่นใจว่าต้องมีคนเลิกคิ้วด้วยความสงสั"

scene bg school_hallway3
with locationchange

# "I have spent the majority of the day fretting as unobtrusively as I could."
"ฉันใช้เวลาแทบทั้งวันไปกับการพะวงอย่างไม่ให้ใครจับสังเกตได้"

# "Even though the nurse thinks that Emi is perfectly okay, I want to see for myself."
"ถึงคุณพยาบาลจะบอกว่าเอมิสบายดี แต่ฉันก็อยากไปดูกับตาตัวเอง"

stop music fadeout 14.0

scene bg school_girlsdormhall
with locationskip

# "It doesn't take long to get to the girls' dormitory and make my way to Emi's room."
"ไม่นานก็มาถึงหอหญิง ฉันเดินไปที่ห้องเอมิ"

# "Standing outside her door, I suddenly pause. What if she's resting?"
"เมื่อมาถึงหน้าห้องแล้วฉันก็ชะงักไปทันที ถ้าเกิดว่าหลับอยู่ล่ะ"

# "I'd hate to wake her up, especially if she's still feeling ill."
"ถ้าเป็นงั้นก็ไม่อยากไปปลุกเลย ยิ่งถ้าเกิดยังไม่สบายอยู่ด้วย"

# "Then again, if she sleeps all day then it could throw off her sleeping schedule."
"แต่ก็นะ ถ้าเอาแต่นอนทั้งวันเดี๋ยวตอนกลางคืนก็นอนไม่หลับกันพอดี"

# "But rest is important if you're ill, isn't it?"
"แต่ถ้าป่วยอยู่ก็ต้องพักเยอะ ๆ สิ"

# "I can't decide what to do, so I settle for standing outside the door looking like an idiot."
"ฉันไม่รู้จะทำอย่างไรจึงได้แต่ยืนอยู่หน้าประตูเหมือนคนซื่อบื้ออย่างนั้น"

# "Then I hear Emi's voice from behind the door."
"แล้วก็ได้ยินเสียงเอมิจากอีกฟากประตู"

# emi "Thanks for your concern, but I really am okay."
emi "ขอบคุณที่เป็นห่วงนะ แต่ฉันไม่เป็นไรจริง ๆ"

# "Is she talking to me?"
"คุยกับฉันเหรอ"

# emi "I'll see you at practice tomorrow!"
emi "เดี๋ยวเจอกันตอนซ้อมพรุ่งนี้นะ!"

# "Guess not."
"ไม่น่า"

# "Still, clearly she's not asleep, so I can knock without worry."
"แต่ชัดแล้วว่าไม่ได้หลับอยู่ เพราะงั้นก็เคาะประตูได้ไม่มีปัญหา"

# "So why this clenched feeling in my gut? I wasn't nervous about dropping by the other day, so why today?"
"แล้วทำไมฉันถึงรู้สึกมวนท้องขึ้นมา ทั้งที่วันก่อนมาหาก็ไม่ได้ประหม่าเลย ทำไมถึงมาเป็นเอาวันนี้"

# "Granted, I still haven't really had time to figure out this newfound interest in Emi's well-being."
"จริงอยู่ว่าฉันไม่มีเวลาได้คิดว่าความอยากรู้ถึงความเป็นอยู่ของเอมินี้คืออะไร"

# "I don't have a lot of experience in the matter, of course, but certainly this seems to go beyond feelings of mere friendship."
"แน่ละว่าฉันไม่ได้มีประสบการณ์กับเรื่องนั้นนัก แต่ที่แน่ ๆ คือความรู้สึกนี้เกินคำว่าเพื่อนเฉย ๆ ไปแล้วแน่นอน"

# "But could I take that step? Could I even bring myself to risk what I have right now?"
"แต่ฉันจะก้าวไปก้าวถัดไปได้หรือเปล่า ฉันจะยอมเสี่ยงด้วยสิ่งที่มีอยู่ตอนนี้หรือเปล่า"

# "I mean it's enough to be friends with her, isn't it?"
"แค่เป็นเพื่อนกับเอมิก็พอแล้วนี่"

# "Either way, shouldn't I just open the door and see how she's doing? That's why I came here… right?"
"แต่จะอย่างไหนก็เถอะ เปิด ๆ ประตูไปดูเลยว่าเอมิเป็นยังไงก็จบแล้ว ที่มาที่นี่ก็คือจะมาหาอยู่แล้วนี่… ใช่มั้ย"

stop music fadeout 1.5

# "What if she's not dressed yet?"
"ถ้าเกิดว่ายังไม่ได้ใส่เสื้อผ้าล่ะ"

play ambient sfx_heartslow

with Fade (0.05, 0.0, 0.3, color="#ffc0cb")

# "The image that flashes through my mind causes my heart to skip a beat, literally."
"ภาพที่แล่นเข้ามาในหัวแวบหนึ่งนั้นทำใจฉันเต้นไม่เป็นจังหวะแบบตรงตัวอักษร"

stop ambient fadeout 3.0

# "I should probably not ever think those thoughts again. Not if I want to avoid a heart attack."
"ฉันไม่ควรจะไปคิดถึงเรื่องอะไรแบบนั้นอีก ถ้าไม่อยากหัวใจวายขึ้นมา"

# "I suddenly realize I'm still standing in the hallway looking like an idiot."
"อยู่ ๆ ก็นึกขึ้นได้ว่าฉันยังยืนอยู่ที่โถงทางเดินอย่างคนซื่อบื้อเหมือนเดิม"

play sound sfx_doorknock2

# "Emi still seems to be in the middle of a conversation, but I knock anyway. Hopefully she won't mind the interruption."
"เอมิเหมือนจะยังคุยไม่เสร็จ แต่ฉันก็เคาะประตู หวังว่าจะไม่ถือที่ฉันมาขัดนะ"

# emi "You worry too mu— Come in! The door's unlocked."
emi "เป็นห่วงกันมากไปแล้— เข้ามาเลย! ประตูไม่ได้ล็อก"

# "So it is. I open the door and step in, which is about where my thought process comes to a grinding halt."
"ไม่ได้ล็อกจริง ๆ ฉันเปิดประตูแล้วเดินเข้าไป เป็นจังหวะนั้นเองที่สมองฉันหยุดทำงาน"

play music music_serene fadein 4.0

scene ev emi_sleepy_face:
    subpixel True
    center
    zoom 1.05
    ease 15.0 zoom 1.0
with whiteout

# "Emi is sitting up in bed, her hair tousled from a day spent asleep. I think this is the first time I've seen her without those familiar beads in her hair."
"เอมินั่งอยู่บนเตียงโดยที่หัวยังยุ่งอยู่เพราะเพิ่งตื่นมาจากการนอนทั้งวัน น่าจะเป็นครั้งแรกเลยที่เห็นเอมิไม่ได้ใส่\nยางรัดผมที่มีลูกกลมอันคุ้นเคยนั้น"

# "Her gym shirt and bloomers, obviously hastily pulled on before I came in, are creased and folded from less than proper storage."
"เสื้อกับกางเกงพละที่ซ้อนกันยับยู่ยี่ไม่ได้เก็บให้เรียบร้อยจนเห็นชัดว่าก่อนฉันเข้ามาเอมิแค่ดึง ๆ รวบไว้ด้วยกัน"

scene ev emi_sleepy_legs at Fullpan(8.0)
with flash

# "Her legs lay bare on the sheets."
"ขาเปลือยเอมิวางอยู่บนที่นอน"

# "I've never seen Emi without prosthetics before. Yet here she is, slender legs terminating in stumps just below her knees."
"ฉันไม่เคยเห็นเอมิแบบไม่มีขาเทียมมาก่อนเลย ขาเรียวของเธอขาดหายไปเป็นตอตรงล่างหัวเข่า"

# "But as odd as the sight is, I find myself more captivated by everything north of the waist."
"แต่แม้ภาพตรงหน้าจะแปลกแค่ไหน ฉันก็ยิ่งรู้สึกหลงสเน่ห์ทุกอย่างที่อยู่เหนือเอวขึ้นไป"

scene ev emi_sleepy:
    subpixel True
    center
    zoom 1.05
    ease 15.0 zoom 1.0
with flash

# "It seems that Emi had finished her conversation with whoever was on the phone with her, and is now watching my reaction closely out of her one open eye as she wipes sleep from the other."
"ดูท่าว่าจะคุยกับคู่สนทนาปลายสายซึ่งเป็นใครก็ไม่รู้นั้นเสร็จแล้ว แล้วตอนนี้ก็หันมามองปฏิกิริยาฉันด้วยตาข้างหนึ่ง\nที่ลืมอยู่โดยยังขยี้ตาอีกข้างให้หายงัวเงียอยู่"

# "Her expression, far from being embarrassed, is rather one of a surprisingly wide yawn. One perhaps appropriate from such a small mouth."
"เอมิไม่ได้อายเลย เธอกลับหาวหวอดใหญ่เกินคาดใส่ฉัน อาจจะเป็นการหาวที่เหมาะแล้วกับปากเล็ก ๆ นั้น"

# "A grin that for a brief moment seems almost flirtatious tugs at the corner of her mouth as she takes the sight of me in."
"เอมิมองฉันพลางยกยิ้มขึ้นมุมปากเหมือนจะยั่วกันอยู่แวบหนึ่ง"

# "I can do nothing but remain in a state fluctuating between fear, confusion, and not a little bit of lust."
"ในสมองฉันมีแต่ความกลัวและความสับสนที่หมุนวนไปมาโดยไม่ได้มีความใคร่อยู่ในนั้นเลย"

# "Emi hastily sweeps her hair out of her eyes, fixing it back into place before addressing me."
"เอมิปัด ๆ ผมที่ปรกหน้าอยู่แล้วจัดแจงให้เรียบร้อยก่อนเรียกฉัน"

scene bg school_dormemi
show emi sad_grin_gym at center
with locationchange


# emi "You seem a bit caught off guard, Hisao."
emi "ดูตกใจเชียวนะฮิซาโอะ"

# "A wave of laughter erupts from her, and I find myself grinning and rubbing the back of my head ruefully."
"แล้วเอมิก็หัวเราะออกมา ฉันยิ้ม ๆ แล้วลูบท้ายทอยแก้เก้อ"

# hi "Sorry, I've just…"
hi "ขอโทษที พอดี…"

# "Never seen someone so disheveled look so attractive."
"ไม่เคยเห็นใครที่ดูไม่เรียบร้อยแต่มีสเน่ห์ขนาดนี้"

# "Never seen you without your legs on."
"ไม่เคยเห็นเธอตอนไม่ใส่ขาเทียม"

# "Never seen you look so…"
"ไม่เคยเห็นเธอ…"

# hi "Um, sorry."
hi "เอ่อ ขอโทษที"

show emi basic_closedgrin_gym
with charachange

# "Emi giggles again and moves to sit up a little straighter."
"เอมิหัวเราะคิกคักแล้วนั่งหลังตรง"

# "I'm caught up in the movements of her shirt, very nearly losing myself."
"ฉันผงะที่เสื้อเธอขยับแบบนั้นจนแทบเสียสติ"

show emi basic_grin_gym
with charachange

# emi "I was wondering what your reaction would be."
emi "คิดอยู่ว่านายจะตอบสนองยังไงน่ะ"

show emi basic_closedhappy_gym
with charachange

# emi "The nurse called and told me you were going to drop by, you see."
emi "ก็เนี่ย คุณพยาบาลโทร. มาบอกว่านายจะแวะมาหา"

show emi basic_grin_gym
with charachange

# emi "And I know you haven't seen me… well, you know."
emi "แล้วก็รู้ด้วยว่านายยังไม่เคยเห็นฉันตอน… ก็ นั่นแหละ"

show emi sad_grin_gym
with charachange

# emi "Without legs."
emi "ไม่มีขา"

# "I respond in a tone of casual surprise."
"ฉันตอบไปด้วยน้ำเสียงแปลกใจแบบสบาย ๆ"

# hi "Oh, you don't have them on? I didn't notice."
hi "อ้าว ไม่ได้ใส่เหรอ ไม่ทันสังเกตเลย"

# "This is almost the truth. I very nearly didn't."
"ซึ่งก็นับว่าจริงอยู่ เพราะฉันเกือบจะไม่ได้สังเกตแล้ว"

# "I'm not trying to be suave or anything, mind you. Somehow I think Emi would get offended by that."
"แต่บอกไว้ก่อนว่าฉันไม่ได้จะทำตัวเป็นคนมั่นหน้าหรืออะไร ไม่รู้ทำไมเอมิเหมือนจะไม่พอใจ"

stop music fadeout 0.5
play sound sfx_pillow
show emi basic_annoyed_gym
with vpunch

# "Instead, she sticks her tongue out at me and chucks a pillow at my head."
"เอมิกลับแลบลิ้นแล้วปาหมอนใส่หัวฉัน"

# emi "Ass."
emi "บ้า"

# "I deftly catch the pillow and take careful aim before throwing."
"ฉันคว้าหมอนไว้อย่างรวดเร็วแล้วเล็งให้ดีก่อนปากลับ"

play music music_running

show emi basic_annoyed_gym:
    center
    parallel:
        ease 0.5 xpos 0.7
    parallel:
        "emi basic_closedhappy_gym" with Dissolve(0.5, alpha=True)

# "Emi laughs and rolls to one side, dodging my shot, the shifting of her shirt distracting me enough so that the next thrown pillow hits me right between the eyes."
"เอมิหัวเราะแล้วกลิ้งตัวไปด้านข้างหลบหมอนที่ปาไป เสื้อเธอที่เลิกขึ้นทำฉันเสียสมาธิจนเมื่อเธอปามาอีกรอบ\nก็โดนเข้าที่หว่างคิ้วเต็ม ๆ"

play sound sfx_pillow

# hi "Oof!" with hpunch
hi "อุ๊บ!" with hpunch

# "I retaliate, of course."
"แน่ละว่าฉันต้องถอย"

# "And once I've retaliated twice, well, a war was bound to break out sooner or later."
"และเมื่อฉันถอยไปสองรอบแล้วสงครามก็จะเริ่มขึ้นในไม่ช้าก็เร็ว"

# "And really, when Emi appears to have far better aim than me, well…"
"และยิ่งเอมิเหมือนจะเล็งแม่นกว่าฉันด้วย ก็นะ…"

# "It was just a matter of time before I'd have to resort to a suicidal charge."
"ไม่นานฉันก็ต้องพึ่งวิธีการจู่โจมพลีชีพแล้ว"

show bg school_dormemi:
    center
    ease 0.5 bgleft

show emi basic_closedhappy_gym:
    ease 0.5 center

with None

show emi basic_closedhappy_gym_close:
    ease 0.5 center

with characlose

# hi "Gotcha!"
hi "ได้ตัวละ!"

show emi basic_hes_gym_close
with charachange

# emi "Eep!"
emi "ว้าย!"

window hide None

play sound sfx_pillow

show comic vfx1
show emi basic_closedsweat_gym_close
with vpunch

with Pause(0.5)

play sound sfx_pillow

show comic vfx2
with hpunch

with Pause(0.5)

play sound sfx_pillow

show comic vfx3
with vpunch

with Pause(0.5)

show comic vfx3:
    truecenter
    easeout 0.5 yanchor 0.3 alpha 0.0
with Pause(0.5)

#"{size=40}BAM!{/size} {w=0.5}{nw}" with vpunch

#extend "{size=40}SMACK!{/size} {w=0.5}{nw}" with hpunch

#extend "{size=40}BIFF!{/size}" with vpunch

stop music fadeout 3.0

scene black
with dissolve

window show

# "And once the charge was accomplished, well, of course I'd have to wrestle the pillows away from her."
"และเมื่อจู่โจมสำเร็จแล้วก็แน่นอนว่าฉันต้องปลุกปล้ำดึงหมอนออกมาจากมือเอมิ"

# "And with that kind of struggle, of course we'd wind up in this sort of position."
"และเมื่อดิ้นกันไปมาแบบนั้นก็แน่นอนว่าเราต้องมาอยู่กันท่านี้"

window hide

play music music_twinkle fadein 2.0

scene ev emi_bed_full:
    xalign 0.5 yalign 1.0 subpixel True
    easein 15.0 yalign 0.0

with Dissolve(1.0)

with Pause(3.0)

window show

# "And so I find myself staring down at her from my position atop her."
"และฉันก็มาคร่อมตัวเอมิมองเธอ"

# "She's grinning, eyes sparkling with amusement, maybe a little sweaty now from our tussle."
"เอมิยิ้มพร้อมตาเป็นประกายด้วยความสนุก เหงื่อออกเล็กน้อยจากการที่เราออกแรงกัน"

# "Her chest is heaving up and down, sucking in air."
"หน้าอกเธอกระเพื่อมขึ้นลงสูบอากาศเข้าออก"

# "The small bit of my brain that is not currently enraptured by the sight and the smell of her observes that she must still be ill, because her stamina's not what it should be."
"สมองเสี้ยวหนึ่งของฉันที่ยังไม่หลงสเน่ห์ไปกับกลิ่นของเธอกับภาพตรงหน้านี้บอกว่าเอมิยังไม่หาย เพราะแรงไม่ได้เยอะ\nเหมือนทุกที"

# "We stay that way for a while."
"เราค้างกันอยู่ท่านั้นพักหนึ่ง"

# "I'm not sure how long, because everything seems to go fuzzy. Everything that isn't her, anyway."
"ไม่แน่ใจว่าอยู่กันนานแค่ไหนเพราะทุกอย่างเลอะเลือนไปหมด ทุกอย่างที่ไม่ใช่เอมิน่ะนะ"

# "Her eyes meet mine, and deep inside them I almost catch a glimpse of… what, fear? Longing?"
"เอมิสบตากับฉัน ในเบื้องลึกนัยน์ตาเธอนั้นฉันเหมือนเห็นแวว… อะไรล่ะ ความกลัว? ความโหยหา?"

# "Hope?"
"ความหวัง?"

# hi "Emi…?"
hi "เอมิ…?"

stop music fadeout 0.5

show ev emi_bed_unsure at center
with vpunch

# "A cough suddenly convulses her, and I'm almost stumbling in my haste to get off, to apologize for everything."
"อยู่ ๆ เอมิก็ตัวกระตุกเพราะไอ ฉันจึงต้องรีบผละตัวออกมาขอโทษจนแทบล้มทับเอมิ"

play music music_emi fadein 3.0

# hi "Sorry, I shouldn't have…"
hi "ขอโทษที ฉันไม่น่า…"

show ev emi_bed_happy
with charachange

# emi "It's fine, it's fine."
emi "ไม่เป็นไร ๆ"

# "She gives me a reassuring pat on the shoulder."
"เอมิลูบบ่าฉันเป็นการปลอบใจ"

show ev emi_bed_normal
with charachange

# emi "So… what brings you here?"
emi "แล้ว… ไปไงมาไงถึงมานี่"

# "She's still breathing hard, and that causes her voice to shake slightly."
"เอมิยังหอบอยู่จนเสียงสั่น"

# hi "Well, before I was so rudely assaulted by pillows, I came to see how you were doing."
hi "ก็ ก่อนหน้าที่ฉันจะโดนจู่โจมด้วยหมอนสุดหยาบคายเมื่อกี้ ฉันมาดูว่าเธอเป็นยังไงบ้างน่ะ"

window hide None

play sound sfx_pillow

show comic vfx4
show ev emi_bed_frown
with vpunch

with Pause(0.5)

show comic vfx4:
    truecenter
    easeout 0.5 yanchor 0.3 alpha 0.0
with Pause(0.5)

window show

# "This earns me another shove, and I very nearly fall off her bed."
"พอพูดแล้วเอมิก็ผลักตัวอีกรอบจนฉันแทบตกเตียง"

show ev emi_bed_normal
hide comic
with charachange

# "Emi's eyes sparkle again, and I wonder how I never noticed how attractive they are before."
"เอมิทำตาเป็นประกายอีกรอบ ฉันนึกสงสัยว่าที่ผ่านมาฉันต้องตาถั่วขนาดไหนถึงไม่เห็นสเน่ห์ของตาคู่นี้นะ"

show ev emi_bed_smile
with charachange

# emi "Consumed with worry, were you?"
emi "เป็นห่วงกันละสินาย"

# "Her tone is mocking, haughty. Teasing."
"น้ำเสียงเอมิฟังดูจองหองเหมือนล้อเลียน ฟังดูเหมือนหยอกกัน"

# "She throws her arm across her forehead dramatically, grin still apparent from underneath."
"เอมิยกแขนขึ้นมาพาดหน้าแบบเล่นใหญ่ โดยยังมีรอยยิ้มอยู่ภายใต้แขนข้างนั้น"

show ev emi_bed_unsure
with charachange

# emi "Couldn't bear the thought of me laying deathly ill?"
emi "ทนไม่ได้ละสิที่ฉันต้องนอนป่วยเหมือนใกล้ตายน่ะ"

# "As we both recover from our brief wrestling match, Emi appears to fall back on teasing me."
"ระหว่างที่เราพักหายใจจากการแข่งมวยปล้ำนั้นอยู่ครู่หนึ่งนี้เอมิก็เหมือนจะกลับมาหยอกฉันอีกแล้ว"

# hi "Well, I wouldn't say consumed with worry, but after you didn't show up this morning like a total wuss…"
hi "ก็ ไม่เชิงว่าเป็นห่วงหรอก แต่พอเห็นว่าเช้านี้เธอทำตัวเหมือนไก่อ่อนไม่ยอมมาวิ่ง…"

show ev emi_bed_frown
with charachange

# "Emi pouts, crossing her arms petulantly and sticking her lower lip out."
"เอมิทำแก้มป่องกอดอกเหมือนขัดใจแล้วเบะปาก"

# emi "It's not my fault."
emi "ไม่ใช่ความผิดฉันสักหน่อย"

# emi "Nurse wouldn't allow it."
emi "คุณพยาบาลห้ามฉัน"

# hi "Sure he wouldn't. I completely believe you."
hi "คงห้ามแหละเนอะ ฉันเชื่อเธอสุดหัวใจเลย"

# "Emi sticks her tongue out again."
"เอมิแลบลิ้นอีกรอบ"

# emi "You're such a jerk, Hisao."
emi "ใจร้ายจริง ๆ นะนายเนี่ยฮิซาโอะ"

# hi "So how was your day then, eh? Did you enjoy slacking off?"
hi "แล้ววันนี้เป็นไงบ้าง นอนอู้สบายมั้ย"

show ev emi_bed_normal
with charachange

# emi "Not really, the phone woke me up pretty early on."
emi "ไม่เท่าไหร่ พอดีมีสายโทร. เข้ามาปลุกฉันน่ะ"

# hi "The phone?"
hi "โทร. เข้ามา?"

# emi "Yeah, the captain of the team called to make sure I was doing okay."
emi "อื้ม หัวหน้าทีมโทร. มาถามว่าสบายดีหรือเปล่า"

# emi "Also to let me know it was okay to skip practice."
emi "แล้วก็บอกด้วยว่าขาดซ้อมได้ไม่เป็นไร"

# "Good, at least she wasn't alone all day. Someone checked up on her."
"ดีแล้ว อย่างน้อยก็ไม่นอนเหงาอยู่ทั้งวัน ยังมีคนคอยดูอาการอยู่"

# "Although I can't help but think that it should have been me."
"แต่ก็อดคิดไม่ได้ว่าทำไมคนนั้นถึงไม่เป็นฉันนะ"

# hi "Oh, that's good."
hi "อ้อ ดีแล้ว"

# hi "He really keeps an eye on you, huh?"
hi "เขาดูแลเธอดีน่าดูเลยนะ"

show ev emi_bed_smile
with charachange

# "Emi shrugs."
"เอมิยักไหล่"

# emi "It's his job."
emi "ก็ตามหน้าที่"

# emi "Part of being the captain means you know where your team members are when they're not in school."
emi "เป็นหัวหน้าทีมก็ต้องรู้ว่าสมาชิกทีมอยู่ไหนถ้าไม่ได้อยู่ในโรงเรียน"

# emi "Still, I guess it was nice of him to call, huh?"
emi "แต่ก็นะ ถือว่ามีน้ำใจแหละที่ยังโทร. หากัน"

# hi "Yep. Sure was."
hi "อื้ม ใช่"

# "Emi yawns and shimmies down into a more comfortable position."
"เอมิหาวแล้วจัดท่าให้นอนสบายขึ้น"

show ev emi_bed_normal
with charachange

# emi "So how was your day?"
emi "แล้ววันนี้นายเป็นไงบ้าง"

# hi "Kind of uneventful, you know?"
hi "ก็ไม่ค่อยมีอะไรนะ"

# hi "I went ahead and ran by myself, and talked with the nurse about how you were doing…"
hi "ฉันไปวิ่งตัวคนเดียว แล้วก็คุยกับคุณพยาบาลเรื่องอาการของเธอ…"

stop music fadeout 2.0

scene bg school_dormemi_ni
with shorttimeskip

# "I meander through the day's events, none of which are particularly engrossing."
"ฉันย้อนรำลึกถึงเหตุการณ์ในวันนี้ที่ไม่ค่อยมีเนื้อหาสาระสักเท่าไหร่"

# "That's when I'm distracted by an arm finding its way across my waist."
"ซึ่งก็เป็นจังหวะนั้นที่ฉันรู้สึกถึงแขนที่โอบเอวฉันอยู่"

# "It seems that Emi fell asleep while I was talking so I draw her blanket to cover us."
"เหมือนเอมิจะผล็อยหลับไปตอนที่ฉันพูดอยู่ ฉันดึงผ้าห่มมาคลุมตัวพวกเราไว้"

play music music_comfort fadein 9.0

scene ev emi_sleep_unsure
with locationchange

# "She's rolled over on to her side, and now one leg is thrown over my legs, effectively trapping me."
"เอมินอนตะแคงจนขาข้างหนึ่งมาพาดขาฉันจนฉันหนีไปไหนไม่ได้"

# hi "Hey."
hi "นี่"

# "It seems a shame to wake her, but I have things to do."
"ไม่อยากปลุกเลย แต่ฉันก็มีธุระของฉันเหมือนกัน"

play sound sfx_rustling

# "I gently shake her, but in response she only tightens her arm's grip on me and sighs a little."
"ฉันเขย่าตัวเอมิเบา ๆ ทว่าเธอกลับโอบฉันไว้แน่นขึ้นกว่าเดิมแล้วถอนหายใจเบา ๆ"

# "My resistance to this position crumbles rather quickly."
"ฉันถอดใจไม่อยากต้านทานท่านี้อีกอย่างรวดเร็ว"

# "The feeling of her body breathing steadily is both calming and incredibly stimulating at the same time."
"สัมผัสจากร่างกายเธอที่หายใจเข้าออกอย่างสม่ำเสมอนั้นชวนให้ใจสงบและไม่สงบเป็นอย่างมากไปพร้อม ๆ กัน"

# "My breathing cannot decide if it wants to relax or speed up."
"ลมหายใจของฉันลังเลว่าจะผ่อนลงหรือเร่งขึ้นดี"

# "Relaxation wins, and I find myself putting an arm around Emi."
"สุดท้ายก็ผ่อนลง ฉันโอบเอมิไว้"

scene ev emi_sleep_normal
with dissolve

# hi "I think I'm in love."
hi "ฉันว่าฉันกำลังมีความรัก"

# "The words slip out and hang in the air unnoticed."
"คำพูดนั้นหลุดลอยออกมาอยู่ในอากาศโดยไม่มีใครได้ยิน"

# "At least I hope they've gone unnoticed."
"อย่างน้อยก็หวังว่าจะไม่มีใครได้ยินน่ะนะ"

scene ev emi_sleep_weep
with dissolve

# "Emi whimpers weakly through her dream, and her grip suddenly tightens again."
"เอมิสะอื้นเบา ๆ ตอนหลับอยู่ และอยู่ ๆ เธอก็กอดฉันแน่นขึ้น"

# "For the first time since I've known her, I see tears running down Emi's face."
"เป็นครั้งแรกนับตั้งแต่ที่ได้รู้จักกันมาที่ฉันได้เห็นน้ำตาของเอมิ"

# "It feels like my heart is about to break."
"เหมือนใจจะสลายเลย"

# "I instinctively tighten my own grip and stroke her hair in what I hope is a soothing manner."
"ฉันกอดเอมิแน่นขึ้นไปโดยอัตโนมัติพลางลูบผมด้วยหวังว่าจะช่วยปลอบได้"

# "Words of comfort, meaningless in this situation, spring to mind."
"ฉันนึกถึงคำพูดปลอบที่น่าจะใช้อะไรไม่ได้กับสถานการณ์ในตอนนี้"

# "Maybe I should wake her. Are you supposed to wake people having nightmares?"
"หรือจะปลุกเอมิดี เราควรปลุกคนที่กำลังฝันร้ายอยู่หรือเปล่า"

# "I can't for the life of me remember."
"นึกให้ตายยังไงก็นึกไม่ออกว่าควรไหม"

# "The decision is taken from me as Emi suddenly jerks awake with a cry."
"ฉันไม่อาจเลือกอย่างไหนได้อีกต่อไปเมื่ออยู่ ๆ เอมิก็สะดุ้งตื่นขึ้นพร้อมเสียงร้อง"

scene ev emi_sleep_cry
with dissolve

# emi "Dad!"
emi "พ่อ!"

# "This is… more than I think I want to hear without her knowing. I quickly sit upright and gently shake her shoulder to stir her."
"ฉันว่า… น่าจะมาได้ยินอะไรเกินกว่าที่ฉันจะอยากได้ยินโดยที่เอมิไม่รู้ตัวแล้วละ ฉันนั่งหลังตรงทันทีแล้วเขย่าไหล่\nปลุกเธอเบา ๆ"

scene bg school_dormemi_ni
with locationchange

# hi "Hey, you okay?"
hi "นี่ เป็นอะไรหรือเปล่า"

# "What a silly question."
"ถามอะไรแปลก ๆ"

show emi basic_shock_gym_close_ni at tworight
with charaenter

# emi "Huh? What?"
emi "ฮะ? อะไร"

show emi basic_hes_gym_close_ni
with charachange

# emi "Hisao?"
emi "ฮิซาโอะ?"

# "She shakes her head as if to clear it and quickly wipes her eyes."
"เอมิสั่นหัวให้สมองปลอดโปร่งขึ้นแล้วรีบเช็ดตาตัวเอง"

# hi "You had a nightmare. I think."
hi "เธอฝันร้าย หรือเปล่า"

show emi sad_shy_gym_close_ni
with charachange

# "Emi shudders again and glances up at me a little cautiously, as if unsure whether or not she's actually up."
"เอมิสะดุ้งอีกรอบแล้วเหลือบมองฉันอย่างระแวดระวังเหมือนไม่แน่ใจว่าตัวเองตื่นแล้วจริง ๆ"

# emi "Y-yeah, I guess so."
emi "อะ อื้ม มั้งนะ"

# hi "You wanna talk about it?"
hi "อยากเล่ามั้ย"

# emi "Hmm?"
emi "หืม"

# "A speedy internal debate seems to be going on in her head, which resolves itself with a shrug."
"เหมือนเอมิกำลังเถียงกับตัวเองอยู่ในหัวแบบเร็ว ๆ ซึ่งลงเอยด้วยการยักไหล่"

show emi basic_hes_gym_close_ni
with charachange

# emi "Nah, I don't really remember much of it."
emi "ไม่อะ ฉันก็จำไม่ค่อยได้"

# "I'm pretty sure she's lying to me, but somehow I don't think I should press the issue."
"ฉันมั่นใจว่าเอมิโกหกฉันอยู่ แต่ก็รู้สึกว่าไม่ควรไปซักไซ้อะไรต่อ"

show emi sad_shyblush_gym_close_ni
with charachange

# "Emi shudders again and turns toward me, looking a little sheepish."
"เอมิสะดุ้งอีกรอบแล้วหันมาทางฉันพร้อมทำหน้าแหย ๆ"

# emi "Sorry for falling asleep on you like that."
emi "ขอโทษที่หลับใส่นายแบบนั้นนะ"

# "I keep my voice as soothing as I can."
"ฉันรักษาน้ำเสียงให้นุ่มนวลที่สุดเท่าที่จะทำได้"

# hi "Hey, don't worry about it. You've been ill."
hi "น่า ไม่ต้องไปคิดมาก เธอไม่สบายนี่"

# emi "Yeah, I guess that cold medicine's just made me a little drowsy."
emi "อื้ม ที่ง่วง ๆ ก็น่าจะเพราะยาแก้หวัดนั่นแหละ"

# hi "I guess so."
hi "คงงั้น"

# "Emi does not strike me as the sort of person who'd fall asleep at the drop of a hat."
"เอมิเหมือนไม่ใช่คนที่จะผล็อยหลับไปง่าย ๆ อย่างนั้นเลย"

# "Rin, maybe. But Emi's far too energetic."
"ถ้ารินอาจจะใช่ แต่เอมิแรงเยอะเกินกว่าจะเป็นอย่างนั้นได้"

show emi basic_grin_gym_close_ni
with charachange

# "Emi gives a half-smile at my response, and then just like that she's back to her old self."
"เอมิยิ้มบาง ๆ ให้กับคำตอบฉัน และเธอก็กลับไปเป็นตัวเธอคนเดิมทันที"

show emi basic_closedgrin_gym_close_ni
with charachange

# emi "Well, prepare yourself for tomorrow morning Hisao!"
emi "นั่นแหละ เตรียมใจไว้สำหรับพรุ่งนี้เช้าด้วยฮิซาโอะ!"

show emi excited_proud_gym_close_ni
with charachange

# emi "We'll have to go twice as hard to make up for today!"
emi "เราต้องวิ่งกันเป็นสองเท่าเพื่อชดเชยวันนี้!"

# hi "But I went running this morning!"
hi "แต่เช้านี้ฉันไปวิ่งแล้วนะ!"

show emi basic_annoyed_gym_close_ni
with charachange

# emi "No excuse!"
emi "ไม่มีข้อแม้!"

# hi "Oh fine, I'll be ready for you!"
hi "เอ้อ เอาเถอะ จะเตรียมตัวคอยเธอแล้วกัน!"

show emi basic_grin_gym_close_ni
with charachange

# "Emi nods, satisfied."
"เอมิพยักหน้าพอใจ"

# emi "Good."
emi "ดี"

# "I take this as my cue to exit."
"ฉันถือจังหวะนี้ขอตัว"

# hi "Well, I'd better get going. Especially if I want to get enough sleep for tomorrow."
hi "โอเค งั้นไปละ ต้องนอนออมแรงให้พอสำหรับวิ่งพรุ่งนี้"

show emi basic_grin_gym_ni
with vpunch

# "I hop off the bed and head for the door."
"ฉันโดดออกจากเตียงแล้วเดินไปที่ประตู"

show emi sad_shy_gym_ni
with charachange

# emi "Hey, Hisao…"
emi "นี่ ฮิซาโอะ…"

# hi "Hmm?"
hi "หืม"

# "I pivot neatly on my heel and face Emi."
"ฉันหมุนส้นเท้าแล้วหันไปทางเอมิ"

show emi basic_hes_gym_ni
with charachange

# "She opens her mouth to say something, and then in another first, I see her falter slightly."
"เอมิอ้าปากจะพูดอะไรบางอย่าง และเห็นว่าเอมิชะงักไปเล็กน้อยเมื่อทำแบบนั้นอีกรอบ"

# "She closes her mouth and opens it again."
"เธอปิดปากแล้วเปิดออกอีกรอบ"

show emi sad_grin_gym_ni
with charachange

# emi "…Thanks."
emi "…ขอบคุณนะ"

# emi "For dropping by, I mean."
emi "ที่แวะมาหาน่ะ"

# emi "You're kind of the first visitor I've ever had who wasn't Rin."
emi "นายเป็นคนแรก ๆ นอกจากรินเลยนะที่แวะมาหาฉัน"

# "Now that's surprising. I would figure that Emi'd have people dropping by all the time."
"ฉันแปลกใจไปเพรราะคิดว่าเอมิคงต้องมีคนแวะมาหาไม่ขาดสาย"

# "She's certainly popular enough, or so I thought. Always talking to people in the hallways."
"เอมิก็เป็นที่รู้จักขนาดนั้น คิดว่านะ เห็นคุยกับคนตามโถงทางเดินตลอด"

show emi sad_shy_gym_ni
with charachange

# "Emi hesitates again."
"เอมิลังเลอีกรอบ"

# emi "And thanks for staying around after I… well."
emi "แล้วก็ขอบคุณนะที่อยู่ด้วยหลังจากที่ฉัน… อืม"

show emi sad_depressed_gym_ni
with charachange

# "A look of pain flits across her face."
"สีหน้าเธอดูเจ็บปวดอยู่แวบหนึ่ง"

# emi "You know."
emi "นั่นแหละ"

show emi sad_grin_gym_ni
with charachange

# emi "It helped."
emi "ขอบคุณนะ"

show emi basic_closedgrin_gym_ni
with charachange

# "She brightens back up and waves cheerily at me."
"เอมิกลับมายิ้มอีกครั้งแล้วโบกมือให้อย่างร่าเริง"

# emi "See you tomorrow!"
emi "เจอกันพรุ่งนี้!"

# hi "Yeah, see you later."
hi "อื้ม เจอกัน"

# "I'm just about to exit the door when something makes me turn around again."
"ฉันกำลังจะออกประตูไป ทว่าก็นึกบางอย่างได้จนต้องหันไปอีกรอบ"

# hi "Hey, Emi."
hi "นี่ เอมิ"

show emi basic_grin_gym_ni
with charachange

# emi "Hmm?"
emi "หืม"

# hi "Anytime you need to talk, let me know, okay?"
hi "ถ้าอยากคุยเมื่อไหร่ก็บอกฉันได้เสมอเลยนะ"

show emi sad_shy_gym_ni
with charachange

# "Emi seems taken aback by this offer."
"เอมิดูตกใจกับข้อเสนอนี้"

show emi basic_closedgrin_gym_ni
with charachange

# "Her grin gets even wider."
"เธอฉีกยิ้มกว้างขึ้นอีก"

# emi "Sure thing, Hisao."
emi "ได้เลยฮิซาโอะ"

show emi basic_grin_gym_ni
with charachange

# emi "See you in the morning!"
emi "เจอกันตอนเช้านะ!"

scene bg school_girlsdormhall_ni
with locationchange

# "I exit Emi's room with my head in a whirl."
"ฉันออกห้องเอมิมาทั้งที่ในหัวยังปั่นป่วน"

# "Should I have even left?"
"ฉันควรออกมาแล้วเหรอ"

# "Was she really okay?"
"เอมิจะไม่เป็นอะไรจริง ๆ เหรอ"

# "I want to turn around and march back down the hallway, open the door and tell her…"
"อยากจะหันกลับแล้วเดินไปตามโถงทางเดิน ไปเปิดประตูห้องแล้วบอกเอมิว่า…"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide

nvl clear

nvl show dissolve

# n "\n\nTell her I love her, tell her I think she's beautiful, tell her that I'll be there when she needs me."
n "\n\nบอกเอมิว่าฉันรักเธอ บอกเอมิว่าเธอนั้นสวยในสายตาฉัน บอกเอมิว่าฉันจะคอยอยู่เคียงข้างยามเธอต้องการ"

# n "I want to stay with her, to hold her close as she falls back to sleep."
n "ฉันอยากอยู่กับเธอ อยากกอดเธอแล้วปล่อยให้หลับไป"

# n "How many nights has she woken up like that?"
n "เธอต้องตื่นมาแบบนั้นกี่คืนแล้ว"

# n "Only to find that nobody's there."
n "ตื่นมาไม่พบใครเคียงข้าง"

# n "I want to be that person she can be with when that happens."
n "ฉันอยากจะเป็นคนที่คอยอยู่กับเธอทุกครั้งที่เกิดเรื่องนั้น"

# n "It's a silly thought, I know."
n "ฉันรู้ว่าเป็นความคิดที่งี่เง่าเหลือเกิน"

# n "We don't know each other that well, do we?"
n "เราก็ไม่ได้รู้จักกันดีขนาดนั้นนี่"

# n "The whole idea, while exhilarating, also makes me feel worry."
n "ถึงจะเป็นความคิดที่ชวนให้ตื่นเต้น แต่ก็ทำให้ฉันกังวล"

# n "Worry, perhaps, that I'd overstep my bounds."
n "กังวล ว่าอาจจะเป็นการล้ำเส้นตัวเอง"

# n "And now to add to my troubles, it seems as if Emi herself already has an interest in someone else."
n "แล้วตอนนี้เรื่องยิ่งยุ่งไปใหญ่เพราะเหมือนเอมิจะมีคนอื่นที่สนใจอยู่แล้ว"

nvl clear

# n "\n\n\n\n\n\nThis track captain of hers who seems so interested in her well-being."
n "\n\n\n\n\n\nหัวหน้าทีมคนนี้ที่ดูจะสนใจความเป็นอยู่ของเอมิ"

# n "True, I've only seen the two of them together a few times, but that doesn't change the fact that they seem better suited to one another."
n "จริงอยู่ว่าฉันเพิ่งเห็นสองคนนั้นอยู่ด้วยกันไม่กี่ครั้ง แต่ทั้งสองคนก็ดูเหมาะสมกันดีมาก"

# n "There's really nothing to be done about that."
n "ซึ่งฉันก็ทำอะไรไม่ได้"

# n "I need to take my mind off of this whole situation."
n "ฉันต้องเลิกคิดเรื่องพวกนี้เสียที"

$ renpy.music.set_volume(1.0, 2.0, channel="music")

nvl clear

nvl hide dissolve

window show

# "I've got homework to do."
"ฉันต้องทำการบ้าน"

# "Maybe that will distract me."
"ทำแล้วฉันอาจจะเลิกคิดไปก็ได้"

stop music fadeout 2.0

$ suppress_window_after_timeskip = True

scene black
with dissolve

########################################################
label th_E14:

window hide None

scene black
with dissolve

scene bg school_dormhisao
with openeye

window show

# "A night of restlessness has left me feeling fairly groggy this morning."
"ฉันตื่นมาด้วยความครั่นเนื้อครั่นตัวเพราะเมื่อคืนแทบไม่ได้นอนเลย"

play music music_drama fadein 8.0

# "The events of the previous day keep intruding upon my mind."
"เหตุการณ์จากวันที่ผ่านมายังวนเวียนอยู่ในหัว"

# "The memory of how Emi felt against me."
"ความทรงจำจากสัมผัสของเอมิ"

# "The memory of our wrestling match."
"ความทรงจำจากการเล่นมวยปล้ำของเรา"

# "And most bothersome, the memory of her nightmare."
"และที่กวนใจที่สุดคือความทรงจำจากฝันร้ายของเอมิ"

# "She was in so much pain."
"เอมิเจ็บปวดเหลือเกิน"

# "I can't stop wondering what it must be like for her to wake up with nobody there."
"ฉันอดสงสัยไม่ได้ว่าเธอจะรู้สึกยังไงถ้าตื่นมาโดยไม่มีใครเคียงข้างเลย"

scene bg school_dormbathroom
show steam
with locationskip

play ambient sfx_shower fadein 1.0

# "The shower shocks me awake with hot water. Awake, but still worried."
"น้ำร้อนจากฝักบัวปลุกฉันให้ตื่น ตื่น แต่ก็ยังเป็นห่วง"

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")
$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide

nvl show dissolve

nvl clear

# n "\nWhat will happen today?"
n "\nวันนี้จะเกิดอะไรขึ้น"

# n "Will things just go back to normal?"
n "ทุกอย่างจะกลับไปเป็นตามปกติหรือเปล่า"

# n "End of the episode, back to the status quo?"
n "จบสิ้นไปอย่างนั้น กลับไปเป็นสถานะเดิม?"

# n "There was a connection yesterday. Something that nearly pushed us past the boundaries of normal friendship."
n "เมื่อวานเกิดสายสัมพันธ์ขึ้น บางอย่างที่เกือบจะทำให้เราล้ำเส้นขอบเขตคำว่าเพื่อน"

# n "Would that have been so bad?"
n "ถ้าเป็นอย่างนั้นแล้วจะแย่ขนาดนั้นเลยเหรอ"

# n "My mind goes back to the look in Emi's eyes after our pillowfight. It almost seemed like she was daring me to go on."
n "ฉันย้อนนึกไปถึงแววตาที่เอมิส่งมาหลังจากศึกปาหมอนของเรา ดูคล้ายว่าเธอท้าให้ฉันเดินหน้าต่ออีก"

# n "Almost."
n "คล้าย"

# n "But I can't know for sure."
n "แต่ฉันก็ไม่แน่ใจนัก"

# n "Anyway, the track captain's probably first in her affections."
n "แต่เอาเถอะ หัวหน้าทีมคนนั้นคงจะเป็นคนที่เธอชอบเป็นอันดับหนึ่ง"

# n "But even as I say that, my mind is already snorting derisively. I'm just looking for an excuse. A reason for everything to go wrong."
n "ทั้งที่คิดอย่างนั้น ในใจฉันก็นึกแค่นหัวเราะเย้ยหยัน ฉันก็แค่หาข้ออ้าง หาสาเหตุที่จะทำให้ทุกอย่างพังทลายลง"

# n "A reason to not try."
n "หาเหตุผลที่จะได้ไม่ต้องไปเสี่ยง"

nvl clear

# n "\n\n\n\nIt's not as if I've even seen the two of them together outside of track practice."
n "\n\n\n\nฉันก็ไม่เคยเห็นสองคนนั้นอยู่ด้วยกันนอกเวลาซ้อมกีฬาด้วยซ้ำ"

# n "And clearly he's never visited. Emi said as much herself. If they were close, surely he'd visit."
n "แล้วก็ชัดว่าเขาไม่ได้มาเยี่ยมหาเอมิด้วยเพราะเธอบอกเอง ถ้าสนิทกันจริงอย่างไรก็ต้องมา"

# n "I'm such a wuss."
n "ฉันมันไก่อ่อน"

# n "I ought to just go for it anyway, damn the consequences."
n "ก็ลอง ๆ ไปเลยสิ ช่างหัวผลที่ตามมาแม่ง"

# n "That's what Emi would do, I think. Hell, I {b}know{/b} that's what she'd do."
n "เอมิก็คงทำอย่างนั้นเหมือนกัน คิดว่า ไม่สิ {b}รู้{/b}เลยแหละว่าเอมิต้องทำอย่างนั้น"

# n "Which is partially why I'm convinced there's no interest on her end. She hasn't acted either."
n "ซึ่งก็เป็นส่วนหนึ่งที่ทำให้ฉันเชื่อได้ว่าเอมิไม่ได้สนใจอะไรฉัน เพราะเธอก็ไม่ได้เดินเกมอะไรเลย"

# n "Maybe because of this track captain. It's possible she's got a bit of an unrequited crush thing going on."
n "อาจจะเพราะหัวหน้าทีมคนนี้ เป็นไปได้ว่าเอมิอาจจะแอบรักเขาข้างเดียวอยู่"

nvl clear

# n "\n\n\n\n\n\nBut who would be able to clarify their relationship?"
n "\n\n\n\n\n\nแต่ใครจะช่วยยืนยันความสัมพันธ์ของสองคนนี้ให้ได้"

# n "It sure as hell can't be Emi. She'd probably just laugh and ask why I wanted to know… and I'm not ready to answer that yet."
n "ยังไงก็ไม่ใช่เอมิแน่ ๆ แล้ว คงจะหัวเราะแล้วถามว่าจะอยากรู้ไปทำไม… ซึ่งฉันยังไม่พร้อมตอบว่าทำไม"

# n "Rin… Rin would probably just give me some cryptic answer or something. And then with my luck, she'd just ask Emi, who would ask me why I wanted to know, and I've already covered that problem."
n "ริน… รินคงจะให้คำตอบลึกลับเป็นปริศนาอะไรประมาณนั้น แล้วยิ่งฉันเป็นคนดวงไม่ดีแบบนี้ รินคงจะเอาไปถามเอมิต่อ\nแล้วเอมิก็จะถามว่าจะอยากรู้ไปทำไม ซึ่งฉันพูดถึงปัญหาข้อนี้ไปแล้ว"

# n "I wonder…"
n "หรือว่า…"

nvl clear

# n "\n\n\n\n\nCould I get away with asking the nurse? He seems pretty protective of Emi. I'm sure he'd know if something was up…"
n "\n\n\n\n\nถามคุณพยาบาลได้หรือเปล่า เห็นใส่ใจเอมิขนาดนั้นยังไงก็ต้องรู้ถ้ามีเรื่องอะไรจริง ๆ …"

# n "And he owes me for not letting Emi know he forgot to tell me about her being ill, so he'll keep quiet."
n "แล้วคุณพยาบาลก็ติดหนี้ฉันค่าปิดปากที่ลืมบอกฉันว่าเอมิไม่สบายด้วย ถ้าฉันถามแล้วก็น่าจะไม่เอาไปบอกต่อ"

# n "What if he asks me why I want to know, though?"
n "แต่ถ้าเกิดคุณพยาบาลถามฉันว่าจะอยากรู้ไปทำไมล่ะ"

# n "I can shake him off. Just say I'm curious as a friend. He'll buy that, won't he?"
n "ก็ปฏิเสธไปได้อยู่ แค่บอกว่าเป็นเพื่อนกันเลยอยากรู้ คุณพยาบาลคงจะเชื่อ ใช่มั้ย"

# n "Of course!"
n "เชื่อสิ!"

# n "That's settled, then."
n "ตามนี้แล้วกัน"

# n "After the run, I'll talk to him while Emi's waiting outside the office."
n "พอวิ่งเสร็จแล้วฉันจะไปคุยกับคุณพยาบาลตอนที่เอมิรออยู่นอกห้อง"

stop ambient fadeout 2.0

nvl clear

nvl hide dissolve

scene bg school_track
with locationskip

nvl show dissolve

# n "\n\n\n\nThere's no sign of Emi when I arrive at the track. Is she still too ill?"
n "\n\n\n\nพอมาถึงที่ลู่แล้วก็ไม่มีวี่แววเอมิเลย ยังป่วยอยู่เหรอ"

# n "I decide to give her ten minutes."
n "ฉันให้เวลารอเอมิสิบนาที"

# n "I'm a little early, and she was ill yesterday, so if she takes a while to show up it shouldn't be surprising."
n "ฉันมาเช้าไปหน่อย แถมเมื่อวานเอมิก็ป่วยด้วย จะมาช้าหน่อยคงไม่แปลก"

# n "Still, I'd hate to just waste my time, so I occupy myself by stretching and pacing back and forth anxiously."
n "แต่ก็ไม่อยากอยู่เฉย ๆ ให้เสียเวลา ฉันจึงยืดเส้นยืดสายแล้วเดินหน้าเดินถอยอย่างกระวนกระวายใจ"

# n "What if I went too far yesterday?"
n "ถ้าเกิดเมื่อวานฉันทำเกินไปล่ะ"

# n "What if she doesn't come because she's embarrassed?"
n "ถ้าเกิดเอมิไม่มาเพราะเขินล่ะ"

# n "What if…"
n "ถ้าเกิด…"

$ renpy.music.set_volume(1.0, 2.0, channel="music")
$ renpy.music.set_volume(1.0, 2.0, channel="ambient")

nvl clear

stop music fadeout 2.0

nvl hide dissolve

window show

show emi basic_closedgrin_gym at center
with charaenter

# emi "You're early again, Hisao!"
emi "มาเช้าอีกแล้วนะฮิซาโอะ!"

show emi excited_proud_gym
with charachange

# emi "I'm impressed!"
emi "ทึ่งจริง ๆ !"

# "Just like that, I feel some of the tension leaving my body."
"แล้วความเกร็งทั้งตัวก็หายไปง่ายดายเช่นนั้น"

# "Emi seems to be bright and cheerful as usual, with no sign that she even was ill the other day, much less had a less-than-restful sleep."
"เอมิดูสดใสร่าเริงอย่างปกติโดยไม่ออกอาการเลยว่าเมื่อวานไม่สบาย ไม่มีท่าทีเลยด้วยซ้ำว่าเมื่อคืนนอนไม่พอ"

# "Still, I have to ask."
"แต่ก็ต้องถามอยู่ดี"

# hi "Sleep well last night?"
hi "เมื่อคืนหลับสบายมั้ย"

play music music_serene

# "It's just a throwaway question. Small talk."
"เป็นแค่การถามหาเรื่องคุยไปเรื่อยเปื่อย"

# "The sort of thing people ask someone they bump into in the café while getting their morning coffee."
"เป็นคำถามที่ถ้าคนเจอกันที่คาเฟตอนไปซื้อกาแฟยามเช้าจะถามกัน"

# "But not for us. At least, not for me."
"แต่ไม่ใช่สำหรับเรา ไม่ใช่สำหรับฉันแล้วแน่ ๆ ละ"

# "I don't know if Emi realizes that I'm actually concerned about how well she slept last night, but the question does give her pause."
"ฉันไม่รู้ว่าเอมิรู้ตัวหรือเปล่าว่าที่ถามคือเป็นห่วงจริง ๆ กับการนอนหลับเมื่อคืน แต่เธอก็เว้นช่วงเงียบไปกับคำถามนี้"

show emi basic_grin_gym
with charachange

# "After a short moment of what seems like her genuinely pondering this, she nods."
"พอเอมิทำท่าเหมือนครุ่นคิดอยู่จริง ๆ พักหนึ่งแล้วก็พยักหน้า"

show emi basic_closedhappy_gym
with charachange

# emi "Yep! Sure did!"
emi "อื้ม! หลับสบายมาก!"

# "Was it because of me?"
"เพราะฉันหรือเปล่า"

# "Did I actually help?"
"ฉันได้ช่วยให้เอมิหลับสบายจริง ๆ มั้ย"

# "Or are you just saying that to get me to stop asking questions?"
"หรือแค่ตอบเพราะไม่อยากให้ฉันไม่ต้องถามอะไรต่อ"

# hi "Good to hear."
hi "ก็ดีแล้ว"

show emi basic_closedgrin_gym
with charachange

# "Emi grins and begins warming up."
"เอมิยิ้มแล้วเริ่มวอร์มอัพ"

show emi basic_grin_gym
with charachange

# emi "So, ready to begin?"
emi "พร้อมเริ่มหรือยัง"

# hi "Pfft, am I ready? Of course I'm ready! I was born ready!"
hi "เหอะ พร้อมหรือยังเหรอ พร้อมอยู่แล้วสิ! พร้อมตั้งแต่เกิดแล้ว!"

show emi basic_closedhappy_gym
with charachange

# "Emi laughs at my bravado, and we take off running."
"เอมิหัวเราะที่ฉันพูดออกความมั่นใจไปแบบนั้น เราออกวิ่งด้วยกัน"

scene bg school_track_running
with shorttimeskip

# "I keep a steady pace the whole time, breathing steadily."
"ฉันคอยรักษาฝีเท้ากับจังหวะการหายใจให้คงที่"

scene bg school_track_on
with Dissolve(2.0)

# "I still feel dead at the end, but at least I don't gasp like a fish out of water now."
"ตอนวิ่งเสร็จแล้วก็ยังเหนื่อยอยู่ แต่อย่างน้อยก็ไม่ได้หอบเหมือนปลาขาดน้ำแล้วอะนะ"

show emi basic_happy_gym:
    center
    xpos 0.6
    easein 0.5 center
with charaenter

# "Emi is positively beaming after the run today."
"พอวิ่งรอบเช้าวันนี้เสร็จเอมิก็ยิ้มแฉ่ง"

# emi "Nice job, Hisao! You're improving!"
emi "เก่งมากฮิซาโอะ! พัฒนาขึ้นเรื่อย ๆ เลย!"

show emi basic_closedgrin_gym
with charachange

# emi "You'll be half as fast as me in no time!"
emi "เดี๋ยวเดียวก็เร็วได้ครึ่งหนึ่งฉันแล้วละ!"

# "This last line is delivered with a teasing grin that I've grown all too used to."
"ประโยคหลังนั้นมาพร้อมกับรอยยิ้มหยอกที่ฉันชินไปเสียแล้ว"

# hi "Oh, how exciting."
hi "โห ตื่นเต้นจัง"

play ambient sfx_emisprinting

$ renpy.music.set_volume(0.3,1.0,channel="ambient")

hide emi
with easeoutleft

# "Emi begins to run her sprints while I take a cool-down lap."
"เอมิออกวิ่งเร็วระหว่างที่ฉันกำลังเดินคูลดาวน์"

# "She's really pushing herself today."
"วันนี้เอมิทุ่มแรงจริง ๆ"

stop ambient fadeout 1.0

scene bg school_track
with shorttimeskip

$ renpy.music.set_volume(1.0,0.0,channel="ambient")

# "By the time I'm done with my lap, she's laying across one of the bleachers, looking exhausted."
"เมื่อฉันเดินเสร็จแล้วเอมิก็นอนอยู่บนสแตนด์เชียร์ดูอ่อนล้า"

# hi "Goodness, not pushing it a little too much today, are you?"
hi "ให้ตาย วันนี้เธอฝืนไปหน่อยมั้ยเนี่ย"

# hi "You did just have a cold, you'll recall."
hi "จำได้ใช่มั้ยว่าเธอเพิ่งหายหวัดมาเนี่ย"

show emi basic_annoyed_gym at center
with charaenter

# "Emi gives an annoyed snort and sits up."
"เอมิหัวเราะหึเหมือนหงุดหงิดแล้วลุกขึ้นนั่ง"

# emi "Bah! I'm just trying to make up for lost time, that's all."
emi "ฮึ! ก็แค่วิ่งชดเชยที่ไม่ได้มาวิ่งแค่นั้นเอง"

show emi excited_happy_gym
with charachange

# emi "I went twice as hard today, you know."
emi "วันนี้ฉันวิ่งทบเป็นสองเท่าเลยนะ"

show emi excited_laugh_gym
with charachange

# emi "A good run always gets the kinks out, you know."
emi "วิ่งสักหน่อยแล้วมันก็สบายตัวขึ้น"

show emi basic_closedgrin_gym
with charachange

# emi "Clears the mind, too."
emi "วิ่งให้สมองมันปลอดโปร่งด้วย"

# hi "Oh?"
hi "หืม"

show emi excited_happy_gym
with charachange

# "Emi nods vigorously."
"เอมิพยักหน้าหงึก ๆ"

show emi excited_amused_gym
with charachange

# emi "Yep! It's a great outlet for that sort of thing."
emi "ใช่! เป็นกิจกรรมระบายความเครียดอะไรประมาณนั้น"

# "She does not explain further, and I don't ask."
"เอมิไม่ขยายความต่อ และฉันก็ไม่ถามอีก"

# "I suspect I know the real reason she went so hard today."
"ฉันว่าฉันรู้ว่าทำไมวันนี้เอมิถึงวิ่งให้หนักขึ้น"

# "Being sick had nothing to do with it. Something's bothering her."
"ไม่เกี่ยวกับที่ไม่สบาย มีเรื่องบางอย่างที่กวนใจเอมิอยู่"

# "Maybe the nightmare. Maybe something else."
"อาจจะฝันร้าย อาจจะอะไรอย่างอื่น"

# "But it's not my place to pry."
"แต่ก็ไม่ใช่กงการอะไรของฉัน"

# "She'd tell me if she wanted me to know."
"ถ้าอยากให้รู้เอมิก็คงบอกเอง"

# hi "I'm sure that comes in handy."
hi "มีประโยชน์น่าดูเลย"

show emi basic_grin_gym
with charachange

# emi "You have no idea."
emi "มีชนิดที่ว่านายคิดไม่ถึงเลยแหละ"

# "The sincerity in her voice confirms my suspicion."
"น้ำเสียงจริงใจนั้นยืนยันในสิ่งที่ฉันสงสัยอยู่"

# "The only problem is…"
"ปัญหาเดียวคือ…"

# "Even though I know she'd tell me if she wanted me to know, I still want to know."
"ทั้งที่รู้ว่าถ้าเอมิอยากให้รู้เธอก็คงบอกเอง แต่ฉันก็อยากรู้อยู่ดี"

# hi "Something on your mind, then?"
hi "มีอะไรกวนใจเธออยู่งั้นเหรอ"

# "Emi doesn't seem surprised by my question."
"เอมิดูไม่แปลกใจเลยที่ฉันถามแบบนี้"

show emi basic_closedgrin_gym
with charachange

# "Instead, she shrugs."
"เธอกลับยักไหล่"

show emi sad_grin_gym
with charachange

# emi "Nah, it's nothing worth getting worried about."
emi "ไม่อะ ไม่มีอะไรให้ต้องคิดมาก"

# "She seems as if she's trying to convince herself as much as she's convincing me."
"เป็นท่าทีที่เหมือนจะบอกคำพูดนั้นกับตัวเองไปด้วย"

# "I open my mouth to ask if yesterday is responsible for her current state of mind, but think better of it."
"ฉันอ้าปากหมายจะถามว่าที่ทำตัวอย่างนี้เพราะเรื่องเมื่อวานหรือเปล่า แต่ก็ตัดใจไม่ถาม"

# "Too much risk of her taking the question the wrong way."
"เพราะถามไปแล้วเสี่ยงมากที่เอมิจะเข้าใจผิด"

# "Besides, I'm not even sure myself what to think about yesterday."
"อีกอย่าง ฉันก็ไม่แน่ใจเหมือนกันว่าจะต้องมองเรื่องเมื่อวานยังไง"

# "Really I can only get about as far as how it felt to have Emi sleeping next to me before my brain shuts down."
"ที่ฉันจำได้จริง ๆ ก็มีแค่ความรู้สึกตอนมีเอมินอนอยู่ข้าง ๆ ก่อนที่สมองฉันจะดับไป"

# "Having her before me now, covered in sweat and looking wryly at me, she's making it difficult to think."
"พอเอมิมาอยู่ตรงหน้าส่งยิ้มแห้ง ๆ ให้พร้อมตัวที่เปียกเหงื่อนั้นแล้วฉันก็คิดอะไรไม่ค่อยออกเลย"

# hi "Yeah, I hear you."
hi "อืม โอเค"

show emi basic_hes_gym
with charachange

# emi "We'd better hurry to see the nurse. We're running short on time."
emi "รีบไปหาคุณพยาบาลกันได้แล้ว เหลือเวลาไม่มากแล้วนะ"

# hi "Aren't we always?"
hi "ก็เหลือไม่มากตลอดนี่"

show emi basic_grin_gym
with charachange

# "Emi laughs at this, a dry chuckle that seems most un-Emi-like."
"เอมิหัวเราะ เป็นเสียงหัวเราะแกน ๆ ที่ไม่สมเป็นเอมิเอามาก ๆ"

show emi sad_grin_gym
with charachange

# emi "Too true."
emi "จริงมาก ๆ"

# "For a brief moment, she looks old, worn down by some old hurt."
"แวบหนึ่งเอมิดูแก่ลงด้วยความเพลียจากแผลเก่า"

# "But just like yesterday I can almost see her shouldering the burden and straightening up slightly."
"แต่ก็เหมือนอย่างเมื่อวาน ฉันเกือบได้เห็นตัวตนเธอที่ต้องคอยแบกรับบางอย่างแล้วแต่เธอก็ยืดหลังตรงเล็กน้อย"

# "And then she's back to being Emi again."
"และกลับเป็นเอมิคนเดิม"

show emi excited_proud_gym
with charachange

# emi "Come on then Hisao. Race ya!"
emi "งั้นก็ไปกันฮิซาโอะ มาวิ่งแข่งกัน!"

play ambient sfx_emisprinting

hide emi
with easeoutleft

stop ambient fadeout 2.0

# "With a sudden smile, she darts off."
"อยู่ ๆ เอมิก็ยิ้มแล้วออกวิ่ง"

# hi "Hey! No fair!"
hi "เฮ้ย! ไม่ยุติธรรมนี่!"

# "I take off after her, knowing I won't catch her but not caring."
"ฉันวิ่งตามเอมิไปทั้งที่รู้ดีว่าคงไม่ทัน แต่ก็ไม่ได้สน"

# "Even if there's no chance of catching her, I'll still run after her."
"ต่อให้ไม่มีวันจะตามเอมิทัน ฉันก็จะยังวิ่งตามเธอ"

stop music fadeout 2.0

scene bg school_nursehall
show emi basic_grin_gym at center
with locationskip

# "Emi's waiting for me at the door as I arrive."
"พอไปถึงเอมิก็รออยู่ที่ประตูก่อนแล้ว"

show emi basic_closedhappy_gym
with charachange

# emi "Well well, look who's finally shown up!"
emi "แหม ๆ ดูซิใครมาเนี่ย!"

# hi "Yeah, yeah."
hi "เออ ๆ"

# hi "Enjoy your victory while you can."
hi "อย่าให้ถึงทีฉันบ้างก็แล้วกัน"

show emi basic_closedgrin_gym
with charachange

# "Emi grins as the nurse pokes his head out of the door."
"เอมิยิ้ม คุณพยาบาลโผล่หัวออกมาจากประตู"

show nurse neutral:
    center
    xpos 0.0 xanchor 0.5
    easein 0.5 xpos 0.1
with charaenter

# nk "Well, there you are."
nk "อะ มากันสักที"

# nk "Come on in, Hisao."
nk "เข้ามาเลยฮิซาโอะ"

play music music_nurse fadein 1.0

scene bg school_nurseoffice
show nurse neutral at center
with locationchange

# "In what has become a familiar routine by now, he checks my blood pressure and my heart rate."
"คุณพยาบาลตรวจความดันเลือดกับอัตราการเต้นของหัวใจฉัน ซึ่งก็ทำกันจนเป็นกิจวัตรอันคุ้นเคยแล้ว"

show nurse fabulous
with charachange

# nk "A bit fast today, isn't it?"
nk "วันนี้เร็วหน่อยนะ"

# hi "Yeah, I kind of raced Emi here."
hi "ครับ ผมวิ่งแข่งกับเอมิมา"

show nurse grin
with charachange

# "The nurse laughs."
"คุณพยาบาลหัวเราะ"

# nk "That's never a good idea!"
nk "คิดยังไงไปวิ่งแข่งกับเอมิเนี่ย!"

show nurse neutral_close
with characlose

# "He leans in to whisper to me in a conspiratory manner."
"คุณพยาบาลโน้มตัวมากระซิบเหมือนมีลับลมคมในอะไร"

show nurse fabulous_close
with characlose

# nk "I don't know if you've heard… but Emi's a bit of a track star."
nk "ไม่รู้ว่าเธอเคยได้ยินมาแล้วหรือยัง… แต่เอมิน่ะเขาเป็นดาวเด่นของทีมวิ่งเลยนะ"

show nurse fabulous
with vpunch

# "I reel back in mock surprise."
"ฉันผละตัวออกมาแสร้งทำท่าแปลกใจ"

# hi "Really? She never mentioned it before!"
hi "จริงเหรอครับ ไม่เห็นเอมิเคยพูดถึงเลย!"

show nurse grin
with charachange

# "The two of us share a laugh."
"เราสองคนหัวเราะกัน"

show nurse neutral
with charachange

# nk "Did she do okay today?"
nk "วันนี้เอมิหายหรือยัง"

# nk "Cold seemed to bother her?"
nk "มีอาการเป็นไข้อยู่ไหม"

# hi "Why don't you ask her?"
hi "ก็ไปถามเอมิเขาเองสิครับ"

show nurse concern
with charachange

# "He rolls his eyes in exasperation."
"คุณพยาบาลกลอกตาด้วยความระอา"

# nk "Of course I'm going to ask her too, but she'll tell me that she didn't have any problems, regardless of whether or not she did."
nk "ถามอยู่แล้ว แต่เดี๋ยวก็คงบอกว่าไม่มีปัญหาอะไรนั่นแหละ ต่อให้จะไม่มีจริง ๆ หรือมีก็เถอะ"

show nurse fabulous
with charachange

# nk "So I'm asking you, because you're her friend and would probably tell me if she had trouble today."
nk "ก็เลยมาถามเธอที่เป็นเพื่อนเอมิ เพราะถ้าวันนี้เอมิมีอาการอะไรเธอก็คงบอก"

# "When he puts it that way, it makes a lot more sense."
"พอพูดแบบนี้แล้วก็ฟังดูสมเหตุสมผลขึ้นมาเยอะเลย"

# hi "She seemed pretty good today, if a little more tired than usual."
hi "ก็ดูโอเคดีนะครับ อาจจะเพลีย ๆ หน่อย"

# hi "She was already feeling better when I dropped by yesterday, so I'm not that surprised."
hi "แต่ผมก็ไม่ได้แปลกใจขนาดนั้นเพราะตอนที่ไปเยี่ยมเมื่อวานเอมิเขาก็ค่อยยังชั่วแล้ว"

show nurse neutral
with charachange

# "The nurse nods, though I notice he tenses slightly when I mention yesterday's visit."
"คุณพยาบาลพยักหน้า แต่ก็เห็นว่าเขาเกร็งไปเล็กน้อยเมื่อฉันพูดถึงเรื่องที่ไปเยี่ยมเมื่อวาน"

# nk "Well, that's good to hear."
nk "งั้นก็ดีแล้วละ"

# nk "I figured it was just a 24-hour thing. Emi tends to recover quickly from colds and the like."
nk "ฉันก็เดาไว้ว่าคงเป็นไม่นานหรอก แค่วันเดียวงี้ เอมิเวลาเป็นหวัดหรืออะไรจะหายไวมาก"

# hi "Hey, speaking of Emi…"
hi "เอ้อ พูดถึงเอมิ…"

# hi "Are she and the track captain…? Well, you know."
hi "เอมิกับหัวหน้าทีมเขา… เอ่อ นั่นแหละครับ"

show nurse fabulous
with charachange

# "A look of suspicion crosses his face."
"คุณพยาบาลทำหน้าสงสัย"

# nk "Why do you ask?"
nk "ถามทำไมเหรอ"

# hi "Well, it's just that they seem kind of close, and I was just curious, you know?"
hi "ก็เห็นสองคนนั้นสนิท ๆ กัน แล้วผมก็อยากรู้ด้วย"

# hi "And I'd never ask her, because that would be kind of embarrassing."
hi "แต่จะให้ไปถามกับเอมิเลยผมก็อาย ๆ ผมคงไม่กล้าถามแน่"

# "So far, so good. Now to really sell it."
"ใช้ได้ ๆ แล้วก็ใส่ตรงนี้ไปให้ดูน่าเชื่อถือขึ้น"

# hi "Besides, I think they'd make a cute couple."
hi "อีกอย่าง ผมว่าถ้าสองคนนั้นเป็นแฟนกันคงน่ารักดี"

show nurse grin
with charachange

# "The nurse laughs."
"คุณพยาบาลหัวเราะ"

# nk "Well, I don't suppose you're the first to think that."
nk "อืม ก็ไม่ได้มีแค่เธอแหละนะที่คิดแบบนั้น"

# nk "But I think I can say with some certainty that the two of them will never do anything like that."
nk "แต่ฉันก็มั่นใจอยู่พอตัวเหมือนกันว่าระหว่างสองคนนั้นน่ะเป็นไปไม่ได้หรอกหรอก"

# hi "Certainty?"
hi "มั่นใจ?"

show nurse neutral
with charachange

# nk "Yep."
nk "ใช่"

show nurse fabulous
with charachange

# nk "Not that I could tell you, of course. Confidentiality and all that."
nk "แต่บอกไม่ได้หรอกนะ ต้องรักษาความลับอะไรแบบนั้นน่ะ"

# hi "Yeah right, you just like holding a secret over my head."
hi "ครับ ๆ คุณนี่ชอบกั๊กความลับกับผมจริงเลยนะ"

show nurse grin
with charachange

# nk "That too."
nk "อันนั้นก็ส่วนหนึ่ง"

show nurse neutral
with charachange

# nk "Right. Get out of here. I'm a busy man, you know."
nk "โอเค ออกไปได้แล้ว ฉันก็มีธุระของฉัน"

stop music fadeout 2.0

scene bg school_nursehall
show emi basic_grin_gym at center
with locationchange

# "I roll my eyes at his last statement and head out the door, motioning to Emi to go in."
"ฉันกลอกตากับประโยคสุดท้ายนั้นแล้วเดินออกประตูมาบุ้ยใบ้ให้เอมิเข้าไป"

show emi basic_grin_gym:
    center
    easeout 0.5 xpos 0.4 alpha 0.0
with Pause(0.5)

hide emi
with None

# "The whole time, I'm trying to keep from doing a celebratory dance."
"และระหว่างนั้นฉันก็ต้องห้ามใจตัวเองไม่ให้ลิงโลดไป"

window hide

play music music_running

# centered "The two of them will never do anything like that."
centered "ระหว่างสองคนนั้นน่ะเป็นไปไม่ได้หรอกหรอก"

window show

# "That's precisely the sort of thing I wanted to hear."
"นี่แหละที่อยากได้ยิน"

# "I'm half-tempted to make some sort of a move on Emi right now, but I think the nurse would probably disapprove."
"ชักอยากเดินหน้ากับเอมิต่อแล้ว แต่ฉันว่าคุณพยาบาลคงไม่เห็นด้วยสักเท่าไหร่"

# "Besides, I still don't know exactly how Emi feels about me."
"อีกอย่าง ฉันก็ไม่รู้แน่ชัดว่าเอมิคิดยังไงกับฉัน"

# "I mean it's obvious that she cares about me as a friend, but something more than that? I can't be certain."
"ก็ชัดแหละว่าเป็นห่วงในฐานะเพื่อน แต่จะมากกว่านั้นหรือเปล่าฉันไม่แน่ใจ"

# "Even so, I can't help but feel hopeful. I just need to figure out a good time to tell Emi exactly how I feel."
"ถึงอย่างนั้นฉันก็อดตั้งความหวังไม่ได้ ที่เหลือก็แค่หาจังหวะดี ๆ บอกความรู้สึกให้เอมิได้รู้"

# "That puzzle should keep me occupied for the rest of the day, at least."
"อย่างน้อยปัญหาข้อนั้นก็คงทำให้สมองได้คิดอะไรบ้างตลอดทั้งวันนี้"

stop music fadeout 6.0

########################################################
label th_E15:

scene bg school_nursehall
with None

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_rooftop fadein 1.0

scene bg school_roof
with shorttimeskip

# "The rooftop is completely deserted."
""

# "Normally I could count on Rin to be up here before me, but she's strangely absent."
""

# "I wonder if she decided to accompany Emi to the cafeteria for once. That seems pretty unlikely, but it's all I can think of right now."
""

# "Part of me wants to go look for Rin, but a far larger part of me is too pleased with the way the sun feels on my skin to care."
""

# "I pick idly at my lunch while I wait for Emi and Rin to show up."
""

# "It does not take long for me to hear the sounds of someone coming up the stairs."
""

$ renpy.music.set_volume(0.5, 0.0, channel="sound")
play sound sfx_door_creak

# "I wait until the door begins to open before talking."
""

# hi "Took you long enough."
hi ""

# hi "Keeping me waiting for you, honestly."
hi ""

# hi "The two of you are…"
hi ""

# hi "Huh?"
hi ""

# "Well that's odd."
""

show emi basic_confused at center
with charaenter

# "The only person standing in the doorway is Emi, who looks mildly confused."
""

# emi "What do you mean, “huh?”"
emi ""

show emi basic_grin
with charachange

# emi "It's me! You know, Emi! We run in the mornings."
emi ""

# "She grins, and I feel my heart jump slightly in my chest at the sight."
""

# hi "Yes, I knew that. I'm just confused…"
hi ""

# hi "…Where's Rin?"
hi ""

show emi sad_depressed
with charachange

# "Emi's grin is replaced by a rather guilty-looking expression."
""

# emi "Yeah, about that…"
emi ""

# emi "I kind of… sort of…"
emi ""

show emi sad_shy
with charachange

# emi "Gavehermycold."
emi ""

play music music_another fadein 0.5
$ renpy.music.set_volume(1.0, 0.0, channel="sound")

# hi "Oh dear."
hi ""

# hi "Am I at risk too?"
hi ""

# "It would make sense, after all. Emi and I were in close contact the other day…"
""

# "So what did she and Rin do that got her ill?"
""

# "…"
""

# "Steady on, old lad. Don't go down that road."
""

# "Rin's just probably got a worse immune system than me."
""

show emi basic_shock
with charachange

# "Emi seems shocked by my comment, like she hadn't considered that before."
""

# emi "I hope not!"
emi ""

show emi excited_sad
with charachange

# emi "I'll feel terrible if you get ill because of me, Hisao!"
emi ""

# hi "Oh man, I think I feel a fever coming on…"
hi ""

show emi sad_annoyed
with charachange

# "Emi looks horrified, and then quickly shifts into a more angry expression."
""

# emi "Hisao!"
emi ""

# emi "You stop getting sick this instant!"
emi ""

show emi basic_annoyed
with charachange

# emi "I won't have it!"
emi ""

show emi basic_annoyed_close
with vpunch

# "Impulsively she seizes me by the collar."
""

# emi "Are you listening to me, Hisao's immune system?"
emi ""

show emi sad_angry_close
with charachange

# emi "Get your ass in gear!"
emi ""

# "I give a smart salute."
""

# hi "Duly noted, ma'am."
hi ""

show emi basic_grin
with charadistant

# "Emi steps back and nods, satisfied."
""

show emi basic_closedgrin
with charadistant

# emi "Good."
emi ""

show emi basic_happy
with charadistant

# emi "You are not allowed to miss any of our morning runs, after all."
emi ""

# hi "But you missed a morning run!"
hi ""

show emi sad_annoyed
with charachange

# "Emi crosses her arms and looks at me haughtily."
""

# emi "Yes, but that's a special case. It was me, and not you."
emi ""

# hi "That's not an explanation at all."
hi ""

show emi basic_confused
with charachange

# "Emi looks flabbergasted."
""

# emi "You're kidding, right?"
emi ""

show emi basic_annoyed
with charachange

# emi "That explanation makes perfect sense!"
emi ""

# hi "No it doesn't! It's a blatant double standard!"
hi ""

show emi sad_annoyed
with charachange

# emi "I don't see what that has to do with anything."
emi ""

# hi "Oh, fine."
hi ""

show emi basic_closedgrin
with charachange

# "Emi seems pleased by her victory."
""

# hi "Anyway, is Rin going to be okay? She's not terribly ill, right?"
hi ""

show emi basic_grin
with charachange

# "Emi shakes her head."
""

# emi "Nope! She'll be fine."
emi ""

show emi excited_proud
with charachange

# emi "I got her some cold medicine that should help her."
emi ""

show emi basic_hes
with charachange

# emi "Although I probably should have made sure she didn't try to take them all at once…"
emi ""

show emi basic_grin
with charachange

# emi "She's done it before, you know."
emi ""

# "Somehow, I don't find this all that surprising."
""

# "I doubt Rin is one to pay attention to maximum dosages and such."
""

# hi "You should probably check in on her later, then. Just to make sure."
hi ""

show emi sad_grin
with charachange

# "Emi shrugs."
""

# emi "I'll stop by after practice. She'll be fine until then."
emi ""

# "I nod, figuring that line of conversation is over."
""

# "The only problem is, I don't know what else to talk about."
""

# hi "So…"
hi ""

# hi "You got any more track meets coming up?"
hi ""

window hide

nvl clear

nvl show dissolve

# n "\n\n\n\n\n\n\n\nThis is a terribly roundabout way of trying to see if she's free on the weekend."
n ""

# n "If she's free, then maybe I can ask her on a date or something."
n ""

# n "Well, assuming I can get myself to actually form the words."
n ""

nvl clear

nvl hide dissolve

window show

show emi basic_grin
with charachange

# "Emi shakes her head."
""

show emi basic_closedgrin
with charachange

# emi "Nah, not for another couple weeks, I think. The season's winding down."
emi ""

# "Oh yeah. I came in right in the middle of things, didn't I?"
""

# "Does that mean exams are coming up soon? I should probably look into that."
""

# hi "What do you do on weekends if there's not a meet?"
hi ""

show emi excited_proud
with charachange

# "An eyebrow goes up, and Emi gets a teasing look on her face."
""

# emi "You're awfully inquisitive today, aren't you?"
emi ""

# "I shrug and hope it looks casual."
""

# hi "Just making conversation."
hi ""

# hi "I don't know what it's like to be a track star, after all."
hi ""

show emi basic_closedgrin
with charachange

# emi "Pfft, flattery."
emi ""

# "She waves a hand idly."
""

show emi basic_grin
with charachange

# emi "I'm not actually that good, you know."
emi ""

show emi basic_closedhappy
with charachange

# emi "You just so happened to see me on a good day, is all."
emi ""

# hi "You liar."
hi ""

show emi sad_grin
with charachange

stop music fadeout 6.0

# emi "Heh, yeah."
emi ""

# emi "But humility is the sign of a good athlete."
emi ""

show emi sad_depressed
with charachange

# emi "At least that's what my dad used to say."
emi ""

# "She shrugs and tries unsuccessfully to hide the rather troubled expression her face has taken on."
""

# hi "Hey, what's up? You seem bothered by something."
hi ""

# "Emi starts to deny it, then sighs in defeat."
""

# "I wonder if she's too tired from being sick to get herself to deny it like usual."
""

# "Or if she actually just trusts me enough at this point to open up."
""

show emi sad_shy
with charachange

play music music_comfort fadein 9.0

# emi "Well, you remember last night?"
emi ""

# "Do I ever. I settle for nodding, however."
""

show emi sad_depressed
with charachange

# emi "That's not the first time that's happened to me."
emi ""

# emi "Actually, I get them kind of…"
emi ""

# "She pauses, as if it's suddenly occurred to her what she's doing."
""

# "It's almost like she's breaking some sort of personal rule, here."
""

# "But she starts up again, choosing her words carefully."
""

# emi "Well, not often, but…"
emi ""

show emi sad_shy
with charachange

# emi "On occasion."
emi ""

# emi "It's just been one of those weeks where that's what happens."
emi ""

show emi sad_depressed
with charachange

# "A sigh escapes her, and she looks terribly frustrated."
""

show emi sad_shy_close
with characlose

# "I reach over and give her a hug, which unlike last time doesn't seem to shock her."
""

# "Instead, she seems to relax as my arms wrap around her."
""

# "We stay that way for a while."
""

# hi "Hey, you know I was serious last night."
hi ""

# hi "You really can talk to me if stuff like this is bothering you. It's always difficult to do this sort of thing solo, you know?"
hi ""

show emi sad_grin_close
with charachange

# "Emi smiles and breaks the embrace, but stays leaning on my shoulder."
""

# emi "Thanks, Hisao."
emi ""

show emi basic_grin_close
with charachange

# emi "I'll be fine, I think."
emi ""

# "I can already see her reassembling herself, getting ready to bottle it all up again."
""

# "Guess that topic's closed, now."
""

# hi "So hey, given any more thought to that career survey?"
hi ""

show emi basic_closedgrin_close
with charachange

# emi "Can't say I have."
emi ""

show emi basic_grin_close
with charachange

# emi "I don't tend to plan very far ahead, you know."
emi ""

# emi "Although I suppose I could at least start looking into college, huh?"
emi ""

# "I shrug."
""

# hi "I suppose, unless you were serious about that pirate thing."
hi ""

# hi "Last I checked, pirates didn't have much need for universities."
hi ""

# hi "Unless there's like, a pirate university out there somewhere."
hi ""

show emi basic_closedgrin_close
with charachange

# "Emi giggles and starts to look a little like her old self, but there's a new element to her expression."
""

# "Impish. That's how I'd describe it."
""

# "Emi looks impish, looking up at me with her head nestled into my shoulder."
""

show emi sad_grin_close
with charachange

# emi "Would you come with me if I ran off to be a pirate?"
emi ""

# hi "Of course I would!"
hi ""

# hi "Who in their right mind would pass up the opportunity to be pirates with you?"
hi ""

show emi basic_grin_close
with charachange

# emi "Well, when you put it that way, I'm not sure."
emi ""

show emi basic_closedgrin_close
with charachange

# "She giggles again."
""

# "I notice that my heart seems to have sped up. It's probably due to Emi's proximity to me."
""

# "That hint of strawberries, again."
""

# "I can't help but grin as I gaze down at her."
""

# "She's happy again."
""

show emi sad_shy_close
with charachange

# emi "Hey, Hisao."
emi ""

# hi "Hmm?"
hi ""

show emi sad_grin_close
with charachange

# emi "If you're going to kiss me, you should probably do it soon. I think the lunch bell is about to ring."
emi ""

stop music fadeout 1.0

# "My thoughts grind to a sudden halt."
""

# "I'm pretty sure my mouth is hanging open in shock."
""

# "All I can manage is a strangled “Huh?”"
""

show emi basic_closedgrin_close
with charachange

# "This amuses Emi even more."
""

show emi excited_proud_close
with charachange

# emi "You were thinking about it, weren't you?"
emi ""

# "She sits up, bringing her face level with mine."
""

show emi basic_grin_close
with charachange

# emi "I'd probably enjoy it, you know?"
emi ""

show emi sad_grin_close
with charachange

# emi "You're a really…"
emi ""

show emi sad_shy_close
with charachange

# emi "…Well."
emi ""

# "She briefly composes herself, looking like she's about to say something important."
""

show emi sad_grin_close
with charachange

# emi "If you hadn't figured it out by now, I think I've developed a bit of a crush on you."
emi ""

show emi basic_grin_close
with charachange

# emi "You're going to have to do something about that."
emi ""

# "This time her grin short circuits several important thought processes."
""

# "At some point I turned toward her, and at another point her arms moved to around my neck."
""

# "At yet another, my arms wrapped around her waist."
""

# "I'll be damned if I could tell precisely when that happened."
""

# "Because at the moment, there's only a voice in the back of my head yelling at me to kiss her."
""

# "I look into Emi's eyes."
""

# "There it is."
""

# "The thing I saw yesterday on the bed. It's there again."
""

# "It suddenly strikes me that she's worried that I'll reject her."
""

stop ambient fadeout 1.5

# "What a silly worry for her to have."
""

window hide

play music music_romance fadein 0.5

scene white
show ev emi_firstkiss:
    truecenter
    zoom 4.0 rotate 20 subpixel True
    0.7
    linear 0.3 zoom 1.1 rotate 0
    easein 12.0 zoom 1.0
with GenericWhiteout(0.5, 0.2, 2.0)

with Pause (5.0)

nvl clear
nvl show dissolve

# n "\n\n\n\nHer lips taste faintly of strawberries."
n ""

# n "She leans into the kiss, and her arms tighten around the back of my head, making sure that I don't pull away."
n ""

# n "Not that there was any danger of that."
n ""

# n "There's a churning feeling in my gut."
n ""

# n "The world falls away."
n ""

# n "There's just me, and her, and this bench."
n ""

# n "My arms tighten, drawing her waist closer, entranced by the feel of her."
n ""

# n "I inhale her scent, my mind trying desperately to memorize everything about how she tastes, how she smells, how she feels."
n ""

play sound sfx_warningbell
play ambient sfx_rooftop fadein 4.0

nvl clear

nvl hide dissolve

scene bg school_roof
show bg school_roof_blurred as overlay:
    center
    linear 6.0 alpha 0.0
show emi sad_shyblush_close
with silentflash

window show

# "The ringing of the bell snaps us both back to reality, and we break the kiss."
""

# "Emi's cheeks are slightly flushed, and she seems to be catching her breath. In her defense, so am I."
""

# "We stand there for a few moments, trying to wrap our heads around what we've just done."
""

# "Emi is the first to break the silence."
""

show emi sad_grin_close
hide overlay
with charachange

# emi "So…"
emi ""

show emi basic_closedgrin_close
with charachange

# emi "…Wanna grab dinner after I'm done with practice?"
emi ""

# hi "What a coincidence."
hi ""

# hi "I was about to ask you the same thing."
hi ""

# "Well, actually I suppose it was going to be some kind of proper date on the weekend or something. But the thought was there, I think."
""

with vpunch

# "Emi gives me a playful shove."
""

show emi basic_happy_close
with charachange

# emi "Yeah right."
emi ""

show emi basic_closedhappy_close
with charachange

# emi "You were still in shock from how incredibly awesome I am at kissing."
emi ""

# "We begin to head down the stairs back to our respective classrooms."
""

stop ambient fadeout 2.0

scene bg school_hallway3
show emi sad_grin at center
with locationskip

# hi "Hey, I didn't see you talking immediately afterwards either."
hi ""

show emi basic_closedgrin
with charachange

# emi "That I didn't."
emi ""

show emi basic_closedhappy
with charachange

# emi "See you after practice, Hisao."
emi ""

show emi basic_closedgrin_close
with charachange

show emi basic_closedgrin_close:
    center
    easeout 0.5 xpos 0.6 alpha 0.0
with None

# "She leans in quickly and gives me a quick kiss in the middle of the hallway, sending me into another brief state of mental freefall."
""

scene bg school_scienceroom
with locationchange

# "As I head into my classroom, a giggling Misha greets me."
""

show misha hips_grin at center
with charaenter

# mi "Why Hicchan, you romantic, you~!"
mi ""

# mi "Did you confess on the rooftop? Did you~?"
mi ""

# hi "Er, actually I think it was the other way around."
hi ""

show misha cross_laugh
with charachange

# "This sends Misha into a fresh fit of laughter."
""

show misha hips_grin
with charachange

# mi "Young love is so unpredictable, isn't it~?"
mi ""

# "This being Misha, I suppose I should have expected her to tease me over this."
""

# hi "I guess…"
hi ""

show misha hips_grin:
    center
    easeout 0.5 xpos 0.4 alpha 0.0
with None

# "Before I can really respond, Mutou's entered the room and Misha skips off to her seat, giggling all the while."
""

# "I suspect that I'll get a lot of that sort of conversation now, especially seeing as how Emi kissed me right in the middle of the hall."
""

# "But somehow, I don't care about that."
""

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
stop music fadeout 5.0

# "For the first time since arriving here, my heart feels light."
""

window hide

return
