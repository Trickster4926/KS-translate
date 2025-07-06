label th_A19:

window hide None
scene black
with dissolve

play sound sfx_alarmclock
stop ambient
    
show bg school_dormhisao
with openeye

play music music_dreamy fadein 2.0

window show

# "The sound of an alarm pulls me out of a fitful slumber and into the unpleasant state of wakefulness."
"เสียงปลุกดังปลุกฉันจากการนอนหลับไม่สนิทให้ตื่นขึ้นมาอย่างหมดแรง"

# "I linger under the blanket for a few minutes, gathering energy to rise up while making excuses as for why I already haven't."
"ฉันมุดตัวอยู่ในผ้าห่มอีกสักพัก พยายามรวบรวมแรงเพื่อลุกออกจากเตียงพลางแก้ตัวว่าทำไมยังไม่ลุกออกจากเตียง"

# "Honestly, I wouldn't mind staying here for all day. School is surprisingly exhausting after a long pause, and the culture shock still has not faded, I think."
"ที่จริงจะนอนอยู่อย่างนี้ทั้งวันเลยก็ได้ พอไม่ได้มาโรงเรียนนานแล้วกลับมาอีกทีก็ทำเอาเพลียได้อย่างเหลือเชื่อ และ\nเหมือนจะยังไม่ชินกับสภาพแวดล้อมแบบนี้เท่าไหร่ด้วย"

# "Still, despite getting an impression that skipping class is easy here, I don't think they are going to let me get away that easily."
"แต่ก็นะ ถึงที่นี่จะโดดเรียนง่าย แต่ทำแล้วน่าจะโดนตามเช็คบิลแหง ๆ"

# "And the nurse is bound to keep breathing down my neck with the talk of exercising as well."
"แล้วคุณพยาบาลเองก็จะมาตามจ้ำจี้จ้ำไชเรื่องการออกกำลังกายอยู่ดี"

# "So eventually I do rise up, swallow the morning medications and put on my old soccer clothing."
"สุดท้ายฉันก็ลุกออกจากเตียง กินยาส่วนของตอนเช้าแล้วใส่ชุดเตะบอลตัวเก่า"

# "Thanks to my condition, I was exempted from taking part in gym classes at Yamaku, so I didn't get issued with a gym outfit."
"และเนื่องจากฉันได้รับการยกเว้นคาบพละที่โรงเรียนยามากุเพราะอาการของฉัน ทางโรงเรียนจึงไม่ได้จัดชุดพละมาให้"

# "I'd order some to cover such a contingency, but wearing my old soccer clothes is kind of nostalgic."
"เดี๋ยวฉันก็สั่งมาเอาไว้เผื่อใช้ในกรณีฉุกเฉินแหละ แต่ว่าใส่ชุดเตะบอลเก่าอันนี้ก็พานให้นึกถึงเมื่อก่อนดี"

# "I can't use them for that any more, so maybe they can get a new life this way. A bit like me."
"ยังไงจะใส่ไปเตะบอลแบบเดิมก็คงไม่ได้ละ เอามาใส่ใหม่แบบนี้ไปเลยก็ได้ เป็นตัวฉันดี"

label th_A19a:

#if C61

# "After all, if I'm going to start taking care of myself, I can't afford to slack around. I'll start from the basics."
"ยังไงซะ ถ้าฉันจะเริ่มดูแลตัวเองก็คงจะขี้เกียจไม่ได้ละ ฉันจะเริ่มจากอะไรง่าย ๆ ก่อน"

# "Basics which include keeping the rest of my body in shape along with what little I can do to strengthen my heart."
"ง่าย ๆ ที่รวมถึงการพยายามรักษาสุขภาพและออกกำลังกายเบา ๆ เพื่อให้หัวใจแข็งแรงขึ้น"

# "Maybe then I can go back to something approaching a normal life; or at least something where I'm less likely to fall over dead at any minute."
"บางทีถ้าทำแบบนั้นฉันอาจจะพอได้กลับไปใช้ชีวิตอย่างปกติได้ หรืออย่างน้อยก็จะไม่เสี่ยงหัวใจวายล้มตายได้ทุกเมื่อ\nแบบนี้"

stop music fadeout 2.0


label th_A19b:
#if C62

# "Seems a bit stupid to me, really."
"เอาจริงก็ดูบ้าบอไปหน่อยสำหรับฉัน"

# "But I suppose this way at least I can tell the nurse honestly that I'm doing something about my health."
"แต่อย่างน้อยคงเอาไปอ้างคุณพยาบาลได้ว่าดูแลตัวเองแล้ว"

# "Not that I was ever much of a runner to begin with."
"ก็ไม่เคยอยากจะเป็นนักวิ่งอยู่ละ"

# "Can't hurt to try, I guess."
"ลองหน่อยคงไม่เสียหาย คิดว่านะ"

stop music fadeout 2.0


label th_A19c:    
#End of split

show bg school_track
with locationskip

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_emijogging fadein 0.1

# "I'm surprised to discover that I'm not the only one present at the track."
"ฉันแปลกใจนิดหน่อยที่เห็นคนมาที่ลู่วิ่งอยู่ก่อนแล้ว"

# "Not just that, but it's a face I've seen before."
"ไม่ใช่แค่คนทั่วไป แต่เป็นคนที่หน้าคุ้น ๆ เคยเจอมาก่อน"  

# "The prosthetic-legged girl who bowled me over in the hallway yesterday is running on the track lithely, like a half-mechanical gazelle."
"สาวที่ใส่ขาเทียมคนที่วิ่งชนฉันที่โถงทางเดินเมื่อวานกำลังวิ่งอยู่บนลู่วิ่งอย่างคล่องแคล่วคล้ายกวางกึ่งจักรกล"

# "What was her name again? It was a short one, but I can't remember."
"เธอชื่ออะไรนะ ชื่อสั้น ๆ แต่ฉันจำไม่ได้"

# "She seems to be running laps at a somewhat easy lope, her prosthetic legs clacking rhythmically on the hard track surface."
"เธอดูวิ่งเป็นรอบ ๆ ได้อย่างสบาย ๆ ขาเทียมของเธอกระทบกับพื้นแข็งของลู่วิ่งอย่างเป็นจังหวะ"

# "I wonder what reason she has for running this early in the morning. Maybe it's something akin to mine, and the nurse is oppressing the poor girl to jog just like he is oppressing me."
"ฉันละอยากรู้ว่าทำไมเธอถึงต้องมาวิ่งแต่เช้าตรู่ขนาดนี้ บางทีเหตุผลอาจจะคล้าย ๆ ฉันแหละมั้ง แบบคุณพยาบาล\nบีบบังคับให้สาวน้อยที่น่าสงสารต้องมาวิ่งเหมือนกับที่เขาบังคับฉันมา"

# "I certainly wouldn't be here if it weren't for my health, and his prompting me to do so."
"ถ้าไม่ใช่ว่าเป็นเรื่องสุขภาพฉันกับที่เขาสั่งให้ฉันมาฉันคงไม่มาหรอก"

# "And even with things being like they are, it's only because I wanted to get it out of the way early."
"แต่แม้ฉันจะมาอยู่ตรงนี้เพราะอย่างนั้นแล้ว ที่รีบมาจะได้รีบทำไปให้มันจบ ๆ เฉย ๆ"

# "The fact that I would be less likely to encounter someone who would witness my pitiful attempts to get in shape was merely a happy accident."
"กับอีกอย่างที่ว่ามาเวลานี้โอกาสที่มีคนมาเห็นฉันพยายามอย่างน่าสมเพชเพื่อรักษาสุขภาพก็จะน้อยลง ซึ่งเป็นเรื่องที่ดี"

# "I'd leave, but it seems that my former assailant noticed me on her last lap."
"ว่าจะกลับละ แต่เหมือนว่าอดีตผู้ร้ายจะเห็นฉันในตอนที่เธอวิ่งรอบสุดท้าย"

# "She waves at me cheerfully and jogs over."
"เธอโบกมือให้ฉันอย่างร่าเริงและวิ่งเหยาะ ๆ เข้ามา"

show emi basic_grin_gym at Slide(0.7,0.5,0.5,0.5,1.0,_ease_in_time_warp)
with charaenter

stop ambient

# emi_ "Good morning! Your name is Hisao, right?"
emi_ "อรุณสวัสดิ์! นายชื่อฮิซาโอะใช่ไหม"

play music music_emi fadein 2.0

# "She grins, seemingly pleased that she'd remembered my name."
"เธอยิ้ม ท่าทางดีใจที่เธอจำชื่อฉันได้"

show emi basic_closedgrin_gym at center
with charachange

# emi_ "You may not remember me."
emi_ "นายน่าจะจำฉันไม่ได้"

show emi basic_grin_gym
with charachange

# emi_ "Emi? I knocked you over in the hall yesterday."
emi_ "เอมิไง คนที่ชนนายที่โถงทางเดินเมื่อวานน่ะ"

label th_A19i:

show emi excited_circle_gym
with charachange

# emi "“Miss Ibarazaki?”"
emi "“คุณอิบาราซากิ”"

# "She imitates Misha “imitating” Shizune, failing to get the same kind of subdued lilt into her high-pitched voice."
"เธอเลียนแบบมิช่าที่ “เลียนแบบ” ชิซูเนะอีกที แต่ก็ไม่เหมือนตรงที่เลียนแบบเสียงต่ำไม่ได้เนื่องด้วยเสียงแหลมของเธอ"


label th_A19j:

# hi "How could I forget such a er, blunt introduction?"
hi "ฉันจะลืมการแนะนำตัวที่แสน เอ่อ ดุดันไปได้ไง"

show emi sad_shy_gym
with charachange

# "Emi has the decency to look vaguely apologetic for a moment before giggling."
"เอมิทำท่าจะรู้สึกผิดไปแวบนึง ก่อนที่จะหัวเราะคิกคักออกมา"

show emi sad_grin_gym
with charachange

# emi "Yeah, sorry about that. Again."
emi "อื้อ ขอโทษเรื่องนั้นอีกรอบนะ"

# hi "Hmm, well, so long as you don't make a habit of it, I suppose I'll be fine."
hi "อืมม ก็ถ้าไม่ได้มาชนเป็นกิจวัตรก็ไม่เป็นไรหรอก"

show emi basic_happy_gym
with charachange

# emi "Great!"
emi "เยี่ยม!"

# "I'm not sure she realized I was joking."
"ไม่แน่ใจว่าเธอจะเข้าใจไหมว่าเมื่อกี้คือมุก"

# hi "So the “spy-consultant” the nurse was talking about… is that actually you?"
hi "สรุปว่า “สายลับที่ปรึกษา” ที่คุณพยาบาลเคยพูดถึงเป็นเธอเองหรอกเหรอ?"

show emi basic_closedgrin_gym
with charachange

# emi "That's right!"
emi "ใช่แล้วละ!"

# hi "Oh."
hi "โอ้"

# hi "I was expecting someone from the nursing staff, to be honest."
hi "เอาจริง ตอนแรกนึกว่าจะเป็นเจ้าหน้าที่พยาบาลเสียอีก"

show emi basic_confused_gym
with charachange

# emi "What, are you saying I don't look like I could be a spy?"
emi "อะไรกัน นายจะบอกว่าฉันเป็นสายลับไม่ได้เหรอ"

# hi "No, this is more like a relief. I was afraid he would have someone to watch my every move."
hi "เปล่า ฉันแค่โล่งอกเฉย ๆ ตอนแรกระแวงว่าจะมีคนจับตาดูทุกฝีก้าวอะไรแบบนั้น"

# hi "Unless you are here to do exactly that."
hi "เว้นแต่ว่าเธอจะมาที่นี่เพื่อทำแบบนั้นอะนะ"

show emi excited_laugh_gym
with charachange

# emi "No, I'm here for my own reasons, the nurse just asked me if I had seen “a messy-haired transfer student who looks like he's kinda lost” around the track."
emi "เปล่า ฉันมาที่นี่ก็มีเหตุผลของฉันเองด้วย คุณพยาบาลถามแค่ว่าฉันเห็น “นักเรียนที่ย้ายมาใหม่ ผมยุ่ง ๆ คนที่ทำท่า\nเหมือนกับหลงทางอยู่” แถว ๆ ลู่วิ่งไหม"

# hi "So why are you down here?"
hi "แล้วทำไมเธอถึงมาที่นี่ล่ะ?"

# "Emi strikes a dramatic pose."
"เอมิทำท่าเล่นใหญ่"

show emi basic_happy_gym
with charachange

# emi "Training!"
emi "มาซ้อม!"

# hi "For what?"
hi "ซ้อมอะไร"

show emi basic_closedhappy_gym
with charachange

# emi "Track!"
emi "วิ่งแข่ง!"

# hi "Ah, I see. You're on the track team, then?"
hi "อ๋อ งี้นี่เอง เธออยู่ในทีมแข่งสินะ"

# "Emi nods enthusiastically."
"เอมิพยักหน้าอย่างกระตือรือร้น"

show emi excited_proud_gym
with charachange

# emi "Yep! I'm one of the better runners, too!"
emi "อื้อ! และฉันก็เป็นตัวแบกทีมด้วยละ!"

# "And modest about it, too."
"แถมไม่ค่อยจะอวดสักเท่าไหร่เลย"

show emi basic_grin_gym
with charachange

# emi "Hey, you should join up!"
emi "นี่ นายก็เอาบ้างสิ!"

# emi "It's good exercise, you know."
emi "จะได้ออกกำลังกายดี ๆ เลยไง"

# "I think that much activity is probably out of the question for me."
"ฉันว่ากิจกรรมใช้แรงเยอะขนาดนั้นฉันไม่น่าไหวแน่ ๆ"

# hi "Nah, I'm not even sure that I really like running all that much."
hi "ไม่หรอก ฉันไม่แน่ใจด้วยซ้ำว่าฉันจะชอบวิ่งขนาดนั้นไหม"

# hi "Plus I'm just not into organized sports, you know?"
hi "อีกอย่าง ฉันเองก็ไม่ได้ชอบพวกงานจัดแข่งกีฬาสักเท่าไหร่"

# "It's true. I never even really got that much into soccer."
"นั่นแหละ ฉันไม่ได้ชอบเล่นบอลขนาดนั้นด้วยซ้ำ"

# "I mean I'd run around with my friends and all, but that was really the only reason I ever played."
"คือก็เคยเล่นกับพวกเพื่อน ๆ น่ะนะ แต่นอกจากนั้นก็ไม่ได้เล่นละ"

# "It wasn't for the glory to be found on the field, that's for sure."
"ไม่ได้เล่นเอาชื่อเสียงเรียงนามจากสนามแข่งขนาดนั้น"

# "Emi seems to understand my meaning."
"เอมิดูจะเข้าใจสิ่งที่ฉันจะสื่อ"

show emi basic_confused_gym
with charachange

# emi "I see, I see. Not that into the whole organization thing."
emi "อย่างนี้นี่เอง ไม่ชอบพวกการจัดแข่งกีฬาอะไรแบบนั้นสินะ"

show emi excited_proud_gym
with charachange

# emi "But now that you're here, I guess we're going to run together, huh?"
emi "แต่ไหน ๆ นายก็มาแล้ว มาวิ่งด้วยกันดีไหมล่ะ"

# hi "What? Er, sure, I guess."
hi "อะ เอ่อ ก็ได้แหละ"

# "Emi seems pleased."
"เอมิดูท่าดีใจ"

show emi excited_joy_gym
with charachange

# emi "Are you going to warm up?"
emi "นายจะอุ่นเครื่องก่อนไหมล่ะ"

# hi "Real men don't warm up."
hi "คนจริงไม่ต้องอุ่นเครื่อง"

show emi basic_annoyed_gym
with charachange

# emi "Oh no, you always should warm up! Bad Hisao!"
emi "ไม่ได้นะ นายควรจะอุ่นเครื่องก่อนทุกครั้ง! แย่จริง ๆ เลยฮิซาโอะ!"

show emi excited_proud_gym_close
with characlose


# "She scolds me enthusiastically, but then smiles and leans closer."
"เธอต่อว่าฉันอย่างจริงจัง แต่ก็สิ่งยิ้มแล้วเอี้ยวตัวเข้ามาใกล้"

# emi "I hate warming up too."
emi "จริง ๆ ฉันก็ไม่ชอบอุ่นเครื่องเหมือนกันแหละ"

show emi excited_laugh_gym_close
with charachange

# "She laughs suddenly."
"แล้วเธอก็หัวเราะออกมา"

# emi "Heck, and I don't even have to stretch my legs!"
emi "โอ๊ย ขนาดฉันไม่ต้องยืดขายังต้องทำเลย!"

play sound sfx_gymbounce

show emi gymbounce
with charadistant

# "As if to confirm her statement she bounces up and down a couple of times, giving a passing impression of standing on a pair of springs. Her legblades seem to be quite elastic."
"เธอกระโดดขึ้นลงสองสามทีราวกับยืนอยู่บนสปริงคล้ายจะยืนยันคำพูดของเธอ ใบขาเทียมของเธอค่อนข้างยืดหยุ่นดี\nเลยทีเดียว"

# emi "Let's go!"
emi "ไปกันเลย!"

stop music fadeout 1.0

play ambient sfx_emijogging fadein 0.3

scene bg school_track_running
with locationchange

# "So we both take off around the track, and I can immediately see that she wasn't lying about being good at running."
"พวกเราเริ่มออกตัววิ่งไปตามลู่วิ่ง และฉันก็ได้เห็นทันทีว่าเธอไม่ได้โกหกเรื่องที่เธอวิ่งเก่งจริง ๆ"

# "Emi moves fluidly, throwing herself into the run with a sort of wild abandon."
"เอมิเธอพลิ้วไหวดั่งสายน้ำสับเท้าวิ่งไปสุดกำลัง"

# "I find myself concentrating more on running properly."
"ฉันสังเกตว่าตัวเองจดจ่ออยู่กับการวิ่งให้ถูกต้องมากขึ้น"

#if C61


label th_A19d:

# "Hands spread, right?"
"กางมือออก ใช่ไหมนะ"

# "And something about hitting on the balls of your feet, rather than the heels…"
"แล้วก็เหมือนจะให้ลงน้ำหนักไปที่หน้าเท้าแทนที่จะเป็นส้นเท้า…"

# "I try to match my stride to Emi's, but it's pretty difficult."
"ฉันพยายามวิ่งให้ทันกับเอมิ แต่ก็ยากเอาการ"

# "Apparently I'm not very good at it."
"เหมือนว่าฉันจะยังวิ่งไม่เก่งเท่าไหร่"

# "Maybe Emi could help me with that sometime."
"ไว้ให้เอมิช่วยแนะนำน่าจะดี"



label th_A19e:

#if C62

# "Frankly, I don't remember if there's any particular form for running, but I can't help but feel like I'm doing it wrong, somehow."
"จริง ๆ แล้วฉันเองก็จำไม่ได้ว่ามีวิธีวิ่งแบบถูกวิธีอยู่หรือเปล่า แต่ตอนนี้เหมือนกับว่าฉันวิ่งผิดวิธีอยู่ยังไงยังงั้น"

# "I feel awkward in comparison to Emi, who never seems to break stride."
"พอเทียบกับเอมิที่ดูจะยังวิ่งไปอย่างสม่ำเสมอได้ตลอดนั้นแล้วท่าวิ่งฉันดูเก้กังไปเลย"

"…"

# "I don't think I want to do this any more."
"ฉันว่าฉันคงวิ่งไม่ไหวแล้ว"


label th_A19f:

# "I'm really not feeling up to more than a couple of laps today, and slow to a walk pretty quickly."
"ฉันรู้สึกว่าวันนี้วิ่งต่ออีกรอบไม่ไหวแล้ว และพลันเปลี่ยนมาเป็นเดินแทน"

scene bg school_track_on
with Dissolve(4.0)

# "Emi keeps running, and doesn't seem to notice I've stopped until she passes me a second time."
"เอมิยังคงวิ่งอยู่ และดูเหมือนว่าจะไม่ทันสังเกตเห็นฉันจนกระทั่งเธอวิ่งผ่านฉันไปรอบที่สอง"

stop ambient

# "She quickly skids to a halt, breathing steadily in contrast to my own somewhat gasping demeanor."
"เธอเบรกเอี๊ยดทันที เธอยังหายใจได้อย่างปกติ ต่างจากฉันที่ไม่แม้แต่จะหายใจทั่วท้อง"

play music music_emi fadein 2.0

show emi basic_confused_gym at center
with charamoveinleft

# emi "Finished already?"
emi "วิ่งเสร็จแล้วเหรอ"

# "I hang my head ruefully."
"ฉันก้มหน้าสลด"

# hi "Heh, yeah."
hi "ฮะ ๆ อื้อ"

# hi "I'm not in very good shape right now."
hi "ร่างกายตอนนี้ไม่ค่อยไหวน่ะ"

show emi basic_grin_gym
with charachange

# "Emi nods, and then grins at me again."
"เอมิพยักหน้า แล้วส่งยิ้มมาให้ฉันอีกครั้ง"

# "She seems to do a lot of smiling."
"เธอนี่ยิ้มบ่อยจริง ๆ"

# emi "Well, the important thing is you started, right?"
emi "แต่ก็ สิ่งที่สำคัญที่สุดก็คือนายก็ได้เริ่มแล้ว ใช่ไหมล่ะ"

show emi excited_amused_gym
with charachange

# emi "Next time, you just have to try to hold out longer, and then longer, and longer, and eventually you'll be great!"
emi "วิ่งรอบหน้านายก็ลองฮึดวิ่งให้นานขึ้น นานขึ้น แล้วก็นานขึ้นไปอีก แล้วในที่สุดนายก็จะวิ่งเก่งเอง!"

# hi "I'll keep that in mind."
hi "จะพยายามละกัน"

# hi "But I think right now I'm going to go get ready for class."
hi "แต่ตอนนี้เดี๋ยวเตรียมตัวไปเรียนละ"

# hi "Shouldn't you?"
hi "แล้วเธอไม่ไปเหรอ?"

# "Emi shrugs unconcernedly."
"เอมิยักไหล่อย่างไม่ยี่หระ"

show emi basic_grin_gym
with charachange

# emi "Nah, I've got plenty of time."
emi "ไม่ละ ฉันยังเหลือเวลาอีกเยอะเลย"

# "I notice that she's not wearing a watch."
"ฉันสังเกตว่าเธอไม่ได้ใส่นาฬิกามา"

# hi "Are you sure?"
hi "แน่ใจนะ"

# "Another careless shrug."
"เธอยักไหล่อีกรอบ"

# emi "Not really… but I've got to finish my routine!"
emi "ก็ไม่ค่อยแน่ใจ…แต่ยังไงฉันก็จะวิ่งรอบสุดท้ายให้จบก่อน!"

show emi basic_closedgrin_gym
with charachange

# emi "See you later, Hisao!"
emi "ไว้เจอกันนะฮิซาโอะ!"

# hi "Er, yeah. See ya."
hi "เอ่อ อื้ม เจอกัน"

stop music fadeout 5.0
play ambient sfx_emisprinting

hide emi
with easeoutleft

stop ambient fadeout 2.0


label th_A19g:

#if C61
# "I'm not sure whether this morning's experiment was a success or a failure, but I'll admit that I do feel slightly good about getting out there this morning."
"ฉันไม่แน่ใจว่าจะเรียกการลองวิ่งเช้านี้ว่าสำเร็จได้ไหม แต่ยอมรับเลยว่ารู้สึกดีขึ้นมานิดหนึ่งที่ได้ออกมาเช้านี้"

# "And like Emi said, I just need to keep at it in order to get better, right?"
"และก็อย่างที่เอมิบอก ฉันต้องมาบ่อย ๆ เพื่อจะได้ทำได้ดีขึ้นสินะ"

# "Practice makes perfect, or something like that."
"ความพยายามอยู่ที่ไหน หรืออะไรทำนองนั้น"

# "It's nice at least to feel like I've taken some semblance of control over my own health."
"อย่างน้อยก็รู้สึกดีที่พอควบคุมสุขภาพของตัวเองได้แล้ว"

# "I'll have to try to keep this up."
"ต้องหมั่นออกมาวิ่งเรื่อย ๆ แล้ว"

scene black
with locationskip_in

label th_A19h:
#if C62

# "Apart from feeling more tired than before, I don't think I accomplished anything today."
"นอกจากว่ารู้สึกเหนื่อยกว่าเดิมแล้ว ฉันว่าฉันไม่ได้อะไรเลยวันนี้"

# "I'm so out of shape it's embarrassing."
"ร่างกายฉันอ่อนแอเหลือเกิน น่าอายจริง ๆ"

# "The whole thing might have been a waste of time. I'll find some other way."
"ทำไปก็คงเสียเวลาเปล่า ฉันคงจะหาทางอื่นเอา"

scene black
with locationskip_in


#**********************************

label th_A20:

scene bg school_dormext_half
with locationskip_out

# "I head back to the dorms to wash and change into my uniform, trying to resist the urge to take a really long and hot shower."
"ฉันตรงดิ่งกลับมาที่หอเพื่ออาบน้ำแต่งตัว พยายามฝืนตัวเองให้ไม่อาบน้ำร้อนนานเกิน"

# "I'm tired from all the running, so I just want to unwind, but I don't want to break my slowly building routine of getting to school before the morning rush."
"ฉันหมดแรงจากการวิ่งมาเลยอยากจะผ่อนคลายสักหน่อย แต่ก็ไม่อยากติดนิสัยเสียในช่วงที่กำลังทำให้ตัวเองชินกับการ\nไปโรงเรียนแต่เช้าแบบไม่ต้องเร่งรีบ"

scene bg school_dormbathroom
show steam
show steam2
with shorttimeskip

# "After taking a long shower anyway, I dry myself off and get out of the stall to put on my clothes."
"สุดท้ายก็แช่อยู่นานอยู่ดี ฉันเช็ดตัวให้แห้งก่อนจะออกจากห้องอาบน้ำเพื่อใส่เสื้อผ้า"

show kenji silhouette_naked at center behind steam
with charaenter

# "Out of nowhere, a shadow appears within the mist, looming and radiating malicious intent. It bursts through the fog."
"จู่ ๆ ก็มีเงาที่แผ่รังสีชั่วร้ายทะลุปรากฏขึ้นในหมอก เงานั้นเดินผ่านม่านไอน้ำออกมา"

play music music_kenji fadein 0.3

hide steam
hide steam2
show kenji neutral_naked
show steam as newsteam behind kenji
show steam2 as newsteam2 behind kenji
with charachange

# ke "Sup?"
ke "ไง"

# hi "What are you doing here? What the hell, you scared me! What's your problem?!"
hi "มาทำไรเนี่ยเฮ้ย ตกใจหมด! มีไรว่ามา!"

show kenji tsun_naked
with charachange

# ke "I should be asking you that. I've been looking for you all over the place, man."
ke "ฉันสิต้องถามนาย ฉันหานายให้ทั่วเลยให้ตายสิ"

# hi "What do you mean “all over the place”?"
hi "หา “ ให้ทั่ว” นี่คือ?" # spacing cause thai ใ make ' invisible"

