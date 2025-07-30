label th_H2:

scene bg school_miyagi
show hanako emb_downsmile_close
with None

play sound sfx_doorknock2

show hanako emb_timid_close
with charachange

"พอพวกเรากำลังตั้งกระดานใหม่ก็มีเสียงที่ประตู"

play sound sfx_dooropen

show bg school_miyagi at bgright
show hanako emb_timid_close at tworight
with charamove

show lilly basic_smileclosed at twoleft
with charaenter

li "ทิวาสวัสดิ์จ้ะ"

play music music_lilly fadein 4.0

show hanako emb_emb_close
with charachange

ha "ลิลลี่…"

hi "อ้าว ว่าไงลิลลี่ งานเสร็จแล้วเหรอ"

show lilly basic_smile at twoleft
with charachange

li "พวกเธออยู่ที่นี่กันทั้งคู่เลยเหรอ ดีเลย พอดีครูเราหาคนมาช่วยเพิ่มได้แล้วน่ะ ฉันเลยออกมาได้ แล้วนี่นายมาที่นี่ตั้งแต่\nตอนที่ออกไปจากแผงเลยหรือเปล่า?"

hi "ประมาณนั้นแหละ พวกเราเพิ่งเล่นหมากรุกไปกันนิดหน่อย"

show hanako emb_smile_close
with charachange

ha "ดะ…ดื่มชาหน่อยไหม"

show lilly basic_weaksmile at twoleft
with charachange

li "จริง ๆ ฉันว่าเราออกไปเดินเล่นข้างนอกกันสักหน่อยดีกว่า…"

show hanako def_worry_close
with charachange

"สีหน้าของฮานาโกะที่เปลี่ยนไปในทันทีฟ้องว่าไม่เห็นด้วยกับแผนนี้ แม้ว่าเธอจะไม่ได้พูดอะไรเลยก็ตาม"

"ฉันรู้สึกแปลก ๆ ที่ต้องบอกสิ่งที่เห็นอยู่บนหน้าเธอจะจะ แต่ลิลลี่มองไม่เห็น"

hi "เอ่อ… ฉันว่าเราอยู่ที่นี่ดีกว่านะ…"

show lilly basic_surprised at twoleft
with charachange

li "งั้นเหรอ พอดีรู้สึกว่าที่นี่คนเยอะมากเลยกะว่าจะออกไปนอกโรงเรียนไปโรงน้ำชาที่อยู่ในเมืองน่ะจ้ะ"

show hanako emb_blushtimid_close
with charachange

ha "ซะ…เซี่ยงไฮ้ น่ะเหรอ"

show lilly basic_smileclosed
with charachange

li "นั่นแหละ เพราะทุกคนมางานเทศกาล ที่นั่นก็น่าจะโล่งพอตัว"

hi "โรงน้ำชาเหรอ"

show lilly basic_weaksmile
with charachange

li "อ้อ ใช่ ๆ นายน่าจะยังไม่รู้จัก"

show lilly basic_smile
with charachange

li "แถว ๆ นี้มีโรงน้ำชาที่พวกเราไปบ่อย ๆ อยู่"

hi "ก็โอเคนะ ฮานาโกะ เธอว่าไงล่ะ"

show hanako defarms_shock_close
with Dissolve(0.2)

show hanako def_worry_close
with charachange

"เธอสะดุ้งนิดหน่อยที่จู่ ๆ ก็โดนดึงเข้ามาคุยด้วย แต่ก็ดีหน่อยตรงที่ดูไม่ค่อยเป็นทุกข์เหมือนก่อนหน้านี้"

show hanako cover_bashful_close
with charachange

ha "ถะ… ถ้าเป็นที่เซี่ยงไฮ้ละก็ ฉันว่าก็ดีนะ"

show lilly basic_planned
with charachange

li "ถ้างั้นก็ตกลงตามนี้นะ ไปกันเถอะจ้ะ"

show hanako basic_bashful
with charadistant

"ฮานาโกะกับฉันลุกขึ้นจากโต๊ะสละเกมหมากรุกที่ยังเล่นไม่ทันจบ"

"ฮานาโกะเทหมากใส่กล่องเล็ก ๆ และเก็บกระดานโดยที่ฉันยังไม่ทันได้ทำอะไร"

hi "ดูท่าทุกคนจะพร้อมแล้วละ ช่วยพาไปที"

stop music fadeout 8.0

scene bg school_hallway3
with locationchange

show hanako emb_smile at Transform(xanchor=0.5, xpos=0.58)
show lilly basic_smileclosed at Transform(xanchor=0.5, xpos=0.42)
with charaenter

"ฮานาโกะเดินไปข้าง ๆ ลิลลี่แล้วพวกเราก็เดินออกไปที่โถงทางเดินของโรงเรียน"

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")

play ambient sfx_crowd_outdoors fadein 1.0

scene bg school_gate_ss
with locationskip

"ทั้งคู่พาฉันเดินผ่านประตูที่ไม่คุ้นตาหลายบาน แล้วเราก็โผล่มาอีกฝั่งของตึกที่อยู่ตรงข้ามกับลานจัดงานเทศกาลพอดี"

"เพราะตึกหินที่หนาเตอะ เสียงฝูงชนเลยจางลงจนเหลือแค่เสียงอู้อี้เบา ๆ เท่านั้น"

hi "แปลกจัง ฉันนึกว่าคนส่วนใหญ่น่าจะกลับไปแล้วเสียอีก…"

show hanako emb_downtimid_ss at Transform(xanchor=0.5, xpos=0.58)
show lilly basic_smile_ss at Transform(xanchor=0.5, xpos=0.42)
with charaenter

li "พวกเขาน่าจะมารอดูพลุน่ะจ้ะ"

hi "พลุเหรอ"

show lilly basic_weaksmile_ss
with charachange

li "ใช่จ้ะ เหมือนโรงเรียนจะจัดงานได้อลังการน่าดูเลยนะ คนจากในเมืองเลยถ่อมาดูพลุกันเยอะเลยน่ะจ้ะ"

"พอจะเข้าใจแล้วว่าทำไมลิลลี่ถึงเลือกที่จะไม่อยู่ที่โรงเรียน เพราะฮานาโกะก็คงจะอึดอัดกับจำนวนคนที่แห่ลงมาดูงาน\nกันขนาดนั้น หรือจะเรียกว่าแห่ขึ้นมาดูก็ไม่น่าผิด"

stop ambient fadeout 7.0
play music music_tranquil fadein 3.0

scene bg school_road_ss
with locationchange

"นี่เป็นรอบที่สองแล้วนับตั้งแต่ที่ฉันเข้ามายามากุที่ฉันได้เดินบนถนนเส้นนี้กับลิลลี่"

"พอมาถึงตอนนี้ที่ฉันแทบไม่ได้ยินเสียงงานเทศกาลที่ดังไม่หยุดก็ถึงเพิ่งรู้ว่ามันดังขนาดไหน ในหูยังอื้ออยู่นิด ๆ\nกับอากาศยามเย็นที่เงียบสงบเลย เหมือนหูมันกำลังฟื้นตัวจากที่โดนกระหน่ำมาทั้งวัน"

show hanako emb_emb_ss at Transform(xanchor=0.5, xpos=0.58)
show lilly basic_smileclosed_ss at Transform(xanchor=0.5, xpos=0.42)
with charaenter

"ฮานาโกะเกาะลิลลี่แน่นเลย แต่ก็ยังพอจะพาลิลลี่เดินไปตามทางได้อยู่ ไหนจะเรื่องนั้นแล้ว ไหนจะต้องคอยหลบสายตา\nอยากรู้อยากเห็นจากคนที่เดินผ่านไปมาอีก ดูท่าทางจะทำให้เธอหมดแรงไปเลยละ"

"เธอไม่ค่อยละสายตาไปจากพื้นตรงหน้าเลย แถมยังไม่ปริปากพูดอะไรออกมาสักคำด้วย"

"ส่วนลิลลี่เองก็ยังคงท่าทางสงบเสงี่ยมเหมือนที่อยู่โรงเรียน เห็นได้ชัดว่าเธอตั้งใจทุ่มเทกับการรักษาภาพลักษณ์\nของตัวเอง ไม่ได้พยายามซ่อนมันไว้เหมือนอย่างที่ฮานาโกะทำ"

"พอเห็นความต่างของทั้งสองคนยามอยู่นอกรั้วยามากุแล้วก็ทึ่งดี แต่ถึงอย่างนั้น ก็เห็นได้ชัดว่าท่าทางของทั้งคู่นั้น\nเปลี่ยนไปจากเดิม"

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")

window hide

nvl clear

$ renpy.music.set_volume(0.5, 1.0, channel="music")

nvl show dissolve

n "\n\n\nที่โรงเรียนยามากุ ทุกคนต่าง “พิเศษ” ซึ่งจะทำให้ “ความพิเศษ” นั้นกลับเป็นความปกติ"

n "แต่เมื่อก้าวเท้าออกมาจากรั้วโรงเรียนแล้ว เราก็จะมีป้าย “คนนอก” และอื่น ๆ แปะอยู่กับตัวดังเดิม"

n "ยิ่งเมื่อมีชุดนักเรียนอยู่ด้วยแล้ว ก็ไม่ต่างอะไรกับการแขวนป้ายไว้กับคอรอให้คนอื่นทายว่าตัวเองนั้นมีอะไรที่ผิดปกติ"

n "ฉันนึกแปลกใจที่มีนักเรียนหลายคนใส่ชุดนักเรียนไปไหนมาไหน แต่ก็นะ ในเมื่อหลายคนมีไม้เท้าติดตัว นั่งวีลแชร์\nจะใส่ไม่ใส่ก็คงดูออกอยู่ดี"

n "\nหรือมีแค่ฉันที่มองว่าเรื่องนี้มันแปลก ๆ กันนะ พออยู่นาน ๆ ไปแล้วอาจจะชินตาขึ้นมาอย่างชุดนักเรียนโรงเรียนอื่น ๆ \nก็ได้"

nvl hide dissolve

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear

scene bg suburb_shanghaiext_ss
with locationskip

window show

"โรงน้ำชาจากด้านนอกก็ดูปกติทั่วไป ก็แค่ตึกที่มีป้ายธรรมดา ๆ ตกแต่งไว้ที่หน้าทางเข้า"

"เป็นที่ที่คนเดินผ่านโดยไม่สนใจ ก็แค่คาเฟทั่ว ๆ ไปเหมือน ๆ กับที่อื่นอีกร้อยพันแห่ง"

"ถ้าฮานาโกะไม่ได้ดึงลิลลี่เข้ามาที่หน้าร้าน ฉันคงเดินผ่านเลยไปตามถนนโดยไม่รู้ด้วยซ้ำว่ามีร้านนี้อยู่"

play sound sfx_storebell

scene bg suburb_shanghaiint at Fullpan(5.0, dir="right")
with locationchange

stop music fadeout 6.0

"ภายในโรงน้ำชาประดับให้ดูมีความรู้สึกอย่างดั้งเดิมมากกว่าภายนอก ทุกอย่างดูเหมือนจะทำมาจากไม้ชิ้นเดียวกันหมด\nตั้งแต่เคาน์เตอร์ ม้านั่ง ไปจนถึงซุ้มที่นั่งพนักพิงสูงที่อยู่ตามผนัง"

"แต่สิ่งที่โดดเด่นที่สุดในห้องนี้คือ ความว่างเปล่าไร้ชีวิตชีวา รู้สึกแว่ว ๆ ได้ยินเสียงอะไรบางอย่างกำลังเดือดปุด ๆ\nอยู่ไกล ๆ แต่นอกเหนือจากเสียงนั้นห้องนี้ก็เงียบสนิทเลย"

"ไม่มีใครรู้ว่าควรทำอะไรต่อ พวกเราก็ได้แต่ยืนรออยู่ตรงทางเข้า ทำตามป้าย “กรุณารอพนักงานจัดที่นั่ง” อย่างว่าง่าย"

hi "เอ่อ ร้านเปิดอยู่มั้ยเนี่ย"

stop music
play sound sfx_impact2

show yuukoshang panic_up:
    xalign 0.5 yanchor 1.0 ypos 1.5 alpha 0.0
    easein 0.3 ypos 1.0 alpha 1.0
show bg suburb_shanghaiint at right
with vpunch

"เสียงเก้าอี้ล้มดังก้องไปทั่วห้องที่ว่างเปล่า แล้วก็มีหัวโผล่ขึ้นมาจากด้านในซุ้มที่นั่งทันที"

play music music_comedy fadein 0.5

show yuukoshang neurotic_up:
    ypos 1.0 alpha 1.0
with charachange

yu "ฉันไม่ได้หลับนะคะ และก็ยินดีต้อนรับสู่เซี่ยงไฮ้ค่ะ!"

"ยูโกะที่ใส่ผ้ากันเปื้อนสีพาสเทลและกำรายการเมนูแน่นรีบวิ่งมารับพวกเรา แว่นที่เอียง ๆ กับผมยุ่ง ๆ ของเธอ\nทำให้คำพูดก่อนหน้านี้ของเธอดูไม่น่าเชื่อถือเท่าไหร่"

"แต่คำถามแรกที่โผล่มาในหัวฉันไม่ใช่ว่าเธอหลับจริงหรือเปล่า"

hi "มาทำงานที่นี่แล้วเหรอครับ แล้วห้องสมุดล่ะ"

show yuukoshang smile_down
with charachange

yu "เดี๋ยวนะ ลิลลี่? ฮิซาโอะ?"

show yuukoshang neurotic_up
with charachange

yu "ยินดีต้อนรับสู่เซี่ยงไฮ้ค่ะ!"

show yuukoshang noglasses_up at Transform(ypos=1.25)
with Dissolvemove(0.2)

play sound sfx_dropglasses

with Pause(0.3)

show yuukoshang noglasses_up at center
with charamove

"ยูโกะที่ยังสะลึมสะลืออยู่ดีดตัวโค้งคำนับอย่างแรงจนแว่นกระเด็นหลุดไปเลย"

yu "อุหวา!? แว่นฉัน…"

"ลิลลี่เปิดปากอธิบายขึ้นตอนที่ฉันกำลังหยิบแว่นของเธอที่ตกอยู่บนพื้น"

show yuukoshang noglasses_up at tworight
show bg suburb_shanghaiint at center
with charamove

show lilly basic_weaksmile at twoleft
with charaenter

li "ยูโกะทำงานพาร์ทไทม์เหมือนที่ห้องสมุดน่ะ ก็เป็นอีกเหตุผลที่เราชอบมาที่นี่นั่นแหละจ้ะ"

show yuukoshang neurotic_up
with charachange

"ยูโกะรับแว่นไปจากมือของฉัน แล้วค่อย ๆ ใส่กลับเข้าที่อย่างสั่น ๆ"

yu "ใช่… ใช่แล้วละ… ขอบใจจ้ะ…"

show yuukoshang neutral_down
with charachange

yu "ให้ฉันพาไปที่โต๊ะไหม"

show yuukoshang worried_up
with charachange

yu "ยังไม่มีใครมาเลย พวกเธอเลือกโต๊ะได้ตามสบายเลยนะ อยากสั่งอะไรก็ได้ แต่ว่าอาจจะต้องรอนานหน่อยนะ\nเพราะฉันต้องทำเองทั้งหมดเลย…"

show lilly basic_smile at twoleft
with charaenter

li "ไม่เป็นไรค่ะคุณยูโกะ แค่ชาดำกาหนึ่งกับแซนด์วิชสักจานก็พอแล้วค่ะ"

show yuukoshang happy_down
with charachange

yu "ได้ค่ะ! เดี๋ยวฉันจัดการให้เดี๋ยวนี้เลย!"

hide yuukoshang
with charaexit

show lilly basic_smile at center
show bg suburb_shanghaiint at bgright
with charamove

"ยูโกะรีบวิ่งไปทางด้านหลังคาเฟ ปล่อยให้พวกเรายืนอยู่ที่ทางเข้า"

"เธอผลักประตูบานคาวบอยออกไป ก่อนที่จะนึกขึ้นได้ว่ายังไม่ได้จัดที่นั่งให้พวกเรา"

yu "ขอโทษค่ะ! ขอโทษค่ะ! เลือกโต๊ะได้ตามสบายเลยนะคะ! เดี๋ยวฉันมาค่ะ!"

stop music fadeout 3.0

hide lilly
with charaexit

show bg suburb_shanghaiint at bgleft
with charamove

"ฉันพาลิลลี่ไปที่ซุ้มที่นั่งที่อยู่ใกล้ที่สุดอย่างที่ยูโกะบอกให้หาที่นั่งโดยมีฮานาโกะเดินตามมา"

show lilly basic_smileclosed:
    twoleft
    ease 1.0 ypos 1.2
show hanako basic_normal:
    tworight
    ease 1.0 ypos 1.17
with Dissolve(1.0)

"พอได้นั่งข้าง ๆ ลิลลี่ ฉันก็เข้าใจว่าทำไมที่นี่ถึงเหมาะกับฮานาโกะ"

"ซุ้มที่นั่งพนักพิงสูงพวกนี้แยกเราออกจากส่วนอื่นของห้องได้เลย แถมดูแล้วก็ไม่น่าจะมีลูกค้าเยอะเท่าไหร่ด้วย"

"เฟอร์นิเจอร์ทั้งหมดไม่ว่าจะเป็นเบาะรองนั่งบนม้านั่งไปจนถึงที่วางเครื่องปรุงนั้นดูเก่าแล้วแต่ก็ไม่ได้โทรมจนเกินไป"

"ฉันสงสัยเลยว่าลิลลี่ตั้งใจเลือกสถานที่แบบนี้เพื่อพาฮานาโกะมาเลยหรือเปล่านะ เธอดูเป็นคนประเภทที่ยอมทำทุกอย่าง\nเพื่อให้ลงตัวกับอาการเฉพาะตัวของฮานาโกะเลย"

play music music_another fadein 4.0

show lilly basic_weaksmile:
     ypos 1.2
with charachange

li "ว่าแต่ฮิซาโอะ ไม่ยักรู้ว่าเธอก็เล่นหมากรุกด้วย…"

hi "ก็นะ ไม่ได้เล่นเก่งหรอก แค่รู้วิธีเล่นน่ะ"

show lilly basic_smile
with charachange

li "คำถามต่อมาก็คงต้อง… แล้วใครชนะเหรอ"

"รอยยิ้มไร้เดียงสาของลิลลี่ทำให้ฉันลังเลไปชั่วขณะ ฉันไม่อยากดูเหมือนกำลังข่มฮานาโกะด้วยชัยชนะของตัวเองเลย"

show hanako cover_bashful:
     ypos 1.17
with charachange

ha "ฮะ…ฮิซาโอะน่ะ"

hi "ใช่แหละ… แต่ว่าก็ไม่ได้ขนาดนั้นหรอก…"

"แม่ง คำพูดฉันเมื่อกี้เหมือนฉันไปทำอะไรผิดมาอย่างงั้น"

show lilly basic_giggle
with charachange

li "เก่งมากจ้ะฮิซาโอะที่ทำสิ่งที่ฉันไม่เคยทำสำเร็จเลยได้"

hi "เอ่อ ขอบใจนะ ฉันเองก็ไม่ได้เล่นนานแล้ว เลยสนุกที่ได้เล่นอีกครั้งน่ะ"

show hanako basic_smile
with charachange

ha "ชะ… ใช่… สนุกมากเลย"

"ฮานาโกะม้วนผมตัวเองนิดหน่อยเสตามองทางอื่นพลางตอบ แต่ก็มีรอยยิ้มเล็ก ๆ ผุดขึ้นมาบนใบหน้าเธอ"

"ท่าทางปฏิกิริยาของเธอเกินคาดไปหน่อย แต่ก็น่ารักในแบบของฮานาโกะแหละนะ"

show hanako defarms_shock at Transform(xpos=0.8)
show lilly basic_surprised at Transform(xpos=0.2)
with Dissolvemove(0.5)

show yuukoshang worried_up at center
with charaenter

