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

"อุตส่าห์โล่งใจที่รอดจากเงื้อมมือพวกสภานักเรียนที่เอาแต่ชวนไปเข้าร่วมมาได้แล้วแท้ ๆ "

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

mi "ยะ—ฮู้~! จบซักที!"

"เห็นได้เลยว่าไม่ใช่ทุกคนที่จะซึมหลังงานเทศกาล"

"คนทั้งห้องมองเธอ คงคิดเหมือนที่ฉันคิดนั่นแหละ"

show misha sign_confused
with charachange

"มิช่ายืนแข็งทื่ออยู่หน้าประตูโดยที่เหยียดแขนอยู่ มองไปรอบ ๆ อย่างประหม่า"

"เธอรู้ตัวแหละว่าบรรยากาศในห้องอึมครึม แต่ไม่รู้จะทำตัวยังไง"

show misha sign_confused at center
with ease_decel

"ทันใดนั้นเองมิช่าก็พุ่งตัวเข้ามา"

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

ha "ระ-เรื่องวันนี้"

hi "โอ้ ได้รายการของลิลลี่มาแล้วใช่ไหม งั้นไปหลังเลิกเรียนเลยแล้วกัน"

show hanako emb_smile
with charachange

ha "อะ-อื้ม"

hi "ฉันจะรอนะ"

"ฮานาโกะยิ้มอย่างอาย ๆ ให้ฉันแวบหนึ่ง แล้วรีบเดินไปยังที่นั่งของเธอทันที"

scene bg school_scienceroom at bgright
with shorttimeskip

play music music_normal fadein 3.0

"ระหว่างคาบก็เห็นได้ชัดว่าไม่ใช่แค่นักเรียนเท่านั้นที่หมดเรี่ยวแรงหลังเทศกาล"

"ครูมุโต้สั่งงานจากหนังสือทิ้งไว้ให้แล้วก็ไปนั่งที่โต๊ะครู"

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

ha "มะ-มีอะไรเหรอ…"

"คงไม่ต้องปิดบังแล้วสินะ…"

hi "โทษที เมื่อกี้มองดูเธอเหมือนคนไปทำอะไรผิดมาอย่างงั้นน่ะ"

show hanako defarms_strain_close
with charachange

ha "มะ- หม-หมายความว่าไง"

hi "ฉันว่าเธออย่าเกร็งไปเลย เราก็ไม่ได้ไปไหนไกลสักหน่อย แถมแถวนี้ก็มีแค่นักเรียนด้วยนี่ จริงไหม"

show hanako def_worry_close
with charachange

ha "อะ-อื้ม"

"รู้สึกลำบากใจนิดหน่อยที่เห็นฮานาโกะดูกังวลมากขนาดนี้"

hi "แล้วเธอเองก็มาทุก ๆ สัปดาห์ด้วยนี่"

show hanako basic_worry_close
with charachange

ha "ชะ-ใช่ กับลิลลี่"

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

ha "นะ- น-นาย ชะ-ช่วย…"

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

ha "กะ-ก็ไม่ขนาดนั้น"

hi "อื้ม ดีแล้ว สงสัยเธอต้องสอนฉันบ้างแล้วละ"

show hanako emb_smile_close_ss
with charachange

ha "ดะ-ได้สิ"

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

ha "มะ-ไม่นะ ฉันไม่ได้… ฉันแค่…"

hi "ล้อเล่น ๆ"

show hanako def_worry_close_ss
with charachange

hi "ฉันมีการบ้านที่ดองไว้สัปดาห์ที่แล้วที่ต้องทำ เพราะงั้นเดี๋ยวต้องไปละ"

hi "ขนไปไหวใช่ไหม"

show hanako cover_bashful_close_ss
with charachange

ha "อะ-อื้ม"

hi "แน่นะ โอเค งั้นไว้เจอกันพรุ่งนี้"

show hanako basic_smile_close_ss
with charachange

ha "บะ-บาย"

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

"ช่วงนี้อากาศเริ่มร้อนขึ้นแล้ว"

"เช้านี้ฉันตื่นมาพร้อมเหงื่อท่วมตัว"

"พอถึงเวลาที่นักเรียนเริ่มออกจากหอพักไปทานอาหารเช้าและทำกิจวัตรประจำวันตอนเช้า แสงแดดก็สาดส่องเต็มที่\nแปลกที่ว่าแสงแดดนั้นกลับทำให้ฉันกระปรี้กระเปร่า"

"ยังไม่แปดโมงด้วยซ้ำ แต่ฉันกลับรู้สึกว่าวันนี้จะต้องเป็นวันหนึ่งที่น่ารื่นรมย์ สงบสุขและอบอุ่น"

"ถ้าไม่ติดว่าฉันอยู่ในโรงเรียนที่มองว่าการขาดของนักเรียนอาจเป็นสัญญาณที่อาจอันตรายถึงชีวิต ฉันก็คงคิดที่จะ\nโดดเรียนทั้งวันหลบไปพักผ่อนอยู่ที่สวนของโรงเรียนไปแล้ว"

"อืม วันนี้คงเป็นวันที่ไม่อยากทำอะไรเลยจริง ๆ"

"ฉันหยุดยืดตัวกะทันหันแล้วนึกถึงคำเตือนของคุณพยาบาลเรื่องการออกกำลังกาย ออกไปวิ่งเหยาะ ๆ ช่วงเช้าต่อ\nน่าจะดี"

"จะให้วิ่งกับคนแบบเอมิก็ดูจะเหนื่อยไปหน่อย แต่ถ้าวิ่งเองเท่าที่ฉันไหวละก็…"

"เอ้อ นี่ฉันคิดว่าตัวเองเป็นใครกัน ฉันคงมุ่งมั่นกับอะไรแบบนั้นไม่ได้นานหรอกถ้าไม่มีแรงจูงใจอะไรเลย"

"ฉันเองก็ไม่ได้นั่งอยู่เฉย ๆ ทั้งวันนะ การเดินไปกลับร้านสะดวกซื้อก็นับเป็นการออกกำลังกายใช่ไหมล่ะ โดยเฉพาะ\nขากลับที่เดินขึ้นมา…"

"อืม ไม่เห็นเป็นไรเลย ถ้าให้เทียบกับตอนที่นอนติดเตียงอยู่โรงพยาบาลหลายเดือน นี่ก็ถือว่าฉันได้ออกกำลังกาย\nเยอะแล้ว"

scene bg school_scienceroom
with shorttimeskip

"ดูเหมือนว่าฉันไม่ได้เป็นคนเดียวที่นึกยินดีกับวันนี้"

"นักเรียนเกือบทุกคนในชั้นเรียนกำลังมองผ่านหน้าต่างออกไปยังท้องฟ้าที่ดึงดูดใจ"

"แม้แต่ชิซูเนะที่ขยันก็ดูขาดความกระตือรือร้นในการเรียนต่างจากทุกที"

"มิช่าที่บ้าบิ่นอยู่แล้ว ถึงกับปลดกระดุมเสื้อสองเม็ดบนออกและกำลังใช้สมุดพัดคลายร้อนให้กับตัวเอง"

"ฉันน่าจะจ้องนานไปหน่อย เพราะเธอแลบลิ้นปลิ้นตาใส่ฉัน"

"แต่เธอก็ไม่ได้แสดงท่าทีว่าจะหยุดเลยแม้แต่น้อยอย่างเปิดเผย"

play sound sfx_normalbell

"เสียงระฆังพักเที่ยงเหมือนจะทำให้ทุกคนประหลาดใจ และคนก็ออกจากห้องเรียนช้ากว่าปกติมาก"

"ดูเหมือนว่าความร้อนกำลังพรากความรีบร้อนไปจากทุกคน"

stop music fadeout 8.0

"ก็แค่เกือบทุกคนอะนะ"

show hanako emb_emb
with charaenter

ha "ฮะ… ฮิซาโอะ"

hi "ไงฮานาโกะ มีอะไรให้ช่วยไหมวันนี้"

"ฮานาโกะถือถุงข้าวกลางวันไว้ในมือ"

"ไม่ต้องฉลาดอย่างนักสืบก็รู้ว่าเรื่องจะเป็นยังไงต่อ"

show hanako emb_smile
with charaenter

ha "เอ่อ… นายอยากจะไปกินข้าวกับพวกเราอีกไหม"

show hanako basic_bashful
with charaenter

ha "ฉะ… ฉันเตรียมมาเผื่อทุกคนเลย"

hi "ดีเลย แต่ไม่ต้องเกร็งขนาดนั้นก็ได้นะ"

show hanako basic_normal
with charaenter

ha "อ่า… อื้ม"

hi "แปลว่าเราจะไปห้องน้ำชากันใช่ไหม"

show hanako cover_worry
with charaenter

ha "ระ… รบกวนด้วยนะ"

show hanako basic_normal
with charaenter

ha "ลิลลี่บอกว่าเธอจะรอเราที่นั่นน่ะ เพราะงั้นเราควร… ควร…"

hi "ควร?"

show hanako emb_smile at center
with charaenter

ha "…ควรไปด้วยกัน…"

hi "ฟังดูดีนี่ อากาศร้อนแบบนี้ก็ชักหิวแล้วสิ"

"ฮานาโกะถอนหายใจโล่งอก ส่วนฉันก็เก็บข้าวของ"

scene bg school_miyagi
with locationskip

play music music_happiness fadein 1.0

"และเช่นเคย บรรยากาศในห้องน้ำชานั้นแสนสดชื่นราวกับถูกตัดขาดจากโลกภายนอก"

"แต่ก็นะ เสียงอึกทึกตามปกติในโรงเรียนดูจะเบาลงไปหน่อย น่าจะเป็นเพราะความขี้เกียจที่เกิดจากความเพลียแดด\nนั่นแหละ"

"ฮานาโกะค่อย ๆ จัดแจงอาหารของเธอลงบนโต๊ะ จดจ่ออยู่กับทุก ๆ การเคลื่อนไหวเล็ก ๆ น้อย ๆ ราวกับว่าเธอกำลัง\nพยายามเบี่ยงเบนความสนใจจากความคิดอื่น ๆ"

"อาจไม่ใช่ของดีเด่อะไร แต่ฉันก็สัมผัสได้จากท่าทางว่าเธอเตรียมทุกอย่างมาอย่างประณีตที่สุด"

hi "ลิลลี่น่าจะยังไม่มา เริ่มกินก่อนเลยไหม"

show hanako emb_timid:
    center
    ypos 1.17
with charaenter

ha "อะ-อีกเดี๋ยวเธอก็มาแล้ว…"

show hanako emb_downtimid
with charachange

"ฮานาโกะพยายามเปิดฝากล่องข้าวแต่ก็ไม่เป็นผล"

hi "มา ขอลองเปิดหน่อย…"

"ฉันหยิบกล่องข้าวมาจากมือฮานาโกะแล้วออกแรงเปิดฝากล่องข้าว"

"ลองจนสุดกำลังแล้ว แต่ก็ดูเหมือนจะปิดแน่นสนิทเลย"

hi "ให้เดานะ เธอปิดฝาตอนข้าวยังร้อนอยู่ใช่ไหมเนี่ย"

show hanako emb_sad
with charachange

ha "ชะ-ใช่ พอดีฉันรีบน่ะ…"

"ฉันวางกล่องข้าวลงบนโต๊ะ"

hi "ก็ว่างั้นแหละ เหมือนกล่องจะปิดแน่นสนิทเลย ต้องหาน้ำร้อนมาราดเปิด"

hi "แต่ให้ทำในนี้น้ำคงหกเลอะเทอะไปทั่ว ไม่ดีแน่"

li "ถ้าอย่างนั้นละก็ ทานส่วนที่ฉันเตรียมมาไหมล่ะจ๊ะ"

show lilly invis at left
with None

show hanako emb_smile:
    tworight
    ypos 1.17
show bg school_miyagi at bgright
show lilly basic_cheerful at twoleft
with dissolvecharamove

"ลิลลี่ยืนยิ้มอยู่ตรงประตูพร้อมชูถุงที่เต็มไปด้วยขนมปังและขนมปังโรลหลากชนิด ฉันอดไม่ได้ที่จะยิ้มตามไปด้วย"

show lilly basic_smileclosed
with charachange

li "ในเมื่อพวกเธอทั้งคู่ยอมเปลี่ยนแผนมาเพื่อฉัน ฉันเลยคิดว่าควรเตรียมอะไรมาสักหน่อยน่ะ"

hi "ขอบใจนะลิลลี่ ฉันช่วยถือให้นะ…"

show lilly basic_smileclosed at Transform(ypos=1.2)
with charamove

"ด้วยความช่วยเหลือเล็กน้อย ขนมปังหลากชนิดของลิลลี่ก็ถูกจัดวางรวมกับอาหารที่ไร้ข้าวของฮานาโกะ ฉันรีบชงชา\nเพื่อเติมเต็มมื้ออาหารให้สมบูรณ์" #ขอไปนอนคิดสักสองสามคืน w/ a little guidance, ...

hi "อืม น่ากินดีนะเนี่ย"

show hanako emb_downtimid
with charachange

"ขณะที่ฉันกินคำแรกก็สังเกตเห็นว่าฮานาโกะพยายามอย่างเต็มที่ที่จะไม่มองมาที่ฉัน"

"ก็เป็นของกินธรรมดา ๆ แต่ก็ว่าไม่ได้ ฉันเองก็ค่อนข้างขี้เกียจเวลาต้องทำอาหารกินเอง"

hi "ไม่เลวนี่ เดาว่าใช้ของซื้อไปเมื่อวานทำใช่ไหม"

show hanako emb_blushtimid
with charachange

ha "ชะ-ใช่"

"สายตาของฮานาโกะจ้องมาที่ฉันราวกับขอความเห็นบางอย่าง"

hi "ก็คุ้มละที่ซื้อมา ขอบใจนะฮานาโกะ"

show hanako cover_bashful
with charachange

ha "ฉัน… ฉันอยากให้นายเห็น… หลังจากที่เมื่อวาน…"

hi "ไม่เป็นไรหรอก ฉันแค่แปลกใจนิดหน่อยกับของที่เธอซื้อน่ะ"

show lilly basic_weaksmile
with charachange

li "ฮานาโกะชอบทดลองทำอาหารน่ะ ฉันว่าก็ออกมาดีนะ… ส่วนมาก… อะนะ"

"แม้รอยยิ้มของลิลลี่จะยังเหมือนเดิม แต่น้ำเสียงของเธอที่เปลี่ยนไปเล็กน้อยทำให้รู้ว่าก่อนหน้านี้คงไม่ค่อยราบรื่น\nสักเท่าไหร่"

"ก็ใช่ว่าจะมีใครที่ไหนมาชิมอาหารที่ฮานาโกะทำนี่นะ…"

stop music fadeout 7.0

"เดี๋ยวนะ… ไม่ใช่ว่าลิลลี่รอให้ฉันกินก่อนใช่ไหมเนี่ย ตอนก่อนที่ฉันจะบอกว่าโอเคนี่เห็นยังไม่ได้แตะเลย…"

"รอยยิ้มเจ้าเล่ห์ของเธอบ่งบอกว่าเธอจงใจนั่นแหละ ฉันคงต้องหาวิธีเอาคืนเธอจากเรื่องนี้ให้ได้"

hi "ก็อร่อยดี แค่นั้นก็พอแล้วนี่ จริงไหม"

show hanako basic_smile
with charachange

ha "อะ-อื้ม"

show lilly basic_smileclosed
with charachange

"ลิลลี่ที่พอใจกับการที่ไม่ใช่คนแรกที่ได้ลิ้มลองฝีมือของฮานาโกะเริ่มลงมือกินอาหารตรงหน้าทันที"

"ฉันคอยจ้องมองไปตามตะเกียบของเธอที่แตะลงบนจานอย่างแผ่วเบา ปลายตะเกียบนั้นเขี่ยและลากเบา ๆ เพื่อระบุ\nตำแหน่งโดยคร่าว ๆ จากนั้นเธอก็คีบอาหารขึ้นมาอย่างคล่องแคล่ว"

"ถ้าไม่ใช่บริบทอย่างนี้แล้วบางคนอาจจะคิดว่าเธอกำลังเล่นของกินเหมือนเด็ก ๆ แต่ต่อให้จะคิดอย่างนั้น ท่าทางของเธอ\nก็เป็นไปอย่างเรียบร้อยและสบาย ๆ จนเห็นได้ชัดว่านี่เป็นเพียงวิธีการกินอาหารแบบนี้ของเธอเท่านั้นเอง"

"ด้วยไม่อยากจะตามใครไม่ทัน ฉันจึงหันมากินต่อ"

show hanako emb_downsmile
with charachange

"ฮานาโกะใช้วิธีที่ต่างออกไป เธอรอจนกระทั่งลิลลี่กับฉันหยิบกันจนเสร็จแล้วค่อยรีบฉวยส่วนของเธอไปอย่างรวดเร็ว"

show hanako emb_smile
with shorttimeskip

play music music_dreamy fadein 4.0

"ไม่นานนักของกินในกล่องก็หมดเกลี้ยง เหลือเพียงกล่องข้าวที่ยังคงปิดสนิท"

show lilly basic_smile
with charachange

li "ขอบคุณนะฮานาโกะ อิ่มมากเลย"

show hanako basic_smile
with charachange

ha "มะ-ไม่หรอก… ต้องขอบคุณเธอเรื่องขนมปังต่างหาก…"

hi "นั่นสิ คงแย่แน่ ๆ ถ้าไม่มีมาน่ะ"

show lilly basic_planned
with charachange

li "ด้วยความยินดีทั้งคู่จ้ะ"

show lilly basic_weaksmile
with charachange

li "แต่ตอนนี้ฉันต้องขอตัวก่อนนะ มานั่งกินข้าวที่นี่ทีไรเผลอแป๊บเดียวก็สายทุกทีเลย"