# "I want to ask if he's been looking for me like that, stark naked, but hold my tongue back."
"ฉันอยากจะถามว่าเขาตามหาฉันด้วยสภาพตัวเปลือยแบบนี้หรือไง แต่ก็ยั้งปากไว้"

# "I finally realize I'm still naked too and quickly hold up my shirt in front of me, but Kenji doesn't seem to notice a thing."
"เพราะฉันก็นึกขึ้นได้ว่าตอนนี้ฉันเองก็อยู่ในสภาพเปลือยไม่ต่างกัน ฉันรีบเอาเสื้อมาปิดตัว แต่ดูเหมือนว่าเคนจิจะ\nไม่เห็นอะไรเลยสักอย่าง"

# "His glasses are fogged up. But then, why doesn't he wipe them off? Is his vision so bad it's like he's perpetually seeing through fog?"
"ฝ้าเกาะแว่นเต็มขนาดนั้นทำไมไม่เช็ดออก หรือสายตาจะแย่ถึงขั้นเหมือนมองผ่านหมอกอยู่ตลอดเวลาอยู่แล้ว?"

# ke "You know, your room, and… Yeah, that's it. Hey, I mean, I still had to get up, though. Whatever. It's not important. Can I borrow some money?"
ke "ก็ หาห้องนายไง แล้วก็…เออนั่นแหละ เนี่ยเห็นปะว่ายังไงฉันก็ต้องตื่นมาอยู่ดี เออช่างเหอะ ไม่สำคัญ ขอยืมเงินหน่อย\nได้ปะ"

show kenji neutral_naked
with charachange

# "He puts on an innocent face and looks away, trying very hard to look very casual. It doesn't work; he's as transparent as his windowpane-sized glasses."
"เขาทำหน้าใสซื่อเสมองทางอื่น ฝืนเก๊กท่าให้ปกติเหมือนไม่มีอะไรเกิดขึ้น ซึ่งไม่ได้ผล แค่นี้ก็เห็นทะลุปรุโปร่งไปยันไส้ใน\nไม่ต่างอะไรกับเลนส์แว่นอันเท่าบ้านคู่นั้นแล้ว"

# "Talking neutrally like this, wearing nothing, feels awkward."
"พอมาคุยอย่างปกติโดยไม่ใส่อะไรเลยอย่างนี้แล้วกระอักกระอ่วนชะมัด"

# "Actually, somehow it's even more awkward to be naked in front of someone when they can't see me being naked. To say nothing of the fact that he's naked as well."
"แล้วแถมต้องมาเปลือยต่อหน้าคนที่ไม่เห็นว่าฉันเปลือยอยู่อีก แล้วยิ่งเขาก็เปลือยด้วยอีกต่างหาก"

# "I try to brush the feeling off, with little success."
"ฉันพยายามปัดความรู้สึกนั้นออก ซึ่งแทบไม่ได้ผลเลย"

# hi "Money? Sure."
hi "เงินเหรอ ได้ดิ"

show kenji happy_naked
hide newsteam #lessening the processor load a little
with charachange

# ke "Awesome."
ke "เยี่ยม"

# hi "Wait, why do you need it?"
hi "เดี๋ยวก่อน เอาไปทำอะไร"

show kenji tsun_naked
with charachange

# ke "Ehhhh…"
ke "เอ่อ…"

show kenji neutral_naked
with charachange

# ke "Can't you just give it to me because I had the good will not to run through your pockets while you were in the shower? I could have, but I exercised restraint. And in the end, isn't it the thought that counts? Come on, be a pal."
ke "นี่ฉันอุตส่าห์เป็นคนดีไม่แอบขโมยเงินนายตอนนายอาบน้ำเลยนะ ให้ฉันหน่อยไม่ได้เหรอ จริง ๆ ฉันทำได้แต่ก็ไม่ทำไง\nแค่นี้ยังดีไม่พอเหรอ ไม่เอาน่าพวก"

# "This makes no sense. If it's the thought that counts, I should withhold payment, since his thoughts were so clearly impure and his intentions are probably even more sinister since he can't tell me what they are. I say as much to him."
"ไม่เห็นจะเกี่ยวเลย ถ้าคนเขาว่ากันว่าขอแค่คิดดีแล้วก็นับว่าดี ฉันว่าฉันไม่ให้ยืมดีกว่า เพราะเห็นชัดว่าความคิดเขานั้น\nไม่ได้ดีเลย แล้วเจตนาของเขาอาจจะเลวร้ายหนักกว่านั้นอีกเพราะเขาไม่ยอมบอกว่าจะเอาไปทำอะไร เท่าที่เห็น\nแล้วเขาก็เป็นอย่างนั้นจริง ๆ "

show kenji tsun_naked
with charachange

# ke "I'm offended man, but if that is your game, then fine, I guess I have no choice. I want to order a pizza, and I already have most of the cost of the pizza. I need your help for the rest."
ke "นี่ทำร้ายจิตใจกันอยู่นะเนี่ย แต่ถ้านายจะเล่นกันอย่างนี้ ฉันก็คงไม่มีทางเลือกอื่นแล้วละ คือฉันว่าจะสั่งพิซซ่า แล้วตอนนี้\nก็มีเงินเกือบจะพอสั่งแล้ว ฉันเลยอยากให้นายช่วยเติมส่วนที่ขาดไปหน่อย"

# hi "I get some of that pizza too, right?"
hi "ถ้างั้นฉันจะได้กินพิซซ่าด้วยใช่ไหม"

# ke "No."
ke "ไม่"

# hi "Are you serious?"
hi "เอาจริงดิ" # "มึงจะบ้าเหรอ #lmao" 

show kenji neutral_naked
with charachange

# ke "Yeah. I would give you some, but you have class, you don't have time to eat a pizza."
ke "น่า ฉันก็ว่าจะแบ่งให้แหละ แต่นายมีเรียนนี่ ไม่มีเวลามากินพิซซ่าหรอก"

# hi "What about you?!"
hi "แล้วนายไม่มีเรอะ!"

# ke "I'm not going to class, I have to wait for the pizza and pay the guy. And then eat it. It's not easy. You have to obtain the pizza stealthily. If you don't, everyone will see you. And the pizza. And they will ask for a slice."
ke "ฉันไม่เข้าเรียน ฉันต้องรอพิซซ่ามาส่งแล้วจ่ายเงินแล้วก็กิน ไม่ง่ายนะเว้ย ต้องแอบไปเอาพิซซ่าแบบเงียบ ๆ ไม่งั้นเดี๋ยวมีคน\nมาเห็นแล้วมาขอแบ่งอีก"

show kenji tsun_naked
with charachange

# ke "It's a hard world out there. Everyone wants a piece. Then you're left pizzaless in an unforgiving world. It's happened before, that's how I know."
ke "โลกนี้อยู่ยากว่ะ ทุกคนต่างก็อยากได้ส่วนแบ่งกัน ท้ายที่สุดนายก็จะถูกปล่อยให้สิ้นไร้ไม้พิซซ่าในโลกที่โหดร้าย ที่ฉันรู้\nเพราะฉันเคยเจอมาก่อนไง"

# ke "Every day, I plan my vengeance, so that when the people who wronged me order a pizza, I will be there. Ever vigilant!"
ke "ทุก ๆ วันฉันวางแผนคอยแก้แค้น ฉันจับตามองตลอด เพื่อที่เมื่อคนที่เคยเล่นงานฉันสั่งพิซซ่าบ้าง ฉันก็จะพุ่งไปทันที!"

# "Kenji strikes a dramatic pose, completely without irony."
"เคนจิทำท่าเล่นใหญ่ไร้ซึ่งการล้อเล่นใด ๆ "

show kenji neutral_naked
with charachange

# ke "But yeah, I only need like 400 yen. Please! You're my only hope! I can't go outside and buy my own pizza, it's too far!"
ke "เออนั่นแหละ ตอนนี้ขาดอีก 400 เยน ขอร้องล่ะ! นายคือความหวังสุดท้ายแล้ว! ฉันออกไปข้างนอกเพื่อไปซื้อพิซซ่า\nไม่ไหวหรอก ร้านอยู่ไกลเกิน"

# ke "I try not to go out unless it's absolutely necessary. Let me tell you what happened the last time I went out without carefully planning it out in advance."
ke "ฉันจะไม่ออกไปไหนถ้าไม่จำเป็นแบบจำเป็นจริง ๆ เดี๋ยวเล่าให้ฟังว่าครั้งล่าสุดที่ออกไปโดยไม่ได้วางแผนล่วงหน้าไว้ให้ดี\nมันเกิดอะไรขึ้น"

# ke "I was outside. I can't remember what I was doing. Something. Standing? Maybe wondering how I got there."
ke "ฉันอยู่ข้างนอก ฉันจำไม่ได้ว่าไปทำอะไร สักอย่างแหละ ยืนเฉย ๆ มั้ง ไม่ก็คิดอยู่ว่ามานี่ได้ไง"

show kenji tsun_naked
with charachange

# ke "And then, out of nowhere, it happened."
ke "ทันใดนั้นเอง จู่ ๆ มันก็เกิดขึ้น"

# ke "Like a flash of lightning, splitting the sky, like how you split a sandwich into two equal pieces to make it more manageable to hold and eat, a bird crapped on my head."
ke "มันมาอย่างรวดเร็วเหมือนฟ้าผ่าแยกท้องฟ้าเป็นสองส่วนเหมือนตอนแบ่งแซนด์วิชให้กินได้ง่าย ๆ ทันใดนั้นเองนกก็ขี้\nใส่หัวฉัน"

# ke "It was the second most shocking moment of my life."
ke "นั่นเป็นสิ่งที่ฉันช็อกเป็นอันดับสองของชีวิตฉันเลย"

# hi "What was the first?"
hi "แล้วอันดับหนึ่งคือ?"

# "He ignores me and keeps going. I want to grab him and shake him. Is he just trying to keep momentum? I'll go with that, even if it's more likely he just didn't hear me."
"คำเมินคำพูดของฉันแล้วเล่าต่อ ฉันอยากจะจับไหล่แล้วเขย่าเรียกสติสักหน่อย นี่เขาพยายามจะไหลต่ออีกเหรอ งั้นก็ได้\nถึงแม้จริง ๆ แล้วเขาน่าจะแค่ไม่ได้ยินที่ฉันพูดมากกว่า"

# ke "It was like in the openings to some kind of anime show, you know how there is always a part where the main dude is fighting his rival, and they fly at each other and clash swords and there's like, big dramatic colored auras and zoom?"
ke "เหมือนฉากเปิดอนิเมะ แบบ ที่มีจะตอนที่พระเอกสู้กับตัวร้ายตลอด พุ่งเข้าหากันประชันดาบแล้วแบบ เล่นแสงสี\nอลังการงานสร้างพร้อมเสียงระเบิดภูเขาเผากระท่อมงี้"

show kenji neutral_naked
with charachange

# ke "It was like that, but with poo."
ke "เป็นแบบนั้นแหละ แค่เป็นขี้นกเฉย ๆ"

# hi "Okay."
hi "เคเลย"

show kenji happy_naked
with charachange

# ke "So yeah, I need some money. Please? Don't leave me hanging, man. I only need like 1000 yen."
ke "ก็นั่นแหละ ฉันต้องการเงินสักหน่อย นะ ๆ อย่าปล่อยฉันอดตายเลยพวก ขาดแค่ 1000 เยนเอง"

# hi "I thought it was 400."
hi "ไหนบอก 400"

# ke "Okay."
ke "โอเค"

# hi "What?"
hi "ฮะ?"

# ke "I'll pay you back, I swear."
ke "เดี๋ยวคืนให้ สาบาน"

# hi "You better, that's what it means to borrow stuff."
hi "ก็ต้องเป็นแบบนั้นไหม ยืมเงินก็ต้องคืนสิ"

show kenji neutral_naked
with charachange

# ke "I don't know when I'll be able to pay you back."
ke "แต่ไม่รู้นะว่าจะได้คืนเมื่อไหร่"

# hi "You have one week."
hi "ให้เวลาสัปดาห์นึง"

show kenji tsun_naked
with charachange

# ke "Aaaaaaaaaaaaaaahhhhhhhhhhhhhhhhhhhhhhhhggggggggggghhhhhhhh……"
ke "อ๊าาาาาาาาาาาาาาาาาาาาาาาากกกกกกกกกกกกกกกกกกกกกกกกกกกกกกกกก……"

# "Kenji winces and makes a noise like a dying cow, a particularly disturbing fact given that his baton is conducting freely."
"เคนจิผงะถอยแล้วร้องเสียงเหมือนวัวโดนเชือด พอเห็นประกอบกับภาพไม้บาตองที่กวัดไกวคุมเสียงประสานอยู่อย่าง\nเสรีตรงข้างล่างนั้นแล้วก็ยิ่งชวนให้ใจคอไม่ดี"

# ke "You're not supposed to be so tight assed about money between brothers in arms, man. Men have it bad enough as it is. Did you know that male porn stars only make about half of what female porn stars make?"
ke "เพื่อนกันจะมาขี้เหนียวอะไรกันนักหนา เนี่ยแค่เกิดเป็นผู้ชายก็ลำบากมากพอละ รู้เปล่าว่าดาราหนังโป๊เนี่ยผู้ชายทำเงิน\nได้แค่ครึ่งเดียวของผู้หญิงเองนะ"

# hi "That doesn't mean anything unless you're a porn star."
hi "ก็ไม่เห็นจะเกี่ยวอะไรนี่ถ้านายไม่ใช่ดาราหนังโป๊ที่ว่า"

# ke "So maybe I am a porn star, on the side, struggling to make ends meet as I fight the feminist agenda, and you can't even spot me your crumbs, you bastard. Nobody understands. Nobody."
ke "ไม่แน่ฉันอาจจะรับจ๊อบไปเป็นก็ได้ แบบว่าเป็นดาราหนังโป๊ที่ต้องดิ้นรนหาเลี้ยงชีพขณะที่ต้องสู้กับแนวคิดสตรีนิยม แต่\nกะอีแค่เศษเงินหลังตู้เย็นนายก็ให้ฉันไม่ได้ ไม่มีใครเข้าใจฉันเลย ไม่มีเลย"

# "Wouldn't feminists be against pornography in the first place?"
"ไม่ใช่ว่าพวกสตรีนิยมจะต่อต้านพวกงานลามกอนาจารแบบนั้นตั้งแต่แรกเหรอวะ"

# hi "This feminist agenda stuff again?"
hi "เรื่องสตรีนิยมอีกแล้วเรอะ"

# ke "This stuff is important. I can see that you don't give a shit, but this is serious, here. Feminists… are a dangerous enemy, make no mistake. You take them lightly, and you'll wake up in the morning with a knife in your back, bam! Out of nowhere!"
ke "เรื่องนี้สำคัญนะเว้ย ฉันรู้นะว่านายไม่สนไม่แคร์ด้วยซ้ำ แต่นี่จริงจังนะ พวกสตรีนิยมน่ะ…เป็นศัตรูตัวฉกาจเลยละ อย่าได้\nประมาทเชียว ถ้านายเผลอตัวนิดหน่อยล่ะก็ ตูม! นายได้ตื่นมาพร้อมมีดที่โผล่มาปักหลังนายแน่"

# hi "How do you wake up in the morning if someone stabbed you in your sleep?"
hi "แล้วจะตื่นยังไงวะถ้ามีคนมาแทงตอนนอน"

show kenji happy_naked
with charachange

# ke "Women are terrible at stabbing things."
ke "พวกผู้หญิงน่ะแทงไม่เก่งหรอก"

# hi "I thought you just said don't take them lightly."
hi "ไหนบอกว่าอย่าประมาทไง"

show kenji neutral_naked
with charachange

# ke "Well, I mean don't take them lightly for the big things. Individually they're not a threat, but if there was some kind of war, like a big war, with men on one side, and the feminist forces on the other side, it would be pretty ugly."
ke "เอาน่า ฉันหมายถึงอย่าประมาทพวกผู้หญิงตอนอยู่หมู่มากน่ะ มาเดี่ยว ๆ ไม่ใช่ปัญหาอะไรหรอก แต่คิดสภาพตอนเกิด\nสงครามที่แบบใหญ่มาก ๆ ที่ฝั่งนึงเป็นผู้ชาย อีกฝั่งเป็นกองกำลังพวกสตรีนิยม สภาพดูไม่ได้แน่ ๆ "

show kenji tsun_naked
with charachange

# ke "And that day will come, when the feminists come out of their central top secret worldwide feminist headquarters, and say “It's on now, motherfuckers!”"
ke "สักวัน วันนั้นจะมาถึง วันที่เหล่าสตรีนิยมจะออกมาจากฐานปฏิบัติการลับพิเศษสตรีนิยมระดับโลกแล้วบอกว่า “มาดิวะ\nไอ้แม่เย็ด!”" # soften by using "ไอ้เวรเอ๊ย!"

# hi "You're being ridiculous, there's no big worldwide feminist headquarters building, where would they even hide that? I mean, it'd have to be massive, you couldn't hide that on Earth, someone would notice a big fortress with women only in it."
hi "อันนี้บ้าละ ไม่มีมั้ง ไอ้ฐานปฏิบัติการลับพิเศษสตรีนิยมอะไรนั่นน่ะ แถมจะซ่อนตัวยังไงวะ หมายถึงแบบ ถ้าแบบนั้นแม่ง\nจะต้องใหญ่มาก ๆ ซึ่งไม่น่าซ่อนบนโลกได้อยู่ละ มันก็ต้องมีคนเห็นไอ้ปราการที่มีแต่ผู้หญิงที่ว่าบ้างแหละ"

show kenji happy_naked
with charachange

# ke "Who said it was on Earth?"
ke "แล้วใครบอกว่าอยู่บนโลก"

# "I turn away from Kenji and start practicing frowning faces in a mirror so that I can figure out what kind of frown will best express my emotions. He can't see me from this distance anyway."
"ฉันเบือนหน้าหนีจากเคนจิแล้วลองทำหน้าบึ้งในกระจกเพื่อหาว่าทำหน้าแบบจะตรงกับอารมณ์ตอนนี้ที่สุด แต่ยังไงอยู่ระยะนี้\nเขาคงไม่เห็นหรอก"

# "Which, unfortunately, means that he just keeps on ranting without any regard to sense or sensibility."
"ซึ่งก็แย่หน่อยตรงที่หมายความว่าเขาจะพล่ามไปเรื่อย ๆ โดยไม่สนสี่สนแปดใด ๆ "

show kenji tsun_naked
with charachange

# ke "Yeah, there is a war going on. A war not many know about, but it's a great one that will one day boil over, and encompass all of the known world. Then, we will have to pick sides. We will have to make a stand. In fact, it's happening right now."
ke "นั่นแหละ ตอนนี้มีสงครามที่กำลังดำเนินอยู่ สงครามที่น้อยคนนักที่จะรู้ แต่ก็เป็นสงครามครั้งใหญ่ที่สักวันจะปะทุขึ้นมา\nแล้วจะแพร่ไปทั่วโลก จากนั้นพวกเราก็ต้องเลือกฝั่งแสดงจุดยืนของตัวเอง เอาจริง ๆ สงครามนั้นกำลังเกิดขึ้น\n ณ ตอนนี้เลย"

# ke "Imagine it, the bloody battlefield. A vicious conflict without end."
ke "คิดดูดิ สนามรบที่นองเลือด ความขัดแย้งอันรุนแรงไร้ที่สิ้นสุด"

# ke "I almost gave up, when I thought this cause was silly… When I grew tired of the bleakness of our fight… When I mistook the time the power went out for a feminist raid and thought the end was near…"
ke "ฉันเกือบที่จะยอมแพ้ละตอนที่คิดว่ามันช่างไร้สาระสิ้นดี… ตอนที่ฉันเริ่มเบื่อกับสิ้นหวังในการต่อสู้ของพวกเรา… ตอนที่ฉัน\nเข้าใจผิดตอนที่ไฟดับว่าพวกสตรีนิยมได้บุกเข้ามาและทุกอย่างใกล้จบสิ้นแล้ว…"

# ke "But then I realized that if I gave up, it would all be over, and I was like, “whoa” and knew I had to get serious. Because I am the last sane man in an insane world. It's about duty."
ke "แล้วฉันก็นึกขึ้นได้ว่า ถ้าฉันยอมแพ้ละก็ทุกอย่างก็คงจบสิ้น แล้วฉันก็คิดแบบว่า “โอ้” และก็รู้ตัวว่าจะต้องจริงจังแล้ว\nเพราะฉันนี่แหละคือคนปกติคนสุดท้ายบนโลกที่ไม่ปกติใบนี้ มันเป็นหน้าที่น่ะ"

# hi "Must be a pretty crappy movement if it all hinges on one naked guy, ranting in a bathroom at another naked guy."
hi "เกือบดีละ ถ้าไม่ติดว่าแผนที่ว่าต้องฝากหน้าที่ให้ชายเปลือยท่านนึงที่ยืนพล่ามในห้องน้ำให้กับชายเปลือยอีกท่านอะนะ"

show kenji neutral_naked
with charachange

# ke "So can I have the money?"
ke "แล้วเออ ขอยืมเงินได้ปะ"

# "He's blocking the way out, it's getting cold because I'm still naked, and I want to go to class, so I agree to spot him the money."
"เขายืนขวางทางออก ตอนนี้เริ่มหนาวเพราะว่าฉันเปลือยอยู่ แถมอยากไปเข้าเรียนแล้วด้วย ฉันเลยให้ยืมไป"

show kenji happy_naked
with charachange

# ke "Awesome. Thanks, dude. We should go bowling later on."
ke "เจ๋ง ขอบใจมากพวก วันหลังไปเล่นโบว์ลิงกัน"

# hi "Bowling?"
hi "โบว์ลิง?"

# ke "Yeah, it's the ultimate sport. There are almost no women bowlers either, making it also the manliest sport."
ke "เออ เป็นสุดยอดกีฬา ที่ผ่านมาแทบไม่มีคนเล่นที่เป็นผู้หญิงเลยด้วย เลยเป็นกีฬาของยอดชายเลยเชียว"

# ke "Should I wear my pink bowling shirt with matching shoes or the pastel green with flower accents?"
ke "เสื้อโบว์ลิงเอาเป็นตัวสีชมพูที่มีรองเท้าเข้าคู่หรือตัวสีเขียวพาสเทลลายดอกดี"

# hi "There are bowling clothes?"
hi "มันมีเสื้อที่เอาไว้เล่นโบว์ลิงด้วยเรอะ"

show kenji neutral_naked
with charachange

# ke "Maybe."
ke "น่าจะแหละ"

# hi "Anyway, you had better pay me back."
hi "เอาเหอะ คืนเงินด้วย"

# ke "I can pay you back in stuff, right?"
ke "คืนเป็นของอย่างอื่นได้ใช่ไหม"

# "I don't have the time to ask him to elaborate on what that means."
"ฉันไม่มีเวลาจะมานั่งให้เขาอธิบายต่อแล้วว่าหมายความว่าไง"

# hi "I don't know. I have to get to class, you're kind of in the way."
hi "ไม่รู้ดิ เดี๋ยวต้องไปเรียนละ แล้วนายก็ขวางทางอยู่"

show kenji tsun_naked
with charachange

# ke "Oh. Sorry. Yeah, I don't want to hold you up, and I have some stuff to do myself. The time has come."
ke "โอ๊ะโทษที เอ้อ ไม่ได้ตั้งใจจะรั้งนายไว้ เดี๋ยวฉันก็ไปทำธุระของฉันละ ถึงเวลาแล้ว"

# hi "The time for what?"
hi "ถึงเวลาอะไรวะ"

show kenji happy_naked
with charachange

# ke "I just like saying that."
ke "พูดไปงั้นแหละ"

# ke "Okay, now the time has really come."
ke "โอเค ตอนนี้ถึงเวลาจริง ๆ ละ"

# hi "For what?"
hi "เวลาอะไร"

show kenji tsun_naked
with charachange

# ke "I have to use the bathroom. Get out of it."
ke "ฉันจะใช้ห้องน้ำ ออกไปได้แล้ว"

# hi "I was just going to! And what does that mean? It's a big bathroom."
hi "ก็กำลังจะไปเนี่ย! แล้วหมายความว่าไงเมื่อกี้ ห้องน้ำมีที่เยอะแยะ"

# ke "So? I have to be alone or I can't go. The pressure…"
ke "แล้วไง ฉันจะอาบคนเดียว ไม่งั้นฉันอาบไม่ได้ รู้สึกกดดันเกิน…"

# hi "Okay. What if someone else comes in?"
hi "โอเค แล้วถ้าคนอื่นเข้ามา?"

ke "…"

# ke "I'll think of something."
ke "ไว้ค่อยคิดละกัน"

# "I give him my practiced frown and it looks kind of silly reflected in his glasses. He either doesn't notice or doesn't see, anyway, so I get dressed and run back to my room, feeling as though an eternity has passed since I woke up."
"ฉันทำหน้าบึ้งที่ซ้อมหน้ากระจกเมื่อกี้ ซึ่งเงาสะท้อนหน้าฉันผ่านแว่นเขาดูตลกมาก เขาดูไม่สนใจ หรืออาจจะแค่\nมองไม่เห็น ยังไงก็ช่าง ฉันออกมาแต่งตัวแล้วเดินกลับห้อง รู้สึกเหมือนเวลาผ่านไปยาวนานเหลือเกินนับตั้งแต่ตอนตื่นมา" 

stop music fadeout 2.0

scene bg school_dormhisao
with locationskip

# "That is time I will never get back. I'll get him for this somehow."
"และนั่นคือเวลาที่เสียไปและไม่มีทางได้คืนมา สักวันเดี๋ยวฉันเอาคืนเขาแน่"

# "But right now, I have to get to class."
"แต่ตอนนี้ฉันต้องไปเข้าเรียนก่อน"



#*****************************************

label th_A21:    

scene bg school_scienceroom
with locationskip

play music music_normal fadein 2.0

# "I'm the first person in class today, although I think I'm a little too early. Then again, sitting alone here for twenty minutes sure beats having to suffer that time with Kenji."
"วันนี้เป็นวันที่ฉันมาถึงห้องคนแรก ถึงแม้ว่าจะเช้าไปหน่อยก็เถอะ แต่อย่างน้อยนั่งในนี้คนเดียวสัก 20 นาทีก็ยังดีกว่าต้อง\nทนทุกข์ทรมานกับเคนจิละนะ"

# "The combination of fatigue, frustration and boredom starts making me feel very tired."
"ความอ่อนล้า หงุดหงิด และเบื่อหน่ายได้หลอมรวมกันทำให้ฉันรู้สึกเพลียมาก ๆ"

# "I black out for a second, waking up when my head hits the surface of my desk. Rubbing my forehead, I realize this is as good a reason as any to stay up for now and stop coming to class so early later."
"ฉับวูบหลับไปแวบนึงแล้วสะดุ้งตื่นตอนที่หัวชนโต๊ะ ฉันเอามือกุมหน้าผากพร้อมเข้าใจว่าทำไมถึงควรจะนอนดึกและไม่ควรรีบมา\nเช้าจนเกินไป"

