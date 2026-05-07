label th_E28:

window hide None

scene black
with dissolve

with Pause(2.0)

play sound sfx_alarmclock

with Pause(3.0)

scene bg school_dormhisao
with openeye

play music music_dreamy fadein 4.0

window show

# "The sound of my alarm is an unwelcome intrusion on a sleep that's been a battle to obtain. I doubt I've been truly asleep for more than an hour or two."
"เสียงนาฬิกาปลุกดังขัดตัวฉันที่กำลังข่มตานอนหลับอยู่ เหมือนจะได้หลับจริง ๆ แค่ชั่วโมงสองชั่วโมงเอง"

# "Too much on my mind. Did I make the right choice, leaving the house yesterday? Did I manage to get Emi to realize how unreasonable she's been?"
"เพราะมีหลายอย่างให้คิด ฉันเลือกถูกแล้วหรือยังกับการออกจากบ้านมาเมื่อวาน ฉันทำให้เอมิเข้าใจหรือยังว่าเธอ\nทำตัวไร้เหตุผลแค่ไหน"

# "Am I ever going to manage to get her to stop being unreasonable? Emi's mom gave me a new perspective the other day, but I'm still not sure that it's the right perspective."
"ฉันจะทำให้เอมิทำตัวมีเหตุผลขึ้นมาได้หรือเปล่า เมื่อวานแม่เอมิได้ให้มุมมองใหม่กับฉันแล้ว แต่ฉันก็ยังไม่แน่ใจอยู่ดี\nว่าเป็นมุมมองที่ถูกต้องหรือเปล่า"

# "She was hurt when I left yesterday, too."
"ตอนที่ออกมาเอมิก็เจ็บปวดอยู่ด้วย"

# "I know that part of any conversation is going to have to include an apology about that. Right thing to do or not, I hurt her."
"ฉันรู้ว่าในบทสนทนาที่จะได้คุยกับเอมิถัดจากนี้ต้องมีคำขอโทษเรื่องนั้นแน่ ๆ ไม่ว่าสิ่งที่ฉันทำจะถูกหรือไม่\nแต่มันก็เป็นการทำร้ายเอมิอยู่ดี"

# "I hurry down to the track, eager to talk to Emi. I think I know what to say. Apologize for leaving first, and go ahead from there."
"ฉันรีบไปที่ลู่วิ่งด้วยความอยากคุยกับเอมิ ฉันว่าฉันรู้แล้วว่าจะต้องคุยอะไร ขอโทษที่ออกมาจากบ้านก่อน แล้วก็พูด\nต่อจากนั้นไปเรื่อย ๆ"

scene bg school_track
with locationskip

# "Unless, of course, Emi doesn't show up."
"แต่แน่นอนว่าเอมิไม่มา"

# "Which from the looks of things seems like it's the case. It's been about fifteen minutes since I got here, and there's no sign of her."
"ซึ่งดู ๆ แล้วก็คงเป็นอย่างนั้น ฉันมาถึงราวสิบห้านาทีได้แล้วและยังไม่มีวี่แววว่าเอมิจะมาเลย"

# "She's never late, not unless she's sick, which is unlikely. She probably just doesn't want to see me right now."
"เอมิไม่เคยมาช้า เว้นเสียแต่ว่าป่วย ซึ่งก็ไม่น่าใช่ อาจจะแค่ยังไม่อยากเจอฉันตอนนี้"

scene bg school_track_on
with locationchange

scene bg school_track_running
with locationchange

# "To take my mind off what that implies, I begin my warm-up routine and take off around the track."
"ฉันทำหัวให้โล่งไม่ไปคิดถึงความหมายของการที่เอมิไม่มาด้วยการวอร์มอัพตามปกติแล้ววิ่งไปตามลู่"

# "It clears my mind wonderfully; for the half-hour I'm running, I don't think about anything but the run."
"ซึ่งทำให้สมองฉันปลอดโปร่งได้เป็นอย่างดี พอวิ่งมาได้ครึ่งชั่วโมงแล้วสมองก็มีแต่เรื่องวิ่ง"

scene bg school_track_on
with locationchange

stop music fadeout 4.0

# "However, once I've finished, and Emi still hasn't shown up…"
"แต่พอวิ่งเสร็จแล้วและเอมิยังไม่มา…"

# "I get a little worried. With any luck, the nurse will know where she is; if nothing else, I can see what he thinks I should do next."
"ฉันนึกกังวลขึ้นมาเล็กน้อย ถ้าโชคดีคุณพยาบาลอาจรู้ก็ได้ว่าเอมิอยู่ที่ไหน หรืออย่างน้อยก็จะได้ปรึกษาว่าฉัน\nควรทำอย่างไรต่อ"

scene bg school_nurseoffice
show nurse grin at center
with locationskip

play music music_nurse fadein 0.5

# nk "So, last night didn't go too well, I take it."
nk "แปลว่าเมื่อคืนจบไม่สวยสินะ"

# hi "Huh? You already know?"
hi "ครับ? รู้แล้วเหรอครับ"

# nk "I have my ways, and it's not as if I'd miss the distinct absence of your running partner this morning, now would I?"
nk "ฉันก็มีวิธีของฉัน แล้วก็ใช่ว่าฉันจะไม่เห็นสักหน่อยว่าเพื่อนวิ่งของเธอไม่มาด้วยเช้านี้น่ะ"

# hi "No, I suppose not."
hi "เอ่อ ก็คงงั้นแหละครับ"

show nurse neutral
with charachange

# nk "So, what happened?"
nk "แล้วนี่เกิดอะไรขึ้น"

# hi "Don't you know already?"
hi "ยังไม่รู้เหรอครับ"

show nurse fabulous
with charachange

# nk "Maybe, but I could be bluffing. Perhaps I'd prefer to get your side of the story before I give any advice."
nk "มั้ง แต่ฉันอาจจะถามหยั่งเชิงเฉย ๆ ก็ได้ อาจจะอยากฟังเรื่องจากฝั่งเธอบ้างแล้วจะได้ให้คำแนะนำถูก"

# "I quickly fill the nurse in on the events of last night, and he takes it all in without changing expression once."
"ฉันรีบเล่าเรื่องเหตุการณ์เมื่อคืนให้คุณพยาบาลฟัง ซึ่งเขาก็ทำหน้านิ่งรับฟัง"

# "Nothing about the whole event seems to surprise him, although he does seem surprised when I say that I didn't follow Emi."
"เหมือนคุณพยาบาลจะไม่ได้แปลกใจอะไรเลย แต่ก็ดูแปลกใจตอนที่ฉันเล่าว่าฉันไม่ได้ตามเอมิไป"

show nurse grin
with charachange

# nk "Chose to talk to her mom instead, huh? Smart move, though I guess it didn't work out too well for you in the end."
nk "คุยกับแม่เอมิแทนงั้นเหรอ ฉลาดดีนี่ แต่สุดท้ายเรื่องก็ยังไม่ลงตัวสินะ"

# hi "Well, I'm not sure. Emi seemed apologetic when I left, or at least she seemed that way until she put up her defenses again."
hi "เอ่อ ก็ไม่แน่ใจครับ เอมิทำหน้าเหมือนรู้สึกผิดตอนผมเดินออกมา เหมือนจะเป็นอย่างนั้นก่อนที่เอมิ\nจะทันได้ปิดใจไปอีกรอบ"

# "The nurse sighs and spreads his hands in a conciliatory gesture."
"คุณพยาบาลถอนหายใจแล้วกางมือทำท่าเหมือนจะเจรจา"

show nurse fabulous
with charachange

# nk "Frankly, I'm surprised she let them down at all. Emi's had a lot of practice on that score. You probably won't get anything else out of her."
nk "ว่าตามตรงนะ ฉันแปลกใจที่เอมิยอมเปิดใจด้วยซ้ำ เอมิเขาปิดใจเก่งมากเลยนะ ถามเอมิไปเธอก็คงไม่ได้คำตอบ\nอะไรมากหรอก"

# hi "I don't believe you."
hi "ผมไม่เชื่อ"

# nk "Is that so? You think she'll tell you the whole tale?"
nk "งั้นเหรอ เธอคิดว่าเอมิจะเล่าเรื่องทั้งหมดให้เธอฟังเหรอ"

# "I'd swear I just saw the nurse's eyes glitter a little. His expression is the same, but he leans forward ever so slightly."
"สาบานเลยว่าเมื่อกี้เหมือนเห็นประกายในตาคุณพยาบาลอยู่หน่อย ๆ สีหน้ายังเหมือนเดิมก็จริง แต่เขาโน้มตัวเข้ามานิด ๆ"

# hi "I think she'll open up if I ask her without being an idiot about it, yeah."
hi "ผมว่าถ้าถามดี ๆ แบบไม่งี่เง่าแล้วเอมิก็คงเปิดใจให้แหละครับ"

# "The nurse gives his enigmatic smile in response and shrugs widely. I think he's enjoying his role a little too much."
"คุณพยาบาลยิ้มเหมือนแฝงนัยอะไรไว้แล้วยักไหล่ สงสัยจะชอบที่ได้ทำหน้าที่คนกลางมาก"

show nurse grin
with charachange

# nk "That's the real trick, isn't it? Are you sure you know the right way to approach the subject? I can guarantee that Emi's going to try her hardest to pretend last night didn't happen."
nk "นี่แหละคือจุดสำคัญเลย เธอแน่ใจใช่มั้ยว่ารู้วิธีคุยเรื่องนี้อย่างถูกต้องหรือยัง ฉันรับประกันเลยว่าเอมิจะแสร้ง\nทำเหมือนเรื่องเมื่อคืนไม่เคยเกิดขึ้น"

show nurse neutral
with charachange

# nk "It will be painfully awkward for the both of you, but it'll also be a lot safer than trying to ask her for the whole story again. It could go worse, this time."
nk "เธอสองคนจะกระอักกระอ่วนกันมาก ๆ แต่แบบนี้ก็จะปลอดภัยกว่าการขอให้เอมิเล่าเรื่องทั้งหมดอีกรอบ ซึ่งคราวนี้\nเรื่องอาจยิ่งแย่ลงอีก"

# nk "Are you ready for something like that?"
nk "เธอเตรียมใจพร้อมกับอะไรแบบนั้นหรือยัง"

# "It sounds like a challenge, like he doesn't believe for a minute that I'd be so bold. I actually feel a little insulted by his lack of confidence in me."
"ฟังเหมือนคำท้าเลย เหมือนไม่เชื่อว่าฉันจะใจกล้าได้ขนาดนั้น ที่จริงฉันก็แอบเคืองเหมือนกันที่คุณพยาบาล\nไม่เชื่อใจฉัน"

# hi "Of course I'm ready for that! I love her!"
hi "พร้อมอยู่แล้วสิครับ! ผมรักเอมิ!"

show nurse fabulous
with charachange

# "My outburst gets a raised eyebrow in response."
"เสียงตะโกนนั้นทำให้คุณพยาบาลเลิกคิ้วตอบ"

# nk "Well then."
nk "โอเค ๆ"

show nurse neutral
with charachange

# nk "Good luck. Let me know how it all turns out."
nk "โชคดีละ ได้ความว่ายังไงก็เอามาบอกด้วยนะ"

# "Although he delivers his parting shot with the same smirk as usual, I actually think that the nurse wants me to succeed."
"ถึงคุณพยาบาลจะบอกลาด้วยรอยยิ้มอย่างเคย แต่ฉันคิดว่าเขาอยากให้ฉันทำให้สำเร็จได้จริง ๆ"

stop music fadeout 3.0

scene bg school_nursehall
with locationchange

# "I resist the urge to charge directly to Emi's room to prove the nurse wrong. I've gone in half-cocked before, and the results were less than stellar."
"ฉันห้ามใจตัวเองไม่ให้พุ่งตัวไปยังห้องเอมิทันทีเพื่อพิสูจน์ว่าคุณพยาบาลคิดผิด ฉันเคยไปโดยที่\nไม่ได้เตรียมตัวพร้อมให้ดีมาก่อนแล้ว ซึ่งผลก็ออกมาไม่สวยงามเลย"

# "If I'm going to do this, I need to figure out exactly what I'm going to say, and how I'm going to say it. Something to think about in class."
"ถ้าฉันจะไปเจอเอมิก็ต้องคิดก่อนว่าจะพูดอะไร และจะพูดอย่างไร ไว้คิดตอนเรียนแล้วกัน"

scene bg school_scienceroom
with shorttimeskip

# "Sure enough, by the time lunch rolls around, I think I have a good enough idea of what to say. I can do this."
"และตามคาด พอใกล้ถึงช่วงพักเที่ยงฉันก็พอจะนึกออกแล้วว่าต้องพูดอะไรดี ฉันทำได้น่า"

play sound sfx_normalbell

scene bg school_staircase1
with locationskip

# "The bell rings, and I grab my lunch and dash up the stairs, eager to be there first. I'll need to ask Rin to leave, and I'll need to—"
"เมื่อระฆังดังฉันก็ไปซื้อข้าวเที่ยงแล้วเดินขึ้นบันไดมาด้วยอยากมาถึงก่อน ต้องขอให้รินออกไปก่อน แล้วก็ต้อง—"

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_rooftop fadein 1.0
play sound sfx_door_creak

scene bg school_roof
show emi basic_hes at twoleft
show rin basic_absent at tworight
with silentwhiteout

# emi "Hi Hisao! Sorry I wasn't able to run with you this morning! I overslept!"
emi "ไงฮิซาโอะ! ขอโทษที่ไม่ได้ไปวิ่งด้วยเมื่อเช้านะ! พอดีฉันตื่นสายน่ะ!"

# "Somehow, both Emi and Rin have managed to get to the roof before me."
"ดูท่าว่าทั้งเอมิทั้งรินจะมาถึงที่ดาดฟ้าก่อนฉันแล้ว"

# hi "Oh, that's no problem. Last night was kind of… draining, I guess."
hi "อ้อ ไม่เป็นไรหรอก เรื่องเมื่อคืนมันก็… ชวนให้เพลียนี่นะ"

# "Emi's expression doesn't alter in the slightest."
"สีหน้าเอมิไม่เปลี่ยนไปเลยแม้แต่น้อย"