"เป็นท่าทีที่เล่นเอาไม่ทันตั้งตัวเลย กว่าฉันจะดึงตัวเองกลับมาให้พูดได้อีกทีก็ตอนที่ยูโกะโผล่มาแบบเด๋อ ๆ นั่นแหละ"

hi "ไหวไหมครับคุณยูโกะ ให้ช่วยไหมครับ"

show yuukoshang neurotic_up
show hanako def_worry
with charachange

yu "ไม่เป็นไรค่ะ ไม่เป็นไรค่ะ ไม่เป็นไรค่ะ ฉันต้องจัดการเองให้ได้ เพราะเป็นงานของฉัน"

show yuukoshang worried_up
with charachange

"สมาธิจดจ่อฉายชัดบนใบหน้าของเธอขณะที่จ้องมองถาดในมือ ราวกับว่าแค่จ้องมองก็สามารถตรึงของที่วางอยู่\nให้อยู่กับที่ได้"

show yuukoshang worried_up at centertremble
with charachange

"น่าเสียดายที่การจ้องนั้นไม่เป็นผลมากนัก แก้วกับจานรองค่อย ๆ ดิ้นไปมา บางทีก็กระทบกันจนเกิดเสียงดังขึ้นมา\nเป็นครั้งคราว"

show yuukoshang worried_up at Transform(ypos=1.1)
with ease

show yuukoshang worried_up at center
with ease

"ยูโกะวางถาดลงบนโต๊ะอย่างระมัดระวังโดยมีเสียงกระทบกันเบาสุด ๆ เท่านั้น"

show yuukoshang happy_down
with charachange

yu "นี่ไง เห็นไหม!"

hi "เอ่อ เก่งมากครับ?"

show lilly basic_weaksmile
with charachange

li "ขอบคุณค่ะคุณยูโกะ"

show yuukoshang neutral_down at Transform(ypos=1.2)
with Dissolvemove(0.2)

with Pause(0.2)

show yuukoshang neutral_down at center
with ease

"หัวของยูโกะดิ่งลงไปด้านล่างเป็นการโค้งคำนับแบบฉบับเฉพาะตัวของเธอ ก่อนจะเอ่ยตอบ"

show yuukoshang closedhappy_down
with charachange

yu "ยินดีที่ให้บริการค่ะ"

show lilly basic_smile
with charachange

li "คุณอยากจะมานั่งด้วยไหมคะ พอดีมีเรื่องที่จะคุยด้วยเรื่องรายการสั่งซื้อนั้นน่ะค่ะ ถ้าไม่ติดอะไร…"

"อ่า จริงด้วย ลิลลี่เคยคุยกับยูโกะเรื่องหนังสือตอนที่ฉันเจอฮานาโกะครั้งแรกก่อนหน้านี้"

"เกี่ยวกับเรื่องที่จะช่วยลิลลี่เรื่องหนังสืออักษรเบรลล์อะไรนี่แหละ…"

show yuukoshang neurotic_up
with charachange

yu "อ่า… ใช่ เราแทบไม่ได้คุยกันเรื่องนั้นเลยสินะ"

show yuukoshang neurotic_up at Transform(ypos=1.17)
with charamove

"ยูโกะรีบเข้ามานั่งข้าง ๆ กับฮานาโกะ"

"ดูเหมือนความทุ่มเทในงานของเธอจะขึ้นอยู่กับสมาธิเท่านั้น พอสมาธิหลุดปุ๊บ เธอก็เลิกคิดไปเลย"

show yuukoshang smile_down
with charachange

yu "เดี๋ยวพรุ่งนี้ฉันจะเข้าห้องสมุดตอนบ่ายนะ ถ้าเธอจะมาตามอีกรอบ…"

show lilly basic_cheerful
with charachange

li "ดีเลยค่ะ เดี๋ยวฉันไปหาหลังเลิกเรียนนะคะ"

show hanako emb_timid
with charachange

ha "เอ่อ… ละ…ลิลลี่…"

show lilly basic_oops
with charachange

li "ตายจริง นั่นสินะ พรุ่งนี้วันจันทร์นี่ ฉันลืมไปได้ยังไงกัน"

"ฉันเริ่มรู้สึกเหมือนตัวเองอยู่นอกวงนิด ๆ แล้วสิ แต่ก็ไม่แปลกหรอก ฉันเองเพิ่งมาอยู่ที่นี่ได้แค่เกือบสัปดาห์เอง จะไปรู้\nตารางเวลาของทุกคนได้ไง"

show lilly basic_weaksmile
with charachange

li "อืม ถ้างั้นคงต้องหาเวลาอื่นแล้วละ"

show lilly basic_smile
with charachange

li "คุณยูโกะคะ คุณจะมาที่ห้องสมุดวันอื่นอีกมั้ยคะ"

show yuukoshang worried_up
with charachange

yu "อืม… คงเข้าแหละ แต่ตอนนี้ก็เลยกำหนดเวลาไปแล้ว…"

show hanako emb_downsad
with charachange

ha "ละ…แล้วฉันก็… มีของ… ที่ต้องใช้…"

show lilly basic_listen
with charachange

li "วุ่นวายแล้วสิ…"

"ลิลลี่ครุ่นคิดอยู่สักพักก่อนจะได้คำตอบ"

show lilly basic_planned
with charachange

li "ให้ใครสักคนมาช่วยดีไหมนะ ถ้าจำเป็นจริง ๆ …"

hi "เอ่อ ช่วยทำอะไรนะ ฉันตามไม่ทันมาสักพักแล้ว…"

"จะให้อาสาช่วยโดยที่ไม่รู้อะไรเลยก็กระไรอยู่"

"อุตส่าห์นึกโล่งใจที่รอดจากเงื้อมมือพวกสภานักเรียนที่เอาแต่ชวนไปเข้าร่วมมาได้แล้วแท้ ๆ "

show lilly basic_smileclosed
with charachange

li "อ๋อ ใช่ คือเมื่อวันก่อนฉันไปช่วยคุณยูโกะจัดเรียงหนังสืออักษรเบรลล์ในห้องสมุดน่ะ"

show lilly basic_weaksmile
with charachange

li "แต่ปกติแล้วฉันกับฮานาโกะจะออกไปซื้อของช่วยบ่ายวันจันทร์ เพราะวันนั้นคนจะน้อยกว่าช่วงวันหยุด"

li "สัปดาห์ก่อนพวกเราไม่ได้ไปเพราะว่าฉันยุ่งกับงานเทศกาลอยู่ ยังดีช่วงนั้นฉันหาวันอื่นไปได้ แต่ฮานาโกะเขา\nไปด้วยไม่ได้น่ะจ้ะ"

hi "อืม ในเมื่อฉันเองก็อ่านอักษรเบรลล์ไม่ออก เดาว่าเธอคงอยากให้ฉันออกไปซื้อของกับฮานาโกะสินะ"

show lilly basic_smile
show hanako emb_timid
with charachange

li "ใช่แล้วจ้ะ ครั้งก่อนเธอช่วยฉันได้เยอะเลย"

hi "ก็ไปได้แหละ ฮานาโกะ เธอว่าไงล่ะ"

show hanako basic_smile
with charachange

ha "ถะ…ถ้านายไม่ติดอะไร…"

hi "ไม่ติดหรอก ดีเสียอีก ฉันเองก็ยังไม่ค่อยคุ้นกับร้านค้าแถวนี้เท่าไหร่ด้วย"

show hanako basic_bashful
with charachange

ha "อะ…โอเค"

show lilly basic_smileclosed
with charachange

li "ในเมื่อแผนลงตัวแล้ว เรามาดื่มชากันดีไหม"

"ตอนนี้ฉันเพิ่งรู้ตัวว่าชาของเราวางอยู่เฉย ๆ นานแล้ว ไม่ได้ร้อนขึ้นไปกว่าเดิม"

show yuukoshang panic_up
with charachange

yu "ฉันผิดเองค่ะ! ให้ฉันรินให้นะคะ…"

"ยูโกะเอื้อมมือที่สั่นเทาออกมา แต่ฉันก็รีบรับไว้ก่อน ดูท่าทางเธอไม่พร้อมจะจับของร้อน ๆ เลยสักนิด"

hi "ไม่เป็นไรหรอกครับ ผมทำเองได้ แค่คุณเตรียมชากับแซนด์วิชมาก็ถือว่าทำตามหน้าที่ของบริกรครบแล้ว จริงไหมครับ"

show yuukoshang neurotic_up
with charachange

yu "คะ… คงงั้นแหละค่ะ"

"ยูโกะผ่อนคลายลงนิดหน่อย แต่ก็ยังคงจับจ้องอย่างกระตือรือร้นตอนที่ฉันแจกจ่ายของว่างบนโต๊ะ"

stop music fadeout 1.0
play ambient sfx_fireworks

show white
with Dissolve(0.1)

hide white
show fireshine
show hanako defarms_shock
show yuukoshang panic_up
show lilly basic_surprised
with charachange

"ขณะที่ฉันกำลังจะกัดแซนด์วิช ก็ได้ยินเสียงปึงปังดังเข้ามาเบา ๆ พร้อมกับแสงวาบจากข้างนอก"

show lilly basic_weaksmile
show yuukoshang smile_down
show hanako emb_timid
with charachange

li "อา งานแสดงคงเริ่มแล้วสินะ"

hide fireshine
show bg misc_sky_ni as front
show fireworks
with locationchange

"เมื่อทอดสายตาออกไปข้างนอกก็ถึงรู้ตัวว่ายามเย็นได้เคลื่อนคล้อยมาและผ่านไปแล้ว ทิ้งไว้เพียงช่วงยามสนธยา"

"ประกายไฟลากทะยานขึ้นสู่ท้องฟ้า เตรียมพร้อมที่จะระเบิดเป็นรูปทรงดอกไม้ของดอกไม้ไฟ"

hide fireworks
hide front
show fireshine
show yuukoshang happy_down
with locationchange

yu "ไปดูกันเถอะ!"

show yuukoshang panic_up
with charachange

yu "โอ๊ะ… ขอโทษที ลิลลี่…"

show lilly basic_ara
with charachange

show hanako_fw behind bg:
    zoom 1.05 truecenter subpixel True
    ease 22.0 zoom 1.0
show ev hanako_shanghaiwindow behind hanako_fw:
    zoom 1.05 truecenter subpixel True
    ease 22.0 zoom 1.0
with None

li "อย่าพลาดการแสดงเพราะฉันเลยนะ จากที่ได้ยินมา ที่นี่ก็ไม่ใช่จุดชมวิวที่แย่อะไรหรอก"

play music music_serene fadein 4.0

hide fireshine
hide bg
hide hanako
hide lilly
hide yuukoshang
with locationskip

"พวกเราทุกคนยกเว้นลิลลี่รีบวิ่งมาที่หน้าต่างของโรงน้ำชาเพื่อดูการแสดง"

"แสงวูบวาบของพลุหลากสีสาดส่องลงบนใบหน้าเปื้อนยิ้มของฮานาโกะกับยูโกะจนทำให้ฉันลืมมองออกไปนอกหน้าต่าง\nไปแวบหนึ่งเลย"

"ในโลกใหม่ใบนี้ ยังมีบางสิ่งที่ไม่ได้เปลี่ยนไปเลย"

"ฉันว่านั่นแหละคือเหตุผลที่โรงเรียนถึงได้จัดเทศกาลนี้อย่างยิ่งใหญ่ เพราะเป็นโอกาสที่จะแสดงให้เห็นถึง\nความเหมือนกันของทุกคน"

stop ambient fadeout 3.0

hide hanako_fw
with Dissolve(1.0)

"การแสดงจบลงเร็วไปหน่อย พลุแพงจะตายไป ต่อให้โรงเรียนจะมีงบเป็นเงินถุงเงินถังเลยก็เถอะ"

scene bg suburb_shanghaiint at bgright
with locationchange

"ก่อนที่เราจะได้ไปกินแซนด์วิชกับชาต่อ ฮานาโกะหันมาหาฉัน"

show hanako emb_downsmile_close
with charaenter

ha "เอ่อ ขะ…ขอบใจนะสำหรับวันนี้"

show hanako emb_smile_close
with charachange

ha "…แล้วก็ วันพรุ่งนี้ด้วย"

hi "ไม่เป็นไร ฉันเองก็ไม่อยากอยู่กลางฝูงชนขนาดนั้นหรอก"

hi "วันดี ๆ แบบนี้ การได้ใช้เวลาปลีกตัวจากทุกคนบ้างมันผ่อนคลายกว่าเยอะเลยนะ ว่าไหมล่ะ"

show hanako basic_normal_close
with charachange

ha "อะ…อื้ม"

hi "แต่เอาเถอะ กลับไปที่โต๊ะกันดีกว่า เดี๋ยวชาเย็นชืดกันพอดี"

show hanako basic_bashful_close
with charachange

ha "อะ…เอาสิ"

stop music fadeout 6.0

hide hanako
with charaexit

show bg suburb_shanghaiint at bgleft
with charamove

show lilly basic_smileclosed:
    yanchor 1.0 xanchor 0.5 ypos 1.2 xpos 0.2
show yuukoshang neutral_down:
    yanchor 1.0 xanchor 0.5 ypos 1.17 xpos 0.5
with locationchange

show hanako basic_smile:
    yanchor 1.0 xanchor 0.5 ypos 1.0 xpos 0.8
    easein 1.0 ypos 1.17
with charaenter

"พวกเรากลับมายังซุ้มและกินของว่างกัน"

show lilly basic_smile
with charachange

li "ฟังดูน่าประทับใจมากเลย อย่างน้อยก็ใหญ่กว่าปีที่แล้วแน่ ๆ "

show yuukoshang happy_down
with charachange

yu "ใช่ เยี่ยมไปเลยละ! ฉันไม่เคยเห็นเขาจัดแสดงได้อลังการขนาดนี้มาก่อนเลย"

yu "งานดีขึ้นทุก ๆ ปีเลย!"

show lilly basic_weaksmile
with charachange

li "แต่เกรงว่าชาจะเย็นชืดไปตอนที่ดูพลุหมดแล้วนะ"

show yuukoshang panic_up at center
with Dissolvemove(0.2)

play music music_ease fadein 0.5

yu "ตายแล้ว! เดี๋ยวชงเพิ่มให้ค่ะ ฉันผิดเองค่ะ!"

hi "ใจเย็น ๆ ก่อนครับคุณยูโกะ ไม่ใช่ความผิดใครทั้งนั้นแหละครับ"

"ฉันจิบชาจากถ้วยของฉันเพื่อพิสูจน์"

hi "ก็ไม่ได้เย็นชืดขนาดนั้นสักหน่อย เหมือนชาดำเย็นปกติมากกว่า"

show yuukoshang worried_up
with charachange

yu "จริงเหรอ"

hi "ครับ เหมือนเลย ถ้าเติมน้ำตาลสักหน่อยก็คงดี"

show yuukoshang neurotic_up
with charachange

yu "แน่ใจเหรอคะ"

hi "แน่สิ เอ้า มานั่งดื่มชาให้หมดด้วยกันดีกว่า"

show yuukoshang smile_down
with charachange

yu "อะ…โอเคค่ะ"

show yuukoshang smile_down at Transform(ypos=1.17)
with charamove

"ยูโกะดูเหมือนจะไม่ค่อยเชื่อเท่าไหร่ แต่ก็ยอมนั่งลงอยู่ดี"

"เธอตักน้ำตาลกะให้ได้ประมาณห้าช้อนชาแล้วเติมลงไปในชาของเธอ"

hi "เอ่อ ผมบอกว่าแค่นิดหน่อย…"

show yuukoshang neutral_down
with charachange

yu "ค่ะ แต่ว่าฉันชอบชาหวาน ๆ น่ะค่ะ"

"ด้วยความอยากรู้ ฉันเลยชะเง้อหน้ามองเข้าไปในถ้วยของเธอ อย่างที่คิด น้ำตาลแทบไม่ละลายในของเหลวเย็น ๆ เลย"

"เธอคนอยู่สองครั้งก่อนจะยกถ้วยขึ้นดื่มรวดเดียว ทั้งน้ำตาลและชาหมดเกลี้ยงในอึกเดียว"

show yuukoshang happy_down
with charachange

yu "จริงด้วย! ไม่ได้แย่อย่างที่คิด!"

hi "เอ่อ ก็ดีครับ…"

"ฉันหันกลับไปมองลิลลี่กับฮานาโกะ ทั้งคู่กินเสร็จไปเรียบร้อยแล้วระหว่างที่ฉันได้เห็นนิสัยของยูโกะเมื่อกี้"

"ด้วยไม่อยากให้ใครต้องรอ ฉันเลยใช้วิธีเดียวกับเธอโดยการดื่มชาที่เหลือรวดเดียวหมดถ้วย"

hi "เอาละ ดูเหมือนทุกคนจะกินเสร็จละนะ"

show lilly basic_smile
with charachange

li "เราจะกลับกันเลยไหม หรือจะสั่งเพิ่มดี"

show yuukoshang neurotic_up
with charachange

"สีหน้าของยูโกะแสดงชัดว่าไม่ใช่ความคิดที่ดีแน่ ๆ"

hi "ฉันว่าเรารีบกลับกันดีกว่านะ"

hi "เราต้องกลับก่อนเวลาปิดประตูหอด้วยนี่นะ"

show lilly basic_smileclosed
with charachange

li "อ้อ ก็จริง"

show lilly basic_smile
with charachange

li "ไว้เจอกันพรุ่งนี้นะคะคุณยูโกะ"

show yuukoshang neutral_down
with charachange

yu "พรุ่งนี้จะรอนะลิลลี่ ลาก่อนทุกคน"

stop music fadeout 9.0

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_cicadas fadein 0.5

scene bg suburb_shanghaiext_ni
with locationchange

"พวกเราเดินออกมาจากโรงน้ำชาเล็ก ๆ แล้วก้าวเข้าสู่ความมืดมิดของยามค่ำคืน"

$ renpy.music.set_volume(0.4, 1.0, channel="ambient")
scene bg suburb_roadcenter_ni
with locationchange

"ลิลลี่กับฮานาโกะกลับมานำทางอีกครั้ง แต่ภายใต้ความมืดมิด ฮานาโกะดูผ่อนคลายลงกว่าตอนขามาเล็กน้อย"

"พวกเราเดินสวนทางกับกลุ่มคนที่กำลังออกจากบริเวณโรงเรียน แต่ฮานาโกะดูเหมือนจะพาเราเลี่ยงไปตามถนน\nสายเล็ก ๆ สองสามสาย หลีกเลี่ยงกลุ่มคนส่วนใหญ่ได้สำเร็จ"

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

scene bg school_dormext_full_ni
with locationskip

"เมื่อถึงหน้าหอพักแล้วก็รู้สึกว่าโรงเรียนเงียบกว่าปกติเมื่อเทียบกับเสียงอึกทึกครึกโครมเมื่อตอนกลางวัน"

hi "โอเค ขอบใจพวกเธอมากสำหรับวันนี้ ฉันว่าฉันได้รู้อะไรหลายอย่างเลย"

show hanako emb_timid_ni at Transform(xanchor=0.5, xpos=0.59)
show lilly basic_weaksmile_ni at Transform(xanchor=0.5, xpos=0.41)
with charaenter

li "ด้วยความยินดีอย่างยิ่งเลยจ้ะ แต่ฉันคงต้องขอตัวแล้วจริง ๆ วันนี้เป็นวันที่เหนื่อยเหลือเกิน"

"นั่นสินะ วันนี้ลิลลี่ยืนแผงมาทั้งวันแถมยังเดินออกไปข้างนอกโรงเรียนอีก เดาได้เลยว่าเหนื่อยมากแน่ ๆ"

"ฉันรู้สึกผิดขึ้นมานิดหน่อยเมื่อนึกขึ้นได้ว่าวันนี้ฉันน่าจะเป็นคนเดียวในโรงเรียนที่ตื่นประมาณสิบโมงเช้า"

hi "เอาสิ"

hi "ก็ เจอกันพรุ่งนี้นะทุกคน ราตรีสวัสดิ์"

show lilly basic_cheerful_ni
with charachange