# "Eventually, I hear a tapping noise outside in the hallway, and Lilly's tall figure appears in the doorway. She's not in this class, so she must have some other business. Maybe she's looking for Hanako."
"จนในที่สุดก็ได้ยินเสียงเคาะดังมาจากข้างนอกที่โถงทางเดิน แล้วร่างสูงของลิลลี่ก็ปรากฏตรงหน้าประตูทางเข้า เธอไม่ได้\nเรียนที่ห้องนี้ เพราะงั้นคงจะมาด้วยเหตุผลอื่นมากกว่า อาจจะมาตามหาฮานาโกะ"

# "Lilly stops at the door, looking hesitant as if she was a vampire who can't come in unless invited. I consider doing so because she looks rather lonesome standing there."
"ลิลลี่หยุดยืนตรงหน้าประตู ดูลังเลที่จะเข้ามาเหมือนกับแขกที่รอให้เจ้าภาพเชิญก่อนถึงจะเข้างาน ฉันนึกจะเรียกเข้ามา\nเพราะเห็นท่าทีเธอยืนดูเหงา ๆ "

# "She steps in on her own accord though, after straightening her skirt and shirt collar as if it was of importance to look prim when entering our classroom." 
"สุดท้ายเธอก็เดินเข้ามาเองหลังจากที่จัดเสื้อและกระโปรงให้เรียบร้อยราวกับต้องทำตัวให้ดูดีก่อนเข้าห้องนี้"

show lilly cane_concerned at left
with charamoveinleft

# li "Excuse me."
li "ขอโทษนะคะ"

# "She calls into the quiet classroom with a probing, delicate voice. I realize the silence might unnerve her because of her blindness so I break it."
"เธอพูดเข้ามาในห้องที่เงียบสนิทด้วยน้ำเสียงอันนุ่มนวลที่รอการตอบกลับ ฉันนึกขึ้นได้ว่าความเงียบคงทำให้เธอรู้สึก\nไม่สบายใจเพราะว่าเธอตาบอด เช่นนั้นฉันจึงทำลายความเงียบลง"

# hi "Good morning, Lilly."
hi "อรุณสวัสดิ์ ลิลลี่"

show lilly cane_surprised at left
with charachange

show lilly cane_surprised at center
show bg school_scienceroom at bgright
with charamove

# li "Hisao? Good morning. I didn't hear you come in."
li "ฮิซาโอะเหรอ อรุณสวัสดิ์จ้ะ ไม่ได้ยินเลยว่าเธอก็เดินมาด้วย"

# "I wonder if she thinks it's suspicious I didn't say anything to her before. It's likely. If I were to tell too big a lie now, it would sink me."
"ฉันนึกอยากรู้ว่าเธอจะคิดว่ามันน่าสงสัยไหมที่ฉันไม่พูดอะไรกับเธอเลยตลอดทางที่ผ่านมา น่าจะคิดงั้นแหละ ถ้าโกหกไป\nเธอคงจับได้อยู่แล้ว"

# hi "Well, I was already here, just asleep until now."
hi "ก็จริง ๆ ฉันมาถึงนี่ตั้งแต่แรกแล้วละ เพิ่งงีบไปจนตะกี้"

show lilly cane_listen
with charachange

# li "Oh. Have you seen Hanako today, by any chance?"
li "โอ้ แล้ววันนี้เธอเห็นฮานาโกะบ้างไหมจ๊ะ"

# hi "No, she seems to come in only just before the bells ring… or after that. Do you want me to tell her something for you?"
hi "ไม่เห็นเลย ปกติเห็นเธอจะมาช่วงก่อนระฆังเข้าคาบดังไม่นาน… หรือไม่ก็มาหลังจากนั้น อยากจะฝากฉันบอกอะไรให้เธอ\nไหมล่ะ?"

show lilly cane_weaksmile
with charachange

# li "No, it's fine. It's strange, but I think we're the only two people in the school right now. I didn't hear anyone else on my way here."
li "ไม่เป็นไรหรอกจ้ะ แต่แปลกจริง รู้สึกเหมือนตอนนี้โรงเรียนจะมีแค่เราสองคนเลย ฉันไม่ได้ยินเสียงใครระหว่างเดินมา\nที่นี่เลย"

# hi "I shouldn't have gotten up so early today, I guess."
hi "ฉันว่าวันนี้ฉันไม่น่ารีบตื่นเลย"

show lilly cane_smile
with charachange

# li "You're chastising yourself for doing something that other people should? Punctuality is a good thing. I think so, anyway."
li "เธอกำลังตำหนิตัวเองกับเรื่องที่ทุก ๆ คนควรทำอยู่นะ ฉันว่าการตรงต่อเวลาเป็นเรื่องที่ดีนะ"

show lilly cane_concerned
with charachange

# li "It's a very busy morning today. The festival is coming up soon, and today is the deadline for event registration, budget reports, and any other official paperwork."
li "วันนี้เป็นวันที่ช่วงเช้ายุ่งน่าดู งานเทศกาลก็กำลังจะมาถึงแล้ว วันนี้ก็เป็นวันที่จะต้องลงทะเบียนกิจกรรม ส่งรายงาน\nงบประมาณ แล้วก็เอกสารของงานโรงเรียนอื่น ๆ ด้วยน่ะจ้ะ"

show lilly cane_weaksmile
with charachange

# li "It could be that everyone is trying to complete the necessary forms at the last minute. Maybe that is why it's so quiet today."
li "วันนี้น่าจะเงียบเพราะทุกคนคงกำลังเร่งทำเอกสารที่ต้องส่งกันให้ทันเอาตอนใกล้กำหนดส่งกันน่ะจ้ะ"

play sound sfx_doorslam

show lilly cane_surprised
with vpunch

# mi "Hi~ hi~!"
mi "หวัด~ ดีจ้า~!"

show shizu behind_blank at offscreenright
show misha hips_grin at offscreenright
with None

show lilly cane_surprised at left
show misha hips_grin at center
show shizu behind_blank at right
show bg school_scienceroom at bgleft
with charamove

hide misha
show misha hips_grin behind shizu
with None

# "Misha pops into the room with Shizune as if on cue, shouting with a loudness that makes Lilly visibly flinch."
"มิช่าโผล่เข้ามาในห้องพร้อมกับชิซูเนะราวกับฟ้าสั่งมา ตะโกนลั่นห้องจนลิลลี่สะดุ้งอย่างเห็นได้ชัด"

show misha hips_smile
with charachange

# mi "Hi, Hicchan~!"
mi "ดีจ้า ฮิจัง~!"

# hi "Hi."
hi "หวัดดี"

show shizu behind_smile
with charachange

shi "…"

show misha hips_grin
with charachange

# mi "Look, it's the class representative~! Hello~!"
mi "ดูสิ นั่นคุณหัวหน้าห้องล่ะ~! หวัดดีจ้า~!"

show lilly cane_smile
with charachange

# "Lilly smiles, probably amused by Misha's - or Shizune's - use of the word “look.”"
"ลิลลี่ยิ้ม อาจจะเพราะแอบขำที่มิช่า—หรือชิซูเนะ—ใช้คำว่า “ดู”"

show lilly cane_smile
with charachange

# li "Good morning."
li "อรุณสวัสดิ์จ้ะ"

show shizu adjust_smug
with charachange

shi "…"

show misha cross_smile
with charachange

# mi "Of course, you're not the representative of this class, right, right~?"
mi "แน่นอนว่า เธอไม่ใช่หัวหน้าห้องของห้องนี้สินะ ใช่ไหม ใช่ไหม~?"

show lilly cane_weaksmile
with charachange

# li "I'm not."
li "อืม ไม่ใช่"

# "Lilly seems a little more guarded in her answers to Shizune than she was with me the other day. I guess they really don't get along at all."
"ลิลลี่ดูระมัดระวังในคำตอบของเธอที่ตอบชิซูเนะมากกว่าตอนที่เธอตอบฉันเมื่อวันก่อน เดาว่าทั้งคู่คงจะไม่ถูกกันสักเท่าไหร่\nจริง ๆ นั่นแหละ"

# "Then I realize that Lilly might actually not know Shizune is present and she's trying to detect whether or not she is, to know who she is talking to."
"แล้วก็นึกขึ้นได้ว่าลิลลี่อาจจะไม่รู้ว่าชิซูเนะอยู่ตรงนี้เลยพยายามจับทางว่าเธออยู่หรือเปล่า เพื่อจะได้รู้ว่ากำลังคุยกับใครอยู่"

# "For all she knows, she's talking to Misha, but knowing that she and Shizune are practically inseparable, she might expect Shizune being the one that actually “talks.”"
"ตอนนี้ที่เธอรู้ คือเธอกำลังคุยกับมิช่าอยู่ แต่ว่าก็รู้ว่ามิช่ากับชิซูเนะเองก็ตัวแทบติดกัน เธอน่าจะคาดว่าคนที่ “พูด” อยู่\nคือชิซูเนะ"

# "Damn, how complicated. I decide to help Lilly out, for my own peace of mind more than anything else."
"แม่ง ซับซ้อนจังวะ ฉันเลือกที่จะช่วยลิลลี่เพราะฉันเองก็จะได้ไม่ต้องปวดหัว"

# hi "You're here early, Shizune."
hi "มาเช้าจังเลยนะชิซูเนะ"

show shizu basic_angry
with charachange

shi "…"

show misha hips_frown
with charachange

# mi "You were here even earlier than us!"
mi "นายมาเร็วกว่าพวกฉันอีกนะ!"

# "Misha puffs out her cheeks angrily. Why is she getting angry? Does she feel emotions on Shizune's behalf, too?"
"มิช่าทำแก้มป่องด้วยความโกรธ ทำไมเธอถึงต้องโกรธด้วยล่ะ ได้รับอารมณ์แบ่งมาจากชิซูเนะด้วยหรือไง"

# "It's not that weird, though, that Shizune didn't like my little comment. It's true, I was here earlier than them, so me saying something like that could definitely be misinterpreted as anything."
"แต่ก็ไม่แปลกหรอกที่ชิซูเนะจะไม่ค่อยชอบคำชมฉัน ก็นะ ในเมื่อฉันมาถึงก่อน การฉันที่พูดว่ามาเร็วก็อาจจะทำให้เกิดการ\nเข้าใจผิดได้ไปเป็นร้อยแปด"

# "Especially to Shizune, who doesn't have the benefit of hearing tone to gauge intent."
"โดยเฉพาะกับชิซูเนะที่ไม่สามารถฟังโทนน้ำเสียงได้"

# "Before I can start weighing whether or not I should apologize, Shizune has already moved on."
"ก่อนที่จะทันคิดว่าจะขอโทษดีไหม ชิซูเนะก็เลิกคิดเรื่องนั้นแล้ว"

show shizu adjust_smug
with charachange

shi "…"

show misha hips_smile
with charachange

# mi "Class rep~! It's a good thing you're here~! We have to talk."
mi "คุณหัวหน้า~! มาก็ดีแล้ว~! เราต้องคุยกันหน่อยนะ"

show shizu behind_frown
with charachange

shi "…"

show misha hips_grin
with charachange

# mi "The festival is coming up in three days, right? Every other class has already handed in their projected budget reports for their events! Even the first-years! Except you~!"
mi "งานเทศกาลจะจัดในอีกสามวันแล้วนะ ห้องอื่น ๆ เขาก็ส่งใบรายงานงบประมาณสำหรับกิจกรรมกันหมดแล้วนะ! แม้แต่\nเด็ก ม. 4 ก็ส่งแล้ว! เหลือแค่เธอแล้วนะ~!"

show misha cross_laugh
with charachange

# mi "Wahaha~!"
mi "วะฮ่าฮ่า~!"

show lilly cane_surprised
with charachange

# li "There is still time to hand it in, isn't there?"
li "ก็ยังมีเวลาให้ส่งอยู่ใช่ไหม"

stop music fadeout 2.0

show shizu cross_angry
with charachange

shi "…"

show misha cross_frown
with charachange

# mi "Today! The deadline is today! You're certainly taking your time, aren't you? If I had it my way, I'd have had all of the necessary paperwork days ago, but someone~! had to say “the deadline, please extend it~!”"
mi "วันนี้! กำหนดส่งคือวันนี้! เธอนี่ก็ใช้เวลาเยอะพอตัวเลยนี่นะ ถ้าเป็นฉันละก็ฉันคงจะจัดการเอกสารสำคัญ ๆ เสร็จตั้งแต่\nวันก่อน ๆ แล้ว แต่บางคน~! ก็มาบอกว่า “ขอเลื่อนวันส่งได้ไหม~!”"

show lilly cane_displeased
with charachange

# li "Yes, that was me. Planning something on this scale is not a small task, and a week is too small a time frame to expect a whole class to work out such a complex issue completely."
li "อืม ฉันเองแหละ แต่การวางแผนกับงานขนาดใหญ่ขนาดนี้ไม่ใช่เรื่องเล็ก ๆ เลยนะ จะมาคาดหวังให้คนทั้งห้องมาช่วย\nจัดการเรื่องยุ่งยากขนาดนี้ภายในสัปดาห์เดียวไม่ได้หรอก"

show shizu adjust_angry
with charachange

shi "…"

show misha hips_frown
with charachange

# mi "Do you want to know what's harder than distributing the funds for one class' event? Handling the same matter for every class in the school and then some~! The one who does that is me!"
mi "อยากรู้รึเปล่าว่าอะไรยากกว่าการจัดแจงงบประมาณกิจกรรมของห้องเรียนหนึ่งห้อง ก็การจัดแจงของทุกห้องในโรงเรียนไง\nแล้ว~! คนที่ต้องจัดการเรื่องนั้นก็คือฉันไงล่ะ!"

# "Misha puts her hands on her hips and stands up straight. Wow, she is really getting into the role. Lilly doesn't look like she's very amused, though."
"มิช่าทำท่าเท้าเอวแล้วยืนตัวตรง โอ้ ตอนนี้เธอสวมบทบาทได้เหมือนเลยทีเดียว แต่ลิลลี่ก็ดูไม่ได้เล่นด้วย"

# hi "Hey, Shizune, aren't you being a little too hard on her? There's still a whole day left."
hi "นี่ชิซูเนะ แบบนี้ก็เคร่งไปหน่อยมั้ง ยังเหลือเวลาอีกทั้งวันนี่"

show lilly cane_weaksmile
with charachange

# li "Please, Hisao. It's all right."
li "เอาเถอะฮิซาโอะ ไม่เป็นไรหรอกจ้ะ"

# "Lilly seems happy I'm taking her side, but a bit conflicted that I might not think she can take care of herself."
"ลิลลี่ดูดีใจที่ฉันเข้าข้างเธอ แต่ฉันก็ยังรู้สึกว่าเธอไม่น่าไหวอยู่ดี"

show lilly cane_listen
with charachange

# li "If this is about the budget, then I'm disappointed you think I have forgotten about it. I understand how important it is."
li "ถ้าเป็นเรื่องงบประมาณละก็ ฉันผิดหวังนะที่เธอคิดว่าฉันลืมเรื่องนั้นไป ฉันรู้หรอกว่าเป็นเรื่องที่สำคัญขนาดไหน"

show shizu behind_frustrated
with charachange

shi "…"

show misha hips_grin
with charachange

# mi "Then~! Can I have it, please?"
mi "งั้น~! ช่วยส่งมาให้หน่อยได้ไหม"

# hi "Shizune, she might not have it on her at this exact second."
hi "ชิซูเนะ เธอคงไม่ได้หยิบติดมือมาด้วยหรอก"

show lilly cane_displeased
with charachange

# li "It's not here right now. I asked two students to take care of it for me. Students from my class."
li "เอกสารยังไม่ได้อยู่ที่นี่หรอก ฉันให้นักเรียนสองคนในห้องไปจัดการอยู่ นักเรียนจากห้องฉันน่ะนะ"

# "She emphasizes the last sentence much to my surprise. She knows about Shizune and Misha's efforts to rope me into the Student Council?"
"เธอเน้นย้ำคำสุดท้ายจนน่าแปลกใจ นี่เธอรู้เรื่องที่ว่าชิซูเนะกับมิช่าพยายามพาฉันเข้าสภานักเรียนด้วยงั้นเหรอ"

# "I guess word must've gotten around, so now she's using me as ammo against Shizune. This just gets better and better…"
"คาดว่าข่าวลือคงแพร่กระจายไปทั่วแล้ว ตอนนี้เธอเลยเอามาเป็นอาวุธใช้เถียงกับชิซูเนะ ชักน่าสนใจแล้วสิ…"

show shizu cross_angry
with charachange

shi "…"

show misha hips_frown
with charachange

# mi "It was your responsibility~! A budget report isn't something you should just be delegating away; as class rep, it's your job to be on top of things! This kind of disregard for proper procedure is really just terrible~!"
mi "นั่นน่ะเป็นความรับผิดชอบของเธอนะ~! รายงานงบประมาณน่ะไม่ใช่อะไรที่เธอจะเอาไปให้คนอื่นมาทำแทนให้ได้นะ\nในฐานะหัวหน้าห้องมันคือหน้าที่ของเธอที่จะจัดการทุก ๆ อย่าง การที่ละเลยไม่ทำตามขั้นตอนที่ถูกต้องเนี่ยถือว่า\nใช้ไม่ได้เลยนะ~!"

show lilly cane_listen
with charachange

# li "They completed it, being capable of doing so, but the students have been sick recently, so they could not come to school and give it back to me. If you want, I will apologize on their behalf for getting sick."
li "ก็พวกเขาทำได้ แล้วก็ทำเสร็จแล้วด้วย แต่ช่วงนี้นักเรียนพวกนั้นไม่ค่อยสบาย เพราะงั้นแล้วพวกเขาเลยมาส่งให้ฉัน\nที่โรงเรียนไม่ได้ ถ้าเธออยากให้ฉันขอโทษ ฉันก็ขอโทษแล้วกันนะที่พวกเขาป่วยตอนนี้น่ะ"

show misha hips_grin
with charachange

# mi "Okay~!"
mi "โอเคจ้า~!"

# "Although Misha misses Lilly's little jab entirely, Shizune doesn't, and she seems torn between being offended by Lilly's daring and jumping for joy at the prospect of a challenge."
"ถึงมิช่าจะไม่รู้เลยว่าเมื่อกี้ลิลลี่แอบพูดกระแนะกระแหนอยู่ แต่ชิซูเนะรู้ และเธอก็ดูย้อนแย้งในตัวเองระหว่างอารมณ์เคือง\nที่โดนลิลลี่จิกกัดกับอารมณ์ตื่นเต้นที่ได้รับคำท้า"

show shizu behind_frown
with charachange

shi "…"

show misha hips_smile
with charachange

# mi "Lilly, don't they live here at the school? That's a five minute walk, you know~."
mi "ลิลลี่ แล้วนักเรียนพวกนั้นก็พักอยู่ในโรงเรียนนี้ไม่ใช่หรือไง เดินไป 5 นาทีก็ถึงแล้วนี่~"

# mi "What could they possibly have that prevents them from taking five minutes out of their busy lives… to drop off something that will affect the enjoyment of their entire class?"
mi "จะต้องยุ่งขนาดไหนกันนะที่ทำให้ไม่ว่างจนสละเวลาให้สัก 5 นาทีไม่ได้… จนต้องทิ้งภาระบางอย่างที่ทำให้คนอื่นเดือดร้อน\nทั้งห้องน่ะ"

show shizu adjust_angry
with charachange

# "Lilly opens her mouth to say something, but Shizune closes the gap between them and starts signing furiously, waving her hands around like an orchestra conductor."
"ลิลลี่อ้าปากเพื่อจะพูดอะไรบางอย่าง แต่ชิซูเนะก็เข้ามาขัดแล้วเริ่มทำภาษามืออย่างรวดเร็ว โบกมือไปมาราวกับวาทยกรประจำ\nวงออเคสตรา"

# "Misha tries her best to convey the same passion, but can't seem to lose her normal cheerful tone. The result is interesting and somewhat surreal."
"มิช่าพยายามอย่างที่สุดเพื่อจะสื่ออารมณ์เดียวกันนั้น แต่ก็ดูทีท่าว่าจะไม่สามารถลดน้ำเสียงร่าเริงนั้นได้เลย ผลที่ออกมา\nนั้นน่าทั้งสนใจและหลอน ๆ กันทีเดียว"

shi "…"

show misha cross_frown
with charachange

# mi "And what's with that attitude~? I said that it's not something you should be delegating away; are you the class representative or aren't you?"
mi "แล้วทำตัวแบบนี้คืออะไร~ ฉันบอกแล้วนี่ว่างานนี้ไม่ใช่ว่าให้ใครก็ได้มาทำ นี่เธอเป็นหัวหน้าห้องจริงปะเนี่ย"

show misha hips_frown
with charachange

# mi "Tell me the names of those two students, they should have your job if you can't even handle something this simple yourself."
mi "ไหนบอกชื่อนักเรียนสองคนนั้นมาทีซิ พวกเขาเหมาะกับตำแหน่งหัวหน้ากว่าเธออีกถ้าเธอยังจัดการเรื่องง่าย ๆ แค่นี้ไม่ได้"

show lilly cane_displeased
with charachange

# li "One form isn't the full extent of what I am supposed to take care of."
li "แค่งานเดียวนั่นไม่เทียบเท่างานที่ฉันจะต้องดูแลทั้งหมดซะหน่อย"

# "Lilly's tone is growing slightly impatient, but she is doing a good job of not letting Shizune see how unsettled she is becoming. She's playing her cards close to her chest."
"น้ำเสียงของลิลลี่เริ่มแสดงออกถึงความขุ่นเคืองเล็กน้อย แต่เธอก็แสดงออกได้ดีโดยการที่ไม่ทำให้ชิซูเนะรู้ว่าเธอเริ่มเคือง\nและยังเก็บซ่อนอารมณ์เธอไว้อยู่"

# "Shizune, on the other hand, wraps her fingers cheerfully along the edge of her glasses, knowing Lilly can neither hear nor see how excited she is."
"ในขณะที่ชิซูเนะเองนั้น ทำไม้ทำมือไปตามกรอบแว่นอย่างร่าเริง เพราะรู้ว่าลิลลี่ไม่ได้ยินและไม่เห็นว่าเธอตื่นเต้นแค่ไหน"

show shizu adjust_smug
with charachange

shi "…"

show misha hips_grin
with charachange

# mi "Of course, you do so much, class rep~! It must be so difficult being you~!"
mi "คุณหัวหน้าทำงานหนักจังเลยเนอะ~! เป็นเธอนี่ลำบากจริงเลยนะ~!"

show lilly cane_listen
with charachange

# "Lilly tightens her lips at Misha's words, clearly understanding the intent behind them even though Misha delivers them without even a hint of the sarcasm which they were meant to have."
"ลิลลี่กัดปากเมื่อได้ยินคำพูดของมิช่า บ่งบอกได้ว่าเธอเข้าใจถึงความหมายเบื้องหลังของคำพูดทั้งหมดที่แม้ตัวมิช่าที่เป็นคน\nพูดแทนนั้นไม่ได้เข้าใจเนื้อหาที่เสียดสีที่ซ่อนอยู่ในคำพูดนั้นเลย"

# "Shizune and Lilly don't like each other, that much is clear, but this seems a little much. It seems like Lilly has had enough and is ready to push back."
"เป็นที่แน่ชัดว่าชิซูเนะกับลิลลี่นั้นไม่ชอบหน้ากัน แต่ตอนนี้ก็ดูจะเลยเถิดไปหน่อย ลิลลี่เองก็ดูพร้อมที่จะสวนกลับแล้ว"

play music music_tension

$ wdt_off(False)

scene black
with Dissolve(0.2)

show showdown_lilly_slice at Transform(xanchor=0.0, xpos=1.0, yalign=0.0)
show showdown_shizu_slice at Transform(xanchor=1.0, xpos=0.0, yalign=1.0)
with None

play sound sfx_draw
show showdown_lilly_slice at Transform(xalign=0.0, yalign=0.0)
with slice_in

with Pause(0.2)

play sound sfx_draw
show showdown_shizu_slice at Transform(xalign=1.0, yalign=1.0)
with slice_in

with Pause(0.2)

play sound sfx_thunder
scene ev showdown
with Fade(0.2, 0.0, 3.0, color="#FFF")


play sound sfx_slide2
show ev showdown_large:
    size (800,600) crop (0, 0, 2400, 1800) subpixel True
    easeout 0.2 crop (280, 100, 800, 600)
with None

window show


# li "I was actually just discussing the budget report before you came by. You must be very talented to have finished all your student council duties so quickly that you can track me down to make sure I don't forget my own."
li "ฉันก็คุยเรื่องงบประมาณไปแล้วก่อนเธอจะมาอีกนะ เธอคงจะเก่งมาก ๆ สินะ เลยสามารถรีบจัดการงานสภานักเรียน\nของเธอจนหมด เพื่อที่จะได้มาตามจี้ฉันเพื่อให้ฉันไม่ลืมเรื่องนี้น่ะ"

play sound sfx_slide
show ev showdown_large:
    ease 0.2 crop (1400,160, 800, 600)
with None

# mi "Are you accusing me of slacking off? It seems like you're confusing me with yourself~!"
mi "นี่เธอจะว่าฉันอู้งานมาเหรอ ดูท่าคงจะสับสนกับนิสัยตัวเองละมั้ง~!"

play sound sfx_slide2
show ev showdown_large:
    ease 0.2 crop (280,100, 800, 600)
with None

# li "I don't think so. That would be a very difficult thing for me to do; comparing myself to you."
li "ไม่หรอก ฉันว่าตัวฉันกับเธอเทียบกันไม่ติดนะ"


play sound sfx_slide2
show ev showdown_large:
    ease 0.2 crop (1400,160, 800, 600)
with None

# mi "You're right, the difference between us is like heaven and hell."
mi "ก็ถูก เธอกับฉันน่ะต่างกันราวกับฟ้ากับเหว"

play sound sfx_slide
show ev showdown_large:
    ease 0.2 crop (280,100, 800, 600)
with None

# li "And it's not hard to guess which one you might represent."
li "ก็รู้ ๆ กันอยู่ว่าใครฟ้าใครเหวอะนะ"

$ _window = False

play sound sfx_thunder
scene ev showdown
with Fade(0.2, 0.0, 1.5, color="#FFF")

window show

# "The air between them ripples with the heat of their enmity. Well, not really. They can't disguise it any more, though. Even Misha looks like she's beginning to understand the real nature of this conversation."
"บรรยากาศรอบ ๆ ทั้งคู่ดุเดือดจากรังสีความเป็นศัตรูกันของทั้งคู่ คือจริง ๆ ตอนนี้ก็ชัดเจนมากแล้วละนะ แม้แต่มิช่าเองก็เริ่ม\nจะเข้าใจแล้วว่าอารมณ์ของบทสนทนานี้เป็นยังไง"

stop music fadeout 5.0

scene bg school_scienceroom
show lilly cane_listen at left
show misha perky_confused at center
show shizu basic_angry at right
with flash

shi "…"

show misha sign_confused
with charachange

