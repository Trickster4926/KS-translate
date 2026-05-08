label th_E16:

window hide None

scene bg school_scienceroom
with fade

nvl clear
nvl show dissolve

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_normal fadein 3.0

# n "\n\n\nMy head's in a spin all through Mutou's class."
n "\n\n\nตลอดคาบเรียนหัวฉันหมุนติ้ว"

# n "I'm going to have dinner."
n "ฉันจะได้กินข้าวเย็น"

# n "With Emi."
n "กับเอมิ"

# n "Who wants to be my girlfriend, no less."
n "และเธออยากเป็นแฟนฉันด้วย"

# n "A date…"
n "เดต…"

# n "And then she kissed me."
n "แล้วเอมิก็จูบฉัน"

# n "That kiss. I keep going back to it, playing it over in my mind again and again."
n "จูบนั้น ฉันกรอกลับไปที่เหตุการณ์นั้นเล่นซ้ำแล้วซ้ำเล่าอยู่ในหัว"

# n "Everything about that moment felt so right."
n "ทุกอย่าง ณ ตอนนั้นช่างลงตัวเหลือเกิน"

# n "\nMy mind drifts off, lost in thoughts of Emi."
n "\nใจฉันล่องลอยไปพลางคิดถึงเอมิ"

$ renpy.music.set_volume(1.0, 2.0, channel="music")

nvl clear
nvl hide dissolve
window show

show muto normal
with charaenter

# mu "Nakai? Hello?"
mu "นากาอิ? ฮัลโหล?"

# "It seems like I've drifted a bit too far."
"ดูท่าว่าจะใจลอยไปไกลไปหน่อย"

# hi "Huh? What?"
hi "ฮะ? ครับ?"

show muto irritated
with charachange

# mu "Egad! You've contracted some kind of amnesia!"
mu "คุณพระ! เธอติดโรคความจำเสื่อมเข้าให้แล้ว!"

# mu "Someone get the nurse!"
mu "ใครก็ได้เรียกคุณพยาบาลมาที!"

# "The class chuckles at Mutou's antics."
"คนทั้งห้องหัวเราะกับมุกตลกของครู"

# hi "Sorry, sir."
hi "ขอโทษครับ"

show muto normal
with charachange

# mu "Hmm, won't happen again and all that, right?"
mu "อืมม จะไม่ทำอีกแล้วใช่ไหม"

# hi "Exactly."
hi "ครับผม"

# "Mutou brightens considerably."
"ครูทำหน้ายิ้ม ๆ ขึ้นมา"

show muto smile
with charachange

# mu "Well! Lovely to hear!"
mu "โอเค! ดีแล้ว!"

# mu "I'd hate to have my star pupil slacking off, after all."
mu "ฉันไม่อยากให้นักเรียนดาวเด่นของฉันอู้หรอกนะ"

hide muto
with charaexit

# "I've been doing well, but I hardly qualify as a star pupil, I think."
"เรียนได้ดีก็จริง แต่ไม่น่าเป็นดาวเด่นขนาดนั้นนะ"

# "I'm fairly certain that this class is the sort that everyone does well in. It's just memorizing formulas."
"ฉันรู้สึกว่าใคร ๆ ก็พอจะเรียนวิชานี้รู้เรื่อง ก็แค่จำสูตรเฉย ๆ"

# "True to my word, I manage to pay attention for the rest of the class."
"ฉันคอยตั้งใจเรียนไปจนหมดคาบอย่างที่ได้บอกครู"

stop music fadeout 2.0

show muto normal
with shorttimeskip

play sound sfx_normalbell

# mu "Nakai, may I have a word with you?"
mu "นากาอิ ขอคุยกับเธอหน่อยได้มั้ย"

# "I wonder if I'm in trouble for earlier."
"เรื่องเมื่อกี้หรือเปล่านะ"

# hi "Uh, sure."
hi "เอ่อ ครับ"

# hi "Am I in trouble?"
hi "ผมทำอะไรไม่ดีหรือเปล่า"

show muto irritated
with charachange

# "Mutou looks genuinely confused for a moment."
"ครูทำหน้างง ๆ ขึ้นมาอยู่ครู่หนึ่ง"

# mu "Beg your pardon?"
mu "อะไรนะ"

# "He tilts his head to one side and thinks for a moment."
"ครูเอียงคอแล้วนึกคิด"

show muto smile
with charachange

# mu "Oh, that! No, no, you're not in any sort of trouble."
mu "อ้อ เรื่องนั้น! เปล่า ๆ เธอไม่ได้ทำอะไรไม่ดีหรอก"

# mu "There's just a question I want to ask you."
mu "ครูแค่มีเรื่องจะถามเธอ"

# hi "What's that?"
hi "อะไรเหรอครับ"

show muto normal
with charachange

# mu "Nothing terrible, I was just wondering what your plans for after graduation are."
mu "ไม่ใช่อะไรหรอก แค่อยากรู้ว่าเรียนจบแล้วเธอจะทำอะไรต่อ"

play music music_another fadein 2.0

# mu "Are you going to university?"
mu "จะเรียนต่อมหา’ลัยหรือเปล่า"

# hi "Yeah, I guess. I can't really see a reason not to go."
hi "อืม มั้งครับ คิดยังไงผมก็ต้องต่อ"

# mu "Given any thought to what you'll study?"
mu "แล้วได้คิดหรือยังว่าจะเรียนอะไร"

# hi "Not really, no. I figure I'll come up with something when I get there."
hi "ก็ไม่นะครับ ผมคิดว่าเดี๋ยวถึงเวลาแล้วก็คงรู้เอง"

show muto smile
with charachange

# "Mutou laughs."
"ครูหัวเราะ"

# mu "Taking things as they come, eh?"
mu "ใช้ชีวิตไปตามกระแสงั้นเหรอ"

# mu "I'd argue against it, but that's how I did things when I went to university."
mu "ก็อยากแย้งอยู่หรอก แต่ตอนครูเรียนมหา’ลัยก็ทำแบบนั้นเหมือนกัน"

# mu "Well, not really."
mu "ก็ ไม่เชิงหรอก"

# mu "I knew I'd go into a science, I just wasn't sure which one."
mu "ครูรู้อยู่ว่าจะเรียนวิทยาศาสตร์ แค่ไม่แน่ใจว่าจะเรียนสาขาไหนดี"

# mu "Ended up with physics, but could just as well have gone for astronomy or what have you."
mu "สุดท้ายก็ไปเรียนฟิสิกส์ แต่เอาจริง ๆ จะไปเรียนดาราศาสตร์หรืออะไรแบบนั้นก็ได้"

show muto irritated
with charachange

# mu "Actually I did go for chemistry first, but there were all sorts of things…"
mu "ที่จริงทีแรกครูเรียนเคมีนะ แต่ก็มีเรื่องอะไรหลายอย่าง…"

# "Mutou trails off, and frowns slightly."
"ครูเสียงอ่อยไปแล้วขมวดคิ้วเล็กน้อย"

# "It takes a minute for him to recover his train of thought, and I wait patiently for him to continue."
"ผ่านไปสักนาทีสองนาทีครูถึงผละจากกระแสความคิดนั้นได้ ฉันรอให้ครูพูดต่ออย่างใจเย็น"

show muto normal
with charachange

# mu "So anyway, I did a lot of physics as well, because I had an interest in that, but I wasn't sure if it was for me."
mu "แต่นั่นแหละ ครูก็เรียนฟิสิกส์หลายตัวอยู่เพราะสนใจ แต่ไม่แน่ใจว่าตัวเองถนัดจริง ๆ หรือเปล่า"

show muto smile
with charachange

# mu "So I went back to chemistry, and here we are. Yes?"
mu "สุดท้ายก็กลับมาหาเคมี แล้วก็เรื่อยมาจนทุกวันนี้ ไง"

show muto smile
with charachange

# "He smiles at me enthusiastically, as if waiting for me to confirm that yes, here is were we are."
"ครูยิ้มให้ฉันอย่างเปี่ยมพลังราวกับรอให้ฉันตอบกลับว่า ครับ แล้วก็เรื่อยมาจนทุกวันนี้"

# "Somehow I get the feeling that Mutou had a plan for this conversation, but I'll be damned if I can figure it out."
"ไม่รู้ทำไมถึงรู้สึกเหมือนครูมีแผนอะไรอยู่ถึงเรียกมาคุย แต่คิดยังไงก็คิดไม่ออกว่าแผนที่ว่าคืออะไร"

# hi "I'm sorry, I'm not following you."
hi "ขอโทษนะครับ คือผมไม่ค่อยเข้าใจ"

# "Mutou frowns and rubs his chin a bit, looking perplexed. He then snaps his fingers as if he's remembered what the point of all this was."
"ครูขมวดคิ้วแล้วลูบคางดูสับสน แล้วก็ดีดนิ้วเหมือนนึกได้ว่าเรียกฉันมาทำไม"

# mu "Right! Yes! You!"
mu "จริงด้วย! ใช่! เธอ!"

# hi "Me?"
hi "ผม?"

# mu "Yes! You should look into studying one of the sciences!"
mu "ใช่! เธอลองไปดูว่าจะเรียนวิทยาศาสตร์สาขาไหน!"

# mu "You're fantastic at it."
mu "เธอเก่งวิทยาศาสตร์นะ"

# mu "Unless you'd rather just go into math."
mu "เว้นเสียแต่ว่าเธอจะอยากไปเรียนคณิตศาสตร์มากกว่า"

show muto irritated
with charachange

# "Mutou makes a sour face."
"ครูทำหน้าเบ้"

# mu "Not a big fan of straight math. I always liked the experiments more than the proofs."
mu "ครูไม่ค่อยชอบคณิตแบบเพียว ๆ เท่าไหร่ ชอบการทดลองมากกว่าการพิสูจน์น่ะ"

# hi "You're saying I should study science at university?"
hi "ครูจะบอกว่าผมควรไปเรียนต่อทางวิทยาศาสตร์?"

# "Mutou seems thrown off balance by my question."
"คำถามนั้นทำให้ครูเหมือนไม่ได้ตั้งตัว"

show muto normal
with charachange

# mu "Well, sort of."
mu "ก็ ประมาณนั้น"

show muto smile
with charachange

# mu "You could also join the science club!"
mu "หรือจะเข้าร่วมชมรมวิทยาศาสตร์ก็ได้นะ!"

# mu "Trouble is, there's not actually a science club."
mu "ปัญหาคือเราไม่มีชมรมวิทยาศาสตร์"

# mu "But there could be!"
mu "แต่ตั้งชมรมใหม่ได้!"

# mu "You could even be a charter member!"
mu "เธอเป็นสมาชิกรุ่นแรกได้เลยนะ!"

# mu "A founding father!"
mu "เป็นผู้บุกเบิก!"

# mu "Of course, you'd need to find other members."
mu "แน่ละว่าเธอต้องไปหาสมาชิกคนอื่นด้วย"

show muto normal
with charachange

# mu "Well, only if you wanted to."
mu "ก็ ถ้าเธออยากตั้งชมรมน่ะนะ"

# mu "We could just start it up with the two of us."
mu "เริ่มจากเธอกับครูก่อนก็ได้"

# mu "And um."
mu "แล้วก็ เอ่อ"

show muto smile
with charachange

# mu "I could give you things to read, and we could talk about them."
mu "ครูก็จะให้หนังสือเธอไปอ่าน แล้วเราก็มาคุยกัน"

# mu "Er, and I could help you get ready for university and such as well."
mu "เอ่อ แล้วครูก็จะได้ช่วยเธอเรื่องการเตรียมพร้อมเรียนต่ออะไรแบบนั้นด้วย"

show muto irritated
with charachange

# mu "Wait!"
mu "เดี๋ยว!"

# "Mutou rummages around in his briefcase and tosses me a book."
"ครูคุ้ยกระเป๋าแล้วโยนหนังสือเล่มหนึ่งมาให้"

show muto smile
with charachange

# mu "Read that."
mu "เอาไปอ่านซะนะ"

# mu "If it's interesting, then we can talk about it."
mu "ถ้ารู้สึกว่าน่าสนใจก็มาคุยกันได้"

# "“A Brief History of Time?”"
"“{i}ประวัติย่อของกาลเวลา{/i}”?"

# "I don't know if I actually want to read this, but Mutou seems pretty excited about it."
"ไม่รู้ว่าอยากอ่านจริง ๆ หรือเปล่า แต่ครูก็ดูตื่นเต้นพอตัวเลย"

# hi "What's it about?"
hi "ข้างในเป็นเรื่องอะไรเหรอครับ"

show muto normal
with charachange

# mu "Time. Space. Space-time. Black holes and such."
mu "เวลา ปริภูมิ ปริภูมิ-เวลา หลุมดำ อะไรทำนองนั้น"

# mu "And it's not that dense. Just to see if that sort of thing's interesting for you, you understand."
mu "แล้วก็ไม่ได้เนื้อหาแน่นมาก ประมาณว่าลองดูก่อนว่าเธอสนใจหรือเปล่า เข้าใจมั้ย"

# mu "Hang around after class, and we can either discuss it, or I can show you how to make explosives in the lab."
mu "หมดคาบแล้วก็อยู่รอคุยกับครูได้ หรือไม่ก็จะได้พาไปห้องทดลองแล้วทำให้ดูว่าสารระเบิดเขาทำกันยังไง"

show muto smile
with charachange

# "He waves a hand at my quizzical expression."
"ครูโบกมือให้กับฉันที่ยังทำหน้างง ๆ อยู่"

# mu "Joking, sorry."
mu "ครูพูดเล่น ขอโทษที"

# mu "Still, I've kept you here long enough for now."
mu "แต่ก็คุยกับเธอมานานแล้ว"

# mu "Think about science as a career path, Nakai. I think you'd enjoy it."
mu "ไปคิดเรื่องเส้นทางสายวิทยาศาสตร์นะนากาอิ ครูว่าเธอน่าจะชอบ"

# hi "Uh, okay. I will. Thank you for the book."
hi "อ่า ครับ ได้ครับ ขอบคุณสำหรับหนังสือนะครับ"

stop music fadeout 14.0

scene bg school_hallway3
with locationchange

# "I leave the classroom and look up at the clock; quite a chunk of time to kill until Emi's out of practice."
"ฉันออกจากห้องแล้วมองนาฬิกา ยังเหลือเวลาอีกมากกว่าเอมิจะฝึกเสร็จ"

# "Guess I'll give this book a look; I should probably shower as well."
"คงต้องลองอ่านหนังสือเล่มนี้สักหน่อย แล้วก็อาจจะอาบน้ำด้วย"

# "Showering before a date's only proper, right?"
"ก่อนไปเดตก็ต้องอาบน้ำอยู่แล้วใช่มั้ยล่ะ"

# "I head back to the dorms."
"ฉันกลับไปที่หอ"

scene bg school_dormhisao
with locationskip

# "I wonder where I'm supposed to meet Emi, anyway."
"แล้วจะไปหาเอมิที่ไหนดีล่ะเนี่ย"

# "She said “after practice,” but she didn't say where I should find her."
"เอมิบอกว่า “หลังซ้อม” แต่ไม่ได้บอกว่าจะให้ไปเจอที่ไหน"

# "I guess I can just swing by the track; that's probably best, anyway."
"ก็คงต้องลองแวะไปที่ลู่นั่นแหละ น่าจะดีที่สุดแล้ว"

# "If she needs a shower, I can just wait for her in her room or something."
"ถ้าเอมิอาบน้ำอยู่ก็รอให้ออกจากห้องมาก่อนก็ได้"

# "Or in the hallway, I guess; that would be better as well."
"หรือจะไปที่โถงทางเดินก็ดีเหมือนกัน"

# "I take a quick shower, remembering to take my medication once I hop out."
"ฉันอาบน้ำแบบผ่าน ๆ แล้วกินยาก่อนออกมา"

# "Now, for a look at this book."
"ทีนี้ก็อ่านหนังสือเล่มที่ครูให้มา"

stop music

scene black
with dissolve


label th_E17:

scene black
with None

scene bg school_dormhisao
with vpunch

# "I wake with a start."
"ฉันสะดุ้งตื่น"

# "Shit! What time is it?"
"ฉิบ! กี่โมงแล้วเนี่ย"

# "A glance at the clock reveals that I've been asleep for nearly an hour."
"พอเหลือบมองนาฬิกาก็เห็นว่าหลับไปค่อนชั่วโมงได้"

# hi "Thank goodness."
hi "รอดไปที"

# "Emi's practice should be finishing up soon."
"เดี๋ยวเอมิน่าจะซ้อมเสร็จแล้ว"

# "I throw on some casual clothes and head for the track."
"ฉันใส่เสื้อสบาย ๆ แล้วไปที่ลู่วิ่ง"

scene bg school_track
with locationskip

# "Somehow I get the feeling we won't be doing anything fancy for dinner."
"ไม่รู้ทำไมถึงรู้สึกว่าเย็นนี้จะไม่ได้ไปทำอะไรหรูหรากันขนาดนั้น"

# "Emi doesn't strike me as a very fancy sort of person."
"ฉันมองว่าเอมิก็ไม่ได้เป็นคนหรูหรา"

# "Still, I suppose there's a lot I have yet to know about Emi."
"แต่ก็นะ อาจจะยังมีเอมิอีกหลายมุมที่ฉันยังไม่รู้จัก"

# "Despite our newfound closeness, I still feel like I don't know her as well as I should."
"ทั้งที่เราได้ความสัมพันธ์ใหม่ใกล้ชิดกว่าเดิมแล้วฉันก็ยังรู้สึกว่าไม่ได้รู้จักเอมิดีขนาดนั้น"

# "Ah well, I have lots of time to fix that."
"เอาเถอะ ยังเหลือเวลาให้ได้รู้อีกมากมาย"

# "To be honest, I'm looking forward to getting to know her more."
"ว่าตามตรง ฉันก็ตั้งตาคอยที่จะได้รู้จักเอมิให้มากขึ้นด้วย"

# "I'm so caught up in my own thoughts that I hardly register that I'm already at the track."
"ฉันมัวแต่จมอยู่กับความคิดจนไม่ทันรู้ตัวว่ามาถึงลู่แล้ว"

# "Emi is nowhere to be found."
"ไม่มีวี่แววเอมิ"

# "I don't even see any signs of the track team."
"ไม่มีวี่แววคนในทีมวิ่งด้วย"

# "This could be embarrassing."
"โดนแกล้งหรือเปล่าเนี่ย"

# "I turn to head toward the girls' dormitory when I hear a shout."
"ฉันหันกลับเตรียมจะไปหอหญิง แต่ก็มีเสียงตะโกนแทรกมา"

# emi "Hey, Hisao!"
emi "นี่ ฮิซาโอะ!"

play music music_emi fadein 1.0

show emicas smile at center
with charaenter

# "I turn around to see Emi making a beeline for me with a gym bag slung over her shoulder."
"พอหันไปก็เห็นเอมิที่แบกกระเป๋าพละพาดบ่าเดินตรงมาทางนี้"

# "She's changed into some decidedly more casual clothing; a pair of shorts and an olive green top."
"เอมิเปลี่ยนชุดดูเป็นอะไรที่เป็นกันเองมากขึ้น เป็นกางเกงขาสั้นกับเสื้อสวมทับสีเขียวมะกอก"

# "Her running blades have been replaced by more realistic-looking legs that probably wouldn't fool anyone."
"ขาที่เป็นแผ่นสำหรับวิ่งนั้นถูกแทนที่ด้วยขาที่ดูสมจริงขึ้นมา ซึ่งก็ยังดูไม่ค่อยเนียนเท่าไหร่"

# "Emi doesn't seem to care about that, a fact which makes me smile."
"เอมิเหมือนจะไม่สนใจสักเท่าไหร่ ซึ่งฉันก็อดยิ้มไม่ได้"

show emicas happy
with charachange

# emi "Hey, you came!"
emi "ไง มาจริงด้วย!"

show emicas closedsmile
with charachange

# emi "I mean I figured you would, but still…"
emi "คือก็คิดแหละว่านายคงมา แต่ก็…"

show emicas closedsmile_up_close
with characlose

# "I suddenly find myself wrapped in a rather affectionate hug, and it proves to be impossible for me to keep what must be the world's largest grin off my face."
"อยู่ ๆ เอมิก็เข้ามากอดฉันด้วยความรัก และฉันก็กลั้นตัวเองไม่ให้ฉีกยิ้มที่คงจะกว้างที่สุดในโลกออกมาไม่ได้"

# hi "Well, of course I came!"
hi "ต้องมาสิ!"

# hi "I'd be crazy not to, right?"
hi "ไม่มาก็บ้าแล้ว เนอะ"

# "Emi ponders for a moment."
"เอมิคิดอยู่ครู่หนึ่ง"

show emicas grin_up_close
with charachange

# emi "You know, that's true."
emi "ก็จริงนะ"

show emicas wink_up_close
with charachange

# emi "I mean I'm pretty amazing, after all."
emi "เนี่ย ฉันก็เป็นคนที่สุดยอดเหมือนกัน"

# "I shrug in response."
"ฉันยักไหล่"

# hi "I certainly think so."
hi "ฉันคิดว่างั้นเลยแหละ"

show emicas blush_up_close
with charachange

# "It's an offhand remark, which is why I'm surprised to see that it seems to have caught Emi by surprise."
"ฉันพูดไปลอย ๆ ถึงได้แปลกใจที่เอมิเหมือนจะไม่ทันตั้งตัวรับคำพูดนั้น"

show emicas smile_up_close
with charachange

# "She blushes and smiles warmly at me before planting a kiss on my lips."
"เอมิหน้าแดงแล้วยิ้มให้ฉันอย่างอบอุ่นก่อนจะจุ๊บ"

# "Now it's my turn to be surprised."
"คราวนี้เป็นตาฉันที่ไม่ทันตั้งตัวบ้าง"

show emicas grin
with charadistant

# "Emi steps back, resting her weight on her back heel, looking pleased with herself."
"เอมิถอยไปแล้วทิ้งน้ำหนักลงส้นเท้าดูพอใจ"

# "My brain fumbles for an appropriate response."
"ฉันคุ้ยสมองหาอะไรเหมาะ ๆ มาพูดตอบ"

hi "…"

# hi "I should compliment you more often."
hi "คงต้องชมเธอบ่อย ๆ แล้วสิ"

show emicas happy_up
with vpunch

# "Emi laughs and gives me a playful shove."
"เอมิหัวเราะแล้วดันตัวฉันหยอก ๆ"

show emicas closedsmile
with charachange

# emi "Jerk."
emi "บ้า"

show emicas weaksmile_up_close
with characlose

# "I throw an arm around Emi's shoulders and am pleased when she immediately leans into me as if it were the most natural thing in the world."
"ฉันโอบไหล่เอมิไว้ และรู้สึกดีเมื่อเธอโน้มตัวเข้ามาเหมือนว่าเป็นเรื่องปกติธรรมชาติ"

# hi "So, where to?"
hi "แล้วจะไปไหน"

show emicas awayfrown_up_close
with charachange

# emi "I'm not actually sure."
emi "ไม่แน่ใจเหมือนกัน"

show emicas neutral_up_close
with charachange

# emi "Where do people go on dates around here, anyway?"
emi "ปกติเวลาจะไปเดตแถวนี้เขาไปที่ไหนกันล่ะ"

# "That's a damned good question."
"ถามได้ดีมาก มาก ๆ"

# hi "I've got no idea."
hi "ไม่รู้เลย"

# hi "Why don't we just head down to the Aura-Mart and grab something portable?"
hi "ไปหาซื้ออะไรที่ร้านออร่ามาร์ทติดมือไปกินกันมั้ยล่ะ"

# "Emi's face brightens at this idea."
"เอมิทำหน้าสดใสขึ้นมาเมื่อได้ยินเช่นนั้น"

show emicas happy_up_close
with charachange

# emi "A picnic!"
emi "ปิกนิก!"

show emicas wink_up_close
with charachange

# emi "I think you're on to something, Hisao."
emi "ความคิดใช้ได้เลยนี่ฮิซาโอะ"

scene bg school_gate
with locationskip

# "Emi snakes her arm around my waist, and we begin to head for the front gate."
"เอมิยื่นแขนมาโอบเอวฉันไว้ เราออกเดินไปที่ประตูหน้าโรงเรียน"

# "I'm entirely unsure of what I'm meant to do in this situation, but at least Emi seems to be equally clueless."
"ฉันไม่แน่ใจนักว่าจะต้องวางตัวยังไงกับสถานการณ์แบบนี้ แต่อย่างน้อยเอมิก็ไม่รู้เหมือนกันแหละนะ"

scene bg suburb_roadcenter
with locationskip

# "Despite the relaxing feeling of being with Emi, I still can't help feeling a little tense."
"ถึงพออยู่กับเอมิแล้วจะรู้สึกผ่อนคลาย แต่ก็อดเกร็งขึ้นมาหน่อย ๆ ไม่ได้"

# "What if I do something wrong?"
"ถ้าเกิดว่าทำอะไรพลาดไปล่ะ"

# "I'd hate to make an ass out of myself."
"ฉันไม่อยากให้ตัวเองกลายเป็นคนไม่ดีไปหรอก"

scene bg suburb_konbiniext
with locationchange

# "The trip to the Aura-Mart is accompanied by Emi's chatter about how practice went."
"เสียงเอมิเล่าถึงการซ้อมคอยประกบเราไปตามเส้นทางไปยังร้านออร่ามาร์ท"

# "I keep quiet for the most part, merely enjoying the warmth of being around Emi."
"ส่วนฉันก็เงียบไปคอยดื่มด่ำกับความอบอุ่นเมื่อได้อยู่กับเอมิ"

# "We get a few odd looks from passersby, but I don't mind."
"มีคนที่เดินผ่านเรามองมาบ้าง แต่ฉันไม่สนใจหรอก"

# "We wind up buying some bread and instant noodles, realizing too late that we cannot actually cook the latter in the park."
"สุดท้ายเราก็ซื้อขนมปังกับบะหมี่กึ่งสำเร็จรูปกัน แต่ก็เพิ่งมาคิดได้อีกทีว่าเราคงต้มบะหมี่กึ่งฯ กันในสวนสาธารณะ\nไม่ได้"

show emicas weaksmile
with charaenter

# emi "Oh well. I'll make it for lunch or something."
emi "เอาเถอะ ค่อยเก็บไว้กินเป็นมื้อเที่ยงหรือมื้ออะไรวันอื่นแล้วกัน"

# hi "That'll work."
hi "ก็ได้"

stop music fadeout 2.0
$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_parkambience fadein 2.0

scene bg suburb_park
with locationskip

# "The park is located after a brief loss of direction that I blame entirely on Emi."
"เราหาสวนสาธารณะกันจนเจอหลังจากที่หลงทางกันอยู่พักหนึ่ง ซึ่งฉันก็โทษเอมิ"

# "She, of course, blames me."
"แน่นอนว่าเอมิก็โทษฉันด้วย"

show emicas smile:
    center
    easein 1.0 ypos 1.13
with charaenter

# "We find a spot beneath a tree and sit down. I lean back against the trunk, Emi sits across from me."
"เราหาพื้นที่ใต้ร่มไม้แล้วนั่งลง ฉันนั่งพิงต้นไม้ ส่วนเอมินั่งประจันหน้ากับฉัน"

play music music_ease fadein 3.0

# hi "I guess we should have brought a blanket or something to sit on, huh?"
hi "รู้งี้เอาผ้าหรืออะไรมาปูรองนั่งด้วยก็ดีเนอะ"

show emicas smile_up:
    ypos 1.13
with Dissolve(0.2)

show emicas smile
with charachange

# "Emi shrugs."
"เอมิยักไหล่"

show emicas closedsmile
with charachange

# emi "I don't mind."
emi "ฉันนั่งได้"

# hi "Neither do I."
hi "ฉันก็นั่งได้"

show emicas grin_up
with charachange

# "Emi tosses me a package of bread and we dig in."
"เอมิโยนห่อขนมปังให้ และเราก็เริ่มกินกัน"

# "Curry bread. Interesting."
"ขนมปังแกงกะหรี่ น่าสนใจ"

# "I guess I wasn't really paying attention to what I grabbed in the store."
"สงสัยตอนซื้อไม่ได้ดูให้ดีเท่าไหร่ว่าซื้ออะไรมาบ้าง"

show emicas wink_up
with charachange

# emi "Hey, Hisao. You look like your bread's a little spicy."
emi "นี่ ฮิซาโอะ เหมือนขนมปังนายจะเผ็ด ๆ นะ"

# "I shake my head, trying in vain to keep an image of manliness."
"ฉันสั่นหัวเป็นการรักษาภาพความเป็นลูกผู้ชาย"

# hi "Nah, it's hardly spicy at all."
hi "ไม่อะ แทบไม่เผ็ดด้วยซ้ำ"

show emicas closedsmile_up
with charachange

# emi "I see, I see. That must be why your face has gotten so red."
emi "อืมฮึ ๆ คงเพราะแบบนี้สินะถึงได้หน้าแดง"

# hi "Yes, exactly. The lack of spice has uh… gotten my blood up."
hi "ใช่ ใช่แล้ว เพราะมันไม่เผ็ด… เอ่อ เลือดเลยเดินขึ้นมา"

# hi "Because of the disappointment."
hi "เพราะผิดหวัง"

show emicas happy
with charachange

# "Emi laughs and swallows the last of her bread."
"เอมิหัวเราะแล้วกินขนมปังคำสุดท้าย"

show emicas wink
with charachange

# emi "Well, if you can't handle it, I'll be glad to take it off of your hands."
emi "เนี่ย ถ้ากินไม่ไหวฉันก็ยินดีกินแทนให้นะ"

# hi "Hey, just because you wolfed down yours so quickly doesn't mean I'm just going to give you mine."
hi "นี่ เธอเขมือบไวแล้วใช่ว่าฉันจะให้เธอกินของฉันสักหน่อย"

show emicas pout
with charachange

# "Emi mock-pouts, causing me to nearly choke on my bread with laughter."
"เอมิแสร้งทำแก้มป่องจนฉันหัวเราะแทบสำลัก"

# emi "Aw, come on Hisao!"
emi "โธ่ ไม่เอาน่าฮิซาโอะ"

show emicas awayfrown
with charachange

# emi "Aren't you supposed to be concerned with making sure I've got enough to eat now?"
emi "ไม่ใช่ว่านายต้องคอยป้อนฉันให้อิ่มหรือไง"

# emi "We're dating, you know!"
emi "เรามาเดตกันอยู่นะ!"

show emicas pout
with charachange

# emi "Though…"
emi "แต่ว่า…"

# "Emi looks troubled all of a sudden."
"อยู่ ๆ เอมิก็ทำหน้ายุ่งขึ้นมา"

show emicas frown_up
with charachange

# emi "I can't say I feel any different."
emi "ฉันก็รู้สึกเหมือนเดิม"

# hi "Hmm? What do you mean by that?"
hi "หืม หมายความว่าไง"

show emicas awayfrown
with charachange

# emi "What makes this a date?"
emi "เพราะอะไรครั้งนี้ถึงนับว่าเป็นเดต"

# emi "It's just what we would have done anyway, really."
emi "ก็เป็นอะไรที่เราคงทำเป็นปกติอยู่แล้วนี่"

# emi "But this should feel different because before when we had lunch we were friends, and now we're a level above friends."
emi "แต่ก็ต้องรู้สึกไม่เหมือนเดิมถ้าให้เทียบกับตอนกินข้าวเที่ยงด้วยกันในฐานะเพื่อน เพราะตอนนี้เราเป็น\nมากกว่าเพื่อนแล้ว"

# hi "You sound like Rin."
hi "พูดอะไรเป็นรินไปได้"

show emicas happy
with charachange

# "Laughter escapes, and Emi grins."
"เอมิหัวเราะแล้วยิ้ม"

show emicas closedsmile_up
with charachange

# emi "Well, she might've put the thought into my mind."
emi "ก็นะ น่าจะเป็นรินนี่แหละที่ทำให้ฉันคิดเรื่องนี้"

show emicas closedsmile
with charachange

# emi "We've talked about that sort of thing before."
emi "ฉันเคยคุยเรื่องนี้กับรินนะ"

# hi "Really? About me?"
hi "จริงเหรอ เรื่องฉันน่ะนะ"

show emicas grin
with charachange

# emi "Not really. Just… stuff, really."
emi "ไม่เชิง แค่… เรื่องนั่นนี่น่ะ"

show emicas neutral
with charachange

# emi "Rin thinks that the change of a label from “friend” to “girlfriend” seems arbitrary most of the time."
emi "รินคิดว่าหลายครั้งการเปลี่ยนสถานะจาก “เพื่อน” เป็น “แฟน” ก็เป็นอะไรที่ทำตามใจไม่มีกฎตายตัว"

# emi "Like there's no difference between the two."
emi "เหมือนว่าสองอย่างนั้นก็ไม่ได้ต่างกันเลย"

# hi "I can think of at least one, you know."
hi "แต่ฉันคิดได้อย่างหนึ่งละ"

# hi "You don't tend to kiss your friends quite as much."
hi "ปกติคนเราไม่จูบกับเพื่อนกันบ่อยขนาดนั้น"

show emicas blush
with charachange

# "For the second time today, Emi blushes slightly and giggles."
"หน้าเอมิขึ้นสีแดงเรื่อก่อนเธอจะหัวเราะคิกคักเป็นครั้งที่สองของวัน"

show emicas closedsmile
with charachange

# emi "I suppose you're right."
emi "ก็คงจริงอย่างนายว่า"

# hi "Exactly. I'm always right about things like this."
hi "ใช่ เรื่องแบบนี้ฉันพูดถูกเสมอแหละ"

show emicas weaksmile_up
with charachange

# "Emi rolls her eyes and chuckles."
"เอมิกลอกตาแค่นหัวเราะ"

# emi "Guess you're pretty smart, huh?"
emi "ฉลาดน่าดูเลยนะนาย"

# "I nod in agreement."
"ฉันพยักหน้าเห็นด้วย"

# hi "Yep."
hi "อื้ม"

# hi "Even Mutou thinks so. He thinks I should go into some scientific study after graduation."
hi "ขนาดครูยังคิดงั้นเลย ครูอยากให้ฉันไปเรียนต่อทางวิทยาศาสตร์หลังเรียนจบ"

show emicas neutral
with charachange

# "Emi raises an eyebrow."
"เอมิเลิกคิ้ว"

# emi "Oh really?"
emi "จริงเหรอเนี่ย"

# hi "Yeah, I'm thinking I actually might do just that."
hi "อื้ม ก็คิดอยู่ว่าอาจจะไปตามอย่างที่ครูว่า"

# "Really, the more I consider the idea, the more it appeals to me."
"เอาจริง ๆ ยิ่งคิดก็ยิ่งรู้สึกสนใจขึ้นมา"

# "I make a mental note to look into it a little more closely."
"ฉันจดบันทึกไว้ในหัวว่าจะไปหาข้อมูลให้ละเอียดอีกหน่อย"

# hi "So what are you thinking of doing after graduation?"
hi "แล้วหลังเรียนจบเธอคิดจะทำอะไรต่อ"

# hi "Still planning on running?"
hi "จะวิ่งต่อมั้ย"

show emicas awayfrown
with charachange

# "Emi shrugs, seeming almost a bit hesitant."
"เอมิยักไหล่ เหมือนจะยังลังเลอยู่"

show emicas frown
with charachange

# emi "I dunno. If I'm good enough and I can find a team, I guess?"
emi "ไม่รู้สิ ถ้าเก่งพอแล้วหาทีมวิ่งอยู่ได้ก็คงวิ่งต่อมั้ง"

# hi "You mean you aren't sure?"
hi "เธอยังไม่แน่ใจเหรอ"

show emicas neutral
with charachange

# emi "I haven't… really thought about it, to be honest."
emi "ฉันไม่… ค่อยได้คิดเรื่องนั้นเท่าไหร่ ว่าตามตรง"

# hi "Really?"
hi "จริงเหรอ"

# hi "You probably should, you know. Graduation isn't that far off."
hi "เธอคิดไว้ก็ดีนะ อีกเดี๋ยวก็จะเรียนจบแล้ว"

show emicas awayfrown
with charachange

# "Emi fidgets a little nervously."
"เอมิบิดตัวไปมาด้วยความประหม่า"

# emi "Yeah, well… it's far enough, right?"
emi "อื้ม แต่ก็… ยังพอมีเวลานี่"

show emicas neutral
with charachange

# emi "Besides, I've got other things to think about."
emi "อีกอย่าง ฉันมีเรื่องอื่นให้คิดด้วย"

show emicas grin_up_close
with vpunch

# "There's a mischievous flash behind Emi's eyes, and I suddenly find myself gloriously pinned against the tree."
"รอยยิ้มเอมิเจือความซุกซน และอยู่ ๆ เอมิก็เข้ามาคร่อมตัวฉันไว้โดยหลังฉันแนบกับต้นไม้"

show emicas smile_up_close
with charachange

# emi "Like making sure this is a real date, right?"
emi "เช่น ต้องทำให้แน่ใจว่าเรามาเดตกันจริง ๆ ใช่มั้ย"

show emicas closedsmile_up_close
with charachange

# emi "I mean if we don't kiss then it's not a date at all, right?"
emi "ถ้าไม่จูบกันก็ไม่ใช่เดตน่ะสิ ใช่มั้ย"

# hi "I suppose s— mmmph." with vpunch
hi "ก็คงงั้— อื้อออ" with vpunch

# "Strawberries and curry. Not the best combination, but I don't think I mind."
"รสสตรอว์เบอร์รีกับแกงกะหรี่ ไม่ค่อยเข้ากันเท่าไหร่ แต่ฉันก็ไม่ถือ"

show emicas grin
with charadistant

# "Emi sits back on my legs and grins again."
"เอมินั่งทับขาฉันแล้วยิ้มอีกรอบ"

# emi "There. Science would approve, right?"
emi "นี่ไง เป็นไปตามหลักการวิทยาศาสตร์"

# "I have the oddest mental image of Mutou nodding seriously and making a mark on some checklist."
"อยู่ ๆ ก็นึกภาพประหลาดเห็นครูมุโต้พยักหน้าอย่างจริงจังแล้วติ๊กถูกกับรายการอะไรสักอย่าง"

# "I can't help laughing at the idea."
"ฉันอดหัวเราะกับภาพนั้นไม่ได้"

show emicas neutral
with charachange

# emi "Well I'll admit, this is the first time I've ever witnessed a kiss being met with laughter."
emi "โห ยอมรับเลยว่าเป็นครั้งแรกที่จูบแล้วเห็นอีกคนหัวเราะเนี่ย"

# emi "Should I feel offended?"
emi "จะให้โกรธดีไหม"

# hi "Heh, no, no."
hi "ฮะ ๆ ไม่ ๆ"

# hi "I'm sure science approves."
hi "เป็นไปตามหลักการวิทยาศาสตร์แหละ"

show emicas happy_up
with charachange

# "Emi beams at me, and I find it increasingly difficult to keep my brain functioning properly."
"เอมิส่งยิ้มให้จนฉันสมองฉันเริ่มทำงานเพี้ยนไปเรื่อย ๆ คุมไม่อยู่แล้ว"

# emi "Oh good!"
emi "ดีเลย!"

# "It is at this point I notice that Emi has stolen the remainder of my curry bread while I was otherwise occupied with images of teachers wielding clipboards."
"และเป็นตอนนี้เองที่ฉันเห็นว่าเอมิขโมยขนมปังแกงกะหรี่ของฉันที่เหลืออยู่ไปตอนที่ฉันมัวแต่นึกภาพครูถือ\nแผ่นกระดาน"

# hi "Hey!"
hi "นี่!"

show emicas blush
with charachange

# "Emi tries to look innocent, but considering she's just crammed the last bits of my bread into her mouth it does not appear to be working."
"เอมิทำตาใสซื่อ แต่ก็ปิดความผิดไม่มิดเพราะเธอเพิ่งจะยัดขนมปังคำสุดท้ายของฉันใส่ปากไป"

# emi "Mmph? F'orry, couln't refisft."
emi "อื๋อ? ออโอ้ดอี อดไอไอ้ไอ๋"

# hi "Thief!"
hi "ขโมย!"

show emicas neutral
with charachange

# "A shrug from my companion is all I get in response."
"อีกฝ่ายเพียงยักไหล่ตอบ"

# hi "You used your feminine wiles on me!"
hi "เธอเล่นมารยาหญิงใส่ฉัน!"

# "I wasn't that hungry anyway, but I still feel that the point needs to be made."
"ก็ไม่ได้หิวขนาดนั้นหรอก แต่รู้สึกว่าต้องทักสักหน่อย"

show emicas pout
with charachange

# "Emi seems confused by the phrase “feminine wiles,” but the understanding dawns on her features after a moment's thought."
"เอมิดูจะไม่เข้าใจคำว่า “มารยาหญิง” แต่คิดอยู่สักพักเธอก็ทำหน้าร้องอ๋อ"

show emicas angry_up
with charachange

# emi "Wasn't anything of the sort!"
emi "ไม่ใช่สักหน่อย!"

show emicas frown_up
with charachange

# emi "You were laughing! Feminine wiles don't involve laughing!"
emi "ก็นายหัวเราะ! มารยาหญิงไม่ได้ใช้การหัวเราะสักหน่อย!"

# "I guess I can't argue with this."
"ก็เถียงไม่ได้แหละนะ"

# hi "That doesn't change your thievery."
hi "แต่ที่เธอทำก็เป็นการลักทรัพย์อยู่ดี"

show emicas happy
with charachange

# "Emi laughs at my injured tone and gives me a playful shove."
"เอมิหัวเราะกับน้ำเสียงเจ็บปวดของฉันแล้วผลักตัวหยอก ๆ"

show emicas closedsmile
with charachange

# emi "Fine, you can have the instant noodles."
emi "ก็ได้ งั้นนายเอาบะหมี่กึ่งฯ ไปกินนะ"

# hi "Are you kidding? That stuff's terrible!"
hi "ล้อเล่นหรือเปล่า อร่อยก็ไม่อร่อย!"

# hi "If anything, you should definitely eat it as punishment!"
hi "เธอด้วยซ้ำที่ต้องกินโทษฐานขโมยของน่ะ!"

show emicas wink
with charachange

# "Another laugh from the girl sitting on my legs."
"เด็กสาวที่นั่งทับขาฉันอยู่หัวเราะอีกรอบ"

# "…Both of which have fallen asleep by now."
"…ซึ่งขาฉันทั้งสองข้างเหน็บกินไปแล้ว"

show expression im.Composite((295,1200), (0,0), "sprites/emicas/emicas_wink.png") as emicas:
   xalign 0.5 yanchor 0.5 ypos 1.13 subpixel True
   easeout 0.8 rotate -90
with None

show expression im.Composite((295,1200), (0,0), "sprites/emicas/emicas_blush.png") as emicas:
   xalign 0.5 yanchor 0.5 ypos 1.13 subpixel True
   easeout 0.8 rotate -90

with Dissolve(0.2)
with Pause(0.6)

hide emicas
with vpunch

# "I twitch one leg to try waking it up, which has the unintended effect of unbalancing Emi, who falls to the side with a startled “Eep!”"
"ฉันเขยื้อนขาหมายจะให้หายชา แต่ก็เผลอไปทำเอมิเสียการทรงตัวจนเธอตัวเอนไปแล้วร้อง “ว้าย!” ขึ้นมา"

# hi "Whoops! Sorry about that."
hi "โอ๊ะ! ขอโทษทีนะ"

# hi "Legs fell asleep on me."
hi "พอดีขาเป็นเหน็บน่ะ"

# "Emi remains on the ground, giggling."
"เอมิยังนอนอยู่กับพืื้นหัวเราะคิกคัก"

# "I stand up a little shakily, feeling the nerves in my legs return to normal."
"ฉันลุกขึ้นยืนตัวสั่นเล็กน้อย เลือดที่ขาเริ่มกลับมาเดินตามปกติแล้ว"

# "My eyes wander over the scenery before fixing on the figure of Emi, who has yet to get up."
"ฉันกวาดตามองทิวทัศน์โดยรอบก่อนจะมาหยุดมองอยู่ที่เอมิที่ยังไม่ลุก"

scene ev emi_parkback:
    xalign 0.5 yalign 0.5 zoom 1.1 subpixel True
    ease 10.0 zoom 1.0
with locationchange

# "Her hair is splayed out around her head, her arms are spread, and laughter is bubbling up through her mouth."
"ผมเอมิแผ่สยายไปรอบ ๆ เธอกางแขนออกแล้วหัวเราะออกมา"

# "Everything about Emi seems condensed into this one image."
"ทุกอย่างที่เป็นตัวเอมิคล้ายจะถูกจับมารวมไว้ในภาพนี้ภาพเดียวแล้ว"

# "Her energy, her spirit, her childish giggling."
"ทั้งบรรยากาศของเธอ นิสัยของเธอ เสียงหัวเราะอย่างเด็ก ๆ ของเธอ"

# "The urge to lay down on the grass with her rises swiftly from the back of my mind to the forefront of my thoughts, and indeed I am convinced that I would love nothing more than to do just that."
"ความอยากนอนกับพื้นหญ้าไปกับเอมิก่อตัวอย่างรวดเร็วก่อนจะผุดลอยขึ้นเด่นในความคิด และฉันก็อยาก\nทำอย่างนั้นขึ้นมาเลยจริง ๆ"

# "Unfortunately the sun has set, and it is probably time for us to get back to the dormitories."
"โชคไม่ดีที่ตะวันตกดินแล้ว และคงถึงเวลาแล้วที่เราจะต้องกลับหอ"

# "While Emi may be happy to stay out here all night, I don't think I have that ability."
"เอมิอาจจะยินดีอยู่ข้างนอกนี้ทั้งคืน แต่ฉันไม่น่าจะอยู่ได้"

# "Besides, homework soon beckons."
"อีกอย่าง ยังมีการบ้านที่รออยู่ด้วย"

# "It wouldn't make sense to start thinking about things like university and then slack off, would it?"
"มาคิดเรื่องเรียนต่อมหาวิทยาลัยแล้วอู้ก็คงใช่ที่"

# "I extend a hand to Emi to help her up."
"ฉันยื่นมือให้เอมิรั้งตัวเองขึ้นมา"

# hi "We should probably get going."
hi "ไปกันได้แล้วนะ"

show ev emi_parkback_frown
with charachange

# "Emi makes a sour face."
"เอมิทำหน้ายู่"

# emi "You're right."
emi "ถูกของนาย"

scene bg suburb_park
with locationchange

show emicas weaksmile_close:
    center
    ypos 1.2
    easein 0.5 ypos 1.0
with charaenter

# "She grabs my proffered hand, and I pull her to her feet and into a hug."
"เอมิจับมือฉันที่ยื่นออกไป ฉันดึงให้เอมิลุกขึ้นยืนแล้วกอดเธอไว้"

# "This time I'm the one who kisses her, unable to resist having Emi against me."
"คราวนี้เป็นฉันที่จูบเธอบ้างด้วยอดใจไม่ไหวที่เอมิอยู่ใกล้"

# hi "Seems a shame to leave, you know."
hi "ไม่อยากไปเลยเนอะ"

show emicas closedsmile_close
with charachange

# emi "Yeah, it does."
emi "อื้ม นั่นสิ"

show emicas grin_up_close
with charachange

# emi "But if we don't get back to the school soon, we'll probably get into trouble."
emi "แต่ถ้าไม่รีบกลับโรงเรียนเดี๋ยวเป็นเรื่องใหญ่แน่"

# "Emi pokes me in the ribs playfully."
"เอมิจิ้มสีข้างฉันหยอก ๆ"

show emicas wink_up_close
with charachange

# emi "And you need to do your homework, I'm sure."
emi "แล้วฉันรู้ว่านายก็ต้องทำการบ้านด้วย"

# hi "Sadly, you're absolutely right."
hi "น่าเสียดาย แต่ถูกของเธอ"

hide emicas
with charaexit

# "I throw my arm around her shoulders, and we make the trek back to the school, accompanied by occasional bouts of laughter as our conversation jumps from subject to subject."
"ฉันโอบไหล่เอมิไว้ เราออกเดินทางกลับโรงเรียนกัน โดยมีเสียงหัวเราะของเราคอยประกบไประหว่างที่\nเปลี่ยนเรื่องคุยกันไปเรื่อย ๆ"

# "Everything from running, to school, to the peculiar way that one of the cafeteria workers smells."
"ตั้งแต่เรื่องวิ่ง เรื่องโรงเรียน ยันเรื่องกลิ่นหนึ่งที่จะได้กลิ่นจากแม่ครัวในโรงอาหาร"

stop ambient fadeout 2.0

scene bg school_dormext_full
with locationskip

# "All too soon we find ourselves outside of the girls' dormitory building."
"ไม่นานเราก็มาถึงหน้าหอหญิง"

show emicas closedsmile at center
with charaenter

# emi "Well, I guess I'll be going, then."
emi "โอเค งั้นไปก่อนนะ"

# hi "I guess so, huh?"
hi "ก็คงงั้นแหละ"

show emicas grin_up
with charachange

# "Emi grins at me again with that mischievous look."
"เอมิยิ้มให้ฉันอีกรอบพลางทำหน้าซุกซน"

# emi "Are you going to be able to survive without me?"
emi "ไม่มีฉันแล้วนายอยู่ได้ใช่มั้ย"

# "I laugh."
"ฉันหัวเราะ"

# hi "I'm sure I'll manage."
hi "อยู่ได้แหละน่า"

show emicas pout_up
with charachange

# emi "How terrible! Aren't you supposed to say something like “I'll be counting the seconds you are away?”"
emi "ใจร้าย! นายต้องพูดอะไรแบบว่า “ฉันจะนั่งนับทุกวินาทีที่เธอไม่อยู่เลย” สิ"

# hi "Nah, I don't think so."
hi "ไม่อะ ไม่น่าหรอก"

show emicas closedsmile_close
with characlose

show emicas weaksmile
with charadistant

# "Emi pulls me down into a quick goodbye kiss and steps back, looking unexpectedly shy."
"เอมิรั้งตัวฉันเข้าไปจุ๊บส่งลาแล้วผละตัวออกไป เธอทำท่าทีอายผิดคาด"

# emi "Thanks for dinner."
emi "ขอบคุณสำหรับเย็นนี้นะ"

# emi "I really had fun."
emi "สนุกมากเลย"

show emicas closedsmile
with charadistant

# emi "Honestly, I did."
emi "สนุกจริง ๆ"

# hi "So did I."
hi "ฉันก็เหมือนกัน"

# hi "I think we shall have to do it again, sometime."
hi "ไว้หาเวลาไปด้วยกันอีกนะ"

show emicas happy
with charadistant

# "Emi laughs at my deadpan delivery and nods."
"เอมิหัวเราะที่ฉันพูดทำหน้าตายแล้วพยักหน้า"

# emi "See you bright and early tomorrow morning, right?"
emi "เจอกันพรุ่งนี้เช้าตรู่นะ"

show emicas wink
with charadistant

# emi "You've gotta run off that bread, after all."
emi "นายต้องไปวิ่งเอาขนมปังออกด้วย"

# hi "Of course. Despite the fact that you ate most of it."
hi "แหงสิ ถึงเธอจะกินไปเกินครึ่งก็เถอะ"

show emicas smile_up
with charadistant

# emi "Yes, despite that."
emi "ใช่ ถึงจะกินไปเกินครึ่ง"

show emicas grin_up
with charadistant

# emi "See you later, Hisao!"
emi "ไว้เจอกันนะฮิซาโอะ!"

stop music fadeout 3.0

show emicas invis:
    xpos 0.6
with dissolvecharamove

hide emicas
with None

# "As Emi turns to head inside, I notice something weird."
"เอมิหันหลังแล้วเดินออกไป แล้วฉันก็เห็นอะไรแปลก ๆ"

# "Something so weird that I'm surprised I didn't notice it earlier."
"แปลกมากจนนึกแปลกใจว่าทำไมก่อนหน้านี้ถึงไม่เห็น"

# "She's limping slightly, favoring the left leg."
"เอมิเดินขากะเผลกเล็กน้อย โดยลงน้ำหนักไปทางขาข้างซ้าย"

play music music_pearly fadein 8.0

# hi "Hey, Emi!"
hi "นี่ เอมิ!"

show emicas invis at tworight
with None

show bg school_dormext_full at bgleft
show emicas neutral at center
with dissolvecharamove

# emi "Hmm?"
emi "หืม"

# hi "Is your leg okay?"
hi "ขาเธอเป็นอะไรหรือเปล่า"

show emicas awayfrown
with charachange

# "Emi looks confused, or at least fakes confusion."
"เอมิทำหน้างง หรือไม่ก็อาจจะทำเป็นงงเฉย ๆ"

show emicas frown
with charachange

# emi "What are you talking about?"
emi "พูดอะไรของนาย"

# hi "Your right leg. You're limping."
hi "ขาขวาเธอน่ะ เห็นเดินกะเผลกอยู่"

show emicas blush
with charachange

show emicas frown
with charachange

# "There's the briefest flash of concern on Emi's face."
"เอมิทำหน้ากังวลขึ้นมาแวบหนึ่ง แวบเดียวจริง ๆ"

# "Either she didn't want me to know, or she didn't think I'd notice - or, I prefer to think, she just didn't realize it."
"ไม่รู้ว่าไม่อยากให้ฉันรู้หรือคิดว่าฉันจะไม่เห็น หรืออาจจะไม่รู้ตัวจริง ๆ ซึ่งฉันอยากให้เป็นอย่างหลังสุดมากกว่า"

show emicas neutral_up
with charachange

# emi "Oh, that."
emi "อ้อ ขาเหรอ"

# "She shrugs casually."
"เอมิยักไหล่สบาย ๆ"

show emicas awayfrown
with charachange

# emi "Must've gotten knocked a little out of alignment during the picnic."
emi "สงสัยจะเคลื่อนนิดหน่อยตอนไปปิกนิกมั้ง"

show emicas wink
with charachange

# emi "No idea what would have caused that, of course."
emi "แต่ไม่รู้หรอกนะว่าเป็นเพราะอะไร"

# "I think back to being pinned under the tree."
"ฉันย้อนนึกไปถึงตอนที่เอมิคร่อมตัวฉัน"

# hi "Ah."
hi "อ้อ"

# hi "You should have told me! We could have stopped and fixed it, you know."
hi "ทำไมไม่บอกฉันล่ะ! จะได้รอเธอจัดให้มันเข้าที่ก่อน"

# "Emi waves a hand airily."
"เอมิโบกไม้โบกมือเหมือนไม่มีอะไร"

show emicas smile_up
with charachange

# emi "Nah, it's not that big of a deal."
emi "ไม่อะ ไม่ใช่เรื่องใหญ่ขนาดนั้น"

show emicas weaksmile_up
with charachange

# emi "Don't worry about it, okay Hisao?"
emi "อย่าไปคิดมากเลยน่า นะ ฮิซาโอะ"

show emicas closedsmile_up
with charachange

# emi "It's fine."
emi "ไม่เป็นไรหรอก"

#Choice Tiem
#1. Press
#2. Rest

label th_choiceE17:
menu:
    with menueffect

    # "Why do I get the feeling that she's convincing herself as well as me?"
    "ทำไมถึงรู้สึกเหมือนเอมิจะบอกกับตัวเองไปด้วยเลยนะ"

    # "Press Emi.":
    "ตื๊อเอมิ":
        return m1

    # "Let it rest.":
    "ปล่อยไป":
        return m2


label th_E17a:
#If you press:

# hi "Are you absolutely sure?"
hi "แน่ใจแล้วจริง ๆ ใช่มั้ย"

# hi "You don't want to go ahead and adjust it before heading up the stairs?"
hi "ไม่ใช่ว่าก่อนขึ้นบันไดก็ไปจัดอีกทีนะ"

# hi "You could get hurt if you don't, right?"
hi "ถ้าไม่จัดเดี๋ยวก็เจ็บตัวเอาหรอก"

show emicas awayfrown_up
with charachange

# emi "I said it was fine, Hisao."
emi "ก็บอกแล้วไงว่าไม่เป็นไรน่ะฮิซาโอะ"

show emicas frown
with charachange

# emi "Seriously, don't worry about it."
emi "จริง ๆ นะ ไม่ต้องเป็นห่วงหรอก"

show emicas weaksmile
with charachange

# emi "I've got some experience in these matters, after all."
emi "ฉันก็พอมีประสบการณ์กับเรื่องพวกนี้อยู่บ้าง"

# hi "Yeah, I suppose so."
hi "อืม ก็คงงั้น"

# "Emi grins reassuringly."
"เอมิยิ้มคลายกังวลฉัน"

show emicas grin
with charachange

# emi "Honestly, Hisao, I appreciate the concern but I really am okay."
emi "ฉันดีใจนะที่นายเป็นห่วงฮิซาโอะ แต่ฉันไม่เป็นไรจริง ๆ"


label th_E17b:
#If you rest

# "Well, she's probably fine."
"ก็คงจะไม่เป็นไรแหละนะ"

# "I imagine she'd say something if it was really a problem."
"ถ้ามีปัญหาจริง ๆ ก็คงบอกไปแล้ว"

# "Heck, she'd probably get annoyed if I kept bringing it up."
"เผลอ ๆ ขืนจี้ถามเรื่อย ๆ แล้วจะรำคาญไปอีก"


label th_E17x:

show emicas smile
with charachange

# emi "Now really, I need to get going."
emi "โอเค ฉันต้องไปแล้วละ"

show emicas wink_up
with charachange

# emi "Your attempts to keep me around are doomed to fail!"
emi "ยังไงนายก็รั้งฉันไว้ไม่นานหรอก!"

# hi "Heh, of course."
hi "ฮะ ๆ แหงอยู่แล้ว"

# hi "Just prolonging the goodbye, I suppose."
hi "แค่อยากยื้อเวลาก่อนบอกลาละมั้ง"

# "Another grin lights up Emi's face."
"เอมิหยัดยิ้มอีกรอบ"

show emicas happy_up
with charachange

# emi "Goodnight, Hisao."
emi "ราตรีสวัสดิ์นะฮิซาโอะ"

# hi "Goodnight."
hi "ราตรีสวัสดิ์"

hide emicas
with charaexit

stop music fadeout 5.0

# "As she limps inside, I find myself hoping she's okay despite her assurances that she's fine."
"เอมิเดินขากะเผลกเข้าไปในตึก หวังว่าจะไม่เป็นอะไรจริง ๆ อย่างที่บอกให้ฉันสบายใจนะ"

# "I think I can call this a successful first date."
"คงนับได้ว่าเป็นเดตครั้งแรกที่ประสบความสำเร็จ"

# "Hell, any day that ends with Emi pinning me under a tree to kiss me can't be bad, can it?"
"ไม่สิ ถ้าได้ปิดท้ายด้วยการที่เอมิล็อกตัวจูบฉันใต้ต้นไม้แล้วจะวันไหนก็คงเป็นวันที่ดีทั้งนั้น"

# "I head back to my room, mentally thank the gods that Kenji doesn't ambush me in the hallway, and get started on my homework."
"ฉันกลับเข้าห้องไปพลางขอบคุณพระเจ้าในใจที่เคนจิไม่มาซุ่มดักรอฉันที่โถงทางเดิน จากนั้นฉันจึงทำการบ้าน"

scene black
with dissolve


########################

label th_E18:

scene bg school_dormhisao
with locationchange

play music music_night fadein 5.0

# "The morning is far too early for my taste."
"ตอนนี้นั้นเช้าเกินกว่าที่ฉันจะรับได้"

# "It doesn't help that I had trouble sleeping last night."
"แล้วยิ่งเมื่อคืนนอนไม่ค่อยหลับอีก"

# "There were simply too many things to think about. My mind refused to slow down."
"เพราะมีหลายเรื่องให้คิดเกินไป และสมองฉันก็ไม่ยอมหยุดทำงานด้วย"

# "Instead I replayed the rooftop, the park, and everything else over and over in my mind."
"กลับเอาแต่กรอภาพบนดาดฟ้า ในสวนสาธารณะ และอื่น ๆ อยู่ในหัวซ้ำแล้วซ้ำเล่า"

# "There's a small part of my mind that is still paranoid that this has all been some kind of joke."
"และยังมีเสี้ยวหนึ่งในใจที่ระแวงว่าเรื่องทั้งหมดนี้เป็นแค่การล้อเล่น"

# "That I'll meet up with Emi at the track, and she'll act like nothing happened yesterday."
"ว่าพอฉันไปเจอกับเอมิที่ลู่แล้วเธอก็จะทำตัวเหมือนเมื่อวานไม่มีอะไรเกิดขึ้น"

# "Pushing these thoughts to the back of my mind, I throw on my running clothes and open the door."
"ฉันเก็บความคิดนี้กลับไปฝังไว้ในส่วนลึกของจิตใจก่อนจะใส่เสื้อผ้าสำหรับวิ่งแล้วไปเปิดประตู"

scene bg school_track
show emi basic_grin_gym at center
with locationskip

# "Emi's waiting for me with her usual smile."
"เอมิคอยฉันอยู่พร้อมรอยยิ้มอย่างเคย"

show emi basic_annoyed_gym
with charachange

# emi "You're late!"
emi "มาช้านะนาย!"

show emi basic_closedgrin_gym
with charachange

# emi "Or at least, you're not early today."
emi "อาจจะไม่ได้ช้า แต่ก็ไม่ได้มาไวเหมือนทุกทีนะวันนี้"

show emi excited_hesitant_gym
with charachange

# emi "Are you tired or something?"
emi "รู้สึกเพลียหรืออะไร"

# "I find myself ruefully rubbing the back of my head."
"ฉันลูบท้ายทอยแก้เก้อ"

# hi "Something like that, yeah."
hi "ก็อะไรประมาณนั้น"

# hi "Lots to think about and all that."
hi "มีเรื่องหลายอย่างให้คิดแล้วก็อะไร ๆ น่ะ"

show emi basic_closedgrin_gym
with charachange

# "Emi giggles at my mild understatement."
"เอมิหัวเราะคิกคักกับคำพูดที่ยังเทียบไม่ได้กับความเป็นจริงเท่าไหร่ของฉัน"

show emi basic_grin_gym
with charachange

# emi "Yeah, I didn't sleep that well either."
emi "อื้ม ฉันก็นอนไม่ค่อยหลับเหมือนกัน"

show emi excited_proud_gym
with charachange

# emi "I was actually glad you weren't early, 'cause I wasn't early either."
emi "จริง ๆ ก็โล่งนะที่นายไม่ได้มาไว เพราะฉันก็มาช้าเหมือนกัน"

# "I wonder if the same thing kept us awake."
"ที่นอนไม่หลับเพราะคิดเรื่องเดียวกันอยู่หรือเปล่านะ"

# "The image of her weeping face passes through my mind."
"ฉันย้อนนึกถึงตอนที่เอมิร้องไห้"

# hi "What kept you up?"
hi "ทำไมนอนไม่หลับเหรอ"

show emi sad_shy_gym
with charachange

# "Emi's expression falters, but she quickly notices my curiosity and forces a smile."
"เอมิผงะไป แต่เธอก็เห็นว่าฉันสงสัยแล้วฝืนยิ้มออกมา"

show emi sad_grin_gym
with charachange

# emi "Nothing important."
emi "ไม่เรื่องสำคัญอะไรหรอก"

# "She's obviously not telling me something."
"ปกปิดอะไรไว้แน่ ๆ"

# "The question is, should I press the issue?"
"คำถามคือ ฉันควรจะซักไซ้ต่อหรือเปล่า"

# "Something's clearly been bothering her for a while."
"ชัดว่ามีเรื่องที่กวนใจเอมิมาสักพักแล้วอยู่"

# "I want to help her, but would it just come off as me being nosy?"
"ฉันอยากช่วยเอมิ แต่จะเป็นการสอดรู้เกินไปหรือเปล่า"

# "She's got to know I care about her, though."
"แต่ก็อยากให้เอมิรู้ว่าฉันเป็นห่วง"

# hi "Are you sure?"
hi "แน่ใจนะ"

# hi "If something's bothering you, I'm here to help you sort it out."
hi "ถ้าคิดมากเรื่องอะไรฉันก็คอยอยู่รับฟังจัดการปัญหาให้ได้นะ"

show emi basic_closedhappy_gym
with charachange

# "Emi laughs then, but it's not her usual laugh. There's an edge to it that seems almost bitter."
"เอมิหัวเราะ แต่ไม่ใช่เสียงหัวเราะอย่างทุกที ในน้ำเสียงเหมือนมีีความขื่นขมปนอยู่"

show emi sad_grin_gym
with charachange

# emi "Sort it out?"
emi "จัดการเหรอ"

# emi "I'm not sure it can be sorted out, Hisao."
emi "ฉันไม่ค่อยแน่ใจเท่าไหร่ว่ามันจะจัดการได้หรือเปล่านะฮิซาโอะ"

# "An almost grim smile crosses her lips."
"ริมฝีปากเธอหยัดยิ้มขื่น ๆ"

# "It's like a smile of resignation."
"เหมือนเป็นการยิ้มถอดใจ"

show emi sad_pout_gym
with charachange

# emi "I don't think you could help me, anyway."
emi "ฉันคิดว่ายังไงนายก็คงช่วยฉันไม่ได้หรอก"

# "That hurts."
"เจ็บจัง"

# "I don't want to say that it hurts to her, but it does."
"ไม่อยากบอกเอมิว่าคำพูดนั้นทำให้ฉันเจ็บปวดเลย แต่ก็เจ็บจริง ๆ"

# "Doesn't she realize I want to be there for her when things go wrong?"
"นี่เอมิไม่รู้เลยเหรอว่าฉันอยากอยู่เคียงข้างเธอยามที่มีปัญหาอะไร"

# hi "Well, I won't push you on the matter."
hi "เอาเถอะ ฉันจะไม่ซักไซ้ต่อแล้วกัน"

# hi "But I'm here for you if you decide later that you'd like to talk about it."
hi "แต่ถ้าวันหลังเธอนึกอยากคุยขึ้นมาฉันก็พร้อมอยู่เคียงข้างเธอเสมอนะ"

# hi "It might help."
hi "อาจจะพอช่วยได้บ้าง"

show emi sad_shy_gym
with charachange

# "I can see the debate raging behind Emi's eyes."
"ฉันเห็นผ่านแววตาเอมิว่าเธอกำลังเถียงกับตัวเองอยู่"

# "It seems like she wants to tell me, but she's not sure whether or not she can."
"เหมือนอยากจะบอกฉัน แต่ก็ยังไม่แน่ใจว่าบอกได้หรือเปล่า"

# hi "Hey, forget about it for now, okay?"
hi "เอ้า ช่างเรื่องนั้นก่อนแล้วกัน"

# hi "We've got running to do."
hi "เราต้องวิ่งกันนะ"

# "The mention of running, something that she can handle, brings Emi back to her usual self."
"พอพูดถึงเรื่องวิ่งที่เธอพอทำได้แล้วเอมิก็กลับมาเป็นตัวเธอคนเดิม"

show emi basic_closedhappy_gym
with charachange

# emi "Right!"
emi "อื้ม!"

show emi basic_grin_gym
with charachange

# emi "Hurry up and stretch out, Hisao!"
emi "รีบยืดเส้นยืดสายกันได้แล้วฮิซาโอะ!"

show emi excited_proud_gym
with charachange

# emi "We've got to get moving!"
emi "เราต้องขยับตัวกัน!"

play ambient sfx_emipacing

hide emi
with easeoutleft

stop ambient fadeout 3.0

# "She takes off like a shot, far quicker than I'm used to."
"เอมิออกวิ่งด้วยความรวดเร็ว เป็นความเร็วที่เร็วกว่าที่ฉันชิน"

scene bg school_track_on
with locationchange

scene bg school_track_running
with Dissolve(2.0)

# "Still, I try to keep pace with her, recklessly testing my limits."
"แต่ฉันก็คอยรักษาฝีเท้าให้เท่ากับเอมิทดสอบขีดจำกัดของตัวเองอย่างไม่คิดหน้าคิดหลัง"

# "It gives me a feeling of freedom, like my heart is no longer important."
"ซึ่งทำให้ฉันรู้สึกเป็นอิสระ เหมือนว่าหัวใจฉันไม่สำคัญอีกต่อไป"

# "I find myself wanting to laugh, filled with the feeling of moving beyond what I once called my boundaries."
"ฉันอยากหัวเราะออกมา ในอกเปี่ยมด้วยความรู้สึกดีที่ได้ก้าวข้ามเส้นที่ฉันเคยขีดไว้ว่าเป็นขอบเขตของตัวเอง"

# "The nurse's warnings to not overdo things echo in my mind, and I disregard them."
"เสียงคุณพยาบาลที่เตือนไม่ให้ฉันฝืนร่างกายมากไปสะท้อนก้องในหัว แต่ฉันก็เมิน"

# "This feeling I have, this willingness to risk a heart attack for something so trivial as a morning run, feels out of character for me."
"ความรู้สึกในอกนี้ ความเต็มใจที่จะยอมเสี่ยงหัวใจวายเพื่อเรื่องเล็ก ๆ อย่างการวิ่งยามเช้านี้นั้นช่างไม่สมเป็นตัวฉัน\nเอาเสียเลย"

# "But is it?"
"แต่เป็นอย่างนั้นจริงหรือ"

# "Or rather, should it be?"
"ไม่สิ ควรเป็นอย่างนั้นหรือเปล่า"

# "I've got a weak heart, sure."
"หัวใจฉันอ่อนแอ ใช่"

# "It'll never be capable of the kind of speed and endurance Emi's capable of."
"คงไม่มีวันไปแตะความเร็วกับความทนในระดับเดียวกันกับเอมิได้"

# "Though I probably wouldn't be able to get that good even if I had a healthy heart."
"แต่ต่อให้หัวใจฉันปกติดีก็คงไม่มีวันไปถึงจุดนั้นอยู่ดี"

stop music fadeout 6.0

# "As we round the final bend, I feel my legs screaming in protest, but for the first time, I ignore them."
"พอถึงโค้งสุดท้ายก็เริ่มปวดขาขึ้นมา แต่ครั้งนี้เป็นครั้งแรกที่ฉันไม่สนใจ"

# "I accelerate to finish at a sprint, nearly catching up to Emi."
"ฉันเร่งฝีเท้าเข้าเส้นชัยไปจนเกือบทันกับเอมิ"

# "That was never going to happen, of course."
"แน่ละว่าไม่มีวันทันแน่นอน"

# "Still, I feel surprisingly good."
"แต่ก็รู้สึกดีเหลือเชื่อ"

# "Oh sure, my legs feel like they're about to catch fire, and I'm having trouble staying upright."
"แน่อยู่แล้วว่าขาฉันนั้นร้อนจนเหมือนไฟลุก ฉันยืนแทบไม่ไหวอยู่แล้ว"

# "But there's been a shift of some sort today."
"แต่วันนี้มีบางอย่างที่เปลี่ยนไป"

# "And it's all thanks to the girl grinning at the finish line, waiting for me."
"ซึ่งทุกอย่างนั้นก็เป็นเพราะเด็กสาวที่ยืนรออยู่ตรงเส้นชัยส่งยิ้มให้ฉัน"

scene bg school_track_on
show emi basic_grin_gym at center
with locationchange

play music music_emi fadein 1.0

# hi "That felt a little faster than usual."
hi "รู้สึกเร็วขึ้นกว่าทุกทีนิดหน่อยนะ"

# "My comment is met with a grin and a shrug."
"เอมิยิ้มแล้วยักไหล่ตอบ"

show emi excited_proud_gym
with charachange

# emi "Can't have you think I was going to go soft on you, now can I?"
emi "ไม่งั้นเดี๋ยวนายก็หาว่าฉันอ่อนข้อให้อีก"

show emi basic_closedgrin_gym
with charachange

# emi "But you managed to handle it just fine."
emi "แต่นายก็วิ่งไหวนี่"

# hi "Well, I couldn't have done it without you."
hi "ก็นะ ถ้าไม่มีเธอฉันคงวิ่งไม่ไหวหรอก"

show emi basic_confused_gym_close
with characlose

# "Still feeling the high from the run and moved by a surge of gratitude, I seize Emi in a hug."
"ความรู้สึกดีหลังวิ่งยังคงค้างอยู่ ฉันรู้สึกยินดีเหลือเกินที่มีเอมิจึงเข้าไปกอดเธอ"

# hi "Thanks."
hi "ขอบคุณนะ"

# hi "Really, I'm not just saying that."
hi "ขอบคุณจริง ๆ ฉันไม่ได้พูดลอย ๆ"

# hi "I'm in your debt."
hi "ฉันติดหนี้บุญคุณเธอนะเนี่ย"

show emi basic_hes_gym_close
with charachange

# "Emi seems flustered by my words, squirming uncomfortably."
"เอมิดูจะเขินกับคำพูดฉัน เธอดิ้นไปมา"

# emi "Don't be silly, Hisao."
emi "พูดอะไรบ้า ๆ น่าฮิซาโอะ"

show emi basic_grin_gym_close
with charachange

# emi "Someone had to haul you out here, didn't they?"
emi "ยังไงก็ต้องมีคนคอยลากนายให้มาอยู่ตรงนี้ให้ได้อยู่แล้ว"

show emi basic_closedgrin_gym_close
with charachange

# emi "And it's not like you're not doing anything for me, right?"
emi "แล้วก็ใช่ว่านายจะได้ประโยชน์อยู่ฝ่ายเดียวสักหน่อย"

show emi basic_grin_gym_close
with charachange

# emi "I needed a running partner, remember?"
emi "ฉันก็ต้องมีคนมาวิ่งด้วยเหมือนกัน จำได้มั้ย"

show emi basic_shock_gym_close
with charachange

# "I shake my head, still pointedly not letting go of Emi, who stops squirming and merely looks up at me with a quickly deepening blush that almost seems out of character."
"ฉันสั่นหัวดื้อดึงไม่ยอมปล่อยเอมิที่ยังคงดิ้นและเงยหน้ามองฉัน เอมิหน้าแดงก่ำจนดูไม่สมเป็นตัวเธอ"

# hi "No, that's not true."
hi "ไม่ ไม่จริงสักหน่อย"

# hi "You wanted a running partner, but you didn't need one."
hi "เธอแค่อยากได้คนมาวิ่งด้วย ไม่ได้จำเป็นต้องมีคนวิ่งด้วย"

# hi "If I hadn't shown up the day after the festival, you would still run, right?"
hi "ถ้าหลังวันงานเทศกาลนั้นฉันไม่มาที่ลู่วิ่งเธอก็จะวิ่งอยู่ดี ใช่มั้ยล่ะ"

# hi "But it doesn't work the other way around."
hi "แต่กับฉันมันไม่ใช่อย่างนั้น"

# hi "I only managed to make it out a few times before the festival."
hi "ก่อนวันงานเทศกาลฉันมาวิ่งได้ไม่กี่ครั้งเอง"

# hi "And without you, I probably wouldn't have made it out at all after that."
hi "และถ้าไม่มีเธอ หลังจากนั้นฉันก็คงไม่มาวิ่งอีกเลย"

show emi basic_closedgrin_gym_close
with charachange

# "Emi smiles at me and prods my chest with one finger."
"เอมิยิ้มให้แล้วใช้นิ้วจิ้มหน้าอกฉัน"

show emi excited_proud_gym_close
with charachange

# emi "You are pretty lazy, Hisao."
emi "นายนี่ขี้เกียจนะฮิซาโอะ"

# hi "Hey, I was giving you a compliment!"
hi "เฮ้ย คนเขาอุตส่าห์ชม!"

show emi sad_grin_gym_close
with charachange

# emi "Well… you're welcome, I guess."
emi "ก็… ด้วยความยินดี ละมั้งนะ"

# hi "I'll pay you back somehow."
hi "ต้องหาทางตอบแทนเธอแล้ว"

show emi basic_hes_gym_close
with charachange

# emi "Oh, uh, well…"
emi "อ้อ อ่า เอ่อ…"

show emi basic_closedgrin_gym_close
with charachange

# emi "That's not necessary, you know."
emi "ไม่เห็นจำเป็นต้องตอบแทนเลย"

show emi basic_happyblush_gym_close
with charachange

# emi "I mean I kinda like you, Hisao."
emi "ก็ฉันชอบฮิซาโอะนี่"

show emi sad_grin_gym_close
with charachange

# emi "And being able to run with you in the mornings isn't exactly a bad deal for me either, so…"
emi "แล้วการที่ได้มาวิ่งกับนายในตอนเช้าก็นับว่าดีเหมือนกัน เพราะงั้น…"

# "For someone who gets so much praise, she seems unused to gratitude."
"เอมิดูจะไม่ชินกับคำขอบคุณทั้งที่เป็นคนได้รับคำชมบ่อย ๆ แท้ ๆ"

# "I can't think of anything else to say, so we fall silent."
"ฉันไม่รู้จะพูดอะไรอีกเราจึงเงียบกันไป"

# "I become aware of Emi's breathing, of the dampness of her clothing, and of the scent of her."
"ฉันรับรู้ถึงเสียงหายใจเอมิ สัมผัสได้ถึงความชื้นจากเสื้อผ้าเธอ ได้กลิ่นของเธอ"

# "Coming off of anyone else, it would stink."
"ถ้าเป็นคนอื่นก็คงเหม็น"

# "Coming off of Emi, it fits her in a way nothing else could."
"แต่พอเป็นเอมิแล้วก็เหมาะกับเธออย่างไม่มีอะไรอาจเทียบ"

# "Her skin is cool, slick with sweat, and a breeze causes goosebumps to rise."
"ผิวเอมิที่ชื้นเหงื่อนั้นเย็น ๆ พอลมโชยมาเธอก็ขนลุก"

show emi excited_amused_gym_close
with charachange

# "Almost without thinking about it, I lean down and meet Emi's mouth which has already moved to meet my own."
"ฉันโน้มตัวลงไปโดยแทบไม่ได้คิดอะไรแล้วทาบริมฝีปากกับเอมิที่เขย่งขึ้นมาหาฉันก่อนแล้ว"

# "Her lips are soft, and she hums happily as we kiss, sending vibrations from her mouth to mine."
"ริมฝีปากเอมินั้นนุ่ม เธอฮัมเสียงไปพลางจูบจนแรงสั่นส่งมาถึงปากฉัน"

# "There's a startling rightness to everything about this moment. We fit one another perfectly."
"ทุกอย่างช่างลงตัวอย่างเหมาะเจาะพอดี เราต่างเข้าคู่กันและกัน"

show emi basic_grin_gym_close
with charachange

# "The kiss ends, and I finally let my arms drop back to my sides."
"พอจูบเสร็จฉันก็ปล่อยมือออกมา"

show emi basic_closedgrin_gym_close
with charachange

# "Emi is smiling warmly at me and giggles again."
"เอมิยิ้มให้อย่างอบอุ่นแล้วหัวเราะคิกคัก"

show emi basic_closedhappy_gym
with charadistant

# emi "Come on Hisao, we'd better go see the nurse."
emi "โอเคฮิซาโอะ ไปหาพยาบาลกันได้แล้ว"

stop music fadeout 1.0

# "Then it happens."
"และแล้วก็เกิดเรื่อง"

show emi basic_closedhappy_gym:
   ease 0.25 ypos 1.05
   ease 0.25 ypos 1.0
with None

show emi excited_sad_gym:
   ease 0.25 ypos 1.05
   ease 0.25 ypos 1.0
with Dissolve(0.25)

# "As she turns to begin walking, she gives out a tiny yelp and stumbles forward."
"จังหวะที่เอมิออกเดินเธอก็ร้องอุทานแล้วสะดุดล้ม"

# hi "Emi!"
hi "เอมิ!"

play music music_rain fadein 2.0

show emi excited_sad_gym_close
with characlose

# "I leap to steady her and notice with some concern that she's favoring the same leg as last night."
"ฉันพุ่งตัวไปช่วยเอมิและเห็นว่าเธอยังเดินลงน้ำหนักกับขาข้างเดียวกันกับเมื่อคืนก่อน"

# hi "Your leg…"
hi "ขาเธอ…"

show emi basic_hes_gym
with charadistant

# "Emi seems panicked and pushes away from me."
"เอมิดูตื่นตระหนกแล้วผลักตัวฉันออก"

# emi "It's fine!"
emi "ไม่เป็นไรน่า!"

# "My expression must seem hurt, because she hastens to apologize."
"ฉันคงทำสีหน้าเจ็บปวดมากเอมิถึงรีบขอโทษขอโพย"

show emi basic_shock_gym
with charachange

# emi "Sorry! Sorry!"
emi "ขอโทษนะ! ขอโทษ!"

# emi "Didn't mean to push you like that!"
emi "ฉันไม่ได้ตั้งใจจะผลักนายเลย!"

show emi basic_closedsweat_gym
with charachange

# emi "I was just…"
emi "ฉันแค่…"

# "She stumbles for something to say."
"เอมิอ้ำอึ้งนึกหาคำพูด"

show emi sad_depressed_gym
with charachange

# emi "It's nothing, really."
emi "ไม่เป็นไรจริง ๆ"

# hi "Hey, don't worry about it."
hi "เอาน่า ไม่ต้องคิดมาก"

# "She's so flustered, I decide to shrug the whole thing off."
"เอมิดูร้อนรนจนฉันต้องยอมไม่สาวความอีก"

# "But there's a cold feeling in the pit of my stomach now that won't go away."
"แต่ในใจรู้สึกหน่วง ๆ ขึ้นมาแล้วไม่ยอมหาย"

# "I tried to step in and help her, and she pushed me away."
"ฉันอุตส่าห์เข้าไปช่วยเอมิ แต่เธอกลับผลักฉันออก"

# "Smiling, I shove those thoughts to the back of my mind and concentrate on Emi."
"ฉันยิ้มแล้วปัดความคิดนั้นทิ้งไปก่อนจะจดจ่ออยู่กับเอมิ"

# hi "I just don't want you getting hurt, that's all."
hi "ฉันแค่ไม่อยากให้เธอต้องเจ็บตัว"

show emi sad_pout_gym
with charachange

# emi "You don't have to worry about me, honest."
emi "นายไม่ต้องเป็นห่วงฉันหรอกน่า จริง ๆ นะ"

show emi sad_grin_gym
with charachange

# emi "I'm fine!"
emi "ฉันไม่เป็นไรหรอก!"

# "Yes, you say that, but I don't believe you."
"ใช่ ปากเธอก็พูดอย่างนั้น แต่ฉันไม่เชื่อหรอก"


label th_E18a:
#If you pressed

# "Why won't you tell me what's wrong?"
"ทำไมเธอถึงไม่ยอมบอกฉันว่าเป็นอะไรล่ะ"

# "It's like she gets offended by my trying to help."
"เหมือนไม่พอใจที่ฉันมาช่วยด้วยซ้ำ"

# "What am I supposed to make of that?"
"จะให้คิดว่ายังไงล่ะ"


label th_E18b:
#If you didn't press

# "I keep worrying about you regardless, and not saying anything yesterday just makes me feel guilty about today."
"ฉันยังทำให้เธอเป็นห่วง แล้วยิ่งเมื่อวานฉันไม่ได้พูดอะไร วันนี้ฉันก็ยิ่งรู้สึกผิดไปอีก"

# "I should have at least asked."
"รู้งี้อย่างน้อยถามไปก็ดี"

# "Would she have reacted the same way last night?"
"ถ้าถามไปตอนนั้นแล้วจะทำตัวเหมือนเดิมหรือเปล่า"

# "Guess I'll never know now."
"แต่ก็คงไม่มีวันได้รู้คำตอบแล้ว"


label th_E18x:

stop music fadeout 2.0

scene bg school_nursehall
with locationskip

# "I'm still trying to sort out what happened on the track as we arrive in front of the nurse's office."
"ฉันยังประมวลผลสิ่งที่เกิดขึ้นที่ลู่วิ่งอยู่ทั้งที่เรามาถึงหน้าห้องพยาบาลแล้ว"

# "Emi raises her hand to knock, hesitates and turns to me smiling guiltily."
"เอมิยกมือขึ้นหมายจะเคาะประตู แต่ก็ลังเลแล้วหันมาทางฉันและยิ้มให้อย่างรู้สึกผิด"

show emi sad_grin_gym:
    yalign 1.0 xanchor 0.5 xpos 0.47
    easein 0.5 center
with charaenter

# emi "Hey, can you do me a favor?"
emi "นี่ รบกวนอะไรนายหน่อยได้มั้ย"

# hi "Of course."
hi "ได้สิ"

show emi excited_proud_gym at center
with charachange

# emi "Can you tell the nurse that I'll see him later?"
emi "บอกคุณพยาบาลให้หน่อยได้มั้ยว่าเดี๋ยวฉันจะมาหาอีกที"

show emi basic_grin_gym
with charachange

# emi "I just remembered that I've got some… stuff to take care of before class."
emi "ฉันเพิ่งนึกได้ว่ามี… เรื่องที่ต้องจัดการก่อนไปเรียนน่ะ"

show emi sad_grin_gym
with charachange

# emi "So I really need to get moving."
emi "เลยต้องรีบไปก่อน"

show emi sad_shyblush_gym
with charachange

# "I peer at her closely, and she fidgets under my stare."
"ฉันจ้องเอมิใกล้ ๆ เธอบิดตัวไปมาเมื่อฉันมอง"

# "Yeah, she's clearly just avoiding the nurse."
"อืม แค่จะเลี่ยงไม่เจอคุณพยาบาลนั่นแหละ"

# "That leg of hers…"
"ขาข้างนั้น…"

# "Well, whatever. I said I'd help, and so I will."
"อืม ช่างเถอะ รับปากแล้วว่าจะช่วยก็ช่วยแล้วกัน"

# "But I'll make damn sure she sees the nurse before the day's out."
"แต่ต้องตามดูให้แน่ใจว่าก่อนหมดวันนี้เอมิจะมาหาพยาบาลจริง ๆ"

# hi "Yeah, okay. I'll let him know."
hi "อืม โอเค เดี๋ยวบอกให้"

show emi excited_smile_gym
with charachange

# "Emi looks like I've just given her a pony on Christmas."
"เอมิทำหน้าเหมือนฉันให้ตุ๊กตาม้าเป็นของขวัญวันคริสต์มาส"

show emi excited_joy_gym
with charachange

# emi "Thank you so much!"
emi "ขอบคุณมาก ๆ เลยนะ!"

show emi excited_amused_gym
with charachange

# emi "You're the best, Hisao!"
emi "นายนี่ดีที่หนึ่งเลยฮิซาโอะ!"

show emi excited_amused_gym_close
with characlose

# "I am rewarded for my complicity in her lie by a kiss that makes it all worth it, or so I tell myself."
"เอมิตอบแทนฉันที่ทำตามคำขอด้วยการจูบ ซึ่งเป็นรางวัลที่คุ้มค่าแล้ว ฉันบอกกับตัวเองว่าคุ้มอะนะ"

hide emi
with charaexit

# "As Emi heads out of the building, trying hard not to let her limp show, I knock on the door of the office."
"เอมิเดินออกอาคารไปพลางเก็บอาการไม่ให้ขากะเผลก ฉันเคาะประตูห้องพยาบาล"

# nk "Ah, Hisao. Come on in."
nk "อ้าว ฮิซาโอะ เข้ามาเลย"

play music music_nurse fadein 1.0

scene bg school_nurseoffice
show nurse neutral at center
with locationchange

# nk "I don't see Emi with you."
nk "เอมิไม่มาด้วยเหรอ"

show nurse fabulous
with charachange

# nk "She's not sick again, is she?"
nk "ไม่ได้ป่วยอีกแล้วใช่มั้ย"

# "From the tone of his voice, I don't think the nurse is expecting me to say “Yes, she's ill.”"
"ฟังจากน้ำเสียงแล้วคุณพยาบาลคงไม่ได้คิดว่าฉันจะตอบว่า “ครับ เอมิไม่สบาย”"

# hi "Er, she said that she'd forgotten to do something, and so she had to skip out, but she'll see you later today."
hi "เอ้อ เห็นบอกว่าลืมทำอะไรสักอย่างเลยไม่มาน่ะครับ แต่เดี๋ยวจะมาหาอีกทีภายในวันนี้"

show nurse concern
with charachange

# "The nurse heaves an exasperated sigh."
"คุณพยาบาลถอนหายใจพรืด"

# nk "Honestly, that girl…"
nk "เอาจริง ๆ นะ เอมิน่ะ…"

# hi "Hmm?"
hi "ครับ?"

show nurse neutral
with charachange

# nk "She's been avoiding me."
nk "เลี่ยงหน้าไม่ยอมเจอฉันอยู่"

# nk "Yesterday she was in and out of here without even taking off her prosthetics. And now this."
nk "เมื่อวานก็เข้ามาแล้วออกไปแบบไม่ได้ถอดขาเทียมเลยด้วยซ้ำ แล้ววันนี้ไม่ยอมมาเจออีก"

# "Well, at least it's not just me Emi doesn't want worrying."
"โอเค อย่างน้อยก็ไม่ได้มีแค่ฉันแล้วแหละที่เอมิไม่ได้อยากให้เป็นห่วง"

# "That's a… comfort, I guess."
"ก็… ค่อยโล่งหน่อย มั้ง"

# "Still, I feel like I should say something about her leg. I said I'd lie for her, but she really needs to see him."
"แต่ก็รู้สึกเหมือนต้องบอกอะไรคุณพยาบาลเรื่องขาเอมิอยู่ดี ฉันบอกเอมิไปว่าจะโกหกให้ก็จริง แต่เอมิต้องมาหา\nคุณพยาบาลจริง ๆ"

# hi "Now that you mention it, she was limping pretty badly today."
hi "จะว่าไป วันนี้ผมก็เห็นเอมิเดินขากะเผลกหนักมาก"

# hi "And last night as well."
hi "เมื่อคืนก็ด้วย"

show nurse concern
with charachange

# "The nurse's eyes narrow at the words “last night.”"
"คุณพยาบาลหรี่ตาเมื่อได้ยินคำว่า “เมื่อคืน”"

# nk "And what exactly were you two doing last night?"
nk "แล้วเมื่อคืนพวกเธอสองคนทำอะไรกัน"

# hi "We were uh, on a date."
hi "พวกเรา เอ่อ ไปเดตกันครับ"

show nurse fabulous
with charachange

# "The nurse raises his eyebrows as if surprised."
"คุณพยาบาลเลิกคิ้วขึ้นเหมือนประหลาดใจ"

# nk "Really? Interesting."
nk "จริงเหรอ น่าสนใจ"

# hi "Huh?"
hi "ครับ?"

show nurse neutral
with charachange

# nk "Oh, nothing."
nk "อ้อ ไม่มีอะไรหรอก"

# "His gaze turns thoughtful, and then he grins at me."
"แววตาคุณพยาบาลดูครุ่นคิด เขาหันมายิ้มให้"

show nurse grin
with charachange

# nk "You don't think you could use some of that boyfriend charm to get her to come see me today, could you?"
nk "ฉันพอจะรบกวนเธอให้ใช้เสน่ห์แฟนหนุ่มหว่านล้อมให้วันนี้เอมิมาหาฉันหน่อยได้มั้ย"

# hi "Of course!"
hi "ได้สิครับ!"

# hi "I was planning on doing that anyway."
hi "ผมก็กะจะทำอย่างนั้นอยู่แล้ว"

# hi "I think she's really hurt and just pretending she isn't."
hi "ผมว่าจริง ๆ แล้วเอมิก็เจ็บมาก แต่ทำเป็นไม่เป็นไรเฉย ๆ"

show nurse neutral
with charachange

# nk "Hmm, yes. She does that."
nk "อืมม ใช่ ตามนั้นแหละ"

# nk "Afraid I'll make her stop running."
nk "คงกลัวว่าฉันจะไปห้ามวิ่ง"

# hi "Will you?"
hi "แล้วคุณจะห้ามเหรอครับ"

show nurse concern
with charachange

# nk "I don't like to, but if it's bad enough that she's been limping, well…"
nk "ก็ไม่อยากห้ามหรอก แต่ถ้ามันหนักถึงขั้นเดินขากะเผลกก็…"

# nk "I guess I'll have to see what's wrong for myself before I make that call."
nk "ก็คงต้องดูก่อนว่าเป็นอะไรแน่แล้วค่อยว่ากันอีกที"

# hi "I see."
hi "อย่างนี้นี่เอง"

# "Emi, not allowed to run? Perish the thought."
"ห้ามวิ่ง กับเอมิน่ะนะ เลิกคิดไปได้เลย"

# "I don't know if she'd be able to function without running."
"ฉันไม่รู้ว่าเอมิจะมีชีวิตอยู่อย่างปกติได้หรือเปล่าด้วยซ้ำถ้าไม่ได้วิ่ง"

# "No wonder she's reluctant to admit anything's wrong."
"มิน่าล่ะถึงได้ไม่ยอมรับว่าเป็นอะไร"

# hi "Well, I'll make sure she sees you."
hi "ครับ ไว้เดี๋ยวผมไปชวนให้เอมิมาหาคุณให้ได้"

show nurse neutral
with charachange

# nk "Good. Oh, and before I forget…"
nk "ดีแล้ว อ้อ แล้วก็ก่อนจะลืม…"

show nurse grin
with charachange

# "He grins at me again in what feels like a vaguely threatening manner."
"คุณพยาบาลยิ้มให้ฉันซึ่งดูเหมือนกำลังข่มขู่อยู่หน่อย ๆ"

# nk "Don't forget that I know what medications you're on."
nk "อย่าลืมนะว่าฉันรู้ว่าเธอต้องกินยาอะไรบ้าง"

show nurse neutral
with charachange

# nk "You be careful around Emi, got it?"
nk "อยู่กับเอมิก็ทำตัวให้ดี ๆ ล่ะ เข้าใจนะ"

# "Wow. He looks serious, too."
"โห ทำสีหน้าจริงจังด้วย"

# hi "Got it."
hi "เข้าใจแล้วครับ"

# hi "Don't hurt Emi. Wouldn't dream of it."
hi "ห้ามทำร้ายเอมิ ผมไม่คิดจะทำร้ายเอมิแน่นอน"

show nurse grin
with charachange

# nk "Grand!"
nk "แจ่ม!"

show nurse fabulous
with charachange

# nk "I'd hate for you to be late."
nk "ฉันไม่อยากให้เธอสาย"

# hi "Huh?"
hi "ครับ?"

show nurse grin
with charachange

# nk "Late, as in the late Hisao Nakai."
nk "สาย สายตัวแทบขาด"

show nurse concern
with charachange

# "He frowns briefly, dissatisfied."
"คุณพยาบาลขมวดคิ้วอยู่ครู่หนึ่งดูไม่พอใจ"

# nk "Sounded better in my head…"
nk "ตอนคิดมันตลกกว่านี้นะ…"

show nurse neutral
with charachange

# nk "Well, at any rate."
nk "เอ้อ เอาเถอะ"

show nurse grin
with charachange

# nk "Get out of here before you miss your first class!"
nk "รีบไปได้แล้ว เดี๋ยวก็ไปไม่ทันคาบแรกหรอก!"

# nk "You've got things to do, I'm sure. Shoo!"
nk "เธอก็คงมีอะไรที่ต้องทำเหมือนกัน ชิ้ว!"

stop music fadeout 6.0

# "As I leave, I notice the nurse pulling out his phone and dialing a number."
"ระหว่างที่เดินออกจากห้องก็เห็นว่าคุณพยาบาลควักโทรศัพท์ออกมาแล้วกดเบอร์โทร. ต่อสาย"

show nurse concern
with charachange

# nk "Meiko, your daughter's being a pain in the ass again…"
nk "เมอิโกะ ลูกสาวเธอน่ะเอาอีกแล้วนะ…"

# "I'd better head back to my room, or I really will be late."
"รีบกลับห้องก่อนดีกว่า เดี๋ยวจะสายจริง ๆ"

# "Hey, wasn't he supposed to check my heart rate?"
"เฮ้ย ไม่ใช่ว่าคุณพยาบาลต้องตรวจอัตราการเต้นของหัวใจฉันก่อนเรอะ"


################################
label th_E19:

scene bg school_scienceroom
with shorttimeskip

play sound sfx_normalbell

# "The lunch bell sounds, and I bring myself out of the stupor I slipped into during the morning's classes."
"ระฆังพักเที่ยงดังดึงตัวฉันออกจากภวังค์ที่ฉันหนีไปอยู่ตอนเรียนคาบเช้า"

# "My lack of sleep last night, coupled with the increased pace of this morning's run, has left me a little exhausted."
"เมื่อคืนนอนไม่พอ แล้วเช้านี้ยังวิ่งเร็วกว่าทุกทีอีก ตอนนี้ถึงได้เพลียนิดหน่อย"

$ renpy.music.set_volume(0.15, 0.0, channel="ambient")
play ambient sfx_rooftop fadein 1.0

scene bg school_staircase1
with locationskip

# "Despite that, I find myself skipping stairs up to the roof."
"แต่ถึงอย่างนั้นฉันก็รีบเดินขึ้นบันไดมาที่ดาดฟ้า"

# "There's a thrill of excitement now, in addition to the pleasure one gets from eating lunch with one's friends."
"ตอนนี้มีความตื่นเต้นขึ้นมาแล้ว ไม่ได้มีแค่ความสบายใจที่ได้กินข้าวกับเพื่อน"

play sound sfx_door_creak
$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

scene bg school_roof
with locationchange

# "True, both Emi and Rin are still my friends, but Emi has become more than that now."
"จริงอยู่ว่าทั้งเอมิกับรินก็ยังเป็นเพื่อนฉัน แต่ตอนนี้เอมิเป็นมากกว่านั้นแล้ว"

# "Rin is back in her usual spot on the roof, almost as if she'd never been absent."
"รินกลับมาอยู่ที่ตำแหน่งประจำบนดาดฟ้าราวกับว่าครั้งก่อนยังมาตามปกติ"

scene ev rin_roof_boredom
show hisao rin_roof
with locationchange

# hi "Feeling better, I take it?"
hi "ดีขึ้นแล้วสินะ"

show ev rin_roof_surprised
with charachange

# "A raised eyebrow is my reward for speaking."
"รางวัลตอบแทนของการที่ฉันพูดคือคิ้วที่เลิกขึ้นของริน"

# rin "Better than what?"
rin "อะไรดีขึ้น"

play music music_rin fadein 6.0

# hi "Er, better than you felt yesterday."
hi "เอ่อ หมายถึงว่าอาการเธอดีขึ้นกว่าเมื่อวานหรือยัง"

show ev rin_roof_nonchalant
with charachange

# "Rin gives my question some serious thought."
"รินขบคิดคำถามนั้นอย่างจริงจัง"

# rin "I'm not sure."
rin "ไม่แน่ใจ"

# rin "I think I might have felt rather good for some of yesterday, but it's all fuzzy."
rin "ฉันว่าเมื่อวานก็เหมือนจะรู้สึกดีอยู่นะ แต่ก็มึน ๆ ไปหมด"

# hi "Too much cold medicine?"
hi "กินยาเยอะไปสิท่า"

show ev rin_roof_doubt
with charachange

# rin "Well, I was asleep. And that usually is pretty good."
rin "ก็ ฉันหลับ ปกติหลับแล้วก็สบายดี"

show ev rin_roof_boredom
with charachange

# rin "But I can't remember what it feels like to be asleep, because I'm not conscious for it."
rin "แต่ฉันจำไม่ได้ว่าตอนหลับรู้สึกยังไง เพราะฉันไม่ได้มีสติรู้ตัว"

# rin "It's a real problem."
rin "เป็นปัญหาใหญ่เลยละ"

show ev rin_roof_nonchalant
with charachange

# rin "Then again, if I knew how good it felt I might not sleep any more."
rin "แต่ก็นะ ถ้าฉันรู้ว่ารู้สึกดีแค่ไหนฉันก็คงไม่หลับอีกเลย"

# rin "But this way I keep trying so I guess that's how I can keep from being overtired."
rin "แต่พอเป็นแบบนี้แล้วฉันก็จะได้แต่เดา แล้วจะได้ไม่ต้องเพลียเกินไป"

# hi "An eternal mystery to keep you sleeping at night?"
hi "เป็นสิ่งลึกลับที่ไม่มีวันรู้ได้ที่เอาไว้คิดก่อนนอนงี้?"

show ev rin_roof_boredom
with charachange

# rin "Maybe mystery's the wrong word. Intangibility might be the proper way to describe it."
rin "คำว่าลึกลับอาจจะยังไม่ใช่ ถ้าจะเลือกคำให้เหมาะน่าจะเป็นคำว่าจับต้องไม่ได้มากกว่า"

# hi "I see."
hi "เข้าใจละ"

# "No, I don't see at all. I have no idea what she's talking about, but that's okay, since I rarely do."
"ไม่ ไม่เข้าใจเลย ไม่เข้าใจเลยว่ารินพูดอะไรอยู่ แต่ไม่เป็นไรหรอก ปกติก็แทบไม่เข้าใจอยู่แล้ว"

show ev rin_roof_doubt
with charachange

# rin "Do you remember what sleeping feels like?"
rin "นายจำได้มั้ยว่าความรู้สึกตอนหลับมันเป็นยังไง"

# rin "Like yesterday, do you remember what you felt like sleeping yesterday?"
rin "อย่างเมื่อวาน นายจำได้มั้ยว่าความรู้สึกตอนหลับเมื่อวานมันเป็นยังไง"

# hi "Well, I actually didn't get a lot of sleep yesterday."
hi "คือ เมื่อวานฉันนอนไม่ค่อยหลับน่ะ"

show ev rin_roof_nonchalant
with charachange

# rin "Hmm."
rin "อืมม"

# rin "Maybe that's because you remember subconsciously."
rin "อาจจะเพราะจิตใต้สำนึกนายจำได้ก็ได้"

# hi "Actually, I think I was worrying about Emi."
hi "จริง ๆ ฉันว่าเป็นเพราะฉันเป็นห่วงเอมิมากกว่า"

show ev rin_roof_surprised
with charachange

# rin "Doesn't Emi worry enough about herself?"
rin "แค่เอมิเป็นห่วงตัวเองยังไม่พออีกเหรอ"

# "I hadn't considered that, but it gives me pause."
"ฉันต้องชะงักเพราะไม่เคยคิดแบบนั้นมาก่อนเลย"

# hi "True, but would she ask for help if she needed it?"
hi "ก็จริง แต่ต่อให้เอมิต้องการความช่วยเหลือแล้วเอมิจะออกปากหรือเปล่า"

show ev rin_roof_doubt
with charachange

# "Rin frowns, and I raise an eyebrow. Will I get a proper answer?"
"รินขมวดคิ้ว ฉันเลิกคิ้ว นี่จะได้คำตอบดี ๆ ไหมเนี่ย"

# rin "Probably not. Is there something she should be asking for help with?"
rin "คงจะไม่ เอมิมีเรื่องอะไรที่ต้องขอความช่วยเหลือด้วยเหรอ"

# hi "Her leg, for starters."
hi "เช่นว่า ขาเอมิไง"

# "This seems to catch Rin's interest."
"เหมือนรินจะสนใจคำตอบนั้น"

show ev rin_roof_disgust
with charachange

# rin "Leg?"
rin "ขา?"

# hi "It's hurt, but she won't see the nurse about it."
hi "เอมิเจ็บขาแต่ไม่ยอมไปหาคุณพยาบาล"

# "Rin shakes her head in disapproval."
"รินสั่นหัวด้วยความรับไม่ได้"

show ev rin_roof_doubt
with charachange

# rin "You have to make her."
rin "นายต้องไปลากเอมิ"

show ev rin_roof_nonchalant
with charachange

# rin "Like she makes me go to class. For her own good."
rin "เหมือนที่เอมิลากฉันให้ไปเรียน เพื่อตัวของเอมิเอง"

# rin "Otherwise she could lose her legs again, and that's just too weird."
rin "ไม่อย่างนั้นเอมิอาจจะเสียขาอีกรอบ ซึ่งก็จะแปลกเกินไป"

# rin "Losing things twice."
rin "การเสียอะไรบางอย่างสองครั้ง"

show ev rin_roof_doubt
with charachange

# rin "Especially if you don't find them again to begin with."
rin "แล้วยิ่งเป็นของที่เอากลับคืนมาไม่ได้ด้วย"

# rin "Unless prosthetics are the same as finding something."
rin "เว้นเสียแต่ว่าขาเทียมจะนับเป็นการเอากลับคืนมา"

show ev rin_roof_nonchalant
with charachange

# rin "But that's a different kind of lost, isn't it?"
rin "แต่ก็จะเป็นการสูญเสียคนละแบบอีกใช่มั้ย"

# hi "I think so."
hi "คิดว่านะ"

show ev rin_roof_boredom
with charachange

# rin "Hmm. I wonder…"
rin "อืมม อยากรู้ว่า…"

stop music fadeout 0.5

show emi rin_roof
with charaenter

# emi "Wonder what?"
emi "อยากรู้อะไร"

scene bg school_roof
show emi basic_grin at center
with locationchange

# "Emi seems to have snuck up on Rin and me, though Rin doesn't seem especially surprised. Which is itself unsurprising, I suppose."
"เหมือนว่าเอมิจะแอบย่องเข้ามาหารินกับฉัน แต่รินดูจะไม่แปลกใจอะไร ซึ่งก็คงไม่ได้น่าแปลกใจละมั้ง"

show bg school_roof at bgleft
show emi basic_grin at twoleft
with charamove

show rin basic_deadpannormal:
    tworight
    ypos 1.25
    easein 0.5 ypos 1.2
with charaenter

# "Rin manages to sit herself upright quite expertly, throwing her upper body forward and using her momentum to right herself."
"รินลุกกลับขึ้นมานั่งหลังตรงได้อย่างคล่องแคล่วโดยเหวี่ยงตัวเองขึ้นแล้วใช้แรงที่ส่งมาจัดท่าตัวเอง"

show rin basic_absent:
    ypos 1.2
with charachange

# hi "Your leg. How's it feel?"
hi "ขาเธอ เป็นยังไงบ้าง"

show emi sad_annoyed
show rin basic_awayabsent
with charachange

# "That earns me a frown and a bit of a glare."
"ฉันได้รับการขมวดคิ้วกับการจ้องหน้าเป็นคำตอบ"

# emi "It's okay, I think."
emi "ก็โอเคแหละ คิดว่านะ"

show emi sad_shy
with charachange

# emi "Not worth worrying about."
emi "ไม่มีอะไรน่าห่วงหรอก"

show rin basic_absent
with charachange

# hi "Tell that to the nurse."
hi "เอาไปบอกคุณพยาบาลนะ"

# hi "He's quite insistent that you visit him, you know."
hi "คุณพยาบาลอยากให้เธอไปหามากนะรู้มั้ย"

show emi sad_pout
show rin basic_awayabsent
with charachange

# "Emi pouts like I've just told her she's been grounded."
"เอมิทำแก้มป่องเหมือนฉันเพิ่งบอกว่าจะกักบริเวณเธอ"

# emi "He worries too much."
emi "คุณพยาบาลน่ะขี้กังวลเกินไป"

show emi basic_grin
with charachange

# emi "It's not a big deal, just a little soreness."
emi "ก็ไม่ใช่เรื่องใหญ่สักหน่อย แค่ปวดนิด ๆ หน่อย ๆ เอง"

# "I try to resist rolling my eyes in exasperation."
"ฉันกลั้นใจไม่ให้กลอกตาไปด้วยความอิดหนาระอาใจ"

show rin basic_absent
with charachange

# hi "If it's nothing, then you should have no problem seeing him, right?"
hi "ถ้าไม่เป็นอะไรก็น่าจะไปหาได้นี่ จริงมั้ย"

show emi basic_annoyed
show rin basic_awayabsent
with charachange

# "Emi narrows her eyes suspiciously."
"เอมิหรี่ตามองอย่างสงสัย"

# emi "Did he put you up to this?"
emi "นี่คุณพยาบาลใช้ให้นายมาจี้ฉันหรือเปล่า"

show rin basic_absent
with charachange

# hi "Well, maybe. A little."
hi "ก็ มั้ง นิดหน่อย"

# hi "But that's not the point. I would have reminded you to see him anyway."
hi "แต่ประเด็นไม่ใช่ตรงนั้น เพราะยังไงฉันก็คงมาบอกให้เธอไปหาคุณพยาบาลอยู่ดี"

# hi "It would be terrible to see you really hurt and not doing anything about it."
hi "จะให้ฉันอยู่เฉยปล่อยให้เธอเจ็บหนักอย่างนี้ได้ไงล่ะ"

# hi "That would make it worse, and I don't really want to see you hurt, you know?"
hi "ขืนปล่อยไว้อาการก็จะยิ่งแย่ไปอีก แถมฉันไม่อยากเห็นเธอบาดเจ็บด้วย"

# hi "Call me crazy, but I kinda would prefer to see you happy and healthy."
hi "จะหาว่าฉันบ้าก็ได้ที่อยากเห็นเธอมีความสุขอย่างสุขภาพดีมากกว่าน่ะ"

show emi sad_grin
show rin basic_awayabsent
with charachange

# "With each statement, Emi's frown fades a little more, until eventually she's grinning, albeit a little shyly."
"เอมิคลายปมคิ้วที่ขมวดอยู่ออกเรื่อย ๆ กับทุกประโยคที่ฉันพูด จนในที่สุดเธอก็ยิ้มอาย ๆ"

play music music_daily fadein 4.0

# emi "Well, if you're going to put it that way, then I guess I'll have to see him."
emi "อืม ถ้านายว่าอย่างนี้แล้วฉันก็คงต้องไปหาคุณพยาบาลแล้วละ"

show emi excited_proud
with charachange

# emi "Otherwise you'll keep worrying, and then I'll never hear the end of it, right?"
emi "ไม่อย่างนั้นนายก็จะเป็นห่วงฉันอยู่เรื่อย ๆ แล้วก็จะบ่นจนฉันหูชาสินะ"

show rin basic_absent
with charachange

# hi "That's right. I'll keep bugging you about it, and that might put a damper on our dates."
hi "ใช่ ฉันจะเอาแต่ตื๊อเธอ เดตของเราอาจกร่อยไปเลยก็ได้"

#"I launch into a series of back-and-forths, playing the role of myself and Emi."

# hi "“How's the food, Hisao?” “Talk to the nurse, Emi.”"
hi "“อาหารเป็นยังไงบ้างฮิซาโอะ” “ไปหาคุณพยาบาลนะเอมิ”"

# hi "“How was your day, Hisao?” “Talk to the nurse, Emi.”"
hi "“วันนี้นายเป็นไงบ้างฮิซาโอะ” “ไปหาคุณพยาบาลนะเอมิ”"

# hi "“Hisao, I think I'm ready to go all the w—” “{b}Talk to the nurse, Emi.{/b}”"
hi "“ฮิซาโอะ ฉันว่าฉันพร้อมที่จะไปให้สุ—” “ไปหาคุณพยาบาลนะเอมิ!”"

# hi "See? It doesn't work that well."
hi "เห็นมั้ย ไปได้ไม่สวยเลย"

show emi basic_closedhappy
show rin basic_awayabsent
with charachange

# "Emi giggles at my high-pitched rendition of her own voice and gives me an affectionate shove."
"เอมิหัวเราะคิกคักที่ฉันล้อเสียงเธอแบบสูงแหลมแล้วผลักฉันด้วยความเอ็นดู"

show emi excited_amused
with vpunch

# emi "My voice isn't that high, jerk."
emi "เสียงฉันไม่ได้สูงขนาดนั้นสักหน่อย ตาบ้า"

show rin basic_deadpan
show emi excited_circle
with charachange

# rin "I thought it was pretty accurate."
rin "ฉันว่าก็เหมือนอยู่นะ"

with Pause(3.0)

# "Emi and I stare at Rin for a while before I burst into laughter."
"เอมิกับฉันจ้องรินอยู่พักหนึ่งก่อนจะระเบิดหัวเราะออกมา"

show emi sad_annoyed
show rin basic_awayabsent
with charachange

# "Emi crosses her arms and huffs, mock-offended."
"เอมิกอดอกทำเสียงฮึดฮัดแสร้งทำไม่พอใจ"

show emi sad_angry
with charachange

# emi "You're both jerks."
emi "เธอสองคนนี่บ้ากันทั้งคู่"

show rin basic_absent
with charachange

# hi "Such vile calumnies from you, young woman."
hi "คำพูดคำจาเธอนี่นะ"

# hi "I'm stunned that you would call me, of all people, a jerk."
hi "ฉันตกใจจริง ๆ ที่เธอมาเรียกฉันว่าบ้าได้ลง"

# hi "Honestly, I just… I don't know what to think."
hi "เอาตรง ๆ นะ ฉัน… ไม่รู้จะว่ายังไงดี"

show emi basic_annoyed
show rin basic_awayabsent
with charachange

# "Emi sticks her tongue out at me."
"เอมิแลบลิ้นใส่"

# emi "You ass."
emi "ใจร้าย"

show emi basic_grin
with charachange

# emi "So Rin, how's the art club these days?"
emi "นี่ริน ช่วงนี้ชมรมศิลปะเป็นยังไงบ้าง"

show rin basic_surprised
with charachange

# "Rin, seemingly as surprised by this sudden change of topic as I am, takes a minute to think before answering."
"รินดูจะแปลกใจพอ ๆ กันกับฉันที่อยู่ ๆ เอมิก็เปลี่ยนเรื่องแบบนี้ รินคิดอยู่สองสามนาทีก่อนจะตอบ"

show rin basic_lucid
with charachange

# rin "I believe it is okay."
rin "ฉันว่าก็โอเคดี"

show rin basic_deadpancontemplation
with charachange

# rin "Although Nomiya keeps telling me to work harder."
rin "ถึงโนมิยะจะเอาแต่บอกให้ทุ่มเทให้มากขึ้นก็เถอะ"

show rin relaxed_nonchalant
with charachange

# rin "But I don't think he understands my methods."
rin "แต่ฉันว่าโนมิยะไม่เข้าใจวิธีการของฉันหรอก"

show emi sad_annoyed
with charachange

# emi "He always struck me as slightly creepy."
emi "ฉันว่าครูโนมิยะก็ชวนให้ขนลุกหน่อย ๆ นะ"

show rin basic_lucid
with charachange

# "Rin ponders this statement for a while."
"รินพินิจประโยคนั้นอยู่พักหนึ่ง"

show rin basic_awayabsent
with charachange

# rin "I've never really noticed."
rin "ไม่เคยสังเกตเลย"

show rin basic_deadpancontemplation
with charachange

# rin "But I don't pay much attention to him most days, so maybe that's why."
rin "แต่ปกติฉันก็ไม่ค่อยได้สนใจเท่าไหร่ ก็เลยไม่เคยสังเกต"

# hi "How often do you meet?"
hi "ปกติทำกิจกรรมชมรมกันบ่อยมั้ย"

show emi basic_closedgrin
with charachange

# emi "Thinking of joining, Hisao?"
emi "อยากเข้าชมรมศิลปะเหรอฮิซาโอะ"

show rin basic_absent
with charachange

# hi "What? Nah, I've already decided to join a club."
hi "ฮะ? ไม่อะ ฉันมีชมรมที่จะเข้าแล้ว"

show emi excited_happy
show rin basic_awayabsent
with charachange

# emi "Really? Which one?"
emi "จริงเหรอ ชมรมอะไร"

show rin basic_absent
with charachange

# hi "Well, it's not really much of a club, to be honest…"
hi "ก็ ไม่เชิงว่าชมรมหรอกถ้าให้พูดตามตรง…"

show emi excited_proud
show rin basic_awayabsent
with charachange

# emi "Oh, you joined the tea club?"
emi "อ้อ ชมรมน้ำชาเหรอ"

show rin basic_absent
with charachange

# hi "No, I uh… joined the science club… I think."
hi "เปล่า ฉัน เอ่อ… เข้าชมรมวิทยาศาสตร์… มั้งนะ"

show emi basic_confused
show rin basic_awayabsent
with charachange

# "Emi looks highly confused."
"เอมิดูงุนงง"

# emi "We have a science club?"
emi "เรามีชมรมวิทยาศาสตร์ด้วยเหรอ"

show rin basic_absent
with charachange

# hi "Er, not really. It's just me."
hi "เอ่อ ก็ไม่เชิง สมาชิกมีแค่ฉัน"

show emi basic_closedhappy
show rin basic_awayabsent
with charachange

# emi "Hisao, that's not a club. That's sitting in your room reading books."
emi "แบบนั้นก็ไม่ใช่ชมรมสิฮิซาโอะ อันนั้นเขาเรียกว่าการนั่งอ่านหนังสืออยู่ในห้องเฉย ๆ"

# hi "No, I mean it's just me and Mutou."
hi "ไม่ จริง ๆ คือมีฉันกับครูมุโต้"

# hi "I'm just the only student so far."
hi "ตอนนี้นักเรียนในชมรมมีแค่ฉัน"

show emi basic_confused
show rin basic_lucid
with charachange

# emi "Mutou? Really?"
emi "ครูมุโต้ จริงเหรอ"

# "A thought strikes her."
"แล้วเอมิก็นึกอะไรออก"

show emi basic_happy
with charachange

# emi "Oh, is that what you were talking about yesterday? Your meeting with Mutou?"
emi "อ้อ เนี่ยเหรอที่นายพูดถึงเมื่อวาน ที่ว่าไปคุยกับครูมุโต้น่ะ"

# hi "Yeah, that was our first meeting, I guess."
hi "อื้ม ก็นับว่าเป็นกิจกรรมชมรมครั้งแรกละมั้ง"

show emi basic_closedgrin
with charachange

# "Emi giggles."
"เอมิหัวเราะคิกคัก"

show emi basic_grin
with charachange

# emi "Nerd."
emi "ตาคงแก่เรียนเอ๊ย"

# hi "Hey, I can't help being clever."
hi "เฮ้ย ก็คนมันฉลาดนี่"

show emi excited_proud
with charachange

# emi "You know, I could have used your help years ago."
emi "นี่นะ ถ้าเป็นสองสามปีก่อนนายคงมาช่วยฉันได้"

# emi "You should've had your heart attack earlier in life, Hisao."
emi "นายน่าจะหัวใจวายให้เร็วกว่านี้นะฮิซาโอะ"

# "I laugh, and then realize this is probably one of the very rare times I've laughed about my heart attack."
"ฉันหัวเราะ แล้วก็นึกขึ้นได้ว่าครั้งนี้คงจะเป็นหนึ่งในไม่กี่ครั้งที่ฉันหัวเราะกับเรื่องหัวใจวายของตัวเอง"

# hi "Hindsight…"
hi "แต่พอมาคิดอีกที…"

show emi sad_grin
with charachange

# emi "Yeah…"
emi "อื้ม…"

play sound sfx_warningbell

# "The ringing of the bell ends our conversation."
"เสียงระฆังดังตัดบทสนทนาของเรา"

# hi "Hmm, guess we'd better go."
hi "อืมม ไปกันเถอะ"

show emi basic_grin
with charachange

# emi "Yeah, I guess so."
emi "อื้ม ไปกัน"

show emi excited_amused:
    xpos 0.45
with dissolvecharamove

# emi "Come on Rin, you too."
emi "ปะริน มาด้วยกันสิ"

show rin basic_surprised
with vpunch

# "Rin has apparently begun to doze off, so Emi gives her a sharp bump."
"เหมือนรินจะม่อยหลับไปแล้ว เอมิกระทุ้งตัวริน"

show rin basic_deadpanupset
with charachange

# rin "I almost had it."
rin "เกือบแล้วเชียว"

show emi basic_closedgrin
with charachange

# emi "Sorry, but you need to go to class."
emi "ขอโทษที แต่เธอต้องไปเรียนแล้วนะ"

show rin relaxed_nonchalant at tworight
with dissolvecharamove

# rin "I disagree, but maybe if I nap in class I'll get it this time."
rin "ขอคัดค้าน แต่ถ้าไปงีบในห้องน่าจะข้ามคำว่าเกือบได้แล้ว"

show rin relaxed_boredom
with charachange

# rin "Changing location is sometimes helpful for that kind of thing."
rin "ของแบบนี้บางทีเปลี่ยนที่อยู่บ้างก็จะช่วยได้เหมือนกัน"

# "Neither Emi or I bother asking what “it” is."
"ทั้งเอมิทั้งฉันต่างก็ไม่คิดจะถามว่าเกือบที่ว่าคือเกือบอะไร"

stop music fadeout 3.0
stop ambient fadeout 2.0
scene bg school_hallway3
with locationskip

# "As we arrive at my classroom, Emi gives me a quick kiss and heads down the hallway, Rin in tow."
"พอมาถึงห้องเรียนของฉันแล้วเอมิก็จุ๊บฉันก่อนเดินไปตามโถงทางเดินโดยมีรินตามไป"

show shizu behind_blank:
    tworight
    xpos 0.8
    easein 0.5 tworight
show misha perky_smile:
    twoleft
    xpos 0.2
    easein 0.5 twoleft
with charaenter

# "I turn to enter the classroom, to be met by the duo of Shizune and Misha."
"ฉันหันไปเตรียมจะเข้าห้องเรียน แล้วก็พบกับคู่หูชิซูเนะกับมิช่า"

play music music_shizune fadein 1.0

show shizu adjust_happy
with charachange

shi "…"

# "Misha seems to be fighting a losing battle to keep from breaking into a fit of giggles while she translates Shizune's latest rant."
"มิช่าดูจะกลั้นใจแทบตายไม่ให้หัวเราะคิกคักไปพลางตอนที่แปลบทเทศน์ของชิซูเนะเมื่อครู่"

show misha hips_grin
with charachange

# mi "While we are pleased, nay thrilled, to see how well you've managed to make new friends and forge relationships - and with such a cutie too, Hicchan~…"
mi "พวกเรายินดีและประทับใจเป็นอย่างยิ่งที่ได้เห็นคุณมีเพื่อนใหม่และได้สานสัมพันธ์ครั้งใหม่ แถมไปสานสัมพันธ์\nกับคนน่ารักซะด้วยนะฮิจัง~…"

# "I think that last part was probably Misha."
"ฉันว่าอย่างหลังนี่มิช่าน่าจะพูดเอง"

show shizu basic_normal
with charachange

shi "…"

show misha hips_frown
with charachange

# mi "We nevertheless feel compelled to politely remind you that public displays of affection are strictly forbidden - really? That's disappointing, Shicchan - by section eight of the code of conduct laid out in the student handbook."
mi "แต่แม้กระนั้น พวกเราก็ต้องขอแจ้งให้คุณทราบอีกครั้งว่าทางโรงเรียนขอห้ามแสดงความรักในที่สาธารณะ\nอย่างเด็ดขาด จริงเหรอ ผิดหวังนะเนี่ยชิจัง ตามมาตราแปดของจรรยาบรรณที่ระบุไว้ในคู่มือนักเรียน"

show shizu adjust_smug
with charachange

shi "…"

show misha sign_smile
with charachange

# mi "In this case, however, ignorance of the law may be your excuse, as we are feeling lenient…"
mi "ทว่าในกรณีนี้คุณอาจอ้างความไม่รู้กฎหมาย และเราก็อยากลดหย่อนผ่อนปรน…"

show shizu behind_smile
with charachange

shi "…"

show misha hips_smile
with charachange

# mi "…and the paperwork required to punish the both of you would only add to the already mountainous volume of work which confronts us, the sole members of the Student Council - and besides, you two are adorable together~!"
mi "…และเอกสารที่ต้องใช้ในกระบวนการเอาผิดพวกคุณทั้งสองคนจะยิ่งทำให้งานที่กองกันเท่าภูเขาที่เรา\nในฐานะสมาชิกสภานักเรียนต้องจัดการมีมากขึ้นไปอีก และอีกอย่างเธอสองคนอยู่ด้วยกันแล้วก็น่ารักดี~!"

show shizu adjust_happy
with charachange

shi "…"

show misha hips_grin
with charachange

# mi "Therefore consider this a formal warning, and please refrain from such displays in the future. At least when Shizune can see you, Hicchan~!"
mi "ดังนั้น ขอให้รับรู้ว่านี่คือคำเตือนอย่างเป็นทางการจากพวกเรา และภายภาคหน้าขออย่าทำเรื่องแบบนี้อีก\nอย่างน้อยก็ไปทำลับหลังชิซูเนะนะฮิจัง~!"

# "This whole spiel is so patently ridiculous that I can't help but reply in the same pompous manner."
"บทพูดเกินจริงเหล่านั้นช่างไร้สาระเสียจนฉันอดไม่ได้ที่จะตอบไปแบบเล่นใหญ่บ้าง"

# hi "Well, I for one feel enlightened."
hi "ครับ ข้าพเจ้าทราบชัดแล้ว"

# hi "I apologize profusely for my rash actions and will strive to contain my baser impulses which, I fear, impel me toward such inappropriate displays of public affection."
hi "ข้าพเจ้าขออภัยเป็นอย่างสูงกับพฤติกรรมซึ่งขาดการยั้งคิดนั้น ข้าพเจ้าจะไม่ทำตัวไปตามความต้องการที่ขัดกับ\nศีลธรรม ซึ่งข้าพเจ้าเกรงว่าเป็นเพราะความต้องการนี้เองที่ทำให้ข้าพเจ้าแสดงความรักในที่สาธารณะอย่างไม่เหมาะสม\nเช่นนั้น"

# hi "It is hardly my wish to burden an already overworked Student Council with such petty matters, and will do my best to make your lives easier in this matter in the future."
hi "ข้าพเจ้ามิได้มีเจตนาจะเพิ่มภาระให้กับสมาชิกสภานักเรียนที่ซึ่งทำงานอย่างหนักหน่วงแล้วด้วยเรื่องเล็กน้อยเช่นนี้เลย\nและข้าพเจ้าจะพยายามอย่างสุดความสามารถเพื่อให้ภายภาคหน้าพวกท่านไม่ต้องลำบากกับเรื่องนี้อีก"

# hi "At least, when Shizune's watching."
hi "แต่ลับหลังชิซูเนะจะยังทำตัวดีอยู่มั้ยก็อีกเรื่อง"

# "This last line is delivered with a wink to Misha, who finally loses control of her laughter."
"ประโยคหลังนั้นฉันพูดพร้อมขยิบตาให้มิช่าซึ่งกลั้นหัวเราะไม่ไหวแล้ว"

show misha cross_laugh
with charachange

# mi "Wahaha~!"
mi "วะฮ่าฮ่า~!"

show misha cross_grin
with charachange

# mi "Well said, Hicchan~!"
mi "พูดได้ดีฮิจัง~!"

# "Chuckling a little myself, we enter the classroom."
"ฉันแค่นหัวเราะตามแล้วเราก็เข้าห้องเรียนกัน"

stop music fadeout 2.0
scene bg school_scienceroom
with shorttimeskip

# "Class is uneventful, and after the final bell rings, I find myself alone with Mutou again."
"ไม่มีเหตุการณ์อะไรระหว่างที่เรียน พอระฆังเลิกเรียนดังแล้วฉันก็อยู่กับครูมุโต้ตามลำพังอีกครั้ง"

show muto smile at center
with charaenter

# mu "So, it looks like we've all assembled for the second meeting of the Science Club."
mu "โอเค ดูเหมือนว่าทุกคนจะมาร่วมกิจกรรมชมรมครั้งที่สองกันครบแล้วนะ"

play music music_another fadein 2.0
show muto normal
with charachange

# mu "Or is it the first? What do you think, should we count yesterday as a meeting?"
mu "หรือเป็นครั้งแรก เธอว่าไง จะนับเมื่อวานเป็นครั้งแรกมั้ย"

# hi "Well, we did form the club yesterday, didn't we?"
hi "ก็ตั้งชมรมกันเมื่อวานแล้วนี่ครับ"

# hi "That seems like club business, so we can safely call yesterday a meeting."
hi "ดูจะเป็นกิจกรรมชมรมอยู่ เพราะงั้นก็นับได้แหละครับ"

show muto smile
with charachange

# "Mutou smiles in his usual stilted and awkward way. I wonder if the muscles in his face are just not shaped correctly to let him smile naturally."
"ครูยิ้มเฝื่อน ๆ แกน ๆ อย่างเคย หรือว่ากล้ามเนื้อใบหน้าจะไม่เข้าตำแหน่งถึงได้ยิ้มให้เป็นธรรมชาติไม่ได้กันนะ"

# mu "You really do have a knack for this, I think. Logical thought processes, that is."
mu "เธอดูจะถนัดเรื่องนี้นะ หมายถึงเรื่องการคิดอย่างมีเหตุผลน่ะ"

# hi "I guess so?"
hi "ก็มั้งนะครับ?"

show muto normal
with charachange

# mu "A scientist speaks with authority, Hisao. The answer here is “Yes, I do.”"
mu "คำพูดของนักวิทยาศาสตร์น่ะต้องมีพลังนะฮิซาโอะ เธอต้องตอบว่า “ใช่แล้วครับ”"

# mu "When the world wants to know how it works, we tell it. Even if all we've got is a decent hypothesis."
mu "ถ้าโลกอยากรู้ว่ามันเป็นยังไงเราก็จะบอกไป ต่อให้สิ่งที่เรามีในมือจะเป็นแค่สมมุติฐานที่พอใช้ได้ก็ตาม"

show muto smile
with charachange

# mu "But we must sound certain anyway, because we're the authorities on the subject, right?"
mu "แต่เราก็ต้องพูดไปด้วยความมั่นใจ เพราะเราเป็นผู้รู้ในเรื่องนี้ จริงไหม"

# "He chuckles, to go along with his awkward smile at his awkward joke. I'm doing my best not to grimace, but I don't think I'm being too successful."
"ครูแค่นหัวเราะก่อนจะยิ้มเจื่อน ๆ กับมุกฝืด ๆ นั้น ฉันปั้นหน้าไม่ให้ทำหน้าเบ้ไป แต่น่าจะไม่ได้ผลเท่าไหร่"

show muto normal
with charachange

# mu "That's entirely false, of course."
mu "แน่ละว่าไม่ใช่อย่างนั้นเลย"

# mu "We know a lot, sure, but nobody's an expert on how the world works, if only because nobody can be sure. With no certainty, there are no experts."
mu "เรารู้เยอะก็จริง แต่ไม่มีใครที่เป็นผู้เชี่ยวชาญเรื่องระบบของโลกนี้ เพราะไม่มีใครที่จะแน่ใจกับเรื่องอะไรสักอย่าง\nได้เลย และพอไม่มีความแน่ใจแล้วก็จะไม่มีใครที่เป็นผู้เชี่ยวชาญอีก"

# mu "But we like to pretend, sometimes."
mu "แต่บางทีเราก็ชอบทำแสร้งไปเหมือนกัน"

# hi "There's some things we can be certain of, right?"
hi "แต่บางอย่างเราก็แน่ใจได้นี่ครับ"

# mu "Yes… but no."
mu "ใช่… แต่ก็ไม่ใช่"

# mu "We know gravity's there, for example."
mu "เช่นว่า เรารู้ว่าแรงโน้มถ่วงมีจริง"

# "To illustrate, Mutou picks up a pencil and drops it."
"ครูหยิบดินสอขึ้นมาแล้วปล่อยให้ตกเป็นการยกตัวอย่าง"

# mu "See? Still there. But it's good to check every once in a while."
mu "เห็นมั้ย ยังมีจริง แต่นาน ๆ ทีลองตรวจดูบ้างก็ไม่เสียหาย"

# mu "That's why you'll still see researchers mucking about with gravity."
mu "เพราะแบบนี้เราถึงยังได้เห็นนักวิจัยที่วุ่นวายอยู่กับเรื่องแรงโน้มถ่วง"

show muto smile
with charachange

# mu "We're pretty sure we know how it works, but there's always a chance that something isn't how we think it is."
mu "เราค่อนข้างแน่ใจว่ามันเป็นยังไง แต่ก็มีโอกาสอยู่เหมือนกันที่สิ่งนั้น ๆ จะไม่ได้เป็นอย่างที่เราคิด"

# mu "So you check, and check, and check. That's science in a nutshell, Hisao."
mu "เราถึงได้ตรวจแล้ว ตรวจอีก ตรวจเข้าไป โดยย่อแล้ววิทยาศาสตร์ก็ประมาณนี้แหละฮิซาโอะ"

# "The whole time I've listened feeling rather spellbound. Mutou seems to really be passionate about this stuff… I think. It's hard to tell, sometimes."
"ฉันคอยฟังเหมือนต้องมนต์สะกด ครูดูจะคลั่งไคล้ในเรื่องทำนองนี้… คิดว่านะ บางทีก็ดูไม่ค่อยออก"

# "How the world works…"
"ระบบของโลกนี้…"

# "How humans work."
"ระบบของมนุษย์"

# "How the universe works."
"ระบบของจักรวาล"

# "All these questions to be answered."
"คำถามเหล่านี้ที่ต้องการคำตอบ"

# "And, depending on what I go into, maybe I could even figure out a way to fix my heart. That said, I don't think that's a real priority for me."
"และฉันอาจจะหาวิธีรักษาหัวใจของฉันก็ได้ ถ้าเลือกเรียนให้ถูกสาขา แต่ถึงอย่างนั้นก็เถอะ สิ่งนั้นไม่ใช่เรื่องสำคัญ\nสำหรับฉันเท่าไหร่"

# "Besides, as we start discussing the book he gave me yesterday, I find myself more and more interested in that than my heart condition."
"อีกอย่าง ระหว่างที่คุยกันเรื่องหนังสือที่ครูให้มาเมื่อวานฉันก็เริ่มสนใจเนื้อหาในนั้นขึ้นมาเรื่อย ๆ สนใจมากกว่า\nอาการหัวใจของตัวเองเสียอีก"

show muto normal
with shorttimeskip

# "Before we even realize it, an hour's gone by."
"หนึ่งชั่วโมงผ่านไปโดยที่เราไม่ทันรู้ตัว"

# mu "Well, let's call this meeting over for now, okay?"
mu "โอเค งั้นก็เลิกกิจกรรมกันเท่านี้ก่อนนะ"

# mu "We'll have another meeting… tomorrow, or uh… the day after."
mu "ไว้มาจัดกิจกรรมชมรมอีกทีกัน… พรุ่งนี้ หรือ เอ่อ… มะรืนนี้"

# "He considers this for a moment."
"ครูคิดอยู่ครู่หนึ่ง"

# mu "Call it the day after. I've got a lot of grading to do."
mu "เอาเป็นมะรืนนี้แล้วกัน ครูยังเหลืองานที่ต้องตรวจอีกเยอะ"

# hi "Okay. See you then."
hi "โอเคครับ งั้นก็ไว้เจอกัน"

scene bg school_hallway3
with locationchange

stop music fadeout 5.0

# "As I exit the classroom, I realize that I don't really have anything to do tonight."
"พอออกจากห้องเรียนมาถึงนึกได้ว่าคืนนี้ฉันไม่มีอะไรให้ทำเลย"

# "Emi and I didn't make plans, so…"
"เอมิกับฉันก็ไม่ได้นัดอะไรกันไว้ เพราะงั้น…"

# "I guess I'll go to the library. It beats doing homework in my room, anyway."
"ไปห้องสมุดแล้วกัน ยังไงก็ดีกว่าไปทำการบ้านอยู่ในห้องตัวเอง"

scene black
with locationskip_in

#######################

label th_E20:

play music music_happiness fadein 2.0
scene bg school_library
with locationskip_out

# "The library always seems cooler than the rest of the building."
"ห้องสมุดดูจะเย็นกว่าส่วนอื่นในอาคาร"

# "Probably to keep the books from getting damaged by excessive heat and humidity."
"อาจจะเพราะต้องเก็บรักษาหนังสือไม่ให้เสียหายจากความชื้นกับความร้อนที่มากเกินไป"

# "Books are sturdy objects, but if you want to keep them in good condition it takes a little effort."
"หนังสือเป็นของทนทาน แต่ถ้าอยากรักษาให้สภาพดีก็ต้องลงทุนนิดหน่อย"

# "I've got several books that are so well-worn the pages are barely clinging to the spine."
"ฉันมีหนังสือหลายเล่มที่สภาพโทรมเสียจนหน้าหนังสือแทบจะขาดจากสันแล้ว"

# "It seems impossible for them to still be usable, but if you handle them with care…"
"อาจจะดูเหมือนใช้ไม่ได้แล้ว แต่ถ้าทะนุถนอมเสียหน่อย…"

# "I make my way to the main desk, where I spot Yuuko busying herself with something or another."
"เมื่อเดินไปที่เคาน์เตอร์ก็เห็นยูโกะกำลังง่วนอยู่กับอะไรสักอย่าง"

show yuuko neutral_up at center
with charaenter

# "She smiles at me as I enter and waves."
"ยูโกะยิ้มเมื่อฉันเดินไปหาแล้วโบกมือทักทาย"

show yuuko closedhappy_down
with charachange

# yu "Hello, Hisao."
yu "สวัสดีฮิซาโอะ"

show yuuko happy_down
with charachange

# yu "Good to see you again! What are you looking for this time?"
yu "ยินดีที่ได้เจออีกครั้งนะ! คราวนี้มาหาอะไรเหรอ"

# hi "Nothing in particular, I guess. I just didn't really feel like going back to my room, is all."
hi "ก็ไม่ได้มาหาอะไรเป็นพิเศษละนะครับ แค่รู้สึกยังไม่อยากกลับห้องเฉย ๆ"

show yuuko neutral_down
with charachange

# "Yuuko nods."
"ยูโกะพยักหน้า"

show yuuko smile_up
with charachange

# yu "Well, if you're unoccupied, maybe you could help me look for something?"
yu "อ่า ถ้าว่าง ๆ ก็มาช่วยฉันหาของหน่อยสิ"

# hi "Sure, what do you need?"
hi "ครับ หาอะไรเหรอ"

stop music fadeout 5.0

show yuuko worried_up
with charachange

# "Yuuko brings a finger to her lips and looks around furtively."
"ยูโกะยกนิ้วขึ้นมาแตะปากแล้วเหลียวซ้ายแลขวา"

# "She seems to be looking for eavesdroppers."
"เหมือนจะหาว่ามีคนดักฟังอยู่หรือเปล่า"

# yu "Come closer."
yu "เข้ามาใกล้ ๆ หน่อย"

show yuuko worried_up_close
with characlose

# "I take a few hesitant steps forward while feeling distinctly unnerved."
"ฉันเดินเข้าไปหาโดยยังไม่แน่ใจนักพร้อมความรู้สึกไม่ค่อยสบายใจ"

# "Yuuko lowers her voice to a confidential whisper."
"ยูโกะลดเสียงลงมาเป็นการกระซิบกระซาบ"

show yuuko neutral_up_close
with charachange

# yu "I'm on the trail of the Yamaku Cat Burglar."
yu "ฉันกำลังสะกดรอยหาแมวขโมยยามากุอยู่"

play music music_tension fadein 0.5

# hi "The what?"
hi "หาอะไรนะครับ"

show yuuko panic_up_close
with charachange

# yu "Shh! The walls have ears, Hisao!"
yu "ชู่! กำแพงมีหูนะฮิซาโอะ!"

# yu "Or they might."
yu "อาจจะมี"

show yuuko worried_down_close
with charachange

# yu "But listen! Those missing books, remember them?"
yu "แต่ฟังนะ! หนังสือที่หายไปน่ะ จำได้มั้ย"

# hi "Er, yeah?"
hi "เอ้อ ครับ?"

show yuuko worried_up_close
with charachange

# yu "Well, they weren't missing! They were stolen!"
yu "จริง ๆ แล้วไม่ได้หาย! แต่โดนขโมยไปต่างหาก!"

# yu "I'm convinced of it!"
yu "ฉันมั่นใจเลย!"

# hi "I remember you saying something of the sort earlier, but how do you know?"
hi "ผมจำได้อยู่ว่าคุณเคยพูดถึงเหมือนกัน แต่คุณรู้ได้ยังไงครับ"

# "Yuuko leans in closer and, if possible, whispers even lower."
"ยูโกะโน้มตัวเข้ามาอีกแล้วเหมือนจะกระซิบเสียงแผ่วกว่าเดิม"

show yuuko closedhappy_down_close
with charachange

# yu "Because I found one of his hiding places!"
yu "เพราะฉันเจอที่ซ่อนตัวของมันแล้ว!"

# hi "You did what?"
hi "อะไรนะครับ"

# "Yuuko looks triumphant."
"ยูโกะดูจะภูมิใจ"

show yuuko happy_up_close
with charachange

# yu "Found one of his stashes! It was under one of the stairwells in the boy's dorm!"
yu "ฉันเจอของที่มันแอบเอาไปแล้วกองหนึ่ง! อยู่ตรงใต้บันไดหอชาย!"

# yu "Three books I'd been looking for, all there!"
yu "หนังสือสามเล่มที่ฉันกำลังตามหาน่ะอยู่ตรงนั้นหมดเลย!"

show yuuko closedhappy_up_close
with charachange

# yu "I'd suspected a thief before, but this proves it!"
yu "ฉันเคยสงสัยอยู่ว่ามีขโมยหรือเปล่า แต่คราวนี้ได้หลักฐานแล้ว!"

# hi "So did you take back the books?"
hi "แล้วได้เก็บหนังสือกลับมามั้ยครับ"

show yuuko panic_up_close
with charachange

# "Yuuko looks as if I've just suggested she walk around naked."
"ยูโกะทำหน้าเหมือนฉันบอกให้ออกไปเดินแก้ผ้า"

# yu "Are you nuts?"
yu "บ้าหรือเปล่า"

show yuuko worried_down_close
with charachange

# yu "He can't know I'm on to him! He might go to ground and evade capture!"
yu "เดี๋ยวมันก็รู้ว่าฉันตามตัวอยู่! มันก็จะกลับเข้าที่กบดานแล้วหนีไม่ให้จับได้อีก!"

# hi "Uh… huh. So what do you need my help with, then?"
hi "อ่า… ฮะ แล้วสรุปจะให้ผมช่วยทำอะไรเหรอครับ"

# "Yuuko casts another glance around the library and leans in closer."
"ยูโกะกวาดตามองไปรอบ ๆ ห้องสมุดอีกรอบแล้วโน้มตัวเข้ามา"

show yuuko neutral_down_close
with charachange

# yu "You've got to spy for me."
yu "ไปตามสืบให้หน่อย"

# hi "Spy?"
hi "สืบ?"

# yu "Yeah, like when you're in the dorms, you know."
yu "ใช่ คอยตามตอนอยู่หออะไรแบบนี้"

show yuuko closedhappy_down_close
with charachange

# yu "Keep an eye out for suspicious activity."
yu "คอยจับตาดูพฤติกรรมน่าสงสัยไว้"

# "What constitutes suspicious, anyway?"
"แล้วไอ้คำว่าน่าสงสัยนี่ต้องพิจารณายังไง"

# "I mean Kenji's a pretty suspicious dude, but I'll wager he barely goes to class, much less sneaks into the library to pilfer books."
"เคนจิก็เป็นคนน่าสงสัยแหละ แต่คงแทบไม่ได้เข้าเรียนเลยมั้ง ยิ่งไม่ต้องพูดถึงว่าจะมาแอบเข้าห้องสมุด\nเพื่อขโมยหนังสือเนี่ย"

# "Still, what's the harm in saying yes? At the least it'll get me out of this weird conversation."
"แต่ตอบตกลงไปก็คงไม่เสียหายมั้ง อย่างน้อยก็จะได้ปลีกตัวจากบทสนทนาพิลึก ๆ นี้เสียที"

# hi "Yeah, I can do that. No problem."
hi "อืม ได้ครับ ไม่มีปัญหา"

show yuuko closedhappy_down
with charadistant

# "Yuuko straightens up and claps excitedly."
"ยูโกะยืดหลังตรงแล้วตบมือตื่นเต้น"

# yu "Great!"
yu "เยี่ยม!"

show yuuko worried_down
with charachange

# yu "Now, hurry up and talk about something else in case someone comes in!"
yu "ทีนี้ก็รีบ ๆ คุยเรื่องอื่นเผื่อมีคนเข้ามาได้แล้ว!"

stop music fadeout 2.0

show yuuko happy_down
with charachange

# yu "How's the school treating you?"
yu "อยู่โรงเรียนนี้เป็นยังไงบ้าง"

# hi "Er, pretty well, actually."
hi "เอ้อ ก็ดีอยู่นะครับ"

# hi "I've been running in the mornings with—"
hi "พักนี้ผมไปวิ่งตอนเช้ากับ—"

show yuuko closedhappy_up
with charachange

# yu "Emi Ibarazaki, right?"
yu "เอมิ อิบาราซากิ ใช่มั้ย"

play music music_comedy fadein 2.0

# hi "Uh, yeah."
hi "เอ่อ ครับ"

# hi "How'd you know?"
hi "รู้ได้ยังไง"

show yuuko smile_down
with charachange

# yu "I served you two in the teahouse, remember?"
yu "ฉันเป็นบริกรให้เธอสองคนที่โรงน้ำชาไง จำได้มั้ย"

show yuuko closedhappy_down
with charachange

# yu "I deduced that if you were going to run with anyone, it would probably be her."
yu "ฉันอนุมานเอาว่าคนที่เธอจะไปวิ่งด้วยก็คงเป็นเอมินั่นแหละ"

# "She looks pleased with herself."
"ยูโกะดูจะพึงใจกับตัวเอง"

# hi "Impressive."
hi "สุดยอดครับ"

# hi "Anyway, yes. We've been running in the mornings."
hi "แต่ก็ใช่ครับ เราไปวิ่งด้วยกันตอนเช้า"

# hi "And uh, we kinda started dating."
hi "แล้วก็ เอ่อ คบ ๆ กันแล้วด้วย"

show yuuko closedhappy_up
with charachange

# "Yuuko claps her hands together excitedly."
"ยูโกะตบมืออย่างตื่นเต้น"

# yu "Really? That's great!"
yu "จริงเหรอ เยี่ยมเลย!"

# yu "I'll bet you two are great together!"
yu "เธอสองคนคงเข้ากันดีแน่!"

show yuuko neutral_down
with charachange

# yu "I love seeing people find one another like that, you know?"
yu "ฉันชอบดูคนที่ได้เจอกับคู่ของตัวเองนะ"

# yu "I even thought to myself when you walked into the Shanghai that one time, “I wonder if that kid will wind up with one of those girls.”"
yu "ตอนที่เธอมาที่เซี่ยงไฮ้หนนั้นฉันยังคิดเลยว่า “เขาคนนี้จะได้คบกับใครสักคนที่พามาด้วยหรือเปล่านะ”"

# hi "…Really?"
hi "…จริงเหรอครับ"

# "Yuuko doesn't seem to notice my somewhat weirded out tone and nods affirmatively."
"ยูโกะเหมือนจะไม่ทันจับสังเกตน้ำเสียงฉันที่รู้สึกแปลก ๆ ไปแล้วพยักหน้ารับ"

show yuuko closedhappy_down
with charachange

# yu "Yup! I could tell that you'd wind up with one of them, you know."
yu "อื้ม! ดูออกเลยว่าเดี๋ยวเธอก็คงต้องคบกับใครสักคนแน่ ๆ"

show yuuko neutral_down
with charachange

# yu "I've got an eye for that sort of thing."
yu "ฉันน่ะมองของพวกนี้ได้แม่นนะ"

show yuuko worried_down
with charachange

# yu "Of course…"
yu "แน่นอนว่า…"

# "Her expression droops slightly."
"ยูโกะทำหน้าหงอยไปเล็กน้อย"

# yu "I'm not so good at it myself."
yu "ฉันน่ะหาคู่ไม่เก่งหรอก"

# hi "Aw, I'm sure that's not true."
hi "โธ่ ผมว่าไม่จริงหรอกครับ"

show yuuko neutral_down
with charachange

# yu "Oh, it's true."
yu "ไม่หรอก จริง"

# yu "I met this guy once…"
yu "ฉันเคยไปเจอผู้ชายคนหนึ่ง…"

show yuuko smile_down
with charachange

# yu "We got along really great, but it turned out he was younger than me."
yu "เราเข้ากันได้ดีมากเลย แต่กลายเป็นว่าเขาน่ะเด็กกว่าฉัน"

show yuuko neutral_up
with charachange

# yu "And that was kinda weird, but not terribly so."
yu "ซึ่งก็แปลก ๆ แต่ก็ไม่ได้แปลกมาก"

# yu "What was really weird was that he disappeared one day, and I've not seen him since then."
yu "ที่แปลกมากคืออยู่ ๆ วันหนึ่งเขาก็หายไป แล้วฉันก็ไม่ได้เห็นหน้าเขาอีกเลย"

# hi "Huh. That does seem kind of odd."
hi "หืม ก็ดูแปลกอยู่นะครับ"

show yuuko worried_up
with charachange

# yu "Doesn't it?"
yu "ใช่มั้ยล่ะ"

show yuuko neurotic_down
with charachange

# yu "I hope it wasn't something I did…"
yu "หวังว่าที่หายไปจะไม่ใช่เพราะฉันทำอะไรพลาดนะ…"

# "I feel compelled to reassure her."
"รู้สึกเหมือนต้องปลอบยูโกะ"

# hi "I'm sure it wasn't."
hi "ผมว่าไม่ใช่หรอกครับ"

stop music fadeout 4.0

$ renpy.music.set_volume(0.5, 0.0, channel="sound")
play sound sfx_phone
show yuuko panic_up
with vpunch

# "I intend to try and calm her down further, but the both of us jump in surprise at the ringing suddenly coming from my pocket."
"ฉันตั้งใจจะปลอบยูโกะอีก แต่เราสองคนก็ต้องสะดุ้งตกใจเมื่ออยู่ ๆ ก็มีเสียงเรียกเข้าดังออกมาจากกระเป๋ากางเกงฉัน"

show yuuko worried_down
with charachange

# "Yuuko sighs to steady herself as I pull the phone from my pocket. I feel a little sheepish for indirectly causing the incident."
"ยูโกะถอนหายใจตั้งสติระหว่างที่ฉันควักโทรศัพท์ออกมา อาย ๆ ขึ้นมาเลยแฮะที่เป็นตัวการขัดจังหวะแบบอ้อม ๆ"

scene bg school_library_yuuko_blurred
show phone mobile:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with locationchange
with Pause (0.5)

# hi "Emi? What's up?"
hi "เอมิ มีอะไรเหรอ"

# emi "Oh thank God I haven't called your phone before so I didn't know if this number would work or whether you would pick up and I can't—"
emi "อาโล่งไปทีฉันไม่เคยโทรศัพท์เข้าเครื่องนายมาก่อนเลยไม่รู้ว่าเบอร์นี้จะใช้ได้หรือเปล่าไม่รู้ว่านายจะรับหรือเปล่า\nแล้วฉันก็—"

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play music music_pearly fadein 2.0

# hi "Woah there Emi, slow down."
hi "เอ้า ๆ เอมิ ใจเย็นก่อน"

# hi "What's wrong?"
hi "มีอะไรเหรอ"

# "There's a pause on the other side of the line, during which I can hear Emi trying to control her breathing in order to calm down."
"ปลายสายเว้นช่วงไป มีเสียงเอมิที่กำลังควบคุมลมหายใจตัวเองให้สงบลงดังลอดออกมา"

# "Something's got her terribly agitated, and it's starting to agitate me."
"มีเรื่องทำให้เอมิลนลาน ซึ่งฉันก็เริ่มลนลานตามแล้ว"

# emi "Can you just…"
emi "รบกวนนาย…"

# emi "Can you stop by?"
emi "รบกวนนายมาหาหน่อย"

# emi "Like, now? Or shortly after now?"
emi "แบบ ตอนนี้เลย หรือไม่ก็อีกสักแป๊บ"

# emi "I really, really need to talk to you."
emi "ฉันอยากคุยกับนายมาก มาก ๆ"

# "There's a tone of pleading in the last sentence that I don't think I've ever heard from her."
"น้ำเสียงอ้อนวอนจากประโยคสุดท้ายนั้นเป็นน้ำเสียงที่ฉันไม่เคยได้ยินเอมิใช้มาก่อนเลย"

# hi "Of course, I'll be right there."
hi "ได้สิ เดี๋ยวไปหา"

# hi "Hold steady, okay?"
hi "ทำใจดี ๆ ไว้นะ"

# "In my increasingly agitated state I've apparently started saying things that don't quite make sense."
"ฉันลนลานหนักขึ้นเรื่อย ๆ จนเหมือนจะพูดอะไรที่ฟังดูเพี้ยน ๆ ไปแล้ว"

# emi "Okay. I'll be okay."
emi "โอเค จะตั้งสติ"

# hi "See you soon."
hi "ไว้เจอกัน"

show phone mobile:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with None

scene bg school_library
show yuuko worried_down at center
show phone mobile:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with locationchange
with Pause (0.5)

hide phone
with None

with charaexit

# "I press the button to end the call before slipping the phone back into my pocket, apologize to Yuuko for running off, and run off."
"ฉันกดวางสายแล้วเก็บโทรศัพท์กลับเข้ากระเป๋ากางเกงก่อนจะขอโทษยูโกะที่ต้องรีบออกมาก่อนแล้วรีบออกมา"

scene bg school_girlsdormhall
with locationskip

# "Perhaps at some point I would have stopped to think about the time, or how suspicious it looks for a guy to enter the girls' dorm at this hour."
"จริง ๆ ฉันอาจจะต้องคิดสักหน่อยถึงเรื่องเวล่ำเวลา คิดว่าการที่ผู้ชายมาเข้าหอหญิงตอนช่วงเวลานี้นั้นดูน่าสงสัย\nแค่ไหน"

# "Except right now I'm just concerned with getting to Emi and finding out what's wrong and how I can help her."
"เว้นก็แต่ตอนนี้ฉันมัวแต่ห่วงเรื่องจะไปเจอเอมิกับไปดูว่าเกิดอะไรขึ้นแล้วจะได้ช่วย"

play sound sfx_doorknock2

# "I knock on the door and am greeted with a subdued “Come in.”"
"ฉันเคาะประตูก่อนจะมีเสียงอู้อี้ว่า “เข้ามาเลย” ตอบกลับมา"

scene bg school_dormemi at left
with locationchange

# "Something is very wrong as I stare at the scene before me."
"เมื่อจ้องมองภาพตรงหน้าก็เห็นว่าบางอย่างแปลกไปอย่างมาก"

# "Emi's there, yes."
"เอมิอยู่ในห้องนี้ ใช่"

# "But she's in a wheelchair."
"แต่นั่งวีลแชร์อยู่"

# "And her legs are missing. I glance around the room and see them sitting in a corner, looking like they've been thrown there."
"และไม่มีขาด้วย พอกวาดตามองรอบห้องก็เห็นขาเทียมที่วางอยู่ตรงมุมหนึ่งในห้องเหมือนมีคนโยนทิ้งไว้"

show emiwheel weaksmile at center
with charaenter

# "Emi responds to my entrance with a lopsided grin that is both pleased to see me and completely, utterly heartbroken."
"เอมิยกยิ้มขึ้นครึ่งหน้าให้กับฉันที่เดินเข้ามาดูดีใจที่ได้เจอฉันและดูใจสลายไม่เหลือชิ้นดี"

# emi "Hi, Hisao."
emi "ไง ฮิซาโอะ"

# "It looks like she's been crying, but if she was, she's stopped now."
"ดูเหมือนจะกำลังร้องไห้อยู่ แต่ตอนนี้ไม่ร้องแล้ว"

# "I notice that I'm a little out of breath, having taken the stairs two at a time in order to get here."
"ฉันเพิ่งรู้ตัวว่าฉันหอบเล็กน้อยเพราะเดินขึ้นบันไดแบบข้ามขั้นมาเพื่อรีบมาที่นี่"

# "My heart doesn't seem to mind the strain, though. I file this happy fact away for later consideration."
"แต่หัวใจฉันดูจะยังไม่เพี้ยนตามความเหนื่อย ฉันเก็บเรื่องอันน่ายินดีนี้ไว้คิดทีหลัง"

# "Like when I am not staring somewhat dumbstruck at my girlfriend in a wheelchair."
"ทีหลังที่ว่าก็เช่นตอนที่ฉันไม่ได้มายืนมองแฟนสาวที่นั่งวีลแชร์อยู่ด้วยความตกตะลึง"

# "Realizing I've still not responded to her greeting, my brain lurches into gear."
"เมื่อระลึกได้ว่ายังไม่ได้ตอบกลับคำทักทายเอมิแล้วสมองฉันก็ทำงานต่อ"

# hi "Emi? What happened?"
hi "เอมิ เกิดอะไรขึ้น"

show emiwheel pout
with charachange

# emi "Guess I should've listened to you, Hisao."
emi "รู้งี้ฉันเชื่อนายเสียแต่แรกก็ดี"

show emiwheel sad
with charachange

# emi "My leg's got a nasty infection. I'm not allowed to run on it for at least a couple of weeks."
emi "ขาฉันติดเชื้อหนักเฃบ แล้วก็ห้ามใช้ขาเทียมวิ่งไปอีกอย่างน้อย ๆ สักสองอาทิตย์"

# "She gives a bitter laugh that shouldn't be coming from her."
"เอมิหัวเราะขื่น ๆ ซึ่งดูไม่สมเป็นตัวเธอเลย"

show emiwheel frown
with charachange

# emi "Heh, I can't even walk on it."
emi "ฮะ ๆ จะเดินก็ยังไม่ได้ด้วยซ้ำ"

# emi "I could have used a crutch and kept one of my legs, but I didn't see the point."
emi "จริง ๆ จะใช้ไม้ค้ำยันแล้วใส่ขาเทียมข้างเดียวก็ได้ แต่ก็ไม่รู้จะทำแบบนั้นไปทำไม"

show emiwheel awayfrown
with charachange

# emi "Why hop? You can't run on one leg."
emi "ทำไมต้องมาคอยโดดเหยง ๆ เอาด้วย วิ่งขาเดียวก็ไม่ได้"

show emiwheel pout
with charachange

# emi "At least this way I can still, I dunno, roll fast or something."
emi "อย่างน้อยแบบนี้ฉันก็ยังได้ ไม่รู้สิ หมุนล้อไปเร็ว ๆ ได้"

# hi "Y-yeah, that's good, right?"
hi "อะ-อื้ม ก็ดีแล้วนี่เนอะ"

# "My awkward attempt to look on the bright side seems appreciated, but not really effective."
"เหมือนเอมิจะขอบคุณที่ฉันอุตส่าห์พยายามมองโลกในแง่ดีแบบเก้ ๆ กัง ๆ แต่ที่พูดไปนั้นก็ไม่ได้ผลสักเท่าไหร่"

# "Emi shrugs again."
"เอมิยักไหล่อีกรอบ"

show emiwheel awayfrown
with charachange

# emi "It's just… kind of a nuisance."
emi "แบบว่า… มันน่ารำคาญน่ะ"

show emiwheel frown
with charachange

# emi "I mean, we can't even eat up on the roof now. No wheelchair access."
emi "คือจะกินข้าวเที่ยงด้วยกันบนดาดฟ้าก็ไม่ได้แล้วเพราะไม่มีทางให้วีลแชร์ขึ้น"

# hi "Yeah, but that's not a big deal, right?"
hi "อืม แต่ก็ไม่ใช่เรื่องใหญ่ขนาดนั้นนี่ ใช่มั้ย"

# hi "I mean we can still eat together, and that's the important thing."
hi "เราก็ยังกินข้าวด้วยกันได้ ซึ่งใจความสำคัญมันอยู่ตรงนั้น"

show emiwheel weaksmile
with charachange

# "That lopsided grin again. It hurts to look at."
"รอยยิ้มครึ่งซีกนั้นอีกแล้ว เห็นแล้วก็เจ็บปวดใจ"

# emi "I suppose so, yeah."
emi "ก็คงงั้น อืม"

show emiwheel frown
with charachange

# emi "But like I said, it's a nuisance."
emi "แต่อย่างที่บอกนั่นแหละว่ามันน่ารำคาญ"

show emiwheel awayfrown
with charachange

# emi "I mean, I haven't really used a wheelchair in…"
emi "คือฉันก็ไม่ได้ใช้วีลแชร์มา…"

stop music fadeout 10.0

# "She thinks for a minute."
"เอมิคิดอยู่ราวหนึ่งนาที"

show emiwheel pout
with charachange

# emi "Maybe seven years? Something like that, anyway."
emi "เจ็ดปีมั้ง ราว ๆ นั้นแหละ"

# emi "A long time."
emi "นานแล้ว"

show emiwheel weaksmile
with charachange

# emi "I'm afraid I'm a bit out of practice."
emi "ฉันกลัวว่าฉันจะใช้ไม่ค่อยถนัดเท่าไหร่"

# hi "Well, fortunately it's only temporary, right?"
hi "แต่ก็โชคดีไปนี่ที่ไม่ได้ต้องใช้ถาวรน่ะ"

# "Emi nods."
"เอมิพยักหน้า"

show emiwheel neutral
with charachange

# emi "Oh yeah, of course."
emi "อ้อ อืม ใช่"

# emi "It's not like I've lost 'em permanently."
emi "ใช่ว่าฉันจะต้องเลิกใช้ขาเทียมไปตลอดชีวิตสักหน่อย"

show emiwheel awayfrown
with charachange

# emi "But it's a pain in the ass all the same."
emi "แต่มันก็น่ารำคาญอยู่ดี"

# "I nod sympathetically."
"ฉันพยักหน้าด้วยความเห็นใจ"

# "There's not much else I can do, after all."
"ฉันก็ช่วยอะไรไม่ได้มากนี่นะ"

# "What am I gonna do, say “I told you so?”"
"จะให้ทำยังไง บอกว่า “ก็บอกแล้วไง” เหรอ"

# "Although I {b}did{/b} tell her to get that leg looked at."
"ถึงฉันจะ{b}บอก{/b}ให้เอมิไปดูเรื่องขาตัวเองก็จริง"

# "But by the time I noticed, it was too late anyway."
"แต่กว่าฉันจะจับสังเกตได้ก็สายไปแล้ว"

# hi "Do you need help with anything?"
hi "มีอะไรให้ช่วยหรือเปล่า"

# hi "Er, that is, can I help with anything?"
hi "เอ่อ ถ้าช่วยได้น่ะนะ"

show emiwheel closedsmile
with charachange

# "Emi shakes her head and there's a bit of her usual grin back."
"เอมิสั่นหัวก่อนจะกลับมายิ้มเหมือนทุกที"

# emi "Nah, I can manage fine by myself."
emi "ไม่อะ ฉันจัดการตัวเองได้"

show emiwheel grin
with charachange

# emi "Although if you want to help me over to my bed, it would save me the trouble of rolling over there myself."
emi "แต่ถ้านายอยากช่วยอุ้มฉันไปที่เตียงก็ได้นะ ฉันจะได้ไม่ต้องลำบากกลิ้งไปนอนบนเตียงเอง"

# "I blush, in spite of myself."
"ฉันหน้าแดงขึ้นมาโดยไม่รู้ตัว"

# "Emi giggles."
"เอมิหัวเราะคิกคัก"

play music music_heart fadein 0.5

show emiwheel wink
with charachange

# emi "You're such a prude, Hisao."
emi "นายนี่ไม่เดียงสาจริง ๆ ฮิซาโอะ"

# hi "I'm not a prude! I just wouldn't want to take advantage of a young woman such as yourself."
hi "ไม่เดียงสาอะไร! ฉันแค่ไม่อยากเอาเปรียบเด็กผู้หญิงอย่างเธอต่างหาก"

# hi "It's ungentlemanly."
hi "สุภาพบุรุษเขาไม่ทำกันแบบนั้น"

hide emiwheel
with charaexit

show bg school_dormemi at right
with charamove

# "I wheel Emi's chair to her bed, and easily scoop her up and deposit her there. She quickly sorts herself out and sits on the side."
"ฉันเข็นวีลแชร์เอมิไปที่เตียงแล้วอุ้มเธอวางลงกับเตียง เอมิรีบจัดแจงตัวเองแล้วนั่งที่ริมเตียง"

show emi basic_grin:
    center
    ypos 1.0
    easein 0.5 ypos 1.1
with charaenter

# "She's actually a little heavier than she looks. It would be rude of me to observe this aloud, of course."
"เอมิตัวหนักกว่าที่เห็นอยู่นิดหน่อย แต่แน่ละว่าถ้าจะให้พูดข้อสังเกตที่ว่านั้นออกไปคงหยาบคาย"

# hi "Man, you're kind of heavy."
hi "โห ตัวเธอก็หนักอยู่นะเนี่ย"

play sound sfx_pillow
show comic vfx2
show emi excited_amused:
    center
    ypos 1.1
with hpunch

with Pause(0.5)

show comic vfx2:
    truecenter
    easeout 0.5 yanchor 0.3 alpha 0.0
with Pause(0.5)

# "Emi hits me with a pillow."
"เอมิเอาหมอนฟาดฉัน"

show emi basic_closedgrin
with charachange

# emi "Ass."
emi "ปากเสีย"

# hi "Just sayin', is all."
hi "แค่บอกเฉย ๆ"

# hi "Must be all that running."
hi "คงเพราะวิ่งเยอะแน่เลย"

show emi sad_shy
with charachange

# "At the mention of running Emi's grin falters slightly."
"พอพูดถึงเรื่องวิ่งแล้วรอยยิ้มเอมิก็หุบลงเล็กน้อย"

show emi sad_pout
with charachange

# emi "Heh, well I guess I won't have to worry about that for a bit, huh?"
emi "ฮะ ๆ คงไม่ต้องคิดมากเรื่องวิ่งไปอีกสักพักเลยสินะ"

show emi sad_grin
with charachange

# emi "Maybe I'll lose some weight."
emi "น้ำหนักอาจจะลดด้วย"

# hi "That's what you do to lose weight, right? Cease physical activity?"
hi "คนเราก็ลดน้ำหนักกันด้วยวิธีนี้ใช่มั้ยล่ะ แบบไม่ต้องขยับตัวมากน่ะ"
#Not really, but this is just Hisao grasping at straws. Leave this in. -SC + HM

show emi basic_closedgrin
with charachange

# emi "I'm pretty sure that's what the nurse would recommend."
emi "ฉันว่าคุณพยาบาลก็คงจะแนะนำแบบนั้นแหละ"

# hi "Speaking of which, are you going to still be showing up in the mornings?"
hi "จะว่าไป เธอจะยังไปที่ลู่ตอนเช้าอยู่มั้ย"

# hi "I'd hate to run alo—"
hi "วิ่งคนเดียวฉันคงเหง—"

show emi sad_depressed
with charachange

# emi "Ah, shit…"
emi "อ๊ะ เชี่ย…"

# "Emi's sudden interjection, more a disquieted muttering than anything too profane, causes me to look over in shock."
"เสียงอุทานของเอมิที่เหมือนเป็นการพึมพำด้วยความขัดใจมากกว่าจะเป็นการก่นด่าอะไรทำให้ฉันต้องหันไปมองเธอ\nด้วยความตกใจ"

# "She's leaning forward, trying to cover the fact that she's crying by covering her eyes with a hand."
"เอมิโน้มตัวแล้วยกมือข้างหนึ่งขึ้นมาปิดตาไว้ไม่ให้เห็นว่าร้องไห้"

# "Of course, the subdued sobbing makes it pretty obvious that she's crying."
"แต่แน่ละว่าเสียงสะอึกสะอื้นอู้อี้นั้นทำให้รู้ชัดว่ากำลังร้องไห้อยู่"

# hi "Hey, I'm sorry."
hi "นี่ ขอโทษนะ"

# hi "Forget I said anything, okay?"
hi "คิดเสียว่าฉันไม่ได้พูดอะไรแล้วกัน"

show emi sad_depressed_close at center
with characlose

# "I place a hand gingerly around her and pull her close."
"ฉันโอบเอมิไว้อย่างแผ่วเบาแล้วรั้งตัวเธอเข้ามา"

# "I can think of nothing else to say or do. How do you comfort someone who's just lost their legs again?"
"ฉันไม่รู้จะพูดอะไรหรือทำยังไงดี เราต้องปลอบคนที่เสียขาไปอีกรอบยังไงนะ"

show emi sad_pout_close
with charachange

# "Emi wraps me in a hug and stays that way for a while."
"เอมิกอดฉันแล้วค้างไว้อย่างนั้นพักหนึ่ง"

# hi "Sorry."
hi "ขอโทษนะ"

# hi "I'm pretty bad at this whole comforting thing, I guess."
hi "ฉันปลอบคนอะไรแบบนี้ไม่ค่อยเก่ง"

# emi "Don't say that."
emi "อย่าพูดอย่างนั้นสิ"

# emi "I'm fine, really."
emi "ฉันไม่เป็นไรจริง ๆ"

# "Her voice is slightly muffled by my chest. I pat her head reassuringly."
"เสียงจากเธอที่ซุกหน้าอกฉันอยู่ฟังดูอู้อี้ ฉันลูบหัวเอมิปลอบ"

# hi "That's the spirit, right?"
hi "ต้องแบบนี้สิ"

# hi "You'll get through this fine, I know it."
hi "ฉันรู้ว่าสุดท้ายแล้วเธอจะไม่เป็นไรแน่นอน"

# hi "Besides, I'm here to help you, remember?"
hi "อีกอย่าง เธอก็ยังมีฉันคอยอยู่เคียงข้างช่วยเธอด้วย"

show emi sad_shy_close
with charachange

# "Emi lifts her head and stares at me with tear-stained eyes."
"เอมิเงยหน้าขึ้นแล้วมองด้วยตาที่ยังมีน้ำตาเหลืออยู่"

show emi sad_grin_close
with charachange

# emi "Can you? Can you really?"
emi "ช่วยได้เหรอ ช่วยได้จริง ๆ เหรอ"

# "She's grinning lopsidedly, and something sparkles in her gaze."
"เอมิยกยิ้มขึ้น แววตามีประกายบางอย่าง"

# "I can't tell if I'm being mocked or not."
"ไม่รู้ว่าเอมิล้อฉันอยู่หรือเปล่า"

# hi "Of course. I mean sure, you're a bit heavy, but -{w=0.5}{nw}"
hi "ได้สิ คือตัวเธอหนักก็จริง แต่—{w=0.5}{nw}"

play sound sfx_impact

show emi excited_amused_close
with vpunch

# extend " mmph!"
extend " อื้มม!"

# "My witty comment is cut off by the sudden press of Emi's lips on mine. I'm caught off guard, and am rewarded by hitting my head on the wall behind her bed."
"คำพูดหยอกล้อของฉันถูกตัดจบไปด้วยริมฝีปากเอมิที่เข้ามาประกบ เมื่อไม่ทันตั้งตัวหัวฉันจึงโขกเข้ากับกำแพง\nที่อยู่หลังเตียง"

# hi "Ow."
hi "โอ๊ย"

show emi basic_hes
with charadistant

# "Emi pulls back, trying to look concerned rather than like she's about to laugh."
"เอมิผละตัวออกปั้นสีหน้าให้ดูเหมือนเป็นห่วงทั้งที่กลั้นขำอยู่"

# emi "Are you okay?"
emi "เป็นอะไรหรือเปล่า"

show emi excited_proud
with charachange

# emi "Sorry!"
emi "ขอโทษที!"

# "I rub my head ruefully and grin back at her."
"ฉันลูบหัวร้องโอดโอยแล้วส่งยิ้มให้"

# hi "Caught me off guard, there."
hi "เล่นเอาไม่ทันตั้งตัวเลยนะ"

# hi "Is that going to become a habit? Am I going to be lectured by Shizune and Misha more?"
hi "เธอจะติดนิสัยทำแบบนี้หรือเปล่าเนี่ย นี่จะโดนชิซูเนะกับมิช่าเทศน์อีกบ่อยขึ้นมั้ย"

# "At the mention of the duo, Emi giggles."
"พอพูดถึงสองคนนั้นเอมิก็หัวเราะคิกคัก"

show emi basic_closedgrin
with charachange

# emi "Honestly, those two…"
emi "เอาจริง ๆ นะ สองคนนั้นน่ะ…"

show emi basic_grin
with charachange

# emi "If I didn't know why, I'd be utterly confused as to why she hangs around with someone so bossy."
emi "ถ้าไม่ได้รู้สาเหตุแล้วละก็ฉันคงยังไม่เข้าใจว่าทำไมถึงไปอยู่กับคนเจ้ากี้เจ้าการแบบนั้นได้"

# hi "Which one are we talking about?"
hi "หมายถึงใคร"

show emi basic_closedhappy
with charachange

# emi "You know exactly which one, Hisao. Misha's hardly bossy."
emi "นายรู้ว่าฉันพูดถึงใครฮิซาโอะ มิช่าน่ะไม่ได้ใกล้เคียงคำว่าเจ้ากี้เจ้าการเลย"

# hi "So what's the reason, then?"
hi "แล้วสาเหตุที่ว่าคืออะไร"

show emi basic_confused
with charachange

# emi "Huh?"
emi "หือ?"

# hi "The reason why Misha hangs around Shizune."
hi "สาเหตุว่าทำไมมิช่าถึงอยู่กับชิซูเนะ"

show emi basic_closedgrin
with charachange

# "Emi waves my question off with a smile."
"เอมิยิ้ม ๆ แล้วโบกมือเป็นเชิงบอกปัด"

# emi "No idea."
emi "ไม่รู้"

# hi "I see."
hi "อ้อ"

show emi basic_grin
with charachange

# emi "Anyway, you seem to be forgetting the original question, don't you?"
emi "แต่เอาเถอะ นายลืมที่ฉันถามไปทีแรกแล้วใช่มั้ย"

# hi "Oh yeah, I guess I am."
hi "อ้อ อืม ก็ไม่เป็นไรมั้งนะ"

# hi "You wouldn't mind giving a guy a little warning, would you?"
hi "จะทำอะไรก็เตือนก็บอกกันสักหน่อยได้มั้ย"

# hi "Otherwise I'm liable to wind up with a concussion."
hi "ไม่งั้นเดี๋ยวสมองฉันก็กระทบกระเทือนหรอก"

# "I emphasize the point by rubbing at the back of my head."
"ฉันลูบท้ายทอยเป็นการเน้นย้ำไปด้วย"

show emi excited_amused
with charachange

# "Emi giggles madly."
"เอมิหัวเราะคิกคักไม่หยุด"

# emi "You could wear a helmet."
emi "ใส่หมวกนิรภัยซะสิ"

show emi excited_proud
with charachange

# emi "Some kids here do, you know."
emi "คนในโรงเรียนนี้บางคนก็ใส่นะ"

stop music fadeout 1.0

# hi "Or I could just take revenge!"
hi "ไม่ก็แก้แค้นเอา!"

play sound sfx_pillow

show emi excited_circle
with vpunch

# "I grab a pillow from beside me and whack Emi over the head."
"ฉันคว้าหมอนที่อยู่ข้าง ๆ มาฟาดหัวเอมิ"

show expression im.Composite((295,1200), (0,0), "sprites/emi/emi_excited_circle.png") as emi:
   xalign 0.5 yanchor 0.5 ypos 1.0 subpixel True
   easeout 0.8 ypos 1.25 rotate -90
with None

show expression im.Composite((295,1200), (0,0), "sprites/emi/emi_excited_sad.png") as emi:
   xalign 0.5 yanchor 0.5 ypos 1.0 subpixel True
   easeout 0.8 ypos 1.25 rotate -90

with Dissolve(0.5)
with Pause(0.3)

play sound sfx_impact

hide emi
with vpunch

# "Emi topples off the bed and lands on the floor with a thump."
"ตัวเอมิล้มตกจากเตียงกระทบกับพื้นดังตุบ"

show emi sad_pout:
   center
   ypos 1.2
   ease 1.0 ypos 1.0
with Dissolve(1.0)

# "Her arms promptly reappear on the bed, and she manages to pull herself back up."
"แขนเอมิโผล่ขึ้นมาที่ริมเตียง เธอดึงตัวเองกลับขึ้นมาได้"

# "She really has a surprising amount of strength in that little body."
"เห็นตัวเล็กอย่างนี้แต่แรงเยอะผิดคาดเลยแฮะ"

# "Her face is turned downwards and away from mine, making me think I might have accidentally hurt her."
"เอมิก้มหน้างุดบิดหนีไปอีกทางจนฉันคิดว่าอาจเผลอทำให้เธอเจ็บจริง ๆ"

# hi "Emi? You okay?"
hi "เอมิ ไหวหรือเปล่า"

# hi "You didn't hit your—{w=0.3}{nw}"
hi "หัวไม่ได้ฟา—{w=0.3}{nw}"

show emi excited_smile_close
with vpunch

# "A hand shoots up and grabs my collar. She pulls me in with a sharp tug, her face now barely an inch away from mine as she grins cheekily."
"มือเอมิพุ่งเข้ามากระชากคอเสื้อฉันจนหน้าเราอยู่ห่างจากกันไม่กี่เซนติเมตร เธอยิ้มเหมือนยั่วล้อ"

# hi "Emi…?"
hi "เอมิ…?"

show emi excited_smile_close:
   subpixel True
   linear 0.1 ypos 1.7 zoom 2.0
with None

scene white
with Dissolve(0.1)

play sound sfx_impact

scene black
with Dissolve(0.75)

# "She gives me a sharp headbutt, our foreheads making quite a loud thud."
"แล้วเอมิก็โขกหน้าผากกับฉันจนเกิดเสียงดังกึก"

scene bg school_dormemi at right
show emi basic_closedgrin at center
with openeye

# "I sit back and rub my now sore head as Emi smirks victoriously."
"ฉันถอยออกมาลูบหน้าผากที่เจ็บอยู่ ส่วนเอมิก็ยิ้มอย่างผู้มีชัย"

show emi basic_grin
with charachange

# emi "How's {b}that{/b} for revenge?"
emi "แก้แค้น{b}แบบนี้{/b}เป็นไงล่ะ"

play music music_running

# hi "No fair!"
hi "ไม่ยุติธรรมเลย!"

# hi "You can't take revenge for revenge!"
hi "จะมาแก้แค้นการแก้แค้นได้ยังไง!"

# "For someone missing most of her legs, Emi's surprisingly agile."
"ทั้งที่ขาหายไปเกือบครึ่งแล้วแต่เอมิก็ว่องไวเกินคาด"

show emi basic_grin:
    center
    parallel:
        "emi basic_closedgrin" with Dissolve(0.2, alpha=True)
    parallel:
        easeout 0.5 xpos 0.3 alpha 0.0
with Pause(0.5)

hide emi
with None

# "I swipe at her, but she deftly rolls out of the way and lands a hit with her pillow."
"ฉันเล็งเอมิอีกรอบ แต่เธอก็กลิ้งตัวหลบไปได้แล้วเอาหมอนมาฟาดฉัน"

# "Of course, the odds are against her. I can stand up, for starters."
"แน่นอนว่าสภาพสนามรบนั้นไม่เป็นใจกับเอมิ เช่นว่าการที่ฉันยืนได้"

scene black
with vpunch

# "Oof!"
"อุ๊ก!"

window hide

show evh emi_grinding_victorytall:
    xalign 0.5 yalign 1.0 subpixel True
    easein 12.0 yalign 0.0

with Dissolve(1.0)

with Pause(6.0)

window show

# "Guess I can't, after all. Emi seems to have effectively tripped me up, and is now sitting primly astride me as I lay on my back. I'm not even sure how she managed it."
"ดูท่าว่าจะยืนไม่ได้ เอมิทำให้ฉันสะดุดล้มได้ และตอนนี้เธอก็นั่งทับฉันที่นอนหงายอยู่แล้ว ไม่รู้เหมือนกันว่าทำได้ยังไง"

# emi "I win!"
emi "ชนะแล้ว!"

# "Her eyes twinkle mischievously. I've been thoroughly defeated, and by a girl that's a fraction of my size, at that."
"ตาเอมิฉายแววเจ้าเล่ห์ ฉันแพ้ราบคาบ แล้วคนที่เอาชนะฉันดันเป็นเด็กผู้หญิงที่ตัวเล็กกว่าฉันอีก"

# "Then again, being defeated doesn't seem quite so bad. Emi being positioned over my waist isn't something that I, or my body, can ignore easily."
"แต่ก็ไม่แย่เท่าไหร่ที่แพ้ ฉัน—ร่างกายฉัน—ไม่อาจเมินเอมิที่นั่งอยู่บริเวณเอวฉันได้"

scene bg school_dormemi
with locationchange

# "I open my lips to speak, but Emi's head darts downwards before I can get so much as a word out. I give no resistance as she presses her mouth to mine, not that I'd want to."
"ฉันเปิดปากจะพูด แต่เอมิก็โน้มหัวลงมาก่อนที่ฉันจะทันได้พูดอะไร ฉันไม่ขัดขืนที่เธอแนบริมฝีปากกับฉัน ซึ่งฉัน\nก็ไม่ได้อยากขัดขืนหรอก"

# "This is… different, somehow."
"ไม่เหมือน… ทุกทียังไงไม่รู้"

# "She pulls back, nips at my lower lip, and reinitiates the embrace. Her tongue darts inside my mouth, exploring. I can feel a warmth spreading through my body as my heart begins to beat faster."
"เอมิผละออกเล็กน้อยพลางกัดริมฝีปากล่างฉันก่อนจะกอดอีกรอบ เธอสอดลิ้นเข้ามาวนเวียนในโพรงปากฉัน\nทั้งตัวฉันร้อนรุ่ม หัวใจฉันเริ่มเต้นเร็วขึ้น"

# "My mind starts to go foggy, and I become vaguely aware of my hand traveling up Emi's blouse. Emi gasps as I reach a breast, then there's a giggle, and then—"
"สมองฉันเริ่มตื้อ มือฉันไต่ขึ้นไปตามเสื้อเอมิโดยแทบไม่รู้ตัว เธอสะดุ้งเฮือกเมื่อฉันจับเข้าที่หน้าอก แล้วเธอ\nก็หัวเราะคิกคัก แล้ว—"

scene evh emi_grinding_victory
with locationchange

# "I stare up at a grinning Emi."
"ฉันเงยหน้ามองเอมิที่ยิ้มอยู่"

# emi "Told you. That makes my second win, now."
emi "บอกแล้วไง คราวนี้ฉันก็ชนะเป็นครั้งที่สองแล้ว"

# hi "What? That doesn't count; you used feminine wiles."
hi "ฮะ? ไม่นับสิ เธอใช้มารยาหญิงนี่"

show evh emi_grinding_wink
with charachange

# emi "“All's fair in love and war,” right?"
emi "“ยามรักยามรบทำอะไรก็ไม่ผิด” นี่"

# emi "Ha, and you're even blushing! I didn't know you were a blusher, Hisao."
emi "ฮ่า แล้วนายหน้าแดงด้วย! ไม่ยักรู้ว่าฮิซาโอะเป็นคนหน้าแดงง่ายนะเนี่ย"

# hi "You were blushing too, you know. Probably because of your prudish ways."
hi "เธอก็หน้าแดงเหมือนกันหรอก อาจจะเพราะเธอนั่นแหละที่เป็นคนไม่เดียงสา"

# "Even I've got to admit this is a stupid thing to say to a woman who is currently straddling me and has been, up until a few seconds ago, playing tonsil hockey with me."
"แม้แต่ฉันยังต้องยอมรับว่าคำพูดเมื่อกี้เป็นอะไรที่ไม่น่าพูดกับผู้หญิงที่นั่งทับฉันอยู่และเมื่อไม่กี่วินาทีที่แล้ว\nเพิ่งแลกลิ้นกันไปกับฉัน"

show evh emi_grinding_grin
with charachange

# emi "A prude, am I?"
emi "ฉันน่ะเหรอไม่เดียงสา"

# emi "Well then, let's see who blushes first, shall we?"
emi "งั้นก็มาแข่งกันว่าใครจะหน้าแดงก่อนดีมั้ย"

# "I'm not sure whether the tone of her voice terrifies or arouses me, but that question is quickly made rather moot."
"ฉันไม่แน่ใจว่าพอได้ยินเสียงเอมิแบบนั้นแล้วฉันกลัวหรือตื่นตัวกันแน่ แต่ไม่นานฉันก็ไม่ต้องคิดหาคำตอบ"

label th_E20h:

show evh emi_grinding_half_undress
with charachange

show evh emi_grinding_half_grin
with charachange

# "In a motion of practiced ease, she peels her blouse off and tosses it carelessly aside. Her bra and skirt quickly follow it onto the floor."
"เอมิถอดเสื้อออกแล้วโยนทิ้งไปแบบลวก ๆ อย่างคล่องแคล่วและง่ายดาย ไม่นานเสื้อชั้นในกับกางเกงก็ตามไปสมทบ\nกับกองนั้น"

# emi "Ha!"
emi "ฮ่า!"

# "I fight the urge to blush. It's a rather hard task."
"ฉันกลั้นใจไม่ให้หน้าแดง ซึ่งก็ยากพอสมควร"

# hi "Escalation, is it?"
hi "เพิ่มระดับงั้นเหรอ"

show evh emi_grinding_off_yawn
with charachange

# "My own shirt follows suit, albeit with some difficulty thanks to my position. Emi mock-yawns."
"ฉันถอดเสื้อตาม แต่ก็ถอดลำบากเล็กน้อยเพราะนอนอยู่ เอมิทำท่าหาวเป็นการล้อ"

# emi "You'll have to try harder than th—"
emi "ต้องทำให้มากกว่านี้สิถ้านายจะ—"

show evh emi_grinding_off_closesurprise
with charachange
stop music fadeout 3.0

# emi "Ah…!"
emi "อ๊ะ…!"

# "My hands gently caress Emi's bare skin, causing her to shiver. It would seem that my hands are acting on their own, again. If our position had let me, I'd probably have finished her undressing for her."
"มือฉันสัมผัสผิวเปลือยเอมิจนเธอตัวสั่น ดูเหมือนว่ามือฉันจะขยับไปเองอีกแล้ว ถ้าอยู่ในท่าที่สะดวกกว่านี้ฉันคง\nถอดเสื้อผ้าให้เอมิจนหมด"

# "I start to say something about how Emi's starting to blush, but both of us are very rapidly reaching the edge of something very barely holding us back. Conversation grinds to a halt, and I feel my arms losing energy."
"ฉันพูดอะไรสักอย่างจนเอมิเริ่มหน้าแดง ทว่าเราสองคนก็เข้าใกล้ถึงขีดจำกัดนั้นที่ต่างรั้งตัวเราทั้งสองคนไว้ไปเรื่อย ๆ\nบทสนทนาหยุดชะงักลง แขนฉันเริ่มไม่มีแรงแล้ว"

play music music_one fadein 0.5

# "Neither of us, however, is prepared for this sudden new sensation."
"แต่เราทั้งสองคนต่างไม่มีใครที่ได้เตรียมใจรับมือกับความรู้สึกใหม่ที่ผุดขึ้นมานี้เลย"

show evh emi_grinding_off_closearoused
with charachange

# "An indescribable heat surges through me, coming from both myself and, it seems, Emi as well."
"ความร้อนรุ่มปริมาณมหาศาลแผ่ซ่านไปทั่วร่าง โดยมาจากฉันและเหมือนจะมาจากเอมิด้วย"

# "With one hand on my chest to steady herself, and another holding mine to make sure that I can't have my way with her body again, she looks quite pleased with herself."
"เอมิดูจะพอใจที่ได้เอามือข้างหนึ่งจับมือฉันไว้ไม่ให้แตะตัวเธออีก โดยอีกข้างคอยประคองตัวเองยันกับหน้าอกฉันไว้"

show evh emi_grinding_off_aroused
with charachange

# "And then, after a moment's hesitation, she moves."
"เอมิลังเลอยู่พักหนึ่งก่อนจะขยับตัว"

# "And she moves again."
"และขยับตัวอีกครั้ง"

# "And again."
"และอีกครั้ง"

# "As she moves, Emi's breath hitches. My breathing is starting to come faster, and more raggedly as well."
"ระหว่างที่ขยับ ลมหายใจของเอมิก็กระชั้นขึ้น ฉันเองก็เริ่มหอบถี่หนักขึ้นแล้วเหมือนกัน"

# "Emi's body shivers and shudders against mine, and I can feel her starting to lose her balance. It must be harder for her to keep steady because she's missing her legs."
"ตัวเอมิกระตุกสั่นอยู่บนตัวฉัน ฉันสัมผัสได้ว่าเอมิเริ่มเสียการทรงตัวแล้ว คงจะประคองตัวเองลำบากหน่อย\nเพราะไม่มีขา"

show evh emi_grinding_off_closesurprise
with charachange

# "I steady her as best as I can, cupping my hands around her backside. It's firm and taut."
"ฉันคอยประคองตัวเอมิไว้ด้วยการจับบั้นท้ายเธอเอาไว้ ก้นเอมินั้นทั้งแน่นทั้งแข็ง"

# "Makes sense, considering how much she runs. The potential power in those muscles makes them flex as she responds to my touch."
"ก็ไม่แปลก เพราะวิ่งเยอะขนาดนั้น พละกำลังที่แฝงอยู่ทำให้ฉันสัมผัสได้ถึงมัดกล้ามเนื้อตอนที่เอมิตอบสนอง\nกับมือฉัน"

# "What I fail to take into account is the fact that my attempt to steady Emi kind of slides her forward and, well… It feels amazing."
"ที่ฉันลืมคิดไปก็คือเมื่อฉันคอยประคองเอมิแบบนี้แล้วตัวเธอก็จะเคลื่อนมาข้างหน้าด้วย ซึ่งก็… รู้สึกดีมาก"

show evh emi_grinding_off_arousedclosed
with charachange

# "Her panties slide easily against my trousers, and it doesn't take us long to figure out a rhythm."
"กางเกงในเธอถูไถอยู่กับกางเกงฉัน ไม่นานเราก็จับจังหวะกันได้"

# "But Emi refuses to keep to it, going now fast, now slow, now pausing for what feels like an eternity. I'm not sure whether she's doing this to toy with me, or if it's to make her feel better, but I'm well past caring."
"แต่เอมิไม่ยอมขยับตามจังหวะ บ้างก็เร็ว บ้างก็ช้า บ้างก็หยุด เธอทำอย่างนั้นอยู่เสียนาน แต่ฉันไม่แน่ใจว่าที่ทำแบบนี้\nเพื่อจะแกล้งฉันหรือเพื่อจะทำให้ตัวเองรู้สึกดีกันแน่ ซึ่งฉันไม่ได้สนใจแล้ว"

# "The heat between us is growing more intense, and I can't hold back a gasp. The noise only seems to drive Emi along."
"อุณหภูมิในอากาศรอบตัวเรายิ่งเพิ่มสูงไปอีก ฉันกลั้นเสียงร้องไว้ไม่ได้แล้ว และเหมือนเสียงนั้นจะทำให้เอมิตื่นตัวไปอีก"

# "I begin to punctuate her movements with some of my own, which causes her modest breasts to bounce in time with my movements. Her breath begins to come faster as we continue, my own breathing becoming equally quick."
"ฉันเริ่มประสานจังหวะให้เข้ากันกับเอมิบ้างจนหน้าอกที่มีพอประมาณของเธอขยับไปตามการเคลื่อนไหว ยิ่งเรา\nทำไปเรื่อย ๆ ลมหายใจของเอมิก็หอบถี่ขึ้น ฉันเองก็เริ่มหอบไม่ต่างกัน"

# "With her eyes closed, her lips purse expectantly. I just manage to lift myself up for a few moments. Our mouths seeking one another, her chest sliding against mine as our sweat mingles."
"เอมิหลับตาแล้วเม้มปากคล้ายรออะไรบางอย่าง ฉันโน้มตัวเองให้ลุกขึ้นมาอยู่ครู่หนึ่ง ปากของเราประกบกัน\nหน้าอกเธอแนบกับหน้าอกฉัน เหงื่อของเราถูกตัวกันและกัน"

# "As I flop back down, my trousers are soaked with sweat. I would take them off if it didn't mean stopping what we're doing."
"พอฉันล้มตัวกลับมานอนอย่างเดิมกางเกงก็ชื้นเหงืื่อไปหมด ถ้าไม่ติดว่าต้องหยุดก่อนฉันก็คงถอดไปแล้ว"

# "And I don't want to stop what we're doing, stop this growing pressure, this tickling in the back of my brain."
"และฉันก็ไม่อยากหยุด ไม่อยากหยุดความรู้สึกที่รุนแรงขึ้นเรื่อย ๆ นี้ ไม่อยากหยุดความเสียวซ่านในหัวนี้"

# "Emi is sliding faster and faster, panting heavily, her voice seemingly unable to convey what she's feeling. Her body, on the other hand, is doing a fine job."
"เอมิเคลื่อนตัวเร็วขึ้นทุกขณะ เธอหอบหนักจนเสียงจากปากเธอถ่ายทอดความรู้สึกตัวเองไม่ได้แล้ว แต่ร่างกายเธอ\nส่งผ่านออกมาได้อย่างแจ่มแจ้ง"

show evh emi_grinding_off_come
with charachange

# "Suddenly she moves a little more erratically as my own breath hitches in my throat, ending in a final desperate thrust that sends me over the edge into a surging feeling I didn't know existed."
"อยู่ ๆ เอมิก็ขยับตัวรุนแรงขึ้น ฉันหอบครางอยู่ในลำคอไปพลางดันตัวอย่างกระเสือกกระสนจนคลื่นความรู้สึก\nที่ฉันไม่เคยรู้จักมาก่อนเข้าถาโถมใส่"

scene white
with Dissolve(3.0)

# "My mind blanks, fills with white noise, and I succumb to the feeling of climax. For a few seconds, everything else in the world falls away except for this amazing feeling of Emi and I, together."
"หัวสมองฉันว่างเปล่า เหลือเพียงสติที่พร่าเลือน ฉันกำซาบความรู้สึกหลังจากที่ถึงฝั่งแล้ว ราวกับว่าทั้งโลกรอบตัว\nได้เลือนหายไป เหลือเพียงความรู้สึกแสนสุดยอดที่เอมิกับฉันได้อยู่ด้วยกันนี้"

show evh emi_grinding_off_end
with Dissolve(1.0)

# "And then… it passes. The white noise clears, and I am left staring up into the eyes of the girl atop me."
"และแล้ว… ก็จบลง สติกลับมาแจ่มชัดขึ้น ฉันมองตาเด็กสาวที่นั่งทับฉันอยู่"

# "For a few minutes, neither of us speaks. The sound of our breathing fills the room, our chests heaving from the experience."
"เราต่างไม่พูดอะไรกันอยู่สองสามนาที ในห้องมีเพียงเสียงหายใจของเรา หน้าอกของเรากระเพื่อมขึ้นลงจากกิจกรรม\nเมื่อครู่"

# "She eventually, reluctantly, shifts off of me and sits against the wall. I join her."
"สุดท้ายเอมิก็ขยับออกลงไปจากตัวฉันด้วยท่าทีเหมือนอยากอยู่ต่อแล้วนั่งพิงกำแพง ส่วนฉันก็ไปนั่งข้าง ๆ"

label th_E20x:

scene bg school_dormemi at right
with locationchange

show eminude smile_close
with charachange

# emi "So… did I blush?"
emi "แล้ว… ฉันหน้าแดงมั้ย"

# hi "I didn't notice."
hi "ไม่ทันสังเกต"

# hi "Did I?"
hi "แล้วฉันล่ะ"

show eminude neutral_close
with charachange

# "Emi shrugs, still breathing a little heavily."
"เอมิยักไหล่ เธอยังหอบอยู่หน่อย ๆ"

show eminude weaksmile_close
with charachange

# emi "Didn't notice either."
emi "ฉันก็ไม่ทันสังเกต"

# hi "Well, maybe we should—"
hi "งั้น หรือว่าเรามา—"

play sound sfx_dooropen

stop music fadeout 0.3

show rin basic_deadpan behind eminude:
    center
    xpos 1.0 xanchor 0.0 alpha 0.0 subpixel True
    easein 0.5 right alpha 1.0
show eminude blush_close
with vpunch

# rin "I need to use your window."
rin "ขอใช้หน้าต่างหน่อย"

# "My first instinct is to hide, but then I realize that I'm still utterly exhausted and sitting next to a topless Emi, so there's no running anyway."
"สัญชาตญาณฉันสั่งให้ซ่อนตัว แต่ก็นึกได้ว่าทั้งตัวฉันไม่มีแรงเหลือแล้ว และนั่งอยู่ข้างเอมิที่ไม่ได้ใส่เสื้อท่อนบน\nไว้เลย เพราะงั้นคงหนีไปไหนไม่ได้อีก"

show rin basic_awayabsent:
    right alpha 1.0
with charachange

show rin basic_absent
with charachange

show rin basic_awayabsent
with charachange

# "Rin's eyes pass over Emi, and me, and focus on the window."
"รินหันมามองเอมิ มองฉัน ก่อนจะกลับไปจ้องหน้าต่าง"

show rin basic_deadpannormal
with charachange

# rin "There was a cloud."
rin "มีเมฆอยู่ก้อนหนึ่ง"

play music music_comedy fadein 0.5

show eminude neutral_close
with charachange

# emi "A cloud?"
emi "เมฆ?"

show rin basic_lucid
with charachange

# "Rin nods."
"รินพยักหน้า"

show rin relaxed_nonchalant
with charachange

# rin "I was watching it from my window, but it didn't stay in my window."
rin "ฉันนั่งดูอยู่ที่หน้าต่าง แต่มันหนีออกไปจากหน้าต่างฉัน"

show rin negative_spaciness
with charachange

# rin "So I need to use your window."
rin "เลยต้องมาดูที่หน้าต่างเธอ"

show eminude closedsmile_close
with charachange

# "Emi shifts a little, causing me to cough in order to cover up a giggle of my own."
"เอมิเขยิบตัว ฉันแสร้งทำไอกลบเกลื่อนที่ตัวเองหัวเราะอยู่"

# emi "How long do you need the window for?"
emi "แล้วจะดูนานมั้ย"

# emi "We're uh."
emi "พวกเรา เอ่อ"

show eminude wink_close
with charachange

# emi "Busy."
emi "ยุ่งอยู่"

# "This time I can't contain my laughter."
"คราวนี้ฉันกลั้นขำไม่อยู่แล้ว"

show rin negative_annoyed
with dissolvecharamove

# "Rin ignores both Emi and me and peers out the window."
"รินเมินทั้งเอมทั้งฉันแล้วมองหน้าต่าง"

show rin basic_deadpanupset
with charachange

# "Her shoulders slump, and she looks disappointed."
"รินหย่อนไหล่ลงดูผิดหวัง"

# rin "Hmm."
rin "อืมม"

# rin "It changed into something else."
rin "เปลี่ยนเป็นอย่างอื่นไปแล้ว"

# rin "Disappointing."
rin "น่าผิดหวัง"

show eminude grin_close
with charachange

# "Emi is having trouble keeping a straight face."
"เอมิกำลังปั้นสีหน้าให้ดูปกติสุดชีวิต"

# emi "Sorry to hear that, Rin."
emi "เสียใจด้วยนะริน"

show eminude pout_close
with charachange

# emi "Could we have a little privacy now, please?"
emi "ทีนี้ก็รบกวนขอความเป็นส่วนตัวให้เราสองคนหน่อยได้มั้ย"

show rin relaxed_nonchalant
with charachange

with Pause(0.2)

show rin relaxed_nonchalant:
    easeout 1.0 xpos 1.0 alpha 0.0 xanchor 0.0 subpixel True
with Pause(1.0)

play sound sfx_doorclose

hide rin
with None

# "Rin shrugs, as if to say “Can you?” and hooks her foot around the door, pulling it closed behind her."
"รินยักไหล่คล้ายจะบอกว่า “แล้วทำได้หรือเปล่าล่ะ” ก่อนจะใช้เท้าเกี่ยวประตูแล้วปิด"

show eminude happy_close
with charachange

# "We both dissolve into raucous laughter, unable to deal with Rin's bizarrely timed visit any other way."
"เราระเบิดหัวเราะดังลั่นเพราะตลกที่รินเลือกจังหวะเข้ามาได้พิลึกพิลั่นดีเหลือเกิน"

# "After our laughter dies down, I look to Emi. We're both a total mess."
"พอหัวเราะกันเสร็จแล้วฉันก็หันไปมองเอมิ สภาพเราสองคนดูไม่ได้เลย"

stop music fadeout 5.0

# hi "Well."
hi "โอเค"

show eminude neutral_close
with charachange

# "Emi raises an eyebrow."
"เอมิเลิกคิ้ว"

# emi "Well?"
emi "โอเค?"

# hi "Again?"
hi "อีกรอบมั้ย"

show eminude wink_close
with charachange

# "Emi grins and laughs, and then she nods."
"เอมิยิ้มแล้วหัวเราะ จากนั้นก็พยักหน้า"

show eminude grin_close
with charachange

# emi "We should probably ditch the clothes, this time."
emi "คราวนี้ถอดเสื้อผ้ากันให้หมดเลยดีกว่า"

$ suppress_window_after_timeskip = True

scene black
with dissolve

########################################################
label th_E21:

window hide None

play sound sfx_alarmclock

with Pause(2.0)

scene bg school_dormhisao
with openeye

window show

# "The sunlight breaks through my window shortly before my alarm ruins the morning silence."
"แสงอาทิตย์ส่องลอดหน้าต่างมาก่อนที่นาฬิกาปลุกจะดังทำลายความเงียบยามเช้า"

play music music_dreamy fadein 6.0

# "I feel sore."
"ระบมไปหมด"

# "The events of the previous evening suddenly intrude upon my consciousness, and I find myself blushing."
"เหตุการณ์เมื่อเย็นวานแทรกตัวเข้ามาในความคิดจนฉันหน้าแดง"

# "That was an eventful evening - and it explains perfectly the soreness in my lower back."
"เป็นยามเย็นที่ไม่น่าเบื่อเลย และยังเป็นสาเหตุด้วยว่าทำไมหลังท่อนล่างฉันถึงปวด ๆ"

# "The walk back, as I recall, had been rather tense."
"เท่าที่นึกออก ตอนเดินกลับนั้นลำบากอยู่"

# "My trousers having been… soiled, I had washed them off in the bathroom before going back to my room."
"กางเกงฉันที่… เปื้อนนั้นฉันต้องเอามาซักที่ห้องน้ำก่อนกลับเข้าห้อง"

# "But there was still a fairly obvious-looking stain on the front."
"แต่ตรงเป้าก็ยังเห็นเป็นรอยชัดอยู่"

# "Fortunately for me, the only person I ran into on my way back was Kenji."
"โชคดีที่คนที่ฉันเจอตอนเดินกลับมามีแค่เคนจิ"

# "And he didn't notice a thing."
"และเคนจิก็ไม่สังเกตเห็นอะไรเลย"

# "Well, apart from my being in the general vicinity."
"เห็นก็แต่ว่าฉันเข้าใกล้เขาอะนะ"

# "Of course he'd asked how the night went, and whether or not I'd learned anything of importance."
"แน่ละว่าเคนจิถามว่าเย็นนั้นเป็นไงบ้าง และถามว่าได้รู้อะไรที่สำคัญมาบ้างหรือเปล่า"

# "I don't even know if I opened my mouth to answer; I was too tired to care."
"ฉันไม่รู้ว่าได้เปิดปากตอบไปหรือเปล่าเพราะเพลียเกินกว่าจะไปสนใจแล้ว"

# "And this morning, I'll admit that I'm feeling pretty worn out."
"และต้องยอมรับว่าเช้านี้ฉันก็ยังล้าอยู่พอสมควร"

# "Still, Emi had promised to meet me at the track, and I'd hate to disappoint."
"แต่เอมิก็สัญญาไว้แล้วว่าจะไปรอเจอฉันที่ลู่วิ่ง จะทำให้ผิดหวังก็คงไม่ดี"

scene bg school_track
show emiwheel weaksmile at center
with locationskip

# "She is indeed waiting for me when I arrive."
"พอไปถึงก็เห็นว่าเอมิรออยู่จริง ๆ"

# "Doing her best to look cheery, despite the fact that she's sitting in a wheelchair."
"โดยทำตัวให้ดูร่าเริงอย่างเต็มที่ทั้งที่นั่งวีลแชร์อยู่"

# "I wave to her and begin stretching."
"ฉันโบกมือให้เอมิก่อนจะยืดเส้นยืดสาย"

# hi "You're early."
hi "มาเช้านะ"

show emiwheel frown
with charachange

# "Emi frowns and shakes her head."
"เอมิขมวดคิ้วแล้วสั่นหัว"

show emiwheel angry
with charachange

# emi "Ridiculous."
emi "ไร้สาระ"

# emi "{b}You're{/b} late."
emi "{b}นาย{/b}น่ะมาช้า"

show emiwheel grin
with charachange

# emi "Overslept, Hisao?"
emi "นอนเพลินเหรอฮิซาโอะ"

show emiwheel wink
with charachange

# emi "All tuckered out?"
emi "หมดแรงข้าวต้มเลยงั้นสิ"

# "Well, at least she seems more like her old self."
"โอเค อย่างน้อยก็ดูเป็นเอมิคนเดิมหน่อยละนะ"

# "And as expected, she doesn't seem that shy about mentioning our… previous activities."
"และตามคาด เอมิดูจะไม่อายกับการพูดถึงเรื่อง… กิจกรรมที่ผ่านมาของเรา"

# hi "Hey, you're lucky I could show up at all."
hi "นี่ ฉันมาได้ก็บุญแค่ไหนแล้ว"

# hi "All that cardiovascular activity last night, I nearly thought I'd have to see the nurse afterwards."
hi "เย็นเมื่อวานหัวใจฉันทำงานหนักจนนึกว่าจะต้องไปหาคุณพยาบาลแล้วนะนั่น"

show emiwheel wink
with charachange

# "Emi laughs out loud, then her face suddenly becomes concerned."
"เอมิหัวเราะออกมาก่อนจะทำหน้าคิดมากขึ้นมาทันที"

show emiwheel blush
with charachange

stop music fadeout 8.0

# emi "Hey, that's not uh…"
emi "นี่ มันก็ไม่ได้ เอ่อ…"

# emi "I mean, you're not…"
emi "คือนายก็ไม่ได้…"

# hi "Go on, spit it out."
hi "พูด ๆ ออกมาเถอะน่า"

show emiwheel awayfrown
with charachange

# emi "It's just that it would be hard to explain if you had an episode while we were…"
emi "แค่คิดว่าคงไม่รู้จะอธิบายยังไงดีถ้าเกิดว่านายอาการกำเริบขึ้นมาตอนที่เรา…"

# hi "Oh."
hi "อ้อ"

# hi "{b}Oh.{/b}"
hi "{b}อ้อ{/b}"

# "Now that she mentions it, it really is a legitimate concern."
"จะว่าไปแล้วก็ดูเป็นอะไรที่น่าจะเป็นไปได้จริง ๆ"

# "I certainly hadn't thought of it last night, of course - other, more pressing concerns had been at hand."
"ซึ่งแน่นอนว่าเมื่อวานฉันไม่ได้คิดถึงเรื่องนี้เลย เพราะมีเรื่องอื่นที่สำคัญกว่าที่ต้องคิด"

# hi "Well, I don't think anything we, er, {b}do{/b} is going to be any more of a strain than these morning runs, and I handle those fine, so…"
hi "ก็ ฉันว่าไอ้ที่เรา เอ้อ {b}ทำ{/b}กันมันก็ไม่ได้หนักหน่วงไปกว่าการวิ่งรอบเช้าที่เราวิ่งกันหรอก แล้วฉันก็วิ่งไหวอยู่\nเพราะงั้น…"

show emiwheel frown
with charachange

# "Emi considers this point."
"เอมิคิดตาม"

show emiwheel evil
with charachange

# "A devious light appears in her eyes."
"แล้วตาเธอก็ฉายแววชั่วร้าย"

play music music_emi fadein 2.0

# emi "Say…"
emi "อ่า…"

# hi "Hmm?"
hi "หืม"

show emiwheel grin
with charachange

# "The light vanishes, and Emi grins ruefully at me."
"แววตานั้นหายไป เอมิยิ้มเจื่อน ๆ ให้ฉัน"

# "I can't help but feel vaguely suspicious."
"ฉันอดสงสัยขึ้นมาหน่อย ๆ ไม่ได้"

show emiwheel happy
with charachange

# emi "I seem to have forgotten a pair of gloves."
emi "เหมือนฉันจะลืมถุงมืออะ"

# hi "What do you need gloves for?"
hi "แล้วจะเอาถุงมือไปทำอะไร"

show emiwheel smile
with charachange

# "Emi indicates the chair upon which she is seated."
"เอมิชี้นิ้วไปที่วีลแชร์ที่เธอนั่งอยู่"

# emi "For this, of course!"
emi "ก็เจ้านี่ไง!"

show emiwheel wink
with charachange

# emi "Sure, regular moving around is all well and good without 'em, but I want to be able to get a good workout."
emi "ถ้าจะไปไหนมาไหนตามปกติแล้วไม่ใส่ถุงมือก็ได้อยู่หรอก แต่ฉันอยากออกกำลังกายไปด้วย"

show emiwheel grin
with charachange

# emi "And to get that kind of speed, you gotta have gloves if you don't want blisters."
emi "แล้วถ้าจะไปให้เร็วแบบนั้นฉันก็ต้องใส่ถุงมือไม่ให้มือพอง"

# hi "So what, are you wussing out on me then? Do I have to go it alone?"
hi "แล้วยังไง นี่กลัวเหรอ จะให้ฉันวิ่งคนเดียวงั้นสิ"

show emiwheel awayfrown
with charachange

# "Emi thinks for a minute - or pretends to think."
"เอมิคิด—หรืออาจจะทำเป็นคิดเฉย ๆ —อยู่สักหนึ่งนาทีได้"

show emiwheel closedsmile
with charachange

# emi "Hmm… if I remember right, there's a spare pair or two in the track shed."
emi "อืมม… ถ้าจำไม่ผิด เหมือนมีถุงมือสำรองอยู่สักคู่สองคู่ในห้องเก็บของของสนามอยู่นะ"

# "So she does seriously want to do it, then."
"ก็คืออยากจะ{i}วิ่ง{/i}จริง ๆ สินะ"

# "But in her normal school uniform? I'd have expected her to wear her gym outfit for something like this."
"แต่จะวิ่งทั้งชุดนักเรียนเนี่ยเหรอ นึกว่าคนอย่างเอมิจะใส่ชุดพละกับการทำอะไรแบบนี้เสียอีก"

# hi "Wait, what are they doing there?"
hi "เดี๋ยว แล้วทำไมในห้องนั้นถึงมีถุงมือด้วย"

show emiwheel frown
with charachange

# "Emi looks askance at me."
"เอมิมองค้อนใส่ฉัน"

# emi "Seriously? You can't think of why a shed full of track supplies at a school for the disabled would have racing gloves?"
emi "ถามจริง? นี่นายคิดไม่ได้เลยเหรอว่าทำไมห้องเก็บของที่มีอุปกรณ์กีฬาครบครันในโรงเรียนสำหรับคนพิการ\nจะต้องมีถุงมือสำหรับแข่งด้วย"

# "Well, when she puts it that way, I suppose that makes perfect sense."
"อืม พอเอมิพูดอย่างนี้แล้วก็พอจะรู้สึกสมเหตุสมผลขึ้นมาบ้าง"

# hi "Hey, I'm still getting used to this place. Give me a break, huh?"
hi "นี่ ฉันก็กำลังปรับตัวกับโรงเรียนนี้อยู่ อย่าว่าฉันนักเลย"

show emiwheel grin
with charachange

# emi "I guess I can let it slide this time."
emi "ครั้งนี้ฉันจะไม่อะไรกับนายต่อแล้วกัน"

show emiwheel wink
with charachange

# emi "Now come on, I'll need your help."
emi "เอ้า เร็ว ๆ ตามมาช่วยฉันด้วย"

# "I can't imagine what for, but then again I didn't have a clue why racing gloves would be in the shed, so I'm not willing to press the issue."
"ฉันนึกไม่ออกว่าจะให้ไปช่วยอะไร แต่ก็นะ ฉันนึกไม่ออกเหมือนกันว่าทำไมห้องเก็บของถึงได้มีถุงมือด้วย ฉันจึงตัดใจ\nไม่ซักไซ้ต่ออีก"

scene bg school_sportsstoreext
with locationchange

# "Emi navigates her way to the shed easily enough, though I can hear her grumbling under her breath."
"เอมิเคลื่อนตัวมาที่ห้องเก็บของได้อย่างไม่ลำบากนัก แต่ก็ได้ยินเธอพึมพำบ่นอะไรอยู่"

# "It's actually kinda cute."
"จริง ๆ ก็น่ารักเหมือนกัน"

# "I hurry a little to reach the door first. Opening it will be easier for me than for her."
"ฉันเร่งฝีเท้าขึ้นเล็กน้อยให้มาถึงที่ประตูก่อนเพราะฉันเปิดประตูได้ง่ายกว่าเอมิอยู่แล้ว"

play sound sfx_door_creak

show emiwheel neutral:
    center
    xpos 0.4
    easein 0.5 xpos 0.5
with charaenter


# "The door opens, and Emi starts to wheel inside, only to come to a sudden halt at the doorway."
"เมื่อประตูเปิดแล้วเอมิก็เลื่อนล้อหมายจะเข้าไปข้างใน แต่ก็ชะงักกึกอยู่ที่ประตู"

# "It seems the doorsill is slightly too high for her to get over by herself."
"เหมือนว่าธรณีประตูจะสูงเกินกว่าจะเลื่อนข้ามไปเองได้"

show emiwheel awayfrown:
with charachange

show emiwheel awayfrown:
    center
    ease 0.4 xpos 0.45
    easeout 0.2 xpos 0.5
    ease 0.4 xpos 0.45
    easeout 0.2 xpos 0.5
    ease 0.4 xpos 0.45
    easeout 0.2 xpos 0.5
    ease 0.4 xpos 0.45
    ease 0.2 xpos 0.5
with Pause(1.0)

# "She makes a few runs at it, unsuccessfully, before crossing her eyes and glaring at the offending object."
"เอมิลองเลื่อนล้ออยู่สองสามรอบแต่ก็ไม่สำเร็จก่อนจะเพ่งตาจ้องไปที่สิ่งที่ทำให้เธอต้องลำบากอยู่ตอนนี้"

show emiwheel angry at center
with charaenter

# emi "Stupid wheelchair."
emi "เจ้าวีลแชร์โง่"

show emiwheel frown
with charachange

# emi "Hisao, can you give me a hand here?"
emi "ฮิซาโอะ มาช่วยหน่อยได้มั้ย"

# hi "Sure, no problem."
hi "อ้อ ได้สิ"

scene bg school_sportsstoreroom
with locationchange

# "It's a simple enough matter for me to bump Emi over the doorway, jostling her slightly."
"แค่เข็นให้ผ่านประตูไปน่าจะไม่ยากอะไรสำหรับฉัน ฉันดันวีลแชร์ไปเล็กน้อย"

show emiwheel blush_close_ni at center
with charaenter

# emi "Hey, easy there!"
emi "นี่ เบา ๆ หน่อย!"

# hi "Whoops! Sorry."
hi "โอ๊ะ! ขอโทษที"

# "It's at about this time that I fail to notice where I'm going and run Emi's chair into a mat."
"ซึ่งก็เป็นตอนนี้เองที่ฉันไม่เห็นว่าตัวเองเข็นวีลแชร์เอมิให้เข้าไปหาแผ่นยางปูพื้น"

play sound sfx_impact

show expression im.Composite((425,1200), (0,0), night("sprites/emiwheel/close/emiwheel_blush_close.png")) as emiwheel:
   xalign 0.5 yanchor 0.5 ypos 1.0 subpixel True
   easeout 0.5 ypos 1.4 rotate 70

with vpunch

hide emiwheel
with None

# "She gives a startled yelp and topples forward out of her chair."
"เอมิร้องว้ายด้วยความตกใจก่อนจะล้มหน้าคว่ำตกจากวีลแชร์ไป"

# "There's a moment of silence as I gaze in horror upon what I've done, and Emi glares at me."
"ฉันยืนหน้าซีดมองสิ่งที่ตัวเองได้ทำลงไปอยู่เงียบ ๆ ครู่หนึ่ง เอมิจ้องมาทางฉัน"

# emi "Hisao…"
emi "ฮิซาโอะ…"

# hi "Yes?"
hi "ครับ?"

# emi "Promise me you'll never work at a hospital."
emi "สัญญากับฉันนะว่าอนาคตนายจะไม่ไปทำงานอะไรที่โรงพยาบาล"

# hi "Sorry! I didn't mean to!"
hi "ขอโทษ! ฉันไม่ได้ตั้งใจ!"

# "Emi giggles, and holds up a hand."
"เอมิหัวเราะคิกคักแล้วยื่นมือมา"

# emi "Would you kindly help me back into my chair, Hisao?"
emi "ช่วยอุ้มฉันกลับขึ้นไปนั่งที่วีลแชร์ทีสิฮิซาโอะ"

show emi basic_closedgrin_close_ni:
    center
    ypos 1.2
    easein 0.5 ypos 1.0
with charaenter

# "As I bend down to pick up Emi, she grins in triumph and pulls me into a kiss that quickly has us both entirely unconcerned about getting her back into the chair."
"ตอนที่ก้มลงไปอุ้มเอมิขึ้นมาเธอก็ยิ้มกระหยิ่มแล้วรั้งหน้าฉันเข้าไปจูบจนทำให้เราสองคนต่างลืมเรื่องวีลแชร์\nกันไปทันที"

play sound sfx_door_creak

# "In fact, as I move to a more comfortable position, I confess that the chair is pushed out the door, which, startled by the passage, swings shut."
"ที่จริงต้องสารภาพอีกอย่างว่าตอนที่ฉันปรับท่าให้สบายตัวขึ้นวีลแชร์ก็โดนดันจนไหลออกประตูไป ซึ่งแรงกระแทก\nจากวีลแชร์ก็ทำให้ประตูเหวี่ยงปิดเข้ามา"

play sound sfx_rustling

hide emi
show eminude smile_close_ni at center
with charachange

# "Well, at least we've got privacy now, which is a good thing as my hands work quickly to remove Emi's blouse and skirt."
"เอาเถอะ อย่างน้อยตอนนี้ก็ไม่มีใครเห็นเราแล้ว ซึ่งก็ดีเพราะฉันกำลังรีบถอดเสื้อกับกางเกงเอมิอยู่"

# "I'm startled to discover that she's forgotten to put her bra on today. Did she plan this?"
"ฉันตกใจเมื่อเห็นว่าวันนี้เอมิไม่ได้ใส่เสื้อชั้นในมา นี่วางแผนไว้แล้วเหรอเนี่ย"

show eminude blush_close_ni
with charachange

# "Her arms hook under mine and rest on my shoulders as I kiss my way down Emi's neck, pausing to give special attention to a spot right where the neck meets the shoulder that I'd found last night."
"เอมิสอดแขนเข้ามาใต้รักแร้ฉันแล้วเกาะไหล่ไว้ ฉันจูบไล้ไปตามลำคอเอมิก่อนจะหยุดมาเล้าโลมอยู่ตรงต้นคอ\nซึ่งเป็นจุดที่ฉันได้รู้มาเมื่อวาน"

# emi "Y-you've gotten pretty good at th-hee!"
emi "นะ นายเริ่มเก่งแล้วนะ นี่!"

# hi "I do try."
hi "ฉันก็หัดบ้างอะไรบ้าง"

show eminude frown_close_ni
with charachange

# "Emi pushes on my chest, insistently, and I draw back with a puzzled expression."
"เอมิฝืนดันหน้าอกฉันจนฉันต้องผละตัวออกมาด้วยสีหน้างุนงง"

# emi "I've got a confession, Hisao."
emi "ฉันมีเรื่องจะสารภาพกับนาย ฮิซาโอะ"

# hi "Oh?"
hi "ว่า"

# "Having pulled back, I decide instead to focus my attention on her breasts."
"พอผละตัวออกมาแล้วฉันจึงเลือกจะหันไปให้ความสนใจที่หน้าอกเอมิต่อ"

show eminude blush_close_ni
with vpunch

# "As she attempts to speak, her words are interspersed with giggles that I find incredibly cute."
"เสียงหัวเราะคิกคักเข้ามาแทรกตอนที่เอมิจะพูดอยู่เป็นช่วง ๆ น่ารักดีแฮะ"

show eminude wink_close_ni
with charachange

# emi "I don't ac-hee hee hee-actually w-woah! Wear gloves."
emi "จริง ๆ แล้วฉัน มะ ฮิ ๆ ๆ ไม่ได้จะใส่ อะ โอ๊ย! ถุงมือหรอก"

# "My own reply is rather mumbled onto her chest instead of being addressed to her face."
"ฉันตอบพึมพำอยู่กับหน้าอกเธอแทนที่จะมองหน้าตรง ๆ"

# hi "Should've known…"
hi "น่าจะคิดได้แต่แรก…"

# "Words quickly become irrelevant."
"คำพูดใด ๆ เริ่มหมดความหมาย"

show eminude closedsmile_close_ni
with vpunch

# "Emi's movements are almost frantic, as if she's been holding something back since we met this morning, and now she has an outlet."
"เอมิดีดดิ้นรุนแรงราวกับว่าได้จังหวะปลดปล่อยหลังจากที่อัดอั้นมาตั้งแต่ได้เจอกันเมื่อเช้านี้แล้ว"

# "I'm very nearly caught off guard by her aggressiveness, feeling her nearly rip my shirt off, the way she seems to vie to be in the dominant position."
"ฉันแทบไม่ทันตั้งตัวกับความรุกหนักของเอมิเมื่อเธอแทบจะทึ้งเสื้อฉันทิ้งคอยแย่งตำแหน่งคุมเกม"

# "For my part, I confess that I'm caught up in her attitude as well, fighting back, rolling and wrestling even as I caress her breasts, even as her fingers dig into my shoulders, and I lose track of where we are."
"ส่วนฉันก็ต้องยอมรับว่าตัวเองก็ไปรับคำท้าของเอมิแล้วสู้กลับเหมือนกัน ฉันพลิกตัวปลุกปล้ำอยู่กับเธอไปพลาง\nจับหน้าอก เอมิจิกนิ้วเข้าที่ไหล่ฉัน จนสุดท้ายฉันไม่ได้ดูแล้วว่าตอนนี้เราอยู่ตรงไหนกัน"

show eminude blush_ni
with vpunch

# "So much so that I roll right off the mat and land on something small and rather hard."
"ไม่ได้ดูให้ดีจนฉันกลิ้งตกใส่แผ่นยางปูพื้นแล้วทับใส่อะไรสักอย่างเล็ก ๆ แข็ง ๆ"

# hi "Ow!"
hi "โอ๊ย!"

show eminude weaksmile_ni
with charachange

# "Emi, still flushed and breathing a little heavily, peers at me and bursts into laughter."
"เอมิที่ยังหน้าแดงหอบ ๆ อยู่มองมาทางฉันแล้วหัวเราะร่วน"

# emi "I'm sorry, I'm sorry. Are you all right?"
emi "ขอโทษ ๆ นายเป็นอะไรหรือเปล่า"

# hi "Yeah, I think so. Not sure what I landed on, though…"
hi "ไม่น่าเป็นนะ แต่ไม่รู้ว่ามาทับใส่อะไรนี่สิ…"

# "I reach under my back and pull the offending object out, inspecting it closely."
"ฉันเอื้อมมือไปไพล่หลังแล้วหยิบของสิ่งนั้นมาดูใกล้ ๆ"

stop music fadeout 0.2

# "“Personal lubricant. Lemon-flavored.”"
"“เจลหล่อลื่น กลิ่นเลมอน”"

# "Wait, what?"
"เดี๋ยว อะไรนะ"

play music music_running

show eminude happy_ni
with charachange

# "Emi's eyes shoot upwards and she begins, if possible, to laugh even harder."
"เอมิเงยหน้ามองแล้วเหมือนจะหัวเราะเสียงดังกว่าเก่า"

# hi "Somehow, I don't think this is… this isn't track-related."
hi "ไม่รู้ทำไม แต่ฉันว่าไอ้นี่มัน… ไม่น่าใช่อุปกรณ์กีฬานะ"

show eminude closedsmile_ni
with charachange

# emi "Oh man, I know whose that is!"
emi "อ๋อ ฉันรู้แหละว่าของใคร!"

# hi "What?"
hi "อะไรนะ"

show eminude wink_ni
with charachange

# emi "It's the track captain's!"
emi "ของหัวหน้าทีม"

# "Ah, my old nemesis. Or, kind of."
"อ้อ โจทก์เก่าฉันนี่เอง หรือไม่ก็ใกล้เคียง"

# hi "How d'you know it's his?"
hi "แล้วรู้ได้ไงว่าของเขา"

show eminude awayfrown_ni
with charachange

# "It appears that I've asked a stupid question, or at least Emi thinks so."
"เหมือนฉันจะถามอะไรโง่ ๆ ออกไป เพราะเอมิทำท่าว่าคิดแบบนั้น"

show eminude frown_ni
with charachange

# emi "Because he's the one who told me the track shed was a good place for… what did he call them?"
emi "เพราะหัวหน้าทีมบอกฉันว่าห้องเก็บของของสนามน่ะเหมาะกับการ… เขาใช้คำว่าอะไรนะ"

show eminude pout_ni
with charachange

# emi "“Clandestine encounters.”"
emi "“แอบนัดกัน”"

# hi "Oh? He invite you to one or something?"
hi "หืม นี่เขาเคยนัดเธอหรือยังไง"

show eminude happy_ni
with charachange

# "Emi bursts into more laughter."
"เอมิหัวเราะหนักกว่าเดิม"

# "I confess the sight of a naked Emi laughing is oddly beautiful."
"ยอมรับเลยว่าเอมิตอนเปลือยที่หัวเราะอยู่นั้นช่างสวยงามพิลึก"

# "I feel an eagerness to end conversation and get back to what we were doing, despite my rather pointed questioning."
"ฉันอยากตัดบทสนทนานี้ทิ้งแล้วกลับไปต่อที่ค้างไว้กันเมื่อครู่ ทั้งที่ตัวเองก็เป็นคนถามเหมือนหาเรื่องไปแบบนั้น"

show eminude closedsmile_ni
with charachange

# emi "Hisao, the track captain's gay."
emi "ฮิซาโอะ หัวหน้าทีมเขาเป็นเกย์"

# "Huh."
"อ้าว"

# hi "Really? And here I initially thought you two were a couple."
hi "จริงเหรอ ฉันก็หลงนึกว่าพวกเธอสองคนเป็นแฟนกันตั้งนาน"

show eminude awayfrown_ni
with charachange

# emi "Well… I did have a crush on him when I first joined up, but he wasn't interested."
emi "ก็… ตอนฉันเข้าทีมมาแรก ๆ ก็ชอบเขาอยู่แหละ แต่เขาไม่ได้สนใจฉัน"

show eminude frown_ni
with charachange

# emi "Obviously."
emi "ซึ่งก็แหงอยู่แล้ว"

show eminude neutral_ni
with charachange

# emi "But we are good friends, I guess."
emi "แต่เราก็เป็นเพื่อนที่ดีต่อกันแหละ"

show eminude grin_ni
with charachange

# emi "I mean he told me about all this, you know."
emi "ก็เนี่ย เขายังอุตส่าห์เล่าเรื่องพวกนี้ให้ฉันฟังด้วย"

# hi "I hesitate to ask,"
hi "ไม่รู้จะถามดีมั้ย"

# "And really, I do. But I ask anyway."
"ไม่รู้เลยจริง ๆ แต่ฉันก็ถามอยู่ดี"

# hi "But what does he need the uh… lube for, anyway?"
hi "แต่หัวหน้าทีมเขาจะ เอ่อ… เอาเจลหล่อลื่นไปใช้ทำอะไร"

# hi "I mean, he doesn't… er…"
hi "คือ เขาคงไม่ได้… เอ้อ…"

# "How the hell does Emi always manage to not blush?"
"นี่เอมิไม่หน้าแดงได้ไงเนี่ย"

show eminude wink_ni
with charachange

# emi "Obviously he uses it for, you know."
emi "ก็แน่อยู่แล้วสิว่าต้องเอาไปใช้ นั่นแหละ"

show eminude evil_ni
with charachange

# emi "Anal."
emi "เข้าประตูหลัง"

# "I try to suppress a snicker."
"ฉันพยายามจะกลั้นขำ"

# "I fail."
"แต่ก็ไม่สำเร็จ"

show eminude happy_ni
with charachange

# "Emi's giggling too."
"เอมิก็หัวเราะคิกคักตาม"

# hi "And he {b}tells{/b} you about all this?"
hi "แล้วนี่เขา{b}เล่า{/b}ทุกอย่างให้เธอฟังหมดเลยเหรอ"

show eminude awayfrown_ni
with charachange

# "Emi shrugs."
"เอมิยักไหล่"

show eminude neutral_ni
with charachange

# emi "Yeah, of course."
emi "อืม แหงสิ"

stop music fadeout 10.0

show eminude closedsmile_ni
with charachange

# emi "He's kinda wild about the whole thing."
emi "หัวหน้าทีมน่ะคลั่งไคล้กับอะไรพวกนี้มาก"

# emi "Says it's a feeling that can't be beat."
emi "บอกว่าเป็นความรู้สึกที่ดีเยี่ยมแบบไม่มีอะไรเทียบเลย"

# hi "Uh… huh."
hi "อ่า… ฮะ"

# "The air in the track shed seems charged with some kind of horrible curiosity."
"บรรยากาศในห้องเก็บของแห่งนี้อวลไปด้วยความอยากรู้อยากเห็นสุดสะพรึง"

# hi "That's interesting."
hi "น่าสนใจ"

# hi "I suppose I'll have to take his word for it."
hi "คงต้องเชื่อคำพูดหัวหน้าทีมเขาแล้วละ"

show eminude neutral_ni
with charachange

# emi "Well…"
emi "อืม…"

# "Birds outside stop chirping."
"นกที่อยู่ข้างนอกหยุดร้อง"

# "The wind dies down."
"สายลมหยุดพัด"

# "Somewhere, a man is drinking a cup of coffee. He freezes with the cup at his lips."
"มีใครสักคนบนโลกนี้ที่กำลังดื่มกาแฟอยู่ เขาคนนั้นชะงักมือที่ยกแก้วขึ้นมาจิบ"

show eminude neutral_ni
with charachange

# emi "We could…"
emi "หรือว่า…"

# extend " maybe…"
extend " เราจะ…"

show eminude blush_ni
with charachange

# emi "Try it."
emi "ลองบ้าง"

play music music_one fadein 5.0

# "My jaw suddenly and spontaneously unhinges and hits the floor."
"กรามฉันหลุดออกมาเองตกกระแทกพื้นโดยทันที"

# hi "W-what?"
hi "อะ อะไรนะ"

# "Emi is finally blushing, rubbing the back of her head ruefully."
"สุดท้ายเอมิก็หน้าแดงขึ้นมาพลางเกาท้ายทอยแก้เก้อ"

show eminude pout_ni
with charachange

# emi "Well, it's just that we really can't… do what we did last night, you know?"
emi "คือ จะให้เราทำแบบเมื่อคืนมันก็… ไม่น่าได้ใช่มั้ยล่ะ"

# emi "It would be a little… it wouldn't be safe, you know?"
emi "มันออกจะ… ไม่ปลอดภัยน่ะนะ"

show eminude weaksmile_ni
with charachange

# emi "I mean it wasn't exactly a great idea last night."
emi "แล้วที่ทำไปเมื่อคืนมันก็ไม่ค่อยดีสักเท่าไหร่"

show eminude closedsmile_ni
with charachange

# emi "So you know, we could try this to see if it uh…"
emi "แล้วก็เนี่ย เราลองดูก็ได้ว่ามัน เอ่อ…"

# hi "Is as good?"
hi "รู้สึกดีเหมือนกันมั้ยงี้?"

show eminude weaksmile_ni
with charachange

# emi "Well uh, yeah. Basically."
emi "ก็ เอ่อ อื้ม นั่นแหละ"

# hi "Huh."
hi "อืมมม"

label th_E21h:

scene evh emi_shed_base1
show emi emi_shed_grin
show hisao emi_shed_neutral
show evh_l emi_shed_up
show evh_r emi_shed_down
with shorttimeskip

# emi "Careful!"
emi "ระวังหน่อย!"

# hi "Are you sure about this?"
hi "เธอแน่ใจแล้วใช่มั้ย"

# "I'm positioned behind Emi, who is looking back over her shoulder, looking a little flushed."
"ฉันมาอยู่ข้างหลังเอมิ เธอหันมามองข้างหลังพร้อมหน้าสีแดงเรื่อ"

# "Well obviously once we decided to go ahead with this idea, we had to get back into the mood."
"ก็นะ ในเมื่อตกลงว่าจะทำแบบนี้แล้วเราก็ต้องเรียกอารมณ์กลับมาใหม่"

# "That accomplished, we emptied the bottle of lube and…"
"พอมีอารมณ์กันแล้วเราก็บีบขวดเจลหล่อลื่นแล้วก็…"

# "Here we are."
"เอาละ"

show emi emi_shed_hesitant
with charachange

# emi "Yes, I'm sure! Come on, before I calm down and think too much about this."
emi "อื้ม แน่ใจแล้ว! เร็ว ก่อนที่ฉันจะมีสติคิดอะไรไปมากกว่านี้"

# "Emi's breathing is still coming a little heavily, and her response is almost impatient."
"เอมิยังหอบ ๆ อยู่ คำพูดของเธอดูร้อนรน"

# "Which is to be expected, I suppose. We were both so close, and this is kind of delaying things."
"ซึ่งก็คงไม่แปลกละมั้ง อีกนิดเดียวเราต่างก็จะถึงแล้วแท้ ๆ และยิ่งเป็นแบบนี้ก็ยิ่งชักช้าไปอีก"

# "I think we've both gone temporarily insane."
"ฉันว่าเราทั้งคู่เป็นคนสติหลุดไปชั่วขณะแล้ว"

# "At least that's going to be my claim from here on out."
"หรือถ้าไม่เป็นอย่างนั้นจริงฉันก็จะอ้างคำพูดนั้นกับเรื่องที่จะเกิดต่อจากนี้"

# "I try hard not to think about the specifics of what I'm about to get myself into."
"ฉันห้ามใจไม่ให้คิดมากกับเรื่องที่กำลังจะทำ"

# "There's no way this is going to be very clean."
"ยังไงก็คงสกปรกแน่ ๆ"

show evh emi_shed_base2
show hisao emi_shed_closed
with charachange

# "Taking a breath that is as much for me as it is for her, I enter slowly."
"ฉันสูดหายใจเข้าลึกพอกันกับเอมิก่อนจะดันตัวเองเข้าไปช้า ๆ"

# "There's a lot of resistance, and it's like both our bodies are reluctant to actually go through with it."
"ซึ่งใส่เข้าไปได้ยากมากราวกับว่าร่างกายเราทั้งสองคนต่างไม่เอาด้วยกับสิ่งนี้"

show emi emi_shed_shock
with hpunch

# "Emi's whole body tenses, and as I'm only partially in by this point, it feels surprisingly good, if a bit odd."
"ทั้งตัวเอมิเกร็งไปหมด ฉันเข้าไปได้บางส่วนแล้ว รู้สึกดีผิดคาด แต่ก็รู้สึกแปลกหน่อย ๆ"

# "Emi, on the other hand, looks uncomfortable."
"ทว่าเอมินั้นดูจะไม่สบายตัวเอาเสียเลย"

# "The expression is almost comical."
"สีหน้าเอมิดูตลก"

show hisao emi_shed_neutral
with charachange

# hi "Should I stop?"
hi "พอก่อนมั้ย"

# "Emi's breath hitches in her throat, and it seems to take a few seconds longer than it should to formulate a reply."
"เอมิครางอยู่ในลำคอ คำตอบของเธอนั้นตามมาช้ากว่าปกติสักสองสามวินาทีได้"

show emi emi_shed_closed
with charachange

# emi "N-no, keep going. It just feels weird."
emi "มะ ไม่ต้อง ทำต่อเลย แค่รู้สึกแปลก ๆ น่ะ"

# "She giggles."
"เอมิหัวเราะคิกคัก"

# "I can't blame her. I'm surprised that I even managed to form a sentence."
"ก็ว่าไม่ได้ละนะ แม้แต่ฉันเองยังแทบพูดไม่เป็นภาษาแล้ว"

show hisao emi_shed_closed
with charachange

# "It's… hot."
"ข้างใน… ร้อน"

# "Feels exceedingly odd."
"รู้สึกแปลกมาก ๆ"

# "The lube glistens unnaturally."
"เจลหล่อลื่นสะท้อนแสงวิบวับผิดธรรมชาติ"

# "It makes me uncomfortable."
"จนฉันอึดอัด"

# "I continue to work my way inside her, working slowly and listening carefully to Emi's breathing."
"ฉันเคลื่อนตัวเองเข้าไปข้างในเอมิเรื่อย ๆ คอยฟังเสียงลมหายใจของเธอ"

show evh emi_shed_base3
show emi emi_shed_hesitant
with charachange

# "I reach my limit and pause. Emi looks back again, biting her lower lip."
"พอเข้าไปจนสุดแล้วฉันก็หยุด เอมิหันมามองอีกรอบพลางเม้มริมฝีปากล่าง"

# emi "Are you going to try moving, or are we just going to sit here feeling silly?"
emi "จะขยับมั้ย หรือจะอยู่กันเฉย ๆ ให้รู้สึกแปลก ๆ แบบนี้?"

show hisao emi_shed_neutral
with charachange

# hi "No, I just wanted to give you a chance to adjust."
hi "ไม่ใช่อย่างนั้น ฉันแค่อยากให้เธอได้ชินก่อนน่ะ"

# "This doesn't make any sense."
"ไม่เห็นจะสมเหตุสมผลเลย"

# "How did we even decide to do this?"
"นี่เราตกลงว่าจะทำกันได้ยังไง"

show emi emi_shed_grin
with charachange

# emi "I don't think there's really any adjusting to this, Hisao."
emi "ฉันว่ามันไม่มีอะไรให้ชินนะฮิซาโอะ"

show emi emi_shed_hesitant
with charachange

# emi "Try moving. Maybe it'll feel better?"
emi "ลองขยับดูสิ อาจจะรู้สึกดีขึ้นก็ได้"

# "She sounds doubtful, but certainly unwilling to admit defeat now that we've come so far."
"น้ำเสียงเอมิฟังดูลังเล แต่ชัดว่าไม่อยากถอยเพราะมาขนาดนี้แล้ว"

show emi emi_shed_closed
with charachange

# "I begin a slow motion that seems to work well for both myself and Emi, as she closes her eyes in an attempt to concentrate on this new feeling."
"ฉันขยับตัวช้า ๆ ให้ตัวเองกับเอมิได้ปรับตัวให้ถนัดไปพร้อมกัน เธอหลับตาคอยจอจ่ออยู่กับความรู้สึกใหม่นี้"

# "As I begin to find a rhythm, I begin to feel that familiar falling-away sensation I got yesterday."
"พอเริ่มจับจังหวะได้ก็มีความรู้สึกล่องลอยอันคุ้นเคยที่ได้สัมผัสมาแล้วเมื่อวานแทรกเข้ามา"

show hisao emi_shed_closed
with charachange

# "I close my eyes and try to lose myself in the feeling, except…"
"ฉันหลับตาปล่อยให้ตัวเองจมจ่อมไปกับความรู้สึกนั้น แต่ว่า…"

# "It doesn't seem right."
"มีบางอย่างแปลกไป"

# "Emi's not making any noise."
"เอมิไม่ส่งเสียงเลย"

# "I learned very quickly yesterday that Emi is somewhat less than quiet when she's enjoying herself."
"เมื่อวานฉันได้รู้แล้วว่าตอนที่เอมิรู้สึกดีอยู่นั้นเธอจะค่อนข้างเงียบ"

show hisao emi_shed_neutral
with charachange

# "As I open my eyes, I see that Emi's trying to get into things, but it just doesn't seem to be working for her."
"พอลืมตามาก็เห็นเอมิที่คอยปรับตัวกับสิ่งนี้อยู่ แต่เหมือนจะไม่ได้ผลเท่าไหร่"

# "Her eyes are closed, and she's biting her lip, but it seems to be out of toleration rather than enjoyment."
"เอมิหลับตากัดริมฝีปากตัวเอง ซึ่งเหมือนไม่ได้กัดเพราะรู้สึกดี แต่กัดเพราะฝืนทนอยู่มากกว่า"

# "A sort of “well, this was a failure, but hopefully it'll be over soon” look."
"เป็นสีหน้าประมาณว่า “โอเค ไปได้ไม่สวยเลย แต่ขอให้มันจบไว ๆ แล้วกัน”"

# "I'm caught in a bit of a situation here."
"ตอนนี้ฉันตกที่นั่งลำบากแล้ว"

# "In truth, I don't want to stop."
"ที่จริงก็ไม่อยากหยุดเลย"

# "But at the same time, it doesn't seem to be doing much for Emi - or if it is, it's coming on far slower than I am."
"แต่ในขณะเดียวกัน เอมิเหมือนจะไม่ได้สบายตัวขึ้นเท่าไหร่ หรือถ้าเริ่มโอเคแล้วก็ยังสบายขึ้นช้ามาก"

# "I feel bad. I want Emi to enjoy this, too."
"รู้สึกผิดเลยแฮะ อยากให้เอมิได้รู้สึกดีด้วย"

show evh_r emi_shed_up
show emi emi_shed_shock
with charachange

# "I reach one arm around to tease at Emi's chest, which startles her."
"ฉันยื่นมือข้างหนึ่งไปหยอกล้อกับหน้าอกเอมิจนเธอตกใจ"

show hisao emi_shed_sweat
with charachange

# "This in turn causes her to tighten around me considerably, causing a wave of pleasure to blindside me."
"ซึ่งทำให้ภายในเอมิตอดรัดฉันแน่นขึ้น ความเสียวซ่านแผ่ไปทั่วร่างฉันอย่างไม่ทันตั้งตัว"

show evh emi_shed_base4
show hisao emi_shed_neutral
show emi emi_shed_closed
show evh_l emi_shed_down
with charachange

# "My gasp seems to amuse Emi, but her grin quickly turns to a gasp as I move my other hand casually down her front and begin to stroke gently at the soft patch of hair between her legs."
"เอมิดูชอบใจที่ฉันร้องคราง แต่ริมฝีปากที่ยิ้มอยู่ของเธอนั้นก็ปล่อยเสียงครางออกมาตามทันทีที่ฉันเลื่อนมืออีกข้าง\nลงไปที่ร่องของเธอแล้วลูบเบา ๆ ตรงผืนขนอ่อนนุ่มที่หว่างขานั้น"

# "The motion of my own hips increases as my hand's ministrations to Emi's front bring back the gasps and yelps that I'm used to."
"ฉันเร่งเอวตัวเองให้เร็วขึ้น มือฉันที่คุมส่วนล่างของเอมิอยู่ทำให้เธอทั้งหอบทั้งครางอย่างที่ฉันเคยได้ยิน"

show hisao emi_shed_sweat
with charachange

# "I concentrate only on the feelings of my hands, one now slick and sliding, the other on skin soft and responsive, goosebumps on her flesh, shivers and sweats, as her own building climax causes her to tighten, until finally I can't possibly—"
"ฉันจดจ่ออยู่กับสัมผัสที่ส่งผ่านมือมาเท่านั้น ข้างหนึ่งอยู่กับสัมผัสที่ทั้งลื่นและชื้นแฉะ อีกข้างอยู่กับสัมผัส\nจากผิวอ่อนนุ่มที่ตอบสนองกับมือฉัน ขนตามตัวเธอลุกชัน เอมิเข้าใกล้ฝั่งไปเรื่อย ๆ ทั้งตัวเธอสั่นและชุ่มไปด้วยเหงื่อ\nภายในเธอตอดแน่นจนในที่สุดฉันก็ไม่อาจ—"

# "NoIcan'tpossibly"
"ไม่ฉันไม่อาจแล้ว"

show hisao emi_shed_closed
with charachange

# "OhgodI'msorryEmiI'mgoingto"
"ตายแล้วเอมิฉันใกล้จะ"

# "I give a final thrust, my fingers tense around Emi's nipples, dive between her legs."
"ฉันกระแทกเข้าไปเป็นครั้งสุดท้ายโดยมือข้างหนึ่งใช้นิ้วบีบยอดหน้าอกเอมิ อีกข้างสอดเข้าไปที่หว่างขาเธอ"

window hide

play sound sfx_flash
with SilentWhiteout(0.1,0.0,0.1)
play sound sfx_flash
with SilentWhiteout(0.1,0.0,0.4)
with GenericWhiteout(0.5,1.0,4.0)

window show

# "Emi's back spasms and she arches up, a high, girlish cry that echoes off the walls, and I feel the wave of my own climax annihilate all other sensations in my body."
"เอมิกระตุกตัวงอ เสียงครางหวานของเธอสะท้อนก้องอยู่ในห้องเก็บของ คลื่นความรู้สึกเมื่อถึงฝั่งนั้นเข้าซัด\nทุกประสาทสัมผัสในร่างกาย"

show evh_l emi_shed_up
show evh_r emi_shed_down
with charachange

# "Emi's arms give out and she falls forward, rather violently disengaging us and pulling something dear to me in the process."
"แขนเอมิอ่อนยวบจนเธอล้มหน้าฟุบจนทำให้เราหลุดจากกันอย่างค่อนข้างกะทันหันดึงสิ่งที่ฉันโหยหาไปจากตัวฉัน"

label th_E21x:

play sound sfx_impact

scene bg school_sportsstoreroom
with vpunch

# "The sudden switch from pleasure to pain causes me to lose my balance, and I fall forward on top of Emi."
"ความเจ็บที่อยู่ ๆ ก็แล่นผ่านทั่วร่างทำให้ฉันเสียการทรงตัวแล้วล้มทับเอมิ"

stop music fadeout 2.0

# emi "Ow!"
emi "โอ๊ย!"

# hi "Ow."
hi "โอย"

# "I quickly roll off Emi and prop myself up, breathing heavily and trying to ignore the pain in my crotch."
"ฉันรีบกลิ้งตัวออกจากเอมิแล้วจัดแจงตัวเอง ฉันหอบหนักมาก ตอนนี้ต้องทำเป็นไม่สนใจเป้าตัวเองที่เจ็บ ๆ อยู่"

# "Emi yelps a little as she rolls over. She grabs a couple of the tissues we'd kept handy earlier, and cleans up before getting her panties back on and awkwardly leaning against a wall."
"เอมิร้องว้ายเบา ๆ ตอนที่กลิ้งตัวออกมา เธอหยิบทิชชูที่เราพกมากันสองสามแผ่นมาเช็ดทำความสะอาด\nก่อนจะใส่กางเกงแล้วมานั่งพิงกำแพงด้วยท่าที่ดูไม่สบายนัก"

# "Still breathing heavily, I decide to sit against the wall next to her. The feeling of the cool concrete against my sweating back is a welcome sensation."
"ส่วนฉันที่ยังเหนื่อยหอบก็มานั่งพิงกำแพงข้างเอมิบ้าง สัมผัสเย็น ๆ จากคอนกรีตที่ถูกหลังชื้นเหงื่อของฉันนั้น\nช่างสบายตัวเหลือเกิน"

show eminude sad_close_ni at center
with charaenter

# emi "That {b}hurt{/b} at the end!"
emi "มาทับกันทำไม {b}เจ็บ{/b}นะ!"

# hi "Yeah, I uh…"
hi "อ่า ฉัน เอ่อ…"

# hi "This was probably not a great idea."
hi "ที่ทำเมื่อกี้น่าจะไม่ใช่ความคิดที่ดีเท่าไหร่"

# "Emi squirms in order to try and sit down beside me without too much pain. Judging by her wincing, it doesn't really work."
"เอมิเขยิบตัวมานั่งข้างฉันโดยเลี่ยง ๆ ไม่ให้ตัวเองต้องเจ็บมาก ซึ่งเห็นหยีตาแบบนี้ก็แปลว่ายังเจ็บอยู่ดี"

show eminude pout_close_ni
with charachange

# emi "Yeah, I'm going to have words with the captain."
emi "อืม เดี๋ยวต้องไปคุยกับหัวหน้าทีมแล้ว"

show eminude angry_close_ni
with charachange

# emi "He was clearly lying."
emi "โกหกกันเห็น ๆ"

play music music_ease

# "The utter and absolute ridiculousness of the situation suddenly hits, and I begin laughing."
"อยู่ ๆ ฉันก็ระลึกถึงความบ้าบออย่างถึงที่สุดของสถานการณ์ในตอนนี้แล้วหัวเราะออกมา"

show eminude happy_close_ni
with charachange

# "Emi shakes her head and begins laughing with me."
"เอมิส่ายหน้าแล้วหัวเราะตาม"

show eminude grin_close_ni
with charachange

# emi "Hey, Hisao."
emi "นี่ ฮิซาโอะ"

# hi "Yeah?"
hi "หืม"

show eminude pout_close_ni
with charachange

# emi "We're never doing this again, right?"
emi "เราจะไม่ทำแบบนี้กันอีกแล้วใช่มั้ย"

# hi "Yeah, I think my curiosity is satisfied on this one."
hi "อืม ฉันว่าตอนนี้ฉันไม่ได้มีความอยากรู้อะไรแล้วละ"

# "Emi nods, satisfied."
"เอมิพยักหน้าพอใจ"

show eminude closedsmile_close_ni
with charachange

# emi "Good."
emi "ดี"

show eminude smile_close_ni
with charachange

# emi "I think we should maybe stick to the basics, don't you?"
emi "ฉันว่าเราทำกันไปตามปกติดีกว่าเนอะ"

show eminude blush_close_ni
with charachange

# emi "I mean most of this is new to me anyway."
emi "แค่ตามปกติที่ว่าน่ะ อะไรหลายอย่างฉันก็ยังไม่เคยเลย"

# hi "What d'you mean, “most?”"
hi "“หลายอย่าง” นี่หมายความว่าไง"

show eminude grin_close_ni
with charachange

# "Emi grins impishly."
"เอมิยิ้มซุกซน"

show eminude closedsmile_close_ni
with charachange

# emi "I'll never tell."
emi "ไม่มีวันบอกซะหรอก"

# "An unpleasant thought strikes me."
"อยู่ ๆ ฉันก็คิดอะไรไม่น่าอภิรมย์"

# "Even more unpleasant is the thought of having to ask Emi about it."
"ที่ไม่น่าอภิรมย์ยิ่งกว่าคือฉันต้องถามเอมิ"

# "Still, after what we've just done, it should be a cakewalk."
"แต่ก็นะ ถ้าผ่านเรื่องเมื่อกี้มาได้แล้วก็น่าจะถามได้ไม่ยาก"

# hi "Hey, is there a sink?"
hi "นี่ แถวนี้มีอ่างล้างมือมั้ย"

# hi "I'd kinda like to, er."
hi "พอดีฉันจะ เอ่อ"

# hi "Wash off a little."
hi "ล้างเลิ้งอะไรสักหน่อย"

show eminude blush_close_ni
with charachange

# "Emi's jaw drops."
"เอมิอ้าปากหวอ"

# emi "In the {b}sink{/b}?"
emi "ล้างใน {b}อ่างล้างมือ{/b} เนี่ยนะ"

# hi "Well, there's not really anywhere else to do it, is there?"
hi "ก็แล้วจะให้ไปล้างที่ไหนเล่า"

# hi "And it uh… I want to avoid a smell."
hi "แถม เอ่อ… ฉันไม่อยากให้มีกลิ่น"

# hi "That the nurse might notice."
hi "เดี๋ยวคุณพยาบาลรู้"

# "This is the most awkward conversation I have ever had."
"ช่างเป็นบทสนทนาที่กระอักกระอ่วนที่สุดในชีวิต"

show eminude closedsmile_close_ni
with charachange

# emi "You're right."
emi "ก็จริงของนาย"

show eminude grin_close_ni
with charachange

# emi "Yeah, there's uh… It's on the back wall."
emi "อืม ก็มี… อยู่ตรงหลังห้องเก็บของนี่แหละ"

show eminude smile_close_ni
with charachange

# emi "There might be some soap, too."
emi "เหมือนจะมีสบู่ด้วย"

# hi "Thanks."
hi "ขอบใจ"

hide eminude
with charaexit

# "There is in fact a little hand soap, which is better than nothing."
"แล้วก็มีสบู่ล้างมือก้อนเล็ก ๆ อยู่จริง ๆ ซึ่งก็ดีกว่าไม่มีอะไรเลยละนะ"

# "No towel, though. Guess I'll just have to drip dry."
"แต่ไม่มีผ้าขนหนู ปล่อยให้แห้งเองแล้วกัน"

show eminude grin_ni at center
with charaenter

# emi "All finished?"
emi "เรียบร้อยแล้วนะ"

# hi "Yeah, that'll do for now. It's not like I'm not going to take a shower after we see the nurse."
hi "อื้ม น่าจะพอใช้ได้แล้ว เดี๋ยวยังไงไปหาคุณพยาบาลกันแล้วฉันก็ต้องไปอาบน้ำอยู่ดี"

show eminude weaksmile_ni
with charachange

# emi "Glad to hear it."
emi "ค่อยโล่งหน่อย"

show eminude wink_ni
with charachange

# emi "Now help me find my clothes. You tossed 'em somewhere."
emi "แล้วก็มาช่วยฉันหาเสื้อผ้าหน่อย นายโยนทิ้งไปไหนไม่รู้เนี่ย"

# hi "Hey, you were no better! How am I supposed to explain that hole in my shirt, hmm?"
hi "เฮ้ย เธอก็ไม่ต่างกันหรอก! ถ้าคนมาเห็นรูที่เสื้อฉันแล้วจะให้ฉันว่ายังไง หืม"

show eminude closedsmile_ni
with charachange

# emi "Heh, sorry. I got a little excited earlier."
emi "ฮะ ๆ ขอโทษที พอดีเมื่อกี้ตื่นเต้นไปหน่อย"

scene bg school_sportsstoreroom
with shorttimeskip

# "It takes some time, but finally we're both more or less clothed."
"ผ่านไปสักพักเราก็ใส่เสื้อผ้ากันครบได้สำเร็จ"

# "There's a frantic moment where neither of us knows where Emi's wheelchair is, but I recall it going through the door and rescue it."
"เราวุ่นวายกันอยู่พักหนึ่งเพราะต่างไม่มีใครรู้ว่าวีลแชร์อยู่ไหน แต่พอจำได้ว่าไหลออกประตูไปฉันก็ไปเก็บมา"

show emiwheel neutral_close_ni at center
with charaenter

# emi "Now be more careful going through the door this time, would you?"
emi "ทีนี้จะเข็นฉันออกประตูก็ระวังหน่อยแล้วกัน"

show emiwheel awayfrown_close_ni
with charachange

# emi "Bumps are not my friend right now."
emi "ช่วงนี้ฉันไม่ถูกกับทางต่างระดับ"

# hi "I am so sorry we tried this."
hi "ขอโทษจริง ๆ นะที่ให้มาลองทำอะไรแบบนี้น่ะ"

show emiwheel grin_close_ni
with charachange

# "Emi shrugs and grins."
"เอมิยักไหล่แล้วยิ้ม"

show emiwheel wink_close_ni
with charachange

# emi "Well, it was worth a shot, right?"
emi "ก็ อย่างน้อยได้ลองก็ดีแล้วนี่ จริงมั้ย"

show emiwheel closedsmile_close_ni
with charachange

# emi "And anyway, it was good exercise, right?"
emi "แถมยังไงก็เป็นการออกกำลังกายที่ดีด้วย ใช่มั้ย"

# "Can't argue that."
"ก็เถียงไม่ลง"

scene bg school_nursehall
with shorttimeskip

# "As we make our way up to the nurse's office, I notice that Emi keeps shifting uncomfortably in her seat."
"ระหว่างที่มาที่ห้องพยาบาลฉันก็เห็นว่าเอมินั่งยุกยิกไปมาตลอดทาง"

show emiwheel awayfrown
with charachange

# emi "God, this feels weird."
emi "ให้ตาย รู้สึกแปลกชะมัด"

show emiwheel neutral
with charachange

# emi "Good thing I'm in a wheelchair, Hisao."
emi "ดีนะเนี่ยที่ฉันนั่งวีลแชร์น่ะฮิซาโอะ"

# hi "Why's that?"
hi "ทำไมเหรอ"

show emiwheel weaksmile
with charachange

# emi "Because, now I don't have to explain to the nurse why I'm walking funny."
emi "ก็เพราะฉันจะได้ไม่ต้องแก้ต่างกับคุณพยาบาลไงว่าทำไมท่าเดินฉันถึงแปลก ๆ"

# hi "Oh."
hi "อ้อ"

# hi "We're never doing this again."
hi "เราจะไม่ทำแบบนี้กันอีกแล้วนะ"

scene bg school_nurseoffice
show nurse fabulous at center
with locationchange

# "The nurse is at least kind enough to not comment on the marks that Emi left on my shoulders."
"อย่างน้อยคุณพยาบาลก็มีน้ำใจพอที่จะไม่พูดถึงรอยที่ฉันทำไว้ตรงไหล่เอมิ"

# "Nor does he say a word about Emi's constant shifting about in her wheelchair."
"แล้วก็ไม่ได้พูดถึงเรื่องที่เอมิขยับตัวอยู่ตลอดตอนนั่งวีลแชร์"

# "Either he didn't notice, or he didn't want to notice."
"อาจจะไม่ทันสังเกต หรือไม่อยากสังเกต"

# "All the same, I'm going to have to make sure he didn't slip cyanide into my medication for a little while."
"แต่จะอย่างไหนฉันก็ต้องดูให้แน่ใจไปสักระยะหนึ่งว่าคุณพยาบาลจะไม่แอบใส่ไซยาไนด์ในชุดยาที่ฉันต้องกิน"

# "Just to be safe."
"ปลอดภัยไว้ก่อน"

stop music fadeout 4.0
scene bg school_dormhisao
with locationskip

# "I shower for longer than usual, just to be sure I'm clean of our little “experiment”, and then collapse on my bed."
"ฉันอาบน้ำนานกว่าปกติให้แน่ใจว่าฉันล้าง “การทดลอง” เล็ก ๆ น้อย ๆ ของสองเราให้สะอาดหมดจดแล้ว จากนั้น\nจึงกลับมานอนที่เตียง"

# "Class is in twenty minutes, so I can probably afford a nap."
"อีกยี่สิบนาทีจะเข้าเรียน อาจจะยังพองีบได้อยู่"

scene black
with shuteye

#***************************************


label th_E22:

scene black
with dissolve

with Pause(5.0)

play sound sfx_doorknock

# "Knock knock."
"ก๊อก ก๊อก"

# "Who's there?"
"ใครเอ่ย"

play sound sfx_doorknock

# "Knock knock."
"ก๊อก ก๊อก"

# "That's not how the joke goes at all."
"ปกติต้องบอกว่าเป็นใครสิ"

play sound sfx_doorknock

# "Knock knock."
"ก๊อก ก๊อก"

# "I already said who's there!"
"ก็ถามไปแล้วไงว่าใครเอ่ย!"

# "More importantly, what time is it?"
"แล้วที่สำคัญ ตอนนี้กี่โมงแล้ว"

# "Even more importantly, what day…?"
"แล้วที่สำคัญกว่านั้น วันนี้วันอะไร…"

scene bg school_dormhisao
with openeyefast

# "I am suddenly catapulted into wakefulness by both the fact that the knocking still hasn't stopped and the fact that it's noon."
"ฉันสะดุ้งโหยงตื่นขึ้นมาเพราะเสียงเคาะประตูยังไม่เงียบไป และเพราะตอนนี้เที่ยงแล้ว"

# "On a school day."
"เที่ยงวันที่มีเรียน"

# "Now fully awake, I can remember why I was napping."
"พอตื่นเต็มตาแล้วถึงนึกออกว่าทำไมถึงมางีบ"

# "Better not give that excuse to Mutou."
"อย่าไปบอกเรื่องนั้นกับครูเลยดีกว่า"

# "“Sorry I wasn't in class, I was experimenting sexually with my girlfriend and it tired me out.”"
"“ขอโทษที่ขาดเรียนครับ พอดีผมไปทดลองเรื่องทางเพศกับแฟนสาวจนเพลีย”"

# "Yeah, that'll go over well."
"อืม ไปได้ไม่สวยแน่นอน"

play sound sfx_doorknock

# "I wonder how long this knocking is going to continue."
"จะเคาะประตูอีกนานมั้ย"

# "Guess I ought to answer the door."
"คงต้องไปเปิดรับแล้วแหละ"

play sound sfx_dooropen

scene bg school_dormhallway
show kenji tsun at center
with locationchange

# "I'm strangely unsurprised to see Kenji on the other side."
"ซึ่งก็ประหลาดที่ฉันไม่แปลกใจเลยเมื่อเห็นเคนจิอยู่ตรงหน้า"

# "Though it appears that Kenji is surprised to see me."
"แต่เหมือนว่าเคนจิจะแปลกใจที่ได้เจอฉัน"

# ke "What the hell are you doing here, man?"
ke "มาทำอะไรที่นี่เนี่ย"

play music music_kenji fadein 0.5

# hi "Well, I was sleeping."
hi "ก็หลับอยู่"

show kenji neutral
with charachange

# "Kenji nods in understanding."
"เคนจิพยักหน้าเหมือนเข้าใจ"

show kenji happy
with charachange

# ke "Knocked out. I see."
ke "สลบเหมือดเลยสินะ"

show kenji tsun
with charachange

# ke "I told you to be careful around that Ibarazaki chick, man."
ke "ฉันบอกแล้วไงว่าอยู่กับยัยอิบาราซากิอะไรนั่นก็ให้ระวังหน่อย"

# ke "This is the sort of thing that happens when you aren't cautious."
ke "ถ้าไม่ระวังตัวให้ดีแล้วละก็จะเป็นแบบนี้แหละ"

# "He makes an attempt to look at the back of my head."
"เคนจิชะเง้อชะแง้จะมองท้ายทอยฉัน"

show kenji neutral
with charachange

# ke "Did she hit you with something?"
ke "นี่ยัยนั่นเอาอะไรทุบนายหรือเปล่า"

# ke "Or was it a drug?"
ke "หรือว่าโดนวางยา"

# hi "Stop trying to touch me."
hi "อย่ามาแตะตัวฉันน่า"

with flash

# "Kenji produces a flashlight and shines it in my eyes."
"เคนจิควักไฟฉายออกมาส่องตาฉัน"

# ke "You got a concussion?"
ke "สมองนายกระทบกระเทือนหรือเปล่า"

# hi "I wasn't knocked out!"
hi "ไม่ได้สลบเว้ย!"

show kenji happy
with charachange

# ke "Maybe you just don't remember."
ke "นายอาจจะลืมเฉย ๆ"

# "This conversation isn't going anywhere."
"ไม่ได้เรื่องแน่อีแบบนี้"

# hi "No, I just had a tiring morning and fell asleep."
hi "เปล่า แค่เช้านี้เพลีย ๆ เลยหลับไปน่ะ"

show kenji tsun
with charachange

# ke "Whatever, man."
ke "ช่างนายเถอะ"

# ke "If you want to be in denial about this, I guess I can't stop you."
ke "ถ้านายไม่อยากยอมรับฉันก็คงห้ามอะไรไม่ได้"

# ke "But you gotta watch out for that girl, man. She's not safe."
ke "แต่ก็ระวังยัยนั่นไว้ด้วยนะ อันตรายเชียวละ"

# hi "What?"
hi "ฮะ?"

show kenji rage
with charachange

# ke "She's not safe to be around; she's one of their most sinister agents!"
ke "เป็นคนที่อยู่ด้วยแล้วอันตราย เป็นตัวแทนสุดชั่วร้ายระดับบน ๆ เลยละ!"

# ke "If you're not careful, there's no telling what could happen!"
ke "ถ้านายไม่ระวังตัวละก็อาจจะเกิดอะไรขึ้นก็ได้!"

# ke "She's brought down stronger men than you, you know!"
ke "ยัยนั่นเคยล้มคนที่แข็งแกร่งกว่านายมาแล้วด้วยนะเว้ย!"

# hi "What the hell are you talking about?"
hi "พูดอะไรของนายเนี่ย"

# hi "She's not an agent of anything, and she didn't knock me out, okay?"
hi "เอมิไม่ใช่ตัวแทนอะไรหรอก แล้วก็ไม่ได้ทุบให้ฉันสลบด้วย โอเคนะ"

# hi "I also highly doubt that she's brought down anyone at all."
hi "แล้วก็ไม่ค่อยเชื่อด้วยว่าเอมิจะไปล้มใครได้"

show kenji tsun
with charachange

# "Kenji looks almost offended."
"เคนจิทำหน้าเหมือนไม่พอใจ"

# "I have no idea why."
"ไม่รู้ทำไม"

# ke "You don't believe me?"
ke "ไม่เชื่อฉันงั้นเหรอ"

# ke "That's cold, man. Real cold."
ke "เย็นชานะนายเนี่ย เย็นชาโคตร ๆ"

# ke "I'm just trying to look out for you. That's what friends do, you know."
ke "ฉันแค่จะเตือนนายในฐานะเพื่อน"

# "We're friends? I had no idea."
"เราเป็นเพื่อนกันเหรอวะ ไม่ยักรู้"

# "Then again, I wonder if Kenji knows what being a friend even entails."
"แต่ก็นะ คนอย่างเคนจิคงไม่รู้มั้งว่าคำว่าเพื่อนมีความหมายว่าอะไรบ้าง"

# "I feel something like pity for him, standing there before me."
"เหมือนจะสงสารเจ้าคนที่ยืนอยู่ตรงหน้าฉันตอนนี้เลย"

# "Maybe he does think he's looking out for me."
"อาจจะคิดว่าตัวเองกำลังเตือนฉันอยู่จริง ๆ ก็ได้"

# hi "I know, I know."
hi "รู้แล้ว ๆ"

# hi "I'm sorry about that. Thanks for the warning."
hi "ขอโทษทีนะ ขอบใจที่เตือน"

# "I hold out my hand as a sign of peace."
"ฉันยื่นมือออกไปหวังคืนดี"

show kenji neutral_close
with characlose

# "Kenji shakes it gingerly, like my hand could possibly be on fire."
"เคนจิจับมือแล้วโยกเบา ๆ เหมือนมือฉันติดไฟอยู่"

# "There's an awkward silence for a few seconds before Kenji remembers that he's still shaking my hand."
"เราเงียบกันไปสองสามวินาทีอย่างกระอักกระอ่วนจนเคนจิรู้ตัวว่ายังโยกมือฉันอยู่"

show kenji happy_close
with charachange

# ke "Anyway, I need a favor."
ke "แต่เอาเถอะ ฉันมีเรื่องจะมารบกวนนาย"

# hi "What kind of favor? I'm out of money…"
hi "รบกวนอะไร ตอนนี้ฉันไม่มีเงินแล้วนะ…"

# ke "No you aren't. You've got money kept in your desk drawer under a black notebook. For emergencies."
ke "มี นายมี ที่ลิ้นชักโต๊ะนายจะมีสมุดสีดำที่ทับเงินไว้อยู่ เป็นเงินฉุกเฉิน"

# hi "Did you ransack my room?"
hi "นี่มาค้นห้องกันเหรอ"

show kenji neutral_close
with charachange

# ke "That's not important."
ke "ไม่ใช่ประเด็น"

# ke "I don't need money, anyway."
ke "แล้วฉันก็ไม่ได้ต้องการเงินด้วย"

# "He adopts a very serious tone."
"เคนจิทำน้ำเสียงจริงจังมาก ๆ ขึ้นมา"

show kenji tsun_close
with charachange

# ke "I'm about to undertake a major op."
ke "ฉันกำลังจะไปปฏิบัติการครั้งใหญ่"

# ke "It'll blow the whole conspiracy wide open if I'm right."
ke "ถ้าฉันคิดถูกแล้วละก็ทฤษฎีสมคบคิดทั้งหมดเหล่านี้จะถูกเปิดโปง"

# ke "But it's dangerous, so I need you to do something for me in case I don't come back."
ke "แต่เป็นงานที่อันตรายมาก ฉันเลยจะรบกวนนายอะไรอย่างเผื่อฉันไม่กลับมาอีก"

# hi "Uh, sure man. Anything."
hi "อ่า เอาเลย ได้หมด"

# "What the hell is he planning on doing?"
"นี่เคนจิคิดจะทำอะไรวะเนี่ย"

# "Should I be telling someone about this?"
"ต้องเอาไปแจ้งใครหรือเปล่า"

show kenji neutral_close
with charachange

# ke "If I go missing, wait three days and then mail my journal off to the newspapers."
ke "ถ้าฉันหายตัวไป ให้รอสามวันแล้วส่งบันทึกของฉันไปให้สำนักข่าวหนังสือพิมพ์"

# ke "It's hidden in my room under a false bottom in one of my desk drawers."
ke "หนังสือเล่มนั้นซ่อนอยู่ที่ใต้กองสองชั้นในลิ้นชักโต๊ะตัวหนึ่ง"

# hi "How do I get into your room? I don't have a key."
hi "แล้วฉันจะเข้าห้องนายได้ไง ฉันไม่มีกุญแจนะ"

show kenji tsun_close
with charachange

# "Kenji looks at me like I'm crazy."
"เคนจิมองเหมือนฉันเป็นคนบ้า"

# ke "So pick the lock. You know how to do that, right?"
ke "ก็สะเดาะเอาสิ นายทำเป็นใช่มั้ยล่ะ"

# ke "It's an important skill to learn at a young age!"
ke "เป็นทักษะที่ต้องมีติดตัวไว้แต่เด็กเลยนะ!"

# hi "Uh, yeah, of course I know how."
hi "อ่า อื้ม ทำเป็นอยู่แล้ว"

# hi "I'll be sure to uh, do that for you. If you go missing."
hi "เดี๋ยวฉันจะ เอ่อ ทำตามที่นายขอนะ ถ้านายหายตัวไป"

# "I don't think I want to read Kenji's journal."
"ฉันว่าฉันคงไม่อยากอ่านบันทึกของเคนจิแน่ ๆ"

# "Either way, Kenji seems pretty happy that I've agreed to do this thing for him."
"แต่ช่างเถอะ เคนจิดูจะมีความสุขทีเดียวที่ฉันตกลงยอมทำตามคำขอ"

show kenji happy_close
with charachange

# ke "Great, man. Great."
ke "ดีเลยพวก ดี"

# ke "I'll see you around, I got stuff to do."
ke "เดี๋ยวเจอกัน ฉันมีธุระ"

stop music fadeout 5.0

show kenji happy_close:
    easeout 0.5 xpos 0.7 alpha 0.0
with Pause(0.5)

hide kenji
with None

# "And he's gone, dashing down the hallway."
"แล้วเคนจิก็พุ่งตัวไปตามโถงทางเดินแล้วหายไป"

# "He made it seem so final."
"พูดเหมือนจะไม่กลับมาแล้วงั้นแหละ"

# "I hope I don't have to carry out his final wishes."
"หวังว่าจะไม่ต้องทำตามคำขอสุดท้ายของเขานะ"

scene bg school_dormhisao
with locationchange

play sound sfx_doorclose

# "Shaking my head, I close my door and walk back to my bed."
"ฉันสั่นหัวแล้วปิดประตูเดินกลับมาที่เตียง"

# "Guess I should go to class, if only to catch the last half of the day."
"ไปเข้าเรียนสักหน่อยก็ดี ต่อให้จะเหลืออีกแค่ครึ่งวันก็เถอะ"

# "But I've come this far without going to class today…"
"แต่ก็ขาดเรียนมาตั้งครึ่งวันแล้ว"

# "And I did want to read more of that Hawking book Mutou lent me…"
"แล้วก็อยากอ่านหนังสือของฮอว์กิงที่ครูให้ยืมมาด้วย…"

# "I'm sure he'll understand."
"ครูคงเข้าใจแหละ"

with shorttimeskip

play sound sfx_hammer

# "Knock knock."
"ก๊อก ก๊อก ก๊อก"

# "This time the noise jerks my attention away from my book."
"คราวนี้เสียงนี้ดึงความสนใจฉันไปจากหนังสือ"

# "An experience not unlike being woken up."
"ซึ่งเป็นความรู้สึกที่ไม่เหมือนตอนเสียงนั้นมาปลุกให้ตื่น"

# hi "Who's there?"
hi "ใครน่ะ"

# emi "Me! Aren't you glad?"
emi "ฉันเอง! ดีใจมั้ย"

play music music_emi fadein 4.0

# "The voice is muffled through the door, but unmistakably Emi's."
"แม้เสียงจะอู้อี้เพราะอยู่อีกฟากประตู แต่เป็นเสียงเอมิแน่นอน"

play sound sfx_dooropen

scene bg school_dormhallway
show emiwheel smile at center
with locationchange

# "I hop up and open the door, smiling broadly."
"ฉันลุกขึ้นมาเปิดประตูส่งยิ้มกว้าง"

# hi "Hey! Nice to see you again!"
hi "ไง! ดีใจที่ได้เจออีกครั้งนะ!"

show emiwheel grin
with charachange

# "Emi grins back, staring up at me from her wheelchair."
"เอมิที่นั่งวีลแชร์อยู่มองฉันแล้วส่งยิ้มกลับ"

show emiwheel closedsmile
with charachange

# emi "Yeah, you would have seen me earlier, but the damned elevator wasn't working."
emi "อื้ม จริง ๆ นายจะได้เจอฉันตั้งแต่ก่อนหน้านี้แล้ว แต่พอดีลิฟต์มันไม่ทำงานน่ะ"

show emiwheel pout
with charachange

# emi "Had to wait for them to fix it."
emi "ต้องรอคนมาซ่อม"

show emiwheel awayfrown
with charachange

# emi "You'd think they could keep it in better order, but nooo…"
emi "เป็นใครก็คงคิดว่าน่าจะมีคนคอยรักษาสภาพลิฟต์ไว้ แต่ที่ไหนได้…"

# "I chuckle a bit at her vexed expression and invite her in."
"ฉันแค่นหัวเราะเบา ๆ ให้สีหน้าเครียด ๆ นั้นแล้วเปิดประตูให้เอมิเข้ามา"

scene bg school_dormhisao
with locationchange

# "She wheels in easily, and with my help she hops onto my bed."
"เธอเลื่อนล้อเข้ามาได้ไม่ลำบากนัก ฉันช่วยอุ้มให้เธอขยับมาอยู่ที่เตียงฉัน"

show emi basic_closedgrin:
    center
    ypos 1.0
    easein 0.5 ypos 1.1
with charaenter

# emi "There. Much more comfortable than that stupid chair."
emi "แบบนี้สิ ค่อยนั่งสบายกว่าวีลแชร์โง่ ๆ นั่นหน่อย"

show emi basic_grin:
    ypos 1.1
with charachange

# "A sigh of contentment hangs in the air, and for a minute we both just stare at one another."
"พวกเราจ้องกันอยู่พักหนึ่งด้วยความพึงใจที่อวลในอากาศ"

# "It's at that point that I notice the circles under Emi's eyes."
"จนตอนนี้เองที่ฉันเพิ่งเห็นว่าใต้ตาเอมิคล้ำ"

# "They're not that dark, but they definitely weren't there before."
"ไม่ได้ดำขนาดนั้น แต่เป็นรอยที่ก่อนหน้านี้ไม่มีแน่นอน"

# "Before I can ask about them, Emi fixes me with a mischievous stare."
"แต่ก่อนที่ฉันจะทันได้ถามเอมิก็จ้องมาทางฉันอย่างเจ้าเล่ห์"

show emi excited_happy
with charachange

# emi "So, I couldn't help but notice you weren't at lunch today."
emi "พอดีวันนี้ไม่เห็นนายไปกินข้าวเที่ยงด้วยน่ะ"

# emi "In fact, I don't think I saw you at all."
emi "ซึ่งที่จริงเหมือนวันนี้จะไม่เห็นนายเลย"

show emi excited_proud
with charachange

# emi "What happened, hmmm?"
emi "เกิดอะไรขึ้นเหรอ หืมมม"

# hi "Fell asleep."
hi "หลับ"

# hi "I actually didn't wake up until lunch, and only then because Kenji woke me up."
hi "เพิ่งตื่นตอนเที่ยงนี่เอง แล้วที่ตื่นก็เพราะเคนจิปลุกด้วย"

show emi excited_amused
with charachange

# emi "What had you so tired, hmm?"
emi "ไปทำอะไรมาถึงได้เพลียขนาดนั้น หืมมม"

# hi "Strenuous workout this morning. Slightly uncomfortable, too."
hi "ก็เช้านี้ออกกำลังกายหนักน่ะสิ ไม่ค่อยสบายตัวด้วย"

show emi basic_closedhappy
with charachange

# "Emi coughs, a half-laughing, half-embarrassed noise."
"เอมิกระแอมกึ่ง ๆ หัวเราะกึ่ง ๆ อาย"

show emi basic_happy
with charachange

# emi "Remind me not to do that again."
emi "ฝากเตือนฉันด้วยว่าห้ามทำแบบนั้นอีก"

# hi "No problem. It wasn't exactly great for me either, to be honest."
hi "ไม่มีปัญหา เอาจริง ๆ ฉันก็รู้สึกไม่ค่อยดีเหมือนกัน"

# hi "We'll just avoid that from now on."
hi "วันหลังเราก็ไม่ต้องทำอีก"

# hi "Are you, er, still sore?"
hi "เธอยัง เอ่อ เจ็บ ๆ อยู่มั้ย"

show emi basic_confused
with charachange

# "Emi stares at me in disbelief."
"เอมิมองฉันด้วยความเหลือเชื่อ"

# hi "What? It's a legitimate question!"
hi "อะไรเล่า คนเขาเป็นห่วงเลยถามเนี่ย!"

show emi sad_grin
with charachange

# emi "Of all the questions I never thought I'd be asked, that's one of them."
emi "เป็นหนึ่งในคำถามที่ฉันไม่คิดว่าจะมีคนถามฉันเลยนะ"

# hi "Well, I didn't ever expect to have to ask it, so we're even."
hi "ก็ ฉันไม่ได้คิดไว้ว่าจะต้องถามหรอก ถือว่าเจ๊ากันแล้วกัน"

show emi basic_closedhappy
with charachange

# "Emi laughs at this."
"เอมิหัวเราะกับคำตอบนั้น"

# emi "I guess so, huh?"
emi "คงงั้นละมั้ง"

stop music fadeout 5.0

show emi sad_shy
with charachange

# emi "Well, since you asked, yes. I'm still a little sore."
emi "แต่ในเมื่อนายถามแล้วก็ ใช่ ยังเจ็บอยู่หน่อย ๆ"

show emi sad_pout
with charachange

# emi "We're never doing that again."
emi "เราจะไม่ทำแบบนั้นอีกแล้ว"

# hi "No arguments from here."
hi "ไม่มีข้อคัดค้านครับ"

# "A yawn escapes her, and I raise an eyebrow."
"เอมิหาว ฉันเลิกคิ้วขึ้น"

# hi "Tired?"
hi "เพลียเหรอ"

show emi sad_grin
with charachange

# "Emi nods sleepily."
"เอมิพยักหน้าง่วง ๆ"

play music music_serene fadein 8.0

show emi sad_depressed
with charachange

# emi "Haven't slept well."
emi "นอนไม่ค่อยหลับ"

# "Not sleeping well?"
"นอนไม่ค่อยหลับเหรอ"

# "I can tell that she didn't mean to tell me this either, because she gives a little start like she's just been caught lying and hastens to add,"
"ฉันดูออกว่าเอมิไม่ได้ตั้งใจจะบอกฉันเพราะเธอทำท่าเหมือนหลุดปากบางอย่างแล้วโดนจับโกหกได้ เอมิรีบเสริมว่า"

show emi basic_closedgrin
with charachange

# emi "It's not a big deal, though."
emi "แต่ก็ไม่ใช่เรื่องใหญ่หรอก"

# hi "What's the trouble?"
hi "มีเรื่องอะไรหรือเปล่า"

show emi basic_grin
with charachange

# "Emi shrugs and refuses to elaborate."
"เอมิยักไหล่ไม่ขยายความต่อ"

# hi "Stressed over exams?"
hi "เครียดเรื่องสอบเหรอ"

# "Another shrug, but after a pause, Emi nods hesitantly."
"เอมิยักไหล่อีกรอบ แต่เธอเว้นช่วงไปก่อนจะกึ่ง ๆ พยักหน้า"

show emi sad_shy
with charachange

# emi "Er, yeah, I guess."
emi "เอ่อ อื้ม มั้งนะ"

# emi "Actually, that's why I stopped by."
emi "จริง ๆ ที่มานี่ก็เพราะเรื่องนั้นแหละ"

# "She begins to look more and more miserable."
"เอมิทำหน้าสิ้นหวังหนักขึ้นเรื่อย ๆ"

# "Not so you'd notice, of course; but her eyes are on her lap, she's fidgeting and her voice is quiet."
"แต่ไม่ได้ทำเพื่อให้เห็นหรอก เพราะเธอมองตักตัวเองแล้วบิดตัวไปมาพูดเสียงเบา"

show emi sad_pout
with charachange

# emi "We uh, we need to stop hanging out so much."
emi "เรา เอ่อ เราต้องเลิกอยู่ด้วยกันสักพักนะ"

# hi "Huh? Why?"
hi "หือ ทำไมล่ะ"

# "Emi takes a deep breath, like she's been practicing this."
"เอมิสูดหายใจลึก ๆ เหมือนซ้อมบทมาแล้ว"

show emi sad_shy
with charachange

# emi "Because you're too much fun to be around."
emi "เพราะอยู่กับนายแล้วสนุกเกินไป"

# emi "And I can't concentrate when you're near me."
emi "พอนายอยู่ใกล้ ๆ แล้วฉันก็ไม่มีสมาธิเลย"

# emi "With exams coming up soon, I just… can't have that distraction."
emi "ยิ่งใกล้สอบแล้วด้วย ฉัน… ต้องมีสมาธิหน่อย"

show emi sad_depressed
with charachange

# emi "Otherwise my grades will be pretty lousy, I'm afraid."
emi "ไม่อย่างนั้นฉันเกรงว่าผลการเรียนของฉันจะตก"

# hi "I could help you study…"
hi "ฉันติวให้เธอได้นะ…"

show emi sad_grin
with charachange

# "She smiles at me, clearly unhappy with the situation."
"เอมิยิ้มให้ สีหน้าชัดว่าไม่อยากให้เรื่องเป็นอย่างนี้เลย"

# emi "I'd love it if you could, but we wouldn't actually study, would we?"
emi "ถ้านายติวให้ได้ก็ดี แต่เราคงจะไม่ได้อ่านหนังสือกันจริง ๆ หรอก ใช่มั้ย"

show emi sad_shy
with charachange

# emi "I mean even now, I'm trying to have a conversation with you but I kinda just want to, uh…"
emi "คือแม้แต่ตอนนี้ที่ฉันตั้งสติจะคุยกับนายฉันยังอยาก เอ่อ…"

show emi sad_shyblush
with charachange

# emi "Not converse."
emi "อยากไม่คุยแล้ว"

# hi "Ah."
hi "อ้อ"

# hi "Overwhelmed by my rugged manliness. I understand."
hi "ความเป็นชายชาตรีของฉันมันมากล้นเกินสินะ เข้าใจ ๆ"

show emi basic_grin
with charachange

# "That earns me a grin, at least."
"อย่างน้อยเอมิก็ยิ้มออกเพราะคำพูดนั้น"

# "Emi shakes her head."
"เธอสั่นหัว"

show emi basic_closedgrin
with charachange

# emi "Idiot. You're full of yourself."
emi "บ้า หลงตัวเองนะนายเนี่ย"

# hi "Well, I am pretty irresistible."
hi "แหม เป็นใครก็หลงเสน่ห์ฉันน่า"

show emi sad_shyblush
with charachange

# emi "Er, more or less. I guess."
emi "เอ่อ ก็ใช่ มั้ง"

show emi sad_grin
with charachange

# emi "So that's the situation, Hisao."
emi "เรื่องก็ประมาณนั้นแหละฮิซาโอะ"

# emi "I have too much fun around you, and if I'm going to go into exams prepared, I need to be alone."
emi "ฉันอยู่กับนายแล้วสนุกเกินไป และถ้าฉันอยากเตรียมพร้อมกับเรื่องสอบฉันก็ต้องอยู่ตัวคนเดียว"

# hi "Hey, that's okay."
hi "นี่ ไม่เป็นไรน่า"

# "It really seems to have been bothering her."
"เหมือนจะเครียดเพราะเรื่องนี้จริง ๆ"

# "Besides, it's only a couple of weeks. And we'll still see each other in the mornings, and at lunch."
"อีกอย่าง ก็แค่สองสัปดาห์เอง แถมเรายังได้เจอกันตอนเช้ากับตอนเที่ยงอยู่"

# hi  "We can just hang out at school, no problem."
hi "ก็อยู่ด้วยกันตอนช่วงที่เรียนนั่นแหละ ไม่มีปัญหา"

# hi "And after exams, we'll go on a date to celebrate their being over, okay?"
hi "แล้วพอสอบเสร็จเราต้องไปฉลองที่จบเรื่องได้สักทีกันนะ"

show emi basic_closedgrin
with charachange

# "Emi grins, pleased by this proposal."
"เอมิยิ้มดีใจกับข้อเสนอนี้"

show emi basic_happy
with charachange

# emi "Yeah, sure! That sounds great!"
emi "อื้ม ได้เลย! ใช้ได้ ๆ !"

show emi excited_amused_close at center
with characlose

# "As if to signal the end of the conversation, she leans in and kisses me."
"เอมิโน้มตัวเข้ามาจูบฉันเหมือนเป็นการส่งสัญญาณจบบทสนทนานี้"

# "The rest of the night is not spent worrying about exams."
"คืนนั้นทั้งคืนฉันไม่ได้คิดเรื่องสอบเลย"

stop music fadeout 2.0

scene black
with dissolve

#####################################

label th_E23:

window hide None

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_night fadein 4.0

scene bg school_library_bw
with locationchange

nvl clear
nvl show dissolve

# n "\n\nIt's weird how easily Emi and I can keep from seeing one another after class now."
n "\n\nแปลกดีที่เอมิกับฉันเลิกเจอกันหลังเลิกเรียนแต่ละคาบไปได้ง่าย ๆ เลย"

# n "Actually, I'd venture to say that it's vaguely disturbing."
n "ที่จริงฉันขอใช้คำว่าชวนให้ไม่สบายใจขึ้นมาหน่อย ๆ เลยดีกว่า"

# n "As easily as we'd come together, we seem to have split apart without much trouble."
n "เรามาอยู่ด้วยกันได้อย่างง่ายดาย และแยกกันอยู่ได้ไม่ลำบากนัก"

# n "Well, I guess that's not exactly true."
n "แต่ก็ไม่เชิงหรอก"

# n "We'd both been pretty bummed after that last night together."
n "เราสองคนยังคงหมอง ๆ อยู่หลังจากที่ได้อยู่ด้วยกันคืนนั้นเป็นคืนสุดท้าย"

# n "And we get to see each other every morning for our runs (and just our runs, I might add)."
n "และเราก็เจอกันทุกเช้าตอนวิ่งด้วยกัน (ขอเสริมว่าแค่วิ่งจริง ๆ )"

# n "Lunch, too. I especially enjoy lunchtime with her."
n "ตอนเที่ยงก็ด้วย ฉันชอบตอนได้อยู่กับเอมิช่วงกินข้าวเที่ยงด้วยกันเป็นพิเศษ"

# n "We have plenty of time to talk about everything outside of school, whereas the morning runs have become increasingly businesslike."
n "เพราะเรามีเวลามากพอที่จะคุยเรื่องอื่นนอกจากเรื่องเรียนกัน ส่วนการวิ่งยามเช้านั้นเริ่มเข้าใกล้คำว่าเป็นทางการ\nขึ้นเรื่อย ๆ"

# n "I think it's because Emi wants to make up for our foolery in the storage shed."
n "ฉันคิดว่าคงเพราะเอมิอยากชดเชยกับตอนที่เราเล่นสนุกกันในห้องเก็บของครั้งนั้น"

# n "But no matter how much we joke at lunch, I can't help feeling a little worried about her."
n "แต่ไม่ว่าเราจะคุยกันตอนพักเที่ยงสนุกกันแค่ไหน ฉันก็อดเป็นห่วงเอมิหน่อย ๆ ไม่ได้"

nvl clear

# n "\n\nShe seems distracted more often, and I've caught her fidgeting nervously more than once."
n "\n\nเหมือนเอมิจะเหม่อบ่อยขึ้น แล้วก็เห็นเธอบิดตัวด้วยความประหม่าอยู่หลายครั้งด้วย"

# n "Never figured her to be someone who cared that deeply about exams, but they certainly seem to be taking their toll."
n "ฉันไม่เคยคิดเลยว่าเอมิจะเป็นคนที่คิดมากเรื่องการสอบขนาดนั้น แต่ดูท่าว่าเรื่องสอบจะเริ่มมีผลกับจิตใจเธอแล้วจริง ๆ"

# n "Even though they haven't even started."
n "ทั้งที่ยังไม่ถึงวันสอบวันแรกด้วยซ้ำ"

# n "This is just the run up, the deep breath before the plunge."
n "ตอนนี้เป็นแค่ช่วงเตรียมตัว เป็นการสูดหายใจก่อนกระโดดลงน้ำ"

# n "Tomorrow, the real trials begin."
n "พรุ่งนี้บททดสอบที่แท้จริงจะเริ่มแล้ว"

# n "Or the real exams, anyway."
n "หรือก็คือวันสอบจริงนั่นแหละ"

# n "As for me, I actually don't feel that worried about exams at all."
n "ส่วนฉันก็ไม่ได้กังวลเรื่องสอบเลย"

# n "I'm not sure why. I mean, they're pretty important; my scores here will determine my odds of getting into a good university."
n "ไม่แน่ใจเหมือนกันว่าเพราะอะไร ทั้งที่การสอบครั้งนี้ก็สำคัญเพราะคะแนนจะเป็นตัวชี้ชะตาว่าฉันมีโอกาสจะสอบติด\nมหาวิทยาลัยดี ๆ มากแค่ไหน"

# n "Hell, if I'm too cavalier now, it could spell doom for my academic career."
n "ไม่สิ ถ้าฉันทำตัวลอยชายมากเกินไปก็อาจนับได้ว่าเส้นทางการเรียนต่อของฉันนั้นดับสิ้นเลยก็ได้"

# n "But going into them, I feel confident that I'll come out the other side okay."
n "แต่ตอนนี้ฉันมั่นใจว่าจะผ่านพ้นการสอบครั้งนี้ไปได้ด้วยดี"

nvl clear

# n "\n\n\n\n\n\nMutou thinks I've got the science examination locked up, at any rate."
n "\n\n\n\n\n\nครูมุโต้คิดว่าฉันพร้อมมาก ๆ ที่จะสอบวิชาวิทยาศาสตร์แล้ว"

# n "Or as he says, “The last thing that should give you trouble is my exam, Hisao. It's way beneath your talents.”"
n "เพราะพูดไว้ว่า “เธอจะมีปัญหากับวิชาไหนก็ช่าง แต่ไม่ใช่กับวิชาที่ครูสอนแน่นอนฮิซาโอะ ความสามารถเธอ\nอยู่สูงกว่าข้อสอบครูมาก”"

# n "Then again, it is Mutou who's telling me this."
n "แต่ก็นะ คนที่พูดคือครูมุโต้"

# n "His praise of me carries the veiled implication that anything less than perfect from me would be a disappointment, which has actually caused me to fret more than I should about the exam.
n "คำชมของครูมีนัยแอบแฝงว่าถ้าทำออกมาได้ไม่ดีแล้วครูคงผิดหวัง ซึ่งทำให้ฉันเครียดกับเรื่องสอบกว่าปกติ"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

scene bg school_library
with locationchange

window show

# "It's for that reason that I find myself in the library after class, poring over the textbook."
"และเพราะเช่นนั้นเองพอเลิกเรียนแล้วฉันจึงมานั่งอ่านหนังสืออยู่ที่ห้องสมุด"

# "Pretty simple things to look over; some formulas of velocity, a few bits about friction…"
"เป็นเรื่องที่ค่อนข้างง่าย สูตรความเร่งสองสูตรสองสูตร แล้วก็เรื่องแรงเสียดทานบ้าง…"

# "A walk in the park compared to my dreaded English exam. Never was good with languages…"
"ถ้าให้เทียบกับคู่ปรับของฉันอย่างวิชาภาษาอังกฤษแล้วก็นับได้ว่ากล้วย ๆ ฉันไม่ถนัดเรื่องภาษาเอาเสียเลย…"

# "As I flip through my notes one more time, my mind begins to wander."
"พอพลิกหน้าสมุดดูอีกรอบจิตใจฉันก็เริ่มล่องลอย"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

# n "\n\n\nAfter these exams are over, things should get easier."
n "\n\n\nถ้าสอบเสร็จแล้วอะไร ๆ ก็น่าจะง่ายขึ้น"

# n "Soon we'll be graduated."
n "อีกเดี๋ยวก็จะเรียนจบกันแล้ว"

# n "Then off to college, hopefully."
n "แล้วก็—หวังว่านะ—จะได้เรียนต่อมหาวิทยาลัย"

# n "I remember my abortive attempt to find out what Emi plans to do after high school."
n "ฉันนึกถึงแต่ละครั้งที่ฉันคอยถามเอมิว่าเรียนจบแล้วจะทำอะไรต่อ"

# n "Hmm, she avoided the subject pretty deftly, as I recall."
n "อืมมม เท่าที่นึกออก เอมิเบี่ยงหัวข้อได้เนียนทีเดียว"

# n "Heck, it seems that just about every time I push too hard, she dances around the subject."
n "ไม่สิ เหมือนทุกครั้งที่ฉันซักไซ้มาก ๆ เข้าเอมิก็จะพูดอ้อมไปอ้อมมา"

# n "Or distracts me through… other means."
n "หรือไม่ก็เบนความสนใจฉันด้วย… วิธีอื่น"

# n "Like a few days ago at lunch, when Rin wasn't around…"
n "เหมือนเมื่อสองสามวันก่อนตอนเที่ยงที่รินไม่อยู่ด้วย…"

# n "Heh."
n "ฮะ ๆ"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide None
window show None

stop music fadeout 0.2

show yuuko happy_up
with vpunch

# yu "I've done it!"
yu "สำเร็จแล้ว!"

# "I'm startled from my reverie by Yuuko's triumphant shout."
"เสียงตะโกนอย่างภาคภูมิของยูโกะดึงให้ฉันหลุดจากภวังค์"

# hi "Gah!"
hi "ว้าก!"

show yuuko panic_up
with charachange

# "Yuuko seems mortified at my sudden starting."
"เหมือนยูโกะจะผงะไปที่ฉันสะดุ้งแบบกะทันหัน"

play music music_happiness fadein 2.0

# yu "Oh my god!"
yu "ตายแล้ว!"

show yuuko panic_down
with charachange

# yu "I'm so sorry! I just got - and I really wasn't - and it's just that—"
yu "ขอโทษที! พอดีฉัน แล้วก็ฉันไม่ได้ แค่ว่าฉัน—"

# "As she stutters, I move to quickly calm her down before she gets too agitated."
"ยูโกะพูดตะกุกตะกักจนฉันต้องรีบเข้าไปช่วยสงบใจไม่ให้ลนลานไปกว่านี้"

# hi "Woah, hey."
hi "เอ้า ๆ เดี๋ยวครับ"

# "My words seem ineffective."
"ที่ฉันพูดไปเหมือนจะไม่ได้ผล"

# "Yuuko continues to work herself into a complete frenzy."
"ยูโกะยังคงทำตัวร้อนรนขึ้นเรื่อย ๆ จนสติหลุด"

show yuuko panic_up
with charachange

# yu "And it's a library and I shouldn't be—"
yu "แล้วก็ที่นี่เป็นห้องสมุดด้วย ฉันไม่ควรจะ—"

# hi "Easy there, just calm down."
hi "ค่อย ๆ พูดครับ ใจร่ม ๆ ก่อน"

show yuuko cry_down
with charachange

# yu "And really I'm setting a bad example, and now I'll get fired because I can't do anything right—"
yu "แล้วตอนนี้ฉันก็เป็นตัวอย่างที่ไม่ดี แล้วทีนี้ฉันก็จะโดนไล่ออกเพราะทำอะไรก็ไม่ได้เรื่อง—"

# hi "YUUKO!" with vpunch
hi "คุณยูโกะ!!" with vpunch

show yuuko worried_up
with charachange

# "Shouting seems to work, though I draw the ire of several other students studying in the library."
"การตะโกนดูจะได้ผล ถึงตอนนี้จะมีนักเรียนที่อยู่ในห้องสมุดหลายคนหันมามองด้วยความไม่พอใจก็ตาม"

# "Yuuko snaps to attention, like a soldier who's just heard the captain bark an order."
"ยูโกะได้สติทันทีเหมือนทหารที่ได้ยินนายออกคำสั่ง"

show yuuko neurotic_up
with charachange

# yu "Sorry! Sorry!"
yu "ขอโทษ! ขอโทษ!"

# hi "Calm down, it's okay."
hi "ใจเย็น ๆ ครับ ไม่เป็นไรหรอก"

# hi "You just startled me a little, and that's only because I was daydreaming instead of studying."
hi "ผมแค่ตกใจนิดหน่อย แล้วที่ตกใจก็เพราะผมมัวแต่เหม่ออยู่แทนที่จะอ่านหนังสือ"

# hi "So really, you got me back on task."
hi "เพราะงั้นเอาเข้าจริง ๆ แล้วคุณช่วยให้ผมกลับมาอ่านต่อได้ด้วยซ้ำ"

# "This is a complete lie. But it seems to work."
"โกหกทั้งเพ แต่ก็ดูจะได้ผล"

show yuuko worried_down
with charachange

# "Yuuko takes a deep breath and seems to calm down a little."
"ยูโกะสูดหายใจลึกทำท่าเหมือนสงบลงบ้างแล้ว"

# "Though she keeps shifting around with a nervous energy that seems awfully familiar."
"แต่ก็ยังบิดตัวไปมาด้วยความประหม่า ซึ่งเป็นภาพที่ฉันคุ้นเคยเป็นอย่างดี"

# hi "So, what's got you so excited anyway?"
hi "แล้วมีเรื่องอะไรถึงตื่นเต้นขนาดนี้เหรอครับ"

show yuuko neutral_up_close
with characlose

# yu "The Yamaku Cat Burglar!"
yu "แมวขโมยยามากุ!"

# "To her credit, Yuuko manages to convey her intense excitement in a whisper."
"ต้องขอชมที่ยูโกะยังอุตส่าห์ส่งผ่านความตื่นเต้นมาได้ทั้งที่แค่กระซิบอยู่"

show yuuko closedhappy_up_close
with charachange

# yu "I think I know who it is!"
yu "ฉันว่าฉันรู้ตัวคนร้ายแล้ว!"

show yuuko happy_down_close
with charachange

# yu "I got an anonymous tip as to their identity!"
yu "ฉันได้เบาะแสถึงตัวตนของคนร้ายมาจากคนนิรนาม!"

# yu "So I did some spying, and I think the tipster was right!"
yu "ฉันเลยไปตามสืบ แล้วก็เป็นอย่างที่คนให้เบาะแสมาจริง ๆ !"

# hi "Oh really? And who was this er, burglar?"
hi "จริงเหรอครับ แล้วใครคือ เอ่อ ขโมยคนนี้"

show yuuko worried_down_close
with charachange

# "Yuuko shuts her mouth, shaking her head decisively."
"ยูโกะปิดปากสั่นหัวด้วยความมั่นใจ"

# yu "Nope, I can't tell you that."
yu "ไม่ บอกเธอไม่ได้"

# hi "Why not?"
hi "ไหงงั้นล่ะครับ"

show yuuko worried_up_close
with charachange

# yu "It's between me and the burglar."
yu "เรื่องนี้เป็นเรื่องของฉันกับขโมยเท่านั้น"

# yu "I can't risk you warning him that I'm on to his game."
yu "ขืนบอกแล้วเดี๋ยวเธอเอาไปบอกต่อว่าฉันกำลังตามตัวเขาอยู่"

# yu "He could tip his hand early and blow town."
yu "เขาอาจรีบลงมือแล้วชิ่งไปเลยก็ได้"

# yu "Then I'm left with no perp."
yu "แล้วฉันก็จะไม่ได้ตัวคนร้ายเลย"

# "When did Yuuko start talking like a hard-boiled detective?"
"นี่ยูโกะพูดเหมือนเป็นนักสืบในหนังสืบสวนได้ตั้งแต่เมื่อไหร่"

# hi "I wouldn't warn them! Why would I care?"
hi "ผมไม่เอาไปบอกหรอกครับ! ผมจะไปสนใจทำไม"

show yuuko neutral_down
with charadistant

# yu "If you've got to ask that question, then you don't need to know."
yu "ถ้าเธอถามแบบนี้ก็แปลว่าเธอไม่จำเป็นต้องรู้"

# hi "That doesn't make any sense, but okay."
hi "ไม่เห็นจะเข้าใจเลย แต่โอเค"

# hi "Congratulations, I guess?"
hi "ยินดีด้วย ละมั้งครับ"

show yuuko closedhappy_down
with charachange

# yu "Thanks!"
yu "ขอบคุณนะ!"

show yuuko worried_up
with charachange

# yu "Uh, what for?"
yu "เอ่อ เรื่องอะไรล่ะ"

# hi "The uh, cat burglar thing?"
hi "เรื่อง เอ่อ แมวขโมยยามากุมั้งครับ"

show yuuko smile_down
with charachange

# "Yuuko nods and smiles appreciatively."
"ยูโกะพยักหน้าแล้วยิ้มขอบคุณ"

# yu "So! Studying for exams?"
yu "แล้วนี่! อ่านหนังสือเตรียมสอบอยู่เหรอ"

# hi "Well, that was the plan. I'm not having much luck, though."
hi "ก็คิดไว้งั้นแหละครับ แต่อ่านไม่ค่อยรู้เรื่องเท่าไหร่"

show yuuko worried_down
with charachange

# yu "Really? Is it because you can't find a book?"
yu "จริงเหรอ เพราะหาหนังสือไม่เจอหรือเปล่า"

show yuuko panic_up
with charachange

# yu "I'm really sorry!"
yu "ขอโทษจริง ๆ นะ!"

# yu "I've been meaning to clean the shelves up for weeks now, but I keep getting distracted!"
yu "ฉันกะจะเก็บกวาดชั้นหนังสือมาสองสามสัปดาห์แล้ว แต่เพราะมัวแต่สนใจอย่างอื่นเลยไม่ได้มาทำ!"

# yu "I'm so sorry!"
yu "ขอโทษจริง ๆ !"

# hi "Woah, wait."
hi "เอ้า ๆ เดี๋ยวครับ"

# hi "It's not that. I've got my book right here."
hi "ไม่ใช่เพราะอย่างนั้นเลย ผมก็ได้หนังสือแล้วนี่ไง"

# "To illustrate the point and hopefully calm Yuuko down, I show her the textbook in front of me."
"ฉันผายมือไปที่หนังสือที่อยู่ตรงหน้าฉันเป็นการตอกย้ำคำพูดนั้นและหวังว่าพอทำแล้วยูโกะจะสงบใจลงได้บ้าง"

# hi "My mind just keeps wandering, is all."
hi "ผมแค่เหม่อเฉย ๆ"

show yuuko worried_up
with charachange

# yu "Is it because of the noise in here?"
yu "เพราะในนี้เสียงดังหรือเปล่า"

# yu "I'm trying to be more strict about the noise levels, but I can't bring myself to yell at people…"
yu "ฉันก็เข้มงวดกับเรื่องการใช้เสียงในห้องสมุดอยู่นะ แต่ฉันตะโกนว่าคนอื่นไม่ลง…"

show yuuko worried_down
with charachange

# yu "I mean aren't their lives hard enough without me throwing my authority around?"
yu "เพราะขนาดฉันไม่ใช้อำนาจ แค่นี้แต่ละคนก็เหนื่อยกับชีวิตตัวเองอยู่แล้วนี่"

# hi "No, it's not the noise level either, I promise."
hi "เปล่าครับ ไม่ใช่เรื่องเสียงด้วย ผมพูดเลย"

# hi "I'm just…"
hi "ผมแค่…"

# "Hell, I don't know."
"โอย ไม่รู้"

# "Worried about Emi."
"คิดมากเรื่องเอมิ"

# "Worried about us."
"คิดมากเรื่องเรา"

# "Worried about what happens after we graduate."
"คิดมากว่าพอเราเรียนจบแล้วจะเป็นยังไงบ้าง"

# hi "Emi's been kind of weird, lately."
hi "ช่วงนี้เอมิทำตัวแปลก ๆ นะครับ"

show yuuko worried_up
with charachange

# yu "What do you mean?"
yu "หมายความว่าไงเหรอ"

# hi "Well, you know how we're dating now?"
hi "ก็ ตอนนี้เราสองคนคบกันอยู่ใช่มั้ยครับ"

# hi "I just don't know that we're actually, you know…"
hi "คือผมไม่แน่ใจว่าเรา เนี่ย…"

# hi "A couple. Or at least I don't know that we're beyond friends."
hi "เป็นแฟนกันจริง ๆ หรือเปล่า ไม่รู้ว่าเราเป็นมากกว่าเพื่อนมั้ย"

# "Though friends normally don't do the sort of things we do."
"ถึงเพื่อนจะไม่ทำอะไรแบบที่เราทำกันหรอก"

# "Physically we're a couple."
"ถ้านับทางกายแล้วเราก็เป็นแฟนกัน"

# "Coupling, at least."
"อย่างน้อยก็เป็นคู่กัน"

# hi "It's like every time I try to find out more about her, or about what she wants to do with her life, she dodges the question."
hi "เหมือนพอผมอยากรู้ว่าเอมิจะเอายังไงกับชีวิตตัวเองหรือทำความรู้จักกับเอมิให้มากขึ้นทีไรแล้วเอมิก็จะ\nเลี่ยงคำถามตลอดเลย"

# hi "Like the other day, I was talking to her at lunch about some schools I've been looking into."
hi "อย่างวันก่อนผมก็คุยกับเอมิตอนพักเที่ยงเรื่องมหา’ลัยที่ผมไปหาข้อมูลมา"

# hi "And I asked her, “Have you looked into any schools lately?”"
hi "แล้วผมก็ถามเอมิว่า “ช่วงนี้ได้ดูที่ไหนไว้มั้ย”"

# hi "She shrugs in response, says no, and when I ask why not, she says that she doesn't think that far ahead."
hi "เอมิยักไหล่แล้วตอบว่าไม่ พอถามว่าทำไมถึงไม่ดู เอมิก็บอกว่าไม่ได้วางแผนไว้ไกลขนาดนั้น"

# hi "I asked why she had that policy, and she…"
hi "แล้วพอถามว่าทำไมถึงถือแนวคิดแบบนั้นเอมิก็…"

# "I suddenly realize what I'm about to start describing, and wisely decide to clam up."
"อยู่ ๆ ฉันก็ระลึกได้ว่าตัวเองกำลังจะเล่าอะไรต่อ คิดได้ดังนั้นแล้วฉันเงียบปากไปทันที"

show yuuko neutral_up
with charachange

# yu "She what?"
yu "เอมิก็อะไร"

# hi "Er, she changed the subject."
hi "เอ่อ เปลี่ยนเรื่องน่ะครับ"

# hi "Wouldn't talk about it."
hi "ไม่ยอมคุยเรื่องนั้น"

show yuuko neutral_down
with charachange

# yu "Maybe it's an uncomfortable subject for her?"
yu "อาจจะเพราะเอมิไม่สบายใจที่จะคุยเรื่องนั้นหรือเปล่า"

# yu "Or she just doesn't think it needs explaining."
yu "หรือไม่ก็เพราะคิดว่าเป็นเรื่องที่ไม่ต้องอธิบายอะไร"

# hi "Yeah, but it's not just that."
hi "ครับ แต่ไม่ใช่แค่นั้นน่ะสิ"

# hi "Every time I try to find out what's been bothering her, she changes the subject too."
hi "ทุกครั้งที่ผมถามว่ามีเรื่องอะไรกวนใจอยู่หรือเปล่าเอมิก็เปลี่ยนเรื่องไปเหมือนกัน"

# hi "It's like she likes being with me, but not getting close to me."
hi "เหมือนตัวอยู่ใกล้แต่ไม่ได้ทำตัวสนิทด้วย"

# "Now that I've said it out loud, I feel worse."
"พอพูดออกมาแล้วก็รู้สึกแย่แฮะ"

# "Yuuko digests this bit of information."
"ยูโกะประมวลผลข้อมูลที่ฉันพูดไป"

show yuuko worried_down
with charachange

# yu "You know, it seems to me that you're more serious about this than she is."
yu "คือ ฉันรู้สึกเหมือนว่าเธอจะจริงจังกับเรื่องนี้มากกว่าเอมิ"

# "I can almost feel my stomach twist into a knot."
"ตอนนี้เหมือนฉันใจแป้วไปเลย"

# "She's right."
"ยูโกะพูดถูก"

# "That's exactly what it seems like."
"เพราะดูเหมือนเป็นแบบนั้นจริง ๆ"

# hi "But is that really what's going on? I mean…"
hi "แต่จะเป็นอย่างนั้นจริงเหรอครับ คือ…"

show yuuko panic_up
with charachange

# yu "Sorry! I'm just talking nonsense!"
yu "ขอโทษ! ฉันแค่พูดไปเรื่อย!"

# yu "You shouldn't take my advice, you barely know me!"
yu "อย่าฟังคำแนะนำของฉันเลยนะ เธอเพิ่งจะรู้จักฉันได้ไม่นานนี้เอง!"

show yuuko cry_down
with charachange

# yu "I'm just the librarian, and I'm single so you can imagine I can't know what I'm talking about!"
yu "ฉันก็เป็นแค่บรรณารักษ์ แถมโสดด้วย ยังไงเธอก็คงรู้ว่าฉันไม่ได้มีความรู้จริง ๆ หรอก!"

# hi "No, I think…"
hi "ไม่สิครับ ผมว่า…"

# hi "I think you have a point."
hi "ผมว่าคุณพูดถูก"

# "As much as it hurts to even consider it."
"ต้องยอมรับแม้จะเจ็บปวดเมื่อคิดอย่างนั้นก็ตาม"

# "Yuuko seems to try desperately to find a way to soften the blow somewhat."
"ยูโกะเหมือนจะพยายามหาทางซับแรงกระแทกให้ได้"

show yuuko neutral_down
with charachange

# yu "Er, look."
yu "เอ่อ นี่นะ"

show yuuko smile_down
with charachange

# yu "I'm probably wrong, but if you want to be sure of how obviously wrong I am, maybe you should just talk to her?"
yu "ฉันอาจจะคิดผิด แต่ถ้าอยากแน่ใจจริง ๆ ว่าฉันคิดผิดแค่ไหนเธอก็ไปคุยกับเอมิสิ"

# yu "Get some time alone and just ask about it."
yu "หาเวลาอยู่ด้วยกันแล้วก็ถามไปเลย"

show yuuko closedhappy_down
with charachange

# yu "And don't let her change the subject, either!"
yu "แล้วก็ห้ามปล่อยให้เอมิเปลี่ยนเรื่องได้ด้วย!"

# hi "Yeah, maybe I should do that."
hi "ครับ ผมคงต้องทำแบบนั้นแหละ"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

# n "\n\nOr maybe I should just enjoy what I have."
n "\n\nหรือฉันจะอยู่ทั้งแบบนี้ไปนั่นแหละ"

# n "We have fun hanging out, after all."
n "เพราะยังไงเราก็สนุกที่ได้อยู่ด้วยกัน"

# n "And the runs are nice, and the other activities are nice, and talking to her is nice…"
n "ตอนวิ่งก็ดี กิจกรรมอื่นก็ดี ได้คุยกับเอมิก็ดี"

# n "Do I really need to get closer to her? What I've got right now is pretty good."
n "ฉันจำเป็นต้องสนิทกับเอมิให้มากกว่านี้ด้วยเหรอ เท่าที่เป็นอยู่ตอนนี้ก็ดีแล้วนี่"

# n "But that's silly."
n "คิดอะไรบ้าบอ"

# n "I want to get closer to her."
n "ฉันอยากจะสนิทกับเอมิให้มากกว่านี้"

# n "I want to be able to help her out with whatever is bothering her."
n "อยากจะช่วยจัดการปัญหาที่กวนใจเอมิอยู่"

# n "But… maybe I should wait until after exams are over."
n "แต่… คงต้องรอให้สอบเสร็จก่อน"

# n "Maybe she'll brighten up once the stress has passed."
n "ถ้าแรงกดดันหายแล้วเอมิอาจจะร่าเริงขึ้นก็ได้"

# n "If she does, then I don't need to worry about it any more."
n "ถ้าร่าเริงขึ้นแล้วฉันก็ไม่ต้องคิดมากเรื่องนี้อีก"

# n "But if she doesn't, well."
n "แต่ถ้าไม่ร่าเริงขึ้นก็ นะ"

# n "I'll cross that bridge when I come to it."
n "เมื่อถึงเวลาแล้วฉันคงต้องทำสิ่งที่ควรทำ"

$ renpy.music.set_volume(1.0, 2.0, channel="music")

nvl hide dissolve
nvl clear
window show

stop music fadeout 5.0

# "I thank Yuuko for her advice and head back to my room."
"ฉันขอบคุณยูโกะที่ให้คำแนะนำแล้วกลับมาที่ห้องตัวเอง"

scene bg school_hallway2
with locationchange

# "Maybe I'll be able to concentrate more on my studies in there."
"อ่านหนังสือในห้องนี้แล้วอาจมีสมาธิขึ้นมาหน่อย"

scene black
with dissolve

#####################################

label th_E24:

scene bg school_hallway3
with locationskip
play music music_tranquil fadein 3.0

# "I leave the room after finishing my final exam and breathe a sigh of relief."
"ฉันออกจากห้องมาหลังจากที่สอบเสร็จแล้วและถอนหายใจด้วยความโล่งอก"

# "As I'd hoped, the exams weren't so bad. I managed to breeze through just about everything but the English final."
"ข้อสอบไม่ได้ยากมากดังหวัง ฉันทำข้อสอบปลายได้เกือบทุกวิชายกเว้นวิชาภาษาอังกฤษ"

# "And even that was acceptable."
"ซึ่งก็ยังพอถูไถอยู่"

# "I wonder how Emi did."
"เอมิจะเป็นยังไงบ้างนะ"

# "Even more so, how she's doing; she looked terrible at lunch today."
"ไม่ได้หมายถึงแค่เรื่องสอบหรอก เห็นตอนเที่ยงดูไม่ค่อยไหวเลย"

# "I mean, she was pretty happy to be out of her wheelchair, but she was so exhausted."
"เอมิก็ดีใจอยู่แหละที่ไม่ต้องใช้วีลแชร์แล้ว แต่เธอก็เพลียมาก"

# "Something's been wearing her down, and I'm starting to really doubt that it was just the exams."
"เอมิเหนื่อยกับอะไรบางอย่างอยู่ ฉันชักสงสัยแล้วว่าน่าจะไม่ใช่แค่เครียดเรื่องสอบแน่ ๆ"

# "Should I confront her about this, though?"
"แต่จะไปถามตรง ๆ เลยดีไหม"

# "My musing is interrupted by a tap on the shoulder."
"ระหว่างที่คิดอยู่ก็มีนิ้วมาสะกิิดไหล่ฉัน"

show muto smile at center
with charaenter

# mu "Hey, Hisao."
mu "นี่ ฮิซาโอะ"

label th_choiceE24:
menu:
    with menueffect

    # mu "Got a minute?"
    mu "พอจะมีเวลามั้ย"

    # "I suppose I can spare a few minutes.":
    "สักสองสามนาทีคงไม่เป็นไร":
        return m1

    # "No, I have other things to worry about.":
    "ไม่ได้ ยังมีเรื่องอื่นให้ต้องคิดอยู่":
        return m2

label th_E24a:

#choice time, kiddies!  Either a) Yeah, sure or b) Not really…

#if a

# hi "Yeah, I've got some time. Nowhere important to be or anything like that."
hi "ครับ พอจะมีเวลาอยู่ ไม่ได้มีธุระต้องไปที่ไหนอะไรแบบนั้น"

show muto normal
with charachange

# "Mutou raises an eyebrow as if questioning my statement, then beckons me back into the classroom."
"ครูเลิกคิ้วขึ้นสงสัยกับคำพูดของฉันก่อนจะบุ้ยใบ้ให้กลับเข้าไปที่ห้องเรียน"

hide muto
with charaexit

scene bg school_scienceroom
with locationchange

show muto normal at center
with charaenter

# mu "I wanted to get some feedback from you, if I could."
mu "ครูแค่อยากถามความคิดเห็นเธอหน่อยว่าที่ฉันสอนเป็นยังไงบ้าง"

# mu "I know that this course wasn't quite up to your level…"
mu "ครูรู้ว่าวิชานี้ยังง่ายไปหน่อยสำหรับเธอ…"

# hi "Don't worry about it. The science club activities more than made up for it."
hi "ไม่ต้องห่วงหรอกครับ แค่กิจกรรมชมรมวิทยาศาสตร์ก็นับว่าชดเชยกันได้แล้ว"

show muto smile
with charachange

# mu "Hmm, did they?"
mu "อืมม งั้นเหรอ"

show muto normal
with charachange

# mu "Well in fact, that's what I wanted to talk to you about."
mu "โอเค ที่จริงครูก็อยากคุยกับเธอเรื่องนี้แหละ"

# mu "Do you think that was a worthwhile activity? Just for my own reference."
mu "เธอคิดว่ากิจกรรมมันคุ้มกับเวลาที่เสียไปมั้ย ครูจะได้เอาไปคิดต่อ"

# hi "Well yeah, it was a great way to go further than we did in class. It was definitely worthwhile."
hi "ก็ดีอยู่นะครับ ได้รู้เนื้อหาที่ไปไกลกว่าที่เราเรียนกันด้วย ถือว่าคุ้มมากครับ"

show muto smile
with charachange

# "Mutou seems delighted by my response."
"ครูดูดีใจกับคำตอบนั้น"

# mu "That's great! Exactly the sort of thing I was hoping for."
mu "ดีแล้ว! นี่แหละที่ครูหวังไว้"

# mu "You know, Hisao, I'm glad you came here. It's always good to have a student who really gets into the subject you teach."
mu "นี่นะฮิซาโอะ ครูดีใจมากที่เธอมาเรียนที่นี่ พอมีนักเรียนที่สนใจวิชาที่ตัวเองสอนแล้วคนเป็นครูน่ะก็ย่อมรู้สึกดี\nอยู่แล้ว"

# mu "In a way, it makes dealing with the rest of the students more tolerable."
mu "ในแง่หนึ่งก็ทำให้มีแรงใจมารับมือกับนักเรียนคนอื่นด้วย"

# mu "You're a bright kid, too. You took to this stuff like a duck to water, or some other such simile."
mu "เธอก็เป็นเด็กฉลาดด้วย เรียนได้ง่าย ๆ เหมือนจระเข้ว่ายน้ำ หรือสำนวนอะไรแบบนั้นแหละ"

# hi "Er, thanks."
hi "เอ้อ ขอบคุณครับ"

# hi "You were a great help. Especially with that college stuff."
hi "ครูก็ช่วยผมได้หลายเรื่องเลย โดยเฉพาะเรื่องมหาวิทยาลัยอะไรพวกนี้"

show muto normal
with charachange

# mu "There's one more thing, Hisao."
mu "ยังมีอีกเรื่องนะฮิซาโอะ"

# mu "A bit of advice, from one scientist to another."
mu "จะขอให้คำแนะนำในฐานะนักวิทยาศาสตร์ด้วยกัน"

# hi "What's that?"
hi "อะไรเหรอครับ"

# mu "What does a scientist do?"
mu "นักวิทยาศาสตร์ทำอะไร"

# hi "Observe the world around him."
hi "สังเกตโลกรอบตัวครับ"

show muto smile
with charachange

# mu "Exactly. Good."
mu "ใช่เลย ดี"

show muto normal
with charachange

# mu "A simple question, but one that most people can't seem to answer. That's the essence of a scientist, Hisao."
mu "คำถามง่าย ๆ ที่หลายคนเหมือนจะตอบไม่ได้ นี่แหละคือแก่นแท้ของนักวิทยาศาสตร์ละฮิซาโอะ"

# mu "We observe what's there, and try to figure it out."
mu "เราสังเกตสิ่งที่อยู่ตรงหน้าแล้วก็ศึกษามัน"

# mu "But what if there's something you can't figure out?"
mu "แต่ถ้าเป็นสิ่งที่ศึกษาไม่ได้ล่ะ"

# mu "What's a scientist to do if he can't observe something?"
mu "ถ้านักวิทยาศาสตร์สังเกตอะไรไม่ได้แล้วเขาจะทำยังไง"

# mu "How, for example, can we talk about quarks when nobody has ever actually seen one? Or black holes when observing them directly is impossible?"
mu "เช่นว่า เราคุยเรื่องควาร์กกันได้ยังไงในเมื่อไม่มีใครเคยเห็นมันเลย หรือเราคุยเรื่องหลุมดำได้ยังไง\nในเมื่อการสังเกตโดยตรงนั้นเป็นไปไม่ได้"

# hi "Well, scientific equipment's pretty advanced…"
hi "ก็ เครื่องมือทางวิทยาศาสตร์สมัยนี้ก็พัฒนามาไกลมากแล้ว…"

show muto irritated
with charachange

# "Mutou irritably waves away my response."
"ครูโบกมือปัด ๆ ด้วยความหงุดหงิดกับคำตอบฉัน"

# mu "No, that's not it at all."
mu "ไม่ ไม่ใช่อย่างนั้นเลย"

# mu "Those are tools, I'm trying to give you a philosophy."
mu "ของพวกนั้นเป็นเครื่องมือเฉย ๆ ครูกำลังจะให้เธอได้รู้จักกับแนวคิดอยู่"

show muto normal
with charachange

# mu "Think. If you can't observe something directly, then how can you observe it?"
mu "คิดดูสิ ถ้าเราสังเกตอะไรไม่ได้ตรง ๆ แล้วเราจะสังเกตยังไง"

# hi "Uh, guess?"
hi "เอ่อ เดาเหรอครับ"

# mu "How? How would you guess the movement of a quark? What is your guess based on?"
mu "ยังไงล่ะ เราจะเดาการเคลื่อนที่ของควาร์กยังไง เราใช้อะไรเดา"

# "Of course."
"แหงอยู่แล้ว"

# "I should have thought of it earlier."
"ทำไมถึงไม่คิดได้ตั้งแต่เมื่อกี้นะ"

# hi "The things it affects."
hi "สิ่งโดยรอบที่ได้รับผลกระทบจากสิ่งนั้น"

show muto smile
with charachange

# "Mutou claps his hands together excitedly and whoops."
"ครูตบมือแปะด้วยความตื่นเต้นแล้วร้องด้วยความดีใจ"

# mu "Yes, exactly. Good."
mu "ใช่ นั่นแหละ ดีมาก"

# mu "Remember that, Hisao."
mu "จำไว้นะฮิซาโอะ"

show muto normal
with charachange

# mu "If you can't examine something directly, it's because you're looking at it wrong."
mu "ถ้าเราพิจารณาอะไรไม่ได้ตรง ๆ ก็เป็นเพราะเรามองผิดมุม"

# mu "You have to look at it differently if you want to uncover the truth. And if it eludes you, then look at what it leaves behind."
mu "ถ้าอยากรู้ความจริงเราก็ต้องมองอีกมุมหนึ่ง และถ้ายังมองไม่เห็นเราก็จะดูร่องรอยที่สิ่งนั้นทิ้งเอาไว้"

# mu "That is the essence of being a scientist. We never stop looking for the answer. Never take anything for granted."
mu "นี่แหละคือแก่นแท้ของการเป็นนักวิทยาศาสตร์ เราไม่เคยหยุดการค้นคว้าหาคำตอบ ห้ามมองอะไร\nไปแบบผ่าน ๆ เด็ดขาด"

# mu "Observe, experiment, and observe some more."
mu "สังเกต ทดลอง แล้วก็สังเกตซ้ำอีก"

# mu "There's a lot of stuff out there that makes no sense, Hisao. Your job is to get it to make sense."
mu "ยังมีอะไรหลายอย่างที่มันไม่สมเหตุสมผลนะฮิซาโอะ หน้าที่ของเธอคือการทำความเข้าใจให้มันสมเหตุสมผลขึ้นมา"

# mu "If nothing else, I hope you've learned that here."
mu "อย่างน้อย ๆ ครูก็หวังว่าเธอจะได้เรียนรู้แนวคิดนี้ตอนเรียนอยู่ที่นี่นะ"

# hi "I think I can remember that."
hi "จะจำไว้ครับ"

show muto smile
with charachange

# "Mutou smiles, satisfied."
"ครูยิ้มด้วยความพอใจ"

# mu "Good. Now go enjoy your time off. You've earned it."
mu "ดี ทีนี้ก็ไปพักให้เต็มที่เถอะ เธอเหนื่อยมาเยอะแล้ว"

stop music fadeout 8.0

scene bg school_hallway3
with locationchange

# "I leave the room feeling a little confused."
"ฉันออกจากห้องเรียนมาด้วยความสับสนเล็กน้อย"

# "What brought that on?"
"ทำไมครูถึงพูดเรื่องนี้ขึ้นมา"

# "Although…"
"แต่ว่า…"

# "Am I going about this thing with Emi the wrong way?"
"หรือฉันจะคิดเรื่องเอมิผิดมุมไป"

# "If she won't tell me, then can I go about it some other way?"
"ถ้าเอมิไม่ยอมบอก ก็อาจจะต้องหาทางอื่นเพื่อตามหาความจริง"

#if b

label th_E24b:

# hi "Actually, I've got something I need to do…"
hi "คือจริง ๆ ผมมีธุระอยู่…"

show muto normal
with charachange

# mu "Yeah? Oh well."
mu "อ้าว งั้นก็ไม่เป็นไร"

# mu "I wanted to get some feedback on the science club from you. But we can do that later, I guess."
mu "ครูแค่อยากขอความคิดเห็นจากเธอเรื่องชมรมวิทยาศาสตร์หน่อยน่ะ แต่ไว้ค่อยมาคุยกันก็ได้"

# mu "Enjoy your break, you hear?"
mu "พักผ่อนให้เต็มที่นะ"

# hi "Thanks, I will."
hi "ครับ ได้ครับ"

# "I'd really love to chat with Mutou, but I've got other things on my mind."
"ก็อยากจะคุยกับครูอยู่หรอก แต่ในหัวฉันตอนนี้มีเรื่องอื่นอยู่"

# "Specifically, what to do about Emi."
"หรือก็คือ ฉันจะเอายังไงกับเอมิดี"

# "Can I really just confront her?"
"ไปเจอหน้ากันตรง ๆ เลยได้หรือเปล่า"

#end split

label th_E24c:

scene bg school_dormhisao
with locationskip

# "The question keeps spinning in my head even after I made my way back to my room."
"คำถามเหล่านั้นยังคงวนเวียนอยู่ในหัวมาแม้แต่ตอนที่ถึงห้องแล้ว"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

# n "\n\nWhat if she gets angry about it?"
n "\n\nถ้าเกิดว่าเอมิโกรธขึ้นมาล่ะ"

# n "Besides, what if it's nothing?"
n "อีกอย่าง ถ้าเกิดมันไม่มีอะไรเลยล่ะ"

# n "If I go in and refuse to leave until she tells me what's wrong or something, won't that come off as clingy?"
n "ถ้าฉันเข้าไปในห้องแล้วไม่ยอมออกมาจนกว่าเอมิจะยอมบอกว่ามีเรื่องอะไรแล้วจะดูเป็นคนตื๊อเกินไปมั้ย"

# n "I don't want to start a fight or anything over something like this."
n "ไม่อยากมาทะเลาะกันเพราะเรื่องแบบนี้เลย"

# n "Maybe I should just drop the matter and see how she is tomorrow before I do anything."
n "หรือจะพักเรื่องนี้ไว้ก่อน รอดูว่าพรุ่งนี้เอมิจะเป็นยังไงแล้วค่อยทำอะไรต่อ"

# n "Would it be so bad to just let it go?"
n "ปล่อย ๆ ไปเลยก็คงไม่ได้แย่หรอกมั้ง"

# n "It's not like we don't enjoy each other's company."
n "ใช่ว่าเราจะรังเกียจการอยู่ด้วยกันที่ไหน"

# n "But odd as it sounds, I really want to… help her."
n "แต่ถึงจะฟังดูแปลก ฉันอยากจะ… ช่วยเอมิจริง ๆ"

# n "I don't even know what with or if there's anything at all she needs help for."
n "ฉันไม่รู้ด้วยซ้ำว่าเอมิจะมีเรื่องอะไรให้ฉันช่วยได้หรือเปล่า"

# n "But I want to."
n "แต่ฉันอยากช่วย"

$ renpy.music.set_volume(1.0, 2.0, channel="music")

play sound sfx_doorknock

stop music fadeout 2.0

nvl clear
nvl hide dissolve

window show

# "Suddenly, a knock at my door rouses me."
"อยู่ ๆ ก็มีเสียงเคาะประตูดังแทรกขึ้นมา"

play sound sfx_dooropen

scene bg school_dormhallway
show kenji neutral at center
with locationchange

# "I open it to see Kenji."
"พอไปเปิดดูก็เห็นว่าเป็นเคนจิ"

# hi "Oh, it's you."
hi "อ้อ นายนี่เอง"

play music music_kenji

show kenji tsun
with charachange

# ke "It's me? That's it?"
ke "ฉันนี่เอง? แค่เนี้ย?"

# ke "If you had any idea what I'd been through, what I'd done, you'd be happier to see me, dude."
ke "ถ้านายรู้ว่าฉันต้องผ่านอะไรมาบ้างและทำอะไรมาบ้างนายคงดีใจกว่านี้ที่ได้เจอฉันนะพวก"

# ke "I mean that was some epic, you-may-never-see-me-again shit."
ke "ก็แบบ เป็นเรื่องสุดยิ่งใหญ่ แบบ นายอาจจะไม่ได้พบกับฉันอีกเลย น่ะ"

# ke "And here you're just acting like I went down to the store for some milk."
ke "แต่นายก็ทำเหมือนฉันแค่ออกไปซื้อนมที่ร้านค้าหรืออะไรงั้นแหละ"

show kenji happy
with charachange

# ke "You're a cold man, Hisao. I really respect that."
ke "นายนี่เย็นชานะฮิซาโอะ ฉันละนับถือเลย"

# hi "Uh, thanks, I guess."
hi "เอ่อ ขอบคุณ ละมั้งนะ"

show kenji neutral
with charachange

# ke "It's smart to play it safe, you know. Don't show any emotion."
ke "นิ่ง ๆ ไว้น่ะดีที่สุด ห้ามแสดงอารมณ์ใด ๆ"

# ke "Keep your cards close to your chest."
ke "ถือไพ่ไว้ให้ใกล้ตัว"

# ke "Unless it's time to show your cards, or you have bad cards."
ke "เว้นเสียแต่ว่าจะมีไพ่ไม่ดีหรือถึงเวลาหงายไพ่"

# ke "Then you should fold or collect your winnings."
ke "ถึงตอนนั้นแล้วก็ให้หมอบหรือกวาดเดิมพันมาให้หมด"

show kenji happy
with charachange

# ke "Do you understand?"
ke "เข้าใจมั้ย"

# hi "Yeah, that makes perfect sense."
hi "อืม เข้าใจมาก ๆ"

# hi "I take it the uh, mission went well?"
hi "แบบนี้ก็แสดงว่า เอ่อ ภารกิจลุล่วงด้วยดีงั้นสิ"

show kenji tsun
with charachange

# ke "Woah, awfully nosy of you, isn't it?"
ke "โห สอดรู้นะนายเนี่ย"

# ke "You can't just go saying things like that! Things are at a delicate stage!"
ke "พูดอะไรอย่างนั้นออกมาดืื้อ ๆ เลยได้ไง! สถานการณ์ตอนนี้ยังอ่อนไหวอยู่นะ!"

# ke "One wrong move, and BAM! The invasion succeeds!"
ke "ขืนก้าวพลาดสักก้าวแล้วละก็ตู้ม! ภารกิจแทรกซึมสำเร็จ!"

# hi "I thought you were going to blow the conspiracy wide open?"
hi "ไหนนายบอกว่าจะเปิดโปงไอ้ทฤษฎีสมคบคิดนี่ไง"

# ke "It's bigger than I thought; I need to update my charts."
ke "พอดีเรื่องมันใหญ่กว่าที่คิดน่ะ ฉันต้องไปอัปเดตผังสักหน่อย"

# ke "And probably change some of the puppets around."
ke "แล้วก็ต้องสลับสับเปลี่ยนหุ่นเชิดบางตัวด้วย"

show kenji happy
with charachange

# ke "You wanna help? I've got some whiskey from… somewhere."
ke "สนใจมาช่วยมั้ย ฉันมีวิสกี้ที่… ได้มาจากสักที่ด้วย"

# ke "You can fill me in on everything your investigation has turned up."
ke "นายได้ความอะไรมาบ้างก็จะได้มาบอกฉันด้วยไง"

# hi "Er, better not. I'm uh… supposed to meet her today."
hi "เอ้อ ไม่เอาดีกว่า ฉัน เอ่อ… ต้องไปเจอกับเอมิวันนี้"

# hi "Gotta go do that. Can't raise suspicion."
hi "จำเป็นต้องเจอจริง ๆ จะให้เอมิสงสัยไม่ได้"

show kenji neutral
with charachange

# "Kenji nods in approval."
"เคนจิพยักหน้าเห็นด้วย"

# ke "Still keeping it close to the chest, eh? Okay man, I respect that."
ke "แต่ก็ถือไพ่ไว้ให้ใกล้ตัวล่ะ โอเค นับถือนายเลย"

# ke "Good luck."
ke "ขอให้โชคดี"

# hi "Er, thanks."
hi "เอ่อ ขอบคุณ"

hide kenji
with charaexit

stop music fadeout 4.0

# "I'm just going to pretend, for the sake of my own sanity, that he's wishing me luck in talking to Emi."
"ฉันจะจินตนาการเอาเองเพื่อไม่ให้ตัวเองเป็นบ้าไปก่อนว่าเคนจิอวยพรให้การคุยกับเอมิของฉันราบรื่น"

# "And if I squint, that whole card analogy he was talking about works here."
"หรือถ้าโยง ๆ สักหน่อย เรื่องไพ่ที่เคนจิพูดถึงนี่ก็เปรียบเหมือนได้อยู่"

# "Time to lay it all on the table."
"ถึงเวลาหงายไพ่แล้ว"

# "Or see if I can't get Emi to do so, rather."
"หรือมองว่าฉันจะทำให้เอมิหงายไพ่ได้บ้างหรือเปล่า"

# "With a sense of something approaching purpose, I head for Emi's room."
"ฉันไปที่ห้องเอมิด้วยความรู้สึกสักอย่างที่ละม้ายคล้ายจุดมุ่งหมาย"

scene bg school_girlsdormhall
with locationskip

play sound sfx_doorknock2

# "I hop up the stairs leading to her room and knock on her door."
"ฉันเดินขึ้นบันไดมาแล้วเคาะประตูห้องเอมิ"

# emi "W-who's there?"
emi "คะ ใครน่ะ"

play music music_drama fadein 8.0

# "Huh. That's odd. Her voice sounds a little choked."
"หือ แปลก เสียงฟังดูสะอื้นอยู่หน่อย ๆ"

# hi "Hey, it's me. Thought I'd stop by."
hi "ไง ฉันเอง พอดีจะแวะมาหาเธอหน่อย"

# emi "Hisao?"
emi "ฮิซาโอะ?"

# emi "Come on in!"
emi "เข้ามาเลย!"

# "I reach down to open the door, only to find that it's locked."
"ฉันยื่นมือไปจับหมายจะเปิดประตู แต่พอลองบิดดูก็รู้ว่าล็อกไว้"

# "More and more curious."
"ฉันยิ่งนึกสงสัยขึ้นไปอีก"

# hi "Er, your door's locked."
hi "เอ่อ ประตูเธอมันล็อกอยุ่"

# emi "Oh yeah, sorry. Gimme a minute."
emi "อ้อ จริงด้วย ขอโทษที แป๊บนะ"

show emi basic_grin:
    tworight
    xpos 0.8
    easein 0.5 tworight
with charaenter

# "In a few minutes, Emi opens the door, grinning."
"ผ่านไปไม่กี่นาทีเอมิก็มาเปิดประตูพร้อมส่งยิ้ม"

# emi "Sorry, I had to put my legs on. I was napping."
emi "ขอโทษที พอดีต้องใส่ขาน่ะ เมื่อกี้งีบอยู่"

# "Despite her grin, there's something definitely off."
"ถึงจะยิ้ม แต่มีบางอย่างแปลกไป"

# "Emi's eyes are slightly red, and it looks like she's been crying."
"ตาเอมิแดง ๆ เหมือนเพิ่งร้องไห้มา"

# hi "Hey, no problem."
hi "น่า เรื่องแค่นี้"

# hi "Er, are you okay?"
hi "เอ่อ เธอไม่เป็นอะไรใช่มั้ย"

show emi sad_shy at tworight
with charachange

# emi "Huh? Yeah, I'm fine!"
emi "หืม อื้ม ก็สบายดี!"

# hi "It's just that you look like you've been crying…"
hi "แค่เห็นเธอเหมือนเพิ่งร้องไห้มาน่ะ…"

# "Oh yeah, Hisao. You're off to a great start on this one."
"แบบนี้สิไอ้ฮิซาโอะ เปิดได้สวย"

show emi sad_grin at tworight
with charachange

# emi "What? Nah, I'm fine. I'm just happy to see you."
emi "อะไรนะ ไม่นี่ ก็สบายดี แค่ดีใจที่ได้เจอนายเฉย ๆ"

scene ev emi_firstkiss
with flash

# "She punctuates this with a long kiss that continues as the door slams shut behind us."
"เอมิประกบประโยคนี้ด้วยการจูบเนิ่นนานที่กินเวลาไปเรื่อย ๆ แม้จะปิดประตูเข้ามาในห้องกันแล้ว"

# "I know what she wants to do now, and I'm also painfully aware of how badly I want to do it too, but…"
"ฉันรู้ว่าตอนนี้เอมิอยากทำอะไร และฉันก็รู้ดีเหลือเกินว่าฉันเองก็อยากทำมาก ๆ แต่ว่า…"

scene bg school_dormemi at left
show emi excited_amused_close at center
with locationchange

# "I break the kiss with a wrench of self control that nearly kills me."
"ฉันบังคับตัวเองจนแทบบ้ากว่าจะผละจูบออกมาได้"

# hi "Hey, wait."
hi "นี่ เดี๋ยวก่อน"

show emi basic_confused_close
with charachange

# "Emi's eyes crinkle in confusion."
"เอมิทำหน้าย่นด้วยความสับสน"

# emi "Huh? Wait for what?"
emi "ฮะ? รออะไร"

# hi "We need to talk."
hi "เรามีเรื่องต้องคุยกัน"

show emi sad_grin_close
with charachange

# emi "Isn't that supposed to be my line?"
emi "อันนั้นมันคำพูดของฉันไม่ใช่เหรอ"

show emi sad_shy_close
with charachange

# emi "And never a good thing to say?"
emi "อีกอย่าง ถ้าจั่วหัวมาแบบนี้ก็แปลว่าไม่ใช่เรื่องดีสินะ"

# "She's got a point."
"ก็ถูกของเอมิ"

# "It's usually the lead-in to a breakup."
"เป็นคำพูดที่เกริ่นมาก่อนจะบอกเลิกกัน"

# "Or the prelude to a fight."
"หรือไม่ก็เป็นบทพูดนำก่อนจะทะเลาะกัน"

# hi "Maybe it can be a good thing this time."
hi "คราวนี้อาจจะเป็นเรื่องดีก็ได้"

# hi "Er, that's the hope, anyway."
hi "เอ่อ ฉันหวังว่ามันจะดีอะนะ"

show emi sad_shyblush_close
with charachange

# emi "Uh… huh."
emi "อ่า… ฮะ"

show emi basic_grin_close
with charachange

# emi "Can we at least get onto the bed? It's my first day back on these things, and I'm still readjusting."
emi "งั้นไปนั่งที่เตียงกันก่อนได้ไหม ฉันเพิ่งกลับมาใส่ขาเทียมวันนี้เป็นวันแรกเลยยังไม่ค่อยชินเท่าไหร่"

show emi basic_closedgrin_close
with charachange

# emi "Plus the nurse said I should try to be on them less often, since running puts such a strain on them."
emi "อีกอย่าง คุณพยาบาลก็บอกด้วยว่าห้ามใส่ขาเทียมบ่อย เพราะใช้งานตอนวิ่งไปเยอะแล้ว"

# hi "Can't argue with that."
hi "ก็เถียงไม่ได้"

# "It's a trap, we both know it, and we both don't care."
"เป็นกับดัก เราต่างรู้ดี และเราต่างก็ไม่สนใจ"

# "Then again, it's awfully hard to get angry while in bed with the object of your affections, so maybe there's that motivation too."
"แต่ก็นะ พอได้มานั่งอยู่บนเตียงกับคนที่ตัวเองหลงรักแล้วก็โกรธไม่ค่อยลง อาจจะเพราะอย่างนี้ด้วยถึงได้ไม่สนใจ"

hide emi
with charaexit

show bg school_dormemi at right
with charamove

show emi basic_grin_close:
    center
    ypos 1.0
    easein 0.5 ypos 1.1
with charaenter

# "I set Emi's legs by the bedside and sit down next to her, throwing an arm around her shoulders."
"ฉันวางขาเทียมเอมิไว้ข้างเตียงแล้วมานั่งข้าง ๆ โอบไหล่เธอเอาไว้"

# "In silence, we just enjoy being able to be in this position again for a few minutes."
"เราเพียงปล่อยให้ตัวเองยินดีที่ได้อยู่ด้วยกันในท่านี้เงียบ ๆ อยู่สองสามนาที"

# "Then, of course, I need to ruin it by opening my mouth."
"จากนั้นก็แน่นอนว่าฉันต้องเปิดปากทำลายบรรยากาศนี้ลง"

# hi "Look, I know that… that you've been having kind of a rough time of it lately."
hi "นี่นะ ฉันรู้… ว่าช่วงนี้เธอมีเรื่องลำบากใจอยู่"

# hi "And I want to help you out."
hi "แล้วฉันก็อยากช่วยเธอด้วย"

# hi "I thought it was just exams getting to you, but now I come to your room and you've been crying, and that kills me."
hi "ทีแรกก็คิดว่าคงเพราะเรื่องสอบเฉย ๆ แต่พอมาหาเธอที่ห้องแล้วเห็นเธอร้องไห้เนี่ยฉันใจสลายเลยนะ"

# hi "But I can't do anything if you won't talk to me about it."
hi "แต่ฉันก็ทำอะไรไม่ได้เพราะเธอไม่ยอมคุยกับฉัน"

show emi basic_closedgrin_close:
     ypos 1.1
with charachange

# emi "I told you, I'm fine."
emi "ก็บอกแล้วไงว่าไม่เป็นไร"

# hi "No, you aren't. It's obvious something's eating at you."
hi "เป็น เป็นสิ ก็เห็น ๆ อยู่ว่ามีเรื่องกวนใจเธอน่ะ"

# hi "You can tell me, you know."
hi "คือเธอจะเล่าให้ฉันฟังก็ได้"

# "There's the slightest increase in tension in Emi's voice."
"น้ำเสียงเอมิฟังดูเครียดขึ้นมาเสี้ยวหนึ่ง"

show emi sad_shy_close
with charachange

# emi "Why is my saying I'm fine not good enough?"
emi "แล้วแค่ฉันบอกว่าไม่เป็นไรนี่มันไม่พอหรือไง"

show emi sad_annoyed_close
with charachange

# emi "You're concerned, I get that. That's cool."
emi "นายเป็นห่วง ฉันรู้ ซึ่งก็ดีแล้ว"

# emi "But I'm fine, and it's nothing that you need to worry about."
emi "แต่ฉันก็ไม่เป็นไร แล้วก็ไม่ใช่เรื่องที่นายจำเป็นจะต้องมาคิดมากด้วย"

# hi "Not sleeping and spacing out more than Rin doesn't strike me as “being fine.”"
hi "ฉันว่าการที่นอนไม่พอแล้วเหม่อบ่อยกว่ารินนี่นับว่า “ไม่เป็นไร” ไม่ได้นะ"

# hi "I just… I want to help."
hi "ฉันแค่… อยากช่วยเธอ"

# emi "Uh-huh."
emi "อ่าฮะ"

# hi "Yeah, I don't like seeing you like this."
hi "อืม ก็ไม่อยากเห็นเธอเป็นแบบนี้นั่นแหละ"

# hi "I want you to be happy, you know?"
hi "ฉันอยากให้เธอมีความสุขไง"

show emi basic_annoyed_close
with charachange

# "I get the feeling that came out wrong, because Emi fixes me with an icy stare."
"รู้สึกเหมือนพูดอะไรพลาดไปเพราะตอนนี้เอมิจ้องมองฉันด้วยสายตาเย็นชา"

# emi "So you want to fix me, Hisao?"
emi "ก็คือนายอยากแก้ปัญหาให้ฉันเหรอฮิซาโอะ"

# "She's definitely getting angry now."
"ตอนนี้เอมิโกรธแน่แล้ว"

show emi sad_grit_close
with charachange

# emi "Wanna swoop in on your white charger and save the day?"
emi "อยากจะเป็นพระเอกขี่ม้าขาวเข้ามาช่วยว่างั้น"

# emi "Stop the nightmares, the phantom limb pains?"
emi "ช่วยปัดเป่าฝันร้าย ปัดเป่าอาการปวดหลอนเหรอ"

show emi sad_angry_close
with charachange

# emi "Restore what's lost?"
emi "ช่วยกู้คืนสิ่งที่เสียไปแล้วเหรอ"

show emi sad_depressed_close
with charachange

# "Her voice catches in her throat, and the tears start to flow."
"ก้อนสะอื้นขึ้นมาจุกคอเอมิ น้ำตาเธอเริ่มไหล"

# emi "Well you {b}can't{/b}."
emi "เหอะ นายช่วย{b}ไม่ได้{/b}หรอก"

show emi sad_pout_close
with charachange

# emi "Nobody can."
emi "ไม่มีใครช่วยได้"

# emi "Nobody will."
emi "ไม่มีเลย"

# "I'm so stunned by her sudden verbal assault that I remain quiet."
"ฉันตะลึงงันกับคำพูดที่ไหลบ่าออกมาจากเอมิจนได้แต่นั่งอยู่เงียบ ๆ"

# "Neither of us says anything for a while."
"เราต่างไม่พูดอะไรกันอยู่พักหนึ่ง"

# "I'm surprised that Emi tightens her grip on me rather than pushing me away."
"ฉันนึกแปลกใจที่เอมิกำหมัดแน่นแทนที่จะผลักตัวฉันออก"

# "After a deep breath, she starts talking again."
"เอมิสูดหายใจลึกแล้วพูดขึ้นมาอีกรอบ"

show emi sad_shy_close
with charachange

# emi "Look, I'm sorry."
emi "โอเค ฉันขอโทษ"

show emi sad_depressed_close
with charachange

# emi "I just… there's these nightmares."
emi "คือฉัน… ฝันร้ายน่ะ"

# emi "About the accident."
emi "เรื่องอุบัติเหตุ"

# "Ah. The accident. I should've known."
"อ้อ อุบัติเหตุ น่าจะเดาได้แต่แรกแล้ว"

# "It took her legs, after all, but it never comes up, of course."
"ก็เป็นอุบัติเหตุที่ทำให้เอมิเสียขาไปนี่นะ แต่แน่นอนว่าเราไม่เคยคุยเรื่องนี้กันเลย"

show emi sad_pout_close
with charachange

# emi "And I usually deal with them fine, because I can run."
emi "และปกติฉันก็ไม่ต้องคิดมากเพราะฉันวิ่งได้"

# emi "Running clears my head like nothing else."
emi "การวิ่งน่ะคือยาที่ทำให้สมองปลอดโปร่งชั้นดีของฉันเลย"

# emi "I don't have to worry about anything while I'm running."
emi "ตอนวิ่งก็ไม่ต้องไปคิดอะไร"

# emi "I just concentrate on breathing, on the rhythm of things."
emi "แค่จดจ่ออยู่กับการหายใจ จดจ่ออยู่กับจังหวะของอะไร ๆ"

# emi "It's easier that way. Life's easier that way."
emi "แบบนั้นน่ะสบายกว่ากันเยอะ ใช้ชีวิตแบบนั้นแล้วสบายดี"

show emi sad_shy_close
with charachange

# emi "Just keep moving forwards, you know? Nothing else matters, just getting around the next curve."
emi "แบบ แค่เดินหน้าไปเรื่อย ๆ เรื่องอื่นไม่สำคัญแล้ว ขอแค่ผ่านโค้งถัดไปไปให้ได้ก็พอ"

# emi "And then it's the next curve, and the next, and the next, until I can't go any more, or think any more, or do anything but slow down and walk until I catch my breath again."
emi "แล้วก็จะมีโค้งถัดไปอีก โค้งถัด ๆ ไป โค้งถัด ๆ ๆ ไป จนฉันไปต่อไม่ไหว คิดไม่ไหว ทำอะไรไม่ไหว ถึงตอนนั้น\nฉันก็จะผ่อนฝีเท้าลงแล้วเดินพักให้หายใจได้เต็มปอดอีกรอบ"

# emi "After something like that, nothing else matters."
emi "พอทำอะไรแบบนั้นมาเรื่องอื่นก็จะไม่สำคัญแล้ว"

show emi basic_annoyed_close
with charachange

# emi "But I've been stuck in that goddamned wheelchair for too long. So, no outlet."
emi "แต่ฉันต้องนั่งติดเจ้าวีลแชร์บ้านั่นอยู่นานเกินไป ก็เลยไม่มีที่ระบาย"

show emi sad_shy_close
with charachange

# emi "Today it just kinda boiled over a little."
emi "แล้ววันนี้อารมณ์มันก็ปะทุออกมาหน่อย ๆ"

# hi "You could have talked to me about it, you know."
hi "เธอจะมาคุยกับฉันก็ได้นี่"

# hi "You didn't have to go it alone."
hi "ไม่เห็นต้องอยู่ตัวคนเดียวเลย"

show emi sad_grin_close
with charachange

# "Emi smiles sadly, like she's trying to explain to a child that all fire burns."
"เอมิยิ้มเศร้า ๆ เหมือนต้องอธิบายให้เด็กฟังว่าไฟมันร้อน"

# emi "Yeah, I did. And I do."
emi "อืม ตอนนั้นฉันอยู่ตัวคนเดียว ตอนนี้ก็ด้วย"

# hi "But why?"
hi "แต่ทำไมล่ะ"

# hi "Why do you have to keep going through this alone?"
hi "ทำไมเธอถึงเอาแต่จัดการกับเรื่องพวกนี้อยู่ตัวคนเดียว"

# hi "Why can't you just trust me enough to let me help you?"
hi "ทำไมเธอถึงไม่เชื่อใจให้ฉันช่วยเธอบ้าง"

# "That smile again."
"รอยยิ้มนั้นอีกแล้ว"

show emi excited_amused_close
with charachange

show emi sad_grin_close
with charachange

# "Emi leans in and kisses me on my cheek, an almost motherly gesture."
"เอมิโน้มตัวเข้ามาหอมแก้มฉันคล้ายตอนที่แม่หอมแก้มลูก"

# "She leaves her mouth close to my ear, as she confesses this one thing to me."
"เธอไม่ผละริมฝีปากไปจากหูฉันก่อนจะสารภาพเรื่องนี้ให้ฉันฟัง"

show emi sad_shy_close
with charachange

# emi "Because, Hisao."
emi "เพราะว่านะฮิซาโอะ"

# emi "I've already had everything I knew ripped away from me once."
emi "ฉันเคยเสียทุกอย่างที่ฉันเคยมีไปแล้วครั้งหนึ่ง"

show emi sad_depressed_close
with charachange

# emi "I don't know what I'd do if it happened again."
emi "และฉันก็ไม่รู้ว่าถ้าต้องเสียไปอีกรอบฉันจะต้องทำยังไงดี"

# "She pauses, as if uncertain as to whether or not she should continue."
"เอมิเว้นช่วงไปเหมือนไม่แน่ใจว่าจะพูดต่อดีหรือเปล่า"

# "I can feel a violent churning in my gut."
"ฉันมวนท้องไปหมด"

# "She continues."
"เอมิพูดต่อ"

show emi sad_shy_close
with charachange

# emi "So I can't rely on you."
emi "เพราะงั้นฉันถึงเชื่อใจเธอไม่ได้"

# emi "Or the nurse."
emi "เชื่อใจคุณพยาบาลไม่ได้"

# emi "Or anyone else."
emi "เชื่อใจใครไม่ได้เลย"

show emi sad_pout_close
with charachange

# emi "Just me."
emi "มีแค่ฉัน"

# emi "That's how it's got to be."
emi "ไม่มีวันเปลี่ยน"

# "Having delivered this short speech, she looks down and covers her mouth with the back of her hand."
"พอพูดประโยคสั้น ๆ เหล่านั้นแล้วเอมิก็ก้มหน้ายกหลังมือขึ้นมาปิดปากไว้"

# "The conversation is clearly over. I search for something to say, but can't think of anything."
"ชัดเจนว่าบทสนทนานี้จบลงแล้ว ฉันนึกหาคำจะพูดแต่ก็นึกไม่ออก"

# hi "I…"
hi "ฉัน…"

# hi "Maybe I should go, for now."
hi "ฉันว่าฉันไปก่อนดีกว่า"

# hi "I've got… stuff."
hi "ฉันมี… เรื่องที่ต้องทำ"

# "Emi doesn't even look up."
"เอมิไม่แม้แต่จะเงยหน้ามอง"

# "She sounds tired, or relieved."
"น้ำเสียงเธอฟังดูเพลีย หรือไม่ก็โล่งใจ"

# "I can't tell which."
"ฉันเดาไม่ถูก"

# emi "Okay, Hisao."
emi "โอเค ฮิซาโอะ"

# emi "Go take care of that stuff."
emi "ไปจัดการกับเรื่องนั้นซะนะ"

# emi "I'll see you tomorrow."
emi "เดี๋ยวพรุ่งนี้เจอกัน"

hide emi
with charaexit

with Pause(0.2)

show bg school_dormemi at left
with charamove

# "I get off the bed and head for the door, pausing at the doorway."
"ฉันลุกขึ้นจากเตียงเดินออกไปก่อนจะหยุดยืนอยู่ตรงหน้าประตู"

# hi "Hey, Emi…"
hi "นี่ เอมิ…"

show emi sad_shy at tworight
with charaenter

# emi "Yeah?"
emi "ว่า"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

# n "\n\nA thousand things I want to say."
n "\n\nคำพูดร้อยพันที่ฉันอยากพูด"

# n "I'm too mixed up to say any of them, though."
n "แต่ก็คละเคล้ากันไปหมดจนไม่รู้จะพูดอะไร"

# n "After her admitting that she'll never let me close, I feel like {b}my{/b} world's just been ripped out from me."
n "พอเอมิยอมรับแล้วว่าจะไม่มีวันให้ใครได้เข้าใกล้ชิดแล้วฉันก็รู้สึกเหมือนโลก{b}ตัวเอง{/b}ถูกพรากไปทั้งใบ"

# n "What happened in that accident?"
n "เกิดอะไรขึ้นตอนอุบัติเหตุครั้งนั้น"

# n "I know she lost her legs, but that's never seemed to bother her."
n "ฉันรู้ว่าเอมิเสียขาไป แต่เธอก็ดูจะไม่เคยคิดมากเรื่องนี้เลย"

# n "What happened there?"
n "เกิดอะไรขึ้นกันแน่"

# n "What scares a girl so badly that she won't accept help, even from someone she loves?"
n "อะไรที่ทำให้เด็กสาวคนหนึ่งหวาดกลัวเสียจนไม่กล้ายอมรับความช่วยเหลือจากใคร แม้คนนั้นจะเป็นคนที่เธอรักก็ตาม"

# n "I don't know."
n "ฉันไม่รู้เลย"

# n "\nBut I want to know."
n "\nแต่ฉันอยากรู้"

# n "I want to know so badly that being denied that answer feels like a knife in my guts."
n "อยากรู้มากเสียจนการที่ไม่ได้คำตอบนั้นเจ็บปวดเหมือนมีมีดคมเฉือนตัวฉัน"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve
window show

# emi "Hisao?"
emi "ฮิซาโอะ?"

# emi "You were saying?"
emi "เมื่อกี้พูดอะไรหรือเปล่า"

# "I'm still standing in the doorway."
"ตอนนี้ฉันยังยืนอยู่ที่ประตู"

# hi "…Nothing."
hi "…เปล่า"

# hi "Never mind."
hi "ช่างเถอะ"

scene bg school_girlsdormhall
with locationchange

play sound sfx_doorclose
stop music fadeout 6.0

# "And I'm closing the door."
"แล้วฉันก็ปิดประตู"

# "And walking down the hallway."
"เดินมาตามโถงทางเดิน"

# "Down the stairs."
"ลงบันไดมา"

scene bg school_dormext_full_ni
with locationskip

# "Out the door."
"ออกประตู"

# "Into the dark."
"ไปสู่ความมืดมิด"

scene bg school_dormhisao_ni
with locationskip

play music music_night fadein 1.0

# "Somehow I wander back to my own room. My brains are doing a mile a minute, going nowhere fast."
"อยู่ ๆ ก็กลับมาถึงห้องตัวเองได้ สมองฉันแล่นด้วยความเร็วเต็มพิกัดไปโดยไม่มีจุดมุ่งหมายใด ๆ"

window hide
nvl clear
nvl show dissolve

# n "\n\nI can't figure out how to deal with this."
n "\n\nฉันไม่รู้จะรับมือกับเรื่องนี้ยังไงดี"

# n "I thought that moving forward was a good thing."
n "ฉันเคยคิดว่าการเดินหน้าต่อไปนั้นเป็นเรื่องที่ดี"

# n "Dwelling less on a past that I can't change. Living in the present and looking at the future."
n "เลิกจมอยู่กับอดีตที่ย้อนกลับไปแก้ไขไม่ได้ อยู่กับปัจจุบันแล้วมองไปยังอนาคต"

# n "\n\nAfter this… thing with Emi, I'm not sure any more."
n "\n\nแต่พอ… มีเรื่องเอมิแล้วฉันก็ชักไม่แน่ใจ"

# n "She was saying the truth. It's simpler to look at the next curve, ignoring the path gone by."
n "เอมิพูดความจริง มองแค่โค้งหน้านั้นจะสบายกว่า ไม่ต้องสนใจเส้นทางที่ผ่านมา"

# n "No worry about the opponent left behind. No care for the spectators on the sidelines."
n "ไม่ต้องกังวลเรื่องโอกาสที่เสียไป ไม่ต้องสนใจผู้ชมข้างสนาม"

# n "And unfortunately, no time to watch out for lagging teammates either."
n "และน่าเสียดายที่จะไม่มีเวลามองเพื่อนร่วมทีมที่ช้ากว่าด้วย"

nvl clear
nvl hide dissolve
window show

# "I throw myself down on the bed, looking at one corner of my ceiling as if the answers I want were written there."
"ฉันทิ้งตัวเองลงนอนกับเตียงมองเพดานตรงมุมหนึ่งราวกับว่ามีคำตอบที่ฉันต้องการเขียนไว้ตรงนั้น"

# "No such luck, of course."
"แน่ละว่าไม่มี"

window hide
nvl clear
nvl show dissolve

# n "\n\n\n\n\nShe's literally running away from something - but have I not been doing the same thing, trying my best to forget about my hospitalization?"
n "\n\n\n\n\nเอมิ{i}วิ่ง{/i}หนีจากอะไรบางอย่างอยู่ แต่ฉันก็ทำเหมือนกันนี่ เพราะฉันเองก็พยายามลืมเรื่องที่ต้องนอนอยู่โรงพยาบาล\nเหมือนกัน"

# n "I am getting better, but my health isn't going to magically fix itself."
n "ฉันอาการดีขึ้นแล้ว แต่สุขภาพของฉันจะไม่ได้กลับมาแข็งแรงดีในชั่วพริบตาแน่นอน"

# n "\nEmi has two legs instead of a heart to deal with, but those aren't going to magically fix themselves either."
n "\nที่เอมิต้องรับมือเหมือนฉันที่ต้องรับมือกับเรื่องหัวใจคือเรื่องขาทั้งสองข้าง แต่ขาทั้งสองข้างของเธอ\nก็จะไม่ได้กลับมาเป็นปกติในชั่วพริบตาแน่นอนเหมือนกัน"

# n "\nMaybe this is just as fixed as the both of us can get."
n "\nหรือ ณ ตอนนี้เราทั้งสองคนต่างก็อาจอยู่ในจุดที่แก้ไขปัญหาตัวเองได้เต็มที่แล้ว"

nvl clear
nvl hide dissolve
window show

# "The room becomes darker and darker, until I can't really tell I'm looking at a corner any more."
"ภายในห้องมืดลงเรื่อย ๆ จนฉันไม่เห็นแล้วว่ากำลังมองมุมบนเพดานอยู่"

#####################

label th_E25:

scene bg school_dormhisao
with shorttimeskip

# "The morning comes too soon, on the heels of a sleepless night."
"ไม่ทันไรก็เช้าแล้ว เมื่อคืนนอนไม่หลับเลย"

# "Is this how Emi's been spending her nights?"
"เอมิจะเป็นแบบนี้เหมือนกันหรือเปล่า"

# "Staring at the wall, or ceiling. Trying to stop thinking about whatever it is."
"มองผนังหรือเพดานห้ามใจไม่ให้คิดเรื่องอะไรสักอย่าง"

# "Her, in my case."
"กับฉันก็เป็นเรื่องของเอมิ"

# "That clenched feeling in my gut is still there."
"ในใจยังรู้สึกหน่วงไม่ยอมหาย"

window hide
nvl clear
nvl show dissolve

# n "\n\n“I can't rely on you.”"
n "\n\n“ฉันถึงเชื่อใจเธอไม่ได้”"

# n "\nWords spoken so casually."
n "\nพูดออกมาได้"

# n "Almost like she were teasing me, or chastising me for suggesting that the Earth is flat."
n "เหมือนหยอกเล่นเฉย ๆ เหมือนสอนเพราะฉันบอกว่าโลกแบน"

# n "\n“That's how it's got to be.”"
n "\n“ไม่มีวันเปลี่ยน”"

# n "\nThe way it's got to be sucks."
n "\nจะไม่เปลี่ยนเลยก็คงแย่มาก"

# n "I'm feeling so miserable that I very nearly decide to skip the run."
n "จิตใจฉันอ่อนเปลี้ยจนทีแรกคิดจะไม่ไปวิ่งแล้ว"

# n "That would be stupid, though. It's not something I should do just to see her."
n "แต่ก็คงงี่เง่าเกินไป ฉันไม่ควรคิดว่าการได้เจอเอมิเป็นเป้าหมายเดียวที่ต้องไปวิ่ง"

# n "Sure, that was the original reason, but it's something more now."
n "แน่ละว่าทีแรกที่ไปวิ่งก็เพราะแบบนั้น แต่ตอนนี้มีเหตุผลอื่นแล้ว"

nvl clear

# n "\n\n\n\nI've started to enjoy the running itself."
n "\n\n\n\nฉันเริ่มชอบการวิ่งขึ้นมาบ้าง"

# n "There are worse ways to get the blood flowing, anyway."
n "เพราะยังไงก็คงเป็นการออกกำลังกายให้เลือดลมเดินที่ดีใช้ได้แล้ว"

# n "Never thought I'd say it after that first week or so, but—"
n "ฉันไม่เคยคิดเลยว่าจะได้พูดแบบนี้หลังจากที่ผ่านประสบการณ์ช่วงที่วิ่งสัปดาห์แรก ๆ แต่ว่า—"

# n "\nI feel a lot better after a run, like no matter what else I do today, I've at least done that one thing."
n "\nพอวิ่งแล้วฉันก็รู้สึกดีขึ้นมาก เหมือนว่าต่อให้วันนี้จะไปทำอะไร อย่างน้อยก็ต้องมาวิ่งก่อน"

# n "It wakes me up, too, and Emi herself said that running always clears her mind. Maybe it'll help clear mine."
n "พอวิ่งแล้วก็ตื่นเต็มตาขึ้น เอมิก็เคยพูดด้วยว่าพอวิ่งแล้วสมองก็ปลอดโปร่ง ไม่แน่ว่าพอฉันวิ่งแล้วสมองฉันอาจจะ\nปลอดโปร่งบ้างก็ได้"

# n "\nI hope so."
n "\nหวังว่านะ"

nvl clear
nvl hide dissolve

scene bg school_track
with locationskip

window show

# "The morning is cool and clear, if a bit humid. Summer's making itself known, it seems."
"อากาศเช้าวันนี้เย็นสบาย เหมือนจะชื้น ๆ เล็กน้อย คงจะเป็นเพราะหน้าร้อนนั่นแหละ"

# "Emi's already stretching out when I arrive, and greets me with a smile and a wave."
"พอมาถึงเอมิก็ยืดเส้นยืดสายอยู่ก่อนแล้ว เธอยิ้มทักทายโบกมือให้"

show emi basic_closedgrin_gym at center
with charaenter

# emi "Hey, Hisao!"
emi "ไง ฮิซาโอะ!"

# "The sight of her so chipper is like a kick in the nuts."
"ฉันจุกขึ้นมาทันทีเมื่อได้เห็นเอมิที่ทำตัวสดใส"

# "How can she be so happy after yesterday?"
"ทั้งที่เมื่อวานบรรยากาศเครียดขนาดนั้น ยังมีความสุขอยู่ได้ยังไง"

show emi excited_amused_gym_close
with characlose

# "I give a half wave and am surprised to receive a hug."
"ฉันยกมือขึ้นมาแค่ครึ่งทางแล้วโบกมือให้ก่อนจะตกใจเมื่อเอมิเข้ามากอด"

show emi sad_shy_gym_close
with charachange

# emi "Hey, about last night."
emi "นี่ เรื่องเมื่อคืนน่ะ"

# "Here it comes."
"เอาแล้วไง"

stop music fadeout 1.0

show emi basic_grin_gym_close
with charachange

# emi "I wanted to say thanks."
emi "ฉันอยากจะขอบคุณนาย"

show emi excited_happy_gym_close
with charachange

# emi "I actually managed to get some sleep for the first time in a while, and I think it's because of our talk."
emi "คือฉันนอนไม่ค่อยหลับมาสักพักแล้ว แต่เมื่อคืนฉันได้หลับสนิทจริง ๆ คงเพราะที่เราคุยกันนั่นแหละ"

show emi basic_closedgrin_gym_close
with charachange

# emi "So, thanks."
emi "เพราะงั้น ขอบคุณนะ"

play music music_rain fadein 4.0

# "How could she sleep better after our chat?"
"คุยกันไปขนาดนั้นแล้วหลับลงได้ยังไง"

# "She basically told me that she wouldn't get any closer to me."
"ก็เธอบอกฉันเลยว่าจะไม่สนิทกับฉันไปมากกว่านี้แล้ว"

# "And that let her sleep well?"
"ซึ่งพอบอกแบบนั้นแล้วก็หลับสบายขึ้น?"

# "Excuse me, but what the hell?"
"ขอประทานโทษนะ แต่เชี่ยอะไรเนี่ย"

# "Emi either doesn't notice my bafflement or chooses not to notice."
"เอมิไม่ทันสังเกตว่าฉันตกตะลึงไป หรือไม่ก็จงใจไม่มอง"

# "No telling with her any more."
"ฉันเดาใจเธอไม่ถูกแล้ว"

# hi "Oh, no problem. Glad it helped."
hi "อ้อ ไม่เป็นไร คุยแล้วหลับสบายก็ดีแล้ว"

# "The venom that threatens to drip into my voice is controlled for now, but I think I'd better start running now, before I do anything stupid."
"ฉันยั้งตัวเองไว้ไม่ให้โทสะแทรกเข้ามาในคำพูด แต่รีบ ๆ ไปวิ่งก่อนดีกว่า ก่อนที่ฉันจะทำอะไรโง่ ๆ ลงไป"

scene bg school_track_on
with locationchange

# "Emi seems equally willing to get started, and before long we're darting around the track."
"เอมิก็ดูอยากจะออกวิ่งพอกัน ไม่นานเราก็เคลื่อนตัวไปตามลู่วิ่ง"

# "I can tell she feels more relaxed."
"ฉันดูออกว่าเอมิผ่อนคลายลงแล้ว"

scene ev emi_run_face:
    truecenter
    zoom 1.0 subpixel True
    acdc_warp 20.0 zoom 1.1
with flash

# "Her running has gone back to the more graceful movements I remember from when I first watched her."
"ท่าวิ่งของเอมิกลับมาสง่าเหมือนอย่างที่ฉันเคยเห็นเป็นครั้งแรกแล้ว"

# "It's a stark contrast to the almost brutal way she's been hurling herself around the track these past few days."
"ซึ่งต่างจากท่าทีที่เอมิรีบร้อนเคลื่อนตัวไปตามลู่วิ่งช่วงสองสามวันที่ผ่านมาอย่างเห็นได้ชัด"

# "Our talk really does seem to have helped her."
"ดูท่าว่าเอมิจะรู้สึกดีขึ้นได้เพราะเราคุยกันจริง ๆ"

# "A pity it couldn't help me."
"น่าเสียดายที่ฉันไม่ได้รู้สึกดีขึ้นด้วย"

# "I get into the rhythm of the running, thinking back to when I couldn't afford thinking about anything else but keeping my breathing steady and legs moving."
"ฉันขยับฝีเท้าให้เป็นการวิ่งพลางคิดถึงเมื่อก่อนที่ตอนวิ่งจะคิดอะไรไม่ได้เลยนอกจากการรักษาจังหวะการหายใจ\nกับการขยับขาไปเรื่อย ๆ"

# "Guess those days are gone."
"คงไม่มีแบบนั้นอีกแล้วละ"

# "At least for the first couple of laps."
"อย่างน้อยก็ไปแบบนี้ได้ตอนสองรอบลู่แรก"

scene bg school_track_running
with Dissolve(2.0)

# "Annoyed at the lack of success I'm having with clearing my head, I increase the pace."
"ฉันหงุดหงิดที่สมองยังไม่ปลอดโปร่งสักทีจึงเร่งฝีเท้าขึ้น"

# "Ah, there's the burning sensation in my legs."
"อา ขาฉันเริ่มร้อน ๆ ขึ้นมาแล้ว"

# "The breaths coming ragged in my chest, the pounding of my heart. Which I still need to be careful about."
"ลมหายใจเริ่มกระชั้น หัวใจเต้นถี่ ซึ่งฉันยังต้องคอยระวังอยู่"

# "But it does seem to have gotten stronger; I can feel it pumping blood through my veins."
"แต่เหมือนจะแข็งแรงขึ้นแล้ว รู้สึกได้ถึงชีพจรที่เต้นอยู่ตามเส้นเลือดเลย"

# "The sound thrums in my ears, but instead of being panicked as I was that day in the snow, I'm instead filled with elation."
"เสียงชีพจรนั้นดังอยู่ในหู แต่ฉันไม่ได้ตระหนกเหมือนอย่างวันหิมะตกครั้งนั้นแล้ว ในใจฉันเปี่ยมไปด้วยความปิติสุข"

# "Yes, it's working! My heart, that fatal flaw that landed me here, has improved."
"นี่แหละ ได้ผลแล้ว! หัวใจที่เล่นงานฉันให้ล้มตึงนั้นพัฒนาขึ้นแล้ว"

# "I'm able to keep going now, and maybe one day I'll be able to stop worrying as much."
"ตอนนี้ฉันไปต่อได้ และสักวันฉันคงจะเลิกคิดมากเรื่องหัวใจได้สักที"

# "Right now, it doesn't matter that I have no idea what to do about Emi and me."
"ตอนนี้ ไม่ว่าฉันจะรู้หรือเปล่าว่าจะต้องทำยังไงกับเรื่องระหว่างเอมิกับฉันก็ไม่สำคัญแล้ว"

# "All that matters is that my arms and legs continue to pump in concert with one another."
"สิ่งสำคัญอย่างเดียวคือการที่แขนกับขาฉันขยับไปอย่างสอดประสานกัน"

# "Nothing else."
"เท่านั้น"

show bg school_track_on
with locationchange

# "As I hit the final stretch, I remind myself that running really does help, though not as much as I'd hoped."
"พอถึงช่วงโค้งสุดท้ายฉันก็เตือนใจตัวเองว่าการวิ่งนั้นช่วยได้จริง ๆ ถึงจะช่วยได้ไม่มากเท่าที่หวังไว้ก็ตาม"

# "I do feel better, and as I walk a few laps to cool down, I begin to remember last night in a slightly less emotional manner."
"ฉันรู้สึกดีขึ้นจริง ๆ และระหว่างที่เดินอีกสองสามรอบเป็นการคูลดาวน์ฉันก็เริ่มย้อนนึกถึงเหตุการณ์เมื่อคืน\nได้อย่างเป็นเหตุผลมากขึ้นเล็กน้อย"

# "Emi wants me to stay distant from her."
"เอมิอยากให้ฉันเว้นระยะกับเธอ"

# "I can't bring myself to do so."
"ซึ่งฉันทำไม่ได้"

# "There's got to be a way around this, some kind of middle ground I can reach."
"ต้องมีทางออกสิ จุดกึ่งกลางสักที่ที่ฉันพอทำได้"

# "Not sure what that middle ground is, though."
"แต่ฉันก็ไม่รู้ว่าจุดกึ่งกลางที่ว่านั้นคืออะไร"

# "Damn, I was almost feeling optimistic."
"แม่ง อุตส่าห์คิดบวกได้แล้วแท้ ๆ"

show emi excited_joy_gym at center
with charaenter

# emi "Nice run, Hisao! You've really improved!"
emi "วิ่งได้ดีนี่ฮิซาโอะ! นายพัฒนาขึ้นแล้วจริง ๆ !"

# "Nice run. That's all I can hope for now, isn't it?"
"วิ่งได้ดี ตอนนี้ก็หวังได้แค่นี้สินะ"

# "Congratulations, Hisao. You're pathetic."
"ยินดีด้วยนะไอ้ฮิซาโอะ เอ็งมันน่าสมเพช"

# "I gotta change my attitude."
"ต้องเปลี่ยนมุมมองเสียหน่อย"

# hi "Well, you know. I am pretty awesome."
hi "ก็นะ ฉันก็สุดยอดเหมือนกันนี่นา"

# "And yet I just keep saying things that I don't mean."
"แล้วฉันยังเอาแต่พูดอะไรที่ไม่ได้มาจากใจจริง"

# "Any second now I'll be as good at hiding my problems as Emi is."
"อีกเดี๋ยวเดียวฉันก็คงปิดบังปัญหาได้เก่งเหมือนเอมิแล้วมั้ง"

show emi basic_closedgrin_gym
with charachange

# emi "I like to think so."
emi "ฉันก็ว่างั้นแหละ"

# "Why does she do this to me? Say something like that with such real affection in her voice that it makes my heart leap?"
"ทำไมเอมิถึงทำแบบนี้กับฉัน พูดอะไรด้วยน้ำเสียงที่ใส่ความรักมาด้วยจนใจฉันเต้นไม่เป็นส่ำ"

# "She doesn't mean it. She can't."
"ไม่ใช่คำพูดที่มาจากใจจริงเอมิหรอก เอมิพูดแบบนั้นไม่ได้"

# "I must be doing a worse job than I thought, because Emi peers closely at me."
"เอมิเข้ามามองฉันใกล้ ๆ สภาพฉันคงแย่กว่าที่ฉันคิดไว้"

show emi basic_confused_gym
with charachange

# emi "Hey, you feeling okay?"
emi "นี่ ไหวหรือเปล่า"

show emi basic_hes_gym
with charachange

# emi "Maybe we should get to the nurse, huh?"
emi "ไปหาคุณพยาบาลกันดีกว่ามั้ย"

# hi "Yeah, I'd hate to keel over on you."
hi "อืม ฉันก็ไม่อยากเป็นลมล้มทับเธอหรอก"

# "Emi looks a little shocked at my bitter tone."
"เอมิเหมือนตกใจเล็กน้อยกับน้ำเสียงขื่น ๆ ของฉัน"

show emi basic_shock_gym
with charachange

# emi "Don't say things like that!"
emi "อย่าพูดอะไรแบบนั้นสิ!"

show emi sad_shy_gym
with charachange

# emi "You've already done it once before, you know."
emi "นายก็เคยล้มทับฉันมาแล้วนี่"

# "Why does she act so affectionate?"
"ทำไมถึงทำตัวสนิทสนมขนาดนี้"

# "She doesn't really care, I thought she made that clear."
"ก็พูดเองไม่ใช่เหรอว่าเธอไม่ได้สนใจกันจริง ๆ"

# "But despite all of that I find myself apologizing, even though I shouldn't have to. Even though she's probably just putting on an act."
"แต่ถึงอย่างนั้นฉันก็ขอโทษ ทั้งที่ไม่น่าใช่เรื่องต้องขอโทษด้วยซ้ำ ทั้งที่เอมิอาจจะแค่แสร้งทำทีไปงั้นเอง"

# hi "Sorry, heh."
hi "ขอโทษทีนะ ฮะ ๆ"

# hi "Come on, let's see the nurse."
hi "ปะ ไปหาคุณพยาบาลกัน"

# "I can't get myself to calm down the whole time."
"ฉันสงบใจตัวเองไม่ได้เลย"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

# n "\n\n\n\nEvery time it feels like I've gotten over what happened last night, Emi does something or says something that shows affection, and I'm back to the beginning."
n "\n\n\n\nพอฉันรู้สึกเหมือนจะเลิกคิดเรื่องเมื่อคืนได้แล้วทีไร เอมิก็ทำหรือพูดอะไรเป็นการแสดงความสนิทสนมออกมาทุกที\nแล้วฉันก็ต้องกลับมานับหนึ่งใหม่"

# n "The image of her ending that conversation haunts me."
n "ภาพเอมิที่ปิดบทสนทนาครั้งนั้นยังติดตรึง"

# n "It was like the final twist of the knife that left me feeling bereft of any hope that Emi and I could be more than what we are."
n "เหมือนคมมีดกรีดกลางใจดับฝันว่าเอมิกับฉันจะเป็นอะไรต่อกันได้มากกว่านี้"

# n "And what are we at this point? Little more than friends who happen to fuck."
n "แล้วตอนนี้เราเป็นอะไรกัน เป็นมากกว่าเพื่อนนิดหน่อยที่มีอะไรกันบ้างเป็นบางครั้ง"

# n "And really, it's not like I don't enjoy the time I spend with her. Said so the other day myself."
n "แล้วก็ใช่ว่าฉันจะไม่อยากใช้เวลาอยู่ร่วมกับเอมิสักหน่อย วันก่อนฉันก็พูดแบบนี้"

# n "I very nearly didn't even bring anything up with her, was just gonna hop on in there and let it ride, wasn't I?"
n "ก็ตอนนั้นฉันแทบจะตัดใจไม่คุยอะไรกับเอมิแล้วนี่ คิดเอาว่าปล่อยตัวเองให้ไหลไปตามกระแสน้ำก็พอแล้ว"

stop music fadeout 2.0

nvl clear
nvl hide dissolve

scene bg school_nursehall
with shorttimeskip

window show

# "With this running through my head, I find myself in front of the nurse's office, still brooding as he checks out Emi."
"ในหัวฉันคิดเรื่องนี้ไปเรื่อย ๆ จนตัวเองมายืนรอคุณพยาบาลตรวจเอมิอยู่หน้าห้องพยาบาล"

# "Emi comes bounding out of the door, gives me a kiss, and darts off to shower, I assume."
"เอมิโผล่ออกมาแล้วจูบฉันก่อนจะรีบกลับไปอาบน้ำ คิดว่านะ"

# "Meanwhile, the nurse beckons me into his office to give me the ritual once-over."
"ส่วนคุณพยาบาลก็เรียกให้ฉันเข้าไปในห้องเพื่อที่จะได้ตรวจฉันบ้าง"

$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_nurse fadein 0.5

scene bg school_nurseoffice
show nurse neutral at center
with locationchange

# nk "Any problems today?"
nk "วันนี้มีอะไรผิดปกติหรือเปล่า"

# hi "Nah. I even pushed it a little harder today than I have in the past, and I seemed able to handle it."
hi "ไม่ครับ วันนี้ผมฝืนวิ่งให้หนักกว่าทุกทีด้วย แต่ก็เหมือนจะยังวิ่งได้อยู่"

show nurse grin
with charachange

# nk "That's uncharacteristically risky coming from you, Hisao."
nk "ทำอะไรสุ่มเสี่ยงไม่สมเป็นเธอเลยนะฮิซาโอะ"

# nk "You've been hanging out with Emi too much. She's rubbed off on you, and not necessarily in a good way."
nk "เธออยู่กับเอมิบ่อยไปจนติดนิสัยเอมิมาแล้วนะ แล้วก็อาจจะไม่ใช่นิสัยที่ดีด้วย"

# "At the mention of Emi's name, I can't help but frown unhappily in spite of my efforts at control."
"พอมีชื่อเอมิโผล่มาฉันก็อดขมวดคิ้วทำหน้ามุ่ยไม่ได้ทั้งที่พยายามจะเก็บอาการแล้ว"

show nurse fabulous
with charachange

# nk "Well, now. This is new, don't you think?"
nk "เอ้า ๆ ไม่เคยเห็นเป็นแบบนี้เลยนะเนี่ย"

show nurse neutral
with charachange

# nk "Last I checked, your usual response to Emi's name was a grin, not a frown."
nk "ทุกทีพอเธอได้ยินชื่อเอมิแล้วจะยิ้มนะ ไม่ใช่ทำหน้านิ่วแบบนี้"

show nurse concern
with charachange

# nk "What exactly happened between you two? Because Emi doesn't seem to be in on it, whatever it is."
nk "เธอสองคนมีเรื่องอะไรกันหรือเปล่า เพราะเหมือนฝั่งเอมิก็ไม่มีเรื่องอะไรเลยนะ"

show nurse neutral
with charachange

# nk "She looked more relaxed than I've seen her in weeks, which is unusual for this time of the year."
nk "ดูสดใสกว่าที่เห็นช่วงสองสามสัปดาห์ที่ผ่านมาด้วยซ้ำ ซึ่งปกติปีก่อน ๆ ช่วงนี้เอมิจะไม่เป็นแบบนี้เลย"

# hi "What do you mean by that?"
hi "หมายความว่ายังไงครับ"

show nurse fabulous
with charachange

# nk "By what?"
nk "หมายถึง?"

# hi "“For this time of year.” I keep trying to find out what's been bothering her, but she clams up as soon as I broach the subject."
hi "“ปกติปีก่อน ๆ ” น่ะครับ ผมคิดหาคำตอบอยู่ว่าเอมิคิดมากเรื่องอะไรอยู่ แต่พอผมเอาเรื่องนี้ไปคุยทีไรเอมิก็ปิดใจ\nหนีไปก่อนตลอดเลย"

# hi "Then last night, she said—"
hi "แล้วเมื่อคืนเอมิก็บอกว่า—"

show nurse neutral
with charachange

# nk "Let me guess. She won't tell you, because she says she can't trust you?"
nk "ให้เดานะ เอมิไม่ยอมบอกแล้วพูดว่ายังเชื่อใจเธอไม่ได้"

# nk "And now you're crushed, because you thought that the two of you were so much more than she seems to think, right?"
nk "ตอนนี้เธอเลยใจสลายเพราะเธอคิดว่าเธอสองคนเป็นอะไรกันมากกว่าที่เอมิคิด ถูกมั้ย"

# hi "Er, more or less."
hi "เอ้อ ก็ใช่ครับ"

# hi "How the heck did you know?"
hi "แล้วนี่รู้ได้ไงครับ"

show nurse grin
with charachange

# nk "Hisao, I'm the nurse. It's my job to know these things."
nk "ฮิซาโอะ ฉันเป็นคุณพยาบาลนะ หน้าที่ของฉันคือการที่ต้องรู้เรื่องพวกนี้ไว้"

show nurse neutral
with charachange

# nk "Plus, I've known Emi for long enough to know that she'd try to do something like this; it's just like her."
nk "อีกอย่าง ฉันก็รู้จักเอมิมานานพอที่จะรู้ได้ว่าเอมิจะทำอะไรแบบนี้แหละ เพราะนี่แหละคือนิสัยเอมิ"

# "He says this in the sort of half-affectionate, half-frustrated tone that would seem more appropriate if he had a cigarette dangling from his lips."
"คุณพยาบาลพูดด้วยน้ำเสียงกึ่งเอ็นดูกึ่งหงุดหงิดที่คงจะเหมาะมากถ้าในปากคุณพยาบาลคาบบุหรี่ไว้ด้วย"

# "As it is, he seems willing to make do with a pen."
"แต่ตอนนี้คุณพยาบาลก็ใช้ปากกาแทน"

show nurse fabulous
with charachange

label th_choiceE25:
menu:
    with menueffect

    # nk "Look, you mind if I give you some advice?"
    nk "นี่ ขอฉันแนะนำอะไรเธออย่างได้มั้ย"

    # "Sure, why not?":
    "ได้สิ":
       return m1

    # "No, this is my problem.":
    "ไม่ เรื่องนี้คือปัญหาที่ฉันต้องจัดการเอง":
       return m2


label th_E25a:

#If you talked to Mutou, then you get to choose between a) Sure, why not? or b) No, this is my problem. If you didn't talk to Mutou, default to choice b.

#If A

# "What was it Mutou said yesterday?"
"เมื่อวานครูพูดว่ายังไงนะ"

# "If you can't observe the thing, then observe what's around it?"
"ถ้าสังเกตสิ่งนั้นไม่ได้ ก็ให้สังเกตสิ่งที่อยู่รอบ ๆ สิ่งนั้นแทน"

# "Worth a shot."
"ลองดูก็ไม่เสียหาย"

# "The nurse knows Emi better than I do, I'll wager."
"ยังไงเสียคุณพยาบาลก็คงรู้จักเอมิดีกว่าฉัน"

# hi "Sure, I'm open to suggestions."
hi "ได้ครับ ผมพร้อมรับฟังทุกคำแนะนำ"

# hi "Honestly, I'm kind of lost."
hi "เอาตรง ๆ ตอนนี้ผมไม่รู้จะทำยังไงดี"

# hi "I've got no idea how to deal with this."
hi "ผมมืดแปดด้านเลย"

show nurse grin
with charachange

# nk "I never would have guessed."
nk "คาดไม่ถึงเลยนะเนี่ย"

# "He grins while he says this. I think he's kidding."
"คุณพยาบาลพูดยิ้ม ๆ คงพูดเล่นแหละ"

show nurse neutral
with charachange

# nk "Look, here's the deal: Emi is… stubborn."
nk "นี่นะ เรื่องคือว่า เอมิน่ะ… หัวแข็ง"

show nurse grin
with charachange

# nk "You should know that by now, and if you don't then you're pretty unobservant, but I'm giving you the benefit of the doubt here."
nk "ป่านนี้เธอคงรู้แล้ว ถ้าไม่รู้ก็คงเป็นคนไม่สนโลกมาก แต่ฉันเชื่อว่าเธอไม่ใช่คนอย่างนั้นหรอก"

# hi "I'm so grateful."
hi "ขอบคุณมากครับ"

show nurse neutral
with charachange

# nk "Anyway, if she's decided that she doesn't want to talk about what happened, then she's not going to talk about what's happened."
nk "แต่นั่นแหละ ถ้าเอมิตั้งใจไว้แล้วว่าจะไม่คุยถึงเรื่องที่เกิดขึ้นแล้วเอมิก็จะไม่คุยถึงเรื่องที่เกิดขึ้นเลย"

# nk "Has she said anything about what's been bothering her? Even a hint?"
nk "เอมิได้บอกมั้ยว่ามีเรื่องอะไรกวนใจอยู่ หรือบอกเป็นนัย ๆ งี้"

# hi "Well, she did say she'd been having nightmares about the accident…"
hi "ก็บอกอยู่ครับว่าฝันร้ายเรื่องอุบัติเหตุ…"

show nurse fabulous
with charachange

# nk "Really? You're making progress, then. That's good."
nk "จริงเหรอ งั้นก็ถือว่าคืบหน้าแล้ว ดี"

show nurse neutral
with charachange

# nk "Well, I guess I can fill you in on this without violating my strict non-interference policy when it comes to Emi making stupid decisions."
nk "โอเค ฉันน่าจะบอกเธอเรื่องนี้ได้ คงไม่ผิดกฎที่ฉันต้องทำตัวเป็นกลางอยู่เฉย ๆ เวลาเอมิตัดสินใจอะไรงี่เง่าลงไป"

show nurse concern
with charachange

# nk "The anniversary of her accident is coming up soon."
nk "อีกเดี๋ยวก็ใกล้ถึงวันครบรอบที่เกิดอุบัติเหตุครั้งนั้นแล้ว"

# nk "She gets depressed around this time, because it was a pretty traumatic event, considering what she lost."
nk "ช่วงนี้เอมิจะหดหู่น่ะ อุบัติเหตุหนนั้นเป็นเหตุการณ์ที่สะเทือนใจมากเพราะเอมิต้องเสียบางอย่างไป"

# hi "That's the other thing. She acted like she lost more than just her legs. What happened?"
hi "อันนั้นก็อีกเรื่องนะครับ ดูท่าทางแล้วเอมิเหมือนจะเสียอย่างอื่นนอกจากขาด้วย ตอนนั้นเกิดอะไรขึ้นเหรอครับ"

show nurse fabulous
with charachange

# nk "Whoa! Nope, not going there. You'll have to ask someone else about that, because that's a whole can of worms I'm not about to open."
nk "เฮ้ย! ไม่ ๆ ไม่เอาเรื่องนี้ ไปถามกับคนอื่นนะ ฉันไม่อยากไปขุดคุ้ยอะไรกับเรื่องนี้ให้ยืดยาวอีก"

show nurse neutral
with charachange

# nk "If Emi wants you to know, she'll tell you in her own time."
nk "ถ้าเอมิอยากให้เธอรู้จริง ๆ เดี๋ยวก็บอกเองตอนที่พร้อมแล้วแหละ"

# nk "You've just got to be patient, that's all."
nk "เธอแค่คอยอยู่อย่างใจเย็นไป"

# hi "Why are you even helping me with all this?"
hi "ทำไมคุณถึงช่วยผมล่ะครับ"

show nurse grin
with charachange

# nk "Because you're good for her. She trusts you, even if you don't think she does."
nk "เพราะเธอดีกับเอมิไง เอมิน่ะเชื่อใจเธอนะ ต่อให้เธอจะคิดว่าเอมิไม่เชื่อก็เถอะ"

# nk "And you've got the best chance out of anyone at this school right now to help her through this time of year."
nk "แล้วเธอก็เป็นคนที่อาจจะช่วยให้เอมิผ่านพ้นช่วงเวลานี้ไปได้ดีที่สุดแล้วถ้าให้เทียบกับคนอื่น ๆ ในโรงเรียนนี้"

show nurse neutral
with charachange

# nk "She won't accept my help, but she might accept yours if you don't screw it up."
nk "เอมิไม่ยอมให้ฉันช่วย แต่ถ้าเธอไม่ทำพลาดแล้วละก็เอมิอาจจะยอมให้เธอช่วยก็ได้"

show nurse fabulous
with charachange

# nk "So don't screw it up, got it?"
nk "เพราะงั้นอย่าทำพลาดละ เข้าใจนะ"

#if b

label th_E25b:

# "Advice? About what? I don't think there's anything I can actually do about this."
"แนะนำเหรอ เรื่องอะไร ฉันว่าฉันทำอะไรกับเรื่องนี้ไม่ได้หรอก"

# hi "Not really. I don't think there's anything you can say that'll help."
hi "ไม่เป็นไรครับ ผมว่าต่อให้คุณพูดอะไรก็คงไม่ได้มีอะไรดีขึ้นมา"

show nurse neutral
with charachange

# nk "You never know, Hisao."
nk "ไม่ลองไม่รู้น่าฮิซาโอะ"

# hi "No, I think I've got a pretty good idea."
hi "ไม่ครับ ผมว่าผมรู้ดีเลยแหละ"

# hi "Emi's just being stubborn about some things, and it's bothering me, but I'll get over it."
hi "เอมิก็แค่หัวแข็งจนผมไม่หายคาใจ แต่เดี๋ยวผมก็ทำใจได้แหละครับ"

# hi "Don't worry about us."
hi "ไม่ต้องห่วงเราหรอกครับ"

show nurse concern
with charachange

# "The nurse doesn't seem to believe me, but shrugs."
"คุณพยาบาลเหมือนจะไม่เชื่อฉัน เขายักไหล่"

# nk "Have it your way, kiddo."
nk "ตามใจเธอเลยพ่อหนุ่ม"

#end split

label th_E25c:

$ renpy.music.set_volume(0.3, 0.0, channel="sound")
play sound sfx_hammer

# "I open my mouth to respond but a knocking sound at the door interrupts me."
"ฉันอ้าปากเตรียมจะตอบแต่เสียงเคาะประตูก็ดังขึ้นมาขัดก่อน"

# emi "Hey, you guys still in there?"
emi "นี่ ยังอยู่กันมั้ยเนี่ย"

show nurse grin
with charachange

# nk "Just a moment, Emi."
nk "แป๊บนะเอมิ"

# nk "Give us a second to get our pants back on."
nk "ขอเราใส่กางเกงกันก่อน"

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_doorslam

show emi invis:
    tworight
    xpos 1.0
with None

show bg school_nurseoffice at bgleft
show nurse grin at twoleft
show emi basic_annoyed_gym at tworight
with dissolvecharamove

# "The door bursts open and Emi glares knives at the nurse."
"เอมิเปิดประตูเสียงดังปังแล้วจ้องอาฆาตใส่คุณพยาบาล"

# emi "Asshole."
emi "บ้า"

show nurse fabulous
with charachange

# nk "Didn't mean to get your hopes up."
nk "ไม่ได้กะจะให้ความหวังเธอนะ"

# hi "Hey, can we… leave me out of this?"
hi "นี่ อย่า… ลากผมไปเกี่ยวด้วยสิ"

# hi "Anyway, what's up, Emi? Forget something?"
hi "ว่าแต่มีอะไรเหรอเอมิ ลืมอะไรหรือเปล่า"

# "I try to take a more cheerful tone with her."
"ฉันทำน้ำเสียงให้ฟังดูร่าเริงขึ้นตอนพูดกับเอมิ"

# "No need to upset her. Two can play the “everything's fine” game."
"ไม่จำเป็นต้องไปทำให้เอมิโกรธ เธอเล่น “ทำเหมือนทุกอย่างยังปกติดี” เป็นคนเดียวหรือไง"

show emi sad_grin_gym at tworight
with charachange

# emi "Actually, I forgot to ask you something."
emi "คือว่าฉันลืมถามนายอย่างน่ะ"

# hi "Oh? What's that?"
hi "อ้อ อะไรเหรอ"

show emi basic_happy_gym
with charachange

# emi "Do you wanna come with me on a trip to my house?"
emi "ไปเที่ยวบ้านฉันด้วยกันมั้ย"

show emi basic_closedgrin_gym
with charachange

# emi "My mom's making dinner, and I thought you might want to join us."
emi "แม่ฉันจะทำข้าวเย็นไว้ให้ ก็เลยกะจะมาชวนนายไปกินด้วย"

show nurse grin
with charachange

# nk "Well, of course I accept."
nk "อ้อ ได้สิ ย่อมได้"

show emi basic_closedgrin_gym:
    parallel:
        "emi excited_proud_gym" with Dissolve(0.2, alpha=True)
    parallel:
        ease 0.2 xpos 0.6
        ease 0.2 tworight
with Pause(0.5)

# "Emi punches the nurse in the arm playfully."
"เอมิต่อยแขนคุณพยาบาลเบา ๆ เป็นการหยอก"

# emi "Not you, idiot. You were over last week."
emi "ไม่ใช่คุณพยาบาลสิ สัปดาห์ที่แล้วก็ไปแล้วนี่"

show emi sad_grin_gym at tworight
with charachange

# emi "I was talking to Hisao."
emi "หนูคุยกับฮิซาโอะอยู่ต่างหาก"

show nurse neutral
with charachange

# nk "Oh? How interesting! Meeting the parent!"
nk "อ้อ น่าสนใจดีนี่! ได้ไปทักทายครอบครัว!"

# hi "I'd love to go, Emi. Thanks."
hi "ไปอยู่แล้วสิเอมิ ขอบคุณนะ"

show nurse fabulous
with charachange

# "The nurse raises an eyebrow, but says nothing."
"คุณพยาบาลเลิกคิ้วแต่ก็ไม่พูดอะไร"

# emi "Great! I'll be in my room, swing by after you shower and change into something clean and we'll grab the bus!"
emi "เยี่ยมเลย! เดี๋ยวฉันจะกลับไปที่ห้องก่อน พอนายอาบน้ำเปลี่ยนเสื้อผ้าแล้วเราจะขึ้นรถบัสไปด้วยกัน!"

# hi "Sounds good. I'll see you in a bit!"
hi "ก็ดี เดี๋ยวเจอกัน!"

stop music fadeout 2.0

show emi excited_amused_gym_close
with characlose

# "This time it's me who leans in for a quick kiss before darting off to my room."
"คราวนี้ถึงทีฉันบ้างที่โน้มตัวเข้าไปจุ๊บก่อนจะมุ่งหน้าไปที่ห้องฉัน"

scene bg school_dormhisao
with locationskip

# "What an interesting development."
"เรื่องชักน่าสนใจแล้วสิ"

# "Maybe we're getting closer after all."
"หรือเราจะได้สนิทกันมากขึ้นแล้วจริง ๆ"

# "Maybe Emi's finally ready to open up a little."
"หรือเอมิจะยอมเปิดใจให้ฉันบ้างแล้วสักที"

# "Or maybe she's just being polite, and a free meal seems like a good way to apologize for last night."
"หรือเอมิอาจจะชวนตามมารยาทเฉย ๆ แล้วเลี้ยงข้าวเป็นการขอโทษกับเรื่องเมื่อคืน"

# "Great. Now I can't decide whether to be excited, nervous, or depressed."
"เยี่ยม ตอนนี้เลือกไม่ถูกเลยว่าจะตื่นเต้น จะประหม่า หรือจะหดหู่ดี"

# "I settle for a combination of all three and hop in the shower."
"ฉันเหมารวบทั้งสามความรู้สึกแล้วไปอาบน้ำ"

scene black
with dissolve

$ suppress_window_after_timeskip = True

#############################

label th_E26:

window hide None

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_businterior fadein 2.0

scene ev busride
with locationchange

nvl clear
nvl show dissolve

# n "\n\n\nI don't think I like riding on buses."
n "\n\n\nฉันว่าฉันเกลียดการนั่งรถบัส"

# n "Actually, I think I'm pretty comfortable saying that as a fact."
n "กล้าพูดเลยว่าฉันเกลียดจริง ๆ"

# n "They sway a lot, and they smell funny, and you can feel every bump in the road."
n "ทั้งโงนเงนไปมา กลิ่นก็แปลก ๆ พอถนนขรุขระก็สะดุดกึก ๆ"

# n "I'm really not looking forward to this."
n "ฉันไม่ชอบเลยจริง ๆ"

# n "\nPlus Emi's legs keep making a clanking noise that draws the attention of everyone else on the bus."
n "\nอีกอย่างขาเอมิก็ชนกันแล้วส่งเสียงจนเป็นที่สนใจของทุกคนในรถบัส"

# n "She's in shorts again, and she's got long socks drawn up on her prosthetics so they don't look so obviously false again."
n "เอมิกลับมาใส่กางเกงขาสั้น และมีถุงเท้ายาวที่ใส่กับขาเทียมไว้ไม่ให้เห็นชัดมากว่าเป็นขาปลอม"

# n "But that doesn't stop the odd look or two every time her legs bump together with an audible clunk."
n "แต่ทุกครั้งที่ขาเทียมชนกันเสียงดังนั้นก็ยังมีคนหันมามองอยู่บ้าง"

nvl clear

# n "\n\n\nI shift nervously in my seat, and Emi raises an eyebrow questioningly."
n "\n\n\nฉันนั่งยุกยิกจนเอมิเลิกคิ้วมองด้วยความสงสัย"

# n "She doesn't seem to mind the stares; either that or she doesn't even notice that people are staring."
n "เอมิเหมือนจะไม่สนใจอะไรที่คนมอง หรือไม่ก็ไม่ทันสังเกตด้วยซ้ำว่ามีคนจ้องอยู่"

# n "I'm sure she's gotten her fill of odd looks before. After a certain amount of time, I doubt she'd notice any more."
n "ก่อนหน้านี้ก็คงมีคนมองเอมิแปลก ๆ แล้วละนะ ผ่านไปสักระยะหนึ่งแล้วเธอก็คงไม่ได้สังเกตเลย"

# n "\n\nNot that she'd ever tell me if I asked."
n "\n\nแต่ต่อให้ถามเอมิก็คงไม่บอกหรอก"

# n "Another fact is, I'm not just uncomfortable about the bus."
n "อีกอย่างคือ ที่ฉันอึดอัดไม่ใช่แค่เพราะต้องนั่งรถบัส"

# n "I can't seem to come to terms with the fact that Emi appears to be trying to bring me closer while at the same time pushing me away."
n "ฉันทำใจไม่ได้กับการที่เอมิทำตัวเหมือนจะดึงฉันให้เข้าไปใกล้ชิดขึ้น ทว่าก็ผลักไสฉันออกมาไปด้วย"

nvl clear

#if you picked A in e25

label th_E26a:

# n "\n\n\nThe nurse said she trusts me, even if it doesn't look like it."
n "\n\n\nคุณพยาบาลบอกว่าเอมิเชื่อใจฉัน ถึงจะดูเหมือนไม่ใช่อย่างนั้นก็ตาม"

# n "But I'm not sure I can trust the nurse."
n "แต่ฉันไม่แน่ใจว่าจะเชื่อคุณพยาบาลดีหรือเปล่า"

# n "He's protective of Emi, just like I'm protective of Emi, and I'd be likely to say something to make her look good if someone asked me about her."
n "คุณพยาบาลคอยปกป้องเอมิเหมือนอย่างฉัน และฉันก็คงจะพูดอะไรให้เอมิดูดีเหมือนกันถ้ามีคนมาถามฉันเรื่องเอมิ"

# n "\nSo he might just be doing that."
n "\nเพราะงั้นคุณพยาบาลอาจจะพูดด้วยเจตนานั้นก็ได้"

# n "\nStill, there was something about the way he seemed genuinely surprised that Emi invited me along…"
n "\nแต่คุณพยาบาลก็ดูประหลาดใจจริง ๆ ตอนที่เอมิมาชวนฉันไปด้วย…"

# n "Maybe last night's talk helped more than I think, but I'm still worried."
n "ที่คุยกันเมื่อคืนอาจช่วยอะไรได้ดีกว่าที่ฉันคิด แต่ก็ยังกังวลอยู่ดี"


label th_E26b:

stop ambient fadeout 12.0

nvl clear

# n "\n\n\nMeeting the parents is a big deal, right?"
n "\n\n\nการได้เจอกับครอบครัวน่ะเป็นเรื่องสำคัญเลยใช่มั้ยล่ะ"

# n "Not that I haven't already met Emi's mother, but that was just as an acquaintance."
n "ก่อนหน้านี้ฉันก็เคยเจอแม่เอมิมาแล้วแหละ แต่หนนั้นฉันก็เป็นแค่คนรู้จัก"

# n "Now it's going to be as Emi's boyfriend, with everything that implies."
n "ตอนนี้ฉันจะไปเจอในฐานะแฟนหนุ่มของเอมิ"

# n "I can feel my heart pounding in my chest, an echo of that snow-covered afternoon that feels like it was so long ago that it might as well be another life entirely."
n "ฉันรู้สึกถึงใจที่เต้นรัวขึ้นมา ย้อนนึกถึงภาพจากอดีตในบ่ายวันหิมะตกวันนั้นที่ผ่านมานานเหมือนเป็นชาติที่แล้ว"

# n "Except then, I didn't know what was going on; I also didn't have medication to help prevent things spiraling out of control."
n "จะไม่เหมือนก็แต่ตอนนั้นฉันไม่รู้ว่าเกิดอะไรขึ้น และไม่ได้กินยาที่คอยควบคุมเรื่องไม่ให้บานปลายไปไกล"

# n "I've come a long way in terms of my physical health, and for the second time today I feel like I'll be able to live normally now, or at least as normally as possible."
n "สุขภาพร่างกายฉันแข็งแรงขึ้นมากแล้ว วันนี้ฉันได้รู้สึกอีกครั้งว่าจะได้ใช้ชีวิตตามปกติ หรืออย่างน้อย ๆ ก็ปกติ\nเท่าที่จะทำได้"

# n "\nNow if only I could manage my relationship as well as I've managed my heart, I'd be in great shape."
n "\nถ้าฉันจัดการกับเรื่องความรักความสัมพันธ์ได้ดีเหมือนอย่างที่ฉันดูแลเรื่องหัวใจแล้วละก็จะนับได้ว่าชีวิตดีทีเดียว"

stop ambient fadeout 1.5

window hide None

nvl clear
nvl hide dissolve

scene bg city_street4
show emicas smile_close at center
with shorttimeskip

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_traffic fadein 2.0

window show

# emi "Well, we're here."
emi "โอเค ถึงแล้ว"

play music music_soothing fadein 2.0

# "Emi grabs my hand as soon as we've stepped off the bus. She starts heading down the street almost immediately."
"เอมิจับมือฉันทันทีที่เราลงจากรถบัส เธอไม่รีรอรีบนำฉันไปตามถนน"

show emicas wink_up_close
with charachange

# emi "Come on, we've got a couple blocks until my place."
emi "เร็ว บ้านฉันต้องเดินไปอีกหน่อยนะ"

# hi "What? Oh, okay."
hi "ฮะ? อ้อ โอเค"

scene bg city_alley
with locationchange

stop ambient fadeout 12.0

# "I follow Emi down the street, watching her confident stride."
"ฉันเดินตามเอมิที่เดินไปตามถนนอย่างมั่นใจ"

# "She's setting kind of a quick pace for just a walk."
"ถือว่าเป็นฝีเท้าที่เร็วกว่าเกินคำว่าเดิน"

# "I guess she's anxious to get there."
"คงจะอยากรีบไปให้ถึงบ้านมั้ง"

# hi "So does your mom do this sort of thing often?"
hi "ปกติแม่เธอทำอะไรแบบนี้บ่อยมั้ย"

show emicas neutral_close at center
with charaenter

# emi "Nah, not too frequently. Mom's never been much for playing hostess."
emi "ไม่อะ ไม่บ่อยมาก แม่ไม่ค่อยชวนใครมาที่บ้านเท่าไหร่แต่ไหนแต่ไรแล้ว"

# hi "Oh yeah?"
hi "งั้นเหรอ"

show emicas awayfrown_close
with charachange

# emi "Yeah, my dad was always the one pushing her to have people over."
emi "อื้ม ปกติเป็นพ่อฉันมากกว่าที่บอกให้แม่ชวนคนอื่นมาที่บ้าน"

# "This sudden and unprompted reference to her father catches me off guard."
"ฉันไม่ทันตั้งตัวที่อยู่ ๆ เอมิก็พูดถึงพ่อขึ้นมาแบบไม่มีปี่มีขลุ่ยแบบนี้"

# "And from the look on Emi's face, I'm not sure she meant to mention him. I think I've only ever heard her talk about him once."
"และดูจากสีหน้าแล้วฉันก็ไม่แน่ใจว่าเอมิตั้งใจจะพูดถึงหรือเปล่า เหมือนจะเคยได้ยินพูดถึงแค่ครั้งเดียวเองมั้ง"

# "All I remember is that Emi's mom told me that he wasn't around any more."
"เท่าที่ฉันจำได้คือตอนที่แม่เอมิบอกว่าเขาไม่อยู่แล้ว"

# hi "Oh? Your mom prefers solitude?"
hi "หืม แม่เธอชอบอยู่คนเดียวเหรอ"

show emicas happy_up_close
with charachange

# "Emi laughs, either from relief that I didn't ask about her father or from finding my statement actually funny."
"เอมิหัวเราะ ซึ่งอาจจะเพราะโล่งใจที่ฉันไม่ถามเรื่องพ่อหรืออาจจะเพราะตลกกับคำถามฉันจริง ๆ"

# emi "Not at all! She's why I'm such an outgoing person, you know."
emi "ไม่เลย! ที่จริงที่ฉันเป็นคนชอบไปไหนมาไหนก็เพราะแม่ด้วยซ้ำ"

show emicas closedsmile_close
with charachange

# emi "She just prefers to be a guest rather than a hostess; it's less stressful that way, or so she says."
emi "แค่ว่าแม่ชอบไปเป็นแขกมากกว่าที่จะต้องเป็นเจ้าบ้านน่ะ เห็นบอกประมาณว่าเป็นแขกแล้วสบายใจกว่าเป็นเจ้าบ้าน"

# hi "Clearly she's never had to meet her girlfriend's mother for dinner."
hi "แปลว่ายังไม่เคยไปกินข้าวเย็นด้วยกันกับแม่แฟนแหง ๆ"

# "Emi giggles again and speaks in a teasing tone."
"เอมิหัวเราะคิกคักอีกรอบแล้วพูดด้วยน้ำเสียงหยอกล้อ"

show emicas wink_close
with charachange

# emi "Nervous, Hisao?"
emi "ประหม่าเหรอฮิซาโอะ"

show emicas smile_close
with charachange

# emi "You shouldn't be, you know! It's not that big a deal! Just dinner at my house, that's all!"
emi "ไม่เห็นต้องประหม่าเลย! ไม่ใช่เรื่องสำคัญขนาดนั้น! แค่กินข้าวเย็นด้วยกันที่บ้านฉันเอง!"

# hi "Yeah, but have you ever brought home a boyfriend before?"
hi "ก็ใช่ แต่เธอเคยพาแฟนเข้าบ้านมาก่อนหรือเปล่าล่ะ"

# "I confess that part of me dreads hearing the answer to this."
"ขอยอมรับว่าใจหนึ่งฉันก็กลัวคำตอบเอมิเหลือเกิน"

# "I know very little of Emi's past relationships - I don't even know if there were past relationships."
"ฉันแทบไม่รู้เรื่องความสัมพันธ์ในอดีตของเอมิเลย ไม่รู้ด้วยซ้ำว่าเคยคบกับใครมาก่อนหรือเปล่า"

show emicas awayfrown_close
with charachange

# emi "No, I guess I haven't."
emi "ไม่นะ เหมือนจะไม่"

show emicas frown_close
with charachange

# emi "Hey, maybe this really is kind of a big deal after all…"
emi "อ้าว หรือว่าจะเป็นเรื่องสำคัญจริง ๆ ล่ะเนี่ย…"

# hi "Oh good, now I feel twice as nervous."
hi "อ้าว เยี่ยม ทีนี้ละยิ่งประหม่าไปอีก"

# "Though to tell the truth, I'm pretty happy to hear that I'm the first one."
"ว่าตามตรงฉันก็ดีใจเหมือนกันที่ได้รู้ว่าฉันเป็นคนแรก"

# "Maybe we've got something special after all."
"หรือความสัมพันธ์ระหว่างเราอาจจะพิเศษจริง ๆ ก็ได้"

stop ambient
stop music fadeout 10.0

scene bg emi_houseext
with locationchange

play sound sfx_hammer

# "Bolstered by this new thought, I've managed to calm down considerably by the time Emi knocks on her front door."
"ฉันมีแรงขึ้นมาเมื่อคิดได้ดังนั้นจนพอเอมิมาเคาะประตูหน้าบ้านแล้วฉันก็ใจเย็นขึ้นพอสมควร"

show emicas grin_up at center
with charaenter

# emi "Hey, mom, open up! We're here!"
emi "แม่คะ เปิดประตูหน่อย! มาแล้วค่ะ!"

show bg emi_houseext at bgleft
show emicas grin_up at twoleft
with charamove

show meiko smile at tworight
with charaenter

# "The door swings open, and Mrs. Ibarazaki stands grinning at her daughter. The grin is still surprisingly similar to Emi's."
"พอประตูเปิดออกก็มีคุณนายอิบาราซากิที่ยืนส่งยิ้มให้ลูกสาวอยู่ เป็นรอยยิ้มที่คล้ายกับเอมิอย่างเหลือเชื่อ"

# "I'm never going to get used to that."
"ให้ตายฉันก้ไม่ชิน"

show meiko wink
with charachange

# emm "You know, people normally wait for a few minutes before they start shouting at the door."
emm "นี่นะ ปกติคนเขาต้องรอสักสองสามนาทีก่อนค่อยตะโกนเรียก"

show emicas pout_up
with charachange

# emi "And most mothers say hello to their daughters instead of scolding them right away."
emi "แล้วปกติคนเป็นแม่จะต้องทักทายลูกสาวตัวเองก่อน ไม่ใช่มาถึงก็ดุเลย"

show meiko happy
with charachange

# emm "Ah, of course. Welcome home, dear. I've missed you."
emm "แหม ได้จ้ะ ยินดีต้อนรับกลับบ้านนะจ๊ะ คิดถึงลูกจังเลย"

play music music_another fadein 0.5

scene bg emi_kitchen
with locationchange

# "An affectionate hug later we're inside, and it is only then that Emi's mom seems to remember that I'm actually here."
"พอเข้าไปในบ้านแล้วทั้งสองคนก็กอดกันอย่างอบอุ่น และเป็นตอนนั้นเองที่แม่เอมิเหมือนจะเพิ่งนึกได้ว่ามีฉันยืนหัวโด่\nอยู่ตรงนี้"

show meiko smile at center
with charaenter

# emm "And hello to you too, Hisao. How are you?"
emm "แล้วก็สวัสดีฮิซาโอะด้วยนะ สบายดีหรือจ๊ะ"

# hi "I'm quite well, thank you. Nice to not have school to worry about for a little bit."
hi "ครับ สบายดีครับ พอไม่ต้องเครียดเรื่องเรียนสักพักแล้วค่อยสบายตัวหน่อย"

show meiko happy
with charachange

# emm "Ah yes, you've finished up your exams, haven't you? That must be quite a relief for you both."
emm "อ้อ จริงสิ เพิ่งสอบเสร็จกันนี่นา ใช่มั้ย เธอสองคนคงโล่งกันน่าดู"

# hi "It's certainly a weight off of my mind, that's for sure."
hi "แค่ไม่ต้องเครียดเรื่องสอบก็โล่งขึ้นเยอะแล้วละครับ"

show bg emi_kitchen at bgright
show meiko happy at tworight
with charamove

show emicas happy at twoleft
with charaenter

# emi "Mine too! I think I slept well for the first time in weeks last night from relief alone."
emi "หนูก็ด้วย! หนูนอนไม่ค่อยหลับมาสองสามสัปดาห์แล้ว แต่เพราะโล่งแล้วถึงเพิ่งได้หลับสนิทก็เมื่อคืนนี่แหละค่ะ"

# "If this news is a surprise to Emi's mother, she doesn't show it. Still, her response betrays a note of interest."
"แม่เอมิทำท่าเหมือนไม่ได้แปลกใจอะไรกับข้อมูลส่วนนี้ แต่คำตอบนั้นแฝงด้วยความสนใจ"

show meiko smile
with charachange

# emm "Is that so? I'm very glad to hear that, Emi. You know I get worried when you get all wound up about… well, exams."
emm "งั้นเหรอจ๊ะ รู้แบบนี้ก็ดีใจแล้วละ แม่ก็เป็นห่วงเพราะเห็นลูกเครียดกับ… เรื่องสอบนั่นแหละ"

# "Certainly Emi's mother knows something I don't - or rather, she doesn't know that Emi's told me about the nightmares."
"ชัดว่าแม่เอมิรู้บางอย่างที่ฉันไม่รู้ หรือก็คือไม่รู้ว่าเอมิเล่าเรื่องฝันร้ายนั้นให้ฉันฟัง"

# "It's interesting, being able to observe how Mrs. Ibarazaki covers for Emi. That protective instinct to make sure that I don't know any more than Emi's willing to tell me."
"น่าสนใจดีที่ได้เห็นคุณนายอิบาราซากิคอยคุ้มกันเอมิอย่างนี้ เป็นสัญชาตญาณการปกป้องเพื่อกันไม่ให้ฉันรู้อะไร\nไปมากกว่าเท่าที่เอมิเต็มใจจะบอกฉัน"

#once again, see this only if you talked to Mutou
label th_E26e:

# "I suppose Emi's got more in common with quarks than I ever realized."
"เอมิคงมีจุดร่วมกับควาร์กมากกว่าที่ฉันคิด"

# "Moves around fast, impossible to understand through direct observation, yet she has an effect on everyone she encounters."
"เคลื่อนตัวรวดเร็ว ทำความเข้าใจด้วยการสังเกตโดยตรงไม่ได้ แต่กลับมีผลกับทุกอย่างที่ไปอยู่ด้วย"


label th_E26f:

# "I wonder if Mrs. Ibarazaki will figure out that I know about the nightmares, or is she just keeping everything secret from everybody?"
"คุณนายอิบาราซากิจะรู้หรือเปล่านะว่าฉันรู้เรื่องฝันร้ายนั้น หรือเก็บทุกอย่างไว้เป็นความลับไม่ยอมบอกใครอยู่แล้ว"

show emicas weaksmile
with charachange

# emi "Yeah, it's not been as bad this year as in the past; Hisao helped me to stay focused."
emi "ค่ะ ปีนี้ค่อยดีกว่าปีก่อน ๆ หน่อย ฮิซาโอะเขาก็ช่วยทำให้หนูมีสมาธิขึ้นด้วย"

# "Okay, I know that's not true. She even cut off contact outside of school hours during exam week!"
"โอเค อันนี้แหละรู้ว่าไม่จริงแน่ ๆ ช่วงสัปดาห์สอบยังไม่ติดต่อกันนอกเวลาเรียนเลยด้วยซ้ำ!"

# "But… she did see me during the day. And she told me more than once that the morning run was the only thing she looked forward to during exams, so maybe it's not that much of a lie."
"แต่… ตอนกลางวันก็มาเจอกันอยู่ แล้วก็บอกหลายรอบด้วยว่าอย่างเดียวที่ตั้งตาคอยช่วงสอบคือการได้วิ่งตอนเช้า\nถือว่าพูดจริงอยู่แหละ"

# "Either way, to hear that being around has helped even a little makes me feel a bit better."
"แต่จะยังไงก็เถอะ ได้ยินว่าพออยู่เคียงข้างแล้วมีประโยชน์แม้เพียงสักนิดแบบนี้ก็รู้สึกดีขึ้นมาหน่อยหนึ่งแล้ว"

# "Emi's mother raises an eyebrow at this statement. Either she doesn't believe Emi, or she's as surprised as I am."
"แม่เอมิเลิกคิ้วกับประโยคนั้น อาจจะเพราะไม่เชื่อหรือแปลกใจเหมือนกันกับฉัน"

show meiko happy
with charachange

# emm "Well, then it appears that it's a good thing you two have become so close."
emm "โอเคจ้ะ งั้นก็คงดีแล้วละที่เธอสองคนสนิทกันขนาดนี้"

show meiko smile
with charachange

# emm "I'd tell you to take good care of my daughter, Hisao, but it looks like you're already doing that."
emm "ฮิซาโอะ ฉันก็อยากบอกอยู่นะว่าฝากดูแลลูกสาวด้วย แต่เหมือนเธอจะดูแลดีอยู่แล้วละนะ"

show emicas closedsmile
with charachange

# "Emi grins at this and seems to take pride in my having managed to ingratiate myself with her mother so easily."
"เอมิยิ้มดูภูมิใจที่ฉันทำให้แม่ของเธอปลื้มได้อย่างง่ายดายขนาดนี้"

# hi "Actually, I'd say your daughter's been the one taking care of me. She's gotten me out and running."
hi "จริง ๆ ลูกสาวคุณต่างหากครับที่ดูแลผม เอมิเขาเป็นคนลากผมให้ออกมาวิ่ง"

# hi "I've probably been more active since meeting her than I ever was, even before…"
hi "ตั้งแต่ผมได้มาเจอเอมิผมก็ได้ขยับตัวขึ้นเยอะ เยอะกว่าตอน…"

# "I'd actually never thought of it that much, nor had I ever appreciated the humor in it."
"ที่จริงฉันไม่เคยคิดเรื่องนี้เท่าไหร่เลย ไม่เคยคิดเลยว่าเป็นเรื่องตลก"

# "I wasn't too active before the heart attack. Pickup games of soccer don't really count since they weren't that common."
"ก่อนหน้าที่หัวใจวายครั้งนั้นฉันก็ไม่ค่อยได้ขยับตัวเท่าไหร่อยู่แล้ว ที่เตะฟุตบอลกันตามนัดนั้นก็ไม่นับ\nเพราะไม่ได้เตะกันบ่อยมาก"

# "So now that I know for sure that I have a weak heart, {b}now{/b} I run every day, pushing my luck with the help of my medication."
"ตอนนี้ฉันถึงได้แน่ใจแล้วจริง ๆ ว่าหัวใจฉันไม่แข็งแรง {b}หลังจาก{/b}ที่ฉันได้มาวิ่งทุกวันฝืนตัวเองไปพลางกินยา"

# "I chuckle quietly, then realize that I never finished my sentence."
"ฉันแค่นหัวเราะในใจก่อนจะนึกได้ว่ายังพูดไม่จบประโยค"

# hi "Well, before I had my heart attack and wound up at school here."
hi "ก็เยอะกว่าตอนที่ผมเป็นหัวใจวายแล้วต้องมาเรียนที่นี่แหละครับ"

# "It comes out so casually. There was a time that I would have thought twice about talking about what was wrong with me at all."
"ฉันพูดออกมาได้สบาย ๆ เมื่อก่อนยังมีช่วงหนึ่งที่ฉันจะคิดแล้วคิดอีกว่าจะพูดเรื่องความผิดปกติของฉันดีหรือเปล่า"

# "But now? Now it just seems silly to care, especially in the company of Emi and her mother."
"แต่ตอนนี้เหรอ ดูงี่เง่าสิ้นดี ยิ่งได้อยู่กับเอมิแล้วก็แม่ของเธอด้วย"

# "If Emi can be cavalier about her disability, then so can I."
"ถ้าเอมิไม่คิดมากเรื่องความพิการของตัวเองได้ ฉันก็ทำแบบนั้นได้เหมือนกัน"

# "I think back to the track meet, where Emi declared herself the fastest thing on no legs."
"ฉันนึกย้อนไปยังตอนงานแข่งวิ่งที่เอมิประกาศว่าตัวเองคือสิ่งไม่มีขาที่เร็วที่สุด"

# "The fact of her obvious loss has never seemed to bother her, at least not in public."
"เอมิดูจะไม่เคยกังวลถึงความสูญเสียที่เห็นได้ชัดของตัวเองนั้นเลย อย่างน้อยก็ตอนอยู่ต่อหน้าคนอื่นน่ะนะ"

# "Being stuck in the wheelchair frustrated her, I know. But even that was something she dealt with on her own, despite my efforts to the contrary."
"ฉันรู้ว่าเอมิหงุดหงิดที่ต้องนั่งวีลแชร์ แต่เธอก็รับมือกับปัญหานั้นได้เอง ต่อให้จะมีฉันคอยช่วยอยู่ก็ตาม"

show meiko happy
with charachange

# emm "Emi has a way of bringing out the more active side in people. I've never quite figured out how she does it."
emm "เอมิเขามีวิธีทำให้ความกระตือรือร้นในตัวคนอื่นตื่นขึ้นมาได้น่ะจ้ะ ฉันก็ไม่ค่อยเข้าใจเหมือนกันว่าทำได้ยังไง"

# "Those puppy dog eyes she gets, for starters."
"เป็นต้นว่า ตาลูกหมาน้อยนั่นไง"

show meiko smile
with charachange

# emm "I'm not surprised that she managed to rope you into an exercise routine."
emm "ฉันเลยไม่แปลกใจที่เอมิลากให้เธอมาออกกำลังกายเป็นประจำได้"

# emm "If Rin weren't just as stubborn as she is, I'm sure that Emi would have gotten her out and running with you too."
emm "ถ้ารินเขาไม่ได้เป็นคนรั้นแบบนั้นแล้วละก็เอมิคงไปลากให้มาวิ่งกับเธอได้ด้วยเหมือนกัน"

show emicas happy
with charachange

# emi "Oh, that reminds me! Rin says hello."
emi "อ้อ จริงด้วย! รินเขาฝากทักทายแม่ด้วยนะคะ"

scene bg emi_dining
with locationchange

# "I drift to the outer edges of the conversation again as we move into the dining room to eat."
"ฉันพาตัวเองออกจากบทสนทนาอีกครั้งระหว่างที่เดินไปห้องกินข้าวด้วยกัน"

# "It smells delicious in here, and the spread that Emi's mom has produced is impressive."
"ในห้องมีกลิ่นหอมอวลไปทั่ว ขนมปังหลากหน้าที่แม่เอมิทำนั้นก็ดูสุดยอดทีเดียว"

show meiko smile at tworight
show emicas happy_up at twoleft
with charaenter

# emi "Woah, you've made enough to feed an army in here!"
emi "โห นี่แม่ทำกะจะเปิดโรงทานหรือไงคะเนี่ย!"

show meiko happy
with charachange

# emm "Is it too much? Well, you can always take some leftovers with you when you go."
emm "เยอะไปเหรอจ๊ะ ยังไงถ้าเหลือก็ห่อกลับหอได้นะ"

# hi "That sounds great! I can only handle cafeteria food for so long. Something home-cooked would be a welcome change of pace."
hi "ก็ดีนะครับ! ผมเอียนกับข้าวที่โรงอาหารแล้ว ได้เปลี่ยนมากินกับข้าวที่ทำในครัวบ้านบ้างก็ดีเหมือนกัน"

show emicas smile
with charachange

# emi "What he said. Thanks, mom."
emi "ตามฮิซาโอะว่าเลยค่ะ ขอบคุณค่ะแม่"

# "The food tastes as good as it smells, and there's a lull in the conversation while we all dig in."
"อาหารนั้นอร่อยสมกับกลิ่นที่หอมหวน ระหว่างที่กินบทสนทนาก็ขาดช่วงไป"

# "Emi assaults her plate with the usual amount of gusto, and I will admit that I set a pretty fast pace myself."
"เอมิกินอาหารในจานตัวเองด้วยความรวดเร็วอย่างทุกที และขอยอมรับว่าฉันเองก็กินเร็วพอกัน"

show meiko wink
with charachange

# emm "So Hisao, I hear that you and my daughter here have gotten rather close, hmm?"
emm "จะว่าไป ฮิซาโอะ ฉันได้ยินมาว่าเธอค่อนข้างสนิทกับลูกสาวฉันแล้วนี่"

# "The urge to say something like “Not really” is so strong that I open my mouth to say it, but then reassert control."
"ฉันอยากจะพูดเหลือเกินว่า “ก็ไม่เชิงหรอกครับ” เสียจนอ้าปากจะพูดออกไปแล้วแต่ก็กลับมาคุมตัวเองได้อยู่"

# "We are close, there's no getting around it. I mean Emi's brought me here, hasn't she?"
"เราสนิทกัน ไม่มีคำว่าแต่ใด ๆ ทั้งนั้น ก็เอมิพาฉันมาถึงที่นี่เลยนี่"

# "Fortunately, both Emi and her mother seem to take my reaction as a sign that I'm caught off guard rather than considering saying something cruel."
"โชคดีที่ทั้งเอมิทั้งแม่ของเธอคิดว่าที่ฉันมีปฏิกิริยาเป็นอย่างนี้เพราะไม่ได้ตั้งตัวกับคำถาม ไม่ใช่เพราะกำลัง\nจะพูดอะไรโหดร้ายออกไป"

# hi "Heh, I suppose we have. I blame the morning runs, myself."
hi "ฮะ ๆ คงงั้นละนะครับ ผมว่าเป็นเพราะการวิ่งตอนเช้านั่นแหละ"

show emicas pout_up
with charachange

# emi "You make it sound like a bad thing, Hisao."
emi "นายพูดเหมือนมันไม่ดีเลยนะฮิซาโอะ"

show meiko smile
with charachange

# emm "Well, I for one found it a relief."
emm "อืม แต่แม่โล่งใจนะ"

# hi "Why's that?"
hi "ทำไมเหรอครับ"

show meiko worry
with charachange

# emm "Emi's always been a popular girl, but never made many close friends."
emm "เอมิเขาเนื้อหอมก็จริง แต่ไม่ค่อยมีเพื่อนสนิทเลย"

# "This is a bit of news to me. I've always seen Emi chatting with her classmates in the hallways."
"ไม่เคยรู้มาก่อนเลยนะเนี่ย ปกติก็เห็นคุยกับเพื่อนที่เรียนห้องเดียวกันอยู่ในโถงทางเดินตลอด"

# "And certainly the whole track team seems to love her, but it is true that she chooses to isolate herself during lunch with Rin and me."
"แล้วก็ชัดด้วยว่าคนทั้งทีมวิ่งต่างรักเอมิ แต่จริงอยู่ว่าเอมิเลือกที่จะปลีกตัวเองออกมาตอนเที่ยงเพื่อมากินข้าวกับริน\nแล้วก็ฉัน"

# "Not exactly the sort of behavior one expects from a popular girl, after all. Then again, I've experienced her unwillingness to get close firsthand, so I can't say I'm that surprised."
"ซึ่งเด็กสาวที่เนื้อหอมน่าจะไม่ทำตัวแบบนี้อยู่แล้ว แต่ก็นะ ฉันนี่แหละที่ได้สัมผัสความไม่อยากสนิทกับใครของเอมิ\nโดยตรงเลย จึงไม่ได้แปลกใจขนาดนั้น"

show meiko serious
with charachange

# emm "I was beginning to have my doubts."
emm "เห็นแบบนั้นฉันก็ชักกังวลใจ"

show emicas awayfrown_up
with charachange

# "Emi rolls her eyes to the ceiling and grumbles something I can't quite make out."
"เอมิกลอกตามองบนแล้วบ่นอุบอิบอะไรสักอย่างที่ฉันฟังไม่ค่อยออก"

stop music fadeout 1.0

# hi "Huh?"
hi "ฮะ?"

show emicas neutral_up
with charachange

# emi "What?"
emi "อะไร"

# hi "What's that you just said?"
hi "เมื่อกี้เธอว่าอะไร"

show emicas blush
with charachange

# emi "Nothing."
emi "เปล่า"

show meiko happy
with charachange

# "Mrs. Ibarazaki chokes on her drink with laughter."
"คุณนายอิบาราซากิหัวเราะจนสำลักน้ำ"

play music music_comedy fadein 0.5

# emm "You've been hanging out with the nurse too long, Emi."
emm "ลูกอยู่กับคุณพยาบาลบ่อยไปแล้วนะ"

# emm "I'm going to have to talk to him about corrupting my daughter."
emm "เดี๋ยวต้องเตือนคุณพยาบาลหน่อยว่าห้ามทำลูกสาวฉันติดนิสัยไม่ดีด้วย"

# hi "Somehow I don't think that would be very effective."
hi "ผมว่าบอกไปก็เท่านั้นละครับ"

show emicas evil
with charachange

# emi "I learned most of it from you anyway. Not the nurse."
emi "ฉันติดนิสัยหลายอย่างนายมามากกว่า ไม่ใช่คุณพยาบาลหรอก"

show meiko smile
with charachange

# emm "Don't listen to her, Hisao. She's a born liar."
emm "ไม่ต้องไปฟังหรอกนะจ๊ะฮิซาโอะ เอมิน่ะขี้โกหก"

show emicas awayfrown
with charachange

# emi "Hmph. Yeah right."
emi "ฮึ ใช่สิ"

# hi "Oh, I don't know, Emi. I think your mother has a point."
hi "โธ่ ไม่รู้สิเอมิ ฉันว่าแม่เธอก็พูดถูกนะ"

show emicas angry_up
with charachange

# emi "What? You traitor! You're supposed to take my side in this!"
emi "อะไรนะ เจ้าคนทรยศ! นายต้องเข้าข้างฉันสิ!"

# hi "Yeah, but you did lie about your leg after the meet—{w=0.3}{nw}"
hi "ก็ใช่ แต่ตอนหลังงานแข่งเธอก็โกหกเรื่องขาเธ—{w=0.3}{nw}"

with vpunch

# extend " ow!"
extend " โอ๊ย!"

# "A kick in the shins from an unmistakably plastic foot cuts me off, but not before Mrs. Ibarazaki's eyebrows shoot upwards."
"แรงจากเท้าพลาสติกเน้น ๆ ที่เตะเข้ากับหน้าแข้งฉันตัดบทฉันไป แต่คุณนายอิบาราซากิก็เลิกคิ้วขึ้น"

show meiko serious
with charachange

# emm "What about your leg?"
emm "ขาลูกเป็นอะไรเหรอ"

show emicas awayfrown
with charachange

# emi "It wasn't a big deal, that's all… I just was, er, inawheelchairforabit."
emi "ไม่ได้เป็นอะไรมากหรอกค่ะ พอดี… คือหนู เอ่อ ดั้ยนั่งวีนแชอยู่พักนึง"

# "The last few mumbled words are quickly deciphered by Emi's mother - I suspect she has experience with this sort of thing - and a worried frown appears on her face."
"แม่เอมิถอดความประโยคสุดท้ายที่เอมิพูดเสียงงึมงำได้ในทันที คงจะเคยเจอเรื่องแบบนี้มาแล้ว เธอขมวดคิ้ว\nด้วยความเป็นห่วง"

show meiko worry
with charachange

# emm "So that's why he kept dodging my calls…"
emm "เพราะแบบนี้สินะลูกถึงได้ไม่ยอมรับสาย…"

# emm "Oh Emi… I know how much you hate being in a wheelchair."
emm "โธ่เอมิ… แม่รู้ว่าลูกไม่ชอบนั่งวีลแชร์เลย"

# emm "No wonder you've been in such a mood lately!"
emm "มิน่าล่ะหมู่นี้ลูกถึงได้ซึมไป!"

show emicas frown
with charachange

# hi "Yeah, she's much happier on her feet, so to speak."
hi "ครับ หรือจะให้พูดก็คือเอมิจะมีความสุขมากกว่าตอนที่ไม่ต้องนั่ง"

show meiko serious
show emicas awayfrown
with charachange

# emm "Well of course! She spent enough time in a chair just after the accident."
emm "แน่อยู่แล้วสิ! แค่ช่วงหลังเกิดอุบัติเหตุเอมิก็ได้นั่งวีลแชร์จนเอือมแล้ว"

show emicas frown
with charachange

# hi "She didn't get prosthetics immediately?"
hi "ไม่ได้ใส่ขาเทียมเลยเหรอครับ"

show meiko worry
show emicas awayfrown
with charachange

# emm "No, she had to finish healing up before they'd let her start the sort of therapy you've got to go through to adjust to those things."
emm "ใช่ ต้องรอให้อาการดีขึ้นก่อนหมอถึงค่อยให้มาบำบัดปรับตัวให้ชินกับของพวกนี้"

# emm "Especially since she wanted to run on them."
emm "แล้วยิ่งเอมิอยากใส่ขาเทียมวิ่งด้วย"

show emicas frown
with charachange

# hi "I had no idea."
hi "เพิ่งรู้เลยนะครับเนี่ย"

show emicas weaksmile_up
with charachange

# emi "Yeah, it sucked. Oh, did you see Rin's mural at the festival?"
emi "ใช่ อึดอัดมาก อ้อ แม่เห็นภาพเขียนผนังของรินตอนงานเทศกาลหรือยังคะ"

# "Emi's sudden change of topic makes me realize belatedly that she's been fidgeting the whole time her mother and I have been talking."
"พออยู่ ๆ เอมิก็เปลี่ยนเรื่องฉันถึงเพิ่งรู้ตัวเอาตอนนี้ว่าเธอนั่งบิดตัวไปมาตลอดตอนที่แม่ของเธอคุยกับฉัน"

# "I should have figured on her being a little skittish when it comes to talking about the accident. Even around her mother."
"น่าจะรู้แต่แรกแล้วว่าเอมิจะกระอักกระอ่วนขึ้นมาพอพูดถึงเรื่องอุบัติเหตุ แม้จะอยู่กับแม่ก็ตาม"

show meiko serious
with charachange

# emm "No, I didn't make it out to the festival, remember?"
emm "ไม่จ้ะ ลูกลืมแล้วเหรอว่าแม่ไม่ได้ไปงานเทศกาลน่ะ"

show meiko happy
with charachange

# emm "Although I caught a glimpse of it at your track meet. It seemed pretty weird to me."
emm "แต่ตอนที่ไปงานแข่งวิ่งก็เห็นผ่าน ๆ อยู่นะ เป็นภาพที่ดูแปลก ๆ ดี"

show emicas closedsmile
with charachange

# emi "I think that's more or less what she was going for. She talked a lot about it being dreamlike. Or trying to make it dreamlike."
emi "หนูว่ารินก็คงตั้งใจให้เป็นอย่างนั้นแหละค่ะ เห็นพูดบ่อย ๆ ว่าเป็นภาพที่เป็นเหมือนฝัน หรือไม่ก็อยากวาด\nให้ดูเหมือนฝัน"

show meiko smile
with charachange

# emm "Rin's art is one of those things I don't think I'll ever understand."
emm "งานศิลปะของรินเป็นอะไรที่แม่คงไม่เข้าใจหรอกจ้ะ"

show emicas wink
with charachange

# emi "That's not surprising. I don't think Rin expects to be understood."
emi "ก็ไม่แปลกหรอกค่ะ รินคงไม่ได้คาดหวังให้ใครมาเข้าใจหรอก"

show emicas grin
with charachange

# emi "She told me once that art allows people to understand stuff they wouldn't understand otherwise, but all the same she doesn't think it actually works that way."
emi "รินเคยบอกหนูว่าศิลปะทำให้คนเข้าใจสิ่งที่ทำให้เข้าใจได้ด้วยศิลปะเท่านั้น แต่ถึงอย่างนั้นรินก็คิดว่าศิลปะ\nไม่ใช่อะไรอย่างนั้น"

# "I'm surprised that Emi's talked about this with Rin extensively enough to actually have Rin's opinion, such as it is."
"ไม่ต้องพูดถึงว่าเป็นเรื่องศิลปะหรอก ฉันแปลกใจที่เอมิคุยกับรินเรื่องอะไรสักอย่างได้ลึกพอที่จะรู้มุมมองของรินแบบนี้"

# "Although I expect that Rin could not, if she were so inclined, say the same thing about Emi's."
"แต่กลับกัน ฉันคาดว่าริน—ต่อให้อยากรู้จริง ๆ ก็—คงไม่ได้รู้มุมมองของเอมิหรอก"

# "Unless, of course, Emi is purposely keeping me in the dark about everything; which is likely, but unpleasant to think about."
"แน่ละว่าเว้นเสียแต่เอมิจะจงใจไม่บอกอะไรทุกอย่างกับฉัน ซึ่งก็เป็นไปได้ แต่ไม่อยากคิดแบบนั้นเลย"

# "I drift down this unpleasant train of thought for a while, losing track of the conversation."
"ฉันคิดอะไรชวนหนักใจเช่นนั้นไปครู่หนึ่งจนไม่ได้ฟังบทสนทนาตรงหน้า"

show meiko serious
with charachange

# emm "Hey Emi, I've been meaning to ask…"
emm "นี่เอมิ แม่ว่าจะถามลูก…"

show emicas neutral
with charachange

# emi "Huh?"
emi "คะ?"

show meiko worry
with charachange

# emm "Are you going to visit your father this year?"
emm "ปีนี้ลูกจะไปเยี่ยมคุณพ่อหรือเปล่า"

stop music fadeout 3.0

# "From the way she says it, you'd think Emi's mother was talking about the weather. From the way Emi reacts, it's clearly not the weather they're talking about."
"ฟังจากน้ำเสียงแล้วเหมือนแม่เอมิพูดถึงเรื่องดินฟ้าอากาศเฉย ๆ แต่ดูจากปฏิกิริยาของเอมิแล้วก็รู้ว่าไม่ได้คุยกัน\nเรื่องดินฟ้าอากาศแน่นอน"

show emicas awayfrown
with charachange

# "She flinches, a slight jerk of the head backwards as if she's just been slapped in the face."
"เธอผงะกระตุกหัวไปข้างหลังเล็กน้อยเหมือนโดนตบหน้า"

show emicas sad
with charachange

# emi "Can we talk about this later?"
emi "ไว้คุยเรื่องนี้กันทีหลังได้มั้ยคะ"

# "Her voice sounds brittle, strained. It looks as if she's been severely shaken by the question."
"เป็นน้ำเสียงที่ฟังดูเปราะบางและเกร็งราวกับว่าสะเทือนใจกับคำถามนั้นมาก"

# "It seems that Mrs. Ibarazaki misjudged just how close Emi and I are."
"ดูท่าว่าคุณนายอิบาราซากิจะประเมินความสนิทของเราพลาด"

# "Some things, it seems, are best not conversed about with me around. Her father is one of these things."
"เท่าที่เห็น บางอย่างก็ไม่ใช่เรื่องที่ควรคุยตอนฉันอยู่ด้วย ซึ่งหนึ่งในนั้นก็คือเรื่องของพ่อเอมิ"

# "The accident that took her legs is probably another one of those things, if her reaction to the earlier conversation between her mother and myself is any indication."
"อีกเรื่องก็คงจะเป็นอุบัติเหตุที่ทำให้เอมิต้องเสียขาไป ดูจากปฏิกิริยาของเอมิที่เห็นตอนแม่ของเธอคุยกับฉันน่ะนะ"

# "It doesn't take Emi's mother long to realize she's screwed up."
"ไม่นานนักแม่เอมิก็รู้ตัวว่าทำพลาดไปเสียแล้ว"

show meiko happy
with charachange

# emm "Of course we can, dear. I'm sorry to bring it up, I just wanted to ask so I could make plans—"
emm "ได้สิจ๊ะลูก ขอโทษที่คุยเรื่องนี้นะ แม่แค่อยากถามไว้ก่อน จะได้เตรียม—"

show emicas neutral
with charachange

# emi "It's fine. Don't worry about it."
emi "ไม่เป็นไรหรอกค่ะ ไม่ต้องคิดมากหรอก"

# "Emi fidgets nervously, as if embarrassed by her own reaction. I confess that her reaction is confusing."
"เอมิบิดตัวไปมาด้วยความประหม่าคล้ายอายที่เมื่อครู่ทำตัวไปอย่างนั้น ขอยอมรับว่าฉันสับสนกับท่าทีเธอเหลือเกิน"

# "She only just mentioned her father to me earlier today! Less than a few hours ago, even!"
"ก็วันนี้เอมิเพิ่งพูดถึงพ่อตัวเองไปหยก ๆ ! ผ่านมาไม่ถึงสองสามชั่วโมงด้วยซ้ำ!"

# "Why does a simple question about when she'll visit her father cause such a strong reaction?"
"ทำไมคำถามง่าย ๆ แค่ว่าจะไปเยี่ยมคุณพ่อตอนไหนถึงได้ทำให้เอมิทำท่าทางขนาดนั้น"

# "Unless whatever serenity she claimed to have reached by means of our talk the previous evening has suddenly evaporated."
"เว้นเสียแต่ว่าสภาวะใจสงบอะไรก็ช่างที่เอมิบอกว่ารู้สึกได้เพราะเราคุยกันตอนเย็นเมื่อวานนั้นอยู่ ๆ ก็สลายหายไปแล้ว"

# "Or it didn't help as much as she thought. Or claimed."
"หรืออาจจะไม่ได้เป็นประโยชน์มากอย่างที่เอมิคิด หรืออย่างที่พูดไว้"

show emicas weaksmile
with charachange

# emi "I'll uh, be right back. Gotta visit the little girl's room."
emi "เดี๋ยว เอ่อ หนูมานะคะ ไปเข้าห้องน้ำ"

hide emicas
with charaexit

show bg emi_dining at bgleft
show meiko smile at center
with dissolvecharamove

# "Emi gets up suddenly and leaves the table, leaving me and Mrs. Ibarazaki alone."
"อยู่ ๆ เอมิก็ลุกไปจากโต๊ะทิ้งให้ฉันอยู่กับคุณนายอิบาราซากิตามลำพัง"

# "I'm a little conflicted. Should I go after her, or should I stay here?"
"ตอนนี้ฉันเลือกไม่ถูกว่าจะตามเอมิไปหรือนั่งอยู่ตรงนี้ดี"

# "It's obvious that Emi's departure was not based on the call of nature. Something's bothering her, and I have to know what it is."
"ชัดว่าที่เอมิไปไม่ใช่เพราะอยากเข้าห้องน้ำแน่นอน มีเรื่องกวนใจเอมิอยู่ และฉันก็ต้องรู้ให้ได้ว่าเรื่องอะไร"

#choice time, kiddies. Well, assuming you talked to Mutou. If you didn't you'll default to 1) Go after her! and not 2) Talk to Emi's mom

label th_choiceE26:
menu:
    with menueffect

    # "How to go about it?"
    "เอายังไงดี"

    # "Go after her.":
    "ตามเอมิไป":
        return m1

    # "Talk to her mom.":
    "คุยกับแม่เอมิ":
        return m2

label th_E26c:

#if you go after her

# "The only way to find out is to go to the source. And the source is currently pretending that she has to use the toilet."
"ทางเดียวที่จะรู้ได้คือต้องตามต้นทางไป และต้นทางที่ว่านั้นตอนนี้ทำเป็นว่าต้องไปเข้าห้องน้ำอยู่"

scene bg emi_kitchen
with locationchange

# "I excuse myself politely from the table and head that way, only to catch sight of Emi not in the bathroom, but in the kitchen just next to the living room."
"ฉันพูดขอตัวอย่างสุภาพก่อนจะเดินตามทางที่เอมิออกไปจนมาเจอกับเธอที่ไม่ได้อยู่ในห้องน้ำแต่อยู่ในครัว\nข้างห้องนั่งเล่น"

show emicas sad
with charaenter

# "Emi's left the door open, and as I approach I can see that she's holding on to the table in an attempt to compose herself, an effort that fails as soon as I open my mouth."
"เอมิเปิดประตูทิ้งไว้ พอเข้าไปดูใกล้ ๆ ก็เห็นว่ากำลังจับโต๊ะเป็นการสงบใจตัวเองอยู่ ซึ่งก็ต้องล้มเหลวเมื่อฉันเปิดปาก"

# hi "Doesn't look like nature's call was that urgent."
hi "ดูท่าว่าจะไม่ได้อยากเข้าห้องน้ำขนาดนั้นนะ"

show emicas angry
with charachange

# "Emi jumps and glares at me."
"เอมิสะดุ้งแล้วจ้องมาทางฉัน"

show emicas angry_up
with charachange

# emi "What are you doing here? I didn't come here to be with other people."
emi "มาทำอะไรที่นี่ ฉันอุตส่าห์หนีคนมาอยู่ตรงนี้"

# hi "I just wanted to help you. You looked pretty rattled."
hi "ฉันแค่อยากช่วยเธอ เห็นเธอตระหนกแบบนั้นน่ะ"

show emicas awayfrown
with charachange

# emi "I said it was nothing, didn't I? And besides, I thought we'd established that you can't help me."
emi "ฉันก็บอกแล้วไงว่าไม่มีอะไร แล้วอีกอย่าง เราคุยกันแล้วไม่ใช่เหรอว่านายช่วยฉันไม่ได้หรอก"

# hi "No, we've established that you're stubborn."
hi "ไม่ เราคุยกันแล้วว่าเธอดื้อต่างหาก"

show emicas angry
with charachange

# emi "Look who's talking. The guy who followed me."
emi "แล้วไอ้คนพูดล่ะ ตามฉันมาถึงนี่เนี่ย"

# hi "This is different! I want to help you with… whatever this is."
hi "ไม่เหมือนกันสักหน่อย! ฉันอยากช่วยเธอเรื่อง… อะไรก็ช่างที่เป็นปัญหาตอนนี้"

show emicas awayfrown
with charachange

# emi "Funny, because {b}I{/b} just want you to leave me alone."
emi "โคตรจะตลก {b}ฉัน{/b}ก็บอกว่าไม่อยากให้นายมายุ่งกับฉันไปหยก ๆ"

# hi "But why? Why can't you just trust me?"
hi "แต่ทำไมล่ะ ทำไมเธอถึงเชื่อใจฉันไม่ได้"

show emicas frown
with charachange

# emi "We've been over this already, Hisao. I've got to deal with this stuff on my own."
emi "เราคุยเรื่องนี้กันแล้วนะฮิซาโอะ ฉันต้องจัดการกับเรื่องนี้ตัวคนเดียว"

# hi "I won't accept that! You need my help, you just won't take it!"
hi "ฉันไม่ยอมหรอก! เธอน่ะต้องการความช่วยเหลือจากฉัน เธอแค่ไม่ยอมรับไว้เฉย ๆ !"

# "My wording seems to have been a little off."
"คำพูดของฉันฟังดูแปร่ง ๆ"

show emicas angry
with charachange

# emi "Need? I {b}need{/b} your help?"
emi "ต้องการเหรอ ฉันเนี่ยนะ{b}ต้องการ{/b}ความช่วยเหลือจากนาย"

play music music_tragic fadein 0.5

show emicas angry_up
with charachange

# emi "Well, it's a good thing we met, isn't it? Because otherwise I guess I'd just be a broken human being, wouldn't I?"
emi "โอเค ดีจังเลยเนอะที่เราได้มาเจอกัน เพราะไม่งั้นฉันก็คงเป็นแค่คนที่แหลกสลายคนหนึ่ง เนอะ"

# emi "No, it's a damn good thing that Hisao came along to save the day, isn't it? Because God knows I can't save myself, can I?"
emi "ไม่ ๆ ดีเท่าไหร่แล้วที่ฮิซาโอะเสด็จมาช่วยฉันน่ะ เพราะฉันน่ะช่วยเหลือตัวเองไม่ได้เลย เนอะ"

# emi "I'm just the poor, emotionally damaged girl with no legs, right?"
emi "ฉันมันก็แค่เด็กสาวไม่มีขาซึ่งบอบช้ำทางจิตใจผู้น่าสงสาร เนอะ"

# hi "Emi, you know I don't think that—"
hi "เอมิ เธอก็รู้ว่าฉันไม่ได้คิด—"

show emicas angry
with charachange

# emi "Really? Because if you thought differently then I don't think you'd be here, saying I need your help."
emi "จริงเหรอ ถ้านายไม่คิดแบบนั้นแล้วฉันว่านายไม่น่ามาอยู่ตรงนี้แล้วบอกว่าฉันต้องการความช่วยเหลือจากนาย\nหรอกนะ"

# emi "I've gotten pretty far in life as a normal human being without you."
emi "ฉันก็ใช้ชีวิตอย่างมนุษย์ปกติสามัญมาได้จนป่านนี้โดยไม่มีนาย"

# hi "So what, nothing we've shared was important? I'm just the guy who hangs out with you?"
hi "แล้วยังไง ระหว่างเรามันไม่มีความหมายเลยเหรอ ฉันมันก็แค่คนที่อยู่กับเธอว่างั้น?"

show emicas awayfrown
with charachange

# emi "You're my boyfriend, Hisao, not my savior."
emi "นายเป็นแฟนฉันนะฮิซาโอะ ไม่ใช่ผู้ที่จะมาช่วยชีวิตฉัน"

# hi "Well no, that much is obvious. You won't even consider that I could be a help to you, will you?"
hi "ก็ใช่ อันนั้นน่ะชัดอยู่แล้ว เธอคิดว่าฉันจะช่วยอะไรเธอไม่ได้เลยงั้นสิ"

# hi "You'll just bottle it all up and hope that a run will solve your problems, or you'll come visit me and we'll fool around until you feel better."
hi "เธอจะเก็บปัญหานั้นไว้กับตัวเองแล้วหวังเอาว่าการวิ่งจะช่วยแก้ปัญหาของเธอได้ หรือไม่ก็จะแวะมาหาฉัน\nแล้วก็สนุกด้วยกันไปจนกว่าเธอจะรู้สึกดีขึ้นงี้เหรอ"

# hi "That's not being a healthy human being, Emi. That's not what a relationship means."
hi "มนุษย์ปกติเขาไม่ทำแบบนั้นกันหรอกนะเอมิ ความรักความสัมพันธ์น่ะมันไม่ได้หมายความแบบนั้น"

show emicas frown
with charachange

# emi "Well it's what it means to me right now, Hisao."
emi "แต่ตอนนี้สำหรับฉันความรักความสัมพันธ์มันหมายความแบบนั้นแหละฮิซาโอะ"

show emicas sad
with charachange

# emi "I wish—"
emi "ฉันละอยาก—"

# "She seems to reconsider her words just then. A flicker of pain, of doubt on her face. For a moment I think she's about to cry."
"อยู่ ๆ เอมิก็ทำท่าชั่งใจคิดคำพูดตัวเองใหม่ เธอทำหน้าเจ็บปวดและเคลือบแคลงขึ้นมาแวบหนึ่งจนฉันคิดว่าเธอ\nจะร้องไห้แล้ว"

show emicas frown
with charachange

# "But the moment passes, and now she's composed herself again. Whatever that wish was will have to go unspoken."
"แต่ชั่วขณะนั้นก็ผ่านไป เอมิกลับมาตั้งสติได้แล้ว ความอยากอะไรก็ช่างนั้นจะไม่มีวันหลุดออกมาจากปากอีก"

# emi "Look, I just… I can't do this right now."
emi "คือ ฉันแค่… ตอนนี้ฉันไม่ไหว"

# hi "What, have a serious conversation? Be open? Be honest? Give a damn about anyone besides yourself and your problems?"
hi "ไม่ไหวอะไร คุยจริงจังไม่ไหว? เปิดใจไม่ไหว? พูดตรง ๆ ไม่ไหว? สนใจคนอื่นนอกจากตัวเองกับปัญหาของตัวเอง\nไม่ไหว?"

show emicas angry_up
with charachange

# emi "What do you know about my problems? Nothing! You don't know what I've been through, so don't pretend that you do."
emi "แล้วนายรู้เรื่องอะไรปัญหาของฉันบ้างล่ะ ไม่รู้เลยไง! นายไม่รู้ว่าฉันต้องผ่านอะไรมาบ้าง อย่ามาทำรู้ดี\nไปหน่อยเลย"

# hi "I know you have nightmares, and I know your father's gone. What happened to him?"
hi "ฉันรู้ว่าเธอฝันร้าย แล้วก็รู้ด้วยว่าพ่อเธอไม่อยู่แล้ว เกิดอะไรขึ้นกับพ่อเธอล่ะ"

show emicas sad_up
with charachange

# "Emi's head jerks backwards as if I've just slapped her. That brittle quality has gotten back into her voice."
"คอเอมิกระตุกไปข้างหลังราวกับว่าฉันตบหน้าเธอ ความเปราะบางนั้นกลับมาแทรกตัวในน้ำเสียงเอมิ"

show emicas sad
with charachange

# emi "That's enough."
emi "พอสักที"

# "This is stupid. This whole conversation has just been variations on Emi stonewalling me."
"งี่เง่าสิ้นดี แต่ละประโยคในบทสนทนาที่ผ่านมานี้ต่างก็เป็นแค่การที่เอมิตั้งกำแพงใส่ฉันแต่เป็นคนละแบบกันเฉย ๆ"

# hi "What, you won't even answer that question? Fine, keep your secrets. They can lie in the grave as far as I'm concerned."
hi "อะไร แค่จะตอบเรื่องนั้นยังไม่ตอบเลยเหรอ ก็ได้ เชิญตามสบาย ให้ความลับมันตาย ๆ ไปกับเธอเสียเถอะ"

show emicas blush
with charachange

# "Emi's eyes widen in shock. When she speaks again, it's in a voice that is low, dangerous."
"เอมิตาเบิกโพลงด้วยความตกใจ พอเธอเปิดปากพูดอีกครั้งก็เป็นเสียงทุ้มต่ำที่ฟังดูน่ากลัว"

show emicas grit
with charachange

# emi "Get out of my house, Hisao."
emi "ออกไปจากบ้านฉันเลยนะฮิซาโอะ"

# "The sudden change in her tone snaps me out of my self-righteous anger and makes me realize with a dawning horror what I've just said."
"น้ำเสียงเอมิที่เปลี่ยนไปกะทันหันนั้นทำให้ฉันได้สติหลุดจากความโทสะซึ่งเกิดจากความถือดีของตัวเอง และทำให้ฉัน\nพรั่นพรึงขึ้นมาเมื่อระลึกถึงสิ่งที่ตัวเองได้พูดออกไป"

# hi "Emi, I didn't mean—"
hi "เอมิ ฉันไม่ได้ตั้งใจจะ—"

stop music fadeout 2.0

show emicas angry
with charachange

# emi "I said {b}go{/b}, Hisao."
emi "ฉันบอกให้{b}ไป{/b}ไง ฮิซาโอะ"

# emi "Tell my mother that she cooked a wonderful meal but you've forgotten a prior engagement, and get out of my house."
emi "บอกแม่ด้วยว่าอาหารอร่อยมาก แต่ลืมไปว่ามีธุระที่นัดไว้แล้ว แล้วก็ออกไปจากบ้านฉันเสีย"

# "She's trembling now, shaking with anger, or sadness, or determination. Her voice is still low, controlled. Almost a growl."
"เอมิตัวสั่นด้วยความโกรธ ไม่ก็ความเศร้า ไม่ก็ความแน่วแน่ เธอยังกดเสียงต่ำไว้จนคล้ายเสียงสัตว์ตอนขู่"

# "I reach out to put an arm on her shoulder, to apologize for going too far, but she jerks away from my touch."
"ฉันยื่นมือจะไปวางไว้ที่บ่าเอมิเป็นการขอโทษที่พูดแรงเกินไป แต่เธอก็สะบัดตัวหนี"

show emicas angry_up
with charachange

# emi "Get out."
emi "ออกไป"

show bg emi_dining at bgleft
show meiko serious at center
with locationchange

# "What can I do? I walk out of the kitchen and go to the living room, make my apology to Mrs. Ibarazaki, and let myself out."
"แล้วจะให้ทำยังไงได้ ฉันเดินออกจากครัวมาที่ห้องนั่งเล่นแล้วขอโทษคุณนายอิบาราซากิก่อนเดินออกบ้าน"

$ suppress_window_after_timeskip = True

scene black
with dissolve

#You'd then dump to e27, you naughty child.

#Ah, but what if you chose to Talk to Emi's Mom?  Well, you'd see this:

label th_E26d:

# "There's an awkward silence at the table for a while after Emi dashes off. I can't think of anything to say."
"พอเอมิออกไปแล้วก็มีความเงียบอันน่าอึดอัดอยู่พักหนึ่ง ฉันไม่รู้จะพูดอะไรดี"

show meiko serious
with charachange

# "Emi's mother sighs, breaking the silence."
"แม่เอมิถอนหายใจก่อนจะทำลายความเงียบ"

play music music_moonlight fadein 5.0

# emm "Sorry about that, Hisao. I sometimes forget that Emi's touchy about certain subjects."
emm "ขอโทษด้วยนะจ๊ะฮิซาโอะ บางทีฉันก็ลืมว่าเอมิเขาอ่อนไหวกับเรื่องพวกนี้"

# emm "And I was talking about the wheelchair thing, too…"
emm "แล้วยังไปพูดถึงวีลแชร์อีก…"

# hi "Should I go after her?"
hi "ให้ผมตามไปมั้ยครับ"

show meiko worry
with charachange

# emm "Heavens no! She didn't leave the table to continue the conversation, you know."
emm "อย่านะจ๊ะ! ที่เอมิลุกไปจากโต๊ะก็เพราะไม่อยากคุยต่อนั่นแหละจ้ะ"

# hi "But if she's troubled, shouldn't someone help her?"
hi "แต่ถ้ามีเรื่องอะไรกวนใจอยู่ก็ต้องมีคนช่วยหรือเปล่าครับ"

show meiko serious
with charachange

# emm "If it were anyone else, I'd say yes. But my daughter is stubborn as a mule, and if she wants to be alone it's best to let her be alone."
emm "ถ้าเป็นคนอื่นฉันก็คงบอกแบบนั้นแหละจ้ะ แต่ลูกสาวฉันน่ะหัวแข็งยิ่งกว่าอะไรดี ถ้าเอมิอยากอยู่คนเดียว\nก็ปล่อยให้อยู่คนเดียวนั่นแหละจ้ะดีที่สุดแล้ว"

# emm "Otherwise she'll probably say something she'd regret, which would cause you to say something you'd regret, and I would prefer that dinner doesn't end with one or the both of you storming out of the house."
emm "ไม่อย่างนั้นเอมิก็คงจะพูดอะไรที่เดี๋ยวคงนึกเสียใจทีหลังอีก ซึ่งก็จะทำให้เธอพูดอะไรแบบนั้นเหมือนกัน\nแล้วฉันก็ไม่อยากให้มื้อเย็นครั้งนี้ต้องจบลงด้วยการที่เธอสักคนหรือทั้งสองคนเดินฮึดฮัดออกจากบ้านไป"

show meiko happy
with charachange

# emm "If that were to happen I'd be a terrible hostess, wouldn't I? I've already acted as a fool once today."
emm "ถ้าเป็นอย่างนั้นแล้วฉันก็คงไม่ใช่เจ้าบ้านที่ดีเลย วันนี้ฉันเองก็ทำตัวไม่รอบคอบไปแล้วหนหนึ่ง"

# hi "That's okay, I shouldn't have brought up the wheelchair, apparently."
hi "ไม่เป็นไรหรอกครับ เป็นผมมากกว่าที่ไม่น่าพูดเรื่องวีลแชร์ก่อน"

show meiko serious
with charachange

# "Mrs. Ibarazaki frowns, clearly more bothered by Emi's omission than she'd let on."
"คุณนายอิบาราซากิย่นคิ้ว ชัดว่ากังวลที่เอมิไม่อยู่แต่ไม่ยอมพูด"

# emm "I wish she wouldn't do that. It just makes me worry more, you know."
emm "ฉันไม่อยากให้เอมิทำแบบนี้เลย เพราะฉันจะยิ่งเป็นห่วงไปอีก"

# hi "She does this often?"
hi "เอมิทำแบบนี้ประจำเหรอครับ"

show meiko smile
with charachange

# emm "What, running off to the bathroom? No, I can't say she does. Keep injuries from her mother, though? Well, that's a little more common."
emm "หมายถึงอะไรล่ะ หนีไปเข้าห้องน้ำน่ะเหรอ ไม่น่าทำประจำหรอก แต่ถ้าเป็นการไม่ยอมบอกว่าตัวเองเป็นอะไร\nให้แม่ฟังแล้วละก็อันนี้บ่อยอยู่จ้ะ"

# emm "Every time I catch her lying like that, she assures me that the only reason she didn't tell me is because it wasn't a big deal."
emm "พอจับโกหกได้ทีไรเอมิก็บอกว่าที่ไม่ยอมบอกก็เพราะไม่ใช่เรื่องใหญ่อะไรมากเท่านั้นเอง"

# hi "If it's any consolation, I'm sure the only reason I knew about it at all was because I saw her every day."
hi "ผมจะบอกอะไรให้นะครับ ผมว่าที่ผมได้รู้นี่ก็เพราะต้องเจอกับเอมิทุกวันนั่นแหละ"

show meiko happy
with charachange

# "This elicits a dry chuckle from across the table. Mrs. Ibarazaki sighs, a little sadly."
"คุณนายอิบาราซากิฟังแล้วแค่นหัวเราะแห้ง ๆ ก่อนจะถอนหายใจเศร้า ๆ"

show meiko smile
with charachange

# emm "Still hesitant about getting close to people, huh? I keep hoping that she'll get over that."
emm "ยังไม่ยอมสนิทกับคนอื่นงั้นเหรอ ฉันก็หวังอยู่ตลอดว่าเอมิจะเลิกทำตัวแบบนั้นสักที"

# emm "It's funny, really. She's bounced back so well from the accident in so many ways…"
emm "ซึ่งก็ตลกนะ เพราะในหลายแง่เอมิก็ฟื้นตัวจากอุบัติเหตุครั้งนั้นได้เป็นอย่างดีเลย…"

show meiko serious
with charachange

# emm "I guess some things never really go away."
emm "บางอย่างมันก็เปลี่ยนแปลงกันไม่ได้ละนะ"

# "From the looks of it, the whole thing still bothers her, too."
"ดู ๆ แล้วเรื่องนี้ก็ยังกวนใจแม่เอมิอยู่เหมือนกัน"

# "She seems to be a little more willing to talk about the accident without Emi around, though."
"แต่พอเอมิไม่อยู่แล้วดูพร้อมที่จะคุยเรื่องอุบัติเหตุขึ้นมาอีกหน่อย"

# hi "Hey, I've got a question, if it's all right."
hi "เอ่อ ถ้าไม่ว่าอะไร ผมขอถามอะไรหน่อยได้มั้ยครับ"

show meiko smile
with charachange

# emm "Oh?"
emm "จ๊ะ?"

# hi "What else did Emi lose in that accident? The nurse said that she gets this way near the anniversary, and she won't talk about it to me…"
hi "ตอนอุบัติเหตุครั้งนั้นเอมิเสียอะไรไปอีกเหรอครับ คุณพยาบาลบอกว่าพอใกล้ถึงวันครบรอบแล้วเอมิจะเป็นแบบนี้ตลอด\nแล้วเอมิก็ไม่ยอมคุยเรื่องนี้กับผมเลย…"

show meiko happy
with charachange

# emm "So you thought I'd fill you in, hmm?"
emm "คิดว่าฉันคงจะเล่าให้เธอฟังได้สินะ หืม"

# hi "Er, yeah. Hopefully."
hi "เอ้อ ครับ หวังว่านะครับ"

show meiko serious
with charachange

# emm "Well, there's a problem with that request, you know."
emm "โอเค แต่ฉันเล่าไม่ได้เพราะติดอยู่อย่างหนึ่ง"

# hi "Let me guess: you promised Emi that you wouldn't tell anyone she didn't want to know, and you don't know if she wants me to know?"
hi "ให้เดานะครับ เพราะรับปากกับเอมิไว้แล้วว่าจะไม่บอกให้กับคนที่เอมิไม่อยากให้รู้ แล้วตอนนี้ก็ไม่รู้ว่าเอมิ\nจะอยากให้ผมรู้หรือเปล่า"

# emm "Something like that. I promised Emi that she'd be the one to tell people the full story."
emm "ประมาณนั้นจ้ะ ฉันรับปากกับเอมิไว้แล้วว่าจะให้เจ้าตัวเป็นคนเล่าเรื่องนี้กับคนอื่นตรง ๆ เท่านั้น"

# hi "But isn't that important? I mean, it's clearly had a huge effect on her if she's still like this so long after the accident happened."
hi "แต่มันก็เรื่องสำคัญนี่ครับ คือยังไงก็ต้องเป็นเรื่องที่มีผลกับเอมิแน่นอนถ้าผ่านมานานขนาดนี้แล้วเอมิยังเป็น\nแบบนั้นอยู่"

show meiko worry
with charachange

# emm "That's true. It did have a long-lasting effect on her. There are a few things that she'll probably never really get over."
emm "ก็จริงจ้ะ เป็นเหตุการณ์ที่มีผลติดตัวเอมิเลย กับเรื่องบางเรื่องเอมิก็คงทำใจไม่ได้จริง ๆ นั่นแหละจ้ะ"

# "For a moment Mrs. Ibarazaki looks incredibly saddened, as if an old wound is bothering her."
"คุณนายอิบาราซากิทำหน้าเศร้าสร้อยหนักขึ้นมาครู่หนึ่งราวกับว่าเจ็บจากแผลเก่า"

# emm "I suppose there are a few things I'll never really get over either…"
emm "แล้วก็คงมีเรื่องบางเรื่องที่ฉันทำใจไม่ได้เหมือนกัน…"

show meiko happy
with charachange

# "Another dry chuckle, and with a shake of her head Emi's mother banishes the memory."
"แม่เอมิแค่นหัวเราะอีกรอบแล้วสั่นหัวคล้ายสลัดความทรงจำนั้นออกไป"

show meiko smile
with charachange

# emm "Look, there's something you absolutely must understand about the way Emi thinks about the accident."
emm "นี่นะ เธอต้องเข้าใจก่อนว่าเอมิมองอุบัติเหตุครั้งนั้นว่ายังไง"

# hi "What's that?"
hi "ยังไงเหรอครับ"

# emm "It wasn't a big deal."
emm "มองว่าไม่ใช่เรื่องใหญ่"

stop music fadeout 1.0

# "Somehow I manage to keep my mouth from falling open in surprise, but it takes some effort."
"ไม่รู้ทำไมฉันถึงยังปิดปากไม่ให้เปิดหวอด้วยความตกใจได้ แต่ก็ต้องห้ามใจอยู่เหมือนกัน"

# "That has to be the most ridiculous thing I've ever heard."
"เป็นประโยคที่บ้าบอที่สุดเท่าที่เคยได้ยินมาเลย"

# hi "I beg your pardon?"
hi "อะไรนะครับ"

play music music_sadness fadein 3.0

show meiko serious
with charachange

# emm "Okay, maybe it's not that simple, but it's a pretty accurate summation. Emi believes that the accident did not define her, and that everything she lost that day didn't define her either."
emm "โอเค อาจจะมีอะไรซับซ้อนกว่านั้น แต่รวม ๆ ก็ประมาณนั้นแหละจ้ะ เอมิเชื่อว่าอุบัติเหตุครั้งนั้นไม่ใช่\nสิ่งที่จะมานิยามตัวเอง และทุกสิ่งที่เสียไปในวันนั้นก็ไม่ใช่สิ่งที่จะมานิยามตัวเองเหมือนกัน"

# emm "She's not “that girl who lost her legs,” she's “The Fastest Thing on No Legs.” Her optimism and energy came out of that wreck without a scratch, as far as she's concerned."
emm "เอมิไม่ใช่ “เด็กสาวที่สูญเสียขาไป” เอมิคือ “สิ่งไม่มีขาที่เร็วที่สุด” ทั้งความมองโลกในแง่บวกทั้งพลังของเอมิ\nรอดมาจากอุบัติเหตุนั้นได้อย่างครบถ้วนสมบูรณ์ เอมิเขาคิดแบบนั้น"

# hi "Yet it goes beyond that, doesn't it? I mean, last night she told me that she refused to rely on me because it would make losing me too painful."
hi "แต่มันก็มีอะไรมากกว่านั้นใช่มั้ยครับ เมื่อคืนเอมิก็บอกผมว่าที่ไม่ยอมพึ่งผมก็เพราะถ้าต้องเสียผมไปอีกก็คง\nเจ็บปวดเกินรับได้"

show meiko smile
with charachange

# emm "Not really. You said she won't tell you about the accident, even though you've asked her about it before."
emm "ไม่เชิงจ้ะ เธอบอกเองว่าเอมิไม่ยอมเล่าเรื่องอุบัติเหตุให้ฟังทั้งที่เธอเคยถามแล้ว"

# emm "The reason she won't talk about it when you ask is because to her it's not something you absolutely need to know. Even if she wasn't terrified of getting too close to anyone, she still wouldn't talk about it."
emm "ที่เอมิไม่ยอมเล่าตอนเธอถามก็เพราะเอมิมองว่าเป็นเรื่องที่เธอไม่ได้จำเป็นต้องรู้ ต่อให้เอมิไม่ได้กลัว\nการสนิทกับใครแล้วก็คงไม่เล่าอยู่ดี"

# hi "She's afraid of being close to me?"
hi "เอมิกลัวการสนิทกับผมเหรอครับ"

show meiko happy
with charachange

# emm "Oh goodness me, yes. For all that talk about being unscathed by the accident, she's gained the ugly knowledge of how quickly it can all be over."
emm "ตายจริง ใช่จ้ะ ถึงจะบอกว่ารอดมาจากอุบัติเหตุครั้งนั้นได้ไม่เป็นอะไร แต่เอมิก็ได้รู้ซึ้งว่าทุกอย่างจะหายวับ\nไปกับตาได้ง่าย ๆ เลย"

show meiko smile
with charachange

# emm "So she's not going to let people get especially close to her, and she certainly would resent any implication that she cannot work through this on her own."
emm "เพราะงั้นเอมิถึงไม่ได้ให้ใครมาสนิทด้วยเป็นพิเศษ และเอมิก็คงไม่ชอบใจแน่ถ้ารู้สึกว่าจัดการกับเรื่องนี้\nด้วยตัวเองไม่ได้"

# hi "But I don't think she {b}can{/b}."
hi "แต่ผมว่าเอมิทำแบบนั้น{b}ไม่ได้{/b}หรอกนะครับ"

show meiko serious
with charachange

# emm "Oh no? Are you sure you've been dating my daughter and not somebody else? Trust me Hisao, she could get through it on her own."
emm "ตายแล้ว นี่เธอแน่ใจใช่มั้ยจ๊ะว่าคบกับลูกสาวฉันอยู่ ไม่ได้ไปคบกับคนอื่นน่ะ เชื่อฉันสิฮิซาโอะ เอมิรับมือ\nกับเรื่องนี้ด้วยตัวเองได้แน่นอน"

# hi "But she has nightmares, and can't sleep well, and—"
hi "แต่เอมิฝันร้ายจนนอนไม่หลับ แถม—"

show meiko smile
with charachange

# emm "And she does this every year. Tell me, if she wasn't able to get through it on her own, do you really think she'd still be alive? She would've killed herself, or something equally melodramatic."
emm "แถมเป็นแบบนี้ทุกปี ขอถามนะฮิซาโอะ ถ้าเอมิรับมือกับเรื่องนี้ด้วยตัวเองไม่ได้ เอมิจะยังมีชีวิตอยู่มาจนทุกวันนี้\nหรือเปล่า ไม่งั้นก็คงฆ่าตัวตายหรือทำอะไรอย่างละครน้ำเน่าไปแล้ว"

# hi "So what, I shouldn't try to help her?"
hi "แล้วยังไงครับ คือจะให้ผมอยู่เฉย ๆ ว่างั้น?"

show meiko serious
with charachange

# emm "I didn't say that! I hate seeing my daughter like this, and knowing that she could rely on someone else would let me relax."
emm "ฉันไม่ได้พูดแบบนั้นสักหน่อย! ฉันก็ไม่อยากเห็นลูกสาวตัวเองเป็นแบบนี้หรอก ถ้ามีคนที่เอมิพึ่งได้ฉันก็คง\nสบายใจ"

# emm "You just need to understand that accepting help goes against everything Emi thinks about herself and the way the world works."
emm "แค่เธอต้องเข้าใจก่อนว่าที่เอมิไม่ยอมรับความช่วยเหลือจากเธอเพราะมันขัดกับมุมมองของเอมิต่อตัวเอง\nกับมุมมองของเอมิต่อโลก"

# emm "If you still want to offer her help, then I guess that's your call. Honestly, I'd like you to, but it'd be silly not to warn you that it's not going to be easy."
emm "ถ้าเธอยังอยากช่วยเอมิจริง ๆ ก็อยู่ที่เธอแล้วละจ้ะ จริง ๆ ฉันก็อยากให้เธอช่วยนะ แต่จะไม่เตือนเธอว่า\nจะเป็นอะไรที่ยากหน่อยก็คงบ้าบอ"

show meiko smile
with charachange

# emm "You just need to be patient with her. She's already closer to you than anyone else she's ever met at Yamaku."
emm "ขอแค่อดทนกับเอมิหน่อย เพราะตอนนี้เอมิก็สนิทกับเธอกว่าใครคนอื่นที่เอมิเคยเจอในยามากุแล้ว"

# hi "Well it sure doesn't feel like we're very close."
hi "แต่ก็รู้สึกเหมือนเราไม่ได้สนิทกันมากเลยนะครับ"

show bg emi_dining at center
show meiko serious at tworight
with dissolvecharamove

show emicas evil at twoleft
with charaenter

stop music fadeout 0.3

# emi "Good, that makes this part easier."
emi "ดี แบบนี้ก็ง่ายขึ้นเยอะ"

# "Emi's voice nearly gives me a heart attack."
"เสียงเอมิที่แทรกมาเกือบทำฉันหัวใจวาย"

# hi "Whoa! Didn't hear you come back, Emi."
hi "เฮือก! ไม่ได้ยินเสียงเธอเดินมาเลยนะเอมิ"

show emicas angry
with charachange

# emi "How convenient."
emi "ลงตัวพอดีเลย"

# hi "Wait, were you eavesdropping?"
hi "เดี๋ยว นี่แอบฟังกันอยู่เหรอ"

show emicas angry_up
with charachange

# emi "Nope. Just happened to come back at the right moment, I guess."
emi "เปล่า แค่บังเอิญกลับมาได้จังหวะพอดีละมั้ง"

show meiko worry
with charachange

# emm "Emi, Hisao was just—"
emm "เอมิ ฮิซาโอะเขาเพิ่ง—"

# "Emi holds up a finger, cutting her mother off."
"เอมิชูนิ้วขึ้นตัดบทแม่ตัวเอง"

show emicas grit
with charachange

# emi "On his way out of the house? Yeah, I know."
emi "บอกว่าจะกลับแล้ว? ค่ะ หนูรู้"

# "Emi's trembling with anger now, looking vaguely betrayed."
"เอมิตัวสั่นด้วยความกลัว สีหน้าเธอดูคล้ายคนที่ถูกหักหลัง"

# emm "Emi, don't be ridiculous, we were just—"
emm "เอมิ พูดอะไรของลูก เราเพิ่ง—"

show emicas angry_up
with charachange

# emi "You {b}promised{/b}!"
emi "แม่{b}สัญญา{/b}แล้ว!"

play music music_rain fadein 0.5

# "The pain carried in that last word is almost too much for me to bear. The idea that I could hurt her that much is like being kicked in the gut."
"ความเจ็บปวดในคำนั้นมีมากเกินฉันจะทนฟังได้ แค่คิดว่าฉันทำร้ายเธอได้ถึงขนาดนี้ฉันก็จุกอกขึ้นมาแล้ว"

# "Emi's mother looks similarly pained by the thought."
"แม่เอมิก็ดูเจ็บปวดกับความคิดนั้นพอกัน"

# emm "And I kept that promise! Just listen, there's no reason to go throwing people out of the house."
emm "แต่แม่ก็ยังรักษาสัญญาอยู่! ฟังนะเอมิ เราจะไล่คนออกจากบ้านสุ่มสี่สุ่มห้าแบบนี้ไม่ได้"

# "Emi's mother seems to be both angry at her daughter's outburst and embarrassed that I'm a witness to it."
"แม่เอมิดูทั้งโกรธที่ลูกสาวตัวเองระเบิดอารมณ์อย่างนั้นและทั้งอายที่ต้องให้ฉันมาเห็นภาพนี้"

# "There's only one real solution to this problem, I think."
"ปัญหานี้มีทางออกเดียวแหละ คิดว่านะ"

# hi "It's okay. I'll go."
hi "ไม่เป็นไรครับ เดี๋ยวผมไปก็ได้"

# emm "Now really, that seems a little unnecessary…"
emm "ไม่เอาน่า ไม่เห็นจำเป็นต้องกลับเลย…"

# hi "Don't worry about it. Thank you for dinner, Mrs. Ibarazaki, and for the advice."
hi "ไม่ต้องห่วงหรอกครับ ขอบคุณสำหรับมื้อเย็นนะครับ แล้วก็ขอบคุณที่ให้คำแนะนำด้วย"

show meiko serious
with charachange

# emm "It was my pleasure, Hisao. I'm sorry we didn't get to the dessert."
emm "ด้วยความยินดีจ้ะฮิซาโอะ ขอโทษนะที่ไม่ได้เอาของหวานมาให้กินด้วย"

# hi "That's okay. I have to watch what I eat anyway."
hi "ไม่เป็นไรครับ ยังไงผมก็ต้องคอยคุมอาหารการกินของตัวเองด้วย"

# hi "Good evening, Emi, Mrs. Ibarazaki."
hi "สายัณห์สวัสดิ์นะครับคุณนายอิบาราซากิ แล้วก็เอมิด้วย"

# "The formality of our conversation, coupled with the fact that I'm getting ready to leave, seems to snap Emi out of her anger."
"ความเป็นทางการของบทสนทนาเรากับการที่ฉันตั้งท่าเตรียมออกจากบ้านแล้วเหมือนจะทำให้เอมิหายโกรธ\nแล้วได้สติขึ้นมา"

show emicas frown
with charachange

# emi "No, wait. I'm sorry, I've been so… and after last night I just thought… You don't have to go, I take it back, it's okay—"
emi "ไม่ เดี๋ยวก่อน ฉันขอโทษ เมื่อกี้ฉัน… แล้วเรื่องเมื่อคืนก็ทำให้ฉันคิดว่า… นายไม่ต้องไปหรอก ฉันขอถอนคำพูด\nไม่เป็นไร—"

# "I can't help but smile slightly. She can barely articulate her apology, and I really would like to stay…"
"ฉันอดอมยิ้มไม่ได้ เอมิแทบพูดคำขอโทษออกมาไม่เป็นภาษาแล้ว และฉันก็ยังไม่อยากไป…"

# "But I don't think I can, right now. I need to think about what her mother said, and about what I'm going to do about us."
"แต่ฉันว่าตอนนี้ฉันต้องไปก่อน ต้องไปคิดถึงเรื่องที่แม่เอมิพูด แล้วก็คิดว่าจะทำยังไงกับเรื่องระหว่างเราดี"

# "I don't want to risk accidentally getting Emi angry again in her current state, either."
"และฉันก็ไม่อยากเสี่ยงไปเผลอทำให้เอมิที่อยู่ในสภาพนี้ต้องโกรธอีกรอบ"

# hi "No, I think I'd better leave. You seem pretty shook up, and, well, I'd only wind up trying to help you again. I know you'd prefer I didn't, so I'm going to leave instead."
hi "ไม่หรอก ฉันว่าฉันไปก่อนดีกว่า อารมณ์เธอก็ยังไม่ค่อยคงที่ ซึ่งฉันก็จะพยายามไปช่วยเธออีก ฉันรู้ว่าเธอไม่อยาก\nให้ฉันช่วยก็เลยจะไปก่อน"

show emicas sad
with charachange

# emi "But—"
emi "แต่—"

# hi "Hey, it's not a problem. You don't want a knight on a white charger, right? Just promise me one thing, okay?"
hi "น่า ไม่เป็นไรหรอก เธอไม่ได้ต้องการให้พระเอกขี่ม้าขาวมาช่วยใช่มั้ยล่ะ แต่รับปากกับฉันอย่างสิ"

show emicas frown
with charachange

# emi "What?"
emi "ว่า"

# hi "Don't be angry at your mom, okay? She was just giving me some advice, that's all."
hi "อย่าโกรธแม่เธอเลยนะ แม่เธอแค่แนะนำฉันเฉย ๆ"

show emicas sad
with charachange

# "Emi nods, hesitantly, like this simple idea is all that she can grab on to at this point. She's so terribly off-balance, but I can't do anything about that right now."
"เอมิกึ่ง ๆ พยักหน้าเหมือนสิ่งเดียวที่พอรับรู้ได้คือคำสัญญาง่าย ๆ นั้น เธอเสียศูนย์อย่างหนัก แต่ตอนนี้ฉันทำอะไร\nไม่ได้หรอก"

# emi "Okay."
emi "โอเค"

# hi "See you tomorrow, okay? Running in the morning. Don't forget!"
hi "เจอกันพรุ่งนี้นะ ไปวิ่งตอนเช้าด้วย ห้ามลืม!"

# "I can see that I've hurt Emi by deciding to leave. But there's nothing I can do for her as things stand, and I know that she's too stubborn to admit that she wants me to stick around."
"ฉันเห็นว่าเอมิเจ็บปวดแค่ไหนที่ฉันเลือกจะไป แต่ถ้าเรื่องยังเป็นอย่างนี้ฉันก็คงช่วยอะไรเธอไม่ได้ และฉันรู้ดีว่าเอมิ\nรั้นเกินกว่าที่จะยอมรับว่าอยากให้ฉันอยู่ต่อ"

# "I watch various emotions cross Emi's face as she tries to process everything that's just happened."
"ฉันมองหน้าเอมิที่มีหลากอารมณ์ระคนกันอยู่ระหว่างที่เธอกำลังประมวลผลสิ่งที่เกิดขึ้น"

show emicas weaksmile
with charachange

# "Shortly comes that calm look again, like last night, and that voice that tries so hard to sound careless."
"ไม่นานสีหน้าดูสงบนั้นก็ปรากฏเหมือนเมื่อคืน และน้ำเสียงนั้นที่ปั้นมาให้เหมือนไม่ได้ยี่หระ"

# emi "Sure, Hisao. See you around."
emi "ก็ได้ฮิซาโอะ ไว้เจอกัน"

# "Both of us are unwilling to concede emotion at this point, and I'm having a hard time keeping up my facade, so I turn on my heel and walk out the door."
"เราทั้งสองคนต่างไม่มีใครยอมรับอารมณ์ที่ตัวเองรู้สึกอยู่ ฉันเองก็รักษาสีหน้าท่าทีปลอมเปลือกไว้ไม่ไหวจึงหมุนเท้า\nแล้วเดินออกประตูมา"

stop music fadeout 7.0

scene bg emi_houseext
with locationskip

# "I shut it behind me slowly, pausing for a moment as the latch catches, my hand on the doorknob."
"ฉันปิดประตูช้า ๆ เว้นช่วงไปครู่หนึ่งตอนที่สลักกลอนลงล็อกโดยมือยังจับลูกบิดไว้"

# "Did I make the right decision just now? Should I have stayed and tried to work things out?"
"เมืื่อกี้ฉันตัดสินใจถูกหรือยัง หรือฉันควรอยู่ต่อแล้วลองกอบกู้สถานการณ์ดู"

# "No, I decide. Not in front of her mother like that. In spite of everything, I'd rather keep Emi's mother insulated from the sort of anger that surfaced last night."
"ไม่สิ ฉันตัดสินใจแล้ว ยิ่งมีแม่เอมิอยู่ด้วย ไม่ว่าจะยังไงก็ตาม ฉันไม่อยากให้แม่เอมิต้องมารับรู้ถึงความโกรธแบบนั้น\nที่ระเบิดออกมาเมื่อคืน"

# "Even though she's probably used to it, some protective instinct wants me to keep Emi's image as a cheerful girl intact."
"ถึงแม่เอมิอาจจะชินแล้ว แต่ในใจฉันก็ยังอยากรักษาภาพลักษณ์เด็กสาวผู้ร่าเริงของเอมิเอาไว้อยู่"

# "With a start, I realize my hand is still resting on the knob. I take my hand away, put it in my pocket, and head down the slowly darkening street."
"ฉันสะดุ้งเมื่อรู้ตัวว่ามือยังจับลูกบิดอยู่ ฉันถอนมือออกมาแล้วล้วงกระเป๋าเดินไปตามถนนที่มืดลงเรื่อย ๆ"

scene bg school_dormhisao
with shorttimeskip

play music music_pearly fadein 1.0

# "I let out a long breath."
"ฉันถอนหายใจพรืด"

# "The wait until tomorrow morning comes isn't going to be easy."
"คงต้องอดทนอย่างหนักกว่าจะรอให้ถึงพรุ่งนี้เช้าได้"

# "In any case, I have to think on what to say to Emi. I must apologize, and I must get through to her somehow."
"แต่ไม่ว่ายังไงฉันก็ต้องคิดไว้ก่อนว่าจะพูดอะไรกับเอมิ ต้องขอโทษ และต้องหาทางทำให้เอมิเข้าใจให้ได้"

# "On that account, something has been on my mind for most of the way back to my room."
"เพราะเหตุนี้เองตอนที่เดินกลับมายังห้องตัวเองฉันถึงคิดอยู่เรื่องหนึ่ง"

# "The letter of apology from Iwanako."
"จดหมายขอโทษจากอิวานาโกะ"

# "I was so concerned about my new life when I received it that I didn't even bother to really read it."
"ฉันมัวแต่วุ่นวายกับชีวิตใหม่ของตัวเองจนไม่ได้ใส่ใจจะอ่านตอนที่จดหมายฉบับนั้นมาถึง"

# "Now that I find myself in a similar position, my curiosity got rekindled. What did she want to let me know so badly?"
"พอตอนนี้ฉันต้องมาตกอยู่ในสถานการณ์ที่คล้าย ๆ กันแล้วก็อยากรู้ขึ้นมาอีกครั้ง เรื่องอะไรที่อิวานาโกะอยากให้ฉันรู้\nนักหนา"

# "If nothing else, reading her thoughts might help me frame mine."
"อย่างน้อย ๆ การได้อ่านความคิดของอิวานาโกะอาจช่วยให้ฉันได้มีแนวคิดใหม่ ๆ บ้าง"

# "I remember tossing it away. Damn, where did I throw that thing?"
"จำได้ว่าปาทิ้งไปแล้ว แม่ง นี่เอาไปทิ้งไว้ไหนเนี่ย"

# "I check under my desk. That turns up nothing, so I look for harder-to-reach, more unlikely locations."
"ฉันก้มดูใต้โต๊ะ ซึ่งไม่มี ฉันจึงไปหาตามซอกมุมต่าง ๆ ที่ไม่น่าจะเจอได้"

"…"

# "Well, now I know where that lost sock went, at least."
"โอเค อย่างน้อยตอนนี้ก็เจอแล้วว่าถุงเท้าที่หายไปตอนนั้นอยู่ไหน"

# "Still no letter, though."
"แต่ยังไม่เจอจดหมายเลย"

# "It's when I try sweeping my arm under my nightstand that I feel something crinkly jammed between it and the wall."
"พอฉันลองยื่นแขนกวาดไปใต้โต๊ะหัวเตียงก็เหมือนจับโดนอะไรสักอย่างสาก ๆ ที่คาอยู่ระหว่างโต๊ะกับกำแพง"

# "Grunting a little with the effort, I reach for my prize and soon manage to bring it into the light."
"ฉันออกแรงฮึดยื่นไปคว้าของที่หมายไว้แล้วหยิบออกมาสู่โลกภายนอกได้"

# "Bingo."
"บิงโก"

play sound sfx_paper

scene ev hisao_letter_open_2
with locationchange

# "I sit at my desk and spread the crumpled paper open. A flick turns on the table light."
"ฉันนั่งที่โต๊ะแล้วคลี่ก้อนกระดาษออกก่อนจะเปิดโคมไฟ"

# "Skipping past the empty pleasantries, I look for the point where I stopped reading. Ah, here it is."
"ฉันข้ามส่วนอารัมภบทไร้แก่นสารพวกนั้นหาว่าอ่านถึงตรงไหน อ้อ ตรงนี้ไง"

window hide

# $ written_note("There are other things I want to say. I'm writing to you because I felt that there are things I should've said after the incident back in winter. I really regret that I wasn't able to say them in person, and I have no excuse for it.\n\n\n\n\n")
$ written_note("ยังมีอย่างอื่นที่ฉันอยากพูดถึงอีก ฉันเขียนจดหมาย\nส่งมาหานายเพราะรู้สึกเหมือนพอเกิดเรื่องนั้นแล้ว\nฉันคงต้องพูดอะไรหน่อย ฉันเสียใจจริง ๆ ที่ฉันมา\nพูดกับนายต่อหน้าตรง ๆ ไม่ได้ และฉันก็ไม่มี\nข้อแก้ตัวอะไรทั้งนั้น\n\n\n\n\n")

# $ written_note("The truth is, the times when I visited you at the hospital made me worried about you. I am not talking about your health. You seemed to become more distant and disheartened. It was natural after something like that happened, I'm sure, but somehow I got the feeling that you had given up on something back then. Happiness, maybe?\n")
$ written_note("ที่จริงคือ ตอนฉันไปเยี่ยมนาย ฉันก็เป็นห่วงนาย\nขึ้นมา ไม่ได้หมายถึงสุขภาพนายนะ แต่นายดูทั้ง\nห่างเหินทั้งไร้เรี่ยวแรง ฉันรู้อยู่ว่าพอเกิดเรื่อง\nอย่างนั้นแล้วจะเป็นแบบนั้นไปก็คงไม่แปลก แต่\nตอนนั้นฉันรู้สึกเหมือนนายถอดใจกับอะไร\nบางอย่างไปแล้ว ความสุข ละมั้ง\n")

window show

# "Giving up on happiness…"
"ถอดใจกับความสุข…"

# "This sounds unpleasantly familiar."
"ฟังดูคุ้น ๆ เป็นบ้า"

window hide

# $ written_note("I wanted to somehow express my feelings, but the right words didn't come to me. I couldn't say anything to comfort you. I am really sorry for not being able to support you when it mattered the most, even though I like you so much. At least now, finally, I can be more honest.\n\n\n\n")
$ written_note("ฉันอยากบอกความรู้สึกให้นายได้รู้ แต่ก็นึกหาคำ\nไม่ได้เสียที ฉันพูดอะไรปลอบใจนายไม่ได้เลย ฉัน\nขอโทษจริง ๆ ที่คอยเป็นแรงใจให้นายยามที่นาย\nต้องการแรงใจที่สุดไม่ได้ ทั้งที่ฉันชอบนายมาก\nแท้ ๆ แต่อย่างน้อยตอนนี้ฉันก็พูดตรง ๆ ขึ้นมา\nได้บ้างแล้ว")

# $ written_note("If I could go back to those quiet days in February and March, I'd tell you to not give up on yourself. That's what I would say. Maybe you wouldn't have drifted so far away if I had just said something. I hope you've managed to get back on your feet on your own.\n\n\n\n")
$ written_note("ถ้าฉันกลับไปช่วงเดือนกุมภาพันธ์กับเดือนมีนาคมที่\nเงียบสงบนั้นได้ฉันก็อยากบอกนายว่าอย่ายอมแพ้\nนะ ฉันจะบอกอย่างนั้น ถ้าฉันพูดอะไรบ้างนายคง\nไม่ออกเหินห่างไปขนาดนี้ ฉันอยากให้นายลุกขึ้น\nมายืนด้วยตัวเองให้ได้\n\n\n\n")

# $ written_note("Now that the distance between us is also physical, it also feels more final, somehow. I wonder if we will meet again. Perhaps it's for the best if we don't? Still, if you would like to correspond with me, by all means write me back. I'd very much like to hear about your new school and how you are doing. I wish you all the best.\n\nSincerely, Iwanako")
$ written_note("แล้วยิ่งทีนี้ห่างกายกันด้วยก็ยิ่งรู้สึกเหมือนเป็นจุด\nส่งท้ายจริง ๆ ยังไงไม่รู้ เราจะได้เจอกันอีกไหมนะ\nหรือถ้าไม่เจอกันอีกเลยจะดีกว่ากันนะ แต่ถ้ายัง\nอยากติดต่อกับฉันอยู่ก็เขียนส่งกลับมาได้เลยนะ\nฉันยินดีมากที่จะได้ฟังเรื่องโรงเรียนใหม่กับ\nชีวิตใหม่ของนาย ขอให้มีความสุขดีนะ\n\nจากใจ อิวานาโกะ")

window show

# "After finishing reading the letter I smooth it out carefully and set it aside on my desk."
"พออ่านจบแล้วฉันก็รีดกระดาษให้เรียบแล้ววางไว้ที่ริมโต๊ะ"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

# n "\n\n\nThank you, Iwanako. I wanted to answer “yes” to your question on that snowy winter day, but I never got to."
n "\n\n\nขอบคุณนะอิวานาโกะ ฉันอยากจะตอบตกลงกับคำถามเมื่อวันหิมะตกในฤดูหนาวครั้งนั้นแต่ก็ไม่มีโอกาสได้ตอบเลย"

# n "By the time we met again, it was too late."
n "กว่าเราจะได้มาเจอกันอีกก็สายไปแล้ว"

# n "Or so I thought. What would have happened if I had behaved differently, back in that dismally sterile hospital room?"
n "ฉันคิดไว้ว่าอย่างนั้น แต่ถ้าเกิดว่าตอนที่อยู่ในห้องสะอาดชวนหดหู่นั้นฉันทำตัวอีกแบบอีกแบบแล้วจะเป็นยังไงล่ะ"

# n "I'm sorry. There's no point in wondering now, but there's no point in trying to forget either."
n "ขอโทษนะ จะมาสงสัยเอาตอนนี้ก็คงไม่ได้อะไรขึ้นมาแล้ว แต่จะให้ทำใจลืมก็คงไม่มีประโยชน์เหมือนกัน"

# n "I am who I am because of all that happened to me and all I look forward to experience. Present, future, and past."
n "ที่ฉันเป็นตัวฉันในตอนนี้เพราะสิ่งที่เคยเกิดขึ้นกับฉันกับสิ่งที่ฉันตั้งตาหมายจะได้สัมผัส ปัจจุบัน อนาคต อดีต"

stop music fadeout 2.0

# n "\n\nAnd the past may just have taught me an important lesson now."
n "\n\nและตอนนี้เหมือนว่าอดีตจะได้ให้บทเรียนสำคัญกับฉันแล้ว"

$ renpy.music.set_volume(1.0, 2.0, channel="music")

nvl clear
nvl hide dissolve

#Hey, you didn't fuck up. As a congratulatory gesture, go to e29. You lucky duck.
# This is actually an act ending, links to titlecard

#########################

label th_E27:

window hide None

scene black
with dissolve

play sound sfx_alarmclock

with Pause(2.0)

scene bg school_dormhisao
with openeye

window show

# "The morning alarm sounds and I roll over, switching it off. My eyes open blearily to stare at the ceiling."
"เสียงนาฬิกาปลุกยามเช้าดังขึ้น ฉันพลิกตัวไปปิดก่อนจะทำตาปรือมองเพดาน"

play music music_night fadein 1.0

window hide
nvl clear
nvl show dissolve

# n "\n\nWhat am I going to do? Do I get out of bed, go down to the track, and pretend that nothing happened?"
n "\n\nจะเอายังไงดี ลุกจากเตียงไปที่ลู่วิ่งแล้วทำเหมือนไม่มีอะไรเกิดขึ้นเหรอ"

# n "Will Emi even show up? After last evening's events, I doubt it."
n "เอมิจะมาหรือเปล่า ดูจากเหตุการณ์เมื่อเย็นวานแล้วคงไม่หรอก"

# n "Even supposing that she did, what would I do then? Get over this fight just to dance the same routine the next time something's bothering her?"
n "หรือต่อให้มาแล้วฉันจะทำยังไง ลืมที่ทะเลาะกันไปแล้วก็ทำซ้ำแบบนี้อีกรอบหน้าถ้ามีเรื่องกวนใจเอมิอีกเหรอ"

# n "I know that I spoke hastily last evening, especially trying to use her father as leverage."
n "ฉันรู้ว่าเมื่อวานฉันใจร้อนไปก็จริง แล้วยิ่งเอาเรื่องพ่อเอมิมาอ้างอีก"

# n "But was anything I said really off the mark? She won't let me in, ever, and she'll be forced to suffer alone."
n "แต่ฉันพูดผิดหรือไง เอมิไม่ยอมเปิดใจให้ฉันเข้าไปเลย และเธอก็จะต้องทนทรมานอยู่ตัวคนเดียว"

# n "Nothing I do, nothing I say is going to change that. She won't change, and she's already decided to keep me at arm's length."
n "ไม่ว่าฉันจะทำอะไร ไม่ว่าฉันจะพูดอะไร ทุกอย่างก็จะเหมือนเดิม เอมิไม่ยอมเปลี่ยน และตัดสินใจแล้วว่าจะเว้นระยะห่าง\nกับฉัน"

# n "\nCan I really bring myself to go down there and see her, knowing that I'm never going to get past where I am now?"
n "\nแล้วอย่างนี้ฉันจะยังอยากลงไปเจอเอมิอีกเหรอ ทั้งที่รู้ว่าฉันจะไปต่ออีกไม่ได้แล้วน่ะนะ"

nvl clear
nvl hide dissolve

scene black
with shuteye

window show

# "No, I decide. I really can't. Not today. I roll over and go back to sleep."
"ไม่เอาหรอก ไม่ได้จริง ๆ ไม่ใช่วันนี้ ฉันพลิกตัวนอนต่อ"

# "She probably won't be there anyway."
"ยังไงเอมิก็คงไม่ไปที่ลู่วิ่งอยู่แล้ว"

scene bg school_cafeteria
with shorttimeskip

# "A similar mental conversation repeats itself when it comes time to go to lunch, and I eat in the cafeteria, alone."
"พอถึงเวลาพักเที่ยงฉันก็คุยกับตัวเองอยู่ในหัวคล้ายอย่างเมื่อเช้า และฉันก็นั่งกินข้าวเที่ยงที่โรงอาหารตัวคนเดียว"

# "I don't want to see her; the very thought makes me feel ill."
"ฉันไม่อยากเจอเอมิ แค่คิดก็รู้สึกไม่ดีแล้ว"

scene bg school_track_ni
with shorttimeskip

# "That night, I go for a run; I'm solo for the first time since Emi got sick after the track meet."
"คืนนั้นฉันออกวิ่ง เป็นอีกครั้งที่ฉันมาวิ่งตัวคนเดียวนับตั้งแต่ที่เอมิป่วยไปตอนหลังจากงานแข่งวิ่งครั้งนั้น"

# "Skipped seeing the nurse, just in case he asked about Emi."
"และไม่ไปหาคุณพยาบาล จะได้ไม่ต้องตอบคำถามเรื่องเอมิ"

# "I don't want to talk about her, either."
"ฉันเองก็ไม่อยากคุยเรื่องเอมิด้วย"

scene bg school_hallway3
with shorttimeskip

# "The next day, I do the same thing. Alarm, off. Stay in bed. Eat alone, run alone."
"วันถัดมาฉันก็ทำเหมือนเดิม ปิดนาฬิกาปลุก นอนต่อ กินข้าวคนเดียว วิ่งคนเดียว"

# "To fill the time that I would usually be spending with Emi, I start reading more."
"ฉันอ่านหนังสือเยอะขึ้นเป็นการชดเชยเวลาที่ปกติฉันจะอยู่กับเอมิ"

# "It works surprisingly well, until I find myself ducking into a restroom because I see her walking down the hall in between classes."
"ซึ่งได้ผลดีเหลือเชื่อ ก็จนกระทั่งฉันต้องมาแอบในห้องน้ำเพราะเห็นเอมิเดินอยู่ตรงโถงทางเดินช่วงเปลี่ยนคาบ"

# "If she noticed me, she didn't show it, even though I don't suppose she ever shows anything."
"เอมิไม่ได้แสดงท่าทีว่าเห็นฉันเลย แต่ก็นะ เอมิไม่เคยแสดงอะไรให้เห็นหรอก"

# "Certainly not to the girls from her class I see talking cheerfully to her."
"ไม่แสดงให้เด็กสาวที่เป็นเพื่อนร่วมชั้นคนนั้นที่ฉันเห็นคุยอยู่กับเอมิอย่างร่าเริงเห็นแน่นอน"

# "Or to her fellow track members."
"ไม่แสดงให้เพื่อนร่วมทีมเห็นด้วย"

# "Especially not to me."
"ยิ่งกับฉันแล้วไม่แสดงให้เห็นเลย"

# "Alarm off. Stay in bed."
"ปิดนาฬิกาปลุก นอนต่อ"

scene bg school_scienceroom
show muto normal at center
with shorttimeskip

# "Mutou and I have a lengthy talk about the possibility that string theory is plausible. I don't buy it, myself."
"ครูมุโต้กับฉันคุยกันเสียยืดยาวว่าทฤษฎีสตริงนั้นเป็นไปได้หรือไม่ ส่วนตัวฉันแล้วเชื่อว่าเป็นไปไม่ได้"

# "More than four dimensions, I can buy. But a bunch of vibrating strings at the subatomic level? That's asking a bit much."
"มิติที่สูงกว่ามิติที่สี่นั้นฉันเชื่ออยู่ แต่จะให้เชื่อว่ามีสตริงหลาย ๆ สตริงที่เล็กกว่าอะตอมสั่นอยู่น่ะเหรอ ยากหน่อยนะ"

# "Looks like I'm not the only one to think this way, too. Apparently it's not really as strong a theory as it once was."
"ดูเหมือนว่าจะไม่ได้มีแค่ฉันที่คิดแบบนี้ด้วย และเหมือนจะไม่ได้เป็นทฤษฎีที่หนักแน่นอย่างสมัยก่อนแล้ว"

# "Mutou says that's just because nobody has found the right way of looking at the data yet."
"ครูมุโต้บอกว่าที่เป็นแบบนั้นก็เพราะยังไม่มีใครค้นพบวิธีการตีความข้อมูลที่ถูกต้องต่างหาก"

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_rooftop

scene bg school_roof
with shorttimeskip

# "Eat alone."
"กินข้าวคนเดียว"

# "The rooftop is deserted today. I briefly wonder where Emi and Rin are, but shrug off the question. The important thing is that they aren't here, so I won't have to talk to them."
"วันนี้ที่ดาดฟ้าไม่มีคน แวบหนึ่งฉันนึกสงสัยว่าเอมิกับรินไปไหน แต่ก็ปัดคำถามนั้นทิ้ง สองคนนั้นไม่อยู่น่ะดีแล้ว\nฉันจะได้ไม่ต้องคุยด้วย"

# "Since I have nobody to talk to, I bring a book with me to read."
"เมื่อไม่มีใครให้คุยด้วยจึงหยิบหนังสือที่พกติดตัวมาอ่าน"

# "The weather's nicer, if getting a little hot."
"อากาศเริ่มสดชื่นขึ้นแล้ว และร้อนขึ้นหน่อย ๆ"

# "Hopefully it will be cooler in the evening; a cool breeze seems to back up my theory."
"หวังว่าพอเย็น ๆ แล้วจะเย็นลงบ้าง สายลมเย็นที่โชยมาสนัยสนุนแนวคิดฉัน"

stop ambient fadeout 2.0

scene bg school_track_on_ni
with shorttimeskip

# "Run alone."
"วิ่งคนเดียว"

# "It is, in fact, cooler at the track. No sign of Emi, which is exactly the sort of thing I'm going for."
"ซึ่งที่ลู่ก็อากาศเย็นกว่าตอนเที่ยงจริง ๆ ไม่มีวี่แววว่าเอมิอยู่ เป็นไปดังที่ฉันหวัง"

# "I stretch out and start on my usual run, trying hard to ignore the lack of a running partner in front of me."
"ฉันยืดเส้นยืดสายก่อนออกวิ่งอย่างทุกทีคอยห้ามใจไม่ให้คิดถึงคู่วิ่งที่ไม่ได้อยู่ตรงหน้า"

# "Finding my thoughts drifting damnably to that girlish laugh, incorrigible grin, those wide and friendly eyes, her incredibly toned body—"
"แต่ใจเจ้ากรรมของฉันดันนึกถึงเสียงหัวเราะอย่างเด็กสาวนั้น รอยยิ้มติดตรึงนั้น ตาโตเป็นมิตรนั้น\nร่างกายที่มีกล้ามนั้น—"

scene bg school_track_running_ni
with Dissolve(1.0)

# "I increase the pace to clear my head. Chew up the distance between me and the turns, find the speed that makes me think only of my legs and how much they burn."
"ฉันเร่งฝีเท้าเพื่อให้สมองปลอดโปร่ง ย่นระยะตัวเองให้เข้าใกล้โค้งไปเรื่อย ๆ พลางเลือกความเร็วที่จะทำให้สมองฉัน\nคิดแต่เรื่องขาตัวเองที่ร้อนจัด"

# "I glance at my watch as I round the final turn, noting that my time's gotten faster."
"เมื่อเหลือบมองนาฬิกาตอนเข้าโค้งสุดท้ายก็เห็นว่าฉันทำเวลาได้เร็วขึ้น"

show bg school_track_on_ni
with Dissolve(2.0)

# "My heart seems a little squirrelly tonight, so I give myself a few extra cool-down laps just to be safe."
"คืนนี้หัวใจฉันดูจะปั่นป่วนเล็กน้อย ฉันจึงเดินคูลดาวน์ให้มากกว่าปกติสักสองสามรอบเพื่อความปลอดภัย"

# "No reason to bring this to the nurse's attention. I'll be fine. A rather Emi-ish thought to have, I'll admit."
"ไม่ต้องเอาไปบอกให้คุณพยาบาลรู้หรอก เดี๋ยวก็ไม่เป็นไรแล้ว แต่ก็ยอมรับว่าเป็นความคิดที่เหมือนอย่างเอมิจริง ๆ"

# "I have to hope that eventually I'll stop thinking about her so much."
"ได้แต่หวังว่าสักวันฉันจะเลิกคิดถึงเอมิมากขนาดนี้เสียที"

scene bg school_dormhisao
with shorttimeskip

# "I finish another book before going to bed that night. I'll have to stop by the library tomorrow."
"ฉันอ่านหนังสืออีกเล่มจบก่อนนอน พรุ่งนี้ต้องไปแวะห้องสมุด"

play sound sfx_switch

show bg school_dormhisao_ni
with Dissolve(0.2)

with Pause(0.5)

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
stop music fadeout 3.5

scene black
with shuteye

window hide

with Pause(2.0)
play sound sfx_alarmclock
scene bg school_dormhisao
with openeye

window show

# "I don't know why I keep the early alarm on any more, but it wakes me up the next morning just the same. I still turn it off and go back to sleep."
"ฉันไม่รู้ด้วยซ้ำว่าจะตั้งนาฬิกาปลุกตอนเช้าไปทำไม แต่นาฬิกาปลุกนั้นยังดังปลุกฉันในเช้าวันถัดมาเช่นเคย และฉัน\nก็ยังปิดแล้วนอนต่อ"

scene bg school_scienceroom
show misha perky_smile at center
with shorttimeskip

play music music_pearly fadein 1.0

# "That afternoon, as I get ready to head to the cafeteria for another solo lunch (I've got a new book about a couple of con men in ancient Persia that I'm pretty excited about reading) I am suddenly cornered by Misha and…"
"บ่ายวันนั้นระหว่างที่จะไปโรงอาหารเพื่อฉายเดี่ยวกินข้าว (ฉันได้หนังสือใหม่มาที่อยากอ่านมาก ในนั้นเล่าเรื่อง\nของนักต้มตุ๋นสองคนที่อาศัยอยู่ในเปอร์เซียโบราณ) อยู่ ๆ ก็มีคนมาดักรอฉัน เป็นมิช่ากับ…"

# "Huh. I guess just Misha."
"หือ คงมีแค่มิช่าแหละ"

show misha hips_smile
with charachange

# mi "Off to eat alone again, Hicchan~?"
mi "ไปกินข้าวคนเดียวอีกแล้วเหรอฮิจัง~"

show misha sign_smile
with charachange

# mi "We've noticed, you know~!"
mi "พวกเราเห็นนะ~!"

# hi "We?"
hi "พวกเรา?"

show misha hips_grin
with charachange

# mi "Uh huh! Shicchan and I noticed that you've been spending more time alone!"
mi "อ่าฮะ! ชิจังกับฉันเห็นว่าฮิจังอยู่ตัวคนเดียวบ่อยขึ้น!"

show misha hips_smile
with charachange

# mi "She wanted me to find out why, so I told her I'd ask you!"
mi "ชิจังอยากรู้ว่าเพราะอะไรฉันเลยบอกไปว่าจะมาถามฮิจังให้!"

# hi "I'm surprised she didn't ask me herself."
hi "แปลกใจนะเนี่ยที่ชิจังไม่ได้มาถามเอง"

show misha perky_smile
with charachange

# mi "She would have, but she wanted to get a head start on some paperwork. There's a lot of it since we're coming up on the end of the term, you know~!"
mi "ชิจังก็คิดจะมาถามอยู่ แต่เห็นอยากไปเริ่มทำงานเอกสารก่อน ช่วงนี้ใกล้ปิดเทอมแล้วงานก็เยอะมากเลย~!"

# hi "Why the sudden interest in my well-being, anyway?"
hi "แล้วทำไมอยู่ ๆ ถึงมาสนใจชีวิตฉันล่ะหืม"

show misha sign_smile
with charachange

# mi "Ah, Shicchan said “It is the duty of the Student Council to keep track of the emotional health of its students! To allow a cons—constituent to spiral into depression unchecked would be an unforgivable failure in the council's duties!”"
mi "อ้อ ชิจังบอกว่า “หน้าที่ของสภานักเรียนคือการตามสังเกตสุขภาพจิตของนักเรียน! ถ้าปล่อยให้คน\nใต้การปกครองในระบ—ระบอบที่มีภาวะซึมเศร้าให้หลุดรอดสายตาไปแล้วคงนับได้ว่าสภานักเรียนล้มเหลว\nในหน้าที่อย่างไม่น่าให้อภัย!”"

# hi "Well, that's easy, then. I'm not depressed."
hi "งั้นก็สบายเลย ฉันไม่ได้ซึมเศร้า"

show misha perky_confused
with charachange

# mi "But you're eating alone, and nobody's seen you and Emi together at all! Something happened, didn't it, Hicchan~?"
mi "แต่ฮิจังกินข้าวคนเดียว แล้วก็ไม่มีใครเห็นฮิจังอยู่กับเอมิเลย! มีเรื่องอะไรกันใช่มั้ยล่ะฮิจัง~"

# "Misha's voice takes on a slightly sterner tone, though somehow she keeps the familiar lilt at the end of her sentences."
"เสียงมิช่าฟังดูเคร่งขรึมขึ้นเล็กน้อย แต่เธอยังรักษาการเล่นเสียงสูงต่ำอันคุ้นเคยตอนปิดท้ายประโยคได้"

#Okay, so you've managed to wind up on the road to BADSVILLE, but you've actually only made one big mistake in all this. SO!  You get the following choice.  Will you figure out that Hisao could use advice, or not?

label th_choiceE27:
menu:
    with menueffect

    # "I purse my lips, uncertain about how to respond."
    "ฉันเม้มปากด้วยไม่แน่ใจว่าจะตอบอย่างไรดี"

    # "Downplay the issue.":
    "บอกว่าไม่ใช่เรื่องใหญ่":
        return m1

    # "Give in and let Misha know.":
    "ยอมบอกมิช่า":
        return m2


#1.  Skirt the issue.
#2.  Spill it all to the bulls--er, Misha, rather.

#If you picked 1:

label th_E27a:
# "I'm not sure I like the idea of airing private matters to the Student Council."
"การเอาเรื่องส่วนตัวไปประกาศให้สภานักเรียนรู้คงไม่น่าใช่อะไรที่ดีสำหรับฉันเท่าไหร่"

# hi "Nothing major."
hi "ไม่ใช่เรื่องใหญ่อะไรหรอก"

show misha cross_frown
with charachange

# mi "Hicchan, lying is a terrible thing to do~!"
mi "ฮิจัง โกหกมันไม่ดีนะ~!"

# "She's not buying it."
"มิช่าไม่เชื่อ"

# "Okay, give her something, but not too much."
"โอเค เล่า ๆ หน่อยแล้วกัน แต่ห้ามบอกเยอะไป"

# hi "We had a disagreement and haven't resolved it yet."
hi "พอดีมีเรื่องไม่ลงรอยกันน่ะ"

show misha perky_confused
with charachange

# mi "Oh? Why not?"
mi "อ้าว ทำไมล่ะ"

# hi "Because - look, I don't need to talk about this, okay?"
hi "เพราะ คือ ฉันไม่อยากคุยเรื่องนี้ โอเคนะ"

# hi "It's not a big deal, okay? I'm fine."
hi "เรื่องเล็ก ๆ น้อย ๆ แหละน่า ฉันไม่เป็นไรหรอก"

show misha perky_sad
with charachange

# mi "And Emi? Is she fine too, Hicchan?"
mi "แล้วเอมิล่ะ เอมิไม่เป็นไรด้วยใช่มั้ยฮิจัง"

stop music fadeout 4.0

# "Misha's voice has taken on a decidedly serious edge. This is ridiculous."
"เสียงมิช่าจริงจังขึ้นมามาก บ้าไปแล้ว"

# hi "I don't know, okay? I haven't asked. Things are complicated right now."
hi "ไม่รู้ โอเคนะ ฉันไม่ได้ถาม ตอนนี้เรื่องมันซับซ้อน"

show misha hips_frown
with charachange

# mi "What kind of man are you? Things get a little rough and you're going to hide from them?"
mi "ฮิจังเป็นคนยังไงเนี่ย พอมีเรื่องนิด ๆ หน่อย ๆ แล้วก็ปกปิดไม่ยอมบอกอีกคน"

play music music_rain fadein 4.0

# "Misha's sudden retort catches me completely off guard."
"หมัดของมิช่าที่สวนมาเล่นเอาฉันไม่ทันตั้งตัว"

show misha cross_frown
with charachange

# mi "Shicchan would call that a cowardly act, and she'd be right too!"
mi "ชิจังคงบอกว่าขี้ขลาด แล้วก็จะถูกของชิจังด้วย!"

# mi "You two were close! Happy together! And you're just going to roll over and die without a fight?"
mi "เธอสองคนสนิทกัน! อยู่ด้วยกันอย่างมีความสุข! แล้วนี่จะยอมสิ้นใจไปโดยไม่แม้แต่จะลุกขึ้นสู้เลยเหรอ"

# mi "You should be willing to fight for your girlfriend, Hisao!"
mi "นายต้องลุกขึ้นสู้เพื่อแฟนสาวของตัวเองสิฮิซาโอะ"

# "It seems that Misha is channeling Shizune at the moment. It wouldn't surprise me to find out that Shizune gave her a script to follow based on my answer."
"ดูท่าว่าตอนนี้มิช่าจะเอาชิซูเนะมาประทับร่างอยู่ ซึ่งฉันก็คงไม่แปลกใจหรอกถ้าชิซูเนะจะให้บทกับมิช่าไว้แล้ว\nว่าต้องตอบฉันยังไงบ้าง"

# "Misha points an imperious arm at the classroom door."
"มิช่ายืดแขนชี้นิ้วไปที่ประตูห้องเรียนอย่างองอาจ"

show misha sign_smile
with charachange

# mi "Now you get out of the classroom and patch things up!"
mi "ทีนี้ก็ออกจากห้องไปง้อเอมิซะ!"

# hi "Um, we've still got afternoon classes…"
hi "เอ่อ คือตอนบ่ายเรายังต้องเรียนอยู่…"

# "This doesn't seem to dissuade Misha."
"มิช่ายังคงไม่เปลี่ยนใจ"

show misha hips_smile
with charachange

# mi "Then after class! You'd better do it, Hicchan! It's important that you don't leave things like this!"
mi "งั้นก็ไปหลังเลิกเรียน! ไปจัดการซะนะฮิจัง! จะปล่อยให้อะไร ๆ มันค้างคาอยู่แบบนี้ไม่ได้!"

# hi "Why?"
hi "ทำไมล่ะ"

show misha cross_frown
with charachange

# "Misha regards me as one would regard an animal's droppings."
"มิช่ามองฉันเหมือนเป็นเศษขี้หมาแห้ง"

# mi "Didn't you care about her, Hisao? That's important, isn't it?"
mi "ก็เอมิสำคัญกับนายไม่ใช่เหรอฮิซาโอะ ประเด็นคือตรงนี้นี่"

# "Huh. She's right."
"อา นั่นสินะ"

# "I did… I do care about her."
"สำคัญ… สำคัญมาตลอด"

# "Don't I?"
"ใช่มั้ยล่ะ"

# hi "Okay. I'll see her after class."
hi "โอเค เดี๋ยวเลิกเรียนแล้วฉันจะไปหาเอมิ"

show misha hips_grin
with charachange

# mi "Great~! I'll let Shicchan know you're okay, then~!"
mi "เยี่ยม~! งั้นเดี๋ยวไปบอกชิจังว่าฮิจังโอเคแล้ว~!"

# "The lilt returns. I guess that means that Misha isn't angry at me any more."
"น้ำเสียงเริงร่านั้นกลับมา คงแปลว่ามิช่าไม่ได้โกรธฉันแล้วสินะ"

hide misha
with charaexit

# "She waves and disappears down the hallway, and I eat my lunch."
"มิช่าโบกมือให้แล้วหายตัวไปตามโถงทางเดิน ส่วนฉันก็ไปกินข้าวเที่ยง"

scene bg school_scienceroom
with shorttimeskip

# "While afternoon classes draw to a close, I prepare myself for the task ahead."
"ระหว่างที่ใกล้หมดคาบบ่ายฉันก็เตรียมตัวกับเรื่องที่จะทำต่อจากนี้"

# "I have to see Emi; Misha was at least correct about that. Leaving the question of Emi and me an open issue won't work."
"ฉันต้องไปหาเอมิ ตรงนี้มิช่าพูดถูก ปล่อยให้ประเด็นระหว่างเอมิกับฉันคาราคาซังคงไม่ได้อะไรขึ้นมา"

# "At the very least, I need to apologize for what I said."
"อย่างน้อย ๆ ก็ต้องไปขอโทษที่ฉันพูดอย่างนั้น"

# "I consider going to her room to find her, but she's probably still at the track."
"ทีแรกฉันคิดจะไปหาเอมิที่ห้อง แต่น่าจะยังอยู่ที่ลู่มั้ง"

scene bg school_courtyard
with locationskip

# "The steps out of the main building and down the path to the track make me feel like a doomed man."
"ฉันเดินออกจากอาคารหลักไปยังลู่วิ่งด้วยความรู้สึกหมดอาลัยตายอยาก"

# "I have a twisting, horrible feeling in my gut that this is all going to go horribly wrong, that I'm not going to accomplish anything."
"ในใจปั่นป่วนอย่างรุนแรงด้วยลางสังหรณ์ว่าจะต้องจบไม่สวย ว่าถ้าทำไปแล้วจะไม่ได้ผลอะไรขึ้นมาเลย"

# "Except for maybe driving the final nail in the coffin of whatever it was Emi and I had."
"ที่จะได้ผลอย่างเดียวก็คงเป็นการตอกฝาโลงส่งท้ายเยื่อใยอะไรก็ตามที่เอมิกับฉันมีต่อกัน"

stop music fadeout 2.0

scene bg school_track
with locationskip

# "There she is, just as expected, running laps around the track after everyone else has gone to shower and dinner."
"ตามคาด อยู่นั่นไง ยังวิ่งอยู่ที่ลู่ ส่วนคนอื่นไปอาบน้ำไปกินข้าวเย็นกันหมดแล้ว"

# "I don't wave, or even make my presence known. I just sit down on the bleachers and watch her run her laps."
"ฉันไม่โบกมือหรือเผยตัวตนให้ได้รับรู้ แค่นั่งอยู่บนสแตนด์เชียร์มองเอมิวิ่งไปเฉย ๆ"

show emi basic_confused_gym:
    center
    xpos 0.6
    easein 0.5 xpos 0.5
with charaenter

# "It takes her a few trips around the track before she notices me, after which she skids to a stop, eyes wide in surprise."
"เอมิวิ่งรอบลู่ได้สองสามรอบถึงเห็นฉัน เธอหยุดวิ่งทำตาโตด้วยความตกใจทันที"

show emi basic_annoyed_gym at center
with charachange

show emi basic_grin_gym
with charachange

# "Surprise is quickly masked by anger, which in turn fades behind a mask that I already know is impenetrable."
"สีหน้าโกรธปรากฏแทนความตกใจนั้นทันที แต่สีหน้านั้นก็หายลับไปอยู่เบื้องหลังหน้ากากที่ฉันรู้อยู่แล้วว่าอย่างไร\nก็คงไปถอดออกไม่ได้"

# emi "What are you doing here?"
emi "มาทำอะไรที่นี่"

# "Not quite the response I'd hoped for, but at this point I don't have much of a choice."
"ไม่เหมือนประโยคที่คาดไว้เท่าไหร่ แต่ตอนนี้ฉันไม่มีตัวเลือกมากแล้ว"

# hi "I wanted to apologize for what I said the other day."
hi "ฉันอยากมาขอโทษเรื่องที่พูดไปเมื่อวันก่อน"

show emi basic_confused_gym
with charachange

# emi "The other day?"
emi "วันก่อนเหรอ"

show emi basic_closedgrin_gym
with charachange

# "She laughs, a curt exclamation of disbelief."
"เอมิหัวเราะห้วน ๆ เหมือนไม่อยากเชื่อ"

play music music_sadness fadein 0.5

show emi basic_grin_gym
with charachange

# emi "It's been almost a week, Hisao."
emi "มันตั้งเกือบสัปดาห์แล้วนะฮิซาโอะ"

# hi "Yeah, well… better late than never, right?"
hi "อืม ก็… มาช้ายังดีกว่าไม่มานี่"

show emi sad_annoyed_gym
with charachange

# "Emi crosses her arms and stares at me coolly, as if sizing me up. Finally, she nods."
"เอมิกอดอกจ้องฉันด้วยสายตาเย็นชาราวจะพินิจพิจารณา จนสุดท้ายก็พยักหน้า"

show emi sad_grin_gym
with charachange

# emi "Hmmph. I suppose you're right. Water under the bridge, then. I forgive you."
emi "หืม ก็คงถูกของนาย งั้นก็ให้มันแล้วกันไปแล้วกัน ฉันให้อภัยนาย"

show emi basic_grin_gym
with charachange

# emi "Is that all?"
emi "แค่นี้ใช่มั้ย"

show emi basic_grin_gym:
    easeout 0.5 xpos 0.3 alpha 0.0
with Pause(0.5)

hide emi
with None

# "Her almost impatient question catches me so off-guard that she's halfway down the track before I think to shout after her."
"ฉันไม่ทันได้ตั้งตัวมาก ๆ กับคำถามรีบร้อนของเอมินั้นจนกว่าจะคิดได้ว่าต้องตะโกนเรียกเอมิก็เป็นตอนที่เธอ\nเดินกลับไปที่ลู่แล้ว"

# hi "No, wait!"
hi "ไม่ เดี๋ยวก่อน!"

show emi basic_annoyed_gym:
    center
    xpos 0.4
    easein 0.5 xpos 0.5
with charaenter

# "Emi stops, turns, and walks back to me, breathing a little heavily and looking annoyed at my interruption."
"เอมิหยุดเดินหมุนตัวเดินกลับมาหาฉันหายใจหอบเล็กน้อยพร้อมสีหน้าหงุดหงิดที่ฉันเรียกขัด"

# emi "What?"
emi "อะไร"

# "Okay, I need to make this right, somehow. I have to know where I stand, maybe patch things up."
"โอเค ต้องหาทางจัดการเรื่องนี้ให้ได้ ต้องรู้ตัวก่อนว่าตอนนี้ฉันอยู่ตรงไหนในความสัมพันธ์ และอาจจะขอคืนดีได้"

# hi "Can you at least sit down?"
hi "เธอนั่งก่อนได้มั้ย"

show emi sad_annoyed_gym at center
with charachange

# emi "I think we're okay talking here."
emi "คุยกันตรงนี้ก็ได้นี่"

# hi "Fine, sure. Look, about us…"
hi "โอเค ได้ คือว่านะ เรื่องของเรา…"

# "I pause, trying to think of a good way to phrase what I'm about to say."
"ฉันเว้นช่วงไปพลางนึกหาว่าจะพูดสิ่งที่คิดออกมาอย่างไรดี"

# "But before I can launch into an impassioned plea for giving me another chance, Emi's already spoken."
"แต่ก่อนที่ฉันจะทันได้คุกเข่าอ้อนวอนขอโอกาสจากเอมิอีกครั้งเธอก็พูดขึ้นมาก่อนแล้ว"

show emi sad_shy_gym
with charachange

# emi "There's no more us, Hisao."
emi "คำว่าเรามันไม่มีอีกต่อไปแล้วละฮิซาโอะ"

# hi "Why not?"
hi "ทำไมล่ะ"

show emi sad_pout_gym
with charachange

# emi "We're just not right for each other."
emi "เราเข้ากันไม่ได้"

# "She delivers this outrageous statement without even looking in my eyes."
"เอมิพูดประโยคแบบนั้นออกมาโดยไม่แม้แต่จะมองตาฉัน"

# hi "I don't believe you! We're great with one another!"
hi "ฉันไม่เชื่อ! เราเข้ากันได้ดีจะตาย!"

show emi basic_annoyed_gym
with charachange

# emi "Says the guy apologizing for getting thrown out of my house last week."
emi "ไอ้คนพูดน่ะยังมาขอโทษที่ทำตัวไม่ดีจนโดนไล่ออกจากบ้านเมื่อสัปดาห์ที่แล้วอยู่เลย"

# hi "It was a fight! I said something really, incredibly stupid and apologized for it!"
hi "ก็เราทะเลาะกันนี่! ฉันพูดอะไรโง่ ๆ เหลือเชื่อออกไปแล้วก็มาขอโทษนี่ไง!"

show emi sad_angry_gym
with charachange

# emi "And how many times had we already discussed the problem that started the fight? How many times had I told you that there was a set boundary that I wouldn't cross, and how many times did you keep trying to cross it?"
emi "แล้วเราคุยเรื่องนี้จนทะเลาะกันมากี่รอบแล้ว ฉันจะต้องบอกนายอีกกี่ครั้งว่าฉันก็มีขอบเขตที่ฉันขีดไว้ว่าจะไม่ข้าม\nกี่ครั้งแล้วที่นายพยายามจะข้ามเส้นนี้"

# hi "Because your boundary was stupid!"
hi "เพราะขอบเขตของเธอมันงี่เง่าไง!"

show emi sad_annoyed_gym
with charachange

# "Emi rolls her eyes, folds her arm across her chest, and cocks her head to the side."
"เอมิกลอกตากอดอกเอียงคอ"

# emi "Do you see this, Hisao? This is why we're not right for one another!"
emi "เห็นมั้ยฮิซาโอะ นี่ไงฉันถึงบอกว่าเราเข้ากันไม่ได้!"

# "Her voice softens a little, and she reaches out to stroke my cheek."
"น้ำเสียงเอมินุ่มนวลขึ้นเล็กน้อย เธอยื่นมือมาลูบแก้มฉัน"

show emi sad_grin_gym_close
with characlose

# emi "You're a good guy, but we're not going to work."
emi "นายเป็นคนดีนะ แต่เราไปกันไม่ได้หรอก"

# "With a horrible lurching feeling, I realize that she's been practicing this. Maybe every day since I left her house."
"ฉันเจ็บแปล๊บในใจขึ้นมาเมื่อรู้ตัวว่าเอมิคงซ้อมไว้แล้ว อาจจะซ้อมมาทุกวันตั้งแต่ที่ฉันออกมาจากบ้านเธอวันนั้น"

# "Even the cheek-stroke seems rehearsed, like something out of a movie."
"แม้แต่จังหวะการลูบยังเหมือนฝึกมา เหมือนเป็นฉากที่หลุดมาจากหนังเลย"

# "She never intended to give me another chance."
"เอมิไม่ได้คิดจะให้โอกาสฉันอีกครั้งอยู่แล้ว"

# "Hell, she probably would have been fine with never seeing me again."
"ไม่สิ ต่อให้ไม่ต้องเจอฉันเอมิก็คงอยู่ได้"

# hi "So that's it, then? Nothing else to say but “Gee, it was fun while it lasted, but so long?”"
hi "ก็คือจบกันเท่านี้เหรอ ไม่อะไรจะพูดแล้วงั้นสิ “เฮ้อ ตอนนั้นมันก็ดีนะ แต่ตอนนี้ขอลาก่อน” แค่นี้?"

show emi basic_closedgrin_gym_close
with charachange

# "This actually seems to amuse Emi far more than I wanted it to. She gives a rather morbid sounding chuckle."
"เหมือนเอมิจะชอบใจที่ฉันพูดอย่างนั้นมากกว่าที่ฉันคาดไว้ไปไกลโข เธอแค่นหัวเราะฟังดูขนลุก"

# emi "That's how I've lived my life, Hisao. You should know that by now."
emi "ฉันก็ใช้ชีวิตมาแบบนี้นี่ฮิซาโอะ ป่านนี้แล้วนายต้องรู้แล้วสิ"

show emi sad_grin_gym_close
with charachange

# emi "And it was fun."
emi "แล้วตอนนั้นมันก็ดีนะ"

# "A sad smile. She shivers slightly, and the smile vanishes."
"รอยยิ้มหมอง ๆ เอมิตัวสั่นเบา ๆ รอยยิ้มนั้นหายไป"

show emi sad_shy_gym_close
with charachange

# emi "But it's over now. It's for the best."
emi "แต่ตอนนี้มันจบแล้ว เป็นแบบนี้แหละดีที่สุดแล้ว"

# "I want to yell, to scream at her. Make her see reason, that this is stupid, the whole act. That she's just afraid of me, afraid of what being close to someone means."
"ฉันอยากจะกรีดร้องก้องตะโกนใส่เอมิ อธิบายให้เอมิตาสว่างสักทีว่าการที่เธอทำตัวอย่างนี้มันงี่เง่า ว่าเธอแค่กลัวฉัน\nกลัวการสนิทกับใครสักคน"

# "I want to tell her that I love her and that I can't just give up on her at the drop of a hat."
"ฉันอยากจะบอกเอมิว่าฉันรักเธอ ว่าฉันไม่อาจปล่อยมือเธอไปได้ง่าย ๆ เช่นนั้น"

# "Except… there's no point. She's made up her mind. We're done."
"หากแต่ว่า… ต่อให้บอกไปก็ไม่มีความหมาย เอมิตัดสินใจได้แล้ว เราจบกันแล้ว"

# hi "Fine."
hi "ก็ได้"

show emi sad_grin_gym_close
with charachange

# "Emi nods, satisfied. I want to hit something."
"เอมิพยักหน้าพอใจ ฉันอยากหาของมาทุบมาต่อยเหลือเกิน"

# emi "Good."
emi "ดี"

show emi basic_grin_gym_close
with charachange

# "She brightens with a false cheeriness."
"เอมิยิ้มด้วยความร่าเริงจอมปลอม"

# emi "See you around, Hisao."
emi "ไว้เจอกันนะฮิซาโอะ"

# hi "No you won't. You won't even try."
hi "ไม่ เธอจะไม่มาเจอฉันหรอก เธอจะไม่ตามหาตัวฉันด้วยซ้ำ"

show emi basic_grin_gym_close:
    easeout 0.5 xpos 0.3 alpha 0.0
with Pause(0.5)

hide emi
with None

# "She shrugs, as if to say “Have it your way,” and turns her back on me once more, quickly accelerating around the curve of the track."
"เอมิยักไหล่ราวกับจะพูดว่า “ตามใจเลย” แล้วหันหลังให้ฉันอีกครั้งแล้วเร่งฝีเท้าขึ้นวิ่งไปตามลู่"

# "I feel numb. This is it. The end of the road for us, whatever that was. Closure, at least."
"ทั้งตัวฉันชาดิก จบแล้ว ตรงนี้คือปลายทางของสองเรา สภาพแบบนี้แหละ แต่อย่างน้อยก็ได้ส่งท้าย"

# "Emi rounds the track again without sparing me a second glance. She's running much faster now, and I can't help but think of that first run together."
"เอมิวิ่งรอบลู่อีกครั้งโดยไม่มองมาทางฉันเลย ตอนนี้เธอวิ่งเร็วกว่าเมื่อครู่มากแล้ว ฉันอดนึกถึงครั้งนั้นที่เราวิ่งด้วยกัน\nเป็นครั้งแรกไม่ได้"

# "I ran to catch you, to try to prove I wasn't as weak as I knew I was. But it ended badly for me, didn't it?"
"ฉันวิ่งไล่ตามเธอ เพื่อจะพิสูจน์ว่าฉันไม่ได้อ่อนแออย่างที่คิด แต่สุดท้ายก็จบไม่สวยนี่นะ"

# "And now, you're off running too fast for me again, and I have the choice to run after you again."
"ตอนนี้เธอก็วิ่งเร็วเกินกว่าที่ฉันจะตามทันอีกแล้ว และฉันก็เลือกที่จะวิ่งตามเธออีกครั้งได้"

# "But I won't. Not this time. You'd never let me catch you."
"แต่ไม่หรอก คราวนี้ฉันไม่เลือกแบบนั้น เธอไม่เคยปล่อยให้ฉันตามได้ทันเลย"

stop music fadeout 6.0

scene bg school_dormhisao
with shorttimeskip

# "I don't even notice walking away from the track, or walking into my room, or pulling a book out of my bag to read."
"ฉันไม่รู้ตัวด้วยซ้ำตอนทีเดินออกมาจากลู่ ตอนที่เดินกลับมาที่ห้อง ตอนที่หยิบหนังสือในกระเป๋าออกมาอ่าน"

# "Just before bed, I reset my alarm. Emi and I have had our final encounter."
"ก่อนนอนฉันตั้งนาฬิกาปลุกใหม่ เอมิกับฉันส่งลากันเรียบร้อยแล้ว"

scene black
with shuteye

# "We don't speak again after that."
"หลังจากนั้นเราก็ไม่คุยกันอีกเลย"

#BAD ENDED, loser.



label th_E27b:
#If you picked 2:

# "Well, I suppose someone else knowing about my problem can't hurt. Heck, maybe Misha can even offer some advice."
"ก็นะ ให้ใครสักคนรับรู้ปัญหาฉันด้วยคงไม่เสียหายหรอก ไม่สิ มิช่าอาจให้คำแนะนำอะไรได้ด้วยซ้ำ"

# hi "We had a fight at her house."
hi "พอดีทะเลาะกันที่บ้านเอมิน่ะ"

# hi "I keep trying to get close to her, and she won't let me get close, and…"
hi "ฉันคอยจะเข้าใกล้ชิดกับเอมิ แล้วเอมิก็ไม่ยอม แล้ว…"

# hi "I said something stupid, and she threw me out."
hi "ฉันก็พูดอะไรโง่ ๆ ออกไปจนโดนเอมิไล่ออกจากบ้าน"

show misha perky_sad
with charachange

# mi "Have you talked to her since then?"
mi "แล้วหลังจากวันนั้นได้คุยกันอีกมั้ย"

# "Misha looks genuinely concerned. I'm surprised, as I'd almost expected her to drop the subject after finding out what the trouble was."
"มิช่าดูเป็นห่วงจริง ๆ แปลกใจเหมือนกัน ฉันก็นึกว่าพอรู้ว่ามีปัญหาอะไรกันแล้วมิช่าจะปัดเรื่องนี้ทิ้งไปเสียอีก"

# "Even more surprising is how quickly I find myself spilling my guts to her."
"ที่น่าแปลกใจกว่านั้นคือฉันยังคงเล่าเรื่องให้มิช่าฟังต่อทันที"

# hi "No, I haven't. I just can't bring myself to face her after that."
hi "ไม่ ไม่ได้คุยเลย ฉันไม่กล้าไปเจอหน้าเอมิแล้ว"

# hi "I made a complete fool of myself, and she probably hates me now anyway. Especially since I haven't seen her since then."
hi "ฉันคงดูงี่เง่ามาก แล้วตอนนี้เอมิก็คงเกลียดฉันไปแล้ว ยิ่งหลังจากนั้นไม่ได้ไปเจอหน้าเอมิอีก"

show misha sign_smile
with charachange

# mi "You're pretty slow, Hicchan."
mi "ฮิจังนี่หัวช้าจังนะ"

stop music fadeout 4.0

# "This doesn't sound like advice."
"ฟังดูไม่เหมือนคำแนะนำเท่าไหร่"

# hi "Huh?"
hi "ฮะ?"

show misha hips_frown
with charachange

# "Misha places her hands on her hips and launches into a speech that would sound more plausible coming from Shizune."
"มิช่ายืนเท้าสะเอวแล้วเปิดปากพูดสิ่งที่น่าจะเป็นคำพูดของชิซูเนะมากกว่า"

# mi "The solution to your problem is simple! You have to go and apologize to her! Leaving things like this will just make things worse!"
mi "ทางแก้มันง่ายนิดเดียว! ไปขอโทษเอมิสิ! ปล่อยไว้แบบนี้เรื่องมันจะยิ่งไปใหญ่นะ!"

# mi "You can't know that she hates you now unless she tells you! Otherwise, there's no evidence that what you fear is true!"
mi "ถ้าเอมิยังไม่ได้พูดแบบนั้นแล้วนายจะรู้ได้ไงว่าเอมิเกลียดนาย! ถ้าไม่ได้พูดก็ไม่มีหลักฐานว่าเป็นอย่างที่นายกลัวจริง!"

# mi "And if you really care about her, shouldn't you be worried about how she's taking all this?"
mi "และถ้าเอมิสำคัญกับนายจริง ๆ นายต้องคิดถึงใจเอมิสิว่าจะคิดยังไงกับเรื่องนี้"

play music music_innocence fadein 1.0

# "With a sudden start, I realize that she's right. I've kept waking up to an early alarm because part of me wants to meet Emi at the track for our runs."
"ฉันสะดุ้งเมื่อคิดได้ว่ามิช่าพูดถูก ฉันตื่นเช้าตามที่ตั้งนาฬิกาปลุกไว้เพราะใจหนึ่งฉันยังอยากไปเจอเอมิที่ลู่วิ่งตอนเช้า"

# "I've kept running, because I know that Emi would worry about me if I didn't stay healthy."
"ฉันยังวิ่งเพราะรู้ว่าเอมิจะเป็นห่วงถ้าฉันไม่รักษาสุขภาพตัวเอง"

# "When I went on the roof yesterday, I was half-hoping that she would be up there, and felt disappointed when she wasn't."
"และเมื่อวานที่ฉันไปดาดฟ้าเพราะใจหนึ่งฉันหวังว่าเอมิจะอยู่บนนั้น และพอไม่เจอก็ผิดหวัง"

# hi "I'm an idiot."
hi "ฉันมันโง่"

show misha hips_grin
with charachange

# mi "Kinda, Hicchan~!"
mi "คงงั้นแหละฮิจัง~!"

show misha sign_smile
with charachange

# mi "So~!  Go and apologize to her as soon as you can, okay~?"
mi "เพราะงั้น~! รีบ ๆ ไปขอโทษเอมิซะนะ~"

# "I open my mouth to say that I'll do it right away, but the lunch bell rings and I realize that I still have afternoon classes to attend."
"ฉันอ้าปากเตรียมตอบว่าจะไปเดี๋ยวนี้ แต่ระฆังพักเที่ยงก็ดัง และฉันก็นึกได้ว่ายังมีเรียนคาบบ่ายอยู่"

# hi "First thing after class is over, I'll go see her. I promise."
hi "งั้นพอเลิกเรียนแล้วฉันจะไปหาเอมิเลย สัญญา"

# hi "And uh, thanks for the advice, I guess."
hi "แล้วก็ เอ่อ ขอบคุณสำหรับคำแนะนำนะ"

show misha hips_grin
with charachange

# "Misha beams at me, as if I were a child that had just learned his ABCs."
"มิช่ายิ้มให้ราวกับว่าฉันเป็นเด็กที่เพิ่งหัดอ่านได้เป็นครั้งแรก"

# mi "Good! I'll let Shicchan know that you're okay, then~!"
mi "เยี่ยม~! งั้นเดี๋ยวไปบอกชิจังว่าฮิจังโอเคแล้ว~!"

# hi "Er, yeah. You do that."
hi "เอ่อ อื้ม เอาเลย"

hide misha
with charaexit

# "With a wave (and completely disregarding the fact that people are starting to trickle back into the classroom, as opposed to out of it), Misha departs the classroom."
"มิช่าโบกมือ (โดยไม่สนเลยว่าคนเริ่มทยอยเข้าห้องเรียนกัน ไม่ใช่เดินไปอีกทาง) แล้วออกจากห้องเรียนไป"

# "I suppose she and Shizune have student council business again."
"สงสัยคงต้องไปทำงานสภานักเรียนอะไรกับชิซูเนะอีกนั่นแหละมั้ง"

scene bg school_scienceroom
with shorttimeskip

# "While the afternoon wears on, I find myself impatient for lessons to end. I need to see Emi now."
"เวลาช่วงบ่ายผ่านไปโดยที่ฉันอดใจรอให้เลิกเรียนไม่ไหวแล้ว ต้องไปหาเอมิตอนนี้เลย"

# "I have to try to set things right. Even if Emi hates me now, I have to at least apologize."
"ฉันต้องลองจัดการอะไร ๆ ดูก่อน ถ้าตอนนี้เอมิเกลียดฉันแล้วอย่างน้อยฉันก็ต้องขอโทษ"

# "I owe her that much."
"ฉันต้องชดใช้เอมิถึงเพียงนั้นแหละ"

# "Should I meet her in her room? No, I decide, it would delay things too much. If I know Emi, then I can find her at the track."
"จะไปหาที่ห้องเอมิดีมั้ย ไม่ ไม่ดีกว่า ไม่งั้นคงช้าไป เท่าที่รู้จักกันมาก็ต้องไปหาที่ลู่วิ่งนี่แหละ"

# "Still have no idea what I'm going to say when I get there, but I take comfort in knowing that Emi probably wouldn't have a plan for something like this either."
"ยังไม่รู้เลยว่าพอไปถึงแล้วจะพูดอะไรดี แต่ฉันก็นึกปลอบใจตัวเองว่าเอมิก็คงไม่ได้คิดเหมือนกันว่าจะต้องเจออะไร\nแบบนี้"

# "Play it by ear. Stop being nervous, and just get to the track. Figure the rest out when I get there."
"ด้นสดไป เลิกประหม่า ไปที่ลู่วิ่ง พอไปถึงก็ค่อยคิดอีกที"

scene bg school_track
with shorttimeskip

# "The track looms ahead, and another jolt of nerves hits me in the gut. I resist the urge to turn and walk away, and instead note with satisfaction that I was right and Emi is still running."
"ลู่วิ่งอยู่เบื้องหน้า ฉันนึกประหวั่นขึ้นมาอีกรอบ แต่ก็กลั้นใจไม่เดินกลับแล้วนึกพอใจว่าฉันคิดถูกแล้วที่เอมิวิ่งอยู่ที่ลู่"

# "I don't make myself immediately known; I find a seat in the bleachers and watch her run instead, thinking back to earlier meetings."
"ฉันไม่ได้ไปหาให้รู้ว่ามาในทันที ฉันนั่งบนสแตนด์เชียร์มองเอมิวิ่งไปพลางคิดถึงเรื่องที่คุยกับมิช่าเมื่อก่อนหน้านี้"

show emi basic_confused_gym:
    center
    xpos 0.6
    easein 0.5 xpos 0.5
with charaenter

# "After a few trips around the track, Emi notices me and skids to a halt, an expression of surprise that slides easily into one of anger."
"เอมิวิ่งรอบลู่ได้สองสามรอบถึงเห็นฉัน เธอหยุดวิ่งทำหน้าตกใจก่อนจะเปลี่ยนเป็นสีหน้าโกรธในทันที"

show emi basic_annoyed_gym at center
with charachange

# emi "What are you doing here?"
emi "มาทำอะไรที่นี่"

# "Not quite the response I'd hoped for, but at this point I don't have much of a choice."
"ไม่เหมือนประโยคที่คาดไว้เท่าไหร่ แต่ตอนนี้ฉันไม่มีตัวเลือกมากแล้ว"

# hi "I wanted to apologize for what I said the other day."
hi "ฉันอยากมาขอโทษเรื่องที่พูดไปเมื่อวันก่อน"

show emi basic_confused_gym
with charachange

# emi "The other day?"
emi "วันก่อนเหรอ"

show emi basic_closedgrin_gym
with charachange

# "She laughs, a curt exclamation of disbelief."
"เอมิหัวเราะห้วน ๆ เหมือนไม่อยากเชื่อ"

show emi basic_grin_gym
with charachange

# emi "It's been almost a week, Hisao."
emi "มันตั้งเกือบสัปดาห์แล้วนะฮิซาโอะ"

# hi "Yeah, well… better late than never, right?"
hi "อืม ก็… มาช้ายังดีกว่าไม่มานี่"

show emi sad_annoyed_gym
with charachange

# "Emi crosses her arms and stares at me coolly, as if sizing me up. Finally, she nods."
"เอมิกอดอกจ้องฉันด้วยสายตาเย็นชาราวจะพินิจพิจารณา จนสุดท้ายก็พยักหน้า"

show emi sad_grin_gym
with charachange

# emi "Hmmph. I suppose you're right. Water under the bridge, then. I forgive you."
emi "หืม ก็คงถูกของนาย งั้นก็ให้มันแล้วกันไปแล้วกัน ฉันให้อภัยนาย"

show emi basic_grin_gym
with charachange

# emi "Is that all?"
emi "แค่นี้ใช่มั้ย"

show emi basic_grin_gym:
    easeout 0.5 xpos 0.3 alpha 0.0
with Pause(0.5)

hide emi
with None

# "Her almost impatient question catches me so off-guard that she's already halfway down the track before I think to shout after her."
"ฉันไม่ทันได้ตั้งตัวมาก ๆ กับคำถามรีบร้อนของเอมินั้นจนกว่าจะคิดได้ว่าต้องตะโกนเรียกเอมิก็เป็นตอนที่เธอ\nเดินกลับไปที่ลู่แล้ว"

# hi "No, wait!"
hi "ไม่ เดี๋ยวก่อน!"

scene bg school_track_on
with locationchange

# "She doesn't seem to have heard me - or she doesn't want to hear me - and so I give chase, disregarding completely the fact that I am not dressed for it."
"เอมิเหมือนจะไม่ได้ยิน หรือไม่ก็ไม่อยากได้ยิน ฉันจึงไล่ตามเอมิไปโดยไม่สนว่าไม่ได้ใส่ชุดมาวิ่ง"

scene bg school_track_running
with Dissolve(2.0)

# "My feet hurt, and my shirt collar feels like a noose around my neck, but I still chase after her, because if I don't I'll lose my chance."
"ปวดเท้าไปหมด คอเสื้อก็เหมือนเป็นบ่วงที่รัดคอไว้ แต่ฉันยังวิ่งตามเอมิไป เพราะถ้าไม่ตามไปแล้วฉันก็คงเสียโอกาส"

# "Emi hasn't started to really accelerate yet, which is probably the only reason why I'm able to catch up to her, to reach out and tap her on the shoulder, just before my legs give up running in dress shoes and stumble to a stop."
"เอมิยังไม่เร่งฝีเท้าเต็มที่ อาจจะเพราะแบบนี้ฉันถึงยังไล่ตามเอมิทันอยู่ ฉันยื่นมือไปแตะไหล่เอมิไว้ทันก่อนที่ขาฉัน\nที่ใส่รองเท้าหนังไว้จะหมดแรงแล้วทรุดลงพอดี"

scene bg school_track_on
with Dissolve(2.0)

# "Surprisingly (fortunately?) all that running seems to have paid off. I'm short of breath, yes, but at least my heart isn't actively trying to force its way out of my ribcage."
"น่าแปลกใจ (และโชคดี?) ที่การวิ่งของฉันที่ผ่านมานั้นมีประโยชน์ขึ้นมา ฉันหอบอยู่ก็จริง แต่อย่างน้อยฉันก็ไม่ได้\nเจ็บหน้าอกจนเหมือนหัวใจจะหลุดจากซี่โครง"

show emi basic_confused_gym_close at center
with charaenter

# "My touch on her shoulder has stopped Emi, and while there is a flash of concern when she sees me catching my breath, it seems that she has a good idea of what I'm capable of too."
"เอมิหยุดวิ่งเมื่อฉันแตะไหล่ แวบหนึ่งเอมิดูเป็นห่วงที่เห็นฉันหอบอย่างนี้ และดูจะรู้เหมือนกันว่าฉันวิ่งได้ขนาดไหนแล้ว"

# "The concern is short-lived."
"แต่ก็เป็นห่วงอยู่แค่ชั่วขณะเท่านั้น"

show emi basic_annoyed_gym_close
with charachange

# emi "What?"
emi "อะไร"

# "She seems so irritated by my being still there that I almost lose my nerve, but I've lost my nerve enough."
"เอมิดูหงุดหงิดที่ฉันยังอยู่ตรงนี้จนฉันแทบสติหลุด แต่ฉันสติหลุดมาหลายครั้งแล้ว"

# hi "I need to explain myself. Why I can't just let the matter rest."
hi "ขออธิบายอะไรหน่อย ว่าทำไมฉันถึงปล่อยเรื่องนี้ไว้เฉย ๆ ไม่ได้"

show emi sad_annoyed_gym_close
with charachange

# "Emi folds her arms and bounces one blade on the ground in an approximation of tapping her foot impatiently. Angry as she is, and as nervous as I am, she still looks beautiful."
"เอมิกอดอกแล้วตบแผ่นขาเทียมกับพื้นขึ้นลงคล้ายการกระดิกเท้าเมื่อร้อนใจ ทั้งที่เธอโกรธขนาดนี้ ทั้งที่ฉันประหม่า\nขนาดนี้ แต่เธอก็ยังดูสวยเหลือเกิน"

# emi "Okay, Hisao. Explain."
emi "โอเค ฮิซาโอะ อธิบายมา"

# hi "The thing is, I know that you're really sensitive about the accident and about your dad."
hi "เรื่องคือ ฉันรู้ว่าเธออ่อนไหวกับเรื่องอุบัติเหตุนั้นกับเรื่องพ่อของเธอมาก"

# "I can see Emi's face twitch at the mention of the two things that have been steadily driving us apart, or at least made me feel like we're being driven apart."
"ฉันเห็นหน้าเอมิกระตุกไปเมื่อพูดถึงสองอย่างนั้นที่คอยถ่างเราสองคนห่างออกจากกัน ฉันคนหนึ่งแหละที่รู้สึกแบบนั้น"

# hi "But that's why I want to know about them, I think."
hi "แต่เพราะแบบนี้แหละฉันถึงได้อยากรู้สองเรื่องนั้น คิดว่านะ"

# hi "Because I see how much they hurt you, and I want to be there to comfort you."
hi "เพราะฉันอยากรู้ว่าเรื่องพวกนั้นทำให้เธอเจ็บปวดแค่ไหน และอยากอยู่เคียงข้างคอยปลอบประโลมเธอ"

# hi "It makes me miserable, seeing you sleepless and depressed - and don't pretend you aren't, because I know, okay?"
hi "ฉันทนเห็นเธอที่ทั้งนอนไม่หลับทั้งหดหู่ไม่ได้เลย แล้วก็อย่าแสร้งทำเป็นว่าไม่ใช่อย่างนั้นนะ ฉันรู้"

# hi "I just remember that night when you fell asleep with me and had that nightmare, and that you were happy to have me there when you woke up."
hi "ฉันนึกถึงคืนนั้นที่เธอหลับกับฉันแล้วฝันร้าย คืนนั้นที่เธอดีใจที่ตื่นมาแล้วเจอฉัน"

# hi "I want to be able to be there for you like that whenever you need me to be."
hi "ฉันอยากอยู่เคียงข้างเธอแบบนั้นทุกครั้งที่เธอต้องการ"

show emi sad_depressed_gym_close
with charachange

# "The stern face cracks, slightly. Emi interrupts before I can continue further."
"สีหน้าเคร่งขรึมของเอมิคลายลงเล็กน้อย เธอขัดขึ้นมาก่อนที่ฉันจะทันได้พูดต่อ"

# emi "Just… stop right there. We can't see each other any more, okay?"
emi "พอ… เลย เรามาเจอกันอีกไม่ได้แล้ว โอเคนะ"

show emi sad_pout_gym_close
with charachange

# "She's rushing now, looking everywhere but at me. I'm surprised she doesn't bolt, she knows I can't catch her…"
"เอมิร้อนรนมองซ้ายมองขวาไม่ยอมสบตา ฉันแปลกใจที่เอมิไม่วิ่งหนีไปทั้งที่รู้ว่ายังไงฉันก็ตามไม่ทัน…"

# emi "We're not… we're not right for one another."
emi "เรา… เราเข้ากันไม่ได้"

# hi "That's not true, and you know it."
hi "ไม่จริงสักหน่อย เธอก็รู้ดีนี่"

show emi sad_shy_gym_close
with charachange

# emi "No, it's true. You're too—"
emi "จริง จริงสิ นายน่ะ—"

# hi "I know. I know that I've been pushy about knowing your past."
hi "ฉันรู้ ฉันรู้ว่าฉันคอยตามตื๊อเรื่องอดีตเธอมาตลอด"

# hi "If you can't tell me yet, then at least let me be there even if I don't know the reason."
hi "ถ้ายังบอกตอนนี้ไม่ได้ อย่างน้อยก็ขอให้ฉันได้อยู่เคียงข้างเธอเถอะ ต่อให้ฉันจะไม่รู้สาเหตุก็ช่าง"

# hi "It's okay, I promise. I won't ask why you need comfort, I'll just give it freely."
hi "ไม่เป็นไรหรอก ฉันสัญญา ฉันจะไม่ถามเลยว่าทำไมถึงอยากให้ฉันปลอบใจ ฉันจะปลอบเธอให้เต็มที่เลย"

show emi sad_depressed_gym_close
with charachange

# "Emi's shaking her head, and tears seem to be threatening the corners of her eyes."
"เอมิสั่นหัว น้ำตาเธอรื้นขึ้นมาในขอบตา"

# emi "Stop saying that!"
emi "เลิกพูดแบบนั้นได้แล้ว!"

# hi "Why? Because you're afraid you'll take me up on it?"
hi "ทำไมเหรอ เพราะกลัวว่าเธอจะยอมรับที่ฉันเสนอไปงั้นเหรอ"

show emi sad_pout_gym_close
with charachange

# emi "I'm not afraid!"
emi "ฉันไม่ได้กลัว!"

# "I can't keep the chiding tone from my voice as I respond."
"ฉันอดทำน้ำเสียงดุตอบเอมิไปไม่ได้"

# hi "Yes, you are. You told me so yourself, remember? That's okay, really it is."
hi "กลัว กลัวสิ เธอบอกเองนี่ จำได้มั้ย แต่ไม่เป็นไรหรอก ไม่เป็นไรเลย"

# hi "However, it seems to me that someone who'd manage to come out of that wreck and still be as energetic and cheerful as you are would be determined enough to face that fear."
hi "ฉันมองว่าคนที่ผ่านพ้นอุบัติเหตุมาได้แล้วยังสดใสร่าเริงได้อย่างเธอน่ะแน่วแน่พอที่จะเผชิญหน้ากับความกลัวนั้น"

show emi sad_angry_gym_close
with charachange

# emi "Determination? What do you know about determination?"
emi "แน่วแน่เหรอ นายรู้เหรอว่าความแน่วแน่คืออะไร"

# hi "I know that there's a girl so determined to take care of a total stranger that she'd steal his food at a festival."
hi "ฉันรู้ว่ามีเด็กผู้หญิงคนหนึ่งที่แน่วแน่พอจะดูแลคนที่ไม่ได้รู้จักกันเลยถึงขั้นฉกอาหารตอนงานเทศกาลไปกินเอง"

# hi "I know that there's a girl so determined to help me with my own problems that she'd draw up a complete dietary and exercise plan, and that she'd not only draw up the plans, but she'd follow them with me, even when she couldn't run."
hi "ฉันรู้ว่ามีเด็กผู้หญิงคนหนึ่งที่แน่วแน่พอจะช่วยฉันถึงขั้นทำตารางออกกำลังกายกับแผนการกินให้เสร็จสรรพ\nแล้วยังออกกำลังกายเป็นเพื่อนทั้งที่ตัวเองก็วิ่งไม่ได้"

# hi "Determined enough to keep me at arm's length that she'd put herself through emotional pain if she thought it was the right thing to do."
hi "แน่วแน่พอที่จะเว้นระยะกับฉัน ยอมให้ตัวเองรับมือกับบาดแผลทางจิตใจเพราะคิดว่าต้องทำอย่างนั้น"

# hi "Although, there's one thing that this determined girl didn't quite plan for, which was that I might feel that same kind of determination to keep her from being hurt."
hi "แต่ทว่ายังมีอย่างหนึ่งที่เด็กสาวผู้แน่วแน่คนนี้ลืมคิด ลืมคิดว่าฉันเองก็อาจแน่วแน่อยากปกป้องไม่ให้เธอคนนี้\nบาดเจ็บเหมือนกัน"

# hi "I fell in love with you, and I refuse to let that be thrown away because you're afraid of losing me."
hi "ฉันตกหลุมรักเธอ และฉันจะไม่ยอมทิ้งความรักนี้ไปแค่เพราะเธอกลัวว่าจะเสียฉันแน่นอน"

show emi excited_sad_gym_close
with charachange

# "What little control Emi still has at this point cracks, and I find myself suddenly enveloped in her embrace as she cries."
"เอมิที่เมื่อครู่กำลังอดกลั้นอยู่อย่างหนักคุมตัวเองไว้ไม่อยู่แล้ว อยู่ ๆ เธอก็เข้ามากอดฉันพลางร้องไห้"

# emi "Why are you doing this? Why can't you just leave me alone?"
emi "ทำไมนายถึงทำแบบนี้ ทำไมนายถึงมายุ่งกับฉันอีก"

show ev emi_forehead
with dissolve

# "I hold her close and plant a kiss on the top of her head."
"ฉันกอดเธอกลับแล้วจุ๊บหน้าผาก"

# hi "I'm sorry, Emi. You helped me when I first arrived, so now I have to help you. It's only fair."
hi "ขอโทษนะเอมิ ตอนฉันมาใหม่ ๆ เธอช่วยฉันแล้ว ฉันก็ต้องช่วยเธอเป็นการตอบแทนบ้าง"

# emi "You're utterly hopeless, did you know that?"
emi "นายนี่มันเกินเยียวยาแล้วนะรู้ตัวมั้ย"

# "She hiccups and trembles a little."
"เอมิสะอื้นตัวสั่นเบา ๆ"

# hi "Funny, I could say the same about you."
hi "ย้อนแย้งดี เธอเองก็เหมือนกันนี่"

# emi "Can you do something for me, Hisao?"
emi "รบกวนอะไรอย่างได้มั้ยฮิซาโอะ"

# hi "Anything."
hi "ว่ามาเลย"

scene bg school_track_on
show emi sad_shy_gym_close at center
with charachange

# emi "Can you go, now?"
emi "นายไปก่อนได้มั้ย"

# "It feels like she's just shoved a knife through my chest."
"ฉันรู้สึกเหมือนเอมิเอามีดปักลงที่กลางใจ"

# hi "Go?"
hi "ไป?"

show emi sad_pout_gym_close
with charachange

# emi "I need to… I need to think, okay?"
emi "ฉัน… ฉันขอเวลาคิดก่อน โอเคนะ"

# emi "I can't just tell you everything yet. I'm still scared, and when you're around, I can't think clearly."
emi "ตอนนี้ฉันยังบอกอะไรกับนายไม่ได้ ฉันยังกลัว แล้วพอนายอยู่ด้วยฉันก็คิดอะไรไม่ค่อยออก"

# emi "But do me another favor."
emi "แล้วก็รบกวนอีกอย่างด้วย"

# hi "What's that?"
hi "อะไรเหรอ"

show emi sad_grin_gym_close
with charachange

# emi "Show up for our morning run tomorrow?"
emi "เช้าพรุ่งนี้มาวิ่งด้วยกันนะ"

# "I smile, feeling better than I have all week."
"ฉันยิ้ม ในใจรู้สึกดีกว่าที่เคยรู้สึกมาตลอดทั้งสัปดาห์"

# hi "Of course. I wouldn't miss it for the world."
hi "ได้สิ อะไรก็ฉุดฉันไม่ได้หรอก"

show emi sad_grin_gym
with charadistant

# "Emi steps back slowly, almost reluctantly. She sniffles a little and then grins at me, a real smile that lights up the track, overpowering the fading evening's light."
"เอมิถอยไปช้า ๆ เหมือนยังไม่อยากปล่อย เธอสูดสะอื้นเบา ๆ แล้วส่งยิ้มให้ฉัน เป็นรอยยิ้มที่แท้จริงซึ่งทำให้ทั้งลู่วิ่ง\nสดใสขึ้นมา สว่างยิ่งเสียกว่าแสงยามเย็นที่หรี่ลงทุกขณะ"

show emi basic_grin_gym
with charachange

# emi "See you tomorrow, Hisao."
emi "เจอกันพรุ่งนี้นะฮิซาโอะ"

# hi "Okay."
hi "โอเค"

show emi excited_amused_gym_close
with characlose

show emi basic_grin_gym
with charadistant

# "She darts forward suddenly, planting a soft kiss on my lips, then steps back shyly."
"อยู่ ๆ เอมิก็โน้มตัวเข้ามาจุ๊บแล้วถอยไปอาย ๆ"

show emi basic_grin_gym:
    easeout 0.5 xpos 0.3 alpha 0.0
with Pause(0.5)

hide emi
with None

# "Spinning on her back foot, she takes off running again, and I know that our conversation's at an end."
"ฉันรับรู้ว่าบทสนทนาของเราจบลงแล้วเมื่อเอมิหมุนเท้าแล้วออกวิ่งอีกครั้ง"

# "My lips tingle with the warmth of that brief kiss and the memories of other, longer kisses."
"สัมผัสอบอุ่นจากรอยจูบสั้น ๆ เมื่อครู่นั้นกับความทรงจำจากรอยจูบอื่นที่นานกว่านั้นแผ่ซ่านอยู่กับริมฝีปากฉัน"

# "I walk back to my room with a spring in my step."
"ฉันเดินกลับห้องตัวเองอย่างอารมณ์ดี"

# "Tomorrow when my alarm goes off, I'll get up."
"แล้วพรุ่งนี้ฉันจะตื่นขึ้นเมื่อเสียงนาฬิกาปลุกดัง"

stop music fadeout 2.0

window hide

return