li "ราตรีสวัสดิ์จ้ะ ฮิซาโอะ"

show hanako basic_smile_ni
with charachange

ha "ระ… ราตรีหวัด"

hide hanako
hide lilly
with charaexit

"พวกสาว ๆ ก็กลับไปหอพวกเธอ และฉันก็กลับไปหอฉัน"

"พอมาคิดดูแล้ว จริง ๆ วันนี้ฉันเองก็เหนื่อยเหมือนกันแหละ"

stop ambient fadeout 2.0

scene black
with dissolve

#---------------------------------------------------------

label th_H3:

window hide None

scene black
with dissolve

$ renpy.music.set_volume(0.0, 0.0, channel="ambient")
play sound sfx_alarmclock

with Pause(1.2)

play sound sfx_impact2

window show

"เสียงปลุกดังขึ้นทะลุหูฉัน ก่อนที่จะเงียบลงทันทีด้วยกำปั้นของฉัน"

scene bg school_dormhisao
with openeye

"ร่างกายของฉันเข้าสู่ระบบอัตโนมัติ พาจิตใต้สำนึกของฉันลุกออกจากเตียงแล้วแต่งตัว"

"ขวดยาตั้งรายเรียงบนโต๊ะรอให้ฉันหยิบขึ้นมากินตามปริมาณที่ต้องกิน สิบเจ็ดเม็ดต่อวัน ทุก ๆ วัน"

scene bg school_scienceroom at bgright
with locationskip

"พอรู้ตัวอีกที ฉันก็เปิดประตูเข้าห้องเรียน 3-3 มาแล้ว ยังดีที่ได้เห็นว่าไม่ใช่แค่ฉันที่ยังล้าจากสัปดาห์งานเทศกาล"

"สีหน้าทุกคนดูสะโหลสะเหล อย่างกับพอเทศกาลจบลงแล้วความฝันในชีวิตของทุกคนได้สำเร็จลุล่วงไปแล้วยังไงยังงั้น"

"พอไม่มีอะไรให้ยึดเหนี่ยวอีก นักเรียนเหล่านั้นก็ใช้สัญชาตญาณดิบอย่างเดียวเพื่อนำพาตัวเองมายังห้องเรียน"

"ไม่ก็ฉันคงคิดมากไป"

"ฉันค่อย ๆ เดินไปยังโต๊ะของฉัน และก็ได้รู้ว่าทำไมวันนี้ห้องถึงเงียบสงบเหลือเกิน"

"โต๊ะข้าง ๆ ฉันว่างเปล่าอย่างน่าอภิรมย์ ล่ามภาษามือที่เสียงดังที่สุดในโลกยังเสด็จมาไม่ถึง"

play sound sfx_doorslam
play music music_running

show misha hips_grin:
    yalign 1.0 xanchor 0.0 xpos 1.0
    easein 0.3 xanchor 1.0
with vpunch

"ในตอนที่ฉันกำลังจะนั่ง ประตูก็เปิดผางออกเผยให้เห็นมิช่ายืนเด่นเป็นสง่า ผมทรงสว่านของเธอเด้งไปมาตามการปรากฏตัว\nที่เล่นใหญ่ เธอเหยียดแขนทั้งสองข้างขึ้นสู่ท้องฟ้า"

show misha hips_laugh at right
with charachange

mi "ยะ-ฮู้~! จบซักที!"

"เห็นได้เลยว่าไม่ใช่ทุกคนที่จะซึมหลังงานเทศกาล"

"คนทั้งห้องมองเธอ คงคิดเหมือนที่ฉันคิดนั่นแหละ"

show misha sign_confused
with charachange

"มิช่ายืนแข็งทื่ออยู่หน้าประตูโดยที่เหยียดแขนอยู่ มองไปรอบ ๆ อย่างประหม่า"

"เธอรู้ตัวแหละว่าบรรยากาศในห้องอึมครึม แต่ไม่รู้จะทำตัวยังไง"

show misha sign_confused at center
with ease_decel

"ทันใดนั้นเอง เธอก็พุ่งตัวเข้ามา"

show misha perky_sad
with charachange

mi "นี่!"

show shizu invis behind misha:
    yalign 1.0 xanchor 0.5 xpos 1.0
with None

show misha perky_sad at twoleft
show bg school_scienceroom at center
show shizu adjust_happy at tworight
with dissolvecharamove

"ขณะที่เธอเดินโซซัดโซเซเข้ามาในห้องเรียนนั้นก็เผยให้เห็นชิซูเนะที่แขนยังยกค้างจากการที่ผลักมิช่าเข้ามาอยู่"

show shizu basic_normal
with charachange

shi "…"

hi "ขอบใจสำหรับความบันเทิงนะ แต่ทำไมถึงยังไม่นั่งกันล่ะ"

show shizu behind_frown
with charachange

shi "…"

"ด้วยความที่ยังอายอยู่หน่อย ๆ มิช่าจึงใช้เวลาอยู่ครู่หนึ่งก่อนนึกได้ว่าต้องแปลให้ฟัง"

show misha sign_smile
with charachange

mi "โอ้! ช่าย! ชิจังบอกว่าเธอไม่สบอารมณ์เท่าไหร่ที่นายทิ้งพวกเราไปเมื่อสัปดาห์ก่อนน่ะ"

show misha cross_frown
with charachange

mi "พวกเรางานยุ่งมากเลยนะ!"

hi "งั้นเหรอ แล้วงานส่วนที่ฉันทำให้พวกเธอล่ะ"

show shizu cross_angry
with charachange

shi "…"

show misha hips_grin
with charachange

mi "เธอบอกว่าผลงานถือว่าเป็นของสมาชิกในสภาเท่านั้นน่ะ ในเมื่อนายปฎิเสธก็ถือว่าเธอไม่ได้ติดค้างอะไรนาย"

show misha hips_grin_close
with characlose

"มิช่าเอี้ยวตัวมากระซิบกระซาบพลางตั้งข้อสังเกต"

mi "จริง ๆ ฉันว่าเธอแค่งอนที่วันนั้นนายไม่อยู่กับเธอมากกว่าอะนะ"

show misha hips_smile_close
with charachange

mi "แต่เธอก็ชื่นชมนายมากนะที่มาช่วยงานเมื่อสัปดาห์ก่อนน่ะ"

show shizu behind_frustrated
with charachange

"พอรู้ตัวว่าถูกนินทา ชิซูเนะก็ใช้นิ้วเคาะโต๊ะจนมิช่าหันกลับไปหาเธอ"

show misha sign_smile
with charadistant

show shizu basic_angry
with charachange

show misha hips_grin
with charachange

show shizu adjust_blush
with charachange

"ฉันไม่เข้าใจภาษามือที่รัวเร็วนั่นเลยสักนิด แต่จากสีหน้าของชิซูเนะที่ดูเขินอายเล็กน้อย และมิช่าที่พยายามกลั้นขำสุด ๆ \nก็พอเดาได้อยู่"

stop music fadeout 8.0

"ระหว่างที่บทสนทนากำลังดำเนินไป ประตูก็เปิดขึ้นอีกครั้ง แต่คราวนี้เปิดมาได้เป็นผู้เป็นคนขึ้นมาก ๆ"

show hanako invis at offscreenright
with None

show bg school_scienceroom at bgleft
show shizu basic_normal at Transform(xpos=0.42)
show misha hips_smile at Transform(xpos=0.18)
show hanako emb_downtimid at right
with dissolvecharamove

"ฮานาโกะเข้ามาในห้องอย่างเงียบ ๆ แล้วปิดประตู"

show hanako emb_timid
with charachange

"เธอมองลอดผมกวาดสายตามองไปทั่วห้องเรียนอย่างรวดเร็ว"

"ตาของเราสบกัน แล้วเธอก็แข็งทื่อไปทันที เธอหลับตาลง หายใจเข้าลึก ๆ แล้วเดินตรงมาที่โต๊ะของฉัน"

show hanako cover_distant
with charachange

ha "อะ… อรุณสวัสดิ์ฮิซาโอะ"

hi "อรุณสวัสดิ์ฮานาโกะ เธอมาสายนิดหน่อยนะ"

show hanako basic_normal
with charachange

ha "ฉัน… ไปคุยกับลิลลี่มา"

show hanako basic_worry
with charachange

ha "ระ เรื่องวันนี้"

hi "โอ้ ได้รายการของลิลลี่มาแล้วใช่ไหม งั้นไปหลังเลิกเรียนเลยแล้วกัน"

show hanako emb_smile
with charachange

ha "อะ อื้ม"

hi "ฉันจะรอนะ"

"ฮานาโกะยิ้มอย่างอาย ๆ ให้ฉันแวบหนึ่ง แล้วรีบเดินไปยังที่นั่งของเธอทันที"

scene bg school_scienceroom at bgright
with shorttimeskip

play music music_normal fadein 3.0

"ระหว่างคาบก็เห็นได้ชัดว่าไม่ใช่แค่นักเรียนเท่านั้นที่หมดเรี่ยวแรงหลังเทศกาล"

"มุโต้สั่งงานจากหนังสือทิ้งไว้ให้แล้วก็ไปนั่งที่โต๊ะครู"

"ฉันลืมเรื่องพักเที่ยงไปพักหนึ่งเลย วันนี้ช่างน่าเบื่อซะจริง ๆ"

play sound sfx_normalbell

"น่าเบื่อจนสมองตื้อไปหมด และทุกคนก็ดูประหลาดใจเมื่อเสียงระฆังดังขึ้นเป็นสัญญาณบอกเลิกเรียน"

show shizu basic_normal at tworight
show misha perky_smile at twoleft
with charaenter

"พอกำลังเก็บของเข้ากระเป๋า ชิซูเนะกับมิช่าก็เข้ามาขนาบข้างและขวางทางฉันไว้"

show misha hips_grin
with charachange

mi "นี่ฮิจัง จะเข้าสภาตอนนี้ก็ยังไม่สายนะ มีงานเอกสารหลังเทศกาลที่เราต้องจัดการอีกเพียบเลย…"

hi "เอ่อ โทษทีนะมิช่า ฉัน… มีธุระน่ะ…"

show hanako invis at offscreenright
with None

show bg school_scienceroom at center
show shizu basic_normal at Transform(xpos=0.42)
show misha hips_grin at Transform(xpos=0.18)
show hanako cover_distant at right
with dissolvecharamove

"ฮานาโกะปรากฏตัวขึ้นข้างหลังฉันเหมือนรู้บท เธอถือกระเป๋าใบเล็ก ๆ และพยายามหลีกเลี่ยงการสบตากับ\nโลกภายนอก"

show misha cross_laugh
with charachange

"มิช่าตาลุกวาวแล้วหัวเราะออกมาเสียงดัง"

mi "วะฮ่าฮ่าฮ่า! นายนี่ก็ไวไม่เบาเลยนะฮิจัง~ งั้นพวกเราไม่รบกวนการเดทของนายละนะ! วะฮ่าฮ่าฮ่า!"

show shizu behind_blank
with charachange

"ฉันเห็นชิซูเนะแสดงท่าทีไม่สนใจเหตุการณ์ที่เกิดขึ้นจนเกินไปอยู่ข้างหลังมิช่าที่กำลังหัวเราะอย่างบ้าคลั่ง อาจจะคิดไปเอง\nแต่ฉันคิดว่าเธอจงใจเมินฉันอยู่แน่ ๆ"

show hanako emb_downtimid_close
with characlose

"ฉันรู้สึกถึงแรงดึงเบา ๆ ที่เสื้อ แล้วหันไปเห็นฮานาโกะจ้องมองพื้นไม่ไปไหน"

show hanako emb_timid_close
with charachange

ha "ปะ… ไปกั…"

hi "ไปละ ชิซูเนะ มิช่า ไว้เจอกัน"

hi "แล้วก็ ฉันยังไม่อยากเข้าสภาอยู่ดีนะ"

show misha cross_grin
with charachange

mi "ไม่หนุกเลย"

stop music fadeout 2.0

hide misha
hide shizu
with charaexit

show bg school_scienceroom at bgleft
show hanako emb_timid_close at center
with charamove

"มิช่ากับชิซูเนะกลับไปที่โถงทางเดินคุยภาษามือกันอย่างสนุกสนาน"

hi "เก็บของเสร็จแล้วใช่ไหม ไปกันเถอะ"

play music music_soothing fadein 4.0

scene bg school_gate
with locationskip

"นักเรียนจำนวนมากทะลักออกจากประตูโรงเรียน และมุ่งหน้าสู่ถนนเข้าเมือง"

"แปลกหน่อย ๆ ตรงที่ว่าภาพตรงหน้านี้ก็ละม้ายคล้ายโรงเรียนมัธยมทั่ว ๆ ไป แต่ภาพลวงนั้นก็จางหายไปเพราะบางคน\nมีรถเข็นหรือแขนขาที่ขาดหายไป"

"อย่างหนึ่งที่สังเกตได้คือไม่มีใครอยู่ตัวคนเดียวเลย"

scene bg school_road
with locationchange

show hanako emb_downsad_close at center
with charaenter

"พอฮานาโกะกับฉันเดินออกนอกประตูมา ฉันก็เห็นว่าเธอลดระยะห่างระหว่างเรา"

"ก็ไม่ถึงกับ “ใกล้” หรอก แต่ก็ไม่ได้ห่างเกินไป{i}นิดหน่อย{/i}เหมือนปกติ"

"เราก็ไม่ได้สนิทกันขนาดที่เธอจะเข้าใกล้เท่า ๆ กับตอนที่เธออยู่กับลิลลี่อะนะ"

"แต่ถึงตัวจะขยับเข้ามาใกล้ขึ้นหน่อยแล้ว ใจเธอก็ดูห่างออกไปแสนไกล"

"มือของเธอจับสายสะพายหนังของกระเป๋าแน่นจนเลือดข้อนิ้วเธอไม่เดิน เธอก้มหน้าลงและเม้มปากแน่น"

"สภาพเธอเหมือนกับเดินไปห้องผอ. เป็นครั้งแรกยังไงยังงั้น"

"ฉันพยายามกลั้นขำที่คิดอย่างนั้นขึ้นมา แต่ก็ไม่เป็นผล"

show hanako emb_timid_close
with charachange

ha "มะ มีอะไรเหรอ…"

"คงไม่ต้องปิดบังแล้วสินะ…"

hi "โทษที เมื่อกี้มองดูเธอเหมือนคนไปทำอะไรผิดมาอย่างงั้นน่ะ"

show hanako defarms_strain_close
with charachange

ha "มะ มะ หมายความว่าไง"

hi "ฉันว่าเธออย่าเกร็งไปเลย เราก็ไม่ได้ไปไหนไกลสักหน่อย แถมแถวนี้ก็มีแค่นักเรียนด้วยนี่ จริงไหม"

show hanako def_worry_close
with charachange

ha "อะ อื้ม"

"รู้สึกลำบากใจนิดหน่อยที่เห็นฮานาโกะดูกังวลมากขนาดนี้"

hi "แล้วเธอเองก็มาทุก ๆ สัปดาห์ด้วยนี่"

show hanako basic_worry_close
with charachange

ha "ชะ ใช่ กับลิลลี่"

"แหงแซะ “กับลิลลี่” สงสัยจริง ๆ ว่าเธอเคยออกมาข้างนอกโดยไม่มีลิลลี่สักครั้งไหม"

"ตอนแรกอาจจะดูเหมือนไม่มากเท่าไหร่ แต่ฮานาโกะก็พึ่งพาลิลลี่หนักมากจริง ๆ"

"ถ้าถึงขนาดรับมือกับการออกจากโรงเรียนโดยไม่มีลิลลี่ไม่ได้ แล้วเกิดถ้าไม่ได้มารู้จักกันแล้วเธอจะเอาตัวรอดยังไง"

"เธอจะหาคนอื่นมาพึ่งพาแทนหรือเปล่า แล้วอะไรที่ทำให้เธอเข้าหาลิลลี่กันนะ"

"เพราะว่าตาบอดหรือเปล่า หรือเพราะว่าลิลลี่ใจดีพอที่จะช่วยเธอกัน"

"ฉันสงสัยว่าจะมีใครมาทำหน้าที่ได้ดีเท่าไหมนะ"

hi "ฉันก็อยู่ด้วยนี่ไง แล้วเราก็ไม่ได้ไปไหนไกลสักหน่อย แป๊บเดียวก็ถึงแล้ว"

show hanako emb_downsmile_close
with charachange

"เลือดที่ข้อนิ้วเธอกลับมาเดินขณะที่เธอพยายามกลั้นยิ้มเอาไว้ แต่ก็เหมือนว่าจะเอาแต่กลั้นยิ้มจนคุยอะไรต่อไม่ได้"

"เราเดินเคียงข้างกันไปตามถนนที่คดเคี้ยวสู่เมือง กลุ่มนักเรียนค่อย ๆ บางตาลงไปตามทางเท้าที่เราเดิน"

"นักเรียนที่เดินเร็วกว่าก็พุ่งไปข้างหน้า ส่วนพวกที่เคลื่อนไหวช้ากว่าก็รั้งท้าย ทำให้ฝูงชนเจือจางลงจนไม่มีเหลือ"

scene bg suburb_konbiniext
with locationskip

"กว่าจะมาถึงร้านสะดวกซื้อก็เรียกได้ว่าเหลือแค่เราสองคนที่ยังอยู่"

scene bg suburb_konbiniint
with locationchange

"ฮานาโกะใช้ฉันเป็นโล่กำบังระหว่างตัวเองกับพนักงานแล้วเดินผ่านทางเดินแคบ ๆ พร้อมกับหยิบของสารพัดอย่าง\nใส่ตะกร้าของเธอ"

"ขนมปัง นม ชา… ไทม์?"

"ร้านสะดวกซื้ออะไรทำไมมีสมุนไพรขายด้วย"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide

nvl clear

nvl show dissolve

n "\n\nแต่ก็นั่นแหละ ไม่มีอะไรในเมืองนี้ที่ดูปกติเลย ซึ่งเมื่อมองย้อนกลับไปแล้ว ก็อาจจะไม่ใช่เรื่องแย่ขนาดนั้นก็ได้"

n "ทุกสิ่งช่างแตกต่างและน่าอึดอัดใจ การหมกมุ่นอยู่กับเรื่องเหล่านั้นคงไม่ใช่เรื่องที่ดีเท่าไหร่"

n "พอคิดถึงเรื่องนั้น ก็พานให้นึกถึงฮานาโกะ"

n "ไม่ว่าจะพยายามแค่ไหนก็ไม่อาจหลีกหนีรอยแผลเป็นของเธอได้ รอยแผลเป็นเหล่านั้นกวนใจฉันทุกครั้งที่ได้เห็น"

n "ถึงจะไม่ค่อยอยากยอมรับก็เถอะ แต่ฉันว่าฉันกำลังบังคับตัวเองให้พยายามมองข้ามรอยแผลเป็นเหล่านั้น"

n "ฉันเองก็มีแผลเป็นเหมือนกันนั่นแหละ รอยหยักที่ลากยาวลงมาตรงกลางอกฉันนั้นไม่มีวันจะหายไปไหน"

n "แต่ของฉันดีหน่อยตรงที่ยังซ่อนได้ง่าย"

n "\nแต่ในแง่หนึ่ง แผลเป็นของพวกเราทั้งคู่ก็เป็นเครื่องบ่งบอกว่าทำไมเราถึงได้มาที่นี่"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

window show

"…"

"ฮานาโกะโยนของชิ้นสุดท้ายลงในตะกร้าแล้วก็ยื่นมาให้ฉันพร้อมธนบัตรอย่างอาย ๆ"

show hanako emb_downtimid_close at center
with charaenter

ha "นะ นะ นาย ชะ ช่วย…"

"ฉันใช้เวลาไม่นานก็เข้าใจสิ่งที่เธอจะสื่อ"

hi "อ้อ เธออยากให้ฉันช่วยจ่ายให้สินะ"

show hanako emb_downsad_close
with charachange

"เธอพยักหน้า แต่ไม่ได้มองขึ้นมา"