# mi "Hicchan~! Don't you slack off either~!"
mi "ฮิจัง~! นายเองก็อย่าอู้งานเชียวละ~!"

# hi "What are you talking about?"
hi "เธอพูดเรื่องอะไรเนี่ย"

show shizu basic_frown
with charachange

shi "…"

show misha hips_smile
with charachange

# mi "Aren't you taking part in the festival, Hicchan? You are, aren't you? Then~! I hope you're going to do a lot more to make sure it goes smoothly than this person~!"
mi "นายเองก็ร่วมงานเทศกาลด้วยไม่ใช่เหรอฮิจัง ใช่ไหมล่ะ เพราะงั้นแล้ว~! ฉันหวังว่านายจะทำงานมากกว่านี้เพื่อให้\nงานออกมาราบรื่นกว่าที่คนคนนี้ทำนะ~!"

label th_choiceA21:
menu:
    with menueffect
    
    # "I don't understand why Shizune is suddenly getting mad at me."
    "ไม่เข้าใจเลยว่าทำไมอยู่ ๆ ชิซูเนะถึงมาโมโหใส่ฉันเนี่ย"
    
    # "Don't drag me into this! I've done my part!":
    "อย่าลากฉันไปเกี่ยวสิ ฉันทำส่วนของฉันเสร็จแล้ว!":
        return m1

    # "Hey, come on. Cut me and Lilly some slack…":
    "นี่ ไม่เอาน่า เพลา ๆ ให้ฉันกับลิลลี่หน่อย…":
        return m2
        
label th_A21a:

# hi "Why am I being dragged into this, again? I've done more than enough, I think."
hi "ทำไมฉันถึงโดนลากมาเรื่องงานนี่อีกแล้วฮะ ฉันว่าฉันก็ทำมากเกินพอละนะ"

# hi "If you're angry with Lilly, that has nothing to do with me."
hi "ถ้าเธอจะโมโหลิลลี่ ก็ไม่เกี่ยวกับฉันสักหน่อย"

show lilly cane_reminisce
with charachange

# li "Now, wait just a second… are you implying the president is more right in scolding me than yourself?"
li "เดี๋ยวนะ นี่เธอจะบอกว่าคุณประธานนักเรียนมีสิทธิ์ด่าฉันได้แต่ด่าเธอไม่ได้เหรอ"

# "Ah damn, I think I could've worded that better."
"อ่า เชี่ย น่าจะเลือกใช้คำให้ดีกว่านี้"

# hi "No, I don't know about that but… I mean…"
hi "เปล่า ไม่ได้หมายความว่าแบบนั้น… แต่คือ…"

show shizu behind_frown
with charachange

shi "…"

show misha perky_confused
with charachange

# mi "What are you saying, Hicchan?"
mi "พูดอะไรน่ะฮิจัง"

# hi "It's just that I hardly think it's fair you can say that, seeing that I've helped you guys."
hi "แค่ฉันคิดว่าเธอจะพูดอย่างนั้นก็ไม่ถูก ฉันก็ช่วยพวกเธอแล้วนะ"

# "The mood has changed. This is like a showdown between two gunfighters now. Well, it was like that before too, but this time Shizune's focus is on me."
"สถานการณ์ตอนนี้เปลี่ยนไปแล้ว ตอนนี้เหมือนกับจังหวะของคาวบอยที่กำลังจะดวลปืนกันเลย จริง ๆ เมื่อกี้ก็เป็นแบบนี้\nนั่นแหละ เพียงแต่ตอนนี้ชิซูเนะหันปืนมาที่ฉันแทนแล้ว"

# "And so is Lilly's, though she keeps quiet. I'm afraid I inadvertently pissed her off."
"และลิลลี่ก็ด้วย ถึงตอนนี้เธอจะเงียบ แต่ฉันก็กลัวว่าฉันไปทำให้เธอโกรธโดยไม่ได้ตั้งใจ"

show shizu cross_angry
with charachange

shi "…"

show misha hips_frown
with charachange

# mi "Are you saying I'm wrong?"
mi "เธอจะบอกว่าฉันผิดเหรอ?"

# "What a dangerous situation."
"สถานการณ์อันตรายสุด ๆ"

# hi "It's too early to argue with you. …Yes, I think it's unfair of you to get on my case."
hi "ฉันยังไม่อยากมาเถียงกับเธอแต่เช้าเลยนะ …แต่ใช่ ฉันว่าเธอจะมาว่าฉันอย่างนี้มันก็ไม่ถูก"

show shizu behind_frustrated
with charachange

shi "…"

show misha hips_smile
with charachange

# mi "Hicchan, you want too much~! But~! You have a point. Okay, okay okay~! You're not lazy, Hicchan."
mi "ฮิจัง นายเรียกร้องมากไปนะ~! แต่~! ที่พูดมาก็มีเหตุผล โอเค โอเค โอเค~! ถือว่านายไม่ขี้เกียจก็ได้ฮิจัง"

show misha hips_laugh
with charachange

# mi "Hahaha~!"
mi "ฮ่าฮ่าฮ่า~!"

# "Shizune pushes her glasses up with her thumb, almost approvingly."
"ชิซูเนะดันแว่นขึ้นพร้อมยกนิ้วโป้งให้กึ่ง ๆ เห็นด้วย"

show shizu adjust_happy
with charachange

shi "…"

show misha perky_smile
with charachange

# mi "That's good! If you're not useless, you shouldn't let anyone say you are~! But the next time I say it, it'll really be because you are disappointing me like Miss Class Rep here, so don't let this go to your head!"
mi "ดีแล้วละ! ถ้านายไม่ไร้ประโยชน์ นายก็ไม่ควรให้ใครมาว่าแบบนั้น~! แต่ถ้าครั้งหน้าฉันได้ว่าอีกละก็ แปลว่าเธอทำให้ฉัน\nผิดหวังเหมือนกับคุณหัวหน้าตรงนี้ เพราะฉะนั้น อย่าเพิ่งได้ใจเลยเชียว"

show lilly cane_displeased
with charachange

# "Lilly takes the jab silently, a venomous visage frozen on her face."
"ลิลลี่คอยฟังคำจิกกัดนั้นเงียบ ๆ หน้าเธอชาอย่างสังเกตได้"

show misha hips_smile
with charachange

# mi "Class rep~! Shicchan says: “Don't forget that report, please~!”"
mi "คุณหัวหน้า~! ชิจังบอกว่า “อย่าลืมรายงานนั้นด้วยนะจ๊ะ~!”"

# li "I won't."
li "ฉันไม่ลืมหรอก"

show lilly cane_listen
with charachange

# li "Would that be all?"
li "แค่นี้ใช่ไหม?"

show misha hips_grin
with charachange

# mi "Yup~!"
mi "อื้ม~!"

# li "Then, good day to you all."
li "งั้น โชคดีทุกคน"

# "Her voice would cut the air of the classroom into half, if it was more tangible."
"ถ้าบรรยากาศในห้องเป็นอะไรที่จับต้องได้ เสียงของเธอคงเป็นตัวผ่ากลางแบ่งครึ่งแน่ ๆ "

hide lilly
with charaexit

# "Lilly leaves the room, understandably in a bad mood but still managing to be as poised and calm as usual."
"ลิลลี่ออกจากห้องไปด้วยอารมณ์ที่พอเข้าใจได้ว่าไม่ค่อยจะดีนัก แต่ก็ยังคงไว้ซึ่งความสงบและสุขุมอย่างปกติ"

show misha hips_grin at twoleft
show shizu adjust_happy at tworight
show bg school_scienceroom at bgleft
with charamove

# hi "Shizune, you really did go a little too far today."
hi "ชิซูเนะ เธอทำเกินไปหน่อยนะวันนี้"

show misha perky_smile
with charachange

# mi "It's true, Shicchan, just a little~."
mi "จริงเลย ชิจัง เกินไปนิดนึง~"

# "If I had been expecting Shizune to grudgingly admit I have a point there as well, I think I was expecting too much. She doesn't respond."
"ฉันคงคาดหวังมากไปถ้าจะให้ชิซูเนะจะยอมรับว่าฉันพูดถูกเหมือนกันอย่างไม่เต็มใจ ชิซูเนะนิ่งไม่ตอบอะไร"

show shizu basic_normal2
with charachange

shi "…"

show misha cross_laugh
with charachange

# mi "Hahaha~! Shicchan thinks you should mind your own business."
mi "ฮ่าฮ่าฮ่า~! ชิจังบอกว่านายไม่ต้องมายุ่งหรอก"

show misha hips_smile
with charachange

# mi "Hicchan, we have a few last minute things to take care of before class~! We might be late, so~! Can you please cover for us?"
mi "ฮิจัง พวกเรามีธุระนิดหน่อยที่ต้องทำก่อนเข้าคาบน่ะ~! แล้วก็อาจมาเข้าสาย เพราะงั้น~! ฝากบอกครูให้หน่อยนะ"

# hi "Yeah."
hi "อืม ๆ"

show misha cross_grin
with charachange

# mi "Perfect~! Yay~! Okay~! Thanks, Hicchan!"
mi "เพอร์เฟกต์~! เย้~! โอเค~! ขอบใจนะฮิจัง!"

hide misha
hide shizu
with charaexit

# "They walk outside even though there are only ten minutes left before the bell will ring, signaling the start of class."
"พวกเธอเดินออกห้องไปถึงแม้จะเหลือเวลาแค่สิบนาทีก่อนที่ระฆังเตือนเพื่อบอกเวลาเริ่มเรียนจะดัง"


label th_A21b:

# hi "Hey, I'm the new guy, remember?"
hi "นี่ ฉันเป็นเด็กใหม่นะ"

# hi "It's not like I could've done much, even if I wanted."
hi "ต่อให้อยากช่วยฉันก็ช่วยอะไรได้ไม่มากหรอก"

show lilly cane_displeased
with charachange

# li "That's right, you shouldn't expect a transfer student to jump right into it on his first week."
li "ใช่ เธอไม่ควรจะคาดหวังให้นักเรียนที่เพิ่งย้ายมาใหม่มาทำอะไรแบบนี้ตอนสัปดาห์แรกของเขาหรอกนะ"

# "Lilly taking my side feels oddly comforting so I decide to back her up too."
"การที่ลิลลี่เข้าข้างฉันทำให้ฉันรู้สึกสบายใจขึ้นมาหน่อย ฉันเลยว่าจะช่วยเธอด้วย"

# hi "Yeah you're being unreasonable with us both."
hi "ใช่ เธอน่ะทำตัวไร้เหตุผลกับพวกเราทั้งคู่อยู่นะ"

show shizu behind_frustrated
with charachange

shi "…"

show misha hips_frown
with charachange

# mi "Excuses, excuses. Miss Class Rep has had plenty of time to deal with her report."
mi "อ้างนู่นอ้างนี่ คุณหัวหน้าน่ะมีเวลาจัดการกับรายงานเหลือ ๆ เลยนะ"

# mi "And we repeatedly offered you a position to help with the student council work, but you refused to commit yourself to making the festival a success."
mi "แล้วพวกเราเองก็เสนอให้นายเข้ามาช่วยงานสภานักเรียนแล้ว แต่นายก็ปฏิเสธที่จะช่วยทุ่มเทอย่างเต็มที่เพื่อให้\nงานเทศกาลออกมาสำเร็จอย่างงดงาม"

# hi "Yeah, but as I said back then, I'm not sure if…"
hi "ก็ใช่ แต่ก็บอกไปแล้วไงว่าฉันยังไม่แน่ใจว่า…"

# "I don't have time for this right now; no matter what I do, it will mean being drawn into a confrontation with Shizune, and that is what she wants."
"ฉันไม่อยากจะมาเสียเวลากับอะไรอย่างนี้ตอนนี้ ไม่ว่าจะพูดอะไรฉันก็ต้องเผชิญหน้ากับชิซูเนะอยู่ดี ซึ่งนั่นเป็นสิ่งที่เธอ\nต้องการ"

# hi "Whatever. Forget it."
hi "เอาเหอะ ช่างมันเถอะ"


label th_A21c:

# "I turn my back at them."
"ฉันหันหลังให้พวกนั้น"

hide shizu
hide misha
with charaexit

show lilly cane_displeased at center
show bg school_scienceroom at bgright
with charamove

# hi "Lilly, class is going to be starting soon, so we can talk more later. I'll tell Hanako you were looking for her."
hi "ลิลลี่ ใกล้ได้เวลาเข้าเรียนแล้ว เดี๋ยวค่อยมาคุยทีหลังแล้วกัน เดี๋ยวฉันบอกฮานาโกะให้ว่าเธอมาหา"

# "I can feel Shizune freezing. Maybe this is the first time she has ever been ignored in such a blunt manner."
"ฉันรู้สึกได้ว่าชิซูเนะกำลังอึ้งไปอยู่ นี่คงเป็นครั้งแรกที่มีคนเมินเธอตรง ๆ แบบนี้"

show lilly cane_smile
with charachange

# li "Thank you, Hisao. I'll leave now, then."
li "ขอบคุณนะฮิซาโอะ งั้นฉันขอตัวกลับก่อนนะจ๊ะ"

# "She gives me the sweetest smile I've seen all week, and turns on her heels to make her exit."
"เธอส่งยิ้มที่หวานที่สุดที่ฉันเคยเห็นในสัปดาห์นี้ให้ฉัน แล้วหันหลังเดินออกไป"

hide lilly
with charaexit

# "As soon as Lilly walks out the door, I suddenly start feeling reluctant about turning to face Shizune."
"ทันทีที่ลิลลี่เดินออกจากประตูไป ฉันก็เริ่มลังเลที่จะหันหน้าหาชิซูเนะ"

# "I can feel her eyes burning into my back, and can't bring myself to look at her. She must be furious. I keep expecting Misha to say something to alleviate the tension, but it really is wanting too much."
"ฉันสัมผัสได้ถึงสายตาพิฆาตของชิซูเนะที่หลังฉันและไม่กล้าหันกลับไปมองเธอ เธอคงจะเดือดมากแน่ ๆ ฉันหวังว่ามิช่าจะพูด\nอะไรบางอย่างเพื่อลดทอนความตึงเครียดนี้ แต่เหมือนฉันจะหวังมากไป"

# "In the end, I go back to my seat and listen to the sound of Shizune's footsteps as she marches out of the room. She doesn't return until a few minutes before class."
"สุดท้ายฉันก็กลับไปนั่งที่ ฉันได้ยินเสียงที่ชิซูเนะเดินปึงปังออกไปจากห้อง เธอไม่กลับมาจนกระทั่งไม่กี่นาทีก่อนเข้าคาบ"


label th_A21d:

hide shizu
hide misha
hide lilly
with charaexit

# "I turn my back at them."
"ฉันหันหลังให้พวกนั้น"

# "I get back to my seat and shut my ears from the finale of the argument between Lilly and Shizune."
"ฉันกลับมานั่งที่แล้วไม่รับฟังอะไรอีกจากการเถียงกันของสองคนนั้น"

# "Eventually, Lilly leaves our classroom and Shizune and Misha seat themselves, without talking to me."
"ท้ายที่สุด ลิลลี่ก็ออกไปจากห้องเรียนของเราและชิซูเนะกับมิช่าก็เข้ามานั่งที่โดยไม่ได้คุยกับฉัน"

# "I can feel Shizune's eyes burning into my back. She is probably angry at me, but I'm just as angry with her."
"ฉันสัมผัสได้ถึงสายตาพิฆาตของชิซูเนะที่หลังฉัน เธอคงจะโกรธฉัน แต่ฉันเองก็โกรธเธอพอ ๆ กัน"

# "I don't get why she had to drag me into the argument."
"ไม่เข้าใจเลยว่าทำไมเธอต้องลากฉันเข้าไปเกี่ยวด้วย"



#*****************************

label th_A22:

scene bg school_scienceroom at bgleft
with shorttimeskip

play music music_daily fadein 0.5

# "Hanako doesn't come to the morning class at all, leaving her seat looking empty and lonely in the back of the classroom."
"และฮานาโกะก็ไม่ได้มาในคาบเช้าเลย ปล่อยให้ที่นั่งของเธอดูว่างเปล่าและเงียบเหงาอยู่ที่หลังห้องเรียน"

# "I have to tell her that Lilly was looking for her if I see her later."
"ถ้าได้เจอเธอคงต้องบอกว่าลิลลี่ตามหาเธออยู่"

# "After the events of this morning, class is pretty boring in comparison. I turn the pages of my textbook lazily."
"พอมีเรื่องเมื่อเช้าแล้วคาบเรียนนี่ก็ดูน่าเบื่อไปเลย ฉันเปิดหนังสือไปด้วยความยืดยาด"

# "We've been covering the same amount of pages each day, so reading ahead is more or less giving myself a preview of what tomorrow's lesson will be about."
"ในแต่ละวันจะเรียนเนื้อหาตามหนังสือด้วยปริมาณหน้าที่เท่า ๆ กัน การอ่านมาก่อนก็เป็นการได้ดูว่าพรุ่งนี้จะเรียนอะไรด้วย"

# "The clock at the front of the room sounds unbearably loud. The teacher hasn't said anything in over seven minutes, instead opting to cover the board in rows and rows of equations taken directly from the book."
"เสียงนาฬิกาที่ด้านหน้าห้องดังจนน่ารำคาญ ครูก็ไม่พูดอะไรเลยกว่าเจ็ดนาที แต่กลับเลือกที่จะเขียนสมการจากหนังสือบน\nกระดานจนเต็มไปหมด"

# "The rhythmic clashing of chalk on blackboard seems to synchronize perfectly with the ticking of the clock."
"เสียงกระทบของชอล์กกับกระดานนั้นดังประสานอย่างเป็นจังหวะไปพร้อมกับเสียงนาฬิกาเดิน"

show misha cross_smile_close at offscreenleft
with None

show misha cross_smile_close at Transform(xpos=0.1, xanchor=0.5)
show bg school_scienceroom at center
with charamove

# "I start to copy down the equations just to pass the time, not noticing Misha's head poking over my shoulder until she is almost on top of me."
"ฉันลอกสมการบนกระดานลงสมุดเพื่อฆ่าเวลา ไม่ได้รู้สึกตัวเลยว่ามิช่ายื่นหัวมาอยู่เหนือไหล่ฉันจนตอนเธอแทบจะ\nเอาคางมาเกยไหล่ฉันแล้ว"

# hi "What are you doing?"
hi "ทำอะไรน่ะ"

# "I try to strike a balance between being quiet enough to not draw attention to myself but loud enough to draw hers."
"ฉันพยายามคุมเสียงให้เบาพอที่จะไม่เป็นที่สนใจจากทั้งห้อง แต่ดังพอที่ทำให้เธอได้ยิน"

show misha cross_grin_close
with charachange

show misha cross_grin_close at twoleft
show bg school_scienceroom at bgright
with charamove

# mi "What are you doing, Hicchan~?"
mi "ทำอะไรอยู่อะ ฮิจัง~"

# "Panic shoots through me as Misha starts talking at her normal volume, and I sputter out a hasty reply, still keeping my voice down despite the fact that she just blew any hope of being discreet I may have had."
"ฉันสะดุ้งตกใจเมื่อมิช่าตอบกลับด้วยเสียงดังปกติของเธอ แล้วรีบตอบเธอโดยพยายามกดเสียงให้เบาไว้ถึงแม้เธอจะทำแผนที่\nฉันพยายามจะเงียบ ๆ พังแล้วก็เถอะ"

# hi "I'm copying down that stuff, what are you doing? Why so loud?"
hi "ฉันก็ลอกตามบนกระดานอยู่ไง แล้วเธอล่ะ ทำไมต้องเสียงดังด้วย"

show misha perky_confused_close
with charachange

# mi "Aw~, really? But it's all in the book… That's why no one else is copying it down~!"
mi "อ๋า~ งั้นเหรอ แต่ในหนังสือก็มีนี่…คนอื่นเขาถึงได้ไม่ลอกลงสมุดตัวเองกันไง~!"

# hi "I know, why are you so loud?"
hi "รู้แล้ว แล้วทำไมเธอต้องเสียงดังด้วยล่ะ?"

show misha hips_grin_close
with charachange

# mi "Why are you so quiet, Hicchan? It's hard to hear you."
mi "แล้วทำไมนายต้องเสียงเบาด้วยล่ะ แทบไม่ได้ยินเลยเนี่ย"

# "I look around to see if anyone is noticing our conversation and it's pretty obvious that everyone has, even the teacher."
"ฉันมองไปรอบ ๆ ห้องเพื่อดูว่ามีใครได้ยินที่เราคุยกันไหม ซึ่งแน่นอนว่าทุกคนได้ยินรวมถึงครูด้วย"


show shizu behind_smile at right
with charamoveinright

# "Shizune smiles coyly and I start to wonder if Misha is doing this because she told her to."
"ชิซูเนะเริ่มยิ้มอาย ๆ ฉันเลยสงสัยเธอว่ามิช่าทำแบบนี้เพราะเธอสั่งหรือเปล่า"

# "Is it because of what happened between her and Lilly earlier?"
"เป็นเพราะเรื่องที่เกิดระหว่างเธอกับลิลลี่ก่อนหน้านี้หรือเปล่านะ"

# "This is what I get for trying to be reasonable? For trying to take the middle path? Shizune is way too prideful, although by now I should know to expect that kind of behavior from her."
"นี่คือสิ่งที่ฉันควรเจอเพียงเพราะว่าฉันจะทำตัวให้มีเหตุผลเหรอ การที่ฉันพยายามเป็นกลางอะนะ ชิซูเนะเป็นคนยึดมั่น\nในศักดิ์ศรีมากไป ถึงจะปกติสำหรับคนอย่างเธอก็เถอะ"

# hi "Why are you doing this?"
hi "ทำไมเธอต้องทำแบบนี้ด้วย"

show misha perky_confused_close
with charachange

# mi "Huh?"
mi "หือ?"

# "Misha is totally oblivious to the awkward stare the teacher is giving both of us, while trying to balance her textbook on one finger. For a brief second it looks as if things could get ugly, but the teacher simply looks away, as if it's not worth the trouble."
"มิช่าพยายามทรงหนังสือเรียนด้วยนิ้วเดียวโดยไม่รู้ตัวเลยว่าครูกำลังจ้องมาที่เรา ตอนแรกดูเหมือนว่าจะจบไม่สวยแล้ว\nแต่สุดท้ายครูก็หันหน้าหนี ราวกับว่าไม่คุ้มที่จะพูดด้วย"

# "I guess this is a good thing, and I slump back in my seat in relief."
"ซึ่งก็คงดีแล้ว และฉันก็เอนตัวกลับไปนั่งอย่างสบายใจ"

scene bg school_scienceroom at bgright
with shorttimeskip

# "The rest of day passes by uneventfully, and this time I'm able to appreciate that it does."
"และทั้งวันก็ผ่านไปโดยไม่มีอะไรเกิดขึ้น ซึ่งรอบนี้ฉันยินดีที่มันเป็นเช่นนั้น"

play sound sfx_normalbell

# "When the bell rings, I'm not in a hurry, so I stay for a while, reviewing what we covered in class today. I prefer to leave last anyway, so I don't have to deal with crowding in the hallways."
"พอเสียงระฆังดัง ฉันนั่งรอสักพักเพราะไม่ได้มีธุระรีบร้อนอะไรพลางทบทวนเนื้อหาที่ได้เรียนในวันนี้ ยังไงฉันเองก็\nอยากจะออกคนท้าย ๆ อยู่แล้ว จะได้ไม่ต้องไปเบียดกับคนหมู่มากที่โถงทางเดิน"

# "I notice Shizune and Misha have also stayed behind, talking to someone from another class."
"ฉันสังเกตเห็นชิซูเนะกับมิช่ายังอยู่ด้วย คุยกับใครสักคนจากห้องอื่น"

# "Shizune's signing so fast that her hands make noises like swords cutting through the air."
"ชิซูเนะส่งภาษามือเร็วมากจนมือเธอทำเสียงเหมือนดาบที่ฟันตัดอากาศ"

# "Misha is trying desperately to keep up, but it's clear she can barely manage to even understand her."
"มิช่าพยายามอย่างหนักเพื่อที่จะตามให้ทัน แต่ก็เห็นได้ชัดว่าเธอแทบไม่เข้าใจเลยด้วยซ้ำ"

# "I put my head down. Whatever they're discussing, it looks like serious business. Probably way over my head.  Not just that, but Shizune also seems angry, although it could just be her normal severity making it appear so."
"ฉันฟุบหน้าลง ไม่รู้หรอกว่าคุยอะไรกันอยู่ แต่ดูท่าว่าจะเป็นเรื่องจริงจังน่าดู และฉันคงไม่น่าจะช่วยอะไรได้ด้วย แล้ว\nชิซูเนะเองก็ดูโมโหด้วย ถึงจริง ๆ ปกติท่าทางเธอก็เป็นแบบนี้อยู่แล้วละนะ"

# "Shizune signs to the point where her wrists crackle, and Misha struggles to spit it out in word form."
"ชิซูเนะทำภาษามือมากจนข้อมือเธอเริ่มดังกรอบแกรบ และมิช่าก็เริ่มลิ้นพันกันแล้ว"

# "Sometimes she trips over herself like she's dealing with tongue twisters. And then on top of that, she has to sign back anything the other girl says."
"บางทีก็พูดผิดเหมือนเวลาต้องพูดคำยาก ๆ ติด ๆ กัน แถมยังต้องทำภาษามือแปลกลับทุก ๆ คำพูดที่คนอื่นพูดด้วย"

# "Seems like a rough job."
"ช่างเป็นงานที่หนักจริง ๆ"

# "Misha looks tired, like she's about to faint."
"มิช่าดูหมดแรง คลับคล้ายว่าจะเป็นลม"

# "Luckily for her, their business is soon finished and the girls sit down on their seats again."
"โชคยังดีที่ไม่นานเรื่องก็จบลง และพวกเธอก็กลับมานั่งที่อีกครั้ง"

show shizu behind_blank at tworight
show misha perky_sad at twoleft
with charaenter

# mi "Uwaaah! I'm so tired!"
mi "อ๊าาาาา! เหนื่อยจังเลย!"

# "She's hanging her head limply on her desk, looking exhausted."
"เธอห้อยหัวฟุบลงกับโต๊ะด้วยท่าทีหมดแรง"

# hi "Festival preparations must be tough for you."
hi "เตรียมจัดงานเทศกาลคงจะเหนื่อยน่าดูเลยนะ"

# "Indeed, the people in this school seem to be taking the festival very seriously. Whenever I see people idling around before and after classes they're always talking about their plans for it."
"ดูเหมือนว่าคนในโรงเรียนนี้จะจริงจังกับงานเทศกาลนี้มาก พออยู่กันว่าง ๆ ทีไรฉันเห็นเป็นต้องคุยกันเรื่องนี้ตลอด"

# "It's kind of neat to see everyone being so enthusiastic about it."
"เห็นทุกคนจริงจังขนาดนี้กับงานนี้ก็ดี"

# "I'm probably the only one who doesn't have something to do."
"ฉันคงเป็นคนเดียวละมั้งที่ไม่มีอะไรให้ทำเลย"