hi "อืม เข้าใจ ๆ กะว่าเก็บของเสร็จแล้วก็จะไปเหมือนกัน"

show lilly basic_smileclosed at twoleft
with dissolvecharamove

li "ถ้างั้นก็ โชคดีจ้ะ"

hide lilly
with charaexit

show hanako basic_smile:
    center
    ypos 1.17
show bg school_miyagi at center
with charamove

"ลิลลี่ออกจากห้องไป เสียงไม้เท้าของเธอเคาะดังเป็นจังหวะไปตามโถงทางเดินที่เงียบสงบ"

"ฮานาโกะกับฉันรีบเก็บของของพวกเราแล้วนั่งรอระฆังดัง"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene bg misc_sky at Fullpan(20.0)
with locationchange

"เราสองคนจ้องมองออกไปนอกหน้าต่างสู่ท้องฟ้าสีครามอันไร้ที่สิ้นสุด"

play sound sfx_warningbell

"ถ้าไม่ได้ยินเสียงระฆังดัง ฉันคงคิดว่าเวลาหยุดเดินไปแล้วเสียอีก"

"ความอยากโดดเรียนเริ่มก่อตัวในใจฉัน"

"ฉันหันไปมองฮานาโกะ ซึ่งยังนิ่งไม่ไหวติงเช่นกัน"

ha "ขอ… อยู่ต่ออีกแป๊บนึง…"

$ renpy.music.set_volume(1.0, 3.0, channel="music")

scene bg school_miyagi
show hanako basic_smile:
    center
    ypos 1.17
with shorttimeskipsilent

"ช่วงเวลาระหว่างเสียงระฆังเตือนให้เข้าห้องกับเสียงระฆังหมดเวลาพักเที่ยงผ่านไปในพริบตาเดียว"

hi "เราต้องไปจริง ๆ แล้วละ… ไม่งั้นคนน่าจะแตกตื่นแล้วออกตามหาแน่ถ้าเราโดดเรียน…"

show hanako basic_distant
with charachange

"ฮานาโกะถอนหายใจ"

show hanako basic_normal
with charachange

ha "ก็จริง"

show hanako basic_normal at center
with charamove

"เธอค่อย ๆ ลุกช้า ๆ และฉันก็ลุกตาม"

scene bg school_staircase2
with locationskip

"เราสองคนเดินขึ้นบันไดเก่า ๆ ไปยังชั้นสามอย่างเงียบ ๆ แล้วตรงไปยังห้องเรียนของเรา"

scene bg school_hallway3
with locationchange

play sound sfx_dooropen

"พอถึงหน้าห้องฉันก็มายืนหน้าฮานาโกะเปิดประตูพร้อมก้มหัวขอโทษล่วงหน้า"

scene bg school_scienceroom at center
with locationchange

stop music fadeout 5.0

hi "ขอโทษที่เข้าสายครับครู"

play sound sfx_doorclose

"ไม่มีคำพูดอันแข็งกร้าวหรือคำสั่งให้ไปนั่งที่ด้วยความโกรธตอบกลับมา แต่มีเพียงความเงียบที่เกิดจากนักเรียนประมาณ\nสิบห้าคนที่กลั้นขำ"

"ครูมุโต้ผู้สายเสมอยังไม่มาถึง แต่ฉันกับฮานาโกะที่มาด้วยกันนั้นมาถึงอย่างชัดแจ้งแล้ว"

show misha hips_grin at center
with charaenter

mi "พรูด… วะฮะ…"

"เอาใหม่ ประมาณสิบสี่คนที่กลั้นอยู่ และอีกคนที่ไม่ไหวละ"

play music music_comedy

show misha cross_laugh
with charachange

mi "พรูด วะฮ่าฮ่าฮ่า! คู่รักเขามาโน่นแล้ว~!"

show misha hips_laugh
with charachange

mi "วะฮ่าฮ่าฮ่า~!!"

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

"พอก้าวผ่านประตูเข้าไปก็รู้ตัวว่าฮานาโกะกำลังแนบชิดติดแผ่นหลังฉันเพื่อซ่อนตัวจากเพื่อนร่วมชั้น"

show hanako invis_close:
    xpos 0.7
with dissolvecharamove

"พอเริ่มใกล้ที่นั่งฉันแล้วเธอก็ยอมผละจากฉันแล้วเดินตัวแข็งทื่อไปยังโต๊ะของเธอเอง ความพยายามที่จะกีดกั้นทุกคน\nออกจากความคิดนั้นปรากฏชัดเจนบนใบหน้าของเธอ"

scene bg school_scienceroom at bgright
with charamove

"ฉันเหลือบมองประตูอย่างรวดเร็วเพื่อดูว่าครูมาหรือยัง ก่อนจะรีบเดินไปที่โต๊ะของฮานาโกะแล้วกระซิบข้างหูเธอ"

hi "ไม่ต้องไปคิดมากเรื่องมิช่าหรอก เธอก็เป็นงี้ตลอดแหละ วันนี้ฉันสนุกมากเลย เพราะงั้นอย่าเครียดเลยนะ โอเคไหม"

"ฮานาโกะพยักหน้าที่ฟุบกับโต๊ะอยู่"

play sound sfx_dooropen

show muto invis at tworight
with None

show muto normal at center
show bg school_scienceroom at center
with dissolvecharamove

"ฉันอยากอยู่ปลอบใจเธอมากกว่านี้ แต่ครูมุโต้ก็เข้ามาในห้องพอดีพร้อมกับบรรยายไปครึ่งทางแล้ว ราวกับว่า\nเริ่มบรรยายตั้งแต่ในโถงทางเดิน"

show muto smile at center
with charaenter

mu "…ซึ่งแน่นอนว่า แปรผันตรงกับประจุ แต่แปรผกผันกับระยะทางกำลังสอง…"

hide muto
with charaexit

play sound sfx_doorclose

"ครูมัวแต่สนใจกับการบรรยายของตัวเองจนไม่ทันสังเกตเห็นฉันที่กำลังย่องจากโต๊ะฮานาโกะกลับไปนั่งที่"

"ในขณะที่ครูมุโต้ยังคงบรรยายไปเรื่อยเปื่อยนั้นมิช่าก็เอนตัวเข้ามาหาฉัน"

show misha invis at offscreenleft
with None

show misha perky_smile_close:
    xanchor 0.5 xpos 0.16
with dissolvecharamove

mi "ครูอาจจะไม่เห็นว่านายมาสาย แต่ฉันเห็นนะ"

"ก็เห็นชัดตั้งแต่ที่เธอทำเมื่อกี้ละนะ"

show misha hips_grin_close
with charachange

mi "ฉันรับคำสั่งมาว่าวันนี้ให้ปล่อยเธอไปก่อน แต่มีเงื่อนไขข้อหนึ่ง"

hi "โอ้ แล้วเงื่อนไขที่ว่าคือ?"

show misha sign_smile_close
with charachange

mi "นายจะต้องมาช่วยเราช่วงบ่ายนี้~!"

"ฉันชะเง้อคอมองข้ามไหล่ของมิช่าไป"

"ชิซูเนะไม่ยอมสบตาราวตั้งใจเลี่ยง"

hi "ก็ได้ แค่วันนี้เท่านั้นนะ"

hi "ฉันบอกเธอไปแล้วนะว่าฉันไม่เข้าสภาน่ะ จำได้ไหม"

show misha hips_grin_close
with charachange

mi "จำได้สิ! การทำแบบนั้นอาจจะถือว่า… เอ่อ ถือว่าเป็นการ…"

show misha perky_confused_close
with charachange

"เธอก้มมองสมุดจดของเธอ แน่นอนว่าเพื่อหาคำตอบตามบทที่เตรียมมา"

show misha hips_grin_close
with charachange

mi "…ขู่เข็ญ ซึ่งขัดต่อกฎระเบียบ"

hi "แปลกเนอะที่เธอมาสนใจเรื่องกฎระเบียบอะไรตอนนี้น่ะ"

show misha sign_smile_close
with charachange

mi "ทุกอย่างควรทำตามกฎระเบียบนะ!"

show misha perky_smile_close
with charachange

mi "แค่ว่ากฎไม่ได้เขียนไว้ครอบคลุมทุกสถานการณ์ เพราะงั้นอาจมีบางกรณีที่สามารถละเลยกฎได้"

hi "เนี่ย แล้วก็มาสงสัยว่าทำไมถึงไม่มีใครอยากเข้าสภาเลย…"

stop music fadeout 3.0

show misha hips_frown_close
with charachange

with Pause(0.3)

show misha invis at offscreenleft
with dissolvecharamove

hide misha
with None

"หลังจากแลบลิ้นปลิ้นตาใส่ฉัน มิช่าก็หันไปอยู่กับสมุดแบบฝึกหัดของเธอต่อ แล้วเราก็ฝ่าฟันช่วงบ่ายของวันเรียนที่เหลือ\nไปได้"

with shorttimeskip

play sound sfx_normalbell

show shizu invis_close at offscreenright
show misha invis_close at offscreenleft
with None

show misha hips_smile_close at twoleft
show shizu behind_blank_close at tworight
with Dissolvemove(0.5, time_warp=_ease_in_time_warp)

"มิช่ากับชิซูเนะเข้ามาจับไหล่ฉันก่อนที่ฉันจะทันได้ลุกด้วยซ้ำ"

hi "เออ ก็บอกแล้วว่าจะไปช่วยน่า…"

play music music_shizune fadein 1.0

show misha hips_grin_close
with charachange

mi "เพื่อความมั่นใจไงฮิซาโอะ เพื่อความมั่นใจ~!"

show hanako invis behind shizu at offscreenright
with None

show misha hips_smile_close at Transform(xpos=0.17)
show shizu behind_blank_close at Transform(xpos=0.5)
show bg school_scienceroom at bgleft
show hanako emb_timid:
    xanchor 0.5 xpos 0.9
with dissolvecharamove

ha "ฮะ-ฮิซาโอะ"

"ฮานาโกะเดินอ้อมพวกเราเพื่อออกจากห้องอย่างอาย ๆ ฉันพลันนึกขึ้นมาว่านี่อาจเป็นโอกาสเดียวที่ฉันจะหนีรอดไปได้"

hi "อ้าว ฮานาโกะ มีอะไรเหรอ"

show shizu basic_angry_close
with charachange

shi "…"

show misha hips_frown_close
with charachange

mi "นี่ เราไม่มีเวลาว่างที่จะมาคุยเล่นหรอกนะ"

hi "ใจเย็นน่า คุยไม่นานหรอก… โทษทีนะฮานาโกะ เมื่อกี้ว่าไงนะ"

show hanako emb_downtimid
with charachange

ha "ฉัน… ฉันว่าจะไปห้องสมุดน่ะ แล้ว… แล้วก็…"

"นิ้วหัวแม่มือของฮานาโกะขยับไปมา ตาเธอหลุกหลิกมองไปทั่วห้องยกเว้นที่พวกเรา"

show misha sign_smile_close
with charachange

mi "ขอโทษทีนะฮานาโกะ แต่ฮิซาโอะต้องไปกับพวกเรา พอดีเขามีงานที่ต้องทำน่ะ"

show shizu behind_smile_close
with charachange

shi "…"

show misha hips_grin_close
with charachange

mi "อ้อ! แต่ถ้าอยากช่วยจะมาด้วยก็ได้นะ"

show hanako cover_worry
with charachange

ha "เอ่อ…"

label th_choiceH4:
menu:
    with menueffect

    mi "แล้ว นายจะเอายังไงล่ะฮิซาโอะ"

    "เธอคิดว่าไงล่ะ ฮานาโกะ?":
        return m1

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

hi "เธอว่าไงล่ะฮานาโกะ ถ้าเราช่วยกันแป๊บเดียวคงเสร็จ"

show hanako emb_timid
with charachange

"อาการอยู่ไม่สุขของฮานาโกะบอกคำตอบให้ฉันรู้ก่อนที่เธอจะทันได้พูดอะไรเสียอีก"

show hanako emb_downtimid
with charachange

ha "ฉะ… ฉันต้องไปแล้วน่ะ…"

"ก็ตามคาด ดูท่าแล้วคงมีแค่ฉันกับสาว ๆ ในสภาเช่นเดิม"

"คงจะง่ายกว่าที่ยอมไปทำงานในช่วงบ่าย ในห้องทำงานเล็ก ๆ ของสภานักเรียน"

hi "งั้นเดี๋ยวฉันตามไปนะ โอเค?"

show hanako emb_smile
with charachange

ha "อะ-โอเค"

stop music fadeout 3.0

show misha hips_grin_close at twoleft
show shizu behind_smile_close at tworight
show hanako invis at offscreenright
show bg school_scienceroom at center
with dissolvecharamove

show misha hips_smile_close at twoleft
hide hanako
with charachange

mi "เอ้า! ร่ำลากันเสร็จก็ไปทำงานได้แล้ว!"

scene bg school_hallway3
with locationchange

"มิช่ากับชิซูเนะพาตัวฉันเดินไปที่ห้องสภานักเรียนโดยจับไหล่ฉันไว้ไม่ปล่อยเลย"

"รู้สึกผิดนิดหน่อยแหละที่ทิ้งฮานาโกะไว้แบบนั้น แต่ถ้าฉันยอมมาแล้วมิช่าจะไม่ไปยุ่งกับฮานาโกะอีกก็เอาเถอะ"

scene bg school_council
with locationchange

hi "แล้ววันนี้จะทำอะไรกัน"

show misha sign_smile at center
with charaenter

play music music_ease fadein 8.0

mi "สรุปงาน!"

hi "ฮะ? ไม่ใช่ว่าต้องสรุปหลังทำอย่างอื่นเหรอ"

show misha hips_grin
with charachange

mi "อื้ม! เราต้องจัดเอกสารของงานเทศกาลให้ชิซูเนะสรุปส่งครูน่ะ"

show misha hips_grin at twoleft
show bg school_council at bgleft
with charamove

show shizu adjust_happy at tworight
with charaenter

"ชิซูเนะวางเอกสารกองใหญ่ลงบนโต๊ะหน้าฉัน แล้วยิ้มแวบหนึ่ง"

show misha hips_smile
with charachange

mi "นายต้องแยกเอกสารออกเป็นสองกอง"

show misha sign_smile
with charachange

mi "กองหนึ่งสำหรับพวกการเงิน เช่นใบเสร็จ อีกกองสำหรับข้อเสนอแนะ อีกกองข้อเสนอแนะเชิงบวก อาจจะมีอีกกอง\nสำหรับปัญหาที่อาจจะเกิดในปีหน้า แล้วก็กองนึงสำหรับปัญหาที่น่าจะแก้ไม่ได้… "

hi "นับ ๆ ดูแล้วเกินสองกองไปอยู่นะ…"

show misha perky_confused
with charachange

mi "ฮะ อ๋อ ช่าย ตอนแรกนึกว่าแค่สองกองน่ะ โทษที"

hi "อ่าฮะ แล้วระหว่างที่ฉันทำงานนี่ พวกเธอจะทำอะไรล่ะ"

show misha hips_grin
show shizu adjust_smug
with charachange

mi "ก็ พวกเราไม่ได้กินข้าวเที่ยงก็เพราะรวบรวมรายงานนี่แหละ เลยว่าจะไปหาอะไรกินสักหน่อย!"

"แล้วทำไมถึงไม่แยกเอกสารตั้งแต่ตอนรวบรวมล่ะหา…"

"โชคยังดีที่กลไกป้องกันตัวเองของฉันทำงานโดยการยั้งไม่ให้ฉันอ้าปากพูดอะไรที่จะทำให้สถานการณ์แย่กว่าเดิม\nออกไป"

show misha perky_confused
with charachange

mi "เอ๋?!"

show misha perky_sad
with charachange

mi "ไม่ยุติธรรมเลย"

show shizu behind_blank
with charachange

shi "…"

"ฉันมัวแต่กังวลกับการแบ่งงานที่ไม่ยุติธรรมจนไม่ทันสังเกตว่าชิซูเนะส่งภาษามืออยู่"

"ถ้าไม่ใช่เพราะมิช่าหลุดพูดมา ฉันคงไม่รู้ตัวด้วยซ้ำ"

show shizu adjust_smug
with charachange

show shizu basic_normal
with charachange

show shizu behind_blank
with charachange

"ดูเหมือนชิซูเนะกำลังสั่งงานมิช่ายาวเหยียด และดูเหมือนจะไม่มีงานไหนน่าอภิรมย์เลย"

show misha sign_sad
with charachange

show misha perky_sad
with charachange

show misha perky_sad at Transform(ypos=1.15)
with charamove

"หลังจากได้ข้อสรุปแล้ว มิช่าก็ส่งภาษามือตอบกลับชิซูเนะสั้น ๆ แล้วนั่งลงที่โต๊ะข้าง ๆ ฉัน"

show shizu adjust_happy
with charachange

hide shizu
with charaexit

show misha perky_sad at Transform(xpos=0.5)
show bg school_council at center
with charamove

"ชิซูเนะโบกมือให้พวกเราสองคนก่อนที่จะหายออกไป"

hi "เมื่อกี้คุยอะไรกัน"

show misha perky_confused
with charachange

mi "ชิจังกลัวว่าถ้าไม่มีคนคอยดูแล้วนายจะทำทุกอย่างผิดหมดน่ะ"

show misha perky_sad
with charachange

mi "และในเมื่อเธอเองก็บอกนายไม่ได้ว่านายทำผิดอยู่หรือเปล่า เธอเลยให้ฉันอยู่นี่น่ะ โธ่… แย่จัง ฉันก็อยากไปกับชิจังนะ!"

show misha cross_smile
with charachange

mi "แต่ชิจังก็จะไปซื้อข้าวมาให้เรานะ~!"