"เดาว่างานนี้ปกติลิลลี่คงได้ทำเป็นประจำแหง ๆ"

hi "ได้สิ เดี๋ยวขอไปหยิบของเพิ่มนิดหน่อยนะ…"

"ฉันรีบคว้าของจำเป็นสองสามอย่างให้ตัวเอง แล้วตรงไปที่เคาน์เตอร์พร้อมกับฮานาโกะที่เดินตามมาติด ๆ"

"พนักงานพยักหน้าให้ฉันอย่างไม่แยแสขณะที่เขาสแกนสินค้า"

"ฉันว่าการทำเป็นไม่สนใจพวกเราก็เป็นวิธีหนึ่งในการรับมือกับความไม่ปกติของยามากุ คงมีนักเรียนมาที่นี่เยอะแน่ ๆ\nเพราะเป็นร้านที่อยู่ใกล้โรงเรียนที่สุด"

"พนักงานที่นี่คงจะมีวิธีรับมือกับพวกเราในแบบของเขา หรือไม่ก็อาจจะไม่ได้มีหรอก บางทีอาจจะมีแค่ฉันคนเดียว\nที่คิดมากเรื่องเพื่อนร่วมโรงเรียน"

stop music fadeout 2.0

scene bg suburb_konbiniext_ss
with locationchange

"พอซื้อของเสร็จฮานาโกะกับฉันก็เดินกลับออกมายังถนน"

scene bg school_road_ss
with locationskip

play music music_tranquil fadein 10.0

"ตอนนี้ถนนก็แทบไม่เหลือคนแล้ว นักเรียนที่เดินนำมาก่อนหน้าก็หายไปหมดแล้ว และยังไม่มีใครกลับมา"

"และเมื่อมีแค่โรงเรียนที่อยู่ข้างหน้าบนถนนเส้นนี้ ทำให้ไม่มีใครอยู่แถวนี้เลย"

show hanako def_worry_close_ss at center
with charaenter

"ความโล่งนี้มีผลต่อฮานาโกะชัดเจน แขนของเธอที่แนบลำตัวแต่ละข้างมีมือที่ถือถุงอยู่ เธอกลับมามองตรงตามปกติ\nไม่ได้ก้มหน้าแล้ว…"

"ราวกับว่าเธอกำลังเพลิดเพลินกับการเดินครั้งนี้เลยทีเดียว"

hi "แล้วซื้อของแปลก ๆ พวกนี้มาทำไมเหรอ เครื่องเทศงี้ เอาไปทำอะไรที่โรงเรียน"

show hanako basic_normal_close_ss
with charachange

ha "ฉัน… บางที… ฉันก็จะทะ… ทำกับข้าวกินน่ะ"

hi "อ๋อ เอ้อฉันเองก็ด้วย แต่… เครื่องเทศอะนะ"

hi "ไม่ยากไปหน่อยเหรอ"

show hanako emb_blushing_close_ss
with charachange

ha "กะ ก็ไม่ขนาดนั้น"

hi "อื้ม ดีแล้ว สงสัยเธอต้องสอนฉันบ้างแล้วละ"

show hanako emb_smile_close_ss
with charachange

ha "ดะ ได้สิ"

"ก็ดูท่าไม่ค่อยแน่ใจสักเท่าไหร่ว่าจะสอนให้จริงไหม แต่ให้จี้ถามก็ใช่เรื่อง"

"อย่างน้อย ๆ เธอก็ดูมีความสุขกว่าตอนขามาละนะ"

"แค่นั้นก็ทำให้ฉันมีความสุขขึ้นมาหน่อยหนึ่งแล้ว"

scene bg school_dormext_full_ss
with shorttimeskip

show hanako basic_normal_close_ss at center
with charaenter

"ฮานาโกะกับฉันช่วยกันแยกข้าวของใส่ถุงตามที่แต่ละคนซื้อมาอยู่หน้าหอพักหญิง"

"พอเทียบกันแล้ว ของฉันดูบ้าน ๆ ไปเลย"

hi "บอกเลย นี่ฉันอายเลยนะเนี่ย…"

show hanako defarms_shock_close_ss
with charachange

ha "มะ ไม่นะ ฉันไม่ได้… ฉันแค่…"

hi "ล้อเล่น ๆ"

show hanako def_worry_close_ss
with charachange

hi "ฉันมีการบ้านที่ดองไว้สัปดาห์ที่แล้วที่ต้องทำ เพราะงั้นเดี๋ยวต้องไปละ"

hi "ขนไปไหวใช่ไหม"

show hanako cover_bashful_close_ss
with charachange

ha "อะ อื้ม"

hi "แน่นะ โอเค งั้นไว้เจอกันพรุ่งนี้"

show hanako basic_smile_close_ss
with charachange

ha "บะ บาย"

hide hanako
with charaexit

stop music fadeout 7.0

"พวกเราแยกทางกัน และฉันก็กลับห้องของฉัน"

scene bg school_dormhisao_ss
with locationskip

"กองงานวางสุมอยู่บนโต๊ะฉันรอคอยการสะสาง ด้วยความวุ่นวายตลอดสัปดาห์ที่ผ่านมาฉันแทบไม่มีเวลาได้ตามงานเลย"

"ฉันพยายามเรียนตามให้ทันตอนที่อยู่โรงพยาบาล แต่เนื้อหาบางอย่างฉันก็ไม่เคยเห็นมาก่อนแม้แต่ตอนที่อยู่โรงเรียนเก่า"

"ฉันเปิดกระป๋องเครื่องดื่มแล้วเริ่มลุยงานทันทีโดยไม่มีการเตรียมการใด ๆ"

scene black
with dissolve

#---------------------------------------------------------

label th_H4:

scene black
with None

play music music_daily fadein 6.0

scene bg school_dormhisao
with locationchange

# "The days are really starting to heat up."
"ช่วงนี้อากาศเริ่มร้อนขึ้นแล้ว"

# "This morning, I awoke covered in sweat."
"เช้านี้ฉันตื่นมาพร้อมเหงื่อท่วมตัว"

# "By the time the student body starts leaving their dorms for breakfast and morning duties, the sun has taken full effect; oddly, that puts me in high spirits."
"พอถึงเวลาที่นักเรียนเริ่มออกจากหอพักไปทานอาหารเช้าและทำกิจวัตรประจำวันตอนเช้า แสงแดดก็สาดส่องเต็มที่\nแปลกที่ว่าแสงแดดนั้นกลับทำให้ฉันกระปรี้กระเปร่า"

# "It's not even eight, yet I feel that this day is going to be one of those pleasant, tranquil, warm ones."
"ยังไม่แปดโมงด้วยซ้ำ แต่ฉันกลับรู้สึกว่าวันนี้จะต้องเป็นวันหนึ่งที่น่ารื่นรมย์ สงบสุขและอบอุ่น"

# "If I weren't at a school that considered every absence from class as a sign of a life-threatening situation, I'd consider skipping the whole day and just relaxing in the school gardens."
"ถ้าไม่ติดว่าฉันอยู่ในโรงเรียนที่มองว่าการขาดของนักเรียนอาจเป็นสัญญาณที่อาจอันตรายถึงชีวิต ฉันก็คงคิดที่จะ\nโดดเรียนทั้งวันหลบไปพักผ่อนอยู่ที่สวนของโรงเรียนไปแล้ว"

# "Yes, today will be a genuinely lazy day."
"อืม วันนี้คงเป็นวันที่ไม่อยากทำอะไรเลยจริง ๆ"

# "For a second, I stop in mid-stretch, and consider the nurse's warning about exercise. Maybe I should have kept up those morning jogs."
"ฉันหยุดยืดตัวกะทันหันแล้วนึกถึงคำเตือนของคุณพยาบาลเรื่องการออกกำลังกาย ออกไปวิ่งเหยาะ ๆ ช่วงเช้าต่อ\nน่าจะดี"

# "Running with someone like Emi might have been a little testing, but if I worked at my own pace…"
"จะให้วิ่งกับคนแบบเอมิก็ดูจะเหนื่อยไปหน่อย แต่ถ้าวิ่งเองเท่าที่ฉันไหวละก็…"

# "Ah, who am I kidding? I couldn't stick to something like that without some kind of motivation."
"เอ้อ นี่ฉันคิดว่าตัวเองเป็นใครกัน ฉันคงมุ่งมั่นกับอะไรแบบนั้นไม่ได้นานหรอกถ้าไม่มีแรงจูงใจอะไรเลย"

# "It's not like I sit around all day. The walk to and from the convenience store counts as exercise, right? Especially the walk back up the hill…"
"ฉันเองก็ไม่ได้นั่งอยู่เฉย ๆ ทั้งวันนะ การเดินไปกลับร้านสะดวกซื้อก็นับเป็นการออกกำลังกายใช่ไหมล่ะ โดยเฉพาะ\nขากลับที่เดินขึ้นมา…"

# "Yeah, it's no big deal. Compared to months lying in a hospital bed I'm getting plenty exercise."
"อืม ไม่เห็นเป็นไรเลย ถ้าให้เทียบกับตอนที่นอนติดเตียงอยู่โรงพยาบาลหลายเดือน นี่ก็ถือว่าฉันได้ออกกำลังกาย\nเยอะแล้ว"

scene bg school_scienceroom
with shorttimeskip

# "It seems that I'm not alone in my appreciation of the day."
"ดูเหมือนว่าฉันไม่ได้เป็นคนเดียวที่นึกยินดีกับวันนี้"

# "Nearly every member of the class is glancing through the window and into the tantalizing sky."
"นักเรียนเกือบทุกคนในชั้นเรียนกำลังมองผ่านหน้าต่างออกไปยังท้องฟ้าที่ดึงดูดใจ"

# "Even the steadfast Shizune seems to lack her usual vigor for schoolwork."
"แม้แต่ชิซูเนะที่ขยันก็ดูขาดความกระตือรือร้นในการเรียนต่างจากทุกที"

# "Misha, as brazen as ever, has even unbuttoned the top buttons of her shirt and is fanning herself with a note book."
"มิช่าที่บ้าบิ่นอยู่แล้ว ถึงกับปลดกระดุมเสื้อสองเม็ดบนออกและกำลังใช้สมุดพัดคลายร้อนให้กับตัวเอง"

# "I must have been staring, as she's now sticking her tongue out at me."
"ฉันน่าจะจ้องนานไปหน่อย เพราะเธอแลบลิ้นปลิ้นตาใส่ฉัน"

# "However, she shows no signs of halting her efforts, nor is she trying to hide the fact."
"แต่เธอก็ไม่ได้แสดงท่าทีว่าจะหยุดเลยแม้แต่น้อยอย่างเปิดเผย"

play sound sfx_normalbell

# "The lunch bells seem to catch everyone by surprise, and the class empties at a much slower pace than usual."
"เสียงระฆังพักเที่ยงเหมือนจะทำให้ทุกคนประหลาดใจ และคนก็ออกจากห้องเรียนช้ากว่าปกติมาก"

# "The heat seems to be draining the need to rush from everyone."
"ดูเหมือนว่าความร้อนกำลังพรากความรีบร้อนไปจากทุกคน"

stop music fadeout 8.0

# "Well, almost everyone."
"ก็แค่เกือบทุกคนอะนะ"

show hanako emb_emb
with charaenter

# ha "H… Hisao?"
ha "ฮะ… ฮิซาโอะ"

# hi "Hey there Hanako, what can I do for you today?"
hi "ไงฮานาโกะ มีอะไรให้ช่วยไหมวันนี้"

# "Hanako already has a lunch bag in hand."
"ฮานาโกะถือถุงข้าวกลางวันไว้ในมือ"

# "I don't have to be a detective to work out where this is going."
"ไม่ต้องฉลาดอย่างนักสืบก็รู้ว่าเรื่องจะเป็นยังไงต่อ"

show hanako emb_smile
with charaenter

# ha "Um… would you like to have lunch with us again?"
ha "เอ่อ… นายอยากจะไปกินข้าวกับพวกเราอีกไหม"

show hanako basic_bashful
with charaenter

# ha "I… I brought enough for everyone…"
ha "ฉะ… ฉันเตรียมมาเผื่อทุกคนเลย"

# hi "Awesome. You don't have to be so stiff about it though."
hi "ดีเลย แต่ไม่ต้องเกร็งขนาดนั้นก็ได้นะ"

show hanako basic_normal
with charaenter

# ha "Ah… right."
ha "อ่า… อื้ม"

# hi "I take it we're going to the tea room?"
hi "แปลว่าเราจะไปห้องน้ำชากันใช่ไหม"

show hanako cover_worry
with charaenter

# ha "P… please."
ha "ระ… รบกวนด้วยนะ"

show hanako basic_normal
with charaenter

# ha "Lilly said she'll meet us in there, so we should… should…"
ha "ลิลลี่บอกว่าเธอจะรอเราที่นั่นน่ะ เพราะงั้นเราควร… ควร…"

# hi "Should?"
hi "ควร?"

show hanako emb_smile at center
with charaenter

# ha "…should go ahead together…"
ha "…ควรไปด้วยกัน…"

# hi "Sounds like a plan. This heat has made me pretty hungry."
hi "ฟังดูดีนี่ อากาศร้อนแบบนี้ก็ชักหิวแล้วสิ"

# "Hanako breathes a sigh of relief, and I gather my things together."
"ฮานาโกะถอนหายใจโล่งอก ส่วนฉันก็เก็บข้าวของ"

scene bg school_miyagi
with locationskip

play music music_happiness fadein 1.0

# "As usual, the aura of the tea room is refreshing, feeling isolated from the rest of the world."
"และเช่นเคย บรรยากาศในห้องน้ำชานั้นแสนสดชื่นราวกับถูกตัดขาดจากโลกภายนอก"

# "Then again, the usual din of the school seems to be a bit subdued; most likely from laziness promoted by heat exhaustion."
"แต่ก็นะ เสียงอึกทึกตามปกติในโรงเรียนดูจะเบาลงไปหน่อย น่าจะเป็นเพราะความขี้เกียจที่เกิดจากความเพลียแดด\nนั่นแหละ"

# "Hanako slowly spreads her food on the table, intently focusing on every little movement, as if she's trying to keep her mind off other thoughts."
"ฮานาโกะค่อย ๆ จัดแจงอาหารของเธอลงบนโต๊ะ จดจ่ออยู่กับทุก ๆ การเคลื่อนไหวเล็ก ๆ น้อย ๆ ราวกับว่าเธอกำลัง\nพยายามเบี่ยงเบนความสนใจจากความคิดอื่น ๆ"

# "It's not much, but I can tell from her demeanor that she has prepared everything with utmost care."
"อาจไม่ใช่ของดีเด่อะไร แต่ฉันก็สัมผัสได้จากท่าทางว่าเธอเตรียมทุกอย่างมาอย่างประณีตที่สุด"

# hi "I guess Lilly isn't here yet. Should we start without her?"
hi "ลิลลี่น่าจะยังไม่มา เริ่มกินก่อนเลยไหม"

show hanako emb_timid:
    center
    ypos 1.17
with charaenter

# ha "S-she'll be here soon…"
ha "อะ อีกเดี๋ยวเธอก็มาแล้ว…"

show hanako emb_downtimid
with charachange

# "Hanako struggles with the lid of the container of rice."
"ฮานาโกะพยายามเปิดฝากล่องข้าวแต่ก็ไม่เป็นผล"

# hi "Here, let me help with that…"
hi "มา ขอลองเปิดหน่อย…"

# "I take the container from Hanako's hands, and try to force open the lid."
"ฉันหยิบกล่องข้าวมาจากมือฮานาโกะแล้วออกแรงเปิดฝากล่องข้าว"

# "Try as I might, it seems wedged shut."
"ลองจนสุดกำลังแล้ว แต่ก็ดูเหมือนจะปิดแน่นสนิทเลย"

# hi "Let me guess, did you put this in while the rice was still hot?"
hi "ให้เดานะ เธอปิดฝาตอนข้าวยังร้อนอยู่ใช่ไหมเนี่ย"

show hanako emb_sad
with charachange

# ha "Y-yes. I was in a rush…"
ha "ชะ ใช่ พอดีฉันรีบน่ะ…"

# "I put the container on the table between us."
"ฉันวางกล่องข้าวลงบนโต๊ะ"

# hi "I thought so. It looks like this is wedged shut. We'll need some hot water to get it open."
hi "ก็ว่างั้นแหละ เหมือนกล่องจะปิดแน่นสนิทเลย ต้องหาน้ำร้อนมาราดเปิด"

# hi "But that could be a pain in here. We'd get water everywhere."
hi "แต่ให้ทำในนี้น้ำคงหกเลอะเทอะไปทั่ว ไม่ดีแน่"

# li "Well, in that case, how about I contribute to today's meal?"
li "ถ้าอย่างนั้นละก็ ทานส่วนที่ฉันเตรียมมาไหมล่ะจ๊ะ"

show lilly invis at left
with None

show hanako emb_smile:
    tworight
    ypos 1.17
show bg school_miyagi at bgright
show lilly basic_cheerful at twoleft
with dissolvecharamove

# "At the door, Lilly smiles while holding up a bag stocked with various buns and bread rolls. I can't help but do the same."
"ลิลลี่ยืนยิ้มอยู่ตรงประตูพร้อมชูถุงที่เต็มไปด้วยขนมปังและขนมปังโรลหลากชนิด ฉันอดไม่ได้ที่จะยิ้มตามไปด้วย"

show lilly basic_smileclosed
with charachange

# li "Since you two had a change of plans because of me, I thought I would bring a little something."
li "ในเมื่อพวกเธอทั้งคู่ยอมเปลี่ยนแผนมาเพื่อฉัน ฉันเลยคิดว่าควรเตรียมอะไรมาสักหน่อยน่ะ"

# hi "Thanks, Lilly. Here, let me get that for you…"
hi "ขอบใจนะลิลลี่ ฉันช่วยถือให้นะ…"

show lilly basic_smileclosed at Transform(ypos=1.2)
with charamove

# "With a little guidance, Lilly's bread assortment joins Hanako's rice-less platter. I hastily make some tea to complete the picture."
"ด้วยความช่วยเหลือเล็กน้อย ขนมปังหลากชนิดของลิลลี่ก็ถูกจัดวางรวมกับอาหารที่ไร้ข้าวของฮานาโกะ ฉันรีบชงชา\nเพื่อเติมเต็มมื้ออาหารให้สมบูรณ์" #ขอไปนอนคิดสักสองสามคืน w/ a little guidance, ...

# hi "Well, I'm looking forward to this."
hi "อืม น่ากินดีนะเนี่ย"

show hanako emb_downtimid
with charachange

# "As I take a bite, I notice Hanako trying her hardest to not look like she is looking at me."
"ขณะที่ฉันกินคำแรกก็สังเกตเห็นว่าฮานาโกะพยายามอย่างเต็มที่ที่จะไม่มองมาที่ฉัน"

# "It's nothing special, but then again I can't really complain. I'm pretty lazy when it comes to cooking for myself."
"ก็เป็นของกินธรรมดา ๆ แต่ก็ว่าไม่ได้ ฉันเองก็ค่อนข้างขี้เกียจเวลาต้องทำอาหารกินเอง"

# hi "Not bad, I guess this is made with the stuff you bought yesterday?"
hi "ไม่เลวนี่ เดาว่าใช้ของซื้อไปเมื่อวานทำใช่ไหม"

show hanako emb_blushtimid
with charachange

# ha "Y-yes."
ha "ชะ ใช่"

# "Hanako's eyes shout at me, begging for some kind of feedback."
"สายตาของฮานาโกะจ้องมาที่ฉันราวกับขอความเห็นบางอย่าง"

# hi "Well it was clearly worth it. Thanks, Hanako."
hi "ก็คุ้มละที่ซื้อมา ขอบใจนะฮานาโกะ"

show hanako cover_bashful
with charachange

# ha "I… I wanted to show you this… after yesterday…"
ha "ฉัน… ฉันอยากให้นายเห็น… หลังจากที่เมื่อวาน…"

# hi "It's okay. I was just a little surprised at the stuff you were buying."
hi "ไม่เป็นไรหรอก ฉันแค่แปลกใจนิดหน่อยกับของที่เธอซื้อน่ะ"