show shizu basic_normal
show misha perky_confused
with charachange

# "Shizune starts signing at me and Misha perks up, looking at her hands with slightly unfocused eyes."
"ชิซูเนะเริ่มทำภาษามือให้ฉันและมิช่าก็เงยหน้าขึ้นมามองไปที่มือของเธอด้วยสายตาเบลอ ๆ เล็กน้อย"

show shizu behind_frown
with charachange

shi "…"

# "She signs with harsh, heavy, dramatic strokes."
"เธอส่งภาษามือด้วยท่าทางที่ดูรุนแรง หนักแน่น และเล่นใหญ่"

# "Misha translates her signing into speech for me."
"มิช่าแปลภาษามือนั้นเป็นคำพูดให้ฉัน"

# "She does it so well it's almost like Shizune is actually speaking, transmitting her thoughts directly through Misha."
"ซึ่งเธอทำได้ดีเหมือนชิซูเนะพูดเองเลยทีเดียว อารมณ์และความคิดของเธอถูกส่งต่อมาที่ฉันผ่านทางมิช่า"

show misha cross_frown
with charachange

# mi "Well, we're in the Student Council, you know, so we're pretty busy."
mi "ก็ พวกเราเป็นสภานักเรียนนี่ เนี่ยนายรู้ไหมว่าเรายุ่งมาก"

# hi "Sarcasm?"
hi "ประชดเหรอ"

show misha perky_confused
with charachange

# mi "Huh?"
mi "หา?"

# "The tone of Shizune's actions make me think she is “speaking” with disdain, but Misha interprets it normally, replacing whatever intent may have been there with her own chipper twist on things. It's still disorienting, I don't think I'll ever get used to it."
"ท่าทางของชิซูเนะทำให้ฉันรู้สึกว่าเธอ “พูด” อย่างดูแคลน แต่มิช่าก็แปลออกมาซื่อ ๆ แล้วใส่ความสดใสร่าเริงของตัวเอง\nลงไปแทนที่เจตนาจริง ๆ อะไรก็ตามของคำพูดนั้น ซึ่งก็คลาดไปจากกันอยู่ แล้วฉันคงไม่มีวันทำใจให้ชินได้แน่ ๆ"

# hi "Never mind."
hi "ช่างเหอะ"

# hi "How could I forget, with you two trying to get me to join at least twice a day?"
hi "ฉันจะลืมได้ไงว่าพวกเธอเป็นสภานักเรียน พวกเธอเล่นชวนฉันต่ำ ๆ ก็วันละ 2 รอบละ"

show misha cross_laugh
with charachange

# mi "Hahaha~! But, Hicchan, some could say the work is too much."
mi "ฮ่าฮ่าฮ่า~! แต่ว่านะฮิจัง งานของพวกเราน่ะจะเรียกว่ามีมากจนล้นเลยยังได้"

show shizu basic_normal2
with charachange

show misha perky_sad
with charachange

# mi "It'd be nice if students were to show a little more support for their leadership, some appreciation to the ones who are working so hard to make it all possible."
mi "ถ้าเหล่านักเรียนคอยสนับสนุนผู้นำของพวกเขาให้มากกว่านี้อีกหน่อยได้ก็คงดี คอยชื่นชมคนที่ยอมทำงานหนัก\nเพื่อทำทุกอย่างให้สำเร็จได้ด้วยดี"

show shizu behind_frown
with charachange

show misha perky_smile
with charachange

# mi "Maybe, for example, a little help. That's asking too much, is it? Yep~! Help would be appreciated~! From students like you~!"
mi "อย่างแบบ มาช่วยงานสักหน่อยงี้ คงจะขอมากไปใช่มะ อื้ม~! ถ้านักเรียนอย่างนาย~! มาช่วยคงเป็นพระคุณยิ่ง~!"

show shizu adjust_angry
with charachange

show misha hips_frown
with charachange

# mi "If students would show their dedication and school spirit, and offer some help, well, I don't exactly need it…"
mi "ถ้าพวกนักเรียนแสดงให้เห็นถึงความทุ่มเทและจิตวิญญาณของโรงเรียนแล้วมาช่วยกันสักหน่อย ฉันคงไม่ต้องขอแรง\nเพิ่มหรอก…"

show shizu behind_smile
with charachange

show misha hips_smile
with charachange

# mi "But I wouldn't necessarily refuse it… So~! it would be nice if someone would…"
mi "แต่ถ้ามีแรงมาช่วยก็อาจจะรับไว้อยู่ดีน่ะนะ… มันก็~! คงจะดี ถ้ามีใครสักคนมา…"

stop music fadeout 2.0

show shizu adjust_blush
show misha perky_confused
with charachange

# mi "Oh? Hello~!"
mi "โอ๊ะ หวัดดีจ้า~!"

show shizu adjust_blush at offscreenleft
show misha perky_confused at Transform(xanchor=0.5, xpos=-0.45)
show bg school_scienceroom at bgleft
with charamove

show hanako emb_timid at Transform(xanchor=0.5, xpos=0.93)
with charamoveinright

play music music_pearly fadein 1.0

# "I look over my shoulder and see Hanako peering timidly into the classroom, most of her body hidden behind the door."
"พอหันไปข้างหลังก็เห็นฮานาโกะกำลังมองเข้ามาในห้องเรียนอย่างอาย ๆ โดยซ่อนตัวของเธอเกินครึ่งไว้หลังประตู"

show misha perky_smile at Transform(xanchor=0.5, xpos=0.15)
with charamove

# mi "Hey! Playing delinquent again?"
mi "นี่เธอ! ทำตัวเกเรอีกแล้วเหรอ"

show hanako emb_blushtimid
with charachange

# "Hanako blushes hard at Misha's straightforward jab, even if it was only in jest."
"ฮานาโกะหน้าแดงแจ๋ทันทีที่มิช่าพูดแซว ถึงแม้จะไม่ได้ว่าจริงจังอะไรมาก"

show shizu basic_angry at Transform(xanchor=0.5, xpos=0.35)
with charamove

shi "…"

show hanako emb_downsad
with charachange

show hanako emb_downsad at Transform(xanchor=0.5, xpos=0.97)
with charamove

# "Shizune stares at her probingly, causing Hanako to look down and start backing away to the point where only her fingers can be seen wrapped nervously around the edge of the door."
"ชิซูเนะมองเธอด้วยความสงสัย ทำให้ฮานาโกะก้มหน้าแล้วถอยหนีไปจนเห็นเพียงนิ้วของเธอเท่านั้นที่จับขอบประตูด้วย\nความประหม่า"

# "Maybe she is showing her dislike of Hanako by association of her dislike of Lilly."
"บางทีคงเพราะเธอไม่ชอบลิลลี่เลยพาลทำท่าไม่ชอบฮานาโกะไปด้วย"

# "It appears so, and Hanako probably knows it as well."
"คงจะเป็นแบบนั้น และฮานาโกะเองก็รู้ตัวเช่นกัน"

# "They seem to have momentarily forgotten about trying to get me to stay for the rest of the day."
"เหมือนพวกเธอลืมไปพักหนึ่งว่าจะรั้งให้ฉันอยู่ต่อจนหมดวัน"

# hi "What is it, Hanako?"
hi "มีอะไรเหรอฮานาโกะ"

show hanako emb_timid
with charachange

# ha "H… has Lilly been here?"
ha "ละ… ลิลลี่อยู่ไหม"

# mi "Sorry, Satou is not here. She, eh, came by in the morning though."
mi "โทษทีจ้า คุณซาโต้ไม่อยู่ที่นี่ เธอ เอ่อ มาเมื่อเช้าน่ะ"

show hanako emb_downtimid
with charachange

# "Hanako keeps looking uneasily at Shizune, who stares back at her with her usual studying gaze. What is she trying to do?"
"ฮานาโกะยังคงมองชิซูเนะอย่างไม่สบายใจ ซึ่งชิซูเนะก็จ้องกลับมาที่เธอด้วยสายตาที่จดจ่ออย่างเคย คิดจะทำอะไรกันนะ"

# "Of course Shizune isn't going to look away, and she is intimidating enough as it is, so I can only imagine how terrified Hanako would be."
"แน่นอนว่าชิซูเนะไม่หยุดมองแน่ ๆ และเธอก็ท่าทางน่ากลัวด้วย สภาพนี้ฮานาโกะคงจะกลัวเอามาก ๆ แน่ ๆ"

# "It is a little funny though, watching Hanako's reaction to Shizune's normal behavior. This is what happens when two people of two different extremes meet, it seems."
"พอดูปฏิกิริยาของฮานาโกะที่มีต่อนิสัยปกติของชิซูเนะแล้วก็แอบตลกเหมือนกัน นี่คงเป็นสิ่งที่จะเกิดขึ้นเมื่อสองคน\nที่นิสัยต่างกันสุดขั้วมาเจอกันสินะ"

show hanako emb_timid
with charachange

# ha "Do… do you know where she is?"
ha "แล้ว… แล้วเธอรู้ไหมว่าลิลลี่อยู่ไหน"

show shizu behind_frown
with charachange

shi "…"

show misha hips_frown 
with charachange

# mi "If she has any sense in her head, she's in her classroom, working on their festival project. But who knows where that woman is loitering at."
mi "ถ้าเธอคนนั้นมีจิตสำนึกสักหน่อย เธอก็คงจะอยู่ห้องเธอช่วยจัดงานเทศกาลแหละ แต่ใครจะรู้ เธอคนนั้นอาจจะจะหนี\nไปซ่อนตัวที่ไหนก็ได้"

label th_A22a:

show misha hips_grin at Transform(xanchor=0.5, xpos=0.15)
with charachange

# mi "She might be slacking off somewhere, just like Hicchan~! Wahaha~!"
mi "เธอคงหนีไปอู้ที่ไหนสักที่แหละ เหมือนฮิจังอะนะ~! วะฮ่าฮ่า~!"

# "Damn, what is it with Shizune and her need to point out stuff like this?"
"แม่ง สองคนนี้เป็นอะไรกันถึงต้องมาแซะแบบนี้"


label th_A22b:

scene bg school_scienceroom at bgleft
show shizu behind_frown at Transform(xanchor=0.5, xpos=0.35)
show misha hips_frown at Transform(xanchor=0.5, xpos=0.15)
show hanako emb_timid at Transform(xanchor=0.5, xpos=0.97)
with None


# mi "She might be slacking off somewhere~! What a useless woman~!"
mi "เธอคงหนีไปอู้ที่ไหนสักที่แหละ ช่างเป็นคนไร้ประโยชน์จริง ๆ ~!"

show hanako emb_downtimid
with charachange

hide hanako
with easeoutright

# "Hanako nods quickly and retreats with haste, obviously to avoid any further contact with Shizune. Unfortunately, this turns their attention fully back to me."
"ฮานาโกะรีบพยักหน้าแล้วถอยหนีอย่างรวดเร็ว ชัดว่าเธอไม่อยากจะเสวนากับชิซูเนะอีก ซึ่งแย่หน่อยตรงที่พอเป็น\nอย่างนั้นแล้วก็ทำให้ความสนใจของพวกชิซูเนะกลับมาที่ฉันอีกรอบ"

stop music fadeout 2.0

show shizu behind_frown at tworight
show misha hips_frown at twoleft
show bg school_scienceroom at bgright
with charamove

show misha hips_grin
show shizu behind_smile
with charachange

# mi "But Hicchan is not useless, right? Right? He said so himself~! Wahaha~!"
mi "แต่ฮิจังไม่ไร้ประโยชน์นี่ ใช่ไหม ใชไหม เขาบอกเองนี่~! วะฮ่าฮ่า~!"

# "I can see where this is going, and I do not want any part of it, not after that experience yesterday."
"ดูจากสภาพก็พอเห็นละว่าจะเกิดอะไรขึ้น และฉันก็ไม่อยากจะยุ่งด้วย โดยเฉพาะที่ฉันได้เจอมาเมื่อวาน"

# hi "Well, good luck with your preparations…"
hi "ก็ ขอให้โชคดีกับการเตรียมงานนะ…"

# "I start packing my bag, ready to make a break for the exit."
"ฉันเก็บกระเป๋า เตรียมจะออกจากห้อง"

# "Unfortunately I'm all the way on the other side of the room."
"แย่หน่อยตรงที่ฉันอยู่อีกฟากของห้องเลยจากทางออก"

# "The short distance to the doorway seems like a vast No Man's Land to me now."
"ระยะสั้น ๆ ไปถึงประตูช่างยาวไกลเหมือนเดินข้ามผ่านแดนรกร้างกว้างไกล"

show misha perky_smile
show shizu behind_blank
with charachange

play music music_shizune fadein 4.0

show bg school_scienceroom at bgleft
show shizu behind_blank at center
show misha perky_smile at Transform(xalign=-0.15)
with charamove

show bg school_scienceroom at center
show shizu behind_blank at tworight
show misha perky_smile at twoleft
with charamove

# "Shizune and Misha both start maneuvering slowly in front of me, cutting off my route of escape in an unsettlingly cautious way that makes me think of ship-to-ship combat."
"ชิซูเนะและมิช่าต่างเคลื่อนไหวอย่างช้า ๆ อยู่ตรงหน้าฉันปิดทางหนีจนชวนให้รู้สึกเหมือนพวกเธอระแวดระวังอย่างทะแม่ง ๆ \nเห็นแล้วก็นึกถึงเรือที่รบกันบนน้ำ"

show misha hips_grin
with charachange

# mi "I think Shicchan is saying that you should help us, Hicchan~!"
mi "ฉันเห็นชิจังบอกว่านายจะช่วยพวกเรานี่ ฮิจัง~!"

# hi "Gee, I wouldn't know, she's so subtle."
hi "โห ไม่รู้เลยนะเนี่ย ไม่เห็นบอกกันตรง ๆ"

show misha perky_confused
with charachange

# mi "But~! that's the intent, so, please? I can't keep up, we have to actually build stalls for the festival, almost all of them all by ourselves, can you believe that?"
mi "แต่ว่า~! นั่นแหละที่เธออยากบอก เพราะงั้น ขอร้องเถอะนะ ฉันไม่ไหวแล้ว เราต้องมาทำแผงสำหรับงานเทศกาลกันสองคน\nเนี่ย เหลือจะเชื่อเลยเนอะ"


show misha perky_sad
with charachange

# mi "Hammering boards together, over and over again, for hours, it's really hard!"
mi "ตอกไม้กระดานให้เข้ากันซ้ำแล้วซ้ำเล่านานนับชั่วโมง ลำบากจริง ๆ !"

# mi "I'm so used to it I was doing swinging motions in class, and I didn't even know it!"
mi "ฉันทำจนชิน จนฉันเผลอแกว่งแขนตอกในห้องเรียนโดยไม่รู้ตัวด้วยซ้ำ!"

# "She bangs her desk a few times, imitating hammer blows."
"เธอทำท่าตีค้อนทุบโต๊ะอยู่สองสามที"

# mi "It's so repetitive, I can't stand it! And yesterday, I actually hammered all the boards on top of each other…"
mi "ซ้ำซากจำเจจนทนไม่ไหวแล้ว! แล้วเมื่อวานอะนะ ฉันเผลอตอกแผ่นไม้ซ้อนกันอีก…"

# mi "It was just a stack of boards all nailed together, and then I had to take it apart and do it all over again, and I got yelled at and laughed at~!"
mi "กลายเป็นว่าแผ่นไม้หลายแผ่นก็เลยตอกเข้าด้วยกัน ฉันต้องมานั่งถอนออกแล้วทำใหม่หมด ฉันเลยโดนทั้งตะโกน\nทั้งหัวเราะเยาะใส่"

# hi "Uh…"
hi "เอ่อ…"

show misha perky_smile
with charachange

# mi "So…"
mi "เพราะงั้น…"

show misha hips_grin_close
with characlose

# "She clamps a hand down on my shoulder and grins, quickly running her tongue across her teeth mischievously."
"เธอจับไหล่ฉันและยิ้มแล้วเอาลิ้นเลียฟันอย่างซุกซนไปมา"

# mi "Do you have any plans for today, Hicchan?"
mi "วันนี้นายว่างมั้ยฮิจัง?"

# mi "I wonder if you do~."
mi "ว่างมั้ยน้า~"

# hi "Sure I have plans…"
hi "ไม่ว่าง…"

show misha perky_confused_close
with characlose

# mi "Really~?"
mi "จริงเหรอ~"

# mi "You're going to help us, right?"
mi "นายจะมาช่วยพวกเราใช่ไหม"

# "I notice her hands are moving constantly."
"ฉันเห็นเธอขยับมืออย่างต่อเนื่อง"

# "She's signing everything we both say so that Shizune can understand."
"เธอแปลบทสนทนาของพวกเราเป็นภาษามือเพื่อให้ชิซูเนะเข้าใจด้วย"

# "Shizune is being somewhat quiet today. Is she still angry? Well, probably at least a bit. I can see it in her eyes. But, this could also just be another way of trying to guilt me into lending her a hand."
"ซึ่งชิซูเนะเองวันนี้เธอดูเงียบแปลก ๆ ยังโกรธกันอยู่เหรอ ก็นะ คงอาจจะแหละ มองตาก็รู้ละ แต่ว่านะ เธออาจจะแค่\nทำให้ฉันรู้สึกผิดเพื่อให้ฉันไปช่วยงานก็ได้"
# "ก็พูดได้ไม่เต็มปากหรอกว่าก็แอบดีใจที่พยายามจะชวนกันขนาดนี้ แต่ก็แอบสงสัยนิดนึงว่าในสภานักเรียนเขาทำอะไรกันแน่   ""ก็พูดได้ไม่เต็มปากหรอกว่าก็แอบดีใจที่พยายามจะชวนกันขนาดนี้ แต่ก็แอบสงสัยนิดนึงว่าในสภานักเรียนเขาทำอะไรกันแน่   " exclude #  len"

# "I have to find a way out of this."
"ต้องหาทางหนีทีไล่ให้ได้"

# hi "Hey, I should go now, to the library. You know, homework…"
hi "เออ เดี๋ยวฉันต้องไปห้องสมุดละ แบบว่า มีการบ้าน…"

# hi "I should get going, shouldn't I? I have to be diligent, because I'm a new student, and all, so I have to make a good first impression, right? Yeah…"
hi "ฉันต้องรีบไปแล้วสินะ ช่วงนี้ต้องขยันหน่อยเพราะว่าฉันเพิ่งมาใหม่ จะได้มีภาพลักษณ์ที่ดีไง ใช่ ๆ …"

# hi "See you later, then!"
hi "ไว้เจอกันละกัน!"

show misha perky_confused_close at offscreenleft
show shizu behind_blank at twoleft
show bg school_scienceroom at bgleft
with ease

hide misha
show misha perky_confused_close behind shizu at offscreenleft

show shizu basic_normal2 at offscreenright
show bg school_scienceroom at center
with ease_accel

show shizu cross_angry_close at tworight
show bg school_scienceroom at bgright
with ease_decel

# "I turn to bolt for the door, but Shizune is blocking my path, her arms crossed over her chest and a stern expression on her face."
"ฉันรีบหันตัวเพื่อหนีไปยังประตู แต่ชิซูเนะก็เข้ามาขวางและยืนกอดอกทำหน้าดุ"

show shizu basic_angry_close
with charadistant

# "She wags a finger tauntingly and begins signing to Misha with the manner of a squad leader giving directions to his fellow soldiers."
"เธอส่ายนิ้วไปมาด้วยท่าทีเยาะเย้ย พร้อมส่งภาษามือให้มิช่าราว ๆ กับนายหมู่สั่งลูกน้องทหาร"

show shizu basic_angry
with charadistant

show misha perky_smile at twoleft
with charamove

# mi "It didn't seem like you were in any rush to get to the library, Hicchan~!"
mi "ไม่เห็นว่านายจะต้องรีบไปห้องสมุดขนาดนั้นเลยนี่ ฮิจัง~!"

show misha hips_grin
with charachange

# mi "That's right, Shicchan~, it does seem like he was probably going to slack off for the rest of the day."
mi "ช่ายแล้วชิจัง~ ดูเหมือนว่าเขาคงจะหนีไปอู้งานตลอดทั้งวันที่เหลือแน่ ๆ"

show misha hips_laugh
with charachange

# mi "Hahaha~! Wahaha~! You're surrounded~!"
mi "ฮ่าฮ่าฮ่า~! วะฮ่าฮ่า~! นายจนมุมแล้วละ~!"

show shizu behind_frown
with charachange

shi "…"

show misha hips_smile
with charachange

# mi "Let's go to the student council room~!"
mi "ไปห้องสภานักเรียนกันเถอะ~!"

# "She lets out a chuckle, and then breaks into laughter."
"เธอหัวเราะคิกคัก ตามด้วยระเบิดเสียงหัวเราะดังลั่น"

show misha cross_laugh
with charachange

# mi "I'm sorry, Hicchan, I feel bad, but this works out for everyone, right?"
mi "โทษทีนะฮิจัง จริง ๆ ฉันก็รู้สึกผิดแหละ แต่ก็เพื่อทุก ๆ คนนี่นะ"

show shizu basic_normal2
with charachange

shi "…"

show misha sign_smile
with charachange

# mi "That's right, Shicchan! Yes~, that's a good point too."
mi "ใช่ ๆ ชิจัง! ช่าย~ ถูก ๆ "

show shizu behind_blank
with charachange

shi "…"

show misha hips_smile
with charachange

# mi "Yes, this is beneficial to everyone, it solves all our problems."
mi "ใช่ เนี่ย ทำเพื่อผลประโยชน์ของทุกคน แก้ปัญหาของพวกเราด้วย"

show shizu basic_frown
with charachange

shi "…"

show misha hips_frown
with charachange

# mi "Yeah yeah~!, I also thought he'd be more appreciative of our efforts."
mi "ช่าย ช่าย~! ฉันก็นึกว่าเขาจะชื่นชมที่พวกเราอุตส่าห์ลงแรงกันไปให้มากกว่านี้เสียอีก"

show misha hips_frown_close
show shizu basic_frown_close
with characlose

# "They pull themselves closer, as if they are about to pounce."
"พวกเธอขยับเข้ามาใกล้ ราวกับว่าจะกระโจนเข้าใส่"

# hi "Hey guys, two-on-one isn't very fair, is it?"
hi "นี่พวกเธอ มารุมสองต่อหนึ่งแบบนี้ไม่ยุติธรรมเลยนี่นา"

show shizu behind_blank_close
with charachange

shi "…"

# "She keeps looking forward, impassive, then gives a sinister smile."
"เธอยังคงจ้องมองมาหน้านิ่ง จากนั้นก็แสยะยิ้มชั่วร้าย"

show shizu basic_sparkle_close
show misha hips_grin_close
with characlose

# mi "Come on, we have a lot of work to do! Let's go to the student council room~!"
mi "เอาเถอะน่า พวกเรามีงานต้องทำอีกเยอะเลย! ไปห้องสภานักเรียนกันเถอะ~!"

# hi "Gee, I don't know…"
hi "อ่า ไม่รู้ดิ…"

show misha cross_laugh_close
with characlose

# "Misha laughs."
"มิช่าหัวเราะออกมา"

show misha hips_grin_close
with characlose

# mi "Deja vu~?"
mi "เดจาวู~?"

# "She chortles, before letting out another laugh."
"เธอหัวเราะคิกคัก ก่อนจะหัวเราะออกมาอีกครั้ง"

show misha cross_laugh_close
with characlose

# mi "Hahaha, you know, my horoscope said it'd be a good day for me today."
mi "ฮ่าฮ่าฮ่า ก็นะ ผลทำนายดวงฉันวันนี้บอกว่าวันนี้เป็นวันที่ดีของฉันล่ะ"

show misha perky_smile_close
with characlose

# mi "And now that you're going to help—{w=.5}{nw}"
mi "และตอนนี้นายก็จะมาช่วย—{w=.5}{nw}"

show shizu adjust_smug_close
with charachange

# "Shizune signs quickly to her."
"ชิซูเนะรีบส่งภาษามือให้เธอ"

show misha hips_grin_close
with charachange

# mi "Right~!, I mean, now that you've decided to help us, completely of your own free will, I'll be able to take it easy! Lucky~, huh?"
mi "ใช่แล้ว~! ก็นายตกปากรับคำด้วยตัวเองแล้วว่าจะช่วยพวกเรา ฉันก็จะได้ไม่ต้องทำงานหนักมากด้วย! ดี๊ดี~ เนอะ"

# "I open my mouth to say something but then realize there's no point."
"ฉันอ้าปากเพื่อที่จะพูดอะไรบางอย่าง แต่ก็นึกได้ว่าไม่มีประโยชน์หรอก"

# "I refocus on trying to think of a way out of this. No, their actions are clearly deliberate, there's no sense in attempting to reason with them."
"ฉันกลับมาคิดหาทางออกจากสถานการณ์นี้อีกครั้ง ไม่ดิ การกระทำของพวกเธอมีเจตนาชัดเจนขนาดนี้ คงไม่มีประโยชน์\nที่จะใช้เหตุผลเถียงด้วยหรอก"

# "You can't reason with madmen. I frown, and they don't even notice my discontent, further proving my suspicions."
"เถียงกับคนบ้าไปก็ไม่ได้ความ ฉันทำหน้าบูด และพวกเธอก็ไม่เห็นอาการไม่พอใจของฉันด้วยซ้ำ เป็นการยืนยันสิ่งที่ฉันคิด\nเข้าไปอีก"

# "They seem pretty relaxed now. I guess they think they've already won, so they're letting their guard down."
"ตอนนี้พวกเธอก็ดูไม่ได้จับจ้องมากแล้ว คงคิดว่าตัวเองชนะแล้วเลยไม่ได้ระแวงอะไรอีก"

stop music fadeout 2.5

# "That's kind of arrogant."
"ช่างได้ใจเสียจริง"

# "They pass forward in front of me as they move through the doorway,"
"พวกเธอเดินแซงหน้าฉันตอนที่เดินออกจากประตู"

hide shizu
hide misha
with charaexit

# "And I stealthily walk backwards back into the classroom as they step into the hallway, turning towards the stairwell."
"และฉันก็แอบย่องกลับมาในห้องเรียนตอนที่พวกเธอกำลังเดินไปยังโถงทางเดิน หันไปทางบันได"

# "I let out a sigh of relief and quickly pack the rest of my stuff so I can make my escape."
"ฉันถอนหายใจอย่างโล่งอก และรีบเก็บของส่วนที่เหลือเพื่อจะได้หนีได้ทัน"

play sound sfx_doorslam

# "The classroom door slams shut."
"ประตูห้องเรียนถูกปิดดังปัง"

play music music_running fadein 0.5

show shizu cross_angry at offscreenright with None
show misha cross_frown at offscreenleft with None
show shizu cross_angry at tworight
show misha cross_frown at twoleft
with ease

shi "…"

# mi "That wasn't very nice, there. Hahaha, you really got us good, though. Didn't he, Shicchan?"
mi "ร้ายนักนะ ฮ่าฮ่าฮ่า แต่นายต้มเราซะเปื่อยเลยนะ ใช่มะชิจัง?"

show shizu behind_frown
with charachange