show misha cross_grin
with charachange

mi "เยี่ยมไปเลยใช่มะ!"

"อารมณ์พลิกผลันของมิช่านี่สุดยอดไปเลย จากที่หงอย ๆ ทำคอตกแล้วก็ร่าเริงทำคอตั้งขึ้นมาได้เพราะอาหารเนี่ย"

"ยากที่จะหาใครเปรียบได้จริง ๆ"

hi "ก็ อาจจะไม่เยี่ยมขนาดนั้นก็ได้"

hi "อะ แล้วต้องทำอะไรบ้าง"

show misha sign_smile
with charachange

mi "จัดเอกสาร"

hi "เอามารวมแล้วนี่ไง"

show misha hips_smile
with charachange

mi "ถ้างั้น ก็เริ่มแยกออกเป็นกอง ค่อยมาดูว่าแต่ละกองคืออะไรอีกที"

hi "ได้…"

show misha perky_smile
with charachange

"พวกเราเริ่มแยกเอกสารออกเป็นหลาย ๆ กองที่ซับซ้อนขึ้นเรื่อย ๆ"

"ตอนแรกก็แค่ตามหมวดหมู่ง่าย ๆ อย่างการเงิน ข้อเสนอแนะ รายงานเหตุการณ์…"

"แล้วกองพวกนั้นก็แยกออกเป็นรายงานที่ดีและไม่ดี แล้วก็ยังซอยย่อยลงไปอีก จนเริ่มจะเหมือนว่าแค่เอาแผ่นกระดาษ\nมาวางเรียงแผ่หลาอยู่บนโต๊ะแล้ว"

hi "จะเสร็จมั้ยเนี่ย"

show misha perky_confused
with charachange

mi "ฮะ ทำไมล่ะ ก็ทำตามสั่งแล้วนี่ ใช่มะ"

hi "ก็ใช่ แต่ตอนนี้เหมือนแค่เอามาวางเล่น ๆ เลยเนี่ย"

show misha hips_grin
with charachange

mi "ไม่นะ ฉันว่าเราทำไปได้เยอะแล้วล่ะ เดี๋ยวชิจังน่าจะมาจัดการต่อได้"

show misha cross_grin
with charachange

mi "เพราะงั้นฉันว่าเราพักมือกันตรงนี้แหละ"

"นี่สามัญสำนึกของมิช่าติดตัวชิซูเนะออกห้องไปพร้อมกันแล้วหรืออะไร"

"แต่ก็นะ เถียงไปก็ไม่ได้อะไรขึ้นมา"

show misha sign_smile
with charachange

mi "เอาเถอะ…"

show misha cross_smile
with charachange

mi "แล้วนายตกลงอะไรกับฮานาโกะไว้ล่ะ"

hi "ตกลงอะไร?"

show misha hips_smile
with charachange

mi "วันนี้นายไปอยู่กับฮานาโกะมาไม่ใช่เหรอ~"

show misha hips_grin
with charachange

mi "แอบไปกุ๊กกิ๊กอะไรกันมาหรือเปล่า หรือแอบซ่อนอะไรเด็ด ๆ ไว้"

hi "ถ้าฉันเล่าให้เธอฟังมันก็ไม่เรียกว่าแอบแล้วไหม"

show misha perky_confused
with charachange

mi "ก็คงไม่…"

hi "พวกเราก็แค่เพื่อนกันน่ะ คิดว่านะ"

hi "แล้วเธอจะอยากรู้อะไรขนาดนั้นล่ะ เธอกับชิซูเนะไม่ชอบฮานาโกะไม่ใช่เหรอ…"

show misha cross_frown
with charachange

mi "ก็ไม่เชิงหรอก นายก็รู้ชิจังกับลิลลี่ไม่ค่อยถูกกัน"

mi "แล้วฮานาโกะก็แทบอยู่ไม่ห่างจากลิลลี่เลย ก็เลยไม่ค่อยได้คุยกันเท่าไหร่"

show misha sign_smile
with charachange

mi "แต่ก็ไม่ได้หมายความว่าฉันไม่ได้เป็นห่วงฮานาโกะสักหน่อย"

hi "แล้วมีอะไรน่าเป็นห่วงล่ะ"

show misha perky_sad
with charachange

mi "ก็ ฮานาโกะไม่เคยจะไปอยู่กับคนอื่น ๆ เลย ใช่ไหมล่ะ ซึ่งไม่ดีเลยฮิจัง!"

"ถ้าชิซูเนะกับลิลลี่ไม่ชอบหน้ากันเพราะ “นิสัยแตกต่างกัน” ก็ไม่อยากนึกสภาพเลยว่าความสัมพันธ์ของมิช่าและ\nฮานาโกะจะเป็นยังไง…"

show misha perky_confused
with charachange

mi "เนี่ย ดู ๆ ไป พวกเราก็เป็นห่วงฮานาโกะไม่ต่างกันเลย จริงไหมล่ะ~"

hi "ก็ คงงั้นแหละ"

show misha sign_smile
with charachange

mi "มีอยู่ครั้งหนึ่งที่ฮานาโกะออกห้องไปตอนกำลังเรียนกันอยู่แล้วชิจังก็เดินไปถามครูว่าจะเอายังไงดี"

show misha sign_confused
with charachange

mi "ครูบอกว่านักเรียนทุกคนที่นี่ต่างก็มีเรื่องอะไรเฉพาะตัวที่ต่างกันไป ซึ่งชิจังไม่ต้องเป็นห่วงหรอก"

show misha perky_confused
with charachange

mi "ฮานาโกะชอบหนีไปก่อนไม่ยอมทำงานกลุ่มเรื่อยเลย"

mi "แค่นั้นก็น่าเป็นห่วงพอแล้วนี่"

hi "ก็คงงั้นละนะ ฮานาโกะแทบไม่พูดอะไรด้วยซ้ำตอนเราคุยกัน"

show misha perky_sad
with charachange

mi "ก็ถือว่าทำได้เยอะกว่าที่ฉันเคยทำได้อีก ตอนฮานาโกะจะคุย ฉันกับชิจังก็ลองคุยดูด้วยแล้ว แต่ฮานาโกะก็กลัว\nแล้วหนีไป"

"ฉันคิดจะบอกมิช่าว่าเจอมาแบบเดียวกัน แต่เหมือนมิช่าก็กำลังคิดอะไรอยู่จนไม่ได้สนใจ"

"ได้ฟังมิช่าโดยไม่ได้มีชิซูเนะประกบอยู่ด้วยนี่ก็… น่าสนใจดี"

show misha cross_frown
with charachange

mi "ฉันว่าฮานาโกะต้องรู้ตัวก่อนว่าคนอื่นไม่ได้สนใจรูปลักษณ์ภายนอกอะไรขนาดนั้น แล้วก็ต้องหัดเชื่อใจพวกเราบ้าง"

show misha cross_smile
with charachange

mi "ถ้าเข้าใจเมื่อไหร่ฉันก็หมดห่วง"

"น่าจะครั้งแรกเลยมั้งที่ได้เห็นมิช่าอยู่นิ่ง ๆ โดยที่ไม่ใช้ภาษามือเลย"

"เวลาอยู่กับชิซูเนะ มิช่าจะโบกมือไปมาตลอดเวลาเพื่ออธิบายสิ่งโดยรอบให้ชิซูเนะเข้าใจ"

"ต่อให้จะเป็นคนที่ใช้สมองได้คล่อง แต่ถ้าต้องใช้ประสาทขนาดนั้นก็คงล้าเหมือนกัน"

"และว่ากันตามตรง มิช่าก็ไม่ใช่คนที่หลักแหลมขนาดนั้นหรอก"

hi "อืม เดี๋ยวฉันช่วยดูฮานาโกะให้เธอละกัน"

hi "แต่เธอก็คงต้องไปขอโทษเรื่องเมื่อกี้ด้วยนะ ฉันว่าฮานาโกะคงไม่ชอบมุกตลกแบบนั้นหรอก"

show misha perky_confused
with charachange

mi "โอ๊ะ อ๋อ~!"

show misha perky_sad
with charachange

mi "ไม่รู้ตัวเลย ขอโทษที"

hi "ไม่ต้องขอโทษฉันหรอก ไปขอโทษฮานาโกะนู่น"

show misha perky_smile
with charachange

mi "โอเค พรุ่งนี้เช้าฉันจะตรงไปขอโทษฮานาโกะก่อนเลย"

hi "ดี"

play sound sfx_doorslam
with vpunch

"เสียงอึกทึกครึกโครมจากประตูป่าวประกาศการกลับมาของชิซูเนะ"

"คาดว่าเธอคงไม่รู้ตัวว่าทำเสียงดังขนาดไหน"

show misha hips_grin
with charachange

mi "โอ้ ชิจัง! เธอกลับมาแล้ว!"

show shizu invis at Transform(xanchor=0.5, xpos=1.0)
with None

show misha hips_grin at Transform(xpos=0.3)
show shizu behind_blank at tworight
show bg school_council at bgleft
with dissolvecharamove

"ชิซูเนะปรากฏตัวขึ้นพร้อมกับของที่ซื้อจากร้านสะดวกซื้อเต็มไม้เต็มมือไปหมด"

show shizu basic_normal2
with charachange

shi "…"

show misha sign_smile
with charachange

mi "พอดีมีงบเหลือจากงานเทศกาลอยู่บ้างน่ะ แล้วตอนนี้ก็นับว่าเป็นเรื่องงานเทศกาลอยู่ ก็เลยจัดเต็มสักหน่อย"

show misha hips_grin
with charachange

mi "ความคิดดีเลยชิจัง สิบคะแนนเต็ม"

hi "ทำได้ด้วยเหรอ"

show shizu cross_angry
with charachange

shi "…"

show misha cross_frown
with charachange

mi "ตัวเองไม่ยอมเข้าร่วมแท้ ๆ จะมาสนใจเรื่องการจัดการในสภาอะไรขนาดนั้น"

show misha cross_grin
show shizu adjust_smug at tworight
with charachange

mi "ฉันจะลงโทษความอวดดีของนายด้วยการปันส่วนอาหารให้แค่เล็กน้อยเท่านั้น"

hi "เออ เออ เข้าใจแล้ว"

show misha perky_smile
show shizu adjust_happy at Transform(ypos=1.15)
with dissolvecharamove

"มิช่าขยับกองเอกสารหลายกองไปข้าง ๆ เพื่อกันที่ให้กองอาหารที่ชิซูเนะกำลังจัดวาง"

"ขณะที่ฉันมองดูงานที่อุตส่าห์ทำอย่างหนักแต่ผิดวัตถุประสงค์กลายเป็นของไร้ค่า ฉันก็นึกได้ว่าการที่สองคนนี้ต้องการ\nให้คนมาช่วยนั้นไม่ได้แปลกอะไรเลย"

"อาหารจากร้านสะดวกซื้อรสชาติไม่ได้ดีเลิศอะไร แต่อย่างน้อยก็ทำให้อิ่มท้องได้"

show shizu behind_smile
with charachange

shi "…"

show misha sign_smile
with charachange

mi "ขอบใจนะที่วันนี้มาช่วย ส่วนใหญ่เราก็ทำแต่เอกสารส่งให้ทางโรงเรียนนั่นแหละ"

show misha perky_smile
with charachange

mi "อย่างน้อยปีนี้ก็พอมีหัวข้อในการสรุปดี ๆ ได้แล้ว"

hi "แน่ใจเหรอว่าไม่ใช่การทุจริตน่ะ"

show misha hips_grin
with charachange

mi "ไม่เลย ๆ พวกเราทำตามกฎระเบียบแล้ว ถ้ากฎเขียนไม่ครอบคลุม เราก็ไม่ผิดสักหน่อย"

hi "ก็นั่นไม่ใช่เหรอที่เรียกว่าทุจริตน่ะ…"

show misha hips_smile
with charachange

mi "คิดมากน่า~!"

hi "เออ ๆ ก็น่าจะถูกของเธอแล้วแหละ"

hi "เอาเถอะ ต้องไปละ…"

hi "…ถ้าเธอให้ฉันไปได้อะนะ"

show shizu adjust_smug
with charachange

shi "…"

show misha hips_grin
with charachange

mi "งานของนายถือว่าเพียงพอแล้ว ไปได้"

hi "อืม ขอบใจ"

hi "รู้อะไรไหม ถ้าเธอเน้นเรื่อง “อาหารฟรี” มากกว่า “งานที่ไม่มีวันหมด” เธออาจจะได้คนมาช่วยเยอะกว่านี้ก็ได้นะ"

stop music fadeout 6.0

show misha sign_smile
with charachange

show shizu behind_blank
with charachange

mi "ที่นายพูดก็น่าจะจริง"

hi "อืม ฝากไว้ให้คิด"

hi "แล้วก็ไปคิดเรื่องที่เราคุยกันไปก่อนหน้าด้วย… ไม่ต้องบอกชิซูเนะก็ได้นะถ้าไม่อยาก"

show misha perky_confused
with charachange

mi "ฮะ อ๋อ อืม เดี๋ยวพรุ่งนี้จะลองไปหาดู"

show misha perky_smile
with charachange

mi "ราตรีหวัด ฮิจัง"

hi "ราตรีหวัดมิช่า ชิซูเนะ"

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

hi "นี่ชิซูเนะ คือฉันก็บอกเองแหละว่าจะช่วย แต่พอดีตอนนั้นลืมไปว่าติดพันอย่างอื่นแล้ว อีกอย่าง สัปดาห์ที่แล้วฉันก็\nช่วยงานไปเยอะเกินพอสมควรแล้วนะ"

hi "สัญญาเลยว่าเดี๋ยวจะมาช่วยวันหลัง"

show misha sign_confused_close
with charachange

show shizu basic_frown_close
with charachange

show misha perky_smile_close
with charachange

show shizu behind_blank_close
with charachange

"ชิซูเนะกับมิช่าปล่อยมือแล้วนิ่งเงียบไปสักพักใหญ่ ๆ"

show misha sign_smile_close
with charachange

mi "อืม ที่นายพูดก็ถูก ว่าตามตรงเราแค่จะใช้งบที่เหลือซื้อเค้กกินกันน่ะ"

show misha cross_laugh_close
with charachange

mi "ซึ่งถ้านายไม่มาด้วยก็ดี ตัวหารจะได้น้อยลงด้วย วะฮ่าฮ่าฮ่า~!"

stop music fadeout 6.0

show shizu invis at offscreenleft
with dissolvecharamove

show misha invis at offscreenleft
with dissolvecharamove

hide shizu
hide misha
with None

"ชิซูเนะหันหลังกลับและเดินออกไป ส่วนมิช่าก็กระโดดโลดเต้นตามเธอไป"

hi "อืม ง่ายกว่าที่คิดแฮะ สัปดาห์ที่แล้วนี่ทำตัวอย่างกับหมาล่าเนื้อ หรือจะเรียกผู้คุมดี"

hi "หรือไม่ก็เป็นผู้คุมที่เป็นหมาล่าเนื้ออีกทีอะนะ…"

"ไม่อยากจะเชื่อเลยว่าตัวเองจะคิดแบบนั้น แล้วยังพูดออกมาอีก คงต้องอยู่ให้ห่างจากเคนจิแล้วละ"

hi "…ช่างเถอะ เอาละ ไปห้องสมุดกันเลยไหม"

show hanako basic_smile
with charachange

ha "อะ-อื้ม"

play ambient sfx_crowd_indoors fadein 0.5

scene bg school_hallway3
show crowd
with locationchange

"ฮานาโกะเดินตามฉันผ่านโถงทางเดินคนที่ยังคงแน่นไปยังห้องสมุดโดยใช้ฉันเป็นโล่กำบัง"

stop ambient fadeout 0.5
play music music_happiness fadein 2.0

scene bg school_library
show hanako invis at offscreenright
show yuuko neutral_down at center
with locationchange

show hanako basic_worry at tworight
with dissolvecharamove

"ทันทีที่เดินเข้าประตูมา ฮานาโกะก็พุ่งตัวไปยังเคาน์เตอร์ที่ยูโกะกำลังกองหนังสืออยู่"

show hanako emb_emb
with charachange

"ฮานาโกะก็กระซิบบางอย่างให้ยูโกะฟังก่อนฉันจะตามไปได้ทัน"

show yuuko neurotic_up
with charachange

yu "เอ่อ น่าจะอยู่ที่หมวดสารคดีนะ แต่ฉันไม่รู้ว่าอยู่ตรงไหน ถ้าจะให้ช่วยหาก็ได้นะ…"

show hanako emb_downsad
with charachange

ha "มะ-ไม่เป็นไรค่ะ"

hi "คุณยูโกะ มีอะไรเหรอครับ"

show yuuko neutral_down
with charachange

yu "อ้าว ฮิซาโอะ… ฮานาโกะแค่จะมาหาหนังสือเรื่อง…"

show hanako emb_blushing
with charachange

ha "ปะ-เปล่า…"

hi "หนังสือเรื่องความว่างเปล่าเหรอ ที่อยู่หมวดสารคดีอะนะ"

show hanako def_strain
with charachange

ha "ฉะ… ฉันแค่จะ…"

show yuuko neurotic_up
with charachange

"ฉันชำเลืองมองยูโกะที่สภาพเหมือนตัวจะระเบิดจากแรงกดดันที่ต้องเก็บความลับเรื่องที่ฮานาโกะขอ"

hi "คุณยูโกะ เกิดอะไร…"

show yuuko happy_down
with charachange

yu "หมากรุกน่ะ! เธอมาหาหนังสือหมากรุกน่ะ!"

"ฉันจะจำไว้เลยว่าจะไม่มีวันฝากความลับสำคัญอะไรไว้กับยูโกะเด็ดขาด"

show hanako defarms_shock
with charachange

ha "คะ-คุณยูโกะ…"

