label th_R1:
#some notes about how Rin's dialogue goes, should probably have written this down earlier.
#I've been playing around with different styles for her to somehow communicate her state of mind through dialogue style. Currently (and this seems to be the final solution), there are two distinct "modes"
#Whenever she's in free-form stream-of-consciousness blabbering mode, she uses awkward grammar badly and has extreme trouble with idioms, sayings and figurative speech. And she talks in short sentences. Many of them in sequence.
#otoh when she pulls herself together and becomes overtly lucid, she starts talking without contractions and uses way more words per sentence than necessary to communicate whatever might currently be swirling inside of her mind.
#these are not hard and fast rules, more like general guidelines thus legibility and smooth flow of text always overrides them. Edit as you see fit really.

window hide None

scene bg school_scienceroom
with locationchange

with Pause(1.0)

play music music_normal fadein 6.0

window show

"แปดโมงครึ่งแล้ว แต่ชั้นเรียนยังไม่เริ่ม ที่จริงคาบนี้ต้องได้เรียนฟิสิกส์ แต่ครูยังไม่โผล่มาเลย"

"รู้งี้นอนตื่นสายหน่อยดีกว่า"

play sound sfx_doorslam
with vpunch

"จู่ ๆ ประตูก็เปิดออกเสียงดังปัง มุโต้งึมงำเป็นคำทักทายยามเช้าอยู่ที่โถงทางเดิน"

show muto normal at center
with charaenter

mu "อรุณสวัสดิ์ทุกคน!"

"สภาพมุโต้เหมือนไม่ได้นอนมาเลยแม้แต่น้อย"

"หนวดก็ไม่ได้โกน ทั้งผมเผ้ารุงรังและเสื้อที่เปื้อนคราบนั้นไม่ได้ทำให้สภาพของครูดูดีนัก"

"เมื่อคืนคงสนุกกับงานอยู่เหมือนกันแหง ๆ "

show muto irritated
with charachange

mu "ขอโทษที่มาสายนะ พอดีมีเรื่องไม่คาดฝันนิดหน่อย ปกติฉันไม่ค่อยอะไรกับงานเทศกาลอย่างนี้หรอก แต่หวังว่าทุกคน\nจะสนุกกันนะ"

mu "ยังไงงานพวกนี้ก็สำคัญกับพวกเธอนี่นะ เพราะจะได้เป็นการพักผ่อนจากการเรียนด้วย"

show muto normal
with charachange

"ทั้งห้องร้องตอบเสียงต่างกันไป จากนั้นมุโต้ก็ขานชื่อแล้วเริ่มสอน"

mu "โอเค งั้น วันนี้เราจะมาเรียนเรื่องอนุภาคโฟตอน…"

hide muto
with shorttimeskip

"ไม่นานฉันก็ตกอยู่ในสภาพสะลึมสะลือไม่ต่างไปจากคนอื่น ๆ ในห้อง ปล่อยให้สิ่งที่มุโต้พล่ามนั้นลอยเข้าหูซ้ายปลิวออก\nทะลุหูขวาไป"

show muto normal at center
with charaenter

mu "เอาละ ไหนใครตอบคำถามข้อนี้ได้บ้าง"

"ครูเขียนสมการที่ดูค่อนข้างง่ายนั้นลงบนกระดาน พยายามให้นักเรียนมีส่วนร่วมด้วย"

show muto irritated
with charachange

mu "ไม่มีเลยเหรอ ตอบหน่อยสิ งั้น นากาอิ?"

"ฉันตอบไปหลังถูกเลือกต้อนให้ตอบอย่างไม่ยุติธรรม จากนั้นเขาก็ยิ้ม เป็นรอยยิ้มเป็นมิตรที่ถ้าเด็กเล็กได้เห็นแล้วคง\nช็อกจนเป็นลมล้มพับไป"

show muto smile
with charachange

mu "ถูกต้อง! เก่งมาก นากาอิ!"

"ทั้งรู้สึกสยองและเป็นเกียรติที่ครูจำชื่อได้ทั้งที่ฉันเพิ่งมาได้สัปดาห์เดียว"

"เท่าที่เห็น มุโต้จะมีปัญหากับการจำชื่อคนในห้องเอามาก ๆ แล้วเกินครึ่งก็อยู่มาแล้วตั้งแต่สมัย ม. ปลาย ปีหนึ่ง"

"ทั้งห้องเต็มไปด้วยบรรยากาศอึมทึม ทั้งนักเรียนและครูต่างดึงตัวเองให้กลับมาสภาพปกติหลังงานเทศกาล"

"สัปดาห์ที่ผ่านมาคงเล่นเอาทุกคนหัวหมุนไปเลย"

play sound sfx_normalbell

stop music fadeout 2.0

"และแล้วระฆังพักเที่ยงก็ดัง"

scene bg school_hallway3
with locationchange

play music music_running

mystery "หลีก ๆ ! เรื่องด่วน ๆ !"

"พอหันหน้าไปก็เห็นว่าคนอื่น ๆ ต่างหลีกทางให้บางคนที่พุ่งมาจากอีกฟากโถงทางเดินที่ติดกับช่องบันได"

"กว่าจะรู้สึกตัวว่าตัวเองกำลังยืนอยู่กลางทางที่พร้อมปะทะกับมนุษย์ที่พุ่งตัวมานั้นก็สายเกินไป"

"ฉันโดดหลบไปทางประตูห้องเรียน แต่โชคร้ายที่คนที่วิ่งมานั้นดันหลบไปทางเดียวกัน"

"ในเสี้ยววินาทีถัดมามีหลายความคิดที่โผล่เข้ามาในหัวตามลำดับแทบจะพร้อม ๆ กัน"

"หนึ่ง ฉันจำได้ว่าคนที่กำลังจะเข้ามาชนนั้นคือเอมิ"

"สอง ไม่รู้ทำไม แต่รู้สึกว่าการที่ถูกเอมิชนอีกครั้งนั้นเป็นเรื่องแสนธรรมดา ถ้าไม่มีความกลัวและอาการตระหนกกับ\nเหตุการณ์ตรงหน้าที่ตอบสนองไปโดยอัตโนมัติแล้วฉันคงรู้สึกสบายใจ"

"สาม เหมือนว่าเอมิจะวิ่งพลางขนกองกระดาษที่ตั้งสูงประมาณสามสิบเซนติเมตรมาด้วย"

play sound sfx_pillow
with vpunch

"เธอชนเข้ากับฉัน แต่อย่างน้อยคราวนี้ก็เฉี่ยวแขนฉันไปเท่านั้น"

show emi sad_depressed at center
with charamoveinbottom

emi "โอ๊ย… ทำไมถึงเป็นอย่างนี้ตลอดเลยนะ"

hi "แหม นั่นสิ เธอว่าเกี่ยวกับที่เธอวิ่งตามโถงทางเดินมาเหมือนโดนไฟลวกมั้ย"

show emi sad_shy
with charachange

# "She whimpers regretfully, looking like a hurt puppy. The sight makes me regret my snappish comment the very instant it emerges from my lips."
"เธอร้องหงิงเหมือนลูกหมาเจ็บ พอได้เห็นก็ทำเอารู้สึกผิดทันทีที่พูดกระแนะกระแหนไปอย่างนั้น"

show emi sad_pout
with charachange

# emi "But… I was in a hurry."
emi "แต่ว่า… ฉันรีบนี่นา"

# hi "I can tell."
hi "ดูออก"

# emi "Sorry."
emi "ขอโทษนะ"

# hi "Don't worry about it."
hi "ไม่เป็นไร ๆ"

show emi sad_shy
with charachange

# "Emi wails weakly one last time and rubs her forehead as if to expel the ache while her gaze sweeps over the hallway floor."
"เอมิร้องโอยเบา ๆ อีกครั้งพลางลูบหน้าผากคล้ายบรรเทาความเจ็บ สายตากวาดมองไปตามพื้นโถงทางเดิน"

# "As she notices her neat stack of papers spread all over the floor in one big mess, she lets out a horrified yelp."
"เธอร้องด้วยความตกใจทันทีที่เห็นกองกระดาษที่ตั้งมาอย่างดีปลิวกระจัดกระจาย"

show emi basic_shock
with charachange

# emi "Aah! The printouts! Oh no oh no, what am I going to do? Teacher will give me hell if they get dirty."
emi "อ๊า! เอกสาร! ไม่นะ ๆ เอาไงดี ถ้าทำเปื้อนแล้วครูต้องว่าแน่เลย"

# hi "They're probably fine. Let's gather them back up; it won't be a problem."
hi "ไม่น่าเป็นไรหรอก เก็บกันก่อนเถอะ ไม่เป็นไรนะ"

# "We quickly round up the papers, and Emi tries to sort the scattered pile in her hands back into the orderly stack it was."
"เรารีบเก็บกวาดกองกระดาษกัน เอมิคอยจัดกระดาษกลับมากองเป็นตั้งให้เรียบร้อยเหมือนเดิม"

show emi basic_grin
with charachange

# emi "Where are you going?"
emi "แล้วนี่นายจะไปไหน"

# hi "Nowhere in particular, I guess. Didn't want to be left alone with Mutou in the classroom. I think he has a hangover."
hi "ก็ไม่ที่ไหนละมั้ง ไม่อยากอยู่ตัวคนเดียวในห้องกับมุโต้ด้วย เหมือนจะเมาค้างมั้ง"

show emi excited_happy
with charachange

# emi "Have you eaten lunch?"
emi "กินข้าวเที่ยงยัง"

# hi "Not yet, but I'm not feeling very hungry anyway."
hi "ยัง แต่ก็ไม่ค่อยหิวเท่าไหร่"

show emi basic_confused
with charachange

# "She looks at me incredulously, as if doubting my sanity for letting such a thing out of my mouth."
"เธอมองด้วยสายตาไม่อยากเชื่อ ราวกับว่าบ้าไปแล้วที่พูดอย่างนั้น"

show emi excited_proud
with charachange

# emi "You should go to the roof! I promised Rin I would eat lunch with her. I bet she'd like company."
emi "งั้นก็มาที่ดาดฟ้าดีกว่า! ฉันสัญญากับรินไว้แล้วด้วยว่าจะกินข้าวเที่ยงด้วยกัน คงอยากได้เพื่อนกินด้วยแน่ ๆ"

# "Uh-oh. My lunches with Rin have been remarkably unsuccessful."
"เอ่อ มื้อเที่ยงของฉันกับรินไปได้ไม่สวยเสียด้วยสิ"

# "I know where this conversation is going and it's hard to not get drawn along, so I have little choice but to play ball."
"ฉันรู้ว่าบทสนทนานี้จะเป็นยังไงต่อ จะฝืนก็คงยาก ก็คงได้แต่ตามน้ำไปนั่นแหละ"

# hi "OK, I'll go pick up some bread or something first."
hi "โอเค เดี๋ยวฉันไปซื้อขนมปังหรืออะไรก่อนนะ"

show emi basic_closedgrin
with charachange

# "Emi smiles brightly before I say anything further."
"เอมิยิ้มแฉ่งก่อนฉันทันพูดอะไรต่อ"

show emi basic_grin
with charachange

# emi "No no, I'll go and deliver these super-quick, and then go buy lunch for us. And Rin, too, of course. What kind of bread do you like?"
emi "ไม่ต้อง ๆ เดี๋ยวฉันจะรีบเอาอันนี้ไปส่งให้แบบด่วนจี๋ก่อน แล้วจะไปซื้อข้าวเที่ยงให้ ของรินด้วยแหละ นายจะเอาขนมปัง\nแบบไหน"

# hi "It's fine, you really don't need to…"
hi "ไม่เป็นไรน่า เธอไม่ต้อ…"

show emi excited_proud
with charachange

# emi "Don't worry, it's all right. Consider it an apology. I'll be back before you know it!"
emi "ไม่ต้องห่วงหรอก สบายมาก ถือเสียว่าเป็นคำขอโทษก็แล้วกัน แป๊บเดียวเดี๋ยวฉันก็มาแล้ว!"

# hi "That's what I'm worried about. Don't get into another accident."
hi "นั่นแหละที่ฉันห่วง อย่าไปชนใครอีกก็แล้วกัน"

# "Emi starts walking down the hall, but since she's still talking to me, she isn't watching where she's going."
"เอมิเดินไปตามโถงทางเดิน แต่เพราะมัวแต่คุยกับฉันเลยไม่ได้มองทางข้างหน้า"

show emi basic_closedhappy
with charachange

# emi "I won't!"
emi "ไม่หรอกน่า!"

hide emi
with charaexit

stop music fadeout 4.5

# "Famous last words. She's already jogging down the stairs as she shouts that not-so-reassuring promise back to me."
"พูดงี้ทุกรายแหละ พอคำสัญญาที่ไม่ค่อยน่าไว้ใจนั้นออกจากปากแล้วเธอก็เริ่มวิ่งเหยาะ ๆ ไปตามบันได"

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_rooftop fadein 2.0

scene bg school_staircase1
with locationchange

# "Sighing quietly, I start plodding along in her wake. But instead of taking the stairs down, I climb upwards."
"ฉันถอนหายใจเบา ๆ แล้วเดินตามทางที่เธอออกไป เพียงแต่ไม่ได้เดินลงบันไดอย่างเธอ"

# "The stairwell up to the roof is unlit and just as creepy as it was before."
"บันไดที่ขึ้นมาดาดฟ้ายังคงมืดและน่ากลัวเหมือนอย่างเคย"

play sound sfx_dooropen

# "The door squeaks weakly in protest as I push it open."
"ประตูส่งเสียงแอ๊ดเบา ๆ ตามแรงที่ฉันเปิดออก"

play sound sfx_door_creak
$ renpy.music.set_volume(1.0, 0.5, channel="ambient")

#if the above doesn't work:
scene bg school_roof
with Fade(0.5, 0.0, 2.0, color="#FFF")

# "Rin is there too, like Emi said, lying on her back at the other end of the pebble-covered rooftop for some reason."
"รินก็อยู่อย่างที่เอมิบอก แต่ไม่รู้ทำไมเธอถึงนอนหงายอยู่ตรงอีกฝั่งของดาดฟ้าที่พื้นปูกรวดนี้"

# "Predicting something unnecessarily strange again, I walk to her as slowly as possible."
"ฉันย่องเข้าไปหาเธอช้า ๆ พลางทายอะไรพิลึกแปลก ๆ เรื่อยเปื่อย"

scene ev rin_roof_boredom
with locationchange

# rin "Helloooo."
rin "สวัสดี———"

# "She sounds very drowsy as she says that, stretching the end of the word with a slurred voice. Despite that, her eyes are wide open."
"เธอลากเสียงยืดยาวฟังดูง่วงงุน แต่เธอกลับลืมตากว้าง"

show hisao rin_roof
with charaenter

# "I look down at her, my shadow overlapping her face."
"ฉันก้มมองโดยที่เงาของฉันบังหน้าเธออยู่"

# hi "What are you doing?"
hi "ทำอะไรอยู่"

show ev rin_roof_doubt
with charachange

# "Rin raises an eyebrow."
"รินเลิกคิ้วขึ้น"

show ev rin_roof_nonchalant
with charachange

# rin "I thought you had a heart problem, not an eye problem."
rin "ปัญหานายอยู่ที่หัวใจไม่ใช่ตานี่"

# "She answers, challenging the rationale of my perfectly valid question without even tilting her head to look at me."
"เธอถามหาความสมเหตุสมผลจากคำถามของฉันที่ไม่ได้ผิดอะไรเลยโดยไม่แม้จะเอียงคอมามอง"

# "Rin's smartass comments are infuriating. The worst thing is that I'm not sure if she's doing it on purpose or not."
"คำพูดของรินที่เหมือนล้อทำฉันหงุดหงิด แล้วที่แย่ที่สุดคือฉันไม่แน่ใจด้วยซ้ำว่าที่พูดอย่างนั้นคือจงใจพูดหรือเปล่า"

# hi "All right, then. Let me rephrase:"
hi "ได้ งั้น ขอถามใหม่นะ"

# hi "Why are you lying on your back on the rooftop?"
hi "ทำไมเธอถึงมานอนหงายอยู่บนดาดฟ้านี้"

show ev rin_roof_boredom
with charachange

# "She gives a lazy shrug and sniffs dismissively."
"เธอยักไหล่เนือย ๆ แล้วทำเสียงฟุดฟิดไม่สนใจ"

# rin "I'm trying to experience. People probably don't do this enough."
rin "ฉันจะลองสัมผัสประสบการณ์ คนเราคงไม่ค่อยได้ทำแบบนี้กันเท่าไหร่หรอกนะ"

# hi "What exactly are you trying to experience here? I can't really tell, but there's probably a reason people don't do… whatever."
hi "แล้วเธอจะลองสัมผัสอะไร คือฉันก็ดูไม่ออกหรอก แต่ที่ไม่มีคนมา…ทำอะไรก็ช่างก็คงมีเหตุผลแหละ"

# "She's playing dodgeball with me again, answering my attempt at small talk with riddles I don't want to puzzle out."
"มาเล่นดอดจ์บอลกันอีกแล้ว ตอบกลับที่ฉันจะหาเรื่องนั่นนี่คุยด้วยปริศนาที่ฉันไม่อยากแก้เนี่ย"

# "But I don't want to ignore her, either."
"แต่ฉันก็ไม่อยากเมินเธอเหมือนกัน"

show ev rin_roof_nonchalant
with charachange

# rin "Yeah, but the reason is that everyone is too busy with their lives to pay attention to the really important things."
rin "อืม แต่เหตุผลที่ว่าก็คือทุกคนมัวแต่วุ่นวายกับชีวิตตัวเองจนลืมสิ่งที่สำคัญจริง ๆ ไปไง"

# hi "Like watching the sky?"
hi "อย่างการดูท้องฟ้าน่ะเหรอ"

show ev rin_roof_surprised
with charachange

# "She tears her gaze away from the sky and finally looks straight at me. The penetrating deepness of her eyes once she focuses them on something is startling."
"เธอละสายตาจากท้องฟ้าแล้วมองตรงมาที่ฉันสักที ความลึกล้ำในสายตาอันพุ่งตรงยามเธอจับจ้องอะไรบางอย่างนั้น\nชวนให้ตกใจ"

# rin "You know, if you were a girl I would be able to see your panties."
rin "เนี่ย ถ้านายเป็นผู้หญิง ฉันเห็นกางเกงในนายแล้วนะเนี่ย"

# hi "If I was a girl, I wouldn't come this close to anyone who tried to sneak a peek at my panties. I have that much common sense."
hi "ถ้าฉันเป็นผู้หญิง ฉันคงไม่มาเข้าใกล้คนที่จ้องจะแอบมองกางเกงในฉันหรอก ฉันก็ไม่ได้โง่ขนาดนั้น"

show ev rin_roof_boredom
with charachange

# rin "I wouldn't either, but sometimes it can't be avoided. Like now, for example."
rin "ฉันก็คงไม่ แต่บางทีมันก็เลี่ยงไม่ได้ เหมือน ตอนนี้"

show ev rin_roof_nonchalant
with charachange

# rin "To tell you the truth, I don't even really want to peek at your panties though."
rin "เอาตามจริง ฉันก็ไม่ได้อยากมองกางเกงในนายขนาดนั้นหรอก"

# rin "Underpants are the soul of a girl. You shouldn't peek at someone else's soul. Even if you are not a girl."
rin "กางเกงในน่ะคือจิตวิญญาณของผู้หญิง นายไม่ควรมองจิตวิญญาณใครนะ ต่อให้นายไม่ใช่ผู้หญิงก็เถอะ"

# hi "As a guy, I guess I can understand that. To us, they're some sort of half-mythical object that we can't quite comprehend."
hi "ในฐานที่ฉันเป็นผู้ชาย ฉันว่าฉันพอเข้าใจนะ สำหรับเราแล้ว กางเกงในน่ะเหมือนเป็นวัตถุกึ่งลึกลับบางอย่างที่พวกเรา\nไม่สามารถเข้าใจได้"

show ev rin_roof_surprised
with charachange

# rin "Yeah, that's exactly how I think about them too. What a coincidence."
rin "อืม ฉันก็คิดแบบนั้นเหมือนกันพอดี บังเอิญจัง"

# hi "It really is."
hi "นั่นสินะ"

# hi "So did you have world history in the morning class?"
hi "แล้วนี่เมื่อเช้าเธอได้เข้าคาบประวัติศาสตร์โลกหรือเปล่า"

show ev rin_roof_doubt
with charachange

# rin "I skipped class."
rin "โดด"

# hi "To do this?"
hi "มานี่อะนะ"

show ev rin_roof_boredom
with charachange

# rin "Well, I'm not actually doing what it looks like I am doing, or at least I think that what I am doing doesn't look like what I look like, but from your perspective…"
rin "ก็ จริง ๆ ฉันไม่ได้ทำอะไรอย่างที่เห็นอยู่นี่หรอก หรืออย่างน้อยฉันก็คิดว่าทำอะไรที่ไม่ได้ดูเหมือนอย่างที่เห็นอยู่\nแต่ถ้ามองจากมุมนายแล้ว…"

# extend " probably…"
extend " ก็คง…"

# rin "Yeah, I skipped class to do this."
rin "อืม ฉันโดดมานี่อะแหละ"

# hi "I guess whatever your reason is, it's as good as any."
hi "จะทำด้วยเหตุอันใดก็คงได้หมดแหละนะ"

hide hisao
with charaexit

play sound sfx_rustling

scene bg school_roof
with locationchange

# "Giving in to the tired feeling in my legs, I sit down on the roof next to Rin."
"ฉันทนเมื่อยขาไม่ไหวจึงนั่งลงกับพื้นดาดฟ้าข้าง ๆ ริน"

# "The pebbles are not the most comfortable bed in the world, but if she can stand it, then I should be able to as well."
"ก้อนกรวดไม่ได้นั่งสบายเท่าไหร่ แต่ถ้าเธอทนได้ ฉันก็คงทนได้เหมือนกัน"

# rin "What are you waiting for?"
rin "รออะไรอยู่ล่ะ"

# hi "Hmm?"
hi "หืม"

# rin "Try it."
rin "ลองทำบ้างสิ"

stop music fadeout 2.0
$ renpy.music.set_volume(0.4, 3.0, channel="ambient")

# "I bend my neck backwards to take a look where she is looking."
"ฉันแหงนหน้ามองไปยังที่ที่เธอมองอยู่"

scene bg misc_sky at Fullpan(40.0)
with locationchange

# "The silvery blue sky, dotted by herds of cloud-sheep, fills my field of vision entirely."
"ฟ้าครามส่องแสงที่ประดับด่างด้วยหมู่เมฆที่คล้ายฝูงแกะแผ่ทั่ววิสัยทัศน์"

# "While it's pretty, the view is nothing special even though the weather is fair."
"สวย แต่ภาพตรงหน้าก็ไม่ได้มีอะไรพิเศษ แม้อากาศจะดี"

# "I give a shrug, trying my best to imitate the nonchalant manner which Rin seems to have evolved to perfection, and lie down on my back."
"ฉันทำท่ายักไหล่ให้ใกล้เคียงกับท่าทีที่ไม่สนใจอะไรของรินที่เธอดูจะทำได้จนเชี่ยวชาญแล้วนอนลงกับพื้น"

# "The stones poke at my back through my thin shirt whenever I shift my weight even a little, forcing me to keep as still as possible."
"ทุกครั้งที่จะขยับตัวหินก็จะทิ่มหลังผ่านเสื้อบาง ๆ บังคับให้ฉันต้องอยู่ให้นิ่งที่สุด"

# "I try to ignore the discomfort and myself, instead concentrating on the vastness over us."
"ฉันละความสนใจจากความไม่สบายตัวและตัวเองไปยังผืนแผ่นกว้างใหญ่ที่อยู่เหนือพวกเรา"

# "Far above, the summer clouds drift soundlessly across the dome of the sky."
"มวลเมฆหน้าร้อนเคลื่อนคล้อยไปอย่างเงียบเชียบอยู่เบื้องบนกลางเวหา"

# "Neither of us has anything more to say, thus silence covers the rooftop."
"ไม่มีใครพูดอะไรอีก จึงเหลือเพียงความเงียบที่ปกคลุมดาดฟ้าแห่งนี้"

# "The subdued noises of students on their lunch break, cicadas in the trees and traffic buzzing past the school are humming pleasantly somewhere in the background."
"เสียงอู้อี้ของเหล่านักเรียนที่กำลังพักเที่ยง เสียงจักจั่นที่เกาะตามต้นไม้ และเสียงรถราที่ผ่านไปมาหน้าโรงเรียนแว่วมา\nชวนให้รื่นหูอยู่ไกล ๆ"

# hi "Listen, I had a great time yesterday."
hi "เนี่ย เมื่อวานสนุกมากเลยนะ"

# rin "Did you?"
rin "เหรอ"

# hi "Well, to be honest, no. But it was all right. It was probably the longest time I've ever sat in one place without doing anything, which is kinda impressive."
hi "เอาจริง ๆ ก็ ไม่ แต่ก็ไม่เป็นไรหรอก น่าจะเป็นครั้งแรกเลยที่นั่งได้นานขนาดนั้นโดยไม่ได้ทำอะไรสักอย่าง ซึ่งก็น่าทึ่งดี"

# "I try to make it sound as convincing as possible."
"ฉันพยายามพูดให้ฟังดูน่าเชื่อถือที่สุด"

# rin "Is that impressive?"
rin "น่าทึ่งเหรอ"

# hi "I think it is. I'm usually too restless to do anything like that."
hi "ฉันว่าน่าทึ่งนะ ปกติฉันคงไม่ใจเย็นพอมาทำอะไรอย่างนั้นหรอก"

# rin "I think I had a good time too."
rin "ฉันว่าฉันก็สนุกเหมือนกันนะ"

# "A cloud passes above us, casting its shadow on the school."
"เมฆเลื่อนผ่านเหนือพวกเราและบังเงาอยู่เหนือโรงเรียน"

# "A chill surges through me from the sudden change of sunlight to shade."
"เมื่อแสงแดดผันเปลี่ยนเป็นร่มเงาก็ทำให้ความร้อนในตัวลดฮวบ"

# "I realize that summer is not in its full bloom quite yet."
"ฉันถึงรู้สึกตัวว่าขณะนี้ฤดูร้อนยังไม่ถึงช่วงร้อนเต็มที่นัก"

# "The only measure of time passing is the slow pace of the clouds moving towards the town."
"สิ่งเดียวที่บอกเวลาที่กำลังไหลผ่านคือก้อนเมฆที่เคลื่อนที่ไปยังเมืองอย่างเชื่องช้า"

# "Stray beams of golden sunlight leak through the gaps, blinding me for a moment whenever they hit me directly in the eyes."
"แสงแดดเรืองรองหลงลอดผ่านรอยแยก ซึ่งทำให้มองอะไรไม่เห็นไปชั่วครู่ทุกครั้งที่แสงแยงเข้าตา"

# "The blue of the sky looks so unreachable."
"สีครามของท้องฟ้านั้นดูเกินเอื้อม"

# "This reminds me of the time I spent in the hospital, where I was bored out of my mind on a daily basis."
"นึกถึงตอนอยู่โรงพยาบาลที่เบื่อจนตายซากอยู่ทุกวัน"

# "Somehow, it didn't matter after a while. I learned to appreciate other things besides watching TV and gossiping with people I didn't even like."
"แต่ผ่านไปสักพักฉันก็เลิกใส่ใจ ฉันเรียนรู้ที่จะมองคุณค่าของสิ่งอื่นนอกจากการดูโทรทัศน์และซุบซิบนินทากับคนอื่น\nที่ฉันไม่ได้ชอบด้วยซ้ำ"

# "A comprehensive sensation of calmness spreads from my sight to my other senses, finally hitting my brain."
"ความสงบโดยสมบูรณ์ค่อย ๆ แผ่จากการมองเห็นไปยังประสาทสัมผัสอื่น ๆ จนสุดท้ายก็มาถึงที่สมอง"

# "An airplane zooms by, leaving two thin contrails in its wake like a pair of chalk lines drawn from one end of the sky to the other."
"เครื่องบินบินผ่านทิ้งแนวเมฆไว้ตามทางที่เคลื่อนไปมองดูคล้ายคู่เส้นชอล์กที่ลากจากแผ่นฟ้าฝั่งหนึ่งไปยังอีกฝั่ง"

# "I wonder where it is heading."
"กำลังไปที่ไหนกันนะ"

# "The low din of its engines carries all the way down to my ears, although it's barely audible over the racket from the quad."
"เสียงเครื่องยนต์ที่ครางต่ำดังมาจนถึงหูฉัน ถึงจะแทบไม่ได้ยินเพราะมีเสียงจอแจจากลานโรงเรียนดังกลบก็เถอะ"

stop ambient fadeout 8.0
$ renpy.music.set_volume(1.0, 10.0, channel="ambient")

# rin "It's nice."
rin "ดีเนอะ"

# hi "It's nice, but I don't understand why this is more important than going to class."
hi "ก็ดี แต่ไม่เข้าใจว่าทำไมมันถึงสำคัญกว่าการไปเข้าเรียน"

# rin "Isn't it good to do something you like?"
rin "ได้ทำอะไรที่ชอบนี่ไม่ดีเหรอ"

# rin "Every once in a while?"
rin "นาน ๆ ที?"

# hi "Of course, but—"
hi "ก็ใช่แหละ แต่—"

stop sound

# emi "What are you doing?"
emi "ทำอะไรอยู่"

# "Emi has snuck up on us without either noticing and is only a step away from me, holding several packages wrapped in plastic film in her arms."
"เอมิย่องเข้ามาหาโดยไม่มีใครทันสังเกต เธออยู่ห่างจากฉันไปเพียงก้าวเดียว แขนหอบของที่ห่อพลาสติกมาหลายอย่าง"

show emi excited_happy_close:
    xalign 0.5 yanchor 1.0 ypos 1.2
    easein 0.5 center
show bg misc_sky at right
with charaenter

# "She leans forwards and peeks over me, overshadowing my face almost exactly the same way I overshadowed Rin before."
"เธอโน้มตัวแล้วมองฉัน ยืนบังเงาตรงหน้าฉันเหมือนที่ฉันยืนบังเงาหน้ารินก่อนหน้านี้เป๊ะ"

# "I wonder how weird this looks, the two of us lying on our backs on the rooftop."
"จะดูประหลาดขนาดไหนกันนะ ที่มานอนหงายกันสองคนอยู่บนดาดฟ้าเนี่ย"

# hi "That's what I asked, too."
hi "ฉันก็ถามแบบนั้นเหมือนกัน"

# rin "I would be more concerned about what you are doing. If I were you, I wouldn't come that close to people who could see your panties."
rin "ฉันสิคิดมากที่เห็นเธอทำอะไรอยู่ตอนนี้ ถ้าเป็นฉันนะ ฉันจะไม่เข้าใกล้คนที่เห็นกางเกงในได้ใกล้ขนาดนั้นแน่ ๆ"

play sound sfx_pillow

show emi sad_angry_close
with vpunch

play music music_comedy fadein 0.5

# emi "Rin!"
emi "รินนี่ละก็!"

show emi sad_angry_close:
    easeout 0.5 ypos 1.2 alpha 0.0
with None

scene bg school_roof
with locationchange

show emi basic_hes:
    xalign 0.5 yanchor 1.0 ypos 1.1
    easein 0.5 center
with charaenter

# "Emi's voice is scandalized, but she quickly takes a step backward, pressing her hands against the front of her skirt so abruptly that the parcels of bread she was carrying fall."
"เสียงเอมินั้นฟังดูรับไม่ได้ แต่เธอก็รีบถอยทันทีก้าวหนึ่งพลางเอามือแนบหน้ากระโปรงอย่างกะทันหันจนขนมปัง\nที่เธอขนมานั้นร่วงกราว"

# "I quickly avert my eyes, and glance angrily at Rin. She pretends not to see me."
"ฉันรีบละสายตาแล้วจ้องรินด้วยความโมโห แต่เธอก็ทำเป็นไม่เห็นฉัน"

show emi basic_shock
with charachange

# emi "Hisao isn't like that, right?"
emi "ฮิซาโอะไม่ใช่คนแบบนั้นหรอก ใช่มั้ย"

# hi "Right."
hi "ใช่"

play sound sfx_rustling

show emi basic_shock:
    parallel:
        ease 0.5 ypos 1.17
    parallel:
        "emi basic_annoyed" with Dissolve(0.5, alpha=True)
    ease 0.5 ypos 1.0
with Pause(1.0)

# "Emi scowls at Rin and crouches down to pick up the packages."
"เอมิมองค้อนใส่รินแล้วย่อตัวลงเก็บของ"

play ambient sfx_rooftop fadein 8.0

show emi basic_grin_close
with characlose

show emi basic_grin_close:
    ypos 1.12
with charamove

# "She wipes the dust off them, and skips lithely around me to Rin's other side where she sets herself down."
"เธอปัด ๆ ฝุ่นออกแล้วอ้อมฉันไปอย่างพลิ้วไหวและนั่งลงข้าง ๆ ริน"

# emi "Anyway, here's your bread. Sorry it took a while."
emi "เอ้า นี่ขนมปังนาย ขอโทษที่ไปนานนะ"

# hi "That's all right. Thanks for treating me."
hi "ไม่เป็นไร ขอบคุณที่เลี้ยงนะ"

# "I pull myself up into a sitting position and gratefully accept the bread Emi is offering."
"ฉันลุกขึ้นนั่งแล้วรับขนมปังที่เอมิยื่นมาพลางขอบคุณ"

# "All three of us ravenously dig into the simple meal. The bread is surprisingly decent and readily fills my stomach."
"พวกเราทั้งสามคนกินมื้อง่าย ๆ นี้กันอย่างหิวกระหาย ขนมปังนั้นอร่อยเกินคาด ไม่นานก็เริ่มอิ่มท้อง"

show rin invis:
    yanchor 1.0 ypos 1.2 xanchor 0.5 xpos 1.0
with None

show emi basic_grin_close:
    xpos 0.3
show bg school_roof at bgleft
show rin basic_awayabsent_close:
    ease 1.0 ypos 1.07 xpos 0.9
with dissolvecharamove

# "I follow from the corner of my eye the skill with which Rin handles her bread between her feet."
"ฉันเหลือบมองไปทางรินที่ใช้เท้าจัดการกับขนมปังด้วยทักษะของเธอ"

show emi excited_proud_close
with charachange

# emi "I haven't seen you on the track in a few days."
emi "ฉันไม่เห็นนายไปวิ่งที่ลู่สักพักแล้วนะ"

show rin basic_absent_close:
    ypos 1.07 xpos 0.9
with charachange

# hi "Oh. Right, I… figured it was too heavy a routine for me to start with."
hi "อ้อ อืม คือฉัน… คิดว่าคงหนักไปหน่อยน่ะ"

show rin basic_awayabsent_close
show emi basic_hes_close
with charachange

# emi "So you've been doing something else?"
emi "แล้วนายได้หาอย่างอื่นทำมั้ย"

show rin basic_absent_close
with charachange

# hi "I've been considering my options."
hi "ก็คิด ๆ อยู่"

show emi basic_annoyed_close
with charachange

# "She frowns but doesn't pursue the issue further, for which I'm thankful."
"เธอขมวดคิ้วแต่ก็ไม่ได้ซักไซ้อะไรต่อ ซึ่งก็ดีแล้ว"

# "Emi seems pretty headstrong and I wouldn't really want to get pestered by her about this on a daily basis. I have enough burdens to bear with Shizune and Misha already."
"เธอดูเป็นคนค่อนข้างรั้น ถ้าเธอจะมาตามตื๊อเรื่องนี้กับฉันทุกวันก็คงไม่ไหว แค่ภาระจากชิซูเนะและมิช่าก็เกินพอแล้ว"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

play sound sfx_warningbell
show rin basic_awayabsent_close
show emi basic_shock_close
with charachange

# "We barely finish the lunch before the bells ring, calling us back to our classrooms."
"พวกเรากินจนหมดทันก่อนระฆังดังเรียกให้กลับไปเข้าเรียนพอดี"

stop ambient fadeout 0.5
$ renpy.music.set_volume(1.0, 1.0, channel="music")

scene bg school_scienceroom
with locationskip

show misha sign_smile at center
with charaenter

# mi "Hicchan!"
mi "ฮิจัง!"

# "Misha waves at me as soon as I enter, and starts talking before I even make my way across the classroom."
"มิช่าโบกมือให้ทันทีที่ฉันเดินเข้าห้องแล้วชวนคุยก่อนฉันทันจะได้เดินไปถึงอีกฟากห้องด้วยซ้ำ"

show misha hips_smile
with charachange

# mi "How was your festival? Did you have fun?"
mi "งานเทศกาลเป็นไง สนุกมั้ย"

# hi "Umm… still somewhat undecided on that. I'd say “probably.”"
hi "เอ่อ… ยังไม่แน่ใจเท่าไหร่ เอาเป็นว่า “น่าจะ”"

# hi "Why?"
hi "ทำไมเหรอ"

show misha hips_grin
with charachange

# mi "Wahaha~, just asking, just asking!"
mi "วะฮ่าฮ่า~ แค่ถาม ๆ !"

# "Her eyes glint in a way that tell me she's not just asking. I can't even start to guess her motives, though."
"แววตาเธอบ่งบอกว่าไม่ใช่แค่ถามเปล่า แต่ฉันก็ไม่รู้อยู่ดีว่าทำไมถึงถามน่ะนะ"

hide misha
with charaexit

# "As the well-timed entrance of the English teacher prevents us from talking further, Misha falls back to plan B."
"ครูภาษาอังกฤษก็เข้ามาได้จังหวะพอดิบพอดี มิช่าหันไปใช้แผนสำรองแทน"

window hide

show misha hips_grin_close at offscreenleft
with None

show misha perky_smile_close:
    xpos 0.1 xanchor 0.5
show bg school_scienceroom at left
with charamove

# $ written_note(u"I was there all day with Shicchan! We had a lot of fun!", text_args={"color":"#FF2AAA"})
$ written_note(u"เมื่อวานเที่ยวงานเทศกาลกับชิจังทั้งวันเลย!\nสนุกมาก!", text_args={"color":"#FF2AAA"})

# $ written_note(u"Weren't you supposed to be doing work?")
$ written_note(u"ไม่ใช่ว่าต้องทำงานเหรอ")

show misha hips_grin_close
with charachange

# $ written_note(u"Don't worry! Everything went really well.", text_args={"color":"#FF2AAA"})
$ written_note(u"ไม่ต้องห่วง! ทุกอย่างราบรื่นดี", text_args={"color":"#FF2AAA"})


window show

# "I don't reply to that, and she leaves me alone after Shizune demands her attention."
"แล้วฉันก็ไม่ได้ตอบ เธอก็ปล่อยฉันไปเพราะชิซูเนะต้องการความสนใจจากเธออยู่"

stop music fadeout 12.0

show misha invis at offscreenleft
with dissolvecharamove

hide misha
show bg school_scienceroom:
    subpixel True yalign 0.0
    ease 30.0 zoom 1.1
with None

# "My own attention, on the other hand, is directed out the windows."
"ส่วนความสนใจของฉันเองนั้นเบนออกมานอกหน้าต่าง"

# "Now that I look at it from here, through the window and the foliage just outside, the sky seems smaller."
"พอมองจากตรงนี้ที่มีหน้าต่างกับใบไม้จากต้นไม้ที่อยู่ข้างนอกบังแล้วท้องฟ้าก็ดูเล็กลง"

# "I catch only small glimpses of blue; everything else is a clutter of noise right in the middle of my field of vision."
"ฉันเห็นสีฟ้าลอดมาเพียงเล็กน้อยเท่านั้น เพราะหลายสิ่งอย่างต่างบดบังทัศนวิสัย"

# "What “experience” did Rin want out of staring at the sky? Surely she's done it before. Everyone has."
"ที่รินจ้องมองท้องฟ้านั้นเธอต้องการจะ “สัมผัส” อะไรกันแน่ เธอต้องเคยทำมาก่อนแล้วแน่ ๆ ทุกคนก็เคย"

# "It's no use trying to guess her mind, but if I don't do that, then I have no excuse for not concentrating on the teacher's words."
"จะเดาความคิดเธอไปก็เปล่าประโยชน์ แต่ถ้าไม่เดา ฉันก็ไม่มีข้ออ้างที่จะไม่สนใจสิ่งที่ครูกำลังพูดอยู่"

# "I look at the scribbles appearing on the blackboard, trying to figure out their meaning with little success."
"ฉันมองตัวหนังสือยึกยือที่อยู่บนกระดานแล้วเค้นสมองนึกความหมาย แต่ก็นึกไม่ค่อยออกเท่าไหร่"

# "English really is not my favorite subject. We have a strong mutual dislike for each other."
"ภาษาอังกฤษไม่ใช่วิชาโปรดของฉันเลย พวกเราต่างเกลียดขี้หน้ากันยิ่งกว่าอะไรดี"

stop music fadeout 2.0

#********************************

label th_R2:

scene bg school_hallway3
with shorttimeskip

play music music_normal fadein 3.0
play sound sfx_normalbell

# "Thick, hot afternoon light invades the corridor, making the air feel heavy and lazy."
"แสงแดดเจิดจ้าอันร้อนแรงยามบ่ายแทรกตัวเข้ามายังโถงทางเดินจนบรรยากาศเอื่อยเฉื่อยหนักอึ้ง"

# "My body feels weighed down by it as I drag it two doors down the hallway to the art classroom."
"ฉันรู้สึกราวกับต้องแบกน้ำหนักอากาศที่ว่านั้นระหว่างที่เดินไปตามโถงทางเดินไปยังห้องศิลปะ"

# "Maybe this is part of the reason why I didn't join any clubs before: afternoons just aren't suited for activity."
"นี่คงจะเป็นเหตุผลว่าทำไมฉันถึงไม่ได้เข้าร่วมชมรมอะไรเลย เพราะช่วงบ่ายไม่ใช่เวลาเหมาะที่จะทำอะไร"

scene ev rin_artclass1
with locationchange

# "I knock on the door of the art room and open it. A girl who was possibly doing something important with the scroll of paper she's carrying turns to reckon me, and smiles in a sweet if a bit confused manner."
"ฉันเคาะประตูห้องศิลปะแล้วเปิดออก หญิงสาวที่น่าจะเอาม้วนกระดาษที่เธอถืออยู่นั้นไปทำอะไรบางอย่างที่สำคัญนั้น\nหันมามองฉันแล้วยิ้มหวานให้ด้วยความสับสนเล็กน้อย"

show ev rin_artclass2
with charachange

# "Student" "Hello…?"
thname("นักเรียน") "สวัสดี…?"

# hi "This is the art club, right?"
hi "ที่นี่ชมรมศิลปะใช่มั้ย"

# "Student" "Yep. You interested in joining?"
thname("นักเรียน") "อื้ม จะเข้าเหรอ"

# hi "Yeah. In fact, I might already have done so, but we'll see."
hi "อาฮะ ที่จริงน่าจะเข้าไปแล้ว แต่เดี๋ยวก็คงรู้"

show ev rin_artclass3
with charachange

# "I give her a weak smile, and her own widens a notch, making me feel less nervous."
"ฉันยิ้มบาง ๆ ให้เธอ เธอเองก็คลี่ยิ้มให้จนทำให้ฉันเกร็งน้อยลง"

# "Student" "Great! Have a seat, then. We'll start when the teacher gets here."
thname("นักเรียน") "เยี่ยม! งั้นก็มานั่งก่อนสิ เดี๋ยวครูมาแล้วก็จะเริ่มกิจกรรมกัน"

show ev rin_artclass4
with charachange

# "Without even scouting the room for a good spot, I walk quickly to the back of the room and settle myself on a free seat, apart from everyone else."
"ฉันไม่เสียเวลาเดินหาที่นั่งเหมาะ ๆ แล้วตรงไปยังที่นั่งว่างตรงหลังห้องที่อยู่ห่างจากทุกคนทันที"

# "A few other members are lounging in their seats, waiting for the teacher. Rin sits alone in a window seat, looking outside. She's the only person here that I know, although a guy I've never really gotten along with from my own class is here, too."
"สมาชิกคนอื่น ๆ บางส่วนก็นั่งรอครูกันอยู่ ส่วนรินนั่งมองข้างนอกอยู่ริมหน้าต่างคนเดียว เธอเป็นคนเดียวในนี้ที่ฉันรู้จัก\nถึงจะมีผู้ชายอีกคนที่เรียนห้องเดียวกันที่ฉันไม่ถูกชะตาอยู่ด้วยก็เถอะ"

# "Nobody else comes to greet me - maybe introductions are left for later? - so I just settle for silent observation as well."
"ไม่มีใครเข้ามาทักทายฉัน—เดี๋ยวแนะนำตัวอะไรอีกทีมั้ง—ฉันจึงนั่งสังเกตการณ์อยู่เงียบ ๆ ด้วยคน"

# "One boy has sunglasses on; an odd sight indoors, were we not at Yamaku. I'll bet he's the blind student Rin was talking about."
"มีผู้ชายคนหนึ่งใส่แว่นกันแดด ถ้าไม่ใช่ที่ยามากุแล้วก็คงแปลกตาเพราะอยู่ในร่ม ก็คงเป็นนักเรียนตาบอดคนนั้น\nที่รินพูดถึงนั่นแหละ"

stop music fadeout 2.0
play sound sfx_footsteps_hard fadein 0.2

scene bg school_classroomart at left
with locationchange

# "The wait proves to be extremely short."
"แต่ก็ได้รอแค่แป๊บเดียว"

stop sound
play music music_happiness fadein 2.0

show nomiya smile at center
with charaenter

# "Nomiya walks over to stand behind his desk in three long strides, then gives a smile and a flamboyant greeting."
"โนมิยะย่างสามขุมมาที่โต๊ะของเขาแล้วยิ้มทักทายอย่างเล่นใหญ่"

show nomiya veryhappy
with charachange

# no "Good afternoon, everyone!"
no "ทิวาสวัสดิ์ทุกคน!"

show nomiya talk
with charachange

# no "First things first: Hisao there is a new member, so everyone get along with him."
no "ก่อนอื่นเลย สมาชิกใหม่ตรงนั้นชื่อฮิซาโอะนะ สนิทกันไว้ด้วยละ"

# "He winks at me unsettlingly."
"เขาขยิบตาให้ชวนขนลุก"

# "All eight members of the club, including myself, answer his greeting with considerably less enthusiasm. Still, people finally straighten up in their seats and begin to pay attention."
"สมาชิกทั้งแปดคนของชมรมรวมฉันด้วยทักทายตอบด้วยความกระตือรือร้นที่น้อยกว่าพอตัว แต่ทุกคนก็เริ่มยืดตัว\nนั่งหลังตรงพร้อมหันมาให้ความสนใจแล้ว"

show nomiya smile
with charachange

# no "I think some of you still have projects to work on, so please continue with those if you like."
no "บางคนน่าจะยังมีงานที่ทำค้างไว้อยู่ ถ้าอยากทำต่อก็ทำเลยนะ"

show nomiya talk
with charachange

# no "As for the rest, I was thinking that today, we could do some rough studies."
no "ส่วนคนอื่น ฉันคิดอยู่ว่าวันนี้มาหัดวาดภาพร่างกันดีมั้ยนะ"

show nomiya veryhappy
with charachange

# no "How does that sound?"
no "ว่ายังไงล่ะ"

# "Nobody answers except with some unintelligible murmurs, which Nomiya apparently interprets as unanimous approval."
"ไม่มีคำตอบอื่นนอกจากเสียงงึมงำพึมพำที่จับใจความไม่ได้ ซึ่งเหมือนโนมิยะจะนับไปว่าเป็นเสียงตกลงโดยเอกฉันท์"

show nomiya talk
with charachange

# no "All right, then! Everyone not working on other projects, choose a partner and draw a sketch of one another."
no "เอาละ งั้น! คนที่ไม่ได้ทำงานอื่นอยู่ ให้จับคู่แล้ววาดภาพร่างของกันและกันนะ"

# no "You should be able to complete this today, but if not, we can continue it next time, or even do it again if you find it interesting."
no "วันนี้น่าจะทำกันให้เสร็จได้นะ แต่ถ้าไม่เสร็จก็ค่อยมาต่อทีหลังได้ หรือถ้าสนใจจะทำอีกก็ได้นะ"

show nomiya veryhappy
with charachange

# no "Remember to pay attention to lighting and shadow, and give it your best!"
no "อย่าลืมดูเรื่องแสงเงาด้วย แล้วก็ทำให้เต็มที่นะ!"

# "Pairing up? I feel pretty awkward about it, hardly knowing anyone here. I wish someone would ask me to be their partner."
"จับคู่เหรอ ไม่รู้จักใครเลย อึดอัดตาย ถ้ามีคนมาขอจับคู่ด้วยก็ดีสิ"

hide nomiya
with charaexit

# "People stand up and move their chairs closer together, but nobody comes to me."
"คนในห้องลุกพลางขยับเก้าอี้ไปชิดกันแล้ว แต่ไม่มีใครมาหาฉันเลย"

# "Pretty soon, everyone else has paired off. Friends team up with each other, but I'm left alone."
"ไม่นานนักทุกคนก็ได้คู่กัน คนที่เป็นเพื่อนกันต่างอยู่ด้วยกัน ส่วนฉันอยู่ตัวคนเดียว"

# "Well, there is Rin."
"ก็ ยังเหลือรินอยู่อะนะ"

show bg school_classroomart at right
with charamove

# "She's sitting in the furthest corner of the classroom, still staring out the window and seemingly uninterested in taking part in the exercise."
"เธอนั่งอยู่ที่มุมหนึ่งของห้องไกล ๆ ยังเหม่อมองไปทางหน้าต่างดูไม่สนใจจะทำกิจกรรมด้วย"

# "Since she's the only other one without a partner, I walk to her seat."
"เมื่อเห็นว่าเธอเป็นคนเดียวที่ยังไม่มีคู่ ฉันจึงเดินไปหาเธอ"

# "I can't see her face because her hair is covering most of it and she's looking away from me."
"ไม่เห็นหน้าด้วยเพราะผมบังอยู่ แล้วก็ไม่ได้มองมาทางนี้ด้วย"

# hi "Rin?"
hi "ริน?"

# "I call out to her. No response."
"ฉันเรียกเธอ แต่ก็ไม่มีเสียงตอบรับ"

# hi "Hey, want to partner up? You're the only one I know here."
hi "นี่ คู่กันมั้ย ในนี้ฉันรู้จักเธออยู่คนเดียวเนี่ย"

show rin basic_absent at center
with charaenter

# "She seems to finally acknowledge my presence, head turning like a robot as she looks to see who is addressing her."
"เธอดูจะตอบสนองกับตัวตนของฉันแล้ว หันหัวมาดูว่าใครเรียกเหมือนหุ่นยนต์"

"…"

# "Rin doesn't answer, and I don't want to repeat the question, either. I'm sure she heard it the first time."
"รินไม่ตอบ และฉันก็ไม่อยากถามย้ำเหมือนกัน ที่ถามไปเมื่อกี้คงได้ยินแล้วแหละ"

"…"

# "Why doesn't she say anything? It can't be such an awful fate to be paired up with me, can it?"
"ทำไมถึงไม่พูดอะไรเลยนะ คู่กับฉันมันคงไม่ได้แย่ขนาดนั้นหรอกมั้ง"

# "She doesn't look at my face, and instead stares directly at my chest and stomach."
"เธอไม่มองหน้าฉัน แล้วจ้องมาที่หน้าอกกับท้องแทน"

"…"

show rin basic_deadpan
with charachange

# rin "Oh, okay. Why not?"
rin "อ้อ โอเค ได้สิ"

"…"

# hi "Okay. Good. Great. I'll get the stuff for us."
hi "โอเค ดี เดี๋ยวไปเอาของให้"

hide rin
with charaexit

show bg school_classroomart at left
with charamove

# "Looking at the equipment Nomiya has prepared for today's meeting confuses me. Instead of graphite or pencils, we are apparently supposed to do ink sketches."
"พอมาเห็นอุปกรณ์ที่โนมิยะเตรียมไว้ให้สำหรับกิจกรรมวันนี้แล้วก็เป็นต้องงง เพราะเหมือนจะได้วาดภาพร่างโดยใช้หมึก\nแทนที่จะเป็นแร่แกรไฟต์หรือดินสอ"

# "I've never done anything like that before."
"ซึ่งฉันไม่เคยทำมาก่อนเลย"

# "The teacher, however, seems confident in my abilities to adapt to this medium."
"ทว่าคุณครูดูจะมั่นใจในความสามารถของฉันที่จะปรับมือให้ใช้สิ่งนี้ได้"

show nomiya veryhappy at center
with charaenter

# no "Simple!"
no "ง่าย ๆ !"

show nomiya smile
with charachange

# no "First you do the outlines in ink. You let them dry, and then you shade with the diluted ink. This is called India ink, it works like watercolors."
no "ก่อนอื่นก็ใช้หมึกร่างเส้นขอบ ทิ้งไว้ให้แห้ง แล้วก็ใช้หมึกที่จางหน่อยลงเงา อันนี้เขาเรียกหมึกอินเดียอิงค์ ใช้ได้เหมือน\nสีน้ำเลย"

show nomiya talk
with charachange

# no "If you're uncomfortable with it, use a pen instead of a brush for the outlines."
no "ถ้าไม่ถนัด ตอนร่างเส้นขอบจะใช้ปากกาแทนพู่กันก็ได้"

# hi "Got it."
hi "ครับ"

hide nomiya
with charaexit

# "I pick up paper, water cups, one pen for me, one brush for Rin and ink for both of us, then return to Rin."
"ฉันหยิบกระดาษ แก้วน้ำ ปากกาหนึ่งด้ามสำหรับฉัน พู่กันหนึ่งด้ามสำหรับริน แล้วก็หมึกสำหรับเราสองคน จากนั้น\nจึงกลับไปหาริน"

show bg school_classroomart at right
with charamove

show rin basic_absent_close:
    center
    ypos 1.1
with charaenter

# "Grabbing a vacated chair from nearby, I seat myself directly opposite her."
"ฉันคว้าเก้าอี้แถวนั้นที่ว่างอยู่มานั่งลงตรงหน้าเธอ"

show rin negative_spaciness_close
with charachange

stop music fadeout 1.0

# rin "Do you want me to do it with my foot or my mouth?"
rin "อยากให้ใช้เท้าหรือปากวาด"

# hi "What did you say?"
hi "ว่ายังไงนะ"

play music music_another fadein 2.0

show rin relaxed_surprised_close
with charachange

# "She tilts her head, her brows forming questioning arches, as if she doesn't understand that I didn't understand the question."
"เธอเอียงคอแล้วเลิกคิ้วขึ้นด้วยความสงสัยราวไม่เข้าใจว่าทำไมฉันถึงไม่เข้าใจที่เธอถาม"

show rin basic_deadpan_close
with charachange

# rin "I don't mind drawing either way. You'll look better if I do it with my foot, though."
rin "ฉันจะใช้อะไรวาดก็ได้แหละ แต่ถ้าใช้เท้าแล้วนายจะดูดีหน่อย"

# hi "With your foot, then, if it's all the same to you."
hi "งั้นเท้าก็แล้วกันถ้าเธอว่าวาดได้เหมือน ๆ กัน"

show rin basic_deadpannormal_close at center
with dissolvecharamove

# "Nodding in answer, Rin gets up from her seat and kicks off her sandals."
"เธอพยักหน้าตกลงแล้วลุกขึ้นและสะบัดรองเท้าแตะออก"

show rin basic_awayabsent_close:
    center
    ypos 1.17
with dissolvecharamove

# "In two fluid motions, she picks up the paper sheet and drops it on the floor, then snatches the brush between her toes before sitting on the floor in a weird half-crosslegged position."
"เธอใช้เท้าคีบกระดาษแล้ววางกับพื้นได้อย่างลื่นไหล จากนั้นก็คีบพู่กันไว้ก่อนจะนั่งลงกับพื้นด้วยท่ากึ่งขัดสมาธิแปลก ๆ"

# "Although I've seen her do everything with her feet already, from eating to painting, this display of dexterity is so prodigious that I just stare at her, stunned."
"ถึงจะเคยเห็นเธอใช้เท้าทำอะไร ๆ มาแล้วตั้งแต่การกินยันการวาดรูป แต่ความคล่องแคล่วที่ได้เห็นนี้ช่างน่าทึ่งจนได้แต่\nมองตาค้าง"

show rin negative_annoyed_close
with charachange

# "Rin contemplates her blank paper intently. The sharp tip of her brush hovers over the paper in anticipation."
"รินใช้สมาธิพินิจมองกระดาษเปล่า ปลายพู่กันนั้นจดอยู่กับกระดาษเตรียมลงลาย"

show rin basic_deadpancontemplation_close
with charachange

# "When she raises her head to see if I'm ready, I quickly turn my face away."
"พอเธอเงยหน้ามองว่าพร้อมหรือยังฉันก็เบือนหน้าหนีทันที"

show rin basic_deadpan_close
with charachange

# rin "I'll go first. Make a pose."
rin "ฉันจะวาดก่อน เต๊ะท่าหน่อย"

# hi "What kind of a pose?"
hi "ให้ทำท่าแบบไหน"

show rin basic_lucid_close
with charachange

# rin "It doesn't matter. That's the point. You have to make the sketch of the impression you get, not decide beforehand."
rin "ไม่สำคัญหรอก นั่นแหละที่สำคัญ เวลาร่างต้องร่างตามความรู้สึกที่ได้เห็น ไม่ใช่คิดมาก่อนแล้วร่าง"

# "I end up just sitting in my chair, my hands hanging limply between my knees."
"สุดท้ายฉันก็นั่งเอามือห้อยไว้ที่ระหว่างหัวเข่า"

show rin basic_deadpanupset_close
with charachange

# "I look at her, and she looks at me for a moment before beginning."
"ฉันมองเธอ ส่วนเธอก็มองฉันอยู่พักหนึ่งก่อนเริ่มวาด"

# "Rin's stare is piercing, but impassive, as if she were trying to absorb a part of me into her own self. I feel like I'm physically shrinking under the pressure of her gaze."
"สายตาของรินนั้นแหลมคมทว่าไร้ซึ่งอารมณ์ ราวกับว่าเธอกำลังจะดูดกลืนส่วนหนึ่งของฉันเข้าไปในตัวของเธอเอง\nฉันรู้สึกเหมือนตัวเองหดเล็กลงด้วยแรงกดดันจากสายตาของเธอ"

# "I get the feeling that for the first time since we met, Rin is actually looking at me, instead of in my general direction."
"ฉันรู้สึกว่าเมื่อครั้งที่เราได้เจอกันครั้งแรกนั้น จริง ๆ แล้วรินมองมา ‘ที่’ ฉัน ไม่ได้มองมา ‘ทาง’ ฉัน"

show rin negative_annoyed_close
with charachange

# "She sketches with confident, bold sweeps of the delicate brush, not caring about the potentially destructive consequences of an accidentally misplaced stroke."
"เธอร่างภาพด้วยความมั่นใจโดยใช้ฝีแปรงอันหนักแน่นของพู่กันอันอ่อนโยนโดยไม่สนใจเลยว่าหากลากผิดแล้ว\nจะเกิดความเสียหายอะไรขึ้นมาบ้าง"

show rin basic_absent_close at center
with dissolvecharamove

# "After she's happy with the outlines, she stands up to pose for me, stretching her back and legs."
"เมื่อร่างเส้นขอบได้จนเป็นที่พอใจแล้วเธอก็ยืนยืดหลังยืดขาให้ฉันวาดบ้าง"

show rin basic_awayabsent_close
with charachange

# "This time, she doesn't look at me. Instead, Rin lets her gaze wander around the room. I'm relieved; it's easier to stare at someone when they aren't staring back at you."
"คราวนี้เธอไม่มองมาที่ฉันแต่มองไปรอบ ๆ ห้องแทน โล่งไป จ้องคนที่ไม่ได้จ้องกลับนี่สบายใจกว่าเยอะ"

# "Even so, I find it hard to get the sketch going."
"แต่ถึงอย่างนั้นก็แทบร่างไม่ออกเลย"

# "I'm not especially artistically talented, so I'm scared my portrait will turn into something disfigured, especially when compared to my partner's skill."
"ฉันไม่ได้มีพรสวรรค์ทางด้านศิลปะเป็นพิเศษขนาดนั้น กลัวว่าภาพเหมือนนี่จะเละจนกลายเป็นอะไรไม่รู้ไป ยิ่งถ้า\nให้เทียบกับความสามารถของอีกฝ่ายแล้ว"

# "I don't want to embarrass myself too badly on the first try."
"ฉันไม่อยากให้ตัวเองต้องอับอายมากกับภาพแรกนี้"

# "Rin is not helping the process, either."
"รินก็ไม่ได้ช่วยให้วาดได้สักเท่าไหร่"

show rin negative_annoyed_close
with charachange

# "She doesn't stand still for even ten seconds; tilting her head from side to side to judge her drawing, biting at her lower lip, looking unsatisfied, and constantly shuffling around like she was on hot coals."
"เธออยู่นิ่ง ๆ ได้ไม่เคยถึงสิบวินาที เอียงคอซ้ายทีขวาทีเพื่อดูภาพวาดของเธอพลางกัดริมฝีปากดูไม่พอใจ แล้วยัง\nยุกยิกไปมาเหมือนยืนอยู่บนถ่านร้อน ๆ"

show rin basic_awayabsent_close:
    center
    ypos 1.17
with dissolvecharamove

# "I finally manage to make some headway on my sketch, and with my outlines done, we both start inking in the shadow and light."
"ภาพร่างของฉันออกมาเป็นรูปเป็นร่างบ้างแล้ว พอฉันลงเส้นร่างเสร็จพวกเราก็เริ่มใช้หมึกลงเงาและแสงกัน"

show rin basic_awayabsent_close:
    tworight
    ypos 1.17
show bg school_classroomart at center
with charamove

show nomiya smile behind rin at twoleft
with charaenter

# "Nomiya passes by, and remarks on the beginnings of our sketches."
"โนมิยะเดินผ่านแล้วทักเรื่องภาพร่างที่พวกเรากำลังเริ่มทำกันอยู่"

show nomiya veryhappy
with charachange

# no "Very good! Standing figure is easier for a beginner to get a grasp of."
no "เยี่ยมมาก! ท่ายืนนี่แหละมือใหม่วาดง่าย"

# hi "But I didn't choose the pose…"
hi "แต่ผมไม่ได้เป็นคนเลือกท่านะครับ…"

hide nomiya
with charaexit

# "I look at him and then at Rin in confusion, but he's already moving onto the next pair, and Rin seems unresponsive."
"ฉันมองไปที่คุณครูแล้วหันไปหารินด้วยความงงงวย แต่คุณครูก็เดินไปหาอีกคู่แล้ว ส่วนรินก็ไม่ตอบสนองอะไร"

show rin basic_awayabsent_close:
    center
    ypos 1.17
show bg school_classroomart at right
with charamove

# "Just like when she was painting the mural, Rin has become so engrossed with her work that it seems she has shut me, the classroom and the entire world itself out from her own little sphere of existence."
"รินก้มหน้าก้มตาตั้งใจทำงานเหมือนอย่างตอนที่เธอวาดภาพเขียนผนังนั้นจนดูเหมือนว่าเธอปิดกั้นแยกฉัน\nกับคนในห้องและทั้งโลกออกจากวงรัศมีตัวตนขนาดย่อมของเธอ"

# "Every now and then, she leans backwards, seemingly to get some perspective. Sometimes she bends forward, leaning down until her nose almost touches the paper."
"บางครั้งบางทีเธอก็เอนตัวเหมือนจะหามุมมองบางอย่าง บางทีก็โน้มตัวจนจมูกแทบแตะกระดาษ"

# "This rocking back and forth looks silly."
"พอเห็นที่โยกตัวไปมาอย่างนี้แล้วก็ตลกดี"

# "Suddenly, Rin proves she hasn't completely drifted off into a world of her own, and speaks."
"จู่ ๆ รินก็พูดขึ้นเป็นการบอกให้รู้ว่าใจเธอทั้งหมดยังไม่ได้ลอยไปอยู่ในโลกส่วนตัวของเธอ"

show rin negative_spaciness_close
with charachange

# rin "Are you having fun already?"
rin "สนุกมั้ยยัง"

# "She doesn't raise her eyes from the drawing, which is a good thing. The breaking of the silence sends a jolt of surprise through me, as if I'd been electrocuted."
"เธอยังไม่ละสายตาจากภาพวาด ซึ่งดีแล้ว เสียงที่ทำลายความเงียบนี้ทำฉันสะดุ้งโหยงราวกับโดนไฟช็อต"

# hi "I… don't know, yet. It's hard to say."
hi "ไม่… รู้สิ บอกยากแฮะ"

show rin basic_awayabsent_close
with charachange

# "I can't hear how she replies to my answer because it seems she is suddenly having a private, whispered conversation with her sketch."
"ฉันไม่ได้ยินว่าเธอตอบว่าอะไร เพราะจู่ ๆ เธอก็หันไปพูดกระซิบกระซาบกับภาพวาดตัวเองเป็นการส่วนตัว"

# "I don't understand how she can draw so well when she has the attention span of a butterfly."
"ฉันไม่เข้าใจว่าทำไมถึงวาดเก่งขนาดนี้ทั้งที่เธอสมาธิสั้นพอ ๆ กับผีเสื้อ"

# "As it seems she lost her interest, I go back to work on my drawing as well."
"เหมือนว่าเธอหมดความสนใจแล้วฉันจึงหันมาทำส่วนของตัวเองต่อ"

# "I try to add texture to Rin's hair, to somehow grasp the way the golden afternoon sun lights her bright red tousle aflame and transfer it to my paper in shades of black and gray."
"ฉันลองเติมรายละเอียดที่ผมของริน พยายามลอกแสงเรืองรองยามบ่ายที่สาดส่องผมสีแดงสดอันยุ่งเหยิงของเธอ\nลงบนกระดาษด้วยสีดำและเทา"

# "Somehow, this pen and the bottle of ink seem like such lousy, inadequate tools for the task."
"แต่ก็ดูเหมือนว่าปากกาและหมึกขวดนี้จะเป็นอุปกรณ์ที่ทำหน้าที่นั้นได้ไม่ดีเอาเสียเลย"

# "Minutes pass, but the sketch doesn't magically look any more like Rin than it did before. Her voice wakes me up from my despair."
"หลายนาทีผ่านไปภาพร่างนั้นก็ไม่ได้ดูเหมือนรินขึ้นมาอย่างมหัศจรรย์ไปกว่าเมื่อก่อนหน้านี้เลย เสียงของเธอเรียกฉัน\nให้ตื่นจากความสิ้นหวังนี้"

show rin basic_deadpannormal_close
with charachange

# rin "What about now?"
rin "แล้วตอนนี้ล่ะ"

# hi "Excuse me?"
hi "อะไรเหรอ"

show rin basic_deadpan_close
with charachange

# rin "Are you having fun already?"
rin "สนุกมั้ยยัง"

# hi "Why do you keep asking that?"
hi "ทำไมถึงเอาแต่ถามอย่างนั้นล่ะ"

show rin basic_deadpancontemplation_close
with charachange

# rin "Because it's a club, right? Clubs are meant to be fun. You joined to have fun. Are you having fun?"
rin "ก็ชมรมใช่มั้ย ชมรมมันต้องสนุก นายมาสนุก นายสนุกมั้ย"

# hi "Is it important that I'm having fun?"
hi "สำคัญด้วยเหรอว่าฉันสนุกมั้ย"

show rin basic_deadpanupset_close
with charachange

# rin "…Yes."
rin "…ใช่"

# hi "…Okay, I'm having fun."
hi "…โอเค สนุก"

show rin basic_lucid_close
with charachange

# rin "Good."
rin "ดี"

# "I wonder if I said that just to please her, or if I really meant it. I can't really decide which it was."
"ฉันนึกสงสัยว่าที่บอกไปนั้นคือเอาใจเธอหรือสนุกจริง ๆ ฉันไม่แน่ใจว่าเป็นอย่างไหน"

# "I don't hate this, though. I can honestly say that much. It's good enough for now."
"อย่างน้อยก็ไม่ได้เกลียดแหละนะ เท่านี้ก็พอแล้วละ"

stop music fadeout 2.0

scene bg school_classroomart at right
with shorttimeskip

# "As the allotted time to finish the studies quickly ticks away, I desperately try to improve my awful sketch, but it doesn't seem to get any better."
"เวลาที่ให้ทำงานนั้นหมดลงไปทุกทีอย่างรวดเร็ว ฉันพยายามสุดฝืมือเพื่อปรับปรุงภาพร่างที่ห่วยแตกนี้ให้ดีขึ้น แต่ก็\nดูจะไม่ดีขึ้นเลย"

# "I want to start again from scratch, but what would be the point? There's no time for that, either."
"อยากเริ่มวาดใหม่หมดเลย แต่จะทำไปทำไม แถมไม่มีเวลามานั่งวาดใหม่แล้วด้วย"

play music music_daily fadein 2.0

# no "Okay everyone, that's it for today! Please turn in the drawings on my desk, and I'll see you all next Monday!"
no "เอาละ ทุกคน วันนี้ก็เท่านี้นะ! ส่งงานที่โต๊ะฉันได้เลย เจอกันจันทร์หน้านะ!"

show ovl rinbyhisao:
    center
    ypos 1.5 alpha 0.0
    easein 1.0 ypos 1.0 alpha 1.0
with Pause(1.0)

# "I glance at my portrait. It doesn't exactly look like Rin. I guess you could say it portrays her, but that might be a bit generous."
"ฉันเหลือบมองรูปเหมือนของฉัน ไม่ได้เหมือนรินแบบเป๊ะ ๆ อาจจะบอกว่าแทนตัวเธอได้อยู่ แต่จะให้ว่าอย่างนั้นก็คง\nมาตรฐานต่ำไปหน่อย"

# "The nose and jaw look hideous, and the shading is terrible. Granted, it's my first attempt at drawing with ink, but it's still pretty bad."
"จมูกกับกรามก็เบี้ยว แสงเงาก็ไม่ได้เรื่อง ก็ใช่แหละว่าเพิ่งเคยวาดภาพด้วยหมึกเป็นครั้งแรก แต่ก็ดูแย่เอาการ"

# rin "That's not bad."
rin "ไม่เลวนี่"

show rin basic_deadpanamused_close behind ovl at center
with None

show ovl rinbyhisao:
    easeout 1.0 ypos 1.5 alpha 0.0
with Pause(1.0)

hide ovl
with None

# "She sneaked up behind me while I was lost in thought."
"เธอแอบเข้ามาทางด้านหลังฉันระหว่างที่ฉันเหม่อคิดไปเรื่อยอยู่"

# hi "Damn it. I was hoping I could smuggle the portrait to the teacher without you seeing it."
hi "โห่ กะจะแอบเอารูปไปส่งแบบไม่ให้เธอเห็นสักหน่อย"

show rin basic_surprised_close
with charachange

# rin "Why?"
rin "ทำไม"

# hi "I'm not really happy with it. I wish I could draw better."
hi "ก็ฉันไม่ค่อยพอใจเท่าไหร่น่ะสิ ถ้าวาดเก่งกว่านี้ก็ดีสิ"

show rin basic_deadpannormal_close
with charachange

# rin "You just need some practice. Could you take my drawing to the teacher too?"
rin "นายก็แค่ต้องฝึกหน่อย ฝากส่งด้วยได้มั้ย"

# "Curious myself about how the sketch turned out, I peek at the picture. From the way Rin was drawing, it looked like she was really into it."
"ฉันแอบมองรูปด้วยความสงสัยว่าภาพวาดร่างนั้นเป็นยังไงบ้าง ดูจากท่าทางที่รินวาดแล้วคงตั้งใจวาดน่าดู"

show ovl hisaobyrin:
    center
    ypos 1.5 alpha 0.0
    easein 1.0 ypos 1.0 alpha 1.0
with Pause(1.0)

# "It's excellent. Somehow the seemingly arbitrary strokes come together to form an image of my face, from the shape of my chin, to the messy hair, to the somewhat gloomy expression."
"สุดยอด เส้นที่เหมือนลากมั่ว ๆ นั้นประกอบร่างขึ้นมาเป็นรูปใบหน้าฉัน ตั้งแต่รูปคาง ผมยุ่ง ๆ ยันสีหน้าหม่น ๆ"

label th_choiceR2:
menu:
    with menueffect

    # "Her sketch blows my mind."
    "ได้เห็นรูปแล้วทึ่งเลย"

    # "You're amazing!":
    "เก่งจัง!":
        return m1

    # "I wish I was as good as you.":
    "อยากเก่งแบบเธอบ้างจัง":
        return m2

label th_R2a:

# hi "Wow, you're amazing."
hi "โห เก่งจัง"

# rin "It's not that amazing."
rin "ก็ไม่ขนาดนั้นหรอก"

# rin "But thanks."
rin "แต่ก็ขอบคุณนะ"

label th_R2b:

# hi "Wow, I wish I was that good. I kind of embarrass myself."
hi "โห อยากเก่งแบบนี้บ้างจัง อายเลยนะเนี่ย"

# rin "Wouldn't you have to be me to be as good as me? I don't think you'd want to be me."
rin "ถ้าจะให้เก่งแบบฉันก็ต้องเป็นฉันก่อนหรือเปล่า ฉันว่านายคงไม่อยากเป็นอย่างฉันหรอก"

# hi "No, I guess not. Maybe just some sort of approximation then."
hi "ก็คงไม่ละนะ อาจจะเอาแบบใกล้เคียงก็ได้"

label th_R2c:

show ovl hisaobyrin:
    yalign 0.0 subpixel True
    easein 20.0 zoom 1.1
with None

# "I take a closer look at her work. It's still glistening with slowly drying ink."
"ฉันเพ่งมองรูปใกล้ ๆ ยังมีแสงสะท้อนจากหมึกที่กำลังแห้งอย่างช้า ๆ อยู่"

# hi "You know, I look kind of grim here."
hi "เอ้อ นี่หน้าฉันหมองนะเนี่ย"

# rin "You do look kind of grim. I mean, I agree; but it's also true otherwise, too. Like this you, not the you I made."
rin "ดูหมองจริงด้วย คือ ก็เห็นด้วยแหละ แต่มันก็จริงเหมือนกันนี่ แบบนายตรงนี้ ไม่ใช่นายที่ฉันสร้าง"

# hi "I do?"
hi "เหรอ"

# rin "I think so at least."
rin "อย่างน้อยฉันก็คิดว่างั้นนะ"

# "Her simple statement makes me suddenly feel incredibly self-conscious. I feel like I need a mirror right now, to confirm or debunk Rin. It's a nasty feeling."
"คำพูดเรียบ ๆ ของเธอทำให้ฉันรู้สึกตัวขึ้นมาในทันทีอย่างเหลือเชื่อ อยากส่องกระจกเสียมันตอนนี้เพื่อที่จะได้ยืนยัน\nหรือโต้แย้งคำพูดของรินไป เป็นความรู้สึกที่ไม่ดีเลย"

# "Maybe it's just her. I hope it's just her, and that I don't look like that sketch to everyone."
"อาจจะมีแค่เธอที่คิดอย่างนั้น หวังว่าจะมีแค่เธอนะ หวังว่าคงไม่มีใครเห็นฉันเป็นเหมือนอย่างรูปนั้นนะ"

# "It's a good sketch, but somehow I get a really oppressive feeling from it."
"รูปก็สวยดีอยู่หรอก แต่ดูแล้วรู้สึกเหมือนมีแรงกดทับยังไงไม่รู้"

show rin basic_absent_close
with None

show ovl hisaobyrin:
    easeout 1.0 ypos 1.5 alpha 0.0
with Pause(1.0)

hide ovl
with None

# hi "I see. Anyway, it looks really good. You really are amazing."
hi "อ้อ แต่ก็สวยดีนะ เธอนี่เก่งจริง ๆ"

show rin basic_deadpandelight_close
with charachange

# rin "Thanks. I'm glad I could draw you. You are an interesting person."
rin "ขอบคุณ ฉันดีใจนะที่วาดนายได้ นายเป็นคนที่น่าสนใจดี"

# hi "You're an interesting person too, but that didn't help me much."
hi "เธอก็น่าสนใจเหมือนกันนะ แต่ก็ไม่ได้ช่วยให้วาดขึ้นมาได้มากเท่าไหร่"

# "My self-deprecation has no limits today, but Rin ignores it all. I knew that I could never compare, but to see the difference with my own eyes is quite humbling."
"วันนี้ฉันเอาแต่ว่าตัวเองไม่หยุดหย่อน แต่รินก็ไม่สนใจ ก็รู้อยู่หรอกว่าคงไม่มีวันเทียบได้ติด แต่พอมาเห็นความต่าง\nด้วยตาตัวเองแล้วฉันเป็นต้องหงอไปเลย"

show rin basic_awayabsent_close
with charachange

# rin "See, I tried to make you look like you think a lot, since you did a lot of thinking."
rin "เนี่ย ฉันตั้งใจวาดให้นายดูคิดเยอะ เพราะนายคิดเยอะ"

show rin basic_deadpanamused_close
with charachange

# rin "And yeah, I might have overdone the fed-up-with-life expression, but cynics are like that, right?"
rin "แล้วก็ อืม อาจจะใส่สีหน้าเบื่อโลกมากไปหน่อย แต่พวกขวางโลกก็เป็นอย่างนั้นกันนี่ ใช่มั้ย"

# "I want to retort something snappy, but Nomiya gives me no time to think, ushering us to the door."
"อยากหาคำอะไรแสบ ๆ มาย้อนเหลือเกิน แต่โนมิยะก็รีบรัดให้ออกห้องไปไม่ให้เวลาได้คิด"

show rin basic_deadpanamused_close at tworight
show bg school_classroomart at center
with charamove

show nomiya talk behind rin at twoleft
with charaenter

# no "Hurry up, you two!"
no "รีบไปได้แล้วพวกเธอ!"

# "While we've been chatting the rest of the club has taken their leave."
"ระหว่างที่พวกเราคุยกันอยู่คนทั้งชมรมก็ไปกันหมดแล้ว"

hide rin
with charaexit

# "I quickly pick up our drawings and take them to the teacher's desk before hurrying after Rin, who has already left the classroom."
"ฉันรีบเอารูปไปส่งที่โต๊ะครูแล้วเร่งฝีเท้าตามรินที่ออกจากห้องไปก่อนแล้ว"

stop music fadeout 4.0

#*********

label th_R3:

scene bg school_hallway3
with locationchange

# "She is not in the hallway, to my surprise. I wonder where she managed to run off to in just a few seconds. Would've been nice to talk more."
"ฉันนึกแปลกใจที่เธอไม่อยู่ที่โถงทางเดิน เพิ่งผ่านไปไม่กี่วินาทีหายไปไหนแล้ว ได้คุยต่ออีกหน่อยคงดี"

# "Well, not that I had much to say, except maybe get back at her for calling me a cynic."
"ก็ใช่ว่าจะมีอะไรคุยด้วยมากหรอก ถ้านอกจากที่ว่าจะหาเรื่องย้อนที่มาว่ากันเป็นคนขวางโลกน่ะนะ"

# "It's surprisingly late. I already got used to school ending at the same time every day, so I can feel the extra hours in my head. And my gut."
"ตอนนี้ก็เย็นมากแล้ว ในหัวรู้สึกได้ถึงเวลาที่สายกว่าปกติเพราะชินกับเวลาเลิกเรียนในทุก ๆ วันแล้ว ในท้องก็รู้สึกด้วย"

# "My growling stomach reminds me that I am absolutely ravenous. I'm so hungry that I'd dare to try anything the cafeteria staff has deemed edible."
"ท้องส่งเสียงร้องเตือนว่าฉันโหยหิวมากแล้ว ถ้าเจ้าหน้าที่โรงอาหารบอกว่าอะไรกินได้ฉันก็คงยัดเข้าปากหมด"

scene bg school_cafeteria
with locationskip

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 1.0

# "Even when I see today's delicacy, fried mystery lumps, my steely resolve doesn't fade. I stuff the dinner down without tasting it at all, which is probably for the best."
"แม้ได้เห็นอาหารของวันนี้ที่เป็นก้อนปริศนาทอดแล้วเจตจำนงของฉันยังแน่วแน่ ฉันยัดมื้อเย็นนี้ลงท้องโดยลิ้นยังไม่ทัน\nรับรสดี ซึ่งก็น่าจะดีแล้ว"

# "I don't have much homework to do, but what little I have won't get done by itself, so I stroll toward the dormitories."
"การบ้านมีไม่มาก แต่มีมากมีน้อยก็ต้องทำอยู่ดี ฉันจึงเดินมุ่งไปที่หอ"

stop ambient fadeout 0.5
scene bg school_dormhallway
with locationskip

$ renpy.music.set_volume(0.0, 2.0, channel="ambient")
play sound sfx_doorknock2

# "Preparing for the post-homework lull, I knock on Kenji's door."
"ฉันคิดหาอะไรไว้เผื่อช่วงว่างหลังทำการบ้านเสร็จจึงมาเคาะประตูห้องเคนจิ"

# "He responds from the other side, although I can't make out what he said. I try the door, but it's locked."
"เสียงเขาตอบมาจากอีกฟากประตู ถึงจะฟังไม่รู้เรื่องก็เถอะ พอจะลองเปิดประตูดูก็เห็นว่าล็อก"

show kenji neutral at Slide(0.2,0.5,0.3,0.5,1.0)
with charaenter

# "After several seconds, the locks click open and he opens the door."
"ผ่านไปหลายวินาทีเขาก็ปลดล็อกแล้วเปิดประตู"

# hi "Hi. Hey, could I borrow a book? The library was already closed after I got away from my club meeting."
hi "ไง นี่ ขอยืมหนังสือหน่อย พอดีกว่าชมรมจะเลิกห้องสมุดมันก็ปิดไปแล้วน่ะ"

show kenji tsun
with charachange

# "He is squinting even more than usual and his eyebrows are twitching nervously."
"เขาขยิบตาถี่ผิดปกติพลางขมวดคิ้วด้วยความร้อนรน"

play music music_kenji fadein 2.0

# ke "Club? That's dangerous, man. Indoctrination, groupthink, brainwashing, you name it."
ke "ชมรมเหรอ อันตรายนะเว้ย พวกย้ำสอน โลกแคบกะลาครอบ ล้างสมอง มีสารพัด"

# ke "High school clubs sow the seeds of conspiracy. Do you know how many secret societies have grown from high school clubs?"
ke "ชมรมในโรงเรียนมัธยมนี่แหละคือต้นเรื่องทฤษฎีสมคบคิดเลย นายรู้มั้ยว่าพวกสังคมใต้ดินหลายที่ก็มาจากชมรม\nในโรงเรียนมัธยมนี่แหละ"

# ke "Watch your back and don't get too deep in. You might not come back."
ke "ระวังตัวอย่าถลำไปให้มันลึกมาก นายอาจจะกลับมาไม่ได้เลยนะ"

# hi "Okay, Kenji. So, how about that book?"
hi "โอเคเคนจิ แล้วหนังสือล่ะ"

show kenji neutral
with charachange

# ke "Er, sure, but return them and don't spoil any of my books. No drinks, no food stains, no bodily fluids, capisce?"
ke "เอ้อ ได้สิ แต่เอามาคืนแล้วห้ามทำเสียด้วยนะ ห้ามให้มีคราบเครื่องดื่ม คราบอาหาร คราบของเหลวจากร่างกาย\nเข้าใจ๊"

# hi "Sure. Thanks."
hi "ได้ ขอบใจ"

show kenji invis:
    xpos 0.2
with dissolvecharamove

# "Instead of letting me in, he retreats from the door, closing it again."
"แทนที่จะให้ฉันเข้าห้องไป เขาผละตัวออกแล้วปิดประตู"

show kenji neutral at Slide(0.2,0.5,0.3,0.5,1.0)
with charachange

# "After a few seconds he returns with a stack of three thick books and hands them over to me."
"ผ่านไปชั่วอึดใจเขาก็กลับมาพร้อมกองหนังสือหนา ๆ สามเล่มแล้วยื่นให้ฉัน"

# "Opening the topmost one, a familiar emblem stamped on the copyright page greets me."
"พอเปิดเล่มที่อยู่บนสุดดูก็เห็นตราอันคุ้นตาที่ประทับไว้ตรงหน้ารายละเอียดลิขสิทธิ์หนังสือ"

# hi "Er, your books? These are from the school library."
hi "เอ่อ หนังสือนายเหรอ อันนี้มันหนังสือของห้องสมุดนี่"

show kenji happy
with charachange

# ke "They are now mine."
ke "มันเป็นของฉันแล้ว"

# hi "You stole these?"
hi "นี่นายขโมยมา?"

show kenji tsun
with charachange

# ke "What are you talking about, man? I've been liberating these from the oppressive feminist movement that controls the library."
ke "พูดอะไรเนี่ย นี่ฉันปลดปล่อยหนังสือพวกนี้ให้เป็นอิสระจากการกดขี่ของการเคลื่อนไหวสตรีนิยมอันกดขี่ที่กดทับ\nห้องสมุดอยู่นะ"

# hi "Please say “oppressive feminist movement” doesn't mean that poor librarian girl, Yuuko. She couldn't even oppress a wet towel."
hi "ได้โปรดบอกฉันทีว่า “การเคลื่อนไหวสตรีนิยมอันกดขี่” ที่ว่าไม่ได้หมายถึงบรรณารักษ์สาวอันน่าสงสารที่ชื่อยูโกะ\nคนนั้น อย่าว่าแต่แรงกดขี่เลย รายนั้นจะให้ออกแรงบิดผ้าชุ่มน้ำยังไม่ออกเลยมั้ง"

show kenji invis:
    xpos 0.2
with dissolvecharamove

hide kenji
with None

stop music fadeout 3.0

# "Kenji turns away, mumbling something I can't make out, and closes the door behind him."
"เคนจิหันหน้าหนีพึมพำอะไรสักอย่างที่จับใจความไม่ได้แล้วปิดประตูหนี"

scene bg school_dormbathroom
with locationchange

play ambient sfx_shower fadein 1.0

# "Before going to my own room, I enter the bathroom. While washing my hands, my eyes catch my reflection from the mirror above the sink."
"ฉันแวะเข้าห้องน้ำก่อนกลับห้องตัวเอง ระหว่างที่ล้างมือก็ไปสะดุดตาเข้ากับกระจกที่อยู่บนอ่างล้างหน้า"

$ ksgallery_unlock("ev hisao_mirror_800")
scene ev hisao_mirror:
    zoom 1.0 xalign 0.5 yalign 0.5 subpixel True
    ease 20.0 zoom 0.8
with locationchange

# "I try to look for the grimness Rin saw in me, but it's just the usual me inside the mirror that stares back."
"ฉันเพ่งดูว่าความหมองที่รินเห็นนั้นอยู่ตรงไหน แต่ก็เห็นแต่ตัวฉันคนเดิมที่อยู่ในกระจกที่จ้องมองกลับมา"

# "I attempt to tell myself that this is what I've always looked like, but I realize I don't remember what I looked like half a year ago."
"ฉันกล่อมตัวเองว่าหน้าฉันก็เป็นอย่างนี้มาตลอดอยู่แล้ว ทว่าฉันก็จำไม่ได้เสียแล้วว่าเมื่อหกเดือนที่แล้วหน้าตาฉัน\nเป็นอย่างไร"

stop ambient fadeout 6.0

$ suppress_window_after_timeskip = True

scene black
with Dissolve(2.0)



#********



label th_R4:

window hide None

scene black with dissolve

scene bg school_dormhisao
with openeye

window show

# "I wake up all sweaty, as if I had run a half-marathon in my sleep."
"ฉันตื่นมาเหงื่อโซมกายเหมือนไปวิ่งฮาล์ฟมาราธอนมา"

play music music_pearly fadein 5.0

# "Odd; I don't recall sleeping badly. It sends a little pang of worry through me; I wouldn't want to have my heart acting up without being able to notice it."
"แปลก ก็นอนหลับสบายดีแท้ ๆ ชักคิดมากขึ้นมาหน่อย ๆ แล้วสิ ถ้าหัวใจจะเป็นอะไรไปตอนหลับไม่รู้เรื่องนี้ไม่เอาด้วยนะ"

# "Still, apart from this odd exhaustion right after waking up, I'm feeling just fine."
"แต่นอกจากความเพลียแปลก ๆ หลังตื่นนี้แล้วก็สบายดี"

# "My mouth is like sandpaper and I have nothing to drink, so I have to go all the way to the bathroom to take my meds. On impulse, I decide to take a shower while I'm at it."
"ปากแห้งจนหยาบเป็นกระดาษทรายหมดแล้ว ไม่มีอะไรให้ดื่มด้วย ต้องถ่อไปถึงห้องน้ำเพื่อไปกินยา แล้วจู่ ๆ ก็นึก\nอยากอาบน้ำขึ้นมาจึงอาบไปด้วยเลย"

scene bg school_dormbathroom
show steam
with locationskip

play ambient sfx_shower fadein 1.0

# "While I'm in the shower, I make up my mind that this counts as morning exercise, if I properly compensate with a nice half-hour walk after school."
"ระหว่างที่อาบน้ำอยู่ก็คิดไปว่าแบบนี้คือการออกกำลังกายตอนเช้าแล้ว ถ้าเดินสักครึ่งชั่วโมงหลังเลิกเรียนด้วยแล้ว\nก็คงได้พอดี"

# "Obviously, I wouldn't want to risk possible complications by going running now. Besides, Emi will never know, and I think she's giving up on me, in any case."
"แน่นอนว่าฉันไม่อยากไปวิ่งให้เสี่ยงมีอาการอะไรอีก อีกอย่าง เอมิคงไม่รู้หรอก เธอน่าจะถอดใจไม่ยอมตื๊อฉันแล้วด้วย"

# "Walking could be nice, anyway, just to get to know the area."
"ไปเดินก็ดีเหมือนกัน ให้ชินกับละแวกนี้"

# "There's a big forest in the hills behind the school, or I could go down to the convenience store."
"มีป่าใหญ่อยู่ที่เนินตรงหลังโรงเรียนให้ไป หรือจะเดินไปร้านสะดวกซื้อก็ได้"

hide steam
with charaexit
stop ambient fadeout 1.0

# "While still dabbing the moisture off my skin, I set out to find my uniform."
"ระหว่างที่เช็ดตัวก็ควานหาชุดนักเรียนไปด้วย"

# "I quickly button up my shirt and pull on my pants before going outside."
"ฉันรีบติดกระดุมเสื้อและใส่กางเกงแล้วออกมา"

scene bg school_courtyard
with locationskip

# "Normally during this time of the year, I'd be eagerly awaiting summer vacation. Having only been at school for a little over a week, I don't really have that kind of feeling."
"ปกติทุกปีช่วงนี้ฉันจะตั้งตาคอยปิดเทอมหน้าร้อนตลอด แต่พอเพิ่งกลับมาเรียนที่โรงเรียนได้สัปดาห์เศษ ๆ\nก็แทบไม่มีความรู้สึกอย่างนั้นแล้ว"

# "I'm still savoring the school life and considering the sharp and awkward turn my life has taken. I haven't had the time to become preoccupied with getting free of it."
"ฉันยังเพลิดเพลินอยู่กับชีวิตในรั้วโรงเรียนพลางคิดถึงชีวิตที่พลิกผันได้อย่างนี้ ยังไม่มีเวลาจะมาคิดเรื่องที่จะหนี\nไปจากโรงเรียนหรอก"

# "Besides, once vacations hit, it'll be a nice surprise for me if I'm not expecting it. Especially with the end of term exams looming ahead."
"อีกอย่าง ไม่ต้องตั้งคาคอยแล้วเก็บเรื่องปิดเทอมไว้เป็นเซอร์ไพรส์ก็ดี ยิ่งใกล้สอบปลายภาคแล้วด้วย"

# "At least I don't have any catching up to do with my studies. My diligence has finally paid off."
"อย่างน้อยก็ไม่ต้องมานั่งอ่านหนังสือเรียนเพิ่มแล้ว ความขยันที่สั่งสมมาออกผลเสียที"

# "I push myself past the boys gathered in the doorway and flop into my seat."
"ฉันเบียด ๆ พวกผู้ชายที่อออยู่หน้าประตูแล้วเดินมาหย่อนตัวลงนั่งที่"

stop music fadeout 2.0

scene bg school_scienceroom
with locationskip

# "From the corner of my eye I can see Shizune and Misha pause their unavoidably animated conversation and turn almost simultaneously in my direction."
"ฉันเห็นชิซูเนะกับมิช่าชะงักภาษามือที่ต้องใช้คุยกันอย่างเลี่ยงไม่ได้อยู่ที่หางตา พวกเธอหันมาทางฉันแทบจะ\nพร้อม ๆ กัน"

# "They clearly want something from me; I can tell from the way Shizune smiles. It's too obnoxiously bright to be sincere and too calculated to be spontaneous."
"พวกเธอต้องการอะไรจากฉันแน่ ๆ เห็นชิซูเนะยิ้มก็รู้ เป็นรอยยิ้มที่ช่างเจิดจ้าเสียจนเกินกว่าจะมาจากใจจริง\nและช่างได้จังหวะเกินกว่าจะมาแบบลอย ๆ"

show shizu behind_smile at tworight
show misha perky_smile at twoleft
with charaenter

play music music_normal fadein 2.0

# mi "Good morning~!"
mi "อรุณสวัสดิ์~!"

# "Her greeting is made of one hundred percent cheer and bursting energy."
"คำทักทายของเธอเต็มไปด้วยความสดใสและพลังงานเหลือล้น"

# hi "Mornin'."
hi "รุณ"

# "I fail to put either of those into my response."
"และฉันก็ไม่สามารถที่จะตอบโดยใส่ความสดใสหรือพลังงานเหลือล้นไปได้"

show misha perky_confused
with charachange

# mi "You don't look very energetic."
mi "นายดูเพลีย ๆ นะ"

# hi "No wonder. I don't feel very energetic either. I think I didn't sleep well, but I'm not sure."
hi "ไม่แปลก ฉันก็เพลีย ๆ เหมือนกัน คงหลับไม่สนิทมั้ง ไม่แน่ใจเหมือนกัน"

show misha hips_grin_close
with vpunch

# "She slaps me in the back and grins."
"เธอตบหลังฉันแล้วยิ้มร่า"

show misha hips_smile_close
with charachange

# mi "Cheer up a bit! It's a great day~!"
mi "ร่าเริงหน่อย! วันนี้วันดีนะ~!"

show shizu basic_normal2
with charachange

# "I catch Shizune's eyes. She has a strange, focused expression on her face, but she furrows her brow a little at direct eye contact and looks away."
"ฉันสบตาเข้ากับชิซูเนะ เธอทำหน้าจดจ่อแปลก ๆ แต่พอเธอเห็นว่ามองอยู่ก็ขมวดคิ้วแล้วเบือนหน้าหนี"

show shizu adjust_happy
with charachange

# "For a moment, I think that Shizune caught a glimpse of my worries, somehow, and is pondering how to respond. But then she quickly straightens her glasses, and with them, her expression."
"แวบหนึ่งฉันคิดว่าเธอคงเห็นว่าฉันคิดมากเรื่องอะไรอยู่แล้วคิดอยู่ว่าจะตอบยังไงดี แต่แล้วเธอก็ดันแว่นพลางปรับสีหน้า"

show shizu basic_happy
with charachange

shi "…"

show misha sign_smile_close
with charachange

# mi "Anyway, we were wondering if you're still interested in that student council position, because we're going to make an offer that you can't decline~"
mi "แต่เอาเถอะ พวกเราอยากรู้ว่านายสนใจเรื่องสภานักเรียนอยู่มั้ย เพราะเราจะยื่นข้อเสนอที่นายไม่อาจปฏิเสธได้~"

# hi "Wait, what? I wasn't really interested in the first place. You're putting words in my mouth."
hi "เดี๋ยว อะไร ฉันสนใจเรื่องสภานักเรียนที่ไหน อย่ามาพูดเองเออเองอย่างนี้สิ"

show shizu adjust_smug
with charachange

shi "…"

# mi "Not as such. But, wouldn't it be nice to hang out with us every day while also being useful to your school?"
mi "ไม่ใช่อย่างนั้นสักหน่อย แต่นายจะได้อยู่กับพวกเราทุกวัน แถมเป็นประโยชน์ต่อโรงเรียนด้วย ดีออก"

# hi "Well, to tell you the truth, I… I kinda joined a club. So it'd actually be sort of hard for me to join the council too."
hi "เอ่อ อันที่จริง ฉัน… พอจะได้ชมรมแล้วน่ะ จะให้เข้าสภานักเรียนด้วยก็คงไม่ไหว"

# hi "Even if I wanted to. Which I don't, as I said."
hi "ต่อให้อยากเข้าก็คงไม่ได้ ซึ่งฉันก็ไม่ได้อยากหรอก อย่างที่บอกไปนั่นแหละ"

show shizu behind_blank
with charachange

shi "…"

show misha cross_smile_close
with charachange

# mi "Is that so? Which club is it, Hicchan~?"
mi "งั้นเหรอ แล้วชมรมที่ว่าคือชมรมอะไรล่ะฮิจัง~"

# hi "The art club."
hi "ชมรมศิลปะ"

show shizu cross_angry
with charachange

shi "…"

# "Shizune's eyes glint in a sinister way as she scowls at me. With the way she looks, I'll be expecting the art club to lose its funding before lunch break, or the art teacher to mysteriously disappear from the face of the Earth."
"แววตาชิซูเนะฉายลางร้ายจังหวะที่เธอมองค้อนมาทางฉัน เห็นแล้วก็มีความรู้สึกว่าก่อนพักเที่ยงนี้ชมรมศิลปะอาจจะ\nโดนตัดงบ หรือไม่ก็ครูศิลปะอาจจะหายจากโลกใบนี้ไปอย่างลึกลับ"

hide shizu
hide misha
with charaexit

# "Before she manages to comment, the teacher finally enters the classroom, getting Shizune and Misha off my back, and sending everyone rummaging in their bags for books and pens."
"ก่อนเธอจะทันได้พูดอะไร คุณครูก็เข้าห้องมาแล้ว ชิซูเนะและมิช่าล่าถอยไป ทุกคนต่างคุ้ยกระเป๋าหาหนังสือ\nกับปากกากัน"

# "I did join the art club, but the first meeting didn't really boost my confidence. I'm not really sure what I'm doing it for."
"ก็เข้าร่วมชมรมศิลปะแล้วแหละ แต่กิจกรรมรอบแรกไม่ได้ช่วยให้มั่นใจขึ้นมาเท่าไหร่ ไม่แน่ใจว่าจะทำไปทำไม"

# "I wish I could draw like Rin, but I don't know what I would do if I could. To what end would I use such a skill? I don't really know."
"อยากวาดได้อย่างรินบ้าง แต่วาดได้ก็ไม่รู้จะเอาไปทำอะไรอยู่ดี ทักษะอย่างนั้นจะเอาไปใช้ทำอะไรได้ ฉันก็ไม่รู้\nเหมือนกัน"

$ renpy.music.set_volume(0.5,  1.0, channel="music")

show ev hisaobird_0:
    center
    alpha 0.0 ypos 1.5
    easein 0.5 alpha 1.0 ypos 1.0
with Pause(0.5)

# "Ignoring the teacher's sleep-inducing voice, I open my notebook to an empty page and press the needle-sharp graphite tip of the pencil onto it."
"ฉันเมินเสียงกล่อมนอนของครูพลางเปิดสมุดมาหน้าว่างแล้วกดปลายไส้ดินสออันแหลมคมลงกับกระดาษ"

# "What to draw?"
"วาดอะไรดี"

# "I can't really think of anything good to draw."
"ไม่รู้จะวาดอะไร"

show ev hisaobird_1:
    center
    alpha 1.0
with charachange

# "As I hesitate and raise my hand, a meek black mark left on the previously blank paper seems aggravating."
"ฉันงอมือขึ้นมาด้วยความลังเล รอยสีดำจาง ๆ ที่ติดอยู่บนหน้ากระดาษเปล่านั้นชวนให้หงุดหงิด"

# "I can't even seem to get to the starting line, let alone get started. It's almost a physical feeling of being held back. Annoyingly, it reminds me of my failed attempt at jogging with Emi."
"อย่าว่าแต่เริ่มวาดเลย ให้ลากเส้นเริ่มยังไม่ได้ อย่างกับว่ามีแรงกดดันอยู่จนวาดไม่ออก แล้วสมองเจ้ากรรมก็พลอย\nไปคิดถึงเรื่องที่ฉันนึกจะไปวิ่งกับเอมิแต่สุดท้ายก็ล้มเลิกไป"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

show ev hisaobird_1:
    center
    easeout 0.5 alpha 0.0 ypos 1.5
show bg school_scienceroom:
    yalign 0.0
    ease 20.0 zoom 1.1
with Pause(0.5)

hide ev
with None

# "I look out of the window in desperation. Right then, a small bird takes flight from one of the cherry trees that grow everywhere on the school grounds."
"ฉันมองออกไปทางนอกหน้าต่างด้วยความสิ้นหวัง ทันใดนั้นเองก็มีนกตัวเล็ก ๆ บินออกมาจากต้นซากุระ\nที่ปลูกอยู่ทั่วโรงเรียน"

# "I can't really see it clearly, and it's not like I could tell one tiny bird from another. But I pick it as my subject anyway."
"ก็เห็นไม่ชัดหรอก แยกไม่ออกด้วยว่านกตัวเล็ก ๆ ตัวไหนเป็นตัวไหนบ้าง แต่ฉันก็เอามาวาดอยู่ดี"

$ renpy.music.set_volume(0.5,  1.0, channel="music")

show ev hisaobird_1:
    center
    alpha 0.0 ypos 1.5
    easein 0.5 alpha 1.0 ypos 1.0
with Pause(0.5)

show ev hisaobird_2:
    center
    alpha 1.0
with charachange

# "Conjuring up the image of a bird in my mind's eye, I turn my gaze back to the notebook and deliberately draw a thick line across the paper to get started."
"ฉันจินตนาการถึงภาพนกอยู่ในหัวแล้วหันกลับมามองที่สมุด จากนั้นจึงลากเส้นเข้ม ๆ ลงบนกระดาษเริ่มวาด"

# "It seems to be mocking me, as I can't follow up right away. Still, it's a start. Getting started is good."
"เหมือนโดนเส้นนั้นเยาะเย้ยเพราะฉันวาดต่อไม่ออก แต่อย่างน้อยก็ได้เริ่มแล้ว ก้าวแรกนั้นเป็นสิ่งที่ดี"

show ev hisaobird_3
with charachange

# "I slowly sketch the picture on the notebook page, the image in my brain becoming clearer as the drawing takes shape."
"ฉันค่อย ๆ ร่างภาพลงบนหน้าสมุด ภาพในหัวเริ่มแจ่มชัดขึ้นเมื่อภาพวาดเป็นรูปเป็นร่างขึ้นมา"

show ev hisaobird_4
with charachange

# "It's really nothing, just that nameless nothing bird on paper, but that's not important."
"ก็ไม่ใช่อะไรหรอก แค่นกนิรนามตัวนั้นที่อยู่บนหน้ากระดาษ แต่ไม่สำคัญ"

show ev hisaobird_5
with charachange

# "My hesitation fades into the background along with the teacher's voice as I continue my struggle. The feathers form a simple pattern in my mind, but on paper it's a mess of too many rough lines despite my best efforts."
"ยิ่งพยายามวาด ความลังเลก็หดหายไปพร้อมกับเสียงคุณครู แม้ลายขนนกที่อยู่ในหัวจะดูเป็นแบบง่าย ๆ และวาด\nจนสุดฝีมือแล้ว แต่พอวาดก็กลับได้แต่เส้นหยาบ ๆ หลายเส้นทับกันไปมา"

show ev hisaobird_6
with charachange

# "I realize that I don't really know what a bird's wing should look like, even if I try to think about it. I even put the pencil down and close my eyes for a moment, trying to trace the shape of a wing in my mind."
"จากนั้นก็ถึงนึกได้ว่าที่จริงฉันไม่รู้ว่าปีกนกหน้าตาเป็นยังไง ฉันถึงขั้นวางดินสอลงแล้วหลับตาอยู่ครู่หนึ่งคอยลาก\nรูปร่างปีกนกอยู่ในหัว"

show ev hisaobird_7
with charachange

# "Being this serious about it all of a sudden makes me a little frustrated."
"พออยู่ ๆ ก็จริงจังขึ้นมาอย่างนี้แล้วก็หงุดหงิดนิดหน่อย"

show ev hisaobird_8
with charachange

# "Art class in middle school was the “easy” class in between exhausting subjects like math or Japanese. But there's this other side to art, the one that you see when you don't just fool around."
"ตอนมัธยมต้น วิชาศิลปะเคยเป็นวิชา “ง่าย ๆ ” ที่มาคั่นกลางระหว่างวิชาที่ดูดพลังงานอย่างวิชาคณิตหรือภาษาญี่ปุ่น\nแต่ศิลปะยังมีด้านนี้อีกด้านหนึ่ง ด้านที่จะได้เห็นถ้าไม่ได้ทำแบบขอไปที"

show ev hisaobird_9
with charachange

# "It's almost like a completely different thing."
"อย่างกับว่าเป็นคนละเรื่องกันเลย"

stop music fadeout 0.5

# mi "Hicchan?"
mi "ฮิจัง?"

show bg school_scienceroom behind ev:
    center
    zoom 1.0
show shizu behind_blank_close behind ev at closeright
show misha cross_smile_close behind ev at closeleft
with None

show ev hisaobird_9:
    center
    easeout 0.5 alpha 0.0 ypos 1.5
with Pause(0.5)

hide ev
with None

# "I look up to see two girls staring back at me."
"พอเงยหน้าขึ้นมาก็เห็นสองสาวที่จ้องฉันอยู่"

$ renpy.music.set_volume(1.0,  0.0, channel="music")
play music music_comedy fadein 1.0

# "Misha and Shizune have carried their chairs to my desk and are now standing by my sides, looking at my drawing."
"มิช่ากับชิซูเนะลากเก้าอี้มาที่โต๊ะฉัน เธอสองคนยืนอยู่ข้าง ๆ มองรูปที่ฉันวาดอยู่"

# hi "How long have you two been there?"
hi "มาตั้งแต่เมื่อไหร่เนี่ย"

show misha hips_grin_close
with charachange

# mi "I think you need more practice."
mi "นายต้องฝึกอีกนะ"

show shizu basic_normal_close
with charachange

# "Shizune draws a few sharp signs in the air between herself and Misha."
"ชิซูเนะทำภาษามือสั้น ๆ อยู่ข้าง ๆ มิช่า"

show misha sign_smile_close
with charachange

# mi "Shicchan agrees."
mi "ชิจังก็เห็นด้วย"

# "Rin said the exact same thing yesterday, but why did it sound less condescending?"
"เมื่อวานรินก็พูดแบบนี้เหมือนกัน แต่ทำไมถึงไม่ได้ฟังดูหยามเท่ากันนะ"

# hi "You shouldn't judge before I'm finished."
hi "ยังวาดไม่เสร็จก็อย่าเพิ่งตัดสินสิ"

# hi "Besides, don't you know it's bad luck to see an unfinished piece of work?"
hi "อีกอย่าง ไม่รู้เหรอว่ามาดูงานที่ยังไม่เสร็จน่ะจะโชคร้ายนะ"

show misha cross_laugh_close
with charachange

# "Misha cracks in exuberant laughter."
"มิช่าหัวเราะร่าเริง"

show misha hips_grin_close
with charachange

# mi "What? Don't be silly~! There's no way that could be true."
mi "หา? พูดบ้า ๆ น่า~! ไม่จริงหรอก"

# hi "Whatever."
hi "เอาเหอะ"

show shizu adjust_frown_close
with charachange

# "Shizune's eyebrows furrow dangerously, and the movements of her hands become abrupt, like the slashing of a knife."
"ชิซูเนะขมวดคิ้วดูอันตราย มือของเธอขยับอย่างรวดเร็วเหมือนมีดฟัน"

show shizu behind_frown_close
with charachange

shi "…"

show misha hips_frown_close
with charachange

# mi "You should learn to take constructive criticism better."
mi "คนเขาวิจารณ์แบบมีสาระก็หัดฟังไว้บ้างสิ"

# hi "I would if you'd actually offer some."
hi "ถ้ามีสาระจริงก็ฟังอยู่หรอก"

# "I know I'm getting too defensive and that Shizune is taking advantage of it, but I can't help it."
"รู้อยู่หรอกว่าฉันพะวงมากไปจนชิซูเนะถือโอกาสเล่นงาน แต่ก็อดไม่ได้อยู่ดี"

# hi "What are you two doing here, anyway?"
hi "แล้วนี่เธอสองคนมาทำอะไรกัน"

show shizu basic_frown_close
with charachange

shi "…"

# "Misha wags her finger admonishingly at my nose."
"มิช่าส่ายนิ้วเตือนอยู่กับจมูกฉัน"

show misha sign_smile_close
with charachange

# mi "Tsk, tsk, Hicchan. Were you not listening to the teacher at all?"
mi "ชิชะ ฮิจัง นี่นายไม่ได้ฟังครูเลยเหรอ"

show shizu behind_blank_close
with charachange

shi "…"

show misha hips_smile_close
with charachange

# mi "We have a group assignment, now."
mi "ครูเขาให้ทำงานกลุ่ม"

# "I nod bleakly, and let them take the lead."
"ฉันพยักหน้าเลื่อนลอยปล่อยให้สองคนนั้นนำไป"

show misha hips_grin_close
with charachange

# mi "So, what do you think of the lesson for today?"
mi "แล้ว ที่เรียนไปวันนี้นายว่าไงบ้าง"

# hi "Not much of anything… I didn't listen to a word of it."
hi "ก็ไม่ว่าไงหรอก… พอดีไม่ได้ฟังเลย"

show misha hips_frown_close
with charachange

# "Misha slaps her forehead and shakes her head theatrically."
"มิช่าตบหน้าผากตัวเองแล้วส่ายหน้าแบบทุ่มทุนสร้าง"

# mi "What are we going to do with you, Hicchan?"
mi "จะเอายังไงกับนายดีนะฮิจัง"

# "Luckily, Shizune and Misha together are more effective than three or four normal people, so I can mostly slack on the assignment."
"โชคดีที่แค่ชิซูเนะกับมิช่าก็เทียบเท่าได้กับคนปกติสามถึงสี่คน ฉันจึงพอจะอู้งานได้"

# "I try my best to offer at least some assistance, but I end up being mostly useless."
"ก็หาเรื่องช่วยอยู่หรอก แต่สุดท้ายฉันก็ช่วยอะไรได้ไม่มาก"

stop music fadeout 2.0

scene bg school_scienceroom
with shorttimeskip

play sound sfx_normalbell

# "The teacher keeps us in class five minutes past the lunch bells, but eventually lets us off the hook."
"หมดคาบมาห้านาทีแล้วครูถึงยอมปล่อยให้ไปพักเที่ยง"

# "I quickly stuff my books into my bag while Shizune and Misha carry their chairs back to their own seats."
"ฉันรีบเก็บหนังสือใส่กระเป๋าระหว่างที่ชิซูเนะและมิช่าย้ายเก้าอี้กลับไปที่ตัวเอง"

# "The failure of a bird-drawing ends up crumpled and stuffed in my pocket as I hurry outside."
"ฉันรีบรุดออกไปพลางขยำยัดรูปวาดนกที่ล้มเหลวนั้นใส่กระเป๋ากางเกง"

stop music fadeout 2.0

scene black
with dissolve

#***************


label th_R5:

scene black
with locationchange

# "After that morning class, and throughout the week, I keep bumping into Rin."
"หลังเลิกคาบเช้าวันนั้นและตลอดทั้งสัปดาห์ ฉันบังเอิญเจอกับรินเป็นประจำ"

window hide

scene bg school_hallway3
show crowd
show rin basic_absent at center
with delayblinds

play ambient sfx_crowd_indoors fadein 2.0

window show

# rin "Hello."
rin "สวัสดี"

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

window hide
nvl clear
nvl show dissolve

play music music_daily fadein 2.0

# n "\n\nThis is somewhat natural, as our classrooms are adjacent. But rather than just cross paths in the hallway like people regularly do, we seem to pause at the sight of each other."
n "\n\nซึ่งก็คงเป็นธรรมดาเพราะห้องเรียนอยู่ใกล้กัน แต่แทนที่จะเดินสวนกันที่โถงทางเดินไปเฉย ๆ อย่างคนทั่วไป ดูเหมือน\nพวกเราจะมองหน้ากันแล้วก็ชะงักไป"

# n "We invariably end up talking a little bit, or just silently hanging out together."
n "สุดท้ายพวกเราก็คุยกันนิดหน่อยหรืออยู่ด้วยกันแบบเงียบ ๆ อยู่ร่ำไป"

# n "I think I'm getting used to being quiet in Rin's company, as it doesn't feel as awkward, any more. I am, by nature, somewhat introverted like her, so we fit together well."
n "ฉันว่าฉันพอจะชินกับการอยู่เงียบ ๆ กับรินแล้วเพราะไม่ได้รู้สึกอึดอัดเท่าแต่ก่อน แต่เดิมฉันก็เป็นคนค่อนข้างเก็บตัว\nอย่างเธออยู่แล้ว พวกเราจึงเข้ากันได้ดี"

# n "I think it's actually an anomaly for someone in this school to be so quiet. Most people here seem to love socializing."
n "ฉันว่าจริง ๆ แล้วคนในโรงเรียนนี้ที่เงียบขนาดนี้ต่างหากที่แปลกแยก เพราะคนที่นี่ส่วนใหญ่ดูจะชอบเข้าสังคม\nอยู่ด้วยกันเป็นเพื่อน"

# n "\nIt's something that I've noticed already, even though I haven't been here very long: people here talk a lot, and they talk all the time."
n "\nสิ่งที่ฉันจับสังเกตได้แม้จะยังมาอยู่ได้ไม่นานก็คือ คนที่นี่คุยกันแบบไม่มีหยุดหย่อน"

nvl clear

# n "\n\nIt's a rare case when I see someone sitting alone, just spacing out or whatever. Obviously there are people like that here, too; that Hanako girl and myself, just to name two from my own class. But overall, they are a minority."
n "\n\nนาน ๆ ทีถึงจะเห็นคนที่นั่งอยู่เหม่อ ๆ หรืออะไรก็ตามอยู่คนเดียว แน่ละว่าที่นี่ก็มีคนอย่างนั้นอยู่ อย่างห้องฉันก็มีสองคน\nคือฮานาโกะคนนั้นแล้วก็ตัวฉันเอง แต่รวม ๆ แล้วก็นับว่าเป็นส่วนน้อย"

# n "At any rate, I wouldn't exactly call what Rin and I do “socializing,” either, but it's something, at least."
n "แต่ถึงอย่างนั้น ระหว่างฉันกับรินจะใช้คำว่า “อยู่ด้วยกันเป็นเพื่อน” ก็คงไม่ถูกต้องมากนัก แต่อย่างน้อยก็มีอะไรบ้างละนะ"

# n "These occurrences themselves don't bother me, but the fact that they happen at all does."
n "ฉันไม่ได้ใส่ใจอะไรเหตุการณ์พวกนี้หรอก แต่ที่ฉันใส่ใจคือตรงประเด็นที่ว่ามันเกิดขึ้นมาได้ต่างหาก"

# n "I'd hesitate to say that we are drawn together by something, but we certainly act as if we were."
n "จะให้ว่ามีอะไรลิขิตบันดาลชักพาก็กระไรอยู่ แต่ที่แน่ ๆ คือเราทั้งคู่ก็ทำตัวเหมือนมีอะไรที่ว่าน่ะแหละ"

# n "\n\nHowever, this sense of a budding friendship is completely wrecked every time Rin opens her mouth."
n "\n\nแต่ทว่า มิตรภาพที่แตกหน่อขึ้นมาที่สัมผัสได้นี้เป็นอันต้องสลายทุกครั้งที่รินเปิดปากพูด"

nvl hide dissolve
nvl clear
window show

stop music fadeout 0.5
stop ambient fadeout 0.5

show rin basic_deadpannormal_close
with characlose

# rin "Can I listen to your heartbeat?"
rin "ขอฟังเสียงหัวใจหน่อยได้มั้ย"

play music music_rin fadein 0.5
$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 4.0

# "She says this, or something else about as outrageous, and I have to fend off whatever nonsense her mind has cooked up during the preceding class of a subject that she is not interested in."
"เธอจะพูดอย่างนี้ หรือไม่ก็อะไรที่หลุดโลกพอ ๆ กัน แล้วฉันก็ต้องรับมือกับเรื่องไร้สาระอะไรก็ตามที่สมองของเธอ\nสุดจะสรรหามาได้ก่อนเข้าเรียนคาบที่เธอไม่ได้อยากเข้าเรียน"

# "It seems Rin has taken a shine to my heart condition as some kind of an extension of her interest in the odder disabilities that people here have, and the consequences of said afflictions."
"ดูเหมือนว่ารินจะสนใจโรคหัวใจของฉันด้วยความสนใจของเธอที่มีต่อความพิการแปลก ๆ และผลจากอาการดังกล่าว\nของเหล่าผู้คนในโรงเรียนนี้"

# "As I stand in front of her for a second too long, looking as flummoxed as I am, she concludes it is necessary to further clarify her request."
"ฉันยืนงงงันประจันหน้าเธอนานไปหน่อยจนเธอคิดว่าคงต้องพูดสิ่งที่ขอไปให้ชัดกว่านี้"

show rin basic_deadpan_close
with charachange

# rin "I know I can, but I mean, will you let me?"
rin "คือฉันฟังได้แหละ แต่คือ นายจะให้ฉันฟังหรือเปล่า"

# hi "Why?"
hi "ทำไม"

show rin relaxed_doubt_close
with charachange

# rin "Do I need a reason? I'm usually pretty bad with reasons."
rin "ต้องใช้เหตุผลด้วยเหรอ ฉันเป็นคนใช้เหตุผลไม่ค่อยเก่งด้วยสิ"

# hi "Not per se, but if you want to do it, you probably do have a reason."
hi "ก็ไม่เชิงหรอก แต่ถ้าเธออยาก ก็แปลว่าเธอต้องมีเหตุผลใช่ไหมล่ะ"

show rin basic_deadpanamused_close
with charachange

# rin "That's kinda clever. You are smarter than you look."
rin "หลักแหลมใช้ได้ นายนี่ฉลาดกว่าหน้าตานายนะ"

# hi "Also, I'd rather you not. I think these things should be private."
hi "แล้วก็ อย่าดีกว่า ฉันว่าเรื่องพวกนี้ไว้เป็นส่วนตัวดีกว่า"

show rin basic_deadpandelight_close
with charachange

# rin "Private. I get it."
rin "ส่วนตัว เข้าใจละ"

# hi "I can tell you something though, if it amuses you. I'm pretty sure it will. My heartbeat does sound very weird. Because of the… you know, condition."
hi "แต่บอกอะไรให้ได้อย่างหนึ่ง ถ้าเธอสนใจ ซึ่งฉันว่าเธอสนใจอยู่แล้วแหละ เสียงหัวใจฉันเต้นจะแปลกมาก เพราะ…\nนั่นแหละ โรคนี้"

# hi "And I hear it. All the time."
hi "แล้วเสียงนั้นอยู่ในหูฉัน ตลอด"

show rin negative_spaciness_close
with charachange

# rin "So you're paranoid."
rin "ก็คือนายหลอนระแวง"

# "It's not a question, it's a statement."
"ไม่ใช่ประโยคคำถาม แต่เป็นประโยคบอกเล่า"

# hi "No, I'm not paranoid. The doctors said that abnormal attention to heartbeat is a common symptom of my… condition."
hi "เปล่า ไม่ได้หลอนระแวง หมอเขาบอกว่าการที่หมกมุ่นอยู่กับจังหวะหัวใจเต้นของตัวเองน่ะเป็นอาการที่พบได้มากกับ…\nโรคนี้"

show rin basic_deadpannormal_close
with charachange

# rin "So, for you, it's normal to be paranoid."
rin "งั้นก็แปลว่าการหลอนระแวงคือเรื่องปกติของนาย"

# "It's not a question either."
"นั่นก็ไม่ใช่ประโยคคำถาม"

# hi "One could also say that me being like this in the first place isn't normal, either, but what the heck."
hi "ที่จริงการที่ฉันเป็นอย่างนี้มันก็ไม่เรียกว่าปกติอยู่แล้วหรอก แต่อะไรเนี่ย"

# hi "Paranoia fits me fine."
hi "หลอนระแวงก็เข้ากับฉันออก"

show rin basic_lucid_close
with charachange

# rin "I don't think it's something that actually can fit anyone or anywhere."
rin "ฉันว่านั่นไม่ใช่อะไรที่จะเข้ากับใครที่ไหนได้นะ"

show rin basic_deadpan_close
with charachange

# rin "You know, I ate an orange today for breakfast."
rin "เนี่ย เช้านีี้ฉันกินส้ม"

# hi "How was it?"
hi "เป็นไง"

# "I'm vaguely proud of myself, managing to keep up with Rin's sudden change of topic."
"ฉันภูมิใจตัวเองขึ้นมาหน่อย ๆ ที่ตามรินที่เปลี่ยนเรื่องแบบกะทันหันทัน"

show rin basic_amused_close
with charachange

# rin "Excellent. I don't remember when I last ate an orange. Because it's annoying to peel one."
rin "เยี่ยมเลย ฉันจำไม่ได้แล้วว่ากินส้มครั้งล่าสุดไปเมื่อไหร่ เพราะปอกลำบาก"

show rin basic_delight_close
with charachange

# rin "It's on the list of things I want to learn properly."
rin "เป็นหนึ่งในสิ่งที่ฉันอยากหัดให้เก่ง"

# hi "How come you ate one, then?"
hi "แล้วกินได้ไง"

show rin basic_deadpanamused_close
with charachange

# rin "Emi had some, so she peeled one for me."
rin "เอมิกิน เลยปอกให้ฉันกินด้วย"

# hi "Good for you."
hi "ดีแล้ว"

show rin relaxed_nonchalant_close
with charachange

stop music fadeout 6.0

# "Rin stretches her back and yawns, and says nothing further."
"เธอยืดตัวหาวแล้วไม่พูดอะไรอีก"

# "She throws me a glance from the corner of her eye while she watches people pass by, but I couldn't say why."
"ระหว่างที่เธอมองคนที่เดินผ่านไปมาก็เหลือบมองฉัน แต่ฉันก็ไม่รู้ว่าทำไม"

# "I realize, though, that this is the first time I've talked naturally about my condition with anyone. In a way."
"แต่ฉันรู้ว่า—ในแง่หนึ่ง—ครั้งนี้เป็นครั้งแรกที่ฉันได้คุยเรื่องโรคของฉันกับใครบางคนอย่างเป็นธรรมชาติ"

stop ambient fadeout 4.0

# "A group of boys walk past us to Rin's classroom, but she doesn't pay them any mind. They pay none to her, either. My mind wanders off, spurred by the silence."
"มีกลุ่มผู้ชายที่เดินผ่านห้องริน แต่เธอก็ไม่สนใจ พวกนั้นก็ไม่สนใจเธอ ความเงียบพาให้ความคิดฉันฟุ้งซ่าน"

window hide
nvl clear
nvl show dissolve

$ renpy.music.set_volume(0.5,  0.0, channel="music")
play music music_pearly fadein 1.0

# n "\n\n\nMaybe I should've let her listen to my heart. It's not like it matters. Nothing really matters that much, at the end of the day."
n "\n\nให้เธอฟังเสียงหัวใจฉันไปเลยก็คงดี ใช่ว่าจะเป็นเรื่องใหญ่อะไร สุดท้ายก็ไม่ได้มีอะไรใหญ่ขนาดนั้นอยู่แล้ว"

# n "I start feeling depressed for no reason, again. It's like a tidal wave out of nowhere rolling over my consciousness, submerging me underwater."
n "อยู่ ๆ ก็หดหู่ขึ้นมาไม่มีปี่มีขลุ่ยอีกครั้ง เหมือนมีน้ำขึ้นน้ำลงในจิตใจที่ขึ้นสูงท่วมจนตัวฉันจมอยู่ใต้น้ำ"

# n "I feel a sigh coming out of my mouth, and I turn away from Rin, pretending to read a poster on the wall. It's an advertisement for the school festival, promoting an event almost a week past."
n "ลมถอนหายใจลอดออกมาจากปากฉัน ฉันเบือนหน้าหนีรินทำเป็นอ่านโปสเตอร์ที่โฆษณางานเทศกาลของโรงเรียน\nที่ผ่านมาแล้วเกือบสัปดาห์ที่แปะอยู่บนผนัง"

# n "The difference between me and Rin is that I'll be more likely than not dead before turning thirty, while she can't eat oranges without help."
n "ความต่างของฉันกับรินอยู่ตรงที่ว่าฉันอาจจะตายก่อนอายุสามสิบ ส่วนเธอก็จะกินส้มไม่ได้ถ้าไม่มีคนปอกให้"

# n "\n\nI can't decide which one of us is worse off."
n "\n\nฉันไม่แน่ใจนักว่าอย่างไหนแย่กว่ากัน"

#ftb or so
#maybe the latter half should be scene of its own

nvl hide dissolve
nvl clear

scene black
with delayblinds

nvl show dissolve

# n "\n\n\nI try to grasp the passing of time, but it seems hard. I'm still used to the rhythm of the hospital, where trivialities such as the day of the week or time of day didn't really matter."
n "\n\n\nฉันคอยปรับตัวให้ชินกับเวลาที่ไหลไป แต่ก็ดูจะยาก เพราะฉันยังชินกับการใช้ชีวิตที่โรงพยาบาลที่เรื่องเล็ก ๆ น้อย ๆ\nอย่างวันหรือเวลานั้นไม่สลักสำคัญเท่าไหร่"

# n "Everything was the same, no matter what."
n "ไม่ว่าจะยังไง ทุกอย่างก็ยังเหมือนเดิม"

# n "Rediscovering the significance of time is an oddly disorienting experience, and I find myself enjoying the fact that I can categorize events in this fashion."
n "การได้กลับมาระลึกถึงความสำคัญของเวลานั้นเป็นความรู้สึกที่ช่างแปลกพิกล แล้วฉันก็สนุกกับการได้จัดแบ่งเหตุการณ์\nโดยใช้วิธีนี้ด้วย"

show ev watch_black:
    center
    alpha 0.0
    linear 1.0 alpha 1.0

# n "The relevancy of a ticking clock is surprisingly delightful, and I decide to start wearing an analog wristwatch, something I didn't use to do before."
#Pondered about the "didn't use to/didn't used to" debacle for a LONG while. We'll do things this way. -SC
n "การได้ยึดโยงกับเข็มนาฬิกาที่เดินไปนั้นทำให้รู้สึกดีอย่างประหลาด จนฉันหันมาใส่นาฬิกาข้อมือแบบหน้าปัดเข็ม\nซึ่งเป็นอะไรที่ฉันไม่เคยทำมาก่อน"

# n "\nWhen I finally ask Rin on Thursday about something that's been bothering me for the entire week, it's already lunch time."
n "\nตอนที่ฉันถามรินเมื่อวันพฤหัสบดีเรื่องที่กวนใจฉันมาทั้งสัปดาห์นั้นก็เป็นเวลาพักเที่ยงแล้ว"

$ renpy.music.set_volume(1.0, 2.0, channel="music")

nvl clear
nvl hide dissolve

scene bg watchhallway_blur
show ev watch_worn:
    xalign 0.5 yalign 0.5
with locationchange

window show

# "The time is somewhere between 11:06 and 11:07, as my watch doesn't have a hand to show seconds. It's the old-fashioned kind with a black leather strap and titanium casing."
"ด้วยว่านาฬิกานั้นไม่มีเข็มวินาที จึงบอกได้เพียงว่าเวลาอยู่ช่วงระหว่าง 11 นาฬิกา 6 นาที และ 11 นาฬิกา 7 นาที\nเป็นนาฬิการุ่นเก่าที่สายทำด้วยหนังสีดำ ส่วนตัวเรือนทำจากไทเทเนียม"

# "It doesn't look flashy, but a wristwatch doesn't need to."
"ไม่ได้ดูหรูหรา แต่นาฬิกาข้อมือก็ไม่จำเป็นต้องหรูหราหรอก"

show ev watch_worn:
    easeout 0.5 ypos 1.0 alpha 0.0
with None

show bg school_hallway3
show crowd behind ev
show rin basic_awayabsent at center behind ev
show ev watch_worn:
    easeout 0.5 ypos 1.0 alpha 0.0
with locationchange

hide ev
with None

play ambient sfx_crowd_indoors fadein 2.0

# hi "Hey."
hi "นี่"

show rin basic_absent
with charachange

# hi "Remember that sketch you made of me? How you said I looked grim and gloomy or something?"
hi "จำที่เธอวาดฉันได้มั้ย ที่เธอบอกว่าหน้าฉันดูหม่น ๆ หมอง ๆ นั่นน่ะ"

# hi "I'd like to know what you meant by that."
hi "ฉันอยากรู้ว่าเธอหมายความว่ายังไง"

show rin negative_spaciness
with charachange

# "She gives me a weird look and tilts her head a few degrees to the left, but doesn't say anything for a while."
"เธอมองฉันแปลก ๆ แล้วเอียงหัวไปทางซ้ายเล็กน้อย แต่ก็ไม่ได้พูดอะไรต่อสักพัก"

# rin "Well, you see…"
rin "ก็ เนี่ย…"

show rin basic_deadpanupset
with charachange

stop ambient fadeout 2.0
stop music fadeout 2.0

# rin "We've known each other for two weeks and I haven't seen you smile even once."
rin "เรารู้จักกันมาสองสัปดาห์แล้ว แต่ฉันยังไม่เคยเห็นนายยิ้มเลยสักครั้ง"

# "Her striking observation gives me pause."
"ข้อสังเกตอันหลักแหลมของเธอทำฉันต้องชะงัก"

window hide
nvl clear
nvl show dissolve

# n "\n\n\nHave I stopped smiling?"
n "\n\nนี่ฉันไม่ได้ยิ้มแล้วเหรอ"

# n "\nI have to take what she says as truth. She has no reason to lie."
n "\nฉันต้องถือเอาว่าที่เธอพูดคือความจริง เธอไม่มีเหตุผลอะไรที่จะต้องโกหก"

# n "Something about the way she puts it annoys me. I frown at Rin, then try to correct my expression to look less depressed."
n "พอรินพูดอย่างนั้นแล้วก็รู้สึกไม่ชอบใจขึ้นมาแปลก ๆ ฉันขมวดคิ้วใส่ริน แต่จากนั้นก็ปรับหน้าตาให้ดูหดหู่น้อยลง"

# n "I haven't been in the cheeriest of moods during the past few months or so, this is true."
n "แต่จริงอยู่ที่ว่าช่วงสองสามเดือนมานี้ฉันไม่ได้มีกะจิตกะใจจะเริงร่าอะไรนัก"

# n "Does it show so much that someone like Rin can tell, after so little contact with me?"
n "นี่ฉันแสดงออกจนแม้แต่คนที่เจอกันน้อยครั้งอย่างรินยังดูออกเลยเหรอ"

# n "Should I try to smile more at Rin? Maybe she could appreciate it, having such a neutral face herself almost all the time."
n "หรือจะยิ้มให้รินให้มากขึ้นดี เธออาจจะชอบก็ได้ เห็นทำหน้าตายอยู่ตลอด"

# n "\nHave I really stopped smiling?"
n "\nนี่ฉันไม่ได้ยิ้มแล้วจริง ๆ เหรอ"

nvl hide dissolve
nvl clear
window show

play ambient sfx_crowd_indoors fadein 2.0

# hi "I see."
hi "อย่างนี้นี่เอง"

# hi "Should I smile more?"
hi "ให้ยิ้มให้มากขึ้นดีมั้ย"

show rin relaxed_nonchalant
with charachange

# rin "I don't mind either way. Be as you are; you can't help being Hisao anyway."
rin "ฉันยังไงก็ได้ นายก็เป็นนายไปเถอะ ยังไงนายก็ต้องเป็นฮิซาโอะอยู่แล้ว"

# hi "But it bothers you?"
hi "แต่เธอไม่ชอบ?"

show rin basic_absent
with charachange

# rin "I just noticed it, that's all."
rin "ฉันก็แค่จับสังเกตได้เท่านั้นเอง"

show emi excited_smile:
    tworight
    xpos -0.5
with None

show rin basic_absent at tworight
show crowd at bgright
show bg school_hallway3 at bgright
show emi excited_smile at twoleft
with charamove

play music music_emi fadein 0.2

# "Emi skips along the hallway, jumps to a sharp stop when she reaches us, and lightly pats Rin's shoulder."
"เอมิโลดเต้นมาตามโถงทางเดินก่อนจะเบรกเอี๊ยดอยู่ตรงหน้าพวกเราแล้วตบบ่ารินเบา ๆ"

show emi basic_happy
with charachange

# emi "Ready for lunch?"
emi "พร้อมกินข้าวเที่ยงหรือยัง"

show rin basic_deadpanupset
with charachange

# rin "Depends on what lunch is today. Remember that stew from March? Never again, that."
rin "ก็อยู่ที่ว่าข้าวเที่ยงคืออะไร จำสตูเมื่อเดือนมีนาได้มั้ย ไม่เอาอีกแล้วนะ อันนั้น"

show emi basic_closedgrin
with charachange

# emi "Let's go anyway. I'm starving!"
emi "ไปเถอะ ๆ ฉันหิวแล้ว!"

hide emi
hide rin
with charaexit

# "As they are about to depart, Emi turns from her friend to me, seemingly as an afterthought, and smiles charmingly."
"จังหวะที่ทั้งสองคนกำลังจะออกไป เอมิก็หันหน้าจากเพื่อนเธอมาทางฉันเหมือนเพิ่งนึกอะไรได้แล้วโปรยยิ้มเสน่ห์"

show emi sad_grin at center
with charaenter

# emi "By the way, Hisao…"
emi "จะว่าไป ฮิซาโอะ…"

# "Her tone is way too sweet and soft to be sincere. I can sense the trap about to be sprung upon me by this miniature health-devil."
"น้ำเสียงเธอดูอ่อนหวานและนุ่มนวลเกินกว่าจะมาจากใจจริง ฉันสัมผัสได้ถึงกับดักที่พร้อมจะงับฉันที่ถูกวางไว้โดย\nปีศาจสุขภาพดีตนนี้"

# "I know what she's about to say even before she continues, because I've been trying to avoid her all week."
"ไม่ต้องให้เธอพูดต่อก็รู้เลยว่าจะบอกอะไร เพราะฉันเลี่ยงมาตลอดทั้งสัปดาห์"

show emi excited_proud
with charachange

# emi "I still haven't seen you at the track this entire week."
emi "สัปดาห์นี้ฉันยังไม่เห็นหน้านายที่ลู่วิ่งเลยสักครั้งนะ"

# hi "Maybe I've been there when you haven't."
hi "ฉันน่าจะไปตอนที่เธอไม่อยู่มั้ง"

show emi sad_annoyed
with charachange

# emi "That's impossible. I'm there all the time."
emi "เป็นไปไม่ได้ ฉันก็อยู่ที่ลู่ตลอด"

# hi "But you sleep and go to class."
hi "แต่เธอต้องไปนอนไปเรียนนะ"

show emi basic_annoyed
with charachange

# emi "I do those at the same time as you do."
emi "ฉันก็นอนก็เรียนเวลาเดียวกันกับนาย"

# hi "Yeah, I know, I know. I just… haven't been able to pick myself up."
hi "เออ รู้ ๆ ฉันแค่… ไม่มีอารมณ์จะวิ่ง"

# hi "Don't rat me out to the nurse, okay?"
hi "อย่าเอาไปฟ้องคุณพยาบาลเลยนะ"

# hi "Running just isn't my thing, and I haven't come up with a good alternative."
hi "วิ่งนี่ไม่ใช่ทางฉันจริง ๆ แล้วฉันก็ยังไม่รู้ว่าจะออกกำลังกายแบบอื่นยังไงดีด้วย"

show emi excited_happy
with charachange

# emi "Why don't you come to the track meet this weekend? Maybe you'll get inspired."
emi "งั้นสุดสัปดาห์นี้มาดูงานแข่งวิ่งมั้ย เผื่อจะมีแรงบันดาลใจขึ้นมา"

# hi "Track meet?"
hi "แข่งวิ่ง?"

show emi basic_happy
with charachange

# emi "Yeah! People from a few other schools come here for some friendly track and field action. It's on Sunday afternoon."
emi "อื้ม! มีคนจากโรงเรียนอื่นมาแข่งกรีฑากระชับมิตรกันด้วย แข่งบ่ายวันอาทิตย์นี้"

# "I can't think of any reason not to go."
"ไม่รู้จะเอาอะไรมาบอกว่าไม่ไปดี"

# hi "Sure. I'll come and cheer for you. I guess you'll be running?"
hi "ได้สิ เดี๋ยวไปส่งแรงใจให้ เธอแข่งวิ่งใช่มั้ย"

show emi excited_proud
with charachange

# emi "Of course! You'll get to see me beat them all!"
emi "แน่อยู่แล้ว! เดี๋ยวนายจะได้เห็นฉันแซงทุกคนเลย!"

show emi basic_grin
with charachange

# emi "But bye now! If I don't get something to eat, I'll die."
emi "แต่ตอนนี้ขอตัวก่อน! ถ้าฉันไม่หาอะไรกินเดี๋ยวจะตาย"

# hi "See you later."
hi "เจอกัน"

hide emi
with charaexit

stop music fadeout 3.0

# hi "Bye Rin. I promise I'll smile next time."
hi "งั้นไปละนะริน เดี๋ยวคราวหน้าสัญญาจะยิ้ม"

# "I call after her, as a bit of an afterthought. Afterward, I feel embarrassed about it, and wonder why I said anything at all."
"ฉันเรียกเธอไปเหมือนนึกทิ้งทวน แต่หลังจากนั้นก็มาอายแล้วคิดว่าจะพูดอะไรออกไปทำไม"

stop ambient fadeout 1.0

scene ev hisao_mirror_800
with shorttimeskip

# "That night, when I'm doubly certain that Kenji won't be barging in the bathroom, I look in the mirror and smile at my reflection."
"คืนนั้น หลังจากที่ดูจนแน่ใจจริง ๆ แล้วว่าเคนจิจะไม่บุกเข้ามาในห้องน้ำฉันก็มองกระจกแล้วยิ้มให้เงาสะท้อนตัวเอง"

# "The me in the mirror smiling at the me in the bathroom looks awfully fake."
"ตัวฉันในกระจกที่ส่งยิ้มให้ฉันในห้องน้ำนั้นดูปลอมเปลือกสิ้นดี"

scene black
with dissolve

#*****************


label th_R6:

play music music_happiness fadein 2.0

scene bg school_library
with locationchange

# "Having exhausted the books Kenji lent me in just a few nights, I go back to the library, deeming it a safer alternative for getting my reading fix."
"หลังจากที่อ่านหนังสือที่เคนจิให้ยืมมาจนหมดในไม่กี่คืนฉันก็มาที่ห้องสมุดด้วยคิดว่าคงจะเป็นตัวเลือกที่ปลอดภัยกว่า\nที่จะมารับยาหนังสือฉัน"

# "I return the books he had stolen while I'm at it, to Yuuko's delight. I don't tell her where I got them, though."
"เอาหนังสือที่ถูกขโมยมาคืนด้วย ยูโกะก็ดีอกดีใจ แต่ฉันไม่ได้บอกหรอกนะว่าได้มาจากไหน"

show yuuko happy_down at center
with charaenter

# yu "Wow, you sure read a lot, don't you?"
yu "โห เธออ่านเยอะน่าดูเลยนะ"

# hi "Yeah, I guess I do."
hi "อื้ม คงงั้นแหละครับ"

# hi "I mean, I do. Even I think it's weird. I think I might have a reading problem. Maybe I'm a junkie."
hi "คือ ก็เยอะแหละครับ แต่ขนาดผมยังว่าแปลกเลย สงสัยจะมีปัญหากับการอ่านแล้วสิ อาจจะติดหนังสือไปแล้วมั้งครับ"

show yuuko panic_up
with charachange

# yu "No no, I didn't mean it that way. It's not weird at all, and being addicted to reading is a lot better than being addicted to… to something else."
yu "เปล่า ๆ ไม่ได้หมายความอย่างนั้น ไม่แปลกเลย ๆ แล้วติดหนังสือน่ะดีกว่าไปติด… อะไรอย่างอื่นเยอะ"

# hi "Yeah, I know. It was a joke."
hi "ครับ ๆ ผมหยอกเล่นน่า"

# "I smile at her reassuringly and drop the books on the counter so Yuuko can check them out. I feel tired, so I sit down in the vacant chair in front of her desk."
"ฉันยิ้มให้เธอคลายกังวลแล้ววางหนังสือไว้กับเคาน์เตอร์ให้ยูโกะจัดการยืมแล้วนั่งลงกับเก้าอี้ว่างตรงหน้าโต๊ะเธอ\nด้วยความเหนื่อยอ่อน"

show yuuko neutral_up
with charachange

# "While Yuuko goes through the modest pile of reading material I found, I let my gaze wander around the library."
"ระหว่างที่ยูโกะกำลังจัดการกับกองหนังสือน้อย ๆ ที่ฉันได้มานั้นฉันก็มองไปรอบ ๆ ห้องสมุด"

hide yuuko
with charaexit

# "At the tables, a pair of girls is chattering in hushed tones rather than working on their homework."
"ที่โต๊ะนั่งมีสาวอยู่คู่หนึ่งกำลังกระซิบกระซาบคุยกันแทนที่จะทำการบ้าน"

# "The short-haired one notices me looking in their direction and waves at me. When I raise my hand back, they glance at each other and giggle in unison."
"คนที่ผมสั้นเห็นว่าฉันมองอยู่จึงโบกมือให้ พอฉันยกมือทักทายกลับทั้งสองคนก็มองตากันแล้วหัวเราะคิกคักกัน"

# "I'm not sure how I should feel about that, so I decide it's a good thing. The one who waved at me has a horrible case of epilepsy."
"ไม่แน่ใจเหมือนกันว่าจะรู้สึกยังไงดี เอาเป็นว่าเป็นเรื่องที่ดีแหละ คนที่โบกมือให้ฉันเธอเป็นโรคลมชักขั้นรุนแรง"

# "I saw her having an attack a few days ago. It was one of the most disturbing and scary things I've seen in a very long time."
"สองสามวันก่อนเห็นเธออาการกำเริบอยู่ ฉันไม่เคยเห็นอะไรที่ชวนให้ใจคอไม่ดีและน่ากลัวขนาดนั้นมานานมากแล้ว"

# "Yet, there she is, happily chirping away about whatever, as if she doesn't have a care in the world."
"แต่เธอก็มานั่งอยู่ตรงนั้น มาคุยอะไรเรื่อยเปื่อยอยู่อย่างมีความสุขราวกับไม่มีอะไรให้ทุกข์ร้อนใจ"

# hi "You know, this school is really something else."
hi "เอ้อ โรงเรียนนี้พิเศษจริงเลยนะครับ"

show yuuko panic_up
with charaenter

# "Yuuko raises her eyes from the books she was going through, slightly startled. She adjusts her glasses and puts on a nervous, confused smile."
"ยูโกะสะดุ้งเล็กน้อยแล้วเงยหน้าขึ้นมาจากกองหนังสือที่เธอจัดการอยู่ เธอดันแว่นแล้วยิ้มขึ้นมาด้วยท่าทีเกร็ง ๆ งง ๆ"

show yuuko smile_down
with charachange

# yu "What do you mean?"
yu "หมายความว่าไงเหรอ"

# hi "I don't really know how to explain it. It's just that everyone's so… active, or …how should I put it?"
hi "ไม่รู้จะอธิบายยังไงดีเหมือนกันครับ แค่ว่าทุกคนดู… กระตือรือร้น หรือจะบอกว่า… จะว่ายังไงดีนะ"

# hi "It's not just the festival thing, I think, even though I haven't been here that long, but it's everything."
hi "ผมคิดว่าไม่ใช่แค่เรื่องเทศกาลหรืออะไรหรอก แต่ดูจะเป็นกับทุกอย่างเลย ถึงผมจะยังมาอยู่ได้ไม่นานขนาดนั้นก็เถอะ "

# hi "People talk more, work harder and just… are… more than in any other school I've seen before."
#I'm not sure what the huge hate for text formatting is about, but it would seem to me that "are" here rates italicization. ---K.
hi "คนที่นี่ดูจะคุยกันมากกว่า ขยันกว่า แล้ว… ก็… พิเศษกว่าโรงเรียนอื่น ๆ ที่ผมเคยเห็นเลย"

# "I'm struggling for words, but it feels like I'm speaking honestly."
"ฉันนึกหาคำพูดไม่ค่อยออก แต่ก็รู้สึกเหมือนได้พูดจากใจ"

label th_choiceR6:
menu:
    with menueffect

    # hi "This school feels so alive."
    hi "โรงเรียนนี้มันมีชีวิตชีวามากเลย"

    # "It's refreshing.":
    "รู้สึกแปลกใหม่ดี":
        return m1

    # "It makes me feel like I'm stuck.":
    "รู้สึกเหมือนติดหล่ม":
        return m2

label th_R6a:

# hi "Sure, there were some people like this in my old school, too, but not as many. And it feels more intense, somehow."
hi "คือที่โรงเรียนเก่าผมก็มีคนแบบนี้นั่นแหละครับ แต่ก็ไม่ได้เยอะเท่านี้ แถมที่นี่ก็ดูมุ่งมั่นกันกว่าด้วย"

# hi "I think, if I had to pin it down to one thing, that the students here really appreciate going to school."
hi "ผมว่า ถ้าจะให้เลือกมาพูดสักอย่าง ก็คงจะเป็นเรื่องว่านักเรียนที่นี่ดูจะชอบมาโรงเรียนกันน่ะครับ"

label th_R6b:

# hi "I feel like I need to start moving in some direction, too. That's how this school makes me feel."
hi "ผมรู้สึกว่าพอได้มาอยู่โรงเรียนนี้แล้วก็รู้สึกว่าตัวผมเองก็ต้องมีเป้าหมายขยับไปข้างหน้าบ้างน่ะครับ"

label th_R6c:

show yuuko worried_up
with charachange

# yu "I don't think that's a bad thing."
yu "ฉันว่ามันก็ไม่ได้แย่หรอก"

# hi "Yeah, me neither."
hi "อื้ม ผมก็ว่างั้น"

# "Suddenly I realize that I've just been babbling my thoughts to Yuuko, out of the blue. She's a bit of a jumpy person, so I fear I might've made a bad impression."
"จนตอนนั้นเองถึงนึกได้ว่าอยู่ ๆ ฉันก็มาพล่ามความคิดของตัวเองให้ยูโกะฟัง เธอเป็นคนค่อนข้างขี้ตกใจ นี่ฉันคงไป\nทำให้เธอกลัวสิเนี่ย"

# "She's looking at me with what I hope is curiosity rather than horror, so I figure she's all right."
"แต่สีหน้าที่เธอมองมาดูจะเป็นความสงสัย—หวังว่านะ—และไม่ใช่ความกลัว ก็แปลว่าคงไม่เป็นไร"

# hi "Sorry for suddenly talking about weird stuff like this. I didn't mean to trouble you."
hi "ขอโทษที่จู่ ๆ ก็พูดอะไรแปลก ๆ อย่างนี้นะครับ ผมไม่ได้ตั้งใจจะรบกวนคุณเลย"

show yuuko smile_down
with charachange

# yu "Oh no, it's not troubling. I'm happy to listen if you feel like talking."
yu "อ้อ ไม่เลย ๆ ไม่รบกวนเลย ถ้าอยากคุยฉันก็ยินดีรับฟังเสมอนะ"

show yuuko neutral_down
with charachange

# yu "It makes me feel a little reliable, too."
yu "จะได้รู้สึกว่าตัวเองพึ่งพาได้หน่อยด้วย"

# "Yuuko smiles sweetly and a little bit ironically at that. I respond with a thankful smile of my own."
"เธอยิ้มหวาน ๆ แถมแกน ๆ อีกต่างหาก ฉันก็ยิ้มขอบคุณไปบ้าง"

# "As she pushes the neat stack of books across the counter, I stand up and gather them in my arms."
"พอเธอดันกองหนังสือที่ตั้งเรียบร้อยแล้วอยู่บนเคาน์เตอร์ฉันก็ลุกขึ้นมารับ"

show yuuko closedhappy_up
with charachange

# yu "Here you are."
yu "เอ้านี่"

# hi "Thank you."
hi "ขอบคุณครับ"

show yuuko neutral_up
with charachange

# yu "I guess we'll be meeting each other again. Please come here anytime."
yu "เดี๋ยวคงจะได้เจอกันอีกแหละเนอะ แวะมาได้เสมอเลยนะ"

# "Yuuko's kindness is heartwarming."
"ความใจดีของยูโกะนั้นแสนจะอบอุ่นหัวใจ"

# hi "You can count on it. See you later."
hi "ครับ ไว้เจอกันนะครับ"

stop music fadeout 2.0

scene black
with dissolve

#**************
label th_R7:

scene bg school_courtyard
show crowd
with locationchange
play ambient sfx_crowd_outdoors fadein 7.0

# "The morning of the track meet greets me with a brilliant sunshine from a crystal blue sky."
"ประกายแดดสาดส่องจากฟ้าครามกระจ่างทักทายฉันในเช้าวันแข่ง"

# "While I leisurely stroll towards the track, I decide this is a good sign. Of what, I'm not sure; this event isn't as exciting for me as it seems to be for a large portion of the student body."
"ระหว่างที่เดินกรีดกรายมายังลู่วิ่งฉันก็นึกได้ว่านี่เป็นนิมิตหมายอันดี อะไรดีฉันก็ไม่แน่ใจเหมือนกัน ฉันไม่ได้ตื่นเต้น\nกับงานนี้สักเท่าไหร่เพราะเหมือนจะเป็นงานสำหรับนักเรียนส่วนใหญ่มากกว่า"

# "I'm even less interested in watching sports than I am in participating, but cheering for Emi is a good cause."
"ฉันยังจะสนใจการเล่นกีฬามากกว่าการดูกีฬาเสียอีก แต่มาเป็นแรงใจให้เอมิก็ดีเหมือนกัน"

# "I'm not expecting this to be any sort of amazing and spectacular experience, but it can't hurt. I'd probably be spending the time reading while cooped up in my room, otherwise."
"ฉันไม่ได้คาดหวังว่าจะได้มาสัมผัสประสบการณ์อันตื่นตาตื่นใจอะไรนัก แต่มาหน่อยก็ไม่เสียหาย ยังไงถ้าไม่มาก็คง\nเอาแต่เก็บตัวอยู่ในห้องอ่านหนังสือนั่นแหละ"

scene bg school_track
show crowd
show rin basic_absent at center
with locationchange

# "When I approach the bleachers, I spot Rin emerging from the crowd right before she spots me."
"พอเดินเข้าไปใกล้สแตนด์เชียร์ก็เห็นรินที่อยู่กลางกลุ่มคน จังหวะนั้นเธอก็เห็นฉันพอดี"

show rin basic_deadpannormal
with charachange

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

show rin negative_spaciness
with charachange

# "Rin shrugs. Seemingly bored with our conversation, she turns on her heel and heads back toward the stands."
"รินยักไหล่ พอเหมือนจะเบื่อกับบทสนทนานี้แล้วเธอก็หมุนส้นเท้าแล้วเดินไปที่สแตนด์เชียร์ต่อ"

# hi "So, are you excited about this?"
hi "แล้วเธอตื่นเต้นมั้ย"

show rin basic_deadpan
with charachange

# rin "Not really."
rin "ไม่เท่าไหร่"

# hi "Me neither."
hi "ฉันก็ไม่"

show rin basic_absent
with charachange

# rin "Then why did you come?"
rin "แล้วนายมาทำไม"

# hi "Why did you?"
hi "แล้วเธออะ"

# "She doesn't reply at all, so I decide not to, either."
"เธอไม่ตอบเลย ฉันก็เลยคิดที่จะไม่ตอบเหมือนกัน"

# "We enter the bleachers, and Rin nods upwards."
"พอมาถึงที่สแตนด์เชียร์แล้วรินก็บุ้ยใบ้ไปข้างบน"

show rin negative_spaciness at center
with charaenter

# rin "Up there."
rin "บนนั้น"

show rin basic_deadpancontemplation
with charachange

# "Rin leads the way, and soon we've settled down on an almost-empty bench."
"รินนำทางขึ้นไป ไม่นานพวกเราก็มานั่งตรงที่นั่งแถวที่โล่ง ๆ "

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
hi "หา?"

show rin basic_surprised
with charachange

# rin "This is no good?"
rin "ไม่ได้เหรอคะ"

show meiko happy
show rin basic_awayabsent
with charachange

# "The woman laughs at Rin and shakes her head, apparently unable to find a comeback for that. I know the feeling."
"เธอหัวเราะรินแล้วสั่นหัว ดูท่าไม่รู้จะตอบยังไง ฉันเข้าใจดีเลยละ"

show meiko smile
with charachange

# emm_ "Well, I suppose you've always been one to go out for one thing and bring back another."
emm_ "อืม เธอก็คงเป็นคนที่ชอบออกไปหยิบของอย่างหนึ่งแล้วได้อีกอย่างมาแทนอยู่แล้วละมั้งจ๊ะ"

# emm_ "But I'm being rude! I haven't introduced myself."
emm_ "ตายละ หยาบคายจัง! ยังไม่ได้แนะนำตัวเลย"

# emm_ "I'm Meiko Ibarazaki. I'm sure that if you know this girl, you've at least met my daughter, too."
emm_ "ฉัน เมอิโกะ อิบาราซากิ จ้ะ ถ้ารู้จักเธอคนนี้ก็คงรู้จักลูกสาวฉันด้วยสินะจ๊ะ"

show meiko happy
with charachange

# emm "Pleased to meet you."
emm "ยินดีที่ได้รู้จักจ้ะ"

# "Well, that explains it. She's like a taller, older, more motherly Emi."
"อืม ก็ว่าอยู่ว่าเหมือนเอมิที่ตัวสูงกว่า แก่กว่า แล้วก็มีความเป็นแม่มากกว่า"

# "Apart from her hair being somewhat darker than her daughter's, there's really no mistaking the resemblance."
"นอกจากสีผมที่เข้มกว่าลูกสาวเธอแล้วที่เหลือก็คล้ายกันมาก"

show rin basic_absent
show meiko smile
with charachange

# hi "Sorry, I'm Hisao. Hisao Nakai. Nice to meet you."
hi "ขอโทษครับ ผมฮิซาโอะ ฮิซาโอะ นากาอิ ยินดีที่ได้รู้จักครับ"

show rin basic_lucid
with charachange

# rin "I'm Rin Tezuka."
rin "ริน เทซูกะ ค่ะ"

show meiko happy
show rin basic_awayabsent
with charachange

# "Mrs. Ibarazaki laughs again - she really does resemble her offspring - and then leans back a little on her seat and raises an eyebrow."
"คุณนายอิบาราซากิหัวเราะอีกครั้ง ลูกไม้หล่นไม่ไกลต้นจริง ๆ เธอนั่งเอนตัวเล็กน้อยแล้วเลิกคิ้วขึ้น"

$ renpy.music.set_volume(0.0, 0.5, channel="ambient")

show meiko serious
with charachange

stop music fadeout 1.0

# emm "So, now that we all know each other, how long have you and Rin been dating?"
emm "ทีนี้ก็รู้จักกันแล้ว เธอสองคนคบกันมานานหรือยัง"

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

# hi "We're not—"
hi "เราไม่ได้—"

show meiko happy
show rin basic_awayabsent
with charachange

# emm "I know, but it's funny to watch you squirm."
emm "รู้จ้ะ แต่เห็นเธออายแล้วตลกดี"

show meiko wink
with charachange

# emm "I'm sorry. Forgive an old woman her amusements."
emm "ขอโทษทีนะจ๊ะ อย่าถือสาคนรุ่นป้าเลยจ้ะ"

# "She chuckles again to herself."
"เธอหัวเราะกับตัวเองอีกครั้ง"

# "Old woman?"
"ป้า?"

# "She sure doesn't look that old to me."
"ก็ดูไม่แก่ขนาดนั้นนะ"

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

# "By the time she rounds the final turn, a few of the other runners have caught up with her."
"พอเธอวิ่งจนมาถึงโค้งสุดท้ายก็มีนักวิ่งสองสามคนที่ตามมาทันแล้ว"

# "But she puts on a final burst of speed that leaves them at least a half second behind."
"แต่เธอก็พุ่งตัวปิดท้ายจนทิ้งห่างจากคนที่ว่าสักครึ่งวินาทีเห็นจะได้"

scene ev emitrack_finish
with locationchange

stop ambient fadeout 1.0
play sound sfx_crowd_cheer

# "Mrs. Ibarazaki whoops and shouts, applauding wildly, and generally looking like any other parent cheering on their child."
"คุณนายอิบาราซากิกรี๊ดกร๊าดพลางปรบมือใหญ่ ดูไม่ต่างไปจากพ่อแม่ที่มาเอาใจช่วยลูกตัวเองที่ลงแข่งโดยทั่วไป"

# "Emi bounds off the track, looking pleased with herself."
"เอมิออกมาจากลู่วิ่งดูพอใจกับตัวเอง"

play music music_daily fadein 2.0

scene bg school_track at bgright
show meiko happy at twoleft
show rin basic_deadpandelight at tworight
with locationchange

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

# "We fall silent as the next event prepares to start."
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
emm "เธอวิ่งอันนี้ วิ่ง 100 เมตร แล้วก็วิ่งผลัดด้วย"

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

# hi "You seem pretty into this stuff. I'm surprised; I thought you said this wouldn't be exciting."
hi "เธอดูสนใจนะ แปลก เธอบอกว่าไม่ได้ตื่นเต้นไม่ใช่เหรอ"

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

stop ambient fadeout 1.0
play sound sfx_crowd_cheer

# "As soon as she crossed the finish line, the fierce look was replaced by her normal grin."
"ทันทีที่เธอเข้าเส้นชัย รอยยิ้มอย่างเคยของเธอก็ผุดขึ้นแทนที่สีหน้าอันมุ่งมั่น"

# "The conquering general returning to his farm."
"เหมือนนายพลอันเก่งกล้าที่กลับมาใช้ชีวิตอยู่บ้านนอก"

# hi "Amazing."
hi "สุดยอด"

# hi "She's really amazing. I've never seen someone move that fast."
hi "สุดยอดจริง ๆ ครับ ผมไม่เคยเห็นใครเร็วขนาดนั้นมาก่อนเลย"

scene bg school_track at bgright
show meiko smile at twoleft
show rin basic_deadpanamused at tworight
with locationchange

# emm "Well, don't look at me, I'm far too relaxed to run that fast."
emm "แหม ไม่ต้องมองฉันหรอกจ้ะ ฉันเอื่อยเกินจะวิ่งเร็วขนาดนั้นแล้ว"

stop sound fadeout 9.0

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

# hi "Ah, really? I didn't know that."
hi "อ้อ จริงเหรอครับเนี่ย ไม่ยักรู้แฮะ"

# "I leave it at that, and don't say anything for a little while. I get the feeling this is something personal I shouldn't ask about."
"ฉันตอบแค่นั้นไม่พูดอะไรต่ออยู่สักพักเพราะรู้สึกว่าเป็นเรื่องส่วนตัวที่ฉันไม่ควรถาม"

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
emm "ฝากบอกเอมิหน่อยได้ไหมจ๊ะว่าแม่ภูมิใจในตัวลูกมาก ฝากบอกด้วยว่าเดี๋ยวคืนนี้จะโทรไปหาอีกที"

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

# "While waiting for the relay to start, I peer at Rin. She seems uninterested in her surroundings, myself included."
"ระหว่างที่รอดูวิ่งผลัดฉันก็เหล่มองริน เธอดูจะไม่สนใจสิ่งรอบข้างรวมถึงฉันด้วย"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

# n "\n\n\n\nThat remark she made before is still stuck in my head."
n "\n\n\nคำพูดนั้นที่เธอบอกก่อนหน้านี้ยังติดหูฉันอยู่"

# n "“Emi's the most Emi when she runs.”"
n "“เอมิจะเป็นเอมิที่สุดก็ตอนที่เธอวิ่ง”"

# n "It does make sense, now that I think about it. After seeing her run now, I can believe that Emi gives her all on the track."
n "ซึ่งพอมาคิดดูแล้วก็เข้าใจ พอได้ดูเธอวิ่งแล้วฉันก็เชื่อเลยว่าเอมิเธอทุ่มเทสุดกำลังเมื่ออยู่บนลู่วิ่ง"

# n "Sports are more than a hobby or even a competition, to her. They're a defining aspect of her life."
n "สำหรับเธอแล้วกีฬานั้นเป็นมากกว่างานอดิเรกหรือการแข่งขัน การวิ่งคือตัวตนของเธอ"

# n "What about Rin, then? Does she feel the same way about art? Considering the persistence she displayed before the festival, I could easily believe it."
n "แล้วรินล่ะ ศิลปะเป็นอย่างนั้นสำหรับเธอด้วยหรือเปล่า พอลองนึกถึงความมุมานะที่เธอแสดงให้เห็น\nก่อนวันงานเทศกาลแล้วฉันก็เชื่อได้ทันทีว่าเป็นเช่นนั้น"

# n "Did I see Rin at her “most Rin” when she was painting the mural?"
n "ฉันได้เห็นรินที่ “เป็นรินที่สุด” ตอนที่เธอวาดภาพเขียนผนังหรือเปล่านะ"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear
window show

# "The relay's about to begin, but I don't see Emi anywhere."
"การแข่งวิ่งผลัดจะเริ่มแล้ว แต่ฉันยังไม่เห็นเอมิเลย"

# hi "I thought Emi ran the relay."
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
"สวยจริง ๆ "

# "The look of determination and fearlessness on her face only adds to the picture."
"สีหน้าอันมุ่งมั่นและไร้ซึ่งความเกรงกลัวใด ๆ ของเธอยิ่งทำให้ดูดีขึ้นไปอีก"

# "Emi at her Emiest, I suppose."
"นี่แหละมั้ง เอมิที่เป็นเอมิ๊เอมิ"

stop ambient fadeout 1.0
play sound sfx_crowd_cheer

show ev emitrack_finish
with locationskip

# "Emi flies across the finishing line with a great leap, just barely ahead of the next runners, but still in first."
"เอมิกระโจนทะยานเข้าเส้นชัยนำเหลื่อมอีกคนมาอย่างเฉียดฉิว แต่เธอก็เข้าเส้นชัยเป็นคนแรก"

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")

scene bg school_track
show rin negative_worried at center
with locationskip

show rin basic_absent
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

# "It doesn't seem her style to draw attention to herself. Or to emote beyond shrugging."
"เธอดูจะไม่ใช่คนที่เรียกความสนใจจากใครเอง ไม่ใช่คนที่จะแสดงอารมณ์อะไรนอกจากการยักไหล่"

# "Being more impatient than Rin, I wave to Emi in her stead. She looks up and grins happily at us."
"ฉันอดใจรออย่างรินไม่ไหวจึงโบกมือทักทายเอมิ เธอยิ้มร่ามาให้เราอย่างมีความสุข"

show bg school_track_on at bgright
show crowd at bgright
show rin basic_awayabsent at tworight
with charamove

play music music_emi fadein 1.0

show emi basic_closedhappy_gym at twoleft
with charaenter

# emi "Hey, you showed up!"
emi "ไง มาจนได้นะ!"

show rin basic_deadpanupset
with charachange

# rin "We would have brought you a crown of laurels, but Hisao didn't find one."
rin "จริง ๆ จะมีมงกุฎช่อมะกอกมาให้เธอด้วย แต่ฮิซาโอะหาไม่เจอ"

show emi basic_grin_gym
with charachange

# hi "Neither did you."
hi "เธอก็หาไม่เจอหรอก"

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
"เอมิหัวเราใส่ฉันกับริน"

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

# hi "Very impressive."
hi "ประทับใจมาก"

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

show emi basic_closedgrin_gym
with charachange

# "Emi giggles, and then seems to remember something."
"เอมิหัวเราะคิกคักแล้วทำท่าเหมือนนึกอะไรได้"

show emi basic_happy_gym
with charachange

# emi "Oh, before I forget…"
emi "อ้อ ก่อนจะลืม…"

# emi "Rin and I are going to do something next Sunday as a post-track meet celebration!"
emi "รินกับฉันจะไปฉลองที่แข่งวิ่งเสร็จกันวันอาทิตย์หน้าละ!"

show emi excited_proud_gym
with charachange

# emi "You should come along!"
emi "นายมาด้วยก็ดีนะ!"

show emi sad_grin_gym
with charachange

# emi "Normally we do it the day after, but since today is Sunday, I've got homework and class and all that stuff to take care of."
emi "ปกติจะไปฉลองหลังวันแข่งเลย แต่พอดีวันนี้วันอาทิตย์ เดี๋ยวมีการบ้านมีเรียนมีอะไรอีก"

show rin basic_absent
with charachange

# hi "Oh sure, I'd love to."
hi "อ้อ ได้สิ ยินดียิ่ง"

show rin basic_awayabsent
show emi excited_laugh_gym
with charachange

# emi "Great! It's a promise, then!"
emi "เยี่ยม! สัญญาแล้วนะ!"

show rin basic_absent
with charachange

# hi "Oh, right. Your mom wanted to say she's proud of you."
hi "เอ้อ จริงสิ แม่เธอฝากบอกว่าภูมิใจในตัวเธอมาก"

# hi "She'll call you later tonight."
hi "แล้วก็คืนนี้แม่เธอจะโทรไปหาอีกที"

show emi basic_happy_gym
show rin basic_awayabsent
with charachange

# emi "I thought I saw her in the stands!"
emi "ก็ว่าเหมือนเห็นที่สแตนด์อยู่!"

show emi basic_closedhappy_gym
with charachange

# emi "I'm glad she made it!"
emi "ดีใจจังที่แม่มาดูจนได้!"

# "Teammate" "Hey, Emi! You're going to miss the medal ceremony!"
thname("เพื่อนร่วมทีม") "นี่ เอมิ! เดี๋ยวก็ไม่ทันไปรับเหรียญรางวัลหรอก!"

show emi basic_shock_gym
with charachange

# emi "Oh yeah, thanks!"
emi "อ้อ จริงด้วย ขอบใจนะ!"

show emi basic_grin_gym
with charadistant

# "She turns to Rin and myself."
"เธอหันมาหารินและฉัน"

# emi "You don't have to stick around for this part. It takes forever."
emi "ไม่ต้องอยู่รอก็ได้นะ พิธีนานเป็นชาติเลย"

show emi excited_proud_gym
with charachange

# emi "Besides, you should get cracking on your homework now if you don't want to be up late, Hisao."
emi "อีกอย่าง ถ้าไม่อยากนอนดึกก็รีบไปทำการบ้านได้แล้วนะฮิซาโอะ"

play sound sfx_emipacing

hide emi
with easeoutleft

stop sound fadeout 2.0

show bg school_track_on at center
show crowd at center
show rin basic_awayabsent at center
with charamove

stop music fadeout 5.0

# "Emi skips back to her teammates, leaving me and Rin by ourselves."
"เอมิทิ้งฉันและรินไว้แล้วกลับไปหาเพื่อนร่วมทีมของเธอ"

# "Neither of us has the slightest interest in the post-competition ceremonies, so we silently get away and back to the quad."
"เราสองคนไม่มีใครสนใจพิธีหลังแข่งเสร็จ พวกเราจึงปลีกตัวกลับมาที่ลานโรงเรียนอย่างเงียบ ๆ"

$ renpy.music.set_volume(0.3, 2.0, channel="ambient")

scene bg school_courtyard
show crowd
show rin relaxed_nonchalant at center
with locationskip

# "Rin yawns without even trying to restrain herself and shuffles her feet around restlessly."
"รินหาวหวอดแบบไม่มีการกลั้นพลางสลับเท้าเดินไปมา"

# "I feel awkward, but less so than if I was with someone else. Still, I'm left hanging, not knowing what I should say next."
"ก็อึดอัดแหละ แต่ก็น้อยกว่าตอนอยู่กับคนอื่น แต่ก็ยังอึน ๆ อยู่เพราะไม่รู้จะพูดอะไรต่อดี"

# hi "Emi was great, wasn't she?"
hi "เอมิเก่งเนอะ"

show rin basic_deadpannormal
with charachange

# rin "She was great. I am very jealous of her."
rin "เก่ง ฉันอิจฉาเธอมาก"

# hi "Why?"
hi "ทำไม"

show rin basic_awayabsent
with charachange

# rin "Like I said, don't you think it's great to be able to really be yourself?"
rin "อย่างที่ฉันบอก เป็นตัวของตัวเองมันดีจะตายไปนี่นา"

# "It sounds weird, coming from Rin."
"พอออกจากปากรินแล้วก็ฟังดูทะแม่ง ๆ"

# hi "I don't think you, of all people, should have trouble finding a way to express yourself."
hi "ฉันว่าคนอย่างเธอ ถ้าให้เทียบกับคนอื่น แสดงตัวตนเป็นตัวของตัวเองได้แบบไม่มีปัญหาเลย"

# hi "Don't you have your paintings?"
hi "เธอก็วาดรูปไม่ใช่เหรอ"

show rin basic_absent
with charachange

stop ambient fadeout 1.0

# "She turns to look at me. For the first time, I see in her eyes this strange, hollow expression that I think must be unique to her."
"เธอหันมามองฉัน เป็นครั้งแรกที่ฉันเห็นแววตาสีหน้าอันเปล่ากลวงที่คงเป็นเอกลักษณ์เฉพาะเธอเป็นแน่แท้"

# rin "No, you see, the problem is that I'm not really sure who I am."
rin "ไม่ เนี่ย เรื่องคือฉันไม่แน่ใจว่าจริง ๆ แล้วฉันเป็นใครกันแน่"

stop ambient fadeout 1.0
scene black
with dissolve

#**************
label th_R8:


$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
scene bg school_classroomart at right
with locationchange

# "Today's art club meeting is currently on hold while everyone waits for Nomiya to show up. I take this time to try and explain my theory about Yamaku to Rin."
"กิจกรรมชมรมวันนี้ยังไม่เริ่มเพราะโนมิยะยังไม่มา ระหว่างนี้ฉันก็คอยเล่าความคิดฉันที่มีต่อยามากุให้รินฟัง"

# "I've tried to figure out what exactly about the school feels so special to me; that concept I unsuccessfully tried to explain to Yuuko the other day."
"ฉันเค้นสมองนึกหาว่าทำไมฉันถึงได้รู้สึกว่าโรงเรียนนี้พิเศษ เรื่องเดียวกันกับที่ฉันเล่าให้ยูโกะฟังเมื่อวันก่อนแต่ก็\nล้มเหลวไม่เป็นท่าไป"

# "It's still difficult, but the track meet and the time I've spent observing my fellow students have helped my ideas mature a little."
"ก็ยังยากอยู่ดีแหละ แต่พอได้มาดูงานแข่งกับจับสังเกตนักเรียนรอบ ๆ ตัวแล้วก็ช่วยให้คิดอะไรขึ้นมาได้บ้าง"

show rin basic_absent_close at center
with charaenter

# hi "Have you noticed that people talk all the time?"
hi "เธอเห็นมั้ยว่าทุกคนคุยกันตลอด"

# hi "I can't really explain it, but…"
hi "ไม่รู้จะว่ายังไงดีเหมือนกัน แต่…"

# "Once again, as I try to explain my observation, I'm struggling for words."
"เป็นอีกครั้งที่ฉันสรรหาคำบรรยายมาอธิบายข้อสังเกตของฉันไม่ได้"

# "The student body is heavily cliqued, and I'm only now beginning to make sense of the intricate grouping and popularity networks. And yet, the feeling of being a part of a group is stronger here than I remember it being in my old schools."
"นักเรียนเกาะกลุ่มกันอยู่เหนียวแน่นมาก ฉันเพิ่งจะมาพอดูออกตอนนี้เองว่าใครอยู่กับใครเกี่ยวกับใครบ้าง แต่เท่าที่ฉัน\nจำได้ ที่โรงเรียนเก่าไม่ได้มีความเป็นพรรคเป็นพวกกันเท่าที่นี่ขนาดนี้"

# hi "I'm trying to say that this school isn't like other schools. Or at least, the students aren't, even after discounting the obvious."
hi "ที่ฉันจะบอกคือว่าโรงเรียนนี้มันไม่เหมือนโรงเรียนอื่น ๆ น่ะ หรืออย่างน้อย ๆ ก็พวกนักเรียนแหละที่ดูต่าง ต่อให้\nหักจุดต่างที่ชัดแล้วก็เถอะ"

# hi "…Do you know what I mean?"
hi "…เธอพอจะเข้าใจที่ฉันพูดมั้ย"

show rin basic_deadpan_close
with charachange

# rin "I don't know what you mean."
rin "ฉันไม่เข้าใจสิ่งที่นายพูด"

# hi "Oh, well… whatever, then."
hi "เอ้อ เอ่อ… งั้นก็ ช่างเหอะ"

# "I want to pursue the issue, but at that point, Nomiya arrives."
"ฉันอยากจะไหลต่อ แต่โนมิยะก็มาแล้ว"

hide rin
with charaexit

show bg school_classroomart at left
with charamove

show nomiya smile at center
with charaenter

play music music_happiness fadein 2.0

# "The teacher is wiping sweat from his forehead with a handkerchief and breathing rather heavily. He quickly glances over the room, then settles down a bit."
"คุณครูใช้ผ้าเช็ดหน้าเช็ดเหงื่อพลางหายใจหอบแล้วกวาดตามองรอบห้องด้วยท่าทีที่ผ่อนคลายลง"

show nomiya veryhappy
with charachange

# no "Hello, hello; apologies for being late."
no "สวัสดี สวัสดี ขออภัยที่มาช้า"

show nomiya talk
with charachange

# no "Is everyone present? Good!"
no "อยู่กันครบนะ ดี!"

# no "I must confess, I haven't really planned anything for today as I have been extremely busy, lately. But I'm sure we can come up with something entertaining."
no "ต้องขอสารภาพว่าวันนี้ไม่ได้เตรียมอะไรมาเลยเพราะช่วงนี้ยุ่งมาก ๆ แต่เดี๋ยวนึกอะไรสนุก ๆ มาทำกันได้แน่นอน"

show nomiya frown
with charachange

# no "Anyone have any suggestions? I was thinking we could have a discussion circle since we haven't had one in a while. I, at least, found the last one magnificently enjoyable."
no "มีใครเสนออะไรมั้ย ฉันคิดอยู่ว่ามาล้อมวงอภิปรายกันดีมั้ยเพราะไม่ได้มาคุยกันสักพักแล้วเหมือนกัน ฉันคนหนึ่งละ\nที่คิดว่าแบบนี้แหละสนุกมากเลย"

# "There are some murmurs here and there, but nobody raises their voice in support of or against Nomiya."
"มีเสียงพึมพำงึมงำดังขึ้นมา แต่ไม่มีใครจะออกเสียงเห็นด้วยหรือคัดค้านโนมิยะ"

show nomiya talk
with charachange

# no "We could delve into various movements of art. Or does someone have a good topic in mind?"
no "ศิลปะแต่ละยุคก็เอามาคุยกันได้อีกยาวเลย หรือมีใครมีหัวข้อดี ๆ มั้ย"

# no "Come on, throw it out there. It doesn't matter if it's silly or odd, we can always cook up something interesting!"
no "น่า เสนอมาเลย จะฟังดูบ้า ๆ เพี้ยน ๆ ก็ไม่เป็นไร เดี๋ยวก็ทำให้น่าสนใจขึ้นมาได้!"

# "Nobody seems to be brave enough to make such a suggestion."
"ไม่มีใครอาจหาญพอจะเสนออะไร"

# "As the awkward silence refuses to be broken, I lift my hand in the air."
"ขณะที่ความเงียบยังคงดำเนินต่อนั้นฉันยกมือขึ้น"

show nomiya smile
with charachange

# no "Oho? Our newest friend seems to have something on his mind. Speak up, my boy, speak up!"
no "โอ้? เพื่อนคนใหม่ล่าสุดของเราดูท่าจะมีอะไรน่าสนใจละ พูดมาเลยลูก ๆ"

# hi "Um, well… I don't know about anyone else, but I've always wondered why art exists in the first place."
hi "เอ่อ คือ… ผมไม่รู้ว่าคนอื่นคิดยังไงนะครับ แต่ผมสงสัยมานานแล้วว่าศิลปะมีไว้ทำไม"

stop music fadeout 2.0

# "My voice trails off. A silence sets in the room, and nobody makes a followup on my meek suggestion."
"เสียงฉันค่อยลงเรื่อย ๆ ทั้งห้องยังคงเงียบไม่มีใครจะพูดต่อจากคำถามอันกระมิดกระเมี้ยนของฉัน"

# "Then, the teacher bursts in laughter."
"แล้วคุณครูก็ระเบิดหัวเราะออกมา"

show nomiya veryhappy
with charachange

# no "Hohoho, excellent!"
no "โฮ่โฮ่โฮ่ ยอดเยี่ยม!"

# no "Very good, very good indeed. Right out of the gate with the big one, huh?"
no "ดีมาก ดีมาก เปิดด้วยประเด็นใหญ่เลยงั้นเหรอ"

# no "Fabulous!"
no "แจ่มไปเลย!"

# "Chuckling, he shifts some papers around on his desk for a few moments. When he's done, he appears to have made some sort of decision."
"คุณครูแค่นหัวเราะพลางจับ ๆ กระดาษที่อยู่บนโต๊ะพักหนึ่ง หลังจากนั้นก็ทำท่าเหมือนตัดสินใจอะไรได้"

show nomiya smile
with charachange

# no "Very well, then. Let us run with this and see where it gets us, shall we?"
no "ถ้างั้นก็ เอาละ ไหนลองคุยกันเรื่องนี้แล้วดูว่าจะเป็นยังไงต่อ"

show nomiya talktongue
with charachange

# no "Oh my, even an old fogey like me gets excited when such delicious enthusiasm is present. Oh my, indeed."
no "ให้ตาย ช่างกระตือรือร้นได้อย่างน่าสนใจจนแม้แต่ตาลุงตกยุคอย่างฉันเห็นยังตื่นเต้นเลย จริง ๆ เลย"

show nomiya smile
with charachange

# no "Let me gather my thoughts a moment so I can figure out a good starting point for everyone."
no "ขอรวบรวมความคิดหาจุดตั้งต้นดี ๆ ที่ทุกคนฟังได้ก่อนสักพักนะ"

# "For some reason the teacher seems to be almost literally bursting with excitement. He scribbles a few things down on a loose sheet of paper, then cleans his glasses with the handkerchief."
"ไม่รู้ทำไม แต่คุณครูดูจะตื่นเต้นจนแทบตัวสั่น จากนั้นก็ขีด ๆ เขียน ๆ อะไรสองสามอย่างลงบนเศษกระดาษ\nก่อนจะใช้ผ้าเช็ดหน้าเช็ดแว่น"

show nomiya dreamy
with charachange

# "He strikes a pose, then freezes for an overtly dramatic, artistic pause that spans what must be half a minute."
"คุณครูเต๊ะท่าค้างไว้ให้ดูมีศิลปะอย่างเล่นใหญ่แบบเวอร์วังอยู่สักครึ่งนาทีได้"

# "It's so quiet I could hear a pin drop."
"ทั้งห้องก็เงียบเป็นเป่าสาก"

show nomiya talk
with charachange

play music music_another fadein 0.5

# no "First, let's come up with a few questions that we want answered, such as “What is art?” and “Why does art exist?”"
no "ก่อนอื่น เริ่มจากคำถามที่อยากรู้กันก่อนเนอะ อย่างเช่น “ศิลปะคืออะไร” และ “ศิลปะมีไว้ทำไม”"

show nomiya smile
with charachange

# no "Anyone have any questions that might be related?"
no "มีใครมีคำถามที่พอจะเกี่ยวกันบ้างมั้ย"

# "The boy with sunglasses pipes up almost immediately. His voice is soft and quiet, and I have a hard time making out what he says."
"ชายที่ใส่แว่นกันแดดโพล่งขึ้นมาแทบจะในทันที เสียงเขานั้นทั้งอ่อนและเบาจนฉันแทบฟังไม่รู้เรื่อง"

# "Sunglasses boy" "What defines an artist?"
thname("ชายใส่แว่นกันแดด") "ศิลปินคืออะไร"

# "After him, another question comes up."
"หลังจากนั้นก็มีอีกคำถาม"

# "Student" "If I fill a cardboard box with water and call it art, is it art?"
thname("นักเรียน") "ถ้าเติมน้ำใส่ลังกระดาษแล้วเรียกว่าเป็นศิลปะ มันจะเป็นศิลปะมั้ย"

show nomiya veryhappy
with charachange

# "Everyone laughs at that, even the teacher."
"ทุกคนหัวเราะ แม้แต่คุณครู"

# no "Great! Wonderful, all of these!"
no "เยี่ยม! สุดยอด ทุกคน!"

show nomiya talk
with charachange

# no "Let me start by saying that this is not a clear-cut issue by any means, and as such, I'm not going to give any answers to you. I'm only going to speak from my own perspective."
no "ขอเกริ่นก่อนว่าเรื่องนี้ไม่ได้มีข้อสรุปที่ชัดเจน ดังนั้น ฉันจะไม่ให้คำตอบอะไรกับพวกเธอ แต่ขอเล่าจากมุมของฉันเอง\nเท่านั้น"

# no "Scholars have argued about these sorts of questions since time immemorial, and there has never really been a broadly applicable consensus reached."
no "เหล่านักวิชาการต่างถกประเด็นนี้กันมานานแสนนานมากแล้ว แล้วก็ไม่มีข้อตกลงที่เป็นที่ยอมรับเป็นวงกว้างสักเท่าไหร่"

show nomiya smile
with charachange

# no "There are, however, some qualities that most tend to generally agree upon. Hopefully, you all should find these acceptable as well."
no "แต่ จะมีคุณสมบัติบางอย่างที่คนส่วนใหญ่มักจะเห็นด้วย หวังว่าพวกเธอก็จะเห็นด้วยเช่นกันนะ"

show nomiya dreamy
with charachange

# no "In short, art defines itself. It simply cannot be contained to a definition from the outside, since the boundaries of art expand and contract from forces within."
no "สั้น ๆ ก็คือ ศิลปะนิยามตัวของมันเอง ไม่มีคำนิยามอย่างอื่นอะไรที่จะมานิยามศิลปะได้ เพราะขอบเขตของศิลปะนั้น\nจะขยายออกหรือหดเข้าด้วยแรงภายในตัวมันเอง"

show nomiya serious
with charachange

# no "Every day, someone somewhere comes up with something completely outrageous that challenges any and all preconceptions."
no "ทุก ๆ วันจะมีสักคนที่คิดทำอะไรที่ท้าทายความคิดเดิม ๆ ทั้งหมดที่เคยมีมาก่อน"

show nomiya frown
with charachange

# no "The core reason for this is that rather than the rational side of the mind, art appeals to the intuition, the instinct, the primal. You would find it very hard to explain why exactly it is that you enjoy some particular style or piece, no?"
no "เหตุผลหลัก ๆ ที่มันเป็นอย่างนี้ก็เพราะว่าศิลปะนั้นจะเข้ากับด้านสัญชาตญาณ ความรู้สึกที่รู้ได้เอง ความรู้สึก\nที่โผล่ขึ้นมาก่อนได้ดีกว่าด้านตรรกะ จะให้บอกว่าทำไมถึงได้ชอบงานศิลปะหรือลายเส้นแบบหนึ่ง ๆ\nก็คงยากมากใช่มั้ยล่ะ"

# "He doesn't wait for a response before continuing."
"คุณครูไม่รอเสียงตอบรับแล้วพูดต่อ"

show nomiya veryhappy
with charachange

# no "This is exactly why."
no "นั่นแหละคือเหตุผล"

show nomiya frown
with charachange

# no "So, art is this sort of wild, uncontrollable thing that lurks somewhere deep in our subconscious. Now, why does it exist?"
no "เพราะงั้น ศิลปะถึงได้เป็นอย่างสิ่งดิบเถื่อนและควบคุมไม่ได้อย่างหนึ่งที่ซุกซ่อนอยู่สักที่ในจิตใต้สำนึก ทีนี้ ศิลปะมีไว้\nทำไม"

# "Nomiya apparently expects someone to pipe up with a guess, but as nobody dares to interrupt his inspired speech, he continues."
"โนมิยะเหมือนจะคาดหวังให้ใครเดาก่อน แต่ในเมื่อไม่มีใครกล้าขัดการบรรยายอันเปี่ยมพลังเขาก็พูดต่อ"

show nomiya dreamy
with charachange

# no "It was a trick question! You see, art also validates itself."
no "เป็นคำถามหลอกหรอกนะ! นี่ไง ศิลปะมันก็ทำให้ตัวตนของมันมีความหมายด้วยตัวมันเองอยู่แล้ว"

show nomiya talk
with charachange

# no "Generally speaking, you might say that art exists for no other purpose than itself. It's something that exists merely to leave a mark in history."
no "ถ้าพูดแบบรวม ๆ ก็บอกได้ว่าศิลปะนั้นมีไว้ก็เพื่อตัวมันเองเท่านั้น เป็นสิ่งที่มีตัวตนเพียงเพื่อฝากรอยไว้ในหน้า\nประวัติศาสตร์"

show nomiya serious
with charachange

# no "It's the defiance of a mortal against the face of darkness, as was once said. Art is truly the proof of our existence. You all should know that human culture and civilization are tightly tied to the existence of art."
no "อย่างที่เคยมีคนพูดไว้ว่าศิลปะเป็นสิ่งแสดงถึงความรั้นของมนุษย์ที่ต้องเผชิญกับความมืดมิด ศิลปะคือหลักฐานถึงตัวตน\nของพวกเรา พวกเธอก็ควรรู้ไว้ว่าวัฒนธรรมและอารยธรรมของมนุษย์นั้นต่างสัมพันธ์กันกับการมีอยู่ของศิลปะ\nอย่างแน่นแฟ้น"

show nomiya frown
with charachange

# no "Then, what about artists? What drives a man to dedicate his life to a thing so fickle and mysterious that it even defies definition?"
no "ทีนี้ แล้วศิลปินล่ะ อะไรทำให้คน ๆ หนึ่งอุทิศชีวิตให้กับสิ่งที่แสนจะปรวนแปรและลึกลับที่ไม่อาจมีอะไรมานิยามได้ด้วยซ้ำ"

show nomiya serious
with charachange

# no "There are as many answers for this as there are artists, but if I had to put it into words… an artist doesn't make art because he can, but because he must."
no "จำนวนคำตอบก็มีเท่าจำนวนศิลปินที่มีอยู่เลยนั่นแหละ แต่ถ้าให้พูด… ศิลปินสร้างสรรค์ศิลปะไม่ใช่เพราะว่าทำได้\nแต่เพราะต้องทำ"

# "Nomiya takes a pause, and his gaze sweeps over his audience, eyes flaring with passion."
"โนมิยะหยุดไปครู่หนึ่ง สายตากวาดมองผู้ฟังด้วยแววตาที่ฉายความคลั่งไคล้"

show nomiya frown
with charachange

# no "It is obvious that art touches the very soul of each and every human being in one way or another. So, if you were given a chance to connect with your fellow man in such a fundamental way, how could you not?"
no "เห็นได้ชัดว่าศิลปะนั้นเข้าถึงจิตวิญญาณของมนุษย์ทุกผู้ทุกคนไม่ทางใดก็ทางหนึ่ง เพราะงั้น ในเมื่อมีโอกาสที่จะได้\nเชื่อมต่อกับมนุษย์ด้วยกันได้อย่างถึงแก่นอย่างนี้แล้ว จะให้อดใจยังไงไหวล่ะ"

show nomiya talk
with charachange

# no "There is a poem I'm very much fond of, and I shall recite the most well-known part of it to you now. I feel that, for me personally, of all possible things it captures best the essence of what it means to be an artist."
no "มีกลอนหนึ่งที่ฉันชอบมาก เดี๋ยวจะท่องบทส่วนที่คนเห็นบ่อย ๆ ให้ฟัง ส่วนตัวฉันรู้สึกว่ากลอนนี้เป็นอะไรที่รวบรวม\nแก่นแท้ของความเป็นศิลปินไว้ได้ดีที่สุดแล้ว"

stop music fadeout 2.5

# "Nomiya leans against the desk as he clears his throat in preparation."
"โนมิยะเอนตัวพิงกับโต๊ะแล้วกระแอมไอเตรียมการ"

# "Looking at some distant place, he utters the words in the heavy afternoon air with his soft basso voice."
"สายตาคุณครูทอดมองสักที่แสนไกล คำพรั่งพรูออกมาด้วยเสียงทุ้มต่ำลอยอยู่ในอากาศอันอบอ้าวยามบ่าย"

show nomiya dreamy
with charachange

play music music_one fadein 0.5

# no "To see a world in a grain of sand"
no "ทรายหนึ่งเทียบแผ่นหล้า ท่านเพียร สรรหา"

# extend "\nAnd a heaven in a wild flower,"
extend "\nฤๅดอกบุบผาเขียน แผ่นฟ้า"

# no "Hold infinity in the palm of your hand"
no "ท่านจับสิ่งล้นเจียน ในฝ่า มือกำ"

# extend "\nAnd eternity in an hour."
extend "\nไหลบ่านิรันดร์ค่า ชั่วสิ้น หนึ่งยาม"
#William Blake (1757-1827), "Auguries of Innocence". Should poetic capitalization be deemed better, here it is:
#To see a World in a Grain of Sand
#And a Heaven in a Wild Flower,
#Hold Infinity in the palm of your hand
#And Eternity in an hour.

# "There is a solemn and unbelievably awkward silence after he finishes reciting the short fragment. Nobody dares speak a word."
"พอท่องบทสั้น ๆ นั้นจบแล้วก็มีความเงียบขรึมที่ชวนให้อึดอัดเหลือเชื่อตามมา ไม่มีใครกล้าพูดอะไร"

# "Nomiya clears his throat again."
"โนมิยะกระแอมอีกครั้ง"

show nomiya talk
with charachange

# no "To be an artist is to see the world in a grain of sand."
no "การเป็นศิลปินคือการมองโลกให้อยู่ในเม็ดทรายได้"

show nomiya dreamy
with charachange

# no "You see, dear children, without art, there would not be much to live for in this world. It is a most profound thing."
no "นี่นะ พวกเธอ ถ้าไม่มีศิลปะ โลกนี้ก็คงไม่มีอะไรให้ยึดถือมากแล้ว เป็นสิ่งที่ล้ำลึกที่สุดเลยละ"

# "He is clearly touched by this notion. I almost expect to see a lone tear rolling down his rough cheek, but it never comes."
"คุณครูซาบซึ้งไปกับความคิดนั้นมาก เล่นเอาเสียจนนึกว่าจะมีน้ำตาไหลย้อยออกมาประกอบด้วยเลย แต่ก็ไม่มีสักหยด"

show rin invis at offscreenright
with None

show nomiya invis at twoleft
show bg school_classroomart at bgleft
show rin basic_awayabsent_close:
    xpos 0.9 xanchor 0.5
with dissolvecharamove

hide nomiya
with None

# "I turn to Rin and whisper to her."
"ฉันหันหน้าไปกระซิบกระซาบกับริน"

# hi "So how is this a discussion circle?"
hi "แล้วนี่มันเรียกว่าล้อมวงอภิปรายยังไง"

# "She shrugs nonchalantly back at me."
"เธอยักไหล่ไม่ยี่หระตอบ"

show rin basic_deadpan_close
with charachange

# rin "The previous ones were the same."
rin "คราวที่แล้วก็งี้"

# "To his credit, Nomiya does try to get some debate going, but the club seems to be reluctant to comply."
"แต่จะว่าขนาดนั้นก็ไม่ได้ โนมิยะเองก็กระตุ้นให้มีการถกประเด็นกันบ้างแล้ว แต่คนในชมรมดูจะไม่ค่อยอยากตอบกัน"

# "I feel a bit guilty about opening my mouth. Maybe we would've been spared from this."
"รู้สึกผิดขึ้นมาหน่อย ๆ ที่ฉันพลั้งปากไปอย่างนั้น ไม่งั้นอาจจะรอดแล้วก็ได้"

stop music fadeout 1.5

show rin basic_awayabsent_close
with shorttimeskip

play music music_normal fadein 2.0

# "As the meeting comes to a close, I realize we haven't once touched any paint or pens today, and I feel somewhat disappointed."
"พอชมรมใกล้เลิกก็ถึงนึกขึ้นได้ว่าวันนี้ยังไม่ได้จับสีจับปากกากันเลย แอบผิดหวังหน่อย ๆ แฮะ"

show nomiya smile at twoleft
with charaenter

# "Nomiya suddenly appears next to us. He seems to be still fired up from the speech he delivered."
"จู่ ๆ โนมิยะก็โผล่มาอยู่ข้างพวกเราด้วยท่าทีที่ยังดูร้อนแรงกับบทบรรยายที่เพิ่งเล่าไป"

# "His cologne smells musky and saccharine at the same time, giving me an instant headache, even though I'm not sensitive to perfumes. He is looking at Rin like a hungry wolf."
"กลิ่นโคโลญของคุณครูนั้นทั้งเหม็นสาบอย่างสัตว์และน้ำตาลจนฉันปวดหัวจี๊ด นี่ขนาดว่าฉันไม่ได้แหวะน้ำหอม\nขนาดนั้นนะ สายตาที่มองรินดูอย่างหมาป่าที่หิวโหย"

show nomiya talk
with charachange

# no "Tezuka, do you remember Mrs. Saionji, who visited us at the festival?"
no "เทซูกะ เธอจำคุณนายไซอนจิที่มาหาตอนงานเทศกาลได้มั้ย"

show rin basic_deadpannormal_close
with charachange

# rin "I think so."
rin "น่าจะนะคะ"

show nomiya veryhappy
with charachange

# no "I'm going to tell you something amazing."
no "ฉันมีอะไรดี ๆ จะบอก"

show nomiya smile
with charachange

# no "The thing is, she's a very well-known gallerist around here. It turns out I might be able to get her to consider having some of your work put on display."
no "เรื่องคือ คุณนายไซอนจิเธอเป็นเจ้าของหอศิลป์ที่ดังในละแวกนี้มาก ฉันอาจจะพอเสนองานของเธอไปจัดแสดงด้วย\nได้นะ"

# "He ends his sentence with a dramatic gesture. It seems he's expecting Rin to show some sort of joyous, shocked reaction at such grand news, but she just stares at him blankly."
"คุณครูปิดท้ายประโยคด้วยท่าทางเวอร์วัง ดูท่าว่าจะคาดหวังให้รินทำท่ายินดีและตกใจที่ได้ฟังข่าวใหญ่ขนาดนี้\nทว่ารินมองกลับด้วยสีหน้าเรียบนิ่ง"

show nomiya veryhappy
with charachange

# no "Magnificent, isn't it? This could be a real chance for us to get ahead, girl."
no "สุดยอดไปเลยใช่มั้ยล่ะ นี่อาจจะเป็นโอกาสที่เธอจะได้ก้าวหน้าก็ได้นะ"

show rin basic_surprised_close
with charachange

# rin "But…"
rin "แต่ว่า…"

show nomiya frown
with charachange

# no "Now now, I know what you're about to say. Yes, it wouldn't be a simple affair, but I think this is an absolutely fantastic opportunity."
no "เอาละ ๆ ฉันรู้ว่าเธอจะพูดอะไรต่อ ถูก เรื่องจะวุ่นวายหน่อย แต่นี่แหละคือโอกาสอันยอดเยี่ยม"

# no "Frankly, I wouldn't be surprised at all if we even made it big! This could be the first step! And then, when the word is out, we strike while the iron is hot! Right, Nakai?"
no "เอาตรง ๆ ถ้าทำจนประสบความสำเร็จแบบถล่มทลายได้ฉันก็จะไม่แปลกใจเลย! นี่แหละก้าวแรก! แล้วพอเริ่มดัง\nก็จะใช้โอกาสนี้แหละตีเหล็กตอนร้อน ๆ ไปเลย! ใช่มั้ย นากาอิ"

# hi "Er, yeah, it does sound pretty great. If you're into that kind of thing."
hi "เอ้อ ครับ ก็ฟังดูดี ถ้าชอบน่ะนะครับ"

show nomiya veryhappy
with charachange

# no "See? We should definitely not let this one pass, am I right?"
no "เห็นมั้ย เราไม่ควรปล่อยโอกาสนี้ไปนะ ว่างั้นมั้ยล่ะ"

show rin negative_confused_close
with charachange

# rin "I don't… really."
rin "ไม่ว่างั้น… เท่าไหร่ค่ะ"

stop music fadeout 7.0

# "Rin seems to be troubled for some reason. I can't figure out why. What Nomiya is saying does indeed sound like a possibly great thing."
"รินดูอึดอัดใจขึ้นมา ฉันไม่รู้ว่าทำไม เพราะสิ่งที่โนมิยะพูดนั้นก็ฟังดูจะเป็นเรื่องที่ดีจริง ๆ"

# "She looks pretty down though, and confused. I've never seen her like this."
"แต่เธอดูเครียดและสับสน ฉันไม่เคยเห็นเธอเป็นอย่างนี้เลย"

show nomiya talk
with charachange

# no "So, what do you think?"
no "แล้ว ว่าไงล่ะ"

# "Rin looks up to her teacher's glowing face, then back down at her desk."
"เธอเงยหน้ามามองหน้าอันเปล่งประกายของคุณครูแล้วก้มมองโต๊ะตัวเอง"

show rin negative_worried_close
with charachange

# rin "I'll think about it."
rin "จะเก็บไปคิดค่ะ"

# "Nomiya is at last taken slightly aback by Rin's lack of superlative delight. Then he smiles widely at her and gently pats her head."
"ในที่สุดโนมิยะก็ดูรู้สึกตกใจเล็กน้อยกับท่าทีที่ไม่สบอารมณ์มากนักของรินเสียที จากนั้นก็ยิ้มกว้างให้เธอแล้วลูบหัวเบา ๆ"

show nomiya smile
with charachange

# no "Good girl."
no "เด็กดี"

hide rin
hide nomiya
with charaexit

# "The club meeting is finally over, and as I lazily collect my things and help clean up, I start feeling exhausted, for some reason. There isn't much to do, however, so it's over quickly."
"ชมรมเลิกแล้ว อยู่ ๆ ฉันก็รู้สึกหมดแรงขึ้นมาระหว่างที่กำลังเก็บข้าวของอย่างเอื่อยเฉื่อยและช่วยเก็บกวาดห้อง\nแต่ก็ไม่ได้มีอะไรให้ทำมากมาย ไม่นานก็เสร็จ"


#*******************************************


label th_R9:

scene bg school_staircase2
show rin negative_spaciness_close at tworight
with locationskip

# "I catch up to Rin who left the club room just a moment earlier, so we're walking down the stairs to the ground floor while I try to go over Nomiya's passionate speech about art, and Rin seems to be lost in thought."
"ฉันตามรินที่เพิ่งออกจากห้องมาก่อนหน้าไม่นาน พวกเราเดินไปตามบันไดไปยังชั้นหนึ่ง ระหว่างนั้นฉันก็คิดเรื่อง\nบทสาธยายอันเปี่ยมพลังของโนมิยะ ส่วนรินก็ดูครุ่นคิดบางอย่าง"

# "Not an unusual state for her, I've learned, but something about her expression makes me feel uneasy."
"ฉันรู้ว่าสภาพนี้ไม่ใช่อะไรที่แปลกสำหรับเธอ แต่สีหน้าของเธอทำให้ฉันอึดอัดชอบกล"

# hi "Penny for your thoughts."
hi "คิดมากอะไรอยู่หรือเปล่า"

show rin basic_deadpancontemplation_close
with charachange

# rin "That'd be too cheap."
rin "หมายถึงว่ามีจำนวนความคิดมากน่ะเหรอ"

# hi "You're just overpricing your thoughts."
hi "อันนั้นมันคิดเยอะหรือเปล่า"

show rin basic_lucid_close
with charachange

# rin "I wouldn't be able to sell them anyway. I'm not sure what I'm thinking yet. That'd be fraud too, like stealing a candy from a baby."
rin "แต่เอาเถอะ มีมากมีน้อยก็เอาไปขายไม่ได้อยู่ดี ฉันยังไม่แน่ใจเลยว่าคิดอะไรอยู่ เอาไปขายก็เข้าข่ายต้มตุ๋นอีก\nเหมือนแย่งลูกอมมาจากเด็ก"

# hi "That's theft, not fraud."
hi "อันนั้นเขาเรียกโจรกรรม ไม่ใช่ต้มตุ๋น"

show rin basic_deadpanupset_close
with charachange

# rin "I have to think about what I think."
rin "ฉันต้องคิดเรื่องที่ตัวเองคิดบ้างแล้ว"

# hi "Is this about what the teacher said? Getting your work put on display and all that?"
hi "เรื่องที่คุณครูพูดหรือเปล่า ที่ว่าจะเอางานไปจัดแสดงอะไรนั่นน่ะ"

scene bg school_lobby
with locationchange

# "She doesn't answer, but stops in her tracks as we reach the lobby."
"เธอไม่ตอบ แต่เท้าเธอชะงักกลางทางระหว่างที่กำลังเดินไปโถงใหญ่"

# "We're the only people around, so it's very quiet. Footsteps echo from a few floors up as someone hurries along a hallway."
"รอบตัวเราไม่มีใครจนเงียบสงัด มีเสียงฝีเท้าจากชั้นบน ๆ ที่มีคนวิ่งตามโถงทางเดินอยู่"

show rin negative_annoyed at center
with charaenter

# rin "I think I'm going to go somewhere elsewhere."
rin "ฉันคิดอยู่ว่าจะไปที่อื่นสักที่"

# "I think she really is troubled."
"คงจะอึดอัดจริง ๆ นั่นแหละ"

# hi "Want company?"
hi "ให้ไปด้วยมั้ย"

# hi "I can't promise much help with the thinking, but it's not like I have much else to do, and I'm supposed to do some light exercise."
hi "ฉันอาจจะช่วยคิดอะไรได้ไม่มาก แต่ฉันก็ไม่มีอะไรทำแล้วแหละ แล้วก็ต้องไปออกกำลังกายเบา ๆ ด้วย"

show rin basic_absent
with charachange

# rin "If you like."
rin "ถ้าอยาก"

play ambient sfx_parkambience fadein 20.0

scene bg school_backexit
with locationskip

# "Rin leads me outside, to the wall behind the dormitories. There is a small back gate there, made from the same wrought iron as the main gate. It leads to the shadowy woodland park behind the school."
"รินนำทางไปทางกำแพงที่อยู่หลังหอที่มีประตูทำจากเหล็กดัดอิตาลีอย่างเดียวกับประตูหน้าโรงเรียนอยู่ ทางเดินนั้น\nทอดไปยังสวนป่าทึบที่อยู่หลังโรงเรียน"

# "The gate is rusty, as if it hasn't seen much use. However, it sits open, so we pass through. It's not forbidden for students to leave the grounds, but somehow I feel a little uneasy."
"ตามประตูมีสนิมเขรอะราวไม่ได้ใช้มานานแล้ว แต่บานประตูนั้นเปิดไว้อยู่พวกเราจึงเดินผ่านไป ถึงจะไม่มีกฎ\nห้ามนักเรียนออกจากโรงเรียนก็เถอะ แต่ก็รู้สึกไม่สบายใจหน่อย ๆ"

scene bg school_forest1
with locationchange

# "A path leads deeper into the forest. Tall zelkova and maple trees rustle in the wind, their canopies creating patches of chill air hanging in the places where the shadows fall."
"ทางเดินนั้นทอดไปตามป่าลึกเข้าไปอีก สายลมเสียดสีกับใบของต้นเซลโควาและต้นเมเปิลที่สูงโปร่ง ใบไม้เหล่านั้น\nที่ปกคลุมก่ออากาศเย็นขึ้นตรงจุดที่มีร่มเงา"

# "The forest smells strongly of earth. I almost feel cold, even though the midsummer day is as hot as ever."
"กลิ่นดินในป่าแรงเตะจมูก รู้สึกเย็น ๆ ขึ้นมาแม้วันนี้จะยังเป็นวันอันร้อนระอุอย่างวันกลางฤดูร้อนตามปกติ"

# "Rin trudges ahead like a sleepwalker, surefooted but with no apparent destination in mind. Her thoughts seem to be somewhere else. I follow a few steps behind, taking more care to watch where my feet land."
"รินย่ำเท้าเดินหน้าไปอย่างคนละเมอ แต่ละก้าวนั้นมั่นคงทว่ายังดูไร้จุดหมาย ใจเธอคงจะไปอยู่ที่อื่น ฉันตามหลัง\nอยู่ไม่ไกลพลางระวังแต่ละก้าวเดิน"

# "The path follows the land uphill at a low angle, sometimes making little detours downhill before climbing back upward. The muted brown and gray trunks line the path on both sides, peppered with ferns and other undergrowth."
"ทางนั้นขึ้นเนินชันเล็กน้อย บางจังหวะก็มีอ้อมลงเนินมาก่อนจะกลับขึ้นเนิน ตามสองข้างทางมีขอนไม้สีน้ำตาลตุ่น ๆ\nและสีเทาที่มีพวกเฟิร์นและไม้พื้นล่างประดับอยู่"

scene bg school_forest2
with locationchange

# "After a little while, I start getting worried. The path is still wide and clear, so there's no chance of getting lost, but it doesn't look like we have any particular destination."
"พอเดินได้อีกไม่นานฉันก็เริ่มคิดหนัก ทางเดินก็ยังกว้างเห็นได้ชัดอยู่ เพราะงั้นไม่มีทางหลงแน่ ๆ แต่เหมือนจะยัง\nไม่มีจุดหมายปลายทางเลย"

# "There's nothing wrong with a bit of aimless wandering around, but I don't want to go so far that I get too tired to walk back."
"เดินเล่นทอดน่องสักหน่อยก็ไม่เป็นไรหรอก แต่ฉันไม่อยากไปไกลเกินจนเหนื่อยเดินกลับไม่ไหว"

scene bg school_forestclearing
with locationchange

# "I'm starting to get a little winded and my legs feel heavy. I want to stop and get a chance to catch my breath and rest my legs, but Rin keeps on going."
"ลมหายใจชักหอบถี่ ขาก็ชักจะหนัก อยากแวะนั่งลงพักขาพักหายใจก่อน แต่รินก็ยังเดินต่อ"

# hi "Where are we going? Or are we going anywhere at all?"
hi "นี่จะไปไหนเนี่ย มีเป้าหมายหรือเปล่าเถอะ"

show rin basic_deadpan at center
with charaenter

# rin "Worry Tree."
rin "ต้นทุกข์"

# hi "I see."
hi "อ้อ"

# hi "So what exactly is the Worry Tree?"
hi "แล้วต้นทุกข์ที่ว่านี่คืออะไร"

show rin negative_spaciness
with charachange

# rin "It's just a tree. Like this."
rin "ก็ต้นไม้ แบบนี้"

# "She stops in front of a particularly large maple that might or might not be the Worry Tree. Its lush green leaves sway lightly in the breeze blowing through the small clearing we entered."
"เธอหยุดยืนอยู่ตรงหน้าต้นเมเปิลต้นใหญ่ต้นหนึ่งที่อาจจะใช่หรือไม่ใช่ต้นทุกข์ ใบอันเขียวชอุ่มของมันพลิ้วไหว\nตามสายลมโชยที่พัดผ่านมาทางรอยแยกเล็ก ๆ ที่พวกเราแหวกเข้ามา"

# hi "I guessed as much."
hi "ก็รู้อยู่"

show rin basic_deadpanupset
with charachange

# rin "There are people who believe that you must come here to wallow in misery, if you are miserable, only by “people” I mean me, and the tree isn't really called anything."
rin "เขาเชื่อว่าเวลาทุกข์ใจให้มาคร่ำครวญที่นี่ “เขา” ที่ว่าหมายถึงแค่ฉันนะ แล้วต้นไม้ต้นนี้ก็ไม่ได้มีชื่ออะไรด้วย"

# hi "So… if you're miserable, you talk to a tree about it?"
hi "แปลว่า… ถ้าเธอทุกข์ใจ ก็จะมาคุยกับต้นไม้?"

show rin basic_deadpan
with charachange

# rin "No. What? You can't talk to trees. What do you think I am, crazy?"
rin "ไม่สิ อะไร คนเราคุยกับต้นไม้ได้ที่ไหน นี่คิดว่าฉันบ้าเหรอ"

# hi "No… I didn't mean it like that."
hi "เปล่า… ไม่ได้หมายความอย่างนั้น"

show rin basic_lucid
with charachange

# rin "Or maybe you talk to trees? I'm sorry, I didn't mean to say that you are crazy. Even though you probably are if you talk to trees."
rin "หรือนายคุยกับต้นไม้ ขอโทษทีนะ ไม่ได้ตั้งใจจะว่านายบ้า แต่ถ้าคุยกับต้นไม้ก็บ้าจริงแหละ"

show rin negative_confused
with charachange

# rin "I wouldn't recommend it in either case. People will think you are a weird person."
rin "แต่จะยังไงฉันก็ขอไม่แนะนำอยู่ดี เดี๋ยวคนมองว่าเพี้ยน"

# hi "No, I… just forget it."
hi "ไม่ คือฉัน… เออช่าง ลืม ๆ ไปเหอะ"

# "She looks mildly confused, for which I don't blame her at all. She tilts her head a little to the side, expression melting back to her usual one."
"เธอดูงง ๆ ซึ่งก็ว่าเธอไม่ได้หรอก เธอเอียงคอเล็กน้อยพลางกลับมาทำหน้าอย่างเดิม"

show rin basic_absent
with charachange

# rin "All right. I'm good at forgetting things."
rin "ได้เลย ฉันลืมเก่ง"

# hi "So why are we here? Are you miserable then?"
hi "แล้วมาที่นี่กันทำไม เธอทุกข์ใจอยู่เหรอ"

# "I can't read the expression she makes. I hate how bad I am at interpreting Rin's mood."
"ฉันดูอารมณ์ด้วยสีหน้าเธอไม่ออก เกลียดตัวเองเหลือเกินที่ดูอารมณ์รินไม่เก่งอย่างนี้"

show rin negative_worried
with charachange

# "She doesn't answer right away, as if she herself isn't quite certain of her own mood. The blank stare changes into a more difficult expression as she shuffles her weight around."
"เธอไม่ตอบในทันทีคล้ายว่ายังลังเลอยู่ว่ารู้สึกยังไง หน้าตายของเธอค่อย ๆ เคร่งขึ้นระหว่างที่เธอกำลังโยกตัวไปมา"

show rin basic_deadpancontemplation
with charachange

# "Finally, coming to a conclusion, Rin shrugs her shoulders. I've grown to seriously dislike that gesture. It doesn't mean anything."
"ในที่สุดรินก็ได้ข้อสรุปแล้วยักไหล่ ฉันรู้สึกไม่ชอบท่านั้นขึ้นมาจริง ๆ แล้ว เพราะมันไม่ได้มีความหมายอะไรเลย"

show rin basic_deadpanupset
with charachange

# rin "Maybe. I just feel kind of like I'm sinking underwater. I don't know what I should do."
rin "มั้งนะ แค่รู้สึกเหมือนกำลังจมน้ำอยู่ ไม่รู้ว่าต้องทำยังไง"

show rin negative_confused
with charachange

# rin "I don't know where I should go, that's all. Maybe it's not a big deal but I thought walking might help. Kind of like, if I go somewhere I would know where I should go. I don't really know if it did."
rin "ฉันไม่รู้ว่าจะไปไหนดี แค่นั้นแหละ อาจจะไม่ใช่อะไรมากมาย แต่คิดว่าเดินหน่อยก็คงพอช่วยได้ ประมาณว่าแบบ\nถ้าฉันไปสักที่ฉันก็ต้องรู้ว่าจะไปทางไหน ฉันไม่แน่ใจว่าช่วยได้จริง ๆ หรือเปล่านะ"

show rin negative_worried
with charachange

# rin "It really would've made sense if walking had helped to decide where to go."
rin "ถ้าเดินแล้วนึกว่าไปไหนดีขึ้นมาได้ก็คงสมเหตุสมผลดี"

# hi "So you don't want to try to get an exhibition? Or rather, you don't know if you do? Can't decide?"
hi "แล้วเธอไม่อยากลองจัดแสดงนิทรรศการเหรอ หรือยังไม่รู้ว่าอยากหรือเปล่า ตัดสินใจไม่ได้งี้"

# "Rin doesn't say anything for a while, arranging her thoughts in silence. The quiet is broken by birdsong from somewhere in the treetops, followed by rustling leaves as the bird takes flight."
"เธอไม่พูดอะไรอยู่พักหนึ่งคอยจัดความคิดตัวเองอยู่เงียบ ๆ เสียงที่แทรกเข้ามาเป็นเสียงนกร้องที่อยู่สักที่บนต้นไม้\nตามด้วยเสียงกรอบแกรบของใบไม้จากนกที่บินออกไป"

show rin basic_awayabsent
with charachange

# rin "Maybe. I'm not sure if I can have a thing like that. So far I've only painted for myself."
rin "มั้งนะ ฉันไม่แน่ใจว่าฉันจะทำอะไรแบบนั้นได้หรือเปล่า ที่ผ่านมาฉันวาดรูปเพื่อตัวเองมาตลอด"

show rin basic_absent
with charachange

# rin "I don't think I could have my things on display the way I am now. This me couldn't do it."
rin "ฉันคิดว่าถ้าฉันยังอยู่ในสภาพนี้ก็เอาอะไรไปให้ใครดูไม่ได้หรอก ตัวฉันตอนนี้ทำไม่ได้"

# "Her reason sounds like a weak excuse. I make my trademark frown but she doesn't notice it."
"เหตุผลของเธอฟังดูเหมือนข้ออ้างห่วย ๆ ฉันขมวดคิ้วอย่างที่ฉันทำประจำ แต่เธอก็ไม่ทันสังเกต"

# hi "I don't get it. The teacher certainly thinks you could. I don't think he'd suggest it otherwise. Sounds like he's calling in favors from his friends, too."
hi "ไม่เข้าใจ ก็คุณครูคิดว่าเธอทำได้ ไม่งั้นก็คงไม่เสนอมาหรอก เหมือนเพื่อนครูคนที่ว่าคนนั้นฝากมาชวนเธอเองด้วยซ้ำ"

show rin relaxed_nonchalant
with charachange

# rin "I know. He's really done a lot for me. But this might be too much."
rin "รู้ ครูเขาก็ทำเพื่อฉันมาเยอะ แต่คราวนี้อาจจะมากไปหน่อย"

show rin negative_confused
with charachange

# rin "Becoming someone who can do it might be pretty hard. Maybe I couldn't do it at all. He can't do it for me and if I let him try, I'd just sink deeper and deeper."
rin "การจะเป็นใครสักคนที่ทำอย่างนั้นได้น่ะค่อนข้างยากนะ ฉันอาจจะทำไม่ได้เลยด้วยซ้ำ คุณครูทำให้ฉันไม่ได้หรอก\nแล้วถ้าให้เขาได้ลอง ฉันมีแต่จะยิ่งจมดิ่งลึกลงไปเรื่อย ๆ"

# "Rin stands in front of the large maple and turns away from me. I want to close the few feet of distance between us and… I don't know. My irritation is suddenly gone, and I start feeling sympathetic to her."
"รินหันหลังให้ฉันยืนอยู่หน้าต้นเมเปิล อยากจะขยับเข้าไปใกล้อีกหน่อย แล้วก็… ไม่รู้สิ อยู่ ๆ ก็หายหงุดหงิดจนเริ่ม\nเห็นใจเธอขึ้นมาแล้ว"

# hi "I know exactly how you feel."
hi "ฉันเข้าใจดีนะ"

# hi "Well, maybe I don't, but still."
hi "อืม อาจจะไม่หรอก แต่ก็นะ"

# hi "I think I haven't felt like I was actually in control of my own life this whole year. I'm just helplessly going along with the flow."
hi "ปีนี้ทั้งปีเหมือนฉันทำอะไรกับชีวิตตัวเองไม่ได้เลย ได้แต่ปล่อยให้ตัวเองไหลตามน้ำไปเรื่อย ๆ โดยที่ทำอะไร\nไม่ได้เลย"

# hi "Like coming here to this school. I didn't really choose it myself. And I certainly didn't choose this time of my life to learn that I have… this condition."
hi "อย่างที่ได้มาโรงเรียนนี้ ฉันก็ไม่ได้เป็นคนเลือกที่จะมาเอง แล้วก็แน่นอนว่าฉันไม่ได้เลือกจังหวะนี้ในชีวิตฉันที่จะมารู้\nว่าฉัน… เป็นโรคนี้"

# "I still can't casually say the word aloud."
"ฉันยังพูดคำนั้นออกมาแบบชัด ๆ สบาย ๆ ไม่ได้"

# hi "It's like… yeah, it's exactly like being underwater. Like I can't even breathe."
hi "เหมือน… อืม เหมือนจมน้ำอยู่นั่นแหละ เหมือนหายใจไม่ออก"

show rin basic_sad
with charachange

# "Rin turns to face me again, a sad expression on her face."
"รินหันหน้ามามองฉันอีกครั้งทำหน้าเศร้า"

# rin "Is that why you look so sad all the time? I don't want to look sad like you. Do I look to you like you look to me?"
rin "เนี่ยเหรอนายถึงได้ดูเศร้าตลอด ฉันไม่อยากดูเศร้าเหมือนนาย นายเห็นฉันเหมือนที่ฉันเห็นนายมั้ย"

# hi "I don't look sad all the time."
hi "ฉันไม่ได้เศร้าตลอดสักหน่อย"

# hi "I just… don't know what I should be feeling. What kind of face I should be making."
hi "ฉันแค่… ไม่รู้ว่าจะต้องรู้สึกยังไง จะต้องทำหน้าแบบไหน"

show rin basic_upset
with charachange

# rin "Me neither. Do I look sad now?"
rin "ฉันก็ไม่ ตอนนี้ฉันดูเศร้ามั้ย"

# hi "Not really. You look like you always do, I think."
hi "ไม่เชิง ก็ดูเหมือนเธออย่างทุกที คิดว่านะ"

show rin negative_sad
with charachange

# rin "But I'm sinking."
rin "แต่ฉันจมน้ำอยู่"

show rin negative_worried
with charachange

# rin "I should try to float. Up, like a rubber duck. Quack quack all yellow and creepy."
rin "ต้องดันตัวเองลอยขึ้น ขึ้นไปเหมือนเป็ดยาง ก้าบ ๆ เหลือง ๆ น่าขนลุก"

# "I have to think for a few seconds about which direction I should pursue in this conversation, then I realize that it doesn't matter."
"ฉันหยุดคิดอยู่สองสามวินาทีว่าจะคุยต่อไปทางไหนดี แล้วก็นึกได้ว่าไม่สำคัญหรอก"

# hi "You think rubber ducks are creepy?"
hi "เธอมองว่าเป็ดยางน่าขนลุกเหรอ"

show rin basic_surprised
with charachange

# rin "You don't? I think they look very creepy. Everything that has eyes but isn't alive is very disturbing. Like rubber ducks and reflections in mirrors."
rin "นายไม่ว่างั้นเหรอ ฉันว่าเป็ดยางน่าขนลุกมากเลยนะ อะไรที่มีตาแต่ไม่มีชีวิตน่ะสยองจะตายไป อย่างเป็ดยาง แล้วก็\nเงาสะท้อนในกระจก"

show rin basic_surprised:
    ease 0.5 ypos 1.2 alpha 0.0
with Pause(0.5)

hide rin
with None
play sound sfx_rustling

# "She plops down on the forest bed, leaning on the maple she named the Worry Tree. After wondering what to do for a minute, I sit down too, three feet apart from her."
"เธอผลุบตัวลงนั่งกับพื้นป่าหลังพิงต้นไม้ที่เธอตั้งชื่อว่าต้นทุกข์ ฉันคิดอยู่ครู่หนึ่งว่าจะทำอะไรดีก่อนจะนั่งลงตาม\nห่างจากเธอไปประมาณหนึ่งเมตร"

play sound sfx_rustling
$ renpy.music.set_volume(0.5, 2.0, channel="ambient")

scene bg worrytree:
    xalign 0.5 yalign 1.0 subpixel True
    acdc_warp 30.0 yalign 0.0
with whiteout

# "The forest envelops us in its embrace, and its stillness falls upon the two of us."
"ผืนป่าโอบล้อมพวกเราสองคนไว้ด้วยความสงัดงัน"

# "We sit there without speaking for a long while. I can literally feel the time passing."
"พวกเรานั่งกันโดยไม่คุยอะไรกันอยู่นาน ฉันสัมผัสได้ถึงเวลาที่ไหลผ่านไป"

# "Patches of sunlight litter the small clearing in a pattern that echoes the maple canopies. One of them falls directly on me, warming me all the way to the bone."
"แสงแดดส่องลอดผ่านรอยแยกวาดขึ้นเป็นเงาร่มใบเมเปิล มีแสงแดดหนึ่งที่สาดโดนฉันจนรู้สึกอุ่นเข้าไปถึงข้างใน"

# "I wonder what I could do for myself, and maybe for Rin. For now, I just keep watching her from this distance."
"ฉันนึกอยู่ว่าจะทำอะไรเพื่อตัวเองได้บ้าง แล้วก็อาจจะเพื่อรินด้วย ตอนนี้ฉันได้แต่มองเธออยู่โดยมีระยะระหว่างเรา"

# "Sometimes she cranes her neck all the way back, so much that it looks almost painful, and stares up at the small patch of sky visible past the canopy of the Worry Tree."
"บางครั้งเธอก็แหงนหน้าขึ้นจนเหมือนคอแทบหักมองแผ่นฟ้าที่ถูกร่มใบของต้นทุกข์บังจนเหลือเพียงผืนน้อย"

# "Sometimes she just stares blankly ahead, as if seeing something just beyond her reach. She keeps whispering to herself but so quietly that I can't hear her, even though I'm sitting right next to her."
"บางครั้งเธอก็จ้องตรงไปข้างหน้าราวกับมองบางอย่างที่ไกลเกินเธอเอื้อม เธอพึมพำอยู่กับตัวเองเสียงแผ่วเบา เบาเสียจน\nแม้แต่ฉันที่นั่งอยู่ข้างเธอนั้นยังไม่ได้ยิน"

# "I only see her lips moving, like she was in the middle of a distant dream."
"ฉันเห็นเพียงริมฝีปากเธอที่ขยับ ท่าทีเธอราวกับว่ากำลังอยู่ท่ามกลางฝันอันไกลห่าง"

# "I realize that right now, I no longer feel any of the intense loneliness I feel at night, just before falling asleep."
"ฉันนึกขึ้นได้ว่าตอนนี้ฉันไม่ได้รู้สึกถึงความเปล่าเปลี่ยวที่ถาโถมยามค่ำคืนก่อนนอนแล้ว"

# "I might be more like Rin than I thought."
"ฉันอาจจะเหมือนรินมากกว่าที่คิดก็ได้"

# "I can either give up and stay submerged under the weight of all the crap in my life, or try to change myself for the better."
"ฉันจะยอมแพ้แล้วยอมจมอยู่ใต้ทุกสิ่งอย่างในชีวิตก็ได้ หรือจะเปลี่ยนแปลงตัวเองให้ดีขึ้นก็ได้"

# "Her decision is different, yet the same."
"การตัดสินใจของเธอนั้นแตกต่างทว่าเหมือนกัน"

# "And unlike her, I know for sure that I can't stay like this forever."
"และฉันก็ไม่เหมือนอย่างเธอตรงที่ฉันรู้แน่ว่าจะมัวแต่อยู่อย่างนี้ไปตลอดกาลไม่ได้"

label th_choiceR9:

menu:
    with menueffect

    # "I have to change."
    "ฉันต้องเปลี่ยนแปลง"

    # "I want to be more like Rin.":
    "ฉันอยากเป็นเหมือนอย่างริน":
        return m1

    # "I want to be more like Emi.":
    "ฉันอยากเป็นเหมือนอย่างเอมิ":
        return m2

label th_R9a:


$ renpy.music.set_volume(0.5, 0.5, channel="ambient")
# "Rin could probably do it. Even though she seems to doubt herself, I have no doubts about her strength."
"รินอาจจะทำได้ก็ได้ ถึงเธอจะยังไม่มั่นใจในตัวเอง แต่ฉันมั่นใจในกำลังของเธอ"

# "She could do it, even if she can't."
"เธอทำได้แน่ แม้เธอจะทำไม่ได้"

label th_R9b:

$ renpy.music.set_volume(0.5, 0.5, channel="ambient")
# "Emi probably has done it. She's so happy and energetic, a runner girl without legs."
"เอมิอาจจะเคยทำมาแล้ว เธอทั้งร่าเริงและสดใส เป็นสาวนักวิ่งที่ไม่มีขา"

# "If anyone has “beaten” a disability, it must be her."
"ถ้าจะมีใครที่ “เอาชนะ” ความพิการแล้วละก็ คนนั้นคือเธอ"

label th_R9c:

# "It makes me feel a little bit better too, and I lean back against the tree, breathing out deeply as if for the first time in a long time."
"ว่าแล้วก็ค่อยรู้สึกดีขึ้นมาบ้างเล็กน้อย ฉันพิงตัวกับต้นไม้แล้วสูดหายใจเข้าลึก ๆ ราวกับไม่ได้ทำมานาน"

show bg worrytree_ss:
    yalign 1.0
with shorttimeskip

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

# "We stay that way in the small clearing until the angle of sun changes and the chilly shadows deepen. No longer warm where we sit, we leave the forest, returning along the same path we took coming in."
"พวกเราอยู่ในช่องเล็ก ๆ นั้นจนพระอาทิตย์คล้อยลงและเงาเย็นเยียบเริ่มทอดยาว เมื่อจุดที่พวกเรานั่งกันอยู่นั้น\nหมดร้อนแล้วพวกเราก็ออกมาจากป่าตามทางเดิมที่เดินเข้ามา"

scene bg school_forest2_ss
show rin negative_spaciness_ss at center
with locationchange

# "It doesn't seem like Rin has come to a decision."
"เหมือนรินจะยังตัดสินใจไม่ได้"

# hi "I wonder if it was a bad idea for me to come along."
hi "ให้ฉันมาด้วยนี่ดีแล้วเหรอ"

show rin basic_absent_ss
with charachange

# rin "It's all right. I don't mind. I'm sure the trees and dirt and rocks won't mind either. Did you mind?"
rin "ไม่เป็นไร ฉันไม่ถือ ต้นไม้ ดิน หิน ก็คงไม่ถือเหมือนกัน นายถือมั้ย"

# hi "No, not at all. I think it helped me too."
hi "ไม่ ไม่เลย เหมือนจะดีกับฉันด้วยเหมือนกัน"

$ renpy.music.set_volume(0.4, 1.0, channel="ambient")
scene bg school_forest1_ni
with locationskip

# "While we walk back towards the dormitories, the sky is changing to a deep ultramarine. The first summer stars twinkle softly from between spots in the canopy, barely visible like tiny fireflies."
"ฟ้าเปลี่ยนเป็นสีน้ำเงินเข้มระหว่างที่พวกเราเดินกลับหอกัน หมู่ดาวในฤดูร้อนแรกระยับแสงริบหรี่ยากมองเห็นอยู่ตรง\nช่องว่างบนหลังคาป่าคล้ายหิ่งห้อยตัวน้อย ๆ"

# "I become very self-conscious about Rin's presence."
"คราวนี้ฉันกระอักกระอ่วนใจหนักที่รินอยู่ข้าง ๆ"

window hide
nvl clear
nvl show dissolve

stop ambient fadeout 2.0

# n "\n\n\n\nI haven't thought much about girls since things fell apart with Iwanako."
n "\n\n\nฉันไม่ได้คิดเรื่องผู้หญิงอะไรมากมายตั้งแต่ครั้งที่ความสัมพันธ์กับอิวานาโกะนั้นขาดไป"

# n "This is kind of the same situation as then, but to be honest I don't think it really counts for much. Not with Rin."
n "คราวนี้ก็เหมือนตอนนั้น แต่ว่าตามตรง ฉันว่าไม่ได้เหมือนกันขนาดนั้นหรอก ยิ่งเป็นรินด้วยแล้ว"

# n "And yet… it feels good walking next to her, even if it isn't anything more than this."
n "แต่… พอได้เดินข้างเธอแล้วก็รู้สึกดี ถึงจะไม่ได้มีอะไรไปมากกว่านั้นก็เถอะ"

# n "At first, I think Rin agitated me quite a bit with her unpredictable behavior. But recently, I feel I haven't had to be on my toes so much."
n "แรกเริ่มเดิมทีฉันหงุดหงิดเพราะเดาใจเธอไม่เคยได้ แต่ช่วงนี้ฉันไม่ได้รู้สึกว่าจะกันท่ากับเธออะไรขนาดนั้นแล้ว"

# n "I've managed to let myself go a little. It makes me feel satisfied, even though ultimately I think it's more thanks to Rin than myself."
n "ฉันปล่อยตัวสบาย ๆ ได้บ้างแล้วจนนึกพอใจขึ้นมา ถึงจริง ๆ แล้วจะเป็นเพราะรินมากกว่าตัวฉันเองก็เถอะ"

# n "She seems to be disinterested in a huge number of things, but something in her makes me try harder than I normally would."
n "เธอดูเป็นคนไม่สนโลกมากมายหลายอย่าง แต่บางอย่างในตัวเธอทำให้ฉันฮึดขึ้นมากว่าปกติ"

nvl clear

# n "\n\n\nIt's not that I want to impress her; I think that truly impressing Rin would take near-superhuman effort just because of how she is. Instead, it's because there is this relentless feeling inside of me that I shouldn't let Rin down."
n "\n\n\nไม่ใช่ว่าฉันอยากทำให้เธอประทับใจหรืออะไร เพราะดูจากสภาพแล้วกว่าจะทำให้รินประทับใจได้ก็คงต้องทุ่มแรง\nปานยอดมนุษย์ แต่ฉันว่าที่จริงเป็นเพราะความรู้สึกหนึ่งในใจที่ไม่อยากทำให้รินผิดหวังมากกว่า"

# n "It's really weird. I wonder why I started thinking like that. I don't even know what sort of expectations she has about pretty much anything."
n "แปลกจริง ๆ ทำไมฉันถึงมาคิดอะไรอย่างนี้กันนะ ไม่รู้ด้วยซ้ำว่าเธอจะคาดหวังกับอะไร ๆ ยังไงบ้าง"

# n "So how could I let her down? Rin has this unassuming air around her, and she doesn't really talk about stuff very often. Even today's confession of her self-doubt caught me a little bit off guard."
n "แล้วฉันจะไปทำให้รินผิดหวังได้ยังไง เธอเป็นคนที่ดูเงียบ ๆ ไม่พูดถึงอะไรเท่าไหร่ ขนาดวันนี้ที่เธอเล่าเรื่องตัวเอง\nฉันยังตกใจหน่อย ๆ เลย"

# n "I feel like I want to talk more with her."
n "ฉันอยากคุยกับเธอให้มากกว่านี้"

# n "The realization suddenly dawns on me that Rin is basically the only person I talk to nowadays, apart from whatever I have to endure from Shizune, Misha or Kenji. I feel slightly depressed."
n "แล้วอยู่ ๆ ฉันก็นึกขึ้นได้ว่าทุกวันนี้ฉันคุยอยู่แต่กับรินแล้ว ถ้าไม่นับอะไรก็ตามที่ฉันต้องทนกับชิซูเนะ มิช่า หรือเคนจิ\nหดหู่ขึ้นมาหน่อย ๆ เลยแฮะ"

nvl clear
nvl hide dissolve

scene bg school_dormext_full_ni at bgright
with locationskip

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_cicadas fadein 1.0

window show

# "In front of the dormitories, as if summoned by my dark thoughts, we run into Kenji himself."
"พวกเราเจอกับเคนจิที่มายืนอยู่ตรงหน้าหอราวถูกความคิดอันดำมืดของฉันอัญเชิญมา"

show kenji tsun_ni at center
with charaenter

# "It feels very odd seeing him outside, breathing fresh outdoor air. At least it's already dusk; I partially expect Kenji would disintegrate upon direct exposure to the sun."
"พอได้เห็นเขามายืนสูดอากาศอยู่ข้างนอกแล้วก็รู้สึกประหลาด แต่อย่างน้อยตอนนี้ก็ค่ำแล้ว ฉันแอบคิดไปด้วยซ้ำ\nว่าถ้าเคนจิโดนแดดแล้วตัวเขาจะสลายเป็นผุยผง"

# "Kenji himself seems very insecure as well, standing around looking like he's waiting for something, but doesn't know himself what it might be."
"เคนจิเองก็ดูจะหวาดระแวงเหมือนกัน ยืนมองซ้ายมองขวาเหมือนรออะไรอยู่ทั้งที่ไม่รู้ว่ารออะไร"

# hi "Hey, Kenji. What're you doing?"
hi "ไง เคนจิ ทำไรอยู่"

show kenji tsun_ni at twoleft
show bg school_dormext_full_ni at center
with charamove

show rin basic_awayabsent_ni at tworight
with charaenter

# rin "Hello."
rin "สวัสดี"

stop ambient fadeout 0.2

show kenji rage_ni
with charachange
with vpunch

# ke "Who're you?"
ke "ใคร"

play music music_tension

show rin basic_absent_ni
with charachange

# hi "It's me, Hisao. Umm… I'm not sure if you know Tezuka from class 3-4?"
hi "ฉันเอง ฮิซาโอะ เอ่อ… ฉันไม่แน่ใจว่านายรู้จักเทซูกะห้อง 3-4 หรือเปล่านะ"

show kenji tsun_ni
with charachange

# "From his face I can see that not only he doesn't know Rin, he also can't see her from this short distance."
"ดูจากสีหน้าแล้วรู้เลยว่าไม่รู้จักไม่พอยังไม่เห็นหน้าเธอทั้งที่อยู่ใกล้ขนาดนี้อีก"

show kenji happy_ni
show rin basic_awayabsent_ni
with charachange

stop music fadeout 0.5

# ke "Oh, sup dudes?"
ke "โอ้ ไงพวก"

play music music_kenji
play ambient sfx_cicadas fadein 6.0

# "Kenji sticks his hand enthusiastically forward, almost straight into Rin's stomach."
"เคนจิยื่นมือมาอย่างกระฉับกระเฉงจนแทบทิ่มเข้ากับท้องริน"

show rin negative_spaciness_ni
with charachange

# "Rin looks at his outstretched hand in confusion until Kenji clears his throat and retracts the hand."
"รินมองมือเคนจิที่ยื่นมาด้วยความงงงัน จากนั้นเคนจิก็กระแอมไอขึ้นมาแล้วหดมือกลับ"

show kenji neutral_ni
with charachange

# "There is something almost cool that he manages to do with social awkwardness. It's not like I'm the most suave man on the planet, but I don't think I'll ever be able to even approach Kenji's level."
"แต่เห็นเวลาที่เขาหาเรื่องทำตัวกลบเกลื่อนเวลาบรรยากาศอึดอัดขึ้นมาทีไรแล้วก็ทึ่ง ฉันก็ไม่ใช่คนที่มั่นหน้าอะไร\nขนาดนั้นหรอก แต่ฉันคงไม่มีวันทำได้เทียบเท่าอย่างเคนจิแน่ ๆ"

# "I think I respect Kenji a little bit more."
"ฉันนับถือเขาขึ้นมาหน่อย ๆ แล้ว"

show rin basic_absent_ni
with charachange

# hi "So you're waiting for someone?"
hi "แล้วนี่รอใครอยู่เหรอ"

show kenji tsun_close_ni
with characlose

# "He leans closer and lowers his voice to an agitated whisper. I see his facial muscles twitching."
"เขาโน้มตัวเข้ามาใกล้แล้วกระซิบกระซาบรัวเร็ว เห็นหน้าเขากระตุกด้วย"

# ke "Come on man, you know I can't talk about stuff here in public. They might be listening."
ke "เฮ้ย พวก ฉันคุยเรื่องนี้ในที่แจ้งไม่ได้นะ พวกนั้นอาจจะฟังอยู่"

# ke "I'm going to have to go pick up some stuff from somewhere, and I don't want those snooping student council hags to get on my case."
ke "ฉันจะออกไปรับของจากที่หนึ่ง แล้วฉันก็ไม่อยากให้พวกสภาตัวจุ้นเข้ามายุ่งด้วย"

# ke "Also, I don't trust your friend. Nothing personal. Are you sure he's trustworthy?"
ke "แล้วก็ ฉันไม่เชื่อใจเพื่อนนายนะ ไม่ได้มีปัญหาอะไรเป็นการส่วนตัวหรอก แต่นายแน่ใจเหรอว่าเขาเชื่อใจได้"

# "I briefly consider telling Kenji about Rin's gender, but as it might end up badly for one or both of them, I decide against it."
"แวบหนึ่งฉันคิดจะบอกเพศริน แต่บอกไปเดี๋ยวไม่ใครก็ใครหรือทั้งสองคนต้องแย่แน่ จึงไม่ได้บอกไป"

# hi "Yeah, I'm sure."
hi "อืม แน่"

show kenji neutral_ni
show rin basic_awayabsent_ni
with charadistant

# "He turns from me to Rin, and I immediately get the feeling that I have to prevent them from talking to each other with whatever means necessary. However, there is little I can do now, apart from physical violence."
"เขาหันหน้าจากฉันไปหาริน แล้วฉันก็รู้สึกทันทีว่าต้องยั้งสุดชีวิตไม่ให้สองคนนี้คุยกันได้ แต่ตอนนี้ฉันก็ทำอะไรได้\nไม่มาก นอกเสียจากว่าจะฉันจะลงไม้ลงมือ"

show kenji happy_ni
with charachange

# ke "In that case, would you be interested in knowing about the worst threat to mankind since they invented vegetarianism?"
ke "ถ้างั้น นายอยากจะรู้ภัยมหันต์ต่อมนุษยชาติที่แย่ที่สุดที่เกิดหลังจากการกินมังสวิรัติหรือเปล่า"

# "He sounds like a vacuum cleaner salesman."
"พูดอย่างกับพนักงานขายเครื่องดูดฝุ่น"

show rin basic_deadpan_ni
with charachange

# rin "I thought it was Sunday."
rin "ไม่ใช่วันอาทิตย์เหรอ"

show kenji neutral_ni
show rin basic_awayabsent_ni
with charachange

# ke "I see you're not in the know. Yeah man, I'm talking about man-eating cows here. Very few people know what I know, so I'm not surprised."
ke "แสดงว่ายังไม่รู้สินะ ใช่ ฉันพูดถึงวัวกินคนอยู่ แต่น้อยคนที่จะรู้ ไม่แปลกใจหรอก"

show kenji happy_ni
with charachange

# ke "We can't talk here, but if you'd like a pamphlet, come to my room after curfew on Mondays or Wednesdays."
ke "ฉันเล่าตรงนี้ไม่ได้ แต่ถ้านายอยากได้แผ่นพับ ให้มาหาฉันวันจันทร์หรือวันอาทิตย์หลังเวลาปิดประตูหอ"

# "He suddenly reaches to his pocket and draws out a ballpoint pen and what looks like a convenience store receipt."
"เขาควักปากกากับใบอะไรสักอย่างที่ดูเหมือนเป็นใบเสร็จรับเงินจากร้านสะดวกซื้อออกมาจากกระเป๋ากางเกง"

# "Kenji furiously scribbles on the scrap of paper and then thrusts it towards Rin."
"เคนจิขีดเขียนขยุกขยิกลงบนเศษกระดาษแผ่นนั้นแล้วยื่นไปทางริน"

show kenji neutral_ni
with charachange

# ke "Here's the password. Memorize it and then eradicate any trace of this document. Eat it, burn it, dissolve in acid, whatever."
ke "เอ้านี่รหัสผ่าน จำไว้ แล้วทำลายเอกสารนี้ทิ้งให้สิ้นซาก กิน เผา แช่กรด ไงก็ได้"

# "I take the receipt from Kenji as Rin is unable to do so, and glance at it. It's indeed a receipt, apparently for two rice balls and five boxes of matches. I hope he is not planning to burn anything down."
"ฉันรับใบเสร็จมาจากเคนจิด้วยว่ารินรับไม่ได้แล้วมองผ่าน ๆ เป็นใบเสร็จจริงด้วย เหมือนจะซื้อข้าวปั้นสองก้อน\nกับไม้ขีดไฟห้ากลัก หวังว่าไม่ได้คิดจะไปเผาอะไรนะ"

# "On the other side is written just one word."
"อีกหน้ามีคำหนึ่งคำเขียนไว้"

window hide

$ written_note(u"มัฟฟินน้ำผึ้ง")

show rin basic_absent_ni
with charachange

window show

# "I show it to Rin too, but she shows no reaction."
"พอเอาให้รินดูด้วยเธอก็ไม่ทำสีหน้าอะไร"

show rin basic_awayabsent_ni
with charachange

# rin "Thank you."
rin "ขอบคุณ"

show kenji tsun_ni
with charachange

# ke "Yo, Hisao. You still in that club? The club of dark arts?"
ke "เออ ฮิซาโอะ ยังอยู่ชมรมนั้นอีกเหรอ ชมรมกาฬศิลป์นั่นน่ะ"

show rin basic_absent_ni
with charachange

# hi "Fine art. Anyway yeah, actually just had a meeting today."
hi "วิจิตรศิลป์ เอ้อ วันนี้เพิ่งทำกิจกรรมชมรมมาเลย"

show rin basic_awayabsent_ni
show kenji neutral_ni
with charachange

# ke "Still got your wits about you? No shady mind tricks going on? Nothing personal man, but I have to be on top of things."
ke "สติสัมปชัญญะยังอยู่ครบนะ ไม่ได้มีกลจิตวิทยาอะไรนะ ไม่ได้มีปัญหาอะไรเป็นการส่วนตัวหรอก แค่ต้องคอยจับตาดู\nว่าฉันยังรับมือทุกอย่างไหวน่ะ"

show kenji tsun_ni
with charachange

# ke "Can't get caught with my pants down. Speaking of which, you should really take showers a bit later. Gotta respect that personal space. Nothing personal."
ke "จะให้เล่นทีเผลอตอนกางเกงหลุดไม่ได้ จะว่าไป เดี๋ยวนายไปอาบน้ำเลยนะ ต้องเคารพพื้นที่ส่วนตัวนั่นหน่อย ไม่ได้\nมีปัญหาอะไรเป็นการส่วนตัวหรอก"

# "Kenji looks around as if he heard something and then straightens his jacket."
"เคนจิมองวอกแวกเหมือนได้ยินอะไรบางอย่างแล้วจัดแจงเสื้อคลุมตัวเอง"

show kenji neutral_ni
with charachange

# ke "Okay, I gotta scoot now before it gets too late. Later dudes. Good luck."
ke "โอเค ต้องรีบไปก่อนสายเกิน เจอกันพวก โชคดี"

hide kenji
with charaexit

show bg school_dormext_full_ni at bgleft
show rin basic_deadpanupset_ni at center
with dissolvecharamove
stop music fadeout 4.0

# "Kenji takes off rapidly towards the main gate. Rin looks after him, frowning."
"เคนจิก้าวฉับ ๆ ไปที่ประตูหน้าโรงเรียน รินขมวดคิ้วมองไล่หลังเขาไป"

# "We watch after Kenji's diminishing figure in silence."
"พวกเรายืนมองตัวเคนจิที่หดเล็กลงไปเรื่อย ๆ กันเงียบ ๆ"

show rin basic_deadpancontemplation_ni
with charachange

# rin "What's wrong with him?"
rin "เขาเป็นอะไร"

# hi "Technically speaking, I think he's legally blind."
hi "ถ้าให้ว่าตามจริง เหมือนเขาจะตาบอดโดยกฎหมายนะ"

show rin basic_deadpansurprised_ni
with charachange

# rin "Oh. I see."
rin "อ้อ งี้นี่เอง"

stop ambient fadeout 2.0

scene black
with dissolve


#******************************************

label th_R10:

scene ev hisao_letter_closed
with locationchange

# "I can immediately tell from the envelope that it's not about official matters of any sort. Someone actually wrote me an old-fashioned, hand-written paper letter."
"ดูจากซองจดหมายแล้วก็รู้ทันทีว่าไม่ใช่จดหมายทางการหรืออะไร มีคนเขียนจดหมายด้วยมือแบบเชย ๆ ส่งมาให้ฉัน\nจริง ๆ"

# "Who bothers doing something like that in this day and age, anyway? Yet, as unlikely as the prospect of receiving one sounds, there is definitely a letter lying on my desk."
"ยุคสมัยป่านนี้แล้วใครจะมานั่งเขียนจดหมายส่งหากันแบบนี้ แต่แม้จะฟังดูเป็นไปไม่ได้เพียงใด สิ่งที่อยู่บนโต๊ะฉันตอนนี้\nคือจดหมายแน่ ๆ"

scene bg school_dormhisao
with locationchange

# "The classes for the day are over. Still feeling pretty full from the big lunch that I had unexpectedly eaten at the cafeteria, I returned to my dorm, planning on finishing my homework and probably skipping dinner, or at least just eating light."
"วันนี้เลิกเรียนแล้ว ด้วยความที่ยังอิ่มท้องจากการยัดทะนานข้าวเที่ยงลงท้องโดยไม่คาดหมายที่โรงอาหาร ฉันจึงกลับมา\nที่หอเตรียมทำการบ้านต่อให้เสร็จ แล้วก็จะไม่กินข้าวเย็น หรือไม่ก็หาอะไรเบา ๆ กินแทน"

# "I feel like I need to eat less than I used to. Maybe I don't use that much energy, now that I don't do much beyond reading."
"คงต้องกินให้น้อยลงกว่าทุกทีแล้ว ฉันอาจจะไม่ได้ใช้พลังงานเยอะขนาดนั้นก็ได้ เพราะก็เอาแต่อ่านหนังสือ"

# "However, the letter on my desk has naturally caught my interest."
"ทว่าจดหมายที่อยู่บนโต๊ะนั้นก็สะดุดตาเข้า"

scene ev hisao_letter_closed:
     xalign 0.5 yalign 0.5 zoom 1.1 subpixel True
     acdc_warp 10.0 zoom 1.0
with locationchange

# "It's the first piece of mail I've received here at Yamaku, so it'd feel special even if it wasn't something as rare as a handwritten letter."
"เป็นของอย่างแรกที่ฉันได้รับนับตั้งแต่ที่ฉันมาเข้าเรียนที่ยามากุ เพราะงั้นถึงต่อให้ไม่ใช่จดหมายเขียนมือก็จะเป็นอะไร\nที่รู้สึกว่าพิเศษอยู่ดี"

# "What causes me even more trepidation is the name of the sender, written neatly on the back of the envelope."
"สิ่งที่ทำให้ฉันสังหรณ์ใจขึ้นมายิ่งกว่านั้นคือชื่อของผู้ส่งที่เขียนไว้ด้วยลายมือเรียบร้อยอยู่หลังซอง"

# "Iwanako."
"อิวานาโกะ"

# "I have no idea why she would write to me. I haven't been in contact with anyone from my old school since I transferred, and Iwanako is the last person I'd expect to want to write me a letter."
"ฉันไม่รู้ว่าเธอจะมีอะไรเขียนถึงฉัน ตั้งแต่ย้ายมาฉันก็ไม่ได้ติดต่อกับใครที่โรงเรียนเก่าแล้ว แล้วอิวานาโกะยิ่งไม่ใช่ใคร\nที่ฉันจะคาดฝันว่าจะเขียนจดหมายส่งมาเลย"

window hide
nvl clear
nvl show dissolve

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_rain fadein 4.0

# n "\n\n\nThe last time I saw Iwanako was terribly awkward; embarrassingly so. She came to my hospital room, peeled me an apple out of courtesy and then we practically sat in silence for half an hour."
n "\n\n\nครั้งสุดท้ายที่ได้เจอกันนั้นทั้งแสนอึดอัดและน่าอาย เธอมาเยี่ยมที่ห้องฉันแล้วปอกแอปเปิลให้เป็นมารยาท แล้วก็อยู่กัน\nเงียบ ๆ ได้ครึ่งชั่วโมง"

# n "She said “goodbye” and didn't look me in the eye when she closed the door."
n "เธอบอกว่า “ลาก่อนนะ” แล้วปิดประตูไปไม่แม้แต่จะมองตากัน"

# n "It might've been a natural end to the series of visits that were probably pretty painful for both of us."
n "การเยี่ยมไข้คงจะทำเราทั้งคู่ค่อนข้างทรมาน อาจจะเป็นธรรมดาที่จบลงไปอย่างนั้น"

# n "Every time she visited me in the hospital I wanted to talk to her, but something stopped me every time. Every time that I didn't speak made the next time even harder."
n "ทุกครั้งที่เธอมาเยี่ยมฉันนึกอยากคุยกับเธอตลอด แต่บางอย่างก็ยั้งปากฉันไว้ แล้วยิ่งไม่ได้พูดครั้งหนึ่ง ครั้งถัดไปก็ยิ่ง\nพูดยากขึ้นไปอีก"

# n "Iwanako always had this aura of fragility around her, as if she'd shatter into pieces at the slightest disturbance. Initially I think it might've been that delicacy that attracted me to her, but after what happened back then, it felt as if she really had shattered."
n "อิวานาโกะเธอดูเป็นคนเปราะบางอย่างนี้เสมอ คล้ายว่าหากมีสิ่งใดรบกวนเพียงเล็กน้อยก็ทำเธอแตกสลายได้ เดิมที\nฉันคงจะชอบความเปราะบางอย่างนั้นของเธอ แต่พอเกิดเรื่องนั้นขึ้นมาแล้วก็รู้สึกราวกับว่าเธอได้แตกสลายไปแล้ว\nจริง ๆ"

nvl clear

# n "\n\n\n\n\nShe looked so sad that I didn't want to say anything that might upset her, and I never could figure out the right words to say."
n "\n\n\n\n\nเธอดูเศร้าเสียจนฉันไม่อยากพูดอะไรที่ไปทำให้เธอเครียดอีก แล้วฉันก็ไม่เคยเฟ้นหาอะไรดี ๆ มาพูดได้เลย"

# n "I told her that it wasn't her fault, she nodded and I really think she understood that if it hadn't been that, then sooner or later something else would've made my heart give out."
n "ฉันบอกเธอไปว่าไม่ใช่ความผิดเธอเลย เธอพยักหน้า ฉันคิดว่าเธอคงเข้าใจแล้วว่าถ้าไม่เกิดเรื่องเมื่อวันนั้นขึ้นมา\nไม่ช้าก็นานสักวันหัวใจฉันก็จะอาการกำเริบอยู่ดี"

# n "Yet she looked so hopelessly sad every time she opened that door and entered my room."
n "ทว่าเธอดูเศร้าโศกทุกครั้งที่เปิดประตูห้องเข้ามาหาฉัน"

# n "So I never managed to say the things I wanted to say. In the end, that might've hurt her even more."
n "ฉันไม่เคยพูดอะไรที่อยากจะพูดได้เลย ซึ่งท้ายที่สุดพอทำอย่างนั้นแล้วเธอคงจะเจ็บหนักกว่าเดิมด้วยซ้ำ"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

scene ev hisao_letter_open
with locationchange

window show

# "Carefully, I open the envelope and draw out the folded letter from within."
"ฉันแกะซองจดหมายอย่างทะนุถนอมแล้วเปิดจดหมายที่อยู่ข้างในออกอ่าน"

window hide

# $ written_note("Dear Hisao,\n\nHow are you? I hope you are well and happy at your new school. Everyone here misses you. Almost all of our second-year class got put together in class 3-1 for the final year, so we are pretty comfortable right from the beginning of the year. I'm sure you would've been assigned to this class as well.")
$ written_note("ถึง ฮิซาโอะ\n\nเป็นยังไงบ้าง หวังว่านายจะสบายดีมีความสุข\nกับโรงเรียนใหม่นะ คนที่นี่คิดถึงนายกัน พวก\nนักเรียนปีที่สองพอได้ขึ้นชั้นมาอยู่ปีที่สามก็ได้\nย้ายมาอยู่ห้อง 3-1 กันเกือบหมดเลย ก็เลยอยู่กัน\nอย่างอบอุ่นแต่ต้นปีการศึกษาเลย ถ้านายยังอยู่\nก็คงได้มาเรียนห้องเดียวกันเหมือนกัน")

# $ written_note("The mood among the third-years seems to be very anxious about the final exams, even though they are so far away. The teachers are badgering us about it all the time - even old Mr. Tachibana who is, by the way, our homeroom teacher this year. Would you believe it? I was sure that he'd retire after our second year, but here he is, nagging everyone about studying for exams.\n")
$ written_note("นักเรียนปีที่สามดูจะเครียดเรื่อง\nสอบปลายภาคกัน ถึงจะยังอีกนานก็เถอะ\nคุณครูก็เอาแต่ตามย้ำอยู่นั่นแหละ ขนาด\nครูทาจิบานะยังเป็นไปกับเขาเลย\nแล้วก็เนี่ย เชื่อมั้ยว่าปีนี้แกได้เป็น\nครูประจำชั้นห้องเราด้วยนะ ฉันก็\nกะไว้แล้วแท้ ๆ ว่ายังไงพอขึ้นชั้นมา\nแกก็คงเกษียณไปแล้ว แต่ก็ไม่\nมายืนจิกหัวให้อ่านหนังสือสอบอยู่เนี่ย\n")

# $ written_note("I think things like that are the main reason why the mood among the third-years is so nervous. I must admit that I'm somehow losing confidence in myself as well, even though I've always fared reasonably well in exams.\n\n\n\n\n")
$ written_note("ฉันว่าเพราะอย่างนั้นแหละพวกปีที่สาม\nเลยร้อนรนกัน ฉันก็ต้อง\nยอมรับเหมือนกันว่าฉันเองก็ชักจะ\nไม่มั่นใจขึ้นมาแล้ว ถึงปกติจะสอบ\nได้คะแนนเยอะพอตัวตลอดก็เถอะ\n\n\n\n\n")

# $ written_note("It's so weird to think we are already seniors, isn't it? Time has really flown past. I wonder where it went. The new first-years seem so young and somehow really innocent. I keep wondering if I was like them in my first year. I've been feeling nostalgic like this for the whole first trimester.\n\n\n")
$ written_note("แปลกเนอะ รู้ตัวอีกทีก็ปีที่สามแล้ว\nเวลาผ่านไปไวจริง ๆ ผ่านไปไหนกันนะ\nนักเรียนปีที่หนึ่งน่ะดูทั้งยังเด็กแล้วก็\nใสซื่อดี ตลอดเทอมแรกนี้ฉันเอาแต่\nย้อนคิดตลอดเลยแหละว่าสมัย\nอยู่ปีที่หนึ่งฉันก็เป็นอย่างนั้นด้วย\nหรือเปล่า\n\n\n")

show ev hisao_letter_open:
    "ev hisao_letter_open_2" with locationchange
with None
$ ksgallery_unlock("ev hisao_letter_open_2")

# $ written_note("There are other things I want to say. I'm writing to you because I felt that there are things I should've said after the incident back in winter. I really regret that I wasn't able to say them in person, and I have no excuse for it.\n\n\n\n\n")
$ written_note("ยังมีอย่างอื่นที่ฉันอยากพูดถึงอีก\nฉันเขียนจดหมายส่งมาหานาย\nเพราะรู้สึกเหมือนพอเกิดเรื่องนั้น\nแล้วฉันคงต้องพูดอะไรหน่อย ฉัน\nเสียใจจริง ๆ ที่ฉันมาพูดกับนาย\nต่อหน้าตรง ๆ ไม่ได้ และฉันก็ไม่มี\nข้อแก้ตัวอะไรทั้งนั้น\n\n\n\n\n")

# $ written_note("The truth is, the times when I visited you at the hospital made me worried about you. I am not talking about your health. You seemed to become more distant and disheartened. It was natural after something like that happened, I'm sure, but somehow I got the feeling that you had given up on something back then. Happiness, maybe?\n")
$ written_note("ที่จริงคือ ตอนฉันไปเยี่ยมนาย\nฉันก็เป็นห่วงนายขึ้นมา ไม่ได้\nหมายถึงสุขภาพนายนะ แต่นาย\nดูทั้งห่างเหินทั้งไร้เรี่ยวแรง ฉันรู้อยู่\nว่าพอเกิดเรื่องอย่างนั้นแล้ว\nจะเป็นแบบนั้นไปก็คงไม่แปลก\nแต่ตอนนั้นฉันรู้สึกเหมือนนายถอดใจ\nกับอะไรบางอย่างแล้ว ความสุข ละมั้ง\n")

# $ written_note("I wanted to somehow express my feelings, but the right words didn't come to me. I couldn't say anything to comfort you. I am really sorry for not being able to support you when it mattered the most, even though I like you so much. At least now, finally, I can be more honest.\n\n\n\n")
$ written_note("ฉันอยากบอกความรู้สึกให้นายได้รู้\nแต่ก็นึกหาคำไม่ได้เสียที ฉันพูดอะไร\nปลอบใจนายไม่ได้เลย ฉันขอโทษจริง ๆ\nที่คอยเป็นแรงใจให้นายยามที่นาย\nต้องการแรงใจที่สุดไม่ได้ ทั้งที่ฉัน\nชอบนายมากแท้ ๆ แต่อย่างน้อยตอนนี้\nฉันก็พูดตรง ๆ ขึ้นมาได้บ้างแล้ว")

# $ written_note("If I could go back to those quiet days in February and March, I'd tell you to not give up on yourself. That's what I would say. Maybe you wouldn't have drifted so far away if I had just said something. I hope you've managed to get back on your feet on your own.\n\n\n\n")
$ written_note("ถ้าฉันกลับไปช่วงเดือนกุมภาพันธ์กับ\nเดือนมีนาคมที่เงียบสงบนั้นได้ฉันก็\nอยากบอกนายว่าอย่ายอมแพ้นะ\nฉันจะบอกอย่างนั้น ถ้าฉัน\nพูดอะไรบ้างนายก็คงไม่ออกเหินห่าง\nไปขนาดนี้ ฉันอยากให้นาย\nลุกขึ้นมายืนด้วยตัวเองให้ได้\n\n\n\n")

# $ written_note("Now that the distance between us is also physical, it also feels more final, somehow. I wonder if we will meet again. Perhaps it's for the best if we don't? Still, if you would like to correspond with me, by all means write me back. I'd very much like to hear about your new school and how you are doing. I wish you all the best.\n\nSincerely, Iwanako")
$ written_note("แล้วยิ่งทีนี้ห่างกายกันด้วยก็ยิ่งรู้สึก\nเหมือนเป็นจุดส่งท้ายจริง ๆ ยังไงไม่รู้\nเราจะได้เจอกันอีกมั้ยนะ หรือ\nถ้าไม่เจอกันอีกเลยจะดีกว่ากันนะ\nแต่ถ้ายังอยากติดต่อกับฉันอยู่\nก็เขียนส่งกลับมาได้เลยนะ\nฉันยินดีมากที่จะได้ฟังเรื่องโรงเรียนใหม่\nกับชีวิตใหม่นาย ขอให้มีความสุขดีนะ\n\nจากใจ อิวานาโกะ")

window show

# "After finishing reading the letter I fold it like it was, and place it on my desk."
"พออ่านจบฉันก็พับเก็บวางไว้บนโต๊ะเหมือนเดิม"

# "I don't know what to think of this. I feel empty and confused."
"ฉันไม่รู้ว่าจะคิดยังไงกับจดหมายฉบับนี้ดี ฉันรู้สึกทั้งว่างโหวงและสับสน"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

# n "\n\nWhy now, after all this time?"
n "\n\nทำไมถึงส่งมาเอาป่านนี้"

# n "Just yesterday I decided that I can't let myself stay like this, that I'd try to get on top of my own life. Reading this letter just reminds me of what could have been."
n "เมื่อวานฉันตัดสินใจแล้วแท้ ๆ ว่าจะปล่อยให้ตัวเองจมอยู่อย่างนี้ไม่ได้ ต้องทำอะไรกับชีวิตตัวเองบ้าง พอได้อ่านจดหมาย\nฉบับนี้แล้วก็ยิ่งคิดว่าอดีตชีวิตฉันอาจเปลี่ยนไปอีกแบบได้"

# n "Of course I wish that I didn't have to be here. I'd want to be in the same class with Iwanako again. Maybe we would talk every day now and go on dates."
n "แน่ละว่าฉันไม่อยากมาอยู่ตรงนี้ ฉันอยากจะอยู่ห้องเดียวกันกับอิวานาโกะอีกครั้ง ป่านนี้พวกเราคงได้คุยกันทุกวัน\nไม่ก็ไปเดตกัน"

# n "\nMy life didn't go like that."
n "\nชีวิตฉันไม่ได้เป็นอย่างนั้น"

# n "I didn't really need to be reminded of this. Iwanako needed to write this letter for her own sake and I'm glad for her that she could, but it would've been better if I hadn't read it."
n "ฉันไม่ได้อยากจะให้มีอะไรมาชวนให้ย้อนนึกถึงเรื่องนี้เลย อิวานาโกะอยากเขียนจดหมายฉบับนี้ขึ้นมาก็เพื่อตัวเธอเอง \nซึ่งฉันก็ยินดีที่เธอเขียนมาได้ แต่คงจะดีกว่าถ้าฉันไม่ได้เปิดอ่าน"

# n "\nOf course, she is right. I thought of the same thing yesterday. I had fallen into a pit of depression and now have to try to climb out."
n "\nแน่ละ เธอพูดถูก เมื่อวานฉันก็คิดเหมือนกัน ว่าฉันตกลงมาอยู่ในหลุมความหดหู่ แล้วทีนี้ฉันก็ต้องตะเกียกตะกาย\nปีนออกมา"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

scene bg school_dormhisao
with locationchange

window show

# "I rip out a page from my notebook, and after a moment of thinking how to frame my words, write a short reply to Iwanako."
"ฉันฉีกสมุดมาหนึ่งหน้าแล้วนึกสรรร่างคำพูดในหัวพักหนึ่งก่อนจะเขียนตอบถึงอิวานาโกะสั้น ๆ"

# "I find it difficult to be really honest to her, but at least I try to appear somewhat convincing. I don't write her about Yamaku at all."
"จะให้พูดอะไรตรง ๆ กับเธอเลยก็ลำบาก แต่อย่างน้อยก็เขียนให้ดูน่าเชื่อถือได้บ้างละนะ ฉันไม่ได้เขียนถึงยามากุเลย"

# "I doubt she will write me again, but I don't feel at all sad about it. I fold my own letter to her and as I have no envelope, set it next to Iwanako's. I'll mail it to her later."
"ฉันไม่แน่ใจด้วยซ้ำว่าเธอจะเขียนส่งมาหาฉันอีกหรือเปล่า แต่ฉันไม่ได้เสียใจเลย ฉันพับจดหมายที่เขียนถึงเธอแล้ววาง\nไว้ข้าง ๆ จดหมายของอิวานาโกะเพราะฉันยังไม่มีซองจดหมาย ไว้ค่อยไปส่งแล้วกัน"

# "Then I lie back on my bed, looking at the monotone gray ceiling."
"จากนั้นฉันก็มานอนที่เตียงมองเพดานสีเทาทึบ"

# "A bird sings outside of my window and a sudden gust of wind flutters my curtains. The summer afternoon feels still, as if time had stopped for a brief moment."
"นกส่งเสียงร้องอยู่นอกหน้าต่าง จู่ ๆ ลมก็พัดจนผ้าม่านกระพือ ยามบ่ายในฤดูร้อนนั้นช่างอืดเอื่อยราวเวลาได้หยุดลง\nไปชั่วขณะ"

# "I think about all the things I've lost and will never regain."
"ฉันคิดถึงสิ่งอย่างที่ฉันสูญไปและไม่มีวันได้กลับคืน"

stop music fadeout 2.0

scene black
with dissolve

$ suppress_window_after_timeskip = True

#*******************************************


label th_R11:

window hide None

play music music_night

scene bg misc_sky at Fullpan(60.0)
with locationchange

nvl clear
nvl show dissolve

# n "Thus the languid days of mid-June pass by."
n "แล้วช่วงกลางเดือนมิถุนายนอันเอื่อยเฉื่อยก็ผ่านไปเช่นนั้น"

# n "I mail my letter to Iwanako, and receive no reply."
n "ฉันส่งจดหมายไปหาอิวานาโกะ และไม่มีการตอบกลับมา"

# n "Having decided to ditch the old me, I start observing my fellow students even closer than I did before, hoping to understand how other people cope with their own issues."
n "ฉันตัดสินใจทิ้งตัวฉันคนเก่า จับสังเกตเหล่านักเรียนให้ถี่ถ้วนกว่าที่เคยด้วยหวังว่าจะได้รู้วิธีการที่คนอื่นรับมือกับปัญหา\nของตัวเอง"

# n "I start seeing things I didn't before, and it makes me wonder if I've been wrong twice."
n "ฉันเริ่มเห็นอะไรที่ไม่เคยเห็นมาก่อน จนนึกสงสัยว่าฉันคิดผิดไปสองครั้งแล้วหรือเปล่า"

# n "Superficially, everyone is abnormal yet so strikingly normal that it shocked me at first. I admired the way my new school mates turned my prejudices around just like that, simply by being themselves."
n "ทีแรกนั้นภายนอกทุกคนดูผิดปกติทว่าปกติมากจนฉันตกใจ ฉันชื่นชมเพื่อนร่วมโรงเรียนใหม่นี้ที่เพียงแค่\nเป็นตัวของตัวเองก็ลบอคติของฉันทิ้งไปได้อย่างง่ายดาย"

# n "Now that I've gotten used to it, I begin noticing other kinds of tones in the people surrounding me every day."
n "ทีนี้พอชินแล้วก็เริ่มสังเกตเห็นบรรยากาศอีกอย่างที่ล้อมตัวคนรอบตัวฉันทุกวันอยู่"

# n "\nThere is this soft, numb sadness all around me."
n "\nจะเป็นบรรยากาศอันเศร้าหมองอ่อน ๆ ที่ด้านชา"

# n "I can see the effort everyone has to make just to get through the day, and how it weighs on their shoulders, like it weighs on mine."
n "ฉันเห็นว่าทุกคนพยายามเพียงใดเพื่อที่จะใช้ชีวิตให้ผ่านพ้นไปได้ในแต่ละวัน เห็นว่าความพยายามที่แบกไว้นั้นหนักอึ้ง\nเพียงใด เหมือนอย่างที่ฉันต้องแบก"

# n "Even the brightest smile is just slightly subdued, every outburst of annoyance just slightly dampened. It's subtle, but it's definitely there."
n "แม้รอยยิ้มที่สดใสที่สุดก็ถูกลดทอนลงเสี้ยวหนึ่ง ทุกความไม่พอใจที่ระเบิดออกมาก็ถูกกดทับไว้เสี้ยวหนึ่ง มองยาก\nแต่สัมผัสได้ว่ามีแน่"

nvl clear

# n "I try to think what it means, what I can learn from others. I wonder if deep down, everyone is as lost as I am. Is there even one person in here who has truly found peace? I start to feel doubtful about myself once again."
n "ฉันทวนคิดดูว่าสิ่งที่จะได้เรียนรู้จากคนอื่นนั้นหมายความว่ายังไงกันแน่ ลึก ๆ แล้วทุกคนที่นี่ต่างก็มองไม่เห็นทาง\nเหมือนกับฉันหรือเปล่า มีใครสักคนไหมที่ปล่อยตัวปล่อยใจให้สบายได้แล้วจริง ๆ ฉันนึกเคลือบแคลงตัวเองขึ้นมา\nอีกครั้ง"

# n "I can't decide whether these people are happy, unhappy, or if they've just learned to cope and now live in an unfeeling limbo like I did all spring."
n "บอกไม่ถูกด้วยซ้ำว่าคนพวกนี้นั้นมีความสุข ไม่มีความสุข หรือแค่ทำใจปล่อยไปแล้วใช้ชีวิตอยู่อย่างคาราคาซัง\nไม่มีความรู้สึกอะไรเหมือนอย่างที่ฉันเป็นตลอดฤดูใบไม้ผลินั้น"

# n "I escape from these feelings into the towering piles of books I carry to my room from Yuuko's sanctuary. After realizing that this will just shut me down even more, I start going to the art club's room more often, usually whenever I can."
n "ฉันหลีกหนีจากความรู้สึกเหล่านั้นไปอยู่กับกองหนังสือที่ฉันขนมาจากแดนอารักขาของยูโกะ แต่พอรู้ตัวว่ายิ่งทำแบบนั้นจะยิ่ง\nทำให้เก็บตัวหนักกว่าเก่าฉันก็เริ่มใช้เวลาว่างที่พอมีแวะมาที่ห้องชมรมศิลปะให้บ่อยขึ้น"

# n "\nRin too seems to spend more time in there than in her own classroom."
n "\nรินเองก็ดูจะมาอยู่ที่ห้องนี้บ่อยกว่าห้องเรียนตัวเองเสียอีก"

# n "I've often seen her totter towards the door at the very end of our corridor. That wooden door and the room behind it, smelling of paint and paper, seem to mean more to her than the rest of the world combined."
n "ฉันเห็นเธอเดินเตาะแตะไปตรงสุดโถงทางเดินอยู่บ่อย ๆ ประตูบานนั้น ห้องนั้น กลิ่นสีและกระดาษ เหล่านั้นดูจะ\nมีความหมายต่อเธอมากกว่าส่วนที่เหลือของโลกทั้งใบรวมกันด้วยซ้ำ"

# n "She says she has special permission to use the room, which I don't doubt at all. I don't think Nomiya would deny Rin anything."
n "เธอบอกว่าเธอได้รับอภิสิทธิ์ในการใช้ห้องนั้น ซึ่งฉันเชื่อสนิทใจ โนมิยะคงไม่มีทางปฏิเสธอะไรรินแน่นอน"

# n "He seems to dote on her like an uncle upon a favorite niece."
n "เขาเอ็นดูเธออย่างลุงที่เอ็นดูหลานคนโปรด"

nvl clear

# n "\n\n\nThe object of his affection, however, has no favorites. She says she appreciates the teacher a lot for going the extra mile for her sake, but even when she says that, her expression is the same as always."
n "\n\n\nแต่คนโปรดที่ว่านั้นไม่ได้โปรดอะไรเลย เธอบอกว่าเธอก็ขอบคุณที่คุณครูอุตส่าห์ทุ่มเทเพื่อเธอ แต่แม้ปากเธอจะพูด\nอย่างนั้น ทว่าสีหน้าของเธอยังคงเหมือนเก่า"

# n "It's as if she was talking about a particularly unremarkable rock that she saw the other day. I can't really figure out their relationship."
n "ราวกับว่าเธอพูดถึงหินก้อนหนึ่งที่ไม่ได้น่าจดจำอะไรที่เธอเห็นเมื่อวันก่อน ฉันดูไม่ออกว่าความสัมพันธ์ของสองคนนั้น\nเป็นอย่างไหนกันแน่"

# n "Rin doesn't seem to let anyone close. I don't think even Emi could say she's crossed the gap that seems to separate Rin from the rest of the world."
n "รินดูจะไม่ยอมให้ใครเข้าใกล้ ฉันว่าแม้แต่เอมิก็ยังก้าวข้ามระยะห่างที่กั้นตัวรินออกจากโลกทั้งใบนั้นไปไม่ได้"

# n "\n\nI don't understand it. She seems so indifferent, yet so passionate at the same time."
n "\n\nไม่เข้าใจเลย เธอดูไม่สนใจอะไร ทว่าก็ดูมีความคลั่งไคล้"

play sound sfx_normalbell

# n "Somewhere, the school bells ring the last call of the day."
n "เสียงระฆังดังเตือนเวลาเลิกเรียนมาจากสักที่ในโรงเรียน"

stop music fadeout 5.0

nvl hide dissolve
nvl clear

scene bg school_classroomart
with locationchange

window show

# "I realize I've been zoning out for who knows how long. Dazed, I sit up straighter, trying to look as inconspicuous as possible."
"นี่ฉันเอาแต่นั่งเหม่อลอยมานานแล้วเหรอเนี่ย ฉันยืดตัวนั่งตรงทั้งที่ยังเบลอ ๆ ทำตัวให้ดูปกติที่สุด"

# "The pungent smells of linseed oil and turpentine mix in my nostrils as I draw a deep breath. I feel drowsy and lightheaded."
"พอสูดหายใจเข้าลึก ๆ ก็ได้กลิ่นฉุนของน้ำมันลินสีดและน้ำมันสนเข้าเตะจมูก รู้สึกทั้งสะลึมสะลือทั้งอึน ๆ"

# "It's already this late and a few club members left early, so it's just me, Rin, the teacher, and two other girls who are also about to leave."
"เวลาก็ผ่านไปนานมากแล้ว สมาชิกชมรมบางคนก็กลับไปก่อน ทั้งห้องจึงเหลือแค่ฉัน ริน คุณครู แล้วก็สาวอีกสองคน\nที่เตรียมจะกลับแล้วเหมือนกัน"

play music music_soothing fadein 4.0

scene ev rin_painting_base
with locationchange

# "Rin is sitting to my right, slowly working on a painting while I'm idling the time away. I don't think she realizes I've been watching her this whole time."
"รินนั่งอยู่ทางขวามือฉันวาดรูปอยู่อย่างช้า ๆ ระหว่างที่ฉันนั่งไปเรื่อยเปื่อย ไม่รู้ตัวด้วยซ้ำมั้งว่าฉันเอาแต่มองเธอ\nตอนวาดรูปอยู่ตลอด"

scene ev rin_painting_foot:
   xalign 0.5 yalign 0.0 subpixel True
   ease 7.0 yalign 1.0
with locationchange

# "With a nimble move of her delicate ankle, she dips the brush into crimson paint and presses it lightly onto the canvas. A stain spreads around, as if the brush was bleeding."
"เธอขยับข้อเท้าที่คีบพู่กันไว้อย่างทะมัดทะแมงจุ่มสีชาดแล้วกดลงกับผืนผ้าใบเบา ๆ รอยสีแผ่ออกราวกับว่าพู่กันนั้น\nเลือดไหล"

# "Her progress has slowed down to a crawl. By now I've learned that this is dangerous for her technique, as the paint must not be allowed to dry before she's finished."
"งานเธอนั้นเดินช้าลงไปอีก ซึ่งตอนนี้ฉันรู้แล้วว่าไม่ดีกับวิธีวาดของเธอแน่ เพราะต้องห้ามให้สีแห้งจนกว่าจะวาดเสร็จ"

# "It occurs to me that I am literally watching paint dry. And yet somehow I'm not feeling bored, despite spacing out just now."
"และฉันก็เพิ่งรู้ตัวว่าตัวเองกำลังนั่งดูสีแห้งแบบตรงตามตัวอักษร แต่กลับไม่เบื่อเลย ทั้งที่เมื่อกี้เหม่ออยู่แท้ ๆ"

window hide

$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene ev rin_painting_base
with locationchange

nvl clear
nvl show dissolve

# n "\n\nMost of the time, the art club is very relaxed and free-form. Apart from times when Nomiya gets really excited about some technique or style he wants to teach us about, everyone is free to pursue their own interests."
n "\n\nชมรมศิลปะส่วนมากก็จะสบาย ๆ ปล่อยอิสระมาก ๆ ยกเว้นบางครั้งที่โนมิยะจะตื่นเต้นอยากบรรยายเรื่องวิธีหรือ\nแนวการวาดที่เขาอยากเอามาสอน แต่นอกนั้นทุกคนจะทำอะไรที่ตัวเองสนใจก็ทำได้เต็มที่"

# n "Lacking one, I keep floating around without a direction. I try this and that, but nothing really leaves me with a deeper impression, not to mention that I don't seem to have a special knack for anything."
n "และในเมื่อฉันไม่มีสิ่งที่สนใจจึงได้แต่เลื่อนลอยไร้ทิศทาง ก็ลองทำนั่นทำนี่อยู่หรอก แต่ไม่มีอะไรที่ฉันประทับใจ\nเป็นพิเศษเลย แล้วยิ่งฉันดูจะไม่มีฝีมือทำอะไรสักอย่างอีกต่างหาก"

# n "Well, I did get praised for my attempt at watercolors, and I felt pretty good about that, myself, but that's it."
n "ก็ได้รับคำชมมาตอนที่ลองใช้สีน้ำอยู่หรอก ซึ่งฉันก็ค่อนข้างภูมิใจเหมือนกัน แต่ก็แค่นั้นแหละ"

# n "I suppose it's to be expected. I joined the art club mostly on a whim, after all."
n "ก็คงไม่แปลกละมั้ง ในเมื่อฉันมาเข้าชมรมศิลปะแบบนึกอยากเข้าก็เข้า"

# n "I'm thinking that maybe I should quit the club, if it's going to be this pointless. But there's nothing really wrong with pointlessness and I can't exactly say I'm unhappy."
n "ฉันคิดอยู่ว่าหรือจะลาออกจากชมรมดี ถ้าจะมาแล้วไร้ค่าขนาดนี้ แต่ความไร้ค่ามันก็ไม่ได้ผิดอะไร แล้วฉันก็ไม่ได้\nไม่มีความสุขขนาดนั้น"

# n "\nUnsatisfied maybe, but I've got only myself to blame for that."
n "\nอาจจะไม่พอใจมั้ง แต่จะโทษใครได้ นอกจากตัวฉันเอง"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

scene bg school_classroomart
with locationchange

window show

# "As the pair of girls exit the club room with a cheerful “bye-bye”, Nomiya stands up from his desk. His chair scoots back with a loud screech that breaks the harmony of this quiet afternoon."
"เมื่อสาวสองคนนั้นออกห้องชมรมไปด้วยคำว่า “บ๊ายบาย” อันสดใสแล้วโนมิยะก็ลุกขึ้นยืน เสียงขยับเก้าอี้ดังเอี๊ยด\nของคุณครูทำลายความสงบเงียบยามบ่ายนี้"

# "He taps a pile of papers in his hands twice against the tabletop in order to straighten them, then stretches his back."
"เขาจับตั้งกระดาษที่อยู่ในมือตอกกับโต๊ะสองครั้งให้เป็นระเบียบแล้วยืดตัว"

show nomiya smile
with charaenter

# no "I have a faculty meeting to attend, so I can't stay. I'll have to do some paperwork later, so if you want to stay we can talk then. Sorry about this."
no "ฉันมีประชุมฝ่ายต่อ ต้องไปแล้วละ แล้วเดี๋ยวหลังจากนั้นต้องมาจัดการเอกสารอีก เพราะงั้นถ้าจะยังอยู่ก็ไว้ค่อยคุยกัน\nตอนฉันกลับมาอีกทีก็ได้นะ ขอโทษที"

# "There are two people here, but he's really talking to only one of us. Nomiya spends extra hours of his time mentoring Rin after official club hours are over, and I'll bet he'd like to discuss his plan of getting Rin's art into a gallery a little more."
"ในห้องมีนักเรียนอยู่สองคน แต่จริง ๆ ก็คุยอยู่กับคนเดียวน่ะนะ โนมิยะจะเอาเวลาว่างมาติวให้รินนอกเวลา\nกิจกรรมชมรมด้วย แล้วก็คงจะอยากคุยเรื่องแผนที่จะเอางานของรินไปจัดแสดงที่หอศิลป์อีกสักหน่อยนั่นแหละ"

scene ev rin_painting_base
with locationchange

# rin "It's all right. I think I'll probably be here, but it's not a big deal if I'm not. I don't really have much going now."
rin "ไม่เป็นไรค่ะ อาจจะอยู่ที่นี่ แต่ไม่อยู่ก็ไม่เป็นไร ตอนนี้ไม่ได้มีอะไรเท่าไหร่อยู่แล้วค่ะ"

# "Rin answers without moving her eyes from her work in progress. The tone of her voice is neither the polite kind expected when talking to a teacher, nor her usual monotone."
"รินตอบโดยยังไม่ละสายตาไปจากภาพที่เธอยังวาดไม่เสร็จ น้ำเสียงเธอไม่ได้มีความสุภาพจ๋าอย่างที่คนปกติจะคุยกับครู\nแต่ก็ไม่ได้เป็นเสียงเรียบอย่างที่เธอพูดแบบปกติ"

# no "So I won't need to send a search party if you aren't here?"
no "แปลว่าถ้าไม่เจอเธอที่นี่ก็ไม่ต้องส่งทีมออกตามหาตัวเธอนะ"

# rin "Yes, no thanks, I don't like to party. We can talk later."
rin "ค่ะ ไม่ต้อง ขอบคุณค่ะ พอดีไม่ชอบทำอะไรเป็นทีม ไว้ค่อยคุยกันได้ค่ะ"

scene bg school_classroomart
show nomiya veryhappy
with locationchange

# no "Good girl."
no "เด็กดี"

hide nomiya
with charaexit

stop music fadeout 6.0

# "Smiling, the teacher picks up the rest of his papers and makes his way to the door. I glance at the clock above it and then at my watch to double check."
"คุณครูยิ้มพลางเก็บกองกระดาษที่เหลือแล้วเดินออกประตูไป ฉันแหงนหน้ามองนาฬิกาแล้วก้มมองที่นาฬิกาข้อมือ\nของตัวเองเพื่อดูให้แน่ใจ"

# "They're three minutes apart, but nevertheless the club's meeting time is over now."
"คลาดกันไปสามนาที แต่ยังไงก็เลยเวลาชมรมเลิกมาแล้ว"

# "Rin seems intent on staying here to work on her piece while waiting for the teacher."
"รินน่าจะยังอยู่วาดภาพของเธอต่อระหว่างที่รอคุณครู"

# "I can't quite imagine what their one-on-one time would be like."
"นึกภาพไม่ค่อยออกเลยว่าถ้าสองคนนี้คุยกันแบบตัวต่อตัวแล้วจะเป็นยังไง"

# "Would they actually discuss anything? Rin is always so subdued in what she says, and when she does say something it's difficult to understand what she's talking about."
"จะได้คุยอะไรกันจริง ๆ เหรอ รินเป็นคนที่ไม่พูดอะไรตรง ๆ พอพูดอะไรทีก็แทบจะไม่เข้าใจว่าพูดอะไรอยู่"

# "Maybe Nomiya just talks endlessly like he does at club meetings, letting Rin absorb what she will from his infinite well of art knowledge, like a sunflower turning to face the glowing sun."
"อาจจะมีแค่โนมิยะที่พูด ๆ ๆ อยู่คนเดียวเหมือนตอนทำกิจกรรมชมรมแล้วปล่อยให้รินซึมซับอะไรก็ตามที่ออกมาจาก\nคลังความรู้ทางศิลปะที่ไร้สิ้นสุดของเขา เหมือนอย่างที่ดอกทานตะวันหันหน้าเข้าหาดวงอาทิตย์"

scene ev rin_painting_base
with locationchange

# hi "Do you mind if I stay? I er… thought maybe I'd give watercolors another try."
hi "ขออยู่ด้วยได้มั้ย ฉัน เอ่อ… ว่าจะลองใช้สีน้ำดูอีกสักรอบน่ะ"

# "I blurt out the excuse sort of accidentally, embarrassing myself. Rin doesn't take her eyes off her painting."
"ข้ออ้างนั้นหลุดออกมาโดยไม่ตั้งใจจนฉันเขิน รินยังคงไม่ละสายตาไปจากภาพที่เธอวาด"

# rin "Okay."
rin "ได้"

scene bg school_classroomart
with locationchange

# "I shift around in my chair, then get to fetching a cup of water, brushes, colors and some paper. The sound of my footsteps invades the still afternoon air."
"ฉันลุกขึ้นยืนเดินไปหยิบแก้วน้ำ พู่กัน สี แล้วก็กระดาษสองสามแผ่น เสียงฝีเท้าของฉันดังอยู่ท่ามกลางอากาศยามบ่าย"

# "Before starting, I try to recall what the teacher told us, an important philosophy of the medium: working with watercolors means more working with water than working with color. I try to keep that in mind, and dip my tiny sable brush into the water cup."
"ก่อนลงมือฉันนึกย้อนถึงสิ่งที่คุณครูสอน แนวคิดของสีน้ำคือการใช้น้ำมากกว่าการใช้สี ฉันจำไว้ให้ขึ้นใจแล้วจุ่ม\nพู่กันขนเซเบิลลงในแก้วน้ำ"

# "I'm mixing yellow and blue, trying to capture the sunlit treetops outside of the window. The sun is low, so the yellows are more pronounced and everything looks darker."
"ฉันผสมสีเหลืองกับสีน้ำเงินให้คล้ายกับสีแดดที่ส่องอยู่ตรงต้นไม้นอกหน้าต่าง พระอาทิตย์คล้อยต่ำจนสีเหลือง\nเด่นขึ้นมาและทำให้บริเวณรอบ ๆ ดูมืดลง"

# "I still can't quite connect what I see with what my hand does with the paints, but it's a passable attempt for my level."
"ฉันยังจับสิ่งที่ตาเห็นมาลงกับสีที่อยู่กับมือได้ไม่เป๊ะเท่าไหร่ แต่ก็ถือว่าผ่านแล้วสำหรับคนระดับฉัน"

# "After a while I start losing my focus and move the paper aside, deciding to watch Rin work for a while, instead."
"ผ่านไปสักหน่อยก็เริ่มไม่มีสมาธิ ฉันพักกระดาษทิ้งไว้แล้วหันมาดูรินวาดภาพสักหน่อยแทน"

# "That little while stretches first into a long while, then into a really long while."
"ทีแรกสักหน่อยที่ว่าก็เริ่มไม่หน่อย แล้วก็นานจนไม่หน่อยเข้าจริง ๆ"

play music music_dreamy fadein 1.0

scene ev rin_painting_base
with locationchange

# "Rin paints, her entire being fully concentrated on the brush between her slender toes and the painting coming to life one stroke at a time."
"รินลงสีโดยที่ทุกส่วนในร่างกายเธอจดจ่ออยู่กับพู่กันที่อยู่ตรงง่ามนิ้วเท้าเรียวที่กำลังเติมชีวิตให้ภาพทีละหนึ่งฝีแปรง"

# "She seems determined and yet at the same time relaxed, effortlessly moving the brush around, never hesitating. Colors meet and part, mix and cover each other on the canvas, bending to her quiet will."
"เธอดูมุ่งมั่น ทว่าก็ดูผ่อนคลาย เธอสะบัดพู่กันไปมาอย่างไม่ลังเลเลย สีบรรจบและแยกจากกัน ผสมกลมกลืนซ้อนทับกัน\nอยู่บนผืนผ้าใบ สีเหล่านั้นแปรร่างไปตามเป้าหมายที่เงียบเชียบของเธอ"

# "I don't know anything about composition, structure or any of that stuff, but I really like Rin's paintings. I like how she looks when she paints."
"ฉันไม่มีความรู้เรื่ององค์ประกอบ โครงสร้าง หรืออะไรเลย แต่ฉันชอบภาพที่รินวาดมาก ๆ ฉันชอบสีหน้าเวลาที่เธอ\nวาดรูป"

# "As usual, the silence between us compels me to speak rather than merely wait for her to open up. She might end up saying nothing at all."
"และความเงียบก็เป็นสิ่งที่ทำให้ฉันรอไม่ไหวต้องเปิดปากพูดก่อนเธอเช่นเคยเพราะไม่งั้นเธอคงจะไม่พูดอะไรเลย"

# hi "Do you mind if we talk?"
hi "คุยหน่อยได้มั้ย"

scene ev rin_painting_reply
with locationchange

# rin "I don't mind."
rin "ได้"

# hi "I kinda wanted to ask more about why you get so weird about this thing the teacher wants to arrange for you."
hi "ฉันอยากถามหน่อยว่าทำไมเธอถึงได้ทำตัวแปลก ๆ ทุกครั้งที่ครูมาคุยเรื่องงานนั้นที่ครูจะจัดให้"

# "Rin picks up a tube of paint and squeezes it between her toes on a palette almost as easily as someone with opposable thumbs would. Taking up a brush again, she replies."
"รินคีบหลอดสีแล้วบีบด้วยนิ้วโป้งเท้าได้อย่างง่ายดายไม่ต่างไปจากคนที่ใช้นิ้วหัวแม่มือได้ตามปกติ เธอคีบพู่กันขึ้นมา\nอีกครั้งแล้วตอบ"

scene ev rin_painting_concerned
with locationchange

# rin "A lot of things. And some not-things. Unthings. I don't think that's a word."
rin "หลายอย่าง แล้วก็บางไม่อย่าง ออย่าง ไม่น่าใช่คำ"

# hi "Do you want to talk about it?"
hi "อยากจะพูดให้ฟังมั้ย"

# "I try to reach out to her clumsily, ignoring the embarrassing feeling of awkwardness. Rin keeps her focus on the painting, spreading more and more paint on the canvas, her lips forming a perfectly straight line as she concentrates on the job."
"ฉันพยายามเข้าใกล้ชิดรินอย่างเก้ ๆ กัง ๆ โดยไม่สนใจความกระอักกระอ่วนที่ชวนให้เขินอาย รินยังตั้งสมาธิอยู่\nกับภาพวาดพลางเติมแต่งสีลงบนผืนผ้าใบอีก ปากเธอเม้มเป็นเส้นตรงขณะที่เธอจดจ่ออยู่กับภาพนั้น"

scene ev rin_painting_base
with locationchange

# rin "Not really."
rin "ไม่เท่าไหร่"

scene ev rin_painting_reply
with locationchange

# rin "Talking is hard. I mean, it's not hard, I'm talking even now. But saying the right things is really hard for me."
rin "ให้พูดอะไรมันยาก คือ ก็ไม่ยากหรอก ขนาดตอนนี้ก็พูดอยู่ แต่สำหรับฉัน การที่คิดว่าจะพูดอะไรดีน่ะยากมาก"

scene ev rin_painting_concerned
with locationchange

# rin "No matter what, I just can't say the things I want."
rin "ไม่ว่าจะยังไง ฉันก็พูดสิ่งที่อยากจะพูดไม่ได้เลย"

# hi "That sounds weird."
hi "ฟังดูแปลกนะ"

scene ev rin_painting_base
with locationchange

# rin "It's true. I say all kinds of things that I don't really mean all the time. And sometimes I forget words and then I use the wrong words. I even come up with new words for things that already have some. That's the worst thing."
rin "จริง ๆ นะ ฉันพูดอะไรเลื่อนลอยที่ไม่ได้จงใจจะพูดตลอด บางทีฉันก็ลืมคำแล้วก็ใช้คำผิด หรือใช้คำใหม่กับอะไรที่มี\nอยู่แล้วอีก แบบนั้นน่ะแย่ที่สุดเลยละ"

# rin "I get really nervous and everything comes out a mess and even I don't really understand what I want to say."
rin "ฉันจะลนลานมากแล้วทุกอย่างก็วุ่นวายไปหมดแล้วฉันก็ไม่รู้จริง ๆ ว่าฉันอยากจะพูดอะไร"

scene ev rin_painting_concerned
with locationchange

# rin "I think there's something wrong with me that makes it like this. Remember when I said I can only think of four things at the same time?"
rin "ฉันว่าฉันต้องมีอะไรผิดปกติแน่ ๆ จำตอนที่บอกว่าฉันคิดอะไรได้แค่ทีละสี่อย่างมั้ย"

# "I nod wordlessly."
"ฉันพยักหน้าไม่พูดอะไร"

scene ev rin_painting_reply
with locationchange

# rin "It's not really four. I mean, it is four, but everything else is also there kind of in the background. Like being at an amusement park and a beehive at the same time. But that's not the point."
rin "จริง ๆ แล้วไม่ใช่สี่อย่าง คือ ก็สี่อย่างแหละ แต่อย่างอื่นจะประมาณว่าไม่ได้ชัด เหมือนอยู่ในสวนสนุกกับรังผึ้ง\nพร้อม ๆ กัน แต่นั่นไม่ใช่ประเด็น"

# rin "I used to do better. Like six or seven things. I think so, at least. I feel like I'm becoming dumber."
rin "ฉันเคยเก่งกว่านี้ หกอย่างเจ็ดอย่างงี้ ฉันคิดว่างั้นละคนหนึ่ง รู้สึกเหมือนตัวเองโง่ลงเลย"

# hi "I think everyone has times when they feel like they can't say the right things."
hi "ฉันว่าทุกคนก็เคยรู้สึกว่าตัวเองไม่รู้ว่าจะพูดอะไรดีเหมือนกันนั่นแหละ"

scene ev rin_painting_base
with locationchange

# rin "But it's there all the time. Stronger and deeper. Yeah, deeper is a good word. I like that word. Deeper."
rin "แต่มันเป็นอย่างนั้นตลอดเลย ยิ่งหนักข้อและล้ำลึก อืม ล้ำลึกก็เป็นคำที่ดี ฉันชอบคำนั้นนะ ล้ำลึก"

# rin "It's that feeling of being underwater. Maybe it's just art."
rin "เป็นความรู้สึกที่เหมือนจมน้ำ อาจจะแค่ศิลปะมั้ง"

scene ev rin_painting_reply
with locationchange

# rin "The more I paint, the more words I forget. Maybe at some point I will forget how to speak completely."
rin "ยิ่งฉันวาดฉันก็ยิ่งลืมคำ บางทีสักวันฉันอาจจะพูดไม่เป็นไปเลยก็ได้"

# rin "It feels like I'm slowly forgetting everything. Do you remember what you thought about things three or four years ago?"
rin "เหมือนกับว่าฉันค่อย ๆ ลืมทุกอย่างไป นายจำได้มั้ยว่าเมื่อสี่ปีที่แล้วนายคิดกับอะไรว่ายังไง"

# rin "I don't."
rin "ฉันจำไม่ได้"

# "A long pause ensues, during which time seems to bend around itself, almost tying itself into a knot. I don't think I've ever heard Rin talk this earnestly and for so long about anything before."
"ตามด้วยช่วงเงียบแสนยาวนานที่คล้ายว่าเวลาขดเข้ากับตัวเองจนแทบพันเป็นเงื่อน รู้สึกเหมือนจะไม่เคยเห็นริน\nพูดอะไรจากใจขนาดนี้หรือนานขนาดนี้มาก่อนเลย"

scene ev rin_painting_concerned
with locationchange

# rin "It's like I'm fading away from the world."
rin "เหมือนฉันค่อย ๆ จางหายไปจากโลกนี้"

scene ev rin_painting_faceconcerned:
    xalign 0.5 yalign 0.5 zoom 1.0 subpixel True
    easein 10.0 zoom 1.05
with locationchange

# "Rin's foot has stopped its work on the canvas and she is staring at her painting, unmoving, as if gazing at some faraway horizon."
"เท้าของรินชะงักอยู่บนผืนผ้าใบขณะที่เธอจ้องภาพที่เธอวาดอยู่นิ่ง ๆ ราวกับว่ากำลังมองไปยังสุดขอบฟ้าไกล"

# "Sunlight briefly glints in the corner of her onyx eyes. Something floats up into the top layer of Rin's being and she lets out a long breath."
"แสงแดดสะท้อนวับแวมอยู่ที่ตาสีนิลของเธอ บางอย่างลอยขึ้นมาอยู่ที่ตัวตนชั้นนอกของริน เธอถอนหายใจยาว"

scene bg school_classroomart
show rin basic_lucid_close:
    tworight
    ypos 1.1
    0.2
    "rin basic_awayabsent_close" with Dissolve(0.3, alpha=True)
with locationchange

stop music fadeout 0.3

# "Then she blinks and it's gone."
"และพอเธอกะพริบตาสิ่งนั้นก็หายไป"

show rin basic_absent_close
with charachange

# rin "Paintings stay behind. When I look at my old things, I remember what I was thinking back when I made them."
rin "ภาพวาดน่ะเป็นสิ่งคงค้าง เวลามองภาพเก่า ๆ ที่ฉันวาด ฉันจะจำได้ว่าตอนวาดฉันคิดอะไรอยู่"

show rin basic_lucid_close
with charachange

# rin "They make me feel like I can be with all the past mes when I was a different me."
rin "พอได้ดูแล้วก็รู้สึกเหมือนว่าฉันได้อยู่กับตัวฉันในอดีตทุกคนตอนที่ฉันเป็นฉันคนละคน"

show rin basic_awayabsent_close
with charachange

# rin "I guess they are the proof of my existence."
rin "ก็เหมือนเป็นหลักฐานถึงตัวตนของฉันละมั้ง"

# "She uses the exact same words Nomiya used when he spoke to us of the nature of art. I didn't think Rin was paying any attention, back then. I wonder if she was listening, or whether she had heard the same passionate speech from Nomiya before."
"เธอใช้คำเดียวกันกับตอนที่โนมิยะบรรยายเรื่องเนื้อแท้ของศิลปะ ตอนนั้นฉันนึกว่ารินไม่ได้ฟังอยู่ เธอฟังอยู่หรือเปล่านะ\nหรือว่าเคยฟังบทบรรยายอันเปี่ยมพลังของโนมิยะมาก่อนหน้านี้แล้วกัน"

# "Either way, I feel overwhelmed."
"แต่ยังไงก็เถอะ ฉันประมวลผลไม่ทันแล้ว"

# hi "Boy, are you complicated. I would've taken up writing a diary."
hi "โห เอาเรื่องเหมือนกันนะเธอเนี่ย เป็นฉันคงมาหัดเขียนไดอารีแล้ว"

show rin basic_absent_close
with charachange

show rin basic_awayabsent_close
with charachange

# "Her eyes quickly flicker to my direction and then back to the painting, but she doesn't pick up the brush any more."
"เธอเหล่มองมาทางฉันแวบหนึ่งก่อนจะกลับไปมองที่ภาพวาด แต่เธอไม่ได้คีบพู่กันแล้ว"

play music music_rin fadein 0.5

# rin "That's a great idea. Why didn't I ever think of that?"
rin "ความคิดดีนี่ ทำไมฉันถึงคิดไม่ได้นะ"

# hi "Are you being sarcastic?"
hi "นี่ประชดเหรอ"

show rin basic_deadpan_close
with charachange

# rin "What's sarcasm?"
rin "อะไรคือประชด"

# "I don't call her on the joke, if it is one."
"ฉันไม่ต่อปากเล่นกับเธออีก ถึงจะไม่รู้ว่าพูดเล่นจริงหรือเปล่าก็เถอะ"

show rin basic_awayabsent_close
with charachange

# "Right at that moment, Nomiya returns from his meeting. He waves to us a very melodramatic hello, mildly surprised to see me here along with his pet student. Walking with a boisterous gait to his desk, he drops his papers upon it."
"และทันใดนั้นเองโนมิยะก็กลับมาหลังประชุมเสร็จ คุณครูโบกมือทักทายให้อย่างที่คนในละครน้ำเน่าทำกัน ดูจะแปลกใจ\nเล็กน้อยที่เห็นฉันอยู่กับลูกรัก เขาเดินขึงขังมาที่โต๊ะแล้ววางกระดาษลง"

# "He picks up a handkerchief and cleans his glasses with incredibly meticulous care before walking over to us."
"เขาหยิบผ้าเช็ดหน้าขึ้นมาแล้วบรรจงเช็ดแว่นเป็นอย่างดีก่อนจะเดินมาหาพวกเรา"

# "Before he is within earshot of us, Rin says something to me in a quick, quiet voice."
"ก่อนที่เขาจะทันได้เดินเข้ามาใกล้พอได้ยินอะไร รินพูดสั้น ๆ เสียงค่อยกับฉัน"

stop music fadeout 0.5

show rin basic_absent_close
with charachange

# rin "Change is the scariest thing in the world to me."
rin "ฉันกลัวการเปลี่ยนแปลงที่สุดในโลกเลย"

show rin basic_upset_close
with charachange

# rin "And I seriously don't know if I want to change into a person who could do the thing the teacher wants me to do. I don't know if I could even if I wanted to."
rin "แล้วฉันก็ไม่รู้จริง ๆ ว่าฉันจะเปลี่ยนเป็นคนที่ทำอะไรอย่างที่ครูอยากให้ฉันทำได้หรือเปล่า ฉันไม่รู้ว่าต่อให้อยากจริง ๆ\nแล้วฉันจะทำได้หรือเปล่า"

show nomiya talk behind rin at twoleft
with charaenter

# no "Hello again!"
no "สวัสดีอีกครั้ง!"

# $ doublespeak(hi,rin,"Hello.")
$ doublespeak(hi,rin,"สวัสดี")

show nomiya smile
with charachange

play music music_pearly fadein 5.0

# no "What's going on?"
no "มีอะไรกัน"

# "He smiles a bit sheepishly, looking at both of us with uninhibited interest."
"เขายิ้มอายน้อย ๆ แล้วมองเราสองคนด้วยความอยากรู้เต็มสูบ"

# hi "Ah, nothing. We were just talking about that thing with your acquaintance and the gallery. For Rin's works. Sort of."
hi "เอ้อ ไม่มีอะไรครับ พอดีกำลังคุยกันเรื่องเพื่อนครูแล้วก็เรื่องหอศิลป์อยู่ งานรินน่ะนะครับ ประมาณนั้น"

show nomiya veryhappy
with charachange

# no "Oho? Any decisions?"
no "โอ้ แล้วว่ายังไง"

# "I look at Rin, who is trying to arrange the bothered expression on her face into something else."
"ฉันมองไปทางรินที่กำลังดัดหน้าเครียดของเธอให้เป็นอะไรอย่างอื่นอยู่"

################

#this choice is a bit tricky. each conditional from the three previous choices in this act corresponds to one option in this one. So there will always be three options in this choice, depending on how player chose earlier.

#choice_R2: "You're amazing"/R2a corresponds to "I think you'd be a big hit". "I wish I was as good as you"/R2b corresponds to "You'd be wasting your talents otherwise"
#choice_R6: "It's refreshing"/R6a corresponds to "It would be exciting". "I feel like I'm stuck"/R6b corresponds to "You won't get a chance like this again."
#choice_R9: "I want to be more like  Rin"/R9a corresponds to "This isn't like you". "I want to be more like Emi" corresponds to "You should aim higher."
#so for example if the player chooses "You're amazing," "I feel like I'm stuck" and "I want to be more like Rin", the options shown for this choice would be the first three listed below.
#I didn't want to work this in imachine because it would've been clumsy as I suck ass. So very Grid1-like
# for more precise flow control, you can change around what corresponds to what. I think it's now possible to get combinations of options that are pretty random (like two that lead to rin being angry or whatever)

#    "I think you'd be a big hit.":
        #return m1

#    "You'd be wasting your talents otherwise.":
        #return m2

#    "You won't get a chance like this again.":
        #return m3

#    "Because it would be exciting.":
         #return m4

#    "It isn't like you at all to hesitate like this.":
        #return m5

#    "You should aim high.":
        #return m6


label th_choiceR11aaa:
menu:
    with menueffect

    # hi "Anyway, I don't think I have much else to say, other than that you should go for it."
    hi "คือผมก็คงไม่มีอะไรจะพูดนอกจากว่า เอาเลย แล้วน่ะนะครับ"

    # "I think you'd be a big hit.":
    "เธอต้องประสบความสำเร็จแน่":
        return m1

    # "Because it would be exciting.":
    "น่าดื่นเต้นดีออก":
        return m4

    # "It isn't like you at all to hesitate like this.":
    "ปกติเธอไม่ลังเลอย่างนี้เลยนี่":
        return m5


label th_choiceR11baa:
menu:
    with menueffect

    # hi "Anyway, I don't think I have much else to say, other than that you should go for it."
    hi "คือผมก็คงไม่มีอะไรจะพูดนอกจากว่า เอาเลย แล้วน่ะนะครับ"

    # "You'd be wasting your talents otherwise.":
    "ไม่เสียดายเหรอ เก่งขนาดนี้":
        return m2

    # "Because it would be exciting.":
    "น่าตื่นเต้นดีออก":
        return m4

    # "It isn't like you at all to hesitate like this.":
    "ปกติเธอไม่ลังเลอย่างนี้เลยนี่":
        return m5


label th_choiceR11aba:
menu:
    with menueffect

    # hi "Anyway, I don't think I have much else to say, other than that you should go for it."
    hi "คือผมก็คงไม่มีอะไรจะพูดนอกจากว่า เอาเลย แล้วน่ะนะครับ"

    # "I think you'd be a big hit.":
    "เธอต้องประสบความสำเร็จแน่":
        return m1

    # "You won't get a chance like this again.":
    "โอกาสอย่างนี้จะไม่มีมาหาเธออีกแล้วนะ":
        return m3

    # "It isn't like you at all to hesitate like this.":
    "ปกติเธอไม่ลังเลอย่างนี้เลยนี่":
        return m5


label th_choiceR11aab:
menu:
    with menueffect

    # hi "Anyway, I don't think I have much else to say, other than that you should go for it."
    hi "คือผมก็คงไม่มีอะไรจะพูดนอกจากว่า เอาเลย แล้วน่ะนะครับ"

    # "I think you'd be a big hit.":
    "เธอต้องประสบความสำเร็จแน่":
        return m1

    # "Because it would be exciting.":
    "น่าตื่นเต้นดีออก":
        return m4

    # "You should aim high.":
    "ต้องตั้งเป้าให้สูงเข้าไว้สิ":
        return m6


label th_choiceR11abb:
menu:
    with menueffect

    # hi "Anyway, I don't think I have much else to say, other than that you should go for it."
    hi "คือผมก็คงไม่มีอะไรจะพูดนอกจากว่า เอาเลย แล้วน่ะนะครับ"

    # "I think you'd be a big hit.":
    "เธอต้องประสบความสำเร็จแน่":
        return m1

    # "You won't get a chance like this again.":
    "โอกาสอย่างนี้จะไม่มีมาหาเธออีกแล้วนะ":
        return m3

    # "You should aim high.":
    "ต้องตั้งเป้าให้สูงเข้าไว้สิ":
        return m6


label th_choiceR11bab:
menu:
    with menueffect

    # hi "Anyway, I don't think I have much else to say, other than that you should go for it."
    hi "คือผมก็คงไม่มีอะไรจะพูดนอกจากว่า เอาเลย แล้วน่ะนะครับ"

    # "You'd be wasting your talents otherwise.":
    "ไม่เสียดายเหรอ เก่งขนาดนี้":
        return m2

    # "Because it would be exciting.":
    "น่าตื่นเต้นดีออก":
        return m4

    # "You should aim high.":
    "ต้องตั้งเป้าให้สูงเข้าไว้สิ":
        return m6


label th_choiceR11bba:
menu:
    with menueffect

    # hi "Anyway, I don't think I have much else to say, other than that you should go for it."
    hi "คือผมก็คงไม่มีอะไรจะพูดนอกจากว่า เอาเลย แล้วน่ะนะครับ"

    # "You'd be wasting your talents otherwise.":
    "ไม่เสียดายเหรอ เก่งขนาดนี้":
        return m2

    # "You won't get a chance like this again.":
    "โอกาสอย่างนี้จะไม่มีมาหาเธออีกแล้วนะ":
        return m3

    # "It isn't like you at all to hesitate like this.":
    "ปกติเธอไม่ลังเลอย่างนี้เลยนี่":
        return m5


label th_choiceR11bbb:
menu:
    with menueffect

    # hi "Anyway, I don't think I have much else to say, other than that you should go for it."
    hi "คือผมก็คงไม่มีอะไรจะพูดนอกจากว่า เอาเลย แล้วน่ะนะครับ"

    # "You'd be wasting your talents otherwise.":
    "ไม่เสียดายเหรอ เก่งขนาดนี้":
        return m2

    # "You won't get a chance like this again.":
    "โอกาสอย่างนี้จะไม่มีมาหาเธออีกแล้วนะ":
        return m3

    # "You should aim high.":
    "ต้องตั้งเป้าให้สูงเข้าไว้สิ":
        return m6


################


label th_R11a:
#"I think you'd be a big hit.":
#"เธอต้องประสบความสำเร็จแน่":

# hi "I think you'd be super popular. I mean, your paintings are really amazing."
hi "เธอต้องดังมากแน่เลย ก็ภาพที่เธอวาดสวยขนาดนั้น"

# hi "And you paint with your feet; that's really cool, too. I bet people will be amazed."
hi "แล้วยังใช้เท้าวาดด้วย สุดยอดจะตายไป คนต้องทึ่งกันแน่ ๆ"

show rin basic_deadpanupset_close
with charachange

# rin "It's not a big deal. I would paint with hands if I had any."
rin "ก็ไม่ได้อะไรขนาดนั้นหรอก ถ้ามีมือฉันก็คงใช้มือวาด"

# hi "Oh… sorry. I'm sorry, I didn't mean it like that."
hi "อ่า… ขอโทษ ขอโทษทีนะ ฉันไม่ได้หมายความอย่างนั้น"

show rin negative_confused_close
with charachange

# "Rin turns away, looking at her painting wistfully. I want to take back what I said if it was what made her make that face."
"รินเบือนหน้าหนีมองภาพเธอเศร้า ๆ ถ้าที่ฉันพูดไปทำให้เธอทำหน้าอย่างนั้นก็อยากจะถอนคำพูดเหลือเกิน"

# rin "I get it."
rin "เข้าใจแล้ว"


label th_R11b:
#"You'd be wasting your talents otherwise.":
#"ไม่เสียดายเหรอ เก่งขนาดนี้":

# hi "You'd be letting your talent go to waste if you don't."
hi "ถ้าไม่ทำก็เสียดายความสามารถเธอออก"

show rin basic_surprised_close
with charachange

# rin "Go where?"
rin "เสีย?"

# hi "To waste. I think it'd be a waste for other people to not see these things."
hi "เสียดาย คงเสียดายที่คนไม่ได้มาเห็นอะไรอย่างนี้น่ะ"

# "I try to press her a little bit, to extract some sort of decisiveness out of her, but Nomiya decides to intervene."
"ฉันกดดันเธอไปนิดหน่อยเผื่อเธอจะตัดสินใจอะไรได้สักที แต่โนมิยะก็เข้ามาขวาง"

show nomiya smile
show rin basic_awayabsent_close
with charachange

# no "Oh, it's not that bad."
no "โอ๊ย ก็ไม่ขนาดนั้นหรอก"

show nomiya talk
with charachange

# no "I agree that it's important to strike when the iron is hot, but Tezuka is still just eighteen. She'll have time and her abilities will mature."
no "บอกให้ตีเหล็กตอนร้อนก็จริง แต่เทซูกะเขาก็ยังอายุเพิ่งสิบแปด ยังมีเวลาให้ความสามารถได้พัฒนาอีกเยอะ"

show nomiya veryhappy
with charachange

# no "That said, there are many advantages for trying to make a break at a young age, if at all possible."
no "ถึงงั้นก็เถอะ แต่ถ้าเปิดตัวดังได้แต่อายุยังน้อยก็ดีหลายอย่างเหมือนกัน ถ้าเป็นไปได้น่ะนะ"

show rin basic_absent_close
with charachange

# hi "Yeah, but…"
hi "ครับ แต่ว่า…"


label th_R11c:
#"You won't get a chance like this again.":
# "โอกาสอย่างนี้จะไม่มีมาหาเธออีกแล้วนะ":

# hi "I mean, the teacher is probably right. You're not going to get a chance like this again."
hi "คือครูเขาก็อาจจะพูดถูกแล้วก็ได้นะ โอกาสอย่างนี้คงไม่มีอีกแล้วละ"

# hi "People don't get many chances in life, and you shouldn't waste any of them even if you have doubts."
hi "คนเรามีโอกาสผ่านมาในชีวิตไม่บ่อยหรอก อย่าเสียเวลามัวลังเลเลย"

show rin basic_absent_close
with charachange

# "Rin stares at me unresponsively. It's like my words don't have any meaning to her at all."
"รินจ้องมองฉันไม่ตอบสนองอะไร เหมือนกับว่าสิ่งที่ฉันพูดไปไม่ได้ทำให้เธอรู้สึกอะไรขึ้นมาเลย"


label th_R11d:
#"Because it would be exciting.":
#"น่าตื่นเต้นดีออก":

# hi "Don't you think it would be exciting? I'd be wild about something like this."
hi "ก็น่าตื่นเต้นดีออกนี่นา เป็นฉันนะคงดีใจจนเป็นบ้าไปแล้ว"

show nomiya talk
with charachange

# no "Hahaha, so would I. But this is about things like your career and future, rather than a youthful adventure. Although there's nothing wrong with enjoying oneself."
no "ฮ่าฮ่าฮ่า ฉันก็เหมือนกันแหละ แต่อันนี้คือเรื่องอาชีพแล้วก็อนาคตนะ ไม่ใช่การผจญภัยอะไรแบบเด็ก ๆ แต่จะสนุก\nไปกับมันบ้างก็ไม่เสียหายหรอก"

# "Nomiya gently reprimands my excitement, but I'm not going to let it go."
"โนมิยะปราม ๆ ฉันไม่ให้ตื่นเต้นมากไป แต่ฉันไม่ยอมหรอก"

# hi "Seriously, everyday life is so dull, you always do the same things every day, in the same way. This would be something else."
hi "จริง ๆ นะ ชีวิตทุกวันนี้จืดชืดจะตาย เธอทำอะไรเดิม ๆ เหมือนเดิมอยู่ทุกวัน ตรงนี้แหละจะได้ลองทำอะไรใหม่ ๆ ไปเลย"



label th_R11e:
#"This isn't like you at all.":
#"ปกติเธอไม่เป็นอย่างนี้นี่"

# hi "This isn't like you. You told me that people should do things they can't, just because they can."
hi "ปกติเธอไม่เป็นอย่างนี้นี่ เธอบอกฉันเองว่าคนเราต้องทำอะไรที่ทำไม่ได้แค่เพราะทำได้"

# hi "And now you're being all wishy-washy yourself about something this important."
hi "แล้วทีนี้เธอดันมาทำตัวใจโลเลกับอะไรที่มันสำคัญขนาดนี้"



label th_R11f:
#"You should aim higher.":

# hi "I really think you should aim higher. You should take the chance."
hi "เธอต้องตั้งเป้าให้สูงเข้าไว้สิ คว้าโอกาสนี้ไว้เลย"

# hi "Even if you crash and burn, at least you tried. It'd be worth it just for that."
hi "ต่อให้จะล้มเหลวกลางทาง แต่อย่างน้อยเธอก็ได้ลอง แค่นั้นก็คุ้มแล้ว"

# "Nomiya sucks in his breath then lets it out after a pause, as if he wants to add something, but he manages to restrain himself. Rin finally replies to me."
"โนมิยะสูดหายใจเข้าแล้วกลั้นหายใจไว้ครู่หนึ่งก่อนจะหายใจออกคล้ายมีอะไรจะพูดแต่ก็ไม่ยอมพูดออกมา และในที่สุด\nรินก็ตอบฉัน"

show rin basic_surprised_close
with charachange

# rin "You don't think I'm good enough like this?"
rin "นายว่าแค่นี้มันยังไม่พอเหรอ"

# hi "No. I think that you're selling yourself short if you think like that. It's cowardly."
hi "ไม่ ฉันว่าเธอประเมินค่าตัวเองต่ำไป เธอขี้ขลาดอยู่นะ"


label th_R11g:
#hisao gets angry
#ฮิซาโอะโมโห

show rin basic_deadpanupset_close
show nomiya smile
with charachange

# "Rin looks absentmindedly at me, not saying anything. I can't even tell if my words had any effect on her."
"รินมองฉันเหม่อ ๆ ไม่พูดอะไร ฉันไม่รู้เลยว่าที่พูดไปจะมีผลอะไรกับเธอบ้างหรือเปล่า"

# hi "I just don't get it. Anyone else would be jumping up and down in excitement."
hi "ฉันไม่เข้าใจจริง ๆ เป็นคนอื่นคงลิงโลดไปแล้ว"

# hi "What's the point of doing your best, being at this art club, if you don't do anything with your talent?"
hi "ถ้าไม่เอาความสามารถออกมาใช้แล้วจะมาทุ่มเทอยู่กับชมรมศิลปะไปทำไม"

# hi "I'm telling you, I'm going to be angry with you if you give this up."
hi "ฉันขอบอกเลยว่าถ้าเธอปล่อยโอกาสนี้ไปฉันโกรธจริง ๆ ด้วย"

# "My voice rises higher. I don't know what makes me say this. It's like I've been taken over by some force out of my control, but I really do feel angry."
"ฉันขึ้นเสียง ไม่รู้อะไรดลใจให้พูดอย่างนั้น เหมือนมีอะไรบางอย่างที่ฉันควบคุมไม่ได้มาสิงร่างอยู่ แต่ฉันโกรธจริง ๆ"

# "Images of a letter written on cute stationery flash in my mind, images of the masked faces of my parents, my doctors, images of the time I've wasted. They mix into my feelings about Rin like a torrent of molten iron."
"ในหัวฉายภาพจดหมายที่เขียนด้วยกระดาษดูน่ารัก ๆ ภาพหน้ากากที่เป็นหน้าพ่อแม่และหมอ ภาพเวลาที่ฉันเสียไป\nทุกอย่างระคนเข้ากับความรู้สึกที่ฉันมีต่อรินราวเกลียววนเหล็กหลอม"

show rin basic_deadpanupset_close at tworight
with charamove

# "I want to continue, but Rin suddenly stands up."
"ฉันจะพูดต่อ แต่รินก็ผุดลุกขึ้นยืน"

# rin "Fine."
rin "ตามใจ"

# rin "I'm going."
rin "ไปละ"

hide rin
with charaexit

# "She trots out of the room without anyone saying anything. I stare after her, still seething, though with the voice of rationality in the back of my head wondering if I made her angry as well."
"เธอวิ่งเหยาะ ๆ ออกห้องไปโดยไม่มีใครพูดอะไร ฉันมองไล่หลังเธอไปด้วยอารมณ์ที่ยังเดือดดาล แต่ความเป็นเหตุผล\nในตัวฉันก็นึกสงสัยว่าไปทำให้เธอโกรธด้วยหรือเปล่า"

show nomiya veryhappy at center
show bg school_classroomart at bgright
with dissolvecharamove

# "The teacher lets out an embarrassed, but extraordinarily loud laugh."
"คุณครูหัวเราะแก้เก้อเสียงดังลั่น"

show nomiya frown
with charachange

# no "You care a lot for her, don't you?"
no "เธอนี่ใส่ใจรินน่าดูเลยนะ"



label th_R11h:
#rin gets angry
#รินโมโห

show rin basic_deadpanupset_close
show nomiya smile
with charachange

# rin "I don't think I want to talk about this."
rin "ฉันว่าฉันไม่อยากคุยเรื่องนี้"

# rin "I'm going."
rin "ไปละ"

show rin basic_deadpanupset_close at tworight
with charamove

hide rin
with charaexit

# "Rin stands up and trots out of the room without anyone saying anything more."
"รินลุกขึ้นยืนแล้ววิ่งเหยาะ ๆ ออกห้องไปโดยไม่มีใครพูดอะไร"

show nomiya smile at center
show bg school_classroomart at bgright
with charamove

# hi "I'm sorry. I think I made her upset."
hi "ขอโทษนะครับ คงไปทำให้โกรธซะแล้ว"

show nomiya veryhappy
with charachange

# no "Hahaha, don't worry about it. She'll be fine, I'm sure. I'll talk to her later."
no "ฮ่าฮ่าฮ่า ไม่ต้องคิดมากหรอก เดี๋ยวก็หายโกรธแหละ ไว้ฉันจะไปคุยกับเทซูกะอีกที"



label th_R11i:
#nomiya disapproves of hisao's idiocy
#โนมิยะปรามที่ฮิซาโอะคิดตื้น ๆ

show nomiya smile
with charachange

# no "Now now, my boy. It's a big decision and even though I'd like Tezuka to be more decisive as well, she needs time to mull it over."
no "เอาละ ๆ ลูก เรื่องนี้เรื่องใหญ่ ถึงฉันจะอยากให้ตัดสินใจให้แน่นอนกว่านี้เหมือนกันก็จริง แต่ปล่อยให้เทซูกะได้คิดก่อน"

show nomiya frown
with charachange

# no "Why don't we let her decide. You have good intentions, but in the end it comes down to her own feelings."
no "ให้เทซูกะเลือกเองดีกว่ามั้ย เธอเจตนาดีก็จริง แต่ท้ายที่สุดก็อยู่ที่ความรู้สึกเจ้าตัวนั่นแหละ"

show nomiya veryhappy
with charachange

# no "Any thoughts on the subject, Tezuka? You've been quiet all afternoon."
no "ว่ายังไงล่ะเทซูกะ เห็นบ่ายนี้เอาแต่เงียบ"

# "We both look at Rin, who doesn't return either of our gazes."
"เราสองคนมองรินที่ไม่มองตาใครตอบเลย"

show rin basic_lucid_close
with charachange

# rin "No. I think I'm going."
rin "ไม่ ไปละค่ะ"

show nomiya talk
with charachange

# no "You are? What a shame. Promise me you'll give me some kind of an answer in a week or so, all right?"
no "ไปแล้วเหรอ เสียดายจัง งั้นรับปากฉันก่อนว่าจะให้คำตอบภายในหนึ่งสัปดาห์ โอเคนะ"

show rin basic_deadpanupset_close
with charachange

# rin "All right."
rin "โอเคค่ะ"

show nomiya smile
with charachange

# no "Good girl."
no "เด็กดี"

show rin basic_deadpanupset_close at tworight
with charamove

hide rin
with charaexit

# "Rin stands up and trots out of the room without anyone saying anything further."
"รินลุกขึ้นยืนแล้ววิ่งเหยาะ ๆ ออกห้องไปโดยไม่มีใครพูดอะไร"

show nomiya smile at center
show bg school_classroomart at bgright
with charamove


label th_R11j:
#everything finally comes back together

# "Nomiya looks at me over his circular pink glasses, smiling sympathetically."
"โนมิยะมองลอดแว่นกลมสีชมพูของเขามาแล้วยิ้มเห็นใจ"

show nomiya talk
with charachange

# no "You've made friends with her then, Nakai?"
no "สนิทกับเทซูกะแล้วงั้นสิ นากาอิ"

# hi "Uh… well, something like that, I guess. Depends on how you look at it. To be honest, I'm not really sure."
hi "เอ่อ… ก็ ประมาณนั้นละมั้งครับ อยู่ที่ว่าจะมองยังไง ให้ว่าตามตรงผมก็ไม่แน่ใจด้วยซ้ำ"

# "It's more like me and Rin just tend to hang around each other irregularly, talking or not about something that more often resembles some twisted mockery of philosophy rather than normal, everyday things that “friends” chat about."
"เหมือนฉันได้มาอยู่กับรินด้วยกันอย่างไม่สม่ำเสมอมากกว่า คุยบ้างไม่คุยบ้าง พอคุยก็จะเหมือนบทล้อเลียนปรัชญา\nเพี้ยน ๆ อะไรสักอย่างมากกว่าจะเป็นเรื่องดินฟ้าอากาศอะไรที่ “เพื่อน” เขาคุยกันตามปกติ"

show nomiya frown
with charachange

# no "Well, that's all good, isn't it? You're a new student and we should be promoting integration into the student body and such. I can't remember all the buzzwords they spew at faculty and Yamaku Foundation meetings, but that's how it is."
no "ก็ ใช้ได้แล้วนี่ เธอเป็นนักเรียนใหม่ก็ควรที่จะเข้ากับกลุ่มนักเรียนที่นี่หรืออะไรประมาณนั้น ฉันจำศัพท์แสงอะไรที่เขา\nใช้คุยกันตอนประชุมฝ่ายกับประชุมมูลนิธิยามากุไม่ได้แล้ว แต่ก็ประมาณนั้นแหละ"

show nomiya veryhappy
with charachange

# no "Tezuka isn't the most social person around these parts, either."
no "เทซูกะเองก็ไม่ใช่คนที่เข้าสังคมหรืออะไรเท่าไหร่เหมือนกัน"

# hi "Yeah, that's definitely true."
hi "ตรงเผงเลยครับ"

show nomiya smile
with charachange

# no "So she's talked about my suggestion to you?"
no "แปลว่าเทซูกะเขาคุยเรื่องที่ฉันเสนอไปกับเธอแล้ว?"

# hi "Oh, no, not really. I think it's been more me pressing her to decide something. Maybe I shouldn't have."
hi "อ้อ ไม่ครับ ไม่เชิง เหมือนผมกดดันรินให้ตัดสินใจอะไรอยู่ฝ่ายเดียวมากกว่า ผมก็ไม่น่าไปกดดันอย่างนั้นเหมือนกัน"

show nomiya talk
with charachange

# no "No, I'm sure it's fine. I'm too soft with her, even when I shouldn't. I don't really know how to handle Tezuka, she's so independent and willful."
no "ไม่หรอก ไม่เป็นไร ฉันเองก็ใจอ่อนกับเธอมากไปจนบางทีก็ใจอ่อนผิดเรื่อง ฉันไม่รู้จะรับมือเทซูกะยังไงดี เป็นคนที่ทั้ง\nไม่พึ่งพาใครเลย แล้วก็รั้นด้วย"

show nomiya talktongue
with charachange

# no "I wonder if this is what every old geezer of an art teacher who got his hands on a young and fiery prodigy felt like."
no "นี่หรือเปล่านะคือความรู้สึกที่ครูศิลปะรุ่นแก่ ๆ ต้องมาดูแลอัจฉริยะน้อยไฟแรงเนี่ย"

show nomiya smile
with charachange

# "He chuckles ironically to himself a little bit, turning to face Rin's latest work which she left drying on the easel. She departed so abruptly that I wonder if she considers it finally finished."
"เขาแค่นหัวเราะแกน ๆ ให้ตัวเองแล้วมองภาพที่รินวาดที่ถูกปล่อยให้แห้งอยู่กับขาตั้ง เธอออกไปอย่างกะทันหันมาก\nเสียจนฉันอยากรู้ว่าเธอจะมองว่าภาพนี้วาดเสร็จแล้วหรือยัง"

show nomiya talk
with charachange

# no "So, let's see the painting then."
no "งั้น มาดูภาพนี้กัน"

# "He leans in closer, peering at the canvas."
"เขาโน้มตัวเข้าเพ่งผืนผ้าใบใกล้ ๆ"

show nomiya frown_close
with characlose

# no "It draws you in, doesn't it?"
no "เห็นแล้วดึงดูดเลยใช่มั้ยล่ะ"

show nomiya dreamy
with charadistant

# "Nomiya stands back straight, his face a dreamy, nostalgic visage. I don't answer him, as he seems to be taking my agreement as a given."
"โนมิยะยืดตัวขึ้นยืนตรงทำหน้าหวนถวิลชวนฝัน ฉันไม่ตอบเพราะเขาก็ถือเอาเองอยู่แล้วว่าฉันคงเห็นด้วย"

show nomiya talk
with charachange

# no "I sometimes stay here after hours just to look at Tezuka's paintings. She's really just prodigious, and at such a young age. I get shivers just thinking of what she could become with a few more years of refinement."
no "บางทีฉันก็อยู่นอกเวลามานั่งดูภาพที่เทซูกะวาดนี่แหละ ฉายแววอัจฉริยะตั้งแต่อายุยังน้อยเลย แค่คิดว่าถ้าฝึกแล้ว\nจะไปได้อีกไกลแค่ไหนฉันก็ตื่นเต้นตัวสั่นเลยละ"

show nomiya frown
with charachange

# no "You asked what makes an artist, remember? This is it. They take a piece of the world and reshape it in their own image. Metaphorically, of course."
no "จำได้มั้ยที่เคยถามว่าศิลปินคืออะไร นี่แหละ ศิลปินคือคนที่บิโลกมาแล้วปั้นใหม่ให้เป็นรูปของตัวเอง แค่เปรียบเปรยนะ"

show nomiya dreamy
with charachange

# no "Looking at her makes you wonder what the world looks like through her eyes. It's a wonderful thing, to be young and full of passion, the most extraordinary time of your life. You would do well to remember that, Nakai."
no "พอได้มองเทซูกะแล้วก็จะสงสัยว่าเธอมองโลกยังไงกัน สุดยอดไปเลยนะการที่ได้เป็นวัยรุ่นที่เป็นช่วงที่พิเศษสุดในชีวิต\nแล้วยังเต็มไปด้วยแรงขับเคลื่อน จำไว้เลยนะนากาอิ"

# hi "Yes, sir."
hi "ครับผม"

show nomiya veryhappy
with charachange

# no "It's so silly."
no "บ้าจริง ๆ นะ"

show nomiya frown
with charachange

# no "People always ask artists “Where do you get your ideas?” as if ideas were something sold at the market for pocket change."
no "คนจะเอาแต่ถามศิลปินว่า “ไปได้ไอเดียมาจากไหน” เหมือนว่าเอาเศษกะตังไปซื้อที่ตลาดก็ได้มาแล้ว"

show nomiya serious
with charachange

# no "You can't explain inspiration. For people like Tezuka, it's like breathing. It's an instinct."
no "แรงบันดาลใจน่ะเป็นอะไรที่อธิบายไม่ได้หรอก สำหรับคนอย่างเทซูกะแล้วมันก็เหมือนกับการหายใจ เป็นสัญชาตญาณ"

# no "I've met maybe one or two with the same kind of raw potential. But no amount of potential will amount to anything if one doesn't work to realize it."
no "คนที่มีศักยภาพพอกันที่ฉันเคยเจอก็มีสักคนสองคนได้มั้ง แต่ศักยภาพมีเท่าไหร่ก็ไร้ค่าถ้าไม่ดึงออกมาใช้"

# no "It's practice, technique, skill. Draw for an hour every day for a few years and even the most hopeless case becomes a passable artist."
no "การฝึกฝน กลวิธี และทักษะต่างหากที่สำคัญ ถ้าให้วาดรูปวันละชั่วโมงทุกวันแล้ว แม้แต่คนที่สภาพดูแล้วสิ้นหวังสุด ๆ\nก็จะยังได้ขึ้นมาเป็นศิลปินแบบพอไปวัดไปวาได้"

show nomiya talk
with charachange

# no "Tezuka is not brilliant because she was born with a natural talent for this kind of thing. She's brilliant because she works harder than anyone, ever since she learned to hold a pen, most likely."
no "เทซูกะไม่ได้เก่งเพราะเกิดมามีพรสวรรค์ทางด้านนี้หรอกนะ ที่เก่งก็เพราะเธอขยันกว่าใคร คงจะขยันมาตั้งแต่\nจับปากกาเป็นเลยนั่นแหละ"

show nomiya veryhappy
with charachange

# no "And all of it with her feet, no less. Absolutely phenomenal."
no "แล้วแถมใช้แค่เท้าด้วยอีกต่างหาก สุดจะบรรยายจริง ๆ"

# "Silence finally lands in the clubroom as Nomiya lets himself get drawn back into Rin's painting, gently murmuring acceptance toward the still-wet canvas."
"ความเงียบกลับเข้ามายังห้องชมรมอีกครั้งหลังโนมิยะหันไปดูภาพที่รินวาดอีกทีพลางพึมพำชมเปาะให้กับผืนผ้าใบ\nที่ยังไม่แห้งดี"

# hi "What kind of things do you paint yourself?"
hi "แล้วครูวาดอะไรเหรอครับ"

show nomiya smile
with charachange

# "As if waking from a reverie, he looks at me, surprised at my talking to him."
"คุณครูหันมามองฉันเหมือนหลุดจากภวังค์ด้วยความตกใจที่ฉันคุยด้วย"

show nomiya talk
with charachange

# no "Oh, I don't. Not any more."
no "อ้อ เลิกแล้ว ไม่วาดแล้ว"

show nomiya smile
with charachange

# no "I became an art teacher only after my career in that field came to an end. Now I just pass on knowledge to the next generation."
no "ฉันมาเป็นครูสอนศิลปะเพราะอาชีพทางฉันมันไปต่อไม่ได้แล้วน่ะ ก็เลยมาส่งต่อความรู้ให้รุ่นต่อไปอยู่นี่แหละ"

# "The way Nomiya answers is curious, both giving and withholding information. I feel like asking more, but he cuts in before I get the chance."
"คำตอบของโนมิยะดูน่าสงสัย ทั้งบอกและไม่บอกอะไรบางอย่าง ฉันนึกจะถามต่อแต่เขาก็ตัดบทก่อนฉันทันได้ถามอะไร"

show nomiya veryhappy
with charachange

# no "Now you should run along, my boy. It's almost dinner time, isn't it?"
no "เอ้า ไปได้แล้วลูก ถึงเวลาข้าวเย็นแล้วนี่"

# hi "Yes, sir. Have a good evening."
hi "ครับผม โชคดีนะครับ"

show nomiya smile
with charachange

# no "You too."
no "เช่นกัน ๆ"

scene bg school_hallway3
with locationchange

stop music fadeout 2.0

# "I quickly collect my stuff and step out into the deserted hallway, leaving the teacher alone with his musings."
"ฉันรีบเก็บกวาดข้าวของแล้วเดินออกมาที่โถงทางเดินปลอดคน ทิ้งให้คุณครูชมภาพต่อไป"

# "The weekend will be here soon. It's amazing how fast time flies here."
"ใกล้จะสุดสัปดาห์แล้ว เวลาผ่านไปไวมากจริง ๆ"

# "I promised Emi I'd join her for the celebration of her triumph at the track meet last week. That should be plenty of fun."
"ฉันสัญญากับเอมิไว้แล้วว่าจะไปร่วมฉลองชัยที่เธอแข่งวิ่งเมื่อสัปดาห์ก่อน ต้องสนุกมากแน่เลย"

scene black
with dissolve

#******************************************

label th_R12:
#scene needs some details panned out with E11. The types of cakes and beverages etc. The picnic basket is a bit tricky, I don't really want that for this. Dunno what to do.

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_daily fadein 3.0

scene bg school_courtyard_rn
with locationchange

# hi "Are you sure you want to go?"
hi "แน่ใจเหรอว่าจะไป"

# "The weather that has been wonderful for all of June has finally taken a turn for the worse. The leaden clouds drooping over the town look worrisome and the air feels heavy and still, just like before rain."
"อากาศดีมาทั้งเดือนมิถุนายน แต่ก็ย่ำแย่ลงจนได้ เมฆสีเทาทึมปกคลุมทั่วเมืองดูน่าหวั่นใจว่าฝนจะตก"

# "The forecast says there's a 60\% chance of rain this afternoon. Maybe this will mark the beginning of the rainy season."
"พยากรณ์อากาศบอกว่าบ่ายนี้ฝนจะตกร้อยละ 60 ของพื้นที่ คงจะเข้าหน้าฝนแล้วละมั้ง"

show emi basic_grin_rn at center
with charaenter

# emi "Of course I'm sure! I've been waiting for this all week!"
emi "แน่ยิ่งกว่าแช่แป้ง! นี่ฉันคอยมาทั้งสัปดาห์เลยนะ!"

# "Emi had planned a picnic at some nearby park, with snacks aplenty bought from the convenience store, but with the weather this gloomy, it seems risky."
"เอมิวางแผนไว้ว่าจะไปปิกนิกกันที่สวนสาธารณะที่อยู่ใกล้ ๆ พร้อมขนมมากมายที่ซื้อมาจากร้านสะดวกซื้อ แต่ในเมื่อ\nฟ้าหม่นขนาดนี้ก็ดูสุ่มเสี่ยงเหลือเกิน"

show emi basic_annoyed_rn
with charachange

# emi "I asked some other people to come too, but they didn't want to go because of the weather. We have to prove them wrong!"
emi "ฉันไปชวนคนอื่นมาด้วยนะ แต่พอเห็นสภาพอากาศแล้วก็ไม่อยากมากัน เราต้องไปแสดงให้เห็นว่าพวกนั้นน่ะคิดผิด!"

# hi "Wrong how?"
hi "คิดผิดยังไง"

show emi excited_smile_rn
with charachange

# emi "You know, like how it always rains when you think it won't, and when you think it will, it doesn't? We'll go no matter what, so it's a win-win situation!"
emi "ก็เนี่ย เวลาคิดว่าจะไม่ตกก็จะตก แล้วเวลาคิดว่าจะตกก็จะไม่ตก ยังไงเราก็จะไปกันอยู่ดี ทางไหนเราก็ได้ทั้งนั้น!"

show emi basic_closedhappy_rn
with charachange

# emi "I've been going without sweets for weeks because of practice for the track meet. But now I can splurge on anything I want. Nothing is going to stop me now!"
emi "ฉันต้องงดของหวานเป็นสัปดาห์ ๆ เพื่อไปแข่งวิ่งเลยนะ แต่คราวนี้แหละฉันจะสวาปามอะไรก็ได้ ไม่มีอะไรจะหยุดฉัน\nได้แล้ว!"

# hi "I thought you were all about a healthy lifestyle and stuff."
hi "ไม่ใช่ว่าเธอเป็นพวกรักสุขภาพอะไรเทือกนั้นหรือไง"

show emi excited_proud_rn
with charachange

# emi "Ohoho, Hisao, you understand so little. There's not a single girl on this planet who doesn't love sweets!"
emi "โอะโฮะ ๆ ฮิซาโอะ ช่างไม่รู้อะไรบ้างเลย สาว ๆ ทั้งโลกน่ะชอบกินของหวานกันทั้งนั้น!"

show emi excited_proud_rn at twoleft
show bg school_courtyard_rn at bgleft
with charamove

show rin basic_deadpan_rn at tworight
with charaenter

# rin "I don't like sweets."
rin "ฉันไม่ชอบของหวาน"

show emi excited_joy_rn
show rin basic_awayabsent_rn
with charachange

# emi "She doesn't count. Anyway, is this clear?"
emi "รายนั้นไม่นับ แต่เป็นอันว่าตามนี้นะ"

show rin basic_absent_rn
with charachange

# hi "Completely. We will go and eat our fill of sweets."
hi "ครับท่าน เราจะออกไปกินของหวานกัน"

show emi basic_closedgrin_rn
show rin basic_awayabsent_rn
with charachange

# emi "Damn straight we will."
emi "กินให้ยับ"

show emi excited_laugh_rn
with charachange

# emi "I'm going to have to work it off later but it's so worth it."
emi "ถึงจะต้องไปเอาออกอีกที แต่ก็คุ้มแล้ว"

# "Emi seems to be extremely determined about this. She is positively exhilarated, brimming with energy as always, but something seems special today."
"เอมิเธอดูหมายมั่นปั้นมือจะไปให้ได้ เธอเปี่ยมล้นด้วยพลังและเริงร่าเหมือนทุกที แต่วันนี้ดูจะมีอะไรพิเศษขึ้นมา"

# "It looks like she can hardly stop herself from jumping up and down on the spot."
"เหมือนว่าอีกนิดเธอก็จะหลุดปล่อยตัวโดดโหยง ๆ แล้ว"

show emi excited_joy_rn
with charachange

# emi "Come on!"
emi "ไปกัน!"

hide emi
hide rin
with charaexit

# "I grasp the wooden handle of the umbrella I brought and start to follow the two girls, who seem to have no qualms about leaving me behind if I keep daydreaming."
"ฉันถือร่มที่คันจับทำจากไม้ที่ซื้อมาแล้วตามสองสาวที่ออกไปไม่เดือดร้อนอะไรที่จะปล่อยให้ฉันนั่งฝันกลางวัน\nอยู่คนเดียว"

# "My umbrella is really fancy, the old-fashioned kind with a curved handle and a metal spike at the end. It used to belong to my grandfather. It looks like an antique, but it's in really good shape; almost as good as new."
"ร่มฉันนั้นแสนจะหรูหรา เป็นร่มอย่างยุคเก่าที่มีมือจับแบบงอปลายเหล็กแหลม ร่มนี้เคยเป็นของคุณปู่ อาจจะดู\nเหมือนของสะสม แต่สภาพร่มนั้นยังดีเหมือนใหม่"

# "It's really big, too. I remember how my grandfather, my grandmother, and I all fit neatly under it when a rainstorm caught us on an afternoon walk years ago, when I was around nine or ten."
"แถมใหญ่มากด้วย ฉันจำได้ว่าเมื่อหลายปีก่อนที่ฉันอายุได้สักเก้าหรือสิบขวบ ร่มคันนี้เป็นร่มที่ทั้งปู่ย่าแล้วก็ฉัน\nใช้หลบพายุฝนที่ตกลงมาตอนเดินเล่นยามบ่ายได้อย่างพอดิบพอดี"

# "My grandparents are both gone now, but I still have the umbrella to keep me dry when it rains."
"ตอนนี้ทั้งปู่และย่าท่านก็ไม่อยู่แล้ว แต่ฉันยังมีร่มคันนี้ที่ใช้กันฝนอยู่"

scene bg school_road_rn
with locationskip

# "We walk along the road leading down from the school towards the convenience store, the clouds casting their dark shadow down on us. The weather seems to be taking a turn for the worse and I am pretty sure I just felt a raindrop on my head."
"พวกเราเดินไปตามถนนที่ออกจากโรงเรียนลงไปที่ร้านสะดวกซื้อ เมฆทอดเงาทะมึนอยู่เหนือพวกเรา สภาพอากาศดู\nจะย่ำแย่ลงไปอีก แถมเมื่อกี้เหมือนมีเม็ดฝนตกใส่หัวแล้วด้วย"

# hi "Didn't you guys think of taking umbrellas? It really looks like it'll rain."
hi "นี่พวกเธอไม่คิดจะเอาร่มมากันเลยเหรอ สภาพฝนจะตกอย่างนี้เนี่ย"

show rin basic_deadpancontemplation_rn at tworight
show emi basic_grin_rn at twoleft
with charaenter

# "Rin looks at her limply hanging sleeves and shrugs her shoulders."
"รินมองแขนเสื้อที่ห้อยต่องแต่งของเธอแล้วยักไหล่"

show emi basic_closedgrin_rn
show rin basic_awayabsent_rn
with charachange

# emi "I don't have one. Besides, a little rain won't kill us."
emi "ฉันไม่มีร่ม แล้วอีกอย่าง ฝนนิด ๆ หน่อย ๆ ไม่ตายหรอกน่า"

# "She pushes her chest out, looking very confident about that."
"เธอยืดอกดูมั่นใจกับคำพูดนั้น"

show emi basic_happy_rn
with charachange

# emi "We aren't made of sugar!"
emi "ตัวพวกเราไม่ได้ทำจากน้ำตาลสักหน่อย!"

show rin basic_absent_rn
with charachange

# hi "I thought that's exactly what girls were made of, especially considering what you're planning to gorge yourself on today."
hi "ไม่ใช่ว่าพวกผู้หญิงก็ทำจากน้ำตาลกันทั้งนั้นเหรอ แล้วเห็นของที่เธอจะกินวันนี้มันก็น้ำตาล"

show emi sad_annoyed_rn
with charachange

# "She just sticks out her tongue in reply."
"เธอแลบลิ้นใส่ตอบ"

hide emi
hide rin
with charaexit

# "The walk down from the school to the local shopping district is not a long one, but it's not very short, either. It's all downhill so our steps roll easily, but time stretches out nevertheless."
"ทางเดินจากโรงเรียนมาย่านการค้าในละแวกนี้นั้นไม่ไกลมากนัก แต่ก็ไม่ได้ใกล้สักเท่าไหร่ เพราะเป็นทางลงเนิน\nจึงเดินกันมาได้ไว แต่ก็ยังนานอยู่ดี"

# "The distance is right there, in that gray area where you don't expect the trip to be quickly over with, but you aren't preparing for a long walk, either."
"ก็เป็นระยะที่ประมาณหนึ่ง อยู่ในเขตกึ่ง ๆ ที่ต้องเตรียมใจว่าจะไม่ได้เดินแค่แป๊บเดียว แต่ก็ไม่ต้องเตรียมใจว่าจะเดิน\nยาว ๆ ขนาดนั้น"

# "Thus, the trip is slightly too long to stay comfortably quiet the whole time, though the girls don't seem to mind."
"เพราะงั้นแล้ว เป็นระยะทางที่ออกจะนานไปหน่อยถ้าจะให้เดินไปเงียบ ๆ ตลอดทาง ถึงสองสาวจะดูไม่ได้อะไรก็เถอะ"

# "Rin walks calmly ahead, seemingly lost in thought. I'm kind of wary about starting a conversation, since the last time didn't end very well for either of us."
"รินเดินนำดูคิดอะไรอยู่ ฉันลังเลว่าจะคุยอะไรดีหรือเปล่า เพราะครั้งล่าสุดที่คุยกันนั้นจบกันไม่สวยสักเท่าไหร่"

# "I haven't exchanged a single word with her since then."
"ตั้งแต่นั้นมาฉันก็ยังไม่ได้คุยอะไรกับเธอเลย"

# "Emi, on the other hand, is way too happy about just walking."
"ในขณะที่เอมินั้นดูจะพอใจกับแค่การเดินไปเฉย ๆ"

# "She seems to literally jump a little on every step, or skip over cracks, or balance on the edge of the sidewalk. Every now and then she comments on something to which Rin replies in an automatic-sounding, nonsensical way that makes Emi giggle a little."
"แต่ละก้าวของเธอนั้นแทบกลายเป็นการกระโดดไปแล้ว โดดข้ามรอยแยกบ้าง หรือมาทรงตัวอยู่ข้างทางเท้าบ้าง\nบางครั้งเอมิก็จะพูดถึงอะไรสักอย่างขึ้นมาแล้วรินก็ตอบด้วยเสียงเนิบ ๆ แบบอัตโนมัติที่ฟังดูหลุดโลกจนเอมิหลุดหัวเราะ"

$ renpy.music.set_volume(0.1, 0.0, channel="ambient")
play ambient sfx_rain fadein 5.0

scene bg suburb_roadcenter_rn
with locationchange

# "As we reach the bottom of the hill, the first raindrops begin to fall. I feel one hit the top of my head, then two more hit my nose in quick succession."
"พอมาถึงที่ตีนเขาฝนเม็ดแรกก็ตกลงมา มีเม็ดหนึ่งที่ตกใส่หัวฉัน อีกสองเม็ดตามมาติด ๆ ตกใส่จมูกฉัน"

play sound sfx_thunder
stop music

$ renpy.music.set_volume(0.2, 0.5, channel="ambient")
$ renpy.music.set_volume(1.0, 4.0, channel="music")
show rain light
with dissolve

# "It's not one or two rainclouds any more. The entire sky has turned shadowy gray, billowing rainclouds swirling right on top of us."
"ตอนนี้ไม่ใช่แค่เมฆฝนก้อนสองก้อนแล้ว แต่ทั้งฟ้ามืดทะมึนมีเมฆฝนก่อตัวหมุนทวนอยู่เหนือพวกเรา"

show emi sad_pout_rn behind rain at center
with charaenter

# emi "Oh, shoot. I guess we aren't going to have a picnic then."
emi "ตายละ คงไม่ต้องไปปิกนิกกันแล้วสิ"

# hi "What now?"
hi "แล้วไงต่อ"

show emi sad_pout_rn at twoleft
show bg suburb_roadcenter_rn at bgleft
with charamove

show rin negative_spaciness_rn behind rain at tworight
with charaenter

# rin "Maybe we could have a rain picnic. A picnic in rain."
rin "จะปิกนิกฝนก็ได้นะ ฝนตกแล้วปิกนิก"

show emi basic_annoyed_rn
with charachange

# emi "No, we'd all just catch a cold and I don't like getting me or my snacks wet."
emi "ไม่ได้สิ เดี๋ยวก็เป็นหวัดกันหมดหรอก แล้วฉันก็ไม่อยากให้ตัวฉันหรือขนมฉันต้องเปียกด้วย"

show rin relaxed_nonchalant_rn
with charachange

# rin "I kind of like it. Not the snacks part though."
rin "ฉันว่าฉันอยาก แต่ไม่นับขนมนะ"

$ renpy.music.set_volume(0.5, 4.0, channel="ambient")

show emi basic_concentrate_rn
show rain medium
with charachange
play sound sfx_rustling

# "Emi considers our problematic situation for a moment while I open my umbrella and lift it up, trying to hold it so that all three of us get covered."
"เอมิครุ่นคิดอยู่กับสถานการณ์ที่ลำบากนี้อยู่ครู่หนึ่ง ระหว่างนั้นฉันเอาร่มออกมากางแล้วถือไว้ให้กันฝนได้ทั้งสามคน"

show emi basic_happy_rn
with charachange

# emi "Hey Hisao, have you been to the Shanghai yet?"
emi "นี่ ฮิซาโอะ นายเคยไปร้านเซี่ยงไฮ้หรือยัง"

show rin basic_absent_rn
with charachange


label th_R12a:

# hi "It's a café somewhere around here, right? I've heard of it."
hi "คาเฟที่อยู่แถวนี้ใช่มั้ย เคยได้ยินอยู่"

label th_R12b:

# hi "Yeah, our class president took me there on my first week."
hi "อื้ม ตอนสัปดาห์แรกหัวหน้าห้องพาฉันไปน่ะ"


label th_R12c:

show rin basic_awayabsent_rn
show emi basic_grin_rn
with charachange

# emi "It's a nice place. Let's go there and wait out the rain. If it's just a really quick shower, we can still go for the picnic, and if it gets worse, we'll just order cake there instead."
emi "ร้านดีนะ ไปหลบฝนที่นั่นกันเถอะ ถ้าตกแป๊บเดียวเดี๋ยวออกไปปิกนิกกันอีกทีก็ได้ หรือถ้าตกหนักจริง ๆ ก็สั่งเค้ก\nที่ร้านกินกันเอา"

show rin basic_absent_rn
with charachange

hide emi
with charaexit

hide rin
with charaexit

# "Neither Rin nor I have better ideas, so with Emi taking the lead, we start walking briskly along a side street."
"ทั้งรินและฉันต่างก็ไม่รู้จะทำยังไงต่อดี พวกเราจึงรีบเดินมาตามซอกซอยตามที่เอมินำทาง"

$ renpy.music.set_volume(1.0, 6.0, channel="ambient")

scene bg suburb_shanghaiext_rn
show rain normal
with locationchange

# "The café is only a few blocks away, but even with the umbrella, we can't avoid getting slightly damp. The rain keeps coming down harder and harder."
"คาเฟอยู่ไม่ไกลมาก แต่ถึงจะมีร่มแล้วก็ยังเปียกฝนอยู่หน่อย ๆ และฝนยิ่งตกหนักขึ้นเรื่อย ๆ"

# "Raindrops leave tiny dots on the black asphalt road, which then combine into bigger patches like pointillist artwork being made in front of our eyes in mere seconds."
"เม็ดฝนตกใส่เป็นจุดเล็ก ๆ อยู่บนพื้นถนนยางมะตอยสีดำ ไม่กี่อึดใจรอยเหล่านั้นก็เติมเต็มไปทั่วจนดูเหมือน\nภาพผสานจุดสีขนาดใหญ่"

# "It's pouring heavily, drumming on the hoods of the cars parked on the sides of the street and already flowing in little creeks along the sidewalks."
"ฝนตกหนักสาดใส่หลังคารถที่จอดอยู่ข้างถนนส่งเสียงดัง น้ำเริ่มนองจนไหลเป็นสายตามทางเท้า"

# "The yellow light shining through the rainwater streaming down the windows looks very warm and inviting."
"แสงสีเหลืองที่ส่องผ่านหน้าต่างที่มีน้ำฝนไหลนั้นช่างดูอบอุ่นและเชื้อเชิญ"

play sound sfx_storebell
stop ambient fadeout 0.5
play music music_jazz fadein 2.0

scene bg suburb_shanghaiint at left
with locationchange

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 2.0

# "I shake the excess water off the umbrella and head inside with them, following Emi to a vacant table in the furthest corner of the small café."
"ฉันสะบัดน้ำออกจากร่มแล้วเดินเข้าร้านไปพร้อมสองคนนั้น จากนั้นตามเอมิไปยังโต๊ะว่างที่อยู่มุมในสุดของคาเฟ"

$ renpy.music.set_volume(0.7, 2.0, channel="ambient")

# "The place is almost full; apparently other people had the same idea as Emi, and now we are all stranded together here in this cozy little place."
"ร้านมีคนอยู่แน่นขนัด ดูเหมือนว่าคนอื่นจะคิดเหมือนกันกับเอมิจนได้มาหลบฝนอยู่ด้วยกันในร้านเล็ก ๆ\nอันแสนสบายนี้"

scene bg suburb_shanghaiint at Fullpan(5.0)
with None

# "Varnished wooden pillars and paper screens mix with Parisian-style tables and chairs in discordant harmony, a contrast of old and new."
"เสาไม้เคลือบวานิชและฉากกั้นกระดาษอยู่ร่วมกับโต๊ะและเก้าอี้อันเรียบหรูได้อย่างแตกต่างลงตัว ผสานความเก่า\nและใหม่เข้าด้วยกัน"

# "Light jazz plays quietly in the background, though it's mostly drowned out by the murmur of the customers."
"ในร้านมีดนตรีแจ๊สคลอเบา ๆ ทว่าก็โดนเสียงจอแจของลูกค้ากลบไปเกือบหมด"


label th_R12d:
#not seen the shizune & misha shanghai scene in act 1
# "There's only one waitress serving the full house, frantically gliding from one table to another and trying to keep up with everything. To my surprise, I think I recognize her."
"ทั้งร้านมีพนักงานเสิร์ฟอยู่คนเดียวโดดจากโต๊ะนั้นไปโต๊ะนี้อย่างรีบร้อนคอยจัดการกับทุกอย่าง แปลก รู้สึกคุ้น ๆ"

# "I watch her deliver a tray of tea cups and pastries to another table taken by Yamaku students, then take an order from a middle-aged couple sitting across from us before finally turning to serve us."
"ฉันดูเธอนำถ้วยชาและขนมไปเสิร์ฟให้โต๊ะอื่นที่มีนักเรียนจากยามากุนั่งอยู่ จากนั้นเธอก็ไปรับรายการจากคู่รัก\nวัยกลางคนที่นั่งอยู่โต๊ะตรงข้ามกัน จนในที่สุดก็ถึงคิวที่เธอต้องแวะมาที่โต๊ะพวกเรา"

# hi "Yuuko?"
hi "คุณยูโกะ?"

show yuukoshang neurotic_up at Slide(0.6,0.5,0.5,0.5,0.5)
show bg suburb_shanghaiint at right
with charaenter

# "Now that she's close and facing me I see that it really is her, the part-time librarian of Yamaku in full waitress attire. It's a pretty cute outfit, and she has tied her hair up in buns to match."
"พอเธอได้มาอยู่ใกล้ ๆ ตรงหน้าแล้วก็ถึงแน่ใจว่าคนตรงหน้าที่ใส่ชุดบริกรนี้เป็นเธอคนนั้นที่ทำงานพาร์ทไทม์เป็น\nบรรณารักษ์อยู่ที่ยามากุจริง ๆ ชุดน่ารักดี แถมเกล้ามวยผมให้เข้ากับชุดด้วย"

show yuukoshang worried_up at center
with charachange

# "It's a completely different image from her mousy, plain style at her other job. Yuuko blinks a few times looking confused, then remembers that she was about to say something."
"ดูไม่เหมือนกับตัวเธอตอนทำงานอยู่ห้องสมุดที่ดูเรียบ ๆ ขี้อาย ยูโกะกะพริบตาสองสามครั้งด้วยความงงงวยก่อนจะ\nนึกได้ว่าเมื่อกี้เธอจะพูดอะไร"

show yuukoshang panic_down
with charachange

# yu "Umm… ah, welcome to the Shanghai."
yu "เอ่อ… อ่า ยินดีต้อนรับสู่ร้านเซี่ยงไฮ้ค่ะ"

# hi "So you work here too? I thought you were a university student or something."
hi "ทำงานที่นี่ด้วยเหรอครับ ไม่ใช่ว่าคุณเรียนมหาลัยอยู่เหรอ"

show yuukoshang neurotic_down
with charachange

# yu "Ehh, yes, that too. It's a part-time job as you can see, ehehe. It's Sunday, so there aren't any lectures."
yu "เอ่ออ อื้ม ก็ใช่ แต่พอดีตรงนี้เป็นงานพาร์ทไทม์ วันนี้วันอาทิตย์ก็เลยไม่มีเรียนน่ะ"

show yuukoshang neutral_down
with charachange

# yu "Good thing, too, since today has been so busy I'm wishing for another pair of hands. Anyway, I'm in a bit of a rush as you can see. What can I get you today?"
yu "ซึ่งก็ดีด้วยเพราะวันนี้ยุ่งมากจนงานล้นมือไปหมดเลย แต่ก็อย่างที่เห็นแหละเนอะ ตอนนี้รีบอยู่ รับอะไรดีคะ"

label th_R12e:
#seen it
# "I notice Yuuko is at work here today, but it seems like she's serving a full house all by herself, frantically gliding from one table to another and trying to keep up with everything."
"ฉันเห็นว่าวันนี้ยูโกะก็อยู่ทำงานด้วย แต่ดูเหมือนว่าทั้งร้านจะมีแค่เธอคนเดียวโดดจากโต๊ะนั้นไปโต๊ะนี้อย่างรีบร้อน\nคอยจัดการกับทุกอย่าง"

# "I watch her deliver a tray of tea cups and pastries to another table taken by Yamaku students, then take an order from a middle-aged couple sitting across from us before finally turning to serve us."
"ฉันดูเธอนำถ้วยชาและขนมไปเสิร์ฟให้โต๊ะอื่นที่มีนักเรียนจากยามากุนั่งอยู่ จากนั้นเธอก็ไปรับรายการจากคู่รัก\nวัยกลางคนที่นั่งอยู่โต๊ะตรงข้ามกัน จนในที่สุดก็ถึงคิวที่เธอต้องแวะมาที่โต๊ะพวกเรา"

# hi "Hi, Yuuko."
hi "สวัสดีครับคุณยูโกะ"

show yuukoshang neurotic_up at Slide(0.6,0.5,0.5,0.5,0.5)
with charaenter

# yu "Umm… ah, welcome to the Shanghai. "
yu "เอ่อ… อ่า ยินดีต้อนรับสู่ร้านเซี่ยงไฮ้ค่ะ"

# hi "Looks like you're busy."
hi "ยุ่งน่าดูเลยนะครับ"

show yuukoshang neurotic_down at center
with charachange

# yu "Ahaha, I'm completely over my head here. I wish I had another pair of hands."
yu "อะฮ่าฮ่า ตอนนี้นี่งานล้นมือไม่ไหวเลย"

show yuukoshang neutral_down
with charachange

# yu "What can I get for you today?"
yu "รับอะไรดีคะ"

label th_R12f:

show emi excited_joy at Slide(-0.1,0.0,0.0,0.0,0.5)
show rin basic_awayabsent at Slide(1.05,1.0,0.95,1.0,0.5)
with charaenter

stop music fadeout 1.0
$ renpy.music.set_volume(0.4, 2.0, channel="ambient")

# "Emi doesn't hesitate even for a second. Her eyes glitter like those of a kid in a candy store."
"เอมิไม่ลังเลแม้วินาทีหนึ่ง ตาเธอเป็นประกายประหนึ่งเด็กที่เดินเข้าร้านขนม"

play music music_comedy fadein 1.0
show emi excited_amused at left
with charachange

# emi "Tea for everyone! And cake for me!"
emi "ชาของทุกคนสามที่ค่ะ! แล้วก็เค้กของหนูหนึ่งที่!"

show yuukoshang smile_up
with charachange

# "Yuuko tries to stay as formal and professional-looking as possible, smiling cheerily at my ravenous companion."
"ยูโกะรักษากิริยาให้ดูเป็นทางการและมืออาชีพที่สุดเท่าที่จะเป็นไปได้พลางยิ้มสดใสให้เพื่อนร่วมโต๊ะผู้หิวโหยของฉัน"

show yuukoshang smile_down
with charachange

# yu "Ahh… yes, today we have a choice of strawberry shortcake, raspberry layer cake, or lemon meringue pie."
yu "อ่า… ค่ะ วันนี้เรามีเค้กสามอย่างให้เลือก สตรอว์เบอร์รีชอร์ตเค้ก เลเยอร์เค้กราสป์เบอร์รี แล้วก็พายเมอแร็งก์เลมอนค่ะ"

show emi basic_happy
with charachange

# emi "Strawberry… no, lemon! No, actually I'll take both!"
emi "ขอสตรอว์เบอร์รี… ไม่สิ เลมอน! ไม่ ๆ ขอทั้งสองอย่างเลยค่ะ"

# "She looks at me in challenge."
"เธอมองท้าฉัน"

# hi "Err… I'll take just the pie."
hi "เอ้อ… ผมขอแค่พายแล้วกัน"

show rin basic_deadpan at Position(xalign=1.0, xpos=0.95)
with charachange

# rin "Nothing."
rin "ไม่เอา"

show emi basic_annoyed
with charachange

# "Emi makes a face at Rin as though she had bitten into a lemon. She's clearly unhappy with her for not joining in."
"เอมิย่นหน้ายู่ใส่รินแสดงให้เห็นว่าเธอไม่พอใจเอามาก ๆ ที่รินไม่สั่งด้วย"

# emi "Oh come on, Rin. That's not polite at all."
emi "ไม่เอาน่าริน หยาบคายนะเธอเนี่ย"

show rin relaxed_boredom
with charachange

# rin "Nothing, thank you."
rin "ไม่เอา ขอบคุณค่ะ"

show emi basic_confused
with charachange

# emi "No, no, you silly! I meant that you should order something too."
emi "ไม่ใช่ ๆ ยัยบ๊อง! ที่ฉันหมายถึงคือให้เธอสั่งอะไรด้วย"

show rin negative_spaciness
with charachange

# rin "I'll take a straw then. My feet are all wet."
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

# "Yuuko is obviously uncertain of what to think about this. She fiddles with her pen and stationery for a moment, looking like she's about to cry, before deciding that we've finished ordering."
"ยูโกะทำหน้าเหลอหลา เธอจับปากกากับกระดาษเล่นอยู่ครู่หนึ่งทำหน้าเบ้เหมือนจะร้องไห้ ก่อนจะถือเอากับตัวเอง\nว่าพวกเราสั่งกันเสร็จแล้ว"

show yuukoshang neurotic_up
with charachange

# yu "Thank you very much!"
yu "ขอบพระคุณค่ะ!"

show yuukoshang neurotic_down at Transform(ypos=1.25)
with Dissolvemove(0.2)

with Pause(0.3)

show yuukoshang neurotic_down at center
with charamove

hide yuukoshang
with charaexit

show emi basic_grin at twoleft
show rin basic_awayabsent at tworight
with dissolvecharamove

$ renpy.music.set_volume(0.7, 2.0, channel="ambient")

# "She bows down a little bit too deeply and scampers to safety behind the counter."
"เธอโค้งให้ต่ำ ๆ แล้วตะลีตะลานไปหลบอยู่ที่หลังเคาน์เตอร์"

# "After that ordeal is over with, I have a chance to relax a bit and take a better look at the surroundings."
"เมื่อเสร็จสิ้นภารกิจแล้วฉันจึงถือโอกาสนี้ผ่อนคลายลงเล็กน้อยพลางมองไปรอบ ๆ"

# "Almost every table is occupied by people happy to be out of the rain, thankfully sipping their tea while waiting to dry off."
"แทบทุกโต๊ะเต็มไปด้วยคนที่มาหลบฝนกันอย่างมีความสุขและจิบชาอย่างเพลินใจระหว่างรอฝนหยุด"

# "Fragments of grumbling about the lousy weather or discussions over recent homework carry from nearby tables to my ears. Each one overlaps the other, but all are covered by the sound of falling rain."
"เสียงบ่นสภาพฟ้าฝนที่ไม่เป็นใจกับเสียงคนที่คุยกันเรื่องการบ้านที่เพิ่งได้มาไม่นานนี้แว่วมาจากโต๊ะใกล้ ๆ หลากเสียง\nต่างซ้อนทับกันทว่าถูกกลืนไปกับเสียงฝนสาด"

show emi basic_grin at left
show rin basic_awayabsent at Position(xpos=0.95, xalign=1.0)
with charamove

show yuukoshang smile_up at center
with charaenter

$ renpy.music.set_volume(0.4, 2.0, channel="ambient")

# "After a while Yuuko returns to our table, carrying a tray with a huge teapot, three cups, a slice of cake and two slices of pie."
"ผ่านไปสักพักยูโกะก็ถือถาดมาที่โต๊ะพวกเรา สิ่งที่วางอยู่ในนั้นมีกาน้ำชาใบใหญ่ ถ้วยสามใบ เค้กหนึ่งชิ้น\nและพายสองชิ้น"

show yuukoshang neurotic_up at centertremble
with charachange

with Pause(0.5)

show yuukoshang smile_down at Transform(ypos=1.25)
with Dissolvemove(0.2)
play sound sfx_pillow

with Pause(0.3)

show yuukoshang smile_down at center
with charamove

hide yuukoshang
with charaexit

show emi basic_grin at twoleft
show rin basic_awayabsent at tworight
with dissolvecharamove

$ renpy.music.set_volume(0.7, 2.0, channel="ambient")

# "She slaps the tray onto our tiny table with a clatter, almost sending the teapot toppling over into Rin's lap. We barely recover before she bows again and leaves, hurrying off to serve the other customers."
"เธอวางแรงจนถาดกระทบเข้ากับโต๊ะเสียงดังและเกือบทำกาน้ำชาหกใส่ริน พวกเรารีบจับไว้ได้อย่างทันท่วงที เธอ\nก้มหัวให้อีกครั้งแล้วรีบไปเสิร์ฟให้ลูกค้าคนอื่นต่อ"

# "Emi has been eyeing her strawberry cake very hungrily all this time, but somehow she managed to contain herself until Yuuko was out of sight."
"สายตาเอมิคอยจับจ้องเค้กสตรอว์เบอร์รีด้วยความหิวขั้นรุนแรง แต่ยังห้ามใจตัวเองไว้รอให้ยูโกะพ้นจากสายตา\nไปก่อนได้"

show emi excited_smile
with charachange

# "She digs in with gusto, while I content myself with pouring tea for everyone and placing the straw in Rin's cup."
"ระหว่างที่เธอจ้วงกินฉันก็คอยเทน้ำชาใส่ถ้วยแต่ละคนแล้วใส่หลอดให้ถ้วยริน"

show rin basic_deadpansurprised
with charachange

# "Rin looks at the way the tea swirls round and round in her white china cup, her eyes half closed, almost like she is being hypnotized."
"รินหรี่ตาอยู่ครึ่งหนึ่งมองน้ำชาที่หมุนติ้วอยู่ในถ้วยน้ำชาสีขาวของเธอคล้ายโดนสะกดจิต"

show shangpai:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

# "I pick up my fork and eye the food in front of me. The pie I got looks perfectly done, a thick layer of meringue atop creamy lemon custard."
"ฉันหยิบส้อมขึ้นมาแล้วเล็งของกินที่อยู่ตรงหน้า ตัวพายนั้นดูสวยงามและมีเมอแร็งก์หนาซ้อนอยู่บนคัสตาร์ด\nรสเลมอนชุ่มฉ่ำ"

# "After having the first bite, I pause, savoring the combination of tangy citrus and smooth, sugary meringue. It's quite good, though a bit too sweet for me."
"พอกัดกินคำแรกฉันก็ค่อย ๆ ลิ้มรสเปรี้ยวที่ผสมอยู่กับเมอแร็งก์รสหวานละมุน ก็อร่อยดี ถึงฉันจะว่าหวานไปหน่อย\nก็เถอะ"

show emi excited_joy
show rin basic_deadpannormal
with None

show shangpai:
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide shangpai

# emi "Iff ver’ good."
emi "อะอ่อยอัง"

# "She's talking through a mouthful of cake, already halfway through her slice even though it's not exactly small."
"เธอพูดทั้ง ๆ ที่ยังเคี้ยวแก้มตุ้ย ๆ แม้เค้กจะชิ้นค่อนข้างใหญ่ แต่เธอก็กินหมดไปแล้วครึ่งหนึ่ง"

show emi basic_grin
with charachange

# emi "I want to taste some of that."
emi "อยากชิมอันนั้นบ้างอะ"

play sound sfx_slide2

show emi excited_happy_close
show rin basic_absent
with characlose

show emi basic_closedgrin
show rin basic_awayabsent
with charachange

# "Before I get to respond, she strikes out at my delicious pie, takes a piece with her fork, and escapes with it."
"ก่อนฉันจะทันได้ตอบอะไรเธอก็ใช้ส้อมเข้ามาจู่โจมพายแสนอร่อยของฉันพาหนีไปแล้ว"

show emi basic_closedhappy
with charachange

# emi "This is pretty good too."
emi "อันนี้ก็อร่อย"

# hi "What are you doing? You have a slice of your own!"
hi "ทำอะไรเนี่ย ของเธอก็มีให้กิน!"

show emi excited_proud
with charachange

# emi "Yeah, but if I started on that before finishing the cake, it'd be rude, don't you think?"
emi "ใช่ แต่ถ้าให้กินอีกอันก่อนกินเค้กอันนี้หมดก็เสียมารยาทแย่ ว่ามั้ยล่ะ"

# "Her insolence is outrageous, but the gentleman in me allows for no retaliation."
"ชักจะมากไปแล้ว แต่ความเป็นสุภาพบุรุษในตัวก็ยั้งฉันไว้ไม่ให้โต้ตอบอะไร"

show emi basic_grin
with charachange

# "I glare angrily at her, and she replies by sticking out her tongue impishly. Emi is even more hyper than usual today, but I don't mind. It's good for her to let off some steam."
"ฉันทำหน้าถมึงทึงใส่เธอ ส่วนเธอก็แลบลิ้นเยาะเย้ยใส่ วันนี้เอมิดูจะตื่นตัวกว่าปกติ แต่ฉันไม่ถือหรอก ปล่อยให้เธอ\nได้ผ่อนคลายบ้างก็ดี"

# "I take another sip of the tea in my cup. It's good and hot, even though I don't usually care much for tea, and the atmosphere in the café is very relaxing."
"ฉันยกถ้วยชาขึ้นดื่มอีกจิบหนึ่ง ชานั้นทั้งหอมและอุ่นแม้ปกติฉันจะไม่ได้อะไรกับชามากนัก แถมบรรยากาศในคาเฟ\nก็ชวนให้ผ่อนคลายดีด้วย"

# "I don't mind spending the rest of the afternoon here, not even after Emi orders her second piece of strawberry cake and Rin spends most of the time staring fixedly at the rain streaming down from the heavens."
"จะให้แช่อยู่ที่นี่ทั้งบ่ายเลยก็ได้ แล้วแถมเอมิก็สั่งเค้กสตรอว์เบอร์รีเพิ่มด้วยอีกต่างหาก ส่วนรินก็เอาแต่จ้องมองฝน\nที่ไหลบ่าลงมาจากฟากฟ้า"

show rain normal behind bg
with None

# "Even Yuuko rolls her eyes at the third piece of cake disappearing into Emi's bottomless stomach just as quickly as the previous two."
"แม้แต่ยูโกะยังต้องกลอกตาใส่พอว่าเห็นเค้กชิ้นที่สามนั้นถูกดูดกลืนหายเข้าไปในกระเพาะหลุมดำของเอมิ\nอย่างรวดเร็วไม่ต่างอะไจากสองชิ้นแรก"

$ renpy.music.set_volume(1.0, 2.0, channel="ambient")
play ambient sfx_rain fadein 1.0

show bg suburb_shanghaiext_rn as bg2 behind rain
hide bg
hide rin
hide emi
with shorttimeskip


show bg suburb_shanghaiext_rn behind rain
hide bg2
with None

# "Despite the passing of time, it's still raining outside when we exit the Shanghai, though it seems to be letting up a little."
"เมื่อเวลาผ่านไปสักระยะหนึ่งแล้วพวกเราก็ออกมาจากร้านโดยที่ฝนยังคงตกอยู่ แต่ก็ดูจะซาลงบ้างแล้ว"

# hi "Too bad it had to rain on your parade."
hi "แย่จังเลยนะ ฝนตกจนแผนล่มหมด"

show rin basic_awayabsent_rn behind rain at center
with charaenter

# rin "Weren't we supposed to have a picnic?"
rin "พวกเราจะมาปิกนิกกันไม่ใช่เหรอ"

show rin basic_awayabsent_rn at tworight
show bg suburb_shanghaiext_rn at bgright
with charamove

show emi basic_closedgrin_rn behind rain at twoleft
with charaenter

# "Emi doesn't look too distraught over this turn of events."
"เอมิไม่ได้ดูอารมณ์บูดอะไรมากนักที่เรื่องเป็นอย่างนี้"

# emi "Nah it's fine! We had a good time, didn't we? I feel really pumped up."
emi "ไม่เป็นไรน่า ก็ได้สนุกกันแล้วนี่ ฉันละมีแรงฮึดขึ้นมาเลย"

show emi basic_grin_rn
with charachange

# emi "It isn't even raining that hard any more. I kinda want to hike back to school to get rid of this energy and work off some of that cake."
emi "แถมฝนก็ไม่ได้ตกหนักขนาดนั้นแล้ว ชักอยากเอาแรงฮึดที่ได้มาไปใช้ขึ้นเขาไปโรงเรียนแล้วสิ แล้วเดี๋ยวจะไป\nออกกำลังกายเอาเค้กออกด้วย"

# "She stretches her arms out, and arches her back like a cat. After rolling her shoulders around twice, she smiles brightly."
"เธอยืดแขนยืดหลังอย่างแมว เธอหมุนไหล่อยู่สองรอบแล้วยิ้มแฉ่ง"

show emi sad_grin_rn
with charachange

# emi "Man, I can't really run with these legs, though, especially uphill. I wish I'd brought my other ones."
emi "เฮ้อ แต่ขาคู่นี้คงใช้วิ่งไม่ไหว ยิ่งเป็นเนินอีก รู้งี้เอาขาอีกคู่มาด้วยดีกว่า"

# "This notion sounds odd, spoken so casually. But I guess for Emi, changing legs is sort of like someone else changing shoes."
"พอพูดขึ้นมาลอย ๆ แล้วคำก็ฟังดูแหม่ง ๆ แต่กับเอมิแล้ว การเปลี่ยนขาก็คงเหมือนการที่คนปกติเปลี่ยนรองเท้าละมั้ง"

show emi excited_proud_rn
with charachange

# emi "Maybe if I walk really fast, that'll be kinda like running. I think I'll do that."
emi "ถ้าเดินให้เร็ว ๆ ก็น่าจะเหมือนการวิ่งอยู่นะ เอางั้นก็แล้วกัน"

show rin basic_absent_rn
with charachange

# hi "I won't be able to keep up with that going uphill, though; I really am in bad shape. Plus, you'll get wet without an umbrella."
hi "แต่เนินขนาดนั้นฉันคงตามไม่ไหวหรอกนะ สังขารฉันไม่ไหวแล้ว อีกอย่าง ไม่มีร่มเดี๋ยวเธอก็เปียกหรอก"

show emi basic_grin_rn
show rin basic_awayabsent_rn
with charachange

# emi "It's hardly even a drizzle, now. A few drops won't hurt. I think I'm gonna go to the track after I change my legs, too."
emi "ก็แค่พรำ ๆ แทบไม่ตกแล้วเนี่ย โดนสักสองสามเม็ดไม่ตายหรอก เดี๋ยวถึงโรงเรียนเปลี่ยนขาแล้วฉันว่าจะไปที่ลู่ด้วย"

# "Emi skips away from the protection of my umbrella and goes on ahead at a brisk pace. Suddenly, she seems to remember something as she stops and spins around."
"เอมิก้าวฉับ ๆ ออกจากร่มฉันนำไปก่อน จู่ ๆ เธอก็นึกอะไรขึ้นได้แล้วชะงักกึกหมุนตัวหันมา"

show emi excited_smile_rn
with charachange

# emi "See you tomorrow!"
emi "เจอกันพรุ่งนี้!"

show emi excited_proud_rn
with charachange

# emi "Come eat lunch with us on the roof! I'll bring enough for three."
emi "มากินข้าวเที่ยงด้วยกันที่ดาดฟ้านะ! เดี๋ยวฉันจะพกข้าวไปให้พอกินกันทั้งสามคนเลย"

show emi invis at offscreenleft
show rin basic_absent_rn at center
show bg suburb_shanghaiext_rn at center
with dissolvecharamove

hide emi
with None

stop music fadeout 5.0

# "Rin and I are left to watch her wave at us and skip off again. Soon she disappears around a street corner. I'll never understand why Emi is perpetually in such a hurry to get somewhere."
"รินและฉันยืนมองเอมิที่โบกมือลาทิ้งพวกเราไว้ ไม่นานเธอก็หายวับไปตรงหัวมุมถนน ฉันคงไม่มีวันเข้าใจว่าทำไมเอมิ\nถึงดูรีบร้อนขนาดนั้นทุกทีเวลาไปไหนมาไหน"

# hi "So, would you like me to walk you back to school so that at least one of you won't get wet?"
hi "แล้ว ให้ฉันเดินไปส่งเธอที่โรงเรียนมั้ย อย่างน้อยก็จะได้มีสักคนที่ไม่ตัวเปียก"

show rin basic_deadpan_rn
with charachange

# rin "If you are happy with it."
rin "ถ้านายพอใจ"

# "It seems neither of us wants to keep alive the strained atmosphere from the argument a few days ago in the art room, which makes me feel relieved. I don't want to bear grudges and I'm happy that Rin feels the same way."
"ดูเหมือนว่าพวกเราต่างก็ไม่อยากจะปล่อยให้บรรยากาศตึงเครียดที่ได้จากทะเลาะกันในห้องศิลปะเมื่อสองสามวันก่อน\nต้องค้างคาอยู่อย่างนั้น ซึ่งฉันก็โล่งใจ ฉันไม่อยากนึกเคืองอะไรเลย แล้วฉันก็ดีใจที่รินก็คิดอย่างนั้นเหมือนกัน"

# "Thus it is decided that we are content with each other's company for now, and we start walking in the same direction as Emi, albeit at a considerably calmer pace."
"จึงเป็นอันตกลงว่าพวกเราก็เดินตามทางที่เอมินำไปด้วยกันได้ แม้จะไม่ได้เร่งรีบเท่าก็ตาม"

hide rin
hide bg
show ev rin_rain_away_close behind rain:
    xalign 0.5 yalign 1.0 subpixel True
    acdc_warp 20.0 yalign 0.0
with whiteout
$ renpy.music.set_volume(0.7, 4.0, channel="ambient")

# "I get a bit closer to Rin, even though the umbrella is already big enough to shelter us both. I can feel her nearby warmth providing a contrast to the chill of this rainy weather."
"ฉันขยับเข้าไปใกล้ ๆ รินอีกหน่อยแม้ร่มจะใหญ่พอที่จะกันฝนให้เราสองคนอยู่แล้ว พออยู่ใกล้ก็สัมผัสได้ถึง\nความอบอุ่นจากตัวเธอที่ขัดกับอากาศเย็น ๆ จากฝน"

# "Raindrops hitting the umbrella make a distinctive sound, playing the staccato melody of rainfall for nobody in particular."
"เสียงฝนตกใส่ร่มดังเปาะแปะเล่นเป็นท่วงทำนองบทเพลงสตักกาโตสายฝนแด่ไม่ใครบางคน"

#"They leave tiny dots on the black asphalt road, which then combine into bigger patches like pointillist artwork being made in front of our eyes in mere seconds."

# "I realize I haven't been outside in the rain in what feels like forever. I inhale, taking in the scent of rain, feeling the weather with all my senses."
"ฉันเพิ่งรู้ตัวว่าฉันไม่ได้ออกมาอยู่กลางฝนอย่างนี้นานมาก ๆ แล้ว ฉันสูดหายใจเอากลิ่นฝนพลางสัมผัสสภาพอากาศนี้\nโดยใช้ทุกประสาทสัมผัส"

# "The world melts into a blur inside the rain."
"ฝนปรอยจนโลกพร่าเลือน"

# "The colors of the sky have deepened from gray to dark blue, with hues of red added to the mix from the sunlight reflecting off the clouds. The low-hanging sky looks pretty, as if I could reach out my hand and touch it."
"ท้องฟ้าเปลี่ยนสีจากเทาเป็นน้ำเงินแซมสีแดงที่เป็นสีแสงแดดที่สะท้อนจากเมฆ ท้องฟ้าที่ลอยต่ำเช่นนี้นั้นดูสวยงาม\nดูคล้ายกับว่าฉันเอื้อมมือไปจับได้ถึง"

$ renpy.music.set_volume(0.5, 4.0, channel="ambient")

# rin "Have I told you how much I like rain? It's like painting. It makes me feel connected."
rin "ฉันเคยบอกนายหรือยังว่าฉันชอบฝนมาก เหมือนภาพวาด ทำให้ฉันรู้สึกได้เชื่อมต่อ"

# "Almost echoing my thoughts, Rin lets out one of her own. It slips out of her mouth, circling around us gently."
"รินพูดสิ่งที่เธอคิดซึ่งแทบจะตรงกับสิ่งที่ฉันคิด คำพูดนั้นออกมาจากปากเธอล้อมตัวพวกเราไว้อย่างอ่อนโยน"

# rin "Everything looks so soft, like the outlines of things just disappear. I like that."
rin "ทุกอย่างดูนุ่ม เหมือนเส้นขอบของอะไร ๆ หายไปหมดเลย ฉันชอบ"

# rin "It's like the rain is hugging me."
rin "เหมือนว่าฝนกอดฉันอยู่"

# "Her voice sounds different from usual; more gentle, now, and soft. I wonder if it's only because of the rain, or because of the mood the rain brought upon the quiet artist girl."
"เสียงเธอต่างไปจากปกติ ฟังดูอ่อนโยนและนุ่มนวล เป็นเพราะฝน หรือเป็นเพราะอารมณ์ที่ฝนพาให้ศิลปินสาว\nที่พูดน้อยคนนี้ได้รู้สึกกันนะ"

show ev rin_rain_away_close behind rain at Position(xalign=0.5, yalign=0.0)
show ovl rin_rain_hisaotowards_close behind rain at Position(xalign=1.0, yalign=0.0)
with charachange

# "I feel that mood in myself too, enhanced by her words."
"ฉันเองก็รู้สึกอย่างนั้นเช่นกัน ยิ่งเสริมด้วยคำพูดเธอด้วยแล้ว"

# hi "Yeah. I like rainy weather too. It's nice every once in a while."
hi "อื้ม ฉันก็ชอบฝน นาน ๆ ทีก็ดีเหมือนกัน"

# hi "I wonder what is it about the rain."
hi "อยากรู้จังว่าฝนมันพิเศษตรงไหน"

show ev rin_rain_towards_close at Position(xalign=0.5, yalign=0.0)
hide ovl
with charachange

# rin "Everything."
rin "ทุกตรง"

show ev rin_rain_towards:
    xalign 0.5 yalign 0.5 zoom 1.05 subpixel True
    ease 5.0 zoom 1.0
with locationchange

$ renpy.music.set_volume(0.35, 6.0, channel="ambient")

# "A silence follows the statement, as it allows for no continuation. I decide to push the direction of the conversation a little."
"ความเงียบตามประโยคนั้นมาเพราะต่ออะไรไม่ได้แล้ว ฉันนึกเปรยเปลี่ยนเรื่องคุยเสียหน่อย"

# hi "But you know, if you like the feeling of being connected, what's the problem with showing your paintings to others?"
hi "แต่เนี่ย ถ้าเธอชอบที่ได้เชื่อมต่อ แล้วทำไมเธอถึงไม่อยากเอารูปที่เธอวาดให้คนอื่นดูล่ะ"

# hi "Don't you want to be connected to other people?"
hi "เธอไม่อยากเชื่อมต่อกับคนอื่นเหรอ"

show ev rin_rain_away at Position(zoom=1.0)
show ovl rin_rain_hisaotowards behind rain at Position(xalign=1.0, yalign=0.0)
with charachange

# rin "It's not the same thing. You're comparing apples and squids."
rin "ไม่เหมือนกันสักหน่อย นายคิดแบบลวก ๆ ไปนะ เหมือนจับแพะชนไก่"

# "I brought up the subject Rin wants to avoid, and it shuts her down again. The question stays hanging between us for the rest of the trip back to school, and I can't help wondering what on Earth I could have said to truly reach Rin."
"ฉันคุยเรื่องที่รินอยากจะเลี่ยงจนเธอปิดกั้นตัวเองไปอีกแล้ว คำถามลอยค้างอยู่กลางระหว่างเราสองคนอย่างนั้นไป\nตลอดทางกลับโรงเรียน ฉันอดคิดไม่ได้ว่าจะมีอะไรที่พูดแล้วส่งไปถึงรินได้จริง ๆ บ้างหรือเปล่า"

# "Does she feel that she's lacking an identity?"
"เธอรู้สึกว่าไม่มีตัวตนเหรอ"

# "She has a strong personality, but if pressed to elaborate, I'm not sure I could describe it accurately. She feels like a person who is in constant conflict with herself. I never know what to expect when I talk to her."
"เธอเป็นคนนิสัยชัดจะตาย แต่ถ้าให้อธิบายอีก ฉันก็ไม่แน่ใจเหมือนกันว่าจะพูดได้ถูกต้องหรือเปล่า เธอดูเหมือนคน\nที่จะทะเลาะอยู่กับตัวเองตลอด ฉันก็ไม่รู้เหมือนกันว่าคาดหวังอะไรอยู่ตอนที่คุยกับเธอ"

# "I wonder how she herself experiences that disconnect."
"การที่ตัวเธอเองรู้สึกถึงการหลุดคลาดขาดการเชื่อมต่อไปนั้นคือยังไงกันนะ"

# "If Rin is asking herself every day “Who am I?” and obsessively paints images to define herself day after day, what does she think of that way of living?"
"ถ้ารินถามตัวเองทุกวันว่า “ฉันเป็นใคร” แล้ววาดรูปอย่างเอาเป็นเอาตายเพื่อนิยามตัวเองวันแล้ววันเล่า เธอคิดยังไง\nกับการที่ใช้ชีวิตอย่างนั้นกัน"

hide ovl
with charachange

# "The irony is, that's the exact same question I've been asking myself for the past four or five months. For me, it was miserable. I can only assume that it's the natural state of being for this girl."
"ที่ตลกก็คือ สี่ห้าเดือนที่ผ่านมานี้ฉันก็ถามตัวเองอย่างนั้นเหมือนกัน ซึ่งเป็นความรู้สึกที่หดหู่เอามาก ๆ แต่สำหรับ\nเธอคนนี้ก็คงเป็นอย่างนั้นอยู่ตลอด"

hide ev
show bg school_dormext_full_rn behind rain
show rin basic_awayabsent_close_rn behind rain at center
with shorttimeskip

$ renpy.music.set_volume(0.7, 1.0, channel="ambient")

# "When we stop in front of the dormitories Rin turns to face me, as if sensing my thoughts from afar. Her gaze travels emptily past my left shoulder into the shapeless rainfall."
"พอมาหยุดยืนอยู่หน้าหอรินก็หันมามองฉันคล้ายจับความคิดฉันจากระยะไกลได้ สายตาว่างเปล่าเธอทอดผ่านบ่าฉัน\nไปยังม่านฝนไร้รูปร่าง"

# "Her dark eyes seem to suck the low ambient light into themselves, like a reverse mirror."
"ตาดำของเธอดูจะจะดูดกลืนแสงที่ความสว่างน้อยเข้าไปราวกับว่าเป็นกระจกแบบย้อนกลับ"

# "That empty gaze lets nothing out. If I want to understand what's going on behind those eyes, I have to work it out myself."
"สายตาว่างเปล่านั้นไม่มีสิ่งใดออกมา ถ้าอยากรู้ว่าอะไรอยู่เบื้องหลังตาคู่นั้น ฉันต้องคิดเอาเอง"

# "Rin opens her mouth, then closes it without saying anything. The silence lasts for a few more moments before she takes a step towards the dorm building door."
"รินอ้าปากแล้วปิดปากไปโดยไม่พูดอะไร ความเงียบดำเนินต่อไปอีกพักหนึ่งก่อนเธอจะเดินไปยังประตูทางเข้าหอ"

show rin basic_absent_rn
with charadistant

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

# rin "See you tomorrow."
rin "เจอกันพรุ่งนี้"

stop ambient fadeout 0.5

scene black
with dissolve


#****************************************


label th_R13:

scene bg school_dormhisao
with dissolve

# "The next morning, like every second Monday morning until he says otherwise, I have an appointment with the nurse."
"เช้าวันถัดมาเป็นวันที่มีนัดกับคุณพยาบาล ฉันต้องไปหาเขาทุก ๆ เช้าวันจันทร์ที่สองของเดือนไปจนกว่าเขาจะมี\nการปรับอะไรอีก"

# "They allow me to skip part of my first class in the morning, and I don't feel any shame in skipping the rest, either."
"ทางโรงเรียนให้ขาดเรียนคาบเช้าคาบแรกได้ และฉันก็ด้านพอที่จะโดดคาบที่เหลือไปด้วย"

# "Rather than being thankful I get to miss world history, I instead feel dread when I think about these appointments."
"ฉันไม่ได้รู้สึกยินดีที่ได้โดดเรียนวิชาประวัติศาสตร์โลก แต่กลับรู้สึกสยองแทนที่จะได้ไปหาคุณพยาบาลตามที่นัด"

scene bg school_dormbathroom
show steam
with locationchange

play ambient sfx_shower fadein 0.5

# "I wake up at the normal time anyway and wash myself in the bathroom I share with Kenji, tidying my sleep-disheveled hair."
"แต่ฉันก็ตื่นตามเวลาปกติเช่นเคยแล้วไปอาบน้ำในห้องน้ำที่ใช้ร่วมกับเคนจิพลางจัดแจงผมเผ้าที่ยุ่งเหยิง"

# "I quickly get dressed and put my laundry in the basket."
"ฉันรีบแต่งตัวแล้วจับเสื้อผ้าที่ใส่แล้วลงตะกร้า"

stop ambient fadeout 0.5
hide steam
scene bg school_dormhisao
with locationchange

# "I pack up for the school day. I have all my homework done, like usual, so I have a bit of free time now."
"ฉันเก็บข้าวของเตรียมไปเรียน การบ้านเสร็จหมดแล้วเช่นเคย ตอนนี้ยังพอจะมีเวลาว่าง"

# "There's no point in going to the morning class for 20 minutes before I'd have to get to the nurse's office, so I lie down on my bed and read a book until it's time to go."
"ไม่จำเป็นจะต้องไปเข้าเรียนคาบเช้าก่อนเพราะยังไงอีกสักยี่สิบนาทีก็ต้องมาที่ห้องพยาบาลอยู่ดี ฉันจึงนอนบนเตียง\nอ่านหนังสือรอจนได้เวลา"

scene black
with dissolve
scene bg school_nurseoffice
with locationskip

play sound sfx_doorknock2

# "The door to the nurse's office is open, which is unusual. I enter while knocking to announce my arrival. Looking up from his computer screen, he motions me to take a seat with a friendly hello."
"ประตูห้องพยาบาลเปิดอยู่ แปลก ฉันเคาะประตูเตือนแล้วเดินเข้าไป เขาละสายตาจากจอคอมพิวเตอร์แล้วบุ้ยใบ้ให้ฉัน\nไปนั่งพลางทักทายอย่างเป็นมิตร"

# "Steam wafts up from a piping hot cup of coffee on his desk. It's probably not his first today."
"ควันลอยฉุยขึ้นมาจากแก้วกาแฟร้อน ๆ ที่วางอยู่บนโต๊ะเขา สงสัยฉันจะไม่ได้มาเป็นคนแรก"

play music music_nurse fadein 0.5
$ renpy.music.set_volume(1.0, 4.0, channel="ambient")

show nurse neutral at center
with charaenter

# nk "How are you feeling on this wonderful morning, Hisao?"
nk "เป็นยังไงบ้างฮิซาโอะกับเช้าอันสดใสวันนี้"

# hi "I'm all right, I think. It was cold yesterday because of the rain so I woke up feeling a bit groggy."
hi "สบายดี มั้งครับ เมื่อวานฝนตกจนหนาว ๆ เช้านี้พอตื่นมาก็เลยรู้สึกหนักตัวนิดหน่อยน่ะครับ"

show nurse fabulous
with charachange

# nk "You too, huh? Quite a few kids got caught without an umbrella, so we've been spending time handing out masks and curing sniffles. Hmm… all right, today it's tests day. Give me your arm."
nk "เธอก็ด้วยเหรอ เห็นมีนักเรียนบางคนไม่พกร่มแล้วไปตากฝนเหมือนกันเลยต้องมารักษาอาการน้ำมูกไหลให้\nกับแจกหน้ากากอนามัยไป อืมม… เอาละ วันนี้วันดูอาการ ยื่นแขนมาหน่อย"

show nurse neutral_close
with characlose

# "I extend my left arm towards him, keeping my face expressionless. The nurse ties a rubber tourniquet around my bicep with a practiced movement and briskly goes about his business."
"ฉันทำหน้าตายยื่นแขนซ้ายไป เขาใช้สายรัดยางรัดเข้าที่บริเวณต้นแขนฉันด้วยท่าทีชำนิชำนาญก่อนจะจัดการ\nอะไร ๆ อย่างรวดเร็ว"

# "I don't think anybody really likes getting stuck with needles, but at least I got over my distaste for them. I had to. Now, I barely even twitch at the moment of truth."
"คงไม่มีใครชอบให้เข็มมาทิ่มตัวเท่าไหร่หรอก แต่อย่างน้อยฉันก็ไม่กลัวแล้ว ก็จำเป็นแหละ เดี๋ยวนี้พอถึงเวลาจริง ๆ\nฉันก็แทบไม่รู้สึกอะไรแล้ว"

# "Once that's done, a blood pressure check follows, then there are checklists and questionnaires to go through. The nurse nods and scribbles in my answers to the questions as I give them."
"พอส่วนนั้นเสร็จสิ้นแล้วก็ถึงเวลาวัดความดัน แล้วก็มีรายการตรวจสอบกับคำถามที่ต้องตอบ คุณพยาบาลพยักหน้า\nแล้วขีดเขียนคำตอบที่ฉันตอบไป"

show nurse grin_close
with charachange

# nk "All right. Let's have a listen, now."
nk "เอาละ ทีนี้ก็ขอฟังหน่อย"

show nurse neutral_close
with charachange
play sound sfx_rustling

# "I unbutton my shirt and put it neatly on the back of the chair I was using while he puts on his stethoscope."
"ฉันปลดกระดุมเสื้อออกแล้วถอดพาดไว้กับพนักเก้าอี้ตัวที่ฉันนั่งอยู่ระหว่างที่เขากำลังใส่เครื่องฟังตรวจ"

# "I know by heart the order of places where he's going to listen to my lungs and heartbeat. I adjust my breathing to be even and deep without even being asked. It's become routine now, for both of us."
"ฉันจำได้ขึ้นใจว่าเขาจะฟังที่ปอดและหัวใจตรงจุดไหนบ้าง ฉันหายใจเข้าออกให้สม่ำเสมอและเต็มที่โดยไม่ต้องรอ\nให้เขาขอ เรื่องนี้ได้กลายเป็นกิจวัตรสำหรับเราทั้งสองคนไปแล้ว"

# "It's funny, this is pretty much the only time in one's life when you really concentrate on breathing and nothing else. It has always amused me."
"ตลกดี เวลานี้คงเป็นเวลาเดียวในชีวิตที่จะได้ตั้งสมาธิอยู่กับการหายใจอย่างเดียว ได้มาตรวจทีไรฉันก็เพลินตลอด"

# "The nurse lifts the cold steel stethoscope from my chest and places it a few inches lower, listening again. The contact of the metal makes me flinch on reflex, even though I was expecting it."
"คุณพยาบาลย้ายจานโลหะเย็น ๆ นั้นลงมาต่ำเล็กน้อยเพื่อฟังอีกครั้ง พอตัวถูกจานเหล็กนั้นแนบก็สะดุ้ง แม้จะ\nเห็นอยู่กับตาว่าจะโดนแล้วก็ตาม"

show nurse concern_close
with charachange

# "He furrows his brow, but I can't tell if it's because he's unhappy or if he's trying to pick something specific out among the complex multitude of irregularities in my heartbeat."
"เขาขมวดคิ้ว แต่ฉันไม่รู้ว่าเขาขมวดคิ้วเพราะไม่พอใจหรือกำลังตรวจจับอะไรบางอย่างที่ทับซ้อนกันอยู่ในจังหวะหัวใจ\nที่เต้นผิดปกติของฉันอยู่"

# hi "Is there something wrong?"
hi "มีอะไรหรือเปล่าครับ"

# nk "Please don't talk."
nk "อย่าเพิ่งคุยนะ"

# "I shut up and become more anxious. The nurse is nice, but I can't help disliking these mandatory checkups. I wonder if I'm going to end up hating all medical appointments from now on because of these."
"ฉันเงียบไปและเริ่มร้อนรน คุณพยาบาลก็ใจดีอยู่หรอก แต่ฉันก็ไม่ชอบการตรวจที่ต้องทำประจำอะไรพวกนี้เลย นี่ฉัน\nจะพาลไม่ชอบเวลามีนัดอะไรแบบนี้ไปด้วยหรือเปล่านะ"

show nurse concern
with charadistant

# "He finally lifts the circular metal plate from my chest, allowing me to talk again."
"จนในที่สุดเขาก็ยกจานโลหะนั้นออกไปจากหน้าอกให้ฉันได้พูด"

show nurse grin
with charachange

# nk "Everything seems to be fine. Are you feeling all right yourself?"
nk "ทุกอย่างก็ดูปกติดีนะ แล้วเธอรู้สึกไม่สบายอะไรมั้ย"

# hi "I suppose. I was out yesterday when it was raining, and yeah, I really felt a bit under the weather in the morning. Maybe I caught a cold."
hi "ไม่น่านะครับ พอดีเมื่อวานออกไปตากฝน แล้วก็นั่นแหละครับ เช้านี้ตื่นมาเหมือนไม่สบายยังไงไม่รู้ สงสัยเป็นหวัด\nนั่นแหละครับ"

show nurse fabulous
with charachange

# nk "Were you with Emi? She came down with a cold, too. My people told her to stay in bed for a day or two."
nk "ไปกับเอมิเหรอ เห็นเอมิก็เป็นหวัดเหมือนกัน ฉันฝากคนรู้จักไปบอกให้นอนพักสักวันสองวันไปแล้วละ"

# hi "Really? I mean, I was with her but I didn't know she got sick."
hi "เหรอครับ เอ่อ ก็ไปกับเอมิแหละครับ แต่ผมไม่รู้ว่าเธอป่วย"

# "I guess it was a dumb thing after all, for her to go out in the rain like that."
"ก็คงโง่จริง ๆ น่ะแหละ ไปตากฝนอย่างนั้นน่ะ"

show nurse neutral
with charachange

# nk "Yeah. Well, let's put that aside. Everything seems to check out for you, but remember to be careful."
nk "ใช่ แต่ช่างเรื่องนั้นก่อน เธอก็ดูสบายดีนะ แต่ระวังตัวหน่อยก็ดี"

# hi "Of course. I really don't want to go back to the hospital."
hi "ครับ ผมไม่อยากกลับไปอยู่โรงพยาบาลอีกแล้ว"

# "He catches something - maybe repressed terror, I don't know - in my voice and glances up from some papers he was looking at."
"เขาจับสังเกตน้ำเสียงฉันได้ว่ามีอะไรบางอย่าง อาจจะความกลัวลึก ๆ มั้ง ไม่รู้สิ จากนั้นก็ละสายตาจากแผ่นกระดาษ\nที่เขาดูอยู่มามองฉัน"

show nurse fabulous
with charachange

# nk "Hey, don't worry. At this stage, it would take a huge crash in your condition to get you rehospitalized."
nk "น่า ไม่ต้องห่วง ถึงขั้นนี้แล้วถ้าจะต้องให้พาเธอเข้าโรงพยาบาลอีกก็คงต้องเป็นอะไรที่ใหญ่มาก ๆ แล้วแหละ"

# "It doesn't really reassure me, but grumbling about it to him won't make any difference. I quietly take my leave."
"ไม่ได้สบายใจขึ้นเท่าไหร่ แต่บ่นกับเขาไปก็คงไม่ได้อะไรขึ้นมา ฉันเดินออกมาเงียบ ๆ"

stop music fadeout 7.0

scene bg school_nursehall
with locationchange

# "Walking along the corridor from the auxiliary building to the main school building, I encounter a young female nurse coming the other way. She smiles at me when we pass by each other."
"ระหว่างที่เดินไปตามโถงทางเดินที่เชื่อมอาคารรองกับอาคารหลักก็เจอเข้ากับพยาบาลสาวที่เดินสวนทางมา เธอยิ้ม\nให้ฉันจังหวะที่เดินสวนกัน"

scene bg school_lobby
with locationchange

$ renpy.music.set_volume(0.1, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 0.5

# "The lobby is empty of people. No surprise, since classes are still going on. I hear muffled sounds of discussion coming from behind the first floor classroom doors."
"ที่โถงใหญ่นั้นไม่มีใคร ไม่แปลก เพราะยังเป็นเวลาเรียนอยู่ ฉันได้ยินเสียงคุยกันอู้อี้ออกมาจากห้องเรียนที่อยู่ชั้นหนึ่ง"

# "I glance at my watch. I'd have to rush to get to my classroom in time, and I don't feel like going to class anyway, so I decide to climb up to the roof and have an extra-long lunch break."
"ฉันเหลือบมองนาฬิกา ถ้าจะไปเรียนให้ทันก็ต้องเร่งเท้า แต่ก็ไม่ได้อยากเรียนอยู่แล้ว ฉันจึงเดินขึ้นมาที่ดาดฟ้า\nเพื่อพักเที่ยงแบบนานพิเศษ"

# "Emi promised she'd bring something for me today but if she's sick, that's probably not going to happen. I'm not feeling hungry anyway, so it's all the same."
"เอมิสัญญาไว้แล้วว่าวันนี้จะเอาข้าวเที่ยงมาให้ แต่ถ้าป่วยอยู่ก็คงมาไม่ได้ แต่ก็ไม่ได้หิว เพราะงั้นก็ไม่เป็นไร"

play ambient sfx_rooftop fadein 0.5
$ renpy.music.set_volume(0.3, 0.5, channel="ambient")

scene bg school_staircase1
with locationchange

# "The climb up the steep stairwell to the roof is oddly liberating, almost like losing weight. I feel satisfaction that it doesn't wind me as badly as it did the first time I came up here."
"การที่ได้เดินตามบันไดชัน ๆ ขึ้นมายังดาดฟ้านั้นทำให้รู้สึกโล่งอย่างประหลาดราวกับว่าได้ลดน้ำหนัก เป็นความรู้สึก\nพอใจที่ไม่ได้ทำให้รู้สึกแย่อย่างที่ขึ้นมาที่นี่เป็นครั้งแรก"

# "I push open the squeaky door at the top and step into sunlight."
"ฉันเปิดประตูบานที่ตั้งอยู่บนสุดดังเอี๊ยดแล้วเดินออกมารับแสงแดด"

play sound sfx_door_creak
$ renpy.music.set_volume(1.0, 1.0, channel="ambient")
scene bg school_roof
with Fade(0.5, 0.1, 2.0, color="#FFF")

# "The chain link fence allows for a grand view over the treetops, all the way to the gray silhouettes of downtown, further away."
"รั้วตาข่ายเหล็กเปิดโปร่งจนเห็นทิวทัศน์สุมทุมพุ่มไม้ที่ทอดยาวไปจนถึงเงาจาง ๆ ของเมืองใหญ่ที่อยู่ไกลออกไป"

scene bg misc_sky:
    left
    subpixel True
    linear 40.0 right
with locationchange

# "The dreary weather of yesterday is just a memory now. The silvery blue sky seems to be a mere arm's reach away."
"ท้องฟ้าอันมืดมนจากเมืื่อวานนั้นไม่มีเหลือหรอ ราวกับฟ้าครามกระจ่างอยู่ใกล้แค่เอื้อม"

# "I forget for a moment that I'm in a bad mood. The warmth of the sun soaks into my bones, making me drowsy and lazy instead."
"ฉันลืมไปพักหนึ่งว่าเมื่อกี้อารมณ์ไม่ดีอยู่ ความอบอุ่นจากแสงแดดกำซาบเข้ามาถึงข้างในชวนให้ง่วงงุนเอื่อยเฉื่อย"

scene bg school_roof
with shorttimeskip
play sound sfx_normalbell

# "The bells ring for lunch break, startling me back into reality."
"ระฆังพักเที่ยงดังกระชากฉันให้ตื่นกลับมายังความเป็นจริง"

# "Soon afterwards, the quad below me bursts into life. Students pour out of the doors down on the ground floor, intent on enjoying lunch at the quad and the lush gardens in this perfect weather."
"ไม่นานลานโรงเรียงก็เต็มไปด้วยเสียงอึกทึก เหล่านักเรียนทะลักออกมาจากประตูไหลมายังชั้นหนึ่งเตรียมมุ่งไปกิน\nมื้อเที่ยงกันที่ลานโรงเรียนและสวนเขียวชอุ่มท่ามกลางอากาศอันแสนเป็นใจ"

# "When I hear the door to the stairwell being pushed open, I don't bother turning to see who it is."
"ฉันไม่แม้จะหันมองว่าใครมาเมื่อได้ยินเสียงประตูที่อยู่ตรงบันไดเปิดออก"

# "The intruder starts coming towards me with uneven footsteps. The little riverstones the roof is covered with rattle and crunch underfoot."
"คนที่เข้ามานั้นเดินมาทางฉันด้วยก้าวเดินที่ไม่สม่ำเสมอ หินกรวดที่ปูพื้นดาดฟ้าดังกรอบแกรบไปตามฝีเท้า"

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

scene bg misc_sky
with locationchange

# "The footsteps stop a few feet behind me, followed by a silence. I look upwards, into the glowing eye of the sun, absorbing its warmth with my whole body."
"เสียงฝีเท้านั้นหยุดลงไปไม่ห่างจากหลังฉันมากนัก และตามมาด้วยความเงียบ ฉันแหงนหน้ามองดวงอาทิตย์เจิดจ้า\nซึมซับความอบอุ่นเข้ามาทั้งตัว"

# rin "What are you doing?"
rin "ทำอะไรอยู่"

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

scene bg school_roof
show rin basic_absent
with locationchange

# "I turn around out of courtesy at her first words, to behold the slim, awkward figure of Rin Tezuka. She looks very much like herself today, too. Her hair is maybe a tad messier than usual, as if she just got out of bed."
"ฉันหันมองเป็นการตอบรับคำถามตามมารยาท เจ้าของคำถามนั้นคือสาวร่างบางไม่สมส่วนที่ชื่อ ริน เทซูกะ วันนี้ก็ดู\nเป็นเธอมาก ๆ ผมเธอนั้นยุ่งกว่าปกติคล้ายคนเพิ่งตื่นนอน"

# "She stands with her weight shifted onto one foot, looking at me with mild curiosity, as if I were something in a store's display window."
"เธอยืนขาเดียวเอียงตัวมองฉันด้วยความสงสัยเล็กน้อยเหมือนกับว่าฉันเป็นของตั้งโชว์ในร้าน"

# hi "I don't know. Just spacing out, I guess."
hi "ไม่รู้สิ เหม่อมั้ง"

# hi "What about you?"
hi "เธอล่ะ"

show rin basic_deadpan
with charachange

# rin "Emi promised food. We usually eat here."
rin "เอมิบอกว่าจะมีอาหาร ปกติกินกันที่นี่"

# hi "I'm afraid you're going to be disappointed. I heard Emi came down with a cold."
hi "ขอโทษที่อาจจะทำให้เธอผิดหวังนะ แต่วันนี้เอมิไม่สบาย"

show rin relaxed_nonchalant
with charachange

# rin "Oh. I guess that makes sense. She wasn't in class."
rin "อ้อ งี้นี่เอง ถึงว่าไม่มาเรียน"

# hi "It's not that common to get a cold in June though. You don't think she went running at the track afterwards like she said? The rain just kept going."
hi "แต่จะเป็นหวัดช่วงเดือนมิถุนาก็ไม่แปลก เธอว่าเอมิจะไปวิ่งที่ลู่ต่ออย่างที่บอกมั้ยล่ะ เห็นตอนนั้นฝนก็ยังตกอยู่เลย"

show rin basic_deadpanupset
with charachange

# rin "Probably."
rin "มั้งนะ"

# hi "In the rain?"
hi "กลางฝนอะนะ"

# rin "In the rain."
rin "กลางฝน"

# "That sounds like a bit too much for just keeping up with training regime. Emi is a hard-headed one, though, so I can see her running in the downpour just because she “had to.”"
"ถ้าจะบอกว่าซ้อม ขนาดนั้นก็เกินไปหน่อยมั้ง แต่เอมิก็เป็นคนรั้นจะตาย พอจะนึกภาพออกอยู่ว่าคงไปวิ่งตากฝน\nแค่เพราะเธอ “ต้อง” วิ่ง"

# hi "Well, that's obviously overdoing it. Probably why she came down with that cold, too."
hi "อืม งั้นก็ทำเกินไปหน่อยแล้ว สงสัยที่เป็นหวัดก็คงเพราะงี้"

# hi "But I guess it's kinda cool."
hi "แต่ก็เท่ดีละมั้ง"

show rin relaxed_boredom
with charachange

# rin "Speaking of that, I'm not feeling well either. I…"
rin "จะว่าไป ฉันก็ไม่ค่อยสบายเหมือนกัน ฉัน…"

stop ambient

show rin relaxed_sleepy
with vpunch

# rin "ACHOO!"
rin "ฮัดเช้ย!"

play music music_another fadein 4.0

# "Rin sneezes pretty hard, failing to stop it in time. She cranes her head down to wipe her nose on her shoulder, so deciding that would be too unladylike I pull out my handkerchief and hold it to her nose."
"รินกลั้นจามที่ดังพอตัวนั้นไว้ไม่ทัน เธอเอียงคอมาใช้ไหล่เช็ด ๆ จมูก พอเห็นกิริยาที่ไม่งามอย่างนั้นฉันก็หยิบ\nผ้าเช็ดหน้าออกมาแล้วจ่อที่จมูกเธอ"

show rin relaxed_sleepy_close
with characlose

# hi "Here. Bless you."
hi "เอ้านี่"

show rin relaxed_doubt_close
with charachange

# rin "Danks."
rin "จัย"

# "She clears her nose and I dab the handkerchief gently on it, wiping it clean."
"เธอสูดจมูก หลังจากนั้นฉันก็ใช้ผ้าเช็ดหน้าซับให้เบา ๆ จนสะอาด"

# "Her nose is really cute. Oddly enough it's probably the girliest part of Rin's face. I think I'm blushing a little, but Rin doesn't notice."
"จมูกน่ารักดี แต่ก็แปลกดีที่ตรงนี้น่าจะเป็นจุดที่ดูเป็นผู้หญิงสุดบนหน้ารินแล้ว เหมือนฉันจะแก้มแดงหน่อย ๆ ด้วย\nแต่รินก็ไม่ทันสังเกตเห็น"

show rin basic_lucid_close
with charachange

# rin "Thanks - I think I might be coming up or down with something, too. Like I was saying."
rin "ขอบใจ ฉันน่าจะเป็นหวัดหรือวัดหรืออะไรอยู่ อย่างที่บอกเมื่อกี้"

# hi "Hope not."
hi "หวังว่าจะไม่นะ"

show rin basic_awayabsent_close
with charachange

# "Rin doesn't seem to be to bothered about eating, so despite the lack of Emi-provided lunch, we stay up on the rooftop. She comes over and stands next to me, right up against the fence, looking into the same abstract distance as I am."
"รินดูจะไม่ใส่ใจเรื่องกินมากนัก เพราะงั้นพวกเราก็อยู่ที่ดาดฟ้ากันทั้ง ๆ ที่ไม่มีข้าวเที่ยงจากเอมิ เธอมายืนตรงหน้ารั้ว\nอยู่ข้าง ๆ ฉันมองไปสักที่ไกล ๆ เหมือนที่ฉันมอง"

# "Nobody else seems to be coming around to intrude upon this calmness, either. It's quiet and peaceful."
"ไม่มีใครดูอยากจะรบกวนบรรยากาศที่ได้อยู่กันสบาย ๆ อย่างนี้ด้วย รอบตัวเรานั้นทั้งเงียบและสงบ"

stop music fadeout 2.0
play ambient sfx_rooftop fadein 3.0

scene bg school_roof
with shorttimeskip

# "What does one do on a lunch break if not eat?"
"ถ้าไม่กินข้าวแล้วพักเที่ยงทำอะไรกัน"

# "It turns out that, between the two of us, we don't really know. Fortunately, passing time is an activity that manages itself just fine."
"สรุปแล้วพวกเราก็ไม่มีใครรู้ว่าต้องทำอะไร แต่โชคดีที่แค่อยู่เฉย ๆ ปล่อยให้เวลาไหลไปก็เป็นอันใช้ได้แล้ว"

# "Even though there's no conversation to fill the silence between the passing seconds, no pointless activities like cloud-gazing to spend upon the minutes between now and then, time marches on relentlessly."
"ถึงจะไม่มีบทสนทนาคอยถมช่องว่างช่วงหลายร้อยวินาที ไม่มีการมองก้อนเมฆไร้สาระที่ได้มาดูบ้างเป็นบางครั้ง\nคอยถมช่องว่างช่วงหลายสิบนาที เวลาก็ยังคงดำเนินต่อ"

# "I keep checking the time on my watch, then decide it's a dumb thing to do. Instead, I try to hold out for as long as possible before I check it again. Maybe I can hold out for six or seven minutes."
"ฉันคอยก้มมองนาฬิกาข้อมือเรื่อย ๆ จนสุดท้ายก็คิดได้ว่าจะทำไปทำไม ฉันจึงคอยให้นานที่สุดก่อนจะก้มดูอีกครั้ง\nน่าจะคอยได้สักหกหรือเจ็ดนาที"

show rin basic_awayabsent_close at center
with charaenter

# "Rin remains silent, idly looking up at the cerulean expanse above us."
"รินยังคงเงียบเหม่อมองผืนแผ่นสีครามที่อยู่เหนือเรา"

# "I wonder why, more often than not, we don't speak much. She said that she doesn't like speaking because of her perceived difficulties with expressing herself properly."
"ทำไมพวกเราถึงได้ไม่คุยกันบ่อยขนาดนี้นะ เธอบอกว่าไม่ชอบพูดเพราะรู้สึกว่าการสื่อสารสิ่งที่อยากจะบอก\nนั้นยาก"

# "As for me, I think I just got sucked into the habit at the hospital, where I spent such a long stretch of time never really talking to anyone."
"ส่วนฉันก็น่าจะเป็นเพราะติดนิสัยตอนอยู่โรงพยาบาลไปแล้ว เพราะตอนนั้นนาน ๆ ทีถึงจะได้คุยกับใคร"

# "Most of the time I feel comfortable about this quiet mood. And even when I get the feeling that I have to break the silence, it's always so difficult to come up with something to talk about when it's with Rin."
"ส่วนมากแค่ได้อยู่เงียบ ๆ อย่างนี้ก็พอใจแล้ว หรือต่อให้อยากพูด ก็ไม่รู้จะหาอะไรมาคุยกับคนอย่างรินดี"

# "She and I are on such different wavelengths that nothing seems to be on common ground."
"เธอกับฉันนั้นต่างกันจนไม่มีอะไรร่วมกัน"

# hi "What is it that you like about the sky so much?"
hi "ทำไมเธอถึงชอบท้องฟ้าขนาดนี้"

show rin basic_deadpannormal_close
with charachange

# "She turns to me, her eyes dark and serious."
"เธอหันมาทางฉัน ดวงตาเข้มนั้นฉายแววจริงจัง"

show rin basic_deadpan_close
with charachange

# rin "Sky is the only thing that is perfect."
rin "ท้องฟ้าเป็นอย่างเดียวที่สมบูรณ์แบบ"

show rin basic_awayabsent_close
with charachange

# rin "I know it. You could say I'm an expert of sky if you wanted. And I am even if you didn't want to. A sky expert."
#The bad grammar in this sentence and the following is intentional. LEAVE IT ALONE. -SC & Aura
rin "ฉันรู้ จะเรียกฉันเป็นผู้เชี่ยวชาญด้านท้องฟ้าก็ได้ถ้าต้องการ ไม่ต้องการฉันก็เป็น ผู้เชี่ยวชาญฟ้า"

# rin "It's always different, but it's always perfect also when it's different."
rin "ต่างตลอด แต่สมบูรณ์แบบตลอดเหมือนกันและแม้ต่างตลอด"

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

scene bg misc_sky at Fullpan (8.0)
with locationchange

# "I follow her gaze up into the boundless blue expanse, thinking of her words."
"ฉันมองตามที่เธอมองไปยังแดนฟ้ากว้างไกลพลางคิดถึงสิ่งที่เธอพูด"

# hi "Have you ever wanted to be something different?"
hi "เธอเคยอยากเป็นอย่างอื่นมั้ย"

# rin "It wouldn't be so bad to be the sky."
rin "เป็นท้องฟ้าก็คงไม่แย่"

# hi "No, I mean, someone else, someone different. To go to a normal school like everyone else, not have to worry about stuff…"
hi "ไม่สิ หมายถึงว่า คนอื่น คนละคน ได้ไปโรงเรียนอย่างคนอื่น ไม่ต้องคิดมากอะไร…"

rin "อะไรคืออะไร"

# "I try to find the right words for a moment, but can't manage to form a sentence that I'd be comfortable with actually using."
"ฉันนึกหาคำอยู่พักหนึ่ง แต่ก็ไม่รู้จะเอามาใส่ประโยคยังไงให้พูดได้ไม่กระดากปากดี"

# hi "Man, I don't really want to say it aloud."
hi "เฮ้อ ไม่อยากพูดออกมาเลย"

# rin "Try. I'm not so good at mind reading."
rin "พูด ฉันอ่านใจไม่เก่ง"

stop ambient fadeout 0.5
scene bg school_roof
show rin basic_awayabsent_close
with locationchange

# hi "Don't you ever want to not be disabled?"
hi "เธอเคยอยากไม่พิการมั้ย"

# "She thinks about this and then shakes her head, frowning."
"เธอคิดแล้วส่ายหัวพลางขมวดคิ้ว"

show rin negative_annoyed_close
with charachange

# rin "That's a hard question. I don't know what to say."
rin "ตอบยาก ไม่รู้จะพูดยังไง"

# hi "It's okay if you don't say anything."
hi "ไม่ต้องตอบอะไรก็ได้ ไม่เป็นไร"

# hi "For some reason, I'm just so unsatisfied with who I am right now that I'm constantly thinking stuff like that. It's pretty hard to admit, but there it is."
hi "ไม่รู้ทำไม แต่ฉันไม่พอใจกับตัวฉันคนนี้จนเอาแต่คิดอะไรอย่างนั้นน่ะแหละ ไม่ค่อยอยากยอมรับหรอก แต่มันก็คิด\nจริง ๆ"

# "Honestly, I feel relieved about finally saying it aloud to someone, even if it's just Rin."
"ว่าตามตรงก็รู้สึกโล่งที่ได้พูดออกมาให้ใครสักคนฟังสักที ถึงจะมีแค่รินก็เถอะ"

show rin negative_confused_close
with charachange

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play music music_serene fadein 8.0

# rin "I think I want to be different, sometimes. I've thought about changing myself lately, but it's a bit scary, like walking backwards with your eyes closed."
rin "ฉันว่า บางที ฉันก็อยากเป็นอย่างอื่น ช่วงนี้ฉันอยากเปลี่ยนตัวเอง แต่ก็แอบกลัว เหมือนหลับตาเดินถอยหลัง"

show rin negative_worried_close
with charachange

# rin "The difficult part is to know where your toes are not pointing. I mean, directions."
rin "ที่ยากก็คือต้องรู้ว่าทางไหนที่นิ้วเท้าชี้ไปอีกทาง คือ หมายถึงทิศทางนะ"

show rin basic_sad_close
with charachange

# rin "Even if I don't do anything, I would never stay the same."
rin "ต่อให้ฉันไม่ทำอะไร ฉันก็จะไม่เหมือนเดิม"

show rin negative_spaciness_close
with charachange

# rin "It's like my old paintings. They are different than what I paint now, because I'm different, but they are still my paintings so there's something same. That's really strange."
rin "เหมือนภาพที่ฉันเคยวาดไว้ ภาพพวกนั้นต่างจากภาพที่ฉันวาดตอนนี้ เพราะฉันต่าง แต่ก็ยังเป็นภาพที่ฉันวาด\nเพราะงั้นก็แปลว่ายังมีอะไรเหมือนเดิม แปลกมาก ๆ"

show rin basic_lucid_close
with charachange

# rin "I am different every day, but I'm still me every day. Who am I then?"
rin "ทุกวันฉันต่าง แต่ทุกวันฉันก็เหมือนเดิม แล้วฉันคือใคร"

# hi "Is that a riddle?"
hi "อันนี้เล่นทายปัญหาเหรอ"

show rin basic_deadpanupset_close
with charachange

# rin "If you want it to be. I don't know the right answer though, so you have to come up with it yourself."
rin "ถ้าอยากจะเอาไปทายก็เอาเลย แต่ฉันไม่รู้คำตอบนะ นายต้องคิดขึ้นมาเอง"

# hi "Well, it's the sky, isn't it? Going by your definition just now."
hi "งั้นคำตอบคือท้องฟ้าใช่มั้ยล่ะ ถ้าว่าตามที่เธอบอกเมื่อกี้"

show rin basic_surprised_close
with charachange

# "I actually manage to surprise her by that. Maybe she had already forgotten about it."
"คำพูดนั้นของฉันทำให้เธอประหลาดใจ เธอน่าจะลืมไปแล้ว"

show rin basic_deadpansurprised_close
with charachange

# rin "That's right! But I was thinking about myself when I said that. Very strange."
rin "จริงด้วย! แต่ตอนพูดฉันนึกถึงตัวเองอยู่นะ แปลกมาก"

show rin basic_lucid_close
with charachange

# rin "Could it be that I actually am the sky?"
rin "หรือจริง ๆ แล้วฉันคือท้องฟ้า"

# hi "I don't think that's possible. Your logic's a bit off somewhere."
hi "ไม่น่าเป็นไปได้นะ เธอโยงอะไรพลาดแล้วละ"

show rin basic_awayabsent_close
with charachange

# "She looks down and shuts up and I can see she's quickly going over the deduction mentally, seemingly unhappy with the result she finally arrives at."
"รินก้มหัวแล้วเงียบไปทำสีหน้าว่าคิดถึงตรรกะที่โยงเมื่อกี้อยู่ในใจ เธอดูไม่พอใจกับข้อสรุปนั้นที่คิดได้"

show rin basic_deadpanupset_close
with charachange

# rin "Yeah, maybe I'm not the sky. Would make sense, I have a hard time knowing what kind of a person I am."
rin "อืม ฉันน่าจะไม่ใช่ท้องฟ้า ก็จริงนะ ฉันนึกไม่ออกว่าฉันเป็นคนยังไง"

# hi "You're not the only one."
hi "ไม่ใช่แค่เธอคนเดียวหรอก"

show rin negative_spaciness_close
with charachange

# rin "It's like my mind is in some other place than the rest of me."
rin "เหมือนใจฉันอยู่คนละที่กับตัว"

# hi "Underwater."
hi "ใต้น้ำ"

show rin basic_awayabsent_close
with charachange

# rin "Yeah. I wonder how it got there."
rin "อืม อยากรู้จังว่าไปอยู่ตรงนั้นได้ยังไง"

# "I have no answer, so a brief silence falls between us for a moment. I shift my gaze back to the sky above us."
"ฉันไม่มีคำตอบต่อ ความเงียบจึงกลับมาอยู่กับพวกเราอีกพักหนึ่ง ฉันหันมองท้องฟ้าที่อยู่เหนือพวกเรา"

$ renpy.music.set_volume(0.5, 2.0, channel="music")

window hide

scene bg misc_sky
with locationchange

nvl clear
nvl show dissolve

# n "\n\nThe last time I really paid much attention to the sky was… I guess it must've been at the hospital. I could only see a thin strip of sky from the window of my room. If I walked up to the windows and pressed my face against the cold glass, the strip became bigger, but not by much."
n "\n\nครั้งล่าสุดที่ฉันได้จดจ่ออยู่กับท้องฟ้าขนาดนี้เป็นตอน… น่าจะตอนที่อยู่โรงพยาบาลแน่ ๆ ฉันเห็นเพียงแถบท้องฟ้า\nผ่านหน้าต่างห้องฉัน ถ้าเดินไปเอาหน้าแนบหน้าต่างเย็น ๆ แถบที่ว่านั้นก็ขยายใหญ่ขึ้น แต่ก็ไม่ได้ใหญ่ขึ้นมาก"

# n "That sky made me feel sad and lonely, a reminder of the world on the other side. I wonder if there's another world beyond the sky we see from up here on the school's roof, as well."
n "ท้องฟ้าผืนนั้นที่เป็นเครื่องเตือนถึงโลกอีกฟากฝั่งทำให้ฉันเศร้าและเหงา จะมีอีกโลกหนึ่งที่อยู่เหนือท้องฟ้าที่เรามอง\nจากดาดฟ้าโรงเรียนนี้ด้วยเหมือนกันหรือเปล่านะ"

# n "I can't stop comparing life at Yamaku to my hospitalization, but I really should. I'm not there any more."
n "ฉันอดไม่ได้ที่จะเทียบชีวิตในรั้วยามากุกับในห้องที่โรงพยาบาล แต่ก็ต้องเป็นอย่างนั้นเพราะฉันไม่ได้อยู่ที่นั่นแล้ว"

# n "The narrow sky from the window of my hospital room, the faces of the doctors, the faces of my parents. The off-white walls everywhere. Iwanako's letter, echoing the words she never said. They're things of the past now."
n "ท้องฟ้าแคบ ๆ หลังหน้าต่างห้องที่โรงพยาบาล ใบหน้าของหมอ ใบหน้าของพ่อแม่ กำแพงขาวสะอ้านที่ห้อมล้อม\nจดหมายของอิวานาโกะที่สะท้อนก้องคำที่เธอไม่เคยพูด เหล่านั้นเป็นอดีตไปแล้ว"

# n "I wish I could forget everything up until now and that time would stop completely. There would be only me, Rin, and the sky, an eternal lunch break on this rooftop. Perfect, unchanging, and forever."
n "ฉันอยากจะลืมทุกสิ่งอย่างที่ผ่านมาแล้วให้เวลาหยุดลง สิ่งที่เหลือมีเพียงฉัน ริน และท้องฟ้า เป็นพักเที่ยงชั่วนิรันดร์\nสมบูรณ์แบบ ไม่แปรเปลี่ยน อยู่ตลอดกาล"

$ renpy.music.set_volume(1.0, 2.0, channel="music")

nvl clear
nvl hide dissolve

window show

# hi "I'm not sure if I like or hate this school."
hi "ฉันไม่แน่ใจว่าฉันชอบหรือเกลียดโรงเรียนนี้"

# rin "I could have gone to a normal school if I wanted, but I chose to come here."
rin "ถ้าฉันจะไปโรงเรียนปกติฉันก็ไปได้ แต่ฉันเลือกจะมาที่นี่"

scene bg school_roof
show rin relaxed_nonchalant_close at center
with locationchange

# hi "Why?"
hi "ทำไม"

show rin relaxed_doubt_close
with charachange

# rin "I just decided I would. Kind of like melon or plum jelly."
rin "ฉันแค่เลือกว่าจะมา เหมือนให้เลือกแตงโมงหรือเยลลีลูกไหน"

# hi "Do you think it was a good idea?"
hi "แล้วคิดว่าดีมั้ย"

# hi "I mean, there are a lot of good things about this school, but I think there are a few bad things also."
hi "คือ ที่โรงเรียนนี้ก็มีอะไรดี ๆ เยอะ แต่อะไรแย่ ๆ มันก็มีบ้าง"

show rin basic_lucid_close
with charachange

# rin "I know."
rin "รู้"

show rin basic_awayabsent_close
with charachange

# rin "I kind of collect people, because they are interesting. People here really are amazing. Most of them. But not all."
rin "ฉันสะสมคน เพราะคนน่าสนใจดี คนที่นี่ก็น่าทึ่งกันทั้งนั้น ส่วนใหญ่นะ แต่ไม่ทั้งหมด"

show rin negative_angry_close
with charachange

# rin "Some people can't take it. They hurt too much. It gets really bad sometimes, you know. They hurt."
rin "บางคนก็ทนไม่ไหว บอกว่าเจ็บเกิน บางทีมันก็หนักเหมือนกันนะ เลยเจ็บ"

show rin basic_deadpanupset_close
with charachange

# rin "I wonder if you're like that too? I hope not. I don't like things like that."
rin "นายเป็นแบบนั้นด้วยหรือเปล่า หวังว่าจะไม่นะ ฉันไม่ชอบอะไรอย่างนั้น"

# hi "Hey, I'm not your case study. And I'm not going to give up and die or anything."
hi "เฮ้ย ฉันไม่ใช่ตัวกรณีศึกษาให้เธอนะ แล้วฉันก็จะไม่ตายหรืออะไรหรอก"

# hi "Anyway, I meant more that this place is too distant from the real world."
hi "แต่เอาเถอะ ที่ฉันถามคือเพราะที่นี่มันไกลจากโลกความเป็นจริงเกินไป"

show rin basic_surprised_close
with charachange

# rin "What's the real world?"
rin "โลกความเป็นจริงคืออะไร"

# hi "Everything out there. Real people, with normal everyday lives that fit together like a puzzle."
hi "ทุกอย่างที่อยู่ข้างนอกโน่นน่ะ คนจริง ๆ ที่ลงล็อกใช้ชีวิตตามปกติทุกวัน"

show rin relaxed_surprised_close
with charachange

# rin "You don't think we aren't like that? Real people?"
rin "นายคิดว่าเราไม่ใช่อย่างนั้นเหรอ คนจริง ๆ ที่ว่าน่ะ"

# hi "Maybe we aren't. Well, no, we are. I just meant that it feels more like we're the leftover pieces."
hi "ก็อาจจะไม่นะ คือ ไม่ ใช่สิ ที่ฉันหมายถึงคือเหมือนว่าเราเป็นเศษเหลืออะไรอย่างนี้มากกว่าน่ะ"

show rin negative_annoyed_close
with charachange

# "Rin thinks for a while, her almond-shaped eyes narrowing as she bites her lip a little bit, like a child."
"รินครุ่นคิดอยู่พักหนึ่ง เธอหรี่ตากลมของเธอลงพลางกัดริมฝีปากเบา ๆ อย่างเด็ก"

show rin basic_deadpansurprised_close
with charachange

# rin "Is it hard to be disabled?"
rin "พิการแล้วมันลำบากเหรอ"

# "Her question earns a dry chuckle from me."
"คำถามของเธอทำให้ฉันต้องแค่นหัวเราะแห้ง ๆ"

# hi "You tell me. You've been in this business a lot longer than I have."
hi "ฉันสิต้องถามเธอ เธออยู่วงการนี้มานานกว่าฉันอีกนี่"

show rin negative_annoyed_close
with charachange

# "She thinks about that for another while."
"เธอครุ่นคิดอยู่อีกพักหนึ่ง"

show rin basic_deadpancontemplation_close
with charachange

# rin "I don't really feel that disabled. I mean I do pretty much everything differently, but it's not that hard. I can always practice."
rin "ฉันไม่ได้รู้สึกพิการขนาดนั้น คือก็ทำอะไรหลายอย่างที่ใช้วิธีแบบไม่ปกติแหละ แต่ก็ไม่ได้ลำบากขนาดนั้น\nหัดทำอะไรได้อยู่แล้ว"

show rin basic_deadpandelight_close
with charachange

# rin "I've started to practice food things this year. I think I'd want to learn to cook in a real kitchen someday."
rin "ปีนี้ฉันหัดกินอาหารด้วยละ คิดว่าสักวันจะหัดทำอาหารในครัวจริง ๆ ด้วย"

# hi "That's admirable, but I don't think it's just a state of mind."
hi "นับถือเลย แต่ฉันมองว่ามันไม่ใช่แค่เรื่องความรู้สึกหรอก"

show rin basic_lucid_close
with charachange

# rin "Maybe not to you."
rin "สำหรับนายก็คงงั้น"

# "I have no good counter to that, so I concede by falling silent. The situation is making me more and more confused."
"ฉันไม่รู้จะแย้งยังไงต่อจึงยอมเงียบล่าถอยไป ฉันยิ่งสับสนหนักกับสิ่งที่เกิดขึ้น"

# "I know what I want, but don't know how to reach it. Rin seems to believe she can simply will herself into the shape she thinks she needs to be, but can't decide whether she wants to be a bird or a butterfly."
"ฉันรู้ว่าต้องการอะไร แต่ไม่รู้ว่าจะไปคว้ายังไง รินดูจะเชื่อว่าแค่คิดอยากจะเป็นรูปร่างแบบไหนก็เป็นได้ แต่ไม่รู้ว่าจะเป็น\nนกหรือผีเสื้อดี"

show rin basic_awayabsent_close
with charachange

# rin "I think, in the end I'm not really that happy with who I am either, but that doesn't mean I regret being who I am."
rin "ฉันว่า เอาเข้าจริง ๆ ฉันก็ไม่ได้พอใจขนาดนั้นกับตัวฉันอย่างที่เป็นอยู่หรอก แต่ก็ไม่ได้แปลว่าฉันเสียใจกับตัวฉัน\nอย่างที่เป็นนะ"

show rin relaxed_nonchalant_close
with charachange

stop music fadeout 0.5

# rin "That's the thing that's wrong with you, Hisao."
rin "นั่นแหละคือปัญหาของนาย ฮิซาโอะ"

play sound sfx_rustling

scene bg school_roof_blurred
show rin basic_lucid_superclose at center
with characlose

# "I've only started to process that rather blunt statement before Rin suddenly hugs me."
"สมองฉันเพิ่งประมวลผลคำพูดที่ออกจะโผงผางนั้นก็ตอนที่รินเข้ามากอด"

# hi "What are you doing?"
hi "ทำอะไรน่ะ"

# "I've never been hugged by a girl with no arms before. To be honest, it doesn't really, physically feel like a hug. The awkward way she presses her body against mine and the lack of embracing arms makes it feel like she fell on top of me."
"ฉันไม่เคยถูกสาวที่ไม่มีแขนกอดมาก่อน เอาตรง ๆ สัมผัสนั้นก็ไม่ได้รู้สึกเหมือนการกอดสักเท่าไหร่ ท่าที่เธอใช้\nลำตัวแนบดูแปลก ๆ โดยไม่มีแขนโอบนี้ให้ความรู้สึกเหมือนว่าเธอทับตัวฉันอยู่มากกว่า"

# "But the warmth of a real hug is still there, and that's how I recognize it for what it is."
"แต่ฉันสัมผัสได้ถึงความอบอุ่นอย่างการกอด และเช่นนั้นฉันถึงได้รู้ว่าสิ่งนี้คือการกอด"

show rin basic_deadpannormal_superclose
with charachange

play music music_comfort fadein 9.0

# rin "I'm hugging you, Hisao."
rin "ฉันกอดนายอยู่นะ ฮิซาโอะ"

# hi "I know that, but…"
hi "รู้แล้ว แต่…"

show rin relaxed_doubt_superclose
with charachange

# rin "Is it wrong? I thought this is what you're supposed to do."
rin "ไม่ใช่เหรอ นึกว่าต้องทำอย่างนี้เสียอีก"

show rin relaxed_sleepy_superclose
with charachange

# rin "I'm not really used to this kind of thing. The first time Emi hugged me I got surprised and kicked her in the stomach. I can kick pretty hard so she hasn't been hugging me an awful lot after that."
rin "ฉันไม่ชินกับอะไรแบบนี้เท่าไหร่ ตอนที่เอมิกอดฉันครั้งแรกฉันตกใจจนเผลอถีบท้องเธอไป แล้วฉันดันถีบแรงจน\nหลังจากนั้นเธอก็ไม่ได้กอดฉันบ่อย ๆ เลย"

# hi "It's not wrong. Just, no, it's just me… things are a bit hard for me, for the time being. I can't seem to react properly to anything."
hi "ไม่ผิดหรอก แค่ ไม่สิ แค่ฉัน… ช่วงนี้อะไร ๆ มันมากมายไปหมด ฉันเหมือนจะตอบสนองอะไรได้ไม่ดีเลย"

show rin relaxed_surprised_superclose
with charachange

# rin "Really? So it is hard being disabled after all?"
rin "จริงเหรอ แสดงว่าพิการก็ลำบากจริงงั้นสิ"

# "I guess she has me cornered there. I don't have the energy to start arguing against it, but I feel like I have to get something out."
"คงจนมุมเท่านี้ละ ฉันไม่มีแรงจะเถียงอะไรอีก แต่ก็รู้สึกเหมือนต้องระบายบางอย่าง"

# hi "Well, I… no, it's not hard. I think it's just me overthinking things."
hi "ก็นะ ฉัน… ไม่สิ ไม่ได้ลำบาก ฉันแค่คิดอะไรมากไป"

# hi "I really wish I didn't feel so sorry for myself all the time."
hi "ฉันไม่อยากเอาแต่นึกสมเพชตัวเองอยู่อย่างนี้"

# "I wonder if I always was this fragile or if I became this way after my incident. Nothing had ever truly shaken my world like that before, so there's no telling."
"ฉันเปราะบางอย่างนี้อยู่แล้ว หรือเพิ่งเป็นหลังเหตุการณ์นั้นกัน เพราะไม่เคยมีอะไรที่เปลี่ยนชีวิตฉันได้อย่างจริงจัง\nขนาดนั้นมาก่อน คงไม่มีทางรู้ได้แน่"

show rin basic_lucid_superclose
with charachange

# "Rin presses her cheek against me tightly. I can feel the warmth of her body close against me."
"แก้มรินแนบแน่นอยู่กับตัวฉัน ฉันสัมผัสได้ถึงความอบอุ่นจากร่างกายเธอที่อยู่ใกล้ชิด"

# "Her body temperature feels really high, as if she had absorbed the sunlight into herself and was now sharing it with me. Or perhaps it's a natural state for her."
"ตัวเธอนั้นร้อนมากราวกับว่าได้ดูดแสงอาทิตย์ไว้กับตัวแล้วมาแบ่งให้ฉัน หรือตัวเธออาจจะเป็นอย่างนี้อยู่แล้วก็ได้"

# "It's the most comforting thing I've felt in a long, long time."
"ฉันไม่ได้สัมผัสอะไรที่แสนอบอุ่นขนาดนี้มานานแสนนานมากแล้ว"

show rin basic_deadpan_superclose
with charachange

# rin "Wow, your heartbeat really does sound really weird. It's like a drunken percussion orchestra."
rin "โห เสียงหัวใจนายเต้นแปลกจริงด้วย เหมือนวงดุริยางค์เครื่องกระทบที่คนเล่นเมาเลย"

# hi "Please don't say stuff like that. I get very uncomfortable."
hi "อย่าพูดอย่างนั้นเลยนะ ฉันอึดอัดน่ะ"

# "I laugh at her comment anyway, in an attempt to ease the tension. It sounds a little bit too forced."
"แต่ฉันก็หัวเราะไปกับคำพูดของเธออยู่ดีด้วยหวังจะคลายเครียด เสียงหัวเราะนั้นฟังดูฝืน ๆ นิดหน่อย"

# hi "Man, I'm sorry I'm such a mess."
hi "เฮ้อ ขอโทษที่ฉันไม่เอาไหนอย่างนี้นะ"

show rin basic_deadpannormal_superclose
with charachange

# rin "It's okay. It's the best part of you."
rin "ไม่เป็นไร ตรงนั้นแหละคือสิ่งที่ดีที่สุดของนาย"

# hi "Hearing that doesn't make me happy."
hi "ฟังแล้วไม่ได้ดีใจขึ้นมาเลยนะ"

scene bg school_roof
show rin basic_deadpannormal_close at center
with charadistant

# "She breaks off the hug and settles down. An awkward silence falls upon us like a blanket; me feeling embarrassed about myself and Rin trying to arrange her expression to something she likes."
"เธอผละตัวออกแล้วนั่งลง ความเงียบเข้าปกคลุมพวกเราอย่างผ้าห่ม ฉันยังอายกับตัวเองอยู่ ส่วนรินก็กำลังปรับสีหน้า\nไปตามใจเธออยาก"

$ renpy.music.set_volume(0.5, 2.0, channel="music")

scene bg misc_sky
with locationchange

# "One last time, I glance upwards."
"ฉันแหงนมองอีกครั้งส่งท้าย"

# hi "This rooftop is really great. It's like I'm just a little bit closer to the sky."
hi "ดาดฟ้านี่เยี่ยมจริง ๆ รู้สึกเหมือนได้เข้าใกล้ท้องฟ้าไปอีกหน่อยเลย"

# rin "I know a better place, but we can't go there on lunch break. I can take you there sometime if you want."
rin "ฉันรู้จักที่ที่ดีกว่านี้นะ แต่จะไปตอนพักเที่ยงไม่ได้ ถ้าอยากไปเดี๋ยวสักวันจะพาไป"

play sound sfx_warningbell

# "The bells ring for the beginning of the afternoon classes and Rin stands up to make her way downstairs. I don't hurry after her, deciding to stay up here for just a little while longer."
"ระฆังดังส่งสัญญาณเริ่มคาบบ่าย รินลุกขึ้นยืนแล้วเดินลงบันไดไป ฉันไม่ได้รีบตามเธอไปเพราะอยากอยู่บนนี้ต่ออีก\nสักหน่อย"

$ renpy.music.set_volume(1.0, 2.0, channel="music")

scene bg school_roof
show rin basic_awayabsent at center
with locationchange

# hi "Thanks for the hug."
hi "ขอบคุณที่กอด"

show rin basic_lucid
with charachange

# rin "Thanks for not kicking me."
rin "ขอบคุณที่ไม่เตะ"

hide rin
with charaexit

# "After Rin leaves I finally let tears roll down my cheeks and cry for my condition for the first and only time in my life."
"พอรินไปแล้วฉันก็ปล่อยน้ำตาให้ไหลอาบแก้ม ร้องไห้ให้กับโรคนี้ของฉันเป็นครั้งแรกและครั้งเดียวในชีวิต"

# "Then I cast away that hollow person lying on the hospital bed, forever."
"แล้วทิ้งตัวฉันอันเปล่ากลวงคนนั้นที่นอนอยู่บนเตียงโรงพยาบาลไปตลอดกาล"

stop music fadeout 2.0
scene black
with dissolve


#***************************************************


label th_R14:

scene bg school_scienceroom
with locationchange

# "Two days later, I'm feeling less miserable. I even go for a long, brisk, healthy walk like the nurse recommended, something which I had avoided and dodged with all sorts of excuses earlier."
"สองวันให้หลังฉันก็หดหู่น้อยลงแล้ว ออกไปเดินเร็วนาน ๆ เพื่อสุขภาพอย่างที่คุณพยาบาลแนะนำด้วย ซึ่งก่อนหน้านี้\nฉันอ้างสารพัดเลี่ยงไม่ยอมทำมาตลอด"

# "I feel more active in class as well, delighting our science/homeroom teacher, Mr. Mutou, with correct and promptly delivered answers."
"รู้สึกจะตื่นตัวกับการเรียนด้วย ฉันคอยตอบคำถามมุโต้ที่เป็นครูประจำชั้นและครูวิชาวิทยาศาสตร์ได้อย่างถูกต้อง\nและรวดเร็วอย่างเป็นที่น่าพอใจ"

# "The break right now between the two morning classes is too short for any sort of meaningful activity, but too long to just spend it sitting in the classroom and doing nothing."
"ช่วงพักระหว่างสองคาบเช้าตอนนี้นั้นน้อยเกินกว่าจะทำอะไรเป็นชิ้นเป็นอัน แต่ก็นานเกินกว่าที่จะให้นั่งอยู่ในห้อง\nเฉย ๆ โดยไม่ทำอะไรเลย"

play ambient sfx_crowd_indoors fadein 0.5

scene bg school_hallway3
show crowd
with locationchange

# "Going out into the hallway isn't much better, but flexing my stiffened muscles is a better use of time than letting them get even stiffer by staying seated."
"จะให้ออกไปที่โถงทางเดินก็ไม่ได้ดีไปกว่ากันสักเท่าไหร่ แต่ได้เอาเวลามายืดเส้นยืดสายกล้ามเนื้อที่ตึง ๆ ก็ดีกว่า\nการนั่งอยู่เฉย ๆ ให้เส้นยึดกว่าเดิม"

# "The door of the neighboring classroom door opens and the students of 3-4 emerge to further fill up the already semi-crowded hallway. It seems their teacher kept them in for a few extra minutes."
"ประตูห้องเรียนที่อยู่ใกล้ ๆ เปิดออก นักเรียนห้อง 3-4 ไหลออกมาสมทบกับกลุ่มคนในโถงทางเดินที่ค่อนข้างแน่น\nอยู่แล้ว เหมือนว่าครูทางนั้นจะปล่อยช้าไปสองสามนาที"

# "Emi is among them. She notices me noticing her, which almost makes me look away on reflex."
"ในนั้นก็มีเอมิอยู่ด้วย เธอเห็นว่าฉันมองอยู่ ทำฉันเกือบจะเบือนหน้าหนีไปโดยอัตโนมัติ"

play music music_emi fadein 0.5

show emi basic_closedgrin at center
with charaenter

# "I don't, however, and Emi smiles at me as she happily skips towards me past the other students."
"แต่ฉันก็ไม่ได้เบือนหน้าหนี เธอยิ้มให้ฉันแล้วฝ่านักเรียนคนอื่น ๆ โดดมาทางฉันอย่างเริงร่า"

# "Emi looks pretty energetic, showing no sign of illness whatsoever. It seems she recovered from the cold."
"เอมิดูค่อนข้างกระฉับกระเฉง ไม่มีทีท่าอาการป่วยหรืออะไรเลย ดูท่าว่าจะหายหวัดแล้ว"

show emi basic_happy
with charachange

# emi "Hey! Good morning!"
emi "ไง! อรุณสวัสดิ์!"

# hi "Nice to see you back on your feet. Feeling better now?"
hi "กลับมาแล้วนี่นา แล้วนี่รู้สึกดีขึ้นหรือยัง"

# "She looks fine to me, but I still feel compelled to ask."
"ก็ดูไม่เป็นอะไรแล้วแหละ แต่ก็รู้สึกว่าต้องถามอยู่ดี"

show emi excited_laugh
with charachange

# emi "Thanks! And yeah, I do. It was just a cold, nothing serious."
emi "ขอบใจนะ! อื้ม ดีขึ้นแล้ว แค่หวัดเอง ไม่ได้เป็นอะไรมาก"

# "Emi laughs confidently, as if to emphasize her condition. I wonder for a moment what would count as serious in Emi's book."
"เธอหัวเราะด้วยความมั่นใจคล้ายเน้นย้ำสภาพร่างกายเธอ ฉันนึกสงสัยว่า ‘อะไรมาก’ ของเธอคืออะไรกันนะ"

# "She seems to be eager to put the topic aside, though."
"แต่ดูท่าแล้วถามไปเธอก็คงเลี่ยงไม่ตอบอะนะ"

show emi excited_happy
with charachange

# hi "Where are you going?"
hi "นี่เธอจะไปไหน"

show emi basic_closedgrin
with charachange

# emi "Off to Rin's room to see if she's awake yet."
emi "จะไปห้องรินดูว่าตื่นหรือยัง"

# hi "Oh? She skipped the morning class?"
hi "อ้าว นี่รินโดดคาบเช้าเหรอ"

show emi sad_grin
with charachange

# "A sheepish smile emerges on Emi's face and she gets slightly flustered."
"เธอยิ้มแหย ๆ เลิ่กลั่กเล็กน้อย"

# emi "Err… not exactly. It seems that she caught the cold that I had."
emi "เอ่อ… ไม่เชิงหรอก เหมือนจะติดหวัดไปจากฉันน่ะ"

# hi "Sorry to hear that. Well, she was out in the rain on Sunday with us, after all. I saw her on Monday and she was feeling a bit under the weather back then too."
hi "อ้าว จริงเหรอเนี่ย ก็นะ ไปตากฝนด้วยกันตอนวันอาทิตย์นี่นะ ตอนวันจันทร์ก็เห็นเหมือนจะไม่สบายอยู่หน่อย ๆ ด้วย"

show emi basic_grin
with charachange

# emi "Yeah. Anyway, I'll ask the nurse for some cold medication to give her if she doesn't get better soon."
emi "อื้ม นั่นแหละ เดี๋ยวถ้ายังไม่หายอีกก็จะไปขอยาแก้หวัดจากคุณพยาบาลไปให้ด้วย"

stop music fadeout 3.0

hide emi
with charaexit

# "She leaves for the girls' dorm. I want to go with her to wish Rin well. I want to tell her that I'm better now too, but it doesn't feel appropriate."
"เธอออกตัวไปที่หอหญิง ฉันอยากจะตามเอมิไปเยี่ยมรินด้วยเหมือนกัน อยากจะบอกรินว่าตอนนี้ฉันรู้สึกดีขึ้นแล้วด้วย\nแต่ก็รู้สึกเหมือนไม่ถูกที่ถูกทางอยู่"

# "An unspecified feeling diverts my thoughts away. Somehow I just can't summon the resolve to go in there. Is this what Iwanako went through when she tried to tell me what she felt?"
"ความรู้สึกบางอย่างที่ระบุไม่ได้เบนความคิดฉันไปทางอื่น ไม่รู้ทำไมถึงรวบรวมความกล้าเข้าไปไม่ได้ เนี่ยน่ะเหรอ\nความรู้สึกของอิวานาโกะที่พยายามบอกจะความรู้สึกเธอให้ฉันได้ฟังน่ะ"

stop ambient fadeout 2.0

scene black
with dissolve

#****************************

label th_R15:

scene bg school_girlsdormhall
with locationchange

# "Even though I'm feeling more energetic, I'm still hesitant about going over there to talk to Rin."
"ถึงฉันจะกระปรี้กระเปร่าขึ้นแล้ว แต่ก็ยังไม่แน่ใจว่าจะไปคุยกับรินดีมั้ย"

# "It's not until two days later, on Friday, that I finally gather enough courage to enter the girls' dorm. I ask the first person I meet inside for directions to Rin's room."
"จนกระทั่งสองวันให้หลังฉันถึงได้กล้าพอที่จะเข้าหอหญิง วันนี้วันศุกร์ ฉันถามคนแรกที่เจอตอนเดินเข้าหอว่าห้องริน\nไปทางไหน"
#Sunday - failed picnic. Monday - checkup. Two days later - start of R14, when he finds out on Wednesday that Rin is sick.
#He visits on Friday, so when he visits Rin has been sick for two days plus - or three plus if she started being sick on Tuesday, but the dialogue is neutral and without implications either way. -SC

play sound sfx_doorknock2

# "I knock on Rin's unmarked door and wait."
"ฉันเคาะประตูห้องรินที่ไม่มีอะไรแปะอยู่แล้วรอ"

$ renpy.music.set_volume(0.5, 0.0, channel="sound")
play sound sfx_rustling
$ renpy.music.set_volume(1.0, 10.0, channel="sound")

# "After a few seconds of silence I hear something rustling inside the room. I start wondering if maybe I should've brought something for her, like a can of warm coffee or some oranges. I could have peeled them for her. Well, too late now."
"หลังจากที่เงียบอยู่สองสามวินาทีก็มีเสียงกุกกักดังมาจากในห้อง เริ่มคิดแล้วว่าหรือควรจะเอาอะไรติดมือมาเยี่ยมด้วย\nอย่างกาแฟอุ่น ๆ สักกระป๋องหรือไม่ก็ส้มสักสองสามลูก จะได้ปอกให้กินด้วย แต่ก็ช้าไปละ"

# "The door opens soundlessly - it was already unlocked - and I find myself staring at Rin, who stares back at me."
"ประตูที่ไม่ได้ล็อกไว้นั้นเปิดออกเงียบ ๆ ฉันยืนจ้องรินที่กำลังจ้องฉันกลับอยู่"

# "She looks like she just got out of bed, with her hair all messed up."
"ผมเผ้าเธอรุงรังเหมือนเพิ่งตื่น"

show rinpan basic_deadpanamused at Slide(1.05,1.0,1.0,1.0,0.5)
with charaenter

# "…and barely any clothes on."
"…และตัวเธอแทบไม่ได้ใส่อะไรเลย"

"…"

show rinpan basic_amused at right
with charachange

# rin "Hellooooo."
rin "สวัสดี———"

play music music_rin fadein 0.5

# "There is a strange, stupid-looking smile on Rin's face. I'm not exactly sure why."
"รินยิ้มโง่ ๆ เพี้ยน ๆ แต่ก็ไม่แน่ใจว่าเพราะอะไร"

# "Rin smiles so rarely that it seems to be out of place every time. Especially so now, given her partially undressed state. Said state makes me feel extremely conflicted about whether or not this was a good idea."
"รินแทบไม่ได้ยิ้มจนยิ้มทีไรก็ชวนให้รู้สึกผิดที่ผิดทางตลอด ยิ่งตอนนี้ที่เธอใส่เสื้อผ้าไม่ครบชิ้นด้วย พอเห็นเธอใน\nสภาพนี้แล้วฉันก็เริ่มตีกับตัวเองว่าคิดถูกแล้วหรือยังที่มาหา"

# "Her cheeks are flushed rose-red, contrasting with the milky-pale complexion of a person who doesn't get enough sunlight. Her forehead looks sweaty, as though she might have a fever."
"แก้มเธอแดงแจ๋ตัดกับผิวขาวนวลอย่างคนไม่ได้ตากแดดให้เพียงพอ หน้าผากเธอเหงื่อซึมเหมือนมีไข้"

# hi "Um, hi."
hi "เอ่อ ไง"

show rinpan basic_absent
with charachange

# "Now what? I didn't plan anything further than this, and Rin is staring at me with those expectant eyes of hers again."
"แล้วไงต่อ ฉันไม่ได้คิดไว้ว่าจะเอายังไงต่ออีก ส่วนรินก็จ้องมาด้วยสายตาคาดหวังคู่นั้นของเธออีกแล้ว"

# "Something about this situation gives me very strange vibes. Her eyes are even more vacant than usual and she seems to have a hard time focusing them on anything."
"ไม่รู้ทำไมถึงได้รู้สึกแปลก ๆ ตาเธอดูว่างเปล่ากว่าปกติ แถมยังเหมือนแทบจะจดจ่อกับอะไรไม่ได้เลย"

# "The lack of clothing is disturbing, but since she herself doesn't seem to be bothered, why should I be?"
"พอเห็นเสื้อผ้าน้อยชิ้นอย่างนี้แล้วก็ใจคอไม่ดีเลย แต่ในเมื่อเธอดูจะไม่คิดอะไร แล้วฉันจะคิดอะไรทำไม"

# "I keep telling myself that."
"ก็บอกตัวเองอย่างนั้นอะนะ"

# hi "Err, I thought I'd pay you a visit since you haven't been at the art club… and I wanted to talk with you and wish you well."
hi "เอ่ออ พอดีเห็นไม่เข้าชมรมศิลปะเลยกะว่าจะมาเยี่ยมน่ะ… แล้วก็อยากมาคุยด้วย"

# "Rin doesn't show any sign of recognizing what I just said, making me wonder if she actually understood my words, or if she even heard them."
"ไม่มีทีท่าว่ารินจะได้ยินสิ่งที่ฉันเพิ่งพูดไปจนฉันสงสัยว่าเธอเข้าใจที่ฉันพูดหรือเปล่า หรือว่าไม่ได้ยินจริง ๆ"

# "Maybe it's the fever making her groggy; she might've actually been asleep before I came over."
"หรือจะยังเบลอ ๆ เพราะเป็นไข้ ก่อนหน้าที่ฉันจะมาหาอาจจะหลับอยู่"

show rinpan basic_deadpan
with charachange

# rin "Okay."
rin "โอเค"

show rinpan basic_deadpan:
    easeout 0.5 alpha 0.0 xpos 1.05
with Pause(0.5)

hide rinpan
with None

# "She turns on her heel and withdraws from the door, walking back inside the small room. From the doorway I can see her walk to her bed and half fall down, half sit down on the messy pile of bedsheets."
"เธอหมุนส้นเท้าแล้วเดินจากประตูกลับเข้าไปในห้องเล็ก ๆ นั้น ฉันยืนอยู่ตรงประตูมองเธอเดินไปที่เตียงทำท่า\nกึ่งนอนกึ่งนั่งอยู่บนกองผ้ารก ๆ อยู่บนที่นอน"

# "The open doorway seems to be more of an obstacle in my mind than the closed door was, but since Rin doesn't say anything else, I step through it, and into her room."
"ประตูที่เปิดดูเป็นอุปสรรคทางจิตใจมากกว่าประตูที่ปิดเสียอีก แต่ในเมื่อรินไม่พูดอะไรต่อ ฉันก็เดินผ่านประตูเข้าไป\nในห้องเธอ"

scene bg school_dormrin
with locationchange

# "Rin is on her bed leaning against the wall, leaving the only chair in the room for me."
"รินนั่งพิงผนังอยู่บนเตียง ในห้องมีเก้าอี้อยู่หนึ่งตัวที่ฉันนั่งได้"

# "She keeps quiet even after I sit down, so maybe she meant to invite me in but just forgot to say so aloud? An implied invitation, as it were."
"และพอฉันนั่งลงแล้วเธอก็ยังเงียบอยู่ กะจะให้เข้ามาในห้องแต่ลืมพูดออกมามั้ง งั้นก็คงเป็นคำชวนทางอ้อมแหละ"

show rinpan basic_deadpanamused at twoleft
with charaenter

# rin "Very exciting. Nobody has visited me before."
rin "ตื่นเต้นมาก ไม่เคยมีใครมาเยี่ยมฉันมาก่อนเลย"

# "The breaking of the silence draws my attention from the room to its inhabitant, who currently seems to be in the middle of a very profound thought process."
"เสียงที่ดังขึ้นมากลางความเงียบนี้ดึงความสนใจฉันจากห้องไปหาเจ้าของห้องที่เหมือนจะกำลังคิดอะไรลึกล้ำอยู่"

#Kinda dumb, I wanted to add some rinservice to appease SC but this kind of shit would probably require art. I'm not gonna go for "damn she doesn't have pants on" angle though.

#"I can't help taking closer note of the unusual shape of her body, exposed due to the incomplete state of her clothing."

#"Her thighs and legs are toned yet sleek like a cyclist's, a result of years of daily usage in ways the lower body is not really designed for, continuing up to the thin and bony upper body that the shirt covers."

#"Rin's body looks like it's shaped by function and her living habits, not by deliberate attempts to make it look a certain way."

show rinpan basic_awayabsent
with charachange

# rin "Actually that was not true. About visiting. But Emi doesn't count even if she visits."
rin "จริง ๆ ก็ไม่ใช่หรอก ที่ว่าไม่มีมาเยี่ยม แต่ต่อให้เอมิมาเยี่ยมก็ไม่นับนะ"

show rinpan basic_deadpan
with charachange

# rin "She always pampers me too much. I think she's having too much fun."
rin "เอมิเอาใจฉันเกินไป สนุกเธอละ"

show rinpan basic_absent
with charachange

# rin "I think I've forgot how to put a bra on by myself."
rin "ฉันว่าฉันลืมแล้วว่ายกทรงใส่ยังไง"

# "She looks groggily down at her chest."
"เธอก้มมองหน้าอกตัวเองเนือย ๆ"

show rinpan basic_surprised
with charachange

# rin "Which is probably why I don't have one on, now that I think about it."
rin "ซึ่งก็น่าจะเป็นเหตุผลว่าทำไมฉันถึงไม่ได้ใส่ จะว่าไปแล้ว"

# "I haven't failed to notice that Rin doesn't have her shirt buttoned up either, but I try to keep my eyes strictly locked on hers."
"ก็เห็นอยู่เหมือนกันแหละว่าไม่ได้ติดกระดุมเสื้อ แต่ฉันก็คอยใช้สายตาจ้องตรงเข้ากับตาเธออย่างเดียว"

# "It's rather evident that she's not a very body-conscious person. My own body, however, is quite conscious of hers right now."
"ค่อนข้างชัดว่าเธอไม่ใช่พวกที่รู้สึกรู้สาอะไรกับสภาพตัวเองเท่าไหร่ แต่ตัวฉันตอนนี้นั้นรู้สึกรู้สากับสภาพเธอไปแล้ว\nพอตัว"

show rinpan relaxed_sleepy
with charachange

# rin "She came to wake me up at half past seven today!"
rin "วันนี้เอมิมาปลุกฉันตอนเจ็ดโมงครึ่งด้วยแหละ!"

show rinpan relaxed_doubt
with charachange

# rin "Can you imagine that?"
rin "นึกภาพไม่ออกเลยเนอะ"

# "She pauses for a while and glances up at my dumbfounded face."
"เธอชะงักไปครู่หนึ่งแล้วมองหน้าฉันที่อึ้ง ๆ อยู่"

show rinpan basic_lucid
with charachange

# rin "On second thought, you probably can. It's not like that reverse rainbow fish I tried to imagine earlier. That was hard."
rin "คิดดูอีกที นายคงนึกภาพได้แหละ ไม่เหมือนปลาสายรุ้งกลับด้านที่เมื่อกี้ฉันกำลังพยายามนึกภาพอยู่ ยากมาก"

# hi "Well yes, that seems like a pretty normal time to wake up if you want to go to class in the morning."
hi "ก็ได้แหละ ถ้าจะไปเรียนคาบเช้าปกติก็ต้องตื่นเวลานั้นนี่"

# "I'm trying to sound as reasonable as possible to counteract Rin's unreasonable annoyance."
"ฉันตอบให้ฟังดูมีเหตุผลที่สุดเท่าที่เป็นไปได้เพื่อที่จะต้านเรื่องหงุดหงิดที่ไร้เหตุผลของริน"

show rinpan basic_deadpanupset
with charachange

# rin "Told her to sod off."
rin "ฉันบอกให้เอมิออกไป"

show rinpan relaxed_nonchalant
with charachange

# rin "She gave me these meds and told me to take them."
rin "เธอให้ยาพวกนี้มาแล้วก็บอกให้กิน"

# "I follow her eyes to the night table and then to the pill bottle sitting on top of it."
"ฉันมองตามสายตาเธอไปยังโต๊ะหัวเตียงจนเจอเข้ากับขวดยาที่ตั้งอยู่"

show pills:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

# "I pick it up and turn it around to look at the label so I can see what kind of medication Emi brought."
"ฉันหยิบขวดนั้นมาอ่านฉลากยาดูว่าเอมิเอาอะไรมาให้รินกิน"

# "Active ingredient… codeine?"
"ตัวยาสำคัญ… โคดีอีน?"

show pills:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide pills
with None

# hi "You took all of these?"
hi "เธอกินหมดนี่เลย?"

show rinpan relaxed_surprised
with charachange

# rin "No. Yes. I've been eating some since there's so many of them. Seem to make this thing not so bad."
rin "ไม่ ใช่ ฉันกินไปบ้างแล้วเพราะยามีเยอะมาก เหมือนจะช่วยให้รู้สึกดีได้"

show rinpan relaxed_sleepy
with charachange

# rin "Actually… I think I'm feeling just fine."
rin "ที่จริง… ฉันว่ารู้สึกดีมากเลยละ"

# "Her head lolls round and round, making it look like she is either trying to stretch her neck muscles or possibly pass out."
"เธอหมุนคอไปมาเหมือนกำลังยืดเส้น หรือไม่ก็เหมือนว่ากำลังจะเป็นลม"

# "She took several of these pills? Can that be safe? At least it's bound to have some side effects… which I'm afraid I am witnessing right now."
"นี่กินไปหลายเม็ดแล้วเหรอ จะเป็นอะไรมั้ยเนี่ย อย่างน้อยน่าจะมีผลข้างเคียงบ้าง… ซึ่งเกรงว่าผลที่ว่าก็คือสิ่งที่ตาฉัน\nเห็นอยู่ตอนนี้"

show rinpan basic_deadpanupset
with charachange

# rin "I am feeling just fine… I am fine… just someone take this buzzing away from my head. I can't think straight."
rin "ฉันรู้สึกดีมาก… รู้สึกดี… แค่ใครเอาอะไรที่ส่งเสียงดังอยู่ในหัวนี้ออกไปที คิดอะไรไม่ออกเลย"

# "The annoyed expression returns to Rin's face."
"เธอทำหน้าหงุดหงิดอีกครั้ง"

show rinpan basic_upset
with charachange

# rin "It's like many of those insect things… or one really big insect thing."
rin "เหมือนมีแมลงพวกนั้นอยู่เยอะ ๆ … หรือมีแมลงพวกนั้นอยู่กลุ่มใหญ่มาก"

show rinpan basic_awayabsent
with charachange

# rin "With lots of wings. Very much color and everything."
rin "มีปีกหลายคู่ มีหลากสี แล้วก็อะไรหลายอย่าง"

show rinpan basic_absent
with charachange

# rin "What's the word for those?"
rin "เรียกว่าอะไรนะ"

show rinpan basic_deadpanamused
with charachange

# rin "Oh, never mind. I remembered. It's butterflies."
rin "อ้อ ช่างเถอะ นึกออกละ ผีเสื้อ"

# "She smiles slightly at her last observation. The small pause in her monologue is not long enough for me to dare saying something that could potentially, but not likely, salvage this discussion."
"เธอยิ้มน้อย ๆ กับข้อสังเกตนั้นของเธอ ช่วงว่างสั้น ๆ ระหว่างที่เธอกำลังคุยกับตัวเองนั้นสั้นเกินกว่าที่ฉันกล้าจะพูด\nอะไรที่พอจะประคับประคองบทสนทนานี้ขึ้นมาได้"

show rinpan basic_amused
with charachange

# rin "I love butterflies. They are the best animal."
rin "ฉันรักผีเสื้อ เป็นสัตว์ที่สุดยอดที่สุดเลย"

show rinpan basic_awayabsent
with charachange

# rin "Did you see any on your way here?"
rin "ตอนนายมานายเห็นมั้ย"

show rinpan basic_deadpansurprised
with charachange

# rin "Hisao."
rin "ฮิซาโอะ"

# "She utters my name as an afterthought, possibly to make clear that she is now addressing me instead of just speaking her mind to whoever might be listening."
"เธอพูดชื่อฉันปิดท้าย น่าจะเป็นการบอกให้ชัดว่าตอนนี้คุยกับฉันอยู่ ไม่ได้เป็นการพูดสิ่งที่เธอคิดให้ใครก็ตาม\nที่อาจจะฟังอยู่"

# "This odd situation has left me speechless more or less since the moment Rin first opened her mouth. Now that she herself doesn't seem to have anything else to add, silence fills the small room."
"สถานการณ์พิลึกพิลั่นนี้นับตั้งแต่ที่รินเปิดปากพูดทำฉันใบ้กิน และเมื่อเธอไม่มีอะไรจะพูดต่อแล้วก็มีเพียงความเงียบ\nที่เติมเต็มห้องห้องนี้"

# "It makes me glance around again in an attempt to find something to talk about."
"ฉันจึงมองไปรอบ ๆ อีกครั้งพลางนึกหาเรื่องคุย"

# "Rin's room is about as small as mine. The big window, which takes up most of the wall furthest from the door, opens to the east just like mine."
"ห้องรินนั้นแคบพอ ๆ กับห้องฉัน หน้าต่างบานใหญ่ที่หันหน้าไปทางทิศตะวันออกเหมือนอย่างเดียวกับที่ห้องฉันกินที่\nอยู่ตรงผนังฝั่งตรงข้ามประตู"

# "It looks very normal, which strikes me as strange. I expected something more… different."
"ดูปกติมากจนฉันรู้สึกผิดปกติ ก็นึกว่าจะมีอะไรที่มัน… ต่างไปกว่านี้"

# "About a dozen paintings - most of them in Rin's signature abstract style - and a few art posters are taking up almost all of the available wall space, but that's about the only real difference between her room and mine."
"พื้นที่ผนังส่วนใหญ่เป็นภาพวาดแนวนามธรรมอันเป็นเอกลักษณ์เฉพาะตัวของรินที่มีอยู่สิบกว่าภาพ ทั้งยังมีโปสเตอร์ศิลปะ\nแปะอยู่สองสามใบ แต่ก็มีแค่จุดนี้แหละที่ไม่เหมือนห้องฉันแบบจริง ๆ"

# "The room is not exactly ascetic, but it doesn't look like what I'd expected from a girl's room, either."
"ห้องก็ไม่ได้เรียบจนจืดขนาดนั้น แต่ก็ดูไม่เหมือนสภาพของห้องสาวน้อยที่ฉันคิดไว้ในหัวเท่าไหร่"

# "A faint smell of art… of paint and paper is floating in the air. It's the same smell the art room has."
"กลิ่นศิลปะจาง ๆ … กลิ่นสีและกระดาษลอยอยู่ในอากาศ กลิ่นเหมือนเดียวกันอย่างกับกลิ่นที่ห้องศิลปะ"

# "Rin isn't too concerned about being tidy, it seems; everything she owns seems to be arranged in various piles around her room."
"และดูเหมือนว่ารินจะไม่ได้ใส่ใจเรื่องความเป็นระเบียบมากนัก ในห้องเธอมีของอะไรวางกอง ๆ รวมกันไปทั่ว"

# hi "Your room looks nice."
hi "ห้องสวยดีนะ"

# "It's an empty sentence one uses to fill empty spaces in conversations, but my wits are failing me pretty hard right now."
"เป็นประโยคลอย ๆ ที่คั่นช่วงว่างในบทสนทนา แต่ตอนนี้สมงสมองก็ไม่อยู่กับเนื้อกับตัวฉันแล้ว"

show rinpan relaxed_nonchalant
with charachange

# rin "Yeah. Would you like me to show you the places?"
rin "อาฮะ อยากให้พาไปดูมั้ย"

# "She looks down at her half-open shirt quizzically, making me inadvertently follow her gaze to her chest."
"เธอก้มมองเสื้อที่แบะออกนั้นงง ๆ จนฉันเผลอมองลงต่ำตามไปด้วย"

show rinpan relaxed_sleepy
with charachange

# rin "Oh… I guess I already did."
rin "อ้าว… น่าจะพาไปดูแล้ว"

# "I can't deny that, no matter how hard I tried to act properly."
"ปฏิเสธไม่ได้แม้ฉันจะฝืนทำตัวปกติแค่ไหนก็ตาม"

show rinpan basic_absent
with charachange

# rin "It is very nice that you came to see me."
rin "ดีจังนะที่นายมาเยี่ยม"

show rinpan basic_deadpancontemplation
with charachange

# rin "It makes me feel very… what's that word… you know, the one about things and stuff."
rin "ฉันละ… เรียกว่าอะไรนะ… คำนั้น ที่ใช้กับอะไร ๆ นั่นน่ะ"

show rinpan basic_lucid
with charachange

# rin "Anyway, you came."
rin "เอาเถอะ นายมาจนได้"

# "Rin's rambling makes me remember that I actually came here for a reason."
"พอรินพล่ามแล้วฉันก็นึกได้ว่าที่มาหาเพราะมีเรื่องจะคุย"

# hi "Hey, about what we talked on Monday. On the rooftop, remember?"
hi "นี่ ที่คุยกันเมื่อวันจันทร์บนดาดฟ้านั่นน่ะ จำได้มั้ย"

stop music fadeout 4.0

show rinpan relaxed_surprised
with charachange

# rin "Hmmm?"
rin "หืมมม"

# "Rin doesn't seem to be exactly attentive right now, not that she ever is. I plow ahead and get it off my chest anyway."
"รินดูไม่ค่อยสนใจเท่าไหร่ แต่ก็ใช่ว่าจะเคยสนใจอยู่แล้ว ฉันดันทุรังพูดออกไปอยู่ดี"

# hi "I just wanted to tell you that I'm going to be better from now on, I guess."
hi "ฉันแค่อยากบอกเธอว่าจากนี้ไปฉันจะทำตัวให้ดีขึ้นแล้วนะ ประมาณนั้น"

# hi "I hate being pathetic, so I decided that I'm not going to be, any more."
hi "ฉันไม่อยากเป็นพวกน่าสมเพช ก็เลยว่าจะไม่เป็น อีกต่อไป"

# hi "I guess… that's all."
hi "ก็คง… แค่นั้นแหละ"

show rinpan relaxed_sleepy
with charachange

# rin "Okay. Isn't that good?"
rin "โอเค ก็ดีแล้วนี่"

# "The blurry words flow out of her lips slowly and uncontrollably."
"คำพูดที่ไม่ค่อยชัดเจนนั้นออกมาจากปากเธอช้า ๆ อย่างไม่อาจควบคุม"

show rinpan relaxed_nonchalant
with charachange

# rin "I'm happy for you I think. That's what I think."
rin "คิดว่าฉันก็ยินดีด้วยนะ นั่นแหละที่ฉันคิด"

show rinpan basic_deadpannormal
with charachange

# rin "You shouldn't look so sad all the time. I mean, looking sad is fine if you are not sad, but you look sad like you actually sad."
rin "นายอย่าเอาแต่ทำหน้าดูเศร้าตลอดเลย คือ ทำหน้าดูเศร้าตอนไม่เศร้าก็ไม่เป็นไรหรอก แต่นายทำหน้าดูเศร้าเหมือน\nนายเศร้าจริง ๆ"

show rinpan basic_deadpan
with charachange

# rin "That's no good."
rin "ไม่ดีนะ"

show rinpan basic_awayabsent
with charachange

play music music_rin fadein 0.5

# rin "Are you going on some training camp where they make men out of boys? Or mountaintop meditation?"
rin "แล้วนายจะไปเข้าค่ายสร้างลูกผู้ชายอะไรงี้เหรอ หรือจะไปนั่งสมาธิอยู่บนยอดเขา"

# hi "No, I don't think so."
hi "ไม่ ไม่น่าหรอก"

show rinpan basic_absent
with charachange

# rin "Oh. I guess that's fine too."
rin "อ้อ ก็น่าจะได้เหมือนกันมั้ง"

# "The sentences come out of her mouth, and probably her brain, one at a time with a small pause between each, making her gibberish hard to understand."
"ประโยคเหล่านั้นออกมาจากปากเธอ และน่าจะจากสมอง ออกมาทีละนิดละหน่อยมีการเว้นช่วงจนสับสนแทบฟัง\nไม่รู้เรื่อง"

show rinpan relaxed_doubt
with charachange

# rin "I just think it seemed like a good idea. Maybe it's not."
rin "แค่คิดว่าน่าจะเป็นความคิดที่ดีน่ะ แต่คงไม่"

# "Rin finishes with one more line, getting to say the last word over herself, an impressive display of what I can only describe as mental shadowboxing."
"รินพูดต่ออีกประโยคปิดท้ายฝั่งของเธอ คงจะเรียกได้ว่าเป็นการชกลมทางจิตที่น่าทึ่งจริง ๆ"

# hi "While I'm embarrassing myself, might as well tell you that I'm sorry that I said some stupid things to you last week."
hi "ไหน ๆ ก็พูดอะไรน่าอายแล้ว ขอโทษไปด้วยเลยแล้วกันที่สัปดาห์ที่แล้วพูดอะไรโง่ ๆ ไปอย่างนั้นน่ะ"

# hi "It's your own business to decide what you're going to do."
hi "เธอจะทำอะไรมันก็เรื่องของเธอนี่นะ"

show rinpan basic_absent
with charachange

# "She seems to not register my words first, but then understanding lights in her eyes and she waves her head around in a way that could be interpreted as anything."
"ทีแรกเธอเหมือนจะยังไม่รับรู้สิ่งที่ฉันพูดไป แต่แล้วตาเธอก็ฉายแววว่าเข้าใจขึ้นมา เธอโยกหัวไปมาแบบที่ดูแล้ว\nจะตีความเป็นความหมายว่าอะไรก็ได้ทั้งนั้น"

show rinpan basic_deadpancontemplation
with charachange

# rin "It's OK."
rin "ไม่เป็นไร"

show rinpan basic_lucid
with charachange

# rin "I probably said stupid things too."
rin "ฉันก็น่าจะพูดอะไรโง่ ๆ เหมือนกัน"

# rin "It's just sometimes a bit hard to keep my thoughts the way I like them."
rin "แค่ว่าบางทีความคิดมันไม่ค่อยได้ดั่งใจเท่าไหร่"

show rinpan relaxed_nonchalant
with charachange

# rin "They are not very straight, at least most of the time."
rin "อย่างน้อยก็หลายครั้งอะนะที่ไม่ค่อยชัดเจน"

# rin "Not that I want to have them straight… I just wish they were at least in some shape."
rin "ก็ไม่ใช่ว่าอยากให้ชัดมากมายหรอก… อยากให้อย่างน้อยก็เป็นรูปเป็นร่างบ้าง"

# rin "Round is fine too. But I need more definition."
rin "วงกลมก็ได้ แต่ก็อยากให้ชัดกว่านั้นอีก"

show rinpan relaxed_boredom
with charachange

# rin "My thoughts are very messy."
rin "ความคิดฉันมันยุ่งเหยิงมาก"

show rinpan relaxed_sleepy
with charachange

# rin "Messy."
rin "ยุ่งเหยิง"

show rinpan invis:
    ypos 1.1
with dissolvecharamove

play sound sfx_pillow

scene ev rin_high_frown
with locationchange

#show rinpan basic_lucid at Position(ypos=1.1)
#with dissolvecharamove

# "She repeats the word melancholically, then flops lying down on her bed and nuzzles her head against her pillow, shutting her eyes."
"เธอย้ำคำนั้นดูหม่น ๆ จากนั้นก็ล้มตัวลงนอนกับเตียงแล้วเอาหัวยี ๆ กับหมอนและหลับตา"

# rin "Enough. Tired. You should go. I'm going to sleep again."
rin "พอ เหนื่อย นายไปเถอะ ฉันจะนอนอีก"

scene ev rin_high_oneeye
with locationchange

# "She opens one of her eyes to look at me."
"เธอลืมตาข้างหนึ่งมองฉัน"

#show rinpan basic_awayabsent
#with charachange

# rin "Was it you who likes to look at sleeping girls? Or someone else?"
rin "นายใช่มั้ยนะที่ชอบมองสาวนอนหลับ หรือคนอื่น"

# rin "Maybe there were many of those."
rin "หรือมีหลายคน"

scene ev rin_high_frown
with locationchange

# rin "I can't remember."
rin "จำไม่ได้"

#show rinpan basic_absent
#with charachange

# rin "You can stay if you want."
rin "ถ้าอยากอยู่ต่อก็อยู่ได้นะ"

# hi "No no, I'll leave. I have to… do homework anyway."
hi "ไม่ ๆ จะไปละ เดี๋ยวต้องไป… ทำการบ้าน"

stop music fadeout 2.0

#hide rinpan
#with charaexit

scene bg school_dormrin
with locationchange

# "I stand up from the chair and take a step towards the door."
"ฉันลุกขึ้นยืนแล้วเดินไปทางประตู"

# rin "Wait."
rin "ช้าก่อน"

# "Her request stops me in my tracks, not that I intended to scoot off right away."
"เสียงเรียกจากเธอรั้งตัวฉันไว้ แต่ก็ไม่ได้กะจะเดินออกไปดื้อ ๆ อยู่แล้วอะนะ"

scene ev rin_high_grin
with locationchange

#show rinpan basic_deadpandelight:
#    twoleft
#    ypos 1.1
#with charaenter

# "I look over my shoulder at the girl lying on her bed, again with the strangest kind of smile on her features."
"ฉันเอี้ยวคอหันมองสาวที่นอนอยู่บนเตียงที่กำลังยิ้มอยู่อย่างประหลาด"

# "She should smile more often."
"น่าจะยิ้มบ่อย ๆ นะ"

# rin "I can walk you to the door."
rin "เดี๋ยวพาไปส่งที่ประตู"

scene ev rin_high_grinwide
with locationchange

#show rinpan basic_delight
#with charachange

# rin "It's the least a gentleman can do."
rin "เป็นมารยาทสุภาพบุรุษนี่นะ"

#show rinpan basic_amused
#with charachange

scene ev rin_high_smile
with locationchange

# "Rin giggles like a little kid, making me beyond absolutely certain that she took far too much of her cold medication today."
"รินหัวเราะคิกคักเหมือนเด็กน้อยจนฉันมั่นใจเกินร้อยว่าวันนี้เธอกินยาแก้หวัดเยอะเกินไปแล้วจริง ๆ"

# rin "I have always wanted to say that."
rin "อยากพูดมาตั้งนานแล้ว"

scene bg school_dormrin
with locationchange

show rinpan invis:
    twoleft
    ypos 1.1
with None

show rinpan basic_deadpandelight at twoleft
with dissolvecharamove

# "Slowly and with difficulty, Rin first rises to a sitting position again, then she stands up with even more difficulty and more slowly still."
"เธอลุกขึ้นนั่งอย่างช้า ๆ ด้วยความทุลักทุเล จากนั้นก็ยืนขึ้นอย่างช้ากว่าเก่าด้วยความทุลักทุเลกว่าเก่า"

# "As if guided by some masculine automation, my eyes instantly lower to the curve of her thighs and the striped panties, at which point my manners force me to lift my gaze back to Rin's eye level."
"สายตาฉันเลื่อนต่ำลงไปที่ต้นขาและกางเกงในลายทางของเธอราวถูกสัญชาตญาณความเป็นชายนำพา ซึ่งมารยาท\nก็ดึงตาฉันให้กลับขึ้นมาสบตากับริน"

# "It's getting almost too hard to do that."
"ชักจะห้ามใจไม่มองไม่ไหวแล้ว"

# "Rin is standing, although barely. It looks like she has trouble keeping her usually decent balance; again, probably a side effect of the medicine."
"รินยืนโงนเงน ดูท่าว่าจะทรงตัวให้ดีเหมือนทุกทีไม่ได้ ซึ่งก็น่าจะเพราะผลข้างเคียงจากยาอีกนั่นแหละ"

show rinpan basic_deadpandelight:
    ease 1.0 center
with None

show rinpan basic_deadpandelight_close:
    twoleft
    ease 1.0 center
with Dissolve(1.0)

# "She takes an unsteady step towards me, then another smaller one as she notices that it's not a good idea to try to take big steps."
"เธอเดินเซมาหาแล้วปรับก้าวเดินให้สั้นลงเมื่อเห็นว่าก้าวยาวไปคงไม่ดี"

# "I feel my muscles tense as I prepare to catch Rin if she falls down."
"ฉันเกร็งตัวเผื่อรอรับรินตอนล้ม"

play music music_twinkle fadein 3.0

scene ev rin_kiss:
    center
    yalign 0.0 zoom 4.0 subpixel True
    easein 0.4 zoom 1.05
    easein 5.0 zoom 1.0
with flash

# "She manages to take two more steps before she falls against me. To my surprise, neither her downwards momentum nor our slight height difference are able to stop Rin from pressing her heart-shaped lips squarely against mine."
"เธอก้าวมาได้อีกสองก้าวก่อนจะล้มใส่ฉัน ริมฝีปากรูปประจับของเธอประทับเข้ากับริมฝีปากฉันอย่างจัง ฉันนึกแปลกใจ\nเพราะเราสองคนตัวสูงไม่เท่ากัน แถมตอนล้มก็เอนมาเหมือนจะคว่ำหน้าอีกต่างหาก"

# "As our lips part after a confusing moment of nothing but the taste of… Rin, I look down at her, trying to find some explanation for this bewildering event."
"ริมฝีปากของเราผละจากกันหลังจากช่วงเวลานั้นที่ฉันได้ลิ้มรส… ริน ฉันก้มมองเธอพลางนึกหาสาเหตุว่าเหตุการณ์\nที่ชวนให้งงงวยนี้เกิดขึ้นได้อย่างไร"

$ renpy.music.set_volume(0.7, 2.0, channel="music")

scene bg school_dormrin
show rinpan basic_deadpandelight_close at center
with locationchange

# "The euphoric smile of a madman broadens on Rin's lips again and—"
"รินยิ้มอิ่มเอิบเหมือนคนบ้าอีกครั้งและ—"

show rinpan relaxed_sleepy_close
with charachange

# rin "I wonder if I will remember this tomorrow."
rin "พรุ่งนี้ฉันจะยังจำได้มั้ยนะ"

# "I am absolutely stumped on how to respond."
"ฉันจนปัญญาไม่รู้จะตอบอย่างไร"

show rinpan relaxed_sleepy_close:
    ease 1.0 twoleft
with None

show rinpan relaxed_sleepy:
    center
    ease 1.0 twoleft
with Dissolve(1.0)

# "Rin takes a step backwards, separating her body from mine, and making me only now realize that they were even connected in the first place."
"รินถอยไปหนึ่งก้าวผละออกจากตัวฉัน จนตอนนั้นฉันก็เพิ่งรู้ตัวว่าเมื้อกี้ตัวแนบกันอยู่"

show rinpan invis:
    ypos 1.1
with dissolvecharamove

play sound sfx_pillow

# "The second step is actually a fall backwards, luckily straight onto her bed."
"พอถอยไปได้อีกก้าวเธอก็ล้มหงายหลัง โชคดีที่มีเตียงรองรับไว้"

# "The soft thud Rin's thin body makes against the mattress breaks the silence."
"เสียงรินล้มตัวลงกับที่นอนดังปุนั้นดังขึ้นทำลายความเงียบ"

scene ev rin_high_open
with locationchange

# "I move quickly over to her to see if she hurt herself, only to be met with the peaceful face of dreaming."
"ฉันรีบไปดูว่าเธอเจ็บตรงไหนหรือเปล่า แต่ก็พบเพียงใบหน้าเคลิบเคลิ้มแสนสงบ"

# "Rin sleeps."
"หลับอยู่"

# "She is lying diagonally across the bed, somehow managing to have simultaneously fallen asleep while standing up, and fallen down in a way that she didn't injure herself."
"ตัวเธอนอนพาดกับเตียง อยู่ ๆ เธอก็หลับทั้งยืนแล้วล้มลงนอนได้โดยไม่บาดเจ็บอะไร"

# "Fool's luck."
"ดวงดีจริงเลย"

scene ev rin_high_sleep
with locationchange

# "I tuck Rin in, covering her with the sheets as well as I can."
"ฉันห่มผ้าให้รินอย่างดี"

# "She feels very light, even though I am not that strong."
"ตัวเธอนั้นเบาหวิว ขนาดว่าฉันไม่ได้มีแรงเยอะมากมายเลย"

show ev rin_high_sleep:
   subpixel True xalign 1.0 yalign 0.0
   ease 10.0 zoom 1.1
with None

# "I stand up to look at her, the oval-shaped face, the dark eyelashes shut against the feverish cheeks, the slender body covered with the pale sheets."
"ฉันยืนมองหน้ากลมรีของเธอ แพขนตาสีดำเรียงอยู่บนแก้มที่แดงด้วยฤทธิ์ไข้ ร่างบางนั้นมีผ้าสีจางคลุม"

# "Rin sleeps."
"หลับอยู่"

# "A conflict - no. Conflicts, plural, churn inside of me. I think about calling a nurse to keep an eye on her, but decide against it. After taking one more glance at her peaceful face, I decide that she'll be fine."
"ในใจสับสน ไม่สิ เกินกว่าคำว่าสับสนอีก ฉันคิดจะโทร. หาพยาบาลให้คอยดูแลเธอแต่ก็ล้มเลิกแผนนั้นไป พอมองหน้าเธอ\nที่หลับสบายอีกครั้งแล้วก็คิดได้ว่าเดี๋ยวก็คงหาย"

# "I do pocket the remaining pills, though."
"แต่ฉันก็ริบยาที่เหลืออยู่มาด้วย"

stop music fadeout 5.0

scene bg school_girlsdormhall
with locationchange

# "I exit the room, and close the door soundlessly behind me."
"ฉันออกจากห้องมาแล้วปิดประตูเงียบ ๆ"

# "I exhale deeply, only now realizing I had held my breath for the better part of a minute. Taking a moment to relax, I try to calm down my heart, racing like a jackrabbit."
"ฉันถอนหายใจยาว และเพิ่งรู้ตัวว่าเมื่อกี้กลั้นหายใจอยู่ค่อนนาที ฉันปล่อยตัวให้สบายคอยหัวใจที่เต้นรัวเป็นกลองนี้\nให้เต้นช้าลง"

$ suppress_window_after_timeskip = True

scene black
with dissolve


#*******************************

label th_R16:

window hide None

scene black
with dissolve

play music music_pearly fadein 1.0

scene bg school_dormhisao
with openeye

window show

# "I had trouble getting to sleep that night, so the next morning finds me exceptionally groggy. I briefly consider skipping class but remind myself that I was supposed to be a stronger person now."
"เมื่อคืนนอนไม่ค่อยหลับ เช้านี้จึงตื่นมาพร้อมอาการครั่นตัวเป็นพิเศษ แวบหนึ่งฉันคิดจะโดดเรียน แต่ก็บอกกับตัวเอง\nว่าตอนนี้ฉันต้องทำตัวให้เข้มแข็งขึ้นได้แล้ว"

scene bg school_courtyard
with locationskip

# "I get up like a good boy and put on my uniform, then make my way to the main school building without eating breakfast."
"ฉันลุกขึ้นมาจากเตียงอย่างว่าง่ายมาใส่ชุดนักเรียนแล้วเดินไปยังอาคารหลักโดยไม่กินข้าวเช้าเลย"

scene bg school_scienceroom
with locationskip

# "I sit in my seat in classroom 3-3, waving a greeting to Misha and Shizune like I do every morning, and let the day wash over me."
"ฉันนั่งลงกับที่ในห้อง 3-3 พลางโบกมือทักทายมิช่าและชิซูเนะเช่นทุกเช้า ปล่อยให้เวลาวันนี้ไหลผ่านฉันไป"

with shorttimeskip

# "The afternoon classes are always longer than those in the morning. This is true regardless of whether I count it by the minute or by the number of doodles drawn in my notebooks."
"คาบบ่ายนั้นนานกว่าคาบเช้าเสมอ ไม่ว่าจะวัดด้วยการนับนาทีหรือนับจำนวนรูปวาดในสมุดฉันก็ยังจริง"

# "Today I'm especially distracted, as I keep thinking about Rin."
"วันนี้เหม่อลอยเป็นพิเศษเพราะเอาแต่คิดถึงริน"

$ renpy.music.set_volume(0.5, 0.5, channel="music")

window hide
nvl clear
nvl show dissolve

# n "\n\n\n\n\nDid I manage to properly tell her that I want to get better? Did she understand a word of what I was saying?"
n "\n\n\n\n\nฉันได้บอกเธอไปแล้วจริง ๆ หรือยังว่าฉันอยากปรับปรุงตัว เธอเข้าใจสิ่งที่ฉันพูดไปบ้างหรือเปล่า"

# n "I think about the kiss we shared and what it means. She was so out of her mind, maybe it means nothing. But we've been getting closer lately. What does that mean?"
n "ฉันนึกถึงจูบนั้นพลางคิดว่าสิ่งนั้นหมายความว่าอะไร สติสตังเธอไม่อยู่กับเนื้อกับตัว ก็คงไม่ได้มีความหมายอะไร แต่\nช่วงนี้เราก็สนิทกันมากขึ้นแล้ว หมายความว่าอะไร"

# n "\n\n\nI think about Rin more and more nowadays. I wonder if she thinks about me."
n "\n\n\nช่วงนี้ใจฉันคิดถึงรินมากขึ้นเรื่อย ๆ เธอจะคิดถึงฉันบ้างหรือเปล่า"

$ renpy.music.set_volume(1.0, 4.0, channel="music")
play sound sfx_normalbell
nvl clear
nvl hide dissolve
window show

# "The ringing of bells makes me flinch, and then realize that I haven't been paying attention during the latter half of class at all."
"ระฆังดังทำฉันสะดุ้งโหยง แล้วฉันก็เพิ่งรู้ตัวว่าเมื่อกี้ไม่ได้ฟังที่ครูสอนมาตลอดครึ่งหลังของคาบนี้เลย"

# "I look at the assortment of sketches traveling up and down the margins of my notebook, the only thing I got done in the last hour."
"ฉันมองรูปวาดทั้งหลายแหล่ที่เป็นอย่างเดียวที่ฉันได้ทำตลอดชั่วโมงที่ผ่านมาที่อยู่เต็มขอบสมุดฉัน"

# "Feeling vaguely disappointed in myself, I pack up and get to the hallway."
"ฉันเก็บข้าวของแล้วเดินออกมาที่โถงทางเดินด้วยความรู้สึกผิดหวังในตัวเองเล็กน้อย"

stop sound fadeout 0.5
$ renpy.music.set_volume(0.0, 1.0, channel="music")
scene bg school_hallway3
show rin basic_absent at center
with locationchange

# "Rin is standing right outside the door, her presence stopping me in my tracks as soon as I spot her."
"รินยืนอยู่หน้าประตู ทันทีที่เห็นเธอฉันก็หยุดเท้าไว้ทันที"

# "Her posture is relaxed as always, but I suddenly feel like I just ate a crowbar. I'm having a hard time meeting her gaze."
"ท่าทีเธอผ่อนคลายอย่างเช่นเคย แต่อยู่ ๆ ก็รู้สึกเหมือนเพิ่งกินชะแลงมา ฉันไม่กล้าสบตาเธอเลย"

# "She doesn't seem to have any trouble looking at me, but those dark eyes are making me feel flustered for no reason."
"เธอมองฉันได้ไม่มีปัญหาอะไร แต่ตาดำคู่นั้นทำให้ฉันว้าวุ่นใจแปลก ๆ"

# "It's hard to look straight at her so I turn my face away a little."
"ฉันไม่กล้าสบตาเธอตรง ๆ จึงเบือนหน้าตัวเองหนีไปเล็กน้อย"

# "I don't know what one should say in this kind of situation."
"ฉันไม่รู้ว่าพอเป็นอย่างนี้แล้วจะต้องพูดยังไง"

# "Then again, I rarely know what to say to Rin in any given situation."
"แต่ก็นะ จะเป็นยังไงฉันก็แทบไม่รู้ว่าจะพูดยังไงกับรินอยู่ดี"

$ renpy.music.set_volume(1.0, 8.0, channel="music")

# hi "Err… hi."
hi "เอ่อ… ไง"

show rin basic_deadpan
with charachange

# rin "Hello."
rin "สวัสดี"

# "I try to get rid of the awkwardness in my voice and invoke a more natural way of speaking. I suddenly worry about where I should put my hands; it feels like they're in the way somehow."
"ฉันปั้นน้ำเสียงให้ดูไม่มีความเกร็งใด ๆ แล้วพูดให้เป็นธรรมชาติมากขึ้น อยู่ ๆ ก็ไม่รู้ว่าจะเอามือไปไว้ที่ไหน รู้สึกเกะกะ\nยังไงไม่รู้"

# hi "How are you feeling? You were pretty out of it yesterday."
hi "เป็นไงบ้าง เมื่อวานเธอดูไม่ไหวเลยนะ"

show rin basic_awayabsent
with charachange

# rin "I'm okay. What do you mean yesterday?"
rin "โอเคดี เมื่อวานนี่หมายถึงอะไร"

# hi "You don't remember?"
hi "จำไม่ได้เหรอ"

show rin relaxed_disgust
with charachange

# "She tilts her head to the side like a bird, looking somewhat confused."
"เธอเอียงคอดูงง ๆ เหมือนนก"

# rin "Remember what? I have a pretty bad memory."
rin "จำอะไร ฉันความจำไม่ค่อยดี"

# hi "About yesterday."
hi "เรื่องเมื่อวาน"

show rin relaxed_surprised
with charachange

# rin "What about yesterday?"
rin "เมื่อวานมีอะไร"

# hi "I came to see you and…"
hi "ฉันไปหาเธอ แล้วก็…"

show rin relaxed_nonchalant
with charachange

# rin "I don't remember that kind of thing happening."
rin "ไม่ยักจำได้ว่ามีอะไรอย่างนั้นด้วย"

# "She really doesn't remember? I don't know if this is a good thing or a bad thing, but I feel disheartened all the same."
"จำไม่ได้จริง ๆ เหรอ ไม่รู้จะเรียกว่าโชคดีหรือโชคร้ายดี แต่จะดีหรือร้ายฉันก็ละเหี่ยใจอยู่ดี"

show rin basic_lucid
with charachange

# rin "I remember that I promised to show you one place, though. Did that happen for real?"
rin "แต่จำได้ว่าสัญญาจะพานายไปดูที่หนึ่ง เป็นอย่างนั้นจริงมั้ย"

show rin basic_awayabsent
with charachange

# rin "Maybe I just think that I remember that and I really don't."
rin "ฉันอาจจะคิดว่าตัวเองจำได้แต่ที่จริงจำไม่ได้ก็ได้"

# hi "No, that was real too."
hi "เปล่า อันนั้นเธอก็พูดจริง ๆ"

show rin basic_absent
with charachange

# rin "Okay. Do you want to go?"
rin "โอเค อยากไปมั้ย"

# hi "Now?"
hi "ตอนนี้?"

show rin basic_deadpannormal
with charachange

# rin "Yeah."
rin "อืม"

# hi "Well, sure, why not. Is it far?"
hi "ก็ ได้สิ ไกลมากมั้ย"

show rin basic_deadpan
with charachange

# rin "It's not."
rin "ไม่ไกล"

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
$ renpy.music.set_volume(0.8, 0.5, channel="music")
play ambient sfx_parkambience fadein 0.5

scene bg school_courtyard
with locationskip

# "Together, we walk downstairs and then outside. The usual summer day, whirring cicadas and all, greets us. It's immensely hot, and without the air conditioning the classrooms offer, I start sweating immediately."
"พวกเราเดินลงบันไดออกมาข้างนอกด้วยกัน วันนี้เป็นวันอย่างวันหน้าร้อนตามปกติที่มีเสียงจักจั่นและอะไร\nทั้งหลายแหล่ อากาศนั้นร้อนจัด พอไม่มีเครื่องปรับอากาศอย่างในห้องเรียนแล้วเหงื่อฉันก็แตกพลั่ก"

scene bg school_gardens
with locationchange

# "We start along the tree-lined pathway that leads towards the dorms."
"พวกเราเดินไปตามทางที่มีต้นไม้ขนาบข้างไปยังหอ"

# "The cherry trees offer shade, with the sunlight blinking through the holes in the canopy. The light creates a chaotic pattern of shadows dappled with bright places where the beams hit the pavement."
"ต้นซากุระบังเป็นร่มเงาโดยที่ยังมีแสงแดดลอดมาตามช่องโหว่จนเกิดเป็นผืนเงาที่มีจุดแสงแดดแต้มอยู่ตามทางเท้า"

# "Rin's eyes are wandering in every direction but mine. I get the feeling that it's intentional."
"ตารินมองไปทุกที่ยกเว้นที่ฉัน สัมผัสได้ว่าเธอจงใจแน่ ๆ"

$ renpy.music.set_volume(0.7, 0.5, channel="ambient")
$ renpy.music.set_volume(0.6, 0.5, channel="music")

scene bg school_forest1
with locationskip

# "She leads me to the back gate once again, taking us through it and into the forest beyond. As before, the dropping temperature and the drastically reduced levels of light make it feel like the forest is swallowing us into its cavernous belly."
"เธอพาฉันมาที่ประตูด้านหลังอีกครั้งแล้วพาเข้าป่าที่อยู่ลึกเข้าไป และอย่างเช่นเคย อุณหภูมิที่ลดวูบและความสว่าง\nที่หดหายให้ความรู้สึกราวกับว่าป่านั้นกำลังกลืนกินพวกเราเข้าไปยังกระเพาะของมันที่เป็นโถงถ้ำ"

scene bg school_forest2
with locationchange

# "We head uphill along the same path as last time, snaking around trees and boulders, over roots and rocks, past wild undergrowth. Birds sing somewhere in the woods, soloists for the humming background music of the treetops."
"พวกเราเดินมาตามทางเดิมที่มาคราวที่แล้ว ลดเลี้ยวไปตามต้นไม้ รากไม้ หินก้อนใหญ่ หินก้อนเล็ก ผ่านพืชพื้นป่า\nที่รกชัฏ เสียงนกร้องแว่วมาจากในป่าเป็นบทเพลงขับกล่อมเดี่ยวแห่งผืนใบบนต้นไม้"

scene bg school_forestclearing
with locationchange

# "We go past the small clearing with the big maple that is now called the Worry Tree. The climb steepens, then becomes easier again."
"พวกเราเดินผ่านรอยแยกเล็ก ๆ ที่อยู่กับต้นเมเปิลที่ตอนนี้ได้ชื่อว่าต้นทุกข์แล้ว ทางเดินชันขึ้น แล้วก็ชันน้อยลงอีกรอบ"

scene bg school_forest2
with locationchange

# "I have to stop a few times to catch my breath, then hurry after Rin who doesn't stop to wait for me."
"ฉันต้องพักหายใจเป็นระยะ ๆ แล้วรีบตามรินที่ไม่รอฉันไป"

# "Soon, I'm out of breath again."
"ไม่นานก็หอบอีกแล้ว"

$ renpy.music.set_volume(1.0, 0.5, channel="ambient")
$ renpy.music.set_volume(0.4, 0.5, channel="music")

scene bg school_hilltop_border
with locationchange

# "Suddenly the trees end, and we emerge from the forest. The boundary of the woods is sharp and abrupt, as though a line had been drawn to mark it."
"จู่ ๆ เหล่าต้นไม้ก็หายไป พวกเราเดินออกมาจากป่า เขตป่านั้นแบ่งชัดราวกับว่ามีเส้นที่ขีดเอาไว้"

# "The hill continues to climb up a little further ahead, but from here to the top it's a rocky meadow, patches of grass and small bushes that look like they are growing straight from the rock."
"ยังมีเนินชันขึ้นไปต่ออีก แต่ตอนนี้มีแต่เนินหินขรุขระแล้ว บริเวณหินมีผืนหญ้าและพุ่มไม้เล็ก ๆ ที่เหมือนงอกออกมา\nจากหินประดับอยู่"

$ renpy.music.set_volume(1.5, 0.5, channel="ambient")
stop music fadeout 2.0
$ renpy.music.set_volume(1.0, 10.0, channel="music")

scene bg school_hilltop_spring at Fullpan(15.0)
with locationchange

# "We soon reach the highest point, with the forest behind us and the view to every direction opening in front of our eyes."
"ไม่นานก็มาถึงยอดเขา ผืนป่านั้นอยู่เบื้องหลังเรา ทิวทัศน์แบบรอบด้านปรากฏสู่สายตา"

# "The city lies far below and away, lazily reveling in the quiet afternoon mood."
"เมืองที่อยู่เบื้องล่างออกไปแสนไกลนั้นทอดตัวอยู่ท่ามกลางบรรยากาศยามบ่ายเงียบงัน"

# "You can see pretty far from here, and the vista is beautiful. I wonder how high up we are."
"พออยู่บนนี้แล้วเห็นได้ไกลพอตัวเลย เป็นภาพทิวทัศน์อันงดงาม ตรงนี้สูงแค่ไหนกันนะ"

# "I breathe the fresh air and feel my heart rate slowly going back down. I think I might've overdone it a bit; a higher pulse is dangerous for me. I'm feeling fine right now, though."
"ฉันสูดหายใจเอาอากาศอันสดชื่นเข้าปอด ใจค่อย ๆ เต้นช้าลงกว่าเมื่อครู่ น่าจะฝืนตัวเองไปหน่อย ให้ใจเต้นแรงมาก\nไม่ดีแน่ แต่ตอนนี้ก็ไม่ได้เป็นอะไรแล้วน่ะนะ"

# "The wind picks up, ruffling my hair and causing the trees below us to sway. It makes the grass undulate in waves as the breeze sweeps across the hilltop."
"ลมพัดมาจนผมฉันปลิวและต้นไม้ที่อยู่ข้างหลังพวกเราขยับไหว หญ้าลู่ลมไปเมื่อลมพัดผ่านยอดเขา"

# "Sun shines from the open skies upon us, a few clouds passing by to shadow it. What was painful heat before is now gentle warmth."
"พระอาทิตย์ส่องแสงจากท้องฟ้าเบื้องบนโดยมีเมฆสองสามก้อนเลื่อนมาบดบัง อากาศที่ร้อนแทบตายนั้นลดเหลือเพียง\nความอบอุ่นอันอ่อนโยน"

# "I take a good look around. The hilltop is pretty in the way nature often is, unplanned harmony found in the natural arrangement of things."
"ฉันมองไปรอบ ๆ ให้ทั่ว ๆ ยอดเขานี้นั้นก็เป็นอย่างที่ธรรมชาติมักเป็น นั่นคือความลงตัวที่ไม่ได้มีความตายตัวแบบวิถี\nการจัดสรรอย่างธรรมชาติ"

# "The most striking feature is the abundance of small yellow flowers. They're literally everywhere in this small meadow. I can't help commenting on it."
"สิ่งที่โดดเด่นที่สุดก็คือดอกไม้สีเหลืองดอกเล็ก ๆ ที่บานสะพรั่งอยู่ทั่วยอดเขานี้ ฉันอดออกปากชมไม่ได้"

# hi "Wow. A lot of flowers."
hi "โห ดอกไม้เยอะจัง"

show bg school_hilltop_spring at right
show rin basic_absent at center
with charaenter

# rin "Yeah. Do you know this kind? They will fly away."
rin "อืม รู้จักดอกนี้มั้ย ที่จะปลิวไปน่ะ"

# hi "Yeah. Dandelions."
hi "อื้ม แดนดีไลออน"

show rin basic_awayabsent
with charachange

# rin "There are not many of them at the school, because they cut the grass so often. Nobody cuts grass up here."
rin "ที่โรงเรียนไม่ค่อยมีเพราะตัดหญ้าบ่อยมาก บนนี้ไม่มีใครมาตัดหญ้า"

# "The fragile-looking flowers will soon turn white and fluffy like cotton, and the wind will carry their seeds away."
"ดอกไม้ดูบอบบางนี้จะกลายเป็นอย่างปุยนุ่นนิ่มนวลสีขาวที่ลมจะพัดพาให้เมล็ดลอยไป"

$ renpy.music.set_volume(1.0, 0.5, channel="ambient")

scene ev dandelion:
   yalign 0.5 xalign 0.5 zoom 0.8 subpixel True
   ease 20.0 zoom 0.9
with locationchange

# "I crouch down to look at one tiny yellow flower, silently basking in the sunlight. There's not a hint of white yet, so it's still waiting for its time to be fulfilled."
"ฉันย่อตัวลงมองดอกสีเหลืองเล็ก ๆ ดอกหนึ่งที่อาบแดดอยู่อย่างเงียบ ๆ ยังไม่มีสีขาวโผล่มา แปลว่ากำลังรอเวลานั้น\nของมันให้มาถึงอยู่"

# "I brush my fingers against the delicate yellow petals, feel the soft texture in my fingertips. It feels nostalgic somehow. I hear Rin approaching from behind and stand back up to face her."
"ฉันลูบกลีบดอกสีเหลืองบอบบางนั้นให้ผิวสัมผัสนุ่มนวลนั้นส่งผ่านปลายนิ้วมือมา ชวนให้คิดถึงอดีตอย่างบอกไม่ถูก\nพอได้ยินเสียงฝีเท้ารินที่เดินเข้ามาทางด้านหลังฉันก็ลุกขึ้นยืนหันไปมองหน้าเธอ"

stop ambient fadeout 3.0

scene bg school_hilltop_spring at left
show rin basic_sad at center
with locationchange

# "She has a weird look on her face."
"เธอทำหน้าแปลก ๆ"

# hi "Something on your mind?"
hi "คิดอะไรอยู่เหรอ"

show rin basic_upset
with charachange

# rin "I don't know. It's just…"
rin "ไม่รู้สิ แค่…"

play music music_rin fadein 0.5

# rinbabble "You just look so sad all the time and become upset so easily and it makes me confused and I really don't remember much about yesterday except that you came to my room and that's why it might be because of me so if it's because of me I think that I know why, it's because people don't really like talking to me and you might be the same and that would be sad I know that people and I'm talking about others than Emi too always say that I'm strange and that I talk strange things so I thought I'd try not to say strange things but that just makes me think more and new and strange and colorful that was not a good word but maybe you understand anyway and odd things so if I want to say something I don't really know how and then the words are not the same as the thoughts because something goes wrong on the way out but it's not like the thoughts are really the thing I should be saying it's more like the idea of the thought or the feeling of the idea or the idea of the feeling but it's not really any of those either because there is no word for it unless I invent a new one which is not really useful so I've been thinking if doing things is better than saying so maybe because yesterday I took those pills and I was feeling a little strange I might have done something that I shouldn't besides I don't even know if it would be any better if I just could say the thought there is no telepathy that's real telepathy isn't there I think it'd be terrible and useful at the same time but right now I wouldn't mind because misunderstanding is so easy but understanding is not and I thought—"
rinbabble "นายดูเศร้าตลอดแถมยังอารมณ์เสียง่ายจนฉันงงแล้วฉันก็จำอะไรเมื่อวานได้ไม่มากนอกจากที่ว่านายมาห้องฉันแล้วฉันก็เลยคิด\n\nว่าคงเป็นเพราะฉันเพราะถ้าเป็นเพราะฉันฉันคิดว่าฉันรู้ว่าทำไมเพราะคนไม่ชอบเวลาคุยกับฉันแล้วนายก็อาจเป็นเหมือนกันด้วย\n\nถ้าเป็นงั้นก็คงเศร้าฉันรู้จักคนนั้นฉันพูดถึงคนอื่นที่ไม่ใช่เอมิอยู่บอกตลอดว่าฉันแปลกฉันพูดแปลกฉันเลยพยายามไม่พูดอะไร\n\nแปลกแต่ยิ่งทำอย่างนั้นก็ยิ่งทำให้ฉันคิดหาอะไรแปลกและมีสีสันที่ใหม่กว่ามาพูดไม่ใช่คำที่ดีหรอกแต่นายก็คงจะเข้าใจนั่นแหละ\n\nแล้วก็อะไรแปลกเพราะงั้นถ้าฉันอยากพูดอะไรฉันไม่รู้จะพูดยังไงแล้วคำพูดไม่ได้เหมือนความคิดเพราะระหว่างทางจะมีอะไรที่\n\nเพี้ยนไปแต่ก็ไม่ได้แปลว่าฉันควรพูดสิ่งที่คิดที่ฉันหมายถึงคือแนวคิดของความคิดหรือความรู้สึกของแนวคิดหรือแนวคิดของ\n\nความรู้สึกแต่ก็ไม่ใช่อะไรพวกนั้นเหมือนกันเพราะไม่มีคำมาใช้อธิบายได้ยกเว้นว่าฉันจะคิดค้นขึ้นมาใหม่ซึ่งก็ไม่ได้มีประโยชน์เท่า\n\nไหร่ฉันเลยคิดว่าถ้าทำดีกว่าพูดแล้วบางทีเพราะเมื่อวานฉันกินยาพวกนั้นไปแล้วฉันก็รู้สึกแปลกนิดหน่อยฉันอาจจะทำอะไรที่ฉัน\n\nไม่ควรทำลงไปอีกอย่างฉันไม่รู้ว่าถ้าพูดสิ่งที่คิดจะดีจริงมั้ยไม่มีกระแสจิตจริงกระแสจิตไม่มีฉันคิดว่าคงจะแย่และมีประโยชน์\n\nเหมือนกันแต่ตอนนี้ฉันไม่อะไรแล้วเพราะการเข้าใจผิดมันง่ายแต่การเข้าใจน่ะไม่ง่ายแล้วฉันก็คิดว่า—"

stop music
play sound sfx_pillow
with vpunch

# "I grasp her shoulder and squeeze hard to make her stop. I don't have the capacity to take all that in at once."
"ฉันจับไหล่เธอแล้วบีบแรง ๆ ให้เธอหยุดพูด สมองฉันประมวลผลหมดนั่นไม่ทันหรอก"

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")

show rin basic_surprised
with charachange

# "Rin shuts up instantly."
"รินเงียบไปทันที"

# hi "Take a breath."
hi "หายใจก่อน"

# hi "I'm not upset. Why would I be? I'm just a little confused, but it's all right."
hi "ฉันไม่ได้อารมณ์เสีย ทำไมฉันจะต้องอารมณ์เสียด้วย ฉันแค่งง ๆ นิดหน่อย แต่ไม่เป็นไรหรอก"

# "I wonder if I was making a face she doesn't like again. I guess I've been thinking about yesterday all the time. Maybe I looked weird. I wish I had a mirror with me at all times."
"ตอนนี้ฉันทำหน้าแบบที่เธอไม่ชอบอีกแล้วหรือเปล่านะ ฉันคงเอาแต่คิดเรื่องเมื่อวานตลอด อาจจะดูแปลก อยากมี\nกระจกไว้คอยส่องตลอดจัง"

# hi "No need to get it all said at once. I'll listen, even if you talk slower."
hi "ไม่ต้องพูดทั้งหมดรวดเดียว พูดช้า ๆ ฉันก็จะฟัง"

show rin basic_deadpanupset
with charachange

# rin "It just came out. Sorry. I'm okay now. I just wanted to say something. I didn't mean that much."
rin "มันไหลออกมาเองน่ะ ขอโทษ ตอนนี้ไม่เป็นไรแล้ว ฉันแค่อยากพูดอะไรหน่อย ไม่ได้กะจะพูดเยอะขนาดนั้น"

play music music_innocence fadein 10.0

show rin negative_worried
with charachange

# rin "It's weird, isn't it?"
rin "แปลกสินะ"

# "She looks at me with a surprisingly timid expression, one that I haven't seen before. I can't help but laugh a little."
"เธอมองฉันอาย ๆ ด้วยสีหน้าที่ฉันไม่เคยเห็นมาก่อน ฉันอดหัวเราะน้อย ๆ ไม่ได้"

# hi "Yeah. It's weird."
hi "อื้ม แปลก"

# hi "You are a pretty weird person but there's nothing wrong with that."
hi "เธอแปลกนะ แต่ก็ไม่ได้ผิดอะไรเลย"

# hi "Thanks for being worried about me, but I'm going to get better. I told you that yesterday, but I guess you don't remember that either."
hi "ขอบคุณที่เป็นห่วงฉันนะ ฉันจะปรับปรุงตัวแล้ว บอกเมื่อวานแล้วไง แต่เธอก็น่าจะจำไม่ได้เหมือนกันมั้ง"

show rin relaxed_nonchalant
with charachange

# rin "I don't. I wonder what else I forgot. Hopefully nothing important like my own name. That'd be terrible."
rin "ไม่ได้ นี่ฉันลืมอะไรไปอีก หวังว่าจะไม่ใช่อะไรที่สำคัญอย่างชื่อฉันนะ ไม่งั้นแย่เลย"

# hi "Well, you kissed me."
hi "ก็ เธอจูบฉัน"

show rin relaxed_surprised
with charachange

# rin "I did?"
rin "เหรอ"

# hi "Yeah, you did. On the lips."
hi "อื้ม จูบปากกัน"

# "I try to sound as matter-of-fact as I can, but I worry that I might be blushing again."
"ฉันปั้นน้ำเสียงให้เรียบนิ่งที่สุด แต่นี่ฉันหน้าแดงอีกหรือเปล่าเนี่ย"

show rin relaxed_doubt
with charachange

# rin "Did you kick me?"
rin "นายเตะฉันมั้ย"

# hi "No! Why would I do that?"
hi "ไม่สิ! ฉันจะเตะเธอทำไม"

show rin basic_deadpancontemplation
with charachange

# rin "Then it's all good, right? It's okay, right? I didn't forget my name."
rin "งั้นก็ไม่เป็นไร ใช่มั้ย โอเคใช่มั้ย ฉันไม่ได้ลืมชื่อฉัน"

# hi "Yeah, it's okay."
hi "อื้ม โอเค"

# "I wish I was more suave so that I could come up with a better follow-up to that, but nothing comes to mind. It's a good thing that Rin has more to say. It makes me feel relieved somehow."
"ฉันอยากมั่นใจกว่านี้เพราะจะได้หาอะไรมาพูดต่ออีก แต่ก็คิดไม่ออก ยังดีที่รินยังมีอะไรจะพูดอีก อยู่ ๆ ก็รู้สึกโล่งใจ\nขึ้นมา"

show rin negative_confused
with charachange

# rin "I think I should say sorry. I'm really bad with people."
rin "ฉันคิดว่าฉันคงต้องขอโทษ ฉันไม่ค่อยรู้ว่าจะต้องทำตัวยังไงกับคนอื่น"

show rin negative_spaciness
with charachange

# rin "Some things are hard to understand - like jellyfish. Do you understand jellyfish?"
rin "บางอย่างก็เข้าใจได้ยาก อย่างแมงกะพรุน นายเข้าใจแมงกะพรุนมั้ย"

# hi "I… I guess not."
hi "ฉัน… ว่าไม่"

show rin negative_sad
with charachange

# rin "People are like jellyfish to me. I don't understand."
rin "ฉันมองว่าคนอื่นน่ะเหมือนแมงกะพรุน ฉันไม่เข้าใจ"

# "Now it's her turn to make a face I don't really like seeing."
"แล้วก็เป็นตาของเธอที่จะทำหน้าที่ฉันไม่อยากเห็นบ้าง"

show rin basic_sad
with charachange

label th_choiceR16:

menu:
    with menueffect

    # rin "I've never really had friends."
    rin "ฉันไม่เคยมีเพื่อนเลย"

    # "What about me?":
    "แล้วฉันล่ะ":
        return m1

    # "What about Emi?":
    "แล้วเอมิล่ะ":
        return m2

label th_R16a:

# hi "Nah. I'm your friend, for one."
hi "ไม่หรอก อย่างน้อยเธอก็มีฉันเป็นเพื่อนแล้วคนหนึ่ง"

# hi "I mean, think about it. We already talk a lot to each other, and we've even gotten upset at each other and then forgiven the other for it."
hi "ก็ลองคิดดูสิ เราคุยกันมาเยอะแล้ว แถมเคยโกรธกัน หายกันแล้วด้วย"

# hi "That's what they call friendship."
hi "นั่นแหละมิตรภาพ"

label th_R16b:

# hi "What about Emi?"
hi "แล้วเอมิล่ะ"

show rin basic_surprised
with charachange

# "She pauses for a while, as if having to consider the possibility came unexpected to her."
"เธอชะงักไปครู่หนึ่งราวกับว่าเธอไม่เคยคิดว่าจะเป็นอย่างนั้นไปได้"

show rin basic_awayabsent
with charachange

# rin "Emi… takes care of me. I don't really know why."
rin "เอมิ… ดูแลฉัน ไม่ค่อยเข้าใจว่าทำไม"

show rin negative_annoyed
with charachange

# rin "But I can't really talk to her, not in that way. It's like her head is made of soap foam and marshmallows. Or maybe it's just me. I like her though."
rin "แต่ฉันคุยแบบนั้นกับเอมิไม่ได้ เหมือนสมองเธอทำจากฟองสบู่กับมาร์ชเมลโลว์"

# hi "She's really nice, isn't she?"
hi "เอมิใจดีเนอะ"

show rin basic_absent
with charachange

# rin "Yeah."
rin "อืม"

# hi "I want to be your friend too."
hi "ฉันก็อยากเป็นเพื่อนเธอเหมือนกัน"

# hi "I'll listen to you if you want to talk. If you don't, then I can just sit quietly next to you."
hi "ถ้าเธออยากคุยฉันก็จะคอยรับฟัง ถ้าเธอไม่อยากฉันก็จะอยู่เงียบ ๆ ข้าง ๆ เธอ"

# hi "And I want to tell you about what I think too. It goes both ways."
hi "แล้วฉันจะบอกด้วยว่าฉันคิดอะไร แลกกัน"

# hi "We should definitely be friends."
hi "เราต้องเป็นเพื่อนกันแล้วละ"

label th_R16c:

show rin basic_deadpanamused
with charachange

# rin "It's really nice of you to say that."
rin "นายนี่แสนดีจังนะ"

show rin basic_awayabsent
with charachange

# rin "I have always been able to tell everything to pencils and paints and paper. They are my best friends."
rin "ฉันพูดอะไรให้ดินสอกับสีกับกระดาษฟังตลอด พวกนั้นเป็นเพื่อนสนิทฉันเลยละ"

show rin basic_lucid
with charachange

# rin "It is harder with people. I have to use words, that is hard for me."
rin "กับคนแล้วพูดยาก ฉันใช้คำพูดไม่เก่ง"

# hi "Yeah I know, you told me. About how you forget."
hi "อื้ม รู้น่า เธอบอกฉันแล้วไง ที่ว่าเธอลืมอะไร ๆ นั่นน่ะ"

show rin basic_absent
with charachange

# "Rin nods at me wordlessly and I dare to attempt showing her a little, encouraging smile. I hope I do it properly. She doesn't reply in any way."
"รินพยักหน้าให้ฉันไม่พูดอะไร ฉันยิ้มบาง ๆ เป็นกำลังใจให้เธอ หวังว่าจะใช้ได้นะ เธอไม่ตอบสนองอะไร"

# "I feel really glad. The distance Rin puts between herself and everything else has made me feel really uneasy ever since I met her. If we become real friends, I'm sure I could understand her more."
"ดีใจจัง ตั้งแต่ที่ได้เจอกัน ระยะห่างที่รินกันตัวเธอออกจากสิ่งอื่นนั้นทำให้ฉันรู้สึกไม่สบายใจเอามาก ๆ ถ้าได้\nเป็นเพื่อนกันแล้วฉันคงเข้าใจเธอได้มากกว่านี้แน่"

# "I'm sure that this way, we can close the gap of understanding between us."
"เช่นนี้แล้ว ฉันมั่นใจว่าระยะห่างระหว่างเราจะลดน้อยลงได้"

show rin basic_awayabsent
with charachange

# "My thoughts don't transmit to Rin. She seems lost deep in thought, wandering amidst the sea of yellow flowers covering the grassy hilltop. It's just as well."
"ความคิดฉันไม่ได้ส่งไปถึงริน เธอทำหน้าคิดอะไรอยู่พลางเดินอยู่กลางทุ่งดอกไม้สีเหลืองที่ปกคลุมยอดเขาที่มีหญ้าแซมนี้\nโชคดีเหลือเกิน"

$ renpy.music.set_volume(0.4, 2.0, channel="music")
play ambient sfx_parkambience fadein 7.0

scene bg school_hilltop_spring_ss at left
with shorttimeskip

# "Time passes, the breeze making the taller grass sway gently in time with the wind. Rin hums a little song to herself so quietly that I can't tell what it is, if it's even anything at all."
"เวลาผ่านไป หญ้าสูงลู่ลมไปตามจังหวะลมพัด รินฮัมเพลงอยู่กับตัวเองเสียงค่อยจนฉันไม่ได้ยินว่าเพลงอะไร ไม่แน่ว่า\nอาจจะไม่ใช่เพลงอะไรด้วยซ้ำ"

# "A stronger gust sweeps over the hilltop, and the sound of the trees in the wind buries the song away."
"คราวนี้ลมพัดแรงขึ้นจนเสียงต้นไม้ที่เสียดสีกับสายลมกลบเพลงนั้นไป"

# "I check my watch, more out of habit more than anything else. It's 4:30 right now, on this Saturday afternoon."
"ฉันก้มมองนาฬิกาด้วยความเคยชิน ขณะนี้เป็นบ่ายวันเสาร์ เวลา 16 นาฬิกา 30 นาที"

show rin basic_awayabsent_ss at center
with charaenter

# "Rin looks into the distant horizon with that odd, blank stare of hers, as if she were looking at nothing at all. Her pupils are dark and quiet like a pair of deep, still ponds."
"รินมองไปสุดขอบฟ้าด้วยสายตาว่างเปล่านั้นของเธอที่ราวกับว่าไม่ได้มองอะไรอยู่เลย รูม่านตาเธอดำสนิทคล้าย\nบ่อน้ำบาดาลสองบ่อที่มีน้ำนิ่งอยู่"

$ renpy.music.set_volume(0.7, 6.0, channel="music")

label th_R16d:

# hi "I think I'm going to quit the art club. I realized it when we had that argument last week."
hi "ฉันว่าจะลาออกจากชมรมศิลปะแล้วละ พอดีตอนที่ทะเลาะกันเมื่อสัปดาห์ก่อนฉันก็เริ่มคิดน่ะ"

# hi "It was a good thing I tried it, but it's just not my thing, you know? I had more fun getting to know you than actually doing the art stuff in there."
hi "ได้ลองทำก็ดีอยู่หรอก แต่ฉันไม่ถนัดเลยจริง ๆ ได้รู้จักกับเธอยังสนุกกว่าไปทำกิจกรรมศิลปะที่ชมรมอีก"

# hi "But I want to stay as your friend. Would that be all right?"
hi "แต่ฉันยังอยากเป็นเพื่อนกับเธออยู่ จะได้หรือเปล่า"

show rin basic_deadpan_ss
with charachange

# rin "Sure. It was getting pretty creepy anyway with you staring at me all the time."
rin "ได้ ฉันก็ขนลุกเหมือนกันที่นายเอาแต่จ้องฉันน่ะ"

# "Her comment makes me fluster immediately, but I manage a reply."
"คำพูดเธอทำเอาลนลาน แต่ฉันก็ตอบไปได้"

# hi "Sorry about that."
hi "ขอโทษนะ"

show rin basic_deadpandelight_ss
with charachange

# rin "It's okay, I'm used to it. You're not the first person who likes to see me paint."
rin "ไม่เป็นไร ฉันชินแล้ว นายไม่ใช่คนแรกหรอกที่ดูฉันตอนวาดรูป"

show rin basic_absent_ss
with charachange

# rin "Are you going to do some other thing?"
rin "จะไปหาอย่างอื่นทำมั้ย"

# hi "I don't know. Probably not."
hi "ไม่รู้สิ คงจะไม่"

label th_R16e:

show rin relaxed_doubt_ss
with charachange

# rin "You are going to become better, right?"
rin "นายจะปรับปรุงตัวใช่มั้ย"

# hi "Sure."
hi "อื้ม"

show rin relaxed_nonchalant_ss
with charachange

# rin "Me too, you know. I'm going to talk to that friend of the teacher and ask her to put my stuff in her place and work hard to get all that done."
rin "ฉันก็ด้วยแหละ ฉันจะไปคุยกับเพื่อนครูคนนั้นแล้วขอให้ขนของฉันไปไว้ที่ที่เธออยู่ แล้วก็ไปตั้งใจทำอะไรให้เสร็จ"

show rin basic_lucid_ss
with charachange

# rin "I decided that just now, you know. But I think I knew it all along."
rin "เพิ่งคิดได้เมื่อกี้แหละ แต่ฉันคิดว่าฉันรู้อยู่แก่ใจมาตลอดอยู่แล้ว"

show rin basic_deadpannormal_ss
with charachange

# rin "I've had this feeling for a long time now, that I am going to change. Even if I hate it and don't want it, even if I wanted to, I would change."
rin "ฉันรู้สึกอย่างนี้มานานแล้ว ที่ว่าฉันจะเปลี่ยนไป ต่อให้ฉันจะไม่ชอบและไม่อยากเปลี่ยน ต่อให้ฉันอยากเปลี่ยน\nฉันจะเปลี่ยน"

show rin basic_deadpanupset_ss
with charachange

# rin "Like I am not enough the way I am. I think this could be a good way to do it because it's like a straight line."
rin "เหมือนว่าแค่นี้มันยังไม่พอ ฉันว่าแบบนี้แหละดีเพราะเหมือนเส้นตรงดี"

show rin basic_deadpancontemplation_ss
with charachange

# rin "Like I've learned all the things in my life so far just for this. It's just art, and it's the only thing I really know. I know what I'm going to do, so it's good. I'm not afraid at all."
rin "เหมือนว่าฉันเรียนรู้อะไรมาทั้งชีวิตเพื่อสิ่งนี้ ก็แค่ศิลปะ ศิลปะเป็นสิ่งเดียวที่ฉันรู้จักจริง ๆ ฉันรู้ว่าจะทำอะไร\nไม่เป็นไรหรอก ฉันไม่ได้กลัวเลย"

show rin basic_deadpansurprised_ss
with charachange

# rin "I feel like I always do. Is that weird?"
rin "ฉันรู้สึกเหมือนเป็นงั้นตลอด แปลกมั้ย"

# hi "No. Not at all."
hi "ไม่ ไม่เลย"

stop ambient fadeout 2.0
$ renpy.music.set_volume(1.4, 4.0, channel="music")

window hide

scene black
with shuteye

window show

# "I close my eyes, and give in to the irresistible sensation that has been growing inside me all week long."
"ฉันหลับตาแล้วปล่อยให้ความรู้สึกที่ก่อขึ้นในใจมาทั้งสัปดาห์นี้พาตัวฉันไป"

# "I float up, towards the surface of my own life."
"ฉันลอยขึ้นมายังพื้นผิวชีวิตฉัน"

# "The pressure of being underwater slowly diminishes, the weightless sensation becomes stronger."
"แรงดันใต้น้ำลดลงอย่างช้า ๆ ความรู้สึกล่องลอยเริ่มมีมากขึ้น"

# "I break the surface of the water, lifting my head into the sunlight and inhale deeply, breathing in fresh air as if for the first time in a long, long while."
"ฉันลอยขึ้นมาจนเหนือน้ำเงยหน้าขึ้นรับแสงแดดแล้วสูดหายใจเอาอากาศอันสดชื่นนี้เข้าลึก ๆ ราวกับว่าไม่ได้สัมผัส\nมานานแสนนาน"

scene bg school_hilltop_spring_ss at left
show rin basic_deadpandelight_close_ss at center
with openeye

# "My lungs fill with oxygen, and I open my eyes to see Rin's peaceful, determined face."
"ออกซิเจนเข้าเติมเต็มในปอดฉัน พอลืมตาก็พบกับใบหน้าอันสงบและมุ่งมั่นของริน"

stop music fadeout 10.0
$ renpy.music.set_volume(1.0, 2.0, channel="music")

scene bg school_hilltop_border_ss
with shorttimeskip

# "We walk down the slope carefully and slowly to avoid falling down, Rin in the lead and me a few steps behind."
"พวกเราค่อย ๆ เดินลงมาพลางระวังไม่ให้ลื่นล้ม รินนำทางโดยมีฉันตามอยู่ไม่ห่าง"

# "Rin surely can do this. Even if she can't, she's going to pull through."
"รินทำได้แน่ ต่อให้ไม่ได้ เธอจะผ่านมันไปได้"

# "I'm sure that I can keep my head above water too, from now on."
"นับจากนี้ไป ฉันเองก็มั่นใจว่าฉันจะประคองให้หัวอยู่พ้นน้ำได้"

# "The sun sets behind our backs, setting the world ablaze in its orange glow."
"พระอาทิตย์ลับขอบฟ้าอยู่เบื้องหลังพวกเรา ประกายแสงส้มเรืองรองลุกโชนอยู่บนผืนโลก"

# "I keep watching the back of the red-headed girl descending the path a few steps ahead of me."
"ฉันมองตามหลังสาวผมแดงคนนี้ที่เดินนำฉันอยู่สองสามก้าว"

# "If it's only this much… this distance between us is definitely within my reach."
"ถ้าเพียงเท่านี้แล้ว… ระยะห่างระหว่างเรานั้นจะไม่ไกลเกินฉันเอื้อม"

window hide

return