shi "…"

show misha hips_grin
with charachange

# mi "Right, right… …Hahaha!"
mi "ช่าย ช่าย… …ฮ่าฮ่าฮ่า!"

show misha cross_frown
with charachange

# mi "What was that about? I thought you said you'd help us!"
mi "ทำอะไรของนายน่ะ ไหนบอกว่าจะช่วยพวกเราไง!"

# mi "And then you bailed on us! And you thought you would get away with it, didn't you?"
mi "และนายก็จะหนีไป และคิดว่าจะรอดไปได้ ใช่ไหมล่ะ"

show misha cross_laugh
with charachange

# "The indignant expression vanishes and she begins to laugh hysterically, calming down only after an aggravated look from Shizune."
"ท่าทางโกรธเคืองหายไป และเธอก็เริ่มหัวเราะอย่างบ้าคลั่ง แต่สงบลงตอนที่ชิซูเนะแสดงท่าทีเคือง ๆ"

show misha cross_grin
with charachange

# mi "Oh, ah… Yeah~, you thought you could get away with it! But, a criminal always returns to the scene of the crime!"
mi "โอ๊ะ อ่า… ช่าย~ นายคงคิดว่าจะรอดไปได้ แต่! ผู้ร้ายน่ะก็มักจะกลับมายังจุดเกิดเหตุเสมอยังไงล่ะ!"

# "I didn't even manage to leave the classroom in the first place. No, wait, I didn't even agree to help in the first place."
"ฉันยังไม่ได้ออกจากห้องไปด้วยซ้ำ ไม่ดิ ฉันยังไม่ได้ตกปากรับคำว่าจะช่วยตั้งแต่แรกแล้วนี่นา"

show misha perky_smile
with charachange

# mi "Not very bright, are you, criminal? Thinking you can just shirk your duties like that… How low, Hicchan~!"
mi "ไม่ฉลาดเอาซะเลยนะคุณผู้ร้าย คิดจะหลบเลี่ยงหน้าที่ของตัวเองแบบนั้นน่ะ… แย่จริง ๆ เลยฮิจัง~!"

# hi "I'm a criminal? What did I do? What's the charge? What am I guilty of?"
hi "ฉันเป็นผู้ร้ายงั้นเหรอ ฉันทำอะไร ข้อหาอะไร ผิดตรงไหน"

show misha hips_grin
with charachange

# mi "That's for the courts to decide, criminal! I don't think we have to tell you that!"
mi "นั่นเป็นเรื่องที่ศาลต้องตัดสินนะคุณผู้ร้าย ฉันว่าเราไม่ต้องบอกนายเรื่องนี้หรอก!"

show misha perky_smile
with charachange

# mi "Besides, you're the criminal here, you know what you did!"
mi "แล้วอีกอย่าง นายก็เป็นคนร้ายนี่ นายทำอะไรก็รู้อยู่แก่ใจ!"

# hi "Have you ever read “The Trial,” by Kafka?"
hi "เธอเคยอ่าน “{i}คดีความ{\i}” ของคัฟคาหรือเปล่า"

show misha hips_grin
with charachange

# mi "No, what's that, Hicchan~? What does that have to do with this?"
mi "ไม่อะ ทำไมเหรอฮิจัง~ หนังสือนั่นเกี่ยวอะไรด้วยเหรอ"

# hi "I read it a few months ago. It's about these people who run a kangaroo court on a guy who just wants to live his life. They refuse to leave him alone, and he can't fight the power."
hi "ฉันอ่านเรื่องนี้เมื่อไม่กี่เดือนก่อน เป็นเรื่องเกี่ยวกับคนกลุ่มหนึ่งที่คอยบริหารศาลเตี้ยเพื่อลงโทษผู้ชายคนหนึ่งที่แค่ต้องการ\nใช้ชีวิต พวกเขาไม่ยอมปล่อยเขาให้อยู่แบบสงบ ๆ และเขาก็ไม่สามารถต่อสู้กับอำนาจได้"

show shizu basic_frown
with charachange

shi "…"

show shizu behind_frown
with charachange

shi "…"

show misha hips_smile
with charachange

# mi "Hicchan, what does that have to do with anything?"
mi "ฮิจัง แล้วมันเกี่ยวอะไรกันด้วย"

show misha sign_confused
with charachange

# mi "Hey~!, what does that mean?"
mi "นี่~! หมายความว่าไงน่ะ"

# "She turns back to me after signing back and forth for a lengthy amount of time."
"เธอหันกลับมาหาฉันหลังจากที่แปลภาษามือไปมาอยู่เสียนาน"

show misha hips_frown
with charachange

# mi "You know, we're both a little disappointed in you. You've let us down, Hisao."
mi "เนี่ย พวกเราผิดหวังในตัวนายนิดหน่อย นายทำเราผิดหวังนะฮิซาโอะ"

show shizu basic_frown
with charachange

shi "…"

# mi "Dropped the ball."
mi "ปล่อยเรือล่ม"

show shizu behind_frown
with charachange

shi "…"

# mi "Left us hanging. And out in the cold~."
mi "ให้พวกเราจมกลางทะเล~"

show shizu cross_angry
with charachange

shi "…"

show misha sign_smile
with charachange

# mi "Is that any way to treat a person? To run away from your responsibilities, to abandon your comrades?"
mi "คนเราเขาทำตัวกับคนอื่นอย่างนี้เหรอ หลีกหนีภาระหน้าที่ ทอดทิ้งพวกพ้องอะนะ"

show misha hips_frown
with charachange

# mi "We think you owe it to us to honor your commitment."
mi "พวกเราคิดว่านายควรทำตามสัญญานะ"

# hi "What? But I didn't commit to anything~!"
hi "อะไร ฉันไม่ได้ไปสัญญิงสัญญาอะไรสักหน่อย~!"

# "My breathing catches in my throat and I momentarily start choking."
"ฉันจุกคอหอยขึ้นมาและหายใจไม่ออกไปชั่วขณะหนึ่ง"

show shizu basic_frown
with charachange

shi "…"

show misha cross_smile
with charachange

# mi "That's not true, Hicchan! You said you are not useless, you definitely said it, yes, definitely, definitely definitely~!"
mi "ไม่จริงสักหน่อยฮิจัง! นายบอกเองว่านายไม่ไร้ประโยชน์ นายพูดเอาไว้แน่ ใช่ แน่นอน แน่นอน แน่นอน~!"

show misha hips_grin
with charachange

# mi "We are calling you on those words now~! You better prepare to show you are not a useless guy!"
mi "พวกเราจะรอดูนายพิสูจน์คำพูดนั้นนะ~! นายต้องทำให้เห็นว่านายน่ะไม่ได้ไร้ประโยชน์!"

# mi "Your honor will be soiled forever if you try to get out of this~!"
mi "ศักดิ์ศรีของนายของจะแปดเปื้อนแน่ ๆ ถ้านายเลือกที่จะหนีไปน่ะ~!"

# mi "So for the rest of the day, we are going to hang out together, just the three of us, and work hard!"
mi "เพราะงั้นแล้วตลอดวันที่เหลือ พวกเราจะอยู่ด้วยกันสามคน และไปตั้งใจทำงานกัน!"

show shizu behind_frown
with charachange

shi "…"

show misha hips_smile
with charachange

# mi "You can't fool us!"
mi "นายหลอกเราไม่ได้หรอกนะ!"

# mi "You should be happy, you're doing your school a great service. Ask not what your school can do for you…"
mi "นายควรจะมีความสุขสิ นายจะได้ช่วยโรงเรียนได้อย่างดีเลย อย่าได้ใคร่ถามเลยว่าโรงเรียนทำอะไรให้นายได้บ้าง…"

# mi "But what you can do for your school!"
mi "หากแต่จงถามว่านายทำอะไรให้โรงเรียนได้บ้างต่างหาก!"

show misha cross_laugh
with charachange

# mi "Hahaha!"
mi "ฮ่าฮ่าฮ่า!"

# mi "Hahahahahahaha!"
mi "ฮ่าฮ่าฮ่าฮ่าฮ่าฮ่าฮ่า!"

# "How depressing."
"หดหู่ว่ะ"

show misha cross_grin
with charachange

# mi "Cheer up, cheer up, Hicchan!"
mi "เอาน่า เอาน่า ฮิจัง!"

# "She slaps me hard across the back with enough strength to knock the air out of my lungs. I gasp to breathe."
"เธอตบหลังฉันดังป้าบเล่นเอาฉันจุกจนหายใจลำบาก"

# mi "Besides, aren't you happy you get to spend the day with two cute girls?"
mi "อีกอย่าง นายไม่มีความสุขเหรอที่จะได้ใช้เวลาอยู่ร่วมกันกับสาวน่ารัก ๆ สองคนน่ะ"

show misha hips_laugh
with charachange

# mi "Hahahaha!"
mi "ฮ่าฮ่าฮ่าฮ่า!"

# "I guess they are right. I did blurt those words out."
"ฉันคงพลั้งปากไปแบบนั้นอย่างพวกเธอว่าจริง ๆ ละมั้ง"

stop music fadeout 3.0

# "Accepting my fate, I follow them to the student council room…"
"ฉันก้มหน้ารับชะตากรรมเดินตามพวกเธอไปยังห้องสภานักเรียน…"

scene bg school_council_ss
with shorttimeskip

play sound sfx_hammer
play music music_tranquil fadein 3.0

# "…And hammer the final nail into the stall. It took all of the afternoon, and dinner time is nearly over. But it is done now."
"…และตอกตะปูที่ซุ้มตัวสุดท้ายจนเสร็จ กินเวลาไปทั้งบ่ายเลยแฮะ แล้วใกล้หมดเวลากินมื้อเย็นแล้วด้วย แต่งานก็เสร็จ\nแล้วละนะ"

show shizu basic_normal_ss at center
with charaenter

# "Shizune pulls out a roll of measuring tape and a small level, and inspects it thoroughly."
"ชิซูเนะหยิบตลับเมตรและระดับน้ำขนาดเล็กออกมาแล้วตรวจสอบอย่างละเอียด"

show shizu behind_smile_ss
with charachange

# "She smiles, looking pleased, then motions for Misha to come over."
"เธอยิ้มดูพึงใจ จากนั้นจึงทำท่าเรียกมิช่าให้เข้ามา"

show shizu adjust_happy_ss
with charachange

shi "…"

show shizu adjust_happy_ss at tworight
show bg school_council_ss at bgright
with charamove

show misha perky_smile_ss at twoleft behind shizu
with charaenter

# mi "She says you did a very good job. In fact, you might actually have a gift for this."
mi "เธอบอกว่านายทำได้ดีมาก จริง ๆ ก็นายดูมีพรสวรรค์เรื่องงานแบบนี้นะ"

show misha hips_smile_ss
with charachange

# mi "Wow, I'm impressed, too. And that was fast, have you done this before?"
mi "ว้าว ฉันก็ประทับใจเหมือนกัน แถมทำไวด้วย นายเคยทำงานนี้มาก่อนเหรอ"

# hi "No. Never."
hi "ไม่อะ ไม่เคยเลย"

# hi "Never before."
hi "ไม่เคยทำเลยสักครั้ง"

# hi "And I never will again."
hi "แล้วก็จะไม่ทำอีกแล้วด้วย"

show shizu behind_smile_ss
with charachange

shi "…"

# mi "Well, our quota for the day is six stalls. In a few minutes, me and Shicchan should finish this one."
mi "เอาละ วันนี้เราตั้งเป้าไว้ที่หกแผง ซึ่งอีกแป๊บ ๆ ฉันกับชิจังก็จะทำอันนี้เสร็จแล้ว"

show misha hips_grin_ss
with charachange

# mi "That means~… four more to go!"
mi "แปลว่า~… เหลืออีกสี่แผงจ้า!"

show misha sign_smile_ss
with charachange

# mi "We're making good time, she says~!"
mi "พวกเราทำเวลาได้ดีเลย เธอว่างี้~!"
# "ก็พูดได้ไม่เต็มปากหรอกว่าก็แอบดีใจที่พยายามจะชวนกันขนาดนี้ แต่ก็แอบสงสัยนิดนึงว่าในสภานักเรียนเขาทำอะไรกันแน่   ""ก็พูดได้ไม่เต็มปากหรอกว่าก็แอบดีใจที่พยายามจะชวนกันขนาดนี้ แต่ก็แอบสงสัยนิดนึงว่าในสภานักเรียนเขาทำอะไรกันแน่   " exclude #  len"

show misha hips_grin_ss
with charachange

# mi "Isn't this great fun?"
mi "น่าสนุกใช่ไหมล่า"

# hi "What?"
hi "ฮะ?"

# "I could think of a million things I'd rather do, but I suppose everyone has to do their share for the festival, even me."
"ฉันนึกถึงงานอื่น ๆ ที่น่าทำกว่าได้อีกเป็นล้านอย่าง แต่ทุก ๆ คนเองก็คงมีงานที่ต้องทำเพื่องานเทศกาลโรงเรียน\nรวมถึงฉันเองด้วย"

# hi "You're both lucky that I'm helping you two out, if I really didn't want to, I could have gotten out of it easily."
hi "พวกเธอสองคนโชคดีมากนะที่ฉันอุตส่าห์มาช่วยเนี่ย ถ้าฉันไม่อยากทำจริง ๆ ฉันคงหนีไปนานแล้ว"

show shizu basic_normal2_ss
with charachange

shi "…"

show misha perky_smile_ss
with charachange

# mi "Really, Hicchan?"
mi "จริงเหรอ ฮิจัง"

show shizu adjust_smug_ss
with charachange

shi "…"

show misha cross_laugh_ss
with charachange

# mi "Wahaha~! Shicchan thinks you are just running your mouth! Japanese people have no flight or fight reflex, Hicchan~!"
mi "วะฮ่าฮ่า~! ชิซูเนะคิดว่านายแค่พูดลอย ๆ ละ คนญี่ปุ่นน่ะไม่ได้มีสัญชาตญาณตอบสนองแบบฉับพลันยามคับขัน\nหรอกนะ"

# "Shizune tents her fingers deviously."
"ชิซูเนะกางนิ้วของเธอออกอย่างเจ้าเล่ห์"

show shizu basic_happy_ss
with charachange

shi "…"

show misha hips_grin_ss
with charachange

# mi "Definitely~! Definitely, definitely~! If you really wanted to escape, you would have taken immediate action~! That is how you know someone is serious; when they have no doubts, no regrets!"
mi "แน่นอน~! แน่นอน แน่นอน~! ถ้านายอยากจะหนีละก็ นายคงชิงทำตอนนี้เลยแล้วแหละ~! นั่นคือวิธีดูว่าใครคิดจริงทำจริง"

show shizu basic_normal_ss
with charachange

shi "…"

show misha sign_smile_ss
with charachange

mi "แต่เมื่อกี้ไม่น่าบอกเลยนะ เพราะทีนี้ฮิจังก็จะรู้แล้วว่าต้องทำยังไง~"

"แต่เอาจริง ๆ แค่ยอมบอกนี่ก็คงรู้แล้วแหละว่าฉันคงไม่กล้าทำหรอก"

"แต่ยิ่งอยากทำเข้าไปอีก อยากให้มีโอกาสแบบนั้นโผล่มาอีกจังเลยนะ แต่ถ้ามีจริง ๆ เธอก็คงจับฉันทันอยู่ดี"

show shizu behind_smile_ss
with charachange

shi "…"

show misha perky_smile_ss
with charachange

mi "ชิจังบอกว่าตอนนี้เธอมีความสุขละ"

stop music fadeout 1.5

scene bg school_council_ni
with shorttimeskip

play music music_dreamy fadein 0.5

"พอเย็นย่ำพวกเราก็ทำเสร็จไปแล้วหกแผง"

"ด้วยความภาคภูมิที่ทำงานจนแล้วเสร็จ พวกเราก็นั่งชื่นชมผลงานที่ทุ่มแรงลงไปกัน ไม่ได้คุยอะไรกัน แค่ดู"

"รู้สึกคอแห้ง ๆ แฮะ"

hi "เอ้อ ที่โถงทางเดินมันมีตู้ขายของแบบหยอดเหรียญอยู่นี่ เครื่องเปิดอยู่ตลอดใช่มั้ย"

show misha hips_smile at center
with charaenter

mi "อื้ม แถมของก็ถูกด้วย ปกติวันทำงานแบบนี้พวกเราก็ไปซื้ออะไรมาดื่มกัน"

"พอคุ้ยกระเป๋าดูก็เจอเหรียญร้อยเยนเหรียญหนึ่ง"

hi "พอมั้ย พอดีคอแห้งอะ"

show misha hips_grin
with charachange

mi "ร้อยเยนเหรอ ซื้อได้หมดเลยแหละ"

hi "งั้นก็ดี ดีแล้ว"

show misha hips_grin at twoleft
show bg school_council_ni at bgleft
with charamove

show shizu adjust_happy at tworight
with charaenter

shi "…"

show misha sign_smile
with charachange

mi "อ๊ะ เดี๋ยวก่อน"

show misha hips_grin
with charachange

mi "หืม มีอะไรเหรอชิจัง อยากให้เขาซื้อมาให้เธอด้วยเหรอ ฮ่าฮ่าฮ่า!"

show shizu behind_smile
with charachange

shi "…"

show misha perky_smile
with charachange

mi "ฮิจัง วันนี้นายช่วยพวกเราได้เยอะเลย วันนี้ฉัน - หมายถึงชิจังนะ จะเลี้ยงเอง"

show misha perky_confused
with charachange

mi "นี่ แล้วฉันล่ะ"

show shizu adjust_smug
with charachange

shi "…"

show misha perky_smile
with charachange

mi "จะเอาอะไรเหรอ ฉันก็คอแห้งแล้วเหมือนกัน"

show misha perky_confused
with charachange

mi "ฉันก็ด้วยนะ!"

hi "อืม ไม่รู้สิ ยังไงก็ได้ งั้นโซดาเมลอนแล้วกัน"

show shizu behind_smile
with charachange

shi "…"

show misha perky_sad
with charachange

mi "นี่ เดี๋ยว ชิจัง! ฉันก็อยากได้เหมือนกันนะ!"

hide shizu
with charaexit

show misha perky_sad at center
show bg school_council_ni at center
with charamove

mi "โธ่…!"

show misha perky_confused
with charachange

mi "เนี่ย เธอชอบแกล้งกันอย่างนี้ตลอดเลย"

hi "คงงั้นละมั้ง แต่ก็คงซื้ออะไรมาให้เธอแหละ"

mi "อื้ม ปกติก็ซื้อมานะ แต่…มันก็ไม่แน่หรอก…"

hi "ฮะ ๆ "

show misha perky_confused at twoleft
show bg school_council_ni at bgleft
with charamove

show shizu basic_normal2 at tworight behind misha
with charaenter

"ชิซูเนะกลับมาพร้อมโซดาเมลอนสองกระป๋องและน้ำผลไม้อีกกระป๋อง"

"เธอยื่นโซดากระป๋องหนึ่งให้ฉัน อีกกระป๋องให้มิช่า"

show misha hips_grin
with charachange

mi "ขอบใจนะชิจัง~! กะแล้วว่าวางใจเธอให้ซื้อมาด้วยได้จริง ๆ ! วะฮ่าฮ่าฮ่า!"

show misha perky_confused
with charachange

mi "แต่เธอรู้ได้ไงว่าฉันอยากได้อันนี้ ทั้งที่ปกติฉันจะซื้ออย่างอื่นน่ะ"

show shizu behind_smile
with charachange

shi "…"

show misha hips_grin
with charachange

mi "หา? เธอรู้ว่าฉันอยากลองแล้วชอบอะไรเป็นเด็ก ๆ แบบนี้เหรอ ฮ่าฮ่าฮ่าฮ่า!"

show misha hips_laugh
with charachange

mi "ฮ่าฮ่าฮ่าฮ่า!"

"ฉันทำท่าขอบคุณให้ชิซูเนะ เธอยิ้มแล้วพยักหน้า"

show shizu adjust_happy
with charachange

shi "…"

stop music fadeout 4.0

show misha sign_smile
with charachange

mi "นี่ ฮิจัง…"

hi "ว่า"

show shizu behind_smile
with charachange

shi "…"

show misha perky_smile
with charachange

mi "เราอยู่ด้วยกันมาสักพักแล้วนะ ทั้งที่เวลาสั้น ๆ อย่างนี้แต่ทำอะไรไปตั้งหลายอย่าง"

mi "พวกเราจะไม่อ้อมค้อมแล้ว ที่ฉันจะบอกก็คือ"

"ฟังดูอย่างกับจะขอคบงั้นแหละ แต่ไม่ใช่หรอก แต่ถึงงั้นใจฉันก็เต้นรัวเร็ว แม่ง นึกถึงเหตุการณ์ที่คล้าย ๆ กันเมื่อตอน\nต้นปีเลย"

"ฉันนึกจะพูดสักอย่าง แต่สมองยังเลือกไม่ได้ว่าจะบอกให้หยุดหรือพูดต่อ"

"รู้สึกว่าหน้าแดงแจ๋ไปยันหูเลย"

show shizu adjust_smug
with charachange

shi "…"

show misha hips_smile
with charachange

mi "ที่ฉันจะบอกก็คือ…"

show misha hips_grin
with charachange

play music music_ease

mi "นายอยากเข้าสภานักเรียนมั้ย"

hi "เฮ้อ เสียดายจัง"

show misha cross_laugh
show shizu adjust_blush
with charachange

mi "ฮ่าฮ่าฮ่า! ฮ่าฮ่าฮ่าฮ่า! ฮ่าฮ่าฮ่าฮ่าฮ่า! วะฮ่าฮ่า! ฮ่าฮ่าฮ่าฮ่า!"

mi "เมื่อกี้นึกว่าเธอจะขอนายคบเหรอฮิจัง"

mi "ฮ่าฮ่าฮ่าฮ่า! ฮ่าฮ่าฮ่า! ฮ่าฮ่าฮ่า! ฮ่าฮ่าฮ่าฮ่า!"

mi "ฮ่าฮ่าฮ่าฮ่าฮ่าฮ่าฮ่าฮ่า!"

"ฉันอายเอามาก ๆ จนรู้สึกว่าหน้าแดงแปร๊ดหนักกว่าเดิม"

"ชิซูเนะทำท่ากลบเกลื่อนหน้าแดงหลังมิช่าแปลให้แล้วยื่นกระดาษสองสามแผ่นมาให้ฉัน"

show shizu behind_frustrated
with charachange

shi "…"

show misha cross_grin
with charachange

mi "จะเอายังไง เอกสารอะไรอยู่นี่ครบหมดแล้ว"

show misha cross_smile
with charachange

mi "แล้วนายก็นั่งอยู่ทำตัวสบายขนาดนี้ มาดื่มมาคุยอะไรกันแบบนี้อีก~!"

#stop music fadeout 2.0

show shizu basic_normal
with charachange

shi "…"

show misha hips_grin
with charachange

mi "ว่าไง"

"เธอลดเสียงลงแล้วถามอีกรอบด้วยน้ำเสียงจริงจังขึ้นเล็กน้อย"

show misha cross_smile
with charachange

mi "ฮิจัง นายว่าไง"

show misha sign_smile
with charachange

mi "นายก็ไม่ใช่ว่าไม่ชอบใช่มั้ยล่ะ"

#play music music_dreamy fadein 1.5

"ฉันแปลกใจอยู่ไม่น้อยที่อยู่ ๆ น้ำเสียงนั้นเปลี่ยนไป ไม่รู้จะต้องตอบยังไงดี"

"ส่วนหนึ่งคือเธอไม่ได้ตะโกนเสียงดังแบบไม่สนโลก"

"ก่อนหน้านี้เธอคงรู้อยู่แล้วว่าฉันคงบอกปัด"

"แต่คราวนี้เธอดูจริงจัง"

show misha perky_smile
with charachange

mi "ฉันว่านายมาเข้าร่วมเถอะ ไม่ใช่แค่ว่าจะได้มีนายมาช่วยอีกแรงหรอก แต่ นั่นแหละ ยังไงนายก็อยู่กับพวกเราอยู่แล้ว"

mi "ชิจังก็คงอยากให้นายมาเข้าร่วมด้วย นายก็ไม่ได้เกลียดพวกเราหรืออะไรใช่มั้ยล่ะ"

show misha perky_sad
with charachange

mi "มาเข้าร่วมก็ไม่เสียหายหรอก แล้วถ้านายมาฉันก็ยินดีมาก ๆ "

"เธอดูชั่งใจอยู่นานกว่าจะพูดได้แต่ละประโยค ซึ่งแปลกสำหรับคนพูดมากอย่างมิช่า"

"จนฉันรู้สึกเป็นห่วงแปลก ๆ "

show shizu behind_blank
with charachange

"ฉันหันมองไปทางชิซูเนะที่จ้องฉันกลับมาทันที เธอทำท่าขัดเล็บไปเรื่อยเปื่อย"

show misha perky_smile
with charachange

mi "ถ้านายไม่อยากเข้าร่วม ฉันสัญญาว่าจะไม่เซ้าซี้อีกแล้ว แต่ถ้านายตกลง พวกเราจะมีความสุขมาก ๆ "

"ทั้งชิซูเนะและมิช่าดูจะไม่อยากมองตาฉันตรง ๆ "

"ให้ว่ากันตามตรง แค่คิดว่าจะได้อยู่กับสาวน้อยน่ารักสองคนอย่างนี้แล้วก็ไม่อยากปล่อยโอกาสไปเลย"

"ฉันก็ไม่ได้อยากทำงานอย่างนี้ทุกวันหรอก แต่หลังงานเทศกาลแล้วงานคงซาลงบ้าง"

"หวังว่าอะนะ"

hi "ก็ได้ คงไม่เสียหายอะไรเหมือนกัน ตกลง"

show shizu adjust_happy
with charachange

shi "…"

show misha hips_grin
with charachange

mi "ยอดเยี่ยม ยอดเยี่ยม! อะฮ่าฮ่าฮ่า~!"

"ชิซูเนะกางนิ้วออกอย่างพอใจ"

show shizu basic_happy
with charachange

shi "…"

show misha perky_smile
with charachange

mi "เดี๋ยวเธอจะกรอกเอกสารให้เองนะฮิจัง ยินดีด้วย นายได้เป็นสมาชิกสภานักเรียนอย่างเป็นทางการแล้วนะ!"

hi "เยี่ยม ฉันจะตั้งตาคอยได้ทำงานแบบไม่เยอะนะ"

hi "เอาตรง ๆ ฉันก็ไม่เคยทำกิจกรรมสภานักเรียนอะไรเลย"

hi "แต่ก็คงจะเป็นประสบการณ์ที่ดีละมั้ง"

"มิช่าเริ่มปรบมือพลางหัวเราะด้วยพลังอันเหลือล้นไปด้วย"

show misha hips_laugh
with charachange

mi "ยินดีด้วยนะฮิจัง!"

show shizu adjust_smug
with charachange

shi "…"

mi "ยินดีด้วยนะ!"

show shizu behind_smile
with charachange

shi "…"

mi "ยินดีด้วยนะ!"

show shizu adjust_happy
with charachange