# emi "Yeah, sorry about that! But I've had such a weird morning since then!"
emi "อื้ม ขอโทษด้วยนะ! แต่หลังจากตื่นมาก็มีเรื่องแปลก ๆ ด้วยแหละ!"

# hi "Oh uh, really?"
hi "อ้อ จริงเหรอ"

show emi basic_happy
with charachange

# "Emi proceeds to make small talk for the rest of the time. I can barely get a word in edgewise, and soon find myself interjecting with the sort of back and forth dialogue that seems to have defined our early relationship."
"ส่วนเวลาที่เหลือเอมิก็คุยเรื่อยเปื่อย ฉันแทบไม่ได้พูดเลย และไม่นานฉันมาก็โต้ตอบบทสนทนาง่าย ๆ กับเอมิ\nที่ดูคล้าย ๆ ตอนเราสองคนคบกันแรก ๆ"

# "I'm not gonna get anywhere on this problem during lunch, obviously. I can respect that; Emi obviously doesn't want to accidentally pull Rin into things, and that's fine."
"ชัดว่าคงไม่ได้พูดถึงเรื่องปัญหานี้ตอนเที่ยงแน่ ๆ ฉันเข้าใจ เอมิไม่อยากเผลอลากรินให้เข้ามาเกี่ยวข้องด้วยแน่นอน\nซึ่งก็ไม่เป็นไร"

# "Not that I think Rin would notice, but I can at least respect that sort of rationale."
"ฉันว่ารินคงไม่สังเกตหรอก แต่อย่างน้อยก็เข้าใจว่าทำไมเอมิถึงคิดแบบนั้น"

# "I try a different tactic."
"ฉันลองอีกกลวิธีหนึ่ง"

# hi "Hey, Emi. What are you up to after class today? I was thinking we could go somewhere for dinner, or something."
hi "นี่ เอมิ เลิกเรียนแล้วมีธุระอะไรหรือเปล่า พอดีกะจะชวนเธอไปกินข้าวเย็นหรืออะไรด้วยกันน่ะ"

show emi sad_depressed
with charachange

# "Emi looks genuinely remorseful."
"เอมิทำหน้าเสียดายจริง ๆ"

# emi "Sorry, Hisao! I promised the track captain that I'd stick around after practice and help some of the other kids with their form! It'll have to be some other time."
emi "ขอโทษนะฮิซาโอะ! ฉันรับปากกับหัวหน้าทีมไว้แล้วว่าซ้อมเสร็จแล้วจะอยู่ช่วยเป็นที่ปรึกษากับเด็กคนอื่น\nเรื่องการเล่นกีฬาน่ะ! ไว้วันหลังนะ"

# hi "Yeah, sure…"
hi "อื้ม ได้…"

window hide

scene black
show bg misc_sky at center
with locationchange

nvl clear
nvl show dissolve

# n "I'm honestly not sure what to do now. Maybe diving into things the day after would be a bad idea anyway."
n "ว่าตามตรง ตอนนี้ฉันไม่รู้จะทำอะไร หรือการมาจัดการเรื่องอะไร ๆ ในวันถัดมาเลยจะไม่ใช่ความคิดที่ดีจริง ๆ"

# n "She might still be angry about it and just not showing it. Besides, if she's got track team responsibilities that's fine, right?"
n "เอมิอาจจะยังโกรธอยู่แต่ไม่ได้แสดงออกก็ได้ อีกอย่าง ถ้ายังมีภาระหน้าที่กับทีมวิ่งอยู่ก็คงไม่เป็นไรหรอก"

show bg misc_sky:
    linear 10.0 alpha 0.0
with None

# n "I tell myself some variation on this theme the next day. Then the next. I wake up, run with Emi (during which she refuses to talk about anything but the run and what she was doing the night before), and then lunch, where we sit and make small talk until the bell rings."
n "วันถัดมาฉันก็บอกอะไรประมาณนั้นกับตัวเอง แล้วก็วันถัดจากนั้นอีก ฉันตื่นขึ้นมาวิ่งกับเอมิ (ซึ่งเอมิไม่ยอมคุย\nเรื่องอื่นเลยนอกจากเรื่องวิ่งกับเรื่องที่ทำเมื่อคืนก่อนหน้า) แล้วก็ไปนั่งกินข้าวเที่ยงคุยเรื่อยเปื่อยกันจนระฆังดัง"

# n "Her new responsibilities effectively keep me from seeing her outside of school. Maybe, just maybe, I'm letting it happen because it's safer this way, just like the nurse said."
n "ภาระหน้าที่ใหม่ของเอมิทำให้ฉันไม่ได้เจอเอมินอกเวลาเรียนเลย หรือ หรือว่านะ ที่ฉันปล่อยให้เป็นแบบนี้อาจเพราะ\nเป็นทางที่ปลอดภัยกว่าอย่างที่คุณพยาบาลว่าไว้"

# n "Except while it may be safer, I'm feeling more and more wretched. Emi doesn't look good when I see her any more; dark circles lurk under her eyes, she seems more and more distracted, and I can't bring myself to just ask what's wrong, because the timing never seems right."
n "ปลอดภัยกว่าก็จริง แต่ฉันยิ่งหดหู่ขึ้นเรื่อย ๆ เอมิไม่ได้ดูดีอย่างที่เคยเป็นแล้ว ใต้ตาเธอดำคล้ำ หน้าตาดูเหม่อลอย\nหนักขึ้นทุกที และฉันก็ไม่กล้าถามว่ามีเรื่องอะไรเพราะจังหวะเหมือนจะไม่เคยลงตัวเลย"

# n "\nI'm absolutely miserable."
n "\nฉันมันน่าสมเพชที่สุด"

stop ambient fadeout 2.0

nvl clear
nvl hide dissolve

$ suppress_window_before_timeskip = True

scene black
with dissolve

#############

label th_E29:

scene bg school_staircase1
with locationchange

# "Another lunch comes. I trudge up the stairs to the rooftop like a condemned man."
"ถึงเวลาพักเที่ยงอีกครั้ง ฉันเดินขึ้นบันไดด้วยสภาพเหมือนนักโทษประหาร"

play ambient sfx_rooftop fadein 1.0

scene bg school_roof at bgleft
show rin basic_absent at center
with locationchange

# "Rin is up there, but Emi is not. Immediately I worry that something's happened to her. Maybe the lack of sleep finally made her collapse, or something worse."
"รินอยู่ แต่เอมิไม่อยู่ ฉันนึกกังวลทันทีว่ามีเรื่องอะไรเกิดขึ้นกับเอมิหรือเปล่า อาจจะเพราะนอนน้อยจนเป็นลม\nไปแล้วจริง ๆ หรืออาจจะแย่กว่านั้น"

# "She seemed pretty tired after our morning run. Maybe she fell asleep and didn't even make it to class."
"หลังจากที่วิ่งตอนเช้าด้วยกันเอมิก็ดูเพลียมากด้วย อาจจะหลับไปแล้วไม่ทันตื่นมาเข้าเรียน"

# hi "Hey, Rin. Where's Emi?"
hi "นี่ ริน เอมิอยู่ไหนเหรอ"

show rin basic_deadpancontemplation
with charachange

# "In response I get a rather penetrating look from Rin, and something approaching a frown appears on her face."
"รินมองตอบด้วยสายตาที่เหมือนจะจ้องผ่านตัวฉัน ก่อนจะทำสีหน้าบางอย่างที่คล้ายการขมวดคิ้ว"

# rin "Is that information really important?"
rin "ข้อมูลที่ว่าสำคัญขนาดนั้นเลยเหรอ"

# hi "I think so. She's usually here with you, isn't she?"
hi "คิดว่านะ ปกติเอมิจะมาอยู่ที่นี่กับเธอนี่"

show rin basic_awayabsent
with charachange

# rin "I don't know. I have no way of being sure."
rin "ไม่รู้สิ ฉันแน่ใจไม่ได้หรอก"

# hi "I can confirm that she is, in fact, usually here with you when I come up."
hi "ฉันยืนยันได้ว่าปกติเอมิจะมาอยู่บนนี้กับเธอจริง ๆ"

show rin basic_deadpannormal
with charachange

# rin "Well she isn't now. Does that worry you?"
rin "ก็ตอนนี้ไม่อยู่นี่ นายคิดมากมั้ยล่ะ"

# hi "Kind of."
hi "ค่อนข้าง"

show rin basic_deadpancontemplation
with charachange

# rin "Hm."
rin "อืม"

play sound sfx_door_creak
with Pause(0.5)

show emi invis:
    twoleft
    xpos 0.1
with None

show bg school_roof at center
show rin basic_deadpancontemplation at tworight
show emi basic_closedhappy at twoleft
with dissolvecharamove

# "That seems to end the conversation, and the point becomes moot anyway because Emi bounds through the door with her usual energy."
"ดูท่าว่าบทสนทนาจะจบลงเท่านี้ และสุดท้ายก็ไม่ต้องหาคำตอบอยู่ดีเพราะเอมิโดดออกจากประตูมาด้วยท่าทีเหมือนเก่า"

show rin basic_deadpan
with charachange

# rin "Hisao is kind of worried about you, Emi. I don't think he can decide, or maybe I just don't believe him, but I think I'm going to go somewhere less awkward now."
rin "ฮิซาโอะค่อนข้างเป็นห่วงเธอละเอมิ ฉันว่าฮิซาโอะตัดสินใจไม่ได้ หรือฉันอาจจะไม่เชื่อใจฮิซาโอะเอง แต่ฉันว่า\nตอนนี้ฉันขอตัวไปอยู่ที่ที่น่าอึดอัดน้อยกว่านี้หน่อย"

hide rin
with charaexit

with Pause(0.5)

show bg school_roof at bgright
show emi basic_confused at center
with dissolvecharamove

# "I'm so surprised by Rin's being so suddenly forward about, well, anything at all that I merely watch her head through the door."
"ฉันแปลกใจมากที่อยู่ ๆ รินก็พูดเรื่อง เอ่อ เรื่องอะไรสักอย่างออกมาตรง ๆ แบบนั้นได้จนได้แต่มองไล่หลังรินที่เดิน\nออกประตูไป"

show emi basic_shock
with charachange

# "Emi is similarly surprised, and colors slightly crimson as she stares openmouthed at me. It occurs to me that I should probably say something, if only to break the awkward silence that has suddenly descended."
"เอมิก็แปลกใจพอกัน เธออ้าปากค้างมองมาทางฉันหน้าแดง ๆ แล้วฉันก็นึกได้ว่าต้องพูดอะไรเสียหน่อย\nเพื่อทำลายความเงียบอันน่ากระอักกระอ่วนที่อยู่ ๆ ก็เข้ามาปกคลุมนี้"

# hi "It's because you weren't here yet. I was uh, worried about it."
hi "ก็เพราะเธอยังไม่มานั่นแหละ ฉันเลย เอ่อ เป็นห่วง"

show emi basic_confused
with charachange

# emi "Why?"
emi "ทำไมล่ะ"

# hi "You're usually here, so I was worried that something had happened to you."
hi "ปกติเธอจะอยู่ที่นี่นี่ ฉันเลยเป็นห่วงว่าเธอเป็นอะไรไปหรือเปล่า"

show emi sad_grin
with charachange

# emi "This isn't the first time that I've been late, you know. Did you get worried all the other times, too?"
emi "ฉันก็ไม่ได้มาช้าเป็นครั้งแรกสักหน่อย นี่นายเป็นห่วงทุกครั้งที่ฉันมาช้าเลยหรือไง"

# hi "Er, not really."
hi "เอ้อ ก็ไม่นะ"

show emi basic_closedgrin
with charachange

# "Emi seems slightly amused by this. I don't know why, but that kind of pisses me off."
"เอมิดูชอบใจเล็กน้อย ไม่รู้ทำไมฉันถึงหงุดหงิดขึ้นมา"

show emi basic_grin
with charachange

# emi "So why was this time an exception?"
emi "แล้วทำไมถึงเป็นห่วงแค่ครั้งนี้ล่ะ"

# "Maybe it's the light, teasing tone of the question, but something in her response pushes me to be honest, though I can't help snapping at her when I say it."
"คำถามของเธอกดดันให้ฉันต้องพูดออกมาตรง ๆ อาจจะเพราะด้วยน้ำเสียงที่ฟังเหมือนไม่ใช่เรื่องจริงจัง แค่หยอกเล่น\nไปเท่านั้น ฉันอดโกรธเอมิไม่ได้เมื่อต้องพูดออกมา"

play music music_innocence fadein 10.0

# hi "Because you've been worrying me since dinner at your house, that's why."
hi "เพราะเธอทำให้ฉันเป็นห่วงตั้งแต่ที่เราไปกินข้าวเย็นกันที่บ้านเธอตอนนั้นแล้วไง"

show emi basic_hes
with charachange

# "Well. Now it's out in the open. And Emi's eyes are wide, and she looks like she wants to bolt, but she doesn't."
"เอาละ พูดออกไปชัด ๆ แล้ว เอมิตาเบิกโพลงทำหน้าเหมือนอยากวิ่งหนี แต่เธอก็ยังอยู่ตรงนี้"

show emi sad_shy
with charachange

# emi "Ah. Still on that, I see."
emi "อ้อ ยังไม่จบเหรอ โอเค"

# hi "What, you think I'm supposed to just forget about it? You threw me out of your house! We've been going on for almost a week pretending it never happened!"
hi "อะไร นี่กะจะให้ฉันลืม ๆ ไปเลยหรือไง เธอไล่ฉันออกจากบ้านนะ! เราทำเหมือนไม่มีอะไรเกิดขึ้นมาหนึ่งสัปดาห์แล้วนะ!"

show emi sad_annoyed
with charachange

# emi "I didn't see you bringing it up either, you know."
emi "ก็ไม่เห็นนายจะพูดถึงเหมือนกันนี่"

# hi "I know, and I'm sorry that was the case. We have to address it, or we'll just keep up this whatever it is we've got right now."
hi "ฉันรู้ แล้วก็ขอโทษด้วยที่เป็นอย่างนั้นไป เราต้องคุยกันนะ ไม่งั้นเราก็จะต้องอยู่กันไปแบบนี้เรื่อย ๆ"