show yuuko panic_up
with charachange

yu "ขอโทษทีนะฮานาโกะ… ฉันเผลอพูดไปน่ะ…"

hi "เอาเถอะ ยังไงก็ไม่ใช่ความลับอีกแล้วละ มา เดี๋ยวฉันช่วย ฉันเองก็ว่าจะลับฝีมือด้วยเหมือนกัน"

show hanako def_worry
with charachange

ha "อะ… โอเค"

hide yuuko
with charaexit

show hanako def_worry at center
show bg school_library at bgleft
with charamove

"ยูโกะหายไปหลังเคาน์เตอร์ด้วยความอับอาย ขณะที่ฮานาโกะกับฉันเดินเข้าไปในหมวดสารคดีอันยืดยาว"

"ก็รู้อยู่หรอกว่ามันมีระบบจัดหมวดหมู่หนังสืออยู่ แต่ฉันก็คิดว่าถ้าไม่ได้ทุ่มเทอยู่กับเรื่องนี้ตลอดชีวิตเลยก็แทบจะ\nเป็นไปไม่ได้ที่จะจำรหัสแล้วแยกแยะออก"

"งี้ละมั้งบรรณารักษ์แต่ละคนที่ฉันรู้จักถึงเป็นประสาทกันทั้งนั้น"

#Dewey Decimal for Chess is 794.1, between magic tricks and educational games.

"ตอนท้ายสุดของชั้นหนังสือ ตรงระหว่างหนังสือเกี่ยวกับกลไพ่กับหนังสือเกมสำหรับเด็ก มีหนังสือเล่มหนึ่งตั้งอยู่\nโดดเด่น ชื่อว่า “{i}กลยุทธ์หมากรุกสำหรับแชมเปี้ยน{/i}” (Chess Tactics for Champions)"

show hanako basic_bashful
with charachange

"ยังไม่ทันที่ฉันจะเอื้อมมือไป ฮานาโกะก็คว้าหนังสือเล่มนั้นไว้แล้วกอดไว้กับหน้าอกของเธอ"

hi "อืม งั้นก็คงเป็นของเธอแล้วละนะ ถ้าอ่านจบแล้วขอยืมต่อได้ไหม"

show hanako cover_worry
with charachange

ha "ดะ-ได้สิ ฉัน… ก่อนหน้านี้ฉันไม่เคยเล่นกับใครเลย นะ…นอกจากลิลลี่ ก็เลยว่าจะ…"

"ตายละ ไม่ใช่ว่าจะตั้งใจเอาชนะฮานาโกะหรอก แต่ดูเหมือนเธอจะเก็บไปคิดมากซะแล้วสิ"

"แต่ก็นะ แปลว่าเธอเองก็อยากเล่นกันฉันอีกรอบ ซึ่งก็เป็นเรื่องที่ดี ใช่ไหมล่ะ"

hi "อ่า ก็ใช่ว่าฉันจะเก่งหรืออะไรหรอกน่า ฉันก็แค่เคยเล่นมานิดหน่อยเอง…"

"แล้วก็เพิ่งนึกได้ว่ายังไม่ได้บอกฮานาโกะเรื่องอาการของฉัน ฉันชะงักไปแป๊บนึงก่อนตัดสินใจที่จะปิดเรื่องนี้ไว้\nคุยกันวันหลัง"

hi "…ก่อนที่จะมาที่นี่น่ะ"

stop music fadeout 6.0

show hanako cover_distant
with charachange

#To be replaced with "concern" if it gets made.

ha "มะ… มีอะไรหรือเปล่า"

hi "เอ้อ พอดีนึกอะไรขึ้นมาได้น่ะ…"

"พอมาคิดดูแล้ว ฉันก็ไม่ควรกลัวที่จะบอกฮานาโกะเรื่องอาการของฉันและเรื่องที่ฉันเคยอยู่ในโรงพยาบาลเลย\nดูจากรอยแผลเป็นของเธอก็พอเดาได้ว่าเธอเองก็น่าจะเคยอยู่บนเตียงโรงพยาบาลมานานพอตัวเหมือนกัน"

"แต่ด้วยเหตุผลอะไรบางอย่าง ฉันก็ไม่กล้าเอามาคุยเลย อย่างน้อยก็ไม่ใช่วันนี้ ไม่ใช่เร็ว ๆ นี้แน่ ๆ"

"ด้วยความอยากตัดบทสนทนานี้ลง ฉันเลยคว้าหนังสือแบบสุ่ม ๆ จากชั้นวางมาเล่มหนึ่ง"

#791.068 – Amusement parks

"เป็นหนังสือเกี่ยวกับรถไฟเหาะที่เร็วที่สุดในโลก…"

"…เผยแพร่ในปี 1982 ก็ไม่ค่อยทันสมัยหรอก แต่อย่างน้อยก็น่าสนใจ"

hi "เอาละ ได้หนังสือกันทั้งคู่แล้ว ไปนั่งกันไหม"

show hanako cover_bashful
with charachange

"ดูเหมือนฮานาโกะจะเชื่อที่ฉันกลบเกลื่อน เรามุ่งหน้าไปที่มุมอ่านหนังสือด้านหลังห้องสมุด"

hide hanako
with charaexit

"พวกเราไม่มีใครพูดอะไร แค่นั่งเปิดหนังสืออ่านกันเท่านั้น"

"ฉันพยายามอ่านของฉัน แต่ดูเหมือนว่ารถไฟเหาะปี 1982 นั้นไม่ใหญ่เท่าอันที่ผลิตไม่กี่สิบปีก่อน"

"ที่อยู่ในเล่มนี้ส่วนใหญ่จะเป็นแบบที่ทำจากไม้ ซึ่งฉันว่าดูไม่ค่อยปลอดภัยเท่าไหร่"

"ถ้าจะต้องขี่อะไรที่อันตราย ๆ ก็อยากให้มันทำจากเหล็กกล้าหรือโลหะผสมยุคอวกาศที่มีคำเท่ ๆ อย่าง “ไทเทเนียม”\nหรือ “รูทีเนียม” ไปเลย"

"ไม่นานก็เบื่อจะอ่าน สายตาฉันเลื่อนไปมองฮานาโกะที่กำลังนั่งอ่านหนังสืออย่างตั้งใจ"

show ev hana_library_read_std:
    truecenter zoom 1.0 subpixel True
    easein 20.0 zoom 1.05
with locationskip

"ดูเหมือนว่าฮานาโกะจะจมจ่อมอยู่กับหนังสือของเธอ เธอกวาดสายตามองกลับไปกลับมาเหมือนกำลังทบทวน\nสิ่งที่เพิ่งอ่านไป"

"จะได้ผลจริงหรือเปล่านะ หรือยิ่งทำแล้วยิ่งปวดหัวกันแน่ละเนี่ย"

"เธอปัดผมบนหน้าเธอไปมาอย่างเหม่อลอย เผยให้เห็นเนื้อเยื่อแผลเป็นแวบ ๆ"

"ฉันยังคงไม่ค่อยแน่ใจเรื่องกติกามารยาทของที่นี่ เช่นว่าผิดไหมที่จะถามเรื่องรอยแผลเป็นของเธอ เรื่องในอดีตของเธอ\nเรื่องว่าอยู่ในโรงพยาบาลมานานแค่ไหน ต้องไปหาหมออยู่ไหม"

"หรือถ้าจะให้พูดแบบคนทั่วไปก็คือ คำถามพวกนี้เหมือนเป็นพวกที่เอาไว้ถามคนที่เพิ่งย้ายเข้ามาในโรงเรียนนั่นแหละ"

"แต่จนถึงทุกวันนี้ ก็ไม่เคยมีใครมาถามฉันแบบตรง ๆ สักที ก็นะ ยกเว้นรินไว้คนนึง แต่รินน่าจะไม่ใช่คนที่จะเอาไว้\nอ้างอิงเรื่องการอยู่ร่วมกับคนในสังคมได้เท่าไหร่"

"ตอนนี้ยังไม่ถามอะไรน่าดีกว่า ถ้าอยากบอกเดี๋ยวก็คงเล่าให้ฟังเองนั่นแหละ ยิ่งบีบคั้นฮานาโกะให้เล่าก็รังแต่ทำให้\nจะกลับไปเก็บตัวอีก"

scene bg school_library_ss
show yuuko worried_up_ss at center
with shorttimeskip

yu "เอ่อ… ขอโทษที่รบกวนนะ แต่ฉันต้องปิดห้องสมุดแล้วน่ะ"

play music music_tranquil fadein 3.0

hi "ปิดแล้วเหรอครับ"

"ฉันมองดูนาฬิกาข้อมือ ไม่รู้ตัวเลยว่าเวลาผ่านไปเกือบสองชั่วโมงระหว่างเหม่อลอยอยู่"

show yuuko smile_down_ss
with charachange

yu "จะยืมหนังสือพวกนั้นไหม ฉันจัดการให้ก่อนออกได้นะ…"

show hanako invis:
    xpos 0.9 xanchor 0.5 ypos 1.17 yanchor 1.0
with None

show hanako basic_worry_ss:
    xpos 0.7
show bg school_library_ss at bgleft
show yuuko smile_down_ss at twoleft
with dissolvecharamove

ha "ระ-รบกวนด้วยค่ะ"

hi "ของผมไม่ต้องครับ เดี๋ยวเอาไปคืนตอนเดินกลับแล้วกัน พอดีอ่านแล้วไม่ค่อยน่าสนใจเท่าที่คิดน่ะครับ"

show hanako emb_timid_ss at tworight
with dissolvecharamove

"ฮานาโกะใช้กระดาษคั่นหนังสือไว้แล้วลุกขึ้นยืน พวกผู้หญิงมุ่งหน้าไปที่เคาน์เตอร์ และฉันก็นำหนังสือของฉันไปคืนที่ชั้น\nที่ฉันคิดว่าน่าจะใช่"

show yuuko neurotic_up_ss
with charachange

"ยูโกะสแกนหนังสือของฮานาโกะอย่างคล่องแคล่วและแม่นยำ แต่ก็ยังมีพลาดอยู่"

show yuuko neutral_down_ss
with charachange

yu "อ่า… ได้สักที กว่าจะติด พอดีว่าเล่มนี้เป็นหมวดสารคดี เพราะงั้นยืมได้แค่สัปดาห์เดียวนะ"

show hanako basic_smile_ss
with charachange

ha "มะ-ไม่เป็นไรค่ะ"

scene bg school_hallway2
with locationchange

"ยูโกะปิดคอมพิวเตอร์ห้องสมุดและพาเราออกมา"

show yuuko panic_up at twoleft
show hanako def_worry at tworight
with charaenter

yu "อ๊าก! ไม่คิดว่าจะเวลาป่านนี้แล้ว…!"

hi "แต่คุณบอกเราเองว่าจะต้องปิดนี่ครับ…"

show yuuko worried_up
with charachange

yu "ก็ใช่แหละ แต่ว่า นั่นน่ะเป็นตอนก่อนที่ฉันจะได้ดูเวลาน่ะ!"

show yuuko neurotic_up
with charachange

yu "ไว้เจอกันนะ"

hide yuuko
with easeoutleft

"ยูโกะรีบวิ่งลงไปที่โถงใหญ่โดยมีกระเป๋าถือที่ปลิวไสวเหมือนธงที่โบกหย็อย ๆ ไล่หลังไป"

show hanako def_worry at center
show bg school_hallway2 at bgleft
with dissolvecharamove

hi "ฉันว่าบรรณารักษ์ทุกคนต้องเป็นโรคประสาทแหง ๆ"

show hanako emb_timid
with charachange

ha "ฮะ?"

hi "อ่า ช่างเถอะ แค่คิดว่ายังไม่เคยเจอบรรณารักษ์คนไหนที่จัดการเวลาได้ดีเลย ถึงจะจัดหนังสือเก่งแค่ไหนก็เถอะ"

show hanako basic_smile
with charachange

ha "อ๋อ… ฉันขะ… เข้าใจสิ่งที่นายจะสื่อแล้ว…"

"ฮานาโกะยิ้มขบขัน จริง ๆ ไม่ได้ตั้งใจจะให้เป็นเรื่องตลกหรอก แต่ฉันคงทำให้เธอนึกถึงบรรณารักษ์คนอื่น…\nหรือสักอย่างนี่แหละ…"

show hanako cover_worry
with charachange

ha "ฉะ… ฉันต้องไปแล้ว"

hi "อื้ม ฉันก็ด้วย ไม่ยักรู้ตัวเลยว่าเวลาป่านนี้แล้ว ขอบใจนะที่ให้มาอยู่ด้วยน่ะ"

show hanako basic_bashful
with charachange

ha "มะ-ไม่มีปัญหา"

hi "ฉันก็จะกลับหอแล้วเหมือนกัน ขอเดินไปด้วยได้ไหม"

show hanako emb_blushing
with charachange

ha "อะ-โอเค"

hide hanako
with charaexit

"ฮานาโกะเดินนำหน้าฉันไปก่อน และฉันต้องวิ่งเหยาะ ๆ เพื่อที่จะตามเธอให้ทัน"

scene bg school_dormext_full_ss
with locationchange

show hanako def_worry_ss at center
with charaenter

"พวกเราเดินผ่านสวน และในที่สุดก็มาถึงที่หน้าหอพัก"

hi "โอย เธอนี่เดินเร็วจริง ๆ นี่ขนาดฉันเคยอยู่ชมรมเตะบอลนะเนี่ย แต่เธอก็ยังเดินเร็วกว่าฉันได้"

stop music fadeout 6.0

show hanako emb_downsmile_ss at center
with charaenter

"ฉันว่าฉันไม่น่าพูดแบบนั้นเลย จริง ๆ เป็นเพราะโรคนี้มาทำให้ฉันสุขภาพแย่ ไม่ใช่เพราะความเร็วของเธอเลยด้วยซ้ำ"

"ปฏิกิริยาของฮานาโกะต่างออกไปจากเดิม ฉันคิดว่าเธอคงพยายามปฏิเสธเรื่องที่เดินเร็ว แต่ก็ได้แต่ยืนหน้าแดงพร้อม\nจ้องไปที่เท้าของเธอและยื้ม"

"ความเงียบเข้าแทรกมาระหว่างเรา ซึ่งเป็นเรื่องปกติเมื่ออยู่กับฮานาโกะ แต่ครั้งนี้รู้สึกต่างออกไปนิดหน่อย\nหลังผ่านไปไม่นานฉันจึงทำลายความเงียบลง"

hi "เอาละ ไว้เจอกันพรุ่งนี้ที่ห้องเรียนนะ"

show hanako emb_smile_ss
with charachange

ha "อะ-อื้ม"

hide hanako
with charaexit

"ฮานาโกะโบกมือให้เล็กน้อยก่อนที่จะเข้าประตูหอไป ฉันยืนจ้องประตูพักหนึ่งก่อนที่จะกลับไปหอของฉัน"

scene black
with dissolve

#-------------------------------

label th_H6:

scene bg school_dormhisao
with locationchange

"สกุณาร่าร้อง"

"ปกติแล้ว ตอนนี้นั้นเป็นเวลาเหมาะที่จะได้รับบรรยากาศอันสวยงามของหมู่ธรรมชาติ"

"แต่นี่มันเพิ่งจะหกโมงเช้า"

play sound sfx_pillow

scene black
with Dissolve(0.2)

"ฉันเอาหมอนมาคลุมหัวคว่ำหน้าทุบลงกับที่นอนเพื่อหวังว่าแรงกระแทกจะทำให้ฉันหลับต่อไปได้"

"เปล่าประโยชน์"

"พลิกตัวจนแทบจะเป็นปลาหมึกย่างไม้ละยี่สิบแล้ว แต่ก็นอนไม่หลับอยู่ดี"

play music music_daily fadein 10.0

scene bg school_dormhisao
with locationchange

"ก็ได้เหล่าธรรมชาติ แกชนะแล้ว ดูซะ ฉันจะลุกแล้ว…"

"การนอนน้อยทำให้สมองของฉันหนักอึ้ง มีทางเดียวที่จะช่วยได้ คือการได้กินอาหารเช้าดี ๆ"

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 0.5

scene bg school_cafeteria
with locationchange

"ได้มาเป็นคนแรกนี่น่าจะดี"

"เป็นคนแรกที่ได้ตักกินแกงร้อน ๆ จากถาด นั่งตรงไหนก็ได้ที่อยากนั่ง…"

"คงจะดีมาก ๆ เลยละ"

"แต่เช้าตรู่ของฉันยังช้ากว่าเช้าของนักเรียนขยันโดยทั่วไปอยู่"

"ที่นี่ก็คงพอจะมีคนที่ตื่นแต่เช้าอยู่บ้างละนะ ด้วยเหตุผลบางประการ"

"กลุ่มนักเรียนที่ใส่ชุดกีฬาล้อมวงอยู่รอบโต๊ะตัวหนึ่งกำลังปรึกษาแผนการเล่นกันอย่างตั้งใจพลางสวาปามอาหารคำโต\nไปด้วย"

"นักเรียนที่ขอบตาโหลนั่งกระจัดกระจายอยู่ตามโรงอาหาร คงจะอยู่สภาพอย่างนั้นด้วยเหตุผลเดียวกับฉัน\nคือรำคาญนกร้อง"

"และแน่นอนว่าก็มีคนที่อภิรมย์กับการตื่นเช้าขนาดนี้เช่นกัน เป็นพวกที่กระเป๋าเต็มไปด้วยตำราเรียนและการบ้าน\nที่ทำเสร็จแล้ว"

"ซึ่งไม่ใช่เรื่องง่ายเลยที่จะไม่เหม็นขี้หน้าคนแบบนั้น โดยเฉพาะยิ่งถ้าเหนื่อย ๆ มาด้วย"