shi "…"

mi "ยินดีด้วยนะ!"

hi "รู้แล้วน่า"

"ฉันอดยิ้มไม่ได้กับความน่ารักของท่าทีที่เป็นเด็ก ๆ นั้น"

show misha hips_grin
with charachange

mi "สภานักเรียนงานยุ่งตลอดอยู่แล้วน่า แต่วันนี้งานหมดแล้ว เจอกันพรุ่งนี้นะฮิจัง!"

show misha hips_smile
with charachange

mi "พรุ่งนี้เรายังมีงานต้องทำกันอยู่ ฝากนายด้วยนะ!"

stop music fadeout 4.0

scene bg school_hallway3
with locationchange

"ฉันออกห้องมาด้วยความอ่อนล้าเต็มทน ตามลานโรงเรียนก็ไม่มีใครแล้ว มืดค่ำป่านนี้แล้วยิ่งทำให้โรงเรียนดูชวนให้\nขนลุกขนพอง ที่ห้องสภานักเรียนเป็นหน้าต่างบานเดียวที่ไฟยังติดอยู่"

"สภานักเรียนเขาทำงานกันอย่างนี้เหรอ สังขารฉันจะไหวมั้ยเนี่ย"



#*****************************

label th_A23:

scene bg school_scienceroom at bgleft
with shorttimeskip

play music music_tranquil fadein 3.0

"และฮานาโกะก็ไม่ได้มาในคาบเช้าเลย ปล่อยให้ที่นั่งของเธอดูว่างเปล่าและเงียบเหงาอยู่ที่หลังห้องเรียน"

"ถ้าได้เจอเธอคงต้องบอกว่าลิลลี่ตามหาเธออยู่"

"พอมีเรื่องเมื่อเช้าแล้วคาบเรียนนี่ก็ดูน่าเบื่อไปเลย"

"ฉันต้องคอยตามเนื้อหาที่เรียนให้ทัน ถึงตอนอยู่ที่โรงพยาบาลจะอ่านหนังสือเรียนตามแล้วก็เถอะ แต่ตอนนี้ไม่มีอารมณ์\nอยากเรียนเท่าไหร่"

"เสียงนาฬิกาที่ด้านหน้าห้องดังจนน่ารำคาญ ครูก็ไม่พูดอะไรเลยกว่าเจ็ดนาที แต่กลับเลือกที่จะเขียนสมการจากหนังสือบน\nกระดานจนเต็มไปหมด"

"เสียงกระทบของชอล์กกับกระดานนั้นดังประสานอย่างเป็นจังหวะไปพร้อมกับเสียงนาฬิกาเดิน"

"ฉันลอกสมการบนกระดานลงสมุดเพื่อฆ่าเวลา แม้ในหนังสือเรียนจะมีเหมือนกันก็ตาม"

scene bg school_scienceroom at bgright
with shorttimeskip

play sound sfx_normalbell

"พอเสียงระฆังดัง ฉันนั่งรอสักพักเพราะไม่ได้มีธุระรีบร้อนอะไรพลางทบทวนเนื้อหาที่ได้เรียนในวันนี้ ยังไงฉันเองก็\nอยากจะออกคนท้าย ๆ อยู่แล้ว จะได้ไม่ต้องไปเบียดกับคนหมู่มากที่โถงทางเดิน"

"ฉันสังเกตเห็นชิซูเนะกับมิช่ายังอยู่ด้วย คุยกับใครสักคนจากห้องอื่น"

"ชิซูเนะส่งภาษามือเร็วมากจนมือเธอทำเสียงเหมือนดาบที่ฟันตัดอากาศ"

"มิช่าพยายามอย่างหนักเพื่อที่จะตามให้ทัน แต่ก็เห็นได้ชัดว่าเธอแทบไม่เข้าใจเลยด้วยซ้ำ"

"ฉันฟุบหน้าลง ไม่รู้หรอกว่าคุยอะไรกันอยู่ แต่ดูท่าว่าจะเป็นเรื่องจริงจังน่าดู และฉันคงไม่น่าจะช่วยอะไรได้ด้วย แล้ว\nชิซูเนะเองก็ดูโมโหด้วย ถึงจริง ๆ ปกติท่าทางเธอก็เป็นแบบนี้อยู่แล้วละนะ"

"ชิซูเนะทำภาษามือมากจนข้อมือเธอเริ่มดังกรอบแกรบ และมิช่าก็เริ่มลิ้นพันกันแล้ว"

"บางทีก็พูดผิดเหมือนเวลาต้องพูดคำยาก ๆ ติด ๆ กัน แถมยังต้องทำภาษามือแปลกลับทุก ๆ คำพูดที่คนอื่นพูดด้วย"

"ช่างเป็นงานที่หนักจริง ๆ"

"มิช่าดูหมดแรง คลับคล้ายว่าจะเป็นลม"

"โชคยังดีที่ไม่นานเรื่องก็จบลง และพวกเธอก็กลับมานั่งที่อีกครั้ง"

show shizu behind_blank at tworight
show misha perky_sad at twoleft
with charaenter

mi "อ๊าาาาา! เหนื่อยจังเลย!"

"เธอห้อยหัวฟุบลงกับโต๊ะด้วยท่าทีหมดแรง"

"ถือโอกาสนี้ง้อชิซูเนะหน่อยแล้วกัน ต้องระวังไม่ให้โดนลากไปเรื่องสภานักเรียนอีก แต่คงจะเป็นไปไม่ได้ละนะ"

hi "เตรียมงานเทศกาลกันเหนื่อยน่าดูเลยนะ"

"ดูเหมือนว่าคนในโรงเรียนนี้จะจริงจังกับงานเทศกาลนี้มาก พออยู่กันว่าง ๆ ทีไรฉันเห็นเป็นต้องคุยกันเรื่องนี้ตลอด"

"เห็นทุกคนจริงจังขนาดนี้กับงานนี้ก็ดี"

"ฉันคงเป็นคนเดียวละมั้งที่ไม่มีอะไรให้ทำเลย"

show shizu basic_angry
with charachange

"ชิซูเนะหัวเราะหึราวกับคิดอยู่ว่าจะเมินหรือเยาะเย้ยฉันดี แต่สุดท้ายก็ไม่ได้ทำทั้งคู่แล้วเริ่มทำภาษามือแทน"

show misha perky_confused
with charachange

"มิช่าเงยหน้าขึ้นมามองไปที่มือของเธอด้วยสายตาเบลอ ๆ เล็กน้อย"

show shizu behind_frown
with charachange

shi "…"

"เธอส่งภาษามือด้วยท่าทางที่ดูรุนแรง หนักแน่น และเล่นใหญ่"

"มิช่าแปลภาษามือนั้นเป็นคำพูดให้ฉัน"

"ซึ่งเธอทำได้ดีเหมือนชิซูเนะพูดเองเลยทีเดียว อารมณ์และความคิดของเธอถูกส่งต่อมาที่ฉันผ่านทางมิช่า"

"คงฝึกมาเยอะเลยสินะ"

show misha cross_frown
with charachange

mi "ก็แหงอยู่แล้ว พวกเราเป็นสภานักเรียนนี่ เนี่ยนายรู้ไหมว่าเรายุ่งมาก"

show shizu basic_frown
with charachange

shi "…"

show misha sign_smile
with charachange

mi "เพราะหน้าที่สำคัญของเราคือการทุ่มเทให้งานเทศกาลออกมาดีที่สุด"

show shizu behind_frown
with charachange

shi "…"

show misha hips_frown
with charachange

mi "ถ้าเกิดว่างานล้มเหลวแล้วเราคงไม่มีหน้าไปเจอกับสภานักเรียนรุ่นก่อน ๆ แน่"

show shizu adjust_angry
with charachange

shi "…"

show misha sign_smile
with charachange

mi "เพราะงั้นจะให้มีตกหล่นหรือเกิด…เอ่อ น่าจะคำว่า “อุปสรรค” นะ ไม่ได้ งานเทศกาลต้องออกมาดีไม่มีที่ติเลย"

"ทั้งบทสาธยายของชิซูเนะที่เปี่ยมล้นด้วยแรงใจกับบทแสดงที่มิช่าทำนั้นดูเหมาะดีพิลึก"

stop music fadeout 2.0

show shizu adjust_blush
show misha perky_confused
with charachange

mi "อ้าว ดีจ้า~!"

show shizu adjust_blush at offscreenleft
show misha perky_confused at Transform(xanchor=0.5, xpos=-0.45)
show bg school_scienceroom at bgleft
with charamove

show hanako emb_timid at Transform(xanchor=0.5, xpos=0.93)
with charamoveinright

play music music_pearly fadein 1.0

"พอหันไปข้างหลังเห็นฮานาโกะกำลังมองเข้ามาในห้องเรียนอย่างอาย ๆ โดยซ่อนตัวของเธอเกินครึ่งไว้หลังประตู"

show misha perky_smile at Transform(xanchor=0.5, xpos=0.15)
with charamove

mi "นี่เธอ! ทำตัวเกเรอีกแล้วเหรอ"

show hanako emb_blushtimid
with charachange

"ฮานาโกะหน้าแดงแจ๋ทันทีที่มิช่าพูดแซว ถึงแม้จะไม่ได้ว่าจริงจังอะไรมาก"

show shizu basic_angry at Transform(xanchor=0.5, xpos=0.35)
with charamove

shi "…"

show hanako emb_downsad
with charachange

show hanako emb_downsad at Transform (xanchor=0.5, xpos=0.97)
with charamove

"ชิซูเนะมองเธอด้วยความสงสัย ทำให้ฮานาโกะก้มหน้าแล้วถอยหนีไปจนเห็นเพียงนิ้วของเธอเท่านั้นที่จับขอบประตูด้วย\nความประหม่า"

"บางทีคงเพราะเธอไม่ชอบลิลลี่เลยพาลทำท่าไม่ชอบฮานาโกะไปด้วย"

"คงจะเป็นแบบนั้น และฮานาโกะเองก็รู้ตัวเช่นกัน"

hi "มีอะไรเหรอฮานาโกะ"

show hanako emb_timid
with charachange

ha "ละ… ลิลลี่อยู่ไหม"

mi "โทษทีจ้า คุณซาโต้ไม่อยู่ที่นี่ เธอ เอ่อ มาเมื่อเช้าน่ะ"

show hanako emb_downtimid
with charachange

"ฮานาโกะยังคงมองชิซูเนะอย่างไม่สบายใจ ซึ่งชิซูเนะก็จ้องกลับมาที่เธอด้วยสายตาที่จดจ่ออย่างเคย คิดจะทำอะไรกันนะ"

"แน่นอนว่าชิซูเนะไม่หยุดมองแน่ ๆ และเธอก็ท่าทางน่ากลัวด้วย สภาพนี้ฮานาโกะคงจะกลัวเอามาก ๆ แน่ ๆ"

"พอดูปฏิกิริยาของฮานาโกะที่มีต่อนิสัยปกติของชิซูเนะแล้วก็แอบอึดอัดเหมือนกัน นี่คงเป็นสิ่งที่จะเกิดขึ้นเมื่อสองคน\nที่นิสัยต่างกันสุดขั้วมาเจอกันสินะ"

show hanako emb_timid
with charachange

ha "แล้ว… แล้วเธอรู้ไหมว่าลิลลี่อยู่ไหน"

show shizu behind_frown
with charachange

shi "…"

show misha hips_frown 
with charachange

mi "ถ้าเธอคนนั้นมีจิตสำนึกสักหน่อย เธอก็คงจะอยู่ห้องเธอช่วยจัดงานเทศกาลแหละ แต่ใครจะรู้ เธอคนนั้นอาจจะจะหนี\nไปซ่อนตัวที่ไหนก็ได้"


label th_A23a:

scene bg school_scienceroom at bgleft
show hanako emb_timid at Transform (xanchor=0.5, xpos=0.97)
show shizu behind_frown at Transform(xanchor=0.5, xpos=0.35)
show misha hips_frown at Transform(xanchor=0.5, xpos=0.15)
with None

hide hanako
with charamoveoutright

"ฮานาโกะรีบพยักหน้าแล้วถอยหนีอย่างรวดเร็ว"

stop music fadeout 2.0

show misha hips_grin
with charachange

mi "เมื่อกี้คุยเรื่องอะไรกันอยู่นะ อ๋อ ใช่ พวกเราน่ะทุ่มเทเรื่องการจัดงานมาก"

"แล้วก็ทำคนอื่นเขาเป็นบ้าไปด้วย"

hi "อืม โชคดีแล้วกัน"

"ฉันลุกขึ้นเตรียมเดินหนีก่อนที่ใครสักคนจะทันมาด่าเรื่องที่ฉันขี้เกียจอีก"

scene bg school_hallway3
with locationchange

"โถงทางเดินนั้นค่อนข้างเงียบอย่างที่คิด ทุกคนคงกำลังทำกิจกรรมชมรมกันอยู่ ไม่ก็ไปเตรียมงานเทศกาลกัน หรือไม่ก็\nทั้งสองอย่าง"

"เสียงที่ชิซูเนะตามจิกเรื่องที่ฉันอู้ยังก้องอยู่ในหัว"

"แอบรู้สึกผิดเหมือนกันที่ไม่ได้ไปเข้าร่วมจัดงาน แต่ฉันก็คงไม่ได้มีกะจิตกะใจจะไปทำอะไรให้เป็นชิ้นเป็นอันขนาดนั้น"

"ส่วนจะให้ไปช่วยงานเทศกาลอะไรอีกก็คงสายไปแล้ว เว้นเสียแต่ว่าจะไปช่วยชิซูเนะและมิช่า ซึ่งฉันไม่ไปแน่ ๆ ละ\nส่วนเรื่องชมรม…ไม่รู้สิ"

"ฉันคงไม่ใช่พวกที่ชอบเข้าชมรมเท่าไหร่"

play music music_soothing fadein 4.0

scene bg school_dormext_half
with locationskip

"พอเดินมาจากโรงเรียนมายังหอได้ครึ่งทางก็เห็นคนหนึ่งที่อยู่ตรงหน้าหอ"

"เป็นริน"

"วันนี้ก็คงมาวาดภาพเขียนผนังของเธออีกแล้วสินะ"

"ฉันเดินไปหา แต่เธอดูจะไม่รู้สึกตัวว่าฉันกำลังเดินเข้ามา"

scene bg mural_unfinished
show rin basic_awayabsent_close at tworight
with locationchange

"เธอนั่งอยู่บนลังที่คว่ำอยู่ จับจ้องผนังที่เธอกำลังลงสีโดยการลากเท้าที่คีบแปรงไปมา"

"งานเดินมาได้ค่อนข้างเยอะแล้วเมื่อเทียบกับเมื่อวาน แต่เท่าที่เห็นก็ดูจะยังเสร็จไปเพียงครึ่งหนึ่งเท่านั้น"

"สีสันที่แต่งแต้มมีมากขึ้น พร้อมกับรูปร่างคล้ายมนุษย์ที่ดูบิดเบี้ยวที่เพิ่มขึ้น"

"ต้องยอมรับเลยว่าเป็นสไตล์ที่เตะตาและมีเอกลักษณ์ทีเดียว ฉันไม่ได้มีความรู้เรื่องศิลปะอะไรมากมาย แต่ถึงอย่างนั้น\nฉันก็เห็นว่าเป็นภาพที่สวยมาก"

"ฉันกระแอมไอเรียกความสนใจจากเธอ แต่ก็ไม่ได้ดังจนทำเธอที่จดจ่ออยู่ตกใจ"

rin "รอเดี๋ยว"

"เธอไม่หันมามองว่าใครมาด้วยซ้ำ"

"รอก่อนแล้วกัน"

stop music fadeout 6.0

"…"
    
"…"

"…"
    
"…"

with shorttimeskip

"…"

"ผ่านไปได้สิบห้านาทีฉันก็รู้สึกว่าเธอคงยังจดจ่อไม่สนใจอะไรจริง ๆ ในเมื่อรอนานขนาดนี้แล้วฉันจึงสะกิดไหล่เธอให้รู้\nว่าฉันอยู่ด้วย"

"เธอหันหน้าช้า ๆ นิ่ง ๆ มาทางฉัน แล้วจ้องอยู่ที่บริเวณเป้าของฉัน"

show rin basic_deadpan_close
with charachange

rin "อ้อ ฮิซาโอะ"

play music music_rin fadein 0.3

"รู้ด้วย? แต่ถ้ามองหน้ากันน่าจะดีกว่าน่ะนะ"

hi "สายตาเฉียบคมเสียจริง ตั้งใจทำงานอยู่สินะ"

"บทสนทนาเริ่มขึ้นเหมือนฉันเพิ่งมาโดยไม่ได้รออยู่ 15 นาที แต่ก็ไม่เป็นไร อย่างน้อยก็ได้คุยแล้ว"

hi "สวยดีนะ"

"ซึ่งก็สวยจริง สีซ้อนทับกันไปมา รูปร่างมนุษย์ที่ถูกวาดและหลอมรวมกันเกิดเป็นภาพที่สร้างความประทับใจ แต่ริน\nทำหน้าเหมือนไม่เล่นด้วย"

show rin basic_deadpanupset_close
with charachange

rin "ห้ามพูดถึงงานที่ยังไม่เสร็จสิ โชคร้ายเจ็ดปีนะ"

hi "ฟังดูไม่ดีเลยแฮะ งั้นขอถอนคำพูดแล้วกัน"

"แต่ก็สวยอะนะ นี่ฉันคิดแล้วจะโชคร้ายไปสิบสี่ปีเลยหรือเปล่าเนี่ย"

show rin basic_awayabsent_close
with charachange

"รินหันกลับไปมองที่ภาพเขียนแล้วใช้นิ้วโป้งเท้าจิ้ม ๆ "

show rin relaxed_nonchalant_close
with charachange

rin "ผสมสีนี้มาให้หน่อยได้มั้ย พอดีใกล้หมดแล้ว"

"เธอมองมาที่ถ้วยที่มีสีชมพู ๆ อย่างเดียวกันที่พร่องไปครึ่งหนึ่ง"

"แต่ที่มาก็ไม่ได้ตั้งใจจะมาอยู่ช่วยน่ะนะ…ก็ไม่ได้จะทำอะไรอยู่แล้วนั่นแหละ"

show rin basic_absent_close
with charachange

"ฉันมองริน ส่วนเธอก็มองกลับเหม่อ ๆ "

hi "แค่ครั้งนี้ครั้งเดียวนะ"

show rin basic_awayabsent_close
with charachange

"รินคีบแปรงอีกอันหนึ่งแล้วมาจุ่มที่ถ้วยสีแดงสีจาง รอบ ๆ ตัวเธอมีถ้วยอย่างเดียวกันวางเต็มไปหมด ดูจากสภาพคงนั่งทำ\nมาแล้วหลายชั่วโมงเหมือนกัน"

"จะเป็นอย่างนั้นหรือเปล่านะ ถ้าใช่ก็แปลว่าเธอโดดเรียนด้วย ซึ่งดูจากสภาพคนอย่างรินแล้วก็ไม่เหนือความคาดหมาย\nสักเท่าไหร่"

"ฉันเทสีขาวและแดงผสมกันอย่างละหน่อย คอยกะให้ออกมาเป็นสีชมพูที่อยู่บนผนังนั้น"

"เหมือนจะไม่ได้สักที"

"จริง ๆ ก็ควรผสมสีให้พอใช้แต่แรกอยู่แล้ว จะผสมให้ได้สีเดียวกันแบบเป๊ะ ๆ คงเป็นไปไม่ได้ แต่อย่างน้อยก็ต้องลองกะให้\nใกล้เคียงที่สุดแล้วกัน"

hi "พูดถึงงาน งานนี้ไม่หนักไปหน่อยสำหรับเธอเหรอ ภาพก็ตั้งใหญ่"

show rin basic_deadpan_close
with charachange

rin "อ้อ ฉันไม่ได้แก่พอจะมานั่งนึกหงุดหงิดอะไรอย่างนั้นหรอก"

hi "ก็คงจะไม่แหละนะ"

show rin basic_deadpannormal_close
with charachange

rin "ตามนั้นเลยแหละ"

show rin basic_deadpancontemplation_close
with charachange

rin "แต่เจ็บขา เหมือนเป็นทาก ทากที่ทำจากทากทะเล"

hi "เพราะอยู่ท่านี้นานไปหรือเปล่า"

rin "อืม ฉันชอบทำแนวนอนมากกว่า นายเข้าใจใช่มั้ย"

rin "ช่วยไม่ได้ละนะ จะขอให้กำแพงมันนอนลงก็ไม่ได้"

show rin negative_spaciness_close
with charachange

"เธอพูดพลางยืดเส้นยืดสายเล็กน้อย ขาของเธอนั้นงอไปมาได้มากกว่ามนุษย์ทั่ว ๆ ไป เวลาเห็นเธอขยับตัวได้อย่าง\nไม่ติดขัดอะไรเลยแล้วก็ทึ่งดี"

show rin negative_annoyed_close
with charachange

show rin negative_spaciness_close
with charachange

"ใบหน้าอันเรียบนิ่งของเธอมีอาการเบ้ไปเล็กน้อย—น่าจะเจ็บ—ระหว่างที่เธอยืดน่อง"

"ทั้งกำลังและความคล่องตัวของรินคงมีมากกว่าคนทั่วไปถึงจะใช้ชีวิตได้อย่างนี้ แต่พอเธอมานั่งวาดแล้วทั้งสองอย่างที่ว่า\nก็ถูกใช้หมดไปเรื่อย ๆ "

hi "จะฝืนตัวเองอะไรขนาดนั้น พักสักหน่อยเถอะ ถ้าไม่ดีขึ้นค่อยต่อพรุ่งนี้ก็ได้"

show rin basic_deadpannormal_close
with charachange

"เธอนิ่งไป"

"นานด้วย เหมือนความคิดเธอว่างไปพักหนึ่ง"

"…"

show rin basic_deadpan_close
with charachange

rin "ฉันว่าไม่หรอกฮิซาโอะ"

rin "ฉันไม่ได้ฝืนตัวเองสักหน่อย"

hi "สภาพอย่างนั้นฉันว่าฝืนแน่ ๆ "

show rin basic_deadpannormal_close
with charachange

rin "เปล่า ไม่ใช่เรื่องฝืนฝืดหรืออะไรอย่างนั้น"

show rin basic_awayabsent_close
with charachange

rin "มีผู้ชายอยู่คนหนึ่ง"

hi "ผู้ชาย?"

show rin basic_absent_close
with charachange

rin "ใช่"

hi "อยู่ที่ไหน"

show rin basic_deadpannormal_close
with charachange

rin "ที่ชมรมศิลปะ"

hi "เอ่ออ…แล้ว?"

show rin basic_deadpan_close
with charachange

rin "ตาเขาบอด"

hi "อ้าว ตาบอดแล้ววาดรูปได้ยังไง"

show rin basic_awayabsent_close
with charachange

rin "ไม่รู้สิ"

hi "แล้วทำไมถึงมาอยู่ที่ชมรมศิลปะ"

show rin basic_absent_close
with charachange

rin "นั่นแหละสาระ เขาอยู่ที่ชมรมศิลปะ"

"จริง ๆ เธอน่าจะพูดให้มันมากกว่าแค่การถามคำตอบคำนะ จะได้เหมือนการคุยกันจริง ๆ ไม่ใช่การสอบปากคำน่ะ"

show rin basic_awayabsent_close
with charachange

rin "เขาทำอะไรที่เป็นคำว่าศิลปะไม่ได้เลยใช่มั้ย แต่เขาก็มาเข้าชมรมศิลปะแล้ววาดรูปอยู่ดี"

show rin basic_deadpannormal_close
with charachange

rin "เพราะอะไร"

hi "ไม่รู้สิ เพราะอะไรเหรอ"

show rin basic_deadpan_close
with charachange

rin "ไม่รู้สิ ถึงได้ถาม"

hi "แล้ว?"

show rin basic_deadpannormal_close
with charachange

rin "เขาไม่ได้วาดรูปบ่อย แต่ฉันว่าภาพที่เขาวาดน่าสนใจดีนะ"

hi "ฉันก็ว่างั้น"

show rin basic_lucid_close
with charachange

rin "ฉันเคยลองทำนะ หลับตาวาดรูป"

show rin basic_deadpannormal_close
with charachange

rin "ไม่ได้น่าสนใจอะไรขนาดนั้น แล้วกว่าจะเช็ดพื้นให้สะอาดอีก เลยไม่เอาอีก"

show rin basic_deadpandelight_close
with charachange

rin "แต่เขาก็ปั้นเก่งขึ้นนะ"

hi "อย่างนี้เอง"

"บางทีเธออาจจะใช้เรื่องนี้สื่ออะไรสักอย่าง บางทีเธอคงจะลืมแล้วว่าจะสื่ออะไร"

hi "ชมรมศิลปะดูจะมีแต่คนน่าสนใจนะ"

show rin basic_deadpan_close
with charachange

rin "ไม่หรอก"

"ตอบมาทื่อ ๆ เลยแฮะ แถมไม่เข้าใจที่ฉันประชดไปอีก"

hi "ไม่เหรอ"

show rin basic_awayabsent_close
with charachange

rin "อย่างที่บอก พวกนั้นไม่ได้น่าสนใจอะไรมาก ปกติฉันไม่สนใจคนที่ไม่น่าสนใจเท่าไหร่"

show rin basic_absent_close
with charachange

rin "นายอาจจะสนใจ"

hi "อาจจะนะ"

"…"

show rin basic_awayabsent_close
with charachange

rin "แต่ผู้ชายคนนั้นน่าสนใจนะ"

show rin basic_lucid_close
with charachange

rin "บางทีฉันคงเหมือนผู้ชายคนนั้น หรือบางทีนายคงเหมือน บางทีทุกคนคงเหมือน"

rin "ทำอะไรที่ทำไม่ได้เพราะทำได้"

"ฟังดูลึกล้ำดีแฮะ ฉันบอกริน"

hi "เธอเป็นคนที่ลึกล้ำดีนะ"

show rin basic_deadpannormal_close
with charachange

rin "ไม่อะ ฉันเป็นคนไม่มีสมองเอาแต่คิดตื้น ๆ จะตาย มีแต่คนบอกฉันแบบนั้น"

show rin basic_deadpanamused_close
with charachange

rin "นายรู้มั้ยว่าฉันคิดอะไรได้แค่สี่อย่างพร้อม ๆ กัน"

hi "ไม่รู้ แต่ตอนนี้รู้แล้ว"

show rin basic_lucid_close
with charachange

rin "ตอนนี้ฉันคิดถึงห้องน้ำหญิงที่อยู่ชั้นสอง ไอศกรีมรสไอศกรีม นิ้วกลางเท้า แล้วก็ตัดผม"

show rin basic_awayabsent_close
with charachange

rin "เดี๋ยวต้องไปตัดผม"

show rin negative_spaciness_close
with Dissolve(0.1)

show rin basic_delight_close
with Dissolve(0.1)

show rin negative_spaciness_close
with Dissolve(0.05)

show rin basic_delight_close
with Dissolve(0.05)