# hi "It's killing me to look at how you look right now, did you know that? Those circles under your eyes and that distracted look in them, and I can't help worrying that I've caused it somehow."
hi "แค่เห็นสภาพเธอฉันก็เหมือนจะตายให้ได้อยู่แล้ว รู้ตัวบ้างไหม ขอบตาดำ ๆ กับสีหน้าเหม่อ ๆ ของเธอน่ะ\nฉันก็อดคิดมากไม่ได้ว่าที่เธอเป็นแบบนี้เพราะฉันหรือเปล่า"

show emi sad_pout
with charachange

# emi "You haven't. Trust me."
emi "ไม่ใช่เพราะนายหรอก เชื่อฉันสิ"

# hi "Well I haven't helped, either. I keep pushing you to tell me things you aren't ready to tell me; maybe I was wrong to try getting your mother to help me out, but I've been so worried about you that I didn't know what else to do."
hi "โอเค แต่ฉันก็ไม่ได้ช่วยเธอเลยด้วย ฉันเอาแต่ตื๊อให้เธอเล่าเรื่องที่เธอยังไม่พร้อมบอกฉัน ฉันอาจจะผิดเองที่ขอ\nให้แม่เธอช่วย แต่ฉันเป็นห่วงเธอมากจริง ๆ จนไม่รู้จะทำยังไงดีแล้ว"

show emi sad_depressed
with charachange

# emi "Well, you don't have to worry about me any more, okay? I think it's pretty clear we're not right for each other, so maybe we should just… stop."
emi "งั้นนายก็ไม่ต้องเป็นห่วงฉันอีกต่อไปแล้วละ โอเคไหม ฉันว่าก็ชัดแล้วนะว่าเราสองคนเข้ากันไม่ได้ เพราะงั้นเรา…\nหยุดก่อนดีกว่า"

# "Her face is twisted up as she says this, like she doesn't want to say it but forces herself to anyway."
"เอมิพูดพลางทำหน้ากระตุกเหมือนใจจริงไม่อยากพูดแต่ก็ฝืนพูดออกมา"

# hi "You don't actually want that, do you? Heck, you can barely bring yourself to say it. Anyway it won't keep me from worrying about you. I care too much about you to just stop on command."
hi "จริง ๆ เธอก็ไม่ได้อยากหยุดใช่มั้ยล่ะ ไม่สิ เธอแทบพูดไม่ออกด้วยซ้ำ แต่นั่นแหละ พูดไปฉันก็ไม่ได้เลิกเป็นห่วงหรอก\nฉันให้ความสำคัญกับเธอมากเกินกว่าที่จะให้ใครมาสั่งให้หยุดได้ง่าย ๆ"

# hi "You don't want to tell me what's wrong? That's fine, but I won't stop trying to help you, even if it's just standing by you."
hi "ไม่อยากบอกฉันใช่มั้ยล่ะว่ามีเรื่องอะไร ไม่ต้องบอกหรอก แต่ฉันจะไม่หยุดหาทางช่วยเธอหรอกนะ ต่อให้จะทำได้แค่\nอยู่เคียงข้างเธอก็เถอะ"

show emi sad_angry
with charachange

# emi "Stop saying that!"
emi "เลิกพูดแบบนั้นได้แล้ว!"

# "She's shaking now, and as she looks at me I can see she's afraid and frustrated and a million different things all at once. I shake my head slowly and take a few steps toward her."
"ตอนนี้เอมิตัวสั่นแล้ว พอเธอมองมาฉันก็เห็นว่าเธอทั้งกลัวทั้งกระวนกระวายทั้งอะไรหลายล้านอย่างพร้อม ๆ กัน\nฉันส่ายหน้าช้า ๆ แล้วเดินเข้าไปหาเอมิ"

# hi "You know what your mom told me? She told me that you'd never ask for help, because you know that you're strong enough to get through anything on your own, but that's not the full story, is it?"
hi "รู้มั้ยว่าแม่เธอบอกฉันว่ายังไง แม่เธอบอกว่าเธอไม่เคยขอความช่วยเหลือเลย เพราะเธอรู้ตัวว่าเข้มแข็งพอ\nที่จะก้าวผ่านอะไรทุกอย่างไปได้ด้วยตัวเอง แต่เรื่องไม่ได้มีแค่นั้นใช่มั้ยล่ะ"

show emi basic_hes
with vpunch

# "Her eyes go wide, and she takes a step back. I keep going, because I think I've finally figured it out. Something tells me I won't get another shot. I've put it off for far too long as it is."
"เอมิทำตาโตแล้วถอยไปหนึ่งก้าว ฉันเดินเข้าหาเธออีกเพราะคิดว่าฉันเข้าใจแล้วสักที ฉันสังหรณ์ว่าจะไม่มีโอกาส\nครั้งที่สองแล้ว เท่านี้ฉันก็เลื่อนเวลามานานมากแล้ว"

# hi "There's no harm in having someone help you, unless you're worried about needing help in the first place. You're scared, aren't you? Because of…"
hi "การขอความช่วยเหลือจากใครสักคนน่ะไม่ใช่เรื่องไม่ดีหรอกนะ เว้นก็แต่ว่าเธอจะคิดมากเสียเอง เธอกลัวใช่มั้ยล่ะ\nเพราะ…"

# "I trail off, because I don't know for certain what happened to Emi's father, and I don't want to jump to a conclusion."
"ฉันลากเสียงไปเพราะไม่รู้แน่ชัดว่าเกิดอะไรขึ้นกับพ่อเอมิกันแน่ และยังไม่อยากด่วนสรุปอะไรเร็วเกินไป"

# hi "Well, never mind why, but it's okay to be afraid. You've been running from it and from me for so long, even though you know eventually you have to turn around and face your fear, and I'm going to be there to help when you do."
hi "เอาเถอะ ช่างเหตุผลก่อน แต่ถ้าเธอจะกลัวก็กลัวได้นะ เธอวิ่งหนีจากสิ่งนั้นกับฉันมานานมากแล้วทั้งที่รู้ดีว่าสักวัน\nเธอก็ต้องหันมาเผชิญหน้ากับความกลัวของตัวเองอยู่ดี และฉันจะคอยอยู่เคียงข้างช่วยเหลือเธอเมื่อถึงวันนั้น"

# hi "I won't stop, because I don't think you'd want me to. You can understand that sort of determination, can't you?"
hi "ฉันจะไม่หยุดหรอก เพราะเธอคงไม่อยากให้ฉันหยุด เธอคงเข้าใจความเด็ดเดี่ยวแบบนี้ใช่มั้ยล่ะ"

# "I can see that I've gotten through to her, but she quickly falls back to anger to try and push me away again."
"ฉันดูออกว่าเอมิเข้าใจในสิ่งที่ฉันพูดแล้ว แต่เธอก็รีบโกรธขึ้นมาแล้วผลักไสฉันออกไปอีกครั้ง"

show emi sad_angry
with charachange

# emi "Back on your white charger, Hisao? Gotta help the poor cripple face her emotional problems? What do you know about me, and about what I've already had to face?"
emi "จะเล่นเป็นพระเอกขี่ม้าขาวอีกแล้วเหรอฮิซาโอะ จะมาช่วยสาวพิการให้เผชิญหน้ากับปัญหาทางจิตใจเหรอ นายรู้ดี\nเรื่องฉันกับสิ่งที่ฉันต้องเผชิญมาแล้วมากขนาดนั้นเลยหรือไง"

show emi sad_grit
with charachange

# emi "You think two months of learning to walk again was fun? But I did it, and after I did that I had to…"
emi "นายคิดว่าการที่ฉันต้องหัดเดินอยู่สองเดือนมันสนุกนักเหรอ แต่ฉันก็ผ่านมาแล้ว และหลังจากนั้นฉันก็ต้อง…"

# "For a moment it seems as if she's going to say something else, but she cuts herself off."
"แวบหนึ่งเอมิทำทีเหมือนจะพูดอะไรอย่างอื่นอีกแต่ก็ตัดบทตัวเองทิ้งไป"

# hi "And after all that, you don't think you can get past your fear? Emi, I can't fathom what you've been through, but to come through it and still be the sort of girl that you are, well, it makes me think that you have even more strength than you think."
hi "และเธอผ่านอะไรมาขนาดนั้นแล้วแต่ยังคิิดว่าจะก้าวข้ามความกลัวของตัวเองไม่ได้เหรอ เอมิ ฉันไม่อาจรู้ซึ้งได้หรอกนะ\nว่าเธอผ่านอะไรมาบ้าง แต่พอฉันเห็นว่าเธอยังอยู่มาจนเป็นตัวเธออย่างทุกวันนี้แล้ว ฉันก็คิดว่าจริง ๆ แล้วเธอเข้มแข็ง\nกว่าที่เธอคิดมาก"

# hi "So I'm not going to help you because I think you need rescuing. I don't want to be a knight rescuing the damsel in distress, but even knights helped each other out, you know. I want to help you, even though I know you can do it on your own."
hi "เพราะงั้นฉันจะไม่ได้มาช่วยเธอเพราะเห็นว่าเธอต้องการความช่วยเหลือ ฉันไม่ได้อยากเป็นอัศวินที่มาช่วย\nสาวน้อยเดือดร้อน แต่แม้แต่อัศวินยังต้องช่วยกันเองเลย ฉันอยากช่วยเธอทั้งที่รู้ดีว่าเธอก็จัดการเองได้"

show emi sad_depressed
with charachange

# "For a moment it looks like Emi's going to break down completely, but she doesn't. Tears run down her face, but she stares at me steadily."
"แวบหนึ่งเอมิเหมือนพร้อมจะปลดปล่อยอารมณ์ทั้งหมดออกมาแล้ว แต่เธอยังนิ่งปล่อยให้น้ำตาไหลอาบแก้มจ้องฉัน\nไม่วางตา"

# emi "Why are you trying so hard to help me?"
emi "ทำไมนายถึงพยายามจะช่วยฉันขนาดนี้"

# hi "I'd say that it's because I owe you one for helping me out when we first met, but that wouldn't be the truth. The truth is, I just want you to be happy, because I love you."
hi "ก็อยากจะพูดอยู่หรอกว่าเพราะติดหนี้บุญคุณที่เธอช่วยฉันไว้ตอนเจอกันครั้งแรก แต่ความจริงไม่ใช่อย่างนั้น\nสักหน่อย เหตุผลจริง ๆ คือฉันอยากให้เธอมีความสุข เพราะฉันรักเธอ"

stop music fadeout 4.0

# "Had I ever said that before? We've been in a relationship, and it's been pretty obvious that I love her, but did I ever actually speak the words?"
"ฉันเคยพูดคำนี้มาก่อนหรือเปล่านะ เราคบกัน และก็ชัดอยู่ว่าฉันรักเอมิ แต่ฉันเคยพูดออกมาจริง ๆ หรือเปล่า"

show emi sad_shyblush
with charachange

# emi "What did you say?"
emi "นายว่าไงนะ"

# "I say it again, savoring the feeling of being able to say it at all, being able to say it and mean it. Emi seems stunned."
"ฉันพูดอีกครั้งพลางกำซาบความรู้สึกดีที่พูดออกมาจากใจจริงได้เสียที เอมิตะลึงงันไป"

# hi "I said I love you, Emi. I love you. Just you, and that makes me want to stand by you, no matter what you have to face."
hi "ฉันบอกว่าฉันรักเธอ เอมิ ฉันรักเธอ แค่เธอคนเดียว เพราะรักถึงอยากอยู่ข้างเธอ ไม่ว่าเธอจะต้องเผชิญหน้า\nกับอะไรก็ตาม"

play music music_serene fadein 0.5

show emi excited_sad_close
with vpunch

# "I'm wrapped in a fierce hug then, as Emi begins to sob against my chest."
"แล้วเอมิก็โผตัวเข้ามากอดซุกหน้าอกฉันแล้วสะอื้นไห้"

# emi "I'm sorry! I'm so sorry about everything but I'm so scared, Hisao, I'm so scared of losing you and I love you too but I can't lose you I just… I'm so sorry!"
emi "ขอโทษนะ! ฉันขอโทษกับทุกอย่างที่ผ่านมาเลย แต่ฉันกลัวเหลือเกินฮิซาโอะ ฉันกลัวว่าจะต้องเสียนายไป\nฉันรักนายเหมือนกันแต่ฉันจะเสียนายไปไม่ได้ฉัน… ฉันขอโทษจริง ๆ !"

show emi sad_shy
with charadistant

# "I hold her quietly, shushing her until she settles down. She steps back, a little more composed."
"ฉันกอดเอมิอยู่เงียบ ๆ แล้วโอ๋เธอจนเธอสงบลง เอมิผละตัวออกดูใจเย็นลงบ้าง"

# emi "Will you come with me tomorrow? Back to my house? There are some things I need to show you, if I'm going to do this."
emi "พรุ่งนี้ไปด้วยกันกับฉันมั้ย กลับไปที่บ้านน่ะ พอดีฉันมีอะไรที่ต้องให้นายได้เห็น ถ้าฉันจะเปิดใจจริง ๆ"

# hi "Of course. Maybe this time we can leave together, instead of separately."
hi "ได้สิ แล้วคราวนี้เราอาจจะได้กลับด้วยกันแทนที่จะแยกกันกลับก็ได้"

show emi sad_grin
with charachange

# "Emi grins, a sudden flash of brightness that seems more genuine than anything I've seen in the past week."
"เอมิยิ้ม เป็นรอยยิ้มสดใสที่ดูจริงใจกว่าที่ฉันเคยเห็นมาตลอดสัปดาห์นี้เลย"

# emi "Yeah, maybe."
emi "อื้ม มั้งนะ"

play sound sfx_warningbell

# "The lunch bell rings, and I curse the universe's poor sense of timing."
"เสียงระฆังพักเที่ยงดัง ฉันก่นด่าโลกนี้ที่กะจังหวะได้ไม่ลงตัวเอาเสียเลย"

# hi "Are you free tonight? We can talk more then, right?"
hi "คืนนี้ว่างหรือเปล่า ไว้คุยกันอีกไง"

# "Emi shakes her head."
"เอมิสั่นหัว"

show emi sad_depressed
with charachange