"หลังจากเจอคนหน้าคุ้นท่ามกลางฝูงชนบางตา ฉันก็เดินตรงไปยังโต๊ะที่ใกล้ที่สุด"

"ลิลลี่นั่งอยู่คนเดียว เธอกำลังใช้ส้อมแตะไปตามจานที่มีไข่ทอดวางอยู่อย่างเบามือ"

"รู้สึกผิดนิดหน่อยแฮะที่ต้องไปขัดจังหวะการเคลื่อนไหวที่ดูเป็นระบบอย่างนั้น"

"คนตาบอดเขาเหม่อลอยกันแบบนี้หรือเปล่านะ แค่เคลื่อนไหวไปตามรูปแบบที่เรียนรู้มาหลายปี เหมือนคนปกติ\nเวลาจะกินบางอย่างตอนกำลังอ่านหนังสือพิมพ์"

hi "อรุณสวัสดิ์ลิลลี่ มาเช้าจังเลยนะ"

show lilly basic_surprised:
    center
    ypos 1.2
with charaenter

li "อ้าวฮิซาโอะ ตกใจหมดเลย ไม่ยักรู้ว่าเธอทานมื้อเช้าเช้าขนาดนี้"

hi "ปกติก็ไม่หรอก แต่รอบนี้ไม่ปกติน่ะ ส่วนใหญ่ฉันอยากมาสายมากกว่าตื่นเช้ามากินข้าวเช้าน่ะ"

show lilly basic_weaksmile
with charachange

"ลิลลี่ถอนหายใจเบา ๆ กับการยอมรับว่าอยากมาสายตอนฉันกำลังเริ่มตักข้าวกิน"

"ซึ่งผ่านไปไม่นานเธอก็กลับไปละเลียดกินแบบเหม่อลอยเหมือนเดิม"

"การเคลื่อนไหวแต่ละครั้งดูไร้เรี่ยวแรง ฉันว่าคงคล้ายกับเวลาที่เราปล่อยตาเหม่อลอย ขณะที่กำลังทำงานบ้านทั่ว ๆ ไป\nนั่นแหละ"

"แต่พอคลำทางกินไปอีกสักสองสามรอบเธอก็วางส้อมลงและเช็ดปากเธอด้วยผ้าเช็ดหน้า"

stop music fadeout 6.0
stop ambient fadeout 6.0

show lilly basic_concerned
with charachange

li "ฮิซาโอะ ขอถามอะไรหน่อยได้ไหม"

"แหม่ สิ่งที่ฉันอยากได้ตอนนี้คือข้าวกับเวลานอนอีกสี่ชั่วโมง ไม่ใช่คนที่จะมาถามว่า “ขอถามอะไรหน่อยได้ไหม”\nที่จะตามด้วยคำถามพื้น ๆ"

hi "ได้สิ"

show lilly basic_listen
with charachange

li "เธอคิดว่าฮานาโกะเป็นเพื่อนหรือเปล่า"

"หืม เหมือนจะต้องมีอะไรถามต่ออีกแน่ ๆ"

hi "ก็… คงงั้นแหละ ถามทำไมเหรอ"

show lilly basic_weaksmile
with charachange

li "ก็ไม่ได้มีเหตุผลหรอกจ้ะ"

show lilly basic_displeased
with charachange

play music music_serene fadein 8.0

li "แต่ฉันขอถามอีกอย่าง ทำไมเธอถึงคิดว่าฮานาโกะเป็นเพื่อนล่ะ"

"อันนี้เหนือกว่าที่คาดละ ที่ถามนี่จะเอายังไงกันแน่"

hi "ไม่ค่อยแน่ใจเหมือนกันแฮะ น่าจะเพราะเธอรับมือกับผู้คนไม่เหมือนชาวบ้านละมั้ง…"

show lilly basic_reminisce
with charachange

li "อืมม ตั้งแต่ที่ฉันรู้จักเธอมา เธอแทบไม่สนิทกับใครเลย"

show lilly basic_concerned
with charachange

li "เธอดูจะไม่สนใจคนอื่นด้วยซ้ำ และฉันว่าคนอื่น ๆ ก็คงกลัวรูปลักษณ์ของเธอเหมือนกัน"

hi "จริงอะ ฉันนึกว่าเรื่องแบบนั้นเขา เอ่อ ไม่ส่งเสริมกันเสียอีก แบบว่าห้ามเหยียดหรืออะไรอย่างนั้น"

show lilly basic_listen
with charachange

li "อืมม ถ้าจะให้ฉันพูดละก็…"

"เธอขมวดคิ้วครุ่นคิด ท่าทีนั้นทำให้ฉันรู้สึกกังวลเล็กน้อยว่าเธอกำลังเลือกเรื่องอะไรขึ้นมาจากสมอง"

show lilly basic_weaksmile
with charachange

li "ฉันว่าเธอใสซื่อไปหน่อยนะ"

"ใสซื่อ? ถ้าไม่ใช่เพราะรอยยิ้มเยาะหยันเล็กน้อยที่ปรากฏบนใบหน้าของเธอนี่ฉันคงโกรธไปแล้ว"

hi "งั้น… เหรอ"

show lilly basic_reminisce
with charachange

li "ถึงยามากุจะมีความเป็นชุมชนที่แข็งแกร่งกว่าโรงเรียนอื่น แต่ก็ยังห่างไกลจากคำว่าปราศจากความขัดแย้งอยู่ดี"

show lilly basic_displeased
with charachange

li "กฎน่ะขจัดนิสัยธรรมชาติของมนุษย์ไม่ได้หรอก ทำได้เพียงแค่กดมันไว้เท่านั้น"

"จริง ๆ ฉันเองก็พอสังเกตมาบ้างแล้วละ"

"แบบเรื่องเล็ก ๆ น้อย ๆ อย่างการที่คนบางกลุ่มหรือกลุ่มเพื่อนหลบหน้ากันในโถงทางเดิน จริง ๆ แล้วก็ไม่ต่างจาก\nโรงเรียนเก่าของฉันเท่าไหร่"

"แม้แต่ลิลลี่กับชิซูเนะที่ดูเหมือนจะเป็นคนเปิดกว้างทั้งคู่ ก็ยังเป็นคู่ที่ตีกันตายได้เลย"

"ก็ อย่างน้อยก็เป็นชิซูเนะในแบบฉบับที่ผ่านมิช่าอะนะ ใครจะรู้ว่าเบื้องหลังภาษามือและแว่นตาของเธอนั้นมีอะไรอยู่\nกันแน่"

hi "ฉันว่าเธอพูดถูก แต่ตอนที่ฉันมาที่นี่ครั้งแรกก็อึ้งกับอะไรหลายอย่างเหมือนกัน"

hi "ฉันทำพลาดอยู่บ่อย ๆ อาจจะไม่พลาดจริงหรอก แต่อย่างน้อยฉันก็คิดว่าพลาดนั่นแหละ อย่างตอนที่ฉันเจอเธอ\nครั้งแรกแล้วฉันพูดออกไปว่า “พอจะเห็นภาพ” ใส่เธอน่ะ"

hi "ฉันไม่รู้ว่าจะเสียมารยาทหรือเปล่าก็เลยทำลืม ๆ ไม่สนใจไปเลย พวกเรื่องที่ว่าต้องระวังตัวเป็นพิเศษเวลาอยู่กับ\nแต่ละคนอะไรทำนองนั้นน่ะ"

hi "ก็เลยทำตัวปกติ ฉันบอกตัวเองเสมอว่าฮานาโกะและเธอรวมถึงคนอื่น ๆ ก็เป็นคนปกติทั่วไป และพยายามมองข้าม\nอะไรที่เห็นอยู่ตำตา"

hi "ฉันคุยกับฮานาโกะเหมือนกับที่ฉันคุยกับคนอื่น ๆ พวกเราก็เลยเป็นเพื่อนกันน่ะ"

hi "ฉันว่าน่าจะเพราะอย่างนั้นแหละ"

hi "แต่ก็นะ ฉันก็รู้สึกผิดแหละที่พูดแบบนั้น เหมือนฉันต้องตั้งหลักไว้ก่อนตลอดเลยว่าฮานาโกะ หรือเธอ หรือคนอื่น ๆ\nเป็นคนปกติ ซึ่งฉันคิดว่ามันไม่ถูกต้องน่ะ"

show lilly basic_smileclosed
with charachange

li "ฮิซาโอะ ฉันว่าเธอใสซื่อก็จริง แต่ฉันก็คิดว่าเธอเป็นคนดีนะ อาจจะเป็นหนึ่งในข้อดีของเธอเลย"

hi "ฉัน… จะถือว่านั่น… เป็นคำชมก็แล้วกันนะ…"

show lilly basic_smile
with charachange

li "บอกหน่อยสิ คืนนี้เธอว่างหรือเปล่า"

hi "ถ้าไม่นับเรื่องการบ้าน ก็ว่างพอตัวเลยละ"

show lilly basic_cheerful
with charachange

li "ถ้างั้นแล้ว เธอจะมาร่วมดื่มชากับฉันและฮานาโกะไหม"

hi "เอ้อ ตอนนี้ฉันไม่ค่อยจะมีเงินน่ะ เพราะงั้นแล้วจะให้ไปข้างนอกก็คง…"

show lilly basic_smile
with charachange

li "อ๋อ ไม่ได้หมายถึงไปข้างนอกน่ะ หมายถึงที่นี่ เย็นนี้แหละ"

hi "เธอเข้าห้องเรียนตอนเย็นได้ด้วยเหรอ"

show lilly basic_giggle
with charachange

li "เปล่า ไม่ได้หมายความว่าอย่างนั้นจ้ะ ฮานาโกะกับฉันจัดงานเลี้ยงน้ำชาด้วยกันบ่อย ๆ ในห้องฉันน่ะ ค่ำ ๆ แล้วมาได้\nเลยนะ"

hi "เอาสิ ไม่มีปัญหา แล้วห้องเธอเลขอะไรล่ะ"

show lilly basic_smileclosed
with charachange

li "225 ห้อง 25 ชั้น 2 จ้ะ"

hi "โอเค ได้เลย"

show lilly basic_weaksmile
with charachange

li "ถ้างั้น ฉันต้องรีบไปแล้วละ ฉันมีงานในฐานะหัวหน้าห้องที่ต้องทำต่อน่ะจ้ะ"

show lilly basic_cheerful at center
with dissolvecharamove

li "เจอกันเย็นนี้นะ ฮิซาโอะ"

hi "อื้ม เจอกัน"

hide lilly
with charaexit

stop music fadeout 8.0

"เดี๋ยวนะ… เมื่อกี้ฉันได้รับเชิญให้ไปที่ห้องของสาว ๆ หลังเลิกเรียนเหรอ ทำได้ด้วยเหรอ"

"คือก็มีเรื่องเวลาปิดประตูหอแหละ แต่ก็ไม่เคยได้ยินกฎเรื่องแขกมาเยี่ยมในห้องเลยอะนะ"

"ถึงอย่างนั้นก็เถอะ แค่นี้ก็เพียงพอแล้วที่จะทำให้สมองที่พักผ่อนไม่เพียงพอของฉันเริ่มทำงานได้อย่างรวดเร็ว"

"พอมาเจอกับอาหารเช้าอุ่น ๆ เลยกลายเป็นตัวกระตุ้นชั้นดีเลย"

scene bg school_scienceroom
with locationskip

"ฉันไปเข้าเรียนอย่างไม่ค่อยเต็มใจ แต่ยังรู้สึกตื่นเต้นที่จะได้ทำบางอย่างที่อาจผิดกฎโรงเรียน"

"รู้สึกเหมือนเด็กน้อยที่วางแผนหนีออกทางหน้าต่างเพื่อไปเที่ยวตอนกลางคืนเลย"

"ก็ อาจจะฟังดูเกินไปหน่อย แต่เมื่อเปรียบเทียบการได้รับเชิญไปงานเลี้ยงกับการนั่งฟังบรรยายหกชั่วโมง ฉันรู้เลยว่า\nอะไรน่าสนใจกว่ากัน"

"มิช่ากับชิซูเนะก็ไม่ได้ช่วยให้หายเบื่อได้เลย เป็นครั้งแรกที่ดูเหมือนว่าพวกเธอตั้งใจจะทำงานที่ครูมุโต้สั่งให้เสร็จ\nจริง ๆ"

scene bg school_scienceroom_ss
with shorttimeskip

play sound sfx_normalbell

"อย่างไรก็ตาม วันนี้ก็ได้ผ่านไป"

scene bg school_dormhisao_ss
with locationskip

"ฉันรีบกลับมาที่ห้องฉันเพื่ออาบน้ำหวีผม โชคดีจริง ๆ ที่ไม่มาเจอเคนจิ"

scene bg school_dormext_full_ss
with locationchange

"และจากนั้นไม่นานฉันก็เดินออกมาจากหอชาย"

#---------------------------------

label th_H7:

scene bg school_girlsdormhall
with locationskip

play sound sfx_doorknock2

"ฉันเคาะประตูหมายเลข 225 ด้วยความประหม่าพร้อมเหลือบมองนาฬิกาอีกครั้ง"

li "นั่นเธอหรือเปล่าฮิซาโอะ ประตูไม่ได้ล็อก เข้ามาได้เลยจ้ะ"

"เสียงของลิลลี่ที่ดังแว่วผ่านประตูช่วยลดความประหม่าของฉันได้อย่างดี"

"เป็นครั้งแรกเลยที่ถูกเชิญมาห้องสาว ๆ ตอนค่ำเนี่ย"

"ถึงแม้จะรู้ว่าคำเชิญนี้ไม่มีเจตนาแอบแฝง แต่ก็หยุดความคิดที่เตลิดของฉันไม่ได้"

"ชายหนึ่งหญิงสอง ในห้องพัก พร้อมชุดชา"

"พอพูดแบบนั้นแล้วก็ฟังดูสองแง่สองง่ามหน่อย ๆ แฮะ"

"ฉันถอนหายใจเบา ๆ เพื่อเรียกสติ จากนั้นค่อย ๆ วางมือลงบนลูกบิดประตูแล้วเปิดออก พร้อมกับยื่นหน้าเข้าไป\nมองข้างในอย่างระมัดระวัง"

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

"ประตูเปิดออกจนสุด และฉันก็มองเห็นห้องของลิลลี่เป็นครั้งแรก"

"เฟอร์นิเจอร์ของเธอส่วนใหญ่ดูเป็นแบบเก่า แต่ผนังกับพื้นนั้นเรียบไร้การตกแต่งใด ๆ ตรงกลางห้องมีโต๊ะเตี้ย ๆ วางอยู่\nฉันเห็นชุดน้ำชาเล็ก ๆ วางอยู่ตรงนั้น"

"ดูเหมือนกับของทุกอย่างในนี้มีที่เป็นของตัวเอง จะเว้นก็เพียงแต่หนังสือหลายกองที่วางซ้อนกันอยู่ชิดผนัง"

"การรับรู้ของฉันไม่ได้ถูกกระตุ้นแค่ทางสายตาเท่านั้น แต่ยังมีกลิ่นบางอย่างที่อ่อน ๆ ลอยอยู่ในอากาศ กลิ่นน้ำยาทาเล็บ\nน้ำหอม เครื่องสำอาง… ยากจะหาคำใดมาอธิบายนอกจากคำว่า “ผู้หญิ๊ง ผู้หญิง”"

"ฉันกวาดตามองไปรอบ ๆ ห้องจนทั่ว ก่อนจะหันกลับไปมองสาว ๆ อีกครั้ง"

scene ev lilly_bedroom_large:
    xpos -130 ypos -400 subpixel True
    acdc_warp 4.0 ypos -600
with flash

"ลิลลี่นั่งอยู่ข้างโต๊ะตัวเล็ก ใส่ชุดนอนสีน้ำเงินเข้ม กางเกงขาสั้นสีน้ำเงินเข้มเผยให้เห็นเรียวขาขาวอันเย้ายวนของเธอ"

show ev lilly_bedroom_large:
    ease 1.0 ypos -300 xpos -830
    acdc_warp 12.0 ypos 0 xpos -830
with None

"ฮานาโกะนั่งสวมชุดราตรีสีชมพูอ่อนแบบเรียบร้อยอยู่ตรงหน้าเธอ"

"เธอนั่งวางมือนิ่งไว้ที่ระหว่างขาเธอพลางโน้มไหล่ไปข้างหน้าและก้มหน้าลงราวกับพยายามซ่อนตัวเองเอาไว้ในชุด"

"ซึ่งถ้าจะซ่อนจริงก็คงไม่ยาก เพราะดูเหมือนว่าชุดจะใหญ่กว่าตัวเธอประมาณสองไซซ์"

"ผ้าสักหลาดเป็นลอนลากยาวลงมาจากร่างเธอ ทำให้เธอดูเหมือนเด็กที่กำลังเล่นแต่งตัวด้วยเสื้อผ้าของพ่อแม่"

"เธอมองขึ้นมาเพื่อยืนยันว่าเป็นฉัน และรอยยิ้มบาง ๆ ก็ปรากฏขึ้นบนใบหน้าของเธอ ก่อนจะหายไปอย่างรวดเร็วจนฉัน\nไม่แน่ใจว่าเมื่อกี้ได้ยิ้มจริง ๆ หรือเปล่า"

show ev lilly_bedroom_large:
    ease 1.0 xpos -130 ypos -400
with None

li "เอาแต่ยืนตรงประตูอย่างนั้นก็เมื่อยขาเปล่าจ้ะ ฮิซาโอะ"

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

"ฉันเดินเข้ามาในห้องแล้วปิดประตู"

show lilly basic_weaksmile_paj
with charachange

li "ตายจริง ห้องนี้คงเล็กไปสำหรับสามคนสิเนี่ย เธอนั่งก่อนไหม"

