label th_L9:

window hide None

scene black
with dissolve

scene bg misc_sky at Fullpan(10.0)
with locationchange

$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_normal fadein 3.0

window show

# "I rest my chin on my hand as I absentmindedly look out the window, yet another of Mutou's lectures droning on and on as if it were endless."
"ฉันนั่งเท้าคางเหม่อมองหน้าต่าง เป็นคาบเรียนอันยืดยาวน่าเบื่อของคุณครูอย่างเช่นเคย"

# "The summer sky is almost alluring in its bright cerulean splendor. Only the odd passing cloud breaks up the deep blue expanse."
"สีครามสดใสเต็มเติมฟ้าฤดูร้อนชวนมอง ก้อนเมฆที่ลอยผ่านไปมาบดบังผืนฟ้าลึกล้ำ"

# "This feeling of longing is probably the outdoors side of me yearning to escape."
"ความโหยหานี้คงมาจากตัวฉันอีกด้านที่ชอบอยู่กลางแจ้งมั้ง"

# mu "Nakai, could you answer this?"
mu "นากาอิ อันนี้ตอบอะไร"

# "That side of me's lost to the past now, though."
"แต่ตัวฉันด้านนั้นตายไปกับอดีตแล้วละ"

scene bg school_scienceroom
show muto normal at center
with locationchange

# hi "In that case… I think it would use the -ane suffix?"
hi "อันนี้… ต้องใช้คำลงท้ายเป็น -ane หรือเปล่าครับ"

show muto smile
with charachange

# mu "Correct. Moving on, the suffix for…"
mu "ถูกต้อง ทีนี้ คำลงท้ายของ…"

# "As my attention towards Mutou slips once again, I spot Misha giving me an enthusiastic thumbs-up, and nod at her to settle her down."
"ฉันเห็นมิช่าที่ยืดอกยกนิ้วโป้งให้เมื่อความสนใจของฉันที่มีให้คุณครูหายไปอีกครั้ง ฉันจึงพยักหน้าตอบไปเป็นการบอก\nให้พอ"

scene bg school_scienceroom
with shorttimeskip

# "It's been a handful of days since Lilly left for Scotland, days which have passed relatively peacefully."
"ผ่านมาแล้วสักสองสามวันนับตั้งแต่ที่ลิลลี่ไปสกอตแลนด์ ซึ่งเหตุการณ์แต่ละวันก็ไม่ได้มีอะไรเป็นพิเศษ"

# "Life largely continued as usual, in contrast to what I'd expected. While thoughts of her have danced around on the edge of my mind since she left, present events manage to subdue them. At least for the time being."
"ส่วนมากก็ใช้ชีวิตอยู่ตามปกติ ซึ่งผิดจากที่คาดเอาไว้ แม้ในหัวจะยังมีเรื่องลิลลี่อยู่บ้างหลังจากที่เธอไปแล้ว แต่เหตุการณ์\nตรงหน้าก็พลอยทำให้ลืม ๆ ไป อย่างน้อยก็ช่วงนี้อะนะ"

# "So I find myself idly chatting with Hanako, as usual, when lunchtime finally rolls by."
"เมื่อถึงเวลาพักเที่ยงฉันก็มานั่งคุยกับฮานาโกะไปเรื่อยเปื่อย"

show hanako basic_normal
with charaenter

# ha "Are the later ones in the series good as well?"
ha "เล่มหลัง ๆ สนุกเหมือนกันมั้ย"

# hi "Not really. You're probably best off just sticking to the original. His later books didn't live up to it, other than maybe “God Emperor.”"
hi "ไม่ค่อยอะ อ่านแต่ภาคแรกน่าจะดีสุดแล้ว ภาคหลัง ๆ ไม่ค่อยสนุกเท่าภาคแรกเท่าไหร่ อันอื่นที่สนุกก็น่าจะภาค\n“{i}จักรพรรดิเทพแห่งดูน{/i}” มั้ง"

show hanako basic_bashful at center
with charachange

# ha "Thanks, I wasn't really sure if…"
ha "ขอบคุณนะ พอดีฉันไม่ค่อยแน่ใจว่า…"

show misha invis at offscreenleft
show shizu invis at offscreenleft
with None

show hanako defarms_shock at right
show shizu behind_blank at center
show misha hips_smile at left
show bg school_scienceroom at bgright
with dissolvecharamove

# "As Hanako steps to the side, I see Shizune stride up in her typically businesslike manner, flanked by her ever-present bright-haired shadow."
"พอฮานาโกะขยับตัวออกก็เห็นชิซูเนะที่เดินอาด ๆ เข้ามาด้วยท่าทีจริงจังเช่นทุกที ขนาบมาด้วยเงาตามตัวที่มีผม\nสีสดใส"

# "Try as I might, I can't read any hint of their intent from their faces. Shizune's poker face and Misha's seemingly boundless cheerfulness are a devilish combination."
"ดูยังไงก็ดูไม่ออกว่าสองคนนี้จะเอายังไงกับฉันกันแน่ สีหน้าเรียบเฉยของชิซูเนะกับความร่าเริงที่ดูไร้ขีดจำกัดของมิช่านั้น\nเป็นคู่ผสมที่ร้ายกาจ"

# hi "'Morning Shizune, Misha."
hi "รุณหวัด ชิซูเนะ มิช่า"

show hanako emb_timid
with charachange

# ha "Um… hi."
ha "เอ่อ… ไง"

show shizu basic_normal
with charachange

# "I accentuate the greeting with a nod to Shizune in order to get the point across. She promptly and curtly returns the gesture to both of us."
"ฉันเน้นการทักทายไปด้วยการพยักหน้าให้ชิซูเนะเพื่อให้สิ่งที่สื่อสารนั้นส่งไปถึง เธอทักทายตอบพวกเราสองคนแบบ\nกระชับและรวดเร็ว"

# "It's been a long while since I've really talked to either of them. For a while I thought they might be avoiding me, but I eventually came to the conclusion that Shizune really isn't the type to do so."
"ไม่ได้คุยกับสองคนนี้มานานแล้วจนนึกว่าจงใจหลบหน้ากันไปเสียอีก แต่พอลองคิด ๆ ดูแล้ว ชิซูเนะคงไม่ใช่คนอย่างนั้น"

show shizu adjust_happy
with charachange

shi "…"

show misha sign_smile
with charachange

# mi "'Morning~! Shicchan says that Mutou wants to see you sometime."
mi "รุณหวัด~! ชิจังบอกว่าเดี๋ยวครูจะเรียกนายไปคุยด้วย"

# "Because of this statement, my face contorts as if I'd just eaten spoiled food, giving Misha no end of amusement."
"พอได้ยินประโยคนั้นแล้วฉันก็ทำหน้าเบ้ราวกับว่ากินข้าวบูดเข้าไปเต็มคำ ซึ่งดูมิช่าจะชอบอกชอบใจเหลือเกิน"

show misha cross_laugh
with charachange

# mi "Wahahaha~! Anyone'd think you were in trouble, Hicchan!"
mi "วะฮ่าฮ่าฮ่า~! เป็นใครก็คงคิดว่านายซี้แหงแน่ ๆ ฮิจัง!"

show shizu behind_smile
with charachange

shi "…"

show misha perky_smile
with charachange

# mi "You may not be aware of it, but you have the least to worry about out of anyone in the class."
mi "นายอาจจะไม่รู้ตัวหรอก แต่ในห้องนี่น่ะ ถ้าให้เทียบแล้ว นายเป็นคนที่แทบไม่มีอะไรจะต้องให้เป็นห่วงเลย"

show hanako emb_smile
with charachange

# "What an unexpected vote of confidence. Even Hanako nods hesitantly to affirm the point."
"อยู่ ๆ ก็ได้รับความไว้วางใจอย่างนี้เลยเหรอ แม้แต่ฮานาโกะยังค่อย ๆ พยักหน้าตามเป็นการยืนยันเลยแฮะ"

# hi "Thanks, I'll keep that in mind. There was something I wanted to ask you, though."
hi "ขอบใจ จะจำไว้แล้วกัน แต่เออ มีเรื่องจะถาม"

show shizu basic_normal
with charachange

shi "…"

show misha hips_smile
with charachange

# mi "And what might that be, Hicchan?"
mi "จะถามว่าอะไรล่ะฮิจัง"

# "I have a feeling this won't go over well, but here goes…"
"รู้สึกว่าน่าจะจบไม่สวยเท่าไหร่ แต่เอาละ…"

# hi "Is there any reason why you and Lilly don't get along? It seems like even a little civility would help you both in your duties."
hi "ทำไมเธอกับลิลลี่ถึงไม่ถูกกันเหรอ ถ้ายอม ๆ กันสักหน่อย เรื่องงานอะไรทั้งหลายแหล่น่าจะราบรื่นขึ้นนะ"

show shizu cross_angry
with charachange

# "Shizune's cold stare after Misha happily signs the words stops me in my tracks. In hindsight, I really could have worded that better."
"ฉันผงะไปเมื่อเห็นสายตาซึ่งชวนให้เย็นเยือกจากชิซูเนะที่จ้องมาหลังจากที่เห็นมิช่าแปลให้แล้ว พอนึกดูแล้ว ฉันเองก็\nน่าจะเลือกใช้คำให้มันดี ๆ หน่อย"

show hanako emb_sad:
    xpos 1.05
with dissolvecharamove

# "Out of the corner of my eye, I'm sure I see Hanako move back. Just a little."
"เหมือนจะเห็นฮานาโกะที่ถอยออกไปแล้วอยู่ตรงหางตา แต่ก็ถอยไปแค่นิดหน่อยอะนะ"

show shizu basic_angry
with charachange

# "Thankfully, Shizune notices this and lets her temper dissipate as she forcefully runs her hand through her hair to let off steam. Perfectly on cue, Misha begins interpreting the second Shizune's arms begin to move."
"แต่โชคดีที่ชิซูเนะรู้ตัวแล้วรอให้ตัวเองใจเย็นลงพลางสางผมตัวเองแรง ๆ เป็นการระบายอารมณ์ มิช่าก็เข้ามาแปลทันที\nที่แขนของชิซูเนะขยับอย่างรู้งาน"

show shizu behind_frown
with charachange

shi "…"

show misha hips_frown
with charachange

# mi "I would say that such matters aren't relevant to you, but since you seem to have befriended Lilly…"
mi "ปกติฉันคงบอกไปว่าไม่เกี่ยวกับนายหรอก แต่ในเมื่อเห็นนายเป็นเพื่อนกับลิลลี่อย่างนี้แล้ว…"

show shizu adjust_frown
with charachange

# "She pauses to adjust her glasses, evidently attempting to articulate her point in the best possible manner."
"ชิซูเนะหยุดไปแล้วดันแว่นตัวเอง ชัดว่ากำลังคิดหาทางที่จะสื่อสารประเด็นออกมาให้ได้ดีที่สุด"

show shizu basic_angry
with charachange

shi "…"

show misha sign_smile
with charachange

# mi "While I assume the same of her, I cannot call my own views on the matter unbiased. Suffice to say, we were closer before than we are now."
mi "ความคิดเห็นของฉันไม่ได้เป็นกลางแน่ ๆ ละ แต่อีกฝั่งเองก็คงไม่ได้มองแบบเป็นกลางเหมือนกัน แต่ที่แน่ ๆ คือเมื่อก่อน\nเราสองคนเคยสนิทกันกว่านี้"

show shizu behind_frown
show misha sign_confused
with charachange

# "Shizune makes a quick gesture to Misha to stop her from interpreting, then has a quick meeting with her before proceeding. The fact that the two can communicate so easily yet so secretly right in front of us is slightly disconcerting."
"ชิซูเนะทำมืออะไรสักอย่างเร็ว ๆ เป็นสัญญาณให้มิช่าหยุดแปล จากนั้นทั้งสองคนก็ประชุมกัน เห็นคุยกันได้ง่าย ๆ แถม\nดันเก็บเป็นความลับได้อย่างนี้อยู่ซึ่ง ๆ หน้าแล้วก็หงุดหงิดหน่อย ๆ แฮะ"

show hanako basic_normal
show shizu basic_normal2
show misha sign_sad
with charachange

# "Hanako seems to share my curiosity at the proceedings, looking on with thinly-masked interest. As they finish their opaque conversation, Misha looks slightly deflated. I guess her opinion on the matter wasn't followed."
"ฮานาโกะเองก็ดูจะอยากรู้เหมือนกับฉัน เพราะเธอกำลังมองด้วยสีหน้าสงสัยที่ปิดแทบไม่มิด พอบทสนทนาสุดโปร่งใส\nของทั้งสองคนจบลงมิช่าก็ดูหงอยลงเล็กน้อย ดูท่าว่าความเห็นของเธอจะส่งไปไม่ถึงอีกคน"

show misha perky_confused
with charachange

# mi "Shicchan says you should ask Lilly about it, as she doesn't want to be the one that gets you involved."
mi "ชิจังบอกว่าให้นายไปถามลิลลี่น่าจะดีกว่า เพราะชิจังไม่อยากเป็นคนลากนายไปเกี่ยวด้วยตัวเอง"

# "Ah well. I'll just have to ask her after she gets back. At least I got some information out of Shizune; the two having been on close terms means that they weren't always at each other's throats, or at least not quite to this extent."
"เอาเถอะ เดี๋ยวค่อยถามตอนลิลลี่บินกลับมาแล้วกัน อย่างน้อยก็ได้รู้จากชิซูเนะแล้วว่าเมื่อก่อนก็สนิทกันดี หรืออาจจะ\nไม่ได้สนิทมากหรอก แต่ก็ไม่ได้จ้องจะตีกันขนาดนี้"

# hi "I understand. Thanks anyway."
hi "เข้าใจละ แต่ก็ขอบคุณนะ"

stop music fadeout 8.0

show shizu invis at offscreenleft
show misha invis at offscreenleft
show hanako basic_normal at center
show bg school_scienceroom at center
with dissolvecharamove

# "With a nod and a farewell the two break away and walk out the door, no doubt headed straight for the student council room."
"ทั้งสองคนพยักหน้าแล้วบอกลาเดินออกไปทางประตู ซึ่งก็คงไปห้องสภานักเรียนนั่นแหละ"

# hi "…Could have gone worse, I suppose."
hi "…ก็ยังดี ละมั้ง"

show hanako cover_bashful
with charachange

# "Hanako lets out a long breath, relieved at the confrontation's resolution. I can't say I blame her."
"ฮานาโกะถอนหายใจพรืดด้วยความโล่งใจที่เรื่องจบลงแล้ว ซึ่งก็ไม่แปลกที่จะรู้สึกอย่างนั้น"

show hanako basic_bashful
with charachange

# ha "I'll see you later, then?"
ha "งั้นเดี๋ยวเจอกันนะ"

# hi "Yeah, I'll meet you in the tea room. Seeya."
hi "อื้ม เดี๋ยวเจอกันที่ห้องน้ำชานะ"

hide hanako
with charaexit

# "With that, she waves and joins the trickle of students leaving the classroom."
"และฮานาโกะก็โบกมือลาแล้วไหลไปตามกลุ่มนักเรียนที่ทยอยออกจากห้องไป"

show muto normal at center
with charaenter

# mu "Nakai, could I speak with you for a moment?"
mu "นากาอิ ครูขอคุยด้วยหน่อยได้ไหม"

# "Delivered in his typical monotone manner. He apparently decided that I need a reminder to see him already."
"น้ำเสียงราบเรียบเช่นเคย ดูท่าว่าจะอยากเตือนฉันให้มาคุยด้วยแล้ว"

hide muto
with charaexit

# "Eventually I finish packing up my things. By the time I reach his desk the classroom is close to empty."
"ฉันเก็บข้าวของจนเสร็จ กว่าจะเดินมาถึงโต๊ะครู ทั้งห้องก็แทบไม่เหลือใครแล้ว"

# hi "Uh… yes, sir?"
hi "เอ่อ… มีอะไรเหรอครับ"

play music music_happiness fadein 5.0

show muto normal at center
with charaenter

# "He looks up, taking measure of my face before giving an awkward, rather obviously acted, chuckle."
"ครูเงยหน้าขึ้นมองหน้าฉันก่อนจะทำเป็นแค่นหัวเราะแห้ง ๆ"

show muto smile
with charachange

# mu "No need to feel guilty, you're not in any trouble. I just want to ask you something I've asked a few of the other students so far."
mu "ไม่ต้องกลัว ไม่ได้มีเรื่องอะไรหรอก พอดีถามนักเรียนคนอื่นมาแล้วเลยอยากถามเธอบ้าง"

# "That's something at least. For a moment, I'd thought my maxim of keeping my head down and pen up had failed me."
"ก็นับว่ามีน่ะแหละ แวบหนึ่งฉันคิดไปว่าหลักการตั้งใจก้มหน้าจดนั้นใช้การไม่ได้เสียแล้ว"

# hi "So what did you want to talk about?"
hi "แล้วจะคุยเรื่องอะไรเหรอครับ"

show muto normal
with charachange

# mu "To start with, what do you think of your progress in this class, so far? Good? Bad?"
mu "ก่อนอื่น เธอรู้สึกว่าการเรียนของตัวเองกับวิชานี้เป็นยังไง ตามทันมั้ย รู้เรื่องหรือเปล่า"

# "I detest that kind of question. For a fair amount of time I try to think of a response that is neither pathetically humble, nor cocky."
"เกลียดคำถามแบบนี้ชะมัด ฉันนึกหาคำตอบที่ไม่ได้ดูถ่อมตัวจนหัวทิ่มดิน แต่ก็ไม่ได้ดูเป็นการอวดด้วย"

# hi "I'd say I'm doing okay. The work doesn't seem too hard, and I'm doing better on the tests than I thought I would."
hi "ก็ใช้ได้อยู่นะครับ งานก็ไม่ได้ยากมาก ผลสอบก็ออกมาดีกว่าที่คิดด้วย"

show muto smile
with charachange

# mu "That's a good answer. A correct one, too."
mu "ตอบได้ดี ตอบได้ถูกต้อง"

# "I give a mental sigh of relief at his satisfaction. To say that I don't gain a little pride from his comment would be a blatant lie."
"ฉันโล่งใจที่ครูพอใจกับคำตอบนั้น จะให้ปฏิเสธว่าไม่ได้รู้สึกภูมิใจกับคำพูดของครูเลยก็คงไม่ได้"

# "In the maelstrom of thoughts clouding my mind after learning that I'd be transferring to Yamaku, my school grades seemed utterly unimportant."
"ความคิดของฉันที่ปั่นป่วนวุ่นวายหลังจากที่ได้รู้ว่าต้องย้ายมาที่ยามากุนั้นทำให้ความสำคัญเรื่องผลการเรียนนั้นลดลง\nเป็นอย่างมาก"

# "Being entirely clueless as to what skill level would be assumed of me, once I actually got here I was hugely relieved when I found out that I understood well enough the schoolwork we'd be doing."
"ฉันเองก็ไม่รู้ว่าเนื้อหาที่จะได้มาเจอนั้นจะไปไกลขนาดไหนแล้ว เพราะอย่างนี้ฉันถึงได้โล่งใจที่พอได้ย้ายมาเรียนจริง ๆ\nแล้วก็ยังเรียนรู้เรื่องดีอยู่"

show muto normal
with charachange

# mu "I know your circumstances might have thrown a wrench in the works, but have you given any thought to your future?"
mu "ครูเข้าใจนะว่าเธอคงเจออะไรหลายอย่างจนไม่ทันได้คิด แต่เธอพอจะมองลู่ทางในอนาคตไว้หรือยัง"

# hi "My future?"
hi "อนาคตเหรอครับ"

# mu "What you'd like to do as a profession. Do you have any thoughts of where you'd like to be in ten or twenty years' time?"
mu "พวกอาชีพที่อยากทำน่ะ เคยคิดหรือเปล่าว่าสักสิบยี่สิบปีข้างหน้าตัวเองจะเป็นอะไรยังไงบ้าง"

# mu "I wouldn't be surprised if you covered this ground in your previous school, but I don't have any record of it if you have."
mu "ซึ่งครูก็คงไม่แปลกใจหรอกถ้าเธอเคยตอบคำถามนี้จากโรงเรียนเก่ามาแล้ว แต่ต่อให้เคยตอบจริง ข้อมูลที่ว่าก็ไม่ได้อยู่\nในมือครูเลย"

# "I suppose the last year of high school is the time when students would need to be thinking about such things. To be honest, I really haven't lent it much thought, compared to my immediate situation."
"ชั้นปีสุดท้ายแล้วเหล่านักเรียนคงต้องมาคิดเรื่องพวกนี้กันสินะ แต่ว่าตามตรง ฉันไม่ค่อยได้คิดถึงเรื่องนั้นเท่าไหร่\nส่วนใหญ่ก็คิดแต่เรื่องที่อยู่ตรงหน้าตอนนี้เลยมากกว่า"

# "Catching on to my thinking, Mutou speaks up."
"คุณครูพูดเสริมเมื่อรู้ว่าฉันคิดอะไรอยู่"

# mu "It's okay if you haven't decided on anything specific yet. I wouldn't be surprised if a lot of your classmates were still undecided, after all. Maybe pursue one of your talents?"
mu "ถ้ายังไม่ได้มีเส้นทางอะไรที่ชัดเจนก็ไม่เป็นไรหรอก ยังไงคนอื่นในห้องก็คงไม่ต่างกันเท่าไหร่ งั้นลองเดินตามทางที่\nตัวเองถนัดดูก็น่าจะดีนะ"

# "He's rather obviously trying to squeeze an answer out of me, and something about his previous wording makes me suspicious."
"ค่อนข้างชัดว่าอยากได้คำตอบจากฉันมาก ๆ และการเลือกใช้คำของครูเมื่อกี้ก็ทำให้ฉันสงสัย"

# "He didn't seem to be intent on asking everybody like this, so he must have some kind of selection criteria. At a guess, our grades in his class."
"ดูท่าว่าจะไม่ได้ไปไล่ถามทุกคนอย่างนี้ด้วย คงต้องมีเกณฑ์อะไรสักอย่างที่ใช้เลือก ถ้าให้เดาก็คงเป็นเกรดวิชาที่เขาสอน"

# hi "Well, something in science might be the path of least resistance."
hi "อืม พวกกลุ่มวิทยาศาสตร์น่าจะไปได้ง่ายอยู่นะครับ"

# "His face brightens, no doubt pleased at the thought of a prized student following his subject as a career path."
"คุณครูยิ้ม ชัดว่าพอใจที่นักเรียนดีเด่นของเขาเลือกเดินตามเส้นทางวิชาของตัวเอง"

show muto smile
with charachange

# mu "Good. Having a general idea is the first step. I would advise you to think on it, though."
mu "ดี เริ่มด้วยการดูไปคร่าว ๆ นี่แหละดีแล้ว แต่ยังไงครูก็ขอแนะนำให้เธอไปคิดดี ๆ นะ"

# hi "I will. Things are kinda settling down, which will help."
hi "ครับ ช่วงนี้อะไร ๆ เริ่มลงตัวแล้ว น่าจะพอมีเวลาให้คิดบ้าง"

# mu "Good to hear. Oh, and I've noticed that Ikezawa's attendance and grades have improved since you came to be friends. I'd like to thank you for that."
mu "งั้นก็ดีแล้ว อ้อ ตั้งแต่เธอเป็นเพื่อนกับอิเคซาวะ เกรดของอิเคซาวะดีขึ้นนะ เข้าเรียนบ่อยขึ้นด้วย ยังไงครูก็ขอ\nขอบคุณเธอนะ"

# hi "I'm surprised you noticed we knew each other."
hi "รู้ด้วยเหรอครับเนี่ยว่าเราสองคนเป็นเพื่อนกัน"

# "He gives a chuckle as awkward as his smile."
"เขาแค่นหัวเราะแกน ๆ ซึ่งแกนพอ ๆ กับรอยยิ้มของเขา"

# "This guy really has no idea how to properly act around others. Every facial movement seems like an act of careful but misdirected choreography."
"คุณครูคนนี้นี่วางตัวตอนอยู่กับคนอื่นไม่เป็นเลยจริง ๆ สีหน้าแต่ละอย่างดูแล้วก็เหมือนการแสดงที่ถูกควบคุมมาอย่างดี\nแต่ดันควบคุมไปผิดทาง"

show muto normal
with charachange

# mu "You could say that having a general idea of who knows whom is part of a teacher's job."
mu "ให้ว่าแล้ว งานของครูอย่างหนึ่งก็คงเป็นการรู้แบบคร่าว ๆ ว่าใครรู้จักใครยังไงนี่ละนะ"

# "Catching himself before he goes off on a tangent, he loudly coughs into his hand."
"เมื่อรู้ตัวว่าเริ่มออกนอกเรื่องครูก็กระแอมใส่กำปั้นตัวเองดัง ๆ"

# mu "I'm sure you have things to do, though, so I'll stop there. Please do think about where you're headed from here, as you don't have long to go before you finish high school."
mu "เธอคงมีธุระอะไรของเธออีก ครูจะไม่รบกวนต่อแล้วกัน ยังไงก็ไปคิดมานะว่าจากนี้จะเอายังไงต่อ อีกไม่นานเธอก็จะ\nเรียนจบแล้ว"

# hi "I will. Thanks."
hi "ได้ครับ ขอบคุณครับ"

stop music fadeout 4.0

scene bg school_hallway3
with locationchange

# "The brief talk ended, I take my leave. He goes back to fussing with the teaching materials on his desk."
"พอคุยกันเสร็จแล้วฉันก็ขอตัวออกมา ส่วนครูก็ง่วนอยู่กับสื่อการสอนของตัวเองอยู่กับโต๊ะ"

# "This is one of the times I'm envious of Lilly, almost maddeningly so. To have one's future so clear and so assured, yet working towards it from such a young age…"
"ฉันนึกอิจฉาลิลลี่ขึ้นมาอีกแล้ว อิจฉาเสียจนน่าหงุดหงิด ทั้งมีเส้นทางในอนาคตที่ชัดเจนและมั่นคงแล้ว แถมเริ่ม\nออกเดินตั้งแต่อายุยังน้อย…"

# "It's an idea so utterly irreconcilable with my own thoughts, mired in the present day just as they've always been."
"เป็นความคิดที่สมองของฉันซึ่งอัดแน่นไปด้วยสถานการณ์ในปัจจุบันนี้ไม่อาจยอมรับได้"

scene black
with dissolve

#**************************************

label th_L10:

scene bg school_lobby
with locationchange

# "Walking through the lobby to the cafeteria, I silently rue my daily routine having been completely thrown off."
"ฉันเดินผ่านโถงไปยังโรงอาหารพลางรำพึงถึงกิจวัตรประจำวันที่ถูกทำให้เสียไปอยู่เงียบ ๆ"

# "It had seemed like a normal day; I arrived in class before most, due to waking early and having become quite adept at chucking down my pills without choking as I get ready for the day."
"เป็นวันที่ดูไม่มีอะไร มาเรียนก่อนคนอื่นเพราะตื่นเช้าและกระเดือกยารอบเช้าแบบไม่ให้สำลักได้ค่อนข้างคล่องแล้ว"

# "But as students trickled in, one never materialized. Hanako."
"ทว่า ในกลุ่มนักเรียนที่ทยอยเข้าห้องมานั้น ไม่มีฮานาโกะอยู่เลย"

play ambient sfx_crowd_indoors fadein 0.5
scene bg school_cafeteria at right
show crowd at left
with locationchange

# "I step inside, my eyes scanning the expanse of the cafeteria in search of a suitable place to take a seat. It's a task made more difficult by the groups of students moving about and busily talking."
"ฉันเดินเข้ามาพลางสอดส่ายสายตามองหาที่นั่งเหมาะ ๆ ในพื้นที่ของโรงอาหารแห่งนี้ ซึ่งหาได้ยากเพราะยังมีกลุ่ม\nนักเรียนที่เดินกันขวักไขว่คุยกันจอแจอยู่"

play sound sfx_impact2
with vpunch
$ renpy.music.set_volume(0.5, 0.3, channel="ambient")

# hi "Geh!"
hi "อุ่ก!"

# "A hand pounds my back hard a couple of times, severely winding me."
"มีคนมาทุบหลังฉันแรง ๆ สองครั้งจนฉันจุก"

$ renpy.music.set_volume(0.0, 0.0, channel="ambient")
scene black
with shuteyefast

# "I couldn't care less about the culprit as I focus my thoughts on my chest in a near-automatic reaction."
"สมองฉันจดจ่ออยู่กับหน้าอกไปโดยแทบจะอัตโนมัติจนไม่เหลือที่ว่างที่จะคิดว่าใครเป็นคนทำ"

play sound sfx_heartfast
show heartattack alpha 
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

# "My hand instinctively tightens on my breast, and I start going through the steps I rehearse in my mind every other day."
"มือของฉันขึ้นมากุมหน้าอกไปโดยสัญชาตญาณ และทำตามขั้นตอนที่ท่องอยู่ในใจแทบทุกวัน"

play sound sfx_heartfast
show heartattack alpha 
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

# "Breathe steadily… in… and out…"
"หายใจช้า ๆ … เข้า… ออก…"

play sound sfx_heartslow
show heartattack alpha 
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.7)

# "With a measure of relief, I can slowly feel my chest becoming less tense. By the time I look back up, my face is covered in sweat from the experience."
"พอหน้าอกหายแน่นลงบ้างแล้วจึงโล่งใจ พอเงยหน้าขึ้นก็รู้สึกถึงเหงื่อที่ผุดขึ้นเต็มหน้าจากเหตุการณ์เมื่อครู่"

$ renpy.music.set_volume(1.0, 5.0, channel="ambient")

scene bg school_cafeteria  at right
show crowd at right
show kenji happy_close at center
with openeye

# ke "Hey… man, are you okay?"
ke "เฮ้ย… พวก ไหวปะเนี่ย"

# hi "GODDAMNIT! Don't {b}do{/b} that, you idiot!"
hi "ปัดโธ่เว้ย!! อย่า{b}ทำ{/b}อย่างนั้นสิวะ ไอ้บ้า!"

show kenji tsun
with charadistant

# "He retreats back, an expression of unease written on his face. In hindsight, I probably shouldn't have barked at him, considering he had no way to know."
"เคนจิถอยกรูดพร้อมสีหน้าอึดอัด พอย้อนคิดดูแล้วก็ไม่น่าไปตวาดใส่อย่างนั้นเลย เพราะเขาคงไม่รู้ว่าฉันเป็นอะไร"

# "I give a sigh and right myself with some difficulty."
"ฉันถอนหายใจแล้วจัดแจงตัวเองให้เข้าที่ด้วยสภาพเก้กังเล็กน้อย"

# hi "Sorry. I just have some… chest problems. Sharp knocks aren't good."
hi "โทษที พอดี… หน้าอกฉันมีปัญหานิดหน่อยน่ะ โดนทุบแรง ๆ ไม่ได้"

# "It seems strange to see him so upset. The fact that I can't do anything about it irritates me."
"เห็นเคนจิตกใจแล้วก็แปลกตาเหมือนกัน หงุดหงิดแฮะที่แก้อะไรไม่ได้"

# hi "Let's get lunch."
hi "ไปเอาข้าวกัน"

show kenji neutral
with charachange

# ke "Okay. It's good to have some company, for once."
ke "ได้ มีเพื่อนกินด้วยสักครั้งก็ดีเหมือนกัน"

hide kenji
with charaexit

show bg school_cafeteria at left
show crowd at left
with charamove

# "We start off to the serving line. One good thing is that Kenji and I can make small talk nowadays, as opposed to my only interaction with him being anti-feminist lectures."
"พวกเราไปต่อแถวรอรับข้าว ยังดีที่ว่าทุกวันนี้ฉันคุยอะไรเรื่อยเปื่อยกับเคนจิได้แล้ว ไม่ใช่ได้แต่นั่งฟังเขาพล่าม\nบทบรรยายเรื่องการต่อต้านสตรีนิยม"

# hi "Seems like it'd be hard to find an empty table."
hi "ดูท่าว่าคงหาที่ว่างยากหน่อยนะ"

show kenji neutral at center
with charaenter

# ke "There's a few people I wouldn't mind sitting with. Nobody's like you, though."
ke "ก็พอมีคนที่ฉันนั่งด้วยได้แหละ แต่ไม่มีใครเหมือนนาย"

$ renpy.music.set_volume(0.0, 0.5, channel="ambient")

# "I feel a shiver run through my spine."
"ฉันเสียวสันหลังวาบขึ้นมา"

# hi "Clarify that now."
hi "อธิบายท่อนท้ายให้ชัด ๆ ทีดิ๊"

play music music_kenji fadein 2.0

show kenji tsun
with charachange

# ke "They don't listen. Their minds are closed. It's the media, man, the Goddamn brainwashing mainstream feminist Fascist media."
ke "พวกนั้นปิดใจไม่ฟังกันเลย เพราะสื่อนี่แหละ สื่อกระแสหลักสตรีนิยมฟาสซิสต์ล้างสมอง"

# "He takes a breath, and I savor the second of silence."
"เคนจิสูดหายใจ ส่วนฉันก็ได้พักในช่วงวินาทีที่เขาเงียบไปนี้"

$ renpy.music.set_volume(1.0, 10.0, channel="ambient")

# ke "Damn, they control everything. Everything but you and me."
ke "ให้ตาย พวกนั้นควบคุมทุกอย่างเลย ทุกอย่าง ยกเว้นนายกับฉัน"

# "I relax a little while we grab our food and drink."
"ฉันพักอีกหน่อยช่วงที่เรากำลังไปเอาของกินกัน"

show kenji happy
with charachange

# ke "So, what've you got for me?"
ke "แล้วว่าไงบ้าง"

# hi "Huh?"
hi "ฮะ?"

show kenji neutral
with charachange

# ke "Come on, you've been hanging around Satou and that other chick for ages now. Rumors are all over my class, and probably some of the others too."
ke "เนี่ย นายก็อยู่กับซาโต้แล้วก็สาวอีกคนนั่นมานานแล้ว ข่าวลือแพร่สะพัดทั่วห้องเรียนฉันเลย เผลอ ๆ ไปถึงห้องอื่นด้วย"

# hi "Eavesdropping isn't a good habit."
hi "แอบฟังมันไม่ดีนะ"

show kenji happy
with charachange

# ke "Let me guess, you never do it? Not even when you're bored? Really?"
ke "ให้เดานะ นายไม่เคยแอบฟังเลย? ตอนเบื่อ ๆ ก็ไม่ทำ? จริงดิ"

# hi "Well… I… uh…"
hi "ก็… ฉัน… เอ่อ…"

# hi "Fine. Point taken."
hi "เออ ก็ถูก"

hide kenji
with charaexit

# "Both of us stop to have soup ladled into a couple of small bowls and placed onto our trays. The concoction that lands into the bowl looks pretty questionable, but at least it smells reasonably good."
"พวกเราถือถ้วยเล็ก ๆ สองใบมารอรับซุป ก่อนจะเอาไปวางในถาดของตัวเอง วัตถุเหลว ๆ ที่อยู่ในถ้วยนั้นดูไว้ใจไม่ค่อยได้\nแต่อย่างน้อยก็หอมดี"

stop ambient fadeout 1.0

show bg school_cafeteria at center
show crowd at Alphaout(1.0), center
show kenji invis at center
with charamove

show kenji neutral:
    ypos 1.14
hide crowd
with dissolvecharamove

# "As we take our seats at a miraculously free table, I try to think of something that would actually interest him at all. I hope I can come up with an acceptable topic."
"พวกเรามานั่งที่โต๊ะว่าง ซึ่งปาฏิหาริย์มากที่ยังมีที่ว่าง ฉันนึกดูว่าพอจะมีอะไรที่เคนจิสนใจบ้างหรือเปล่า หวังว่าจะมีเรื่อง\nอะไรกลาง ๆ ที่พอคุยกันได้นะ"

# hi "I found an answer to that question you asked a couple of weeks back. Where Lilly's non-Japanese half comes from, that is."
hi "คำถามที่นายถามไปเมื่อสองสัปดาห์ที่แล้วน่ะฉันได้คำตอบมาแล้วนะ ที่ถามว่าอีกครึ่งที่ไม่ใช่ญี่ปุ่นของลิลลี่คือที่ไหน"

show kenji happy
with charachange

# ke "Good man. It's Russia, right? Totally Russia."
ke "ดี ๆ รัสเซียใช่มั้ย รัสเซียแน่ ๆ"

# hi "Scotland."
hi "สกอตแลนด์"

show kenji tsun
with charachange

# "He's visibly stopped in his tracks."
"เขาชะงักไปอย่างเห็นได้ชัด"

# ke "…Scotland?"
ke "…สกอดแลนด์เหรอ"

# hi "Yeah, that was my reaction too. She can speak English fluently and everything."
hi "อืม ตอนรู้ฉันก็สภาพนั้นแหละ แถมยังเก่งภาษาอังกฤษมากด้วย"

show kenji rage
with charachange

# ke "…Damn it! Do you realize what this means? How terrifying this news is to me?"
ke "…ให้ตายเถอะ! รู้มั้ยว่ามันหมายความว่าอะไร รู้มั้ยว่าฉันตกใจกับสิ่งนี้มาก"

label th_choiceL10_1:
menu:
    with menueffect

    # "I think he's hyperventilating. Passing out for a little while would probably make him more relaxed than he normally is."
    "เหมือนจะหายใจเกินแล้ว ปล่อยให้สลบไปสักพักน่าจะช่วยให้เพลา ๆ ลงจากปกติได้บ้าง"

    # "Humor him.":
    "ตามน้ำ":
        return m1
        
    # "Ignore his insane ramblings.":
    "เมินที่พล่ามไปเรื่อย":
        return m2

label th_L10a:

# hi "I have no idea what it means. Enlighten me."
hi "ไม่รู้เลยว่ะ บอกหน่อย"

# ke "I just lost 1000 yen, man! 1000 yen! Damn, this is the worst day ever."
ke "ฉันเสีย 1,000 เยนไปแล้ว! 1,000 เยน! ให้ตาย วันนี้มันวันเฮงซวยจริง ๆ"

label th_L10b:

# "I dig into my food, hoping he'll take the hint from my silence."
"ฉันกินข้าวด้วยหวังว่าเคนจิจะรู้ตัวจากการที่ฉันเงียบไป"

# ke "I just lost 1000 yen, man! 1000 yen! Damn, this is the worst day ever."
ke "ฉันเสีย 1,000 เยนไปแล้ว! 1,000 เยน! ให้ตาย วันนี้มันวันเฮงซวยจริง ๆ"

# "No such luck."
"เปล่าประโยชน์"

label th_L10c:

# hi "You're kidding me. You made a bet about her nationality?"
hi "ล้อเล่นปะเนี่ย นี่ไปพนันเรื่องเชื้อชาติของลิลลี่มาเหรอ"

show kenji tsun
with charachange

# ke "One of the dudes in my class was bugging me about it. I gave him some of my wisdom, and he had the audacity to say my logic was wrong."
ke "มีไอ้คนหนึ่งในห้องมาตื๊อฉัน ฉันเลยแผ่ปัญญาของตัวเองไปให้ แล้วยังมีหน้ามาบอกว่าตรรกะของฉันผิดอีก"

# hi "So what did he think?"
hi "แล้วเขาเดาว่าไง"

# ke "Eh, Germany or something. It doesn't matter. What matters is my 1000 yen."
ke "เอ่อ เยอรมันหรืออะไรนี่ละมั้ง แต่ไม่สำคัญหรอก ที่สำคัญคือ 1,000 เยนของฉันเนี่ย"

show kenji rage
with charachange

# ke "Damn, this day is ruined thanks to her. What a bitch."
ke "ให้ตาย เพราะยัยนั่นแท้ ๆ ทำอารมณ์เสียเลย บัดซบ"

show kenji tsun
with charachange

# "He looks utterly devastated as he wolfs down several clumps of his soggy soy-soaked rice. It only takes a few mouthfuls before he pokes his chopsticks at me, stabbing the air repeatedly in revelation."
"เขาทำสิ้นหวังสุดขีดพลางสวาปามก้อนข้าวชุ่มซีอิ๊ว กินไปได้ไม่กี่คำก็ชี้ตะเกียบมาทางฉันแล้วทำท่าจิ้มกลางอากาศ\nรัว ๆ คล้ายจะประกาศบางอย่าง"

# ke "Why… mm… mm… would… mm…"
ke "คน… หงุบ… หงุบ… ที่ไหน… อืม…"

# hi "Didn't your mother ever tell you not to speak with your mouth full?"
hi "แม่ไม่สอนเหรอว่าห้ามพูดตอนกินข้าวอะ"

# "He gives me a dirty look before choking down the rest of the food left in his mouth and taking a gulp of juice. It's rather unsightly."
"เคนจิส่งสายตาอาฆาตก่อนจะกระเดือกข้าวที่อยู่ในปากแล้วตามด้วยน้ำผลไม้อีกหนึ่งอึก เป็นภาพที่ไม่น่าดูเอาเสียเลย"

# "Remembering my own food sitting in front of me, I decide to get the task of eating the cafeteria food over and done with as fast as possible. The sooner I do so, the sooner the experience will be over."
"พอนึกได้ว่าตัวเองก็ยังมีข้าวที่ต้องกินอยู่ก็รีบกินข้าวของโรงอาหารให้หมด ๆ ให้เร็วที่สุด ยิ่งหมดเร็วก็ยิ่งไม่ต้องอยู่\nแตะลิ้นนาน"

show kenji neutral
with charachange

# ke "So as I was saying,"
ke "เออนั่นแหละ"

show kenji tsun
with charachange

# ke "Why would anyone want to live in that place anyway? I mean, what is there to see? Grassy plains. That's it. Lots and lots of grassy plains."
ke "คนที่ไหนเขาจะอยากไปอยู่ที่นั่นวะ แบบ มันมีอะไรน่าดูเหรอ มีแต่ทุ่งหญ้า แค่เนี้ย ทุ่งหญ้า ทุ่งหญ้าเต็มไปหมด"

# ke "And men in kilts."
ke "กับผู้ชายใส่กระโปรงคิลต์"

# "I'm not sure which is worse, this food or his world view. I can feel my face being dragged down by their combined weight. Not that he'd notice, or care."
"ระหว่างกับข้าวในถาดนี่ กับมุมมองของเคนจิ ชักไม่แน่ใจแล้วว่าอย่างไหนแย่กว่ากัน รู้สึกทั้งสองอย่างจะถ่วงจนหน้าฉัน\nดูเครียดไปแล้ว แต่เคนจิก็ไม่ได้สังเกตหรือใส่ใจอยู่ดีน่ะนะ"

# hi "It's not that bad. Why do you care about her so much anyway? She's just your class representative, after all."
hi "ก็ไม่ขนาดนั้นสักหน่อย แล้วจะมาสนใจเรื่องลิลลี่อะไรขนาดนี้ ก็เป็นแค่หัวหน้าห้องห้องนายเองนี่"

show kenji neutral
with charachange

# "He gives a malevolent chuckle. Were this anyone but Kenji, I'd feel uneasy at how he sounds."
"เขาหัวเราะหึ ๆ ถ้าไม่ใช่เคนจิแล้วฉันคงสยองกับเสียงนั้นแน่ ๆ"

# ke "I finally found the chink in the feminist legion's armor. It took a while, but I'm confident that this is going to be how we can bring down the whole system."
ke "ฉันเจอรอยแตกบนชุดเกราะกองกำลังสตรีนิยมแล้วละ ถึงจะใช้เวลานานหน่อย แต่ฉันมั่นใจว่านี่แหละจะเป็นลู่ทาง\nให้เราโค่นล้มทั้งระบบได้"

show kenji happy
with charachange

# ke "I'm about to blow your mind. Are you ready?"
ke "ฉันจะเปิดโลกนายเลย พร้อมหรือยัง"

stop music fadeout 2.0

# "I tune out his rambling for a moment as I finish my rice and start on the unappetizing soup. One taste is enough to confirm that it's cold."
"ฉันเมินที่เขาพล่ามไปครู่หนึ่งตอนที่กินข้าวหมดแล้วหันมากินซุปที่ดูไม่น่าอร่อยต่อ ช้อนเดียวก็รู้เลยว่าเย็นชืดแล้ว"

# hi "Ready as I'll ever be."
hi "พร้อมเหมือนทุกทีแหละ"

show kenji happy
with charachange

# ke "I confirmed that Lilly is in the Mafia."
ke "ฉันรู้แล้วว่าลิลลี่อยู่ในกลุ่มมาเฟียซิซิลี"

play music music_kenji

# hi "What."
hi "อะไรวะ"

show kenji neutral
with charachange

# ke "All right, stay with me for a second here, and I'll describe the scene."
ke "เอาละ ฟังฉันก่อนนะ เดี๋ยวจะแจกแจงให้ฟัง"

# "I wish I could do otherwise."
"ไม่ฟังได้หรือเปล่า"

# ke "Lilly's there, walking down the street after school."
ke "มีวันหนึ่ง ลิลลี่เดินไปตามถนนหลังเลิกเรียน"

# hi "You're not stalking her, are you?"
hi "นี่ไม่ได้แอบตามลิลลี่ไปใช่มั้ย"

show kenji tsun
with charachange

# ke "No! Damn man, I do have some sense of self-preservation."
ke "ไม่เว้ย! ให้ตาย ฉันก็รักตัวกลัวตายเหมือนกันนะ"

# "But not dignity, or morals, or social standards…"
"แต่ไม่ได้รักเกียรติ ศีลธรรม หรือบรรทัดฐานทางสังคม…"

show kenji neutral
with charachange

# ke "Anyway, as I was saying. This car pulls up next to her, and guess who steps out? A man in a pinstripe suit. Waves her in, then the two leave just like that. I tell you man, she's under protection. Under. Protection."
ke "แต่นั่นแหละ ทีนี้มีรถคันหนึ่งมาจอดข้าง ๆ แล้วรู้มั้ยใครลงจากรถมา ผู้ชายใส่ชุดสูทลายทางเว้ย โบกมือเรียกยัยนั่น\nให้ขึ้นรถไป แล้วก็บึ่งรถออกไปเลย บอกเลยนะ ยัยนั่นน่ะมีคนคุ้มกันอยู่ มีคน คุ้มกัน"

# "A man in a… oh. I can see where this is going now. It takes effort not to sigh in exasperation."
"ผู้ชายใส่… อ้อ รู้ละว่าจะเป็นยังไงต่อ ฉันต้องกลั้นใจไม่ให้ตัวเองถอนหายใจด้วยความระอา"

# hi "Let me guess; this man was about average height, had a slightly slender build, had blonde hair, looked foreign, and smiled a lot?"
hi "ให้เดานะ ผู้ชายคนนี้ไม่สูงไม่เตี้ย ค่อนข้างเพรียว ผมสีบลอนด์ ดูเป็นฝรั่ง ยิ้มบ่อย ใช่มั้ย"

show kenji rage
with charachange

# "He looks positively stunned. I take advantage of the moment of quiet to quickly gulp a mouthful of cold soup."
"เคนจิอึ้งกิมกี่ ฉันรีบถือจังหวะที่บรรยากาศเงียบไปนี้กลืนซุปอันเย็นชืดไปหนึ่งอึก"

show kenji tsun
with charachange

# ke "It seems you're more observant than I thought."
ke "ตาแหลมกว่าที่คิดนะนายเนี่ย"

show kenji neutral
with charachange

# ke "Yes, I have chosen well."
ke "ใช่เลย ฉันเลือกคนมาถูกจริง ๆ"

# "He giggles a little, and nods to himself so dramatically that it looks comical. I can't tell whether that's intentional or not, and that fact makes me frown."
"เขาหัวเราะคิกคักแล้วพยักหน้าหงึก ๆ ชวนขัน ไม่รู้ว่าจงใจทำอย่างนี้หรือเปล่า ฉันขมวดคิ้วด้วยความสงสัย"

show kenji happy
with charachange

# ke "This has important ramifications, you know. If she really is connected to people like them, and we're smart about what we do with this information, we could turn this into our greatest weapon against the Student Council."
ke "เนี่ย เรื่องนี้มันมีบทบาทสำคัญมากเลยนะ ถ้ายัยนั่นเกี่ยวพันกับคนพวกนั้นจริง แล้วเราฉลาดพอที่จะเอาข้อมูลนั้นมาใช้\nให้ถูกทาง เราก็จะได้อาวุธที่ทรงพลังที่สุดที่จะใช้ต่อต้านสภานักเรียนได้"

show kenji happy:
    2.0
    "kenji neutral" with Dissolve(0.5, alpha=True)
    3.0
    "kenji happy" with Dissolve(0.5, alpha=True)
    1.0
    "kenji neutral" with Dissolve(0.5, alpha=True)
    4.0
    "kenji tsun" with Dissolve(0.5, alpha=True)
    repeat

# "Once he starts rambling into conspiracy territory, my juice suddenly becomes of much more importance."
"พอเคนจิเริ่มพล่ามมาทางทฤษฎีสมคบคิดแล้ว อยู่ ๆ น้ำผลไม้ของฉันก็กลายเป็นเรื่องที่สำคัญกว่ามาก"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

nvl clear

window hide
nvl show dissolve

# n "\n\n\n\nOnly half-listening to his pontifications, my mind drifts to the matter of Lilly and her antipathy for Shizune."
n "\n\n\n\nฉันฟังบ้างไม่ฟังบ้างกับสิ่งที่เคนจิพล่าม ๆ โม้ ๆ ส่วนในหัวก็คิดไปถึงเรื่องที่ลิลลี่ไม่ถูกกับชิซูเนะ"

# n "The past between them is steadily becoming more coherent, but I'm not even sure if I should be learning of her past this way. Indeed, even if I do work out what went on, it really doesn't seem like my business to go and interfere."
n "อดีตของทั้งสองคนเริ่มโยงถึงกันมากขึ้น ฉันไม่แน่ใจนักว่ามารู้เรื่องอดีตของลิลลี่ด้วยวิธีแบบนี้ดีแล้วหรือเปล่า แต่\nต่อให้สืบจนรู้ว่าเกิดอะไรขึ้น มันก็ไม่ใช่กงการอะไรของฉันที่จะต้องเข้าไปยุ่มย่ามด้วยอยู่ดี"

# n "…Damn, not having Lilly around is making my thoughts wander. I'm noticeably more bored and sullen without her company, and the same goes for Hanako. All we do during lunch any more is eat and play chess."
n "…ให้ตาย พอลิลลี่ไม่อยู่แล้วใจก็วุ่นวาย เหมือนจะเบื่อจะหมองง่ายขึ้น ฮานาโกะก็ด้วย ตอนพักเที่ยงเราสองคนก็ได้แต่\nกินข้าวกับเล่นหมากรุกด้วยกัน"

# n "Come to think of it, I need to go check on Hanako after school, too. Considering her much improved attendance, I'm guessing she's come down with something."
n "จะว่าไป หลังเลิกเรียนต้องแวะไปดูฮานาโกะสักหน่อย ช่วงนี้เข้าเรียนบ่อยขึ้นแล้ว แปลว่าที่หายไปต้องมีเรื่องอะไรแน่ ๆ"

stop music fadeout 2.0
$ renpy.music.set_volume(1.0, 6.0, channel="music")

nvl clear

nvl hide dissolve

scene bg school_scienceroom
with shorttimeskip

play sound sfx_normalbell

window show

# mu "Oh, Nakai?"
mu "อ้าว นากาอิ"

show muto normal at center
with charaenter

# "I stop as I'm about to leave the classroom, turning on the ball of my heel to meet Mutou. He's holding out to me a couple of the worksheets we'd worked on during the day with his long, lanky arm."
"ฉันหยุดเดินจังหวะที่กำลังจะออกจากห้องแล้วหมุนส้นเท้าหันไปมอง คุณครูยื่นใบงานสองใบที่พวกเราได้ทำในคาบวันนี้\nมาด้วยแขนยาว ๆ ที่ดูผอมกะหร่องนั้น"

show muto smile
with charachange

# mu "Would you mind giving these to Ikezawa? I'd normally ask one of the girls to do it, but I assume you'll be checking on her."
mu "ฝากเอาไปให้อิเคซาวะหน่อยได้ไหม ปกติครูจะฝากพวกผู้หญิงไป แต่เดี๋ยวเธอคงแวะไปหาอยู่แล้วใช่มั้ย"

# "For a moment I briefly consider the possibility of that being more than an innocent prediction. I quickly discard the idea though, as it's hard to think of him acting in such a Machiavellian way. It's not in his nature."
"แวบหนึ่งฉันคิดไปว่าครูคงไม่ได้แค่คาดเดาไปแบบซื่อ ๆ แต่แล้วก็ปัด ๆ ความคิดนั้นทิ้งไป เพราะครูคงไม่ใช่คนที่วางแผน\nใช้คนเก่งอะไรขนาดนั้น ครูไม่ใช่คนอย่างนั้นเลย"

# hi "Sure, no problem."
hi "ครับ ได้เลยครับ"

scene bg school_girlsdormhall
with locationskip

play music music_night fadein 1.0

# "Walking up the hallway of the girl's dormitory, several ideas of why Hanako's been absent float around my head. The most obvious of them is just a simple cold."
"ฉันเดินไปตามโถงทางเดินหอหญิงพลางคิดถึงสาเหตุต่าง ๆ นานาที่ฮานาโกะขาดเรียนไป ที่ชัดที่สุดน่าจะเป็นแค่หวัด\nธรรมดา ๆ"

# "That said, she may not even be sick at all. It's been almost a week since Lilly left, and despite her at least appearing to be normal, I've suspected she's somewhat more insecure about it than she's letting on."
"ถึงอย่างนั้นก็เถอะ อาจจะไม่ได้ป่วยเลยก็ได้ ลิลลี่ไปสกอตแลนด์แล้วเกือบหนึ่งสัปดาห์ ถึงฮานาโกะจะทำตัวดูปกติก็จริง\nแต่ฉันก็สงสัยว่าจริง ๆ แล้วในใจเป็นกังวลกว่าที่แสดงให้เห็นหรือเปล่า"

show bg school_girlsdormhall at right
with charamove

# "Eventually I come to Hanako's dormitory room, its simple brown door separating us. Her room's position next to Lilly's is extremely convenient, and probably a large contributor to their meeting in the first place."
"จนในที่สุดก็มาถึงหน้าห้องฮานาโกะ มีเพียงประตูสีน้ำตาลเรียบ ๆ ที่คั่นกลางฉันกับตัวห้อง สะดวกดีที่ห้องฮานาโกะอยู่\nข้างห้องลิลลี่อย่างนี้ แถมน่าจะเป็นสาเหตุหลัก ๆ ที่ทั้งสองคนมารู้จักกันเลยด้วย"

$ renpy.music.set_volume(0.5, 0.0, channel="sound")
play sound sfx_doorknock2

# "Grimacing slightly at the prospect of her being sick, I rap my knuckles on the door."
"ฉันทำหน้าเบ้เล็กน้อยเมื่อคิดว่าฮานาโกะคงไม่สบายพลางเคาะประตู"

# "…Silence. I listen intently for any sound of shuffling coming from inside, but I can't hear a thing."
"…เงียบ ฉันเงี่ยหูฟังว่าพอจะมีเสียงอะไรขยับหรือเปล่า แต่ก็ไม่ได้ยินอะไร"

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_doorknock2

# "I knock on the door again, slightly harder."
"ฉันเคาะประตูอีกครั้งให้หนักมือขึ้นอีกเล็กน้อย"

# "Still no answer. How strange."
"ไม่มีเสียงตอบรับจากเลขหมายที่ท่านเรียก แปลกแฮะ"

$ renpy.music.set_volume(0.5, 0.0, channel="sound")
play sound sfx_dooropen

show bg school_girlsdormhall at center
with charamove

# "A door opens behind me. A freckled and somewhat scrawny underclassman I don't recognize comes out and is briefly taken off guard by my presence."
"ประตูห้องที่อยู่ข้างหลังเปิดออก รุ่นน้องผู้หญิงที่ดูไม่คุ้นหน้าคนหนึ่งโผล่ออกมา ดูค่อนข้างผอมและตกกระ เธอผงะไป\nเล็กน้อยเมื่อเห็นฉัน"

label th_choiceL10_2:
menu:
    with menueffect
    
    # "Girl" "Uh… hi."
    thname("เด็กสาว") "เอ่อ… ไง"

    # "Ask about Hanako.":
    "ถามเรื่องฮานาโกะ":
        return m1
    
    # "Keep it to myself.":
    "ไม่บอกอะไร":
        return m2

label th_L10d:

# "Actually, this may be a rather fortuitous meeting."
"เอาจริง ๆ แล้ว ได้มาเจอกันอย่างนี้ก็จังหวะเหมาะพอดี"

# hi "Hey. Excuse me, do you know if Hanako's come out of her room today or not? She doesn't seem to be answering."
hi "ไง ขอโทษทีนะ แต่พอจะรู้หรือเปล่าว่าวันนี้ฮานาโกะออกมาจากห้องมั้ย พอดีเคาะแล้วไม่เห็นตอบอะไรเลย"

# "Girl" "Ikezawa is Ikezawa. Her not answering the door is totally normal. That tall foreign girl's the only person she'll ever talk to, after all."
thname("เด็กสาว") "ก็ปกติของอิเคซาวะเขานั่นแหละ เคาะแล้วไม่เคยจะมาเปิดให้หรอก ก็นะ คนที่คุยด้วยก็มีแต่ยัยลูกครึ่งตัวสูง ๆ คนนั้น\nอะนะ"

# "She gives a shrug before walking off down the hallway, having much more important matters to attend to than Hanako or me."
"เธอยักไหล่แล้วเดินไปตามโถงทางเดิน ดูท่าว่าจะมีเรื่องที่สำคัญกว่าฮานาโกะกับฉัน"

# "Her dismissive attitude annoys me."
"หมั่นไส้กับไอ้ท่าทางหยิ่ง ๆ นั่นเหลือเกิน"

# "Hanako must have a reputation as a hermit; a reputation that doesn't seem outright undeserved, at least in the time before we'd met."
"ฮานาโกะคงเป็นที่รู้จักในฐานะคนชอบเก็บตัวละนะ ซึ่งก็ไม่ได้ผิดไปจากความเป็นจริงเสียทีเดียวหรอก อย่างน้อยก็ตอน\nก่อนที่เราจะได้เจอกัน"

label th_L10e:

# hi "Hey. Sorry, don't mind me."
hi "ไง โทษทีนะ ไม่ต้องสนใจฉันหรอก"

# "I think the situation with Hanako should be kept as private as possible, for her sake. I don't really know anything about what's happened to her, and my gut tells me that it's not physical sickness that's befallen her."
"ยังไงก็คงต้องปิดเรื่องสถานการณ์นี้ไว้ให้รู้กันน้อยที่สุดเพื่อตัวฮานาโกะเองละนะ ฉันเองก็ไม่รู้ว่าฮานาโกะเป็นอะไร\nแต่พอจะสัมผัสได้ว่าไม่ได้ป่วยกายหรอก"

# "She doesn't need rumors about her going around. As much as it may pain me to think so, she'd likely prefer to keep her status as a strangely-ignored member of the class over having people talk behind her back."
"ฮานาโกะคงไม่อยากให้มีข่าวลืออะไรหรอก ถึงคิดแล้วจะปวดใจ แต่ฮานาโกะคงมองว่าการรักษาสถานภาพของตัวเอง\nในฐานะเพื่อนร่วมชั้นที่ถูกเมินแบบแปลก ๆ นั้นดีกว่าการมีคนเอาเรื่องของเธอไปนินทา"

# "Girl" "Whatever."
thname("เด็กสาว") "ตามสบาย"

# "With that, she turns and walks down the hallway without a second thought. How rude."
"แล้วเธอก็เดินไปตามโถงทางเดินในทันที หยาบคายชะมัด"

label th_L10f:

show bg school_girlsdormhall at right
with charamove

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_doorknock2

# "Scratching my head, I make one last attempt at getting Hanako to answer as I knock on the door one final time."
"ฉันเกาหัวแกรก ๆ พลางลองเคาะเรียกให้ฮานาโกะตอบเป็นครั้งสุดท้าย"

# hi "Hanako, it's just me. Mutou said to give you some stuff."
hi "ฮานาโกะ ฉันเอง ครูฝากเอกสารมาให้แน่ะ"

# "For a while, the attempt seems just as unsuccessful as the last. Just before I slip the sheets under her door, though, I can hear the handle rattling."
"ความเงียบซึ่งบ่งบอกว่าความพยายามนั้นล้มเหลวไม่ต่างจากครั้งก่อนนั้นตามมาอยู่ชั่วขณะ แต่จังหวะที่ฉันกำลังจะสอด\nแผ่นกระดาษเข้าทางช่องตีนประตูก็ได้ยินเสียงลูกบิดขยับ"

play sound sfx_dooropen
with Pause(1.5)

show hanagown distant:
    xpos 1.0 xanchor 0.75
with charamoveinright

# "As the door opens halfway, I do my best to look Hanako over as quickly as possible. It's a task made somewhat more difficult by her oversized gown hiding so much of her body."
"ประตูเปิดออกกึ่งหนึ่ง ฉันรีบมองสำรวจฮานาโกะด้วยความรวดเร็ว ซึ่งก็มองยากเพราะเสื้อคลุมที่หลวมโพรกนั้นปกปิด\nร่างกายเธอไปเสียเกือบหมด"

# "She doesn't look sick, or at least not immediately so. To be honest, I'd have preferred that to her expression right now."
"ฮานาโกะดูจะสบายดี อย่างน้อยก็ด้วยสภาพร่างกายน่ะนะ แต่ว่าตามตรง ฉันยอมเห็นฮานาโกะตอนไม่สบายดีกว่า\nต้องมาเห็นสีหน้าของฮานาโกะตอนนี้"

# hi "Hi, Hanako. Mutou wanted me to give you these since you weren't in class today."
hi "ไง ฮานาโกะ พอดีวันนี้เธอไม่ได้เข้าเรียน ครูเลยฝากอันนี้มาให้"

# "I hold out the loose sheets, which she tentatively takes in her hands. The way she moves is weird, devoid of thought, as if she's some kind of mechanical automaton rather than a living being."
"ฉันยื่นแผ่นกระดาษให้ ฮานาโกะก็รับไปแบบอึก ๆ อัก ๆ ท่าทางการขยับตัวของเธอนั้นดูแปลก ๆ เพราะเหมือนไม่ได้มี\nความตั้งใจอะไรเลย แค่ขยับไปโดยอัตโนมัติเหมือนหุ่นยนต์ ไม่ใช่สิ่งมีชีวิต"

# hi "Are you… okay? If you're feeling sick or anything, I could get the nurse."
hi "ไหว… หรือเปล่า ถ้าไม่สบายหรืออะไรให้ฉันเรียกพยาบาลมาก็ได้นะ"

# "It feels almost pitiful to put on such a routine “get well soon” act. I can't think of anything else I could possibly do for her, though."
"พอมาทำตัวแบบ “หายไว ๆ นะ” อย่างนี้แล้วก็รู้สึกสมเพชเหมือนกัน แต่ก็ไม่รู้แล้วว่าจะทำยังไงให้ฮานาโกะดีขึ้นได้อีก"

show hanagown normal:
    xanchor 0.7
with dissolvecharamove

# "She seems to collect herself a little at the notion… but only a little."
"ฮานาโกะดูจะรู้สึกตัวขึ้นมาหน่อยหนึ่งกับสิ่งที่ฉันสื่อไป… แต่ก็แค่หน่อยหนึ่ง"

show hanagown distant_blush
with charachange

# ha "I'm fine."
ha "ฉันสบายดี"

# hi "Okay."
hi "โอเค"

stop music fadeout 6.0

with Pause(2.0)

hide hanagown
with charamoveoutright

play sound sfx_doorclose

# "An awkward silence follows, eventually ended by her nodding solemnly in farewell and closing the door. The entire experience feels surreal."
"และความเงียบอันน่าอึดอัดก็ตามมา สุดท้ายฮานาโกะก็พยักหน้าอย่างจริงจังเป็นการบอกลาแล้วปิดประตู รู้สึกเหมือน\nเมื่อกี้ไม่ใช่เรื่องจริงเลย"

# "More than a little put off, I wander back to my room and hope that she'll be better by tomorrow, despite not knowing exactly what's wrong with her."
"ฉันเดินคอตกกลับมาที่ห้องตัวเองพร้อมหวังใจว่าพรุ่งนี้ฮานาโกะจะดีขึ้น แม้จะไม่รู้แน่ชัดว่าเธอเป็นอะไรก็ตาม"

scene black
with dissolve

#**************************************

label th_L11:

show bg school_girlsdormhall at right
with locationchange

# "Once again, I find myself in front of Hanako's door after another of her unexplained absences from class."
"เป็นอีกครั้งที่ฉันมายืนอยู่ตรงหน้าห้องฮานาโกะ เนื่องจากเธอขาดเรียนอีกแล้ว"

play sound sfx_doorknock2

"…"

play sound sfx_doorknock2

"…"

# "Nothing. Considering this is the second day in a row she's been like this, I'm starting to worry about her."
"ไม่ตอบ นี่ก็วันที่สองแล้วที่ฮานาโกะเป็นอย่างนี้ ชักเป็นห่วงแล้วสิ"

# "Summoning my willpower, I decide to try one last way to get her to respond."
"ฉันปลุกใจตัวเองแล้วใช้ไม้ตายให้ฮานาโกะตอบ"

# hi "Hanako, if you don't say anything I'll go get the nurse for you."
hi "ฮานาโกะ ถ้าไม่พูดอะไรเดี๋ยวฉันจะไปเรียกพยาบาลให้มาหาแล้วนะ"

# ha "…Go away."
ha "…ไปให้พ้น"

play music music_hanako fadein 10.0

# "Wh… what? It's hard to tell whether her tone's one of depression, anger, or both. What in the world can I actually do to help her, if she doesn't even want help?"
"อะ… อะไรนะ บอกไม่ถูกเลยว่าน้ำเสียงแบบนั้นคือเครียดหรือโกรธอยู่ ไม่ก็ทั้งสองอย่าง ในเมื่อไม่ยอมรับความช่วยเหลือ\nอย่างนี้แล้วฉันจะทำอะไรได้"

# "The message is clear enough. I can't just leave her like this, though; just sitting in her room for days on end."
"ฉันได้ยินประโยคนั้นเต็มสองหู แต่จะปล่อยให้เอาแต่หมกตัวอยู่กับห้องอย่างนี้ไปทั้งวันก็ไม่ได้"

# "Rubbing my temples in thought, I withdraw to my own room to think about how to proceed. Rationality is what's needed here, as an overreaction may just make matters worse."
"ฉันนวดขมับพลางคิดก่อนจะล่าถอยกลับมาที่ห้องตัวเองเพื่อดูว่าจะเอายังไงต่อ ตอนนี้ต้องทำอะไรให้มันสมเหตุสมผล\nก่อน ขืนบุ่มบ่ามไปอาจจะยิ่งทำให้อะไร ๆ แย่ลงไปอีก"

scene bg school_dormhisao
with shorttimeskip

# "I dig around drawer after drawer of my desk, looking for where I put that damned piece of paper."
"ฉันเปิดลิ้นชักที่โต๊ะตัวแล้วตัวเล่าหาว่าตัวเองเก็บไอ้กระดาษแผ่นนั้นไว้ที่ไหน"

# "Before she left, Lilly told me the number to call her on while in Scotland and I wrote it down. Now that I need it though, the damned thing is—"
"ลิลลี่บอกเบอร์โทร. ไว้ก่อนไปสกอตแลนด์ ซึ่งฉันก็จดไว้ แต่ทีพอต้องการขึ้นมาละดัน—"

# "Ah. Here."
"อ้อ อยู่นี่เอง"

# "I probably should have just entered it directly into my cell phone, come to think of it. Without further ado, I enter the numbers and anxiously press the call button."
"จะว่าไปแล้ว บันทึกใส่โทรศัพท์ไปเลยเสียก็สิ้นเรื่อง ฉันกดไปตามปุ่มตัวเลขในทันทีแล้วกดโทร. ด้วยความร้อนใจ"

scene bg school_dormhisao_blurred
show phone mobile:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with locationchange
with Pause (0.5)

# "The fact the phone rings at all shows that I got the prefix for a call to Scotland right at least. I've never made an international call before, so that's some comfort."
"มีเสียงต่อสายอย่างนี้ก็แปลว่ากดรหัสประเทศสกอตแลนด์ถูกแล้วละ โล่งไปที ฉันเองก็ไม่เคยโทรข้ามประเทศมาก่อน\nเสียด้วย"

# "Eventually the phone picks up, a feminine voice I don't recognize on the other end. It's probably Lilly's mother."
"ในที่สุดก็มีคนรับสาย ปลายสายเป็นเสียงผู้หญิงคนหนึ่งที่ฉันไม่คุ้นหู อาจจะแม่ลิลลี่มั้ง"

$ renpy.music.set_volume(0.5, 0.2, channel="music")

#mystery "<Good morning. This is Karla Satou. May I help you?>"
# mystery "{image=vfx/garbage.png} {image=vfx/garbage.png} Satou {image=vfx/garbage.png}?"
mystery "{image=vfx/garbage.png} {image=vfx/garbage.png} Satou {image=vfx/garbage.png}?"

# "English? Suddenly finding myself unprepared, I realize I can't understand a word she says, either due to my limited vocabulary or her heavy accent. I should have anticipated this, since according to Lilly, her mother is a native Scot."
"ภาษาอังกฤษเหรอ ไปต่อไม่ถูกเลย ฟังไม่ออกเลยสักคำแฮะ คงเพราะฉันรู้คำศัพท์น้อยไม่ก็เพราะสำเนียง จริง ๆ น่าจะ\nคิดได้แต่แรกเพราะรู้มาจากลิลลี่แล้วว่าแม่เธอนั้นเป็นคนสก็อตแลนด์โดยกำเนิด"

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
thname("คุณนายซาโต้") "มีเพื่อนมารยาทงามอย่างนี้ด้วย! ลิลลี่ มีคนโทรหาลูกแน่ะ!"

# "Her mother seems nice, if a little overenthusiastic given the mundane situation."
"ก็ดูเป็นคนดีนะ ถึงออกจะตื่นเต้นไปหน่อยกับเรื่องธรรมดา ๆ อย่างนี้ก็เถอะ"

# "There's a small silence as Lilly takes her time getting to the phone. In the distance, I can just make out her mother scolding her playfully for just getting up."
"ก่อนที่ลิลลี่จะมารับโทรศัพท์นั้นปลายสายเงียบไปครู่หนึ่ง ฉันได้ยินเสียงแม่ลิลลี่ที่กึ่งดุกึ่งกระเซ้าเจ้าตัวที่เพิ่งตื่นอยู่แว่ว ๆ"

$ renpy.music.set_volume(1.0, 5.0, channel="music")

# li "Hello, Lilly speaking."
li "สวัสดีค่ะ ลิลลี่นะคะ"

# hi "You sound awful."
hi "เสียงฟังดูไม่ไหวเลยนะ"

# "She makes a sound somewhere between a dying animal and a yawn."
"ลิลลี่ทำเสียงหาวโอดโอยคล้ายสัตว์ใกล้ตาย"

# "The one thing I did remember to check before calling was the time zone. It'd be pretty late in the morning over there, so she really has no excuse."
"ก่อนโทรฉันดูเรื่องเขตเวลาแล้วเรียบร้อย ตอนนี้ที่สกอตแลนด์ก็เข้าช่วงสายพอสมควรแล้ว เพราะงั้นจะอ้างอะไร\nก็คงไม่ได้อีก"

# hi "Not feeling well?"
hi "ไม่สบายเหรอ"

# li "Just tired. What time is it there?"
li "แค่เพลียนิดหน่อยจ้ะ ที่ญี่ปุ่นกี่โมงแล้วเหรอ"

# hi "Late afternoon. School finished for the day not long ago."
hi "บ่ายแก่ ๆ เพิ่งเลิกเรียนมาเมื่อกี้เอง"

# hi "You're really not a morning person, are you?"
hi "เธอคงไม่ชอบตื่นเช้าสินะเนี่ย"

# li "I don't need you making fun of it as well…"
li "นี่เธอก็จะล้อฉันเรื่องนี้ด้วยเหรอ…"

# "It takes me a measure of restraint not to laugh at her pained groan. Poor girl."
"ฉันต้องห้ามใจตัวเองไม่ให้ขำไปกับเสียงโอดโอยของลิลลี่ ช่างน่าสงสาร"

# hi "How're you doing over there then, bar the mornings?"
hi "แล้วอยู่นู่นเป็นไงบ้าง ถ้าไม่นับเรื่องตื่นเช้าน่ะ"

# li "It's been enjoyable. After not meeting them for so long, just having a meal together with my parents is nice."
li "ก็สนุกดีจ้ะ ไม่ได้อยู่กับพ่อแม่เสียนาน แค่ได้กินข้าวด้วยกันกับพวกท่านก็ดีใจแล้วละจ้ะ"

# li "Though the pool and the sheer size of the house might have something to do with that as well."
li "ถึงส่วนหนึ่งน่าจะเพราะสระน้ำกับขนาดของบ้านด้วยก็เถอะจ้ะ"

# "Even if they're not in Japan, from the way it sounds her family must be pretty wealthy to live so luxuriously."
"ถึงจะไม่ได้อยู่ที่ญี่ปุ่น แต่ฟังดูแล้วที่บ้านของลิลลี่คงจะรวยพอสมควร ถึงได้กินหรูอยู่สบายอย่างนั้น"

# li "Are things all right with you and Hanako?"
li "แล้วเธอกับฮานาโกะเป็นยังไงบ้าง โอเคดีหรือเปล่า"

stop music fadeout 0.3

# "Damn, I was hoping that wouldn't be brought up quite so quickly."
"ให้ตาย ไม่คิดเลยแฮะว่าจะพูดถึงเรื่องนี้เร็วขนาดนี้"

# "I take a moment to try and sort out exactly how to describe the situation without causing her undue worry, but she picks up on that without a word being said."
"ฉันคิดเรียบเรียงคำพูดอยู่ครู่หนึ่งว่าจะอธิบายสถานการณ์ตอนนี้อย่างไรไม่ให้ลิลลี่เป็นกังวลมากจนเกินเหตุ แต่ลิลลี่\nก็ยังสัมผัสได้โดยที่ไม่ต้องมีคำพูดใด ๆ เลย"

play music music_moonlight fadein 2.0

# li "Hanako's not well, is she?"
li "ฝั่งฮานาโกะคงไม่โอเคใช่มั้ย"

# hi "How did you know?"
hi "รู้ได้ยังไง"

# li "Because today is her birthday. I'd hoped she might have gotten at least a little better after coming to know you, but…"
li "ก็วันนี้วันเกิดฮานาโกะนี่นา ทีแรกฉันก็หวังอยู่นะว่าพอฮานาโกะได้สนิทกับเธอแล้วจะดีขึ้น แต่ว่า…"

# li "How is she right now?"
li "ตอนนี้ฮานาโกะเป็นยังไงบ้าง"

# hi "She missed school yesterday and seemed out of sorts when I checked up on her. Today she missed school again, and just told me to go away."
hi "เมื่อวานไม่ได้เข้าเรียนน่ะ แล้วตอนไปแวะดูก็เหมือนไม่ค่อยสบายด้วย วันนี้ก็ขาดเรียนอีก แถมไล่ฉันให้ไปให้พ้นด้วย"

# hi "I've really got no idea what to make of it. Has this happened in the past? Is it related to her scarring in some way?"
hi "ฉันจนปัญญาไม่รู้จริง ๆ ว่าจะทำยังไงดี เมื่อก่อนเคยมีแบบนี้มั้ย เกี่ยวอะไรกับแผลเป็นหรือเปล่า"

# li "Unfortunately so. Roughly the same thing happened last year when her birthday came up."
li "เกรงว่าจะเป็นอย่างนั้นจ้ะ วันเกิดฮานาโกะเมื่อปีที่แล้วก็มีเรื่องประมาณนี้เหมือนกัน"

# li "As far as I can tell, it's because her parents died in the accident that caused her scarring, and Hanako blames herself for their deaths."
li "เท่าที่พอจะนึกออก คงเป็นเพราะพ่อแม่ฮานาโกะท่านเสียชีวิตไปพร้อม ๆ กับตอนที่เกิดอุบัติเหตุที่ทำให้เกิดแผลเป็น\nฮานาโกะเลยโทษตัวเองว่าตัวเองเป็นต้นเหตุที่ทำให้ทั้งสองคนจากไป"

# "What she says does seem to make sense. If she's blaming herself on her birthday, she may well be ruing that she was ever born."
"ที่พูดมาก็มีเหตุผล ถ้าถึงวันเกิดแล้วฮานาโกะโทษตัวเอง ก็คงหมายความได้ว่าเธอกำลังนึกเสียใจที่ตัวเองเกิดมา"

# "The fact that Lilly seems so in the dark about it though, almost to the extent that I am, is a surprise."
"แต่ที่ฉันแปลกใจก็คือ ลิลลี่ดูจะไม่ค่อยรู้เรื่องรู้ราวอะไรพอ ๆ กันกับฉันด้วยเช่นกัน"

# hi "So that's why she lives in the student dormitories, as well. Has she told you any more about the accident?"
hi "ก็คงเป็นเหตุผลที่ฮานาโกะมาอยู่หอในด้วยละนะ ฮานาโกะเคยเล่าเรื่องอุบัติเหตุที่ว่าอะไรให้ฟังอีกหรือเปล่า"

# li "As close as we've come… she's very barely told me anything about what happened. What I know about it is largely conjecture."
li "เราสองคนสนิทกันขนาดนี้ก็จริง… แต่ฮานาโกะแทบไม่เคยเล่าให้ฟังเลยว่าเกิดอะไรขึ้นบ้าง ที่ฉันรู้ส่วนใหญ่ก็เป็นแค่\nการคาดการณ์เท่านั้นแหละจ้ะ"

# "She sounds depressed, almost defeated. Considering the trauma Hanako must have gone through, I really can't fault Lilly for not knowing. Nevertheless, she still seems to consider it a personal failing."
"น้ำเสียงลิลลี่ฟังดูเศร้าหมองค่อนไปทางเหนื่อยอ่อน แต่ถ้าคิดดูว่าฮานาโกะต้องผ่านเหตุการณ์สะเทือนขวัญอะไรมาบ้าง\nลิลลี่จะไม่รู้ก็ไม่แปลก แต่เหมือนลิลลี่จะยังมองว่าเป็นฝั่งตัวเองที่ยังพยายามไม่พออยู่ดี"

# hi "Don't blame yourself, Lilly. With everything she's gone through…"
hi "อย่าโทษตัวเองเลยลิลลี่ ฮานาโกะก็ผ่านอะไรมาขนาดนั้น…"

# li "I know. Thank you, Hisao. I'm sorry I can't be of more help to you."
li "รู้จ้ะ ขอบคุณนะฮิซาโอะ ขอโทษด้วยนะที่ช่วยอะไรได้ไม่มาก"

# hi "It's fine, I'll just give it some more thought. Thanks, and have a good time in Scotland."
hi "ไม่เป็นไรหรอก เดี๋ยวฉันค่อยไปคิดต่ออีกสักหน่อย ขอบใจนะ แล้วก็เที่ยวสกอตแลนด์ให้สนุกละ"

# li "Um, I…"
li "เอ่อ ฉัน…"

# hi "Hmm?"
hi "หืม?"

# li "It's nothing. Thank you for taking care of Hanako."
li "เปล่าจ้ะ ขอบคุณที่คอยดูแลฮานาโกะนะ"

# hi "…Okay. Bye."
hi "…โอเค บาย"

# li "Goodbye."
li "ลาก่อนจ้ะ"

stop music fadeout 4.0

# "And with that, the line goes silent."
"แล้วปลายสายก็เงียบไป"

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

# "Amid the seemingly only increased number of questions I can't answer, the most immediate is what Lilly was going to say."
"ในบรรดาคำถามมากมายซึ่งฉันนึกหาคำตอบไม่ออกที่ผุดขึ้นมาไม่หยุดหย่อน คำถามที่ต้องการคำตอบอย่างเร่งด่วน\nที่สุดคือ เมื่อกี้ลิลลี่จะพูดอะไร"

# "Oh. Oh no."
"ฉิบ ฉิบหาย"

# "I'm an idiot. She must have thought I was calling to talk with her, but I only asked for help with Hanako."
"โง่บัดซบ ลิลลี่คงคิดว่าที่โทรไปเพราะอยากคุยด้วย แต่ฉันดันไปขอความช่วยเหลือเรื่องฮานาโกะอย่างเดียวเสียนี่"

# "Even more shameful than that thought is the fact that such an appraisal would be largely correct."
"ที่น่าขายหน้ากว่านั้นก็คือ สิ่งที่ฉันคาดเดาไปมีโอกาสเป็นไปตามนั้นสูงมาก"

# "Well… first things first. For now, I need to at least sort out Hanako and make sure that she's actually eating okay."
"เอาเถอะ… ก่อนอื่น ตอนนี้อย่างน้อยต้องทำให้ฮานาโกะกลับเป็นสภาพเดิมก่อน แล้วคอยดูว่ากินอาหารเพียงพอดี\nหรือเปล่าด้วย"

show bg school_girlsdormhall
with shorttimeskip

# "The occasional passing students give badly hidden glances at the plate of food I carry to the female dormitories."
"นักเรียนที่เดินสวนไปมาจ้องมองแบบแทบไม่เก็บอาการกับถาดอาหารที่ฉันเดินถือมาที่หอหญิง"

# "It's hardly a meal to be proud of, only being an instant microwave meal from the convenience store, but it should at least fill her up."
"ก็ไม่ใช่อาหารอะไรที่จะภูมิใจได้นักหรอก เป็นแค่อาหารสำเร็จรูปอุ่นไมโครเวฟจากร้านสะดวกซื้อนี่นะ แต่อย่างน้อย\nก็คงพอทำให้ฮานาโกะอิ่มท้องได้บ้าง"

show bg school_girlsdormhall at right
with charamove

# "Eventually I arrive outside of her room, after having to ward off a couple of girls who jokingly tried to pilfer the food I'd taken so long to procure."
"จนในที่สุดก็เดินมาถึงตรงหน้าห้องฮานาโกะ ซึ่งก่อนหน้านี้ฉันต้องไล่ ๆ สาวสองคนที่ทำทีจะจิ๊กอาหารที่ฉันอุตส่าห์\nเสียเวลามาทำ"

# "I decide to forgo knocking, since it was proven to be an utterly useless measure and it's somewhat difficult to do with my hands full."
"ฉันเลือกที่จะไม่เคาะประตู เพราะดูจากก่อนหน้านี้ก็เห็นชัดแล้วว่าเคาะไปก็เท่านั้น แถมตอนนี้มือทั้งสองข้างก็ไม่ว่าง"

# hi "Hanako, it's Hisao."
hi "ฮานาโกะ ฉันฮิซาโอะนะ"

# hi "I know you're listening. I got some food for you."
hi "รู้นะว่าเธอฟังอยู่ ฉันเอาข้าวมาให้กินแน่ะ"

# "Silence. As I expected."
"เงียบ ตามคาด"

# hi "I'll leave it beside your door. Please eat it at least, okay?"
hi "เดี๋ยววางไว้ให้ข้างประตูนะ กินหน่อยเถอะนะ โอเคมั้ย"

# "There. I've said my piece. Now it's up to her."
"เอาละ บทของฉันหมดแล้ว ทีนี้ก็อยู่ที่ฮานาโกะ"

show bg school_girlsdormhall at center
with charamove

# "Putting the plate down, I walk back to my own room to eat my dinner."
"ฉันวางถาดไว้แล้วเดินกลับมากินข้าวเย็นที่ห้องตัวเอง"

with shorttimeskip

# "By the time I return to Hanako's dormitory, a good hour's passed."
"เมื่อผ่านไปราวหนึ่งชั่วโมงฉันก็กลับมาที่ห้องฮานาโกะอีกครั้ง"

# "Thankfully, there isn't anything to be seen beside her door. I walk back at least somewhat happier that she's eating."
"ซึ่งดีที่ตรงข้างประตูนั้นไม่มีอะไรอยู่แล้ว ฉันเดินกลับหอด้วยความเบาใจว่าอย่างน้อยฮานาโกะก็ได้กินข้าวแล้ว"

# "If she intends to get through this by herself, then being able to help, even if it's just in such a small way, is at least something."
"ถ้าเธออยากก้าวข้ามสิ่งนี้ไปด้วยตัวของเธอเอง การที่ได้คอยช่วย—แม้จะเป็นอะไรเล็ก ๆ น้อย ๆ เช่นนี้—ก็นับว่า\nมีความหมายแล้ว"

scene black
with dissolve

#**************************************

label th_L12:

scene bg school_library_ss
with locationchange

play music music_pearly

# "I sit reading in the library after school, turning page after page, barely registering the words written on each out of sheer boredom."
"พอเลิกเรียนแล้วฉันก็มานั่งอ่านพลิกหน้าหนังสือไปเรื่อย ๆ และความเบื่อก็ทำให้แต่ละคำที่อยู่บนหน้าหนังสือนั้นแทบ\nไม่ผ่านเข้าสมองเลย"

# "With my cheek resting in my hand, I can't help noticing the slightly rough feeling against my palm. It won't be long before I'll need to get a razor."
"พอเอามือเท้าคางก็รู้สึกถึงสัมผัสสาก ๆ บนฝ่ามือ อีกเดี๋ยวคงต้องโกนหนวดแล้ว"

# "Giving up on reading, I simply let my head drop onto the book in front of me."
"ฉันเลิกอ่านแล้วเอาหัวหนุนกับหนังสือที่วางอยู่ตรงหน้า"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide

nvl clear
nvl show dissolve

# n "\n\n\nThings have quieted down considerably since Hanako began attending school again."
n "\n\n\nหลังจากที่ฮานาโกะเริ่มกลับมาเข้าเรียนแล้วอะไร ๆ ก็ดูเงียบไปพอสมควร"

# n "When she first returned to class, nothing was said nor done that wasn't part of the usual routine, and it's been the same way since. Neither of us desired to bring up her accident, so there simply wasn't any point in pursuing it."
n "ตอนที่ฮานาโกะกลับมาเข้าเรียนวันแรก ไม่มีใครพูดหรือทำอะไรที่นอกเหนือไปจากกิจวัตรตามปกติ และก็เป็นอย่างนั้น\nเรื่อยมา ไม่มีใครอยากจะพูดถึงเรื่องอุบัติเหตุครั้งนั้นของฮานาโกะ ดังนั้นก็ไม่มีเหตุผลอะไรที่จะต้องไปซักไซ้เรื่องนั้น"

# n "Thus a few days went by, the daily grind continuing just as it had before."
n "แล้วเวลาก็ผ่านไปอีกสองสามวัน กิจวัตรน่าเบื่อดำเนินไปอย่างเช่นเคย"

# n "It's only natural that my mind would wander to other places, and more importantly, other people. The Lilly-shaped hole in the daily life of Hanako and me has been pretty noticeable for a while now."
n "ไม่แปลกอะไรที่จิตใจฉันจะล่องลอยไปหาที่อื่น โดยเฉพาะคนอื่น รูโหว่ที่เป็นรูปลิลลี่ซึ่งปรากฏในชีวิตประจำวันของ\nฮานาโกะกับฉันนั้นกวนใจพวกเรามาได้สักพักแล้ว"

# n "I'd be pleased to say that this has allowed me time to refine just what my thoughts on her exactly are, but alas, I've had no such luck."
n "ฉันเองก็อยากบอกตัวเองเหมือนกันหรอกว่านี่แหละคือโอกาสที่จะได้คิดทบทวนว่าฉันคิดยังไงกับลิลลี่กันแน่ แต่ก็นะ\nสมองดันไม่ได้รับรู้แบบนั้นด้วย"

# n "It doesn't help that many attempts to do so have led to the troublesome topic of Iwanako. Every time my thoughts drift into that direction, I reflexively try to think about something else."
n "แล้วยิ่งคิดทบทวนไปก็จะทำให้ไพล่นึกไปถึงเรื่องอิวานาโกะอันน่าหนักใจอีก ทุกครั้งที่คิดถึงเรื่องนั้นสมองจะฝืนไปคิด\nเรื่องอื่นแทนโดยอัตโนมัติ"

$ renpy.music.set_volume(1.0, 2.0, channel="music")

nvl clear

nvl hide dissolve

window show

# hi "Why did this have to happen now…"
hi "ทำไมต้องเป็นตอนนี้ด้วยนะ…"

# yu "Um…"
yu "เอ่อ…"

show yuuko worried_up_ss
with charaenter

# "I turn and look up to the source of the tentative voice coming from behind me."
"ฉันเงยหน้าขึ้นไปมองว่าเจ้าของเสียงที่ฟังดูอ้ำ ๆ อึ้ง ๆ นั้นเป็นใคร"

# hi "Ah, sorry. I didn't mean to disturb anyone."
hi "อ๊ะ ขอโทษครับ ไม่ได้กะจะกวนใครเลย"

show yuuko worried_down_ss
with charachange

# yu "That's… not it."
yu "ไม่ใช่… อย่างนั้น"

# hi "Ah…"
hi "เอ่อ…"

# "I glance around the orange-tinted room, quickly realizing how silly my apology must have sounded. In the time I've spent thinking and lazing about in here, everyone's well and truly left."
"พอมองไปรอบ ๆ ห้องที่เจือด้วยแสงสีส้มก็รู้ทันทีว่าคำขอโทษเมื่อครู่นั่นฟังดูชวนขันเพียงใด ระหว่างที่ฉันนั่งคิด\nนั่งเหม่ออยู่ในนี้นั้นทุกคนต่างทยอยออกไปกันหมดแล้ว"

# hi "Library closing?"
hi "ห้องสมุดจะปิดแล้วเหรอครับ"

show yuuko neurotic_down_ss
with charachange

# yu "If you don't want to go, I could keep it open a bit longer. It's no trouble at all."
yu "ถ้าอยากอยู่ต่อฉันจะเปิดไว้ให้อีกหน่อยก็ได้นะ สบายมาก"

# hi "Don't worry, I should get going anyway. Thanks."
hi "ไม่เป็นไรครับ เดี๋ยวผมต้องไปแล้ว ขอบคุณครับ"

show yuuko worried_down_ss
with charachange

# "As I get up and begin to move off, I feel Yuuko's eyes drilling into my back."
"ระหว่างที่กำลังลุกขึ้นเตรียมเดินออกก็รู้สึกได้ถึงสายตาของยูโกะที่จับจ้อง"

# hi "Is there something wrong?"
hi "มีอะไรหรือเปล่าครับ"

show yuuko worried_up_ss
with charachange

# yu "You look depressed. Are you okay?"
yu "เธอดูเครียด ๆ นะ ไหวหรือเปล่า"

# "Yuuko nervously twists her fingers as she says this, unsure whether she's overstepping her boundaries or not. I really can't tell if she's more worried about my mood or about bothering me."
"นิ้วยูโกะยุกยิกไปมาด้วยความไม่แน่ใจว่าตัวเองล้ำเส้นความเป็นส่วนตัวเกินไปหรือเปล่า ไม่รู้เหมือนกันว่าตอนนี้ยูโกะ\nคิดมากว่าฉันดูเครียดหรือคิดมากที่มารบกวนฉันกันแน่"

# "Normally I'd just shrug it off and assure her that I'm fine, but my reflective mood gets the better of me. Despite being staff, she really doesn't feel as much like an authority figure as the others."
"ปกติฉันคงทำเฉยแล้วบอกไปว่าไม่มีอะไร แต่คราวนี้อารมณ์แท้จริงที่สะท้อนออกมามีอิทธิพลมากกว่า ถึงยูโกะจะเป็น\nพนักงานของโรงเรียนคนหนึ่ง แต่เธอก็ไม่ได้ดูมีอำนาจเท่าคนอื่น ๆ ขนาดนั้น"

# hi "It's just… I guess the best term for it would be relationship problems."
hi "แค่ว่า… ถ้าให้เลือกคำที่เหมาะที่สุดก็คงจะเป็นปัญหาความสัมพันธ์ละมั้งครับ"

show yuuko worried_down_ss
with charachange

# yu "Oh. I'm… not too good with that kind of thing. My only relationship ended a bit abruptly."
yu "อ้อ ฉัน… ไม่ค่อยสันทัดเรื่องแบบนั้นเท่าไหร่ ความสัมพันธ์ที่เคยมีอยู่ครั้งเดียวก็จบไปแบบกะทันหันหน่อย ๆ ด้วย"

show yuuko smile_down_ss
with charachange

# yu "But if you want to talk about it, I mean, I could listen. I think."
yu "แต่ถ้าอยากเล่า คือ ก็รับฟังได้ คิดว่า"
#Awkward sentence intentionally left in. -SC

# "Now I feel kind of bad for bringing it up. She's not that old, though, so at least she has a good chance of finding another partner."
"ชักรู้สึกไม่ดีแล้วแฮะที่พูดถึงเรื่องนี้ แต่ยูโกะเองก็ไม่ได้แก่ขนาดนั้น อย่างน้อยก็ยังมีโอกาสหาแฟนอีกคนได้อยู่"

# hi "It isn't like we're in a bad situation right now. We have spent many days together as friends, sometimes going out to do stuff… that kind of thing."
hi "ไม่ใช่ว่าความสัมพันธ์มันแย่อะไรอย่างนั้นหรอกครับ พวกเราก็อยู่เป็นเพื่อนด้วยกันมาหลายวัน บางทีก็ไปเที่ยว\nไปทำอะไร… ประมาณนั้น"

# hi "But I'm starting to want to do more for her, learn more about her, and be with her more. I'm not sure whether it's actually love or not, though, and our friendship as it stands is enjoyable."
hi "แต่ผมเริ่มรู้สึกอยากทำอะไรให้มากขึ้น เรียนรู้เรื่องของเธอให้มากขึ้น อยู่กับเธอให้มากขึ้น แต่ผมก็ไม่แน่ใจว่าใช่รัก\nจริงหรือเปล่า แถมความสัมพันธ์ของพวกเราในฐานะเพื่อนมันก็โอเคดีอยู่แล้ว"

show yuuko panic_up_ss
with charachange

# yu "You shouldn't let that stop you!"
yu "อย่าเอาความคิดนั้นมาปิดกั้นตัวเองสิ!"

show yuuko worried_down_ss
with charachange

# yu "Ah… sorry."
yu "เอ่อ… ขอโทษที"

show yuuko worried_up_ss
with charachange

# yu "How to say this… um…"
yu "จะว่ายังไงดี… อืม…"

show yuuko neutral_down_ss
with charachange

# yu "I think that it's nice that you have a good friendship, but school is going to eventually end. Do you think you'll be fine with not knowing if it could have gone further after you've graduated?"
yu "มีเพื่อนดีน่ะก็ดีนะ แต่เดี๋ยวสักวันก็ต้องเรียนจบกันอยู่ดี เธอโอเคเหรอที่พอเรียนจบแล้วจะปล่อยให้ความสัมพันธ์\nมันหยุดอยู่ตรงนั้นโดยที่ไม่รู้เลยว่ามันจะไปได้อีกไกลแค่ไหนน่ะ"

# hi "I guess that's the crux of the problem. I really have no idea what the answer to that question is."
hi "ก็นั่นแหละครับที่น่าจะเป็นประเด็นเลย คือผมไม่รู้จริง ๆ ว่าผมโอเคหรือเปล่า"

show yuuko worried_down_ss
with charachange

# yu "Well, I can't really help there. What your true feelings are is something you have to decide for yourself. But I think that if you do love her, you should definitely say something."
yu "เรื่องนั้นฉันก็ช่วยไม่ได้แล้วละ ความรู้สึกที่แท้จริงของคนเราก็มีแต่เจ้าตัวเท่านั้นแหละที่จะตัดสินได้ แต่ฉันว่าถ้าเธอ\nรักคนนั้นจริง ๆ ก็ต้องบอกอะไรไปสักหน่อยนะ"

show yuuko smile_down_ss
with charachange

# yu "After thinking about it really hard, I decided that even though my relationship didn't work out, it's still better that way than never knowing if it might have or not."
yu "พอฉันลองคิดไปคิดมาดูแล้ว ถึงความสัมพันธ์ของฉันจะไปไม่รอด แต่อย่างน้อยให้เป็นอย่างนั้นยังก็ดีกว่าการอยู่เฉย ๆ\nแล้วไม่รู้ว่าจะรอดหรือไม่รอดกันแน่"

# "I never expected Yuuko to sound so wise. It only makes sense that, with more life experience than I, she'd have a better idea about this."
"คาดไม่ถึงเลยแฮะว่ายูโกะจะพูดอะไรที่ชวนคิดได้ขนาดนี้ ซึ่งก็คงไม่แปลก ในเมื่อเธอมีประสบการณ์ชีวิตมากกว่าฉัน ยังไง\nเธอก็ย่อมรู้ดีกว่าฉันอยู่แล้ว"

# "While I suppose not very much was actually answered, talking to her has helped get it off my chest, and I have no doubt that I should confess if I really do like Lilly."
"ถึงจะยังไม่ได้คำตอบแบบชัดแจ้งมากนัก แต่พอได้คุยกับยูโกะแล้วก็โล่งขึ้น และแน่ใจขึ้นมาแล้วว่าถ้าชอบจริง ๆ ยังไงฉัน\nก็ต้องสารภาพรักกับลิลลี่"

# "I give a slightly frustrated sigh."
"ฉันถอนหายใจด้วยความอึดอัดเล็กน้อย"

# hi "If only reading so much actually helped when it comes to situations like this."
hi "ถ้าการอ่านหนังสือเยอะช่วยเรื่องอะไรแบบนี้ได้ก็ดีสิ"

show yuuko closedhappy_up_ss
with charachange

# "She gives a girlish giggle, which only reinforces my view of her as being different from the usual staff here."
"ยูโกะหัวเราะคิกคักอย่างผู้หญิง ซึ่งยิ่งทำให้ภาพลักษณ์ของเธอที่ต่างไปจากพนักงานคนอื่น ๆ ในโรงเรียนนี้นั้นชัด\nขึ้นไปอีก"

stop music fadeout 9.0

nvl clear

window hide
nvl show dissolve

# n "\n\n\n\n\n\nIn the end, it all comes down to what will happen after school finishes once again."
n "\n\n\n\n\n\nสุดท้ายแล้ว ทุกอย่างก็ต้องรอดูหลังปิดเทอม"

# n "Considering what happened before I came to Yamaku, it feels like being asked to keep up with a field of runners despite having started from a dozen yards behind them."
n "ถ้าลองมองเรื่องที่ฉันเจอก่อนย้ายเข้ามาเรียนที่ยามากุแล้ว ตอนนี้ฉันก็เหมือนคนที่ต้องวิ่งให้ทันคนอื่น ๆ ที่วิ่งอยู่บนลู่\nโดยที่คนอื่นนั้นทิ้งห่างจากฉันไปแล้วสักสิบเมตรได้"

# n "It's just one more motive to move on from the past. The last thing I need right now is to get too caught up in that and getting homesick while I'm at it."
n "ขอแค่มีแรงอีกหน่อยฉันก็จะก้าวขาออกจากอดีตได้แล้ว ตอนนี้ต้องหลีกจากอดีตให้มากที่สุด และห้ามหวนคิดถึงบ้านเก่า\nเป็นอันขาด"

nvl clear
nvl hide dissolve

scene bg school_dormhisao_ss
with locationskip
window show

# "Once again, I find myself calling Lilly. My phone bill is going to be horrific, considering this is international."
"เป็นอีกครั้งที่ฉันโทร. หาลิลลี่ โดนค่าโทรศัพท์อ่วมแหง ๆ โทร. ข้ามประเทศขนาดนี้"

# "But it's worth it. I don't only want to smooth over her feelings from the last time I called, I genuinely want to talk to her again."
"แต่ก็คุ้ม ที่โทร. ครั้งนี้นั้นไม่ใช่แค่เพราะไม่อยากเมินความรู้สึกของลิลลี่จากการโทร. ครั้งก่อน แต่ยังโทร. ไปด้วย\nความอยากคุยจริง ๆ"

scene bg school_dormhisao_blurred_ss
show phone mobile:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with locationchange
with Pause (0.5)

# "When the phone finally picks up, I easily recognize the voice on the other end."
"พอมีคนรับสายก็มีเสียงอันคุ้นหูดังลอดออกมา"

#"Mrs Satou" "<Hello, this is Karla Satou speaking.>"
# "Mrs. Satou" "{image=vfx/garbage.png} {image=vfx/garbage.png} Satou {image=vfx/garbage.png}?"
thname("คุณนายซาโต้") "{image=vfx/garbage.png} {image=vfx/garbage.png} Satou {image=vfx/garbage.png}?"

# hi "<Hello, Mrs. Satou. May I… uh… speak…>"
hi "<Hello, Mrs. Satou. May I… เอ่อ… speak…>"

# "Damn. I've forgotten how the rest is supposed to go. It's not encouraging to forget such a small amount of words, even if I didn't spend that long trying to memorize them."
"โถ่เว้ย ลืมแล้วว่าที่เหลือต้องพูดยังไงต่อ ถึงจะไม่ได้นั่งท่องเอาเป็นเอาตายขนาดนั้นก็เถอะ แต่พอลืมคำไม่กี่คำแล้ว\nก็ชวนให้หมดกำลังใจเหมือนกัน"

# hi "May I speak with Lilly, please?"
hi "ขอสายลิลลี่ได้มั้ยครับ"

# "Mrs. Satou" "Hello again, Hisao. Are you teaching yourself English?"
thname("คุณนายซาโต้") "สวัสดีอีกครั้งจ้ะฮิซาโอะ ฝึกพูดภาษาอังกฤษอยู่เหรอ"

# hi "Just a little. I don't think I'm too good at languages in general."
hi "นิดหน่อยครับ แต่ผมก็ไม่ค่อยถนัดเรื่องภาษาเท่าไหร่"

# "Mrs. Satou" "Oh, don't say that. Your pronunciation was good! I'll get Lilly for you, just wait a moment."
thname("คุณนายซาโต้") "โธ่ อย่าพูดอย่างนั้นสิจ๊ะ เธอออกเสียงได้ชัดมาก! เดี๋ยวตามลิลลี่ให้นะ รอสักครู่จ้ะ"

# "I obediently wait as she goes off in search of Lilly, the other end going silent."
"ฉันถือสายรออย่างว่าง่ายระหว่างที่เธอกำลังตามลิลลี่ให้และปลายสายเงียบไป"

# "Eventually a much more awake-sounding Lilly than last time answers, the time over there being past noon by now."
"จนสุดท้ายก็มีเสียงลิลลี่ที่ฟังดูง่วงน้อยกว่าครั้งที่แล้วมากดังออกมา ตอนนี้ที่นู่นก็ประมาณบ่าย ๆ แล้ว"

play music music_comfort fadein 12.0

# li "Hisao, are you there?"
li "ฮิซาโอะ ได้ยินมั้ยจ๊ะ"

# hi "Yeah, I'm here. Hi."
hi "อื้ม ได้ยิน ไง"

# li "Good afternoon. Sorry for taking so long, I was outside in the garden."
li "ทิวาสวัสดิ์จ้ะ ขอโทษที่ให้รอนานนะ พอดีเมื่อกี้อยู่ในสวนน่ะ"

# hi "Gardening?"
hi "ทำสวนเหรอ"

# li "Unfortunately I've found I'm no good at it, so I just smell the flowers. I think my fingers appreciate it more."
li "น่าเสียดาย แต่ไม่ใช่จ้ะ พอดีฉันไม่ถนัดเรื่องทำสวนเลย ที่อยู่ในสวนก็ไปดมดอกไม้เฉย ๆ นี่แหละ การทำอย่างนี้คงดี\nกับนิ้วฉันมากกว่าด้วย"

# li "I take it Hanako's recovered a bit?"
li "ฮานาโกะดีขึ้นบ้างแล้วใช่มั้ย"

# hi "Yeah. I just made sure she was eating, and eventually she righted herself. Thanks for the help the other day."
hi "อื้ม พอไปจัดแจงอะไรให้กินแล้วก็เริ่มกลับมาเป็นปกติแล้วละ ขอบคุณที่เธอช่วยวันนั้นด้วยนะ"

# li "I don't think I was really that much help. The main thing is that she's better, though."
li "ฉันคงไม่ได้มีส่วนช่วยอะไรขนาดนั้นหรอกจ้ะ แต่อย่างน้อยฮานาโกะก็ดีขึ้นแล้วละนะ"

# hi "True. How's life over there, then? It sounds like you've been living in nothing short of a mansion."
hi "นั่นสินะ แล้วอยู่ที่นู่นเป็นไงบ้าง ฟังดูแล้วบ้านเธอนี่เรียกคฤหาสน์ก็ยังได้เลยมั้งเนี่ย"

# li "I wouldn't call it a mansion…"
li "ก็ไม่เชิงว่าคฤหาสน์หรอกจ้ะ…"

# "“But it is rather large” is obviously what she wants to say, though modesty stops her. I'm a little envious, but it is her holiday."
"ชัดว่าลิลลี่กำลังจะพูดต่อว่า “แต่ก็หลังใหญ่ทีเดียว” ทว่าความถ่อมตัวก็มาปรามเธอไว้ก่อน แอบอิจฉาแฮะ แต่ก็\nคนไปเที่ยวนี่นะ"

# li "It's a nice house to stay in, though. There's a beach near here too, which Akira's especially fond of."
li "แต่ก็เป็นบ้านที่อยู่สบายนะ มีทะเลอยู่ใกล้ ๆ ด้วย พี่ฉันชอบทะเลเป็นพิเศษเลยละ"

# hi "She's a swimmer?"
hi "พี่อากิระว่ายน้ำเก่งเหรอ"

# li "She's constantly dragging me there to have swimming competitions. Which she wins. Every time."
li "พี่ลากฉันไปแข่งว่ายน้ำด้วยประจำเลย แล้วพี่ก็ชนะตลอด"

# "Lilly doesn't strike me as very athletic at all, so not being adept at swimming seems logical enough."
"ลิลลี่ดูจะไม่ใช่สายออกกำลังกายเลย ซึ่งก็ไม่แปลกอะไรที่เธอจะว่ายน้ำไม่เก่ง"

# "The fastest I've ever seen her move is her understandably relaxed pace during her walks to and from the suburbs down the hill from the school. It makes the image of her swimming hard to imagine."
"การเคลื่อนไหวของลิลลี่ที่เร็วที่สุดเท่าที่ฉันเคยเห็นคือตอนที่ลิลลี่เดินสบาย ๆ ตอนที่ขึ้นลงเนินเขาที่อยู่ระหว่างโรงเรียน\nกับชานเมือง ซึ่งพอเป็นอย่างนี้แล้วก็ทำให้นึกภาพเวลาลิลลี่ว่ายน้ำแทบไม่ออกเลย"

# hi "The beaches there must look nice. They'd be less crowded than the ones around here at least."
hi "ทะเลที่นู่นคงสวยน่าดู อย่างน้อยก็น่าจะคนไม่เยอะเท่าที่นี่"

# li "Indeed, Akira says the area around here looks beautiful because it's so far outside the city."
li "ใช่จ้ะ พี่บอกว่าแถวนี้วิวดีเพราะไกลจากตัวเมืองมาก"

# "I only realize what I've said after I say it, but it doesn't bother her at all. It's still easy to forget that she can't see when she's not around, despite the time we've been friends."
"เมื่อพูดแล้วฉันถึงฉุกคิดได้ว่าพูดอะไรออกไป แต่ลิลลี่ก็ดูจะไม่คิดมากอะไร พอไม่ได้อยู่ด้วยแล้วก็ลืม ๆ เหมือนกันว่าลิลลี่\nมองไม่เห็น ทั้งที่เป็นเพื่อนกันมาสักพักแล้วแท้ ๆ"

# li "That said, the local accent sometimes makes communication a bit hard. It's a constant reminder that this isn't home."
li "แต่ถึงอย่างนั้นก็มีปัญหาเรื่องการสื่อสารอยู่บ้างเพราะเรื่องสำเนียงของที่นี่ ซึ่งก็เป็นสิ่งเตือนใจว่าที่นี่ไม่ใช่บ้าน"

# "While the fact that she doesn't consider her parents' residence to be her home makes good sense, it makes me realize that I can't really answer whether the same goes for me."
"ไม่แปลกที่ลิลลี่จะมองว่าที่อยู่ของพ่อแม่เธอนั้นไม่ใช่บ้านของเธอเอง และยังทำให้ฉันมาย้อนคิดว่าฉันมองอย่างนั้นด้วย\nหรือเปล่า ซึ่งฉันก็ไม่แน่ใจเหมือนกัน"

# "Graduation from Yamaku is distant enough to be difficult to view objectively, and I've spent so much time in this small room. I've come to accept the dormitory as my new home surprisingly quickly."
"วันจบการศึกษายังอีกนาน ฉันจึงมองเรื่องของวันนั้นให้แน่ชัดไม่ได้ และฉันก็ใช้เวลาอยู่กับห้องเล็ก ๆ ห้องนี้มานานแล้ว\nฉันถือเอาหอพักนี้เป็นบ้านใหม่ได้อย่างรวดเร็วเหลือเชื่อ"

# hi "I guess that would be hard to deal with. Is your knowledge of English holding up?"
hi "ลำบากแย่เลย ภาษาอังกฤษของเธอยังไหวหรือเปล่า"

# li "Thankfully. I may be fluent, but being in a position where I have to use it often helps in curbing my Japanese accent, so it's been useful practice."
li "ไหวอยู่จ้ะ ถึงจะใช้ได้คล่องแล้ว แต่พอมาอยู่กับสภาพแวดล้อมที่ต้องพูดบ่อย ๆ ก็ช่วยให้สำเนียงญี่ปุ่นหายไปได้ด้วย\nถือว่าเป็นการฝึกได้อย่างดีเลยละจ้ะ"

# li "I hear you're trying to teach yourself English?"
li "ได้ยินมาว่าเธอหัดพูดภาษาอังกฤษอยู่ด้วยใช่มั้ย"

# hi "More like memorizing a few lines, and failing at even that much. I'm really not cut out for learning another language."
hi "จำ ๆ มาแบบกระท่อนกระแท่นมากกว่า แถมยังจำไม่รอดอีกต่างหาก ฉันนี่ไม่เหมาะกับการเรียนภาษาเลยจริง ๆ"

# "My admission of defeat draws an amused giggle."
"คำยอมรับความพ่ายแพ้ของฉันทำให้ลิลลี่หัวเราะคิกคักชอบใจ"

# li "I believe that there are things one chooses to do in life, and also things that are chosen for one to do in life."
li "ฉันเชื่อว่าคนเรามีทั้งสิ่งที่ตัวเองเลือกที่จะทำและสิ่งที่ถูกเลือกมาให้ตัวเองทำนะ"

# li "You can take comfort in the fact you're better than me in science and math, at least."
li "อย่างน้อยเธอก็สบายใจได้ว่าเธอเก่งวิทยาศาสตร์กับคณิตศาสตร์กว่าฉันแน่นอน"

# hi "All that's helped in is making me Mutou's star student…"
hi "เก่งไปก็เป็นได้แค่นักเรียนดีเด่นของครูมุโต้เนี่ยนะ…"

# li "I wouldn't worry about it. They're useful skills for many jobs, right?"
li "ไม่เห็นจะเป็นไรเลยนี่จ๊ะ ยังไงทักษะพวกนั้นก็ใช้ทำงานได้หลายอย่างเลยใช่มั้ย"

# hi "That's what he tells me. His face veritably lit up when I said I'd probably go into a career involving either."
hi "ครูก็บอกอย่างนั้นแหละ พอบอกว่าจะไปทางวิชาพวกนั้นนะ หน้านี่ยิ้มบานมาแต่ไกลเลย"

# "We both share a warm laugh at the events that have befallen each other on opposite ends of the world. It's nice, and reminds me of our simple smalltalk that I've been missing since she left."
"พวกเราหัวเราะด้วยกันอย่างอบอุ่นให้กับเหตุการณ์ทั้งหลายที่เกิดขึ้น ณ สองฟากโลก รู้สึกดีเหมือนกัน พอได้คุยแล้ว\nก็ชวนให้นึกถึงการคุยเรื่อยเปื่อยอย่างนี้ที่ไม่ได้คุยนับตั้งแต่ที่ลิลลี่ไปสกอตแลนด์ด้วย"

# "As each of us waits for the other to begin speaking, I decide to push ahead with my feelings. I can feel my throat tightening slightly."
"ระหว่างที่เราทั้งสองคนต่างรออีกฝ่ายให้พูดก่อนฉันก็ตัดสินใจบอกความรู้สึกตัวเองออกไป รู้สึกคอตีบขึ้นมาหน่อย ๆ\nเลยแฮะ"

# hi "We… um, I… miss you."
hi "พวกเรา… เอ่อ ฉัน… คิดถึงเธอนะ"

# "The silence on the other end of the phone tells me she's given the words their due weight, but as it goes on I can't help feeling more and more apprehensive."
"ความเงียบจากฝั่งปลายสายบ่งบอกว่าเธอกำลังใคร่ครวญกับคำพูดนั้นตามสมควร แต่ยิ่งเงียบไปเรื่อย ๆ ฉันก็อด\nกระวนกระวายใจไม่ได้"

# "Thankfully the silence ends, almost as quickly as it had begun."
"โชคดีที่มีเสียงตามมาอย่างรวดเร็วเหมือนอย่างตอนที่ความเงียบนั้นเริ่มขึ้นมา"

# li "I miss you too, Hisao."
li "ฉันก็คิดถึงเธอนะ ฮิซาโอะ"

# li "Goodbye."
li "ลาก่อนจ้ะ"

# hi "Goodbye, Lilly."
hi "ลาก่อนนะลิลลี่"

stop music fadeout 6.0

# "Once again, the phone is hung up; simply and without any further ado."
"และสายก็ตัดไปอีกครั้ง รวดเร็วง่ายดายเช่นนั้น"

show phone mobile:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with None

scene bg school_dormhisao_ss
show phone mobile:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with locationchange
with Pause (0.5)

hide phone
with None

# "That light, tentative, almost shy voice. Her warm and soft tone… I'd simply be lying to myself if I were to say that I don't recognize this feeling for what it is."
"น้ำเสียงอึกอักฟังดูขวยเขินอันอบอุ่นนุ่มนวลนั้น… ถ้าจะให้บอกว่าฉันไม่รู้จักความรู้สึกในใจนี้ก็คงเป็นการหลอกตัวเอง\nแล้วละ"

# "With thoughts of Lilly dancing on my mind, I start anticipating her return. Today has been a most excellent day."
"ฉันตั้งตาคอยให้ลิลลี่กับมาพร้อมหัวสมองที่วนเวียนอยู่กับเรื่องของเธอ วันนี้ช่างเป็นวันที่ดีเสียจริง"

scene black
with dissolve

#**************************************

label th_L13:

scene bg school_scienceroom
with locationchange

# "I sit listening to another of Mutou's long-winded lectures, my mind wandering far from the scribbles on the dirty blackboard."
"ฉันนั่งฟังที่ครูสอนอย่างยืดยาวน่าเบื่อเช่นเคย จิตใจลอยไกลห่างไปจากรอยขีดขยุกขยิกที่อยู่บนกระดานดำ\nอันมอมแมม"

play music music_tranquil fadein 4.0

nvl clear

window hide
nvl show dissolve

# n "\n\nSince I called Lilly, my mind's been drawn in two directions. Both, roughly, lead to the same conclusion; I've started to feel oddly detached from my past life."
n "\n\nตั้งแต่ที่โทร. หาลิลลี่ครั้งนั้น จิตใจฉันก็ลอยไปสองทางพร้อม ๆ กัน ซึ่งทั้งสองทางนั้นก็พอจะชี้มายังข้อสรุปเดียวกัน\nว่าฉันนั้นไม่ได้ยึดติดกับชีวิตในอดีตแล้วแปลก ๆ"

# n "It's only been a month and a half since I arrived here, yet this school's become a second home. I've gained new friends and contacts, managed to get to grips with the school's lifestyle and culture, and become accustomed to the quirks of my classmates."
n "ฉันเพิ่งมาเรียนที่นี่ได้เดือนกว่า ๆ แต่โรงเรียนแห่งนี้กลับกลายเป็นบ้านหลังที่สองไปแล้ว ฉันได้รู้จักคนใหม่ ๆ ได้เพื่อน\nใหม่ ๆ คุ้นชินกับวิถีชีวิตและวัฒนธรรมของโรงเรียนนี้ และยังคุ้นเคยกับความพิเศษของเพื่อนร่วมชั้นแล้ว"

# n "To become used to a school where disabilities are the norm, rather than the rare exception, still catches me off guard sometimes when I think on it. The same school that's populated by burn victims, amputees, the blind, the deaf and all manner of disabilities inbetween."
n "พอคิดดูแล้วก็น่าตกใจเหมือนกันที่ฉันชินกับการอยู่โรงเรียนที่ความพิการนั้นเป็นเรื่องปกติ ไม่ใช่ข้อยกเว้นพิเศษอะไร\nโรงเรียนที่มีนักเรียนที่เป็นแผลไฟไหม้ ไม่มีแขนขา ตาบอด หูนวก และความพิการทั้งหลายทุกรูปแบบ"

# n "If someone had described this school to me before I'd come, I'd have shrugged it off as an overactive imagination. Even when I first arrived I felt like the Dutch, coming to this strange new land for the first time."
n "ถ้ามีคนมาบรรยายเรื่องโรงเรียนนี้ให้ฟังก่อนที่ฉันจะมาจริง ๆ ฉันคงไม่ใส่ใจคิดไปว่าที่พูดนั้นคิดเกินจริงไปหรือเปล่า\nขนาดตอนที่ฉันมาเป็นครั้งแรกยังรู้สึกตัวเองเหมือนเป็นชาวฮอลันดาที่มาเหยียบแผ่นดินใหม่อันน่าพิศวงนี้\nเป็นครั้งแรกเลย"

# n "It's amazing how quickly one becomes used to the environment they're forced to live in, really. And now I've even found someone that's got me entirely smitten. What a strange life."
n "การที่คนเราปรับตัวกับสภาพแวดล้อมที่ถูกบังคับให้อยู่ได้อย่างรวดเร็วนั้นน่าทึ่งจริง ๆ แล้วตอนนี้ยังมีคนที่ฉันชอบ\nหัวปักหัวปำอีกต่างหาก ชีวิตคนเรานี่ช่างน่าพิศวงเสียจริง"

nvl clear
nvl hide dissolve
window show

# "Before my mind can wander any further, though, I find a page of lined paper slipped under my distracted face. The garish, bright pink ink has no doubt been penned by Misha."
"แต่ก่อนที่ใจฉันจะลอยไปไกลกว่านั้นก็มีกระดาษตีเส้นแผ่นหนึ่งที่สอดมาอยู่ตรงหน้าฉันที่เหม่อ ๆ อยู่ หมึกสีชมพูสด\nแสบตานั้นบอกชัดว่าผู้เขียนคือมิช่า"

window hide

show misha hips_grin_close at offscreenleft
with None

show misha hips_grin_close:
    xpos 0.1 xanchor 0.5
show bg school_scienceroom at left
with charamove


# $ written_note(u"Don't look so bored, Hicchan! School's nearly over! Three-day holiday!", text_args={"color":"#FF2AAA"})
$ written_note(u"อย่าทำหน้าเซ็งอย่างนั้นสิฮิจัง! เดี๋ยวก็ได้หยุด\nแล้ว! หยุดสามวันเลยนะ!", text_args={"color":"#FF2AAA"})

window show

# "Oh, right, we get Saturday and Monday off. Can't complain about having less school, I suppose."
"อ้อ จริงสิ วันเสาร์กับวันจันทร์ที่จะถึงนี้หยุดนี่นา ก็ดีละมั้งที่ได้หยุดเรียน"

# "I uncap my pen and scribble on the page before covertly passing it back to her, flicking my eyes to the front of the class every now and then. Mutou continues scrawling away arcane equations and formulas on the board."
"ฉันเปิดปลอกปากกาแล้วเขียน ๆ ลงบนแผ่นกระดาษก่อนจะแอบส่งคืนให้มิช่าพลางลอบมองหน้าห้องเป็นระยะ ๆ คุณครู\nยังคงขีดเขียนสูตรกับสมการอันลึกลับอยู่กับกระดานดำ"

window hide

# $ written_note(u"I'm guessing you have something planned?")
$ written_note(u"มีแผนว่าจะทำอะไรแล้วเหรอ")

show misha perky_smile_close
with charachange

window show

# "Misha takes the paper back and hunches over it comically, even for her, with her tongue poking through the side of her mouth. Did she misinterpret my expression as depressed, and is she trying to cheer me up?"
"มิช่าหยิบกระดาษไปก้มหน้าอ่าน—ซึ่งท่านั้นดูตลก ขนาดว่าคนทำเป็นมิช่าแท้ ๆ —พลางเลียริมฝีปาก นี่เข้าใจผิด\nว่าฉันเขียนไปด้วยอารมณ์หม่น ๆ แล้วอยากให้ฉันร่าเริงขึ้นเหรอ"

window hide

show misha sign_smile_close
with charachange

# $ written_note(u"Student council work with Shicchan, of course.", text_args={"color":"#FF2AAA"})
$ written_note(u"ก็อยู่ทำงานสภานักเรียนกับชิจังนั่นแหละ", text_args={"color":"#FF2AAA"})

# $ written_note(u"You're not still brooding over that, surely?")
$ written_note(u"นี่คงไม่ได้อารมณ์เสียกับเรื่องนั้นอยู่ใช่มั้ย")

show misha hips_frown_close
with charachange

# $ written_note(u"But Hicchan could have helped us poor, lonely girls.", text_args={"color":"#FF2AAA"})
$ written_note(u"แต่ถ้าฮิจังมาช่วยสองสาวโดดเดี่ยวผู้น่าสงสารได้\nก็คงดีสิ", text_args={"color":"#FF2AAA"})

# $ written_note(u"I'd lend you a hand for today if I weren't going to be busy.")
$ written_note(u"ถ้าไม่ติดว่าวันนี้ฉันมีธุระก็อยากไปช่วยอยู่หรอก")

show misha hips_grin_close
with charachange

# $ written_note(u"Ooh, naughty naughty Hicchan!", text_args={"color":"#FF2AAA"})
$ written_note(u"ตายแล้ว ไม่ดีนะ ไม่ดีนะ ฮิจัง!", text_args={"color":"#FF2AAA"})

# $ written_note(u"I'm just going to meet Lilly with Hanako. I don't know what you've got going through your head.")
$ written_note(u"ฉันแค่จะไปหาลิลลี่กับฮานาโกะเอง นี่คิดอะไรของเธอ\nอยู่เนี่ย")

show misha perky_smile_close
with charachange

# $ written_note(u"So Lilly's back?", text_args={"color":"#FF2AAA"})
$ written_note(u"แปลว่าลิลลี่กลับมาแล้ว?", text_args={"color":"#FF2AAA"})

# $ written_note(u"Yeah, she's coming on the evening flight with her sister, so she'll be back in school next week.")
$ written_note(u"อาฮะ เย็นนี้ลิลลี่จะบินกลับมาพร้อมพี่อากิระ\nเดี๋ยวอาทิตย์หน้าก็กลับมาเข้าเรียนแล้ว")

show misha hips_grin_close
with charachange

window show

# "As she takes the note back and begins to write, I look up to see an unwelcome sight."
"จังหวะที่มิช่าหยิบกระดาษไปแล้วเริ่มเขียนฉันก็เงยหน้าขึ้นพบกับภาพอันไม่น่ายินดี"

stop music fadeout 2.0

show muto irritated behind misha at Alphain(1.0), Slide(0.8, 0.5, 0.6, 0.5, 1.0)
with Pause(0.5)

# "While I frantically try to silently catch Misha's attention, Mutou confidently strides though the gap between the desks from the front of the class, his intent gaze focused directly on her."
"ระหว่างที่ฉันกำลังคอยทำท่าให้มิช่าสนใจอยู่เงียบ ๆ จนจะเป็นบ้านั้นครูก็เดินอาด ๆ จากหน้าห้องมาตามทางเดิน\nระหว่างโต๊ะโดยที่สายตามุ่งตรงไปที่มิช่า"

show misha perky_confused_close
with charachange

# "She suddenly stops writing as his tall figure casts an impossibly long shadow over the page."
"มิช่าชะงักมือไปเมื่อเงาทอดยาวจากร่างสูงของครูพาดผ่านหน้ากระดาษ"

show misha sign_confused_close
with charachange

# mi "Ah… I…"
mi "อ๊ะ… หนู…"

# "He silently takes the piece of paper from her and begins to read."
"ครูคว้าเศษกระดาษไปเงียบ ๆ แล้วอ่าน"

# "Sweating bullets, I quickly glance around the class, noting their complete silence. Of course, it would just have to be the one thing that actually gets their attention during the lesson."
"ฉันมองไปรอบ ๆ พร้อมเหงื่อที่ผุดพรายเมื่อเห็นว่าทั้งห้องเงียบเป็นเป่าสาก แหงละ ก็มีแต่อะไรอย่างนี้นั่นแหละที่จะทำให้\nคนในห้องหันมาสนใจในชั่วโมงเรียนได้"

play sound sfx_impact
show misha perky_sad_close
with vpunch

# "After a scant few seconds examining the page, he rolls the paper up into a small tube and lightly bops Misha over the head with it."
"พอดูแผ่นกระดาษได้สักสองสามวินาทีครูก็ม้วนกระดาษแผ่นนั้นแล้วเคาะหัวมิช่าเบา ๆ"

show muto normal
with charachange

# mu "Half an hour until you can hop off to the Student Council. I think you can hold on until then."
mu "อีกครึ่งชั่วโมงค่อยไปสภานักเรียนนะ แค่นี้คงรอไหวใช่มั้ย"

play music music_ease

# "Misha's face cracks as the entire class erupts into laughter. He might well be awkward, but he knows how to handle her excellently."
"พอคนทั้งห้องระเบิดหัวเราะมิช่าก็หน้าเสียไป ถึงจะเป็นคนที่ชวนให้รู้สึกอึดอัด แต่ครูก็รับมือมิช่าได้เป็นอย่างดี"

# "I'd probably feel sorry for her if I weren't as busy stifling my own laughter."
"ก็คงจะสงสารมิช่าให้อยู่หรอก ถ้าไม่ติดว่าฉันเองก็กำลังกลั้นขำอยู่อะนะ"

scene bg hosp_ext at right
show hanako basic_distant_cas at center
with shorttimeskip

play ambient sfx_rooftop fadein 2.0

# ha "Hisao, is that one it?"
ha "ฮิซาโอะ ใช่ลำนั้นมั้ย"

# hi "No, I think that's some foreign airline."
hi "ไม่นะ ลำนั้นน่าจะเป็นของสายการบินต่างชาติที่อื่น"

# "And so, the third aircraft they're not on comes in to land."
"และเครื่องบินลำที่สามที่ลิลลี่และอากิระไม่ได้โดยสารมาก็ลงจอด"

# "For the past half hour we've been whiling away the time with small snippets of pointless chatter. Lilly and Akira's flight has been delayed, and at this rate it'll probably be dark before their plane arrives."
"พวกเรานั่งคุยเรื่อยเปื่อยฆ่าเวลามาแล้วสามสิบนาทีได้ เที่ยวบินของลิลลี่กับอากิระนั้นจะมาล่าช้า ซึ่งขืนเป็นอย่างนี้\nกว่าสองคนนั้นจะมาถึงก็คงมืดเสียก่อน"

show hanako def_worry_cas at twoleft
with shorttimeskip

# ha "Is that one it?"
ha "ใช่ลำนั้นมั้ย"

# hi "No, the company colors are wrong."
hi "ไม่นะ ดูจากสีแล้วเป็นคนละสายการบิน"

show hanako basic_distant_cas
with charachange

show hanako basic_normal_cas
with charachange

# "Hanako's eyes flutter left and right, following the trickle of people in and out of the huge glass doors ahead of us. Fortunately nobody pays her much heed, their attention apparently directed towards greater things."
"ฮานาโกะทำตาหลุกหลิกไปมาตามฝูงชนที่เดินขวักไขว่เข้าออกประตูกระจกบานใหญ่ที่อยู่ตรงหน้าเรา โชคดีที่ไม่มีใคร\nสนใจอะไรเธอ ดูท่าว่าแต่ละคนต่างมีสิ่งที่สำคัญกว่าให้สนใจ"

show hanako emb_timid_cas at tworight
with shorttimeskip

# ha "Maybe that one is it?"
ha "ใช่ลำนั้นมั้ย"

# hi "No, I think that's… hold on a minute, I think that one might be it after all."
hi "ไม่นะ ฉันว่าลำนั้น… เดี๋ยวนะ ลำนี้น่าจะใช่แล้วแหละ"

show hanako cover_distant_cas at center
with shorttimeskip

# "It takes still some more time before the billboard changes their flight's status to “disembarking.”"
"แต่ยังต้องรออีกสักพักก่อนป้ายประกาศจะเปลี่ยนสถานะเที่ยวบินเป็นคำว่า “ลงจอด”"

# "A loud yawn sneaks up on me, not allowing enough time to stifle it. My sleep patterns have, once again, been all over the place; likely due to a mix of worrying about Hanako and the side-effects of my medications."
"ฉันอ้าปากหาวหวอดโดยไม่ทันได้ตั้งตัวที่จะปิดปาก ตารางการนอนของฉันกลับมาวุ่นวายอีกแล้ว ซึ่งก็คงจะเป็นผล\nจากการที่เป็นห่วงฮานาโกะกับผลข้างเคียงของยานั่นแหละ"

show hanako emb_smile_cas
with charachange

# ha "Hisao, over there…"
ha "ฮิซาโอะ ตรงนั้น…"

# "I look to Hanako, then follow her gaze to the airport door."
"ฉันมองไปทางฮานาโกะก่อนจะมองตามสายตาของเธอไปที่ประตูหน้าสนามบิน"

# aki "Hmm? Oh, Lilly, they're here!"
aki "หืม? อ้าว ลิลลี่ มากันแล้ว!"

# li "Really?"
li "จริงเหรอ"

show akira basic_smile:
    xanchor 0.5 xpos -0.3
show lilly basic_cheerful at offscreenleft
with None

show akira basic_smile at left
show lilly basic_cheerful_cas:
    xanchor 0.5 xpos 0.4
show hanako emb_smile_cas at tworight
show bg hosp_ext at center
with charamove

# "We all call out to each other in greeting, quickly shuffling over to the side to avoid blocking the passage of others."
"พวกเราเรียกชื่อทักทายกันก่อนจะย้ายตัวมาอยู่ด้านข้างไม่ให้เกะกะทางคนอื่น"

# ha "Lilly!"
ha "ลิลลี่!"

show hanako emb_downsmile_cas at center
with dissolvecharamove

# "Hanako jumps forward to hug Lilly, a wide smile on her face being all that's needed to see her happiness at Lilly's return. Lilly simply smiles in return, her voice soft."
"ฮานาโกะพุ่งตัวเข้ากระโดดกอดลิลลี่ เธอยิ้มกว้างแทนความดีใจที่ลิลลี่กลับมาอีกครั้ง ส่วนลิลลี่เพียงยิ้มตอบก่อนจะ\nเอ่ยด้วยเสียงอันนุ่มนวล"

show lilly basic_smileclosed_cas
with charachange

# li "It's wonderful to meet you again, Hanako."
li "ยินดีที่ได้พบอีกครั้งจ้ะฮานาโกะ"

show akira basic_smile at twoleft
show lilly basic_smileclosed_cas:
    xpos 0.6
show hanako emb_downsmile_cas at tworight
show bg hosp_ext:
    xpos 0.55
with charamove

# "As the two give each other a hug, well deserved after all that's happened while she was gone, I turn to Akira."
"พอทั้งสองคนกอดกันจนหนำใจกับเรื่องทั้งหลายแหล่ที่เกิดเมื่อลิลลี่ไม่อยู่แล้วฉันก็หันไปมองอากิระ"

show akira basic_ending
with charachange

# aki "Yo."
aki "ไง"

# hi "You're pretty late."
hi "มาช้านะครับ"

show akira basic_annoyed
with charachange

# aki "Yeah, there was a really bad storm over the airport. We got drenched just going from the car to the door."
aki "อืม พอดีที่สนามบินพายุเข้าหนักเลยแน่ะ ตอนออกจากรถเดินมาประตูสนามบินนี่เปียกฝนหมด"

# hi "I guess you'll appreciate the weather here more, then. Welcome back to you too, Lilly."
hi "งั้นคงชอบสภาพอากาศที่นี่มากกว่าสินะครับ ยินดีต้อนรับกลับนะลิลลี่"

stop music fadeout 4.0

show hanako basic_smile_cas:
    xpos 0.8
show akira basic_smile
show lilly basic_weaksmile_cas
with dissolvecharamove

# "Hanako breaks off from Lilly as I speak. For a long time, neither of us says a word."
"พอฉันทักฮานาโกะก็ผละตัวออกจากลิลลี่ พวกเราสองคนเงียบไปนานสองนาน"

# "Contrary to what I'd thought her homecoming would be like, the atmosphere feels awkward, almost stifling. Both of us try to guess each other's feelings, not quite sure about what should be said."
"บรรยากาศนั้นอึดอัดจนแทบหายใจไม่ออก ซึ่งขัดกับสิ่งที่ฉันคิดไว้ว่าพอมาต้อนรับกลับบ้านอย่างนี้แล้วน่าจะดีกว่านี้\nพวกเราสองคนต่างเดาความรู้สึกอีกฝ่ายพลางชั่งใจว่าจะพูดอะไรดี"

# "Damn. This is exactly what I feared when I'd thought of trying to move things forward between us. Lilly runs her hand through her fair hair and awkwardly twirls one of her bangs in her fingers, clearly trying to think of how best to react."
"ให้ตาย นี่แหละคือสิ่งที่ฉันกลัวที่สุดตอนที่ฉันตัดสินใจจะเดินหน้าความสัมพันธ์ระหว่างเราต่อ ลิลลี่สางผมตัวเอง\nก่อนจะใช้นิ้วม้วนผมหน้าม้าครุ่นคิดว่าจะทำตัวอย่างไรดี"

# "Eventually, thankfully, Lilly gives a small sigh and breaks the silence."
"ซึ่งยังดีที่สุดท้ายลิลลี่ก็ถอนหายใจเล็กน้อยแล้วพูดขึ้นมา"

show lilly basic_smile_cas
with charachange

play music music_lilly fadein 6.0

# li "Thank you, Hisao. It's nice to be back."
li "ขอบคุณนะฮิซาโอะ ดีใจจังที่ได้กลับมา"

show hanako basic_worry_cas
with charachange

# ha "Are you okay? You look tired."
ha "เธอไหวหรือเปล่า ดูเพลีย ๆ นะ"

# "Evidently not recollecting herself all that well, she quickly waves her hand in front of her face to stave off any concern Hanako may have over her."
"ถึงจะชัดว่าสติของเธอจะยังไม่ได้อยู่กับตัวเต็มที่ แต่ลิลลี่ก็โบกมือปัด ๆ เป็นเชิงไม่ให้ฮานาโกะเป็นห่วงอะไรกับตัวเอง\nให้มากนัก"

show lilly basic_weaksmile_cas
with charachange

# li "I'm okay, really. It's just a bit of jet lag."
li "ยังไหวอยู่จ้ะ พอดีเจ็ตแล็กนิดหน่อย"

show akira basic_laugh
with charachange

# aki "Weak."
aki "อ่อน"

# hi "You don't have any?"
hi "พี่ไม่เป็นเลยเหรอครับ"

show akira basic_ending
with charachange

# "She simply gives a big grin, puffing out her modest chest."
"อากิระเพียงแสยะยิ้มพลางยืดอกที่เธอมีอยู่พอประมาณ"

# aki "I feel absolutely fine!"
aki "สอบอมอยอหอ!"

show lilly basic_sleepy_cas
with charachange

# li "That's not fair…"
li "ไม่ยุติธรรมเลย…"

show akira basic_smile
show hanako basic_normal_cas
with charachange

# aki "Haha, ah well. Ya shouldn't take too long to get rid of it."
aki "ฮ่า ๆ เอาเถอะ เดี๋ยวเดียวก็คงหายแล้ว"

show lilly basic_smile_cas
with charachange

# li "Ah! That's right, Hisao?"
li "อ้อ! จริงสิ ฮิซาโอะ"

# hi "Yeah?"
hi "ว่า"

show lilly basic_smileclosed_cas
with charachange

# li "Don't we have a holiday from school soon?"
li "เดี๋ยวจะได้หยุดใช่มั้ย"

# hi "I'd have forgotten if Misha hadn't reminded me this morning. We've got a three-day weekend starting from tomorrow."
hi "ถ้าเช้านี้มิช่าไม่ทักฉันก็คงลืมไปแล้วละ พรุ่งนี้เราจะได้หยุดยาวสามวันกัน"

show akira basic_laugh
with charachange

# "Akira playfully bumps her elbow lightly into Lilly's side, grinning."
"อากิระถองศอกกระเซ้าลิลลี่พลางยิ้มน้อยยิ้มใหญ่"

show akira basic_smile
with charachange

# aki "Told ya you wouldn't miss it."
aki "บอกแล้วว่าทัน"

# hi "You have something planned?"
hi "มีแผนจะทำอะไรหรือเปล่า"

show lilly basic_smile_cas
with charachange

# li "If neither you nor Hanako are busy…"
li "ถ้าเธอสองคนว่าง…"

# hi "I've got no plans, so something to do would be appreciated. Hanako?"
hi "ฉันก็ว่าง ๆ อยู่ หาอะไรทำก็ดีเหมือนกัน ฮานาโกะว่าไง"

show hanako basic_smile_cas
with charachange

# ha "No, nothing."
ha "อื้ม ว่าง"

show lilly basic_cheerful_cas
with charachange

# li "That's good. I was thinking we could go to my family's summerhouse for a bit of quiet over the break. We've rarely used it recently, though, so we'd have to dust things off a little while we're there."
li "ดีเลย ฉันกะจะชวนไปเที่ยวที่บ้านพักตากอากาศของครอบครัวฉันเป็นการพักผ่อนหย่อนใจช่วงวันหยุดด้วยกันสักหน่อย\nแต่พักหลัง ๆ มาไม่ค่อยได้ไปอยู่เท่าไหร่ อาจจะต้องไปทำความสะอาดอะไรสักหน่อยด้วย"

# hi "Oh? Where is it?"
hi "เหรอ แล้วบ้านพักตากอากาศที่ว่านี่อยู่ที่ไหนล่ะ"

show akira basic_ending
with charachange

# aki "Up north, in Hokkaido. The place is practically deserted, so it should be a nice quiet break for you guys."
aki "ขึ้นเหนือไปฮกไกโดนู่นเลย แถวนั้นแทบไม่มีคนอยู่ด้วย น่าจะใช้อยู่พักผ่อนแบบสงบ ๆ ได้สบาย"

# hi "You're not coming?"
hi "พี่ไม่ไปด้วยเหรอครับ"

show akira basic_smile
with charachange

# aki "Nah. Got a little holiday of my own set up with my boyfriend."
aki "ไม่อะ พอดีคิววันหยุดยกให้แฟนไปแล้ว"

# "I lower my eyes at her, suspicious of her intentions."
"ฉันหรี่ตามองด้วยความเคลือบแคลงในเจตนาของอีกฝ่าย"

# hi "It sounds like we're just cleaning up the summerhouse for you."
hi "นี่กะจะให้ไปทำความสะอาดบ้านพักตากอากาศให้ใช่มั้ยครับ"

show lilly basic_displeased_cas
with charachange

# li "That's… perhaps a valid conclusion…"
li "ฟังดู… เป็นไปได้อยู่นะ…"

# "Both of us zero in on Akira, her face somewhat evasive. Looks like we were right."
"เราสองคนพุ่งสายตาไปที่อากิระที่หลบ ๆ หน้าอยู่ ดูท่าว่าจะคิดถูก"

show akira basic_boo
with charachange

# aki "That's just a convenient bonus. Really. Me and the guy left it in pretty good condition last we were there, I promise."
aki "อันนั้นก็ของแถมดี ๆ เฉย ๆ น่า จริง ๆ นะ ครั้งล่าสุดที่ฉันไปเที่ยวกับแฟนก็รักษาสภาพไว้เนี้ยบพอสมควรเลย จะบอกให้"

show akira basic_smile
with charachange

# aki "Now then, I'm outta here."
aki "เอาละ ๆ ขอตัวก่อนนะ"

show lilly basic_reminisce_cas
with charachange

# li "Already? Akira…"
li "จะไปแล้วเหรอพี่…"

# "She quickly turns and walks away, her hand held high."
"อากิระหันขวับเดินออกไปแล้วชูมือ"

show akira basic_laugh
with charachange

# aki "See ya in a few days, guys."
aki "อีกสักสองสามวันเจอกัน"

show akira basic_laugh at Alphaout(1.0), offscreenleft
with charamove

hide akira
with None

show lilly basic_reminisce_cas:
    xpos 0.4
show hanako basic_smile_cas:
    xpos 0.6
show bg hosp_ext at bgleft
with charamove

# "Lilly and I can only sigh at her hasty retreat."
"ฉันกับลิลลี่ได้แต่ถอนหายใจให้กับอากิระที่ถอนตัวไปอย่างรีบร้อน"

show hanako cover_bashful_cas
with charachange

# ha "It does sound like it would be a nice place to go."
ha "ฟังดูน่าเที่ยวเหมือนกันนะ"

show lilly basic_smileclosed_cas
with charachange

# "Lilly gives an enthusiastic nod, taking her carry bag in one hand and placing her other on Hanako's shoulder for guidance as we begin to make our way to the taxi area."
"ลิลลี่พยักหน้าด้วยความตื่นเต้น เธอถือกระเป๋าไว้ที่มือข้างหนึ่ง ส่วนอีกข้างนั้นจับไหล่ฮานาโกะให้นำทางไป พวกเรา\nเดินไปยังบริเวณที่รถแท็กซี่จอดกันอยู่"

# "After the fracas of the past few days, spending a weekend in the country alone with her and Hanako sounds like a dream."
"พอผ่านเรื่องวุ่นวายเมื่อสองสามวันก่อนมาได้แล้วก็ทำให้รู้สึกว่าที่จะได้ไปเที่ยวด้วยกันกับลิลลี่พร้อมฮานาโกะนั้น\nเหมือนฝันเลย"

# "The more I think about it, the more sure I am. This will be the right time and place to confess my feelings to her."
"ยิ่งคิดฉันก็ยิ่งแน่ใจ ว่าการไปเที่ยวครั้งนี้จะเป็นทั้งสถานที่และเวลาอันเหมาะสมที่ฉันจะได้เผยความรู้สึกของตัวเองให้ลิลลี่\nได้รับรู้"

stop music fadeout 2.0
stop ambient fadeout 2.0

scene black
with dissolve

#**************************************

label th_L14:

scene bg city_station
with locationchange

play music music_daily fadein 7.0

# "The morning chill wraps itself around my shivering body. I huff into my cupped hands to desperately try and stave off the cold as we mill about on the station platform."
"อากาศเย็นเยียบยามเช้าเข้าห่อร่างอันหนาวสั่นของฉันเอาไว้ ฉันคอยเป่าลมหายใจรดอุ้งมือคลายหนาวอย่าง\nสุดความสามารถระหว่างที่พวกเราเดินเตร็ดเตร่ไปตามชานชาลา"

# "Lilly's clothing looks rather ill-suited for the temperature around us. I can only hope it's indicative of what she expects the weather to be like at our destination."
"เสื้อผ้าที่ลิลลี่ใส่มานั้นดูจะไม่เข้ากับอุณหภูมิโดยรอบขณะนี้สักเท่าไหร่ หวังว่าที่แต่งมาอย่างนี้เพราะรู้ว่าปลายทาง\nสภาพอากาศจะเป็นยังไงนะ"

show lilly basic_sleepy_cas at twoleft
show hanako basic_distant_cas at tworight
with charaenter

# hi "Dammit, Lilly, why'd we have to get here so early?"
hi "ให้ตายเถอะลิลลี่ ทำไมต้องมาแต่ไก่โห่ขนาดนี้"

show lilly basic_displeased_cas
with charachange

# li "Unfortunately the train schedule is against us. The next train to Hokkaido is at two in the afternoon."
li "พอดีว่าเที่ยวรถไฟไม่เป็นใจเท่าไหร่น่ะจ้ะ ขาขึ้นไปฮอกไกโดอีกเที่ยวก็เป็นตอนบ่ายสองนู่นเลย"

# hi "Great. Just great."
hi "เยี่ยม เยี่ยมจริง ๆ"

# "I pause a moment to wipe some sleep out of my eyes, and Lilly promptly takes advantage of the opening."
"ฉันหยุดพูดมาขยี้ตาให้หายงัวเงีย ส่วนลิลลี่ก็ถือจังหวะนั้นพูดแทรกขึ้นมาอีก"

show lilly basic_weaksmile_cas
with charachange

# li "Cheer up, Hisao. Once we get there it'll be much warmer."
li "ร่าเริงหน่อยเถอะจ้ะฮิซาโอะ เดี๋ยวพอไปถึงที่นู่นก็ไม่หนาวเท่าไหร่แล้ว"

# hi "Why not just take the bullet train? A normal train's going to take hours to get us there, so we may as well take the Shinkansen line as far north as it goes, and just switch at the end."
hi "แล้วทำไมไม่นั่งรถไฟความเร็วสูงไปล่ะ ยังไงถ้านั่งรถไฟธรรมดากว่าจะไปถึงก็หลายชั่วโมงอยู่แล้ว นั่งชิงกังเซงขึ้นเหนือ\nไปจนสุดแล้วค่อยเปลี่ยนสายต่อเอาก็ได้"

show lilly basic_smile_cas
with charachange

# li "There's a certain charm to older trains, wouldn't you agree?"
li "รถไฟเก่า ๆ อย่างนี้ก็มีเสน่ห์เหมือนกันนะจ๊ะ เธอว่ามั้ย"

# hi "I'd agree if I weren't freezing in the morning cold because we decided to take one."
hi "ก็คงจะว่าอย่างนั้นอยู่หรอกถ้าฉันไม่ต้องมาทนยืนตัวขดตัวแข็งกับอากาศหนาว ๆ ตอนเช้าอย่างนี้เนี่ย"

show hanako emb_timid_cas
with charachange

# ha "I'm… sorry, Hisao."
ha "ขอ… โทษนะ ฮิซาโอะ"

# hi "Sorry? What for?"
hi "ขอโทษ? เรื่อง?"

show hanako emb_downtimid_cas
with charachange

# ha "I was… the one who suggested taking a normal train."
ha "ฉัน… เป็นคนเสนอให้มานั่งรถไฟธรรมดาเอง"

# "Way to make me feel guilty. All I can do is sigh and cover my face with my hand."
"เป็นคนไม่ดีเลยทีนี้ ฉันได้แต่ถอนหายใจแล้วเอามือแนบหน้าตัวเอง"

# hi "It's fine, I'm just grumbling."
hi "ไม่เป็นไร ฉันแค่บ่นไปเรื่อยแหละ"

show lilly basic_ara_cas
with charachange

# li "My my, Hanako, you needn't shoulder all the blame yourself. Even without your suggestion, I'd still have opted for the same thing."
li "แหม ๆ ฮานาโกะ ไม่ต้องรับผิดคนเดียวอย่างนั้นหรอกจ้ะ ต่อให้เธอไม่ได้เสนอ ฉันก็คงจะเลือกนั่งรถไฟธรรมดาอยู่ดี"

show hanako emb_smile_cas
with charachange

hide hanako
hide lilly
with charaexit

# "Thankful for the quick interception from Lilly, I take a quick gander around the station."
"ฉันถือจังหวะที่ลิลลี่เข้ามาขัดบทสนทนาให้อย่างรวดเร็วนั้นมองไปรอบ ๆ สถานี"

# "Aside from us, the train platform's all but deserted, the morning dew settling on the empty benches. I guess no one else was masochistic enough to brave the very early morning."
"ที่ชานชาลาแห่งนี้นอกจากพวกเราแล้วก็ไม่มีใครเลย ตามม้านั่งที่ว่างมีน้ำค้างยามเช้าเกาะอยู่ คงไม่มีใครอยากทรมาน\nตัวเองด้วยการมาแต่เช้าตรู่ขนาดนี้หรอกมั้ง"

# "Though if someone was, they'd more than notice the huge bags both Lilly and Hanako brought with them."
"และต่อให้ถ้ามีคนจริง ๆ ก็คงเห็นกระเป๋าใบใหญ่ที่ทั้งลิลลี่กับฮานาโกะขนมาแล้ว"

# hi "Just what did you have to pack into those things, anyway?"
hi "แล้วนี่เอาอะไรมาเยอะแยะเนี่ย"

show lilly basic_listen_cas at center
with charaenter

# li "The bags? Hmm…"
li "สัมภาระเหรอ อืมม…"

# "She pauses a moment and tilts her head in thought."
"ลิลลี่เว้นจังหวะเอียงคอเล็กน้อยทำท่าคิด"

show lilly basic_smileclosed_cas
with charachange

# li "A change of clothing, raincoat, underwear, sleepwear, a number of books… I think that's most of it."
li "เสื้อผ้าสำหรับเปลี่ยน เสื้อกันฝน ชุดชั้นใน ชุดนอน หนังสือสองสามเล่ม… ส่วนมากก็น่าจะประมาณนั้นนะ"

# hi "You make it sound as if I'm unprepared."
hi "เทียบกันแล้วของฉันนี่เหมือนแทบไม่ได้เตรียมอะไรมาเลย"

show lilly basic_surprised_cas
with charachange

# li "You brought less?"
li "เธอเอาของมาไม่เยอะเหรอ"

# hi "Underwear and a pack of cards. That's it."
hi "ก็ชุดชั้นในแล้วก็ไพ่หนึ่งสำรับ แค่นั้นแหละ"

# "And my pills, but never mind that."
"แล้วก็ยาด้วย แต่ช่างมัน"

# li "No pajamas?"
li "ชุดนอนล่ะ"

# hi "Damn. I knew I forgot something."
hi "แม่ง ว่าละลืมอะไร"

# "As I ruffle my hair in frustration, Lilly sighs."
"ฉันยีผมตัวเองด้วยความหัวเสีย ลิลลี่ถอนหายใจ"

show lilly basic_weaksmile_cas
with charachange

# li "There should be clothes you could use there. Akira still occasionally goes there, after all, and I think some of our parents' clothing is still in storage."
li "ที่นู่นน่าจะพอมีเสื้อผ้าให้เธอใช้เปลี่ยนได้อยู่นะ เพราะยังไงบางทีพี่ก็แวะไปทางนั้นอยู่แล้ว แล้วก็เหมือนเสื้อผ้าของ\nพ่อแม่ฉันจะยังอยู่ในห้องเก็บของด้วย"

show lilly basic_smile_cas
with charachange

# li "I don't think there'll be any problem with you borrowing a set of pajamas, if need be."
li "ถ้าจำเป็นจริง ๆ จะยืมชุดนอนสักชุดก็คงไม่เสียหายหรอกจ้ะ"

# hi "Thanks. Still, I don't mind just sleeping in my normal clothing."
hi "ขอบใจนะ แต่เอาจริง ๆ ฉันก็นอนกับชุดที่ใส่ตามปกติได้แหละ"

show lilly basic_surprised_cas
with charachange

# li "For two days?"
li "แต่ตั้งสองวันเลยนะ"

# hi "Good point."
hi "นั่นสินะ"

# "Not really. Though two days would be borderline, it's more that looking even a little like a slob would be unacceptable while in the presence of two girls."
"จริง ๆ ก็พอทนได้อยู่แหละ สองวันนี่คือเต็มที่แล้ว แต่เรื่องของเรื่องคือฉันจะต้องทำให้สารรูปตัวเองดูดีที่สุดเท่าที่จะทำได้\nเพราะต้องอยู่กับผู้หญิงอีกสองคน"

hide lilly
with charaexit

# "As we leisurely talk on the station platform an announcement sounds from the loudspeakers, loudly heralding our ride's arrival."
"ระหว่างที่พวกเราคุยกันเรื่อยเปื่อยก็มีเสียงจากลำโพงประกาศถึงรถไฟเที่ยวของพวกเราที่กำลังจะมาถึง"

# "Looking past Lilly and Hanako, though, the train's still well out of sight. A quick check of my watch is enough to see that it's the one we'll be taking."
"พอมองผ่านไปทางลิลลี่กับฮานาโกะก็ยังไม่เห็นตัวรถไฟ เวลาบนนาฬิกาข้อมือของฉันบอกว่ารถไฟเที่ยวที่กำลังจะมาถึงนี้\nเป็นเที่ยวที่เราจะขึ้นจริง ๆ"

# hi "The five-thirty train was ours, right?"
hi "เราจะขึ้นเที่ยวตีห้าครึ่งกันใช่มั้ย"

show lilly basic_smileclosed_cas at twoleft
show hanako basic_distant_cas at tworight
with charaenter

# li "Correct."
li "ใช่จ้ะ"

# hi "Either of you want me to take your bags? Mine's not exactly heavy."
hi "มีใครอยากฝากให้ฉันถือสัมภาระมั้ย พอดีของฉันไม่ค่อยหนักเท่าไหร่"

show lilly basic_ara_cas
with charachange

# li "My my, that's very gentlemanly of you, Hisao."
li "แหม ๆ เป็นสุภาพบุรุษดีจังเลยนะจ๊ะฮิซาโอะ"

# hi "Don't accept too reluctantly, now."
hi "ไม่ต้องเกรงใจหรอกน่า"

# "As I bend down to pick up Lilly's large bag, I look up to see Hanako picking up hers."
"ฉันย่อตัวลงถือกระเป๋าใบใหญ่ของลิลลี่ พอเงยหน้ามองก็เห็นฮานาโกะที่ถือกระเป๋าตัวเองอยู่"

# hi "You fine with that?"
hi "เธอถือไหวใช่มั้ย"

show hanako basic_normal_cas
with charachange

# "A silent nod's the only answer. I'm starting to get the feeling that by the trip's end, I'll be able to count every sentence she said on one hand."
"ฮานาโกะเพียงพยักหน้าตอบเงียบ ๆ รู้สึกว่าตลอดเวลาที่จะได้ไปเที่ยวด้วยกันนี่ฉันคงนับประโยคที่ฮานาโกะพูด\nได้ด้วยมือข้างเดียวเลย"

stop music fadeout 5.0
play ambient sfx_trainint fadein 5.0

$ ksgallery_unlock("ev lilly_trainride")
scene train_scenery
show train_scenery_fg
show evfg lilly_trainride at train_shake
with shorttimeskip

# "With the morning landscape passing by the window and the occasional rattle of the train bumping the carriage around, I try to focus my attention on the aging playing cards held in my hands."
"ทิวทัศน์ยามเช้าเลื่อนไหลผ่านไปตามหน้าต่างพร้อมกับเสียงกึงกังตึงตังจากขบวนรถไฟที่ไหวไปมา ฉันตั้งสมาธิอยู่กับไพ่\nที่ดูเก่า ๆ ในมือ"

# hi "I'll raise you five."
hi "เกเพิ่มอีกห้าตัว"

# ha "Um… I…"
ha "เอ่อ… ฉัน…"

# "She scrunches her face up and leans over to Lilly conspiratorially, the two exchanging a few whispered words. Considering how often this has happened so far, I'm coming to doubt Hanako's grasp of how to play poker."
"ฮานาโกะเงยหน้าขึ้นแล้วเอนตัวไปทางลิลลี่เหมือนมีแผนบางอย่างแล้วกระซิบกระซาบอะไรกัน ซึ่งเธอทำบ่อยจนฉัน\nเริ่มสงสัยแล้วว่าฮานาโกะเล่นโปกเกอร์เป็นจริงหรือเปล่า"

# "It doesn't seem to disturb Lilly's reading though, her hands flitting over each page with only occasional corrections to account for the train's bumping and rocking."
"แต่ลิลลี่ก็ดูไม่ได้เสียสมาธิไปจากการอ่านเลย มือลิลลี่เลื่อนกวาดไปตามหน้าหนังสือเรื่อย ๆ บางครั้งก็ต้องตั้งต้นใหม่\nเพราะแรงโยกจากขบวนรถไฟ"

# "My collection of chess pieces that we're using as chips is steadily growing anyway, so it doesn't really bother me."
"แต่ยังไงกองตัวหมากที่เราใช้แทนชิปกันก็เพิ่มขึ้นเรื่อย ๆ แล้ว เพราะงั้นก็ไม่เป็นไรหรอก"

# "Looking around us, our carriage is almost as empty as the station platform we'd waited for the train itself on. Only a handful of people can be seen, looking mostly like tourists and couples on holiday."
"ฉันมองสำรวจไปรอบ ๆ ในขบวนนั้นค่อนข้างโล่งไม่ต่างอะไรกับชานชาลาที่พวกเรายืนรอกันตอนเช้า แต่ก็ยังพอ\nมีคนอยู่บ้าง ส่วนใหญ่ก็ดูเหมือนจะเป็นนักท่องเที่ยวกับคู่รักที่มาเที่ยววันหยุดด้วยกัน"

# "While the two continue their less-than-clandestine strategizing, a small boy looks over the seat and stares at me. Hoping he doesn't begin to stare at Hanako, I simply give him a wave and a smile."
"ระหว่างที่ทั้งสองคนกำลังวางแผนปรึกษากันในที่ที่ไม่รโหฐานเลยนั้นก็มีเด็กผู้ชายคนหนึ่งมองข้ามพนักพิงจ้องมาที่ฉัน\nฉันโบกมือยิ้มให้พลางหวังว่าเขาจะไม่ไปจ้องฮานาโกะต่อ"

# "Thankfully, he retreats back to his seat after finding me far too boring to waste his attention on."
"โชคดีที่เขากลับไปนั่งที่ตามเดิมเมื่อเห็นว่าฉันนั้นน่าเบื่อเกินกว่าที่เขาจะให้ความสนใจได้"

# ha "I'll see you and raise you… another five."
ha "งั้นฉันขอเกเพิ่มอีก… ห้าตัว"

# hi "Damn, you got me. I fold."
hi "ตายละ ความแตกจนได้ หมอบ ๆ"

# "I've been bluffing, and she's caught me. Hanging my head, I push over a large portion of my winnings."
"เมื่อกี้ฉันแค่เกข่มไปเท่านั้น ซึ่งฮานาโกะจับไต๋ได้แล้ว ฉันห้อยหัวห่อเหี่ยวพลางกวาดกองเดิมพันที่ฉันลงไปให้"

$ ksgallery_unlock("ev lilly_trainride_smiles")
show evfg lilly_trainride_smiles at train_shake
with charachange

# "Hanako looks absolutely delighted, and even if Lilly keeps her attention focused on her reading material, I can see the smirk on her face. They're both extremely pleased."
"ฮานาโกะยิ้มแป้น และลิลลี่ที่เหมือนจะจดจ่ออยู่กับหนังสือของตัวเองก็อมยิ้มอยู่ด้วยเหมือนกัน ทั้งสองคนดูจะชอบใจ\nเอามาก ๆ"

# "For a moment I try to work out what Lilly's reading, but the cover is too faded to read beyond the fact that Roman letters are on it. A pity I can't read the Braille above the printed title."
"ฉันเพ่งมองอยู่พักหนึ่งว่าลิลลี่อ่านอะไรอยู่ แต่ปกก็เลือนไปจนเห็นแค่ว่าที่พิมพ์อยู่นั้นเป็นอักษรภาษาอังกฤษ\nและน่าเสียดายที่ฉันอ่านอักษรเบรลล์ซึ่งพิมพ์อยู่บนตัวอักษรภาษาอังกฤษนั้นไม่ออก"

# hi "What're you reading, Lilly? The title looks like it's in English."
hi "อ่านอะไรอยู่เหรอลิลลี่ เหมือนชื่อจะเป็นภาษาอังกฤษใช่มั้ย"

# li "That's right. It's “And Then There Were None”, an old British story. I could read it to you if you'd like."
li "ใช่จ้ะ วรรณกรรมเก่าจากอังกฤษเรื่อง “{i}And Then There Were None{/i}” จ้ะ ถ้าอยากอ่านด้วย ให้ฉันอ่าน\nให้เธอฟังก็ได้นะ"

# "She extends the offer with a grin, obviously in jest."
"ลิลลี่เสนอพลางยกยิ้มเป็นเชิงขบขัน"

# hi "I think I'll pass, thanks."
hi "ขอบใจ แต่ขอผ่านละกัน"

stop ambient fadeout 2.0

scene bg hok_houseext at Fullpan(10.0, dir="left")
with shorttimeskip

play music music_tranquil fadein 3.0
play ambient sfx_parkambience fadein 4.0

# "After a seemingly endless trip, we finally reach the promised land of the Satou summerhouse. Even after the train trip, the walk up seemed to take forever."
"หลังจากที่เดินทางมานานสักชาติหนึ่งได้ พวกเราก็มาถึงบ้านพักตากอากาศของตระกูลซาโต้เสียที หลังจากที่ลง\nจากรถไฟมาแล้วยังต้องเดินเท้ามาอีกไม่รู้กี่กิโลเมตร"

# "Despite my grumblings though, I'd have never guessed the sight that would be in store for us once we traveled that long, deserted road."
"ถึงจะบ่นอย่างนั้นก็เถอะ ฉันก็ไม่คิดเหมือนกันว่าจะได้มาเห็นภาพตรงหน้านี้หลังจากที่เดินผ่านถนนรกร้างทอดยาว\nอย่างนั้นมา"

# "It looks more like a farmhouse than the everyday house I'd imagined, small in size and surrounded by trees and bushes."
"เป็นบ้านหลังเล็กที่มีสุมทุมพุ่มไม้ร่มครึ้มเหมือนบ้านไร่มากกว่า ไม่เหมือนบ้านปกติทั่วไปอย่างที่ฉันนึกภาพไว้\nสักเท่าไหร่"

# "An empty expanse of wheat fields and farming land can be seen as we walk up, the fencing only consisting of rickety old wooden planks."
"เมื่อเดินเข้าไปอีกก็พบทุ่งสาลีกว้างไกลพร้อมเรือกสวนที่ล้อมด้วยรั้วซึ่งเป็นเป็นไม้เก่าคร่ำคร่า"

# "It really drives home how far we are from the major cities and is a sight that feels antithetical to the environment I grew up in."
"พอได้เห็นแล้วก็ทำให้รู้สึกขึ้นมาทันทีว่าที่ตรงนี้อยู่ห่างจากเมืองใหญ่แค่ไหน ทั้งยังผิดกับสภาพแวดล้อมที่ฉันเคยอยู่"

# "The only thing that doesn't surprise me is its Western styling."
"สิ่งเดียวที่เป็นไปตามคาดคือลักษณะบ้านที่เป็นแบบตะวันตก"

show bg hok_houseext at left
with None

# hi "Wow, it's amazing out here…"
hi "โห สุดยอดไปเลย…"

show lilly basic_smileclosed_cas at twoleft
show hanako basic_bashful_cas at tworight
with charaenter

# ha "Mm, it's wonderful."
ha "อื้ม ดีมาก ๆ"

show lilly basic_smile_cas
with charachange

# li "That's nice to hear. While Akira may have said that she's kept the house in reasonable condition, I was worried that we might have different standards of “reasonable.”"
li "ได้ยินอย่างนั้นฉันก็ดีใจจ้ะ พี่บอกแล้วก็จริงว่ารักษาสภาพไว้ดีพอสมควร แต่ฉันก็อดคิดไม่ได้ว่าคำว่า “พอสมควร”\nของเราเหมือนกันหรือเปล่า"

# hi "It looks like there isn't another soul for miles. I thought Akira would be the type to keep to the city."
hi "เหมือนแถวนี้จะไม่มีใครอยู่เลย นึกว่าพี่อากิระจะเป็นคนที่ชอบอยู่ติดเมืองเสียอีก"

show lilly basic_listen_cas
with charachange

# "Lilly furrows her brow in thought, seemingly recalling almost forgotten knowledge."
"ลิลลี่ขมวดคิ้วครุ่นคิดคล้ายกำลังนึกถึงอะไรบางอย่างที่แทบจะลืมไปแล้ว"

show lilly basic_weaksmile_cas
with charachange

# li "Hmm, from memory there's a small town not too far ahead. Other than that though, this is largely just old farmland."
li "อืมม จำได้ว่าถ้าเดินทางไปอีกหน่อยจะมีหมู่บ้านเล็ก ๆ อยู่ นอกนั้นแถวนี้ก็มีแต่ไร่กับสวนนี่แหละจ้ะ"

show lilly basic_smile_cas
with charachange

# li "Akira and I stayed in our parents' house which was in the nearest city for a while, but after they left we decided to move into a smaller, more easily maintainable, house."
li "พี่กับฉันอยู่บ้านพ่อแม่ที่อยู่ในเมืองใกล้ ๆ อยู่พักหนึ่ง แต่หลังจากนั้นเราก็ย้ายไปบ้านที่หลังเล็กดูแลง่ายหน่อย"

# hi "To find a place like this in Japan nowadays… it's kind of anachronistic."
hi "ญี่ปุ่นสมัยนี้คงแทบไม่มีที่อย่างนี้แล้วมั้งนี่… ออกจะหลงยุคอยู่เหมือนกันนะ"

show lilly basic_smileclosed_cas
with charachange

# li "Well, this town does have quite a bit of history."
li "อืม เมืองนี้ก็มีความหลังอะไรอยู่พอตัวเหมือนกันจ้ะ"

# "I look down the street one last time before getting back to the task at hand."
"ฉันมองไปตามถนนอีกครั้งก่อนจะหันกลับมายังเรื่องที่สำคัญกว่า"

# hi "Shall we go in, then? I'm parched."
hi "งั้นเข้าไปกันเลยมั้ย คอแห้งจะตายแล้ว"

show hanako basic_normal_cas
with charachange

# ha "It was a long walk to get here."
ha "เดินมาไกลมาก"

show lilly basic_smile_cas
with charachange

# "Lilly gives an enthusiastic nod, the three of us lugging our bags into the house."
"ลิลลี่พยักหน้าเต็มที่ แล้วพวกเราก็ขนสัมภาระเข้าบ้านกัน"

stop ambient fadeout 1.0
$ renpy.music.set_volume(0.7, 1.0, channel="music")

scene bg hok_lounge
with locationchange

# "As soon as we set foot inside, Hanako and I start looking around, taking in every detail of where we'll be staying for the next few days."
"ทันทีที่เข้ามาในตัวบ้าน ทั้งฮานาโกะกับฉันก็มองไปรอบ ๆ สำรวจทุกซอกทุกมุมภายในบ้านที่เราจะมาอาศัยอยู่\nในช่วงสองสามวันนับจากนี้"

# "All the artifacts of another's life stopped mid-motion are around the house, such as the television guide lying beside the counter it was on, and pans in the adjoining kitchen still sitting on the stove."
"วัตถุต่าง ๆ ซึ่งบ่งบอกถึงผู้อื่นที่เคยอยู่มาถูกวางทิ้งไว้ตามจุดต่าง ๆ ในบ้าน ไม่ว่าจะเป็นนิตยสารผังรายการโทรทัศน์\nที่วางไว้ข้าง ๆ เคาน์เตอร์ที่มีโทรทัศน์ตั้งอยู่ หรือกระทะที่ตั้งอยู่บนเตาซึ่งอยู่ในห้องครัวที่อยู่ห้องถัดไป"

# "It's a strange feeling, really; as if we were stepping into Akira's life for a brief moment, before leaving in a couple of days just as we'd come. Of course, the more mundane reality is that she just hasn't cleaned up after herself that well."
"แต่ก็เป็นความรู้สึกที่ประหลาดดี รู้สึกเหมือนพวกเราได้เข้ามาสำรวจชีวิตอากิระที่เจ้าตัวเพิ่งออกไปเมื่อสองสามวันก่อน\nอยู่ครู่หนึ่งเลย ซึ่งแน่นอนว่าสิ่งที่ชวนให้หน่ายใจกว่านั้นคือเรื่องที่ว่าอากิระเองก็ไม่ได้เก็บกวาดดีขนาดนั้น"

# hi "Where should we put our bags?"
hi "ให้เก็บกระเป๋าไว้ไหนเหรอ"

show lilly basic_smileclosed_cas at twoleft
show hanako basic_normal_cas at tworight
with charaenter

# li "I'll show Hanako our bedroom. You can put yours here, if you like."
li "เดี๋ยวฉันจะพาฮานาโกะไปที่ห้องนอนก่อน เธอจะวางกระเป๋าตัวเองตรงนี้เลยก็ได้นะ"

# hi "You mean I don't have the same bedroom as you two?"
hi "หมายความว่าฉันจะไม่ได้นอนห้องเดียวกันกับพวกเธอเหรอ"

show hanako emb_blushing_cas
show lilly basic_emb_cas
with charachange

# "Hanako flowers into a full blush as Lilly takes her cheek in her hand."
"ฮานาโกะหน้าแดงฉ่าขึ้นมาทันที ส่วนลิลลี่ก็ยกฝ่ามือมาแนบแก้ม"

show lilly basic_ara_cas
show hanako emb_emb_cas
with charachange

# li "Oh my, how bold."
li "ตายจริง ช่างอาจหาญ"

# "You two…"
"นี่พวกเธอ…"

# hi "Hold on, if I'm to leave my bags here, where will I be sleeping?"
hi "เดี๋ยว ถ้าฉันเอากระเป๋าไว้ตรงนี้แล้วจะให้ไปนอนที่ไหน"

show lilly basic_weaksmile_cas
with charachange

# li "Well, seeing as we lack a guest bedroom…"
li "ก็นะ ที่นี่ไม่มีห้องนอนแขก เพราะงั้น…"

# hi "The convertible futon, huh?"
hi "นอนกับฟูกฟูตง เนอะ"

show lilly basic_concerned_cas
with charachange

# li "Sorry, Hisao."
li "ขอโทษทีนะจ๊ะฮิซาโอะ"

# "I sigh, lamenting my place on the bottom rung of sleeping location priorities."
"ฉันถอนหายใจเป็นการโอดครวญที่ตัวเองอยู่ลำดับล่างสุดในการจัดหาที่นอนให้"

# hi "I guess there's no other choice."
hi "ก็คงไม่มีทางเลือกอื่นละนะ"

hide lilly
hide hanako
with charaexit

# "Lilly leaves to show Hanako to their bedroom, so I take a small tour of my surroundings after I drop my bag on the floor."
"ลิลลี่ปลีกตัวพาฮานาโกะไปยังห้องนอน พอฉันวางกระเป๋าลงกับพื้นแล้วจึงเดินสำรวจบริเวณโดยรอบสักเล็กน้อย"

scene bg hok_kitchen
with locationchange

# "The kitchen, just like the living room, is fairly modest. The rustic nature of the wooden furnishings drives home just how far we are from civilization."
"ครัวนั้นค่อนข้างเรียบง่ายไม่ต่างอะไรกับห้องนั่งเล่น สภาพไม้เก่า ๆ ทำให้ความรู้สึกของการอยู่ไกลห่างจากอารยธรรม\nภายนอกนั้นเด่นชัดยิ่งขึ้น"

scene bg hok_lounge
with locationchange

# "Returning to the living room, I decide to try out the television until they get back. With a touch of the remote it immediately flickers to life, apparently set to a news channel."
"ฉันกลับมาที่ห้องนั่งเล่นหมายจะดูโทรทัศน์รอสองคนนั้นกลับมา ทันทีที่กดปุ่มรีโมตโทรทัศน์ก็ติดขึ้นมา โดยช่อง\nที่เปิดค้างไว้นั้นเป็นช่องข่าว"

# "Almost flopping down from exhaustion rather than sitting, I lay back and watch."
"ฉันนั่งลงจนแทบล้มตัวลงนอนด้วยความเพลีย จากนั้นจึงเอนตัวแล้วดูโทรทัศน์"

stop music fadeout 5.0
$ renpy.music.set_volume(1.0, 8.0, channel="music")

# "And watch."
"และดูโทรทัศน์"

# "And watch…"
"และดูโทรทัศน์…"

window hide

scene black
with shuteye

with Pause(4.0)

window show

# ha "Hisao…"
ha "ฮิซาโอะ…"

play ambient sfx_cicadas fadein 5.0

scene bg hok_lounge_ni
show lilly basic_smileclosed_cas at twoleft
show hanako basic_normal_cas at tworight
with openeye

# "I quickly blink to wake myself up, Lilly and Hanako having returned minus their bags."
"ฉันกะพริบตาปลุกตัวเองให้ตื่น ลิลลี่กับฮานาโกะกลับมาแล้วโดยที่ไม่มีกระเป๋าติดมืออีก"

# "From the Hokkaido night sky visible outside the windows, it looks like I drifted off to sleep. Looking to the wall-mounted clock, it's already ten."
"ดูจากท้องฟ้ายามค่ำคืนของฮกไกโดที่อยู่นอกหน้าต่างแล้ว ฉันคงเผลอหลับไป เมื่อมองนาฬิกาที่อยู่บนกำแพงก็เห็นว่า\nตอนนี้สี่ทุ่มแล้ว"

show lilly basic_weaksmile_cas
with charachange

# li "You've found the television, then."
li "เจอโทรทัศน์แล้วสินะจ๊ะ"

# hi "Yeah. It really does feel nice and homey, here."
hi "อืื้ม ที่นี่อยู่สบายดีนะ"

show lilly basic_smile_cas
with charachange

# li "I'm glad you like it."
li "ดีใจที่ชอบจ้ะ"

show lilly basic_giggle_cas
with charachange

# li "You were already out like a light when we came back after unpacking our things, so we didn't have the heart to wake you sooner."
li "ตอนที่เราเก็บของกันเสร็จแล้วกลับมาก็เห็นเธอกำลังหลับสบายอยู่เลยไม่กล้าปลุกน่ะจ้ะ"

# "Judging from her giggle, I must sound funny when I sleep. I swiftly decide not to inquire."
"หัวเราะคิกคักอย่างนี้แปลว่าตอนหลับฉันคงทำเสียงอะไรตลก ๆ แน่ ๆ ฉันตัดใจไม่ถามอะไรต่ออย่างรวดเร็ว"

show hanako emb_smile_cas
with charachange

# ha "There's some dinner waiting for you in the kitchen…"
ha "ข้าวเย็นนายอยู่ในครัวนะ…"

show hanako emb_downtimid_cas
with charachange

# "Hanako gives a deep yawn, only just remembering to cover her mouth at the last second. "
"ฮานาโกะหาวหวอด กว่าจะนึกยกมือมาป้องปากได้ก็ตอนเกือบจะงับปากไปแล้ว"

show lilly basic_weaksmile_cas
with charachange

# li "My my, are you tired?"
li "แหม ๆ เพลียเหรอจ๊ะ"

show hanako emb_timid_cas
with charachange

# ha "Ah, mm. I didn't get much sleep last night."
ha "อ๊ะ อื้ม เมื่อคืนนอนไม่ค่อยหลับเลย"

# hi "I'm pretty tired too. It was a long walk up here, and it's getting late."
hi "ฉันก็เพลีย ๆ เหมือนกัน เดินมาตั้งไกล แถมตอนนี้ก็ดึกแล้วด้วย"

show lilly basic_smileclosed_cas
with charachange

# li "If that's the case, I suppose we should retire for the night. Good night, Hisao."
li "ถ้างั้นวันนี้ก็นอนกันก่อนเถอะ ราตรีสวัสดิ์จ้ะฮิซาโอะ"

show hanako basic_smile_cas
with charachange

# ha "Good night."
ha "ราตรีสวัสดิ์"

# hi "'Night."
hi "ฝันดี"

hide hanako
hide lilly
with charaexit

# "With that, they quietly turn and walk back to their bedroom."
"แล้วทั้งสองคนก็เดินกลับห้องตัวเองไป"

# "Rubbing my eyes, I sigh. I wonder if I'll be able to get back to sleep after being woken up."
"ฉันขยี้ตาพลางถอนหายใจ ตื่นมาขนาดนี้แล้วจะหลับต่อได้มั้ยเนี่ย"

# "I suppose I'll eat something and watch some more TV quietly before going to bed."
"หาอะไรกิน ดูโทรทัศน์แบบเปิดเสียงเบา ๆ แล้วค่อยหลับดีกว่า"

stop ambient fadeout 2.0

scene black
with dissolve

#**************************************

label th_L15:

scene black
with dissolve

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_parkambience fadein 6.0

# ha "Is he still sleeping?"
ha "หลับอยู่เหรอ"

# li "I think so."
li "น่าจะนะ"

# "I'm not. I am, however, incredibly tired."
"ไม่ได้หลับ แต่ว่า เพลียมาก ๆ"

# ha "It's getting late in the morning…"
ha "นี่ก็สายแล้ว…"

# "I know that."
"รู้น่า"

# li "He likely stayed up to watch television. I could hear it from our bedroom."
li "น่าจะเพราะเอาแต่ดูโทรทัศน์ไม่ยอมนอนแน่เลย ตอนอยู่ในห้องนอนก็ได้ยินเสียงอยู่"

# "Only because I couldn't get to sleep."
"ที่ดูก็เพราะนอนไม่หลับนั่นแหละ"

# ha "Should we wake him?"
ha "ปลุกดีมั้ย"

# "Don't do that, Hanako. Please."
"อย่านะ ฮานาโกะ ขอร้อง"

# li "No, we should leave him. I doubt he'd want to be woken early if he didn't get much sleep during the night."
li "ไม่ต้อง ปล่อยให้นอนไปเถอะ ถ้านอนดึกขนาดนั้นเขาก็คงไม่ได้อยากให้ใครมาปลุกเช้า ๆ หรอก"

# "Thank you, Lilly."
"ขอบคุณนะลิลลี่"

# li "Besides, he sounds so peaceful. It would be a shame to wake him when he's like this."
li "อีกอย่าง ฟังดูหลับสบายมากเลย จะให้ปลุกตอนนี้ก็คงไม่ดี"

# "Keep a straight face, Hisao. It is nice she cares so much, though."
"อย่ายิ้มนะไอ้ฮิซาโอะ แต่ดีใจแฮะที่ใส่ใจกันขนาดนี้"

# ha "Um…"
ha "อ่า…"

# li "Hanako, could you go to the fridge and fish out what's needed to make lunch?"
li "ฮานาโกะ ไปเอาของในตู้เย็นสำหรับทำข้าวเที่ยงออกมาให้หน่อย"

# ha "All right, just the vegetables and rice?"
ha "ได้ แค่ผักกับข้าวใช่มั้ย"

# li "Mm, that should be enough. We only need something simple, as we can eat in town later."
li "อื้ม แค่นั้นแหละจ้ะ ทำอะไรง่าย ๆ กินกันก็พอ เดี๋ยวพวกเราค่อยไปกินข้าวในเมืองกันต่อ"

# "Hanako's footsteps on the carpeted floor can be heard, moving away from the living room. As they do, I feel Lilly's hand gently rest on my chest."
"เสียงฮานาโกะที่เดินไปตามพื้นปูพรมออกไปจากห้องนั่งเล่นดังตามมา ระหว่างนั้นสัมผัสจากฝ่ามือลิลลี่ก็ถูกเข้า\nกับหน้าอกฉัน"

# "It takes a titanic effort not to react, but something about her makes me think she knows I'm awake."
"ต้องกลั้นใจแทบตายกว่าจะขืนตัวให้นิ่งไว้ได้ แต่รู้สึกเหมือนลิลลี่จะรู้แล้วว่าฉันไม่ได้หลับอยู่"

# "A long silence passes."
"มีเพียงความเงียบเนิ่นนาน"

# "The only thought in my mind is of that gentle, outstretched hand laying upon my chest. After an indiscernible amount of time, Lilly withdraws her hand."
"สิ่งที่อยู่ในหัวมีเพียงฝ่ามือที่ยื่นมาแตะหน้าอกของฉันอย่างอ่อนโยน เมื่อเวลาผ่านไปนานเท่าไหร่ไม่ทราบได้ลิลลี่ก็\nถอนมือออก"

# li "Good morning, Hisao."
li "อรุณสวัสดิ์จ้ะฮิซาโอะ"

$ renpy.music.set_volume(1.0, 3.0, channel="ambient")
play music music_dreamy fadein 8.0

scene bg hok_lounge
show lilly basic_smileclosed_cas at center
with openeye

# "Conceding defeat all too easily, I prop myself up and rub my eyes."
"ฉันยอมแพ้โดยดุษณีแล้วเด้งตัวลุกขึ้นขยี้ตา"

# hi "How'd you know?"
hi "รู้ได้ไงเนี่ย"

show lilly basic_weaksmile_cas
with charachange

# li "Your breathing was off."
li "เสียงหายใจเธอมันแปลก ๆ น่ะจ้ะ"

# "While that makes sense, she couldn't have needed that long to work it out. Knowing her hearing, she likely knew before laying her hand on me."
"ถึงจะฟังดูสมเหตุสมผลดี แต่คนหูดีระดับลิลลี่คงไม่ต้องใช้เวลานานขนาดนั้นหรอก คงรู้ตั้งแต่ก่อนที่จะเอามือแตะฉัน\nแล้วด้วยซ้ำ"

show lilly basic_displeased_cas
with charachange

# li "If you want to sleep more, you should really go to bed earlier. I heard the television going long into the night."
li "ถ้าอยากพักผ่อนมาก ๆ ก็อย่านอนดึกนะจ๊ะ เมื่อคืนได้ยินเสียงโทรทัศน์เปิดอยู่นานเลย"

# hi "Sorry about that. My medications have been interfering with my sleep for a while now. Even if I'm tired I have trouble actually sleeping."
hi "ขอโทษทีนะ ช่วงนี้นอนไม่ค่อยสม่ำเสมอเพราะยาน่ะ บางทีเพลีย ๆ มาก็ยังหลับไม่ลงเลย"

show lilly basic_oops_cas
with charachange

# li "I'm… sorry for bringing it up, Hisao."
li "ขอ… โทษที่พูดถึงเรื่องนี้นะ ฮิซาโอะ"

label th_choiceL15:
menu:
    with menueffect

    # "I sigh. This is exactly the kind of thing I wish others wouldn't do."
    "ฉันถอนหายใจ นี่แหละ ฉันไม่อยากให้ใครต้องมาคิดมากด้วยเลย"

    # "Address it.":
    "คุยต่อ":
        return m1
    
    # "Wave her off.":
    "ไล่":
        return m2


label th_L15a:

# hi "Come on, you worry about me more than I do at times. It just means I have to sleep a bit longer, that's all."
hi "ไม่เอาน่า บางทีเธอยังน่าเป็นห่วงกว่าฉันด้วยซ้ำมั้ง แค่เรื่องนอน นอนเพิ่มอีกหน่อยเอาก็ได้แล้ว"

show lilly basic_reminisce_cas
with charachange

# li "But still…"
li "แต่ว่า…"

# hi "I'd say that I look absolutely fine, but I guess that wouldn't have a lot of meaning for you."
hi "ปกติก็คงบอกอะนะว่าสบายมาก แต่บอกอย่างนั้นไปเธอก็คงไม่สบายใจขึ้นใช่มั้ย"

show lilly basic_displeased_cas
with charachange

# "She gives a sigh of consternation before trailing off with an amused chuckle, giving up the point."
"ลิลลี่ถอนหายใจด้วยความกังวล ก่อนจะปิดด้วยเสียงหัวเราะคิกคักเป็นเชิงยอมแพ้"

show lilly basic_weaksmile_cas
with charachange

# li "If you say so. Please do take care of yourself, Hisao."
li "ถ้าเธอว่างั้นละก็นะ แต่ก็ดูแลตัวเองด้วยนะ ฮิซาโอะ"

# hi "Go on, Hanako could use some help."
hi "ไปช่วยฮานาโกะทำกับข้าวก่อนเถอะ"

hide lilly
with dissolve

# "She moves to protest, but reluctantly acquiesces and disappears into the kitchen, her hand running along the smooth white walls as she slowly walks."
"ลิลลี่ทำท่าจะประท้วง แต่สุดท้ายก็ยอมด้วยความอิดออดแล้วเดินหายไปในครัวอย่างช้า ๆ โดยที่มือลากไปตาม\nกำแพงเรียบสีขาว"

label th_L15b:

# hi "Hanako could… probably use some help."
hi "ไป… ช่วยฮานาโกะทำกับข้าวก่อนเถอะ"

show lilly basic_displeased_cas
with charachange

hide lilly
with dissolve

# "Lilly seems about to protest for a moment, but eventually acquiesces, nodding before leaving for the kitchen."
"ลิลลี่ทำท่าจะประท้วงอยู่ครู่หนึ่ง แต่สุดท้ายก็ยอมแล้วพยักหน้าก่อนจะเดินไปที่ครัว"

label th_L15c:

# "For a while I sit and watch television in an attempt to wake myself a little more, but it's futile. I don't have anything better to do, so I follow Lilly's lead."
"ฉันนั่งดูโทรทัศน์ให้ตื่นเต็มตาอีกสักหน่อยอยู่พักใหญ่แต่ก็ไม่เป็นผล ฉันตามลิลลี่ไปเพราะไม่มีอะไรทำอยู่แล้วด้วย"

stop ambient fadeout 5.0

scene bg hok_kitchen
with locationchange

# "As I round the corner, I see Hanako and Lilly, backs turned, quietly cutting food on the granite-colored counter."
"พอเดินพ้นหัวมุมมาก็เห็นฮานาโกะกับลิลลี่ที่หันหลังให้และกำลังซอยอะไรบางอย่างอยู่บนเคาน์เตอร์สีหินแกรนิต"

# "I am temporarily engrossed as I watch Lilly guiding the knife down carefully with a finger on the cabbage she's cutting, each slice delivered slowly but with precision."
"ฉันมองด้วยความสนใจไปยังลิลลี่ที่ใช้นิ้วนำทางมีดไปตามผิวกะหล่ำปลีที่เธอกำลังซอยอยู่ การซอยแต่ละครั้งนั้น\nเป็นไปอย่างช้า ๆ ทว่าแม่นยำ"

# "She seems a little slow, but considering that she can't see what she's doing it's a small wonder she can cook at all, let alone for both her and Hanako."
"ถึงจะช้านิดหน่อย แต่การที่เธอทำอาหารได้ทั้งที่มองไม่เห็นนั้นก็เป็นอะไรที่ชวนให้ทึ่งอยู่เหมือนกัน แล้วยิ่งต้องทำให้\nทั้งตัวเองกับฮานาโกะอีก"

# hi "Hi Hanako, Lilly. Want any help?"
hi "ไง ฮานาโกะ ลิลลี่ มีอะไรให้ช่วยมั้ย"

show lilly back_surprise_cas at twoleft
show hanako basic_normal_cas at tworight
with charaenter

stop music fadeout 0.3

# $ doublespeak(li, ha, "Is that Hisa— ah!",  "Oh, 'morning Hisao.")
$ doublespeak(li, ha, "ฮิซาโอะใช่มั้— อ๊ะ!",  "อ๊ะ รุณสวัสดิ์ ฮิซาโอะ")

show lilly basic_oops_cas
with charachange

# "Lilly jerks back in surprise before turning around, her yelp immediately drawing Hanako and me to her side."
"ลิลลี่สะดุ้งก่อนจะหันมา เสียงร้องของเธอทำให้ทั้งฉันกับฮานาโกะพุ่งเข้าหาทันที"

# hi "What's… ah."
hi "มีอะไร… อ๊ะ"

# "A small trickle of scarlet falls downward from her pale fingertip, the knife having cut just deep enough to draw blood."
"ปลายนิ้วขาวของเธอมีหยดของเหลวสีชาดอยู่ มีดนั้นบาดจนได้เลือดพอดิบพอดี"

# "With the television's sound masking my footsteps, she must not have noticed me coming. To compensate for having to use touch to guide everything she does during cooking, she must need to pay extra attention."
"เสียงโทรทัศน์คงดังจนไม่ได้ยินเสียงฝีเท้าฉันแน่ ๆ แล้วยิ่งต้องจดจ่อกับการทำอาหารที่ต้องคอยใช้มือในการสัมผัส\nเพื่อนำทางอะไร ๆ อีก"

show hanako defarms_shock_cas
with charachange

play music music_dreamy fadein 8.0

# ha "Lilly!"
ha "ลิลลี่!"

show lilly basic_weaksmile_cas
with charachange

# li "Don't worry, Hanako. It's just a small wound."
li "ไม่ต้องห่วง ฮานาโกะ แผลแค่นี้เอง"

# hi "You should still get a band-aid on it, at least until it stops bleeding. First aid stuff would be in the bathroom, right?"
hi "แต่หาปลาสเตอร์ปิดแผลมาติดหน่อยก็ดีนะ ให้เลือดหยุดไหลก็ยังดี กล่องปฐมพยาบาลอยู่ในห้องน้ำใช่มั้ย"

show lilly basic_sleepy_cas
with charachange

# li "I think so. Will you be okay here, Hanako?"
li "น่าจะนะ ฮานาโกะ เธอทำต่อได้ใช่มั้ย"

show hanako cover_worry_cas
with charachange

# "I frown at how little heed she's paying to herself as Hanako gives a quick, almost automatic, nod."
"ฉันขมวดคิ้วที่ลิลลี่แทบไม่ได้สนใจตัวเองเลย ฮานาโกะพยักหน้าตอบในทันทีโดยแทบจะอัตโนมัติ"

show hanako basic_worry_cas
with charachange

# ha "It's fine, I can keep making lunch."
ha "ไม่เป็นไร ฉันทำข้าวเที่ยงต่อเองได้"

scene bg hok_bath
with locationskip

# "An awkward silence reigns as I set the bottle of antiseptic and box of band-aids on the side of the sink, Lilly's finger held out for me to treat."
"มีเพียงความเงียบอันน่าอึดอัดระหว่างที่ฉันหยิบขวดยาฆ่าเชื้อกับปลาสเตอร์ปิดแผลออกมาวางตรงขอบอ่างล้างหน้า\nส่วนลิลลี่ยื่นนิ้วออกมารอ"

# "The lid of the bottle comes off with a minimum of resistance, and the small ball of cotton I soak in the liquid stains a pale green."
"ฝาขวดนั้นเปิดได้ไม่ยากนัก ก้อนสำลีเล็ก ๆ ที่จุ่มเข้าไปถูกย้อมด้วยสีเขียวจาง ๆ"

# hi "Okay, hold still. This'll probably hurt a bit."
hi "โอเค อยู่นิ่ง ๆ ไว้ อาจจะเจ็บนิดหน่อยนะ"

show lilly basic_weaksmile_cas_close at center
with charaenter

# "She gives a small nod as I take hold of her hand to steady it. With all the tenderness I can muster, I gently bring the dampened wad to the small red line."
"ลิลลี่พยักหน้าน้อย ๆ ฉันจับมือลิลลี่ไว้ให้อยู่นิ่ง ๆ แล้วค่อย ๆ ถูก้อนสำลีชุบยาไปตามรอยสีแดงด้วยความเบามือ\nอย่างยิ่งยวดเท่าที่จะทำได้"

show lilly basic_oops_cas_close
with charachange

# li "Ah!"
li "อ๊ะ!"

# hi "What? I've barely touched it."
hi "ฮะ? ยังแทบไม่ได้แตะเลยนะ"

show lilly basic_reminisce_cas_close
with charachange

# li "Sorry…"
li "ขอโทษนะ…"

# "I give a sigh, both at her reaction and to settle my own nerves. Her pain tolerance is startlingly low."
"ฉันถอนหายใจให้กับปฏิกิริยาของลิลลี่ และเพื่อสงบใจตัวเองด้วย เป็นคนเจ็บง่ายจนน่าตกใจเลยแฮะ"

# hi "I would tell you to man up, but I can't really do that."
hi "ก็อยากบอกให้แข็งใจไว้หน่อยอยู่หรอก แต่จะบอกงั้นก็คงไม่ได้เนอะ"

show lilly basic_weaksmile_cas_close
with charachange

# "As she gives a small giggle, I take advantage of her momentary distraction and gently press the cotton against her finger a few times. Thankfully, it's enough to do the job."
"ลิลลี่หัวเราะคิกคัก พอสบโอกาสที่เธอสนใจอย่างอื่นอยู่ครู่หนึ่งฉันจึงกดสำลีเข้ากับนิ้วอีกสองสามครั้ง โชคดี\nที่การฆ่าเชื้อจบลงเพียงเท่านั้น"

# "We both settle somewhat as I bring the band-aid over the tip of her finger, covering the wound while making sure not to get it stuck to her fingernail."
"ฉันเอาปลาสเตอร์ปิดแผลมาติดตรงแผลที่ปลายนิ้วลิลลี่โดยคอยระวังไม่ให้ติดกับเล็บ ระหว่างนั้นพวกเราก็เริ่มสงบใจลง\nกันได้แล้ว"

# hi "There, finished. You can move now."
hi "เอ้า เสร็จแล้ว ขยับได้"

# "Taking her hand from mine, she gently clasps it in the other."
"ลิลลี่ถอนมือออกแล้วใช้มืออีกข้างกุมมือข้างนั้นไว้"

show lilly basic_smileclosed_cas_close
with charachange

# li "Thank you."
li "ขอบคุณนะ"

# hi "It's no problem. It's the least I can do after causing you to hurt yourself, after all."
hi "เรื่องแค่นี้เอง ยังไงเสียฉันก็ต้องรับผิดชอบในฐานที่ทำให้เธอเจ็บตัวนี่นา"

show lilly basic_emb_cas_close
with charachange

# "She lowers her head slightly at the apology, absentmindedly rubbing her hand in what seems to be embarrassment."
"เธอก้มหัวเล็กน้อยเป็นการขอโทษพลางถูมือตัวเองแบบเหม่อ ๆ คล้ายกำลังอาย"

show lilly basic_weaksmile_cas_close
with charachange

# li "I really don't mind."
li "ฉันไม่ถือหรอก"

stop music fadeout 5.0

# "Her answer doesn't seem to make much sense, given that what happened is pretty clearly my fault."
"คำตอบของลิลลี่ฟังดููไม่ค่อยสมเหตุสมผลเท่าไหร่ เพราะสิ่งที่เกิดขึ้นนั้นเป็นความผิดของฉันจริง ๆ"

# "I can't help grimacing at her, despite the fact that her dainty smile still holds. She must not like being reminded of the limitations her lack of sight imposes on her."
"ฉันอดทำหน้าเบ้ไม่ได้แม้ลิลลี่กำลังยิ้มบาง ๆ อยู่ ลิลลี่คงไม่ชอบให้อะไรมาทำให้ต้องคิดถึงข้อจำกัดทางการมองเห็น\nของตัวเอง"

# "It's something I can't possibly fault her for. I've fallen prey to the same kind of feelings before, despite my condition not being nearly as ubiquitous in my life."
"ซึ่งฉันเองก็ว่าลิลลี่ไม่ได้หรอก เพราะฉันเองก็เคยรู้สึกอย่างนั้นเหมือนกัน ถึงอาการของฉันจะไม่ได้มีผลต่อชีวิต\nประจำวันหนักมากขนาดนั้นก็เถอะ"

# "Neither of us any the happier, we head back to the various smells of cooking food coming from the kitchen."
"เราสองคนไม่ได้ร่าเริงขึ้นเท่าไหร่ พวกเราเดินไปยังครัวที่อบอวลไปด้วยกลิ่นมากมายจากอาหาร"

scene bg hok_lounge
with shorttimeskip

play music music_another fadein 8.0

# "I lay out the plates of food, steam slowly rising from the well-cooked rice and curry dishes, while Hanako lays out the cutlery."
"ฉันจัดวางจานที่มีข้าวแกงกะหรี่สีสวยซึ่งมีควันร้อน ๆ ลอยเอื่อยออกมา ส่วนฮานาโกะคอยจัดแจงอุปกรณ์การกินต่าง ๆ"

# "Knife one side, fork on the other. Western. How perfectly fitting for someone like Lilly."
"ฝั่งหนึ่งมีมีด อีกฝั่งเป็นส้อม เป็นแบบตะวันตกที่ช่างเหมาะสมกับลิลลี่เป็นอย่างมาก"

# "As we take our seats, taking careful heed of the dark red tablecloth hanging below our knees, Lilly emerges from the kitchen."
"พวกเรานั่งลงพลางระวังผ้าปูโต๊ะสีแดงเข้มที่ยาวจนมาพาดกับหัวเข่า จากนั้นลิลลี่ก็เดินออกมาจากครัว"

# "In her hands are three glasses and… a bottle of wine?"
"ในมือลิลลี่มีแก้วสามใบและ… ไวน์หนึ่งขวด?"

# "As I recall our previous run-in with that devilish elixir, I hide my face in my palm."
"เมื่อย้อนนึกถึงความเดิมที่ได้ประสบกับน้ำยาปีศาจนั้นฉันก็เอามือลูบหน้า"

# hi "Alcohol? Seriously?"
hi "เหล้า? เอาจริงดิ"

show lilly basic_cheerful_cas at center
with charaenter

# "She pauses as she reaches the table, a playful grin perched on her face."
"ลิลลี่ชะงักไปตอนที่กำลังเดินมาที่โต๊ะ เธอฉีกยิ้มซุกซนออกมา"

show lilly basic_giggle_cas
with charachange

# li "Akira specifically gave permission to take a bottle from her collection."
li "พี่อุตส่าห์บอกเลยนะว่าให้หยิบมาได้หนึ่งขวดจากคลังที่มีอยู่น่ะ"

# "Not only does she give alcohol to minors, she even lets them pilfer their own? The perfect model of a responsible adult Akira is not."
"ให้เหล้ากับผู้เยาว์ไม่พอ ยังปล่อยให้จิ๊กได้ตามใจชอบอีก ถ้าอยากโตไปเป็นผู้ใหญ่ที่มีความรับผิดชอบละก็ต้องไม่เอา\nอากิระเป็นเยี่ยงอย่างเป็นอันขาด"

# "More to the point, though, is that this is hardly a meal deserving of alcohol. I'm starting to think Lilly's the type to easily become hooked on things."
"แต่ประเด็นจริง ๆ คือ กับข้าวตอนนี้ไม่ใช่อะไรที่จะต้องกินกับไวน์เลย นี่ลิลลี่เป็นพวกที่แบบถ้าลองอะไรแล้วจะติดใจ\nเอาง่าย ๆ เลยหรือเปล่าเนี่ย"

# hi "That's not really the problem. I don't really have any qualms with it, but didn't you have a bad experience with it last time?"
hi "ปัญหาไม่ได้อยู่ตรงนั้น ฉันไม่ได้อะไรหรอก แต่ล่าสุดที่เธอดื่มก็แทบเอาตัวไม่รอดเลยไม่ใช่เหรอ"

show lilly basic_smileclosed_cas
with charachange

# li "Last time was likely due to drinking too much, so a single glass shouldn't prove a problem."
li "ครั้งนั้นน่าจะเพราะดื่มเยอะไปมากกว่า เพราะงั้นแค่แก้วเดียวไม่เป็นไรหรอก"

show lilly basic_smile_cas
with charachange

# li "Think of it as a learning experience."
li "คิดเสียว่าครั้งนั้นเป็นประสบการณ์สอนใจไงจ๊ะ"

# hi "I can't recall many learning experiences that made me feel rotten before putting me to sleep, but I'll take your word for it."
hi "รู้สึกว่าจะไม่ค่อยมีประสบการณ์สอนใจอันไหนที่ทำให้ฉันต้องรู้สึกเหมือนจะตายให้ได้เวลาจะนอนนะ แต่จะเชื่อเธอ\nก็แล้วกัน"

show lilly basic_smileclosed_cas
with charachange

# "She dips an uninjured finger inside to feel the liquid level, tip against the bottom as the liquid rises up."
"ลิลลี่ใช้นิ้วที่ไม่เป็นแผลแตะก้นแก้วเพื่อวัดระดับแล้วเทจนของเหลวในแก้วสูงขึ้นเรื่อย ๆ"

# "The white of her finger almost seems to glow as the sunlight hits it, the delicate outline blurred and refracted by the glass."
"นิ้วขาวของเธอยามต้องแสงแดดนั้นดูคล้ายว่าเรืองแสงอยู่เบื้องหลังผิวแก้วที่สะท้อนแสงขาวอ่อนโยน"

# "Her fingers are definitely longer than mine, the kind I'd think more suited to a pianist than a teacher. She'd likely have done well if she'd learned how to play."
"นิ้วลิลลี่นั้นยาวกว่านิ้วฉันอย่างเห็นได้ฉัน เป็นนิ้วที่รู้สึกว่าน่าจะเหมาะกับการเป็นนักเปียโนมากกว่าการเป็นครู"

hide lilly
with charaexit

# "We quickly dig into our meal, forks and knives clattering against plates."
"พวกเรากินข้าวกันอย่างรวดเร็วโดยมีเสียงส้อมกับมีดกระทบกับจานไปมา"

# "None of us are particularly eager to speak while eating, Lilly altogether too reserved for such a thing, Hanako probably too shy to start conversation, and I too busy savoring the food."
"ไม่มีใครอยากพูดอะไรตอนกินข้าวสักเท่าไหร่ ลิลลี่เองก็เป็นคนเรียบร้อยเกินกว่าที่จะทำอะไรอย่างนั้น ส่วนฮานาโกะ\nก็คงไม่กล้าพอที่จะเปิดบทสนทนา และฉันเองก็ง่วนอยู่กับการเขมือบอาหารอยู่"

# "Such a pedestrian activity, eating together at a table. It seems so utterly normal, yet it makes me realize how long it's been since I've done something like this."
"การกินข้าวด้วยกันเช่นนี้นั้นก็เป็นเพียงกิจกรรมที่ธรรมดาสามัญอย่างถึงที่สุด ทว่าก็ทำให้ฉันได้ย้อนคิดว่าพวกเราเอง\nก็ไม่ได้กินข้าวด้วยกันอย่างนี้นานเพียงใดแล้ว"

# "Just the three of us, sitting around a single table eating as if we were a malformed family. Maybe this trip, as far away from everything as we are, was worth it."
"เราสามคนนั่งล้อมวงกินข้าวด้วยกันราวกับเป็นครอบครัวพิลึกพิลั่น บางที การมาเที่ยวครั้งนี้ซึ่งไกลห่างจากทุกสิ่งอย่าง\nในชีวิตของพวกเรานั้นอาจไม่ได้ไร้ความหมายเสียทีเดียว"

with shorttimeskip

# "It takes quite a long time, but eventually we all finish our surprisingly filling meal. The wine, thankfully, has little effect given we've only had a glass or two each."
"เมื่อเวลาผ่านไปนานพอสมควรพวกเราก็กินข้าวกันจนอิ่มเหลือเชื่อ ยังดีที่ไวน์ที่เราดื่มกันไปคนละสองแก้วนั้นไม่ได้มีผล\nอะไรมากนัก"

# "I slump back into the seat, rubbing my stomach contentedly."
"ฉันเอนตัวพิงพนักเก้าอี้ลูบท้องด้วยความอิ่มหนำ"

# hi "I'm stuffed."
hi "อิ่มจังเลย"

show lilly basic_smileclosed_cas at twoleft
show hanako basic_smile_cas at tworight
with charaenter

# "Lilly pats her mouth with a napkin. Twice, only twice, and with evenly timed intervals in between. It's hard to tell sometimes whether how she acts is a well-trained routine or a well-rehearsed act."
"ลิลลี่ใช้ผ้าเช็ดปากแตะ ๆ ปาก สองครั้ง สองครั้งจริง ๆ โดยที่แต่ละครั้งมีการเว้นช่วงเวลาเท่ากันด้วย บางทีก็ดูไม่ออก\nเหมือนกันว่าการกระทำของลิลลี่แต่ละอย่างนั้นเป็นกิจวัตรที่ฝึกมาอย่างดีหรือการแสดงที่ซ้อมมาอย่างหนักกันแน่"

show lilly basic_satisfied_cas
with charachange

# li "I think I must be as well. Did you like it, Hanako?"
li "ฉันก็ด้วยจ้ะ อร่อยมั้ยฮานาโกะ"

show hanako cover_bashful_cas
with charachange

# ha "Mm, it was nice."
ha "อื้ม อร่อย"

show lilly basic_smileclosed_cas
with charachange

# li "Now that we're well fed, shall we be off?"
li "ท้องอิ่มกันแล้ว ทีนี้ก็ไปกันเลยมั้ย"

# hi "Off? Where?"
hi "ไป? ไปไหน"

show lilly basic_weaksmile_cas
with charachange

# li "Ah, you weren't privy to the discussion between Hanako and me earlier."
li "อ้อ เธอไม่ได้อยู่เป็นวงในด้วยตอนที่ฉันกับฮานาโกะคุยกันนี่นา"

# "I get the impression that she's having a subtle dig at my sleeping in."
"รู้สึกเหมือนกำลังล้อเรื่องที่ฉันตื่นสายอยู่ยังไงไม่รู้"

show hanako basic_bashful_cas
with charachange

# ha "We'll be going into the town nearby."
ha "เดี๋ยวเราจะออกไปเมืองที่อยู่แถวนี้กัน"

# "I guess I should have expected two girls to take a holiday as an excuse to go shopping, no matter where on the planet they may be."
"จริง ๆ ก็ควรจะเดาได้อยู่แล้วอะนะว่าการที่ผู้หญิงมาเที่ยวในวันหยุดก็คือการหาข้ออ้างที่จะได้ไปเดินซื้อของ ไม่ว่าจะเป็น\nการไปเที่ยวที่หลืบไหนของโลกก็ช่าง"

# "I am interested to see more around the north though, so this can only be a good thing."
"แต่ฉันก็อยากเห็นบรรยากาศทางภาคเหนือด้วยเหมือนกัน ไปด้วยกันก็ดี"

# hi "Sounds good. How long's the walk in, then?"
hi "ก็ได้นะ แล้วเดินไปไกลมากมั้ย"

show lilly basic_smile_cas
with charachange

# li "It's supposed be around a mile to a mile and a half."
li "ประมาณกิโลเมตรกว่า ๆ สองกิโลเมตรจ้ะ"

stop music fadeout 4.0

# hi "Nearby, huh? Great."
hi "อยู่แถวนี้เหรอ เยี่ยม"

# "Just great."
"เยี่ยมจริง ๆ"

scene bg hok_road at bgright
with shorttimeskip

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_parkambience fadein 6.0
play music music_soothing fadein 0.5

# "As we climb up the path surrounded by trees and undergrowth, I watch Lilly and Hanako walking ahead."
"ฉันมองลิลลี่กับฮานาโกะที่เดินนำไประหว่างที่พวกเราเดินไปตามเส้นทางที่โอบล้อมไปด้วยต้นไม้และพืชพื้นป่า"

# "The slight breeze all but whisks away the sound of Lilly's cane gently tapping on the ground. I notice that Lilly's since removed the bandaid now that the bleeding of her finger has stopped."
"แม้มีลมอ่อน ๆ ที่โชยมา เสียงเคาะจากไม้เท้าของลิลลี่ยังคงดังพอที่จะให้ได้ยิน ฉันเพิ่งเห็นว่าลิลลี่แกะปลาสเตอร์ออก\nและเลือดก็หยุดไหลแล้วด้วย"

# "A deep, lung-filling breath of the fresh country air makes me wish all the harder that the air around home had been quite so clean."
"พอได้สูดอากาศอันสดชื่นจากชนบทให้เต็มปอดแล้วก็นึกอยากให้อากาศที่ชวนให้อึดอัดแถวบ้านนั้นสะอาดอย่างนี้บ้าง"

# "It can't have even been half a mile, but I'm already working up a sweat. It isn't a pleasantly cool day, though, so I shouldn't be too hard on myself for it."
"ยังเดินมาไม่ถึงหนึ่งกิโลเมตรเหงื่อก็เริ่มออกแล้ว แต่วันนี้ก็อากาศเย็นสบายดี อย่าไปคิดมากอะไรกับร่างกายตัวเองเลย"

# hi "Hey Lilly, how well do you know this town, anyway?"
hi "นี่ ลิลลี่ เธอรู้จักเมืองนี้ดีมากมั้ย"

show lilly back_smileclosed_cas at center
show lillyprop back_cane
with charaenter

# li "Since I spent quite a few of my vacations here up until I entered Yamaku, I'd say I know it fairly well. We used to drive there once a weekend then."
li "ก่อนหน้าที่จะได้ย้ายมาอยู่ที่ยามากุฉันก็พอจะได้มาเที่ยวที่นี่อยู่บ้าง เพราะงั้นก็รู้จักดีพอสมควรเลยล่ะจ้ะ ช่วงนั้น\nเราก็จะนั่งรถไปเที่ยวกันสัปดาห์ละหน"

# "How I wish Akira was here to drive us now."
"อยากให้อากิระมาอยู่ขับรถให้ตอนนี้เลยจริง ๆ"

# "I quickly take a moment to rub my hands a couple of times, staving off the oddly cold feeling in them."
"ฉันลูบหน้าตัวเองเร็ว ๆ สองสามครั้งเพื่อไม่ให้หน้ารู้สึกเย็นแบบแปลก ๆ"

# hi "Did you like it up here?"
hi "เธอชอบที่นี่มั้ย"

show lilly cane_weaksmile_cas
hide lillyprop
with charachange

# li "I'd say it was nice during winter, but as you can work out, summers get a little too hot for comfort. It's nice and quiet, at least."
li "ช่วงหน้าหนาวนี่ดีมากเลยจ้ะ แต่เธอน่าจะพอเดาได้ว่าถ้าหน้าร้อนแล้วอาจจะร้อนไปหน่อย แต่อย่างน้อยที่นี่ก็เงียบดีจ้ะ"

# li "My family's real house is quite far south. When they left Japan, my parents gave it to Akira and me. Only Akira lives there now, after my moving into Yamaku."
li "บ้านจริง ๆ ของครอบครัวฉันอยู่ทางใต้นู่นเลย ตอนที่พวกท่านย้ายออกไปจากญี่ปุ่นก็ยกบ้านหลังนั้นให้พี่กับฉัน\nแต่ตอนนี้ก็เหลือแต่พี่ที่อยู่ที่นั่นแล้วเพราะฉันย้ายมาอยู่ที่ยามากุแทน"

# hi "Well, quiet certainly describes this place."
hi "อืม ก็เงียบอย่างเธอว่าจริงละนะ"

# "Though lonely is how I'd put it."
"แต่ถ้าเป็นฉันก็จะใช้คำว่าโดดเดี่ยว"

# "Other than the prophesied small town, there isn't another soul for miles around. Coming from a home nestled deep within the big city, it's certainly different."
"นอกจากเมืองเล็ก ๆ ที่ว่านั้นแล้ว ในละแวกหนึ่งกิโลเมตรกว่า ๆ นี้นั้นไม่มีใครอยู่เลย สำหรับฉันซึ่งบ้านอยู่ใจกลาง\nเมืองใหญ่แล้วนับว่าเป็นอะไรที่แปลกใหม่มาก"

# "I think that if I'd not come to Yamaku, staying out in the country like this would be too much of a change to get used to."
"ถ้าฉันไม่ได้ย้ายมาอยู่ที่ยามากุ การอยู่ที่ที่อยู่นอกเมืองอย่างนี้คงเป็นการเปลี่ยนแปลงที่หนักหนาเกินกว่าที่ฉัน\nจะทำตัวให้ชินได้"

# "After getting accustomed to the school's isolation, though, the idea of living in a place such as this has become almost inviting. To be somewhere away from the hustle and bustle of the metropolitan centers."
"แต่หลังจากที่ฉันชินกับความสันโดษที่โรงเรียนแล้วก็ชักอยากอาศัยอยู่ในสถานที่เช่นนี้ขึ้นมา อยู่ให้ห่างจาก\nความรีบร้อนวุ่นวายของใจกลางมหานคร"

show lilly cane_smile_cas
with charachange

# li "So Hisao, have you been to Hokkaido before?"
li "จะว่าไป ฮิซาโอะ เธอเคยมาฮกไกโดมั้ย"

# hi "Nah. I used to live down south, and we never had any field trips or holidays up this far."
hi "ไม่อะ ฉันอยู่ทางใต้นู่น แล้วก็ไม่เคยได้มาทัศนศึกษาหรือมาเที่ยวไกลขนาดนี้เลย"

show lilly cane_cheerful_cas
with charachange

# li "Well, it's a new experience for you then."
li "งั้นก็แปลว่าเป็นครั้งแรกของเธอสินะจ๊ะ"

# hi "Yeah, it is. I'm surprised at how nice it feels here."
hi "อื้ม ครั้งแรกเลย ทึ่งเหมือนกันนะที่ดูจะอยู่สบายขนาดนี้"

# hi "How about you, Hanako?"
hi "แล้วเธอล่ะฮานาโกะ"

show lilly cane_cheerful_cas at twoleft
show bg hok_road at center
with charamove

show hanako emb_smile_cas at tworight
with charaenter

# "She shakes her head from side to side."
"ฮานาโกะสั่นหัวไปมา"

show hanako basic_bashful_cas
with charachange

# ha "It's my first time too."
ha "ฉันก็เพิ่งมาเป็นครั้งแรกเหมือนกัน"

# "As we continue walking, I begin to feel pins and needles in my legs. It's a little disturbing, given there's no reason for it to be happening."
"ระหว่างเดินฉันก็รู้สึกเหน็บชาขึ้นมาที่ขา อยู่ ๆ ก็เป็นอย่างนี้แล้วชักใจคอไม่ดีเลยแฮะ"

stop ambient fadeout 9.0
stop music fadeout 4.0

# hi "Could you two hold on a moment? I just need to…"
hi "เธอสองคนรอเดี๋ยวก่อนได้มั้ย ขอฉัน…"

show lilly cane_surprised_cas
with charachange

# li "Is anything wrong?"
li "มีอะไรหรือเปล่า"

# hi "Nah, I've just got pins and needles in…"
hi "นิดหน่อย พอดีเหน็บกิ…"

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

with Pause(0.05)

play sound sfx_heartstop
show heartattack alpha 
with Dissolve (0.1)

show heartattack residual
with Dissolve (0.8)

play music music_tragic fadein 0.5

window show

# "My vocal cords suddenly become taut as my chest tightens instantaneously. I quickly pull my upper arm over it, trying to quell the shot of pain spreading throughout my entire body."
"จู่ ๆ เส้นเสียงของฉันก็หดเกร็งขึ้นมาพร้อม ๆ กับอาการแน่นหน้าอก ฉันรีบยกแขนท่อนบนขึ้นมากดหวังบรรเทา\nอาการปวดที่แผ่ไปทั่วร่าง"

show lilly cane_reminisce_cas
show hanako defarms_strain_cas
with charachange

# li "Hisao?"
li "ฮิซาโอะ?"

# "Lilly's face is only mildly concerned, not knowing the sight which Hanako's recoiling from."
"ลิลลี่ทำหน้าเป็นกังวลเล็กน้อยเพราะไม่ได้รับรู้สิ่งที่ฮานาโกะเห็นจนผวาไป"

# hi "I'm fine, I'm… fine. Just… tired…"
hi "ไม่เป็นไร ฉัน… ยังไหว แค่… เหนื่อย…"

# "I remove my arm from my chest and force myself to begin walking again. It's just a minor heart flutter, so it'll pass like the others."
"ฉันผละแขนออกจากหน้าอกแล้วแข็งใจเดินต่อ แค่หัวใจเต้นผิดจังหวะเล็กน้อยเหมือนคราวก่อน ๆ แหละ เดี๋ยวก็หาย"

play sound sfx_heartslow

show heartattack alpha 
with Dissolve (0.1)

show heartattack residual
with Dissolve (0.8)

# "It only takes a couple of steps before my body violently revolts against me, my legs suddenly beginning to give way underneath me and all tension in my knees seeming to evaporate."
"แต่ก้าวขาไปได้อีกสองก้าวร่างกายก็ออกอาการหนัก จู่ ๆ ขาก็หมดแรง และแรงที่หยัดเข่าไว้ก็คล้ายอันตรธานสิ้น"

scene bg hok_road:
    xalign 0.5 yalign 0.52 rotate 0 zoom 1.0
    linear 0.1 rotate -6 zoom 1.2
show lilly cane_reminisce_cas:
    xanchor 0.5 xpos 0.3 yalign 0.52 rotate 0 zoom 1.0
    linear 0.1 xpos 0.25 rotate -6 zoom 1.2
show hanako defarms_strain_cas:
    xanchor 0.5 xpos 0.7 yalign 0.52 rotate 0 zoom 1.0
    linear 0.1 xpos 0.75 rotate -6 zoom 1.2
show heartattack residual
play sound sfx_pillow
with vpunch

# "Before I can react they uselessly give way under my weight, leaving me only just enough time to brace myself and fall onto all fours."
"กว่าจะรู้ตัวอีกทีเข่าฉันก็เหลวเป๋วจนร่างทรุด ฉันได้แต่ตั้งท่ารอยันแขนตอนล้มเท่านั้น"

# hi "Ah, damn…"
hi "อึก ให้ตาย…"

show hanako defarms_shock_cas
with charachange

# ha "Hisa… AAAAH!"
ha "ฮิซา… กรี๊ดดด!!"

# "As I look up to her I realize my face is still taut with pain, only adding that much more to her worrying."
"พอเงยหน้าขึ้นมองก็ถึงรู้ตัวว่าตอนนี้ฉันหน้าเบ้ไปหมดด้วยความเจ็บปวด ซึ่งยิ่งทำให้ฮานาโกะพะวงหนักไปอีก"

show lilly cane_oops_cas
with charachange

# li "Hisao!? Hanako, tell me what's going on!"
li "ฮิซาโอะ!? ฮานาโกะ เกิดอะไรขึ้น บอกมา!"

# li "Hanako, tell me!"
li "ฮานาโกะ บอกมาสิ!"

show hanako def_strain_cas_close
with characlose

# "Hanako quickly moves to my side as Lilly almost panics, having little clue as to exactly how bad a condition I'm in. While she stands there petrified, I lower my face and take a deep breath."
"ฮานาโกะเข้ามารับตัวฉันอย่างรวดเร็ว ส่วนลิลลี่นั้นเริ่มแตกตื่นแล้วเพราะไม่รู้ว่าฉันเป็นอะไรกันแน่ ระหว่างที่ลิลลี่\nยืนค้างอยู่ตรงนั้นฉันก็ก้มหน้าแล้วสูดหายใจลึก ๆ"

scene black
show heartattack alpha
with shuteyefast

# "I come to a realization that makes me endlessly irritated with my stupid self. With all the excitement of my new surroundings, I'd entirely neglected to take my medications last night or even this morning."
"พอนึกอะไรบางอย่างได้ฉันก็ได้แต่หงุดหงิดกับความโง่ของตัวเอง มัวแต่ตื่นเต้นกับสถานที่ใหม่จนลืมกินยาของเมื่อคืน\nกับเช้านี้ไปเสียได้"

stop music fadeout 9.0

hide heartattack
with Dissolve(3.0)

# "Taking another breath, the acute pain in my chest begins to die down as suddenly as it had arrived."
"พอสูดหายใจเข้าอีกครั้งอาการปวดหนึบที่อยู่ตรงหน้าอกนั้นก็หายไปอย่างรวดเร็วไม่ต่างกับตอนเกิด"

# "Thank God. Thank God. Thank God, thank God, thank God."
"รอดแล้ว รอดแล้ว รอดแล้ว รอดแล้ว รอดแล้ว"

play ambient sfx_parkambience fadein 6.0

scene bg hok_road
show lilly cane_oops_cas at twoleft
show hanako def_strain_cas_close at tworight
with openeye

# "As it does, I become acutely aware of the sweat by now pouring off my face and the two scared girls around me."
"พอหายปวดแล้วก็รู้สึกถึงเหงื่อที่ท่วมหน้าอยู่ ทั้งสองสาวที่อยู่ด้วยกันนั้นผวาไปแล้ว"

show lilly cane_reminisce_cas
with charachange

# li "Hisao!"
li "ฮิซาโอะ!"

# hi "I'm fine, Lilly. I'm… fine."
hi "ไม่เป็นไรแล้ว ลิลลี่ ไม่… เป็นไรแล้ว"

show hanako defarms_strain_cas_close
play sound sfx_impact
with vpunch

# "I screw up my brow in an effort to lever myself up, Hanako's arms quickly moving to catch me if I fall as I stumble a bit before regaining my balance."
"ฉันขมวดคิ้วเรียกกำลังเพื่อหยัดตัวเองลุกขึ้นยืน ฮานาโกะรีบเข้ามาประคองไม่ให้ล้มอีกเพราะฉันยังมีอาการเซ ๆ อยู่\n จากนั้นฉันก็กลับมายืนได้ตามปกติ"

# "I look to Lilly and Hanako, worry written on both their faces. I feel awful. Utterly awful."
"ฉันมองไปทางลิลลี่กับฮานาโกะที่ต่างมีสีหน้าว่าเป็นห่วง รู้สึกแย่ชะมัด แย่มาก ๆ"

show lilly cane_sad_cas
with charachange

# li "I think we should go back."
li "กลับกันก่อนดีกว่ามั้ย"

# hi "I…"
hi "ฉัน…"

# "Realizing the futility of protesting, I look away in frustration."
"ฉันเบือนหน้าหนีด้วยความหัวเสียเมื่อนึกได้ว่าต่อต้านไปก็เท่านั้น"

# hi "Fine."
hi "ก็ได้"

stop ambient fadeout 2.0

$ suppress_window_after_timeskip = True

scene black
with dissolve

#**************************************

label th_L16:

window hide None

scene black
with dissolve

scene bg hok_lounge_ss
with openeye

window show

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_cicadas fadein 2.0

# "I open my eyes groggily, completely bereft of energy."
"ฉันลืมตาขึ้นมาพร้อมอาการครั่นเนื้อครั่นตัวหมดเรี่ยวแรง"

# "For a while, I simply lie down lifelessly, staring at the ceiling as I review the events of the morning in an attempt to organize my thoughts."
"ฉันนอนแบ็งจ้องเพดานอยู่ครู่หนึ่งพลางนึกทบทวนถึงเหตุการณ์เมื่อเช้าเป็นการจัดระเบียบความคิด"

# "We went to walk to town. My heart nearly gave way. We came back. I took my pills. I slept."
"เราเดินไปเมือง ฉันเกือบหัวใจวาย เรากลับมา ฉันกินยา ฉันหลับ"

# "I can only remember each period of time as a snapshot, but the timeline is clear enough. The memory of the girls' faces as I struggled to stand is an unpleasant one, stinging my feelings harshly."
"ฉันจำภาพเหตุการณ์ได้เป็นช่วง ๆ เท่านั้น แต่ยังจำลำดับได้ชัดเจนดีอยู่ ภาพสีหน้าของทั้งสองคนที่ได้เห็นสภาพฉัน\nที่แทบลุกยืนไม่ไหวนั้นทิ่มแทงในความรู้สึกจนเจ็บปวด"

# "If I look at the ceiling hard enough, I can imagine the tile edges and small dimples of the ceiling in the hospital. That fact alone is enough to make me sit up and try to pull myself together."
"ถ้าเพ่งเพดานนาน ๆ ไปก็จะมีภาพฝ้าของโรงพยาบาลที่มีเหลี่ยมมุมพร้อมรอยยุบเล็ก ๆ ลอยมาซ้อนทับ เมื่อนึกได้ดังนั้น\nฉันจึงผุดลุกขึ้นนั่งแล้วตั้งสติ"

# "I scratch the back of my disheveled hair, glancing around the room. Lilly and Hanako are nowhere to be seen, and the television's turned off."
"ฉันเกาผมส่วนท้ายทอยอันยุ่งเหยิงพลางมองไปรอบ ๆ ห้อง ลิลลี่กับฮานาโกะไม่อยู่ โทรทัศน์ก็ปิดอยู่"

# "The clock above it says it's pretty late in the afternoon. The noticeably reddened sky outside the windows confirms it further."
"นาฬิกาบนผนังบอกเวลาว่าตอนนี้บ่ายแก่ ๆ ฟ้าสีแดงฉานนอกหน้าต่างเน้นย้ำเวลาขณะนี้อีกทางหนึ่ง"

# "I turn and pick myself off the futon, swaying slightly as I put my arms out for balance. I suppose I'd better go look for the girls to see if they're… all right…"
"ฉันบิดตัวแล้วลุกจากฟูกฟูตงขึ้นยืนพลางยืดแขนออกประคองตัวเองไม่ให้โซเซ คงต้องไปดูสองคนนั้นสักหน่อยว่า…\nโอเคดีมั้ย…"

# "As I look out the window, I faintly see something in the distance."
"พอมองออกไปนอกหน้าต่างก็เห็นเงาบางอย่างอยู่รำไร"

# "Straining my eyes, I can just make out the shape of a person's figure. Her long blonde hair, swaying in the faint breeze, makes her almost seem to melt into the bright yellow of the wheat field."
"เมื่อเพ่งตามองก็เห็นเป็นเงาคน ผมยาวสีบลอนด์ที่ไหวไปตามสายลมทำให้ดูคล้ายว่าเธอนั้นกลืนเลือนไปกับทุ่งสาลี\nสีทองอร่าม"

# "Without a second thought, I leave the room to follow that lone apparition."
"ฉันเดินออกห้องไปหาเงาที่ยืนโดดเดี่ยวอยู่ตรงนั้นในทันที"

stop ambient fadeout 2.0
play music music_innocence fadein 14.0

scene bg hok_wheat_ss at Fullpan(8.0)
with Fade(0.5, 0.2, 3.0, color="#fff")

# "The brightness of the setting sun assaults my freshly woken eyes, forcing me to avert them until they adjust."
"แสงอาทิตย์เจิดจ้าแยงตาฉันที่ยังงัวเงียอยู่จนต้องหรี่ตารอให้ปรับตัวกับความสว่างได้"

# "The long, yellow strands of wheat brush against my legs as I wade through them, the densely-grown field making it hard to advance."
"ฉันเดินฝ่าทุ่งสาลีเหลืองอร่ามสูงชะลูดซึ่งขึ้นอย่างแน่นหนาจนเดินลำบาก"

# "Regardless, my eyes stay fixed ahead, true to that solitary figure. Within minutes I reach her, meters behind her turned back."
"แต่แม้กระนั้น สายตาของฉันยังคงจับจ้องอยู่ที่เงาโดดเดี่ยวตรงหน้านั้นไม่ไปไหน ผ่านไปสองสามนาทีฉันจึงเดินมาถึง\nในระยะที่อยู่ห่างจากแผ่นหลังของเธอไปไม่กี่เมตร"

# hi "Lilly?"
hi "ลิลลี่?"

scene bg hok_wheat_ss at right
show lilly back_pout_cas_ss at center
with charaenter

# "She simply nods."
"ลิลลี่เพียงพยักหน้า"

# hi "Where's Hanako?"
hi "ฮานาโกะอยู่ไหน"

show lilly back_listen_cas_ss
with charachange

# li "She's in bed. She went to sleep after I calmed her down."
li "ฮานาโกะหลับอยู่ พอปลอบให้แล้วก็หลับไป"

# "She says it matter-of-factly and with as few words as possible, as if saying any more was strictly forbidden."
"ลิลลี่พูดด้วยน้ำเสียงราบเรียบและยังไม่ใช้คำให้ฟุ่มเฟือย ราวกับว่าการจะพูดอะไรมากกว่านั้นเป็นสิ่งต้องห้าม"

# "There's something different about her. Her normally confident figure seems oddly fragile, her body offering no resistance to the breeze blowing her skirt."
"เธอดูแปลกไปจากทุกที ปกติตัวลิลลี่นั้นดูเป็นคนมั่นใจ ทว่าคราวนี้เธอดูเปราะบางอย่างประหลาด ร่างกายเธอไม่มีแม้\nแรงต้านสายลมที่พัดโบกกระโปรงของเธอ"

# "The strands of wheat sway from side to side while a deafening pause passes, the only sound being their rustling."
"ต้นสาลีลู่เอนไปตามลม สิ่งที่เข้ามาแทรกความเงียบในขณะนี้นั้นมีเพียงเสียงต้นสาลีเหล่านั้นที่เสียดสีกัน"

# "As we stand in the field alone, I know what I have to ask."
"พวกเรายืนอยู่กลางทุ่งสาลีกันตามลำพัง และฉันรู้แล้วว่าจะต้องถามอะไรต่อ"

# hi "What's wrong, Lilly? You're not acting like you usually do."
hi "มีอะไรหรือเปล่าลิลลี่ เธอทำตัวแปลก ๆ นะ"

show lilly back_sad_cas_ss
with charachange

# li "Remember when I talked of my family, Hisao?"
li "จำตอนที่ฉันเล่าเรื่องครอบครัวให้เธอฟังได้มั้ยฮิซาโอะ"

# hi "Your family…"
hi "ครอบครัวของเธอ…"

# "I look downwards in thought, sifting through my scattered memories. The event seems to leap ready to hand when I search for it, rising to the surface as soon as it was recalled."
"ฉันก้มหัวครุ่นคิดเสาะหาในท่ามกลางความทรงจำอันระเกะระกะ เหตุการณ์นั้นคล้ายลอยเด่นขึ้นมาจากกองเหล่านั้น\nทันทีที่ฉันย้อนระลึกถึง"

# hi "After Hanako's birthday party?"
hi "ตอนที่จัดงานวันเกิดให้ฮานาโกะแล้วน่ะเหรอ"

# "She gives a single, simple nod."
"ลิลลี่พยักหน้าสั้น ๆ หนึ่งครั้ง"

show lilly back_pout_cas_ss
with charachange

# li "It was nice… back then. You and I, celebrating with Hanako. Simply sharing presents, talking, having fun together. It was almost as if we were a family. One small, misshapen family."
li "ตอนนั้น… มันก็ดีนะ นายกับฉันฉลองด้วยกันกับฮานาโกะ ให้ของขวัญกัน คุยกัน สนุกด้วยกัน เหมือนว่าพวกเรา\nเป็นครอบครัวเลย ครอบครัวเล็ก ๆ ผิดรูปครอบครัวหนึ่ง"

show lilly back_sad_cas_ss
with charachange

# li "I thought that could just go on forever. Just the three of us, happily together."
li "ฉันอยากให้เป็นอย่างนั้นไปตลอดกาลเลย เพียงเราสามคนอยู่ด้วยกันอย่างมีความสุข"

# "She takes a long breath, a slight shakiness to it just barely audible through the moving air."
"ลิลลี่ถอนหายใจยาว ความสั่นเครือในน้ำเสียงนั้นถูกลมที่พัดไหวกลบไปจนแทบสิ้น"

show lilly back_pout_cas_ss
with charachange

# li "Even if my family was so far away… as long as we were together, that was all I needed. I don't want to lose you, Hisao."
li "ถึงแม้ครอบครัวของฉันจะอยู่แสนไกล… แต่ขอแค่ตราบใดที่พวกเราอยู่ด้วยกัน ฉันก็ไม่ต้องการอะไรอีกแล้ว\nฉันไม่อยากเสียเธอไปเลย ฮิซาโอะ"

# li "I didn't even realize how afraid I was of losing someone else until today. Until…"
li "ฉันไม่เคยรู้เลยว่าฉันเองกลัวการสูญเสียใครสักคนไปแค่ไหน จนกระทั่ง…"

# hi "I'm sorry, Lilly. I know my body's weak, but even then I make the most stupid of mistakes."
hi "ขอโทษนะลิลลี่ ทั้งที่รู้อยู่แท้ ๆ ว่าร่างกายตัวเองอ่อนแอ แต่บางทีฉันก็ยังทำอะไรพลาดแบบโง่ ๆ อยู่เลย"

stop music fadeout 4.0

show lilly back_sad_cas_ss
with charachange

# li "Don't apologize… please don't apologize…"
li "ไม่จำเป็นเลย… ไม่จำเป็นต้องขอโทษหรอก…"

# hi "Lilly…?"
hi "ลิลลี่…"

show lilly basic_concerned_cas_ss
with charachange

# "She turns to face me, her pale cheeks stained with tears."
"เธอหันมามองฉันพร้อมน้ำตาที่อาบสองแก้ม"

show lilly basic_concerned_cas_close_ss
with characlose

# "One misguided step after another she stumbles towards me, her arms held out in search of so much as a faint brush against me."
"ลิลลี่ก้าวพลาดติดกันสองสามก้าวจนสะดุดล้มเข้าหาฉัน เธอยื่นแขนออกมาเพื่อที่จะพยายามเสาะหาตัวฉันแม้เพียง\nเสี้ยวหนึ่งให้เจอ"

play music music_romance fadein 2.0

window hide

scene unlock_ev lilly_wheat_close
show ev lilly_wheat_large:
        yalign 0.5 xalign 0.0 subpixel True
        easein 20.0 xalign 1.0
show ovl lilly_wheat_foreground:
        yalign 0.5 xalign 0.0 subpixel True
        easein 20.0 xalign 1.0
with GenericWhiteout(1.0, 0.0, 4.0)

window show

# "My heart doesn't race nor pound as I step towards Lilly, gently taking and steadying her in my arms as she quickly clutches to me, sobbing."
"ฉันเดินเข้าไปหาลิลลี่ด้วยใจที่ไม่ได้เต้นรัวแรงเป็นพิเศษแล้วคว้าพยุงตัวเธอไว้อย่างอ่อนโยนในจังหวะเดียวกันกับที่เธอ\nจับตัวฉันแน่นพลางร้องสะอึกสะอื้น"

# "With her face trembling against my shoulder, the next words from her mouth are the last I expected."
"ลิลลี่ตัวสั่นซบอยู่กับไหล่ฉัน คำพูดต่อมาจากเธอนั้นเกินจากความคาดหมายของฉันไปไกล"

# li "I love you, Hisao. I love you, I love you, I love you, I love you, I love you!"
li "ฉันรักเธอนะฮิซาโอะ ฉันรักเธอ ฉันรักเธอ ฉันรักเธอ ฉันรักเธอ ฉันรักเธอ!"

# li "Don't go away, I beg of you. Never, ever go away. I love you, so please…!"
li "อย่าไปไหนเลยนะ ขอร้องละ อย่าไปไหนอีกเลย ฉันรักเธอ ได้โปรด…!"

# "So… that's why she's been acting like this. That tender voice when I called her, her thoughtless concern at the slightest pain I might feel…"
"มิน่าล่ะ… ลิลลี่ถึงได้ทำตัวอย่างนั้น ทั้งเสียงขานรับอันอ่อนโยนยามที่ฉันเรียกหา ทั้งความเป็นห่วงที่มีให้กับอาการ\nเจ็บป่วยแม้เพียงน้อยนิดของฉันโดยไม่คิดอะไร…"

# "After having been left in Japan without her family, and with only Akira, Hanako and me around, she was afraid of losing yet another person who was close to her. She was genuinely worried for me."
"ลิลลี่ถูกครอบครัวทิ้งให้อยู่ที่ญี่ปุ่น โดยที่คนใกล้ชิดกับเธอมีเพียงอากิระ ฮานาโกะ แล้วก็ฉัน เธอจึงกลัวการที่จะต้อง\nสูญเสียคนที่สนิทกับเธอไปอีกคน ที่ผ่านมาลิลลี่นั้นเป็นห่วงฉันจริง ๆ"

# "It's a strange feeling. A mix of surprise and sorrow, yet also of the deepest gratitude I think I've ever felt. The only reaction I can muster among my conflicting emotions is a calm sigh."
"เป็นความรู้สึกที่ประหลาด มีทั้งความแปลกใจ เศร้าสร้อย และยังมีความรู้สึกยินดีอย่างถึงที่สุดเท่าที่เคยรู้สึกมาต่อเธอ\nในใจยังคงมีอารมณ์ที่ระคนกันอยู่ สิ่งเดียวที่ฉันพอจะตอบเธอได้มีเพียงเสียงถอนหายใจอย่างสงบเท่านั้น"

# hi "You idiot."
hi "ยัยบ๊อง"

# li "Hi… sao?"
li "ฮิ… ซาโอะ?"

# "For a fleeting moment, I feel her body become still. The only movement to be felt is the calm afternoon breeze."
"ร่างลิลลี่ที่ฉันสัมผัสอยู่แข็งค้างไปชั่วเสี้ยววินาทีหนึ่ง สิ่งเดียวที่ยังเคลื่อนไหวมีเพียงสายลมเอื่อยยามบ่าย"

# hi "I said it before, didn't I? It's only natural to feel concerned about those around you."
hi "ฉันเคยบอกเธอไปแล้วนี่ว่าคนเราจะเป็นห่วงคนรอบตัวก็ไม่แปลก"

# hi "I'm still here, and I'll always be here, because I want to see you more each day. To share in your happiness, to support you in your sadness…"
hi "ฉันยังอยู่ตรงนี้ และจะอยู่เคียงข้างเธอตลอดไป เพราะทุกวันฉันอยากเจอเธอให้บ่อยขึ้น เพื่อที่พอมีสุขแล้วก็จะได้ร่วมสุข\nมีทุกข์ก็จะได้ร่วมทุกข์…"

# hi "But most of all, I'll still be here because I want to see your smile. Your true smile."
hi "แต่ที่สำคัญที่สุด ฉันจะอยู่เคียงข้างเธอ เพราะฉันอยากเห็นรอยยิ้มของเธอ รอยยิ้มที่แท้จริงของเธอ"

# "A single gust of wind rustles the long strands of wheat, a second's silence passes."
"ลมพัดมาวูบหนึ่งไล้ต้นสาลีที่สูงชะลูด พวกเราเงียบไปชั่วอึดใจหนึ่ง"

# hi "Smile when you want to smile. Cry when you want to cry. I love you, Lilly. So you don't have to hold back any more."
hi "ถ้าอยากยิ้มก็ยิ้มเลย ถ้าอยากร้องไห้ก็ร้องเลย ฉันรักเธอนะลิลลี่ ไม่ต้องฝืนตัวเองอีกแล้วนะ"

# "With that, her arms clutch my back as tightly as she can, her face buried beside mine."
"แล้วเธอก็ซบหน้าเข้ากับไหล่ฉันพลางจับหลังฉันแน่นสุดแรง"

scene ev lilly_wheat_small:
    xalign 0.5 yalign 0.5 zoom 1.1 subpixel True
    ease 16.0 zoom 1.0
with whiteout

# "Her tears fall down my back and she cries unrestrainedly as the last of her resistance melts away."
"น้ำตาเธอร่วงเผาะลงที่หลังฉัน เธอทิ้งความอดกลั้นทั้งหลายใด ๆ แล้วปล่อยให้ตัวเองร้องไห้เต็มที่"

# li "Hisao! Hisao! Hisao!"
li "ฮิซาโอะ! ฮิซาโอะ! ฮิซาโอะ!"

# "I close my eyes and bring my head down to her shoulder, holding her shaking frame tightly."
"ฉันหลับตาซบไหล่โอบร่างที่สั่นเทาของเธอไว้แน่น"

# hi "It's okay, Lilly. I'll never go away."
hi "ไม่เป็นไรนะลิลลี่ ฉันจะไม่ไปไหนอีกแล้ว"

# hi "I promise."
hi "ฉันสัญญา"

stop music fadeout 6.0

#**************************************

label th_L17:

scene bg hok_lounge_ss
with locationskip

# "We slowly walk back to the house, holding each other tightly as we take a seat inside. Lilly leans her head onto my shoulder as I put my arm around her waist."
"พวกเราค่อย ๆ เดินกลับมาที่บ้าน พอนั่งลงแล้วพวกเราก็กอดกันแน่น ลิลลี่เอาหัวซบไหล่ฉัน ส่วนฉันก็เอาแขนโอบเอว\nเธอไว้"

# "Neither of us has any want to break the silence."
"ไม่มีใครต้องการที่จะพูดอะไร"

# "With her eyes shut it's hard to work out whether she's fallen asleep. Not that I mind: the warmth of her body leaning against me, the softness of her hand delicately held in mine…"
"ลิลลี่หลับตาจนฉันไม่รู้ว่าหลับอยู่หรือเปล่า ซึ่งฉันก็ไม่ถือหรอก ทั้งความอบอุ่นจากร่างกายเธอที่พิงฉัน ทั้งความนุ่มนวล\nจากมือเธอที่จับมือฉันไว้อย่างอ่อนโยน…"

# "For a long, long time we sit leaning against one another, sharing our warmth and feelings as night eventually begins to settle in."
"พวกเรานั่งพิงกันแบ่งปันความอบอุ่นและความรู้สึกของกันและกันอยู่นานสองนานจนค่ำคืนเริ่มคืบคลานเข้ามา"

# "Lilly's gentle, soft voice ends the silence."
"ลิลลี่เปล่งเสียงอันอ่อนโยนและนุ่มนวลขึ้นมาก่อน"

show lilly basic_smileclosed_cas_close_ss at center
with charaenter

play music music_twinkle fadein 6.0

# li "Thank you, Hisao."
li "ขอบคุณนะฮิซาโอะ"

# hi "Thank you?"
hi "ขอบคุณ?"

show lilly basic_smile_cas_close_ss
with charachange

# li "For returning my feelings."
li "ที่ตอบรับความรู้สึกของฉัน"

# hi "Did you think I wouldn't?"
hi "คิดว่าฉันจะบอกปัดเหรอ"

show lilly basic_weaksmile_cas_close_ss
with charachange

# li "There was the possibility."
li "ก็ยังเป็นไปได้นี่นา"

# "I take a deep breath in thought. That much was only my fault."
"ฉันสูดหายใจลึกพลางครุ่นคิด ก็เป็นความผิดของฉันเองละนะ"

# hi "It's funny, actually. I was thinking of telling you about my own feelings sometime soon."
hi "แต่ก็ตลกดีนะ ฉันเองก็กะจะบอกรักเธออยู่เหมือนกัน"

# hi "I guess, in that way, you saved me the effort."
hi "ก็คงนับได้ว่าเธอช่วยทุ่นแรงฉันไปได้ละมั้ง"

show lilly basic_giggle_cas_close_ss
with charachange

# "She raises her head a little and gives a tiny, amused giggle. I smile at how earnest it is, so girlish in its lightness. She collects herself soon afterward, her hair resting against my shoulder."
"ลิลลี่ยกหัวขึ้นเล็กน้อยก่อนจะหัวเราะคิกคักชอบใจ ฉันยิ้มให้กับความจริงใจในเสียงหัวเราะอันสดใสราวเด็กสาวนั้น\nแล้วเธอก็จัดแจงตัวเองให้ดูเรียบร้อยโดยที่ผมของเธอยังพาดอยู่บนบ่าฉัน"

# hi "Feeling a bit better?"
hi "รู้สึกดีขึ้นหรือยัง"

show lilly basic_smileclosed_cas_close_ss
with charachange

# "She gives a small nod."
"ลิลลี่พยักหน้าน้อย ๆ"

show lilly basic_smile_cas_close_ss
with charachange

# li "You are thoughtful, Hisao. That's why I like you."
li "เธอเป็นคนจิตใจดีนะฮิซาโอะ นี่แหละฉันถึงได้ชอบเธอ"

# hi "I'm sorry I'm like this. As much as I didn't want to make you concerned for me, I couldn't do anything to prevent it."
hi "ขอโทษที่ฉันอ่อนแออย่างนี้นะ ถึงฉันจะไม่อยากให้เธอต้องมาห่วงฉันก็จริง แต่ฉันก็ทำอะไรกับความอ่อนแอนี้ไม่ได้เลย"

show lilly basic_concerned_cas_close_ss
with charachange

# li "Don't apologize for it. Please don't."
li "ไม่ต้องขอโทษหรอกจ้ะ อย่าเลย"

# hi "Lilly?"
hi "ลิลลี่?"

show lilly basic_reminisce_cas_close_ss
with charachange

# li "Have I ever apologized for my blindness, even once? You can't help the way you were born, Hisao. There's no point in apologizing for who you are."
li "ฉันเคยขอโทษที่ฉันตาบอดสักครั้งหรือเปล่า คนเราน่ะเลือกเกิดไม่ได้หรอกนะฮิซาโอะ ขอโทษที่ตัวเราเป็นอย่างนั้นไป\nก็ไม่ได้อะไรขึ้นมาหรอก"

# "She says this with surprising conviction. In the end, it was perhaps this mentality which spurred her to befriend me in such a short time, in addition to her motherly instincts."
"น้ำเสียงเธอฟังดูเด็ดเดี่ยวเหลือเชื่อ สุดท้ายแล้ว ก็อาจเป็นความคิดเช่นนี้เองที่ทำให้เธอได้เป็นเพื่อนกับฉันได้อย่าง\nรวดเร็วขนาดนั้น กอปรกับสัญชาตญาณอย่างคนเป็นแม่ของเธอด้วย"

# "She did seem to become trusting very quickly, but I'd never questioned why. Now it seems obvious that she did so to help me as I went through one of the lowest points of my life."
"ลิลลี่วางใจฉันตั้งแต่แรก ๆ ที่รู้จักกันก็จริง แต่ฉันก็ไม่เคยคิดจะถามหาเหตุผลเลย ทว่าตอนนี้คำตอบนั้นชัดเจนแล้วว่า\nที่เธอทำไปเพราะอยากช่วยฉันที่กำลังฝ่าฟันช่วงที่แย่ที่สุดช่วงหนึ่งในชีวิตอยู่"

# "I move to respond, but cut myself off as I feel her fingers run gently through my hair. I feel their soft and delicate touch moving downwards to trace the contours of my face, her palm finally settling on my cheek."
"ฉันเตรียมจะพูดตอบ แต่ก็ต้องผงะไปเมื่อลิลลี่สางผมฉันเบา ๆ สัมผัสอันนุ่มนวลและแผ่วเบานั้นลากไปตามส่วนนูนเว้า\nบนใบหน้า จนสุดท้ายมาหยุดอยู่ที่แก้ม"

show lilly basic_weaksmile_cas_close_ss
with charachange

# li "You are a beautiful person, Hisao. Please, don't ever apologize for that."
li "เธอน่ะเป็นคนที่{i}งดงาม{/i}นะฮิซาโอะ อย่าได้ขอโทษเรื่องนั้นอีกเลย"

# "For a moment, I'm utterly speechless. I slowly bend my head down, placing a tender kiss on her light, voluminous hair."
"ฉันนิ่งอึ้งไปครู่หนึ่งก่อนจะก้มหัวลงลงจุมพิตกลุ่มผมสลวยของเธออย่างแผ่วเบา"

# hi "We're a couple of right old fools, aren't we?"
hi "พวกเราสองคนนี่โง่เง่าสิ้นดีเลยเนอะ"

show lilly basic_cheerful_cas_close_ss
with charachange

# li "…We are."
li "…นั่นสินะ"

# "After a long calm, she speaks again."
"หลังจากที่เงียบกันไปอีกพักหนึ่งลิลลี่ก็พูดขึ้นอีกครั้ง"

show lilly basic_smile_cas_close_ss
with charachange

# li "Hisao?"
li "ฮิซาโอะ?"

# hi "Yes?"
hi "ว่า"

show lilly basic_smileclosed_cas_close_ss
with charachange

# li "I…"
li "ถ้า…"

stop music fadeout 4.0

show lilly basic_weaksmile_cas_close_ss
with charachange

# li "I wouldn't mind if you…"
li "ถ้าเธอจะ…"

# "I feel her hand tensing under mine, trembling slightly. My mouth opens, but try as I might I can't formulate a response to her proposition."
"มือของเธอที่ฉันกุมอยู่นั้นสั่นเกร็งเล็กน้อย ฉันได้แต่อ้าปากโดยที่ไม่อาจนึกหาคำพูดใด ๆ มาตอบรับสิ่งที่เธอว่ามาได้"

# hi "Lilly…"
hi "ลิลลี่…"

# "Before I can say another word, she slips her hand from under mine and tenderly holds the side of my face once more."
"ลิลลี่ดึงมือออกจากการเกาะกุมของฉันแล้วมาจับใบหน้าด้านข้างของฉันอีกครั้งอย่างนุ่มนวล"

show lilly basic_pout_cas_close_ss
with charachange

# li "Please."
li "ขอร้องละ"

# "I give a peaceful smile, holding her hand against my cheek as I nod a single time."
"ฉันยิ้มตอบอย่างผ่อนคลายพลางจับมือเธอที่อยู่บนแก้มฉันแล้วพยักหน้าหนึ่งครั้ง"

# hi "Okay."
hi "ได้"

play music music_heart fadein 0.5

show lilly basic_smileclosed_cas_close_ss
with charachange

# "As I look into her eyes, she leans towards me. Her delicate lips touch mine as she guides herself with her hand."
"ฉันมองตาลิลลี่ในจังหวะที่เธอโน้มตัวเข้ามา ริมฝีปากลิลลี่ทาบเข้ากับริมฝีปากฉันระหว่างที่เธอใช้มือนำทาง"

# "She breaks off not a second later, faintly smiling."
"ผ่านไปชั่วอึดใจเธอก็ผละตัวออกแล้วคลี่ยิ้มจาง ๆ"

show lilly basic_smile_cas_close_ss
with charachange

# li "I love you, Hisao."
li "ฉันรักเธอนะฮิซาโอะ"

show lilly basic_smileclosed_cas_close_ss
with charachange

# "We kiss again, this time with both of us meeting the other."
"เราจูบกันอีกครั้ง ทว่าคราวนี้เราสองคนหันตัวเข้าหากันเต็มที่"

# "While the previous kiss was one of love, this is one of lust, our tongues meeting and our breathing heavy. After precious seconds we part, both our faces well and truly flushed."
"จูบครั้้งแรกนั้นเป็นความรัก และจูบครั้งนี้เป็นความใคร่ ลิ้นของเราสอดประสานกันอยู่ใต้ลมหายใจที่หอบหนัก\nหน้าของพวกเรานั้นแดงก่ำหลังจากที่ชั่วขณะอันหอมหวานนั้นจบลง"

# "Both of us bring our fingers to our lips in unison, recalling that fleeting feeling, rapidly becoming buried both by our urges and bashfulness."
"พวกเรายกมือขึ้นมาแตะปากพร้อม ๆ กันเพื่อระลึกถึงสัมผัสชั่วแล่นนั้น ทั้งแรงกระตุ้นและความเขินอายแล่นเข้ามา\nในความคิดพวกเราอย่างรวดเร็ว"

show lilly basic_pout_cas_close_ss
with charachange

# "Lilly is the first to shift uncomfortably, though."
"แต่เป็นฝั่งลิลลี่ที่ทำท่ากระมิดกระเมี้ยนก่อน"

# hi "What is it?"
hi "มีอะไรเหรอ"

show lilly basic_weaksmile_cas_close_ss
with charachange

# li "Should we… get more comfortable?"
li "ไปที่… ที่มันสะดวกกว่านี้มั้ย"

# hi "Hmm? Ah, o-okay…"
hi "หืม? อ้อ อะ โอเค…"

# "Now that she mentions it, this futon would be a bit too narrow to do much on. Considering the thoughts running through both our minds, it's no small wonder one of us has any measure of foresight left."
"จะว่าไปแล้ว ฟูกฟูตงนี่ก็คงแคบเกินกว่าที่จะทำอะไรได้ถนัด แต่ด้วยสิ่งที่อยู่ในความคิดเราสองคนตอนนี้ ก็คง\nไม่แปลกที่ต่างคนต่างแทบไม่เหลือสมองส่วนที่มาจะคิดวางแผนอะไรแล้ว"

show lilly invis:
    ypos 1.2
with dissolvecharamove

hide lilly
with vpunch

# "I take her hands and guide her sideways as I move, the brief and awkward dance ending with both of us tentatively sitting on the floor opposite each other."
"ฉันจับมือเดินนำทางลิลลี่ไปด้านข้าง พวกเราเดินอย่างกระอักกระอ่วนโซเซกันไปมาอยู่ครู่หนึ่งก่อนจะมานั่งกับพื้น\nหันหน้าเข้าหากันอย่างเก้ ๆ กัง ๆ"

# "As I reach forward to pull her top up, she stops after she moves her hands to do the same."
"พอยื่นมือไปหมายจะถกเสื้อของเธอขึ้น ลิลลี่ที่ยื่นมือมาเพื่อจะถอดเสื้อฉันด้วยก็ชะงักไป"

show lilly basic_concerned_cas_close_ss:
    center
    ypos 1.17
with charaenter

# li "You're shaking…"
li "มือเธอสั่น…"

# "I pause for a moment and look at my hands."
"ฉันนิ่งไปครู่หนึ่งแล้วก้มมองมือตัวเอง"

# "Sure enough, they're quivering slightly. Whether it's from nervousness or excitement, I'm not sure."
"ก็จริง มือฉันสั่นอยู่นิดหน่อย แต่ไม่รู้ว่าสั่นเพราะประหม่าหรือตื่นเต้นกันแน่"

# hi "Uh… I guess I am."
hi "เอ่อ… ก็สั่นแหละ"

show lilly basic_weaksmile_cas_close_ss
with charachange

# li "So you're as nervous as I am, then?"
li "แปลว่าเธอก็ตื่นเต้นเหมือนกันงั้นสิ"

# "I withdraw my hands and sigh, steadying myself. We have plenty of time, so there's no need to rush this."
"ฉันชักมือกลับแล้วถอนหายใจเพื่อตั้งสติ ยังมีเวลาอีกเยอะ ไม่ต้องรีบ"

# hi "Sorry. It's my first time, so I'm a bit…"
hi "ขอโทษที พอดีเพิ่งเคยทำเป็นครั้งแรก ก็เลย…"

show lilly basic_cheerfulblush_cas_close_ss
with charachange

# "She giggles shakily, all but confirming what I reasonably deduced by now."
"ลิลลี่หัวเราะคิกคักเสียงสั่น ซึ่งก็บ่งบอกว่าที่ฉันเดานั้นถูกแล้ว"

show lilly basic_smile_cas_close_ss
with charachange

# li "It's the same for me. I'm happy… we could share this together."
li "ฉันก็เหมือนกัน ดีใจจัง… ที่ได้ทำเป็นครั้งแรกด้วยกัน"

# "I match her smile twofold, leaning forward and taking her body in my arms as she reaches to hug me back."
"ฉันยิ้มกว้างไปกว่าลิลลี่สองเท่าก่อนจะโน้มตัวเข้าไปโอบเธอเอาไว้ ส่วนเธอเองก็กอดฉันกลับ"

# hi "I love you, Lilly."
hi "ฉันรักเธอนะลิลลี่"

show lilly basic_smileclosed_cas_close_ss
with charachange

# li "You already said that."
li "เธอพูดไปแล้วนี่"

# "I can't help grinning. Even in such a situation, she still has her wits about her."
"ฉันอดยิ้มไม่ได้ สถานการณ์อย่างนี้แท้ ๆ แต่สติยังอยู่ดี"

hide lilly
with charaexit

# "Breaking our embrace, we decide to take off our own clothing. While it's easier this way, I don't doubt it's just an attempt to distract ourselves from our nerves."
"พวกเราผละออกจากกันแล้วต่างถอดเสื้อผ้าของตัวเอง ส่วนหนึ่งที่ทำอย่างนี้เพราะสะดวกกว่าก็จริง แต่อีกส่วนก็\nเป็นไปได้ว่าที่ทำไปเพราะจะได้ไม่ประหม่ากันมากด้วย"

# "With slightly stiff hands, I begin to slide the first button out from my shirt."
"ฉันแกะกระดุมเสื้อเม็ดแรกด้วยมือที่ยังเกร็ง ๆ อยู่"

# "Once we remove the last of our clothes, which end up haphazardly piled behind us, my breath is taken by the sight in front of me."
"พวกเราถอดเสื้อผ้ากองไว้แบบลวก ๆ ที่หลังแต่ละคน เมื่อถอดเสื้อผ้าชิ้นสุดท้ายแล้วฉันก็ต้องตะลึงกับภาพตรงหน้า"

label th_L17h:

show lilly behind_reminisce_nak_ss
with charaenter

# "Her long, shapely legs, full hips and her breasts, plump but dainty… her slightly blushing face, delicate and reserved, is framed by the bangs of her hair."
"ขายาวได้รูป สะโพกอิ่ม อกอวบกำลังดี… ผมที่ปรกใบหน้าอันบอบบางและเรียบร้อยที่มีสีแดงเรื่อ"

# "Her hands, tightly held behind her, only serve to further accentuate her chest. Her tall and pale body is beautiful when bared."
"มือของเธอที่จับกันแน่นไพล่หลังอยู่ยิ่งขับเน้นหน้าอกเธอให้เด่นชัด ร่างสูงขาวนวลของเธอยามเปลือยนั้นช่างงดงาม"

# "This girl in front of me, reserved yet playful, astute yet hospitable, is the girl I've fallen in love with."
"ผู้หญิงตรงหน้าคนนี้—ที่เรียบร้อยทว่าขี้เล่น ที่หลักแหลมทว่าโอบอ้อมอารี—คือคนที่ฉันตกหลุมรัก"

# "I lean forward, delicately taking her shoulders in my hands."
"ฉันโน้มตัวเข้าไปจับไหล่เธอไว้"

show lilly behind_listen_nak_close_ss
with charachange

# "As I do, she brings her hands to my chest. With a slightly uneven breath, we lean into a deep kiss."
"จังหวะนั้นเองเธอก็ยื่นมือมาแตะที่หน้าอกฉัน แล้วเราก็โผเข้าจูบโดยที่ลมหายใจยังสั่นอยู่เล็กน้อย"

# "I feel one of Lilly's hands slowly slide up to my shoulder, it and her head very gently moving forwards. Assuming her intent, I lean back onto the floor."
"มือของลิลลี่สัมผัสเลื่อนขึ้นมาที่ไหล่ฉัน เธอใช้มือดันไหล่และโน้มหัวเข้าหาช้า ๆ ฉันจึงเอนตัวลงนอนไปตามที่เธอ\nคงต้องการ"

# hi "Ah…"
hi "อ๊ะ…"

scene evhunlock lilly_handjob_chest_normal_small
show evh lilly_handjob_chest_normal:
    xalign 0.7 yalign 1.0 subpixel True
    ease 8.0 xalign 0.4 yalign 0.2
with whiteout

# "She lowers herself beside me, one hand stroking my hair as the other moves across my chest. The feeling of her breast against it is enough to excite me."
"ลิลลี่เอนตัวลงนอนข้าง ๆ ฉัน มือข้างหนึ่งสางผมฉัน ส่วนอีกข้างก็ไล้ไปมาตามหน้าอก สัมผัสจากหน้าอกเธอที่ถูก\nตัวฉันนั้นทำให้ฉันตื่นตัว"

# "This must be her way of taking in what I've already seen of her; despite her lack of sight, she engraves every detail of my bare body and chest into her mind."
"เธอคงทำเช่นนี้เพื่อเป็นการรับรู้ในสิ่งที่ฉันได้เห็นด้วยตาเมื่อครู่ไปแล้ว แม้เธอจะมองไม่เห็น แต่เธอจะสลักทุกรายละเอียด\nจากหน้าอกและร่างเปลือยเปล่าของฉันไว้ในใจมั่น"

# "When her middle finger falls into the slight recess of my chest scar, a lingering effect of my operation so many months ago, she slowly runs her hand down its length."
"เธอลากนิ้วกลางไปตามรอยยุบตรงหน้าอกฉันซึ่งเป็นแผลเป็นจากการผ่าตัดเมื่อหลายเดือนที่แล้วอย่างช้า ๆ"

show evhunlock lilly_handjob_chest_frown_small
show evh lilly_handjob_chest_frown:
    xalign 0.4 yalign 0.2
with charachange

# li "This is…"
li "นี่มัน…"

# hi "The scar, from my surgery. They had to do this in order to operate on my heart."
hi "แผลเป็นจากการผ่าตัดน่ะ หมอต้องผ่ารักษาหัวใจตรงนี้"

# "For a moment she's lost for words, the idea of such extensive scarring adding a new worry for her. Her expression changes from curiosity to apprehension."
"เธอเงียบไปครู่หนึ่งด้วยความกังวลเรื่องแผลเป็นที่มีความยาวมากขนาดนี้ สีหน้าซึ่งเป็นห่วงผุดขึ้นแทนที่สีหน้าซึ่งสงสัย"

# li "Should we… really be doing this kind of thing…?"
li "แล้วมาทำอะไรอย่างนี้… จะไม่เป็นอะไรใช่มั้ย…"

# "Those words bother me beyond what is rational. Lilly's face breaks my heart more than even her words possibly could, yet I don't even know the answer to her question."
"คำพูดของเธอทำให้ฉันพะวงไปไกลเกินกว่าที่จะเรียกได้ว่าสมเหตุสมผล ใบหน้าของลิลลี่นั้นทำให้ฉันรู้สึกแย่ยิ่งกว่า\nคำพูดของเธอเสียอีก แต่ฉันเองก็ไม่มีคำตอบให้เธอเช่นกัน"

# "I can't let this condition dominate me forever. It may not even be medically advisable, but I outright refuse to live my life in such a prison."
"แต่จะปล่อยให้อาการนี้คอยบงการชีวิตฉันไปตลอดไม่ได้ ฉันไม่ยอมใช้ชีวิตอยู่ในการจองจำนั้นหรอก แม้อาจจะเป็นอะไร\nที่หมออยากให้เลี่ยงก็ตาม"

# hi "It's okay, Lilly. This much will be okay."
hi "ไม่เป็นไรหรอกลิลลี่ ประมาณนี้ยังไหวอยู่"

show evh lilly_handjob_chest_normal
with charachange

# "Her troubled expression holds for a moment longer, but she eventually acquiesces, her hand moving to my lower chest and then my thigh."
"ลิลลี่ยังคงทำหน้าไม่สบายใจอยู่อีกพักหนึ่ง แต่สุดท้ายเธอก็ยอมเออออตามแล้วเลื่อนมือลงไปข้างล่างหน้าอกก่อนจะ\nขยับไปที่ต้นขา"

show evh lilly_handjob_chest_normal:
    zoom 1.0 xalign 0.4 yalign 0.2
    ease 4.0 zoom 0.667 xalign 0.5 yalign 0.5
with None

show evh lilly_handjob_stroke_normopen:
    zoom 1.0 xalign 0.4 yalign 0.2
    ease 4.0 zoom 0.667 xalign 0.5 yalign 0.5
with charachange

# "With a look of slight surprise, she slowly moves her hands downwards, her breath catching as she brushes the side of my lower hair."
"ลิลลี่ทำหน้าประหลาดใจเล็กน้อยพลางเลื่อนมือลงต่ำไปอีก ลมหายใจเธอขาดห้วงไปเมื่อสัมผัสเข้ากับขนส่วนล่าง"

# "She tentatively moves her hand sideways, delicately touching the most honest part of my body."
"เธอขยับมือเข้ามาอย่างกล้า ๆ กลัว ๆ แล้วแตะเข้ากับส่วนซึ่งตรงกับใจของฉันที่สุดอย่างเบามือ"

show evh lilly_handjob_stroke_normshut_small:
    truecenter 
    zoom 1.0
with charachange

# li "Th… this is…"
li "นะ… นี่มัน…"

# hi "Y-yeah."
hi "อะ อื้ม"

# "Our nervousness peaks as the act begins, her hand gently patting up and down as lightly as if it would break if breathed upon."
"พวกเราประหม่าอย่างถึงขีดสุดเมื่อมาถึงจุดเริ่ม ลิลลี่ขยับมือสัมผัสขึ้นลงอย่างแผ่วเบาราวกับว่าสิ่งนั้นอาจแหลกสลาย\nหากเพียงหายใจรดใส่"

# "I'm not sure whether it's just to steady myself or because I want to steady her, but I take my free hand and hold the side of her face in it. The feeling of her hair and soft skin is nice, and it seems to lighten her mood a bit."
"ฉันเอื้อมมือไปจับใบหน้าด้านข้างของเธอ ซึ่งฉันเองก็ไม่แน่ใจเหมือนกันว่าทำไปเพื่อจะทำให้ตัวเองใจเย็นลง\nหรือจะปลอบให้ลิลลี่ใจเย็นลงกันแน่ สัมผัสจากผมและผิวนุ่มของเธอนั้นช่างรู้สึกดี และดูเหมือนเธอเองก็จะ\nรู้สึกผ่อนคลายลงเล็กน้อยด้วย"

# "The mere fact that I'm being touched by her is surprisingly erotic. I feel my body relaxing as I submit to the pleasure overwhelming me."
"เพียงถูกเธอสัมผัสฉันก็รู้สึกร้อนรุ่มขึ้นมาเกินคาด ฉันคลายตัวให้หายเกร็งปล่อยให้ความหวามไหวแผ่ซ่านไปทั่วร่าง"

# "Long minutes pass in almost total silence, our heavy breathing the only sound to be heard in the house. Lilly's fingers stop affectionately stroking my hair and she opens her lips once again."
"หลายนาทีผ่านไปพร้อมความเงียบงัน โดยเสียงที่เติมเต็มภายในบ้านนั้นมีเพียงเสียงหายใจหอบของพวกเรา มือของลิลลี่\nซึ่งลูบไล้อยู่ที่ผมของฉันหยุดชะงัก เธอเปิดปากพูดอีกครั้ง"

show evh lilly_handjob_stroke_flustopen_small
with charachange

# li "Hisao…"
li "ฮิซาโอะ…"

# "I wait a second for the rest of the sentence, but none is forthcoming. She may be trying to take the lead, but she's still incredibly nervous."
"ฉันรอให้ลิลลี่พูดต่อ แต่ก็ไม่มีคำพูดใดตามมาอีก อาจจะพยายามนำอยู่ แต่ตัวเธอยังคงประหม่าหนัก"

# "I can't help smiling as I stroke her hair from her face a couple of times, reassuring her. As nervous as she may be, I'm thankful that Lilly's taking the lead. I'd probably be just as anxious as she if I were attending to her."
"เห็นแล้วก็อดยิ้มไม่ได้ ฉันลูบผมเธอที่ปรกหน้าอยู่สองสามครั้ง ถึงจะประหม่าไปหน่อย แต่ฉันก็ยินดีให้เธอนำให้ ถ้าฉัน\nเป็นฝ่ายนำบ้างก็คงเกร็งพอกัน"

show evh lilly_handjob_stroke_normopen_small
with charachange

# hi "Okay."
hi "ได้"

# "She pauses a moment before giving a small nod, sitting up and shifting her legs over mine. Once again my breath is stolen by the magnificent sight of her body over mine."
"ลิลลี่ชะงักไปครู่หนึ่งก่อนจะพยักหน้าแล้วขยับตัวลุกขึ้นนั่งเอาขาคร่อมตัวฉัน เป็นอีกครั้งที่ฉันต้องทึ่งกับกายอันงดงาม\nของเธอซึ่งอยู่บนตัวฉัน"

show evh lilly_cowgirl_smile_small
with whiteout

# "I can only look on frozen as she delicately lowers herself, resting her reddened lips over me. She slowly begins to move her hips downwards, her softness enveloping my consciousness."
"ฉันได้แต่มองไม่วางตาปล่อยให้เธอค่อย ๆ ลดตัวลงให้กลีบกุหลาบสีหวานนั้นทาบทับตัวฉัน เธอขยับเอวลงต่ำอีกช้า ๆ\nให้ความอ่อนนุ่มของเธอเข้าครอบครองความรับรู้ของฉัน"

show evh lilly_cowgirl_weaksmile_small
with charachange

# "She takes a deep breath to collect herself, her face remaining steady. With her hands taking in my body in lieu of sight, the intimate situation muddles her usual efforts to compensate for lack of eye contact."
"ลิลลี่สูดหายใจลึกตั้งสติโดยที่ยังตั้งหน้าตรงอยู่ เธอใช้มือสัมผัสร่างกายของฉันแทนการมองเห็น ตามปกติแล้วเธอจะใช้\nสัมผัสนี้แทนสายตาได้ตามปกติ ทว่าเหตุการณ์แสนรัญจวนนี้ได้เข้ามาขัดขวางจนจดจ่อลำบาก"

# "She gradually lowers herself onto me, her knees and hands supporting her as she does. Her entire body tenses as I enter, her expression obviously one of stifled pain."
"เธอลดตัวลงมาเรื่อย ๆ โดยใช้มือกับเข่ายันตัวไว้ พอฉันชำแรกเข้าไปทั้งร่างกายเธอก็เกร็งขึ้นมา สีหน้าเธอบอกชัด\nว่ากำลังกลั้นความเจ็บปวดอยู่"

# "Despite that, I can't help savoring the soft, warm feeling enveloping my consciousness, the surge of pleasure overcoming all my senses."
"ถึงอย่างนั้นฉันก็อดที่จะดื่มด่ำไปกับสัมผัสอันอ่อนนุ่มและอุ่นร้อนที่เข้าครอบครองความรับรู้ คลื่นความหวามไหว\nเข้าสาดซัดทุกประสาทสัมผัส"

# "The last vestiges of it all but disappear inside her while her nails slightly scrape into my chest in an effort to stop herself from yelping in pain. A pained moan, too much for her to suppress completely, escapes from her lips."
"ส่วนสุดท้ายที่เหลืออยู่ได้หลบหายเข้าไปในตัวเธอทั้งหมดแล้ว ลิลลี่จิกเล็บเข้ากับหน้าอกฉันเล็กน้อยเพื่อกลั้นเสียง\nไม่ให้ตัวเองร้องด้วยความเจ็บ เสียงครางอันเจ็บปวดซึ่งเกินกว่าที่เธอจะกลั้นไหวหลุดออกมาจากปากเธอ"

# "As I open my mouth to comfort her, I see the barely visible red drops from between her legs."
"จังหวะที่ฉันกำลังจะพูดปลอบเธอนั้นสายตาก็เหลือบไปเห็นหยดสีแดงหยดเล็ก ๆ ตรงหว่างขาเธอ"

# hi "Lilly, if it's too much…"
hi "ลิลลี่ ถ้าเธอไม่ไหว…"

scene evh lilly_cowgirl_strain_small
with charachange

# "She clenches her mouth tightly, quickly and forcefully shaking her head from side to side in defiance. After a couple of seconds she relaxes her body slightly, though she's still obviously far from being comfortable."
"เธอเม้มปากแน่นแล้วสั่นหัวปฏิเสธแรง ๆ ไปมา ไม่นานเธอก็คลายความเกร็งลงเล็กน้อย แต่ก็ชัดอยู่ว่ายังไม่ได้หายเกร็ง\nโดยสมบูรณ์"

# li "I… it's okay… I'm okay."
li "ไม่… เป็นไร… ฉันยังไหว"

scene evh lilly_cowgirl_frown_small
with charachange

# "She swallows hard, trying to collect herself."
"ลิลลี่กลืนน้ำลายอึกใหญ่สงบใจตัวเอง"

# "Lifting herself slowly and bringing herself back down, she relaxes a little more as the feelings of pleasure begin to overtake those of pain."
"เธอยกตัวขึ้นช้า ๆ แล้วลดตัวลงอีกครั้ง เมื่อความสุขสมเข้าทับถมความเจ็บปวดเหล่านั้นเธอจึงคลายความเกร็งลงได้อีก\nเล็กน้อย"

scene evh lilly_cowgirl_strain_small
with charachange

# "Her breathing starts to match the same ragged patterns as mine, her body moving almost teasingly slowly. She looks as if she's slowly beginning to enjoy the act, my feelings finally reaching her."
"ลมหายใจของเธอเริ่มขาดห้วงไปเหมือนอย่างฉัน เธอขยับตัวได้ช้าจนฉันแทบขาดใจ ดูเหมือนว่าเธอเองก็เริ่มจะสุข\nไปกับกิจกรรมนี้แล้ว ความรู้สึกของฉันส่งไปถึงเธอเสียที"

# "I'm not sure if she's keeping herself at this speed for her sake or for mine, but either way… with this slow and steady pace, I think I can… keep my body in check. It's funny, in a way, that even now I'm depending on her."
"ฉันไม่แน่ใจนักว่าเธอทำความเร็วเท่านี้เพื่อตัวเธอเองหรือเพื่อฉันกันแน่ แต่จะเพื่อใคร… ถ้าทำแบบช้า ๆ เรื่อย ๆ แบบนี้\nร่างกายฉัน… น่าจะพอไหวอยู่ จะว่าไปแล้วก็ตลกดีที่แม้แต่ตอนนี้ฉันก็ยังต้องพึ่งเธออีก"

# "For us to be joined together like this, our feelings so close… it makes me glad. To be sharing our first moment together like this… is an almost… overwhelming… feeling…"
"ฉันดีใจ… ที่เราสองคนได้เชื่อมประสานถึงกันโดยที่ความรู้สึกนั้นตรงกัน ได้ทำครั้งแรกร่วมกันอย่างนี้… มันช่าง…\nสุขล้น… เหลือเกิน…"

# hi "I love you… Lilly…"
hi "ฉันรักเธอนะ… ลิลลี่…"

scene evh lilly_cowgirl_cry_small
with charachange

# li "Hisao… Hisao…!"
li "ฮิซาโอะ… ฮิซาโอะ…!"

# "I can feel her body tensing, her breathing and movements becoming steadily less carefully controlled. I'm happy to be making her feel so good, but as my thoughts become increasingly focused, I can feel myself rapidly nearing my limit."
"ฉันสัมผัสได้ถึงร่างกายเธอที่หดเกร็ง ทั้งลมหายใจและการขยับตัวของเธอเร็วขึ้นเรื่อย ๆ ดีใจจริง ๆ ที่ฉันทำให้เธอ\nรู้สึกดีได้ขนาดนี้ แต่ยิ่งจดจ่อก็ยิ่งรู้สึกได้ถึงตัวฉันที่เข้าใกล้ขีดจำกัดอย่างรวดเร็ว"

scene white
with Dissolve(3.0)

# "Control of my body is instantaneously wrested from my mind as I grit my teeth hard, a loud moan escaping as I climax and my hips hit hers. Her body hunches over at the same moment, her breasts touching on my chest."
"ฉันไม่อาจควบคุมร่างกายตัวเองได้อีกต่อไป ฉันกัดฟันกรอดครางต่ำเมื่อยกสะโพกเข้าหาตัวเธอแล้วปล่อยให้ตัวเอง\nไปถึงฝั่ง เธอเองก็โน้มตัวเข้ามาจนหน้าอกของเธอแนบกับหน้าอกของฉัน"

# "We stay locked in all-encompassing ecstasy for a brief moment, my mind completely taken by the feeling for a precious few seconds."
"พวกเราปล่อยให้ตัวเองติดตรึงไปกับความหวามไหวซึ่งแผ่ซ่านนั้นอยู่ครู่หนึ่ง ในสมองฉันเต็มไปด้วยความรู้สึกจาก\nชั่วขณะอันหอมหวานนั้น"

scene evh lilly_cowgirl_weaksmile_small
with charachange

# "It ends all too soon and our bodies collapse in exhaustion with Lilly barely staying on top of me."
"กิจกรรมจบลงไปอย่างรวดเร็ว ร่างของพวกเราทรุดลงด้วยความเหนื่อยอ่อน ลิลลี่ยังคงนอนทับอยู่บนตัวฉัน"

# "I lifelessly manage to wrap my arms around her limp, sweating body, and for minutes we simply lay there, silently savoring the contact with each other while we recover from the experience."
"ฉันยกแขนขึ้นโอบร่างอาบเหงื่อไร้เรี่ยวแรงของเธออย่างหมดแรง พวกเรานอนนิ่ง ๆ อยู่อย่างนั้นหลายนาที คอยดื่มด่ำ\nสัมผัสของกันและกันอยู่เงียบ ๆ พลางตั้งสติจากเหตุการณ์เมื่อครู่"

# "Neither of us had thought ourselves prepared for such a thing, of that much I'm certain."
"สิ่งหนึ่งที่ฉันแน่ใจคือ พวกเราต่างไม่มีใครได้เตรียมใจกับเหตุการณ์เช่นนั้นเลย"

# "Entirely drained, far past the point of conversation, I look at her tired face. It looks as if the exertion, both physical and mental, has almost forced her to the verge of collapse."
"ฉันมองใบหน้าอันอ่อนเพลียของเธอ ตอนนี้ฉันไม่มีแรงแม้แต่จะพูดคุยอะไรแล้ว ดูท่าว่าการที่เธอต้องออกแรงกาย\nและใช้ความคิดอย่างหนักนั้นจะทำให้เธออ่อนเปลี้ยจนแทบขยับตัวไม่ไหว"

# hi "I love you, Lilly."
hi "ฉันรักเธอนะลิลลี่"

scene evh lilly_cowgirl_smile_small
with charachange

# "She nods weakly, rubbing my hair with her left hand. If we could simply remain together like this for an eternity, it would be a paradise like no other."
"ลิลลี่พยักหน้าเบา ๆ พลางใช้มือซ้ายของเธอลูบหัวฉัน ถ้าหากเราสองคนอยู่ด้วยกันเช่นนี้ได้ไปชั่วนิรันดร์ เท่านั้น\nเราคงมีความสุขยิ่งกว่าอะไร"

stop music fadeout 2.0

scene black
with dissolve

#**************************************

label th_L18:

scene bg hok_lounge_rn
with locationchange

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_rain fadein 1.0

# "After being woken by a sound, I open my eyes with a measure of reluctance."
"ฉันลืมตาตื่นด้วยความไม่เต็มใจนักเพราะได้ยินเสียงบางอย่าง"

# "Turning my head to the left, I find the rain outside sweeps against the windows loudly. Spray after wind-blown spray lashes against the glass, as if trying its hardest to make up for the summer's previous heat."
"พอหันมองไปทางด้านซ้ายก็เห็นฝนที่ซัดสาดใส่หน้าต่างจนเกิดเสียงซ่า ลมที่ตีม่านฝนเข้ามากระทบกับหน้าต่างนั้น\nพัดรุนแรงราวกับจะชดเชยความร้อนจากฤดูร้อนเมื่อก่อนหน้านี้"

# "I sit up in the futon, holding the back of my neck to try and subdue the pain from my awkward sleeping position."
"ฉันลุกขึ้นนั่งกับฟูกฟูตงแล้วนวด ๆ ท้ายทอยบรรเทาความปวดจากการนอนด้วยท่าที่ผิดธรรมชาติ"

# "By all accounts I should be lamenting the turn in the weather, given that this is our last day here. The events of yesterday refuse to stop flooding my mind, though."
"ถ้าว่าตามจริงแล้วฉันต้องเสียดายที่สภาพอากาศดันมาเป็นอย่างนี้ เพราะวันนี้เป็นวันสุดท้ายแล้วที่จะได้อยู่ที่นี่ แต่\nเหตุการณ์เมื่อวานยังคงวนเวียนอยู่ในความคิดไม่ไปไหน"

# "The feeling of holding Lilly's crying body in my arms. The rush of lust and hormones that flowed through us as we spent the night together. It seems almost futile to try and rationalize everything that happened."
"ความรู้สึกที่ได้โอบกอดลิลลี่ที่ร้องไห้ ความรู้สึกที่ความใคร่กับฮอร์โมนแล่นพล่านไปทั่วตัวขณะที่เราได้หลับนอนด้วยกัน\nทุกอย่างที่เกิดขึ้นนั้นคงไม่อาจใช้เหตุผลอะไรมาอธิบายได้"

# "In an attempt to distract myself, I groan and lean over to retrieve my bag without standing. Pulling out one bottle after another, I take the daily regimen's worth of pills from their containers and swallow them without further ado."
"ฉันร้องโอดโอยเอี้ยวตัวไปหยิบกระเป๋าโดยที่ไม่ลุกเพื่อเป็นการเบนความสนใจของตัวเองก่อนจะหยิบขวดยาต่าง ๆ\nออกมาแล้วเทเม็ดยาตามปริมาณที่ต้องกินเป็นประจำทุกวันออกมาจากแต่ละขวดและกลืนยาไปโดยทันที"

$ renpy.music.set_volume(0.1, 1.0, channel="ambient")

window hide
nvl show dissolve

nvl clear

# n "\n\n\n\nIt took a surprisingly short amount of time to get used to swallowing pills without water. That said, I suppose the same thing goes for getting used to living in a school for disabled students."
n "\n\n\n\nฉันชินกับการกินยาโดยที่ไม่ต้องกินน้ำตามได้อย่างเร็วเหลือเชื่อ แต่ก็นะ ฉันเองก็ชินกับการอยู่ในโรงเรียนสำหรับ\nนักเรียนพิการได้อย่างเร็วเหลือเชื่อเหมือนกัน"

# n "Remembering Yamaku, I become all the more grateful for having the chance to get away, even if it's just for the shortest of times."
n "พอนึกถึงยามากุแล้วฉันก็นึกยินดีที่ได้ปลีกตัวออกมาจากตรงนั้น แม้จะเป็นเพียงระยะเวลาสั้น ๆ ก็ตาม"

# n "I appreciate the chance to spend time alone with Lilly and Hanako, away from the bustle of school life, even considering the latest complications."
n "ฉันรู้สึกยินดีที่ตัวเองมีโอกาสได้ใช้เวลาอยู่ห่างจากความวุ่นวายของชีวิตในโรงเรียนด้วยกันกับลิลลี่กับฮานาโกะ\nตามลำพัง ถึงจะมีเหตุการณ์อย่างเมื่อคืนเกิดขึ้นก็เถอะะ"

# n "I never thought I'd say it, but the idea of living away from the city in a nice, tranquil area is an inviting one. It's a thought that, barely a year ago, would have seemed simply ludicrous."
n "ฉันไม่เคยคิดเลยว่าตัวเองจะมาคิดอย่างนี้ได้ แต่ฉันอยากไปอาศัยอยู่ในพื้นที่ดี ๆ ที่เงียบสงบ อยู่ห่างไกลจากตัวเมือง\nซึ่งเป็นความคิดที่ถ้าตัวฉันเมื่อสักหนึ่งปีที่แล้วได้ยินก็คงบอกว่าไร้สาระ"

$ renpy.music.set_volume(0.2, 1.0, channel="ambient")

nvl clear
nvl hide dissolve

window show

# "A flash of pink, no doubt Hanako's gown, peeks from around the corner. Realizing I must look a sight since I've only just woken up, I slap the remaining pills into my mouth and run a hand through my hair."
"ตรงมุมผนังมีผ้าสีชมพูแวบออกมา ซึ่งก็คงเป็นชุดของฮานาโกะนั่นแหละ สภาพฉันที่เพิ่งตื่นตอนนี้คงดูไม่ได้แน่ ๆ\nฉันรีบยัดยาที่เหลือเข้าปากแล้วใช้มือสาง ๆ ผม"

show hanagown smile_rn at center
with charaenter

# ha "Good morning, Hisao."
ha "อรุณสวัสดิ์ ฮิซาโอะ"

# hi "Ah, go— ack!"
hi "อ๊ะ อรุ— อ่อก!"

$ renpy.music.set_volume(0.0, 0.2, channel="ambient")

with vpunch

# "I reply to her completely forgetting that I'm in the middle of swallowing a particularly large pill. Coughing and spluttering, I violently gag on it."
"ฉันตอบฮานาโกะไปโดยยังไม่ทันนึกได้ว่ากำลังกลืนเม็ดยาที่ค่อนข้างใหญ่อยู่ ฉันสำลักไอค่อกแค่กไม่หยุด"

show hanagown worry_rn
with charachange

# ha "Ah, Hisao!"
ha "อ๊ะ ฮิซาโอะ!"

$ renpy.music.set_volume(0.2, 10.0, channel="ambient")

# "After sputtering loudly and tapping my chest a couple of times to force it down, I manage to recover."
"พอไอโขลกไปพร้อมทุบหน้าอกตัวเองสองสามครั้งให้เม็ดยาหลุดลงไปแล้วฉันก็กลับมาตั้งตัวได้"

# hi "I'm fine. Sorry, forgot I was swallowing."
hi "ไม่เป็นไร ขอโทษที พอดีลืมว่ากินยาอยู่"

play music music_happiness fadein 5.0

show hanagown distant_rn
with charachange

# ha "Sorry, I didn't mean to—"
ha "ขอโทษนะ พอดีฉันไม่ได้ตั้ง—"

# "I hold my hand up, gesturing for Hanako to stop."
"ฉันยกมือปรามฮานาโกะ"

# hi "I gagged. It's my fault. 'Morning, Hanako."
hi "ฉันสำลักเองน่า รุณสวัสดิ์ ฮานาโกะ"

# "She pauses a moment before bowing in reply."
"ฮานาโกะเงียบไปครู่หนึ่งแล้วโค้งตัวตอบ"

show hanagown distant_rn at tworight
show bg hok_lounge_rn at bgright
with charamove

show lilly basic_sleepy_paj_rn at twoleft
with charaenter

# "Walking, no, staggering in behind Hanako is the familiar figure of Lilly, also dressed in her pajamas. With her eyes full of sleep and hair bedraggled, she's a sight to behold."
"ส่วนเงาลิลลี่อันคุ้นเคยที่เดิน ไม่สิ โซเซอยู่หลังฮานาโกะนั้นก็ใส่ชุดนอนเช่นกัน เธอทำตาปรือด้วยความงัวเงีย ผมเผ้า\nยังรุงรัง เป็นภาพที่น่าดูชมทีเดียว"

# hi "Hi, Lilly."
hi "ไงลิลลี่"

show lilly basic_weaksmile_paj_rn at twoleft
with charaenter

# li "Good morning… Hisao."
li "อรุณสวัสดิ์… ฮิซาโอะ"

# "For a while, a silence hangs in the air as neither of us knows what to do."
"เราสามคนนิ่งเงียบค้างไปเพราะต่างคนต่างทำตัวไม่ถูก"

# "Given what happened last night, we both have more than enough reason to be finding the situation awkward; just how are we meant to react to meeting each other after something like… that?"
"เราสองคนต่างรู้สึกกระอักกระอ่วนกับสถานการณ์ในตอนนี้เพราะเรื่องเมื่อคืน เวลาอยู่ด้วยกันแล้วจะให้ทำตัวยังไง\nก็พวกเรา… กันไปแล้ว"

# "The best course of action would probably be to talk to Lilly alone, to set things in order."
"ทางเลือกที่ดีที่สุดคงจะเป็นการคุยกับลิลลี่ตัวต่อตัวเพื่อจัดการให้อะไร ๆ ลงตัว"

# hi "Um, I'll… start making breakfast."
hi "เอ่อ เดี๋ยวฉัน… ไปทำข้าวเช้านะ"

# "Lilly evidently catches on to my train of thought."
"ชัดว่าลิลลี่เองก็รู้ว่าฉันคิดอะไรอยู่"

show lilly basic_smileclosed_paj_rn
with charachange

# li "I'll help. Hanako, could you set the table?"
li "เดี๋ยวฉันไปช่วยทำนะ ฮานาโกะ เธอไปจัดโต๊ะให้หน่อยได้หรือเปล่า"

# "She nods, her head disappearing into a cupboard as she quickly goes about her assigned task."
"ฮานาโกะพยักหน้าแล้วมุดตู้เก็บของเพื่อทำตามหน้าที่ที่ได้รับมอบหมาย"

$ renpy.music.set_volume(0.1, 0.5, channel="ambient")

scene bg hok_kitchen_rn
with locationchange

# "I rub a little more sleep out of my eyes as I wander over to the fridge and take out some milk, and Lilly grabs various brightly colored boxes from some of the lower cupboards to my side."
"ฉันขยี้ตาให้ตื่นตัวขึ้นอีกหน่อยพลางเดินไปหยิบนมในตู้เย็น ส่วนลิลลี่ก็หยิบกล่องสีสดใสหลายกล่องออกมาจาก\nตู้เก็บของด้านล่างตู้หนึ่งที่อยู่ข้างฉัน"

# "While we make the rather bland-looking meal, I whisper somewhat more quietly than usual. Knowing Lilly's hearing, she won't have any trouble catching what I say."
"พวกเราจัดแจงมื้ออาหารซึ่งดูค่อนข้างเรียบง่าย ฉันกระซิบเสียงแผ่วกว่าปกติคุยกับลิลลี่ เธอคงได้ยินแน่ ๆ ละ เพราะเธอ\nหูดีขนาดนั้น"

# hi "Are you okay, Lilly? After last night…"
hi "ไหวมั้ยลิลลี่ เมื่อคืน…"

show lilly basic_reminisce_paj_rn at center
with charaenter

# "She gives a delicate nod, her expression weak."
"ลิลลี่พยักหน้าเบา ๆ สีหน้าของเธอคล้ายไม่มีเรี่ยวแรง"

# "Though her tiredness surely plays a part, she seems genuinely unsure about what's happened between us, and how to move ahead. I can't say I blame her, considering my feelings are the same."
"ถึงส่วนหนึ่งจะเป็นเพราะความเหนื่อยอ่อนก็จริง แต่เธอก็ดูไม่แน่ใจจริง ๆ กับสิ่งที่เกิดขึ้นระหว่างเรา และไม่รู้ว่าจะต้อง\nทำยังไงต่อ จริง ๆ จะว่าเธอก็ไม่ได้หรอก เพราะฉันเองก็รู้สึกอย่างนั้นเหมือนกัน"

show lilly basic_sad_paj_rn
with charachange

# li "I'm sorry, Hisao. I wasn't thinking straight yesterday. I never stopped to consider you or Hanako, and I even went as far as…"
li "ขอโทษนะฮิซาโอะ เมื่อวานสติฉันไม่อยู่กับตัวเลย ฉันไม่แม้แต่จะฉุกคิดถึงเธอหรือฮานาโกะ แล้วฉันยังถึงขั้น…"

# "She's winding herself up. With her hands and voice both tightening, I give her a gentle bump to try and lighten up the situation."
"ลิลลี่ตระหนกหนัก น้ำเสียงเธอฟังดูเกร็ง มือของเธอก็เกร็งเช่นกัน ฉันถองศอกใส่เธอเบา ๆ ด้วยหวังไม่ให้บรรยากาศ\nเครียดเกินไป"

# hi "You don't have to apologize. I said I liked you as well, after all."
hi "ไม่ต้องขอโทษหรอก ฉันก็บอกแล้วนี่ว่าฉันก็ชอบเธอเหมือนกัน"

show lilly basic_oops_paj_rn
with charachange

# li "But I…"
li "แต่ฉัน…"

# "As her composure begins to falter, it becomes obvious there's no alternative."
"ลิลลี่เริ่มร้อนรน แปลว่าฉันไม่มีทางเลือกอื่นแล้ว"

show lilly basic_sad_paj_close_rn
with characlose

# "Turning to Lilly, I gently embrace her tall frame. She offers no resistance at all, thankfully pulling back, just, from the edge of her emotions."
"ฉันหันไปทางลิลลี่แล้วโอบกอดร่างสูงของเธอ เธอไม่ขัดขืนเลย และโชคดีที่เธอกลับมาใจเย็นลงได้ก่อนที่เธอจะ\nปั่นป่วนใจไปกว่านี้"

show lilly basic_sad_paj_close_rn at twoleft
show bg hok_kitchen_rn at bgleft
with charamove

show hanagown normal_rn at tworight
with charaenter

# "Despite our reassuring embrace lasting only a matter of seconds, I notice Hanako wordlessly watching. The plate in her hand hovers inches above the table, her action halted midway by the sight."
"แม้จะกอดปลอบลิลลี่อยู่ไม่นาน ฉันก็เห็นฮานาโกะที่กำลังมองเงียบ ๆ อยู่ เธอถือจานลอยค้างจากโต๊ะไปไม่กี่เซนติเมตร\nไม่ทันวางเพราะเห็นภาพเราสองคนกอดกันเสียก่อน"

stop music fadeout 2.0

scene bg hok_lounge_rn
show hanagown distant_rn:
    tworight
    ypos 1.15
show lilly basic_sleepy_paj_rn:
    twoleft
    ypos 1.17
with shorttimeskip

$ renpy.music.set_volume(0.2, 0.5, channel="ambient")

# "The clatter of utensils against plates is the only sound to be heard as we silently eat. Whereas before only two of us may have been unsure of ourselves, the entire situation has changed."
"พวกเรากินอาหารกันอย่างเงียบ ๆ โดยมีเพียงเสียงอุปกรณ์การกินที่กระทบกับจานดังแทรก ก่อนหน้านี้พวกเราสองคน\nคงไม่แน่ใจในความรู้สึกของตัวเอง แต่ตอนนี้สถานการณ์ได้เปลี่ยนไปแล้ว"

# "After weeks of blissful friendship, whiling away the days with shared meals and chatter with little meaning, the relationship of Lilly and me, no, that of all of us, has irreversibly changed."
"มิตรภาพอันแสนสุขในช่วงหลายสัปดาห์ อยู่กินข้าวด้วยกันทุกวันคุยกันเรื่อยเปื่อยไม่มีสาระอะไร มิตรภาพระหว่างลิลลี่\nกับฉัน ไม่สิ ระหว่างเราสามคนได้เปลี่ยนแปลงไปอย่างไม่อาจย้อนคืน"

# "I can't take this."
"ทนไม่ไหวแล้ว"

# hi "Lilly…"
hi "ลิลลี่…"

stop ambient fadeout 25.0

show lilly basic_listen_paj_rn
with charachange

# "She solemnly nods, gently laying her spoon onto the plate in front of her. Neither of us knows exactly how we regard each other, let alone how Hanako would view us."
"ลิลลี่พยักหน้าจริงจังแล้ววางช้อนลงบนจานตรงหน้าเธออย่างเบามือ เราสองคนต่างไม่รู้ว่าอีกฝ่ายมองตัวเองอย่างไร\nและไม่รู้ด้วยซ้ำว่าฮานาโกะจะมองตัวพวกเราอย่างไรด้วย"

show lilly basic_weaksmile_paj_rn
with charachange

# li "This might seem abrupt but… I've confessed to Hisao."
li "ออกจะกะทันหันไปสักหน่อย แต่ว่า… ฉันสารภาพรักกับฮิซาโอะแล้วนะ"

show hanagown distant_blush_rn
with charachange

# "For a moment, Hanako looks almost confused; precisely the reaction I'd thought she would have. She eventually nods, her spoon still in her mouth as she does."
"ฮานาโกะดูค่อนข้างสับสนอยู่ครู่หนึ่ง ซึ่งฉันก็คิดไว้แล้วว่าเธอต้องทำหน้าอย่างนี้แน่ แต่สุดท้ายเธอก็พยักหน้าโดยที่ยัง\nคาบช้อนไว้ในปากอยู่"

show hanagown normal_blush_rn
with charachange

# ha "Did you accept?"
ha "แล้วนายรับรักมั้ย"

# hi "I did."
hi "รับ"

show hanagown smile_rn
with charachange

# "She gives a smile so large, and so earnest, I find myself blushing. I think it's the brightest I've ever seen her expression look."
"ฮานาโกะยิ้มกว้างอย่างจริงใจจนฉันหน้าแดง รอยยิ้มนี้คงเป็นรอยยิ้มที่สดใสที่สุดเท่าที่ฉันเคยเห็นฮานาโกะยิ้มมาเลย"

play music music_serene fadein 6.0

# ha "Then I'm happy. I'm really, really happy."
ha "งั้นก็ดีแล้วละ ฉันมีความสุขมาก ๆ เลย"

show lilly basic_sleepy_paj_rn
with charachange

# li "I'm sorry for not telling you anything about it before. Things have been…"
li "ขอโทษที่ก่อนหน้านี้ไม่ได้บอกนะ พอดีเรื่องมัน…"

# "Hanako shakes her head from side to side emphatically, apparently forgetting in her rush that Lilly couldn't possibly notice."
"ฮานาโกะสั่นหัวด้วยความเข้าใจ ซึ่งเหมือนเธอจะไม่ทันคิดว่าอย่างไรลิลลี่ก็คงมองไม่เห็น"

show hanagown distant_blush_rn
with charachange

# "She begins fiddling with her fingers, looking a little more nervous than she did before."
"เธอจับนิ้วตัวเองเล่นดูประหม่ากว่าเมื่อครู่"

# ha "To be honest, I began to think you might like each other a while ago. At first I didn't really know what to think about it… but I…"
ha "เอาจริง ๆ ฉันก็คิดมาสักพักแล้วว่าเธอสองคนชอบกันหรือเปล่า ตอนแรกฉันก็ไม่รู้เหมือนกันว่าจะรู้สึกยังไงดี…\nแต่ฉัน…"

show hanagown smile_rn
with charachange

# ha "I decided in the end that… if my friends are happy, then I'm happy."
ha "ฉันก็คิดเอาว่า… ถ้าเพื่อนฉันมีความสุข ฉันก็มีความสุข"

# ha "I was really glad to have another friend when we met Hisao, so you finding love through him is even better… right?"
ha "ฉันดีใจมากที่เราได้เพื่อนใหม่ตอนที่เจอฮิซาโอะ เพราะงั้น การที่เธอได้รู้จักคำว่ารักเพราะเขาก็ยิ่งดีไปอีก… ใช่มั้ย"

# "A feeling of relief at her acceptance of our relationship falls over me like a wave. The same happens to Lilly, judging by her expression."
"ฉันโล่งใจเป็นอย่างมากที่ฮานาโกะยอมรับความสัมพันธ์ของพวกเรา ดูจากสีหน้าแล้ว ลิลลี่ก็คงรู้สึกไม่ต่างกัน"

show lilly basic_weaksmile_paj_rn
with charachange

# li "Thank you, Hanako. I really appreciate you being so understanding."
li "ขอบคุณนะฮานาโกะ ฉันดีใจมากที่เธอเข้าใจ"

show hanagown distant_rn
with charachange

# "Lilly's voice still sounds slightly apologetic, or at least unsure. This doesn't escape Hanako, who appears lost in thought for a few moments before turning to me."
"น้ำเสียงลิลลี่ยังฟังดูคล้ายเป็นการขอโทษอยู่เล็กน้อย หรือไม่ก็เป็นความไม่แน่ใจ ซึ่งฮานาโกะที่เหมือนคิดอะไรอยู่ครู่หนึ่ง\nก็จับน้ำเสียงนั้นได้แล้วหันมาทางฉัน"

show hanagown smile_rn
with charachange

# ha "Hisao, do you mind if Lilly and I go outside for a bit?"
ha "ฮิซาโอะ ขอฉันกับลิลลี่ออกไปข้างนอกด้วยกันสักหน่อยได้มั้ย"

# hi "Ah, no, feel free…"
hi "อ้อ ได้สิ ตามสบาย…"

show lilly basic_surprised_paj_rn
with charachange

# li "Hanako?"
li "ฮานาโกะ?"

show hanagown smile_rn at tworight
with charamove

show lilly basic_surprised_paj_rn at twoleft
with charamove

hide lilly
hide hanagown
with charaexit

stop ambient
$ renpy.music.set_volume(1.0, 0.0, channel="ambient")

# "Hanako gets up from her seat, taking Lilly's hand and almost dragging her from the table in her excitement. Considering Lilly's typically slow and steady pace, Hanako's haste makes her footing awkward and she almost loses her balance a couple of times."
"ฮานาโกะลุกจากเก้าอี้แล้วจับมือลากตัวลิลลี่ไปจากโต๊ะด้วยความตื่นเต้น ลิลลี่ซึ่งปกติจะเดินอย่างช้า ๆ และสม่ำเสมอนั้น\nเดินไปแบบแปลก ๆ จนแทบจะเสียการทรงตัวอยู่บ้างเมื่อฮานาโกะลากตัวไปด้วยความเร่งรีบ"

# "It's a pretty amusing sight, leaving me wordless as I watch them disappear out the door. It's only now that I realize the rain's stopped, being replaced by a sky seemingly all the more vivid and bright to make up for the morning's drab gray expanse."
"ดูแล้วก็ตลกดี ฉันมองพวกเธอสองคนออกไปทางประตูเงียบ ๆ และฉันก็เพิ่งรู้ตัวว่าฝนหยุดแล้ว ท้องฟ้าใสสว่าง\nเข้ามาแทนที่ราวกับจะชดเชยความหมองหม่นจากผืนฟ้าเมื่อเช้านี้"

# "For Hanako, this must be a pretty big revelation. Lilly and I are really the only people she associates with, almost as if we were parents in her own's stead."
"ข่าวนี้คงเป็นข่าวใหญ่ทีเดียวสำหรับฮานาโกะ ลิลลี่กับฉันเป็นคนกลุ่มเดียวที่เธอคลุกคลีด้วยจนคล้ายว่าพวกเราเป็น\nพ่อแม่ที่เข้ามาทดแทนพ่อแม่จริง ๆ ของเธอ"

# "I suppose that might well be the best way to describe the relationship we share. A father, mother and daughter, all playing around in our little make-believe family as if it could last forever."
"ถ้าให้ว่าแล้ว ความสัมพันธ์ของพวกเราก็คงเป็นอย่างนั้นนั่นแหละ พ่อ แม่ ลูก อยู่เล่นเป็นครอบครัวด้วยกันราวกับว่า\nจะเล่นบทบาทเช่นนี้ไปได้ตลอดกาล"

# "It might be a strange dynamic, and one that certainly can't last for long… but maybe, just for this one small moment, it's okay."
"อาจจะเป็นความสัมพันธ์ที่พิลึก และเป็นความสัมพันธ์ที่อย่างไรก็อยู่ได้ไม่นาน… แต่ว่า เพียงได้เป็นอย่างนี้ ณ\nชั่วขณะนี้ ก็คงนับว่าดีแล้ว"

# "As I stand from the table and go to join Lilly and Hanako in the fields outside, I nod to myself in affirmation."
"ฉันลุกเดินออกจากโต๊ะไปหาลิลลี่กับฮานาโกะที่อยู่กลางทุ่งด้านนอกพลางพยักหน้าให้ความมั่นใจกับตัวเอง"

# "This one small moment of happiness, no matter how brief, will last with me, with all of us, forever."
"ความสุข ณ ชั่วขณะสั้น ๆ นี้—ไม่ว่าจะสั้นเพียงใด—จะอยู่ในใจฉัน ในใจพวกเราทุกคน ไปตลอดกาล"

stop music fadeout 2.0

label th_L19:

scene bg hok_bath
show steam
with shorttimeskip

# "Submerged deep in the hot water, I let a drawn-out sigh escape my lips. The feeling of seemingly every muscle in my body relaxing is euphoric."
"ฉันนอนแช่น้ำร้อนแล้วถอนหายใจยาว ความรู้สึกที่ได้ผ่อนคลายกล้ามเนื้อตอนแช่น้ำร้อนนี่สบายตัวเสียจริง"

# "I have no idea how long it's been since I had a genuine hot bath, but right now I can hardly be bothered trying to remember."
"ลืมไปแล้วเหมือนกันว่าตัวเองได้แช่น้ำร้อนครั้งล่าสุดจริง ๆ ตอนไหน แต่ตอนนี้ก็ขี้เกียจคิดแล้ว"

play music music_dreamy fadein 2.0

nvl clear
window hide

nvl show dissolve

# n "Maybe I'm giving the simple fact that for once I get to have a real bath more credit than it's due; the chance to just calm down, allow myself to unwind and have some time to myself is a welcome one."
n "ฉันอาจจะแค่คิดได้ว่าคราวนี้ฉันได้อาบน้ำแบบจริง ๆ สักครั้ง เป็นการอาบน้ำที่เปิดโอกาสให้ฉันได้มีเวลาอยู่กับตัวเอง\nอยู่แบบสบาย ๆ อย่างผ่อนคลาย ซึ่งฉันยินดีที่ได้อาบน้ำอย่างนี้"

# n "Hanako, Lilly and I wandered about outside, exploring the extent of the surprisingly large tract of land surrounding the house. Then we spent the majority of the afternoon resting, watching television, reading, and playing cards."
n "ฮานาโกะ ลิลลี่ แล้วก็ฉันเดินเล่นด้วยกันข้างนอกสำรวจอาณาบริเวณรอบบ้านซึ่งกว้างกว่าที่คาด จากนั้นพวกเราก็มา\nพักผ่อนกันตอนบ่าย ดูโทรทัศน์ อ่านหนังสือ เล่นไพ่กัน"

# n "It may not have been the most exciting finale to the trip, but such tranquil peacefulness is something to savor. Even after we return to the school tomorrow, I think I'll remember this little house in Hokkaido for a long time."
n "อาจจะไม่ใช่การปิดท้ายวันหยุดที่หวือหวามากนัก แต่การได้อยู่อย่างสบายเงียบสงบเช่นนี้ก็เป็นอะไรที่ดีเช่นกัน แม้พรุ่งนี้\nเราจะต้องกลับไปที่โรงเรียนกันแล้ว แต่ฉันคงจะยังจดจำบ้านหลังเล็กที๋ฮกไกโดแห่งนี้ไปอีกนานแสนนาน"

# n "It's a pity we only have a couple more hours to spend here before going to get the train back."
n "น่าเสียดายที่อีกไม่กี่ชั่วโมงเราจะต้องขึ้นรถไฟขาล่องกลับกันแล้ว"

# n "All I can do is yawn contentedly while I watch the steam slowly rising from the clear water's placid surface, my eyes eventually locking onto the ceiling."
n "ฉันได้แต่หาวด้วยความอิ่มใจแล้วมองไอน้ำที่ลอยจากผิวน้ำที่เรียบนิ่ง สุดท้ายฉันก็หันไปมองที่เพดาน"

# n "Our exams are imminent. I've barely studied at all for them."
n "ใกล้สอบแล้ว แต่ฉันยังไม่ได้อ่านหนังสืออะไรเท่าไหร่เลย"

# n "On top of that, I don't even know what I'll do after graduation. Passing exams is all well and good, but to what end?"
n "แล้วยิ่งไปกว่านั้น ฉันยังไม่รู้เลยว่าพอเรียนจบแล้วจะเอายังไงต่อ สอบให้ผ่านน่ะก็ดีอยู่หรอก แต่ผ่านแล้วได้อะไรบ้าง"

# n "Also now, of all times, I'm getting into a relationship."
n "แล้วแถมยังมามีแฟนเอาจังหวะนี้อีก"

nvl clear
nvl hide dissolve
window show

# hi "What the hell am I doing?"
hi "นี่ฉันกำลังทำบ้าอะไรอยู่วะ"

"…"

# "…I guess I shouldn't think like that. What's done is done, and maybe this could be viewed as just another aspect of my new life that I'm working on."
"…แต่จะคิดอย่างนั้นก็คงไม่ได้ อะไรที่ทำลงไปแล้วจะย้อนกลับไปแก้ไขไม่ได้ แล้วบางทีสิ่งนี้ก็อาจจะเป็นอีกมุมหนึ่ง\nของชีวิตใหม่ที่ฉันกำลังสร้างขึ้นมาด้วยก็ได้"

# "I enjoy being with Lilly, and there's more to life than school and a career after all."
"ฉันชอบการได้อยู่กับลิลลี่ แล้วชีวิตคนเราก็ใช่ว่าจะมีแต่เรื่องเรียนและงานสักหน่อย"

# "As I busily attempt to rationalize all that's happened, I hear a series of raps on the door. I pick myself up and sit upright, trying to figure out the source."
"ระหว่างที่ฉันแก้ตัวกับเรื่องที่เกิดขึ้นเป็นพัลวันนั้นก็มีเสียงเคาะประตูเป็นจังหวะ ฉันขยับตัวลุกขึ้นนั่งหลังตรงหาต้นตอ\nของเสียง"

# "Three, no more and no less. Light yet assertive in their tapping, and timed regularly enough to tune a metronome. I'd be extremely surprised if it wasn't Lilly."
"เคาะสามครั้งพอดิบพอดี น้ำหนักการเคาะแต่ละครั้งนั้นมีการกำหนดชัดเจน และมีการเว้นจังหวะสม่ำเสมอเทียบได้กับ\nเมโทรโนม ถ้าไม่ใช่ลิลลี่ฉันคงประหลาดใจมาก"

# li "May I… come in?"
li "ขอเข้าไปหน่อย… ได้มั้ยจ๊ะ"

# "Yeah, it's Lilly."
"อืม ลิลลี่จริงด้วย"

# hi "I'm still in the bath, I'll be out in a sec."
hi "อาบน้ำอยู่ เดี๋ยวจะออกไปแล้ว"

# li "…I know."
li "…รู้จ้ะ"

stop music fadeout 3.0

# "The voice coming from the other side of the door freezes me. After a second's thought, I rest on the side of the bath and let my arms dangle over the side."
"พอได้ยินเสียงที่ดังมาจากอีกฟากประตูแล้วฉันเป็นต้องตกใจ ฉันคิดอะไรอยู่แวบหนึ่งแล้วขยับตัวมาอยู่ริมอ่างแล้ว\nห้อยแขนกับขอบอ่าง"

# "Despite trying my best to play it off, I can't help letting my mind wander."
"ถึงจะทำนิ่งไว้ แต่ในใจก็อดไม่ได้ที่จะคิดอะไร ๆ"

# hi "S-sure, come in."
hi "อะ อื้ม เข้ามาสิ"

show lilly basic_smileclosed_cas at Alphain(1.0), Slide(0.4, 0.5, 0.5, 0.5, 1.0)
with Pause(1.0)

# "With that she opens the door, slowly walking into the room and closing it behind her. She looks oddly calm, countering my racing heart."
"แล้วลิลลี่ก็เปิดประตูเดินเข้ามาอย่างช้า ๆ แล้วปิดประตู เธอดูใจเย็นแปลก ๆ ขัดกับฉันที่ใจเต้นแรงเหลือเกิน"

# hi "Ah… h-hey… Lilly."
hi "อ่า… งะ ไง… ลิลลี่"

play music music_one fadein 9.0

show lilly basic_smile_cas at center
with charachange

# li "Do you mind if I take a bath with you?"
li "เธอจะว่าอะไรมั้ยถ้าฉันจะขออาบน้ำด้วย"

# hi "I don't mind. Go ahead."
hi "ไม่ว่าครับ เอาเลย"

show lilly basic_listen_cas at center
with charachange

# "With a small nod she begins to lift her sweater off her shoulders, baring her chest little by little."
"ลิลลี่พยักหน้าก่อนจะถอดเสื้อคลุมออกเผยส่วนหน้าอกเธอออกมาทีละน้อย"

# hi "I could do that for you, if you'd like."
hi "ถ้าจะให้ฉันช่วยถอดก็ได้นะ"

show lilly basic_emb_cas at center
with charachange

# li "Refused."
li "ขอปฏิเสธ"

# hi "Why?"
hi "ทำไม"

show lilly basic_pout_cas at center
with charachange

li "…"

# "Her face shows she's still not overly comfortable with letting me attend to her. I can't say I blame her."
"สีหน้าของเธอบ่งบอกว่าเธอไม่ได้ชินกับการที่จะให้ฉันดูแลขนาดนั้น ซึ่งก็ว่าไม่ได้หรอก"

hide lilly
with charaexit

play sound sfx_rustling

# "She continues undressing, her shirt and skirt falling to the floor and leaving her in her white lace bra and panties. Eventually, she stands bare in the center of the room."
"ลิลลี่ยังคงถอดเสื้อผ้าต่อ เสื้อกับกระโปรงของเธอร่วงลงกับพื้นเผยให้เห็นยกทรงและกางเกงในลายลูกไม้สีขาว\nและสุดท้ายเธอก็ยืนตัวเปลือยอยู่กลางห้องน้ำ"

label th_L19h:

show lilly behind_sleepy_nak at center
with charachange

# "Compared to last time, it's a lot easier to take in her entire figure. It's a wonderful sight."
"คราวนี้ฉันมองร่างของเธอได้แบบไม่ประหม่ามากเท่าคราวที่แล้ว เป็นภาพที่งดงามจริง ๆ"

# li "Hisao?"
li "ฮิซาโอะ?"

# hi "Hmm?"
hi "หืม?"

show lilly behind_pout_nak at center
with charaenter

# li "You're thinking perverted thoughts, aren't you?"
li "คิดอะไรลามกอยู่ละสิ"

# hi "Give me a break, you're undressing in front of me."
hi "ถามอะไรแปลก ๆ ก็เธอมาถอดเสื้อผ้าต่อหน้าฉันเนี่ย"

show lilly behind_weaksmile_nak at center
with charachange

# "She furrows her brow in thought."
"ลิลลี่ขมวดคิ้วครุ่นคิด"

# li "I guess this would be somewhat more erotic for you than me."
li "ของแบบนี้คงดูเย้ายวนสำหรับเธอมากกว่าฉันละมั้ง"

# hi "Why?"
hi "ทำไม"

# hi "…Ah."
hi "…อ๊ะ"

show lilly behind_giggle_nak at center
with charachange

# "She gives a small, lighthearted chuckle, which seems to settle her nerves a little."
"ลิลลี่หัวเราะคิกคักน้อย ๆ ซึ่งเหมือนจะช่วยให้เธอใจเย็นลง"

show lilly behind_smile_nak at center
with charachange

# li "If this is too much for you, Hisao, I can come back later."
li "ฮิซาโอะ ถ้าแบบนี้มันแรงไปสำหรับเธอ ไว้ฉันค่อยมาหาอีกทีก็ได้นะ"

# hi "No, no, this is fine. I'm just a bit… well…"
hi "ไม่ ๆ ไม่เป็นไร ฉันแค่… เอ่อ…"

# hi "You're really beautiful, you know."
hi "เธอสวยมากเลยนะ รู้มั้ย"

show lilly behind_emb_nak at center
with charachange

# "My earnest comment draws a vivid red blush from Lilly."
"คำชมจริงใจของฉันทำให้เธอหน้าแดงก่ำขึ้นมา"

# li "Hisao…"
li "ฮิซาโอะ…"

# "I give a small grin. She's cute when she's taken off guard."
"ฉันหยัดยิ้มเล็กน้อย พอเธอโดนจู่โจมแบบไม่ทันตั้งตัวแล้วก็ดูน่ารักดี"

show lilly behind_smileclosed_nak at center
with charachange

# li "In any case, may I come in?"
li "ว่าแต่ว่า ขอแช่ด้วยได้มั้ยจ๊ะ"

# hi "Ah, sure."
hi "อ้อ ได้สิ"

hide lilly
with charaexit

# "I lean forwards and take her soft hands in mine, helping her over the side of the bath."
"ฉันโน้มตัวไปจับมืออ่อนนุ่มของเธอนำทางให้เธอข้ามขอบอ่างเข้ามา"

# "She feels out the side of the bathtub then slowly lowers herself in, my breath catching when she sits and leans her back onto my front, her legs inside mine. I'd expected her to sit at the other end."
"ลิลลี่จับไปตามขอบอ่างแล้วหย่อนตัวลงแช่น้ำ ฉันถึงกับหยุดหายใจไปชั่วครู่เมื่อเธอมานั่งเอาหลังพิงหน้าอกฉันแล้ว\nวางขาไว้ตรงระหว่างขาฉันทั้งสองข้าง นึกว่าจะไปนั่งแช่ที่อีกฝั่งเสียอีก"

scene evh lilly_bath_smile_small
with whiteout

# "Letting out a long breath to calm myself, I rest my arms on the sides of the bath as I struggle to control my urges."
"ฉันถอนหายใจยาวเพื่อสงบใจตัวเองแล้ววางแขนพาดขอบอ่างพลางควบคุมตัวเองไม่ให้ตื่นตัว"

# "Far from missing the sight of her… assets, the feeling of her body against mine is surprisingly relaxing. If Lilly's so sensitive to touch, it must be all the more so for her."
"สองตาเห็น… ส่วนเหล่านั้นอันอวบอิ่มของเธอแบบจะจะ แต่สัมผัสจากร่างกายของเธอที่แนบกับตัวฉันนั้น\nช่างผ่อนคลายเหลือเชื่อ และยิ่งลิลลี่เป็นคนประสาทสัมผัสไว เธอคงรู้สึกดีกว่าฉันเสียอีก"

# li "You run your baths quite hot, don't you?"
li "น้ำที่เธออาบนี่ร้อนน่าดูเลยนะ"

# hi "A bit. Do you want me to run some cold water to cool it down a bit?"
hi "นิดหน่อย จะให้เติมน้ำเย็นสักหน่อยมั้ยล่ะ"

# "She gives a small shake of her head."
"ลิลลี่สั่นหัวเบา ๆ"

# li "No, this is fine."
li "ไม่ต้องจ้ะ แบบนี้แหละ"

# hi "Okay."
hi "โอเค"

# "The conversation comes to an abrupt end, silence taking over."
"บทสนทนาจบลงไปอย่างรวดเร็ว มีเพียงความเงียบที่ตามมา"

show evh lilly_bath_emb_small
with charachange

# "A very long, and very awkward, silence."
"ความเงียบอันน่าอึดอัดที่ดำเนินอยู่เนิ่นนาน"

# li "Maybe this was a bit too…"
li "หรือแบบนี้มันจะ…"

# hi "Don't worry, it's okay."
hi "ไม่ต้องห่วง ไม่เป็นไรหรอก"

# "The situation only becomes even more awkward. As if to distract herself, Lilly runs her free hand over her legs while holding one over her breasts for modesty."
"สถานการณ์ยิ่งน่ากระอักกระอ่วนไปใหญ่ ลิลลี่ใช้มือข้างที่ยังว่างลูบขาตัวเองเล่นราวกับจะเบนความสนใจของตัวเอง\nส่วนมืออีกข้างนั้นปิดหน้าอกตัวเองไว้เพื่อความสุภาพ"

# "I sit idly watching the wall ahead of me and the rising steam, every now and again stealing a glimpse at her body."
"ฉันนั่งเหม่อมองกำแพงตรงหน้าที่มีไอน้ำซึ่งลอยขึ้นจากอ่างคั่นกลางอยู่โดยลอบมองร่างกายเธอเป็นระยะ ๆ"

# "The white of her skin glistens as she keeps sliding her hand over her legs, their length and tone all the more obvious."
"ระหว่างที่เธอลูบขาอยู่นั้นสีขาวจากผิวเธอก็เปล่งประกายออกมา ซึ่งยิ่งขับเน้นความยาวและสีผิวของขาเธอให้เด่นชัด"

# hi "You know, compared to Akira, you look a lot more foreign."
hi "จะว่าไป หน้าตาเธอดูเป็นฝรั่งมากกว่าพี่อากิระไปเยอะเลยนะ"

# li "I took after my mother's side, genetically. Akira took after my father's more."
li "ฉันได้แม่มาน่ะจ้ะ ส่วนพี่ได้พ่อมา"

# hi "I guess that makes sense. How on Earth did a native Scot and a Japanese businessman meet, anyway?"
hi "ก็คงเป็นอย่างนั้นละนะ แล้วคนสกอตแลนด์โดยกำเนิดไปเจอกับนักธุรกิจญี่ปุ่นได้ยังไงล่ะเนี่ย"

# li "My mother was a journalist. She met my father while he was at a conference in Inverness."
li "แม่ฉันเป็นนักข่าวน่ะจ้ะ ท่านได้เจอกับพ่อตอนที่พ่อไปประชุมที่อินเวอร์เนสส์"

# hi "Ah, I see. Taking after your Scottish side would also explain your height, I suppose."
hi "อ้อ อย่างนี้นี่เอง ความสูงเธอก็น่าจะได้แม่มาด้วยละนะ"

# "I look back down at her as she nods, and sigh at the ridiculousness of the situation."
"ฉันก้มมองลิลลี่ที่พยักหน้าอยู่แล้วถอนหายใจให้กับความบ้าบอของสถานการณ์ในตอนนี้"

# hi "This really is too much, isn't it?"
hi "แบบนี้คงมากไปจริง ๆ สิินะ"

show evh lilly_bath_smile_small
with charachange

# li "You're enjoying it though, aren't you?"
li "แต่เธอก็ชอบนี่ ใช่ไหม"

# hi "In some ways, yes. I guess things turned out okay, in the end."
hi "จะว่าใช่ก็ใช่ สุดท้ายอะไร ๆ ก็ลงเอยด้วยดีละนะ"

# hi "Everything's settled down, Hanako took our relationship well, and we'll be going back to school tomorrow."
hi "ทุกอย่างก็ลงตัวแล้ว ฮานาโกะก็เข้าใจเรื่องความสัมพันธ์ของเรา แล้วพรุ่งนี้เราก็จะได้กลับไปที่โรงเรียนแล้ว"

# li "Indeed. It's a shame to be going back so soon, but we'll still have our memories of this place."
li "นั่นสินะจ๊ะ ถึงจะน่าเสียดายที่อีกไม่นานจะต้องกลับแล้ว แต่เราก็มีความทรงจำกับที่นี่แล้วนี่นะ"

# hi "Memories, huh? I suppose so. We'll have to see how everything goes once we get back, but for now… I'm just glad you like me."
hi "ความทรงจำเหรอ คงงั้นละมั้ง เดี๋ยวพอกลับไปที่โรงเรียนแล้วคงต้องดูอีกทีว่าจะเรื่องเป็นยังไงต่อ แต่ตอนนี้…\nฉันดีใจนะที่เธอชอบฉัน"

# hi "I've been winding myself up for weeks about that, so I'm thankful for things turning out like this."
hi "ฉันคิดมากเรื่องนี้อยู่หลายสัปดาห์เลย ฉันเลยดีใจมากที่อะไร ๆ ลงเอยอย่างนี้น่ะ"

# "She nods, leaning into me as we share the warmth of our bodies."
"ลิลลี่พยักหน้าเอนตัวแนบฉัน พวกเราแบ่งปันความอบอุ่นจากร่างกายให้กันและกัน"

# "I'm not sure whether she'll be okay with it or not, but my temptation rapidly begins to get the better of my self-restraint."
"ถึงไม่รู้ว่าลิลลี่จะโอเคหรือเปล่า แต่ตอนนี้ความอยากที่ก่อตัวเริ่มเกินกว่าที่ฉันจะควบคุมตัวเองไหวแล้ว"

# hi "Hey, Lilly?"
hi "นี่ ลิลลี่"

# li "Yes?"
li "อะไรเหรอ"

# hi "How was it? Last night, that is."
hi "เป็นไงบ้าง เมื่อคืนน่ะ"

# "She pauses in thought before looking down slightly. A delicate smile finds its way onto her lips as she blushes, her body becoming more relaxed. It's more than enough to answer the question."
"ลิลลี่เงียบพลางคิดก่อนจะก้มหน้าลงเล็กน้อย รอยยิ้มบาง ๆ ปรากฏบนใบหน้าเธอซึ่งเปลี่ยนเป็นสีแดงเรื่อ ทั้งตัวเธอ\nคลายลง ซึ่งเท่านี้ก็เพียงพอที่จะตอบคำถามได้แล้ว"

# "Even as I give a small nod in response, thoughts of last night run through my mind. Considering the situation, I don't really think anyone'd blame me."
"แม้แต่ตอนที่ฉันพยักหน้าตอบเบา ๆ ก็ยังมีเหตุการณ์เมื่อคืนที่ผ่านมาแล่นเข้ามาในความคิด สถานการณ์พาไป\nขนาดนั้น ฉันว่าใคร ๆ ก็คงเข้าใจแหละ"

# li "Hisao, your heart's beating…"
li "ฮิซาโอะ ใจเธอเต้น…"

# "Her voice is cut off as I delicately place a hand on her thigh. While I'd resisted before, the memory of our first time is enough to make me give in."
"เสียงเธอขาดห้วงไปเมื่อฉันสัมผัสเข้าที่ต้นขาของเธออย่างเบามือ ก่อนหน้านี้ฉันทนแล้ว แต่เมื่อนึกถึงครั้งแรกของเรา\nแล้วฉันก็ไม่อาจทนได้อีกต่อไป"

# "She lets her body lean into mine without a word of protest, an invitation that I'd be hard put to ignore. I place a small kiss on her neck to accept, before slowly moving my hand over her smooth legs."
"ลิลลี่เอนตัวพิงฉันเงียบ ๆ ไม่ต่อต้านอะไรอันเป็นการเชื้อชวนซึ่งยากจะเมินเฉย ฉันจุมพิตเข้าที่ต้นคอเธอเบา ๆ\nเป็นการตกลงรับก่อนจะเริ่มลูบไปตามขาเนียนของเธอ"

# li "Hisao, please…"
li "ฮิซาโอะ ได้โปรด…"

# "Even as she says it, her mouth curls upward into a smile, her tone caught between embarrassment and awkward giggling."
"แม้แต่ตอนที่เธอพูดเธอก็ยังยิ้มอยู่ คล้ายเธอเลือกไม่ถูกว่าจะอายดีหรือหัวเราะคิกคักดี"

show evh lilly_bath_open_small
with charachange

# "Eventually she takes one of my hands in hers, guiding it to her right breast. I greatly appreciate the tentative guidance she's willing to give me."
"สุดท้ายเธอก็จับมือฉันให้ไปจับที่หน้าอกข้างขวาของเธอ ฉันยินดีเป็นอย่างยิ่งที่เธอยอมนำทางให้ฉันแบบอ้อม ๆ\nอย่างนี้"

show evh lilly_bath_grab_small
with charachange

# "All signs of tension in her body give way. I continue to take in the feeling of her soft skin, redoubled as my other hand slips between her legs."
"ลิลลี่หายเกร็งแล้ว ฉันยังคงสัมผัสผิวอ่อนนุ่มของเธอไปเรื่อย ๆ และยิ่งรู้สึกถึงสัมผัสนั้นได้มากขึ้นทวีคูณเมื่อมืออีกข้าง\nเลื่อนต่ำไปตรงหว่างขาของเธอ"

# "I wonder if the feeling of my hands on her is exaggerated by her lack of sight, since her other senses are so finely tuned."
"ฉันนึกสงสัยว่าเธอจะรู้สึกถึงการสัมผัสจากมือฉันได้มากกว่าปกติหรือเปล่า เพราะประสาทการรับรู้อื่น ๆ ของเธอนั้น\nไวเป็นพิเศษเพื่อชดเชยกับการที่เธอมองไม่เห็น"

# "She does seem to be enjoying it to a surprising extent, after all. It gives me a somewhat odd feeling, but a pleasurable one."
"เธอเองก็ดูจะชอบกว่าที่ฉันคิดเอาไว้เหมือนกัน เป็นความรู้สึกที่ประหลาด แต่ก็ชวนให้รู้สึกดี"

show evh lilly_bath_moan_small
with charachange

# "It only takes a few minutes before her body starts to squirm ever so slightly, her efforts to stifle her moaning becoming visible as she purses her lips. Her lighthearted, whispered protestations become noticeably more quiet."
"ผ่านไปไม่กี่นาทีทั้งร่างเธอก็เริ่มเกร็งขึ้นมาเล็กน้อย ปากเธอที่เม้มอยู่บอกชัดว่ากำลังกลั้นเสียงครางอยู่ เสียงร้องประท้วง\nแผ่วเบาและผ่อนคลายนั้นยิ่งเบาลงไปอีก"

# "This makes me realize that all her squirming against my body's made me increasingly excited as well."
"และฉันเองก็เพิ่งรู้ตัวว่าการที่เธอดีดดิ้นอยู่บนตัวฉันนั้นทำให้ฉันตื่นตัวขึ้นเป็นอย่างมากด้วย"

# hi "Lilly…"
hi "ลิลลี่…"

show evh lilly_bath_smile_small
with charachange

# "I withdraw my hands to give her addled senses time to respond. Nodding, she shakily stands and offers her hands for me to lead her out of the cramped bathtub."
"ฉันถอนมือออกเพื่อให้ลิลลี่ที่ถูกกระตุ้นหนักได้มีเวลาพักก่อนจะตอบสนอง เธอพยักหน้าแล้วลุกขึ้นยืนตัวสั่นยื่นมือ\nนำทางพาฉันออกจากอ่างน้ำอันคับแคบ"

scene evh lilly_afterbath_open_small
with locationchange

# "She maneuvers herself out of the bath as I do, our hands holding each other's."
"พวกเราจับมือพากันออกจากอ่างอาบน้ำพร้อม ๆ กัน"

# "Eventually I sit beside the bathtub, the two of us fussing around a little until we get comfortable. With a small gasp, desperately constrained to avoid being audible outside, she lowers herself onto me once again."
"สุดท้ายเรามานั่งลงที่ข้างอ่างอาบน้ำโดยจัดแจงตัวเองอีกเล็กน้อยให้อยู่ได้แบบสบายตัว ลิลลี่ลดตัวลงนั่งทับฉันอีกครั้ง\nฉันหลุดร้องเฮือกออกมาเล็กน้อยแม้พยายามกลั้นเสียงเพื่อไม่ให้มีเสียงเล็ดลอดออกไปแล้วก็ตาม"

# "The way she moves makes it obvious that she must still be on the verge of her climax."
"ดูจากการที่ลิลลี่ขยับอย่างนี้แล้ว แปลว่าเธอยังอารมณ์ค้างอยู่"

# "She slowly starts to move her hips up and down, her tongue finding mine as she holds my face upwards. I realize just how much pleasuring her has excited me."
"เธอขยับเอวขึ้นลงช้า ๆ ระหว่างที่เธอกำลังจับหน้าฉันไว้เพื่อจูบและสอดลิ้นเข้ามา และฉันก็ได้รู้ว่าการที่ทำให้เธอได้\nรู้สึกดีนั้นทำให้ฉันตื่นตัวได้ขนาดไหน"

scene evh lilly_afterbath_shut_small
with locationchange

# li "Hisao… Hisao…"
li "ฮิซาโอะ… ฮิซาโอะ…"

# "Despite her clouded eyes being shut, her tightening grip on my shoulders show that she's nearing the end of her endurance."
"แม้ตาขุ่นมัวคู่นั้นจะปิดอยู่ แต่แรงบีบจากมือเธอที่ไหล่ฉันนั้นบอกชัดว่าเธอจะทนไม่ไหวแล้ว"

# "As our breathing becomes more and more ragged, I rapidly feel my limit approaching as well."
"ลมหายใจพวกเราหอบกระชั้นหนักขึ้นทุกขณะ ฉันเองก็ใกล้จะทนไม่ไหวแล้วเช่นกัน"

# "A series of harsh breaths is the only warning before her final gasp of ecstasy, her entire body tensing and her fingernails digging into my shoulders."
"เสียงหายใจหอบจากเธอเป็นสัญญาณเดียวที่บอกว่าอารมณ์ของเธอนั้นขึ้นถึงขีดสุดแล้ว ทั้งร่างของเธอหดเกร็ง\nเธอจิกไหล่ฉันแน่น"

# "My loins hit hers, both of us frozen against each other in climax."
"ส่วนล่างของฉันเข้ากระทบกับตัวเธอ เราทั้งสองคนต่างนิ่งค้างไปกับความสุขสมนั้น"

with Fade(0.5,1.0,4.0, color="#FFF")
stop music fadeout 8.0

# "In a few precious seconds, it's all over, Lilly slumping forward onto me as I try to regain myself."
"ทุกอย่างสิ้นสุดลง ณ ชั่วขณะอันหอมหวานนั้น ลิลลี่ทิ้งตัวลงฟุบกับฉันซึ่งกำลังตั้งตัวอยู่"

# hi "That was… good…"
hi "รู้สึก… ดีจัง…"

# "She takes a gulp of air before replying, steadying herself as she nods."
"เธออ้าปากสูดหายใจเฮือกใหญ่พลางตั้งตัวตรงแล้วพยักหน้าก่อนตอบ"

# li "Mm…"
li "อื้ม…"

# "She bows her head down to give me a small kiss, my hand reaching up to hold strands of her disheveled hair as we once again sit in blissful silence."
"ลิลลี่ก้มหัวเข้ามาจูบเบา ๆ ฉันเอื้อมมือไปลูบกลุ่มผมที่ดูไม่เรียบร้อยของเธอ พวกเรานั่งเงียบอย่างสุขใจอยู่ด้วยกัน\nอีกครั้ง"

stop music fadeout 2.0

scene black
with dissolve

label th_L20:

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_trainint fadein 5.0

scene ev lilly_trainride_ni
show train_scenery_ni
show train_scenery_fg_ni
show lilly_trainride_ni norm at train_shake
with locationchange

# "After a chaotic dash to the station and finding our seats in the otherwise deserted carriage, we promptly crashed. Looking at the time - close to midnight - it's little surprise that few take this particular train."
"พวกเราโกยหน้าตั้งมาที่สถานีรถไฟแล้วมาหาที่นั่งในขบวนที่แทบไม่มีใครก่อนจะทรุดตัวลงกับที่นั่งในทันที ซึ่งก็คง\nไม่แปลกเท่าไหร่ที่แทบไม่มีใครขึ้นรถไฟเที่ยวนี้ เพราะตอนนี้ก็เกือบจะเที่ยงคืนแล้ว"

# "Hanako is fast asleep on Lilly's shoulder and I can only barely muster the energy to stay awake. The excitement we had a while ago probably didn't help."
"ฮานาโกะพิงไหล่ลิลลี่หลับปุ๋ยอยู่ ส่วนตาฉันก็แทบจะปิดอยู่แล้ว ยิ่งก่อนหน้านี้มีเรื่องให้ต้องออกแรงอีก"

# "I'd probably be pretty depressed about going back to school if my brain was actually working."
"ถ้าสมองฉันยังทำงานปกติอยู่ฉันคงนั่งหมองที่อีกเดี๋ยวจะต้องกลับไปเรียนแล้ว"

# "As it is, though, the sight of the night-time scenery scrolling by is surprisingly beautiful."
"แต่ทิวทัศน์ยามค่ำคืนที่เลื่อนไหลผ่านสายตาไปนั้นสวยงามเกินคาด"

# "My loud yawn is nearly wholly drowned out by the clacking of the train tracks and the old carriage's rattling."
"เสียงกึงกังตึงตังจากรางรถไฟและขบวนรถไฟเก่า ๆ นั้นดังกลบเสียงหาวหวอดของฉันไปจนแทบสิ้น"

# hi "So tired…"
hi "เหนื่อยชะมัด…"

play music music_comfort fadein 2.0

show lilly_trainride_ni ara at train_shake
with charachange

# li "And whose fault is that, Hisao?"
li "ก็แล้วความผิดใครล่ะจ๊ะ ฮิซาโอะ"

# "She really does toe the line between insulting and amusing sometimes, though I manage to wring out a weary smile."
"บางทีสิ่งที่ลิลลี่พูดหยอกขำ ๆ ก็ชวนให้หงุดหงิดได้หน่อย ๆ เหมือนกัน แต่ฉันก็ยิ้มตอบเพลีย ๆ ไป"

# "I look back out the window, my reflection just visible on the clear pane. Truth be told, she's perfectly correct. If it weren't for that little interlude a few hours ago, both of us would have a lot more energy."
"ฉันหันมองหน้าต่าง บานกระจกใสนั้นสะท้อนภาพใบหน้าของฉันอยู่ราง ๆ แต่ว่าตามตรง ที่ลิลลี่พูดน่ะถูกแล้ว ถ้าไม่ใช่\nเพราะเรื่องที่เกิดขึ้นเมื่อสองสามชั่วโมงก่อน เราสองคนคงมีแรงอีกเหลือเฟือ"

# "On top of that, we both had to take another bath, very nearly making us late for the train's departure."
"แล้วยิ่งไปกว่านั้น เราสองคนต้องอาบน้ำกันอีกรอบ ซึ่งกินเวลาจนพวกเราแทบจะตกรถไฟอยู่แล้ว"

# hi "Yeah, yeah, it was mine. Still, getting into a bath with a guy is a dangerous thing to do."
hi "เออ ๆ ความผิดฉันเอง แต่ว่านะ การอาบน้ำกับผู้ชายเนี่ยเป็นอะไรที่อันตรายมากนะ"

show lilly_trainride_ni smile at train_shake
with charachange

# li "Evidently."
li "ชัดเจนจ้ะ"

# hi "Sorry. I guess I kind of took advantage of the situation back there."
hi "ขอโทษทีนะ ตอนนั้นฉันเองก็คงย่ามใจไปหน่อย"

show lilly_trainride_ni weaksmile at train_shake
with charachange

# li "Well… I didn't exactly hate it…"
li "อืม… ฉันเองก็ไม่ได้รังเกียจ…"

# "As she trails off, I look back to her. My eyes narrow as I see her slightly reddened cheeks and small grin, her mind obviously elsewhere."
"จังหวะที่ลิลลี่เสียงอ่อยไปนั้นฉันก็หันกลับมามองเธอ ฉันหรี่ตามองเธอที่หน้าแดงเรื่อและยิ้มน้อย ๆ อยู่ ตอนนี้ใจเธอ\nไม่ได้อยู่กับตัวแล้วแน่ ๆ"

# hi "Say it."
hi "พูดต่อสิ"

# li "I… knew the possibility of it happening… was there."
li "ฉัน… รู้ว่าเรื่องมันจะเป็นอย่างนั้น… ไปได้อยู่"

# hi "I knew it. You're just as dirty-minded as I am."
hi "ว่าแล้วเชียว เธอก็ทะลึ่งเหมือนฉันน่ะแหละ"

# "She quickly coughs into her free hand, making her disapproval crystal clear."
"ลิลลี่รีบกระแอมใส่มือข้างที่ว่างอยู่เป็นการแสดงความไม่เห็นด้วย"

show lilly_trainride_ni pout at train_shake
with charachange

# li "That's a rather crude way of putting it."
li "เธอก็พูดเกินไป"

# hi "Oh? And you would suggest?"
hi "เหรอ แล้วจะให้พูดว่าไงล่ะ"

# li "I merely have a healthy adolescent sex drive."
li "ฉันก็แค่มีแรงขับเคลื่อนทางเพศซึ่งอยู่ในระดับที่เหมาะสมกับวัย"

# hi "So in other words, dirty-minded."
hi "หรือก็คือ ทะลึ่งนั่นเอง"

# "Almost seeming to sense the moment, Hanako mumbles quietly as she furrows her brow in Lilly's lap."
"ฮานาโกะที่นอนหนุนตักลิลลี่อยู่ขมวดคิ้วละเมอเสียงแผ่วราวกับรับรู้ได้ถึงสถานการณ์ในตอนนี้"

show lilly_trainride_ni opensmile at train_shake
with charachange

# "Lilly's look of disapproval melts away as she gently smiles and strokes her hand on Hanako's long, dark hair."
"สีหน้าไม่พอใจของลิลลี่หายไปในทันที เธอยิ้มอ่อนโยนแล้วลูบผมยาวสีเข้มของฮานาโกะ"

# "All I can do is watch. Watch and smile."
"ฉันได้แต่นั่งมอง มองแล้วยิ้ม"

# "If someone were to ask me when I fell in love with her, I wouldn't be able to answer. The best I'd be able to come up with is “it just happened at some point, but I didn't realize it.”"
"ถ้ามีใครถามว่าฉันไปรักลิลลี่ตอนไหน ฉันคงตอบไม่ได้ อย่างดีก็คงตอบได้แค่ว่า “คงรักสักตอนหนึ่งแหละ แต่ฉันไม่รู้ตัว\nเท่านั้นเอง”"

# "If someone were to ask me why I love her, though, then I could answer much more easily."
"แต่ถ้ามีใครถามว่าทำไมฉันถึงรักลิลลี่ ฉันจะหาคำตอบมาตอบให้ได้อย่างง่ายดาย"

# hi "You really love Hanako, don't you?"
hi "เธอนี่ชอบฮานาโกะจริงเลยนะ"

show lilly_trainride_ni smile at train_shake
with charachange

# "She gives a deep nod, smiling warmly."
"ลิลลี่ยิ้มอบอุ่นพยักหน้าชัด"

label th_choiceL20:
menu:
    with menueffect
    
    # li "It's a pity we have to return to school. She seemed to relax so much while we were all away."
    li "เสียดายจังที่ต้องกลับโรงเรียนกันแล้ว ตอนที่พวกเราไปเที่ยวกันฮานาโกะดูจะผ่อนคลายลงเยอะเลย"

    # "Talk about Hanako.":
    "คุยเรื่องฮานาโกะ":
        return m1

    # "Talk about school.":
    "คุยเรื่องโรงเรียน":
        return m2


label th_L20a:
# [1]

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

# hi "I wouldn't worry. Hanako's been gaining confidence thanks to you, at least for as long as I've known you two."
hi "ไม่ต้องคิดมากหรอก เท่าที่ฉันรู้จักเธอสองคนมา ที่ฮานาโกะมั่นใจขึ้นก็เพราะเธอนะ"

show lilly_trainride_ni weaksmile at train_shake
with charachange

# "She gives a self-deprecating sigh."
"ลิลลี่ถอนหายใจเป็นเชิงตัดพ้อ"

# li "I think I merely provided her with company and support. Since she came to know you she's opened up much more, even to me."
li "ฉันก็แค่อยู่เป็นเพื่อนคอยสนับสนุนฮานาโกะเอง ตั้งแต่ที่ฮานาโกะได้มารู้จักเธอ ฮานาโกะเขาก็เปิดใจขึ้นเยอะ\nแม้แต่กับฉันด้วย"

# "I get the feeling she's understating her influence on Hanako, especially given that before the two came to know each other, Hanako had no friends to speak of."
"ฉันคิดว่าลิลลี่คงเข้าใจว่าตัวเองมีอิทธิพลต่อฮานาโกะอย่างไรบ้าง แถมก่อนหน้าที่สองคนนี้จะได้มาเจอกัน ฮานาโกะนั้น\nไม่มีเพื่อนให้คุยด้วย"

# "The friends I'd had in my previous school fulfilled what I'd have expected of them, for the most part simply being there for idle chatter, but in Hanako and Lilly there really feels to be more to their relationship."
"เพื่อนที่โรงเรียนเก่าของฉันก็ทำหน้าที่ในฐานะเพื่อนตามที่ฉันคาดหวังได้ ส่วนใหญ่ก็เป็นหน้าที่ของการเป็นเพื่อนคุย\nเรื่อยเปื่อย แต่สำหรับฮานาโกะกับลิลลี่แล้ว ฉันรู้สึกว่าความสัมพันธ์ของสองคนนี้มีอะไรที่มากกว่านั้น"

# "A part of me envies it, but another can't ignore the fact that the school year will eventually end. After graduation, I really have no idea what Hanako will do. This trip has shown me just how much we've all come to depend on one another."
"ใจหนึ่งฉันก็นึกอิจฉา แต่อีกใจก็ยังคิดอยู่ว่าท้ายที่สุดแล้วสักวันทุกคนก็จะเรียนจบ พอเรียนจบแล้วฉันไม่รู้ว่าฮานาโกะ\nจะทำอย่างไรต่อ การไปเที่ยวครั้งนี้ได้แสดงให้เห็นว่าพวกเราต่างพึ่งพากันและกันมากขนาดไหน"

# "Indeed, we're all going to have to make decisions. Maybe that's the reason why, despite our return to school also heralding a return to the normalcy of everyday life, I can't help feeling a little restless."
"นั่นสินะ สุดท้ายแล้วพวกเราทุกคนต่างต้องตัดสินใจ ซึ่งอาจจะเป็นเหตุผลว่าทำไมฉันถึงร้อนรนอยู่บ้างที่ได้กลับไป\nที่โรงเรียน ทั้งที่สิ่งนี้หมายความว่าจะเป็นการได้กลับไปใช้ชีวิตในทุก ๆ วันตามปกติด้วย"

label th_L20b:
# [2]

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

# hi "Indeed. Exams will be starting, too, which will be another thing to deal with. Think you're ready for them?"
hi "นั่นสินะ เดี๋ยวก็จะสอบแล้วด้วย ซึ่งก็ต้องว่ากันอีกที เธอพร้อมสอบมั้ย"

show lilly_trainride_ni weaksmile at train_shake
with charachange

# li "I think so. I don't think it will be a pleasant period at all, though."
li "พร้อมจ้ะ แต่ช่วงสอบนี่เป็นอะไรที่ไม่น่าอภิรมย์เอาเสียเลย"

# "I can't say I disagree with her. The exams had completely slipped my mind for a while now, and even though I may score well on most of our tests, I can't assume that I can pass easily with so little studying beforehand."
"ก็ปฏิเสธไม่ได้ละนะ ก่อนหน้านี้เรื่องสอบนั้นหายไปจากสารบบอยู่พักใหญ่เลย และถึงฉันจะทำคะแนนสอบหลาย ๆ วิชา\nได้ดีก็จริง แต่ก็ใช่ว่าถ้าไม่อ่านอะไรเลยแล้วจะยังผ่านได้ง่าย ๆ"

# "Lilly does seem more studious, or at least more regimented, than me. That said, she has to contend with doing rather badly in some subjects no matter how much she tries."
"ลิลลี่ดูเป็นคนตั้งใจเรียน—หรืออย่างน้อยก็เป็นคนมีระเบียบ—กว่าฉัน แต่ถึงอย่างนั้น เธอเองก็ต้องรับมือกับบางวิชา\nที่ไม่ว่าเธอจะพยายามแค่ไหนก็ยังได้คะแนนไม่ค่อยดีด้วย"

# hi "At least they'll only last a couple of weeks."
hi "อย่างน้อยช่วงสอบก็มีแค่สองสัปดาห์ละนะ"

label th_L20c:
# End split

# hi "On the bright side, it won't take long for the summer holidays to arrive after our exams are finished. We could come back here during the summer holidays if you want."
hi "แต่มองในแง่ดี เดี๋ยวสอบเสร็จก็ได้ปิดเทอมฤดูร้อนกันแล้ว ถ้าอยากมาเที่ยวอีกก็เอาไว้ค่อยมาช่วงนั้นก็ได้"

# "For a moment she thinks on the notion, her face becoming somewhat distant. I can only guess she's reflecting on all that's happened here."
"ลิลลี่ครุ่นคิดกับข้อเสนอนั้นอยู่ครู่หนึ่ง สีหน้าเธอดูเหม่อ ๆ คงจะคิดถึงเรื่องต่าง ๆ ที่เกิดขึ้นตอนไปเที่ยวอยู่ละมั้ง"

show lilly_trainride_ni opensmile at train_shake
with charachange

# li "That would be… good, I think."
li "ก็คง… ดีเหมือนกันนะจ๊ะ"

# "I nod approvingly, smiling at her."
"ฉันยิ้มพยักหน้าเห็นด้วย"

# "Summer, together with Lilly. This idea seems like the perfect way to spend our holiday."
"ฤดูร้อน ที่ฉันได้อยู่กับลิลลี่ เพียงคิดก็สัมผัสได้ว่าจะต้องเป็นวันปิดเทอมที่แสนสมบูรณ์แบบอย่างแน่นอน"

stop music fadeout 3.0
stop ambient fadeout 3.0

window hide
return