# emi "Sorry Hisao, but I'm still helping the track team. Plus, I don't think it would be good if we talked this over tonight. I'm going to be too tired to think properly, and I want to be able to tell you everything without screwing it up."
emi "ขอโทษทีนะฮิซาโอะ พอดียังต้องไปช่วยงานทีมวิ่งอยู่น่ะ อีกอย่าง ฉันว่าถ้าคุยเรื่องนี้กันตอนค่ำคงไม่ดีเท่าไหร่\nเพราะฉันจะเพลียจนคิดอะไรไม่ค่อยถนัด แล้วฉันก็อยากบอกนายทุกอย่างให้เป็นเรื่องเป็นราวโดยไม่ทำอะไรพลาดด้วย"

show emi sad_shy
with charachange

# emi "You can wait, right?"
emi "นายรอได้ใช่มั้ย"

# "Even now, there's a bit of fear in her voice. I smile and rest a hand on her shoulder."
"แม้แต่ตอนนี้น้ำเสียงเอมิยังเจือด้วยความกลัวอยู่ ฉันยิ้มแล้วจับไหล่เธอ"

# hi "Okay. I'll be waiting."
hi "โอเค จะรอนะ"

show emi excited_amused_close
with characlose

# "Emi gives me a quick kiss before she heads for the stairwell."
"เอมิจุ๊บฉันแล้วเดินไปทางประตู"

show emi sad_grin
with charadistant

# emi "Thanks, Hisao. See you tomorrow morning."
emi "ขอบคุณนะฮิซาโอะ เจอกันเช้าวันพรุ่งนี้"

# hi "Wouldn't miss it."
hi "เจอกัน ๆ"

hide emi
with charaexit

$ renpy.music.set_volume(1.0, 2.0, channel="ambient")
stop ambient fadeout 2.0

scene bg school_staircase1
with locationchange

# "I head down the stairs with the feel of her lips on mine, suddenly aware of how much I've missed that sensation. I'll have to remember to thank Rin for getting us to talk to one another."
"ฉันเดินลงบันไดมา สัมผัสจากริมฝีปากเธอยังคงค้างอยู่ และจู่ ๆ ก็รู้ตัวว่าตัวเองคิดถึงสัมผัสนี้มากแค่ไหน\nไว้ต้องไปขอบคุณรินแล้วที่เปิดโอกาสให้เราสองคนได้คุยกัน"

# "Although it's possible she won't even realize what she's done. Still, if not for her I doubt I'd have ever been able to confront Emi again."
"ซึ่งก็เป็นไปได้ว่ารินคงไม่รู้ตัวเหมือนกันว่าทำอะไรดี ๆ ไว้ แต่ก็นะ ถ้าไม่มีรินแล้วฉันก็คงไม่มีโอกาสที่จะได้ประจันหน้า\nคุยกับเอมิแบบนั้นอีกหรอก"

# "I guess I needed more help than I realized. Tomorrow, however, I'll need to stand alone through whatever Emi's trying to work herself up to doing."
"ฉันเองก็ต้องมีคนมาคอยช่วยบ่อยกว่าที่คิดแฮะ แต่ว่าวันพรุ่งนี้จะมีเพียงฉันที่ต้องเจอกับอะไรก็ตามที่เอมิ\nเตรียมจะทำจะบอกกับฉัน"

# "I'll be up to the task. I hope."
"ฉันจะต้องทำหน้าที่นั้นได้สำเร็จ หวังว่านะ"

stop music fadeout 2.0

scene black
with dissolve

$ suppress_window_after_timeskip = True

#########################

label th_E30:

window hide None

scene black
with dissolve

with Pause(2.0)

play sound sfx_alarmclock

with Pause(3.0)

scene bg school_dormhisao
with openeye

window show

# "The morning sun is bright through my open window, and the sound of my alarm quickly has me up and about."
"แดดยามเช้าส่องผ่านหน้าต่างฉัน เสียงนาฬิกาปลุกปลุกให้ฉันลุกขึ้น"

# "I slept surprisingly well last night, secure in the knowledge that at least I've got another chance with Emi."
"เมื่อคืนฉันนอนหลับสนิทอย่างเหลือเชื่อเพราะรู้ว่าได้มีโอกาสเริ่มต้นใหม่กับเอมิอีกครั้ง"

# "If I can just keep myself from doing anything stupid, maybe I'll find out what's been eating her recently."
"ถ้าฉันห้ามตัวเองไม่ให้ทำอะไรโง่ ๆ แล้วอาจจะรู้ก็ได้ว่าช่วงนี้เอมิคิดมากเรื่องอะไร"

# "I have a few educated guesses, but nothing concrete. And certainly nothing that I'm going to say to her; I'd much prefer to have her tell me herself."
"ฉันพอจะอนุมานได้สองสามอย่าง แต่ก็ไม่ได้แน่ใจนัก และฉันจะไม่เอาไปบอกเอมิแน่นอน รอให้เจ้าตัวบอกเองเลยดีกว่า"

#if you came from e29, see this

label th_E30a:

# "Although I can't help remembering the nurse's warning that I might not like what she has to say. Do I really need to know that badly?"
"แต่ฉันก็อดนึกถึงที่คุณพยาบาลเตือนไม่ได้ว่าฉันอาจจะไม่อยากฟังสิ่งที่เอมิจะบอกนัก แล้วฉันอยากรู้ขนาดนั้นเลย\nหรือเปล่า"

# "What if it's something awful that makes me repulsed by her? Can I really say that I'm prepared to handle whatever she has to say, regardless of what it is?"
"ถ้าเป็นอะไรที่แย่มากจนฉันแขยงเอมิขึ้นมาล่ะ ฉันเตรียมใจพร้อมฟัง{i}ทุกอย่าง{/i}จากเอมิจริง ๆ แล้วหรือยัง"

# "Emi said she wanted to tell me “without screwing it up.” What the hell did she mean by that? What's there to screw up?"
"เอมิบอกว่าอยากบอกได้โดยที่ “ไม่ทำอะไรพลาด” หมายความว่ายังไงกันแน่ มีอะไรให้พลาดด้วยเหรอ"

# "I suppose there's not much use worrying about it, though. I'll find out today. It occurs to me that I really, really need a run this morning, to clear my head if nothing else."
"แต่กังวลไปก็คงไม่ได้อะไร ยังไงวันนี้ก็จะได้รู้ แล้วฉันก็นึกได้ว่าเช้านี้จำเป็นต้องออกไปวิ่ง อย่างน้อยก็เพื่อทำให้สมอง\nปลอดโปร่ง"

#if you came from e27, you'll just drop in at this point

label th_E30b:

scene bg school_track
show emi basic_grin_gym at center
with locationskip

# "Emi is waiting for me as promised, looking a little haggard but otherwise bright and cheerful. Much more so than any previous day this week."
"เอมิรอฉันอยู่ตามสัญญา ดูเพลียเล็กน้อยแต่ยังสดใสร่าเริง สดใสร่าเริงกว่าวันก่อน ๆ ที่ผ่านมามาก"

show emi excited_proud_gym
with charachange

# emi "Hisao! You're late!"
emi "ฮิซาโอะ! มาช้านะนาย!"

# "I wave my hand dismissively."
"ฉันโบกไม้โบกมือ"

# hi "Nonsense! You're just early."
hi "ไร้สาระ! เธอมาเร็วต่างหาก"

play music music_emi fadein 2.0

show emi basic_closedgrin_gym
with charachange

# "Emi grins back, and it feels like we're finally back where we should be with one another."
"เอมิส่งยิ้มกลับ รู้สึกเหมือนว่าเราได้กลับไปเป็นดังเดิมอย่างที่ควรแล้วสักที"

# "Except now Emi, not just me, wants to take another step forward. Although a part of me worries that she'll back out at the last second."
"เว้นเสียก็แต่ตอนนี้เอมิอยากก้าวไปข้างหน้าบ้างแล้ว ไม่ได้มีแค่ฉันคนเดียว ใจหนึ่งฉันก็ยังกังวลว่าเอมิจะถอนตัว\nเอาวินาทีสุดท้ายหรือเปล่า"

show emi basic_grin_gym
with charachange

# emi "Hurry up and stretch, Hisao! I don't want to miss the bus!"
emi "รีบยืดเส้นยืดสายกันได้แล้วฮิซาโอะ! เดี๋ยวฉันตกรถบัส!"

# hi "The bus?"
hi "รถบัสเหรอ"

show emi sad_grin_gym
with charachange

#if you came from e27, see this

label th_E30c:

# emi "Yeah, the bus. I want to show you something, and I don't want to be late."
emi "อื้ม รถบัส ฉันมีอะไรที่อยากให้นายได้เห็นน่ะ แล้วก็ไม่อยากช้าด้วย"

# hi "Oh, okay."
hi "อ้อ โอเค"

# "I try not to grin too wide. I'm happy beyond words that Emi wants to hang out after the run at all, but her promise of showing me something has me even more intrigued."
"ฉันกลั้นใจไม่ให้ยิ้มกว้างมากไป ฉันสุขใจเกินบรรยายที่เอมิอยากอยู่ต่อหลังวิ่งเสร็จแล้ว แต่ที่ฉันสนใจกว่านั้น\nคือการที่เธอบอกว่ามีอะไรจะให้ฉันได้ดู"

# "Is this what she had to think about? I wonder just what she's planning to do."
"นี่น่ะเหรอเรื่องที่ว่าต้องไปคิดมาก่อน นี่เอมิวางแผนจะทำอะไรกันนะ"

#if you came from e29, see this

label th_E30d:

# emi "I said I wanted you to come back to my house, remember? And I promised mom we'd be there in time for lunch, so I wanted to hurry!"
emi "ฉันบอกว่าอยากให้นายมาบ้านฉันด้วยกันไง ลืมแล้วเหรอ แล้วฉันก็รับปากกับแม่ไว้แล้วด้วยว่าจะไปกินข้าวเที่ยง\nกันด้วย เลยอยากรีบ ๆ ไปน่ะ!"

# hi "Early start, huh?"
hi "ไปเช้าจังเลยนะ"

show emi basic_closedgrin_gym
with charachange

# emi "It's more for my mom's benefit than anything else."
emi "หลัก ๆ ก็เพื่อแม่ฉันนั่นแหละ"

# hi "Ah, well that's okay."
hi "อ้อ ได้ โอเค"

# "I unsuccessfully try to guess what Emi has planned, shortly before realizing that it doesn't matter that much to me."
"ฉันเดาไม่ถูกเลยว่าเอมิวางแผนอะไรไว้ ก่อนจะนึกได้ว่าเรื่องนั้นไม่ได้สำคัญอะไรกับฉันนัก"

#end of split

label th_E30e:

show emi basic_concentrate_gym
with charachange

play sound sfx_gymbounce

show emi gymconcentratebounce
with None

# "I quickly go through my warm up routine while Emi bounces impatiently from one foot to the other. She really does seem to want to get moving as soon as possible."
"ฉันรีบวอร์มอัพอย่างที่ทำประจำ ส่วนเอมิเด้งตัวสลับขาไปมาอย่างร้อนใจ ดูท่าว่าจะอยากรีบไปแล้วจริง ๆ"

scene bg school_track_running
with shorttimeskip

# "The run is over so quickly I can barely believe that I haven't fallen over dead afterwards. Emi set a blistering pace and I, in my foolishness, kept up with her."
"เราวิ่งเสร็จกันเร็วมากจนฉันแทบไม่อยากเชื่อว่าพอวิ่งแล้วฉันยังมีชีวิตอยู่ เอมิวิ่งด้วยความเร็วสูง และฉัน\nก็วิ่งตามเธอไปด้วยความโง่เง่า"

scene bg school_track_on
with Dissolve(2.0)

show emi basic_grin_gym at center
with charaenter

# "Well, until the last few laps. I had to slow down just in case. But I don't mind, and Emi's waiting patiently for me when I finish. As patiently as she can wait, anyway."
"แต่ก็ได้ไม่กี่รอบน่ะนะ สุดท้ายก็ต้องผ่อนฝีเท้าลงเพื่อความปลอดภัย แต่ฉันก็ไม่ได้ใส่ใจอะไรนัก เอมิรอให้ฉันวิ่งเสร็จ\nอยู่อย่างใจเย็น ซึ่งก็ใจเย็นเท่าที่เธอจะรอไหวนั่นแหละ"

show emi basic_closedgrin_gym_close
with vpunch

# emi "Finished? Good! Come on!"
emi "วิ่งเสร็จแล้วใช่มั้ย ดี! ไปกัน!"

stop music fadeout 2.0

scene bg school_nursehall
with locationskip

# "Grabbing my arm, she practically rushes me down to the nurse's office."
"เอมิคว้าแขนฉันไว้แล้วรีบลากฉันไปที่ห้องพยาบาล"

play music music_nurse fadein 0.5

show nurse neutral:
    twoleft
    xpos 0.2
    easein 0.5 twoleft
with charaenter

# nk "You seem in a hurry, Emi. Trying to catch the early bus?"
nk "ดูเธอรีบ ๆ นะเอมิ จะไปขึ้นรถบัสเที่ยวเช้าเหรอ"

show emi basic_grin_gym at tworight
with charaenter

# emi "Yeah, I told mom I'd be back for lunch."
emi "ค่ะ พอดีบอกแม่ไว้ว่าจะไปกินข้าวเที่ยง"

show nurse grin at twoleft
with charachange

# nk "Well, I'll take care of you first, then."
nk "โอเค งั้นเดี๋ยวตรวจเธอก่อนแล้วกัน"

show emi basic_confused_gym
with charachange

# emi "But Hisao's gotta come with me too!"
emi "แต่ฮิซาโอะจะไปกับหนูด้วยนะ!"

show nurse fabulous
with charachange

# "The nurse raises a single eyebrow at this statement and peers at the two of us searchingly."
"คุณพยาบาลเลิกคิ้วขึ้นข้างหนึ่งกับประโยคนั้นแล้วมองเราสองคนไปมา"

# nk "Really? Today, huh?"
nk "จริงเหรอ วันนี้น่ะนะ"

show emi sad_grin_gym
with charachange

# "Emi's response is a nod, followed by a surprisingly shy grin."
"เอมิพยักหน้าตอบ ส่วนคุณพยาบาลก็ยิ้มอาย ๆ ผิดคาด"