"ฉันค่อย ๆ เดินไปยังโต๊ะอย่างระมัดระวังไม่ให้ไปแตะอะไรเข้าแล้วนั่งลง"

"ฉันยังอดไม่ได้ที่จะเหลือบมองเข้าไปในเสื้อของลิลลี่อย่างรวดเร็วขณะที่ฉันกำลังหย่อนตัวลงนั่ง"

"การที่ถูกพรากการมองเห็นไปนั้นคงเป็นชะตากรรมที่โหดร้ายที่สุดแล้วละ"

show lilly basic_smileclosed_paj
with charachange

li "เอาละ เรามาดื่มชากันดีกว่า ฮานาโกะ เธอช่วยรินให้ทีได้ไหม"

show hanagown normal_blush
with charachange

ha "ดะ…ได้สิ ฮะ…ฮิซาโอะ… นาย…"

show hanagown distant_blush
with charachange

ha "…นายจะ…"

show hanagown worry_blush
with charachange

ha "…นายจะดื่ม…"

hi "ดื่มสิ ให้ช่วยไหม"

show hanagown normal_blush
with charachange

ha "มะ… ไม่ ไม่เป็นไร…"

show hanagown smile
with charachange

ha "ขอบคุณนะ…"

play music music_dreamy fadein 2.0

show lilly basic_giggle_paj
with charachange

"ลิลลี่อดไม่ได้ที่จะยิ้มกับความประหม่าของเพื่อน ซึ่งฉันก็ว่าไม่ได้หรอก"

show hanagown distant
with charachange

hi "วันนี้เหนื่อยไหม"

show hanagown smile
with charachange

ha "อะ… อื้ม"

show lilly basic_smileclosed_paj
with charachange

"ฉันนั่งเอนหลังอยู่ตรงหน้าตู้ที่อยู่อีกฟากโต๊ะ"

"ทางซ้ายคือลิลลี่ในชุดสีน้ำเงิน และทางด้านขวาคือฮานาโกะชุดสีชมพู"

show teaset:
     xalign 0.5 yanchor 0.5 ypos 0.6 alpha 1.0
     easein 0.5 ypos 0.5
with charaenter

"ชุดน้ำชาที่อยู่บนโต๊ะดูน่ารักและใช้งานได้ดี เป็นชุดสีแดงที่มีลายดอกไม้ประดับอยู่"

"ดูแปลกเมื่อเทียบกับเฟอร์นิเจอร์ของลิลลี่ที่ดูเรียบง่ายแต่โดยรวมแล้วดูหรูหรา ซึ่งทำให้ฉันคิดว่าฮานาโกะน่าจะเป็นคน\nเลือกมา"

"มีเสียง “ติ๊ง” เล็กน้อยเมื่อฮานาโกะเผลอไปเกี่ยวกาน้ำชาเข้ากับถ้วยขณะที่กำลังรินชา"

show hanagown worry
show lilly basic_displeased_paj
with None

show teaset:
    easeout 0.5 alpha 0.0 ypos 0.6
with Pause(0.5)

hide teaset
with None

"เธอหายใจเข้าดังเฮือก คงจะประหม่ามาก เพราะปกติไม่น่ามีใครจดจ่อกับอะไรแบบนี้"

show hanagown worry_blush
with charachange

"ฮานาโกะตัวสั่นกับความผิดพลาดของเธอ"

show lilly basic_weaksmile_paj
with charachange

li "ไม่เป็นไรหรอกฮานาโกะ ไม่ต้องกังวลขนาดนั้นหรอกจ้ะ"

show hanagown normal
with charachange

"ฮานาโกะดูจะได้รับความมั่นใจจากคำพูดที่แผ่วเบาแต่ปลอบโยนของลิลลี่และรินชาเพิ่มอีกสองถ้วยอย่างคล่องแคล่ว"

show hanagown normal_blush
with charachange

ha "อะนี่ ฮิซาโอะ… ลิลลี่"

"ฮานาโกะวางถ้วยและจานรองอย่างระมัดระวังตรงหน้าลิลลี่และฉัน ฉันน่าจะชินกับการบริการแบบนี้ได้ไม่ยาก"

show lilly basic_smile_paj
with charachange

li "ขอบคุณจ้ะฮานาโกะ"

hi "อื้ม ขอบใจ"

show hanagown smile
with charachange

ha "ดะ-ด้วยความยินดี"

show lilly basic_smileclosed_paj
with charachange

"ลิลลี่ควานหาแก้วของตัวเอง พอเจอแล้วก็จิบอย่างละเมียดละไม"

"ฉันเองก็จิบตาม รสชาติของชานี้รู้สึกว่าดีกว่าแบบที่ดื่มเป็นประจำที่โรงเรียน"

hi "อร่อยแฮะ รู้สึกว่าไม่เหมือนกับแบบที่เคยดื่มเลย…"

show lilly basic_ara_paj
show hanagown normal_blush
with charachange

li "เหมือนว่าเธอจะเลือกมาถูกนะฮานาโกะ"

show lilly basic_smileclosed_paj
with charachange

li "เก่งมากจ้ะที่กล้าเลือกมา"

show hanagown smile
with charachange

"ฮานาโกะกลับมายิ้มอีกครั้ง แต่คราวนี้ยิ้มกว้างกว่าเดิม"

"ถึงแม้หน้าจะมีรอยแผล แต่รอยยิ้มอาย ๆ ของเธอไม่มีคำใดจะเรียกได้ดีเท่าคำว่า “น่ารัก”"

show hanagown distant_blush
with charachange

ha "ชอบก็ดีแล้วละ…"

"ฮานาโกะที่ในที่สุดก็เริ่มผ่อนคลายจิบชาจากถ้วยของเธอ"

#--------------------
label th_H7a:

$ renpy.music.set_volume(0.5, 1.0, channel="music")
window hide
nvl clear
nvl show dissolve

n "พอนึกย้อนเรื่องที่คุยกับมิช่าเมื่อวันก่อน"

n "นิสัยของฮานาโกะตอนนี้นี่ควรเรียกว่าน่าเป็นห่วงจริง ๆ หรือเธอแค่ขี้อายกันแน่"

n "แล้วไหนจะเรื่องที่ลิลลี่พูดเมื่อเช้าอีก"

n "ทั้งคู่เป็นห่วงเธอจริง ๆ แน่นอน และพวกเธอเข้าใจสถานการณ์นี้ดีกว่าฉันเสียอีก"

n "แต่ก็นะ แล้วฉันจะช่วยยังไงได้บ้าง"

n "ฉันเองก็ไม่ใช่หมอศัลยกรรม เพราะงั้นแล้วก็ช่วยเรื่องรูปลักษณ์ไม่ได้แน่ ๆ แล้วก็ไม่ใช่จิตแพทย์ที่จะช่วยให้เธอ\nเข้าสังคมได้เช่นกัน"

n "แล้วลิลลี่กับมิช่าอยากให้ฉันทำอะไรกันแน่"

n "หงุดหงิดแฮะ ฮานาโกะกับฉันก็เป็นเพื่อนด้วยกันเองแท้ ๆ และพอเป็นแบบนั้น ทุก ๆ คนก็เหมือนอยากให้ฉัน\nมาแก้ปัญหาของเธอทั้งหมดซะงั้น"

n "และฉันก็ไม่รู้ด้วยซ้ำว่าต้องทำยังไง"

n "ในเมื่อไม่มีใครมาช่วยเรื่องหัวใจฉัน หรือสายตาลิลลี่ หรือแม้แต่อาการของสักคนในโรงเรียนนี้ได้ด้วยซ้ำ"

n "ยังไงก็เถอะ ฉันว่าการได้เป็นเพื่อนกับฮานาโกะให้มากขึ้นก็ไม่ใช่เรื่องเสียหายอะไร ตอนนี้เธอดูสบายใจกับฉันขึ้น\nเยอะ จนฉันก็สนุกที่ได้ใช้เวลาอยู่กับเธอเหมือนกัน"

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

n "\n\n\n\nพอเห็นอย่างนี้แล้วพานให้นึกถึงคำถามของลิลลี่เมื่อตอนกินข้าวเช้า"

n "ทำไมฉันถึงเป็นเพื่อนกับฮานาโกะงั้นเหรอ"

n "ลิลลี่เองก็ดูเป็นห่วงการเป็นอยู่ของฮานาโกะด้วย แต่ก็ใช่ว่าฉันจะช่วยอะไรเธอได้ซะหน่อย"

n "เท่าที่เห็นตอนนี้คือ แผลเป็นของเธอก็ไม่ได้ทำให้ร่างกายมีปัญหาอะไร และทุกคนที่ฉันเจอมาก็ดูจะรับมือกับความพิการ\nของตัวเองได้ในระดับหนึ่งเลย"

n "และที่ฉันอยู่กับฮานาโกะนี่ก็ไม่ได้มีเจตนาแอบแฝงอะไรหรอก ก็แค่ชอบอะไรคล้าย ๆ กันเฉย ๆ"

n "\nแค่นั้นก็พอแล้วนี่"

$ renpy.music.set_volume(1.0, 1.0, channel="music")
nvl clear
nvl hide dissolve
window show


#-----------------

label th_H7c:

show lilly basic_smile_paj
with charachange

li "ว่าแต่ ฮิซาโอะจ๊ะ เป็นไงบ้าง โอเคไหม"

"คำพูดลิลลี่ทำให้ฉันหลุดจากภวังค์ ฉันใช้เวลาสักพักเพื่อนึกว่าฉันอยู่ที่ไหน"

"ฉันอยู่ในห้องกับสองสาวในชุดนอน ถ้าถามว่าโอเคไหมก็โอเคมาก"

hi "อื้ม ก็ผ่อนคลายดี ราวกับว่าไม่ได้อยู่ในโรงเรียนเลยละ พวกเธอมานั่งดื่มที่นี่กันบ่อยมั้ย"

show lilly basic_weaksmile_paj
with charachange

li "ก็บ่อยพอตัว แต่ก็ไม่ได้บ่อยเท่าที่เราไปดื่มชาในอาคารเรียนหรอกจ้ะ"

"ไม่แปลกใจเท่าไหร่ เพราะพวกเธอดื่มชากันที่ห้องนั้นแทบทุกวัน"

"พอจะยกถ้วยชาขึ้นจิบอีกทีก็ถึงรู้ว่ามันหมดซะแล้ว"

hi "อร่อยมากเลย ขอบคุณนะฮานาโกะ ลิลลี่"

show hanagown smile
with charachange

ha "ด้วยความยินดี"

show lilly basic_smile_paj
with charachange

li "ด้วยความยินดีอย่างยิ่งจ้ะฮิซาโอะ ดีใจที่ได้มีคนที่สามในห้องด้วย"

hi "ก็ ถ้าอยากได้คนมาเติมตำแหน่งตรงนั้นฉันก็พร้อมเสมอ ว่างตลอด"

"ในสถานการณ์แบบนี้ ต้องมั่นใจว่าได้สื่อสารในสิ่งที่ต้องการจะพูดออกไปอย่างชัดเจน"

stop music fadeout 8.0
show lilly basic_sleepy_paj
with charachange

"ลิลลี่หาวเบา ๆ ซึ่งปกปิดด้วยมือไม่ทัน"

show lilly basic_weaksmile_paj
with charachange

li "ขอโทษทีนะ ฉันว่าฉันเหนื่อยนิดหน่อยน่ะ"

show hanagown distant
with charachange

ha "ฉันว่าทุกคนก็เหนื่อยนิดหน่อยนะ…"

show lilly basic_ara_paj
with charachange

li "แหม ๆ คืนนี้ฮานาโกะดูหัวไวเป็นพิเศษเลยนะ"

show lilly basic_weaksmile_paj
with charachange

li "ฉันว่าเราควรไปนอนได้แล้วละจ้ะ พรุ่งนี้มีเรียนด้วย"

hi "อืม… ฉันก็ควรไปละ"

show lilly basic_smile_paj
with charachange

li "ขอบคุณที่มานะจ๊ะ ฮิซาโอะ"

show hanagown normal
with charachange

ha "ขะ… ขอบใจนะ นายจะมาอีกใช่ไหม"

hi "ต่อให้มีช้างมาฉุด ฉันก็จะมาให้ได้"

show lilly basic_cheerful_paj
with charachange

li "ฉันละยอมใจในความมุ่งมั่นของเธอจริง ๆ เลยนะฮิซาโอะ"

hi "เอาเถอะ ก็คงตามนั้นแหละ แยกย้ายกันเถอะ"

"ฉันลุกขึ้นเดินไปยังประตู"

show hanagown normal at tworight
with dissolvecharamove

"ฮานาโกะค่อย ๆ ลุกตามมา"

"ฉันหยุดและหันไปหาเธอ"

hi "จะไปด้วยกันเหรอ"

play music music_comedy fadein 0.5

show hanagown normal_blush
with charachange

"ฮานาโกะหน้าแดงแปร๊ดอย่างฉับพลัน"

show hanagown distant_blush
with charachange

ha "เปล่า… ฉัน… ไม่ได้… พอดีห้อง…"

hi "ล้อเล่นน่า ไม่เป็นไรหรอก"

show hanagown smile
with charachange

ha "อ้อ… โอเค… ราตรีสวัสดิ์…"

show lilly basic_smileclosed_paj
with charachange

li "ราตรีสวัสดิ์ฮานาโกะ ราตรีสวัสดิ์ฮิซาโอะ"

hi "ราตรีหวัดทุกคน"

"และงานเลี้ยงน้ำชาก็จบลงเช่นนั้น"

scene bg school_girlsdormhall
with locationchange

"ฉันยังไม่มั่นใจว่าลิลลี่อยากให้ฉันทำอะไรเพื่อฮานาโกะกันแน่ แต่ฉันก็ไม่อยากทำให้เธอผิดหวัง"

"ฉันรอจนประตูปิดจนสนิทก่อนจะหันไปหาฮานาโกะ"

show hanagown distant_blush
with charaenter

hi "นี่ฮานาโกะ เธอไม่ต้องกังวลหรืออะไรเวลาอยู่กับฉันหรอกนะ"

hi "ก็แบบ เราเป็นเพื่อนกันนี่นะ จริงไหม"

show hanagown normal_blush
with charachange

ha "ชะ-ใช่ เราเป็น… เพื่อนกัน"

hi "ถ้าอยากเจอกันหรือยังไงก็บอกได้เลย เรายังค้างกันเรื่องเล่นหมากรุกอีกรอบนะ จำได้ไหม"

show hanagown distant
with charachange

ha "อะ-อื้ม…"

show hanagown normal
with charaenter

ha "ตะ-แต่รอบนี้นายแพ้แน่…"

hi "ถ้าชนะง่าย ๆ ก็ไม่สนุกน่ะสิ"

show hanagown smile
with charachange

"ดูเหมือนว่าฮานาโกะจะหัวเราะเบา ๆ แต่อาจจะแค่ถอนหายใจออกมาเฉย ๆ ก็ได้"

ha "ฝะ-ฝันดีนะ ฮิซาโอะ…" 

show hanagown invis at tworight
with Dissolvemove(0.5, time_warp=_ease_out_time_warp)

hide hanako
with None

stop music fadeout 5.0

"พูดจบ ฮานาโกะก็รีบรุดเข้าห้องของตัวเองไปทันที ซึ่งห้องของเธอก็อยู่ติดกับห้องของลิลลี่เลย"

"ฉันเดินกลับไปที่หอของฉัน แต่แค่การเดินธรรมดา ๆ ก็เหมือนจะสูบพลังงานที่มีไปจนหมดเลย"

scene bg school_dormhisao
with locationskip

"ฉันมาถึงห้องแบบฉิวเฉียดก่อนความเหนื่อยล้าจะถาโถมเข้ามา"

play sound sfx_switch

scene bg school_dormhisao_ni
with Dissolve(0.2)

"ฉันถอดรองเท้าทิ้งตัวลงบนเตียงและหลับลงทันทีที่หัวถึงหมอน"

scene black
with dissolve

#-----------------
label th_H8:

scene bg school_dormhallway
with locationchange

"ฉันปิดประตูเตรียมพร้อมออกไปเรียนอีกวัน"

show kenji invis at twoleft
with None

show kenji neutral_close at center
with Dissolvemove(0.5, time_warp=_ease_in_time_warp)

ke "หลับสบายดีไหม"

play music music_kenji fadein 0.5

"เคนจิโผล่มาแบบไม่ทันตั้งตัว เลยทำให้ฉันสะดุ้งสุดตัวและเกือบจะหัวโขกกับเขาเข้า"

"ก็รู้แหละว่าเขาสายตาไม่ดี แต่ในเมื่อก็รู้อยู่แล้วว่าฉันเป็นใคร ทำไมยังมายืนใกล้ขนาดนี้อีก"

show kenji neutral
with charadistant

hi "อ้อ เออ หลับปุ๋ยเป็นเด็กเลย"

show kenji tsun
with charachange

ke "แม่ง ทำไมคนถึงพูดแบบนั้นกันวะ นายเคยได้ยินตอนเด็กเล็กหลับปะ"

ke "ร้องแทบทั้งคืน ทุกคืน เด็กเล็กน่ะ ไม่เคยนอนเต็มอิ่มหรอก"

"เอาละ ลาก่อนความสงบยามเช้า ต้องจำไว้เลยว่าห้ามใช้สำนวนกับเคนจิเด็ดขาด"

hi "เออ ๆ เข้าใจละ แค่เปรียบเทียบหรอก"

show kenji neutral
with charachange

ke "เอองั้นแหละ เอาเถอะ เมื่อคืนนายไปไหนมาเนี่ย ว่าจะให้ช่วยอะไรสักหน่อยแต่นายไม่อยู่ซะงั้น"

"แวบนึงฉันคิดที่จะบอกความจริงกับเคนจิไปว่าฉันไปอยู่กับฮานาโกะและลิลลี่"

