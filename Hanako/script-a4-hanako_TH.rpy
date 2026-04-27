label th_H21:

scene bg school_scienceroom
with locationchange

play music music_normal fadein 3.0

# "I woke up, took my pills, had a nice shower, quickly slipped on my uniform, ate a tasty breakfast, grabbed my bag, and headed off, all as per my usual daily routine."
"ฉันตื่นมากินยา อาบน้ำให้สดชื่น สวมชุดนักเรียน กินมื้อเช้าอร่อย ๆ คว้ากระเป๋าเดินไปเรียนตามปกติที่ทำเป็นกิจวัตร\nประจำวัน"

# "It was only after arriving in class that the normality of the day was thrown off."
"พอมาถึงห้องแล้วก็พบกับสิ่งที่ทำให้ความปกตินั้นหายไป"

# "After taking my seat, I watched my classmates trickle into the room over the next hour, until every empty seat was eventually taken, other than Hanako's."
"ฉันนั่งกับที่มองเพื่อนร่วมชั้นเรียนทยอยเข้าห้องมาอยู่ราวหนึ่งชั่วโมงจนกระทั่งทุกที่นั่งที่ว่างอยู่นั้นมีคนนั่งจนเต็ม\nเว้นก็แต่ที่โต๊ะฮานาโกะ"

stop music fadeout 10.0

$ ksgallery_unlock("evul hanako_emptyclassroom")
scene evbg hanako_emptyclassroom:
    truecenter
    subpixel True zoom 0.9
    easein 20.0 zoom 1.0
show evfg hanako_emptyclassroom:
    truecenter
    subpixel True zoom 0.8
    easein 20.0 zoom 1.0
with whiteout

# "I can never get used to the idea that she just doesn't show up to class every now and again. It feels all the more worrying now as well, given that Lilly's left."
"ฉันทำใจให้ชินกับการที่ฮานาโกะขาดเรียนไปบ้างเป็นบางครั้งไม่ได้เลย และยิ่งตอนนี้ลิลลี่ไม่อยู่ด้วยแล้วก็ยิ่ง\nชวนให้กังวลไปใหญ่"

# "As Mutou continues to drone on, I find my gaze flicking every so often over to her seat, as if she might appear there any moment now. Nobody else seems to care at all about her absence, but they have little reason to."
"ระหว่างที่ครูสอนไปเอื่อย ๆ เรื่อย ๆ สายตาฉันก็เหล่มองไปที่โต๊ะฮานาโกะอยู่บ่อย ๆ ราวกับว่าเธออาจปรากฏตัวขึ้น\nณ ขณะนั้นเลยก็ได้ ไม่มีใครดูจะสนใจที่เธอขาดไปมากนัก ซึ่งก็เพราะไม่มีความจำเป็นต้องสนใจนั่นแหละ"

# "Hanako being absent from class, after all, is perfectly normal. Or at least, it was. Her attendance hasn't been all that bad from what I've seen in my time here, but it was apparently much more spotty beforehand."
"เพราะยังไงเสียการที่ฮานาโกะขาดเรียนนั้นเป็น—หรืออย่างน้อย ๆ ก็เคยเป็น—เรื่องปกติสามัญ ตั้งแต่ที่ฉันมาเรียน\nก็เห็นเธอขาดเรียนไม่บ่อยขนาดนั้น แต่เหมือนว่าก่อนหน้านี้จะหายไปบ่อยกว่า"

# "This is also an ominous time for her to be gone. It's the day before her birthday, and my suspicions are starting to rise, after the breakdown she had in class when it was mentioned."
"และการที่ฮานาโกะหายไปตอนนี้นั้นก็ไม่ใช่สัญญาณที่ดีด้วย เป็นวันก่อนถึงวันเกิดฮานาโกะ และฉันก็ยิ่งกังขา\nหนักขึ้นไปอีกหลังจากที่เธอแพนิกในห้องตอนพูดถึงเรื่องวันเกิด"

# "An increasing amount of my thoughts is taken up by how I can help her, but in the end, I feel like I can't do anything."
"ฉันคิดหาทางช่วยฮานาโกะจนเรื่องนั้นกินพื้นที่สมองมากขึ้นไปเรื่อย ๆ แต่สุดท้ายก็รู้สึกว่าตัวเองทำอะไรไม่ได้เลย"

scene bg school_scienceroom
with silentwhiteout
play sound sfx_normalbell

# "The bell heralding the beginning of lunchtime rings out, shaking me out of my thoughts. A collective sigh of relief can be heard from the class, though Mutou looks quite put off."
"ระฆังซึ่งป่าวร้องถึงเวลาเริ่มพักเที่ยงดังขึ้นดึงสติให้ฉันหลุดจากห้วงความคิด ฉันได้ยินเสียงคนทั้งห้องที่ถอนหายใจ\nเป็นเชิงโล่งอกพร้อม ๆ กัน แต่ครูดูจะหงุดหงิดอยู่บ้าง"

# "He dislikes being interrupted in the middle of his exciting lectures, after all."
"ครูไม่ชอบให้อะไรมารบกวนการสอนสุดตื่นเต้นของตัวเองนี่นะ"

# "Just when I'm wondering what I should do on lunch break, given that Hanako and Lilly aren't here, the solution presents itself."
"จังหวะที่กำลังคิดอยู่ว่าพักเที่ยงนี้จะทำอะไรดีเพราะฮานาโกะกับลิลลี่ไม่อยู่ด้วยแล้วนั้นคำตอบก็ปรากฏกาย"

show shizu invis:
    tworight
    xpos 0.8
show misha invis:
    twoleft
    xpos 0.2
with None

show shizu behind_blank at tworight
show misha hips_grin at twoleft
with dissolvecharamove

play music music_shizune fadein 5.0

# mi "'Afternoon, Hicchan~!"
mi "ทิวาหวัดฮิจัง~!"

show shizu adjust_happy
with charachange

shi "…"

# hi "'Afternoon Misha, Shizune. You both look as bright as ever."
hi "ทิวาหวัดมิช่า ชิซูเนะ ดูสดใสเช่นเคยเลยนะ"

show shizu basic_normal2
with charachange

shi "…"

show misha sign_smile
with charachange

# mi "Shicchan wants to know if you'd like to have lunch with us today~?"
mi "ชิจังถามว่าวันนี้นายอยากไปกินข้าวเที่ยงด้วยกันกับพวกเราไหม~"

# hi "Sure. It'll be good to have some company."
hi "ได้ มีเพื่อนกินก็ดีเหมือนกัน"

scene bg school_cafeteria
show crowd
with locationskip

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 1.0

# "The cafeteria hums with activity, much like my old school's did. Yamaku is different, though, in how… strangely civilized the lunchtime rush is."
"โรงอาหารนั้นเต็มไปด้วยเสียงดังเซ็งแซ่เหมือนที่โรงเรียนเก่าฉัน แต่ยามากุนั้นต่างตรงที่… ฝูงชนยามพักเที่ยงนั้น\nดูมีอารยธรรมอย่างน่าประหลาด"

# "What one would expect to be an unruly mob chomping at the bit to get to the serving area is, rather, a neat and organized line."
"ภาพที่คิดว่าจะได้เห็นต้องเป็นคนที่ยกโขยงกรูกันเข้ามาให้ถึงบริเวณแจกจ่ายอาหาร ไม่ใช่คนที่ต่อแถวกัน\nอย่างเป็นระเบียบเรียบร้อยเช่นนี้"

# "There's a small amount of jostling, and people's heads are often craning around to check on what's happening up ahead, but it's pretty subdued."
"ถึงจะมีการเบียดเสียดบ้าง บางทีก็มีคนที่ชะเง้อชะแง้แลดูว่าข้างหน้ามีอะไร แต่เหล่านั้นก็ยังไม่ทำให้ดูวุ่นวายนัก"

# "This is due, no doubt, to the very serious rules regarding such matters in this school. The same strict discipline is observed when students move in the hallways, or come to and from their dormitories and the school gate."
"ซึ่งแน่แท้ว่าเป็นเพราะกฎของยามากุที่เอาจริงเอาจังกับเรื่องทำนองนี้ การยึดถือวินัยอย่างเคร่งครัดนี้ยังพบได้\nเวลาที่นักเรียนเดินตามโถงทางเดินหรือจากหอไปยังประตูหน้าโรงเรียน"

# "While the reasons for it may be slightly off-putting, I've come to quite like this sense of order that's enforced in the school."
"เหตุผลอาจจะฟังดูแปลกเล็กน้อย แต่ฉันก็เริ่มชอบความมีระเบียบที่โรงเรียนนี้ใช้แล้ว"

show shizu behind_smile:
    tworight
    ypos 1.1
show misha perky_smile:
    twoleft
    ypos 1.1
with charaenter

hide crowd
with charaexit

$ renpy.music.set_volume(0.4, 7.0, channel="ambient")

# "I didn't really like being told by Shizune and Misha to get their lunches, though. I feel a little used as I take a seat at the table where they're sitting, plunking their food down in front of them."
"แต่ฉันไม่ชอบกับการโดนชิซูเนะกับมิช่าสั่งให้มาเอาข้าวเที่ยงเลยอะนะ ฉันนั่งลงตรงโต๊ะที่ทั้งสองคนนั่งอยู่\nพร้อมความรู้สึกเหมือนโดนใช้หน่อย ๆ ก่อนจะวางถาดอาหารของแต่ละคนให้ตรงหน้าเสียงดังปึก"

# "Sweet bread and strawberry milk for Misha, a bowl of ramen and juice for Shizune. I heave a sigh of relief as I put it all down, after the significant difficulty I had carrying it all in addition to my own lunch."
"ขนมปังหวานกับนมรสสตรอว์เบอร์รีของมิช่า ราเมงหนึ่งชามกับน้ำผลไม้ของชิซูเนะ เมื่อวางแล้วฉันก็ถอนหายใจ\nเฮือกใหญ่เพราะกว่าจะขนทั้งหมดนี่รวมทั้งอาหารของตัวเองด้วยได้นั้นเล่นเอาลำบากมาก"

show misha hips_grin
with charachange

# mi "Thank you~!"
mi "ขอบคุณนะ~!"

show shizu behind_smile
with charachange

# "Misha claps her hands together before popping open the wrapper and digging into her bread ravenously. Shizune simply gives an appreciative nod before giving her steaming ramen a stir and blowing on it a little to cool it down."
"มิช่าตบมือแล้วแกะห่อขนมและกินขนมปังอย่างหิวโหย ส่วนชิซูเนะเพียงพยักหน้าเป็นเชิงขอบคุณก่อนจะ\nคนราเมงในชามแล้วเป่าเบา ๆ ให้เย็นลง"

# "I open my own lunch, another packet of sweet bread, and take a bite before washing it down with some juice. The bread is very sweet, so much so that I end up forcing myself to stomach it just to get the experience over with."
"ฉันแกะของกินของตัวเองบ้างซึ่งเป็นขนมปังหวานเช่นกันแล้วกินหนึ่งคำและตามด้วยน้ำผลไม้ ขนมปังนั้นหวานมาก\nจนฉันต้องฝืนกินให้รีบหมด ๆ ไป"

# "Midway through, I decide to take a break from the difficult task and ask what's on my mind."
"แต่กินไปได้สักพักฉันก็พักจากการฝืนอันยากเย็นนั้นแล้วถามสิ่งที่คาใจอยู่"

# hi "So, I'm guessing you two had a reason to drag me down here? You two seem to always have an ulterior motive, after all."
hi "แล้วที่ลากฉันมานี่มีเหตุผลอะไรอยู่ใช่ไหม ปกติเธอสองคนทำอะไรแล้วชอบมีเจตนาแอบแฝงตลอด"

show misha sign_confused
with charachange

# mi "What are you faying, Hiffan~! We mon't hafe any uffer mofiffe~."
mi "อู้ดอาไออะอิ๊อัง~! เอาไอ่อีเอดอะอาแอบแอ๋งซู้กอ่อย~"

show shizu basic_angry
with charachange

# "Her mouth is full of sweet bread as she speaks. It's a pretty unpleasant sight. Shizune looks a little grossed out, before going back to eating her ramen."
"ปากมิช่าตอนพูดนั้นอัดแน่นไปด้วยขนมปังหวาน เป็นภาพที่ไม่น่ามองเลย ชิซูเนะทำหน้าขยะแขยงเล็กน้อย\nก่อนจะหันไปกินราเมงต่อ"

show shizu basic_normal
show misha perky_smile
with charachange

# "I wait until Misha swallows what she has in her mouth before speaking again."
"ฉันรอให้มิช่ากลืนอะไรก็ตามที่อยู่ในปากนั้นจนหมดก่อนค่อยพูดอีกรอบ"

# hi "You're not buttering me up to make me work with you after school?"
hi "เธอไม่ได้เอาใจฉันเพื่อที่จะได้ให้ฉันไปช่วยงานพวกเธอตอนเลิกเรียนใช่ไหม"

show misha hips_smile
with charachange

# mi "Nope!"
mi "ไม่!"

# hi "Not trying to extract information from me that I might not want to give?"
hi "ไม่ได้จะรีดเค้นข้อมูลอะไรที่ฉันไม่อยากบอก?"

show misha cross_smile
with charachange

# mi "Nuh-uh!"
mi "ม่ายช่าย!"

# hi "…Fine. You win. I guess you just wanted to eat lunch with someone as intelligent and handsome as me, then."
hi "…เออ ยอม งั้นก็คงแค่อยากมากินข้าวเที่ยงด้วยกันกับคนที่ทั้งหล่อทั้งหัวดีอย่างฉันสินะ"

show misha cross_grin
with charachange

# mi "That's it, Hicchan~! You got it~!"
mi "ใช่แล้วฮิจัง~! ตามนั้นเลย~!"

# "Shizune looks unimpressed as Misha finishes signing our conversation, and sucks in the last of a long noodle as she signs her own thoughts."
"ชิซูเนะดูจะไม่ปลื้มกับบทสนทนาของเราเมื่อได้เห็นที่มิช่าแปลให้แล้ว เธอกินเส้นราเมงยาว ๆ ที่อยู่ในปากให้หมด\nแล้วส่งภาษามือบ้าง"

show shizu behind_blank
with charachange

shi "…"

show misha sign_smile
with charachange

# mi "Shicchan says you shouldn't be so suspicious of us~. She's just doing her duty as a class representative, after all~."
mi "ชิจังบอกว่าไม่ต้องสงสัยพวกเราขนาดนั้นหรอก~ ชิจังก็แค่ทำหน้าที่ของตัวเองในฐานะหัวหน้าห้องเท่านั้นเอง~"

# hi "How is she… err… are you doing that?"
hi "แล้วมันเป็นการทำหน้าที่ของชิซู… เอ่อ เธอในฐานะหัวหน้าห้องยังไง"

# "As much as I hate to admit it, it looks as if I still have trouble communicating with Shizune."
"ถึงจะไม่ค่อยอยากยอมรับสักเท่าไหร่ แต่ดูท่าว่าฉันจะยังมีปัญหากับการสื่อสารกับชิซูเนะอยู่"

# "It should be a simple matter of keeping eye contact with her and addressing Shizune instead of Misha in my speech, but when somebody else is doing the talking for her, it's a surprisingly difficult task."
"ที่จริงก็น่าจะไม่ใช่เรื่องยาก แค่สบตากับมิช่าแล้วใช้คำพูดให้เหมือนคุยกับชิซูเนะก็พอ แต่พอมีคนพูดแทนให้ชิซูเนะ\nแล้วกลับเป็นอะไรที่ยากเหลือเชื่อ"

show shizu basic_normal2
with charachange

shi "…"

show misha hips_smile
with charachange

# mi "It's the class representative's job to ensure everybody's doing all right in class, isn't it~?"
mi "หน้าที่ของหัวหน้าห้องคือการดูให้แน่ใจว่าทุกคนในห้องยังโอเคดีอยู่ไง จริงไหม~"

# hi "Not… really…"
hi "ไม่… น่า…"

# hi "Wait, how is making me get your food ensuring that I'll go well in class?"
hi "เดี๋ยว ไอ้การที่ใช้ให้ฉันไปเอาของกินให้นี่มันเกี่ยวกับความโอเคของฉันยังไง"

show shizu adjust_frown
with charachange

# "Shizune huffs and adjusts her glasses disapprovingly."
"ชิซูเนะพ่นลมดังฮึแล้วดันแว่นด้วยความไม่พอใจ"

show shizu behind_frown
with charachange

shi "…"

show misha cross_frown
with charachange

# mi "So this is the thanks we get for giving you companionship during lunchtime?"
mi "นี่เหรอคำขอบคุณของนายที่เราอุตส่าห์มากินข้าวเที่ยงเป็นเพื่อนน่ะ"

$ renpy.music.set_volume(0.0, 3.0, channel="music")

# "That's a total dodge of the question. Wait, hang on…"
"จะเลี่ยงคำถามไกลไปไหน เดี๋ยว เดี๋ยวนะ…"

# hi "How did you know that I…?"
hi "นี่เธอรู้ได้ไงว่าฉัน…"

show shizu basic_normal
with charachange

shi "…"

show misha sign_smile
with charachange

# mi "Lilly's away and Hanako is absent, and since those two are the only people you hang around with…"
mi "ลิลลี่ไม่อยู่ ฮานาโกะก็ขาดเรียน แล้วคนที่นายอยู่ด้วยบ่อย ๆ ก็มีแค่สองคนนั้น เพราะงั้น…"

show shizu adjust_smug
with charachange

shi "…"

show misha cross_smile
with charachange

# mi "You also made it kind of obvious to see~…"
mi "นายเองก็ออกอาการชัดเหมือนกันด้วย~…"

$ renpy.music.set_volume(1.0, 3.0, channel="music")

# "Ouch. I may well have done so, but she didn't need to rub it in. Maybe this is payback for before."
"โอ๊ย ก็คงออกอาการจริง แต่ไม่เห็นต้องซ้ำเติมกันอย่างนี้เลย สงสัยคงเป็นการเอาคืนที่ว่าเมื่อกี้แน่ ๆ"

# hi "Right. Well, thanks. I appreciate it, and that isn't sarcasm."
hi "อืม ขอบคุณนะ ขอบคุณจริง ๆ ไม่ได้ประชดด้วย"

show shizu basic_normal
show misha perky_smile
with charachange

# "The two nod, and we get back to finishing our meals. It feels a little embarrassing to be accompanied just because they noticed I was lonely, but it isn't as if they're strangers either."
"ทั้งสองคนพยักหน้า พวกเรากินมื้อเที่ยงกันต่อให้หมด แอบอายอยู่เหมือนกันที่พวกเธอมากินข้าวเป็นเพื่อนด้วย\nเพราะเห็นว่าฉันเหงา ๆ แต่ก็ใช่ว่าจะเป็นคนอื่นไกลที่ไหนนี่นะ"

# "It isn't long before I finish the last of my bread and start on the last of my juice, and as I do so, I find my mind wandering back to what I'd been thinking about before the two interrupted my train of thought."
"ไม่นานฉันก็กินขนมปังหมดและดื่มน้ำผลไม้อึกสุดท้ายตาม ระหว่างนั้นก็ไพล่นึกไปถึงเรื่องที่คิดอยู่ก่อนหน้า\nที่ทั้งสองคนจะเข้ามาขัด"

# "It feels like I'm the only one in the class that so much as acknowledges Hanako not being there. It felt like this the other times she skipped class, but now it's even more acutely annoying."
"รู้สึกเหมือนทั้งห้องจะมีแค่ฉันที่ใส่ใจรับรู้ว่าฮานาโกะไม่มา คราวอื่นที่ฮานาโกะขาดเรียนไปฉันก็รู้สึกแบบนี้เหมือนกัน\nแต่หนนี้ยิ่งชวนให้หงุดหงิดเป็นพิเศษ"

# "Does nobody care if she's happy or not? Have they just written off any possibility of helping to make her better? Even Mutou doesn't try to keep her in class, and I'm still not wholly convinced by his reasoning."
"ไม่มีใครสนเลยเหรอว่าฮานาโกะจะเป็นตายร้ายดียังไง ทุกคนถอดใจแล้วเหรอว่ายังไงก็คงช่วยให้ฮานาโกะรู้สึกดีขึ้นไม่ได้\nแม้แต่ครูยังยอมปล่อยให้ออกห้องไปได้ง่าย ๆ และฉันก็รู้สึกว่าเหตุผลของครูยังฟังไม่ค่อยขึ้นสักเท่าไหร่"

show misha perky_smile
with charachange

# mi "Hey Hicchan, is your juice past its expiry date?"
mi "นี่ฮิจัง น้ำผลไม้หมดอายุแล้วเหรอ"

# hi "What?"
hi "ฮะ?"

show misha hips_grin
with charachange

# mi "You were pulling a weird face, like this~."
mi "เห็นนายทำหน้าแปลก ๆ แบบนี้~"

show misha perky_confused
show shizu adjust_happy
with charachange

# "As if it were needed, Misha mimics my own expression. Her exaggeration makes me grimace, though Shizune at least takes some amusement from it."
"มิช่าทำสีหน้าล้อกับฉันคล้ายว่าต้องทำประกอบคำพูดตัวเองด้วย ฉันหน้าเบ้ไปเมื่อเห็นมิช่าทำหน้าเวอร์ ๆ แบบนั้น\nแต่ชิซูเนะดูจะชอบใจอยู่บ้าง"

# hi "I was just thinking about Hanako."
hi "แค่คิดถึงเรื่องฮานาโกะอยู่น่ะ"

show misha hips_smile
with charachange

# mi "Oh?"
mi "อื๋อ?"

show shizu basic_happy
with charachange

# "Misha's interest is piqued, and so is Shizune's, once my words are interpreted for her."
"มิช่าสนใจอยากรู้ขึ้นมา ชิซูเนะก็ไม่ต่างกันเมื่อมิช่าแปลให้แล้ว"

# hi "I'm just worried about her being absent so often. Especially now, though, what with her birthday coming around."
hi "แค่คิดมากที่ว่าฮานาโกะขาดเรียนไปบ่อย ๆ น่ะ ยิ่งตอนนี้ใกล้ถึงวันเกิดฮานาโกะแล้วด้วย"

show misha perky_sad
show shizu behind_sad
with charachange

# "The memories of that incident in class are still fresh in their minds. Their faces alone are telling that much."
"ความทรงจำจากเหตุการณ์ในห้องเมื่อครั้งนั้นยังชัดเจนอยู่ในใจของทั้งสองคน ดูแค่สีหน้าก็รู้แล้ว"

# hi "Do you know anything about Hanako? Anything that might help?"
hi "เธอพอรู้อะไรเรื่องฮานาโกะไหม แบบที่พอจะมีประโยชน์น่ะ"

show misha perky_confused
show shizu behind_blank
with charachange

# "Misha shrugs and looks to Shizune, who mulls on this for a while."
"มิช่ายักไหล่แล้วหันไปทางชิซูเนะที่ครุ่นคิดอยู่ครู่หนึ่ง"

show shizu basic_normal2
with charachange

shi "…"

show misha perky_smile
with charachange

# mi "The only people she's ever talked to for more than a sentence or two are you and Lilly."
mi "คนที่ฮานาโกะคุยด้วยมากกว่าประโยคสองประโยคก็มีนายกับลิลลี่นี่แหละ"

# "Shizune may not be able to convey Lilly's name in a derisive tone of speech, but I feel as if it comes through in her sign language. The effect is lost, however, after Misha's interpretation."
"ชิซูเนะอาจถ่ายทอดน้ำเสียงเย้ยหยันตอนพูดชื่อลิลลี่ไม่ได้ก็จริง แต่เหมือนจะสัมผัสได้ผ่านภาษามืออยู่\nซึ่งความรู้สึกส่วนนั้นหายไปเมื่อมิช่าแปลออกมาแล้ว"

show shizu behind_blank
with charachange

shi "…"

show misha sign_smile
with charachange

# mi "There are a couple of things we know about Hanako as Student Council members, thanks to the records that pass through our hands, but we can't say anything about what's in them."
mi "มีอยู่อย่างสองอย่างเรื่องฮานาโกะที่เราในฐานะสภานักเรียนรู้เพราะได้เห็นบันทึกข้อมูลที่ผ่านมือเรามา แต่เรา\nจะบอกไม่ได้ว่าในนั้นมีอะไรบ้าง"

# hi "Understandable."
hi "เข้าใจได้"

# "It sounds a lot like the nurse's “patient confidentiality.” Every time I find someone that knows something about Hanako's past, it turns up being a dead end."
"ฟังดูเหมือนหลัก “ความลับของคนไข้” ของคุณพยาบาลมาก ๆ ทุกครั้งที่เจอคนที่รู้เรื่องอดีตของฮานาโกะ\nก็กลายเป็นว่าต้องเจอกับทางตันแทน"

# "The only way I'll ever find out is by asking her. I don't know if she'll let me know such things, but if it's for her sake, I have to at least try."
"ทางเดียวที่จะรู้ได้คือต้องถามฮานาโกะ ไม่รู้ว่าจะยอมบอกหรือเปล่า แต่ต้องลองสักตั้ง เพื่อตัวของเธอเอง"

show shizu adjust_happy
with charachange

shi "…"

show misha hips_smile
with charachange

# mi "Don't worry about it, Hicchan~. It happens every year, after all~."
mi "อย่าคิดมากน่าฮิจัง~ ก็เป็นแบบนี้ทุกปีนั่นแหละ~"

# "That doesn't remove my sense of worry at all. I still feel a little at fault for what happened in class, but this feels like it goes further, even without their confirmation of that fact."
"ไม่ได้ช่วยให้หายกังวลเลย ยังรู้สึกผิดอยู่หน่อย ๆ กับเรื่องที่เกิดขึ้นในห้องวันนั้น แต่เหมือนว่าจะต้องมีอะไรที่ลึกลงไป\nกว่านั้น ถึงจะยังไม่ได้รับการยืนยันก็เถอะ"

show misha perky_confused
show shizu behind_blank
with charachange

# "Misha notes my troubled expression, her own usually happy and reassuring face dropping."
"มิช่าเห็นว่าฉันทำหน้าเครียด สีหน้าสุขใจชวนให้สบายใจอย่างทุกทีหายไป"

# mi "Everyone has problems they have to deal with, right, Hicchan?"
mi "ทุกคนต่างก็มีปัญหาของตัวเองที่ต้องรับมือกันทั้งนั้นแหละ จริงไหมฮิจัง"

# hi "Yeah. I just wish I could help Hanako more with hers."
hi "อืม แค่ว่าอยากช่วยอะไรให้มันได้มากกว่านี้น่ะ"

# "With that, the conversation trails off on a depressing note."
"แล้วบทสนทนาก็ปิดท้ายไปด้วยความหม่นหมอง"

stop music fadeout 4.0

show misha hips_grin
with charachange

# "Eventually Misha manages to pick the mood back up through her usual bright and bubbly antics, but my mind remains focused on Hanako."
"สุดท้ายมิช่าก็กลับมาทำตัวสดใสร่าเริงตามปกติได้ แต่ในใจฉันยังวนอยู่กับเรื่องฮานาโกะ"

# "I'll go check on her later."
"ไว้ไปแวะหาแล้วกัน"

stop ambient fadeout 1.0

scene bg school_dormhallway
with shorttimeskip

# "I make sure my door is locked after dropping off my school bag."
"เมื่อวางกระเป๋าลงแล้วฉันก็ดูให้แน่ใจว่าล็อกประตูแล้ว"

# "The dorms are quiet. Mutou kept me occupied longer than I expected, discussing my studies after classes ended and pressing on me some worksheets to give to Hanako almost as an afterthought."
"ในหอนั้นเงียบเชียบ ครูรั้งฉันไว้นานกว่าที่คาดโดยคุยเรื่องการเรียนหลังเลิกเรียนแล้วและฝากใบงานให้ฮานาโกะ\nเหมือนเพิ่งนึกขึ้นได้"

# "Absorbed in thought, I'm late in registering the shadow that appears in front of me. Looking up reveals the owner of said shadow."
"ฉันจมอยู่กับความคิดจนไม่ทันได้รับรู้ถึงเงาที่ปรากฏอยู่ต่อหน้าฉัน พอเงยหน้ามองก็เห็นเจ้าของเงานั้น"

show kenji happy at center
with charaenter

play music music_kenji fadein 0.5

# ke "Hey, man. Haven't seen you in a while."
ke "ไงพวก ไม่เจอกันนานเลยนะ"

# hi "Oh. Hi."
hi "อ้าว ไง"

show kenji tsun
with charachange

# ke "What's with that response?"
ke "ตอบแบบนั้นคืออะไร"

# "My absentminded greeting visibly annoys him. I'd probably have had the same reaction."
"ชัดว่าเคนจิหงุดหงิดที่ฉันตอบไปเหม่อ ๆ แบบนั้น เป็นฉันก็คงหงุดหงิดเหมือนกัน"

# hi "Sorry, just thinking about a lot of stuff."
hi "ขอโทษที พอดีคิดอะไรหลายอย่าง"

# ke "“Thinking” is a pretty poor excuse to not be aiding the war effort."
ke "“คิด” นี่ไม่ใช่ข้ออ้างที่จะไม่ไปช่วยรบที่ดีเลยนะ"

# hi "And how goes the war?"
hi "แล้วสงครามเป็นไงบ้าง"

show kenji neutral
with charachange

# ke "I am preparing. Right now I need money to help with those preparations."
ke "กำลังเตรียมการอยู่ ตอนนี้ฉันต้องการเงินเพื่อไปใช้กับการเตรียมการพวกนั้น"

# hi "If you want me to loan you money, just say it."
hi "จะมาขอยืมเงินก็บอกมาเหอะ"

show kenji happy
with charachange

# ke "No man, I'm good."
ke "ไม่ละ ไม่เป็นไร"

# hi "You're… good? You don't want my money?"
hi "ไม่… เป็นไร? ไม่เอาเงินฉันเหรอ"

show kenji tsun
with charachange

# ke "Hey man, don't look so surprised. It's insulting."
ke "เฮ้ยพวก ไม่เห็นต้องตกใจขนาดนั้นเลย โกรธนะเนี่ย"

show kenji neutral
with charachange

# ke "I'm pretty big in the competitive bowling scene, but yesterday, I found some guys who didn't know that."
ke "ฉันมีชื่อในวงการโบว์ลิงอยู่พอสมควรเลยนะ แต่เมื่อวานเจอกับคนที่ไม่รู้ว่าใครใหญ่ว่ะ"

# hi "I'm fairly sure that betting would be against the school rules…"
hi "เหมือนว่าการพนันมันผิดกฎโรงเรียนนะ…"

show kenji tsun
with charachange

# ke "School rules don't matter; this is a war situation. People these days, they have no appreciation for what war means."
ke "กฎโรงเรียนไม่สำคัญหรอก นี่น่ะคือภาวะสงคราม คนสมัยนี้ไม่รู้จักคำว่าสงครามกันดีเท่าไหร่แล้ว"

# hi "So what do you need this money for, dare I ask?"
hi "งั้นขอเรียนถามหน่อยว่าจะเอาเงินก้อนนี้ไปทำอะไร"

show kenji neutral
with charachange

# ke "Non-perishable canned food. Building materials; mostly corrugated iron and wood panels. First aid kit. Camping heater. Portable radio. Sleeping bag. Flashlight. Mechanical clock."
ke "อาหารกระป๋องที่เสียยาก วัสดุสำหรับการก่อสร้าง หลัก ๆ ก็แผ่นเหล็กลูกฟูกกับแผ่นไม้ ชุดปฐมพยาบาล ฮีตเตอร์\nสำหรับการตั้งแคมป์ วิทยุพกพา ถุงนอน ไฟฉาย นาฬิกาแบบใช้เฟือง"

# "At first it strikes me as a rather random assortment of objects and materials, but after a few seconds, it clicks."
"แวบแรกก็รู้สึกว่าเป็นแค่วัตถุกับวัสดุที่มาคละรวม ๆ กัน แต่ผ่านไปสองสามวินาทีถึงร้องอ๋อ"

# hi "Isn't that a list of materials for a fallout shelter?"
hi "นี่มันรายการของที่ต้องใช้กับที่กำบังฝุ่นกัมมันตรังสีนี่"

show kenji happy
with charachange

# ke "Ah, so you've read a Protect and Survive booklet. It's good to see someone so knowledgeable about how to protect themselves."
ke "อ้อ นายเองก็อ่านจุลสาร{i}โพรเทกต์แอนด์เซอร์ไวฟ์{/i}เหมือนกันสินะ ดีใจจริง ๆ ที่เห็นคนรู้เรื่องการเอาตัวรอด\nดีอย่างนี้"
#"Protect and Survive" is British stuff from the eighties. Thus I'm deeming it entirely suitable as a reference work for Kenji in 2010 Japan. Bravo. :3. -SC

# hi "You don't seriously think…"
hi "นี่นายคงไม่ได้คิดจะ…"

show kenji neutral
with charachange

# ke "It's a non-zero possibility."
ke "แต่ความเป็นไปได้ก็ไม่ใช่ศูนย์เลยสักหน่อย"

# hi "No, I'm pretty sure there's zero possibility of that ever happening."
hi "ไม่อะ ฉันว่าความเป็นไปได้ที่จะเกิดเรื่องนั้นมันเป็นศูนย์แหละ"

show kenji happy
with charachange

# "He slowly and dramatically raises an eyebrow. Well, as dramatically as one can raise an eyebrow."
"เคนจิเลิกคิ้วขึ้นแบบเล่นใหญ่ เอ่อ ก็เล่นใหญ่เท่าที่คนเราจะเลิกคิ้วได้อะนะ"

# hi "The chance is, I don't know, zero point one to the trillionth place. It's infinitesimal. Besides, where can you build a fallout shelter anyway? Certainly not on campus."
hi "ความเป็นไปได้มันเท่ากับ ไม่รู้สิ หนึ่งในล้านล้านมั้ง น้อยแบบเป็นค่าที่เข้าใกล้ศูนย์มาก ๆ น่ะ อีกอย่าง จะไปสร้าง\nที่กำบังฝุ่นกัมมันตรังสีตรงไหน ไม่ใช่ในโรงเรียนแน่ ๆ ละ"

show kenji neutral
with charachange

# ke "It's my summer holiday project while I'm at home. My dad said I can do it."
ke "เป็นโครงการปิดเทอมฤดูร้อนของฉันตอนอยู่บ้านไง พ่ออนุญาตด้วย"

# hi "Really?"
hi "จริงเหรอ"

# ke "Yeah. He thought it'll improve my crafting skills and manual dexterity. Or something."
ke "ใช่ พ่อบอกว่าทักษะการประดิษฐ์กับความคล่องแคล่วงของมือจะได้พัฒนาขึ้น หรืออะไรประมาณนั้นแหละ"

# "Knowing Kenji, his dad probably just thought it might keep him out of his hair for a while."
"ดูจากท่าทางเคนจิแล้วพ่อเขาคงแค่อยากปัดให้พ้นรำคาญไปพักหนึ่ง"

# "Still, it does make me wonder what his parents are like. Maybe they're totally normal, and Kenji is just an aberration. On the other hand, maybe this kind of paranoia and fearful survivalism runs in the family."
"แต่พ่อแม่เขาจะเป็นคนยังไงกันนะ อาจจะเป็นคนปกติแต่เคนจิเป็นความไม่ปกติก็ได้ หรือไม่ก็อาจจะหวาดระแวง\nคอยคิดแต่เรื่องเอาตัวรอดแบบนี้กันทั้งบ้าน"

show kenji happy
with charachange

# ke "Hey, want to help me build it? You look like the type to be handy with tools. If I had your help, we could make a really badass bunker instead of just a fallout shelter."
ke "นี่ จะมาช่วยสร้างมั้ย นายดูเป็นคนถนัดเรื่องเครื่องมืดดีนะ ถ้านายมาช่วยเราก็จะได้สร้างหลุมหลบภัยเจ๋ง ๆ\nแทนที่จะเป็นแค่ที่กำบังฝุ่นกำมันตรังสีไง"

# "I doubt that. Playing soccer before my accident gave me good footwork, but I've never really tried my hand at anything approaching real handiwork."
"เหรอวะ ฉันได้ฝึกฝีเท้าจากการเล่นฟุตบอลเมื่อครั้งก่อนเกิดอุบัติเหตุครั้งนั้นก็จริง แต่ไม่เคยทำอะไรที่เป็นงานฝีมือ\nจริง ๆ เลย"

# hi "I'm not, really. I'm busy over the holidays anyway, I'm afraid."
hi "ไม่อะ ไม่เลย แล้วเกรงว่าตอนปิดเทอมฉันจะยุ่งด้วย"

show kenji tsun
with charachange

# ke "A shame. If the feminists ever get a hold of the launch codes, I fear that so few will be prepared."
ke "น่าเสียดาย ถ้าพวกสตรีนิยมได้รหัสยิงนิวเคลียร์แล้วละก็คงมีไม่กี่คนเท่านั้นที่เตรียมตัวพร้อมแล้ว"

# hi "And your fallout shelter will protect you from a nuclear bomb explosion, in the case that this does happen?"
hi "แล้วที่กำบังฝุ่นกำมันตรังสีของนายก็จะปกป้องนายจากระเบิดนิวเคลียร์ได้ถ้าเหตุการณ์นั้นเกิดขึ้นจริง?"

# ke "A fallout shelter isn't meant to protect against the blast. That's what a blast shelter is for."
ke "ที่กำบังฝุ่นใช้กันแรงระเบิดไม่ได้ อันนั้นต้องเป็นที่กำบังแรงระเบิดต่างหาก"

# ke "I thought you knew better."
ke "เรื่องแค่นี้นายน่าจะรู้สิ"

# hi "My mistake…"
hi "ขอโทษที…"

show kenji neutral
with charachange

# ke "My home's pretty far away from any major military sites, so the fallout following a nuclear exchange is a bigger concern than the blast itself."
ke "บ้านฉันอยู่ไกลจากฐานที่มั่นทางการทหารใหญ่ ๆ มาก เพราะงั้นเรื่องที่น่าเป็นกังวลกว่าคือฝุ่นกัมมันตรังสี\nจากสงครามนิวเคลียร์ ไม่ใช่แรงระเบิด"

show kenji happy
with charachange

# ke "What this'll do is keep the dust and other particulates away from me, my food supply, and my sleeping area. It's gotta last me at least fourteen days, though."
ke "ที่กำบังจะกันฝุ่นกับอนุภาคอื่น ๆ ไม่ให้มาถูกตัวฉัน เสบียงฉัน ที่นอนฉัน แต่อย่างน้อยต้องอยู่ให้ได้ครบสี่สิบวัน"

# hi "Fourteen days is a pretty long time."
hi "สี่สิบวันก็นานเหมือนกันนะ"

show kenji neutral
with charachange

# ke "It is. I need one liter of water a day for drinking, two optimally so that I can wash as well. Toiletry is easy enough; just garbage bags and a bin placed outside the shelter area. Food means canned supplies, of course."
ke "นาน ฉันต้องเตรียมน้ำวันละหนึ่งลิตรไว้สำหรับดื่ม อย่างดีก็วันละสองเพื่อจะได้เอามาใช้ล้างเนื้อตัวด้วย\nเรื่องทำธุระส่วนตัวก็ไม่ยาก แค่ใส่เตรียมถังกับถุงขยะไว้นอกบริเวณที่กำบังก็พอ และแน่นอนว่ากินอาหารกระป๋อง"

# hi "Of course. And the radio is for outside communication?"
hi "อืมฮึ แล้ววิทยุก็เอาไว้รับส่งข่าวคราวสินะ"

# ke "Right, right. So I can pick up government alerts on what's going on outside. I need a mechanical clock rather than an electric one in case the electromagnetic pulse from a nuclear airburst fries it, too."
ke "ใช่ ๆ จะได้รู้ว่าข้างนอกเกิดอะไรขึ้นบ้างจากประกาศของทางรัฐบาล ฉันต้องใช้นาฬิกาแบบเฟือง ไม่ใช่แบบใช้ไฟฟ้า\nเผื่อว่ามีนิวเคลียร์ระเบิดกลางอากาศแล้วมีคลื่นแม่เหล็กไฟฟ้ามาทำระบบไฟฟ้าพังด้วย"

# ke "There's all the other stuff I need as well, like extra clothing, matches, and candles. I think I still have time to gather it all, though. Maybe."
ke "แล้วก็มีของอย่างอื่นที่ฉันต้องใช้อีก เช่นเสื้อผ้าสำรอง ไม้ขีดไฟ เทียน แต่ฉันว่ายังมีเวลาให้เตรียมทันอยู่ น่าจะนะ"

# "As much as I hate to say it, I'm a little impressed. He's really researched this and thought it through. Then again, I don't know if I want to live in a post-apocalyptic world with only people like Kenji having survived."
"ถึงจะไม่ค่อยอยากยอมรับเท่าไหร่ แต่ประทับใจหน่อย ๆ อยู่ที่เคนจิค้นคว้าเรื่องนี้มาแบบทะลุปรุโปร่ง แต่ก็นะ\nไม่รู้เหมือนกันว่าฉันจะอยากอยู่ในโลกหลังการล่มสลายที่มีแต่คนอย่างเคนจิเหลือรอดหรือเปล่า"

# hi "It sounds like you really know what you're doing."
hi "ฟังดูรู้ดีจังเลยนะ"

show kenji happy
with charachange

# ke "Damn right I do."
ke "รู้สิวะ"

# "It must be hard, living in constant fear like this. He hardly ever socializes either, so the fact he went bowling with others is in itself something of a surprise."
"คงลำบากมากที่ต้องอยู่อย่างหวาดกลัวตลอดอย่างนี้ ปกติก็แทบไม่ได้ปฏิสัมพันธ์กับใครด้วย ฉันจึงนึกแปลกใจอยู่\nที่เคนจิไปโบว์ลิงกับคนอื่น"

# "This mentality reminds me a little of a certain someone. Thankfully, her fear of others doesn't manifest in such a distinctly eccentric way."
"ความคิดแบบนี้ทำให้ฉันนึกถึงใครบางคนขึ้นมา ซึ่งโชคยังดีที่ความกลัวผู้คนของเธอนั้นไม่ได้มาในรูปแบบ\nที่พิลึกกึกกือเช่นนี้"

# "One thing I know for sure is that I certainly can't tell him exactly why I haven't been hanging around with him much recently."
"แต่ที่แน่ ๆ คือฉันจะบอกเคนจิไม่ได้ว่าเพราะอะไรช่วงนี้ฉันถึงไม่ค่อยได้เจอหน้าเขา"

# hi "It's late. I have stuff to do. I'll think about making a fallout shelter or something, though."
hi "เย็นแล้ว เดี๋ยวฉันมีธุระอีก แต่จะเก็บเรื่องการสร้างที่กำบังฝุ่นกำมันตรังสีอะไรนั่นไปคิดแล้วกัน"

show kenji neutral
with charachange

# ke "Yeah, all right, that's cool. A man has to do what he's gotta do, after all."
ke "เออ ได้ ๆ เยี่ยม ลูกผู้ชายย่อมต้องทำตามหน้าที่นี่นะ"

# ke "You should hang out with me sometime, by the way. You're a cool dude. Cool dudes should hang out together, right?"
ke "จะว่าไป ไว้ว่าง ๆ ไปเที่ยวกับฉันบ้างนะ นายเจ๋งดี คนเจ๋ง ๆ ต้องอยู่ด้วยกันสิ จริงไหม"

# "For some reason, that compliment actually feels kinda nice. The situation with Hanako being what it is, though, means that I probably won't be able to fulfill his request. For now, at least."
"ไม่รู้ทำไม แต่คำชมนั้นทำให้ฉันดีใจอยู่เหมือนกัน แต่เนื่องด้วยสถานการณ์ที่ฮานาโกะเป็นอย่างนี้ก็แปลว่าฉันคง\nทำตามคำขอเคนจิไม่ได้ อย่างน้อยก็สักพัก"

# hi "That'd be good. I'll talk to you later about it when I can."
hi "ก็ดี ไว้มีเวลามาคุยกัน"

show kenji happy
with charachange

# ke "Cool. Later, dude."
ke "เจ๋ง เจอกันพวก"

stop music fadeout 3.0

hide kenji
with charaexit

# "He retreats to his dormitory room."
"เคนจิล่าถอยกลับไปที่ห้องตัวเอง"

# "I had better go see Hanako."
"ไปแวะหาฮานาโกะดีกว่า"

stop ambient fadeout 1.0

scene bg school_dormhanako_ni
show hanagown worry_close:
    center
    xpos 0.39
show expression Solid("#00000022")
show hanako_door_base at right
show hanako_door_door at left
with locationskip

# "I stand outside of the door to Hanako's room, hoping that she isn't in too much of a state as I nervously clutch the worksheets Mutou asked me to pass on to her."
"ฉันยืนอยู่หน้าห้องฮานาโกะพลางหวังว่าเธอจะไม่เป็นอะไรมากโดยในมือกำใบงานที่ครูฝากมาอย่างประหม่า"

# "It's one more reason to visit her, and it gives me something to talk about, so I suppose I should be thankful to him for giving me the task."
"เป็นอีกสาเหตุที่ต้องมาหาด้วย และจะได้มีเรื่องคุย เพราะงั้นก็คงต้องขอบคุณครูที่ฝากฉันมา"

play sound sfx_doorknock2

# "With a long breath to steady myself, I rap my knuckles on the door in front of me."
"ฉันสูดหายใจลึก ๆ ตั้งสติแล้วเคาะประตูตรงหน้า"

# "…Silence. I listen intently for any sound of shuffling coming from inside, but I can't hear a thing."
"…เงียบ ฉันเงี่ยหูฟังว่าพอจะมีเสียงอะไรขยับหรือเปล่า แต่ก็ไม่ได้ยินอะไร"

$ renpy.music.set_volume(0.5, 0.0, channel="sound")
play sound sfx_hammer

# "I knock on the door again, slightly harder."
"ฉันเคาะประตูอีกครั้งให้หนักมือขึ้นอีกเล็กน้อย"

# "Still no answer. How strange."
"ไม่มีเสียงตอบรับ แปลกแฮะ"

# "Scratching my head, I make one last attempt at getting her to answer as I knock on the door one final time."
"ฉันเกาหัวแกรก ๆ พลางลองเคาะเรียกให้ฮานาโกะตอบเป็นครั้งสุดท้าย"

# hi "Hanako, it's just me. Mutou said to give you some stuff."
hi "ฮานาโกะ ฉันเอง ครูฝากเอกสารมาให้แน่ะ"

# "For a while, the attempt seems just as unsuccessful as the last. Just before I slip the sheets under her door, though, I hear the handle rattling."
"ความเงียบซึ่งบ่งบอกว่าความพยายามนั้นล้มเหลวไม่ต่างจากครั้งก่อนนั้นตามมาอยู่ชั่วขณะ แต่จังหวะที่ฉันกำลังจะสอด\nแผ่นกระดาษเข้าทางช่องตีนประตูก็ได้ยินเสียงลูกบิดขยับ"

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_dooropen

show hanako_door_door:
   xpos -0.1
with charamove

play music music_moonlight fadein 4.0

# "As the door opens halfway, I quickly try to see how Hanako's faring. It's a task made somewhat more difficult by her oversized gown hiding so much of her body."
"ประตูเปิดออกกึ่งหนึ่ง ฉันรีบมองสำรวจสภาพฮานาโกะ ซึ่งก็มองยากเพราะเสื้อคลุมที่หลวมโพรกนั้นปกปิด\nร่างกายเธอไปเสียเกือบหมด"

# "She doesn't look sick, or at least not immediately so. To be honest, I'd have preferred that to her expression right now. She looks terribly tired, and appears to be barely acknowledging my presence."
"ฮานาโกะดูจะสบายดี อย่างน้อยก็ด้วยสภาพร่างกายน่ะนะ แต่ว่าตามตรง ฉันยอมเห็นฮานาโกะตอนไม่สบายดีกว่า\nต้องมาเห็นสีหน้าของฮานาโกะตอนนี้ เธอดูอิดโรย และเหมือนแทบจะไม่รับรู้ถึงตัวตนฉันแล้ว"

# hi "Hi, Hanako. Mutou wanted me to give you these since you weren't in class today."
hi "ไง ฮานาโกะ พอดีวันนี้เธอไม่ได้เข้าเรียน ครูเลยฝากอันนี้มาให้"

# "I hold out the loose sheets, which she tentatively takes in her hands. The way she moves is devoid of thought. Her posture is slumped, in an unusual manner for someone that's so often tense and wound up."
"ฉันยื่นแผ่นกระดาษให้ ฮานาโกะก็รับไปแบบอึก ๆ อัก ๆ ท่าทางการขยับตัวของเธอนั้นดูเหมือนไม่ได้มีความตั้งใจอะไร\nท่าทีอ่อนล้าผิดวิสัยคนที่ปกติจะเกร็งตัวยึดอยู่บ่อย ๆ"

show hanagown distant_close
with charachange

# "Even her eyes keep looking away from mine, doing their best to avoid eye contact. I move my head a little to try and get a better look, but she just ends up turning away."
"ฮานาโกะยังเอาแต่เสตามองทางอื่นไม่ยอมสบตาสุดความสามารถ ฉันชะเง้อหัวเพื่อดูให้เต็มตาอีกหน่อย ทว่าเธอ\nก็หันหน้าหนีไป"

# hi "Are you… okay? If you're feeling sick or anything, I could go get a nurse."
hi "ไหว… หรือเปล่า ถ้าไม่สบายหรืออะไรให้ฉันเรียกพยาบาลมาก็ได้นะ"

# "It feels almost pitiful to put on such a routine “get well soon” act. I can't think of anything else I could possibly do for her, though."
"พอมาทำตัวแบบ “หายไว ๆ นะ” อย่างนี้แล้วก็รู้สึกสมเพชเหมือนกัน แต่ก็ไม่รู้แล้วว่าจะทำยังไงให้ฮานาโกะดีขึ้นได้อีก"

show hanagown normal_close
with charachange

# "She seems to collect herself a little at the notion… but only a little. Her head remains turned away, but her eyes move towards me."
"ฮานาโกะดูจะใจเย็นลงเมื่อพิจารณาตัวเลือกนั้น… แต่ก็เย็นลงแค่นิดหน่อย เธอยังคงหันหน้าหนีอยู่เหมือนเดิม\nแต่ตาเธอมองมาที่ฉัน"

# ha "I'm fine."
ha "ฉันสบายดี"

# "An awkward silence follows. As it lingers, I notice that the sleeves and the cuffs of her gown bear slightly damp stains. Her cheeks are a bit red, too. Has she been crying?"
"และความเงียบอันน่าอึดอัดก็ตามมา ระหว่างที่เงียบกันไปนั้นฉันก็เห็นว่าแขนเสื้อกับปลายแขนเสื้อชุดนอนนั้น\nมีรอยเปียก ๆ อยู่ แก้มก็แดง ๆ ด้วย ร้องไห้มาเหรอเนี่ย"

# hi "I see."
hi "เข้าใจละ"

# "I hesitate a little before coming out with the words I really came here to say."
"ฉันลังเลอยู่เล็กน้อยก่อนจะพูดในสิ่งที่ฉันตั้งใจจะมาพูด"

# hi "Would you like me to stay? I don't have anything urgent to do at the moment, so it wouldn't be any trouble."
hi "อยากให้อยู่เป็นเพื่อนไหม ตอนนี้ฉันก็ไม่มีอะไรเร่งด่วนที่ต้องทำ ไม่เป็นการรบกวนฉันหรอก"

show hanagown distant_close
with charachange

# "Her eyes slide away from me, and I lose any hope for an improvement of her mood. I wait for a response, but she doesn't say anything, nor give any kind of gesture. She just stands there, looking away from me."
"ฮานาโกะเสตาหนีไปจนฉันหมดหวังที่จะทำให้เธอรู้สึกดีขึ้นได้ ฉันรอคำตอบทว่าเธอก็ไม่พูดหรือมีท่าทีอะไร\nแค่ยืนอยู่เฉย ๆ ไม่มองหน้ากัน"

# hi "Hanako…?"
hi "ฮานาโกะ…?"

# "She slowly shakes her head."
"เธอสั่นหัวช้า ๆ"

# hi "Okay. Um… good night, then."
hi "โอเค เอ่อ… งั้นก็ราตรีสวัสดิ์"

stop music fadeout 3.0

show hanako_door_door:
   xpos 0.0
with charamove

play sound sfx_doorclose

# "With that, Hanako steps back and closes her door without a second word."
"แล้วฮานาโกะก็ถอยกลับเข้าห้องไปแล้วปิดประตูไม่พูดอะไรอีก"

# "More than a little worried, I retreat back to my room."
"ฉันกลับมาที่ห้องตัวเองพร้อมความกังวลที่ไม่น้อยเลย"

# Timeskip
scene bg school_dormhallway
with locationskip

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_footsteps_hard

# "Wandering up the hallway, I keep mulling over what happened. It felt like Hanako was only half there, as if I was interacting with a robot that was just doing what it was programmed to without any real thought."
"ฉันเดินไปตามโถงทางเดินพลางคิดถึงเหตุการณ์นั้น เหมือนจิตใจฮานาโกะไม่ได้อยู่กับตัว ราวกับว่าฉันกำลังปฏิสัมพันธ์\nอยู่กับหุ่นยนต์ที่ทำตามแค่สิ่งที่ได้รับการตั้งค่ามาให้ทำอย่างไม่คิดอะไรเลย"

# "She was a husk of a person."
"ฮานาโกะเป็นเพียงเปลือกที่ว่างเปล่า"

# "This is frustrating. I had hoped that meeting Hanako would help the situation, but I feel like it's only made it harder to understand her. How am I supposed to try and help her when she quite literally shuts me out like that?"
"หงุดหงิดชะมัด ก็คิดว่าถ้าได้เจอฮานาโกะแล้วอะไร ๆ จะดีขึ้นเสียอีก แต่เหมือนจะยิ่งทำให้ฉันเข้าใจเธอได้ยากไปอีก\nถ้ากีดกันกันแบบนี้แล้วฉันจะช่วยได้ยังไง"

stop ambient fadeout 0.3

scene bg school_dormhisao_ni
with locationchange

# "I don't even bother to turn on the light, opting instead to simply change into my pajamas, quickly choke down my evening pills, and collapse onto my bed."
"ฉันไม่มีแก่ใจจะเปิดไฟในห้อง จึงเพียงเปลี่ยนเสื้อผ้าเป็นชุดนอนและกรอกยารอบเย็นเข้าปากแล้วล้มตัวลงกับที่นอน"

scene black
with shuteye

#-----------------

label th_H22:

scene bg school_scienceroom
with locationchange

play music music_pearly

# "Once again, Hanako doesn't turn up for class. Try as I might to concentrate on other matters, this fact continues to distract me throughout the entire school day, and even as I walk through the school gardens to the dormitories."
"ฮานาโกะไม่มาเข้าเรียนอีกแล้ว ฉันลองปรับให้สมองไปจดจ่อกับเรื่องอื่น แต่เรื่องนี้ก็ยังดึงสมาธิฉันไปตลอดทั้งวัน\nที่เรียนจนกระทั่งตอนที่เดินผ่านสวนในโรงเรียนกลับหอ"

# "I don't think today being her birthday is a coincidence, either. I don't know the link between the two events though, nor do I have any idea on what she's feeling."
"และการที่วันนี้เป็นวันเกิดของฮานาโกะด้วยก็ไม่ใช่เรื่องบังเอิญแน่นอน แต่ฉันก็ไม่รู้ว่าทั้งสองเหตุการณ์เกี่ยวข้องกัน\nอย่างไร ไม่รู้ด้วยว่าฮานาโกะรู้สึกว่ายังไงบ้าง"

# "Were it physical pain, I could at least provide some limited comfort. With something like this though, I have no idea where to start."
"ถ้าเป็นอาการเจ็บป่วยทางกายฉันก็อาจพอช่วยเยียวยาอะไรให้ได้บ้าง แต่พอเป็นเรื่องแบบนี้แล้วฉันไม่รู้เลยว่าจะเริ่ม\nจากตรงไหนดี"

# "I run the people I know through my head, thinking about whether they could help. Shizune and Misha don't know that much about Hanako, and what little they do know they can't tell me. Same for the nurse."
"ฉันไล่ย้อนนึกถึงคนที่ฉันรู้จักว่ามีใครที่จะช่วยได้หรือเปล่า ชิซูเนะกับมิช่าไม่รู้เรื่องฮานาโกะขนาดนั้น ซึ่งส่วนที่รู้\nก็บอกฉันไม่ได้ คุณพยาบาลก็เหมือนกัน"

# "In the end, there's only one person that knows Hanako well and would be willing to tell me anything."
"สุดท้ายก็มีเพียงคนเดียวที่รู้จักฮานาโกะดีพอและพร้อมที่จะบอกฉันทุกอย่าง"

scene bg school_dormhisao
with shorttimeskip

# "Entering my dormitory room, I notice something that takes me off guard; it's starting to feel familiar."
"เมื่อเข้าห้องมาแล้วฉันก็ต้องแปลกใจว่าตัวเองเริ่มคุ้นเคยกับที่นี่แล้ว"

# "With everything that's going on around me, I'm thankful that this room's started to finally be somewhere I can relax a little. When I'd first entered Yamaku, it felt immediately foreign in every way, from the untouched neatness to the way it smelled."
"ฉันนึกยินดีที่ห้องนี้ได้กลายเป็นที่ที่ฉันพอจะพักใจได้บ้างแล้วด้วยต้องเจอกับเรื่องราวร้อยแปดพันเก้า ตอนที่\nมายามากุครั้งแรกฉันรู้สึกว่าห้องนี้เป็นสิ่งประหลาดทันที ตั้งแต่ความเรียบร้อยจากการที่ไม่มีคนอยู่ไปจนถึงกลิ่นในห้อง"

# "Focusing back on the task at hand, I throw my bag onto the bed as I open the top drawer of my desk."
"ฉันโยนกระเป๋าไว้ที่เตียงแล้วกลับมาสนใจกับสิ่งที่ต้องทำด้วยการเปิดลิ้นชักโต๊ะตัวบนสุด"

# "Before she left, Lilly told me the number to call her on while in Scotland and I wrote it down. In hindsight, I wonder if she knew something like this could happen."
"ลิลลี่บอกเบอร์โทร. ไว้ก่อนไปสกอตแลนด์ ซึ่งฉันก็จดไว้ แต่จะว่าไปแล้ว ที่บอกไว้เพราะรู้ว่าจะเกิดเรื่องแบบนี้\nหรือเปล่านะ"

# "Now that she's out of reach, I realize just how much both Hanako and I have relied on her for guidance."
"พอลิลลี่ไม่อยู่ด้วยแล้วถึงนึกได้ว่าทั้งฮานาโกะทั้งฉันต้องพึ่งพาให้ลิลลี่เป็นคนนำทางบ่อยแค่ไหน"

# "I dig around drawer after drawer, looking for that damned piece of paper. Eventually, thankfully, I find it nestled under a borrowed library book."
"ฉันเปิดลิ้นชักที่โต๊ะตัวแล้วตัวเล่าหาว่าตัวเองเก็บไอ้กระดาษแผ่นนั้นไว้ที่ไหน โชคดีที่สุดท้ายก็เจอ หนังสือที่ยืม\nมาจากห้องสมุดทับไว้อยู่"

scene bg school_dormhisao_blurred
show phone mobile:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with locationchange
with Pause (0.5)

# "I probably should have just entered it directly into my cell phone, come to think of it. Without further ado, I enter the numbers and anxiously press the call button."
"จะว่าไปแล้ว บันทึกใส่โทรศัพท์ไปเลยเสียก็สิ้นเรื่อง ฉันกดไปตามปุ่มตัวเลขในทันทีแล้วกดโทร. ด้วยความร้อนใจ"

# "Eventually the phone picks up, a feminine voice I don't recognize on the other end. It's probably Lilly's mother."
"ในที่สุดก็มีคนรับสาย ปลายสายเป็นเสียงผู้หญิงคนหนึ่งที่ฉันไม่คุ้นหู อาจจะแม่ลิลลี่มั้ง"

stop music fadeout 1.0

#mystery "<Good morning. This is Karla Satou. May I help you?>"
mystery "{image=vfx/garbage.png} {image=vfx/garbage.png} Satou {image=vfx/garbage.png}?"

# "English? Suddenly finding myself unprepared, I realize I can't understand a word she says, either due to my limited vocabulary or her heavy accent. I should have anticipated this, since according to Lilly, her mother is a native Scot."
"ภาษาอังกฤษเหรอ ไปต่อไม่ถูกเลย ฟังไม่ออกเลยสักคำแฮะ คงเพราะฉันรู้คำศัพท์น้อยไม่ก็เพราะสำเนียง จริง ๆ น่าจะ\nคิดได้แต่แรกเพราะรู้มาจากลิลลี่แล้วว่าแม่เธอนั้นเป็นคนสกอตแลนด์โดยกำเนิด"

# "I soldier on in the hope that she must know some Japanese, considering it's her daughter's native language."
"ฉันดันทุรังไปต่อด้วยความหวังว่าเธอคงพอจะรู้ภาษาญี่ปุ่นบ้าง เพราะยังไงก็เป็นภาษาแม่ของลูกตัวเอง"

# hi "Um, it's Hisao Nakai… speaking…"
hi "เอ่อ ฮิซาโอะ นากาอิ… นะครับ…"

# "An enthusiastic sound of realization can be heard as she recognizes the language. My feeling of relief is immense."
"พอรู้ว่าเป็นภาษาอะไรเธอก็ทำเสียงตื่นเต้น ตอนนี้ฉันโล่งใจอย่างกับยกภูเขาออกจากอก"

# "Mrs. Satou" "Ah, you must be one of Lilly's friends from school, correct?"
thname("คุณนายซาโต้") "อ้อ เธอคงเป็นเพื่อนที่โรงเรียนของลิลลี่ใช่มั้ย"

# "Even so, her accent means I have to concentrate to work out what she's saying."
"ถึงอย่างนั้นก็เถอะ ฉันยังต้องเงี่ยหูฟังให้ดีเพราะยังมีติดสำเนียงอยู่"

# hi "Yes, that's right. Pleased to speak to you, Mrs. Satou."
hi "ครับ ใช่ครับ ยินดีที่ได้รู้จักนะครับ คุณนายซาโต้"

# "Mrs. Satou" "It's so nice of her to find someone so polite! Lilly dear, it's for you!"
thname("คุณนายซาโต้") "มีเพื่อนมารยาทงามอย่างนี้ด้วย! ลิลลี่ มีคนโทร. หาลูกแน่ะ!"

# "Her mother seems nice, if a little overenthusiastic given the mundane situation."
"ก็ดูเป็นคนดีนะ ถึงออกจะตื่นเต้นไปหน่อยกับเรื่องธรรมดา ๆ อย่างนี้ก็เถอะ"

# "There's a small silence as Lilly takes her time getting to the phone. In the distance, I can just make out her mother scolding her playfully for just getting up."
"ก่อนที่ลิลลี่จะมารับโทรศัพท์นั้นปลายสายเงียบไปครู่หนึ่ง ฉันได้ยินเสียงแม่ลิลลี่ที่กึ่งดุกึ่งกระเซ้าเจ้าตัวที่เพิ่งตื่นอยู่แว่ว ๆ"

# li "Hello, Lilly speaking."
li "สวัสดีค่ะ ลิลลี่นะคะ"

# hi "You sound awful."
hi "เสียงฟังดูไม่ไหวเลยนะ"

# "She makes a sound somewhere between a dying animal and a yawn."
"ลิลลี่ทำเสียงหาวโอดโอยคล้ายสัตว์ใกล้ตาย"

# "The one thing I did remember to check before calling was the time zone. It'd be pretty late in the morning over there, so she really has no excuse."
"ก่อนโทร. ฉันดูเรื่องเขตเวลาแล้วเรียบร้อย ตอนนี้ที่สกอตแลนด์ก็เข้าช่วงสายพอสมควรแล้ว เพราะงั้นจะอ้างอะไร\nก็คงไม่ได้อีก"

# hi "Not feeling well?"
hi "ไม่สบายเหรอ"

# li "Just tired. What time is it there?"
li "แค่เพลียนิดหน่อยจ้ะ ที่ญี่ปุ่นกี่โมงแล้วเหรอ"

# hi "Late afternoon. School finished for the day not long ago."
hi "บ่ายแก่ ๆ เพิ่งเลิกเรียนมาเมื่อกี้เอง"

# li "Hanako's not well, is she?"
li "ฝั่งฮานาโกะคงไม่โอเคใช่มั้ย"

play music music_drama 

# "That was quick. My assumption that she must have known something like this could happen seems to have been on the mark."
"ตัดเข้าเรื่องเร็วแฮะ ดูท่าจะเดาถูกว่าลิลลี่ต้องรู้ว่าจะเกิดเรื่องแบบนี้แน่"

# hi "How did you know?"
hi "รู้ได้ยังไง"

# li "Because today is her birthday. I'd hoped she might have gotten at least a little better after coming to know you, but…"
li "ก็วันนี้วันเกิดฮานาโกะนี่นา ทีแรกฉันก็หวังอยู่นะว่าพอฮานาโกะได้สนิทกับเธอแล้วจะดีขึ้น แต่ว่า…"

# li "How is she right now?"
li "ตอนนี้ฮานาโกะเป็นยังไงบ้าง"

# hi "She missed school today and yesterday. I still have to check up on her today. To be honest, after seeing how she was when I talked to her yesterday… I'm pretty anxious."
hi "ฮานาโกะขาดเรียนไปวันนี้กับเมื่อวานน่ะ เดี๋ยววันนี้ต้องไปหาอีกที ว่าตามตรง ดูจากสภาพฮานาโกะตอนฉัน\nไปคุยด้วยเมื่อวานแล้ว… ฉันก็หวั่น ๆ ใจอยู่เหมือนกัน"

# hi "I really have no idea what to make of it. Has this happened in the past? Is it related to her scarring in some way?"
hi "ฉันจนปัญญาไม่รู้จริง ๆ ว่าจะทำยังไงดี เมื่อก่อนเคยมีแบบนี้มั้ย เกี่ยวอะไรกับแผลเป็นหรือเปล่า"

# li "Unfortunately so. Roughly the same thing happened last year when her birthday came up."
li "เกรงว่าจะเป็นอย่างนั้นจ้ะ วันเกิดฮานาโกะเมื่อปีที่แล้วก็มีเรื่องประมาณนี้เหมือนกัน"

# li "As far as I can tell, it's because her parents died in the accident that caused her scarring, and Hanako blames herself for their deaths."
li "เท่าที่พอจะนึกออก คงเป็นเพราะพ่อแม่ฮานาโกะท่านเสียชีวิตไปพร้อม ๆ กับตอนที่เกิดอุบัติเหตุที่ทำให้เกิดแผลเป็น\nฮานาโกะเลยโทษตัวเองว่าตัวเองเป็นต้นเหตุที่ทำให้ทั้งสองคนจากไป"

# "What she says does seem to make sense. If she's blaming herself on her birthday, she may well be ruing that she was ever born."
"ที่พูดมาก็มีเหตุผล ถ้าถึงวันเกิดแล้วฮานาโกะโทษตัวเอง ก็คงหมายความได้ว่าเธอกำลังนึกเสียใจที่ตัวเองเกิดมา"

# "Hanako had mentioned her stay in the orphanage to me. Maybe I should take some heart that she trusts me enough to tell me such a thing."
"ฮานาโกะเคยเล่าเรื่องตอนที่อยู่สถานรับเลี้ยงเด็กกำพร้าให้ฟัง คงนับว่าเป็นเรื่องที่ดีละนะที่เชื่อใจพอที่จะเล่า\nอะไรแบบนั้นให้ฟังได้"

# "Lilly seeming so in the dark about it though, almost to the extent that I am, is a surprise."
"แต่ที่ฉันแปลกใจก็คือ ลิลลี่ดูจะไม่ค่อยรู้เรื่องรู้ราวอะไรพอ ๆ กันกับฉันด้วยเช่นกัน"

# hi "So that's why she lives in the student dormitories, as well. Has she told you any more about the accident?"
hi "ก็คงเป็นเหตุผลที่ฮานาโกะมาอยู่หอในด้วยละนะ ฮานาโกะเคยเล่าเรื่องอุบัติเหตุที่ว่าอะไรให้ฟังอีกหรือเปล่า"

# li "As close as we've come… she's very barely told me anything about what happened. What I know about it is largely conjecture."
li "เราสองคนสนิทกันขนาดนี้ก็จริง… แต่ฮานาโกะแทบไม่เคยเล่าให้ฟังเลยว่าเกิดอะไรขึ้นบ้าง ที่ฉันรู้ส่วนใหญ่ก็เป็นแค่\nการคาดการณ์เท่านั้นแหละจ้ะ"

# "She sounds depressed, almost defeated. Considering the trauma Hanako must have gone through, I really can't fault Lilly for not knowing. Nevertheless, she still seems to consider it a personal failing."
"น้ำเสียงลิลลี่ฟังดูเศร้าหมองค่อนไปทางเหนื่อยอ่อน แต่ถ้าคิดดูว่าฮานาโกะต้องผ่านเหตุการณ์สะเทือนขวัญอะไรมาบ้าง\nลิลลี่จะไม่รู้ก็ไม่แปลก แต่เหมือนลิลลี่จะยังมองว่าเป็นฝั่งตัวเองที่ยังพยายามไม่พออยู่ดี"

# hi "Don't blame yourself, Lilly. With everything she's gone through…"
hi "อย่าโทษตัวเองเลยลิลลี่ ฮานาโกะก็ผ่านอะไรมาขนาดนั้น…"

# "There's a long silence from the other end of the line. I begin to wonder if the call cut out before the voice at the other end speaks once again."
"ปลายสายเงียบอยู่นานจนชักสงสัยแล้วว่าหรือสายจะตัดไปแล้ว แต่เสียงจากปลายสายก็ดังขึ้นอีกครั้ง"

# li "There is another person, though, that has been a subject of worry for me as of late."
li "แต่มีอีกคนนะที่ช่วงนี้ฉันก็เป็นห่วงอยู่เหมือนกัน"

# hi "Oh?"
hi "หืม?"

# "I run through the people she could be talking about in my head. The only friends she seems to keep very close are Hanako and me, though there is Akira as well…"
"ฉันลองไล่นึกดูว่าคนที่ลิลลี่พูดถึงจะเป็นใครได้บ้าง เพื่อนที่ลิลลี่สนิทด้วยจริง ๆ ก็เหมือนจะมีแค่ฮานาโกะกับฉัน หรือว่า\nอากิระ…"

# li "That person is you, Hisao."
li "คนที่ว่าก็คือเธอนี่แหละจ้ะฮิซาโอะ"

# "There's another silence on the line, but this time it's caused by me."
"เกิดความเงียบขึ้นในสายอีกครั้ง แต่คราวนี้มาจากฉัน"

# "Making others worry about me is something I've very actively tried to avoid since coming to Yamaku. Indeed, even my interaction with Hanako has helped stave off any major health problems thanks to our relaxed and slow-paced lives."
"ตั้งแต่ฉันมายามากุฉันก็พยายามเลี่ยงไม่ให้คนอื่นต้องมาเป็นห่วงอยู่เสมอ แม้แต่การที่ฉันอยู่กับฮานาโกะก็ช่วยให้ฉัน\nพ้นจากปัญหาเรื่องสุขภาพที่ร้ายแรงได้ด้วยว่าพวกเราใช้ชีวิตกันแบบสบาย ๆ ไม่เร่งรีบ"

# hi "Uh… huh. What is there to worry about over me?"
hi "อ่า… ฮะ ฉันมีอะไรให้เป็นห่วงด้วยเหรอ"

# li "I apologize; I didn't mean any offense."
li "ขอโทษทีจ้ะ ไม่ได้ตั้งใจจะตำหนิอะไรเธอนะ"

# hi "Sorry, I was just taken a bit off guard. Still, isn't Hanako a bigger problem at the moment?"
hi "โทษที ๆ พอดีเมื่อกี้ไม่ได้ตั้งตัว แต่ตอนนี้ปัญหาที่ใหญ่กว่าน่าจะเป็นเรื่องฮานาโกะไม่ใช่เหรอ"

# li "For some time now I've thought that the both of you may be feeding into each other's more worrying habits. I tried to amend this before leaving, but it seems to have done little."
li "ฉันคิดมาสักพักแล้วว่าเธอสองคนจะยิ่งทำให้นิสัยที่ชวนให้เป็นห่วงของกันและกันย่ำแย่เข้าไปอีก ก่อนเดินทาง\nฉันก็ลองบรรเทาอาการนี้ดูแล้ว แต่เหมือนจะไม่ได้ผลสักเท่าไหร่"

# hi "“Worrying habits?”"
hi "“นิสัยที่ชวนให้เป็นห่วง” เหรอ"

# li "When I asked you about what you had in mind for the future, your answer was very similar to what Hanako has said in the past when that question was posed to her."
li "ตอนฉันถามเธอว่าจะเอายังไงกับอนาคต คำตอบของเธอคล้ายกับตอนที่ฮานาโกะตอบคำถามนี้มาก"

# li "It is well and good to want to protect her, but I fear that treating Hanako like this, as if she were a daughter or someone in need of special care, is only going to achieve the opposite."
li "ที่เธออยากปกป้องฮานาโกะน่ะก็ดีแล้ว แต่ฉันเกรงว่าถ้ายังปฏิบัติกับฮานาโกะเหมือนเป็นลูกสาวหรือคนที่ต้อง\nได้รับการดูแลเป็นพิเศษอย่างนี้รังแต่จะทำให้ได้ผลตรงกันข้าม"

#right now the ending just hinges on this one choice. the previous ones don't even matter at all.
#the best you get is to choose your bad end and small alternatives later

label th_choiceH22:
menu:
    with menueffect

    # "The situation got effectively turned on its head. After everything that's happened, this is the first time I find myself doubting Lilly's judgment."
    "เหตุการณ์กลับตาลปัตรไปเสียแล้ว มีเรื่องอะไรหลายอย่างเกิดขึ้นแล้วก็จริง แต่หนนี้เป็นครั้งแรกที่ฉันนึกเคลือบแคลง\nกับการพินิจของลิลลี่"

    # "Agree with Lilly.":
    "เห็นด้วยกับลิลลี่":
        return m1
        
    # "Trust my own judgment.":
    "เชื่อการพินิจของตัวเอง":
        return m2

label th_H22a:

# "I don't want to admit it, but she may have a point. Something else bugs me, though."
"ก็คงจริงอย่างลิลลี่ว่า ถึงจะไม่อยากยอมรับเลยก็เถอะ แต่ฉันยังมีอย่างอื่นที่คาใจอยู่"

# hi "And you tried to… “amend” this?"
hi "แล้วเธอก็ลอง… “บรรเทา”?"

# hi "Wait… our outing into the city?"
hi "เดี๋ยว… ที่ไปเที่ยวกันในตัวเมืองวันนั้น?"

# li "Quite astute. I thought that it might help if I dragged both of you out of Yamaku and into the wider world. I am thankful you became closer for it, though."
li "หัวไวมากจ้ะ ฉันคิดว่าถ้าลากพวกเธอสองคนออกจากยามากุไปพบกับโลกที่กว้างขึ้นแล้วอาจช่วยอะไรได้บ้าง\nแต่ฉันก็ดีใจนะที่หลังจากนั้นเธอสองคนก็สนิทกัน"

# "So she noticed that. I suppose she may well have been paying attention to us, and her hearing's incredibly good; quite likely good enough to have picked up what we were talking about, if she tried."
"สังเกตได้ด้วยสินะ ก็น่าจะกำลังจับสังเกตเราสองคนอยู่นั่นแหละ แล้วหูลิลลี่ก็ดีมากด้วย ดีชนิดที่ว่าถ้าจะเงี่ยหูฟัง\nเสียอย่างแล้วก็จะได้ยินสิ่งที่เราคุยกันแน่นอน"

# hi "This sounds more and more like you were manipulating us."
hi "ยิ่งฟังยิ่งเหมือนว่าเธอวางแผนหลอกพวกเราเลยนะ"

# "Silence. It's a harsh way of putting it, but I have no intention of stepping back from those words."
"เงียบ เป็นคำที่แรง แต่ฉันไม่ถอนคำพูดหรอก"

# li "I'm sorry. I was just… worried about you."
li "ขอโทษจ้ะ ฉันแค่… เป็นห่วงเธอ"

# hi "It's fine. I guess there are more important things anyway."
hi "ไม่เป็นไร ยังไงก็คงมีเรื่องที่สำคัญกว่าละนะ"

# "It's not a total surprise that she'd do such a thing. Her motherly nature can be slightly overbearing at times, but she does have the best of intentions."
"ก็ไม่ได้แปลกใจนักว่าลิลลี่จะทำอะไรแบบนี้ บางครั้งความเป็นแม่ชอบดูแลของเธออาจจะมากไป แต่ทุกอย่างล้วน\nมาจากเจตนาดีทั้งนั้น"

# hi "So you think I should think about myself more instead of trying to cater to Hanako?"
hi "สรุปคือเธอคิดว่าฉันควรจะคิดถึงตัวเองก่อนแทนที่จะไปดูแลฮานาโกะเหรอ"

# li "That largely sums it up. Again, I'm sorry for not telling you this in a clearer way before going behind your back."
li "รวม ๆ ก็ประมาณนั้นจ้ะ ยังไงก็ขอโทษนะจ๊ะที่ไม่ได้บอกให้ชัด ๆ ก่อนแล้วแอบไปวางแผนลับหลังอย่างนั้น"

# li "I know I am at least as guilty of being overprotective of Hanako as you, but I fear that you are neglecting yourself in your efforts to give Hanako happiness."
li "ฉันรู้ว่าฉันเองก็ผิดอยู่บ้างที่คอยประคบประหงมฮานาโกะเหมือน ๆ กันกับเธอ แต่ฉันเกรงว่าเธอจะมัวแต่\nมอบความสุขให้ฮานาโกะจนไม่ได้ดูแลตัวเอง"

# hi "Do you really think Hanako will be okay?"
hi "เธอคิดว่าฮานาโกะจะไม่เป็นไรจริง ๆ เหรอ"

# li "She isn't as fragile as you think. I don't know exactly what experiences she's lived through, or what feelings she has in her mind, but she has managed to work her way through them until now."
li "ฮานาโกะไม่ใช่คนเปราะบางขนาดนั้นอย่างที่เธอคิดหรอกจ้ะ ฉันก็ไม่รู้รายละเอียดว่าฮานาโกะต้องผ่านอะไรมาบ้าง\nไม่รู้ว่าในใจรู้สึกอย่างไร แต่ฮานาโกะก็ก้าวผ่านทุกอย่างมาได้จนตอนนี้แล้ว"

# li "It's also my hope that giving her a little space will allow her to decide what she truly wants for herself, and give her the initiative to reach out for it."
li "แล้วฉันเองก็หวังด้วยว่าถ้าให้พื้นที่กับฮานาโกะแล้วเจ้าตัวอาจจะตัดสินใจได้ว่าสิ่งที่ต้องการจริง ๆ คืออะไร\nแล้วค่อยเรียกร้องเอง"

# li "Please have faith in Hanako. That's all I ask."
li "ได้โปรดเชื่อมั่นในตัวฮานาโกะเถอะจ้ะ ฉันขอแค่นี้แหละ"

# hi "I'll… I guess I'll think about it for a while."
hi "ได้… เดี๋ยวฉันคงต้องเก็บไปคิดสักพัก"

# li "That's good. Being rash won't get you anywhere."
li "ดีแล้วจ้ะ บุ่มบ่ามไปก็ไม่ได้อะไรขึ้นมาหรอก"

# li "I know that at times you may doubt your relationship to Hanako, but she does…"
li "ฉันรู้ว่าบางทีเธออาจยังไม่แน่ใจเรื่องความสัมพันธ์ของเธอกับฮานาโกะ แต่ฮานาโกะน่ะ…"

# "Lilly cuts herself off and takes a moment to reconsider her words."
"ลิลลี่ตัดบทตัวเองไปแล้วเว้นช่วงเพื่อเลือกสรรคำพูด"

# li "Please keep in mind that I wouldn't have befriended you if I hadn't thought you a fundamentally good person. You're a good friend, both to myself and to Hanako."
li "อย่าลืมนะว่าที่ฉันมาเป็นเพื่อนกับเธอก็เพราะฉันคิดว่าจริง ๆ แล้วเธอเป็นคนดี เธอก็เป็นเพื่อนที่ดีต่อทั้งฉัน\nทั้งฮานาโกะ"

# hi "Thank you. That helps."
hi "ขอบคุณนะ ค่อยโล่งใจหน่อย"

# "We share some smalltalk to try and lighten the atmosphere, but it feels very stilted. There's a lot I don't know about Lilly's stay in Scotland, but after such a heavy subject, I want to be alone for a bit to think."
"เราคุยเรื่อยเปื่อยกันบ้างหวังคลายบรรยากาศ แต่รู้สึกเหมือนกำลังฝืนอยู่มาก ๆ ฉันยังไม่รู้ว่าที่ลิลลี่เดินทาง\nไปสกอตแลนด์ครั้งนี้มีอะไรหรือเป็นอย่างไรบ้าง แต่พอคุยเรื่องหนัก ๆ กันแบบนั้นแล้วฉันก็อยากมานั่งคิด\nอยู่ตัวคนเดียวสักพัก"

stop music fadeout 8.0

show phone mobile:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with None

scene bg school_dormhisao
show phone mobile:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with locationchange
with Pause (0.5)

hide phone
with None

# "After a few minutes, we end up saying our goodbyes and I set my phone on my desk."
"ผ่านไปสองสามนาทีเราก็บอกลากัน ฉันวางโทรศัพท์ลงกับโต๊ะ"

# "Compared to Hanako's situation, mine feels utterly mundane. I still have both of my parents, I had a reasonably normal childhood, and unlike many in Yamaku, my condition isn't immediately visible to the public."
"ถ้าให้เทียบกับฮานาโกะแล้วชีวิตฉันตอนนี้ช่างเอื่อยเฉื่อย พ่อแม่ฉันก็ยังอยู่ ชีวิตวัยเด็กก็ปกติดี และอาการของฉัน\nก็ไม่ได้ปรากฏแก่สายตาคนอื่นทันที ไม่เหมือนอย่างนักเรียนหลาย ๆ คนในยามากุ"

# "But then again… isn't this just an attempt to justify the way I've been acting towards her?"
"แต่ว่า… ที่ฉันคิดแบบนี้มันก็แค่การหาข้ออ้างให้ฉันทำตัวแบบนั้นกับฮานาโกะได้นี่"

# "That may well be what our pasts were like, but when it comes to the future I still have no idea what I want to do. In school I've just concentrated on each day's work, and I've put off more and more things to cater to Hanako."
"อดีตของพวกเราเป็นเช่นนั้น แต่พอพูดถึงเรื่องอนาคตแล้วฉันก็ยังไม่รู้ว่าจะทำอะไร ฉันเรียนโดยจดจ่ออยู่กับภาระงาน\nในแต่ละวันโดยเอาแต่ผัดสิ่งต่าง ๆ ที่คิดจะทำเพื่อดูแลฮานาโกะออกไปเรื่อย ๆ"

# "I recall the words Mutou told me after Hanako's breakdown; about the purpose of Yamaku and my education. In hindsight, he was probably trying to push exactly the same thing."
"ฉันย้อนนึกถึงคำพูดที่ครูพูดกับฉันหลังจากที่ฮานาโกะแพนิกกำเริบครั้งนั้นที่ว่าด้วยจุดประสงค์ของยามากุ\nกับการศึกษาของฉัน พอลองมาคิดดูตอนนี้แล้วครูก็น่าจะต้องการบอกสิ่งเดียวกันกับสิ่งที่ลิลลี่พูด"

# "Just what have I been doing in the time since my heart attack? If I ever did manage to get Hanako out of her room and to open up, what then?"
"พอฉันหัวใจวายแล้วเอาเวลาหลังจากนั้นไปทำอะไรหมด ถ้าฉันทำให้ฮานาโกะออกมาจากห้องแล้วเปิดใจได้\nแล้วจะเอายังไงต่อ"

# "I look out of my dormitory window as the sun slowly sets. It's a nice sight, but what I really savor is the quiet as the students return to their dormitory rooms."
"ฉันหันมองไปทางหน้าต่างห้องดูพระอาทิตย์ที่คล้อยตกดิน เป็นภาพที่สวยงาม แต่สิ่งที่ฉันดื่มด่ำอยู่เป็นความเงียบ\nในระหว่างที่นักเรียนต่างกลับห้องของตัวเองกัน"

# "All I want to do now is think. I'm not sure how much time I have, but I want to work out where I'll go from here."
"ตอนนี้ฉันอยากคิดก่อน ไม่รู้ว่าฉันเหลือเวลาอีกเท่าไหร่ แต่ฉันอยากคิดวางแผนว่านับจากนี้จะทำอะไรต่อไป"

scene black
with dissolve

# To H25, Good End


label th_H22b:

stop music fadeout 5.0

# "I listen carefully to what Lilly has to say, but I can't bring myself to agree with her."
"ฉันตั้งใจฟังสิ่งที่ลิลลี่พูด แต่ฟังอย่างไรก็เห็นด้วยไม่ลง"

# "Hanako is a delicate person at the best of times, and after what happened when her birthday was brought up, I think this is the very last situation where we should be leaving her alone if she's deliberately secluding herself."
"ตอนที่ฮานาโกะปกติดีก็เป็นคนบอบบางอยู่แล้ว และพอได้เห็นสิ่งที่เกิดขึ้นหลังจากมีการพูดถึงวันเกิดของเธอ\nฉันก็คิดว่าตอนนี้ไม่ใช่สถานการณ์ที่เราจะปล่อยให้ฮานาโกะอยู่คนเดียวได้ถ้าเธอเป็นคนปลีกตัวออกไปเอง"

# "It feels like Lilly has a very definite image of how best to deal with Hanako in her mind, though. Not just now, but in all the time that I've known the two."
"แต่ฉันรู้สึกเหมือนลิลลี่จะมีแผนในหัวชัดว่าจะต้องรับมือกับฮานาโกะอย่างไร ไม่ใช่แค่ตอนนี้หรอก แต่เป็นทุกครั้ง\nเท่าที่ฉันรู้จักทั้งสองคนมาเลย"

# "I mull over the best course of action in my head, and find myself trying to verbally agree with Lilly as softly and as ambivalently as I can."
"ฉันครุ่นคิดถึงทางออกที่ดีที่สุดในหัวแล้วพูดตอบเห็นด้วยกับลิลลี่ไปอย่างนุ่มนวลและก้ำกึ่งที่สุดเท่าที่จะทำได้"

# "We make some smalltalk afterwards, but neither of us really has much stomach for it in the light of recent events. We say our goodbyes before I hang up."
"จากนั้นเราก็คุยกันเรื่อยเปื่อย แต่เราทั้งสองคนต่างไม่มีใครมีอารมณ์จะคุยเท่าไหร่ด้วยเหตุการณ์ที่เกิดขึ้นล่าสุดนี้\nเราบอกลากันก่อนฉันจะกดวางสาย"

show phone mobile:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with None

scene bg school_dormhisao
show phone mobile:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with locationchange
with Pause (0.5)

hide phone
with None

# "I want to talk to Hanako myself, to help her as best I can. The best thing for her right now would be to have someone close to her, not to be left alone."
"ฉันอยากจะไปคุยกับฮานาโกะด้วยตัวเองเพื่อจะได้ช่วยให้สุดความสามารถ สิ่งที่ดีกับตัวฮานาโกะที่สุดในตอนนี้\nคือการที่มีคนอยู่เคียงข้าง ไม่ใช่การถูกทิ้งไว้คนเดียว"

#no black, this connects directly

#To H23, Rage End


label th_H22c:

stop music fadeout 5.0

# "I listen carefully to what Lilly has to say, but I can't bring myself to agree with her."
"ฉันตั้งใจฟังสิ่งที่ลิลลี่พูด แต่ฟังอย่างไรก็เห็นด้วยไม่ลง"

# "I want to be with Hanako more. I want to be a better friend to her, to support her when she needs support, and to be there when she most needs people. I think that now is one of those times."
"ฉันอยากอยู่กับฮานาโกะให้มากกว่านี้ อยากจะเป็นเพื่อนที่ดีกว่านี้สำหรับเธอ คอยเป็นกำลังให้ยามที่เธอต้องการ\nคอยอยู่เคียงข้างยามที่เธออยากอยู่กับใครสักคน ซึ่งฉันคิดว่าตอนนี้แหละคือช่วงเวลาที่ว่าเหล่านั้น"

# "The memory of the store owner we met in town together still puts me off. Anyone who takes even the slightest glance at Hanako ends up staring, and to fault them for it would be completely hypocritical, given my own reaction."
"ฉันยังไม่สบายใจกับความทรงจำของเจ้าของร้านคนนั้นที่เราเจอตอนไปเที่ยวในตัวเมืองด้วยกัน ใครที่\nได้เห็นฮานาโกะแม้เพียงมองผ่าน ๆ เป็นต้องจ้องมอง แต่หากจะกล่าวโทษพวกเขาเหล่านั้นแล้วก็คงเป็นอะไร\nที่ย้อนแย้ง เพราะฉันเองก็มีปฏิกิริยาแบบเดียวกัน"

# "I don't like my own scarring either, but at least I can cover it up with something as simple as a shirt. I can't imagine a life where every day would be spent trying to hide myself as much as possible."
"ฉันก็ไม่ชอบแผลเป็นของตัวเองเหมือนกัน แต่อย่างน้อยก็ปกปิดได้ง่าย แค่ใส่เสื้อก็จบแล้ว ฉันนึกภาพไม่ออกเลย\nว่าชีวิตที่ต้องปกปิดร่างกายตัวเองให้มิดชิดที่สุดอยู่ทุกวันนั้นเป็นอย่างไร"

# "And on top of that, Hanako doesn't even have people around her that would support her no matter what she looks like. I live away from my parents, but I can still contact and visit them when I wish."
"และยิ่งไปกว่านั้นฮานาโกะก็ไม่มีคนรอบตัวที่จะคอยสนับสนุนเธอโดยไม่สนว่ารูปลักษณ์จะเป็นอย่างไรด้วย ฉันอยู่ห่าง\nจากพ่อแม่ก็จริง แต่ถ้าจะติดต่อหรือไปหาก็ย่อมทำได้"

# "I mull over the best course of action in my head, and find myself trying to verbally agree with Lilly as softly and as ambivalently as I can."
"ฉันครุ่นคิดถึงทางออกที่ดีที่สุดในหัวแล้วพูดตอบเห็นด้วยกับลิลลี่ไปอย่างนุ่มนวลและก้ำกึ่งที่สุดเท่าที่จะทำได้"

# "We make some smalltalk afterwards, but the both of us don't really have much stomach for it in the light of recent events. We say our goodbyes before I hang up."
"จากนั้นเราก็คุยกันเรื่อยเปื่อย แต่เราทั้งสองคนต่างไม่มีใครมีอารมณ์จะคุยเท่าไหร่ด้วยเหตุการณ์ที่เกิดขึ้นล่าสุดนี้\nเราบอกลากันก่อนฉันจะกดวางสาย"

show phone mobile:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with None

scene bg school_dormhisao
show phone mobile:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with locationchange
with Pause (0.5)

hide phone
with None

# "There is at least one thing I can do for Hanako. If I make this small gesture for her, I can only hope that she allows me to come that little bit closer."
"ยังมีอย่างหนึ่งที่ฉันพอจะทำเพื่อฮานาโกะได้ ถ้าส่งสัญญาณเล็ก ๆ นี้ให้เธอแล้วฉันก็คงได้แต่เฝ้าหวังว่าเธอจะเปิดใจ\nให้ฉันใกล้ชิดกับเธอให้มากขึ้นอีกสักเล็กน้อย"

# To H24, Sad End

#-----------------

label th_H23:

#Bad End 1 - Rage End

scene bg school_dormhanako_ni
show hanako_door_base at right
show hanako_door_door at left
with shorttimeskip

play sound sfx_hammer
# Three knocks while being harsher than sfx_doorknock2. sfx_doorknock is more than thrice. - Raide

play music music_tragic fadein 0.5

# "I rap my knuckles thrice on Hanako's door. As expected, there's no answer. I briefly consider knocking again, but I know full well that I'd get just the same result if I did."
"ฉันเคาะประตูห้องฮานาโกะสามครั้ง ไม่มีเสียงตอบรับตามคาด ฉันนึกชั่งใจครู่หนึ่งว่าจะเคาะอีกครั้งดีไหม แต่ก็รู้ดี\nว่าต่อให้เคาะไปก็คงได้ผลอย่างเดิม"

# "Resting my hand on Hanako's door handle, I try and prepare what I want to say to her. Try as I might, I can't really think of anything worth saying. I want to comfort her, yes, but I have no idea how to do that."
"ฉันจับมือจับประตูห้องฮานาโกะพลางคิดเตรียมไว้ว่าจะพูดอะไรกับเธอดี แต่เค้นสมองเท่าไหร่ก็นึกเรื่องที่จะพูดไม่ออก\nจริงอยู่ว่าฉันอยากปลอบเธอ แต่ก็ไม่รู้ว่าจะต้องทำอย่างไร"

# "That alone is almost enough to stop me. I told Lilly that I would, though, so I feel I have to follow through, whether I'm confident about it or not."
"คิดแค่นั้นฉันก็ไม่อยากไปต่อแล้ว แต่ในเมื่อบอกลิลลี่ไปแล้วฉันก็ต้องไปให้สุดทาง ไม่ว่าจะแน่ใจหรือไม่ก็ตาม"

# "I turn the handle downwards, with a large amount of hesitation. It doesn't move far though, due to the door being locked."
"ฉันบิดมือจับลงทั้งที่ในใจยังเต็มไปด้วยความลังเล แต่ก็บิดได้ไม่มากเพราะประตูล็อกไว้"

# hi "Hanako…"
hi "ฮานาโกะ…"

# "So she really has locked me out. After everything that happened between us, and the time that we spent together… she's shut me out completely."
"ก็คือกีดฉันออกแล้ว ทุกเหตุการณ์ที่เราผ่านมาด้วยกัน ช่วงเวลาที่เราได้อยู่ด้วยกัน… เธอกลับปิดกั้นฉันไปโดยสมบูรณ์"

# hi "Um… I don't know if you can hear me, but…"
hi "เอ่อ… ไม่รู้ว่าเธอได้ยินหรือเปล่า แต่ว่า…"

# hi "I just want to talk to you a bit. If you can hear me, could you unlock the door?"
hi "ฉันอยากคุยกับเธอหน่อย ถ้าได้ยินก็มาเปิดประตูให้หน่อยได้ไหม"

with Pause(4.0)

play sound sfx_lock

# "I wait in silence. Minutes pass, but eventually I hear footsteps coming to the door and the lock being worked."
"ฉันรออยู่เงียบ ๆ ผ่านไปหลายนาทีก็มีเสียงฝีเท้าเดินมาที่ประตู ตามด้วยเสียงปลดล็อก"

# "At least she's willing to hear me out. That's one good thing."
"อย่างน้อยก็ยังดีที่ยอมรับฟังกันละนะ"

# hi "I… I don't really know what to say, but… I just wanted to see you. I wanted to make sure you're all right."
hi "ฉัน… ฉันไม่รู้ว่าจะพูดอะไรดี แต่… ฉันอยากเจอเธอ อยากดูให้แน่ใจว่าเธอไม่เป็นอะไร"

# "I take a breath before pushing the handle down and opening the door. If she unlocked it without raising any protest, it should be fine for me to go in."
"ฉันสูดหายใจแล้วบิดมือจับเปิดประตู ถ้าปลดล็อกให้โดยไม่แย้งอะไรก็คงแปลว่าเข้าไปได้"

play sound sfx_door_creak

show hanako_door_door:
   easeout 1.0 xpos -0.2
show hanako_door_base:
   easeout 1.0 xpos 1.1
show bg school_dormhanako_ni:
   center
   easeout 1.0 xpos 0.55
with None

scene bg school_dormhanako
show hanagown distant:
    center
    ypos 1.15
with silentwhiteout

# "Hanako is sitting on the side of her bed, her face sullen as though deep in thought. Her room is as stark as ever, and right now, she seems to perfectly suit the mood it gives off."
"ฮานาโกะนั่งอยู่ที่ริมเตียงพร้อมสีหน้าหม่นหมองคล้ายกำลังคิดอะไรอยู่ ห้องยังคงเปล่าเปลือยเช่นเคย และตอนนี้เธอ\nก็ดูเข้ากันกับอารมณ์ของห้องมาก"

show hanagown normal
with charachange

show hanagown worry at center
with Dissolvemove(0.2)

# "Eventually, her eyes slowly move to the door. As soon as she notices my presence, she darts off her bed and jumps to her feet, facing me straight-on."
"จนในที่สุดฮานาโกะก็ค่อย ๆ เหล่ตามามองที่ประตู ทันทีที่เห็นว่าฉันเข้ามาก็เด้งตัวออกจากเตียงลุกขึ้นยืน\nประจันหน้าฉัน"

# "Her oversized gown makes this gesture look all the more sweeping as it freely moves about her light frame."
"ชุดนอนหลวมโพรกที่พลิ้วไปตามร่างบางของเธออย่างอิสระนั้นยิ่งทำให้การขยับตัวของเธอนั้นดูยิ่งใหญ่"

# ha "Wh-what are you…?"
ha "นะ-นี่นาย…"

# "I quickly regret coming in as I look at her. She looks depressed, but there's a tinge of anger behind it. So, she can make this kind of expression as well."
"ฉันนึกเสียใจที่เข้ามาทันทีที่เห็นหน้าฮานาโกะ เธอดูเศร้า แต่ก็มีความโกรธเจืออยู่ด้วย ทำสีหน้าแบบนี้เป็นด้วยสินะ"

# hi "I… I just wanted to check that you were all right. I thought it would be okay, since you unlocked the door."
hi "ฉัน… ฉันแค่อยากมาดูว่าเธอโอเคดีหรือเปล่า เห็นปลดล็อกประตูก็นึกว่าให้เข้ามาได้"

show hanagown distant_blush
with charachange

# "Hanako opens her mouth to speak, but quickly closes it again before looking away."
"ฮานาโกะอ้าปากจะพูด แต่ก็ปิดปากไปแล้วเบือนหน้าหนี"

show hanagown distant_blush:
    center
    ypos 1.15
with charamove

# "We stand in silence for a while, before she steps back and sits down on the side of her bed. I'm not sure whether she's frustrated with me and resigned to the fact that I'm here, or genuinely okay with me being in her room."
"เรายืนอยู่เงียบ ๆ กันพักหนึ่งก่อนที่ฮานาโกะจะถอยกลับไปนั่งที่ริมเตียง ฉันไม่แน่ใจว่าเธอหงุดหงิดแล้วทำใจยอมรับ\nให้ฉันอยู่ในห้องไปหรือให้ฉันอยู่ในห้องได้จริง ๆ"

# "Once again, I find myself completely unable to work out how she feels. It's annoying."
"เป็นอีกครั้งที่ฉันเดาใจไม่ถูกเลยว่าฮานาโกะรู้สึกอย่างไรอยู่ น่ารำคาญชะมัด"

# "I end up walking to her desk chair and taking a seat. I do it slowly, to allow her time to raise any issue she might have with me sticking around, but she doesn't say anything. All she does is stare at the ground, not moving a muscle."
"ฉันเดินไปที่โต๊ะฮานาโกะแล้วนั่งลงที่เก้าอี้โดยค่อย ๆ ทำทุกอิริยาบถเพื่อให้เวลาเธอได้ท้วงติงถ้าไม่อยากให้ฉัน\nอยู่ด้วย แต่เธอก็ไม่พูดอะไร ฮานาโกะเอาแต่จ้องกับพื้นอยู่นิ่ง ๆ ไม่ไหวติง"

# "After sitting with my front to the chair's back, I take a better look at Hanako. She appears pale, but her cheeks look red. I'm not sure she's been eating well, either, given how thin her frame looks."
"พอนั่งแบบหันหน้าเข้าพนักพิงแล้วฉันก็มองฮานาโกะให้ชัด ๆ ดูซีด ๆ แต่แก้มแดงอยู่ ไม่แน่ใจด้วยว่าได้กินอะไร\nให้เป็นเรื่องเป็นราวหรือเปล่าเพราะผ่ายผอมไปขนาดนี้"

# "Lilly might have said it would be better if I kept more of a distance from her, but it's hard to think of that as the correct way to deal with Hanako when she looks like this."
"ลิลลี่พูดว่าให้รักษาระยะห่างกับฮานาโกะไว้จะดีกว่าก็จริง แต่ฉันก็แทบไม่อยากเชื่อเลยว่าวิธีนั้นจะถูกต้องแล้ว\nกับการรับมือฮานาโกะในสภาพนี้"

# "She keeps looking at the ground without a word, as if waiting for me to say something. It's entirely reasonable, since I'm the one who came into her room."
"ฮานาโกะก้มหน้ามองพื้นไม่พูดอะไรคล้ายรอให้ฉันพูดอะไรบางอย่าง ซึ่งก็สมเหตุสมผลเพราะฉันเป็นคนเข้ามา\nในห้องเธอเอง"

# hi "Want to go out somewhere? Going down the hill to town might be a bit much, but we could at least go for a walk outside."
hi "อยากออกไปไหนไหม เดินลงเขาไปอาจจะไกลหน่อย แต่อย่างน้อยไปเดินข้างนอกกันก็ได้"

show hanagown worry_blush
with charachange

# ha "Why… do you want to do that?"
ha "ทำไม… ถึงอยากเดิน"

# hi "I was just thinking that it might help you a bit. You spend so much time inside, your skin's going to get as pale as Lilly's before long."
hi "แค่คิดว่าเดินแล้วเธออาจจะรู้สึกดีขึ้นหน่อยน่ะ เอาแต่อยู่ในห้องแบบนี้เดี๋ยวผิวได้ซีดเหมือนลิลลี่พอดี"

show hanagown distant_blush
with charachange

# "I snort in amusement, expecting Hanako to do the same, but she gives no reaction; she just goes back to looking at the ground."
"ฉันแค่นหัวเราะหวังให้ฮานาโกะหัวเราะตาม แต่เธอก็ไม่ตอบสนองอะไร เพียงแต่กลับไปก้มมองพื้นเหมือนเดิม"

# ha "If you don't want to go… I-I don't want to go either."
ha "ถ้านายไม่อยากไป… ฉะ-ฉันก็ไม่อยากไป"

# hi "It's fine. I played soccer and hung out with friends after school a lot before coming to Yamaku, so I like being outdoors."
hi "ไม่เป็นไรน่า ก่อนที่มายามากุนี่ฉันก็เล่นฟุตบอลกับไปเฮฮากับเพื่อนหลังเลิกเรียนออกจะบ่อย นี่แหละ\nฉันถึงได้ชอบอยู่ข้างนอก"

# "Hanako shows no visible reaction. It's hard to talk to her when the discussion is so one-sided."
"ฮานาโกะไม่แสดงปฏิกิริยาใด ๆ ให้เห็น พอพูดอยู่ฝ่ายเดียวแล้วก็คุยลำบากแฮะ"

# hi "We could go to the library… uh, if it wasn't closed by about now. The gardens would be fine, though."
hi "จะไปห้องสมุดกันก็ได้นะ… เอ่อ ถ้าตอนนี้มันยังไม่ปิดอะนะ หรือจะไปที่สวนก็ได้เหมือนกัน"

# "She begins to play with her hair. It's distracting, and strikes me as a little unusual for her."
"ฮานาโกะเริ่มจับผมเล่น เห็นแล้วเสียสมาธิและยังดูไม่สมเป็นเธออยู่หน่อย ๆ"

# "Then again, since the incident in class happened, I've been tiptoeing around her for fear of hurting her like that again. Actively trying to get her outside might be a good thing."
"แต่ก็นะ ตั้งแต่ที่เกิดเรื่องในห้องครั้งนั้นฉันก็ระวังตัวกับฮานาโกะตลอดเพราะกลัวว่าจะไปทำร้ายเธอแบบนั้นอีก\nการชวนให้ฮานาโกะออกไปข้างนอกบ่อย ๆ อาจเป็นสิ่งที่ดีก็ได้"

# "I lean forward a bit more in the chair and give her a slightly forced smile, to try and lighten the mood a little."
"ฉันโน้มตัวเข้าไปอีกแล้วยิ้มฝืน ๆ ให้ฮานาโกะด้วยหวังว่าจะช่วยให้บรรยากาศผ่อนคลายลงบ้าง"

# hi "There wouldn't be anyone around by now, so you wouldn't have to worry about someone getting in our way. It could be a little date or something."
hi "ตอนนี้น่าจะไม่มีใครอยู่ข้างนอก เพราะงั้นก็ไม่ต้องกลัวว่าจะมีใครมาขัด นับเป็นเดตเล็ก ๆ หรืออะไรแบบนั้นก็ได้"

show hanagown normal
with charachange

# "I give a small chuckle, but catch myself as Hanako stops playing with her hair and grips the bed tightly. Hanako's mouth moves, but try as I might, I can't pick out what she's mumbling."
"ฉันแค่นหัวเราะเบา ๆ แต่ก็ต้องชะงักไปเมื่อเห็นว่าฮานาโกะหยุดจับผมแล้วกำเตียงแน่น เธอขยับปาก แต่ต่อให้\nเงี่ยหูฟังเท่าไหร่ก็ฟังไม่ออกว่าพึมพำอะไรอยู่"

# hi "Hanako?"
hi "ฮานาโกะ"

# ha "You… don't understand…"
ha "นาย… ไม่เข้าใจ…"

# "Even now, I can only barely understand what she says. It feels like she's trying to make her presence as small as possible; that's incredibly natural for her to do in class or around others, but it hurts when she tries it around me."
"ตอนนี้ฉันก็ยังแทบฟังไม่รู้เรื่องด้วยซ้ำว่าฮานาโกะพูดอะไร เหมือนเธอกำลังย่อส่วนตัวตนตัวเองให้เล็กที่สุดเท่าที่\nจะทำได้ ซึ่งเธอก็ทำแบบนี้ประจำตอนอยู่ในห้องเรียนหรือตอนอยู่กับคนอื่น แต่พอมาทำกับฉันแล้วฉันก็เจ็บปวดขึ้นมา"

# hi "I told you, it's fine. It's just a little walk, nobody'll notice us."
hi "ก็บอกแล้วไงว่าไม่เป็นไรหรอก แค่เดินกันนิดหน่อย ไม่มีใครเห็นหรอก"

# "I get out of the chair and walk towards the door, turning back to invite Hanako along. Once again, she doesn't respond at all to what I say."
"ฉันลุกจากเก้าอี้เดินไปที่ประตูแล้วหันมาชวนให้ฮานาโกะตามมาด้วย แต่เธอก็ไม่ตอบสนองอะไรกับสิ่งที่ฉันพูด\nเหมือนเดิม"

show hanagown distant
with charachange

# ha "I don't…"
ha "ฉันไม่…"

# hi "Going outside for a bit is good for clearing your head."
hi "ออกไปสูดอากาศข้างนอกแล้วสมองจะได้ปลอดโปร่งไง"

# ha "Why do you… want to do this…"
ha "ทำไมนาย… ถึงอยากทำแบบนี้…"

# hi "Because I want to help you."
hi "เพราะอยากช่วยเธอไง"

# ha "I don't… want… help. Did you just come here… to try and get me out…?"
ha "ฉันไม่… อยากให้ใคร… มาช่วย นายมาที่นี่แค่เพื่อจะ… ลากฉันออกไปข้างนอกเหรอ…"

# hi "I don't mind. I think everyone needs help sometimes. When I was trying to get through my first days at Yamaku, you and Lilly helped me a lot."
hi "ไม่เห็นเป็นไรเลย ฉันว่าคนเราบางทีก็ต้องให้คนอื่นมาช่วยบ้าง ตอนฉันมาอยู่ที่ยามากุใหม่ ๆ ก็ได้เธอกับลิลลี่นี่แหละ\nช่วยไว้"

# hi "Besides, I'm not exactly busy."
hi "อีกอย่าง ฉันก็ไม่ได้มีธุระอะไรด้วย"

# ha "I don't w-want to go. I'm… fine."
ha "ฉันไม่ยะ-อยากไป ไม่… เป็นไร"

# hi "I don't really think it's healthy to stay indoors that long. The sun's still got a little life in it, so it's not too late to have at least a little walk."
hi "ฉันว่าเอาแต่หมกตัวอยู่ในห้องแบบนี้นาน ๆ มันไม่ดีต่อร่างกายนะ ตอนนี้ยังพอมีแดดอยู่ ไปเดินกันสักหน่อย\nก็ยังทัน"

# hi "I could probably use a bit of exercise anyway, to help wake me up. I've got some homework to get done, and it wouldn't be good to fall asleep halfway through doing it."
hi "ฉันก็จะได้ออกกำลังกายสักหน่อยให้หายง่วง ยังมีการบ้านที่ต้องทำอีก ขืนหลับไปตอนทำการบ้านคงไม่ดีแน่"

show hanagown normal
with charachange

# ha "Then… go."
ha "งั้นก็… ไปสิ"

# hi "By myself?"
hi "ไปแค่ฉัน?"

# "She nods."
"ฮานาโกะพยักหน้า"

# hi "Well, I'm not really against that, but… are you sure? I swung by to invite you to come with me."
hi "อืม ก็ไม่ได้อะไรหรอก แต่ว่า… แน่ใจนะ ฉันแวะมาชวนเธอออกไปเดินด้วยกันเนี่ย"

show hanagown distant
with charachange

# ha "I'm fine. You can go."
ha "ไม่เป็นไร นายไปเถอะ"

# hi "Come on, just a small walk."
hi "ไม่เอาน่า เดินนิดหน่อยเอง"

# ha "Please, just go. I-I'm fine here."
ha "ขอร้องละ ไปเถอะ ฉะ-ฉันอยู่ที่นี่ได้"

# hi "…Hanako?"
hi "…ฮานาโกะ?"

# "I try to look at her face to gauge her feelings, but her expression is wooden. As if it was so carefully arranged, that a single movement might cause it to collapse."
"ฉันลองมองหน้าฮานาโกะดูว่าเธอรู้สึกอย่างไร แต่สีหน้าของเธอนั้นแข็งทื่อราวกับว่าจัดวางมาอย่างดีแล้ว\nและหากมีอะไรเคลื่อนแม้เพียงเล็กน้อยก็พังได้"

# hi "Well, if you want to stay here… maybe we could play a game?"
hi "งั้นถ้าอยากอยู่ที่นี่… เล่นเกมกันไหม"

# ha "Just leave. Please. I don't… want to do anything right now."
ha "ไปเถอะ ขอร้องละ ตอนนี้ฉัน… ไม่อยากทำอะไร"

# hi "Surely there's something you want to do. It must be boring, sitting here in your room alone."
hi "ต้องมีอะไรที่เธออยากทำสิ นั่งอยู่ในห้องคนเดียวแบบนี้เบื่อตายชัก"

# ha "I want you to go."
ha "ฉันอยากให้นายไป"

# hi "Come on, you don't have to be like that. I just want to spend some time with you. Lilly and I are worried, so…"
hi "ไม่เอาน่า อย่าพูดแบบนั้นสิ ฉันแค่อยากใช้เวลาอยู่กับเธอสักหน่อย ลิลลี่กับฉันก็เป็นห่วงเธอ…"

show hanagown worry_blush
with charachange

# ha "You… talked to her?"
ha "นาย… คุยกับลิลลี่?"

# hi "Uh… yeah. We were… on the phone, just a little while ago. We're both really worried about you."
hi "อ่า… อื้ม คุย… โทรศัพท์กันน่ะ เมื่อกี้นี่เอง เราสองคนเป็นห่วงเธอมากนะ"

show hanagown irritated
with charachange

# "Hanako mumbles to herself again. It's increasingly disturbing."
"ฮานาโกะพึมพำกับตัวเองอีกครั้ง ยิ่งดูยิ่งชวนขนลุกเรื่อย ๆ"

# hi "Hanako…?"
hi "ฮานาโกะ…?"

# ha "I'm telling you… please, go away. You don't understand anything…"
ha "ขอร้องละ… ได้โปรดเถอะ ไป นายไม่เข้าใจอะไรหรอก…"

# hi "If we just had a talk, you could tell me what I don't understand. I just want to protect you, I don't really see…"
hi "ถ้าคุยกันเธอก็จะได้บอกฉันไงว่าฉันยังไม่เข้าใจอะไร ฉันอยากปกป้องเธอนะ ฉันไม่รู้ว่า…"

# ha "Get… out, p-please…"
ha "ออก… ไป ขะ-ขอร้อง…"

# hi "Just locking yourself in your room again isn't going to help anything, Hanako. Please…"
hi "อุดอู้อยู่แต่ในห้องมันไม่ได้ทำให้อะไรดีขึ้นมาหรอกฮานาโกะ ขอร้อง…"

stop music fadeout 2.0

# "Silence."
"เงียบ"

# hi "Hanako, I just want to help you—{w=0.3}{nw}"
hi "ฮานาโกะ ฉันแค่อยากจะช่วยเธอ—{w=0.3}{nw}"

scene ev hanako_rage:
    truecenter
    subpixel True zoom 3.0
    0.25
    linear 0.2 zoom 1.05
    easein 8.0 zoom 1.0
with flash

play music music_rain

# "She suddenly storms off her bed, turning to me with an expression that takes me completely off guard."
"ฮานาโกะพุ่งตัวออกมาจากเตียงแล้วมองฉันด้วยสีหน้าที่ทำให้ต้องตกตะลึง"

# ha "Get out of my room, get out of my room, get out of my room…!" with vpunch
ha "ออกไปจากห้องฉันนะ ออกไปจากห้องฉันนะ ออกไปจากห้องฉันนะ…!" with vpunch

# "Hanako yells at me with such force that, for the first time in a long time, I feel genuinely frightened. I… I have no idea how to react to this, and from Hanako of all people."
"ฮานาโกะตะเบ็งเสียงดังชนิดที่ว่าฉันพรั่นพรึงขึ้นมาจริง ๆ ซึ่งฉันไม่ได้สัมผัสความรู้สึกแบบนี้มานานแล้ว ฉัน…\nฉันไม่รู้ว่าจะต้องไปยังไงต่อ ยิ่งต้นทางมาจากฮานาโกะด้วย"

# ha "Leave! I'm telling you, go!" with vpunch
ha "ออกไป! ฉันบอกให้ไปไง!" with vpunch

# hi "B-but… I was just trying to… help you…"
hi "ตะ-แต่… ฉันแค่จะ… ช่วยเธอ…"

# ha "I know I need help! I know I'm broken! I don't need you to tell me that!" with vpunch
ha "รู้น่าว่าฉันต้องให้คนอื่นมาช่วย! รู้น่าว่าฉันมันแหลกสลาย! ไม่ต้องบอกกันก็ได้!" with vpunch

# hi "I never said you were broken, or anything like that!"
hi "ฉันไม่เคยบอกว่าเธอแหลกสลายหรืออะไรเลยนะ!"

# ha "It's written on your face, it's written on Lilly's face, it's written on everybody's faces!" with vpunch
ha "แต่สีหน้านายบอกงั้นนี่ สีหน้าลิลลี่ก็บอกงั้น สีหน้าทุกคนก็บอกงั้น!" with vpunch

# ha "I see a therapist every week, Lilly dotes on me as if I were her child, and now… even you!" with vpunch
ha "ฉันต้องพบจิตแพทย์ทุกสัปดาห์ ลิลลี่ก็เอาใจฉันเหมือนเป็นลูก แล้วทีนี้… นายยังจะ!" with vpunch

# ha "Nothing's changed, nothing at all! I hate Lilly, and I… I hate you more than anyone…!" with vpunch
ha "เหมือนเดิม เหมือนเดิมทุกอย่าง! ฉันเกลียดลิลลี่ แล้วฉัน… ฉันก็เกลียดนายกว่าใครด้วย…!" with vpunch

# "Her face moves in strange, almost grotesque ways. I've never seen someone completely lose it before, but it looks like the usually quiet and withdrawn girl in front of me is going into just such a destructive cycle before my eyes."
"หน้าฮานาโกะบิดเบี้ยวไปชวนสยอง ฉันไม่เคยเห็นใครตบะแตกแบบนี้มาก่อน เหมือนว่าหญิงสาวที่ปกติจะเป็นคนเงียบ ๆ\nและเก็บตัวตรงหน้าฉันคนนี้จะเข้าสู่โหมดทำลายล้างต่อหน้าต่อตาฉันแล้ว"

# "I don't know what to do. I have no idea what I should say or do."
"ฉันไม่รู้ว่าต้องทำอย่างไร ไม่รู้เลยว่าควรจะพูดหรือทำอะไรดี"

# ha "Go! Leave me alone! Get out of here!" with vpunch
ha "ไป! ไสหัวไป! ออกไปได้แล้ว!" with vpunch

# "I take a step back, then another, and then another. My retreat is only halted when I feel the door against my back."
"ฉันถอยไปหนึ่งก้าว สองก้าว และสามก้าว ฉันต้องหยุดเมื่อหลังชนประตูแล้ว"

# "I can't fix this situation. Nothing I say would change anything, now. I feel like I'm in a strange and deeply unsettling foreign world. I don't want to be here any more."
"ฉันแก้ไขสถานการณ์นี้ไม่ได้แล้ว ตอนนี้ไม่ว่าจะพูดอะไรไปก็คงไม่มีอะไรเปลี่ยน รู้สึกราวกับว่าตัวเอง\nอยู่ในโลกแปลกแยกที่ประหลาดชวนให้อึดอัดเป็นอย่างมาก ฉันไม่อยากอยู่ตรงนี้แล้ว"

# "The door handle fights my clumsy attempts to open the door without turning my back to Hanako. Eventually, thankfully, the handle moves downwards. I open the door as fast as I can and almost leap backwards through it."
"ฉันตีกับมือจับประตูพยายามเปิดโดยไม่หันหลังให้ฮานาโกะอย่างเก้ ๆ กัง ๆ โชคดีที่ในที่สุดก็บิดได้จนได้ ฉันรีบ\nเปิดประตูแล้วโดดพุ่งถอยหลังออกมา"

# "As I go through, I keep my eyes on the girl in front of me."
"ระหว่างที่ออกมาฉันยังคงจ้องเด็กสาวตรงหน้า"

# "She's not broken. Hanako isn't broken. If she was broken, then I'm just as broken as she is after all that's happened to me. Lilly only ever did the best by her, and I only ever tried to protect her as best I could."
"เธอไม่ได้แหลกสลาย ฮานาโกะไม่ได้แหลกสลาย ถ้าเธอแหลกสลายจริงฉันก็คงแหลกสลายพอ ๆ กันกับเธอ\nจากเหตุการณ์ในอดีตทั้งหลาย ลิลลี่ก็ทำสุดเท่าที่ตัวเองจะทำได้ ส่วนฉันก็แค่เพียงปกป้องเธอสุดความสามารถ"

scene ev hanako_rage_sad:
    zoom 1.0
with charachange

# "Hanako looks down, all her energy spent. Now that I've stepped out of her room, the worst of her fury is gone."
"ฮานาโกะก้มหน้าหมดแรง ความโกรธที่ขึ้นถึงขีดสุดของเธอลดลงมาแล้วหลังจากที่ฉันออกมาจากห้อง"

# "But even now, I can't bring myself to argue with her. It's not just the deep shock at what she said… it feels like something else is stopping me. Something deep, that makes me feel physically sick."
"แต่ตอนนี้ฉันก็ยังไม่กล้าเถียงฮานาโกะ ไม่ใช่แค่เพราะตกใจกับคำพูดของเธอ… แต่เพราะรู้สึกว่ามีบางอย่างที่ห้ามฉันไว้\nบางอย่างลึก ๆ ในใจที่ทำให้ฉันรู้สึกไม่สบายตัวขึ้นมา"

show bg school_dormhanako_ni:
   center
   xpos 0.55
   linear 5.0 center
show hanako_door_door:
   left
   xpos -0.2
   linear 5.0 left
show hanako_door_base:
   right
   xpos 1.1
   linear 5.0 right
with flash

stop music fadeout 4.0

# "Without a word, I slowly shut the door. The creak of the old hinges sounds almost deafening."
"ฉันปิดประตูช้า ๆ ไม่พูดอะไร เสียงเอี๊ยดจากบานพับเก่า ๆ นั้นดังเสียดหู"

play sound sfx_doorclose

show bg school_dormhanako_ni at center
show hanako_door_door at left
show hanako_door_base at right
with ease
# "With a final thud, the wooden door closes. The Hanako that I felt I knew disappears behind it, and only faint orange slivers of light peek around the very edges."
"แล้วประตูไม้บานนั้นก็ปิดลงพร้อมเสียงดังปึง ฮานาโกะที่ฉันเคยคิดว่ารู้จักหายไปในประตูบานนั้น มีเพียงแสงสีแสดอ่อน ๆ\nที่ส่องลอดตามขอบประตูออกมา"

scene bg school_girlsdormhall
with locationchange

# "I feel numb. Without anything else to do, I begin the walk back to my dormitory room, mechanically placing one foot in front of the other while barely registering a thing around me."
"ฉันรู้สึกชาดิก ด้วยไม่มีอะไรให้ทำแล้วฉันจึงเดินกลับหอ ขาข้างหนึ่งของฉันก้าวนำขาอีกข้างไปโดยอัตโนมัติ สมองฉัน\nแทบไม่รับรู้สภาพแวดล้อมแล้ว"

# "My mind keeps ticking, questioning everything that I thought I knew about Hanako."
"ในใจฉันตั้งคำถามถึงทุกเรื่องของฮานาโกะที่ฉันเคยคิดว่าตัวเองรู้"

# "But one thing is not questioned; that shutting that door brought a close to more than that single visit."
"แต่อย่างหนึ่งที่แน่แท้ไม่ต้องตั้งคำถาม คือการปิดประตูบานนั้นไม่ได้เป็นการตัดจบเพียงการแวะมาหาของฉันเท่านั้น"

#------------------------

label th_H24:

#Bad End 2 - Sad End

scene bg school_girlsdormhall
with locationchange

play music music_night fadein 4.0

# "After talking to Lilly at the end of the school day, I sat at my desk and looked out the window, idly watching students leaving the school building. Usually they left in groups, but even when they left alone, they'd say goodbye to their friends first."
"หลังจากที่คุยกับลิลลี่ตอนเลิกเรียนแล้วฉันก็มานั่งมองหน้าต่างที่โต๊ะดูนักเรียนที่เดินออกจากอาคารเรียน ปกติ\nจะออกมากันเป็นกลุ่ม หรือถ้าออกมาคนเดียวก็จะบอกลาเพื่อนก่อน"

# "It's completely normal. Something that I would have missed completely, had it been any other day, because it's so mundane."
"เป็นเรื่องปกติสามัญ เป็นเรื่องที่ถ้าเป็นตัวฉันในวันอื่น ๆ ได้มามองแล้วละก็คงไม่เห็น เพราะไม่ได้มีอะไรขนาดนั้น"

# "But it's also something Hanako has never had in the time that I've known her. As I stand outside of Hanako's door for the second time in as many days, that fact doesn't leave my mind."
"แต่ก็เป็นเรื่องที่ฮานาโกะไม่เคยเจอเลยเท่าที่ฉันรู้จักเธอมา ฉันยืนอยู่หน้าห้องฮานาโกะเป็นครั้งที่สองเหมือนอย่าง\nวันอื่น ๆ โดยที่ในหัวยังคงมีเรื่องนั้นอยู่"

# "I hold two plates in my hands. On each is… not exactly the most hearty of meals, but I want to be sure that Hanako is at least feeding herself. It may also be a way to gain a little leverage in getting her to let me in."
"ในมือฉันมีจานอยู่สองใบ ในจานแต่ละใบนั้น… ไม่ได้เป็นอาหารที่ดีเด่อะไร แต่ฉันก็อยากทำให้แน่ใจว่าอย่างน้อย ๆ\nฮานาโกะก็ได้กินข้าวบ้าง แถมอาจจะใช้เป็นสิ่งเล็ก ๆ น้อย ๆ ที่เธอจะรับไว้พิจารณาเพื่อมาเปิดประตูให้ฉันด้วย"

# "Lilly and I have tried our best to be there for her. Ever since she broke down in class, I've dearly wanted to protect Hanako. Such a thing happening to her again, or even something worse, is something I don't want to think about."
"ลิลลี่กับฉันคอยสนับสนุนฮานาโกะสุดความสามารถ ตั้งแต่ที่แพนิกกำเริบในห้องครั้งนั้นฉันก็อยากปกป้องฮานาโกะ\nให้เต็มที่ ฉันไม่แม้แต่จะอยากนึกภาพเลยว่าถ้าเหตุการณ์ทำนองนั้นหรือเลวร้ายยิ่งกว่าอีกเกิดกับเธอจะเป็นอย่างไร"

scene bg school_dormhanako_ni
show hanagown distant_close:
    center
    xpos 0.39
show hanako_door_base at right
show hanako_door_door at left
with locationchange

play sound sfx_doorknock2

# "The door gives a solid series of thuds as I knock on it while carefully propping up one plate on my other arm. I doubt Hanako will open it for me, so all I can really hope to accomplish is to attract her attention."
"ประตูสะท้อนเสียงกึก ๆ เมื่อฉันใช้มือเคาะโดยที่วางจานใบหนึ่งไว้กับแขนอีกข้างอย่างระมัดระวัง ฮานาโกะคงไม่มา\nเปิดให้หรอก ตอนนี้ฉันได้แต่หวังว่าอย่างน้อยก็จะได้ดึงความสนใจเธอบ้าง"

# hi "'Evening, Hanako. It's just me."
hi "สายัณห์หวัดฮานาโกะ ฉันเอง"

# "I pause for a moment to see if she will respond, but the fact that she doesn't isn't very surprising."
"ฉันเว้นช่วงไปรอดูว่าฮานาโกะจะตอบหรือเปล่า แต่ก็ไม่ได้แปลกใจนักเมื่อเธอไม่ตอบจริง ๆ"

# hi "I… I have some food for the both of us. Could I come in?"
hi "ฉัน… ฉันเอาของกินมากินด้วยกันด้วย ขอเข้าไปหน่อยได้ไหม"

# "For what feels like a very long time, some muffled voices from the floor below are the only sound to be heard."
"เวลาผ่านไปเนิ่นนานโดยมีเพียงเสียงอู้อี้ที่ดังมาจากชั้นล่างที่ดังอยู่"

play sound sfx_lock

# "Then I can hear the sound of bare feet on the floor coming up to the door, and I have to stifle a sigh of relief as I hear the door's lock being worked."
"แล้วฉันก็ได้ยินเสียงเท้าเปล่าที่เดินมาทางประตู ฉันต้องห้ามตัวเองไม่ให้ถอนหายใจด้วยความโล่งอกเมื่อได้ยินเสียง\nปลดล็อกประตู"

play sound sfx_dooropen

show hanako_door_door:
   xpos -0.1
with charamove

# "When Hanako opens the door, I look at her intently."
"พอฮานาโกะเปิดประตูแล้วฉันก็จ้องมองเธอ"

show hanagown normal_close
with charachange

# "She looks up momentarily to the plate in my left hand. It's a modest curry dish I quickly made from a packet."
"ฮานาโกะมองมาที่จานในมือซ้ายฉันแวบหนึ่ง ในนั้นเป็นแกงกะหรี่ที่ฉันอุ่นมาจากซองสำเร็จรูป"

show hanagown distant_close
with charachange

# "Her eyes move to the plate in my right hand, which holds the same thing, before looking down again."
"เธอเหลือบมองไปที่จานในมือขวาฉันซึ่งเป็นแกงกะหรี่เหมือนกันก่อนจะก้มหน้าลง"

hide hanagown
with charaexit

# "As she shuffles back into her room, I realize that I haven't said a word to her. I glumly follow her in, slightly embarrassed by having been so wrapped up in observing her."
"ระหว่างที่ฮานาโกะเดินกลับเข้าห้องไปฉันก็เพิ่งนึกได้ว่ายังไม่ได้พูดกับเธอ ฉันเดินตามไปด้วยท่าทีหมอง ๆ\nพลางนึกอายเล็กน้อยที่มัวแต่มองเธอจนไม่ได้พูดอะไร"

play sound sfx_door_creak

show hanako_door_door:
   easeout 1.0 xpos -0.2
show hanako_door_base:
   easeout 1.0 xpos 1.1
show bg school_dormhanako_ni:
   center
   easeout 1.0 xpos 0.55
with None

scene bg school_dormhanako
with silentwhiteout

# "More than ever, the gray and stark atmosphere of Hanako's room feels like a reflection of her personality. The voices from outside become completely inaudible, and the silence inside oppressive, once I close the door."
"บรรยากาศสีเทาทึมในห้องฮานาโกะดูจะสะท้อนลักษณะตัวตนของเธอได้ดีกว่าทุกครั้ง ตอนนี้ไม่ได้ยินเสียง\nจากนอกห้องแล้ว และเมื่อปิดประตูก็เกิดความเงียบที่ชวนให้รู้สึกกดดัน"

# "Walking to the far end of the room, I place the two plates on her desk. I'm thankful that she let me in, but as I turn to face her, I can't help having second thoughts about coming to see her."
"ฉันเดินไปอีกฟากของห้องแล้ววางจานทั้งสองใบลงที่โต๊ะฮานาโกะ แม้จะโล่งใจที่ให้เข้ามาได้ แต่พอหันไปมองเธอ\nแล้วฉันก็อดคิดไม่ได้ว่าดีแล้วจริงหรือที่มาหา"

show hanagown distant:
    center
    ypos 1.15
with charaenter

# "I don't believe Lilly was right, though. Looking at Hanako like this, I can only think that giving her space is the last thing we should be doing. I don't want to imagine it, but she may do something very foolish."
"แต่ก็ไม่อยากเชื่อลิลลี่อยู่ดี เห็นสภาพฮานาโกะอย่างนี้แล้วฉันก็รู้สึกว่าการให้พื้นที่กับเธอคือสิ่งที่ไม่ควรทำเลยต่างหาก\nขืนปล่อยไว้เธออาจทำอะไรที่โง่เง่าลงไปก็ได้ ไม่อยากจินตนาการเลย"

# hi "Um… it's just an instant meal, but it should be filling."
hi "เอ่อ… คือก็เป็นแค่อาหารสำเร็จรูปแหละ แต่น่าจะกินให้อิ่มได้อยู่นะ"

# "I take a plate in my hand, offering it to her. She wordlessly takes it and sits on the side of her bed. I take a seat in her chair, and the familiar sound of eating rings in the room as we dig in with the forks that were stuck into the rice."
"ฉันคว้าจานใบหนึ่งมายื่นให้ฮานาโกะ เธอรับไปเงียบ ๆ แล้วนั่งลงที่ริมเตียง ฉันนั่งลงกับเก้าอี้ที่โต๊ะ จากนั้น\nก็มีเสียงส้อมซึ่งฉันเสียบไว้ในข้าวกระทบกับจานยามทานอาหารอันคุ้นเคยที่ดังสะท้อนอยู่ในห้องตามมา"

# "The curry itself tastes… okay. I wouldn't expect much more from a packet whose brand I didn't recognize, so it not being horrible is at least something."
"รสชาติแกงกะหรี่ก็… ใช้ได้ ฉันไม่ได้คาดหวังอะไรกับของสำเร็จรูปยี่ห้อที่ฉันไม่รู้จักหรอก อย่างน้อย\nไม่ได้รสชาติห่วยแตกก็โชคดีแล้ว"

# "Eating takes the edge off the fact that she isn't talking. Neither of us really likes to talk while we're eating, and this reminds me of the lunchtimes we so often spent together."
"พอได้กินแล้วก็ช่วยเบนสมาธิไปจากความเงียบของฮานาโกะได้บ้าง เราต่างไม่มีใครชอบพูดตอนกินข้าว ชวนให้นึกถึง\nช่วงพักเที่ยงที่เราอยู่ด้วยกันบ่อย ๆ"

# hi "It's kind of nice, eating together like this."
hi "ได้กินข้าวด้วยกันแบบนี้ก็ดีเหมือนกันนะ"

show hanagown worry
with charachange

# "Hanako looks at me quizzically. It's at least a better expression than what she's been wearing this far."
"ฮานาโกะมองฉันด้วยความสงสัย ซึ่งอย่างน้อยก็ดีกว่าสีหน้าที่ฉันเห็นตลอดเมื่อครู่น่ะนะ"

# hi "We became friends mainly over sharing lunch breaks, so it's nice to go back to those times a bit."
hi "หลัก ๆ ที่เราได้เป็นเพื่อนกันก็เพราะอยู่กินข้าวตอนพักเที่ยงด้วยกันนี่แหละ ฉันก็ดีใจที่ได้มาทำอะไร\nเหมือนตอนนั้นบ้าง"

# "She hesitates for a couple of seconds, and I find myself grimacing. Did I say something wrong?"
"ฮานาโกะลังเลอยู่แวบหนึ่ง ฉันทำหน้าเบ้ไปด้วยความสงสัยว่าพูดอะไรพลาดไปหรือเปล่า"

show hanagown smile
with charachange

# "Eventually she smiles and nods. I would normally be very encouraged by this, but her smile looks strange. I can't quite put my finger on why."
"จนสุดท้ายฮานาโกะก็ยิ้มพยักหน้า ปกติฉันคงใจชื้นขึ้นมา แต่รอยยิ้มเธอนั้นดูแปลก ๆ ซึ่งบอกไม่ถูกเหมือนกัน\nว่าเพราะอะไรถึงรู้สึกแบบนั้น"

# ha "Everything's… the same as before, isn't it?"
ha "ยัง… เหมือนเดิมเลยเนอะ"

# hi "Y-yeah. Of course it is."
hi "อะ-อื้ม ก็เหมือนน่ะสิ"

# hi "You've still got Lilly and me to help you and protect you, and once she gets back, everything will be just like she never left."
hi "เธอยังมีลิลลี่กับฉันที่คอยปกป้องอยยู่ แล้วพอลิลลี่กลับมาแล้วทุกอย่างก็จะกลับเป็นเหมือนเดิม เหมือนว่าลิลลี่\nไม่เคยหายไปไหนเลย"

show hanagown distant
with charachange

# "Hanako nods again, her expression remaining exactly the same as before. She feels like a different Hanako from the one I'd first seen when I entered her room, and it's vaguely off-putting."
"ฮานาโกะพยักหน้าอีกรอบด้วยสีหน้าที่ยังเหมือนเดิม เหมือนเป็นคนละคนกับคนที่ฉันเจอตอนเพิ่งเข้าห้องมาเลย\nชักใจคอไม่ดีแล้วสิ"

# "Both of us go back to finishing off our dinners after the short exchange. Despite Hanako looking happier than before, my eyes keep flicking to her as if to reassure myself of this fact."
"หลังจากที่คุยกันนิดหน่อยแล้วเราก็หันไปกินข้าวกันต่อ ทั้งที่ฮานาโกะดูจะสดใสขึ้นแล้วฉันก็ยังอดเหลือบมองเธอ\nเป็นระยะ ๆ ไม่ได้ราวกับจะดูให้แน่ใจว่าเป็นแบบนั้นจริง ๆ"

# "Before long, the last of Hanako's curry is cleared. I finish the last of mine as she puts the empty plate on the desk, and place my own empty plate and used fork on top of hers."
"ไม่นานฮานาโกะก็กินแกงกะหรี่จนหมด เธอหยิบจานมาวางที่โต๊ะจังหวะที่ฉันกินคำสุดท้ายพอดีแล้ววางจานเปล่า\nของตัวเองกับส้อมที่ใช้แล้วไว้บานจานของฮานาโกะ"

# "I briefly wonder what I should say, desperately wanting to avoid another awkward silence or the prospect of leaving her room after so short a time, but Hanako is the one to speak up first."
"ฉันเค้นสมองคิดอยู่ครู่หนึ่งว่าจะพูดอะไรดีด้วยไม่อยากให้เกิดความเงียบอันน่าอึดอัดนั้นอีก และยังไม่อยาก\nออกจากห้องไปทั้งที่เพิ่งเข้ามาด้วย แต่ฮานาโกะเป็นฝ่ายพูดขึ้นมาก่อน"

show hanagown worry_blush
with charachange

# ha "I… I was wondering… since y-you're here…"
ha "ฉัน… ฉันคิดอยู่ว่า… ไหน ๆ นะ-นายก็มานี่แล้ว…"

# "She quickly goes to one of her drawers, and after a minimum of fussing around, pulls out her chessboard."
"ฮานาโกะรีบเดินไปที่ลิ้นชักตัวหนึ่ง พอคุ้ยอยู่ได้สักพักก็คว้ากระดานหมากรุกออกมา"

show hanagown smile
with charachange

# ha "W-would you… like to play…?"
ha "มะ-มาเล่น… ด้วยกันไหม…"

# "This time, I can't stifle the sigh of relief that escapes my lips."
"คราวนี้ฉันเผลอปล่อยให้ตัวเองถอนหายใจด้วยความโล่งอกออกมา"

hide hanagown
with charaexit

show bg school_dormhanako at left
with charamove_slow

# "I hastily agree, and Hanako promptly busies herself setting up while I get off the chair and take a seat on her bed."
"ฉันเออออตกลงไป ฮานาโกะเตรียมกระดานทันทีในระหว่างที่ฉันลุกจากเก้าอี้ไปนั่งที่เตียงเธอ"

# "Once again, Hanako is willing to let me into her world, with so simple a gesture as a game shared between us. I guess I was just winding myself up for no reason."
"เป็นอีกครั้งที่ฮานาโกะยอมให้ฉันได้เข้ามายังโลกของเธอด้วยสิ่งง่าย ๆ อย่างการเล่นเกมระหว่างเรา ฉันคง\nคิดมากไปเองสินะ"

show hanagown smile_close:
    center
    xpos 0.55
    easein 1.0 center
with Dissolve(1.0)

# "After the board is laid down on the bed between us, we finish placing our respective pieces on it."
"พอวางกระดานลงบนเตียงตรงกลางระหว่างเราแล้วเราก็จัดวางหมากของฝั่งตัวเอง"

# "Throughout our friendship, we've never exchanged that many words. When we're like this, though, I see that perhaps we never really needed to. Just a simple book, or board, or meal between us is enough to bridge that distance."
"เราเป็นเพื่อนกันมาโดยแทบไม่ได้คุยอะไรกันเลย แต่เมื่อได้อยู่อย่างนี้แล้วฉันก็เข้าใจว่าเราคงไม่จำเป็นต้องใช้คำพูดใด ๆ\nแค่หนังสือ กระดาน หรือมื้ออาหารระหว่างเรา เหล่านั้นก็เพียงพอแล้วที่จะร่นระยะนั้นเข้ามา"

# "I make the first move, just as I've always done. This is the way our friendship was, and this is the way it will probably always be."
"ฉันเป็นฝ่ายเริ่มก่อนเหมือนอย่างเคย มิตรภาพของเราเป็นเช่นนี้ และคงจะเป็นอย่างนี้ตลอดไป"

# "Something definitely feels different about her, though, and I can't quite grasp what it is. I look at Hanako intently, but I can't work out anything from her expression."
"แต่ฉันรู้สึกว่าฮานาโกะเปลี่ยนไปแล้วจริง ๆ อย่างบอกไม่ถูก ฉันจดจ้องฮานาโกะแต่ก็อ่านสีหน้าเธอไม่ออกเลย"

# "As physically close as we may be, it feels like we're further apart than ever. Hanako is a fragile person, though, and I would never want to hurt her."
"แม้ตัวเราจะอยู่ใกล้กันอย่างนี้ แต่ฉันกลับรู้สึกว่าเราอยู่ห่างจากกันกว่าทุกที แต่ฮานาโกะเป็นคนเปราะบาง\nฉันไม่อยากทำร้ายเธอเลย"

# "That was also the way things always were, and the way things between us will probably always be."
"อะไร ๆ ก็เป็นมาอย่างนี้เสมอ และอะไร ๆ ระหว่างเราคงจะเป็นเช่นนี้ตลอดไป"

stop music fadeout 2.0

# Sad End complete


#*********************

label th_H25:

#Good End assured from here on

scene bg school_scienceroom at bgright
with locationchange

# "Since talking to Lilly yesterday, I've wanted to try and move on from the listlessness I've felt ever since coming to Yamaku."
"ตั้งแต่คุยกับลิลลี่มาเมื่อวานฉันก็อยากทำตัวให้หลุดพ้นจากความเอื่อยเฉื่อยที่เป็นมาตลอดตอนที่อยู่ยามากุ"

# "But even if I try to concentrate on the book in front of me, Hanako's empty seat at the back of the classroom looms larger than life. Every time I start getting focused, my eyes flick over to her desk again and my mind starts spinning."
"แต่ไม่ว่าจะพยายามจดจ่อกับหนังสือตรงหน้ามากเท่าไหร่ โต๊ะฮานาโกะที่ว่างอยู่นั้นยังเบียดสมาธิฉันได้ ทุกครั้ง\nที่เริ่มตั้งสมาธิได้แล้วตาฉันก็จะเหลือบไปทางโต๊ะฮานาโกะอีกรอบพาให้ฉันหัวหมุน"

show miki smile at center
with charaenter

# "Once more my eyes drift over to it, but this time my vision is blocked by a certain other classmate."
"ฉันเหลือบไปมองที่โต๊ะฮานาโกะอีกครั้ง แต่คราวนี้มีเพื่อนร่วมห้องคนหนึ่งมาบดบังวิสัยทัศน์"

# hi "Oh, hey Miki."
hi "อ้าว ไงมิกิ"

show miki grinclosed
with charachange

# mk "Maybe you should just have lunch. I can hear your stomach growling from my desk."
mk "ไปกินข้าวเที่ยงเหอะ เสียงท้องร้องของนายดังมาถึงโต๊ะฉันเลยเนี่ย"

play music music_happiness

# "I let my head drop in disappointment. She seems to take some amusement from my reaction, and hops up onto my desk. Her grin as she sits on it reminds me of the Cheshire Cat."
"ฉันก้มหัวลงด้วยความผิดหวัง ดูท่าจะชอบใจที่เห็นฉันเป็นแบบนี้ มิกิโดดขึ้นนั่งกับโต๊ะฉันแล้วฉีกยิ้ม\nชวนให้นึกถึงแมวเชสเชียร์"

show miki grin_close
with characlose

# mk "So, whatcha' workin' on?"
mk "แล้วนี่ทำไรอยู่"

# hi "Some math. I have a decent handle on it, but I just wanted to revise."
hi "คณิต พอจะเข้าใจอยู่นะ แต่อยากทบทวนอีกหน่อย"

show miki whistle_close
with charachange

# mk "Oh really? Lemme see that."
mk "จริงดิ ขอดูหน่อย"

# "Before I can object, she grabs my mathematics book with her hand. She scans the page I was on, holding it open with the one hand she has, her left arm sitting uselessly on her lap."
"ยังไม่ทันได้แย้งอะไรมิกิก็คว้าหนังสือคณิตศาสตร์ไปแล้ว เธอดูหน้าที่ฉันเปิดไว้อยู่ด้วยมือข้างหนึ่งที่มีอยู่\nส่วนแขนข้างซ้ายวางอยู่บนตักนิ่ง ๆ"

# "In my time here at Yamaku, I've noticed that the other students have a wide range of adjustment to their disabilities, on a purely practical level. Miki is one of those who seem to have some trouble."
"เท่าที่อยู่ยามากุมาฉันเห็นว่าความสามารถในการปรับตัวเข้ากับความพิการของนักเรียนแต่ละคนนั้นแตกต่างกันมาก\nถ้าว่ากันด้วยเฉพาะการใช้ชีวิตตามปกติน่ะนะ มิกิจะอยู่ในกลุ่มที่ยังปรับตัวได้ไม่คล่องนัก"

# "The stump of her left arm tends to be either hanging by her side, slipped into a pocket, or otherwise put out of the way. Sometimes she has a difficult time doing common tasks, which makes her visibly quite frustrated."
"ท่อนแขนข้างซ้ายของมิกิจะอยู่แนบลำตัวเฉย ๆ บ้าง อยู่ในกระเป๋าเสื้อบ้าง หรือไม่ก็ไพล่หลังไว้ บางทีก็จะมีปัญหา\nกับการทำอะไรในทุก ๆ วัน ซึ่งเธอจะทำสีหน้าชัดว่าหงุดหงิดพอสมควร"

# "I feel a little bad for thinking this way, but I'm thankful that Hanako and I don't have disabilities affecting our freedom of movement to that extent."
"รู้สึกผิดอยู่ที่คิดแบบนี้ แต่ฉันก็ดีใจที่ฮานาโกะกับฉันไม่ได้มีความพิการที่มีผลต่อการเคลื่อนไหวมากขนาดนั้น"

# "Then again… if Miki's problem worsened, at least she wouldn't have a real possibility of dying."
"แต่ก็นะ… ถ้าอาการของมิกิหนักกว่านี้ อย่างน้อยก็ไม่ได้ถึงขั้นใกล้ตาย"

show miki smile_close
with charachange

# "My attention is refocused as she thumbs through a few pages, skimming their contents. With such casual interest in the subject matter, it's clear by now that she won't be any help."
"ฉันหันกลับมาสนใจมิกิอีกครั้งเมื่อเธอเปิดไปตามแต่ละหน้าดูเนื้อหาคร่าว ๆ สนใจแค่ผ่าน ๆ แบบนี้ก็ชัดแล้วละ\nว่าคงช่วยอะไรไม่ได้หรอก"

# hi "I'm guessing you're not too interested in this stuff?"
hi "ไม่ค่อยชอบอะไรแบบนี้งั้นสิ"

show miki angry_close
with charachange

# mk "Screw math. It's boring as hell."
mk "ช่างหัวคณิต น่าเบื่อจะตาย"

# "She puts the book back in front of me with indifference. Her eyes move to the notebook beside it that I'd been working out practice equations on."
"มิกิวางหนังสือคืนที่ตรงหน้าฉันอย่างไม่ยี่หระ เธอเลื่อนตามองมาที่สมุดข้าง ๆ ที่ฉันกำลังทำแบบฝึกหัดอยู่"

show miki confused_close
with charachange

# mk "Wait, you're actually able to work that stuff out?"
mk "เดี๋ยว นี่นายทำได้จริงดิ"

# hi "Yeah."
hi "อืม"

show miki wink_close
with charachange

# mk "Wow. I've never talked to a computer with legs before."
mk "โห ไม่เคยคุยกับคอมฯ เดินได้เลยนะเนี่ย"

# hi "Thanks… I think. At least I'm doing better in this than history."
hi "ขอบใจ… มั้ง อย่างน้อยก็ดีกว่าวิชาประวัติศาสตร์อะนะ"

show miki grin_close
with charachange

# mk "Think it's worth asking that librarian for help? I heard she's shooting for uni."
mk "ไปให้บรรณารักษ์คนนั้นช่วยก็น่าจะได้นะ เห็นว่าอยากเข้ามหา’ลัยเหมือนกัน"

# hi "Ah, Yuuko? Maybe. I don't know what she wants to study, though."
hi "อ้อ ยูโกะเหรอ มั้งนะ แต่ไม่รู้ว่ายูโกะจะเรียนคณะอะไรนี่สิ"

# hi "So what about you? Got anything you're thinking of doing after you graduate?"
hi "ว่าแต่เธอเถอะ เรียนจบแล้วจะไปทำอะไรต่อล่ะ"

show miki grinclosed_close
with charachange

# mk "Me? Nah, not really. Just enjoying it while it lasts."
mk "ฉันเหรอ ไม่อะ ไม่ได้คิด แค่ใช้ชีวิตให้สนุกเต็มที่ก่อน"

# "She looks a little awkward when asked about her future, and absentmindedly rubs her left forearm. I kind of want to ask her about it, but I don't think I know her well enough to do so."
"มิกิดูกระอักกระอ่วนไปเล็กน้อยตอนที่ฉันถามเรื่องอนาคตพลางลูบต้นแขนข้างซ้ายเหม่อ ๆ อยากจะถามต่อ\nอยู่เหมือนกัน แต่ฉันคงไม่ได้รู้จักเธอดีพอที่จะถามแบบนั้น"

show miki serious_close
with charachange

# "The conversation peters out, and I lean back in my chair, giving up on the prospect of studying. Miki notices my tired expression and looks oddly serious."
"บทสนทนาจบลงเพียงเท่านั้น ฉันเอนตัวพิงพนักถอดใจเรื่องอ่านหนังสือแล้ว มิกิเห็นฉันที่ดูอ่อนล้าจึงทำสีหน้า\nจริงจังแปลก ๆ ขึ้นมา"

# mk "Thinking about Hanako?"
mk "คิดถึงฮานาโกะอยู่เหรอ"

# hi "It's that obvious?"
hi "ชัดขนาดนั้นเลยเชียว?"

show miki wink_close
with charachange

# mk "You've been glancing at her seat, and you've been pretty quiet. Not too hard to connect the dots."
mk "ก็เห็นเอาแต่มองโต๊ะฮานาโกะ แล้วนายก็เงียบ ๆ ด้วย เดาได้ไม่ยากหรอก"

# hi "I'm just worried about her."
hi "แค่เป็นห่วงน่ะ"

show miki serious_close
with charachange

# mk "Yeah, I can see why you would be. She can get… weird, sometimes."
mk "อืม ก็พอจะรู้นะนายว่าเป็นห่วงเพราะอะไร บางทีฮานาโกะก็ทำตัว… แปลก ๆ เหมือนกัน"

# "She sounds put off, but I can't blame her. Hanako was a hard person to interact with before she warmed up to me, even with Lilly around to help. I haven't known her for that long either, so some of her habits would still be unknown to me."
"น้ำเสียงมิกิฟังดูอึดอัด แต่ก็ว่าไม่ได้หรอก ก่อนที่ฮานาโกะจะเปิดใจให้ฉันเธอก็เป็นคนที่ปฏิสัมพันธ์ด้วยยากแม้จะมีลิลลี่\nคอยช่วยอยู่ด้วยก็ตามที ฉันเองก็ไม่ได้รู้จักฮานาโกะมานานขนาดนั้น อาจจะมีนิสัยบางอย่างที่ฉันยังไม่รู้ก็ได้"

# "My face becomes troubled. If I hadn't developed feelings for her, this would be at least a little easier to deal with."
"ฉันทำหน้ายุ่ง ถ้าฉันไม่ได้มีความรู้สึกอะไรต่อฮานาโกะแล้วเรื่องนี้ก็คงจะรับมือง่ายขึ้นมาอีกหน่อย"

show miki whistle_close
with charachange

# mk "Ah, I mean, no offense. She isn't a bad person, I know that much."
mk "อ่า คือ ไม่ได้จะว่าอะไรนะ ฉันรู้น่าว่าฮานาโกะก็ไม่ใช่คนไม่ดีหรอก"

# told miki about love
label th_H25a:

# hi "I know, I didn't take it that way. It's just harder to deal with when, well, you know. You have feelings for someone."
hi "เข้าใจ ฉันก็ไม่ได้ถืออะไรหรอก แค่ว่าพอ แบบ มีความรู้สึกต่อใครสักคนแล้วมันก็รับมือยากน่ะ"

show miki serious_close
with charachange

# mk "Yeah, I can imagine that. It's hard to forget something like what happened to her during class, too."
mk "อืม พอจะนึกออกอยู่ แถมจะให้ลืมเรื่องอย่างที่เกิดในห้องตอนนั้นก็คงยากด้วย"

# "I wish she hadn't reminded me of that. She just confirmed that it was clearly noticed by others in the room as well."
"ไม่น่ามาสะกิดใจกันเลย ยิ่งแบบนี้ก็เป็นการยืนยันว่าคนอื่นในห้องก็สังเกตเห็นด้วยเหมือนกัน"

# end conditional
label th_H25c:

show miki smile_close
with charachange

# mk "Come on, don't get that down. She's done this before, you've just gotta wait it out."
mk "ไม่เอาน่า อย่าไปซึมอย่างนั้น ฮานาโกะก็เคยเป็นแบบนี้มาก่อนแล้ว นายแค่รอไปก็พอ"

# "She locks herself in her room and acts like an empty husk of a person for a sizable amount of time, ever since she entered Yamaku if not before then as well, and I'm not supposed to be concerned about that?"
"ฮานาโกะขังตัวเองไว้ในห้องแล้วทำท่าเหมือนตัวเองเป็นแค่เปลือกที่ว่างเปล่าอยู่ระยะหนึ่งแบบนั้น ซึ่งเป็นแบบนี้\nมาตั้งแต่เข้าเรียนที่ยามากุหรืออาจจะก่อนหน้านั้นด้วย แล้วแบบนี้จะไม่ให้เป็นห่วงได้ยังไง"

# "Well, I might think that, but there's nothing that I can do. I can't force her to come out, and she does see a therapist, so it's not like she isn't getting any help for her issues."
"โอเค ฉันคิดว่างั้นก็จริง แต่ก็ใช่ว่าจะทำอะไรได้ จะบังคับให้ออกมาจากห้องก็ไม่ได้ แล้วยังไงฮานาโกะก็พบจิตแพทย์\nอยู่แล้วด้วย ไม่ใช่ว่าจะไม่มีคนมาช่วยเรื่องปัญหาของเธอเลยสักหน่อย"

# "Maybe it's natural to think that way when you're so powerless to help someone. “That's just the way she is, and you just have to deal with it.”"
"พอช่วยอะไรใครสักคนไม่ได้แล้วจะคิดแบบนี้ก็คงไม่แปลก “เธอก็เป็นแบบนี้แหละ ทำใจยอมรับไปเสีย”"

show bg school_scienceroom at center
show miki smile_close at twoleft
with charamove

stop music fadeout 3.0

# "As I mull things over, I notice a movement out of the corner of my eye. I glance to see who it is, and end up doing a doubletake."
"ระหว่างที่ครุ่นคิดอะไรหลายอย่างก็เห็นบางอย่างขยับอยู่ที่หางตา เมื่อเหลือบมองว่าใครมาก็ต้องดูให้แน่ใจอีกครั้ง"

show hanako invis:
    right
    xpos 1.1
with None

show hanako basic_normal at right
with dissolvecharamove

# "Sure enough, it's Hanako. She walks through the door just as she would any normal school day, and begins to move towards her seat in her usual silent and humble manner."
"ฮานาโกะไม่ผิดแน่ เธอเดินผ่านประตูเข้ามาเหมือนมาเรียนตามปกติแล้วเดินมาที่โต๊ะตัวเองด้วยท่าทีสงบเสงี่ยม\nไร้เสียงใด ๆ เช่นเคย"

show hanako emb_downtimid
with charachange

# "She looks at me for a moment before blushing and looking away in embarrassment, which makes me realize that I was staring at her. I feel sorry for that, but not doing it is hard after all that's happened."
"ฮานาโกะมองฉันแวบหนึ่งก่อนจะหน้าแดงแล้วเบือนหน้าหนีไปด้วยความอาย ซึ่งฉันก็เพิ่งรู้ตัวว่าจ้องเธออยู่ รู้สึกผิด\nเลยแฮะ แต่จะห้ามตัวเองก็คงยาก เกิดเรื่องอะไรตั้งขนาดนั้น"

hide hanako
with charaexit

play music music_another fadein 4.0

show bg school_scienceroom at bgright
show miki grinclosed_close at center
with dissolvecharamove

# "The girl sitting on my desk looks to me, grinning."
"สาวที่นั่งโต๊ะฉันอยู่หันมามองแสยะยิ้ม"

show miki grin_close
with charachange

# mk "See? Your sweetheart's back already. What did I tell ya?"
mk "เห็นมะ หวานใจนายกลับมาแล้ว ก็บอกแล้วไง"

# hi "You be quiet."
hi "หนวกหูน่า"

# "It might only be meant as a joke, but she hits close enough to make me quite uncomfortable."
"ถึงจะพูดเล่น แต่ก็จี้ใจดำจนฉันขัด ๆ เขิน ๆ ขึ้นมาเหมือนกัน"

show miki smile
with charadistant

# "As we talk, someone calls Miki's name from the door. She jumps down from her vantage point on my desk before turning to me."
"ระหว่างที่คุยกันก็มีคนมาที่ประตูเรียกมิกิ เธอโดดลงจากมุมสูงบนโต๊ะฉันแล้วหันมามอง"

show miki grin
with charachange

# mk "Gotta go, Hisao. Remember to eat sometime, will ya?"
mk "ไปละนะฮิซาโอะ กินข้าวกินปลาบ้างนะ"

# hi "Fine, I will. See you."
hi "อืม ได้ เจอกัน"

hide miki
with charaexit

# "She gives a casual salute before jogging over to the door, where a male student in gym uniform is waiting for her. Probably someone from the track and field club."
"มิกิทำท่าบอกลาสบาย ๆ แล้ววิ่งเหยาะ ๆ ไปที่ประตูซึ่งมีนักเรียนชายใส่ชุดพละยืนอยู่ คงจะเป็นคนในชมรมกรีฑาละมั้ง"

show bg school_scienceroom at right
with charamove_slow

# "Seizing the opportunity, I get up and make my way to Hanako's desk."
"ฉันอาศัยจังหวะนี้ลุกขึ้นเดินไปที่โต๊ะฮานาโกะ"

show hanako emb_timid:
    center
    ypos 1.15
with charaenter

# ha "H-hello…"
ha "สะ-สวัสดี"

# hi "Hi, Hanako. What's up?"
hi "ไงฮานาโกะ ทำไรอยู่"

show hanako emb_downtimid
with charachange

# ha "N-nothing…"
ha "มะ-ไม่ได้ทำอะไร…"

# "Maybe talking to her this soon after she came back to class was a bad move."
"สงสัยการรีบคุยทันทีที่ฮานาโกะกลับมาเข้าเรียนเลยอาจไม่ใช่เรื่องที่ดีเท่าไหร่"

# hi "Want to go come with me and grab something from the cafeteria? I'm pretty hungry."
hi "ไปหาอะไรกินที่โรงอาหารด้วยกันไหม ฉันหิวแล้ว"

show hanako cover_worry
with charachange

# ha "But… I thought you were studying."
ha "แต่… นายอ่านหนังสืออยู่ไม่ใช่เหรอ"

# "Studying can wait. Turning up for class after all this time must have taken some courage for Hanako, so the least I can do is stay with her."
"ไว้ค่อยอ่านก็ได้ กว่าจะมาเข้าเรียนได้คงต้องใช้ความกล้าเป็นอย่างมากทีเดียวกับฮานาโกะที่ผ่านช่วงเวลานั้นมา\nอย่างน้อยฉันก็อยากอยู่เคียงข้างเธอ"

# "“That's just the way she is, and you just have to deal with it” is the way Miki, and probably the class as a whole, views Hanako. I can do more for her, though. I want to do more for her."
"“เธอก็เป็นแบบนี้แหละ ทำใจยอมรับไปเสีย” เป็นแนวคิดที่มิกิและอาจจะคนทั้งห้องด้วยใช้มองฮานาโกะ แต่ฉัน\nยังทำเพื่อเธอได้มากกว่านั้น ฉันอยากทำเพื่อเธอให้มากกว่านั้น"

# hi "After being distracted by Miki, I don't think I'm going to get any work done. Come on, let's go."
hi "มิกิมากวนสมาธิจนฉันไม่น่าทำอะไรได้แล้วละ เถอะน่า ไปกัน"

show hanako basic_bashful at center
with dissolvecharamove

# "She hesitates, but eventually gets up and joins me as we begin walking. These may be small steps for her, but the fact that she's finally out of her room of her own volition lifts a large weight off my shoulders."
"ฮานาโกะชั่งใจก่อนจะลุกขึ้นเดินตามฉันไปด้วยกัน อาจเป็นก้าวเล็ก ๆ สำหรับเธอ แต่แค่เธอตั้งใจมาเข้าเรียน\nด้วยตัวเองแบบนี้ฉันก็สบายใจขึ้นมากแล้ว"

stop music fadeout 2.0

scene black
with dissolve

#*********************

label th_H26:

scene bg suburb_shanghaiint at bgright
with locationchange

play music music_dreamy fadein 2.0

# "My pen busily scrawls onto a slowly filling page of my notebook. My other hand remains on the page of a reference book I borrowed from the library, marking my spot as my eyes flicker to and fro."
"ปากกาฉันขีดไปตามหน้าสมุดที่ค่อย ๆ ถูกทับถมด้วยเส้นหมึก มืออีกข้างฉันวางไว้ที่หน้าหนังสืออ้างอิงที่ฉันยืม\nมาจากห้องสมุดพลางไล่มองเลื่อนนิ้วไปตามจุดต่าง ๆ"

# "As I work, I occasionally mark red circles or underlines onto the photocopied sheets of paper that lie on the table in front of me."
"ระหว่างนั้นฉันก็จะใช้ปากกาแดงวงหรือขีดเส้นใต้ตามแผ่นกระดาษที่ถ่ายเอกสารมาซึ่งวางอยู่บนโต๊ะตรงหน้า"

# "Wanting a change of scenery from the library and to avoid the distractions of the classroom, I decided to make use of the Shanghai for some quiet study time."
"ด้วยอยากเปลี่ยนบรรยากาศจากห้องสมุดและไม่อยากอยู่ในห้องเรียนให้เสียสมาธิฉันจึงมาที่ร้านเซี่ยงไฮ้\nเพื่อมาอ่านหนังสือเงียบ ๆ"

# "It ended up being nice and quiet as expected, and being able to get coffee while I study is a nice bonus."
"ซึ่งก็อยู่สบายและเงียบอย่างที่คิด แถมยังสั่งกาแฟมาดื่มไประหว่างที่อ่านได้ด้วย"

# "Hanako may have returned to her normal self since she came out of her room, but I've done quite the opposite. Daily routine may have returned to us, but I feel as if I'm a different person."
"ฮานาโกะกลับเป็นคนเดิมหลังจากที่ออกห้องมาแล้วก็จริง แต่ฉันกลับทำตรงกันข้าม เราอาจกลับไปใช้ชีวิตตามกิจวัตร\nประจำวันได้แล้วก็จริง แต่ฉันรู้สึกเหมือนตัวเองเป็นคนละคน"

# "Maybe I'm not. It's only been a few days, after all, since I decided I wanted to try and get out of the rut I'd found myself in after my accident. But I want to change, and I'm now actively working towards that goal."
"หรืออาจจะเป็นคนละคนจริง ๆ เพราะผ่านมาได้สองสามวันแล้วที่ฉันลุกขึ้นมาตะกายตัวออกจากหล่มที่ฉันติดอยู่\nตั้งแต่เกิดอุบัติเหตุครั้งนั้น ฉันอยากเปลี่ยนแปลงตัวเอง และตอนนี้ฉันก็ทำสิ่งต่าง ๆ เพื่อเป้าหมายนั้นอยู่ไม่ขาด"

# "Or at least, I would like to think that I am."
"อาจจะไม่ใช่แบบนั้นเลย แต่อย่างน้อยฉันก็คิดว่าตัวเองกำลังทำอยู่"

# hi "Ugh, this is impossible. Brute-forcing this isn't going to work."
hi "โอย ไม่ได้ มัวแต่ฝืนทำแบบนี้ไม่ได้แน่"

# "What's more, I have another piece of writing I have to do after this. I fear that's going to be no easier."
"ยิ่งไปกว่านั้นฉันยังมีงานเขียนอีกชิ้นที่ต้องทำ และเกรงว่างานนั้นจะไม่ได้ง่ายไปกว่านี้ด้วย"

# yu "Um…"
yu "เอ่อ…"

# "I look up in mild surprise to the source of the tentative voice."
"ฉันเงยหน้าขึ้นด้วยความประหลาดใจเล็กน้อยเพื่อมองต้นเสียงอ้ำอึ้งนั้น"

show yuukoshang worried_up at center
with charaenter

# "Yuuko stands at the head of the table with a damp towel in hand, clearly having taken the opportunity to clean the tables while no other patrons were around. She looks curious, her eyes as much on my work as on me."
"ยูโกะยืนอยู่อีกฟากโต๊ะ ในมือถือผ้าขนหนูเปียกอยู่ซึ่งแสดงชัดว่าเธอถือจังหวะที่ลูกค้าคนอื่นไม่อยู่คอยเช็ดโต๊ะ\nสายตาเธอที่มองงานของฉันสลับกับตัวฉันนั้นดูสงสัย"

# hi "What's the matter?"
hi "มีอะไรเหรอครับ"

show yuukoshang worried_down
with charachange

# yu "I was just wondering… what sort of work are you having so much trouble with?"
yu "พอดีอยากรู้น่ะ… ว่าเธอทำอะไรอยู่เหรอ เห็นเครียดมาก"

# hi "Oh. It's just history. I'm fine with science and math, so I'm trying to get my other subjects up to par."
hi "อ๋อ วิชาประวัติศาสตร์น่ะครับ คือผมทำวิชาวิทยาศาสตร์กับคณิตศาสตร์ได้เลยจะลองฝึกให้วิชาอื่นถนัดขึ้นมา\nพอ ๆ กันบ้าง"

show yuukoshang happy_up
with charachange

# "Yuuko looks positively delighted at this development. I feel like I just chose the right answer on some big quiz show."
"ยูโกะดูดีใจมากที่เรื่องเป็นแบบนี้ รู้สึกเหมือนตอบคำถามในรายการเกมโชว์ดัง ๆ สักรายการถูกเลย"

show yuukoshang closedhappy_down
with charachange

# yu "Oh! I think I can help you with that!"
yu "โอ้! ฉันน่าจะพอช่วยได้นะ!"

show yuukoshang worried_down
with charachange

# yu "Um, if you don't mind… of course…"
yu "เอ่อ ถ้าเธอไม่ว่าอะไร… น่ะนะ…"

# "I briefly consider turning down the offer in order to not cause her too much trouble, but she looks too excited about this for me to do it. It would be mean to shoot her down like that, after such a reaction."
"แวบหนึ่งฉันคิดจะบอกปัดข้อเสนอนั้นไปด้วยไม่อยากรบกวนยูโกะมาก แต่เธอดูตื่นเต้นมากจนฉันปฏิเสธไม่ลง\nทำท่าขนาดนี้แล้วไม่ตอบรับก็คงใจดำเกินไปหน่อย"

# hi "If you're willing to help, I'd really appreciate it."
hi "ถ้าเต็มใจผมก็ยินดีครับ"

show yuukoshang closedhappy_up
with charachange

hide yuukoshang
with charaexit

# "She claps her hands together and quickly deposits her towel on the counter, before returning and taking a seat across from me."
"ยูโกะตบมือทันทีแล้วรีบไปวางผ้าขนหนูไว้ที่เคาน์เตอร์ก่อนจะกลับมานั่งตรงหน้าฉัน"

show yuukoshang invis at center
with None

show yuukoshang smile_down at Position(ypos=1.15)
with dissolvecharamove

# "I take my notebook off the top of the textbook and hand it over for her to peruse."
"ฉันหยิบสมุดที่วางอยู่บนหนังสือยื่นให้ยูโกะได้ดู"

show yuukoshang neutral_up
with charachange

# yu "So you're studying the Edo Period?"
yu "เรียนยุคเอโดะอยู่เหรอ"

# hi "Yeah. I'm not really much good at this, though."
hi "ครับ แต่ไม่ค่อยถนัดเท่าไหร่"

show yuukoshang worried_up
with charachange

# "She takes the textbook and reads a few pages from a random section near the middle for a bit, but the aura of enthusiasm she'd been radiating previously is rapidly sapping away."
"ยูโกะหยิบหนังสือไปเปิดหน้ากลาง ๆ อ่านอยู่สองสามหน้า แววความตื่นเต้นที่เธอเปล่งออกมาเมื่อกี้จางหาย\nไปอย่างรวดเร็ว"

# hi "I'm guessing this isn't the kind of history you were expecting?"
hi "ไม่ใช่ประวัติศาสตร์แบบเดียวกันกับที่คิดไว้สินะครับ"

show yuukoshang worried_down
with charachange

# yu "Unfortunately not. My main area is European history, especially in the classical era. Sorry."
yu "เกรงว่าจะไม่ ฉันถนัดประวัติศาสตร์ยุโรปมากกว่า โดยเฉพาะยุคคลาสสิกน่ะ ขอโทษทีนะ"

# "She looks a bit downcast, but as she carefully closes the book and lays it back down on the table, her face perks up again."
"ยูโกะดูหมองไปเล็กน้อย แต่พอเธอปิดหนังสืออย่างเบามือแล้ววางไว้กับโต๊ะแล้วเธอก็ทำหน้าสดใสเหมือนเดิม"

show yuukoshang smile_down
with charachange

# yu "Would you like another cup of coffee?"
yu "รับกาแฟอีกแก้วไหม"

# hi "Hmm? Oh, yeah, sure."
hi "หืม? อ้อ ครับ รับ"

show yuukoshang invis at center
with dissolvecharamove

# "I reach forward and get my book back as Yuuko gets up, takes my mug, and slowly walks to the counter to make another brew."
"ฉันเอื้อมไปหยิบหนังสือ ยูโกะลุกขึ้นหยิบแก้วฉันเดินไปที่เคาน์เตอร์ชงกาแฟให้ใหม่"

# "As usual, she's absolutely silent as she does this; every ounce of her concentration is focused on not tripping over or dropping the plain white mug."
"ยูโกะเงียบสนิทไปทุกการกระทำเหมือนเคยเพราะต้องตั้งสมาธิอย่างแน่วแน่ระวังไม่ให้สะดุดหรือทำแก้วสีขาวนั้นตก"

# "I take the opportunity to lay back and relax for a bit, the hum of the coffee machine filling the otherwise quiet air."
"ฉันถือโอกาสนี้เอนตัวผ่อนคลายเสียหน่อย บรรยากาศเงียบงันมีเพียงเสียงเครื่องทำกาแฟที่เข้ามาแทรก"

# "It's small details like that which make me realize how much I've come to appreciate the little things in life."
"รายละเอียดเล็ก ๆ เช่นนี้เองที่ทำให้ฉันระลึกได้ว่าตัวเองจับสังเกตสิ่งเล็ก ๆ รอบตัวได้แล้ว"

# "The peace and quiet of the local town, the discipline and order of Yamaku, the green of the trees that were so rare in my home city, the relaxed pace at which the aging residents live their lives…"
"ความสงบเงียบในเมืองชนบท ความมีวินัยเป็นระเบียบในยามากุ ต้นไม้เขียวชอุ่มที่พบได้ยากในเมืองที่ฉันจากมา\nผู้สูงอายุในท้องที่ที่ใช้ชีวิตกันแบบไม่เร่งร้อน…"

# "Everything feels so… certain. It's comforting."
"ทุกอย่างมันช่าง… มั่นคง ชวนให้สบายใจ"

# "I can feel myself beginning to nod off, when the sound of the mug coming to rest on the table grabs my attention. Seems like it arrived not a moment too soon."
"ฉันเกือบจะม่อยหลับไปแล้วถ้าไม่มีเสียงแก้วกาแฟที่วางบนโต๊ะมาดึงความสนใจฉันก่อน ดูท่าจะมาได้จังหวะพอดีเลย"

show yuukoshang neutral_down at Position(ypos=1.15)
with dissolvecharamove

# "Yuuko takes her previous seat once again as I pick myself up and bring a hand around the mug to check its temperature. It's just a little too hot to drink right away, so I blow on it a little."
"ยูโกะนั่งลงที่เดิม ฉันยืดตัวนั่งตรงแล้วใช้มือแตะ ๆ แก้วเพื่อดูเรื่องอุณหภูมิ เมื่อเห็นว่ายังเย็นไม่พอที่จะดื่มได้ทันที\nจึงเป่าเบา ๆ"

show yuukoshang worried_down
with charachange

# yu "It's a shame you don't like history all that much. I sort of guessed you might be more into science."
yu "น่าเสียดายนะที่เธอไม่ได้สนใจประวัติศาสตร์ขนาดนั้น แต่ก็พอเดาไว้แล้วละนะว่าเธอคงชอบวิทยาศาสตร์มากกว่า"

# hi "How so?"
hi "ทำไมเหรอครับ"

show yuukoshang smile_up
with charachange

# yu "You've nearly read out the science fiction section of the library already. It wasn't hard to notice."
yu "เธออ่านหนังสือหมวดนิยายวิทยาศาสตร์เกือบหมดแล้วนี่ ดูได้ไม่ยากหรอก"

# hi "You do have a good point, there. Well, what can I say? You've pegged me just about right."
hi "ก็ถูกนะครับ เอ่อ จะให้แก้ตัวยังไงล่ะ คุณเดาทางผมแม่นขนาดนี้"

show yuukoshang neutral_down
with charachange

# hi "You sound like you really take an interest in history though, especially considering how specific you were about it. Do you study in that area, or something? Go on digs overseas?"
hi "แต่คุณยูโกะก็ฟังดูสนใจประวัติศาสตร์มากเลยนะครับ ยิ่งเห็นพูดเจาะจงแบบนั้นอีก เรียนประวัติศาสตร์\nหรืออะไรแบบนั้นเหรอครับ ไปอยู่ต่างประเทศงี้"

show yuukoshang closedhappy_up
with charachange

# "She giggles nervously at the thought."
"ยูโกะหัวเราะคิกคักเมื่อคิดตาม"

show yuukoshang neurotic_down
with charachange

# yu "I'd like to visit the Mediterranean sometime and see the old architecture and art for myself, but I don't think I could trust myself to handle such delicate things."
yu "ถ้ามีโอกาสฉันก็อยากไปดูศิลปะกับสถาปัตยกรรมโบราณที่แถบเมดิเตอร์เรเนียนเหมือนกันนะ แต่ฉันว่าตัวเอง\nคงอยู่กับของเปราะบางแบบนั้นไม่ได้หรอก"

show yuukoshang neutral_down
with charachange

# yu "I'm saving up to formally study it in university, although I also read up on it whenever I have free time outside of work."
yu "ฉันเก็บเงินไว้ไปเรียนให้เป็นเรื่องเป็นราวในมหาวิทยาลัยอยู่ แต่พอว่างจากงานแล้วฉันก็ไปหาของพวกนี้อ่าน\nเหมือนกัน"

# "So Miki was right about her university aspirations. Considering how she fares as a waitress, a more theoretical path may suit Yuuko better. It's nice to hear that she has some ambitions though, considering how hard she works."
"สรุปคือจริงอย่างมิกิว่าที่ยูโกะอยากเรียนมหาวิทยาลัย ดูจากการทำงานในฐานะบริกรแล้ว เส้นทางภาคทฤษฎี\nน่าจะเหมาะกับเธอมากกว่า แต่ก็ดีใจที่เห็นว่าเธอมีจุดมุ่งหมายอะไรบ้าง เพราะเป็นคนขยันขนาดนี้"

# "I nod and take a careful sip of my coffee. By now it's cooled to the right temperature, so I begin to drink while keeping an eye on the book below,
# trying to read at the same time."
"ฉันพยักหน้าแล้วจิบกาแฟช้า ๆ ตอนนี้กาแฟเย็นได้ที่แล้วฉันจึงดื่มไปพลางมองหนังสือที่วางอยู่ข้างล่างอ่านไปด้วย"

# "A few minutes pass quietly, Yuuko looking out the window and watching the world go by while I have my coffee and study."
"เวลาผ่านไปสองสามนาทีอย่างเงียบเชียบ ยูโกะมองโลกที่ดำเนินไปผ่านทางหน้าต่าง ส่วนฉันดื่มกาแฟไปอ่านหนังสือไป"

show yuukoshang closedhappy_up
with charachange

# "A movement catches my eye, and I look up to see Yuuko smiling and waving to someone outside. Following her gaze surprisingly reveals the someone to be Hanako."
"ฉันสะดุดตาเข้ากับบางอย่างที่ขยับอยู่ พอเงยหน้ามองก็เห็นยูโกะที่ยิ้มโบกมือทักทายใครบางคนที่อยู่ข้างนอก\nฉันมองตามสายตาเธอไปแล้วต้องแปลกใจเมื่อเห็นว่าคนนั้นคือฮานาโกะ"

# "She is looking at us from the side of the street across from where we are. Her usually all-too-visible timidity is largely absent, probably thanks to there being so few people around right now."
"ฮานาโกะยืนมองเราอยู่จากอีกฝั่งถนน ความอายที่ฉายชัดโดยปกติของเธอนั้นแทบไม่มีอยู่ อาจจะเพราะตอนนี้\nไม่ค่อยมีคนมาก"

# "Evidently she decides to join us, as after a little wave, she gives a quick glance up and down the street and crosses towards the side that the café is on."
"ฮานาโกะโบกมือหย็อย ๆ แล้วก้ม ๆ เงย ๆ มองถนนก่อนจะข้ามมาฝั่งที่คาเฟนี้ตั้งอยู่ คงจะอยากมาร่วมวงด้วยละนะ"

$ renpy.music.set_volume(0.3, 0.0, channel="sound")
play sound sfx_storebell

show hanako invis:
    right
    xpos 1.0
with None

show yuukoshang happy_up:
    twoleft
    ypos 1.15
show bg suburb_shanghaiint at center
show hanako basic_normal at tworight
with dissolvecharamove

# "The familiar doorbell to the Shanghai rings out as Hanako enters and makes her way to the table we're sitting at."
"ฮานาโกะเข้ามาพร้อมเสียงกระดิ่งของร้านเซี่ยงไฮ้อันคุ้นเคย เธอเดินมาที่โต๊ะที่พวกเรานั่งอยู่"

show hanako cover_distant at Position(ypos=1.15)
with dissolvecharamove

# ha "H-hello…"
ha "สะ-สวัสดี…"

show yuukoshang smile_down
with charachange

# yu "Good afternoon."
yu "ทิวาสวัสดิ์"

# hi "Hi, Hanako. What's up?"
hi "ไงฮานาโกะ ทำอะไรอยู่เหรอ"

show hanako emb_smile
with charachange

# ha "N-nothing… just… g-going for a walk… since the weather was nice."
ha "มะ-ไม่มีอะไร… แค่… เห็นว่าอากาศดี… เลยอะ-ออกมาเดินนิดหน่อย"

# hi "Yeah, I get what you mean. I'm glad I decided to study here instead of the library."
hi "อื้ม ก็จริงนะ คิดถูกจริง ๆ ที่วันนี้มาอ่านหนังสือที่นี่แทนที่ห้องสมุด"

# "It's comfortable in here thanks to that, better than the sometimes quite stuffy library. I look to Yuuko, who nods in response."
"ในร้านก็อยู่สบายเพราะอากาศดีด้วย ดีกว่าห้องสมุดที่บางทีก็อึดอัด ฉันหันไปมองยูโกะที่พยักหน้าตอบ"

show yuukoshang neutral_down
with charachange

# yu "It's nice. It's just a shame that summer can't last forever."
yu "เห็นด้วย เสียดายที่หน้าร้อนอยู่ไม่ครบตลอดปี"

show yuukoshang neurotic_up
with charachange

# yu "Oh wait, sorry, um, would you like a drink?"
yu "เอ๊ะ เดี๋ยว ขอโทษที เอ่อ รับอะไรดีคะ"

show hanako basic_smile
with charachange

show yuukoshang neutral_down
with charachange

# "Hanako shakes her head. Thankfully, it's enough to calm Yuuko back down."
"ฮานาโกะสั่นหัว โชคดีที่แค่นั้นยูโกะก็สงบลงได้แล้ว"

show hanako basic_bashful
with charachange

# ha "H-how are you going with studying?"
ha "อะ-อ่านหนังสือเป็นไงบ้าง"

# hi "Okay… ish."
hi "ก็พอ… ได้"

# hi "Oh yeah, have you talked with Lilly?"
hi "เอ้อ แล้วเธอได้คุยกับลิลลี่หรือยัง"

show yuukoshang smile_up
with charachange

# yu "I'm interested too; how is she doing?"
yu "ฉันก็อยากรู้เหมือนกัน ลิลลี่เป็นยังไงบ้าง"

show hanako cover_worry
with charachange

# ha "Sh-she's enjoying it… I think."
ha "กะ-ก็เหมือนจะ… สนุกนะ"

# "I… think that's all we're going to get out of her. Being around Yuuko is tensing her up."
"ฉัน… ว่าเราคงได้รู้แค่นี้แหละถ้าถามฮานาโกะ พออยู่กับยูโกะแล้วฮานาโกะก็เกร็ง"

show yuukoshang closedhappy_down
with charachange

# yu "Ah, it would be so nice to travel to Scotland."
yu "เฮ้อ ได้บินไปสกอตแลนด์คงดี"

show yuukoshang happy_down
with charachange

# yu "Green fields, castles, lovely small towns, men in kilts, interesting history…"
yu "ทุ่งสีเขียว ปราสาท เมืองเล็ก ๆ อันอบอุ่น ผู้ชายใส่กระโปรงคิลต์ ประวัติศาสตร์อันน่าสนใจ…"

# "I can't say I see the appeal of men in kilts, myself. It does seem like a picturesque place, though."
"ฉันไม่ค่อยสนใจผู้ชายใส่กระโปรงคิลต์สักเท่าไหร่ แต่ก็น่าจะเป็นสถานที่ที่ทิวทัศน์สวยดี"

play sound sfx_storebell

show hanako defarms_shock
show yuukoshang panic_up
with vpunch

# "As we talk, the jingle of the doorbell rings again. Hanako is startled, noticing Yuuko's panicked expression at the prospect that she might leave customers to wait a handful of seconds, due to her chatter with us."
"ระหว่างที่คุยอยู่นั้นเสียงกระดิ่งประตูก็ดังขึ้นอีกครั้ง ฮานาโกะตกใจเมื่อเห็นยูโกะที่ลนลานเพราะคิดว่าตัวเอง\nมัวแต่คุยกับพวกเราจนอาจทำให้ลูกค้าต้องรออยู่ประมาณสองสามวินาที"

show yuukoshang worried_down at twoleft
with Dissolvemove(0.3)

with Pause(0.2)

hide yuukoshang
with charaexit

# "Yuuko gives us a quick bow, then hastily skitters over and greets the new customers, an elderly man and his wife. I watch her for a bit, craning my head around to get a good view."
"ยูโกะค้อมตัวเล็กน้อยแล้วรีบพุ่งตัวไปต้อนรับลูกค้าใหม่ที่เป็นชายแก่กับภรรยาของเขา ฉันมองยูโกะอยู่ครู่หนึ่ง\nพลางชะเง้อหน้ามองไปรอบ ๆ ร้าน"

show hanako def_worry
with charachange

# "Hanako is staring at me with her one visible eye."
"ฮานาโกะจ้องฉันด้วยตาข้างหนึ่งที่ผมไม่ได้ปรกอยู่"

show hanako def_worry:
     center
     ypos 1.15
show bg suburb_shanghaiint at bgleft
with charamove

show hanako emb_downtimid
with charachange

# "She averts her head in embarrassment as I turn to make eye contact."
"เธอหันหน้าหนีด้วยความอายเมื่อฉันหันไปสบตาด้วย"

# hi "I was just thinking that it's nice to have ambitions for the future. Yuuko was telling me a little about her university aspirations before."
hi "พอดีคิดอยู่น่ะว่าการมีจุดมุ่งหมายในอนาคตนี่มันดีจังนะ เมื่อกี้ยูโกะก็เล่าเรื่องที่จะเข้ามหา’ลัยให้ฟังนิดหน่อย"

show hanako emb_timid
with charachange

# ha "Oh."
ha "อ้อ"

# hi "It's a shame. If she wasn't so neurotic and overworked, I think she could be a really happy person."
hi "น่าเสียดายนะ ถ้าไม่ใช่คนขี้ตระหนกที่ต้องทำงานหนักแบบนี้คงเป็นคนที่มีความสุขมาก ๆ เลย"

# "As much as I'd like to play host to Hanako and entertain her a bit, I do need to study as well. To be honest, I don't think the distraction from Yuuko helped either."
"ถึงอยากจะเป็นเพื่อนคุยสนุก ๆ ให้ฮานาโกะอยู่ แต่ฉันเองก็ต้องอ่านหนังสือเหมือนกัน แต่ว่าตามตรง พอยูโกะ\nมากวนแล้วฉันก็ไม่ค่อยมีสมาธิแล้วด้วย"

# hi "Sorry if I'm a bit distracted. I need to try and get this done, otherwise I'm going to flunk the history exams pretty hard."
hi "ขอโทษนะถ้าคุยไปแบบเหม่อ ๆ น่ะ พอดีต้องจัดการเจ้านี่ให้เสร็จก่อน ไม่งั้นเดี๋ยวคะแนนวิชาประวัติศาสตร์\nตกฮวบแน่"

# "I'm left running my hand through my hair in frustration. That letter needs doing as well, once I get back to my dormitory room."
"ฉันขยี้ผมด้วยความหัวเสีย เดี๋ยวพอกลับหอแล้วต้องไปจัดการกับจดหมายนั่นด้วย"

# hi "I hope I have more luck with that than this. Damn."
hi "หวังว่าจะทำไอ้นั่นได้ดีกว่างานนี้นะ ให้ตาย"

show hanako emb_downtimid
with charachange

# ha "W-what with?"
ha "อะ-ไอ้นั่นคืออะไรเหรอ"

# hi "Oh, uh… I was going to… write to Iwanako. Right now though, this is more important."
hi "อ้อ เอ่อ… พอดีจะ… เขียนจดหมายถึงอิวานาโกะน่ะ แต่ตอนนี้อันนี้สำคัญกว่า"

# "All I've done is rattle myself. I can't focus on the work in front of me when my stomach is slowly turning at the prospect of actually attempting to write her back, after all this time."
"ฉันยิ่งทำตัวเองร้อนใจไปอีก พอท้องไส้ปั่นป่วนเมื่อนึกถึงว่าต้องเขียนกลับไปหาอิวานาโกะจริง ๆ ทั้งที่ผ่านมา\nนานขนาดนี้แล้วก็ไม่มีสมาธิจะมาจดจ่อกับงานตรงหน้าเลย"

# "I force myself to concentrate on the book, picking up my pen once I have a quick sip of coffee."
"ฉันฝืนตัวเองให้จดจ่ออยู่กับหนังสือแล้วจิบกาแฟก่อนจับปากกา"

show hanako basic_distant
with charachange

# "After a few seconds, Hanako stops silently watching me and leans back in her seat, relaxing as much as she ever seems to be able to, looking out the window to pass the time."
"ผ่านไปสองสามวินาทีฮานาโกะก็เลิกมองฉันแบบเงียบ ๆ แล้วเอนตัวพิงพนักทำท่าผ่อนคลายที่สุดซึ่งฉันก็เคยเห็น\nว่าเธอผ่อนคลายได้ที่สุดก็ประมาณนี้แล้วมองออกไปนอกหน้าต่างฆ่าเวลา"

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
stop music fadeout 3.0

# "We stay like this for a long time before leaving for the dormitories together. I'm surprised she had the patience to wait me out."
"เรานั่งด้วยกันอย่างนั้นอยู่นานก่อนจะออกร้านแล้วกลับหอ ฉันนึกประหลาดใจที่ฮานาโกะใจเย็นพอจะรอจนฉันออกมา"

scene ev hisao_letter_open
with shorttimeskip

play music music_night fadein 1.0

# "Iwanako's letter lies on my desk beside a blank sheet of lined paper and an unused envelope. The tapping of my pen is the only thing to be heard this late at night."
"จดหมายของอิวานาโกะวางบนโต๊ะฉันอยู่ข้างกระดาษตีเส้นเปล่ากับซองจดหมายที่ยังไม่ได้ใช้ ค่ำคืนนี้มีเพียง\nเสียงกดปากกาที่ดังก้องอยู่"

# "As I feared, my second task for the day turns out to be just as difficult as the first, if not harder."
"และภาระที่สองของวันนี้ก็ยากพอ ๆ กันกับภาระแรก—หรือไม่ก็อาจยากกว่า—อย่างที่หวั่นใจไว้"

# "It's been so many months since we even saw each other. Even so, I can still remember what she looked like, what she sounded like, and what she acted like. By now, though, the little details are beginning to slip away."
"เราไม่ได้เจอหน้ากันมานานหลายเดือนมากแล้ว ถึงอย่างนั้นฉันก็ยังจำได้ว่าเธอหน้าตาเป็นอย่างไร เสียงเป็นอย่างไร\nกิริยาท่าทีเป็นอย่างไร แต่ตอนนี้ฉันก็ลืม ๆ รายละเอียดบางส่วนไปบ้างแล้ว"

# "When I first saw her letter, I barely recognized her handwriting at all. Even the pink pen she always used was forgotten until her writing reminded me of it."
"ตอนที่ได้เห็นจดหมายของเธอเป็นครั้งแรกฉันแทบจำลายมือไม่ได้ด้วยซ้ำ ลืมไปแล้วว่าปกติเธอใช้ปากกา\nหมึกสีชมพูเขียนจนนึกได้ก็ตอนที่เห็นลายมือของเธอ"

# "I wonder why she didn't use it for the letter; she used to write everything with it. Maybe she thinks it's too immature now."
"อยากรู้จังว่าทำไมถึงไม่เขียนจดหมายฉบับนี้ด้วยปากกาสีชมพู ทั้งที่เมื่อก่อนก็ใช้เขียนทุกอย่าง อาจจะเพราะตอนนี้\nมองว่าเป็นอะไรที่ดูเป็นเด็ก ๆ ละมั้ง"

# "I should be thinking about myself, and about what I want to communicate to her. My mind can't stop concentrating on her, though. On the past we shared before it was taken away so suddenly."
"ที่จริงตอนนี้ฉันควรคิดถึงเรื่องตัวเองกับคิดว่าจะสื่อสารอะไรกับเธอบ้าง แต่ใจฉันยังจดจ่ออยู่กับเธอไม่หยุด จดจ่อ\nอยู่กับอดีตที่เราเคยอยู่ด้วยกันก่อนที่ช่วงเวลานั้นจะถูกพรากไปอย่างกะทันหัน"

# "The bright and slightly garish decorations suit her sense of aesthetics. Picking up the letter to take a closer look at it, I give a long sigh."
"ของประดับสดใสดูบาดตาเล็กน้อยนั้นสมกับรสนิยมของตัวเธอจริง ๆ ฉันหยิบจดหมายขึ้นมาดูใกล้ ๆ\nแล้วถอนหายใจพรืด"

# "This is the last link binding me to my past. Iwanako didn't suddenly cease to exist when she left my hospital room for the last time, but I needed this letter to remind me of that."
"สิ่งนี้เป็นพันธะสุดท้ายที่ยังตรึงฉันไว้กับอดีต ฉันต้องให้จดหมายนี้มาเป็นสิ่งเตือนว่าอิวานาโกะไม่ได้หายตัวไปทันที\nหลังจากที่ออกจากห้องในโรงพยาบาลนั้นไปเป็นครั้งสุดท้าย"

# "I had all those feelings neatly filed away. I felt as if I didn't need them, that I could just begin life completely anew. It was easier that way."
"ฉันเก็บความรู้สึกเหล่านั้นไว้ในลิ้นชักเรียบร้อยแล้ว ฉันคิดว่าตัวเองคงไม่ต้องการความรู้สึกเหล่านั้น คิดว่าคง\nเริ่มชีวิตใหม่ตั้งแต่ต้นได้ ทำแบบนั้นแล้วอะไร ๆ จะง่ายขึ้น"

# "In the end, I suppose that was a rather naive thing to think. Sooner or later, my past would have caught up with me one way or the other."
"สุดท้ายแล้วฉันคงคิดง่ายเกินไปสินะที่คิดแบบนั้น ไม่ช้าก็เร็ว สักวันอดีตจะต้องหวนกลับมาหาตัวฉัน\nไม่ทางใดก็ทางหนึ่ง"

# "But what am I supposed to say to her? “Thank you for bringing me closure?” All the letter did was end the sense of closure I'd previously felt."
"แต่จะให้ฉันพูดกับเธอว่ายังไงล่ะ “ขอบคุณที่พูดส่งท้ายกันนะ” จดหมายฉบับนี้ก็ทำได้เพียงแค่ย้ำชัดถึงความรู้สึก\nว่าทุกสิ่งจบลงไปแล้วที่ฉันเคยรู้สึก"

# "Try as I might, I can't write so much as a single word down on the paper in front of me. I can't even think of what exactly I want to say."
"ไม่ว่าจะคิดหนักแค่ไหนฉันก็เขียนลงบนกระดาษตรงหน้านี้ไม่ได้เลยแม้แต่คำเดียว คิดไม่ออกด้วยซ้ำว่าต้องพูดอะไร"

stop music fadeout 4.0

scene bg school_dormhisao_ss
with locationchange

# "Putting the letter down on top of the blank sheet, I gather the materials together and file them away in my drawer."
"ฉันวางจดหมายฉบับนั้นไว้บนกระดาษเปล่าแล้วรวบของทุกอย่างใส่ลิ้นชักไว้"

# "The clunk the desk makes as it closes makes me momentarily tense in frustration, before I get up to go grab a drink from the vending machine on the first floor."
"เสียงดังกึงจากโต๊ะเมื่อดันลิ้นชักเข้าไปแล้วทำให้ฉันตัวเกร็งขึ้นมาแวบหนึ่งด้วยความหงุดหงิด ฉันลุกขึ้น\nไปซื้อเครื่องดื่มจากตู้ขายของแบบหยอดเหรียญที่อยู่ชั้นหนึ่ง"

scene bg school_dormhallway
with locationchange

# "I tried, but I couldn't do it. After all the time that's passed, I still don't know how to deal with Iwanako."
"ฉันพยายามแล้วแต่ก็ทำไม่ได้ ผ่านมานานขนาดนี้แล้วฉันก็ยังไม่รู้ว่าจะต้องรับมือเรื่องอิวานาโกะอย่างไร"

scene black
with dissolve

#*********************

label th_H27:

scene bg school_library
with locationchange

play music music_happiness

# "The library, while not humming with activity, is noticeably more busy than usual. Exams are not far away, and that's reflected in the number of students burying their noses in textbooks at the tables around us."
"ห้องสมุดนั้นดูวุ่นวายกว่าปกติ ถึงจะไม่ได้มีคนมากขนาดนั้น เห็นได้ว่าไม่นานจะถึงวันสอบแล้วจากการที่\nมีนักเรียนหลายคนก้มหน้าก้มตาอ่านหนังสืออยู่ตามโต๊ะรอบตัว"

# "I've been studying quite a lot in the past few days, just like them, in hope of doing well in the exams. This also means that Hanako and I have been playing games less, so she's begun studying as well just to fill in the time."
"ช่วงสองสามวันมานี้ฉันอ่านหนังสือมากเหมือนอย่างคนเหล่านั้นด้วยหวังจะสอบให้ได้คะแนนดี ซึ่งแปลว่าฮานาโกะ\nกับฉันเองก็ได้เล่นเกมกันน้อยครั้งลงด้วย เธอจึงอ่านหนังสือบ้างเพื่อคั่นเวลา"

# "Nevertheless, I've found myself forsaken by her on this particular day."
"แต่แม้กระนั้นวันนี้ฮานาโกะก็ไม่อยู่กับฉัน"

# "The textbook in front of me has remained on the same page for some time. After so much reading on subjects I couldn't care less about if not for the exams, my mind is beginning to wander."
"หนังสือตรงหน้าฉันค้างอยู่หน้าเดิมมาสักพักแล้ว หลังจากที่อ่านวิชาที่ถ้าไม่มีสอบก็คงไม่สนใจแล้วจิตใจฉัน\nก็เริ่มล่องลอย"

# "I find my eyes flicking over to where Hanako would usually be, just like on the days she wasn't in class. Her usual beanbag in the corner of the room is conspicuously unoccupied."
"ฉันเหลือบตามองไปยังที่ที่ฮานาโกะจะนั่งประจำเหมือนอย่างที่ทำในวันที่เธอไม่มาเรียน บีนแบ็กตรงมุมห้อง\nซึ่งเป็นที่ประจำของฮานาโกะนั้นว่างลงอย่างเห็นได้ชัด"

# "It was here that we first really met. I tried to start a conversation with her, she got skittish, and eventually bolted from the room altogether."
"เป็นตรงนี้เองที่เราได้เจอกันเป็นครั้งแรกจริง ๆ ฉันลองคุยกับฮานาโกะ แต่เธอก็ตกใจกลัวแล้ววิ่งหนีออกจากห้องไป"

# "I probably shouldn't smile about it, but it was kind of amusing, in hindsight. Nowadays, it's more and more difficult to imagine her doing such a thing. Even with Lilly gone, she's been doing well now that she's come out of her room."
"อาจจะไม่ใช่เรื่องชวนยิ้มเท่าไหร่ แต่พอย้อนนึกดูก็ตลกดี ยิ่งนานวันไปฉันก็ยิ่งนึกภาพได้ยากขึ้นเรื่อย ๆ ว่าฮานาโกะ\nจะทำอะไรแบบนั้น แม้แต่ตอนนี้ที่ลิลลี่ไม่อยู่ฮานาโกะก็สบายดีและออกมาจากห้องได้แล้ว"

# "I want to talk with her, or at least play another game of chess. I'm tired of studying, and it's been a few days since we've really done anything together."
"ฉันอยากคุยกับฮานาโกะหรือไม่ก็อย่างน้อย ๆ เล่นหมากรุกด้วยกันสักเกม ฉันเบื่อจะอ่านหนังสือแล้ว แถมเรา\nก็ไม่ได้ทำอะไรด้วยกันมาสองสามวันแล้วด้วย"

# "The question of where to find Hanako isn't a particularly difficult one. If she's not in the library, chances are that she's either in the tearoom for some peace and quiet, or in her dormitory room."
"คำถามว่าจะไปตามหาฮานาโกะได้ที่ไหนบ้างนั้นตอบได้ไม่ยากเลย ถ้าไม่อยู่ที่ห้องสมุดก็แปลว่าอาจไปหาความสงบเงียบ\nที่ห้องน้ำชาหรือไม่ก็อยู่ที่หอ"

# "Deciding to check them in that order, I pack up my books and make my way out of the library."
"ฉันคิดจะไปไล่ดูแต่ละที่ตามลำดับแล้วปิดหนังสือเดินออกมาจากห้องสมุด"

stop music fadeout 5.0

# timeskip
scene bg school_girlsdormhall
with shorttimeskip

# "I stretch and give a loud groan as I walk down the hallway. Studying may be frustrating at times, but with the progress I feel I've made, there is also some sense of pride in getting it done. It's a good feeling."
"ฉันบิดขี้เกียจแล้วร้องโอดโอยไประหว่างที่เดินตามโถงทางเดิน ถึงบางครั้งการอ่านหนังสือจะน่าหงุดหงิดไปบ้าง แต่อ่าน\nได้มากขนาดนี้แล้วก็รู้สึกภูมิใจขึ้นมาเหมือนกัน เป็นความรู้สึกที่ดีเชียว"

scene bg school_dormhanako_ni
show hanako_door_base at right
show hanako_door_door at left
with locationchange

# "There isn't a sound to be heard from inside as I stand in front of the door to Hanako's room. I guess that isn't very indicative of whether she's inside or not, given how quiet she usually is."
"เมื่อมายืนอยู่หน้าห้องฮานาโกะแล้วฉันก็ไม่ได้ยินเสียงอะไรในห้องเลย แต่น่าจะใช้เรื่องเสียงดูว่าอยู่หรือไม่อยู่ไม่ได้\nเพราะปกติฮานาโกะก็เป็นคนเงียบ ๆ"

# "Still, she wasn't in the tearoom. I try knocking lightly to make my presence known, but am surprised when I find the door unlocked and yielding at my touch."
"แต่ไม่ได้อยู่ที่ห้องน้ำชาแล้วแน่ ๆ ฉันลองเคาะเบา ๆ ให้รับรู้ว่าฉันมา ทว่าก็ต้องแปลกใจเมื่อลองบิดมือจับแล้วเปิดได้"

play sound sfx_door_creak

show hanako_door_door:
   easeout 1.0 xpos -0.2
show hanako_door_base:
   easeout 1.0 xpos 1.1
show bg school_dormhanako_ni:
   center
   easeout 1.0 xpos 0.55
with None

scene bg school_dormhanako
show hanako basic_distant:
    center
    ypos 1.15
with silentwhiteout

# "With a small creak, the door opens. It looks like my suspicions were correct; Hanako is indeed here. "
"ประตูเปิดพร้อมเสียงเอี๊ยดเบา ๆ ดูท่าว่าฉันจะคิดถูกแล้ว ฮานาโกะอยู่ที่นี่จริง ๆ"

# "She's sitting at the table with an open book in front of her, but pays it no heed as she keeps looking out the window. She looks utterly oblivious to my presence."
"ฮานาโกะนั่งอยู่ที่โต๊ะโดยมีหนังสือวางอยู่ตรงหน้า แต่เธอมองออกไปนอกหน้าต่างไม่ได้สนใจอ่านเลย เหมือนจะ\nยังไม่รู้เลยว่าฉันอยู่ตรงนี้"

# "With her head thoughtfully resting on her hand, she looks calm and collected. It's a shame she can't look like this more often."
"เธอนั่งเท้าคางครุ่นคิดดูสงบและใจเย็น น่าเสียดายที่ฮานาโกะไม่ได้ทำตัวแบบนี้บ่อย ๆ"

show hanako basic_distant_close:
    center
    ypos 1.1
with characlose

# "Smiling a little, I walk up to the table and softly speak to her."
"ฉันยิ้มบาง ๆ เดินไปที่โต๊ะคุยกับเธอเสียงเบา"

# hi "Good evening, Hanako."
hi "สายัณห์สวัสดิ์ ฮานาโกะ"

show hanako basic_normal_close
with charachange

# "Hanako's head turns a little to see me, but she's still only half there. I put a hand on the table and lower my head to better look at her face, mildly curious about what mood she's in."
"ฮานาโกะหันหน้ามาทางฉันเล็กน้อยโดยที่ยังไม่รู้ตัวดี ฉันวางมือลงบนโต๊ะแล้วก้มหัวลงมองหน้าเธอ\nด้วยความสงสัยเล็กน้อยว่ารู้สึกอย่างไรอยู่"

# hi "What's up?"
hi "ทำอะไรอยู่เหรอ"

show hanako basic_worry_close
with Dissolve(0.2)

# "She gasps a little, finally acknowledging my presence in the room for the first time."
"เธอสะดุ้งเฮือกเมื่อรับรู้ถึงตัวตนฉันที่อยู่ในห้องนี้ได้เต็มตื่นเป็นครั้งแรกเสียที"

# "Hanako's blushing really heavily. Her mouth is open just a little, as if paused midsentence. Most striking, though, is what she's doing."
"ฮานาโกะหน้าแดงก่ำ เธอเผยอปากคล้ายชะงักไปตอนกำลังพูดอยู่ แต่ที่เด่นที่สุดคือสิ่งที่เธอกำลังทำอยู่"

scene ev hanako_eye:
    truecenter
    subpixel True zoom 0.9
    acdc_warp 20.0 zoom 1.0
with locationchange

# "She's looking directly at me. Her eyes are pinned on my own, from such a close distance that I can almost see my reflection in them. They don't turn away, nor move at all. They're absolutely still, just looking into mine."
"ฮานาโกะมองหน้าตรง ๆ จ้องตาฉันในระยะที่ใกล้ชนิดที่ว่าฉันแทบจะเห็นเงาสะท้อนตัวเองในนั้นได้ นัยน์ตาคู่นั้น\nไม่เลื่อนหนีหรือขยับเขยื้อน เพียงอยู่นิ่งสนิทมองเข้ามาในตาฉัน"

# "They're dark, and give her an almost analytical air. Even when reading on subjects she has no interest in, she would appear to be rapt in her work to a casual observer. She absorbs information very well, and even now, I can feel that."
"ดวงตาสีดำสนิทนั้นทำให้ฮานาโกะดูเป็นคนชอบเพ่งพินิจ แม้แต่ตอนที่กำลังอ่านวิชาที่ตัวเองไม่ได้สนใจเลย\nคนนอกก็อาจยังมองได้ว่าเธอจดจ่ออยู่ ฮานาโกะซึมซับข้อมูลได้ดีเยี่ยม ซึ่งตอนนี้เองฉันก็ยังรู้สึกได้ว่าอย่างนั้น"

# "I feel like I'm seeing something behind those eyes that I never saw before. I don't know what it is, though."
"เหมือนว่าฉันจะเห็นบางอย่างที่อยู่เบื้องหลังดวงตาคู่นั้นซึ่งฉันไม่เคยเห็นมาก่อน แต่ฉันก็ไม่รู้ว่าสิ่งนั้นคืออะไร"

# hi "Hanako…?"
hi "ฮานาโกะ…?"

# "Her lips move just a little, silently mouthing something. She looks like she's on the verge of saying something, but won't say it."
"ริมฝีปากเธอขยับเล็กน้อยเป็นคำพูดบางอย่างอยู่เงียบ ๆ เหมือนกำลังจะพูดอะไรสักอย่างแต่ก็ไม่ยอมพูด"

# "But that's the way Hanako always is. On the verge of saying something, but never quite doing it. As I look intently into her eyes, I realize something."
"แต่ฮานาโกะก็เป็นแบบนี้เสมอ จะพูดอะไรแต่ก็ไม่ค่อยได้พูด ระหว่างที่จดจ้องอยู่กับตาเธอนั้นฉันก็นึกอะไรได้"

# "Everyone has their own thoughts, things they want to say, their own worldview. But I can't work out what Hanako wants to say, and I can't work out what she's thinking. I never have been able to."
"คนเราต่างมีความคิดเป็นของตัวเอง สิ่งที่ตัวเองอยากพูด มุมมองต่อโลกของตัวเอง แต่ฉันคิดไม่ออกเลยว่าฮานาโกะ\nอยากพูดอะไร คิดไม่ออกเลยว่าเธอคิดอะไร ไม่เคยคิดออกเลย"

# "It's frustrating. It feels like I don't know her at all, despite all the time we've spent together."
"ซึ่งชวนให้หงุดหงิดเพราะเหมือนกับว่าฉันไม่ได้รู้จักเธอเลย ทั้งที่อยู่ด้วยกันบ่อยขนาดนี้"

# ha "Hi… sao…"
ha "ฮิ… ซาโอะ…"

scene bg school_dormhanako
show hanako basic_worry_close
with charachange

# "It's only now that I find myself blushing. I've been looking directly into Hanako's eyes from such a short distance with absolutely no regard for her, and she's been looking into mine without shirking away."
"ฉันเพิ่งรู้ตัวว่าตัวเองหน้าแดงก็ตอนนี้เอง ฉันมองตาฮานาโกะตรง ๆ ในระยะประชิดขนาดนี้โดยไม่ได้สนใจเธอเลย\nส่วนเธอก็มองตาฉันไม่หลบไปทางอื่น"

show hanako emb_downtimid_close
with charachange

# "I quickly look away while covering my face with my hand. Hanako does just the same."
"ฉันรีบเบือนหน้าหนีพลางเอามือปิดหน้าไว้ ฮานาโกะก็ทำเหมือนกัน"

# "Another awkward silence reigns. I hate these. At first I accepted them as just being a fact of life around Hanako, but now all they feel like is an affirmation of how little we're able to communicate."
"ความเงียบชวนอึดอัดเข้าครองอีกแล้ว ทีแรกฉันรับได้แล้วก็จริงว่าการอยู่กับฮานาโกะย่อมมีความเงียบด้วย แต่ตอนนี้\nยิ่งเหมือนมาตอกย้ำว่าเราสื่อสารกันน้อยแค่ไหน"

# "Some anger makes its way in the complex mixture of emotions I'm experiencing right now. I want to bridge that gap between us. Friends shouldn't have to tiptoe around each other like this."
"ในกลุ่มอารมณ์ที่คละกันในใจตอนนี้มีความโกรธปนอยู่บางส่วน ฉันอยากจะอุดช่องว่างระหว่างเรา เพื่อนกันไม่ควรมา\nอ้ำ ๆ อึ้ง ๆ ใส่กันแบบนี้สิ"

# "I speak before I can argue myself out of what I'm going to do. My scarring isn't as bad as Hanako's, and I can't possibly compare my life to hers, but I want to show her that she's not alone."
"ฉันพูดออกไปก่อนจะทันได้เถียงกับตัวเองว่าต้องทำอะไรต่อ แผลเป็นของฉันไม่ได้หนักเท่าฮานาโกะ และชีวิตฉัน\nก็เทียบกับเธอไม่ได้เลยด้วย แต่ฉันอยากทำให้เธอได้เห็นว่าเธอไม่ได้อยู่ตัวคนเดียว"

# "Doing this in such a blunt manner might be the only way to get my point across."
"ทำอะไรแบบนี้ตรง ๆ ไปเลยคงจะเป็นวิธีเดียวที่จะสื่อสิ่งที่ฉันอยากบอกได้"

# hi "Hanako… I want to show you something."
hi "ฮานาโกะ… ฉันมีบางอย่างที่อยากให้เธอได้เห็น"

show hanako emb_timid_close
with charachange

# "I take a deep breath to prepare myself. This could backfire badly, but I feel as if we've come close enough for this to be okay."
"ฉันสูดหายใจลึก ๆ เป็นการเตรียมใจ ทำแบบนี้แล้วอาจเกิดผลร้ายหนักขึ้นได้ แต่ฉันว่าเราสนิทกันพอที่จะทำแบบนี้\nแล้วละ"

# hi "I'm not going to strip naked or anything weird, I'm just going to take off my shirt."
hi "ฉันไม่ได้จะแก้ผ้าเปลือยหรือทำอะไรแปลก ๆ นะ แค่จะถอดเสื้อเฉย ๆ"

show hanako def_shock_close at center
with dissolvecharamove

# "Hanako's eyes grow to the size of saucers. Her face is an amusing mixture of curiosity and nervousness as she stands. It helps take the edge off my own nervousness at doing this in front of another person."
"ฮานาโกะทำตาโต เธอยืนขึ้นพร้อมสีหน้าที่มีทั้งความอยากรู้กับความประหม่าระคนกันชวนขัน ซึ่งช่วยให้ฉันเอง\nหายขัดเขินไปได้บ้างที่ต้องทำแบบนี้ต่อหน้าคนอื่น"

play sound sfx_rustling

# "Slowly, with my entire body feeling tense, I unknot my tie and begin to loose the first of the buttons. I'm trying to mentally block out Hanako to make this easier, but it's not really working."
"ฉันค่อย ๆ ปลดเน็กไทออกแล้วแกะกระดุมเม็ดแรกทั้งที่เกร็งไปทั้งตัว ฉันพยายามหลอกตัวเองว่าฮานาโกะไม่ได้\nอยู่ตรงนี้เพื่อความสบายใจของตัวเอง แต่ไม่ได้ผลเท่าไหร่"

# "As I work my way down, I expect to hear some form of protest from her. She remains silent, though, which just makes this feel even stranger."
"ในใจฉันคิดไปว่าฮานาโกะคงบอกให้หยุดหรืออะไรบ้างระหว่างที่แกะกระดุมลงไปเรื่อย ๆ แต่เธอก็เงียบ ซึ่งยิ่งทำให้\nรู้สึกแปลกเข้าไปอีก"

# "With the last of my shirt unbuttoned, I take a breath and look at her."
"พอแกะกระดุมเสื้อเม็ดสุดท้ายออกแล้วฉันก็สูดหายใจและมองฮานาโกะ"

scene ev hisao_scar_large:
    xanchor 0 yanchor 0 xpos -600 ypos -140 
with whiteout

play music music_heart fadein 0.5

# "Hanako's gaze is fixed on my scarring, as expected, and once I nod to say it's okay, she steps forward and tentatively places her hand on the vertical line running down my chest."
"สายตาฮานาโกะจดจ่ออยู่ที่แผลเป็นของฉันตามคาด และเมื่อฉันพยักหน้าอนุญาตแล้วเธอก็เดินเข้ามาวางมือไว้\nที่รอยเส้นตรงที่หน้าอกฉันอย่างกล้า ๆ กลัว ๆ"

show ev hisao_scar_large:
    ease 1.0 xpos 0 ypos -290

# "The scarring on her hand, a pattern of damaged skin across its surface, contrasts with the single uniform line that makes up mine. Her hand isn't trembling at all, unlike what I predicted."
"แผลเป็นบนมือเธอที่เป็นลายไปทั่วจากผิวหนังที่เสียหายนั้นขัดกับแผลเป็นของฉันที่เป็นเส้นเดี่ยว มือเธอไม่สั่นเลย\nซึ่งผิดไปจากที่เดาไว้"

# ha "This is…"
ha "นี่มัน…"

# hi "The scar from the surgery that followed my heart attack. The surgeons had to cut open my chest to operate on my heart."
hi "แผลเป็นจากการผ่าตัดหัวใจที่ฉันหัวใจวายน่ะ หมอต้องผ่าเปิดตรงอกเพื่อผ่าตัดหัวใจฉัน"

show ev hisao_scar_large:
    ease 1.0 xpos -600 ypos -140 

# ha "I never knew…"
ha "ไม่เคยรู้เลย…"

# "Hanako's words are calmer and softer than usual. The soft feeling of her fingers moving from my scar to my breast makes me hesitate a little before continuing on."
"น้ำเสียงฮานาโกะฟังดูสงบและแผ่วเบากว่าทุกที สัมผัสนุ่มนวลจากนิ้วเธอที่ลากจากแผลเป็นไปยังหน้าอกทำฉันลังเล\nเล็กน้อย จากนั้นฉันก็พูดต่อ"

# hi "You're the first person to see this since I left the hospital."
hi "เธอเป็นคนแรกเลยนะที่ได้เห็นตั้งแต่ตอนฉันออกโรงพยาบาลมา"

scene ev hisao_scar:
    truecenter
    zoom 1.05 subpixel True
    easein 8.0 zoom 1.0
with flash

# ha "But… why are you showing this to me?"
ha "แต่… ทำไมถึงมาเปิดให้ฉันดูล่ะ"

# hi "I wanted to prove to myself that I could do this; that I could accept my past and move on. I wanted to show that to you, as well."
hi "ฉันอยากจะพิสูจน์กับตัวเองว่าฉันทำแบบนี้ได้ ว่าฉันยอมรับและก้าวข้ามอดีตได้ และฉันก็อยากพิสูจน์ให้เธอ\nได้เห็นด้วย"

# "She nods. From her reaction, she seems to know how difficult this is for me. More than anything, this scar represents a visible reminder of my condition. A reminder that I'm not “normal” any more."
"ฮานาโกะพยักหน้า ดูจากปฏิกิริยาแล้วเธอก็คงรู้ว่าฉันต้องใช้ความกล้าขนาดไหนถึงทำแบบนี้ได้ แต่ที่สำคัญที่สุด\nแผลเป็นนี้คือเครื่องเตือนให้เห็นถึงอาการของฉัน เตือนว่าฉันไม่ “ปกติ” อีกต่อไปแล้ว"

# "That's something that, until now, I had tried my hardest to ignore."
"เป็นสิ่งที่ก่อนหน้านี้ฉันพยายามเป็นอย่างยิ่งที่จะเมินมาตลอด"

# "As the minutes tick by, Hanako's gaze lingers. Her eyes look less focused on my scarring than before. The situation feels a bit different than it previously did, and makes me feel slightly uncomfortable."
"สายตาของฮานาโกะยังไม่ไปไหนอยู่สองสามนาที แต่เธอไม่ได้จ้องอยู่แค่ที่แผลเป็นเหมือนอย่างเมื่อกี้แล้ว สถานการณ์\nตอนนี้ต่างออกไปจากก่อนหน้านี้เล็กน้อยจนฉันอึดอัดขึ้นมาหน่อย ๆ"

scene bg school_dormhanako
show hanako basic_normal_close at center
with silentwhiteout

# "Her hand retreats, and I draw my shirt closed and begin to button it up. Her blushing face suddenly returns to its typical tense and timid state as she looks away."
"ฮานาโกะถอนมือออกไป ส่วนฉันก็ใส่เสื้อกลับแล้วติดกระดุมเข้าดังเดิม อยู่ ๆ เธอบิดหน้าที่ขึ้นสีแดงเรื่อของเธอ\nซึ่งกลับไปเกร็ง ๆ อาย ๆ อย่างทุกทีหนี"

# "The room is completely silent as I fix my shirt and tie, feeling put off after such an unexpectedly intimate moment."
"ในห้องนั้นเงียบฉี่ ฉันจัดแจงเสื้อกับเน็กไทตัวเองพร้อมความรู้สึกประหลาดที่อยู่ ๆ ก็ต้องเจอเหตุการณ์เปิดใจใกล้ชิด\nแบบไม่คาดฝัน"

# hi "So… I guess you're not the only one that's scarred."
hi "แปลว่า… คนที่มีบาดแผลคงไม่ได้มีแค่เธอสินะ"

show hanako basic_smile_close
with charachange

# "Hanako smiles a little at the joke, thankfully lightening the atmosphere a bit."
"ฮานาโกะยิ้มบาง ๆ กับมุกนั้นของฉัน โชคดีที่บรรยากาศดูหายเครียดลงบ้างแล้ว"

# ha "Thank you… H-Hisao. I think… I understand."
ha "ขอบคุณนะ… ฮะ-ฮิซาโอะ ฉันว่า… ฉันเข้าใจแล้วละ"

# "I give a long sigh of relief. I really didn't know how she'd take it, but I'm glad everything seems to have worked out as I hoped. Hanako's smile only proves that further."
"ฉันถอนหายใจยาวด้วยความโล่งใจ ฉันไม่รู้ว่าฮานาโกะจะคิดอย่างไร แต่ก็ดีใจที่เหมือนทุกอย่างจะเป็นไปตามที่หวังไว้\nรอยยิ้มของฮานาโกะยิ่งย้ำชัดว่าเป็นเช่นนั้น"

# "I'm finding the path I want to follow now, and what Hanako needs to do is to find her own. It's something I can't help her with, and it's something that she needs to overcome her past in order to do."
"ฉันกำลังค้นหาเส้นทางที่ฉันอยากออกเดิน และสิ่งที่ฮานาโกะต้องทำคือการค้นหาเส้นทางของตัวเองบ้าง ซึ่งฉัน\nช่วยตรงนั้นไม่ได้ เป็นสิ่งที่เธอต้องก้าวข้ามอดีตของตัวเองให้ได้ก่อนถึงจะทำได้"

show hanako basic_distant_close
with charachange

# "Hanako checks her watch. It's getting late by now."
"ฮานาโกะดูนาฬิกา ตอนนี้เริ่มค่ำแล้ว"

show hanako basic_worry_close
with charachange

# ha "Hisao… um…"
ha "ฮิซาโอะ… เอ่อ…"

# hi "Yeah, I'd better be going. I'll be thankful for some sleep. It's been a long day, after all."
hi "อื้ม เดี๋ยวต้องไปละ อยากหลับอยู่เหมือนกัน วันนี้มีแต่อะไรหลายอย่างเลย"

# hi "Good night, Hanako."
hi "ฝันดีนะฮานาโกะ"

show hanako basic_bashful_close
with charachange

# ha "G-good night."
ha "ฝะ-ฝันดี"

stop music fadeout 3.0

scene bg school_girlsdormhall
with locationchange

# "I make my way out of her room and into the hallway, remaining silent as I do so. I think both of us have gone through a few emotions today."
"ฉันเดินออกมาจากห้องมาที่โถงทางเดินเงียบ ๆ ฉันว่าวันนี้เราทั้งสองคนต่างก็ได้รู้สึกอะไรบางอย่างแล้วละ"

scene black
with dissolve

#*********************

label th_H28:

scene bg city_street1
with locationchange

play music music_daily fadein 2.0
$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_traffic fadein 2.0

# "The heat of the summertime sun beats down on my sweating brow. Dabbing with a handkerchief doesn't help too much in making me any more comfortable."
"ความร้อนจากแดดฤดูร้อนส่องกระทบคิ้วเปียกเหงื่อของฉัน ใช้ผ้าเช็ดหน้าเช็ดเหงื่อแล้วก็ไม่ได้ช่วยให้รู้สึกสบายตัว\nขึ้นมาเท่าไหร่เลย"

# "Giving up on the idea of getting more done today, I stop and lean against one of the overpass fences, resting my bag on the ground."
"ฉันล้มเลิกความคิดที่จะไปทำอะไรต่อแล้ววางกระเป๋าลงกับพืื้นยืนพิงรั้วทางยกระดับ"

# "The stores in the town below Yamaku are well-stocked and offer enough variety for me to get by, but at least an occasional shopping trip to the city is something that can't really be avoided."
"ร้านในเมืองข้างล่างยามากุนั้นมีของครบครันและหลากหลายพอให้ฉันอยู่ได้แล้วก็จริง แต่อย่างไรบางครั้งก็เลี่ยงไม่ได้\nที่จะต้องเข้ามาซื้อของในตัวเมือง"

# "I've been here a few times, now. The city's layout is getting more familiar, and the nostalgia from its atmosphere is beginning to wear off."
"ฉันมาที่นี่สองสามครั้งได้แล้วจนเริ่มชินกับผังเมืองขึ้นมาและความรู้สึกชวนคิดถึงเริ่มจางลงไป"

# "I realize that I've begun to wheeze. I sound like an old man that's overexerted himself, and having to connect that to the fact that I'm the source is a bit disturbing."
"ฉันเริ่มหืดขึ้นคอแล้ว ฟังดูอย่างกับคนแก่ที่ฝืนออกแรงมากไปเลย แล้วยิ่งฉันเป็นคนทำเสียงแบบนั้นอีก\nก็ยิ่งทำให้รู้สึกขนลุกขึ้นมา"

# "I put a hand on my chest and concentrate for a bit to make sure I haven't gone far enough to cause any further problems."
"ฉันทาบมือไว้กับหน้าอกแล้วตั้งสมาธิเล็กน้อยให้แน่ใจว่าอาการตอนนี้ยังไม่ถึงขั้นที่จะเป็นปัญหาอะไรอีก"

# "Thankfully, my heart is acting normally. There's no dull pain, and the beating is regular, albeit fast-paced, as I recover from overdoing things in this kind of heat."
"โชคดีที่หัวใจฉันยังปกติ ไม่ได้ปวดหนึบ จังหวะยังสม่ำเสมอถึงจะเร็วอยู่ ฉันพักให้หายเหนื่อยจากการทำอะไรเกินตัว\nท่ามกลางอากาศร้อน ๆ แบบนี้"

# "I hate my body. It's frustrating to be held back, even more to be held back by fear of my life being ended, when doing something as simple as walking around the city for a while."
"ไม่ชอบร่างกายตัวเองเลย พอมีอะไรมาฉุดไว้แล้วก็หงุดหงิด ยิ่งสิ่งที่ฉุดนั้นคือความกลัวว่าชีวิตจะจบลงแล้วด้วย ทั้งที่\nก็แค่มาเดินในตัวเมืองอยู่แป๊บ ๆ เท่านั้นเอง"

$ renpy.music.set_volume(0.2, 0.0, channel="sound")
play sound sfx_phone

# "As I ponder on my health, I feel my pocket vibrating. By the time my phone's begun to ring, my hand is already fishing for it."
"ระหว่างที่ใคร่ครวญถึงเรื่องสุขภาพตัวเองอยู่กระเป๋ากางเกงก็สั่นขึ้นมา กว่าเสียงเรียกเข้าจะดังฉันก็ตะปบมือ\nหาโทรศัพท์ไปก่อนแล้ว"

# "A glance at the screen shows a caller number I don't recognize. Strange."
"เมื่อมองหน้าจอโทรศัพท์ก็เห็นว่าเป็นเบอร์โทร. ที่ไม่คุ้นเลย แปลก"

$ renpy.music.set_volume(0.1, 2.0, channel="ambient")
$ renpy.music.set_volume(0.5, 2.0, channel="music")

scene bg city_street1_blurred
show phone mobile:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with locationchange
with Pause (0.5)

# "Shrugging, I press the button to answer the call and bring the phone to my ear."
"ฉันยักไหล่ก่อนจะกดรับสายแล้วยกโทรศัพท์ขึ้นมาไว้ข้างหู"

# hi "Hello, Hisao Nakai speaking."
hi "ฮัลโหลครับ ฮิซาโอะ นากาอิครับ"

mystery "…"

# "The sound of a couple of short breaths can be heard, but no actual speech is forthcoming."
"เสียงหายใจเข้าออกสองสามทีดังลอดมา แต่ไม่มีคำพูดใด ๆ"

# hi "Hello?"
hi "ฮัลโหล?"

# ha "H… Hisao?"
ha "ฮะ… ฮิซาโอะ?"

# "It's Hanako. Her voice is really easy to place, even if I've never heard it over a phone before."
"ฮานาโกะน่ะเอง เสียงฮานาโกะฟังออกง่ายมาก ถึงจะไม่เคยได้ยินเสียงเธอผ่านโทรศัพท์มาก่อนก็ตาม"

# hi "Hanako? Sorry, I wasn't expecting you to call. What's up?"
hi "ฮานาโกะเหรอ ขอโทษที พอดีไม่คิดว่าเธอจะโทร. มา มีอะไรเหรอ"

# ha "U-um… I… um…"
ha "อะ-เอ่อ… ฉัน… เอ่อ…"

# ha "If… if you're not busy… I-I was wondering if y-you would… l-like to… m—"
ha "ถ้า… นายไม่ติดธุระอะไร… ฉะ-ฉันไม่รู่ว่านะ-นาย… จะ-จะมา… เจอ—"

# hi "Meet up?"
hi "เจอกัน?"

# ha "Yes! U-um… I mean…"
ha "อื้ม! อะ-เอ่อ… คือ…"

# "She sounds really wound up about this. I can hear muffled voices in the background, and it's about time for afternoon tea, so I guess she'll want me to meet her at the Shanghai or something."
"ฮานาโกะฟังดูตื่นเต้นมาก ฉันได้ยินเสียงอู้อี้แว่ว ๆ มาด้วย ตอนนี้ก็ถึงเวลาดื่มชายามบ่ายแล้ว อาจจะอยากให้ไปเจอกัน\nที่ร้านเซี่ยงไฮ้หรืออะไรมั้ง"

# hi "That sounds fine. Are you at the Shanghai?"
hi "ก็ได้นะ อยู่ที่ร้านเซี่ยงไฮ้เหรอ"

# ha "I-I'm in… the city…"
ha "ฉะ-ฉันอยู่… ในตัวเมือง…"

# "Hanako's here? Alone? That's a surprise. It's little wonder she's like this, if she's surrounded by people and entirely by herself."
"ฮานาโกะมาที่นี่? ตัวคนเดียว? ทึ่งแฮะ ก็ไม่แปลกเลยที่เธอจะเป็นแบบนี้ถ้ามาตัวคนเดียวแล้วรอบตัวมีแต่ผู้คน"

# hi "That works out well; I'm just wandering around there now. Where are you?"
hi "ได้สิ ตอนนี้ฉันก็อยู่แถว ๆ นี้แหละ เธออยู่ไหน"

# "Hanako manages to stammer out the street name, address, and some basic directions to where she is. Luckily It's not too far, so I agree to see her soon before hanging up."
"ฮานาโกะบอกชื่อถนน ที่อยู่ กับทางไปแบบคร่าว ๆ ว่าอยู่ตรงไหนแบบอึก ๆ อัก ๆ โชคดีที่อยู่ไม่ไกลจากตรงนี้มาก\nฉันจึงตอบตกลงว่าเดี๋ยวจะไปหาก่อนวางสาย"

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
$ renpy.music.set_volume(1.0, 1.0, channel="music")
stop ambient fadeout 2.0

show phone mobile:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 0.5 ypos 0.6
with None

scene bg misc_sky
with locationchange

stop music fadeout 5.0

# "I look up to the sky. The summer heat is beating down."
"ฉันแหงนหน้ามองท้องฟ้า ความร้อนจากฤดูร้อนเริ่มลดระดับลงแล้ว"

# "This is the first time Hanako's asked for us to do something together beyond a simple board game, and the first time, at least since I've known her, that she's come to the city by herself. Maybe this means that Lilly was right."
"เป็นครั้งแรกเลยที่ฮานาโกะชวนไปทำอะไรนอกเหนือจากการแค่เล่นบอร์ดเกมด้วยกัน และเป็นครั้งแรกด้วยที่\n—อย่างน้อยก็เท่าที่รู้จักกันมา—เธอเข้าตัวเมืองตัวคนเดียว ซึ่งอาจจะแปลว่าลิลลี่พูดถูกแล้วก็ได้"

scene bg city_karaokeint
with shorttimeskip

$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_soothing fadein 2.0
$ renpy.music.set_volume(0.4, 0.0, channel="ambient")
play ambient sfx_crowd_outdoors fadein 2.0

# "By the time I manage to stagger up to the café where Hanako is, I've started to wheeze again. I'm sweating so much that I feel like a melting popsicle, and can barely hold the bag in my hand."
"กว่าจะเดินตุปัดตุเป๋มาจนถึงคาเฟที่ฮานาโกะอยู่ได้ฉันก็หืดขึ้นคออีกรอบแล้ว เหงื่อท่วมตัวจนเหมือนเป็นไอศกรีม\nที่กำลังละลาย แทบไม่มีแรงถือกระเป๋าแล้วด้วย"

# "I need to sit down, badly."
"ฉันต้องนั่ง ไม่ไหวแล้ว"

# "The tables outside are all occupied by busily chatting couples and girls gossiping between themselves. The contrast between the different age groups and fashions of the people here and the people from the town near Yamaku is striking."
"โต๊ะข้างนอกทุกตัวต่างมีคู่รักที่คุยกันไม่หยุดหรือไม่ก็กลุ่มสาว ๆ ที่คุยกันอย่างออกรสนั่งอยู่กันหมดแล้ว เห็นได้ชัด\nว่าอายุและรสนิยมการแต่งตัวของคนที่นี่นั้นต่างจากคนในเมืองในละแวกยามากุโดยสิ้นเชิง"

# "I scan over the people sitting at the tables, but I can't see Hanako. She did say she was sitting outside, so I must just be missing her. Not difficult, given how small she usually tries to make her presence."
"ฉันกวาดตาไปตามคนที่นั่งอยู่แต่ละโต๊ะแต่ก็ไม่เห็นฮานาโกะ เห็นบอกว่านั่งอยู่ข้างนอก ฉันอาจจะไม่ทันได้สังเกตก็ได้\nซึ่งก็เป็นไปได้เพราะปกติฮานาโกะจะทำตัวลีบตลอด"

# "I look around again, more slowly this time, taking particular care to see if I can find Hanako's hat. It's pretty distinctive, and I'd be very surprised if she wasn't wearing it."
"ฉันมองไปรอบ ๆ อีกครั้ง แต่คราวนี้เลื่อนหัวให้ช้าลงแล้วตั้งใจมองว่าหมวกฮานาโกะอยู่ตรงไหน หมวกใบนั้นเป็นหมวก\nที่เด่นพอตัว และถ้าฮานาโกะไม่ใส่มาแล้วฉันก็คงจะแปลกใจมาก"

# "There she is. Sure enough, her head is kept low and the table she's sitting at is right beside the building in an inconspicuous corner."
"อยู่นั่นไง ใช่แล้ว ฮานาโกะนั่งก้มหัวต่ำอยู่ตรงโต๊ะข้าง ๆ อาคารซึ่งเป็นมุมอับ"

$ renpy.music.set_volume(0.2, 4.0, channel="ambient")

# "I walk up to where she is and make sure that I have her attention before I sit, lest I give her a scare. She notices me, and gives a small wave as I arrive at her table."
"ฉันเดินไปที่โต๊ะที่ฮานาโกะนั่งอยู่แล้วดูให้แน่ใจว่าเธอรู้แล้วว่าฉันมาก่อนจะนั่งเพื่อไม่ให้เธอตกใจ พอฮานาโกะ\nเห็นฉันแล้วเธอก็โบกมือให้เบา ๆ ระหว่างที่ฉันเดินไปหา"

show hanako basic_worry_cas_close:
    center
    ypos 1.1
with charaenter

# ha "A-are you feeling okay?"
ha "นะ-นายไหวมั้ย"

# "I try my best to laugh it off, but doing so just makes me more out of breath."
"ฉันทำท่าจะหัวเราะบอกปัดไป แต่ยิ่งทำแบบนั้นก็ยิ่งหอบไปใหญ่"

# hi "Not very fit these days. Don't mind me."
hi "เดี๋ยวนี้ไม่ค่อยฟิตเลย ไม่ต้องสนใจฉันหรอก"

show hanako basic_distant_cas_close
with charachange

# "Hanako nods, but still looks a bit put off."
"ฮานาโกะพยักหน้าทั้งที่ยังทำสีหน้ารู้สึกแปลก ๆ"

# "Now that I can get a good look at her face, something about her seems a bit different. I'm not sure if my eyes are playing tricks on me, but she looks kind of nice."
"พอได้มาดูชัด ๆ แล้วก็รู้สึกว่าฮานาโกะเปลี่ยนไปเล็กน้อย ไม่รู้ว่าฉันหลอนไปเองหรือเปล่า แต่ฮานาโกะดูดีใช้ได้เลย"

show hanako basic_normal_cas_close
with charachange

show hanako basic_distant_cas_close
with charachange

# "Her eyes move upwards to look at me, before quickly flicking down again. I begin to think this is going to be a rather quiet meeting, but a waitress thankfully arrives and sets down a cup of tea in front of Hanako."
"ฮานาโกะเหล่ตาขึ้นมามองฉันก่อนจะกลับไปมองพื้นเหมือนเดิม ชักคิดแล้วว่าคงจะได้กลายเป็นนัดเงียบแล้วแน่ ๆ\nแต่โชคดีที่บริกรมาวางถ้วยชาลงตรงหน้าฮานาโกะให้พอดี"

show hanako emb_downtimid_cas_close
with charachange

# "Hanako almost automatically turns slightly away and lowers the side of her head. It's an amazingly practiced motion, and does a good job of its intended purpose - hiding her scars from someone who's leaning in close."
"ฮานาโกะหันไปมองเล็กน้อยในทันทีก่อนจะบิดขมับลง เป็นท่าทางที่เป็นธรรมชาติอย่างน่าทึ่งและทำหน้าที่\nในการปกปิดแผลเป็นไม่ให้คนที่โน้มตัวเข้ามาเห็นได้เป็นอย่างดีตามที่ตั้งใจไว้"

# "Her right arm is still laying on the table though, with the scarring on the back of her hand quite visible. It catches the waitress's eye, and I move to quickly distract her."
"แต่แขนขวาฮานาโกะที่มีแผลเป็นซึ่งเห็นได้ชัดอยู่หลังมือยังอยู่บนโต๊ะ บริกรสะดุดตาเข้ากับแผลเป็นนั้นฉันจึงรีบ\nเข้ามาขัดทันที"

# hi "Excuse me, may I place an order?"
hi "ขอโทษนะครับ ขอสั่งอะไรหน่อยได้ไหม"

# "The waitress nods and gives me a couple of seconds to look at the menu."
"บริกรพยักหน้าแล้วรอให้ฉันดูรายการของกิน"

# hi "Could I have a mango smoothie, please?"
hi "ขอมะม่วงปั่นหนึ่งที่ครับ"

# "She gives a nod before almost enthusiastically bouncing inside. Everything is so different in the city, in more ways than one."
"เธอพยักหน้าแล้วเดินกลับเข้าไปในร้านอย่างกระตือรือร้น พอเป็นในตัวเมืองแล้วอะไร ๆ ก็ไม่เหมือนเดิม ไม่ใช่แค่\nในแง่ใดแง่หนึ่ง"

show hanako emb_timid_cas_close
with charachange

# "Hanako looks back up towards me and adjusts her hat a little. If she noticed the waitress staring at her scars, she doesn't show it."
"ฮานาโกะเงยหน้าขึ้นมามองแล้วจัดหมวกเบา ๆ ถ้าสมมติเธอรู้ตัวว่าบริกรคนเมื่อกี้มองแผลเป็นจริง ๆ ก็แปลว่าเธอ\nเก็บอาการเก่งมาก"

# ha "N-not coffee…?"
ha "มะ-ไม่สั่งกาแฟเหรอ…"

# hi "I think I'd die from this heat if I had something like coffee right now."
hi "ร้อนแบบนี้ขืนกินกาแฟก็ได้ซี้แหงก่อนพอดี"

show hanako emb_downtimid_cas_close
with charachange

# "Resting my head in my hand, I look to my quiet companion. She seems taken aback; a very unexpected reaction to my lame joke. An unwelcome emotion bubbles up inside me as I realize her reason why."
"ฉันนั่งเท้าคางมองเพื่อนร่วมโต๊ะพูดน้อยของฉัน ฮานาโกะดูจะตกใจ ซึ่งฉันไม่ได้คิดเลยว่าเธอจะมีท่าทีแบบนี้กับมุกฝืด ๆ\nของฉัน พอนึกได้ว่าเป็นเพราะอะไรก็มีอารมณ์อันไม่พึงประสงค์ก่อตัวขึ้นในใจ"

# "Unlike most in Yamaku, indeed, unlike anyone there that I'm aware of, my condition goes beyond limiting the activities I can do. Or to be more precise, breaching those limits could have much more grave consequences."
"อาการของฉันนั้นไม่เหมือนคนอื่นในยามากุ—และแน่แท้ว่าไม่เหมือนกับใครคนอื่นเท่าที่ฉันพอรู้จักด้วย—ตรงที่ว่า\nอาการของฉันไม่ได้จำกัดแค่กิจกรรมที่ฉันทำได้ หรือจะพูดให้เจาะจงก็คือ การฝืนขีดจำกัดที่ว่านั้นอาจทำให้เกิดผล\nที่ร้ายแรงยิ่งกว่าตามมาได้"

# "Thankfully, it's something that's very rarely come up since I entered Yamaku. I thought that it was so rare that Hanako and Lilly might not think of it at all. It turns out that I was wrong."
"โชคดีที่อาการของฉันแทบไม่กำเริบเลยตั้งแต่มาอยู่ที่ยามากุ ฉันนึกว่าเกิดน้อยจนฮานาโกะกับลิลลี่อาจลืมไปแล้ว\nด้วยซ้ำ แต่ดูท่าว่าจะคิดผิด"

# "Hanako silently drinks her tea while I wait for my drink, confirming that it's the right temperature with a small sip before she begins in earnest."
"ฮานาโกะดื่มชาอยู่เงียบ ๆ โดยจิบดูก่อนว่าเย็นพอดื่มได้หรือยังก่อนจะดื่มไประหว่างที่ฉันรอเครื่องดื่มของตัวเอง"

# "I feel guilty for being the cause of an uncomfortable silence, since in the past I've been kind of hard on Hanako for those."
"รู้สึกผิดเลยแฮะที่ทำบรรยากาศเงียบไปแบบอึดอัดอย่างนี้ ยิ่งที่ผ่านมาฉันทำแบบนี้กับฮานาโกะบ่อย ๆ ด้วย"

# "Eventually the same waitress as before bounces up, handing me my drink. I gather change from my pocket and drop it into her waiting hand, before she goes off to attend to another customer. My eyes linger on her as she walks away."
"จนในที่สุดบริกรคนเดิมก็โผล่มาพร้อมเครื่องดื่มของฉัน ฉันล้วงเศษเงินในกระเป๋าใส่มือเธอที่ยื่นมารอรับเงิน จากนั้นเธอก็เดินไปบริการลูกค้าคนอื่นต่อ ฉันมองตามเธอที่เดินออกไป"

show hanako emb_sad_cas_close
with charachange

# ha "Do you think that she looks… pretty…?"
ha "นายว่าเขา… น่ารักเหรอ…"

# "Hanako is following my gaze, her eyes taking in the waitress that served us. I can feel my blood slowly going to my cheeks as I rest my smoothie back on the table."
"ฮานาโกะมองตามสายตาฉันไปและมองบริกรที่มาเสิร์ฟเครื่องดื่มให้เรา ฉันวางแก้วมะม่วงปั่นลงพร้อมความรู้สึก\nที่เหมือนเลือดค่อย ๆ เดินขึ้นมาที่แก้ม"

# hi "Nah, can't really say that I'm really into that look. She just looked a lot like an old friend I knew before my heart attack."
hi "ไม่อะ ไม่ค่อยตรงสเป็กเท่าไหร่ แค่ว่าหน้าเหมือนเพื่อนเก่าที่รู้จักกันก่อนฉันหัวใจวายรอบนั้นน่ะ"

show hanako basic_worry_cas_close
with charachange

# ha "Did you… have many friends?"
ha "นาย… มีเพื่อนเยอะเหรอ"

# hi "I had a few at my previous school, though I wouldn't say a lot. The four of us just hung around together after school and stuff."
hi "ที่โรงเรียนเก่าก็มีอยู่บ้าง ไม่ได้เยอะหรอก ส่วนมากเราสี่คนก็ไปเฮฮากันตามประสาหลังเลิกเรียนน่ะ"

show hanako basic_normal_cas_close
with charachange

# ha "Do you still talk to them?"
ha "ยังคุยกับพวกนั้นอยู่มั้ย"

# "I shake my head."
"ฉันสั่นหัว"

# hi "No. We gradually lost contact while I was stuck in the hospital."
hi "ไม่อะ พวกเราค่อย ๆ ขาดการติดต่อกันไปตอนฉันนอนโรงพยาบาล"

show hanako cover_worry_cas_close
with charachange

# ha "You're not… saddened by that? Or angry?"
ha "นายไม่… เศร้าเหรอ ไม่โกรธเลยเหรอ"

# "Hanako looks genuinely surprised. I guess it's the right reaction."
"ฮานาโกะดูประหลาดใจจริง ๆ แต่จะคิดแบบนั้นก็คงไม่แปลก"

# hi "Well, life did move on for them while I was stuck in the ward. I was pretty sore about it at the time, but now it's just a bunch of nice memories."
hi "ก็นะ ชีวิตพวกนั้นก็เดินหน้าต่อช่วงที่ฉันต้องนอนอยู่โรงพยาบาล ตอนนั้นฉันก็เจ็บใจอยู่ แต่ตอนนี้มันก็เป็นแค่\nความทรงจำดี ๆ เท่านั้นละ"

# hi "Besides, once I came to Yamaku I found new friends as well."
hi "อีกอย่าง พอมายามากุแล้วฉันก็ได้เพื่อนใหม่ด้วย"

# "That's quite a whitewash of what my feelings were back then. I went through some dark times during my stay at the hospital, and I really am glad that Hanako and Lilly were around to help me after I left it."
"คำพูดนั้นยังนับว่าน้อยถ้าเทียบกับความรู้สึกตอนนั้นจริง ๆ ตอนอยู่โรงพยาบาลนั้นถือว่าเป็นช่วงมืดบอดของชีวิตฉันเลย\nก็ว่าได้ และฉันก็ดีใจที่ได้ฮานาโกะกับลิลลี่คอยอยู่ช่วยฉันหลังจากที่ฉันออกจากโรงพยาบาลแล้ว"

show hanako basic_bashful_cas_close
with charachange

# "Hanako blushes as we both get down to enjoying our drinks. She seems to have calmed down since I arrived, and I've started to feel a little better now that I've had the chance to rest a bit, so this is getting to be a nice outing already."
"ฮานาโกะหน้าแดง เราสองคนต่างดื่มเครื่องดื่มของตัวเองกันต่อ เหมือนว่าตั้งแต่ฉันมาหาฮานาโกะดูจะใจเย็นลงบ้างแล้ว\nฉันเองพอได้พักหายใจหายคอแล้วก็รู้สึกดีขึ้นหน่อย ๆ ด้วย แบบนี้สิค่อยสมเป็นการออกมาเที่ยวข้างนอกดี ๆ"

# "Even if she's calmer than before, though, she's still fidgeting a bit. She runs her hand down one of her bangs as I try to think of something to say."
"แต่ถึงจะสงบลงกว่าเมื่อครู่แล้วฮานาโกะก็ยังทำท่ากระมิดกระเมี้ยน เธอลูบไปตามผมหน้าม้าข้างหนึ่ง ฉันลองคิดดูว่า\nจะพูดอะไรดี"

# hi "That's right. I was going to ask…"
hi "จริงสิ ว่าจะถาม…"

show hanako emb_timid_cas_close
with charachange

# "Hanako tilts her head quizzically."
"ฮานาโกะเอียงคอด้วยความฉงน"

# hi "I didn't know you had a mobile phone. How'd you get my number?"
hi "ไม่ยักรู้ว่าเธอมีโทรศัพท์ด้วย เอาเบอร์โทร. ฉันมาจากไหนเหรอ"

show hanako emb_smile_cas_close
with charachange

# ha "L-Lilly… gave it… to me."
ha "ละ-ลิลลี่… บอก… มา"

# "I should have guessed."
"ไม่น่าถาม"

# hi "You know, you could have just asked; I'd have given it to you."
hi "เนี่ย เธอถามฉันเอาก็ได้ ยังไงก็เต็มใจให้อยู่แล้ว"

# hi "Want to exchange email addresses?"
hi "แลกที่อยู่อีเมลกันไหม"

show hanako basic_bashful_cas_close
with charachange

# "Hanako nods, setting down her drink and fishing out her phone from her pocket as I do the same."
"ฮานาโกะพยักหน้าแล้ววางเครื่องดื่มก่อนจะคุ้ยหาโทรศัพท์ในกระเป๋าออกมา ส่วนฉันก็คุ้ยของตัวเอง"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

show hanaphone:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

# "It's, surprisingly, the same model as mine. Pink, though."
"ฉันต้องประหลาดใจเมื่อโทรศัพท์ของเธอนั้นเป็นรุ่นเดียวกันกับฉัน ไม่เหมือนก็ตรงที่ของเธอเป็นสีชมพู"

# hi "Nice phone."
hi "สวยนี่"

show hanako basic_smile_cas_close
with None

$ renpy.music.set_volume(1.0, 1.0, channel="music")

show hanaphone:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide hanaphone
with None

# "She looks to me with a curious expression, before noticing my phone and giggling. It's one of the very few times I've seen Hanako let her guard down enough to do such a thing."
"ฮานาโกะมองฉันด้วยความสงสัยก่อนจะเห็นโทรศัพท์ฉันแล้วหัวเราะคิกคัก ฉันแทบไม่เคยเห็นเธอปล่อยตัวสบาย\nให้ตัวเองหัวเราะอะไรแบบนี้ได้เลย"

show hanako cover_bashful_cas_close
with charachange

# ha "I didn't pick it out myself, though."
ha "แต่ฉันไม่ได้เป็นคนเลือกเองนะ"

# hi "Oh?"
hi "หืม?"

show hanako basic_bashful_cas_close
with charachange

# ha "It was a present, from Lilly."
ha "เป็นของขวัญจากลิลลี่น่ะ"

show hanako emb_emb_cas_close
with charachange

# ha "I never really needed a phone, and I couldn't afford one. She bought me one for Christmas, though, saying that we could use it to keep in touch."
ha "ฉันไม่จำเป็นต้องใช้โทรศัพท์ขนาดนั้น แถมไม่มีเงินซื้อด้วย แต่ลิลลี่ก็ซื้อมาให้ตอนวันคริสต์มาส บอกว่า\nจะได้ติดต่อกันสะดวก"

# "They see each other basically every day anyway, both in and out of school…"
"ยังไงก็เจอหน้ากันแทบทุกวันอยู่แล้ว ไม่ว่าจะในหรือนอกโรงเรียน"

# "Then again, Lilly does have her class representative duties and other friends that she talks with. It'd probably help for situations like this, too, when she's gone away for a while."
"แต่ก็นะ ลิลลี่ก็มีภาระหน้าที่ในฐานะหัวหน้าห้องอยู่เหมือนกัน ไหนจะมีเพื่อนคนอื่นที่ต้องคุยด้วยอีก แล้วก็จะได้\nเป็นประโยชน์กับสถานการณ์แบบนี้ที่เธออยู่ด้วยไม่ได้สักพักด้วย"

# hi "Lilly's a very special person to you, isn't she?"
hi "ลิลลี่คงเป็นคนสำคัญสำหรับเธอน่าดูเลยนะ"

show hanako emb_downsmile_cas_close
with charachange

# ha "She is. I… love her… very much."
ha "อื้ม ฉัน… รักลิลลี่… มากเลยละ"

# "Hanako looks down and smiles as she thinks of her. None of my friendships were as deep as theirs, and I have to admit to myself that I'm a little jealous of their relationship."
"ฮานาโกะก้มหน้ายิ้มพลางคิดถึงลิลลี่ มิตรภาพของฉันไม่เคยมีมิตรภาพไหนที่แน่นแฟ้นเท่าพวกเธอสองคนเลย\nต้องยอมรับว่าฉันเองก็อิจฉาหน่อย ๆ กับความสัมพันธ์ของทั้งสองคนเหมือนกัน"

# "We tell each other our email addresses and thumb them into our respective phones, and I get Hanako's number from earlier and put it into my contacts list."
"พวกเราบอกที่อยู่อีเมลของตัวเองให้กันและกันและกดบันทึกใส่โทรศัพท์ของตัวเอง ฉันบันทึกเบอร์โทร.\nของฮานาโกะจากเมื่อครู่เข้ามาในสมุดรายชื่อ"

show hanako basic_smile_cas_close
with charachange

# ha "…Done. That makes three, now."
ha "…เรียบร้อย ทีนี้ก็มีสามคนแล้ว"

# hi "Three?"
hi "สามคน?"

show hanako basic_bashful_cas_close
with charachange

# ha "Lilly, Akira and you."
ha "ลิลลี่ พี่อากิระ แล้วก็นาย"

# hi "Ah, Akira. She's an interesting person, isn't she?"
hi "อ้อ อากิระ ก็เป็นคนที่น่าสนใจดีนะ ว่าไหม"

show hanako emb_smile_cas_close
with charachange

# ha "She is. She's also really nice, though. Her suit makes her… look a bit cool."
ha "อื้ม แถมเป็นคนดีมาก ๆ ด้วย ชุดสูทก็… ดูเท่"

# hi "I'm a little surprised you know each other well, what with her job taking up so much of her time."
hi "ฉันยังแปลกใจอยู่เหมือนกันนะที่เธอสองคนรู้จักกันดีขนาดนั้น แล้วไหนพี่อากิระจะติดงานบ่อย ๆ ด้วยอีก"

show hanako emb_downsmile_cas_close
with charachange

# "Hanako looks down a little and takes another sip of her drink. If I wasn't looking intently at her face, I'd miss the small smile perched on it. I guess when she knows so few people, those she knows must mean a lot to her."
"ฮานาโกะก้มหน้าเล็กน้อยแล้วจิบชาอีกรอบ ถ้าไม่ได้จดจ้องอยู่ละก็ฉันคงไม่เห็นรอยยิ้มจาง ๆ ที่อยู่บนใบหน้าเธอแน่\nพอรู้จักคนไม่มากแล้วก็คงแปลว่าทุกคนต่างสำคัญกับเธอมากสินะ"

# ha "How many… do you have?"
ha "แล้วนาย… มีกี่คนเหรอ"

# hi "Me? About nine or ten."
hi "ฉันเหรอ สักเก้าคนสิบคนนี่แหละ"

# "I hesitate to go into them for fear of rubbing in the fact that Hanako doesn't have parents, or apparently even close relatives. Two of those are Shizune and Misha, too, which is another can of worms."
"ฉันลังเลไม่อยากไล่รายชื่อแต่ละคนด้วยกลัวว่าจะเป็นการซ้ำเติมเรื่องที่ว่าฮานาโกะไม่มีพ่อแม่—หรืออาจจะไม่มี\nญาติสนิทเลยก็ได้—อีกสองคนในรายการนั้นเป็นชิซูเนะกับมิช่า ซึ่งก็เป็นเรื่องที่ต้องต่อความกันอีกยืดยาวเหมือนกัน"

# hi "I imagine that Lilly would have more than both of us put together, probably."
hi "แต่ฉันว่าลิลลี่น่าจะมีเยอะกว่าของพวกเราสองคนรวมกันเสียอีกนะ"

show hanako basic_smile_cas_close
with charachange

# "Hanako gives a childish giggle, and I can't help smiling. It's a good feeling that she's gotten this comfortable around me; at times like this, I feel like I'm getting close to talking to her true self."
"ฮานาโกะหัวเราะคิกคักเป็นเด็ก ๆ จนฉันอดยิ้มไม่ได้ พอเห็นว่าอยู่กับฉันได้แบบไม่เกร็งแล้วก็ดีใจ เป็นแบบนี้แล้วรู้สึก\nเหมือนได้คุยกับตัวตนของเธอจริง ๆ เลย"

# hi "Do you mind if I ask something that I've been wondering?"
hi "ขอถามอะไรหน่อยได้ไหม พอดีอยากรู้มานานแล้วน่ะ"

show hanako basic_normal_cas_close
with charachange

# "Hanako shakes her head as she takes a last sip of her tea, finishing it off."
"ฮานาโกะสั่นหัวพลางจิบชาไปจนหมดถ้วย"

# hi "You don't seem very jealous of Lilly having lots of friends. Don't you want to make some more friends yourself, or get to know some of hers?"
hi "เธอดูไม่อิจฉาที่ลิลลี่มีเพื่อนเยอะเท่าไหร่เลย ไม่อยากหาเพื่อนเพิ่มหรือไปรู้จักกับเพื่อนลิลลี่บ้างเหรอ"

show hanako cover_worry_cas_close
with charachange

# ha "I'm not jealous. I… don't like people, so I don't mind not having many friends."
ha "ฉันไม่อิจฉาเลย ฉัน… ไม่ชอบคนน่ะ เลยไม่อะไรกับการที่มีเพื่อนน้อย"

# "That's… really not the answer that I was expecting. She doesn't look fearful or sad as she says this, but rather, quite serious."
"เป็น… คำตอบที่ไม่ได้คาดไว้เลย ฮานาโกะพูดโดยไม่ได้มีสีหน้าที่หวาดหลัวหรือเศร้าเลย กลับดูจริงจังด้วยซ้ำ"

show hanako cover_distant_cas_close
with charachange

# ha "I…"
ha "ฉัน…"

# "Hanako rubs her arm awkwardly, having taken my quietness as a reason to continue. I'm not really sure what I should say, so I end up simply giving her my attention in silence."
"ฮานาโกะถูแขนตัวเองดูกระอักกระอ่วน เธอถือเอาว่าที่ฉันเงียบไปคือให้พูดต่อ ฉันไม่รู้ว่าจะต้องพูดอะไรดีถึงได้เพียง\nมองเงียบ ๆ ด้วยความสนใจ"

# ha "In middle school, I got bullied… a lot. I was called names, and got excluded from work groups and sports teams. There were… worse things, too."
ha "ตอนม. ต้น ฉันโดนแกล้ง… บ่อยมาก โดนล้อ โดนกันไม่ให้ทำงานกลุ่มด้วย โดนกันไม่ให้ร่วมทีมเล่นกีฬาด้วย\nแล้วยัง… มีอะไรที่แย่กว่านั้นอีก"

# hi "And that's what made you not like other people?"
hi "เพราะแบบนี้เธอถึงได้ไม่ชอบคนอื่น?"

# "She shakes her head."
"ฮานาโกะสั่นหัว"

show hanako emb_timid_cas_close
with charachange

# ha "That was… elementary school."
ha "ฉันไม่ชอบคน… มาตั้งแต่ประถมแล้ว"

# "I feel bad for bringing this up now. Adults have enough problems dealing with Hanako's scarring; children would be all the worse."
"รู้สึกผิดเลยแฮะที่ยกเรื่องนี้ขึ้นมาคุย แค่คนโตยังรับมือกับแผลเป็นฮานาโกะไม่ค่อยจะได้ ยิ่งเด็กไม่ต้องพูดถึง"

# "I had assumed that the way she tried to make her presence not felt was just to avoid people staring at her, or because she was afraid of them; certainly not because she genuinely didn't want to interact with them in the first place as well."
"ฉันเคยคิดว่าที่ฮานาโกะทำตัวลีบบ่อย ๆ นั้นเป็นแค่เพราะไม่อยากให้คนจ้องมองหรือเพราะกลัว และที่แน่ ๆ คือไม่ได้คิด\nว่าเป็นเพราะเธอไม่อยากปฏิสัมพันธ์กับผู้คนจริง ๆ"

# "I notice the condensation from my neglected smoothie forming a little puddle around the bottom of the cup, so I take the opportunity to finish it off."
"เมื่อเห็นว่าก้อนมะม่วงปั่นที่ฉันไม่ได้แตะเริ่มละลายจนเป็นของเหลวอยู่ก้นแก้วแล้วจึงถือจังหวะนี้กินจนหมด"

stop music fadeout 5.0

show hanako emb_downtimid_cas_close
with charachange

# "As I drink, she begins to fiddle with her phone. It looks like she's remembered the people around her again, and begun to tense up."
"ระหว่างที่ดื่มฮานาโกะก็เริ่มกดโทรศัพท์เล่น ดูท่าว่าจะนึกขึ้นได้ว่ารอบตัวมีคนอยู่ถึงได้เริ่มเกร็ง"

# "It isn't exactly a cheap phone - I had to save up for quite a while to afford one when I got mine. If Lilly went to a private school, she probably wouldn't have too much trouble getting one for a present, though."
"ไม่ใช่โทรศัพท์ถูก ๆ ด้วย ตอนที่จะซื้อฉันต้องเก็บเงินอยู่พักใหญ่เหมือนกัน แต่ถ้าลิลลี่เรียนโรงเรียนเอกชนได้\nก็คงไม่เดือดร้อนอะไรกับการที่ต้องซื้อโทรศัพท์เครื่องนี้ให้เป็นของขวัญ"

# "Watching her fiddle with it gives me an idea…"
"ฉันนึกอะไรได้เมื่อเห็นฮานาโกะที่เล่นโทรศัพท์อยู่…"

# hi "Hey Hanako, wait for me. I'll be right back."
hi "นี่ ฮานาโกะ รอฉันก่อนนะ เดี๋ยวมา"

$ renpy.music.set_volume(0.4, 4.0, channel="ambient")

# "I put the now empty cup down, slip my phone into my pocket, and begin to move off, carefully stepping around the bag I'd placed beside my feet. Thankfully, sitting around while talking to Hanako has helped me feel a lot better than before."
"ฉันวางแก้วที่ตอนนี้มะม่วงปั่นพร่องไปหมดแล้วลง เก็บโทรศัพท์ใส่กระเป๋า ตั้งท่าเตรียมลุกออกเดินระวังไม่ให้เหยียบ\nกระเป๋าที่วางอยู่ข้างเท้า โชคดีที่พอได้นั่งพักอยู่คุยกับฮานาโกะแล้วก็มีแรงขึ้นมากว่าเมื่อครู่มาก"

show hanako defarms_worry_cas_close
with charachange

# ha "Wait, w-what? Wh-where are you going?"
ha "เดี๋ยว อะ-อะไรนะ นะ-นายจะไปไหน"

# hi "Just stay here, I'll be back in a bit!"
hi "เธออยู่นี่แหละ แป๊บเดียวเดี๋ยวมา!"

$ renpy.music.set_volume(0.0, 1.0, channel="ambient")

show bg city_karaokeint
show hanako invis_close
with shorttimeskip

$ renpy.music.set_volume(0.2, 0.3, channel="ambient")
# "As much as I'd have liked to have jogged back, I know full well that I couldn't. I end up walking back to the café, a little blue bag in my right hand."
"แม้จะอยากวิ่งตอนขากลับมาแค่ไหนแต่ก็รู้ดีว่าวิ่งไม่ได้ สุดท้ายจึงได้แต่เดินกลับมาที่เคาเฟพร้อมถุงสีฟ้าใบเล็กในมือ"

show hanako defarms_worry_cas_close
with charachange

play music music_another fadein 3.0

# "Hanako notices me quickly, looking about as confused as she did when I left. I deposit the diminutive bag in front of her and sit back down."
"ฮานาโกะเห็นฉันทันทีที่กลับมาพร้อมสีหน้างงงวยเหมือนตอนที่ฉันเดินออกไป ฉันวางถุงขนาดย่อมนั้นไว้ตรงหน้าเธอ\nก่อนจะนั่งลง"

show hanako basic_worry_cas_close
with charachange

# ha "Is this…?"
ha "นี่คือ…?"

# hi "It's for you. You can open it."
hi "ให้ เปิดดูเลย"

show hanako cover_worry_cas_close
with charachange

# ha "B-but…"
ha "ตะ-แต่"

# hi "Go on."
hi "เปิดเลย"

# "She looks very unsure about it, but eventually gives in, slowly opens the bag and picks its contents out."
"ฮานาโกะทำหน้าไม่แน่ใจมาก ๆ แต่สุดท้ายก็ยอมทำตามที่บอก เธอค่อย ๆ เปิดถุงแล้วหยิบของข้างในออกมา"

show phonestrap:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

$ renpy.music.set_volume(0.5, 1.0, channel="music")

# "A silver chain phone strap dangles from her fingers, ending in a delicate flower. It isn't exactly a masterwork of jewelry, but it's about as much as I could afford."
"สายประดับโทรศัพท์ที่เป็นโซ่สีเงินห้อยออกมาจากมือฮานาโกะ ตรงส่วนปลายมีดอกไม้สวย ๆ ประดับอยู่ ถึงไม่ใช่\nเพชรน้ำหนึ่งหรืออะไร แต่ฉันก็เลือกของเท่าที่พอจะมีกำลังซื้อให้ได้"

show hanako cover_bashful_cas_close
with None

# "Hanako's eyes light up when she looks at it. It's the kind of reaction I was hoping for."
"ฮานาโกะทำตาลุกวาวทันทีที่เห็น เป็นท่าทีที่ฉันคาดหวังไว้เลยละ"

# "The summer sun's light glints off the silver as it twists to and fro a little. It's not too ostentatious, but still looks a little charming. I think it suits her well."
"แสงแดดสะท้อนวิบวับตอนที่สายโซ่เงินนั้นเคลื่อนไปมา ดูสวยโดยที่ไม่ได้อลังการจนเกินไป เหมาะกับฮานาโกะดีทีเดียว"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

show phonestrap:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide phonestrap
with None

# "Hanako lowers the phone strap to the table and looks to me once more."
"ฮานาโกะวางสายประดับโทรศัพท์ลงกับโต๊ะแล้วมองฉันอีกรอบ"

show hanako cover_worry_cas_close
with charachange

# ha "But… it's not… Christmas, or my birthday…"
ha "แต่… วันนี้ไม่ใช่… วันคริสต์มาสหรือวันเกิดฉัน…"

# hi "It's fine, don't worry about it. I just thought it might be nice to have something to decorate your phone with."
hi "ไม่เป็นไรน่า เรื่องแค่นี้เอง แค่เห็นว่าถ้ามีอะไรประดับโทรศัพท์เธอบ้างคงดี"

show hanako basic_worry_cas_close
with charachange

# ha "I-I don't have anything to give to you…"
ha "ฉะ-ฉันไม่มีอะไรจะให้…"

# hi "I told you, it's fine. Friends can give things to each other like this sometimes, right?"
hi "บอกแล้วไงว่าไม่เป็นไร เพื่อนกันให้ของแบบนี้กันบ้างก็ไม่แปลก เนอะ"

show hanako emb_downsmile_cas_close
with charachange

# ha "Friends…"
ha "เพื่อน…"

# "Hanako lowers her face so much that I can't see her expression. She eventually nods, before taking her phone and fiddling with the strap to attach it properly."
"ฮานาโกะก้มหน้างุดจนฉันไม่เห็นสีหน้าเธอ สุดท้ายเธอก็พยักหน้าแล้วหยิบโทรศัพท์กับจับสายประดับไปมาหาวิธีติด"

show hanako emb_smile_cas_close
with charachange

$ renpy.music.set_volume(0.5, 1.0, channel="music")

show hanaphonestrap:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

# "She looks to me and smiles as she holds up her phone, now adorned with a little flower."
"ฮานาโกะมองฉันแล้วยิ้มพลางชูโทรศัพท์ที่ตอนนี้มีดอกไม้ดอกเล็ก ๆ ประดับอยู่แล้ว"

# ha "Thank you… Hisao."
ha "ขอบคุณนะ… ฮิซาโอะ"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

show hanaphonestrap:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide hanaphonestrap
with None

# "Her smile proves infectious."
"รอยยิ้มของเธอพาให้ฉันยิ้มตาม"

# "Out of the corner of my eye, I notice a couple getting up and leaving. That reminds me that the bus back to the town below Yamaku will be coming soon."
"ฉันเห็นคู่รักคู่หนึ่งที่ลุกจากโต๊ะเดินออกไปอยู่ตรงหางตาจนนึกได้ว่าใกล้ถึงเวลาที่รถบัสเที่ยวกลับไปเมืองที่อยู่\nล่างยามากุจะมาแล้ว"

# hi "I guess I'd better be going if I want to catch the next bus back to town. You coming as well?"
hi "ต้องไปแล้วละ พอดีจะขึ้นรถเที่ยวกลับเมือง จะไปด้วยไหม"

show hanako def_worry_cas_close
with charachange

# ha "Ah, y-yes."
ha "อ๊ะ อะ-อื้ม"

show hanako invis_close at center
with dissolvecharamove

# "She hastily nods before carefully putting her phone back into her pocket and getting out of her chair. I do the same and pick up the bag I'd left beside me on the way out."
"ฮานาโกะรีบพยักหน้าแล้วเก็บโทรศัพท์ใส่กระเป๋าอย่างเบามือแล้วลุกจากเก้าอี้ ฉันลุกตามแล้วหยิบกระเป๋าที่วางไว้ข้าง ๆ\nตอนที่เดินออกมา"

stop ambient fadeout 1.0
stop music fadeout 3.0

scene bg city_street2
show hanako emb_downsmile_cas_close at center
with locationskip

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_traffic fadein 1.0

# "We walk side by side as we make our way to the bus station, exchanging no words between us. Hanako's gaze is firmly locked ahead of her, though she looks very happy with herself."
"เราเดินเคียงกันไปจนถึงสถานีรถบัสโดยไม่คุยอะไรกัน ฮานาโกะมองทางข้างหน้าเขม็ง ดูจะมีความสุขมาก ๆ"

# "I'm not sure what I should say to her, but I'm also not sure that I need to say anything. The fact that Hanako is happy, and happy because of me, is enough to make the load on my arm feel light as a feather."
"ฉันไม่แน่ใจว่าจะต้องพูดอะไรกับเธอดี ไม่แน่ใจด้วยว่าจำเป็นต้องพูดหรือเปล่า แค่ฮานาโกะมีความสุขได้เพราะฉัน\nก็ทำให้แขนฉันที่แบกของอยู่นั้นเบาหวิวดุจขนนกขึ้นมาแล้ว"

stop ambient fadeout 2.0

scene black
with dissolve


#*********************

label th_H29:

scene bg school_scienceroom
with locationchange

play music music_normal fadein 2.0

# "Finally reaching the classroom after the usual walk from the dormitories, I step inside. My eyes immediately turn to the third seat from the left in the back row; Hanako's seat."
"ฉันเดินจากหอมาจนถึงห้องเรียนอย่างทุกทีแล้วเดินเข้าไป สายตาฉันหันไปมองที่โต๊ะที่สามนับจากทางซ้าย\nของแถวหลังสุดซึ่งเป็นโต๊ะฮานาโกะทันที"

# "It's empty, and after glancing around the classroom, it looks like she isn't here yet. The two girls from the newspaper club are here in the two seats to the left of Hanako's, as are Shizune and Misha, but that's about it."
"ว่างเปล่า และเมื่อมองไปรอบ ๆ ห้องก็เห็นว่าคงจะยังไม่มา สองสาวจากชมรมหนังสือพิมพ์นั่งอยู่ที่โต๊ะถัดจากฮานาโกะ\nไปทางซ้าย ชิซูเนะกับมิช่าก็อยู่ แต่ก็เท่านั้น"

# "We exchange morning greetings before I take my seat. I have to admit that this is a bit of a relief. This gives me at least a few more minutes to think."
"เราทักทายยามเช้ากันก่อนฉันเดินมานั่งที่ ค่อยโล่งใจขึ้นมาหน่อยเพราะจะได้มีเวลาคิดอีกสักพัก"

# "Not that I haven't been doing so previously; ever since our trip to town, Hanako's been on my mind."
"ตั้งแต่ที่นัดเจอกันในตัวเมืองครั้งนั้นฉันก็เอาแต่คิดถึงฮานาโกะ ถึงก่อนหน้านี้จะคิดอยู่แล้วก็เถอะ"

# "I still don't know what to make of my relationship to Hanako. I like her, I can admit that much to myself. I want to protect and shield her from the pain she feels. I really don't think my feelings are just those of friendship any more."
"ฉันยังไม่รู้ว่าจะต้องมองความสัมพันธ์ของตัวเองกับฮานาโกะเป็นอะไร ฉันชอบฮานาโกะ ส่วนนี้ฉันยอมรับ ฉันอยาก\nปกป้องและคุ้มกันเธอให้พ้นจากความเจ็บปวด ความรู้สึกของฉันคงไม่ใช่แค่คำว่าเพื่อนแล้ว"

# "But that said… I feel like I don't even know her."
"แต่ถึงอย่างนั้น… ฉันก็รู้สึกเหมือนตัวเองไม่ได้รู้จักฮานาโกะด้วยซ้ำ"

# "If I made a move on her, how would she take it? Is she in an emotional state that allows her to make a reasonable decision about a relationship? How would she cope with anything that might happen afterwards?"
"ถ้าฉันเดินหน้าต่อแล้วฮานาโกะจะคิดอย่างไร สภาพจิตใจเธอคงที่พอจะตัดสินใจเรื่องความสัมพันธ์ของเราได้\nอย่างสมเหตุสมผลหรือเปล่า ถ้าหลังจากนั้นเกิดอะไรขึ้นอีกแล้วเธอจะรับได้ไหม"

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_footsteps_hard fadein 4.0

# "There's also the possibility that I'm just completely misinterpreting Hanako; not a difficult thing to do with someone whose social skills seem to be so underdeveloped."
"หรือฉันอาจจะตีความฮานาโกะไปผิดก็ได้อีกต่างหาก ซึ่งก็เป็นแบบนั้นได้ไม่ยากเลยเมื่ออีกฝ่ายเป็นคนที่ไม่มีทักษะ\nทางสังคมขนาดนั้น"

# "The sound of footsteps comes up to the door, making me perk up."
"เสียงฝีเท้าที่เดินมาทางประตูทำให้ฉันต้องหันไปมอง"

stop ambient fadeout 0.3

show miki invis:
    right
    xpos 1.1
with None

show miki whistle at right
with dissolvecharamove

# "It ends up just being Miki."
"ปรากฏว่าเป็นมิกิ"

show miki smile
with charachange

show miki invis at Position (xpos=0.9)
with dissolvecharamove

# "She barely acknowledges my existence when I accidentally make eye contact with her. I'm about to look away, but another person comes in not long after she takes her seat."
"มิกิแทบไม่ได้รับรู้ถึงตัวตนฉันตอนที่เผลอไปสบตาเข้า ฉันจะเบือนหน้าหนีแล้วแต่ก็มีเสียงอีกคนเดินตามมาไม่นาน\nหลังจากที่เธอนั่งที่"

show hanako invis:
    right
    xpos 1.1
with None

show hanako emb_downtimid at right
with dissolvecharamove

stop music fadeout 2.0

# "I feel myself freeze as I see Hanako enter. This isn't a rational reaction, but I have no idea about how I should act or what I should say to her."
"ฉันชะงักไปเมื่อเห็นว่าฮานาโกะเข้ามา ไม่แปลกที่ฉันจะชะงัก แต่ฉันไม่รู้ว่าจะต้องทำตัวยังไงหรือพูดอะไรกับฮานาโกะ"

show hanako emb_timid
with charachange

# "For a moment, our eyes meet."
"เราสบตากันแวบหนึ่ง"

show hanako emb_downtimid
with charachange

show hanako invis at Position (xpos=0.9)
with dissolvecharamove

# "And then, just as quickly, she looks away and moves to her seat without saying a single word."
"แล้วเธอก็มองไปทางอื่นด้วยความรวดเร็วก่อนจะนั่งที่ไม่พูดอะไร"

scene bg school_library_ss
with shorttimeskip

play music music_tranquil fadein 3.0

# "As is now usual for the period following classes, my face is buried deep in a book that I find thoroughly uninteresting."
"ตอนนี้หน้าฉันจมอยู่กับหนังสือที่ฉันรู้สึกว่าไม่น่าสนใจเอาเสียเลย ซึ่งกลายเป็นเรื่องปกติไปแล้วกับช่วงเวลา\nหลังเลิกแต่ละคาบ"

# "Studying is not something that comes naturally to me. I didn't study a lot before coming to Yamaku, and until now I've largely managed to coast through on talent alone. It's frustrating that I can't do that any more."
"การเรียนไม่ใช่ทางของฉันแต่แรก ก่อนมายามากุฉันก็ไม่ได้ตั้งใจเรียนขนาดนั้น และที่ผ่านมาได้จนตอนนี้ส่วนใหญ่\nก็พึ่งพรสวรรค์ที่ติดตัวมาทั้งนั้น พอทำได้แค่นี้แล้วก็รู้สึกหงุดหงิด"

# "Judging by the faces of the other few students in the library, I don't think I'm alone in my distaste for this. Misery loves company, I suppose."
"ดูจากสีหน้านักเรียนคนอื่นสองสามคนที่อยู่ในห้องสมุดแล้ว คงไม่ได้มีแค่ฉันสินะที่หน่ายใจกับเรื่องนี้ นี่ละมั้งที่เขาว่า\nคนเราชอบหาผู้ร่วมโชคชะตาเดียวกัน"

# "I decided to spend lunchtime with Hanako, since we haven't had lunch together for a while now. I may as well have spent the time studying, though; aside from pathetically small snippets of smalltalk, there was barely a word said between us."
"ฉันคิดจะไปกินข้าวเที่ยงกับฮานาโกะเพราะไม่ได้กินด้วยกันมาสักพักแล้ว แต่ก็อาจเจียดเวลานั้นมาอ่านหนังสือได้\nเหมือนกัน เพราะเราก็แทบไม่ได้คุยอะไรกันเลยนอกเสียจากการคุยเรื่อยเปื่อย ๆ เล็กน้อย ๆ"

# "Why does she keep doing this to me? I just want to protect her, to be there for her, but every time I feel like we're coming closer, we end up further away."
"ทำไมถึงทำแบบนี้กับฉันกัน ฉันแค่อยากปกป้องฮานาโกะ อยากอยู่เคียงข้างฮานาโกะ แต่ทุกครั้งที่เหมือนจะได้\nเข้าใกล้ชิดแล้วเราก็กลับห่างออกจากกันไปอีก"

# ha "A-are you busy…?"
ha "ยะ-ยุ่งอยู่หรือเปล่า…"

$ renpy.music.set_volume(0.0, 0.3, channel="music")

show hanako defarms_shock_ss at center
with vpunch

# hi "Hanako!?"
hi "ฮานาโกะ!?"

# "My head whips around in surprise, causing her to retreat in fright."
"ฉันหันหัวเหลียวซ้ายแลขวาด้วยความตกใจจนฮานาโกะสะดุ้งถอยกรูด"

show hanako emb_downsad_ss
with charachange

# "That was bad timing. If I hadn't been thinking about her at that very moment, I probably wouldn't have been nearly so startled."
"จังหวะบัดซบสิ้นดี ถ้าไม่ได้คิดถึงฮานาโกะอยู่ฉันก็คงไม่ตกใจขนาดนี้หรอก"

$ renpy.music.set_volume(1.0, 5.0, channel="music")

# hi "Sorry, you just startled me."
hi "ขอโทษที พอดีตกใจเธอนิดหน่อย"

# "I find myself staring at her longer than I should, so I go back to the text lying on the table in front of me. I feel more like I'm just staring at the words rather than actually reading."
"ฉันจ้องฮานาโกะนานเกินความจำเป็น จึงหันกลับไปมองหนังสือที่อยู่บนโต๊ะตรงหน้า รู้สึกเหมือนไม่ได้อ่านแต่จ้องคำ\nไปเป็นคำ ๆ มากกว่า"

# "I get the feeling Hanako can notice this as well, so I sigh and close the book."
"ฮานาโกะก็น่าจะดูออกด้วย ฉันถอนหายใจแล้วปิดหนังสือ"

# hi "What's up?"
hi "มีอะไร"

show hanako emb_sad_ss
with charachange

# ha "I was just… w-wondering what you were r-reading…"
ha "แค่… ยะ-อยากรู้ว่านายอะ-อ่านอะไรอยู่…"

# "She looks a little downcast after my reaction to seeing her. Giving up on the prospect of getting any more work done, I get up and return the book to its place on a nearby shelf."
"ฮานาโกะดูหมองไปเล็กน้อยเมื่อเห็นปฏิกิริยาของฉันหลังจากเห็นเธอ ฉันล้มเลิกความคิดที่จะอ่านต่อแล้วลุกขึ้น\nนำหนังสือไปเก็บที่ชั้นใกล้ ๆ"

# hi "Just an English textbook."
hi "หนังสือภาษาอังกฤษน่ะ"

show hanako basic_normal_ss
with charachange

# ha "H-has it helped?"
ha "พะ-พอรู้เรื่องขึ้นมาไหม"

# hi "It helped me realize that I don't like English, yeah."
hi "อืม รู้เรื่องว่าฉันไม่เก่งภาษาอังกฤษอะนะ"

show hanako basic_smile_ss
with charachange

# "Hanako gives a small giggle. I may muse on the strange state of our friendship, but I do know that such little gestures are things that I wouldn't see were I not at least some distance closer to her than when we first met."
"ฮานาโกะหัวเราะคิกคัก ฉันคิดมากเรื่องสถานะสุดพิลึกของความสัมพันธ์เราก็จริง แต่ฉันก็รู้ดีว่าถ้าฉันไม่สนิทกับเธอ\nเข้ามาสักหน่อยนับตั้งแต่ที่ได้เจอกันครั้งแรกแล้วคงไม่ได้เห็นท่าทีเล็ก ๆ น้อย ๆ แบบนี้"

# "I look at her for a moment, thinking about what I do and don't know about her. It's a slightly depressing topic."
"ฉันมองฮานาโกะอยู่ขณะหนึ่งพลางคิดว่าฉันรู้และไม่รู้อะไรเรื่องเธอบ้าง ซึ่งเป็นหัวข้อที่ชวนหดหู่หน่อย ๆ"

show hanako basic_worry_ss
with charachange

# ha "I-is something… wrong?"
ha "มะ-มีอะไร… เหรอ"

stop music fadeout 5.0

# "If I want to know more about her, maybe I should stop being so evasive about it."
"ถ้าอยากรู้จักฮานาโกะให้มากกว่านี้ฉันก็คงต้องเลิกอ้อมไปอ้อมมาสักที"

# "Talking with Lilly as an equal rather than being constantly in fear of causing her to become upset worked fine, so I should just try a straightforward approach with Hanako as well."
"การคุยกับลิลลี่ในฐานะเพื่อน ๆ กันแทนที่จะมามัวกลัวว่าจะทำให้อีกฝ่ายต้องเศร้าขึ้นมาก็ดูจะใช้ได้ เพราะงั้น\nก็ใช้วิธีคุยตรง ๆ แบบนี้นี่แหละกับฮานาโกะด้วย"

# hi "Hey Hanako, do you mind if I ask you a question?"
hi "นี่ ฮานาโกะ จะว่าอะไรไหมถ้าขอถามเธออย่าง"

show hanako cover_worry_ss
with charachange

# ha "I-I don't mind."
ha "มะ-ไม่ว่า"

# hi "I… want to know what your life was like. Your life before coming to Yamaku."
hi "ฉัน… อยากรู้ว่าชีวิตเธอเป็นยังไงน่ะ ชีวิตก่อนจะมายามากุ"

show hanako emb_blushing_ss
with charachange

# "She hesitates. I briefly consider backing off, but she seems to be taking the question quite seriously."
"ฮานาโกะลังเล ฉันนึกจะถอยไม่ถามต่อแล้ว แต่เธอดูจะชั่งใจกับคำถามนั้นอย่างจริงจัง"

# "I sit and watch her, silently letting her take her time. She's not making eye contact with me, and looks almost as if she's arguing with herself into letting herself open up to me more."
"ฉันนั่งมองฮานาโกะเงียบ ๆ ปล่อยให้เธอใช้เวลาคิด เธอไม่สบตากับฉันเลย ทั้งทำสีหน้าเหมือนกำลังเถียงกับตัวเอง\nว่าจะเปิดใจกับฉันให้มากกว่านี้ดีไหม"

# "Her answer finally comes in a stiff, almost reluctant nod. She looks far more tense than she did before I'd asked."
"สุดท้ายฮานาโกะก็ตอบรับด้วยการพยักหน้าหงึกคล้ายไม่แน่ใจ ดูเกร็งกว่าตอนก่อนที่ฉันถามอีก"

show hanako basic_worry_ss
with charachange

# ha "Okay. B-but in return… you have to t-tell me about your life as well…"
ha "โอเค ตะ-แต่… นายจะต้องละ-เล่าเรื่องชีวิตนายให้ฟังก่อนนะ…"

hide hanako
with charaexit

# "I nod, and follow her as she begins to walk out the library so we can talk."
"ฉันพยักหน้าแล้วเดินตามเธอที่ออกจากห้องสมุดไปเพื่อจะได้คุยกัน"

scene bg school_hallway3
show hanako basic_normal at center
with locationchange

play music music_serene fadein 0.5

# "By now most of the students have already left the main building, so apart from a few people hovering around club rooms, the hallways are largely empty."
"ตอนนี้นักเรียนหลายคนออกจากอาคารหลักไปกันแล้ว โถงทางเดินจึงแทบไม่มีใคร ยกเว้นคนบางคนที่ยังวนเวียน\nอยู่ตามห้องชมรม"

# hi "I guess… we'll start with coming to Yamaku."
hi "งั้น… เริ่มที่ตอนได้มายามากุแล้วกัน"

# hi "Let's see… I was in the hospital when my parents first told me about Yamaku Academy."
hi "นึกก่อนนะ… ตอนที่พ่อแม่บอกว่าจะได้มาเรียนยามากุเป็นตอนที่ฉันอยู่ที่โรงพยาบาล"

# hi "The doctors told me I shouldn't go to my old school any more. My parents agreed and persuaded me to apply for Yamaku, even though it would mean living away from them for the first time."
hi "หมอบอกว่าฉันไม่ควรกลับไปเรียนที่เดิมแล้ว พ่อแม่ฉันก็ตกลงแล้วหว่านล้อมให้ฉันเข้าเรียนที่ยามากุ ซึ่งก็แปลว่า\nฉันจะต้องใช้ชีวิตอยู่ห่างจากพ่อแม่เป็นครั้งแรกเลย"

show hanako cover_worry
with charachange

# ha "It must have… been hard for you."
ha "คง… ลำบากมากเลยสินะ"

# hi "Well… yeah, I have to admit that it was. My parents both work long hours and full-time, so having to live reasonably independently wasn't anything new to me. It was the fact that I was going to a school for disabled students that hit hardest, I think."
hi "อืม… ก็ใช่ ยอมรับเลยว่าลำบาก แต่พ่อแม่ฉันก็ทำงานหนักแบบเต็มเวลา เพราะงั้นฉันก็พอจะชินแล้วกับการใช้ชีวิต\nอยู่ตัวคนเดียว ที่คิดหนักที่สุดน่าจะเป็นเรื่องที่ว่าฉันต้องไปเรียนที่โรงเรียนสำหรับคนพิการนี่แหละ"

# hi "And you?"
hi "แล้วเธอล่ะ"

scene bg school_staircase2
show hanako emb_downtimid_close at right
with locationchange

# "A small group of chatting girls passes us as we near the stairs, with Hanako pressing herself tightly to my side until we reach the ground floor. She doesn't usually come this close while just walking in the school, so I'm left a little put off."
"กลุ่มเด็กสาวสองสามคนเดินผ่านเราไปตอนที่เราเดินใกล้ถึงบันได ฮานาโกะแนบตัวชิดกับฉันไปจนถึงชั้นล่าง\nฉันรู้สึกแปลก ๆ ขึ้นมาหน่อยเพราะปกติแค่เดินในโรงเรียนเธอจะไม่อยู่ใกล้ขนาดนี้"

show hanako emb_downsad_close
with charachange

# ha "The staff at the o-orphanage offered me some options on what I could do. Middle school… hadn't been good, so I thought that Yamaku might be better."
ha "พี่ ๆ ที่บะ-บ้านก็เสนอตัวเลือกว่าให้เลือกอะไรได้บ้าง ที่เรียนตอนมัธยมต้น… ก็ไม่ค่อยดีเท่าไหร่ เลยคิดว่ามาเรียน\nที่ยามากุน่าจะดีกว่า"

# ha "It was isolated, and I thought it might be easier to get by here with most of the others being disabled."
ha "โรงเรียนนี้อยู่ไกลจากบ้านคน แล้วก็คิดว่าน่าจะใช้ชีวิตที่นี่ได้ง่ายกว่าเพราะคนอื่นหลายคนที่มาเรียนก็พิการ"

scene bg school_lobby_ss
with locationchange

# "It's pretty ironic that the reasons Hanako looked forward to Yamaku are the exact reasons I hated the idea. To me, it felt like I was being shunted somewhere away from society, and everyone I knew. To Hanako, that was probably an inviting prospect."
"ย้อนแย้งดีที่สาเหตุที่ฮานาโกะอยากมาที่ยามากุนั้นคือสาเหตุที่ฉันไม่อยากมายามากุ ฉันมองว่าโรงเรียนนี้ทำให้รู้สึก\nเหมือนตัวเองปลีกแยกออกจากสังคม ออกจากทุกคนที่ฉันรู้จัก ซึ่งฮานาโกะอาจมองว่าสิ่งนี้คือเรื่องที่ดีก็ได้"

# hi "What was life like at the orphanage?"
hi "ชีวิตที่สถานรับเลี้ยงเด็กกำพร้ามันเป็นยังไงเหรอ"

show hanako emb_timid_ss at center
with charaenter

# ha "It was… okay. The staff there were nice, and they took care of us. The children there didn't talk to me much, but I didn't really want to talk with them either, so I didn't mind."
ha "ก็… โอเคนะ พี่ ๆ เขาก็ดี คอยดูแลพวกเรา เด็กคนอื่นในบ้านไม่ค่อยคุยกับฉันเท่าไหร่ แต่ฉันก็ไม่อะไรเพราะไม่ได้\nอยากคุยกับคนอื่นอยู่แล้ว"

show hanako emb_downsmile_ss
with charachange

# ha "The orphanage had a little library, so I started to read to pass the time. The staff didn't mind it, because it made me easier to handle than many of the other children."
ha "ที่บ้านนั้นมีห้องสมุดย่อม ๆ ด้วย ฉันเลยเริ่มหันมาอ่านหนังสือฆ่าเวลา พี่ ๆ ก็ไม่ว่าอะไรเพราะแบบนี้จะได้รับมือ\nกับฉันง่ายกว่าเด็กคนอื่น"

# hi "You didn't make any friends there?"
hi "เธอไม่มีเพื่อนอยู่ที่บ้านนั้นเลยเหรอ"

show hanako basic_worry_ss
with charachange

# ha "No. I think… my life was on hold… during that time. I knew that, but I didn't mind."
ha "ไม่เลย ฉันว่า… ตอนนั้น… ชีวิตฉันชะงักไป ฉันรู้แหละ แต่ก็ไม่ได้อะไร"

# "To think her life was on hold for all that time, though… depending on when the fire happened, that was a huge chunk of her life. No parents, no friends, apparently no relatives…"
"แต่ชีวิตชะงักไปตลอดช่วงนั้นเลยเหรอเนี่ย… แล้วก็เป็นช่วงที่กินเวลาในชีวิตไปหลายปีด้วย แล้วแต่ว่าเหตุการณ์\nไฟไหม้ครั้งนั้นเกิดขึ้นเมื่อไหร่ ไม่มีพ่อแม่ ไม่มีเพื่อน และเหมือนจะไม่มีญาติด้วย…"

scene bg school_courtyard_ss
with locationchange

# "We walk through the door into the courtyard. I expect to need to avert my eyes from the sun, but by now it's well into sunset."
"เราเดินออกจากประตูมายังลาน ฉันนึกว่าจะต้องหรี่ตารับแสงแดด แต่ตอนนี้ก็เย็นย่ำมากแล้ว"

show hanako emb_timid_ss at center
with charaenter

# "Hanako's eyes keep flicking to me, so I look away from her for a bit."
"ฮานาโกะเหลือบมองฉันไม่หยุด ฉันจึงเบือนหน้าหนีบ้าง"

# ha "What was it like in the hospital?"
ha "ที่โรงพยาบาลเป็นไงบ้างเหรอ"

# "I quickly clear my thoughts and try to refocus them."
"ฉันจัดสมองให้โล่งด้วยความรวดเร็วแล้วตั้งสมาธิอีกรอบ"

# "I hesitate for a bit, but I know that I have to tell her. We're close enough for her to feel comfortable telling me this, so it's only fair that I reciprocate."
"ฉันลังเลเล็กน้อย แต่อย่างไรก็ต้องบอกละนะ เราสนิทกันพอที่ฮานาโกะจะเล่าเรื่องนี้ให้ฟังได้แล้ว เพราะงั้นฉันก็ต้อง\nตอบรับด้วยการเล่าให้ฟังบ้าง"

# hi "It was okay at times, but at others, it was pretty bad. At the beginning, everyone sent their sympathies, and came to visit often. It was just like breaking an arm or something."
hi "บางครั้งก็พอได้ บางครั้งก็ไม่ไหวเหมือนกัน แรก ๆ ทุกคนก็เห็นอกเห็นใจฉันมาเยี่ยมฉันบ่อย ๆ เหมือนว่าฉัน\nแขนหักหรืออะไรงั้นแหละ"

# hi "Meeting all my friends was one of the good times. Iwanako came in often as well; more often than anyone else."
hi "ตอนที่ได้เจอเพื่อนทุกคนก็เป็นช่วงเวลาที่ดีนะ อิวานาโกะก็มาเยี่ยมบ่อยเหมือนกัน บ่อยกว่าใครเลยแหละ"

# hi "But there were bad times, too. When my friends slowly stopped visiting, I began to realize how grave my situation was. It reminded me that this wasn't just a broken limb, but that I was now a different person than before."
hi "แต่ช่วงเวลาที่ไม่ดีก็มีเหมือนกัน ตอนที่เพื่อนเริ่มไม่มาเยี่ยมแล้วฉันก็ค่อย ๆ ระลึกได้ว่าสถานการณ์ของฉัน\nมันร้ายแรงขนาดไหน เตือนให้ฉันคิดได้ว่าฉันไม่ได้แค่แขนขาหัก แต่กลายเป็นคนละคนกับเมื่อก่อนไปแล้ว"

# hi "Even the times Iwanako would spend with me became torturous. By the end, we were reduced to silence, whereas before, she'd be talking constantly."
hi "แม้แต่ตอนที่อิวานาโกะมาอยู่ด้วยฉันก็เริ่มอึดอัด สุดท้ายก็เงียบกันไป ทั้งที่ก่อนหน้านี้อิวานาโกะจะพูดจ้อ\nตลอดเลย"

# "But that's how Iwanako always was. She may have been a fragile person, but she would talk constantly to try and hide that fact. Not about anything in particular, just… talk."
"แต่อิวานาโกะเป็นแบบนั้นอยู่แล้ว ถึงจะเป็นคนเปราะบาง แต่เธอก็แค่พูดไม่หยุดเพื่อจะปกปิดว่าตัวเองเป็นคนแบบนั้น\nไม่ได้พูดเรื่องอะไรเป็นพิเศษ แค่… พูดเฉย ๆ"

# hi "I think the three lowest points would have been when my parents told me I wouldn't be going to my old school any more, my birthday passing while in the hospital, and… when Iwanako left for the last time."
hi "ฉันว่าจุดต่ำสุดในชีวิตฉันมีอยู่สามที่ หนึ่งคือตอนที่พ่อแม่บอกฉันว่าฉันจะไม่ได้กลับไปเรียนที่เดิมแล้ว สองคือ\nเวลาถึงวันเกิดตอนที่ฉันอยู่ในโรงพยาบาล และสาม… ตอนที่อิวานาโกะจากฉันไปไม่กลับมาเลย"

scene bg school_gardens_ss
with locationchange

# "We leave the school buildings behind us as we begin to follow the main path through the gardens. There may have been the odd bystander in the school buildings, but outside, we're practically alone."
"เราเดินมาตามทางหลักที่ผ่านสวนโดยทิ้งอาคารเรียนไว้เบื้องหลัง ตามอาคารเรียนอาจมีคนอยู่บ้าง แต่ข้างนอกนั้น\nนับได้ว่ามีเพียงเราสองคนเท่านั้น"

show hanako basic_worry_ss at center
with charaenter

# ha "What was your middle school like?"
ha "โรงเรียนม. ต้นนายเป็นยังไงเหรอ"

# hi "I liked it. I grew up in a really metropolitan area, and the middle school was nearby, so it was pretty crowded. I didn't mind it, probably because I'm used to being in crowds and around lots of other people."
hi "ก็ชอบนะ ฉันโตมากับเมืองกรุง แล้วโรงเรียนม. ต้นนั้นก็อยู่ใกล้บ้านด้วย คนเยอะทีเดียวละ ฉันก็ไม่ได้อะไร คงเพราะ\nฉันชินกับการอยู่กับฝูงชนผู้คนมากมายแล้ว"

# hi "I got good grades, and I played soccer with my friends. I spent a fair bit of time hanging out with them after school as well.
# Did get teased a bit over my hair, though."
hi "ผลการเรียนฉันก็ดี ฉันเล่นฟุตบอลกับเพื่อนด้วย แล้วพอเลิกเรียนก็ไปสังสรรค์ด้วยกันบ่อยเหมือนกัน แต่พวกนั้น\nชอบล้อเรื่องผมฉัน"

show hanako def_worry_ss
with charachange

# ha "Your hair?"
ha "ผมนาย?"

# "I grimace a little as I put a hand over my hair to cover it."
"ฉันทำหน้าเบ้พลางยกมือมาปิดผมไว้"

# hi "I'd keep getting tufts and strands that refused to flatten or stay where I wanted them, and my mother wouldn't let me just get my hair shaved. It had a habit of popping out, no matter how much I tried to brush it down."
hi "มันจะมีผมที่ชอบชี้ตลอดไม่ยอมลู่ไปกับผมเส้นอื่นทั้งที่ไม่อยากให้ชี้ แม่ก็ไม่ยอมให้ฉันตัดผมเกรียนด้วย\nหวีให้มันเรียบเท่าไหร่ ๆ มันก็จะเด้งขึ้นมาตลอดอยู่ดี"

show hanako basic_smile_ss
with charachange

# ha "It still does, a little."
ha "ตอนนี้มันก็ชี้อยู่หน่อย ๆ นะ"

# hi "I was worried I'd get that reply."
hi "กลัวอยู่พอดีว่าเธอจะทักงั้น"

show hanako cover_worry_ss
with charachange

# ha "S-sorry, I didn't mean to…!"
ha "ขะ-ขอโทษ ฉันไม่ได้ตั้งใจ…!"

# "I give a mild laugh and wave it off."
"ฉันหัวเราะเบา ๆ แล้วบอกปัดไป"

# hi "It's fine, I know it still does."
hi "ไม่เป็นไรน่า รู้แหละว่ายังชี้อยู่"

# "It feels strange to have someone act so interested in my past. If it were anyone else I'd think they were just acting polite, but that's something I really don't think Hanako would do. Or if she did, she'd do it so badly that it would be obvious."
"รู้สึกแปลกดีพอมีคนมาสนใจเรื่องอดีตของฉันขนาดนี้ ถ้าเป็นคนอื่นฉันคงคิดว่าแค่ถามไปตามมารยาท แต่ฮานาโกะ\nไม่ทำอย่างนั้นหรอก หรือถ้าจะทำแบบนั้นจริงก็คงไม่เนียนจนดูออกชัดว่าแค่ถามตามมารยาท"

scene bg school_dormhallground
show hanako emb_downtimid_close at right
with locationskip

# "There are a number of girls in the common room on the ground floor, and Hanako presses herself to my side once more as we pass them. I expect her to break off, but instead she continues to cling onto me as we walk towards the stairway."
"ในห้องส่วนกลางที่ชั้นล่างของหอนั้นมีเด็กสาวอยู่จำนวนหนึ่ง ฮานาโกะแนบตัวเข้ามาชิดกับฉันตอนที่พวกเรา\nเดินผ่าน ฉันคิดว่าเดี๋ยวก็คงปล่อย แต่เธอก็แนบอยู่อย่างนั้นไปตลอดทางที่ขึ้นบันได"

stop music fadeout 5.0

# "Something about the way she's holding onto me feels… different from the usual."
"รู้สึกว่าการที่ฮานาโกะจับแขนครั้งนี้… ต่างไปจากทุกทียังไงไม่รู้"

scene bg school_girlsdormhall
with locationchange

# "I'm left deep in thought as we walk up the stairs and down the hallway. It's only when we stop that I look up and realize that I've been following her without question."
"ฉันจมอยู่กับความคิดตัวเองไประหว่างที่เราเดินขึ้นบันไดมายังโถงทางเดิน พอเราหยุดเดินแล้วฉันเงยหน้าขึ้นมอง\nถึงนึกได้ว่าฉันตามฮานาโกะมาโดยไร้ซึ่งข้อกังขาใด ๆ เลย"

# hi "Why did we come to your dormitory room?"
hi "ทำไมเราถึงมาที่ห้องเธอกันนะ"

show hanako basic_distant_close at center
with charaenter

# "She looks straight at the door, without so much as a glance in my direction."
"ฮานาโกะมองตรงไปที่ประตูไม่แม้แต่จะหันมามองทางฉัน"

# hi "Hanako?"
hi "ฮานาโกะ?"

show hanako basic_normal_close
with charachange

# "She moves to answer, but stops herself."
"ฮานาโกะตั้งท่าจะตอบแต่ก็ยั้งตัวเองไว้"

hide hanako
with charaexit

play sound sfx_dooropen

# "Instead, she silently breaks from my side, opens her door, and steps inside."
"เธอกลับผละออกจากฉันเงียบ ๆ เปิดประตูเดินเข้าไปข้างใน"

# "I look up and down the hallway, a bit lost as to exactly what I should do. Shrugging, I decide to follow her since I don't have any reason to do otherwise."
"ฉันมองโถงทางเดินไปมาด้วยยังงง ๆ ว่าควรทำอย่างไรต่อ ฉันยักไหล่แล้วเดินตามเข้าไป ก็ไม่มีเหตุผลอะไรที่ฉัน\nจะต้องกลับหอตัวเองนี่นะ"

scene bg school_dormhanako_ss
show hanako basic_normal_ss at center
with locationchange

# "Hanako stands in the middle of her room and looks straight at me. It's unnerving when she does this, as it's such an unusual action for her. I open my mouth to speak, but she preempts me."
"ฮานาโกะยืนอยู่กลางห้องมองตรงมาที่ฉัน ฉันกระอักกระอ่วนทุกทีที่เธอมองแบบนี้เพราะปกติเธอจะไม่ทำ\nฉันอ้าปากจะพูดแต่เธอก็ขัดก่อน"

# ha "Could you… close and lock the door?"
ha "รบกวน… ปิดแล้วล็อกประตูให้หน่อยได้ไหม"

# "Hanako's hand reaches for her chest, grabbing her blouse at her heart."
"ฮานาโกะยกมือขึ้นมาที่หน้าอกแล้วกำเสื้อบริเวณนั้นไว้"

hide hanako
with charaexit

play sound sfx_doorclose
with Pause (0.8)                                                                                                                            

play sound sfx_lock

# "I turn and lock the door shut, then freeze."
"ฉันหันไปปิดประตูแล้วต้องชะงัก"

# "The atmosphere is beginning to feel quite strange. This feeling is only made more profound when I hear the curtains being pulled behind me."
"บรรยากาศตอนนี้ชักแปลก ๆ แล้ว และยิ่งแปลกไปใหญ่เมื่อได้ยินเสียงรูดผ้าม่านปิดอยู่ข้างหลังฉัน"

# "It's going to be night soon. We're a guy, and a girl, in a bedroom. She's closing the curtains, and I'm shutting and locking the door. She can't… she can't really have that in mind… can she?"
"ไม่นานก็จะค่ำแล้ว ฉันเป็นชาย เธอเป็นหญิง สองเราในห้องนอน เธอปิดผ้าม่าน ฉันปิดและล็อกประตู เธอคงไม่…\nไม่ได้คิดแบบนั้น… ใช่ไหม"

# "I gulp and turn around very, very slowly. Hanako is in the center of the room, but hasn't turned back to face me."
"ฉันกลืนน้ำลายแล้วหันหน้าไปอย่างเชื่องช้า ฮานาโกะอยู่กลางห้องแต่ยังไม่หันหน้ามาทางฉัน"

show hanako emb_downtimid_ss at center
with charaenter

# ha "You told me about your past, so I have to tell you mine."
ha "นายเล่าเรื่องอดีตให้ฉันฟังแล้ว ตาฉันเล่าเรื่องอดีตของฉันบ้าง"

# "She takes a deep, shuddering breath, and pauses for a number of seconds. Her hands move to her ribbon and begin to tug, all but confirming my thoughts."
"ฮานาโกะสูดหายใจลึกตัวสั่นแล้วเว้นช่วงไปสองสามวินาที เธอขยับมือมาดึงโบว์ที่เสื้อ ซึ่งยิ่งย้ำว่าสิ่งที่ฉันคิดนั้น\nถูกแล้ว"

# hi "H-Hanako…"
hi "ฮะ-ฮานาโกะ…"

show hanako emb_timid_ss
with charachange

# ha "P-please… don't say anything."
ha "ยะ-อย่า… เพิ่งพูดอะไรนะ"

# "I obediently stay hushed as she slips off her ribbon and continues to unbutton her blouse, before working the clip on her bra. The process is slow. Perhaps it just feels slow because of what she's doing. I'm not sure."
"ฉันเงียบตามเธอสั่ง ฮานาโกะปลดโบว์ออกแล้วเริ่มแกะกระดุมเสื้อก่อนจะปลดตะขอเสื้อชั้นใน ซึ่งแต่ละอย่างเป็นไป\nอย่างช้า ๆ หรืออาจจะรู้สึกว่าช้าเพราะเป็นการถอดเสื้อผ้าก็ได้ ไม่แน่ใจ"

# "Frozen to the spot, all I can do is watch as Hanako, hands trembling, unclips her skirt and lets it drop to the ground."
"ฉันได้แต่ยืนอยู่กับที่มองฮานาโกะที่ปลดกระโปรงมือสั่น ๆ ก่อนจะปล่อยทิ้งลงกับพื้น"

play music music_hanako fadein 1.0

scene ev hanako_scars:
with whiteout

# "Finally, she takes her blouse in her hands and draws it off, her bra falling from her shoulders. And so, Hanako stands in the middle of the room all but bared, save for her stockings and underwear."
"จนในที่สุดเธอก็จับเสื้อถอดออกมาและปล่อยให้เสื้อชั้นในไหลออกจากบ่า เหลือเพียงฮานาโกะที่ยืนอยู่กลางห้อง\nด้วยกายที่มีเพียงถุงน่องและกางเกงในปกปิดอยู่"

# ha "This is me. All… of me."
ha "นี่คือฉัน ตัวฉัน… ทั้งหมด"

show ev hanako_scars_large:
    xalign 0.0 yalign 1.0 subpixel True
    acdc_warp 30.0 xalign 1.0 yalign 0.0
with locationchange

# "My eyes are immediately drawn to the scarring on her back. The skin on her right side is of a similar texture to that of her face, but it's also stretched taut and covering a much larger area. The scarring is by far the worst on the shoulder, buttock, and thigh."
"ตาฉันมองไปที่แผลเป็นตรงแผ่นหลังของฮานาโกะทันที ผิวตามลำตัวซีกขวาของเธอคล้ายกับผิวบนหน้า แต่เป็นรอย\nที่ลากยาวกว่าและกินพื้นที่เยอะกว่า ส่วนที่เป็นแผลเป็นหนักที่สุดเห็นจะเป็นบริเวณไหล่ ก้น กับต้นขา"

# "Just as my heart attack redefined my life… this is the event that redefined Hanako's."
"นี่คือเหตุการณ์ที่กำหนดความเป็นตัวของฮานาโกะขึ้นมาใหม่… เหมือนอย่างที่เหตุการณ์หัวใจวายของฉัน\nกำหนดชีวิตฉัน"

# "If I'd seen this when I first met her, I'd have been shocked. Not only at the sight, but also at the idea that something like this was survivable."
"ถ้าฉันเพิ่งเจอฮานาโกะแล้วได้เห็นรอยแผลเป็นนี้ฉันคงตกใจ ไม่ใช่แค่เพราะภาพที่เห็น แต่ตกใจว่ารอดจากเหตุการณ์\nที่ทำให้เกิดแผลขนาดนี้มาได้ด้วย"

# "But after having had time to get used to the idea, and after seeing the scars on her face, hands and collar, my reaction is more measured. My reaction right now is not due to her scarring, but to her body."
"แต่พอมีเวลาทำใจให้ชินและได้เห็นแผลเป็นบนหน้า มือ กับคอบ่อย ๆ แล้วฉันก็ไม่ได้ออกอาการอะไรมาก ที่ฉัน\nตอบสนองอยู่ตอนนี้ไม่ใช่เพราะแผลเป็น แต่เป็นเพราะร่างกายเธอต่างหาก"

# ha "The fire happened when I was eight years old. It was night, and we were sleeping when it started."
ha "เหตุการณ์ไฟไหม้ครั้งนั้นเกิดขึ้นตอนฉันอายุได้แปดขวบ ซึ่งเกิดเมื่อตอนกลางคืนที่พวกเราหลับกันอยู่"

# "Hanako's voice trembles, the shaking of her blouse giving away the fact that her hands are doing just the same."
"เสียงฮานาโกะสั่นเครือ เสื้อที่สั่นอยู่นั้นบ่งบอกว่ามือเธอก็สั่นด้วยเช่นกัน"

# ha "I… curled up into a ball… when the fire swept over me. My mother… tried to shield me. Th-that's the only reason… I lived…"
ha "ฉัน… นอนขดตัว… ตอนที่ไฟโหมเข้ามา แม่ฉัน… คอยกันไฟไม่ให้ถูกตัวฉัน พะ-เพราะแบบนี้ฉันถึง… ได้รอด…"

# "Hanako's eyes begin to moisten, her voice cracking under the combined pressure of exposing herself to me like this, and reliving those painful memories from so long ago."
"ฮานาโกะน้ำตารื้น เสียงเธอสั่นด้วยความกดดันที่ต้องเปิดเผยตัวเองให้ฉันได้เห็นเช่นนี้กับการที่ต้องย้อนนึกถึง\nความทรงจำอันเจ็บปวดเมื่อนานมาแล้ว"

# "I want to say something, anything, to make her feel better. I can't, though. I feel completely useless when faced with a situation like this. She's forcing herself to come so close, yet it's at times like this that I feel most distant to her."
"ฉันอยากจะพูด พูดอะไรก็ได้ พูดให้ฮานาโกะรู้สึกดีขึ้น แต่ก็พูดไม่ออก พอเป็นสถานการณ์แบบนี้แล้วฉันก็รู้สึกว่า\nตัวเองไร้ค่า เธอฝืนตัวเองเพื่อที่จะให้ได้เข้ามาใกล้ชิดฉัน แต่ก็กลับเป็นช่วงเวลาเช่นนี้ที่ฉันจะรู้สึกอยู่ห่างจากเธอ\nมากที่สุด"

# ha "I'm sorry… for making you see this."
ha "ขอโทษ… ที่ต้องให้นายมาเห็นอะไรแบบนี้นะ"

# "There's no point in denying the obvious. I think what I should say now, and what Hanako wants me to say now, is the truth. What I genuinely, honestly, believe."
"คงไม่ต้องปฏิเสธอะไรกับสิ่งที่รู้กันอยู่แล้ว สิ่งที่ฉันควรจะพูดตอนนี้ซึ่งเป็นสิ่งที่ฮานาโกะอยากให้พูดนั้นเป็นความจริง\nเป็นสิ่งที่ฉันเชืื่อสุดใจและมาจากใจจริง"

# hi "It doesn't matter. You're a wonderful person, Hanako. Your body doesn't change that."
hi "ไม่สำคัญหรอก เธอน่ะเป็นคนที่ดีนะฮานาโกะ ร่างกายเธอจะเป็นยังไงก็ไม่เกี่ยวกันเลย"

# "She looks at me for a long time, her breathing uneven as she tries to remain steady amidst the emotions we're both feeling. It feels less like she's looking at me than she's looking through me."
"ฮานาโกะมองฉันเนิ่นนาน ลมหายใจของเธอสั่น ๆ เธอพยายามตั้งสติกับอารมณ์ทั้งหลายที่เราทั้งสองคนต่างรู้สึก\nเหมือนว่าเธอไม่ได้มองมาที่ฉัน แต่มองผ่านเข้ามายังฉัน"

# "I slowly walk towards her, and gently place my hands on her shoulders as she lets go of her blouse. She gasps a little; not in fright, but in simple startlement."
"ฉันค่อย ๆ เดินไปหาฮานาโกะแล้ววางไหล่บนบ่าตอนที่เธอปล่อยเสื้อ เธอสะดุ้งเฮือก แต่ก็ด้วยความตกใจไม่ใช่ความกลัว"

# "Being so close to her causes my mind to become a jumble of feelings. The scarring on her shoulder, plain to see and leather-like to the touch, conflicts strangely with her otherwise soft skin and silky dark hair."
"เมื่อได้อยู่ใกล้เธอแล้วอารมณ์ฉันก็รวนไปหมด แผลเป็นที่เธอเปิดให้เห็นนั้นสัมผัสคล้ายหนังสัตว์ ซึ่งขัดกับผิวอ่อนนุ่ม\nกับผมสีเข้มลื่นสลวยของเธออย่างประหลาด"

# "Hanako is a girl, with all that entails. She's taller than usual for a woman, but still has curves in all the right places. The nape of her neck, just visible thanks to her hair slung over her shoulder, is alluring."
"ฮานาโกะเป็นเด็กผู้หญิง ซึ่งก็มีความเป็นผู้หญิงตามสมควร เธอสูงกว่าผู้หญิงโดยทั่วไป แต่ก็มีส่วนโค้งเว้าตามแต่ละส่วน\nอย่างเหมาะเจาะ ต้นคอเธอที่เปิดให้เห็นเพราะผมไปเคลียบ่าแล้วนั้นช่างมีสเน่ห์"

# ha "I know… that I'm not pretty… like Lilly. I just… wanted you… to see me. The real me."
ha "ฉันรู้… ว่าฉันไม่ได้สวย… เหมือนอย่างลิลลี่ ฉันแค่… อยากให้นาย… ได้เห็นฉัน เห็นตัวตนจริง ๆ ของฉัน"

# hi "I've already seen the real you, though. You didn't need to take off your clothes for that."
hi "แต่ฉันได้เห็นตัวตนของเธอจริง ๆ แล้วนี่นา ไม่เห็นต้องถอดเสื้อผ้าเลย"

scene bg school_dormhanako_ss
show hanagown stockworry_blush_close_ss at center
with locationchange

# "Her lips are open, just a little. She lets out a sharp breath as, without thinking, I breathlessly lean forwards and press my lips to hers."
"เธอเผยอปากออกพ่นลมออกมาโดยไม่ทันได้คิดอะไร ฉันโน้มตัวเข้าไปประทับริมฝีปากพลางกลั้นหายใจ"

# "The kiss only lasts for a fleeting moment before our faces part, our breathing quick and nervous. The feeling of Hanako's mouth lingers, and her eyes remain locked to mine."
"เราจูบกันอยู่เพียงชั่วขณะหนึ่งก่อนจะผละจากกัน ลมหายใจของเราถี่ขึ้นด้วยความประหม่า สัมผัสจากริมฝีปากเธอ\nยังคงค้างอยู่ ฮานาโกะยังคงมองฉันไม่วางตา"

show hanagown stockdistant_blush_ss at center
with charachange

# "Trembling a little myself, I remove my tie and begin undoing the buttons of my shirt. Hanako remains standing where she is, looking at the ground in front of her rather than watching me undress."
"ฉันปลดเน็กไทตัวเองแล้วเริ่มแกะกระดุมเสื้อด้วยมือที่สั่นอยู่หน่อย ๆ ไม่ต่างกันกับฮานาโกะ เธอยังยืนมองพื้นอยู่ที่เดิม\nไม่ได้มองฉันตอนถอดเสื้อผ้า"

# "On the one hand, I'm thankful for that. I've always been somewhat self-conscious of my body, but my scarring has made that quite a lot worse. On the other, though, this atmosphere feels very strange."
"ใจหนึ่งฉันก็นึกยินดีที่ไม่มองเพราะปกติฉันก็อาย ๆ กับร่างกายตัวเองอยู่แล้ว ยิ่งมีแผลเป็นฉันยิ่งอายไปใหญ่ แต่อีกใจ\nฉันก็รู้สึกว่าตอนนี้บรรยากาศนั้นแปลกมาก"

show hanagown stocknormal_blush_ss at center
with charachange

# "My shirt falls to the floor in a heap, as untidy and crumpled as Hanako's blouse and skirt. Hanako's entire body visibly flinches at the sound of the zipper on my trousers being pulled down."
"เสื้อฉันร่วงลงไปกองกับพื้นแบบลวก ๆ เหมือนกันกับกองเสื้อกับกระโปรงของฮานาโกะ เธอสะดุ้งตัวโยนเมื่อได้ยิน\nเสียงรูดซิปกับเสียงกางเกงฉันที่ถกลง"

# "My trousers join my shirt on Hanako's floor next to the bed, as do my socks in short measure. I hesitate before taking off my boxers, and end up leaving them on."
"ฉันวางกางเกงไว้กับพื้นข้างเตียงฮานาโกะ ไม่นานถุงเท้าฉันก็ตามไป ฉันนึกลังเลขึ้นมาเมื่อจะถอดบ็อกเซอร์\nแต่สุดท้ายก็ใส่ไว้"

# "They represent one last hurdle I don't think I can overcome quite yet. Sheer embarrassment stops me, along with not wanting Hanako getting even more worked up. My unease about the situation has also left me needing my own stimulation."
"เป็นสิ่งแทนถึงอุปสรรคขั้นสุดท้ายที่ฉันรู้สึกว่ายังก้าวข้ามไปไม่ได้ ฉันไม่ยอมไปต่อเพราะอาย และเพราะไม่อยาก\nให้ฮานาโกะตระหนกไปมากกว่านี้ และฉันก็ต้องการอะไรมากระตุ้นให้หายอึดอัดจากสถานการณ์นี้ด้วย"

show hanagown stockdistant_blush_ss at center
with charachange

# hi "Hanako…"
hi "ฮานาโกะ…"

hide hanagown
with charaexit

# "She gives a nod without so much as glancing at me, and makes her way to the bed as I do. She walks as if her legs were wooden sticks. I'd find it amusing if I weren't doing exactly the same thing."
"ฮานาโกะพยักหน้าไม่แม้แต่จะมองหน้าเดินไปยังเตียงพร้อม ๆ กันกับฉัน เธอเดินเหมือนกับว่าขาตัวเอง\nเป็นท่อนไม้แข็ง ๆ ซึ่งฉันคงจะขำอยู่ถ้าตัวเองก็ไม่เป็นเหมือนกัน"

# "I take the initiative, turning around and sitting on the side of the bed. I look to her face to invite her to take a seat either next to me or in front of me, but end up awkwardly looking down to stop myself from staring at her body."
"ฉันเป็นฝ่ายเริ่มก่อนโดยการหันตัวนั่งลงที่ริมเตียง ฉันมองหน้าฮานาโกะเป็นการเชื้อเชิญให้มานั่งข้าง ๆ หรือนั่งที่ตัก\nแต่สุดท้ายฉันก็ต้องก้มหน้าลงอย่างกระอักกระอ่วนเพื่อไม่ให้ตัวเองต้องจ้องร่างกายฮานาโกะ"

label th_H29h:

scene evh hanako_bed_boobs_glance
with whiteout

# "Nevertheless, she takes her cue and reluctantly sits between my legs. As she does, a rush of sensations hits me all at once."
"แต่ถึงอย่างนั้นฮานาโกะก็เข้ามานั่งตักฉันอย่างรู้กัน ความรู้สึกทั้งหลายแผ่ซ่านทั่วตัวทันทีที่เธอนั่ง"

# "The feeling of her behind against my crotch is the most obvious, but her scent is just as strong. She's worked up a slight sweat already from her nervousness, and the smell and feeling of her hair is washed across my face."
"สัมผัสจากเธอผ่านเป้ากางเกงนั้นชัดที่สุด แต่กลิ่นของเธอก็ชัดพอกัน เหงื่อเธอเริ่มออกบ้างด้วยความประหม่าแล้ว\nทั้งกลิ่นและสัมผัสจากผมเธอกระจายไปทั่วหน้าฉัน"

# "I try to put on a smile to try and make the situation a bit more comfortable for her, but it feels really stilted. Deciding to try and move things along, one hand finds itself on her breast as the other rests on her leg."
"ฉันลองปั้นยิ้มให้ฮานาโกะไม่ต้องอึดอัดเกินไป แต่ก็กลายเป็นรอยยิ้มเจื่อน ๆ ฉันตัดสินใจเดินหน้าต่อด้วยการ\nยกมือข้างหนึ่งขึ้นมาจับหน้าอกฮานาโกะ ส่วนอีกข้างวางไว้ที่ขาเธอ"

show evh hanako_bed_boobs_blush
with charachange

# "Her lips purse tightly together as she tries, unsuccessfully, to suppress a squeal of surprise at the action."
"ฮานาโกะเม้มปากแน่นหมายจะยั้งเสียงร้องสะดุ้งแต่ก็กลั้นไม่อยู่"

# hi "Sorry, I didn't mean to startle you."
hi "ขอโทษที ไม่ได้ตั้งใจจะทำให้เธอตกใจน่ะ"

# "Hanako takes a breath and shakes her head as her only reply."
"ฮานาโกะสูดหายใจแล้วเพียงสั่นหัวตอบ"

# "A gulp comes from deep in my throat, before beginning to move my hand around, feeling and massaging her breast and nipple. It feels really nice, giving way underneath my palm with just a little firmness."
"ฉันกลืนน้ำลายดังเอื๊อกก่อนจะขยับมือไปสัมผัสและคลึงหน้าอกกับส่วนยอด เป็นสัมผัสที่ละมุน หน้าอกเธอยุบ\nไปตามฝ่ามือที่จับโดยมีแรงต้านเล็กน้อย"

# "For a while I don't think it's helping her get into the mood at all, but slowly her eyelids begin to lower. Her breathing slows to a more rhythmic pattern, and her body begins to relax into mine."
"ฉันคิดอยู่ครู่หนึ่งว่าทำไปแล้วฮานาโกะคงไม่ได้มีอารมณ์ด้วย แต่เธอก็หรี่ตาลงช้า ๆ จังหวะหายใจของเธอเริ่มคงที่\nทั้งตัวเธอค่อย ๆ ผ่อนเกร็งอยู่บนตักฉัน"

# "It's newly satisfying to be able to make Hanako feel like this; definitely better than the feeling of her body alone. I can sense a little hard bump brushing against my fingers that wasn't there before, too."
"เป็นอะไรที่ชวนให้พอใจได้แบบแปลกใหม่ดีที่ทำให้ฮานาโกะรู้สึกแบบนี้ได้ ดีกว่าสัมผัสจากร่างกายเธอเสียอีก ฉันยังรู้สึก\nได้ถึงจุดนูนเล็ก ๆ ที่ขัดกับนิ้วฉันซึ่งก่อนหน้านี้ไม่มีอยู่ด้วย"

###
show evh hanako_bed_crotch_blush
with charachange

# "I slowly move my hand downwards, trying not to surprise her too much. She gives no protest, and my fingers soon begin to move up and down the soft groove between her legs."
"ฉันค่อย ๆ เลื่อนมือลงต่ำด้วยไม่อยากให้ฮานาโกะต้องตกใจมาก เธอไม่ขัดขืนอะไร นิ้วฉันขยับขึ้นลงตามร่องอ่อนนุ่ม\nตรงระหว่างขาเธอ"

# "Her body is pressed against mine by now, a thin sheen of sweat on both of us. She feels warm, and all this has more than served to arouse me, as well as her."
"ตัวฮานาโกะแนบชิดกับฉัน ผิวเราทั้งสองคนต่างมีเหงื่อเคลือบอยู่บาง ๆ ทั้งความอุ่นและอะไรทั้งหลายนั้นมากเกินพอ\nที่จะทำให้ฉันมีอารมณ์ขึ้นมา เธอเองก็ด้วย"

# "Hanako gives a small gasp, my fingers pressing a little harder and moving a little faster almost instinctively. The girl in front of me, the girl pressing against me… I want her. All of her."
"ฮานาโกะร้องออกมาเบา ๆ เมื่อฉันออกแรงกดนิ้วอีกเล็กน้อยและขยับให้เร็วขึ้นอีกหน่อยไปตามสัญชาตญาณ\nเด็กสาวที่อยู่ตรงหน้าฉัน ที่นั่งทับฉัน… ฉันต้องการเธอ ต้องการทุกอย่างที่เป็นเธอ"

show evh hanako_bed_crotch_glance
with charachange

# "I stop moving my fingers, making Hanako give a long breath of relief from the feelings welling up inside of her. Her face looks to mine a little, silent, but expectant."
"ฉันหยุดนิ้วให้ฮานาโกะได้ถอนหายใจยาวพักจากความรู้สึกที่สะสมขึ้นอยู่ในตัวเรื่อย ๆ เธอเหลือบมามองฉันเงียบ ๆ\nด้วยความคาดหวังบางอย่าง"

# "All I do is nod. I don't know which one of us is more apprehensive right now."
"ฉันได้แต่พยักหน้ารับ ไม่รู้เหมือนกันว่าฉันหรือเธอที่ตื่นเต้นกว่ากัน"

scene bg school_dormhanako_ss
with locationchange

# "I push myself back onto the bed, extricating myself from Hanako with a certain amount of reluctance. For her part, she slides back and lies down with her head on her pillow, breathing heavily all the while."
"ฉันผละตัวเองออกจากฮานาโกะเข้ามาที่เตียงด้วยความยากลำบากเล็กน้อย ส่วนเธอก็ขยับตัวออกแล้วนอน\nหนุนหมอนพร้อมลมหายใจหอบหนัก"

scene evh hanako_missionary_underwear
with whiteout

# "Hanako lying in front of me, her panties darkened, her chest heaving, her face flushed, and her eyes looking into mine… her scars just make her look all the more unique. I'm left without words that she'd allow me to see her like this."
"ฮานาโกะนอนอยู่ต่อหน้าฉัน กางเกงในเธอสีเข้มขึ้น หน้าอกของเธอขยับขึ้นลง ใบหน้าแดงฉ่า ตามองฉัน…\nแผลเป็นนั้นยิ่งทำให้เธอดูมีเอกลักษณ์ ฉันถึงกับไม่รู้จะพูดอะไรเมื่อเธอให้ฉันได้เห็นเธอในสภาพนี้"

# "I bring myself closer to her, closing my hands on her waist. I wait for her to nod before taking a delicate hold of her stockings, taking them up a bit as gently as I can manage."
"ฉันเข้าไปใกล้ ๆ แล้ววางมือไว้ที่เอวเธอ ฉันรอให้ฮานาโกะพยักหน้าก่อนแล้วถึงค่อย ๆ จับถุงน่องนั้นแล้วดึงขึ้น\nอย่างเบามือที่สุด"

# "I don't think I can get them off without tearing them, so I end up leaving them on her legs and moving her panties aside."
"ฉันคงถอดถุงน่องออกหมดแบบไม่ให้ขาดไม่ได้ สุดท้ายจึงถกขึ้นมาไว้ที่ขาแล้วจับกางเกงในเลื่อนออกด้านข้าง"

# "Hanako lies practically naked on the bed; her most delicate parts and the scarring of her body are now plain to see."
"เรียกได้ว่าตอนนี้เธอนอนเปลือยอยู่บนเตียงแล้ว ทั้งส่วนที่บอบบางที่สุดกับส่วนที่เป็นแผลเป็นของเธอปรากฏให้เห็น\nทั้งหมด"

# "Bringing my fingers to her crotch, I stroke her a little more, causing her breath to catch. She should be okay if she's this aroused, so I open my boxers and move myself up a little on the bed."
"ฉันยื่นนิ้วไปวางไว้ที่หว่างขาเธอแล้วคลึงอีกเล็กน้อยจนลมหายใจเธอขาดห้วง ถ้าตื่นตัวขนาดนี้แล้วน่าจะใช้ได้\nฉันถอดบ็อกเซอร์แล้วย้ายตัวเข้ามาที่ด้านในเตียง"

# "Hanako's entire body tenses as I bring myself closer to her, her eyes widening. She's… scared?"
"พอฉันขยับเข้าใกล้ฮานาโกะแล้วทั้งตัวเธอก็เกร็งพร้อมดวงตาเบิกโพลง เธอ… กลัวเหรอ"

# "I take a long breath, before realizing something I should have thought of before. I close my eyes and concentrate deeply."
"ฉันสูดหายใจลึก ๆ ก่อนจะนึกอะไรที่ควรนึกได้ตั้งแต่ก่อนหน้านี้แล้ว ฉันหลับตาแล้วตั้งสติ"

# "My heart thumps away as I focus my mind on its beating. It's faster than usual, of course, but the beat is regular. I… think… I can keep it in check, if I take this slowly."
"ฉันจดจ่ออยู่กับหัวใจที่เต้นอยู่ เต้นรัวกว่าปกติ แต่จังหวะยังสม่ำเสมออยู่ ฉัน… ว่า… น่าจะพอไหว ถ้าทำแบบค่อย ๆ"

# ha "Are you… okay…?"
ha "นายไหว… หรือเปล่า…"

# "I open my eyes and look at her. I guess that must have looked pretty worrying to someone else watching me."
"ฉันลืมตามองฮานาโกะ ท่าทีเมื่อกี้ของฉันคงดูน่าเป็นห่วงพอตัวเลยสินะ"

# hi "I'm okay. I was just making sure that I was."
hi "ไหว แค่ดูให้แน่ใจเฉย ๆ น่ะว่าตัวเองยังไหว"

# "She hesitates a little before nodding. She looks a little less afraid than before, so maybe showing her that I was also worried helped reassure her."
"ฮานาโกะยังลังเลอยู่หน่อย ๆ แต่ก็พยักหน้า เธอไม่ได้ดูกลัวเท่าเมื่อครู่แล้ว อาจจะเพราะเห็นว่าฉันเองก็กังวลเหมือนกัน\nแล้วถึงได้สบายใจขึ้นมา"

# "I lean over her and press my lips to hers, our tongues tentatively touching. I can feel her body becoming less tense under mine, so it's getting both of us back into the right mood."
"ฉันโน้มตัวเข้าไปทาบทับริมฝีปากกับเธอ ลิ้นเราสัมผัสกันแบบกล้า ๆ กลัว ๆ ตัวเธอที่อยู่ข้างใต้ฉันนั้นเริ่ม\nคลายความเกร็งลง เราทั้งสองเริ่มกลับมามีอารมณ์กันอีกครั้ง"

# "Then I remember something and pull back."
"แล้วฉันก็นึกอะไรได้ก่อนจะถอนตัวออกมา"

# "I lean over the side of the bed to where my trousers are, my hand reaching for the back pocket. I feel around blind for a few seconds, until a little foil square brushes just underneath my fingertip."
"ฉันเอี้ยวตัวไปหากางเกงที่กองอยู่ข้างเตียงแล้วเอื้อมไปที่กระเป๋าหลังคลำ ๆ หาบางอย่างจนปลายนิ้ว\nสัมผัสเข้ากับซองสีเงินขนาดเล็ก"

# "I quickly pull it out and right myself on the bed, sitting back from Hanako a little and fiddling with the packet. It takes a little while for everything to go on correctly, but eventually the rubber sleeve covers what it should, fitting snugly."
"ฉันหยิบออกมาทันทีแล้วจัดแจงตัวเองกลับมานั่งท่าเดิมห่างจากฮานาโกะเล็กน้อยก่อนจะจับซองนั้นไปมา ต้องงม\nอยู่สักพักกว่าทุกอย่างจะลงตัวถูกต้อง สุดท้ายถุงยางก็มาครอบอยู่กับสิ่งที่ควรครอบตามหน้าที่อย่างพอดิบพอดี"

# "My slight confusion at my first time trying to work a condom seems to have amused her a little, and as I position myself over her, we share a small nervous laugh. Now, though, I need to try and concentrate."
"ดูท่าว่าฮานาโกะจะชอบใจอยู่บ้างที่เห็นฉันใส่ถุงยางครั้งแรกนั้นแบบไม่ค่อยเป็น และเมื่อฉันตั้งท่าเตรียมแล้วเราก็\nหัวเราะเบา ๆ กันอย่างกระอักกระอ่วน แต่ตอนนี้ต้องตั้งสมาธิแล้ว"

# "I look down and try to get my knees and waist in what I think are the right places, and take my penis in my slightly shaking hand. Hanako's face is looking at mine, but her eyes are pointed down at where our crotches meet."
"ฉันก้มมองแล้วจัดให้เข่ากับเอวอยู่ในตำแหน่งที่คิดว่าน่าจะใช่แล้วจับของตัวเองด้วยมือที่ยังสั่น ๆ หน้าของฮานาโกะ\nอยู่ตรงกับหน้าฉัน แต่ตาเธอมองตรงที่หว่างขาของเราสองคน"

# "With a short breath, I position the head and push my hips forward."
"ฉันสูดหายใจตื้น จ่อตรงส่วนปลายแล้วดันเอวไปข้างหน้า"

scene evh hanako_missionary_closed
with charachange

# ha "Aahn…!"
ha "อ๊า…!"

# "In one stroke, I push myself fully inside of her. The rush of sensations and emotions fills my head, and Hanako yelps in pain."
"ฉันดุนตัวเองเข้าไปข้างในเธอทั้งหมดรวดเดียว สัมผัสกับอารมณ์ทุกอย่างไหลบ่าเข้ามาในสมอง ส่วนฮานาโกะ\nร้องด้วยความเจ็บ"

# "Looking at her face makes me feel uneasy. I mistakenly pushed too hard and too fast, and caused her more pain than necessary. Neither of us really knows what we're doing, and the last thing I wanted was to hurt her."
"พอมองหน้าเธอแล้วฉันก็อึดอัด ฉันเผลอดันแรงและเร็วเกินไปจนฮานาโกะต้องเจ็บเกินความจำเป็น เราต่างไม่รู้\nว่าต้องทำอย่างไร และสิ่งที่ฉันอยากเลี่ยงที่สุดเลยคือการทำให้เธอเจ็บ"

scene evh hanako_missionary_open
with charachange

# "Hanako opens her eyes again and looks towards me. She must have seen how troubled I look, as she tries her best to put on a happy face. It's not very convincing at all."
"ฮานาโกะลืมตาอีกครั้งมองมาทางฉัน คงเห็นว่าฉันทำหน้าลำบากใจอยู่ถึงได้ปั้นสีหน้าให้ดูมีความสุขขนาดนั้น\nซึ่งไม่เนียนเอาเสียเลย"

# "I look down and begin, slowly, to move my hips again after giving her a few moments to recover."
"ฉันก้มมองแล้วค่อย ๆ เริ่มขยับเอวอีกครั้งหลังจากที่เว้นช่วงให้ฮานาโกะได้พักแล้ว"

# "The movement feels really unnatural, and I can feel muscles moving all over my lower body that I haven't felt moving in this way before."
"เป็นการขยับที่ไม่เป็นธรรมชาติเอามาก ๆ รู้สึกว่ากล้ามเนื้อร่างกายส่วนล่างได้ขยับในแบบที่ไม่เคยขยับมาก่อนเลย"

# "I know I'm putting stress on my heart that I probably shouldn't, as well, and with every movement I keep track of my heart's beat."
"และฉันก็รู้ด้วยว่าฉันทำให้หัวใจต้องทำงานหนักเกินสมควร ฉันคอยจับสังเกตจังหวะหัวใจทุกครั้งที่ขยับตัว"

# "The feeling inside of Hanako is soft and warm, and if not for the condom deadening a little of the sensation, I doubt I'd be able to last very long at all. Her soft gasps and constant movements don't help at all, either."
"สัมผัสภายในฮานาโกะนั้นทั้งนุ่มทั้งอุ่น ซึ่งถ้าไม่มีถุงยางคอยซับความรู้สึกไปหน่อย ๆ แล้วฉันคงทนได้ไม่นานแน่\nทั้งการขยับตัวเรื่อย ๆ กับเสียงร้องอ่อนหวานของเธอนั้นช่วยเร้าอารมณ์เข้าไปอีก"

scene evh hanako_missionary_clench
with charachange

# "For Hanako's part, the look of pain doesn't really seem to be dissipating as I'd hoped. Her scar tissue causes one side of her body to move a little differently from the other, and strands of her hair are by now sticking to her face."
"สีหน้าที่ดูเจ็บ ๆ ของฮานาโกะนั้นไม่ได้หายไปอย่างที่หวังไว้ ผิวหนังส่วนที่เป็นแผลเป็นซีกหนึ่งของเธอนั้นเขยื้อน\nไม่เหมือนกับอีกซีก และเส้นผมยังระหน้าเธอไปหมด"

# "I put my arms around her body and lift it up a little. After some squirming for the both of us, we try positioning ourselves a bit differently to minimize her pain."
"ฉันโอบตัวยกเธอขึ้นมาเล็กน้อย เราเขยิบตัวไปมาอยู่ครู่หนึ่งจัดท่าให้ต่างจากเดิมเพื่อไม่ให้ฮานาโกะต้องเจ็บมาก"

# "With my hands holding her legs, both of us are moving in less and less measured movements by now. The smell of Hanako fills my senses, and from this position, I'm not stressing my body quite as much."
"เราสองคนขยับตัวได้แบบสบายขึ้นเรื่อย ๆ โดยมีฉันจับขาเธอไว้ กลิ่นฮานาโกะแทรกเข้ามาในความรับรู้ ท่านี้\nทำให้ฉันไม่ต้องออกแรงมากด้วย"

# "My sense of time seems distorted, and I feel like I'm starting to get faint from hyperventilating. I want Hanako to feel good, though, and I can't stop now that we've reached this point."
"เหมือนสมองส่วนรับรู้เวลาจะเพี้ยนไปแล้ว และเหมือนจะหายใจเกินจนคล้ายจะเป็นลมให้ได้ แต่ฉันก็อยากให้ฮานาโกะ\nรู้สึกดี มาถึงขั้นนี้แล้วจะให้หยุดก็คงไม่ได้"

# "A new wave of pleasure suddenly begins to wash over me. My feelings are beginning to well up, and I don't think I can control them any more. I speed up, concentrating less and less on pacing myself."
"ความหวามไหวเข้าถาโถมในฉับพลัน ความรู้สึกเริ่มก่อตัวขึ้นเรื่อย ๆ จนฉันแทบคุมไม่อยู่แล้ว ฉันเร่งการขยับ\nโดยเริ่มไม่ได้สนใจกับการผ่อนจังหวะให้เหมาะกับตัวเอง"

# "Every time it feels like we've found a rhythm, we lose it in our movements. From the sounds she's making, I don't think this position's helped Hanako feel much better, and I don't think I'm going to be able to hold her much longer, either."
"ทุกครั้งที่เหมือนจะได้จังหวะลงตัวแล้วตัวเราก็เคลื่อนจนจังหวะนั้นหายไป ท่านี้ไม่น่าช่วยให้ฮานาโกะรู้สึกดีขึ้นเท่าไหร่\nและฉันก็น่าจะกลั้นได้อีกไม่นานแล้วด้วย"

# "I turn and lay her back down on the bed, both of us well beyond the point of doing anything but reaching the end."
"ฉันวางตัวฮานาโกะลงกับเตียง ตอนนี้สิ่งที่เราทั้งสองทำต่างมีเพียงการไปให้ถึงที่หมายเท่านั้น"

# "One thrust after another, I begin to feel that point coming, frantically tensing myself to try and stave it off for as long as I can."
"เมื่อกระแทกเข้าไปเรื่อย ๆ ก็เริ่มสัมผัสได้ว่าใกล้เต็มที ฉันเกร็งสุดชีวิตยื้อไว้ให้นานที่สุดเท่าที่จะทำได้"

# hi "Hanako…!"
hi "ฮานาโกะ…!"

scene evh hanako_missionary_closed
with charachange

# "Hanako gives a small shriek as my mind blanks. My waist hits hers with a fair amount of force as I hit the point of climax, and I can feel myself twitching inside of her. Her body twists and turns under mine, only heightening the feelings of euphoria."
"ฮานาโกะร้องเสียงแหลมเล็ก หัวสมองฉันว่างเปล่า เอวฉันกระทบเข้ากับเธออย่างหนักเมื่อฉันถึงฝั่งแล้วและยังรู้สึก\nถึงตัวเองที่กระตุกอยู่ข้างใน เธอบิดตัวไปมาจนทำให้ฉันเสียวซ่านขึ้นไปอีก"

window hide

label th_H29x:

scene bg school_dormhanako_ni
show white
with Dissolve(3.0)

window show

# "And then, after a couple of seconds… it ends."
"และผ่านไปสองสามวินาที… ทุกอย่างก็สิ้นสุดลง"

# "The sound of Hanako's breathing and my own rings in my ears, almost painfully loudly. Hanako holds an arm over her face, her mouth open and gulping in air."
"ทั้งเสียงหายใจของฮานาโกะกับเสียงจี๊ดในแก้วหูนั้นดังเสียดหู ฮานาโกะยกแขนขึ้นมาก่ายหน้าพลางสูดหายใจ\nทางปาก"

stop music fadeout 10.0

show white:
    linear 10.0 alpha 0.0

# "As I hold myself over her, suddenly my arms almost give way and my vision distorts, as if someone's grabbed it and pulled sideways. I let myself fall sideways onto the bed beside the panting Hanako, for fear of falling onto her instead."
"ระหว่างที่คร่อมฮานาโกะนั้นอยู่ ๆ แขนฉันก็เปลี้ยราวกับมีใครมาชักแขนออกและภาพตรงหน้าบิดเบี้ยวไป\nฉันทิ้งตัวลงนอนข้างฮานาโกะที่หอบอยู่ด้วยกลัวว่าจะหมดแรงล้มทับตัวเธอไปก่อน"

# "We both lie beside each other, naked and pressed against one another in order to fit on a bed made for a single person. My eyes try to focus on the ceiling, to not much success. Pulling a blanket over us to stave off the cold is all I can do."
"เรานอนเคียงเบียดเสียดแนบกายเปลือยเข้าหากันให้นอนอยู่บนเตียงสำหรับนอนคนเดียวได้ ฉันพยายามจะจดจ้อง\nแค่ตรงเพดานแต่ก็มองได้ไม่นาน จึงเพียงชักผ้าห่มมาคลุมคลายความหนาวให้เราสองคน"

# "The only sound in the room is that of our breathing. The sweat that had accumulated on my body feels uncomfortable. We're both physically and emotionally exhausted, and a complete mess all over."
"ในห้องมีเพียงเสียงหายใจของเราสองคน เหงื่อท่วมตัวจนฉันนอนได้ไม่สบายตัว ทั้งร่างกายและจิตใจเรา\nอ่อนล้ายุ่งเหยิงไปหมด"

window hide

play sound sfx_heartslow
show heartattack alpha 
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.8)

window show

# "My vision slowly begins to return to normal as I continue to stare at the ceiling, but my limbs still feel like jelly. I try to concentrate on my chest, and find its beat irregular and mildly painful."
"ฉันจ้องเพดานจนภาพที่เห็นเริ่มกลับมาเป็นปกติ แต่แขนขาฉันยังอ่อนเหมือนบวบต้ม หัวใจที่เต้นอย่างไม่สม่ำเสมอนั้น\nทำให้เสียดเจ็บขึ้นมาเล็กน้อยเมื่อตั้งสมาธิไปที่หน้าอก"

window hide

play sound sfx_heartslow
show heartattack alpha 
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.8)

window show

# "This is a dangerous time. I have to think this through and not panic, lest I make my situation any worse."
"ตอนนี้อันตราย ต้องคิดให้รอบคอบอย่างไม่ตื่นตระหนก ไม่อย่างนั้นแล้วอะไร ๆ จะต้องแย่กว่านี้แน่"

window hide

play sound sfx_heartslow
show heartattack alpha 
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.8)

window show

# "With a huge effort, I take control of my erratic breathing, forcing myself to make long, deep breaths. I count half a dozen before I start to feel physically calm again, and press my hand to my chest to assure myself."
"ฉันคุมจังหวะหายใจตัวเองที่เพี้ยนไปอย่างสุดความสามารถด้วยการสูดหายใจเข้าลึก ๆ พอนับหนึ่งไปถึงหกแล้ว\nถึงรู้สึกค่อยยังชั่วบ้าง จากนั้นจึงกดหน้าอกเป็นการบรรเทาอาการ"

# "My heartbeat's back to normal. I'm okay."
"หัวใจฉันกลับมาเป็นปกติแล้ว โอเคแล้ว"

scene ev hanako_after_worry
with locationchange

play music music_twinkle fadein 1.0

# "I turn my face towards Hanako, who's already looking at me. Her expression looks pretty dazed, but underneath that, there's definitely a look of concern. She's realized what happened."
"ฉันหันไปมองฮานาโกะที่มองฉันอยู่ก่อนแล้ว สีหน้าเธอดูเหม่อ ๆ ทว่าเห็นชัดว่ามีความกังวลแฝงอยู่ เธอรู้ว่าเมื่อครู่\nเกิดอะไรขึ้น"

# hi "I'm… okay. Everything's… back to normal."
hi "ฉัน… โอเคแล้ว ทุกอย่าง… กลับมาเป็นปกติแล้ว"

# "I find myself barely able to get the words out between breaths. I don't think sex would tire a normal body out this much, so I have no doubt my condition's at least partially at fault. Why did my body have to do this right now?"
"ฉันหอบหนักจนแทบพูดไม่เป็นคำ ไม่คิดเลยว่าเซ็กส์จะทำให้เพลียได้ขนาดนี้ อาการของฉันก็คงมีส่วนด้วยแน่นอน\nทำไมร่างกายฉันถึงมาเป็นแบบนี้เอาตอนนี้นะ"

scene ev hanako_after_smile
with charachange

# "All thoughts of my heart, though, are pushed aside as I see the wide smile forming on Hanako's face."
"แต่รอยยิ้มที่ผุดขึ้นบนใบหน้าฮานาโกะก็ปัดเป่าทุกความคิดเรื่องหัวใจให้พ้นไปจากสมอง"

# "As always, I smile back without another thought. Hanako's smile has always been infectious in its almost childlike sweetness and earnesty, something that sets her apart from anyone else I know."
"ฉันยิ้มกลับไปไม่คิดอะไรเหมือนอย่างเคย รอยยิ้มของฮานาโกะนั้นช่างจริงใจและหวานล้ำเหมือนเด็ก ๆ จนทำให้\nอดยิ้มตามไม่ได้ เป็นสิ่งที่ทำให้ฮานาโกะนั้นแตกต่างจากคนอื่นที่ฉันเคยรู้จักมา"

# "Right now… we don't need words. Everything we want to communicate to each other, we can share just fine without them."
"ตอนนี้… เราไม่ต้องการคำพูดใด ๆ ทุกอย่างที่เราอยากสื่อสารนั้นส่งถึงกันและกันได้โดยไม่ต้องใช้คำพูด"

stop music fadeout 2.0

scene black
with shuteye

#*********************

label th_H30:

scene black
with dissolve

# hi "Mmh…"
hi "อือ…"

play music music_pearly

scene bg school_dormhanako at left
with openeye

# "My eyes feel heavy as they slowly open, the light from outside making me blink a bit to let them get adjusted. My body feels like lead, and my head feels just as heavy."
"เปลือกตาฉันที่ค่อย ๆ เปิดออกนั้นหนักอึ้ง แสงที่ส่องจากข้างนอกเข้ามาทำให้ฉันต้องกะพริบตาสองสามครั้ง\nเป็นการปรับตา ทั้งตัวก็เหมือนมีตะกั่วถ่วง หัวก็หนัก ๆ เหมือนกัน"

# "Waking up to an unfamiliar ceiling is an uncomfortable feeling. It reminds me of the first time I awoke to the dimpled white tile ceiling of the hospital."
"ตื่นมาแล้วเห็นเพดานที่ไม่คุ้นตาแล้วก็รู้สึกอึดอัดแปลก ๆ นึกถึงตอนที่ตื่นมาเจอเพดานสีขาวที่มีรอยยุบ\nในห้องของโรงพยาบาลเป็นครั้งแรกเลย"

# "It's only after spending a few seconds staring up at it that I realize where I am. This is Hanako's dormitory room."
"จ้องอยู่ได้สองสามวินาทีถึงนึกออกว่าตัวเองอยู่ที่ไหน ที่นี่คือห้องฮานาโกะ"

# "I feel as though my heart stopped again, as the events of last night rush through my head, blood rushes to my cheeks, and I shut my eyes once more."
"รู้สึกราวกับหัวใจจะหยุดเต้นอีกครั้งเมื่อเหตุการณ์เมื่อคืนเล่นซ้ำในสมอง เลือดสูบฉีดเข้ามาที่แก้ม ฉันหลับตาลง\nอีกครั้ง"

# "There's very little point to getting myself worked up this early though, so I try to push such things out of my mind for now."
"เช้ามาก็อย่าเพิ่งกระวนกระวายอะไรเลยดีกว่า ฉันคอยปัดความคิดนั้นทิ้งไปจากหัวก่อน"

# "I roll my head to the side to see if Hanako's where she was when I drifted off to sleep. All that's there now is an empty space on the bed, and the room beyond."
"ฉันหันหัวไปด้านข้างมองไปตรงที่ที่ฮานาโกะเคยอยู่ตอนก่อนฉันจะผล็อยหลับไป ซึ่งตอนนี้ตรงนั้นเหลือเพียงเตียง\nที่ว่างเปล่า ในห้องก็ไม่มีใคร"

# "I sluggishly sit up and rub my eyes, before pinching the bridge of my nose and looking around the room."
"ฉันลุกขึ้นนั่งแบบเอื่อย ๆ มาขยี้ตาบีบสันจมูกแล้วมองไปรอบ ๆ ห้อง"

show bg school_dormhanako at right
with charamove_slow

# "The only person here is me. I'm still bereft of my clothes, and after a quick scan of the floor for them, I notice that they're neatly folded in a corner of the room. Try as I might, I can't see Hanako's anywhere."
"ในห้องนี้มีแค่ฉันที่ยังไม่มีเสื้อผ้าติดตัว พอกวาดตามองหารอบ ๆ ห้องก็เห็นว่าเสื้อผ้าของฉันวางพับไว้อย่างดีอยู่ตรง\nมุมหนึ่งของห้อง แต่หาเท่าไหร่ก็หาฮานาโกะไม่เจอ"

# "The foil packet for the condom's been removed too, presumably put into the bin."
"ไม่มีซองถุงยางสีเงินแล้วด้วย อาจจะอยู่ในถังขยะแล้ว"

# "With a great yawn, I get myself out of bed and quickly look for some underwear. I grimace a little at the prospect of putting my boxers back on after yesterday's efforts did a job on them, but I don't have much choice."
"ฉันหาวหวอดใหญ่ลุกออกจากเตียงมองหาชุดชั้นใน ฉันหน้าเบ้ไปเล็กน้อยเมื่อคิดว่าต้องใส่บ็อกเซอร์ที่ผ่านศึกเมื่อวาน\nมาจนบอบช้ำตัวเดิม แต่ก็ใช่ว่าจะมีทางเลือกอื่นละนะ"

# "Taking advantage of the fact that I have some time without anyone around, I get myself dressed for the coming school day in short order."
"ฉันถือเอาจังหวะที่ตอนนี้ไม่มีใครอยู่ด้วยรีบแต่งตัวเตรียมไปเข้าเรียน"

# "And then… I'm alone."
"และแล้ว… ก็ไม่มีใคร"

# "Without anything more to busy myself with, my mind becomes focused on the fact that I'm standing in another person's bedroom after we spent the night together, but there's not a single sign of her around."
"เมื่อไม่มีอะไรอย่างอื่นให้คิดให้ทำแล้วสมองฉันก็จดจ่ออยู่กับเรื่องที่ว่าตอนนี้ฉันอยู่ในห้องนอนคนอื่นที่ฉัน\nนอนค้างอ้างแรมด้วย ซึ่งไม่มีวี่แววว่าเธอคนนั้นอยู่แถวนี้เลย"

play sound sfx_rumble

# "My gut proves to be more helpful than my brain at working out this riddle. With a loud growl, it reminds me that she may well just be getting breakfast."
"ดูท่าว่าท้องไส้จะช่วยฉันได้มากกว่าสมองในการไขปริศนานี้ พอได้ยินเสียงท้องร้องแล้วก็นึกได้ว่าฮานาโกะคงแค่\nออกไปหาข้าวเช้ากิน"

# "I would have liked to wake up next to her, but… maybe it's a good thing that I have a few moments alone."
"ก็อยากจะตื่นมาแล้วเจอฮานาโกะอยู่ข้าง ๆ อยู่หรอก แต่ว่า… ให้ฉันได้อยู่ตัวคนเดียวบ้างก็คงดีเหมือนกัน"

# "Hanako's room, as always, is quite bleak in appearance. There are precious few decorations, and practically no personal artifacts that aren't hidden away in cupboards and drawers."
"ห้องฮานาโกะยังเปล่าเปลือยเหมือนเช่นเคย มีของตกแต่งล้ำค่าอยู่บ้าง ไม่มีของใช้ส่วนตัวอะไรที่ไม่ได้เก็บไว้ในตู้\nหรือลิ้นชักเลย"

# "She's lived here for three years, but the room looks as if it's barely been occupied for a single day."
"ฮานาโกะอยู่ที่นี่มาสามปีแล้ว แต่สภาพห้องเหมือนเพิ่งมาอยู่ได้แทบไม่ถึงวันด้วยซ้ำ"

# "I shouldn't overthink this. She might just like living this way, as some do. Having the ability to put such low stock in physical possessions does have its advantages, but even so, it feels a little disconcerting given her past."
"ไม่ควรไปคิดอะไรมากสิ ฮานาโกะอาจจะใช้ชีวิตอยู่อย่างนี้ คนอื่นที่อยู่แบบนี้ก็คงมี การอยู่แบบไม่ต้องมีของใช้ส่วนตัว\nมากมายก็มีประโยชน์อยู่เหมือนกัน แต่ถึงอย่างนั้น พอนึกถึงอดีตของฮานาโกะแล้วได้มาเห็นสภาพนี้ก็รู้สึก\nไม่สบายใจเหมือนกัน"

# "She said she viewed herself as having had her life on hold while at the orphanage. She certainly lives as if she still does, but… after what happened last night, it's pretty hard to imagine that she still thinks that way."
"ฮานาโกะเคยบอกว่าตัวเองมองว่าชีวิตชะงักไปตอนที่อยู่สถานรับเลี้ยงเด็กกำพร้า ซึ่งเธอก็ยังใช้ชีวิตเหมือนอย่าง\nตอนอยู่ที่นั่นนั่นแหละ แต่ว่า… พอได้เห็นเธอเมื่อคืนที่ผ่านมาแล้วฉันก็ไม่ค่อยจะเชื่อว่าฮานาโกะยังคิดแบบนั้นอยู่\nจริง ๆ"

play sound sfx_dooropen

# "The sound of the doorhandle cracks through my thoughts, and I turn to face it."
"เสียงลูกบิดแทรกเข้ามาในความคิด ฉันหันไปมอง"

show hanako basic_normal at center
with charaenter

# "Sure enough, Hanako comes through and shuts the door behind her. She has what seem to be two microwaved instant meals in her hands, so this is a little difficult."
"เป็นฮานาโกะดังคาด เธอเดินเข้ามาแล้วปิดประตู ในมือเหมือนจะมีอาหารสำเร็จรูปที่อุ่นไมโครเวฟมา คงลำบาก\nอยู่หน่อย ๆ"

# hi "Good morning, Hanako."
hi "อรุณสวัสดิ์ฮานาโกะ"

show hanako basic_bashful
with charachange

# ha "M… 'morning."
ha "ระ… รุณหวัด"

# "She gives a little bow before making her way to her desk, setting down both plates. I can now see them to be small satay dishes, their contents steaming, with a fork stuck inside the rice of each."
"ฮานาโกะก้มหัวเล็กน้อยก่อนเดินมาวางจานทั้งสองใบที่โต๊ะ ตอนนี้ฉันเห็นแล้วว่าในจานเป็นสะเต๊ะกับข้าวที่มีส้อม\nเสียบไว้อยู่ซึ่งมีควันลอยฉุย"

show hanako basic_distant at Position(ypos=1.15)
with dissolvecharamove

# "I give thanks to her for bringing them in, and we each take one and get down to eating. She sits on her desk chair, while I sit on the side of the bed."
"ฉันขอบคุณฮานาโกะที่นำข้าวเช้ามาให้ เราหยิบไปคนละจานแล้วกินกัน เธอนั่งอยู่ที่โต๊ะ ส่วนฉันนั่งอยู่ที่ริมเตียง"

# "I don't like talking while eating, so the silence between us isn't annoying in and of itself. It's the fact that it only exists because we don't quite know what to say to each other that's off-putting."
"ฉันไม่คุยตอนกินข้าวอยู่แล้ว ที่น่าหงุดหงิดจึงไม่ใช่ความเงียบในตอนนี้เพียงอย่างเดียว แต่ที่รู้สึกแปลก ๆ เพราะเรา\nต่างไม่รู้จะพูดอะไรกันต่างหาก"

show hanako basic_normal
with charachange

show hanako basic_distant
with charachange

# "Hanako glances towards me every so often as she eats. I only notice her doing so because I'm doing just the same thing."
"ฮานาโกะกินไปพลางเหลือบมองฉันไปพลางอยู่บ่อย ๆ และที่ฉันรู้ก็เพราะฉันก็ทำเหมือนกัน"

# "We're eating together as if we were a couple. We even had sex last night; a first for the both of us. Something feels… wrong, though."
"เรากินข้าวด้วยกันเหมือนว่าเราเป็นแฟนกัน เมื่อคืนเรามีอะไรกัน—ซึ่งต่างเป็นครั้งแรกของเราสองคน—แล้วด้วย\nแต่เหมือน… มีอะไรผิดที่ผิดทางไป"

# "Maybe that's why we can't say even a word to each other as we finish our plates and leave them in the sink."
"อาจจะเพราะอย่างนี้เราถึงไม่พูดอะไรกันแล้วกินอาหารในจานตัวเองไปจนหมดแล้วเก็บจานไว้ที่อ่างล้างจาน"

scene bg school_girlsdormhall
with locationchange

# "Maybe that's why we leave Hanako's room without holding hands, or making smalltalk."
"อาจจะเพราะอย่างนี้เราถึงออกมาจากห้องฮานาโกะโดยไม่จับมือกันหรือคุยเรื่อยเปื่อยกัน"

# "Maybe that's why it feels as if we're further apart than we've ever been before."
"อาจจะเพราะอย่างนี้ถึงรู้สึกเหมือนว่าเราอยู่ห่างจากกันกว่าทุกที"

# timeskip
scene bg school_scienceroom at left
with locationskip

# "We enter the classroom together, neither of us so much as glancing at each other. Just after we do so, I realize that this may have been a mistake. Shizune lifts her eyebrow at the sight, her suspicions raised."
"เราเข้าห้องเรียนพร้อมกันโดยไม่แม้แต่จะเหลือบมองกัน ทันทีที่เข้าไปฉันก็ระลึกได้ว่าทำพลาดไปแล้ว ชิซูเนะเลิกคิ้ว\nด้วยความสงสัยที่เห็นเราสองคนมาด้วยกัน"

show hanako cover_distant at center
with charaenter

# "We reach the center aisle between the classroom's desks and look to each other. I'm not quite sure what I should say. Does she want me to address her as a girlfriend? I didn't think our relationship was… Oh. That's why this feels so strange."
"เราเดินมาถึงทางเดินที่อยู่ระหว่างโต๊ะนักเรียนแล้วมองตากัน ฉันไม่แน่ใจนักว่าควรพูดอะไรดี อยากให้เรียก\nว่าเป็นแฟนหรือเปล่า ฉันว่าความสัมพันธ์ของเรามันยัง… อ้อ มิน่าล่ะถึงได้รู้สึกแปลกขนาดนี้"

# hi "S-see you."
hi "จะ-เจอกัน"

show hanako cover_bashful
with charachange

# ha "Okay."
ha "โอเค"

hide hanako
with charaexit

# "I awkwardly hold up a hand as we part and take our seats at our respective desks."
"ฉันยกมือโบกให้เธออย่างกระอักกระอ่วนก่อนจะแยกกันไปนั่งที่ของตัวเอง"

# "I can't even look back to her out of embarrassment. I feel like the gulf between Hanako and me is because of me."
"ฉันไม่กล้าหันไปมองฮานาโกะด้วยซ้ำเพราะอาย ที่ระหว่างฮานาโกะกับฉันมีช่องว่างอยู่ก็น่าจะเพราะฉันนี่แหละ"

show shizu invis:
    center
    xpos -0.1
show muto invis:
    center
    xpos 0.75
with None

show shizu basic_normal:
    xpos 0.0
with dissolvecharamove

show muto normal:
    tworight
with dissolvecharamove

# "Shizune begins to make her way towards me, but then Mutou enters the room."
"ชิซูเนะตั้งท่าจะเดินมาหาฉัน แต่ครูก็เข้าห้องมาก่อน"

show shizu invis at Position(xpos=-0.1)
with dissolvecharamove

# "I'm thankful for his arrival being so well-timed, drawing Shizune and her questioning away, to wait for another time."
"ฉันนึกโล่งใจที่ครูมาช่วยยื้อชิซูเนะกับการซักไซ้จากเธอไว้ไปทีหลังได้ตรงจังหวะขนาดนี้"

# "I wouldn't have been able to answer her, anyway."
"ซึ่งยังไงฉันก็คงตอบชิซูเนะไม่ได้อยู่ดี"

# "I like Hanako, but I've never told her what my feelings for her are. Hanako never said she saw me as anything beyond a friend, either. Yet, despite that, we slept together."
"ฉันชอบฮานาโกะ แต่ไม่เคยบอกให้เธอได้รับรู้ถึงความรู้สึกของฉันเลย ฮานาโกะก็ไม่เคยบอกเหมือนกันว่ามองฉัน\nเป็นมากกว่าเพื่อน แต่แม้กระนั้นเราก็หลับนอนด้วยกัน"

stop music fadeout 2.0

scene bg school_scienceroom at left
with shorttimeskip

play sound sfx_normalbell

# "The bell to signal the beginning of lunch rings out. Mutou is taken a little off guard, his chemistry lecture being cut off midsentence, much to his chagrin."
"ระฆังบอกเวลาพักเที่ยงดังขึ้น ครูสะดุ้งเล็กน้อยด้วยไม่อยากให้การสอนวิชาเคมีของตัวเองถูกตัดกลางคันอย่างนี้"

# "For the entirety of the class, his rambling has passed through one ear and out the other as my mind mulls over the question of Hanako. I can't get her out of my mind, and by now I've managed to wind myself up about it."
"เนื้อหาที่ครูสอนมาทั้งคาบนั้นเข้าหูซ้ายทะลุหูขวาไปหมดแล้ว โดยที่ในหัวฉันตั้งคำถามกับเรื่องฮานาโกะอยู่\nฉันสลัดเธอออกไปจากใจไม่ได้เลย และตอนนี้ฉันก็เครียดขึ้นมาแล้วด้วย"

# "I realize that she never said yes to what we did. She didn't say no either, but… would she have been able to? She's extremely submissive at the best of times, and no doubt it took her a gargantuan effort to show me her scarring."
"ฉันฉุกคิดได้ว่าฮานาโกะไม่เคยตอบตกลงกับสิ่งที่เราทำลงไปเลย แต่ก็ไม่ได้ปฏิเสธด้วย แต่ว่า… จะปฏิเสธได้ด้วยเหรอ\nตอนปกติก็เป็นคนที่ยอมอะไรง่าย ๆ อยู่แล้ว และชัดว่าเธอต้องรวบรวมความกล้ามามากแค่ไหนที่จะเปิดแผลเป็นให้ฉันดูได้"

# "I decide to try and at least make conversation with her. That would be better than the monosyllabic communication that's been the most we've managed between each other so far today."
"ฉันตัดสินใจว่าอย่างน้อย ๆ ก็ไปลองคุยดูก่อนแล้วกัน คงจะดีกว่าการสื่อสารพยางค์เดียวที่เราใช้กันมาตั้งแต่ตอนเช้า\nของวันนี้"

show bg school_scienceroom at bgleft
with charamove_slow

show hanako emb_downtimid:
    center
    ypos 1.15
with charaenter

# "I walk to her desk intending to chat, but she awkwardly blushes and looks down even before I've come up to her."
"ฉันเดินไปที่โต๊ะฮานาโกะหมายจะคุยด้วย แต่ยังไม่ทันไปถึงเธอก็ก้มหน้าแดง ๆ นั้นด้วยท่าทีกระอักกระอ่วน"

play music music_rain fadein 4.0

# "I take a breath to speak, but find myself lost for words. What in the world should I say to her?"
"ฉันสูดหายใจเตรียมพูด แต่ก็ไม่มีคำไหนผุดขึ้นมาในหัว จะให้พูดกับฮานาโกะว่าอะไรเล่า"

# "Hearing approaching footsteps, I turn to see Shizune and Misha already making their way towards us, no doubt with the intent to start asking troublesome things."
"พอหันไปตามเสียงฝีเท้าที่ใกล้เข้ามาก็เห็นชิซูเนะกับมิช่าที่เดินมาทางเรา แน่แท้ว่าจะต้องมาถามอะไรชวนลำบากใจ\nแน่นอน"

# "A couple of other classmates are looking at us and gossiping between themselves as they throw sidelong glances. They must also have noticed Hanako and me coming in together earlier."
"เพื่อนร่วมชั้นบางคนก็หันมามองทางเราพลางซุบซิบอะไรกันอยู่โดยเหล่ตามองมา คงจะเห็นที่ฮานาโกะกับฉัน\nเข้ามาด้วยกันเมื่อกี้สินะ"

# "I open my mouth to reassure Hanako, but she preempts me."
"ฉันอ้าปากเตรียมปลอบฮานาโกะ แต่เธอก็ขัดก่อน"

show hanako def_strain
with charachange

# ha "I… I…"
ha "ทะ… ทะ…"

show hanako defarms_strain:
    center
with Dissolvemove(0.3)

# ha "Ivegottogodosomething!"
ha "โทษทีมีธุระ!"

show hanako defarms_strain:
   easeout 0.5 alpha 0.0 xpos 0.0 xanchor 1.0
with Pause(0.5)

hide hanako
with None

# "She gets out of her chair and dashes for the door. A couple of the books and pens that were on her desk are sent falling to the floor in her rush."
"ฮานาโกะลุกจากเก้าอี้พุ่งไปที่ประตู หนังสือกับปากกาที่วางอยู่บนโต๊ะหล่นตกพื้นไปด้วยความรีบของเธอ"

# "Not many people seem to care about this event. A few look around to see what all the fuss is about, but go back to what they were previously doing soon after."
"ไม่มีใครดูจะสนใจเหตุการณ์นี้เท่าไหร่ คนอื่น ๆ แค่มองว่ามีเรื่องอะไรกันแล้วหันกลับไปทำสิ่งที่กำลังทำอยู่กันต่อ"

# "I'm left despairingly looking at the door that Hanako disappeared out of. The idea of running after her passes through my mind, but I'm fairly sure that Hanako can run faster than I can."
"ฉันมองไปทางประตูที่ฮานาโกะออกไปด้วยความสิ้นหวัง แวบหนึ่งฉันคิดว่าจะวิ่งตามไปดีไหม แต่ยังไงฮานาโกะ\nก็คงวิ่งเร็วกว่าฉันแหละ"

# "And besides… what would I say to her once I caught up, anyway?"
"แล้วอีกอย่าง… ต่อให้ตามทันแล้วจะพูดอะไร"

# "Eventually, I simply crouch down and begin picking up the items that had fallen to the ground from her desk. I feel low in every way, reduced to this as students pass by me on their way out of the room."
"สุดท้ายฉันก็เพียงย่อตัวลงเก็บของที่ตกจากโต๊ะฮานาโกะ รู้สึกว่าตัวเองต่ำต้อยเหลือเกินที่ต้องมาก้มเก็บของแบบนี้\nต่อหน้าคนอื่นที่เดินออกห้องไป"

show shizu invis_close:
    tworight
    xpos 0.8
show misha invis_close:
    twoleft
    xpos 0.2
with None

show shizu behind_blank_close at tworight
show misha perky_smile_close at twoleft
with dissolvecharamove

# "I feel a tap on my shoulder. I look up to see Shizune and Misha looking at me, curiosity about the situation written on their faces, mixed with a slightly apologetic look at the idea that they were partially responsible for what just happened."
"มีใครบางคนมาแตะไหล่ฉัน เมื่อเงยหน้ามองก็เห็นชิซูเนะกับมิช่าที่มองฉันอยู่ด้วยสีหน้าสงสัยถึงเรื่องที่เกิดขึ้น\nและเจือด้วยความรู้สึกผิดที่คิดว่าตัวเองคงมีส่วนผิดกับเหตุการณ์เมื่อครู่นั้น"

show shizu basic_normal2_close
with charachange

shi "…"

show misha sign_confused_close 
with charachange

# mi "Hicchan, if we can help at all…"
mi "ฮิจัง ถ้ามีอะไรที่เราพอจะช่วยได้…"

# "I just shake my head. This isn't a matter for them, and from Shizune's expression and the tone of Misha's voice, I think they know the same thing."
"ฉันเพียงสั่นหัวตอบ เรื่องนี้ไม่ใช่เรื่องของสองคนนั้น และดูสีหน้าชิซูเนะกับฟังน้ำเสียงมิช่าแล้วก็รู้ว่าทั้งสองคนก็คงรู้\nเหมือนกัน"

show shizu behind_blank_close
with charachange

with Pause(0.3)

hide misha
hide shizu
with charaexit

# "Shizune acknowledges my response, and gives a solemn bow before making her way out of the room. Misha soon follows her out, obediently following her role as Shizune's shadow."
"ชิซูเนะรับทราบที่ฉันตอบไปแล้วโค้งตัวให้อย่างจริงจังก่อนจะเดินออกห้องไป มิช่าเดินตามไปทันทีในฐานะเงา\nของชิซูเนะอย่างว่าง่าย"

# "I pick myself up, books and pens in hand, and place them inside Hanako's desk. With the classroom now empty, I end up just leaning against her desk and thinking to myself in silence."
"ฉันหยิบหนังสือกับปากกาแล้วลุกขึ้นยืนมาวางไว้บนโต๊ะฮานาโกะ พอในห้องไม่มีใครแล้วฉันก็ยืนพิงโต๊ะฮานาโกะ\nพลางครุ่นคิดอยู่กับตัวเอง"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

# n "\n\nIt feels like there's a complete emotional disconnect between Hanako and me. We haven't known each other for all that long, and despite wanting to start going out with her, I really don't know that much about how Hanako views things."
n "\n\nเหมือนว่าอารมณ์ระหว่างฮานาโกะกับฉันยังไม่สัมพันธ์กันเลย เราไม่ได้รู้จักกันมานานขนาดนั้น และถึงฉันจะอยาก\nคบกับฮานาโกะ ฉันก็ไม่ได้รู้มากว่าเธอมองอะไร ๆ เป็นอย่างไรบ้าง"

# n "I've been studying as hard as I can for exams, but I still don't feel like I have any real sense of direction behind it. I tried to be a friend to Hanako, even if I couldn't tell her my feelings, and all we've done is drive each other apart."
n "ฉันอ่านหนังสืออย่างหนักเพื่อเตรียมสอบ แต่เอาเข้าจริงแล้วฉันก็ไม่ได้รู้สึกว่าทำไปโดยมีทิศทางอะไรเลย ฉันคอย\nผูกสัมพันธ์เป็นเพื่อนกับฮานาโกะต่อให้ฉันจะบอกความรู้สึกกับเธอไม่ได้ ทว่าสิ่งที่ฉันทำรังแต่จะถ่างระยะให้เราห่าง\nออกจากกันไปอีก"

# n "\nI couldn't even write a letter back to the one girl who ever loved me, Iwanako."
n "\nแม้แต่จะเขียนจดหมายถึงเด็กสาวที่เคยรักฉัน—อิวานาโกะ—ยังเขียนไม่ได้เลยด้วยซ้ำ"

# n "\nWhat should I do… what can I do… I simply don't know the answer to either of those questions. I do know that nobody else can help me with them."
n "\nต้องทำยังไง… ฉันทำอะไรได้บ้าง… ฉันตอบคำถามสองข้อนั้นไม่ได้เลย ซึ่งฉันรู้ว่าไม่มีใครจะมาช่วยคิดคำตอบ\nให้ได้หรอก"

# n "Just going back to the way things were would be enough to make me happy, but I know that it can never happen. Something changed between us last night. Maybe it changed beforehand, and it just came to a head then."
n "แค่อะไร ๆ กลับไปเป็นเหมือนอย่างเดิมฉันก็มีความสุขแล้ว แต่ฉันก็รู้ดีว่าคงเป็นไปไม่ได้ บางอย่างระหว่างเรา\nได้เปลี่ยนไปแล้วเมื่อคืน อาจจะเปลี่ยนตั้งแต่ก่อนหน้านั้นแล้วแต่มาถึงจุดพลิกผันจริง ๆ เอาเมื่อตอนนั้น"

nvl clear

# n "\n\nI know that there's a wall that Hanako has between me and her. I've been hitting that wall every time I've tried to interact with her on any level."
n "\n\nฉันรู้ว่าฮานาโกะตั้งกำแพงกั้นระหว่างฉันกับเธอไว้อยู่ ทุกครั้งที่ฉันจะปฏิสัมพันธ์กับเธอไม่ว่าจะทางไหน\nก็จะชนเข้ากับกำแพงนั้นตลอด"

# n "But now I'm beginning to think that I have my own wall between us just as much as she does. She had to practically drag my past out of me, and mine was much less traumatic than hers."
n "แต่ตอนนี้ฉันชักคิดแล้วว่าฉันเองก็ตั้งกำแพงไว้หนาพอ ๆ กันกับฮานาโกะ เธอต้องฉุดฉันให้พ้นจากอดีต ซึ่งความสาหัส\nของอดีตฉันนั้นแทบเทียบไม่ได้กับอดีตของฮานาโกะเลยด้วยซ้ำ"

# n "I want to say it's because I haven't had long to adjust since my heart attack, but I know full well that it would just be an excuse."
n "ก็อยากจะพูดอยู่หรอกว่าที่ฉันยังอยู่แบบนี้เป็นเพราะฉันไม่มีเวลาให้ปรับตัวได้มากเท่าไหร่ตั้งแต่ที่หัวใจวายครั้งนั้น\nแต่ก็รู้อยู่เต็มอกว่าความคิดนั้นก็เป็นแค่ข้ออ้าง"

# n "The one time I can recall when it really felt like she was opening up to me of her own accord, when we were playing billiards in the city, I was the one who stopped her from going further."
n "ครั้งเดียวที่จำได้ว่ารู้สึกว่าฮานาโกะเปิดใจให้ฉันด้วยความสมัครใจจริง ๆ คือตอนที่เล่นบิลเลียดกันในตัวเมืองตอนนั้น\nเป็นฉันเองที่หยุดเธอไว้ไม่ให้เล่าไปมากกว่านั้น"

# n "\n\nI want to know Hanako better. I want to save our friendship, if not begin a real relationship with her."
n "\n\nฉันอยากจะรู้จักฮานาโกะให้ดีกว่านี้ ฉันอยากจะกอบกู้มิตรภาพของเรา หรือจะเริ่มความสัมพันธ์จริง ๆ สักครั้ง\nกับเธอก็ได้"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear
window show

# "My mind begins to tick as I sit against her desk, thinking to myself in the empty classroom that we've spent so much time in together."
"ฉันพิงโต๊ะฮานาโกะไปพลางนึกคิด คิดอยู่กับตัวเองในห้องเรียนซึ่งไม่มีใครห้องนี้ที่เราได้ใช้เวลาอยู่ร่วมกันบ่อย ๆ"

stop music fadeout 2.0

# "I have to talk to Hanako."
"ฉันต้องไปคุยกับฮานาโกะ"

#*********************

label th_H31:

scene bg suburb_park
with shorttimeskip

play music music_moonlight fadein 0.5

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_parkambience fadein 2.0

# "I pace around in the park, feelings of anxiety rolling over me. Every so often I reach into my pocket to take out my phone, but each and every time I hesitate and end up slipping it back in."
"ฉันเดินไปตามสวนสาธารณะพร้อมความกังวลที่แล่นอยู่ในใจ ฉันควักกระเป๋าหมายจะหยิบโทรศัพท์ออกมา\nอยู่หลายครั้ง แต่สุดท้ายก็เก็บกลับไว้อย่างเดิมทุกครั้ง"

# "If this were any normal situation, I wouldn't be cutting classes. Unfortunately, it isn't, and so I find myself in the town below the school at two in the afternoon."
"ถ้าเป็นสถานการณ์ทั่ว ๆ ไปฉันคงไม่โดดเรียน แต่คราวนี้ไม่ใช่ ฉันจึงมาอยู่ที่สวนสาธารณะที่เมืองด้านล่างโรงเรียน\nตอนบ่ายสองโมง"

# "Ever since I met Hanako, I've been the one to initiate everything between us. The one that started conversations, went to her wherever she was, and suggested what we should do. Today, this once, I don't want to be the only one doing that."
"ตั้งแต่ที่ได้เจอฮานาโกะมาฉันก็เป็นคนเดินหน้าทุกเรื่องระหว่างเราเป็นคนแรกตลอด เป็นคนเปิดบทสนทนาเป็นคนแรก\nไปหาที่ที่ฮานาโกะอยู่แล้วเสนอว่าจะทำอะไรกันดี แต่ขอแค่วันนี้ที่ฉันจะไม่เป็นคนเริ่มก่อนบ้าง"

# "My hand dives into my pocket once more. This time I quickly navigate to the texting menu before I have a chance to change my mind again."
"ฉันล้วงกระเป๋าอีกรอบ แต่คราวนี้รีบกดไปที่หน้าส่งข้อความก่อนจะทันได้เปลี่ยนใจไปไหนอีก"

# "“Hanako, if you want to talk, I'll be at the park in town for a while.”"
"“ฮานาโกะ ถ้ามีเรื่องจะคุยก็มาหาที่สวนสาธารณะได้นะ จะอยู่อีกสักพักเลย”"

# "Fighting a last measure of doubt, I thumb in my message to Hanako and press the button to send it."
"ฉันตัดใจไม่ลังเลอีกแล้วพิมพ์ข้อความกดส่งหาฮานาโกะไป"

# "And now… I wait. My part in this has been fulfilled; what needs to happen now is for Hanako to make the decision. It would be meaningless for me to drag her here. She needs to decide for herself whether she wants to meet me."
"และ… รอ หน้าที่ของฉันเสร็จสิ้นแล้ว ตอนนี้ก็รอให้ฮานาโกะตัดสินใจ ถ้าจะลากมาเลยก็คงไม่ได้อะไรขึ้นมา เธอต้อง\nเป็นคนตัดสินใจเองว่าจะอยากเจอฉันหรือเปล่า"

stop ambient fadeout 4.0

with shorttimeskip

# "The apple juice from the vending machine tastes awfully bitter as I swill it down. My grip on the can has caused it to dent slightly in the middle."
"น้ำแอปเปิลจากตู้ขายของแบบหยอดเหรียญที่ฉันกระดกอยู่นั้นรสขมปร่า ฉันกำมือแน่นจนตัวกระป๋องบุบไปเล็กน้อย"

# "I shouldn't be this tense, but it's probably inevitable."
"ฉันไม่ควรจะเกร็งขนาดนี้สิ แต่คงช่วยไม่ได้"

# "Hanako is dear to me."
"ฮานาโกะน่ะคือสิ่งสำคัญสำหรับฉัน"

# "What happened in the last couple of days has put a lot of pressure on both of us. The idea of losing all the progress we've made in coming closer to one another, and losing our friendship as a whole, is deeply unsettling."
"เรื่องเมื่อสองสามวันมานี้กดดันเราสองคนมาก แค่คิดว่าเราจะต้องถอยกลับไปหลังจากที่ได้ขยับเข้ามาใกล้ชิดกันแบบนี้\nหรือคิดว่าอาจจะต้องสูญเสียมิตรภาพไปเลยก็ใจคอไม่ดีแล้ว"

# "But even then… I still don't really know how close we are. We may have had sex, but before that, all I knew us to be was friends. Maybe we are more than that, but if so, I never realized it."
"แต่ถึงอย่างนั้น… ฉันก็ไม่รู้ชัดว่าเราสนิทกันขนาดไหน เรามีอะไรกันแล้วก็จริง แต่ก่อนหน้านั้นฉันก็เห็นว่าเราเป็นแค่\nเพื่อนกัน อาจจะเป็นมากกว่านั้น ซึ่งถ้าเป็นจริงก็แปลว่าฉันไม่รู้ตัวเลย"

# "Maybe that's why I feel so uneasy right now. I don't understand Hanako, despite all the time we've spent together. The minutes are ticking by, and I still have no idea whether she'll show up."
"อาจจะเพราะอย่างนั้นตอนนี้ฉันถึงได้ไม่สบายใจเอามาก ๆ ฉันไม่เข้าใจฮานาโกะทั้งที่อยู่ด้วยกันบ่อยขนาดนี้\nเวลาไหลไปเรื่อย ๆ โดยที่ฉันยังไม่รู้ว่าฮานาโกะจะมาหรือเปล่า"

# ha "H… Hisao…?"
ha "ฮะ… ฮิซาโอะ…?"

# "I pause for a moment, almost not believing that I'm hearing the voice I am hearing. I drop the can and stand up with a start."
"ฉันชะงักไปแวบหนึ่งด้วยไม่อยากเชื่อหูตัวเองว่าได้ยินเสียงนั้นจริง ๆ ฉันทิ้งกระป๋องแล้วผุดลุกขึ้นทันที"

show hanako basic_worry_cas at center
with charaenter

# hi "Hanako…"
hi "ฮานาโกะ…"

show hanako emb_downtimid_cas
with charachange

# "We look at each other for a few seconds, before Hanako becomes too embarrassed to maintain eye contact and begins to nervously fiddle with the roughly-cut lock of hair covering the side of her face."
"เรามองหน้ากันอยู่สองสามวินาทีจนฮานาโกะเป็นฝ่ายหลบไปก่อนด้วยความอายแล้วจับผมหน้าม้าที่ตัดหยาบ ๆ\nซึ่งปรกอยู่นั้นเล่น"

# "When I went to see Hanako in her room by myself after her breakdown, I had no idea what to say. That was fine, then. All either of us wanted was each other's presence."
"ตอนที่ฉันไปหาฮานาโกะด้วยตัวเองที่ห้องหลังจากที่เธอแพนิกกำเริบแล้วฉันก็ไม่รู้จะพูดอะไร ซึ่งตอนนั้นก็ไม่ต้อง\nใช้คำพูดใด ๆ สิ่งที่เราต่างต้องการมีเพียงตัวตนของกันและกันเท่านั้น"

# "Now, though… I feel like I need to talk to her directly. I want to break down this wall between us, before it forces us apart for good."
"แต่ตอนนี้… ฉันรู้สึกว่าต้องคุยกับฮานาโกะตรง ๆ ฉันอยากจะพังกำแพงที่กั้นระหว่างเราลงก่อนที่กำแพงนี้จะกีด\nเราสองคนออกจากกันไปตลอดกาล"

stop music fadeout 4.0

# hi "Hanako… I…"
hi "ฮานาโกะ… ฉัน…"

# hi "What we did that night… how should I interpret that?"
hi "เรื่องเมื่อคืนนั้น… ฉันต้องคิดว่ายังไง"

show hanako cover_worry_cas
with charachange

# "Hanako stops playing with her hair and looks at me, her head cast slightly downwards. She looks ashamed, which is probably a good mirror of how I would look now if I weren't so concerned."
"ฮานาโกะเลิกจับผมเล่นแล้วมองฉัน เธอก้มหน้าลงเล็กน้อยด้วยสีหน้าละอายใจ ซึ่งฉันก็คงจะทำสีหน้าแบบนั้นด้วย\nเช่นกัน ถ้าไม่ติดว่าฉันเป็นเป็นกังวลขนาดนี้"

show hanako basic_worry_cas
with charachange

play music music_innocence fadein 4.0

# ha "I thought… you might eventually go away if I was only someone you needed to protect."
ha "ฉันคิด… ว่าสักวันนายก็คงจากไป ถ้าฉันเป็นแค่คนที่นายอยากปกป้อง"

show hanako emb_sad_cas
with charachange

# ha "I thought that if I let you do that… you might see me as someone more than that."
ha "ฉันคิด ว่าถ้าฉันยอมให้นายทำแบบนั้น… นายอาจจะมองว่าฉันเป็นอะไรมากกว่านั้น"

# "My first reaction is disbelief, but… I did do it with her, after all. I had plenty of opportunities where I could have stopped things, stepped back, and questioned what we were doing. In the end, though… I didn't."
"สิ่งแรกที่ฉันรู้สึกได้คือความเหลือเชื่อ แต่… ฉันก็ทำอย่างนั้นกับเธอนี่นะ ฉันจะหยุดยั้งตอนไหนก็ได้ ถอยออกมา\nตอนไหนก็ได้ ตั้งคำถามต่อสิ่งที่เราทำกันอยู่ตอนไหนก็ได้ ทว่าสุดท้าย… ฉันก็ไม่หยุด ไม่ถอย ไม่ตั้งคำถาม"

# "A horrible feeling rises in the pit of my stomach. She offered herself to me because of what she thought I wanted, and now, it feels like I took advantage of her. She may have been willing, but only under false premises."
"ท้องไส้ฉันปั่นป่วนด้วยความรู้สึกไม่ดี ฮานาโกะเสนอตัวให้ฉันเพราะคิดว่าคงเป็นสิ่งที่ฉันต้องการ และตอนนี้ฉันก็รู้สึก\nเหมือนตัวเองเอาเปรียบเธอไปแล้ว เธอเต็มใจก็จริง แต่เต็มใจด้วยความคิดที่ผิดทางเท่านั้น"

# "I've never been good at hiding my emotions from physically showing, and now is no different. Hanako looks down once more, a strange mixture of depression, regret, and sickness written to her face."
"ฉันปกปิดอารมณ์ไม่ให้ส่งผ่านออกมาทางใบหน้าหรือร่างกายไม่เก่งอยู่แล้ว ตอนนี้ก็เช่นกัน ฮานาโกะก้มหน้าอีกครั้ง\nสีหน้าเธอระคนด้วยความเศร้า ความเสียใจ กับความแขยงอยู่อย่างประหลาด"

# "Thick silence hangs in the air, save for the breeze blowing through the trees around us."
"ความเงียบอันน่าอึดอัดอวลในอากาศที่มีเพียงลมพัดผ่านต้นไม้รอบตัวเราเท่านั้น"

show hanako emb_downsad_cas
with charachange

# ha "I knew… you couldn't look at me that way…"
ha "ฉันรู้… ว่านายคงมองฉันแบบนั้นไม่ได้…"

# "Hanako's words are said in little more than a whisper, seemingly directed just as much at herself as to me."
"คำพูดของฮานาโกะนั้นแทบจะกลายเป็นเสียงกระซิบอยู่แล้วราวกับว่าพูดกับตัวเองไปด้วย"

# hi "In what way? What do you mean?"
hi "แบบไหน หมายความว่ายังไง"

# ha "All I ever was to you was… a useless person. Just someone… to protect. Someone like… a child."
ha "นายก็มองฉันเป็นแค่… คนไร้ประโยชน์ แค่คน… ที่ต้องปกป้อง คนที่เหมือน… เด็ก ๆ"

show hanako cover_distant_cas
with charachange

# ha "I-I wanted to be more to you than that, but after so long… I… got used to it."
ha "ฉะ-ฉันอยากให้นายมองฉันเป็นมากกว่านั้น แต่นานไป… ฉัน… ก็ชิน"

# "The tone of her voice is unlike any I've heard her use before. She sounds disgusted. Not at me, but at herself."
"น้ำเสียงฮานาโกะตอนนี้เป็นน้ำเสียงที่ฉันไม่เคยได้ยินมาก่อน เป็นน้ำเสียงที่ฟังดูสะอิดสะเอียน แต่ไม่ได้รังเกียจฉัน\nเธอรังเกียจตัวเอง"

show hanako cover_worry_cas
with charachange

# ha "After I came out of my room… I saw that you had started drifting away."
ha "หลังจากที่ฉันออกห้องตัวเองมาแล้ว… ฉันก็เห็นว่านายเริ่มตีตัวออกหากไป"

show hanako basic_worry_cas
with charachange

# ha "I felt like I was going to lose you, because… you wanted somebody you could have… that kind of relationship with."
ha "ฉันรู้สึกเหมือนจะเสียนายไป เพราะ… นายอยากได้ใครสักคน… ที่จะมีความสัมพันธ์แบบนั้นด้วยได้"

show hanako emb_downtimid_cas
with charachange

# ha "You were more quiet in school than before, and you were getting on so well with Yuuko… I thought… that I might lose you."
ha "ตอนอยู่ที่โรงเรียนนายก็เงียบไปกว่าปกติ และก็เข้ากันได้ดีกับยูโกะด้วย… ฉันคิด… ว่าฉันอาจจะเสียนายไป"

# "She thought I was bored of her, because I wanted a romantic relationship?"
"คิดว่าฉันเบื่อเธอเพราะฉันต้องการความสัมพันธ์ฉันคนรักงั้นเหรอ"

# hi "But… we're friends, right? I wouldn't just abandon you like that, even if what you're saying was true."
hi "แต่… เราเป็นเพื่อนกันนี่ ซึ่งต่อให้สมมติว่าเป็นอย่างที่เธอว่าจริงฉันก็คงไม่ทิ้งเธอไปอย่างนั้นหรอก"

show hanako emb_timid_cas
with charachange

# ha "Friendship… was something I thought I'd given up on. I stopped believing in others… after what happened after the accident…"
ha "เพื่อน… เป็นอะไรที่ฉันล้มเลิกความคิดที่จะมีไปแล้ว ฉันไม่เชื่อใจใครอีก… หลังจากอุบัติเหตุครั้งนั้น…"

show hanako emb_downsad_cas
with charachange

# ha "Before the accident happened, I got on well with people and other children. I didn't have many friends… but I didn't mind, because I treasured the ones that I had."
ha "ก่อนเกิดอุบัติเหตุครั้งนั้นฉันเข้ากันได้ดีกับทุกคน เข้ากันได้ดีกับเด็กคนอื่น ฉันมีเพื่อนไม่เยอะ… แต่ก็ไม่ถือ\nเพราะฉันก็ให้ค่าเพื่อนทุกคนที่ฉันมี"

show hanako emb_sad_cas
with charachange

# ha "Afterwards, though…"
ha "แต่หลังจากนั้น…"

show hanako emb_downsad_cas
with charachange

# ha "I was called names by the others, and teased a lot. It hurt… really deeply. The teachers tried to help, but they couldn't do much, and even many of them recoiled just at the sight of me."
ha "ทุกคนก็ล้อฉัน โดนแกล้งหลายครั้ง เจ็บ… มากเลยละ พวกครูพยายามช่วยแล้วแต่ก็ช่วยได้ไม่มาก ครูหลายคน\nแค่เห็นฉันก็ผงะไปด้วยซ้ำ"

# ha "Among those calling me names and teasing me… were the ones that I thought were my closest friends."
ha "แล้วคนที่ล้อฉันแกล้งฉัน… ในนั้นมีคนที่ฉันเคยคิดว่าเป็นเพื่อนสนิทด้วย"

show hanako cover_worry_cas
with charachange

# ha "From then on, I believed that it didn't matter if nobody else acknowledged me. All my existence ever did was make people troubled, after all. It was… easier… if I just didn't exist."
ha "จากนั้นมาฉันก็เชื่อว่าปล่อยให้ทุกคนเมินฉันไปเลยก็ไม่เป็นไรหรอก ก็ตัวตนของฉันมีแต่ทำให้คนอื่นต้องยุ่งยาก\nลำบากใจ คงจะ… ดีกว่านี้… ถ้าฉันหายไปเลย"

show hanako cover_bashful_cas
with charachange

# ha "But after meeting Lilly, and then you…"
ha "แต่พอได้มาเจอลิลลี่ แล้วก็นาย…"

show hanako basic_normal_cas
with charachange

# ha "I tried, but I… couldn't make myself think that way again."
ha "ฉันพยายามแล้ว แต่ฉัน… ฝืนตัวเองให้คิดแบบนั้นไม่ได้อีกเลย"

# "All that time… she didn't trust me. She thought, just like everyone else in her life had, that she was worthless. Someone to throw away once I got bored of being with her."
"ที่ผ่านมา… ฮานาโกะไม่เชื่อใจฉันเลย เธอมองตัวเองเหมือนอย่างที่คนอื่นในชีวิตเคยมองเธอ มองว่าไร้ค่า\nมองว่าเป็นคนที่ถ้าเบื่อแล้วก็ทิ้งไปได้"

# "That hurts. That's the one kind of person I never, ever wanted to be seen as, because I know better than most just how horrible it feels to be thrown away by those who I thought liked me."
"เจ็บ เป็นมุมมองที่ฉันไม่อยากไปตกเป็นเป้าเลย ไม่เลย เพราะฉันเข้าใจดีกว่าใครหลายคนว่าการถูกคนที่คิดว่า\nชอบตัวเองนั้นทิ้งรู้สึกแย่แค่ไหน"

# "She's cracking from the memories she's bringing up. I feel useless, completely unable to console her. In a strange way, though, I am almost thankful that she's allowing me to know this."
"ฮานาโกะเริ่มรับไม่ไหวกับความทรงจำที่เธอกำลังย้องระลึก รู้สึกว่าตัวเองไร้ประโยชน์มากที่ปลอบใจเธอไม่ได้เลย\nแต่ฉันก็ยินดีอย่างประหลาดที่เธอยอมให้ฉันได้รู้เรื่องนี้"

# "The wall between us is going away, even if it hurts so badly to bring it down."
"กำแพงระหว่างเราเริ่มทลายลง แม้การทำลายกำแพงนั้นจะทำให้ต้องเจ็บปวดมากก็ตามที"

# hi "Hanako, if you'd just told me…"
hi "ฮานาโกะ ถ้าเธอบอกฉัน…"

show hanako cover_worry_cas
with charachange

# ha "Was I… wrong?"
ha "ฉัน… คิดผิดเหรอ"

# hi "Of course you…"
hi "ก็แน่อยู่…"

# "She wasn't. Hanako wasn't wrong. It's difficult to force myself to admit this, but I know trying to deny it is pointless. To me, and to Lilly, she was someone we tried to protect."
"ไม่สิ ฮานาโกะไม่ได้คิดผิด ถึงจะทำใจยอมรับได้ยากแค่ไหน แต่ฉันรู้ว่าปฏิเสธไปก็ไม่ได้อะไรขึ้นมา ทั้งฉันทั้งลิลลี่\nต่างมองว่าฮานาโกะคือคนที่เราต้องคอยปกป้อง"

# "She had become to me what I'd become to my friends after my heart attack - a broken person. I liked her, possibly even loved her, but I never acted on that precisely because I thought she was so fragile."
"เรามองฮานาโกะเหมือนอย่างที่เพื่อนมองฉันตอนหลังจากเหตุการณ์หัวใจวายครั้งนั้น มองว่าเป็นคนที่แหลกสลาย\nฉันชอบเธอ หรืออาจจะรักเธอด้วยซ้ำ แต่ที่ฉันไม่ยอมเดินหน้าต่อก็เพราะฉันมองว่าฮานาโกะเปราะบางมากนั่นแหละ"

# hi "I mean… I don't look at you that way now."
hi "คือ… ตอนนี้ฉันไม่ได้มองเธอแบบนั้นแล้ว"

# hi "I got worried about you after what happened to you in class, and I thought I should try to protect you."
hi "พอเกิดเหตุการณ์ในห้องเรียนวันนั้นแล้วฉันก็เป็นห่วงเธอ คิดว่าฉันต้องคอยปกป้องเธอ"

# hi "When you locked yourself in your room, though, I got afraid. I thought you were rejecting me, and it forced me to think a lot about… different things."
hi "แต่ตอนที่เธอขังตัวเองไว้ในห้องฉันก็กลัวขึ้นมา ฉันคิดว่าเธอปฏิเสธฉันอยู่ จนฉันต้องกลับมาคิดทบทวน…\nอะไรหลายอย่าง"

show hanako defarms_strain_cas
with charachange

# ha "I wasn't rejecting you!"
ha "ฉันไม่ได้จะปฏิเสธนายนะ!"

# "She blurts it out with an almost scared tone to her voice, taking me off guard. She quickly becomes embarrassed by her outburst, before clenching her fists and working through what she wants to say in her mind."
"ฮานาโกะโพล่งขึ้นมาด้วยน้ำเสียงที่ยังสั่นกลัวจนฉันตกใจ เธออายทันทีที่อยู่ ๆ ก็ทำตัวแบบนั้นก่อนจะกำหมัด\nพลางคิดอยู่ในหัวถึงสิ่งที่อยากจะพูด"

show hanako emb_timid_cas
with charachange

# ha "I wouldn't ever do that. Not to you."
ha "ฉันไม่มีวันทำแบบนั้นหรอก ฉันไม่มีวันปฏิเสธนาย"

show hanako emb_downtimid_cas
with charachange

# ha "Even though I was scared… even though I tried to push you away… you still tried to get closer to me."
ha "ทั้งที่ฉันกลัวมาก… ทั้งที่ฉันพยายามจะผลักไสนาย… นายก็ยังจะมาเข้าใกล้ชิดฉัน"

# ha "I locked myself away because… I was just a burden to you. To Lilly. To everyone."
ha "ฉันขังตัวเองเพราะ… ฉันเป็นภาระกับนาย กับลิลลี่ กับทุกคน"

show hanako emb_sad_cas
with charachange

# ha "E-every birthday was the same. Everyone doing their best to pretend that I mattered. Everyone pretending everything was all right… for that one day of the year."
ha "วะ-วันเกิดครั้งไหนก็เหมือน ๆ เดิม ทุกคนแสร้งสุดความสามารถทำเหมือนว่าฉันสำคัญ ทุกคนทำเหมือนว่า\nทุกอย่างปกติดี… แค่วันนั้นวันเดียว"

show hanako emb_downsad_cas
with charachange

# ha "I didn't want to exist, but they wouldn't let me. Even after meeting Lilly… everything was the same. I was as useless as I'd always been, unable to do anything for her, or for myself."
ha "ฉันอยากจะหายไป แต่ทุกคนก็ไม่ยอม หลังจากที่ได้เจอลิลลี่แล้ว… ทุกอย่างก็ยังเหมือนเดิม ฉันยังไร้ประโยชน์\nเหมือนเก่า ทำอะไรเพื่อลิลลี่หรือเพื่อตัวเองไม่ได้เลย"

# ha "I didn't want to be the same way… to you."
ha "ฉันไม่อยากเป็นแบบนั้น… กับนายอีก"

# "Lilly and I were completely wrong. From what she's said, everything we did for her… it would have only made her feel worse. Even what little I thought I had right about her was a complete misjudgment."
"ลิลลี่กับฉันคิดผิดมหันต์ เท่าที่ฟังฮานาโกะเล่ามา ทุกอย่างที่เราทำไป… มีแต่จะทำให้เธอรู้สึกแย่ แม้แต่เรื่องของเธอ\nเล็ก ๆ น้อย ๆ ที่ฉันคิดว่าคิดถูกแล้วก็ยังตัดสินไปผิดมากโข"

# hi "After you locked yourself in your room, I decided to try to work out my past as well, and sort out my future. I didn't know how to deal with the things I'd lost by coming to Yamaku, so I was trying to sort them out myself."
hi "หลังจากที่เธอขังตัวเองไว้ในห้องแล้วฉันก็มาจัดการกับอดีตของตัวเองแล้วก็คิดเรื่องอนาคตด้วย ฉันไม่รู้ว่าจะต้อง\nรับมือกับสิ่งที่ฉันเสียไปก่อนมาเรียนที่ยามากุยังไง ฉันเลยจะลองใช้สมองตัวเองคิด"

# hi "I thought… it would help us become better friends… if I did that."
hi "ฉันคิด… ว่าเราคงจะเป็นเพื่อนที่ดีต่อกันได้… ถ้าฉันทำแบบนั้น"

hide hanako
with charaexit

# "Silence hangs in the air again. I try to keep looking at her, but I can't. I feel really low, and though I want to apologize… I don't know how I possibly could."
"มีเพียงความเงียบอยู่ในอากาศอีกครั้ง ฉันพยายามจะสบตามองฮานาโกะแต่ก็ทำไม่ได้ รู้สึกว่าตัวเองต่ำต้อยเหลือเกิน\nอยากจะขอโทษ… แต่ก็ไม่รู้จะขอโทษยังไง"

# "I hear her take a deep breath, and only look back to her after hearing her drop to the ground."
"ฉันได้ยินเสียงสูดหายใจลึก และเมื่อได้ยินเสียงฮานาโกะผลุบตัวลงนั่งกับพื้นฉันก็หันไปมอง"

scene ev hanako_park_alone
with whiteout

# "The sound of her crying breaks my heart. I know I'm responsible for this, and I know that I can't do anything to help her. If Hanako feels ashamed, then I feel all the more so."
"เสียงร้องไห้ของเธอทำใจฉันสลาย ฉันรู้ว่าฉันมีส่วนผิด และรู้ว่าฉันคงช่วยเธอไม่ได้ ถ้าฮานาโกะละอายใจ\nฉันก็ละอายใจหนักขึ้นไปอีก"

show ev hanako_park_away
with charachange

# "I rush to her as tears continue to roll down her cheeks unabated, wrapping my arms around her. I don't care about how I must look any more. I just want to be close to her right now."
"ฉันเข้าไปหาฮานาโกะที่น้ำตาไหลอาบแก้มไม่ขาดสายแล้วโอบเธอไว้ ฉันไม่สนใจแล้วว่าสภาพตัวเองจะเป็นอย่างไร\nตอนนี้ฉันเพียงอยากอยู่ใกล้เธอ"

# ha "I'm sorry, Hisao… I-I've messed up everything…"
ha "ขอโทษนะฮิซาโอะ… ฉะ-ฉันทำพลาดทุกอย่างเลย…"

# hi "It's fine. Everything's fine. I'm the one that should be sorry. I was meddling around behind your back, and I never told you anything."
hi "ไม่เป็นไรหรอก ไม่มีอะไรผิดพลาดเลย ฉันต่างหากที่ต้องขอโทษที่เอาแต่ทำอะไรลับหลังเธอโดยที่ไม่บอกเธอเลย"

# "I can feel my grip tightening on Hanako as my vision blurs. I can't be bothered trying to hold back, now. I have to force my words out as a lump begins to stick in my throat."
"ภาพตรงหน้าฉันเริ่มพร่ามัว ฉันกอดฮานาโกะให้แน่นขึ้น ฉันไม่มีแก่ใจจะมากลั้นอะไรแล้ว ฉันต้องฝืนพูด\nผ่านก้อนสะอื้นที่จุกคอออกมา"

# hi "To tell you the truth, Hanako… I was scared. For the first time since my heart attack, I was really scared."
hi "ว่าตามตรงนะฮานาโกะ… ตอนนั้นฉันกลัว เป็นครั้งแรกที่ฉันกลัวมาก ๆ เลยนับจากที่หัวใจวายครั้งนั้น"

show ev hanako_park_look
with charachange

# ha "Hisao…?"
ha "ฮิซาโอะ…?"

# hi "I lost so much when I came to Yamaku. I was… depending on you, more than I ever thought I did."
hi "ตอนมายามากุฉันต้องสูญเสียอะไรไปหลายอย่าง ฉัน… พึ่งเธอมากกว่าที่ฉันคิดเสียอีก"

# hi "Even now, I still have that hole inside me. After losing my entire life, and everyone I'd known, the thought of losing you, as well…"
hi "แม้แต่ตอนนี้ในใจฉันก็ยังมีรูโหว่อยู่ ฉันต้องสูญเสียชีวิต สูญเสียทุกคนที่เคยรู้จัก แล้วพอคิดว่าจะต้องเสียเธอ\nไปอีก…"

show ev hanako_park_away
with charachange

# ha "But I'm just a useless—"
ha "แต่ฉันมันไร้—"

# hi "You're my friend, Hanako! You're…"
hi "เธอเป็นเพื่อนฉันนะฮานาโกะ! เธอเป็น…"

# hi "No, you're more than that. I love you, Hanako. I love you so much, that the thought of losing you frightened me so much…"
hi "ไม่สิ เธอเป็นมากกว่านั้น ฉันรักเธอนะฮานาโกะ ฉันรักเธอมาก มากเสียจนพอคิดว่าจะต้องเสียเธอไปแล้ว\nฉันก็กลัวเหลือเกิน"

# "Ah, this is bad… I'm really letting all of this out. I can't bring myself to look at her face right now."
"อา แย่แล้วไง… ฉันปลดปล่อยทุกอย่างออกมาหมดเลย ตอนนี้ฉันไม่กล้ามองหน้าฮานาโกะแล้ว"

show ev hanako_park_look
with charachange

# ha "I'm sorry, Hisao…"
ha "ขอโทษนะฮิซาโอะ…"

# ha "I can't help… feeling a bit happy. For so long… that's what I've wanted… to hear…"
ha "ฉันอด… ดีใจไม่ได้เลย ฉันอยาก… ได้ยินคำนี้… มาตั้งนานแล้ว"

show ev hanako_park_closed
with charachange

# "The last of the floodgates breaks, the sound of her crying permeating the air as her body jerks against mine. We hold each other tightly, connected more closely than ever in our shared grief, and our shared happiness."
"ไม่มีสิ่งใดมาปิดกั้นอีกต่อไป เธอร้องไห้โฮพร้อมกับสะอื้นตัวโยนอยู่ในอ้อมกอดฉัน เราโอบกอดกันแน่นและเชื่อมต่อถึงกัน\nด้วยความโศกเศร้าและสุขสันต์ที่เรามีร่วมกัน"

# "I don't know how things are going to be like, after this. Right now, though… I don't care. There's no other person in the world that either of us could possibly share these memories and emotions with. Nobody."
"ฉันไม่รู้ว่าวันข้างหน้านับจากนี้จะเป็นอย่างไรต่อ แต่ตอนนี้… ฉันไม่สนใจแล้ว เราคงแบ่งปันความทรงจำกับอารมณ์เหล่านี้\nกับใครคนอื่นบนโลกใบนี้ไม่ได้อีก ไม่มีเลย"

stop music fadeout 2.0

scene bg suburb_park
with shorttimeskipsilent

play ambient sfx_parkambience fadein 2.0
play sound sfx_can_clatter

# "After dropping the dirtied can into a bin next to the bench, I take a seat beside Hanako. She puts away the handkerchief I gave her to clean herself up, which hasn't helped much."
"พอทิ้งกระป๋องสกปรกนั้นลงถังขยะข้างม้านั่งแล้วฉันก็นั่งข้างฮานาโกะ เธอเก็บผ้าเช็ดหน้าที่ฉันให้เธอไป\nซึ่งก็ช่วยซับน้ำตาได้ไม่ค่อยหมดจดเท่าไหร่"

# "Then again, I doubt I look much more presentable. Even now, I feel emptied and a bit embarrassed after letting my emotions out in public like that. It's not a bad sensation, though. I think Hanako feels the same way, too."
"แต่ก็นะ ฉันเองก็คงดูไม่ได้พอกัน ตอนนี้ยังรู้สึกโล่ง ๆ อาย ๆ ที่ปล่อยให้อารมณ์ตัวเองทะลักออกมากลางที่สาธารณะ\nอย่างนั้น แต่ก็ไม่ได้รู้สึกแย่ ฮานาโกะก็น่าจะคิดเหมือนกัน"

# hi "Have you calmed down a bit?"
hi "สงบลงบ้างหรือยัง"

play music music_comfort fadein 4.0

show hanako cover_bashful_cas_close:
    tworight
    ypos 1.1
with charaenter

# ha "Y-yes. Thank you."
ha "อะ-อื้ม ขอบคุณนะ"

# "For a while, we just sit and take our time before talking again to one another. We both need a little time to collect ourselves."
"เรานั่งกันอยู่เฉย ๆ พักหนึ่งก่อนที่จะเริ่มคุยกันอีก เราต่างต้องการเวลาให้ตั้งสติกันสักเล็กน้อย"

show hanako basic_smile_cas_close
with charachange

# ha "The weather is nice at this time of year."
ha "ช่วงเดือนนี้อากาศดีเนอะ"

# hi "Yeah, it is."
hi "อื้ม นั่นสิ"

show black
with shuteye 

# "I close my eyes for a moment, relishing the feeling of the sun's heat and the cool breeze against my face. The weather really is nice, today. Really, really nice."
"ฉันหลับตาอยู่ครู่หนึ่งคอยกำซาบความร้อนจากแสงแดดและลมเย็น ๆ ที่ตีหน้า วันนี้อากาศดีจริง ๆ ดีมาก ๆ เลย"

# hi "You know… I don't really want to go back to classes, right now. Do you?"
hi "แล้วก็นะ… ฉันยังไม่อยากกลับไปเรียนตอนนี้เลย เธออยากไหม"

hide black
show hanako basic_bashful_cas_close
with openeye

# "She shakes her head as she finishes wiping her eyes with her cuff. The small smile she gives is nice, and it's a reminder of how earnest it can be."
"ฮานาโกะสั่นหัวไปพลางใช้ปลายแขนเสื้อเช็ดตาตัวเอง รอยยิ้มเล็ก ๆ ของเธอนั้นชวนมอง และพอเห็นฉันก็คิดได้ว่า\nช่างเป็นรอยยิ้มที่จริงใจเหลือเกิน"

# "Smiling for other people might be a completely normal, everyday thing. For Hanako though… she smiles so rarely and so sincerely, that each and every time she does it, I feel a sense of relief and happiness."
"คนอื่นอาจมองว่าการยิ้มเป็นเรื่องธรรมดาสามัญประจำวัน แต่กับฮานาโกะแล้ว… เธอยิ้มน้อยครั้งมากและยิ้ม\nอย่างจริงใจมากเสียจนทุกครั้งที่เธอยิ้มแล้วฉันจะรู้สึกสบายใจและสุขใจ"

show hanako cover_worry_cas_close
with charachange

# ha "I'm sorry. For… everything."
ha "ขอโทษ… ทุกเรื่องเลยนะ"

# hi "It's okay. I think we both have a bit to be sorry for."
hi "ไม่เป็นไรน่า ฉันว่าเราต่างก็มีเรื่องที่ต้องขอโทษกันทั้งนั้นแหละ"

show hanako emb_timid_cas_close
with charachange

# ha "I know that… I'm too shy. I know you don't want me to be, I don't think I can…"
ha "ฉันรู้ว่า… ฉันขี้อายเกินไป ฉันรู้ว่านายอยากให้ฉันเลิกขี้อาย แต่ฉันคงเลิกไม่ได้…"

# hi "You can change, Hanako. I know that because, even in the time I've known you, you've already changed. To be honest, just being able to sit here and talk to you like this means that you've changed a lot since we first met."
hi "เธอเปลี่ยนแปลงตัวเองได้น่าฮานาโกะ ที่ฉันรู้เพราะเธอก็เปลี่ยนไปเหมือนกันเท่าที่ฉันได้รู้จักเธอมา เอาตรง ๆ นะ\nแค่ได้มานั่งคุยกับเธอแบบนี้ก็แปลว่าเธอเปลี่ยนไปแล้วนับตั้งแต่ครั้งแรกที่เราเจอกัน"

show hanako emb_downtimid_cas_close
with charachange

# ha "But… I can't be like that for… anyone else. I don't have any plans for after school ends, either…"
ha "แต่… ฉันทำแบบนี้… กับคนอื่นไม่ได้นี่นา เลิกเรียนแล้วฉันก็ไม่ได้มีแผนจะทำอะไรด้วย…"

# "Hanako's confidence begins to slide down again, but I think that now, I can finally talk to her as an equal. I can do it because I know that we're just the same in so many ways."
"ความมั่นใจของฮานาโกะเริ่มถดถอยไปอีกแล้ว แต่ตอนนี้ฉันก็คุยกับเธอตามปกติได้แล้วสักที ที่ฉันคุยได้ก็เพราะ\nเราต่างเหมือนกันในหลาย ๆ แง่"

# hi "Just give yourself time, and I think you'll be able to achieve what you want. No, I'm sure that you'll be able to do it. I can see you've been trying, and I have faith in you."
hi "ไม่ต้องรีบหรอก ฉันว่าสักวันเธอจะทำได้ดังใจต้องการแน่นอน ไม่สิ ฉันมั่นใจเลยแหละ ฉันดูออกว่าเธอพยายามอยู่\nและฉันเองก็เชื่อมั่นในตัวเธอด้วย"

# hi "And you can depend on me if you feel like you need someone to support you, you know."
hi "แล้วก็เนี่ย ถ้าตอนไหนอยากให้ใครสักคนมาเป็นแรงผลักดันให้ก็มาพึ่งฉันได้"

show hanako defarms_strain_cas_close
with charachange

# ha "B-but I can't ask that of you…"
ha "ตะ-แต่จะให้ไปรบกวนนายได้ยังไง…"

# hi "You can, because that's exactly what I'm asking of you. I'm going through the same thing, you know."
hi "ได้สิ เพราะฉันก็จะรบกวนเธอด้วยเหมือนกัน ฉันเองก็ต้องเผชิญกับปัญหาเหมือน ๆ กันนี่นา"

# hi "It's called love."
hi "นี่ละที่เขาเรียกว่ารัก"

show hanako basic_bashful_cas_close at tworight
with dissolvecharamove

# "Hanako smiles, before I get off the bench and dust myself off. She does the same in short measure."
"ฮานาโกะยิ้มก่อนฉันจะลุกจากม้านั่งแล้วปัด ๆ ฝุ่นตามตัว จากนั้นเธอก็ลุกตาม"

# hi "I'm kinda hungry. Want to grab something to eat?"
hi "ชักหิวแล้วสิ ไปหาอะไรกินกันไหม"

# "She nods vigorously. The way she's smiling, the way she's acting, even just the general air she gives off… I feel as if this is the first time I've seen her genuinely happy."
"ฮานาโกะพยักหน้าแรง ๆ รอยยิ้มของเธอ กิริยาของเธอ แม้แต่บรรยากาศรอบตัวเธอ… ราวกับว่าครั้งนี้เป็นครั้งแรกเลย\nที่ได้เห็นเธอมีความสุขจากใจจริง"

$ renpy.music.set_volume(0.6, 1.0, channel="ambient")

scene bg suburb_roadcenter
with locationchange

# "We both make our way onto the street, walking beside each other."
"เราสองคนเดินเคียงข้างกันไปตามถนน"

show hanako emb_emb_cas_close at center
with charaenter

# ha "Hisao?"
ha "ฮิซาโอะ?"

# hi "Yeah?"
hi "หืม"

show hanako emb_downtimid_cas_close
with charachange

# ha "I… I think… I don't really understand you."
ha "ฉัน… ฉันว่า… ฉันไม่ค่อยเข้าใจนายเท่าไหร่"

# hi "I don't think I understand you, either. I believe that's fine, though."
hi "ฉันก็ว่าฉันไม่ค่อยเข้าใจเธอเท่าไหร่เหมือนกัน แต่ฉันเชื่อนะว่าต่อให้ไม่เข้าใจก็ไม่เป็นไรหรอก"

# "There's not a single hint of despair in our voices. Not understanding each other is only natural; the walls we set up between ourselves couldn't possibly be broken down in a single day."
"น้ำเสียงเราไม่มีความสิ้นหวังเจืออยู่เลย เราจะไม่เข้าใจกันก็ไม่แปลก กำแพงที่เราสองคนตั้งมาคั่นกลางกันนั้น\nไม่อาจทุบให้พังราบลงได้ภายในวันเดียว"

# "But that's fine. As long as we take it day by day, and try to understand one another… I think everything will be okay."
"แต่ไม่เป็นไรหรอก ตราบใดที่เราคอยทำความเข้าใจกันและกันไปทุก ๆ วัน… ทุกอย่างจะลงเอยด้วยดี"

show hanako emb_timid_cas_close
with charachange

show hanako emb_downtimid_cas_close
with charachange

# "As we walk down the street, though, Hanako's eyes flick to my face and back to the street repeatedly."
"ทว่าเมื่อเดินกันไปตามถนนเรื่อย ๆ ตาฮานาโกะก็เหลือบมองฉันสลับกับพื้นถนนเรื่อย ๆ"

# hi "Is something on your mind? You look restless."
hi "มีอะไรหรือเปล่า เธอดูลนลานนะ"

show hanako basic_normal_cas_close
with charachange

# "She slows before stopping completely. When I turn to meet her, she takes a long, deep breath, looking at my face intently. This expression… I saw it once before on her face. Just once, when I accidentally surprised her in her room."
"ฮานาโกะผ่อนฝีเท้าลงก่อนจะหยุดเดิน เมื่อหันไปมองเธอก็สูดหายใจลึก ๆ แล้วจ้องหน้าฉันเขม็ง ฉัน… เคยเห็นสีหน้านี้\nมาก่อน แต่แค่ครั้งเดียว ครั้งนั้นที่ฉันเผลอทำเธอตกใจตอนเธออยู่ในห้องตัวเอง"

# ha "I… I think… I think I have something… I need to give you."
ha "ฉัน… ฉันว่า… ฉันว่าฉันมีอะไร… ที่ต้องให้นาย"

# hi "What is it? You don't need to be evasive about it."
hi "อะไรเหรอ ไม่ต้องอ้อมไปอ้อมมาหรอกน่า"

show hanako cover_distant_cas_close
with charachange

# ha "I wanted to give you this for a long, long time, but… now that I need to… it's too embarrassing…"
ha "ฉันอยากให้เจ้านี่กับนายมานานมากแล้ว แต่… พอตอนนี้จะให้… ก็อาย…"

# hi "Don't worry. I'll accept it, whatever it is."
hi "ไม่ต้องห่วงน่า จะเป็นอะไรฉันก็รับไว้หมดแหละ"

show hanako basic_bashful_cas_close
with charachange

# "She gives a sweet, bashful smile, before taking my shoulder in her hand."
"ฮานาโกะยิ้มหวานดูขวยเขินก่อนจะวางมือไว้กับบ่าฉัน"

# ha "Then, please accept my first gift to you, Hisao…"
ha "งั้น ได้โปรดรับของขวัญชิ้นแรกจากฉันทีนะฮิซาโอะ…"

# hi "Hanako…?"
hi "ฮานาโกะ…?"

stop ambient fadeout 1.0

window hide
scene unlock_ev hanako_goodend_close
show unlock_ev hanako_goodend_muffin
show unlock_ev hanako_goodend

show ev hanako_goodend_close:
    xalign 0.0 yalign 0.0
    zoom 1.0 subpixel True
    linear 6.5 zoom 0.8
with whiteout

$ renpy.pause(4.0, hard=True)

play sound sfx_whiteout

scene ev hanako_goodend:
    xalign 0.0 yalign 0.0
    zoom 1.0 subpixel True
    parallel:
        easein 12.0 zoom 0.8
    parallel:
        6.0
        "ev hanako_goodend_muffin" with Dissolve(2.0)
with locationchange

$ renpy.pause(12.0, hard=True)

$ renpy.music.set_volume(1.0, 2.0, channel="ambient")
stop music fadeout 4.0

return