show nurse grin
with charachange

# nk "Well then, we'll make this quick."
nk "โอเค งั้นเดี๋ยวจะรีบหน่อยแล้วกัน"

hide nurse
hide emi
with charaexit

# "Emi enters the nurse's office, and I patiently wait outside for her to be finished, wondering just why the nurse seemed to be surprised by Emi's declaration."
"เอมิเข้าห้องพยาบาลไป ฉันรอให้เธอรับการตรวจเสร็จอยู่ข้างนอกอย่างใจเย็นพลางคิดว่าทำไมคุณพยาบาลถึงดูแปลกใจ\nกับคำพูดของเอมิ"

# "I feel like I'm missing out on some joke or the significance of today. Beyond the fact that it is clearly significant in some way, of course."
"หรือฉันจะไม่เข้าใจมุกอะไรหรือความสำคัญของวันนี้หรือเปล่า ถ้าไม่นับเรื่องความสำคัญที่เห็นได้ชัดน่ะนะ"

scene bg school_nurseoffice
with shorttimeskip

# "True to his word, the nurse has Emi out of his office surprisingly quickly, and I take her place after promising to meet up at the front gate. The nurse takes my pulse and listens for a bit."
"และเอมิก็ออกมาจากห้องพยาบาลเร็วผิดคาด คุณพยาบาลรีบตรวจอย่างที่บอกไว้จริง ๆ พอบอกกับเอมิว่าจะไปเจอกัน\nที่ประตูหน้าโรงเรียนแล้วฉันก็เข้าไปในห้องพยาบาลบ้าง คุณพยาบาลจับชีพจรฉันแล้วฟังอยู่ครู่หนึ่ง"

show nurse fabulous at center
with charaenter

# nk "Your heartbeat's faster than usual. Been pushing yourself again, have you?"
nk "ใจเต้นเร็วกว่าปกตินะ นี่ฝืนตัวเองอีกแล้วเหรอ"

# hi "Well, Emi seemed in a rush to get through the run, so…"
hi "ก็ เอมิเหมือนจะรีบวิ่ง ๆ ให้เสร็จ ผมเลย…"

show nurse neutral
with charachange

# nk "Hm, I'm not surprised. Today is rather important to her, you know."
nk "อืม ก็ไม่แปลกใจหรอก วันนี้เป็นวันที่สำคัญกับเอมิเชียวละ"

# hi "I suspected that could be the case, but I have no idea why that's the case."
hi "ผมก็คิดว่าคงเป็นอย่างนั้นแหละครับ แต่ไม่รู้ว่าทำไม"

show nurse fabulous
with charachange

# nk "She hasn't told you? Interesting."
nk "เอมิยังไม่ได้บอกเหรอ น่าสนใจ"

# hi "So you're not going to tell me either, then."
hi "ก็คือคุณจะไม่บอกผมด้วยเหมือนกัน"

show nurse grin
with charachange

# nk "No, I'm not. I suspect that Emi has her own plan for explaining today to you, and I don't want to mess with that. You'll find out soon enough, so what's the rush?"
nk "ไม่ ไม่บอกหรอก ฉันว่าเอมิคงเตรียมจะเล่าเรื่องของวันนี้ให้เธอฟังแล้วละ แล้วฉันก็ไม่อยากไปยุ่งด้วย เดี๋ยวเธอ\nก็ได้รู้แล้ว ไม่ต้องรีบหรอก"

show nurse neutral
with charachange

# nk "Now as for your heart, I would take it easy the rest of the day. No spontaneous races or anything like that, got it?"
nk "ส่วนเรื่องหัวใจเธอ วันนี้ห้ามทำอะไรหักโหมอีกนะ ไม่ใช่ว่านึกจะวิ่งแข่งก็วิ่งตาม เข้าใจนะ"

# hi "Got it. She won't have her running legs on anyway, right?"
hi "เข้าใจแล้วครับ แต่ยังไงเอมิก็คงไม่ได้ใส่ขาเทียมสำหรับวิ่งอยู่แล้วนี่ครับ"

show nurse grin
with charachange

# nk "No, but if you think something like that is going to stop her…"
nk "ก็ใช่ แต่ถ้าเธอคิดว่าเอมิจะไม่วิ่งกับขาเทียมปกติแล้วละก็…"

# hi "Good point."
hi "ก็ถูกครับ"

show nurse neutral
with charachange

# nk "I don't think it'll be much of an issue today of all days, but still."
nk "ฉันว่าวันนี้เอมิไม่น่าทำอย่างนั้นหรอก แต่ก็นะ"

# "If he's trying to reassure me, he's doing a terrible job. I'm quickly becoming more and more worried about what today could be for, like suddenly finding out Emi's in a cult or something."
"ถ้าจุดประสงค์ของคำพูดนั้นคือการปลอบใจแล้วละก็ฉันไม่ได้สบายใจขึ้นเท่าไหร่เลย ฉันยิ่งคิดมากไปเรื่อย ๆ ว่าวันนี้\nคือวันอะไรกันแน่ เหมือนอยู่ ๆ ก็ได้รู้ว่าเอมิอยู่ในลัทธิหรืออะไรทำนองนั้น"

# "At the same time, if today is such a big deal and Emi wants me to be with her for it, then maybe she really does want to grow closer to me. Maybe this will be the answer to all the riddles, to the sleepless nights and the sudden mood swings."
"แต่ในขณะเดียวกัน ถ้าวันนี้เป็นวันที่สำคัญกับเอมิขนาดนั้นแล้วเธออยากให้ฉันอยู่ด้วย ก็แปลว่าเธออยากสนิทกับฉัน\nจริง ๆ หรือสิ่งนี้อาจจะเป็นกุญแจไขปริศนาถึงเหตุผลที่ทำให้เธอนอนไม่หลับและอารมณ์แปรปรวน"

stop music fadeout 1.0

scene bg school_dormhisao
with locationskip

# "Either way, I barely remember to thank the nurse before taking off as quickly as I dare for my room, to get a shower and throw on some decent-looking clothes. If today is as important as it seems to be, I should dress appropriately."
"และสุดท้ายฉันก็แทบลืมขอบคุณคุณพยาบาล จากนั้นฉันรีบออกมามุ่งหน้าไปยังห้องตัวเองเพื่ออาบน้ำเปลี่ยนเสื้อผ้า\nให้ดูดีขึ้นมาอีกหน่อย ถ้าวันนี้เป็นวันสำคัญอย่างที่คิดจริง ๆ แล้วก็ต้องแต่งตัวให้เหมาะสม"

scene bg school_gate
show emicas grin at center
with locationskip

play music music_dreamy fadein 2.0

# "Emi, of course, proves me wrong as soon as I reach the front gate, wearing her usual shirt and shorts. So at least I know it's not a terribly formal affair, whatever it is."
"ซึ่งแน่นอน ทันทีที่ได้เห็นเอมิที่ใส่เสื้อยืดกับกางเกงขาสั้นตัวเก่งยืนรอตรงประตูหน้าโรงเรียนก็รู้ตัวว่าฉันคิดผิด\nอย่างน้อยฉันก็ได้รู้ว่าไม่ใช่เรื่อง—จะเรื่องอะไรก็ช่าง—ที่เป็นทางการจ๋าขนาดนั้น"

show emicas smile
with charachange

# emi "You're early, Hisao."
emi "มาไวนะฮิซาโอะ"

# hi "Not as early as you. Eager, are we?"
hi "เธอไวกว่าอีก รีบเหรอ"

show emicas wink_up
with charachange

# "Emi cheekily pokes out her tongue."
"เอมิแลบลิ้นซุกซน"

show emicas closedsmile
with charachange

# "The bus stop isn't very crowded at this hour, which seems to please Emi, and we end up relaxing a little as we wait. We sit in silence for a while, but I can tell that Emi's trying to work herself up to say something."
"ช่วงเวลานี้ที่ป้ายรอรถบัสนั้นยังไม่มีคนมาก ซึ่งเอมิดูจะพอใจที่คนน้อย เรานั่งรอสบาย ๆ อยู่เงียบ ๆ กันสักพัก\nแต่ฉันดูออกว่าเอมิกำลังตั้งใจเตรียมพูดอะไรอยู่"

# "I don't have anything to say myself, so I sit waiting for her to talk. It doesn't take too long."
"ฉันเองก็ไม่มีอะไรจะพูดจึงนั่งรอให้เอมิพูดก่อน ซึ่งก็ไม่ต้องรอนานนัก"

show emicas awayfrown
with charachange

# emi "So uh, I'm sure you're curious as to why the nurse thought it was so weird for me to be bringing you along today…"
emi "คือ เอ่อ นายคงสงสัยใช่มั้ยว่าทำไมคุณพยาบาลถึงคิดว่าแปลกที่วันนี้ฉันพานายมาด้วย"

# hi "I was a bit, yes, but if you're not ready to tell me—"
hi "ก็นิดหน่อย แต่ถ้าเธอยังไม่พร้อมบอก—"

show emicas blush_close
with characlose

# "Emi stops my sentence by placing a finger on my lips."
"เอมิตัดบทฉันด้วยการยกนิ้วมาแนบริมฝีปากฉัน"

show emicas frown_close
with charachange

# emi "Don't tempt me, Hisao. I want to tell you this, but I'm just uncertain as to how to go about it. I don't want to keep delaying or deferring, I just want to be able to say it."
emi "อย่าพูดให้ฉันเปลี่ยนใจเลยฮิซาโอะ ฉันอยากบอกนาย แค่ยังไม่แน่ใจว่าจะบอกยังไงดี ฉันไม่อยากชักช้า\nรออะไรแล้ว อยากจะพูด ๆ ออกมาเลย"

# hi "So say it."
hi "งั้นก็พูดเลยสิ"

show emicas neutral_close
with charachange

# emi "You know that it's not going to be that easy for me, Hisao."
emi "นายก็รู้ว่าฉันพูดออกมาเลยแบบนั้นไม่ได้ ฮิซาโอะ"

# hi "So treat it like running. Warm up to it with something small and easy, and go from there. But don't do it too fast, okay? I'm a patient man, I can wait for you to get to it."
hi "งั้นก็คิดเสียว่าเป็นการวิ่งสิ วอร์มอัพด้วยเรื่องเล็ก ๆ ที่พูดง่าย ๆ ก่อน แล้วก็ไล่ลำดับไปเรื่อย ๆ แต่อย่าไปไวเกินนะ\nฉันเป็นคนใจเย็น รอให้เธอปรับตัวให้ชินก่อนได้"

show emicas awayfrown_close
with charachange

# "Emi seems to consider my words, weighing them against what is probably a desire to get it over with. I will admit, as much as I keep telling Emi to take her time, I wouldn't mind her getting it over with either."
"เหมือนเอมิจะเก็บคำพูดฉันไปคิดชั่งน้ำหนักกับความอยากที่จะให้เรื่องมันจบ ๆ ไป ซึ่งขอยอมรับว่าฉันเองก็รับได้เหมือนกัน\nถ้าเอมิจะรีบพูดให้เสร็จไปทีเดียว ถึงเมื่อกี้จะบอกให้เธอใช้เวลาได้เต็มที่ก็ตาม"

# "But somehow I know that Emi probably needs more time than the bus ride will provide to get it all out, whatever it is."
"แต่ฉันพอจะรู้ว่าเอมิคงต้องใช้เวลานานกว่าการนั่งรถบัสนี้ในการเรียบเรียงเรื่อง—จะเรื่องอะไรก็ช่าง—ทั้งหมดนี้ออกมา"

show emicas frown_close
with charachange

# emi "Yeah, maybe you're right. The bus stop probably isn't the best place for this anyway. But just to make sure that I don't go back on my word, I'll at least say this:"
emi "อื้ม ก็คงถูกของนาย ยังไงจะให้คุยที่ป้ายรอรถก็คงไม่เหมาะเท่าไหร่ แต่ก็ไม่อยากถอนคำพูดเอาทีหลังด้วย\nเพราะงั้นขอบอกแบบนี้ไว้ก่อนแล้วกัน"

show emicas awayfrown_close
with charachange

# "She takes a deep breath, lets it out, and after a moment says in a low voice,"
"เอมิสูดหายใจลึก ๆ แล้วพ่นลมออกมา ผ่านไปครู่หนึ่งเธอก็พูดเสียงเบาว่า"

show emicas weaksmile_close
with charachange

stop music fadeout 1.0

# emi "We're going to see my dad today."
emi "วันนี้เราจะไปหาพ่อฉันกัน"

# "The words hang in the air, and I can see that Emi's afraid that I'll panic and disappear in response. Which a part of me almost wants to do."
"คำพูดนั้นลอยอยู่ในอากาศ ฉันดูออกว่าเอมิกลัวว่าฉันจะตระหนกแล้วหนีไปเมื่อได้ยินเช่นนั้น ซึ่งใจหนึ่ง\nฉันก็อยากอยู่เหมือนกัน"

# "But it would be stupid of me to back out, or to suddenly abandon the promise I made to be there for Emi when she needs me."
"แต่ถ้าถอนตัวเอาตอนนี้หรือผิดสัญญาที่บอกว่าจะอยู่เคียงข้างเอมิในยามที่เธอต้องการฉันแล้วก็คงโง่มาก"

# "The nurse thought it was so weird of her to bring me along. She doesn't bring anyone along, or at least I'm willing to bet that she hasn't before today."
"คุณพยาบาลมองว่าแปลกที่เอมิพาฉันมาด้วย เอมิไม่ได้พาใครมาเลย อย่างน้อยก็แน่ใจในระดับหนึ่งเลยแหละ\nว่าก่อนหน้านี้ก็ไม่เคย"

# "The day seems to take on an even greater significance. What has it taken Emi to even get this far?"
"ซึ่งยิ่งทำให้วันนี้ดูสำคัญเข้าไปอีก เอมิต้องรวบรวมความกล้ามาแค่ไหนถึงทำได้ขนาดนี้"

play music music_dreamy fadein 5.0

# hi "Ah."
hi "อ้อ"

# "And why is that the best I can manage as a response?"
"แล้วทำไมฉันถึงตอบได้แค่นั้น"

show emicas neutral_close
with charachange