"โชคดีที่ความคิดแวบนั้นแค่ผ่านมาแล้วก็ผ่านไป"

hi "แค่ออกไปข้างนอกมาน่ะ ไปสำรวจแถว ๆ นี้มานิดหน่อย แบบว่าลาดตระเวนอะ"

show kenji happy
with charachange

ke "ดีละ ฉันนึกแล้วว่านายเป็นพวกชอบวางแผนล่วงหน้า…"

hi "เอาเหอะ แล้วจะขอให้ช่วยอะไรล่ะ"

show kenji neutral
with charachange

ke "ฉันว่าจะสั่งอาหารสักหน่อยน่ะ แต่ต้องการเศษเงินนิดหน่อย"

hi "เดี๋ยวนะ เงินที่ฉันให้นายไปเมื่อสัปดาห์ก่อนนายยังไม่ได้คืนมาเลยนะ!"

show kenji tsun
with charachange

ke "ชิ นึกว่านายจะเป็นพวกเจ๋งเสียอีก"

"เคนจิล้วงกระเป๋ากางเกงและหยิบกระเป๋าสตางค์ออกมา"

"พอเขาหยิบเงิน 400 เยนที่ยืมออกมา ฉันก็เห็นแบงก์ 10000 เยนอย่างต่ำ ๆ ก็สองใบ"

hi "อะไรเนี่ย รวยขนาดนั้นแล้วจะยืมกันหาพระแสงอะไร"

"เคนจิจิ๊ปากเมื่อเห็นว่าความแตกแล้ว"

ke "อย่ายุ่งเถอะน่า ถ้าเอาแบงก์ใหญ่ไปแตกกับของที่ราคาไม่ถึงครึ่งแล้วมันจะโชคร้ายนะ เป็นกฎเศรษฐีเว้ย"

ke "มื้อเย็นเมื่อคืนทำให้ฉันต้องโชคร้ายไปตั้งเจ็ดปีเลยนะ ตั้งเจ็ดปี!"

show kenji happy
with charachange

ke "รู้งี้แล้วยังจะไม่อยากช่วยอีกเหรอ ขนาดถ้าฉันขโมยของยังจะโดนโทษเบากว่านี้อีกนะ"

"สามัญสำนึกของฉันร้องบอกให้ฉันพูดอะไรบางอย่างกับเขา แต่ยังดีที่ฉันห้ามตัวเองไว้ได้"

"การเถียงเรื่องแบบนี้กับเคนจิมีแต่จะทำให้เรื่องยุ่งยากและซับซ้อนขึ้นไปอีก"

hi "เออ ก็คงงั้นแหละ คราวหลังก็วางแผนให้ดีกว่านี้ละกัน"

show kenji neutral
with charachange

ke "เออน่ารู้แล้ว แต่ฉันก็มีอะไรต้องทำเยอะแยะเลย มันยากนะเว้ย แล้วช่วงนี้นายก็ไม่ค่อยอยู่ด้วย ฉันเลยต้องทำคนเดียว\nตลอดเลย"

ke "อย่าลืมสิว่าเราเป็นเหมือนพี่น้องกันนะ!"

hi "เออ ๆ เข้าใจแล้ว ทฤษฎีสมคบคิดระดับโลกและอะไรเทือกนั้น ฉันจะคอยตามข่าวเรื่อย ๆ ละกัน"

show kenji neutral_close
with charachange

"เคนจิยื่นหน้าเข้ามาใกล้จนได้กลิ่นปากกลิ่นกระเทียม"

show kenji tsun_close
with charachange

ke "เออ ตามไว้เลย นายแทบจะอยู่ไม่ติดห้องแล้วนะ และนั่นแหละเป็นสิ่งแรกที่พวกนั้นจะทำ"

ke "พวกนั้นจะพยายามแยกเราออกจากกัน แบบแบ่งแยกและเอาชนะไง ซุนวูได้กล่าวไว้"

hi "รับทราบ แต่ตอนนี้ฉันต้องไปละ มีเรียนอีก นายไปไหม"

show kenji neutral_close
with charachange

ke "ไม่อะ เหนื่อยแล้ว พอดีอยู่โต้รุ่งรอดูว่าจะมีอะไรเกิดขึ้นหลังแตกแบงก์นั้นไปไหม"

hi "มีเหตุผลเช่นเคยเลยนะ"

show kenji tsun_close
with charachange

ke "เอาเหอะ ราตรีหวัด"

stop music fadeout 3.0

show kenji invis at twoleft
with Dissolvemove(0.5, time_warp=_ease_out_time_warp)

"เคนจิรีบวิ่งกลับเข้าไปในห้อง และขณะที่ฉันกำลังเดินไปตามโถงทางเดินก็ได้ยินเสียงเขาลั่นกลอนประตู"

#--------------

label th_H9:

scene bg school_dormhallway
with None

scene bg school_scienceroom
show muto smile at center
with shorttimeskip

play music music_daily fadein 4.0

mu "…นั่นเป็นเหตุผลว่าทำไมบางคนถึงห่อลิ้นไม่ได้ หรือทำไมบางคนนิ้วชี้เท้ายาวกว่านิ้วโป้งเท้า"

"ครูมุโต้ยิ้มแฉ่งเป็นพระจันทร์ครึ่งซีกให้พวกเรา เห็นได้ชัดเลยว่าภูมิใจกับคำอธิบายเรื่องยีนด้อยของตัวเองมาก ๆ"

"อย่างไรก็ตาม ไม่ว่าครูจะประทับใจกับหลักวิทยาศาสตร์ที่กำหนดว่าเราเป็นใครมากแค่ไหน บรรยากาศในห้องเรียน\nก็ยังคงเงียบกริบเหมือนเดิม"

"ทำไมคำอธิบายที่แย่ ๆ ถึงทำให้เรื่องที่น่าสนใจที่สุดกลายเป็นเรื่องไร้ค่าไปได้เลยกันนะ"

show muto irritated
with charachange

"ฉันเห็นครูมุโต้หน้าเจื่อนลงจากการที่เขารู้ตัวว่าตลอดครึ่งชั่วโมงที่ผ่านมาไม่มีอะไรที่พูดไปเข้าหัวพวกเราเลยแม้แต่น้อย"

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 4.0

"แล้วเสียงซุบซิบก็เริ่มดังขึ้นมาทำลายความเงียบ และไม่นานเสียงคุยก็เริ่มดังขึ้นเรื่อย ๆ ราวหิมะถล่มที่ไร้การยับยั้ง"

show muto normal
with charachange

"ด้วยหมดหนทาง ครูมุโต้หาคำถามจากในหนังสือเรียนมาให้ทำแล้วก็เริ่มลบกระดาน"

hide muto
with charaexit

"ไม่ผิดจากที่คาด พอคนเริ่มคุยและหัวเราะกัน ฮานาโกะก็รีบเก็บของแล้วเดินออกจากห้องไปทันที"

"ช่วงแรกก็ตกใจที่เห็นคนโดดเรียนแบบโจ่งแจ้งขนาดนี้ ตอนนี้ความรู้สึกนั้นเริ่มลดลงไปบ้างแล้ว แต่ก็อดสงสัยไม่ได้อยู่ดี"

"เธอออกไปเพราะไม่อยากให้ใครมาคุยด้วยหรือเปล่า หรือแค่ไม่อยากให้คนรอบข้างมาทำลายความสงบของเธอ"

play sound sfx_normalbell
$ renpy.music.set_volume(1.0, 4.0, channel="ambient")

"ก่อนที่ฉันจะได้คิดอะไรไปมากกว่านี้ เสียงระฆังพักเที่ยงก็ดังขึ้นมาเสียก่อน ที่ฮานาโกะออกไปก่อนหน้านี้คือ\nแค่เพราะจะหาโอกาสที่จะออกไปก่อนหรือเปล่านะ"

"เสียงเหล่านักเรียนที่เก็บหนังสือกลับเข้ากระเป๋าและควักข้าวเที่ยงออกมาดังไปทั่วอย่างเคย ตอนที่มิช่ากำลังวุ่น ๆ\nอยู่นั้นเองฉันก็รีบคว้ากล่องข้าวแล้วเดินออกจากห้องไปทันที"

stop ambient fadeout 1.0

scene bg school_miyagi
show lilly basic_smileclosed:
    center
    ypos 1.2
with locationskip

"ลิลลี่นั่งอยู่ในห้องน้ำชาแล้ว เธอกำลังจัดเตรียมอาหารกลางวันของตัวเองอยู่คนเดียว"

hi "เอ่อ ฮานาโกะไม่อยู่ที่นี่สินะ"

show lilly basic_smile
with charachange

li "อ้าว ฮิซาโอะ สบายดีมั้ยจ๊ะ แต่ขอโทษทีจ้ะ ฉันก็เจอกับฮานาโกะแค่เมื่อเช้ารอบเดียวเอง"

"นั่นสินะ ฮานาโกะกับลิลลี่อยู่ห้องข้าง ๆ กันเลยนี่นา"

"ไม่รู้ทำไม แต่บทสนทนาตอนเช้าของสองคนนั้นน่าจะมีสาระกว่าเรื่องที่เคนจิเพ้อเจ้อเยอะเลย"

hi "แปลกจัง พอดีฮานาโกะออกมาก่อนก็เลยนึกว่ามาที่นี่น่ะ"

show lilly basic_displeased
with charachange

li "ตอนนี้ก็ยังออกก่อนเวลางั้นเหรอ…"

hi "หืม อื้ม ก็เห็นออกไปสองสามทีอยู่"

show lilly basic_sad
with charachange

stop music fadeout 7.0

"ลิลลี่ก้มหน้าลงเล็กน้อย เสียงเธอฟังดูหมองลงอย่างเห็นได้ชัด ดูอย่างกับคนที่เพิ่งได้ฟังข่าวร้ายมายังไงยังงั้น"

li "ฉันก็นึกว่าพอพวกเธอสองคนเป็นเพื่อนกันแล้วฮานาโกะจะเลิกทำอย่างนั้นน่ะ"

show lilly basic_weaksmile
with charachange

li "คนเราก็คงค่อยเป็นค่อยไปปรับตัวได้เร็วไม่เท่ากันน่ะนะ"

hi "ก็นะ วันนี้ฉันก็สงสัยอยู่เหมือนกันว่าทำไมเธอถึงต้องออกก่อนด้วย"

show lilly basic_reminisce
with charachange

li "ฉันเองก็ไม่แน่ใจเท่าไหร่ แต่ส่วนตัวฉันว่าเพราะเธอไม่อยากอยู่ในสถานการณ์ที่จะต้องคุยกับใครน่ะจ้ะ"

"ฉันนึกถึงตอนที่เจอเธอครั้งแรกขึ้นมาทันที ตอนนั้นฉันคิดว่าเธอดูเหมือนสัตว์ที่จนมุมอยู่ในกรง พอมานึกแล้วก็คง\nไม่ต่างจากความเป็นจริงเท่าไหร่"

hi "แต่ตอนคุยกับเธอฮานาโกะก็ดูไม่อะไรนี่ ตอนคุยกับฉันด้วย… นิดหน่อย…"

show lilly basic_displeased
with charachange

li "เรื่องมันซับซ้อนกว่านั้นนิดหน่อยน่ะ เวลาคนเจอฮานาโกะก็คงถามเรื่องแผลเป็นนั้นก่อน แล้วก็ถามว่าเกิดอะไรขึ้น"

li "เธอก็ไม่ค่อยคุยเรื่องนั้นกับฉันเท่าไหร่หรอก แต่ก็พอรู้ว่าเธอไม่อยากจะรำลึกถึงความหลังสักเท่าไหร่"

show lilly basic_reminisce
with charachange

li "การที่ออกจากห้องไปไม่ยอมคุยอย่างนั้น ก็คงเป็นวิธีตอบโต้ล่วงหน้าในแบบของฮานาโกะเขานั่นแหละจ้ะ"

hi "หืม… แล้วทำไมฮานาโกะถึงยังมาคุยกับฉันล่ะ"

show lilly basic_weaksmile
with charachange

li "เธอบอกเองเมื่อวานตอนมื้อเช้านี่จ๊ะ ว่าเธอพยายามไม่สนใจแผลเป็นของฮานาโกะ แล้วพอเห็นว่าเธอไม่ได้พูดถึง\nเรื่องนั้น ฮานาโกะก็เลยยอมเปิดใจน่ะจ้ะ"

hi "อืม ก็จริง คงงั้นแหละมั้ง ไม่รู้ดิ เธอรู้จักฮานาโกะดีกว่าฉันนี่นะ เอาเป็นว่าจะเชื่อเธอแล้วกัน"

play music music_normal fadein 3.0

show lilly basic_giggle
with charachange

li "ฉันว่าไม่ต้องคิดมากหรอกจ้ะ ฉันเชื่อว่าไม่นานเดี๋ยวเธอก็จะได้รู้จักฮานาโกะดีเท่าฉันแน่นอน"

show lilly basic_smileclosed
with charachange

li "ฉันก็ดีใจนะที่ฮานาโกะจะได้มีเพื่อนใหม่ แล้วพวกเธอทั้งคู่ก็ดูมีอะไรที่คล้ายกันหลายอย่างอยู่นะ…"

hi "ก็ไม่ขนาดนั้นหรอก ฉันว่าการอ่านหนังสือน่ะไม่ใช่เรื่องที่ต้องทำเป็นทีมอยู่แล้ว แต่การมีเพื่อนอ่านด้วยก็เป็นเรื่องดีน่ะนะ"

show lilly basic_smile
with charachange

li "นั่นแหละจ้ะ ฮานาโกะเองก็เป็นคนธรรมดาคนหนึ่ง เธอเองก็อยากมีเพื่อนอยู่ด้วยบ้างในบางครั้งเหมือนกัน"

hi "อ๋อ เข้าใจละ มั้งนะ เอาจริง ๆ พวกเธอทั้งคู่ทำฉันสับสนนิดหน่อย"

show lilly basic_smileclosed
with charachange

li "ปกติจ้ะฮิซาโอะ พวกเราเพิ่งรู้จักกันไม่นานเอง พวกเราก็ไม่ได้คาดหวังให้เธอมาเข้าใจเลยหรอก เพราะพวกเราเองก็ยัง\nไม่เข้าใจเธอเลยเหมือนกัน"

show lilly basic_weaksmile
with charachange

li "แต่นั่นก็เป็นเรื่องสนุกของการได้เป็นเพื่อนกันนี่ จริงไหมจ๊ะ"

hi "ใช่ ถูกเลยละ"

show lilly basic_giggle
with charachange

li "แต่ฉันว่า… สิ่งที่มีผลจริง ๆ ก็เพราะเพศไม่ตรงกันนี่แหละ ผู้ชายกับผู้หญิงมักจะไม่ค่อยเข้าใจกันอยู่บ่อย ๆ ละนะ"

"เธอพูดไปหัวเราะคิกคักไป ดูเหมือนจะรู้สึกขบขันกับเรื่องเล็ก ๆ น้อย ๆ ในชีวิต"

show lilly basic_cheerful
with charachange

li "ฉันจะทานข้าวแล้ว หวังว่าเธอจะไม่ว่าอะไรนะ"

hi "ไม่ ๆ เอาเลย ฉันว่าจะกินด้วยเหมือนกัน ต้องรีบกินแล้วรีบเอาหนังสือไปคืนห้องสมุดก่อนเข้าเรียนด้วย"

show lilly basic_smileclosed
with charachange

li "เดี๋ยวถ้าไปก็น่าจะเจอฮานาโกะ ถ้าเจอก็ฝากบอกให้ฮานาโกะมาที่ห้องฉันคืนนี้หน่อย พอดีมีเรื่องจะคุยน่ะ"

hi "แล้วเธอไม่ไปกับฉันเหรอ"

show lilly basic_weaksmile
with charachange

li "พอดีมีประชุมหัวหน้าห้องต่อ เลยว่าถ้าทานเสร็จแล้วก็จะไปประชุมเลยน่ะจ้ะ"

hi "โอเค งั้น ถ้าไม่เจอที่ห้องสมุดเดี๋ยวเอาไปบอกตอนเจอกันในห้องให้ พักเที่ยงแล้วก็คงกลับมา"

"เราต่างเงียบไปขณะที่เริ่มกิน และฉันก็ใช้เวลาสักครู่ทบทวนเรื่องที่เราเพิ่งคุยกันไป"

"ฉันนึกมาตลอดเลยว่าความขี้อายของฮานาโกะเป็นเพราะเธอไม่มั่นใจในรอยแผลเป็นของตัวเอง"

"แต่นั่นเป็นเพียงแค่การมองเธอแบบผิวเผินเท่านั้น"

"พอคิดว่าตัวเองเข้าใจเรื่องของลิลลี่กับฮานาโกะแล้ว ฉันกลับพบว่าตัวเองยิ่งสับสนหนักกว่าตอนแรกเสียอีก"

"ลิลลี่กินมื้อเที่ยงของเธอเสร็จอย่างรวดเร็วเพราะตระหนักดีว่าเธอมีนัดอยู่ ซึ่งฉันก็เข้าใจเธอนะ"

"ชิซูเนะเองก็คงไปด้วย และฉันว่าเธอคงไม่อยากเปิดโอกาสให้ชิซูเนะมาหาเรื่องเถียงได้อีกรอบ"

show lilly basic_smile
with charachange

li "ฉันต้องไปแล้วละจ้ะ พรุ่งนี้เวลาเดิมไหม"

hi "โอเค เวลาเดิม ที่เก่าเจ้าเดิม ฉันก็ต้องรีบไปเหมือนกัน ไม่อยากเสี่ยงไปสาย"

show lilly cane_smileclosed
with charachange

show lilly cane_smileclosed at center
with charamove

stop music fadeout 4.0