show lilly basic_weaksmile
with charachange

# li "Hanako's always liked to experiment when it comes to food. I think it's good… most… of the time."
li "ฮานาโกะชอบทดลองทำอาหารน่ะ ฉันว่าก็ออกมาดีนะ… ส่วนมาก… อะนะ"

# "While Lilly's smile doesn't waver, the slight change in her tone tells me that things have not gone so well in the past."
"แม้รอยยิ้มของลิลลี่จะยังเหมือนเดิม แต่น้ำเสียงของเธอที่เปลี่ยนไปเล็กน้อยทำให้รู้ว่าก่อนหน้านี้คงไม่ค่อยราบรื่น\nสักเท่าไหร่"

# "And it's not like Hanako has many people to sample her cooking…"
"ก็ใช่ว่าจะมีใครที่ไหนมาชิมอาหารที่ฮานาโกะทำนี่นะ…"

stop music fadeout 7.0

# "Hang on… was Lilly waiting for me to go first? She didn't start eating until after I said it was all right…"
"เดี๋ยวนะ… ไม่ใช่ว่าลิลลี่รอให้ฉันกินก่อนใช่ไหมเนี่ย ตอนก่อนที่ฉันจะบอกว่าโอเคนี่เห็นยังไม่ได้แตะเลย…"

# "Her cheeky grin tells me that this was a deliberate action on her part. I'll have to try and work out how to get one over her in the future, to make up for this."
"รอยยิ้มเจ้าเล่ห์ของเธอบ่งบอกว่าเธอจงใจนั่นแหละ ฉันคงต้องหาวิธีเอาคืนเธอจากเรื่องนี้ให้ได้"

# hi "Well, it's good, and that's all that counts, right?"
hi "ก็อร่อยดี แค่นั้นก็พอแล้วนี่ จริงไหม"

show hanako basic_smile
with charachange

# ha "R-right."
ha "อะ อื้ม"

show lilly basic_smileclosed
with charachange

# "Lilly, satisfied at not being the first to sample Hanako's creation, begins to consume the food in front of her."
"ลิลลี่ที่พอใจกับการที่ไม่ใช่คนแรกที่ได้ลิ้มลองฝีมือของฮานาโกะเริ่มลงมือกินอาหารตรงหน้าทันที"

# "I find myself staring as I watch her chopsticks gently touch the plate, their tips delicately poking and tracing to quickly ascertain the positions of the food as she dexterously picks it up."
"ฉันคอยจ้องมองไปตามตะเกียบของเธอที่แตะลงบนจานอย่างแผ่วเบา ปลายตะเกียบนั้นเขี่ยและลากเบา ๆ เพื่อระบุ\nตำแหน่งโดยคร่าว ๆ จากนั้นเธอก็คีบอาหารขึ้นมาอย่างคล่องแคล่ว"

# "One might think she were a child playing with her food if not for the situation, though she does it with such care and thoughtlessness that it's obvious this is simply how she eats this kind of meal."
"ถ้าไม่ใช่บริบทอย่างนี้แล้วบางคนอาจจะคิดว่าเธอกำลังเล่นของกินเหมือนเด็ก ๆ แต่ต่อให้จะคิดอย่างนั้น ท่าทางของเธอ\nก็เป็นไปอย่างเรียบร้อยและสบาย ๆ จนเห็นได้ชัดว่านี่เป็นเพียงวิธีการกินอาหารแบบนี้ของเธอเท่านั้นเอง"

# "Not wanting to miss out, I start filling up myself."
"ด้วยไม่อยากจะตามใครไม่ทัน ฉันจึงหันมากินต่อ"

show hanako emb_downsmile
with charachange

# "Hanako takes a different approach, waiting until Lilly and I have our hands clear before quickly snatching up her share."
"ฮานาโกะใช้วิธีที่ต่างออกไป เธอรอจนกระทั่งลิลลี่กับฉันหยิบกันจนเสร็จแล้วค่อยรีบฉวยส่วนของเธอไปอย่างรวดเร็ว"

show hanako emb_smile
with shorttimeskip

play music music_dreamy fadein 4.0

# "Before long the containers are empty, save for the still-shut rice container."
"ไม่นานนักของกินในกล่องก็หมดเกลี้ยง เหลือเพียงกล่องข้าวที่ยังคงปิดสนิท"

show lilly basic_smile
with charachange

# li "Thank you Hanako, that was filling."
li "ขอบคุณนะฮานาโกะ อิ่มมากเลย"

show hanako basic_smile
with charachange

# ha "N-no… thank you for the bread…"
ha "มะ ไม่หรอก… ต้องขอบคุณเธอเรื่องขนมปังต่างหาก…"

# hi "Yes, it would have been a disaster if not for that."
hi "นั่นสิ คงแย่แน่ ๆ ถ้าไม่มีมาน่ะ"

show lilly basic_planned
with charachange

# li "You're both welcome."
li "ด้วยความยินดีทั้งคู่จ้ะ"

show lilly basic_weaksmile
with charachange

# li "But now, I must be getting back. It's far too easy to be late after eating here."
li "แต่ตอนนี้ฉันต้องขอตัวก่อนนะ มานั่งกินข้าวที่นี่ทีไรเผลอแป๊บเดียวก็สายทุกทีเลย"

# hi "Yeah, I see what you mean. I think we'll just clean up here and then head off."
hi "อืม เข้าใจ ๆ กะว่าเก็บของเสร็จแล้วก็จะไปเหมือนกัน"

show lilly basic_smileclosed at twoleft
with dissolvecharamove

# li "Well then, good day."
li "ถ้างั้นก็ โชคดีจ้ะ"

hide lilly
with charaexit

show hanako basic_smile:
    center
    ypos 1.17
show bg school_miyagi at center
with charamove

# "Lilly leaves, her cane tapping away down the quiet hallway."
"ลิลลี่ออกจากห้องไป เสียงไม้เท้าของเธอเคาะดังเป็นจังหวะไปตามโถงทางเดินที่เงียบสงบ"

# "Hanako and I quickly pack our things and stay seated, waiting for the bell."
"ฮานาโกะกับฉันรีบเก็บของของพวกเราแล้วนั่งรอระฆังดัง"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene bg misc_sky at Fullpan(20.0)
with locationchange

# "Together, we stare out the window and into the endless azure sky."
"เราสองคนจ้องมองออกไปนอกหน้าต่างสู่ท้องฟ้าสีครามอันไร้ที่สิ้นสุด"

play sound sfx_warningbell

# "If it weren't for the pealing of the bells, I would have sworn that time had stopped."
"ถ้าไม่ได้ยินเสียงระฆังดัง ฉันคงคิดว่าเวลาหยุดเดินไปแล้วเสียอีก"

# "The urge to skip class rises in my gut."
"ความอยากโดดเรียนเริ่มก่อตัวในใจฉัน"

# "I shoot a glance at Hanako, who shows no signs of moving either."
"ฉันหันไปมองฮานาโกะ ซึ่งยังนิ่งไม่ไหวติงเช่นกัน"

# ha "Not… just yet…"
ha "ขอ… อยู่ต่ออีกแป๊บนึง…"

$ renpy.music.set_volume(1.0, 3.0, channel="music")

scene bg school_miyagi
show hanako basic_smile:
    center
    ypos 1.17
with shorttimeskipsilent

# "The interval between the warning bells and the end of lunch bells passes in the blink of an eye."
"ช่วงเวลาระหว่างเสียงระฆังเตือนให้เข้าห้องกับเสียงระฆังหมดเวลาพักเที่ยงผ่านไปในพริบตาเดียว"

# hi "We really should go… people will freak out and start a search party if we skip…"
hi "เราต้องไปจริง ๆ แล้วละ… ไม่งั้นคนน่าจะแตกตื่นแล้วออกตามหาแน่ถ้าเราโดดเรียน…"

show hanako basic_distant
with charachange

# "Hanako sighs."
"ฮานาโกะถอนหายใจ"

show hanako basic_normal
with charachange

# ha "You're right."
ha "ก็จริง"

show hanako basic_normal at center
with charamove

# "Slowly, she rises to her feet, and I follow suit."
"เธอค่อย ๆ ลุกช้า ๆ และฉันก็ลุกตาม"

scene bg school_staircase2
with locationskip

# "Silently, we make our way up the old stairs to the third floor and then to our classroom."
"เราสองคนเดินขึ้นบันไดเก่า ๆ ไปยังชั้นสามอย่างเงียบ ๆ แล้วตรงไปยังห้องเรียนของเรา"

scene bg school_hallway3
with locationchange

play sound sfx_dooropen

# "At the door, I take point and open the door ahead of Hanako, bowing my head down in apology in advance."
"พอถึงหน้าห้องฉันก็มายืนหน้าฮานาโกะเปิดประตูพร้อมก้มหัวขอโทษล่วงหน้า"

scene bg school_scienceroom at center
with locationchange

stop music fadeout 5.0

# hi "I'm sorry we're late, teacher."
hi "ขอโทษที่เข้าสายครับครู"

play sound sfx_doorclose

# "I am greeted not by stern words, nor by an angered instruction to take my seat, but simply by the silence created by fifteen or so students trying not to laugh."
"ไม่มีคำพูดอันแข็งกร้าวหรือคำสั่งให้ไปนั่งที่ด้วยความโกรธตอบกลับมา แต่มีเพียงความเงียบที่เกิดจากนักเรียนประมาณ\nสิบห้าคนที่กลั้นขำ"

# "Mutou, ever tardy, has yet to arrive. However, the fact that Hanako and I have arrived together is blatantly obvious."
"มุโต้สายเสมอยังไม่มาถึง แต่ฉันกับฮานาโกะที่มาด้วยกันนั้นมาถึงอย่างชัดแจ้งแล้ว"

show misha hips_grin at center
with charaenter

# mi "Pff… pffwa…"
mi "พรูด… วะฮะ…"

# "Make that about fourteen students trying, and one student failing."
"เอาใหม่ ประมาณสิบสี่คนที่กลั้นอยู่ และอีกคนที่ไม่ไหวละ"

play music music_comedy

show misha cross_laugh
with charachange

# mi "Pft-bwahahaha! The lovers return~!"
mi "พรูด วะฮ่าฮ่าฮ่า! คู่รักเขามาโน่นแล้ว~!"

show misha hips_laugh
with charachange

# mi "WAHAHAHA~!"
mi "วะฮ่าฮ่าฮ่า~!!"

# hi "Yeah, thanks. You can calm down now."
hi "เออขอบใจ พอได้ละ"

hide misha
show hanako invis_close:
    center
    xpos 1.0
with charaexit

show bg school_scienceroom at bgleft
show hanako emb_downsad_close:
    xpos 0.8
with dissolvecharamove

# "I step through the door, and realize that Hanako is firmly pressed against my back, hiding herself from the class."
"พอก้าวผ่านประตูเข้าไปก็รู้ตัวว่าฮานาโกะกำลังแนบชิดติดแผ่นหลังฉันเพื่อซ่อนตัวจากเพื่อนร่วมชั้น"

show hanako invis_close:
    xpos 0.7
with dissolvecharamove

# "With my steps coming closer to my desk, she eventually breaks from me and stiffly walks to her own. Her efforts to mentally block everyone's presence from her mind are written fairly clearly on her face."
"พอเริ่มใกล้ที่นั่งฉันแล้วเธอก็ยอมผละจากฉันแล้วเดินตัวแข็งทื่อไปยังโต๊ะของเธอเอง ความพยายามที่จะกีดกั้นทุกคน\nออกจากความคิดนั้นปรากฏชัดเจนบนใบหน้าของเธอ"

scene bg school_scienceroom at bgright
with charamove

# "Quickly checking the door for any signs of the teacher's arrival, I make a trip to Hanako's desk and whisper in her ear."
"ฉันเหลือบมองประตูอย่างรวดเร็วเพื่อดูว่าครูมาหรือยัง ก่อนจะรีบเดินไปที่โต๊ะของฮานาโกะแล้วกระซิบข้างหูเธอ"

# hi "Don't worry about Misha, she's always like this. I enjoyed myself today. Don't sweat it, okay?"
hi "ไม่ต้องไปคิดมากเรื่องมิช่าหรอก เธอก็เป็นงี้ตลอดแหละ วันนี้ฉันสนุกมากเลย เพราะงั้นอย่าเครียดเลยนะ โอเคไหม"

# "Hanako nods her head behind her folded arms, but still doesn't show her face."
"ฮานาโกะพยักหน้าที่ฟุบกับโต๊ะอยู่"

play sound sfx_dooropen

show muto invis at tworight
with None

show muto normal at center
show bg school_scienceroom at center
with dissolvecharamove

# "I yearn to stay and console her more, but Mutou picks this exact moment to enter the class, halfway through his lecture, as if he started it in the hallway."
"ฉันอยากอยู่ปลอบใจเธอมากกว่านี้ แต่มุโต้ก็เข้ามาในห้องพอดีพร้อมกับบรรยายไปครึ่งทางแล้ว ราวกับว่าเขา\nเริ่มบรรยายตั้งแต่ในโถงทางเดิน"

show muto smile at center
with charaenter

# mu "…which, of course, is directly proportional to the charge but inversely proportionally to the square of the distance…"
mu "…ซึ่งแน่นอนว่า แปรผันตรงกับประจุ แต่แปรผกผันกับระยะทางกำลังสอง…"

hide muto
with charaexit

play sound sfx_doorclose

# "He's so engrossed in his speech that he doesn't even notice me sneaking back into my seat from Hanako's desk."
"เขามัวแต่สนใจกับการบรรยายของตัวเองจนไม่ทันสังเกตเห็นฉันที่กำลังย่องจากโต๊ะฮานาโกะกลับไปนั่งที่"

# "While Mutou's spiel rambles on, Misha leans over to me."
"ในขณะที่มุโต้ยังคงบรรยายไปเรื่อยเปื่อยนั้นมิช่าก็เอนตัวเข้ามาหาฉัน"

show misha invis at offscreenleft
with None

show misha perky_smile_close:
    xanchor 0.5 xpos 0.16
with dissolvecharamove

# mi "The teacher may not have noticed your tardiness, but I did."
mi "ครูอาจจะไม่เห็นว่านายมาสาย แต่ฉันเห็นนะ"

# "That much is obvious from the show you just put on."
"ก็เห็นชัดตั้งแต่ที่เธอทำเมื่อกี้ละนะ"

show misha hips_grin_close
with charachange

# mi "I have been instructed to let you off the hook for today, but only on one condition."
mi "ฉันรับคำสั่งมาว่าวันนี้ให้ปล่อยเธอไปก่อน แต่มีเงื่อนไขข้อหนึ่ง"

# hi "Oh? And what would that be?"
hi "โอ้ แล้วเงื่อนไขที่ว่าคือ?"

show misha sign_smile_close
with charachange

# mi "You have to help us this afternoon~!"
mi "นายจะต้องมาช่วยเราช่วงบ่ายนี้~!"

# "I crane my neck to look over Misha's shoulder."
"ฉันชะเง้อคอมองข้ามไหล่ของมิช่าไป"

# "Shizune is conveniently not making eye contact with me."
"ชิซูเนะไม่ยอมสบตาราวตั้งใจเลี่ยง"

# hi "Fine. Just for today."
hi "ก็ได้ แค่วันนี้เท่านั้นนะ"

# hi "I've already told you I'm not joining the council, remember?"
hi "ฉันบอกเธอไปแล้วนะว่าฉันไม่เข้าสภาน่ะ จำได้ไหม"

show misha hips_grin_close
with charachange

# mi "Of course! Doing so could be considered… um, considered…"
mi "จำได้สิ! การทำแบบนั้นอาจจะถือว่า… เอ่อ ถือว่าเป็นการ…"

show misha perky_confused_close
with charachange

# "She looks down at her notebook, obviously looking for her place in her script."
"เธอก้มมองสมุดจดของเธอ แน่นอนว่าเพื่อหาคำตอบตามบทที่เตรียมมา"

show misha hips_grin_close
with charachange

# mi "…under duress and hence would be against regulations."
mi "…ขู่เข็ญ ซึ่งขัดต่อกฎระเบียบ"

# hi "How very strange of you to be considerate of the regulations now."
hi "แปลกเนอะที่เธอมาสนใจเรื่องกฎระเบียบอะไรตอนนี้น่ะ"

show misha sign_smile_close
with charachange

# mi "Things should be done by the book!"
mi "ทุกอย่างควรทำตามกฎระเบียบนะ!"

show misha perky_smile_close
with charachange

# mi "It's just that the book hasn't been written for every situation, so there are times when it can be ignored."
mi "แค่ว่ากฎไม่ได้เขียนไว้ครอบคลุมทุกสถานการณ์ เพราะงั้นอาจมีบางกรณีที่สามารถละเลยกฎได้"

# hi "And yet, you two wonder why no one else wants to be in the Student Council…"
hi "เนี่ย แล้วก็มาสงสัยว่าทำไมถึงไม่มีใครอยากเข้าสภาเลย…"

stop music fadeout 3.0

show misha hips_frown_close
with charachange

with Pause(0.3)

show misha invis at offscreenleft
with dissolvecharamove

hide misha
with None

# "After poking her tongue out at me, Misha returns to her workbook, and we battle our way through the latter half of the school day."
"หลังจากแลบลิ้นปลิ้นตาใส่ฉัน มิช่าก็หันไปอยู่กับสมุดแบบฝึกหัดของเธอต่อ แล้วเราก็ฝ่าฟันช่วงบ่ายของวันเรียนที่เหลือ\nไปได้"

with shorttimeskip

play sound sfx_normalbell

show shizu invis_close at offscreenright
show misha invis_close at offscreenleft
with None

show misha hips_smile_close at twoleft
show shizu behind_blank_close at tworight
with Dissolvemove(0.5, time_warp=_ease_in_time_warp)

# "Before I can even stand up, Misha and Shizune have placed their hands on both my shoulders."
"มิช่ากับชิซูเนะเข้ามาจับไหล่ฉันก่อนที่ฉันจะทันได้ลุกด้วยซ้ำ"

# hi "Hey, I said I'd help out, damn…"
hi "เออ ก็บอกแล้วว่าจะไปช่วยน่า…"

play music music_shizune fadein 1.0

show misha hips_grin_close
with charachange

# mi "This is just insurance, Hisao, insurance~!"
mi "เพื่อความมั่นใจไงฮิซาโอะ เพื่อความมั่นใจ~!"

show hanako invis behind shizu at offscreenright
with None

show misha hips_smile_close at Transform(xpos=0.17)
show shizu behind_blank_close at Transform(xpos=0.5)
show bg school_scienceroom at bgleft
show hanako emb_timid:
    xanchor 0.5 xpos 0.9
with dissolvecharamove

# ha "H-Hisao?"
ha "ฮะ ฮิซาโอะ"

# "Hanako timidly tries to leave the room by circling around us and I suddenly realize that this may be my one chance to escape."
"ฮานาโกะเดินอ้อมพวกเราเพื่อออกจากห้องอย่างอาย ๆ ฉันพลันนึกขึ้นมาว่านี่อาจเป็นโอกาสเดียวที่ฉันจะหนีรอดไปได้"

# hi "Oh hey Hanako. What's up?"
hi "อ้าว ฮานาโกะ มีอะไรเหรอ"

show shizu basic_angry_close
with charachange

shi "…"

show misha hips_frown_close
with charachange

# mi "Hey, what makes you think you've got time to chat?"
mi "นี่ เราไม่มีเวลาว่างที่จะมาคุยเล่นหรอกนะ"

# hi "Oh relax, this won't take long… sorry Hanako, you were saying?"
hi "ใจเย็นน่า คุยไม่นานหรอก… โทษทีนะฮานาโกะ เมื่อกี้ว่าไงนะ"

show hanako emb_downtimid
with charachange

# ha "I… I was going to go to the library, and… and I thought…"
ha "ฉัน… ฉันว่าจะไปห้องสมุดน่ะ แล้ว… แล้วก็…"

