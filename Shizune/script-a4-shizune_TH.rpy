label th_S30:

window hide None

scene bg school_library
with locationchange

window show

play music music_happiness fadein 2.0

# "Only a day later, the weekend has already arrived. I drop a heavy stack of books on the librarian's desk, not meaning to slam them, but they weigh so much that it happens anyway."
"ผ่านไปหนึ่งวันก็เป็นวันสุดสัปดาห์แล้ว ฉันวางหนังสือกองใหญ่ไว้กับโต๊ะบรรณารักษ์โดยไม่ได้จงใจกระแทก แต่น้ำหนัก\nของหนังสือก็ทำให้เกิดเสียงดังอยู่ดี"

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_impact

show yuuko panic_up:
    center
    ypos 1.2 alpha 0.0
    easein 0.25 ypos 1.0 alpha 1.0
with vpunch

show yuuko panic_up:
    center
    alpha 1.0
with None

# "Yuuko bolts out of her chair with enough force to dislodge her glasses. She barely holds on to them."
"ยูโกะพุ่งตัวออกมาจากเก้าอี้อย่างรวดเร็วเสียจนแว่นเบี้ยว เธอจับ ๆ แว่นไว้ไม่ให้หลุด"

show yuuko neutral_up
with charachange

# yu "Oh, hi."
yu "อ้าว ไง"

# hi "Sorry. I'm here to return all those books I was supposed to."
hi "ขอโทษครับ ผมมาคืนหนังสือพวกนั้นตามกำหนด"

show yuuko worried_down
with charachange

# yu "That's great, but I wish you had brought them back sooner. It wouldn't be a problem if the library had more copies of everything, but it doesn't… and they act like that's my fault."
yu "ดีแล้ว แต่เอามาคืนเร็วหน่อยก็ดีนะ ถ้าห้องสมุดมีหนังสือทุกเรื่องหลาย ๆ เล่มหน่อยก็ไม่มีปัญหาอะไรหรอก\nแต่มันไม่ใช่อย่างนั้นน่ะสิ… แล้วพวกนั้นก็ทำเหมือนเป็นความผิดฉันด้วย"

# hi "“They?”"
hi "“พวกนั้น”?"

show yuuko panic_down
with charachange

# yu "Other students. They can be… um, pretty pushy."
yu "นักเรียนคนอื่นน่ะ บางคนก็… เอ่อ ตื๊อมาก"

# hi "Sorry. It just kind of slipped my mind. It's been a pretty rough couple of days."
hi "ขอโทษครับ พอดีผมลืมน่ะ ช่วงสองสามวันมานี้มีอะไรหลายอย่างเลย"

show yuuko worried_down
with charachange

# yu "Oh… Um, I suppose you don't want to talk about it…"
yu "เอ้อ… เอ่อ เธอคงไม่อยากเล่าสินะ…"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

# n "\n\nYuuko meekly turns to the task of logging all the books I've brought back as returned, treating them with extreme care and precision, like she's a bomb disposal technician rather than a librarian."
n "\n\nยูโกะหันไปเช็กอินหนังสือที่ฉันเอามาคืนอาย ๆ ด้วยความทะนุถนอมอย่างยิ่งยวดเหมือนไม่ใช่บรรณารักษ์\nแต่เป็นหน่วยเก็บกู้วัตถุระเบิด"

# n "Over the past couple of days, I've been thinking about something Misha said. Of course, I'd thought about everything she said, but one thing in particular keeps coming back. She talked about how she didn't want to miss people or think about being apart from them any more."
n "สองสามวันมานี้ฉันเอาแต่นึกทบทวนถึงสิ่งที่มิช่าพูด แน่ละว่าฉันคิดถึงทุกคำพูดของมิช่า แต่มีคำพูดหนึ่งที่ฉันยัง\nคาใจอยู่ ที่เธอบอกว่าไม่อยากให้คนหายไปจากชีวิตและไม่อยากต้องแยกจากใครอีก"

# n "When I recalled those words, they stopped me cold, like a sharp slap across the cheek. In just a few months, we'll be graduating. Misha and Shizune were nearly inseparable, but after graduation, they might never see each other again. I wonder if that thought is what started all of this."
n "พอนึกถึงคำนั้นแล้วฉันก็ต้องสะอึกเหมือนโดนตบหน้าหนึ่งฉาด อีีกไม่กี่เดือนเราก็จะเรียนจบแล้ว มิช่ากับชิซูเนะ\nตัวติดกันยิ่งกว่าอะไรดี แต่พอเรียนจบแล้วทั้งสองคนอาจไม่ได้เจอกันอีกเลยก็ได้ หรือเพราะรู้ว่าจะเป็นอย่างนั้น\nถึงต้องทำแบบนี้"

# n "If Misha were to try and talk to Shizune about it, Shizune likely wouldn't think about it at all. It would sadden her, and for that reason, she would try and toss it away. For someone like Shizune, who is so quick to suppress her worries, it would be easy."
n "ถ้ามิช่าเอาเรื่องนี้ไปคุยกับชิซูเนะแล้วชิซูเนะก็คงไม่ได้คิดอะไรแล้วปัดความคิดนั้นทิ้งไปเพราะจะทำให้หมอง ซึ่งก็ไม่ยาก\nสำหรับคนอย่างชิซูเนะที่กลบความกังวลในใจได้อย่างรวดเร็ว"

nvl clear

# n "\n\nMisha turned out to be more sensitive than she seemed. It would have crushed her, even more so because Shizune's reaction could come off as pretty cold. I don't know if that's how Shizune handled it, but it seems likely, and I can understand why she would act that way."
n "\n\nกลายเป็นว่ามิช่านั้นอ่อนไหวกว่าที่เห็น เรื่องนี้คงทำให้มิช่าใจสลาย และจะยิ่งสลายหนักไปอีกด้วยปฏิกิริยาของชิซูเนะ\nที่ดูเย็นชา ฉันไม่รู้ว่าชิซูเนะจะตอบกลับแบบนั้นหรือเปล่า แต่ก็เป็นไปได้ว่าจะเป็นอย่างนั้น และเข้าใจด้วยว่าเพราะอะไร"

# n "I can also understand why Misha would be troubled by the thought of drifting away from someone who is such an important part of her. I'd never thought about graduation until that moment."
n "และเข้าใจด้วยว่าทำไมมิช่าถึงคิดมากกับการที่ต้องแยกทางกันจากคนที่เป็นส่วนสำคัญของเธอ ก่อนหน้านั้น\nฉันไม่เคยคิดเรื่องเรียนจบเลย"

# n "Then I began to think things like, “Has it really only been less than a year?” I started thinking of everyone I've met. Not only Shizune and Misha, but everyone else. They were fond thoughts. Then, I thought of losing them. Suddenly, I could understand Misha's anxieties."
n "แล้วฉันก็ไพล่คิดต่อว่า “ยังผ่านไปไม่ถึงปีเหรอ” ฉันนึกถึงคนทุกคนที่เคยเจอกัน ไม่ใช่แค่ชิซูเนะกับมิช่า แต่คิดถึง\nทุกคนเลย เป็นความคิดอันอบอุ่น แล้วฉันก็คิดว่าต้องเสียทุกคนไป ทันใดนั้นเองฉันก็เข้าใจถึงความกังวลของมิช่า"

# n "\nIt could be nice to talk to someone about it."
n "ถ้าได้เอาไปคุยกับใครสักคนคงดี"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear
window show

# hi "Actually, I kind of want to."
hi "จริง ๆ ก็อยากเล่าอยู่นะครับ"

show yuuko worried_up
with charachange

# yu "With whom?"
yu "กับใครล่ะ"

# "I can sense an obvious tinge of apprehension in her voice."
"ฉันสัมผัสได้ถึงความหวาดหวั่นที่เจืออยู่ในน้ำเสียง"

# hi "With you."
hi "กับคุณยูโกะ"

show yuuko neurotic_up
with charachange

# yu "Ah… Really? Are you sure? W-why me?"
yu "เอ่อ… จริงเหรอ แน่ใจนะ ทะ ทำไมเป็นฉันล่ะ"

# hi "Because you're an adult."
hi "เพราะคุณเป็นผู้ใหญ่"

show yuuko neurotic_down
with charachange

# yu "That's it? Ahhhh… that's…"
yu "แค่นั้นเหรอ เอ่ออออ… คือ…"

# "Wincing, she fidgets a little in her seat, trying to get comfortable in a pretty uncomfortable-looking way. I guess this means she's okay with it."
"ยูโกะทำหน้าเจื่อนแล้วบิดตัวปรับมุมให้เข้าที่ซึ่งดูเหมือนจะไม่เข้าที่อยู่กับที่นั่ง น่าจะแปลว่าพร้อมรับฟังละนะ"

# hi "Is it hard, being an adult?"
hi "การเป็นผู้ใหญ่นี่ลำบากมั้ยครับ"

show yuuko cry_down
with charachange

# yu "Yes."
yu "ลำบาก"

show yuuko panic_down
with charachange

# yu "I don't think I'm that old, though… It's surprising that students now, l-like Shizune and you, wear stuff like perfumes or cologne… I never did. I still don't use them…"
yu "แต่ฉันว่าตัวเองก็ไม่ได้แก่ขนาดนั้นนะ… ฉันแปลกใจจริง ๆ ที่เดี๋ยวนี้นักเรียนอย่าง ชะ ชิซูเนะหรือเธอใส่น้ำหงน้ำหอม\nหรือโคโลญอะไรแบบนี้… ฉันไม่เคยใส่เลยแม้แต่ครั้งเดียว…"

show yuuko worried_up
with charachange

# yu "Um, by the way, you're not wearing your grape cologne today."
yu "เอ่อ จะว่าไป วันนี้เธอไม่ได้ใส่โคโลญกลิ่นองุ่นมานี่นา"

# hi "Yeah, it wasn't working out for me."
hi "ครับ พอดีรู้สึกว่าไม่เหมาะน่ะ"

show yuuko worried_down
with charachange

# yu "Oh, that's good. I thought the same thing… Sorry."
yu "อ้อ ดีแล้ว ฉันก็ว่างั้นแหละ… ขอโทษที"

# "Yuuko looks genuinely sorry, and I feel a pang of guilt. I smile, despite myself. A tiny lie like that can come back to bite me in the butt."
"ยูโกะดูรู้สึกผิดจริง ๆ จนฉันพลอยรู้สึกผิดไปด้วย ฉันยิ้มออกมาไม่รู้ตัว โกหกอะไรเล็ก ๆ น้อย ๆ แบบนั้นไปยังมาแว้งกัด\nกันได้นะ"

# "For Misha, trying to conceal how she felt in order to put on a happy face for Shizune for so long must have been crushing."
"มิช่าคงเหนื่อยน่าดูที่ต้องอำพรางความรู้สึกตัวเองเพื่อจะได้ยิ้มแย้มให้ชิซูเนะมานานขนาดนี้"

# hi "Someone I know brought up that we're going to be graduating, and I realized that I've never thought about it before."
hi "คนรู้จักผมคนหนึ่งมาบอกว่าเราจะเรียนจบแล้วนะ ผมเลยนึกได้ว่าก่อนหน้านั้นผมไม่เคยคิดเรื่องนี้เลย"

# hi "I feel stupid that I could go so long and never think about these things. I've met a lot of great people, and I've never thought about what it's going to be like to graduate and maybe never see them again."
hi "ผมรู้สึกตัวเองโง่ที่อยู่มานานขนาดนี้โดยไม่คิดเรื่องพวกนั้นเลย เจอคนดี ๆ หลายคน แต่ไม่เคยคิดเลยว่าหลังจาก\nเรียนจบแล้วต้องหายหน้าหายตากันไปแล้วจะเป็นยังไง"

show yuuko neutral_down
with charachange

# yu "There are still ways you could keep in touch…"
yu "เรียนจบแล้วก็ยังติดต่อกันได้นี่…"

# hi "Yeah, I guess. I feel childish. I know everyone is going through the same thing, probably. I bet you hear this kind of problem a lot."
hi "ก็คงงั้นมั้งครับ รู้สึกเหมือนตัวเองงอแงเป็นเด็กเลย ผมรู้แหละว่าทุกคนก็คงคิดแบบนี้กันทั้งนั้น คุณคงต้องมานั่งฟัง\nอะไรแบบนี้บ่อยน่าดู"

show yuuko worried_down
with charachange

# yu "N-no… I haven't been working here that long…"
yu "มะ ไม่นะ… ฉันไม่ได้ทำงานที่นี่มานานขนาดนั้น…"

show yuuko worried_up
with charachange

# yu "I worried about the same thing when I graduated from high school. Um, I didn't go to school here, though. I also miss my friends… and I wish I had kept in touch with them better. I should have tried harder."
yu "ตอนฉันเรียนจบมัธยมฉันก็กลัวแบบนั้นเหมือนกัน เอ่อ แต่ฉันไม่ได้เรียนที่นี่นะ ฉันก็คิดถึงเพื่อนเหมือนกัน…\nถ้าติดต่อกันให้มากกว่านี้ก็คงดี ฉันน่าจะพยายามให้มากกว่านี้"

# "Yuuko isn't really helping me feel better, and she clams up quickly when she sees it on my face."
"ยูโกะไม่ได้ช่วยให้ฉันรู้สึกดีขึ้นเท่าไหร่ ซึ่งเธอก็สงบตัวเองลงได้เมื่อเห็นสีหน้าฉันที่บอกแบบนั้น"

# hi "I don't want to look back and have those same regrets."
hi "ผมไม่อยากมองย้อนกลับไปแล้วมานั่งเสียใจแบบนั้นน่ะครับ"

# hi "I wonder if Shizune even thinks about that kind of stuff. Because she goes on sometimes, about how she doesn't want to live with any regrets."
hi "ผมไม่รู้ว่าชิซูเนะจะคิดเรื่องพวกนั้นด้วยซ้ำหรือเปล่า เพราะก็เจ้าตัวก็เคยเล่าเป็นบางครั้งเหมือนกันว่าอยากใช้ชีวิต\nแบบที่ไม่ต้องเสียใจทีหลัง"

show yuuko panic_up
with charachange

# yu "Wow… That sounds impossible, to me…"
yu "โห… ฉันว่า… ฟังดูเป็นไปไม่ได้เลยนะ"

# "I nod, only halfway wanting to agree."
"ฉันพยักหน้ากึ่ง ๆ เห็นด้วย"

show yuuko closedhappy_up
with charachange

# yu "Even so… I think that is kind of admirable, too… Kind of brave. Don't you think so?"
yu "แต่ถึงอย่างนั้น… ฉันว่าก็น่านับถือเหมือนกันนะ… เป็นคนกล้าหาญ เธอว่างั้นมั้ย"

# hi "“Brave” is a new way to put it."
hi "ได้มองมุมใหม่เลยนะครับเนี่ย ที่บอกว่า “กล้าหาญ” น่ะ"

show yuuko neutral_down
with charachange

# "Yuuko shakes her head insistently."
"ยูโกะสั่นหัวยืนกราน"

# yu "It's true, though. And also kind of intimidating…"
yu "แต่จริงนะ แล้วก็น่าเกรงขามด้วย…"

# hi "Geez. You shouldn't be intimidated by high schoolers."
hi "โห่ คนอย่างคุณไม่ต้องกลัวเด็กมัธยมหรอกครับ"

show yuuko worried_up
with charachange

# yu "I'll try…"
yu "จะพยายามนะ…"

hide yuuko
with charaexit

# "She turns away to start folding a sticky note over and over. Pretty idle behavior for a university student, but more importantly, I wonder if I said the wrong thing to her."
"ยูโกะหันไปพับโพสต์อิตซ้ำแล้วซ้ำเล่า เด็กมหาวิทยาลัยเขาทำอะไรแบบนี้แก้มือว่างกันสินะ แต่ที่สำคัญกว่านั้นคือฉัน\nอยากรู้ว่าไปพูดอะไรสะกิดใจเข้าหรือเปล่า"

# "Being around Shizune for so long, I can't stop reading as much as I can into every moment of silence."
"พออยู่กับชิซูเนะนานเข้าฉันก็อดไม่ได้ที่จะตีความทุกอย่างทุกครั้งที่คนเงียบไป"

# "If Yuuko were the type of person who didn't get intimidated by high schoolers, it probably wouldn't be so easy to talk to her."
"ถ้ายูโกะเป็นคนที่ไม่กลัวเด็กมัธยมแล้วฉันก็คงมาคุยสบาย ๆ แบบนี้ไม่ได้หรอก"

# "It's all too easy to want to shed some negative quality of yours. When I think of everyone I know, it's those qualities that I like the best."
"คนเราต่างก็อยากขจัดคุณสมบัติด้านลบของตัวเองกันทั้งนั้น แต่พอนึกถึงทุกคนที่ฉันรู้จักแล้วกลับเห็นว่าเป็น\nคุณสมบัติเหล่านั้นเองที่ฉันชอบที่สุด"

show yuuko worried_up at center
with charaenter

# yu "Um…"
yu "เอ่อ…"

show yuuko smile_down
with charachange

# yu "I don't think I really regret it. I thought, as long as I could remember the good times, that was enough."
yu "แต่ฉันว่าฉันไม่ได้เสียใจอะไรขนาดนั้นหรอก ตราบใดที่ยังนึกถึงวันเวลาดี ๆ ได้ แค่นั้นก็พอแล้วละ"

show yuuko worried_down
with charachange

# yu "I don't know. …Sorry."
yu "ไม่รู้สิ …ขอโทษที"

# "I notice a couple students starting to trickle into the library, and decide that my time is up."
"ฉันเห็นนักเรียนสองสามคนทยอยเข้าห้องสมุดมา พอแค่นี้ก่อนแล้วกัน"

# hi "No, that was helpful."
hi "ไม่หรอกครับ ช่วยได้เยอะเลย"

# hi "I feel like two of my friends are fighting because one of them is taking the fact that we might not see each other again after we graduate really hard. And the other is probably being stoic about it, which only makes it worse."
hi "ผมรู้สึกเหมือนเพื่อนทะเลาะกันเพราะเพื่อนคนหนึ่งคิดมากว่าหลังเรียนจบแล้วจะไม่ได้เจอกันอีก ส่วนอีกคนก็\nเหมือนจะไม่เดือดร้อนอะไร เรื่องเลยยิ่งแย่ไปใหญ่"

# hi "I don't get how I'm supposed to handle this kind of situation. It doesn't seem like the kind of problem where I'll have to end up taking a side, but it could turn out that way, and then I have no idea what I'm going to do."
hi "ผมไม่รู้ว่าจะต้องรับมือกับสถานการณ์แบบนี้ยังไง ถึงจะดูเหมือนว่าเป็นเรื่องที่ผมไม่ต้องเลือกข้าง แต่สุดท้ายสักวัน\nก็อาจต้องเลือกอยู่ดี ซึ่งถ้าเป็นอย่างนั้นจริงผมก็ไม่รู้ต้องทำตัวยังไง"

show yuuko neutral_down
with charachange

# yu "You should tell them they shouldn't fight."
yu "บอกไปสิว่าอย่าทะเลาะกัน"

# hi "I know. Fighting is bad."
hi "รู้น่าครับ ทะเลาะกันมันไม่ดี"

# hi "It's not Shizune and Misha, by the way."
hi "แล้วก็ไม่ได้พูดถึงชิซูเนะกับมิช่านะครับ"

show yuuko worried_up
with charachange

# yu "Okay… Um, I wasn't really thinking that, though…"
yu "โอเค… เอ่อ แต่ฉันไม่ได้คิดแบบนั้นเลยนะ"

# "How embarrassing. Even though I knew it would be, I still feel my cheeks redden, and even so, I still said something so transparent and blatantly a lie. But it could be that sometimes that is the right way."
"น่าอายชะมัด รู้อยู่ว่าน่าอายแต่ก็ยังหน้าแดง แถมโกหกทนโท่อะไรแบบนั้นไปหน้าตาเฉย แต่บางทีก็คงต้องเลือกพูด\nอย่างนี้แหละ"

# hi "Do you have any books about people who have to make hard decisions?"
hi "พอจะมีหนังสือเกี่ยวกับคนที่ต้องเลือกอะไรที่น่าหนักใจมั้ยครับ"

show yuuko happy_down
with charachange

# yu "We have a lot of self-help books…"
yu "ที่นี่มีหนังสือพัฒนาตนเองเยอะแยะเลย…"

# "It's funny that I can find that surprising, because I wouldn't have only a few months ago."
"ตลกดีที่ฉันแปลกใจ เพราะสองสามเดือนก่อนฉันก็คงไม่รู้สึกแปลกอะไร"

# hi "I meant “about,” not “for.” There aren't many, right?"
hi "ผมถามว่า “เกี่ยวกับ” ไม่ใช่ “สำหรับ” นะครับ คงไม่มีไม่เยอะใช่มั้ย"

show yuuko worried_down
with charachange

# yu "Yes. Um, not many, I mean."
yu "อื้ม เอ่อ หมายถึง มีไม่เยอะ"

stop music fadeout 3.0

# "Though I feel a bit apprehensive about it, I want to talk to Shizune. I don't understand why I feel nervous about it, and that disgusts me a little."
"ถึงในใจจะยังวิตกอยู่ แต่ฉันก็ยังอยากคุยกับชิซูเนะ ไม่เข้าใจเลยว่าทำไมถึงประหม่าจนนึกแขยงขึ้นมา"

scene bg school_council
with locationskip

# "It also motivates me to look for her, right then and there, although I don't have to look very hard. She's in the student council room, as always."
"ซึ่งก็ทำให้ฉันอยากตามหาตัวเธอด้วยแบบปัจจุบันทันที ถึงไม่ต้องลงแรงมากก็เถอะ เพราะอยู่ที่ห้องสภานักเรียนอย่าง\nเคยน่ะแหละ"

play music music_pearly fadein 5.0

show shizu behind_blank at center
with charaenter

# "Worryingly, Misha isn't with her. When Shizune notices me and looks up from her paperwork, the first thing I ask is where she is."
"พอเห็นมิช่าอยู่ด้วยแล้วฉันก็ใจเสีย สิ่งแรกที่ฉันทำหลังจากชิซูเนะเห็นฉันแล้วละสายตาจากเอกสารคือการถาม\nว่ามิช่าอยู่ไหน"

show shizu basic_normal2
with charachange

# ssh "I don't know."
ssh "ไม่รู้สิ"

# "There is so much uncertainty in her answer that I can't let it go just like that."
"เป็นคำตอบที่เต็มไปด้วยความลังเลจนฉันปล่อยผ่านไปเฉย ๆ ไม่ได้"

# his "She's missing a lot of school."
his "มิช่าขาดเรียนหลายครั้งแล้วนะ"

show shizu adjust_happy
with charachange

# ssh "Are you the attendance police?"
ssh "นี่นายเป็นตำรวจตรวจการเช็กชื่อหรือยังไง"

# his "That's really strange, coming from the Student Council president."
his "แปลกนะที่คนอย่างประธานนักเรียนพูดอะไรแบบนั้นน่ะ"

show shizu adjust_smug
with charachange

# "Shizune hides a laugh behind a cupped hand, and I start to think that I might be worrying for nothing, but then her laughter slowly fades away to a more serious and pensive expression."
"ชิซูเนะยกมือป้องปากหัวเราะ ฉันคิดไปว่าตัวเองอาจคิดมากไปเอง ทว่ารอยยิ้มนั้นก็จางลงแปรเป็นสีหน้าจริงจังครุ่นคิด"

show shizu basic_normal
with charachange

# ssh "You're right."
ssh "ก็จริง"

show shizu behind_blank
with charachange

# ssh "Yesterday,"
ssh "เมื่อวาน"

show shizu adjust_happy
with charachange

# "I catch the hint of a knowing smile on her face when she sees my poorly-hidden panic at the word. Despite her best efforts, she can't help being satisfied in eliciting surprise from everyone else, to the very end."
"ฉันเห็นรอยยิ้มกรุ้มกริ่มบาง ๆ ของชิซูเนะเมื่อเธอเห็นสีหน้าตื่นตระหนกของฉันที่ปิดไว้ไม่มิดเมื่อได้ยินคำนั้น\nไม่ว่าอย่างไร ถึงจะพยายามขนาดไหนก็อดที่จะรู้สึกพึงใจไม่ได้กับการทำให้คนอื่นตกใจสินะ"

# "Even then, I can see that she has bigger concerns from how quickly her smile vanishes."
"แต่ฉันก็ดูออกอยู่ว่าชิซูเนะมีเรื่องให้ต้องกังวลใจที่หนักกว่าจากการที่รอยยิ้มเธอหายไปอย่างรวดเร็ว"

show shizu basic_angry
with charachange

# ssh "…before either of you noticed me, I saw what you were saying. I'm not stupid."
ssh "…ฉันเห็นนะว่านายพูดอะไรก่อนที่พวกเธอสองคนจะเห็นฉันเสียอีก ฉันไม่ได้โง่นะ"

show shizu behind_frown
with charachange

# ssh "If I hadn't, I could still see through Misha while we were walking back. Even if she hadn't told me everything later. She didn't make a big deal out of it, but any way you look at it, it's my fault, isn't it?"
ssh "หรือต่อให้ฉันไม่เห็น ฉันก็ดูออกจากท่าทางมิช่าตอนเดินกลับด้วยกันอยู่ดี ถึงเจ้าตัวจะไม่ได้เล่าทุกอย่างก็เถอะ\nมิช่าไม่ได้บ่นอะไรก็จริง แต่ดูยังไงก็ความผิดฉันสินะ"

# his "What did she tell you?"
his "มิช่าบอกอะไร"

show shizu adjust_frown
with charachange

# "Shizune winces at the question, though it's clear she's been expecting it. She follows it up with a very grand gesture."
"ชิซูเนะผงะไปกับคำถามนั้น ถึงจะชัดก็เถอะว่าเธอรู้อยู่แล้วว่าฉันจะถาม จากนั้นจึงทำภาษามือแบบกว้าง ๆ"

show shizu basic_normal2
with charachange

# ssh "A lot."
ssh "หลายอย่าง"

show shizu adjust_frown
with charachange

# ssh "Like, that I can be selfish, and confusing. I try too hard to bring people around me, and then push them away."
ssh "เช่นว่าบางทีฉันก็เห็นแก่ตัว เข้าใจยาก ฝืนพาคนอื่นเข้ามาในชีวิตแล้วผลักไสออกไป"

show shizu basic_normal2
with charachange

# ssh "I didn't know what I should do. I thought she was right to mention all of those things, so I just agreed with her, but that only made things worse."
ssh "ฉันไม่รู้ว่าควรทำยังไงดี ฉันคิดว่ามิช่าก็พูดถูกเหมือนกันเลยบอกเห็นด้วยไป แต่ยิ่งทำให้เรื่องไปกันใหญ่"

show shizu behind_sad
with charachange

# ssh "I don't understand."
ssh "ไม่เห็นเข้าใจเลย"

# "Adjusting her glasses, she looks pretty tired. I hope it isn't because she's been busy avoiding Misha, but I can't help considering the possibility, seeing where this conversation is going."
"ชิซูเนะดันแว่นด้วยท่าทีอ่อนล้า หวังว่าจะไม่ใช่เพราะต้องคอยหลบหน้ามิช่าหรอกนะ แต่ก็อดคิดไม่ได้อยู่ดี\nว่าจะเป็นเช่นนั้นจากหลายอย่างที่เธอบอก"

show shizu adjust_smug
with charachange

# ssh "It's true. Even the Student Council being this small, and us always being swamped with work, is my fault. I might have even ended up driving a lot of people off, and away from the Student Council, acting like that."
ssh "ก็จริงแหละว่าทั้งที่สภานักเรียนก็มีกันแค่นี้แต่งานสุมท่วมหัวน่ะเป็นความผิดฉัน แล้วก็น่าจะเพราะฉันทำตัว\nอย่างนั้นคนอื่นถึงกระเจิงไปจากฉันหมด ไปจากสภานักเรียนด้วย"

# "Shizune wags a finger mischievously, acknowledging that “might” is an understatement. However, from how wearily she does it, it's obvious the humor is only to put me at ease, and therefore not genuine."
"ชิซูเนะส่ายนิ้วซุกซนเป็นการรับรู้ว่าการใช้คำว่า “น่าจะ” นั้นยังน้อยไป แต่ดูจากท่าทีที่เหมือนทำผ่าน ๆ อย่างนั้นแล้ว\nเหมือนว่าจะทำให้ดูตลกให้ฉันสบายใจมากกว่า ไม่ได้เป็นอะไรที่มาจากใจจริง"

show shizu basic_normal
with charachange

# ssh "Like Lilly, for instance. She was the first person to join when I started trying to recruit people again after everyone else left, because they couldn't stand me, I guess."
ssh "ยกตัวอย่างเช่นลิลลี่ ลิลลี่เป็นคนแรกที่มาเข้าร่วมสภานักเรียนอีกครั้งหลังจากที่ทุกคนออกไป—น่าจะเพราะ\nอยู่กับฉันไม่ได้ละมั้งนะ—แล้วฉันกำลังตามหาสมาชิกใหม่อยู่"

show shizu adjust_happy
with charachange

# ssh "We managed to put together the last festival, and even ran a booth together at the last minute."
ssh "พวกเราจัดงานเทศกาลครั้งสุดท้ายกันได้ ตั้งแผงด้วยกันเอาวินาทีสุดท้ายอีกต่างหาก"

show shizu behind_frown
with charachange

# ssh "But I didn't like her because I thought she was selfish, always holding us up in order to tend to one friend of hers or another, and leaving Misha and me alone to sort out things involving the whole school by ourselves."
ssh "แต่ฉันไม่ชอบลิลลี่เพราะฉันมองว่าเธอเห็นแก่ตัว เอาแต่รั้งพวกเราเพื่อไปช่วยเพื่อนคนนั้นคนนี้แล้วปล่อยให้มิช่า\nกับฉันจัดการเรื่องงานโรงเรียนกันอยู่สองคน"

show shizu cross_angry
with charachange

# ssh "If there were any problem she was going through, she would leave us high and dry while she panicked over it, and wouldn't come back until it was solved."
ssh "ถ้าเจอปัญหาอะไรก็จะปล่อยให้เราลอยเท้งเต้งกลางทะเลโดยที่ตัวเองมัวแต่ตระหนก จะกลับมาอีกทีก็ตอนที่เรื่อง\nคลี่คลายแล้ว"

show shizu adjust_angry
with charachange

# ssh "She would focus on it one hundred percent, and be too preoccupied to focus on any student council work!"
ssh "จะจดจ่ออยู่กับมันเต็มที่เลย จมอยู่กับมันจนตั้งใจทำงานสภานักเรียนไม่ได้!"

show shizu behind_frustrated
with charachange

# ssh "That was the worst, to me, that she could be so nice and still take so many people for granted. Why even join the Student Council, then? It seemed so shortsighted and selfish, don't you think?"
ssh "ฉันมองว่าแบบนั้นน่ะแย่ที่สุดเลย ที่เป็นคนดีขนาดนั้นแต่กลับไม่คิดถึงคนอื่นให้จริงจัง แล้วจะมาเข้าร่วมสภานักเรียน\nทำไม คิดตื้น ๆ แถมยังเห็นแก่ตัวด้วย นายว่างั้นมั้ยล่ะ"

show shizu basic_normal2
with charachange

# ssh "But, it's actually me who's that way."
ssh "แต่จริง ๆ แล้วฉันต่างหากที่เป็นแบบนั้น"

show shizu adjust_frown
with charachange

# ssh "Like Misha said, always trying to pull people close to me and then shutting them out."
ssh "อย่างที่มิช่าบอกนั่นแหละว่าฉันเอาแต่คอยดึงคนเข้ามาในชีวิตแล้วกีดกันทุกคนออกไป"

show shizu behind_sad
with charachange

# ssh "That is how I've treated her, which makes me a bad friend. And it feels like I did the same thing to you, then, so I guess I'm a bad girlfriend, too, even if Misha says that you might as well replace her."
ssh "ฉันทำแบบนั้นกับมิช่า ซึ่งแปลว่าฉันเป็นเพื่อนที่แย่ แล้วฉันก็รู้สึกเหมือนว่าทำอย่างเดียวกันกับนายด้วย ซึ่ง\nแปลว่าฉันก็คงเป็นแฟนที่แย่เหมือนกัน ถึงมิช่าจะบอกก็เถอะว่าให้นายมาอยู่แทนตัวเองไปเลยก็ได้นะ"

show shizu basic_normal2
with charachange

# ssh "I'm angry that I screwed things up enough for it to get this out of hand. All I wanted was to…"
ssh "ฉันโกรธที่ฉันทำพลาดจนอะไร ๆ มันเละเทะขนาดนี้ ฉันก็แค่อยากจะ…"

stop music fadeout 3.0

# "She pauses to look for the right words, tenting her fingers in concentration."
"ชิซูเนะเว้นจังหวะนึกหาคำที่เหมาะระหว่างที่กางนิ้วชนกันเพื่อตั้งสมาธิ"

show shizu behind_blank
with charachange

# ssh "Make people happy, I think."
ssh "ทำให้ทุกคนมีความสุข มั้งนะ"

show shizu adjust_happy
with charachange

# ssh "Even though that seems like a simple way to put it."
ssh "ฟังดูไม่ซับซ้อนดีเนอะ"

# "As she rests her head against her hand, Shizune's bangs fall delicately across her eyes, hidden behind those polished glasses reflecting just the tiniest bit of light."
"ชิซูเนะเอนหัวยกมือมาแนบหูไว้ หน้าม้าปรกตาเธอ เบื้องหลังแว่นใสนั้นสะท้อนแสงเลือนราง"

# "It may be wrong to think so, but right now, she seems especially beautiful. Like a more complete person."
"ถึงอาจจะไม่ควรคิดแบบนี้ แต่ฉันมองว่าตอนนี้ชิซูเนะดูงดงามเป็นพิเศษ เหมือนเป็นคนที่สมบูรณ์ขึ้น"

# "It feels like this is my first chance to respond to her outpouring of emotions. Replacing Misha as Shizune's interpreter? Misha must be joking."
"ตอนนี้น่าจะเป็นโอกาสแรกที่ฉันจะได้ตอบกลับอารมณ์ของชิซูเนะที่ไหลบ่าออกมา ให้อยู่เป็นล่ามชิซูเนะแทนมิช่าเหรอ\nมิช่าคงพูดเล่นแน่ ๆ"

# "It took all my energy to keep up with her just now, her signing filled with gestures that I've never seen before."
"แค่เมื่อกี้ฉันก็เสียพลังงานไปหมดสิ้นแค่กับการจนอ่านทุกอย่างจากชิซูเนะ มีแต่ท่าที่ฉันไม่เคยเห็นเต็มไปหมด"

# "Likely, they're habits picked up from Misha, and developed from years of them being together. I could never replace someone so close to her."
"คงเป็นนิสัยที่ติดมาจากมิช่าละมั้ง อยู่ด้วยกันมานานหลายปีขนาดนั้น ฉันคงไม่อาจทดแทนคนที่ใกล้ชิดกับชิซูเนะ\nขนาดนั้นได้หรอก"

# his "I like you because I like you, not because I got tricked into it by you."
his "ฉันชอบเธอเพราะเธอเป็นเธอ ไม่ใช่เพราะเธอหลอกฉันให้ชอบ"

# "Despite how hard she tried, anyway. I continue to stare back into her eyes, as sharp as ever. The first time I saw them, they had seemed a bit intimidating to me. Like the eyes of a predator. That hasn't changed, which I find reassuring."
"แต่ก็จริงอยู่ว่าชิซูเนะล่อหลอกฉันหลายรอบน่ะนะ ฉันจ้องสายตาอันเฉียบคบไม่เปลี่ยนแปลงของชิซูเนะนั้นกลับ\nครั้งแรกที่ได้เห็นนั้นฉันกลัวอยู่เล็กน้อย เป็นสายตาที่เหมือนอย่างนักล่า ซึ่งตอนนี้ก็ยังเป็นเช่นเดิม และทำให้ฉันสบายใจ\nขึ้นมา"

show shizu basic_normal
with charachange

# ssh "I still want to make everyone happy."
ssh "แต่ฉันก็ยังอยากให้ทุกคนมีความสุขอยู่ดี"

# his "Starting with Misha?"
his "เริ่มด้วยมิช่าก่อนเหรอ"

play music music_shizune fadein 6.0

show shizu basic_frown
with charachange

# "Shizune looks a bit annoyed that I would imply she would start with anyone else, and smiles confidently, as though a friend's sadness is a physical opponent she can just strangle into submission."
"ชิซูเนะดูหงุดหงิดเล็กน้อยที่ฉันใช้คำพูดเหมือนจะบอกว่าตัวเองจะเริ่มด้วยคนอื่นก่อนจะยิ้มอย่างมั่นใจราวกับ\nความเศร้าของเพื่อนนั้นคือศัตรูที่มีกายเนื้อแล้วรัดคอให้สยบยอมได้"

show shizu behind_frustrated
with charachange

# ssh "Of course; obviously; naturally."
ssh "แหงสิ แน่นอนอยู่แล้ว ต้องเป็นแบบนั้นแหละ"

#see report
show shizu adjust_noglasses
with charachange

# "Taking off her glasses, she leans back in her chair and lets out a sigh. It's the first time I've seen her without them on, but I don't get a good look before she slips them back on."
"ชิซูเนะถอดแว่นเอนตัวพิงพนักเก้าอี้ถอนหายใจ ครั้งแรกเลยที่เห็นชิซูเนะตอนไม่ใส่แว่น แต่ยังไม่ทันได้ดูให้ดีเธอก็กลับ\nไปใส่แว่นแล้ว"

show shizu behind_smile
with charachange

# ssh "But, I'm too tired to start today. First thing tomorrow."
ssh "แต่จะเริ่มวันนี้ก็ไม่ไหว เหนื่อย ค่อยเริ่มพรุ่งนี้แล้วกัน"

show shizu basic_normal
with charachange

# ssh "Do you want to help?"
ssh "นายอยากช่วยมั้ย"

# his "Yeah."
his "อืม"

show shizu adjust_happy
with charachange

# ssh "And… I have other student council stuff you could help me with, while you're at it."
ssh "แล้วก็… ไหน ๆ ก็ไหน ๆ ฉันมีงานสภานักเรียนอย่างอื่นจะให้นายช่วยด้วย"

# "Although it turns out that there isn't much other work at all."
"ถึงงานที่ว่านั้นจริง ๆ จะไม่ได้มีมากก็ตาม"

stop music fadeout 2.0
$ suppress_window_after_timeskip = True

scene black
with dissolve


##############################

label th_S31:

window hide None

scene black
with dissolve

with Pause(2.0)

play sound sfx_doorknock

with Pause(2.0)

scene bg school_dormhisao
with openeye

window show

play sound sfx_doorknock

# "There's no school today, so I expected to be able to sleep in late. Unfortunately, I'm awakened by someone mercilessly pounding on my door at eight in the morning."
"วันนี้ไม่มีเรียน ฉันจึงคาดไว้ว่าคงนอนต่อได้ โชคไม่ดีที่เสียงทุบประตูปึงปังอย่างไร้ปรานีนั้นมาปลุกฉันตอนแปดโมงเช้า"

# "At first, I think it could be Kenji, but when my shouts of annoyance go unanswered, I realize it's Shizune."
"แวบแรกฉันคิดว่าอาจเป็นเคนจิ แต่เมื่อตะโกนตอบกลับด้วยความรำคาญแล้วไม่ได้คำตอบจึงรู้ว่าเป็นชิซูเนะ"

play sound sfx_dooropen

scene bg school_dormhallway
show shizu adjust_happy_close at center
with locationchange

play music music_another fadein 0.5

show shizu behind_blank at center
with charadistant

# "She immediately backs away from the door when I open it, quickly concealing something behind her back. Kind of ominous."
"ชิซูเนะถอยกรูดไปเมื่อฉันเปิดประตูรีบซ่อนอะไรบางอย่างไว้ข้างหลัง รู้สึกไม่ค่อยดีเลยแฮะ"

# his "What's that? Is it a surprise? I don't really like surprises."
his "นั่นอะไร เซอร์ไพรส์เหรอ ฉันไม่ค่อยชอบเซอร์ไพรส์เท่าไหร่นะ"

show shizu behind_frown
with charachange

# "The displeased expression on her face says that she wants me to stop being such a wet blanket, but she's too busy fumbling with what's behind her back to sign it."
"สีหน้าไม่พอใจของชิซูเนะบ่งบอกว่าฉันควรเลิกทำให้คนอื่นหมดสนุกได้แล้ว แต่เธอก็ไม่อาจทำภาษามืออะไรได้ด้วยมือ\nที่ยังถืออะไรไว้ข้างหลังอยู่"

show shizu adjust_smug
with charachange

# "It must be frustrating for her, because seconds later, she swings the object out, proudly, and also a little dangerously."
"คงหงุดหงิดน่าดู เพราะสองสามวินาทีให้หลังชิซูเนะก็ยื่นของที่ว่านั้นออกมาอย่างภาคภูมิจนแทบจะชนหน้าฉันอยู่แล้ว"

show shizu basic_happy
with charachange

#see report
# ssh "Ta-da. A picnic basket. We can have lunch together, the three of us."
ssh "แต่นแต๊น ตะกร้าปิกนิกละ มากินมื้อเที่ยงด้วยกันสามคนดีกว่า"

# "It's not really a basket, it looks more like a plastic bag. Taking a quick look inside, I can see that most of the food inside is also store-bought, not homemade. Some items still have the price stickers on."
"ไม่ใช่ตะกร้าจริง ๆ หรอก เหมือนถุงพลาสติกมากกว่า พอมองแวบหนึ่งก็เห็นว่าของในนั้นส่วนมากก็ซื้อมาจากร้าน\nไม่ใช่ของทำเอง บางอย่างยังมีป้ายราคาติดอยู่เลย"

# "There's a very diverse selection here, though. Even a tiny tin of caviar. I'm slowly becoming more impressed with this lunch. I pick a grape out of there and pop it in my mouth."
"แต่ในนั้นก็มีอะไรหลากหลายดี มีแม้กระทั่งคาเวียร์กระป๋องเล็ก ๆ ด้วย ชักสนใจขึ้นมาแล้วสิ ฉันบิองุ่นมาหนึ่งลูก\nเข้าปากกิน"

show shizu adjust_frown
with charachange

# ssh "Don't just take things like that! I spent all night perfecting this final weapon."
ssh "อย่าหยิบเล่นแบบนั้นสิ! ฉันตัดแต่งอาวุธสุดยอดนี้อยู่ทั้งคืนเลยนะ"

show shizu adjust_frown:
    ease 0.5 ypos 1.2
    ease 0.5 center
with Pause(0.5)

play sound sfx_pillow

show shizu basic_normal:
    ypos 1.2
    ease 0.5 center
with charachange

# "Shizune places it down on the ground to free up her hands, and immediately starts playfully tapping it between her feet like a soccer ball. Definitely not what you should do to anything you're going to call a “final weapon.”"
"ชิซูเนะวางถุงลงกับพื้นให้มือว่างแล้วใช้เท้าเขี่ยเล่นเหมือนลูกฟุตบอลทันที อันนี้ก็น่าจะไม่ใช่อะไรที่ควรทำกับของ\nที่จะมาเรียกว่า “อาวุธสุดยอด” ได้นะ"

show shizu adjust_happy at center
with charachange

# ssh "All part of my “get-Misha-to-stop-being-so-depressed” plan. I stayed up all last night working on it."
ssh "ทุกอย่างคือแผน “ให้มิช่าเลิกซึมเศร้า” ฉันนั่งทำอยู่ทั้งคืนเลยนะ"

show shizu behind_smile
with charachange

# ssh "When we tried to order in last time, Misha barely got anything, and used it as an excuse to leave early. I won't let her get off so easily this time. The food is already here. She'll have to sit down and eat with us."
ssh "คราวที่แล้วตอนจะสั่งอะไรมากินมิช่าก็แทบไม่สั่งอะไรเลยแล้วอ้างหาเรื่องปลีกตัวไปก่อน คราวนี้ไม่ปล่อยไป\nง่าย ๆ แน่ อาหารอยู่ตรงนี้แล้ว ยังไงก็ต้องมานั่งกินด้วยกัน"

show shizu basic_happy
with charachange

# ssh "It's the perfect bait. Doesn't everything look irresistible? I tried to make it myself, but I don't know how to make it look all fancy, so I ended up buying everything. Still looks delicious, doesn't it? It should be."
ssh "นี่แหละกับดักสุดสมบูรณ์แบบ ทุกอย่างดูน่ากินมากเลยใช่มั้ยล่ะ ฉันลองทำเองแล้วแต่ไม่รู้จะทำยังไงให้ดูสวยดี\nก็เลยซื้อทุกอย่างเอา แต่ก็ดูน่าอร่อยใช่มั้ย ควรจะแหละ"

# "She's very perky today, juiced up on the thought of cheering Misha up. Although it's odd to see her so happy about it, I know that she's just as unsure now as she was yesterday."
"วันนี้ชิซูเนะกระตือรือร้นเหลือเกินกับแผนที่จะทำให้มิช่าร่าเริง แต่ก็แปลกที่ดูมีความสุขขนาดนี้ ทั้งที่ก็เหมือนจะยัง\nไม่แน่ใจไม่ต่างจากเมื่อวานเลย"

# "The only thing that has changed is that by viewing it as another sort of challenge for herself, she can put her worries aside and throw herself into it recklessly."
"อย่างเดียวที่เปลี่ยนไปคือชิซูเนะตัดความกังวลไปได้แล้วและทุ่มสุดตัวด้วยการมองว่าสิ่งนี้คือภารกิจอย่างหนึ่งที่จะได้\nท้าทายตัวเอง"

# "It has worked well enough for Shizune so far. It wouldn't surprise me if it's the only way she knows how to live."
"ก็ดูจะเป็นไปได้ด้วยดี ฉันจะไม่แปลกใจเลยถ้าจะบอกว่าชิซูเนะใช้ชีวิตเป็นแค่ด้วยวิธีนี้วิธีเดียว"

# his "It's a little early, though…"
his "แต่จะเช้าไปหน่อยมั้ย…"

show shizu adjust_frown
with charachange

# ssh "It's already eight in the morning, that's late! Even Misha gets up at eight or nine. She goes to bed at 7:00 p.m., but that isn't important."
ssh "แปดโมงเช้าแล้ว สายแล้วนะ! มิช่ายังตื่นตอนแปดเก้าโมง นอนตอนหนึ่งทุ่ม แต่ไม่สำคัญ"

# his "It's very important."
his "อันนั้นน่ะแหละสำคัญมาก"

show shizu basic_normal_close
with characlose

# "Shizune ignores me, gagging my hands by taking them in hers instead of a more proper rebuttal. The way she lingers against me a moment longer than expected feels really comforting."
"ชิซูเนะเมินฉันแล้วปิดปากด้วยการจับมือแทนที่จะแย้งอะไรกลับให้ดีกว่านี้ ฉันอุ่นใจขึ้นมาเมื่อเห็นว่าเธอลังเลไม่กล้าจับ\nอยู่นานกว่าที่คาดไว้"

show shizu adjust_happy_close
with charachange

# ssh "The point is, she's awake right now, walking around somewhere. Let's go find her."
ssh "ประเด็นคือมิช่าตื่นแล้วและออกไปเดินอยู่สักที่ ไปตามหามิช่ากัน"

scene bg school_courtyard at bgleft
with locationskip

# "She sprints out the door impatiently, and her gusto as she drags me along looking for Misha makes me feel more like I'm following a hunter on a safari than looking for a mutual friend."
"ชิซูเนะพุ่งตัวออกจากประตูด้วยความรีบร้อน แรงที่เธอใช้ลากฉันให้ไปตามหามิช่าด้วยทำให้ตัวเองรู้สึกเหมือนว่าไม่ได้\nไปตามหาเพื่อนแต่กำลังติดตามนักล่าที่ท่องป่าชมสัตว์ตามแอฟริกาอยู่"

# "We don't have to look very hard. Even cropped short, her pink hair stands out. The fact that she's just meandering around the grounds out in the open makes it even easier. Now I'm sounding like a safari hunter."
"ซึ่งไม่ต้องหาให้เหนื่อยเลย ผมสีชมพูเธอนั้นเด่นแม้จะตัดแล้ว และยิ่งออกมาเดินตามที่โล่งอย่างนี้ก็เจอตัวง่ายขึ้นไปอีก\nเอาละ นี่ฉันจะกลายเป็นนักล่าแทนแล้ว"

show shizu adjust_happy_close at tworight
with charaenter

shi "…!"

# hi "Misha!"
hi "มิช่า!"

show mishashort hips_smile at twoleft behind shizu
with charaenter

# mi "Huh~?"
mi "หา~?"

# hi "We were just looking for you."
hi "กำลังหาตัวอยู่เลย"

show shizu behind_smile_close
with charachange

# ssh "It's a good day for a picnic, you should join us. We even have caviar; not sturgeon, of course, but really tasty."
ssh "วันนี้วันดี มาปิกนิกกัน เธอก็มาด้วยสิ มีคาเวียร์ด้วยนะ แน่ละว่าไม่ใช่ของปลาสเตอร์เจียน แต่อร่อยมากเลยนะ"

show mishashort perky_confused
with charachange

# mi "Caviar? Surgeon?"
mi "คาเวียร์? สตอเจีย?"

# "Apparently finding it annoying to have to explain anything at length with only one hand, Shizune gives up quickly."
"ดูเหมือนว่าจะรำคาญที่ต้องอธิบายอะไรยาว ๆ ด้วยมือเดียว ชิซูเนะยอมแพ้แล้วตอบสั้น ๆ"

show shizu adjust_frown_close
with charachange

# ssh "Fish eggs."
ssh "ไข่ปลา"

show mishashort sign_confused
with charachange

# mi "What?"
mi "อะไรนะ"

show shizu behind_smile_close
with charachange

# ssh "It tastes good."
ssh "อร่อยนะ"

show mishashort cross_smile
with charachange

# mi "Sorry, Shicchan, I think I'll pass for today."
mi "ขอโทษทีนะชิจัง แต่วันนี้ขอผ่าน"

show shizu basic_angry_close
with charachange

# "When Misha starts to walk away, Shizune holds the bag out towards me, needing me to take it so that her hands can be free."
"พอมิช่าทำท่าจะเดินหนีชิซูเนะก็ยื่นถุงให้ฉันถือแล้วตัวเองจะได้มือว่าง"

hide shizu
with None

show shizu basic_angry_close at tworight behind mishashort
with None

show mishashort cross_smile:
    ease 1.0 center
show bg school_courtyard:
    ease 1.0 center
show shizu basic_angry_close:
    ease 1.0 xpos 0.75
with Pause(0.5)
show shizu behind_blank:
    tworight
    xpos 0.725
    ease 0.5 xpos 0.75
with charadistant

show mishashort perky_confused at Position(xpos=0.35)
show shizu behind_blank at Position(xpos=0.65)
show bg school_courtyard at Position(xpos=0.43)
with dissolvecharamove

# "As soon as it's out of her hands, she darts in front of Misha, cutting her off."
"พอถุงพ้นมือไปแล้วชิซูเนะก็พุ่งตัวไปขวางมิช่าไว้ทันที"

show shizu adjust_happy
with charachange

# ssh "I made so much food, though."
ssh "แต่ฉันทำมาเยอะเลยนะ"

show mishashort perky_sad
with charachange

# mi "Sorry, I'm just not hungry right now."
mi "ขอโทษที ตอนนี้ยังไม่หิว"

show shizu behind_blank
with charachange

shi "…"

show shizu behind_frown
with charachange

# ssh "When are you going to be hungry, then?"
ssh "แล้วเมื่อไหร่จะหิว"

show mishashort hips_frown
with charachange

# mi "Shicchan, that's impossible to know~."
mi "ชิจัง ฉันจะไปรู้ได้ยังไงล่ะ~"

show shizu adjust_frown
with charachange

# ssh "You can guess."
ssh "ก็เดาได้นี่"

# "The tension between them infuriates Shizune, and she's trying to deal with it by trying to tear through it. But that approach isn't going to work."
"ความตึงเครียดระหว่างทั้งสองคนพาให้ชิซูเนะเลือดเดือด เธอกำลังรับมือด้วยการตื๊ออยู่ แต่วิธีแบบนั้นไม่ได้ผลหรอก"

# "I'd thought, and hoped, that Misha had gotten herself together, but I guess she was just cut too deep by what happened."
"ฉันคิดว่า—และหวังว่า—มิช่าคงตั้งสติได้บ้างแล้ว แต่ดูท่าคงจะเจ็บหนักมากกับเรื่องที่เกิดขึ้น"

# "In that case, it's really out of anyone's hands. I believe that Shizune might understand that, on some level. If she didn't, she wouldn't have any doubts at all."
"ถ้าอย่างนั้นไม่ว่าใครก็คงช่วยไม่ได้ ฉันเชื่อว่าชิซูเนะคงเข้าใจอยู่บ้าง เพราะถ้าไม่เข้าใจก็คงไม่ลังเลหรอก"

# "Because she can't speak, though, I've learned to notice her hesitation. It's very clear; she might as well be screaming."
"แต่เพราะเธอพูดไม่ได้นั่นแหละฉันถึงหัดสังเกตเวลาที่เธอลังเล เห็นชัดว่าตอนนี้เธออยากจะกรีดร้องแทบตาย"

show mishashort sign_smile
with charachange

hide mishashort
with charaexit

stop music fadeout 5.0

# "Misha waves her hands in front of her, not wanting to continue the discussion any further, and quickly slips away. Shizune fumes silently, reluctant to let her go but having no way to keep her here."
"มิช่าโบกมือตรงหน้าชิซูเนะด้วยไม่อยากสนทนาต่ออีกแล้วแวบหายไปอย่างรวดเร็ว ชิซูเนะโมโหอยู่เงียบ ๆ เพราะ\nไม่อยากปล่อยมิช่าไป แต่ก็ไม่มีวิธีใดที่จะรั้งได้"

# "As Misha's back grows smaller in the distance, I wonder where she's heading off to. Is Shizune wondering the same thing, as she bites her lip in frustration?"
"แผ่นหลังมิช่าหดเล็กลงเมื่อระยะทิ้งห่างออกไป จะไปไหนกันนะ ชิซูเนะที่ยืนกัดริมฝีปากด้วยความหัวเสียจะสงสัย\nเหมือนกันหรือเปล่า"

# "I want to touch her reassuringly on the shoulder, but I stop myself, not knowing if it's the right thing to do."
"ฉันอยากไปตบบ่าปลอบใจแต่ก็ยั้งตัวเองไว้เพราะไม่รู้ว่าควรทำหรือไม่"

# "Not because she looks fragile, vulnerable, or sad. It's the opposite. After a while, her expression belies no emotion at all. Only contemplation. Suddenly, she whirls around."
"ไม่ใช่เพราะชิซูเนะดูเปราะบาง บอบบาง หรือเศร้าสร้อย กลับกันเลยต่างหาก ผ่านไปสักพักสีหน้าเธอก็ไร้อารมณ์\nเหลือเพียงความครุ่นคิด ทันใดนั้นเองเธอก็หมุนตัวมา"

play music music_dreamy fadein 4.0

show shizu basic_angry at center
show bg school_courtyard at right
with dissolvecharamove

# ssh "Now all this food is going to go to waste."
ssh "แล้วทีนี้อาหารพวกนี้ก็จะเสียเปล่า"

# his "Yeah."
his "อืม"

show shizu behind_sad
with charachange

# ssh "That makes me mad."
ssh "เศร้าจัง"

# "Although it's obvious Shizune is more hurt than mad. The bag dangling from my hand feels like it's filled with lead."
"แต่ก็ชัดแหละนะว่าตอนนี้ชิซูเนะไม่ได้โกรธแต่เจ็บปวดอยู่ ถุงที่ฉันถืออยู่นั้นหนักราวกับว่ามีตะกั่วใส่ไว้"

show shizu behind_blank
with charachange

# $ doublespeak(ssh, his, "Let's go on a date.", "Let's use it, then.")
$ doublespeak(ssh, his, "ไปเดตกันเถอะ", "งั้นก็กินกันเถอะ")

show shizu adjust_blush
with charachange

shi "…"

show shizu basic_normal
with charachange

# ssh "Where do you want to go?"
ssh "นายอยากไปไหน"

# his "I don't know."
his "ไม่รู้สิ"

show shizu behind_blank
with charachange

# ssh "The roof."
ssh "ดาดฟ้า"

show shizu adjust_happy
with charachange

# ssh "It's my favorite spot."
ssh "ที่โปรดฉัน"

# "A wry smile appears on her face, disappearing just as quickly."
"ชิซูเนะยิ้มแห้ง ๆ รอยยิ้มนั้นหายไปอย่างรวดเร็ว"

play ambient sfx_rooftop fadein 1.0

scene bg school_roof
show shizu behind_frown_close at center
with shorttimeskip

# "On the roof, I immediately crack open the caviar, ignoring a derisive look from Shizune all the while. I end up putting it down immediately."
"พอมาถึงดาดฟ้าแล้วฉันก็เปิดกระป๋องคาเวียร์ทันทีโดยไม่ได้สนใจสายตาหยามเหยียดของชิซูเนะ ฉันวางกระป๋องลง\nทันที"

# his "Where are the toast points?"
his "แล้วไหนขนมปังปิ้งสามเหลี่ยมที่จะมากินคู่กัน"

show shizu basic_normal2_close
with charachange

# ssh "I didn't make any. Like I told you, I bought everything."
ssh "ไม่ได้ทำ ก็บอกแล้วไงว่าฉันซื้อมาทุกอย่าง"

# his "Not toast points, though…"
his "แต่ถ้าไม่มีขนมปังปิ้งสามเหลี่ยมมันก็…"

show shizu adjust_frown_close
with charachange

# ssh "Why is that important? Anyway, they don't sell just toast points. That would be stupid."
ssh "แล้วมันสำคัญตรงไหน แต่นั่นแหละ ไม่มีร้านไหนขายขนมปังปิ้งสามเหลี่ยมแบบแยกหรอก เขาคงไม่บ้า\nขนาดนั้น"

# his "I bet they do."
his "ฉันว่ามี"

show shizu behind_blank_close
with charachange

# ssh "Maybe in stores for the exceptionally lazy, but not here. Why don't you use a tortilla chip?"
ssh "ถ้าร้านสำหรับคนที่ขี้เกียจเป็นพิเศษก็อาจจะมี แต่ที่นี่ไม่มี ใช้ตอร์ติยาชิปก็ได้นี่"

# his "A tortilla chip is not the same."
his "ตอร์ติยาชิปมันไม่เหมือนกันกับขนมปังปิ้งสามเหลี่ยมสักหน่อย"

show shizu basic_frown_close
with charachange

# ssh "They're both triangles. Stop being such a princess. I didn't know there was a proper way to eat caviar, this is the first I'm hearing of it."
ssh "ก็เป็นสามเหลี่ยมเหมือนกันแหละน่า เลิกเรื่องมากเป็นเจ้าหญิงได้แล้ว ฉันไม่รู้ว่าคาเวียร์เขากินกันยังไง เพิ่งเคยได้ยิน\nเป็นครั้งแรกเนี่ย"

# his "It's not the same thing at all."
his "มันไม่เหมือนกันเลย"

show shizu adjust_smug_close
with charachange

# "I can't be decadent like this. And anyway, how can she not know? She lives in a huge mansion. Shizune takes the opportunity to scoop half the tin onto a single chip in the meantime."
"ฉันไม่ยอมทำตัวไร้อารยธรรมหรอก แล้วนี่ไม่รู้ได้ยังไง อยู่ในคฤหาสน์หลังใหญ่อย่างนั้น ชิซูเนะอาศัยจังหวะนี้\nใช้ชิปหนึ่งแผ่นคว้านคาเวียร์ไปครึ่งกระป๋อง"

# his "Hey!"
his "นี่!"

# "I'm sure it doesn't even taste good like that."
"ทำแบบนั้นต้องไม่อร่อยแน่ ๆ"

show shizu behind_smile_close
with charachange

shi "…"

# "There is too much food here for two people. Because we can't communicate with each other while we eat, both Shizune and I have a lot of time to sit in silence and think about the fact that Misha, the person she set all this up for, isn't here."
"ของพวกนี้กินกันสองคนไม่หมดหรอก และเพราะเวลากินเราสื่อสารกันไม่ได้ ทั้งชิซูเนะกับฉันจึงมีเวลาเหลือเฟือ\nให้ตระหนักว่ามิช่า—คนที่ชิซูเนะวางแผนเพื่อเอาใจโดยเฉพาะ—ไม่อยู่ตรงนี้"

show shizu basic_angry_close
with charachange

# ssh "It's annoying that she isn't here. I can't even enjoy my meal like this."
ssh "มิช่าไม่อยู่แล้วหงุดหงิด กินไม่อร่อยเลย"

# "I stare at the paper cup next to her, still half-full of juice."
"ฉันจ้องแก้วกระดาษที่วางอยู่ข้างชิซูเนะซึ่งยังมีน้ำผลไม้อยู่ครึ่งหนึ่ง"

# his "I thought you didn't want all this food to go to waste."
his "ไหนบอกว่าไม่อยากให้เสียเปล่าไง"

show shizu adjust_frown_close
with charachange

# ssh "I wanted Misha to be here, too. That was the whole point. I wasn't able to accomplish what I wanted to, so it doesn't taste good."
ssh "ฉันอยากให้มิช่าอยู่ตรงนี้ด้วย นั่นน่ะคือใจความหลัก ฉันทำไม่ได้ตามเป้าที่ตั้งไว้ อาหารเลยไม่อร่อย"

show shizu behind_blank_close
with charachange

# ssh "You should eat it. Eat more."
ssh "นายก็กินสิ กินอีก"

# his "I want the fried things, though. You keep eating them all, even though you say they don't taste good."
his "แต่ฉันอยากกินของทอดอะ เธอก็เอาแต่กินทั้งที่บอกว่าไม่อร่อย"

show shizu basic_normal_close
with charachange

# ssh "Fried things are always delicious. There is always an exception for them."
ssh "ของทอดน่ะอร่อยเสมอ ของทอดคือข้อยกเว้นสำหรับทุกอย่าง"

# his "You'll get fat."
his "เดี๋ยวก็อ้วนหรอก"

# his "I think you're being too aggressive."
his "ฉันว่าเธอรุกหนักไปนะ"

show shizu behind_blank_close
with charachange

# ssh "It's like I told you yesterday, I'm only trying to cheer her up."
ssh "ก็อย่างที่บอกเมื่อวานน่ะแหละว่าฉันแค่อยากให้มิช่าร่าเริงเฉย ๆ"

# his "Yeah, but it seems more like you're planning a military campaign."
his "ก็ใช่ แต่มันดูเหมือนว่าเธอกำลังรณรงค์เรื่องการทหารอยู่น่ะ"

show shizu basic_normal2_close
with charachange

# ssh "I'm only trying to take it seriously."
ssh "ฉันก็แค่จะทำให้มันจริงจัง"

show shizu behind_sad_close
with charachange

# ssh "…And this is the only way I know how to do it seriously."
ssh "…แล้วฉันก็ทำอะไรแบบจริงจังเป็นแค่วิธีนี้ด้วย"

show shizu basic_normal2_close
with charachange

# ssh "I feel so powerless. I hate it. I can't even yell at her, too, even though I want to. Yelling is for serious occasions, right?"
ssh "ฉันรู้สึกว่าตัวเองทำอะไรไม่ได้เลย ไม่ชอบเลย จะตะโกนใส่ก็ไม่ได้ทั้งที่อยากตะโกนมาก การตะโกนเอาไว้ใช้กับ\nเรื่องจริงจังใช่มั้ย"

# his "Yeah."
his "อืม"

show shizu adjust_frown_close
with charachange

# ssh "You should yell at Misha for me. You can tell her that I want her to stop being so down. Even if she feels sad and alone, it's no reason to stay gloomy forever."
ssh "นายน่าจะตะโกนใส่มิช่านะ บอกหน่อยว่าฉันอยากให้เลิกทำตัวหมองสักที ถึงจะทั้งเศร้าทั้งโดดเดี่ยว แต่ก็\nไม่มีเหตุผลอะไรที่จะต้องทำตัวหม่นอย่างนั้นไปตลอด"

# his "Why don't you?"
his "แล้วทำไมเธอไม่ว่าเอง"

show shizu basic_frown_close
with charachange

# ssh "I already did."
ssh "บอกไปแล้ว"

show shizu behind_blank_close
with charachange

# ssh "Over a game of dice."
ssh "ด้วยเกมทอดลูกเต๋า"

show shizu basic_happy_close
with charachange

# ssh "Under-Over, to be exact. I won! Five times!"
ssh "ทายว่าจะออกสูงหรือต่ำ ฉันชนะละ! ชนะห้ารอบ!"

# "Only the two of them would take so much pride in winning games of pure chance."
"คงมีแค่สองคนนี้แหละที่ภูมิใจกับเกมที่ว่ากันด้วยโอกาสล้วน ๆ"

show shizu adjust_frown_close
with charachange

# ssh "Then, I tried to talk to her, but it didn't go so well, obviously."
ssh "แล้วฉันก็ลองคุยกับมิช่า ซึ่งชัดว่าไปได้ไม่สวยเท่าไหร่"

# his "Well, so did I. I tried and failed."
his "ฉันก็เหมือนกันน่ะแหละ ลองแล้วก็ล้มเหลว"

show shizu basic_normal2_close
with charachange

# ssh "My goal has always been to do everything better, though."
ssh "แต่เป้าหมายของฉันคือการทำให้ตัวเองเก่งขึ้นในทุก ๆ ด้าน"

# his "Yeah, your one-upmanship is really something."
his "อืม นิสัยชอบเอาชนะคนอื่นของเธอนี่รุนแรงจริง ๆ"

show shizu behind_frustrated_close
with charachange

# ssh "But I failed too…"
ssh "แต่ฉันก็ยังล้มเหลว…"

show shizu basic_normal2_close
with charachange

# ssh "That's why I want your help."
ssh "ฉันถึงได้อยากให้นายช่วย"

show shizu behind_sad_close
with charachange

# ssh "I don't understand what I'm supposed to do any more."
ssh "ฉันไม่รู้แล้วว่าจะต้องทำยังไง"

# "For someone like Shizune, who has only ever interacted with the world by locking horns with every obstacle in her path, understanding only goes so far."
"สำหรับคนอย่างชิซูเนะที่ใช้ชีวิตอยู่ในโลกนี้ด้วยการพุ่งเข้าชนทุกอุปสรรคที่ขวางทางนั้น ต่อให้รู้ไปก็คงไม่ช่วยอะไร"

$ renpy.music.set_volume(0.5, 2.0, channel="music")
$ renpy.music.set_volume(0.5, 2.0, channel="ambient")

window hide

scene bg misc_sky at Fullpan(30.0)
with locationchange

nvl clear
nvl show dissolve

# n "\n\nI want to tell her that she doesn't have to worry. That she is great at cheering people up, because she managed to cheer me up, my first week here."
n "\n\nฉันอยากบอกชิซูเนะว่าไม่ต้องกังวลไป บอกว่าเธอน่ะเก่งกับการทำให้คนอื่นร่าเริง เพราะชิซูเนะทำให้ฉัน\nร่าเริงขึ้นได้กับการมาอยู่ที่นี่ในสัปดาห์แรก"

# n "In retrospect, I must have looked like kind of a dick, being in such a sour mood from the moment I came here. Even though I don't think I was being unreasonable."
n "พอลองย้อนนึกดูแล้ว ฉันคงจะดูเป็นคนไม่ดีเหมือนกัน เพิ่งมาถึงก็ทำอารมณ์บูดมาแต่ไกล แต่ก็ใช่ว่าฉันจะทำตัว\nไม่มีเหตุผลเลยน่ะนะ"

# n "Even having months to digest it, finding out that you have a heart defect like I did is hard to deal with. I'd had had much less time to mull over suddenly being transferred to Yamaku, on top of that."
n "ถึงจะมีเวลาเป็นเดือน ๆ แต่การจะให้ทำใจว่าหัวใจตัวเองอ่อนแออย่างฉันนั้นก็ไม่ง่าย และซ้ำร้าย ฉันยิ่งมีเวลา\nให้ทำใจว่าจะต้องย้ายมาอยู่โรงเรียนยามากุแบบกะทันหันน้อยกว่านั้นเสียอีก"

# n "\n\nSpending the festival with Shizune really helped me out of a rut. I was happy, enough to forget that the entire time it had felt as though she were manipulating me. I understand now that I had allowed myself to be manipulated."
n "\n\nฉันหลุดมาจากหล่มได้เพราะได้เที่ยวงานเทศกาลกับชิซูเนะ ฉันมีความสุข มีความสุขพอที่จะลืมความรู้สึกว่าชิซูเนะ\nวางแผนล่อหลอกฉัน ตอนนี้ฉันเข้าใจแล้วว่าฉันปล่อยให้ตัวเองถูกล่อหลอกไปแล้ว"

nvl clear

# n "\n\nEven though I felt like I was at the bottom of the world, I still wanted to have a normal life again, I'm sure, because I enjoy what I have now. I think it must be the same for everyone. Including Misha. Everyone wants someone there to pull them up, out of their self-pity."
n "\n\nแม้ฉันจะรู้สึกเหมือนโลกพร้อมดับสูญสิ้น ฉันก็ยังอยากใช้ชีวิตอย่างปกติ ที่ฉันมั่นใจก็เพราะตอนนี้ฉันพอใจกับสิ่งที่\nเป็นอยู่ ทุกคนก็คงเหมือนกัน มิช่าเองก็ด้วย ทุกคนต่างอยากมีใครสักคนที่จะดึงตัวเองให้หลุดพ้นจากความสมเพช\nตัวเอง"

# n "It's just that Misha always wanted Shizune to be that person, but because they can't be together, I think Misha feels that she can't accept Shizune's hand. And that frustrates Shizune. But if she could cheer up a stranger like me, then she'll die trying with Misha."
n "และเพราะมิช่าอยากให้ชิซูเนะเป็นคนนั้นมาตลอด แต่ทั้งสองคนกลับอยู่ด้วยกันไม่ได้ ฉันเลยคิดว่ามิช่า\nคงจะรู้สึกว่าตัวเองไม่อาจคว้ามือชิซูเนะที่ยื่นมาช่วยไว้ได้ ซึ่งทำให้ชิซูเนะหงุดหงิด แต่ถ้าชิซูเนะทำให้คนแปลกหน้าอย่างฉันร่าเริง\nขึ้นได้ เธอก็คงทุ่มชีวิตตัวเองเพื่อจะทำแบบเดียวกันกับมิช่าด้วย"

# n "\nI can see it in her eyes, too. Though she tries to treat it like any other problem in her life, Shizune cannot do that with Misha's depression. Her thought processes are entirely different, in some ways more careful, in some ways more reckless and frenetic. She cares that much more."
n "\nแววตาเธอฉายแววชัดเช่นกัน ทว่าชิซูเนะกลับใช้วิธีเดียวกันกับที่เธอใช้จัดการปัญหาอื่น ๆ ในชีวิต ซึ่งเธอ\nไม่อาจทำอย่างนั้นกับความเศร้าของมิช่าได้ ความคิดความอ่านของเธอนั้นต่างออกไป ในแง่หนึ่งก็รอบคอบ แต่ในอีกแง่\nก็บ้าบิ่นมุทะลุ ชิซูเนะให้ความใส่ใจกับปัญหานี้ถึงเพียงนั้น"

nvl clear

# n "\n\n\n\n\nI end up not saying anything. Partly because sitting next to her like this, just the two of us, is pleasant enough in itself that I don't want to interrupt the moment with a question."
n "\n\n\n\n\nสุดท้ายฉันก็ไม่ได้พูดอะไร ส่วนหนึ่งก็เพราะฉันพอใจแล้วแค่กับการได้นั่งข้างเธออยู่ตามลำพังจนไม่อยาก\nจะขัดจังหวะนี้ด้วยคำถาม"

# n "\n\nAnd partly for a more cowardly reason. I've started to think they weren't, but I don't know if her actions that day might not have been an afterthought, or even a fluke, just a collection of coincidences. I don't know if that would change anything, but I'm uncomfortable thinking about it."
n "\n\nอีกส่วนก็เป็นอะไรที่ฟังดูขี้ขลาด ฉันไม่รู้ว่าการกระทำของเธอในวันนั้นคือความคิดตกค้างหรือเปล่า หรืออาจจะบังเอิญ\nบังเอิญซ้อนบังเอิญ ซึ่งฉันก็เริ่มคิดว่าคงไม่ใช่ ฉันไม่รู้ว่าเหตุการณ์นั้นจะเปลี่ยนแปลงอะไรได้หรือเปล่า แต่แค่นึกถึง\nก็ไม่สบายใจแล้ว"

$ renpy.music.set_volume(1.0, 2.0, channel="music")
$ renpy.music.set_volume(1.0, 2.0, channel="ambient")

nvl hide dissolve
nvl clear

scene bg school_roof
with locationchange

window show

stop music fadeout 5.0

# "The fence behind me trembles slightly, and I turn to see that it's because Shizune has fallen asleep leaning against it. Considering she was up all night, it's not surprising."
"รั้วที่ฉันพิงอยู่สั่นเล็กน้อย พอหันไปมองก็เห็นว่าเป็นเพราะชิซูเนะผล็อยหลับพิงอยู่กับรั้ว ก็ไม่แปลกหรอก ไม่ได้นอน\nทั้งคืนเลยนี่นะ"

# "Where does all that motivation come from? Not just in regards to Misha. I'm cynical, so it's hard for me to just accept that anyone can simply be that strong."
"ไปเอาแรงฮึดขนาดนั้นมาจากไหน ไม่ใช่แค่เรื่องมิช่าด้วย ฉันเป็นคนขวางโลก จึงไม่อาจยอมรับได้ว่าจะมีใครสักคน\nที่เข้มแข็งขนาดนั้นจริง ๆ"

# "My first thought was that maybe it's because she hates herself. It's very plausible."
"ฉันคิดไปก่อนว่าเธอคงจะเกลียดตัวเอง ดูเป็นไปได้มาก ๆ"

# "Leaning against her, I feel sad knowing that that might be the case. But it could be that we're similar in that we both want to be better people."
"พอได้เอนตัวพิงแล้วก็เศร้าขึ้นมาเมื่อคิดว่าคงเป็นเช่นนั้นจริง แต่ก็คงเป็นเพราะเราคล้ายกันตรงที่ว่าเราต่างอยาก\nปรับปรุงตัวให้ดีขึ้น"

stop ambient fadeout 2.0

scene black
with dissolve

$ suppress_window_after_timeskip = True

##################################

label th_S32:

window hide None

scene black
with dissolve

scene bg school_dormhisao
with openeye

window show

play music music_daily fadein 8.0

# "It seems like I ate too much yesterday, because I wake up in the morning feeling just nauseous enough for it to be a problem."
"ดูท่าว่าเมื่อวานคงกินมากไป เพราะเช้านี้ตื่นมาก็คลื่นไส้จนทนไม่ไหว"

# "I really can't postpone going into town for shopping, though. So despite wanting to roll over and sleep it away, I force myself to get up and dress instead."
"แต่จะเลื่อนการเข้าเมืองไปซื้อของก็ไม่ได้ เพราะอย่างนั้นฉันถึงกลั้นความอยากที่จะพลิกตัวนอนต่อแล้วลุกขึ้นมา\nแต่งตัว"

scene bg suburb_roadcenter
with locationskip

# "Somewhere between buying toothpaste and a few other groceries, I end up walking it off. Then, I feel hungry. After stopping for breakfast, it hits me how much time has gone by."
"ระหว่างที่เดินไปซื้อยาสีฟันกับของกินของใช้อย่างอื่นอาหารในท้องก็ย่อยหมดพอดีจนหิวขึ้นมา พอแวะซื้ออาหารเช้า\nแล้วก็เพิ่งรู้ตัวว่าเวลาผ่านไปนานมากแล้ว"

# "I hadn't expected to be out this long at all. I'm not even sure if I bothered to lock my door. I should really get back."
"ไม่ได้คิดเลยว่าจะออกมาข้างนอกนานขนาดนี้ ไม่แน่ใจด้วยซ้ำว่าล็อกประตูห้องแล้วหรือยัง ต้องรีบกลับแล้ว"

scene bg school_dormhallway
show hideaki bored at center
with locationskip

# "When I get back to the dorm, I see Hideaki standing in front of my room from the entrance. I can think of few things more unexpected, and I can't help thinking I might have a heart attack just from the surprise. Fortunately, it doesn't happen."
"พอกลับมาที่หอก็เห็นฮิเดอากิยืนอยู่ตรงหน้าประตูห้อง ฉันพอจะนึกต่อได้ว่าจะเกิดอะไรที่เหนือความคาดหมายอีก\nและอดคิดไม่ได้ว่าฉันคงจะหัวใจวายไปด้วยความตกใจ โชคดีที่ไม่เป็นอย่างนั้น"

show hideaki normal
with charachange

# "As soon as he sees me, he says hello in his usual detached way. I'm a little slow to reply to him, so he repeats the greeting, without missing a beat."
"ทันทีที่ฮิเดอากิเห็นฉันก็ทักทายด้วยน้ำเสียงเนือย ๆ เช่นเคย ฉันตอบช้าไป เขาจึงทักซ้ำอีกรอบทันที"

show hideaki triangle
with charachange

# hh "Hello."
hh "สวัสดี"

show hideaki normal
with charachange

# hh "Is something wrong?"
hh "มีอะไรหรือเปล่า"

# hi "I'm just surprised to see you here."
hi "แค่ตกใจที่เห็นนายอยู่ตรงนี้"

# "Not as surprised as I could have been, since it's impossible to mistake him for anyone else. I'd recognize those weird clothes anywhere. Come to think of it, I've really surrounded myself with distinctive-looking people lately."
"ซึ่งก็ไม่ได้ตกใจสุดขีดขนาดนั้น เพราะยังไงก็รู้แหละว่าเป็นเขาแน่นอนไม่ใช่ใครอื่น ชุดแปลกตาแบบนี้อยู่ที่ไหนก็ดูออก\nจะว่าไป เดี๋ยวนี้ฉันพาแต่คนลักษณะเด่น ๆ มาอยู่รอบตัวฉันเต็มไปหมดเลย"

show hideaki confused
with charachange

# "Hideaki's head lolls slightly to one side, a little too easily."
"ฮิเดอากิเอียงคอเล็กน้อยจนหัวไหลไปดื้อ ๆ"

# hh "Why? Is it unusual to see someone's family come to see them?"
hh "ทำไมครับ ปกติไม่ค่อยมีญาติมาแวะหานักเรียนเหรอ"

# hi "Well… yeah, actually."
hi "ก็… เอ่อ ก็ใช่"

show hideaki surprise_up
with charachange

show hideaki bored
with charachange

# "So, Hideaki isn't such a robot after all. In fact, it's almost as if he's more caught off guard by the fact he even can be caught off guard, but he recovers quickly."
"สรุปฮิเดอากิก็ไม่ได้เป็นเหมือนหุ่นยนต์ขนาดนั้น ที่จริงเหมือนเขาจะตกใจกับการที่ตัวเองตกใจได้มากกว่าเสียอีก\nแต่ครู่เดียวเขาก็ตั้งสติได้"

# "Nevertheless, in that brief moment, he looks his age. That uncomfortable side of his seems like the more honest, and I wouldn't mind seeing more of it."
"แต่แม้กระนั้น จังหวะสั้น ๆ ที่ฮิเดอากิตกใจอยู่นั้นท่าทีเขาก็ดูสมวัย มุมอึดอัดของเขาน่าจะเป็นตัวตนจริง ๆ ซึ่งถ้าได้เห็น\nบ่อยกว่านี้ก็คงดี"

# "Not so much, though, that I'd go out of my way to pry. Only Shizune would be that zealous. That my thoughts get so far is proof she is rubbing off on me."
"แต่ก็ไม่ได้อยากถึงขั้นจะไปเค้นอะไรกับเขาน่ะนะ มีแต่ชิซูเนะแหละที่กล้าพอจะทำอย่างนั้น แค่การที่ฉันคิดอย่างนี้\nก็เป็นหลักฐานว่าฉันติดนิสัยชิซูเนะมาแล้ว"

# hi "I'd think that you'd have a reason, that's all."
hi "แค่คิดว่าคงมีสาเหตุอะไรที่นายมาน่ะ"

show hideaki triangle
with charachange

# hh "There is one."
hh "มีหนึ่งสาเหตุครับ"

# hi "See? Anyway, we can talk while we're looking for her. That's why you're here, right?"
hi "เห็นมั้ย เอาเถอะ ไว้ค่อยคุยกันตอนตามหาตัวแล้วกัน ที่มาก็มาหาชิซูเนะใช่มั้ย"

show hideaki normal_up
with charachange

# hh "Shizune is in the student council room. I was looking for you. We might take a trip soon, a family trip. Do you think she would want to come with us?"
hh "พี่ชิซูเนะอยู่ที่ห้องสภานักเรียน ผมหาพี่อยู่ เดี๋ยวพวกเราอาจต้องไปเที่ยว เที่ยวแบบครอบครัว พี่คิดว่าพี่ชิซูเนะ\nจะอยากมาด้วยมั้ยครับ"

# hi "Yeah, I don't know. She's kind of been on the warpath lately, with a lot of stuff. And once she's focused on something, she won't just drop it. …I guess you would know that."
hi "เออ ไม่รู้สิ ช่วงนี้เห็นมุ่งมั่นเหลือเกินกับอะไรหลายอย่าง แล้วถ้าชิซูเนะได้จดจ่อกับอะไรแล้วจะกัดไม่ปล่อยเลย …แต่\nนายคงรู้อยู่แล้วมั้ง"

show hideaki closed_up
with charachange

# hh "Mm."
hh "อื้ม"

scene bg school_courtyard
with locationskip

# "Hideaki looks much more at ease walking around than I did my first week."
"ฮิเดอากิดูจะคุ้นชินกับการเดินในโรงเรียนกว่าฉันตอนเพิ่งมาสัปดาห์แรกเสียอีก"

# hi "So, this isn't your first time here?"
hi "แล้วนี่เพิ่งเคยมาครั้งแรกเหรอ"

# "Just throwing it out there. Of course, completely ignoring the surrounding environment could just run in the family. It'd explain why Hideaki seems so distant from Shizune. I get the feeling there's more to it than just her deafness."
"แค่โยนหินถามทางเฉย ๆ และแน่นอนว่าโดนเมิน ไอ้ความไม่สนโลกนี่น่าจะเป็นกันทั้งบ้าน ซึ่งก็น่าจะเป็นสาเหตุ\nว่าทำไมฮิเดอากิถึงดูห่างเหินกับชิซูเนะด้วย ฉันรู้สึกว่าไม่ได้เป็นแค่เพราะชิซูเนะหูหนวกหรอก"

show hideaki bored at center
with charaenter

# hh "No, but this is the first time I could walk around so much. It is kind of weird here. I bumped into a person who told me women are not allowed in the dorms."
hh "เคยมาครับ แต่เพิ่งเคยเดินเยอะขนาดนี้ ที่นี่แปลกนะครับ ผมเจอคนหนึ่งที่บอกว่าห้ามผู้หญิงเข้าหอนะ"

show hideaki disapproves
with charachange

# hh "After I told him I am not a woman, he told me I was misleading, and then accused me of being an assassin."
hh "พอบอกว่าผมไม่ใช่ผู้หญิงแล้วก็บอกว่าผมทำให้เขว กล่าวหาว่าผมเป็นผู้ลอบสังหาร"

show hideaki normal
with charachange

# hh "I was warned that he was not only invincible, but strong enough to probably destroy the building with a punch, or at least knock over the painting hanging in the hallway. By the way, that painting is actually screwed to the wall."
hh "เขาเตือนผมว่าเขาแข็งแกร่งสุด ๆ แข็งแกร่งพอที่จะต่อยให้ตึกทลายได้ หรืออย่างน้อย ๆ ก็ชกรูปที่แขวนอยู่ตรง\nโถงทางเดินให้ล้มได้ ว่าแต่นะครับ รูปนั้นจริง ๆ แล้วเขายึดสกรูไว้กับกำแพง"

# hi "Yeah, that's the guy across the hall from me. He's okay."
hi "อืม ไอ้คนที่อยู่ห้องตรงข้ามฉันน่ะแหละ ก็เป็นคนปกติดี"

show hideaki triangle
with charachange

# hh "I see. Oh, you left your door open. It was unlocked when I came here."
hh "อย่างนี้นี่เอง อ้อ พี่เปิดประตูทิ้งไว้ ตอนผมมาลูกบิดไม่ได้ล็อก"

# "I'm a little annoyed that Hideaki knows that. The only way he could is if he had opened my door. But the feeling passes."
"รำคาญหน่อย ๆ ที่ฮิเดอากิรู้ว่าไม่ได้ล็อกประตู เพราะวิธีเดียวที่จะรู้ได้คือเขาต้องเปิดประตูฉันแล้ว แต่ความรำคาญ\nก็หายไปฉับพลัน"

# hi "It doesn't matter."
hi "ไม่สำคัญ"

# hi "I have nothing to hide, or steal."
hi "ฉันไม่มีอะไรจะซ่อนหรือให้ขโมย"

show hideaki happy_up
with charachange

# hh "Your soccer ball is really nice."
hh "ลูกบอลสวยนะครับ"

# hi "That's one of the things that doesn't matter."
hi "อันนั้นก็ของที่ไม่สำคัญอย่างหนึ่ง"

show hideaki serious
with charachange

# hh "If you are a soccer player, a soccer ball is very important."
hh "ถ้าเป็นนักฟุตบอล ลูกบอลสำคัญนะครับ"

# "I guess it is. The thought makes me smile."
"คงงั้น ฉันคิดตามแล้วยิ้ม ๆ"

show bg school_lobby
show hideaki closed_up at center
with locationskip

# hh "I'm here because my father bought a new phone, and he wanted to update Shizune, in case she needs to call him. I thought that you should know, too, since you're her boyfriend, aren't you?"
hh "ผมมาที่นี่เพราะพ่อซื้อโทรศัพท์ใหม่แล้วพ่ออยากบอกให้พี่ชิซูเนะรู้ด้วยเผื่อต้องโทร. หาพ่อ ผมก็รู้สึกว่าพี่ควรจะ\nได้รับรู้ด้วยเพราะพี่เป็นแฟนพี่ชิซูเนะ ใช่มั้ยครับ"

# hi "Yeah…"
hi "อืม…"

# hi "…Why?"
hi "…ทำไม"

show hideaki bored
with charachange

# hh "Just in case there is something wrong, or she needs anything."
hh "เผื่อว่ามีอะไรเกิดขึ้นหรือพี่ชิซูเนะขาดเหลืออะไร"

# "It isn't what I meant, but I'll go along."
"ไม่ได้ถามถึงเรื่องนั้น แต่ตามน้ำไปแล้วกัน"

# hi "Even if she did, she probably wouldn't call."
hi "ต่อให้ขาดเหลือจริง ๆ ก็คงไม่โทร. มาหาหรอก"

show hideaki triangle
with charachange

# hh "That is how she is."
hh "พี่ชิซูเนะเป็นแบบนั้นแหละครับ"

# hi "Well, if you know… Coming all the way here for that, though? He could have updated her via e-mail."
hi "เออ ก็รู้นี่… แต่ถ่อมาถึงนี่เพราะเรื่องโทรศัพท์เนี่ยนะ แจ้งผ่านอีเมลก็ได้มั้ง"

show hideaki closed_up
with charachange

# hh "He does not like using e-mails."
hh "พ่อผมไม่ชอบใช้อีเมล"

# hi "That's so old-fashioned. Don't tell me he still does business through regular mail, or something."
hi "หัวโบราณเป็นบ้า นี่อย่าบอกนะว่าพ่อนายยังใช้จดหมายหรืออะไรแบบนั้นติดต่อสื่อสารเรื่องธุรกิจกันน่ะ"

stop music fadeout 3.0

# "Silence. Now it's my turn to feel awkward. Is Hideaki taking it literally, or did I hit the mark?"
"เงียบ ทีนี้เป็นตาฉันที่อึดอัดบ้าง นี่ฮิเดอากิตีความไปแบบตรงตัวหรือว่าฉันพูดถูกกันแน่"

# "Nah. I'm sure that what it really comes down to is that he does want to see his daughter and stay in contact with her. In the end, they are still family, after all. Even though they play at being at each other's throats."
"ไม่อะ ฉันว่าจริง ๆ แล้วก็แค่ว่าพ่อเขาอยากเห็นหน้าลูกสาวตัวเองบ้างไม่ให้ขาดการติดต่อไปน่ะแหละ ยังไงเสีย\nก็เป็นครอบครัวกัน ถึงท่าทีเหมือนจะฆ่าแกงกันแล้วก็เถอะ"

scene bg school_council
show jigoro smug at tworight
show shizu basic_normal2 at twoleft
with locationskip

play music music_happiness fadein 2.0

# "The door to the student council room is open, and Hideaki and I walk in on Jigoro in mid-rant. He sees us, but decides that it's not something worth stopping rambling at Shizune over. This is really shaking my faith in my previous assumption."
"ประตูห้องสภานักเรียนเปิดอยู่ ฮิเดอากิกับฉันเดินเข้าไปจังหวะที่จิโกโรกำลังพล่ามอยู่พอดี เขาเห็นอยู่ว่าพวกเรามา\nแต่เห็นว่าไม่สำคัญพอที่จะหยุดการพล่ามของตัวเองให้ชิซูเนะฟัง ชักไม่แน่ใจแล้วสิว่าที่เดาไปว่าเขาอยากมาเจอ\nลูกสาวตัวเองนี่จริงหรือเปล่า"

show jigoro angry
with charachange

# hx "When I was in the Student Council, our room was smaller. Colder, too. Like working out of a meat locker. Not like you spoiled kids. What a waste. Sitting here in your giant room, doing nothing."
hx "ตอนพ่อยังเป็นสมาชิกสภานักเรียนนะ ห้องแคบกว่านี้อีก หนาวกว่านี้ด้วย เหมือนอยู่ในตู้แช่เนื้อเลย ไม่เหมือนพวก\nเสียคนอย่างเธอ เสียของจริง ๆ นั่งอยู่ในห้องโอ่โถงแบบนี้แต่ไม่ทำอะไร"

show shizu behind_frown
with charachange

shi "…"

# hx "Aren't there only three of you? That makes having so many desks only seem like an unnecessary display of mindless decadence. Appalling. You must use the desks you need, and not one more. It is part of my code."
hx "พวกเธอมีกันแค่สามคนไม่ใช่เหรอ แล้วมีโต๊ะเยอะอย่างนี้ก็เห็นเลยว่าเป็นพวกชอบความหรูหราไร้ความคิด ทั้งที่\nไม่จำเป็นต้องให้ใครเห็นแบบนี้เลย ห่วยแตกจริง ๆ ต้องใช้โต๊ะเท่าที่จำเป็น ห้ามเกินมาแม้แต่ตัวเดียว ประมวลกฎหมาย\nของฉันว่าไว้อย่างนั้น"

# "It may be odd of me to think so, but… hearing only one half of a conversation is pretty strange. Also, that's some code."
"อาจจะแปลกที่คิดอย่างนี้ แต่… การได้มาฟังบทสนทนาแค่ครึ่งเดียวนี่ประหลาดมาก แล้วก็ประมวลกฎหมายอะไรล่ะนั่น"

# "Now that I've arrived, he changes the subject, and starts talking about the reason he's here."
"พอฉันมาแล้วจิโกโรก็เปลี่ยนเรื่องแล้วพูดถึงสาเหตุที่มาที่นี่แทน"

show jigoro neutral
with charachange

# hx "Hideaki and I are going on a trip."
hx "ฮิเดอากิกับฉันจะไปเที่ยวกัน"

show shizu basic_normal2
with charachange

shi "…"

show jigoro angry
with charachange

# hx "What are you doing? Does everyone who uses sign language mumble while they do it?"
hx "ทำอะไรน่ะ ทุกคนที่ใช้ภาษามือเป็นชอบพึมพำไปพลางทำภาษามือกันทุกคนเลยเหรอ"

# hi "No, but I'm just an amateur. It helps me think. It's kind of like force of habit."
hi "ไม่หรอกครับ แต่ผมก็แค่มือใหม่ ช่วยให้สมองผมทำงานด้วย เหมือนเป็นความเคยชินน่ะครับ"

# hx "Just an amateur… unbelievable… Fine."
hx "แค่มือใหม่… ไม่อยากจะเชื่อ… ก็ได้"

# "He turns back to Shizune just in time to catch her shaking her head from side to side."
"จิโกโรหันไปทันจังหวะที่ชิซูเนะส่ายหน้าพอดี"

show jigoro neutral
with charachange

# hx "Are you sure you won't be coming along?"
hx "แน่ใจนะว่าจะไม่ไปด้วยกัน"

show shizu adjust_frown
with charachange

# "She reiterates the gesture."
"ชิซูเนะทำท่าย้ำ"

show jigoro angry
with charachange

# hx "Fine."
hx "ก็ได้"

show jigoro neutral
with charachange

# hx "Can you tell her to call me if she needs anything?"
hx "ฝากบอกหน่อยว่าถ้าขาดเหลืออะไรก็ให้โทร. มา"

# hi "Yes."
hi "ได้ครับ"

# hi "I really think sending an e-mail would have been easier, though."
hi "แต่ผมว่าส่งอีเมลเอาน่าจะง่ายกว่านะครับ"

show jigoro angry
with charachange

# hx "I'm not going to read e-mails on my phone. If she won't speak, she can call Hideaki. I suppose if I have to be reached, you would have to call me, or that other girl would have to call me. …Hmph. Actually, all three of you can just call Hideaki."
hx "ฉันไม่อ่านอีเมลในโทรศัพท์ฉันหรอก ถ้าไม่ยอมพูดก็โทร. หาฮิเดอากิเอา แต่ยังไงถ้าจะติดต่อฉันไม่เธอก็ยัยอีกคนนั่น\nต้องโทร. หาฉันอยู่ดี …ฮึ จริง ๆ พวกเธอสามคนโทร. หาฮิเดอากิเลยก็ได้"

hide jigoro
with charaexit

stop music fadeout 3.0

# "And with that, he swiftly turns and leaves, Hideaki trailing behind him. A long trip, for something that took five minutes."
"แล้วเขาก็หมุนตัวขวับก่อนจะเดินจากไปโดยมีฮิเดอากิตามไปด้วย ถ่อมาตั้งไกลเพื่อคุยธุระห้านาทีเนี่ยนะ"

# "Neither of them can express their feelings very well. In Shizune's case, I have to question whether she would if she could. It explains a lot, but she doesn't seem unhappy with the arrangement. Even so, I wonder if she might be."
"ไม่มีใครที่แสดงอารมณ์ของตัวเองได้ชัดเลย ส่วนกับชิซูเนะฉันต้องถามว่าต่อให้แสดงอารมณ์ได้แล้วจะทำหรือเปล่า\nฉันพอจะเห็นอยู่ว่าชิซูเนะเองก็ดูไม่ได้ไม่พอใจกับแผนนั้น ถึงอย่างนั้นก็ยังสงสัยอยู่ว่าเธอคิดแบบนั้นจริง ๆ หรือ"

play sound sfx_doorclose
with Pause(1.0)
show shizu basic_normal at center
show bg school_council at bgright
with dissolvecharamove

play music music_normal fadein 3.0

# "When the door closes behind them, leaving Shizune and me by ourselves, she lets out a deep breath that seems to echo in the silence of the room."
"พอประตูปิดลงทิ้งให้เหลือเพียงชิซูเนะกับฉันอยู่กันตามลำพังแล้วเธอก็ถอนหายใจยืดยาวที่ดูจะสะท้อนก้องในห้อง\nอันเงียบงัน"

show shizu behind_frown
with charachange

# ssh "It's totally ridiculous asking me to go on a trip. The timing couldn't be worse, it overlaps the student council elections, for one. Second, I haven't even cheered up Misha. If you consider that, it's annoying to even have anything else to think about."
ssh "จะมาชวนฉันไปเที่ยวนี่บ้าไปแล้วหรือเปล่า จังหวะนรกสุด ๆ อย่างแรกเลยคือเวลาไปทับซ้อนกับช่วงเลือกตั้ง\nสภานักเรียน อย่างที่สองคือฉันยังทำให้มิช่าร่าเริงไม่ได้ด้วย ถ้ามองสองอย่างนี้แล้ว จะให้มีอะไรมาหนักหัวอีกก็คง\nน่ารำคาญ"

# his "Yeah, but you might be too focused on all of that stuff right now."
his "อืม แต่เธออาจจะจดจ่อกับเรื่องพวกนั้นมากไปก็ได้"

show shizu adjust_frown
with charachange

# "Shizune adjusts her glasses roughly."
"ชิซูเนะดันแว่นแบบผ่าน ๆ"

show shizu behind_frown
with charachange

# ssh "Completely, one hundred percent right. The minute I decided I was going to cheer up Misha, everything else went on the back burner, I suppose."
ssh "ถูกต้องตรงเป๊ะเลย ทันทีที่ฉันคิดจะทำให้มิช่าร่าเริง ฉันก็ต้องวางอะไรอย่างอื่นไว้ก่อนหมด มั้งนะ"

# his "I think your dad might care about you more than he lets on."
his "ฉันว่าพ่อก็เป็นห่วงเธอกว่าที่เห็นนะ"

show shizu basic_normal
with charachange

# ssh "I know."
ssh "ฉันรู้"

# his "So, then, it could be a good idea—"
his "งั้น เนี่ย ถ้าเธอ—"

show shizu adjust_frown
with charachange

# ssh "No."
ssh "ไม่"

# "And then again, more firmly, as if for both of us."
"และย้ำอีกครั้งอย่างหนักแน่นกว่าเก่าราวกับว่าย้ำให้ตัวเองไปด้วย"

show shizu cross_angry
with charachange

# ssh "No."
ssh "ไม่"

show shizu basic_frown
with charachange

# ssh "After coming this far, I can't take a break. A vacation would be jarring. It would be like waking up in a different life. Yesterday was like my vacation. So now we have to go all-in."
ssh "ฉันมาขนาดนี้แล้วจะพักไม่ได้ จะไปเที่ยวคงไม่ดีแน่ คงเหมือนตื่นมาใช้ชีวิตครั้งใหม่เลย เมื่อวานเหมือนการพักแล้ว\nคราวนี้เราเลยต้องเทหมดหน้าตัก"

show shizu behind_blank
with charachange

# ssh "I'm sorry, but it's just how I am."
ssh "ขอโทษที ฉันก็เป็นอย่างนี้แหละ"

$ renpy.music.set_volume(0.5, 2.0, channel="music")

window hide
nvl clear
nvl show dissolve

# n "\n\nI remember what Yuuko said, that she found Shizune brave, in a kind of way. I think I understand what she meant, and I have to agree. Even though it could also be called recklessness, and foolishness, and pointless stubbornness, I guess you could call it “bravery” too."
n "\n\nฉันนึกถึงที่ยูโกะบอกว่าตัวเองรู้สึกว่าในแง่หนึ่งแล้วชิซูเนะนั้นกล้าหาญ ฉันว่าฉันพอจะเข้าใจแล้วว่าหมายความ\nว่าอย่างไร และเห็นด้วยกับยูโกะด้วย ถึงอาจจะเรียกได้ว่าเป็นความบ้าบิ่น ความโง่เง่า และความรั้นแบบไร้ประโยชน์ แต่ก็คง\nเรียกว่าเป็น “ความกล้าหาญ” ได้เช่นกัน"

# n "However, I can see that there is a fundamental flaw in Shizune's thinking that I hadn't noticed until now."
n "แต่ฉันเห็นข้อผิดพลาดร้ายแรงของกระบวนการคิดของชิซูเนะที่ก่อนหน้านี้ฉันไม่เคยสังเกตเลย"

# n "\nI'm sure that Shizune has reflected longer, and more arduously than I could, about where she messed up to create such a bad situation between her and Misha. However, as typical for her, she wouldn't let it hold her back and immediately set out to fix the problem."
n "\nฉันมั่นใจว่าชิซูเนะตกตะกอนมานานกว่าและเข้มข้นกว่าฉันว่าตัวเองทำพลาดตรงไหนจนสถานการณ์ระหว่างเธอ\nกับมิช่าถึงได้แย่ขนาดนี้ ทว่าด้วยนิสัยของชิซูเนะ เธอไม่ยอมให้ความคิดนั้นมาฉุดรั้งตัวเองและมุ่งแก้ปัญหาทันที"

# n "This completely ignores a large part of the problem: Misha herself. Moving from critical introspection to holding Misha up as part of a goal causes the person to get lost in the shuffle. Shizune has “said” a lot in the past few days, but nothing about how Misha feels."
n "ซึ่งวิธีคิดแบบนี้จะไม่ได้มองส่วนที่ใหญ่ที่สุดของปัญหานี้ ซึ่งคือตัวของมิช่าเอง การเปลี่ยนสภาพจากการใคร่ครวญ\nสะท้อนคิดมาเป็นการจับมิช่ามาเป็นเป้าหมายทำให้เจ้าตัวหลงลืมอะไรบางอย่างไป สองสามวันมานี้ชิซูเนะ “พูด” มาก\nก็จริง แต่ไม่เคยพูดถึงความรู้สึกมิช่าเลย"

nvl clear

# n "\n\nShizune's way of thinking is abnormal. Few normal people would reject a friend, and then expect things to go back to the way they were so easily. Shizune does, because she sees life as, if I had to put it simply, capable of being segmented and compartmentalized."
n "\n\nแนวคิดของชิซูเนะนั้นเพี้ยนไปจากปกติ คงมีไม่กี่คนที่จะบอกปัดเพื่อนตัวเองแล้วคาดหวังให้อะไร ๆ กลับไปเป็นดังเดิม\nอย่างง่ายดาย ชิซูเนะคิดเช่นนั้นเพราะเธอมองว่าชีวิตนั้น—ถ้าให้ว่ากันง่าย ๆ แล้วก็คงเป็นคำว่า—ตัดแยกและ\nแบ่งเป็นส่วนได้"

# n "Misha, like anyone else, sees it as a whole experience. A long, continuous journey, where one moment of heartache can follow you forever."
n "มิช่านั้นก็เหมือนอย่างทุกคนที่มองเป็นประสบการณ์ก้อนเดียว เป็นการเดินทางต่อเนื่องยาวนานที่แม้แต่ช่วงเวลา\nชวนเจ็บปวดใจเพียงครั้งเดียวก็ตามหลอกหลอนได้ตลอดกาล"

# n "For Shizune, an event is an event, and few of them cross over. Life is compartmentalized around triumphs, failures, and decisions, where each one stands as its own story. It's why the thought of a vacation is jarring to her. It's why she can only appreciate people's immediate emotions."
n "ส่วนชิซูเนะ เหตุการณ์หนึ่งคือเหตุการณ์หนึ่ง โดยมีเพียงไม่กี่เหตุการณ์ที่ซ้อนทับกัน ชีวิตตัดแยกตามความสำเร็จ\nความล้มเหลว และทางเลือก โดยที่แต่ละอย่างนั้นนับว่าเป็นเรื่องราวแยกขาดจากกัน เพราะเหตุนี้เองชิซูเนะจึงมองว่า\nการเที่ยวนั้นเป็นสิ่งรบกวน เพราะเหตุนี้เองชิซูเนะจึงเข้าใจอารมณ์คนเพียงผิวเผิน"

# n "It's exactly how someone obsessed with living in the moment would think, really."
n "จริง ๆ ก็เหมือนกับความคิดของคนที่ยึดติดกับการใช้ชีวิตอยู่กับปัจจุบันทุกกระเบียดนิ้วเลย"

# n "Likewise, Shizune can see Misha as a friend, but I doubt that she has ever thought of Misha as anything more until recently. Or questioned anything about her. “Misha is Misha” would be enough for her, even if to Misha it must be unbelievably stifling."
n "และในทำนองเดียวกัน ชิซูเนะมองว่ามิช่าเป็นเพื่อนก็จริง แต่ฉันไม่แน่ใจว่าเธอจะเคยมองมิช่าเป็นอะไรมากกว่านั้น\nหรือเปล่า ไม่รู้ว่าเคยนึกสงสัยอะไรเรื่องมิช่าหรือไม่ สำหรับชิซูเนะ แค่คิดว่า “มิช่าก็คือมิช่า” ก็พอแล้ว ซึ่งมิช่าคงรู้สึกอึดอัด\nจนแทบหายใจไม่ออก"

nvl clear

# n "\nShizune is just Shizune to herself. It's likely she doesn't even think about the aftereffects of her actions in the long term, as long as they stir up other people's lives. To Misha, though, I'm sure it made her seem almost heroic. Like Yuuko admiring her bravery, and even myself."
n "\nส่วนชิซูเนะก็มองตัวเองว่าชิซูเนะก็คือชิซูเนะ เป็นไปได้ว่าเธอไม่เคยคิดถึงผลที่ตามมาจากการกระทำของตัวเอง\nในระยะยาวด้วยซ้ำ คิดว่าขอแค่ให้ชีวิตคนอื่นมีอะไรขึ้นมาก็พอแล้ว แต่ฉันว่ามิช่าคงมองว่าความคิดแบบนั้นแหละที่ทำให้\nชิซูเนะดูเท่ เหมือนกับการที่ยูโกะ—แม้กระทั่งฉัน—ชื่นชมความกล้าหาญของชิซูเนะ"

# n "And Shizune's thoughts on that sentiment are that it was good she could touch someone's life. But it ends there. It's easy to captivate; much harder to nurture. On to the next thing. Thinking of life in terms of almost completely isolated events has a tendency to isolate a person, too."
n "และชิซูเนะก็มองว่าแนวคิดแบบนั้นดี ดีตรงที่ได้เข้าไปสัมผัสชีวิตใครสักคน แต่มันก็แค่นั้น ทำให้คนอื่นประทับใจได้\nง่ายก็จริง แต่การจะทำให้งอกเงยขึ้นมานั้นยากยิ่งกว่า และเรื่องถัดมา การมองชีวิตเป็นเหตุการณ์แยกขาดจากกัน\nโดยสมบูรณ์นั้นมีแนวโน้มจะทำให้คนหนึ่ง ๆ ปลีกแยกออกมาด้วย"

# n "Though she's trying to remedy it now, the point remains: There is simply no way Shizune could have avoided hurting Misha. Her emotional investment in Shizune was something Shizune couldn't account for, so she didn't. Combined with her personality, it was inevitable."
n "แม้ตอนนี้ชิซูเนะจะลุกขึ้นมาแก้ไขแล้ว แต่ปัญหาหลักก็ยังอยู่เหมือนเดิม อย่างไรชิซูเนะก็ต้องทำให้มิช่าเจ็บอยู่ดี\nความรู้สึกของมิช่าที่ผูกพันกับชิซูเนะนั้นเป็นสิ่งที่ชิซูเนะไม่อาจนำมาพิจารณาร่วมได้ เธอจึงตัดทิ้งไป และยิ่งชิซูเนะ\nเป็นคนแบบนั้นด้วยแล้ว อย่างไรก็เลี่ยงไม่ได้"

# n "Both of them have pretty much told me all of that in bits and pieces over the past couple months I've known them."
n "ทั้งสองต่างก็บอกใบ้ทุกอย่างแล้วตลอดช่วงสองสามเดือนที่ได้รู้จักกันมา"

# n "\nIn the middle of considering their differences, an idea begins to take shape in my mind."
n "\nระหว่างที่พินิจความต่างของพวกเธออยู่นั้นความคิดหนึ่งก็ก่อตัวขึ้นในหัว"

$ renpy.music.set_volume(1.0, 2.0, channel="music")

nvl hide dissolve
nvl clear
window show

# his "Are you working on your plan right now? This second?"
his "กำลังคิดอยู่หรือเปล่า แผนสองเนี่ย"

# his "Your cheer-up-Misha plan."
his "แผนทำให้มิช่าร่าเริง"

show shizu basic_happy
with charachange

# ssh "Of course. I was thinking about it the whole time I was being yelled at."
ssh "แหงสิ ฉันคิดอยู่ตลอดเลยตอนที่พ่อฉันมาตะโกน"

show shizu adjust_happy
with charachange

# "Flicking her glasses up the bridge of her nose with an oddly triumphant air, she taps her finger against her temple."
"ชิซูเนะดันแว่นที่สันจมูกด้วยรังสีผู้มีชัยดูแปลก ๆ เธอใช้นิ้วแตะหน้าผาก"

show shizu behind_smile
with charachange

# ssh "It's multitasking!"
ssh "แบ่งสมองทำหลายหน้าที่ไง!"

stop music fadeout 4.0

# "Really? Isn't it more like you're able to concentrate on something like that because you can't hear? Well, whatever. When I ask her what she thinks of mine, it turns out we've both arrived at a similar idea."
"จริงเหรอ ไม่ใช่ว่าเพราะไม่ได้ยินเลยมีสมาธิมาจดจ่อกับอะไรแบบนั้นหรอกเหรอ เอ้อ เอาเถอะ พอถามชิซูเนะ\nว่าแผนฉันเป็นไงแล้วก็ได้รู้ว่าเราทั้งสองคนต่างคิดเหมือนกัน"

scene black
with dissolve

#****************************

label th_S33:

scene bg school_scienceroom at bgleft
with locationchange

play music music_pearly fadein 5.0

# "Although it makes me feel kind of uneasy, since we're talking about a human being, the first step is to corner Misha."
"ถึงฉันจะรู้สึกไม่ค่อยดีเท่าไหร่เพราะเป้าหมายที่ว่านี้เป็นมนุษย์—ขั้นแรกคือการไล่ต้อนมิช่า"

# "Though the situation is a little too much like something out of a cop drama for me, it's come to this because talking to her normally is proving to be near impossible."
"แต่สถานการณ์ตอนนี้เหมือนอย่างในหนังตำรวจมากกว่า ที่เป็นเช่นนี้เพราะเรารู้แล้วว่าการจะคุยกับมิช่าตามปกตินั้น\nแทบเป็นไปไม่ได้"

# "But we do have classes together. Even the very first class of the day."
"ทว่าเราก็ได้เรียนห้องเดียวกัน วิชาแรกของวันเลยด้วย"

show shizu invis:
    center
    xpos 0.75
show mishashort invis_close:
    center
    xpos 0.15
with None

show shizu behind_blank at tworight
show mishashort perky_confused_close at twoleft
show bg school_scienceroom at center
with dissolvecharamove

# "Although it takes a while for the announcement to come, the second that I hear we're going to be working in groups today, Shizune and I try to make sure Misha is in ours."
"แม้จะประกาศช้าไปหน่อย แต่ทันทีที่ได้ยินว่าวันนี้จะได้ทำงานกลุ่มกันแล้วชิซูเนะกับฉันก็ลากมิช่าให้มาอยู่กลุ่มเดียวกัน"

# hi "You know, I think Mutou assigns a suspiciously large amount of group work and self-study, don't you think so?"
hi "เออเนี่ย ฉันว่าครูสั่งงานกลุ่มกับงานที่ให้ศึกษาด้วยตัวเองบ่อยจนน่าสงสัยเลยนะ ว่างั้นมั้ย"

show mishashort perky_smile_close
with charachange

# mi "Hm~, but it's easy, so it's ok, right~?"
mi "อืมม~ แต่งานก็ไม่ได้ยากนี่ ไม่เป็นไรหรอก ใช่มั้ย~"

# hi "Yeah? There's other stuff that I've been thinking about lately, that might not be okay, though."
hi "อาฮะ? แต่ช่วงนี้ฉันคิดเรื่องอย่างอื่นอยู่น่ะ อันนี้น่าจะเป็น"

# "Misha nods after each sentence, then brushes it all aside."
"มิช่าพยักหน้าตามแต่ละประโยคแล้วทำเป็นไม่สนใจ"

show mishashort sign_confused_close
with charachange

# mi "I thought about it, and~… I don't do enough work when I work with you and Shicchan! So, I'm going to try harder today. So~!, don't distract me, Hicchan~. I have to stay focused~."
mi "ฉันไปคิดมาแล้ว แล้วก็~… พอฉันอยู่กับนายแล้วก็ชิจังฉันแทบไม่ได้ทำงานเลย! วันนี้ฉันจะทำงานให้เยอะขึ้น\nเพราะงั้น~! อย่ากวนกันนะฮิจัง~ ฉันต้องตั้งใจทำ~"

show shizu behind_frustrated
with charachange

# "That was an annoyingly transparent dodge. Shizune doesn't look too happy either, since Misha didn't bother to sign any of it, opting to twirl a pen in her hands instead."
"เป็นการเลี่ยงที่เห็นชัดเสียจนน่าหงุดหงิด ชิซูเนะก็ดูไม่พอใจเท่าไหร่เพราะมิช่าไม่ได้ทำภาษามือเลยแต่ควงปากกา\nในมือแทน"

# "From the shaky way she was doing it, I'm sure it was so she wouldn't sign anything inadvertently."
"มือที่ควงสั่นอย่างนั้นก็แปลว่าทำไปเพราะจะได้ไม่เผลอทำภาษามืออะไรไป"

# "From the way Misha looks, distracted and uneasy, I doubt it's because she wants to keep Shizune out of the loop for any malicious reason. Although, it's still obviously a way of distancing Shizune from herself."
"ดูจากท่าทีของมิช่าที่เหม่อ ๆ และอึดอัดแล้วเธอคงไม่ได้จงใจกีดกันชิซูเนะออกด้วยเหตุผลไม่ดีอะไรหรอก แต่ก็ชัดอยู่ดี\nว่ามิช่ากำลังทำให้ชิซูเนะเบนความสนใจไปจากตัวเอง"

# hi "Shizune wants to talk to you."
hi "ชิซูเนะอยากคุยกับเธอ"

show mishashort perky_sad_close
with charachange

mi "…"

show mishashort perky_confused_close
with charachange

# mi "Can't it wait until later, Hicchan?"
mi "ไว้ค่อยคุยไม่ได้เหรอฮิจัง"

show shizu basic_angry
with charachange

# ssh "No."
ssh "ไม่"

# hi "Why not now?"
hi "ทำไมคุยตอนนี้ไม่ได้"

show mishashort sign_confused_close
with charachange

# mi "We're in the middle of class~…"
mi "ก็เราเรียนอยู่~…"

# "Now she's spinning a pen in each hand. I'm beginning to think her signing has turned into a kind of nervous tic for her. This isn't a good replacement, although the sight of her dual wielding is pretty impressive."
"คราวนี้มิช่าควงปากกาข้างละด้าม ชักสงสัยแล้วว่าหรือการทำภาษามือจะเป็นประสาทอัตโนมัติของมิช่าไปแล้ว\nซึ่งการควงปากกาชดเชยส่วนนั้นได้ไม่ดีเท่าไหร่ แต่ภาพที่เธอควงปากกาสองมือนั้นน่าประทับใจทีเดียว"

# hi "After class, then."
hi "งั้นไว้เลิกเรียนนะ"

scene bg school_scienceroom at bgleft
with shorttimeskip

# "After class, I don't waste a second bringing it back up."
"พอเลิกเรียนแล้วฉันก็ไม่รอช้าถามมิช่าอีกรอบทันที"

show shizu invis:
    center
    xpos 0.75
show mishashort invis_close:
    center
    xpos 0.15
with None

show shizu behind_frown at tworight
show mishashort perky_sad_close at twoleft
show bg school_scienceroom at center
with dissolvecharamove

# "As everyone else files out of the classroom, leaving the three of us alone, Misha takes increasingly longer glances in every direction except forward."
"พอทุกคนออกจากห้องกันไปหมดแล้วเหลือแค่เราสามคนมิช่าก็มองไปทางอื่นที่ไม่ใช่ตรงหน้านานขึ้นทุกขณะ"

# hi "Do you want to get something to eat?"
hi "ไปหาอะไรกินกันมั้ย"

show mishashort hips_frown_close
with charachange

# mi "Why do you and Shicchan keep asking me if I want to eat something~? ~Hicchan?"
mi "ทำไมทั้งนายทั้งชิจังถึงเอาแต่ถามฉันว่าอยากกินอะไรมั้ยตลอดเลย~ ~ฮิจัง"

# hi "Because we're all headed to the cafeteria, and we haven't eaten together in a long time. So, why not?"
hi "เพราะเราจะไปโรงอาหารกัน แล้วเราก็ไม่ได้กินข้าวด้วยกันนานแล้วด้วย ก็ไปกินข้าวกัน"

show mishashort perky_confused_close
with charachange

# mi "Is this about the Student Council?"
mi "เรื่องสภานักเรียนหรือเปล่า"

show shizu behind_blank
with charachange

shi "…"

show mishashort perky_sad_close
with charachange

# "Taking Shizune's lack of a reply as admission, Misha sighs."
"มิช่าถือว่าการที่ชิซูเนะไม่ตอบคือการยอมรับแล้วถอนหายใจ"

show mishashort hips_frown_close
with charachange

# mi "Shicchan, is that all you ever think about?"
mi "ชิจัง ในหัวเธอมีแต่เรื่องนี้เหรอ"

stop music fadeout 5.0

hide mishashort
with charaexit

# "Before Shizune can reply, she leaves. I have to say, I'm not left feeling very confident after what's just happened."
"ก่อนที่ชิซูเนะจะทันได้ตอบมิช่าก็จากไป ต้องบอกเลยว่าพอเห็นเป็นแบบนี้ก็ไม่ค่อยมั่นใจแล้ว"

show shizu behind_blank at center
show bg school_scienceroom at bgleft
with charamove

# "Neither of us were expecting it to go smoothly, but it would have been nice."
"เราสองคนต่างไม่มีใครคาดหวังว่ามันจะเป็นไปอย่างราบรื่น แต่ถ้าราบรื่นก็คงดี"

show shizu adjust_frown
with charachange

# "Reading my mind, Shizune curls a finger around her glasses for awhile before signing."
"เมื่อเห็นว่าฉันคิดอะไรชิซูเนะก็จับแว่นอยู่ครู่หนึ่งก่อนทำภาษามือ"

show shizu basic_angry
with charachange

# ssh "I know what you're thinking, but no, it's not that I think we should give her some space now. I told you I wouldn't give up so easily."
ssh "ฉันรู้นะว่านายคิดอะไรอยู่ แต่ไม่เลย ที่ปล่อยไปไม่ใช่เพราะฉันอยากให้พื้นที่กับมิช่า ฉันบอกแล้วว่าจะไม่ยอมแพ้\nง่าย ๆ หรอก"

# his "Yeah, well, now I'm starting to wonder if it's not too soon."
his "อ่า อืม ฉันชักสงสัยแล้วว่าหรือจะสายไปแล้ว"

show shizu behind_frown
with charachange

# ssh "Cold feet?"
ssh "กลัวขึ้นมาแล้วเหรอ"

show shizu adjust_frown
with charachange

# ssh "Well, I'm not going to. That would be giving up on her."
ssh "เอาเถอะ ฉันไม่กลัวหรอก ฉันจะไล่ตามมิช่าต่อไป"

show shizu behind_blank
with charachange

# ssh "There's a fine line between helping someone and smothering them. But I just want Misha to pull herself together and stop acting so weird."
ssh "ระหว่างการจะช่วยใครสักคนกับการบีบคั้นน่ะคั่นด้วยเส้นบาง ๆ เท่านั้น แต่ฉันก็แค่อยากให้มิช่าตั้งสติแล้วเลิก\nทำตัวแปลก ๆ สักที"

show shizu basic_normal
with charachange

# ssh "I know she can do it. Even if she wants to try, people don't change overnight. If they could, the world would be a much easier place."
ssh "ฉันรู้ว่ามิช่าทำได้ แต่คนเราใช้เวลาแค่ชั่วข้ามคืนเปลี่ยนตัวเองไม่ได้หรอก ต่อให้พยายามแค่ไหนก็เถอะ ถ้าทำได้\nโลกนี้ก็คงสงบสุขขึ้นเยอะ"

# his "Okay, you win."
his "โอเค เธอชนะ"

# his "Then I guess this is the part where we split up and look for her."
his "งั้นก็แปลว่าตอนนี้เราต้องแยกกันตามหามิช่า"

# "Though I'm the only one who is really supposed to find her."
"ถึงเอาเข้าจริง ๆ แล้วก็มีแค่ฉันแหละที่ควรตามหา"

show shizu adjust_happy
with charachange

play music music_tranquil fadein 3.0

# ssh "If I run into her first, I'll call your cell phone."
ssh "ถ้าฉันเจอมิช่าก่อนแล้วจะโทร. หานะ"

# "Smiling, Shizune takes out her cell phone, turning it on to prepare. I notice that she has an extremely high number of unread messages, and looking at her expression, so does she. Twirling it around by the strap a couple of times, she grimaces."
"ชิซูเนะยิ้มแล้วหยิบโทรศัพท์ออกมาเปิดเตรียมไว้ ฉันเห็นว่ามีข้อความที่ยังไม่ได้อ่านหลายข้อความ สีหน้าชิซูเนะ\nบอกว่าเธอเองก็เห็นเช่นกัน เธอหมุนโทรศัพท์เล่นกับสายคล้องอยู่สองสามครั้งพลางทำหน้าเบ้"

show shizu behind_frown
with charachange

# ssh "I don't like using this thing."
ssh "ไม่ชอบใช้เจ้านี่เลย"

show shizu basic_angry
with charachange

# ssh "Why can't I just snap my fingers?"
ssh "ทำไมถึงดีดนิ้วเอาไม่ได้นะ"

# his "And then what? I'm not a dog. And it doesn't travel as far as a phone signal."
his "แล้วไงต่อ ฉันไม่ใช่หมานะ แล้วเสียงดีดนิ้วก็ส่งได้ไม่ไกลเท่าสัญญาณโทรศัพท์ด้วย"

show shizu behind_smile
with charachange

# his "You're having a lot of fun with this, aren't you?"
his "สนุกน่าดูเลยนะเธอ"

# "Shaking her head from side to side, she continues."
"ชิซูเนะสั่นหัวแล้วเสริมอีก"

show shizu adjust_happy
with charachange

# ssh "It's obvious where she will go. You can't look for her on the school grounds, she would want to go as far away as she can."
ssh "ชัดแล้วว่ามิช่าจะไปที่ไหน ไปตามหาที่ลานโรงเรียนไม่เจอแน่ มิช่าต้องอยากไปให้ไกลที่สุด"

show shizu behind_blank
with charachange

# ssh "Check the tea shop? It's usually empty this early; Misha loves to go there if she feels like skipping class, and she loves the parfaits they have there."
ssh "ไปโรงน้ำชามั้ย ปกติเช้า ๆ แบบนี้จะไม่มีคน มิช่าชอบโดดเรียนไปที่ร้านนั้น แล้วก็ชอบพาร์เฟต์ร้านนั้นด้วย"

# "“You really know a lot about her.” But she would overthink it, and turn it into something that would seem a lot more backhanded than it actually is, so I choose to just nod and leave instead, until I feel her holding on to my sleeve."
"“รู้เรื่องมิช่าดีจังนะ” แต่ขืนบอกไปคงคิดมากแล้วเก็บไปคิดว่ามีนัยแฝงอะไรลึกกว่านั้นอีก ฉันจึงเพียงพยักหน้า\nแล้วเดินออกไปจนกระทั่งรู้สึกได้ว่าชิซูเนะจับแขนเสื้อไว้อยู่"

show shizu basic_normal_close
with characlose

# hi "What?"
hi "อะไร"

# "I say instinctively, forgetting that she can't hear me."
"ฉันตอบไปตามสัญชาตญาณโดยลืมไปว่าอีกฝ่ายไม่ได้ยิน"

show shizu behind_smile_close
with charachange

# ssh "It feels nice that I don't have to do it all by myself any more, because I can trust you. I'm really happy."
ssh "พอไม่ต้องทำทุกอย่างเองแล้วรู้สึกดีนะ เพราะฉันเชื่อใจนายได้ด้วย มีความสุขมากเลย"

# "It makes me happy to hear it. I can't think of a way to respond, and end up only nodding again."
"รู้แบบนี้แล้วก็ดีใจแฮะ ฉันไม่รู้จะตอบอย่างไรจึงพยักหน้าไปอีกครั้ง"

play ambient sfx_crowd_indoors fadein 2.0

scene bg school_lobby
show mishashort perky_confused:
    center
    xpos 0.6
    ypos 1.05
show crowd
with locationskip

# "Heading outside, I catch a glimpse of pink hair behind some other girl's head, and as I head that way, I realize that this isn't the way you go if you want to leave school."
"เมื่อออกมาข้างนอกก็เห็นผมสีชมพูที่อยู่ข้างหลังนักเรียนหญิงคนอื่นอยู่ไว ๆ พอลองตามไปก็เห็นว่าไม่ใช่ทางเดิน\nออกโรงเรียน"

# "It's the way to the student council room. If I wanted to avoid Shizune, I wouldn't head there."
"เป็นทางไปห้องสภานักเรียน ถ้าเป็นฉันแล้วฉันไม่อยากเจอหน้าชิซูเนะคงไม่ไปที่นั่นแน่"

# "It's strange that Misha would be going in that direction, then. Maybe she wants to talk things over with Shizune."
"งั้นก็แปลกว่าทำไมมิช่าถึงไปทางนั้น หรือจะมีเรื่องอยากคุยกับชิซูเนะ"

# "In which case, I have to wonder if letting things play out naturally would be such a bad idea after all, especially if it seems to be going in a good direction."
"ถ้าอย่างนั้นฉันก็ต้องมาคิดแล้วว่าหรือการปล่อยให้อะไร ๆ เป็นไปตามธรรมชาติก็คงไม่แย่เหมือนกัน และยิ่งเหมือนว่า\nจะเป็นไปในทางที่ดีด้วย"

show mishashort invis as mishafront:
    center
    xpos 0.6
    ypos 1.05
with None

show mishashort invis at center
show mishashort hips_smile as mishafront at center
with Dissolvemove(0.7)

hide mishashort
hide mishafront
with None

show mishashort hips_smile at center
with None

# "Suddenly, Misha stops and spins around, catching me by surprise."
"อยู่ ๆ มิช่าก็หยุดเดินแล้วหมุนตัวมาจนฉันตกใจ"

show mishashort hips_grin
with charachange

# mi "Surprise~, Hicchan~! Were you looking for me? I had a feeling~!"
mi "เซอร์ไพรส์~ ฮิจัง~! ตามหาฉันอยู่เหรอ ก็ว่าอยู่ต้องใช่แน่ ๆ ~!"

# "I was going to say “Hey, I was just looking for you”, but I suppose that's no good now."
"ฉันเกือบจะพูดไปว่า “เอ้า กำลังตามหาตัวอยู่เลย” แต่พูดตอนนี้คงไม่ดีแน่"

show mishashort hips_grin:
    easeout 0.7 xpos 1.0 alpha 0.0
with Pause(0.7)

# "She isn't even finished with her sentence before she blows past me, heading for the exit. I have to admit that Misha is infuriatingly sharper than I'd expected. Also, surprisingly fast."
"ยังพูดไม่ทันจบประโยคด้วยซ้ำมิช่าก็เดินสวนฉันไปที่ทางออกแล้ว ต้องยอมรับเลยว่ามิช่านั้นฉลาดขึ้นกว่าที่ฉันคาด\nจนน่าหงุดหงิด แถมยังเร็วเหลือเชื่อด้วย"

stop ambient fadeout 2.0

scene bg school_courtyard
with locationskip

# "Although it's more physical activity than I think I should be getting, I manage to catch up with her halfway to the gate."
"ฉันตามมิช่ามาจนถึงประตู แม้สิ่งนี้อาจจะเป็นการขยับตัวที่เกินกว่าร่างกายฉันรับไหวก็ตาม"

# hi "You're really being the rudest woman in the world right now."
hi "นี่เธอทำตัวเป็นผู้หญิงที่หยาบคายที่สุดในโลกเลยนะ"

# hi "Can you just stop trying to run away for one second? I want to talk to you."
hi "เลิกวิ่งหนีสักวินาทีได้มั้ย ฉันอยากคุยกับเธอ"

show mishashort cross_smile at center
with charaenter

# "Misha turns on her heel, looking mildly amused, and raises her hands as if to tell me to go on. Now that I've got her attention, though, it's hard to think of the right thing to say."
"มิช่าหมุนส้นเท้ามาด้วยสีหน้าชอบใจก่อนจะยกมือขึ้นเป็นเชิงให้ฉันพูดต่อ แต่พอมิช่าสนใจแล้วฉันกลับนึก\nไม่ค่อยออกว่าจะพูดอะไรดี"

# hi "Where are you going now?"
hi "นี่เธอจะไปไหน"

show mishashort sign_smile
with charachange

# mi "The Shanghai~."
mi "ร้านเซี่ยงไฮ้~"

# hi "Can I go with you, then?"
hi "งั้นขอไปด้วยได้มั้ย"

show mishashort perky_confused
with charachange

# "Waiting for her to answer feels like an eternity. It's almost as if I can hear my wristwatch ticking off the individual seconds."
"ฉันรอให้มิช่าตอบอยู่นานเหมือนรอเป็นชาติ เงียบราวกับว่าได้ยินเสียงเข็มนาฬิกาข้อมือที่เดินอยู่ทุกวินาทีเลย"

show mishashort hips_smile
with charachange

# mi "Okay, then, Hicchan."
mi "โอเค ก็ได้ ฮิจัง"

stop music fadeout 3.0

# "I get the sense that she only agreed because she doesn't want to argue any more today."
"รู้สึกเหมือนที่ยอมตอบตกลงก็เพราะวันนี้เธอเบื่อจะเถียงแล้ว"

scene bg suburb_shanghaiint
show mishashort perky_smile:
    center
    ypos 1.02
with shorttimeskip

with Pause(0.2)

play sound sfx_storebell
show mishashort perky_confused:
    ease 0.1 ypos 1.0
    ease 0.2 ypos 1.02
with Pause(0.3)

# "When we get there, a couple comes in after us, causing Misha to jump slightly at the noise."
"พอไปถึงแล้วก็มีคนอีกสองคนที่เดินตามเข้ามา มิช่าสะดุ้งกับเสียงนั้นเล็กน้อย"

show mishashort perky_smile_close at Position(ypos=1.1)
with dissolvecharamove

# "Seeing that it isn't Shizune, she relaxes again, smiling almost as usual to order a parfait from Yuuko, and sliding into the nearest booth."
"พอเห็นว่าไม่ใช่ชิซูเนะก็คลายความเกร็งลง ยิ้มอย่างเกือบจะเหมือนตามปกติสั่งพาร์เฟต์กับยูโกะแล้วผลุบนั่งลง\nกับโต๊ะใกล้ ๆ"

# hi "You ran off too fast. You could have at least waited to see what she was going to say."
hi "เธอรีบหนีไปนะ อย่างน้อยก็รอก่อนสิว่าชิซูเนะจะบอกอะไรอีก"

show mishashort hips_frown_close
with charachange

# "Misha's angry reaction tells me it could be that she was afraid of what Shizune might say."
"ท่าทีโกรธของมิช่าบอกฉันว่าเธอคงจะกลัวว่าชิซูเนะจะพูดอะไรต่อ"

# mi "Why are you both doing this, Hicchan?"
mi "ทำไมเธอสองคนถึงทำกันแบบนี้ล่ะฮิจัง"

# hi "Because Shizune still wants to be your friend. I guess that for her it's kinda like launching a nuclear missile from a submarine, you need two keys to do it."
hi "เพราะชิซูเนะยังอยากเป็นเพื่อนกับเธอไง ชิซูเนะคงมองว่าเหมือนการยิงมิสไซล์จากเรือดำน้ำที่ต้องใช้กุญแจสองดอก\nน่ะแหละ"

show mishashort perky_confused_close
with charachange

mi "…"

# hi "What else can she do, though?"
hi "แล้วจะให้ชิซูเนะทำยังไงล่ะ"

# "She isn't automatically signing whatever she hears or says any more, and I'm sure that is the reason Shizune's been having so much trouble with her."
"มิช่าไม่ทำภาษามือตามสิ่งที่ได้ยินหรือพูดโดยอัตโนมัติแล้ว และนี่แหละคงเป็นสาเหตุว่าทำไมช่วงนี้ชิซูเนะถึงได้รับมือ\nกับมิช่าลำบากเหลือเกิน"

# hi "If she tried to just talk it over, you wouldn't listen."
hi "พอชิซูเนะจะคุยกับเธอ เธอก็ไม่ยอมฟัง"

show mishashort perky_sad_close
with charachange

play music music_night fadein 6.0

# "Misha's guilty expression tells me I've hit the mark."
"สีหน้ารู้สึกผิดของมิช่าบอกว่าฉันพูดจี้ใจดำพอดี"

# hi "Do you really hate Shizune that much?"
hi "เกลียดชิซูเนะขนาดนั้นเลยเหรอ"

show mishashort sign_confused_close
with charachange

# mi "No, Hicchan. I told you that."
mi "ไม่ใช่เลยฮิจัง ฉันเคยบอกแล้วนี่"

show mishashort perky_confused_close
with charachange

# "She answers without even flinching, idly playing with a spoon."
"มิช่าตอบทันทีไม่แม้แต่ลังเลพลางจับช้อนเล่น"

# hi "Yeah, I know."
hi "อืม รู้"

# hi "I'm sure she knows it too, but I wonder if it might be easier if you did."
hi "ฉันมั่นใจว่าชิซูเนะก็รู้เหมือนกัน แต่ถ้าเธอเกลียด ๆ ไปเลยเรื่องอาจจะลงตัวกว่านี้ก็ได้มั้ง"

# hi "The only thing she's really thought about for the last week is how to make you happy. Since Shizune is still attached to you. Yesterday, though, she thought that maybe it would be easiest for you if you just hated her."
hi "ตลอดหนึ่งสัปดาห์ที่ผ่านมาชิซูเนะเอาแต่คิดว่าจะทำให้เธอมีความสุขยังไงดี เพราะชิซูเนะยังผูกพันกับเธออยู่\nแต่เมื่อวานชิซูเนะคิดแล้วว่าปล่อยให้เธอเกลียดไปเลยคงดีกว่า"

# hi "Since you didn't tell her you hate her, Shizune thinks that you can both still be friends. She's like that, only thinking in extremes."
hi "เพราะเธอไม่เคยบอกชิซูเนะเลยว่าเกลียด ชิซูเนะถึงคิดว่าพวกเธอสองคนยังเป็นเพื่อนกันได้ ยัยนั่นก็เป็นงี้แหละ\nคิดเป็นแต่อะไรแบบสุดโต่ง"

# "Her parfait is starting to melt, the ingredients coming together in tiny rivers that remind me of the growing roots of a tree being shown through time-lapse photography."
"พาร์เฟต์ของมิช่าเริ่มละลาย วัตถุดิบไหลมารวมกันในสายน้ำเล็ก ๆ ที่ชวนให้ฉันนึกถึงภาพแบบย่นเวลาของรากไม้\nที่แตกแขนงออกไป"

show mishashort cross_frown_close
with charachange

# mi "That's stupid. Shicchan isn't that stupid, Hicchan. Don't be ridiculous~."
mi "บ้าน่า ชิจังไม่โง่ขนาดนั้นหรอกฮิจัง อย่ามาพูดอะไรไร้สาระ~"

# hi "It's got nothing to do with intelligence. Smart people can do stupid things. And anyway, isn't it true? I was terrified last week when we talked, but at the end, I was relieved because it sounded like things might go back to normal."
hi "เรื่องนี้ไม่เกี่ยวกับความฉลาดเลย คนฉลาดก็ทำอะไรโง่ ๆ ได้เหมือนกัน ก็แล้วมันไม่จริงเหรอ สัปดาห์ก่อน\nตอนเราคุยกันฉันกลัวมาก แต่สุดท้ายก็โล่งเพราะดูเหมือนอะไร ๆ จะกลับเป็นปกติแล้ว"

# hi "I wasn't expecting you two to have a fight right after."
hi "ฉันไม่คิดเลยว่าหลังจากนั้นเธอสองคนจะทะเลาะกัน"

show mishashort perky_confused_close
with charachange

# mi "It wasn't a fight, Hicchan. It was just me yelling at her."
mi "ไม่ได้ทะเลาะกันสักหน่อยฮิจัง ฉันแค่ตะโกนใส่ชิจังเอง"

# "I've noticed that Misha's voice never really changes in tone, just volume. It's so low with guilt that I can hardly believe it came from her."
"ฉันสังเกตว่าน้ำเสียงมิช่าไม่เปลี่ยนเลย มีแค่ระดับเสียงเท่านั้นที่ต่าง เป็นเสียงอันเบาที่เต็มไปด้วยความรู้สึกผิดราวกับว่า\nคนพูดไม่ใช่มิช่าเลย"

# hi "Either way, I was happy, because I thought you and her could still be friends. Since she needs you."
hi "แต่เอาเถอะ ตอนนั้นฉันมีความสุขเพราะคิดว่าเธอกับชิซูเนะยังเป็นเพื่อนกันได้ เพราะชิซูเนะขาดเธอไม่ได้"

show mishashort sign_confused_close
with charachange

# mi "Hm~. No she doesn't, Hicchan."
mi "อืม~ ขาดได้สิฮิจัง"

# hi "So? How do you know that? There's a lot of things Shizune doesn't…"
hi "แล้ว? รู้ได้ยังไง หลายอย่างชิซูเนะก็ไม่ได้…"

# "Vocalize? Say? Talk about? I'm afraid if I say the wrong thing, it'll ruin the mood. I get to finally have a conversation with her and don't want to screw it up. I wonder if this is the first time she's had an honest conversation with me."
"ออกปาก? พูด? คุย? ฉันกลัวว่าถ้าพูดอะไรพลาดไปแล้วจะทำลายบรรยากาศหมด มีโอกาสได้คุยกับมิช่าแล้ว\nฉันก็ไม่อยากทำพลาด ครั้งนี้ครั้งแรกเลยหรือเปล่านะที่มิช่าเปิดอกคุยกับฉัน"

# hi "Just because she didn't tell you doesn't mean she doesn't like you."
hi "แค่เพราะไม่เคยบอกไม่ได้แปลว่าไม่ชอบสักหน่อย"

show mishashort hips_frown_close
with charachange

# mi "That doesn't make sense…"
mi "ไม่เห็นจะสมเหตุสมผลเลย…"

# hi "Yes, it does. Otherwise, she would argue back."
hi "สมเหตุสมผลสิ ไม่งั้นชิซูเนะก็คงเถียงกลับแล้ว"

show mishashort hips_grin_close
with charachange

# mi "Wahaha~."
mi "วะฮ่าฮ่า~"

# hi "You don't think so? She picks fights with everyone, so why not you? Obviously, because you're her friend, and she values you. And Shizune is hurt, too."
hi "เธอไม่คิดงั้นเหรอ ชิซูเนะหาเรื่องคนไปทั่ว แล้วทำไมไม่หาเรื่องเธอด้วย แน่นอน ก็เธอเป็นเพื่อนไง แล้วชิซูเนะก็ให้ค่า\nกับเธอด้วย และชิซูเนะก็เจ็บปวดด้วย"

# hi "She's just awful at showing her feelings. Usually does it the wrong way, too. But she still likes you."
hi "ชิซูเนะก็แค่แสดงความรู้สึกไม่เก่ง แล้วหลายครั้งก็แสดงผิดวิธีด้วย แต่ชิซูเนะยังชอบเธออยู่นะ"

show mishashort perky_confused_close
with charachange

# mi "Hicchan, do you remember when I said I didn't want to hate Shicchan, or upset her? The truth is~, I ended up doing both. Now it's like there's, like, an awkwardness between us. It's hard to explain."
mi "ฮิจัง จำได้มั้ยตอนที่ฉันบอกว่าไม่อยากเกลียดชิจัง ไม่อยากทำให้ชิจังโกรธ ความจริงคือ~ ฉันก็ทำไปทั้งสองอย่างเลย\nแล้วตอนนี้ก็เหมือน แบบว่า ความสัมพันธ์ของเรามันกระอักกระอ่วน อธิบายยากนะ"

# hi "Both of you are so stubborn. You were talking about how you didn't want to drift apart from Shizune, but then you're going to let it happen."
hi "เธอสองคนนี่รั้นจริง ๆ เธอเคยบอกว่าไม่อยากแยกจากชิซูเนะ แต่เธอก็ปล่อยให้เป็นแบบนั้น"

# hi "And Shizune is just as bad. She wants to be your friend, but respects you too much to be as aggressive as she'd be with anyone else."
hi "ชิซูเนะก็พอกัน อยากเป็นเพื่อนกับเธอ แต่ก็เคารพเธอจนไม่ได้รุกหนักเท่าที่ทำกับคนอื่น"

# "And I'm sure that Misha interprets Shizune giving her space as a lack of caring."
"และฉันก็มั่นใจว่ามิช่าตีความการให้พื้นที่ของชิซูเนะนั้นเป็นการไม่ใยดี"

show mishashort perky_sad_close
with charachange

# mi "I screwed up already, Hicchan. It'll happen again~, I'm sure. When I think about it that way, I don't know what I'm supposed to do. It feels like either way, I'll end up making things worse. Then, it might be better if I didn't do anything at all, right~?"
mi "ฉันทำพลาดไปแล้วละฮิจัง แล้วก็จะมีพลาดซ้ำสองอีก~ ฉันมั่นใจเลย พอคิดอย่างนั้นแล้วฉันก็ไม่รู้จะทำยังไงดี\nเหมือนไม่ว่าเลือกทางไหนก็ทำให้อะไรแย่ลงไปอีกเหมือนเดิม ถ้างั้นแล้วไม่ทำอะไรเลยสักอย่างก็น่าจะดีกว่าใช่มั้ยล่ะ~"

# hi "Don't be ridiculous. Why would you even think that way in the first place? Be more positive."
hi "พูดอะไรไร้สาระ ไปเอาความคิดแบบนั้นมาจากไหน มองให้มันดีกว่านั้นสิ"

# "“It should be easy for you,” I want to say, but that would be presumptuous."
"“อย่างเธอน่าจะมองได้ไม่ยากนะ” อยากพูดอยู่ แต่น่าจะเป็นการอวดดีเกินไป"

show mishashort hips_smile_close
with charachange

# mi "Hicchan~, I never knew you were so optimistic. I never expected it."
mi "ฮิจัง~ ไม่ยักรู้ว่านายเป็นคนคิดบวกขนาดนี้ คิดไม่ถึงเลยนะเนี่ย"

hi "…"

show mishashort perky_smile_close
with charachange

# mi "You always act so gloomy when I try and surprise you."
mi "ฮิจังเอาแต่ทำตัวซึมตอนที่ฉันมาทำให้ตกใจเล่น"

# hi "No, this is a recent thing. Really. I just hate it when people give up easily now."
hi "เปล่าหรอก ฉันเพิ่งมาเป็นแบบนี้ จริง ๆ นะ ฉันไม่ชอบเวลาคนถอดใจกับอะไรง่าย ๆ"

show mishashort cross_grin_close
with charachange

# mi "Haha~."
mi "ฮ่าฮ่า~"

show mishashort perky_smile_close
with charachange

# mi "“Now,” huh~…?"
mi "“เพิ่ง” เหรอ~…"

# hi "It makes me mad when people give up. I used to think that giving up was kind of like running away, since that's how people always describe it, but now that I think about it, it's usually more like throwing something away."
hi "ฉันโมโหเวลาคนยอมแพ้ ฉันเคยคิดว่าการยอมแพ้เหมือนการวิ่งหนี เพราะคนก็พูดแบบนั้นกันมาตลอด แต่พอลอง\nมาคิดดี ๆ แล้วมันเหมือนการโยนอะไรบางอย่างทิ้งมากกว่า"

# hi "When you run away from something, you can think of it as still being there. So, I was in the hospital, and I didn't just want to run away from my problems, I wanted to never think about them again."
hi "พอเราวิ่งหนีจากอะไรบางอย่าง เราก็ยังนึกถึงว่าสิ่งนั้นยังมีอยู่ได้ เพราะงั้น ตอนที่ฉันอยู่โรงพยาบาล ฉันไม่ได้แค่\nอยากจะวิ่งหนีจากปัญหา แต่ฉันไม่อยากจะคิดถึงมันอีกเลย"

# "Misha eats a spoonful of her gray ice cream goo. Did she only just remember it was there now, or could it be she likes it that way?"
"มิช่าตักกินก้อนไอศกรีมเหลว ๆ หนึ่งช้อน เพิ่งนึกได้หรือไงว่าตัวเองสั่งมา หรือจะชอบกินเละ ๆ แบบนี้กันแน่"

# hi "Anyway, my point is, you can't do that. People are too sentimental to just throw their memories out like that."
hi "แต่นั่นแหละ ที่ฉันจะบอกคือ เธอทำแบบนั้นไม่ได้ คนเราน่ะไม่ได้ใจไม้ไส้ระกำกันถึงขั้นจะทิ้งความทรงจำไปดื้อ ๆ\nอย่างนั้นได้"

# hi "It's impossible. Shizune can't think of life in terms of anything but winning and losing; don't you think she wishes she didn't have to remember the parts where she loses?"
hi "เป็นไปไม่ได้หรอก ชิซูเนะมองชีวิตเป็นแค่ว่าได้มาหรือสูญเสียก็จริง แต่เธอไม่คิดเหรอว่าชิซูเนะก็ไม่อยากนึกถึง\nส่วนที่ต้องสูญเสียเหมือนกัน"

# hi "You can't pick and choose, though. That's like wanting to live in a bubble. The worst part is, your way of thinking is so wasteful. It's making you so pessimistic you're afraid of everything."
hi "เราหยิบจับเลือกอะไรตามใจไม่ได้หรอก ถ้าคิดแบบนั้นก็ไม่ต่างอะไรกับการอยากใช้ชีวิตอยู่แบบปิดไม่รับรู้อะไร\nแล้วที่แย่ที่สุดคือความคิดแบบเธอน่ะไม่ทำให้ได้อะไรขึ้นมาเลย รังแต่จะทำให้เธอมองโลกในแง่ลบจนกลัวไปหมดทุกอย่าง"

stop music fadeout 4.0

# hi "Come on."
hi "ไปกัน"

# "I grab her hand as I wave Yuuko over with the other to pay for our food."
"ฉันจับมือมิช่าไว้แล้วใช้อีกมือโบกเรียกยูโกะให้มาคิดเงิน" 

show mishashort sign_confused_close
with charachange

# mi "Where are we going now?"
mi "นี่เราจะไปไหน"

# hi "Back to school before lunch is over, but I want to check out a few places before then."
hi "กลับไปที่โรงเรียนก่อนหมดพักเที่ยง แต่ก่อนกลับฉันอยากไปแวะที่อื่นสักหน่อย"

scene bg school_gate:
   right
   subpixel True
   linear 30 left
with locationskip

play music music_comfort

# "Although I start feeling tired even after doing what could be described as on the level of a brisk jog at best, Misha and I eventually make it to the gate of the school with a little over ten minutes to spare."
"เมื่อออกไป—อย่างดีก็คงเรียกได้ว่า—วิ่งเหยาะ ๆ กับมิช่าจนเริ่มเหนื่อยแล้วเราก็กลับมาที่ประตูหน้าโรงเรียน ยังทันอยู่\nเหลือเวลาอีกประมาณสิบนาที"

# hi "I didn't even want to really come to this school, you know. I didn't have a choice. When I got to this gate, I'm sure a part of me was thinking, “What a depressing place.”"
hi "เนี่ย ฉันไม่อยากมาเรียนที่นี่เลย ฉันเลือกไม่ได้ พอมาถึงที่ประตูนี้ ในใจตอนนั้นฉันต้องคิดว่า “เป็นที่ที่ชวนหดหู่\nเหลือเกิน” แน่ ๆ"

# hi "It doesn't look depressing at all, though. Well, I still thought I had everything figured out. I felt practically like another person."
hi "ซึ่งไม่ได้ดูหดหู่เลยนะ แต่ก็ ฉันยังคิดอยู่นะว่าฉันจัดการอะไรลงตัวหมดแล้ว รู้สึกเหมือนตัวเองเป็นคนละคนเลย"

# hi "If I could, I'd go back and tell myself to stop thinking he can write everything off at a glance, and acting like his life is already over, and he can never have fun again."
hi "ถ้าเป็นไปได้ฉันก็อยากย้อนเวลากลับไปบอกตัวเองให้เลิกปฏิเสธทุกอย่างทั้งที่ได้เห็นแค่เสี้ยวเดียว เลิกทำตัวเหมือน\nชีวิตจบสิ้นแล้ว เลิกทำเหมือนว่าจะไม่ได้สนุกอีกแล้ว"

scene bg school_gardens:
   right
   subpixel True
   linear 30 left
with locationskip

# "The school grounds are still littered with quite a few people. It's lunchtime, so it's typical."
"ตรงลานหน้าโรงเรียนยังพอมีคนอยู่ประปราย ซึ่งไม่แปลกเพราะเป็นเวลาพักเที่ยง"

# hi "This is where you and Shizune had me helping you put together two festivals. What a lot of hard work. I thought, “I don't have time for this.”"
hi "ที่นี่แหละที่เธอกับชิซูเนะลากฉันให้มาช่วยจัดงานเทศกาล ทุ่มเทจริง ๆ ตอนนั้นฉันคิด “จะมามัวแต่ทำอะไรแบบนี้\nได้ยังไง”"

# hi "When I look back on it, though, I didn't do all that much. I also didn't have anything better to do. I'd have just spent the time alone."
hi "แต่พอลองย้อนมองดูแล้วฉันก็ไม่ได้ทำอะไรมากขนาดนั้น แถมก็ไม่มีอะไรจะทำอยู่แล้วด้วย ถ้าไม่ทำก็คงได้แต่\nอยู่ตัวคนเดียว"

scene bg school_scienceroom:
   right
   subpixel True
   linear 30 left
with locationskip

# "I drag her to our homeroom next, which is empty except for Mutou trying to eat a sandwich before classes resume."
"ฉันลากมิช่าไปที่ห้องเรียนประจำเป็นที่ถัดไป ซึ่งไม่มีคนอื่นอยู่เลยนอกจากครูที่นั่งกินแซนด์วิชรอถึงเวลาเข้าเรียน\nอีกรอบ"

# hi "Every time I thought of either of you, I wished you would leave me alone. Whether it was here, or…"
hi "ทุกครั้งที่ฉันนึกถึงพวกเธอคนใดคนหนึ่งฉันก็นึกอยากให้เธอสองคนปล่อยฉันไปได้แล้ว ไม่ว่าจะที่นี่หรือ…"

scene bg school_lobby
with locationskip

# "Leaving Mutou to his lunch, we head for the nearby vending machine, and I grab a soda while I still have five minutes to drink it. I've spent an entire lunch period with Misha; longer than both Shizune and I have managed to find to talk to her in days."
"พวกเราปล่อยให้ครูกินมื้อเที่ยงต่อไปแล้วมุ่งหน้าไปยังตู้ขายของแบบหยอดเหรียญที่อยู่ใกล้ ๆ ฉันซื้อน้ำอัดลม\nมาหนึ่งกระป๋องแล้วใช้เวลาห้านาทีที่เหลือดื่มจนหมด ฉันอยู่กับมิช่าตลอดช่วงพักเที่ยง ซึ่งนานกว่าเวลาที่ทั้งชิซูเนะ\nกับฉันได้มาคุยกับมิช่าในช่วงสองสามวันนี้เสียอีก"

# hi "…Following me to the cafeteria, or trying to corner me after half my classes."
hi "…ตามมาถึงโรงอาหาร หรือเลิกเรียนมาไล่ต้อนฉัน"

# hi "I never realized we only talked like four times. It really was all in my head. I only barely realized it now."
hi "ฉันไม่เคยรู้ตัวเลยว่าพวกเราคุยกันได้สี่ครั้งเอง ฉันคิดไปเองว่าหลายครั้ง เพิ่งมารู้ตัวก็ตอนนี้เอง"

show mishashort hips_smile at center
with charaenter

# mi "I remember that, Hicchan. But~, I know where all of these places are, too."
mi "ฉันจำได้นะฮิจัง แต่ว่า~ ฉันรู้อยู่แล้วนี่ว่าที่พวกนี้อยู่ตรงไหน"

# hi "Wait, let me finish my guided tour. Since we're running out of time. By the way, do you want a soda?"
hi "เดี๋ยวสิ ขอฉันนำทางให้เสร็จก่อน ใกล้หมดเวลาแล้ว จะว่าไป เอาน้ำอัดลมสักกระป๋องมั้ย"

scene bg school_staircase2
with locationchange

# "Making our way to the stairwell, I'm glad that I don't have to pull her by the hand any more."
"พวกเรามาถึงขั้นบันได ฉันนึกดีใจที่ไม่ต้องดึงมือลากแขนกันแล้ว"

# hi "You get dizzy on stairs, right?"
hi "เธอเวียนหัวกับบันไดใช่มั้ย"

show mishashort perky_sad_close at twoleft
with charaenter

# mi "Yeah~."
mi "อื้ม~"

# hi "I guess just here is good enough, then."
hi "งั้นอยู่แค่ตรงนี้แล้วกัน"

show mishashort perky_sad_close:
    ease 1.0 ypos 1.2
with Pause(1.0)

# "I lean against the wall as Misha sits down on the steps, across from me."
"ฉันยืนพิงกำแพง ส่วนมิช่าก็นั่งที่ขั้นบันไดอยู่ตรงข้ามกันกับฉัน"

# hi "Do you ever miss the people you went to school with in elementary school, or middle school?"
hi "เธอเคยคิดถึงคนที่เรียนด้วยกันสมัยประถมหรือมัธยมต้นหรือเปล่า"

show mishashort perky_confused_close
with charachange

# mi "No."
mi "ไม่"

# "That was fast. She didn't even have to think about it. I find myself cringing reflexively."
"ตอบเร็วแฮะ ไม่ต้องคิดเลยด้วยซ้ำ ฉันทำหน้าเบ้ไปโดยอัตโนมัติ"

# hi "I had more friends in my old school, but I don't talk to them any more. It almost feels like that was another lifetime ago. Which is sad, really."
hi "ที่โรงเรียนเก่าน่ะฉันมีเพื่อนเยอะกว่านี้ แต่ก็ไม่ได้คุยกันแล้วละ รู้สึกเหมือนตอนนั้นเป็นชาติที่แล้วเลย ซึ่งเอาจริง ๆ\nก็น่าเศร้านะ"

# hi "Sometimes I want to talk to them again, but I know I can't. I'm scared, and embarrassed, things like that. They're too far away for me to go see them. Then I think about calling them, but I don't know most of their numbers."
hi "บางครั้งก็อยากไปคุยอีกรอบ แต่ฉันรู้ดีว่าคุยไม่ได้แล้ว ฉันกลัว อาย อะไรแบบนั้น อยู่ไกลเกินกว่าจะไปเจอหน้ากันได้\nแล้วก็คิดว่าโทร. ดีไหมนะ แต่ฉันก็แทบไม่มีเบอร์โทร. ใครเลย"

# hi "And I left on a sour note. So why would they want to see me again?"
hi "แล้วก็ใช่ว่าฉันจะจากมาแบบสวย ๆ ด้วย เรื่องอะไรพวกนั้นจะอยากเจอฉันอีก"

# hi "It feels like I should just forget about it, but I still think about it anyway and regret that I didn't try harder to stay in touch somehow."
hi "รู้สึกเหมือนว่าลืม ๆ ไปเสียเถอะ แต่ฉันก็ยังนึกถึงอยู่ดี แล้วไม่รู้ทำไมถึงรู้สึกผิดที่ไม่พยายามติดต่อพวกนั้น\nให้ดีกว่านี้"

# hi "And I start to think that maybe feeling like I should forget about it is wrong. It would be an insult to all those people I had fun with and a waste of all the good times."
hi "แล้วฉันก็เริ่มคิดว่า หรือความรู้สึกที่ว่าลืม ๆ ไปเสียเถอะน่ะไม่ถูกต้อง คิดแบบนั้นก็คงเป็นการดูถูกทุกคนที่เคยสนุก\nด้วยกันมา เป็นการเอาช่วงเวลาดี ๆ ทั้งหลายนั้นไปทิ้งให้เสียเปล่า"

# hi "Like I said before, even if there are some bad times, too, it's all right if you can look back on them as happy memories."
hi "อย่างที่ฉันเคยบอกนั่นแหละ ถึงจะมีจังหวะที่อะไร ๆ มันไม่ดีบ้าง แต่ก็ไม่ผิดหรอกถ้าเราจะมองย้อนนับว่าสิ่งเหล่านั้น\nเป็นความทรงจำแสนสุข"

# hi "But I didn't even think about it then. So, it was like I woke up one day and realized I had no friends. I just let myself lose all my friends, and it felt awful. I'd really hate it if you and Shizune ended up the same way. That's all."
hi "แต่ตอนนั้นฉันคิดไม่ได้ เลยเป็นความรู้สึกประมาณว่าวันหนึ่งตื่นมาแล้วรู้ตัวว่าไม่เหลือเพื่อนแล้ว ฉันปล่อยให้เพื่อน\nห่างหายไปดื้อ ๆ ซึ่งฉันรู้สึกแย่มาก ฉันไม่อยากให้เธอกับชิซูเนะกลายเป็นแบบนั้นไปเหมือนกัน แค่นั้นแหละ"

show mishashort perky_sad_close
with charachange

# mi "“That's all~.”"
mi "แค่นั้นแหละ~"

# hi "It makes me sad to think that you'll do the same thing and push away your friend. Especially because you're not far away from Shizune; I mean, you even live in the same dorm."
hi "พอคิดว่าเธอจะทำเหมือนกันแล้วผลักไสเพื่อนไปแล้วฉันก็เศร้าขึ้นมา แล้วยิ่งเธอไม่ได้อยู่ไกลจากชิซูเนะด้วย ก็เนี่ย\nอยู่หอเดียวกันด้วยซ้ำ"

# mi "Friend, hm~…"
mi "เพื่อน อืมม~…"

show mishashort perky_confused_close
with charachange

# mi "Aren't you my friend, too, Hicchan?"
mi "ฮิจังก็เป็นเพื่อนฉันเหมือนกันนี่"

# hi "Yeah."
hi "อืมฮึ"

# hi "You slept through all of it, but the fireworks were really nice way back, at the festival."
hi "ดอกไม้ไฟที่งานเทศกาลตอนนั้นสวยมากเลยนะ แต่เธอหลับอยู่"

# hi "My first time seeing fireworks like that. And my first time really seeing the sky in a while. And, I'd never really looked at the stars before then, either."
hi "เป็นครั้งแรกเลยที่ฉันได้เห็นดอกไม้ไฟแบบนั้น แล้วก็ได้เห็นท้องฟ้าแบบเต็มตาเป็นครั้งแรกเลยหลังจากที่ไม่ได้เห็น\nมานาน ก่อนหน้านั้นฉันก็ไม่เคยตั้งใจดูดาวด้วย"

# "I had thumbed through a book about them while I was in the hospital, though, and learned a lot."
"แต่ตอนอยู่โรงพยาบาลฉันก็อ่านเรื่องดาวแล้วเรียนรู้อะไรหลายอย่างมาแล้วน่ะนะ"

# "Like that stars aren't just burning, they're more like a constant chain of explosions, so far away that some of the stars I'd be seeing would have been burnt out for thousands of years already."
"เช่นว่าดาวฤกษ์ไม่ได้เกิดแค่จากการเผาไหม้ แต่เป็นการระเบิดต่อเนื่องแบบลูกโซ่ อยู่ห่างจากโลกมาก บางดวงที่เห็น\nตัวจริงก็ดับไปเป็นพัน ๆ ปีแล้ว"

# "It's that their light would only just then be reaching Earth. I saw a mockup comparing the size of the planet to our sun, and then that to other suns. Japan wasn't even visible on the tiny Earth in that book."
"ที่เป็นแบบนั้นเพราะแสงเพิ่งเดินทางมาถึงโลก ฉันเคยเห็นแผนภาพที่เทียบขนาดดาวเคราะห์กับดวงอาทิตย์\nกับดวงอาทิตย์ดวงอื่นอยู่ มองญี่ปุ่นบนภาพโลกใบเล็กที่อยู่ในหนังสือเล่มนั้นไม่เห็นด้วยซ้ำ"

# hi "You know what I'd never realized?"
hi "เธอรู้มั้ยว่าตอนนั้นฉันไม่รู้อะไร"

show mishashort perky_smile_close
with charachange

# "She looks at me expectantly."
"มิช่ามองรอคำตอบจากฉัน"

# hi "They're amazingly shiny."
hi "ไม่รู้ว่ามันส่องสว่างเหลือเชื่อ"

show mishashort hips_grin_close
with charachange

# mi "Ahahaha~."
mi "อะฮ่าฮ่าฮ่า~"

# hi "It's true."
hi "จริง ๆ นะ"

show mishashort perky_confused_close
with charachange

# mi "Why're you doing this, Hicchan?"
mi "นายทำแบบนี้ทำไมฮิจัง"

# hi "Doing what?"
hi "ทำอะไร"

show mishashort cross_frown_close
with charachange

# mi "I'm not stupid."
mi "ฉันไม่ได้โง่นะ"

# hi "I don't know. A bunch of reasons. Because you're Shizune's friend? And I liked how close you were? And maybe I'm trying to tell you that we all have our low points, but giving up is stupid. Anyway, it seems worth the trouble."
hi "ไม่รู้สิ ก็หลายเหตุผล เพราะเธอเป็นเพื่อนชิซูเนะ? เพราะเห็นว่าเธอสองคนสนิทกันดี? แล้วก็อาจจะเพราะอยาก\nบอกเธอว่าคนเราต่างมีจุดตกอับในชีวิตกันบ้าง แต่จะถอดใจยอมแพ้เลยก็ไร้สาระ นั่นแหละ ก็ดูคุ้มที่จะลงแรงดี"

show mishashort sign_smile_close
with charachange

# mi "That's the only reason?"
mi "แค่นั้นเองเหรอ"

# hi "And you're my friend."
hi "แล้วก็เพราะเธอเป็นเพื่อนฉัน"

show mishashort hips_smile_close
with charachange

# mi "That's it?"
mi "แค่นั้น?"

# hi "Can't I do something for no reason?"
hi "ขอฉันทำอะไรแบบไม่มีเหตุผลไม่ได้หรือไง"

show mishashort hips_grin_close
with charachange

# mi "Wahaha~. You can, you can~, but~, I want to know."
mi "วะฮ่าฮ่า~ ได้สิ ได้สิ~ แต่ว่า~ ฉันอยากรู้นี่นา"

# hi "Well, what else do you want to hear?"
hi "แล้วอยากให้บอกว่าอะไรอีกล่ะ"

play sound sfx_warningbell
stop music fadeout 3.0

# "The bell rings before Misha can reply, so she ends up laughing instead."
"ระฆังดังก่อนที่มิช่าจะทันได้ตอบ เธอจึงหัวเราะแทน"

scene black
with dissolve


#****************************

label th_S34:

scene black
with dissolve

# "I see less of Misha in the following days. But I don't worry, because when I do see her, she looks a bit more like her old self each time."
"วันถัด ๆ มาฉันก็ไม่ค่อยได้เจอมิช่าแล้ว แต่ก็ไม่ได้คิดมากอะไรเพราะแต่ละครั้งที่เห็นมิช่าก็เหมือนกลับเป็นคนเดิม\nทีละน้อย"

# "Once it's clear enough that I don't have to be afraid of it being my wishful thinking coloring my perceptions, I start to relax again."
"พอเห็นได้ชัดถึงขั้นที่ไม่ต้องระแวงว่าฉันคิดบวกไปเองจนมองว่าเป็นอย่างนั้นแล้วจึงค่อยสบายใจขึ้น"

window hide

with Pause(1.0)

scene bg school_dormhisao
with openeye

window show

# "I wake up very early and feeling sick on Sunday. I went to sleep too early last night, too. Something's also wrong with my curtains, and they won't close completely."
"เช้าวันจันทร์ฉันตื่นแต่เช้าตรู่พร้อมอาการครั่นเนื้อครั่นตัว เมื่อคืนเข้านอนเร็วไปด้วย ม่านก็เหมือนจะไม่ปกติ\nเพราะปิดหน้าต่างไม่มิด"

# "Because of that, I can't even attempt to go back to sleep. The sun hits me in the eyes every time. I'm sure this is probably why
# I woke up so early this morning as well."
"และด้วยเหตุเช่นนั้นฉันจึงไปนอนต่อไม่ได้ แสงอาทิตย์แยงตาฉันตลอด คงเพราะอย่างนี้ด้วยฉันถึงได้ตื่นเช้าขนาดนี้"

play sound sfx_doorknock

# "Being this sick and tired is a perfect storm of frustration. I'm almost glad when there's a knock at the door."
"ทั้งป่วยทั้งเพลีย เป็นส่วนผสมที่ชวนให้หงุดหงิดดีเหลือเกิน พอมีคนมาเคาะประตูก็เหมือนจะโล่งใจ"

scene bg school_dormhallway
show kenji neutral at center
with locationchange

play music music_kenji fadein 0.5

# "It's a familiar person holding an almost completely eaten apple in his hand. Taking one last bite, he attempts to shoot it into my trash can and misses completely, and it smashes apart on the wall two meters too high."
"เป็นคนหน้าคุ้นที่ถือแอปเปิลซึ่งพร่องไปจนแทบจะหมดแล้วอยู่ในมือ พอกินคำสุดท้ายเคนจิก็ลองโยนให้ลงถังขยะ\nทว่าคลาดไปไกลโข โดนใส่กำแพงที่ความสูงสูงจากถังขยะไปสองเมตร"

# see report
# "To be fair, most of the pieces afterwards do manage to fall into the trash can, but I'm pretty sure no one is so brazen that they would be aiming to do something like this on purpose."
"แต่เอาจริง ๆ ซากหลายชิ้นที่โดนกำแพงแล้วก็ร่วงใส่ถังขยะอยู่ดี แต่คงไม่มีใครมั่นหน้าถึงขั้นจะจงใจเล็งเพื่อทำอะไร\nอย่างนี้หรอก"

show kenji happy
with charachange

# ke "Perfect shot!"
ke "สวย!"

show kenji neutral
with charachange

# ke "Sup, roomie?"
ke "ไงเพื่อนร่วมห้อง"

# hi "I'm not your roomie, we don't live in the same room."
hi "เพื่อนร่วมห้องบ้านนายสิ เราไม่ได้อยู่ห้องเดียวกันนะ"

show kenji tsun
with charachange

# ke "It doesn't matter."
ke "ไม่สำคัญ"

# hi "It does, you should at least know the difference between living in the same building and living in the same room."
hi "สำคัญสิวะ อย่างน้อยก็หัดแยกบ้างว่าคนที่อยู่อาคารเดียวกันมันไม่เหมือนกับคนที่อยู่ห้องเดียวกัน"

show kenji neutral
with charachange

# ke "I need to use your room."
ke "ขอใช้ห้องนายหน่อย"

# hi "For what?"
hi "จะทำอะไร"

# "I messed up, I should have said “absolutely not.”"
"พลาดแล้ว น่าจะตอบไปว่า “ไม่ให้เสียหรอก”"

show kenji tsun
with charachange

# ke "The Student Council keeps delivering my mail, even though I asked them to put it in my locker or something."
ke "สภานักเรียนเอาแต่ส่งจดหมายมาให้ฉัน ทั้งที่ขอว่าให้เก็บไว้ที่ล็อกเกอร์หรืออะไรนี่แหละ"

# ke "But they keep putting it under my door, delivering my mail without me noticing it, so today, I'm lying in wait to catch them in the act… like a detective, or a safari hunter."
ke "แต่ก็เอามาสอดไว้ใต้ประตูตลอดโดยที่ฉันไม่ทันรู้ตัว วันนี้ฉันเลยจะมาซุ่มดักรอพวกนั้นแบบคาหนังคาเขา…\nเหมือนนักสืบ หรือนักล่าในแอฟริกา"

show kenji neutral
with charachange

# ke "I need to chill in your room for today and look through the little peephole or I won't be able to catch them in the act. And maybe tomorrow, too."
ke "วันนี้ฉันขอมานอนเอกเขนกอยู่ห้องนายแล้วส่องที่ตาแมวหน่อย ไม่งั้นจับพวกนั้นไม่ได้แน่ ๆ แล้วอาจจะมาขออยู่\nพรุ่งนี้ด้วย"

show kenji happy
with charachange

# ke "It'll be awesome, we'll get pizza, on both days. Or should we get pizza on just one day, and something else on the other day? But what? And which day is pizza day?"
ke "ต้องสุดยอดแน่นอน เราจะสั่งพิซซ่ามากินกันทั้งสองวันเลย หรือจะสั่งพิซซ่าวันเดียวแล้วอีกวันสั่งอย่างอื่นดี แต่สั่ง\nอะไรดีล่ะ แล้ววันไหนที่จะสั่งพิซซ่า"

# hi "Not today. Never. You know, I'm in the Student Council. Why didn't you just ask me about this?"
hi "ไม่ใช่วันนี้ ไม่ใช่สักวัน คือ ฉันก็เป็นสภานักเรียนนะ ทำไมไม่ถามฉันเลยล่ะ"

# "If he had, I would have been able to find out very easily and wouldn't have to have Kenji in my room. It's win-win, except I guess this way he might be able to get a pizza out of me. I start thinking that maybe that was Kenji's intention."
"ถ้าถามแล้วฉันก็จะหาคำตอบให้ได้ง่าย ๆ โดยที่เคนจิไม่ต้องบุกห้องฉันเลย ก็ได้ประโยชน์ทั้งสองฝ่าย เว้นก็แต่ว่า\nทางนี้จะเป็นการหาเรื่องให้ฉันเลี้ยงพิซซ่าได้ ชักสงสัยแล้วว่าหรือเจตนาของเคนจิคือแบบนั้น"

# "But… No, I doubt it. There's no way he could plan something that elaborate." 
"แต่… ไม่น่ามั้ง เคนจิคงคิดแผนซับซ้อนซ่อนเงื่อนขนาดนั้นไม่ได้หรอก"

show kenji tsun
with charachange

# ke "You know?"
ke "นายรู้เหรอ"

# hi "When they deliver mail? Well, no. They just hand me my mail when I go to Student Council, usually. The point is, I could find out by asking them. Then I'd know and I could tell you. That's how people find things out, by asking."
hi "เวลาส่งจดหมายเหรอ ไม่อะ ปกติพอฉันไปที่สภานักเรียนพวกนั้นก็เอาจดหมายให้ฉัน ประเด็นคือ ฉันไปถามให้ก็ได้\nฉันก็จะได้เอาคำตอบมาบอกนาย คนเรารู้กันด้วยวิธีนี้แหละ ถามสิถาม"

show kenji neutral
with charachange

# ke "Not cavemen. Aw yeah, no response to that, right? Checkmate."
ke "มนุษย์ถ้ำถามกันไม่ได้นะ อะโธ่ หมดคำตอบเลยอะดิ อะเรียบร้อย"

# hi "…Use your own peephole."
hi "…ใช้ตาแมวห้องตัวเองสิ"

show kenji tsun
with charachange

# ke "What if they see me?"
ke "แล้วถ้าพวกนั้นเห็นฉันล่ะ"

# hi "They can't, that's how peepholes work. It's like a one-way glass."
hi "จะเห็นได้ไง มันส่องกลับไม่ได้ ตาแมวมันก็คือกล้องส่องทางเดียวน่ะแหละ"

show kenji happy
with charachange

# ke "For real? Well… No way. They'll be expecting me to be in my room, anyway. They'll sense my presence and know I'm there. They'd never expect me to actually be in the room across the hall."
ke "จริงเหรอ ก็… ไม่มีทาง ยังไงพวกนั้นก็ต้องเดาว่าฉันอยู่ในห้องแน่ ๆ พวกนั้นจะสัมผัสได้ถึงตัวตนฉันแล้วรับรู้\nว่าฉันอยู่ที่ห้อง คงไม่คาดคิดแน่ว่าจะอยู่ห้องอีกฝั่งน่ะ"

# hi "I'm going to go to the student council room and go get your mail for you, right now."
hi "เดี๋ยวจะไปเอาจดหมายนายที่ห้องสภานักเรียนให้ ตอนนี้แหละ"

show kenji tsun
with charachange

# ke "Then I guess I can't let you leave."
ke "งั้นฉันก็คงปล่อยให้นายไปไม่ได้"

# hi "That's dumb. What if I have to use the toilet?"
hi "บ้าเปล่า เกิดฉันอยากเข้าห้องน้ำล่ะ"

show kenji neutral
with charachange

# ke "Your games won't work on me."
ke "อย่าคิดเล่นตุกติกกับฉันนะ"

scene bg school_dormhisao
with locationchange

# "I sit down at my desk and start doing my homework for the weekend."
"ฉันนั่งที่โต๊ะทำการบ้านสุดสัปดาห์"

# hi "You know, you're going to have to leave eventually, so you can't stay here forever, or keep me here forever. I mean, this is my room to start with."
hi "เออเนี่ย ยังไงเดี๋ยวนายก็ต้องออกไป เพราะงั้นนายจะอยู่ที่นี่หรือกักฉันไว้ตลอดไปไม่ได้ คือ ห้องนี้มันห้องฉัน"

show kenji neutral at tworight
with charaenter

# ke "Yeah, I don't think I can. What time's the mail usually come?"
ke "เออ ฉันก็กะไว้แล้วว่าทำงั้นไม่ได้หรอก ปกติจดหมายมาตอนไหนเหรอ"

# hi "Now."
hi "ตอนนี้"

show kenji tsun
with charachange

# ke "Why are women so slow?"
ke "ทำไมพวกผู้หญิงช้าจัง"

# hi "Why do you care so much about the mail anyway? Are you expecting something?"
hi "ทำไมนายถึงอะไรกับจดหมายขนาดนั้นฮะ นี่นายรออะไรอยู่"

show kenji neutral
with charachange

# ke "I'm always expecting something. …Not today, though."
ke "ฉันรอบางอย่างเสมอ …แต่ไม่ใช่วันนี้นะ"

# hi "Do you want them to send something? Do you even send mail?"
hi "อยากให้เขาส่งอะไรมา นี่นายส่งจดหมายด้วยเหรอ"

show kenji tsun
with charachange

# ke "Nope! That's how they get you. I haven't used the mail since I was eight. Sent a letter to Lego asking them to make Dragonball Legos."
ke "ไม่! นี่แหละจุดที่คนเราจะพลาด ฉันไม่ได้ใช้จดหมายมาตั้งแต่อายุแปดขวบแล้ว ตอนนั้นฉันส่งจดหมายไปที่บริษัทเลโก้\nขอให้ทำเลโก้ดราก้อนบอลให้หน่อย"

show kenji happy
with charachange

# ke "They said they couldn't get the rights and gave me some coupons. Totally worth it, but after that I made sure to stay off the radar."
ke "บริษัทบอกว่าขอลิขสิทธิ์ไม่ได้แล้วส่งคูปองมาให้แทน โคตรจะคุ้ม แต่หลังจากนั้นฉันก็ทำตัวให้ไม่เด่นเข้าไว้"

show kenji neutral
with charachange

# ke "You don't use mail, do you?"
ke "นายไม่ใช้จดหมายใช่มั้ย"

# hi "I wrote to my parents last week."
hi "สัปดาห์ก่อนฉันเขียนจดหมายหาพ่อแม่"

show kenji tsun
with charachange

# ke "But that's how they get you!"
ke "นี่แหละนายพลาดแล้ว!"

# hi "Yes, I should have known. Maybe that's why they put that microchip in me the next day."
hi "เออ รู้งี้ไม่ส่งดีกว่า คงเพราะงี้แหละมั้งวันถัดจากนั้นพวกนั้นก็ฝังไมโครชิปใส่ฉัน"

show kenji neutral
with charachange

# ke "So… the rumors were true."
ke "แปลว่า… ข่าวลือเป็นจริงสินะ"

# "I'd like to know what rumor mill he got that from."
"อยากรู้เหลือเกินว่าไปเอาข่าวลือมาจากแหล่งไหน"

# hi "I was kidding. It's a joke."
hi "ล้อเล่น พูดเล่นเฉย ๆ"

show kenji tsun
with charachange

# ke "Joke? Damn. You would joke on me? I guess this is how it feels… to have jokes cracked on. I never thought it'd happen to me. This is a serious issue. Man, I think you are not appreciating the depths of my dilemma."
ke "พูดเล่น? เฮ้ย นี่ล้อฉันเล่นเหรอ นี่สินะความรู้สึก… ของการโดนล้อเล่น ไม่เคยคิดเลยว่าจะโดนกับตัว เรื่องใหญ่เลย\nนะเนี่ย ให้ตาย ฉันว่านายยังรู้ซึ้งถึงความลำบากที่ฉันต้องอยู่ในภาวะกลืนไม่เข้าคายไม่ออกไม่พอนะ"

# ke "It's a work in many acts. Complicated acts, with many players. It's really hard, okay? After I'm done I'm gonna eat a whole fish, to celebrate. Aaaah, shit. I wanted a pizza, though. I still want pizza. Can I get fish on the pizza? Do they do that now?"
ke "เป็นละครมีหลายองก์ องก์สุดซับซ้อนที่มีผู้เล่นหลายคน เอาเป็นว่าลำบากมากเลย ถ้าจบเรื่องแล้วฉันจะไปกิน\nปลาทั้งตัวเป็นการฉลอง โอยยย ให้ตาย แต่อยากกินพิซซ่า ยังอยากกินพิซซ่าอยู่ ขอพิซซ่าหน้าปลาได้มั้ย เดี๋ยวนี้เขายัง\nใส่ปลาอยู่หรือเปล่า"

# hi "You're going to be paying for it. You still haven't paid me back, and I'm not hungry right now anyway."
hi "นายจ่ายเองนะ ของคราวที่แล้วนายยังไม่ได้คืนฉันเลย แล้วตอนนี้ฉันก็ยังไม่หิวด้วย"

show kenji neutral
with charachange

# ke "Not in the mood for pizza? That's just not possible, son."
ke "ไม่อยากกินพิซซ่าเหรอ เป็นไปได้อย่างไรวะ"

show kenji tsun
with charachange

# ke "It's got to be pizza, anyway. I'm in the pizza stage of my life. Before I was in an ice cream stage, but my girlfriend kept eating all the strawberry out of my Neapolitan. It'll probably happen to you, too."
ke "ยังไงก็ต้องเป็นพิซซ่า ตอนนี้ฉันอยู่ในวัยเสี้ยนพิซซ่า ก่อนหน้านี้เป็นไอศกรีม แต่แฟนก็ชอบตักกินนีโอโพลีแทนแต่ส่วน\nที่เป็นรสสตรอว์เบอร์รี เดี๋ยวนายก็คงประสบเรื่องนี้บ้างเหมือนกัน"

# "It's hard to tell if he's serious half the time; I can only see his expression when he's not nose deep in my door."
"บางทีก็ดูไม่ออกเหมือนกันว่าพูดเล่นหรือพูดจริง จะมองหน้าได้ชัด ๆ ก็แค่ตอนไม่เอาหน้ามาจ่อกับประตูเนี่ย"

# hi "I doubt that. Hey, you know that I do have a girlfriend, right? Not Iwanako, either. The Student Council president, actually."
hi "ไม่หรอกมั้ง เออ นายรู้ใช่มั้ยว่าฉันมีแฟนแล้ว ไม่ใช่อิวานาโกะด้วย เป็นประธานสภานักเรียนแน่ะ"

show kenji neutral
with charachange

# ke "Old news."
ke "ข่าวเก่าแล้ว"

# hi "What? Seriously?"
hi "ฮะ? จริงดิ"

show kenji happy
with charachange

# ke "I have my sources."
ke "ฉันก็มีแหล่งข่าวของฉันอยู่"

show kenji tsun
with charachange

# ke "Anyway… Then it dawned on me that I'd gotten fat from all that ice cream. It was a rude awakening. Like sleeping on a beach and getting hit by a wave that destroys your sand castle."
ke "แต่นั่นแหละ… แล้วฉันก็ระลึกได้ว่าฉันกินไอศกรีมจนอ้วน เป็นการระลึกที่ตบหน้าฉาดจนตื่นเลย เหมือนเวลา\nนอนอยู่บนหาดแล้วโดนคลื่นที่ถล่มปราสาททรายเข้าซัด"

show kenji neutral
with charachange

# ke "I started running. Had to lose the pounds. But maybe… I was really running away from myself."
ke "ฉันเริ่มวิ่ง ต้องลดน้ำหนักหลายกิโลฯ แต่ที่จริงแล้ว… ฉันน่าจะวิ่งหนีตัวเองมากกว่า"

play sound sfx_doorknock
stop music
show kenji rage:
    tworight
    ease 0.3 twoleft
with vpunch

# "A sudden and continuous knocking causes him to leap backwards far enough to hit the wall all the way behind him. I take the opportunity to walk over and open the door."
"เสียงเคาะประตูที่มาแบบกะทันหันนั้นทำให้เคนจิถอยกรูดจนหลังไปชนเข้ากับกำแพง ฉันถือจังหวะนี้เดินไปเปิดประตู"

play sound sfx_dooropen

scene bg school_dormhallway
show shizu behind_blank
with locationchange

# ssh "Good morning. What's up?"
ssh "อรุณสวัสดิ์ เป็นยังไงบ้าง"

# ke "I hear if you salt the doorway they can't enter uninvited."
ke "ฉันเคยได้ยินว่าถ้าวางเกลือไว้ที่ธรณีประตูแล้วจะกันไม่ให้เข้ามาแบบดื้อ ๆ ได้นะ"

play music music_comedy fadein 4.0

scene bg school_dormhisao
show kenji neutral at center
with whip_left

# hi "I'm not going to put salt in my doorway."
hi "ไม่ทำหรอก"

show kenji happy
with charachange

# ke "But… you're considering it. Good."
ke "แต่… นายก็เก็บไปคิดอยู่ ดี"

scene bg school_dormhallway
show shizu behind_blank
with whip_right

# hi "Good morning. Are you here to deliver the mail?"
hi "อรุณสวัสดิ์ มาส่งจดหมายเหรอ"

show shizu adjust_happy
with charachange

# "Nodding, Shizune waves a couple envelopes between our faces. I take them from her, freeing up her hands for conversation."
"ชิซูเนะพยักหน้าแล้วโบกจดหมายสองซองอยู่ตรงหน้าเราสองคน ฉันหยิบจดหมายมาเพื่อให้เธอได้สนทนา"

show shizu basic_normal2
with charachange

# ssh "How did you know, how did you know?"
ssh "รู้ได้ยังไง รู้ได้ยังไง"

# hi "You were hiding it behind your back in a really obvious way."
hi "ก็ซ่อนไว้ข้างหลังไม่เนียนขนาดนั้น"

# ke "Hiding what?"
ke "ซ่อนอะไร"

scene bg school_dormhisao
show kenji tsun at center
with whip_left

# hi "The mail."
hi "จดหมาย"

scene bg school_dormhallway
show shizu basic_normal2
with whip_right

with Pause(0.2)

show shizu adjust_smug
with charachange

# ssh "It's okay, I wasn't trying very hard to hide it in the first place."
ssh "ไม่เป็นไรหรอก ฉันไม่ได้คิดจะลองซ่อนขนาดนั้นอยู่แล้ว"

# hi "That's not like you. You're the type of person who'd go “anything worth trying is worth trying hard.”"
hi "ไม่สมเป็นเธอเลยนะ คนอย่างเธอต้องคิดว่า “อะไรที่ลองได้ก็ต้องลองให้สุด” สิ"

# ke "Girls taking initiative? And what about me? I've been using that phrase for years. Where's my parade, dawg?"
ke "ผู้หญิงเป็นฝ่ายรุกเหรอ แล้วฉันล่ะ ฉันใช้วลีนั้นมาหลายปีแล้วนะ ไหนคำเยินยอสรรเสริญวะ เฮ้ย"

# ke "I spit literary gold and you women just steal it and wear it out like a two-for-one sundress. You're all like the Picard to my Kirk. Or you could even be Janeway."
ke "ฉันผลิตทองคำแท่งแห่งวงการวรรณกรรม แล้วพวกผู้หญิงอย่างเธอก็ขโมยไปใช้ไปโชว์เหมือนเป็นชุดเดรส\nซื้อสองแถมหนึ่งตามตลาดนัด เหมือนฉันเป็นกัปตันเคิร์ก ส่วนพวกเธอทุกคนเป็นกัปตันพิคาร์ด หรือจะเทียบว่าเป็น\nกัปตันเจนเวย์ยังได้เลย"

show shizu behind_frown
with charachange

# ssh "Not all the time. Are you making fun of me?"
ssh "ก็ไม่เสมอไปสักหน่อย นี่ล้อฉันเหรอ"

show shizu adjust_happy
with charachange

# "Finally noticing Kenji, she gives him a wave."
"เมื่อเห็นเคนจิแล้วชิซูเนะก็โบกมือทักทาย"

scene bg school_dormhisao
show kenji tsun at center
with whip_left

# hi "Hey, Kenji, the Student Council president says hi."
hi "นี่ เคนจิ ประธานนักเรียนทักทาย"

show kenji neutral
with charachange

# ke "Hi."
ke "ไง"

scene bg school_dormhallway
show shizu behind_blank at center
with whip_right

# ssh "Introduce me. I have no idea what he was saying, but it looked confident."
ssh "แนะนำตัวฉันให้หน่อย ฉันไม่รู้ว่าเขาพูดอะไรอยู่ แต่ดูมั่นใจดี"

# "Oh yes, no one is better at saying that kind of stuff confidently."
"เอ้อ ใช่แหละ ไม่มีใครจะพูดอะไรอย่างนั้นได้อย่างมั่นใจไปกว่าเคนจิแล้ว"

# hi "I already did. I even introduced you by title. This is Kenji, he's the guy across the hall. His room is right behind you. Anyway, do you have his mail too?"
hi "แนะนำไปแล้ว แนบยศไปให้ด้วยซ้ำ นี่เคนจิ คนที่อยู่ห้องฝั่งตรงข้าม ห้องอยู่ข้างหลังเธอ แล้วนี่มีจดหมาย\nของเคนจิมั้ย"

show shizu adjust_happy
with charachange

# ssh "I'm only delivering your mail because it was there. I have early access! It's all about location. Consider it as a perk of being in the Student Council."
ssh "ฉันเอาจดหมายมาส่งให้นายเพราะมันอยู่ห้องสภานักเรียนหรอก ฉันมีสิทธิ์เข้าถึงก่อน! ของพวกนี้\nขึ้นอยู่กับที่ตั้งทั้งนั้น คิดเสียว่าเป็นสิทธิพิเศษของการเป็นสมาชิกสภานักเรียนแล้วกัน"

# "That doesn't sound very fair. She takes a lot of liberties with her position. At least they're small ones."
"ฟังดูไม่ยุติธรรมเลยแฮะ ใช้อำนาจของตำแหน่งตัวเองทำอะไรหลายอย่างเหมือนกัน อย่างน้อยก็เป็นแค่อะไร\nเล็ก ๆ น้อย ๆ ละนะ"

#if not seen A26b:
label th_S34a:

# ssh "I never got to enter your room before. It's interesting."
ssh "ฉันไม่เคยมาห้องนายเลย น่าสนใจดีนะ"

#if seen A26b:
label th_S34b:

# ssh "This is the first time I've really been able to see your room."
ssh "ครั้งแรกเลยนะเนี่ยที่ได้มาเห็นห้องนายจริง ๆ จัง ๆ"

# "It's a blatant lie, or she'd have signed it much faster. I'm sure Shizune remembers that it's not the first time."
"โกหกเห็น ๆ ไม่งั้นก็คงทำภาษามือบอกเร็วกว่านี้แล้ว ยังไงก็จำได้แหละว่าครั้งนี้ไม่ใช่ครั้งแรก"

#end split
label th_S34c:

show shizu basic_frown
with charachange

# ssh "Why does he get to see your room and I can't? Is it a guy thing?"
ssh "ทำไมเขาได้เห็นห้องนายแต่ฉันไม่ได้เห็น ผู้ชายเขาเป็นกันแบบนี้เหรอ"

# hi "It's not a secret club being a guy."
hi "การเป็นผู้ชายมันไม่ได้เหมือนการเป็นสมาชิกชมรมลับสักหน่อย"

# ke "It should be. With rings. Rings with big-ass emblems. And gold!"
ke "ซึ่งควรจะเป็นนะ ต้องมีแหวนด้วย แบบหัวแหวนขนาดบิ๊กเบิ้ม แล้วก็ทำจากทอง!"

show shizu adjust_smug
with charachange

# ssh "Are you sure? Are you really sure? I always thought that there was a secret brotherhood of men."
ssh "แน่ใจนะ แน่ใจจริง ๆ เหรอ ฉันคิดมาตลอดเลยว่าพวกผู้ชายน่ะมีภราดรภาพเร้นลับเชื่อมถึงกันอยู่"

# ke "Why's she ignoring me? Let me tell her about the guy club. Also, what's up with the hand signals? Is she trying to hex me or something?"
ke "ทำไมยัยนี่ถึงเมินฉันล่ะ ขอฉันเล่าเรื่องชมรมลูกผู้ชายหน่อย แล้วไอ้สัญญาณมือนี่มันอะไร นี่จะเล่นของใส่กันเหรอ"

scene bg school_dormhisao
show kenji tsun at center
with whip_left

# hi "No, stay out of this. I'll have to translate anything you say to her, and I'm not sure if I could even handle it. And she'll probably misunderstand it, and then you'll probably misunderstand the reply, and I'll have to translate your rebuttal."
hi "ไม่ นายถอยไปเลย เดี๋ยวฉันต้องแปลสิ่งที่นายพูดให้ชิซูเนะอีก ซึ่งฉันไม่รู้ว่าจะไหวหรือเปล่าด้วย และเดี๋ยวชิซูเนะก็จะ\nเข้าใจผิด ซึ่งนายก็คงจะเข้าใจประโยคตอบผิดอีก แล้วฉันก็ต้องแปลคำแก้ต่างของนาย"

show kenji happy
with charachange

# ke "Rebuttal? Why would I rebutt? I like my butt."
ke "แก้ต่างเหรอ แก้ทำไม หน้าต่างฉันก็สวยอยู่แล้ว"

scene bg school_dormhallway
show shizu behind_frustrated at center
with whip_right

# ssh "What is he saying?"
ssh "เขาว่าไง"

# hi "He says he has no rebuttal."
hi "เขาบอกว่าไม่มีอะไรจะแก้ต่าง"

show shizu basic_normal
with charachange

# ssh "Rebuttal to what? I haven't even begun to challenge him yet."
ssh "แก้ต่างเรื่องอะไร ฉันยังไม่ได้ท้าอะไรเขาเลยด้วยซ้ำ"

# "I don't like the way she put that. So, it appears that she wants to. But about what? It doesn't matter, since it wouldn't end well."
"ใช้คำได้ชวนให้ใจคอไม่ดีมาก แปลว่าอยากท้าเหรอ แต่จะท้าเรื่องอะไร แต่ไม่สำคัญหรอก เพราะจะเรื่องอะไรก็คง\nจบไม่สวยแน่"

# hi "Don't pick fights where there are none."
hi "อย่าไปหาเรื่องคนอื่นซี้ซั้วอย่างนั้นสิ"

show shizu adjust_frown
with charachange

# ssh "I've never met your friends. Why can't I? It looks like he's… being passionate."
ssh "ฉันไม่เคยเจอเพื่อนนายเลย ทำไมถึงให้เจอไม่ได้ เหมือนว่าเขาเป็นคนที่… ไฟแรงมาก ๆ"

# "I suppose with the way he's flailing around it would be stupid to expect Shizune to think otherwise. Anyway, I'd better change the subject."
"ออกท่าทางขนาดนั้น จะคิดว่าชิซูเนะคงมองเป็นอย่างอื่นได้คงโง่ไป แต่เอาเถอะ เปลี่ยนเรื่องก่อนดีกว่า"

# "Not that it would be likely to work on her, but I'm sure that she has to have come here for a reason, other than just to drop my mail off."
"ซึ่งคงไม่ได้ผลกับชิซูเนะสักเท่าไหร่น่ะนะ แต่ที่มานี่ต้องมีเหตุผลแหละ ไม่ใช่แค่มาส่งจดหมายให้หรอก"

# "If it was something that tiny she wouldn't have even bothered knocking."
"ถ้าเป็นเรื่องเล็กขนาดนั้นคงไม่เคาะประตูด้วยซ้ำ"

# hi "You didn't come here just to give me my mail or chat up my friends, did you?"
hi "เธอคงไม่ได้มาเพื่อแค่จะส่งจดหมายหรือมาคุยกับเพื่อนฉันใช่มั้ย"

play sound sfx_snap

# "Shizune snaps her fingers in mock frustration. It's as cringe-inducingly loud as ever."
"ชิซูเนะดีดนิ้วแทนความหงุดหงิด เสียงยังดังจนชวนให้หน้าหยีเหมือนเคย"

show shizu basic_normal
with charachange

# ssh "You're right."
ssh "ถูกต้อง"

show shizu behind_smile
with charachange

# ssh "Let's go somewhere again."
ssh "ไปสักที่กันอีกกันเถอะ"

# hi "Do you have somewhere in mind already?"
hi "มีที่หมายที่จะไปแล้วเหรอ"

show shizu adjust_smug
with charachange

# ssh "You're right again. Let's go to the usual place."
ssh "ถูกต้องอีกแล้ว ไปที่ประจำกัน"

# see report
# "She whips out a bag of neatly wrapped containers from just outside of the doorframe. I'm guessing they're filled with food, and this time, it doesn't look store-bought. Setting it down between her feet, she continues."
"ชิซูเนะหยิบกล่องที่ห่อมาอย่างดีที่วางอยู่ด้านนอกข้างวงกบ ข้างในคงมีอาหารนั่นแหละ และคราวนี้ไม่ได้ดูเป็นของ\nที่ซื้อมาด้วย เธอวางไว้ตรงระหว่างเท้าสองข้างแล้วเสริมอีก"

show shizu behind_smile
with charachange

# $doublespeak (ke, ssh, "Is that for me?", "This was the real surprise. See?")
$doublespeak (ke, ssh, "ของฉันเหรอ", "นี่ต่างหากเซอร์ไพรส์ของจริง เห็นมั้ย")

show shizu adjust_smug
with charachange

# ssh "I have to have something over everyone at the very end."
ssh "ยังไงฉันก็ต้องทำอะไรสักอย่างให้ทุกคนแหละนะ"

# "I agree, in the way people normally do when someone makes a statement in front of them that tells more than they meant to tell."
"ฉันเห็นด้วย เห็นด้วยแบบที่ปกติคนจะทำเวลามีคนมาพูดอะไรที่มีความหมายมากกว่าความหมายแบบตรงตัวให้ฟัง\nต่อหน้า"

show kenji invis:
    center
    xpos 0.0
with None

show shizu behind_smile at tworight
show kenji tsun at twoleft
show bg school_dormhallway at bgright
with dissolvecharamove

# ke "Well, fine, if you're both going to ignore me, I'm out of here. So cruel. You'll regret this!"
ke "เอาเถอะ ก็ได้ ถ้าพวกเธอทั้งสองคนจะเมินกันละก็ขอตัวก่อนละ ใจร้าย เดี๋ยวจะได้เห็นดีกัน!"

stop music fadeout 2.0

hide kenji
with charaexit

scene ev shizu_roof at shizu_roof_in
with shorttimeskip

play ambient sfx_rooftop fadein 1.0
play music music_soothing fadein 0.5

# "Not long afterwards, we find ourselves on the school roof."
"ไม่นานหลังจากนั้นพวกเราก็มากันที่ดาดฟ้า"

# "Is it normally deserted at this time, on a nice day like this, on the weekend? No, of course not. I can only think that it's because of Shizune. Not that clearing out a roof would require anything more than posting a sign on the door."
"ปกติสุดสัปดาห์วันฟ้าใสแบบนี้ที่ดาดฟ้าจะไม่มีคนเหรอ มี ยังไงก็ต้องมี ฉันนึกสาเหตุออกแค่ว่าเพราะชิซูเนะแน่ ๆ\nแต่จะเว้นที่ให้ดาดฟ้าโล่งก็ไม่ได้ยากหรอก แค่แปะป้ายไว้กับประตูก็พอแล้ว"

# "The empty plastic containers Shizune had packed our meal in lie next to me. It was another quiet meal, since holding chopsticks prevents us from saying much to each other."
"กล่องพลาสติกที่ชิซูเนะใส่อาหารมาซึ่งขณะนี้พร่องไปหมดแล้ววางอยู่ข้างฉัน เป็นมื้อที่ดำเนินไปอย่างเงียบเชียบอีกครั้ง\nเพราะการถือตะเกียบทำให้เราคุยอะไรกันไม่ค่อยได้"

# "While it's not blowing hard enough to be a problem, the wind is a little strong today. It blows the plastic bag loose from under the empty containers, so it whips around for a bit before rolling over my legs and getting caught on the tip of Shizune's shoe."
"วันนี้ลมแรงเล็กน้อย ถึงจะไม่ได้แรงถึงขั้นเป็นปัญหาได้ก็ตาม ลมนั้นพัดถุงพลาสติกที่กล่องเปล่าวางทับอยู่ปลิวมา\nพลิกอยู่บนขาฉันก่อนจะไปเกี่ยวเข้ากับปลายรองเท้าชิซูเนะ"

show ev shizu_roof_towardsangry at shizu_roof_in
with charachange

# "Immediately, she grabs it and starts signing, not looking happy that I'm laughing at her, even though she's trying not to let out a laugh herself. With the bag in the way, however, she has to eventually sit on it to continue."
"ชิซูเนะหยิบถุงใบนั้นแล้วทำภาษามือทันทีด้วยท่าทีไม่พอใจที่ฉันหัวเราะใส่ทั้งที่ตัวเองก็กลั้นขำอยู่แท้ ๆ แต่เมื่อ\nยังมีถุงเป็นอุปสรรคอยู่เธอจึงหยิบไปนั่งทับแล้วบอกว่า"

# ssh "Very funny."
ssh "ตลกมาก"

show ev shizu_roof_towardsnormal at shizu_roof_in
with charachange

# ssh "How was it?"
ssh "เป็นยังไงบ้าง"

show ev shizu_roof2_towardsnormal at shizu_roof_in
with charachange

# his "The food? It tasted familiar."
his "อาหารเหรอ ก็รสชาติคุ้นปากดี"

show ev shizu_roof2_towardsangry at shizu_roof_in
with charachange

# ssh "That means it was bad."
ssh "แปลว่าไม่อร่อย"

show ev shizu_roof_towardsangry at shizu_roof_in
with charachange

# his "No, no. I remember eating this exact meal before, when you made it."
his "อร่อย อร่อยสิ ฉันจำได้ว่าเคยกินเจ้านี่ตอนที่เธอทำมา"

# "Not exactly the same. The fried shrimp was new."
"ไม่เหมือนทุกอย่างน่ะนะ คราวนี้มีกุ้งทอดมาเป็นของใหม่"

# ssh "It's the only thing I know how to make, but I should have improved."
ssh "ฉันทำเป็นแค่นี้แหละ แต่ฝีมือน่าจะดีขึ้นนะ"

# his "How many times have you made it before?"
his "แล้วก่อนหน้านี้เคยทำมาแล้วกี่รอบ"

show ev shizu_roof_towardsnormal at shizu_roof_in
with charachange

# ssh "This is the second time."
ssh "ครั้งนี้ครั้งที่สอง"

# his "Making this particular meal?"
his "ที่ทำอาหารมื้อนี้น่ะนะ"

show ev shizu_roof at shizu_roof_in
with charachange

# ssh "Cooking."
ssh "ที่ทำอาหาร"

show ev shizu_roof_smile at shizu_roof_in
with charachange

# ssh "Next time, it's your turn to try it."
ssh "คราวหน้าตานายลองบ้าง"

show ev shizu_roof_towardsangry at shizu_roof_in
with charachange

# "The way she keeps tugging on the corner of the bag is bothering me. I think I know why she's doing it."
"เห็นชิซูเนะเอาแต่ดึงขอบถุงไว้อย่างนั้นแล้วก็รำคาญตา ฉันว่าฉันรู้แล้วว่าทำไมเธอถึงทำอย่างนั้น"

show ev shizu_roof2_towardsangry at shizu_roof_in
with charachange

# his "Is it really bugging you that much?"
his "คาใจขนาดนั้นเลยหรือไง"

show ev shizu_roof2_towardsnormal at shizu_roof_in
with charachange

# ssh "I want to pack them up properly."
ssh "ฉันอยากเก็บให้เรียบร้อย"

show ev shizu_roof_towardsnormal at shizu_roof_in
with charachange

# his "It's okay, I'll get them."
his "ไม่เป็นไร เดี๋ยวฉันหยิบให้"

# see report
# "As I'm picking them up, I realize she must have brought a lot of food to be able to fill all these containers. I didn't even eat much. Shizune must have some metabolism in order to pack all that away."
"ขณะที่กำลังหยิบถุงอยู่ก็คิดได้ว่าปริมาณอาหารที่ชิซูเนะเอามานั้นคงมีไม่น้อยถึงได้มีกล่องเยอะขนาดนี้ ฉันไม่ได้\nกินเยอะด้วยซ้ำ ระบบเผาผลาญของชิซูเนะต้องดีมากแน่ ๆ ถึงได้เก็บกวาดทุกอย่างไหว"

stop music fadeout 1.0
play sound sfx_impact

scene black
with vpunch

# "Even though I've only been up for a second, it's long enough to stupidly trip over my own feet. Barely managing to break my fall, I end up landing on my elbows and knees right next to Shizune's lap."
"ยืนได้ไม่กี่วินาทีฉันก็สะดุดขาตัวเองเข้าเสียแล้ว ฉันแทบรับตัวเองไว้ไม่ทันล้มลงข้างตักชิซูเนะโดยใช้ข้อศอก\nกับเข่าตัวเองรองไว้"

scene bg school_roof
with locationchange

play sound sfx_heartslow
show heartattack alpha 
with Dissolve (0.1)

hide heartattack
with Dissolve (0.7)

# "As I pull myself back up, hand gingerly held on my chest, all I can think about is how my knees hurt and how this fall could have killed me. I feel nauseous."
"ฉันหยัดตัวลุกขึ้นยืนอีกครั้งพร้อมเอามือลูบอกเบา ๆ ในหัวมีแต่ความเจ็บที่เข่ากับความคิดที่ว่าฉันอาจสะดุดล้ม\nจนตายได้ ชักคลื่นไส้ขึ้นมาแล้ว"

# "Shizune gives a helpful push on my shoulder to help me upright, though I notice her eyeing me oddly. Unfortunately, even a light shove is enough to take me by surprise."
"ชิซูเนะดันไหล่พยุงตัวฉันให้ยืนตัวตรง เธอมองฉันด้วยสายตาแปลก ๆ โชคไม่ดีที่แค่ดันเบา ๆ อย่างนี้ก็ทำให้ฉันตกใจ\nได้แล้ว"

show shizu basic_normal2_close:
    center
    ypos 1.1
with charaenter

# ssh "Are you okay?"
ssh "ไหวมั้ย"

# "I nod, but we don't return to sitting beside each other. Naturally, being alone with Shizune is going to involve a lot of silence, but I only start to notice it now. The typical sign of awkwardness. Again, she's the one to break the ice."
"ฉันพยักหน้า แต่พวกเราไม่ได้กลับไปนั่งข้างกันเหมือนเดิม ไม่แปลกอะไรที่การอยู่กับชิซูเนะจะมีความเงียบ\nเป็นส่วนใหญ่ แต่ฉันเพิ่งสังเกตเอาเดี๋ยวนี้เอง เป็นสัญญาณปกติถึงความกระอักกระอ่วน และเธอก็เป็นฝ่ายเปิดประเด็น\nอีกครั้ง"

show shizu behind_smile_close
with charachange

# ssh "I was expecting you to try something dirty."
ssh "ฉันนึกว่านายจะพูดอะไรสองแง่สองง่าม"

hi "…"

show shizu behind_sad_close
with charachange

# "And now the mood is back to awkward."
"และบรรยากาศก็กลับมากระอักกระอ่วนเหมือนเดิม"

# his "How's Misha?"
his "มิช่าเป็นยังไงบ้าง"

show shizu basic_normal_close
with charachange

play music music_twinkle fadein 6.0

# ssh "Misha seems happier now, back to her old self. I thought this would be a good way to celebrate, and to thank you for helping her."
ssh "มิช่าดูจะมีความสุขขึ้นนะ กลับเป็นมิช่าคนเดิมแล้ว เลยคิดว่าฉลองกันอย่างนี้ดีกว่า แล้วก็เป็นการขอบคุณที่นาย\nช่วยมิช่าด้วย"

# "Her hand stumbles for a bit on the last word."
"มือชิซูเนะกระตุกไปเล็กน้อยกับคำสุดท้ายนั้น"

# his "You think too much like a businesswoman."
his "เธอคิดอะไรเป็นนักธุรกิจเกินไปนะ"

show shizu behind_blank_close
with charachange

# ssh "I can't help it, it's how I've been taught to do things."
ssh "ก็ช่วยไม่ได้นี่นา ที่บ้านฉันสอนมาอย่างนี้"

show shizu adjust_happy_close
with charachange

# ssh "It makes me happy that you're asking about Misha. It would be more accurate to say “back to her real self.” She would only be back to her old self to you."
ssh "ฉันดีใจนะที่นายถามเรื่องมิช่า ถ้าจะให้ถูกต้องใช้คำว่า “กลับไปเป็นตัวตนที่แท้จริง” แล้วมากกว่า ซึ่งมิช่า\nจะกลับไปเป็นมิช่าคนเก่าเพื่อนายเท่านั้น"

show shizu basic_normal_close
with charachange

# ssh "The Misha you know is completely different from the one I think of, when I think of the first time we met. Even though I think she looks better cheerful and smiling, that isn't how she typically is."
ssh "พอลองย้อนนึกดูตอนที่ฉันเจอมิช่าครั้งแรกแล้ว มิช่าที่นายรู้จักน่ะไม่เหมือนกับที่ฉันนึกถึงเลยนะ ถึงมิช่าจะดู\nเหมาะกับความร่าเริงกับรอยยิ้มมากกว่าก็จริง แต่ปกติมิช่าไม่ได้เป็นอย่างนั้น"

show shizu behind_blank_close
with charachange

# ssh "I wonder if it's true for you, too?"
ssh "ไม่รู้ว่านายคิดเหมือนกันหรือเปล่า"

# "I don't answer."
"ฉันไม่ตอบ"

# his "Well, if Misha is happy, then it doesn't matter, if it worked out in the end. Your plan worked."
his "เอาเถอะ ตราบใดที่มันได้ผล ขอแค่มิช่ามีความสุขก็พอแล้วละ แผนของเธอสำเร็จแล้ว"

# his "You knew her just as well as you said. You knew everything she would say. If your idea was just that I'd speak for you, though, doesn't that just make me your puppet? I didn't do anything, then."
his "เธอก็รู้จักมิช่าดีเหมือนกันอย่างทีี่พูดนั่นแหละ เธอรู้หมดว่ามิช่าจะพูดอพไร แต่ถ้าแผนเธอมีแค่การให้ฉัน\nไปพูดแทนเธอแล้วฉันก็เป็นแค่หุ่นเชิด ไม่ได้ลงมือทำอะไรเลย"

show shizu cross_angry_close
with charachange

# ssh "Not true. It was your idea first."
ssh "ไม่จริงเลย นายเป็นคนคิดได้ก่อนต่างหาก"

show shizu basic_frown_close
with charachange

# ssh "I was wrong. I have a way of seeing things that is very flawed, now that I've thought about it. I'm sure you know. Sometimes, I treat everything like a competition between myself and everyone else. Even when it doesn't make sense to."
ssh "ฉันคิดผิด พอลองมานึก ๆ ดูแล้วก็เห็นว่ามุมมองของฉันต่ออะไร ๆ มันมีจุดบกพร่องร้ายแรง นายคงรู้แล้วแหละ\nบางทีฉันก็ทำเหมือนทุกอย่างเป็นการแข่งขันระหว่างฉันกับคนอื่น ทั้งที่บางทีมันก็ไม่สมควรทำเลย"

# "Sometimes?"
"บางที?"

show shizu behind_blank_close
with charachange

# ssh "I know very well how easy it is to ignore someone if they can only communicate with you through sign. I should have asked for help. But I was so sure I could do it on my own. It was actually a brave thing you did. Even if you won't take credit for it."
ssh "ฉันรู้ดีว่าถ้าสื่อสารกับใครสักคนได้ด้วยแค่ภาษามือแล้วฉันจะเมินคนนั้นไปได้ง่าย ๆ เลย ฉันควรขอความช่วยเหลือสิ\nแต่ฉันก็มั่นใจมากว่าทำเองได้ จริง ๆ นายก็กล้ามากนะที่ทำอย่างนั้น ต่อให้นายจะไม่รับคำขอบคุณไว้กับตัวเองก็เถอะ"

show shizu basic_normal_close
with charachange

# ssh "Aside from that, you've really become kind of admirable lately."
ssh "แล้วก็อีกอย่าง ช่วงนี้นายทำตัวน่านับถือมากเลยนะ"

# "It's strange having her compliment me while her facial expression hasn't changed in the slightest."
"พอได้รับคำชมโดยที่สีหน้าของชิซูเนะไม่เปลี่ยนไปเลยแม้แต่น้อยแล้วก็รู้สึกแปลก ๆ แฮะ"

show shizu adjust_frown_close
with charachange

# ssh "But!"
ssh "แต่!"

show shizu basic_happy_close
with charachange

# ssh "“People don't change so easily.” According to you. Am I right?"
ssh "“คนเราไม่ได้เปลี่ยนกันง่าย ๆ ” นายว่างั้นใช่มั้ย"

# "She winks, clearly enjoying herself very much."
"ชิซูเนะขยิบตาชอบใจเป็นอย่างมาก"

# his "Does Misha tell you everything?"
his "มิช่าบอกเธอหมดเลยเหรอ"

show shizu behind_blank_close
with charachange

# ssh "Almost everything."
ssh "เกือบหมด"

# his "I guess you're going to tell me that I'm wrong about that, aren't you?"
his "เธอคงจะบอกว่าฉันคิดผิดใช่มั้ยล่ะที่พูดแบบนั้น"

show shizu basic_normal2_close
with charachange

# ssh "Yes and no."
ssh "ใช่และไม่ใช่"

show shizu adjust_frown_close
with charachange

# ssh "I'm the one who told Misha that before anyone else. But she took it too far, and changed the meaning. It's not easy, but she acts like that makes it impossible."
ssh "ฉันเป็นคนบอกมิช่าก่อนใครเลย แต่มิช่าก็คิดไปแบบสุดโต่งแล้วไปเปลี่ยนความหมาย เปลี่ยนได้ยากก็จริง แต่มิช่า\nก็ทำเหมือนว่าเปลี่ยนไม่ได้เลย"

show shizu basic_normal_close
with charachange

# ssh "It's possible, if you go little by little. I'm considering trying to be less competitive."
ssh "จริง ๆ เปลี่ยนได้นะ ถ้าเปลี่ยนไปทีละเล็กละน้อยน่ะ ฉันคิดอยู่ว่าจะลดเรื่องความอยากเอาชนะลงสักหน่อยดีมั้ย"

# his "I thought you enjoyed that, though."
his "แต่เหมือนเธอจะสนุกนี่"

show shizu behind_smile_close
with charachange

# ssh "Maybe just a little. That's why I specifically used “less.”"
ssh "ก็อาจจะนิดหน่อย ฉันถึงได้เจาะจงใช้คำว่า “ลด” ไงล่ะ"

# "She leans against the fence. I have things I want to say to her, but it doesn't seem like the right time for it, somehow. It's a feeling I have. I can tell she isn't done just yet."
"ชิซูเนะยืนพิงรั้ว ฉันมีบางอย่างอยากบอกเธอ แต่ไม่รู้ทำไมถึงรู้สึกว่าตอนนี้ยังไม่ถึงเวลา แค่รู้สึก ฉันดูออกว่าชิซูเนะ\nยังมีอะไรจะบอกอีก"

show shizu basic_normal2_close
with charachange
 
# ssh "A lot of people think I try too hard."
ssh "คนอื่นมองว่าฉันทุ่มเทมากไป"

show shizu adjust_happy_close
with charachange

# ssh "Well… I've always thought that I try to try just enough."
ssh "ก็นะ… ฉันคิดมาตลอดว่าฉันจะลองทำอะไรโดยทุ่มเทแบบพอดีบ้าง"

# see report
# "The sound the fence makes as she pushes against it, and the delicate clink of her sleeve buttons scraping against the links, are oddly soothing. So is the breeze gently picking up behind me. I can hear people below us."
"เสียงเอี๊ยดจากรั้วที่ชิซูเนะพิงกับเสียงกรุ๋งกริ๋งที่กระดุมชายเสื้อเกี่ยวกับตะแกรงนั้นชวนให้ใจสงบอย่างประหลาด ทั้งยัง\nมีเสียงสายลมหวีดหวิวที่โชยมาอ่อน ๆ อยู่เบื้องหลังและเสียงจอแจของผู้คนจากข้างล่าง"

show shizu basic_normal_close
with charachange

# "Shizune's eyes dart below us as well, and I wonder if she still thinks about what she might be missing out on. The attention-grabbing way she tends to snap her fingers proves she has an understanding of how other people perceive sound."
"สายตาชิซูเนะมองไปที่ข้างล่างเช่นกัน จะคิดอยู่หรือเปล่านะว่าตัวเองพลาดอะไรไปบ้าง เสียงดีดนิ้วที่ดึงความสนใจคนได้นั้น\nเป็นหลักฐานว่าเธอรู้ว่าคนอื่นรับรู้และตีความเสียงอย่างไร"

show shizu invis_close at center
with dissolvecharamove

hide shizu
with None

# "It must be odd, being able to understand that much, but unable to experience it yourself. She starts walking slowly around the perimeter of the roof, still scraping her buttons against the fence. It isn't rhythmic at all, though not for a lack of trying."
"คงแปลกน่าดูที่รู้ถึงขนาดนั้นแต่ไม่อาจสัมผัสได้ด้วยตัวเอง ชิซูเนะออกเดินช้า ๆ ไปตามกรอบดาดฟ้าโดยที่กระดุมนั้น\nยังเกี่ยวไปตามตะแกรงอยู่ เป็นเสียงที่ไม่มีจังหวะใด ๆ แต่ไม่ใช่เพราะไม่เจตนา"

show shizu invis_close at twoleft
with None

show shizu basic_normal_close at center
with dissolvecharamove

# "I sort of zone out in thought while she does, and am rudely snapped out of it when she circles around completely and taps me on the shoulder."
"ระหว่างนั้นฉันก็เหม่อ ๆ ไปพลางก่อนจะสะดุ้งเฮือกรู้ตัวเมื่อชิซูเนะเดินครบรอบแล้วมาแตะไหล่ฉัน"

show shizu behind_blank_close
with charachange

# ssh "Do you remember what we were talking about?"
ssh "จำได้มั้ยว่าเราคุยอะไรกัน"

# his "When? Now? Of course, it just happened."
his "หมายถึงตอนไหนเหรอ เมื่อกี้? แหงสิ ก็เพิ่งคุยไปนี่"

show shizu basic_angry_close
with charachange

# ssh "It's been almost ten minutes."
ssh "ผ่านไปเกือบสิบนาทีแล้วนะ"

show shizu adjust_frown_close
with charachange

# ssh "When I first saw you, you seemed like you were very attached to the idea of feeling sorry for yourself."
ssh "ตอนที่ฉันเห็นนายครั้งแรก นายดูเป็นคนที่จมลึกมากอยู่กับความรู้สึกสมเพช"

# "That stings, even if it is true."
"เจ็บ แต่ก็จริง"

show shizu behind_smile_close
with charachange

# ssh "Sorry, sorry."
ssh "ขอโทษ ขอโทษ"

show shizu basic_normal_close
with charachange

# ssh "It made me want to cheer you up at first sight. I was scared it would be for nothing, though. I couldn't help thinking it would be hard to change your mind."
ssh "พอเห็นหน้าครั้งแรกฉันก็อยากทำให้นายร่าเริงขึ้น แต่ก็กลัวว่าพอทำแล้วคงไม่มีประโยชน์อะไร ฉันอดคิดไม่ได้\nว่าจะเปลี่ยนความคิดนายคงยากมาก"

show shizu behind_smile_close
with charachange

# ssh "But you did. I thought that was very surprising, and also that you might be kind of easily influenced. Still, I was surprised. It made me reconsider a lot of things. Like… that maybe everything was worth it in the end."
ssh "แต่นายก็เปลี่ยน ฉันแปลกใจมาก แล้วก็แปลกใจด้วยที่นายถูกชักจูงง่ายพอตัวเลย แต่นั่นแหละ ฉันแปลกใจจนต้อง\nมานั่งทบทวนอะไรหลายอย่าง เช่น… ว่าสุดท้ายทุกอย่างก็สมกับที่ทุ่มเทไป"

# his "Everything?"
his "ทุกอย่าง?"

show shizu adjust_happy_close
with charachange

stop music fadeout 4.0

# ssh "—That's why I like you."
ssh "—นี่แหละฉันถึงได้ชอบนาย"

# his "I see."
his "อย่างนี้นี่เอง"

# "It's nice to finally know."
"ดีใจจริงที่ได้รู้เสียที"

stop ambient fadeout 2.0

scene black
with dissolve

#****************************

label th_S35:

scene bg school_council_ss at right
show mishashort hips_smile_close_ss at closeleft
show shizu behind_blank_close_ss at closeright
with locationchange

play music music_ease

# hi "…And remember, you have to take this job seriously. Too many people think you can just slack off, and that it isn't important. That is a dangerous way of thinking."
hi "…และอย่าลืมว่าขอให้จริงจังกับงานนี้ มีหลายคนคิดว่าจะอู้ยังไงก็ได้เพราะเป็นเรื่องไม่สำคัญ ซึ่งเป็นความคิดที่\nอันตรายมาก"

show mishashort cross_frown_close_ss
with charachange

# mi "Definitely~. You can't take it too seriously~! If you aren't always thinking big, thinking positive, and if you show any signs of weakness, people will start to think you're incompetent, you know~."
mi "ใช่เลย~ ไม่มีคำว่าจริงจังเกินไปหรอกนะ~! ถ้าไม่ฝันให้ใหญ่ ไม่คิดให้บวก ออกอาการว่าอ่อนแอ คนจะคิดว่าเรา\nเป็นพวกไม่มีน้ำยาเอาได้นะ~"

show mishashort sign_confused_close_ss
with charachange

# mi "And soon you won't be able to do anything because your power is going to be delegated off to others piece by piece, and you'll be left with nothing. That's what happened last time~."
mi "แล้วไม่นานอำนาจของเราก็จะหายไปเพราะตกไปอยู่กับคนอื่นทีละเล็กละน้อย สุดท้ายเราก็จะไม่เหลืออะไรเลย\nคราวที่แล้วก็เป็นแบบนั้น~"

show mishashort hips_grin_close_ss
with charachange

# mi "So~! Remember~, it may seem like an easy job, but a lot of carnage can happen in this room. Ahaha~. And~, out of it. Dealing with school staff, too! Even trying to get a budget report from a class rep can be a fight to the death~, sometimes."
mi "เพราะงั้น~! จำไว้~ อาจดูเหมือนเป็นงานง่าย ๆ แต่ในห้องนี้ก็อาจมีการถล่มกันเกิดขึ้นได้ อะฮ่าฮ่า~ แล้วก็~\nนอกห้องก็เกิดได้ด้วย ไหนจะต้องรับมือกับคนของทางโรงเรียนอีก! แม้แต่การไปขอรายงานงบประมาณจากหัวหน้าห้อง\nก็อาจกลายเป็นศึกชิงเลือดกันได้เลยนะ~ บางที"

# hi "…Yeah. It's kill or be killed. There are no friends in the pits and you take no prisoners. …Are you sure about this? Is this right?"
hi "…ใช่ หลักการของที่นี่คือไม่ฆ่าก็ถูกฆ่า ***** …เธอแน่ใจแล้วเหรอ ให้พูดแบบนี้ใช่มั้ย"

show shizu basic_angry_close_ss
with charachange

# ssh "You don't seem excited enough, I have to make sure it's getting through properly. Once more, with feeling!"
ssh "นายยังดูตื่นเต้นไม่พอนะ ฉันต้องดูให้แน่ใจว่าข้อความที่จะสื่อน่ะส่งผ่านไปโดยสมบูรณ์หรือยัง อีกรอบ\nใส่อารมณ์เข้าไป!"

show aoi_keiko:
    yalign 1.0 xanchor 0.5 xpos 0.0 alpha 0.0
with None

play sound sfx_flash

show bg school_council_ss at left
show mishashort invis_close at Position(xpos=1.1)
show shizu invis_close at Position(xpos=1.6)
show aoi_keiko:
    center
    alpha 1.0
with Dissolvemove(0.5)

# "Shizune twists her hands like a maestro for emphasis, visibly intimidating the two girls standing at attention in front of us. To think this all started because one of them asked if she wasn't taking her job too seriously."
"ชิซูเนะบิดมืออย่างวาทยกรเป็นการเน้น ซึ่งทำให้สองสาวที่อยู่ตรงหน้าเรานั้นมีท่าทีกลัวอย่างเห็นได้ชัด เหลือเชื่อมาก\nเพราะเรื่องทั้งหมดนี้เกิดขึ้นแค่เพราะมีคนหนึ่งถามว่าตัวเองจริงจังกับงานนี้ไปมั้ย"

# ssh "Do you understand!?"
ssh "เข้าใจมั้ย!"

# hi "Do you understand? Pretend I'm shouting it."
hi "เข้าใจมั้ย แกล้งทำเป็นว่าฉันตะโกนนะ"

# "Aoi" "Okay, okay! Aaargh! This Student Council is so weird."
thname ("อาโออิ") "โอเค โอเค! อ๊าาาา! สภานักเรียนที่นี่แปลกจัง"

# "Keiko" "Yes, sir."
thname ("เคโกะ") "ค่ะท่าน"

# hi "“Sir?” Who are you guys talking to, anyway?"
hi "“ท่าน”? นี่พวกเธอคุยกับใครอยู่เนี่ย"

play sound sfx_flash

show bg school_council_ss at right
show mishashort hips_smile_close_ss at closeleft
show shizu adjust_frown_close_ss at closeright
show aoi_keiko:
    yalign 1.0 xanchor 0.5 xpos 0.0 alpha 0.0
with Dissolvemove(0.5)

# ssh "It's not weird! You have to think of it as a job. If you want, think of it like they are paying you with the right to use this great office."
ssh "ไม่แปลกสักหน่อย! พวกเธอต้องมองว่าเป็นงานสิ หรือจะมองว่าเป็นงานที่เขาให้ผลตอบแทนเป็นการให้สิทธิ์\nใช้สำนักงานอันยิ่งใหญ่แห่งนี้ก็ได้"

play sound sfx_flash

show bg school_council_ss at left
show mishashort invis_close at Position(xpos=1.1)
show shizu invis_close at Position(xpos=1.6)
show aoi_keiko:
    center
    alpha 1.0
with Dissolvemove(0.5)

# hi "You want another lecture?"
hi "อยากให้พูดอีกมั้ย"

# "Aoi" "Noooo…"
thname ("อาโออิ") "ม่าาาาาย…"

# ssh "You can go now."
ssh "ไปได้"

stop music fadeout 5.0

scene bg school_council_ss
show mishashort perky_smile_ss:
    twoleft
    ypos 1.1
with shorttimeskip

# "Just like that, the hour-long student council orientation is over. Personally, I thought it was about fifty minutes too long, and also found it funny that it incorporated a tour of a school that we have all been going to for a while, but I guess it didn't hurt."
"และแล้วการปฐมนิเทศสภานักเรียนที่กินเวลาไปหนึ่งชั่วโมงก็สิ้นสุดลง แต่ฉันรู้สึกว่านานเกินกว่าความจำเป็น\nไปสักห้าสิบนาทีได้ แล้วก็ตลกดีที่ในการปฐมนิเทศมีการพาเดินตระเวนรอบโรงเรียนอย่างที่พวกเราทำกันมาสักพักแล้ว\nแต่ก็คงไม่เสียหายอะไรมั้ง"

# "I expect Shizune to fall back into her chair, since she has been on edge all day, but she doesn't. She continues pacing the room restlessly."
"ฉันคิดไว้ว่าชิซูเนะคงหย่อนตัวลงนั่งที่เก้าอี้เพราะยืนอย่างจดจ่อมาทั้งวันแล้ว แต่ก็ไม่นั่ง เธอยังคงเดินไปรอบห้อง\nอย่างกระวนกระวายใจ"

show shizu invis:
    center
    xpos 1.0
with None

play music music_shizune fadein 1.0

show shizu adjust_frown_ss at tworight
with dissolvecharamove

# ssh "They still have a long way to go! Right now, they're a joke."
ssh "ยังอีกนานเลยกว่าจะใช้ได้! ตอนนี้สภาพยังเหลวเป๋วอยู่"

show mishashort sign_confused_ss:
    twoleft
    ypos 1.1
with charachange

# mi "Eh?"
mi "เอ๊ะ"

# hi "What?"
hi "อะไร"

show shizu behind_frustrated_ss
with charachange

# ssh "They think they can be the new Student Council? They're so unfocused. You can really see the lack of experience. This was our best year yet; I don't think they have what it takes to be our follow-up act."
ssh "คิดเหรอว่าจะมาเป็นสภานักเรียนรุ่นใหม่ได้ ไม่มีเป้าหมายชัดเจนเลย เห็นแล้วก็รู้ว่ายังขาดประสบการณ์ ปีนี้เป็นปี\nที่ดีที่สุดแล้ว ฉันว่าพวกนั้นยังไม่ดีพอจะมาสานต่อจากเราได้"

show shizu basic_frown_ss
with charachange

# ssh "And I know there are more of them than those two girls. Where are they? They're like the heavily-marketed but mediocre, big-budget, critically-panned sequel to the acclaimed, low-budget sleeper hit."
ssh "และฉันรู้ว่ายังมีคนอื่นอีกนอกจากสองคนนั้น อยู่ไหนกันหมด สองคนนั้นดูแล้วเหมือนหนังภาคต่อทุ่มทุนสร้าง\nที่ทำการตลาดหนัก ๆ แต่มีแต่คนด่า ซึ่งหนังภาคก่อนหน้าเป็นหนังดีทุนต่ำที่มีแต่คนยกย่องแถมไม่ได้ทำการตลาด\nอะไรมากมายเลย"

show mishashort perky_confused_ss
show shizu behind_blank_ss:
    ypos 1.1
with dissolvecharamove

# "Eventually, she does stop and sit down."
"สุดท้ายชิซูเนะก็นั่งพัก"

# hi "Are you going to miss it?"
hi "เธอคงจะคิดถึงสภานักเรียนน่าดูเลยสินะ"

show shizu basic_normal_ss
with charachange

# ssh "Obviously."
ssh "แหงสิ"

show mishashort perky_sad_ss
with charachange

# mi "Hm~… I'd be happier if I didn't have to leave, too."
mi "อืม~… ฉันก็เหมือนกัน ฉันคงมีความสุขกว่านี้ถ้าได้อยู่ต่อ"

show mishashort hips_smile_ss
with charachange

# mi "I like being in the Student Council, even if it can be tiring, too."
mi "ฉันชอบอยู่ในสภานักเรียนนะ ถึงบางทีจะอยู่แล้วเหนื่อยก็เถอะ"

# hi "Yeah, it's definitely tiring."
hi "อืม เหนื่อยจริงแหละ"

show mishashort hips_grin_ss
with charachange

# mi "Only because Shicchan is always trying to do more than she has to~."
mi "ก็เพราะชิจังคอยทำอะไรเกินกว่าความจำเป็นตลอดเลย~"

show shizu adjust_frown_ss
with charachange

# ssh "You're forgetting that if I did the bare minimum, we wouldn't do anything all year except hand out flyers, collect surveys, and plan the next student council election so the next Student Council could sit around for another year of doing nothing."
ssh "พวกเธอลืมนึกไปนะว่าถ้าฉันทำแค่เท่าที่จำเป็นเราก็คงแทบไม่ต้องทำอะไรเลยตลอดปีการศึกษา จะมีก็แต่\nแจกเอกสาร ทำแบบสำรวจ แล้วก็วางแผนสำหรับการเลือกตั้งสภานักเรียนรุ่นถัดไปเพื่อให้รุ่นถัดไปที่ว่าเข้ามานั่งอยู่เฉย ๆ\nไปอีกปี"

show shizu behind_frown_ss
with charachange

# ssh "Asking me to let that happen? Don't be ridiculous. In a Student Council like that there wouldn't even be any power to play around with."
ssh "แล้วคนอย่างฉันมีเหรอจะปล่อยให้เป็นอย่างนั้น พูดอะไรไร้สาระ สภานักเรียนแบบนั้นน่ะไม่มีอำนาจอะไรให้ใช้\nได้หรอก"

show shizu adjust_happy_ss
with charachange

# ssh "I'm just happy that even though I clearly need to ride them harder, those two aren't bad. Not there yet, but the new Student Council should be in good hands."
ssh "แต่ฉันก็ดีใจนะที่สองคนนั้นก็ไม่ได้แย่ ถึงฉันจะยังกดดันไม่พอก็เถอะ ยังไม่ดีพอ แต่สภานักเรียนรุ่นใหม่ก็ดูจะ\nมั่นคงละนะ"

# hi "How can you tell?"
hi "รู้ได้ยังไง"

show shizu behind_smile_ss
with charachange

# ssh "After the festival, they asked me if we could also organize a Halloween event, like a haunted house or something along those lines. They had a bunch of other ideas, as well."
ssh "หลังเลิกงานเทศกาลแล้วพวกนั้นก็มาถามว่าให้จัดงานวันฮาโลวีนด้วยได้มั้ย เหมือนจะเป็นบ้านผีสิงหรืออะไร\nนี่แหละมั้ง แล้วก็คิดจะทำอะไรอย่างอื่นหลายอย่างด้วย"

show shizu adjust_smug_ss
with charachange

# ssh "Of course my response was “no.” I had Misha tell them to do it themselves, if they wanted it so badly. They were angry, for some reason."
ssh "ซึ่งแน่นอนว่าฉันตอบว่า “ไม่” ฉันฝากมิช่าให้บอกว่าไปทำกันเองนะถ้าอยากให้มีขนาดนั้น แต่ไม่รู้ทำไมถึงโกรธ"

show mishashort cross_laugh_ss
with charachange

# mi "Ahaha~."
mi "อะฮ่าฮ่า~"

# hi "Of course they'd be angry if you said that."
hi "พูดแบบนั้นก็โกรธสิ"

# "And Misha delivering the message wouldn't help."
"แล้วยิ่งให้มิช่าเป็นคนพูดด้วย"

show mishashort cross_smile_ss
show shizu behind_blank_ss
with charachange

# ssh "I was angry too."
ssh "ฉันก็โกรธเหมือนกัน"

show shizu basic_frown_ss
with charachange

# ssh "All of a sudden, they want so much. If they wanted a haunted house, or a traditional-style café, or a trip to the beach, or whatever other cliché thing, why didn't they try to organize it before? It was like they were taking advantage of me."
ssh "อยู่ ๆ ก็มาเรียกร้องอะไรเยอะแยะ ถ้าอยากได้บ้านผีสิง คาเฟตามแบบดั้งเดิม ทริปเที่ยวทะเล หรืออะไรก็ช่าง\nที่โรงเรียนอื่นเขาทำกัน ทำไมก่อนหน้านี้ไม่ลองจัดกันเองล่ะ คงกะจะมายืมแรงฉันให้ทำสิท่า"

show shizu behind_frown_ss
with charachange

# ssh "I worked hard to organize those festivals, and in return they came to me with “That was nice, but can you do this now? How about doing this? It's what I really want.”"
ssh "ฉันลงแรงไปตั้งเยอะกับการจัดงานเทศกาลพวกนี้ แล้วมาตอบแทนกันด้วยการบอกว่า “เยี่ยมเลย งั้นเดี๋ยวทำนี่อีกสิ\nอันนี้เป็นไง อันนี้แหละที่อยากได้มาก”"

show mishashort sign_smile_ss
with charachange

# mi "Shicchan was wrong~, though."
mi "แต่ชิจังคิดผิด~ นะ"

show shizu basic_happy_ss
with charachange

# ssh "Right. They wanted to join the Student Council so they could make it happen. I made them feel jealous and riled them up. That can be a kind of motivation too."
ssh "ใช่ พวกนั้นมาเป็นสภานักเรียนเพราะอยากทำให้สิ่งเหล่านั้นเกิดขึ้นได้ ฉันยั่วโมโหทำให้พวกนั้นอิจฉา ซึ่งก็นับว่า\nเป็นแรงกระตุ้นได้เหมือนกัน"

show shizu adjust_happy_ss
with charachange

# ssh "The desire to do something great spreads, even if it's to show me up. They decided to take me up on the challenge nonetheless."
ssh "ความปรารถนาที่จะทำสิ่งดี ๆ ก็แพร่กระจายไป ถึงจะเป็นการทำเพื่อแสดงให้เห็นว่าตัวเองดีกว่าฉันก็เถอะ แต่ยังไง\nพวกนั้นก็รับคำท้าฉันละนะ"

show shizu behind_blank_ss
with charachange

# ssh "I'm impressed. Well, for now. I would have to see how it plays out a little longer in order to know for sure."
ssh "ฉันประทับใจมาก เท่าที่เห็นน่ะนะ ยังไงก็ต้องรอดูอีกสักระยะให้แน่ใจว่าจะออกหัวหรือออกก้อย"

play sound sfx_snap

show shizu adjust_happy_ss
show mishashort perky_confused_ss:
    ease 0.1 ypos 1.05
    ease 0.1 ypos 1.1
with vpunch

# "She snaps her fingers suddenly, which sends Misha almost bolting out of her seat. Interesting, I guess it is impossible to get used to."
"อยู่ ๆ ชิซูเนะก็ดีดนิ้วจนมิช่าพุ่งตัวลุกจากที่นั่ง น่าสนใจดี ดังขนาดนี้ฟังกี่รอบก็คงไม่ชิน"

show shizu basic_happy_ss
with charachange

# ssh "That's right! We were going to have a party to celebrate passing the reins to the new Student Council, weren't we? Why not have that now? Or at least plan it now, and have it tomorrow."
ssh "จริงด้วย! เราจะจัดงานเลี้ยงฉลองที่ได้ส่งไม้ต่อให้สภานักเรียนรุ่นใหม่กันนี่ งั้นจัดตอนนี้เลยมั้ยล่ะ หรืออย่างน้อย\nจะวางแผนไว้ตอนนี้แล้วค่อยจัดวันพรุ่งนี้ดี"

# hi "But they're not even in charge yet. In fact, that's the first thing you told them: “You're not in charge yet.” It seems premature."
hi "แต่พวกนั้นยังไม่ได้เข้ามาเป็นเลยด้วยซ้ำนะ แล้วเธอก็บอกก่อนเลยด้วยว่า “พวกเธอยังไม่ได้เป็นสภานักเรียนนะ” จะจัดตอนนี้เลยก็ดูเร็วไปหน่อย"

show shizu adjust_frown_ss
with charachange

shi "…"

show shizu behind_blank_ss
with charachange

# ssh "Misha, what do you think?"
ssh "มิช่า เธอว่าไง"

show mishashort hips_smile_ss
with charachange

# mi "Hmmm~, I agree, it's too early. Plus~, I don't think I could go anyway. Sorry~! In fact, I was going to leave right now."
mi "อืมมม~ ฉันเห็นด้วยนะว่ายังเร็วไป อีกอย่าง~ ฉันน่าจะไปร่วมไม่ได้ด้วย ขอโทษทีนะ~! ที่จริงก็จะไปตอนนี้\nแล้วแหละ"

# ssh "Why not?"
ssh "ทำไมมาร่วมไม่ได้"

show mishashort hips_grin_ss
with charachange

# mi "No~ comment~!"
mi "โน~ คอมเมนต์~!"

show shizu adjust_frown_ss
with charachange

# ssh "Come on, tell me."
ssh "ไม่เอาน่า บอกฉันมา"

show mishashort perky_confused_ss
with charachange

# mi "Well… okay~!"
mi "เอ่อ… ก็ได้~!"

# "Way to not crack under pressure, Misha."
"ทนแรงกดดันได้ดีจริงเลยนะมิช่า"

show mishashort sign_confused_ss
with charachange

# mi "I thought about it, and~… Even if I didn't want to go, I would say yes~! Usually~. It's the kind of person I am. I really should stop doing that, and this is a good place to start, I think."
mi "ฉันไปคิดมาแล้ว แล้วก็~… ต่อให้ฉันไม่อยากไปฉันก็จะตอบตกลงอยู่ดี~! ปกตินะ~ ฉันเป็นคนแบบนั้นแหละ\nฉันต้องเลิกทำแบบนั้นสักที แล้วคราวนี้แหละคือจุดเริ่มต้นที่ดีเลย คิดว่านะ"

show mishashort perky_sad_ss
with charachange

# mi "If it's a celebration to say goodbye, I don't want it. It would be too sad~. I want to do something else instead. And after all, Hicchan, you and Shicchan will still be here tomorrow. It doesn't seem right."
mi "ต่อให้เป็นงานเลี้ยงอำลาฉันก็ไม่อยากร่วมหรอก คงเศร้าแย่เลย~ ฉันอยากทำอย่างอื่นมากกว่า แล้วยังไงเสีย พรุ่งนี้\nทั้งฮิจังกับชิจังก็ยังอยู่ จะจัดงานเลี้ยงแบบนั้นก็ยังไงอยู่"

show mishashort hips_grin_ss
with charachange

# mi "Besides, I have other school things I have to do today~! I can't drop them just like that."
mi "อีกอย่าง วันนี้ฉันมีธุระเรื่องโรงเรียนอย่างอื่นต้องไปจัดการอีก~! จะให้ทิ้งไปดื้อ ๆ เลยไม่ได้หรอก"

show shizu adjust_frown_ss
with charachange

# ssh "We can postpone it."
ssh "เลื่อนไปก่อนก็ได้นี่"

show mishashort hips_frown_ss
with charachange

# mi "No. No early goodbyes~!"
mi "ไม่ ไม่ลาล่วงหน้า~!"

# "She looks very firm as she says this."
"มิช่าพูดด้วยท่าทีหนักแน่น"

# hi "Aren't you going to go now, though?"
hi "แล้วไหนบอกจะไปแล้ว"

show mishashort hips_grin_ss
with charachange

# mi "Hm~? Oh, that's right~! Wahaha~!"
mi "หืม~ อ้อ จริงด้วย~! วะฮ่าฮ่า~!"

show mishashort perky_smile_ss at twoleft
with Dissolvemove(0.7)

show mishashort sign_smile_ss
with charachange

# mi "Okay, besides now, no too-early goodbyes, okay?"
mi "โอเค ไม่นับเรื่องเมื่อกี้ ไม่เอาการลาล่วงหน้านะ โอเคนะ"

show shizu behind_blank_ss
with charachange

# ssh "I get it."
ssh "เข้าใจแล้ว"

show mishashort hips_grin_ss
with charachange

# mi "Okay, later~!"
mi "โอเค เจอกัน~!"

stop music fadeout 4.0

hide mishashort
with charaexit

show bg school_council_ss:
    subpixel True
    center
    parallel:
        "bg school_council_ni" with Dissolve(5.0)
    parallel:
        ease 5.0 bgleft
show shizu behind_blank_ss:
    subpixel True
    parallel:
        "shizu behind_blank" with Dissolve(5.0, alpha=True)
    parallel:
        ease 5.0 xpos 0.5
with None

# "With that, it's just Shizune and me left alone in the student council room."
"แล้วในห้องสภานักเรียนแห่งนี้ก็เหลือเพียงชิซูเนะกับฉันอยู่ตามลำพัง"

play music music_dreamy fadein 4.0

with Pause(2.0)

# "Sunset slowly changes to night as we sit in silence, both searching for something to say."
"อาทิตย์อัสดงคล้อยต่ำเปลี่ยนเวลาผ่านเป็นกลางคืน พวกเราต่างนั่งกันเงียบ ๆ นึกหาเรื่องคุย"

show bg school_council_ni at bgleft
show shizu adjust_frown:
    center
    subpixel False ypos 1.1
with Dissolvemove(0.5)

# ssh "Would it really be that bad?"
ssh "มันไม่ดีขนาดนั้นเลยเหรอ"

# his "Yeah. I didn't think about it like that, but Misha's right. Parties set a mood, and it would be a sad one. A sad party doesn't sound like a whole lot of fun."
his "อืม ฉันก็ไม่เคยคิดมุมนั้นหรอก แต่มิช่าพูดถูกนะ งานเลี้ยงเป็นตัวกำหนดอารมณ์ ซึ่งอารมณ์ที่ว่าคือความเศร้าด้วย\nและงานเลี้ยงเศร้า ๆ ก็ฟังดูไม่ค่อยสนุกเท่าไหร่เลยนะ"

show shizu basic_angry
with charachange

# ssh "Why would it be sad?"
ssh "ทำไมถึงเศร้าล่ะ"

# "Is it a trick question? I'm sure of it. Shizune's eyes pierce into mine, waiting for my answer with a detached, analytical stare that I haven't seen in a while, but feels familiar anyway."
"ถามหยั่งเชิงหรือเปล่า ต้องใช่แน่ ๆ ชิซูเนะมองเข้ามาในตาฉันรอคำตอบด้วยสายตาเรียบนิ่งเพ่งพินิจที่ฉันไม่ได้เห็น\nมาสักพักแล้ว แต่ก็เป็นสายตาที่คุ้นเคยดี"

# "I consider my answer carefully, but also what it means for her to ask me."
"ฉันพิจารณาคำตอบอย่างถี่ถ้วนพลางคิดไปถึงเจตนาของชิซูเนะที่ถามด้วย"

# "It could be that Shizune finds it depressing as well. Or it could be that she doesn't understand why anyone would find it depressing. Both are equally plausible."
"อาจจะเพราะชิซูเนะเองก็เศร้าเหมือนกัน หรืออาจจะเพราะไม่เข้าใจว่าทำไมคนถึงคิดว่าเศร้า ทั้งสองทางดูจะเป็นไปได้\nเท่า ๆ กัน"

# his "I had a thought that when you graduate, that's it. It's going to be the end of the Student Council. I was wondering if you had the same idea."
his "ฉันมีความคิดพอเรียนจบแล้วก็คือจบกันเลย เป็นจุดจบของสภานักเรียนด้วย ฉันอยากรู้ว่าเธอคิดเหมือนกันหรือเปล่า"

show shizu behind_frown
with charachange

# ssh "Don't be stupid. I look forward to it. I won't be a student any more, so the expectations are going to be completely different. People's expectations of me, and my expectations about everything else. It seems exciting!"
ssh "ถามอะไรโง่ ๆ ฉันตั้งตาคอยจะตาย ฉันจะไม่ได้เป็นนักเรียนแล้ว ความคาดหวังอะไรก็จะเปลี่ยนไป ทั้ง\nความคาดหวังจากคนอื่นที่มีต่อฉัน ทั้งความคาดหวังจากฉันที่มีต่ออย่างอื่น น่าตื่นเต้นจะตายไป!"

show shizu adjust_frown
with charachange

# ssh "As for the Student Council, it should be in good enough hands. I don't have anything to be sad about."
ssh "ส่วนเรื่องสภานักเรียนฉันก็เห็นว่าน่าจะมั่นคงพอแล้ว ไม่ต้องมีอะไรให้เศร้าอีก"

# his "I don't think you're being honest. You looked upset about having to give the Student Council up not even a few weeks ago. It wasn't about leaving it to a bunch of newbies either, it was having to stop doing student council work at all."
his "ฉันว่าเธอไม่ได้รู้สึกแบบนั้นจริง ๆ หรอก เมื่อสองสามสัปดาห์ก่อนยังเห็นซึม ๆ ที่ต้องลาจากสภานักเรียนไป\nไม่ใช่เพราะต้องยกให้พวกหน้าใหม่ด้วย แต่เพราะจะไม่ได้ทำงานสภานักเรียนแล้วนี่แหละ"

show shizu behind_smile
with charachange

# "Unexpectedly, Shizune smiles."
"ฉันแปลกใจที่ชิซูเนะยิ้ม"

# his "So, you're not disagreeing."
his "ก็คือไม่เถียงสินะ"

# his "Then it doesn't make sense. Why would you want to have a party about it?"
his "งั้นก็ไม่เห็นจะสมเหตุสมผลเลย ทำไมเธอถึงอยากจัดงานเลี้ยงอำลาล่ะ"

show shizu basic_normal
with charachange

# ssh "I'm trying to get over it. Besides… Goodbye celebrations are very important. People say the first step is the most crucial, but following it through and finishing cleanly are just as important, right?"
ssh "ฉันก็ทำใจให้ลืมอยู่ อีกอย่าง… งานเลี้ยงอำลาน่ะสำคัญมากนะ คนชอบบอกว่าก้าวแรกนั้นสำคัญ แต่การทำ\nไปให้ตลอดรอดฝั่งและลงจอดอย่างสวยงามน่ะก็สำคัญเหมือนกันนะ ใช่มั้ย"

# his "I guess that is true."
his "ก็คงจริง"

show shizu adjust_smug
with charachange

# ssh "Anyway, I don't consider it goodbye. But it's still an event. You still have to go through the proper motions."
ssh "แต่นั่นแหละ ฉันไม่ได้มองว่าเป็นการอำลาหรอก ก็เป็นเหตุการณ์เหตุการณ์หนึ่งที่ยังต้องเคลื่อนไปตามรูปแบบ\nที่เหมาะสมเหมือนกัน"

show shizu behind_blank
with charachange

stop music fadeout 4.0

# ssh "Aren't you going to?"
ssh "แล้วนายจะอยู่เฉย ๆ เหรอ"

# his "Aren't I going to what?"
his "หมายถึงอะไร"

show shizu basic_normal
with charachange

# ssh "Kiss me, of course."
ssh "นายจะไม่จูบฉันเหรอ"

# his "Is that “the proper motions?”"
his "นี่เหรอ “การเคลื่อนไปตามรูปแบบที่เหมาะสม” ที่ว่า"

show shizu behind_blank
with charachange

# ssh "It would be normal, wouldn't it? The natural thing to do."
ssh "ก็ปกตินี่ ใช่มั้ย ต้องเป็นแบบนั้นอยู่แล้ว"

# "It's time to act decisively. If I don't, I'm sure my heart will explode."
"จะมามัวอ้ำอึ้งไม่ได้แล้ว ขืนชักช้าหัวใจฉันน่าจะระเบิดก่อน"

show shizu adjust_blush_close
with charachange

# "I kiss her immediately, so quickly that I don't even have time to enjoy it. Even though she was prepared for it, Shizune blushes a deep red. I feel a similar heat rising in my neck and cheeks."
"ฉันจูบชิซูเนะทันที เร็วจนฉันไม่ทันได้ลิ้มรสจูบเต็มที่ เธอหน้าแดงก่ำทั้งที่เตรียมใจไว้แล้ว ฉันรู้สึกว่าทั้งคอกับแก้มตัวเอง\nก็ร้อนผ่าวไม่ต่างกัน"

play music music_one fadein 4.0

scene evh shizu_undressing_clothed_stare
with whiteout

# "I move in for another kiss, but as I do so, she moves backwards at the same time and impishly jumps onto the cabinet behind her. Alone, in the total silence of the room, we just look at each other for a while."
"ฉันขยับเข้าไปจูบอีกครั้ง แต่ในขณะเดียวกันชิซูเนะก็ถอยแล้วปีนขึ้นไปอยู่ที่ตู้ข้างหลังอย่างซุกซน พวกเราซึ่งอยู่กัน\nตามลำพังในห้องเงียบสงัดแห่งนี้มองหน้ากันอยู่พักใหญ่"

show evh shizu_undressing_clothed_kiss
with charachange

# "This time, I kiss her more deeply. Her lips are light and dry, and open a tiny bit. I'm only able to appreciate the sensation for a moment before Shizune starts kissing me back forcefully."
"คราวนี้ฉันจูบชิซูเนะให้หนักหน่วงขึ้น ริมฝีปากเธอซึ่งไม่อวบอิ่มมากและแห้งกร้านเผยอออก ฉันดื่มด่ำกับสัมผัสนั้น\nได้ขณะหนึ่งก่อนที่ชิซูเนะจะจูบฉันกลับอย่างรุนแรง"

# "Her bangs brush against my closed eyelids as I let myself sink deeper into the kiss. I can feel the shape of her body through her clothes, which only makes me hold Shizune tighter."
"หน้าม้าชิซูเนะระอยู่กับเปลือกตาที่ปิดอยู่ของฉันผู้ซึ่งปล่อยให้ตัวเองจมจ่อมไปกับการจูบครั้งนี้ ฉันสัมผัสได้ถึง\nทรวดทรงของเธอที่อยู่ภายใต้เสื้อผ้าจนยิ่งอยากกอดให้แน่นขึ้นอีก"

show evh shizu_undressing_clothed_blush
with charachange

# "It takes some effort for the both of us to draw back from each other. We're both blushing, both from the kiss and thoughts of what's to come, and I'm far from the only one breathing a little heavier."
"เราต่างต้องห้ามใจอยู่พอสมควรกว่าจะผละจากกันได้ เราทั้งคู่หน้าแดงเหมือนกันจากการจูบกับสิ่งที่จะเกิดขึ้นต่อจากนี้\nและฉันก็ไม่ใช่คนเดียวที่หายใจหอบกว่าปกติเล็กน้อย"

# "As Shizune begins to take off my tie, I start undoing her blouse. It takes a while to figure it out. I'd never really thought about how our school's blouses work before."
"ฉันถอดเสื้อชิซูเนะออกไประหว่างที่เธอแกะเน็กไทฉัน ซึ่งต้องใช้เวลาสักพักกว่าจะถอดได้เพราะฉันไม่เคยคิดเลย\nว่าชุดนักเรียนหญิงจะใส่หรือถอดอย่างไร"

# "Shizune's blouse is a little tight on her, and her arms get stuck for a moment because of it. I find myself peeling it off of her, although with the way she's trying to wriggle out of it at the same time, it isn't easy. The sight is a little comical."
"เสื้อชิซูเนะคับเล็กน้อยจนแขนติดเสื้ออยู่ครู่หนึ่ง ฉันต้องถกเสื้อออกจากตัวให้โดยที่เธอสะบัดตัวให้หลุดไปพลาง\nนับว่าไม่ง่ายเลย เป็นภาพที่ดูชวนขันพิลึก"

play sound sfx_rustling

show evh shizu_undressing_unclothed_closed
with charachange

# "Once Shizune's arms are free, she slides out of her shirt, her skirt falling around her knees with it after she unhitches it and works it off her legs. The only thing covering her now are her bra and panties."
"พอชิซูเนะผลุบแขนออกจากเสื้อจนเป็นอิสระแล้วกระโปรงก็ร่วงไปอยู่ที่หัวเข่าหลังจากเธอปลดแล้วเขย่าขาออก ตอนนี้\nทั้งตัวเธอมีเพียงเสื้อชั้นในกับกางเกงในปกปิด"

# "Her figure is curvaceous and taut, and the healthy color of her skin contrasts with the black of her underwear. It's a wonderful sight, especially against the background of the moonlight through the window."
"รูปร่างโค้งเว้าของชิซูเนะดูเกร็ง ผิวอมชมพูตัดกับชั้นในสีดำ เป็นภาพที่งดงาม ยิ่งมีแสงจันทร์ที่ส่องลอดหน้าต่าง\nอาบด้วยแล้ว"

show evh shizu_undressing_unclothed_blush
with charachange

# "She looks at my chest and works the buttons of my shirt one by one. The process is greatly slowed by my hands moving up and down her thighs. It's a little amusing to play with her like this."
"ชิซูเนะมองหน้าอกฉันแล้วแกะกระดุมทีละเม็ด มือเธอแกะได้ช้ามากเพราะฉันลูบต้นขาเธออยู่ พอหยอกเล่นแบบนี้แล้ว\nก็สนุกเหมือนกัน"

show evh shizu_undressing_unclothed_kiss
with charachange

# "Eventually, finally, my shirt falls to the ground. Shizune surprises me by quickly pulling me in for a deep kiss without warning, but I quickly return the gesture."
"สุดท้าย ท้ายที่สุด เสื้อของฉันก็ร่วงผล็อยลงไปกับพื้นจนได้ ชิซูเนะดึงตัวฉันเข้าไปจูบโดยไม่ให้สัญญาณล่วงหน้า\nใด ๆ ทั้งสิ้นจนฉันตกใจ แต่ฉันก็รีบจูบกลับทันที"

show evh shizu_undressing_unclothed_talk
with charachange

# ssh "Why are you bolder today than on the roof?"
ssh "ทำไมวันนี้ถึงกล้ากว่าตอนอยู่บนดาดฟ้า"

# ssh "Or in your room?"
ssh "หรือตอนอยู่ที่ห้อง"

# "I try to think of a good answer, but it isn't easy. How would I be able to respond to that even if I could? There's no way to, unless I were to say that bureaucracy really puts me in the mood."
"ฉันเค้นหัวนึกหาคำตอบเหมาะ ๆ แต่ก็ไม่ง่ายเลย ต่อให้มีคำตอบแล้วจะตอบว่ายังไง ไม่ได้หรอก เว้นเสียแต่จะบอกว่า\nฉันมีอารมณ์กับการปกครองโดยอำนาจรัฐน่ะนะ"

# "My shirt having been disposed of, Shizune moves on to my belt, and I decide to help her undo it instead of answering her question. I don't think it would do much good to at this point."
"เมื่อถอดเสื้อแล้วชิซูเนะก็ย้ายมาจัดการที่เข็มขัดต่อ ฉันช่วยเธอปลดเข็มขัดแทนที่จะตอบคำถามนั้น ตอบไปตอนนี้\nก็คงไม่ได้อะไรขึ้นมาหรอก"

scene bg school_council_ni
with locationchange

# "It's not hard to get off, and falls to the ground with a metallic clunk. I move in for another kiss and begin to slide my hand up her side, but she suddenly lurches forwards, making me stumble backward."
"ซึ่งก็ถอดไม่ยาก กางเกงร่วงลงพร้อมเสียงโลหะที่กระทบกัน ฉันโน้มตัวเข้าไปจูบชิซูเนะอีกครั้งแล้วเลื่อนมือไปตามสีข้าง\nแต่เธอก็งอตัวจนฉันเสียสมดุลถอยออกมา"

# "The stiff edge of the table behind me was the furthest thing from my mind, until I feel it stabbing into my lower back. I hadn't even noticed it was there. It makes me grab Shizune a little tighter as we fall back onto the surface of the table."
"ฉันลืมไปเลยว่าข้างหลังฉันมีโต๊ะอยู่ มานึกก็ได้ตอนที่หลังไปชนเข้ากับขอบแข็ง ๆ นี่เอง ไม่ทันได้สังเกตด้วยซ้ำ\nพอเราสองคนล้มลงไปอยู่บนโต๊ะแล้วฉันก็กอดชิซูเนะให้แน่นขึ้นอีกเล็กน้อย"

label th_S35h:

show evh shizu_pushdown
with charachange

# "I hold back a sigh as Shizune victoriously holds herself above me. She's won again."
"ฉันห้ามใจตัวเองไม่ให้ถอนหายใจเมื่อชิซูเนะขึ้นคร่อมฉันอย่างมีชัย เธอชนะอีกแล้ว"

# "I'm distracted until Shizune's bra falls on me, seemingly like it dropped out of the sky. I end up laughing, despite how hard I try not to, and it's contagious enough that Shizune starts to as well."
"ฉันยังเหม่ออยู่จนกระทั่งเสื้อชั้นในชิซูเนะร่วงใส่หน้าฉันเหมือนร่วงจากฟ้า ฉันหัวเราะทั้งที่ฝืนกลั้นแล้ว และเธอ\nก็หัวเราะตามฉันไปด้วย"

# "Freed from her bra, her breasts are larger than I'd thought, even though they were noticeably large through her shirt already. She picks up her bra with her fingers and flicks it off as my hands move over her body."
"พอไม่มีเสื้อชั้นในมาบังแล้วก็เห็นว่าหน้าอกชิซูเนะนั้นใหญ่กว่าที่คิด ถึงปกติตอนใส่เสื้อจะดูใหญ่อยู่แล้วก็เถอะ เธอใช้นิ้ว\nเกี่ยวเสื้อชั้นในขึ้นมาแล้วโยนทิ้งไประหว่างที่มือฉันเลื่อนไปตามร่างกายเธอ"

# "Straddling me with her knees on the table, Shizune slips her underwear off, with my hands moving from her hips unconsciously to help her. I catch a glimpse of my watch. It's only been a few minutes, but it felt like so much longer."
"ชิซูเนะที่นั่งชันเข่าคร่อมฉันอยู่เลื่อนกางเกงในออก ฉันผละมือจากเอวเธอมาช่วยถอดโดยอัตโนมัติและเหลือบไปเห็น\nนาฬิกาข้อมือตัวเอง เพิ่งผ่านไปไม่กี่นาทีแต่รู้สึกเหมือนผ่านมานานมากแล้วเลยแฮะ"

# "She eases herself downwards, closer and closer until our bare chests are touching, her breasts feeling strange against the scar over my heart."
"เธอโน้มตัวเข้ามาหาฉันเรื่อย ๆ จนหน้าอกเปลือยเราแตะกัน สัมผัสจากหน้าอกเธอที่ถูกกับแผลเป็นตรงหน้าอกฉันนั้น\nแปลกดี"

window hide

show evh shizu_straddle_open
with whiteout

with Pause(7.0)

window show

# "When Shizune sits up, I feel myself slipping inside, slowly enveloped by her below as her breasts lift away from my torso. An attack from two fronts, I think dryly considering the situation. How like her."
"เมื่อชิซูเนะดึงตัวกลับขึ้นไปอยู่ท่านั่งแล้วก็รู้สึกได้ว่าตัวเองสอดใส่เข้าไปแล้ว ส่วนล่างของเธอโอบรับฉันไว้ช้า ๆ ทุกขณะ\nที่หน้าอกเธอเคลื่อนออกไปจากตัวฉัน โจมตีสองทางเลยเหรอ ฉันคิดได้อย่างใจเย็นทั้งที่อยู่ในสภาพนี้ สมเป็น\nชิซูเนะจริง ๆ"

show evh shizu_straddle_tease
with charachange

# ssh "I should just stop now, and leave you stewing in your lust."
ssh "หยุดแล้วปล่อยให้นายอารมณ์ค้างอยู่แบบนี้น่าจะดี"

# "She says, as she starts grinding herself against me, causing me to blink at the sudden pleasure. Very funny, Shizune. I soon lose track of my thoughts."
"เธอพูดก่อนจะบดเอวเข้ากับตัวฉันจนต้องหลับตาจากอารมณ์หวามไหวที่แล่นขึ้นมา ตลกมากชิซูเนะ ไม่นานฉันก็เริ่ม\nคิดอะไรไม่ออกแล้ว"

show evh shizu_straddle_closed
with charachange

# shi "…sss."
shi "…อึก"

# "Shizune bites her lip to muffle her voice from coming out. An unwanted voice. This is the most I've ever heard of it, and she blushes once she realizes she let it slip out."
"ชิซูเนะกัดปากตัวเองกลั้นเสียงที่ตัวเองไม่ต้องการไว้ เป็นครั้งแรกที่ฉันได้ยินเธอส่งเสียงมากขนาดนี้ และเธอก็แก้มแดง\nเมื่อรู้ตัวว่าปล่อยให้เสียงหลุดปากออกมา"

# "To cover it up, Shizune drives herself against me harder, causing me to jolt against her, driving my erection deeper into her."
"ชิซูเนะดันตัวเองลงมาแรงกว่าเดิมเป็นการกลบเกลื่อนจนฉันสะดุ้งแล้วดันความแข็งขืนเข้าไปลึกกว่าเก่า"

# "I thrust my hips towards her at the sudden sensation of movement, and Shizune fights against me, trying to pin me back down when I manage to pull my arms out from under me."
"ฉันยกเอวเข้าไปหาตัวชิซูเนะตอบสนองที่เธอขยับตัวแบบกะทันหันอย่างนั้น และชิซูเนะก็ไม่ยอมแล้วจับมือฉันกดไว้\nตอนที่ฉันดึงมือออกจากหลังมาได้แล้ว"

show evh shizu_straddle_smile
with charachange

# "In that moment, her hips thrust back with even greater force in response."
"จังหวะนั้นเธอตอบโต้ด้วยการโยกเอวลงมาแรงให้กว่าเดิม"

# "The sound of Shizune's soft, restrained moans, and the sight of her bountiful breasts moving up and down each time her hips buckle against mine, grow more arousing with time in the stillness of the student council room."
"เสียงครางอันอ่อนนุ่มของชิซูเนะที่เธอกลั้นไว้ ภาพอกอิ่มที่ขยับขึ้นลงทุกครั้งที่เอวเธอโยกเข้าออกกับตัวฉัน เหล่านี้\nยิ่งยั่วเย้าฉันไปทุกขณะในห้องสภานักเรียนอันสงัดงันแห่งนี้"

# shi "Mmphh…"
shi "อื้ม…"

# shi "…nn…"
shi "…อื้อ…"

# "I almost can't take it any more. The pleasurable sensations welling up between my legs, multiplied by the pressure of Shizune's weight on top of me, make it hard for me to think. My hips start bucking by themselves."
"ฉันแทบทนไม่ไหวแล้ว ความเสียวซ่านเอ่อขึ้นตรงบริเวณหว่างขาฉัน ซึ่งยิ่งทบขึ้นไปอีกหลายเท่าตัวด้วยน้ำหนัก\nของชิซูเนะที่กดทับจนสมองฉันแทบไม่ทำงานแล้ว เอวฉันขยับไปโดยอัตโนมัติ"

# "Shizune's hands push mine down onto the table. Every motion of hers is a push of some kind."
"ชิซูเนะจับมือฉันกดไว้กับโต๊ะ ทุกการขยับของเธอยิ่งเป็นการกดทับฉัน"

# "The table under us rattles under our combined weight. I doubt it would collapse, but the noise is really something."
"โต๊ะขยับจนเสียงดังตึงตังไปตามน้ำหนักตัวเราสองคน ยังไงก็คงไม่พังง่าย ๆ แต่เสียงดังมาก"

show evh shizu_straddle_come
with charachange

# "Not that Shizune notices. Her pace only grows faster, until it feels as though she might shove me across the table with how forceful she is being. Without warning, her movements come to a final crescendo."
"ซึ่งชิซูเนะไม่รู้หรอก เธอเพิ่มความเร็วขึ้นเรื่อย ๆ จนเหมือนตัวฉันจะโดนดันทะลุโต๊ะไปด้วยแรงขนาดนี้ และบทเพลง\nของเธอก็บรรเลงมาจนถึงช่วงสุดท้ายโดยไม่มีสัญญาณเตือนใด ๆ"

scene bg school_council_ni
with locationchange
with vpunch

# "Suddenly, she stops, almost falling onto me with enough speed that if she didn't catch herself, it would probably have knocked us unconscious. The worst situation possible, if someone happened to walk in while we were knocked out."
"อยู่ ๆ ชิซูเนะก็หยุดขยับแล้วล้มตัวลงกับฉันด้วยความเร็วชนิดที่ว่าถ้าเธอไม่ประคองตัวเองไว้แล้วฉันคงจะโดนกระแทก\nจนหมดสติไปได้ ซึ่งคงไม่ดีแน่หากมีคนมาเห็นตอนที่เราสลบกันอยู่"

# "I'm surprised, but not enough to forget that we're both naked and the sudden, painful interruption that just happened."
"ฉันตกใจ แต่ยังไม่ลืมว่าเราทั้งสองคนยังเปลือยอยู่ และยังไม่ลืมถึงจังหวะที่ชะงักไปจนเจ็บแบบกะทันหันเมื่อครู่นั้น"

# "Why did this have to happen? Was it intentional, to leave me stewing in my own lust? Shizune lets out her breath sheepishly, realizing it at the same time as I do."
"ทำไมถึงเป็นแบบนี้ไปได้ จงใจจะปล่อยให้ฉันอารมณ์ค้างเหรอ ชิซูเนะถอนหายใจอาย ๆ และเพิ่งรู้ตัวถึงการกระทำนั้น\nพร้อมกันกับตอนที่ฉันสังเกตเห็น"

show shizu behind_blank_nak
with charaenter

# ssh "Sorry, I tripped, or slipped, or something like that."
ssh "ขอโทษที ฉันสะดุด ลื่น หรืออะไรแบบนั้นแหละ"

# his "I had a thought, is the door unlocked?"
his "เพิ่งนึกอะไรด้ ประตูล็อกหรือยัง"

hide shizu
with charaexit

# "She quickly gets off the table and bolts over to check, and locks it, unlocks it, and locks it again, pulling on the knob just to make sure. When she's finally sure, she makes an out-of-place motion with her hands."
"ชิซูเนะรีบลงจากโต๊ะแล้วพุ่งไปดูประตูก่อนจะล็อก ปลดล็อก ล็อกอีกรอบ และบิดลูกบิดเพื่อความแน่ใจอีกครั้ง พอมั่นใจ\nจริง ๆ แล้วเธอก็ทำท่าที่ดูจะไม่เข้ากับสถานการณ์ขึ้นมา"

show shizu behind_smile_nak
with charaenter

# ssh "Safe!"
ssh "ปลอดภัย!"

# his "I'm glad you can take things so lightly."
his "เห็นเธอทำอะไรได้แบบไม่คิดมากแบบนี้แล้วฉันก็ดีใจ"

show shizu behind_frown_nak
with charachange

# ssh "I didn't do it on purpose. Why don't you take the lead, then?"
ssh "ฉันไม่ได้จงใจสักหน่อย งั้นทำไมนายไม่นำบ้างล่ะ"

show shizu behind_smilelow_nak
with charachange

# ssh "Come on."
ssh "มาสิ"

hide shizu
with charaexit

# "I grab Shizune by the shoulders and try to put her onto the table instead. Her brow scrunches in displeasure as the edge of the table pokes her in the back, just as it did to me. She opts to help herself up onto it."
"ฉันจับไหล่ชิซูเนะไว้แล้วดันให้นอนลงกับโต๊ะ เธอขมวดคิ้วด้วยความไม่สบายตัวตอนที่ขอบโต๊ะชนเข้ากับข้างหลัง\nเหมือนกับฉันเมื่อครู่แล้วเลือกที่จะขยับตัวขึ้นไปนอนอยู่บนโต๊ะเอง"

scene evh shizu_table_smile
with dissolve

# "This is also the first time I've seen Shizune lying down unclothed. The contours of her collarbone and breasts are beautiful, and my eyes follow them down to her shapely hips. A delicate hourglass figure."
"ครั้งนี้ยังเป็นครั้งแรกที่ฉันได้เห็นชิซูเนะนอนเปลือยเปล่า เส้นเงาตามกระดูกไหปลาร้ากับหน้าอกเธอนั้นช่างสวยงาม\nสายตาฉันมองไปตามสองสิ่งนั้นแล้วเลื่อนลงมาที่เอวได้รูป เป็นหุ่นทรงนาฬิกาทราบอันบอบบาง"

# "I run my hands along the curve of her body, from her shoulders on down."
"ฉันไล้นิ้วไปตามส่วนโค้งเว้าของร่างกายเธอไล่ตั้งแต่ไหล่ลงมา"

# "I slowly insert myself into Shizune up to the hilt. An intense warmth and tightness immediately surround me, and I start pistoning into her to pick up where we left off before."
"ฉันค่อย ๆ สอดใส่ตัวเองเข้าไปภายในชิซูเนะจนสุดทาง ความอุ่นกับความคับแน่นเข้าโอบล้อมทันทีก่อนฉันจะ\nขยับตัวเข้าออกเพื่อสานต่อจากการกระทำก่อนหน้า"

# "Her body feels so hot against my skin, each time our hips meet with each thrust, and where we're holding each other. I feel like I'll be scalded by her body heat."
"สัมผัสจากร่ายกายเธอที่ส่งผ่านผิวฉันมานั้นร้อนผ่าว ไม่ว่าจะตอนที่เอวเรากระทบกันหรือตอนที่เรากอดกัน\nอุณหภูมิร่างกายเธอสูงจนคล้ายจะเผาฉันได้"

# "On top of that, I feel more sensitive now than before, and find myself pushing into Shizune harder to make up for it."
"ยิ่งไปกว่านั้น ตอนนี้ฉันประสาทไวกว่าก่อนหน้านี้อีก ฉันต้องดันตัวเองให้เข้าไปลึกขึ้นเป็นการชดเชย"

scene evh shizu_table_normal
with charachange

# "My hand glides around the curve of her thigh and I carefully tease her with my hand as well, almost losing my balance when she reacts strongly, snapping upwards and back into my groin and nearly pushing us both to the floor."
"ฉันเลื่อนมือไปตามส่วนโค้งเว้าบนต้นขาเธอพลางใช้มือหยอกเย้าไปด้วย ชิซูเนะดิ้นตอบสนองอย่างรุนแรงจนฉันแทบ\nเสียสมดุล เธอขยับตัวขึ้นและลงมากระทบกับหว่างขาฉันจนเกือบล้มลงไปกับพื้นกันทั้งคู่"

# "Moving my hands up, I grab her prominent breasts and fondle them as I've always wanted to. They feel even larger than they appear, and overflow my hands, soft and perfectly shaped."
"ฉันขยับมือขึ้นมาจับเนินอกชิซูเนะแล้วบีบขยำอย่างที่นึกอยากมานานแล้ว พอได้จับแล้วก็ล้นมือ รู้สึกว่าใหญ่กว่า\nที่ตาเห็นอีก ทั้งนุ่มและทรงสวย"

# "She squirms under me as I flick my fingers over her nipples, and twists her arms around mine instead, gripping my fingers and drawing me closer. It feels like I'm wrestling her; the lock is inescapable."
"ชิซูเนะบิดตัวทุกครั้งที่ฉันใช้นิ้วเขี่ยส่วนยอดนั้น เธอใช้แขนโอบแขนฉันไว้แล้วจับมือดึงตัวฉันเข้ามา จับแน่น\nจนดิ้นไม่หลุดเหมือนกำลังเล่นมวยปล้ำกันอยู่เลย"

# "From the first time our hands met, I guess we were connected."
"เราคงเชื่อมถึงกันตั้งแต่ครั้งแรกที่จับมือกันแล้วละนะ"

# "Whether it's through her pulling me from one student council event to another, or holding hands as lovers, I think it's been the same, the confidence that comes across in the way she grasps my hand."
"ไม่ว่าจะตอนที่ชิซูเนะลากฉันจากงานสภานักเรียนหนึ่งไปอีกงานหนึ่ง ไม่ว่าจะตอนจับมือกันแบบคนรัก ฉันคิดว่า\nมีสิ่งหนึ่งที่ไม่เปลี่ยนไป นั่นคือความมั่นใจของเธอที่ส่งผ่านมาจากการจับมือ"

# "Her hands writhe across the surface of the table, and grabbing onto it, she hooks her legs around my back, pressing us closer together, connecting us even more closely and entrapping me inside her."
"ชิซูเนะบิดขยับมือไปทั่วพื้นที่โต๊ะก่อนจะจับขอบเอาไว้ เธอใช้ขาเกี่ยวเอวรั้งล็อกตัวฉันให้อยู่ภายในเธอและชิดเข้ามา\nจนเราเชื่อมสนิทถึงกันกว่าเดิม"

show evh shizu_table_comeopen
with charachange

# "Her inner walls are so hot and tight, and with her pushing up against me, the friction only increases, sending me over the top."
"พื้นผิวภายในเธอนั้นทั้งร้อนผ่าวและคับแน่น เมื่อชิซูเนะดันตัวเข้าหาฉันก็ยิ่งเพิ่มแรงเสียดสีขึ้นจนฉันไปถึงฝั่ง"

show evh shizu_table_comeclosed
with whiteout

stop music fadeout 4.0

# "All too soon, the feeling ends. All I can do afterwards is stay inside of her with my hands holding the table, both for lack of energy and because her legs are still locking me in. For Shizune's part, she smiles almost dreamily."
"เพียงชั่วขณะหนึ่งความรู้สึกนั้นก็หายไป พอเสร็จแล้วฉันได้แต่นิ่งอยู่ภายในเธอโดยที่จับมือวางไว้กับโต๊ะ ด้วยเพราะ\nทั้งเหนื่อยอ่อนกับทั้งขาเธอที่ยังโอบฉันไว้อยู่ ส่วนชิซูเนะยิ้มชวนฝันอยู่"

# "The sight makes me smile as well. Her legs slowly fall, allowing me to extract myself."
"เป็นภาพที่ชวนให้ฉันยิ้มตามไปด้วย ชิซูเนะค่อย ๆ ลดขาลงต่ำให้ฉันถอนตัวออกได้"

label th_S35x:

scene bg school_council_ni
with locationchange

# "Exhausted, I lean back against a desk and try to regain my breath before putting my clothes back on."
"ฉันพิงโต๊ะด้วยความหมดแรงพลางหายใจให้เต็มที่อีกครั้งก่อนจะใส่เสื้อผ้ากลับดังเดิม"

# "I notice a dull, hot throbbing in my chest as I button my shirt back up. It puts a bad aftertaste on everything that just happened."
"เมื่อติดกระดุมเสื้อก็สัมผัสได้ถึงใจที่เต้นตุบ ๆ อยู่อย่างร้อนผ่าว เป็นความรู้สึกปิดท้ายแด่เหตุการณ์ทั้งหลายก่อนหน้า\nที่ไม่ดีเลยเสียจริง"

show shizu behind_smile_nak
with charaenter

# ssh "It was a lucky break that Misha couldn't be here, wasn't it?"
ssh "โชคดีไปเนอะที่มิช่าอยู่ด้วยไม่ได้"

# his "You're in an unusually joking mood today."
his "วันนี้เธอพูดติดตลกผิดปกตินะ"

# his "I wonder what she had to do."
his "อยากรู้จังว่าติดธุระอะไร"

show shizu behind_blank_nak
with charachange

# "Shizune traces the air lazily with a finger and points to the door."
"ชิซูเนะลากนิ้วอยู่กลางอากาศอย่างเอื่อยเฉื่อยแล้วชี้ไปที่ประตู"

# ssh "Go see for yourself."
ssh "ไปดูเองสิ"

# his "Why don't you just tell me?"
his "ทำไมไม่บอกกันล่ะ"

show shizu behind_smile_nak
with charachange

# ssh "It's more interesting if you see for yourself. Seeing is believing."
ssh "ไปดูเองจะน่าสนใจกว่านะ สิบปากว่าไม่เท่าตาเห็น"

# his "Sure. Clever. Maybe I will. What about you, are you going to stay here all day? It's getting late."
his "ได้ พูดได้ดี ไว้จะไปดู แล้วเธอล่ะ จะอยู่ที่นี่ทั้งวันเลยหรือไง นี่ก็เริ่มค่ำแล้วนะ"

show shizu behind_blank_nak
with charachange

# ssh "It feels like my last day as Student Council president, so maybe I'll sleep here tonight. It could be the last chance I have to sleep at my desk, like after a long day trying to meet a deadline."
ssh "รู้สึกเหมือนวันนี้จะเป็นวันสุดท้ายที่จะได้เป็นประธานนักเรียนแล้วเลย ขอค้างคืนที่นี่แล้วกัน เป็นโอกาสสุดท้าย\nที่จะได้หลับที่โต๊ะตัวเองเหมือนอย่างที่ฉันทำเวลาอยู่ต้องทำงานยาว ๆ ให้ทันก่อนส่ง"

# his "That's weird."
his "พิลึกคน"

# his "I'll sleep in my bed."
his "เดี๋ยวฉันไปหลับที่เตียงตัวเองแล้วกัน"

# ssh "Sleeping sitting up is a skill. A very useful one."
ssh "การหลับตอนนั่งน่ะเป็นทักษะชนิดหนึ่งนะ เป็นทักษะที่มีประโยชน์มาก"

# his "Right."
his "โอเค"

scene bg school_lobby_ni
with locationchange

# "For a moment after I leave the room, I actually do consider seeing what Misha is up to, just because Shizune made it sound so secretive, as if she were building a time machine or something. But in the end I decide not to."
"พอออกจากห้องมาได้สักพักฉันก็ชั่งใจอีกทีว่าจะไปดูว่ามิช่าทำอะไรอยู่ดีไหม เพราะชิซูเนะบอกอย่างกับว่า\nเป็นความลับเหมือนกำลังสร้างไทม์แมชชีนหรืออะไรแบบนั้นอยู่เลย แต่สุดท้ายฉันก็ตัดใจไม่ไปดู"


#****************************

label th_S36:

scene bg school_courtyard_ni
with locationskip

# "The night air is pleasant at this time of year. It's refreshing and a little humid, but not so chilly as to make it uncomfortable to stay outside for a while. It's late enough for the courtyard to be all but deserted, too."
"ช่วงนี้ของทุกปีอากาศตอนกลางคืนนั้นจะเย็นสบาย สดชื่นและชื้นเล็กน้อย แต่ก็ไม่เย็นจนเมื่ออยู่ข้างนอกนาน ๆ\nแล้วหนาว ตอนนี้ก็ค่ำมากจนที่สวนไม่มีใครอยู่เลย"

# "After Shizune and I said our farewells to each other, I'd set out to return to my dormitory room. I didn't even make it all the way there, though, before getting distracted."
"พอฉันลาชิซูเนะมาแล้วฉันก็คิดจะกลับมาที่หอ แต่ยังเดินไปไม่ถึงด้วยซ้ำก็มีบางอย่างมากวนใจก่อน"

# "It doesn't seem like a bad idea to go see what Misha is up to. I have nothing better to do. No homework. I'm out of anything worth reading. On top of that, I simply want to know."
"ไปดูว่ามิช่าทำอะไรอยู่ก็น่าจะไม่เสียหายอะไร ยังไงก็ไม่มีอะไรทำอยู่แล้ว การบ้านก็ไม่มี หนังสือก็ไม่รู้จะอ่านอะไร\nยิ่งไปกว่านั้นคือฉันอยากรู้นี่แหละ"

scene bg school_lobby_ni
with locationchange

# "This isn't my first time being in the main building after hours, but usually, it's as I'm leaving the place with Shizune and Misha after a long day at the Student Council. Not entering it alone."
"ครัั้งนี้ไม่ใช่ครั้งแรกที่ฉันมาอยู่ในอาคารหลักนอกเวลาทำการ แต่ปกติฉันจะเดินออกมาพร้อมชิซูเนะกับมิช่า\nหลังทำงานสภานักเรียนกันยาว ๆ ไม่ใช่เข้ามาคนเดียวแบบนี้"

# "The atmosphere is quiet, a word I would not normally use to describe these halls. It's a little creepy. A light starts flickering up ahead. This seems like a horror movie moment waiting to happen."
"บรรยากาศนั้นเงียบ ซึ่งเป็นคำที่ปกติฉันจะไม่ใช่พูดถึงโถงทางเดิน ดูชวนขนหัวลุกหน่อย ๆ หลอดไฟเริ่มติด ๆ ดับ ๆ\nชักจะดูเหมือนฉากในหนังผีแล้วสิ"

play sound sfx_rustling
with vpunch

# "Feeling a hand on my shoulder, I stiffen reflexively."
"พอมีบางอย่างมาจับบ่าฉันก็ยืดตัวตรงแหน็วไปโดยอัตโนมัติ"

# "It's not Misha, or else there would be hands clamped over my eyes and a sing-song “guess who” accompanying them. So, who is it? I hope it's not Kenji, or at least that it's someone I know, or this will take a turn for the weird."
"ไม่ใช่มิช่า เพราะไม่งั้นคงมีมือมาปิดตาพร้อมคำพูดแบบใส่ทำนองว่า “ทายซิใครเอ่ย” แล้วใครกันล่ะ หวังว่าจะไม่ใช่\nเคนจินะ หรืออย่างน้อยก็ขอให้เป็นคนที่ฉันรู้จักเถอะ ไม่งั้นคงดูแปลก ๆ แน่"

show shizu invis_close at tworight
with None

show shizu behind_blank_close_ni at center
with dissolvecharamove

play music music_happiness fadein 4.0

# "Whoever it is quickly slips in front of me. It's Shizune."
"ใครคนนั้นผลุบตัวมาอยู่ตรงหน้าฉัน ชิซูเนะนี่เอง"

# hi "What are you doing here?"
hi "มาทำอะไรที่นี่"

# "I'm so relieved that I forget to sign it."
"ฉันโล่งใจเสียจนลืมทำภาษามือ"

show shizu adjust_frown_close_ni
with charachange

# "Shizune puts a finger up to her lips. I guess even though she can't hear, she has some idea of what loudness is, and can tell from my expression that I was being loud. And apparently, being loud isn't a good thing right now."
"ชิซูเนะยกนิ้วมาแตะที่ริมฝีปากตัวเอง ถึงจะไม่ได้ยินแต่ก็คงพอรู้สินะว่าความดังเบาคืออะไร และคงดูสีหน้าออก\nว่าฉันเสียงดังอยู่ ซึ่งดูเหมือนว่าการส่งเสียงดังตอนนี้จะไม่ใช่เรื่องดีเสียด้วย"

# "But then, why is Misha her interpreter?"
"แล้วทำไมมิช่าถึงมาเป็นล่ามให้ชิซูเนะล่ะ"

# his "Oh, very funny. Why are you here?"
his "โห ตลกมาก เธอมาที่นี่ทำไม"

show shizu basic_normal_close_ni
with charachange

# ssh "I was waiting for you to come see. I knew you would show up. It took you a while, though."
ssh "ฉันรอให้นายมาดูอยู่ ฉันรู้ว่านายจะต้องมา แต่ก็นานอยู่เหมือนกันนะเนี่ย"

# his "You've been waiting here?"
his "นี่เธอรออยู่ตรงนี้?"

show shizu behind_blank_close_ni
with charachange

# ssh "Yes, but that isn't important. We have to be stealthy, if we don't want Misha to detect us. Tell me if I'm not being stealthy enough, okay?"
ssh "ใช่ แต่เรื่องนั้นไม่สำคัญหรอก เราต้องแอบเข้าไป ไม่งั้นเดี๋ยวมิช่ารู้ว่าพวกเรามา ถ้าฉันไม่เนียนพอก็บอก\nหน่อยนะ"

show shizu basic_normal_close_ni
with charachange

# "With that, Shizune starts slowly tiptoeing through the middle of the hall. I pat her on the shoulder to get her attention."
"แล้วชิซูเนะก็เริ่มย่องข้ามผ่านโถงทางเดินไป ฉันแตะไหล่เธอเพื่อให้หันมา"

# his "That's not stealthy."
his "ไม่เนียนนะ"

# his "Why do we have to be stealthy?"
his "แล้วทำไมต้องทำตัวเนียนด้วย"

show shizu behind_frustrated_close_ni
with charachange

# "She refuses to answer, probably because signing and walking stealthily at the same time doesn't look easy."
"ชิซูเนะไม่ยอมตอบ คงเพราะการทำภาษามือไปพลางเดินแบบย่อง ๆ ไปพลางนั้นไม่ง่ายเท่าไหร่"

scene bg school_hallway3_ni
with locationskip

# "Before I know it, we're in front of our homeroom."
"รู้ตัวอีกทีพวกเราก็มาถึงที่ห้องเรียนประจำแล้ว"

stop music fadeout 0.5
play sound sfx_snap
with vpunch

# "Suddenly, a sound like the crack of a whip pierces the air, followed by a familiar expression of frustration."
"อยู่ ๆ ก็มีเสียงเหมือนแส้หวดผ่านอากาศ ตามมาด้วยน้ำเสียงที่ฟังดูเอือมระอา"

# "I'm sure a sound like that isn't good for my heart. Not to mention, everything sounds about a million times louder with how silent it is. It's coming from inside the room, and I sidle up to Shizune to get a look inside."
"ฉันมั่นใจว่าเสียงแบบนั้นไม่ดีต่อใจฉันแน่ ๆ แล้วยิ่งไม่ต้องพูดถึงว่าความเงียบยิ่งทำให้เสียงทุกอย่างดังขึ้นเป็นล้านเท่า\nเสียงเหล่านั้นดังมาจากในห้อง ฉันเดินเลียบ ๆ เคียง ๆ ตามชิซูเนะชะเง้อมองข้างใน"

scene ev misha_nightclass:
    center
    xpos 0.4
show ovl misha_nightclass_aperture at left
with silentwhiteout

play music music_comedy fadein 0.5

# mu "Can you stop throwing your pencil, please? How do you even throw a pencil that loudly?"
mu "เธอเลิกปาดินสอสักทีได้ไหม ครูขอร้องละ นี่ปายังไงให้เสียงดังได้ขนาดนั้น"

# ssh "He looks very flustered."
ssh "ครูดูหงุดหงิดมากเลยละ"

# "What an understatement. I sympathize with Mutou. I was able to hear Misha's pen break the sound barrier even through a wall and a thick classroom door. It probably blew out his eardrums and left an imprint on the wall."
"แค่คำว่าหงุดหงิดยังน้อยไป ฉันเข้าใจครูมาก ๆ ทั้งที่มีกำแพงกับประตูห้องเรียนหนา ๆ กั้นฉันยังได้ยินเสียงปากกามิช่า\nที่พุ่งผ่านกำแพงเสียงเลย สงสังคงทำแก้วหูครูแตกพร้อมทำกำแพงเป็นรอยไปแล้วมั้ง"

show ev misha_nightclass:
    ease 1.0 xpos 0.23 xanchor 0.0
show ovl misha_nightclass_aperture:
    ease 1.0 right
with None

# mi "I'm not throwing it~, when I get nervous, I like to spin it around, but~, then I forget I'm holding onto it, and—"
mi "หนูไม่ได้ปานะ~ พอหนูประหม่าหนูก็จะควงเล่น แต่~ หนูจะลืมว่าถือไว้ในมืออยู่แล้ว แล้วก็—"

# mu "It doesn't matter, either way, there shouldn't be pencils flying around. I get enough of that during regular school hours, I don't need it after hours."
mu "ช่างเรื่องนั้นเถอะ เรื่องคือมันไม่ควรมีดินสอพุ่งไปมาแบบนั้น แค่ตอนสอนตอนกลางวันครูก็เห็นจนเอือมแล้ว\nครูไม่อยากมาเห็นตอนค่ำอีก"

# mi "R-right~! Sorry."
mi "คะ ค่ะ~! ขอโทษค่ะ"

# mu "Whatever, just stop throwing, or releasing, or dropping things, please. Teachers have work, too."
mu "เอาเถอะ เลิกปา ปล่อย หรือทำอะไรตก ครูขอร้องละ ครูก็มีงานที่ต้องทำเหมือนกัน"

scene bg school_hallway3_ni
show shizu behind_blank_close_ni at center
with locationchange

# "I notice Shizune watching the same scene I am. Mutou is yelling at the top of his lungs, and Misha is being Misha."
"ฉันเห็นว่าชิซูเนะก็กำลังดูภาพเดียวกันกับฉันอยู่ ครูตะโกนสุดเสียง ส่วนมิช่าก็ทำตัวเป็นมิช่า"

# "I can hear them reasonably well through the door. But Shizune obviously can't hear anything at all. So, I wonder what watching this is like for her."
"ฉันได้ยินเสียงทั้งสองคนชัดพอสมควรแม้จะมีประตูกั้น แต่แน่นอนว่าชิซูเนะไม่ได้ยินอะไรเลย อยากรู้จัง\nว่าพอมาดูอะไรแบบนี้แล้วจะรู้สึกยังไงกันนะ"

# "She must know, since she understands well enough to want me to see it too, but I have to wonder if she ever feels like she's missing out on something, having to work that much harder to understand what she's observing."
"คงรู้แหละ เพราะเข้าใจจนถึงขั้นอยากให้ฉันมาดูด้วย แต่ก็ยังสงสัยอยู่ดีว่าจะรู้สึกเหมือนพลาดอะไรไปหรือเปล่าที่ต้อง\nตั้งสมาธิมากขนาดนั้นเพื่อทำความเข้าใจสิ่งที่ตัวเองกำลังสังเกตการณ์อยู่"

show shizu basic_normal_close_ni
with charachange

# ssh "It looks like she is taking supplementary lessons. Is she?"
ssh "เหมือนจะเรียนพิเศษอยู่ ใช่มั้ยนะ"

# his "Yeah."
his "อืม"

# "I answer, despite knowing the question is completely rhetorical."
"ฉันตอบทั้งที่รู้ดีว่าคำถามนั้นเป็นการถามลอย ๆ"

show shizu behind_smile_close_ni
with charachange

# ssh "Misha told me she really wants to be a sign language teacher in the future. If she can get a recommendation, she can study overseas for it. That is why she is working so hard. Her grades were always kind of on the low side."
ssh "มิช่าบอกว่าพอโตขึ้นแล้วอยากเป็นครูสอนภาษามือมาก ๆ ถ้าโรงเรียนมีจดหมายแนะนำตัวให้ก็ไปเรียนต่างประเทศ\nได้ด้วย นี่แหละมิช่าถึงได้ทุ่มเทหนักมาก เพราะผลการเรียนของมิช่าน่ะค่อนไปทางต่ำตลอดเลย"

# his "Now I feel guilty. I haven't even thought about what I'm going to do yet."
his "รู้สึกผิดขึ้นมาเลยแฮะ ฉันยังไม่ได้คิดเลยว่าจะไปทำอะไรต่อ"

show shizu adjust_smug_close_ni
with charachange

# ssh "Neither have I!"
ssh "ฉันก็เหมือนกัน!"

# "The cheerful way that she signs it is very unlike her, and is very obviously false."
"ท่าทีการส่งภาษามืออันร่าเริงนั้นไม่สมเป็นชิซูเนะเลย และชัดมากว่าไม่ได้เป็นความจริง"

show shizu basic_normal2_close_ni
with charachange

# ssh "Let's get out of here, we don't want to be seen. It would be a problem if we were caught standing out here like idiots."
ssh "ไปกันเถอะ เดี๋ยวมีคนมาเห็น ถ้าเขาเห็นเรายืนอยู่เหมือนคนบ้าสองคนแบบนี้คงไม่ดีแน่"

# his "Where? The student council room?"
his "ไปไหน ห้องสภานักเรียนเหรอ"

show shizu adjust_happy_close_ni
with charachange

stop music fadeout 3.0

show shizu invis_close at tworight
with dissolvecharamove

# "Shaking her head, she slips into the classroom across the hall instead."
"ชิซูเนะสั่นหัวแล้วเคลื่อนตัวไปยังห้องเรียนที่อยู่อีกฟากโถงทางเดิน"

scene bg school_room34_ni
with locationchange

# his "Great hiding place."
his "ที่ซ่อนเนียนดีนี่"

show shizu behind_blank_ni at center
with charaenter

# ssh "You're unusually sarcastic, lately. With the door closed it's a good one. Anyway, wasn't it interesting?"
ssh "ช่วงนี้นายประชดบ่อยผิดปกตินะ มีประตูปิดก็ใช้ได้แล้ว แล้วนายว่าน่าสนใจดีมั้ยล่ะ"

# his "Yes, but I'm not really surprised."
his "ก็น่าสนใจ แต่ไม่แปลกใจเท่าไหร่"

play sound sfx_doorclose

# see report
show shizu adjust_smug_ni at Position(ypos=1.1)
with dissolvecharamove

# "I close the door behind us, prompting Shizune to laugh soundlessly as she slides into a chair. For a second, it depresses me. I want to hear her real laugh."
"ฉันเดินเข้ามาแล้วปิดประตู ชิซูเนะหัวเราะอยู่เงียบ ๆ พลางนั่งลงกับเก้าอี้ ฉันนึกหดหู่อยู่แวบหนึ่งเพราะอยากได้ยิน\nเสียงหัวเราะจริง ๆ ของเธอ"

show shizu behind_smile_ni
with charachange

play music music_innocence fadein 10.0

# ssh "I was. I've been looking down on Misha. I didn't think she had a goal at all. But it turns out that I was wrong, I made a careless assumption. I thought Misha was as aimless as I was. I was stupid. I lost."
ssh "ฉันแปลกใจนะ เพราะฉันเอาแต่ดูถูกมิช่า คิดว่าเป็นคนไม่มีเป้าหมาย แต่กลายเป็นว่าฉันคิดผิด สมมติอะไร\nแบบส่งเดชไปอย่างนั้น ฉันคิดว่ามิช่าเป็นคนไร้เป้าหมายเหมือน ๆ กับฉัน ฉันมันโง่ ฉันแพ้แล้ว"

show shizu basic_normal_close_ni
with charachange

# "Shizune pauses to crack her knuckles, then folds her hands over each other, and leans forward in her chair. In the abnormal quiet of the building, I can hear Mutou yelling at Misha again even across a hallway and through two doors."
"ชิซูเนะเว้นช่วงหักข้อนิ้วตัวเองแล้ววางมือทับกันโน้มตัวเข้าหาโต๊ะ ฉันได้ยินเสียงครูตะคอกใส่มิช่าอีกรอบอยู่ในอาคาร\nที่เงียบผิดปกติอย่างนี้ทั้งที่อยู่อีกฟากของโถงทางเดินและมีประตูกั้นอยู่สองบาน"

# "Shizune's eyes are locked on mine, unblinking behind the gleaming lenses of her glasses, observing my reaction to her words."
"ชิซูเนะจ้องตาฉัน นัยน์ตาประกายแสงเบื้องหลังเลนส์แว่นตานั้นสังเกตปฏิกิริยาฉันที่มีต่อคำบอกเล่าของเธอ"

# "This is a test. Her opinion of people is rarely formed from how they respond to questions; it's how they respond to statements that counts."
"สิ่งนี้คือแบบทดสอบ ชิซูเนะแทบไม่ได้มองคนจากปฏิกิริยาที่มีต่อคำถาม แต่มองจากปฏิกิริยาที่มีต่อประโยค\nเป็นส่วนใหญ่"

# "In hindsight, it makes sense. Shizune's inability to speak, as well as just her personality in general, means that anything she “says” is a big commitment on her part. Everything."
"พอย้อนนึกดูแล้วก็สมเหตุสมผลอยู่ เนื่องจากชิซูเนะพูดไม่ได้กับทั้งด้วยนิสัยของเจ้าตัว ทำให้ทุกสิ่งที่ “พูด” นั้น\nคือสิ่งสำคัญสำหรับเธอ ทุกอย่างเลย"

# "For that reason, I sometimes doubt she says anything without a hidden agenda behind it."
"และเพราะอย่างนี้เองบางครั้งฉันก็นึกเคลือบแคลงว่าสิ่งที่ชิซูเนะพูดนั้นมีเจตนาแอบแฝงอะไรหรือเปล่า"

# "That sounds remarkably paranoid. Even Kenji would think so. Unfortunately, I'm so caught up in thinking about it that I forget to give her an answer. She takes it as there not being one. There was an invisible time limit to this test, shorter than usual."
"ฟังดูเป็นคนขี้ระแวงเอามาก ๆ แม้แต่เคนจิก็คงรู้สึกแบบนั้น โชคไม่ดีที่ฉันมัวแต่คิดถึงประโยคนั้นจนลืมให้คำตอบ\nกับชิซูเนะไป เธอถือเอาว่าฉันไม่มีคำตอบให้ แบบทดสอบนั้นมีตัวจับเวลาล่องหนอยู่ ซึ่งคราวนี้ให้เวลาน้อยกว่าปกติ"

show shizu adjust_smug_close_ni
with charachange

# ssh "Just as I thought."
ssh "ว่าแล้วเชียว"

# his "What do you mean?"
his "หมายความว่ายังไง"

show shizu behind_blank_close_ni
with charachange

# ssh "You don't agree?"
ssh "นายไม่เห็นด้วยเหรอ"

# his "Not really, it's not that. I don't get it."
his "ก็ไม่เชิง ไม่ใช่แบบนั้นหรอก ฉันแค่ไม่เข้าใจ"

show shizu basic_normal2_close_ni
with charachange

# ssh "I want to force my will on people."
ssh "ฉันอยากให้คนอื่นทำอะไรตามใจฉัน"

# "How refreshingly honest."
"ซื่อตรงได้อย่างแปลกใหม่เหลือเกิน"

show shizu behind_frown_close_ni
with charachange

# ssh "Don't give me a weird look like that. It's not like that was always my intention."
ssh "อย่ามองฉันแปลก ๆ อย่างนั้นสิ ฉันก็ไม่ได้มีเจตนาแบบนั้นตลอดสักหน่อย"

show shizu basic_normal_close_ni
with charachange

# ssh "At first, I was just bored. I wanted to see someone's passion for something. Then I could try and beat them. I wanted to test their ability or their convictions."
ssh "ทีแรกฉันก็แค่เบื่อ ฉันอยากเห็นคนที่มีใจรักกับการทำอะไรบางอย่างแล้วก็จะได้ลองเอาชนะ ฉันอยากทดสอบ\nฝีมือหรือไม่ก็ความมุมานะของคนที่ว่านั้น"

show shizu adjust_frown_close_ni
with charachange

# ssh "But it was impossible, no one has any passion for anything in this school. They just want to keep to themselves."
ssh "แต่ก็ทำแบบนั้นไม่ได้ ในโรงเรียนนี้ไม่มีใครมีใจรักกับการทำอะไรเลย ทุกคนต่างอยากเก็บแรงขับนั้นไว้กับตัว"

show shizu behind_frustrated_close_ni
with charachange

# ssh "I can't believe it. It's too boring that way. I thought that there was no way these drab people could be for real. It goes beyond not wanting to make waves."
ssh "ไม่อยากจะเชื่อเลย แบบนั้นก็น่าเบื่อเกินไปสิ ฉันเคยคิดว่าคนเรามันคงไม่จืดชืดได้ถึงขนาดนั้นจริง ๆ หรอก\nคงไม่ใช่แค่ว่าอยากอยู่เฉย ๆ ไม่ไปวุ่นวายกับอะไร"

show shizu adjust_angry_close_ni
with charachange

# ssh "They had to have some interests. They had to be hiding something. I wanted to expose it, and reveal it, and drag it out."
ssh "ต้องมีสิ่งที่สนใจสิ ต้องซ่อนอะไรอยู่แน่ ๆ ฉันอยากดึงผ้าคลุมออกมา เปิดมันออกมา ลากมันออกมา"

show shizu behind_blank_close_ni
with charachange

# ssh "One of the most successful ways to get people to open up to you, and cheer them up, is to open up with a story about yourself. And then you ease them into telling you about themselves."
ssh "วิธีหนึ่งที่ทำให้คนอื่นเปิดใจกับเราแล้วให้กำลังใจได้ดีที่สุดคือเริ่มจากการเปิดใจด้วยเรื่องราวของตัวเราเองก่อน\nแล้วก็ค่อย ๆ ให้เขาเปิดใจเล่าเรื่องตัวเองบ้าง"

show shizu adjust_happy_close_ni
with charachange

# ssh "It's like give and take, but with an element of manipulation, which makes it interesting."
ssh "เหมือนการให้กับการรับน่ะแหละ เพียงแต่อันนี้สอดไส้การชักใยที่ทำให้น่าสนใจขึ้นมาด้วย"

show shizu behind_blank_close_ni
with charachange

# ssh "I can't do that. If I attempt to have Misha talk about me, for me, it makes me seem arrogant. The message has to go through a messenger. I'm standing next to Misha, telling her to tell someone about me."
ssh "ฉันทำแบบนั้นไม่ได้ ถ้าฉันจะลองให้มิช่าเล่าเรื่องของฉันแทนฉันก็จะรู้สึกว่าตัวเองน่ะอวดดี สารต้องส่งผ่าน\nคนส่งสาร แล้วฉันมายืนอยู่ข้างมิช่าบอกให้มิช่าบอกคนอื่นถึงเรื่องของฉัน"

show shizu adjust_frown_close_ni
with charachange

# ssh "You don't have to be able to read sign language to see that. If I were forced to sit through that, I would think I was arrogant, too."
ssh "ไม่ต้องอ่านภาษามือออกก็ดูออก ถ้าฉันต้องจำใจมานั่งฟังฉันก็จะคิดว่าฉันน่ะอวดดีเหมือนกัน"

show shizu basic_angry_close_ni
with charachange

# ssh "I was frustrated; I couldn't figure out a way to have a conversation with anyone but Misha. No one would open up to me."
ssh "ฉันหงุดหงิดเพราะนอกจากมิช่าแล้วฉันก็ไม่รู้จะคุยกับคนอื่นยังไงดี ไม่มีใครยอมเปิดใจให้ฉันเลย"

show shizu behind_frown_close_ni
with charachange

# ssh "I came to the conclusion that I can't make people confide in me, or believe in me. I can only hope to create things, and show them to people, and hope they make them happy. Or I could be more forceful and hope it would eventually stick to someone."
ssh "จนฉันก็สรุปเอาว่าฉันคงทำให้คนอื่นไว้ใจฉันไม่ได้ ที่ฉันจะทำได้ก็มีแค่สร้างสิ่งหนึ่ง เอาสิ่งนั้นไปให้คนอื่นดู แล้วก็\nหวังว่าพวกเขาจะมีความสุข หรือฉันจะยัดเยียดให้มากกว่านั้นแล้วหวังว่าสักวันคนจะประทับใจ"

# "I guess that would be me. Feels vaguely depressing."
"ก็คงจะเป็นฉันนั่นแหละ รู้สึกหดหู่ขึ้นมาหน่อย ๆ แฮะ"

show shizu basic_normal_close_ni
with charachange

# ssh "Somewhere along the line, I think I started to ignore Misha, or see her as less of a person, or something like that. I took her for granted, I think would be the best way to put it. It was like she was just an extension of myself."
ssh "แล้วฉันว่าระหว่างนั้นฉันเริ่มเมินมิช่าไป ไม่ได้มองเป็นคนคนหนึ่ง หรืออะไรแบบนั้น ฉันไม่ได้มองมิช่าให้จริงจัง\nใช้คำนี้น่าจะดีที่สุด เหมือนว่ามิช่าเป็นแค่ส่วนเสริมของตัวฉัน"

show shizu behind_sad_close_ni
with charachange

# ssh "I forgot that the whole time, Misha was there, opening up to me, and giving a hundred percent every day."
ssh "ฉันลืมไปว่ามิช่าอยู่เคียงข้างฉันเปิดใจให้ฉันแบบเต็มร้อยเสมอมา"

show shizu basic_angry_close_ni at center
with Dissolvemove(0.7)

# ssh "I missed what I was looking for, because it was in plain sight. How stupid of me. I really did become arrogant. That's why I've lost. I'm more shortsighted than I was back then. I went in reverse."
ssh "ฉันคลาดกับสิ่งที่ฉันกำลังมองหาเพราะเป็นสิ่งที่เห็นกันจะจะตา ฉันมันโง่ กลายเป็นคนอวดดีไปจริง ๆ เพราะอย่างนี้\nฉันถึงได้แพ้ ฉันไม่ได้เป็นคนมองการณ์ไกลอย่างแต่ก่อน ความคิดฉันกลับด้านไป"

# "She's pacing back and forth now, almost brooding, yet still filled with so much energy that she can't stand to stop moving."
"ชิซูเนะโยกตัวไปมาด้วยท่าทีหมอง ๆ ทว่ายังมีแรงเหลือมากจนอดอยู่นิ่ง ๆ ไม่ได้"

# "If you got her to hold two wires I'm sure Shizune could power a light bulb. It's odd that I could have such a lighthearted thought while she's being so serious."
"ถ้าเอาสายไฟสองเส้นให้ชิซูเนะจับแล้วคงเอามาต่อให้หลอดไฟติดได้ แปลกดีที่ฉันคิดอะไรเพลิน ๆ แบบนี้ได้ทั้งที่เธอ\nกำลังจริงจังอยู่"

show shizu adjust_frown_close_ni
with charachange

# ssh "And in spite of that, Misha tells me that I'm her inspiration. Isn't that ridiculous? I'm not the kind of person who can inspire others."
ssh "ถึงอย่างนั้นมิช่าก็ยังบอกฉันว่าฉันคือแรงบันดาลใจของเธอ บ้าดีเนอะ ฉันไม่ใช่คนที่จะไปเป็นแรงบันดาลใจให้ใคร\nได้เลย"

show shizu behind_blank_close_ni
with charachange

# ssh "Even if a person who inspires you is flawed, it can be acceptable. I've thought about this. There is even acceptable hypocrisy."
ssh "เรายังรับได้ต่อให้คนที่เป็นแรงบันดาลใจให้เรานั้นจะมีข้อเสีย ฉันไปลองคิดมาแล้วนะ ความย้อนแย้งบางอย่าง\nเราก็รับได้"

show shizu basic_normal2_close_ni
with charachange

# ssh "For instance… If your hero was an athlete, but unsportsmanlike, they could still be respected for their athletic ability, even if they had shortcomings as a person."
ssh "ยกตัวอย่างเช่น… ถ้าพระเอกของเราเป็นนักกีฬาแต่ไม่มีน้ำใจนักกีฬา คนจะยังนับถือทักษะทางด้านกีฬา\nของคนนั้น ต่อให้จะมีนิสัยเสียก็ตาม"

play sound sfx_snap
show shizu adjust_angry_close_ni
with charachange

# ssh "However,"
ssh "แต่ว่า"

# "She snaps her fingers briskly. It sounds like a thunderclap in the empty room, and Shizune takes a few seconds to stretch her fingers. Come to think of it, this is the most she has ever signed."
"ชิซูเนะดีดนิ้วรุนแรงจนฟังดูคล้ายมีฟ้าผ่าในห้องอันว่างเปล่าแห่งนี้ก่อนจะพักเหยียดนิ้วอยู่ครู่หนึ่ง จะว่าไปแล้ว ครั้งนี้\nเป็นครั้งแรกเลยที่เธอทำภาษามือเยอะขนาดนี้"

show shizu cross_angry_close_ni
with charachange

# ssh "If someone like me has no goals, it would be totally unacceptable. It'd be the worst kind of hypocrisy. And hypocrites don't deserve responsibility over anything, they can't even manage themselves."
ssh "การที่คนอย่างฉันไม่มีเป้าหมายน่ะเป็นสิ่งที่ยอมรับไม่ได้หรอกนะ เป็นความย้อนแย้งแบบสุดกู่ และคนย้อนแย้ง\nก็ไม่สมควรจะมีหน้าที่รับผิดชอบอะไรเพราะแม้แต่จะจัดการตัวเองยังทำไม่ได้"

# "How incredibly pessimistic. It makes me angry to think about it."
"มองโลกในแง่ลบเสียจริง คิดตามแล้วก็โมโห"

# "I would hate myself just a few months ago. This must be how I looked to others."
"ถ้าเป็นสองสามเดือนก่อนฉันคงเกลียดตัวเองไปแล้ว คนอื่นคงมองฉันเป็นแบบนี้สินะ"

# "And, funny enough, it was Shizune and Misha who convinced me to stop. Without them I'm sure things would be much different, and not for the better. "
"ซึ่งก็ตลกดีที่ชิซูเนะกับมิช่าเป็นคนทำให้ฉันเลิกทำตัวแบบนั้นได้ ถ้าไม่ได้สองคนนี้ฉันคิดว่าอะไรหลายอย่าง\nคงต่างไปจากตอนนี้มาก ๆ และไม่ได้ต่างไปในทางที่ดีด้วย"

# "Lately, I feel as though we pass around our miseries as much as we're supported by each other, but I think it just comes with the territory of having friends and being close to someone."
"ช่วงนี้ฉันรู้สึกว่าเราต่างก็ส่งต่อความสิ้นหวังของกันและกันไปพอ ๆ กันกับการหนุนกันและกัน แต่ฉันว่าสุดท้ายมันก็คือ\nเรื่องของการมีเพื่อนกับการได้สนิทกับใครสักคนนั่นแหละ"

# his "You're the leader anyway."
his "แต่เธอก็เป็นผู้นำนี่"

show shizu behind_frown_close_ni
with charachange

# ssh "That is only because no one else wants to be."
ssh "เพราะไม่มีใครอยากเป็นหรอก"

# his "But that means you still are, since people are putting their trust in you anyway. In fact, doesn't that make it more important?"
his "แต่ก็แปลว่าเธอยังเป็นผู้นำอยู่ เพราะคนอื่นก็ยังวางใจให้เธอรับหน้าที่นี้ ซึ่งที่จริง แบบนี้มันก็ยิ่งสำคัญเลย\nไม่ใช่เหรอ"

# his "Either way, you are the leader, you are the inspirational figure or whatever you want to call it. You're responsible for what you tame."
his "แต่จะยังไงก็เถอะ เธอคือผู้นำ เป็นผู้ซึ่งเป็นแรงบันดาลใจให้ผู้คนหรืออะไรแล้วแต่เธอจะเรียก เธอจะต้องรับผิดชอบ\nต่อทุกสิ่งที่เธอมีความสัมพันธ์ด้วย"

# his "I read that in a book somewhere."
his "ฉันเคยอ่านเจอจากที่ไหนสักที่น่ะ"

show shizu basic_normal_close_ni
with charachange

# ssh "That's clever."
ssh "คมดีนะ"

# "Shizune only seems to show what she's feeling on her face when she wants to, but I don't think she's being sarcastic."
"ชิซูเนะเหมือนจะแสดงอารมณ์ผ่านสีหน้าได้ก็ต่อเมื่ออยากจะแสดงให้เห็นเท่านั้น แต่ฉันคิดว่าเธอคงไม่ได้ประชดหรอก"

show shizu adjust_frown_close_ni
with charachange

# ssh "I don't want to “tame” anyone, though."
ssh "แต่ฉันไม่ได้อยาก “มีความสัมพันธ์” กับใครขนาดนั้นนะ"

# his "Being the leader and being looked up to, then. Same thing."
his "งั้นก็เปลี่ยนเป็นการเป็นผู้นำให้คนนับถือแล้วกัน เหมือน ๆ กันนั่นแหละ"

show shizu behind_frustrated_close_ni
with charachange

# ssh "I never wanted to be the leader, it just ends up that way."
ssh "ฉันไม่ได้อยากเป็นผู้นำเลย แค่ปล่อยไปตามน้ำแล้วมันมาลงเอยเอง"

# his "I don't believe that, all you do is try to grab more and more responsibility."
his "ไม่เชื่อหรอก เธอก็เอาแต่คว้าภาระมาใส่ตัวเรื่อย ๆ"

show shizu adjust_frown_close_ni
with charachange

# ssh "Wait, wait. I wasn't going to tell you that I don't enjoy it. I don't care about being the leader, but I don't mind. I don't care about being the best, but I don't mind. You're right, though, about me wanting responsibility."
ssh "เดี๋ยว ๆ ฉันไม่ได้บอกว่าฉันไม่ชอบ ฉันไม่ได้สนใจการเป็นผู้นำก็จริง แต่ฉันก็ไม่ถือเหมือนกัน ฉันไม่ได้สนใจ\nการเป็นที่หนึ่ง แต่ฉันก็ไม่ถือเหมือนกัน แต่ถูกของนายที่ว่าฉันอยากได้ภาระน่ะ"

show shizu basic_happy_close_ni
with charachange

# ssh "Of course I want more responsibility. Having responsibility makes me feel alive. That's why I joined the Student Council: If there is no pressure, I just can't stand it."
ssh "แน่ละว่าฉันอยากรับภาระให้มากขึ้น การมีหน้าที่ที่ต้องรับผิดชอบน่ะทำให้ฉันรู้สึกกระปรี้กระเปร่าขึ้นมา\nนี่แหละฉันถึงได้มาเป็นสมาชิกสภานักเรียน ถ้าไม่มีแรงกดดันอะไรเลยฉันก็อยู่เฉยไม่ได้หรอก"

show shizu behind_blank_close_ni
with charachange

# ssh "Even so, now I'm the leader. I always thought being the leader meant you give orders, but it really is more."
ssh "ถึงอย่างนั้นตอนนี้ฉันก็มาเป็นผู้นำ ฉันเคยคิดมาตลอดว่าผู้นำคือคนสั่ง แต่จริง ๆ แล้วมันมีอะไรมากกว่านั้น"

show shizu adjust_frown_close_ni
with charachange

# ssh "It's about having a goal. If I don't have a goal, then it's pointless. People would only be following me for my own enjoyment. It would be selfish."
ssh "สิ่งสำคัญคือการมีเป้าหมาย ถ้าฉันไม่มีเป้าหมายก็เปล่าประโยชน์ สิ่งที่คนจะทำตามฉันก็มีแค่สิ่งที่เป็นความอยาก\nของตัวฉันเอง ซึ่งเป็นอะไรที่เห็นแก่ตัวมาก"

# "It's a strangely moral viewpoint for a person who seems to love one-upping others so much."
"เป็นมุมมองของคนที่ชอบเอาชนะคนอื่นที่มีศีลธรรมมากพิลึก"

show shizu basic_normal2_close_ni
with charachange

# "Resting her chin on her tented fingers, Shizune looks disarmingly childish as she thinks hard about her problem. The expression on her face is a little comical, because it's too obvious, and therefore, very unlike her."
"ภาพที่ชิซูเนะเอาคางเกยนิ้วที่มาประกบกันพลางขบคิดถึงปัญหาตัวเองนั้นดูเป็นเด็กไร้พิษภัยใด ๆ สีหน้าเธอ\nดูตลกเล็กน้อยเพราะเป็นสีหน้าที่ชัดเจนมากจนไม่สมกับเป็นชิซูเนะ"

# his "It comes with the job. I think you'd have to be a leader. You wouldn't be satisfied with anything else, you would just get bored."
his "มันก็มาพร้อมกับภาระหน้าที่นั่นแหละ ฉันว่ายังไงเธอก็ต้องเป็นผู้นำ เพราะไม่งั้นเธอจะเป็นอะไรก็คงไม่พอใจ\nเพราะจะเบื่อก่อน"

show shizu basic_frown_close_ni
with charachange

# "Shizune doesn't reply, but from her annoyed expression, I think I've guessed correctly."
"ชิซูเนะไม่ตอบ แต่เดาจากสีหน้าหงุดหงิดนั้นแล้วฉันคงเดาถูกสินะ"

# his "I've been thinking that I need a little direction, too."
his "ฉันก็คิด ๆ อยู่ว่าฉันเองก็ควรมีทิศทางชีวิตบ้าง"

show shizu adjust_happy_close_ni
with charachange

# ssh "Were you told that it's important to contribute to society?"
ssh "มีคนบอกนายเหรอว่านายต้องทำตัวให้เป็นประโยชน์กับสังคมน่ะ"

# "What an unusual response. It's so out of nowhere that I don't know how to respond. And it also bothers me, though I don't know why. Possibly because it doesn't seem like something that would come from her."
"ตอบได้แปลกจริง เป็นประโยคที่มาแบบลอย ๆ จนฉันไม่รู้จะตอบยังไงดี และไม่รู้ว่าทำไมฉันถึงข้องใจกับประโยคนั้นนัก\nอาจจะเพราะเป็นอะไรที่ฉันไม่คิดว่าชิซูเนะจะเป็นคนบอกมั้ง"

# "So I start to think that it isn't Shizune's thought at all. I wonder who told her that. Well, it was probably her dad. But there is a chance that she came up with it on her own. If so, would it be because she can't hear?"
"ฉันเลยเริ่มคิดว่าหรือจริง ๆ แล้วจะไม่ใช่ความคิดของเจ้าตัวเลย ใครบอกมากันนะ ก็นะ คงเป็นพ่อละมั้ง แต่ก็\nมีโอกาสเหมือนกันที่เธอจะเป็นคนคิดเอง ถ้างั้นก็เป็นเพราะชิซูเนะฟังอะไรไม่ได้เหรอ"

# his "Why do you say that?"
his "ทำไมถึงบอกแบบนั้น"

show shizu behind_blank_close_ni
with charachange

# ssh "Just because."
ssh "ก็อยาก"

# his "I don't believe it."
his "ไม่เชื่อ"

# his "I guess that's right, though."
his "แต่ก็คงจริงละนะ"

show shizu basic_normal_close_ni
with charachange

# ssh "I see."
ssh "อย่างนี้นี่เอง"

show shizu adjust_frown_close_ni
with charachange

# ssh "I don't know if it's the same for me. I hate it."
ssh "ฉันก็ไม่รู้ว่าฉันเป็นแบบนั้นเหมือนกันหรือเปล่า ไม่ชอบเลย"

# "I think everyone wants a purpose. Looking back, it makes sense that Shizune doesn't have one. All that energy would otherwise have been directed at something."
"ฉันคิดว่าคนเราต่างก็ต้องการจุดมุ่งหมาย พอมองย้อนไปแล้ว การที่ชิซูเนะไม่มีจุดมุ่งหมายเลยนั้นก็สมเหตุสมผล\nไม่อย่างนั้นพลังทั้งหมดของเธอก็คงถูกนำไปทุ่มให้กับอะไรบางอย่างแล้ว"

# "Since she had nothing to channel it towards, Shizune lashed out in all directions. Reminds me of a downed power line flailing in a storm: Furious and incandescent, but aimless and dangerous. Just like Shizune."
"และเพราะไม่มีบางอย่างให้ทุ่มใส่ ชิซูเนะจึงปล่อยพลังทั้งหมดไปคนละทิศละทาง ฉันนึกถึงสายไฟที่ขาดแล้วสะบัดอยู่\nท่ามกลางพายุ รุนแรงและสว่างวาบทว่าไร้ทิศทางและอันตรายเหมือนอย่างชิซูเนะ"

# "I want to say that this is why she feels the need to turn everything into a competition, but… that's probably just how she is. Having a goal to put that energy towards is just the next level."
"ก็อยากจะคิดต่อไปอยู่หรอกว่าเพราะแบบนี้ชิซูเนะถึงได้อยากทำให้ทุกอย่างกลายเป็นการแข่งขัน แต่ว่า… เธออาจจะ\nเป็นแบบนี้อยู่แล้วก็ได้ การมีเป้าหมายให้ทุ่มเทก็เป็นแค่ขั้นถัดไปจากนั้น"

show shizu behind_blank_close_ni
with charachange

# ssh "How about this? I could go into business. My family is well connected, so it shouldn't be too hard. …That comes off sounding a little unethical and nepotistic, doesn't it?" 
ssh "งั้นแบบนี้เป็นไง ฉันจะทำธุรกิจ ครอบครัวฉันก็มีเส้นสาย น่าจะทำได้ไม่ยากมาก …ฟังดูไม่ซื่อตรงเลยเนอะ รับฝาก\nโดยเส้นสายอะไรแบบนี้ ว่ามั้ย"

# his "A little."
his "นิดหน่อย"

show shizu adjust_frown_close_ni
with charachange

# ssh "I won't coast, though. I'll work hard, until I'm at the very apex."
ssh "แต่ฉันจะไม่ทำแบบหยิบหย่งหรอก ฉันจะทุ่มสุดตัวจนกว่าจะไปถึงจุดสูงสุด"

# ssh "When I have as much money as possible, so much that it'll be like I won't know what to do with it, I'll move on to the next step. After sitting on it for a while, of course, like a fairy tale dragon."
ssh "พอฉันมีเงินเยอะมาก ๆ แบบสุดกำลังเท่าที่จะหาได้แล้ว—เยอะแบบไม่รู้จะเอาไปทำอะไรดี—ฉันก็จะขยับไป\nขั้นถัดไป แต่แน่นอนว่าต้องอยู่นิ่ง ๆ สักพักก่อนเหมือนอย่างมังกรในเทพนิยาย"

# his "You want to be…?"
his "เธออยากเป็น…?"

show shizu basic_happy_close_ni
with charachange

# ssh "A philanthropist!"
ssh "นักการกุศล!"

hi "…"

show shizu adjust_smug_close_ni
with charachange

# ssh "Tsk tsk. What were you thinking? That I want to be a miser?"
ssh "ชิ ๆ นี่นายคิดอะไรอยู่ คิดว่าฉันจะเป็นพวกโกยแล้วไม่แบ่งเหรอ"

show shizu behind_blank_close_ni
with charachange

# ssh "Well, it's true, it is a part of the plan. Don't sell me short and stop there, though."
ssh "ก็จริง ตรงนั้นคือส่วนหนึ่งของแผนเหมือนกัน แต่อย่าดูถูกกันแล้วคิดว่าฉันจะหยุดแค่ตรงนั้นนะ"

stop music fadeout 8.0

# "Shizune still looks uneasy. Of course; even if she did seem to resolve her problem quickly, no one can get over their anxieties that fast. No one can solve their problems that easily."
"ชิซูเนะยังดูไม่สบายใจ แน่ละว่าดูจะคลี่คลายปัญหาของตัวเองได้เร็วจริง แต่ก็ไม่มีใครหรอกที่จะหายวิตกได้เร็วขนาดนั้น\nไม่มีใครที่จะแก้ปัญหาของตัวเองได้ง่ายขนาดนั้น"

# "The important thing is, it looks as though she has her heart set on trying. It's still hard to tell whether that drive of hers comes from a good or bad place."
"ทว่าสิ่งสำคัญคือดูท่าว่าชิซูเนะจะยังตั้งใจพยายามต่อไป ฉันยังดูไม่ออกว่าต้นทางแรงขับเคลื่อนของเธอนั้นเป็นแหล่งที่ดี\nหรือไม่ดี"

# "But she has something to hold on to now. I can genuinely believe that she does. I'm happy for her. And at the same time, I feel a little cold. I'm the one who's behind. Now, I'm the only one without a goal."
"แต่ตอนนี้ชิซูเนะก็มีีอะไรให้ยึดเหนี่ยวแล้ว ฉันเชื่อได้อย่างสนิทใจ ดีใจแทนจริง ๆ และในขณะเดียวกันก็รู้สึกเย็นเยียบ\nขึ้นมาหน่อย ๆ ฉันยังรั้งท้ายอยู่ ตอนนี้เหลือแค่ฉันแล้วที่ยังไม่มีเป้าหมาย"

$ suppress_window_after_timeskip = True

scene black
with dissolve

#****************************
    
label th_S37:

window hide None
nvl clear

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_daily fadein 0.5

scene bg school_dormhisao_bw
with dissolve

nvl show dissolve

# n "\n\n\n\n\n\n\n\n\n\There haven't been any further disruptions since that week."
n ""

nvl clear

# n "\nOf course, that's what I thought the week before that. And Shizune and Misha's sudden, newfound clarity had left me feeling a little lost and envious. I thought there was no way I could rest easy at the time."
n ""

# n "But fortunately, nothing came of my worries. Then before I knew it, there was enough to deal with in school that I even managed to put them off my mind. And still, everything was fine."
n ""

# n "I was wrong. I'd seen Shizune and Misha's carefully hidden vulnerabilities; but they were still strong."
n ""

# n "Now, we're going to be graduating soon. I've grown so comfortable here that it kind of crept up on me. When it did, I felt sad and didn't want to think about it. So, I didn't. Not until recently."
n ""

# n "About a week ago, I started making a list of people I thought I should say goodbye to before graduation. The first rule I laid out for myself was that I would try not to write them down in any kind of special order, like least important to most important."
n ""

# n "Somehow, it ended up like that anyway, even though it also ended up being a shorter list than I expected it to be. Kenji is somewhere in the middle."
n ""

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

scene bg school_dormhisao
show kenji neutral at center
with locationchange

window show

# ke "They said I would have to graduate eventually. Well, I showed them. I've lived here rent free for more than long enough. If you take into account the rising cost of land, I think you could say I've won in the end."
ke ""

show kenji happy
with charachange

# ke "No, you know what? I did win. History will acknowledge me as the victor."
ke ""

# hi "The victor of what?"
hi ""

# ke "I managed to stay out of sight, and slip through the cracks. I beat the system."
ke ""

# hi "If you put it that way, it sounds like you just ran away from the system."
hi ""

# ke "Sometimes, running is the greatest form of victory; like in the Olympics."
ke ""

# "I'm too tired to argue with him. Who's he kidding? Everyone knows the shot put is the best Olympic event, in any case."
""

# hi "So, what you're basically saying is, you won't miss it?"
hi ""

show kenji neutral
with charachange

# ke "Miss what?"
ke ""

# hi "School, dummy."
hi ""

show kenji tsun
with charachange

# ke "No. I told you, this place is too filled with feminists. It's beyond saving. But at least I'll be able to get out before it reaches critical mass. I'll only come back, years later, when they build a statue to honor me."
ke ""

# hi "Do they do the ten year later reunion thing here?"
hi ""

show kenji neutral
with charachange

# ke "How would I know that? Probably. Anyway, I have to start packing now. Take care of yourself, man."
ke ""

# hi "You should have packed a week ago, like I did."
hi ""

# "Not that I had much to pack."
""

show kenji tsun
with charachange

# ke "That's not how it goes. You're supposed to do everything at the last minute. Men are better at doing everything at the last minute, the last minute can have more productivity than like, the entire week before it. It's how we keep shit fair."
ke ""

show kenji neutral
with charachange

# ke "Pffft, you'll never understand our manly ways."
ke ""

# hi "You take care of yourself, too."
hi ""

show kenji happy
with charachange

show kenji invis at right
with dissolvecharamove

play sound sfx_doorslam

hide kenji
with vpunch

# "With a salute, he shoots backwards through the door, slamming it shut behind him hard enough that the entire dorm probably heard it. I've noticed that a lot of people slam doors here. Maybe it's a local thing."
""

# "“Take care of myself.” It's the first time I've heard him say it. Usually he ends our conversations with something like, “seeya.” “I'll pay you back later, man.” Well, he was a little annoying sometimes, but I'll miss him. I cross him off my list mentally."
""

# "The list is very short now, and I once again discard the notion of going through it in any kind of order. Like I said, I never had that intention."
""

scene bg school_dormhallway
with locationchange

# "So, I go out to look for Shizune and Misha. I can only think of one place they could be. The student council room, of course."
""

play ambient sfx_crowd_indoors fadein 2.0

scene bg school_lobby
show crowd
with locationskip

# "Turning the corner, I almost bump into a small group of students. For a second, a bitter feeling flashes through me, since for all I know, that could have been fatal."
""

# "It's the new Student Council. There aren't a lot of them, but a lot more than three. Which is good, since it means there's enough of them that they can each have their own title."
""

# "It would have been cool if I could have had a little desk plaque with my name and title on it. I don't think they do that now, or ever did, unfortunately."
""

# "The new Student Council surrounds me while I'm thinking. If anyone were looking at this from afar, it would be a pretty sinister sight."
""

# "Maybe they have come to finally get back on me for calling them “the new Student Council” all those times. I was just translating for Shizune, but I guess I should have been less lazy and more tactful. I regret nothing."
""

# "I find myself being thanked for “everything I've done.”"
""

# "I'm being thanked. This should make me happy, considering how often I would think to myself that being in the Student Council was a completely thankless job. It does make me happy, but I can't enjoy it fully."
""

$ renpy.music.set_volume(0.5, 1.0, channel="music")
$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

window hide
nvl clear
nvl show dissolve

# n "\n\nI wonder how things would have turned out if our Student Council had grown as large as the one that's set to replace us."
n ""

# n "Even though they've only got two or three other members, it's enough that they have set roles. Not like us, where Shizune seemed to be the president, but that was it."
n ""

# n "The new council thanking me gives me a strange feeling. It's like coming back home and seeing that a tree you nurtured years before has grown. But I feel like I didn't nurture that tree enough. I wonder what more I could have done."
n ""

# n "It would likely make Shizune furious that I would feel distant from what I did in the Student Council this way, or that I'd imply I didn't do enough, but it's true. I was only following her."
n ""

# n "\nSo, in a way, I also feel like I'm viewing that same tree from far away. As if I'm seeing it from the window of a train as it passes by."
n ""

$ renpy.music.set_volume(1.0, 1.0, channel="music")
$ renpy.music.set_volume(1.0, 1.0, channel="ambient")
stop music fadeout 4.0

nvl hide dissolve
nvl clear
window show

# "I indulged in these thoughts for too long. When I snap out of it, I realize that I'm still standing there, surrounded by the new Student Council. I do the only thing I can do, and apologize for zoning out. Then, I thank them back."
""

stop ambient fadeout 0.5

scene bg school_council
with locationchange

play music music_normal fadein 3.0

# "When they walk away, I enter the student council room, which looks a lot messier, but seems to have gained a computer."
""
#the have a computer, it's just really crappy
#i remember making a cutin for it

# "It makes sense; I recall hearing one of the clipboard girls talking about her plans to use a computer to make all the boring data entry Shizune does more tolerable."
""

# "I can't remember which one said it, though. Aoi seems to be the more ambitious one, but then again, Keiko appears more serious. Well, it doesn't matter now."
""

# "I'm not alone in the room, but instead of finding Shizune here like I expected, it's just Misha. She's sitting on Shizune's desk, like Shizune herself often does, swinging her legs back and forth."
""

show mishashort invis:
    center
    ypos 1.2
with None

show mishashort hips_grin at center
with  Dissolvemove(0.5)

# "When our eyes meet, she hops off and inexplicably poses like a superhero."
""

# mi "Hi, Hicchan~! I'm surprised to see you here~!"
mi ""

# hi "What are you doing?"
hi ""

show mishashort cross_smile
with charachange

# mi "You first~."
mi ""

# hi "I was looking for Shizune."
hi ""

show mishashort cross_grin
with charachange

# mi "Me, too~! I thought she would be here, but I got Hicchan instead~!"
mi ""

# hi "Gee, thanks."
hi ""

show mishashort sign_smile
with charachange

# mi "Wahaha! Well~, this is good. Really, really~. I wanted to talk to you, anyway~."
mi ""

# hi "About what?"
hi ""

# "I take the time to glance around the room a little more. I see a hot plate. They are really living high."
""

show mishashort perky_sad
with charachange

# mi "I wanted to say sorry~, of course~, for all the trouble I made for you and Shicchan."
mi ""

# hi "Don't call it “trouble.”"
hi ""

show mishashort sign_confused
with charachange

# mi "Right~, right~."
mi ""

# hi "Don't apologize to Shizune."
hi ""

show mishashort hips_smile
with charachange

# mi "Ahaha~. Right~, right~. But that isn't why I'm here, Hicchan. I wouldn't apologize to Shicchan. Since you're here, I want to ask you a question."
mi ""

show mishashort perky_confused
with charachange

# mi "Hicchan, what do you think it would take for Shicchan to be happy?"
mi ""

# hi "World domination, obviously."
hi ""

show mishashort cross_laugh
with charachange

# mi "Wahaha~!"
mi ""

show mishashort hips_smile
with charachange

# mi "Even though you're joking, Hicchan~… No, even if she could, it wouldn't make Shicchan happy. Only for a little while."
mi ""

show mishashort sign_smile
with charachange

# mi "Hicchan, have you ever heard of artists who tear up their paintings as soon as they finish them? Such people really exist in the world, you know~!"
mi ""

show mishashort perky_smile
with charachange

# mi "I remembered it all of a sudden. It's just like Shicchan, now that I think about it. Whenever Shicchan sets up a challenge for herself and completes it, she acts like her skills have no meaning any more."
mi ""

show mishashort perky_confused
with charachange

# mi "I wonder~, is it because she can't create anything permanent?"
mi ""

show mishashort perky_sad
with charachange

# mi "It's just like those artists, and how they want to create a piece of art to leave behind~, a really great one~, but can't do it. It's really obvious when I look back at it~, but~, I didn't see it before. Now, I'm scared. I wonder if Shicchan will ever be happy."
mi ""

# hi "No, I don't think so. Not about her ever being happy. I think you're wrong. Shizune is actually happy more often than I'd thought."
hi ""

# hi "I think it's actually kind of amazing. Usually, people don't think about that kind of stuff until they're middle aged or dying. Then they think “I want to leave something behind” or “I want to be remembered.”"
hi ""

# "Like me."
""

# "Only I skipped ahead a little. My life was short, and seemed even shorter after my heart attack."
""

# "I didn't think about what I was leaving behind, because I very quickly thought there was almost nothing I was leaving behind. So all that was left was for me to stew in my own bitterness."
""

# hi "Shizune already wants to leave her mark somewhere. But she wants to do it by helping people. That's why celebrations are so important to her. She even wants to be a philanthropist."
hi ""

# hi "I think it's the best way to live, living on by what you give to others. Even if it's for a selfish reason, that's okay, too."
hi ""

# hi "Shizune is already happy, because if something goes well, there will always be someone else to see it and remember it. That's what makes her happy."
hi ""

# "Misha sighs, arms stiff at her sides, hands tapping the air softly."
""

show mishashort sign_sad
with charachange

# mi "Before, I still thought… hm~… I might be able to make Shizune happy; and I was in a good place to do it before. Since I was her interpreter, I could always be with her. Maybe…"
mi ""

show mishashort perky_confused
with charachange

# mi "And~, I thought I would do it by becoming like… Shicchan's shadow."
mi ""

show mishashort perky_sad
with charachange

# mi "I kept trying even when she rejected me. It felt like I was stuck and I couldn't do anything but watch Shicchan's back getting smaller while she kept going. I was scared, even though I should have just accepted it."
mi ""

# mi "It's hard. Maybe I could have at least understood Shicchan~."
mi ""

show mishashort cross_smile
with charachange

# mi "But it looks like I was completely wrong after all~… I didn't even know that, or think about it… Shicchan would call it a complete loss."
mi ""

show mishashort cross_frown
with charachange

# mi "Okay~, I'm done. That's it, Hicchan~. But~! Since you're the one who knows Shicchan best of all, you can't make her cry. Or I'll be angry~!"
mi ""

show mishashort hips_smile
with charachange

# mi "I'm going to go overseas after this. I even have letters of recommendation, or I don't think I would be able to normally~! Maybe I'll study and become a sign language teacher over there? Who knows~!"
mi ""

show mishashort hips_grin
with charachange

# mi "That means~! You have to look after Shicchan, okay?"
mi ""

stop music fadeout 8.0

# "Misha's smile is as honest as ever, but she's obviously changed. The look in her eyes is that of a much more attentive girl. It seems to be true that hardship builds wisdom. It reminds me of the look in Shizune's eyes."
""

# "I wonder what Shizune might have been through to have become who she is. I can take a guess. Or maybe she was always like that. I want to see her even more, and suggest to Misha that we should look for her together."
""

# "Of course, it's just a pretext to spend more time with a friend. It's strange how it hasn't been long since we last hung out together, the three of us, in the span of a routine student council day. Yet, it seems like it was long ago."
""

# "Thinking about the future can put that kind of lens over the past."
""

# "Speaking of lenses…"
""

scene bg school_courtyard at bgleft
show yuuko neutral_up at center
with locationskip

play music music_ease fadein 8.0

# "Outside, Yuuko is standing around, fiddling with a tiny, modern-looking camera in her hands. It would be unnoticeable if it weren't metallic enough to reflect the sunlight. Misha calls out to her. I thought we were supposed to be looking for Shizune."
""

show yuuko neutral_up at tworight
show bg school_courtyard at center
with charamove

show mishashort hips_grin at twoleft
with charaenter

# mi "Hi~ hi~!"
mi ""

show mishashort cross_smile
with charachange

# mi "What are you doing~?"
mi ""

show yuuko closedhappy_down
with charachange

# yu "I'm just taking photos of everyone."
yu ""

show mishashort hips_grin
with charachange

# mi "That's obvious~!"
mi ""

# "Awkward. Misha, I'll never forget how you taught me that someone can hold so many secrets, and still have a massive lack of tact."
""

# hi "Where's my photo?"
hi ""

show yuuko worried_up
with charachange

# yu "Y-you want a copy? I… don't know. Well… Only if you promise to keep it a secret, or else everyone will want one too."
yu ""

show mishashort cross_smile
with charachange

# mi "That happened to me in elementary school, only it was with candy~!"
mi ""

show yuuko smile_up
with charachange

# yu "Okay… I'll take a photo of you now, then…"
yu ""

# hi "Ah, wait, I'm not ready. I was just kidding."
hi ""

show mishashort sign_smile
with charachange

# mi "Hicchan, make a peace sign~!"
mi ""

# hi "I'm not going to do that."
hi ""

play sound sfx_camera
with cameraflash

# "The camera flash goes off, blinding me."
""

show mishashort perky_confused
show yuuko worried_down
with charachange

# "Yuuko shields herself behind it, letting out a moan of frustration. You're not supposed to turn the flash on outdoors."
""

show yuuko invis at right
with dissolvecharamove

# "She starts apologizing unnecessarily, and then quietly slips away."
""

# hi "Ah, wait."
hi ""

show yuuko worried_up at tworight
with dissolvecharamove

# yu "Yes?"
yu ""

show mishashort sign_smile
with charachange

# mi "Did you see Shicchan around here~?"
mi ""

show yuuko neutral_up
with charachange

# yu "Yes… In front of the gate."
yu ""

# hi "Thanks."
hi ""

# "I can barely get it out before I have to start following behind Misha."
""

play ambient sfx_crowd_outdoors fadein 3.0

scene bg school_gate
show crowd at center
show shizu behind_blank at center
with locationskip

# "Fortunately, not for very long. The gate is barely a minute's walk from here, even though even that can be tiring for me sometimes. We see Shizune with the Student Council; they're probably thanking her too."
""

$ renpy.music.set_volume(0.3, 1.0, channel="ambient")

show shizu adjust_frown
with charachange

hide crowd
with charaexit

# "As soon as she sees us, she shoos them away. Which is very easy, since I doubt any of them can understand sign language or use it, so they're not too sad about leaving."
""

# "Which in turn makes me wonder why they would thank her without someone who can, but it's the thought that counts."
""

show mishashort invis at twoleft behind shizu
with None

show mishashort hips_grin:
   xpos 0.36
show shizu adjust_blush
with Dissolvemove(0.4)

show bg school_gate at bgright
show mishashort perky_smile at twoleft
show shizu behind_smile at tworight
with dissolvecharamove

# "Misha immediately hugs Shizune, and then leans against the gate, next to her. I, on the other hand, decide to hang back a little, and let them talk. After all, Misha wanted to talk to Shizune this whole time. I can wait."
""

show bg school_gate at right
show shizu invis:
    xpos 0.4
show mishashort invis:
    xpos 0.0
with dissolvecharamove

# "I even turn away, so I don't “eavesdrop” on their conversation."
""

# "I end up losing track of the time."
""

# "When I look at my watch, it's already been ten minutes. I wonder if they're done, and turn around to find them behind me."
""

show bg school_gate at bgright
show mishashort perky_smile at twoleft
show shizu behind_blank at tworight
with dissolvecharamove

# ssh "What are you thinking about?"
ssh ""

# hi "Boring philosophical things that I don't want to talk about. Don't worry, I'm not thinking about it too hard."
hi ""

show shizu adjust_smug
with charachange

# ssh "Good. Getting philosophical at a time like this would be the worst thing you could do."
ssh ""

# hi "Yeah. I just want to stand here for a bit. It's relaxing."
hi ""

show mishashort hips_grin
with charachange

# mi "Wahaha~! It was~ a busy week."
mi ""

# hi "Not really, not for me."
hi ""

$ renpy.music.set_volume(0.5, 1.0, channel="music")
$ renpy.music.set_volume(0.1, 1.0, channel="ambient")

window hide
nvl clear
nvl show dissolve

# n "\n\n\n\nI know that they must have been busy. But I think I know what I want to do now, and when it hit me, I didn't feel particularly fired up, or anxious."
n ""

# n "It is the opposite. I feel at peace for the first time in a long time, and I want to savor that feeling a little more."
n ""

# n "\nI think that I want to teach here."
n ""

# n "\nAs soon as I thought this, a long, winding road appeared in my mind. An uncertain road, that leads back here."
n ""

nvl clear

# n "\n\n\n\nI wonder if I'll be able to meet someone in the future like me. Someone filled with bitterness."
n ""

# n "I want to talk to that person, since I can't talk to myself. I want to tell them that life is too short; something that couldn't be told to me, only shown. I want to do it without pity."
n ""

# n "If I had been pitied, I'm sure that I'd have only died a little more. When I think about that first week, I still think about how well it went. So well that it could only be called the result of kindness. I feel like I want to show others the same kindness."
n ""

# n "\nAnd I also want to keep chasing Shizune."
n ""

$ renpy.music.set_volume(1.0, 1.0, channel="music")
$ renpy.music.set_volume(0.3, 1.0, channel="ambient")

nvl hide dissolve
nvl clear

show mishashort perky_smile
with charachange

window show

# mi "What did the new Student Council want, Shicchan~?"
mi ""

# "It's hard to daydream when you have to deal with Misha's voice."
""

# hi "I didn't know that they had someone who knew sign language."
hi ""

show shizu behind_smile
with charachange

# ssh "They don't. I think it was most likely just a goodbye, so I appreciate it, even though I couldn't tell them."
ssh ""

show shizu basic_normal
with charachange

# ssh "How did you know I was here?"
ssh ""

# hi "Is it supposed to be a secret? Anyway, we just asked Yuuko. Did she take a photo of you, too?"
hi ""

show shizu behind_blank
with charachange

# ssh "Yes, without asking me first. Since Yuuko doing anything spur-of-the-moment is rare, though, I'll let it go."
ssh ""

play sound sfx_snap
show shizu basic_sparkle
with charachange

# "She snaps her fingers, more because I think she likes it, than out of realization of an idea."
""

show shizu behind_smile
with charachange

# ssh "We should take a photo of the three of us."
ssh ""

show shizu adjust_happy
with charachange

# ssh "We haven't taken a student council photo yet. Now's the perfect chance."
ssh ""

show shizu basic_normal
with charachange

# ssh "But, if I have to look at this picture a year from now, I don't want us staring back at me."
ssh ""

# mi "Hm~? What does that mean, Shicchan?"
mi ""

show shizu adjust_frown
with charachange

# ssh "Pictures are supposed to capture the moment, isn't that right? Without a doubt. They're not portraits. Just standing around would be so stiff. It wouldn't even capture how I feel."
ssh ""

show shizu behind_smile
with charachange

# ssh "I feel like we'll meet again. So, this isn't an occasion to take such a serious photo. It should be a “see you later” type of photo; not a big deal. It should be something more… festive."
ssh ""

# hi "Oh boy."
hi ""

show shizu basic_happy
with charachange

# ssh "Like this. Follow me."
ssh ""

show shizu adjust_smug
with charachange

show shizu behind_smile
with charachange

# "Shizune poses like a musketeer, so quickly that I'm sure even she knows it's silly."
""

show mishashort cross_laugh
with charachange

# mi "Ahahaha~!"
mi ""

# hi "Do we really have to do… such a cheesy pose?"
hi ""

show shizu adjust_happy
with charachange

# ssh "I can think of no better pose. Misha, go find Yuuko!"
ssh ""

show mishashort sign_smile
with charachange

# mi "I don't like this pose either, but I think it's kind of nice~."
mi ""

# hi "That doesn't even make sense."
hi ""

show mishashort invis:
    xpos 0.0
with dissolvecharamove

# "She's already gone, and returns dragging Yuuko behind her."
""

show yuuko invis:
    center
    xpos -0.2
with None

show bg school_gate at left
show shizu behind_smile_close:
    xpos 0.83
show mishashort hips_grin at center
show yuuko neutral_up at left
with dissolvecharamove

# "The flash is off. A red LED blinks three times above it after Yuuko's finger presses the button. Shizune glances at both of us to make sure we have the timing down. Synchronize watches. We jump."
""

play sound sfx_camera
$ renpy.music.set_volume(0.0, 0.5, channel="ambient")

scene ev shizu_goodend
with cameraflashlong

# ssh "I bet that turned out excellently."
ssh ""

# ssh "Okay, …"
ssh ""

# mi "Now, let's get one with Yuuko, too~!"
mi ""

# yu "N-no, please…"
yu ""

# hi "That's not necessary."
hi ""

# "I want a copy of this photo, too."
""

show ev shizu_goodend_pan
with None

# "I'll likely die younger than the average person. My life could unexpectedly burn out at any time. I don't have any time to waste, then. I want to live as much as possible. I also want to see other people smile from what I've made and done."
""

# "Living vicariously through the happiness of others doesn't seem so bad. Feeling joy through another person's happiness doesn't seem like such a bad thing. It's the easiest way I can think of to draw out my own life, and give it distinction."
""

# "Maybe this is the meaning that Shizune has found for herself, although it's just my theory. People find themselves alone often in their lives, and without direction."
""

# "However, people can take refuge in moments of happiness. They can dot a person's life like stops on a train map. Or waypoints of memory on a long trail."
""

# "These individual moments, on reflection, can give a person's life fulfillment. Every friend, and festival, and joyful meeting, and joyful parting."
""

# "I want to be able to ask Shizune one day if I'm right. I want to spend the time I have with her. Finally, I want to make Shizune smile for herself."
""

$ renpy.music.set_volume(0.3, 1.0, channel="ambient")

scene bg school_gate at left
#show yuuko neutral_up at left
show mishashort perky_smile at twoleft #center
show shizu behind_smile_close at tworight #:
#    center
#    xpos 0.83
with locationchange

# hi "I love you."
hi ""

# "I pause, wondering if she'll look at me, confused, and ask why I'd say it out of the blue. She doesn't."
""

# hi "Do they do that reunion thing here?"
hi ""

show shizu adjust_happy_close
with charachange

# ssh "Of course they do."
ssh ""

show mishashort sign_smile
with charachange

# mi "A Student Council member should know that~!"
mi ""

show shizu behind_smile_close
with charachange

# ssh "Sooner than that, though, okay?"
ssh ""

show shizu adjust_happy_close
with charachange

# ssh "Both of you."
ssh ""

show mishashort hips_grin
with charachange

# mi "Right~!"
mi ""

# hi "Yeah."
hi ""

show shizu basic_happy_close
with charachange

# ssh "Yuuko! You do the pose, too!"
ssh ""

show shizu adjust_happy_close
with charachange

# ssh "Afterwards, we can go for tea."
ssh ""

# "Shizune laughs, as if she doesn't have a care in the world, Misha's laughter joining with hers as easily as if it were her own. We'll meet again."
""

stop ambient fadeout 2.0
stop music fadeout 2.0

#shizune good end complete

#****************************

#shizune bad end branch begin

label th_S38:

play music music_pearly

scene bg school_scienceroom
with locationchange

# "The next day, Misha is back in class, although still looking pretty sullen. Not that I was expecting her to magically feel better; that would be asking the impossible considering what happened."
""

# "This time it's Shizune who's out. At first, it almost makes me laugh that suddenly whenever one is in class the other isn't. But thinking about it, there's nothing funny at all about it. In fact, I find it hard to concentrate on my work because of it."
""

# "It could be that she's just sick. Or she could simply be skipping class. It could also be something more serious, and I'm tempted to ask Misha if she knows, but I end up doing nothing."
""

# "I don't regret stepping in yesterday, scared that Misha would do something rash."
""

play sound sfx_normalbell

# "But now I feel like I should give her some space. Eventually, the bell rings, and Misha gets up for lunch along with everyone else. I decide to eat lunch in an empty classroom today… just not this one."
""

scene bg school_hallway3
with locationchange

# "Unfortunately, a lot of other students seem to have the same idea, so there aren't a whole lot of empty classrooms to go around. Finally, as I'm about to give up on the idea, I find a dark one at the end of the hall."
""

scene bg school_miyagi
show lilly back_surprise:
    center
    ypos 1.15
with locationchange

# "On turning the lights on, however, I find out that this one isn't empty either. Lilly's head turns in my direction, which freaks me out before I realize she probably heard me flipping the light switch."
""

show lilly basic_listen
with charachange

# li "Hello."
li ""

# hi "Hey, Lilly. I didn't think anyone else would be here."
hi ""

show lilly basic_weaksmile
with charachange

# li "Is that you, Hisao?"
li ""

# hi "Yeah, but you probably knew that already."
hi ""

# "I turn to leave, which prompts Lilly to quickly speak up."
""

show lilly basic_smile
with charachange

# li "You don't have to leave so quickly. We can both have lunch in the same room. As a matter of fact, I would prefer to eat with someone else."
li ""

# "I'm about to ask her how she knew I was here to eat lunch, but brush it aside. It's just simple common sense, and I don't want to seem too easily impressed."
""

show lilly basic_smile_close:
    center
    ypos 1.1
with characlose

# "I take a seat at the desk in front of Lilly, after reversing it to face hers. I've heard that our minds fill in a lot of what we see based on how we remember seeing it once before, or our expectations."
""

# "Mostly for efficiency, so as to not have to process everything you look at individually."
""

# "Lilly never seems to stop to question any noise. So, I wonder, is it because her mind is filling in context every time? Or does she not care and just sort of accept things as they fall into place?"
""

# "On her desk there are just a few cookies and a thermos of tea. She must be one of those light lunch types. I bite into my sandwich. Some of the ingredients spill out the back end."
""

show lilly basic_ara_close
with charachange

# li "We haven't spoken in a long time, I'm surprised that you still remember my name."
li ""

# hi "Mmphffmm?"
hi ""

show lilly basic_smileclosed_close
with charachange

# li "It must be very busy in the Student Council."
li ""

# hi "It's different every week. Some weeks are pretty slow, some weeks I consider taking a sick day."
hi ""

# "Hold on, Lilly, I need a second to catch my breath from inhaling that sandwich."
""

show lilly basic_smile_close
with charachange

# li "And how has it been lately?"
li ""

# hi "Unpredictable."
hi ""

play sound sfx_snap

show lilly basic_oops_close
with vpunch

# "I snap my fingers, which, from her facial expression, upsets her a lot."
""

show lilly basic_reminisce_close
with charachange

# li "I think that you have been hanging out around those two too much."
li ""

# hi "I guess it is one of Shizune's trademarks. Personally, I like it."
hi ""

show lilly basic_displeased_close
with charachange

# li "I ignore it."
li ""

# "Her tone doesn't change even slightly, but Lilly's mood has obviously dipped."
""

# hi "Doesn't seem like it would be easy to. I've been trying to figure out how she can make it so loud, but I think I'm damaging my knuckles."
hi ""

show lilly behind_displeased_close
with charachange

# li "Even if it were loud enough to break the windows, I would ignore it. I'm not a trained seal; I have that luxury."
li ""

# hi "Are you still mad about that?"
hi ""

# "I ask the question as carefully and diplomatically as possible, although in the end I'm only asking to satisfy my curiosity."
""

show lilly basic_weaksmile_close
with charachange

# li "No, of course not, although I don't like Shizune."
li ""

show lilly basic_reminisce_close
with charachange

# li "We were in the Student Council together for a brief time."
li ""

# hi "I heard."
hi ""

show lilly basic_sleepy_close
with charachange

# li "I wish you hadn't been so quick to join."
li ""

show lilly basic_listen_close
with charachange

# li "I don't like the way Shizune runs the Student Council. Did you know that she scared off most of the old members? That is why I think she tries to surround herself with people who won't oppose her."
li ""

show lilly basic_reminisce_close
with charachange

# li "And they don't. It's like a dependency bubble."
li ""

# "I'm sure that Shizune is aware of what Lilly is saying. After all, I can remember her specifically denying it a couple times, which I'd always thought was strange."
""

# "They say that the more specific a denial is, the more likely it is that the allegations are true. In this case, I think I'd disagree. Shizune is the one subject on which her opinion could be called less than objective."
""

# hi "Did you tell her that?"
hi ""

show lilly basic_displeased_close
with charachange

# li "Very often."
li ""

# "Lilly stops to polish off the last of her tea. I'm running behind on finishing my own lunch and take advantage of the pause to eat as much as possible."
""

show lilly basic_sleepy_close
with charachange

# li "All of her friends are related to the Student Council, like Misha."
li ""

# li "I heard things are touchy between her and Misha. Did they have a fight?"
li ""

# hi "Not really."
hi ""

show lilly basic_surprised_close
with charachange

# li "Is that so?"
li ""

show lilly basic_reminisce_close
with charachange

# li "Either way, there is no point in attempting to force them to make up. Always try to confront everything head-on is what Shizune would do, but it doesn't work in the real world. At some point, it's just being stubborn, not bravery or good intentions."
li ""

# hi "That's a little general, don't you think?"
hi ""

show lilly basic_smileclosed_close
with charachange

# li "Hm, I suppose."
li ""

show lilly basic_weaksmile_close
with charachange

# li "What do you think is the best to have with tea? Cookies, or scones? I like them both, in different ways. I couldn't possibly choose."
li ""

show lilly basic_displeased_close
with charachange

# li "I don't like people who constantly force me to pick sides or want to turn everything into a contest."
li ""

# li "When I joined the Student Council, I thought it would just mean helping everything run smoothly and helping people out, like being the class representative."
li ""

show lilly basic_reminisce_close
with charachange

# li "Instead, every day consisted of having Shizune stomp around, using Misha like a megaphone, to talk about how we had to outdo the last Student Council, and create more and more events, and make them increasingly larger."
li ""

# hi "But then the two of you basically want the same thing. All that stuff makes things exciting. I didn't really get it at first, but it's not some ego project. People like fireworks, and soba huts, candied apples, and dress-up days, or whatever."
hi ""

# hi "The more the Student Council does, the more responsibility the school gives us. It means extra work, but in a way, it also means more freedom."
hi ""

# hi "You have the pull to do things like organize a big festival, and they'll think you're capable enough to handle it instead of just rejecting it instantly."
hi ""

# hi "Anyway, I want that too, now. It's got its share of pointless busywork, but there are moments that make it worth it when everything comes together. It gives me something to do. If I were to just go to school day in, day out, I think I'd explode."
hi ""

show lilly basic_weaksmile_close
with charachange

# li "I think Yamaku is much more easygoing than other schools."
li ""

# "Yamaku isn't other schools, though."
""

# "I start slipping into another, familiar mentality. In some ways, it's almost too easygoing."
""

# "And if I were a different person I'm sure that I would find how easygoing it was to be stifling, though in any other school, such easiness would just be the normal flow of life."
""

# "But here, the uneventfulness would be compounded. It would feel different, because I'm not a normal person, after all."
""

# "I'd be reminded of it every time I heard the blood beating in my temples. I'd feel patronized and weak, and my bitterness would only grow."
""

# hi "Yeah, sure."
hi ""

# hi "The point is, I think I understand what it's all about now. You're really giving Shizune too much of a hard time."
hi ""

show lilly basic_sleepy_close
with charachange

# li "That might be true, but when it comes to how she treats individual people, she doesn't do very well."
li ""

# "Unfortunately, that one is a little harder to argue."
""

show lilly basic_smile_close
with charachange

# li "Do you have the time? I like to go to class ten minutes before the bell."
li ""

# hi "Then you're right on time if you go now."
hi ""

show lilly invis_close at center
with dissolvecharamove

stop music fadeout 4.0

# "Excusing herself, Lilly leaves, and I sit listening to the clicking of her cane on the floor fading into the mumble of other students having conversations in the other classrooms and in the hall."
""

# "I feel exhausted, and completely forget that I wanted to talk to Shizune today."
""

scene black
with dissolve


#****************************

label th_S39:

scene bg school_hallway3
with locationchange

# "After classes the next day, I instantly head towards the student council room to talk to Shizune."
""

# "Even though she's in class, trying to cut her off and have a conversation with her near the doorway or out in the hall could be a little obstructive."
""

scene bg school_lobby
with locationchange

# "Better to try and meet up with her at the student council room. I take my time heading there, getting a juice from the vending machine on the way."
""

# "I also go over what I want to say to her in my head. It's nothing too important, only a few questions about upcoming events."
""

scene bg school_council
with locationchange

play music music_rain fadein 8.0

# "The door is unlocked when I get there. I'd think the room was empty too, if I couldn't see Shizune's bag perched on her desk, with the top of her head peeking from behind it. It looks as though she's built herself a little fort."
""

show shizu basic_normal at center
with charaenter

# "Shizune gives a wave from behind her bag, before picking it up with a finger and moving it out of the way."
""

# "But after that, she immediately goes back to tapping her pen against the desk and staring into a checklist as if it held the meaning of life itself in it."
""

show shizu adjust_frown
with charachange

# ssh "What do you need?"
ssh ""

# his "I wanted to see if there was anything I could help with. Like all that over there, what are those?"
his ""

# "I point to the medium-sized stack of folders beside her, but she waves her hand dismissively."
""

show shizu behind_blank
with charachange

# ssh "I can handle it myself."
ssh ""

# his "Then what about the elections?"
his ""

# his "Also, where's Misha?"
his ""

show shizu behind_sad
with charachange

# shi "…"
shi ""

show shizu basic_normal2
with charachange

# ssh "It's going okay. And I told Misha that I was going to handle everything myself."
ssh ""

# his "Why?"
his ""

# "Shizune spins a pen in her hand slowly, working it between each of her fingers, like a needle through a patch of cloth."
""

show shizu behind_blank
with charachange

# ssh "No reason."
ssh ""

# his "Really?"
his ""

show shizu adjust_frown
with charachange

# ssh "No reason."
ssh ""

# "She signs it again for emphasis, to shut down the notion that there's anything more behind it. But there is, since she's definitely not acting normally."
""

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

# n "\n\n\n\n“What's with the silent treatment?” is the phrase that immediately springs to mind, even though it is hardly the time for humor. It does describe how I feel. We can't communicate normally, so I appreciate the few ways we can. To be shut out like this hurts."
n ""

# n "It's obvious that whatever her reasons, it's going to be pretty much impossible to talk to Shizune today. Beyond just being stubborn, she seems depressed, but with the way our conversation is going already, I don't see myself being able to find out what she's depressed about."
n ""

# n "\nSomehow, that only makes me want to find out more. And that means I have to ask Misha. The problem is, I don't really know where Misha goes in her spare time."
n ""

$ renpy.music.set_volume(1.0, 1.0, channel="music")
stop music fadeout 3.0

nvl hide dissolve
nvl clear

scene bg school_lobby
with shorttimeskip

window show

# "After asking way more people than I should if they've noticed a girl with bright pink hair around, and getting way more negative answers than expected, I finally find a couple who have seen her."
""

scene bg school_cafeteria
show mishashort perky_smile at center
with locationchange

play music music_moonlight fadein 8.0

# "By the time I reach the cafeteria, where Misha has apparently been this entire time, I've been around the whole school twice, and am very tired. I realize I've passed by her before, and just didn't see her behind a pillar."
""

# hi "Why are you better at finding me than I am at finding you?"
hi ""

show mishashort hips_smile
with charachange

# mi "You were looking for me, Hicchan?"
mi ""

show mishashort hips_grin
with charachange

# mi "Hm~… Who knows~? I think it's just coincidence."
mi ""

# hi "You know, the whole point of coincidences is that they aren't consistent."
hi ""

show mishashort cross_laugh
with charachange

# mi "Hahaha~."
mi ""

# hi "Are you having a really late lunch?"
hi ""

show mishashort sign_smile
with charachange

# mi "I didn't get to eat at lunchtime, so yeah~! But~, not too much, so I can still have dinner."
mi ""

show mishashort perky_smile
with charachange

# mi "Did you want to talk to me about something, Hicchan?"
mi ""

# "I don't waste any time."
""

# hi "Yeah. The reason I'm here… Did you notice Shizune has been kind of moody today?"
hi ""

show mishashort perky_confused
with charachange

# mi "I wanted to ask you the same thing, Hicchan~."
mi ""

show mishashort perky_sad
with charachange

# mi "Well~, except, she's been this way for a couple of days now."
mi ""

# hi "I see."
hi ""

show mishashort sign_confused
with charachange

# mi "Hicchan, do you think it's because of something I did? Do you think I got upset at Shicchan, like last time?"
mi ""

# hi "No. She seems angrier at me, anyway."
hi ""

# "I'm not lying, I really don't. Unfortunately, my attempts to assure her of that don't seem to be going so well. In her own way, Misha is pretty stubborn, too."
""

scene bg school_dormhisao_ss
with locationskip

# "Eventually, I just head back to my dorm. The last few days have been nothing but a continuously frustrating experience, and they left me drained. I feel tired enough that I decide to take a nap, hoping that maybe I'll figure things out in my sleep."
""

stop music fadeout 3.0

window hide

scene black
with shuteye

with Pause(1.0)
with shorttimeskip
with Pause(1.0)

scene bg school_dormhisao_ni
with openeye

window show

play music music_night fadein 1.0

# "When I wake up, I feel more refreshed, but still without clarity. The only thing that has changed is that it's dark outside."
""

# "From opening the window a little, I can tell the weather is still kind of nice. After dry-swallowing my nighttime pills, I take a little walk to the vending machines."
""

scene bg school_lobby_ni
with locationskip

# "They're out of everything I'd normally get, so I mash my hand against the buttons until something pops out."
""

scene bg school_courtyard_ni
with locationchange

# "The lights are off in the main building, including the student council room. Just an offhand observation."
""

play sound sfx_rustling

# "As I'm thinking to myself, I hear a rustling behind me. I've seen this movie before, and that is a very ominous sound to hear, alone at night."
""

show kenji happy_ni at center
with charaenter

# "Luckily, it's just Kenji, and he wanders out of the bushes in an unusually cheery mood."
""

# ke "Hey."
ke ""

# hi "What the hell? Do you just creep up on people at night and casually go “hey” a lot?"
hi ""

show kenji neutral_ni
with charachange

# ke "No, that'd be weird. I knew it was you. I have extremely good night vision. Maybe it's because I'm superhuman."
ke ""

# hi "What are you doing here, then?"
hi ""

show kenji tsun_ni
with charachange

# ke "I could ask you the same thing. What are YOU doing here?"
ke ""

# "I consider just telling him the truth, but quickly decide against it. It would take too long to explain."
""

# hi "Howling at the moon."
hi ""

show kenji neutral_ni
with charachange

# ke "I do that too, sometimes. The moon isn't out tonight, though."
ke ""

# "I barely even hear him, feeling a bit resentful at the interruption."
""

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

# n "\n\nI lied to Shizune through my teeth that nothing was wrong. Or, to be more exact, I lied through my hands. And at the exact same time, I was carrying on an entirely different conversation with Misha."
n ""

# n "That conversation, understandably, could upset Shizune. But there was no way that she could have heard it. Even Misha's hands, usually signing all her thoughts, were completely still. Even if they weren't, I was standing in front of her, blocking them from Shizune's view."
n ""

# n "The only way that Shizune could listen in on that conversation would be if she could read lips. Pretty much the first thing I'd asked about when taking sign language was about lip reading, just out of curiosity. It's not easy, nor is it perfect… so I'd never considered it until now."
n ""

# n "\nIt would make sense, and the room for misunderstandings while reading lips wouldn't help."
n ""

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear
window show

# ke "…So I realized that I could use the cover of darkness to buy milk. Usually, I only go out when it's raining or I can shroud myself in a sea of bikers, or tourists. This is much more consistent… I'm spending too much money on milk now, though."
ke ""

show kenji happy_ni
with charachange

# ke "You seem kind of mopey or out of it or something. Don't think too hard, a man has to be all about action! You can think about stuff all day, but changing the situation around by doing something is the best way."
ke ""

# ke "I do things all the time without thinking about it. That's why in middle school they called me “causes many problems.” I thought it was cool; sounds like an Indian name."
ke ""

# hi "I'm not really in the mood."
hi ""

show kenji neutral_ni
with charachange

# ke "Having a bad day?"
ke ""

# hi "Yeah, I don't know. I'm kind of distracted right now."
hi ""

stop music fadeout 7.0

hide kenji
with dissolve

# "So distracted that it doesn't hit me until he leaves that his was actually kind of sound advice. I think Shizune would have given me the same suggestion. By then, it's too late to thank him politely."
""

# "I already responded in the rudest tone possible. I just feel like an ass."
""

"In retrospect, these past few days I've regretted every action I've taken. The worst part is that I haven't taken the time to stew over them, and in doing so, learn from them. This only leads to - has led to - more regrets." 

scene black
with dissolve

#****************************

label th_S40:

play music music_dreamy fadein 2.0

scene bg school_dormhisao
with locationchange

play sound sfx_doorknock2

# "The next morning, as I'm getting dressed, I hear a knock at my door. Quickly putting on the rest of my clothes, I open it, without really stopping to think about who could be behind it."
""

scene bg school_dormhallway
show shizu basic_normal
with locationchange

# "It turns out to be Shizune."
""

show shizu behind_blank
with charachange

# ssh "Misha told me that you were looking for me."
ssh ""

# "I'm a bit hurt that I don't even get a “good morning,” but it's not too big a deal."
""

# his "I was."
his ""

show shizu basic_normal2
with charachange

# ssh "But you found me yesterday."
ssh ""

# "Shizune's fingers trace a crack in the wall. It seems like she's trying her best to look distant."
""

show shizu adjust_smug
with charachange

# ssh "Well, I didn't make it easy, did I?"
ssh ""

# his "It's all right."
his ""

show shizu behind_blank
with charachange

# ssh "That's why I'm here. We can talk today. Although… I kind of want to go somewhere else."
ssh ""

# his "What about class?"
his ""

show shizu adjust_smug
with charachange

# ssh "It's fine, it's fine."
ssh ""

show shizu basic_normal2
with charachange

# ssh "How about we take a walk around the school? Everywhere except the main building is going to be deserted. The first period bell should be ringing right now."
ssh ""

# "I take a quick glance at my watch and see that she's right."
""

# his "Okay."
his ""

stop music fadeout 6.0

show shizu basic_angry
with charachange

# shi "…"
shi ""

# his "Is there something wrong?"
his ""

show shizu behind_blank
with charachange

# ssh "Why do you think there is something wrong?"
ssh ""

# his "Because you're obviously upset. I could just tell."
his ""

# his "It's what I wanted to talk to you about."
his ""

show shizu basic_normal2
with charachange

# "Shizune quickly cracks her knuckles while I sign to her."
""

show shizu behind_blank
with charachange

# ssh "Apparently, I'm easier to read than I'd thought. I was trying hard to hide it. Can you tell what I'm thinking right now?"
ssh ""

hide shizu
with charaexit

# "I don't respond, and Shizune heads towards the door, slowly enough that I can tell she wants me to follow her. Her hands are folded behind her back, which is arched against them as though she is about to bend over backwards at any second."
""

scene bg school_courtyard
with locationchange

# "Outside, I see Shizune is right. The school is completely deserted. Although it's not my first time seeing the school like this, it's kind of eerie."
""

scene bg school_backexit at right
with locationchange

# "Shizune acts almost as though I'm not there, browsing a vending machine and taking a slow and winding path until we end up behind the main building."
""

show shizu invis_close at tworight
with None

show shizu basic_normal_close:
    ypos 1.05
with dissolvecharamove

# "Finally, she leans against a wall and faces me, but it's like I've forgotten how to start a conversation."
""

play music music_sadness fadein 8.0

show shizu behind_blank_close
with charachange

# ssh "There is a saying. “You don't know how much you've screwed up until you screw up.”"
ssh ""

# his "Who says that?"
his ""

show shizu basic_normal2_close
with charachange

# ssh "I guess it's me."
ssh ""

show shizu basic_angry_close
with charachange

# "Reconsidering her train of thought, she waves her hands in frustration."
""

show shizu behind_blank_close
with charachange

# ssh "Okay, I'll put it differently."
ssh ""

show shizu basic_normal_close
with charachange

# ssh "When I was younger, we had to make posters for Earth Day in school. There was another girl in my class whom everyone considered the best artist."
ssh ""

show shizu behind_blank_close
with charachange

# ssh "It wasn't because she could draw better than everyone else, it was how much she could fit into a single picture."
ssh ""

show shizu adjust_frown_close
with charachange

# ssh "I wanted to be better than her, so I made countless posters until I ended up with the best possible one. I had to be the best and have the greatest one. In the end, everyone liked my poster the most of all, even the teacher."
ssh ""

show shizu basic_normal_close
with charachange

# ssh "A week later, it was meaningless. I threw it in the trash."
ssh ""

show shizu behind_blank_close
with charachange

# ssh "I think I've told you something like this before."
ssh ""

# his "Yeah."
his ""

show shizu basic_angry_close
with charachange

# ssh "When I feel like I'm finished, I wish I could just wipe the slate clean. Whether I succeed or not. I put Misha through a lot, and even dragged you into it."
ssh ""

show shizu adjust_frown_close
with charachange

# ssh "And every point where I could have solved this silly situation, or prevented it from happening in the first place, keeps coming back to me."
ssh ""

show shizu behind_sad_close
with charachange

# ssh "It's the worst feeling. Especially when I feel like I've done nothing right and everything wrong. Like recently. It's the worst kind of failure. I feel like a failure on every level."
ssh ""

show shizu basic_normal2_close
with charachange

# ssh "I wish I could wipe away everything I've done and just be alone, since all I've done is mess with Misha for two years. And jerk you around for a year for selfish reasons."
ssh ""

# his "It's fine."
his ""

show shizu adjust_frown_close
with charachange

# ssh "No, it's not. You don't understand. I was just thinking about it; everything I do feels like I have to beat someone else. Everyone else, even. If that is how it is, then what are my relationships with people? They almost feel the same."
ssh ""

# "I can see where this is going."
""

show shizu behind_sad_close
with charachange

# ssh "The point is that I've messed up so many people by being selfish, and now I want to be away from other people for a while."
ssh ""

# his "Even me?"
his ""

# "There's a pause."
""

show shizu basic_normal_close
with charachange

# ssh "Yes."
ssh ""

# "Followed by an even longer pause, this time from me."
""

# his "I see."
his ""

# his "That's the most selfish thing you could do."
his ""

# his "It's just you making another decision by yourself."
his ""

show shizu basic_normal2_close
with charachange

# shi "…"
shi ""

# "For a minute, it looks as though she's considering the best way to respond, but in the end, she simply nods. Which, I think, is the best way to respond anyway."
""

# "It's very like her, to be roundabout even now, but ultimately without excuses."
""

# "All my emotions simmer inside me. I see a kettle in front of me, water rolling inside it, so close that I can touch it and feel the heat radiating off of it. I'm glad for the distraction, because I know there's no recourse or bargaining possible."
""

show shizu adjust_frown_close
with charachange

# ssh "You told me that everything was fine, but it wasn't true, was it?"
ssh "นายบอกฉันเองนี่ว่าทุกอย่างจะโอเค แต่ก็ไม่เป็นอย่างนั้นนี่ จริงไหมล่ะ?"

show shizu behind_sad_close
with charachange

# ssh "I can't believe it ever again, then."
ssh "ฉันคงเชื่อไม่ได้อีกต่อไปแล้วล่ะ"

# hi "All right."
hi "เอาเถอะ"

show bg school_backexit at center
show shizu invis_close:
    xpos 0.85
with dissolvecharamove

# "Not even bothering to sign it, I stand up. My hands are in my pockets, fingering my loose change. The morning air is cold against my face."
"ฉันลุกขึ้นโดยไม่แม้แต่จะส่งภาษามืออีกต่อไป มือของฉันล้วงกระเป๋า นิ้วเขี่ยเศษเหรียญ อากาศยามเช้าเย็นยะเยือก\nปะทะใบหน้าของฉัน"

scene ev shizu_badend:
    xalign 0.0 yalign 0.5 zoom 1.1 subpixel True
    acdc_warp 10.0 zoom 1.0
with locationchange

# "As I look back at her, she seems very lonely. I'm reminded of myself. I've made that expression before. Maybe it's on my face right now. It feels like the image of such a lonely girl will stick in my mind forever."
"พอหันกลับไปหาเธอ เธอดูโดดเดี่ยวเหลือเกิน ทำให้ฉันนึกถึงตัวเอง ฉันเคยทำหน้าแบบนั้นมาก่อน บางทีตอนนี้ฉันอาจจะ\nกำลังทำหน้าแบบนั้นอยู่ก็ได้ รู้สึกเหมือนภาพเด็กสาวที่โดดเดี่ยวคนนี้จะติดอยู่ในใจฉันตลอดกาล"

# "Every moment where I could have prevented this, or solved the problem, comes back to me. It makes me smile in a way without amusement."
"ทุก ๆ ช่วงเวลาที่ฉันสามารถป้องกัน หรือแก้ไขปัญหานี้ได้ย้อนกลับมาหาฉันอีกครั้ง ทำให้ฉันยิ้มออกมาโดยไม่มีความสุขเลย\nแม้แต่น้อย"

stop music fadeout 4.0

window hide

return

#shizune bad end complete