"ลิลลี่ยิ้มเบา ๆ ก่อนจะหยิบไม้เท้าของเธอและเดินออกไปยังโถง"

#----------

label th_H10:

scene bg school_hallway2
with locationchange

"ฉันหันหลังให้ลิลลี่แล้วแยกกันไปคนละทาง ไม่รู้ทำไมฉันถึงหวังว่าลิลลี่จะไม่ต้องไปทะเลาะกับชิซูเนะอีก"

"ถึงแม้ฉันจะชอบลิลลี่มากแค่ไหน แต่ก็ต้องยอมรับว่าชิซูเนะกับมิช่าเองก็มีส่วนช่วยให้ฉันปรับตัวได้เยอะเหมือนกัน\nถึงแม้บทสนทนาส่วนใหญ่ของเราจะแฝงไปด้วยความพยายามในการชักชวนให้เข้าร่วมสภาก็เถอะ"

"แต่ก็นั่นแหละ ฉันแทบไม่รู้จักพวกเธอเลย บางทีพวกเธออาจเคยเป็นผู้นำของสมาคมลับบางอย่างมาก่อน แต่ความรัก\nที่มีให้กันกลับทำให้ทั้งคู่ต้องแยกจากกันไป…"

"โอย คงต้องหยุดอ่านนิยายน้ำเน่าได้ละ สมองเสียหมด หรืออีกอย่างก็คือต้องอยู่ให้ห่างจากเคนจิกับการชักนำแย่ ๆ\nของเขา"

"แย่หน่อยที่ฉันแยกทั้งสองอย่างที่ว่าไม่ค่อยออกละ"

scene bg school_library at right
with locationskip

play music music_happiness fadein 2.0

"ฉันเลื่อนหนังสือลงบนรางสำหรับส่งคืน กองหนังสือตกลงไปกระทบกับรถเข็นด้านล่างเกิดเป็นเสียงดังที่ฟังดูน่าพอใจดี"

play sound sfx_impact2

show yuuko panic_up
with vpunch

"อย่างไรก็ตาม ยูโกะดูไม่ได้พอใจแบบที่ฉันพอใจ"

yu "ฮะ ฮิซาโอะ! ตกใจหมด!"

hi "ขอโทษทีครับ นึกว่าคุณจะชินแล้วนะ หรือว่าที่นี่คนรู้หนังสือน้อยมากจนไม่มีใครยืมหนังสือเลยเหรอ"

show yuuko worried_up
with charachange

yu "หืม ไม่นะ ฉันว่าทุกคนก็อ่านออกกันนะ…"

hi "อ๋อ… ช่างเถอะครับ"

"บางอย่างเราก็ไม่มีทางชนะ การพยายามอธิบายมุกตลกก็เป็นหนึ่งอย่างในนั้น ฉันรู้มากับตัวเพราะพ่อนี่แหละ"

hi "ว่าแต่ คุณยูโกะครับ เห็นฮานาโกะบ้างหรือเปล่า เห็นออกมาก่อนเวลา แต่ว่าก็ไม่ได้อยู่ที่ซ่อนประจำน่ะ"

show yuuko closedhappy_down
with charachange

yu "ฉันว่าฉันเห็นเธอแอบเข้ามาก่อนพักเที่ยงอยู่นะ…"

show yuuko panic_up
with charachange

yu "โอ๊ะ! แต่ฉันไม่ควรบอกเรื่องนั้นให้ใครรู้นี่นา!"

hi "ผมเพิ่งเล่าไปเองว่าเห็นเธอออกมาก่อนน่ะ เพราะงั้นไม่ต้องคิดมากหรอกครับ…"

show yuuko smile_down
with charachange

yu "อ้อ… โอเค น่าจะอยู่ข้างหลังนะ"

hi "ขอบคุณครับ ว่าแต่มีหนังสือใหม่มาไหมครับช่วงนี้"

show yuuko worried_up
with charachange

yu "ขอโทษที ยังไม่มีน่ะ ถ้ามีเมื่อไหร่เดี๋ยวฉันจะบอกนะ"

hi "โอเคครับ"

"ถ้าจะมีเรื่องหนึ่งที่ฉันรู้เกี่ยวกับบรรณารักษ์ ไม่ว่าจะประจำหรือพาร์ทไทม์ ก็คือพวกเขาจะรู้สึกชื่นชมคนที่แสดง\nความสนใจในงานของพวกเขาอย่างจริงใจ"

hide yuuko
with charaexit

show bg school_library at Fullpan(10.0, dir="left")
with None

"ฉันเดินไปตามเส้นทางที่คุ้นเคยเพื่อไปที่มุมอ่านหนังสือของฮานาโกะ โดยเลือกหนังสือไปสองสามเล่มระหว่างทาง"

"บางทีก็ยากที่จะหาหนังสือที่น่าสนใจได้จากชั้นวาง ชื่อผู้เขียนกับชื่อหนังสือสองสามพยางค์ที่ดูเหมือน ๆ กันไปหมด\nในกองตัวอักษรพวกนี้ไม่ได้สื่ออะไรมากมาย"

"นั่นเป็นเหตุผลที่บางครั้งฉันกลับไปอ่านหนังสือที่เคยอ่านมาแล้ว สู้ลงเงินกับม้าตัวโปรดยังจะดีกว่าลงกับม้าตัวใหม่"

"มีชื่อหนังสือที่ไม่คุ้นเคยของนักเขียนที่คุ้นเคยเล่มหนึ่งโผล่ออกมาจากชั้นวางท่ามกลางเล่มอื่น ๆ ฉันเลยหยิบออกมาดู"

"อย่างน้อยก็ไม่ใช่เรื่องเก่าละนะ"

scene ev hana_library_read_std
with locationskip

"อย่างที่คาดไว้ ฮานาโกะนั่งอยู่บนบีนแบ็กและกำลังอ่านเรื่อง “{i}เริงระบำแดนสนธยา{/i}” อย่างตั้งใจ"

hi "ไงฮานาโกะ เป็นไงบ้าง"

"ฉันกลั้นความอยากถามว่าทำไมเธอถึงออกจากห้องเรียนก่อนเวลา ถ้าที่ลิลลี่สงสัยเป็นเรื่องจริง การถามเรื่องนั้นออกไป\nอาจจะให้ผลตรงกันข้ามเลยก็เป็นได้"

"ปล่อยให้เป็นเรื่องของเวลาคงจะดีที่สุด บางทีทางที่ดีที่สุดการที่จะได้คำตอบมาคือการที่ไม่ถามอะไรไปเลย"

show ev hana_library_smile_std
with charachange

ha "สวัสดี ฮะ-ฮิซาโอะ ก็สบายดี"

"บางอย่างแปลกไป และพอผ่านไปสักพักฉันก็เห็นว่าบางอย่างที่ว่าคือ ฮานาโกะยิ้มอยู่"

"เธอดูดีใจที่ได้เจอฉัน เป็นความรู้สึกที่ดีที่แตกต่างไปจากปฏิกิริยาหวาดกลัวที่เจอบ่อย ๆ และเป็นสิ่งที่ฉันหวังว่าจะได้เห็น\nบ่อยขึ้นเมื่อเราได้รู้จักกันมากขึ้น"

hi "ดีแล้วละ แล้วเล่มนั้นเป็นไง เห็นว่าสนุกน่าดูเลย"

ha "กะ-ก็ดี… คิดว่านะ"

ha "ฉันเพิ่งดะ-ได้อ่านน่ะ ก็เลย มะ-ไม่ค่อยรู้น่ะ"

hi "เข้าใจได้ เป็นไงเอามาเล่าด้วยนะ เผื่อเธออ่านจบแล้วจะได้ขอยืมมาอ่านบ้าง"

ha "อะ-อื้ม"

"เหลือเวลาสิบห้านาทีก่อนหมดพักเที่ยง ไม่พอที่ให้อ่านหนังสือสักเล่ม แต่ก็นานเกินกว่าจะยืนเฉย ๆ ไม่ทำอะไรเลย"

show ev hana_library_read_std
with charachange

"และฮานาโกะเองก็หันกลับไปอ่านหนังสือแล้ว คงไม่น่าได้คุยอะไรมาก"

"เอาเถอะ ปล่อยตัวสบาย ๆ แล้วกัน"

play sound sfx_pillow

"ฉันเอนตัวลงบนบีนแบ็กและเปิดหนังสืออ่าน"

"สไตล์การเขียนที่คุ้นเคยของนักเขียนคนนี้โดดเด่นออกมาตั้งแต่บรรทัดแรก พอไล่อ่านประโยคต่อยาวมาจนครบย่อหน้า\nฉันก็เริ่มผ่อนคลายลงเล็กน้อย"

stop music fadeout 8.0

"แต่ไม่ว่าจะพยายามแค่ไหน ก็ดูเหมือนจะเข้าไม่ถึงบรรยากาศของหนังสือเล่มนี้เลย"

"ส่วนหนึ่งก็เพราะเวลาไม่พอ แต่สิ่งที่รบกวนใจมากกว่าก็ฮานาโกะนี่แหละ"

show ev hana_library_std
with charachange

show ev hana_library_read_std
with charachange

"ประมาณทุก ๆ สิบวินาทีหรือราว ๆ นั้นเธอจะแอบมองลอดหนังสือมา แต่พอสบตากันก็จะหลบหลังหนังสือ"

"เดาว่าเธอคงอยากคุยอะไรสักอย่างแน่ ๆ "

scene bg school_library
with locationskip

hi "มีอะไรหรือเปล่า ดูอย่างกับตัวแพรรีด็อกที่กำลังเฝ้ายามอยู่เลย"

show hanako emb_blushing:
    center
    ypos 1.17
with charaenter

ha "มะ… ไม่มีอะไร"

hi "ก็บอกแล้วนี่ว่าเวลาเธอพูดว่า “ไม่มีอะไร” เนี่ยมักจะ “มีอะไร” ตลอด"

show hanako cover_worry
with charachange

"ฮานาโกะขยับตัวเล็กน้อยอยู่บนบีนแบ็กด้วยหวังให้การเปลี่ยนท่านี้จะช่วยให้นึกคำที่จะตอบได้"

show hanako emb_downsad
with charachange

ha "ฉะ… ฉันประสบอุบัติเหตุน่ะ"

hi "อุบัติเหตุ? เมื่อกี้เหรอ เป็นอะไรไหม"

show hanako emb_sad
with charachange

"ฮานาโกะส่ายหน้า ผมของเธอพลิ้วไหวรอบไหล่เป็นระลอกสีม่วงบนผิวเนื้อที่ซีดและคล้ำ"

show hanako emb_downsad
with charachange

ha "ปะ-เปล่า ตอนที่ฉันยะ-ยังเด็กน่ะ"

play music music_hanako

"ความคิดพลันแล่นเข้ามาเหมือนรถบรรทุกพุ่งเข้าชน"

ha "ตอนที่ฉัน… ตอนที่ฉันยัง… "

hi "ไม่เป็นไรฮานาโกะ ถ้าไม่อยากเล่าก็ไม่ต้องเล่าก็ได้นะ"

"เธอส่ายหัวอีกครั้ง"

show hanako emb_sad
with charachange

ha "มะ-ไม่ ฉันอยาก… ฉันจะต้องบอกนาย"

scene ev hanako_crayon1:
     truecenter zoom 1.0 subpixel True
     linear 20.0 zoom 1.05
with locationskip

ha "ตอนที่ฉันยังเด็ก… บ้านฉันไฟไหม้"

ha "ละ-แล้ว ฉันก็ตะ-ติด อยู่ในนั้น จนเกือบ… จนเกือบไม่รอดออกมาแล้ว…"

show ev hanako_crayon2:
     linear 8.0 zoom 1.05
with charachange

ha "จะ-จากนั้น… ฉันก็ตัวคนเดียวมาตลอด…"

scene bg school_library
show hanako emb_downsad_close:
    center
    ypos 1.1
with locationskip

"ดวงตาของฮานาโกะเป็นประกายในแสงสลัวของห้องสมุด และฉันก็เอื้อมมือไปกุมมือเธอไว้"

hi "ไม่เป็นไรฮานาโกะ เธอไม่ต้องเล่าต่อก็ได้"

show hanako emb_sad_close
with charachange

ha "ตะ-แต่… ฉันต้อง…"

hi "ทำไมล่ะ ทำไมเธอถึงเล่าขึ้นมา"

show hanako cover_distant_close
with charachange

ha "มะ-เมื่อคืนลิลลี่เล่าเรื่องหัวใจ ขะ-ของนายให้ฉันฟังน่ะ…"

show hanako cover_worry_close
with charachange

ha "ละ-และฉะ… ฉันคิดว่ามันไม่ ยะ-ยุติธรรมน่ะ"

hi "ยุติธรรม?"

show hanako emb_blushing_close
with charachange

ha "ทะ-ที่ฉันรู้เรื่องของนาย ตะ-แต่นายไม่รู้เรื่องฉันน่ะ…"

"ฉันบีบมือฮานาโกะเบา ๆ"

hi "พูดบ้า ๆ น่า แต่ใช่ ฉันเป็นโรคหัวใจ"

"ฉันเอนตัวเข้าไปใกล้ฮานาโกะเล็กน้อย"

hi "ที่ฉันไม่ได้บอกลิลลี่ไปก็คือ หัวใจฉันวายครั้งแรกก็ตอนที่มีสาวมาสารภาพรักน่ะ"

"ฉันยิ้มเล็กน้อยเพื่อคลายความตึงเครียด"

show hanako cover_worry_close
with charachange

ha "จ-จริงเหรอ"

hi "อื้ม ซึ่งฉันก็ไม่ได้ข่าวคราวเธอมาสักพักแล้ว ฉันคิดว่าก็คงจบกันไปแล้วละ"

"ฉันรู้อยู่แล้วละว่ามันจบไปแล้ว สิ่งที่เกิดขึ้นเมื่อตอนที่ฉันได้เจอเธอเป็นครั้งสุดท้ายนั้นตีความเป็นอื่นไม่ได้อีก ในแง่หนึ่ง\nการที่ไม่ได้ข่าวจากเธออีกเลยก็ช่วยให้ฉันก้าวผ่านช่วงเวลานั้นของชีวิตมาได้"

hi "เอาละ ตอนนี้เราต่างคนต่างก็ได้รู้เรื่องของกันและกันมากขึ้นแล้วนะ แต่ถ้าเธอไม่อยากเล่าอีกก็ไม่ต้องเล่าแล้วก็ได้"

"จริง ๆ ก็รู้สึกแย่หน่อย ๆ พอนึกถึงเรื่องราวทั้งหมดนั่น แทบจะรู้สึกได้ถึงกลิ่นยาฆ่าเชื้อของโรงพยาบาลที่แสบโพรงจมูก\nอีกครั้ง"

"ฉันว่าฮานาโกะก็ผ่านอะไรแบบนี้มาเหมือนกัน"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\nตอนที่ฉันยังอยู่ในโรงพยาบาล ฉันไปที่แผนกไฟไหม้น้ำร้อนลวกครั้งนึง และแค่ครั้งเดียวเท่านั้น เพราะตอนนั้นเบื่อ ๆ\nเลยเดินเล่นไปทั่วทุกแผนก"

n "ฉันเดินผ่านแผนกมะเร็งมาได้แบบสบาย ๆ แต่พอไปถึงแผนกไฟไหม้น้ำร้อนลวกเท่านั้นแหละ ฉันก็หันหลังกลับไปที่เตียง\nตัวเองทันทีเลย"

n "แล้วฮานาโกะต้องใช้เวลาอยู่ที่นั่นเป็นเดือน ๆ ได้กลิ่นแค่ผิวหนังที่เสียหาย น้ำยาฆ่าเชื้อแรง ๆ กับอากาศปลอดเชื้อ"

n "พวกที่อาการหนัก ๆ จะถูกแยกไว้ในห้องกักกันที่ไม่มีสิ่งแปลกปลอมใด ๆ เข้าไปได้ ซึ่งก็คงแปลว่าจะอ่านหนังสือ\nก็ไม่ได้เลย"

n "\nฉันคงได้เป็นบ้าแน่ ๆ ถ้าไม่ได้อ่านหนังสือตอนอยู่ในโรงพยาบาล"

n "และเธอก็บอกว่าเธอตัวคนเดียวด้วย…"

n "พ่อแม่ของเธอตายแล้วเหรอ ไว้ต้องไปคุยกับลิลลี่ละ ฉันนึกภาพตัวเองพูดอะไรโง่ ๆ ออกไปโดยไม่ได้ตั้งใจออกเลย"

stop music fadeout 2.0

nvl clear
nvl hide dissolve

show hanako emb_timid_close
with charachange

window show

ha "ขะ-ขอบคุณนะฮิซาโอะ"

show hanako emb_downtimid_close
with charachange

ha "ฉะ-ฉันแทบไม่เคยเล่าเรื่องนี้ให้ใครฟังเลย"

hi "เอาจริง ๆ ฉันเองก็แทบไม่เคยเล่าเรื่อง… อะไรของฉันให้ใครฟังเลยเหมือนกัน"

show hanako cover_smile_close
with charachange

ha "ถะ-ถ้างั้น ฉันก็จะไม่บอก ค-ใครเหมือนกัน"

hi "ตกลงตามนั้น"

play sound sfx_warningbell

"ฉันเปลี่ยนท่าที่กุมมือเธอเป็นจับมือสัญญา ประจวบเหมาะกับเสียงระฆังเตือนหมดเวลาดังลอดผ่านหน้าต่างเข้ามาพอดี"

hi "ถ้างั้น กลับห้องเรียนกันเลยเนอะ"

show hanako basic_bashful_close
with charachange

ha "อะ-อื้ม"
$ renpy.music.set_volume(1.0, 0.0, channel="music")

window hide

return

#-------------