# "Hanako's thumbs dance around each other and her eyes flit around the room, looking everywhere but at us."
"นิ้วหัวแม่มือของฮานาโกะขยับไปมา ตาเธอหลุกหลิกมองไปทั่วห้องยกเว้นที่พวกเรา"

show misha sign_smile_close
with charachange

# mi "Sorry Hanako, but Hisao has to come with us. He's got work to do."
mi "ขอโทษทีนะฮานาโกะ แต่ฮิซาโอะต้องไปกับพวกเรา พอดีเขามีงานที่ต้องทำน่ะ"

show shizu behind_smile_close
with charachange

shi "…"

show misha hips_grin_close
with charachange

# mi "Oh! But you can help too if you'd like."
mi "อ้อ! แต่ถ้าอยากช่วยจะมาด้วยก็ได้นะ"

show hanako cover_worry
with charachange

# ha "Um…"
ha "เอ่อ…"

label th_choiceH4:
menu:
    with menueffect

    # mi "So, how about it, Hisao?"
    mi "แล้ว นายจะเอายังไงล่ะฮิซาโอะ"

    # "What do you think, Hanako?":
    "เธอคิดว่าไงล่ะ ฮานาโกะ?":
        return m1

    # "I've done enough work for the council already.":
    "ฉันทำงานให้สภามากพอแล้วนะ":
        return m2


label th_H5_1:
#-----------------------

scene bg school_scienceroom at bgleft
show hanako cover_worry:
    xanchor 0.5 xpos 0.9
show shizu behind_smile_close at Transform(xanchor=0.5, xpos=0.5)
show misha hips_grin_close at Transform(xanchor=0.5, xpos=0.17)
with None

hi "What do you say, Hanako? If we all help it shouldn't take long at all."

show hanako emb_timid
with charachange

"Hanako's fidgeting answers my question before she can even form the words."

show hanako emb_downtimid
with charachange

ha "I… I really need to go…"

"Well, that was to be expected. Looks like it's just me and the council girls again."

"It's easier to resign myself to another afternoon's work in the small council office."

hi "I'll catch up with you later, okay?"

show hanako emb_smile
with charachange

ha "O-okay."

stop music fadeout 3.0

show misha hips_grin_close at twoleft
show shizu behind_smile_close at tworight
show hanako invis at offscreenright
show bg school_scienceroom at center
with dissolvecharamove

show misha hips_smile_close at twoleft
hide hanako
with charachange

mi "Right! Now that the farewells are over, it's work time!"

scene bg school_hallway3
with locationchange

"Misha and Shizune frog-march me to the student council office, never once letting go of my shoulders."

"I feel a little bad for ditching Hanako like this, but if this is the price of getting Misha off her back, so be it."

scene bg school_council
with locationchange

hi "So then, what are we up to today?"

show misha sign_smile at center
with charaenter

play music music_ease fadein 8.0

mi "Debrief!"

hi "Huh? Isn't that supposed to happen after something?"

show misha hips_grin
with charachange

mi "Yup! We have to collate all of the information from the festival so that Shicchan can debrief the teachers."

show misha hips_grin at twoleft
show bg school_council at bgleft
with charamove

show shizu adjust_happy at tworight
with charaenter

"Shizune drops a large pile of paperwork on the desk in front of me, and smiles succinctly."

show misha hips_smile
with charachange

mi "You need to sort those out into two piles."

show misha sign_smile
with charachange

mi "One for financial stuff, like receipts, one for feedback, one for positive feedback, maybe one for things that look like they could be problems next year, one for problems that probably won't be able to be fixed…"

hi "That's a few more than two piles…"

show misha perky_confused
with charachange

mi "Huh? Oh, right. Yeah I thought it would be only two piles. My bad."

hi "Right. While I'm doing this, what will you two be doing?"

show misha hips_grin
show shizu adjust_smug
with charachange

mi "Well, we missed lunch because we were collecting all of these reports, so we're going to go get some food!"

"Why didn't you just sort them out while you were collecting them…"

"Thankfully my self-defense mechanism kicks in and prevents me from opening my mouth and further worsening my situation."

show misha perky_confused
with charachange

mi "Eh?!"

show misha perky_sad
with charachange

mi "How is that fair?"

show shizu behind_blank
with charachange

shi "…"

"I was fretting over the unfair distribution of work so much that I didn't notice that Shizune had kept on signing."

"If it weren't for Misha's outburst, I probably wouldn't have noticed at all."

show shizu adjust_smug
with charachange

show shizu basic_normal
with charachange

show shizu behind_blank
with charachange

"Shizune seems to be delivering a fairly long string of commands to Misha, and none of them look pleasant."

show misha sign_sad
with charachange

show misha perky_sad
with charachange

show misha perky_sad at Transform(ypos=1.15)
with charamove

"Reaching a conclusion, Misha signs briefly back to Shizune, and then sits down at the desk next to me."

show shizu adjust_happy
with charachange

hide shizu
with charaexit

show misha perky_sad at Transform(xpos=0.5)
show bg school_council at center
with charamove

"Shizune waves to the both of us before disappearing out the door."

hi "What was all that about?"

show misha perky_confused
with charachange

mi "Shicchan was worried that you'd get it all wrong unless you were supervised."

show misha perky_sad
with charachange

mi "And since she can't tell you how you are messing things up, she's making me stay. Awww… bummer, I wanted to go with Shicchan!"

show misha cross_smile
with charachange

mi "But she is going to bring us back some food~!"

show misha cross_grin
with charachange

mi "How good is that!"

"Misha's flippancy is out of this world. From down in the dumps to on top of the world over some calories."

"It's hard to imagine how anyone could operate at that level."

hi "Well, it could have been worse."

hi "So what are we supposed to be doing?"

show misha sign_smile
with charachange

mi "Collation."

hi "I gathered that."

show misha hips_smile
with charachange

mi "Well, let's just start making piles. We'll work out what the piles mean later."

hi "Right…"

show misha perky_smile
with charachange

"We start to separate all of the papers into increasingly complex piles."

"At first it's just simple categories; financial, feedback, incident reports…"

"Then they split apart into the good and bad reports, and further still, until it starts to look like we've just thrown the papers onto the desk."

hi "This is hopeless."

show misha perky_confused
with charachange

mi "Huh? Why? We're doing what we were told, right?"

hi "Yes, but it looks like we're just making a mess."

show misha hips_grin
with charachange

mi "No, I think we got a lot done. Shicchan will be able to work out the rest from here."

show misha cross_grin
with charachange

mi "So I think we can stop about here then."

"It's almost as if Misha's common sense left the room with Shizune."

"Still, there's no point in arguing."

show misha sign_smile
with charachange

mi "Anyway…"

show misha cross_smile
with charachange

mi "What's the deal with you and Hanako?"

hi "Deal?"

show misha hips_smile
with charachange

mi "You were hanging out with her today, weren't you~?"

show misha hips_grin
with charachange

mi "Have there been any fireworks? Any gossip that you're withholding from me~?"

hi "If I told you about my own circumstances, it wouldn’t be gossip, would it?"

show misha perky_confused
with charachange

mi "I guess not…"

hi "We're just friends, I guess."

hi "Why are you so interested? I thought you and Shizune didn't like her…"

show misha cross_frown
with charachange

mi "It's not really like that. You know Shicchan and Lilly don't get along well."

mi "And since you can't really get Hanako away from Lilly, we don't talk to her much."

show misha sign_smile
with charachange

mi "But that doesn't mean that I can't be concerned for her."

hi "What is there to be concerned about?"

show misha perky_sad
with charachange

mi "Well, she never hangs out with anyone else, right? It's no good, Hicchan!"

"If Shizune and Lilly dislike each other because “their personalities are different” then I hate to think how Misha and Hanako would get along…"

show misha perky_confused
with charachange

mi "I mean, in one way or the other, we're all in the same boat here, right~?"

hi "Well, I guess."

show misha sign_smile
with charachange

mi "This one time, when she left class halfway through, Shicchan went to the teacher and asked what was going to be done about it."

show misha sign_confused
with charachange

mi "He said that every student here has special needs, and that Shicchan shouldn't worry herself about it."

show misha perky_confused
with charachange

mi "Hanako never does any group work; she just runs off."

mi "Isn't that enough to be concerned about?"

hi "I guess you're right. She still hardly says a word when we're talking."

show misha perky_sad
with charachange

mi "Well, that's more than I have been able to do. Shicchan and I both tried when she started, but she got scared and ran off."

"I consider telling Misha that exactly the same thing happened with me, but she seems caught up in thought."

"Listening to Misha without Shizune's influence is… interesting."

show misha cross_frown
with charachange

mi "I think she needs to realize that people here don't care what she looks like, and that she can trust us."

show misha cross_smile
with charachange

mi "If she could, I'd feel a lot better about her."

"I think this is the longest I have watched Misha without seeing her sign."

"When she's with Shizune, she is constantly waving her hands about, explaining the world to Shizune."

"That amount of effort probably places a strain even on an agile mind."

"And let's face it; Misha isn't the world's brightest spark."

hi "Well, I'll keep an eye on her for you."

hi "But you should probably apologize for earlier. I don't think Hanako is cut out for that kind of joke."

show misha perky_confused
with charachange

mi "Oh? Oh~!"

show misha perky_sad
with charachange

mi "I didn't even notice. Sorry."

hi "Don't say it to me, just mention it to her."

show misha perky_smile
with charachange

mi "All right. First thing tomorrow, I'll speak to her."

hi "Good."

play sound sfx_doorslam
with vpunch

"A cacophony from the door heralds the return of Shizune."

"I guess she can't really tell how much noise she is making."

show misha hips_grin
with charachange

mi "Oh, Shicchan! You're back!"

show shizu invis at Transform(xanchor=0.5, xpos=1.0)
with None

show misha hips_grin at Transform(xpos=0.3)
show shizu behind_blank at tworight
show bg school_council at bgleft
with dissolvecharamove

"Shizune appears, completely laden with goods from the convenience store."

show shizu basic_normal2
with charachange

shi "…"

show misha sign_smile
with charachange

mi "There was some surplus left from the festival. Since this is officially festival business, I've splurged a little."

show misha hips_grin
with charachange

mi "Nice idea Shicchan, ten points."

hi "Is that really allowed?"

show shizu cross_angry
with charachange

shi "…"

show misha cross_frown
with charachange

mi "For someone who refuses to join us, you seem to take an unhealthy interest in the politics of this council."

show misha cross_grin
show shizu adjust_smug at tworight
with charachange

mi "I shall punish your insolence by rationing your portion of the feast."

hi "Fine, fine, I get it."

show misha perky_smile
show shizu adjust_happy at Transform(ypos=1.15)
with dissolvecharamove

"Misha slides the multiple stacks of paper to one side to make room for the avalanche of food Shizune is spreading out."

"As I watch my hard yet misdirected work become wasted, I realize that it's little wonder why these two need help."

"The convenience store meal isn't overly tasty, but at the very least it's filling."

show shizu behind_smile
with charachange

shi "…"

show misha sign_smile
with charachange

mi "Thanks for helping today. Most of the time we just make up the reports for the staff."

show misha perky_smile
with charachange

mi "This year we can at least make up some relevant headings on the debrief."

hi "Are you sure this isn't a corrupt organization?"

show misha hips_grin
with charachange

mi "Not at all, not at all. We're by the book. It's not our fault if the book isn't specific enough."

hi "I thought that was the definition of corruption…"

show misha hips_smile
with charachange

mi "You think too much~!"

hi "You know what? You're probably right."

hi "Anyway, I must be off…"

hi "…that is, if I'm allowed to leave."

show shizu adjust_smug
with charachange

shi "…"

show misha hips_grin
with charachange

mi "Your work has been deemed sufficient. You may leave."

hi "Well, thank you."

hi "You know, if you stressed the “free meal” side of things over the “endless workload” side, you'd probably end up with more recruits."

stop music fadeout 6.0

show misha sign_smile
with charachange

show shizu behind_blank
with charachange

mi "You might just have a point."

hi "Well, think about it."

hi "And think about what we talked about… you don't have to tell that to Shizune if you don't want."

show misha perky_confused
with charachange

mi "What? Oh, right. I'll try to see her tomorrow."

show misha perky_smile
with charachange

mi "G'night, Hicchan."

hi "Night Misha, Shizune."

scene black
with dissolve

#-------------
label th_H5_2:

scene bg school_scienceroom at bgleft
show hanako cover_worry:
    xanchor 0.5 xpos 0.9
show shizu behind_smile_close at Transform(xanchor=0.5, xpos=0.5)
show misha hips_grin_close at Transform(xanchor=0.5, xpos=0.17)
with None

hi "Hey, Shizune. I know I said I'd help, but I forgot I'd already made plans. Besides, I helped out more than my fair share last week, didn't I?"

hi "I promise I'll make it up to you some other time."

show misha sign_confused_close
with charachange

show shizu basic_frown_close
with charachange

show misha perky_smile_close
with charachange

show shizu behind_blank_close
with charachange

"Shizune and Misha release their grip on me and have a long, deep, and silent conversation."

show misha sign_smile_close
with charachange

mi "Well, you have a point there. To be honest, we were only going to spend the rest of the budget on cakes."

show misha cross_laugh_close
with charachange

mi "So, if you're not there, it works out better. More cake for us. Wahahaha~!"

stop music fadeout 6.0

show shizu invis at offscreenleft
with dissolvecharamove

show misha invis at offscreenleft
with dissolvecharamove

hide shizu
hide misha
with None

"Shizune about-faces and marches out the door, and Misha skips out after her."

hi "Well, that was a lot easier than I thought it was going to be. Last week those two were like bloodhounds. Or prison guards."

hi "Or maybe prison guards bred from bloodhounds…"

"I can't believe I just thought that, let alone saying it out loud. I think I need to move away from Kenji."

hi "…Never mind. Anyway, should we go to the library?"

show hanako basic_smile
with charachange

ha "S-sure."

play ambient sfx_crowd_indoors fadein 0.5

scene bg school_hallway3
show crowd
with locationchange

"Hanako follows me through the still-crowded halls to the library, using me as a shield."

stop ambient fadeout 0.5
play music music_happiness fadein 2.0

scene bg school_library
show hanako invis at offscreenright
show yuuko neutral_down at center
with locationchange

show hanako basic_worry at tworight
with dissolvecharamove

"As soon as we are through the door, Hanako bolts for the counter, where Yuuko is stacking books."

show hanako emb_emb
with charachange

"Before I can catch up, Hanako has whispered something to her."

show yuuko neurotic_up
with charachange

yu "Um, you'd find that in non-fiction, but I don't know where, exactly. If you want I can look it up…"

show hanako emb_downsad
with charachange

ha "N-never mind."

hi "Hey Yuuko, what's all this about?"

show yuuko neutral_down
with charachange

yu "Oh, Hisao… Hanako was just looking for a book on…"

show hanako emb_blushing
with charachange

ha "N-nothing…"

hi "A book on nothing? In the non-fiction section?"

show hanako def_strain
with charachange

ha "I… I was just…"

show yuuko neurotic_up
with charachange

"I shoot a glance at Yuuko. She looks like she's about to burst from the pressure of keeping Hanako's request secret."

hi "Yuuko, what did…"

show yuuko happy_down
with charachange

yu "Chess! She's looking for a chess book!"

"I make a mental note to never entrust Yuuko with any important information."

show hanako defarms_shock
with charachange

ha "Y-Yuuko…"

show yuuko panic_up
with charachange

yu "I'm sorry Hanako… it just slipped out…"

hi "Well, it's not a secret any more. Come on, I'll give you a hand. I should really brush up on my skills, too."

show hanako def_worry
with charachange

ha "O… okay."

hide yuuko
with charaexit

show hanako def_worry at center
show bg school_library at bgleft
with charamove

"Yuuko disappears behind the counter in shame as Hanako and I wander into the depths of the non-fiction section."

"I know there is supposed to be a system for categorizing these books, but I don't see how anyone can decipher it without spending half of their life researching it."

"That's probably why all the librarians I know are neurotic."

#Dewey Decimal for Chess is 794.1, between magic tricks and educational games.

"Towards the end of the aisle, between a book on card tricks and some book on kid's games, stands a single book bearing the title “Chess Tactics for Champions”."

show hanako basic_bashful
with charachange

"Before I can reach for it, Hanako has the book in her hands, clutching it to her chest."

hi "Well, I guess that's yours then. Mind if I borrow it when you're finished?"

show hanako cover_worry
with charachange

ha "S-sure. I… I just haven't really played against anyone but L-Lilly before, so I thought…"

"Damn. It's not like I was trying to beat Hanako deliberately or anything, but she seems to have taken it to heart."

"Then again, at least this means she wants to play me again. That's a plus, right?"

hi "Ha, well it's not like I'm a master or anything; I just played a bit before…"

"It occurs to me that I haven't told Hanako about my condition. I falter for a second, deciding to cover my tracks. That is a conversation for another day."

hi "…before I came here."

stop music fadeout 6.0

show hanako cover_distant
with charachange

#To be replaced with "concern" if it gets made.

ha "Are… are you all right?"

hi "Yeah, I was just remembering something…"

"When I think about it, I shouldn't be afraid to tell Hanako about my condition and my time in the hospital. Judging by her scars, she probably spent a fair amount of time in a hospital bed."

"But, for some reason, I can't bring it up. At least not today, and not on short notice."

"Eager to break off the conversation, I grab a random book from the shelf."

#791.068 – Amusement parks

"It's some book on the world's fastest roller coasters…"

"…published in 1982. Well, not very up to date, but it should at least be interesting."

hi "Well, we both got books now, should we go sit down?"

show hanako cover_bashful
with charachange

"Hanako seems to accept my bluff, and we head to the reading nook in the back of the library."

hide hanako
with charaexit

"Neither of us says a word; we simply open our books and start reading."

"I try to read my book, but it would seem that in 1982 roller coasters weren't nearly as large as the ones built in the decades since."

"Most of the ones listed are made of wood. Something about that doesn't seem safe to me."

"If I'm going to ride on something potentially dangerous, I want it to be made out of steel, or some kind of space-age alloy that has big words like “Titanium” and “Ruthenium”."

"I quickly lose interest, and my eyes wander across the reading area to rest on Hanako."

show ev hana_library_read_std:
    truecenter zoom 1.0 subpixel True
    easein 20.0 zoom 1.05
with locationskip

"Hanako seems absorbed in her book, flicking back and forth through the pages, as if confirming what she just read."

"I wonder if that's actually effective, or if she's just overloading herself."

"She unconsciously brushes her hair from her face, temporarily revealing her scar tissue."

"I'm still not sure about the protocol here. Is it right to ask her about her scars? Or her past? How long was she in the hospital? Does she still visit the doctor?"

"These all seem like the questions that you'd ask someone who just transferred to your school, translated into the local language."

"But, to date, no one has directly asked me any of them. Well, except Rin, but I don't think I should use her as a guide to proper social behavior."

"For the time being, I'll just keep my mouth shut. If someone wants you to know something, then they'll tell you. Trying to force the issue might drive Hanako back into herself."

scene bg school_library_ss
show yuuko worried_up_ss at center
with shorttimeskip

yu "Um… sorry to interrupt, but I have to close the library now."

play music music_tranquil fadein 3.0

hi "Already?"

"I check my watch. Somehow, as I was lost in thought, nearly two hours have passed."

show yuuko smile_down_ss
with charachange

yu "Do you want to check out those books? I can do it on the way out…"

show hanako invis:
    xpos 0.9 xanchor 0.5 ypos 1.17 yanchor 1.0
with None

show hanako basic_worry_ss:
    xpos 0.7
show bg school_library_ss at bgleft
show yuuko smile_down_ss at twoleft
with dissolvecharamove

ha "P-please."

hi "I'm done. I'll drop this one back on the way through. It wasn't as interesting as I first thought."

show hanako emb_timid_ss at tworight
with dissolvecharamove

"Hanako marks her place with a slip of paper and stands up. The girls head to the counter and I return my book to what I think is the right shelf."

show yuuko neurotic_up_ss
with charachange

"Yuuko scans Hanako's book with practiced precision, yet still manages to fumble it."