# emi "Yeah."
emi "อื้ม"

# hi "I uh, I don't know what I should say."
hi "ฉัน เอ่อ ฉันไม่รู้ว่าจะพูดอะไรดี"

# emi "Nothing, I think. Just promise that you're going to come with me."
emi "ก็คงไม่ต้องพูดอะไรหรอก แค่สัญญาว่าจะไปด้วยกับฉันก็พอ"

# hi "Of course! You know I will."
hi "แหงสิ! ไปอยู่แล้ว"

show emicas weaksmile_close
with charachange

# "Emi smiles wanly, looking a little relieved."
"เอมิยิ้มหงอย ๆ ดูโล่งใจขึ้นมาเล็กน้อย"

# emi "Good. In that case, we'd better get going."
emi "ดี ถ้างั้นก็รีบไปกันดีกว่า"

# "The bus pulls up just a little after she finishes the sentence."
"เอมิพูดจบได้ไม่นานรถบัสก็มาถึง"

scene bg city_street4
with shorttimeskip

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_traffic fadein 2.0

# "Vague memories of my first trip out here come to mind as I step off the bus, but unfortunately, they're too vague to be of any use."
"เมื่อลงจากรถบัสความทรงจำจากครั้งที่มาก่อนหน้านี้ผุดขึ้นมาราง ๆ แต่โชคไม่ดีที่รางเกินกว่าจะนึกทางได้"

# "I will be the first to admit that I don't quite recall how to get to Emi's house, so I let her lead the way."
"ถ้าให้ว่าตามตรงแล้วฉันก็จำทางไปบ้านเอมิไม่ได้ จึงให้เธอนำทางไป"

$ renpy.music.set_volume(1.0, 8.0, channel="ambient")
stop ambient fadeout 1.0

scene bg emi_houseext
with locationskip

# "She seems content to walk in silence, and I myself have no idea what I could possibly say, so the two of us arrive at her house having said nothing since getting off the bus."
"เอมิดูจะพอใจที่ได้เดินเงียบ ๆ ฉันเองก็ไม่รู้เหมือนกันว่าจะพูดอะไรได้ เราสองคนจึงมาถึงบ้านเอมิโดยไม่คุยอะไรกันเลย\nตลอดทางตั้งแต่ลงรถมา"

show meiko smile:
    tworight
    xpos 0.8
    easein 0.5 tworight
with charaenter

# "Emi's mother opens the door and doesn't seem surprised to see me standing next to her daughter.
# I expect that Emi would have phoned ahead to let her mother know of the change in plans."
"แม่เอมิมาเปิดประตูโดยที่ดูไม่แปลกใจเลยที่ฉันยืนอยู่ข้างเอมิ ก็คงโทร. บอกแม่ไว้แล้วแหละว่าจะเปลี่ยนแผน"

show meiko happy at tworight
with charachange

# emm "Emi, Hisao, you're just in time! Lunch is just about ready."
emm "เอมิ ฮิซาโอะ มาทันพอดีเลย! ข้าวเที่ยงจะเสร็จแล้วจ้ะ"

show emicas happy at twoleft
with charaenter

# emi "Great! I was afraid we might be running late."
emi "ดีเลยค่ะ! หนูก็กลัวอยู่ว่าจะมาช้าไปหรือเปล่า"

# hi "As fast as you were going this morning, I doubt there was much of a chance of that."
hi "ตอนเช้าวิ่งเร็วขนาดนั้นคงมาช้าอยู่หรอกมั้ง"

show meiko serious
with charachange

# emm "I certainly hope she wasn't too much of a bother, Hisao. She tends to get a little paranoid about being on time when food's involved."
emm "หวังว่าลูกสาวฉันจะไม่ทำให้เธอเดือดร้อนมากนะฮิซาโอะ พอเป็นเรื่องของกินแล้วเอมิชอบคิดมากว่าตัวเอง\nจะตรงเวลาหรือเปล่า"

# hi "I hadn't noticed."
hi "ไม่รู้เลยนะครับเนี่ย"

show emicas pout_up
with charachange

# "This earns me a swat on the arm from Emi, who despite the serious nature of our conversation on the bus and the almost brooding quiet walk has quickly become cheerful again."
"เอมิตบแขนฉันเบา ๆ เธอกลับมาร่าเริงอีกครั้งอย่างรวดเร็วทั้งที่ตอนอยู่บนรถบัสก็คุยเรื่องจริงจังกันและตอนเดินก็เงียบ\nมาตลอด"

# "Probably to keep her mother from worrying about whatever it is Emi plans to tell me later."
"อาจจะเพราะไม่อยากให้แม่ต้องเป็นห่วงเรื่องที่เธอเตรียมจะบอกกับฉัน"

scene bg emi_dining
with shorttimeskip

# "Mrs. Ibarazaki ushers us in, and in short order we're around the table devouring lunch. I hadn't realized how hungry I was until I got here, but for once I seem to be eating almost as much as Emi."
"คุณนายอิบาราซากิพาเราสองคนเข้าบ้านไป ไม่นานเราก็ได้มานั่งกินข้าวเที่ยงกันที่โต๊ะ ฉันเพิ่งหิวขึ้นมาก็ตอนที่\nมาถึงบ้าน เป็นครั้งแรกที่ฉันกินเยอะพอ ๆ กันกับเอมิ"

show meiko happy at tworight
show emicas closedsmile at twoleft
with charaenter

# emm "Goodness, it's a good thing I made so much. The two of you are acting like you haven't eaten in days!"
emm "ตายจริง ดีนะที่ทำไว้เยอะน่ะ เธอสองคนกินอย่างกับไม่ได้กินข้าวมาหลายวันแล้วแน่ะ!"

# hi "I skipped breakfast this morning."
hi "วันนี้ผมไม่ได้กินข้าวเช้าครับ"

show emicas grin
with charachange

# emi "Me too."
emi "หนูด้วย"

show meiko smile
with charachange

# emm "Had to catch the bus, I assume?"
emm "คงจะรีบมาขึ้นรถบัสสินะ"

show emicas wink_up
with charachange

# emi "That and I figured you'd make too much food so it wouldn't matter if I skipped breakfast."
emi "ก็ใช่ค่ะ แล้วหนูก็คิดไว้แล้วว่าแม่คงทำกับข้าวไว้เยอะ ต่อให้ไม่กินข้าวเช้ามาก็คงไม่เป็นไร"

show meiko wink
with charachange

# emm "Well, it's good to know that I'm predictable."
emm "แหม แม่เดาใจง่ายสินะจ๊ะเนี่ย"

show emicas grin_up
with charachange

# "Emi nods enthusiastically, and conversation falls off again as we very nearly clear the table of anything edible. It is a testament to the sheer amount of food on offer that we don't finish everything."
"เอมิพยักหน้าหงึก ๆ แล้วเราก็เงียบกันไปอีกครั้งเมื่อต่างหันกลับมาจัดการอะไรก็ตามที่กินได้ซึ่งอยู่บนโต๊ะนี้\nจนเกือบหมด และการที่เรายังกินเหลืออยู่นั้นก็เป็นการพิสูจน์ได้ว่าอาหารมื้อนี้มีมากแค่ไหน"

show emicas grin
show meiko smile
with shorttimeskip

# "I lean back in my chair with a sigh and thank Mrs. Ibarazaki for the food."
"ฉันเอนตัวพิงพนักถอนหายใจแล้วขอบคุณคุณนายอิบาราซากิสำหรับอาหารมื้อนี้"

show meiko happy
with charachange

# emm "I'm glad you liked it, Hisao. Now, has Emi told you where we're going?"
emm "ดีใจนะจ๊ะที่อาหารถูกปากเธอฮิซาโอะ เอาละ เอมิบอกเธอหรือยังว่าเราจะไปไหนกัน"

# hi "Yeah, sort of. Is it far from here?"
hi "ครับ บอกคร่าว ๆ แล้ว อยู่ไกลจากที่นี่มากมั้ยครับ"

show emicas closedsmile
with charachange

# emi "Not really, but we'll drive there to save time. It closes kind of early."
emi "ไม่ค่อยหรอก แต่เดี๋ยวจะให้แม่ขับรถไป จะได้เร็วหน่อย พอดีมันปิดไวน่ะ"

# "I nod in assent and stand up, ready to go."
"ฉันพยักหน้าตกลงแล้วยืนขึ้นเตรียมออกตัว"

# hi "Well then, shall we?"
hi "โอเค งั้นก็ไปกัน"

hide meiko
with charaexit

show bg emi_dining at bgright
show emicas awayfrown at center
with dissolvecharamove

# "Mrs. Ibarazaki nods and leaves the room to grab her keys. Emi, I notice, has started to fidget nervously."
"คุณนายอิบาราซากิพยักหน้าแล้วออกห้องไปหากุญแจรถ ฉันเห็นว่าเอมิเริ่มบิดตัวด้วยความประหม่า"

# hi "Second thoughts?"
hi "เปลี่ยนใจแล้วเหรอ"

show emicas weaksmile
with charachange

# "Emi smiles tightly at me and shrugs. She's fallen silent again, which probably means that I'm right, and she is starting to regret bringing me along."
"เอมิเม้มปากยิ้มยักไหล่ให้ฉัน เงียบไปอีกแล้ว คงแปลว่าฉันคิดถูกที่ตอนนี้เธอเริ่มคิดว่าไม่น่าพาฉันมาแล้ว"

# "Not that I blame her; she's done such a good job of shutting me out that I doubt it's easy to suddenly open up. Honestly, I'm worried that she's forcing it."
"แต่ก็ว่าไม่ได้หรอก เอมิปิดใจสนิทกีดฉันออกได้ขนาดนั้น จะให้อยู่ ๆ เปิดใจเลยคงไม่ง่าย ว่าตามตรง ตอนนี้\nฉันก็กังวลแล้วว่าเอมิฝืนตัวเองอยู่หรือเปล่า"

# "But she said while waiting for the bus that I'm not supposed to give her a chance to back out, and since I promised to go with her anyway, I suppose there's not much of a choice. I can't go back on my promise, and she can't go back on hers."
"แต่เอมิบอกกับฉันตอนเรารอรถบัสแล้วว่าห้ามฉันให้โอกาสเธอถอนตัว และอย่างไรฉันก็รับปากไว้แล้วว่าจะไปด้วย\nคงไม่มีทางเลือกอื่นละนะ ฉันจะผิดสัญญาตัวเองไม่ได้ เอมิก็ผิดสัญญาตัวเองไม่ได้เหมือนกัน"

# "I just hope the both of us are up to it."
"จึงได้แต่หวังว่าเราทั้งสองคนจะทำได้"

show bg emi_dining at center
show emicas weaksmile at twoleft
with charamove

show meiko happy at tworight
with charaenter

# emm "We're off!"
emm "ไปกันเลย!"

# "Emi's mother blows through the dining room, collects the two of us, and heads out the door at a brisk pace. Now I know where her daughter gets it from."
"แม่เอมิพุ่งตัวมารับเราสองคนที่ห้องกินข้าวแล้วเดินฉับ ๆ ออกไปที่ประตู โอเค รู้แล้วว่าเอมิได้ใครมา"

stop music fadeout 4.0

scene bg city_graveyard
with shorttimeskip

# "The car pulls up at the cemetery gates, and I feel Emi tense up beside me. I reach over and give her hand a comforting squeeze, which causes her to relax a little."
"รถมาจอดอยู่ที่ทางเข้าสุสาน เอมิที่นั่งอยู่ข้าง ๆ ตัวเกร็งขึ้นมา ฉันยื่นมือไปบีบมือเธอไว้เบา ๆ จนเธอผ่อนคลายลงบ้าง"

# "Emi's mother doesn't follow us, explaining that she prefers to visit the grave alone. Emi steps through the gates and looks back, as if to make sure I'm still there. We step into the cemetery."
"แม่เอมิบอกว่าจะขอไปที่หลุมศพตัวคนเดียวจึงไม่ได้ตามพวกเรามาด้วย เอมิเดินผ่านประตูเข้าไปแล้วเหลียวหลัง\nคล้ายดูให้แน่ใจว่าฉันยังอยู่ เราเดินเข้ามาด้านในสุสาน"

# "I don't feel comfortable in cemeteries. Gravestones litter the ground, each one serving as a reminder that someone used to be alive and is no longer."
"ฉันอึดอัดเมื่อเข้ามาอยู่ในสุสาน หลุมศพมากมายเรียงรายเต็มพื้นที่ แต่ละหลุมเป็นสิ่งเตือนใจว่ามีคนที่เคยมีชีวิตอยู่\nและได้ตายไปแล้ว"

# "How many died young? How many were as old as I am now? When do I wind up with a marker of my own? How much longer do I have left?"
"กี่คนที่ต้องตายตั้งแต่อายุยังน้อย กี่คนที่ตายตอนอายุเท่าฉัน เมื่อไหร่ฉันจะมีป้ายหน้าหลุมศพเป็นของตัวเองบ้าง\nฉันเหลือเวลาให้ใช้ชีวิตได้อีกนานเท่าไหร่"

# "The concept of not waking up, not seeing Emi any more, is not a happy one. It frightens me, and I very nearly turn around and exit right then and there."
"แค่คิดว่าจะไม่ได้ลืมตาตื่นขึ้นมาพบกับเอมิอีกฉันก็หดหู่ ฉันกลัวขึ้นมาจนเกือบจะหมุนตัวเดินออกจากสุสานไปเสีย\nเดี๋ยวนั้น"

# "I don't want to go among dead people, I don't want to see their stones and think about who they were or what they could have been if they'd only had more time."
"ฉันไม่อยากอยู่กลางหมู่คนตาย ฉันไม่อยากเห็นป้ายแต่ละอันแล้วคิดว่าแต่ละคนเป็นใคร และถ้ายังไม่ตายแล้ว\nในอนาคตจะไปต่อทางไหนได้อีก"

# "Then I look at the girl next to me, and my resolve returns. Emi's striding purposefully down the path, eyes clear, setting a pace that's very nearly a jog. The sooner we get there, I suspect she thinks, the better."
"แต่เมื่อมองเด็กสาวที่อยู่ข้างฉันแล้วใจก็กลับมาแน่วแน่อีกครั้ง เอมิก้าวย่างไปตามทางอย่างมีจุดมุ่งหมายด้วยฝีเท้า\nที่เกือบจะเป็นการวิ่งเหยาะ ๆ ตาเธอมองตรง ฉันเดาว่าเอมิคงคิดว่ายิ่งไปถึงเร็วยิ่งดี"

