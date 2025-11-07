label th_S17:

window hide None

scene bg school_hallway3
with locationchange

nvl clear
nvl show dissolve

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_normal fadein 3.0

# n "\n\nThe following days pass uneventfully and with surprising quickness. I find renewed motivation to learn sign language. It seems that I have a knack for learning sign, so it would be a waste to not do it, and falling behind would be even more unacceptable."
n "\n\nวันถัดมานั้นผ่านไปโดยไม่มีอะไรเป็นพิเศษ ทั้งยังผ่านไปไวเหลือเชื่ออีกต่างหาก ชักรู้สึกอยากเรียนภาษามือขึ้นมา\nอีกแล้วสิ ดูท่าว่าฉันพอจะเรียนภาษามือได้ดีด้วย จะล้มเลิกไปก็คงเสียดายความสามารถ แล้วยิ่งถ้าเรียนตามไม่ทัน\nก็ยิ่งหนักเข้าไปอีก"

# n "Summer break is coming up. Even though I figured that student council work would see a drop-off proportional to how lethargic my classes are becoming, it doesn't happen that way. Every day, I get swamped under increasingly meaningless work."
n "ใกล้ปิดเทอมฤดูร้อนแล้ว ทีแรกเห็นสภาพแต่ละวิชาที่เริ่มอืด ๆ แล้วก็นึกว่างานสภานักเรียนจะลดหลั่นลงตามไปบ้าง\nแต่ไม่เลย ทุก ๆ วันมีแต่งานไร้สาระอะไรไม่รู้ท่วมหัวไปหมด"

# n "Despite how much I want to, I don't have even a free second to talk to Shizune nowadays. Every time I look at her, her face is buried in some book of records or some stack of papers that need to be checked over in triplicate."
n "ใจจริงก็อยากคุยกับชิซูเนะแทบตาย แต่ทุกวันนี้แทบจะไม่มีเวลาว่างเลยสักวินาที พอหันไปมองทีไรก็เห็นเอาหน้าจม\nอยู่กับกองบันทึกหรือไม่ก็เอกสารอะไรที่ต้องตรวจดูซ้ำสามครั้ง"

# n "\n\nToday, I woke up early to come to school before everyone else, hoping to catch Shizune. She has a habit of coming in first thing in the morning, to be more punctual than all the other students. Unfortunately, I think I am earlier than her."
n "\n\nวันนี้ฉันตื่นเช้าเพื่อมาโรงเรียนก่อนใครด้วยหวังว่าจะได้เจอกับชิซูเนะ ปกติเธอจะมาเช้าเป็นคนแรกตรงเวลากว่า\nใครคนอื่นเสมอเป็นนิสัย แต่โชคไม่ดีที่ดูเหมือนว่าฉันจะมาเช้ากว่าเธอเสียอีก"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

play sound sfx_doorclose

window show

# "Hearing the student council room door click closed to my right tells me that isn't the case. I guess I got here just behind her."
"เมื่อได้ยินเสียงปิดประตูห้องสภานักเรียนที่ดังมาจากทางด้านขวาแล้วฉันก็ได้รู้ว่าไม่ใช่อย่างที่คิด สงสัยฉันคงจะมาช้ากว่า\nไปนิดหน่อย"

play sound sfx_dooropen

scene bg school_council
with locationchange

# "I enter the room and tap Shizune on the shoulder to get her attention."
"ฉันเข้าไปในห้องแล้วแตะ ๆ ไหล่ ให้เธอหันมา"
#i don't get this sequence of events at all
#You know how you remove the "X smiles" lines because they say things you should direct instead? This is how things look without them. For example, I expected to open at Hisao's room, and a series of BG changes until reaching the council room. -SC
#I think I fixed it... somewhat?

show shizu behind_smile at center
with charaenter

# "Maybe she expects a conversation, which is why she puts down the carton of orange juice in her hand."
"คงจะคิดว่าได้คุยถึงได้วางกล่องน้ำส้มที่ถืออยู่ในมือลง"

# ssh "Good morning."
ssh "อรุณสวัสดิ์"

# his "Where's your better half?"
his "แล้วอีกครึ่งตัวเธอไปไหน?"

show shizu adjust_frown
with charachange

# ssh "We are separate individuals."
ssh "พวกเราไม่ใช่ร่างเดียวกันนะ"

# "Thinking about it, they must get that quite a bit. I can think of no other way to explain how ready she was with that answer."
"มาคิด ๆ ดูแล้ว คงจะมีคนล้ออย่างนั้นบ่อยอยู่เหมือนกัน ไม่งั้นคงไม่ตอบได้ฉับไวขนาดนี้หรอก"

show shizu basic_normal
with charachange

# ssh "You're here early. That's good, you can help me look over some handouts. They're going out later today."
ssh "มาเช้านะ ดี ช่วยดูเอกสารพวกนี้ให้หน่อย เดี๋ยววันนี้จะต้องเอาไปแจก"

# his "I came here early specifically so I could see you without having to do work."
his "ฉันตั้งใจมาเช้าเพื่อที่จะได้เจอเธอตอนที่ไม่ต้องทำงานนะ"

show shizu behind_smile
with charachange

# ssh "According to Misha, being early isn't new for you."
ssh "เห็นมิช่าบอกนายก็มาเช้าเป็นประจำนี่"

# his "It's not new for you either."
his "เธอก็มาเช้าประจำหรอก"

show shizu adjust_happy
with charachange

# ssh "Are you saying you want to race?"
ssh "อยากแข่งเหรอ"

# "Shizune adjusts her glasses nonchalantly, a gesture that belies how giddy she is inside about the thought of having something very petty to take competitively and seriously. I think the smaller the matter is, the more it excites her."
"ชิซูเนะดันแว่นสบาย ๆ เป็นท่าทางที่บ่งบอกว่าเธอตื่นเต้นเหลือเกินที่หยิบเรื่องเล็กน้อยขนาดนี้มาแข่งเอาจริงเอาจัง\nรู้สึกว่ายิ่งเรื่องเล็กเธอยิ่งตื่นเต้น"

# his "It's not a race. Do you want to make it a contest? I don't."
his "เปล่าสักหน่อย เธออยากแข่งเหรอ ฉันไม่อยาก"

# "I almost forget to add the last part, the most important part."
"เกือบลืมพูดส่วนที่สำคัญที่สุดลงท้ายแล้ว"

show shizu behind_smile
with charachange

# ssh "…Well, that's fine. There are too many days left in the school year, I'd get tired of it anyway."
ssh "…อืม เอาเถอะ ยังเหลือเวลาให้เรียนอีกตั้งหลายวัน เดี๋ยวฉันก็คงเบื่ออยู่ดี"

# "With that, Shizune picks up her juice and finishes it off. I wonder if she's going to try and shoot the empty container into the trash, but she doesn't. In fact, she seems puzzled as to why I seem so disappointed. I'd better get to the point."
"แล้วเธอก็หยิบน้ำผลไม้ขึ้นมาดูดจนหมด จะโยนกล่องทิ้งลงถังขยะหรือเปล่านะ แต่ก็ไม่โยน เธอดูงง ๆ ที่ฉันดูผิดหวัง\nเข้าเรื่องเลยดีกว่า"

# his "I just wanted to talk. Our break is practically here, you know."
his "แค่อยากคุยน่ะ เนี่ย นี่ก็จะปิดเทอมแล้ว"

# his "And we should spend more time together, anyway. I was thinking that we could do that over the summer."
his "แล้วเราก็ต้องอยู่ด้วยกันให้มากขึ้นด้วย เลยกะว่าปิดเทอมฤดูร้อนรอบนี้หาเวลามาอยู่ด้วยกันดีมั้ยนะ"

show shizu adjust_blush
with charachange

# "Shizune's face turns as red as mine must be, and she starts adjusting her glasses, flustered. What an all-purpose gesture. She taps her fingers together in thought, considering her next words carefully."
"หน้าชิซูเนะคงแดงพอ ๆ กับหน้าฉันตอนนี้ เธอดันแว่นดูลนลาน เป็นท่าทางที่สะดวกใช้จริง ๆ เธอเคาะนิ้วครุ่นคิด\nเลือกสรรคำ"

show shizu basic_normal
with charachange

# ssh "You mean like a date?"
ssh "แบบเดตอะไรอย่างนี้เหรอ"

# his "Just because we're going out somewhere, that instantly makes it a date?"
his "แค่ไปเที่ยวด้วยกันก็นับว่าเป็นเดตเลยเหรอ"

show shizu behind_blank
with charachange

# ssh "It's not?"
ssh "ก็ไม่ใช่เหรอ"

show shizu adjust_frown
with charachange

# ssh "I want it to be a date."
ssh "ฉันอยากให้เป็นเดต"

# his "Then it is one."
his "งั้นก็ได้"

show shizu basic_happy
with charachange

# "Shizune approvingly claps her hands once, before adding on to my statement:"
"ชิซูเนะตบมือพอใจ ก่อนจะเสริม"

show shizu behind_blank
with charachange

# ssh "But not today."
ssh "แต่ไม่ใช่วันนี้"

show shizu basic_normal2
with charachange

# ssh "I'm going away for a week to visit my family."
ssh "สัปดาห์นี้ฉันต้องไปเยี่ยมครอบครัว"

# "That is an oddly formal way of putting it, and for that reason, my interest is piqued. Maybe her family is the prim and proper, traditional kind, living in a giant old-timey mansion with a little stream and koi pond, where everyone wears kimonos all the time."
"ทำท่าเหมือนเป็นเรื่องทางการยังไงไม่รู้ และพอเห็นอย่างนั้นแล้วเลยรู้สึกสนใจขึ้นมา ครอบครัวเธอคงเป็นแนวคนดูดี\nมีสกุลแบบดั้งเดิม อยู่ในคฤหาสน์เก่า ๆ หลังใหญ่ที่มีน้ำไหลกับบ่อปลาคาร์ป แต่ละคนก็ใส่ชุดกิโมโนตลอด"

# "It's a wild assumption, but it's fun to speculate sometimes. I wonder if Shizune puts on the appearance of being a calm and mature good daughter like Lilly when she is with her family."
"อาจจะคิดไกลไป แต่เดาเล่น ๆ ก็เพลินดี พออยู่กับครอบครัวแล้วชิซูเนะจะวางตัวเป็นลูกสาวที่ใจเย็นและมีความ\nเป็นผู้ใหญ่อย่างลิลลี่มั้ยนะ"

# "I can't imagine it, but if there's even a possibility that it's true, then I must see it."
"นึกภาพไม่ออกเลย แต่ถ้ามีโอกาสจะเป็นอย่างนั้นจริงฉันก็ต้องไปดูให้ได้"

# his "Only a week? It must not be that far of a trip, then."
his "สัปดาห์เดียวเองเหรอ งั้นก็คงไม่ไกลมากงั้นสิ"

show shizu behind_frustrated
with charachange

# ssh "Of course not, they're still in Japan, after all."
ssh "แหงสิ ก็อยู่ในญี่ปุ่นนี่แหละ"

# his "Really…"
his "จริงเหรอ…"

show shizu adjust_happy
with charachange

# ssh "It isn't like you can come with me. Is that what you're trying to say?"
ssh "แต่ก็ใช่ว่านายจะไปด้วยได้หรอก อยากไปด้วยเหรอ"

# his "Why can't I?"
his "ทำไมไปไม่ได้"

show shizu basic_normal2
with charachange

# ssh "It isn't like you would enjoy it."
ssh "นายคงเบื่อ"

# his "You don't know that. It could be fun."
his "ใครจะไปรู้ อาจจะสนุกก็ได้"

# his "Ah, I almost forgot: you didn't answer my question. Are you going alone, or is Misha going with you? Does your family know sign?"
his "เอ้อ เกือบลืม เธอยังไม่ได้ตอบคำถามฉันเลยนะ เธอจะไปคนเดียวหรือมิช่าไปด้วย ครอบครัวเธอรู้ภาษามือมั้ย"

show shizu behind_blank
with charachange

# ssh "Misha is coming along."
ssh "มิช่าไปด้วย"

# "The part of the question left unanswered is the most telling."
"ส่วนคำถามที่ไม่ได้ตอบนั้นก็ชัดแล้วละ"

# "If Shizune's family can't communicate with her, I have to wonder what her childhood was like. She probably wrote everything on that pad she carries around and still produces out of nowhere sometimes."
"ถ้าครอบครัวชิซูเนะสื่อสารกับเธอไม่ได้ วัยเด็กเธอจะเป็นยังไงเนี่ย คงจะเขียนใส่กระดาษสมุดเล่มนั้นที่ทุกวันนี้บางที\nเธอก็เอาออกมาใช้"

# "Usually, it's when neither Misha nor I are around. I can notice her from far away when she pulls it out like a last resort, grimacing the whole time."
"ปกติก็ใช้ตอนที่มิช่าหรือฉันไม่อยู่ ฉันเหลือบเห็นไกล ๆ อยู่ตอนที่เธอทำหน้าเบ้ตอนต้องใช้เหมือนเป็นที่พึ่งสุดท้าย"

# his "If Misha is going, then I'm going to go, too."
his "ถ้ามิช่าไปงั้นฉันก็ไปด้วย"

show shizu basic_normal
with charachange

# ssh "Do you like Misha?"
ssh "นายชอบมิช่าเหรอ"

# his "It's the principle of the thing."
his "โดยหลักการแล้วฉันก็ต้องไปด้วยอยู่แล้วนี่"

# "I entertain the notion that Shizune might actually be jealous, but I doubt it. She usually wears her emotions pretty plainly on her face, and I don't see anything that would support my theory right now."
"หรือจะหึงอยู่กันนะ คิดแล้วก็สนุกดี แต่คงไม่หรอก ปกติก็ทำหน้านิ่ง ๆ ตลอด ไม่เห็นจะมีอะไรที่บอกว่าหึงเลย"

show shizu adjust_frown
with charachange

# ssh "I think you're just bored."
ssh "นายแค่เบื่อเฉย ๆ เถอะ"

show shizu behind_smile
with charachange

# ssh "That's okay, though. All right, we'll all go together. It's what I hoped for in the first place."
ssh "แต่ไม่เป็นไร ก็ได้ ไปด้วยกันสามคนนี่แหละ ยังไงฉันก็อยากให้ไปกันหมดนี่แต่แรกอยู่แล้ว"

show shizu adjust_smug
with charachange

# ssh "You can't skip out on Student Council today to pack your bags, just because you're coming with us on such short notice, it's no excuse!"
ssh "แต่จะโดดงานสภานักเรียนไปเก็บของไม่ได้นะ จะอ้างว่าเพิ่งมาบอกแบบกระชั้นชิดไม่ได้!"

# his "It's okay, I hardly have anything to pack anyway."
his "ไม่เป็นไร ๆ ใช่ว่าฉันจะมีของให้เก็บเยอะ"

show shizu basic_normal
with charachange

# "Shizune pauses, tenting her fingers thoughtfully."
"ชิซุูเนะนิ่งไปประกบนิ้วเข้าด้วยกันพลางคิด"

show shizu behind_blank
with charachange

# ssh "You must have come to this school on very short notice."
ssh "นายคงมาโรงเรียนนี้แบบไม่ทันตั้งตัวเลยสินะ"

#If seen A26b:

label th_S17a:

# "It could be that she is thinking back to the time when she and Misha unexpectedly shoved themselves into my room and caught a glimpse of all my medicines. That was an awkward moment I'd like to forget, and I don't like revisiting it."
"คงจะนึกถึงตอนที่เธอกับมิช่าเข้ามาบุกห้องฉันแล้วเห็นยาที่เรียงราย กระอักกระอ่วนเสียจนอยากลืม ไม่อยากนึกถึง\nเท่าไหร่เลยแฮะ"

# "The way she tiptoes around the issue even now only makes me more uncomfortable."
"ยิ่งเธอทำทีอ้อมไปอ้อมมาไม่เลิกอย่างนี้แล้วฉันก็ยิ่งอึดอัด"

#End conditionals
label th_S17x:

# his "I did. It was kind of an on-the-spot decision. It worked out better than I expected, though."
his "อืม ค่อนข้างปุบปับเหมือนกัน แต่สุดท้ายก็ดีกว่าที่คิดละนะ"

# "I hope Shizune won't pursue the matter, and to my relief, she doesn't."
"หวังว่าจะไม่ซักไซ้อะไรอีกนะ แล้วฉันก็โล่งที่เธอไม่อะไรต่อ"

show shizu adjust_happy
with charachange

# ssh "My home is in a particularly beautiful part of Saitama."
ssh "บ้านฉันอยู่ไซตามะ แถวนั้นวิวดีมากเลย"

show shizu behind_smile
with charachange

# ssh "We'll be leaving early in the morning, so be ready. Let's talk about it more later, okay? For now, those handouts won't look over themselves, and you're going to help me."
ssh "เดี๋ยวต้องออกตัวกันแต่เช้า เตรียมตัวให้พร้อมด้วย ไว้ค่อยคุยเรื่องนี้อีกที ตอนนี้มาช่วยฉันดูเอกสารที่ต้องเอาไปแจก\nพวกนี้ก่อน"

stop music fadeout 3.0

hide shizu
with charaexit

# "As Shizune dives into her work, pulling me along with her, I think that she seems almost, but not quite, excited to go."
"ชิซูเนะทำงานต่อพลางลากฉันให้มาช่วยอีกแรง ดูเหมือนเธอก็ตื่นเต้นอยากไปเหมือนกัน"

scene black
with dissolve

#*****************************************************************************************************

label th_S18:

scene bg school_dormhallway
with locationchange

play music music_daily fadein 0.5

# "When Shizune and Misha arrive early the next morning to pick me up, they are dressed in something other than the school uniform I've grown used to seeing them in."
"ชิซูเนะและมิช่ามารับฉันแต่เช้า ทั้งสองคนไม่ได้ใส่ชุดนักเรียนอย่างที่ฉันเคยเห็นจนชินตา"

show shizu behind_blank_cas at center
with charaenter

# "It makes sense, since we're on holiday, but it's still jarring. Shizune's dress is sharp and fashionable, almost too much for a quiet place like Yamaku. Thinking back to what she wore at the Tanabata festival, I'm starting to notice a trend with her."
"ก็ถูกแล้วแหละ ปิดเทอมแล้วนี่นะ แต่ก็รู้สึกแปลกหน่อย ๆ ชิซูเนะแต่งตัวเนี้ยบมีสไตล์จนออกจะเด่นไปหน่อยกับโรงเรียน\nยามากุที่เงียบ ๆ แบบนี้ พอนึกถึงชุดที่เธอใส่วันทานาบาตะก็พอจะนึกภาพออกแล้วว่าเธอเป็นคนแต่งตัวยังไง"

# "All of her clothes are very tasteful and mature; very well thought out. So, then, I wonder why she herself is so immature."
"ทุกชุดที่เธอใส่นั้นถูกจัดมาอย่างดี ทั้งมีรสนิยมและมีความเป็นผู้ใหญ่ แล้วไหงตัวเธอถึงทำตัวเป็นเด็กอย่างนี้เนี่ย"

show bg school_dormhallway at bgright
show shizu behind_blank_cas at tworight
with charamove

show misha perky_smile_cas at twoleft
with charaenter

# "Well, at least Misha's clothes reflect her inner self on the outside."
"แต่อย่างน้อยชุดมิช่าก็สะท้อนตัวตนเธอดีแหละนะ"

show shizu adjust_frown_cas
with charachange

# ssh "You're bringing so little."
ssh "เอาของมาน้อยจัง"

# hi "I said I would. I said there wasn't much to pack."
hi "ก็บอกแล้วนี่ว่าฉันมีของไม่เยอะ"

show shizu basic_frown_cas
with charachange

# "Shizune pouts and rocks her own, rather large collection of luggage with her foot as if embarrassed. Misha only has one suitcase with her, but it's almost larger than she is. She looks self-conscious about it as well."
"ชิซูเนะทำแก้มป่องแล้วใช้เท้าโยกกองสัมภาระที่ค่อนข้างใหญ่นั้นไปมาดูอาย ๆ มิช่าเอากระเป๋าเดินทางมาใบเดียว\nแต่ขนาดกระเป๋านั้นใหญ่พอ ๆ กับตัวเธอ ดูจะรู้ตัวอยู่เหมือนกันว่ากระเป๋าตัวเองใบใหญ่แค่ไหน"

# "God, that suitcase is as big as a compact car. The pea green color is unsettling, too. It's like something used to transport bodies. The way they look right now makes me want to tease them a little."
"ใหญ่พอ ๆ กับรถเก๋งเลยมั้ง สีก็เป็นสีเขียวอย่างกับถั่วจนชวนขนลุก เหมือนกระเป๋าที่เอาไว้ขนร่างคนเลย เห็นสภาพ\nแล้วก็อดหยอกไม่ได้"

# hi "Aw, that's bad luck for you and Misha, isn't it? Having to carry those huge bags. Gotta pack light next time, like me. Everything fits into one little suitcase."
hi "โธ่ ลำบากน่าดูเลยนะทั้งสองคน ขนกระเป๋ามาขนาดนั้น คราวหน้าเอาของมาน้อย ๆ หน่อยแล้วกัน แบบฉันเนี่ย\nกระเป๋าเล็ก ๆ ใบเดียวก็พอแล้ว"

show misha hips_grin_cas
with charachange

# mi "Like James Bond~!"
mi "เหมือนเจมส์บอนด์~!"

# hi "Yes, exactly like James Bond."
hi "ใช่ เหมือนเจมส์บอนด์"

show shizu adjust_frown_cas
with charachange

shi "…"

# "Shizune gently tugs at her glasses in concentration."
"ชิซูเนะดันแว่นจดจ่อ"

show shizu basic_normal_cas
with charachange

# ssh "We should split the amount we carry equally."
ssh "มาแบ่งกันขนของดีกว่า"

show misha sign_smile_cas
with charachange

# mi "Wow~! That's a great idea, Shicchan~!"
mi "โห~! ความคิดดีนี่ชิจัง~!"

# hi "What? No."
hi "ฮะ? ไม่"

show shizu adjust_smug_cas
with charachange

# ssh "It would benefit us all."
ssh "ก็ได้ประโยชน์กันทุกคน"

show misha cross_laugh_cas
with charachange

# mi "Yup~! Wahaha~!"
mi "ช่าย~! วะฮ่าฮ่า~!"

# hi "I'm going to have to say no."
hi "ฉันต้องขอปฏิเสธ"

show shizu cross_angry_cas
with charachange

# ssh "You're outvoted!"
ssh "นายเป็นเสียงข้างน้อยนะ!"

# "She almost lunges forth as she signs it. Terrifying."
"ที่ทำภาษามือเมื่อกี้นี่แทบจะพุ่งเข้าใส่แล้ว น่ากลัว"

# hi "Ah, well. I was just kidding. I don't mind carrying a few extra. I just thought it would be fun to mess with you both."
hi "เอ่อ เอาเหอะ หยอก ๆ ถือเพิ่มอีกนิดหน่อยฉันไม่อะไรหรอก แค่กะว่าหยอกเธอสองคนคงสนุกดี"

# hi "But, if you were going to try and make me carry it all, I was going to ride that giant green case down the mountain like a sled."
hi "แต่ถ้าจะให้ขนไปคนเดียวหมดนี่ฉันจะนั่งกระเป๋าสีเขียวใบใหญ่นั่นเป็นเลื่อนไหลลงเขาเลยนะ"

show shizu adjust_smug_cas
with charachange

shi "…"

# "That seems to make Shizune laugh, and she holds a hand up to her mouth to hold it back. It's like she is hiding it. I wonder if she can laugh. If not, that might be why she does that. That kind of makes me feel sad."
"ชิซูเนะดูจะขำพร้อมยกมือป้องปากกลั้นขำเหมือนซ่อนเอาไว้ เธอจะหัวเราะได้มั้ยนะ หรือที่ทำแบบนั้นก็เพราะหัวเราะ\nไม่ได้นั่นแหละ คิดตามแล้วก็หดหู่ยังไงไม่รู้"

stop music fadeout 3.0

scene bg city_station
with locationskip

# "With that taken care of, we head for the train station, and a very uneventful ride follows. Shizune and Misha manage to fall asleep almost instantly, but I find myself unable to. That's never happened before. Maybe it's my medication."
"พอจบเรื่องแล้วเราก็มายังสถานีรถไฟ จากนั้นก็นั่งรถไฟมาเรื่อย ๆ ตอนขึ้นรถไฟมาชิซูเนะกับมิช่าก็ผล็อยหลับ\nแทบจะทันที แต่ฉันหลับไม่ลง ปกติก็หลับได้แท้ ๆ น่าจะเพราะยามั้ง"

scene bg shizu_houseext
with shorttimeskip

play music music_soothing fadein 0.5

# "When we arrive at Shizune's house, it's quite a bit larger than I'd envisioned it would be. I don't think huge would be much of an overstatement."
"พอได้มาเห็นบ้านชิซูเนะแล้วก็รู้สึกว่าใหญ่กว่าที่คิดเอาไว้หน่อย ใช้คำว่ามโหฬารก็น่าจะไม่เกินจริงนัก"

# hi "You live in a mansion?"
hi "นี่เธออยู่คฤหาสน์เหรอ"

show shizu cross_angry_cas at center
with charaenter

# "Shizune indignantly stands up on her tiptoes so that we're at eye level, and frowns deeply, having had my comment translated to her by Misha. It's as if she's saying, “how can you even suggest such a thing?”"
"พอได้ฟังคำพูดฉันผ่านมิช่าแล้วชิซูเนะก็เขย่งเท้าให้ระดับสายตาเท่ากันแล้วขมวดคิ้วมองหน้าฉันอย่างไม่พอใจราวกับ\nจะบอกว่า “พูดอะไรอย่างนั้นออกมาได้ยังไง”"

show shizu basic_frown_cas
with charachange

# ssh "This is just a normal house. Nothing as ostentatious as a mansion."
ssh "ก็แค่บ้านธรรมดานั่นแหละ ไม่ได้หรูหราถึงขั้นคฤหาสน์หรอก"

# "I believe our definitions of those terms are quite different, then."
"งั้นนิยามของเราสองคนก็คงไม่เหมือนกันละมั้ง"

show bg shizu_houseext at bgright
show shizu basic_frown_cas at tworight
with charamove

show misha hips_grin_cas at twoleft
with charaenter

# mi "Wahaha~. Hicchan, are you surprised? Do you want me to point out where you'll be staying?"
mi "วะฮ่าฮ่า~ ฮิจัง ตกใจเหรอ อยากให้พาไปดูมั้ยว่านายจะได้นอนที่ไหน"

show shizu behind_blank_cas
with charachange

# ssh "I think we have a guest room, but I'm not sure if we have two. I'll check."
ssh "เหมือนจะมีห้องนอนสำหรับแขกอยู่นะ แต่ไม่แน่ใจว่ามีสองห้องหรือเปล่า เดี๋ยวไปดู"

show misha sign_smile_cas
with charachange

# mi "Hm~, it's no problem, though, Hicchan~! Shicchan and I can share a room if we have to. Well~, unless hers is being used for something else now."
mi "อืม~ แต่ไม่เป็นไรหรอกนะฮิจัง~! ถ้าจำเป็นจริง ๆ ฉันนอนกับชิจังได้ ก็~ เว้นเสียแต่ว่าห้องนั้นจะไม่ว่างเพราะเอาไป\nทำอะไรอย่างอื่น"

hide shizu
with charaexit

hide misha
with charaexit

stop music fadeout 5.0

# "“Not sure?” I'm starting to think Shizune doesn't spend a lot of time at home. Before I can make a joke of it at her expense, Shizune vanishes into the house, and Misha goes with her, leaving me alone on the grounds."
"“ไม่แน่ใจ”? หรือชิซูเนะจะไม่ค่อยได้อยู่บ้านกันนะ แต่ก่อนที่ฉันจะทันได้หยอกล้ออะไร ชิซูเนะก็หายแวบเข้าไปในบ้าน\nพร้อมมิช่าที่ตามไปติด ๆ ทิ้งให้ฉันยืนอยู่คนเดียว"

# "I don't want to follow them inside just yet. I put my bag down by the front door, and take the opportunity to look around the grounds, just making a quick lap around the house."
"ฉันวางกระเป๋าไว้ที่ประตูหน้าบ้านเพราะยังไม่อยากตามเข้าไปพลางถือโอกาสนี้เดินดูรอบ ๆ บ้าน"

show hideaki bored at center
with shorttimeskip

# "Even though it takes just a few minutes, when I get back the first thing I notice is that my bag is gone, and a tiny girl is in its place. She looks a lot like Shizune, although Shizune wouldn't wear red shorts and star-and-moon stockings."
"ทั้งที่ไปไม่กี่นาที แต่กลับมากระเป๋าฉันก็ไม่อยู่แล้ว และมีผู้หญิงตัวเล็ก ๆ ที่ดูเหมือนชิซูเนะมาก ๆ คนหนึ่งมาแทนที่\nถึงชิซูเนะจะไม่ใส่กางเกงสีแดงกับถุงน่องลายดาวกับพระจันทร์แบบนั้นน่ะนะ"

# hi "Hi! Are you Shizune's little sister or something?"
hi "ไง! เธอเป็นน้องสาวชิซูเนะเหรอ"

show hideaki normal
with charachange

# hh "No. I'm her little brother. My name is Hideaki."
hh "เปล่าครับ ผมเป็นน้องชาย ชื่อฮิเดอากิ"

show hideaki thinking
with charachange

# hh "It's nice to meet you."
hh "ยินดีที่ได้รู้จักครับ"

play music music_happiness fadein 2.0

# "The voice that responds is straightforward, monotone, and also definitely male. I feel embarrassed to the point where I could almost turn around and leave right now, if I could remember my way back to the train."
"เสียงที่ตอบกลับมานั้นทื่อ ๆ และเรียบนิ่งที่ฟังดูแล้วยังไงก็เป็นผู้ชายแน่นอน อายจนแทบอยากเดินออกบ้านกลับไป\nเสียตอนนี้ ติดก็แต่จำทางไปสถานีรถไฟไม่ได้"

show hideaki serious
with charachange

# hh "Are you the second person that my sister brought with her?"
hh "พี่เป็นคนที่สองที่พี่ชิซูเนะขนมาด้วยหรือเปล่าครับ"

# hi "“Brought with her?” I'm not luggage."
hi "“ขนมาด้วย”? ฉันไม่ใช่กระเป๋านะ"

# hi "Anyway, I'm Hisao. Did you take my bag?"
hi "แต่เอาเถอะ ฉันชื่อฮิซาโอะ แล้วนี่นายเก็บกระเป๋าฉันไปเหรอ"

show hideaki triangle
with charachange

# hh "Yes, it is my right to keep anything I find on my property."
hh "ครับ ผมเจออะไรก็ย่อมเป็นสิทธิ์ของผมที่จะเก็บ"

# hi "No, it's not. That's not how it works at all."
hi "ไม่ ไม่ได้สิ ใช่อย่างนั้นที่ไหนเล่า"

# "I guess even particularly well-spoken little kids believe in the law of finders keepers. Even though I call him little, he doesn't seem that much younger, now that I think about it. Maybe two or three years younger, at most."
"แม้แต่เด็กที่พูดจาฉะฉานอย่างนี้ก็ยังเชื่อเรื่องใครเจอใครได้เหรอ ถึงตอนแรกฉันจะบอกว่าเป็นน้อง แต่พอดูแล้ว\nอายุก็ไม่น่าห่างกันเท่าไหร่ อย่างมากก็คงสักสองสามปี"

show hideaki normal
with charachange

# hh "I gave it to Shizune. It's inside. Are you on the Student Council?"
hh "ผมเอาไปฝากพี่ชิซูเนะไว้ในบ้านแล้ว พี่เป็นสภานักเรียนด้วยเหรอครับ"

# hi "Yeah, how did you know? Does she bring it up often?"
hi "อื้ม รู้ได้ไงเนี่ย พี่นายเล่าให้ฟังบ่อยเหรอ"

# "I almost said “does she talk about it often?” That could have been bad."
"เกือบหลุดปากไปว่า “พูดถึงบ่อยเหรอ” แล้ว ซึ่งน่าจะไม่ดีแน่"

show hideaki bored
with charachange

# hh "Yes, all the time. Do you get along with her?"
hh "ครับ ตลอดเลย สนิทกันดีเหรอครับ"

# hi "Get along? That's a weird question. I wouldn't be on the Student Council if I couldn't get along with her. What about you, do you two get along well?"
hi "สนิทกันดีมั้ยเหรอ ถามอะไรแปลก ๆ ไม่สนิทคงไม่มาเข้าสภานักเรียนหรอก แล้วนายล่ะ สนิทกับพี่นายดีมั้ย"

# "Even though he has a monotone voice, his face is as expressive as Shizune's, and belies how he really feels. It must run in the family. Looks like he isn't happy about my question, for whatever reason."
"ถึงเสียงจะเรียบ แต่สีหน้าก็บอกอะไรหลายอย่างได้เหมือนชิซูเนะ ซึ่งทำให้รู้ว่าเสียงนั้นขัดกับความรู้สึกจริง ๆ สงสัย\nเป็นกันทั้งบ้าน และเหมือนเขาจะไม่ปลื้มกับคำถามนั้นสักเท่าไหร่"

show hideaki thinking
with charachange

# hh "I'm sorry. I was only asking because you both act so much alike."
hh "ขอโทษครับ ผมแค่ถามเพราะเห็นพี่ทำตัวคล้ายพี่ชิซูเนะมากเลย"

# "I don't know why, but it feels like he's teasing me. Unfortunately, it works. I don't like being compared to Shizune."
"ไม่รู้ทำไม แต่รู้สึกเหมือนล้อกันอยู่ ซึ่งก็ได้ผล ฉันไม่ชอบให้ใครมาเปรียบเทียบฉันกับชิซูเนะ"

# hi "You're a lot more like Shizune, but that's to be expected. I mistook you for her little sister, even. If you don't want people to make that mistake, you should dress more appropriately."
hi "นายน่ะเหมือนพี่นายมากกว่านะ แต่ก็ไม่แปลกหรอกมั้ง นึกว่าเป็นน้องสาวด้วยซ้ำเนี่ย คราวหลังถ้าไม่อยากให้ใคร\nเข้าใจผิดก็แต่งตัวดี ๆ หน่อยนะ"

show hideaki confused
with charachange

# hh "I don't understand, my clothes are perfectly seasonal."
hh "ไม่เห็นเข้าใจเลย เสื้อผ้าผมก็เข้ากับสภาพอากาศดีออก"

# hi "What's with the stockings?"
hi "แล้งถุงน่องนั่นคือ?"

show hideaki angry_up
with charachange

# hh "They are cool."
hh "เท่ออก"

show hideaki disapproves
with charachange

# hh "You act like my sister. Eventually people will start mistaking you for her."
hh "พี่ทำตัวเหมือนพี่ชิซูเนะเลยนะครับ เดี๋ยวคนเข้าใจผิดว่าพี่เป็นพี่ชิซูเนะแน่"

# "I guess my comment hit him harder than I thought. That would explain this attempt at turning it around."
"สงสัยจะจี้ใจดำได้แรงกว่าที่คิดถึงได้รีบเปลี่ยนเรื่องอย่างนี้"

# hi "I hate being compared to other people."
hi "ฉันไม่ชอบให้ใครมาเปรียบเทียบฉันกับคนอื่น"

show hideaki evil
with charachange

# hh "Shizune doesn't like it when she is compared to others either."
hh "พี่ชิซูเนะก็ไม่ชอบให้ใครเอาตัวเองไปเปรียบเทียบกับคนอื่นเหมือนกัน"

# "I'd thought that Hideaki was a little more mature than Shizune, but they have the same competitive streak and inclination to provoke people. I wonder if he's like this because of Shizune, or if it's the other way around."
"ก็นึกว่านิสัยจะโตกว่าชิซูเนะ ที่ไหนได้ ดันชอบหาเรื่องแข่งกับยั่วโมโหคนเก่งพอกัน นี่ใครติดนิสัยใครมากันแน่เนี่ย"

# hi "And neither do you, right? Okay, I get it. I shouldn't be so petty."
hi "นายก็คงไม่ชอบเหมือนกันใช่มั้ยล่ะ โอเค เข้าใจละ ฉันไม่น่ามาคิดเล็กคิดน้อยเลย"

show hideaki normal
with charachange

stop music fadeout 4.0

# "Especially to little kids. Hideaki seems to accept this as an acknowledgment of defeat, which is something that I feel like I can't let go. Nevertheless, I'll just have to let it go while I have the chance."
"โดยเฉพาะกับเด็กเล็ก ฮิเดอากิดูจะยอมแพ้จนฉันอยากจะหาเรื่องอะไรต่อสักหน่อย แต่เอาเถอะ มีโอกาสได้จบ\nก็รีบ ๆ จบไป"

scene bg shizu_living
with locationchange

# "I can hear Misha's laughter bouncing through the halls the moment I step through the door to the house, and follow it into what I would guess is the living room. It holds more people than I'd expected."
"พอเดินผ่านประตูบ้านเข้ามาก็ได้ยินเสียงหัวเราะมิช่าที่ดังก้องไปทั่วโถง ฉันเดินตามเสียงนั้นไปยังห้องที่น่าจะเป็น\nห้องนั่งเล่น แต่คนเยอะกว่าที่คิดแฮะ"

show lilly basic_displeased_cas:
    center
    ypos 1.17 xpos 0.55
show akira basic_boo:
    tworight
    ypos 1.15 xpos 0.72
show hideaki bored:
    center
    xpos 0.92
    easein 1.0 ypos 1.1
show shizu behind_blank_cas:
    twoleft
    ypos 1.11 xpos 0.27
show misha perky_smile_cas:
    center
    ypos 1.1 xpos 0.08
with charaenter

play music music_another fadein 4.0

# "Among them I spot a distinctive and familiar blonde ponytail. I'm more confused by why Lilly is here than surprised. Shizune seems just as surprised. Lilly doesn't look ecstatic about this chance meeting either."
"ในนั้นมีผมหางม้าสีบลอนด์ที่เด่นและคุ้นตาอยู่ ฉันงงก่อนที่จะทันได้แปลกใจว่าทำไมลิลลี่ถึงมาอยู่ที่นี่ ชิซูเนะก็ดู\nแปลกใจพอกัน ลิลลี่เองก็ดูจะไม่ยินดีเท่าไหร่นักที่เรื่องบังเอิญเป็นอย่างนี้"

# "Sitting next to Lilly is a tall, androgynous looking woman in a sharp suit. I'd like to assume that it's her older sister, but I don't want to risk it."
"ข้าง ๆ ลิลลี่มีผู้หญิงที่ดูเหมือนทั้งชายทั้งหญิงใส่ชุดสูทอย่างเนี้ยบคนหนึ่งนั่งอยู่ คงจะเป็นพี่สาวของลิลลี่ละมั้ง\nแต่ก็อาจจะไม่ใช่ก็ได้"

show lilly basic_listen_cas
with charachange

# li "I didn't expect that you would arrive so early."
li "มาถึงเร็วผิดคาดเลยนะ"

# "At first I think she's talking to me, but it turns out that she's referring to Shizune. I don't think Lilly even notices my presence. I've clearly walked in on them mid-conversation, and it looks like with her focus on Shizune, she couldn't hear me."
"ตอนแรกก็นึกว่าคุยกับฉัน แต่ที่จริงแล้วเธอคุยกับชิซูเนะอยู่ ลิลลี่น่าจะยังไม่รู้ด้วยซ้ำว่าฉันอยู่ด้วย ฉันคงเข้ามาจังหวะ\nที่กำลังคุยกันพอดี แถมดูจะจดจ่ออยู่กับชิซูเนะด้วย น่าจะไม่ได้ยินที่ฉันมา"

show shizu basic_frown_cas
with charachange

# ssh "I should have rearranged my entire schedule for you."
ssh "รู้ว่าเธอจะมาอย่างนี้ฉันเปลี่ยนแผนใหม่หมดเลยคงดี"

show misha sign_smile_cas
with charachange

# mi "Shicchan says: I should have rearranged my schedule just for you~!"
mi "ชิจังบอกว่า รู้ว่าเธอจะมาอย่างนี้ฉันเปลี่ยนแผนใหม่หมดเลยคงดี~!"

show lilly basic_displeased_cas
with charachange

# li "That would have been nice, but I would not expect you to do such a thing."
li "ก็คงดีแหละจ้ะ แต่ฉันคิดว่าเธอคงไม่ใช่คนที่จะเปลี่ยนแผนหรอก"

show misha hips_smile_cas
with charachange

# mi "Oh, hi, Hicchan~! You're finally here."
mi "โอ๊ะ ไง ฮิจัง~! มาจนได้นะ"

# hi "Yeah. Hello, Lilly."
hi "อื้ม สวัสดี ลิลลี่"

show lilly basic_surprised_cas
with charachange

# li "Oh, Hisao? This is quite a surprise. Akira, this is Hisao, a schoolmate. Hisao, this is Akira, my sister."
li "อ้าว ฮิซาโอะเหรอ ไม่คิดว่าจะมาด้วยนะจ๊ะเนี่ย พี่ นี่ฮิซาโอะ เพื่อนร่วมโรงเรียนหนู ฮิซาโอะ นี่อากิระ พี่สาวฉัน"

show akira basic_smile
with charachange

# aki "Yo."
aki "ไง"

# "She holds up her hand in a brief and quite casual gesture of greeting. So she is the older sister after all."
"เธอโบกมือทักทายเร็ว ๆ อย่างเป็นกันเอง เป็นพี่สาวของลิลลี่จริง ๆ ด้วย"

show akira basic_boo
show lilly basic_weaksmile_cas
with charachange

# aki "I hope we're not messing up any of your plans. Since we're only going to be here for one more day, Lilly and I thought she may as well come with me."
aki "หวังว่าไม่ได้มาทำแผนอะไรพังนะ เดี๋ยวจะอยู่ที่นี่อีกแค่วันเดียวแหละ ฉันกับลิลลี่ก็คิดว่ามาด้วยกันไปเลยคงไม่เสียหาย\nอะไร"

# "Akira turns to me, like she feels compelled to explain. I'm grateful for that."
"อากิระหันมาทางฉันเหมือนอยากอธิบาย ซึ่งฉันก็ยินดีที่อุตส่าห์เล่า"

show akira basic_ending
with charachange

# aki "I suppose my position here would be best described as a babysitter."
aki "หน้าที่ฉันตอนนี้ ถ้าจะให้ว่าแล้วก็คงเป็นพี่เลี้ยงเด็กละมั้ง"

show hideaki disapproves
with charachange

# "Akira ruffles Hideaki's hair as he carries on with his pastime of looking displeased."
"อากิระยี ๆ ผมฮิเดอากิตอนเขากำลังทำหน้าบูดอย่างที่ชอบทำบ่อย ๆ ยามว่าง"

# hh "That is demeaning."
hh "หยามกันอยู่นะครับ"

show akira basic_smile
with charachange

# aki "Really? Maybe I'll change my title once you get a few more years on you. Or at least a few centimeters."
aki "เหรอ งั้นเดี๋ยวไว้นายโตขึ้นฉันค่อยเปลี่ยนตำแหน่งแล้วกัน หรืออย่างน้อย ๆ ก็ไว้นายสูงขึ้นอีกสักสองสามเซนฯ"

# "They make an interesting pair, although Akira looks more like a lawyer than a babysitter. I'm still not really sure why both she and Lilly are here, though."
"เป็นคู่ที่น่าสนใจดี แต่อากิระดู ๆ แล้วก็เหมือนทนายมากกว่าพี่เลี้ยงเด็กอีก แต่ฉันก็ยังไม่ค่อยแน่ใจเท่าไหร่ว่าทำไม\nทั้งสองคนถึงมาอยู่ที่นี่ได้"

# "Taking a glance around the room, there are tennis rackets, golf clubs, and even a stack of fishing poles and tackle boxes secreted here and there."
"เมื่อมองไปรอบ ๆ ห้องก็เห็นทั้งไม้เทนนิสไม้กอล์ฟ แถมมีเบ็ดตกปลากับกล่องอุปกรณ์ทั้งหลายแหล่อีกต่างหาก"

# "Behind every chair, in every corner, and under every table there is some piece of outdoor hobbyist equipment. I pick up one of the fishing rods and play with it."
"ที่พนักเก้าอี้ทุกตัว ที่หลืบบ้านทุกมุม ที่ใต้โต๊ะทุกตัว ทุกที่จะมีอุปกรณ์ที่เป็นกิจกรรมกลางแจ้งทั้งหมด ฉันคว้า\nคันเบ็ดมาคันหนึ่งแล้วจับ ๆ เล่น"

# hi "This is a nice house."
hi "บ้านสวยดีนะ"

# hi "Shizune, it looks like your dad has a lot of hobbies."
hi "ชิซูเนะ พ่อเธอทำกิจกรรมหลายอย่างน่าดูเลยนะ"

show misha sign_smile_cas
with charachange

show misha perky_smile_cas
with charachange

# "For a moment I forget to sign what I say, but Misha's already in the process of interpreting what I said for her. I'm still a little impressed at how automatic interpreting is for Misha."
"ฉันลืมไปแวบหนึ่งว่าต้องทำภาษามือ แต่มิช่าก็แปลที่ฉันพูดไปแล้ว ฉันยังทึ่งอยู่หน่อย ๆ ที่มิช่าแปลได้อย่างอัตโนมัติ\nขนาดนั้น"

show hideaki normal
with charachange

# hh "Do you fish?"
hh "พี่ตกปลาด้วยเหรอครับ"

# hi "No, I don't know how. I kind of want to learn, as I heard it's relaxing."
hi "เปล่าหรอก ฉันตกไม่เป็น แต่ก็อยากหัดอยู่นะ เห็นว่าผ่อนคลายดี"

show shizu behind_blank_cas
with charachange

# ssh "There is a river only a short drive away, my whole family knows how to fish. If you want, we could go there sometime."
ssh "แถวนี้มีแม่น้ำอยู่ด้วยนะ นั่งรถไปแป๊บเดียวก็ถึง ทั้งบ้านฉันตกปลาเป็นกันหมด ถ้านายอยากไปไว้จะพาไปด้วยกัน"

show akira basic_laugh
with charachange

# aki "You and Hideaki can fish? I didn't expect people your age to know, considering it's always seemed like a hobby for old men."
aki "เธอกับฮิเดอากิตกปลาเป็นด้วยเหรอ ไม่คิดว่าคนรุ่นพวกเธอจะตกกันเป็น เห็นเหมือนเป็นอะไรที่คนแก่เขาทำกัน"

show akira basic_ending
with charachange

# aki "Y'know, Lilly is great at cooking. If we had some fresh fish…"
aki "เอ้อเนี่ย ลิลลี่เขาทำอาหารเก่งนะ ถ้าได้ปลาสด ๆ มาสักตัวสองตัว…"

# "It's not hard to follow Akira's train of thought."
"เห็นได้ไม่ยากว่าอากิระคิดอะไรอยู่"

show lilly basic_displeased_cas
with charachange

# li "If you want to eat fish, we could go to the store."
li "ถ้าพี่อยากกินปลาเดี๋ยวไปซื้อที่ร้านก็ได้"

# "Lilly's voice sounds slightly more authoritative than usual. She really doesn't seem to share her sister's enthusiasm for the idea."
"น้ำเสียงลิลลี่ฟังดูเคร่งกว่าปกติเล็กน้อย ดูท่าจะไม่เอาด้วยกับความคิดของพี่สาวเธอสักเท่าไหร่"

show shizu basic_happy_cas
with charachange

shi "…"

show misha hips_grin_cas
with charachange

# mi "It's more fun to go fishing; we could even make it like a game and try to see who catches the biggest one~! That would be exciting, right? Yeah~! Hicchan, what do you think? It sounds fun, doesn't it?"
mi "ไปตกปลาสนุกกว่านะ แถมตกแข่งกันได้ด้วยว่าใครจะตกได้ปลาตัวใหญ่กว่ากัน~! ตื่นเต้นน่าดูเลยใช่มั้ยล่ะ ใช่~!\nฮิจังว่าไง ฟังดูสนุกไปเลยใช่มั้ย"

# hi "Yeah, it definitely could be."
hi "อื้ม ต้องสนุกแน่"

show akira basic_smile
with charachange

# aki "Sounds like a plan. I don't know how to fish either, so now's as good a time as any to learn."
aki "งั้นก็ตามนั้นนะ ฉันก็ตกไม่เป็นเหมือนกัน หัดตกตอนนี้เลยนี่แหละดี"

show akira basic_boo
with charachange

# "Her eyes shift towards Lilly, who remains unmoved. This sours Akira's smile a bit, and makes me wonder why Lilly's being so obstinate about this."
"อากิระเหลือบมองลิลลี่ที่ยังนิ่งอยู่จนรอยยิ้มของเธอหดหายไปเล็กน้อย ทำไมลิลลี่ถึงได้ไม่อยากไปขนาดนั้นกันนะ"

show hideaki normal
with charachange

# hh "I don't think we have enough fishing equipment for everyone."
hh "คันเบ็ดไม่น่ามีพอนะครับ"

show shizu behind_smile_cas
with charachange

# ssh "We can take turns. It'll be a team battle."
ssh "ผลัดกันตกก็ได้ แข่งแบบทีมไง"

show hideaki confused
with charachange

# hh "What is she saying?"
hh "พี่ชิซูเนะว่ายังไงนะครับ"

# hi "We can take turns. She also wants to make it a contest."
hi "ผลัดกันตกก็ได้ บอกว่าอยากแข่งกันด้วยน่ะ"

show akira basic_laugh
with charachange

# aki "Come on Lilly, we may as well make the most of it."
aki "มาสิลิลลี่ ไหน ๆ ก็ไหน ๆ แล้ว"

show akira basic_boo
with charachange

# aki "So is this going to be a competition to see who can catch the biggest fish, or the most?"
aki "แล้วนี่จะแข่งขนาดปลาหรือจำนวนปลา"

show shizu adjust_smug_cas
with charachange

# ssh "It looks like the older sister understands better, as always."
ssh "คนพี่นี่หัวไวกว่าเหมือนเดิมเลย"

show shizu basic_normal_cas
with charachange

shi "…"

show misha sign_smile_cas
with charachange

# mi "Shicchan says that she supposes Lilly would prefer to go to the store, right~? It's much less work, so it's natural that she would! Going fishing would be more fun, though, and save money. Akira, you have the right idea~!"
mi "ชิจังบอกว่า ลิลลี่คงจะอยากไปที่ร้านมากกว่าใช่มั้ย~ ที่อยากไปเพราะไม่ต้องวุ่นวายอะไรมาก! แต่ไปตกปลาสนุกกว่านะ\nแถมประหยัดด้วย อากิระคิดถูกแล้วละ~!"

show akira basic_smile
with charachange

# "Akira gives a gracious, if slightly stilted, smile. Shizune's praise wasn't her goal, after all."
"อากิระยิ้มขอบคุณแบบแกน ๆ เพราะยังไงก็ไม่ได้หวังให้ชิซูเนะชมนี่นะ"

show lilly basic_sleepy_cas
with charachange

li "…"

show lilly basic_weaksmile_cas
with charachange

# li "Isn't the river quite far away?"
li "แต่แม่น้ำอยู่ค่อนข้างไกลเลยนี่จ๊ะ"

show akira basic_ending
with charachange

# aki "I don't think it's that far, and I can drive if we have to. I'm okay with it, as long as you catch something."
aki "ไม่น่าไกลขนาดนั้นนะ ฉันขับรถไปส่งให้ก็ได้ สบายมาก ขอแค่ตกให้ได้เถอะ"

# hi "Can your car fit this many people, and a whole lot of fishing gear on top of that?"
hi "แล้วรถพี่ยัดคนเยอะขนาดนี้ไหวเหรอครับ ไหนจะอุปกรณ์ตกปลาอีก"

show akira basic_boo
with charachange

# "She purses her lips as her fingers subtly move, counting up the amount of passengers and the required cargo. If we're going to be taking me, Shizune, Misha, Lilly, Akira, and Hideaki…"
"เธอเม้มปากแล้วขยับนิ้วนับจำนวนคนและของที่ต้องขนไป ถ้าจะไปก็จะมีฉัน ชิซูเนะ มิช่า ลิลลี่ อากิระ แล้วก็ฮิเดอากิ…"

show akira basic_lost
with charachange

# aki "Six people. Damn, my car can only take five."
aki "หกคน ให้ตาย รถฉันนั่งได้ห้าคนเอง"

show akira basic_ending
with charachange

# aki "Actually, if Hideaki sat on my lap, we could—"
aki "อันที่จริง ถ้าฮิเดอากินั่งตักฉัน เราก็—"

show hideaki angry_up
with charachange

# hh "I'm not sitting on your lap."
hh "ผมไม่นั่งตักพี่"

show akira basic_resigned
with charachange

# aki "Aw."
aki "โธ่"

show shizu adjust_happy_cas
with charachange

shi "…"

show misha hips_smile_cas
with charachange

# mi "Shicchan says that her father's car would be big enough."
mi "ชิจังบอกว่ารถพ่อน่าจะใหญ่พอ"

show akira basic_lost
with charachange

# aki "What, the Fuga? If he doesn't mind us using it, then I guess we have no other choice. Feels kinda bad forsaking my car, considering I won't have it for much longer."
aki "หืม ไอ้นิสสันฟูก้าคันนั้นน่ะนะ ถ้าพ่อเธอไม่ว่าก็คงไม่มีทางเลือกอื่นแล้วแหละ รู้สึกผิดแฮะที่ต้องทิ้งรถตัวเองไว้ เดี๋ยวก็\nไม่ได้อยู่ด้วยกันแล้วแท้ ๆ"

# "Despite Lilly's obstinacy, and Hideaki's questions of whether or not we'd prefer to eat first than bet on a fish dinner that might fail to ever materialize, there is no way to dissuade Akira and Shizune as they agree on the transport plan."
"ถึงลิลลี่จะไม่ยอม และยังไม่แน่ใจกับคำตอบของคำถามจากฮิเดอากิว่าจะกินข้าวกันไปก่อนแทนที่จะหวังมื้อเย็นจากปลา\nที่อาจตกไม่ได้ดีหรือไม่ แต่ไม่มีใครอาจยั้งอากิระและชิซูเนะที่ตกลงเรื่องการเดินทางกันเรียบร้อยแล้ว"

stop music fadeout 5.0

scene ev shizune_car
with shorttimeskip

play ambient sfx_businterior fadein 1.0

# "My expectations of a somewhat relaxing drive through the countryside are fulfilled. Akira's driving is as smooth and peaceful as the surroundings, to the point where Misha falls asleep during the trip."
"และฉันก็ได้นั่งรถชมวิวชนบทสบาย ๆ ดังใจหวัง อากิระขับรถได้นิ่มและชวนให้ผ่อนคลายไม่ต่างอะไรกับบรรยากาศ\nโดยรอบ นิ่มเสียจนมิช่าหลับไปตลอดทาง"

# "I thought this trip would have been rather too slow-paced for Shizune's liking, but she seems to genuinely enjoy it. Even with Hideaki awkwardly sandwiched between her and the door, she just keeps looking out of the window and smiling."
"ฉันนึกว่าความเร็วรถจะช้าไม่ทันใจชิซูเนะ แต่เธอก็ดูจะเพลินจริง ๆ เธอยิ้มมองไปทางหน้าต่างรถโดยที่ระหว่างเธอ\nกับประตูมีฮิเดอากิเบียดอยู่ตรงกลาง"

stop ambient fadeout 0.5

scene bg shizu_fishing at left
with shorttimeskip

play ambient sfx_parkambience fadein 0.5

# "The area surrounding the river is quite beautiful. Akira and Shizune head off for the river so quickly that we have no choice but to chase them. We would be left in the dust, otherwise."
"พื้นที่โดยรอบแม่น้ำก็สวยดี อากิระและชิซูเนะรีบรุดไปทางแม่น้ำเร็วเสียจนพวกเราต้องวิ่งตาม ไม่งั้นต้องถูกทิ้งห่าง\nไว้แน่ ๆ"

show lilly basic_weaksmile_cas at left
show hideaki bored at center
show misha hips_grin_cas at right
with charaenter

# "I can see Hideaki and Lilly are just humoring their siblings, Lilly being the more unenthusiastic of the two. Misha seems as happy as ever, though. Looks like she managed to latch onto some of Shizune and Akira's excitement."
"ฮิเดอากิและลิลลี่ดูจะเป็นสีสันให้พี่ของตัวเองกันดี ถึงลิลลี่ดูจะไม่ได้ตื่นเต้นเท่าอีกคนก็เถอะ แต่มิช่าก็ดูเริงร่า\nเหมือนเคย ดูท่าจะดูดความตื่นเต้นจากชิซูเนะและอากิระมาได้บ้างแล้ว"

# "As for myself, I'd rather eat now, but the thought of fresh fish prepared by Lilly is appealing."
"ส่วนฉันอยากกินข้าวตอนนี้เลยมากกว่า แต่ก็อยากลองกินอาหารที่ทำจากปลาสด ๆ ด้วยฝีมือของลิลลี่เหมือนกัน"

# "The river is larger than I'd imagined, although very scenic and peaceful. Other than a small pier apparently built just to fish off of, this place looks untouched by civilization, and it makes me realize how much greenery I've seen lately."
"แม่น้ำกว้างกว่าที่คิดเอาไว้ แต่ก็สวยและสงบดี รอบ ๆ ไม่มีสิ่งปลูกสร้างใด ๆ นอกจากท่าน้ำที่ใช้ตกปลา จนฉันนึกได้ว่า\nช่วงนี้ได้เห็นธรรมชาติอยู่บ่อยครั้ง"

show shizu invis at offscreenright
show akira invis:
    center
    xpos 1.5
with None

show bg shizu_fishing at right
show lilly invis at Position(xpos=-0.6)
show hideaki invis at offscreenleft
show misha perky_confused_cas at left
show shizu basic_happy_cas:
    center
    xpos 0.37
show akira basic_smile:
    center
    xpos 0.8
with Dissolvemove(1.5)

# "Shizune pulls Misha away so that they can explain how to fish to Akira. Lilly and Hideaki are talking between themselves, so I decide to join the enthusiastic trio."
"ชิซูเนะลากตัวมิช่าไปเพื่อสอนอากิระตกปลา ลิลลี่และฮิเดอากิคุยกันอยู่ ฉันจึงเข้าไปร่วมวงสามคนที่แสนตื่นเต้น\nกันนั้น"

show akira basic_ending
with charachange

# aki "Hmm… so which one of these lures should I use then? Can I use this cute little one?"
aki "อืมม… แล้วฉันต้องใช้เหยื่อแบบไหนดี ใช้อันที่กระจุ๋มกระจิ๋มอันนี้ได้มั้ย"

show shizu basic_frown_cas
show misha sign_smile_cas
with charachange

# mi "Wait, wait~! This is a contest, we need to pick teams first! Shicchan and I will be on one team, of course. Hicchan, you're going to be on our team too, won't you? We can be the Student Council team~!"
mi "เดี๋ยว เดี๋ยว~! เราจะแข่งกันก็ต้องจับกลุ่มกันก่อน! แน่นอนว่าฉันกับชิจังจะอยู่ทีมเดียวกัน ฮิจัง นายก็จะอยู่ทีมเราด้วย\nใช่มั้ย จะได้เป็นทีมสภานักเรียนไง~!"

# hi "Okay."
hi "โอเค"

show akira basic_laugh
with charachange

# aki "All right, then. That makes me, Hideaki, and Lilly on the other team. Lilly, what should we call ourselves?"
aki "ได้ งั้นฉัน ฮิเดอากิ แล้วก็ลิลลี่จะอยู่ทีมเดียวกัน ลิลลี่ ชื่อทีมเอาอะไรดี"

stop music fadeout 2.0

play sound sfx_flash

show bg shizu_fishing at left
show lilly basic_sleepy_cas at twoleft
show hideaki bored at tworight
show misha invis at Position(xpos=0.85)
show shizu invis at offscreenright
show akira invis:
    center
    xpos 1.5
with Dissolvemove(0.5)

# $ doublespeak (li, hh, "I don't see why it matters.", "I don't think it matters.")
$ doublespeak (li, hh, "หนูไม่เห็นว่าจะสำคัญตรงไหน", "ผมว่าไม่สำคัญหรอก")


play sound sfx_flash

show bg shizu_fishing at right
show lilly invis at Position(xpos=-0.6)
show hideaki invis at offscreenleft
show misha perky_confused_cas at left
show shizu basic_angry_cas:
    center
    xpos 0.37
show akira basic_ending:
    center
    xpos 0.8
with Dissolvemove(0.5)

show akira basic_lost
with charachange

# aki "Team No-Enthusiasm it is…"
aki "ทีมห่อเหี่ยวเลี้ยวลงท่อแล้วกัน…"

play music music_comedy fadein 0.5

# "Yet again, Akira's best efforts are rebuffed. Shizune and Misha, on the other hand, have no lack of enthusiasm whatsoever."
"เป็นอีกครั้งที่ความพยายามของอากิระต้องถูกขัด ส่วนชิซูเนะและมิช่านั้นไม่ได้ห่อเหี่ยวหรืออะไรแม้แต่น้อย"

show misha hips_smile_cas
show shizu behind_frown_cas
with charachange

# ssh "Hisao! You can be our point man, please try hard to catch as many, or the biggest, fish possible."
ssh "ฮิซาโอะ! นายเปิดก่อนเลย ตกปลามาให้ได้เยอะ ๆ ใหญ่ ๆ เท่าที่ตกได้เลยนะ"

# hi "Why me? No one's even taught me how to fish yet."
hi "ไหงเป็นฉันล่ะ ยังไม่มีใครมาสอนฉันตกปลาเลยนะ"

show misha hips_grin_cas
show shizu behind_blank_cas
with charachange

# mi "We can do that now~."
mi "สอนตอนนี้เลยก็ได้~"

# "After a quick tutorial, Shizune immediately tries to draw us into a discussion about the strategy in a tag team fishing competition."
"หลังจากที่สอนคร่าว ๆ แล้วชิซูเนะก็ลากให้พวกเรามาคุยกันเรื่องแผนการแข่งตกปลาแบบทีมกัน"

# "Somehow, competition doesn't seem particularly applicable to a sport where you spend hours sitting down and hoping a fish bites a worm."
"ซึ่งการแข่งดูจะใช้ไม่ได้กับกีฬาที่ต้องนั่งเป็นชั่วโมง ๆ หวังให้ปลางับหนอนสักเท่าไหร่"

show shizu adjust_happy_cas
with charachange

# ssh "It looks like Hideaki got stuck with the spare rod. You know it's just a string tied to a bamboo pole, right? That means when deciding the order, you should go against him."
ssh "เหมือนฮิเดอากิจะได้คันเบ็ดสำรองที่เป็นสายเอ็นตกปลาผูกกับไม้ไผ่นะ แปลว่าถ้าจะต้องเลือกลำดับกันแข่ง นายต้อง\nไปตกกับเขา"

# hi "What, why me?"
hi "ฮะ? ไหงเป็นฉันล่ะ"

show misha sign_smile_cas
with charachange

# mi "You have the least experience here, Hicchan~."
mi "ก็ฮิจังมีประสบการณ์การตกปลาน้อยสุดนี่นา~"

# hi "Yeah? So who's the best here? Shizune? Hideaki is your brother, he's probably just as good. He probably fishes all the time, since he lives closer to a lake. He might even be better."
hi "อาฮะ? แล้วใครเก่งสุด? ชิซูเนะ? ฮิเดอากิเป็นน้องเธอนะ ก็คงจะเก่งพอกันนั่นแหละ แถมอาจตกปลาตลอดเพราะอยู่\nใกล้แม่น้ำเนี่ย เผลอ ๆ เก่งกว่าเธออีกมั้ง"

show akira basic_annoyed
with charachange

# aki "Watching you three makes my head hurt. You know I'm only hearing two thirds of a conversation, right? What's this about?"
aki "ดูเธอสามคนคุยกันแล้วปวดหัว รู้ใช่มั้ยว่าฉันรับรู้แค่สองในสามส่วนของบทสนทนาเนี่ย คุยอะไรกัน"

# hi "Picking our lineup."
hi "เลือกลำดับกันอยู่ครับ"

# "Akira makes a troubled face. She's getting impatient, which probably isn't too unreasonable."
"อากิระทำหน้าเครียด ดูจะเริ่มทนไม่ไหวแล้ว ซึ่งก็พอจะเข้าใจได้แหละ"

show shizu basic_sparkle_cas
with charachange

# ssh "If you're impatient, that only makes me more excited. Now I want to play for higher stakes."
ssh "ยิ่งเห็นรอไม่ไหวอย่างนี้ก็ยิ่งตื่นเต้นแล้วสิ อยากจะเล่นให้เดิมพันมากขึ้นแล้วสิ"

show akira basic_lost
with charachange

# aki "What's she saying?"
aki "เธอว่าไง"

# hi "She wants to play for higher stakes."
hi "บอกว่าอยากเอาเดิมพันให้มากขึ้นน่ะ"

show akira basic_laugh
with charachange

# aki "I wouldn't be too hasty; we have beginner's luck twice over on our side, after all. The only way you'll be able to beat that is by catching a whole ocean."
aki "อย่าเพิ่งรีบนักสิ เรายังมีดวงมือใหม่อยู่ตั้งสองเท่าเลยนะ จะเอาชนะได้ก็คงต้องตกมาให้ได้ทั้งมหาสมุทรเลยแหละ"

show shizu adjust_happy_cas
with charachange

shi "…"

show misha hips_grin_cas
with charachange

# mi "This is a freshwater body of water, you marine biologist~."
mi "นี่มันน้ำจืดนะแม่นักชีววิทยาทางทะเล~"

# "A weird insult, delivered with unblinking and innocent good cheer. Akira doesn't seem bothered. She laughs it off, and Shizune looks like her usual mischievous self again. I'm glad they get along."
"ด่าอะไรแปลก ๆ แถมพูดอย่างหน้าซื่อตาใสอย่างนั้นอีกต่างหาก อากิระดูจะไม่ว่าอะไรแล้วหัวเราะ ส่วนชิซูเนะก็กลับไป\nเป็นคนเจ้าเล่ห์อย่างเคย ดีจังที่สองคนนี้เข้ากันได้"

show akira basic_smile
with charachange

# aki "So are we going to pick teams, or what? I'm getting kinda hungry…"
aki "แล้วนี่จะจับกลุ่มกันตกหรืออะไร ฉันชักหิวแล้วนะ…"

show shizu basic_normal_cas
with charachange

# ssh "Hisao, Misha, and I are on one team, and Lilly, Hideaki, and you are on the other, aren't you?"
ssh "ฮิซาโอะ มิช่า แล้วก็ฉันจะอยู่ทีมเดียวกัน ส่วนลิลลี่ ฮิเดอากิ แล้วก็ทางนั้นอยู่อีกทีม ก็ตามนั้นนี่"

show akira basic_ending
with charachange

# aki "I suppose that's the most obvious arrangement. Wouldn't mixing it up a little be more fun, though? Eh?"
aki "ก็คงต้องอย่างนั้นแหละนะ แต่คละ ๆ กันหน่อยก็น่าสนุกออก เนอะ"

show misha perky_smile_cas
with charachange

# mi "Hmm~, you don't want to fish with your own sister?"
mi "อืมม~ แล้วไม่อยากตกปลากับน้องสาวตัวเองเหรอ"

show akira basic_boo
with charachange

# aki "Well, neither of us know how to fish, so putting both of us on the same team is kinda…"
aki "ก็เราสองคนไม่มีใครตกปลาเป็นเลยนี่ จะให้อยู่ทีมเดียวกันมันก็…"

# "Well, it sounds like I've heard something kind of dangerous. I try to change the subject before Shizune can turn that incredulous look on her face into anything more."
"แหม่ เหมือนจะได้ยินอะไรอันตรายเข้าแล้วสิ ฉันรีบเปลี่ยนเรื่องก่อนที่สีหน้าที่ไว้ใจไม่ได้ของชิซูเนะจะทันกลายเป็น\nอะไรอย่างอื่นที่มากกว่านั้น"

# hi "So, I guess you and Shizune know each other?"
hi "แล้วนี่แปลว่าพี่รู้จักกับชิซูเนะงั้นสิครับ"

show akira basic_smile
with charachange

# aki "Sure do. We go way back."
aki "รู้จักสิ รู้จักกันมานานแล้ว"

show shizu basic_normal2_cas
with charachange

# "Akira throws a knowing grin at Shizune. It's not until Misha's finished translating what she's said that Shizune gains a troubled face."
"อากิระยิ้มให้ชิซูเนะเป็นเชิงว่ารู้กัน พอมิช่าแปลให้แล้วชิซูเนะก็ทำสีหน้าปั้นยากขึ้นมา"

# "Akira sure is different from Lilly. Aside from how they look, she's much more informal and laid back. I expected Lilly's family to all be proper and formal like her, so this is a surprise. But, I feel like she's easy to talk to."
"อากิระต่างกับลิลลี่จริง ๆ ไม่ใช่แค่รูปลักษณ์ภายนอก แต่รวมทั้งนิสัยที่ดูเป็นกันเองและสบาย ๆ กว่ามาก ฉันแปลกใจ\nเพราะคิดว่าคนในบ้านลิลลี่จะเป็นคนที่เรียบร้อยผู้ดีอย่างลิลลี่กันหมดเสียอีก แต่รู้สึกเหมือนจะคุยด้วยง่ายแฮะ"

show akira basic_laugh
with charachange

# aki "As much as I like talking about catching fish, we should probably actually do it sometime."
aki "ก็อยากคุยเรื่องตกปลาอยู่หรอกนะ แต่รีบ ๆ ตกกันจริง ๆ เลยดีกว่า"

show shizu behind_blank_cas
with charachange

# ssh "Would you suggest that there should be a lineup, like in baseball? Or should it be everyone-at-once, or a tag battle style?"
ssh "จะให้มีรายชื่อคนตกแบบเบสบอล หรือจะตกทั้งสองทีมทีเดียวเลย หรือจะให้แข่งกันแบบคู่ต่อคู่ดี"

show shizu basic_sparkle_cas
with charachange

# ssh "Can everyone sit wherever they want, or do teams have to stick together? Do we call where we fish? What fish sizes will we be counting?"
ssh "จะให้นั่งตรงไหนก็ได้ หรือให้ทีมเดียวกันนั่งติดกัน จะให้ประกาศจุดตกปลาด้วยมั้ย จะนับขนาดปลากันยังไงดี"

show akira basic_lost
with charachange

# "Seeing Akira groan after Misha dutifully translates for her, Shizune rubs her glasses, laughing silently."
"ชิซูเนะถูแว่นหัวเราะอยู่เงียบ ๆ เมื่อเห็นอากิระโอดโอยหลังได้ฟังที่มิช่าแปลให้อย่างขันแข็ง"

show shizu adjust_happy_cas
with charachange

stop music fadeout 4.0

# ssh "Never mind. Let's just fish, then."
ssh "ช่างเถอะ งั้นก็ตก ๆ เลยดีกว่า"

show shizu behind_smile_cas
with charachange

# ssh "It can be an individual contest."
ssh "แข่งแบบหนึ่งต่อหนึ่งแล้วกัน"

stop ambient fadeout 2.0

scene ev shizu_fishing_ah
with shorttimeskip

play music music_ease

# "I sit down, ready to fish, although I'm not feeling very confident. Everyone else is already sitting, except Akira, who takes a seat next to me and throws her line out after taking off her suit jacket and rolling up her sleeves."
"ฉันนั่งลงเตรียมตกปลา ถึงจะยังไม่มั่นใจเท่าไหร่ก็เถอะ ทุกคนนั่งกันหมดแล้วยกเว้นอากิระที่เพิ่งถอดชุดสูทออก\nแล้วพับแขนเสื้อก่อนจะมานั่งลงข้างฉันแล้วเหวี่ยงคันเบ็ด"

# "Misha and Hideaki end up sitting on the shore and fishing together, as there's not enough room on the pier for everyone. Truth be told, I'd rather be sitting next to Shizune, but Akira seems approachable enough."
"มิช่าและฮิเดอากินั่งอยู่ริมตลิ่งตกปลาด้วยกันเพราะท่าน้ำไม่พอนั่ง เอาจริง ๆ ฉันอยากนั่งข้างชิซูเนะมากกว่า\nแต่อากิระก็พอเป็นคนที่คุยด้วยได้ละนะ"

# aki "Careful there, you're a little close. Don't tangle our lines, 'kay?"
aki "ระวังหน่อย ใกล้ไปแล้ว ห้ามให้สายพันกันนะ เค๊?"

# hi "So, you've never fished before?"
hi "แล้วนี่พี่ไม่เคยตกปลามาก่อนเหรอครับ"

# aki "No, but I've seen a bit of it on TV. I always wanted to catch one of those big fish with a sword for a face. Marlin, I think."
aki "ไม่อะ แต่เคยเห็นในโทรทัศน์อยู่ ฉันอยากตกปลาที่หัวเหมือนดาบนั่นมานานแล้ว ปลากระโทงมั้ง"

# li "If I recall correctly, those are from the ocean; they are saltwater fish."
li "ถ้าจำไม่ผิด เหมือนปลาที่ว่าจะเป็นปลาน้ำเค็มอยู่ในมหาสมุทรนะ"

# aki "I know that. Why's everyone acting like I don't know the difference between freshwater and saltwater fish?"
aki "รู้น่า ทำไมทุกคนถึงทำเหมือนฉันแยกปลาน้ำจืดกับปลาน้ำเค็มไม่ออกเนี่ย"

# li "If you aren't careful, you'll scare off the fish, saltwater or not."
li "ระวังหน่อยนะ เดี๋ยวปลาก็ตกใจหนีไปหมดหรอก น้ำเค็มน้ำจืดก็ช่าง"

# "Akira's voice is somewhat loud between her attempts to both egg on Shizune and keep Lilly entertained, so she may have a point. My line doesn't seem to be picking up anything, but I don't know how much of that is down to Akira."
"อากิระพยายามจะโหมไฟให้ชิซูเนะและดึงให้ลิลลี่สนุกไปด้วย แต่เสียงออกจะดังไปหน่อย ก็คงถูกของลิลลี่ละนะ\nเหมือนเบ็ดฉันจะยังไม่กระตุกหรืออะไร แต่ไม่รู้ว่าฝั่งอากิระเป็นยังไงแล้วบ้าง"

# "Shizune does her best to relax in the sun, and pulls the look off very well, but I can tell that she'd be slightly put off by not knowing what's being talked about. Not having Misha around can be a real problem."
"ชิซูเนะทำทีเป็นอาบแดดอยู่สบาย ๆ ได้ดีทีเดียว แต่ฉันรู้ว่าเธอคงแอบหงุดหงิดที่ไม่รู้ว่าทางนี้คุยอะไรกันอยู่ ไม่มีมิช่า\nแล้วลำบากจริง ๆ"

# ssh "Hisao, what's the score so far? Are we winning? I hope we are, given that I've entrusted you with our team's success."
ssh "ฮิซาโอะ คะแนนเท่าไหร่แล้ว นำอยู่หรือเปล่า หวังว่าจะนำอยู่นะ อุตส่าห์ฝากความหวังทีมไว้กับนาย"

# "I manage to do some awkward signing with creative placement of my rod. It's probably close to being gibberish in spoken terms."
"ฉันทำภาษามือแบบเก้ ๆ กัง ๆ โดยที่วางคันเบ็ดไว้แบบแปลก ๆ ถ้าเป็นเทียบการพูดแล้วก็คงแทบจับใจความไม่ได้"

# hi "You're like, right there. Can't you tell?"
hi "ก็เห็น ๆ กันอยู่นี่ ดูไม่ออกเหรอ"

# ssh "Disappointing; you let yourself get distracted. You have to stay focused."
ssh "น่าผิดหวังเสียจริง นายวอกแวกแล้ว นายต้องจดจ่อสิ"

# hi "Should have known. Well, it's 0-0 in any case."
hi "ขอโทษที เอาเถอะ คะแนนยัง 0-0"

# "Akira chuckles, although it's clear that really took the wind out of her sails."
"อากิระหัวเราะ ถึงจะเห็นจ๋อยไปตอนได้ยินคะแนนนั้นก็เถอะ"

# hi "Is it just numbers now, or are we keeping track of size, too?"
hi "แล้วนี่จะนับจำนวนหรือวัดขนาดด้วย"

# ssh "Both; grading matters."
ssh "ทั้งคู่ ต้องคิดคะแนน"

# hi "Who's going to be grading them? Are you a certified fish judge?"
hi "แล้วใครจะคิดคะแนน เธอมีใบรับรองกรรมการชั่งตวงวัดปลาหรือไง"

# "Shizune shakes her head to signify that she isn't."
"ชิซูเนะสั่นหัวเป็นเชิงว่าไม่มี"

# ssh "…But it doesn't seem like it would be very hard. Tell Misha to stop flailing her hands around like that, it's scaring all the fish away. And ask Hideaki why he hasn't even bothered to cast yet."
ssh "…แต่ก็ดูจะไม่ยากนี่ บอกมิช่าให้เลิกโบกมือไปมาอย่างนั้นได้แล้ว เดี๋ยวปลาก็หนีไปหมด แล้วบอกฮิเดอากิด้วยว่าทำไม\nยังไม่เหวี่ยงคันเบ็ดอีก"

# "I look over to the two and yell what Shizune said to them."
"ฉันหันไปตะโกนบอกที่ชิซูเนะฝากบอก"

# mi "Shicchan, I think he's upset that he's stuck with the backup rod~!"
mi "ชิจัง เหมือนเขาจะไม่พอใจที่ได้ใช้คันเบ็ดสำรองนะ~"

# "Since Misha is largely unable to sign anything coherently right now, she only gets a puzzled look from Shizune for a reply. Shizune just sighs after I translate it for her."
"มิช่ายังไม่สามารถทำภาษามือได้อย่างสมบูรณ์เท่าไหร่ ชิซูเนะได้แต่มองด้วยความงงงัน เธอถอนหายใจหลังจากที่ฉัน\nแปลให้"

# aki "Hey, even if you're depressed about it, you've got to try. You could catch the big one, for all you know. But you won't catch anything unless you do!"
aki "นี่ จะหดหู่หรืออะไรก็ช่าง ต้องลองก่อนนะ อาจจะตกได้ตัวใหญ่เลยก็ได้ แต่ถ้าไม่ลองก็ตกไม่ได้อะไรเลยนะ"

# "I feel that at least half of her encouragement is because if Hideaki does catch “the big one,” she wants to be there to eat it, and having six people fishing just leads to better chances of catching something than having five."
"ฉันสัมผัสได้ว่าส่วนหนึ่งที่ส่งกำลังใจไปอย่างนั้นเพราะอากิระอยากกินด้วยถ้าฮิเดอากิตกได้ “ตัวใหญ่” มาจริง ๆ\nและการที่มีหกคนช่วยกันตกก็ย่อมมีโอกาสมากกว่าห้าคน"

# "The constant awkward shuffling I have to do to communicate with Shizune, not to mention her increasing fidgeting, make me think it might be good to give her a go at fishing."
"พอต้องสลับคันเบ็ดไปมาเพื่อสื่อสารกับชิซูเนะแล้วก็รู้สึกว่าน่าจะถึงเวลาแล้วที่ต้องเปลี่ยนตัวให้เธอมาตกบ้าง เห็น\nทำท่ายุกยิกอยูุ่ด้วย"

# hi "Hey guys, can we switch over now?"
hi "นี่ทุกคน เปลี่ยนตัวกันได้หรือยัง"

# aki "Sure. Lilly?"
aki "ได้ ลิลลี่?"

# li "No, no, please. I have no idea how to fish."
li "ไม่ ไม่ต้องหรอก หนูตกปลาไม่เป็น"

# "I sign what they say, given that I seem to have taken Misha's place as Shizune's interpreter right now."
"ฉันทำภาษามือที่สองคนนี้คุยกัน เพราะเหมือนฉันจะต้องมาสวมบทมิช่าเป็นล่ามให้ชิซูเนะแล้ว"

# ssh "How magnanimous of you, Lilly."
ssh "ใจใหญ่ใจโตจังเลยนะลิลลี่"

# "Oh boy, here we go. I don't bother translating what she says for fear of sparking another fight."
"โอย เอาแล้วไง ฉันไม่แปลที่เธอบอกเพราะไม่อยากให้เกิดการวิวาทขึ้นอีก"

# hi "Shizune says you should at least try. It might even turn out to be fun."
hi "ชิซูเนะบอกว่าลองหน่อยก็ดีนะ อาจจะสนุกก็ได้"

# li "Very well. Akira, how do you use this?"
li "งั้นก็ได้ พี่ อันนี้ใช้ยังไงเหรอ"

# aki "It's pretty simple…"
aki "ง่ายนิดเดียว…"

# "I wonder how ethical it is to purposely completely change what Shizune said like that. At least it paid off."
"บิดเบือนสิ่งที่ชิซูเนะบอกอย่างนั้นมันผิดจริยธรรมมั้ยนะ แต่อย่างน้อยก็ไม่มีการวิวาทเกิดขึ้น"

scene ev shizu_fishing_sl
with shorttimeskip

# li "…I think I understand. What bait do you think would be the best to use? I'd prefer something that wouldn't hurt the fish too much."
li "…พอจะจับทางได้แล้วละ พี่ว่าเหยื่อแบบไหนดีสุดเหรอ หนูไม่อยากให้ปลาต้องเจ็บมาก"

# aki "If you're putting a hook through their mouth, I don't think the bait's going to hurt them much more."
aki "ถ้าเบ็ดมันจะเกี่ยวปาก ยังไงเหยื่อก็ไม่มีผลขนาดนั้นมั้ง"

# hi "And letting it go…? No, no, don't do that."
hi "ตกแล้วจะปล่อยเหรอ… ไม่ ๆ อย่าทำอย่างนั้น"

# li "But if it isn't big, there's little point in killing it…"
li "แต่ถ้าไม่ใช่ปลาตัวใหญ่ ฆ่าแกงไปก็ไม่เห็นมีประโยชน์อะไรเลย"

# "With my hands freed, it's much easier for me to interpret what everyone's saying. Now Shizune's the one that has to deal with her hands being full, but she seems to take it in her stride."
"พอมือฉันว่างแล้วก็แปลสิ่งที่ทุกคนพูดได้ง่ายขึ้น คราวนี้เป็นชิซูเนะแทนที่มือไม่ว่าง แต่เธอก็ดูตื่นเต้นเอามาก ๆ"

# ssh "That's so arrogant. Okay, I'll only reel in the big ones too, from now on."
ssh "อวดดีจังเลยนะ ได้ งั้นจากนี้ฉันจะตกเฉพาะตัวใหญ่ ๆ ก็แล้วกัน"

# aki "What's she saying?"
aki "เธอว่าไง"

# "Akira just sighs after I interpret for her."
"อากิระถอนหายใจเมื่อได้ฟังที่ฉันแปลให้"

# aki "No, I don't like that “only.” You know, a fish is a fish, and you take what you can get."
aki "ไม่สิ คำว่า “เฉพาะ” มันยังไงอยู่นะ ปลามันก็คือปลามั้ย ตกได้อะไรก็ต้องเอาตัวนั้นเลย"

# "Unfortunately, Shizune can't hear her and Lilly doesn't seem to be paying much attention now."
"แต่โชคไม่ดีที่ชิซูเนะไม่ได้ยิน ส่วนลิลลี่ก็ดูจะไม่สนใจเท่าไหร่"

# "Lilly's taking to fishing easily; it is a very relaxed activity, after all. It isn't long before they both catch a fish, and surprisingly, Lilly is just as interested in which is the bigger of the two as Shizune is."
"ลิลลี่จดจ่ออยู่กับการตกปลาไปแล้ว ก็นะ เป็นกิจกรรมที่ผ่อนคลายดีนี่นา ไม่นานทั้งสองคนก็ตกได้ ลิลลี่ดูจะอยากรู้\nพอ ๆ กับชิซูเนะว่าปลาของใครใหญ่กว่ากัน"

stop music fadeout 3.0

# "As the hours pass, it seems like they're even starting to have fun."
"ผ่านไปสองสามชั่วโมงทั้งสองคนก็ดูจะสนุกกันขึ้นมาแล้ว"

scene bg shizu_fishing_ss
with shorttimeskip

play ambient sfx_parkambience fadein 4.0
play music music_tranquil fadein 3.0

# "At the end of the day, we have several good-sized fish between us. Even Hideaki and Misha managed to catch one. No one brings up that we were competing to see who could catch more. I don't think it matters to anyone any more."
"จนสุดท้ายก็ได้ปลาที่ขนาดพอใช้ได้มาหลายตัว แม้แต่ฮิเดอากิและมิช่าก็ตกมาได้เหมือนกัน ไม่มีใครพูดถึงเรื่องที่\nตกปลาแข่งกันเลย คงไม่มีใครสนใจแล้วละนะ"

show akira basic_smile_ss at center
with charaenter

# "Shizune and Misha are talking between themselves some distance away, and Lilly and Hideaki are doing the same. I decide to take advantage of the quiet moment to talk with Akira."
"ชิซูเนะและมิช่าคุยกันอยู่สองคนอยู่ห่าง ๆ ลิลลี่และฮิเดอากิก็เช่นกัน ฉันจึงถือโอกาสช่วงที่เงียบ ๆ นี้คุยกับอากิระ"

# hi "Lilly and Shizune got on well today. I didn't really expect it, after seeing how they act towards each other in school."
hi "วันนี้ทั้งลิลลี่กับชิซูเนะดูเข้ากันดีนะครับ ปกติเห็นอยู่ที่โรงเรียนก็ไม่ค่อยถูกกันเท่าไหร่แท้ ๆ ผิดคาดเลย"

show akira basic_boo_ss
with charachange

# "She gives an amused snort. It looks like she doesn't take their feuding as seriously as I do."
"เธอแค่นหัวเราะยิ้ม ๆ เหมือนจะไม่คิดมากเรื่องที่สองคนนี้ไม่ลงรอยกันอย่างฉันเท่าไหร่"

# aki "They've got their reasons. Lilly and I are going away for a while tomorrow, so we thought we'd just pop by."
aki "สองคนนั้นก็มีเหตุผลของเขาแหละ เดี๋ยวพรุ่งนี้ลิลลี่กับฉันก็จะไม่ได้อยู่ที่นี่สักพักแล้ว เลยกะว่าจะแวบมาหน่อย"

show akira basic_ending_ss
with charachange

# aki "In the end, I'm glad we did."
aki "ซึ่งก็ดีใจนะที่ได้มา"

# "After a brief silence, she stretches loudly and then claps her hands to get everyone's attention."
"หลังจากที่เงียบไปสักพักเธอก็ยืดเส้นสายร้องโอดโอยแล้วตบมือดึงความสนใจจากทุกคน"

show akira basic_smile_ss
with charachange

# aki "Well, that looks like enough to feed everyone. We should be getting back, now."
aki "เอาละ น่าจะพอกินแล้วนะ กลับกันตอนนี้เลยดีกว่า"

show bg shizu_fishing_ss at bgright
show akira basic_smile_ss at tworight
with charamove

show lilly basic_weaksmile_cas_ss at twoleft
with charaenter

# "Lilly nods, but then hesitates. Even with her face clouding a bit, she still looks to be in a better mood than this morning. Akira really seems to know how to handle her, and defused her antipathy towards Shizune pretty well."
"ลิลลี่พยักหน้าก่อนจะทำท่าลังเล ถึงสีหน้าจะยังดูหม่น ๆ แต่ก็ดูอารมณ์ดีขึ้นกว่าตอนเช้า อากิระดูจะรู้วิธีรับมือเธอ\nกับนิสัยเย็นชาของเธอที่เป็นกับชิซูเนะได้ดีจริง ๆ"

show akira basic_ending_ss
with charachange

# aki "Today's catch looks delicious, I kinda wish I had some soy sauce so I could just eat it now."
aki "ปลาวันนี้ดูน่าอร่อยนะ อยากได้โชยุมาจิ้มกินตอนนี้เลยจริง ๆ"

show lilly basic_surprised_cas_ss
with charachange

# li "I thought you wanted me to cook it…"
li "ไหนพี่บอกจะให้หนูเอาไปทำกับข้าว…"

show akira basic_laugh_ss
with charachange

# aki "You don't think eating it raw would be okay?"
aki "อ้าว กินดิบไม่ได้เหรอ"

# "Despite Akira's protests, or joking as I can't tell which, we decide to wait to at least cook the fish before eating it."
"ถึงอากิระจะร้องประท้วง—หรือไม่ก็แค่หยอกเล่นเฉย ๆ เพราะฉันดูไม่ออกว่าพูดเล่นหรือพูดจริง—พวกเราก็ตัดสินใจว่า\nอย่างน้อยก็จะเอาไปทำกับข้าวก่อนกินกัน"

stop ambient fadeout 2.0

scene bg shizu_houseext_lights
with shorttimeskip

stop music fadeout 3.0

# "It's already become pretty late while we were out, and by the time we arrive back at Shizune's house, it's a good time for dinner."
"กว่าจะได้กลับกันก็เย็นมากแล้ว เมื่อมาถึงบ้านชิซูเนะก็ประจวบเหมาะได้จังหวะทานมื้อเย็นพอดี"

scene black
with dissolve

#************************************************

label th_S19:

scene bg shizu_guesthisao
with locationchange

play music music_pearly fadein 5.0

# "Some of my pills spilled out all over the bottom of my bag, which I didn't realize until minutes before I was set to go to bed last night. I spent quite a bit of time scraping them out of my luggage."
"ยาของฉันบางส่วนหกเกลื่อนอยู่ก้นกระเป๋า มารู้อีกทีก็ตอนที่ฉันเตรียมเข้านอน กว่าจะเก็บกวาดยาทั้งหมดได้\nก็ใช้เวลาพอสมควร"

# "By the time I get up, I'm already starting the day with a migraine from a combination of trouble falling asleep and waking up late."
"และเมื่อตื่นมาก็ปวดหัวรับวันกันเลยทีเดียว เพราะเมื่อคืนนอนไม่ค่อยหลับ แถมยังตื่นสายอีก"

scene bg shizu_living
show hideaki normal_up at center
with locationchange

# "When I step into the living room, Hideaki is there finishing up his breakfast. His fork raised midway to his mouth, he seems unsure whether he should continue eating or greet me. Maybe I should back out of the room."
"พอเดินไปที่ห้องนั่งเล่นก็เห็นฮิเดอากิที่กำลังกินข้าวเช้าจนใกล้หมดแล้ว เขาถือส้อมค้างไว้ดูไม่แน่ใจว่าจะกินต่อหรือ\nทักทายฉันก่อนดี หรือฉันจะเดินหนีไปก่อนดีนะ"

show hideaki triangle
with charachange

# hh "Good morning."
hh "อรุณสวัสดิ์ครับ"

# hi "Morning."
hi "อรุณ"

show hideaki thinking
with charachange

# hh "What do you think we should have for breakfast?"
hh "เช้านี้เรากินอะไรกันดีครับ"

# hi "“We?” Aren't you eating breakfast right now?"
hi "“เรา”? ตอนนี้นายก็กินอยู่ไม่ใช่เหรอ"

show hideaki normal
with charachange

# hh "Yes. Everyone else ate already."
hh "ครับ ทุกคนกินหมดแล้ว"

# "Despite that, he repeats his question again. He's just trying to be nice. It's an odd way to show it, but I appreciate it nonetheless, and I am feeling pretty hungry."
"ถึงอย่างนั้นเขาก็ถามซ้ำอยู่ดี คงหวังดีแหละนะ ถึงการกระทำจะแปลกไปหน่อย แต่ฉันก็ยินดีแหละ ฉันเองก็หิวอยู่\nเหมือนกัน"

# "I try to make some conversation with him while I'm getting my breakfast, to fill in the silence."
"ฉันหาเรื่องคุยระหว่างที่ตัวเองหาอะไรกินเพื่อไม่ให้บรรยากาศเงียบไป"

# hi "That fishing trip yesterday was fun. Do the Hakamichis and Satous often get together like that?"
hi "เมื่อวานไปตกปลาสนุกมากเลย ปกติสองบ้านนี้ไปด้วยกันอย่างนั้นบ่อยมั้ย"

show hideaki bored
with charachange

# hh "Not really."
hh "ไม่เท่าไหร่ครับ"

# hi "I see."
hi "เข้าใจละ"

# "I don't, really. There's a brief pause before Hideaki deigns to fill me in a little more."
"จริง ๆ ก็ไม่เข้าใจหรอก แล้วก็เงียบไปครู่หนึ่งก่อนฮิเดอากิจะเห็นควรว่าต้องเล่าเรื่องอะไรให้ฉันอีกหน่อย"

show hideaki thinking
with charachange

# hh "Family issues. Our fathers are brothers-in-law, and do not like each other."
hh "ปัญหาครอบครัวน่ะครับ พ่อของพวกเราเป็นพี่น้องบุญธรรมกัน แล้วก็ไม่ชอบพอกันเท่าไหร่"

# "Hearing that gives me plenty to think about. It puts the way Shizune and Lilly deal with each other into context, and makes me even more wary of getting involved."
"พอรู้อย่างนั้นแล้วฉันก็คิดอะไรอีกหลายอย่าง เบื้องหลังสาเหตุที่ชิซูเนะและลิลลี่ทำตัวอย่างนั้นใส่กันก็ปรากฏ ฉันยิ่ง\nรู้สึกว่าต้องระวังกับเรื่องนี้ขึ้นไปอีก"

# hi "Ah. Family issues can be troublesome."
hi "อ้อ บางทีปัญหาครอบครัวมันก็ยุ่งยากงั้นแหละนะ"

show hideaki normal
with charachange

# "Hideaki simply nods as I sit at the table with my breakfast. I wish he were a little easier to converse with."
"ฮิเดอากิพยักหน้ารับไม่ว่าอะไรจังหวะที่ฉันมานั่งกินข้าวเช้าที่โต๊ะ ถ้าเป็นคนคุยด้วยง่ายอีกหน่อยคงดี"

# "While I'm eating, I notice that the house seems oddly quiet for a place with Misha in it. If Shizune and Misha ate breakfast already, it can't be because they're asleep. I ask Hideaki where they are."
"ระหว่างที่กินฉันก็รู้สึกว่าถ้ามิช่าอยู่บ้านคงไม่เงียบขนาดนี้ ถ้าทั้งชิซูเนะและมิช่ากินข้าวเช้าไปแล้วก็แปลว่าต้องตื่นแล้ว\nฉันถามฮิเดอากิว่าสองคนนั้นไปไหน"

show hideaki bored
with charachange

# hh "Shizune and Misha left to run some errands for our dad. The local businesspeople love dealing with Misha, so he insisted."
hh "พี่ชิซูเนะกับพี่มิช่าออกไปทำธุระให้พ่อครับ นักธุรกิจท้องถิ่นเขาชอบคุยกับมิช่า พ่อเลยวานให้ไป"

# hi "Well, she's got a nice and cheerful personality. I can see why they would. Maybe you should start taking lessons from her, you could increase your business connections."
hi "ก็นะ เป็นคนร่าเริงสดใสดี พอเข้าใจได้แหละว่าทำไมถึงชอบ นายก็น่าจะดูมิช่าไว้บ้างนะ เผื่อจะได้เพิ่มเส้นสาย\nทางธุรกิจ"

show hideaki confused
with charachange

# hh "Are you serious?"
hh "เอาจริงเหรอครับ"

# "He sounds serious. I don't know what kind of business connections a little kid would need. Maybe he wants to have the best bake sale fundraiser ever."
"น้ำเสียงเขาจริงจัง ฉันไม่รู้ว่าเด็กตัวเล็ก ๆ อย่างเขาจะเอาเส้นสายทางธุรกิจไปทำอะไร สงสัยอยากเป็นคนขายขนม\nหาเงินเข้าโรงเรียนรายใหญ่มั้ง"

# "It's a shame I'll eventually have to leave here and won't be around to see whatever he is planning."
"น่าเสียดายที่ฉันจะไม่ได้อยู่ดูว่าเขาวางแผนคิดจะทำอะไรกันแน่"

# "I wonder what kind of person Shizune's dad is again, other than relatively outdoorsy. What I know so far is that he asks his business partners and friends of his daughter to do favors for him."
"จะว่าไปแล้ว พ่อของชิซูเนะเป็นคนแบบไหนกันนะ นอกจากที่ว่าเป็นคนชอบทำกิจกรรมนอกบ้านแล้ว ตอนนี้ก็รู้อีกว่า\nเป็นคนที่วานให้คู่ค้าทางธุรกิจกับเพื่อนของลูกสาวตัวเองไปทำงานให้"

# "I'm assuming he's extremely shy or extremely lazy. Maybe it's a rude call to make so early, but it would certainly explain a large chunk of Shizune's personality."
"เดาว่าคงจะเป็นคนขี้อายมาก ๆ หรือไม่ก็ขี้เกียจมาก ๆ ก็หยาบคายอยู่หรอกที่ด่วนสรุปตัดสินไปอย่างนั้น แต่ถ้าเป็น\nอย่างนั้นจริง ก็จะคลายสงสัยไปได้พอสมควรเลยว่าทำไมบุคลิกชิซูเนะถึงเป็นอย่างนั้น"

show hideaki triangle
with charachange

# hh "Do you want to go anywhere?"
hh "อยากไปที่ไหนมั้ยครับ"

# hi "Not really. Why, do you?"
hi "ไม่เท่าไหร่ ทำไม นายอยาก?"

show hideaki normal
with charachange

# hh "I thought there might be somewhere you would want to go. You don't want to do some sightseeing, or eat at a specific restaurant?"
hh "ผมคิดว่าพี่อาจจะอยากไปที่ไหนสักที่ ไม่อยากไปเที่ยวหรือไปกินข้าวที่ร้านอาหารสักร้านเหรอครับ"

# hi "I don't know. I've never been here before."
hi "ไม่รู้สิ พอดีไม่เคยมาแถวนี้"

show hideaki thinking
with charachange

# hh "I see."
hh "อย่างนี้นี่เอง"

# "I was just about to ask him about what Shizune was like when she was younger, but he's managed to sidetrack me with just one question. This appears to be as awkward a conversation for him as it is for me."
"เมื่อกี้กำลังจะถามว่าตอนเด็ก ๆ ชิซูเนะเป็นยังไง แต่เขาก็ถามแทรกขึ้นมาก่อน เหมือนว่าต่างคนต่างก็รู้สึกเก้ ๆ กัง ๆ กับ\nบทสนทนานี้"

# hi "You're sure eager to please today. Why are you being so nice? Are you showing your secret nice side now that your sister isn't around?"
hi "วันนี้นายพร้อมปรนนิบัติเหลือเกินนะ ทำไมทำตัวดีขนาดนี้ พอพี่นายไม่อยู่แล้วจะเผยด้านดี ๆ ที่ซ่อนไว้หรือไง"

show hideaki bored
with charachange

# hh "You're sort of right. Shizune wanted me to keep you company today."
hh "ก็ประมาณนั้นแหละครับ พี่ชิซูเนะอยากให้ผมอยู่เป็นเพื่อนพี่"

# "I don't want to trouble him, and try to make him see that, but Hideaki is as stubborn as his sister and feels as if this is his duty. He also seems to be earnestly trying to be nice."
"ฉันทำท่าให้เห็นว่าไม่อยากรบกวน แต่เขาก็เป็นคนรั้นพอ ๆ กับพี่ แถมยังทำเหมือนเป็นหน้าที่ของตัวเองอีก\nทั้งเหมือนจะพยายามทำตัวดีจริง ๆ ด้วย"

# "Quickly, I start to realize that Hideaki's idea of fun is fishing, collecting cameras, and making esoteric puns. Fishing is fun, but it's something I would rather do than discuss. The same goes for cameras; I'd rather handle them than collect them."
"และฉันก็ฉุกคิดได้ว่าคำว่าสนุกของฮิเดอากิคือการตกปลา สะสมกล้อง กับการเล่นมุกฝืด ๆ เข้าใจยาก ตกปลาก็สนุก\nอยู่หรอก แต่ได้ตกจริง ๆ คงดีกว่าคุยเฉย ๆ เรื่องกล้องก็เหมือนกัน ให้ฉันเอากล้องไปถ่ายรูปยังดีกว่าให้มา\nเก็บสะสมเฉย ๆ"

# "This is something Hideaki picks up on himself."
"ซึ่งฮิเดอากิก็เหมือนจะรู้ตัว"

show hideaki normal_up
with charachange

# hh "Are you bored?"
hh "เบื่อเหรอครับ"

# hi "I'm not bored at all."
hi "ไม่เบื่อเลย"

# "I almost yawn the words, so Hideaki ignores them entirely."
"พูดไปเมื่อกี้ก็เกือบหลุดหาวจนฮิเดอากิไม่เชื่อ"

show hideaki sad
with charachange

# hh "You are bored. Shizune said to be entertaining, and I think I don't know how to do that."
hh "พี่เบื่อ พี่ชิซูเนะบอกให้ผมทำตัวให้สนุก แต่ผมไม่รู้จะทำยังไง"

# hi "I am entertained."
hi "ฉันสนุก"

show hideaki serious
with charachange

# hh "You don't sound entertained."
hh "ฟังดูไม่สนุกเลยนะครับ"

# hi "I am!"
hi "สนุก!"

show hideaki normal
with charachange

# hh "Why do you yell? I hope you do not yell so much around Shizune."
hh "ตะโกนทำไมครับ พี่คงไม่ได้ตะโกนกับพี่ชิซูเนะบ่อย ๆ นะครับ"

# "It's hard to tell if he's joking. Either way, I'm a bit surprised. I try to play it off and change the subject."
"ไม่รู้ว่าเมื่อกี้พูดเล่นหรือเปล่า แต่ก็ตกใจหน่อย ๆ เหมือนกัน ฉันทำเนียน ๆ แล้วเปลี่ยนเรื่อง"

# hi "Do you just collect cameras, or are you into photography, too?"
hi "นายสะสมกล้องอย่างเดียวหรือชอบถ่ายรูปด้วย"

show hideaki bored
with charachange

# hh "Not really. If I did, there would be more photos in this house than there currently are. What is there to take pictures of?"
hh "ไม่เท่าไหร่ครับ ถ้าชอบจริงในบ้านคงมีรูปถ่ายเยอะกว่านี้ มีอะไรให้ถ่ายรูปด้วยเหรอครับ"

# hi "I don't know. Birds? Architecture? One of those restaurants you were talking about? I thought this city had tons of cool stuff. How can you live in a place with so much to do and do nothing?"
hi "ไม่รู้สิ นก? สถาปัตยกรรม? ร้านอาหารที่นายพูดถึง? เมืองนี้มีอะไรดี ๆ เยอะเลยนะ มาอยู่เฉย ๆ ได้ไงเนี่ย มีอะไรให้ทำ\nตั้งเยอะแยะ"

show hideaki triangle
with charachange

# hh "I thought you didn't know what there was to do here. Suddenly you have many ideas and are an authority on how interesting it is. You are like our board of tourism. Do you want to go watch birds or buildings?"
hh "ไหนบอกว่าไม่รู้ว่าเมืองนี้มีอะไรไงครับ ทำไมอยู่ ๆ ถึงรู้ขึ้นมาแล้วชี้นิ้วบอกได้ว่าน่าสนใจแค่ไหน ทำตัวเหมือนเป็น\nคณะกรรมการกรมการท่องเที่ยวเลย อยากไปดูนกดูตึกเหรอครับ"

# hi "Okay, okay, no need to get so mad."
hi "โอเค โอเค ไม่เห็นจะต้องอารมณ์เสียเลย"

show hideaki normal
with charachange

# hh "…I'm not mad. I just think that if you feel that strongly about it, then we should go to an amusement park."
hh "…ผมไม่ได้อารมณ์เสีย ผมแค่คิดว่าถ้าพี่คิดอย่างนั้นจริง ๆ ก็ไปสวนสนุกกันดีกว่า"

# hi "Why?"
hi "ทำไม"

show hideaki confused
with charachange

# hh "So that you can be amused. It will be fun."
hh "พี่จะได้สนุก สนุกแน่ ๆ"

# "Will he have this same flat, un-fun expression on his face while we're riding roller coasters and drop towers? It would sure bring the fun levels down. The thought does not convince me that it's worth the trip."
"ถ้าได้ไปนั่งรถไฟเหาะแล้วจะยังทำหน้านิ่ง ๆ เบื่อโลกแบบนี้อยู่หรือเปล่า ไม่งั้นคงไม่ได้สนุกเต็มที่เท่าไหร่ แค่คิดก็\nรู้สึกแล้วว่าถ้าไปไม่คุ้มแน่ ๆ"

# hi "I don't know, it always sounded to me like going to an amusement park meant you spend more time waiting in lines than actually doing stuff. You'd have to go earlier than this just to skip the lines."
hi "ไม่รู้สิ ฉันว่าไปสวนสนุกนี่เสียเวลาต่อแถวนานกว่าได้เล่นอะไรจริง ๆ อีก ถ้าไม่อยากไปต่อแถวนาน ๆ ก็ต้องไป\nให้เช้ากว่านี้"

show hideaki normal
with charachange

# hh "Have you ever been to one?"
hh "เคยไปเหรอครับ"

# hi "No, but it seems like that is what it's like."
hi "เปล่าหรอก แต่ก็ดูจะเป็นอย่างนั้น"

show hideaki bored
with charachange

# hh "…Fine. What about a regular park? There is one nearby that Shizune likes going to. Maybe she will be there, and I can unload you onto her."
hh "…ครับ งั้นสวนสาธารณะเป็นไง แถวนี้มีสวนสาธารณะที่พี่ชิซูเนะไปบ่อย ๆ ด้วย เผื่อเจอพี่ชิซูเนะที่นั่นแล้วผมจะได้\nส่งต่อพี่ให้พี่ชิซูเนะ"

# hi "What do you mean “unload?” I'm not luggage."
hi "“ส่งต่อ” นี่คืออะไร ฉันไม่ใช่สัมภาระนะ"

show hideaki triangle
with charachange

# hh "You don't want to go to an amusement park. I don't know what to do."
hh "พี่ไม่อยากไปสวนสนุก ผมก็ไม่รู้จะทำยังไง"

# "He looks as though I've hurt his feelings by refusing to go with him. I am already rationalizing my decision. I don't like waiting in lines. It would be too much like a date. I'd rather go with Shizune. It would be too tiring."
"เหมือนที่ปฏิเสธไปเมื่อกี้จะเป็นการทำร้ายจิตใจเขาแล้ว แต่ฉันก็อธิบายเหตุผลไปแล้ว ฉันไม่ชอบไปยืนต่อแถวรอ\nจะเหมือนเป็นการเดตเสียมากกว่า ถ้าจะไปก็ไปกับชิซูเนะดีกว่า คงเหนื่อยแย่"

# hi "It's nothing personal, it's just that I kinda wanted Shizune to show me around town instead."
hi "ฉันก็ไม่ได้อะไรหรอก แค่ว่าฉันอยากให้ชิซูเนะเป็นคนพาฉันไปเที่ยวดูเมืองนี้มากกว่า"

stop music fadeout 2.0

# "And I don't think that with my condition going to an amusement park would be such a hot idea."
"แล้วโรคของฉันก็คงไม่ถูกกับสวนสนุกสักเท่าไหร่"

scene bg shizu_park
with locationskip

play music music_soothing fadein 0.5

# "The park is close enough that their property could almost be considered an extension of it. Both it and Shizune's backyard look about the same, except that the park has benches and more people."
"สวนสาธารณะนั้นอยู่ใกล้จนคล้ายว่าเป็นส่วนหนึ่งของบ้าน ทั้งสวนหลังบ้านของชิซูเนะและที่นี่นั้นดูคล้ายกัน\nจะไม่เหมือนก็ตรงที่นี่มีม้านั่งกับคนเยอะกว่า"

# "That said, it's quite nice. There are even people out walking their dogs, and children flying kites that can be seen lazily drifting back and forth over trees in the distance. I could sit here in a relaxing and scenic place like this forever."
"แต่บรรยากาศก็ดีใช้ได้ มีคนพาหมามาเดินเล่น มีเด็กที่เล่นว่าวที่ลอยเอื่อยไปมาตามต้นไม้อยู่ลิบ ๆ ทั้งภาพสวย ๆ\nกับบรรยากาศชวนผ่อนคลายอย่างนี้ทำให้รู้สึกว่าไม่อยากไปไหนเลย"

show hideaki bored at center
with charaenter

# "Hideaki, on the other hand, looks like he's extremely bored. I want to poke him to see if he is still alive. But, would he react either way?"
"ในขณะที่ฮิเดอากินั้นดูเบื่อเต็มกลืน อยากจิ้ม ๆ ดูว่าตายหรือยัง แต่ต่อให้ไม่ตายแล้วจะตอบสนองด้วยเหรอ"

# hi "Are you bored?"
hi "เบื่อเหรอ"

show hideaki normal
with charachange

# hh "No. Are you going to jog or play frisbee with dogs like everyone else? Is that what people do in parks?"
hh "เปล่าครับ จะไปวิ่งหรือเล่นขว้างจานร่อนกับหมาอย่างคนอื่น ๆ เหรอครับ คนที่มาสวนสาธารณะเขาทำอย่างนั้นกัน\nใช่มั้ย"

# hi "Well, you go to parks to get back to nature and enjoy the atmosphere. That's why you jog in the park, instead of just on the sidewalk or something. You can jog anywhere."
hi "ก็ที่คนมาสวนสาธารณะก็เพื่อจะมาดื่มด่ำกับบรรยากาศธรรมชาตินี่แหละ คนถึงได้มาวิ่งที่สวนสาธารณะ ไม่ได้ไปวิ่ง\nตามทางเท้าหรือที่อื่น จริง ๆ ไอ้วิ่งน่ะวิ่งที่ไหนก็ได้"

# hi "I can't believe I am having this conversation. How can you not know this? You shouldn't have brought that up, it's too weird. Haven't you ever heard of “children should be seen, not heard?”"
hi "นี่ฉันต้องมาคุยเรื่องนี้จริง ๆ เหรอ ไม่รู้ได้ไงเนี่ย นายไม่น่าพูดเรื่องนั้นขึ้นมาเลย แปลกเกิน ไม่เคยได้ยินเหรอ\nที่เขาว่า “เด็กไม่ควรพูดมาก” น่ะ"

show hideaki bored
with charachange

# hh "Yes."
hh "ครับ"

show hideaki triangle
with charachange

# hh "I lied. I'm bored. Would you like to play a game?"
hh "ผมโกหก ผมเบื่อ อยากเล่นเกมมั้ยครับ"

# "I groan audibly enough to hope that he understands I don't want to. He doesn't care. In fact, he's already toying with a deck of playing cards."
"ฉันร้องโอดโอยดัง ๆ ให้พอที่จะทราบว่าฉันไม่อยากเล่น ซึ่งเขาไม่สนใจ อันที่จริง ตอนนี้ในมือเขาก็กำลังจับไพ่\nหนึ่งสำรับเล่นอยู่แล้ว"

show hideaki serious
with charachange

# hh "Why are you upset? That is why we are here."
hh "ทำไมถึงอารมณ์ไม่ดีล่ะครับ ที่มาก็เพื่อเล่นนี่ครับ"

# hi "I thought we were here to look for Shizune."
hi "ไหนบอกว่าจะมาหาชิซูเนะ"

show hideaki happy
with charachange

# hh "Exactly. That is why we should play a game. It's a Shizune trap. You can trap anything, including people."
hh "ครับ เพราะงั้นถึงได้ต้องเล่นเกมไงครับ เป็นกับดักที่ใช้ดักพี่ชิซูเนะ เราจะดักอะไรก็ได้ แม้แต่คน"

show hideaki thinking
with charachange

# hh "If we compete against each other in the spirit of competition and in a sportsmanly manner, she will be drawn here to challenge the winner, like a shark. Then I will defeat her like a safari hunter. Then take a photo of the award ceremony."
hh "ถ้าแข่งกันด้วยจิตวิญญาณนักแข่งอย่างมีน้ำใจนักกีฬาแล้วพี่ชิซูเนะจะต้องมาท้าดวลกับผู้ชนะเหมือนอย่างฉลาม\nแน่ครับ จากนั้นผมก็จะกำราบเหมือนอย่างนักล่าสัตว์ป่า แล้วก็จะถ่ายรูปงานฉลองมอบรางวัล"

# "Sharks do not go around challenging people to games of chance like dojo breakers."
"ฉลามไม่ได้ไปท้าดวลใครต่อใครกับเกมวัดดวงอย่างพวกที่ชอบไปตะลอนท้าประลองตามแต่ละสำนักนะ"

# hi "When did you bring that camera? Anyway, no. I get enough games hanging out with your sister."
hi "แล้วนี่เอากล้องมาตอนไหนเนี่ย แต่เอาเหอะ ไม่อะ แค่อยู่กับพี่นายฉันก็เล่นเกมมาเยอะพอแล้ว"

show hideaki normal
with charachange

# hh "No, come on. It will be fun. We can play chess."
hh "ไม่เอาน่าครับ สนุกแน่ หรือจะเล่นหมากรุกก็ได้"

# hi "Please, no. Besides, playing chess in the park is something old people do, like fishing. You're going to get old too fast if you keep doing all this old man stuff."
hi "ขอร้องเถอะ แล้วมีแต่คนแก่หรอกที่มาเล่นหมากรุกในสวนสาธารณะเนี่ย ตกปลาก็มีแต่คนแก่ที่ตก ทำอะไรอย่างคนแก่\nแบบนั้นเดี๋ยวก็แก่เร็วหรอก"

show hideaki darkside
with charachange

# "Hideaki freezes like I've suddenly started speaking a foreign language. Maybe I've offended him again. Maybe he's secretly 50 years old and has just aged incredibly well. Him being Shizune's brother could be a cover story."
"ฮิเดอากิตัวแข็งทื่อไปราวกับว่าฉันพูดภาษาต่างชาติอยู่ สงสัยคงไปจี้ใจดำอีกแล้ว จริง ๆ แล้วเขาอาจจะอายุ 50 ปีแล้ว\nแค่ว่ายังดูเด็กเฉย ๆ แล้วที่บอกว่าเป็นน้องนี่ก็อาจเป็นแค่เรื่องแต่งก็ได้"

show hideaki disapproves
with charachange

# hh "What about checkers, or go? Or even backgammon is fine, even though I don't like it. If board games aren't your thing, we can play card games. Anything other than seven card, because it is for wimps."
hh "งั้นหมากฮอสล่ะครับ หมากล้อม หรือจะแบ็กแกมมอนก็ได้ครับ ถึงผมจะไม่ชอบก็เถอะ ถ้าพี่ไม่ชอบเกมกระดาน งั้นเล่น\nเกมไพ่ก็ได้ครับ อะไรก็ได้ที่ไม่ใช่แข่งกันเรียงไพ่ เพราะมีแต่พวกกระจอกที่เล่นกันอย่างนั้น"

show hideaki evil
with charachange

# hh "Are you afraid that you will lose? If you can beat me I'll give you candy."
hh "กลัวว่าจะแพ้เหรอครับ ถ้าพี่เอาชนะผมได้ผมจะให้ขนม"

# hi "Hideaki, you are just like Shizune. I'm starting to think this is all a pretense to play games."
hi "ฮิเดอากิ นายนี่เหมือนชิซูเนะเลย ฉันเริ่มคิดแล้วว่าหรือทั้งหมดนี่คือแผนที่จะได้มาเล่นเกมกัน"

show hideaki thinking
with charachange

# hh "No. That is not true."
hh "ไม่จริงสักหน่อยครับ"

# hi "You are! I bet that competitive streak is genetic. I'll sell you to science."
hi "จริงสิ! พนันได้เลยว่าเชื้อชอบแข่งเนี่ยอยู่ในสายเลือดแล้ว เดี๋ยวต้องลองเอาไปขายให้พวกนักวิทยาศาสตร์\nวิเคราะห์ดูแล้ว"

show hideaki normal
with charachange

# hh "No one can own a human being."
hh "ไม่มีใครครอบครองมนุษย์ได้หรอกครับ"

# hi "How about I teach you some sign language instead?"
hi "งั้นฉันจะสอนภาษามือให้ ว่าไง"

# hi "When Shizune asked me if I wanted to come here, we talked a little, and it seemed like you and your dad don't use sign language. I'm just guessing, but if you don't, I could teach you some. I'm not a master at it, though."
hi "ตอนที่ฉันขอชิซูเนะว่าจะมาด้วยก็ได้คุยกันหน่อยหนึ่งแล้วได้รู้ว่าทั้งนายกับพ่อนายไม่มีใครรู้ภาษามือเลย จริง ๆ\nก็แค่เดาว่างั้นนะ แต่ถ้านายไม่รู้จริง ๆ ฉันก็พอสอนให้ได้ แต่ไม่ได้เก่งอะไรขนาดนั้นนะ"

# hi "I think it might be good for you to move your arms more, anyway."
hi "คือยังไงการขยับแขนให้มากขึ้นอีกหน่อยก็น่าจะดีกับตัวนาย"

# "He barely moves his arms. Most of the time they just hang limply at his sides. How unnerving."
"เขาแทบไม่ขยับแขนเลย ส่วนใหญ่ก็แค่ปล่อยไว้เฉย ๆ อยู่ข้างลำตัว เห็นแล้วก็รู้สึกแปลก ๆ"

# "It's been bothering me that Shizune's entire family apparently doesn't know how to sign. I wonder what she did before she met Misha. Did they just hire translators for her? Did she write out everything on that pad she carries around?"
"ฉันอดคิดมากไม่ได้ที่ว่าทั้งบ้านชิซูเนะเหมือนจะไม่มีใครรู้ภาษามือเลย ก่อนที่จะมาเจอกับมิช่านี่อยู่กันยังไง\nจ้างล่ามเหรอ หรือเขียนใส่กระดาษสมุดที่พกติดตัวเล่มนั้น?"

# "The second is the most likely, or she could type it out on a phone. That would explain why she dislikes using the pad so much. Sad as it is, I can sort of see why Hideaki or her dad might not have bothered to learn sign language."
"ซึ่งเหมือนจะเป็นอย่างที่สองมากกว่า หรือไม่ก็พิมพ์ผ่านโทรศัพท์เอา ซึ่งถ้าเป็นอย่างนั้นก็ไม่แปลกที่เธอจะไม่ชอบ\nใช้กระดาษ ถึงจะคิดแล้วจะหดหู่ แต่ฉันก็พอเข้าใจได้ว่าทำไมทั้งฮิเดอากิและพ่อของเธอไม่ได้กระตือรือร้นที่จะเรียน\nภาษามือเลย"

# "It probably was too much of a hassle at the time. It's very easy to think that. From what I've seen so far, though, neither of them hold it against each other or are too badly affected by it. It could be that I'm overthinking the situation."
"ตอนนั้นก็คงมองว่าเป็นเรื่องยุ่งยากเกินไป ของแบบนี้จะมองว่าลำบากก็ไม่แปลกอะไรเลย แต่เท่าที่ดูก็ไม่เห็นว่าจะ\nเกลียดกันเพราะเรื่องนี้หรือคิดมากเรื่องนี้เท่าไหร่ ฉันอาจจะคิดมากไปเองก็ได้"

# hi "Come on. Well, to be honest, I'm still learning sign language myself. I brought all my books along with me so I can keep up, you know? Still, I can at least teach you the alphabet. It's pretty simple. This is “kite.”"
hi "เถอะน่า คือ เอาตรง ๆ ฉันก็ยังเรียนภาษามืออยู่เหมือนกัน เนี่ย ฉันขนหนังสือของฉันมาอ่านเพิ่มด้วย แต่อย่างน้อยฉัน\nก็พอจะสอนพวกตัวอักษรให้นายได้นะ ง่ายนิดเดียวเอง อย่างนี่คือคำว่า “ว่าว”"

# "I feel really corny right now, and even more so when Hideaki stares back at me blankly as if the entire concept of learning is alien to him."
"พูดไปก็ขนลุกกับตัวเอง ยิ่งพอฮิเดอากิเหม่อมองมาทางฉันราวกับว่าการเรียนรู้อะไรสักอย่างเป็นสิ่งประหลาดกับตัวเขา\nแล้วก็ยิ่งหนักกว่าเก่าอีก"

show hideaki bored
with charachange

# hh "Shizune liked flying kites here as well."
hh "พี่ชิซูเนะก็ชอบมาเล่นว่าวที่นี่"

# "This is his attempt to salvage the conversation, and I'm happy to oblige."
"เขาพยายามจะกอบกู้บทสนทนานี้ขึ้นมาให้ได้ ซึ่งฉันยินดียิ่งที่จะตามน้ำด้วย"

# hi "Fishing, and now kites, too? Shizune really likes all these relaxing hobbies?"
hi "ตกปลาไม่พอ เล่นว่าวอีกเหรอ ชิซูเนะชอบกิจกรรมชวนผ่อนคลายอะไรอย่างนี้จริงเหรอเนี่ย"

show hideaki thinking
with charachange

# hh "Fighter kites. Actually, about Shizune—{w=0.5}{nw}"
hh "เล่นว่าวแข่งกัน อันที่จริง เรื่องที่พี่ชิซูเนะ—{w=0.5}{nw}"

stop music fadeout 0.3

show misha cross_grin_cas behind hideaki:
    center
    ypos 1.1 alpha 0.0
    linear 0.2 ypos 1.0 alpha 1.0
show hideaki ohshit
with vpunch

# "Hideaki freezes as Misha appears behind him and puts her hands over his eyes."
"ฮิเดอากิตัวแข็งทื่อไปทันทีที่มิช่าเข้ามาทางด้านหลังแล้วเอามือปิดตาเขา"

play music music_comedy fadein 0.5

# mi "Hi hi~! Guess who~!"
mi "ไง~! ทายซิใครเอ่ย~!"

# "He seemed to finally be loosening up, too."
"เหมือนเขาเองก็เริ่มผ่อนคลายลงแล้วด้วย"

# hi "Hi, Misha. Is Shizune with you?"
hi "ไงมิช่า ชิซูเนะมาด้วยมั้ย"

# mi "Hicchan, no spoilers! Don't spoil it, don't ruin the surprise, okay~?"
mi "ฮิจัง ห้ามบอก! ห้ามเฉลย ห้ามทำความแตก โอเคนะ~"

show hideaki thinking
with charachange

# hh "Misha."
hh "มิช่า"

show bg shizu_park at bgright
show hideaki normal at tworight
show misha perky_confused_cas at twoleft
with dissolvecharamove

# mi "Bingo~! That's right! But~, it was too easy, somehow."
mi "บิงโก~! ใช่แล้วละ! แต่~ เหมือนง่ายไปยังไงไม่รู้"

# "I don't know what she means by “somehow.”"
"ไม่เข้าใจว่า “ยังไงไม่รู้” ที่ว่านั่นคืออะไร"

show misha hips_frown_cas
with charachange

# mi "Too many people can tell it's me! I want to surprise someone! I thought for sure that Hideaki would be fooled~. Why weren't you, hm~?"
mi "มีคนทายว่าเป็นฉันถูกหลายคนเกินไปแล้ว! ฉันอยากจะเซอร์ไพรส์สักคน! อุตส่าห์คิดแล้วว่าต้องหลอกฮิเดอากิได้แน่~\nทำไมถึงหลอกไม่ได้นะ~"

show hideaki bored
with charachange

# hh "You are the only person who does that. You, and kidnappers."
hh "มีพี่คนเดียวที่เล่นแบบนี้ มีพี่ แล้วก็แก๊งลักพาตัว"

show misha cross_laugh_cas
with charachange

# mi "Really? Wahaha~!"
mi "จริงเหรอ วะฮ่าฮ่า~!"

show hideaki serious
with charachange

# hh "Why do you laugh?"
hh "หัวเราะอะไรครับ"

show shizu invis:
    center
    xpos 0.1
with None

show bg shizu_park at left
show misha cross_laugh_cas at Position(xpos=0.4)
show hideaki serious at Position(xpos=0.8)
show shizu basic_angry_cas at Position(xpos=0.2)
with dissolvecharamove

# ssh "Are you giving Hisao trouble? I thought you would take him somewhere more exciting than the park. It isn't even that far from home. You are so lazy."
ssh "นี่ทำฮิซาโอะเขาปวดหัวหรือเปล่า นึกว่าจะพาไปที่ที่ชวนให้ตื่นเต้นกว่าสวนสาธารณะหน่อย แถมที่นี่ก็อยู่ใกล้บ้าน\nนิดเดียวเอง ขี้เกียจจริงเลยนะ"

show misha hips_frown_cas
with charachange

# mi "Hideaki, are you giving Hicchan trouble? You should have taken him somewhere more exciting! The park is too close to home, Shicchan says you're lazy~."
mi "ฮิเดอากิ นายทำฮิซาโอะเขาปวดหัวหรือเปล่า พาไปที่ที่ชวนให้ตื่นเต้นกว่านี้หน่อยสิ! สวนสาธารณะมันใกล้บ้านเกินไป\nชิจังบอกว่านายขี้เกียจละ~"

show hideaki bored
with charachange

# hh "He wanted to come here. Why are you so argumentative?"
hh "พี่ฮิซาโอะเขาอยากมาที่นี่ ทำไมพี่ถึงว่ากันอย่างนี้"

show shizu behind_frown_cas
with charachange

# ssh "I have to keep my little brother in line."
ssh "ฉันต้องคอยดูความประพฤติของน้องชายตัวเอง"

show hideaki triangle
with charachange

# hh "What is she saying?"
hh "พี่ชิซูเนะว่ายังไงนะครับ"

# hi "You must be kept in line."
hi "ชิซูเนะต้องคอยดูความประพฤติของนาย"

show hideaki serious
with charachange

# hh "Really…"
hh "จริงเล้ย…"

# "They're ready to go at each others' throats this quickly. On one hand, I've heard that siblings fighting so much isn't uncommon, and the fact that they fight at all proves there has to be some level of communication going on. So, it's nice they get along."
"มาถึงก็จะกัดกันซะแล้ว แต่ก็พอได้ยินมาอยู่บ้างว่าพี่น้องตีกันมันเรื่องปกติ แล้วถ้าทะเลาะกันได้ก็แปลว่าต้องสื่อสาร\nกันบ้างแหละ เข้ากันได้อย่างนี้ก็ดีแล้ว"

scene bg shizu_houseext
with locationskip

stop music fadeout 4.0

# "They argue all the way back home. Misha translates for Shizune, and I for Hideaki. So it looks more like we're the ones arguing instead, except not really. Nobody could listen to Misha and believe that."
"ทั้งคู่เถียงกันไม่หยุดหย่อนไปตลอดทาง มิช่าแปลให้ชิซูเนะ ส่วนฉันก็แปลให้ฮิเดอากิ เลยดูเหมือนว่าเราสองคนทะเลาะ\nกันแทน ซึ่งก็ไม่ค่อยเหมือนเท่าไหร่ ถ้าใครได้ยินมิช่าพูดก็คงไม่เชื่อเหมือนกัน"

# "The day got entertaining in the end, at least."
"อย่างน้อยวันนี้ก็สนุกขึ้นมาละนะ"

$ suppress_window_after_timeskip = True

scene black
with dissolve

###########################

label th_S20:

window hide None

scene black
with dissolve

show bg shizu_guesthisao
with openeye

window show

# "Despite having only been here for two days, it feels like it's been much longer. I wake up feeling more tired than refreshed. Maybe because I've been moving around almost constantly since I got here."
"ทั้งที่เพิ่งมาได้สองวัน แต่รู้สึกเหมือนนานกว่านั้นอีก ตื่นมาก็รู้สึกเพลียแทนที่จะสดชื่น คงเพราะตั้งแต่มาที่นี่แทบไม่ได้\nพักอยู่กับที่สักครั้งเลย"

# "Whatever the reason, it's making me get up unusually late each day. I like sleeping in, but it could be inconvenient if it ends up becoming a habit."
"และไม่ว่าจะด้วยเหตุอันใด ฉันได้ตื่นสายกว่าปกติทุกวัน ฉันชอบนอนต่อนาน ๆ ก็จริง แต่ขืนทำจนติดเป็นนิสัย\nคงลำบากแน่"

# "I can hear a deep, male voice shouting loudly in the background. It must be Shizune's dad. Or maybe, with the size of this place, it's creditors. More likely the former, since the yelling doesn't seem angry, just loud."
"เหมือนได้ยินเสียงผู้ชายทุ้ม ๆ มาแว่ว ๆ ต้องเป็นพ่อชิซูเนะแน่ ๆ หรือไม่ก็เป็นเจ้าหนี้มั้ง ดูจากสภาพบ้านที่ใหญ่ขนาดนี้\nซึ่งน่าจะเป็นอย่างแรกมากกว่า เพราะเสียงตะโกนที่ว่าไม่ได้มีความโกรธมาด้วย แค่เสียงดังเฉย ๆ"

scene bg shizu_living
show hideaki normal:
    center
    xpos 0.5
show misha perky_smile_cas:
    center
    xpos 0.3
show shizu basic_normal_cas:
    center
    xpos 0.08
show jigoro smug:
    center
    xpos 0.87
with charaenter

play music music_another fadein 0.5

# "Shizune, Misha, and Hideaki are sitting in the living room, having a one-sided conversation with a giant bear-man who alternates between shoveling away food from a plate balanced on his leg and twirling a sword."
"ชิซูเนะ มิช่า และฮิเดอากินั่งอยู่ในห้องนั่งเล่นฟังชายตัวโตคนหนึ่งที่ตักข้าวกินจากจานที่ตั้งอยู่บนขาพลางควงดาบ\nไปด้วยพล่ามอยู่"

# "From what Shizune and Hideaki are like, I'd expected their dad to be a very reserved, clean-cut, possibly androgynous person, so I'm pretty surprised. I'm surprised for a while, until he starts talking to me."
"ดูจากท่าทางของชิซูเนะกับฮิเดอากิแล้วฉันก็คิดภาพไว้ว่าพ่อสองคนนี้คงจะเป็นคนเนี้ยบนิ้งรักษากิริยามารยาท\nอาจจะไม่ได้ดูเป็นลูกผู้ชายจ๋าขนาดนั้นด้วยซ้ำ ฉันเลยค่อนข้างแปลกใจที่ได้เห็นอย่างนี้ ฉันแปลกใจอยู่สักพัก\nจนเขาหันมาคุยกับฉัน"

show jigoro laugh
with charachange

# hx_ "Hello! You must be Shizune's other friend. Did you have a good night's rest? The guest rooms are a bit sparse, if there is anything you need, feel free to tell me."
hx_ "สวัสดี! เธอคงเป็นเพื่อนชิซูเนะอีกคนสินะ เมื่อคืนหลับสบายดีมั้ย ห้องนอนแขกค่อนข้างกว้าง ถ้าขาดเหลืออะไร\nก็บอกได้ไม่ต้องเกรงใจนะ"

# hi "Thanks. You must be Shizune's father. It's nice to meet you. I'm Shizune's classmate, Hisao Nakai."
hi "ขอบคุณครับ คุณคงเป็นพ่อของชิซูเนะสินะครับ ยินดีที่ได้รู้จักนะครับ ผมเพื่อนร่วมชั้นชิซูเนะ ชื่อฮิซาโอะ นากาอิครับ"

show jigoro neutral
with charachange

# hx_ "The pleasure is mine. I've wanted to meet you, after hearing that I would have a second guest in my house. Unexpected. You hear something like that, and obviously you want to see what that person is like. Would you like my business card?"
hx_ "ด้วยความยินดี พอได้ยินว่าบ้านฉันจะมีแขกอีกคนแล้วฉันก็อยากเจอเธอเหมือนกัน ไม่คาดฝันเลย ได้ยินอะไร\nอย่างนั้นแล้วก็ย่อมอยากเห็นหน้าค่าตาอยู่แล้วใช่มั้ย รับนามบัตรของฉันไว้ก่อนมั้ย"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

show jigorocard:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

# "He holds up a case full of them for a second and I can see that his name is Jigoro and that his office hours are from eight to six. They also say that he's a “consultant”. What a prepared guy, carrying his card case around in his own home."
"เขายื่นตลับที่มีนามบัตรตั้งกองอยู่ข้างใน แวบหนึ่งฉันเห็นในนามบัตรว่าเขาชื่อจิโกโร เข้างานแปดโมงเช้าถึงหกโมงเย็น\nทั้งมีเขียนไว้ว่าเป็น “ที่ปรึกษา” เตรียมพร้อมดีจริง ๆ ทั้งที่อยู่ในบ้านก็ยังพกตลับนามบัตรไว้ติดตัว"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

show jigorocard:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide jigorocard
with None

show jigoro smug
with charachange

# hx "We're just sitting down to a slightly late lunch, you're just in time to join us. Good. Pick a place to sit down and I'll bring you a plate. I hope you don't mind eating bear liver."
hx "พวกเราเพิ่งมานั่งกินข้าวเที่ยงที่เลยเที่ยงมานิดหน่อย เธอมาได้จังหวะพอดี ดี เลือกที่นั่งได้เลยนะ เดี๋ยวฉันไปเอาจาน\nมาให้ เธอกินตับหมีได้ใช่มั้ย"

# "I thought that bear liver was toxic. Either way, the thought of eating a bear liver doesn't appeal to me other than for the ability to tell people I've eaten bear liver. I suppose it wouldn't hurt to try it. But Shizune's dad merely laughs."
"ไม่ใช่ว่าตับหมีมันเป็นพิษเหรอ แต่กินได้ไม่ได้ฉันก็ไม่เห็นว่ากินแล้วจะได้อะไรขึ้นมา นอกจากว่าจะเอาไปเล่ากับคนอื่น\nว่าตัวเองเคยกินตับหมีแล้ว ลองหน่อยคงไม่เสียหายมั้ง แต่พ่อของชิซูเนะก็หัวเราะขึ้นมา"

show jigoro laugh
with charachange

# hx "I'm just making a joke. Although, maybe it wouldn't be such a bad idea to cook up some bear livers for you kids. They will make you strong."
hx "แค่ล้อเล่นหรอก แต่ถ้าได้ตับหมีมาทำกับข้าวให้พวกเธอกินก็คงดีเหมือนกันนะ กินแล้วจะได้แข็งแรง"

show jigoro neutral
with charachange

# hx "We're actually having omelettes. I'll make you one right now. Is that unusual for you, having an omelette for lunch?"
hx "จริง ๆ จะกินไข่ทอดกัน เดี๋ยวไปทำให้ แปลกมากมั้ย เธอเคยกินไข่ทอดเป็นข้าวเที่ยงหรือเปล่า"

show hideaki triangle
with charachange

# hh "Very unusual."
hh "แปลกมากครับ"

# hi "No, not at all."
hi "ไม่ ไม่เลยครับ"

hide jigoro
with charaexit

# "Jigoro vanishes to where the kitchen must be. I'm surprised that despite living in this place, he has to cook my lunch. Maybe he only cooks because he likes to."
"จิโกโรแวบหายไปทางที่น่าจะพาไปยังห้องครัว ฉันนึกแปลกใจที่เขามาทำข้าวเที่ยงให้ฉันทั้ง ๆ ที่บ้านออกจะหรูขนาดนี้\nอาจจะทำกับข้าวเพราะอยากทำมั้ง"

show jigoro smug:
    center
    xpos 0.87
with shorttimeskip

# "My steaming plate of food is done in a very short time. It smells really good."
"กับข้าวที่ควันหอมฉุยลอยโขมงนั้นมาถึงในไม่กี่อึดใจ"

# hx "Are you in the Student Council, like Shizune? Is the Student Council that busy, that Shizune has to drag her friends along with her everywhere she goes?"
hx "เธอเป็นสภานักเรียนเหมือนชิซูเนะหรือเปล่า สภานักเรียนงานเยอะถึงขั้นต้องลากเพื่อนติดตัวไปทุกที่ด้วยเลยเหรอ"


show shizu behind_blank_cas at Position(xpos=0.12)
with charachange

# ssh "Sometimes a vacation is just a vacation."
ssh "เที่ยวก็คือเที่ยวมั้ยล่ะคะ"

# hi "You're right about the student council part. I think we're just here for fun, though."
hi "ครับ ผมเป็นสภานักเรียน แต่ที่พวกเรามาที่นี่ก็มาเที่ยวเฉย ๆ แหละครับ"

show jigoro neutral
with charachange

# hx "I see. Is that right? When I was young, our student councils had so much work that I don't think we could have afforded going on vacation. It must be nice, having so much free time. Should give you plenty of time to think about your future."
hx "อย่างนี้นี่เอง งั้นเหรอ ตอนฉันเด็ก ๆ สภานักเรียนโรงเรียนฉันงานเยอะมาก คงไม่มีเวลาว่างมาเที่ยวได้หรอก มีเวลาว่าง\nเยอะอย่างนี้คงดีแน่ ๆ จะได้มีเวลามาคิดถึงเรื่องอนาคตตัวเองเยอะ ๆ ด้วย"

# "I do not like the direction this discussion is taking, and start thinking about how to avoid it."
"รู้สึกลางไม่ดีขึ้นมาแล้ว ฉันเริ่มคิดว่าจะเบี่ยงประเด็นไปยังไงดี"

# hx "Have you thought about that? About what you want to do?"
hx "เคยคิดบ้างมั้ย สิ่งที่ตัวเองอยากทำน่ะ"

# hi "No, I haven't given it much thought recently. What do you do, if you don't mind me asking? It must be something pretty cool, if it can get you a house like this."
hi "ไม่หรอกครับ ช่วงนี้ผมไม่ได้คิดมากเรื่องนั้นเท่าไหร่ จะว่าไป ผมถามหน่อยได้มั้ยครับว่าคุณทำงานอะไรอยู่ งานคงดี\nแน่ ๆ เลยถึงได้ซื้อบ้านอย่างนี้ได้"

show jigoro angry
with charachange

# hx "Why do you want to know that? Children aren't interested in business. What business of yours is my business? Suspicious. Are you some kinda tax man, boy?"
hx "เธอจะอยากรู้ไปทำไม เด็กน่ะไม่สนเรื่องอะไรอย่างนี้หรอก เรื่องอะไรเธอจะต้องรู้เรื่องของฉัน น่าสงสัย\nเป็นสรรพากรหรือเปล่าหนุ่ม"

# "I guess he really does not like being asked questions."
"คงไม่ชอบให้ใครถามอะไรจริง ๆ แหละนะ"

show misha hips_grin_cas
with charachange

# mi "Hicchan isn't a tax collector's boy, I think~. Hicchan, what do your parents do? You never told us~!"
mi "ฮิจังคงไม่ใช่สรรพากรหนุ่มหรอกนะคะ~ ฮิจัง พ่อแม่นายทำงานอะไรเหรอ นายไม่เคยบอกเราเลย~!"

# hx "You, be quiet. Don't interrupt me. I hate being interrupted. Rude."
hx "เธอ เงียบไปเลย อย่าขัด ฉันไม่ชอบให้ใครมาขัด หยาบคาย"

show misha perky_sad_cas
with charachange

# mi "Aah~…"
mi "แง~…"

show shizu basic_normal2_cas at Position(xpos=0.08)
with charachange

# "Shizune doesn't look too happy with this turn of events. Even with Misha unable to sign to her what's going on, she can read the mood easily. Her glare becomes more smoldering as Jigoro continues to rant."
"ชิซูเนะดูจะไม่พอใจเท่าไหร่ที่เรื่องเป็นอย่างนี้ แม้มิช่าจะแปลบทสนทนาเป็นภาษามือให้ไม่ได้ แต่เธอก็ดูอารมณ์ออก\nได้อย่างง่ายดาย ยิ่งจิโกโรพูดพล่ามนานเรื่อย ๆ สายตาเธอเริ่มมีควันคุกรุ่นขึ้นมา"

# hx "One more thing. My fishing equipment. I came home and it was just in a big pile in the corner. Rods just stacked haphazardly on top of tackle."
hx "แล้วอีกอย่าง อุปกรณ์ตกปลาของฉันน่ะ ฉันกลับมาบ้านก็เห็นกองสุมกันอยู่ลวก ๆ อย่างนั้น คันเบ็ดก็ซ้อนเกลื่อน\nบนกองนั้นอีก"

show hideaki thinking
with charachange

# hh "That was me."
hh "ผมเองครับ"

# "I can't remember if it actually was him. If it wasn't, I appreciate that he's willing to take one for the team. It doesn't matter because Jigoro ignores him without skipping a beat."
"ฉันจำไม่ได้แน่ว่าเป็นเขาจริงหรือเปล่า ถ้าไม่ใช่ฉันก็อยากขอบคุณที่อุตส่าห์ออกหน้าแทนคนอื่น ซึ่งเปล่าประโยชน์\nเพราะจิโกโรเมินฮิเดอากิไปแล้วพูดต่ออีก"

show jigoro smug
with charachange

# hx "Well, anyway, I'm glad that my fishing equipment could provide so much entertainment for my daughter's friends. Did not even tell me you were going to be using them. Those are expensive, custom-made poles. Not for dilettantes."
hx "แต่เอาเถอะ ฉันก็ดีใจนะที่อุปกรณ์ตกปลาของฉันทำให้เพื่อนของลูกสาวฉันสนุกกันได้ขนาดนี้ เอาไปใช้ไม่เห็น\nบอกกล่าวกันเลย แพงนะไอ้พวกคันเบ็ดสั่งทำเนี่ย ไม่ใช่ของสำหรับคนที่จะมาตกปลาเล่น ๆ กัน"

# "I suddenly become aware of the eggshell fragments in my omelette. Is he just a bad cook? Does he eat them for the calcium? Were they purposely added there to give me even more discomfort?"
"อยู่ ๆ ฉันก็เคี้ยวโดนเศษเปลือกไข่ที่อยู่ในไข่ทอด นี่ฝีมือทำกับข้าวห่วยจริงหรือใส่มาเพื่อเสริมแคลเซียม หรือจงใจใส่มา\nให้ฉันรู้สึกไม่ดีหนักกว่าเดิมกันแน่"

# "Though confused, I'm not as unnerved as I think I would normally be. Then again, my life has been pretty strange lately, and I keep running into all sorts of different people. Nothing surprises me any more."
"ถึงจะงง ๆ แต่ฉันก็ไม่ได้ลนลานอย่างเมื่อก่อนแล้ว แต่ก็นะ ช่วงนี้ชีวิตฉันก็แปลก ๆ เจอคนมากหน้าหลายตา\nหลากประเภท ฉันคงไม่แปลกใจกับอะไรแล้ว"

show jigoro angry
with charachange

# hx "Didn't even properly clean them after use. Terrible."
hx "ใช้เสร็จแล้วไม่ทำความสะอาดให้ดีอีก แย่จริง ๆ"

# hx "Do you even know how to fish? Unlikely. There are not enough poles here for all of you. How does that work? Did you all share? One person baits the hook, and another casts? Two people to reel? Incompetent."
hx "ตกปลาเป็นหรือเปล่าเถอะ ไม่น่านะ แล้วคันเบ็ดก็มีไม่พอกับพวกเธอทุกคนด้วย ทำยังไงกัน แบ่งกันตก คนหนึ่ง\nเอาเหยื่อเกี่ยวเบ็ด อีกคนเหวี่ยงคันเบ็ด แล้วอีกสองคนเย่อปลาเหรอ โหลยโท่ยจริง ๆ"

# hi "Well, six of us went, so we couldn't all do it at the same time. First it was just me, Akira, Hideaki, and Misha."
hi "เอ่อ พอดีไปกันหกคนครับ เลยตกพร้อมกันไม่ได้ คนที่ได้ตกรอบแรกมีผม อากิระ ฮิเดอากิ แล้วก็มิช่า"

# hx "Stop talking. That sounds unspeakably dirty. I have had enough of your filth. How vulgar. Make sure that your statements are not so embarrassingly, carelessly worded next time."
hx "หยุดพูดไปเลย ฟังดูสกปรกเหลือเกินนะ แค่พวกเธอก็สกปรกพอแล้ว หยาบคายเสียจริง คราวหน้าคราวหลังจะพูดอะไร\nก็ระวังอย่าพูดพล่อย ๆ ลอย ๆ แล้วกัน"

# hi "What…?"
hi "ฮะ…?"

# hx "“What?” You are so disrespectful. Amazing. Are all delinquent types like this? Even the way you dress shows flippant disregard for authority. Sweater vest. Disgraceful…"
hx "“ฮะ”? ไม่มีมารยาทเลยนะ สุดยอด พวกเกเรเป็นอย่างนี้กันหมดเลยหรือไง เสื้อผ้าที่เธอใส่ยังไม่มีความเคารพ\nผู้หลักผู้ใหญ่เลย เสื้อกั๊กไหมพรมเนี่ยนะ อุจาดตาเสียจริง…"

# hi "Delinquent? I'm on the Student Council."
hi "เกเรเหรอครับ แต่ผมเป็นสภานักเรียนนะ"

# "I'm hurt by his comment on my sweater vest, especially when it's coming from a guy in such a tacky shirt. I guess I can't really say anything, though. He has a sword. He might also kill bears."
"ฉันเจ็บจี๊ดที่เขาพูดถึงเสื้อกั๊กไหมพรมของฉันอย่างนั้น เสื้อที่คนพูดใส่ก็เห่ยเถอะ แต่คงพูดอะไรไม่ได้อะนะ อีกคน\nมีดาบอยู่ เผลอ ๆ ใช้ฆ่าหมีด้วย"

stop music fadeout 0.3
play sound sfx_impact
with vpunch

# "Misha loudly puts her plate down on the table."
"มิช่ากระแทกจานเข้ากับโต๊ะดังปัง"

show misha hips_smile_cas
with charachange

# mi "That was delicious~! Shicchan and I are done now. Hicchan, you are too, right~? We should get going!"
mi "อร่อยมากเลย~! ชิจังกับหนูอิ่มแล้ว ฮิจัง นายก็อิ่มแล้วด้วยใช่มั้ย~ ไปกันดีกว่า!"

# "What a simple, yet effective exit strategy."
"เป็นกลยุทธ์เอาตัวรอดที่เรียบง่ายแต่ได้ผลดีจริง ๆ"

scene bg shizu_houseext
with locationchange

# "I barely have the time to put down my plate before they pull me up and out of there, and finally outside."
"ยังไม่ทันจัดแจงจานตัวเองดีฉันก็ถูกลากออกมาข้างนอกแล้ว"

show shizu behind_frustrated_cas at tworight
show misha perky_confused_cas at twoleft
with charaenter

shi "…"

show misha sign_confused_cas
with charachange

# mi "Unbelievable~! It's like I'm really watching an interrogation~! This is not a cop show! Guests definitely have responsibilities, but hasn't he ever heard of being a gracious host~? Really~!"
mi "ไม่อยากจะเชื่อเลย~! เหมือนมานั่งดูตำรวจซักผู้ร้ายเลย~! ทำเป็นละครสืบสวนไปได้! แขกก็มีหน้าที่ที่ต้องทำ\nจริงแหละ แต่ไม่เคยได้ยินเรื่องการเป็นเจ้าบ้านที่ดีหรือไง~ จริง ๆ เลย~!"

# "Misha attempts to sloppily mimic Shizune's angry, chopping gestures as best as she can. She has the expression down too, but the tone of her voice is the same as ever, thus lacking the anger necessary to bring it all together."
"มิช่าพยายามล้อท่าทางฟึดฟัดของชิซูเนะให้ใกล้เคียงที่สุด แม้แต่สีหน้าก็ยังคล้าย แต่น้ำเสียงเธอยังเป็นเช่นเคย\nคำพูดนั้นจึงยังดูโกรธไม่พอกับต้นทางเท่าไหร่"

show misha hips_smile_cas
with charachange

# mi "Wahaha~. Don't take it too hard, Hicchan~! Shicchan's dad does this to everyone, I think it's like a joke~."
mi "วะฮ่าฮ่า~ อย่าเครียดไปเลยฮิจัง~! พ่อชิจังก็เป็นงี้กับทุกคนแหละ ฉันว่าน่าจะเหมือนหยอกเฉย ๆ นะ~"

# hi "That was the most aggressive joke possible."
hi "ช่างเป็นการหยอกที่รุนแรงสุด ๆ ไปเลยนะ"

# "I'm also not at all convinced that it was a joke, considering this hastily staged retreat, but this isn't a good moment to discuss how Shizune's father might be a jerk."
"ฉันก็ไม่ค่อยเชื่อเท่าไหร่ว่าเมื่อกี้คือหยอก ดูจากการที่ต้องจัดฉากถอยทัพมาอย่างนี้ แต่ตอนนี้ก็ไม่ใช่เวลาจะมาคุย\nเรื่องนิสัยของพ่อชิซูเนะที่ใช้ไม่ได้"

play music music_shizune fadein 4.0

show misha sign_smile_cas
with charachange

# mi "Hicchan, let's go shopping!"
mi "ฮิจัง ไปซื้อของกันเถอะ!"

show shizu adjust_happy_cas
with charachange

# ssh "You haven't been to town yet, have you? It'll be fun. We can see the sights, and go to an amusement park, maybe eat at a good restaurant."
ssh "นายยังไม่เคยมาตัวเมืองเลยใช่มั้ย ต้องสนุกแน่ อาจจะไปดูวิว ไปสวนสนุก หรือไม่ก็ไปกินข้าวที่ร้านอาหารดี ๆ สักที่"

# hi "We just had lunch."
hi "เราเพิ่งกินข้าวเที่ยงไปนะ"

# "Even though I didn't eat much."
"ถึงฉันจะกินไปไม่เยอะก็เถอะ"

show shizu behind_smile_cas
with charachange

# ssh "It's okay, in that case, we just have to make sure that today is so busy that by the time we're done, it will be time for dinner."
ssh "ไม่เป็นไรหรอก ถ้างั้นก็แค่หาอะไรทำข้างนอกให้หมดวัน เอาให้พอกลับถึงบ้านแล้วได้กินข้าวเย็นพอดีเลย"

show misha cross_grin_cas
with charachange

# mi "It works out perfectly~! Come on, Hicchan~!"
mi "ลงตัวมาก ๆ เลย~! เถอะน่า ฮิจัง~!"

show shizu behind_smile_cas_close at closeright
show misha cross_smile_cas_close at closeleft
with characlose

# "They immediately flank me and hook my arms with theirs, Shizune taking one arm and Misha taking the other. At first, we almost trip over each other. Shizune walks at a very brisk pace, and Misha has an unusually bouncy way of moving around."
"ทั้งมิช่าและชิซูเนะเข้าประกบควงแขนฉันไว้ข้างละคน ตอนแรกแทบจะสะดุดขากันล้มแล้ว ชิซูเนะเดินเร็วมาก ส่วนมิช่า\nก็เดินโดดไปมาแบบพิลึก ๆ"

scene bg shizu_park
with locationchange

# "We get the hang of it soon enough, and I notice we're going to town by cutting through the park. It doesn't seem efficient, so I'm guessing this is the scenic route."
"ไม่นานพวกเราก็เดินจนจังหวะลงตัว เหมือนจะได้เข้าตัวเมืองด้วยการเดินลัดสวนสาธารณะไป ซึ่งดูไม่ใช่ทางที่เร็ว\nสักเท่าไหร่ คงหวังมาเดินกินลมชมวิวมั้ง"

# "Walking this way hinders how we can communicate with each other significantly. I can't talk to Shizune at all. Shizune and Misha are down to one handed gestures only. It feels nice, though, so I don't mind too much."
"พอมาเดินอย่างนี้แล้วพวกเราก็สื่อสารกันแทบไม่ได้ ฉันคุยกับชิซูเนะไม่ได้เลย ส่วนชิซูเนะและมิช่าก็สื่อสารกันด้วย\nมือข้างเดียว แต่ก็รู้สึกดีเหมือนกัน ฉันจึงไม่ถืออะไรมากมาย"

# "When I make a crack about it to Misha, she responds with mild confusion."
"พอฉันบ่นเรื่องนี้ให้มิช่าฟังเธอก็ตอบมาด้วยความสับสนเล็กน้อย"

show misha perky_confused_cas_close at closeleft
with charaenter

# mi "Really, Hicchan~? Hm… If you really want Shicchan's attention, you can tell me, and then I can tap her on the shoulder for you."
mi "จริงเหรอฮิจัง~ อืม… ถ้าอยากให้ชิจังสนใจนายจริง ๆ ก็บอกฉันได้นะ เดี๋ยวฉันสะกิดไหล่ชิจังให้"

# hi "You could just let me go and I'll do it myself. How are you going to tap her on the shoulder from over there?"
hi "ปล่อยให้ฉันทำเองก็ได้มั้ง เธออยู่ฝั่งนั้นแล้วจะสะกิดไหล่ยังไง"

show misha hips_grin_cas_close
with charachange

# mi "Like this~!"
mi "แบบนี้~!"

with vpunch

show shizu behind_frustrated_cas_close behind misha at closeright
with charachange

# "She suddenly stops in her tracks roughly, and tries to reach behind her back and across my shoulders to get Shizune's attention. She succeeds, but only because when Misha stopped, I had to as well or we'd all fall over."
"จู่ ๆ เธอก็หยุดเดินแบบชะงักกึกแล้วเอื้อมแขนข้ามหลังฉันไปทางชิซูเนะให้เธอหันมาสนใจ ซึ่งได้ผล แต่เป็นเพราะฉัน\nต้องหยุดตามเธอไปด้วยต่างหาก ไม่งั้นได้สะดุดล้มทั้งแผงแน่"

show misha hips_laugh_cas_close
with charachange

show shizu adjust_blush_cas_close
with charachange

# "Obviously, Shizune had to jerk to a halt too. The sight makes Misha let out one of her characteristic laughs, which shakes us around more, and Shizune starts flailing her free hand to get her to stop, which only causes her to laugh harder."
"แน่นอนว่าชิซูเนะต้องชะงักไปอีกคนด้วย มิช่าหัวเราะด้วยเสียงอันเป็นเอกลักษณ์เฉพาะตัวของเธอที่ได้เห็นสภาพ\nพวกเราที่เป็นอย่างนี้ ซึ่งทำให้พวกเราโงนเงนหนักกว่าเก่าอีก ชิซูเนะใช้มืออีกข้างที่ว่างอยู่รีบส่งสัญญาณให้มิช่าหยุด\nแต่ยิ่งทำให้มิช่าหัวเราะดังกว่าเดิม"

# "It is pretty funny to watch her getting so flustered, and I start laughing too."
"เห็นชิซูเนะลนลานแล้วก็ตลกดี ฉันจึงผสมโรงขำไปด้วย"

stop music fadeout 2.0

scene black
with dissolve

###############################

label th_S21:

scene bg shizu_guesthisao
with locationchange

play music music_dreamy fadein 2.0

# "I've been neglecting my sign language studies, so I should probably spend some time studying up on it. Although, I think I've learned a lot just by osmosis. I'm very proud of that, and will have to be careful not to brag about it."
"ฉันทิ้งเรื่องเรียนภาษามือมาสักพักแล้ว หาเวลาเรียนสักหน่อยดีกว่า ถึงเหมือนจะเรียนรู้ผ่านการซึมซับมาเยอะแล้ว\nก็เถอะ แล้วก็ต้องคอยถ่อมตัวเอาไว้ห้ามอวดด้วย"

# "Most of the books I brought with me aren't manuals on learning sign language, but studies about different signing “dialects.” I know Shizune has some secret signals with Misha that only the two of them know the meaning of."
"หนังสือที่ฉันพกมาด้วยส่วนใหญ่ไม่ใช่คู่มือภาษามือ แต่เป็นหนังสือเรื่อง “ภาษาถิ่น” ของภาษามือแบบต่าง ๆ ฉันรู้\nว่าชิซูเนะกับมิช่ามีภาษาลับที่ใช้สื่อสารกันแค่สองคนอยู่"

# "After seeing a couple of them, this book caught my eye in the school library."
"พอเห็นสองคนนั้นแล้วหนังสือเล่มนี้ที่อยู่ในห้องสมุดก็สะดุดตาขึ้นมา"

# "Maybe I should incorporate some examples into my own signing, to mess with them, because I'm pretty sure that they have started using their code words more when I started learning sign language. That will teach them."
"น่าจะเอาไปใช้กับภาษามือของฉันเอาไว้แกล้งสองคนนั้นเล่นบ้าง เพราะฉันแน่ใจทีเดียวว่าพวกเธอใช้รหัสลับกัน\nมากกว่าเดิมตอนที่ฉันเริ่มเรียนภาษามือ เผื่อจะได้รู้สึกบ้าง"

# "After a quick break for a shower, I resume practicing my signing in the guest room mirror. Yesterday, I crashed my fingers against each other pretty hard. It still smarts, and I don't want a repeat of that to happen again."
"หลังจากที่อาบน้ำอยู่ไม่นานฉันก็กลับมาฝึกภาษามือกับกระจกในห้องนอนแขกต่อ เมื่อวานทำนิ้วตัวเองชนกันแรง\nจนเจ็บมาถึงตอนนี้ ต้องระวังไม่ให้เป็นอย่างนั้นอีก"

play sound sfx_doorknock2

show hideaki normal at center
with charaenter

# "I hear knocking on the door behind me and turn to find Hideaki standing inside the doorway, staring at me. How polite of him to knock, but usually you don't open the door first."
"ฉันหันไปมองเมื่อได้ยินเสียงเคาะประตูจากข้างหลัง ฮิเดอากิยืนจ้องฉันอยู่ตรงประตู มีมารยาทดีที่เคาะ แต่ปกติต้องรอ\nให้คนตอบก่อนค่อยเปิดประตูไม่ใช่เหรอ"

show hideaki triangle
with charachange

# hh "What are you doing?"
hh "ทำอะไรอยู่เหรอครับ"

# hi "I'm practicing sign language. How long have you been standing there?"
hi "ฝึกภาษามืออยู่ มายืนตรงนั้นตั้งแต่ตอนไหนแล้ว"

show hideaki thinking
with charachange

# hh "I did not see anything."
hh "ผมไม่เห็นอะไรทั้งนั้น"

# "That isn't the point. I don't even know what he means by that. It's not like I was doing something that I would be ashamed to have people see me doing."
"ไม่ใช่ประเด็นสักหน่อย หมายความว่ายังไงเนี่ย ใช่ว่าฉันทำอะไรน่าอายจนไม่อยากให้คนมาเห็นสักหน่อย"

# "Although, sign language must look strange to most people. I'm only used to it from being around Shizune and Misha so much."
"แต่ก็นะ ภาษามือคงดูแปลกกับคนส่วนใหญ่แหละ ที่ฉันชินก็เพราะอยู่กับชิซูเนะกับมิช่าบ่อย ๆ เท่านั้นเอง"

# hi "I'm brushing up on my sign language, and reading about it too. Stuff like the history of it, even though they cover it in sign language class."
hi "ฉันรื้อฟื้นทักษะภาษามือตัวเองอยู่ แล้วก็อ่านเรื่องภาษามือด้วย อย่างพวกความเป็นมา ถึงจะเคยเรียนตอนเรียน\nภาษามือในห้องแล้วก็เถอะ"

show hideaki normal
with charachange

# hh "Your school teaches sign language as a class?"
hh "ที่โรงเรียนพี่สอนภาษามือด้วยเหรอครับ"

# hi "Yeah. One of the first things they brought up was that it's not very common to do that. I guess we're very international, or something."
hi "อื้ม ตอนไปเรียนแรก ๆ เขาก็บอกอยู่ว่าไม่ค่อยมีโรงเรียนที่ไหนสอนภาษามือหรอก สงสัยโรงเรียนฉันจะมีความ\nเป็นสากลมาก ๆ เลยละมั้ง"

show hideaki serious
with charachange

# hh "It looks fun."
hh "ดูสนุกนะครับ"

# hi "Well, I wouldn't call it fun."
hi "ก็ ไม่เชิงสนุกหรอก"

show hideaki bored
with charachange

# hh "If you do not enjoy this, it seems like a lot of work to go through just to talk to my sister."
hh "ถ้าไม่สนุกก็คงน่าเบื่อแย่ที่ต้องลงทุนขนาดนี้เพื่อคุยกับพี่ชิซูเนะ"

# hi "Why does everyone keep saying that?"
hi "ทำไมถึงมีแต่คนพูดอย่างนั้น"

show hideaki happy
with charachange

# "Hideaki's mouth twitches like he was about to laugh, but he restrains himself. Come to think of it, he hasn't laughed once since I've met him. I could take it as a compliment that he doesn't laugh at me, but I'm curious to see it."
"ปากของฮิเดอากิขยับเหมือนจะหัวเราะ แต่เขาก็กลั้นไว้ จะว่าไป ตั้งแต่เจอมายังไม่เคยเห็นหัวเราะเลย ก็นับว่าเป็นเรื่องดี\nแหละมั้งที่ไม่หัวเราะใส่กัน แต่อยากเห็นแฮะ"

# hi "Laugh."
hi "หัวเราะซิ"

show hideaki thinking
with charachange

stop music fadeout 4.0

hh "…"

show hideaki bored
with charachange

# hh "Why?"
hh "ทำไม"

# "It was the fastest and most direct way I could think of towards accomplishing my goal."
"ก็เพราะเป็นวิธีที่เร็วที่สุดและตรงที่สุดที่จะได้เห็นนายหัวเราะไง"
#Hisao is mentally shrugging. Does it make sense now? Would you like a "I shrug." actually added to the beginning of the line? -SC

show hideaki normal_up
with charachange

# hh "Can you teach me sign language?"
hh "สอนภาษามือให้หน่อยได้มั้ยครับ"

# "He says it plainly, but his body language is nervous, showing that he clearly needs to put some effort in to ask. I guess Hideaki likes his sister after all. I'd think Misha is a lot more approachable though, so I wonder why he didn't ask her."
"เขาพูดเสียงเรียบ แต่ดูท่าทางแล้วเหมือนตื่นเต้นอยู่ แปลว่ากว่าจะกล้าถามได้ก็ลำบากเหมือนกัน ฮิเดอากิคงชอบ\nพี่ตัวเองแหละนะ แต่ไม่รู้ทำไมถึงไม่ไปขอมิช่าที่น่าจะดูคุยด้วยง่ายกว่าแทน"

# "Secretly, I'm shouting “yes!” inside. I had thought he wanted to learn sign language and even brought it up, but he had evaded the subject skillfully. It turns out I was right after all. I don't really know why this makes me so pleased."
"ในใจโลดเต้นตอบว่า “ได้!” ไปก่อนแล้ว ฉันคิดอยู่ว่าเขาคงอยากเรียนภาษามือจนถึงขั้นถามออกไปแล้ว แต่เขาก็\nเบี่ยงประเด็นไปอย่างแนบเนียน แต่ฉันก็คิดถูกอะนะ ไม่รู้เหมือนกันว่าทำไมฉันถึงดีใจเหลือเกิน"

# hi "Sure."
hi "ได้"

# "But now that I think about it, I'm not a sign language teacher. I don't even know where to start. In class, I'd be learning stuff gradually over a week. Does Hideaki expect me to teach him anything usable in a one-day crash course?"
"แต่มาคิดดูอีกที ฉันไม่ใช่ครูสอนภาษามือนี่นา ไม่รู้จะเริ่มจากตรงไหนดี ถ้าเรียนในห้องแต่ละเรื่องจะค่อย ๆ มาตามขั้น\nในแต่ละสัปดาห์ นี่เขาคาดหวังให้ฉันรวบตึงสอนสิ่งที่มีประโยชน์ทีเดียวในวันเดียวเลยหรือเปล่า"

show hideaki normal
with shorttimeskip

play music music_normal fadein 3.0

# "My teacher spent a couple days just giving a history of sign language. I decide to start off with that, to buy some time while I figure out how I can segue it into the hard stuff. Five minutes in, Hideaki raises his hand."
"ครูที่สอนฉันใช้เวลาไปสองวันสอนเรื่องความเป็นมาของภาษามือ เริ่มจากตรงนั้นแล้วกัน จะได้ยื้อเวลาให้ฉันคิดด้วยว่า\nจะเลี้ยวไปเรื่องอื่นที่ยากขึ้นยังไงดีด้วย ผ่านไปห้านาทีฮิเดอากิก็ยกมือขึ้น"

show hideaki serious_up
with charachange

# hh "I don't understand what you are doing."
hh "ผมไม่เข้าใจว่าพี่ทำอะไรอยู่"

# hi "Uh… well, you can't just jump into teaching, you know. You have to ease into it. It's like when you go swimming, you don't just jump in the lake like in some movie."
hi "เอ่อ… ก็ จะสอนเลยก็ไม่ได้ใช่มั้ยล่ะ ต้องค่อย ๆ ไปทีละขั้น เหมือนตอนไปว่ายน้ำก็ใช่ว่าจะได้โดดลงทะเลสาบเลย\nอย่างในหนังที่ไหนล่ะ"

show hideaki triangle
with charachange

# hh "I do not swim."
hh "ผมไม่ว่ายน้ำ"

# "It's like scientists managed to create a process to suck out all the hyperactive, infuriating, and childish qualities of a small child and then implant them into the dad, creating a raging jerk dad, and leaving behind Hideaki."
"เหมือนมีนักวิทยาศาสตร์ได้คิดค้นกระบวนการสูบความกระตือรือร้น ความยั่วโมโห ความเป็นเด็กทุกอย่างออกจากเด็ก\nตัวเล็ก ๆ จนเหลือฮิเดอากิอย่างตอนนี้แล้วเอาไปปลูกถ่ายให้พ่อจนได้พ่อขี้โมโหอย่างนั้น"

# "I begin to feel claustrophobic, despite the fact that the guest room is three times bigger than my dorm room and there's just the two of us in here. It's all in my head, I know it, and I don't care. I still use it as an excuse to move the lesson outside."
"อยู่ ๆ ก็รู้สึกกลัวที่แคบขึ้นมา ทั้งที่ห้องนี้ก็กว้างกว่าห้องที่หอฉันตั้งสามเท่า แถมอยู่กันแค่สองคนอีก ฉันรู้ดีว่าฉัน\nคิดไปเอง แต่สนที่ไหนล่ะ ฉันใช้ความกลัวนี้เป็นข้ออ้างที่จะมาสอนนอกบ้าน"

scene bg shizu_garden
with locationskip

# "It's a lot easier to concentrate out here. Even the precious few seconds it took to relocate managed to allow me to sort my thoughts. There were no questions during this time. Hideaki can't seem to talk and walk at the same time."
"อยู่ข้างนอกนี้แล้วสมาธิดีขึ้นเยอะ ขนาดเวลาที่ใช้ไปตอนเดินออกมาเปลี่ยนที่แป๊บ ๆ ก็มากพอให้ฉันจัดระเบียบ\nความคิดตัวเองได้แล้ว ตอนที่เดินกันอยู่ไม่มีคำถามอะไรเพราะเหมือนฮิเดอากิจะเดินไปด้วยคุยไปด้วยไม่ได้"

# "Eventually, however, I start to realize that if I'm going to teach him anything I have to keep the lesson constantly moving. The second there's an opening for it, he'll ask a question, which will lead to more questions. Then there's no end to it."
"แต่แล้วฉันก็นึกขึ้นได้ว่าถ้าจะสอนอะไรฉันก็ต้องสอนแบบเดินไปมาตลอด ตราบใดที่มีช่องให้เขาถามได้เขาก็จะถาม\nซึ่งจะมีคำถามอื่นตามมาอีกเรื่อย ๆ ไม่รู้จบ"

# "The second time he asks me why a certain hand motion means what it does, and I have to reach deep into my memory to look for etymology I don't know about a gesture I only knew about a month longer than him, I start looking for an out."
"พอเขาถามว่าทำไมท่านี้ถึงหมายความอย่างนี้เป็นครั้งที่สองฉันจึงเริ่มหาทางหนี ซึ่งท่าที่เขาถามเป็นท่าที่ฉันเพิ่งรู้\nมาได้ค่อนเดือน ฉันต้องขุดคุ้ยความทรงจำถึงที่มาของความหมายของท่านั้น ๆ"

# hi "Hideaki, let's take a break."
hi "ฮิเดอากิ พักกันก่อนเถอะ"

show hideaki bored
with charachange

# hh "Okay."
hh "ครับ"

show hideaki serious
with charachange

# hh "What is your school like?"
hh "โรงเรียนของพี่เป็นยังไงบ้างเหรอครับ"

# "This kid is like a little reporter, but it makes sense for someone his age to be curious, and this is one question I don't mind."
"เด็กคนนี้ดูอย่างกับนักรายงานข่าวตัวน้อย แต่ก็ไม่แปลกที่เด็กรุ่นเขาจะเป็นคนขี้สงสัย และคำถามนี้ฉันก็ตอบให้ได้อยู่"

# hi "What's it like? I never really thought about it. It's on top of this mountain, so it feels kind of isolated and lonely up there sometimes, even though that's also why it has a pretty great view."
hi "เป็นยังไงเหรอ ไม่เคยคิดว่าเป็นยังไงเท่าไหร่เลยแฮะ ก็อยู่บนเขา บางครั้งก็รู้สึกเหมือนอยู่ตัวคนเดียวเหงา ๆ\nแต่วิวตรงนั้นก็สวยดีนะ"

# hi "The students there are interesting. Actually, I felt bad at first. You know what kind of school it is, right?"
hi "นักเรียนที่นั่นก็น่าสนใจดีด้วย จริง ๆ ทีแรกฉันก็รู้สึกไม่ดีแหละ นายรู้ใช่มั้ยว่าเป็นโรงเรียนอะไรน่ะ"

show hideaki normal
with charachange

# hh "Yes."
hh "ครับ"

# hi "I felt bad because I didn't want to go there. I don't even remember exactly what I was thinking at the time. Probably it was something like, a school for crippled people would be a depressing place. They were telling me to go be forgotten there."
hi "ที่ฉันรู้สึกไม่ดีเพราะฉันไม่อยากไป ฉันก็จำไม่ค่อยได้แล้วว่าตอนนั้นคิดอะไรอยู่ อาจจะแบบว่า โรงเรียนคนพิการคงหดหู่\nแน่ ๆ แบบนั้นมั้ง อารมณ์เหมือนฉันจะถูกทิ้งไว้ที่โรงเรียนนั้น"

# hi "Then, everyone there was just living their lives, for the most part. So I felt even worse. It wasn't different at all, so I felt like kind of a jerk."
hi "แต่นักเรียนส่วนใหญ่ก็ใช้ชีวิตกันตามปกติ ซึ่งฉันยิ่งรู้สึกแย่เข้าไปอีก เพราะโรงเรียนนั้นไม่ได้ต่างจากที่อื่นเลย ฉันเลย\nรู้สึกว่าตัวเองเป็นคนงี่เง่า"

# hi "Shizune was the first person I met. She's in most of my classes. Misha, too, they're always together. I guess the school is accommodating enough to pair them up as much as possible. There's this girl in my class, Hanako, whom I feel bad for."
hi "ฉันเจอชิซูเนะเป็นคนแรก ส่วนใหญ่ก็ได้เรียนห้องเดียวกัน แล้วก็มิช่าด้วย สองคนนั้นอยู่ด้วยกันตลอด โรงเรียนก็คง\nพร้อมสนับสนุนพอที่จะให้สองคนนั้นได้อยู่ด้วยกันบ่อย ๆ เลยนั่นแหละ แล้วก็ห้องฉันมีผู้หญิงอีกคนที่ชื่อฮานาโกะ\nฉันสงสารคนนั้นนะ"

# hi "She has these burns, and seems to have a complex about them. But I think she looks fine. She's a cute girl. And friends with Lilly, too. You know Lilly, right? Does she bring up Hanako?"
hi "คนนั้นมีแผลไฟไหม้ แล้วก็เหมือนจะมีปมกับแผลนั้นด้วย แต่ฉันว่าก็หน้าตาดีนะ น่ารักดี เป็นเพื่อนกับลิลลี่ด้วย\nนายรู้จักลิลลี่ใช่มั้ย ลิลลี่พูดถึงฮานาโกะบ้างหรือเปล่า"

show hideaki thinking
with charachange

# hh "Yes, sometimes."
hh "ครับ ก็มีบ้าง"

# hi "I'm trying to remember who else is interesting. We have a little track star ace who runs on these prosthetics."
hi "นึกก่อนนะว่ามีใครที่น่าสนใจอีก แล้วก็มีนักวิ่งแข่งดาวเด่นที่ใส่ขาเทียม"

# hi "There's this one girl, Rin, who doesn't have arms, but she's a great painter. All her art has this harsh, alive quality. Have you ever been to Yamaku? You've probably seen some of it hanging around."
hi "แล้วก็ผู้หญิงที่ชื่อรินที่ไม่มีแขน แต่วาดรูปเก่งนะ ผลงานทุกชิ้นจะเน้นฝีแปรงหนัก ๆ แบบมีชีวิตชีวา นายเคยไป\nยามากุมั้ย น่าจะเคยเห็นงานของรินบ้างแหละ"

# hi "A little weird, sometimes, but I've always heard that artistic and creative types are like that. That reminds me, the guy who lives across the hall from me is pretty weird, too. But he can be interesting, at least."
hi "บางครั้งก็ทำตัวแปลกหน่อย ๆ แต่ฉันเคยได้ยินมาว่าพวกหัวศิลป์ก็ประมาณนั้นแหละ จะว่าไป ผู้ชายที่อยู่หอชั้นเดียวกัน\nกับฉันก็แปลก ๆ เหมือนกัน แต่อย่างน้อยบางทีเขาก็ทำตัวน่าสนใจนะ"

show hideaki normal
with charachange

# hh "You are also interesting."
hh "พี่ก็น่าสนใจ"

# hi "Is that bad? And what's with that tone? What does that even mean? Are you saying I'm weird, Hideaki?"
hi "ไม่ดีเหรอ แล้วน้ำเสียงนั่นคืออะไร หมายความว่ายังไงเนี่ย นี่นายจะหาว่าฉันแปลกเหรอฮิเดอากิ"

show hideaki triangle
with charachange

# hh "You talk a lot."
hh "พี่พูดมาก"

# "My first instinct is to go on the defensive, but the more I think about it, he has a point."
"แวบแรกในหัวฉันคือเตรียมแย้งแล้ว แต่ยิ่งคิดก็ยิ่งรู้สึกว่าจริง"

# hi "That's right, I do talk a lot. I don't think I used to."
hi "ก็จริง ฉันพูดมาก เหมือนเมื่อก่อนฉันไม่ได้พูดมากด้วย"

# hi "I think… It's probably because of all the time I spend around Shizune and Misha. Talking with them, I get caught up in all their circular logic and just how they do everything. I feel like I'm going to be drowned out, or left behind."
hi "ฉันว่า… คงจะเพราะได้อยู่กับชิซูเนะแล้วก็มิช่านี่แหละมั้ง พอได้คุยแล้วก็ต้องตามคำพูดที่วกไปวนมาหรือการกระทำ\nอะไรก็ช่างให้ทัน ไม่งั้นฉันก็กลายเป็นคนไม่มีปากมีเสียงหรือโดนดีดออกวงไปเลย"

show hideaki confused
with charachange

# hh "My sister can drown you out?"
hh "พี่ชิซูเนะทำให้พี่เป็นคนไม่มีปากมีเสียงได้เหรอครับ"

# hi "It's not like she's literally talking over me and stuff, obviously. It's hard to explain. They have more energy than I do. It's like, an aggressiveness. I don't feel like I have to match it, but I want to. I think maybe your sister has that effect on people."
hi "คือแหงแหละว่าไม่ได้หมายความว่าพูดเสียงดังกลบอะไรอย่างนั้นนะ อธิบายยากแฮะ สองคนนั้นมีพลังเยอะกว่าฉันน่ะ\nเหมือนมีความกระตือรือร้นอะไรอย่างนั้น คือฉันก็ไม่ได้อยากให้ตัวเองมีแรงเทียบเท่าสองคนนั้นหรอก แต่อีกใจก็อยาก\nเหมือนกัน พี่นายคงทำให้ทุกคนรู้สึกอย่างนั้นได้ละนะ"

show hideaki thinking
with charachange

hh "…"

# hi "Do you look up to your sister?"
hi "นายนับถือพี่นายมั้ย"

show hideaki normal_up
with charachange

# "He stares at me blankly, tense and confused as to how to react to the question."
"เขาจ้องมองฉันเหม่อ ๆ เกร็ง ๆ เหมือนเลือกไม่ถูกว่าจะตอบสนองกับคำถามนั้นยังไงดี"

show hideaki angry_up
with charachange

stop music fadeout 5.0

# hh "I will be better than Shizune."
hh "ผมจะต้องเก่งกว่าพี่ชิซูเนะ"

# hi "Better at what?"
hi "เก่งกว่าเรื่องอะไร"

show hideaki angry
with charachange

# hh "At… everything."
hh "เรื่อง… ทุกเรื่อง"

# hi "Like what?"
hi "เช่นอะไร"

show hideaki triangle
with charachange

# hh "I can do magic tricks."
hh "ผมเล่นกลได้"

# hi "You mean like telling people you've got their nose, or more like the kind of magic where you pull a rabbit out of your ass?"
hi "กลแบบที่ใช้หลอกว่าขโมยจมูกคนอื่นมาได้ หรือกลแบบที่ว่าดึงกระต่ายออกมาจากก้น?"

# "He doesn't look happy. Someday, I will see Hideaki laugh. I might just try tickling him, if I have to."
"ดูเหมือนเขาจะไม่พอใจเท่าไหร่ สักวันต้องเห็นเขาหัวเราะให้ได้ ถ้าจำเป็นจริง ๆ ก็คงต้องจักจี้เอาแล้วละ"

play sound sfx_doorslam

show hideaki surprise
with vpunch

show hideaki thinking at twoleft
show bg shizu_garden at bgleft
with dissolvecharamove

show jigoro neutral at tworight
with charaenter

# "The back door flies open and Jigoro strides out of it, keeping his back straight and taking giant, slow, regal strides, like either a king or a huge jackass."
"ประตูเปิดออกพร้อมจิโกโรที่ยืดหลังตรงเดินอาด ๆ ออกมาท่าทางคล้ายราชาไม่ก็พวกกุ๊ยข้างถนน"

# "I try to turn away, using the train of logic that if I can't see him, he can't see me. Unfortunately, it doesn't pan out and he comes over so fast it's like he appeared out of the air over my shoulder."
"ฉันรีบหันหน้าหนีด้วยคิดเอาว่าถ้าฉันไม่เห็นเขาแล้วเขาก็ไม่เห็นฉัน ซึ่งโชคไม่ดีที่ไม่เป็นไปตามนั้น เขาแวบมาอยู่\nข้างหลังฉันเหมือนเพิ่งโผล่มากลางอากาศ"

show jigoro laugh
with charachange

play music music_happiness fadein 2.0

# hx "Oho. What's up here? What are you two doing, flailing your hands around? Playing cat's cradle like a bunch of girls?"
hx "โฮ่ มีอะไรกันพวกเธอสองคน เห็นสะบัดมือสะบัดแขนไปมา เล่นพันด้ายกันแบบพวกผู้หญิงอยู่เหรอ"

# hi "I'm teaching Hideaki some sign language. What about you, Mr. Hakamichi?"
hi "ผมสอนภาษามือให้ฮิเดอากิอยู่น่ะครับ แล้วคุณล่ะครับ"

show jigoro angry
with charachange

# "He narrows his eyes suspiciously, as if he's not used to people being polite to him."
"เขาหรี่ตาลงมองอย่างไม่ไว้วางใจราวกับไม่ชินที่มีคนทำตัวสุภาพด้วย"

# hx "I am writing an autobiography of my life and times. And by “writing” I mean I am dictating it to my biographer. Unfortunately, she is running late. Unprofessional."
hx "ฉันเขียนอัตชีวประวัติถึงชีวิตและยุคสมัยของฉันอยู่ ที่บอกว่า “เขียน” นี่คือฉันพูดแล้วให้คนเขียนเขียนตามนะ\nซึ่งแย่หน่อยที่เธอคนนั้นมาสาย ไม่มีความเป็นมืออาชีพเลย"

show jigoro smug
with charachange

# hx "Perhaps you should read it when it is published later this year. I can put you on the waiting list. Maybe it will give you the moral compass you seem to lack in your life, and inspire you to stop sucking."
hx "เดี๋ยวถ้าปีนี้ได้ตีพิมพ์แล้วเธอก็น่าจะอ่านด้วยนะ ฉันจองล่วงหน้าไว้ให้ได้ เผื่ออ่านแล้วชีวิตจะได้มีเข็มทิศทางศีลธรรม\nที่เหมือนเธอจะไม่มีขึ้นมา แล้วก็จะได้เลิกทำตัวห่วยแตกด้วย"

# "It can't be sustainable for him to be so casually insulting to everyone. Though, Hideaki is likely too detached to even notice, Shizune is deaf, and most of the insults must fly over Misha's head. But surely Akira must have an opinion on this."
"คนเราไม่ควรจะมาลอยหน้าลอยตาด่าใครได้อย่างนี้หรือเปล่า แต่ฮิเดอากิก็ดูจะไม่ได้สนใจอะไร ส่วนชิซูเนะก็หูหนวก\nมิช่าก็คงไม่เข้าใจคำด่าสักเท่าไหร่ แต่อากิระต้องรู้สึกอะไรบ้างแหละ"

# "I try not to think about it. If he is doing this to psyche me out, then I have to stay calm or he wins. He must absolutely, definitely not win. This must be how Shizune feels."
"อย่าไปสนใจเลย ถ้าจะใช้วิธีกดดันฉันก็ต้องเย็นไว้ไม่ให้เขาชนะได้ จะให้เขาชนะไม่ได้เด็ดขาด ชิซูเนะก็คงรู้สึกอย่างนี้\nเหมือนกันสินะ"

# hi "How old are you?"
hi "คุณอายุเท่าไหร่เหรอครับ"

show jigoro neutral
with charachange

# hx "Forty-six."
hx "สี่สิบหก"

# hi "That doesn't seem old enough to justify writing a biography. I mean, that's not even old. Don't most people start writing their memoirs a lot later than that?"
hi "อายุก็ไม่น่ามากพอที่จะมาเขียนชีวประวัตินี่ครับ คือ ก็ไม่เห็นจะแก่ขนาดนั้นเลย คนจะมาเขียนรำลึกความทรงจำอีกที\nก็ตอนแก่ ๆ กว่านี้อีกไม่ใช่เหรอครับ"

show jigoro angry
with charachange

# hx "Shut up, boy. I am going to give you advice: do not talk about matters of age with people older than you. You are less than half my age, you have no right to talk about old. I have an ulcer older than you."
hx "เงียบไปเลยหนุ่ม ฉันขอแนะนำอะไรให้นะ ห้ามคุยเรื่องอายุกับคนที่แก่กว่า เธออายุยังไม่ถึงครึ่งอายุฉันด้วยซ้ำ\nเธอไม่มีสิทธิ์พูดว่าแก่หรือไม่แก่ แผลในปากฉันบางที่ยังมีมาก่อนเธอเกิดอีก"

# "He should get that checked out. He might have a point though, he is definitely older than I am."
"ไปหาหมอหน่อยก็ดีนะครับ แต่ก็คงถูกของเขาแหละมั้งที่ว่าตัวเองแก่กว่าฉันเนี่ย"

show jigoro laugh
with charachange

# hx "…Either way, even if we were the same age, I wouldn't have to explain myself to you, sweater vest."
hx "…แต่เอาเถอะ ต่อให้อายุเท่ากัน ฉันก็ไม่เสียเวลามาแก้ต่างตัวเองให้เธอฟังหรอก พ่อหนุ่มเสื้อกั๊กไหมพรม"

# hi "Eugh."
hi "โอ๊ย"

show jigoro angry
with charachange

# hx "Why do you make that noise? Are you mad? Well, obviously. Good. Your sweater is terrible, and I want you to feel bad about it. The burn tells me it's working."
hx "ทำไมทำเสียงอย่างนั้น โมโหเหรอ แหงละ ดี เสื้อกั๊กของเธอมันห่วยแตก แล้วก็อยากให้เธอไม่อยากใส่ด้วย เห็นเจ็บ\nอย่างนี้แปลว่าเริ่มไม่อยากใส่แล้วละสิ"

# hi "I like my sweater."
hi "ผมชอบเสื้อกั๊กผม"

show jigoro smug
with charachange

# hx "I'm sure you like huffing glue, too. That doesn't make it right."
hx "ฉันว่าเธอดมกาวด้วยแน่ ๆ แต่ใช่ว่าดมแล้วจะใส่ได้นะ"

# hi "I don't huff glue. Where did you get the impression I do?"
hi "ผมไม่ได้ดมกาวนะครับ ทำไมถึงคิดว่าผมดมกาวล่ะ"

show hideaki normal
with charachange

# hh "That is slander."
hh "หมิ่นประมาทนะครับ"

# "I wonder how Hideaki knows what slander is. Maybe Jigoro is a lawyer. I can sort of see that, although I thought only TV lawyers were this antagonistic. I don't know if I should take the chance and ask if that's his job."
"ไปรู้เรื่องหมิ่นประมาทมาจากไหนเนี่ย จิโกโรอาจจะเป็นทนายละมั้ง ก็พอเห็นภาพอยู่ แต่นึกว่ามีแค่ทนายในโทรทัศน์\nที่ทำตัวเป็นศัตรูอย่างนี้ หรือจะถือโอกาสนี้ถามอาชีพที่เขาทำอยู่ดี"

# hi "He's right. It is slander. Are you a lawyer?"
hi "ใช่ครับ นี่คุณกำลังหมิ่นประมาทอยู่นะ เป็นทนายหรือเปล่า"

show jigoro neutral
with charachange

# hx "I was guessing, a guess based on the fact that you are stupid. It's like how you are assuming I am a lawyer, except you have no reason to think that. If you want to know what I do so badly, why don't you preorder my autobiography?"
hx "ฉันก็แค่เดา ดูความโง่ของเธอ เหมือนที่เธอเดาว่าฉันเป็นทนายนั่นแหละ เว้นก็แต่ว่าเธอเดามาแบบลอย ๆ ไม่มีเหตุผล\nอะไร ถ้าอยากรู้นักทำไมไม่สั่งจองหนังสืออัตชีวประวัติของฉันล่ะ"

show jigoro angry
with charachange

# hx "Now you are insulting my book, and, by extension, my entire life. What gives you the right to do that? Arrogant. I'm trying to think of how I could make you understand my struggle. Maybe by beating you. With my autobiography."
hx "แล้วนี่เธอกำลังดูถูกหนังสือฉัน ซึ่งหมายความว่าเธอดูถูกชีวิตฉันด้วย เธอมีสิทธิ์อะไรมาว่าอย่างนั้น จองหองจริง ๆ\nฉันคิดอยู่ว่าจะให้เธอรู้ซึ้งถึงความลำบากที่ฉันต้องผ่านมายังไงดี ตีน่าจะดี ตีด้วยหนังสือฉัน"

# hx "I hope you walk away from the beating having learned a valuable lesson, like not making assumptions."
hx "หวังว่าหลังจากที่เธอโดนตีแล้วจะได้เรียนรู้อะไรดี ๆ บ้างนะ เช่นว่าห้ามเดาอะไรไปก่อน"

show hideaki bored
with charachange

# hh "Assault…"
hh "ทำร้ายร่างกาย…"

# "But he made an assumption too, that I huffed glue. I consider calling him out on this glaring example of hypocrisy, but I don't think it's worth it. He would probably explain his way out of it by saying “Shut up, boy.”"
"แต่เขาก็เดาไปก่อนว่าฉันดมกาวนี่ ฉันคิดอยู่ว่าจะท้วงตัวอย่างที่เห็นทนโท่อันนั้นดีมั้ย แต่ไม่น่าคุ้มหรอก เดี๋ยวก็คง\nแถไปว่า “เงียบไปเลยหนุ่ม”"

show jigoro smug
with charachange

# hx "Back in my day, children were seen and not heard, and to be an adult meant having experienced many hardships. With even a glance, people could instantly judge a man's character. Childhood existed only to temper you for adulthood."
hx "สมัยก่อนนะ เด็กน่ะไม่พูดมาก คนที่จะโตเป็นผู้ใหญ่ได้ต้องผ่านความลำบากร้อยพัน คนเรามองกันแวบเดียว\nก็ดูออกแล้วว่าเป็นคนยังไง วัยเด็กน่ะคือวัยที่จะมาผ่านฝึกฝนให้โตเป็นผู้ใหญ่"

# hx "When you look at me, can you not see the catalogue of my experiences even at a glance?"
hx "ตอนที่เธอมองฉันแวบแรกเธอไม่เห็นหรือไงว่าฉันผ่านอะไรมาบ้าง"

# hi "Uh… maybe. Were you a swordfighter?"
hi "เอ่อ… มั้งครับ เคยเป็นนักดาบเหรอครับ"

# "He could also be Hawaiian, and a werewolf."
"ไม่ก็เป็นชาวฮาวาย แล้วก็เป็นมนุษย์หมาป่า"

# hi "Wait, didn't you tell me before not to make assumptions? Now, you just asked me to assume stuff. And you're saying everyone when you were my age did it. And that had to be in, like, the '80s. That wasn't even that long ago!"
hi "เดี๋ยวนะครับ แต่เพิ่งบอกไปหยก ๆ ไม่ใช่เหรอครับว่าห้ามเดาอะไรไปก่อนน่ะ แล้วไหงดันมาให้ผมเดาเนี่ย แล้วก็\nบอกอีกว่าสมัยก่อนคนรุ่นผมก็ทำแบบนี้กัน แต่สมัยก่อนของคุณที่ว่ามันก็แค่ช่วงยี่สิบปีที่แล้วนี่ครับ ก็ไม่ได้นาน\nขนาดนั้นสักหน่อย!"

# "I'm ready to give him a piece of my mind, for talking like he had to walk fifteen miles in the snow to ride a coal train, that he had to shovel coal into himself, before climbing up a mountain while fighting ogres to get to school."
"ฉันละอยากจะแหวใส่เขาจริง ๆ มาโม้เหมือนว่าถ้าตัวเองจะไปโรงเรียนก็ต้องเดินยี่สิบกว่ากิโลเมตรไปขึ้นรถจักรไอน้ำที่\nตัวเองต้องตักถ่านเติมเอง แล้วจากนั้นก็ต้องไปปีนเขาสู้กับยักษ์อีก"

# "But, now that I finally want a fight, Jigoro is happy to have a good thing going just continuing to ramble about how difficult it was growing up one generation ago, twirling his sword like a baton and stopping occasionally to yawn or check the time."
"แต่พอฉันอยากจะเถียงกลับขึ้นมาจริง ๆ เขาก็ดันพล่ามต่อถึงความลำเค็ญของชีวิตคนรุ่นตัวเองที่ผ่านมาพลาง\nควงดาบเป็นไม้คทา จะหยุดควงก็ตอนที่หาวไม่ก็ตอนที่ดูเวลา"

# "The tardiness of his autobiographer is still foremost in his mind. That means the whole time he's been insulting me, he must have been doing it just to pass the time. To add insult to insult, his watch is also really nice."
"แต่สิ่งที่เขาคิดจริง ๆ ยังเป็นเรื่องคนเขียนอัตชีวประวัติที่มาช้า ซึ่งหมายความว่าเมื่อกี้ที่ด่าคือแค่ทำไปเพื่อฆ่าเวลาเล่น\nแล้วที่ฉันยิ่งรู้สึกแย่หนักคือนาฬิกาเขาก็สวยจริง ๆ"

show jigoro angry
with charachange

# hx "…When I was your age, kids had responsibilities. Not like today. Sickening. No one thinks about the consequences of their actions any more. They just do whatever they want, thinking no one will hold them accountable since they are young."
hx "…สมัยฉันอายุเท่าเธอ เด็ก ๆ น่ะต่างมีความรับผิดชอบ ไม่เหมือนทุกวันนี้ น่าปวดหัว ทำอะไรก็ไม่คิดถึงผลที่จะตามมา\nอยากทำอะไรก็ทำเพราะคิดว่าคงไม่มีใครมาต่อว่าอะไรได้เพราะเป็นเด็ก"

# "It's odd, that description could fit Shizune and Misha. I thought something similar only yesterday. But it only fits them slightly."
"ฟังดูเหมือนชิซูเนะกับมิช่าแปลก ๆ เมื่อวานฉันก็คิดอะไรประมาณนี้ แต่เหมือนนิดหน่อยแค่นั้นแหละ"

# hx "Look at yourself. An amoral, directionless, delinquent glue-huffer, with a complete lack of etiquette and absolutely no fashion sense. You are tomorrow's Japan. Disgraceful. Is this the future of this once-great country?"
hx "ดูตัวเองซิเนี่ย เป็นคนดมกาวไร้ทิศทางไร้ศีลธรรม มารยาทก็ไม่มี หัวทางด้านการแต่งตัวก็ไม่ได้ เธอคืออนาคตของญี่ปุ่น\nน่าขายหน้าจริง ๆ นี่น่ะเหรออนาคตของชาติที่เคยรุ่งเรือง"

# hi "I know someone you would get along well with."
hi "ผมพอรู้จักคนที่น่าจะอยู่กับคุณได้"

# hx "Don't interrupt! Who? One of your friends? Why would I want to talk to some awful teenager? Have you even been listening? Why are you so rude, boy? Your attitude is not one that will make you a lot of friends."
hx "อย่าขัด! ใคร เพื่อนเธอเหรอ ฉันจะลดตัวไปคุยกับวัยรุ่นเหลวแหลกทำไม เคยฟังใครบ้างมั้ย ทำไมหยาบคายอย่างนี้\nหนุ่ม นิสัยเธออย่างนี้คบใครไม่ได้หรอก"

# hi "I wish you would stop giving me so much advice."
hi "เลิกสอนผมสักทีเถอะครับ"

# "Or at least, I wish he would give me advice that he would have the decency to adhere to himself."
"หรืออย่างน้อยก็สอนอะไรที่ตัวเขาเองพอจะทำได้บ้างน่ะ"

show jigoro neutral
with charachange

# hx "Where have you been?"
hx "ไปไหนมา"

# hi "Huh?"
hi "ฮะ?"

show jigoro angry
with charachange

stop music fadeout 3.0

# hx "Not you, idiot."
hx "ไม่ใช่เธอ เด็กโง่"

show jigoro angry at Position(xpos=0.85)
show hideaki normal at Position(xpos=0.45)
show bg shizu_garden at center
with dissolvecharamove

show shizu behind_blank_cas behind hideaki:
    twoleft
    xpos 0.2
with charaenter

shi "…"

# hi "Oops. I didn't notice you there."
hi "โอ๊ะ เพิ่งเห็น"

show shizu adjust_happy_cas
with charachange

# "Shizune smiles and gives a short wave. Her arrival made Jigoro stop talking, so I'm already happy to see her for that reason alone."
"ชิซูเนะยิ้มโบกมือทักทายเล็กน้อย จิโกโรหยุดพูดเมื่อเธอมา ซึ่งทำให้ฉันดีใจมากที่เธอโผล่มา"

show shizu basic_normal2_cas
with charachange

# ssh "Misha and I decided to go into town again. Hisao, I noticed you were looking at some clothes yesterday in a store window, and I thought I would go back and buy some of them for you. It was supposed to be a surprise, though."
ssh "มิช่ากับฉันไปเข้าตัวเมืองกันอีกรอบน่ะ เห็นเมื่อวานนายมองเสื้อผ้าตามร้าน ฉันเลยกะว่าจะกลับไปซื้อมาให้นาย\nสักหน่อย แต่จริง ๆ ทีแรกจะเก็บเป็นเซอร์ไพรส์น่ะนะ"

# "She looks annoyed that the surprise is ruined, even though she ruined it herself."
"เธอดูไม่พอใจที่อดเซอร์ไพรส์ ถึงจะเป็นเธอเองที่เอามาบอกก็เถอะ"

show shizu behind_blank_cas
with charachange

# ssh "Here you go!"
ssh "เอ้านี่!"

# hi "Thanks."
hi "ขอบใจ"

show shizu basic_normal_cas
with charachange

# ssh "Misha wanted to cut her hair. I told her not to, but she said it was too hot for the summer."
ssh "มิช่าก็อยากตัดผม ฉันบอกว่าอย่าตัดเลย แต่มิช่าก็บอกว่าไว้ผมยาวกับหน้าร้อนแล้วมันร้อน"

# hi "Yeah? I don't know, that makes a lot of sense to me. It must be like an oven under there. I want to see it. Where is Misha, anyway?"
hi "หืม ไม่ยักรู้แฮะ แต่ก็เข้าใจได้นะ ไว้ยาวอย่างนั้นคงร้อนมากแน่ ๆ อยากเห็นเลยแฮะ ว่าแต่มิช่าอยู่ไหน"

# mi "Over here~! Hi, Hicchan~! Hi, Mr. Shicchan's-father~! Hi, Hideaki~!"
mi "ตรงนี้~! ไงฮิจัง~! ไงคะคุณพ่อชิซูเนะ~! ไงฮิเดอากิ~!"

show jigoro smug
with charachange

hx "…"

play music music_running

show mishashort hips_grin_cas behind shizu at offscreenleft
with charamoveinright

hide mishashort
with None

show mishashort hips_grin_cas at offscreenleft
with None

show shizu basic_normal_cas:
    xpos 0.3
show jigoro smug:
    xpos 0.95
show hideaki normal:
    xpos 0.55
show mishashort hips_grin_cas:
    center
    xpos 0.1
show bg shizu_garden:
    xpos 0.55
with dissolvecharamove

# "Misha runs around us once in a wide circle before stopping next to Shizune."
"มิช่าวิ่งรอบพวกเราหนึ่งรอบแล้วมาหยุดยืนข้างชิซูเนะ"

# "For the first time, she hasn't put her hands over my eyes, although now I see she has bags of her own to carry, so it's not like she could have even if she wanted to. Although I am positive she's tried before."
"เป็นครั้งแรกที่เธอโผล่มาแบบไม่ปิดตาฉันก่อน แต่ก็คงจะเพราะถุงข้าวของที่ถือมานั่นแหละ ต่อให้อยากทำอย่างนั้น\nมือก็คงไม่ว่างอยู่ดี แต่ฉันว่ามิช่าน่าจะเคยลองถือถุงปิดตาแล้วแหละ"

# "Her meticulously styled curls are gone now, in favor of a much shorter, sportier look. Misha looks even happier than usual, probably because she knows she won't have to wake up at the crack of dawn every morning just to do her hair."
"ผมม้วนเป็นระเบียบไม่มีแล้ว เหลือแต่ทรงผมสั้น ๆ สายลุยมาแทน มิช่าดูจะมีความสุขกว่าปกติ น่าจะเพราะคิดว่าจากนี้\nไม่ต้องตื่นแต่ไก่โห่เพื่อมาทำผมแล้ว"

show jigoro angry
with charachange

# hx "What is that haircut? You look like an intern. Your old haircut merely made you look like you were wearing a pink judge wig. Judge to intern is a huge demotion."
hx "แล้วทรงผมนั่นอะไร ดูอย่างกับเด็กใหม่ ทรงผมเก่าเธอก็เหมือนวิกผมผู้พิพากษาสีชมพูแท้ ๆ ลดขั้นไกลมากนะ\nจากผู้พิพากษามาเป็นเด็กใหม่เนี่ย"

show shizu behind_frown_cas
with charachange

# ssh "Hisao, is he saying something insulting? Tell him not to insult my friends!"
ssh "ฮิซาโอะ นี่เขาว่าใครอะไรอยู่หรือเปล่า บอกหน่อยว่าห้ามด่าเพื่อนฉัน!"

# hi "Don't insult my friends."
hi "อย่ามาว่าเพื่อนผมนะครับ"

# hx "Which one of you is talking?"
hx "คนไหนพูด"

# hi "Both of us. I agree with her."
hi "พวกเราสองคนนี่แหละครับ ผมก็คิดเหมือนชิซูเนะ"

show mishashort hips_smile_cas
with charachange

# mi "Hehehe~! What do you think, Hicchan?"
mi "เฮะ ๆ ๆ ~! ว่าไงล่ะฮิจัง"

show shizu adjust_frown_cas
with charachange

# ssh "You should have kept it like it was."
ssh "เธอไม่น่าเปลี่ยนทรงผมเลยนะ"

show mishashort perky_sad_cas
with charachange

# mi "Aw~… Hicchan, you look disappointed, you don't like it either?"
mi "โธ่~… ฮิจัง นายดูผิดหวังนะ ไม่ชอบเหมือนกันเหรอ"

# hi "Well, yeah, I'll admit I kind of liked your old haircut more, but I think this one is nice too. It suits you."
hi "ก็ อืม บอกตรง ๆ ว่าฉันชอบทรงเก่ามากกว่า แต่ทรงนี้ก็เหมาะกับเธอดีนะ"

show mishashort hips_grin_cas
with charachange

# mi "Aw, thanks, Hicchan~!"
mi "อ๋า ขอบคุณนะฮิจัง~!"

# hx "Touching. If you like it so much, maybe you two should trade."
hx "ซาบซึ้งจริง ๆ ถ้าชอบมากก็แลกกันเลยสิ"

# hi "You can't trade a haircut."
hi "ทรงผมแลกกันได้ที่ไหนล่ะครับ"

# hx "What a shame. Even her old haircut would suit you so much more than your current, slacker haircut. Awful. As for you…"
hx "น่าเสียดาย ทรงผมเดิมของเธอยังจะเหมาะกับเธอกว่าทรงผมที่เหมือนคนไม่เอาไหนทรงนี้อีก แย่จริง ๆ ส่วนเธอ…"

show jigoro laugh
with charachange

# hx "Hmmm… Actually, this is much less garish than your other haircut. I like it."
hx "อืมมม… ที่จริง ทรงนี้ก็ดูบาดตาน้อยกว่าทรงเดิมนะ ฉันชอบ"

show mishashort cross_laugh_cas
with charachange

# mi "Ahahahaha~! Really? Thanks, Mr. Shizune's-dad~!"
mi "อะฮ่าฮ่าฮ่าฮ่า~! จริงเหรอคะ ขอบคุณค่ะคุณพ่อชิซูเนะ~!"

show jigoro angry
with charachange

# hx "It's Mr. Hakamichi. Talk like a normal person."
hx "คุณฮากามิจิ พูดให้เหมือนคนปกติหน่อย"

show mishashort perky_smile_cas
with charachange

# mi "Hm~? I don't understand~! Okay, okay okay~! I'll call you Mr. Hakamichi!"
mi "ขา~? ไม่เข้าใจค่ะ~! โอเค โอเค โอเค~! หนูจะเรียกคุณว่าคุณฮากามิจิ!"

# hx "Agh, it's like speaking to a slide whistle. Contemptible. Where's my biographer? Hideaki!"
hx "โอย เหมือนคุยอยู่กับนกหวีดเลย น่ารังเกียจจริง ๆ แล้วนี่คนเขียนชีวประวัติฉันอยู่ไหน ฮิเดอากิ!"

show jigoro invis
show shizu basic_normal_cas
show hideaki bored
with charaexit

# "He starts quietly muttering to himself and walks off. I guess a wannabe-cranky old man like Jigoro would at the very least be hesitant to yell at girls. Suddenly, he doubles back, unable to resist his urge to have the last word."
"เขาพึมพำอยู่กับตัวเองแล้วเดินหนีไป แม้แต่ตาลุงขี้โม้เจ้าอารมณ์อย่างจิโกโรอย่างน้อยก็น่าจะมีความเกรงใจพอที่จะ\nไม่ตะคอกใส่เด็กผู้หญิงละนะ จู่ ๆ เขาก็ถอยมาเพราะอดที่จะพูดปิดท้ายไม่ได้"

show jigoro angry
with charaenter

# hx "And another thing, you do not have to be so loud. I do not like being shouted at."
hx "แล้วอีกอย่าง ไม่ต้องเสียงดังขนาดนั้น ฉันไม่ชอบให้ใครมาตะโกนใส่"

show mishashort hips_grin_cas
with charachange

# mi "What? Shouting~? I'm not shouting~!"
mi "ขา? ตะโกนเหรอคะ~ หนูไม่ได้ตะโกนนะ~!"

# "I can't think of anyone more unqualified to talk about what's garish or to chastise someone else on shouting at people. It's like a parade of hypocrisies and the hits just keep coming."
"สภาพคนที่ว่าคนอื่นเรื่องความบาดตากับเรื่องระดับเสียงนี่ก็ไม่ต่างกันเท่าไหร่นะ ยิ่งดูเหมือนยิ่งได้เห็นความย้อนแย้ง\nที่ไหลมาเรื่อย ๆ ไม่หยุด"

# "An unusual reaction seems to be taking place. Misha apparently finds Jigoro funny and laughs pretty much every time he says something, which only makes him berate her harder. I guess this is what they call a vicious circle."
"แล้วก็เหมือนจะมีปฏิกิริยาเพี้ยน ๆ เกิดขึ้น ดูท่าว่ามิช่าจะขำจิโกโรจนหัวเราะแทบทุกครั้งที่เขาพูด แล้วพอหัวเราะ\nเขาก็ยิ่งว่าเธอหนักเข้าไปอีก นี่ละมั้งที่เขาเรียกว่าวงจรอุบาทว์"

# "Misha's voice is punctuated with explosions of laughter and seems to come from everywhere. On the other hand Jigoro's is booming and directed like a cannon. In any case, they are both unbelievably loud."
"เสียงมิช่าจะถูกคั่นด้วยระเบิดหัวเราะที่มาจากทั่วทุกสารทิศ ส่วนฝั่งจิโกโรจะเป็นเสียงยิงตู้มต้ามแบบปืนใหญ่ ซึ่งเสียง\nทั้งคู่ก็หนวกหูเหลือเชื่อนั่นแหละ"

# "The more they talk to each other, the more they seem to play off each other's volume and get louder."
"ยิ่งสองคนนั้นคุยกันก็ยิ่งเหมือนเร่งเสียงกันและกันให้ดังขึ้นเรื่อย ๆ"

show mishashort perky_sad_cas
with charachange

# mi "Ow~! My ears hurt~!"
mi "โอ๊ย~! เจ็บหู~!"

# hx "WHY ARE YOU SHOUTING?"
hx "ตะโกนทำไม!!"

hide shizu
with charaexit

show black
with hands_in

# "Shizune's hands wrap around my eyes from behind, something I'm so used to Misha doing that for the first time I find myself confused by it, since Misha is in front of me."
"ชิซูเนะเข้ามาทางข้างหลังฉันแล้วปิดตา ฉันชินการกระทำนี้กับมิช่าแล้วก็จริง แต่ฉันก็ตกใจเพราะตอนนี้มิช่า\nอยู่ตรงหน้าฉัน"

show shizu adjust_happy_cas_close at center behind black
show hideaki bored at center
with None

hide black
with hands_out

# "She lets go and holds a finger up to her lips."
"เธอปล่อยมือแล้วใช้นิ้วตัวเองแตะที่ริมฝีปาก"

show shizu behind_smile_cas_close
with charachange

# ssh "What a perfect distraction! Now's our opportunity. Let's sneak off."
ssh "เบี่ยงความสนใจได้สวย! จังหวะนี้แหละคือโอกาสของเรา แอบหนีไปกันเถอะ"

# his "Why do we have to sneak off? Why not just walk off?"
his "ทำไมต้องแอบหนีด้วย เดินหนีเฉย ๆ ไม่ได้เหรอ"

show shizu adjust_smug_cas_close
with charachange

# ssh "It wouldn't be as fun."
ssh "ไม่งั้นก็ไม่สนุกน่ะสิ"

show shizu basic_happy_cas_close
with charachange

# ssh "It's decided: it's a secret mission. Escape without being detected. Extract Hideaki for bonus points."
ssh "ตกลงตามนี้ ภารกิจนี้เป็นภารกิจลับ หนีโดยที่ห้ามให้ใครจับได้ ถ้าช่วยฮิเดอากิออกมาได้ด้วยจะได้คะแนนพิเศษ"

hide shizu
with charaexit

stop music fadeout 3.0

# "Already, she has simplified the situation into a game. Shizune quietly slides away from the scene and begins edging towards the house. I walk towards it, normally."
"เธอทำให้เรื่องนี้เป็นเกมไปแล้ว ชิซูเนะแอบหนีออกมาแล้วเลียบ ๆ ไปตามทางมายังบ้าน ส่วนฉันก็เดินเข้าบ้านตามปกติ"


########

label th_S22:

scene bg shizu_living
with locationskip

# "I can't find Shizune at first, but eventually she walks into the main part of the house, sipping a glass of ice water and dangling her glasses back and forth from her free hand. She whips them on as soon as she sees me."
"ตอนแรกฉันยังไม่เห็นชิซูเนะ แต่ไม่นานเธอก็เดินเข้ามาที่ใจกลางบ้านพลางจิบน้ำที่ใส่น้ำแข็งโดยที่มืออีกข้าง\nแกว่งแว่นตาไปมา เธอรีบใส่แว่นตาทันทีที่เจอกับฉัน"

show shizu basic_normal2_cas at center
with charaenter

play music music_ease fadein 4.0

# ssh "You didn't rescue Hideaki. That means you don't get the bonus points. If you were also being graded on style, I'd have to deduct points for a booooooring escape."
ssh "นายไม่ได้ช่วยฮิเดอากิมาด้วย แปลว่านายไม่ได้คะแนนพิเศษ ถ้าจะให้คิดคะแนนจากท่าหนีด้วยฉันก็คงต้องหักคะแนน\nเพราะนายหนีมาได้น่าเบื่อมาาาาาาาก"

# his "It looked like you wanted to talk to me, I didn't know I had to be stylish about it. You know, some say that the most stylish people are the ones that don't try too hard to look cool."
his "เหมือนเธอมีเรื่องจะคุยกับฉัน ไม่ยักรู้ว่าต้องทำเท่ ๆ ด้วย เนี่ย บางคนเขาก็บอกว่าคนที่เท่ที่สุดก็คือคนที่ไม่เก๊ก\nให้ตัวเองเท่"

show shizu cross_wut_cas
with charachange

# ssh "You're really cool."
ssh "นายเท่มาก"

# "I wonder how is it that I can pick up on her sarcasm so easily, and how hard it might have been for her to learn the concept of sarcasm without being able to hear. I can't imagine it."
"ทำไมฉันถึงรู้ได้ไวขนาดนี้นะว่าที่บอกเมื่อกี้คือประชด แล้วการที่ชิซูเนะจะเข้าใจคำว่าประชดได้โดยที่ไม่ได้ยินนี่\nคงลำบากมากแน่ ๆ นึกภาพไม่ออกเลย"

# his "You seem like you're in a good mood."
his "เธอดูอารมณ์ดีนะ"

# "Although I guess it isn't really a good mood. It's more that she seems very excited."
"ถึงจะไม่เชิงว่าอารมณ์ดีก็เถอะ เหมือนตื่นเต้นมาก ๆ มากกว่า"

show shizu behind_frown_cas
with charachange

# ssh "I'm in a bad mood."
ssh "ฉันอารมณ์ไม่ดี"

show shizu basic_normal2_cas at Position(ypos=1.1)
with dissolvecharamove

# "Setting her drink down, Shizune sits down on the couch."
"ชิซูเนะวางแก้วแล้วนั่งลงกับโซฟา"

show shizu behind_frown_cas
with charachange

# ssh "I liked her regular hairstyle so much more. It looked so pretty. It was refined and meticulous. Now she looks too sporty and tomboyish."
ssh "ฉันชอบทรงผมเดิมกว่าเยอะ ทรงนั้นน่ะสวยมาก ดูเป็นระเบียบเรียบร้อย แล้วทรงนี้ทำให้ดูเป็นสายลุยเกิน\nแถมดูเหมือนทอมอีก"

# his "I wouldn't call Misha refined and meticulous. That sounds more like you. You should give it a chance. Grow your hair out and make it look like drills."
his "ฉันว่าคำว่าเป็นระเบียบเรียบร้อยนี่ไม่น่าใช่มิช่านะ สองคำนั้นเหมือนเธอมากกว่า เธอก็น่าจะลองบ้างนะ ไว้ผมยาว\nแล้วทำทรงสว่านน่ะ"

# his "Hm… actually, maybe this suits you just fine."
his "อืม… จริง ๆ ทรงนี้ก็น่าจะเหมาะกับเธอดีอยู่แล้วนะ"

show shizu adjust_frown_cas
with charachange

# "Shizune rubs the frame of her glasses roughly, looking annoyed at the implications behind what I just signed to her. That's fine, because I was totally implying that. She moves a little closer to me when I take a seat."
"ชิซูเนะถูกรอบแว่นตัวเองแรง ๆ เหมือนนึกหงุดหงิดกับสิ่งที่ฉันจะสื่อ ก็ไม่เป็นไรหรอก ฉันจะสื่ออย่างนั้นน่ะแหละ พอฉัน\nนั่งลงแล้วเธอก็เขยิบเข้ามาใกล้ ๆ"

show shizu basic_angry_cas
with charachange

# ssh "I'm a tomboy?"
ssh "ฉันเป็นทอมเหรอ"

# his "Well, no one would call you a tomboy. …Based on appearances."
his "ก็ คงไม่มีใครจะเรียกเธอว่าทอมหรอก… ถ้าดูจากรูปลักษณ์แล้วน่ะนะ"

# "Shizune glares at me, unamused. I have to fight to keep a straight face."
"ชิซูเนะจ้องฉันด้วยความไม่พอใจ ฉันปั้นหน้านิ่ง ๆ ไว้"

# his "Maybe you two should trade haircuts anyway."
his "เธอสองคนน่าจะแลกทรงผมกันนะ"

shi "…"

show shizu behind_frown_cas
with charachange

# ssh "You sound like my father."
ssh "พูดเป็นพ่อฉันไปได้"

show shizu adjust_smug_cas at center
with Dissolvemove(0.2)

# "It's true. Shizune giggles noiselessly when she sees my displeasure at the realization. Jumping to her feet, she twirls an invisible sword in her left hand while standing up militarily straight and grimacing. A terrifyingly accurate impression."
"ก็จริง ชิซูเนะทำท่าแอบขำน้อย ๆ ที่เห็นฉันหน้าเบ้ไปเมื่อนึกถึงพ่อของเธอ เธอเด้งตัวลุกขึ้นยืนแล้วควงดาบล่องหน\nพลางยืนแบบอกผายไหล่ผึ่งพร้อมปั้นหน้าบูดด้วย เหมือนเป๊ะจนขนลุกเลย"

show shizu basic_frown_cas
with charachange

# ssh "Anyway, I don't take advice from anyone who wears a blue sweater with brown pants. Where's your sense of color coordination? Dreadful."
ssh "แต่เอาเถอะ ฉันไม่ฟังคนที่ใส่เสื้อสีน้ำเงินกับกางเกงสีน้ำตาลหรอก ไหนความกลมกลืนสี ขนลุก"

show shizu adjust_smug_cas
with charachange

# ssh "…But changing my haircut, that might be fun. Wouldn't it be? I want to see how everyone would react."
ssh "…แต่ถ้าฉันตัดผมทรงใหม่คงสนุกน่าดู อยากรู้จังว่าทุกคนจะว่ายังไง"

# his "You must really like playing with people. Sometimes, I think, a little too much."
his "เธอนี่ชอบเล่นกับคนอื่นจริงนะ ฉันว่าเพลา ๆ บ้างก็ดี"

show shizu adjust_frown_cas
with charachange

# "No answer. The way she fiddles with her glasses, brow furrowed, tells me that it's because she can't."
"ไม่มีการตอบรับ เธอจับแว่นเล่นพลางขมวดคิ้วสื่อว่าเธอตอบรับไม่ได้"

show shizu behind_blank_cas
with charachange

# ssh "It's fun."
ssh "ก็สนุกดี"

# "Then, with more confidence and while pulling herself closer to me:"
"จากนั้นเธอขยับเข้ามาใกล้ด้วยความมั่นใจ"

show shizu basic_happy_cas
with charachange

# ssh "It's fun to drag more and more people into my life."
ssh "ก็สนุกดีที่ได้ลากใครต่อใครให้เข้ามาในชีวิตฉัน"

# his "Oh, I see."
his "อ้อ อย่างนี้นี่เอง"

# "I wonder if I'm included in that number. I want to ask, but am not even sure how I would."
"นับฉันด้วยหรือเปล่านะ อยากถามแต่ก็ไม่รู้จะถามยังไง"

show shizu adjust_happy_cas
with charachange

# "Shizune wags a finger preemptively, indicating that she won't be answering such a question anyway."
"ชิซูเนะส่ายนิ้วดักฉันว่ายังไงเธอก็ไม่ตอบคำถามนั้นให้แน่นอน"

stop music fadeout 0.5

show shizu adjust_blush_cas_close
with vpunch

# "She reaches for her glass, but doesn't seem to realize how far she's managed to inch away from it all this time. To prevent herself from tipping over clumsily, Shizune tries to grab on to me, and ends up pulling me on top of her."
"เธอเอื้อมมือไปคว้าแก้วน้ำ แต่เหมือนจะไม่รู้ตัวว่าเธอขยับตัวห่างจากแก้วมาเรื่อย ๆ ตั้งแต่เมื่อกี้แล้ว เธอจับฉันไว้\nไม่ให้ตัวเองล้มคว่ำ แต่ก็กลายเป็นว่าเธอดึงจนฉันล้มทับเธอแทน"

scene ev shizu_couch
with vpunch

play music music_serene fadein 9.0

# "As I lean over her, I can feel the heat coming off her body and realize how close we are. I can hear her soft breathing and the slight rustling of her clothes as she momentarily fidgets about."
"พอฉันขยับเข้าไปใกล้ ไอร้อนที่แผ่มาจากตัวเธอทำให้ฉันรู้สึกถึงระยะที่ใกล้ชิด เสียงหายใจแผ่วเบาและเสียงจากเสื้อผ้า\nเมื่อเธอขยับตัวเล็กน้อยดังอยู่ในหูฉัน"

# "A blush starts to creep into her cheeks, but her eyes stare straight into mine, dark and unblinking."
"แก้มเธอแดงเรื่อขึ้นมา ทว่าสายตาดำขลับยังคงจับจ้องฉัน"

# "It's the same look from the first time I saw her, piercing and devoid of any clear emotions. Just waiting to see what will happen next, like the eyes of a cat. It makes me feel uncomfortable, being looked at in such a way."
"เป็นดวงตาอันแหลมคมและไร้ซึ่งอารมณ์คู่เดียวกันกับตอนที่ฉันได้เจอเธอเป็นครั้งแรก เป็นสายตาที่จ้องมอง\nสิ่งที่จะเกิดขึ้นคล้ายตาของแมว ฉันอึดอัดที่ถูกมองเช่นนั้น"

# "This is the first time I've been so close to her for an extended period of time, and the mood is different now. The situation now isn't the same as a passing touching of hands or her and Misha's usual games."
"เป็นครั้งแรกที่ฉันได้อยู่กับเธอนานขนาดนี้ และอารมณ์ตอนนี้ต่างออกไปจากทุกครั้งที่มักจะเป็นการแตะมือกัน\nเล็กน้อยหรือไม่ก็การแตะตัวกันเวลาเล่นเกมที่มิช่าชอบเล่น"

# "Shizune's fingers weave together tentatively, but she makes no move to sign. The look in her eyes isn't just nothing, like I'd thought. It's more like expectation. I wonder if maybe I've been following the string of her expectations this entire time."
"นิ้วของชิซูเนะขยับไปมาคล้ายรอบอกบางอย่าง แต่ก็ไม่ขยับทำภาษามือใด ๆ สายตาที่เธอจ้องมานั้นไม่ได้จ้องมาเปล่า\nอย่างที่ฉันคาด หากแต่เหมือนคาดหวังบางอย่าง นี่ฉันทำตามที่เธอคาดหวังมาตลอดหรือเปล่านะ"

scene bg shizu_living
with vpunch

show shizu behind_blank_cas_close
with charaenter

# "I feel her grabbing me by the shoulders and then gently, but firmly, pushing me off of her. I roll sideways onto the soft couch and pull myself into a sitting position less than a foot from her. The way I feel, she might as well have thrown me ten yards."
"เธอจับไหล่ฉันไว้แล้วค่อย ๆ ผลักฉันออกอย่างมั่นคง ฉันพลิกตัวลงกับโซฟาแล้วลุกขึ้นนั่งไม่ห่างจากเธอ ในใจตอนนี้\nฉันรู้สึกเหมือนถูกเธอปาทิ้งไปไกลสักเกือบสิบเมตรได้"

# "When I think about it, this is perhaps one of the biggest drawbacks to sign language. Shizune said that the fact that you have to sign your words out with your hands means you have time to reflect on what you say before you say it."
"พอมาคิดดูแล้ว นี่แหละมั้งข้อเสียที่แย่ที่สุดของภาษามือ ถึงชิซูเนะจะบอกว่าการบอกอะไรผ่านภาษามือทำให้มีเวลา\nได้คิดคำพูดก่อนก็เถอะ"

# "But on the other hand, it also means that what would normally just be an awkward silence becomes an insurmountable wall. I'd just blurt out something, anything, to try and dispel the tension I'm feeling right now if I could, but I can't."
"แต่อีกแง่หนึ่ง ความเงียบที่น่าอึดอัดนั้นก็จะกลายเป็นกำแพงหนาขึ้นมา ถ้าพูดแล้วมันคลายความรู้สึกตึงเครียด\nที่อยู่ในใจฉันตอนนี้ได้ฉันก็จะพล่ามอะไรก็ได้สักอย่างออกมา แต่ฉันทำอย่างนั้นไม่ได้"

# "Ordinarily, I think that what would be normal would be to apologize, and maybe leave. But right now, I wonder if that is even applicable. I can't get past how guilty such an action would seem. Like I were just slinking away."
"ปกติแล้วฉันก็คงจะขอโทษแล้วเดินหนีไป แต่จะทำอย่างนั้นกับสถานการณ์ตอนนี้ได้หรือเปล่า ฉันอดรู้สึกผิดไม่ได้\nที่จะทำอย่างนั้น เพราะจะเหมือนกับว่าฉันแอบหนีไปดื้อ ๆ เลย"

# "Of course, it's not like I can just play it off like nothing happened, either. That would just be insulting to both of us. So, as much as I don't want to, I apologize quickly, so quickly I forget to sign it. Then I go back to my room."
"แต่แน่ละว่าฉันจะทำเหมือนไม่มีอะไรเกิดขึ้นไม่ได้ ทำอย่างนั้นไปก็เจ็บใจกันทั้งคู่เปล่า ๆ ฉันจึงแข็งใจรีบขอโทษจนลืม\nบอกเป็นภาษามือแล้วกลับมาที่ห้องตัวเอง"

window hide None

scene bg shizu_guesthisao_ss
with locationskip

play sound sfx_pillow
with vpunch

$ renpy.music.set_volume(0.5, 1.0, channel="music")

show black
with shuteye

window show

# "Sighing, I let myself fall backwards into bed. I wish I could just go to sleep right now, but I feel wide awake."
"ฉันถอนหายใจทิ้งตัวลงนอนกับเตียง อยากจะหลับไปเลย แต่ตอนนี้ไม่ได้ง่วงแม้แต่น้อย"

play sound sfx_doorclose
$ renpy.music.set_volume(1.0, 3.0, channel="music")

with Pause(3.0)

show shizu basic_normal2_cas_close
hide black
with openeye

# "I sit up when I hear the door closing and open my eyes to see Shizune sitting in the chair in front of me."
"ฉันลุกขึ้นนั่งเมื่อได้ยินเสียงปิดประตู พอลืมตาก็เห็นชิซูเนะที่นั่งกับเก้าอี้อยู่ตรงหน้าฉัน"

show shizu behind_blank_cas_close
with charachange

shi "…"

# "She asks a question that goes right over my head, due to my surprise. It's not a feeling I'm good at concealing, and I don't think it's what she intended. Whatever she was saying, she backs off, and doesn't attempt to sign again for a while."
"เธอถามอะไรสักอย่างที่ฉันไม่รับรู้เลยเพราะยังตกใจอยู่ ฉันซ่อนความตกใจตัวเองไม่เก่ง เธอเองก็คงไม่ได้อยากให้ฉัน\nตกใจด้วย เธอยอมแพ้ไม่ทำภาษามือนั้นซ้ำอีกแล้วนิ่งไปพักหนึ่ง"

show shizu adjust_happy_cas_close
with charachange

# ssh "This is the first time I've been in your room."
ssh "ฉันเพิ่งเคยมาห้องนายเป็นครั้งแรกเลยนะ"

# "Shizune tents her fingers and puts on an exaggerated attempt to make herself look embarrassed and modest at the thought. I can't appreciate the joke, just the fact that she's here has me feeling a bit scattered."
"เธอประกบนิ้วเข้าหากันแล้วทำท่าให้ดูกระมิดกระเมี้ยนกับคำพูดเมื่อกี้แบบเวอร์ ๆ ซึ่งฉันขำไม่ลง เพราะแค่เธอมา\nอยู่ตรงนี้ก็ทำอารมณ์ฉันปั่นป่วนไปแล้วเล็กน้อย"

# his "Very funny. It isn't even my room. It's your guest room."
his "ตลกมาก ห้องนี้ไม่ใช่ห้องฉันด้วยซ้ำ นี่มันห้องนอนแขกของเธอ"

#If seen A26b:
label th_S22a:

# his "Besides, you and Misha barged into my room once before."
his "อีกอย่าง เธอกับมิช่าก็เคยบุกห้องฉันมาแล้วนี่"

show shizu behind_blank_cas_close
with charachange

# "It seems as if she expects me to say more. I remember feeling very panicked when they burst into my room, afraid of what conclusions they would jump to seeing the wall of pills lining the place. I don't think that Shizune remembers, though."
"เหมือนว่าเธอคาดหวังจะให้ฉันบอกอะไรอีก ฉันยังจำได้ว่าตอนนั้นฉันลนลานมากที่สองคนนั้นบุกห้องเพราะกลัว\nจะเห็นยาที่ตั้งเรียงรายแล้วคิดอะไรได้ แต่ชิซูเนะน่าจะจำไม่ได้แล้วมั้ง"

show shizu basic_normal_cas_close
with charachange

# ssh "It made you nervous."
ssh "นายลนมาก"

#if not seen A26b:
label th_S22b:

# ssh "You still looked startled when I came in."
ssh "ตอนฉันเข้าห้องมานายยังดูลนอยู่เลย"

#end split
label th_S22c:

# "The way she says it so factually stings me."
"พอพูดออกมาหน้าซื่ออย่างนั้นแล้วฉันก็จี๊ดขึ้นมา"

# his "A lot of things make me nervous."
his "ฉันลนกับอะไรหลายอย่าง"

# his "You're one of them."
his "กับเธอด้วย"

show shizu behind_blank_cas_close
with charachange

shi "…?"

# his "Because you're overeager to always get people involved in… whatever you're doing. Whether it's joining the Student Council, or even taking a break. Whether they want to or not."
his "เพราะเธอชอบลากคนมา… ทำอะไรหลายอย่างที่เธอทำอยู่ ทั้งสภานักเรียนเอย ลากไปพักก็ไม่เว้น ลากแบบไม่สนว่า\nเขาจะอยากทำหรือเปล่า"

show shizu basic_angry_cas_close
with charachange

shi "…"

show shizu adjust_happy_cas_close
with charachange

shi "… … … …"

show shizu basic_normal2_cas_close
with charachange

shi "… …"

# "She signs almost at a crawl, her hands pausing mid-sentence far too much, causing the words to dissipate formlessly before I can even begin to try to understand them. I try not to let on that this is the case."
"เธอส่งภาษามืออย่างเชื่องช้า มือเธอชะงักกลางคันบ่อยเกินไปจนทันไม่ทันจับใจความคำได้ครบถ้วน แต่ฉันก็ทำเป็น\nเหมือนว่ายังดูรู้เรื่อง"

# "It seems to work, but she looks a little sad, and I regret that I have nothing to say to snap her from the strangely wistful and distant expression she is wearing. All I can do is wait for her to come out of it."
"ซึ่งก็ดูจะได้ผล แต่เธอยังดูหมอง ฉันนึกเสียใจที่ไม่อาจพูดอะไรให้เธอคลายสีหน้าที่เศร้าสร้อยและเหินห่างนั้นได้เลย\nฉันทำได้เพียงแต่รอให้เธอหายเอง"

show shizu behind_sad_cas_close
with charachange

# ssh "You are right. I want to drag everyone into my life. But, lately, I'm no longer sure if it's the right thing to do."
ssh "นายพูดถูก ฉันอยากลากทุกคนเข้ามาในชีวิตฉัน แต่ช่วงนี้ฉันเริ่มคิดแล้วว่าที่ทำอย่างนั้นถูกแล้วหรือยัง"

# his "I enjoyed you taking me to your favorite restaurant the other night."
his "ขอบคุณนะที่พาไปกินข้าวร้านโปรดเธอเมื่อคืนก่อน"

show shizu basic_normal_cas_close
with charachange

# ssh "It's not like that was my favorite restaurant… I have others I like. I might even be able to rank them by number."
ssh "ร้านนั้นไม่ใช่ร้านโปรดฉันหรอก… ร้านอื่นที่ฉันชอบก็มี ให้จัดอันดับเลยยังได้"

# his "Really…"
his "จริงเหรอ…"

show shizu adjust_frown_cas_close
with charachange

# ssh "This chair is so hard. I want to sit on the bed."
ssh "เก้าอี้นี่นั่งไม่สบายเลย อยากนั่งบนเตียงจัง"

# "Motioning to her to go ahead, I wait for her to get off the chair and take her place when she does. Though I didn't intend for it to be, she finds it amusing."
"ฉันบุ้ยใบ้ให้เธอมานั่งที่เตียงแล้วรอไปนั่งที่เก้าอี้แทนที่เธอ เธอยิ้ม ๆ ทั้งที่ฉันไม่ได้ตั้งใจจะให้เธอขำหรืออะไร"

show shizu behind_smile_cas_close
with charachange

stop music fadeout 5.0

# ssh "Close your eyes."
ssh "หลับตาสิ"

# his "Why?"
his "ทำไม"

show shizu adjust_smug_cas_close
with charachange

# ssh "It's a surprise."
ssh "เซอร์ไพรส์"

show black
with shuteye

# "I decide to humor her and close them. I can feel her leaning over me, and suddenly, something soft and moist touches my lips. My body tenses up in surprise. Fortunately, not as awkward a reaction as I could have made."
"ฉันหลับตาตามเธอสั่งอย่างว่าง่าย เหมือนเธอจะโน้มตัวเข้าหาฉัน มีบางอย่างที่นุ่มนิ่มและชุ่มฉ่ำเข้าแตะริมฝีปากฉัน\nทั้งตัวฉันเกร็งด้วยความตกใจ ยังดีที่ฉันไม่ได้ตื่นตระหนกหนักมากมาย"

# "It was just a quick peck, and I almost think that's the end of it, but then she kisses me again, more deeply this time. Her hands slide onto my shoulders, up to my neck, and then back down again. Then across my shoulders and down my arms."
"เป็นแค่จุ๊บสั้น ๆ ซึ่งฉันคิดว่าน่าจะมีแค่นั้น แต่แล้วเธอก็จูบซ้ำอีกหนโดยที่คราวนี้หนักหน่วงกว่าเก่า มือเธอเข้ามาแตะ\nที่ไหล่ฉันก่อนจะเลื่อนขึ้นมาที่คอแล้วกลับลงไปที่ไหล่ จากนั้นแขนข้างนั้นก็โอบฉันโดยที่มือจับแขนฉันอีกข้างเอาไว้"

# "I can feel the weight of her body on my legs, and the eroticism of the situation isn't lost on me. At this point, I'm ready to try and open my eyes just a crack, but as if expecting it, she puts her fingers on my eyelids."
"เธอทิ้งตัวลงกับขาฉัน และฉันก็รับรู้ถึงสัญญาณของการกระทำเหล่านี้ดี ซึ่งฉันเตรียมจะลืมตาแอบมองแล้ว แต่เธอก็\nใช้นิ้วทาบไว้ที่เปลือกตาฉันราวกับรู้ว่าฉันจะทำอะไร"

play sound sfx_rustling

# "Seconds later, something ties my hands together at the wrists, and I panic, not knowing what to make of this. My first thought is to ask Shizune what she's thinking. Even though she can't hear me, I'm sure she gets the gist of it."
"ไม่นานมือฉันก็ถูกมัดไว้ด้วยบางอย่าง ฉันลนลานเพราะยังสับสน ฉันอยากจะถามชิซูเนะก่อนว่าเธอคิดอะไรอยู่กันแน่\nถึงเธอจะไม่ได้ยิน แต่ก็ต้องรู้แน่ ๆ ว่าฉันจะถามอะไร"

# "She won't let go of my hands, tracing her fingers over them, from the lines of my palms, over my knuckles, and to my wrists."
"ชิซูเนะไม่ยอมผละจากมือฉัน เธอลากนิ้วไปตามเส้นลายมือ ขึ้นมาที่ข้อนิ้ว จากนั้นก็เลื่อนมาที่ข้อมือ"

scene evh shizune_hcg_tied_stare:
    yalign 0.0 xalign 1.0 subpixel True
    easein 6.0 xalign 0.5 zoom 0.5
    truecenter
    zoom 1.0
    "evh shizune_hcg_tied_stare_small"
with whiteout

play music music_heart fadein 5.0

# hi "Hey, what are you doing? What's this?"
hi "เฮ้ย อะไรเนี่ย ทำอะไรของเธอ"

# "Or course, with my hands tied behind my back, I might as well be gagged. A part of me can't help but think that this is what she intended."
"แน่นอนว่าการที่ฉันถูกมัดมือนั้นก็ไม่ต่างอะไรกับการถูกปิดปาก ฉันอดคิดไม่ได้ว่าเธอจงใจให้เป็นอย่างนี้หรือเปล่า"

scene evh shizune_hcg_tied_smile_small
with charachange

# "As if reading my thoughts, a mischievous expression lights up her face, but her blushing doesn't fade. In fact, it only deepens when our eyes meet."
"เธอยิ้มเจ้าเล่ห์คล้ายอ่านความคิดฉันได้ แต่หน้าเธอยังแดงเรื่อ และยิ่งแดงหนักกว่าเดิมเมื่อสบตากัน"

# "Embarrassed, she leans deeper into our partial embrace, hiding her face by burying it in my shoulder and neck. Her hair is soft and tickles me, and I let out a laugh knowing that she won't hear me; won't be offended."
"เธอโน้มตัวเข้าใกล้อีกด้วยความอับอายและซ่อนใบหน้าตัวเองด้วยการซุกเข้าที่บ่าและคอของฉัน ผมนุ่มของเธอทำให้\nฉันจักจี้ ฉันปล่อยหัวเราะออกมาเพราะรู้ว่าเธอคงไม่ได้ยินและไม่คิดอะไร"

label th_S22h:

scene evh shizune_hcg_tied_blush_small
with charachange

# "Shizune's hands move downwards to the fly of my pants, covered by her skirt. Her hands disappear from view, only to jerk back on touching my erection. Shizune almost falls off me from nervousness. It's like she didn't expect it to be there."
"มือชิซูเนะเลื่อนต่ำลงมาที่เป้ากางเกงฉันที่กระโปรงเธอปรกอยู่ มือเธอหายไปใต้กระโปรงนั้นก่อนจะกระตุกเล็กน้อย\nเมื่อได้แตะความแข็งขืนนั้น เธอเกือบทรงตัวไม่อยู่ด้วยความลนลานคล้ายไม่คาดคิดว่าจะเจอสิ่งนั้น"

# "The sudden display of naivety is the starkest contrast yet to how forward she has been so far, and I find it amusing. Suddenly, she seems very immature again. A high-school girl playing the role of a more aggressive woman."
"ความใสซื่อที่ขัดกับความกล้าจากการที่เธอทำตัวมาตลอดก่อนหน้านี้ทำให้ฉันอดยิ้มไม่ได้ จู่ ๆ เธอก็ดูเป็นเด็ก\nเป็นสาวมัธยมปลายที่สวมบทบาทเป็นผู้หญิงสายรุก"

scene evh shizune_hcg_tied_blush:
    yalign 0.0 xalign 0.8
show evh_hi shizune_hcg_tied_hisao2:
    yalign 0.0 xalign 0.8
with flash

# "She pokes at my penis curiously with her index finger, her face reddening as she runs the rest of her fingers down its underside. Her movements are soft and curious, and they belie the embarrassed look on her face."
"เธอใช้นิ้วแตะของฉันด้วยความสงสัย หน้าเธอแดงขึ้นทุกขณะเมื่อเธอลากนิ้วอื่นที่เหลืออยู่ไปตามด้านล่าง มือเธอ\nที่ขยับสำรวจไปมาอย่างนุ่มนวลขัดกับสีหน้าเขินอายของเธอ"

show evh shizune_hcg_tied_stare
hide evh_hi
with charachange

# "It's likely Shizune is as nervous as I am, so I'm a bit relieved when she stops her exploratory prodding, but then I think about what's next to come."
"ชิซูเนะเองก็คงประหม่าไม่ต่างกับฉัน ฉันจึงโล่งใจไปเปลาะหนึ่งตอนที่เธอหยุดการสำรวจนั้น แต่แล้วฉันก็คิดถึงสิ่ง\nที่จะตามมาอีก"

# "She might try and unbutton my shirt. Who knows what she would say, seeing the scar on my chest. I'm still self-conscious about it, and I can imagine the concern on her face on seeing it; the tenting of her fingers in thought."
"เธออาจจะมาแกะกระดุมเสื้อฉัน ไม่รู้ว่าพอเห็นแผลเป็นบนหน้าอกฉันแล้วเธอจะว่ายังไง ฉันยังคิดเรื่องแผลเป็นนี้\nอยู่ตลอด พอเห็นแล้วเธอก็คงทำหน้าเครียดครุ่นคิดพลางประกบนิ้วเข้าหากัน"
#Yes I have seen the "she would say". It's fine. -SC

# "Luckily, in this position, she couldn't take off my sweater without ripping it off me. The fear fades from my mind. Now, I'm only experiencing a strange, uncomfortable mix of anticipation and nervousness."
"แต่โชคดีที่ว่าตอนนี้ถ้าจะถอดเสื้อฉันออกก็ต้องกระชากเสื้อไหมพรมนี่ออกก่อน เพราะแขนฉันไพล่หลังอยู่ ตอนนี้\nฉันจึงไม่กลัวแล้ว มีแต่ความประหม่าที่ระคนกับความคาดหวังแบบแปลก ๆ ชวนอึดอัด"

show evh shizune_hcg_tied_blush
with charachange

# "A newfound lightness on my knees brings me back to reality, and I can see Shizune standing on the tips of her toes to slide her underwear down her thighs. When she sees me looking at her, she tries to cover my eyes with one hand."
"พอเธอลุกจากหัวเข่าฉันไปฉันก็รู้สึกตัวอีกครั้ง ชิซูเนะยืนเขย่งเท้าถกกางเกงในตัวเองลงอยู่ พอเห็นว่าฉันมองเธอก็รีบ\nใช้มือข้างหนึ่งปิดตาฉัน"

# "I wonder exactly when it was that I started being attracted to her. Not just attracted to her physically, but drawn to her. And, I wonder why. She's pretty, but then, also very combative. Not just that, but she seems to like being that way."
"ฉันไปหลงเธอตอนไหนกันนะ ไม่ใช่แค่หลงเพราะรูปลักษณ์ภายนอก แต่ด้วยความเป็นเธอ ทำไมกันนะ เธอสวย\nแต่ก็เป็นคนพร้อมสู้ แถมเธอเองก็ดูจะชอบที่ได้ทำตัวอย่างนั้นด้วย"

scene evh shizune_hcg_tied_blush_small
with charachange

# "The way she's acting now, however, and at other times, doesn't really fit that image. I'm starting to think that maybe her tying my hands might have been for more reasons than just the most obvious."
"แต่การกระทำบางครั้งของเธอที่คล้ายกับตัวเธอตอนนี้กลับไม่เหมือนภาพจำอย่างนั้นสักเท่าไหร่ หรือจริง ๆ ที่มัดมือไว้\nจะมีเหตุผลอื่นนอกจากที่ว่าไม่ให้ฉันได้สื่อสารกันนะ"

# "Still, that aggressiveness that she flashes around as comfortably as a business card is real. I don't know whether or not that kind of attitude could be considered dangerous. If it is, I wonder what kind of person that makes me."
"แต่ตัวตนเธอที่เป็นคนชอบบุกซึ่งเธอแสดงให้ใครต่อใครเห็นไม่ต่างจากนามบัตรนั้นก็คือตัวเธอจริง ๆ ฉันไม่รู้ว่านิสัย\nอย่างนั้นนับว่าอันตรายหรือเปล่า ถ้าอันตรายจริง ฉันก็สงสัยแล้วว่าตัวเองเป็นคนยังไงกันแน่"

# hi "It was probably the first week I was here. A week doesn't sound so long when I think about it, but at the time it did. Even though I pretty much thought my days were numbered that week, it still seemed to go by so slowly."
hi "ฉันอยู่ที่นี่มาได้หนึ่งสัปดาห์แล้วมั้ง พอมาคิดดูแล้ว หนึ่งสัปดาห์ก็ไม่นานขนาดนั้นนะ แต่ตอนนั้นรู้สึกเหมือนนาน\nมากเลย ถึงจะคิดแล้วก็เถอะว่าฉันคงเหลือเวลาให้ใช้ชีวิตอีกไม่นาน แต่เวลาก็ผ่านไปช้าอยู่ดี"

# "Even if she can't hear me, it puts me at ease."
"แม้เธอจะไม่ได้ยิน แต่ก็โล่งใจที่ได้พูด"

# hi "I started to realize that I didn't have that much to complain about. But there's still…"
hi "ฉันเริ่มรู้สึกว่าจริง ๆ แล้วมันก็ไม่ได้แย่อะไรขนาดนั้น แต่ก็…"

# hi "Well, never mind."
hi "อืม ช่างเถอะ"

scene evh shizune_hcg_tied_stare_small
with charachange

# "She glances at me, for no reason other than that I'm talking. Because she can't understand what I'm saying, Shizune becomes increasingly flustered, but doesn't sign anything in reply."
"ชิซูเนะเหลือบมองฉันแค่เพราะเห็นว่าฉันกำลังพูด เธอยิ่งรู้สึกขัดใจเพราะไม่รู้ว่าฉันพูดอะไรอยู่ แต่เธอก็ไม่ส่งภาษามือ\nอะไรตอบ"

scene evh shizune_hcg_tied_close_small
show evh_hi shizune_hcg_tied_hisao2_small
with charachange

# "Shizune sucks in her breath sharply as she lowers herself onto my penis, trying to keep herself upright as she teeters on top of me."
"ชิซูเนะสูดหายใจเข้าแรง ๆ ขณะที่เธอประคองตัวเองหย่อนตัวลงนั่งกับของฉันโดยที่คอยยืดหลังตัวเองให้ตรงไว้"

# "The skirt of her dress covers both of our intimate parts, and traps our body heat under it like a tent. Under it, I feel unbearably hot, and Shizune's hand guiding me into her only adds to it."
"กระโปรงเธอปกปิดส่วนเร้นลับของเราทั้งสองคนไว้และกักความร้อนไว้อย่างกระโจม ตัวฉันที่อยู่ข้างใต้นั้นร้อน\nจนแทบทนไม่ไหว และมือเธอที่คอยนำทางฉันก็ยิ่งทำให้ร้อนขึ้นไปอีก"

show evh shizune_hcg_tied_kinky3_small
with flash

# "The second that I penetrate her, Shizune winces, then nearly falls on top of me. The sudden sensation is mind-numbing, and I feel waves of pleasure radiate through me from both ends of my body."
"ชิซูเนะสะดุ้งจนแทบล้มทับตัวฉันทันทีที่ฉันเข้าไปข้างในตัวเธอ ความรู้สึกที่พุ่งพล่านนี้ทำเอาประสาทชา\nความเสียวซ่านแผ่ไปทั่วร่างตั้งแต่หัวจรดเท้า"

# "It feels as if my entire lower body is enveloped in the warmth and wetness of Shizune's body, able to feel her every twitch and shudder as she starts moving."
"ราวกับว่าร่างกายท่อนล่างของฉันถูกโอบอุ้มไว้ด้วยความร้อนรุ่มและชื้นแฉะของตัวเธอ ทุกแรงกระตุกของเธอ\nเมื่อเธอเริ่มขยับส่งผ่านมายังตัวฉัน"

show evh shizune_hcg_tied_kinky2_small
with charachange

# "Shizune begins rocking her hips back and forth, at first slowly, but with her tempo increasing each time she pulls herself almost completely off of me only to plunge back down at the last second."
"เธอโยกเอวไปมา เริ่มด้วยจังหวะเนิบนาบและเร่งขึ้นทุกครั้งที่เธอยกตัวขึ้นจนแทบหลุดแล้วกระแทกกลับเข้ามา"

scene evh shizune_hcg_tied_kinky2:
    zoom 1.0 yalign 0.1 xalign 0.7
    acdc_warp 6.0 xalign 0.9
with flash

# "Being so close to her, I can see the sweat beading on her skin and the fog that forms on her glasses when they slide down her nose and too close to her mouth before she pushes them back up."
"ฉันอยู่ใกล้จนเห็นหยดเหงื่อบนผิวกายเธอและแว่นเธอที่ขึ้นฝ้าเมื่อไหลลงจนอยู่ใกล้ปากก่อนที่เธอจะดันกลับขึ้นไป"

# "Her fingertips press into my shoulders, holding on to them to steady herself, pushing against them to pull herself off of me, and then running down my arms and grasping for my wrists and hands as she pushes herself back down."
"นิ้วเธอบีบไหล่ฉันเอาไว้เพื่อประคองตัว เธอจะดันไหล่ฉันเมื่อเธอยกเอวตัวเองขึ้น จากนั้นจะเลื่อนลงมาตามแขน\nแล้วจับตามข้อมือและมือของฉันเมื่อเธอปล่อยตัวเองลงมา"

scene evh shizune_hcg_tied_close_small
with flash

# "Maneuvering around like this is difficult at best. Shizune tries to brace herself against me while pushing herself up and down with her feet. I attempt to kiss her, but only manage to succeed in touching our foreheads together, at least not painfully."
"การจะขยับไปมาด้วยท่านี้นั้นลำบากเอาการ ชิซูเนะคอยโอบฉันระหว่างที่โยกเอวตัวเองขึ้นลงพลางใช้เท้ายันไว้\nฉันพยายามจูบ แต่สุดท้ายก็ได้แค่แตะหน้าผากเข้าด้วยกัน อย่างน้อยหัวก็ไม่ได้โขกกันละนะ"

# "My thoughts wander briefly to whether or not the door is locked. If it were to open now, I'd probably have a heart attack, literally. And then there's the question of who would be opening the door."
"แวบหนึ่งสมองฉันไปพะวงเรื่องประตูว่าล็อกหรือยัง ถ้าประตูเปิดตอนนี้ฉันคงหัวใจวายแบบวายจริง ๆ ไม่ได้เปรียบเทียบ\nแล้วใครจะมาเปิดประตูกัน"

# "The sense of danger only serves to make Shizune's movements more torturous, and I wish she would speed up, but from this position, it may not even be possible."
"ยิ่งคิดถึงความสุ่มเสี่ยงนี้แล้วก็ยิ่งทำให้รู้สึกว่าชิซูเนะนั้นขยับได้ไม่ทันใจเลย อยากให้เร่งขึ้นอีกจริง ๆ แต่อยู่ท่านี้\nจะเร่งก็คงยาก"

show evh shizune_hcg_tied_kinky1_small
show evh_hi shizune_hcg_tied_hisao2_small
with charachange

# "I start moving my hips upwards in rhythm with her, trying to drive myself deeper into her. It doesn't matter to me that my movements are shaking the chair we're on, creating a loud knock as the wooden chair raps against the wooden floor."
"ฉันขยับเอวรับจังหวะกับเธอดันตัวเองเข้าไปในตัวเธอให้ลึกขึ้น ถึงการโยกจะยิ่งทำให้เก้าอี้ที่พวกเรานั่งทับกันอยู่นี้\nเคาะกับพื้นไม้จนเสียงดังฉันก็ไม่สนใจแล้ว"

$ ksgallery_unlock("evhul shizune_hcg_tied_hisao2_small")
show evh shizune_hcg_tied_kinky3_small
with charachange

# shi "…nn…!"
shi "…อื้อ…!"

# "Her breathing grows louder, and even sounds like suppressed moans escape her throat. Though it's obvious that she wants to hold them in, they're still loud enough that they would be audible to anyone standing outside the door."
"เธอหอบหนักขึ้นทั้งยังกลั้นเสียงครางไม่อยู่ แม้จะกลั้นแล้วแต่เสียงก็ยังดังชนิดที่ว่าถ้ามีคนมาอยู่ที่หน้าประตูก็คงได้ยิน"

# "I stop thrusting into Shizune, partly because it's harder to keep up with her as she starts getting more and more into it and moving faster than I can manage to match while under her."
"ฉันหยุดขยับเอวตัวเองไป ส่วนหนึ่งก็เพราะเริ่มตามจังหวะของเธอที่เน้นหนักและเร่งเร็วขึ้นเรื่อย ๆ ไม่ทันแล้ว"

window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.4)

window show

# "My heart races so quickly that I can almost hear the blood pounding in my temples, and more worryingly, I can feel a dull throb in my chest. I stop thinking about the pressure I feel between my thighs, if only for a moment."
"หัวใจฉันเต้นเร็วจนฉันได้ยินเสียงชีพจรตัวเองที่เต้นตุบ ๆ อยู่ที่ขมับ แถมยังตามมาด้วยแรงกระตุกแกน ๆ ตรงหน้าอก\nที่ทำให้ฉันใจคอไม่ดี ฉันกลั้นใจไม่นึกถึงแรงที่รัดตรงหว่างขาไปให้ได้แม้เพียงเสี้ยววินาที"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene white
with whiteout

# "That moment, though, is enough. Combined with the tightness of her squeezing herself around me and the sensation of her skin rubbing against mine, I tense up and fire off inside Shizune. A fleeting feeling of power and flight."
"แต่สิ้นเสี้ยววินาทีนั้นฉันก็กระตุกเกร็งแล้วปลดปล่อยเข้าข้างในตัวเธอเพราะแพ้ทั้งแรงตอดรัดของเธอและสัมผัสจาก\nผิวกายเธอที่แนบกับฉัน เป็นความรู้สึกชั่วแล่นที่ทำให้รู้สึกถึงแรงที่พลุ่งพล่านขึ้นมาจนคล้ายจะลอยได้"

label th_S22x:

$ renpy.music.set_volume(1.0, 2.0, channel="music")
$ renpy.music.play(music_heart, fadein=2.0, if_changed=True)

scene evh shizune_hcg_tied_close:
    yalign 0.1 xalign 0.8
show evh_hi shizune_hcg_tied_hisao2:
    yalign 0.1 xalign 0.8
with Dissolve(2.0)

# "Afterwards, I listen to the sound of my heartbeat slowing down until it reaches its normal rhythm. I listen to the sound of Shizune's breathing as it does the same."
"หลังจากนั้นฉันคอยฟังเสียงหัวใจตัวเองที่ค่อย ๆ เต้นช้าลงจนกลับมาเข้าจังหวะปกติ และฟังจังหวะการหายใจ\nของชิซูเนะที่ค่อย ๆ ผ่อนคลายลงตามกัน"

hide evh_hi
with charachange

# "Her glasses are slightly askew, and this is the first time she isn't messing around with them in some way. I want to straighten them for her, but the second I try, I'm reminded that I can't. Shizune seems to have forgotten it as well."
"แว่นเธอเบี้ยวเล็กน้อย และเป็นครั้งแรกที่เธอไม่ได้จับแว่นเธอเล่นหรืออะไร ฉันอยากจัดแว่นให้ แต่ทันทีที่จะยกมือ\nขึ้นมาก็ถึงรู้ตัวว่าทำไม่ได้ ชิซูเนะก็เหมือนจะลืมแล้วเหมือนกัน"

stop music fadeout 7.0

scene evh shizune_hcg_tied_close_small:
    truecenter
    subpixel True zoom 1.2
    easein 10.0 zoom 1.0
with Dissolve(2.0)

# "Instead of getting up, she presses herself against me in the chair to extend her reach. It's almost as if this is the only position she can think to untie my hands from. That is what I think as I feel her unbinding my wrists."
"แต่แทนที่เธอจะลุก เธอกลับเขยิบตัวเข้ามาอีกให้เอื้อมมือถึงข้อมือฉันที่ถูกมัดไว้อยู่ราวกับว่าเธอคิดท่าแก้มัดท่าอื่น\nไม่ออกแล้ว ฉันคิดไปพลางปล่อยให้เธอแก้มัด"

# "However, she doesn't get off me. Her fingers gently stroke against mine, occasionally bending inwards to run over my palms. It's funny, but I feel more connected to Shizune through this simple act than before."
"แม้จะแก้แล้วแต่เธอก็ยังไม่ลุก เธอลูบนิ้วฉันอย่างอ่อนโยนพลางงอข้อนิ้วเข้าเกากับฝ่ามือฉันเบา ๆ ตลกดี พอชิซูเนะ\nทำอะไรง่าย ๆ อย่างนี้แล้วฉันกลับรู้สึกใกล้ชิดกับเธอกว่าการกระทำเมื่อกี้อีก"

# "Shizune stays pressed against me like this for some time. It's a little uncomfortable, but it makes me feel happy, as if I could stay like this for hours."
"ชิซูเนะแนบตัวอยู่กับฉันพักใหญ่ แม้จะอึดอัดเล็กน้อย แต่ฉันก็มีความสุขจนเหมือนจะอยู่อย่างนี้ได้นานเป็นชั่วโมง ๆ"

scene black
with dissolve

label th_S23:

scene bg shizu_guesthisao
with locationchange

play music music_daily fadein 0.5

# "The days since then have passed so quickly that time seemed to slip through my fingers like water. Every time I've tried to talk with Shizune, she has been out running errands or with Misha. I feel as if she's avoiding me."
"นับแต่นั้นวันเวลาก็ผ่านไปอย่างรวดเร็วเหมือนสายน้ำที่ไหลออกจากฝ่ามือ ทุกครั้งที่ฉันนึกจะคุยกับชิซูเนะ เธอก็จะ\nออกไปทำธุระหรือไม่ก็ออกไปข้างนอกกับมิช่า รู้สึกเหมือนเธอหลบหน้ากันอยู่"

# "I'm not surprised. Of course it bothers me, but I think the way she's acting seems pretty natural. Then again, it's not like I've been through this before."
"ก็ไม่แปลกใจหรอก แน่ละว่าฉันคิดมาก ทว่าเธอก็ดูทำตัวปกติดี แต่ก็ใช่ว่าฉันเคยเจอเรื่องอะไรอย่างนี้มาก่อนที่ไหน"

scene bg shizu_living at left
show mishashort perky_smile_cas at center
with locationskip

# "Whenever I can't find Shizune, I end up running into Misha, and when I do I ask her to help me with my signing. However, she always ends up squirming out of it. We're leaving after today, so I'm determined not to let her escape this time."
"พอหาชิซูเนะไม่เจอทีไรฉันก็เจอกับมิช่าทุกที ซึ่งฉันก็ขอให้เธอสอนภาษามือให้ทุกครั้ง แต่เธอก็บ่ายเบี่ยงไปได้ตลอด\nพวกเราจะต้องกลับกันวันพรุ่งนี้แล้ว คราวนี้จะปล่อยให้หนีไปอีกไม่ได้"

# "Once we head back to school, we're probably going to have to start grinding through more student council affairs in preparation for school restarting. I want to brush up on my signing as much as possible by then, even if it's a day's worth."
"พอได้กลับโรงเรียนแล้วพวกเราก็คงต้องเริ่มไปปั่นงานสภานักเรียนเตรียมรับเปิดเทอมอีก ฉันอยากฝึกภาษามือให้คล่อง\nเอาไว้ก่อน ถึงจะเป็นการฝึกแค่วันเดียวก็ตาม"

# hi "Come on, it's pretty much just having a couple sign language conversations! You do that all the time. Actually, you're doing it right now."
hi "เถอะน่า แค่คุยภาษามือกันสองสามเรื่องเอง! เธอก็ทำภาษามือตลอดอยู่แล้ว แล้วเนี่ย ตอนนี้เธอยังทำเลย"

show mishashort cross_laugh_cas
with charachange

# mi "Wahaha~, really, Hicchan? That's funny!"
mi "วะฮ่าฮ่า~ จริงเหรอฮิจัง ตลกจัง!"

# "Misha temporarily stops her unconscious signing in order to wave her hands in front of her face in denial, but then quickly resumes gesturing everything the both of us are saying to no one in particular."
"มิช่าหยุดทำภาษามือมาโบกไม้โบกมือเป็นเชิงปฏิเสธ แต่ก็กลับไปทำภาษามือแปลสิ่งที่เราสองคนคุยกันให้ใครก็ไม่รู้อีก"

show mishashort sign_confused_cas
with charachange

# mi "Hicchan, you're so persistent. Suddenly being interested in sign language again… could it be that Hicchan wants to make a career out of it? That's not fair, that was my idea first~!"
mi "ฮิจัง นายนี่ตื๊อจริง ๆ เลยนะ อยู่ ๆ ก็มาอยากเรียนภาษามืออีก… หรือนายอยากจะเอาไปทำเป็นอาชีพ ไม่ยุติธรรมเลย\nฉันคิดได้ก่อนนะ~!"

show mishashort cross_frown_cas
with charachange

# mi "You should be careful, Hicchan. Times change too quickly~… By the time I decided I wanted to be a sign language interpreter, they had cell phones that people could type out whole paragraphs on. Amazing~! Not very good for me, though!"
mi "ระวังตัวไว้ให้ดีล่ะฮิจัง โลกมันหมุนเร็วมาก~… ตอนที่ฉันนึกอยากเป็นล่ามภาษามือ เขาก็ผลิตโทรศัพท์ที่ใช้พิมพ์แบบ\nยาว ๆ เป็นย่อหน้าออกมาแล้ว สุดยอด~! แต่ฉันใช้ไม่เป็นเท่าไหร่!"

# "As if she knows that another deferral isn't going to cut it this time, Misha changes her tune pretty quickly to a more apologetic one."
"มิช่าเปลี่ยนแนวการพูดมาเป็นการขอโทษทันทีราวกับรู้ตัวว่าบ่ายเบี่ยงอีกต่อไปไม่ได้แล้ว"

show mishashort perky_sad_cas
with charachange

# mi "I'm sorry, Hicchan, I'm just so~ tired~! Especially lately, even though being with Shicchan is fun, she has way more energy than me! Teaching on top of that would be too~ tiring; I don't have that much stamina! Sorry~!"
mi "ขอโทษนะฮิจัง พอดีฉันเหนื่อย~ มาก~! ยิ่งช่วงนี้เหนื่อยเป็นพิเศษเลย อยู่กับชิซูเนะสนุกก็จริง แต่ชิซูเนะมีพลัง\nมากกว่าฉันเยอะ! จะให้มาสอนอีกก็คงเหนื่อย~ เกินไป ฉันไม่ได้มีพลังเยอะขนาดนั้น! ขอโทษนะ~!"

# "She doesn't seem very tired, shouting the statement with her usual cheer and vigor. I know it's wrong of me to keep pestering her like this, though."
"เหมือนจะไม่เหนื่อยเท่าไหร่เลยนะ ยังมีเรี่ยวแรงตะโกนด้วยความร่าเริงได้อย่างเคยเนี่ย แต่ก็รู้แหละว่าการที่ฉันเอาแต่\nตามตื๊อเธออย่างนี้มันไม่ดี"

show mishashort sign_smile_cas
with charachange

# mi "Actually~, Shicchan and I were planning on going shopping today! It's our last chance to pick up some souvenirs."
mi "ที่จริง~ ฉันกับชิจังกะว่าวันนี้จะไปซื้อของกันแหละ! โอกาสสุดท้ายแล้วที่จะได้ไปหาซื้อของฝาก"

# hi "Souvenirs, huh? I almost forgot that I was on vacation."
hi "ของฝากเหรอ แทบลืมไปเลยว่ามาเที่ยวนะเนี่ย"

# hi "I understand what you're saying. Teaching doesn't seem so easy. Hideaki asked me to teach him how to sign and I was unbelievably lost the whole time."
hi "แต่ก็เข้าใจเธอนะ การสอนอะไรน่ะมันไม่ง่ายเท่าไหร่ ตอนฮิเดอากิขอให้ฉันสอนภาษามือให้ฉันก็งง ๆ ไปเยอะ\nเหมือนกัน"

# hi "Well, I wonder how it'll work out for you when you become a sign language teacher. You can't get tired too easily doing that."
hi "แต่อยากรู้จังเลยนะว่าถ้าเธอได้เป็นครูสอนภาษามือแล้วจะเป็นยังไง จะมาสอนแป๊บ ๆ เหนื่อยก็คงไม่ได้แล้ว"

show mishashort perky_confused_cas
with charachange

# mi "Yeah, right, right~! I hope not!"
mi "อื้ม ใช่ ใช่~! หวังว่าจะไม่เหนื่อยนะ!"

show mishashort hips_smile_cas
with charachange

# mi "Hicchan, now I'm kind of worried. But~, souvenirs! So~!, some other time, Hicchan. Aha hahaha~. Do you want us to get you something, too?"
mi "ฮิจัง ตอนนี้ฉันชักเป็นห่วงแล้วสิ แต่ว่า~ ของฝาก! เพราะงั้น~! ไว้คราวหน้าแล้วกันนะฮิจัง อะฮะฮ่าฮ่าฮ่า~ นายจะ\nฝากซื้ออะไรมั้ย"

# "Just because I understand doesn't mean I don't want her to teach me. I suppose I can't press her any further now, though. Even I'm bothered by how selfish it would seem to do so. I give up."
"บอกว่าเข้าใจแต่ใช่ว่าจะไม่อยากให้สอนให้สักหน่อย แต่จะให้ตื๊อต่อตอนนี้ก็คงไม่ได้ละนะ ขนาดฉันยังรู้สึกเหมือน\nคิดถึงแต่ตัวเองเกินไปเลย พอก่อนแล้วกัน"

# hi "No. Don't get me anything. I'm serious, don't surprise me with a funny shirt or something, okay?"
hi "ไม่อะ ไม่ต้อง จริงจังนะ อย่าซื้อเสื้อตลก ๆ หรืออะไรมาเลย โอเคนะ"

show mishashort cross_grin_cas
with charachange

# mi "Heheheh~."
mi "เฮะ ๆ ๆ ~"

# "I don't like the sound of that."
"ฟังแล้วไว้ใจไม่ค่อยไว้ใจได้เท่าไหร่เลยนะ"

hide misha
with charaexit

# "Slipping on her shoes, she yells goodbye to the otherwise empty house and opens the door to leave, letting a cool breath of fresh air into the hallway. A tuft of dark hair peeking from the door frame tells me Shizune is waiting for her outside."
"มิช่าใส่รองเท้าแล้วบอกลาแบบเสียงดัง ๆ ให้บ้านที่แทบไม่มีใครอยู่ตอนนี้ก่อนจะเดินไปเปิดประตูให้ลมเย็น ๆ พัดเข้ามา\nในโถงทางเดิน ผมสีเข้ม ๆ ที่โผล่มาจากประตูทำให้ฉันรู้ว่าชิซูเนะรอมิช่าอยู่ข้างนอก"

# hi "Good morning."
hi "อรุณสวัสดิ์"

show mishashort invis:
    center
    xpos 0.8
show shizu invis:
    center
    xpos 1.0
with None

show bg shizu_living at right
show shizu adjust_happy_cas at tworight
show mishashort perky_smile_cas at center
with Dissolvemove(2.0)

# "Misha translates for me from beyond the doorway, and Shizune turns around to give me a small wave."
"มิช่าแปลเป็นภาษามือให้อยู่ตรงหน้าประตู ชิซูเนะหันมาโบกมือทักทายน้อย ๆ"

# "Even though it's different from her usual offhand greetings in the smallest ways, there is an unmistakable hesitation there. It leaves me with a vaguely empty and distant feeling."
"ถึงการทักทายของเธอแทบจะไม่ต่างจากทุกครั้งที่ดูเย็นชา แต่คราวนี้ฉันสัมผัสได้แน่ว่าเธอแอบลังเลอยู่ ซึ่งทำให้ฉัน\nรู้สึกว่างโหวงและเหินห่างราง ๆ"

show shizu behind_blank_cas
with charachange

shi "…"

show mishashort hips_grin_cas
with charachange

# mi "Hicchan, you're up early~! Am I interrupting a conversation?"
mi "ฮิจัง นายตื่นเช้าจัง~! ฉันมากวนหรือเปล่า"

# hi "I was trying to get Misha to teach me how to talk to you, but I guess I was being impatient, and it can wait. You two were planning on going shopping today, anyway."
hi "ฉันขอให้มิช่าสอนวิธีการคุยกับเธออยู่ แต่ฉันคงใจร้อนไปหน่อยแหละ ไว้ทีหลังได้ วันนี้เธอสองคนจะไปซื้อของกันนี่"

# "Having Misha there, I forget to sign my words as I say them. Unfortunately, since Shizune moved to fill the doorway, Misha is behind her. This brief misalignment in our positions means that what I'm saying is totally lost on her."
"เมื่อมีมิช่าอยู่ฉันจึงลืมทำภาษามือตอนพูด โชคไม่ดีที่ชิซูเนะเดินเข้ามาแล้วมิช่าเลยอยู่ข้างหลังเธอ ตำแหน่งจุดยืน\nที่เพี้ยนไปชั่วขณะนี้ทำให้ชิซูเนะไม่ได้รับรู้สิ่งที่ฉันบอกเลยแม้แต่น้อย"

show shizu basic_angry_cas
with charachange

# ssh "I don't understand you at all."
ssh "ฉันไม่รู้เรื่องเลย"

# "There are things I want to say that I can't put in a way she would understand, and there are entire conversations that she could have that would go right over my head. I want to tell her now that it won't be that way for much longer."
"ฉันมีอะไรที่อยากบอกเธอแต่ไม่รู้จะบอกให้เธอเข้าใจได้ยังไง และเธอก็มีสิ่งที่เธออยากคุยกับฉันที่หากคุยกันแล้วฉันคง\nไม่เข้าใจ ฉันอยากบอกเธอว่าปัญหาเหล่านี้อีกเดี๋ยวจะไม่มีแล้ว"

hide shizu
hide mishashort
with charaexit

# "Instead, I just say “never mind” and tell them to have a good time, then wave them off."
"แต่ฉันก็พูดแค่ว่า “ช่างเถอะ ขอให้สนุกนะ” แล้วโบกมือลา"

# "It seems like everyone is out for the day, so I sit down on the biggest and most comfortable-looking chair in the living room with a book. Not a sign language book, but one of the novels I checked out of the library my first week."
"เหมือนว่าวันนี้จะไม่มีใครอยู่บ้านเลย ฉันจึงนั่งลงกับเก้าอี้ตัวที่ใหญ่ที่สุดและดูนั่งสบายอ่านหนังสืออยู่ในห้องนั่งเล่น\nไม่ใช่หนังสือภาษามือหรอก แต่เป็นนิยายที่ฉันยืมมาจากห้องสมุดตอนช่วงมาสัปดาห์แรก"

# "That was so long ago. I should really start chipping at that pile of books I borrowed, or at least return them."
"ซึ่งผ่านมานานมากแล้ว ฉันต้องไล่อ่านหนังสือที่ฉันยืมมาให้หมด หรืออย่างน้อยก็ต้องเอาไปคืนบ้าง"

stop music fadeout 2.0

show jigoro neutral at center
with charaenter

# "Sixteen pages in, Jigoro walks into the room, a stack of papers in one hand and his sword twirling idly like a baton in the other, casually shaking water from a recent shower from his hair."
"อ่านไปได้สิบหกหน้าจิโกโรก็เดินเข้าห้องมา มือข้างหนึ่งถือกระดาษมาหนึ่งตั้ง มืออีกข้างควงดาบเล่นเป็นไม้คทาพลาง\nสะบัดหัวที่เปียกมาจากการอาบน้ำให้แห้ง"

show jigoro angry
with charachange

show jigoro angry at Position(ypos=1.15)
with charamove

# "Upon being seen doing something so ungentlemanly, he freezes like a deer in the headlights, and slowly moves on to smoldering with powerful but baseless fury as he sits down on the couch a few feet away."
"เขาเหวอไปเมื่อมีคนมาเห็นเขาที่กำลังทำกิริยาไม่สมเป็นสุภาพบุรุษก่อนจะมานั่งลงที่โซฟาห่าง ๆ จากฉันพร้อม\nความโกรธรุนแรงเลื่อนลอยที่คุกรุ่นขึ้นมา"

# "This is only the third time I've met him and I'm already starting to feel nauseous on reaction. I guess in a way this could be considered a kind of charisma."
"เพิ่งได้เจอกันเป็นครั้งที่สาม แต่แค่เห็นหน้าก็คลื่นไส้ขึ้นมาแล้ว จะนับว่าเป็นรังสีข่มชนิดหนึ่งก็ได้แหละมั้ง"

# "I haven't even said anything and he already seems less than pleased. It's likely a bad idea to provoke him, and just talking to him may count as provoking him. However, I can't help thinking of the alternative situations that could play out."
"ฉันยังไม่ทันได้พูดอะไรก็หน้าบูดขึ้นมาก่อนแล้ว อย่ายั่วโมโหเขาเลยดีกว่า ซึ่งแค่การคุยกับเขาก็อาจนับได้ว่าเป็นการ\nยั่วโมโหแล้ว แต่ฉันก็ไม่รู้จะทำยังไงดีเหมือนกัน"

# "Let's say I don't open my mouth at all and walk away, maybe to go read in my room or outside. That would definitely go down as an unforgivable insult. He would probably tell me to hold it and destroy me. Either way, not too polite on my part."
"ถ้าเกิดว่าฉันเงียบปากแล้วเดินหนีไปอ่านหนังสือที่ห้องหรืออะไรก็ช่างเดี๋ยวก็กลายเป็นการหยามขั้นรุนแรงอีก เขาก็จะ\nรั้งฉันไว้แล้วเล่นงานฉัน แต่ยังไงก็เถอะ ถ้าทำอย่างนั้นมันก็ไม่มีมารยาทเท่าไหร่จริง ๆ แหละ"

# hi "What are you reading?"
hi "อ่านอะไรอยู่เหรอครับ"

show jigoro smug
with charachange

play music music_another fadein 6.0

# hx "The draft for my autobiography. It is the story of a man who wakes up to find an uninvited guest in his living room, sitting in his chair and reading shallow literary dreck."
hx "แบบร่างอัตชีวประวัติของฉันน่ะ เป็นเรื่องของชายที่ตื่นมาเจอแขกไม่ได้รับเชิญที่มานั่งอ่านนิยายน้ำเน่าเกรดต่ำ\nอยู่กับเก้าอี้ในห้องนั่งเล่นตัวเองน่ะ"

# "I've barely started reading the book, I don't even have an opinion on it yet. I can already see how this conversation is going to play out, so I might as well try to steer it in a different direction."
"เพิ่งเริ่มอ่านเอง ยังไม่ทันรู้เลยว่าเป็นอะไรยังไง แต่พอจะรู้แล้วว่าถ้าคุยต่อต้องเป็นยังไง ลองเปลี่ยนเรื่องหนีดีกว่า"

# hi "Where's Hideaki?"
hi "ฮิเดอากิอยู่ไหนครับ"

show jigoro angry
with charachange

# hx "You even ask questions rudely. Disgraceful. That aside, why would you even ask me such a stupid question? How would I know? Am I my son's keeper?"
hx "ถามอะไรหยาบคายอีกต่างหาก น่าอับอายจริง ๆ แล้วนี่ทำไมเธอถึงถามคำถามโง่ ๆ อย่างนั้น ฉันจะไปรู้ได้ยังไง ฉันเป็น\nคนเฝ้าลูกชายฉันหรือไง"

# "“Well, you are his dad, and it seems like he does live here, so…” But, I guess I can't say that, tempting as it is."
"“ก็ คุณเป็นพ่อเขา แล้วก็เหมือนเขาจะอยู่บ้านหลังนี้ด้วย ก็เลย…” แต่ต่อให้อยากพูดแค่ไหนก็คงพูดไม่ได้ละนะ"

# "I give up. I already tried to make small talk with him and failed. It's like trying to talk to a brick wall that also hates you. That is my cue to leave and sift through my wallet to see if I have enough money to go to a movie."
"ขอยอมแพ้ ลองคุยอะไรเรื่อยเปื่อยแล้วก็ล้มเหลวอยู่ดี เหมือนคุยอยู่กับกำแพงอิฐที่เกลียดขี้หน้าฉันด้วย ก็คงเป็นจังหวะ\nที่ฉันจะต้องออกไปค้นกระเป๋าสตางค์ดูว่ามีเงินพอไปดูหนังหรือเปล่า"

# "As I'm about to stand, I have second thoughts. I'm too tired to go through trying to smooth over my problematic situations by trying to continuously walk away from them."
"จังหวะที่ฉันกำลังจะลุกก็นึกอยากเปลี่ยนใจขึ้นมา ฉันเหนื่อยเกินกว่าจะเอาแต่ทำเนียนเดินหนีปัญหาตัวเองทุกอย่างแล้ว"

# "It's hypocritical of me to get upset at Misha for trying to defer things when I even run from my own girlfriend. When Jigoro attempts to stop me, I'm almost glad, even though I no longer have any intention to leave."
"ย้อนแย้งดี ทำเป็นไม่ชอบที่มิช่าเอาแต่ผัดวันประกันพรุ่งอะไร ๆ ทั้งที่ฉันก็หนีหน้าแฟนตัวเอง และตอนที่จิโกโรรั้งฉันไว้\nในใจจะเรียกว่าโล่งเลยก็ได้ ถึงจะไม่ได้อยากหนีแล้วก็เถอะ"

show jigoro neutral
with charachange

# hx "Wait."
hx "ช้าก่อน"

# "He says it with plenty of authority but nothing else, as if it's just a particularly commanding afterthought. Only a very powerful or very arrogant person can tell someone to hold on in such a manner. I'm sort of impressed."
"เขาพูดด้วยน้ำเสียงทรงอำนาจราวกับว่าจะสั่งทิ้งทวนอะไรสักอย่าง มีแต่คนที่มีบารมีจริง ๆ หรือคนที่จองหองจริง ๆ\nเท่านั้นแหละที่สั่งให้ใครหยุดอย่างนั้นได้ น่าทึ่งดีเหมือนกัน"

show jigoro smug
with charachange

# hx "You are in the Student Council with Shizune, aren't you? What is your job there?"
hx "เธอเป็นสภานักเรียนเหมือนชิซูเนะใช่มั้ย เธอมีหน้าที่อะไร"

# hi "I don't think there are specific roles, other than president. Shizune is always trying to round people up to help out here and there. Usually we might get like, one person to pitch in, but otherwise the three of us do whatever needs to be done."
hi "ก็ไม่มีหน้าที่อะไรตายตัวหรอกครับ นอกจากตำแหน่งประธานน่ะนะ ชิซูเนะจะคอยขอให้คนนั้นคนนี้มาช่วยตลอด\nปกติก็จะได้คนมาช่วยสักหนึ่งคน แต่นอกนั้นเราสามคนก็จะช่วยกันทำงานที่มีนั่นแหละครับ"

# "It's crossed my mind a couple times, around when I first met her, that Shizune's disquietingly analytical stare might be because of her deafness, but it turns out it's a trait shared by everyone else in her family."
"ฉันเคยคิดมาสองสามครั้งแล้วว่าสายตาของชิซูเนะที่จ้องพินิจชวนให้อึดอัดอาจเป็นผลมาจากการที่เธอหูหนวก\nแต่กลายเป็นว่าจริง ๆ แล้วคนในบ้านคนอื่นก็เป็น"

show jigoro neutral
with charachange

# hx "And that is okay with you?"
hx "แล้วเธอโอเคเหรอ"

# hi "Why wouldn't it be?"
hi "มีอะไรให้ไม่โอเคด้วยเหรอครับ"

show jigoro laugh
with charachange

# hx "You, Shizune, and that pink-haired girl? Is that really your entire Student Council?"
hx "เธอ ชิซูเนะ แล้วก็แม่หนูผมสีชมพูนั่นน่ะนะ สภานักเรียนมีกันแค่นั้นเหรอ"

show jigoro smug
with charachange

# hx "With a Student Council that small, they wouldn't even bother to hold elections. I am going to take a guess and say that you didn't join the Student Council, Shizune drafted you into it. You said you do not know exactly what your title is."
hx "สภานักเรียนคนน้อยขนาดนั้นคงไม่มีใครจัดเลือกตั้งแน่ ๆ ขอเดาว่าเธอไม่ได้มาเข้าร่วมสภานักเรียนเองหรอก จริง ๆ\nชิซูเนะลากตั้งเธอเข้ามาเอง เธอบอกเองนี่ว่าไม่รู้ว่าตัวเองดำรงตำแหน่งอะไร"

# hx "That makes sense. I suppose if you weren't even elected, you couldn't be expected to know. After all, if you are not elected, you aren't really anything."
hx "ซึ่งก็สมเหตุสมผลดีนะ ถ้าไม่มีใครเลือกตั้งเธอมา เธอก็คงไม่รู้ตำแหน่งตัวเอง เพราะถ้าไม่ได้ผ่านการเลือกตั้ง ก็แปลว่า\nเข้ามาแบบไม่มีตำแหน่งอะไรเลย"

show jigoro laugh
with charachange

# hx "No one is going to respect a Student Council like that. An unelected body of three people trying to scrounge up the equivalent of temp workers? It must be a sorry school if three kids having a tea party can handle every issue."
hx "สภานักเรียนอย่างนั้นน่ะไม่มีใครนับถือหรอก สภาพสามคนที่ไม่ได้ผ่านการเลือกตั้งมารีดแรงจากคนที่มาช่วย\nแบบชั่วคราวเนี่ยนะ โรงเรียนต้องอนาถาขนาดไหนถึงใช้แค่เด็กที่เล่นขายของจัดการปัญหาได้ทุกอย่าง"

# hi "What's how small it is have to do with anything? If the Student Council gets things done, isn't that enough?"
hi "เล็กใหญ่แล้วมันทำไมล่ะครับ ขอแค่สภานักเรียนจัดการอะไร ๆ ได้ก็พอแล้วนี่ครับ"

# hi "It's not just a game, either. Maybe you should actually come to the school one day. If you get there on the right days, you might even be able to see what Shizune is able to accomplish."
hi "ไม่ได้ทำกันเล่น ๆ ด้วย หาเวลามาแวะดูที่โรงเรียนบ้างก็ดีนะครับ ถ้ามาได้จังหวะก็จะเห็นด้วยว่าชิซูเนะทำอะไรได้บ้าง"

show jigoro angry
with charachange

# hx "Do you think that I have so much free time, that I can afford to waltz over to your boondocks and watch my daughter's feats of self-aggrandizement? I have never been more disgusted in my life."
hx "คิดว่าฉันว่างพอที่จะไปนวยนาดชมพวกหลังเขาอย่างเธอกับผลงานที่ลูกสาวฉันอวดอ้างนักหรือไง ไม่เคยมีใคร\nหยามฉันขนาดนี้มาก่อนเลยนะ"

# hi "What you're saying is they might as well not have a Student Council, but the fact remains there is one. And Shizune got elected to it, and for her it isn't a meaningless position. In fact, she works very hard for it."
hi "คุณบอกว่าจะมีไม่มีก็ค่าเท่ากันก็จริง แต่ยังไงมันก็มีอยู่ดีนั่นแหละครับ แล้วชิซูเนะก็ได้รับเลือกให้เป็นประธานด้วย\nเธอเองก็ไม่ได้มองว่าเป็นตำแหน่งที่ไร้ค่าอะไรเพราะทุ่มเทไปตั้งเยอะ"

show jigoro laugh
with charachange

# hx "You sound like someone who voted for her."
hx "พูดงี้คือเธอเลือกชิซูเนะมางั้นสิ"

# hi "No, I wasn't there for that."
hi "เปล่าครับ ผมไม่ได้อยู่ตอนที่เลือกตั้ง"

show jigoro neutral
with charachange

# hx "Ha. You didn't even vote for her. Well, besides that - why don't you ask Hideaki about this?"
hx "เฮอะ เธอไม่ได้เลือกให้ชิซูเนะด้วยซ้ำ แล้วเออ ลองไปถามฮิเดอากิดูสิ"

show jigoro smug
with charachange

# hx "Shizune has wanted to be a high school Student Council president since middle school. She would have him read all her practice speeches, wasting his time. For what reason?"
hx "ชิซูเนะอยากเป็นประธานนักเรียนมัธยมมาตั้งแต่ช่วงประถมแล้ว แล้วก็ไปขอให้ฮิเดอากิอ่านบทซ้อมพูดสุนทรพจน์\nให้เปลืองเวลาด้วย เพื่อ?"

# "This whole time, he hasn't even looked up from thumbing through his manuscript. It's getting increasingly frustrating."
"ปากก็พูด มือก็เปิดอ่านแบบร่างของตัวเองไม่เลิก ยิ่งเห็นยิ่งหงุดหงิด"

# hi "Because it isn't a game; we don't run the school, but it's not like we're just playing at it and not taking it seriously."
hi "ก็เพราะไม่ได้ทำกันเล่น ๆ ไงครับ คือไม่ได้เป็นคนจัดการโรงเรียนก็จริง แต่ก็ใช่ว่าจะทำแบบหยิบโหย่งขอไปทีสักหน่อย"

# "I wonder if it is so wrong to not be a purist."
"ผิดนักหรือไงที่จะไม่ใช่คนยึดติดกฎเกณฑ์ขนาดนั้นน่ะ"

show jigoro angry
with charachange

# hx "I have been to your school. Really… The students there…"
hx "ฉันเคยไปโรงเรียนเธอมาแล้วนะ ให้ตาย… นักเรียนที่นั่นน่ะ…"

# "I can already think of about a million things he might say, and I'm preparing for my heart to sink on hearing any of them. It's funny, they are probably things I've thought before."
"สมองฉันคิดถึงสิ่งที่เขาจะพูดต่อได้อีกล้านแปด และเตรียมใจเสียไว้ล่วงหน้าสำหรับทุกคำแล้วด้วย ตลกดี คำพวกนั้น\nเผลอ ๆ จะเป็นอะไรที่ฉันเคยคิดด้วยซ้ำ"

# hx "They don't even have cleaning duty."
hx "ไม่มีการจัดการเวรทำความสะอาดด้วยซ้ำ"

# "That was not what I expected at all. He's also wrong."
"โอเค ผิดคาดไปไกลโข แล้วไม่พอ เขาคิดผิดอีกต่างหาก"

# hi "They do. I should know, I get to skip out on it since I'm in the Student Council."
hi "มีสิครับ ผมรู้ว่ามีเพราะผมไม่ต้องอยู่ทำเวรเพราะเป็นสภานักเรียนเนี่ย"

show jigoro neutral
with charachange

# "The concept of being wrong confuses Jigoro. I should take this opportunity to go on the attack. It's really odd that I am thinking this way about a simple conversation."
"เหมือนจิโกโรจะสะกดคำว่าผิดไม่เป็น ต้องใช้โอกาสนี้แหละจู่โจมเขา แปลกดี คุยกันแค่นี้แต่ฉันมาคิดเรื่องโจมตีตั้งรับ\nอะไรให้มากมาย"

# hi "It sounds like the last time you were there was really some time ago."
hi "ที่ไปครั้งล่าสุดคงนานมาแล้วสินะครับ"

# hi "If you can leisurely write some memoirs, you can talk to Shizune now and then. Don't you think that she has stuff she is proud of?"
hi "ถ้ามีเวลามาลอยชายเขียนบันทึกความทรงจำอย่างนี้ ไปคุยกับชิซูเนะบ้างก็ดีนะครับ ไม่คิดเหรอครับว่าชิซูเนะจะมีอะไร\nภูมิใจอยากอวดบ้าง"

# hi "That's how young people are. We have things to be proud of. If you're writing an autobiography, you should get that."
hi "คนหนุ่มสาวก็งี้แหละครับ เราก็มีอะไรที่เราภูมิใจ ถ้ามาเขียนอัตชีวประวัติได้ก็แปลว่าคุณน่าจะเข้าใจนะครับ"

# "Such an opportunity, and I blew it. I don't know how I was expecting him to react. Maybe introspectively, but Jigoro only grows angrier by the second. Yet as he does, he also seems calmer, in a way. More sure of himself and in control."
"โอกาสดีแท้ ๆ แต่ฉันดันทำพังเสียได้ ไม่รู้เหมือนกันว่าที่พูดอย่างนั้นคาดหวังให้เขาตอบรับยังไง จิโกโรยิ่งดูโมโหขึ้น\nแต่ไม่รู้ว่าโกรธตัวเองหรือเปล่า แต่ยิ่งโกรธกลับยิ่งดูคล้ายจะเย็นลง ทำนองว่ามีความหนักแน่นควบคุมตัวเองได้ขึ้น"

show jigoro angry
with charachange

# hx "Who do you think you are to assume that my life is so easy? You haven't even read my biography, yet you are able to tell me how I should handle all my affairs, including dealing with my own daughter. You could never understand."
hx "เธอเป็นใครมาจากไหนถึงมาคิดเอาเองว่าชีวิตฉันน่ะง่ายนัก เธอยังไม่ได้อ่านชีวประวัติฉันแท้ ๆ แต่ดันมาชี้นิ้วบอกว่า\nฉันต้องจัดการเรื่องตัวเองหรือทำตัวกับลูกสาวตัวเองยังไง เธอไม่มีวันเข้าใจหรอก"

# hx "Even if I were to get up from this couch, walk over to you right now, and punch you in the forehead with brass knuckles with a condensed edition of my life story on them, leaving my biography imprinted in your face, you would not understand."
hx "ต่อให้ฉันลุกจากโซฟาตัวนี้ไปต่อยเธอด้วยสนับที่ทำจากชีวิตฉันแบบอัดขึ้นรูปจนหน้าเธอเป็นรอยแล้วเธอก็คงไม่เข้าใจ\nอยู่ดี"

# hx "For twelve years, Shizune did not even talk to me, even though I hired multiple tutors and interpreters of all sorts for her to try and get her to become normal. It isn't as simple as you think it is."
hx "สิบสองปีมาแล้วที่ชิซูเนะไม่คุยกับฉันเลย ทั้งที่ฉันจ้างติวเตอร์หรือล่ามสารพัดมาให้เธอกลับเป็นปกติแล้วแท้ ๆ ไม่ได้\nง่ายอย่างที่เธอคิดหรอกนะ"

show jigoro smug
with charachange

# hx "If she does not want to bother with me, then fine. I assume that is normal. When was the last time you talked to your parents?"
hx "ถ้าชิซูเนะไม่อยากยุ่งกับฉันก็ไม่เป็นไร ก็คงเป็นเรื่องปกติแหละ เธอคุยกับพ่อแม่ครั้งล่าสุดเมื่อไหร่ล่ะ"

# "It has been a while, and I feel ashamed. More so that he caught me than at how easily I could have dropped my parents a phone call or sent them an e-mail, or even a letter, and haven't. This knowledge only makes me feel more ashamed."
"ก็สักพักแล้ว ขายหน้าขึ้นมาเลยแฮะ แล้วก็คงรู้ด้วยว่าการจะติดต่อกับพ่อแม่ฉันไม่ใช่เรื่องยากเลย แค่โทรไปหรือ\nส่งอีเมลไปก็พอ หรือจะส่งจดหมายก็ยังได้ แต่ฉันก็ไม่ทำ ยิ่งคิดฉันยิ่งขายหน้า"

show jigoro laugh
with charachange

# hx "I thought so."
hx "ว่าแล้วเชียว"

# hi "If I wanted to see my parents, I couldn't. This is different. You aren't that far from her, it's one train ride away!"
hi "แต่ใช่ว่าผมจะไปเจอหน้าพ่อแม่ได้ตามใจอยากนี่ครับ ไม่เหมือนคุณที่แค่นั่งรถไฟเที่ยวเดียวก็ไปหาได้แล้ว!"

show jigoro neutral
with charachange

# hx "That is enough. No means no. You are very persistent. If only it was about something that mattered. I can't see what you may have learned from my daughter aside from that and how to backtalk people. Is that it?"
hx "พอเลย ไม่ก็คือไม่ เธอนี่รั้นจริง ๆ ถ้าเอาความรั้นไปใช้อะไรที่เกิดประโยชน์คงดี นี่เธอไม่ได้เรียนรู้อะไรจากลูกสาวฉัน\nนอกจากการเถียงคนเลยเหรอ มีแค่นั้นจริง ๆ เหรอ"

stop music fadeout 10.0

# "The answer is yes. I wasn't this persistent or argumentative before meeting Shizune and Misha. After all, prior to meeting them, I'd just experienced a small death. It's a mystery as to why I refused to join the Student Council in the first place."
"ใช่ครับ ก่อนมาเจอชิซูเนะกับมิช่าฉันไม่ใช่คนรั้นหรือเถียงคนเก่งขนาดนี้ ก็ก่อนทีี่ฉันจะมาเจอสองคนนั้นสิ่งที่ฉันเจอ\nก็มีแค่ความเกือบตาย แปลกจริง ทำไมฉันถึงไม่ยอมเข้าสภานักเรียนแต่แรกกันนะ"

#if not seen A2b:
label th_S23a:

# "It took monumental effort just to introduce myself on my first day there. I might have rolled over for anyone and any cause. It might have just been chance that Student Council appealed to me so little that I would fight it."
"แค่แนะนำตัววันแรกฉันก็ต้องรวบรวมแรงมหาศาลก่อนพูด ถ้าจะคล้อยตามใครต่อใครหรือสิ่งใด ๆ ก็คงไม่แปลก สงสัย\nเพราะบังเอิญว่าสภานักเรียนมันไม่น่าเข้าถึงขั้นที่ฉันต้องต่อต้าน"

#End conditionals

label th_S23x:

# "Possibly it was from trying to get away from their nagging so much that I was able to get my energy back. It's a cute idea."
"อาจจะเพราะฉันคอยหนีจากความจู้จี้ของสองคนนั้นจนแรงฉันฟื้นขึ้นมา คิดแล้วขำดี"

# "I think again about why I'm still here. Arguing with Jigoro is pointless, yet I think I almost looked forward to it. And he is right, I cannot understand him. Even if I did, he wouldn't care. I'm a louse that crawls on a whale: wholly insignificant."
"ฉันย้อนคิดว่าทำไมตัวเองถึงไม่ไปไหน เถียงกับจิโกโรไปก็ไร้ประโยชน์ แต่เหมือนฉันอยากจะเถียง และเขาพูดถูก\nฉันไม่เข้าใจเขาเลย ต่อให้ฉันเข้าใจเขาก็คงไม่สนใจอยู่ดี เพราะฉันไม่ต่างอะไรกับเห็บที่คลานบนหลังวาฬ เป็นสิ่งซึ่ง\nไร้ความสำคัญโดยสิ้นเชิง"

# "He has a confidence that I don't have. Shizune does, and it could be that the reason why I am here now, in an almost-shouting match with her father, is because some of that bravery has rubbed off onto me. However, I don't have anything to keep it going."
"ฉันไม่เหมือนเขาที่มีความมั่นใจ ชิซูเนะเองก็เช่นกัน และเพราะฉันคงติดความกล้ามาจากเธอบ้างแล้วฉันถึงได้ยังมา\nเถียงคอเป็นเอ็นอยู่กับพ่อของเธอตรงนี้ แต่นอกจากความกล้าแล้วฉันก็ไม่มีอะไรที่จะใช้เถียงเลย"

# "Still, I hate him. I don't know what I can do. A few months ago, I think I would have punched him and let the consequences play out as they may. But now, I can't risk it. If he were to hit me back, he'd likely kill me."
"แต่ฉันเกลียดเขา ไม่รู้ด้วยว่าจะทำอะไรได้บ้าง ถ้าเป็นสองสามเดือนก่อนฉันคงอัดเขาแล้วปล่อยให้ตัวเองไหลไปกับผล\nที่ตามมา แต่ตอนนี้ฉันจะทำอะไรเสี่ยง ๆ อย่างนั้นไม่ได้แล้ว ถ้าเขาทำฉันกลับคงเล่นเอาถึงตาย"

# "So in the end, the only thing I can do is look at Jigoro in silence, knowing that I have no reply, and hate him, and feel completely at a loss. Oddly, he takes it as defiance."
"สุดท้ายฉันก็ได้แต่มองหน้าเขาอยู่เงียบ ๆ เพราะไม่มีอะไรจะโต้ตอบโดยที่ในใจยังมีความสับสนและความรู้สึกเกลียดเขา\nซึ่งน่าแปลกที่เขาตีความไปว่าฉันกำลังต่อต้านเขาอยู่"

show jigoro angry
with charachange

# hx "Hmph. Fine, then. Have fun with that."
hx "ฮึ ก็ได้ ขอให้สนุกแล้วกัน"

show jigoro invis at center
with dissolvecharamove

# "Picking up his sword and using it to pull himself to his feet, he turns and casually saunters out of the room. I want to throw my book after him, but I'm happy to finally be alone, even if I'm not in the mood to read any longer."
"เขาใช้ดาบค้ำตัวเองลุกขึ้นยืนแล้วเดินออกไปสบาย ๆ อยากจะปาหนังสือไล่หลังไปด้วยจริง ๆ แต่ได้อยู่คนเดียวเสียที\nก็ดีแล้วละ ถึงจะไม่มีอารมณ์อ่านอะไรแล้วก็เถอะ"

scene black
with dissolve

label th_S24:

scene bg city_station
with locationchange

# "Our return trip to the school keeps getting delayed in one way or another. Shizune and Misha come back so late that there's no use even leaving and we end up staying another day."
"มีเหตุที่ทำให้เรากลับโรงเรียนช้าไปเรื่อย ๆ อย่างแรก ชิซูเนะและมิช่ากลับบ้านค่ำเสียจนออกบ้านไม่ได้อีกจนสุดท้าย\nต้องอยู่ต่ออีกวัน"

# "The morning after, we miss the train by a single minute and then the next two don't arrive. We miss the fourth train because I wandered off to get a drink in the meantime. Shizune wasn't very happy about that."
"เช้าวันรุ่งขึ้นก็ตกรถไฟไปหนึ่งนาที อีกสองขบวนต่อจากนั้นก็ไม่มา และตกขบวนที่สี่เพราะออกไปหาอะไรดื่ม ซึ่ง\nชิซูเนะไม่พอใจเท่าไหร่นัก"

scene bg school_dormhisao
with shorttimeskip

play music music_dreamy fadein 2.0

# "By the time I finally get back to my room, I feel so tired, even though I spent most of the ride back sleeping. I can't say it's only because of today; this seems like a familiar symptom of traveling. It's not the first time it's happened."
"กว่าจะกลับถึงห้องก็เล่นเอาเหนื่อยทีเดียว ทั้งที่หลับมาเกือบตลอดทางแล้วแท้ ๆ จะว่าเป็นเรื่องที่เกิดแค่วันนี้ไม่ได้หรอก\nเพราะเหมือนได้เดินทางทีไรก็เป็นอย่างนี้ทุกที ครั้งนี้ไม่ใช่ครั้งแรกเลย"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide

scene black
with shuteye

window show

# "If no one has beaten me to it, I could do a thesis on it, maybe get in a medical journal. “Returning From A Trip Syndrome.” Not very creative. I fall asleep before I can think of a better name."
"ถ้ายังไม่มีใครทำก็น่าจะเขียนวิทยานิพนธ์เรื่องนี้ได้ อาจจะเอาไปตีพิมพ์ลงวารสารการแพทย์ “กลุ่มอาการป่วยการเดินทาง”\nฟังดูไม่สร้างสรรค์เท่าไหร่ แต่ฉันก็ผล็อยหลับไปก่อนที่ทันจะได้คิดชื่อที่ดีกว่านั้น"

window hide

play sound sfx_doorknock
with Pause(1.0)

scene bg school_dormhisao
with openeye

$ renpy.music.set_volume(1.0, 1.0, channel="music")

window show

# "A loud knock on my door wakes me up only a few hours into my nap. I'm annoyed because I had just been in the middle of a dream that I can't remember, having been woken up in the middle of it. But I'm sure it was a good one."
"งีบได้ไม่กี่ชั่วโมงก็มีเสียงเคาะประตูที่ทำฉันสะดุ้งตื่น ฉันนึกหงุดหงิดเพราะต้องตื่นตอนที่กำลังฝันอะไรสักอย่างซึ่งฉัน\nจำไม่ได้อยู่ แต่ต้องเป็นฝันที่ดีแน่ ๆ"

# "I briefly wonder who it could be, but it's not like I get many visitors, so I'm sure it's Kenji. I hope he is just rolling out the welcome wagon and not going to hit me up for money again. If that was the case I'd be almost touched."
"ฉันคิดแวบหนึ่งว่าจะเป็นใครได้ แต่ก็ใช่ว่าจะมีคนมาหาฉันเยอะแยะขนาดนั้นน่ะนะ คงเป็นเคนจินั่นแหละ หวังว่าจะมา\nแค่ฉลองต้อนรับกลับแล้วไม่ได้มายืมเงินนะ ถ้ามาฉลองจริงนี่ฉันคงซึ้งเลยแหละ"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene black
with shuteye

# "Not touched enough to fight off the urge to roll over and go back to sleep, though."
"แต่ก็ไม่ได้ซึ้งพอที่จะทำให้ฉันลุกไปจากที่นอนได้อะนะ"

stop music fadeout 5.0

window hide

with Pause(4.0)

scene bg school_dormhisao
with openeye

window show

# "A few hours after that, I wake up again and immediately spot an envelope on the floor."
"ไม่กี่ชั่วโมงให้หลังฉันก็ตื่นมาอีกครั้ง สายตาเหลือบไปเห็นซองจดหมายที่วางอยู่กับพื้น"

# "It must be something that came in the mail while I was away. That's Shizune and Misha's department, so I wonder if they dropped by to give it to me, or maybe someone filled in for them in their absence and told Kenji to pass it along…"
"คงมาอยู่ในกล่องจดหมายช่วงที่ฉันไม่อยู่มั้ง ซึ่งปกติชิซูเนะและมิช่าจะเป็นคนจัดการ สองคนนั้นแวะมาหย่อนให้\nที่ห้องฉันหรือเปล่านะ ไม่ก็ใครสักคนมารับหน้าที่ช่วงที่สองคนนั้นไม่อยู่แล้วฝากเคนจิเอามาให้…"

show letter_insert:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_rain fadein 4.0

# "When I pick it up, any remnants of sleepiness in me instantly vanish."
"พอหยิบขึ้นมาดูฉันก็หายง่วงเป็นปลิดทิ้ง"

# "Even if the name of the sender wasn't on it, I would have known whom it was from by looking at the envelope itself, realizing why it looked so familiar. By recognizing the delicate handwriting addressing it."
"แม้ไม่มีชื่อผู้ส่ง แต่ดูแค่ซองจดหมายฉันก็รู้แล้ว มิน่าละถึงได้คุ้นตาเหลือเกิน เพราะลายมือแสนบรรจงที่ใช้เขียนที่อยู่\nบนซองจดหมายนี่เอง"
#This directly contradicts everyone else's take on things. I don't think it's worth changing though, since moving it back in time to the proper place would wreck what in our circles passes for "plot" forever. :p -SC

# "It's from Iwanako. At first, I can't believe it, but it wouldn't be too hard for her to track me down if she wanted to."
"อิวานาโกะเป็นคนส่งมา แวบแรกฉันยังไม่เชื่อ แต่ถ้าเธอจะตามที่อยู่ฉันจริง ๆ ก็คงไม่ยากอะไร"

# "Of course, I hadn't thought that she would want to. She was maybe my girlfriend for all of five seconds. After that, we barely spoke to each other."
"แน่ละ ฉันไม่คิดว่าเธอจะอยากลงทุนตามที่อยู่ฉันขนาดนั้น ก็เธอได้เป็นแฟนฉันสักห้าวินาทีได้เองมั้ง แล้วหลังจากนั้นก็\nแทบไม่ได้คุยกันเลย"

show letter_insert:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide letter_insert
with None

# "It would be too easy to put this letter away somewhere and forget about it. A part of me wants to do that. Or throw it away, unread. Why I want to do these things, I don't know. It would be easy to do them. Easier than to read it."
"จะให้เก็บจดหมายนี้ไว้สักที่แล้วลืม ๆ ไปก็กระไรอยู่ ใจหนึ่งฉันก็อยากทำอย่างนั้น ไม่ก็ทิ้ง ๆ ไปเลยโดยที่ไม่ต้องเปิดอ่าน\nฉันเองก็ไม่รู้ว่าทำไมถึงอยากทำอย่างนั้น คงเพราะการทิ้งไปอย่างนั้นจะง่ายกว่าการเปิดอ่าน"

scene ev hisao_letter_open
with locationchange

# "Slitting the envelope open with the tip of a pen, I'm surprised by the length of the letter that spills out."
"ฉันใช้ปลายปากกากรีดซองจดหมายให้เปิดออก แล้วก็ต้องตกใจกับความยาวของตัวจดหมายที่ออกมาจากซองนั้น"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide

# $ written_note("Dear Hisao,\n\nHow are you? I hope you are well and happy at your new school. Everyone here misses you. Almost all of our second-year class got put together in class 3-1 for the final year, so we are pretty comfortable right from the beginning of the year. I'm sure you would've been assigned to this class as well.")
$ written_note("ถึง ฮิซาโอะ\n\nเป็นยังไงบ้าง หวังว่านายจะสบายดีมีความสุขกับ\nโรงเรียนใหม่นะ คนที่นี่คิดถึงนายกัน พวก\nนักเรียนม. 5 พอได้ขึ้นชั้นมาอยู่ม. 6 ก็ได้ย้ายมาอยู่\nห้อง 3-1 กันเกือบหมด ก็เลยอยู่กันอย่างอบอุ่น\nแต่ต้นปีการศึกษาเลย ถ้านายยังอยู่ก็คงได้มาเรียน\nห้องเดียวกันเหมือนกัน")
 
# $ written_note("The mood among the third-years seems to be very anxious about the final exams, even though they are so far away. The teachers are badgering us about it all the time - even old Mr. Tachibana who is, by the way, our homeroom teacher this year. Would you believe it? I was sure that he'd retire after our second year, but here he is, nagging everyone about studying for exams.\n")
$ written_note("นักเรียนม. 6 ดูจะเครียดเรื่องสอบปลายภาคกัน\nถึงจะยังอีกนานก็เถอะ คุณครูก็เอาแต่ตามย้ำอยู่\nนั่นแหละ ขนาดครูทาจิบานะยังเป็นไปกับเขาเลย\nแล้วก็เนี่ย เชื่อมั้ยว่าปีนี้แกได้เป็นครูประจำชั้นห้อง\nของเราด้วยนะ ฉันก็กะไว้แล้วแท้ ๆ ว่ายังไงพอ\nขึ้นชั้นมา แกก็คงเกษียณไปแล้ว แต่ก็ไม่\nมายืนจิกหัวให้อ่านหนังสือสอบอยู่เนี่ย\n")
 
# $ written_note("I think things like that are the main reason why the mood among the third-years is so nervous. I must admit that I'm somehow losing confidence in myself as well, even though I've always fared reasonably well in exams.\n\n\n\n\n")
$ written_note("ฉันว่าเพราะอย่างนั้นแหละพวกม. 6 เลยร้อนรน\nกัน ฉันก็ต้องยอมรับเหมือนกันว่าฉันเองก็ชักจะ\nไม่มั่นใจขึ้นมาแล้ว ถึงปกติจะสอบได้คะแนนเยอะ\nพอตัวตลอดก็เถอะ\n\n\n\n\n")
 
$ renpy.music.set_volume(1.0, 1.0, channel="music")

window show

# "The small talk makes me feel nostalgic. It's almost like I'm in the hospital again. Every now and then Iwanako would drop by and give me the gist of what was going on in a class that, even then, I had an inkling that I would never return to."
"พอเธอเล่าอย่างนี้แล้วก็ชวนให้คิดถึงรู้สึกเหมือนได้กลับไปอยู่โรงพยาบาลอีกครั้งเลย ตอนนั้นเธอจะคอยแวะมาเยี่ยม\nแล้วเล่าให้ฟังว่าในห้องเป็นยังไงบ้าง ซึ่งแม้แต่ตอนนั้นฉันก็รู้สึกได้แล้วว่าคงไม่ได้กลับไปอีก"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide

# $ written_note("It's so weird to think we are already seniors, isn't it? Time has really flown past. I wonder where it went. The new first-years seem so young and somehow really innocent. I keep wondering if I was like them in my first year. I've been feeling nostalgic like this for the whole first trimester.\n\n\n")
$ written_note("แปลกเนอะ รู้ตัวอีกทีก็ม. 6 แล้ว เวลาผ่านไปไว\nจริง ๆ ผ่านไปไหนกันนะ นักเรียนม. 4 น่ะดูทั้ง\nยังเด็กแล้วก็ใสซื่อดี ตลอดเทอมแรกนี้ฉันเอาแต่\nย้อนคิดตลอดเลยแหละว่าสมัยอยู่ม. 4 ฉันก็เป็น\nอย่างนั้นด้วยหรือเปล่า\n\n\n")

show ev hisao_letter_open:
    "ev hisao_letter_open_2" with locationchange
with None
$ ksgallery_unlock("ev hisao_letter_open_2")

# $ written_note("There are other things I want to say. I'm writing to you because I felt that there are things I should've said after the incident back in winter. I really regret that I wasn't able to say them in person, and I have no excuse for it.\n\n\n\n\n")
$ written_note("ยังมีอย่างอื่นที่ฉันอยากพูดถึงอีก ฉันเขียนจดหมาย\nส่งมาหานายเพราะรู้สึกเหมือนพอเกิดเรื่องนั้นแล้ว\nฉันคงต้องพูดอะไรหน่อย ฉันเสียใจจริง ๆ ที่ฉันมา\nพูดกับนายต่อหน้าตรง ๆ ไม่ได้ และฉันก็ไม่มี\nข้อแก้ตัวอะไรทั้งนั้น\n\n\n\n\n")
 
# $ written_note("The truth is, the times when I visited you at the hospital made me worried about you. I am not talking about your health. You seemed to become more distant and disheartened. It was natural after something like that happened, I'm sure, but somehow I got the feeling that you had given up on something back then. Happiness, maybe?\n")
$ written_note("ที่จริงคือ ตอนฉันไปเยี่ยมนาย ฉันก็เป็นห่วงนาย\nขึ้นมา ไม่ได้หมายถึงสุขภาพนายนะ แต่นายดูทั้ง\nห่างเหินทั้งไร้เรี่ยวแรง ฉันรู้อยู่ว่าพอเกิดเรื่อง\nอย่างนั้นแล้วจะเป็นแบบนั้นไปก็คงไม่แปลก แต่\nตอนนั้นฉันรู้สึกเหมือนนายถอดใจกับอะไร\nบางอย่างไปแล้ว ความสุข ละมั้ง\n")
 
# $ written_note("I wanted to somehow express my feelings, but the right words didn't come to me. I couldn't say anything to comfort you. I am really sorry for not being able to support you when it mattered the most, even though I like you so much. At least now, finally, I can be more honest.\n\n\n\n")
$ written_note("ฉันอยากบอกความรู้สึกให้นายได้รู้ แต่ก็นึกหาคำ\nไม่ได้เสียที ฉันพูดอะไรปลอบใจนายไม่ได้เลย ฉัน\nขอโทษจริง ๆ ที่คอยเป็นแรงใจให้นายยามที่นาย\nต้องการแรงใจที่สุดไม่ได้ ทั้งที่ฉันชอบนายมาก\nแท้ ๆ แต่อย่างน้อยตอนนี้ฉันก็พูดตรง ๆ ขึ้นมา\nได้บ้างแล้ว")

$ renpy.music.set_volume(1.0, 1.0, channel="music")

window show

# "What a convenient time for her to rediscover her sincerity. Well, even as I think that, I know she's right. “Distant and disheartened” is a good way to describe it. And maybe I had given up, too."
"มาหาความจริงใจเจอได้ถูกเวลาจริง ๆ แต่ถึงอย่างนั้นก็เถอะ ฉันรู้ว่าเธอพูดถูก การที่เธอบอกว่าฉัน “ทั้งเหินห่าง\nทั้งไร้เรี่ยวแรง” ก็ถูกแล้ว ฉันเองก็คงถอดใจไปแล้วด้วย"

# "It weighs on my heart when I think back to when I was lying in the hospital, feeling so bitter when she finally stopped showing up. I wasn't surprised, and I had no right to be. How could she not stop coming when it was the only expectation I had of her?"
"พอคิดถึงตอนที่ฉันนอนอยู่ที่โรงพยาบาลแล้วในใจก็หนักอึ้งขึ้นมา ยังรู้สึกขมขื่นเมื่อนึกถึงเวลานั้นที่เธอไม่มาหาอีกเลย\nตอนนั้นฉันไม่แปลกใจเลย และไม่มีสิทธิ์อะไรจะแปลกใจด้วย ในเมื่อสิ่งเดียวที่ฉันคาดหวังกับเธอคือการที่เธอมาหา\nเธอจะไม่มาอีกเลยก็ไม่แปลก"

# "She dropped by only for all of six weeks after the incident. If I drifted away from her, it was because I could feel her already moving herself away from me the moment she showed up."
"เธอมาเยี่ยมฉันเป็นระยะเวลาหกสัปดาห์หลังเหตุการณ์ครั้งนั้นเท่านั้น ถ้าฉันออกห่างจากตัวเธอจริง ก็คงเพราะฉันเอง\nที่รู้สึกว่าเธอนั้นเริ่มเคลื่อนห่างออกจากฉันทันทีที่ได้เห็นหน้าเธอ"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide

# $ written_note("If I could go back to those quiet days in February and March, I'd tell you to not give up on yourself. That's what I would say. Maybe you wouldn't have drifted so far away if I had just said something. I hope you've managed to get back on your feet on your own.\n\n\n\n")
$ written_note("ถ้าฉันกลับไปช่วงเดือนกุมภาพันธ์กับเดือนมีนาคมที่\nเงียบสงบนั้นได้ฉันก็อยากบอกนายว่าอย่ายอมแพ้\nนะ ฉันจะบอกอย่างนั้น ถ้าฉันพูดอะไรบ้างนายคง\nไม่ออกเหินห่างไปขนาดนี้ ฉันอยากให้นายลุกขึ้น\nมายืนด้วยตัวเองให้ได้\n\n\n\n")
 
# $ written_note("Now that the distance between us is also physical, it also feels more final, somehow. I wonder if we will meet again. Perhaps it's for the best if we don't? Still, if you would like to correspond with me, by all means write me back. I'd very much like to hear about your new school and how you are doing. I wish you all the best.\n\nSincerely, Iwanako")
$ written_note("แล้วยิ่งทีนี้ห่างกายกันด้วยก็ยิ่งรู้สึกเหมือนเป็นจุด\nส่งท้ายจริง ๆ ยังไงไม่รู้ เราจะได้เจอกันอีกไหมนะ\nหรือถ้าไม่เจอกันอีกเลยจะดีกว่ากันนะ แต่ถ้ายัง\nอยากติดต่อกับฉันอยู่ก็เขียนส่งกลับมาได้เลยนะ\nฉันยินดีมากที่จะได้ฟังเรื่องโรงเรียนใหม่กับ\nชีวิตใหม่ของนาย ขอให้มีความสุขดีนะ\n\nจากใจ อิวานาโกะ")

$ renpy.music.set_volume(1.0, 1.0, channel="music")

window show

# "It's a strange feeling. I know that I'm never going to hear from her again."
"เป็นความรู้สึกที่ประหลาดดี ที่ได้รู้ว่าฉันจะไม่ได้รับข่าวคราวอะไรจากเธออีกแล้ว"

# "If she really wanted to keep in touch, she wouldn't have picked a medium like snail mail to do it through. If she could get my address, then my e-mail or phone number wouldn't have been much more work, had she wanted them. This is only a goodbye."
"ถ้าเธอยังอยากติดต่อกันจริง ๆ ก็คงไม่เลือกส่งจดหมายไปรษณีย์มาอย่างนี้ เพราะถ้าตามที่อยู่ฉันได้ เธอก็คงตาม\nอีเมลหรือเบอร์โทร. ฉันได้ด้วยถ้าจะตามจริง ๆ ที่ส่งจดหมายมาคราวนี้เธอก็แค่จะลากันเท่านั้น"

stop music fadeout 4.0

# "I exhale, only just now becoming aware that I had been reading with bated breath. Now who's being distant, Iwanako? But maybe it really is for the best."
"เมื่อถอนหายใจก็เพิ่งรู้ตัวว่าเมื่อกี้อ่านจดหมายแบบหายใจไม่เต็มปอดอยู่ ไหน ทีนี้ใครกันแน่ที่เหินห่าง อิวานาโกะ\nแต่ให้เป็นอย่างนี้ก็คงดีที่สุดแล้วจริง ๆ"

# "For her to pick up a pen and write this letter to me, it can only be because she felt guilty about how things ended. That she was hurt by how we floated out of each other's lives makes me feel a sort of wistful happiness."
"ที่จับปากกามาเขียนจดหมายส่งมาหากันอย่างนี้ก็คงแค่เพราะรู้สึกผิดที่เรื่องจบไปอย่างนั้นน่ะแหละ พอคิดว่าเธอเอง\nก็เจ็บปวดที่เราสองคนลอยห่างออกจากวงโคจรของกันและกันอย่างนี้แล้วฉันก็รู้สึกสุขอย่างเศร้าสร้อยขึ้นมา"

# "I almost want to thank her, and I only don't because I know she wouldn't want me to reply."
"อยากจะขอบคุณเธอจริง ๆ แต่ก็ไม่ได้ขอบคุณเพราะรู้ว่าเธอคงไม่อยากให้ฉันเขียนตอบเธอไป"

play sound sfx_doorknock

scene bg school_dormhisao
with locationchange

# "There's a knock at my door, then it opens anyway about a millisecond later. I forgot to lock it, stupidly."
"เสียงเคาะประตูดังขึ้น ไม่กี่เสี้ยววินาทีถัดมาประตูก็เปิดออก โง่ลืมล็อกเสียได้"

# ke "Sup, man? Why's your door open?"
ke "ไงพวก ไหงไม่ล็อกประตูเนี่ย"

# "I run to the door faster than is probably medically safe for me to do so I can prevent Kenji from seeing the mountains of pills just a couple feet away from him, blocked from his sight only by the door."
"ฉันพุ่งตัวไปที่ประตูด้วยความเร็วเกินหมอกำหนดเพื่อกันไม่ให้เคนจิเห็นกองยาที่อยู่ห่างจากตรงหน้าเขาไปราวครึ่งเมตร\nซึ่งก่อนหน้านี้มีเพียงประตูที่กั้นไว้ไม่ให้เห็น"

# "Then there's the letter I'm holding. If he asks about it, I don't think I could make up anything convincing."
"ตอนนี้ในมือฉันก็มีจดหมายอีก ถ้าเกิดเขาถามขึ้นมาฉันคงแต่งเรื่องอะไรที่น่าเชื่อไม่ได้แน่ ๆ"

# "About two feet away from him I realize that his vision is so bad that it was probably never an issue. He didn't even see me about to practically tackle him back through the door frame."
"เมื่อเข้าใกล้เขาได้ราวครึ่งเมตรแล้วฉันก็ถึงคิดได้ว่าสายตาเขานั้นย่ำแย่ชนิดที่ว่าคงไม่ต้องห่วงว่าจะเห็นอะไรเข้า เขายัง\nไม่เห็นฉันที่พุ่งตัวเตรียมเข้าชนให้เขาถอยห่างจากประตูด้วยซ้ำ"

scene bg school_dormhallway
show kenji tsun_close at center
with locationchange

play music music_kenji fadein 0.5

# ke "Hey, what the hell, man?"
ke "เฮ้ย อะไรเนี่ย"

# hi "What are you talking about? Your room has a billion locks on it, yet you just barge right through other people's doors."
hi "พูดอะไรของนาย ห้องนายล็อกเป็นล้านชั้น แต่เวลาเข้าห้องคนอื่นดันบุกเข้ามาอย่างนี้เลยอะนะ"

# hi "You didn't even wait a second after knocking before you tried the door, it was like, simultaneous. You were already opening the door while you were knocking on it."
hi "แล้วเคาะได้ไม่ถึงวิก็บิดลูกบิดมาก่อนแล้ว แทบจะเคาะแล้วบิดเปิดประตูเข้ามาเลยมั้ง"

show kenji happy_close
with charachange

# ke "See? That's exactly why I have all those locks. It's a cold and uncaring world out there, a gate crasher's world. Now you also understand."
ke "เห็นมั้ย เนี่ยฉันถึงได้ล็อกห้องตัวเองขนาดนั้น โลกมันโหดร้ายทารุณนะเว้ย โลกของคนพังประตู ทีนี้นายก็เข้าใจด้วย\nสักที"

show kenji neutral_close
with charachange

# ke "I just taught you a valuable lesson, dude. Knowledge is power. Why are you yelling at me? I'm a hero."
ke "ฉันให้บทเรียนอันล้ำค่าแก่นายไปนะ ความรู้คือพลัง ตะโกนใส่กันทำไม ฉันคือวีรบุรุษนะเว้ย"

show kenji tsun_close
with charachange

# ke "Look at you… you didn't even lock your door. The average woman could have killed you a billion times already, then replaced you with a female clone indistinguishable from the original. It almost happened to me."
ke "แล้วดูเนี่ย… นายไม่ได้ล็อกประตูเลยด้วยซ้ำ ถ้าเป็นผู้หญิงทั่วไปคงฆ่านายตายไปเป็นพันล้านรอบแล้วหาร่างโคลนผู้หญิง\nที่เหมือนตัวต้นแบบทุกกระเบียดนิ้วมาอยู่แทน ฉันเคยเกือบเป็นอย่างนั้นมาแล้ว"

# "Ignoring the latter part, since it's too confusing, it's funny he should say that. He was unable to stop me from tackling him head-on, yet apparently a woman could have killed me a billion times. If this man is a hero, we are all doomed."
"ไอ้ท่อนหลัง ๆ ช่างก่อนเพราะฟังแล้วงง ๆ แต่ที่เหลือฟังแล้วก็ตลกดี ตัวเองก็หยุดฉันที่เข้ามาเบียดเขาไม่ได้ แล้วก็\nบอกว่าถ้าเป็นผู้หญิงคงฆ่าฉันไปพันล้านรอบ งี้ถ้าเขาเป็นวีรบุรุษจริง พวกเราคงตายห่ากันหมด"

show kenji happy_close
with charachange

# ke "What's that you've got there?"
ke "ที่ถืออยู่นั่นอะไร"

# "Somehow, he is able to see the letter still in my hand. With how I've been waving it around, that is no surprise. I fold it back up quickly, but take care not to whip it behind my back or anything else. That would be too suspicious."
"แต่เขายังเห็นจดหมายที่อยู่ในมือฉันอยู่แฮะ แต่โบกไปมาขนาดนั้นจะเห็นก็ไม่แปลก ฉันรีบเก็บทันที แต่ก็คอยระวัง\nไม่ให้ขยับเป็นท่าเอามือไพล่หลังไว้หรืออะไร ไม่อย่างนั้นจะน่าสงสัยเกินไป"

# "It seems like I'm jumpier than I'd thought about Iwanako writing to me."
"ดูท่าว่าฉันจะตื่นเต้นที่อิวานาโกะเขียนจดหมายมาหากว่าที่คิดเอาไว้อีก"

# hi "I got a letter."
hi "จดหมาย"

show kenji neutral_close
with charachange

# ke "Oh, yeah, I put that there. I was sleeping, then I woke up because I heard explosions."
ke "อ้อ อืม ฉันเป็นคนเอาไปไว้ตรงนั้นเองแหละ ตอนนั้นฉันหลับอยู่แล้วก็สะดุ้งตื่นเพราะได้ยินเสียงระเบิด"

# ke "I put on my helmet and then peeked outside to see what was going on, but it was just that Student Council woman banging on your door. It was the one without pink hair."
ke "ฉันใส่หมวกนิรภัยแล้วแอบดูว่าข้างนอกมีอะไรกัน แต่ที่แท้ก็แค่เสียงยัยสภานักเรียนคนนั้นมาทุบประตูนาย คนที่ผม\nไม่ใช่สีชมพูน่ะ"

show kenji tsun_close
with charachange

# ke "She was knocking so loudly that it was obvious she was filled with murderous rage. Rage at you. Then she somehow sensed me behind her, and I tried to escape, but it was too late. She caught me and started pointing at the door."
ke "เคาะดังจนรู้เลยว่าโกรธนายจนอยากฆ่าคนเลยแน่ ๆ แล้วจากนั้นก็เหมือนรู้ว่าฉันดูอยู่ ฉันพยายามหนีแล้วแต่ก็สายไป\nพอจับฉันได้ยัยนั่นก็ชี้ ๆ ไปที่ประตู"

# "I open my mouth to tell him that she's deaf, but decide not to. For various reasons."
"ฉันอ้าปากเตรียมบอกว่าเธอหูหนวก แต่แล้วก็ตัดใจไม่บอกไปด้วยเหตุผลหลายประการ"

# ke "I didn't really get it, and she got more and more pissed off, like an old man trying to use a touchscreen phone."
ke "ไม่เข้าใจเลย แล้วยิ่งดูโมโหขึ้นเรื่อย ๆ อีกต่างหาก สภาพอย่างกับคนแก่ ใช้มือถือจอสัมผัส"

show kenji happy_close
with charachange

# ke "She was going to kill me. Kill me and replace me with a woman version of me. But then the sunlight reflected off my glasses and blinded her, saving my life."
ke "ตอนนั้นคือกะจะฆ่ากันแล้วแน่ ๆ ฆ่าแล้วเอาฉันที่เป็นร่างผู้หญิงมาแทน แต่แล้วแสงแดดก็สะท้อนจากแว่นฉันจนยัยนั่น\nมองไม่เห็น ฉันเลยรอดมาได้"

show kenji neutral_close
with charachange

# ke "It was like, behold, optic blast. I don't get how someone with glasses can be hurt by glasses. She uses them too, she should be immune to their death rays… but whatever. She gave me this envelope with your name on it and just left."
ke "แบบว่า จงดู ลำแสงแว่นตา ยังงงอยู่ว่าทำไมใส่แว่นแล้วแสงจากแว่นถึงยังมีผลอยู่ ใส่แว่นแล้วก็น่าจะทานลำแสงพิฆาต\nจากแว่นได้… แต่ช่างเหอะ ยัยนั่นให้จดหมายฉบับนี้ที่มีชื่อนายแปะอยู่แล้วก็เดินหนีไปเลย"

show kenji happy_close
with charachange

# ke "Clearly, she was out for blood, so I lied and said you were away. I think you were away, right? I've been trying to ask you if you wanted to help me with my homework for a week now, but kept getting no answer. …Welcome back, man!"
ke "ชัดเลยว่าออกมาล่าเหยื่อแน่ ๆ ฉันเลยโกหกไปว่านายไม่อยู่ เหมือนนายจะไม่อยู่นี่ ฉันขอให้นายช่วยฉันทำการบ้าน\nมาเป็นสัปดาห์แล้วแต่ก็ไม่มีเสียงตอบรับอะไรเลย …ยินดีต้อนรับกลับพวก!"

# hi "Thanks."
hi "ขอบใจ"

show kenji neutral_close
with charachange

# ke "Yeah, so she gave me this envelope and it had your name on it. I didn't want to hold on to it, because, what if it was a bomb? So I just shoved it under your door when she was gone."
ke "เออ ยัยนั่นก็ยื่นซองจดหมายที่มีชื่อนายติดอยู่นี่มาให้ ฉันก็ไม่อยากถือไว้ เพราะแบบ เกิดเป็นระเบิดทำไง พอยัยนั่น\nเดินไปแล้วฉันก็เลยสอดไว้ใต้ประตูห้องนาย"

# ke "I was going to tell you, but you got back before I could. At least it's not a bomb."
ke "กะจะมาบอกนายอยู่ แต่นายก็กลับมาก่อน อย่างน้อยก็ไม่ใช่ระเบิดอะนะ"

# hi "Gee, thanks. I'm not going to help you out with your math homework, because, what if your math textbook is a bomb?"
hi "เออ ใจ แต่ฉันไม่ช่วยนายทำการบ้านคณิตหรอก เพราะแบบ เกิดหนังสือคณิตนายเป็นระเบิดทำไง"

show kenji tsun_close
with charachange

# "He looks devastated, and also like he's considering the possibility that it really could be a bomb. I guess it is possible, since no one really uses their math book all that much."
"เขาดูอึ้งไป แถมเหมือนจะเริ่มคิดแล้วด้วยว่าหนังสือจะเป็นระเบิดจริง ๆ ก็น่าจะเป็นไปได้แหละ ไม่ค่อยเห็นใคร\nใช้หนังสือคณิตกันเท่าไหร่เลยนี่"

scene bg school_dormhisao
with locationchange

# "I throw the letter on the dresser behind me and turn to leave, swinging the door shut behind me as I do. It collides against the tip of Kenji's shoe and bounces back open, while he hops around for a bit, acting like it hurt way more than it should have."
"ฉันโยนจดหมายทิ้งไว้บนหลังตู้แล้วหันหลังมาพลางปิดประตู บานประตูชนเข้ากลับปลายรองเท้าเคนจิแล้วเด้งเปิดออก\nเขาโดดเหยง ๆ ทำท่าเหมือนเจ็บมากทั้งที่โดนไปแค่นั้น"

show kenji neutral at center
with charaenter

# "Before I know it, he's already inside my room. I'm powerless to stop him before he scoops up the letter, strangely ignoring the towers of pill bottles surrounding it."
"รู้ตัวอีกทีเขาก็มาอยู่ในห้องฉันแล้ว ฉันไม่อาจหยุดเขาที่กำลังคว้าจดหมายมาได้อีก แปลกที่เขาไม่เห็นขวดยาที่ตั้ง\nเรียงอยู่รอบ ๆ จดหมายฉบับนั้น"

# hi "Don't just read mail that isn't your own."
hi "อย่ามาเปิดอ่านจดหมายคนอื่นซี้ซั้วสิ"

show kenji happy
with charachange

# ke "C'mon, what is it? A love letter from your girlfriend? Did she include any photos? Sexy photos?"
ke "เออน่า จดหมายอะไรเนี่ย จดหมายรักจากแฟนนาย? มีรูปแนบมาด้วยมั้ยอะ? รูปยั่ว ๆ งี้?"

play sound sfx_dropstuff
stop music fadeout 4.0

# "Reclining against the dresser and paying no mind to the bottles he sends all over the floor by doing so, Kenji quietly reads through Iwanako's letter."
"เขาพิงกับตู้ใบนั้นแล้วอ่านจดหมายจากอิวานาโกะอยู่เงียบ ๆ โดยไม่สนใจขวดยาที่เขาทำตกเกลื่อนกลาดเลย"

# "The process takes seemingly forever, and with how close he holds it up to his face, makes it look like he's trying to eat it."
"ซึ่งอ่านนานเป็นชาติได้ แถมเอาหน้าจ่อจดหมายจนเหมือนอย่างกับว่าจะกินเข้าไปแล้ว"

show kenji tsun
with charachange

# ke "Who's “Iwanako?”"
ke "“อิวานาโกะ” นี่ใคร"

# hi "My ex-girlfriend."
hi "แฟนเก่าฉัน"

play music music_night fadein 4.0

show kenji neutral
with charachange

# ke "Ex-girlfriend, huh? This is the breakup letter, then. I thought they were a myth."
ke "แฟนเก่าเหรอ งั้นก็จดหมายเลิกกันงั้นสิ นึกว่าของแบบนี้ไม่มีจริงเสียอีก"

# hi "No. I guess it is, but really, she's been my ex-girlfriend for a while. Anyway, I think I'm already over it."
hi "ไม่ใช่ คือก็คงใช่แหละ แต่ก็เป็นแฟนเก่ามาสักพักแล้ว เอาเหอะ ฉันว่าฉันก็ไม่อะไรกับเธอแล้วละ"

# "Kenji gives a thumbs up, clearly relieved that I'm not going to take this into an awkward direction, although I almost want to since I told him not to read it."
"เคนจิยกนิ้วโป้งให้เป็นสัญญาณว่าเขาโล่งใจที่ฉันไม่เอาเรื่องนี้มาคุยแบบทำให้บรรยากาศต้องอึดอัด ทีแรกก็อยาก\nอยู่หรอก บอกแล้วนี่ว่าอย่าอ่าน"

show kenji happy
with charachange

# ke "Yeah, that's a good attitude. It's all right, I had a bad breakup, too, but you can't let it get you down. I mean, just look at me."
ke "เออ ต้องงี้สิ ไม่เป็นไรเว้ย ฉันก็เคยผ่านการเลิกแบบแย่ ๆ มาแล้วเหมือนกัน แต่อย่าไปเครียดกับมันมาก เนี่ย\nดูฉันนี่"

# hi "Uhhhh…"
hi "เอ้ออออ…"

# ke "But, hey, she wrote you a letter. Maybe she wants to get back together, huh? It says right there, write her back. You should do it. Is she cute?"
ke "แต่ก็ยังเขียนจดหมายมานี่ อาจจะอยากให้กลับไปคบกันก็ได้ เขียนไว้ด้วยนี่ว่าให้ตอบกลับด้วย เขียนตอบไปก็ดีนะ\nแล้วน่ารักมั้ย"

# "For a guy who thinks feminists are working to enslave men everywhere, he really is interested in cute girls."
"ช่างสนใจสาวน่ารักได้ผิดวิสัยคนที่คิดว่าพวกสตรีนิยมลงแรงกดขี่ผู้ชายทั่วโลกจริง ๆ"

# hi "I have a girlfriend. Besides, look at the context, she doesn't want me to write back. Just because that's what it says, that isn't what she means."
hi "ฉันมีแฟนแล้ว อีกอย่าง ดูบริบทด้วย เธออยากให้ฉันเขียนตอบจริง ๆ ที่ไหน ใช่ว่าเธอเขียนแล้วจะหมายความตรงตัว\nอย่างนั้นสักหน่อย"

show kenji neutral
with charachange

# ke "But that's what she wrote. This rock-fish-kid chick totally still wants you. It even says it right there."
ke "แต่ก็เขียนไว้งั้นนี่ ยัยอีหว้าหน้าโค้กอะไรนี่ยังต้องการนายอยู่แน่ ๆ มีเขียนตรงนี้ด้วยเนี่ย"

# hi "I read it, I know what it says. I told you, you have to look at the context. She said I drifted away from her, and everything there shows she accepted that."
hi "อ่านแล้ว ฉันรู้น่าว่าเขียนว่าอะไรบ้าง ดูบริบทสิ เธอบอกว่าฉันออกห่างจากเธอ แล้วที่เขียนในนั้นทั้งหมดก็สื่อว่าเธอ\nทำใจยอมรับแล้ว"

# hi "I think the reason she wrote to me is that she just wants to, I guess, part amicably. But we're done, she doesn't want to get back together or whatever you're thinking."
hi "ที่เขียนจดหมายฉบับนี้มาก็แค่อยากส่งลาแบบถนอมน้ำใจกันบ้างน่ะแหละ แต่เราสองคนจบกันแล้วจริง ๆ เธอไม่ได้\nอยากให้กลับไปคบกันหรืออะไรก็ช่างอย่างที่นายคิดหรอก"

# "As I think about it more, it sounds to me like I'm just trying to make excuses for myself. That's not a good place to be."
"ยิ่งคิดก็เหมือนยิ่งแก้ตัวให้ตัวเอง จะให้กลับไปก็คงไม่ได้แล้ว"

# "I'm positive that she doesn't want me to write her back. I can live with that. If I were to write her back and get a less than desirable response, or no response, then I would just be crushed."
"ฉันมั่นใจว่าเธอไม่อยากให้ฉันเขียนตอบ ซึ่งฉันก็ทำใจได้ ถ้าเขียนตอบไปแล้วเธอส่งคำตอบอะไรที่ไม่น่าอ่านกลับมาอีก\nหรือไม่ตอบเลยฉันก็คงใจสลายเปล่า ๆ"

# "Perhaps the fear of that is why I'm trying to justify my decision. It could be, but I don't want to think about it. The thought is oddly repulsive."
"คงเพราะฉันกลัวอย่างนั้นฉันถึงได้หาข้ออ้างที่ไม่เขียนตอบไป อาจจะเป็นอย่างนั้น แต่ฉันไม่อยากคิดแล้ว แค่คิดก็รู้สึก\nรังเกียจขึ้นมาพิกล"

# hi "Why is this such a big deal to you, anyway?"
hi "แล้วนายจะอะไรกับมันกันนักกันหนาฮะ?"

show kenji happy
with charachange

# ke "Because you should write back to her. She wants you to. I want to see what the response is going to be."
ke "เพราะนายควรเขียนตอบไปไง เธอก็อยากให้นายตอบ ฉันอยากรู้ว่าเธอจะตอบมาว่ายังไง"

show kenji neutral
with charachange

# ke "Damn, it doesn't even have to be a nice letter. That's cool too, but you could write an angry letter and call her out. That's my new attack strategy, I'm just going to call women out. You should try it."
ke "โห่ ไม่ต้องเขียนอะไรดี ๆ ก็ได้ ไม่เป็นไร เขียนแบบโกรธ ๆ แล้วนัดออกมาเจอกันเลย นี่แหละกลยุทธ์การจู่โจมแบบใหม่\nของฉัน ฉันจะนัดพวกผู้หญิงออกมาเจอกัน นายต้องลองบ้างนะ"

# hi "Even if she wrote me a letter, you have to understand what that means. Writing someone a letter is different now. It's not something you just do. Not in this kind of situation."
hi "ต่อให้เขียนจดหมายมาก็จริง แต่นายต้องทำความเข้าใจด้วยนะว่าหมายความว่าอะไร ยุคนี้การเขียนจดหมายมัน\nไม่เหมือนเมื่อก่อนแล้ว มันไม่ใช่อะไรที่ทำไปงั้น ๆ ยิ่งกับเรื่องอย่างนี้อีก"

# hi "You can pick up your phone and call someone across the world in an instant, and talk to them almost like they were there with you. Or send them an email; they'll be notified instantly that they got it and can reply back, just like that."
hi "เดี๋ยวนี้แค่ใช้โทรศัพท์ก็คุยกับคนที่อยู่คนละฟากโลกได้เหมือนนั่งอยู่ข้างกันแล้ว ส่งอีเมลก็ได้ เดี๋ยวก็แจ้งเตือนก็ไปโผล่\nที่คนรับว่ามีจดหมายเข้าแล้วก็ตอบกลับได้ ง่ายแค่นี้เอง"

# hi "A letter can be a personal thing, but she wanted to keep me at an arm's distance. It's not like I can pop over there and visit her."
hi "บางทีจดหมายมันเป็นเรื่องส่วนตัวก็จริง แต่เธออยากรักษาระยะกับฉันเอาไว้ ใช่ว่าฉันจะโผล่หัวไปแวะหาเธอได้เลย\nสักหน่อย"

# hi "If I had her number, I could call her, or if I had her mail, I could mail her. If she really wanted to hear back from me, she would have dropped one of those in there."
hi "ถ้าฉันมีเบอร์ก็โทร. ไปหาได้ หรือถ้ามีอีเมลก็ส่งไปหาได้ ถ้าอยากให้ฉันติดต่อกลับจริง ๆ เธอก็คงเขียนช่องทางติดต่อ\nอะไรสักอย่างแบบนั้นมาด้วย"

# "I feel silly for continuously reassuring myself that I'm not fazed by Iwanako writing to me, when it's so obvious that I am."
"รู้สึกงี่เง่าที่ต้องคอบปลอบใจตัวเองว่าไม่ได้หวั่นไหวอะไรที่อิวานาโกะเขียนจดหมายมาหา ทั้งที่ออกจะชัดว่าฉันหวั่นไหว"

show kenji tsun
with charachange

# ke "It could be like a gradual thing for her. She might be too shy to call you up. I remember my girlfriend would always send me text messages because she was so shy. It was annoying as hell, man."
ke "เธออาจจะอยากให้ค่อยเป็นค่อยไปก็ได้นะ อาจจะแค่ไม่กล้าโทร. มาหานาย ยังจำได้เลยที่แฟนฉันชอบส่งข้อความ\nมาหาเพราะเป็นคนขี้อายมาก ๆ เนี่ย น่ารำคาญมากให้ตาย"

# ke "I didn't really give a shit about phones so I didn't have the thing, and it turns out I had to pay for every single one. But I don't like phones so I couldn't even call her back to tell her to cut that out."
ke "แต่ฉันก็ไม่ได้อะไรกับโทรศัพท์น่ะนะ เลยไม่ใช้ แต่ฉันต้องมาจ่ายค่าส่งข้อความให้ทุกรอบอยู่ดี แต่พอดีฉันไม่ชอบ\nโทรศัพท์ก็เลยไม่ได้โทร. บอกให้เธอเลิกส่งมาสักที"

show kenji neutral
with charachange

# ke "I did it anyway, though. I called her out. I even used a phone. It was literally the call out."
ke "แต่สุดท้ายก็ได้โทร. ใช้โทรศัพท์นี่แหละโทร. บอกเลย"

# hi "I guess it was."
hi "อ้อเหรอ"

# "Even if he's right, it means that Iwanako still wants to keep her distance from me. She's “not ready” to chat with me comfortably."
"ต่อให้เป็นอย่างเคนจิว่า ยังไงอิวานาโกะก็คงยังอยากรักษาระยะกับฉันอยู่ดีนั่นแหละ เพราะเธอยัง “ไม่พร้อม” ที่จะคุย\nกับฉันแบบสบาย ๆ"

# "Why? Am I some kind of freak? I'm not reassured by her actions anyway, in that case. Maybe I am overthinking it, but I just don't know."
"ทำไม เพราะฉันเป็นพวกน่าเกลียดเหรอ ถ้างั้นการที่เธอทำอย่างนี้ก็ไม่ได้ทำให้ฉันสบายใจขึ้นมาเลย ฉันอาจจะ\nคิดมากไป แต่ไม่รู้สิ"

# "Kenji can't think of anything to say to that, and the silence that follows is so awkward and thick that I start to count the seconds until he makes up a reason to leave and excuses himself."
"เคนจิไม่รู้จะพูดต่อจากนั้นยังไงอีก ความเงียบที่ตามมาช่างอึดอัดรัดแน่นเสียจนฉันนับวินาทีอยู่ในใจ จนท้ายที่สุดเขาก็\nหาข้ออ้างปลีกตัวออกไป"

show kenji tsun
with charachange

# ke "I miss her…"
ke "คิดถึงเธอจัง…"

# hi "Your ex?"
hi "แฟนเก่านาย?"

# ke "Yeah. Even if she was insane, it was nice being with her."
ke "เออ ถึงจะบ้า แต่ตอนได้คบกันก็ดีนะ"

# ke "My back hurts. If she were still around I could tell her to massage it. I don't know how to use an oven, either. I miss baked food. And we would go bowling in the hallway sometimes. I miss that, too. I had to bowl all by myself during that last festival."
ke "ปวดหลังชะมัด ถ้ายังอยู่ฉันคงขอให้นวดให้ ฉันใช้เตาอบไม่เป็นด้วย คิดถึงอาหารแบบอบจัง แล้วบางทีก็จะไปเล่นโบว์ลิง\nกันที่โถงทางเดินด้วย คิดถึงอันนั้นเหมือนกัน งานเทศกาลล่าสุดนี่ฉันก็ต้องไปเล่นโบว์ลิงตัวคนเดียว"

# hi "You bowl in the hallway? You're going to hit someone."
hi "นี่ไปโบว์ลิงที่โถงทางเดินเหรอ เดี๋ยวก็ไปโดนใส่ใครเข้าหรอก"

# ke "She used to say that all the time…"
ke "เธอพูดงั้นตลอดเลย…"

# "Kenji sighs nostalgically, clearly not appreciating just how badly someone can get hurt by slipping on a bowling pin. Apparently, neither did his girlfriend, since she bowled with him. What a strange definition of love, but I guess it's something."
"เคนจิถอนหายใจหวนถวิล ชัดว่าเขาไม่ได้คิดเลยว่าคน ๆ หนึ่งจะบาดเจ็บได้หนักขนาดไหนถ้ามาเหยียบพินโบว์ลิงแล้ว\nลื่นล้ม ดูเหมือนแฟนเขาก็ไม่ได้คิดด้วย เป็นนิยามของคำว่ารักที่แปลกเหลือเกิน แต่รักก็คือรักแหละมั้ง"

# hi "Maybe you should write her a letter. If she writes back, you can get married."
hi "นายน่าจะเขียนจดหมายถึงเธอบ้างนะ ถ้าเธอเขียนตอบมานายก็จะได้แต่งงาน"

stop music fadeout 0.3

show kenji rage
with charachange

# ke "Married?! No. No no no. No."
ke "แต่งงาน?! ไม่ ไม่ ๆ ๆ ไม่"

# hi "Okay, fine. But why not? You clearly like her, even though you hate women."
hi "โอเค๊ แต่ทำไมไม่เขียนล่ะ นายก็ชอบเธออยู่ ขนาดว่านายเกลียดผู้หญิงแท้ ๆ"

show kenji tsun
with charachange

play music music_kenji fadein 2.0

# ke "Feminists! Not women, feminists. There's a difference. There are non-feminist women. Damn, your discrimination is incredible. Correlation doesn't equal causation. Even if she is insane and a woman, it doesn't mean she is a feminist insane woman."
ke "พวกสตรีนิยม! ไม่ใช่ผู้หญิง พวกสตรีนิยม ไม่เหมือนกันสักหน่อย ผู้หญิงที่ไม่ใช่พวกสตรีนิยมก็มี นายนี่เป็นคน\nแบ่งแยกแบบนี้เหรอเนี่ย อะไรที่สัมพันธ์กันมันไม่ได้เป็นเหตุผลกันเสมอไปเว้ย เธอบ้าแล้วก็เป็นผู้หญิงก็จริง แต่ก็ไม่ได้\nหมายความว่าเธอจะเป็นผู้หญิงบ้าที่เป็นพวกสตรีนิยมนะ"

show kenji neutral
with charachange

# ke "It's like how the absence of evidence isn't the evidence of absence. If it's true, then by the relative property, the presence of evidence doesn't equal the evidence of presence."
ke "ก็เหมือนกับที่ว่าการไม่มีหลักฐานไม่ได้เป็นหลักฐานว่าไม่มีน่ะแหละ ถ้าจริงแล้ว ด้วยสมบัติถ่ายเท จะได้ว่า\nการมีหลักฐานไม่ได้เป็นหลักฐานว่ามี"

# hi "Actually, I think it is. And I don't think it's called the relative property."
hi "ที่จริง มีหลักฐานแล้วก็ต้องแปลว่ามีหรือเปล่า แล้วก็ไม่น่าเรียกว่าสมบัติถ่ายเทนะ"

show kenji tsun
with charachange

# ke "No, shut up, it's mathematics! Are you saying math is wrong?"
ke "ไม่ หุบปากเลย คณิตศาสตร์นะเว้ย! นายจะบอกว่าคณิตศาสตร์ผิดเหรอ"

# "I think he is wrong."
"เขาน่าจะผิดมากกว่านะ"

# "So even Kenji has someone that he likes. I'm tempted to ask why he and his ex broke up, or to dig for more information in general, but I shouldn't. Not only would it be prying, but he might reverse the question back to me."
"แม้แต่เคนจิยังมีคนที่ชอบสินะ อยากถามเหมือนกันว่าทำไมถึงเลิกกัน ไม่ก็ถามขุดคุ้ยอะไรอีกก็ได้ แต่อย่าดีกว่า\nไม่ใช่แค่ว่าถามแล้วจะเป็นการสอดรู้เกินไป แต่เดี๋ยวเขาคงจะย้อนถามฉันอีก"

stop music fadeout 8.0

# "This conversation makes me think about Shizune, although the thoughts I'm having are scattered and wispy. Just questions."
"พอคุยแล้วก็คิดไปถึงชิซูเนะ ถึงความคิดที่ว่าจะกระจัดกระจายเลือนรางมีแต่คำถามก็เถอะ"

# "I wonder if I even had the chance to love Iwanako, and this whole situation with her still stings me, a sour note in the back of my mind."
"ฉันได้ทันรักอิวานาโกะหรือเปล่านะ พอความสัมพันธ์หรืออะไร ๆ กับเธอเป็นอย่างนี้ไปแล้วฉันก็นึกเจ็บปวดอยู่ลึก ๆ"

# "I like Shizune much more. Yet it feels like I am chasing her, even now. I don't mind the chase, but I want to close that distance between us."
"ฉันชอบชิซูเนะมากกว่ามาก แต่ยังรู้สึกเหมือนว่าแม้แต่ตอนนี้ฉันยังไล่ตามเธออยู่ ฉันไล่ตามได้ไม่เหนื่อยหรอก แต่ฉัน\nอยากให้ระยะระหว่างเราสองคนร่นลงใกล้กันกว่านี้"

# "Iwanako's letter is responsible, but I've also felt this way for a while. I've come closer, but it's not enough. I want to try again, right now."
"จดหมายของอิวานาโกะมีส่วนก็จริง แต่ฉันก็รู้สึกอย่างนี้มาสักพักแล้ว ได้เข้าใกล้แล้วแต่ยังใกล้ไม่พอ ฉันอยากลองใหม่\nตอนนี้เลย"

hide kenji
with charaexit

# "I tell Kenji to get out so I can change, and then head for the student council room."
"ฉันบอกให้เคนจิออกไปเพราะจะเปลี่ยนชุด พอเสร็จแล้วฉันก็มุ่งไปยังห้องสภานักเรียน"

scene bg school_courtyard
with locationskip

# "The grounds are mostly deserted today, which is a shame, because it's so nice out."
"วันนี้ลานหน้าโรงเรียนดูค่อนข้างโล่ง น่าเสียดาย อากาศดีขนาดนี้แท้ ๆ"

scene bg school_hallway3
with locationskip

play sound sfx_doorknock2

# "No one answers when I knock. I try to go in anyway, but it's locked. When I pull my hand away from the doorknob, it's covered in dust. It looks like no one's been here since we left."
"ฉันเคาะประตูแล้วแต่ไม่มีเสียงตอบรับ พอลองบิดลูกบิดดูก็พบว่าประตูล็อกอยู่ เมื่อพลิกมือดูก็เห็นฝุ่นที่เกาะอยู่บน\nฝ่ามือ ดูท่าว่าตอนที่พวกเราไม่อยู่นั้นไม่มีใครมาที่ห้องนี้เลย"

# "Since I'm already out here and dressed, I might as well get something to eat in town. My wallet is back in my room, though."
"ไหน ๆ ก็เปลี่ยนชุดออกมาขนาดนี้แล้ว ไปเข้าเมืองหาอะไรกินแล้วกัน แต่กระเป๋าสตางค์ดันอยู่ที่ห้องนี่สิ"

scene ev misha_sad:
     truecenter
     subpixel True zoom 1.05
     easein 10.0 zoom 1.0
with locationskip

# "On the way back there, I stumble across Misha sitting down behind the main building."
"ตอนที่เดินกลับหอฉันเจอมิช่าที่นั่งอยู่หลังอาคารหลัก"

# "Her eyes are closed in sleep, and she looks very tranquil. It's always been hard to picture her not constantly bouncing around or hopping on the tips of her toes impatiently."
"เธอหลับตาพริ้มหลับอยู่ดูสงบ ปกติจะนึกสภาพเธอที่ไม่ได้เริงร่าหรือโดดเขย่งเท้าไปมาเหมือนรอไม่ได้ไม่ออกเลย"

# "My first instinct is to call out to her and ask her if she has seen Shizune, or if she wants to go to town with me, but now that I've seen her I don't feel like disturbing her. I leave her alone."
"แวบแรกฉันอยากเรียกเธอแล้วถามว่าเห็นชิซูเนะหรือเปล่า ไม่ก็อาจจะชวนไปเข้าเมืองด้วยกัน แต่พอเห็นสภาพนี้แล้วก็\nไม่อยากกวน ฉันจึงปล่อยให้เธอหลับอยู่อย่างนั้น"

scene black
with dissolve

$ suppress_window_after_timeskip = True

label th_S25:

window hide None

scene bg school_council_bw
with locationchange

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_pearly

nvl clear
nvl show dissolve

# n "\n\n\nFor the first few days after I was back, I almost forgot that I was in the Student Council. I managed to pick up here and there that the Student Council usually gets swamped with work around the end of the break, but it didn't have to be the case."
n "\n\n\nวันแรก ๆ ฉันแทบลืมไปแล้วว่าตัวเองเป็นสภานักเรียน ฉันพอได้ยินมาบ้างว่าปกติช่วงเปิดเทอมสภานักเรียนจะมีงาน\nเข้ามาจนท่วมหัว แต่ดูท่าว่าจะไม่เป็นอย่างนั้นเสมอไป"

# n "The few times when I managed to catch Shizune or Misha, they were in too much of a hurry for me to get a chance to ask if they needed help. Anytime they weren't, I'd only be able to get ahold of Misha."
n "ฉันเห็นชิซูเนะไม่ก็มิช่าอยู่ไม่กี่ครั้ง ทั้งสองคนดูจะรีบร้อนเกินกว่าจะเปิดจังหวะให้ฉันได้เสนอตัวเข้าช่วย หรือถ้าเป็น\nช่วงที่สองคนนั้นไม่รีบฉันก็จะได้คุยกับแค่มิช่า"

# n "\nShizune would say something about how there was work, but it was so little that involving either Misha or I would only bore us."
n "\nชิซูเนะจะอ้างว่ามีงานต้องทำ แต่เป็นงานเล็กน้อยที่ถ้าฉันหรือมิช่าไปช่วยก็คงเบื่อกันก่อน"

# n "\n\nAfter awhile, the idea of having some free time again had started to grow on me, though there were still periods when I felt like I had too much of it."
n "\n\nผ่านไปพักหนึ่งฉันก็เริ่มรู้สึกอยากมีเวลาว่างขึ้นมาอีกแล้ว ถึงจะมีช่วงที่รู้สึกว่าว่างเกินไปอยู่ก็เถอะ"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

scene bg school_council
show shizu basic_normal2 at center
with locationchange

window show

# "Just when I was getting used to it, though, things changed again. Now I find myself back in the student council room, arguing with Shizune about whether tissue boxes make good ballot boxes or not."
"แต่พอฉันเริ่มชิน อะไร ๆ ก็เปลี่ยนไปอีก ตอนนี้ฉันมาเถียงกับชิซูเนะอยู่ในห้องสภานักเรียนว่ากล่องทิชชูใช้ทำ\nหีบบัตรเลือกตั้งได้หรือเปล่า"

# hi "I'm telling you, they work just fine, as long as we get the cube-shaped ones, not the rectangular ones."
hi "ก็บอกแล้วไงว่าใช้ได้ไม่มีปัญหาอะไร ขอแค่เป็นกล่องทรงลูกบาศก์ ไม่ใช่กล่องสี่เหลี่ยมด้านยาว"

# hi "Misha, can you sign that to her? I've kind of got my hands full. …On second thought, forget it."
hi "มิช่า แปลเป็นภาษามือให้หน่อย ฉันมือไม่ว่าง …แต่คิดอีกที ช่างเหอะ"

# "She is busy cutting out ballot slips, so if she were to make one errant movement she would probably send those scissors flying into someone's head."
"เธอกำลังง่วนอยู่กับการตัดบัตรเลือกตั้ง ถ้าเกิดขยับมือไม้อะไรมั่วซั่วเดี๋ยวกรรไกรคงได้ปลิวเข้ามือใครสักคนแน่ ๆ"

# "I drop the box of poster paints I'm carrying onto my little table in the student council room, and cough as a wave of dust hits me in the face. It really has been a while."
"ฉันวางลังสีโปสเตอร์ที่ขนมากับโต๊ะตัวเล็ก ๆ ของฉันในห้องสภานักเรียน ฝุ่นที่ปลิวเข้าหน้าทำฉันไอ ผ่านไปนาน\nจนฝุ่นเขรอะเลยนะเนี่ย"

show shizu behind_blank
with charachange

# ssh "Do you think we should change the size of the ballot slips?"
ssh "ปรับขนาดบัตรเลือกตั้งดีมั้ย"

show bg school_council at bgright
show shizu behind_blank at tworight
with charamove

show mishashort sign_confused at twoleft
with charaenter

# mi "What~? But Shicchan, I already cut out so many of them…"
mi "หา~ แต่ว่านะชิจัง ฉันตัดไปเยอะแล้ว…"

show shizu basic_normal
with charachange

# ssh "We can make them smaller. It will be more efficient. We just have to shrink the font. More ballots will fit in a single box that way. We'll only need half the amount of paper, then."
ssh "ทำให้เล็กลงหน่อย จะได้มีประสิทธิภาพกว่า ลดขนาดตัวอักษรลงด้วย จะได้ใส่บัตรเลือกตั้งในหีบได้เยอะ ๆ แล้วก็\nจะได้ประหยัดกระดาษไปครึ่งหนึ่งด้วย"

show shizu behind_smile
with charachange

# ssh "The format for voting can be changed. It could be more like a real election; then we might be able to get away with buying less boxes."
ssh "หรือจะเปลี่ยนรูปแบบการเลือกตั้งด้วยก็ได้ อาจจะทำเหมือนเลือกตั้งจริง ๆ เลย จะได้ไม่ต้องซื้อกล่องมาเยอะด้วย"

show shizu adjust_happy
with charachange

# ssh "With the money left over, we can get a pizza, or maybe Chinese, or a cake, or three bowls of the new ramen bowl I want to try."
ssh "พอเงินเหลือเราก็จะได้ซื้อพิซซ่า ไม่ก็อาหารจีน ไม่ก็เค้ก ไม่ก็ราเมงที่ฉันอยากลองชิมสักสามชาม"

# "Shizune excitedly rubs a finger along the frame of her glasses as she ponders more ways to cut even a half-yen of spending off of our budget."
"ชิซูเนะถูกรอบแว่นไปมาด้วยความตื่นเต้นพลางคิดหาวิธีประหยัดงบให้ได้แม้ครึ่งเยนก็ตาม"

# "Since I think she is the only one who even knows what our budget is, I'm scared to ask just how tiny is it for her to have to do this."
"เธอน่าจะเป็นคนเดียวที่รู้ว่าเรามีงบอยู่เท่าไหร่ ฉันจึงไม่กล้าถามว่าจริง ๆ แล้วที่จัดเลือกตั้งนี่ใช้งบไปน้อยขนาดไหน"

# hi "What about all the ballot slips Misha already cut out?"
hi "แล้วบัตรที่มิช่าตัดไปแล้วล่ะ"

show shizu basic_happy
with charachange

# ssh "Don't worry, don't worry. I can make them into memo pads and sell them in the school store."
ssh "ไม่ต้องห่วง ๆ เดี๋ยวฉันจะเอาไปทำเป็นสมุดจดแล้วขายให้สหกรณ์โรงเรียนเอง"

show mishashort perky_confused
with charachange

# mi "Shicchan, they don't look very cute, though~…"
mi "ชิจัง แต่ว่ามันดูไม่น่ารักเท่าไหร่เลยนะ~…"

show shizu adjust_frown
with charachange

# "Shizune seems to disagree. Now they're arguing, but it looks like it consists of nothing more than signing “Yes, they do” and “No, they don't” at each other until they're so tired of it they are just taking turns pointing at each other commandingly."
"เหมือนชิซูเนะจะไม่เห็นด้วย และตอนนี้ทั้งสองคนก็เถียงกันแล้ว แต่เหมือนจะเถียงกันด้วยการบอกแค่ว่า “น่ารัก” กับ\n“ไม่น่ารัก” ใส่กันไปจนเหนื่อยแล้วเปลี่ยนมาใช้วิธีการชี้นิ้วสั่งใส่กันแทน"

# "It's strange, partly because it looks kind of ridiculous, but also because I've never seen them disagree."
"แปลกดี ส่วนหนึ่งก็เพราะดูไร้สาระ แต่ก็เพราะไม่เคยเห็นสองคนนี้ความเห็นไม่ตรงกันเลยด้วย"

# "Then again, both of them have looked very stressed these past few days."
"แต่ก็นะ ช่วงสองสามวันมานี้ก็ดูเครียด ๆ กันทั้งคู่"

# "Shizune has been increasingly absorbed in the idea of student council elections, though they're months away. I imagine this is how politicians act when they realize a regime change is imminent and their era is over."
"ชิซูเนะดูจะหมกมุ่นอยู่กับการเลือกตั้งสภานักเรียน ทั้งที่ก็เหลือเวลาอีกหลายเดือนแท้ ๆ นี่สินะนักการเมืองเวลารู้ตัว\nว่ายุคสมัยของตัวเองจะสิ้นสุดลงและใกล้ถึงเวลาเปลี่ยนระบอบการปกครองแล้ว"

# "I'm having trouble taking student council matters seriously at all, even now, as I practice my calligraphy on signs that won't go up for weeks, but I can understand why Shizune does."
"ขนาดตอนนี้ที่ฉันมานั่งคัดลายมือเขียนป้ายที่ต้องรออีกหลายสัปดาห์กว่าจะได้แปะ ฉันก็ยังไม่สามารถคิดจริงจัง\nกับเรื่องสภานักเรียนได้เท่าไหร่ แต่ก็เข้าใจว่าทำไมชิซูเนะถึงจริงจังกับเรื่องนี้"

# "After all, she has been Student Council president for three years. According to her dad, she has wanted the job for even longer. I guess three years is too short a career for her to leave feeling satisfied."
"ก็เป็นประธานสภานักเรียนมาสามปีแล้วนี่นะ แถมเท่าที่ได้ยินพ่อเธอบอก เธอฝันอยากเป็นมาตั้งแต่ก่อนหน้านั้นอีก\nสงสัยสามปีคงยังไม่หนำใจเธอพอที่จะสละตำแหน่งนี้ได้"

# hi "Did the last Student Council go through this much trouble to make it a smooth transition for you?"
hi "สภานักเรียนรุ่นก่อนเขาลงทุนให้ผลัดคนได้ราบรื่นกันขนาดนี้เลยเหรือเปล่า"

show shizu behind_frustrated
with charachange

# "Shizune makes a chagrined face that tells me they weren't very helpful at all."
"ชิซูเนะทำหน้าเบ้เป็นเชิงว่ารุ่นก่อนไม่ได้มีประโยชน์อะไรเท่าไหร่เลย"

# hi "I guess you're doing all this to set a good example, then?"
hi "งั้นแสดงว่าที่เธอทำก็เพื่อจะเป็นตัวอย่างที่ดีสินะ"

show shizu basic_frown
with charachange

shi "…"

show mishashort hips_frown
with charachange

# mi "That only comes into play if they learn anything from it, Hicchan~! If they don't, I'll be hyper mad~! If they turn out to be the flaky type, I'll definitely be hard on them~."
mi "ตัวอย่างที่ดีจะมีค่าก็ต่อเมื่อมีคนเอาอย่างเท่านั้นแหละฮิจัง~! ถ้าไม่เอาอย่างฉันละก็ฉันจะโกรธมาก~! ถ้าเป็นพวก\nไม่เอาไหนละก็ฉันจะจี้ให้หนักเลย~"

# "It doesn't sound very threatening when Misha is saying it."
"พอมิช่าพูดแล้วก็ฟังดูไม่น่ากลัวเท่าไหร่เลยแฮะ"

# hi "So, you've already met them?"
hi "งั้นแสดงว่าเคยเจอกันแล้วงั้นสิ"

show shizu adjust_smug
with charachange

shi "…"

show mishashort hips_grin
with charachange

# mi "Ahaha~. Hicchan, there are no candidates yet~!"
mi "อะฮ่าฮ่า~ ฮิจัง ยังไม่มีผู้สมัครรับเลือกตั้งเลย~!"

# hi "What? None?"
hi "ฮะ? ไม่มีเลย?"

show shizu behind_smile
show mishashort hips_smile
with charachange

# ssh "Not even for Student Council president. That is why I am trying to drum up interest for the position. What do you think?"
ssh "แม้แต่ตำแหน่งประธานสภานักเรียนก็ยังไม่มีเลย ฉันถึงได้พยายามกระตุ้นให้คนมาสนใจสมัครตำแหน่งนี้กัน คิดว่าไงล่ะ"

# "She proudly holds up a poster she has been working on herself. It looks very, uh, military."
"เธอชูโปสเตอร์ที่ทำเองกับมือให้ดูด้วยความภูมิใจ ซึ่งดูสภาพ เอ่อ เหมือนหลุดมาจากค่ายทหาร"
#i'm pretty tempted to pilfer kamifish's secret santa 2011 thing for a cutin here

# hi "You might be taking this a little too seriously, then."
hi "งั้นเธอก็จริงจังไปหน่อยแล้วมั้ง"

show shizu adjust_frown
with charachange

# "Shizune frowns and plays with her glasses, offended."
"เธอขมวดคิ้วแล้วจับกรอบแว่นเล่นด้วยความไม่พอใจ"

# ssh "Is that weird?"
ssh "แปลกเหรอ"

# hi "Yes."
hi "ใช่"

show shizu behind_smile
with charachange

# "She looks oddly happy that I'm disagreeing with her, and I think that if she weren't genuinely focused on what she was doing, she would try to argue with me just because it would be interesting to her."
"เธอดูมีความสุขแปลก ๆ ที่ฉันค้านเธอ ถ้าไม่ติดว่าเธอกำลังตั้งสมาธิทำอะไรอยู่แล้วคงมาเถียงกับฉันเพราะน่าสนใจดี\nแน่ ๆ"

show shizu basic_normal
with charachange

# ssh "What's weird about it?"
ssh "แปลกตรงไหน"

show shizu adjust_smug
with charachange

# "It looks like she will do that after all. But then, Shizune waves her hand dismissively, like she is trying to catch the words in the air and delete them. Instead, she catapults into insulting her future successors."
"ก็ดูท่าว่าจะเถียงอยู่ดีนั่นแหละ เธอโบกไม้โบกมือเป็นเชิงปฏิเสธราวกับว่าจะจับคำที่ลอยอยู่ในอากาศนั้นลบทิ้งไป\nและเธอก็เตรียมเปลี่ยนมาเป็นการตำหนิคนรุ่นถัดจากเธอแทน"

# hi "Well, one thing that's weird is that in my old school the elections would happen in about six months, since, you know, we're graduating in March. It's pretty weird to think about them so early."
hi "ก็ ที่แปลกอย่างหนึ่งเลยก็คือถ้าเป็นที่โรงเรียนเก่าฉันก็ต้องอีกสักหกเดือนกว่าจะได้เลือกตั้ง เพราะ แบบ เราจะจบ\nช่วงเดือนมีนาใช่มั้ย จะมาคิดถึงการเลือกตั้งเอาเร็วขนาดนี้มันก็แปลกอยู่นะ"

show shizu behind_blank
with charachange

# ssh "It's a little different here."
ssh "ไม่เหมือนกันสักหน่อย"

show shizu adjust_frown
with charachange

shi "…"

show mishashort sign_smile
with charachange

# mi "Hicchan, I'll be discouraged if we don't have any replacements when I have to go~! Shicchan says."
mi "ฮิจัง ฉันคงอ่อนใจแน่ถ้ายังไม่มีใครมาแทนตอนที่ฉันต้องไปน่ะ~! ชิจังว่างั้น"

show mishashort hips_grin
with charachange

# mi "But~!, it isn't like the school will stop running without a Student Council. It will be harder for them to hand out forms, though~!"
mi "แต่~! ใช่ว่าไม่มีสภานักเรียนแล้วการจัดการอะไรของโรงเรียนจะชะงักไปเลยน่ะนะ แต่คงแจกเอกสารอะไรยากหน่อย~!"

show mishashort cross_laugh
with charachange

# mi "Hahaha~."
mi "ฮ่าฮ่าฮ่า~"

show shizu basic_normal2
show mishashort cross_smile
with charachange

# "Shizune isn't laughing, however. Misha's joke causes her to flinch, as if she were stung. Though Misha didn't mean for it to come out that way, her quip had a callous cruelty to it in the end."
"แต่ชิซูเนะไม่ขำด้วย มุกของมิช่าทำชิซูเนะผงะไปราวกับว่าเจ็บใจขึ้นมา ถึงมิช่าจะไม่ได้ตั้งใจเสียดสี แต่คำพูดล้อที่ว่า\nก็ได้ผลเช่นนั้นโดยที่เธอไม่รู้ตัว"

show shizu adjust_frown
with charachange

# ssh "Hmph. I'm trying to get more people to run, but everyone is so lazy. They think they can take it easy just because there are no deadlines yet. Slackers, not taking the early game advantage."
ssh "ฮึ ฉันอุตส่าห์จะหาคนมาทำเยอะ ๆ แท้ ๆ แต่ทุกคนก็ขี้เกียจเหลือเกิน คิดว่าไม่เป็นไรเพราะยังอีกนานกว่าจะถึงเวลา\nขี้เกียจจริง ๆ ที่ไม่ยอมเดินเกมก่อน"

show shizu cross_angry
with charachange

# ssh "“Still” six months away? If they aren't making their move now, they don't deserve a vote!"
ssh "ยังอีก “ตั้ง” หกเดือนเหรอ ถ้ายังไม่เริ่มทำอะไรตอนนี้ก็ไม่สมควรมีใครกาให้หรอก!"

show mishashort sign_smile
with charachange

# mi "Do they really think it's such an easy job that they can do everything at the last minute and just coast into the role~? Insulting~! Really~, really~!"
mi "คิดเหรอว่าเป็นงานง่ายถึงขั้นที่จะมาปั่นเอานาทีสุดท้ายแล้วเดินลอยชายเข้ามารับตำแหน่งได้เลยน่ะ~ ดูถูกกันมาก~!\nจริง~ จริงเลย~!"

show mishashort hips_frown
with charachange

# mi "They're going to be eaten alive once they have to sit at this tiny desk and see just how much work they have to do~!"
mi "ถ้าได้มานั่งที่โต๊ะเล็ก ๆ ตัวนี้แล้วเห็นกองงานเท่าภูเขาแล้วคงไม่เหลือสภาพแน่~!"

show shizu behind_frustrated
with charachange

# ssh "If this were a real election, they would be in deep trouble. I was reading about Japanese campaigning laws the other day. Only the bad ones, for some reason."
ssh "ถ้าเป็นเลือกตั้งจริงคงไม่รอดแล้ว วันก่อนฉันไปอ่านพระราชบัญญัติการเลือกตั้งสมาชิกสภาผู้แทนราษฎรญี่ปุ่นมา\nแต่อ่านเฉพาะส่วนที่แย่นะ ไม่รู้ทำไมเหมือนกัน"

# hi "For some reason."
hi "ไม่รู้ทำไมเหมือนกัน"

# "For a second, Shizune was “talking” like her father there, and it was coming out of Misha's mouth. Creepy."
"เมื่อกี้แวบหนึ่งชิซูเนะ “คุย” เหมือนอย่างกับพ่อเธอเลย แล้วดันออกมาจากปากมิช่าอีก ขนลุก"

# hi "Well, first off, shadow shogun, you can't really make that call. They'll be elected. Second, it's just a school election. It's not like running for city council, or the Diet. I don't think Japanese campaigning laws apply."
hi "เอาละ อย่างแรกเลยนะครับท่านผู้กุมอำนาจอยู่เบื้องหลัง คุณไม่ใช่คนที่จะตัดสินใจเรื่องนั้นครับ เดี๋ยวคนจะเลือกตั้ง\nกันมาเอง อย่างที่สอง อันนี้มันแค่เลือกตั้งกันในโรงเรียนครับ เราไม่ได้จะเลือกตั้งสมาชิกสภาท้องถิ่นหรือรัฐสภากัน\nนะครับ พระราชบัญญัติการเลือกตั้งสส. ญี่ปุ่นอะไรนั่นไม่น่าเกี่ยวกันนะครับ"

# "Third, although I don't want to say it, I'm nervous that Shizune is so enthusiastic about this, talking of elections and votes."
"อย่างที่สาม ซึ่งฉันไม่อยากพูด คือฉันใจคอไม่ดีที่ชิซูเนะคุยเรื่องการเลือกตั้งและดูกระตือรือร้นกับเรื่องนี้เหลือเกิน"

# "According to her dad, she wasn't even elected herself. Come to think of it, I can't remember Shizune ever saying she was elected, either."
"พ่อเธอบอกว่าเธอไม่ได้รับเลือกตั้งมาด้วยซ้ำ จะว่าไปแล้ว เหมือนชิซูเนะก็ไม่เคยบอกด้วยว่าตัวเองได้รับการเลือกตั้งมา\nเหมือนกัน"

# "Then, did she get this position by being recruited into the Student Council, and having it fall apart until she was the only one left? Somehow, I'd never considered it."
"แล้วที่ได้ตำแหน่งนี้มาเพราะสมัครเข้าสภานักเรียนแล้วอยู่จนสภานักเรียนล่มจนเหลือแค่เธอคนเดียวเหรอ ไม่เคย\nลองคิดอย่างนั้นมาก่อนเลยแฮะ"

# "I don't know what to think about that, but it wouldn't surprise me. We're only three people strong now."
"ไม่รู้ว่าใช่อย่างนั้นหรือเปล่า แต่ถ้าใช่ก็คงไม่แปลก ตอนนี้เหลือแค่เราสามคนทรงอำนาจอยู่"

# "If the circumstances behind her becoming the Student Council president were that sad, I wonder if there will be a vote at all. Interest could just be that low; or nonexistent, really. Then all her energy would be going towards nothing."
"ถ้าที่มาของตำแหน่งเธอมันจะหดหู่ขนาดนั้นแล้วจะได้จัดเลือกตั้งหรือเปล่า คงไม่ค่อยมีใครสนใจ หรือไม่ก็ไม่มีใคร\nสนใจเลย ซึ่งจะแปลว่าที่เธอทุ่มเทไปก็เสียเปล่า"

# "I slap an exclamation mark on the end of the poster I'm working on. It's a little plain, so I think adding one is okay. Actually, it still might be a little too plain. I make the mark twice as large."
"ฉันเติมเครื่องหมายอัศเจรีย์ใส่โปสเตอร์ที่ฉันกำลังทำอยู่ เติมหน่อยคงไม่เป็นไรเพราะตัวโปสเตอร์ก็ดูเรียบไปหน่อย\nอันที่จริง เติมแล้วก็อาจจะยังดูเรียบไปหน่อยอยู่ดี ขยายขนาดขึ้นเป็นสองเท่าเลยดีกว่า"

# hi "I still say you need to slow down. If this stuff isn't going to be relevant for months, maybe you're working a little too hard on it. That's what I think. You're worrying too much."
hi "แต่นั่นแหละ เพลา ๆ ลงหน่อยก็ดีนะ ถ้ายังมีเวลาอีกหลายเดือนแล้วทุ่มขนาดนี้ก็เกินไปมั้ง ฉันคิดว่างั้นนะ เธอพะวง\nมากไปแล้ว"

# "I don't know how to sign the word “relevant.” I try, and only end up flicking a long line of paint where I didn't intend to. There is no way I can fix that."
"ฉันทำภาษามือคำว่า “พะวง” ไม่เป็น พอจะลองทำก็กลายเป็นว่ามือเผลอลากสีเป็นเส้นไปใส่ตรงที่ไม่ได้อยากใส่ จะแก้\nก็ไม่ได้แล้ว"

# hi "Misha, can you ask her that?"
hi "มิช่า ฝากบอกให้หน่อยได้มั้ย"

show mishashort sign_smile
with charachange

show shizu adjust_happy
with charachange

# "Shizune giggles silently, clenching her teeth so that no sound actually comes out."
"ชิซูเนะขำอยู่เงียบ ๆ กัดฟันกลั้นเสียงเอาไว้"

show shizu behind_blank
with charachange

# ssh "Because there is a lot to worry about."
ssh "เพราะมีเรื่องให้พะวงหลายอย่างไง"

# hi "Like what?"
hi "เช่นอะไร"

show shizu basic_normal
with charachange

# ssh "Like… usually the boxes end up looking very pretty, so people take them. Have to plan for that."
ssh "เช่น… กล่องมันจะสวยจนคนเอาไป ต้องวางแผนเผื่อไว้"

show mishashort hips_grin
with charachange

# mi "Wahaha~! We should make them funny-looking this time, then, so no one will take them! How about that, Shicchan~?"
mi "วะฮ่าฮ่า~! งั้นคราวนี้ก็ต้องทำตลก ๆ ให้ไม่มีใครกล้าเอาไปเลย! เป็นไงชิจัง~"

# hi "We can draw some weird faces on them. Or we can put a little picture of Shizune on each one saying “Stealing is wrong.”"
hi "วาดหน้าคนหน้าอะไรเพี้ยน ๆ ติดก็ได้นะ ไม่ก็แปะรูปชิซูเนะใบเล็ก ๆ ไว้แล้วเขียนบนแต่ละใบว่า “ขโมยไม่ดีนะ”"

show shizu behind_frown
with charachange

# ssh "No. It's not funny! It's not the only problem, either. There is voter turnout, of course…"
ssh "ไม่ ไม่ตลก! ปัญหาไม่ได้มีแค่เรื่องนั้นด้วย ไหนจะเรื่องสัดส่วนคนที่ออกมาเลือกตั้งอีก…"

show shizu basic_normal2
with charachange

# ssh "…And then the worst case scenario would be not having any candidates."
ssh "…แล้วกรณีที่แย่ที่สุดก็คือการที่ไม่มีผู้สมัครเลย"

# "Although it seems she meant it jokingly, from the way she smiles as she signs it, that isn't how it comes out."
"ถึงดูเหมือนเธอจะพูดหยอกเล่น แต่ดูจากรอยยิ้มกับท่าทางในภาษามือแล้วดูท่าว่าจะจริงจัง"

show mishashort cross_laugh
with charachange

# "Even Misha understands that the possibility is very real, and though she tries to salvage the mood by punctuating Shizune's statement with a laugh, it doesn't work."
"แม้แต่มิช่ายังรู้ว่ามีความน่าจะเป็นที่จะเป็นอย่างนั้นจริง ๆ และแม้ตัวมิช่าจะพยายามคลายอารมณ์ที่ตึงเครียด\nด้วยการหัวเราะคั่นคำพูดของชิซูเนะแล้วก็บรรยากาศก็ยังไม่ดีขึ้น"

show shizu behind_frustrated
with charachange

shi "…"

show shizu basic_angry
with charachange

# ssh "What is wrong with both of you?"
ssh "พวกเธอสองคนเป็นอะไรไป"

show shizu adjust_frown
with charachange

# ssh "I was just making a joke. There actually is some interest this year. If there wasn't, would I be doing all this work? I'm not stupid."
ssh "แค่ล้อเล่นหรอกน่า ที่จริงปีนี้ยังพอมีคนสนใจอยู่บ้าง ถ้าไม่มีฉันจะมาทำอะไรถึงขนาดนี้เหรอ ฉันก็ไม่ได้โง่สักหน่อย"

show shizu behind_smile
with charachange

# ssh "When the elections are over, I'll buy everyone dinner. I'm already planning it."
ssh "ถ้าเลือกตั้งเสร็จแล้วเดี๋ยวฉันเลี้ยงข้าวเย็น กำลังวางแผนอยู่เลย"

# hi "Even the new Student Council?"
hi "เลี้ยงสภารุ่นใหม่ด้วยเหรอ"

show shizu adjust_smug
with charachange

# ssh "No, they can buy their own celebration dinner. It will only be for the current Student Council. I'll be happy once I'm through having to do these thankless jobs all the time."
ssh "ไม่หรอก ถ้าพวกนั้นอยากกินมื้อเย็นฉลองก็ให้ซื้อกันเองเอา ที่ฉันเลีี้ยงรอบนี้เฉพาะรุ่นปัจจุบัน ถ้าจบงานเพื่อส่วนรวม\nพวกนี้ที่ต้องทำมาตลอดได้แล้วฉันก็จะโล่งสักที"

show mishashort hips_grin
with charachange

# mi "A dinner just for us~? Yay~! It's like a little party, Shicchan~!"
mi "มื้อเย็นของเราสามคนเหรอ~ เย้~! เหมือนงานเลี้ยงขนาดย่อมเลยชิจัง~!"

stop music fadeout 3.0

# "Though her cheerfulness is obviously forced, I say nothing. For the rest of the period, which fortunately isn't very long, we work in silence."
"ถึงฉันจะเห็นชัดว่าจริง ๆ แล้วเธอฝืนทำร่าเริงแต่ก็ไม่ได้พูดอะไร เวลาทั้งคาบที่เหลือ—ซึ่งแย่หน่อยตรงที่เหลือไม่มาก\nแล้ว—เราก็ทำงานกันไปเงียบ ๆ"

scene bg school_hallway3
with shorttimeskip

play music music_daily fadein 0.5

# "After classes, I find the student council room locked. It's strange, because Shizune was so busy earlier that I would expect her to continue working after school. It would be what she would normally do."
"พอเลิกเรียนแล้วมาดูที่ห้องสภานักเรียนก็เห็นว่าประตูล็อก แปลก เมื้อกี้ก็เห็นชิซูเนะยุ่งอยู่ นึกว่าจะเอางานมาทำต่อ\nหลังเลิกเรียนด้วย เพราะปกติจะเป็นอย่างนั้น"

# "Maybe she listened to my suggestion and decided to take a break. I'm hoping it's that simple."
"อาจจะฟังที่ฉันบอกเลยไปพักบ้าง หวังว่าเรื่องจะมีแค่นั้นนะ"

scene bg school_courtyard_ss
with locationskip

# "Feeling a little uneasy, I take a brief stroll around the school. It's only half-conscious; I can't remember when I started moving my feet, but I've already covered enough of the campus that I'm starting to feel tired. Not that that means anything, now."
"ฉันเดินเล่นอยู่ในโรงเรียนสักหน่อยคลายความอึดอัดเล็กน้อยที่อยู้ในตัว ซึ่งขาก็ไปแบบกึ่งอัตโนมัติ ฉันจำไม่ได้ด้วยซ้ำ\nว่าเริ่มออกเดินตอนไหน แต่เหมือนจะเดินอยู่ในโรงเรียนเยอะพอที่จะทำให้เริ่มเหนื่อยแล้ว แต่ก็ใช่ว่าจะมีอะไรเป็นพิเศษ\nน่ะนะ"

# "Just a short stroll around the school grounds, and I'm already winded. Really pathetic."
"เดินเล่นนิด ๆ หน่อย ๆ อยู่ในโรงเรียนก็หอบรับประทานแล้ว น่าสมเพชจริง ๆ"

scene bg school_hallway3
with locationskip

# "Before I know it, I'm back in front of the student council office. There's someone else, too, this time."
"รู้ตัวอีกทีก็กลับมาอยู่ที่หน้าห้องสภานักเรียน แต่คราวนี้มีคนแล้ว"

show mishashort hips_smile at center
with charaenter

# mi "Hi, Hicchan~!"
mi "ไงฮิจัง~!"

# hi "It's locked."
hi "ประตูล็อก"

# "Seeing a can of lemonade in her hand, I reflexively start looking for a vending machine nearby. I'm so thirsty."
"พอเห็นกระป๋องน้ำมะนาวในมือมิช่าแล้วตาก็สอดส่ายหาตู้ขายของแบบหยอดเหรียญไปโดยอัตโนมัติ ตอนนี้ฉันคอแห้ง\nเอามาก ๆ"

show mishashort sign_smile
with charachange

# mi "I know that, Hicchan~! Shicchan is somewhere else, I guess~!"
mi "รู้น่าฮิจัง~! ชิจังคงไม่อยู่ละมั้ง~!"

# hi "Weird."
hi "แปลก"

show mishashort hips_grin
with charachange

# mi "Ahahaha~. We aren't stuck together, Hicchan~."
mi "อะฮ่าฮ่าฮ่า~ เราสองคนไม่ได้ตัวติดกันสักหน่อยฮิจัง~"

# "Misha takes a long drink from her lemonade, eventually just tipping it over and pouring the rest into her mouth. I feel like I am being mocked."
"มิช่ากระดกดื่มน้ำมะนาวอึกใหญ่ จนสุดท้ายเธอจับกระป๋องดิ่งให้น้ำที่เหลืออยู่ข้างในไหลเข้าปากตัวเอง รู้สึกเหมือน\nโดนเยาะเย้ยยังไงไม่รู้"

show mishashort perky_smile
with charachange

# mi "Do you want one, Hicchan~?"
mi "อยากดื่มบ้างเหรอฮิจัง~"

# hi "No, it's okay. I can't take someone else's drink, it's rude. Besides, you're making fun of me, aren't you? I just saw you inhale all of that."
hi "ไม่เป็นไร ๆ ฉันดื่มอะไรของคนอื่นไม่ได้หรอก เสียมารยาทแย่ อีกอย่าง นี่เธอเยาะเย้ยกันใช่มั้ย เมื่อกี้เห็นสูบเอาจน\nหมดกระป๋องเลย"

show mishashort sign_smile
with charachange

# mi "I have another one in my bag~! I was prepared, see~, see~? I'm just like Shicchan~!"
mi "ยังมีในกระเป๋าฉันอีกกระป๋องนะ~! ฉันเตรียมไว้แล้ว เห็นมั้ย~ เห็นมั้ย~ เหมือนชิจังเลย~!"

# hi "She's a little too prepared. It's good some of that is rubbing off on you, anyway. After what, two years?"
hi "รายนั้นก็เป็นคนเตรียมพร้อมไปหน่อยอะ แต่อยู่ด้วยกันมาตั้ง เท่าไหร่นะ สองปี? เธอติดนิสัยมาบ้างก็ดีแล้วละ"

show mishashort cross_laugh
with charachange

# mi "Wahaha~!"
mi "วะฮ่าฮ่า~!"

# "The way she stares at me as I drink it is a little disconcerting, but I'm too grateful to care much about it."
"พอเธอจ้องตอนฉันดื่มอยู่ก็แอบอึดอัดแฮะ แต่ช่างเถอะ ให้ดื่มนี่ก็บุญโขแล้ว"

# hi "You and Shizune always end up treating me to something. It's starting to embarrass me."
hi "ทั้งเธอทั้งชิซูเนะได้เลี้ยงอะไรฉันตลอดเลย ชักอายแล้วสิ"

show mishashort hips_smile
with charachange

# mi "Really~, Hicchan? Ahaha~. Buy me lunch sometime, then, okay~? Then~!, we'll be even."
mi "จริงเหรอ~ ฮิจัง อะฮ่าฮ่า~ งั้นไว้เลี้ยงข้าวเที่ยงฉันบ้างนะ~ แล้วเรา~! จะได้เจ๊ากัน"

# hi "Well, it's funny you should say that. I was going to ask you if you wanted to eat in town…"
hi "เออ บังเอิญดีนะ ฉันกะจะชวนเธอเข้าเมืองไปกินข้าว…"

show mishashort hips_grin
with charachange

# mi "Yeah~ yeah~! I'm really hungry today, Hicchan! Thanks!"
mi "อื้ม~ อื้ม~! วันนี้ฉันหิวมากเลยละฮิจัง! ขอบใจนะ!"

show mishashort invis at tworight
with dissolvecharamove

stop music fadeout 3.0

# "…Yesterday. I was going to ask her yesterday. Misha cuts me off before I can finish the sentence, and I can't find an opening to correct her as she dashes enthusiastically around me, laughing, her arms flapping excitedly at her sides."
"…เมื่อวาน ฉันกะจะชวนเมื่อวาน มิช่าแทรกก่อนที่ฉันจะทันได้พูดให้จบ และไม่มีช่องให้ฉันได้แก้เลยเพราะเธอโดดไป\nโดดมาอยู่รอบตัวฉันหัวเราะสะบัดแขนขาด้วยความตื่นเต้น"

scene bg suburb_roadcenter_ss
with locationskip

play music music_dreamy fadein 2.0

# "I already have my wallet with me, so I start walking towards town with Misha trailing behind me, playing idly with her hands and loudly wondering to herself where we should go eat. At least, I think so. She could be asking me."
"ฉันพกกระเป๋าสตางค์ติดตัวมาด้วยแล้วจึงเดินเข้าเมืองไปโดยที่มีมิช่าตามหลังอยู่ เธอจับมือตัวเองเล่นไปมาพลางถาม\nด้วยความสงสัยว่าจะไปกินที่ไหนดี ก็น่าจะถามฉันแหละนะ คงไม่ได้พูดกับตัวเองหรอก"

# hi "Do you have anywhere specific where you want to go?"
hi "เธออยากไปร้านไหนเป็นพิเศษมั้ย"

show mishashort hips_smile_ss at center
with charaenter

# mi "Hmmm~. I want to go to the teahouse, they have a really big parfait there."
mi "อืมมม~ ฉันอยากไปที่โรงน้ำชานั้น ร้านนั้นมีพาร์เฟต์แก้วใหญ่ขายด้วย"

# hi "I saw you eat a parfait there last time, it looked really big."
hi "เห็นเธอกินคราวที่แล้วก็ใหญ่จริง ๆ แหละ"

show mishashort hips_grin_ss
with charachange

# mi "No no no~! This one is really, really~ big! It's also really expensive~!"
mi "ไม่ ๆ ๆ ~! อันนี้ใหญ่ ใหญ๊~ ใหญ่! แพงมากด้วย~!"

# hi "Really, really~ expensive?"
hi "แพง แพ๊ง~ แพงมากเลยเหรอ"

show mishashort cross_laugh_ss
with charachange

# mi "Hahaha~! A little~…"
mi "ฮ่าฮ่าฮ่า~! ก็นิดหน่อย~…"

# hi "Jeez. Well, you and Shizune paid for my food a bunch of times, so it's fine."
hi "ดูพูดเข้า เอาเถอะ เธอกับชิซูเนะก็เลี้ยงฉันมาหลายรอบละ ไม่เป็นไรหรอก"

show mishashort perky_confused_ss
with charachange

# mi "Hicchan, I don't think I ever did that~. Are you sure it wasn't just Shicchan?"
mi "ฮิจัง ฉันว่าฉันไม่เคยเลี้ยงเลยนะ~ แน่ใจนะว่าคนที่เลี้ยงไม่ได้มีแค่ชิจัง"

# hi "Are you really arguing against a free meal? Don't worry about it."
hi "คนเขาเลี้ยงนี่จะไม่เอาจริงเหรอ ไม่ต้องคิดมากน่า"

scene bg suburb_shanghaiint
with locationskip

# "We go to the Shanghai, and are seated by a waitress who is surprisingly not Yuuko."
"เราตรงไปร้านเซี่ยงไฮ้แล้วนั่งรอพนักงานเสิร์ฟ ซึ่งน่าแปลกที่ไม่ใช่ยูโกะ"

# "Misha is very eager to eat that parfait, because she shouts her order as soon as she walks through the door. When it arrives, I can see that it is both very big and very expensive-looking."
"มิช่าดูจะหิวพาร์เฟต์มาก ๆ เพราะพอเดินเข้าร้านมาเธอก็สั่งทันที พอได้เห็นพาร์เฟต์ที่ว่ามาเสิร์ฟแล้วก็รู้สึกว่าดูใหญ่\nและแพงมากจริง ๆ"

show mishashort perky_confused_close at center
with charaenter

# mi "Aren't you going to order anything, Hicchan~? If you're hungry, we can share."
mi "จะไม่สั่งอะไรเลยจริงเหรอฮิจัง ถ้าหิวก็แบ่งกันกินได้นะ"

# hi "Nah. I don't like parfaits. I don't like pralin."
hi "ไม่อะ ฉันไม่ชอบพาร์เฟต์ ไม่ชอบถั่วบดด้วย"
#http://en.wikibooks.org/wiki/Cookbook:Pralin vs. http://en.wikipedia.org/wiki/Granola I'm actually not too happy either way, but eh. -SC

show mishashort sign_smile_close
with charachange

# mi "You can pick it out~!"
mi "เขี่ยออกก็ได้นี่~!"

# hi "You can't just pick out pralin; don't be silly."
hi "ถั่วบดมันเขี่ยออกได้ที่ไหน พูดอะไรบ้า ๆ"

show mishashort perky_smile_close
with charachange

# "Even if I could, Misha is mashing her food together to the point where it is no longer possible. It also looks kind of gross."
"ถึงตอนแรกจะเขี่ยได้ แต่มิช่าก็คนจนตอนนี้เขี่ยออกไม่ได้แล้ว ดูขยะแขยงหน่อย ๆ ด้วย"

# "I wonder if that many flavors can even blend together well. Can she really taste anything in that goop? She is acting like it's delicious, anyway."
"คนขนาดนั้นรสชาติจะไม่ตีกันแย่เหรอ ก้อนเหลว ๆ นั่นจะมีรสอะไรขึ้นมาได้จริงเหรอ แต่มิช่าก็กินด้วยท่าทีที่เหมือน\nจะอร่อย"

show mishashort hips_grin_close
with charachange

# mi "Mm~. Parfaits are the best~, I have sensitive teeth, so ice cream is a no-no~. Cake is too soft, though, and if there is too much icing, I get bored. Parfait is interesting."
mi "อื้ม~ พาร์เฟต์เนี่ยสุดยอดเลย~ ฉันเสียวฟันเลยกินไอศกรีมไม่ได้~ เค้กก็นิ่มไป แล้วถ้ามีของแต่งหน้าเยอะไปฉันก็\nจะเบื่อ พาร์เฟต์นี่แหละน่าสนใจ"

show mishashort perky_smile_close
with charachange

# mi "How many cafés have parfaits here~? I think, ten! I've tried them all, I like this one the best. It has a little flan~!"
mi "แถวนี้มีคาเฟที่ขายพาร์เฟต์กี่ที่กันนะ~ ฉันว่าน่าจะสิบที่! ฉันไปลองชิมมาหมดแล้ว ฉันชอบของร้านนี้ที่สุด มีฟลาน\nก้อนเล็ก ๆ ให้ด้วย!"

# hi "You sound like you're some kind of dessert expert."
hi "นี่เธอเป็นผู้เชี่ยวชาญด้านขนมหวานหรือเปล่า"

show mishashort hips_smile_close
with charachange

# mi "Not just dessert~! I want to eat all kinds of delicious things~."
mi "ไม่ใช่แค่ขนมหวาน~! ฉันอยากกินอะไรอร่อย ๆ หมดเลย~"

show mishashort hips_grin_close
with charachange

# mi "Someday, I'll have enough money to buy a two kilogram Matsusaka beef steak~!"
mi "สักวันฉันจะเก็บเงินซื้อสเต๊กเนื้อมัตสึซากะสักสองกิโลเลย~!"

# hi "That's like over a hundred thousand yen… I guess this kind of decadent food is kind of your hobby then, huh?"
hi "ซื้อขนาดนั้นราคาคงเป็นแสนเยนได้มั้ง… งั้นการกินอาหารทราม ๆ อะไรพวกนี้คงเป็นงานอดิเรกของเธองั้นสิ"

# "A hobby isn't something that should take months to learn about someone. I've been very rude, in retrospect. Also, that is one pricey hobby."
"สองสามเดือนคงจะน้อยไปหน่อยกับการดูว่าใครมีงานอดิเรกอะไร พอมาย้อนคิดดูแล้วก็เสียมารยาทมากเลยแฮะ\nแถมเป็นงานอดิเรกที่แพงเสียด้วย"

show mishashort perky_confused_close
with charachange

# mi "I guess so~! …Decadent~?"
mi "มั้งนะ~!…ซาม ๆ ~?"

# hi "Yeah."
hi "อื้ม"

show mishashort hips_grin_close
with charachange

# "Misha giggles, raising her hand to her face. It looks like some ice cream accidentally got on her nose. She doesn't notice it. I can't stop noticing it. I wish she would wipe it off. I'm about to tell her about it, but she suddenly says,"
"มิช่าหัวเราะคิกคักยกมือขึ้นแตะหน้า เหมือนที่จมูกจะมีไอศกรีมติดอยู่แต่เธอยังไม่รู้ตัว ฉันละสายตาไปไม่ได้ เมื่อไหร่\nจะเช็ดสักทีนะ พอฉันจะบอกเธอก็โพล่งขึ้นมาว่า"

show mishashort perky_confused_close
with charachange

# mi "I don't know what that means."
mi "ฉันไม่รู้ความหมายของคำนั้นอะ"

# hi "Oh. I guess that's a bad word, anyway. It has implications. Epicurean is better. It means, someone who enjoys eating nice food. That's the adjective, though. So, epicure is the word for it."
hi "อ้อ ก็คำไม่ค่อยดีเท่าไหร่หรอก มันสื่ออะไรหลายอย่าง ใช้คำว่าแสวงรสดีกว่า อารมณ์เหมือนการตามหาอะไรที่รสชาติ\nอร่อย ๆ มากิน ถ้าจะเติมเข้ามาให้เป็นการพูดถึงคนก็ นักแสวงรส งี้"

show mishashort cross_laugh_close
with charachange

# mi "Wahaha~!"
mi "วะฮ่าฮ่า~!"

show mishashort cross_grin_close
with charachange

# mi "Hicchan, you're too wordy."
mi "ฮิจัง นายใช้คำยากไปนะ"

# hi "Sorry."
hi "ขอโทษที"

show mishashort perky_smile_close
with charachange

# mi "Hahaha~. I think that is what Shicchan likes about you."
mi "ฮ่าฮ่าฮ่า~ แต่ฉันว่าชิจังชอบนายก็ตรงนี้แหละ"

# hi "Because I'm wordy? I need to buy some thesauruses, then."
hi "เพราะฉันใช้คำยากเหรอ งั้นเดี๋ยวต้องไปหาซื้อหนังสือรวมคำคล้ายแล้ว"

show mishashort hips_grin_close
with charachange

# mi "Wahaha~! No, not like that, Hicchan~!"
mi "วะฮ่าฮ่า~! ไม่ ไม่ใช่อย่างนั้นสักหน่อยฮิจัง~!"

# "I decide to order some coffee after all, but it takes a while to get the waitress to notice, and I think actually getting my coffee will take about as long."
"สุดท้ายฉันก็สั่งกาแฟ แต่ก็ต้องรอสักพักกว่าพนักงานจะเห็น และกว่าจะได้กาแฟก็คงนานพอกัน"

# "The tea shop is filling up. No surprise, as we've already been here for almost an hour while she was chipping at that dessert. I order my coffee to go, but Misha orders one as well, so it seems that we're going to be here longer than I thought."
"คนเริ่มเข้าโรงน้ำชามามากขึ้นเรื่อย ๆ ก็ไม่แปลก ตอนที่นั่งรอมิช่ากินของหวานนี่ก็อยู่มาเกือบชั่วโมงแล้ว ฉันสั่งกาแฟ\nแบบถือกลับบ้าน แต่มิช่าก็สั่งตาม ดูท่าว่าจะได้แช่อยู่ที่นี่นานกว่าที่คาดเอาไว้"

# hi "I really wish it was that easy. It's hard to talk to her lately."
hi "ถ้ามันง่ายอย่างนั้นก็ดีสิ ช่วงนี้แทบไม่ได้คุยกับชิซูเนะเลย"

show mishashort sign_smile_close
with charachange

# mi "Shicchan's been busy because of the elections~!"
mi "ชิจังงานยุ่งเพราะเรื่องเลือกตั้งไง~!"

# hi "I know we can't have fun all the time. It's just that there's a lot I want to say to her, I think. I always screw up when the time comes, though. And I don't even have the time now. Because of the elections."
hi "ฉันรู้น่าว่าเราจะอยู่ด้วยกันสบาย ๆ ไปไม่ได้ตลอดหรอก แค่ว่าฉันมีเรื่องอยากบอกเธอเยอะไปหมด มั้งนะ แต่พอถึงเวลา\nฉันก็ไม่ได้พูด แล้วตอนนี้ก็ไม่มีเวลาด้วยแล้วเพราะเรื่องเลือกตั้งอีก"

# hi "They're not for a while, though."
hi "ทั้งที่เลือกตั้งก็อีกนาน"

show mishashort hips_frown_close
with charachange

# mi "Hicchan, do you think that Shicchan is avoiding you?"
mi "ฮิจัง นายคิดว่าชิจังหลบหน้านายเหรอ"

# "Misha sounds angry. That's to be expected, but I don't feel that way at all."
"น้ำเสียงมิช่าฟังดูโกรธ ซึ่งก็ไม่แปลก แต่ฉันไม่ได้คิดอย่างนั้นเลย"

# hi "No."
hi "เปล่า"

show mishashort perky_sad_close
with charachange

# mi "Is that so~…"
mi "งั้นเหรอ~…"

# "The dreamy way in which she says it makes me think that Misha is disappointed with my answer. In that case, it could be how she feels. I'm uneasy asking such a question, but I trust Misha would answer it honestly. Otherwise, I wouldn't even dream of it."
"น้ำเสียงเลื่อนลอยของเธอทำให้ฉันคิดว่ามิช่าผิดหวังกับคำตอบของฉันหรือเปล่า ถ้างั้นเธอก็คงคิดว่าชิซูเนะหลบหน้า\nเธออยู่ จะถามก็กระดากปาก แต่หวังว่ามิช่าจะตอบตรง ๆ นะ เพราะฉันนึกภาพเธอโกหกไม่ออกเลย"

# hi "Do you?"
hi "แล้วเธอคิดงั้น?"

show mishashort hips_smile_close
with charachange

# mi "No, of course not, Hicchan~! But~! …It's frustrating, sometimes~. Shicchan has so much energy, and is always trying to make people feel as excited about things as she is~."
mi "ไม่ ไม่เลยฮิจัง~! แต่~! …บางทีมันก็น่าหงุดหงิด~ ชิจังน่ะมีพลังเยอะ แถมยังคอยโหมให้คนอื่นตื่นเต้นไปด้วย\nอยู่เรื่อยเลย~"

show mishashort perky_sad_close
with charachange

# mi "But it's like Shicchan doesn't know how to handle things when everyone gets really hyped up. Or~! I think that she wants to make sure nothing goes wrong. When I want to help out, Shicchan always pushes me away."
mi "แต่เหมือนชิจังไม่รู้จะรับมือยังไงต่อพอทุกคนตื่นเต้นกันมาก ๆ แล้ว หรือไม่ก็~! ฉันว่าชิจังอาจจะอยากให้ทุกอย่าง\nราบรื่นดี พอฉันเสนอตัวจะช่วย ชิจังก็ผลักไสฉันตลอดเลย"

# mi "It's frustrating."
mi "น่าหงุดหงิดนะ"

show mishashort hips_grin_close
with charachange

# mi "I'm just overthinking it, probably~! Right~?"
mi "ฉันแค่คิดมากไปเอง มั้ง~! ใช่มั้ย~"

# "Misha takes a big gulp from her cup of coffee, then sticks her tongue out."
"มิช่าดื่มกาแฟอึกใหญ่แล้วแลบลิ้น"

show mishashort hips_laugh_close
with charachange

# mi "Ow~! Hot~ hot~ hot~… thought it would have cooled down by now~!"
mi "โอ๊ย~! ร้อน~ ร้อน~ ร้อน~… อุตส่าห์ทิ้งไว้ นึกว่าจะเย็นแล้ว~!"

# hi "Has it really been that long?"
hi "เพิ่งแป๊บเดียวเองไม่ใช่เหรอ"

# "I check my watch. It hasn't been very long at all, but looking outside, the sun is already starting to set."
"ฉันก้มมองนาฬิกาตัวเอง ยังผ่านไปไม่ทันเท่าไหร่เลย แต่พอหันมองนอกหน้าต่างก็เห็นว่าพระอาทิตย์คล้อยตกดินแล้ว"

# hi "Not really. Huh, it got dark out pretty quickly today, though, so I could understand why you might think that."
hi "ก็ไม่นานนี่ อืม แต่ดูเหมือนวันนี้จะมืดเร็วพอตัวเลยนะ ก็คงไม่แปลกที่เธอจะนึกว่านานแล้ว"

show mishashort perky_sad_close
with charachange

# "At my words, Misha looks outside and yawns almost immediately. She looks sleepy. That's funny, because…"
"พอมิช่าได้ยินที่ฉันพูดแล้วเธอก็หันมองข้างนอกแล้วหาวแทบจะทันที สีหน้าดูง่วง ๆ ซึ่งตลกดี เพราะ…"

# hi "Are you sleepy? You were wide awake like, just two seconds ago."
hi "ง่วงเหรอ แต่แบบ สองวินาทีเมื่อกี้เธอยังตื่นเต็มตาอยู่เลย"

show mishashort sign_sad_close
with charachange

# mi "I feel tired when it gets dark, Hicchan~."
mi "พอมืดแล้วฉันจะง่วงน่ะฮิจัง~"

# hi "Just like that? Are you a bird?"
hi "ง่าย ๆ งี้เลย? เป็นนกเหรอ"

show mishashort perky_smile_close
with charachange

# mi "Ahahaha~."
mi "อะฮ่าฮ่าฮ่า~"

# "I pick up my own coffee and have a sip. It's not very hot at all, but very tasty. I down it as quickly as possible, because now I want to get back to my dorm room as well. Misha tries to emulate me, but it's still too hot for her."
"ฉันยกถ้วยกาแฟขึ้นมาจิบ ซึ่งไม่ร้อนเท่าไหร่แต่อร่อยมาก ฉันรีบดื่มให้ไวที่สุด เพราะตอนนี้ฉันก็อยากกลับหอแล้ว\nเหมือนกัน มิช่าจะกระดกตามฉันบ้าง แต่เหมือนกาแฟจะยังเย็นไม่พอสำหรับเธอ"

# "While I wait for her to finish, I start to wonder what she meant back then about Shizune liking something about me. Suddenly, I'm very curious, but dragging that back up now feels like an unnecessary action."
"ในหัวฉันคิดไปถึงเรื่องที่มิช่าบอกว่าชิซูเนะชอบบางอย่างในตัวฉันระหว่างที่รอเธอดื่มกาแฟให้หมด อยู่ ๆ ก็อยากรู้\nขึ้นมาแบบมาก ๆ แต่จะให้ย้อนกลับมาถามเรื่องนี้อีกก็ดูจะวุ่นวายไปหน่อย"

show mishashort hips_grin_close
play sound sfx_impact
with vpunch

# "I try to weigh the option again, but am interrupted by Misha slamming her empty cardboard cup down on the table with a loud pop."
"ฉันคิดอยู่ว่าสิ่งนั้นคืออะไรกันแน่ แต่แล้วเสียงถ้วยกระดาษเปล่าที่เคาะกับโต๊ะจากฝั่งมิช่าก็เข้ามาขัด"

show mishashort cross_grin_close
with charachange

# mi "Done~!"
mi "หมดแล้ว~!"

# "She lets out a short laugh, seeming very pleased with herself. Kind of like a toddler. I wonder if she had that drill-shaped haircut when she was little, too. Or was it something more like her current look? It would make more sense."
"เธอหัวเราะน้อย ๆ ดูพอใจกับตัวเอง เหมือนเด็กทารกเลย ตอนเด็กเธอจะทำผมทรงสว่านแบบนั้นเหมือนกันมั้ยนะ\nหรือเพิ่งมาทำทรงสว่านเอาตอนโต? น่าจะเป็นอย่างหลังมากกว่า"

# hi "I guess we should head back then. I can't see the waitress. Try not to fall asleep while I pay for the sundae, okay?"
hi "งั้นก็กลับกันดีกว่า แต่พนักงานไปไหนเนี่ย เดี๋ยวฉันไปจ่ายค่าซันเดให้ก่อน ห้ามหลับ โอเคนะ"

show mishashort sign_smile_close
with charachange

# mi "Not a sundae; It's a parfait, Hicchan."
mi "ซันเดที่ไหนล่ะฮิจัง พาร์เฟต์ต่างหาก"

show mishashort cross_laugh_close
with charachange

# mi "Wahaha~."
mi "วะฮ่าฮ่า~"

# hi "You have ice cream on your nose."
hi "ไอศกรีมติดจมูกอยู่แน่ะ"

stop music fadeout 2.0

scene black
with dissolve

label th_S26:

scene bg school_scienceroom at right
with locationchange

play sound sfx_paper
play music music_normal fadein 3.0

# "In class the next afternoon, I'm two problems into a math logic worksheet when a folded up piece of paper hits me in the head. I'm sure I know whom it's from, but I quickly look around the classroom anyway, just in case."
"ฉันกำลังทำแบบฝึกหัดเรื่องตรรกศาสตร์อยู่ในห้องเรียนยามบ่ายถัดจากวันนั้น เมื่อทำไปได้สองข้อก็มี\nก้อนกระดาษถูกโยนมาที่หัวฉัน ถึงจะรู้แล้วแหละว่าใครโยนมา แต่ฉันก็หันไปดูเพื่อความแน่ใจอีกที"

show shizu invis at left
with None

show bg school_scienceroom at left
show shizu behind_blank at center
with dissolvecharamove

# "No one in this classroom is good at acting casual. I can tell that everyone saw who threw it at me, and looking at the culprit herself it was obviously Shizune. She isn't even trying to be coy about it."
"ในห้องเรียนไม่มีคนที่เก็บอาการเป็นเลยสักคน ฉันรู้ทันทีว่าทุกคนเห็นว่าใครโยนมา เพราะสายตาทุกคู่จับจ้องคนร้าย\nที่เห็น ๆ กันอยู่ว่าเป็นชิซูเนะ แถมยังไม่มีทีท่าว่าจะพยายามทำตัวให้เนียนด้วย"

# "The countryside is so different. At my old school I would have no idea who it was right now."
"คนที่นี่ไม่เหมือนในเมืองเลย ถ้าเป็นที่โรงเรียนเก่าฉันคงยังไม่รู้ว่าใครเป็นคนโยนมากันแน่"

# "Opening up the note, it says:"
"พอคลี่กระดาษออกดูก็เห็นข้อความที่เขียนว่า"

window hide

# $ written_note("Misha is absent! Help me out today after school!")
$ written_note("มิช่าไม่อยู่! เลิกเรียนแล้วมาช่วยงานหน่อย!")

window show

# hi "I don't understand what's with the note, why can't you just use sign language?"
hi "แล้วจะใช้กระดาษทำไม ใช้ภาษามือเอาไม่ง่ายกว่าเหรอ"

# "A large part of how I learned sign language was by copying Misha's style of signing her words as she speaks, so I end up blurting the sentence out loud as I sign it to Shizune. A slight laugh goes around the room. How awkward."
"ส่วนมากฉันก็รู้ภาษามือจากการเลียนแบบมิช่าที่พูดไปทำภาษามือไป ฉันจึงเปล่งเสียงประโยคนั้นออกมาพร้อม ๆ กับ\nการส่งภาษามือให้ชิซูเนะ มีคนในห้องหัวเราะคิกคักกัน น่าอายชะมัด"

# his "I'll help if I don't have to do a lot."
his "ถ้างานไม่เยอะฉันก็จะช่วย"

show shizu basic_angry
with charachange

# ssh "That's silly, obviously if Misha is absent you have to help as much as two people."
ssh "บ้าหรือเปล่า ถ้ามิช่าไม่อยู่ก็แปลว่านายต้องช่วยเป็นสองเท่าคนเลยสิ"

# "I don't know if that really means anything. After all, Misha was complaining yesterday mostly about how Shizune wouldn't let her help her. I don't do much as-is, either."
"มิช่าไม่อยู่แล้วงานจะเยอะขึ้นขนาดนั้นเลยเหรอ ก็เมื่อวานมิช่ายังบ่นอยู่เลยว่าชิซูเนะไม่ยอมให้ช่วยงานด้วย แล้วปกติ\nฉันก็ไม่ได้ทำอะไรเยอะอยู่แล้วด้วย"

# "After pretending to think it over for a bit, I write her a note back telling her I will. I'm actually happy that she asked me, because I've been meaning to talk to her for a while."
"ฉันทำทีเป็นคิดอยู่พักหนึ่งก่อนจะเขียนตอบตกลงว่าจะไปช่วย จริง ๆ ก็ดีใจนะที่ขอให้ไปช่วย จะได้มีเวลาคุยกันด้วย"

# "It's a good opportunity, but I feel I should at least make it look like I'm putting up some resistance to the idea."
"ก็เป็นโอกาสที่ดี แต่รู้สึกเหมือนต้องทำเป็นว่าไม่ค่อยอยากไปเท่าไหร่สักหน่อย"

hide shizu
with charaexit

# "I go back to my worksheet and immediately get stuck on the third problem. After trying to work around it, I casually toss my own note over to Shizune. It says:"
"ฉันกลับมาทำแบบฝึกหัดต่อแล้วติดอยู่กับข้อที่สามทันที พอลองทำอยู่สักพักฉันก็ปากระดาษของตัวเองไปทางชิซูเนะ\nโดยที่ในนั้นเขียนว่า"

window hide

# $ written_note("Why is Misha absent? And what's the answer to question 3?")
$ written_note("มิช่าไปไหน แล้วข้อที่สามตอบอะไร")

show shizu behind_blank at center
with charaenter

window show

# ssh "She told me that she was sick and her stomach hurt. Misha gets stomachaches a lot, but I wish she'd picked a better time for it this week."
ssh "มิช่าบอกว่าปวดท้องไม่สบายน่ะ มิช่าก็ปวดท้องบ่อยอยู่หรอก แต่ไม่น่ามาเป็นเอาวันนี้เลย"

show shizu basic_normal2
with charachange

# ssh "Use sign language."
ssh "ใช้ภาษามือสิ"

# "I'd think she has a stomachache because of the way she sucked down a parfait larger than her head the other day."
"ที่ปวดท้องก็คงเพราะสูบพาร์เฟต์ที่ใหญ่กว่าหัวเธอลงท้องไปเมื่อวานมั้ง"

# "If she gets them quite often, though, either it's a coincidence or she has a habit of eating things that can put her in debilitating pain."
"แต่ถ้าปวดท้องบ่อย งั้นก็คงแค่บังเอิญมาเป็นหลังไปกินเฉย ๆ หรือไม่ก็ชอบกินอะไรที่ทำให้ตัวเองต้องเจ็บไข้ได้ป่วย\nอยู่บ่อย ๆ"

# "I notice the teacher staring at us disapprovingly. I don't blame him. We're “talking” in class, and with sign language, in quite a visible and distracting way. I try clearing my throat to back out of our conversation, but Shizune doesn't get the hint."
"ฉันเห็นว่าครูกำลังจ้องมาทางเราด้วยสีหน้าที่ไม่ค่อยพอใจนัก ก็ว่าไม่ได้หรอก ตอนนี้เราก็กำลัง “คุยกัน” ในเวลาเรียน\nอยู่ด้วยการใช้ภาษามือที่ท่าทางออกจะรบกวนสมาธิคนอื่นอยู่เหมือนกัน ฉันกระแอมตัดบทสนทนา แต่ชิซูเนะไม่เข้าใจ\nสัญญาณที่ฉันทำ"

# "Well, obviously. Before I try to get the message across again with my hands, however, I can see Shizune notices what's up, she just doesn't care."
"ก็แหงอยู่แล้วแหละ แต่ก่อนที่ทันจะได้บอกชิซูเนะผ่านภาษามืออีกรอบฉันก็เห็นว่าจริง ๆ แล้วเธอรู้ว่าครูมองอยู่\nเพียงแต่ทำเป็นไม่สนใจ"

show shizu adjust_smug
with charachange

# ssh "Do you still want to know the answer to question 3? I will tell you, but you have to give me the answer for question 25."
ssh "ยังอยากได้คำตอบข้อที่สามอยู่มั้ย เดี๋ยวฉันจะบอกให้ แต่ขอแลกกับคำตอบข้อที่ยี่สิบห้าจากนาย"

# his "Hey, I was just thinking about how a teacher who didn't know sign language could think we were abusing it and using it to cheat, if he were to assume the worst. I can't believe you're actually doing that! And, I'm not up to 25."
his "นี่ ครูไม่รู้ภาษามือก็จริง แต่เกิดครูระแวงว่าเราแอบใช้ภาษามือโกงกันจะทำยังไง นี่เธอจะเอาอย่างนั้นจริง ๆ เหรอ!\nแล้วฉันยังทำไม่ถึงข้อที่ยี่สิบห้าเลย"

show shizu behind_frown
with charachange

# ssh "You wanted to know what the answer to 3 was; you asked first. Hypocrite."
ssh "นายขอคำตอบข้อสามมาก่อนนะ ย้อนแย้งจริง ๆ"

# his "You're the Student Council president, you can't cheat."
his "เธอเป็นสภานักเรียนนี่ โกงได้ที่ไหนล่ะ"

# "I don't have time for this, and I think I'm trying the teacher's patience to the breaking point. I'd like to continue taking potshots at her while working on the math problems in front of me, but it would require at least two extra hands."
"ไม่มีเวลามาเถียงต่อแล้ว แถมรู้สึกเหมือนครูก็เริ่มจะทนไม่ไหวแล้วเหมือนกัน อยากจะว่าชิซูเนะต่อไปพลางทำ\nแบบฝึกหัดคณิตที่อยู่ตรงหน้าไปพลางจริง ๆ แต่จะทำอย่างนั้นได้ก็ต้องมีมือเพิ่มอย่างน้อย ๆ อีกหนึ่งคู่"

show shizu basic_normal
with charachange

# "Shizune is a bit more creative, and gets around this limitation by using long, semi-broken strings of simpler words. I take a couple mental notes in between being dizzied by a couple of particularly long equations."
"ชิซูเนะทำได้อย่างแยบยลกว่าด้วยการคอยเว้นระยะส่งคำสั้น ๆ ที่เหมือนไม่ต่อเนื่องกัน ฉันคอยจดไว้ในหัวไปพร้อม ๆ\nกับความรู้สึกมึนหัวที่เกิดจากสมการสองสมการที่ยาวเป็นพิเศษ"

show shizu adjust_smug
with charachange

play sound sfx_impact2
with vpunch

# "Right before the bell rings, she caps her pen and triumphantly slams it on her desk with an ear-popping crack that makes the whole room jump, quickly forgotten because everyone would rather go to lunch than question its origin."
"ก่อนระฆังจะดังไม่กี่วินาทีชิซูเนะก็ปิดปลอกปากกาแล้วกระแทกเข้ากับโต๊ะด้วยเสียงอันดังจนทั้งห้องสะดุ้ง แต่หลังจากนั้น\nก็ไม่มีใครสนใจจะดูว่าเป็นเสียงอะไรเพราะทุกคนอยากพักเที่ยงกันแล้ว"

stop music fadeout 6.0

show shizu basic_normal_close at twoleft
with characlose

# "After a couple brief stretches, she gets up and hovers around my left shoulder."
"พอฉันยืดเส้นยืดสายอยู่สองสามครั้งชิซูเนะก็เดินมาอยู่ทางไหล่ซ้ายของฉัน"

show shizu behind_frown_close
with charachange

# ssh "Are you still not done? I was going to ask if you wanted me to hand in yours too, while I was up."
ssh "ยังไม่เสร็จอีกเหรอ กำลังจะมาถามว่าจะฝากส่งด้วยมั้ย ไหน ๆ ฉันก็ลุกมาแล้ว"

# his "Someone distracted me. I had to beg the teacher to give me nine minutes between now and the end of passing to finish it. It's not easy to solve this one-handed while having a conversation, by the way."
his "มีคนกวนสมาธิฉันน่ะสิ ฉันต้องขอครูต่อเวลาทำอีกเก้านาทีเนี่ย รู้มั้ยว่าลำบากมากนะที่ต้องทำมือเดียวแล้วอีกมือ\nใช้คุยด้วย"

# "He wasn't happy with the request, wanting to get out of here as much as I do."
"ครูเองก็ไม่ค่อยพอใจเท่าไหร่ที่ฉันขอต่อเวลาเพราะก็อยากรีบ ๆ ไปไม่ต่างกับฉัน"

# "Since I'm only one problem away from finishing, it looks like Shizune doesn't really believe me. The second that I'm done handing it in, I find myself being dragged to the student council room."
"ชิซูเนะเหมือนจะไม่เชื่อเพราะฉันเหลือข้อสุดท้ายแล้ว ทันที่ที่ฉันทำเสร็จแล้วส่งก็ถูกลากตัวมาที่ห้องสภานักเรียน"

scene bg school_council
with locationskip

play music music_happiness fadein 2.0

# "It's eerily and annoyingly clean. I can't find what I was working on yesterday."
"ดูเรียบร้อยจนขนลุกน่ารำคาญ หาอะไรที่ทำค้างไว้เมื่อวานไม่เจอเลย"

# his "Where is everything?"
his "ของอะไรไปไหนหมดเนี่ย"

show shizu behind_blank at center
with charaenter

# ssh "I did some cleaning."
ssh "ฉันเก็บกวาดนิดหน่อยน่ะ"

# his "That doesn't tell me anything. See, it's like you forgot where you even put the stuff you put away. Oh well, If I can't find it, I guess I'll just go home."
his "ไม่ได้ตอบคำถามเลย เนี่ย ขนาดเธอยังเหมือนไม่รู้เลยว่าเก็บอะไรไว้ที่ไหนบ้าง เอาเถอะ ถ้าไม่รู้ว่าอยู่ไหนฉันก็กลับละ"

show shizu basic_normal2
with charachange

# ssh "It's in the drawer right there."
ssh "อยู่ในลิ้นชักตรงนั้น"

# "Shizune sulks as I pull out the posters I was working on, and then shuffle them around a little, since she stacked them by color. It's not that I'm taunting her; I just have my own system, although I doubt she would believe me if I were to tell her."
"ชิซูเนะทำหน้าไม่พอใจแล้วดึงโปสเตอร์ที่ฉันทำค้างไว้ออกมาแล้วเขี่ย ๆ ไปมาเล็กน้อยเพราะเธอเรียงเอาไว้ตามสี\nก็ไม่ได้จะทำให้เธอรำคาญหรอก แค่ว่าฉันก็มีระบบการจัดการของฉัน แต่ถ้าบอกไปก็คงไม่เชื่ออะนะ"

# his "I like it when things are a little messy. It's more natural. And a time saver. It's all right where I left it, and I don't have to go looking through shelves just to find what I was working on yesterday."
his "ฉันชอบให้อะไร ๆ อยู่แบบไม่เป็นระเบียบบ้าง ทั้งเป็นธรรมชาติกว่าทั้งประหยัดเวลากว่า วางไว้ตรงนั้นก็ดีอยู่แล้ว จะได้\nไม่ต้องไปตามดูชั้นเก็บของว่าเมื่อวานทำอะไรค้างไว้อยู่"

show shizu adjust_frown
with charachange

# ssh "Lazy."
ssh "ขี้เกียจจริง"

# his "That's not true. I'm not lazy, you just always go too far."
his "ไม่จริงสักหน่อย ฉันไม่ได้ขี้เกียจ เธอต่างหากที่เคร่งเกินไป"

# "I quickly glance at her desk. A memo pad neatly placed at one corner, behind it a small desk calendar with each box filled with notes in a neat, but microscopic handwriting. On the right, three boxes of pens, in blue, black, and red."
"ฉันเหลือบมองโต๊ะเธอที่มีกระดาษวางอยู่มุมหนึ่งไว้อย่างเรียบร้อย ถัดจากนั้นมีปฏิทินตั้งโต๊ะที่ในช่องแต่ละวันมีลายมือ\nตัวเท่ามดเขียนไว้อยู่ ส่วนทางขวามีกล่องปากกาอยู่สามกล่องที่มีปากกาสีน้ำเงิน สีดำ และสีแดงแยกกันอยู่คนละกล่อง"

# his "Look, you even put the pens back in their original box at the end of each day, all color-coded and everything. I don't think that can even be called being a neat freak."
his "เนี่ย ขนาดปากกาเธอยังเก็บแยกสีไว้แต่ละกล่องทุกวันเลย เรียกแค่ว่าบ้าความเป็นระเบียบยังน้อยไปมั้ง"

show shizu behind_frown
with charachange

# ssh "What do you do with them, throw them in a mug on your desk?"
ssh "แล้วทีนายล่ะ จับ ๆ รวมใส่แก้วบนโต๊ะนั่นน่ะนะ"

# his "Hey, I think that's being organized enough."
his "เฮ้ย แค่นั้นก็เป็นระเบียบพอแล้วนี่"

show shizu basic_frown
with charachange

# ssh "You're so disorganized, you can't even comb your hair down properly."
ssh "นายเป็นคนไร้ระเบียบมาก ผมยังไม่หวีให้เรียบร้อยเลย"

# his "That hurts…"
his "เจ็บนะ…"

# "It's not like I don't try; it just won't stay flat. I pick up a box of pens and quickly pop it open to see if she also puts them in so that they're all facing the same direction. She understands what I'm thinking, and doesn't look very amused."
"ไม่ใช่ว่าไม่หวีเลยสักหน่อย แค่ว่าผมมันไม่ยอมลู่ ฉันคว้ากล่องปากกามากล่องหนึ่งแล้วเปิดดูว่าเธอเก็บให้ปลายปากกา\nหันไปทางเดียวกันทุกด้ามหรือเปล่า เธอรู้ทันทีว่าฉันคิดอะไรอยู่และทำหน้าไม่พอใจ"

play sound sfx_dropstuff

# "It turns out that the box wasn't closed properly on the bottom, and as soon as I pick it up, they immediately pour out of it like a waterfall."
"และก้นกล่องปากกาปิดไม่สนิท ทันทีที่ฉันยกกล่องขึ้นมาปากกาทุกด้ามก็ร่วงกราวราวน้ำตก"

# his "My fault. I'll get them, don't worry."
his "ขอโทษที เดี๋ยวเก็บให้เอง"

stop music fadeout 4.0
play sound sfx_impact

show shizu adjust_blush_close
with vpunch

# "I bend down to pick up the pens, forgetting that with her attention focused on them, she couldn't have possibly seen me signing to her. Shizune's head bumps into my chest; not very hard, but it unbalances me enough to make me fall over."
"ฉันค้อมตัวลงจะเก็บปากกา แต่ลืมไปว่าชิซูเนะคงมองปากกาจนไม่ได้มองฉันที่ทำภาษามือบอกไปเมื่อครู่ หัวชิซูเนะ\nชนเข้ากับหน้าอกฉัน ไม่ได้ชนแรงมาก แต่ก็แรงพอที่จะทำให้ฉันทรงตัวไม่อยู่จนล้มลง"

show shizu adjust_blush
with charadistant

# "I laugh it off, and expect her to do the same. When she stiffens and backs away from me instead, a feeling of dread begins to creep over me."
"ฉันหัวเราะกลบเกลื่อนด้วยหวังให้เธอหัวเราะตาม แต่เมื่อได้เห็นเธอที่ทำท่าเกร็ง ๆ แล้วถอยกรูดไปฉันก็เริ่มใจคอไม่ดีขึ้นมา"

# "That is a weird reaction. I start to think about why she would have such a strange reaction. It's pretty obvious: she just bumped headfirst into someone with a heart condition."
"แปลก ทำไมถึงได้ทำท่าแปลก ๆ อย่างนั้น ค่อนข้างชัดแหละว่าเพราะหัวเธอโขกเข้ากับคนที่เป็นโรคหัวใจ"

#if seen A26b:
label th_S26a:

# "Shizune would know I have one, having seen the rows and rows of pills lining the edge of my dresser. Or at the very least, she would know I have something severe enough to require that much medication, but not visible at a glance."
"ชิซูเนะคงรู้ว่าฉันเป็น เพราะเห็นขวดยาที่ตั้งเรียงรายอยู่บนหลังตู้ฉันขนาดนั้น หรืออย่างน้อย ๆ ก็คงรู้ว่าฉันเป็น\nอะไรสักอย่างที่รุนแรงจนต้องกินยามากขนาดนั้น ซึ่งอาการที่ว่าไม่ใช่อาการที่เห็นได้ชัด"

#if not seen A26b:
label th_S26b:

# "Shizune would know I have one, maybe thanks to the records her student council duties give her access to. Or at the very least, she would know I have something severe enough to need monitoring."
"ชิซูเนะคงรู้ว่าฉันเป็น อาจจะเพราะเธอเป็นสภานักเรียนเลยสามารถดูประวัติอะไรได้ หรืออย่างน้อย ๆ ก็คงรู้ว่าฉันเป็น\nอะไรสักอย่างที่รุนแรงจนต้องมีคนคอยจับตาดูอยู่เสมอ"

#end conditionals
label th_S26c:

# "So she is treating me like I'm made of glass. For her, it's the natural way to react. I haven't forgotten how she freaked out back when Emi knocked into me. Why would it be any different for her?"
"ถึงได้ทำเหมือนว่าฉันเปราะบางเหมือนแก้วอย่างนั้น จะเป็นอย่างนั้นก็ไม่แปลก ฉันยังจำได้เลยว่าเธอตกใจมากตอนที่\nเอมิชนเข้ากับฉัน"

show shizu basic_normal
with charachange

# "I'm sure she is remembering that, right now. I can see it on her face. She looks angry at herself."
"เธอก็คงกำลังนึกถึงตอนนั้นอยู่เหมือนกัน สีหน้าเธอบ่งบอกว่าเธอโกรธตัวเองมาก"

# "It would be a good opportunity to bring up that time. Even though I don't want to drag that back up, it would be a good idea to. It would clear the air."
"ก็คงเป็นโอกาสอันดีที่จะพูดถึงเรื่องเมื่อตอนนั้นอีก ถึงจะไม่อยากขุดขึ้นมาพูดเลยก็เถอะ แต่เอามาพูดหน่อยก็คงดี\nจะได้คลายบรรยากาศให้เครียดน้อยลงด้วย"

# "Still, I'm afraid, and end up saying nothing. Partly because as I imagine having to draw her attention from the floor, and then having to sign what kind of a cripple I am to her one gesture at a time, the idea begins to seem more and more depressing."
"แต่ฉันกลัว สุดท้ายก็ไม่ได้พูดอะไรเลย อาจจะเพราะฉันนึกภาพไปว่าต้องดึงความสนใจจากเธอมาแล้วก็ทำภาษามือ\nเล่าไปแบบตะกุกตะกักว่าฉันเป็นอะไร ยิ่งคิดก็ยิ่งหดหู่"

hide shizu
with charaexit

# "Taking a seat, I decide to just try and finish up these posters to get my mind off of it. There are some that I don't remember making. From the wall-to-wall text and ultra-neat handwriting, I can tell Shizune must have done these."
"ฉันจึงมานั่งแล้วทำโปสเตอร์ต่อให้เสร็จเพื่อเบนความสนใจของตัวเองไม่ให้คิดเรื่องนั้นอีก มีบางอย่างที่เหมือนฉัน\nไม่ได้ทำไว้โผล่มาด้วย ซึ่งดูจากตัวหนังสือที่เป็นระเบียบเนี้ยบนิ้งยืดยาวแล้วก็คงเป็นชิซูเนะนั่นแหละที่ทำ"

# "That means that the remainder must have been done by Misha. They are a lot more visual, with cute little stylized pictures of us on them. I don't know how I feel about being used as a mascot character, but I'm not really thrilled by it."
"ซึ่งแปลว่าส่วนที่เหลือที่เป็นงานภาพคือมิช่าทำ ซึ่งเป็นภาพวาดพวกเราสามคนน่ารัก ๆ ขนาดเล็ก ไม่รู้จะว่ายังไงดี\nกับการถูกจับไปเป็นตัวละครมาสคอต แต่ที่แน่ ๆ คือฉันรู้สึกว่าไม่น่าสนใจเท่าไหร่"

scene bg school_council_ss
with shorttimeskip

play music music_tranquil fadein 3.0

# "Some time passes; long enough for the sun to start setting. I hear Shizune putting down her pen and cracking her knuckles methodically, one at a time. It's so loud in the silence of the room that I look up, wondering if she is trying to get my attention."
"เวลาล่วงผ่านไป ผ่านไปนานจนพระอาทิตย์เริ่มตกดิน ชิซูเนะวางปากกาลงแล้วหักข้อนิ้วตัวเองเป็นจังหวะสม่ำเสมอ\nในห้องอันเงียบงันแห่งนี้ ซึ่งเสียงดังจนฉันต้องมองเธอ หรือทำเพื่อให้ฉันมองกันนะ"

show shizu behind_blank_ss
with charaenter

# "Although it wasn't what she intended, when she notices me looking at her, Shizune begins to sign without skipping a beat."
"แม้เธอจะไม่ได้ตั้งใจให้ฉันหันไปมอง แต่เมื่อเธอเห็นว่าฉันมองอยู่เธอก็ส่งภาษามือมาทันที"

show shizu basic_normal_ss
with charachange

# ssh "Let's take a break."
ssh "พักกันเถอะ"

# his "I'm surprised you would say that."
his "แทบไม่เคยเห็นเธอบอกอย่างนั้นเลยนะ"

show shizu adjust_happy_ss
with charachange

# ssh "It's okay. I'm almost done, anyway. And I'm hungry. Aren't you?"
ssh "ไม่เป็นไรหรอก ฉันใกล้จะเสร็จแล้วด้วยแหละ หิวแล้วด้วย นายหิวมั้ย"

# his "A little."
his "นิดหน่อย"

show shizu basic_normal2_ss
with charachange

# ssh "I'm really hungry."
ssh "ฉันหิวมาก"

# his "We could order something."
his "สั่งอะไรมากินกันเถอะ"

show shizu behind_smile_ss
with charachange

# ssh "I was thinking of you. I already have something to eat."
ssh "ฉันถามเพราะห่วงนายเฉย ๆ ฉันมีอะไรกินแล้ว"

# his "Where?"
his "ไหน"

show shizu adjust_smug_ss
with charachange

# "She produces a cinnamon bun from under her desk, raising it to head level slowly, like a magician levitating a rock."
"เธอหยิบขนมปังซินนามอนขึ้นมาจากใต้โต๊ะแล้วค่อย ๆ ชูขึ้นมาอยู่ตรงหน้าเธอราวนักมายากลที่เสกหินให้ลอย"

show shizu behind_smile_ss
with charachange

# ssh "But!"
ssh "แต่!"

show shizu basic_sparkle_ss
with charachange

# ssh "There is only one. Not enough for both of us."
ssh "มีแค่ชิ้นเดียว ไม่พอกินสองคน"

# "Ah, how dramatic. I can tell what this means. A feeling of déjà vu briefly washes over me."
"อืม ช่างน่าใจหายเสียจริง ฉันรู้ทันทีว่าหมายความว่าอะไร รู้สึกเหมือนเคยผ่านเรื่องแบบนี้มาแล้วเลยนะ"

# his "We could just split it."
his "แบ่งกันกินก็ได้"

show shizu adjust_frown_ss
with charachange

# ssh "That's. No. Fun. So boring. Let's play shogi for it."
ssh "แล้ว มัน จะ สนุก ตรงไหน น่าเบื่อตาย เล่นโชงิแข่งกันดีกว่า"

# "She already has the board out. That desk must have everything in it."
"เธอเตรียมกระดานแล้วพร้อมสรรพ ใต้โต๊ะนั้นต้องมีทุกสิ่งอย่างอยู่แน่ ๆ"

# his "Not chess?"
his "ไม่เล่นหมากรุกเหรอ"

show shizu behind_smile_ss
with charachange

# ssh "Chess has boring promotions, this is better."
ssh "หมากรุกเลื่อนขั้นหมากได้น่าเบื่อจะตาย โชงิดีกว่า"

# his "I don't know about that. Well, I'm actually pretty decent at shogi, so this is fine."
his "ไม่ยักรู้ เอาเถอะ ฉันก็เล่นโชงิเก่งพอตัวแหละ ได้เลย"

show shizu basic_happy_ss
with charachange

# ssh "Is that so? Okay, we can make it a little more interesting, then. Each move has to be completed in thirty seconds. You can add a rule, too."
ssh "งั้นเหรอ โอเค งั้นเพิ่มความตื่นเต้นสักหน่อยดีกว่า เอาเป็นว่าแต่ละตาเดินให้เดินภายในสามสิบวินาที นายจะเพิ่มกฎอื่น\nอีกก็ได้นะ"

# his "No thanks, anything I could add would only hurt me more than it would help. A thirty-second time limit is already too tight for me."
his "ไม่ละ ขอบใจ ฉันเพิ่มกฎไปเดี๋ยวฉันก็เสียเปรียบเปล่า ๆ แทนที่จะได้เปรียบ แค่สามสิบวินาทีฉันก็แทบคิดไม่ทันแล้ว"

# his "You're making me regret thinking it was all right to brag a little."
his "นี่ฉันคิดผิดหรือคิดถูกเนี่ยที่โม้เธอไปหน่อย ๆ เมื่อกี้"

scene bg school_council_ss
show shizu basic_normal_close_ss at center
with shorttimeskip

# "After Shizune wins the right to go first in a quick coin toss, she immediately starts playing with the aim of promoting all of her pieces as soon as possible. It seems like a very basic playstyle, and I can't help thinking it might be a trap of some sort."
"ผลจากการโยนเหรียญบอกว่าชิซูเนะได้เริ่มก่อน เธอเริ่มเล่นโดยเล็งที่จะเลื่อนขั้นหมากทุกตัวให้ได้เร็วที่สุดเท่าที่\nจะทำได้ เหมือนจะเป็นแนวการเล่นแบบพื้นฐานสุด ๆ ก็จริง แต่ฉันก็อดคิดไม่ได้ว่าอาจจะเป็นกับดักหรืออะไรหรือเปล่า"

# "It's not, though. The draw of this game to Shizune appears to be the fact that she can upgrade her pieces, and steal mine. She's very good at it, but it makes her predictable. I end up doing a little better than I'd expected to."
"แต่ก็ไม่มีกับดัก ดูเหมือนว่าชิซูเนะจะสนใจโชงิเพราะการเลื่อนขั้นหมากของตัวเองและการจับหมากของอีกฝ่าย เธอเล่น\nเก่งมาก แต่ความเก่งนั้นก็ทำให้เดาได้ว่าเธอจะเล่นอะไรต่อ ฉันเองก็เล่นได้ดีกว่าที่คาดไว้ด้วย"

# "The 30-second time limit is pretty painful, though. The game ends in a draw. At this point, I think you're supposed to either go for a rematch or tally the pieces for points."
"แต่เวลาคิดที่มีเพียงสามสิบวินาทีนั้นสาหัสเอาการ สุดท้ายก็เสมอ จริง ๆ ถ้าเสมอก็คงต้องเล่นอีกกระดาน หรือไม่ก็\nต้องนับแต้มจากหมาก"

# "Shizune doesn't want to go again in the interest of time, but winning on points clearly doesn't satisfy her."
"ชิซูเนะไม่อยากเสียเวลาเล่นต่อแล้ว แต่ก็ชัดว่าเธอไม่พอใจกับการชนะด้วยการนับแต้มจากหมาก"

show shizu adjust_frown_close_ss
with charachange

stop music fadeout 4.0

# "She sits there, shifting a silver general from one edge to the other as she contemplates which of those two options she'll go for. It takes so long that I think she has forgotten about the bet."
"เธอนั่งจับเงินย้ายจากขอบกระดานมุมหนึ่งไปยังอีกมุมหนึ่งพลางคิดว่าจะเล่นต่อดีหรือไม่ เธอคิดอยู่นานเสียจน\nฉันคิดว่าน่าจะลืมไปแล้วว่าเดิมพันอะไรกันไว้"

# "Eventually, she stops fiddling with the shogi piece and puts it down."
"ในที่สุดเธอก็เลิกจับหมากเล่นแล้ววางลง"

show shizu behind_blank_close_ss
with charachange

# ssh "Is Misha angry at me?"
ssh "มิช่าโกรธฉันเหรอ"

# "That really came out of nowhere."
"อยู่ ๆ ก็ถามแบบไม่มีปี่มีกลองเลยแฮะ"

play music music_pearly fadein 5.0

# "Shizune's frankness is disorienting, because with her, any kind of candor is a sign of total seriousness. There is no playful smile on her face, instead it's her usual stoic mask of concentration, ready to try and see if I'm about to tell her the truth."
"ความตรงไปตรงมาของชิซูเนะนั้นชวนให้ขนหัวลุก เพราะเมื่อเธอว่าอะไรออกมาตรง ๆ แล้วแปลว่าเธอจริงจังมาก ๆ\nใบหน้าเธอไม่มีรอยยิ้มขี้เล่นใด ๆ แต่กลับเป็นสีหน้าอันจดจ่อเรียบนิ่งอย่างเช่นเคยที่รอดูว่าฉันจะบอกความจริงกับเธอ\nหรือไม่"

# "I'm upset that she thinks that I would tell her anything else, but I also know now that they have probably fought recently, out of my sight, and it makes me feel warm to know that they both care about each other so much."
"ฉันน้อยใจที่เธอคิดว่าฉันอาจไม่ยอมบอกความจริง แต่ฉันก็รู้ว่าช่วงนี้ทั้งสองคนคงทะเลาะกันตอนที่ฉันไม่อยู่ด้วย\nซึ่งทำให้ฉันอบอุ่นใจขึ้นมาว่าทั้งสองคนต่างก็ห่วงกันและกันขนาดนี้"

# his "No. I strongly doubt it."
his "ไม่ ฉันว่าไม่หรอก"

# his "Did you know that she thinks you're angry at her?"
his "เธอรู้มั้ยว่ามิช่าคิดว่าเธอโกรธอยู่"

show shizu behind_sad_close_ss
with charachange

# "Shizune nods slowly and uncomfortably."
"ชิซูเนะพยักหน้าช้า ๆ คล้ายไม่สบายใจ"

show shizu basic_normal2_close_ss
with charachange

# ssh "Yes."
ssh "รู้"

# his "She was more roundabout with the question than you. Kind of surprising, because I thought that you were the one who liked playing games."
his "มิช่าน่ะถามอ้อมกว่าเธออีกนะ ซึ่งฉันก็ตกใจเหมือนกัน เพราะฉันนึกว่าเธอเป็นพวกชอบวางแผนไม่ยอมบอกอะไรง่าย ๆ\nเสียอีก"

show shizu behind_blank_close_ss
with charachange

# ssh "Not all the time."
ssh "ก็ไม่เสมอไปหรอก"

"…"

# his "Are you two having some kind of fight?"
his "ทะเลาะกันหรืออะไร"

show shizu adjust_frown_close_ss
with charachange

# ssh "No."
ssh "เปล่า"

# "She is very quick to deny it, and not happy with the thought. I feel like I've stepped on a landmine."
"เธอปฏิเสธทันควันและดูไม่พอใจที่ฉันถามอย่างนั้น เหมือนฉันไปเหยียบกับระเบิดเข้าให้แล้วสิ"

show shizu behind_sad_close_ss
with charachange

# ssh "Sorry. Actually, yes. Just a tiny one."
ssh "ขอโทษที จริง ๆ ก็ทะเลาะกันนิดหน่อยแหละ"

show shizu behind_blank_close_ss
with charachange

# ssh "I know that she has no interest in the Student Council. She only joined because of me. I'm still grateful. I'm so happy she's my friend. But I don't understand what she is upset about this time."
ssh "ฉันรู้ว่ามิช่าไม่ได้สนใจเรื่องสภานักเรียนหรอก ที่เข้ามาเป็นสภานักเรียนก็เพราะฉัน แค่นั้น แต่ฉันก็ยินดีนะ\nฉันดีใจมากที่มิช่าเป็นเพื่อนกับฉัน แต่ที่ผ่านมาฉันไม่รู้ว่ามิช่างอนเรื่องอะไรอยู่"

# his "Why don't you just ask her?"
his "ทำไมไม่ถามมิช่าไปเลยล่ะ"

show shizu basic_normal2_close_ss
with charachange

# ssh "She won't tell me. I'll figure it out by myself, instead. I was sure that I was very perceptive, even if I can't hear. That was dumb. I know better now."
ssh "มิช่าไม่ยอมบอกฉันหรอก เดี๋ยวฉันจะหาคำตอบเอาเอง ฉันเคยคิดว่าฉันเป็นคนประสาทไว ต่อให้จะหูหนวกก็ตาม\nแต่ฉันคิดตื้นไป ตอนนี้ฉันรู้ซึ้งแล้ว"

show shizu behind_sad_close_ss
with charachange

# ssh "It is probably something that is my fault."
ssh "ฉันคงจะทำอะไรพลาดสักอย่างแหละ"

stop music fadeout 8.0

# "Shizune doesn't elaborate further on what it could have been. I'm sure that it is because she does not fully understand the situation herself."
"ชิซูเนะไม่ขยายความต่อว่าสิ่งที่พลาดนั้นจะเป็นอะไรได้บ้าง คงเพราะเธอเองก็ยังไม่เข้าใจสถานการณ์ตอนนี้ดี\nสักเท่าไหร่นั่นแหละ"

# "It's odd to think that Shizune, usually so sure of everything, could be scared by a little argument with a friend. But the more I think about it, the more it makes sense."
"คิดแล้วก็แปลกดีว่าชิซูเนะที่ปกติจะมั่นใจกับอะไร ๆ ทุกอย่างกลับมากลัวการทะเลาะเล็ก ๆ น้อย ๆ กับเพื่อนอย่างนี้\nแต่ยิ่งคิดก็ยิ่งรู้สึกว่าถูกแล้วที่เธอจะเป็นเช่นนี้"

# "They're a lot closer to each other than normal friends, and Shizune is pretty isolated from other people, in a way. The fact that she is deaf is no small part of it."
"ทั้งสองคนสนิทกันกว่าที่เพื่อนโดยปกติมักจะสนิทกัน ชิซูเนะเองก็นับได้ว่าเป็นคนที่ปลีกแยกออกมาจากกลุ่มคนอื่น ๆ\nซึ่งความที่เธอหูหนวกนั้นก็เป็นปัจจัยสำคัญ"

# "But I get the feeling that she uses Misha as a buffer between other people of her own will, not just because it's been forced onto her. She can communicate well enough with her little pad. She just hates it."
"แต่ฉันรู้สึกว่าชิซูเนะเองจงใจใช้มิช่าเป็นตัวกั้นระหว่างตัวเองกับคนอื่น ไม่ใช่ว่าเธอถูกคนอื่นกันให้ปลีกแยกออกมา\nชิซูเนะเองก็ใช้สมุดจดเล่มเล็กนั้นสื่อสารกับคนอื่นได้ เพียงแต่เธอไม่ชอบ"

# "After such a long time of talking through another person, I guess you start to lose touch. It seems unavoidable. It isn't such a far-out idea to think that she isn't that great with people."
"พอสื่อสารผ่านคนกลางแล้วก็คงจะค่อย ๆ หลงลืมเรื่องปฏิสัมพันธ์กับผู้คนไปอย่างเลี่ยงไม่ได้ การที่เธอรับมือคนไม่เก่ง\nก็ไม่ใช่เรื่องที่จะเป็นไปไม่ได้เลย"

hide shizu
with charaexit

# "I return to working, kind of wanting to eat that cinnamon bun more as time drags on, but when I count the shogi pieces still left out on Shizune's table, I can tell at a glance she would win."
"ฉันทำงานต่อด้วยความหิวขนมปังซินนามอนที่เพิ่มขึ้นเรื่อย ๆ ตามเวลาที่ผ่านไป แต่พอเหลือบมองนับหมากที่ยังอยู่\nบนโต๊ะชิซูเนะแล้วฉันก็รู้ว่าเธอชนะ"

# "I'm also too hungry to concentrate if we were to have a rematch. Motivated by my desire to wrap up and eat something, I put the finishing touches on the last of the posters."
"ถ้าจะแข่งอีกรอบฉันก็คงหิวเกินกว่าที่จะตั้งสมาธิเล่นได้ ฉันรีบจัดการเก็บรายละเอียดโปสเตอร์ให้เสร็จด้วยความที่อยาก\nรีบ ๆ ไปหาอะไรกิน"

# his "Done. I think this many is enough. Too many can be a bad thing."
his "เสร็จแล้ว เท่านี้คงมากพอ เยอะไปเดี๋ยวไม่ดี"

play music music_shizune fadein 3.0

show shizu behind_blank_ss at center
with charaenter

# ssh "Okay."
ssh "โอเค"

# his "That's it? Just “okay?”"
his "แค่นั้นน่ะนะ แค่ “โอเค” เหรอ"

show shizu adjust_frown_ss
with charachange

shi "…?"

show shizu behind_blank_ss
with charachange

# ssh "…I'll probably do some myself, after I'm done picking what voting format to go with."
ssh "…เดี๋ยวฉันคงทำเพิ่มอีกหลังคิดได้ว่าจะให้ลงคะแนนแบบไหนดี"

# his "Arrgghh. Too many posters is bad, too. Haven't you ever heard of oversaturation?"
his "โอยยยย โปสเตอร์น่ะเยอะไปก็ไม่ดีนะ ไม่เคยได้ยินคำว่าเฝือเหรอ"

# his "I really think you're trying too hard."
his "ฉันว่าเธอทุ่มเทหนักไปจริง ๆ นะ"

show shizu basic_normal_ss
with charachange

# "Tenting her fingers, Shizune looks like she could almost admit it."
"ชิซูเนะประกบนิ้วเข้าหากัน สีหน้าเธอดูคล้ายยอมรับ"

show shizu behind_blank_ss
with charachange

# ssh "Maybe."
ssh "มั้งนะ"

# his "It's what Misha thinks, too."
his "มิช่าก็คิดเหมือนกัน"

show shizu basic_normal2_ss
with charachange

# "I watch as her fingers continue uneasily twining around and pulling at each other in a miniature tug-of-war."
"ฉันมองนิ้วเธอที่เกี่ยวกระหวัดดึงกันไปมาราวชักเย่อขนาดย่อม"

# his "I don't mind, but I asked around in a couple classes today and interest is low. It's like you said. So…"
his "จริง ๆ ฉันไม่ได้คิดมากอะไรนะ แต่วันนี้ฉันไปถามคนมาสองสามห้องเรื่องเลือกตั้งแล้วก็ไม่ค่อยมีคนสนใจเท่าไหร่\nเหมือนอย่างที่เธอว่าเลย เพราะงั้น…"

show shizu adjust_frown_ss
with charachange

# ssh "Does that make it wrong?"
ssh "แล้วแปลว่าที่ฉันทำมันผิดเหรอ"

# his "No. But… it does make it kind of pointless."
his "ไม่หรอก แต่… ทำขนาดนั้นแล้วมันก็เหมือนไม่ได้อะไรขึ้นมา"

show shizu basic_angry_ss
with charachange

# ssh "It's not."
ssh "ได้สิ"

# "Yeah, but to who? I doubt even Shizune truly believes that."
"ได้ แต่ใครบ้างที่ว่าได้ ฉันว่าชิซูเนะเองก็คงไม่ได้คิดอย่างนั้นจริง ๆ หรอก"

show shizu behind_frustrated_ss
with charachange

# ssh "I'm not doing all this work just for my own ego."
ssh "ฉันไม่ได้ทุ่มทำไปเพื่ออีโก้ตัวเองสักหน่อย"

# his "That isn't what I mean."
his "ฉันไม่ได้หมายความว่าอย่างนั้น"

# "The first chance to be alone with her in days, and I have already really cocked it up. Still, she doesn't actually look angry."
"ไม่ได้อยู่ด้วยกันสองคนมาหลายวัน แต่พอมาคุยก็ดันทำเสียเรื่องเสียแล้ว แต่เธอก็ไม่ได้ดูโกรธอะไร"

# "It's more like she's frustrated that she can't express herself clearly enough. Since she's an expert in sign language, I wouldn't think that would be the case."
"เหมือนเธอหงุดหงิดมากกว่าว่าสื่อเจตนาตัวเองได้ไม่ชัดพอ แต่เธอเองก็เป็นผู้เชี่ยวชาญด้านภาษามือ คงไม่ใช่อย่างนั้น"

# "I wonder what advantage being able to speak would offer her, and if she has ever thought about it."
"ถ้าเธอพูดได้แล้วจะมีอะไรที่ดีขึ้นมาอีกกันนะ เธอเคยคิดอะไรอย่างนั้นสักครั้งหรือเปล่า"

show shizu basic_frown_ss
with charachange

# ssh "It's another project of mine. Just like the festivals. I'm going to do it, because it's my job. It's just that a student council election isn't as fun as a festival, so no one cares."
ssh "ก็แค่โครงการที่ฉันจะทำโครงการหนึ่ง เหมือนงานเทศกาลนั่นแหละ ฉันจะทำเพราะมันเป็นงานของฉัน เพียงแต่ว่า\nการเลือกตั้งสภานักเรียนมันไม่ได้สนุกเหมือนงานเทศกาล คนเลยไม่สนใจกัน"

# "She briefly touches her fingertips together, as if to say “but, maybe…” There is some truth to it, but Shizune doesn't want to say anything that could be boiled down into something so glib."
"เธอแตะนิ้วเข้าหากันอยู่ครู่หนึ่งราวกับจะบอกว่า “แต่บางที ถ้า…” แต่ชิซูเนะก็ไม่ว่าอะไรต่อ เพราะสิ่งที่จะบอกนั้นจริง ๆ\nก็อาจจะเป็นอะไรที่สุดจะตื้นเขิน"

show shizu behind_frown_ss
with charachange

# ssh "But I don't care. I want to get people riled up, but it isn't about me. I don't want to be involved at all."
ssh "แต่ฉันไม่สนหรอก ฉันอยากให้คนตื่นตัวกัน แต่ไม่ใช่เพื่อฉัน ฉันไม่ได้อยากเข้าไปยุ่งเกี่ยวด้วยเลย"

# his "What do you mean? You go to like, every single festival."
his "หมายความว่ายังไง เธอก็ไปทุกงานเทศกาลเลยนี่"

show shizu adjust_frown_ss
with charachange

# "Shizune waves her hand in mock indignation."
"ชิซูเนะโบกมือไม้ทำทีเป็นโมโห"

show shizu behind_blank_ss
with charachange

# ssh "Well… I have to have fun, too. But you know, it's not the same thing."
ssh "ก็… ฉันก็ต้องสนุกบ้างเหมือนกัน แต่เนี่ย มันไม่เหมือนกันสักหน่อย"

# "Her spirits seem to have improved, if she can manage to crack a joke."
"ถ้าหยอกเล่นอะไรอย่างนี้ก็คงจะอารมณ์ดีขึ้นแล้วละนะ"

show shizu basic_normal2_ss
with charachange

# ssh "I don't want anyone to make a point of me being involved. It's a hassle. I don't want that responsibility."
ssh "ฉันไม่อยากให้ใครต้องมาคอยชูว่าฉันมีส่วนร่วมด้วย วุ่นวายจะตาย ฉันไม่อยากแบกรับอะไรอย่างนั้น"

show shizu adjust_frown_ss
with charachange

# ssh "Things are becoming too complicated now as-is. The more I try to hype up the elections, the more involved I have to be. No one wants to play their hand yet, and it doesn't feel like my time is over, even though it should."
ssh "แค่นี้เรื่องก็ยุ่งยากพออยู่แล้ว ยิ่งฉันจะโหมเรื่องการเลือกตั้งเท่าไหร่ ฉันก็ยิ่งต้องเข้าไปมีส่วนร่วมมากเท่านั้น ตอนนี้\nยังไม่มีใครมีทีท่าว่าจะทำอะไร แล้วเวลาของฉันก็ยังไม่หมด ทั้งที่ควรจะหมดได้แล้วน่ะนะ"

show shizu behind_frustrated_ss
with charachange

# "Crossing her arms and leaning back, she grinds her teeth together in frustration."
"เธอกอดอกเอนตัวกัดฟันด้วยความหงุดหงิด"

show shizu cross_angry_ss
with charachange

# ssh "They're all so lazy; it's impossible to get them to do anything. Anywhere else, the elections would be an exciting event. It's illogical, why does everyone have to be so different? If only there was some way to punish them…"
ssh "ทุกคนขี้เกียจกันมาก ขอให้ทำอะไรนี่ก็ไม่เคยทำกันเลย ถ้าเป็นที่อื่นก็จะมองว่าการเลือกตั้งเนี่ยเป็นอะไรที่น่าตื่นเต้น\nไม่สมเหตุสมผลเลย ทำไมทุกคนถึงต้องต่างกันขนาดนี้ ถ้าลงโทษได้ก็ดีสิ…"

show shizu adjust_angry_ss
with charachange

# ssh "…Like chaining the school to their desks. Voting is mandatory. If you don't vote, you get whipped."
ssh "…แบบล่ามโซ่ไว้กับโต๊ะอะไรงี้ ต้องลงคะแนน ถ้าไม่ลงคะแนนก็จะโบยเสีย"

# "Terrifying. I wonder how hypocritical it would be if I were to stay in bed on election day. With the flu. And a cold. And strep throat. And a sprained ankle."
"น่ากลัว งี้เดี๋ยวก็คงหาว่าแบ่งแยกแน่ถ้าเกิดว่าวันเลือกตั้งฉันข้อเท้าแพลงนอนบนเตียงเป็นทั้งหวัดทั้งไข้หวัดพร้อม\nอาการติดเชื้อในคอ"

# his "You should put yourself on one of these."
his "เธอเอาหน้าตัวเองแปะโปสเตอร์บ้างก็ได้นะ"

# his "Not as punishment. Don't misunderstand."
his "แต่ไม่ใช่จะทำโทษนะ อย่าเข้าใจผิดล่ะ"

# "I hold up one of Misha's posters."
"ฉันชูโปสเตอร์ที่มิช่าทำขึ้นมาใบหนึ่ง"

# his "Like this. It's kind of a neat idea. Misha was on to something. It's a lot cuter than just text. I'd think you would like it. Having cute mascots would drum up some excitement."
his "แบบนี้ไง ความคิดเข้าท่าใช้ได้เลยนะ มิช่าคิดมาจากบ้านแล้ว น่ารักกว่าแบบที่มีแต่ข้อความเยอะ ฉันว่าเธอก็คงชอบ\nเหมือนกัน มีมาสคอตน่ารัก ๆ แล้วคนจะได้สนใจบ้างไง"

show shizu basic_normal_ss
with charachange

# ssh "Maybe if it's just Misha."
ssh "ถ้ามีแค่มิช่าคนก็คงสนใจอยู่"

# his "Why not me? Someone told me that this school has slightly more girls than boys… you have to cater to that demographic, too."
his "แล้วฉันล่ะ มีคนบอกฉันว่าโรงเรียนนี้มีผู้หญิงเยอะกว่าผู้ชายอยู่นิดหน่อย… เราต้องเจาะกลุ่มเป้าหมายนั้นด้วย"

show shizu adjust_blush_ss
with charachange

# "Shizune giggles, audibly this time. I'm surprised, and when she sees my face, so is she. Her face flushes pink, embarrassed to have let out a sound. Which is really confusing, to say the least."
"ชิซูเนะขำคิกคัก แต่คราวนี้มีเสียงแล้ว ฉันตกใจ พอเธอเห็นหน้าฉันเธอก็ตกใจเหมือนกัน หน้าเธอแดงเรื่อด้วย\nความอายที่ส่งเสียงออกมา ซึ่งจะว่างงก็งงอยู่"
#Giggles? :/ -SC

# his "Why don't you put yourself on it?"
his "แล้วเธอจะไม่แปะหน้าตัวเองบ้างเหรอ"

# "She just waves my question away."
"เธอโบกมือเป็นเชิงปัดคำถามฉันทิ้ง"

show shizu basic_angry_ss
with charachange

# ssh "It's troublesome."
ssh "วุ่นวาย"

# his "What do you mean, troublesome? Everyone knows that you're in the Student Council."
his "วุ่นวายนี่คืออะไร ทุกคนก็รู้อยู่แล้วนี่ว่าเธอเป็นสภานักเรียน"

# "My stomach growls, making me realize that I'm hungrier than I'd thought. Shizune uses the moment to deflect my question by changing the subject."
"ท้องฉันส่งเสียงร้องเป็นสัญญาณว่าจริง ๆ แล้วฉันหิวกว่าที่คิด เธอใช้จังหวะนี้ปัดคำถามฉันทิ้งด้วยการเปลี่ยนเรื่อง"

show shizu behind_blank_ss
with charachange

# ssh "Is something wrong?"
ssh "มีอะไรเหรอ"

# his "No. My stomach growled."
his "เปล่า ท้องฉันร้อง"

show shizu basic_normal_ss
with charachange

# ssh "I see."
ssh "อย่างนี้นี่เอง"

# "She looks at the forgotten pastry on her desk then frowns, finding it inadequate for two people."
"เธอมองขนมที่วางแอ้งแม้งอยู่บนโต๊ะแล้วขมวดคิ้วด้วยเห็นว่าปริมาณไม่พอแบ่งสองคน"

show shizu adjust_happy_ss
with charachange

# ssh "Let's go to the Shanghai, if you are that hungry. It might be a little busy this late, but Yuuko is working there today. We will definitely get a table."
ssh "ถ้านายหิวขนาดนั้นก็ไปร้านเซี่ยงไฮ้กันเถอะ เย็นป่านนี้แล้วคนอาจจะเยอะหน่อย แต่วันนี้ยูโกะมาทำงานที่ร้าน ต้องมี\nโต๊ะว่างให้เราแน่นอน"

# "There is something worryingly underhanded in that smile."
"เป็นรอยยิ้มที่เหมือนมีลับลมคมในยังไงชอบกล"

# his "I'll pass. I've already been there twice this week, back to back."
his "ขอผ่านแล้วกัน สัปดาห์นี้ฉันไปที่ร้านมาแล้วสองรอบติดเลย"
#The first time doesn't show in script, but then again I suppose it doesn't have to. -SC

show shizu basic_frown_ss
with charachange

# "Shizune pouts, leaning back against her desk and scrunching up her posture in protest."
"เธอทำแก้มป่องแล้วนั่งยองพิงกับโต๊ะตัวเองเป็นการประท้วง"

# his "What?"
his "อะไร"

show shizu adjust_frown_ss
with charachange

# ssh "I'm disappointed you said no."
ssh "ฉันผิดหวังนะที่นายปฏิเสธ"

# his "Well, I can't agree with you on everything."
his "เออ ฉันก็ใช่ว่าจะเห็นด้วยกับเธอไปได้ทุกอย่างสักหน่อย"

show shizu behind_frown_ss
with charachange

# ssh "You don't give your opinion often enough, anyway. It would be easiest for me if it was like that, but not very interesting, right? There are some decisions you should disagree with me on, then. You have a duty to."
ssh "นายก็ไม่ค่อยมีปากมีเสียงอยู่แล้วละนะ ถ้าเป็นอย่างนั้นก็คงสะดวกฉันดี แต่ก็ไม่น่าสนใจเท่าไหร่ จริงไหม งั้นก็เป็น\nหน้าที่ของนายที่ต้องต่อต้านกับตัวเลือกของฉันบ้าง"

# his "How am I supposed to know which is which?"
his "แล้วฉันจะรู้ได้ยังไงว่าตัวเลือกไหนที่ฉันต้องต่อต้าน"

show shizu basic_normal_ss
with charachange

# ssh "It's easy."
ssh "ง่ายนิดเดียว"

# his "No, it's not. Sometimes it's hard for me to tell whether you're joking or serious."
his "ไม่ ไม่ง่าย บางทีฉันก็ดูไม่ค่อยออกว่าเธอพูดเล่นหรือพูดจริง"

stop music fadeout 9.0

# "Although, since she communicates entirely in sign language, that would seem pretty obvious. I wouldn't say that that's all there is to it, though."
"ถึงน่าจะเห็นได้ชัดว่าเป็นอย่างนั้นเพราะเธอสื่อสารผ่านภาษามืออย่างเดียวก็เถอะ แต่ฉันคิดว่าคงไม่ใช่แค่เพราะเรื่องนั้น\nหรอก"

# "I remember when I had my heart attack, Iwanako wouldn't stop talking, at first. Eventually, I wished that she would just shut up. Or I would have, if I hadn't been happy to have any kind of company at all. Gradually, I stopped being so grateful."
"ฉันจำได้ว่าตอนที่อยู่โรงพยาบาลเพราะหัวใจวายรอบนั้น แรก ๆ อิวานาโกะพูดไม่หยุด จนฉันอยากให้เธอเงียบปาก\nไปเลย หรือถ้าฉันไม่ได้ยินดีที่ยังมีคนมาอยู่ด้วยบ้างแล้วฉันก็คงเงียบใส่ไปเหมือนกัน และความยินดีนั้นก็ค่อย ๆ หายไป"

# "When we talked, I felt like it was nothing more than ritualized exchanges of politeness. Iwanako tried extremely hard to obfuscate how she felt, which was that I was hopeless. In the end, her outer behavior matched her inner feelings."
"ทุกครั้งที่คุย ฉันรู้สึกเหมือนว่าเราคุยกันไปตามมารยาทเพียงเท่านั้น อิวานาโกะพยายามอย่างหนักเพื่อกลบเกลื่อน\nสิ่งที่เธอคิดอยู่ ที่เธอคิดว่าหวังอะไรกับฉันไม่ได้แล้ว จนท้ายที่สุด ท่าทีภายนอกของเธอก็ตรงกับความรู้สึกภายในของเธอ"

# "For that reason, I was able to accept it when one day she stopped showing up. I was no longer surprised by the time it happened. Even though she considered herself a master at hiding her feelings, I was not surprised."
"และด้วยเหตุนั้นเอง ฉันจึงทำใจได้เมื่อถึงวันที่เธอไม่มาอีก ตอนนั้นฉันไม่แปลกใจเลย แม้เธอจะมองว่าตัวเองปกปิด\nความรู้สึกตัวเองเก่ง แต่ฉันก็ไม่แปลกใจเลย"

# "I've heard that games like shogi and chess can tell you a lot about a person. I wish I knew what Shizune thought they said about me."
"ฉันเคยได้ยินมาว่าเกมจำพวกโชงิหรือหมากรุกนั้นบ่งบอกถึงตัวตนของคนหนึ่ง ๆ ได้มาก อยากรู้จังว่าชิซูเนะจะเห็นอะไร\nจากการเล่นของฉัน"

# "It could be that I'm a little more like Iwanako than I'd like to think, if I can only tie with Shizune by retreating. I suggest that we should order out."
"ถ้าไม่มีทางอื่นที่ฉันจะชนะชิซูเนะได้นอกจากการถอนตัวแล้ว ฉันอาจจะเหมือนอิวานาโกะมากกว่าที่ฉันอยากจะคิดก็ได้\nฉันเสนอชิซูเนะให้สั่งอะไรมากินด้วยกัน"

scene black
with dissolve

#####################

label th_S27:

scene bg school_hallway2
with locationchange

# "The next day, I walk up to my usual vending machine at lunch only to find that it's out of my favorite drink. Secreted so far away from most of the classrooms, between a storeroom and the library, it's like no one knew about it."
"วันถัดมาฉันเดินแวะมาที่ตู้ขายของแบบหยอดเหรียญตอนพักเที่ยง ทว่าเครื่องดื่มโปรดฉันหมด ตู้นี้เป็นตู้ที่อยู่ค่อนข้าง\nห่างจากห้องเรียนหลายห้อง อยู่ระหว่างทางจากห้องเก็บของไปห้องสมุด เป็นตู้ที่ดูราวกับว่าไม่มีใครรู้ว่าตั้งอยู่ตรงนี้"

# "I'd expected a vending machine so close to the library to be booming with customers, but then again, the library is empty most of the time, and anyone who goes there is only doing it to look for stuff to pad a paper with."
"ก็นึกว่าตู้ที่อยู่ใกล้ห้องสมุดอย่างนี้จะมีคนใช้เยอะเสียอีก แต่ก็นะ ปกติห้องสมุดก็ไม่มีคนอยู่แล้ว คนที่มาก็จะเป็นคน\nที่จะทำรายงานแล้วมาหาอ้างอิงมากกว่า"

# "No one stays there longer than they absolutely have to. For the past month, it's been working out in my favor, but the trade-off with a vending machine no one knows about is that it's never restocked."
"ไม่มีใครจะแช่อยู่ที่ห้องสมุดนาน ๆ ถ้าไม่จำเป็น สองสามเดือนที่่ผ่านมาฉันจึงใช้ประโยชน์กับตู้นี้ได้เต็มที่ แต่สิ่งที่ต้อง\nแลกมากับตู้ขายของแบบหยอดเหรียญที่ไม่มีใครรู้นี้คือการที่จะไม่มีใครมาเติมของให้ใหม่"

play sound sfx_can

# "Settling for a can of orange soda, I decide on drinking it here instead of waiting until I get to the cafeteria, when the library door opens next to me."
"ฉันจึงเลือกซื้อโซดารสส้มมาแทนและนึกจะดื่มเสียตรงนี้แทนที่จะเดินไปดื่มที่โรงอาหาร แต่ก่อนจะทันได้ทำเช่นนั้น\nประตูห้องสมุดที่อยู่ข้าง ๆ ก็เปิดออก"

show yuuko worried_down at center
with charaenter

# yu "Ah…"
yu "อ๊ะ…"

show yuuko worried_up
with charachange

# yu "I've been looking for you!"
yu "กำลังหาตัวอยู่เลย!"

play music music_happiness fadein 2.0

# "Yuuko seems to be acting a lot more assertive than usual today, although it isn't enough to keep her from going back to mumbling immediately afterwards."
"วันนี้ยูโกะดูจะกล้ากว่าทุกที แต่ก็ยังไม่กล้าพอที่จะพูดดัง ๆ จนได้แต่พึมพำอะไรต่อเหมือนเคย"

show yuuko worried_down
with charachange

# yu "R-return your books, please. I mean… the library's books. The books you checked out are really overdue. Some of them are on waiting lists…"
yu "คะ คืนหนังสือด้วยนะ หมายถึง… หนังสือของห้องสมุดน่ะ หนังสือที่เธอยืมไปเลยกำหนดส่งมานานแล้ว บางเล่มก็มีคน\nจะยืมต่อ…"

# hi "Oops. I forgot. I keep checking out new ones, and forget the return the old ones."
hi "โอ๊ะ ลืมไปเลย ผมมัวแต่ยืมจนลืมคืนเล่มเก่า ๆ น่ะ"

show yuuko neurotic_up
with charachange

# yu "That happens to me all the time at the university library, it's so embarrassing."
yu "กับห้องสมุดของมหาวิทยาลัยฉันก็เป็นอย่างนั้นประจำแหละ น่าอายมากเลย"

# hi "Do they send someone to try and get you to bring them back?"
hi "ที่มหาวิทยาลัยเขาส่งคนมาตามทวงหนังสือมั้ยครับ"

show yuuko worried_up
with charachange

# yu "No… The university library is bigger, they don't notice if I happen to borrow something longer than normal. It's convenient, because their policy on keeping the books too long is… really strict, stricter than here…"
yu "ไม่หรอก… ห้องสมุดของมหาวิทยาลัยน่ะใหญ่กว่าของที่นี่ ถ้าเกิดฉันยืมเล่มไหนไปนานหน่อยก็ไม่มีใครสังเกตอะไร\nซึ่งก็ดีเหมือนกัน เพราะกฎเรื่องการยืมหนังสือนาน ๆ ของที่นู่นน่ะ… เคร่งกว่าที่นี่มาก มาก ๆ …"

# "I like how despite what she said, Yuuko has no problem with borrowing books for longer than she is supposed to anyway. It makes her being so on top of my own lateness a little hypocritical. It takes a thief, I guess."
"น่าสนใจจริง ถึงจะบอกว่าเคร่ง แต่ก็ยังทำอย่างนั้นอยู่ดี ซึ่งพอเธอมาทวงหนังสือที่ฉันยืมจนเลยกำหนดส่งแล้วก็เลย\nทำให้ดูย้อนแย้งอยู่หน่อย ๆ ก็คงอย่างที่เขาว่าผีเห็นผีละมั้ง"

# "Catching on to the meaning of her words around the same time I do, Yuuko clams up and starts backpedaling furiously."
"พอยูโกะนึกถึงความหมายในประโยคนั้นได้หลังจากฉันไปไม่กี่วินาทีเธอก็เงียบไปแล้วรีบแก้ตัวทำโกรธกลบเกลื่อน"

show yuuko panic_up
with charachange

# yu "…Um… ah… That's different… from this situation! It's totally different…"
yu "…เอ่อ… อ่า… มัน… ไม่เหมือนกันนะ! ไม่เหมือนกันเลย…"

# "Yuuko stares at her nails for a second as if she really wants to bite them, but is too self-conscious to do so."
"ยูโกะจ้องเล็บตัวเองคล้ายอยากกัดเล็บใจจะขาด แต่สติที่คอยห้ามไม่ให้ทำนั้นมีมากไป"

show yuuko worried_down
with charachange

# yu "For instance, how long it's been… You checked out some of these books months ago, Hisao. Sorry… It's just that, other people want to read them, too. If you're a slow reader, that's okay, though…"
yu "อย่าง ระยะเวลาที่ยืมไป… ฮิซาโอะ บางเล่มเธอยืมไปสองสามเดือนแล้วนะ ขอโทษที… พอดีว่าคนอื่นก็อยากอ่านบ้างน่ะ\nแต่ถ้าเธอเป็นคนอ่านช้าก็ไม่เป็นไร…"

# hi "No, it's a total screw-up on my part. To be honest, I haven't even read some of them. I shouldn't keep taking out books when I have a backlog."
hi "ไม่หรอกครับ ผมผิดเอง เอาตรง ๆ บางเล่มผมก็ยังไม่ได้อ่านเลย ถ้ามีเล่มที่ค้างอยู่อย่างนั้นผมก็ไม่ควรยืมเล่มอื่นอีก"

# yu "That's not good…"
yu "ไม่ดีเลยนะ…"

# hi "Yeah, it really isn't…"
hi "ครับ ไม่ดี…"

# "Now I'm starting to copy her habit of trailing off quietly. Her awkwardness is very contagious, for some reason."
"แล้วฉันก็ติดนิสัยการพูดแบบเบาเสียงตอนลงท้ายประโยคด้วย ความอึดอัดของเธอเหมือนจะถูกส่งต่อได้ง่ายมาก"

# "That said, I'm surprised. Yuuko seems almost normal today, although every now and then, her waitress-y nervous tics keep popping back up."
"ถึงอย่างนั้นฉันก็แปลกใจอยู่ดี วันนี้ยูโกะดูค่อนข้างปกติ บางครั้งความลนลานอย่างตอนที่เธอเป็นพนักงานเสิร์ฟก็โผล่มา"

# "Come to think of it, she didn't act this way when I first met her. She was a little clumsy and neurotic, but it wasn't anywhere near this severe until Shizune, Misha, and I ran into her at the Shanghai."
"จะว่าไป ตอนที่เจอยูโกะครั้งแรกเธอก็ไม่ได้เป็นอย่างนี้ อาจจะซุ่มซ่ามหรือลนลานไปบ้าง แต่พอฉัน ชิซูเนะ แล้วก็มิช่า\nไปเจอเธอที่ร้านเซี่ยงไฮ้ก็ดูอาการหนักขึ้น"

# "It could be that Yuuko has a complex about having kids from the school seeing her waitressing."
"อาจจะไม่อยากให้นักเรียนที่โรงเรียนมาเห็นตอนที่ทำงานเป็นพนักงานเสิร์ฟอยู่ละมั้ง"

# "I guess it was a little odd for her to pick the closest café to the school to work in, then. In that case, maybe the place having so few customers could be considered a lucky break."
"งั้นก็คงแปลกอยู่หน่อย ๆ ที่เลือกทำงานอยู่คาเฟที่อยู่ใกล้โรงเรียนที่สุด ถ้าอย่างนั้นก็คงนับได้ว่าเป็นโชคดีของเธอ\nที่ได้ร้านที่ไม่ค่อยมีลูกค้า"

# hi "Well, I get it. I'll return them right after school."
hi "แต่ทราบแล้วครับ เดี๋ยวเลิกเรียนแล้วผมจะเอามาคืน"

show yuuko smile_up
with charachange

# yu "As soon as possible, please."
yu "ให้ไวเลยนะ"

show yuuko worried_up
with charachange

# yu "Um… wait, can I ask you for one more thing?"
yu "เอ่อ… เดี๋ยวก่อน วานอะไรอีกอย่างหน่อยสิ"

# hi "Sure, what is it?"
hi "ได้ครับ อะไรเหรอครับ"

show yuuko worried_down
with charachange

# yu "I… I have to go for a while, but I can't just leave the library empty… Sorry, but can I ask you to watch it while I'm gone? Just for a little bit, I'll be right back as soon as possible! You're in the Student Council, so I'm sure if you did it, it would be okay."
yu "ฉัน… มีธุระนิดหน่อยน่ะ แต่จะปล่อยให้ห้องสมุดไม่มีคนดูก็ไม่ได้… ขอโทษทีนะ แต่รบกวนฝากดูห้องสมุดตอนที่ฉัน\nไม่อยู่ให้หน่อยได้มั้ย แป๊บเดียว เดี๋ยวฉันจะรีบกลับมา! เธอเป็นสภานักเรียนใช่มั้ย คงไม่เป็นไรหรอก"

# hi "All right, I'll do it, don't worry ab—"
hi "ได้ครับ เดี๋ยวดูให้ ไม่ต้องห่—"

show yuuko closedhappy_up
with charachange

# yu "Thank you!"
yu "ขอบคุณนะ!"

show yuuko neurotic_up
with vpunch

# "Yuuko quickly slides forward as if she's so grateful she is about to give me a hug, but she stops two centimeters into it, which ultimately just makes the gesture look extremely confusing."
"ยูโกะถลาตัวเข้ามาหาราวกับจะกอดขอบคุณ แต่เมื่อเหลือระยะอีกสองเซนติเมตรเธอก็เบรกจนท่าทางเธอดูเก้กัง\nชวนสับสนหนัก"

# "I'm also surprised that she can control her momentum so well, since she seems kind of clumsy."
"และฉันก็ทึ่งที่เธอควบคุมโมเมนตัมของตัวเองได้ดีมาก ทั้งที่ดูเป็นคนซุ่มซ่ามแท้ ๆ"

hide yuuko
with charaexit

stop music fadeout 6.0

# "Before I can say as much as “You're welcome,” she is already dashing off with the urgency of someone late to an appointment."
"ฉันยังไม่ทันได้พูดแม้แต่คำว่า “ด้วยความยินดีครับ” เธอก็รีบพุ่งตัวออกไปราวกับเลยเวลาที่นัดธุระไว้แล้ว"

# "That could be the case, but I wouldn't feel safe assuming so. It's Yuuko, and she seems like the kind of person to treat everything that way."
"ซึ่งก็เป็นไปได้ แต่อาจจะไม่ใช่ก็ได้ เพราะยูโกะดูจะเป็นคนที่ไม่ว่าจะทำอะไรก็รีบอย่างนั้นตลอด"

scene bg school_library
with locationchange

# "Now that I'm in the library, I feel a bit silly. I don't really know what I'm supposed to do. Should I sit down like I normally would and read? It probably would do, but wouldn't meet Yuuko's high standards."
"พอมาอยู่ในห้องสมุดแล้วก็รู้สึกเด๋อ ๆ เพราะไม่รู้จะทำอะไรดี หรือจะนั่งอ่านหนังสือไปตามปกติดี ก็อาจจะได้แหละ\nแต่คงไม่ได้ตามมาตรฐานอันสูงส่งของยูโกะ"

# "Maybe I should sit at the librarian's desk, and give anyone who comes in a stern and analytical glare. I use Shizune's as a starting point, and practice it a couple times in the mirrored surface of a pen."
"ไม่ก็ไปนั่งที่โต๊ะของบรรณารักษ์แล้วเพ่งพินิจขรึม ๆ มองคนที่เข้าห้องสมุดมา ฉันลองทำตามอย่างชิซูเนะอยู่\nสองสามรอบด้วยการใช้ปากกาที่เป็นผิวสะท้อนดูหน้าตัวเอง"

# "I think it looks pretty good. Frustratingly, no one comes in, so I give up on the idea quickly, and decide to just go looking for Hanako instead."
"น่าจะใช้ได้แล้ว แต่น่าหงุดหงิดที่ไม่มีใครมาเลย ฉันจึงล้มเลิกความคิดนั้นไปอย่างรวดเร็วแล้วออกตามหาฮานาโกะแทน"

# "It's deserted. I think I see someone, but the second I blink, whoever it is is gone. As soon as I return to Yuuko's desk and crack open an interesting-looking book, a familiar person swings in front of me like a falling pendulum."
"ไม่มีใครอยู่เลย เมื่อกี้เหมือนเห็นคน แต่พอกะพริบตาแล้วคนนั้นก็หายไปเลย ทันทีที่ฉันกลับมาที่โต๊ะยูโกะแล้วเปิด\nหนังสือที่น่าอ่านเล่มหนึ่งออกอ่านก็มีใบหน้าอันคุ้นเคยเฉี่ยวผ่านหน้าฉันมาราวลูกตุ้มที่แกว่งไกว"

show kenji invis:
    center
    xpos 0.4
with None

show kenji tsun at center
with dissolvecharamove

play music music_kenji fadein 0.5

# ke "Yo, librarian, I've been looking for you for like, ten minutes. What?! It's you? Man, you must really get around, or the Student Council makes you get around. Those bitches! How could they?"
ke "ไงคุณบรรณารักษ์ ตามหาตัวอยู่ตั้งสิบนาทีแน่ะ ฮะ?! นายเองหรอกเหรอ โห ไปไหนก็เจอนาย หรือเพราะสภานักเรียน\nใช้นายให้ไปหลายที่เนี่ย ยัยพวกนั้น! กล้าดียังไง"

show kenji rage
with charachange

# ke "Slave drivers!"
ke "พวกใช้แรงงานทาส!"

# "He must be exaggerating, because it took me thirty seconds just to do a slow walk around the whole place. The thought is overridden by my surprise to see him."
"ก็เวอร์ไป ฉันเดินทั่วห้องสมุดแบบสบาย ๆ สักสามสิบวินาทีก็ทั่วแล้ว แต่ความคิดนั้นก็ถูกปัดตกไปด้วยความตกใจ\nที่ได้เจอเขา"

# hi "Where did you come from? What are you doing here?"
hi "นายมาจากไหนเนี่ย แล้วมาทำอะไรที่นี่"

show kenji tsun
with charachange

# ke "What, can't a guy go to the library now? I can't even go to the library without some young buck like you giving me the third degree over it. I see some girl coming in here all the time, but no one ever asks her what she's doing here."
ke "อะไร เดี๋ยวนี้เขาห้ามผู้ชายเข้าห้องสมุดหรือไง ฉันเข้าห้องสมุดมาทีไรก็เจอแต่ไอ้พวกเด็กเมื่อวานซืนอย่างนายซัก\nเอาจนหมดไส้หมดพุง ทีผู้หญิงบางคนละฉันเห็นเดินเข้ามาได้สะดวกโยธินไม่มีใครถามเลยว่ามาทำอะไร"

# ke "Is it because she reads and I don't?"
ke "เพราะยัยนั่นอ่านหนังสือแต่ฉันไม่อ่านเหรอ"

# "He must be talking about Hanako. Although I suppose they both avoid people, I want to tell him that reading is what you usually do in a library. So if he's not reading, whatever he's doing is bound to make him look way more suspicious than her."
"หมายถึงฮานาโกะแน่ ๆ ถึงทั้งสองคนจะไม่ชอบอยู่กับคนเหมือนกัน แต่อยากจะบอกเขาว่าส่วนมากคนที่มาห้องสมุดก็\nมาอ่านหนังสือกันนั่นแหละ ถ้าเขาไม่ได้มาอ่านแล้วมาทำอะไรอย่างอื่นคนก็ย่อมรู้สึกสงสัยกับเขามากกว่าฮานาโกะ\nอยู่แล้ว"

# "In the end, though, I'm too surprised by him practically appearing out of thin air."
"แต่ยังไงฉันก็ยังตกใจสุดขีดอยู่ดีที่อยู่ ๆ เขาก็โผล่หัวแบบแวบมาอย่างนี้"

# hi "That— that doesn't tell me what you are doing here."
hi "แล้ว— แล้วสรุปว่านายมาทำอะไรกันแน่"

show kenji neutral
with charachange

# ke "I'm here because of you."
ke "ฉันมาหานาย"

# "His response makes me feel confused. Maybe I fell asleep and this is all just some weird dream, and this Kenji isn't real, but really my subconscious. Is he going to start giving me deep but vaguely-worded advice now?"
"คำตอบของเขาทำฉันสับสน ฉันอาจจะเผลอหลับไปแล้วฝันอะไรแปลก ๆ อยู่ แล้วเคนจิตรงหน้าก็อาจไม่ใช่ตัวจริง\nแต่เป็นร่างที่จิตใต้สำนึกฉันสร้างขึ้น นี่เขากำลังจะให้คำแนะนำอันลึกซึ้งที่ฟังไม่ค่อยรู้เรื่องหรือเปล่า"

show kenji tsun
with charachange

# ke "Because of you, I got chased out of my dorm by feminists. Now, I wander this library, like a soldier without a country, or a ghost. I should haunt you, for ruining things for me."
ke "เพราะนาย ฉันถึงถูกพวกสตรีนิยมขับไล่ออกจากหอฉัน ตอนนี้ฉันต้องเร่ร่อนอยู่ในห้องสมุดนี้เหมือนทหารไร้แผ่นดิน\nเหมือนวิญญาณ ฉันจะตามหลอกหลอนนาย ฐานที่นายทำชีวิตฉันพัง"

# "It's a shame, it would have been an interesting dream, but it seems like this is the real deal."
"น่าเสียดาย ถ้าเป็นฝันก็คงเป็นฝันที่น่าสนใจดี แต่เหมือนว่าเคนจิตรงหน้าจะเป็นตัวจริงนี่แหละ"

# ke "Yeah, you had to start working with women, and that brought them to my door. You remember that? You should, since you were there. After that day, I knew they were on to me. I should have trusted my instincts, but I was young and stupid."
ke "ใช่แล้ว นายเริ่มทำงานให้ยัยพวกนั้นแล้วพามาเยือนถึงหน้าประตูห้องฉัน จำได้มั้ย จำได้สิ นายก็อยู่ด้วยนี่ นับแต่วันนั้น\nฉันก็รับรู้ได้ว่ายัยพวกนั้นตามล่าฉันอยู่ รู้อย่างนี้ฉันเชื่อสัญชาตญาณตัวเองดีกว่า แต่ตอนนั้นฉันยังเด็ก\nและคิดไม่ได้"

# hi "That wasn't even a week ago."
hi "ไอ้ที่ว่าน่ะยังผ่านไปไม่ถึงสัปดาห์เลยนะ"

# ke "Then, my dad called and said one of my letters hadn't been delivered. The post office couldn't have lost it, so it must have been intercepted. Information warfare!"
ke "แล้วพ่อฉันก็โทรมาบอกว่ามีจดหมายของฉันหนึ่งฉบับที่ส่งมาไม่ถึง ไปรษณีย์คงไม่ทำหายแน่นอน เพราะงั้นต้องมีคน\nมาสกัดจดหมายฉบับที่ว่าไปแน่ ๆ นี่มันสงครามข้อมูล!"

show kenji neutral
with charachange

# ke "That's when I knew my secret hideout was compromised. Now I'm on the run, like a fugitive. It's code red. "
ke "ตอนนั้นเองฉันก็รู้ว่าที่ซ่อนลับของฉันถูกเปิดโปงเข้าให้แล้ว ตอนนี้ฉันเลยต้องหนีอย่างผู้หลีกลี้ เพราะเป็นภัยขั้นรุนแรง"

# hi "Dorm rooms aren't secret, they put your name and number on a board right in the doorway."
hi "ห้องพักในหอไม่ใช่ความลับสักหน่อย ตรงประตูก็มีทั้งชื่อทั้งเลขแปะอยู่"

show kenji rage
with charachange

# ke "I know, I saw that. They're diabolical. Why not just put up a big Wild West wanted poster, if they're gonna be like that?! “Wanted: Dead or Alive!” Probably alive, so they can clone me or turn me into a grasshopper."
ke "รู้ เห็นแล้ว ชั่วร้ายมาก ถ้าจะทำขนาดนั้นก็แปะโปสเตอร์ค่าหัวอย่างพวกตะวันตกไปเลยดีมั้ย “จับเป็นหรือจับตายก็ได้!”\nอาจจะจับเป็น จะได้เอาร่างฉันไปโคลนต่อ หรือไม่ก็ทำให้ฉันกลายเป็นตั๊กแตน"

show kenji tsun at Position(ypos=1.15)
with Dissolvemove(0.5)

# "Jumping without warning into the empty chair opposite me, Kenji takes out a cigarette and starts spinning it between his fingers. I've never seen him smoking before, so it must be for effect."
"เคนจิโดดเข้ามานั่งที่เก้าอี้ว่างตรงหน้าฉันแบบไม่บอกไม่กล่าว เขาหยิบบุหรี่ออกมาแล้วใช้นิ้วควงเล่น คงเอามาทำเท่\nเฉย ๆ นั่นแหละ ไม่เคยเห็นเขาสูบเลย"

# ke "I can't even live where I want to any more. This is where it all begins."
ke "ฉันจะอยู่ที่ไหนตามใจอยากไม่ได้อีกต่อไปแล้ว นี่แหละคือจุดเริ่มต้น"

# ke "The tactical brilliance… I mean, once they're in your home, it's over, like termites. If the feminist plan for dominance STARTS there, where the fuck can we go?"
ke "เป็นกลยุทธ์สุดหลักแหลม… ก็เนี่ย ถ้าพวกนั้นได้เข้าบ้านแล้วเมื่อไหร่ก็จบเห่เลย เหมือนปลวกไง ถ้าแผนการกุมอำนาจ\nของพวกสตรีนิยม ‘เริ่ม’ จากตรงนั้นแล้วเราจะหนีไปไหนได้อีก"

show kenji happy
with charachange

# ke "The only question is how they could take a page out of the termite playbook when women are naturally repelled by wood."
ke "คำถามเดียวก็คือแล้วพวกสตรีนิยมมันจะใช้แผนของพวกปลวกได้ยังไง ในเมื่อโดยธรรมชาติแล้วผู้หญิงแพ้ทางไม้น่ะ"

# hi "“You can never go home again.” Is that how the saying goes?"
hi "ใช่วลีที่ว่า “ไม่มีที่ซุกหัวนอนแล้ว” หรือเปล่า"

show kenji neutral
with charachange

# ke "Man, I don't know about never. I was just there. I don't know anywhere else I can shower and get new clothes. And eat, and use the bathroom. And watch TV. I have to keep watching the news, to keep informed."
ke "ไอ้คำว่าไม่มีนี่ก็ไม่แน่ใจเหมือนกันว่ะ ฉันก็อยู่ของฉันเฉย ๆ ฉันไม่มีที่อื่นให้อาบน้ำให้เปลี่ยนเสื้อผ้าให้กินให้เข้าห้องน้ำ\nให้ดูโทรทัศน์แล้ว ฉันต้องตามข่าวสารบ้านเมือง จะได้ไม่ตกข่าว"

# "For someone ousted from his dorm room and living on the run, he sure has no qualms about going back there several times a day for long periods of time."
"ตัวเองบอกว่าโดนขับออกจากห้องพักจนต้องจรลีหนีมาแท้ ๆ แต่ก็ดูจะกลับไปอยู่ที่หอวันละหลาย ๆ รอบ รอบละนาน ๆ\nได้ไม่มีปัญหาอะไร"

# "But by now he's slowly turned away from me and is talking to a revolving display of murder mysteries. There's really no point in interrupting him, I guess."
"แต่ตอนนี้เขาค่อย ๆ หันหน้าหนีจากฉันไปช้า ๆ แล้วพล่ามถึงปริศนาฆาตกรรมที่เวียนวนอยู่ จะขัดเขาก็คงไม่ได้อะไรขึ้นมา\nอะนะ"

play sound sfx_can_clatter

# "I finish off my soda and throw the can into the basket near the door. It hits the rim, but goes in anyway. I silently pump my fist."
"ฉันกระดกโซดาจนหมดกระป๋องแล้วโยนใส่ถังขยะที่อยู่ข้างประตู กระป๋องกระทบเข้ากับขอบถังแต่ยังลงถังอยู่ ฉันกำหมัด\nเฮอยู่เงียบ ๆ"

show kenji neutral at center
with dissolvecharamove

# "Kenji quickly gets up and starts to head towards the door. I wasn't really paying attention; I hope I didn't fist pump at an inappropriate moment."
"เคนจิผุดลุกขึ้นแล้วตรงไปที่ประตู เมื่อกี้ไม่ได้ฟังเลย หวังว่าไม่ได้กำหมัดเฮไปแบบไม่ได้จังหวะนะ"

# hi "Where are you going?"
hi "ไปไหน"

show kenji tsun
with charachange

# ke "You kept sucking down that juice."
ke "นายเอาแต่สูบน้ำผลไม้"

# hi "So? It wasn't even juice, it was soda. And it's gone now. And what do you mean, “sucking it down?” I had two sips."
hi "แล้ว? ไม่ใช่น้ำผลไม้ด้วยซ้ำ โซดาต่างหาก แล้วก็หมดแล้วด้วย แล้ว “สูบ” นี่คือ? ฉันจิบไปสองรอบเอง"

# ke "Yeah, right, you had like fifty million sips."
ke "เออ ๆ นายจิบไปเป็นห้าสิบล้านรอบได้มั้ง"

# hi "That's not even possible."
hi "จิบขนาดนั้นได้ที่ไหนล่ะ"

show kenji neutral
with charachange

# ke "Maybe for you; I go beyond the impossible all the time. Okay, whatever, now I'm thirsty too. I'm going to get my own juice, I'll be right back."
ke "นายอาจจะทำไม่ได้ แต่ฉันก้าวล้ำเกินขีดความเป็นไปได้เสมอแหละ โอเค ช่างเถอะ ตอนนี้ฉันคอแห้งแล้วเหมือนกัน\nเดี๋ยวไปหาน้ำผลไม้บ้าง เดี๋ยวมา"

show kenji invis at Position(xpos=0.4)
with dissolvecharamove

with Pause(0.5)

show kenji neutral at center
with dissolvecharamove

# "He does come almost right back, so quickly that I suspect he knows about my secret vending machine."
"เขาไปแล้วกลับมาแทบจะในทันที เร็วจนฉันสงสัยว่าเขารู้พิกัดตู้ขายของแบบหยอดเหรียญลับของฉันหรือเปล่า"

# ke "I got you one, too. Hope you like grape juice. We're even for the pizza, now."
ke "ฉันซื้อมาเผื่อนายด้วย หวังว่านายจะชอบน้ำองุ่นนะ ทีนี้เราก็เจ๊ากันเรื่องพิซซ่าแล้ว"

# hi "Thanks."
hi "ขอบใจ"

show kenji neutral at Position(ypos=1.15)
with charamove

# "I want to tell him that I lent him nearly ten times the cost of a can of grape juice, but that might make me seem petty. Unopposed, Kenji sits down and starts furiously drinking juice like a man with a vendetta against grapes."
"อยากจะบอกว่าไอ้เงินที่ให้ยืมค่าพิซซ่าไปนี่เยอะกว่าค่าน้ำองุ่นหนึ่งกระป๋องไปเกือบสิบเท่าอีก แต่พูดไปเดี๋ยวหาว่า\nเป็นคนใจแคบ เคนจินั่งลงแล้วกระดกน้ำผลไม้ดื่มอย่างบ้าคลั่งราวโคตรเหง้าตระกูลเขาไปมีเรื่องกับองุ่นมาแต่ชาติปางก่อน"

show kenji happy
with charachange

# ke "You know, it's a lucky break for me that I managed to run into you here, man. I kinda need you to do me a favor."
ke "รู้มั้ย ฉันโชคดีมากที่บังเอิญมาเจอนายที่นี่เนี่ย มีเรื่องจะรบกวนพอดี"

# "Although it's cynical, I wonder if him getting me juice was so he could ask me for this favor. If so, it's very transparent, and poorly timed. I doubt Kenji would think about something so deeply, though. Just asking for things straight out is more his style."
"อาจจะดูเป็นคนหวาดระแวง แต่ที่ซื้อน้ำผลไม้นี่ให้คือจะคิดเป็นค่าคำขอนี่หรือเปล่า ถ้าเป็นงั้นจริงก็เป็นแผนที่มอง\nจากดาวอังคารยังรู้ แถมเลือกจังหวะได้ผิดมาก แต่เคนจิคงไม่ใช่คนที่คิดอะไรให้มากมายขนาดนั้นหรอก เขาเป็นคน\nที่จะขออะไรตรง ๆ เลยมากกว่า"

# ke "I need you to recommend me some books."
ke "ฉันอยากให้นายแนะนำหนังสือให้หน่อย"

# hi "But I thought you didn't read."
hi "แต่นายไม่อ่านหนังสือไม่ใช่เหรอ"

show kenji neutral
with charachange

# ke "How did you know?"
ke "รู้ได้ไง"

# hi "You told me. You said you think people discriminate against you because you don't read."
hi "นายบอกฉัน นายบอกว่าคนเลือกปฏิบัติกับนายเพราะนายไม่อ่านหนังสือ"

show kenji happy
with charachange

# ke "Well, they do. And I do read, I read audio books, because that's the way of the future."
ke "ก็เลือกปฏิบัติแหละ แต่ฉันอ่านนะ อ่านหนังสือเสียง เพราะหนังสือเสียงคือเส้นทางแห่งอนาคต"

show kenji neutral
with charachange

# ke "I have to read a book a month for Literary Studies, though, and I found out that the school doesn't really accept such classics as “Advanced Cryptography.” If I don't read a bunch of books, they're gonna fail me."
ke "แต่ฉันก็ต้องอ่านหนังสือเดือนละเล่มเพราะมีวิชาวรรณกรรมน่ะนะ แล้วที่นี่ก็เหมือนจะไม่ค่อยชื่นชมหนังสือสุดคลาสสิก\nอย่างพวก “วิทยาการรหัสลับขั้นสูง” สักเท่าไหร่ ถ้าฉันไม่อ่านหนังสือให้เยอะ ๆ เดี๋ยวก็สอบไม่ผ่านอีก"

show kenji tsun
with charachange

# ke "I can't fail Literary Studies… that would make me illiterate. That would mean my mom was right. My mom can't be right. I'll just have to study literacy as much as possible."
ke "ฉันจะตกวิชาวรรณกรรมไม่ได้… ไม่งั้นฉันก็จะกลายเป็นคนไม่รู้หนังสือ ซึ่งจะทำให้สิ่งที่แม่ฉันพูดถูก แม่ฉันพูดอะไร\nถูกไม่ได้หรอก ฉันต้องเรียน ‘หนังสือ’ ให้เยอะ ๆ เท่าที่จะเรียนได้"

# hi "What about doing some extra credit?"
hi "งั้นก็ลงหน่วยกิตเพิ่มสิ"

# ke "No thanks. It's bad enough I'm gonna have to carry around these stupid things now."
ke "ไม่ละ ขอบใจ แค่ต้องแบกของโง่ ๆ พวกนี้ก็เต็มทนแล้ว"

# "He picks up a dictionary, flips through it, and places it on the murder mystery rack behind him."
"เขาหยิบพจนานุกรมขึ้นมาแล้วเปิดผ่าน ๆ ก่อนจะวางกับชั้นวางหนังสือหมวดสืบสวนฆาตกรรมที่อยู่ข้างหลังเขา"

# ke "I can't believe this is actually the medium that our ancestors used to look at porn."
ke "ไม่อยากจะเชื่อเลยว่าเจ้านี่คือสื่อที่บรรพบุรุษของเราใช้ดูภาพโป๊"

# "I spit my drink all over the book I'm still holding, damaging it beyond any hope of repair. I quickly check the back and see its suggested retail price is 7900 yen. I think I might have a heart attack."
"ฉันสำลักน้ำจนหกใส่หนังสือที่ฉันถืออยู่จนสภาพยับเยินเกินซ่อมแซม พอรีบพลิกหน้าหลังดูราคาขายแนะนำก็เห็นว่า\nราคาเป็น 7,900 เยน รู้สึกเหมือนใจจะวายเลย"
#Can't find anything for or against the retail price being present and unblanked. :/ -SC

show kenji happy
with charachange

# ke "Wow, destroyed. Shouldn't have done that, though, they take vandalism super seriously here. You're gonna get caned."
ke "โห้ ไม่เหลือ ไม่น่าทำอย่างนั้นเลยนะ ที่นี่เขาเคร่งเรื่องกฎการทำลายทรัพย์สินมากนะ นายโดนตีแน่"

# "He chortles, amused, before taking an extremely long, loud sip from his can of juice."
"เขาหัวเราะยกใหญ่ด้วยความตลกก่อนจะจิบน้ำผลไม้จากกระป๋องอีกอึกยาว ๆ ด้วยเสียงอันดัง"

# hi "It's not vandalism, I didn't do it on purpose. You made me do it, with your words."
hi "มันใช่การทำลายทรัพย์สินที่ไหน ฉันไม่ได้ตั้งใจทำสักหน่อย คำพูดของนายนั่นแหละตัวการ"

# hi "And what do you mean caned? I don't want to be caned."
hi "แล้วตีนี่คืออะไร ฉันไม่อยากโดนตีนะ"

show kenji neutral
with charachange

# ke "Wait, chill out, I didn't mean they actually cane you, they just make you pay for it, and really, really yell at you. It's like they were going to bite my ass off. Still not that big a deal."
ke "เดี๋ยว เย็นก่อน ฉันไม่ได้หมายความว่าตีแบบตรงตัวเว้ย แค่หมายถึงว่าพวกนั้นจะให้นายจ่ายค่าเสียหาย แล้วก็ตะโกน\nเสียงดัง ๆ เหมือนจะงาบหัวนายอะ แต่ก็ไม่ใช่เรื่องใหญ่อะไรขนาดนั้นน่ะนะ"

# hi "I don't care if it's figurative, I don't want to get caned, or get my ass bitten off, or any kind of punishment, you… you dumbass."
hi "จะเปรียบเทียบหรืออะไรก็ช่าง ฉันไม่อยากโดนตีโดนงาบหัวโดนลงโทษอะไรทั้งนั้น ไอ้… ไอ้เบื๊อก"

# hi "What am I going to do? I'm the only person in here. That she knows of, anyway. I can't even throw the book in the trash. It will be found. Then she'll know."
hi "แล้วนี่ฉันจะทำยังไงดี ตรงนี้ก็มีแต่ฉันอยู่ หมายถึงคนที่ยูโกะรู้จักน่ะนะ แล้วจะทิ้งก็ไม่ได้ เดี๋ยวมาเจอก็รู้อยู่ดี"

show kenji tsun
with charachange

# ke "Damn, dude, stop being so weird."
ke "โห่พวก เลิกทำตัวแปลกได้แล้ว"

# hi "How is it weird to not want to be fined?"
hi "ไม่อยากถูกปรับมันแปลกตรงไหนวะ"

# ke "Man, stop flipping out, man."
ke "เฮ้ย เลิกโวยวายเลยเฮ้ย"

# hi "I'm not flipping out, I'm trying to save money."
hi "ไม่ได้โวยวาย ฉันแค่ไม่อยากเสียเงิน"

# ke "So cheap."
ke "ขี้เหนียวว่ะ"

show kenji invis at center
with Dissolvemove(0.5)

hide kenji
with None

stop music fadeout 1.0

# "I'm about to strangle him when I hear Misha's “wahaha” coming up the hallway. Apparently, Kenji hears it too, and uses the opportunity to quickly vanish behind the autobiography section. Like the wind."
"จังหวะที่ฉันเตรียมจะบีบคอเขาก็มีเสียง “วะฮ่าฮ่า” ของมิช่าที่ดังมาตามโถงทางเดินมาขัด เหมือนเคนจิจะได้ยิน\nเสียงนั้นด้วยจึงฉวยโอกาสนี้หายตัวไปอยู่หลังส่วนที่เป็นอัตชีวประวัติด้วยความรวดเร็วดุจสายลม"

show mishashort hips_grin at center
with charaenter

play music music_comedy fadein 0.5

# mi "Hi, Hicchan~!"
mi "ไง ฮิจัง~!"

show bg school_library at bgleft
show mishashort hips_grin at twoleft
with charamove

show yuuko neurotic_down at tworight
with charaenter

# "Misha shouts exuberantly, dragging an embarrassed Yuuko behind her."
"มิช่าตะโกนเสียงแปดหลอดพร้อมลากยูโกะมาด้วย"

show mishashort sign_confused
with charachange

# mi "Hicchan~! Were you talking to yourself?"
mi "ฮิจัง~! นายคุยกับตัวเองอยู่เหรอ"

# "On one hand, saying yes could make me look kind of crazy. On the other hand, if I blow Kenji's cover, he might go off and make me look crazy by association."
"ทางเลือกที่หนึ่ง การตอบว่าใช่จะทำให้ฉันถูกมองว่าบ้า แต่อีกทางเลือกที่สอง การเปิดเผยตัวตนของเคนจิอาจทำให้เขา\nกลายร่างจนฉันถูกเหมารวมว่าบ้าไปด้วย"

# hi "Yes."
hi "อืม"

show mishashort cross_grin
with charachange

# mi "Ahaha~! That's okay~! Don't be embarrassed, Hicchan; I do it too, sometimes, when I'm alone! La~ la~ la~."
mi "อะฮ่าฮ่า~! ไม่เป็นไร~! อย่าอายไปเลยฮิจัง บางทีตอนฉันอยู่คนเดียวก็คุยกับตัวเองเหมือนกัน! ลา~ ล้า~ ลา~"

show yuuko worried_up
with charachange

# yu "Um… nothing happened while I was gone?"
yu "เอ่อ… ตอนฉันไม่อยู่มีเรื่องอะไรมั้ย"

# hi "Absolutely nothing."
hi "ไม่มีเลยครับ"

show yuuko worried_down
with charachange

# yu "It smells like… grapes."
yu "กลิ่นเหมือน… องุ่น"

# hi "I'm wearing grape-scented cologne."
hi "ผมใช้โคโลญกลิ่นองุ่นครับ"

# "I lie brazenly and obviously. From her reaction, I'm going to assume that she knows I'm lying, or thinks I have an abysmal sense for colognes."
"ฉันโกหกไปหน้าด้าน ๆ ไร้ซึ่งความเนียนใด ๆ ดูจากสีหน้าแล้วก็คงรู้ว่าฉันโกหกอยู่ ไม่ก็กำลังคิดว่ารสนิยมกลิ่นโคโลญ\nของฉันนั้นเกินเยียวยา"

# "Since the can of grape juice I drank from is still right there, it's likely to be the former. Fortunately, she doesn't ask any follow-up questions."
"แต่ในเมื่อกระป๋องน้ำองุ่นที่ฉันเพิ่งดื่มไปก็ยังตั้งอยู่ทนโท่ คงน่าจะรู้แหละว่าโกหก แต่โชคดีที่เธอไม่ซักไซ้อะไรต่อ"

# hi "What are you two doing together?"
hi "มาทำอะไรกันเหรอ"

show mishashort sign_smile
with charachange

# mi "We had lunch together~! Strictly business, a business lunch~!"
mi "ไปกินข้าวเที่ยงด้วยกันมาน่ะ~! เป็นมื้อเที่ยงทางธุรกิจ เป็นแค่เรื่องธุรกิจเท่านั้น~!"

# "I try to picture Misha in a suit, having a business lunch with anyone. Somehow, I just can't see it."
"ฉันลองนึกภาพมิช่าใส่ชุดสูทนั่งกินข้าวเที่ยงกับใครสักคน แต่นึกยังไงก็นึกไม่ออก"

# hi "What kind of business?"
hi "ธุรกิจอะไร"

show yuuko panic_up
with charachange

# yu "You don't know?"
yu "เธอไม่รู้เหรอ"

show mishashort hips_grin
with charachange

# mi "Ahaha~! It's nothing~, nothing~. It's normal for one part of the Student Council to not know what the other is doing~!"
mi "อะฮ่าฮ่า~! เปล๊า~ เปล่า~ การที่มีสภานักเรียนบางส่วนไม่ได้รับรู้เรื่องที่คนอื่นทำอยู่ก็ปกติแหละ~!"

# hi "Hey, don't “nothing, nothing” something like that. That isn't normal at all. In fact, it's bad. We're only three people."
hi "นี่ อย่ามา “เปล๊าเปล่า” ใส่กันอย่างนั้นสิ มันปกติตรงไหน จะว่าแย่ยังได้เลย เรามีกันแค่สามคนนะ"

show yuuko neurotic_up
with charachange

# "Yuuko laughs nervously. She must be terrified."
"ยูโกะหัวเราะเจื่อน ๆ สงสัยกลัวแน่ ๆ"

show yuuko worried_down
with charachange

# yu "Misha says that you want to put posters in the library… for the elections. Um… even though they are really far away, I guess it's okay. I didn't know that I could even decide those kinds of things…"
yu "มิช่าบอกว่าอยากเอาโปสเตอร์… เลือกตั้งมาติดในห้องสมุดน่ะ เอ่อ… คือมันก็อยู่ไกลมาก แต่คงไม่เป็นไรละนะ ไม่ยักรู้\nเลยว่าฉันมีสิทธิ์ตัดสินใจอะไรอย่างนี้ได้ด้วย…"

show mishashort cross_laugh
with charachange

# mi "You can~! Isn't that great~? Ahaha~! Aren't you happy? Yay~ yay~!"
mi "มีสิ~! เยี่ยมไปเลยใช่มั้ยล่ะ~ อะฮ่าฮ่า~! ดีใจมั้ย เย้~ เย้~!"

show yuuko panic_up
with vpunch

# "Misha grabs Yuuko's hands and forces her to clap joyously for herself. Yuuko doesn't look very happy about learning that she has more responsibility and power than she'd previously thought."
"มิช่าจับมือยูโกะเข้าตบ ๆ กันด้วยความเริงร่า ยูโกะดูจะไม่ค่อยมีความสุขเท่าไหร่ที่ได้รู้ว่าตัวเองมีภาระและอำนาจเยอะ\nกว่าที่คิดเอาไว้"

show mishashort sign_smile
with charachange

# mi "Hicchan~! Since you're here, you can help me put them up!"
mi "ฮิจัง~! ไหน ๆ นายก็อยู่นี่แล้ว มาช่วยกันติดหน่อย!"

# "Pulling out a giant stack of posters from her bag, she cuts them in half like a deck of cards and passes me the slightly smushed half."
"มิช่าควักโปสเตอร์ปึกใหญ่ออกมาจากกระเป๋าแล้วแบ่งครึ่งเหมือนตัดไพ่ก่อนจะส่งกองครึ่งที่ยับหน่อย ๆ มาให้ฉัน"

show mishashort hips_smile
with charachange

# mi "Shicchan had a really good idea~! We can put some flyers inside books, too~! Then, even if they try to ignore us, they won't be able to! They could even be spring loaded!"
mi "ชิจังคิดอะไรดีมาก ๆ ได้ด้วยละ~! เราเอาใบปลิวสอดไว้ตามหนังสือด้วยก็ได้นะ~! แบบนั้นแล้วต่อให้จะพยายามเมิน\nแค่ไหนก็หนีไม่พ้น! หรือจะทำแบบที่เปิดแล้วเด้งขึ้นมาเลยก็ได้นะ!"

# "Misha tries her best to convey the same tone Shizune used. It sounds close to the real thing, and also a little menacing."
"มิช่าเลียนอารมณ์ของชิซูเนะออกมาสุดความสามารถ ซึ่งฟังดูใกล้เคียงมาก และฟังดูน่าขนลุกหน่อย ๆ ด้วย"

# hi "She was probably kidding."
hi "ชิซูเนะก็พูดเล่นไปงั้นแหละมั้ง"

show mishashort perky_confused
with charachange

# mi "I liked it~."
mi "ฉันชอบนะ~"

show yuuko cry_up
with charachange

# yu "N-no… please… not that…"
yu "มะ ไม่… ขอร้อง… ไม่เอาอย่างนั้น…"

show mishashort cross_smile
with charachange

# mi "A super ultra aggressive marketing blitz~! We're going to start going door to door, too~!"
mi "การตลาดแบบบุกเต็มพิกัด~! แล้วก็จะทำแบบไล่เคาะประตูรายห้องด้วย~!"

# hi "That's a terrible idea."
hi "เป็นความคิดที่ไม่เข้าท่าเลยนะ"

show mishashort cross_frown
with charachange

# "Misha pouts in her best Shizune impression, fingertips tapping together rapidly in annoyance."
"มิช่าทำแก้มป่องให้คล้ายชิซูเนะที่สุดพลางแตะนิ้วเข้าหากันรัว ๆ ด้วยความรำคาญ"

# mi "Hicchan~! You think every idea is terrible…"
mi "ฮิจัง~! ความคิดอะไรนายก็ว่าไม่เข้าท่าหมดแหละ…"

# hi "Yeah, but that idea is too terrible, too terrible to ignore. I can't have that."
hi "เออ แต่ความคิดอันนั้นมันก็ไม่เข้าท่าเกินไป เกินกว่าจะหลับหูหลับตาให้ผ่านได้ ไม่เอาด้วยหรอก"

show mishashort hips_smile
with charachange

# mi "Wahaha~! Hicchan, that sounds like a challenge. Mutiny~, mutiny~!"
mi "วะฮ่าฮ่า~! ฮิจัง นี่นายท้าเหรอ ก่อกบฏ~ ก่อกบฏ~!"

show yuuko cry_down
with charachange

# yu "M-mutiny is bad… Don't fight."
yu "กะ ก่อกบฏไม่ได้นะ… อย่าทะเลาะกันเลย"

show mishashort hips_grin
with charachange

# mi "Wahaha~! It was just a joke~!"
mi "วะฮ่าฮ่า~! ล้อเล่นน่า~!"

show yuuko worried_down
with charachange

# yu "Okay…"
yu "โอเค…"

show yuuko worried_up
with charachange

# yu "Don't fight."
yu "อย่าทะเลาะกันเลย"

show mishashort cross_laugh
with charachange

# mi "Aha~ ha~ ha~."
mi "อะฮ่า~ ฮ่า~ ฮ่า~"

# "The way Yuuko sounds when she's trying to be firm makes me think of a kindergarten teacher. I suppose that makes her very persuasive in her own way."
"พอได้ฟังเสียงยูโกะตอนพยายามทำตัวหนักแน่นแล้วก็นึกถึงพวกครูเด็กอนุบาล ถ้าว่างั้นแล้วจะนับว่ายูโกะมีดีทางด้าน\nคำพูดในแบบของตัวเธอเองก็ได้แหละนะ"

hide mishashort
hide yuuko
with charaexit

stop music fadeout 5.0

# "Putting up the posters is surprisingly hard, simply because the library is already plastered with bulletin boards and flyers lining every couple meters, some of them in places so unlikely that I'd never noticed them before."
"การติดโปสเตอร์นั้นยากเหลือเชื่อ เพราะในห้องสมุดแทบทุก ๆ สองเมตรจะมีป้ายประกาศกับโปสเตอร์ติดอยู่เต็มไปหมด\nบางที่ที่มีติดไว้ก็เหมือนว่าฉันจะไม่เคยเห็นมาก่อนเลยด้วยซ้ำ"

play sound sfx_warningbell

# "Deciding which of them to peel off in favor of our own adds a lot of time to an otherwise simple job. By the time the bell rings to signal the end of lunch, Misha and I still have a sizable amount of posters left."
"ยิ่งต้องมาเลือกว่าจะลอกใบไหนออกก็ยิ่งเสียเวลาเข้าไปอีก ทั้งที่แค่ติดโปสเตอร์ก็งานง่าย ๆ และเมื่อระฆังหมดพักเที่ยงดัง\nแล้วเราก็ยังเหลือโปสเตอร์ที่ยังไม่ได้ติดอยู่อีกพอสมควร"

# "As we leave, I decide to stick one right by the door. It must be one that Misha did; it has a little drawing of Shizune on the bottom."
"ตอนที่เดินออกมาฉันติดใบหนึ่งไว้ที่ตรงประตู ต้องเป็นใบที่มิช่าทำแน่ ๆ เพราะมีรูปวาดชิซูเนะรูปเล็ก ๆ อยู่ข้างล่างด้วย"

scene black
with dissolve

label th_S28:

scene bg school_scienceroom
with locationchange

# "A couple days later, Shizune heads off to go eat lunch by herself and doesn't come back. She must really be swamped with student council work, although I know that she probably made most of that work for herself."
"สองวันให้หลังชิซูเนะออกไปกินข้าวเที่ยงแล้วไม่กลับมาที่ห้อง สงสัยงานสภานักเรียนคงมีเยอะจนท่วมหัว ถึงงานที่ว่า\nส่วนใหญ่น่าจะเพราะหาเรื่องไปทำเองก็เถอะ"

scene bg school_hallway3
with shorttimeskip

# "When I get to the student council room, I find the door unlocked. Before opening it, I hold back for a second, to see if I'll hear Misha's laughing through it. Nothing."
"พอมาถึงหน้าห้องสภานักเรียนก็พบว่าประตูไม่ได้ล็อกอยู่ ก่อนเปิดฉันรอฟังก่อนว่าจะมีเสียงหัวเราะมิช่าดังมาหรือเปล่า\nเงียบ"

# "I'd almost take that as a sign that no one's in, but Shizune wouldn't leave the door unlocked in that case."
"ตอนแรกก็คิดว่าคงไม่มีใครอยู่ แต่แล้วก็คิดได้ว่าถ้าไม่มีคนอยู่จริงชิซูเนะคงต้องล็อกห้องไว้"

play sound sfx_dooropen

scene bg school_council
with locationchange

# "She's at her desk, sleeping in her chair with her arms folded over her chest. What a stiff pose; if it weren't for her eyes being closed, there would be no way to tell that she was asleep. In fact, I can't even be sure that she is asleep now."
"ชิซูเนะนั่งกอดอกหลับอยู่ที่โต๊ะ แค่เห็นท่าก็ปวดแทน ถ้าไม่เห็นว่าตาปิดอยู่คงไม่รู้ว่าหลับอยู่ อันที่จริง ฉันก็ไม่แน่ใจ\nด้วยซ้ำว่าหลับอยู่หรือเปล่า"

# "Normally, I'd tap a desk to wake anyone else up, but it wouldn't work with her. I immediately start thinking of tricks I could play on her if she's sleeping. It's disappointing that my train of thought goes in those kinds of directions."
"ปกติถ้าเป็นคนอื่นฉันคงเคาะโต๊ะให้ตื่น แต่กับชิซูเนะคงไม่ได้ ฉันคิดทันทีว่าจะแกล้งชิซูเนะตอนหลับได้ยังไงบ้าง\nผิดหวังจริง ๆ ที่สมองฉันคิดอะไรอย่างนั้นไปก่อนแล้ว"

show shizu basic_normal at center
with charaenter

# ssh "Hello. Good afternoon."
ssh "สวัสดี ทิวาสวัสดิ์"
#You sure this can be done, A22? -SC

play music music_shizune fadein 3.0

# "She signs one greeting with each hand. It's really confusing."
"ชิซูเนะทำภาษามือข้างละประโยค เห็นแล้วก็งง"

# his "Hey, what were you doing? Secretly slacking off?"
his "นี่ ทำอะไรเนี่ย แอบอู้เหรอ"

show shizu behind_smile
with charachange

# "Shizune smiles, but lowers her head to conceal it, and tries her best to look annoyed instead."
"ชิซูเนะยิ้มแต่ก็ก้มหัวไม่ให้เห็นพลางปั้นหน้าให้ดูรำคาญที่สุด"

show shizu adjust_frown
with charachange

# ssh "Don't just stand there, it makes me nervous if I'm sitting down and you're not."
ssh "อย่ายืนอยู่อย่างนั้นสิ พอฉันนั่งแต่นายยืนแล้วมันอึดอัดนะ"

# "I take a seat in the nearest chair while Shizune pauses to adjust her glasses on the bridge of her nose like she's fine-tuning an instrument."
"ฉันนั่งเก้าอี้ตัวที่อยู่ใกล้ ๆ ชิซูเนะดันแว่นที่สันจมูกเธอราวกับกำลังจูนเสียงเครื่องดนตรีอยู่"

show shizu adjust_angry
with charachange

# ssh "Why are you so far away?"
ssh "ทำไมอยู่ไกลจัง"

# his "Does that make you nervous, too?"
his "อยู่ไกลแล้วอึดอัดเหมือนกันเหรอ"

# "Pursing her lips, Shizune doesn't look too amused at my taunting her."
"ชิซูเนะเม้มปากดูไม่พอใจเท่าไหร่ที่ฉันล้อเธอ"

# his "I had some free time, so I thought I would drop by and see if you were still busy."
his "ฉันว่าง ๆ พอดีเลยกะว่าจะมาแวะดูว่าเธอยุ่งอยู่หรือเปล่า"

show shizu behind_blank
with charachange

# ssh "Do you want to help me?"
ssh "อยากช่วยเหรอ"

# his "Yeah."
his "อืม"

show shizu adjust_smug
with charachange

# ssh "Too bad."
ssh "แย่หน่อยนะ"

show shizu behind_smile
with charachange

# ssh "I'm grateful, but it's not necessary. I just finished the last of it, and now everything that needed to be done is done."
ssh "ฉันยินดีนะที่นายจะช่วย แต่ไม่ต้องแล้ว ฉันเพิ่งปิดงานที่ต้องทำทั้งหมดไปแล้วพอดี"

# his "So formal. Misha was just as businesslike yesterday. Are you both getting serious for official student council business?"
his "จริงจังจังเลยนะ เมื่อวานมิช่าก็เหมือนกัน นี่พวกเธอจริงจังกับงานของสภานักเรียนที่เป็นทางการกันเหรอ"

show shizu basic_normal2
with charachange

# ssh "I'm always serious. Like the student council candidates should be."
ssh "ฉันจริงจังเสมอ จริงจังอย่างที่ผู้สมัครเป็นสภานักเรียนควรจะเป็น"

# "That was fast. From zero to immediately criticizing people who aren't even her colleagues yet before I've had the chance to stretch my legs."
"จะรีบไปไหน ฉันยังไม่ทันได้ทันจะยืดแข้งยืดขา มาถึงก็ว่าให้คนที่ยังไม่ได้มาร่วมงานกันเลยด้วยซ้ำแล้ว"

show shizu behind_frown
with charachange

# ssh "At least the presidents. They need initiative, then maybe they can motivate everyone else, or at least strongarm them along. But even though there's a bunch of them, they're all so wishy-washy."
ssh "อย่างน้อยประธานต้องจริงจังเพราะจะเป็นหัวขบวนที่กระตุ้นให้ทุกคนตามได้ หรืออย่างน้อยก็ต้องลากได้ แต่พวกไม่เอาไหน\nมันก็มีเยอะ"

show shizu basic_angry
with charachange

# ssh "There's no one running for vice president. So, they all want the big prize, but none of them have the right drive for it. And then the treasurers are always so flaky, I've decided to use my power to just eliminate the position."
ssh "ไม่มีใครสมัครเป็นรองประธานเลย สรุปก็คือทุกคนอยากได้รางวัลใหญ่ แต่ไม่มีใครที่มีความต้องการจริง ๆ ส่วนเหรัญญิก\nก็มักเป็นคนที่เชื่อถือไม่ได้ ฉันเลยใช้อำนาจฉันตัดตำแหน่งนั้นทิ้งไป"

# his "Wait a sec, please. Can you even do that? I don't think it works that way."
his "เดี๋ยวก่อน เดี๋ยว ทำอย่างนั้นได้ด้วยเหรอ ฉันว่าไม่น่าใช่อย่างนั้นนะ"

show shizu adjust_frown
with charachange

# ssh "It is how it is."
ssh "มันก็เป็นอย่างนั้นแหละ"

# "With that, Shizune stares grimly into the distance, rubbing the frame of her glasses. That doesn't answer the question, future dictator."
"แล้วชิซูเนะก็ทำหน้าเคร่งทอดสายตามองไปไกล ๆ พลางลูบกรอบแว่น ผมยังไม่ได้คำตอบเลยนะครับว่าที่ท่านผู้นำ\nเผด็จการ"

show shizu behind_frown
with charachange

# ssh "I'm disappointed. They should want me out of here faster, because they want the job, or at least disagree with me having the job. If I can't mobilize a bunch of student council wannabes for either reason, all my work will have been for nothing."
ssh "ผิดหวังจริง ๆ พวกนั้นต้องอยากให้ฉันออกจากสภานักเรียนเร็ว ๆ สิ ตัวเองจะได้เข้ารับตำแหน่ง หรืออย่างน้อยก็ต้อง\nไม่เห็นด้วยที่ฉันดำรงตำแหน่งอยู่ ถ้าฉันทำให้พวกที่อยากเป็นสภานักเรียนเคลื่อนไหวเพราะสาเหตุสองอย่างนั้นไม่ได้\nทุกอย่างที่ฉันทุ่มทำไปก็เสียเปล่า"

show shizu adjust_angry
with charachange

# ssh "If they are going to be so slow about it, I'll just hold on to my office as long as possible!"
ssh "ถ้าจะยืดยาดกันขนาดนี้ฉันก็จะยึดสภานักเรียนไว้ให้นานที่สุดเลย!"

play sound sfx_snap

# "Shizune punctuates the sentence with a snap of her fingers, creating a sound as sharp as a gunshot. I wonder if she knows how loud she can do that."
"ชิซูเนะปิดประโยคด้วยการดีดนิ้ว เสียงดีดนิ้วนั้นดังราวเสียงปืน จะรู้ตัวหรือเปล่านะว่าตัวเองดีดได้ดังขนาดไหนเนี่ย"

# "It's definitely an attention-grabber, so I could only see it as invaluable to a mute. She might have practiced it because of that."
"แต่ใครได้ยินเสียงนี้ก็ต้องหันแน่นอน ซึ่งก็ดูเป็นประโยชน์มากสำหรับคนเป็นใบ้ อาจจะฝึกมาเพื่อการนี้เลย"

# his "“All of it,” huh? That's too harsh."
his "“ทุกอย่าง” เลยเหรอ เกินไปหน่อยมั้ง"

show shizu behind_blank
with charachange

# ssh "I always thought this is the real test. Leaving a lasting impression is important. It's why I don't build sand castles, they crumble when you leave."
ssh "ฉันคิดว่านี่คือการทดสอบที่แท้จริงมาโดยตลอด การสร้างความประทับใจครั้งสุดท้ายไว้น่ะสำคัญน่ะ ฉันถึงได้ไม่สร้าง\nปราสาททราย เพราะพอจากไปแล้วมันก็จะพัง"

# his "Maybe, but if I see an especially neat one, I still think it's impressive. I'll say it's impressive."
his "ก็คงจริง แต่ถ้าฉันเห็นปราสาททรายหลังสวย ๆ สักหลังฉันก็ประทับใจนะ ฉันก็จะบอกว่าน่าประทับใจอยู่ดี"

# his "I kind of admire you. So, to me, it wasn't for nothing."
his "ฉันนับถือเธอนะ เพราะงั้นฉันถึงได้มองว่าที่เธอทำไปมันไม่ได้สูญเปล่าหรอก"

show shizu adjust_happy
with charachange

# "She tugs at her glasses as if she wants to take them off, smiling wryly."
"เธอจับแว่นคล้ายจะถอดออกแล้วยิ้มเจื่อน ๆ"

show shizu basic_normal
with charachange

# ssh "Sorry."
ssh "ขอโทษนะ"

show shizu behind_blank
with charachange

# ssh "I was careless, and something selfish slipped out."
ssh "ฉันเผลอหลุดอะไรเห็นแก่ตัวไป"

show shizu basic_normal
with charachange

# ssh "I've always wanted to stand at the top. It didn't matter what it was, as long as I was the best at it, and understood it completely, and made it my own."
ssh "ฉันอยากอยู่ตรงจุดสูงสุดมาโดยตลอด ไม่ว่าจะเป็นเรื่องอะไรก็ตาม ตราบเท่าที่ฉันทำสิ่งนั้นได้ดีที่สุด เข้าใจอย่าง\nทะลุปรุโปร่ง แล้วทำให้เป็นส่วนหนึ่งของตัวฉัน"

show shizu adjust_happy
with charachange

# ssh "Like when you hear a song and dream of being a musician, or see a plane and wish you could be a pilot. Have you ever had a dream like that?"
ssh "เหมือนเวลาได้ฟังเพลงแล้วฝันอยากเป็นนักดนตรี หรือได้เห็นเครื่องบินแล้วฝันอยากเป็นนักบิน นายเคยฝันอะไร\nอย่างนั้นหรือเปล่า"

# his "Yeah."
his "อืม"

# "The first time I played soccer, I'd wondered if maybe I could ever get good enough to wow people. That was just a fantasy, though. As soon as I saw the gap between me and people with real talent, I put those dreams behind me."
"ตอนที่ฉันได้เล่นฟุตบอลเป็นครั้งแรก ฉันก็คิดว่าอาจจะเล่นจนเก่งพอที่จะทำให้คนทึ่งได้ แต่ก็เป็นได้แค่ฝันลม ๆ แล้ง ๆ\nน่ะนะ พอฉันเห็นความต่างชั้นระหว่างฉันกับคนที่มีพรสวรรค์จริง ๆ ฉันก็พับฝันนั้นเก็บทิ้งทันที"

# "Well, with my heart the way it is, I can't play soccer any more, anyway."
"แต่เอาเถอะ หัวใจฉันเป็นอย่างนี้ก็คงเล่นฟุตบอลอีกไม่ได้แล้วละนะ"

# his "Do you still have dreams like that?"
his "เธอยังฝันอะไรอย่างนั้นอยู่หรือเปล่า"

show shizu basic_normal2
with charachange

# ssh "No, they're unrealistic. I realized it very quickly. There is always someone better."
ssh "ไม่หรอก ไม่นานฉันก็รู้ว่าฝันเหล่านั้นมันไกลเกินไป เพราะจะมีคนที่เก่งกว่าอยู่เสมอ"

# "A nostalgic expression crosses her face. She looks oddly mature right now, as if the days of competing vigorously against others for supremacy are long behind her."
"เธอทำสีหน้าหวนถวิล ตอนนี้เธอดูเป็นผู้ใหญ่ชอบกล ราวกับว่าวันวานที่ต้องแข่งขันอย่างดุเดือดกับคนอื่นเหล่านั้น\nผ่านมาแล้วแสนนาน"

# "Of course, I know that nothing could be further from the truth. Just last week, she wanted to see which one of us could blow the biggest bubble with a piece of gum. It could be that she was even worse when she was younger; a terrifying thought."
"แต่ฉันก็รู้ว่าสิ่งที่ว่านั้นคงไม่ได้ไกลจากความเป็นจริงนักหรอก สัปดาห์ที่แล้วฉันยังแข่งเป่าหมากฝรั่งให้ได้ลูกใหญ่ ๆ\nกับเธออยู่เลย ตอนเด็กอาจจะยังเป่าไม่เก่งเท่าตอนนี้ด้วยซ้ำ แค่คิดก็ขนลุก"

show shizu behind_smile
with charachange

# ssh "I liked that. That there was always someone better. When someone greater than me would appear, I'd get so excited. I'd want to challenge them."
ssh "ฉันชอบนะ การที่มีคนเก่งกว่าอยู่เสมอ ฉันจะตื่นเต้นมากที่ได้เห็นว่ามีคนที่เก่งกว่าฉันแล้วจะอยากแข่งกับคนที่ว่า\nขึ้นมาเลย"

show shizu adjust_frown
with charachange

# ssh "Even though in the end, they would usually turn out to be better, and I would be left in awe. There are some people who are on a different level, completely. After a while, I got jealous. I wanted something like that for myself."
ssh "ถึงสุดท้ายแล้วผลจะได้ว่าคนนั้นเก่งกว่าจนฉันต้องมองอ้าปากค้างก็เถอะ แต่บางคนก็อยู่คนละชั้นแบบฉันเทียบไม่ติด\nผ่านไปสักพักฉันก็อิจฉาอยากได้อย่างนั้นบ้าง"

# his "Is that what the Student Council is, the thing just for you?"
his "แล้วสภานักเรียนคือสิ่งที่เกิดมาเพื่อเธอโดยเฉพาะงั้นเหรอ"

show shizu basic_normal
with charachange

# ssh "No, no. Even though it feels like that, sometimes, that wasn't why I decided to do it. That is another story entirely."
ssh "ไม่ ไม่เลย ถึงบางครั้งจะรู้สึกเหมือนเป็นอย่างนั้นก็เถอะ แต่ก็ไม่ใช่สาเหตุที่ฉันมาเป็นสภานักเรียน สาเหตุที่ว่าน่ะ\nคนละเรื่องกันเลย"

show shizu adjust_happy
with charachange

# ssh "But… I like being Student Council president. Even if the work is hard and I'm always biting off more than I can chew, that is what keeps it exciting. People at the top shouldn't be able to be comfortable all the time, anyway."
ssh "แต่… ฉันชอบการเป็นประธานสภานักเรียนนะ ถึงบางครั้งงานจะหนัก ภาระเยอะเกินจะแบก แต่นี่แหละคือสิ่งที่ทำให้\nสภานักเรียนน่าตื่นเต้น ยังไงเสียคนที่อยู่ชั้นบน ๆ ก็ไม่ควรเอาแต่นั่งกินนอนกินอยู่แล้ว"

# his "You sound like a farmer."
his "ฟังดูอย่างกับชาวสวนชาวไร่แน่ะ"

# "Although they wouldn't suit her, Shizune would look cute in overalls and a straw hat."
"อาจจะฟังดูไม่เหมาะ แต่ถ้าชิซูเนะใส่ชุดเอี๊ยมกับหมวกฟางแล้วคงน่ารักดี"

# his "So, if that wasn't the reason, why did you run for the job?"
his "ถ้าไม่ใช่สาเหตุที่ว่า แล้วเพราะอะไรถึงมาสมัครตำแหน่งนี้"

show shizu behind_frown
with charachange

# ssh "I didn't, but afterwards, I decided to stick with it anyway. I wanted to be the Student Council president because the old Student Council was stupid."
ssh "ฉันไม่ได้สมัคร แต่หลังจากนั้นฉันก็อยู่ตำแหน่งนี้ไปนั่นแหละ ฉันอยากเป็นประธานสภานักเรียนเพราะรุ่นเก่าน่ะ\nไม่รู้เรื่องอะไรเลย"

show shizu basic_normal
with charachange

# ssh "And I want to stir people up, so that they will be able to say, “That was interesting. Today was interesting.” That kind of thing. Memorable experiences."
ssh "แล้วฉันก็อยากให้คนตื่นตัวกัน จะได้พูดกันว่า “น่าสนใจดีนะ วันนี้สนุกดี” อะไรประมาณนั้น เป็นประสบการณ์ที่ควรค่า\nแก่การทรงจำ"

show shizu behind_smile
with charachange

# ssh "I'm happy, because I think we succeeded. You, and Misha, and me."
ssh "ฉันมีความสุขนะ เพราะฉันว่าเราทำสำเร็จแล้ว ทั้งนาย ทั้งมิช่า แล้วก็ฉัน"

show shizu basic_normal2
with charachange

# ssh "I have a selfish desire too, though. At first it was something I thought would only be a nice bonus, but I've gotten greedy."
ssh "แต่ฉันเองก็มีความอยากที่ดูเห็นแก่ตัวเหมือนกัน ตอนแรกฉันก็มองแค่ว่าคงเป็นของแถมอะไรเล็ก ๆ น้อย ๆ แต่นานไป\nฉันก็เริ่มโลภ"

show shizu behind_blank
with charachange

# ssh "That is why it would make me happy if the elections go smoothly. It would be the only way that I could see that my wish was granted."
ssh "เพราะอย่างนี้แหละฉันถึงอยากได้ให้การเลือกตั้งเป็นไปอย่างราบรื่น เพราะเป็นสิ่งเดียวที่จะทำให้ความปรารถนาของฉัน\nได้รับการเติมเต็ม"

# his "What is it, then?"
his "แล้วความปรารถนาที่ว่าคืออะไร"

show shizu adjust_blush
with charachange

# ssh "It's a secret."
ssh "ความลับ"

# "Sensing that I might not be ready to let such a weak dodge slide by so easily, Shizune quickly waves down any attempt at a follow-up, embarrassment coloring her face. It's something she wants to keep to herself only because it's too silly to do otherwise."
"ชิซูเนะรู้ตัวว่าฉันคงไม่ยอมเลิกตื๊อกับคำตอบเลี่ยงตื้น ๆ อย่างนั้นง่าย ๆ จึงโบกมือปัด ๆ เป็นเชิงไม่อยากให้คุยต่ออีก\nเธอทำหน้าอาย ๆ อาจจะเป็นเรื่องที่ดูงี่เง่าเลยอยากเก็บไว้เป็นความลับละมั้ง"

# "I start to feel a pang of hunger, and check my watch. It's earlier than it looks. Too early for dinner."
"ความหิวเริ่มเข้าจู่โจม พอก้มมองนาฬิกาก็เห็นว่ายังอีกนานกว่าจะถึงเวลามื้อเย็น แต่หิวแล้วแฮะ"

# his "Do you have any kind of food in your desk?"
his "ในโต๊ะเธอมีอะไรให้กินบ้างมั้ย"

show shizu cross_wut
with charachange

# "For a second, it looks like the question confuses her, but she recovers quickly."
"แวบหนึ่งเธอยังดูงง ๆ กับคำถามอยู่ แต่ก็ตั้งหลักได้ทันควัน"

show shizu behind_frustrated
with charachange

# ssh "Desks are for supplies."
ssh "โต๊ะมีไว้เก็บอุปกรณ์"

# his "Food is supplies."
his "อาหารก็เป็นอุปกรณ์"

show shizu basic_normal
with charachange

# ssh "You should have eaten lunch."
ssh "ทำไมไม่กินข้าวเที่ยงมาล่ะ"

# his "I didn't think it would be a problem if I didn't. If I was working, I wouldn't have to think about it. I'd be too busy to be hungry."
his "ก็นึกว่าไม่กินมาแล้วจะอยู่ได้ แบบว่าถ้าทำงานแล้วจะได้ไม่ต้องคิดเรื่องข้าวเพราะยุ่งจนลืมหิวไปเลย"

show shizu adjust_happy
with charachange

# "She puts her hand up to her mouth in a poor attempt to conceal a laugh, and tries to hide it further by pretending to use it to push her glasses further up the bridge of her nose."
"ชิซูเนะเอามือป้องปากกลั้นขำแทบไม่อยู่ แล้วยังทำทีเป็นดันแว่นที่สันจมูกไม่ให้เห็นว่าขำอีก"

# his "I guess you're not, since you already ate."
his "เธอคงไม่หิวสินะ กินข้าวมาแล้วนี่"

# "I'm not good enough to sign the appropriate words, so I settle for pointing at the stack of Chinese food containers leaning precariously out of the top of her trash can."
"ฉันไม่รู้ว่าจะทำภาษามือเป็นคำว่าอะไรดีจึงใช้วิธีการชี้ ๆ กล่องอาหารจีนที่กอง ๆ อยู่บนถังขยะ"

show shizu basic_normal
with charachange

# ssh "Those are from yesterday."
ssh "อันนั้นของเมื่อวาน"

# his "Then we're both hungry. Let's get something to eat."
his "งั้นก็แปลว่าเธอหิวเหมือนกัน หาอะไรกินกันเถอะ"

# his "Not from the cafeteria. There wasn't anything good at lunch, so I really doubt there will be anything good left over. Order something?"
his "ไม่เอากับข้าวที่โรงอาหารนะ ตอนเที่ยงไม่มีอะไรอร่อย ๆ ให้กินเลย แล้วยิ่งป่านนี้แล้วคงไม่เหลืออะไรอร่อย ๆ แน่ ๆ\nสั่งอะไรมากินมั้ย"

show shizu behind_frown
with charachange

# ssh "Ordering out two days in a row is unnatural. Only in case of emergencies. That is my personal policy."
ssh "สั่งข้าวกินสองวันติดน่ะผิดวิสัยนะ จะทำได้ก็ต่อเมื่อเป็นกรณีฉุกเฉินเท่านั้น ฉันตั้งกฎไว้อย่างนั้น"

# "This is why she should think of putting some snacks in her desk, it would be an easier way of dealing with these kinds of “emergencies.” I want to tell her, but signing out how hungry I am like five times has made me too tired to be a smartass."
"นี่ไงเธอถึงต้องเอาขนมอะไรใส่ใต้โต๊ะเผื่อไว้บ้าง จะได้มีวิธีง่าย ๆ ที่ใช้รับมือ “กรณีฉุกเฉิน” พวกนี้ได้ อยากจะบอก\nอยู่หรอก แต่ฉันทำภาษามือว่าหิวไปสักห้ารอบได้แล้วมั้ง ขี้เกียจจะมาทำตัวเป็นลูกอีช่างติแล้ว"

# "The temptation is really great, though."
"แต่ก็อยากจะบอกจริง ๆ เลยนะ"

# mi "Hi~! Hi, hi!"
mi "งาย~! ไง ไง!"

# "Misha's distinctive up-and-down voice sounds muffled through the door. She bursts in a second later."
"เสียงสูงต่ำอันเป็นเอกลักษณ์ของมิช่าดังผ่านประตูเข้ามา ผ่านไปหนึ่งวินาทีเธอก็เปิดประตูเข้ามา"

show shizu behind_blank at tworight
show bg school_council at bgright
with dissolvecharamove

show mishashort perky_confused at twoleft
with charaenter

mi "…"

show mishashort perky_smile
with charachange

# mi "Hicchan~! You're here, too~!"
mi "ฮิจัง~! นายก็อยู่ด้วย~!"

# hi "“Too?” How did you know there was already someone in here?"
hi "“ด้วย”? รู้ได้ไงว่ามีคนอยู่ในนี้อยู่ก่อนแล้ว"

show mishashort sign_smile
with charachange

# mi "If it opens, someone is inside~."
mi "ถ้าไม่ได้ล็อกก็แปลว่ามีคนอยู่~"

show mishashort cross_laugh
with charachange

# mi "Wahaha~!"
mi "วะฮ่าฮ่า~!"

show mishashort hips_grin
with charachange

# mi "Am I interrupting~?"
mi "ฉันมาขัดหรือเปล่า~"

show shizu basic_normal
with charachange

# "Shizune shakes her head."
"ชิซูเนะสั่นหัว"

show mishashort hips_smile
with charachange

# mi "Great~! That's really great~! But~! I was sure I would be. Is this a break?"
mi "เยี่ยม~! เยี่ยมจริง ๆ ~! แต่~! ฉันนึกว่าจะมาขัดนะ พักกันอยู่เหรอ"

# hi "I thought so, too, but it turns out everything student council related is over, for now. Is that why you're here?"
hi "ฉันก็คิดอย่างนั้นแหละ แต่เหมือนตอนนี้งานสภานักเรียนจะไม่มีแล้ว ที่มานี่คือจะช่วยเหรอ"

show mishashort perky_smile
with charachange

# mi "Wahaha~! Yeah~! That's right, Hicchan!"
mi "วะฮ่าฮ่า~! ช่าย~! ใช่แล้วฮิจัง!"

# ssh "Sorry to disappoint you. We were just discussing whether or not to order out for dinner."
ssh "ขอโทษที่ทำให้ผิดหวังนะ แต่เมื่อกี้คุยกันอยู่ว่าจะสั่งอะไรมากินดีมั้ย"

show mishashort hips_grin
with charachange

# mi "That sounds fun~."
mi "ฟังดูสนุกดีนี่~"

# hi "Shizune isn't being very fun about it, though. She says that she can't order food two days in a row. Are you hungry, too? Because if you are, we could outvote her."
hi "แต่ชิซูเนะไม่สนุกด้วยนี่สิ เห็นบอกว่าสั่งข้าวกินสองวันติดไม่ได้ เธอหิวด้วยมั้ยล่ะ ถ้าเธอหิวเราก็จะได้เป็นเสียงข้างมาก"

show mishashort hips_smile
with charachange

# mi "Hm~ hm~, that sounds fun, Hicchan! And, I am a little hungry…"
mi "อืม~ อืม~ ฟังดูสนุกดีนะฮิจัง! ฉันก็หิวหน่อย ๆ แล้วด้วย…"

# hi "I thought you would say it sounds like mutiny."
hi "นึกว่าจะหาว่าเป็นการก่อกบฏอีก"

show shizu adjust_frown
with charachange

# "Shizune pinches the frame of her glasses, clearly thinking that it does seem like mutiny, but being outvoted by a clean 2-to-1 margin, there is nothing she can do. Misha already has her phone out. It's awfully garish."
"ชิซูเนะจับกรอบแว่น เห็นได้ชัดว่าเธอมองว่าสิ่งนี้คือการก่อกบฏจริง ๆ แต่ก็ทำอะไรไม่ได้อยู่ดีเพราะเราชนะเสียง\nสองต่อหนึ่งอย่างใสสะอาด มิช่าควักโทรศัพท์ที่แค่เห็นก็ปวดลูกกะตาแล้วออกมา"

show mishashort sign_smile
with charachange

# mi "Shicchan, you promised we would have a student council thing, just for us, right~? Right, right~! This can be it~!"
mi "ชิจัง เธอสัญญาแล้วนี่ว่าเราจะจัดงานเลี้ยงสภานักเรียนที่มีแค่เราสามคนกันน่ะ ใช่มั้ย~ ใช่ ใช่~! นับรอบนี้เป็น\nงานเลี้ยงที่ว่าก็ได้นะ~!"

show shizu behind_frown
with charachange

# "Shizune only shakes her head. The last party she will be able to attend as Yamaku's Student Council president is too special to her to put that label on our spur-of-the-moment early dinner."
"ชิซูเนะได้แต่สั่นหัว งานเลี้ยงส่งครั้งสุดท้ายที่เธอจะได้เข้าร่วมในฐานะประธานสภานักเรียนของยามากุนั้นพิเศษเกินกว่า\nที่จะมานับกับมื้อเย็นล่วงหน้าที่นึกอยากกินขึ้นมาตามอารมณ์นี้"

stop music fadeout 3.0

# "Even though I'm sure the real thing will be just like this: a meal like any other, with the three of us."
"แต่ฉันว่าของจริงก็อาจจะเป็นอย่างนี้ที่มีพวกเราสามคนมานั่งกินข้าวด้วยกันเหมือนอย่างทุกครั้งนั่นแหละ"

scene bg school_dormext_full_ss
with shorttimeskip

# "After we finish eating and clean up, I say goodbye to them and head to my dorm. Although I don't feel particularly tired, I think I'll just go straight to sleep tonight."
"พอกินและเก็บกวาดกันเรียบร้อยแล้วฉันก็บอกลาทั้งสองคนเดินกลับมาที่หอตัวเอง ถ้าถึงห้องแล้วหลับเลยดีกว่า ถึงจะ\nไม่ได้เพลียอะไรขนาดนั้นก็เถอะ"

# "If I were back home, my mom would nag me not to go to bed right after eating, but what she doesn't know won't hurt her."
"ถ้าเป็นที่บ้านแม่ฉันคงว่าเรื่องที่กินเสร็จแล้วนอนเลย แต่ถ้าแม่ไม่รู้ก็คงไม่เสียหายอะไร"

scene bg school_dormhisao_ss
with locationskip

# "I take a look at the clock as soon as I get in, and realize that it's a lot later than I'd thought."
"พอเข้าห้องมาได้ฉันก็มองนาฬิกาทันที ค่ำกว่าที่คิดไปเยอะเลยแฮะ"

# "It also feels a bit silly checking the clock when I have a phone and a wristwatch. I take off my watch and hold it in one hand, while holding my phone in the other. It makes me feel powerful, and stupid."
"แล้วก็รู้สึกเด๋ออยู่หน่อย ๆ ที่มาดูนาฬิกาในห้องทั้งที่โทรศัพท์กับนาฬิกาข้อมือก็มือ ฉันถอดนาฬิกาข้อมือออกมาถือไว้\nที่มือข้างหนึ่ง อีกข้างถือโทรศัพท์ ทำแล้วก็รู้สึกทรงพลัง และโง่"

play sound sfx_doorknock

# "I try unsuccessfully to go to sleep, and am glad when someone interrupts me by knocking on my door after only a few minutes. I figure that it couldn't be anyone but Kenji, which is why I'm surprised when it ends up being Misha."
"ฉันข่มตานอนแต่ก็นอนไม่หลับ ยังดีที่ผ่านไปได้ไม่กี่วินาทีก็มีคนมาเคาะประตูขัด คงเป็นใครไปไม่ได้นอกจากเคนจิ\nแต่พอเปิดประตูออกก็ต้องตกใจเมื่อพบว่าเป็นมิช่า"

play sound sfx_dooropen

scene bg school_dormhallway
show mishashort hips_smile at center
with locationchange

# mi "Hi, Hicchan~!"
mi "ไง ฮิจัง~!"

show mishashort perky_sad
with charachange

# mi "You don't look happy to see me~…"
mi "ไม่ดีใจเหรอที่ได้เจอฉัน~…"

# hi "No, I'm just kind of surprised. Did Shizune remember something that she wants me to do after all?"
hi "ไม่ใช่อย่างนั้น ฉันแค่ตกใจน่ะ นี่ชิซูเนะนึกออกแล้วเหรอว่าจะให้ฉันช่วยอะไร"

# hi "It's late, but… whatever. I guess it's good that I didn't change."
hi "คือก็ค่ำแล้วแหละ แต่ก็… ช่างเหอะ ยังดีนะที่ไม่ได้เปลี่ยนชุด"

show mishashort sign_smile
with charachange

# mi "Nope~. I just thought I'd follow you back, Hicchan~!"
mi "เปล่า~ ฉันแค่อยากตามนายกลับมาด้วยน่ะฮิจัง~!"

# hi "For fun?"
hi "แค่อยาก?"

# "No, of course not. It's because she wants to talk. It must be about something important, and something she doesn't want Shizune to know about."
"ไม่ใช่แค่อยากตามหรอก คงมีเรื่องจะคุยนั่นแหละ ต้องเป็นอะไรที่สำคัญจนไม่อยากให้ชิซูเนะรู้ด้วยแน่ ๆ"

# hi "Do you want to come in?"
hi "จะเข้ามาก่อนมั้ย"

show mishashort hips_grin
with charachange

# mi "Yeah~, thanks, Hicchan!"
mi "อื้ม~ ขอบใจนะฮิจัง!"

scene bg school_dormhisao_ss
show mishashort invis at center
with locationchange

show mishashort perky_smile_ss at Position(ypos=1.13)
with dissolvecharamove

play sound sfx_doorclose

# "She walks in and immediately takes a seat in the chair. The natural thing to do, but I'd expected her to sit on the bed."
"เธอเดินเข้ามาแล้วนั่งลงกับเก้าอี้ทันที ก็เป็นเรื่องปกติที่ต้องทำ แต่นึกว่าคนอย่างมิช่าจะนั่งบนเตียงเสียอีก"

show mishashort cross_frown_ss
with charachange

# mi "Hicchan…"
mi "ฮิจัง…"

# "Misha frowns harshly, arms folded over her chest. It's like she's trying to play a grim interrogator. All that's missing is the mustache and the dangling, flickering lightbulb on a string."
"มิช่ากอดอกขมวดคิ้วจนแทบจะผูกกัน เหมือนกำลังจะเล่นบทผู้สอบสวนผู้น่ากลัวอยู่เลย ขาดก็แต่หนวดกับหลอดไฟ\nสักดวงที่ติด ๆ ดับ ๆ ห้อยอยู่กับเพดาน"

# mi "Did you make Shicchan sad?"
mi "นายทำให้ชิจังเศร้าเหรอ"

play music music_drama fadein 6.0

# hi "What do you mean?"
hi "หมายความว่าไง"

show mishashort hips_frown_ss
with charachange

# mi "When I went to the office today, Shicchan couldn't hear me coming. That's why~, when I opened the door, I saw a really confusing expression on her face. Shicchan looked happy and sad, and~ I wanted to know why."
mi "ตอนฉันไปที่ห้องทำงานวันนี้ชิจังไม่ได้ยินที่ฉันมาหา เพราะงั้น~ ตอนฉันเปิดประตูก็เลยเห็นชิจังทำสีหน้าที่ดูแล้วสับสน\nมาก ดูทั้งมีความสุขทั้งเศร้า แล้ว~ ฉันอยากรู้ว่าเพราะอะไร"

# hi "Well, it wasn't because of me. I didn't even see it."
hi "ไม่ใช่ฉันแล้วแหละ ฉันไม่เห็นด้วยซ้ำ"

# hi "I think she's depressed that she won't be Student Council president any more in a few months."
hi "ฉันว่าชิซูเนะหดหู่ที่อีกไม่กี่เดือนก็จะไม่ได้เป็นสภานักเรียนแล้ว"

show mishashort perky_confused_ss
with charachange

# mi "Hm~… When I asked Shicchan about it, she said that it was okay~!"
mi "อืม~… ตอนฉันถาม ชิจังก็บอกว่าไม่เป็นไร~!"

# hi "That's meaningless. Shizune would say that, but it's ridiculous to think that she would let it go that easily."
hi "ถามไปก็ไม่ได้อะไรหรอก ชิซูเนะก็ต้องพูดอย่างนั้นอยู่แล้ว แต่คนอย่างชิซูเนะยังไงก็ต้องเก็บเอาเรื่องนี้ไปคิดมาก\nแน่ ๆ ละ"

# hi "I mean, there are times when she'll want to fight me over the last apple, or chocolate milk, or whatever. And that is stuff that doesn't even matter."
hi "ก็เนี่ย บางทีฉันกับชิซูเนะยังตีกันเรื่องแอปเปิลลูกสุดท้ายเอย นมช็อกโกแลตเลย เยอะแยะ แล้วนี่ขนาดว่าเป็นแค่เรื่องที่\nไม่ได้สลักสำคัญเลยนะ"

show mishashort hips_frown_ss
with charachange

# mi "Chocolate milk is important."
mi "นมช็อกโกแลตน่ะสำคัญนะ"

# hi "Okay, it is. Don't get mad. But not as much as Student Council is to her. She wouldn't just wave it off so easily."
hi "โอเค สำคัญ อย่าโกรธเลยนะ แต่สำหรับชิซูเนะ เรื่องนั้นก็ไม่สำคัญเท่าเรื่องสภานักเรียน คงไม่ยอมปล่อยไป\nง่าย ๆ หรอก"

show mishashort hips_grin_ss
with charachange

# mi "Wahaha~. You're right~."
mi "วะฮ่าฮ่า~ ถูกของนาย~"

# "I thought that this was supposed to be an interrogation, but it appears Misha has already forgotten about it."
"นึกว่าจะมาสอบสวนอะไร แต่เหมือนมิช่าจะลืมไปแล้ว"

show mishashort sign_smile_ss
with charachange

# mi "But~! I don't want Shicchan to lie to me to make me feel better."
mi "แต่~! ฉันไม่อยากให้ชิจังโกหกให้ฉันสบายใจ"

show mishashort hips_grin_ss
with charachange

# mi "Hahaha~! Most people don't know how serious Shicchan is and think she's just putting on a show. I'm happy that you understand her, Hicchan."
mi "ฮ่าฮ่าฮ่า~! หลายคนยังไม่รู้ว่าชิจังเป็นคนจริงจังแค่ไหน คิดกันไปว่าทำท่าเหมือนจริงจังแค่นั้น ฉันดีใจนะที่นายเข้าใจ\nชิจัง"

# hi "It's obvious. Especially with how she talked about it today."
hi "ก็เห็น ๆ กันอยู่นี่ ยิ่งวันนี้ตอนที่ชิซูเนะพูดถึงเรื่องสภานักเรียนอีก"

# "Misha leans in closer with interest, resting her head on her palms."
"มิช่าโน้มตัวเข้ามาใกล้ด้วยความอยากรู้พลางใช้มือเท้าหัว"

show mishashort cross_smile_ss
with charachange

# mi "Really~? What did she say?"
mi "จริงเหรอ~ ชิจังว่าไง"

# "They are close enough that I don't think much of how she is prying."
"ใกล้พอที่ฉันจะลืมคำถามที่ละลาบละล้วงอย่างนั้น"

# hi "Why she joined the Student Council. Sort of. She started, but then decided that some stuff should just stay classified. And signed, “It's a secret.” So, I guess that's what she told me: it's a secret."
hi "เรื่องที่ชิซูเนะมาเข้าสภานักเรียนน่ะ อะไรประมาณนั้น เปิดประเด็นมาแล้วก็เหมือนจะนึกได้ว่าบางเรื่องควรจะเก็บเป็น\nความลับเอาไว้ แล้วก็ส่งภาษามือว่า “ความลับ” นั่นแหละมั้งที่ชิซูเนะบอกกับฉัน"

show mishashort sign_smile_ss
with charachange

# mi "Well~, if someone tells you that they have a secret, you can sort of call that a secret by itself, Hicchan~!"
mi "เอ~ ถ้ามีคนบอกว่ามีความลับ งั้นที่บอกอย่างนั้นก็พอจะนับได้ว่าเป็นความลับด้วยนะฮิจัง~!"

# hi "Just like how, according to you, luck is a skill?"
hi "เหมือนที่เธอบอกว่าดวงคือทักษะน่ะเหรอ"

show mishashort hips_grin_ss
with charachange

# mi "It can be!"
mi "ก็เป็นงั้นได้นะ!"

show mishashort cross_laugh_ss
with charachange

# mi "Wahaha~!"
mi "วะฮ่าฮ่า~!"

# hi "Be careful, not so loud."
hi "เบา ๆ หน่อย อย่าเสียงดังไป"

show mishashort perky_confused_ss
with charachange

# mi "Why, Hicchan?"
mi "ทำไมเหรอฮิจัง"

# hi "You're going to wake up half the people in the building, and on top of that, dorms aren't co-ed."
hi "เดี๋ยวคนครึ่งตึกเขาก็ตื่นกันหมด แล้วยิ่งไปกว่านั้น หอที่นี่เขาแยกชายหญิงนะ"

show mishashort hips_frown_ss
with charachange

# mi "Hicchan, are you thinking something dirty?"
mi "ฮิจัง นายคิดอะไรลามกอยู่เหรอ"

# hi "Stop being weird."
hi "เลิกทำตัวแปลก ๆ ได้แล้ว"

show mishashort hips_grin_ss
with charachange

# mi "Ahahaha~."
mi "อะฮ่าฮ่าฮ่า~"

show mishashort hips_smile_ss
with charachange

# mi "If you are, it's okay, I think."
mi "ถ้าฮิจังว่างั้นก็โอเค มั้งนะ"

# "Hearing that makes me realize how easy it's been for me to talk to Misha all this time, that I would be able to go this long without feeling the need to be on guard. This is the first time I have."
"พอได้ฟังแล้วฉันก็เพิ่งรู้ตัวว่าฉันคุยกับมิช่าได้อย่างสบาย ๆ มาตั้งนานโดยที่ไม่ต้องตั้งท่ากันอะไรเลย ครั้งแรกเลยที่ได้\nคุยอย่างนี้"

show mishashort perky_sad_ss
with charachange

# mi "I feel sad, Hicchan."
mi "ฉันเศร้าจังเลยฮิจัง"

# mi "It's funny, the happier Shicchan gets, the more depressed I feel. Even though I should be happy for Shicchan. I still am… But~, I can't talk about my problems with her."
mi "ตลกดี ยิ่งชิจังมีความสุข ฉันยิ่งหดหู่ ทั้งที่ฉันควรจะมีความสุขไปกับชิจังแท้ ๆ ก็มีแหละ… แต่~ ฉันเล่าปัญหา\nของตัวเองให้ชิจังฟังไม่ได้"

# hi "Why not?"
hi "ทำไมไม่ได้"

show mishashort sign_sad_ss
with charachange

# mi "Just like Shicchan can't talk about her problems to me. It's the same thing, Hicchan. If we have that kind of problem, then I'm not sure any more what I should do. I wonder… if I'm a bad friend."
mi "ก็สาเหตุเดียวกับที่ชิจังเล่าปัญหาตัวเองให้ฉันไม่ได้นั่นแหละ เหมือนกันเลยฮิจัง ถ้าเรามีปัญหาอย่างนั้นฉันก็ไม่รู้แล้วว่า\nจะทำยังไงดี นี่ฉันเป็นเพื่อนที่แย่… หรือเปล่า"

#hi "What are you doing?"

#"Although it's just a formality. I'd be stupid to not know what she is getting at, it's just that it seems so unlikely that I'm hoping there will be some way I won't have to deal with it."
#Moved these -SC

show mishashort perky_sad_close_ss at center
with characlose

stop music fadeout 2.0

# "Misha gets up and quickly drops herself on the bed, until we're sitting only a few inches apart. Just a couple seconds later, she pushes her head forward, and gives me a light kiss. It misses my lips, more due to bad aim on her part than because of me."
"มิช่าผุดลุกขึ้นแล้วมาหย่อนตัวลงนั่งกับเตียง ระยะห่างระหว่างเราเหลือเพียงไม่กี่นิ้ว ผ่านไปอีกไม่กี่วินาทีเธอก็ยื่นหัว\nเข้ามาจูบฉันเบา ๆ ซึ่งไม่โดนริมฝีปากฉัน แต่เป็นเพราะเธอเล็งไม่โดนเอง ไม่ใช่ว่าฉันหลบหรืออะไร"

# hi "What are you doing?"
hi "ทำอะไรของเธอ"

# "Although it's just a formality. I'd be stupid to not know what she is getting at, it's just that it seems so unlikely that I'm hoping there will be some way I won't have to deal with it."
"แต่ก็ถามไปตามเรื่องแค่นั้นแหละ ถ้าไม่รู้ว่ามิช่าคิดอะไรอยู่ก็คงโง่บรม เพียงแต่ว่าดูเป็นไปไม่ได้จนฉันหวังว่าจะพอมีทาง\nให้ฉันเลี่ยงไม่ต้องรับมือกับเรื่องนี้"
#To here -SC

show mishashort hips_grin_close_ss
with charachange

# "Now she decides to be shy, and giggles, embarrassed."
"แล้วเธอก็มาทำท่าเขินอายพร้อมเสียงหัวเราะคิกคัก"

mi "…"

show mishashort perky_smile_close_ss
with charachange

# mi "Do you like me, Hicchan?"
mi "นายชอบฉันมั้ยฮิจัง"

# hi "Yeah."
hi "อื้ม"

# "Her head is buried in my chest. It feels like she's talking into my scar. She might be able to feel it brushing against her cheek."
"เธอซุกหัวเข้ากับอกฉันราวกับว่าเธอกำลังพูดอยู่กับแผลเป็นของฉันอยู่ รอยแผลเป็นน่าจะโดนเข้ากับแก้มของมิช่าอยู่"

# "I'd tried too hard to hide it from both of them before. It seems like such a dumb thing to have worried so much about, in retrospect."
"ก่อนหน้านี้ฉันคอยปกปิดเรื่องนี้กับทั้งสองคนมาตลอด แต่พอมาย้อนคิดดูแล้วก็รู้สึกว่างี่เง่าที่มาคิดมากกับอะไรอย่างนี้"

show mishashort perky_sad_close_ss
with charachange

#***choice 1

label th_choiceS28:
menu:
    with menueffect

#choice:
    # mi "Please comfort me, Hicchan. Just for today."
    mi "ขอร้องละฮิจัง ขอแค่วันนี้วันเดียว ปลอบฉันหน่อยสิ"

    # "Comfort Misha.":
    "ปลอบมิช่า":
        return m1

    # "Refuse.":
    "ปฏิเสธ":
        return m2

# Comfort Misha
label th_S28a:

play music music_moonlight fadein 4.0

# "As much as I pretend to protest, I've allowed things to come to this point. Even though I knew so far ahead of when she actually came out with it that this was what she was getting at."
"แม้ฉันจะทำเป็นต่อต้านเพียงใด แต่ฉันก็ปล่อยให้เรื่องมาจนถึงจุดนี้ ทั้งที่ฉันรู้มาตั้งนานแล้วว่าเธอหมายความอย่างนี้\nตั้งแต่ตอนที่เธอเปิดใจเรื่องนั้น"

# "At the very least, I was okay with this outcome. If I needed any more proof, it's simple: I still haven't turned her away."
"อย่างน้อยฉันก็รับผลลัพธ์นี้ได้ ถ้าจะถามหาหลักฐานก็ง่ายนิดเดียว นั่นคือการที่ฉันยังไม่บอกปัดเธอไป"

# "I could have at any point, and it was wrong of me not to do it sooner, but now, not doing so is something beyond simple carelessness."
"ฉันจะบอกปัดไปตอนไหนก็ได้ และผิดที่ฉันไม่ยอมบอกปัดไปให้เร็วกว่านี้ แต่การที่ตอนนี้ฉันไม่ยอมบอกปัดนั้นไม่ใช่\nเพียงเพราะแค่ความประมาทแล้ว"

show mishashort perky_sad_close_ss:
    linear 0.2 alpha 0 ypos 1.1
with vpunch

hide mishashort
with None

# "Misha takes my silence as agreement, and squeezes herself against me tightly, as if she is trying to get into my clothes. My arms are enveloped by the softness of her skin and the warmth of her body. I roll over on reflex, and end up on top of her."
"มิช่าเห็นฉันเงียบไปจึงถือเอาว่าฉันตกลง เธอแนบตัวเข้ามาแน่นขึ้นราวกับจะมุดเข้ามาในเสื้อผ้าของฉัน ความนุ่ม\nจากผิวเธอและความอบอุ่นจากกายเธอแนบแขนฉันไว้ ฉันพลิกตัวคร่อมเธอไปโดยอัตโนมัติ"

# "She looks at me, as if expecting me to take the lead, and closes her eyes nervously the second I return her gaze. I guess I have no choice, and I clumsily begin trying to undress her, something I've never done before."
"เธอมองมาที่ฉันคล้ายรอให้ฉันนำทางก่อนจะหลับตาไปด้วยความประหม่าทันทีที่ฉันมองกลับ คงไม่มีทางเลือกอื่นละนะ\nฉันถอดเสื้อผ้าเธออย่างเก้ ๆ กัง ๆ เพราะไม่เคยทำมาก่อน"

label th_S28h:

scene evh misha_naked:
    xalign 1.0 ypos 0.0 subpixel True
    easein 12.0 xalign 0.0
with whiteout

# "After all, I've only had sex once before, and I was restrained to a chair. This time, I'm in control, like I'd wished then. But it's really kind of scary, now that I am. I start by unbuttoning her blouse, and slipping it off of her shoulders."
"ก็เพราะฉันเคยมีอะไรกับใครมาแค่ครั้งเดียว แถมตอนนั้นฉันก็ถูกมัดไว้กับเก้าอี้ด้วย คราวนี้ฉันได้เป็นคนคุมดังหวังแล้ว\nแต่พอได้คุมแล้วฉันก็กลัวขึ้นมา ฉันปลดกระดุมเสื้อมิช่าออกแล้วค่อย ๆ ดึงขึ้นมาตามไหล่"

# "Her figure is curvier than I expected, and complements her cute face."
"รูปร่างของเธอมีส่วนโค้งเว้ามากกว่าที่ฉันคิดเอาไว้ซึ่งรับกับใบหน้าน่ารักของเธอ"

# "Her bra unhooks in the back, and I have trouble getting it off, partly because Misha seems ashamed of her breasts, and halfheartedly tries to cover them before I've even undone it."
"ตะขอยกทรงอยู่ข้างหลัง ปลดยากแฮะ ส่วนหนึ่งก็เพราะมิช่าเหมือนจะอายกับหน้าอกตัวเองแล้วเอามือปิด ๆ ก่อนที่ฉัน\nจะทันได้ปลดตะขอเสียอีก"

# "When I unlatch her skirt and start pulling down her panties, she offers more moments of weak, fake resistance. It's just a formality."
"พอฉันปลดกระโปรงแล้วชักกางเกงในมิช่าออกเธอก็ทำทีเป็นขัดขืนเล็กน้อยพอเป็นพิธี"

# "I realize now that formalities are very important to Misha. It's why she always greets everyone so happily, even when she probably isn't happy to see them."
"ฉันรู้ว่า ‘พิธี’ นั้นสำคัญกับมิช่าแค่ไหน เพราะอย่างนี้เธอถึงได้ทักทายทุกคนอย่างร่าเริง ทั้งที่บางครั้งเธออาจจะไม่ได้\nยินดีที่ได้เจอคนหนึ่ง ๆ"

# "Her eyes are open now, and I run my hand up the inside of her thigh, almost laughing when she shudders and nearly crushes it when she tightens her legs. A genuine reaction, and a cute one."
"เธอลืมตาแล้ว ฉันใช้มือลูบไปตามต้นขาด้านในของมิช่า เธอสะดุ้งจนขาหนีบมือฉันแทบหัก เห็นแล้วก็แทบกลั้นขำ\nไม่อยู่ เป็นความตกใจที่แสดงออกมาจริง ๆ แล้วก็น่ารักดีด้วย"

# "Shizune was better at hiding her inexperience, even though she was just as embarrassed."
"ชิซูเนะปกปิดได้ดีกว่ามิช่าว่าตัวเองนั้นไม่เคย ทั้งที่ทั้งสองคนก็อายพอ ๆ กัน"

# hi "Are you ready?"
hi "พร้อมหรือยัง"

# "She nods without looking at me."
"เธอพยักหน้าไม่มองฉัน"

scene evh misha_sex_aside:
    truecenter
    subpixel True zoom 1.05
    easein 6.0 zoom 1.0
with locationchange

# "As I push myself into her, I can feel her becoming rigid with nervousness, which I start to feel as well when I meet a resistance inside her. I feel so tense that every time I move, it feels painfully mechanical."
"ยิ่งเข้าไปลึกเท่าไหร่ ฉันก็ยิ่งสัมผัสได้ถึงเธอที่เกร็งด้วยความประหม่ามากเท่านั้น ซึ่งฉันเองก็เริ่มประหม่าเช่นกัน\nเมื่อต้องดุนดันเข้าไปด้วยความยากลำบาก ฉันเกร็งจนการขยับตัวของฉันนั้นไม่เป็นธรรมชาติเอาเสียเลย"

# "I wonder if I should go more quickly, like Shizune did. But Shizune is pretty forward. It's a different situation now, one I regret getting myself into. I start pushing in slowly, and Misha winces in pain."
"หรือจะขยับให้เร็วกว่านี้เหมือนที่ชิซูเนะทำดี แต่กับชิซูเนะไม่ได้มีอะไรซับซ้อน ส่วนตอนนี้เป็นคนละเรื่อง เป็นเรื่องที่ฉัน\nนึกเสียใจที่ทำด้วย ฉันดันเข้าไปช้า ๆ จนมิช่ากระตุกด้วยความเจ็บ"

# mi "Please do it quickly…"
mi "ทำเร็ว ๆ หน่อย…"

scene evh misha_sex_closed:
    zoom 1.0
with locationchange

# mi "Ow…"
mi "โอ๊ย…"

# "I stop."
"ฉันหยุด"

scene evh misha_sex_aside
with locationchange

# mi "No, it's okay."
mi "ไม่ ไม่เป็นไร"

# "And then I push myself even deeper into her, to the hilt, feeling Misha's hands clasp my arms, and then reach higher, as if she is trying to climb them."
"และดันตัวเองเข้าไปภายในเธอให้ลึกขึ้นจนถึงที่สุด มิช่ายื่นมือมาคว้าแขนฉันไว้แล้วไล่ขึ้นไปเรื่อย ๆ ราวกับจะปีนขึ้นไป"

# "Grabbing at my shoulders, she pulls herself against me, joining us more tightly together, and I can't do anything but push back."
"เธอจับไหล่ฉันไว้แล้วดึงตัวเองเข้าหาฉันจนเราสองคนชิดสนิทแนบแน่นกันเข้าไปอีก ฉันจึงได้แต่ดันเข้าไปอีก"

scene evh misha_sex_closed
with locationchange

# mi "Ah~… aaah…"
mi "อ๊ะ~ อ๊าาา……"

# "Hearing her moans, I speed up and find a rhythm. Her hands grip each other around my back, and I feel her elbows digging into the space under my ribs as I piston into her."
"ยิ่งเธอครางฉันก็ยิ่งเร่งเร้าจังหวะให้เข้าที่ มิช่าประสานมือกอดฉันเอาไว้จนทุกครั้งที่ฉันกระแทกข้อศอกของเธอก็กด\nเข้ากับบริเวณใต้ซี่โครงของฉัน"

# "The blood pounds in my ears like the beating of a drum, until I can barely hear her."
"เสียงชีพจรเต้นดังอยู่ในหัวรัวเร็วราวกลองจนฉันแทบไม่ได้ยินมิช่า"

# mi "Hnn~…"
mi "อื้อ~…"

scene evh misha_sex_aside
with locationchange

# mi "This is my first time with a man. It's weird."
mi "ครั้งแรกเลยที่ได้ทำกับผู้ชาย แปลกจัง"

# "I wish she would stop talking. Her voice is so quiet and breathy that I have trouble understanding her, but the tone of sadness permeating it is unmistakable, and only makes me feel guiltier."
"อยากให้เธอหยุดพูดจริง ๆ เสียงเธอทั้งแผ่วทั้งหอบจนฉันแทบฟังไม่รู้เรื่องก็จริง แต่ความเศร้าที่เจืออยู่ในน้ำเสียงนั้นฉัน\nรับรู้ได้ชัด ซึ่งยิ่งทำให้ฉันรู้สึกผิดหนักเข้าไปอีก"

# "I'm supposed to be comforting her, but it's entirely physical, and if Misha is being reassured in any way by this, she isn't showing it. That makes me question whether my decision was the right one. I'm really starting to doubt it."
"ฉันต้องปลอบมิช่าสิ แต่ที่ทำก็เป็นการปลอบทางกายเท่านั้น และถ้ามิช่าสบายใจขึ้นจริงก็ต้องแสดงสีหน้าอะไรบ้างสิ\nฉันนึกสงสัยว่าฉันเลือกถูกแล้วหรือเปล่า ชักไม่แน่ใจแล้ว"

scene evh misha_sex_closed
with locationchange

# "Despite that, her soft cooing in my ear makes me keep going, as does the hot, slick tightness around my member. Eventually, her leg twisting around mine, she tenses up in orgasm, her smooth neck rubbing across my cheek."
"แต่ถึงอย่างนั้น เสียงร้องแผ่วเบาในหูฉัน—และความรัดแน่นอันอบอุ่นและชื้นแฉะภายในตัวเธอ—ยังทำให้ฉันขยับต่อ\nจนในที่สุดเธอก็ถึงฝั่งจนตัวเกร็งขางอรัดตัวฉันแน่น คอเรียบเนียนของเธอถูกกับแก้มฉัน"

scene evh misha_naked
with whiteout

stop music fadeout 6.0

# "It takes her a minute to separate herself from me. It gives me an opportunity to see her body fully, her pink skin blushing bright red and dabbed with sweat. I feel cold."
"ผ่านไปสักหนึ่งนาทีเธอถึงผละตัวฉันออกจนฉันได้เห็นเรือนร่างเธอทั้งตัว ผิวนวลของเธอขึ้นสีแดงเรื่อพร้อมเหงื่อที่\nชโลมอยู่ หนาวจัง"

# mi "…Hicchan?"
mi "…ฮิจัง?"

# "I can't hear anything but the ticking of the clock, and the sound of my own breathing."
"เสียงที่อยู่ในหูฉันตอนนี้มีเพียงเสียงเข็มนาฬิกาเดินและเสียงหอบของฉัน"

# mi "…Never mind, Hicchan."
mi "…ช่างเถอะฮิจัง"

# "I search around for Misha's hand with my own, and caress it. How light and delicate it seems, even as it grabs me so tightly around my wrist. The feeling is familiar."
"ฉันคลำเปะปะหามือมิช่าแล้วจับเอาไว้ เป็นมือที่ดูแสนจะเบาหวิวและบอบบาง แม้มือนั้นจะกำลังจับข้อมือฉันแน่นอยู่\nก็ตาม เป็นความรู้สึกที่คุ้นเคย"

scene black
with dissolve

#***choice 2

# Refuse
label th_S28b:

show mishashort perky_sad_close_ss:
    linear 0.2 alpha 0 ypos 1.1
with vpunch

hide mishashort
with None

play sound sfx_pillow

# "Before I can answer, she pushes her whole weight against me, and it unbalances me enough to send us both onto the bed. If I don't answer quickly, then the situation will only become more precarious."
"ฉันยังไม่ทันได้ตอบเธอก็ทิ้งตัวมาแนบฉันแล้ว ซึ่งแนบแรงจนเราทั้งสองคนล้มลงไปกับเตียง ถ้าไม่รีบตอบแล้วสถานการณ์\nจะยิ่งหมิ่นเหม่ไปกว่านี้แน่"

# "I know that I should have never let things get as tangled as they already are."
"ฉันรู้ดีว่าฉันไม่ควรปล่อยให้อะไร ๆ มันยุ่งเหยิงไปมากกว่านี้"

# "So, even though it isn't the most tactful way to refuse her, I push her off of me. Misha falls backwards onto the sheets, so softly that it seems like she barely fell at all. Eyes closed, she stays like that for a while, before getting up with a hollow laugh."
"ฉันผลักตัวมิช่าออก ฉันรู้ว่านี่ไม่ใช่วิธีปฏิเสธที่ดูเป็นคนมีหัวคิดมากนัก เธอหงายหลังตกลงกับที่นอนเบาชนิดที่ว่า\nเหมือนหลังไม่ได้กระแทกเลยด้วยซ้ำ เธอนอนนิ่งอยู่สักพักก่อนจะลุกขึ้นนั่งหัวเราะแห้ง ๆ"

show mishashort invis:
    center
    ypos 1.2
with None

show mishashort perky_sad_ss at center
with dissolvecharamove

play music music_moonlight fadein 6.0

# mi "You're right, Hicchan. I'm sorry."
mi "ถูกของนาย ฮิจัง ฉันขอโทษ"

scene black
with shuteye

# "I'm not sure how I feel. Regretful, slightly, even though I've grown to hate regret. Sad, for a multitude of reasons. I'm also a little angry, both at her and at myself. And in a way, it even seems like I'm not really feeling at all."
"ฉันก็ไม่แน่ใจเหมือนกันว่าตอนนี้ฉันรู้สึกยังไง เสียใจ นิดหน่อย ถึงฉันจะเกลียดความเสียใจแล้วก็เถอะ เศร้า ด้วยเหตุผล\nล้านแปด แล้วก็โกรธหน่อย ๆ ด้วย โกรธทั้งมิช่าโกรธทั้งตัวเอง และในแง่หนึ่งก็ดูเหมือนว่าฉันจะไม่ได้รู้สึกอะไรเลย\nด้วยซ้ำ"

# hi "Don't be."
hi "ไม่ต้องขอโทษหรอก"

# mi "No, Hicchan. It's okay~. I am, really, really~."
mi "ไม่ได้สิฮิจัง ไม่เป็นไรน่า~ ฉันขอโทษจริง ๆ จริง ๆ ~"

# mi "But… just asking was enough for me, I think."
mi "แต่… แค่ได้ถามฉันก็พอใจแล้วละ คิดว่านะ"

# mi "I'm happier that you said no."
mi "ฉันดีใจเสียอีกที่นายปฏิเสธ"

# hi "Is that right? Well, that's good."
hi "จริงเหรอ งั้นก็ดีแล้ว"

# mi "Yeah~, it is. Thanks, Hicchan."
mi "อื้ม~ ดี ขอบใจนะฮิจัง"

# "She pulls herself up and leans against the wall. I'm assuming she is. My head hurts so much that I don't bother opening my eyes. I lie on my bed, listening to the rustle of my hair brushing against the sheets and the grass waving in the wind outside."
"เธอลุกขึ้นยืนพิงผนัง เดาว่านะ ฉันปวดหัวจนไม่อยากลืมตาแล้ว ฉันนอนอยู่บนเตียงคอยฟังเสียงผมของฉันที่ยีอยู่\nกับที่นอนและเสียงหญ้าที่ไหวลู่ลมอยู่ข้างนอก"

# "I guess that I should say more to reassure her, but I wonder if that would really help. Maybe it would be better to say nothing. I just don't know, although I think that in this situation, there's no one right thing I can do."
"จริง ๆ คงต้องพูดอะไรปลอบมิช่าอีก แต่จะช่วยได้หรือเปล่าเถอะ ไม่พูดอะไรเลยคงดีกว่า ไม่รู้สิ สถานการณ์อย่างนี้\nอาจจะไม่มีทางเลือกที่ถูกจริง ๆ ก็ได้"

# mi "Goodnight, Hicchan."
mi "ราตรีสวัสดิ์นะฮิจัง"

play sound sfx_doorclose

stop music fadeout 4.0

# "With that, she leaves, the door clicking shut behind her like a guilty whisper."
"เธอพูดแล้วก็เดินออกไป เสียงประตูที่ปิดไล่หลังมานั้นฟังราวกับเป็นเสียงกระซิบแห่งสำนึกผิด"

# "Maybe it's because I'm eager to put today behind me, but after Misha is gone, I find it much easier to fall asleep. I do so almost instantly."
"แต่พอมิช่าไปแล้วก็รู้สึกว่าหลับได้ง่ายขึ้นมาก อาจเพราะฉันอยากจะรีบไปให้พ้น ๆ จากวันนี้ ฉันผล็อยหลับไปแทบจะ\nในทันทีที่หลับตาลง"

scene black
with dissolve


#######################################################

label th_S29:

scene bg school_dormhisao
with locationchange

play music music_night fadein 4.0

# "The following morning, I wake up thinking that most of my time is going to be spent trying to avoid Shizune and Misha."
"เช้าวันถัดมาฉันตื่นมาพร้อมความคิดที่อยากจะหลบหน้าทั้งชิซูเนะและมิช่า"

# "What happened last evening still makes me feel uneasy. I'd thought that sleeping on it would help alleviate that feeling. I feel like an idiot for believing it would be that easy."
"เรื่องเมื่อตอนค่ำยังทำฉันอึดอัด ทีแรกก็นึกว่าหลับแล้วจะเลิกรู้สึกอย่างนั้นได้สักที แต่ก็ดูท่าว่าจะคิดตื้นไปที่ว่าแค่หลับ\nแล้วจะเลิกคิดได้ง่าย ๆ อย่างนั้น"

# "I think about whether or not Misha might feel the same way. If so, she probably won't show up to school today. I'd considered doing the same, but it would be pretty suspicious, and staying inside all day in fear doesn't appeal to me. It never really has."
"มิช่าจะรู้สึกเหมือนกันหรือเปล่านะ ถ้าใช่วันนี้มิช่าก็คงไม่มาเรียน ฉันคิดจะโดดเหมือนกัน แต่เดี๋ยวจะดูน่าสงสัยอีก\nแล้วไอ้การมัวแต่กลัวอุดอู้อยู่ในห้องนี่ก็ฟังดูไม่น่าอภิรมย์เท่าไหร่ ไม่เลย"

scene bg school_scienceroom
with locationskip

# "Like I thought, Misha isn't in class this morning. Shizune is, but today is a busier day than most, so she gives her all concentrating on her classwork, and that means there's little idle time for her to start up a conversation with me."
"ตามคาด เช้านี้มิช่าไม่เข้าเรียน ชิซูเนะมา แต่วันนี้มีงานเยอะกว่าทุกที เธอจึงจดจ่ออยู่กับการทำงานในห้อง และแปลว่า\nเธอจะเหลือเวลาว่างที่จะมาทักฉันได้น้อยลง"

#bad end lines
label th_S29a:

# "It's strange that I should be running from the thought of having to talk to Shizune after spending so much time trying to do just that, but I can't think of any other way I should feel. I had sex with her best friend."
"แปลกดี ตอนนี้ดันมาเลี่ยงไม่อยากคุยกับชิซูเนะ ทั้งที่ก่อนหน้านี้ทุ่มเวลาไปแทบตายเพื่อจะได้คุย แต่ก็ไม่รู้จะรู้สึกยังไงดี\nเหมือนกัน ฉันมีอะไรกันกับเพื่อนของเธอไปแล้ว"

# "If I feel this way about it, I wonder how Misha must feel. Just as regretful? When she came on to me, she was more depressed than sexy to start with. I can only imagine how much worse it would be now."
"ถ้าฉันรู้สึกอย่างนี้แล้วมิช่าจะเป็นยังไง เสียใจพอกันเหรอ ตอนที่มิช่าเข้าหาฉันด้วยความอยากนั้นเธอดูหดหู่มากกว่า\nจะมีอารมณ์ด้วยซ้ำ แล้วตอนนี้ก็คงจะยิ่งหดหู่หนักไปอีก"

# "Thinking about it like that, I want to see her again. But only halfheartedly. The other half of me is still terrified, even though I hate to use that word."
"พอคิดอย่างนี้แล้วก็อยากเจอมิช่าอีก แต่ก็แค่ใจหนึ่งน่ะนะ เพราะอีกใจฉันยังกลัว ถึงฉันจะไม่อยากใช้คำนั้นเลยก็เถอะ"

# "It makes me feel ashamed, but I'm sure it's the only way to describe myself right now. It's not a good feeling."
"คิดแล้วก็ละอายใจ แต่ก็น่าจะมีแค่คำนั้นแหละที่ใช้อธิบายตัวฉันตอนนี้ได้ เป็นความรู้สึกที่ไม่ดีเลย"

#good end lines
label th_S29b:

# "I'd grown so used to seeing Shizune and Misha together that I hadn't realized until yesterday how much that hasn't been the case lately."
"ฉันเห็นชิซูเนะกับมิช่าอยู่ด้วยกันจนชินตาแล้ว ชินจนถึงขั้นที่ว่าเพิ่งรู้ตัวเมื่อวานว่าช่วงนี้สองคนนี้ไม่ค่อยได้อยู่ด้วยกันเลย"

# "And it's a shame, because the empty seat next to her reminds me that they are a pair. So, yesterday is something I'll take to my grave."
"ซึ่งน่าเสียดาย เพราะเก้าอี้ตัวข้าง ๆ ที่ว่างเป็นเครื่องเตือนถึงฉันว่าสองคนนั้นอยู่ด้วยกัน ดังนั้นสิ่งที่เกิดขึ้นเมื่อวาน\nฉันจะเก็บเป็นความลับไปจนวันตาย"

# "If I feel this way about it, I wonder how Misha must feel. Just as regretful? When she came on to me, she was more depressed than sexy to start with. I can only imagine how much worse it would be now."
"ถ้าฉันรู้สึกอย่างนี้แล้วมิช่าจะเป็นยังไง เสียใจพอกันเหรอ ตอนที่มิช่าเข้าหาฉันด้วยความอยากนั้นเธอดูหดหู่มากกว่า\nจะมีอารมณ์ด้วยซ้ำ แล้วตอนนี้ก็คงจะยิ่งหดหู่หนักไปอีก"

# "Thinking about it like that, I want to see her again. But only halfheartedly. The other half of me is still terrified, even though I hate to use that word."
"พอคิดอย่างนี้แล้วก็อยากเจอมิช่าอีก แต่ก็แค่ใจหนึ่งน่ะนะ เพราะอีกใจฉันยังกลัว ถึงฉันจะไม่อยากใช้คำนั้นเลยก็เถอะ"

# "It makes me feel ashamed, but I'm sure it's the only way to describe myself right now."
"คิดแล้วก็ละอายใจ แต่ก็น่าจะมีแค่คำนั้นแหละที่ใช้อธิบายตัวฉันตอนนี้ได้ เป็นความรู้สึกที่ไม่ดีเลย"

#end split
label th_S29x:

scene bg school_library
with shorttimeskip

# "I spend the next couple periods in the library, not in the mood to sit in classes for the rest of the day, but unwilling to walk back to the dorms."
"อีกสองคาบถัดมาฉันโดดมาอยู่ที่ห้องสมุดเพราะไม่มีอารมณ์จะนั่งเรียนจนหมดวัน และไม่มีอารมณ์จะเดินกลับหอด้วย"

show shizu invis at center
with None

show shizu behind_frown at Position(ypos=1.14)
with dissolvecharamove

# "While I'm lazily flipping through the pages of an uninteresting historical fiction novel, Shizune drops herself into the chair across from me, pouting."
"ระหว่างที่ฉันพลิกหน้านิยายเชิงประวัติศาสตร์ที่น่าเบื่อเล่มหนึ่งไปเอื่อย ๆ ชิซูเนะก็มาหย่อนตัวลงนั่งที่เก้าอี้ตรงหน้าฉัน\nทำหน้าไม่พอใจ"

show shizu adjust_frown
with charachange

# ssh "I think it's sort of pointless to come to school and then skip every class."
ssh "ถ้าจะมาเรียนแล้วโดดทุกคาบแล้วจะมาเพื่ออะไร"

# his "Sorry."
his "ขอโทษ"

show shizu behind_frustrated
with charachange

# ssh "At least tell everyone that you're sick."
ssh "อย่างน้อยก็บอกคนอื่นสิว่าไม่สบาย"

# his "I'm just not feeling it today. Yesterday I was fine, though. Tomorrow, I'll probably be fine. Taking a sick day in the middle of the week is just too suspicious. That “24-hour flu” thing or whatever won't fly."
his "วันนี้ไม่ค่อยอยากเรียนน่ะ แต่เมื่อวานก็ยังปกติดีนะ พรุ่งนี้ก็คงปกติดี ให้ลาเรียนเอาวันที่อยู่กลางสัปดาห์มันก็น่าสงสัย\nเกินไป ไอ้ “ไข้หวัดยี่สิบสี่ชั่วโมง” อะไรนั่นน่ะคนเขาไม่เชื่อหรอก"

show shizu adjust_frown
with charachange

# ssh "It's not suspicious."
ssh "ไม่เห็นจะน่าสงสัย"

# his "It is."
his "น่าสงสัยสิ"

show shizu basic_angry
with charachange

# "I turn back to my book, but Shizune gently pulls it down, in contrast with her expression, which straddles the line between concern and anger."
"ฉันกลับมาอ่านหนังสือต่อ แต่ชิซูเนะก็ดึงหนังสือลงอย่างอ่อนโยนขัดกับสีหน้าของเธอที่มีทั้งความเป็นห่วง\nกับความโกรธ"

show shizu behind_blank
with charachange

# ssh "Is something wrong?"
ssh "มีอะไรหรือเปล่า"

# his "What?"
his "อะไรนะ"

show shizu basic_normal2
with charachange

# ssh "Is something bothering you? Because you're acting a little suspicious today, in a different way."
ssh "นายไม่สบายใจเรื่องอะไรหรือเปล่า วันนี้นายทำตัวน่าสงสัยอยู่หน่อย ๆ นะ แต่ไม่ใช่น่าสงสัยแบบนั้น"

show shizu behind_blank
with charachange

# ssh "If there is, just tell me, or I'll be mad. I'm not good at reading people."
ssh "ถ้ามีเรื่องไม่สบายใจก็บอกฉันได้ ไม่บอกฉันโกรธนะ ฉันอ่านใจคนไม่เก่ง"

# "What a ridiculous thing to say, after picking up my mood so easily."
"ไร้สาระ บอกว่าอ่านใจคนไม่เก่งแต่ดันดูอารมณ์ฉันออกเนี่ยนะ"

# "She is only half-kidding, but there is some truth in it. After all, she can't hear tone, and has to rely on reading to communicate with others."
"จริง ๆ เธอก็ว่าแบบกึ่งล้อเล่นกึ่งจริงจังนั่นแหละ ก็นะ ชิซูเนะฟังน้ำเสียงไม่ได้ ต้องอาศัยการอ่านเท่านั้นในการสื่อสาร\nกับคนอื่น"

# "It's as if you could only ever have conversations with someone through text messages. That has to mess with you in some way."
"ให้เทียบก็เหมือนการที่ต้องคุยกับใครบางคนผ่านการส่งข้อความเท่านั้นน่ะแหละ นาน ๆ เข้ายังไงก็ต้องมีระบบรวนกันบ้าง"

# "It's probably why she stares so intently at people, in order to gauge their reaction. Or maybe it's why she pushes people so hard, to get them to react."
"อาจจะเพราะอย่างนี้เธอถึงได้จ้องคนแบบจ้องเขม็งเลย จะได้ดูปฏิกิริยาว่าเป็นยังไง และอาจจะเพราะอย่างนี้เธอถึงได้\nรบเร้าใครต่อใครแบบหนัก ๆ จะได้ให้คนเหล่านั้นตอบสนอง"

# "I've thought about it before, but it's too hard to say for sure what Shizune's exact motivations are for anything."
"ฉันก็เคยคิดอย่างนั้นบ้าง แต่เจตนาที่แท้จริงของชิซูเนะกับการทำอะไร ๆ นั้นเป็นสิ่งที่บอกได้ยากมาก"

# "So, I wonder how much of that was a joke. Sometimes, it's easy to tell. This time, it isn't. Assuming it wasn't a joke, I can't tell her anyway. Because it's sign language, there is enough time to collect myself and lie effectively."
"ฉันจึงสงสัยว่าสิ่งที่บอกนั้นส่วนที่พูดเล่นคือส่วนไหนบ้าง บางครั้งก็ดูออกง่าย แต่ครั้งนี้ดูแทบไม่ออกเลย แต่ต่อให้\nพูดเล่นฉันก็คงบอกชิซูเนะไม่ได้อยู่ดี และภาษามือก็ทำให้ฉันมีเวลาได้ตั้งตัวคิดคำโกหกอันแนบเนียน"

# his "Nothing."
his "ไม่มี"

show shizu cross_wut
with charachange

shi "…"

# his "I've just been thinking a lot about the Student Council's future, lately. I believe Misha is doing the same… well, in her own way."
his "แค่ว่าช่วงนี้ฉันคิดหายอย่างเรื่องอนาคตของสภานักเรียนน่ะ มิช่าก็คงเหมือนกัน… คิดในแบบมิช่าน่ะนะ"

show shizu behind_frustrated
with charachange

# ssh "So am I, but she isn't here today. I wish she would have let me know something, because I might need her help later today. Yours too, unless you're busy."
ssh "ฉันก็เหมือนกันนั่นแหละ แต่วันนี้มิช่าไม่อยู่ แต่บอกกันหน่อยก็น่าจะดี เพราะวันนี้ฉันน่าจะมีเรื่องให้มิช่าช่วยอยู่\nอาจจะต้องขอแรงนายด้วย ถ้านายว่างน่ะนะ"

# his "I'm not…"
his "ว่าง…"

show shizu basic_normal
with charachange

# ssh "Thank you."
ssh "ขอบคุณ"

show shizu behind_sad
with charachange

# ssh "I feel like I'm losing a lot of people close to me, lately."
ssh "ช่วงนี้ฉันรู้สึกเหมือนเสียคนสนิทไปเยอะเลย"

# "I can't think of a good way to respond to that. Something reassuring and confident, telling her not to worry. “I'm here for you. I'm not one of those people.”"
"ไม่รู้จะตอบยังไงดี หรือจะหาอะไรทีี่ฟังแล้วใจชื้นขึ้น แบบที่บอกไปแล้วจะเลิกคิดมาก “ฉันจะอยู่ข้างเธอนะ ฉันไม่เหมือน\nคนพวกนั้นหรอก”"

# "Then, who is? And it seems so forced. I manage a wave of my hand that seems extremely callous as soon as I do it."
"แล้วคนที่ว่านี่คือใคร แถมฟังดูไม่เป็นธรรมชาติเอาเสียเลย ฉันโบกมือปัดจนดูเหมือนว่าฉันไม่ได้สนใจเรื่องของเธอ\nแม้แต่น้อย"

# his "You shouldn't feel that way."
his "อย่าไปคิดอย่างนั้นสิ"

show shizu basic_normal2
with charachange

shi "…"

# his "I might be just a little sick, not enough to go through the trouble of making it official. It's just easier for me this way."
his "ฉันอาจจะไม่สบายนิดหน่อย แบบไม่ได้หนักถึงขั้นที่ต้องทำเรื่องลาขนาดนั้น ฉันว่าทำแบบนี้มันก็ง่ายกว่า"

show shizu behind_frown
with charachange

# ssh "It's the wrong way."
ssh "ทำผิดแล้ว"

# "I've heard the hard way and the right way are usually the same thing, so it's not a big stretch to say that the opposite is true."
"ฉันเคยได้ยินมาว่าการทำอะไรแบบลำบากมักจะเป็นแบบที่ถูก ดังนั้น หากจะกล่าวว่าการทำอะไรแบบง่าย ๆ มักจะเป็น\nแบบที่ผิดก็คงไม่ผิดมากนัก"

show shizu basic_normal
with charachange

# ssh "Well, fine. If you say you are all right, that's good enough for me."
ssh "เอาเถอะ ตามนั้น ถ้านายว่าไม่มีอะไรก็ดีแล้ว"

# his "Wait."
his "เดี๋ยว"

show shizu behind_blank
with charachange

shi "…?"

# his "You asked me, so I'm turning it around. Is everything okay with you?"
his "เธอถามฉันแล้ว ฉันขอถามเธอบ้าง เธอมีเรื่องหนักใจอะไรอยู่หรือเปล่า"

show shizu basic_normal2
with charachange

# ssh "Yes."
ssh "ไม่มี"

stop music fadeout 3.0

# "She signs it without a moment's hesitation. After that, Shizune waits to see if I'm going to follow up on it."
"ชิซูเนะทำภาษามือตอบกลับมาแบบทันควัน จากนั้นเธอก็รอดูว่าฉันจะถามอะไรต่ออีกหรือเปล่า"

show shizu invis at center
with dissolvecharamove

hide shizu
with None

# "I don't, and she leaves. I feel like an idiot for not going further, even though I think it's better that I didn't."
"ซึ่งฉันก็ไม่ได้ถาม เธอจึงเดินออกไป โง่จริง ๆ ที่ไม่ซักไซ้ต่อ แต่เอาเข้าจริง ไม่ถามต่ออีกก็คงดีแล้วละ"

# "I've been in the library for quite a while, and decide to go up to the roof for a change of pace."
"ฉันอยู่ห้องสมุดมาได้สักพักหนึ่งแล้วจึงตัดสินใจขึ้นไปบนดาดฟ้าเปลี่ยนบรรยากาศบ้าง"

play sound sfx_door_creak
play ambient sfx_rooftop fadein 1.0

scene bg school_roof_ss
with locationskip

# "A fresh breeze hits me the second I open the door. This is really my favorite area of the school, I think. Then I see that I'm not the only one here. I can see a girl with bubblegum-pink hair in front of me."
"ทันทีที่เปิดประตูลมเย็น ๆ ก็เข้าปะทะ ดาดฟ้าน่าจะเป็นที่ในโรงเรียนนี้ที่ฉันชอบที่สุดแล้วละมั้ง และก็พบว่าฉันไม่ได้\nอยู่คนเดียว ตรงหน้ายังมีสาวผมสีชมพูอย่างหมากฝรั่งอยู่"

# "Her back is to me, but I don't have to see her face to know who it is. I'm sure Misha is the only person in the world with hair like that."
"แม้เธอจะหันหลังให้ฉัน แต่ฉันก็รู้ว่าเธอเป็นใคร มิช่าคงเป็นคนเดียวบนโลกใบนี้ที่มีผมอย่างนั้น"

# "I get the feeling that I've stumbled on her at a bad moment. She obviously wants to be alone, and I wonder if she hasn't noticed my presence. If so, I'll leave right now. But she has, and turns to face me."
"เหมือนจะมาผิดจังหวะไปหน่อย ยังไงมิช่าก็คงอยากอยู่คนเดียวแน่ ๆ จะรู้ตัวหรือยังนะว่าฉันมา ถ้ายังก็จะได้เดินออกไป\nแต่แล้วเธอก็รู้สึกตัวและหันมาหาฉัน"

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

scene ev misha_roof_normal:
    yalign 1.0 xalign 0.5 subpixel True
    easein 12.0 yalign 0.0
with whiteout

play music music_sadness fadein 8.0

# mi "Oh, Hicchan. I thought someone was behind me, but I didn't think it was going to be you. This time, you surprised me."
mi "อ้าว ฮิจัง เมื่อกี้รู้สึกเหมือนมีคนมา แต่ก็ไม่คิดว่าจะเป็นนาย คราวนี้นายทำฉันตกใจนะเนี่ย"

# "If she's referring to her habit of sneaking up behind me and asking me to guess who it is… I've never been surprised by that."
"ถ้าตกใจที่ว่าคือหมายถึงปกติที่เธอชอบแอบซุ่มมาข้างหลังแล้วให้ทายว่าใครละก็… ฉันไม่เคยตกใจเลยสักครั้ง"

# hi "I'm surprised, too. But this is good. I had something I wanted to talk to you about, anyway."
hi "ฉันก็ตกใจเหมือนกัน แต่ก็ดี มีเรื่องจะคุยกับเธอพอดี"

mi "…"

# hi "Not that…"
hi "ไม่ใช่เรื่องนั้น…"

# hi "What's going on between you and Shizune? She won't tell me, so I'm asking you."
hi "เธอกับชิซูเนะมีเรื่องอะไรกันหรือเปล่า พอดีชิซูเนะไม่ยอมบอกเลยมาถามเธอ"

# "“Because you're easier to get an answer out of, since the same sign language that gives me the leeway to lie to her gives her a cushion against my questions, so that she can more easily brush them off.” When she hesitates, I push her harder."
"“เพราะถามเธอแล้วน่าจะได้คำตอบง่ายกว่า เพราะภาษามือที่ฉันใช้โกหกไปได้เนียน ๆ ก็เป็นสิ่งเดียวกันกับที่ชิซูเนะ\nใช้เบี่ยงคำถามฉันไปแบบง่าย ๆ เหมือนกัน” พอมิช่าลังเลฉันก็รบเร้าหนักขึ้น"

# hi "Give me an honest answer, please."
hi "ตอบมาตรง ๆ เลย ได้มั้ย"

# mi "It's complicated, Hicchan… It's because of something that happened a long time ago. I thought I could just forget about it, but~… it's really hard. So~, that and graduation coming up made me want to spend more time with Shicchan~!"
mi "มันซับซ้อนน่ะฮิจัง… มันเป็นเรื่องที่เกิดขึ้นเมื่อนานมาแล้ว ฉันก็คิดว่าเดี๋ยวก็คงลืม แต่~… มันยากมากเลย เพราะงั้น~\nทั้งเรื่องนั้นกับเวลาเรียนที่อีกเดี๋ยวก็จบแล้วทำให้ฉันอยากใช้เวลาอยู่กับชิจังอีกเยอะ ๆ ~!"

scene ev misha_roof_sad
with charachange

# mi "But Shicchan is always busy now. So~! We've been fighting. But, I'm tired of it now."
mi "แต่ช่วงนี้ชิจังยุ่งตลอดเลย เราก็เลย~! ทะเลาะกัน แต่ฉันเอือมแล้วละ"

# mi "Because~… I like Shicchan."
mi "เพราะ~ ฉันชอบชิจัง…"

# hi "So do I."
hi "ฉันก็ชอบ"

scene ev misha_roof_normal
with charachange

# mi "Wahaha~. No, no~. I know you like her, Hicchan. I mean that I like Shicchan in the same way."
mi "วะฮ่าฮ่า~ เปล่า เปล่า~ ฉันรู้ว่าฮิจังชอบชิจัง ที่ฉันบอกว่าชอบชิจังคือชอบแบบเดียวกับนาย"

scene ev misha_roof_closed
with charachange

# mi "I want her to be my girlfriend."
mi "ฉันอยากเป็นแฟนกับชิจัง"

# "Misha closes her eyes, like a condemned criminal confessing the last of their sins in front of the executioner. It only makes it harder for me to think of a response, and I know I have to give one."
"มิช่าหลับตาราวกับว่าเป็นอาชญากรที่สารภาพบาปประการสุดท้ายที่ได้ทำลงไปให้เพชฌฆาตได้ฟัง ซึ่งยิ่งทำให้ฉัน\nคิดหนักไม่รู้จะตอบว่าอย่างไรดี แต่ฉันต้องตอบ"

# hi "I see. I never knew."
hi "งั้นเหรอ ไม่เคยรู้เลย"

scene ev misha_roof_normal
with charachange

# mi "I didn't really want to come to this school, Hicchan~. But it sounded interesting, and even if everyone hated me, at least it felt like they would leave me alone. I was learning sign language, but wasn't very good at it~."
mi "จริง ๆ ฉันก็ไม่ได้อยากมาโรงเรียนนี้เลยฮิจัง~ แต่ก็ฟังดูน่าเรียนดี แถมต่อให้ทุกคนเกลียดฉัน อย่างน้อยพวกนั้นก็\nจะปล่อยให้ฉันได้อยู่คนเดียว ตอนนั้นฉันเรียนภาษามืออยู่ แต่ก็ไม่ค่อยเก่งเท่าไหร่หรอก~"

# mi "Shicchan was trying to get people to join the Student Council, because it was only her and Lilly. Then, she came up to me. I couldn't understand her at all~."
mi "ตอนนั้นชิจังหาคนมาเข้าสภานักเรียนเพราะทั้งสภามีแค่ชิจังกับลิลลี่ แล้วชิจังก็มาหาฉัน ฉันไม่เข้าใจอะไรที่ชิจัง\nบอกเลย~"

scene ev misha_roof_angry
with charachange

# mi "But~! Shicchan wouldn't use her pen and paper. She knew that I was taking sign language classes. I was exposed quickly, I didn't know any~… That only made her try harder, and I hated Shicchan and thought she was making fun of me."
mi "แต่~! ชิจังไม่ยอมใช้ปากกากับกระดาษ ชิจังรู้ว่าฉันเรียนภาษามืออยู่ ความแตกไวมาก ฉันยังไม่รู้เรื่องเลย~… แล้วชิจัง\nก็ยิ่งพยายามคุยอีกจนฉันไม่ชอบเพราะนึกว่าชิจังล้อฉันอยู่"

scene ev misha_roof_normal
with charachange

# mi "That wasn't the reason, though~…"
mi "แต่ไม่ใช่เพราะเรื่องนั้นหรอกนะ~…"

#"Misha smiles in fond reminiscence."
#nope

# mi "So~! I slowly fell in love with Shicchan, and I told her… that I loved her."
mi "จากนั้น~! ฉันก็เริ่มตกหลุมรักชิจัง แล้วก็บอกชิจังว่า… ฉันรักเธอ"

scene ev shizu_flashback:
    truecenter
    zoom 1.15 subpixel True
    easein 30.0 zoom 1.0
with whiteout

# mi "It was in the student council room, you know. When it was just the two of us."
mi "ตอนที่บอกน่ะ ฉันกับชิจังอยู่ในห้องสภานักเรียนด้วยกันสองต่อสอง"

# mi "I had these fantasies of Shicchan staying alone in the office, trying to put everything together all by herself. It seemed so lonely to me, and so sad~. I think I wanted it to be that way~."
mi "พอนึกภาพว่าชิจังอยู่ตัวคนเดียวในห้องทำงานแล้วทำทุกอย่างด้วยตัวของเธอเองก็เหงาแทนเลย ดูน่าเศร้ามาก~\nแต่ฉันว่าฉันอยากให้เป็นอย่างนั้นนะ~"

# mi "That way, I could be there for Shicchan, and maybe Shicchan would like me. Even though there was no reason for me to believe it, I did anyway. I wanted it to be true, so I was okay with letting myself believe it, even though I think I knew."
mi "เพราะถ้าเป็นอย่างนั้นแล้ว ฉันก็จะได้อยู่เคียงข้างชิจัง แล้วชิจังก็อาจจะชอบฉัน และทั้งที่ไม่ได้มีหลักฐานอะไรว่าจะเป็น\nอย่างนั้น ฉันก็ทำแบบนั้นอยู่ดี เพราะฉันอยากให้มันจริง ฉันเลยกล่อมตัวเองให้เชื่ออย่างนั้น ทั้งที่ฉันรู้ความเป็นจริง\nอยู่แก่ใจ"

# mi "That day was really, really~ beautiful, too, Hicchan~. We were done with everything, and I was looking out through the window. Even through the window, the light was so warm~… I wanted to stay like that forever, next to Shicchan."
mi "วันนั้นน่ะบรรยากาศดีม้าก~ มากเลยละฮิจัง~ เราทำงานกันเสร็จแล้วฉันก็นั่งมองหน้าต่างอยู่ แสงแดดน่ะอุ่นมากทั้งที่\nมีหน้าต่างคั่นอยู่แท้ ๆ ~… และฉันก็อยากอยู่ข้าง ๆ ชิจังอย่างนั้นไปตลอดกาลเลย"

# mi "But~! Then I looked at Shicchan, and she had her back to the window and was still working on something, blocking out the rest of the world. The light was on her shoulders, like when I would put a blanket on my shoulders as a little kid."
mi "แต่~! พอหันไปมองก็เห็นชิจังหันหลังให้หน้าต่างทำงานอะไรสักอย่างปิดกั้นตัวเองออกจากโลกรอบข้างอยู่ แดดส่อง\nไหล่ชิจังเหมือนผ้าห่มที่ฉันชอบเอามาคลุมไหล่ตอนเป็นเด็ก ๆ เลย"

# "Misha stops for a second as if trying to hold onto the image of Shizune in her mind."
"มิช่าหยุดไปแวบหนึ่งราวกับจะตรึงภาพของชิซูเนะในใจเธอให้เห็นแจ่มชัด"

# mi "Shicchan looked… hm~… It was like, Shicchan looked in a way that made me want to be with her… But it felt like it would be hard for that to happen."
mi "ชิจังดู… อืม~… ชิจังดูเป็นตัวของชิจังที่ทำให้ฉันอยากอยู่ด้วย… แต่ฉันก็รู้สึกว่าคงเป็นไปได้ยาก"

# mi "Wahaha~. That was~, a really~ long~ time ago. My hair was different back then, too. A little messy~? I cut it because Shicchan was always talking about it."
mi "วะฮ่าฮ่า~ เรื่องมันก็~ นาน~ มาแล้ว ผมฉันตอนนั้นไม่ได้เหมือนตอนนี้ด้วย ดูยุ่ง ๆ งี้~? ฉันตัดผมเพราะชิจังทัก\nตลอดเลย"

# mi "Anyway~! I told her, right then and there; I confessed~."
mi "แต่นั่นแหละ~! ฉันก็บอกเธอตรงนั้นเดี๋ยวนั้นเลย ฉันสารภาพรักไป~"

scene ev misha_roof_sad
with whiteout

# mi "I was rejected~."
mi "แล้วก็โดนปฏิเสธ~"

# mi "So~, I thought that that was it, Hicchan. But Shicchan was always trying to find me, and I hated Shicchan again for it. And when I asked her why she was doing it, it was because I was her friend."
mi "จากนั้น~ ฉันก็คิดว่าเรื่องคงจบแค่นั้นแหละฮิจัง แต่ชิจังน่ะคอยตามตัวฉันตลอดจนฉันไม่ชอบขึ้นมาอีกรอบ แล้วพอ\nถามว่าทำไมถึงทำอย่างนี้ ชิจังก็ตอบว่าเพราะฉันเป็นเพื่อน"

# "Her cheeks have a hint of red in them. I wonder how much experience she has had with crying, that she can keep herself from doing it so well. If she didn't pause to wipe her eyes, I might never have noticed."
"แก้มของเธอมีสีแดงเจืออยู่จาง ๆ เธอร้องไห้บ่อยขนาดไหนกันนะถึงได้กลั้นน้ำตาเก่งขนาดนี้ ถ้ามิช่าไม่พักเช็ดน้ำตา\nแล้วฉันก็คงไม่ทันสังเกตเห็นเลย"

scene ev misha_roof_closed
with charachange

# mi "Having Shicchan say that made me happy, but also sad, and even though she never meant to hurt me, it still hurts. Even now…"
mi "พอชิจังพูดอย่างนั้นแล้วฉันก็ดีใจ และเศร้าด้วย แล้วทั้งที่ชิจังไม่ได้จงใจทำร้ายฉัน แต่ฉันก็เจ็บ เจ็บมาจนถึงตอนนี้…"

# mi "Shicchan has a way of manipulating people, Hicchan. Sometimes she wants to, and sometimes she doesn't really, but it happens anyway~. And sometimes I'm just not sure… exactly which one it is. And I feel doubt…"
mi "ชิจังน่ะบงการคนเป็นนะฮิจัง บางครั้งเธอก็จงใจทำ หรือบางครั้งก็ไม่ได้จงใจหรอก แต่มันก็เป็นอย่างนั้นไป~ หรือ\nบางครั้งฉันก็ไม่แน่ใจด้วยซ้ำว่าจงใจ… หรือเปล่า จนฉันนึกสงสัย…"

# mi "I just wish that Shicchan liked me instead of you. It made me wonder if I was starting to hate you and Shicchan… just a little. I… didn't like that."
mi "ฉันแค่อยากให้ชิจังหันมาชอบฉันแทนนาย จนฉันสงสัยว่าหรือฉันเกลียดนายกับชิจังอยู่… หน่อย ๆ ซึ่งฉัน… ไม่ชอบ\nความรู้สึกนั้นเลย"

# hi "So you were thinking, maybe it would be better if I weren't here at all?"
hi "เธอก็เลยคิดว่าถ้าไม่มีฉันอยู่คงดีกว่านี้?"

scene ev misha_roof_normal
with charachange

# "She looks confused. The thought has never crossed her mind."
"เธอดูสับสนเพราะคงไม่เคยคิดอย่างนั้นมาก่อนเลย"

# mi "That's not it, Hicchan."
mi "ไม่ใช่อย่างนั้นสักหน่อยฮิจัง"

scene ev misha_roof_sad
with charachange

# mi "I thought about it a lot these last few days, and I don't want to hate anyone. You, or Shicchan. It's so stupid that I ever felt like that, isn't it, Hicchan? I don't want to think about that kind of stuff ever again."
mi "ช่วงสองสามวันมานี้น่ะฉันเอาแต่คิดเรื่องนั้นไม่ไปไหนเลย แล้วฉันก็ไม่อยากเกลียดใครด้วย ไม่ว่าจะนายหรือชิจัง งี่เง่า\nใช่มั้ยล่ะฮิจังที่ฉันรู้สึกอย่างนั้นน่ะ ฉันไม่อยากคิดเรื่องอะไรพวกนั้นอีกแล้ว"

# mi "And missing people, and being apart from them; I'm tired of it, and don't want to think about it any more."
mi "ไม่อยากคิดถึงใคร ไม่อยากแยกจากใคร ฉันเหนื่อยแล้ว ฉันไม่อยากคิดแล้ว"

# mi "I already did, though. So~! …I'm still really the worst kind of person. I wasn't thinking that it would be better if Hicchan had never come to this school.
# I was thinking… wouldn't it be better if I just died?"
mi "แต่ฉันก็คิดไปแล้ว เพราะงั้น~! …ฉันก็ยังเป็นคนที่แย่ที่สุดในโลก ฉันไม่ได้คิดเรื่องที่จะเกิดถ้าฮิจังไม่มาโรงเรียนนี้หรอกนะ\nแต่ฉันคิดว่า… ถ้าฉันตาย ๆ ไปเลยก็คงดีเสียกว่า"


#bad end
label th_S29xa:

#next line is only if you had sex with misha
scene ev misha_roof_closed
with charachange

# mi "After all, I've even done something really terrible, now. Unforgivably terrible."
mi "เพราะยังไงฉันก็ทำอะไรที่เลวร้ายมาก ๆ ลงไปแล้วนี่นา เลวร้ายมากจนไม่น่าให้อภัย"

# "Misha presses herself harder against the fence at her back, as if hoping to slip right through it."
"มิช่าแนบหลังตัวเองเข้ากับรั้วที่กั้นอยู่ราวกับอยากจะลอดตัวผ่านออกไปให้ได้"

# hi "Don't be stupid."
hi "พูดอะไรโง่ ๆ"

# "I'm surprised by the tone of my voice."
"ฉันตกใจกับน้ำเสียงตัวเอง"

# hi "Sorry."
hi "ขอโทษ"

# hi "I realized, I hate it when I'm left feeling regretful, over anything. Even so, it's impossible for me to not end up regretting something."
hi "ฉันเพิ่งนึกได้ว่าฉันเกลียดความรู้สึกเวลาต้องมาเสียใจเรื่องในอดีต จะเป็นเรื่องอะไรก็ช่างเถอะ แต่ถึงอย่างนั้น สุดท้าย\nฉันก็อดไม่ได้ที่จะเสียใจกับอะไรสักอย่างอยู่ดี"

# hi "Yesterday, I did a stupid thing. That's probably part of the reason why I'm here right now, so I could figure out if I could maybe… make it right, somehow."
hi "เมื่อวานฉันทำอะไรโง่ ๆ ลงไปแล้ว ส่วนหนึ่งที่ขึ้นมาดาดฟ้านี่ก็คงเพราะเรื่องนั้นมั้ง จะได้มาคิดว่า… ยังพอมีทางแก้ไข\nอยู่หรือเปล่า"

# hi "Do you ever feel that way? You said you've done some terrible things. You can try fixing them."
hi "เธอเคยรู้สึกอย่างนั้นมั้ย เธอบอกว่าเธอทำอะไรแย่ ๆ ลงไป ลองแก้ไขดูก็ได้นะ"

scene ev misha_roof_normal
with charachange

# mi "Hicchan~, isn't that…"
mi "ฮิจัง~ นั่นมัน…"

# "I know that she's thinking that I'm saying this more for me than for her."
"ฉันรู้ว่าเธอคิดว่าที่ฉันพูดอย่างนี้คือบอกตัวเองมากกว่า"

# hi "No. It's not."
hi "ไม่ ไม่ใช่อย่างนั้น"

# hi "I just think that killing yourself is the biggest regret a person could end up with."
hi "ฉันแค่คิดว่าการฆ่าตัวตายน่ะคือความเสียใจขั้นสุดในชีวิตของคนคนหนึ่งเลย"

mi "…"

# mi "Hicchan, you're so dramatic."
mi "ฮิจัง นายนี่เวอร์จัง"

scene ev misha_roof_closed
with charachange

# "Whether she was serious, I'll never know. I don't try to find out; as she lets out a sigh and closes her eyes as if going to sleep, I feel that the dangerous mood I was picking up from her has passed."
"ฉันไม่อาจรู้ได้ว่าเธอพูดเล่นหรือพูดจริง ฉันไม่สนใจจะคิดต่อ เธอถอนหายใจแล้วหลับตาลงคล้ายจะหลับ สัญญาณ\nอันตรายที่ฉันจับได้จากเธอเมื่อครู่นั้นหายไปแล้ว"


#good end
label th_S29xb:

stop music fadeout 0.5
$ renpy.music.set_volume(0.0, 0.5, channel="ambient")

# "Misha presses herself harder against the fence at her back, as if hoping to slip right through it."
"มิช่าแนบหลังตัวเองเข้ากับรั้วที่กั้นอยู่ราวกับอยากจะลอดตัวผ่านออกไปให้ได้"

scene bg school_roof_ss
show mishashort perky_confused_close_ss at center
with vpunch

$ renpy.music.set_volume(1.0, 6.0, channel="ambient")

# "Without really thinking about it, I grab her hand. My reflexes are terrible, and I manage to only grasp onto a few of her fingers, but it's unimportant."
"ฉันคว้ามือเธอเอาไว้ก่อน การตอบสนองทางกายของฉันนั้นย่ำแย่ ที่ฉันคว้าได้ก็มีเพียงนิ้วของเธอไม่กี่นิ้ว แต่เรื่องนั้น\nไม่สำคัญ"

play music music_rain fadein 6.0

# hi "Sorry. It's just that you said something pretty weird just now."
hi "ขอโทษที พอดีเห็นเมื่อกี้เธอพูดอะไรแปลก ๆ น่ะ"

show mishashort perky_sad_close_ss
with charachange

# mi "Hahaha~. Yeah~, I guess that's right, Hicchan."
mi "ฮ่าฮ่าฮ่า~ อื้ม~ ก็คงงั้นแหละนะฮิจัง"

# hi "Yeah."
hi "อื้ม"

# hi "Do you want to know what I think?"
hi "อยากรู้มั้ยว่าฉันคิดอะไรอยู่"

# hi "Shizune is the type of person who won't let anyone close to her except on her terms. It's frustrating, sometimes it's even infuriating."
hi "ชิซูเนะน่ะเป็นพวกที่จะไม่ให้ใครได้เข้าใกล้ ยกเว้นจะมีข้อตกลงบางอย่าง ซึ่งก็น่าหงุดหงิดนะ บางทีก็น่าโมโหด้วยซ้ำ"

# hi "That probably would have bothered me, when I was in the hospital and anyone who shut me out was dead to me. I'd forgotten all about it until recently. I got a letter, and it was all about that."
hi "ก็คงเพราะอย่างนั้นฉันถึงได้รำคาญ ตอนที่ฉันอยู่ที่โรงพยาบาลน่ะ ในสายตาฉัน คนที่ตีตัวออกหากจากฉันไปน่ะ\nก็ไม่ต่างอะไรกับคนที่ตายไปแล้ว ก่อนหน้านั้นฉันก็ลืม ๆ ไปหมดแล้ว จนกระทั่งตอนที่มีจดหมายส่งมาฉันถึงนึกได้\nเนื้อหาข้างในก็พูดถึงเรื่องพวกนั้นนั่นแหละ"

# hi "I was mad. I thought, “How can you accuse me of closing myself off from everyone and giving up? Isn't that what everyone else did to me? What else am I supposed to do? What can I do?”"
hi "ฉันโมโห ในใจก็คิด “มาหาว่าฉันยอมแพ้ปิดกั้นตัวเองออกจากคนอื่นได้ยังไง ทุกคนก็ทำอย่างนั้นใส่ฉันนี่ แล้วจะ\nให้ฉันทำยังไง ฉันจะทำอะไรได้”"

# hi "Yeah, even now, I know that's how it happened, but… she was right, too. I did close myself off."
hi "อืม จนตอนนี้ฉันก็ยังเชื่ออยู่ว่าเรื่องมันเป็นอย่างที่คิดนั่นแหละ แต่ว่า… เขาก็พูดถูกเหมือนกันว่าฉันปิดกั้นตัวเอง"

# hi "So, I made up my mind that I'm not going to let that be the case ever again."
hi "ฉันเลยตั้งใจว่าจะไม่ให้เรื่องแบบนั้นเกิดขึ้นซ้ำสองอีก"

show mishashort perky_confused_close_ss
with charachange

#if seen A26b:
label th_S29xba:

# mi "The hospital? Hicchan… is that what those pills are for?"
mi "โรงพยาบาลเหรอ ฮิจัง… หรือว่ายาพวกนั้น?"

#if not seen A26b:
label th_S29xbb:

# mi "The hospital? Hicchan… what are you…"
mi "โรงพยาบาลเหรอ ฮิจัง… นี่นาย…"

#end split
label th_S29xbc:

# hi "Just listen, please."
hi "ฟังก่อนนะ"

# hi "Shizune is the opposite of how I was. She has always wanted to draw people closer to her. That's the only reason Shizune was interested in me in the first place, I think. And I think I was determined to not let that happen, in a way."
hi "ส่วนชิซูเนะเป็นคนละอย่างกับฉันเลย เธออยากจะดึงให้คนได้มาเข้าใกล้เธอ ฉันว่าแรกเริ่มเดิมทีที่ชิซูเนะสนใจฉันก็คง\nเพราะแค่นั้นแหละ แล้ว ในแง่หนึ่ง จะว่าตอนนั้นฉันตั้งเป้าว่าจะไม่ให้ตัวเองถูกลากไปก็ว่าได้"

# "Misha casts her eyes downwards, understanding perfectly."
"มิช่าหลุบมองต่ำรับฟังด้วยความเข้าใจ"

# hi "I never realized how hard that can be."
hi "ฉันไม่เคยรู้เลยว่าการจะทำอย่างนั้นมันลำบากแค่ไหน"

# hi "And now, I feel like I'm going to return the favor, even if it takes twice as long. I already learned a second language just to get this far."
hi "แล้วตอนนี้ฉันก็รู้สึกว่าต้องตอบแทนเธออะไรสักหน่อย ต่อให้จะต้องใช้เวลานานกว่านั้นเป็นสองเท่าตัวเลยก็เถอะ\nเพราะขนาดว่าเรียนภาษาที่สองไปแล้วยังมาได้เท่านี้เลย"

# hi "It wasn't as hard as I thought, but it was definitely hard. Sometimes, I felt like I was clawing my way up a mountain, with how my hands hurt."
hi "ก็ไม่ได้ยากอย่างที่คิดหรอก แต่ก็ยากอยู่ บางครั้งก็เจ็บมือจนนึกว่าไปปีนเขามา"

# hi "And you did the same thing. And it was for the same reason, wasn't it? That's really amazing. Which is why it makes me sad, and a little angry, that you would say a stupid thing like that."
hi "แล้วเธอก็ทำเหมือนกัน แล้วก็ด้วยเหตุผลอย่างเดียวกันด้วยนี่ ใช่มั้ย สุดยอดไปเลยนะ เพราะงั้นฉันถึงได้เศร้ากับโกรธ\nหน่อย ๆ ที่เธอพูดอะไรโง่ ๆ อย่างนั้น"


mi "…"

# hi "That's just what I believe, anyway."
hi "แต่ยังไงที่ฉันว่าไปมันก็แค่ความคิดของฉันน่ะนะ"

show mishashort perky_sad_close_ss
with charachange

# "Her shoulders slump, and Misha almost slides to the floor, like she is drained of all energy."
"เธอหย่อนไหล่ลงจนตัวแทบไหลลงไปกับพื้นราวกับหมดแรง"

# mi "You're too dramatic, Hicchan."
mi "นายก็เวอร์ไปนะฮิจัง"

# "She says, while looking away, turning her head almost as if she wants to look out at the school grounds, but not turning it enough to do so."
"เธอพูดพลางเบือนหน้าหนีเหมือนอยากหันไปมองลานหน้าโรงเรียน แต่ก็ยังเอี้ยวคอไม่พอที่จะหันไปมองจริง ๆ"

# mi "Wahaha~."
mi "วะฮ่าฮ่า~"


#end split
label th_S29y:

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

scene bg school_roof_ss
show mishashort perky_confused_close_ss at center
with locationchange

stop music fadeout 0.5
$ renpy.music.set_volume(0.2, 0.0, channel="sound")
play sound sfx_door_creak

# "The door behind us opens, the sound only barely able to be heard over the ambient breeze."
"เสียงของประตูด้านหลังพวกเราที่เปิดออกนั้นแว่วมาอย่างแผ่วเบาตามสายลมเอื่อย"

scene bg school_roof_ss at bgleft
show mishashort perky_confused_close_ss at closeleft
with charamove

show shizu behind_blank_ss at tworight
with charaenter

# ssh "I've been looking everywhere for you two. Is this some secret meeting?"
ssh "ฉันไปตามหาเธอสองคนทั่วโรงเรียนเลยแน่ะ ประชุมลับกันอยู่หรืออะไร"

# "She walks over to us, leaning against the fence next to Misha as if she needs to stop and catch her breath, before pushing herself off it and continuing."
"เธอเดินเข้ามาแล้วพิงเข้ากับรั้วข้าง ๆ มิช่าราวกับจะพักหายใจก่อนจะเด้งตัวกลับมาแล้วคุยต่อ"

show shizu basic_normal_ss
with charachange

# ssh "I'm bored sitting in the student council room every day now, without either of you ever coming by. Taking some time off is fine, but this is just too much."
ssh "ฉันเบื่อการนั่งอยู่ในห้องสภานักเรียนทุกวันอยู่ตัวคนเดียวแล้ว พวกเธอสองคนไม่เคยแวะมาเลย พักบ้างน่ะไม่เป็นไร\nแต่นี่ก็พักบ่อยไป"

# "Normally, Misha and I would be jokingly making excuses for ourselves at this point. This time, there's only silence. Shizune, always expecting resistance, is thrown off balance by the lack of it."
"ปกติมิช่ากับฉันจะต้องหาอะไรมาเถียงข้าง ๆ คู ๆ ไปแล้ว แต่คราวนี้มีเพียงแต่ความเงียบ ชิซูเนะที่ตั้งท่ารอเสียงประท้วง\nอย่างเคยก็ตั้งตัวไม่ถูกเมื่อเจอกับความเงียบนี้"

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_snap
show shizu adjust_happy_ss
with Dissolve(0.3)

# "A few seconds pass in uneasy silence, which Shizune breaks with an ear-shattering snap of her fingers, smiling as if to say “eureka.”"
"ความเงียบอันน่าอึดอัดกินเวลาอยู่สองสามวินาที ชิซูเนะดีดนิ้วดังจนแสบแก้วหูเพื่อทำลายความเงียบนี้แล้วยิ้มราวกับ\nจะกล่าวคำว่า “ยูเรก้า”"

show shizu basic_happy_ss
with charachange

# ssh "Let's go do something together."
ssh "ไปหาอะไรทำกันเถอะ"

# hi "Like what?"
hi "เช่นอะไร"

show shizu behind_smile_ss
with charachange

# ssh "Anything! We should go to the student council room first, and then figure it out from there."
ssh "อะไรก็ได้! ไปห้องสภานักเรียนกันก่อนแล้วค่อยคิดว่าจะเอายังไงต่อก็ได้"

# hi "That seems like a trick to get us to do work instead."
hi "นี่หลอกให้ไปทำงานหรือเปล่าเนี่ย"

show shizu basic_normal2_ss
with charachange

# ssh "Very funny."
ssh "ตลกมาก"


#bad end
label th_S29ya:

show shizu behind_smile_ss
with charachange

# ssh "It's not a trick. I promise. It will be something fun."
ssh "ไม่ได้หลอกนะ ฉันสัญญา สนุกแน่นอน"

show mishashort perky_sad_close_ss
with charachange

play music music_rain fadein 4.0

# "Misha contrasts the genial smile on Shizune's face with a lonely expression of her own."
"มิช่าทำหน้าอ้างว้างขัดกับรอยยิ้มเป็นมิตรของชิซูเนะ"

# "If Misha is really jealous of me for stealing Shizune away from her, then it'd only make it worse if all three of us were together. I imagine it'd be like rubbing salt in an open wound. So I get the idea to let them spend time together."
"ถ้ามิช่าอิจฉาที่ฉันแย่งชิซูเนะไปจากเธอจริง งั้นการที่เราสามคนอยู่ด้วยกันจะยิ่งแย่ไปใหญ่เพราะเหมือนเข้าไปซ้ำเติมอีก\nฉันจึงคิดได้ว่าควรให้สองคนนั้นได้ใช้เวลาอยู่ด้วยกัน"

# "I'm not so idealistic that I think a single afternoon to themselves will solve everything, but it might help. It seems like the better option than going with them, because my presence definitely wouldn't help at all."
"ฉันก็ไม่ได้คิดบวกถึงขั้นที่คาดหวังว่าแค่เวลาช่วงบ่ายวันเดียวจะแก้ไขปัญหาทุกอย่างได้ แต่ก็คงพอช่วยได้บ้างแหละ\nแล้วก็คงดีกว่าการที่ฉันไปอยู่ด้วย เพราะอยู่ไปก็คงไม่มีอะไรดีขึ้นแน่ ๆ"

# hi "You two can go have fun, then. I'm going to go to bed early."
hi "งั้นก็ไปสนุกกันสองคนเลย วันนี้ฉันนอนละ"

show shizu basic_normal_ss
with charachange

# ssh "Are you sure? It's barely past lunch."
ssh "แน่ใจนะ เพิ่งพักเที่ยงมาได้ไม่นานเอง"

# hi "I told you, I don't feel too good today. I think I'm coming down with something."
hi "บอกแล้วไงว่าวันนี้ฉันไม่ค่อยสบาย เหมือนจะเป็นอะไรสักอย่าง"

show shizu adjust_frown_ss
with charachange

# ssh "I thought that you said excuses like that won't work."
ssh "ไหนบอกว่าข้ออ้างแบบนั้นไม่มีใครเชื่อไง"

# "She has me there."
"ไปต่อไม่ถูกเลยทีนี้"

show shizu basic_normal2_ss
with charachange

# ssh "It's okay. But refusing someone's invitation is rude. I'll expect you to make it up to me."
ssh "ไม่เป็นไรหรอก แต่การปฏิเสธเวลามีคนชวนน่ะหยาบคายนะ หวังว่าคราวหน้าจะมาแก้ตัวนะ"

show shizu adjust_happy_ss
with charachange

# "Shizune turns around and smiles at Misha, and starts signing something that I can't see. I assume it's along the lines of “it looks like it's just going to be the two of us.”"
"ชิซูเนะหันไปยิ้มให้มิช่าแล้วทำภาษามืออะไรสักอย่างที่ฉันไม่เห็น คงจะประมาณว่า “ดูท่าว่าจะได้อยู่ด้วยกันแค่สองเรา\nแล้วละ”"

stop music fadeout 3.0

# "That's good."
"ดีแล้ว"

stop ambient fadeout 2.0

window hide


#good end
label th_S29yb:

show mishashort hips_grin_close_ss
with charachange

play music music_comfort fadein 5.0

# "Misha laughs, managing to let out a restrained “wahaha.” That Shizune can't see it makes me feel better. It means that it wasn't only for her benefit."
"มิช่าหัวเราะ “วะฮ่าฮ่า” แบบกลั้นเอาไว้ ฉันรู้สึกโล่งใจที่เธอไม่ได้หัวเราะเพราะแค่อยากให้ชิซูเนะสบายใจขึ้น ดูได้จาก\nการที่เธอไม่ได้หัวเราะให้ชิซูเนะเห็น"

show shizu behind_smile_ss
with charachange

# ssh "I was thinking that you both actually could help me with something. What else is there? We can't go out to eat. We already ordered in yesterday, and that was already breaking policy. Three days in a row would be unforgivable."
ssh "ก็คิดอยู่ว่าพวกเธออาจจะพอช่วยงานอะไรฉันได้ จะให้เป็นอะไรไปได้อีก จะไปกินข้าวข้างนอกก็ไม่ได้เพราะเพิ่งสั่งข้าว\nมากินเมื่อวาน ซึ่งที่สั่งข้าวเมื่อวานก็เป็นการแหกกฎแล้ว ครั้งที่สามนี่ไม่ควร"

show mishashort perky_smile_close_ss
with charachange

# mi "But~! That was ordering in, Shicchan~! Going out to eat is different."
mi "แต่~! เมื่อวานมันสั่งข้าวมากินที่นี่นะชิจัง~! ไม่เหมือนการกินข้าวที่ข้างนอกสักหน่อย"

# hi "Yeah, totally different."
hi "ใช่ ไม่เหมือนกันเลย"

show shizu adjust_frown_ss
with charachange

# ssh "You're both kidding yourselves."
ssh "นี่พวกเธอกำลังหลอกตัวเองกันอยู่นะ"

show shizu basic_normal_close_ss at closeright
with characlose

# "Before I can reply, Shizune grabs my hand, limiting my ability to do so. My options cut down so drastically, I have no choice but to settle for making a face at her instead. She makes one back, before extending her hand to Misha as well."
"ชิซูเนะจับมือฉันก่อนที่จะทันได้ตอบจนฉันตอบไม่ได้ ทางเลือกเหลือเพียงน้อยนิด เอาเป็นว่าทำหน้าส่งสัญญาณ\nไปแล้วกัน เธอก็ทำหน้าตอบกลับมาก่อนจะยื่นมือไปรอจับมือมิช่าด้วย"

# "When Misha is reluctant to take it, I walk forward as far as holding onto Shizune at the same time will allow me, and take her hand myself."
"มิช่าดูยังไม่เต็มใจอยากจับ แต่ฉันอาจหาญจับมือชิซูเนะตอบและใช้จังหวะนั้นใช้มือข้างที่ว่างเข้าไปจับมือมิช่า\nไว้เสียเอง"

show mishashort hips_smile_close_ss
with charachange

# mi "…Hahaha."
mi "…ฮ่าฮ่าฮ่า"

# "She only has a second to smile before Shizune starts pulling us impatiently towards the door, binding us together, like a human chain."
"มิช่ายิ้มอยู่ได้วินาทีเดียวก็ถูกชิซูเนะลากไปทางประตู พวกเราถูกลากกันไปราวโซ่มนุษย์"

stop ambient fadeout 1.0

scene ev shizu_hands
with locationskip

# "Although it's dangerous, none of us seem to think of letting go any step of the way through the school, out of the doors, and across the grounds."
"ถึงจะอันตราย แต่ก็เหมือนไม่มีใครคิดจะปล่อยมือไปตลอดทางที่เดินผ่านตัวอาคารออกมายังลานหน้าโรงเรียน"

# "This feels familiar, as if we've walked like this before. The three of us, hand in hand. Of course, the mood was a lot happier then."
"เป็นความรู้สึกที่คุ้นเคยราวกับว่าพวกเราสามคนเคยเดินจับมือกันอย่างนี้มาก่อน แต่แน่นอนว่าตอนนั้นมีความสุข\nกว่าเวลานี้มาก"

# "I can see the lingering sadness on their faces, and it makes me wonder if anything has really changed. If this is all just a distraction or not. But I think it's just me slipping back into being cynical because of the moment. It's a start."
"ฉันเห็นความเศร้าที่เจืออยู่ในสีหน้าของทั้งสองคนจนนึกสงสัยว่ามีอะไรเปลี่ยนไปแล้วจริงหรือเปล่า หรือทั้งหมดนี้\nเป็นการหาเรื่องเบนความสนใจไปทางอื่น แต่ก็คงเป็นแค่ความหวาดระแวงของฉันที่ชอบโผล่มาตอนเรื่องเป็นอย่างนี้\nนั่นแหละ นี่แหละคือจุดเริ่มต้น"

stop music fadeout 3.0

window hide
return