show yuuko neutral_down_ss
with charachange

yu "Oh… there we go. Third time lucky. Since this is a non-fiction book, you can only have it for a week."

show hanako basic_smile_ss
with charachange

ha "T-that's okay."

scene bg school_hallway2
with locationchange

"Yuuko shuts down the library's computer and herds us out the door."

show yuuko panic_up at twoleft
show hanako def_worry at tworight
with charaenter

yu "Argh! I didn't think it was this late already…!"

hi "But you're the one that told us you had to close…"

show yuuko worried_up
with charachange

yu "Yes but, I know but, that was before I looked at the time!"

show yuuko neurotic_up
with charachange

yu "I'll see you later."

hide yuuko
with easeoutleft

"Yuuko bolts down the hall, her handbag trailing behind her like an awkward streamer."

show hanako def_worry at center
show bg school_hallway2 at bgleft
with dissolvecharamove

hi "I guess all librarians really are neurotic."

show hanako emb_timid
with charachange

ha "Huh?"

hi "Ah, never mind. I was just thinking that I've never met a librarian that can organize their time, no matter how good they are with their books."

show hanako basic_smile
with charachange

ha "Oh… I k-know what you mean…"

"Hanako smiles in amusement. It wasn't meant to be a joke, but I must have reminded her of some other librarian… or something…"

show hanako cover_worry
with charachange

ha "I… I have to get back."

hi "Yeah, me too. I didn't realize it was this late. Thanks for letting me hang out with you."

show hanako basic_bashful
with charachange

ha "N-no problem."

hi "I'm going to my dormitory room now anyway, so do you mind if I tag along?"

show hanako emb_blushing
with charachange

ha "O-okay."

hide hanako
with charaexit

"Hanako sets off ahead of me, and I need to jog a little to reach her side."

scene bg school_dormext_full_ss
with locationchange

show hanako def_worry_ss at center
with charaenter

"We walk through the gardens, eventually arriving in front of the dorm buildings."

hi "Man, you walk pretty fast. I used to play in a soccer club, and you manage to outpace me."

stop music fadeout 6.0

show hanako emb_downsmile_ss at center
with charaenter

"I kinda regret saying that. It has less to do with her pace than with the fact that my condition has significantly worsened my fitness."

"Hanako's reaction is odd. I expected an awkward attempt to downplay her walking speed, but she just blushes while looking at her feet and smiling."

"Silence hangs in the air between us. That happens often around Hanako, but feels slightly different than usual this time. After a few seconds, I try to break the silence."

hi "Here you go. See you in class tomorrow?"

show hanako emb_smile_ss
with charachange

ha "S-sure."

hide hanako
with charaexit

"Hanako waves a short goodbye before pushing her way through the dorm's doors. I stand and look at them for a while, before making my way to my own dormitory room."

scene black
with dissolve

#-------------------------------

label th_H6:

scene bg school_dormhisao
with locationchange

"Chirping birds."

"Normally, this would be a good time to reflect upon the beauty of nature."

"But it is 6 AM."

play sound sfx_pillow

scene black
with Dissolve(0.2)

"Covering my head with the pillow, I slam my face into the mattress, hoping that the impact will send me instantly back to sleep."

"Futile."

"I toss and turn, but sleep simply won't return to me."

play music music_daily fadein 10.0

scene bg school_dormhisao
with locationchange

"All right nature, you've won. See? I'm getting up now…"

"The lack of sleep weighs my mind down, and there's only one remedy for this; a nice, hearty breakfast."

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 0.5

scene bg school_cafeteria
with locationchange

"It would be nice to be the first person here."

"To be the first to dig into a piping hot pile of food, to sit wherever I desire…"

"It would have been nice."

"But even my exceptionally early start has put me behind the most diligent students."

"I guess there are quite a few people that have early starts here, for one reason or another."

"A group of students in sports clothes huddle around one table, eagerly discussing game plans inbetween inhaling great gulps of food."

"Scattered around the hall are a number of bleary-eyed students, probably suffering from the same ailment as myself - noisy birds."

"And, of course, there are the people that actually enjoy getting up this early, the ones with their bags stuffed with textbooks and completed homework."

"It's hard not to despise people like that, even more so when you're tired yourself."

"Picking out a familiar face from the thin crowd, I head towards the nearest table."

"Lilly sits alone, delicately feeling her way around a small plate of eggs with her fork."

"It's almost a shame to interrupt her and her clockwork movements."

"I wonder, is this how a blind person zones out? Simply moving in pre-determined patterns learned over the years, just like how a sighted person would eat while reading a newspaper."

hi "Good morning, Lilly. I didn't expect you to be here this early."

show lilly basic_surprised:
    center
    ypos 1.2
with charaenter

li "Oh, Hisao, you startled me. I didn't know you took breakfast this early."

hi "I don't. This is an exception to the rule. I'd greatly prefer to be late to school than early to breakfast."

show lilly basic_weaksmile
with charachange

"Lilly gives a small sigh at my admitted tardiness as I begin eating my food."

"It doesn't take long for her to lapse back into her previous mindless nibbling."

"Each short motion lacks energy. I suppose this is similar to letting your eyes wander while performing any ordinary chore."

"But after a few repetitions of the find food/eat food cycle, Lilly puts down her fork and dabs her lips with a napkin."

stop music fadeout 6.0
stop ambient fadeout 6.0

show lilly basic_concerned
with charachange

li "Hisao, do you mind if I ask you a question?"

"Damn. All I want is a little food and about four hours of sleep. And nobody says “can I ask you a question” for a simple question."

hi "Sure."

show lilly basic_listen
with charachange

li "Do you think of Hanako as a friend?"

"Huh, this seems like a leading question."

hi "I… guess so. Why do you ask?"

show lilly basic_weaksmile
with charachange

li "No real reason."

show lilly basic_displeased
with charachange

play music music_serene fadein 8.0

li "I do have another question though. Why is it that you think of her as a friend?"

"This is well above my level. What is she expecting from me?"

hi "I'm not really sure. I guess it's because she's a little different in the way she deals with people…"

show lilly basic_reminisce
with charachange

li "Hmm. Since I've known her, she hasn't really connected with anyone."

show lilly basic_concerned
with charachange

li "She doesn't seem interested in other people, and I think people are a little scared off by her appearance."

hi "Really? I thought that kind of thing was, well, discouraged here. Discriminating and such."

show lilly basic_listen
with charachange

li "Hmm, if I were to put it one way…"

"She furrows her brow in thought, a move which makes me slightly anxious as to what she's plucking from her mind."

show lilly basic_weaksmile
with charachange

li "I'd say that you're a little naive."

"Naive? I'd be insulted if not for the slightly cynical grin on her face."

hi "I… see."

show lilly basic_reminisce
with charachange

li "While Yamaku has a stronger sense of community compared to other schools, it's far from being free of conflict."

show lilly basic_displeased
with charachange

li "Rules cannot remove human nature, after all, only suppress it."

"That's something I've noticed, actually."

"Just little things, like how certain people and cliques avoid each other in the hallways. It's no different than my old school, really."

"Even Lilly and Shizune could be considered bitter rivals, even though they both seem like fairly accepting people."

"Well, at least the Misha-tinted Shizune does; who knows what actually goes on with her fingers and behind her glasses."

hi "I guess you're right. But when I first came here, everything was a bit of a shock."

hi "I kept on making mistakes, or at least thinking I was making mistakes. Like when we first met, and I said “I see” to you."

hi "I didn't know if that was considered rude or anything, so I tried to just put it in the back of my mind. Treating people any differently and that kinda thing."

hi "So I didn't. I told myself that Hanako and you and everyone else was just normal, and I tried to ignore the obvious."

hi "I talked to Hanako as if she were any other person, and so we became friends."

hi "At least, that's how I think it happened."

hi "But you know, I feel guilty just from saying something like that aloud. As if it took extra effort to think of Hanako, or you, or anyone here as normal people. I don't think that's right."

show lilly basic_smileclosed
with charachange

li "Hisao, I think you are naive, but I also think that you are a good person. It is perhaps one of your better traits."

hi "I… suppose… I can take that as a compliment…"

show lilly basic_smile
with charachange

li "Tell me, are you free tonight?"

hi "If you don't count homework, then I'm as free as the breeze."

show lilly basic_cheerful
with charachange

li "In that case, would you care to join myself and Hanako for tea?"

hi "Er, I don't really have that much money at the moment, so going out isn't really…"

show lilly basic_smile
with charachange

li "Oh, I didn't mean going out. Just here, this evening."

hi "You can access the classrooms in the evening here?"

show lilly basic_giggle
with charachange

li "No, that's not what I meant. Hanako and I often use my room for tea parties together. Please feel free to drop by after dusk."

hi "Sure, I see no problem with that. What's your room number?"

show lilly basic_smileclosed
with charachange

li "225; Room 25 on the second floor."

hi "Okay, sure."

show lilly basic_weaksmile
with charachange

li "Well then, I had best be off. I have class representative duties to attend to, after all."

show lilly basic_cheerful at center
with dissolvecharamove

li "Until this evening, Hisao."

hi "Yeah, catch you later."

hide lilly
with charaexit

stop music fadeout 8.0

"Hang on… was I just invited to a girl's room after hours? Is that even allowed?"

"There is the curfew here, but I've never heard any rules about visitors in the dorm rooms."

"Even still, this is enough to get my sleep-deprived brain jump-started."

"Add that to a lukewarm breakfast and you have one hell of a pick-me-up."

scene bg school_scienceroom
with locationskip

"I grudgingly go to class, still a little excited at the prospect of breaking the rules."

"I feel a little like a kid planning to sneak out of his window at night."

"Well, maybe that's going a little too far, but when you compare an invitation to a party to six or so hours of lectures, I know which one wins."

"Misha and Shizune do little to relieve my boredom either. For once, they seem determined to actually complete Mutou's assignments."

scene bg school_scienceroom_ss
with shorttimeskip

play sound sfx_normalbell

"Nevertheless, the day eventually winds to a close."

scene bg school_dormhisao_ss
with locationskip

"I hurry back to my room to wash up and comb my hair. Thankfully I don't run into Kenji."

scene bg school_dormext_full_ss
with locationchange

"Before long I am leaving the boys' dorm."

#---------------------------------

label th_H7:

scene bg school_girlsdormhall
with locationskip

play sound sfx_doorknock2

"I nervously rap on the door marked 225, checking my watch once again."

li "Is that you, Hisao? The door is open, you can come in."

"Lilly's voice lilts through the door and soothes my nerves."

"This is the first time I've been invited to a girl's room after dark."

"Even though I know there is no ulterior motive behind this invitation, it doesn't stop my mind running wild with possibilities."

"One guy. Two girls. In a dorm room. With a tea set."

"When I put it like that, it sounds a little dodgy."

"Giving a small sigh to steady myself, I gingerly put my hand on the handle and open the door, craning my head to see inside."

play sound sfx_dooropen

window hide

scene white
with dissolve

with Pause(0.1)

play music music_one fadein 10.0

scene ev lilly_bedroom:
    truecenter
    zoom 1.1 subpixel True
    ease 15.0 zoom 1.0
with Dissolve(4.0)

window show

"The door opens completely and I catch my first glimpse of Lilly's room."

"Her furniture looks almost antique, but the bare walls and flat surfaces are barely decorated at all. In the center of the room sits a low table, where I see a small tea set at rest."

"It seems that everything in this room has its place, possibly excepting the several piles of books stacked up against the wall."

"My sense of vision isn't the only one to be stimulated; the faint smell of something can be picked up on the air. Nail polish, perfume, makeup… it's hard to describe in any way other than “girly”."

"My eyes finish their quick sweep of the room, before returning their position onto the girls."

scene ev lilly_bedroom_large:
    xpos -130 ypos -400 subpixel True
    acdc_warp 4.0 ypos -600
with flash

"Lilly sits next to the small table, wearing very dark blue pajamas. Dark blue pajamas with shorts that show off plenty of her alluring pale legs."

show ev lilly_bedroom_large:
    ease 1.0 ypos -300 xpos -830
    acdc_warp 12.0 ypos 0 xpos -830
with None

"Opposite her, Hanako sits adorned in a conservative light pink gown."

"Her hands are firmly fixed between her legs, her shoulders forward, and her head down, as if trying to hide herself in it."

"It would be easy for her to do; it looks about two sizes too big for her."

"Waves of flannel flow from her frame, making her look like a child playing dress-up in her parents' clothes."

"She looks up to confirm my identity, and the beginnings of a thin smile creep across her face, before vanishing so fast that I can't be sure they ever were there."

show ev lilly_bedroom_large:
    ease 1.0 xpos -130 ypos -400
with None

li "There's no point in you standing in the doorway, Hisao."

scene bg school_dormlilly
show lilly basic_smile_paj:
    twoleft
    ypos 1.2
show hanagown distant:
    tworight
    ypos 1.17
with locationchange

play sound sfx_doorclose
stop music fadeout 10.0

"I take a step into the room, closing the door behind me."

show lilly basic_weaksmile_paj
with charachange

li "My my, I'm afraid this really is a small room for the three of us. Would you like to take a seat?"

"I slowly walk to the table and sit down, trying my hardest not to disturb anything along the way."

"I also can't help but steal a quick glance into Lilly's top as I sit."

"To be robbed of sight would be a most terrible fate."

show lilly basic_smileclosed_paj
with charachange

li "Well now, how about some tea. Hanako, could you please pour?"

show hanagown normal_blush
with charachange

ha "S… sure. Hi… sao… would…"

show hanagown distant_blush
with charachange

ha "…would you…"

show hanagown worry_blush
with charachange

ha "…would you like…"

hi "I would love some tea. Do you need a hand?"

show hanagown normal_blush
with charachange

ha "N… no, I'm fine…"

show hanagown smile
with charachange

ha "Thank you…"

play music music_dreamy fadein 2.0

show lilly basic_giggle_paj
with charachange

"Lilly finds it difficult to resist a smile at her companion's nervousness, something I can't really blame her for."

show hanagown distant
with charachange

hi "Been a tiring day?"

show hanagown smile
with charachange

ha "Y… yeah."

show lilly basic_smileclosed_paj
with charachange

"I relax at my place, opposite of the cabinet."

"To my left is the blue-clad Lilly and to my right sits the pink Hanako."

show teaset:
     xalign 0.5 yanchor 0.5 ypos 0.6 alpha 1.0
     easein 0.5 ypos 0.5
with charaenter

"The tea set on the table looks cute as well as practical; painted red with a floral motif."

"It looks odd when contrasted with Lilly's plain but generally sophisticated-looking furniture, which leads me to think that Hanako might have picked it out."

"There is a slight “ting” when Hanako accidentally clips the teapot on a cup as she is pouring."

show hanagown worry
show lilly basic_displeased_paj
with None

show teaset:
    easeout 0.5 alpha 0.0 ypos 0.6
with Pause(0.5)

hide teaset
with None

"She breathes in sharply; she must be really nervous, as it's not the kind of thing anyone would worry about."

show hanagown worry_blush
with charachange

"Hanako quivers at her mistake."

show lilly basic_weaksmile_paj
with charachange

li "It's okay, Hanako. There's no need to be nervous."

show hanagown normal
with charachange

"Hanako seems to find some confidence in Lilly's reassuringly soft-spoken words and deftly pours the next two cups."

show hanagown normal_blush
with charachange

ha "Here you are, Hisao… Lilly."

"Hanako carefully places a cup and saucer in front of Lilly and myself. I could get used to service like this."

show lilly basic_smile_paj
with charachange

li "Thank you, Hanako."

hi "Yeah, thanks."

show hanagown smile
with charachange

ha "Y-you're welcome."

show lilly basic_smileclosed_paj
with charachange

"Lilly searches for her cup, and upon finding it, sips delicately."

"I do the same. This tea tastes somewhat better than the tea we usually have at school."

hi "This is nice, it's so different from any tea I had before…"

show lilly basic_ara_paj
show hanagown normal_blush
with charachange

li "Looks like you picked the right one, Hanako."

show lilly basic_smileclosed_paj
with charachange

li "You've done well, even if it was a bold move."

show hanagown smile
with charachange

"Hanako's smile returns, redoubled."

"Even with her blighted face, her shy smile couldn't be called anything but “cute”."

show hanagown distant_blush
with charachange

ha "I'm glad you like it…"

"Hanako, finally beginning to relax, sips from her cup."

#--------------------
label th_H7a:

$ renpy.music.set_volume(0.5, 1.0, channel="music")
window hide
nvl clear
nvl show dissolve

n "I think back to my chat with Misha the other day."

n "Is Hanako's behavior something to be concerned about, or is she just shy?"

n "And then there was Lilly earlier this morning."

n "The concern from both of them seemed to be genuine, and they know the situation better than I."

n "But, really, how could I possibly help?"

n "I'm no plastic surgeon, so I can't really help her appearance. Nor am I a psychologist who can make her more sociable."

n "So what the hell do Lilly and Misha want me to do?"

n "It's frustrating. Hanako and I are quickly becoming friends on our own accord, and because of that, it's like everyone wants me to solve all her problems."

n "And I have no idea how to do that."

n "No one can cure my heart, nor Lilly's eyes, nor anyone who is here, in this school."

n "However, I see no harm in becoming better friends with Hanako. Now that she's warming up to me I kind of enjoy hanging out with her."

$ renpy.music.set_volume(1.0, 1.0, channel="music")
nvl clear
nvl hide dissolve
window show

#------------------------

label th_H7b:


$ renpy.music.set_volume(0.5, 1.0, channel="music")
window hide
nvl clear
nvl show dissolve

n "\n\n\n\nSomething about this makes me think about Lilly's question at breakfast."

n "Why am I friends with Hanako?"

n "Lilly seems genuinely concerned for Hanako's well being, but it's not like I can do anything to help her."

n "As far as I can tell, her scars don't hold her back physically, and everyone I've met seems to have overcome their disabilities to some extent."

n "I don't have any ulterior motives to hang out with Hanako, we just share similar interests."

n "\nIsn't that enough?"

$ renpy.music.set_volume(1.0, 1.0, channel="music")
nvl clear
nvl hide dissolve
window show


#-----------------

label th_H7c:

show lilly basic_smile_paj
with charachange

li "So, Hisao, are you enjoying yourself?"

"Lilly's words break me out of my reverie, and I take a second to reconsider where I am."

"I'm in a room with two girls in their bedclothes. This is something to be enjoyed."

hi "Yeah, it's relaxing. Almost like I'm not in the school any more. Do you do this often?"

show lilly basic_weaksmile_paj
with charachange

li "Quite often, but not as often as we take tea in the school building."

"Considering they do that nearly every day, that's not a big surprise."

"As I move to take another sip from my teacup, I find it sadly empty."

hi "That was delicious. Thank you Hanako, Lilly."

show hanagown smile
with charachange

ha "You're welcome."

show lilly basic_smile_paj
with charachange

li "Yes, you're most welcome Hisao. It's nice to have a third person here."

hi "Well, any time you need someone to fill that position, I'm always available. Always."

"One must be sure to get one's point across in these circumstances."

stop music fadeout 8.0
show lilly basic_sleepy_paj
with charachange

"Lilly lets loose a yawn, which she unsuccessfully hides with her hand."

show lilly basic_weaksmile_paj
with charachange

li "Pardon me, I think I'm a little tired."

show hanagown distant
with charachange

ha "I think we're all a little tired…"

show lilly basic_ara_paj
with charachange

li "My my, how astute we are tonight, Hanako."

show lilly basic_weaksmile_paj
with charachange

li "We really should head to bed; we all have class tomorrow."

hi "Yeah… I should go."

show lilly basic_smile_paj
with charachange

li "Thank you for your presence, Hisao."

show hanagown normal
with charachange

ha "Th… thanks. You'll come again?"

hi "Not even a whole army could stop me."

show lilly basic_cheerful_paj
with charachange

li "I'm impressed by your determination, Hisao."

hi "Either way, you're right. We'd best get going."

"I stand up, and make for the door."

show hanagown normal at tworight
with dissolvecharamove

"Hanako gingerly stands up behind me."