show emicas weaksmile at center
with charaenter

# emi "We're here."
emi "ถึงแล้ว"

scene black
show ev emi_grave:
    truecenter
    subpixel True zoom 0.95
    easein 10.0 zoom 1.0
with whiteout

$ renpy.music.set_volume(0.4, 0.0, channel="music")
play music music_friendship fadein 1.0

# "A gravestone, wholly unremarkable in everything except for the name etched upon it. The grass has grown up around the base."
"ป้ายหลุมศพ เป็นป้ายที่เหมือน ๆ กับป้ายทุกอัน เว้นก็แต่ชื่อที่สลักไว้บนนั้น ตรงฐานมีหญ้าขึ้นปกคลุม"

# "Emi's eyes are riveted to the stone."
"ตาเอมิจับจ้องอยู่ที่ป้าย"

scene bg city_graveyard
show emicas neutral at center
with locationchange

$ renpy.music.set_volume(1.0, 20.0, channel="music")

# "After a few moments she turns around, looking surprisingly calm, yet solemn."
"ผ่านไปชั่วขณะหนึ่งเอมิก็หันมาด้วยใบหน้าที่สงบผิดคาดทว่าเคร่งขรึม"

show emicas awayfrown
with charachange

# emi "Pink's not actually my favorite color, you know."
emi "จริง ๆ แล้วฉันไม่ได้ชอบสีชมพูนะ"

# hi "Er, what?"
hi "เอ่อ อะไรนะ"

show emicas frown
with charachange

# emi "I'm warming up to it."
emi "วอร์มอัพอยู่"

# hi "Ah."
hi "อ้อ"

show emicas neutral
with charachange

# emi "People tend to think that pink's my favorite color. I think it's because I like strawberries, and even though those are red they just assume that pink's the right color for strawberries."
emi "คนชอบคิดว่าฉันชอบสีชมพู อาจจะเพราะฉันชอบสตรอว์เบอร์รี ทั้งที่สตรอว์เบอร์รีก็สีแดง แต่คนชอบคิดว่า\nสีของสตรอว์เบอร์รีคือสีชมพู"

# emi "And that it's my favorite color. But it's not. I'm too polite to tell anyone otherwise, of course, and it's not the kind of thing worth getting worried about, but I'll bet even you thought pink was my favorite color."
emi "แล้วก็คิดว่าเป็นสีที่ฉันชอบ ซึ่งไม่ใช่ แต่แน่ละว่าฉันไม่กล้าเถียงคนพวกนั้นหรอก แล้วก็ไม่ใช่เรื่องที่จะต้อง\nเก็บมาใส่ใจด้วย ฉันขอเดาว่าแม้แต่นายก็คิดว่าฉันชอบสีชมพูเหมือนกัน"

show emicas weaksmile_up
with charachange

# emi "Blue. That's my favorite color. My mom and dad are the only two who know that, and now you do too."
emi "สีฟ้า นั่นแหละสีที่ฉันชอบ มีแค่แม่กับพ่อที่รู้ แล้วตอนนี้นายก็รู้ด้วย"

# hi "Thanks for telling me, I think."
hi "ขอบคุณที่บอก นะ"

show emicas closedsmile
with charachange

# emi "You're welcome."
emi "ด้วยความยินดี"

# "There's a pause as she considers what to say next, drawing a quick breath."
"เอมิเว้นช่วงไปคิดว่าจะพูดอะไรต่อแล้วสูดหายใจสั้น ๆ"

show emicas neutral
with charachange

# emi "I can't carry a tune to save my life. I can hum, but actually singing a song is something I've never been able to do. I don't mind, because I'm not a fan of karaoke anyway."
emi "ฉันร้องเพลงเพี้ยน ฮัมเพลงได้นะ แต่ไม่เคยร้องเพลงจริง ๆ ได้เลย ซึ่งฉันก็ไม่ได้ใส่ใจเพราะไม่ได้ชอบคาราโอเกะ\nอยู่แล้ว"

# hi "Well that's one potential date idea out the window."
hi "โอเค ตัดตัวเลือกสถานที่เดตไปแล้วหนึ่ง"

show emicas frown
with charachange

# emi "People all think that I'm a really popular and friendly person, but I only have a few close friends. Probably because I keep everyone in the dark, but I think it's also because I hate the idea of losing a close friend."
emi "ทุกคนคิดว่าฉันเนื้อหอมมากและเป็นมิตรด้วย แต่ฉันมีเพื่อนสนิทไม่กี่คน อาจจะเพราะฉันไม่ยอมเล่าอะไร\nให้คนอื่นฟังเลย แต่ฉันก็คิดว่าคงเป็นเพราะฉันไม่อยากเสียเพื่อนสนิทไปด้วย"

show emicas awayfrown
with charachange

# emi "There aren't many people worth the risk."
emi "คนที่คุ้มจะเสี่ยงเป็นเพื่อนสนิทได้ด้วยน่ะมีไม่กี่คนหรอก"

show emicas frown
with charachange

# emi "I'm terrible at saying goodbye."
emi "ฉันบอกลาไม่เก่ง"

# emi "I sometimes think that I only run because it's what I used to do with my father."
emi "บางครั้งก็คิดนะว่าที่ฉันวิ่งก็เพราะการวิ่งเป็นสิ่งที่ฉันเคยทำกับพ่อเฉย ๆ"

show emicas neutral
with charachange

# emi "You're not my first boyfriend. I dated a guy for a long while during my second year at Yamaku, but in the end we broke up, because I didn't want to get closer to him. He couldn't live with that distance between us."
emi "นายไม่ใช่แฟนคนแรกของฉัน ตอนอยู่ยามากุได้สองปีฉันคบกับคนหนึ่งอยู่พักใหญ่เลย แต่สุดท้ายก็เลิกกัน\nเพราะฉันไม่อยากสนิทกับเขา เขารับไม่ได้ที่เราต้องเว้นระยะกันขนาดนั้น"

# "Her rate of speaking increases slightly, as if she's rushing towards a finish line."
"เอมิพูดเร็วขึ้นเล็กน้อยคล้ายรีบวิ่งไปให้ถึงเส้นชัย"

show emicas weaksmile
with charachange

# emi "I'm actually one year older than you. Everybody thinks I'm younger because I'm short, but I had to skip one school year because of my accident."
emi "จริง ๆ แล้วฉันแก่กว่านายหนึ่งปี ทุกคนคิดว่าฉันเด็กกว่าเพราะตัวเตี้ย แต่ฉันเรียนช้าไปหนึ่งปีเพราะเรื่องอุบัติเหตุ\nนั่นแหละ"

show emicas neutral
with charachange

# emi "They initially thought I was paralyzed when they pulled me out of the wreckage. I'd lost my legs already, but they were afraid that I wouldn't even be able to use what was left of them."
emi "ทีแรกทุกคนคิดว่าฉันเป็นอัมพาตไปแล้วตอนที่เขามาช่วยฉันออกจากซากรถ ฉันเสียขาไปแล้ว แต่เขากลัว\nว่าส่วนที่เหลืออยู่จะขยับไม่ได้อีก"

# emi "After surgery, it was clear that their initial assessment was mistaken. I couldn't feel my legs because of shock. Short term paralysis due to the other trauma I'd experienced."
emi "พอผ่าตัดเสร็จผลก็ปรากฏชัดว่าที่ทุกคนคิดไว้ทีแรกนั้นผิด ขาฉันชาเพราะความช็อก เป็นอาการอัมพาตชั่วคราว\nที่เกิดจากเหตุสะเทือนขวัญอย่างอื่นที่ฉันต้องประสบ"

# emi "My recovery was one of the fastest they'd ever seen, or so they told me. I never found out if they were serious about that or if they told that to all the patients learning to walk again."
emi "ฉันฟื้นตัวได้เร็วกว่าคนอื่น ๆ ที่หมอเคยรักษามาเลย บอกว่างั้นนะ ฉันไม่เคยได้รู้เลยว่าพูดจริงหรือพูดแบบนี้\nกับคนไข้ทุกคนที่กลับมาหัดเดินอยู่แล้ว"

show emicas awayfrown
with charachange

# emi "I…"
emi "ฉัน…"

# "She pauses, gathering herself for one last effort."
"เอมิเว้นช่วงตั้งสติรวบรวมแรงเฮือกสุดท้าย"

show emicas sad
with charachange

# emi "Eight years ago today, I lost my legs. And I lost my father as well."
emi "แปดปีที่แล้วฉันเสียขาไป และเสียพ่อไปด้วย"

# emi "He died on the way to the hospital. I didn't even get to go to the gravesite until two months later, and couldn't attend his funeral."
emi "พ่อฉันตายตอนถูกนำตัวส่งโรงพยาบาล กว่าจะได้มาเยี่ยมที่สุสานอีกทีก็อีกสองเดือนให้หลัง ฉันไม่ได้\nไปงานศพพ่อด้วยซ้ำ"

# hi "I'm so sorry."
hi "เสียใจด้วยนะ"

show emicas neutral
with charachange

# emi "Don't be. That's what everyone always says, that they're sorry. I hate hearing that. Like anyone could have done anything to change what happened."
emi "ไม่ต้องหรอก ทุกคนก็พูดแบบนั้นแหละว่าเสียใจด้วยนะ ฉันไม่อยากได้ยินคำนั้นเลย พูดเหมือนกับว่าจะช่วย\nย้อนกลับไปแก้ไขอะไรได้งั้นแหละ"

show emicas frown
with charachange

# emi "You know the best piece of advice I got? “These things happen.” I don't even remember who said it, but I guess they didn't have anything better to say."
emi "นายรู้มั้ยว่าคำแนะนำที่ดีที่สุดที่ฉันเคยได้ยินมาคืออะไร “มันก็เป็นอย่างนั้นแหละ” ฉันจำไม่ได้ด้วยซ้ำว่าใครพูด\nแต่คงไม่มีอะไรจะพูดแล้วละมั้ง"

show emicas sad
with charachange

# emi "But it's true, you know? These things happen, and there's nothing you can do about it. They aren't necessarily planned, and they aren't always bad, and they aren't always good, but they are."
emi "แต่ก็จริงนะ มันก็เป็นอย่างนั้นแหละ แล้วเราก็ทำอะไรกับมันไม่ได้ด้วย ไม่มีใครวางแผนไว้ว่ามันจะเกิด\nไม่ได้เป็นเรื่องแย่เสมอไป ไม่ได้เป็นเรื่องดีเสมอไป แต่มันเป็นอย่างนั้น"

# emi "So I made the decision that I would live without worrying about the future. And to be sure that I never had to say goodbye again, I decided I wouldn't let people get close to me any more."
emi "ฉันเลยตั้งใจว่าจะใช้ชีวิตโดยไม่ต้องไปกังวลเรื่องอนาคต แล้วก็ตั้งเป้าว่าจะไม่ต้องบอกลาอีกด้วยการไม่ให้ใคร\nเข้ามาสนิทกับฉันได้"

# emi "After all, they could be taken away at any time. And you know what?"
emi "เพราะยังไงเสียคนเหล่านั้นจะหายไปจากฉันเมื่อไหร่ก็ได้ แล้วนายรู้อะไรมั้ย"

# "She laughs, a little bitterly."
"เอมิหัวเราะขื่น ๆ"

show emicas sad_up_close
with characlose

# "Her eyes start to well up with tears, and I step forward to embrace her but she holds up a hand to stop me."
"น้ำตาเธอรื้นขึ้นมา ฉันเดินเข้าไปโอบแต่เธอก็ยกมือขึ้นมาปราม"

# emi "M'not finished."
emi "ยังพูดไม่จบ"

# "A deep breath, and she continues."
"เอมิสูดหายใจลึกแล้วพูดต่อ"

show emicas sad_close
with characlose

# emi "It worked pretty well! Until I met you and saw that you were trying to adjust to stuff here, so I thought I'd help and then you were so nice and I couldn't help it, I just…"
emi "มันได้ผลดีมาก! จนฉันได้มาเจอนายที่กำลังปรับตัวให้เข้ากับยามากุนั่นแหละ ฉันเลยอยากช่วยนาย แล้วนาย\nก็แสนดีมาก ๆ จนฉันอดใจไม่ไหว ฉัน…"

$ ksgallery_unlock("evul emi_cry_down")
show ev emi_cry_down at slow_out_tf
with whiteout

# "The tears are flowing now, and she accepts the embrace this time. The rest of her sentence is mumbled into my chest."
"น้ำตาเธอไหลริน คราวนี้เอมิยอมให้ฉันกอดแล้ว เธอพูดต่อโดยที่เสียงอู้อี้อยู่กับหน้าอกฉัน"

# emi "I tried not to fall for you, but I did. And then I tried to keep you at a distance, like with my first boyfriend, but I couldn't. But I've been so scared, because I don't want to lose you and I might anyway—"
emi "ฉันห้ามใจตัวเองไม่ให้ตกหลุมรักนาย แต่ก็ห้ามไม่อยู่ แล้วฉันก็คอยเว้นระยะกับนายเหมือนที่ทำกับแฟนคนแรก\nแต่ก็ทำไม่ลง แต่ฉันกลัวเหลือเกิน เพราะฉันไม่อยากเสียนายไป แล้วยังไงฉันก็อาจ—"

# hi "Hey, I'm still around, right? And maybe I won't be forever, but don't you think it'll be fun while it lasts? Neither of us could survive the day, there could be a bus crash or something, but so long as I know that I've been with you, I don't think it matters."
hi "ไม่สิ ฉันก็ยังอยู่ตรงนี้นี่ อาจจะไม่ได้อยู่ตลอดไป แต่อย่างน้อยตอนยังอยู่มันก็ดีนี่นา เราต่างหนีความตายไม่พ้นหรอก\nสักวันเราอาจตายตอนนั่งรถบัสแล้วเกิดอุบัติเหตุหรืออะไรประมาณนั้น แต่ขอแค่รู้ว่าเคยได้อยู่กับเธอฉันก็พอใจแล้ว"