show rin negative_spaciness_close
with Dissolve(0.05)

show rin basic_delight_close
with Dissolve(0.05)

show rin negative_spaciness_close
with Dissolve(0.1)

show rin basic_delight_close
with Dissolve(0.2)

"เธอสั่นหัวแรง ๆ จนผมสั้น ๆ ยุ่ง ๆ ของเธอสะบัดไปมา ดูท่าแล้วเธอจะชอบทำอย่างนี้"

show rin basic_awayabsent_close
with charachange

"พวกเราเงียบไปเมื่อรินเริ่มเดินเลื่อนลอยไปมาพลางเขี่ยพุ่มไม้เล่น เรื่องชมรมศิลปะนั้นยังคงค้างอยู่ในหัวฉัน"

"รู้สึกเหมือนเข้ามาย่ำแดนสนธยาที่เรียกว่าศิลปะเลย แต่ละทีที่ได้มาเจอรินรู้สึกอย่างกับมาเริ่มเสพติดบุหรี่ยังไงยังงั้น\nหรือจะเลิกคุยกับเธอดี"

"ไม่ใช่ว่าไม่ชอบหรอก ถึงเธอจะทำตัวงง ๆ ก็เถอะ แล้วฉันก็ไม่ได้เกลียดศิลปะขนาดนั้น บางทีฉันยังวาดรูปเล่นอยู่เลย\nเพียงแต่ฉันไม่ได้มีหัวสร้างสรรค์ขนาดนั้น ฝีมือก็ไม่มี"

"ปกติเวลาจะวาดรูปอะไรก็จะชอบเป็นโรคกระดาษขาวแล้วแน่นิ่งไปเลย"

"หรือไม่ก็จะวาดอะไรบิด ๆ เบี้ยว ๆ แล้วพาลหงุดหงิดที่ดึงภาพที่อยู่ในหัวมาวาดลงกระดาษไม่ได้ แล้วก็ล้มเลิกก่อนจะทัน\nได้พยายามอะไรให้มันจริงจัง"

"แน่นอนว่ารินไม่ได้มีปัญหาอะไรอย่างที่ว่า…แต่เธอทำให้ฉันหงุดหงิดไปอีกแบบ เวลาอยู่กับเธอแล้วเหมืองมองกระจก\nที่ไม่สะท้อนอะไรกลับมาเลย"

"พอทำไปแล้วก็จะนึกสงสัยว่าตัวเองยังสติดีอยู่หรือเปล่า"

show rin basic_absent_close
with charachange

"รินนั่งลงกับลังแล้วโยกตัวไปมาดูไม่อึดอัดอะไรกับความเงียบอันน่าอึดอัดนี้ เธอมองมาที่ฉันอีกครั้ง ไม่ก็มองที่ไหล่ ฉัน\nมองไม่ค่อยออกว่าตาเธอจดจ่ออยู่ที่ไหนกันแน่"

"ไปดีกว่า เธอจะได้ทำงานได้โดยไม่มีใครกวน ส่วนฉันก็จะไปทำอะไรอยู่คนเดียว แต่วันนี้ฉันก็ไม่ได้มีอะไรให้ทำหรอก…"

hi "โอ๊ะ ตายแล้ว"

show rin basic_deadpan_close
with charachange

rin "ใครตาย"

hi "ไม่ใคร ฉันแค่ลืมบอกฮานาโกะน่ะว่าลิลลี่ตามหาอยู่"

hi "รู้จักมั้ย ฮานาโกะห้องฉันน่ะ"

show rin basic_deadpanamused_close
with charachange

rin "อ๋อ คนนั้นเหรอ สาวห้องน้ำลึกลับน่ะเอง"

show rin basic_amused_close
with charachange

rin "เป็นคนตลกดีนะ เห็นช่วงพักเมื่อสามสัปดาห์ที่แล้วไปเข้าห้องน้ำตั้งห้ารอบ เป็นสถิติโลกเลยแน่ ๆ "

show rin basic_deadpandelight_close
with charachange

rin "ลึกลับมาก ๆ "

hi "เพราะงั้นถึงได้เรียกว่าสาวห้องน้ำลึกลับเหรอ"

show rin basic_absent_close
with charachange

rin "แล้วจะมีเหตุผลอะไรอย่างอื่นอีกล่ะ อืม แต่ถ้ามีก็คงเป็นเรื่องลึกลับไปตลอดกาล พอดีฉันไม่ได้ตามเธอเข้าไปด้วย"

"…"

show rin basic_awayabsent_close
with charachange

rin "หรือเป็นสัปดาห์ก่อนหน้านั้นอีกนะ เป็นไปได้"

"…"

rin "พอเห็นเธอก็หิวขึ้นมาเลย"

hi "ห้ามพูดอย่างนั้น"

hi "อย่างน้อยก็ห้ามพูดตอนเจ้าตัวเขาอยู่ด้วย"

show rin basic_deadpannormal_close
with charachange

"รินมองฉันกลับเหม่อ ๆ เหมือนไม่แน่ใจว่าทำไมฉันถึงตำหนิเธอไป"

"แต่เธอก็ไม่ได้ทำท่าว่าจะเข้าใจขึ้นมาจากเมื่อครู่เลย ฉันเลยปล่อย ๆ ไป"

hi "แล้วอยากกินข้าวเย็นแล้วเหรอ"

show rin basic_awayabsent_close
with charachange

rin "ไม่ ยัง"

"สายตาอันโหยหิวของรินหันกลับไปมองที่ผนัง เธอดูมีแรงขึ้นมาเล็กน้อย หรืออย่างน้อยก็ไม่ได้ดูเอื่อยอย่างเมื่อกี้แล้ว"

"ราวกับว่าผนังนั้นคือศัตรูที่เธอต้องกำราบ เป็นสิ่งที่ต้องล้มให้ได้ก่อนจะได้ไปทานมื้อเย็นให้อร่อย"

"เข้าใจเลยแหละ ฉันรู้สึกเข้าใจเธออย่างประหลาดจนฉันยิ้มน้อย ๆ อยู่กับตัวเอง"

"แม้จะแปลก แต่เธอก็เจ๋งดี"

hi "เดี๋ยวไปละนะ"

hi "ขอให้สนุก"

stop music fadeout 3.0

"รินคีบแปรงขึ้นมาจุ่มสีอีกครั้งแล้ว จึงไม่แปลกที่เธอไม่ได้ยินฉันอีก หรือต่อให้ได้ยินเธอก็ไม่ตอบอะไร"



#*******************************

label th_A24:

stop music fadeout 6.0

scene bg school_scienceroom at bgleft
show hanako emb_timid at Transform (xanchor=0.5, xpos=0.97)
show shizu behind_frown at Transform(xanchor=0.5, xpos=0.35)
show misha hips_frown at Transform(xanchor=0.5, xpos=0.15)
with None

show bg school_scienceroom at right #omg hax
show hanako emb_timid at right
show shizu behind_frown at offscreenleft
show misha hips_frown at offscreenleft
with charamove

hide misha
hide shizu
with None

hi "You need to find her? She was looking for you in the morning but I guess you have missed each other."

"She waits a little without answering the simple question, looking awfully like she's not sure if it's proper to answer such a question."

show hanako emb_blushtimid
with charachange

ha "Y…yeah."

hi "I can come with you."

hi "If it's okay."

show hanako emb_downtimid
with charachange

show hanako emb_blushtimid
with charachange

"Hanako nods fractionally, still on guard, her shoulders stiff like wood. I get the feeling that she might be more comfortable by herself after all, but it's too late to back off now."

"She has this really troubled expression she seems to wear almost constantly, one that makes me constantly be on guard myself. I wonder why."

"I kind of understand why she always seems to be so wary… or maybe more like, why there could be a person like her."

"But I still have no idea how I should act around such a person."

hi "It's dinnertime soon. Were you planning to eat with Lilly?"

show hanako emb_downtimid
with charachange

show hanako emb_blushtimid
with charachange

"She nods slightly."

"So she must have been trying to get in the cafeteria."

"Well, there's something of a dinner crowd, just like the cafeteria is crowded during lunch."

"It's not as bad because dinnertime is longer than lunch hour, but I can understand why Hanako could be discouraged from going in."

"I pick up my bag and we take our leave. Hanako skips a little to meet my initial pace, so I slow down to match her speed."

scene bg school_hallway3
with locationchange

"It doesn't take long for us to be walking at a comfortable pace down the hallway."

show hanako def_worry at right
with charaenter

"It almost feels like we're going for a stroll together; something that I can't say I've really done before with a girl."

"Hanako doesn't seem to be thinking the same thing though. Even though we are walking at the same pace, she never comes within arm's reach of me."

"I guess she's still a little uncomfortable around me. Given how shy she is, there doesn't seem to be much helping it, at least for now."

scene bg school_cafeteria
with locationchange

play music music_night fadein 3.0

"By the time we arrive at the cafeteria, there is not much of a crowd there, but Lilly is nowhere to be seen."

show hanako emb_downsad at center
with charaenter

"Hanako's head sinks even lower than usual."

hi "Have you looked somewhere else already?"

show hanako basic_worry
with charachange

ha "J-just at the library… I was reading…"

"So she does spend the classes she skips at the library."

hi "Ah, so not exactly a thorough search then. Well, if I had to guess, she'd be in her own class like Shizune said, right?"

show hanako cover_worry
with charachange

ha "R-right."

show hanako basic_normal
with charachange

"With the slightest of nods, Hanako agrees with my reasoning."

"God, she's being so awkward."

"It's like I need double layered silk gloves with padding to even begin interacting with her."

"Some small talk might help her become a bit more used to me. It isn't hard to tell that the silence between us is hovering on the edge of both our minds."

hi "So you and Lilly usually hang out together after class, right?"

show hanako emb_downtimid
with charachange

ha "Y-yes."

"I'm not quite sure what I expected from her answer, nor why I even asked the question. That much was rather obvious, after all."

"She doesn't seem like the type to cultivate a social circle, either, so I suspect that Lilly may well be her only friend."

hi "Must be a pain being in different classes, I'm guessing."

"She gives a sharp, almost reflexive nod. Compared to Lilly's careful thought about her actions and speech, Hanako hastens to make her answers as prompt and short as possible."

show hanako emb_downsmile
with charachange

ha "Lilly… comes by the classroom, though. Even when she's busy…"

"She gives a small smile as she says it, evidently appreciating the fact that Lilly goes out of her way to help her."

"It's pretty cute, really. There isn't any need to say more, both of us content that the discussion's reached an end."

scene bg school_staircase2
with locationchange

"As we ascend the stairs back to the lobby we are met by a group of students heading downstairs like a school of fish moving from one feeding area to another."

show hanako cover_worry_close at Transform(xanchor=0.4, xpos=0.0)
with easeinleft

"They seem to be keeping mostly to themselves, but before I can notice her doing so, Hanako has moved around behind me."

hi "Hey, are you all right?"

show hanako basic_worry_close
with charachange

ha "J-just keep going…"

hide hanako
with easeoutleft

"The students pass us without as much as a second glance, and Hanako takes up position to my side again as we enter the building, her momentary reprieve from her anxiety all but snatched away."

scene bg school_lobby
show hanako basic_normal at center
with locationchange

"Even as we climb towards the third floor, she doesn't seem to relax."

"It isn't as if I've never known a shy person before, or even shy girls, but Hanako seems to be pretty far beyond what I'd call normal in her fear of other people."

"If it weren't for Lilly acting as a mediator, I doubt Hanako would have even been able to walk beside me like this. She seems to completely shut down in the presence of others."

"The rest of the walk up to Lilly's classroom continues in strained silence, while I rue her inability to socialize at all."

scene bg school_hallway3
with locationskip

stop music fadeout 4.0
$ renpy.music.set_volume(0.1, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 2.0

"After we make our way up the stairs, the noise coming from Lilly's classroom is audible from halfway down the hallway. I wasn't expecting such a din at all."

hi "Well, I guess we found her…"

"This wasn't hard. Did Hanako come here first then come to me for backup, I wonder?"

"Well, if that's true, then at least she's starting to trust me a little. That can only be a good thing."

"Eventually, the two of us reach the door to class 3-2. With Hanako less than subtly positioning herself behind me, I open the door."

play sound sfx_dooropen
$ renpy.music.set_volume(1.0, 1.0, channel="ambient")
play music music_another fadein 1.0

scene bg school_room32 at bgright
with locationchange

"Inside is a hive of activity, seemingly every student in the class talking at once as they work hurriedly on their separate tasks."

"Going by the paint cans, decorations and banners being made, it must be for the upcoming school festival."

"I guess my first priority should be finding Lilly…"

"…{w} There."

"Finding her among the din is surprisingly easy, not the least because of her looks."

"With a couple of students gathered around her as she stands at the front of the class, she seems to be in charge of the preparations, or at least busy organizing them."

"Carefully negotiating a path through the various students hunched over the floor for lack of desk space, I raise a hand entirely out of habit as we finally reach Lilly."

hi "Hi, Lilly."

show lilly basic_surprised at center
with charaenter

"She perks her head up as she breaks off talking to a noticeably smaller girl who must be her classmate, trying to listen as best she can."

li "Sorry, who…"

hi "Ah, sorry. Hisao. I have Hanako too."

show lilly basic_smile
with charachange

show lilly basic_smile at twoleft
show bg school_room32 at center
with charamove

show hanako basic_normal at tworight
with charaenter

ha "H-hi."

"She's pretty skittish. Considering the number of people around, it isn't too hard to work out why."

"Lilly takes a moment's pause to assess the situation before turning to the other student once again."

show lilly basic_smileclosed
with charachange

li "For the moment, just ask Moriya for his advice. Kenji's busy with painting one of the banners already."

"A quick nod and she bounces off, fingers carefully sliding along the wall's face for orientation."

$ renpy.music.set_volume(0.1,1.0)

"Wait… Kenji? That Kenji?"

"I quickly turn about, leaning to the side to see past Hanako."

"Sure enough, in a corner of the room, Kenji's hunched over a sheet of cloth as he paints it. His eyes remain only inches from the brush, reminding me of how close he had to be to make out my face when I met him."

$ renpy.music.set_volume(1.0,1.0)

show lilly basic_smile
with charachange

li "Sorry about that. Our class doesn't have many students with even partial eyesight, so they're in high demand."

"That's right, class 3-2 was specially for students with poor vision. Preparing for the festival must be pretty arduous for them."

hi "Need a hand? I could give you help if you need some. Maybe Hanako could too."

"A chance to set her mind on something would do her good, but I doubt she has the courage to ask outright. She quickly nods in affirmation afterwards, so I'm confident I made the right move."

"Lilly gives a noticeable sigh of relief."

show lilly basic_weaksmile
with charachange

li "Ah, that's good. This might actually get finished before everyone goes off to dinner, now."

show lilly basic_listen
with charachange

li "Would you be able to help the person painting the main banner? It's a big task for him to do, but nobody else can help."

hi "Kenji? Sure."

show lilly basic_surprised
with charachange

"She seems surprised that I know him. I can't really blame her."

li "I take it you've met?"

hi "Our rooms in the dorm are right next to each other. Hard to miss each other, really."

show lilly basic_ara
with charachange

li "Well, it's good to see you're getting friends so fast."

"Friend… I wonder if that's the right word to use for him."

"Hanako's silence during the proceedings reminds me of the reason I put her up to helping in the first place."

hi "We'll go help him then. He knows what needs doing, right?"

show lilly basic_smileclosed
with charachange

li "That's right. Just ask if you have any problems."

hide lilly
hide hanako
with charaexit

$ renpy.music.set_volume(0.5, 2.0, channel="ambient")

"Chorusing in assent, Hanako and I begin another trek across the classroom."

"Kenji sits crouched on the floor, his gaze fixed on the white calico in front of him."

show kenji tsun at Transform(yanchor=0.45, ypos=1.0, xalign=0.5)
with charaenter

hi "Hey Kenji."

"…No answer. He continues dragging his paint-soaked brush along the large half-painted kanji that's sketched on the sheet in pencil."

hi "Kenji?"

show kenji tsun at center
with charamove

ke "Huh? What? Who is it?"

"If this is the way he treats class members, it's no small wonder he's working on this alone."

hi "It's me. Hisao. From the—{w=.5}{nw}"

ke "Right, right, I know that, man. What're you doing here, though?"

"His dismissive attitude annoys me."

"He must be the type to really get focused on his work, hating to be disturbed by anyone until he's done, I suppose."

show kenji tsun at twoleft
show bg school_room32 at bgleft
with charamove

show hanako cover_distant at tworight
with charaenter

"While we talk, the sound of Hanako's footsteps as she walks out from behind me reminds me that she's here."

hi "I was just going to help with the banner. Hanako and I, that is."

show hanako cover_worry
with charachange

ha "H… Hello…"

show kenji happy
with charachange

ke "Oh. Er, hey. I guess that's okay."

"As soon as Hanako enters the equation, his demeanor takes a complete about-face. His sudden faux-hospitality is slightly unsettling."

"Oh, right. Women. On second thoughts, this may not have been a great idea after all."

stop music fadeout 2.0

scene bg school_room32 at bgleft
show kenji neutral_close at left
show hanako basic_distant_close at right
with locationskip

"Hanako and I grudgingly set ourselves down on the opposite side of the cloth banner to Kenji, noting the several small paint tins on the ground around it."

"Class 3-2… noodle stall?"

hi "You guys selling noodles at the festival on Sunday?"

show kenji happy_close
with charachange

ke "Yeah, some stalls outside. Or something."

"“Or something?” His noncommittal nature sparks a fair amount of suspicion on my behalf. The task at hand comes first, though."

hi "So how do you want to split this? We do borders while you do the text? Or do you want to switch and do the borders?"

show kenji tsun_close
with charachange

ke "Text is mine. You do borders."

"He has surprisingly strong feelings on the topic."

show hanako basic_distant_close
with charachange

"As I reach over to grab a brush, I notice Hanako's already debating between colors to use."

show hanako basic_normal_close
with charachange
show hanako basic_distant_close
with charachange
show hanako basic_normal_close
with charachange

"By the time I've put brush to cloth, she's already started on a delicate pattern. Looks like my idea of taking her mind off everyone around her worked."

"With a dark blue stroke, the three of us silently get to work."

"Not before Kenji takes advantage of Hanako's working to lean towards me and whisper conspiratorially, though."

show bg school_room32 at center
show kenji tsun_close at center
show hanako basic_normal_close at offscreenright
with charamove

show kenji neutral_close
with charachange

play music music_kenji fadein 0.5

ke "Okay man, why're you here?"

hi "Hanako just wanted some help to find Lilly, that's all."

show kenji tsun_close
with charachange

"He apparently disapproves of my motivations."

ke "I get it. It looks like I misjudged you."

show kenji happy_close
with charachange

ke "You're infiltrating them, aren't you? Going deep undercover?"

"I should have guessed. Letting the truth slip by him would probably be better than outright lying or annoying him, in any case."

hi "Is that why you're here?"

ke "Obviously. It sucks, but there's no better way to get intel than going in yourself."

show kenji tsun_close
with charachange

ke "We gotta stick together, man. This is a harsh school, a harsh world."

hi "Yes, very harsh."

"He misses my true meaning as he leans back, satisfied I'm sympathetic to his cause. I'd better get down to work."

stop music fadeout 2.0
stop ambient fadeout 2.0

scene bg school_room32
show kenji neutral_close at left
show hanako basic_normal_close at right
with shorttimeskip

ha "Finished."

hi "Looks like I am too. Good job."

"The two of us connect up the lines of our patterns, mine being as close a copy as I could manage of hers."

scene bg school_room32
with locationskip

"With a grunt, I lever myself up from the floor and look around."

play music music_dreamy fadein 4.0

"Aside from Hanako and myself, there's only Kenji left finishing off a sign as well as Lilly and a couple of students talking among themselves in the classroom."

"Looking at my watch, it's no surprise. It's getting pretty late."

hi "Need a hand?"

show hanako basic_normal at center
with charamoveinbottom

"I offer a hand to Hanako, which she uses to get herself up."

"As she does, I can't help but glance at her wrist; if her scars extend even to there, just how much of her body was burned?"

show hanako emb_downtimid
with charachange

"I feel a pang of guilt about it however as she quickly covers her wrist with her other hand."

hi "Looks good, doesn't it?"

show hanako emb_timid
with charachange

"She looks surprised for a moment before noticing that I mean the banner."

show hanako basic_bashful
with charachange

ha "It does… I guess."

"Her smile shows that she feels a slight sense of pride in the result, just as I do."

hide hanako
with charaexit

"With the floor significantly neater for the decorations being placed on desks and shelves, it's much easier to get to Lilly as we cross the room."

hi "We've finished the banner. I guess that's all that needs to be done?"

show hanako basic_smile at tworight
show lilly basic_smileclosed at twoleft
with charaenter

"Lilly gives an appreciative nod."

show lilly basic_smile
with charachange

li "Thank you Hisao, Hanako. If there's any way I can thank you…?"

hi "It's fine. Beats sitting in my room studying, at any rate."

show hanako basic_normal
with charachange

ha "I don't mind either."

"She nods, before suddenly remembering one last person."

show lilly basic_surprised
with charachange

li "Oh, is Kenji still here?"

"Just as I open my mouth, Kenji gives the answer from the other side of the room."

ke "Yeah, just finished."

"He carefully slides his sign onto an empty section of shelf to dry, before quickly walking past us and out the door."

show hanako basic_normal at center
show lilly basic_surprised at left
show bg school_room32 at bgleft
with charamove

show kenji neutral at Transform(xalign=1.15)
with charaenter

ke "Seeya man."

hi "Bye."

hide kenji
with charaexit

show hanako basic_normal at tworight
show lilly basic_surprised at twoleft
show bg school_room32 at center
with charamove

"The remaining two students say their goodbyes to Lilly before taking their cue to leave as well, leaving only the three of us."

hi "Well, I guess that's everyone."

show lilly basic_displeased
with charachange

li "I hope we don't have to do anything like that again."

hi "Working past schooltime?"

show lilly basic_concerned
with charachange

li "Indeed. The class's plans this year were ambitious. Maybe too ambitious."

show hanako emb_smile
with charachange

ha "The stalls look nice, though."

hi "She's right, it shows that a lot of work's gone into them."

show lilly basic_ara
with charachange

li "My my, I'm sure a lot of us would be glad to hear that. At least now there's not much work to do until the festival itself."

show hanako basic_smile
with charachange

ha "Umm… It's getting pretty late. Should we go?"

show lilly basic_smileclosed
with charachange

li "That's probably a good idea. Are you going back to the dorms as well, Hisao?"

hi "Yeah, I guess I'll tag along."

scene bg school_gardens2_ni
with locationskip

"The nighttime lighting really makes the gardens look quite different. Compared to the usual look of lush greenery, things are much more calm."

"Being that it's so late, the lack of students around probably helps. The odd one or two can be seen scurrying to and from the dorms trying to eke the most out of their approaching curfews, but no more."

"All that can be heard is our footsteps, in addition to Lilly's cane regularly gently tapping the ground in front of her."

"It's nice to finally be able to relax a bit after the mad rush during school."

"Without even noticing it, I let out a small yawn."

show lilly cane_smile_ni at twoleft
show hanako basic_normal_ni at tworight
with charaenter

li "Tired?"

hi "Yeah. Still getting used to the flow of things, I guess."

hi "The… uh… thing… with Shizune took me kind of off guard, though."

"I grit my teeth a little at the candid mention of their rather public spat. That said, I do want to sort out what in the world was behind it."

show lilly cane_displeased_ni
with charachange

li "Ah… about that…"

li "I'm sorry about it being so public. Shizune and I… go back some ways."


label th_A24c:
#lol label order

# If he pissed off Lilly

"Her voice seems slightly irritated as she remembers Shizune, and on second thought, possibly my part in the proceedings."

show lilly cane_listen_ni
with charachange

li "I would appreciate it if you didn't help her. The last thing she needs is urging on."

"Well, that confirms my suspicions at the time. I pissed her off."

"That said, while I may have inadvertently fed her to the dogs, I couldn't know and therefore am in no position where I'd need to apologize."

"A couple of minutes of strained silence pass by between us, Hanako's eyes darting left and right."

"Giving up on the prospect of any kind of apology, Lilly surrenders the fight and changes the topic."



label th_A24d:

# If he didn't

"Her voice seems slightly irritated as she remembers Shizune, obviously unwilling to discuss it any further."

show hanako basic_distant_ni
with charaenter

"I glance to Hanako for her views on this, but her expression is, unsurprisingly, evasive and difficult to read."

"Either way I guess her apologizing for it is something, even if my curiosity goes unanswered."



label th_A24e:

# End conditionals

show lilly cane_weaksmile_ni
with charachange

li "I'll be glad once the festival is over, in any case."

"The change of topic's welcome, clearing the thickening air quickly."

hi "I can imagine. My old school's festivals were a lot more low-key than this."

show lilly cane_smileclosed_ni
with charachange

li "Yamaku stresses the idea of a school community, so the staff likes to make our festivals and such special occasions."

hi "And yet the students are the ones who do the work. What an unfair world."

show lilly cane_giggle_ni
show hanako emb_emb_ni
with charachange

"Hanako and Lilly both chuckle in agreement, savoring the fact that none of the staff are around to hear our grumbling."

show lilly cane_smile_ni
show hanako basic_smile_ni
with charachange

li "I suppose coming from a strict all-girls school helped me a bit with Yamaku. Compared to there, Yamaku is much more relaxed."

"That'd go a way towards explaining her well-bred speech and behavior, in any case."

scene bg school_dormext_half_ni
show lilly cane_smile_ni at twoleft
show hanako basic_smile_ni at tworight
with locationskip

"As we come up to the dormitories, it eventually comes time to leave for our respective rooms."

hi "See you Lilly, Hanako."

"The two both give polite nods before setting off to the women's dorms, just next to the guys'."

stop music fadeout 4.0

hide lilly
hide hanako
with charaexit

"As is to be expected of such an arrangement, there's a staff member casually patrolling around outside to prevent any nighttime shenanigans."

"Walking past him, I quickly stretch my arms and rub my neck, both quite sore after having worked on the floor for so long, before walking to my room."

"It feels good to actually have direction, though. After so long in the hospital, the everyday facts of studying, homework and teachers seem almost a blessing."

"I guess if things continue like this, my time at Yamaku might turn out okay."


label th_A24a:

scene bg school_dormhisao_ni
with locationskip

"Adhering to the nurse's nagging voice in the back of my head, I set my alarm clock to wake me up early enough to go jogging again."

"I made a promise and I'm going to keep it. Besides, Emi is bound to rat on me if I don't show up."

"But it's not all that bad."

$ suppress_window_after_timeskip = True

scene black
with shuteye


label th_A24b:

scene bg school_dormhisao_ni
with locationskip

"I'm feeling tired so I set my alarm clock to wake me up as late as I can afford, while still making it to the first class."

"The nurse's voice is almost nagging in the back of my head about morning jogs. I make a resolution to make up for it by going for a walk after school tomorrow."

"Emi won't care either way, I bet."

$ suppress_window_after_timeskip = True

scene black
with shuteye

return