"I stop and face her."

hi "Are you coming with me?"

play music music_comedy fadein 0.5

show hanagown normal_blush
with charachange

"Hanako instantly blossoms into full blush."

show hanagown distant_blush
with charachange

ha "No… I… not… this room… isn't…"

hi "It's okay, I was only joking."

show hanagown smile
with charachange

ha "Oh… okay… good night…"

show lilly basic_smileclosed_paj
with charachange

li "Good night, Hanako. Good night, Hisao."

hi "Night all."

"And with that, our tea party finishes."

scene bg school_girlsdormhall
with locationchange

"I'm still not sure what it is that Lilly wants me to do for Hanako, but I don't want to let her down."

"I wait until the door has closed behind us before turning to Hanako."

show hanagown distant_blush
with charaenter

hi "Hey, Hanako, you know, you don't have to be nervous around me or anything."

hi "I mean, we're friends, right?"

show hanagown normal_blush
with charachange

ha "R-right. We're… friends."

hi "If you ever want to hang out or anything, just let me know. We still need to have that chess rematch, remember?"

show hanagown distant
with charachange

ha "S-sure…"

show hanagown normal
with charaenter

ha "B-but I don't think you'll win…"

hi "It wouldn't be any fun if it was easy."

show hanagown smile
with charachange

"Hanako seems to give a muted laugh, but she could have just as easily been exhaling."

ha "G-good night Hisao…"

show hanagown invis at tworight
with Dissolvemove(0.5, time_warp=_ease_out_time_warp)

hide hanako
with None

stop music fadeout 5.0

"With that, Hanako quickly retreats into her room, located next to Lilly's."

"I start to walk back to my dorm, but the simple act of walking seems to drain me of my energy."

scene bg school_dormhisao
with locationskip

"I barely make it to my room before I am hit by a wave of exhaustion."

play sound sfx_switch

scene bg school_dormhisao_ni
with Dissolve(0.2)

"I kick off my shoes, fall into bed and fall asleep by the time my head hits the pillow."

scene black
with dissolve

#-----------------
label th_H8:

scene bg school_dormhallway
with locationchange

"I pull my door closed, ready for another day of classes."

show kenji invis at twoleft
with None

show kenji neutral_close at center
with Dissolvemove(0.5, time_warp=_ease_in_time_warp)

ke "Sleep well?"

play music music_kenji fadein 0.5

"Kenji's sudden arrival makes me jump, and I narrowly avoid butting heads with him."

"I know he has poor eyesight, but he knows who I am now. Does he still have to stand this close?"

show kenji neutral
with charadistant

hi "Oh. Yeah. Like a baby."

show kenji tsun
with charachange

ke "Damn, why do people say that? Have you ever heard a baby sleep?"

ke "They scream. All night. Every night. Babies don't sleep well, ever."

"Well, there goes my restful state. I have to remember to never use figures of speech with Kenji."

hi "All right, I get your point. It was a figure of speech."

show kenji neutral
with charachange

ke "Yeah, sure, whatever. Where were you last night? I had a favor to ask but you weren't around."

"For a split second I consider telling Kenji the truth; that I was spending time with Hanako and Lilly."

"Thankfully, that split second passes as soon as it came."

hi "I was just out. Checking out the local area and stuff. You know, recon."

show kenji happy
with charachange

ke "Good man, good. I knew you were the type to plan ahead…"

hi "Anyway, what was this favor you wanted?"

show kenji neutral
with charachange

ke "I was going to get some take-out, but I needed change."

hi "Wait, what? I gave you money last week and you still haven't paid me back!"

show kenji tsun
with charachange

ke "Tch, and I was starting to think you were cool."

"Kenji fishes around in his pocket and produces his wallet."

"As he counts out the 400 yen he owes me, I can clearly see at least two 10,000 yen notes."

hi "Hey, what the hell? Why are you borrowing money off me when you've got that much cash?"

"Kenji hisses a little, realizing that he's been had."

ke "Get off my case, man. It's bad luck to break a big note for anything less than half its value. It's the tycoon's rule."

ke "Last night's dinner is going to cost me seven years of bad luck. Seven years!"

show kenji happy
with charachange

ke "Don't you think that's enough cause to help someone out? I'd get a shorter sentence if I just stole the stuff."

"My common sense screams at me to say something to him, but thankfully I restrain myself."

"Arguing a point like this with Kenji will just lead to further and more complicated discussions."

hi "Yeah, I guess you're right. Maybe you should plan these things a little better?"

show kenji neutral
with charachange

ke "Yeah man, I know. But I've just got so much stuff to do, it's hard. And you're never around any more so I'm on my own."

ke "We're supposed to be brothers in brotherhood, remember?"

hi "Yeah yeah, I get you. Global conspiracy and such. I'll keep my ear to the ground."

show kenji neutral_close
with charachange

"Kenji draws close enough for me to get a clear whiff of his garlic-tainted breath."

show kenji tsun_close
with charachange

ke "You'd better, man. You're already spending less time here. That's the first thing they do."

ke "They'll try to split us up. Divide and conquer. Sun Tzu said that."

hi "Roger that. Now, I've got to be going. I've got classes. You coming?"

show kenji neutral_close
with charachange

ke "Nah, I'm tired. I stayed up all night just to make sure nothing was going to happen after splitting that note."

hi "As rational as ever, I see."

show kenji tsun_close
with charachange

ke "Whatever. Night."

stop music fadeout 3.0

show kenji invis at twoleft
with Dissolvemove(0.5, time_warp=_ease_out_time_warp)

"Kenji scurries back into his room, and I hear him throwing his locks as I walk down the hallway."

#--------------

label th_H9:

scene bg school_dormhallway
with None

scene bg school_scienceroom
show muto smile at center
with shorttimeskip

play music music_daily fadein 4.0

mu "…that is why some people can't roll their tongue, or why their second toe is longer than their big toe."

"Mutou beams a half-moon smile at us, obviously proud of his explanation of recessive genes."

"However, no matter how impressed he is at the science that defines who we are, the classroom seems to be reduced to a stupor."

"Why is it that a bad explanation can make even the most interesting thing seem worthless?"

show muto irritated
with charachange

"I can see Mutou deflate as he realizes that nothing he's said in the past half hour has sunk in."

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 4.0

"Whispered conversations start to break the silence, and like an avalanche, the noise level in the class starts to rise."

show muto normal
with charachange

"Defeated, Mutou identifies some questions from the text book and sets to clearing off the blackboard."

hide muto
with charaexit

"Almost as if expected, Hanako packs up her things and leaves as soon as people start talking and laughing among themselves."

"The initial shock of seeing someone play so blatantly truant has started to fade, but it doesn't stop me from wondering."

"Is she leaving because she doesn't want people to speak to her? Or is it just the thought of people around her shattering her peace?"

play sound sfx_normalbell
$ renpy.music.set_volume(1.0, 4.0, channel="ambient")

"Before I can think about the topic any further, the lunch bells ring. I wonder if she was simply taking the opportunity to leave early."

"The usual clamor of students exchanging books for lunch reverberates around the room, and while Misha is distracted, I grab my lunch and head out the door."

stop ambient fadeout 1.0

scene bg school_miyagi
show lilly basic_smileclosed:
    center
    ypos 1.2
with locationskip

"Lilly already sits in the tea room, setting out her lunch alone."

hi "So, Hanako's not here then?"

show lilly basic_smile
with charachange

li "Oh, Hisao, how are you? I haven't met Hanako since this morning, I'm afraid."

"That's right, Hanako and Lilly live next to each other."

"Somehow I think their morning conversations are slightly more grounded than Kenji's ramblings."

hi "That's strange. She left class early, so I figured that she'd come here."

show lilly basic_displeased
with charachange

li "So she's still leaving class early…"

hi "Huh? Yeah, I've seen her do it a few times."

show lilly basic_sad
with charachange

stop music fadeout 7.0

"Lilly drops her head a little, and her tone of voice is notably depressed. It's very reminiscent of someone who is used to hearing bad news."

li "I was so sure that she'd stop doing that once you two became friends."

show lilly basic_weaksmile
with charachange

li "Everyone has their own pace, I suppose."

hi "Well, I was wondering about just that today. Why exactly does she leave?"

show lilly basic_reminisce
with charachange

li "I'm not entirely sure myself. I personally think it's because she doesn't want to be put in a situation where she has to answer someone."

"I have a flashback of my first meeting with her, when I thought she looked like a cornered animal. Maybe I wasn't far from the truth."

hi "But she seems fine with talking to you, and with me… a bit…"

show lilly basic_displeased
with charachange

li "It's a little more complex than that. I imagine that the first thing most people ask her about is her scars, and what happened."

li "She rarely talks about it with me, but I can tell that she doesn't like to remember whatever happened back then."

show lilly basic_reminisce
with charachange

li "Leaving class and running away from discussions is her preemptive strike, if you will."

hi "Huh… so then how does that explain her talking to me?"

show lilly basic_weaksmile
with charachange

li "You said it yourself yesterday at breakfast; you tried to ignore her scars. Once she saw that you weren't going to ask her about that, she opened herself up to you."

hi "Hrm, I guess you're right. Maybe. I dunno. You know her better than I, so I'll take your word for it."

play music music_normal fadein 3.0

show lilly basic_giggle
with charachange

li "I wouldn't worry about that. I'm sure you'll come to know her as well as I do soon enough."

show lilly basic_smileclosed
with charachange

li "I welcome the prospect of her having a new friend, and the two of you have such similar interests…"

hi "Well, I hardly count reading as a team sport. It is good to have company, though."

show lilly basic_smile
with charachange

li "That's my point. Hanako is still an average person at heart. She also wants company at times like that."

hi "Huh, I see. I think. To be honest, both of you still confuse me a little."

show lilly basic_smileclosed
with charachange

li "That's only natural, Hisao. We've only known each other for a little while; it's unreasonable to expect you to understand us, just as we can't understand you."

show lilly basic_weaksmile
with charachange

li "But that is half the fun of becoming friends, right?"

hi "Yes, yes it is."

show lilly basic_giggle
with charachange

li "Although… I suppose there is the matter of us being opposite genders. Men and women do seem to confuse each other quite often."

"She says this with a light giggle, finding amusement at the odd little details of life."

show lilly basic_cheerful
with charachange

li "I hope you don't mind, but I'm going to start eating."

hi "No, go ahead, I think I'll eat something too. I've got some books I want to drop back at the library before classes start, so I'd better get a move on."

show lilly basic_smileclosed
with charachange

li "You'll probably find Hanako there as well. If you do see her, can you tell her to stop by my room later tonight? I'd like to talk to her."

hi "You're not coming?"

show lilly basic_weaksmile
with charachange

li "Unfortunately I have a class representatives' meeting later, so I'll be gone as soon as I've finished my lunch."

hi "Okay then, if I don't see her in the library then I'll tell her in class. I'm sure she'll be back after lunch."

"We fall silent as we start to eat, and I take a second to reflect on our conversation."

"I've always thought that Hanako's shyness was simply due to her being self-conscious of her scars."

"But that is a pretty superficial way of looking at her."

"Just when I thought I was able to see through the fog of Lilly and Hanako, I realize that I'm more lost than when I started."

"Lilly quickly finishes her lunch, acutely aware of her meeting. I don't blame her."

"Shizune is most likely going to be there, and I doubt she wants to give her the satisfaction of another argument."

show lilly basic_smile
with charachange

li "I must be off. Same time tomorrow?"

hi "Same time, same channel. I'd better head off too; I don't want to risk being late."

show lilly cane_smileclosed
with charachange

show lilly cane_smileclosed at center
with charamove

stop music fadeout 4.0

"Lilly smiles gently, picks up her cane and walks out into the hall."

#----------

label th_H10:

scene bg school_hallway2
with locationchange

"I turn my back on Lilly as we head in opposite directions. For some reason I find myself hoping she doesn't get into another fight with Shizune."

"As much as I like Lilly, Shizune and Misha have been pretty instrumental in helping me adjust, even if half of our conversations are thinly-veiled recruitment attempts."

"Then again, I barely know either of them. Maybe they were previously leaders of some kind of secret society, but their love for each other drove them apart…"

"Man, I need to stop reading cheap fiction. It's rotting my brain. Either that or I've got to move away from Kenji and his bad influence."

"It's sad that I can't tell the two apart any more."

scene bg school_library at right
with locationskip

play music music_happiness fadein 2.0

"I slide my books down the return chute and they crash into the cart with a pleasant thud."

play sound sfx_impact2

show yuuko panic_up
with vpunch

"Yuuko, however, doesn't seem as impressed as I."

yu "H-Hisao! You scared me!"

hi "Sorry, I thought you would be used to that by now. Or is the literacy level here so low that nobody borrows any books?"

show yuuko worried_up
with charachange

yu "Huh? No I think everyone here can read fine…"

hi "Yeah… never mind."

"There are some battles that you can never win. Trying to explain jokes is one of them. My Dad taught me that the hard way."

hi "Say, Yuuko, have you seen Hanako about? She left class early but she wasn't in her usual hiding place."

show yuuko closedhappy_down
with charachange

yu "I think I saw her sneak in before lunch…"

show yuuko panic_up
with charachange

yu "Oh! But I'm not supposed to tell anyone that!"

hi "I just told you that I saw her leave, no need to stress out…"

show yuuko smile_down
with charachange

yu "Oh… of course. She's probably in the back."

hi "Thanks. Get any new books in recently?"

show yuuko worried_up
with charachange

yu "No, sorry. I'll let you know when we do, though."

hi "Okay."

"If there's one thing I know about librarians, part-time or otherwise, it's that they appreciate people who take a genuine interest in their work."

hide yuuko
with charaexit

show bg school_library at Fullpan(10.0, dir="left")
with None

"I walk the now-familiar path to Hanako's reading nook, picking out a few titles along the way."

"Sometimes I find it hard to discover a book that will interest me among the shelves. An author's name and a two-word title don't mean much in a sea of similar words."

"For that reason, I sometimes re-read books that I read in the past. Better to bet on the favorite than a new runner."

"An unfamiliar title from a familiar author peeks out among the spines of its neighbors, so I remove it from the shelf."

"At least I'm not going over old material."

scene ev hana_library_read_std
with locationskip

"As expected, Hanako sits on her beanbag, buried deep in a copy of “Dance Dance Dance.”"

hi "Hi Hanako. How's it going?"

"I fight back the urge to ask why she left class early. If Lilly's suspicions were right, then asking her about that could have the opposite effect."

"Best to leave it for the time being. Sometimes the best way to get an answer from someone is to never ask the question."

show ev hana_library_smile_std
with charachange

ha "Hello, H-Hisao. I'm fine."

"Something seems off, and after a couple of seconds, I realize what it is. Hanako's smiling."

"She looks as if she's pleased to see me. It's a nice change from the usual, instinctively frightened reaction, and something I hope I can see more of as we get to know each other better."

hi "Good to hear. How's that book? I've heard it's a trip."

ha "I-it's good… I think."

ha "I've only j-just started it, so I d-don't really know."

hi "Fair enough. Let me know how it goes; I may borrow it once you're done."

ha "S-sure."

"There's a good fifteen minutes left in lunch. Not enough to really get into a book, but too much to stand around doing nothing."

show ev hana_library_read_std
with charachange

"And Hanako's already returned to her reading, so I doubt I'll get much conversation from her."

"Oh well, I'd better make myself comfortable."

play sound sfx_pillow

"I slouch into a beanbag and crack open my book."

"The familiar style of the author leaps out at me from the very first line. As the sentences turn into paragraphs, I start to relax a little."

stop music fadeout 8.0

"But no matter how I try, I can't seem to get myself into the atmosphere of the book."

"This is partly due to the lack of time, but the more distracting factor is Hanako."

show ev hana_library_std
with charachange

show ev hana_library_read_std
with charachange

"Every ten or so seconds she peers over the top of her book, but when our eyes meet she quickly ducks behind the covers."

"I guess she did want to talk about something after all."

scene bg school_library
with locationskip

hi "What's up? You look like a prairie dog on lookout."

show hanako emb_blushing:
    center
    ypos 1.17
with charaenter

ha "N-… it's nothing."

hi "I've told you before, “nothing” means “something” when you say it like that."

show hanako cover_worry
with charachange

"Hanako squirms a little in her beanbag, hoping that by changing her position she'll find the words she's looking for."

show hanako emb_downsad
with charachange

ha "I… I was in an accident."

hi "Accident? Just now? Are you all right?"

show hanako emb_sad
with charachange

"Hanako shakes her head, her hair flowing around her shoulders in wisps of amethyst on a background of pale and dark flesh."

show hanako emb_downsad
with charachange

ha "N-no. When I was y-younger."

play music music_hanako

"Realization crashes into me like a semi."

ha "When I… when I was…"

hi "It's all right Hanako, you don't have to tell me anything if you don't want to…"

"Again she shakes her head."

show hanako emb_sad
with charachange

ha "N-no. I want… I have to tell you."

scene ev hanako_crayon1:
     truecenter zoom 1.0 subpixel True
     linear 20.0 zoom 1.05
with locationskip

ha "When I was young… I was in a fire."

ha "M-my house b-burned down, and I nearly… I nearly didn't make it."

show ev hanako_crayon2:
     linear 8.0 zoom 1.05
with charachange

ha "A-after that… I was alone…"

scene bg school_library
show hanako emb_downsad_close:
    center
    ypos 1.1
with locationskip

"Hanako's eyes glisten in the dim light of the library, and I reach out to grasp her hand."

hi "It's okay, Hanako. You don't have to keep going."

show hanako emb_sad_close
with charachange

ha "B-but… I have to…"

hi "Why? What brought this on?"

show hanako cover_distant_close
with charachange

ha "L-Last night Lilly t-told me about your heart…"

show hanako cover_worry_close
with charachange

ha "A-and I… I didn't think it was f-fair."

hi "Fair?"

show hanako emb_blushing_close
with charachange

ha "T-that I knew about you b-but you didn't know about me…"

"I squeeze Hanako's hand a little."

hi "Don't be silly. But yes, I have a heart condition."

"I lean a little closer to Hanako."

hi "What I didn't tell Lilly is that I had my first attack when a girl confessed to me."

"I smile a little to break the tension."

show hanako cover_worry_close
with charachange

ha "R-really?"

hi "Really. I haven't heard from her for a while though, so I guess it's all over."

"I know it's all over. There's no other way to interpret what happened the last time I saw her. In some ways, not having heard from her again has helped me move on from that period of my life."

hi "So now, we both know a little more about each other. But you don't have to talk about things if you don't want to."

"In fact, I feel a little bad even thinking about that whole incident. I can almost smell the hospital's disinfectant burning the back of my sinuses again."

"I imagine Hanako is going through the same thing now."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\nWhen I was in the hospital I went to the burn ward once, and only once. I was bored, so I went for a walk through all of the wards."

n "I went through oncology and thought I could take it, but when I got to the burn ward I turned around and went back to my bed."

n "To think that Hanako would have spent months in a place like that, smelling nothing but corrupted skin, strong disinfectant and sterilized air."

n "The really bad cases were kept in isolated pods that no foreign objects could enter. That would have meant no reading."

n "\nI would have gone insane if I didn't have my books in the hospital."

n "And she said she was alone…"

n "Did her parents die? I'll have to ask Lilly about it. I can imagine myself saying something dumb unintentionally."

stop music fadeout 2.0

nvl clear
nvl hide dissolve

show hanako emb_timid_close
with charachange

window show

ha "T-thank you, Hisao."

show hanako emb_downtimid_close
with charachange

ha "I… I haven't told many people about this."

hi "To be honest, I haven't told many people about my… circumstances either."

show hanako cover_smile_close
with charachange

ha "T-then I won't tell a-anyone either."

hi "Deal."

play sound sfx_warningbell

"I change my grip on Hanako's hand into a handshake as the warning bells chime through the window."

hi "Well then, we'd better head back to class then, eh?"

show hanako basic_bashful_close
with charachange

ha "S-sure."
$ renpy.music.set_volume(1.0, 0.0, channel="music")

window hide

return

#-------------