# "A sudden thought strikes me, and I can't help laughing. My condition had me scared of dying so badly that I immediately seized on the opportunity Emi presented to improve my odds of living longer."
"อยู่ ๆ ฉันก็นึกอะไรออกแล้วอดหัวเราะไม่ได้ อาการที่ฉันเป็นทำให้ฉันกลัวตายเสียจนต้องรีบคว้าโอกาสในการยืดชีวิต\nให้อยู่ได้นานขึ้นที่เอมิยื่นมาให้"

# "But without Emi, would there have been any motivation to keep up with my running? It hits me that Emi is the reason I want to go running every day, so I can spend as much time with her as possible. Emi looks up at me, confused."
"แต่ถ้าไม่มีเอมิแล้วฉันจะยังมีแรงใจจะวิ่งอยู่หรือเปล่า แล้วฉันก็คิดได้ว่าที่อยากไปวิ่งทุกวันก็เพราะอยากใช้เวลา\nอยู่ร่วมกับเอมิให้มากที่สุด เธอเงยหน้ามองฉันงง ๆ"

# hi "We'll go on living until we stop. And when we stop living we'll be able to know that at least we've had time together, and I wouldn't have it any other way. Because I love you, Emi, and right now that's enough for me."
hi "เราจะต้องอยู่ไปจนวันตาย และพอจะตายแล้วเราก็จะได้รู้ว่าอย่างน้อยเราก็ได้ใช้เวลาอยู่ร่วมกัน ซึ่งแบบนี้แหละ\nดีที่สุดแล้วสำหรับฉัน เพราะฉันรักเธอ เอมิ สิ่งสำคัญสำหรับฉันในตอนนี้ก็มีแค่นี้แหละ"

scene bg city_graveyard
show emicas weaksmile_close at center
with locationchange

# "Emi smiles through her tears, and steps back from me."
"รอยยิ้มเอมิเปื้อนน้ำตา เธอผละตัวออกจากฉัน"

# emi "You know, it's funny."
emi "เนี่ย ตลกเหมือนกันนะ"

# hi "What is?"
hi "อะไรเหรอ"

show emicas closedsmile_close
with charachange

# emi "I thought that the best way to live in the moment was to do it alone. But now, I don't think I'd have it any other way either. I'm glad I met you, Hisao."
emi "ฉันเคยคิดว่าการอยู่กับปัจจุบันที่ดีที่สุดคือการอยู่ตัวคนเดียว แต่ตอนนี้ฉันก็รู้สึกเหมือนกันว่าแบบนี้แหละดีที่สุดแล้ว\nสำหรับฉัน ฉันดีใจจริง ๆ นะที่ได้มาพบกับนาย ฮิซาโอะ"

# hi "Well, these things happen."
hi "อืม มันก็เป็นอย่างนั้นแหละ"

# "Emi and I stay by the grave for a while, as Emi pays her respects to her father. When she's ready to go, we exit the graveyard side by side."
"ฉันยืนอยู่ตรงนั้นพักหนึ่งในขณะที่เอมิกำลังไหว้ป้ายหลุมศพอยู่ พอเอมิพร้อมไปแล้วเราก็เดินเคียงกันออกมา"

stop music fadeout 15.0


#################


label th_E31:

scene bg school_gate_ss
with shorttimeskip

# "Emi's mother drives us back to Yamaku. The trip back is very quiet."
""

show emicas neutral_close_ss
with charaenter

# "We wave goodbye as the car drives off, and I glance down at the girl leaning on my arm."
""

# hi "How are you feeling?"
hi ""

show emicas awayfrown_close_ss
with charachange

# "Emi shrugs noncommittally."
""

show emicas frown_close_ss
with charachange

# emi "I'll be fine. Come on, let's go."
emi ""

scene bg school_dormext_full_ss
with locationskip

# "We pause outside the girls' dorm and I turn to face Emi, ready to say goodbye."
""

show emicas weaksmile_close_ss
with charaenter

# emi "Why don't you come up for a while?"
emi ""

# hi "Okay."
hi ""

scene bg school_girlsdormhall_ss
with locationskip

# "The walk up to her room is in silence. I'm not sure why I supposed I'd be turned away at the door."
""

# "I guess I just assumed she'd want to be alone."
""

# "Her mom, the nurse, hell, everyone who knew the significance of today seemed to think it best to leave Emi alone."
""

# "But she took me into the graveyard with her. She told me the whole story of what happened on the day she lost her legs."
""

# "She wanted me around. The significance of this does not escape me."
""

play sound sfx_dooropen

# "Emi opens the door and steps into her room, not even bothering to invite me in, holding the door for me expectantly."
""

scene bg school_dormemi_ss at left
with locationskip

play sound sfx_doorclose

# "I step in, and the door swings shut behind me."
""

show emicas weaksmile_close_ss
with charaenter

# emi "Hey, can I ask you a favor?"
emi ""

# hi "Sure. Can't guarantee I'll do it, but…"
hi ""

show emicas closedsmile_close_ss
with charachange

# "Emi giggles and pulls me into a kiss that starts out soft but deepens into something almost desperate."
""

show emicas smile_close_ss
with charachange

# emi "Stay with me? Please?"
emi ""

# "Her voice has dropped to a whisper, the question is barely audible over the sound of my own breathing."
""

# "There's something about the way that she asks that question, the hesitancy in it, the quiet voice, that makes me think she doesn't mean tonight."
""

# "No, she means exactly what she said. “Stay with me.” Not “tonight” or “forever,” because both of us know there's no such thing as forever."
""

# "There's no time limit to her request, there's just the request."
""

# "The favor."
""

# "Can I do that?"
""

# "Can I stay with her?"
""

# hi "Of course."
hi ""

play music music_comfort fadein 4.0

show bg school_dormemi_ss at right
show emicas closedsmile_close_ss
with dissolvecharamove

# "We embrace again, Emi guiding me towards her bed, stepping backwards with care, until she sits down on the edge."
""

label th_E31h:

hide emicas
show eminude smile_close_ss
with charachange

# "She's gotten my shirt off by this point, and I've similarly lifted hers over her head, bra and all. Her shorts come off just as quickly."
""

# "With practiced ease she removes her legs and pulls me onto the side of the bed with her, my hand coming around her smooth shoulder."
""

hide eminude
with charachange

# "I cast my gaze over her face, down her neck, following the line to the swell of her breasts before I lower my head, planting kisses across her chest, listening to her breath hitch as her hand slides further and further down my chest."
""

# "As I work my way back up to her neck, I can feel her hands working at my belt, now fumbling slightly with the buckle, now unbuttoning, now unzipping, until my pants fall to the floor."
""

# "Her panties are noticeably darkened in the right place, showing that my earlier ministrations have produced some results."
""

# "I step back quickly and shuck my boxers, and move back in as Emi reaches over into a drawer on her nightstand, removing a small foil package."
""

# "She tears it open with a quick jerk of her teeth and reaches down to apply the protection, which, as always, causes me to gasp a little."
""

# "Her expression suddenly changes as she takes the view of me in."
""

show eminude evil_close_ss
with charaenter

# emi "Wait a second… Are you still in your socks?"
emi ""

# "I pause, and look down. Apparently, I am."
""

# hi "Er, yeah. Does that matter?"
hi ""

show eminude frown_close_ss
with charachange

# emi "Take 'em off, it's weird if you still have them on."
emi ""

# hi "You know, you've still got your socks on too."
hi ""

show eminude closedsmile_close_ss
with charachange

# emi "Yes, but I don't have my legs on. So it doesn't count."
emi ""

# "Unable to deny her logic and impatient to have the conversation over anyway, I quickly remove the offending items."
""

# "I'm so eager to get back at Emi that I practically jump on top of her, pushing her down playfully."
""

scene evh emi_miss_closed
with whiteout

# "Emi's giggling and squirming quickly ends, replaced by a happy sigh as I enter her. Breathing deeply as she savors the feeling, she spreads her arms to grab the sheets."
""

# "Her breath is in my ear as I begin moving, whispering words of encouragement, nipping at my neck, now at my mouth."
""

# "My hips hit the edge of the mattress, shaking the bed. A part of my brain briefly wonders if I should try to be quieter before succumbing to the waves of pleasure racing up my spine."
""

scene evh emi_miss_open
with charachange

# "Emi's stomach tenses as she grows closer to the edge, and as our bodies both begin to glisten with sweat time begins to become hazy."
""

# "The sound of my own breathing mingles with Emi's panting, and I ready myself for a final surge before surrendering to the rushing wave of climax."
""

# "Emi's body shudders, and she cries out, her fingers digging into my back as I too lose control of myself."
""

# "My back arches as I let myself go, feeling my body spasm as I orgasm."
""

label th_E31x:

scene bg school_dormemi_ss at right
with shorttimeskip

# "I collapse next to Emi, who almost immediately curls against me, smiling."
""

# "Mentally, I feel grateful that Emi keeps her nails short, otherwise I think she might have drawn blood."
""

# "I sit up briefly to dispose of the now-used condom and lay back down next to Emi, who's in turn taken care of cleaning herself off."
""

# "For a while, we lay in silence, savoring the feeling of being next to one another."
""

# "Emi is the first to speak."
""

show eminude smile_close_ss
with charaenter

# emi "Hey, Hisao."
emi ""

# hi "Hmm?"
hi ""

show eminude closedsmile_close_ss
with charachange

# emi "Thanks for coming with me today."
emi ""

# "I smile and plant a kiss on her head."
""

show eminude blush_close_ss
with charachange

# hi "Of course. My pleasure."
hi ""

show eminude closedsmile_close_ss
with charachange

# "Emi snuggles closer, and I can feel her breathing begin to slacken as she begins to drift off to sleep."
""

# "Just as she's about to fall asleep, she wakes up enough to mutter a single sentence."
""

# emi "I love you, Hisao."
emi ""

# "Then she's out like a light, leaving me feeling like I'm on top of the world."
""

# "I draw the slumbering Emi as close as possible, pull the covers over us to keep the chill off, and fall asleep as happy as I've ever been."
""

stop music fadeout 2.0

$ suppress_window_after_timeskip = True

scene black
with dissolve

##############################

label th_E32:

window hide None

scene black
with dissolve

scene bg school_dormemi
with openeye

window show

# "The morning light seems to reach further into Emi's room than it does into mine."
""

# "This results in my waking up earlier than I would have if I had gone back to my room last night, as had previously been our routine."
""

# "I did not realize it until this morning, but this is the first time we've actually spent the night together."
""

play music music_twinkle fadein 1.0

# "A small movement from my partner's still-slumbering form causes me to look to the side."
""

# "Hair splayed across her face, Emi continues to sleep peacefully curled up next to me."
""

# "It's slightly weird seeing her without her trademark twintails, but it's also a look I could get used to."
""

# "The small size of the beds here necessitates her curling up, but I'm pretty sure she would have done so anyway."
""

# "The covers are nearly over her head, and I smile as an errant strand of hair causes her nose to twitch slightly."
""

# "Unable to help myself, I draw her a little closer, a move which she seems to think is a good idea."
""

# "Her steady breath raises a trail of goosebumps on my chest, but I don't mind."
""

# "I am no longer tired, but I do not feel a need to move from my current position."
""

# "Emi's warm body in repose against mine is far too comfortable to move."
""

# "I gaze up at the ceiling and consider how it is that we got to this point. We've been close for a while, but not this close."
""

# "It seems like only yesterday that she ran into me in the hallway and after apologizing decided to take an interest in my well-being."
""

# "But that grew into something else, which I at least was not expecting."
""

# "One thing is for certain: having found Emi, I will try as hard as I can not to lose her."
""

# "My morning musing is interrupted by further movement from Emi."
""

# "Her eyes flutter open, and she seems briefly confused by my presence in her bed as well as her current state of dress, which is nonexistent."
""

scene ev emi_ending_smile
with whiteout

# "Then she smiles happily and sits up, her face looking down at me."
""

# emi "Good morning, Hisao."
emi ""

# hi "Hi. Sleep well?"
hi ""

# emi "Yeah. Yeah, I did. Exhausting day yesterday, you know?"
emi ""

# "I think back over yesterday's trip to the graveyard."
""

# hi "Yeah. Glad to hear you slept well."
hi ""

# emi "How'd you sleep?"
emi ""

# hi "Well enough, although you kept hogging the covers…"
hi ""

# "This earns me a shove and a stuck-out tongue. I chuckle, and Emi giggles a little, and we fall quiet for a while."
""

# "I soak up the feeling of how right it all seems, waking up with Emi by me, crammed into a bed made for one person."
""

# "It's something I could get used to."
""

# emi "Hey, Hisao…"
emi ""

# hi "Hmm?"
hi ""

# emi "Thanks for sticking around."
emi ""

# hi "No problem. Saved me the walk back anyway, right?"
hi ""

scene ev emi_ending_serious
with charachange

# "This draws another giggle, but then Emi's expression turns serious again."
""

# emi "No, really. I kept trying to push you away, because I thought that was the right thing to do, and you stuck around through it all."
emi ""

# emi "I haven't made any of this easy for you, but you stuck it out anyway."
emi ""

# emi "So really, I mean it. Thank you."
emi ""

scene ev emi_ending_smile
with charachange

# "She punctuates this by giving me a kiss, pulling back and looking at me with an expression of affection."
""

# "I reach up and ruffle her hair, smiling all the while. I'm stupidly lucky, I think. To have come through everything after my heart attack and to somehow have found this girl is nothing short of a miracle."
""

# hi "You're very welcome, Emi."
hi ""

# "I couldn't bear the thought of giving you up."
""

# hi "I'll even continue to stick around, if you want."
hi ""

# emi "I'd like that."
emi ""

# "That settles it, then. I don't know how long my heart will keep working, and I don't even really know what I'll do after this year is over, apart from going to university."
""

# "As long as Emi's around, I think I'll be okay. I've managed to help her, and she's managed to help me. If we keep doing that, we'll be okay, I think."
""

# emi "So, Hisao."
emi ""

# hi "Hmm?"
hi ""

scene ev emi_ending_glad
with charachange

# emi "What do you want to do today?"
emi ""

window hide

stop music fadeout 3.0

return
