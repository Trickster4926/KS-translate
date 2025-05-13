init -3 python:
    # this is the master language so it lives at init level -3, not -2 like the others
    #everything in here inherits, if a language doesn't set it the th version is used

    ### THAI

    init_language("th")

    displayDict["th"].styleoverrides = {"font": "LayijiMahaniyomV1_61.ttf",
                                        "language": "thai",
                                        "line_spacing": 0}

    displayDict["th"].timeformat = "%b %d, %H:%M"

    displayDict["th"].selector_padding = 0 # some fonts need this to be set to a nonzero amount on 6.16 or the library etc will overflow
    displayDict["th"].nvl_paragraph_distance = 10 # This needs to be set far lower for some fonts due to a particular bug in 6.16. Ignored in 6.10 releases.

    displayDict["th"].sayfont = mainfont

    displayDict["th"].quote_outer_opth = u"“"
    displayDict["th"].quote_outer_close = u"”"
    displayDict["th"].quote_inner_opth = u"‘"
    displayDict["th"].quote_inner_close = u"’"

    displayDict["th"].activeLanguage = "Thai"
    displayDict["th"].allLanguages = {}
    displayDict["th"].allLanguages["th"] = displayDict["th"].activeLanguage
    displayDict["th"].allLanguages["en"] = "English"
    displayDict["th"].allLanguages["de"] = "German"
    displayDict["th"].allLanguages["it"] = "Italian"
    displayDict["th"].allLanguages["fr"] = "Frthch"
    displayDict["th"].allLanguages["es"] = "Spanish"
    displayDict["th"].allLanguages["jp"] = "Japanese"

    displayDict["th"].act_term = u"องก์"
    displayDict["th"].window_name = u"Katawa Shoujo"

    displayDict["th"].main_menu_start = u"เริ่ม"
    displayDict["th"].main_menu_load = u"โหลด"
    displayDict["th"].main_menu_extra = u"คลัง"
    displayDict["th"].main_menu_config = u"ตั้งค่า"
    displayDict["th"].main_menu_quit = u"ออก"

    displayDict["th"].game_menu_return = u"กลับ"
    displayDict["th"].game_menu_show = u"ดูรูป"
    displayDict["th"].game_menu_history = u"ประวัติข้อความ"
    displayDict["th"].game_menu_skip = u"โหมดข้าม"
    displayDict["th"].game_menu_auto = u"โหมดออโต้"
    displayDict["th"].game_menu_config = u"ตั้งค่า"
    displayDict["th"].game_menu_save = u"บันทึก"
    displayDict["th"].game_menu_load = u"โหลด"
    displayDict["th"].game_menu_main = u"หน้าหลัก"
    displayDict["th"].game_menu_quit = u"ออก"
    displayDict["th"].game_menu_current_scene = u"ฉาก"
    displayDict["th"].game_menu_current_music = u"เพลง"
    displayDict["th"].game_menu_replay_indicator = u"เล่นซ้ำ"

    displayDict["th"].return_button_text = u"กลับ"

    displayDict["th"].hdisabled_label = u"ปิดเนื้อหาสำหรับผู้ใหญ่"
    displayDict["th"].config_page_caption = u"ตัวเลือก"
    displayDict["th"].config_fullscreen_label = u'เต็มหน้าจอ'
    displayDict["th"].config_transitions_label = u'ปิดการใช้งานเปลี่ยนฉาก'
    displayDict["th"].config_skip_unseen_label = u'ข้ามข้อความที่ไม่ได้อ่าน'
    displayDict["th"].config_skip_after_choice_label = u'ข้ามตัวเลือก'
    displayDict["th"].config_textspeed_label = u'ความเร็วข้อความ'
    displayDict["th"].config_afmspeed_label = u'ดีเลย์โหมดออโต้'
    displayDict["th"].config_musicvol_label = u"ระดับเสียงเพลง"
    displayDict["th"].config_musicvol_jukebox_label = u"Vol."
    displayDict["th"].config_sfxvol_label = u"ระดับเสียงประกอบ"
    displayDict["th"].config_sfxtest_label = u"ทดสอบ"
    displayDict["th"].config_gamepad_label = u"แป้นลัด…"

    displayDict["th"].config_language_sel = u"ภาษา…"
    displayDict["th"].config_language_caption = u"ตั้งค่า > ภาษา"
    displayDict["th"].config_language_restart_note = "หมายเหตุ: การเปลี่ยนภาษาขณะเล่นจะทำให้เกมย้อนกลับไปยังโหนดล่าสุด"

    displayDict["th"].gamepad_caption = u"ตั้งค่า > แป้นลัด"
    displayDict["th"].gamepad_key_na = u"ยังไม่ได้ตั้งค่า"
    displayDict["th"].gamepad_request_key = u"กดปุ่มที่ต้องการตั้งค่า “%s” \nคลิกที่เมาส์หรือเลือกปุ่มเพื่อล้างการตั้งค่าปุ่ม"

    displayDict["th"].yesno_yes = u"ใช่"
    displayDict["th"].yesno_no = u"ไม่"
    displayDict["th"].yesno_okay = u"ต่อ"
    displayDict["th"].yesno_savesuccess = u"บันทึกแล้ว"
    displayDict["th"].yesno_quit = u"ต้องการออกจากเกม\nใช่หรือไม่"
    displayDict["th"].yesno_return_to_main = u"ต้องการกลับไปที่หน้าหลัก\nใช่หรือไม่"
    displayDict["th"].save_page_caption = u"บันทึก"
    displayDict["th"].new_save_button = u"สร้างบันทึกใหม่"
    displayDict["th"].load_page_caption = u"โหลด"
    displayDict["th"].yesno_load_in_game = u"ต้องการไปยังฉากนี้ในขณะนี้\nใช่หรือไม่"
    displayDict["th"].yesno_save_overwrite = u"ต้องการบันทึกซ้อนทับข้อมูลนี้\nใช่หรือไม่"
    displayDict["th"].yesno_delete_savegame = u"ต้องการลบข้อมูลการบันทึกนี้\nใช่หรือไม่"
    displayDict["th"].play_time_label = u"เวลาที่เล่นไปทั้งหมด"
    displayDict["th"].show_manual_saves = u"บันทึก"
    displayDict["th"].show_auto_saves = u"บันทึกอัตโนมัติ"

    displayDict["th"].text_history_caption = u"ประวัติข้อความ"
    displayDict["th"].text_history_note = u"หมายเหตุ"

    displayDict["th"].extra_menu_caption = "คลัง"
    displayDict["th"].extra_music_button_label = "กล่องดนตรี"
    displayDict["th"].extra_gallery_button_label = "ภาพ"
    displayDict["th"].extra_scene_button_label = "ห้องสมุด"
    displayDict["th"].extra_omake_button_label = "พิเศษ"
    displayDict["th"].extra_opening_button_label = "โรงหนัง"
    displayDict["th"].commentary_label = "แสดงข้อความเพิ่มเติม"

    displayDict["th"].video_page_caption = "คลัง > โรงหนัง"


    displayDict["th"].music_page_caption = "คลัง > กล่องดนตรี"
    displayDict["th"].music_stop_button_text = "หยุด"
    displayDict["th"].music_now_playing = "ขณะนี้กำลังเล่น"

    displayDict["th"].gallery_page_caption = "คลัง > ภาพ"
    displayDict["th"].gallery_onelocked = "เหลืออีก 1 ภาพที่ยังไม่ได้ปลดล็อก"
    displayDict["th"].gallery_manylocked = "เหลืออีก %d ภาพที่ยังไม่ได้ปลดล็อก"
    displayDict["th"].gallery_singlelocked = "เหลืออีก %d จาก %d ที่ยังไม่ได้ปลดล็อก"
    displayDict["th"].gallery_num_page_prefix = "หน้าที่"
    displayDict["th"].gallery_num_page_error = "ไม่มีภาพให้แสดง"

    displayDict["th"].scene_page_caption = "คลัง > ห้องสมุด"
    displayDict["th"].scene_completion_label = "เล่นแล้ว %s%%"
    displayDict["th"].scene_playthrough_label = "ใช้รีเพลย์โฟล์ว (Replay Flow) (แนะนำ)"
    displayDict["th"].scene_launch_path = "ต้องการเริ่มเล่นทั้งรูทใหม่\nใช่หรือไม่"

    displayDict["th"].joy_left = "ซ้าย"
    displayDict["th"].joy_right = "ขวา"
    displayDict["th"].joy_up = "ขึ้น"
    displayDict["th"].joy_down = "ลง"
    displayDict["th"].joy_dismiss = "ตัวเลือก/อ่านต่อ"
    displayDict["th"].joy_rollback = "ประวัติข้อความ"
    displayDict["th"].joy_holdskip = "กดค้างเพื่อข้าม"
    displayDict["th"].joy_toggleskip = "โหมดข้าม"
    displayDict["th"].joy_hide = "แสดงภาพ"
    displayDict["th"].joy_menu = "แสดงเมนู"

    ##Names

    displayDict["th"].name_hi = "ฮิซาโอะ"

    displayDict["th"].name_ha = "ฮานาโกะ"
    displayDict["th"].name_emi = "เอมิ"
    displayDict["th"].name_rin = "ริน"
    displayDict["th"].name_li = "ลิลลี่"
    displayDict["th"].name_shi = "ชิซูเนะ"
    displayDict["th"].name_mi = "มิช่า"

    displayDict["th"].name_ke = "เคนจิ"
    displayDict["th"].name_mu = "มุโต้"
    displayDict["th"].name_nk = "พยาบาล"
    displayDict["th"].name_no = "โนมิยะ"
    displayDict["th"].name_yu = "ยูโกะ"
    displayDict["th"].name_sa = "ซาเอะ"
    displayDict["th"].name_aki = "อากิระ"
    displayDict["th"].name_hh = "ฮิเดอากิ"
    displayDict["th"].name_hx = "จิโกโร"
    displayDict["th"].name_emm = "เมโกะ"
    displayDict["th"].name_sk = "พนักงานร้าน"
    displayDict["th"].name_mk = "มิกิ"

    displayDict["th"].name_mystery = "???"

    displayDict["th"].name_ha_ = "สาวที่ผมสีม่วง"
    displayDict["th"].name_emi_ = "สาวที่ผมทวินเทล"
    displayDict["th"].name_rin_ = "สาวที่ดูพิลึก"
    displayDict["th"].name_li_ = "สาวที่ผมเป็นลอน"
    displayDict["th"].name_mi_ = "สาวที่หัวเราะ"
    displayDict["th"].name_ke_ = "เพื่อนร่วมหอใส่แว่น"
    displayDict["th"].name_mu_ = "ชายตัวสูง"
    displayDict["th"].name_yu_ = "บรรณารักษ์"
    displayDict["th"].name_no_ = "ชายผมสีเทา"
    displayDict["th"].name_sa_ = "เจ้าของหอศิลป์"
    displayDict["th"].name_aki_ = "คนที่แต่งตัวดูดี"
    displayDict["th"].name_nk_ = "ชายที่ยิ้ม"
    displayDict["th"].name_hh_ = "สาวตัวบาง"
    displayDict["th"].name_emm_ = "สาวถักเปีย"
    displayDict["th"].name_hx_ = "ชายร่างใหญ่"

    displayDict["th"].videos = (("ฉากเปิด", "video/op_1.mkv"),
                                ("เอมิ", "video/tc_act2_emi.mkv"),
                                ("ฮานาโกะ", "video/tc_act2_hanako.mkv"),
                                ("ลิลลี่", "video/tc_act2_lilly.mkv"),
                                ("ริน", "video/tc_act2_rin.mkv"),
                                ("ชิซูเนะ", "video/tc_act2_shizune.mkv"),
                               )



    # scenes available in the extras -> scene select menu. Name, label, description, path (path may also be a tuple).
    # Now also doubles as a lookup list for the actual scene names. Display in the extras can be suppressed
    # by setting the third value in the tuple to False. Suppression doesn't work in DQN mode.
    # Note that Ren'Py doesn't like non-ASCII characters in scene titles if the titles are not unicode strings
    displayDict["th"].s_scenes = (("บทนำ", rp_actmark, rp_actmark, ("องก์ 1","บทนำ")),
                                    ("ตัวเย็น", "NOP1", "ในวันที่หิมะตกอันหนาวเย็นนั้นฝันของฮิซาโอะกำลังจะเป็นจริง ทว่าถูกโรคหัวใจเล่นงานเสียก่อน", ("องก์ 1","บทนำ")),
                                    ("คนรอบตัว", "NOP2", "ฮิซาโอะได้รู้เรื่องโรงเรียนยามากุที่เขาจะต้องใช้ชีวิต ม. ปลาย ที่นั่น", ("องก์ 1","บทนำ")),
                                    ("องก์ 1: ค่าคาดหมายของชีวิต", rp_actmark, rp_actmark, "องก์ 1"),
                                    ("ทางเปลี่ยนผ่าน", "A1", "ฮิซาโอะมาที่โรงเรียนยามากุเป็นครั้งแรกและพบกับครูประจำชั้นที่ชื่อมุโต้", "องก์ 1"),
                                    ("แสดงตัว", "A2", "หลังจากที่แนะนำตัวกับชั้นเรียนก็ได้พบกับหัวหน้าห้องและล่ามของเธอ", "องก์ 1"),
                                    ("ณ ห้องพยาบาล", "A3", "มิช่าและชิซูเนะพาฮิซาโอะไปที่โรงอาหาร และไปพบกับพยาบาล", "องก์ 1"),
                                    ("ห้องปริศนา", "A4", "ฮิซาโอะย้ายมาที่ห้องใหม่ของเขาและได้พบกับเพื่อนร่วมหอที่ชื่อเคนจิ", "องก์ 1"),
                                    ("มีเรื่องจะคุย", "A5", "ชิซูเนะกับมิช่าบอกฮิซาโอะเรื่องงานเทศกาลที่จะจัดขึ้นพร้อมชวนไปกินข้าวเที่ยง", "องก์ 1"),
                                    ("กล้าได้กล้าเสี่ยง", "A6", "ชิซูเนะแข่งครองโลกกับฮิซาโอะในบอร์ดเกม{i}ริสก์{/i} (Risk)", "องก์ 1"),
                                    ("ชุดอุ่นกาน้ำชาเทียม", "A7", "ฮิซาโอะหลงทางระหว่างที่กำลังหาทางไปห้องสมุดจนได้พบกับลิลลี่ในห้องเรียนที่ไม่ได้ใช้แล้ว", "องก์ 1"),
                                    ("ห้องสมุดร่วม", "A8", "เมื่อหาห้องสมุดเจอก็ได้พบกับฮานาโกะ แต่ทำให้เธอตกใจหนีไป", "องก์ 1"),
                                    ("ประหลาดพันลึก", "A9", "เคนจิเผยความลับอันดำมืดของยามากุ", "องก์ 1"),
                                    ("ทฤษฎีวิวัฒน์ข้าวเที่ยง", "A10", "ชิซูเนะกับมิช่าตามตื๊อให้ฮิซาโอะเข้าสภานักเรียน ก่อนจะคุยกันเรื่องข้าวเที่ยง", "องก์ 1"),
                                    ("ตื้อ ติด ตึง", "A11_1", "ระหว่างที่ไปโรงอาหารกับมิช่าและชิซูเนะ เอมิก็ชนเข้ากับฮิซาโอะในโถงทางเดิน", "องก์ 1"),
                                    ("แรกพบสบตา", "A11_2", "เอมิที่กำลังวิ่งชนกับฮิซาโอะที่กำลังไปโรงอาหารกับมิช่าและชิซูเนะ", "องก์ 1"),
                                    ("ทางเบี่ยงข้างหน้า", "A12", "ชิซูเนะและมิช่าพาฮิซาโอะไปที่ร้านอาหารโปรดของพวกเธอที่ชื่อ{i}เซี่ยงไฮ้{/i}", "องก์ 1"),
                                    ("จิบ (ตอน 1)", "A13", "มื้อเที่ยงอันแสนสงบของฮิซาโอะกับลิลลี่และฮานาโกะ", "องก์ 1"), # there is no A14
                                    ("คนเราเจอหลายอย่าง", "A15", "มุโต้มาถ่ายทอดความมุ่งมั่นให้ฮิซาโอะผ่านบทสนทนา ก่อนฮิซาโอะจะถูกมิช่ามาลากตัวไปทำงาน", "องก์ 1"),
                                    ("มื้อเที่ยงแบบส่วนตัว", "A16", "ระหว่างที่กำลังหาอุปกรณ์ ฮิซาโอะก็ได้พบกับสาวประหลาดคนหนึ่งในห้องศิลปะ", "องก์ 1"),
                                    ("หยุดตรวจ", "A17", "พยาบาลเข้ามาถามฮิซาโอะระหว่างที่กำลังช่วยรินถือสี", "องก์ 1"),
                                    ("อีกเขียวหนึ่ง", "A18", "ฮิซาโอะดูรินวาดกำแพง", "องก์ 1"),
                                    ("สาวนักวิ่ง", "A19", "ฮิซาโอะเจอกับเอมิที่ลู่วิ่งตอนที่เขานึกพยายามลองออกกำลังกายตอนเช้า", "องก์ 1"),
                                    ("สบู่", "A20", "เคนจิซุ่มโจมตีฮิซาโอะในห้องอาบน้ำหวังยืมเงิน", "องก์ 1"),
                                    ("สงครามเย็น", "A21", "ชิซูเนะปะทะคารมกับลิลลี่ด้วยเรื่องงบงาน", "องก์ 1"),
                                    ("ใช้ได้ไม่ได้", "A22", "ชิซูเนะกับมิช่าพยายามลากให้ฮิซาโอะเข้าร่วมสภานักเรียน", "องก์ 1"),
                                    ("ขอบฟ้าเหตุการณ์", "A22_2", "ชิซูเนะกับมิช่าพยายามลากให้ฮิซาโอะเข้าร่วมสภานักเรียน", "องก์ 1"),
                                    ("ทำให้เกินร้อย", "A23_1", "ชิซูเนะสาธยายหน้าที่อันทรงเกียรติของสภานักเรียนให้ฮิซาโอะฟัง", "องก์ 1"),
                                    ("สิ่งที่ทำได้", "A23_2", "เมื่อรอดจากเงื้อมมือชิซูเนะและมิช่ามาได้แล้วฮิซาโอะก็มาช่วยริน", "องก์ 1"),
                                    ("ระบายสีตามตัวเลข", "A24", "ฮานาโกะและฮิซาโอะช่วยห้องลิลลี่ทำแผงสำหรับงานโรงเรียน", "องก์ 1"),
                                    ("ออกกำลังกาย", "A25", "ฮิซาโอะมาวิ่งกับเอมิที่ลู่วิ่งอีกวัน", "องก์ 1"),
                                    ("หมวกล่องหน", "A26", "เคนจิแนะนำฮิซาโอะเรื่องการเข้าสังคมด้วยประสบการณ์จากวงใน", "องก์ 1"),
                                    ("โชคดีที่เป็นเจ้าบ้าน", "A26_1", "ชิซูเนะและมิช่ามากล่อมฮิซาโอะที่กำลังจะออกห้องไปเรียน", "องก์ 1"),
                                    ("ไม่มีการฟื้นตัว", "A27", False, "องก์ 1"), #this is somewhat of a hack, and a special case
                                    ("ฟื้นตัวช้า", "A27_1", "เมื่ออาการหัวใจเต้นผิดจังหวะเริ่มดีขึ้นฮิซาโอะก็มาเข้าเรียน", "องก์ 1"),
                                    ("ไม่มีการฟื้นตัว", "A27_2", "ฮิซาโอะลากสังขารมาที่ห้องเรียนหลังจากที่ถูกสภานักเรียนเกลี้ยกล่อม", "องก์ 1"),
                                    ("ไม่มีข้าวเที่ยงฟรี", "A28", "ฮิซาโอะถูกประกบตัวพาไปที่สภานักเรียนเป็นการทำงานวันแรก", "องก์ 1"),
                                    ("เท้าปาก", "A29", "เอมิลากฮิซาโอะมาที่ดาดฟ้าเพื่อกินข้าวเที่ยงกับริน", "องก์ 1"),
                                    ("ไปไหนให้ระวัง", "A30", "ฮิซาโอะและลิลลี่ออกไปซื้อของและพบกับรินที่ดูสับสนระหว่างทางกลับ", "องก์ 1"),
                                    ("แรงสนับสนุน", "A31", "ฮิซาโอะมาเรียนวันเสาร์เป็นครั้งแรก ปิดด้วยการคุยกับมุโต้", "องก์ 1"),
                                    ("สุนทรียะ", "A32", "เอมิเห็นฮิซาโอะที่ว่าง ๆ จึงเกณฑ์มาช่วยรินอีกครั้ง", "องก์ 1"),
                                    ("เจ็บปวดสร้างสรรค์", "A33", "ฮิซาโอะพบกับครูสอนศิลปะที่ชื่อโนมิยะในขณะที่รินกำลังวาดกำแพงอยู่", "องก์ 1"),
                                    ("การออกกำลังกายที่ถูกต้อง", "A34", "เอมิกับฮิซาโอะคุยถึงเรื่องความสำคัญของการรักษาสุขภาพ", "องก์ 1"),
                                    ("จิบ (ตอน 2)", "A35", "ฮิซาโอะเดินไปรอบ ๆ โรงเรียนฆ่าเวลาเล่น", "องก์ 1"),
                                    ("ล่อซื้อที่เซี่ยงไฮ้", "A36", "การแข่งขันน้ำชาและเค้กกับชิซูเนะและมิช่าที่ร้านเซี่ยงไฮ้", "องก์ 1"),
                                    ("เงียบงัน", "A37", "ฮานาโกะและฮิซาโอะอ่านหนังสือในวันงานโรงเรียน", "องก์ 1"),
                                    ("อย่าล่ก", "A38", "หลังฮิซาโอะตื่นมาในวันงานเคนจิก็เข้ามาบ่น", "องก์ 1"),
                                    ("เทศกาลละ!", "A39", "เอมิเห็นฮิซาโอะกินของทอดจึงคอยตามติดเป็นการลงโทษ", "องก์ 1"),
                                    ("Nc5xb3", "A42", "เมื่อไม่ได้ไปช่วยลิลลี่ที่แผง ฮิซาโอะจึงตามหาฮานาโกะที่งานโรงเรียน", "องก์ 1"),
                                    ("เคลื่อนไหว", "H2", "หลังเสร็จงานแล้วลิลลี่ก็พาฮานาโกะและฮิซาโอะมาเลี้ยงน้ำชาที่ร้านเซี่ยงไฮ้", "องก์ 1"), # the titlecard comes after this so it IS part of องก์ 1
                                    ("สัญญาแห่งกาลเวลา", "A41", "หลังเช้าอันวุ่นวายที่แผง ฮิซาโอะพาลิลลี่ออกตามหาฮานาโกะ", "องก์ 1"),
                                    ("ใจลอยไปตามก้อนเมฆ", "A40", "ฮิซาโอะอยู่เป็นเพื่อนรินและภาพเขียนกำแพงของเธอ", "องก์ 1"),
                                    ("ปาบอล", "A44", "ฮิซาโอะใช้เวลาอยู่กับชิซูเนะและมิช่าตามที่พูดไว้", "องก์ 1"),
                                    ("ซอยตัน", "A43", "เคนจิและฮิซาโอะปิกนิกกันที่ดาดฟ้าอย่างลูกผู้ชายและไม่ไปร่วมงานโรงเรียน", "องก์ 1"),
                                    ("องก์ 2: รูปร่าง", rp_actmark, rp_actmark, ("องก์ 2","เอมิ")),
                                    ("วิ่งรอบเช้า", "E3", "ฮิซาโอะมาวิ่งกับเอมิรอบเช้าเป็นครั้งแรก ก่อนจะมีครั้งต่อไปอีกหลายครั้ง", ("องก์ 2","เอมิ")),
                                    ("เมฆขาว เดินทางข้ามเวลา แก", "E4", "ฮิซาโอะมากินข้าวเที่ยงที่ดาดฟ้ากับเอมิและรินอีกครั้ง ก่อนจะถูกรบเร้าให้มาดูงานแข่งวิ่งของเอมิ", ("องก์ 2","เอมิ")),
                                    ("คำถามที่ต้องการคำตอบ!", "E5", "เอมิกับฮิซาโอะคุยกันเรื่อยเปื่อย ก่อนฮิซาโอะจะถามเรื่องความสัมพันธ์ระหว่างเอมิและรินเพิ่มเติม", ("องก์ 2","เอมิ")),
                                    ("ครั้งที่สองจะแย่ที่สุด", "E6", "มาวิ่งรอบเช้าเป็นครั้งที่สอง ฮิซาโอะแทบเป็นแทบตายอยู่บนลู่วิ่ง", ("องก์ 2","เอมิ")),
                                    ("รักษาสุขภาพให้ดี", "E7", "ฮิซาโอะมาหาพยาบาลกับเอมิ ก่อนจะได้รู้ว่าที่จริงทั้งสองคนรู้จักกันมาสักพักแล้ว", ("องก์ 2","เอมิ")),
                                    ("งานแข่ง", "E8", "วันงานแข่ง ตัวตนอีกด้านของเอมิถูกเปิดเผย", ("องก์ 2","เอมิ")),
                                    ("เพลา ๆ บ้างนะ", "E9", "ฮิซาโอะเล่าถึงอาการเจ็บหน้าอกแล้วถูกพยาบาลเทศน์", ("องก์ 2","เอมิ")),
                                    ("ล่องเรือออกทะเล", "E10", "ฮิซาโอะคุยเรื่องอนาคตในฐานะโจรสลัดกับเอมิ ก่อนจะถูกขัดอารมณ์ด้วยจดหมายจากอิวานาโกะ", ("องก์ 2","เอมิ")),
                                    ("ปากพระร่วง", "E11", "เอมิและรินพาฮิซาโอะไปปิกนิก แต่แล้วฝนก็ตกจนแผนล่ม", ("องก์ 2","เอมิ")),
                                    ("คนขาด", "E12", "ฮิซาโอะไปที่ลู่วิ่งอย่างเคย ทว่าไม่พบเอมิ", ("องก์ 2","เอมิ")),
                                    ("แวะมาหา", "E13", "ฮิซาโอะมาเยี่ยมไข้เอมิ และกลายเป็นอย่างอื่นไปทันที", ("องก์ 2","เอมิ")),
                                    ("เช้าถัดมา", "E14", "ฮิซาโอะนึกถึงเรื่องเมื่อตอนเย็นและตัดสินใจทำบางอย่างเพื่อช่วยเอมิ", ("องก์ 2","เอมิ")),
                                    ("จุดเริ่มต้น (ที่แท้จริง)", "E15", "มื้อเที่ยงบนดาดฟ้าอย่างเคยโดยไร้ริน", ("องก์ 2","เอมิ")),
                                    ("องก์ 3: มุมมอง", rp_actmark, rp_actmark, ("องก์ 3","เอมิ")),
                                    (u"วิดกระยาสาด", "E16", "มุโต้คุยกับฮิซาโอะถึงเรื่องอนาคตของเขา", ("องก์ 3","เอมิ")),
                                    ("นิยาม", "E17", "เอมิและฮิซาโอะไปปิกนิกอีกครั้ง คราวนี้ฟ้าฝนเป็นใจแล้ว", ("องก์ 3","เอมิ")),
                                    ("หินล่องหน", "E18", "กลับมาวิ่งรอบเช้าอีกครั้ง เหมือนเดิม... หรือเปล่า", ("องก์ 3","เอมิ")),
                                    ("ข้าวเที่ยงและวิทยาศาสตร์", "E19", "ฮิซาโอะคุยกับมุโต้อีกครั้งเรื่องอนาคตในสายวิทยาศาสตร์", ("องก์ 3","เอมิ")),
                                    ("ลุก แล้วล้ม แล้วลุกอีก", "E20", "เสียงปลายสายจากเอมิทำให้ฮิซาโอะต้องมาหาที่ห้อง จนต้องตกใจกับสองเรื่อง", ("องก์ 3","เอมิ")),
                                    ("ห้องเก็บของ", "E21", "เอมิชวนฮิซาโอะให้มาที่ห้องเก็บของของสนาม", ("องก์ 3","เอมิ")),
                                    ("แผนหลังเลิกเรียน", "E22", "เอมิคุยกับฮิซาโอะอย่างจริงจังถึงเรื่องสอบที่จะมาถึง", ("องก์ 3","เอมิ")),
                                    ("หลุดจาก", "E23", "ฮิซาโอะนั่งทบทวนเรื่องความสัมพันธ์กับเอมิ", ("องก์ 3","เอมิ")), # renamed this one from "Disconnected" - "Disconnect" is the name of Rin's องก์ 2
                                    ("ปวดหลอน", "E24", "ฮิซาโอะพยายามแสดงความเป็นห่วงให้เอมิ ทว่าไปได้ไม่สวยดังหวังนัก", ("องก์ 3","เอมิ")),
                                    ("คลางแคลงปรากฏเมื่อโต้แย้ง", "E25", "ฮิซาโอะสับสนในท่าทีของเอมิและคำชวนไปบ้านของเธอ", ("องก์ 3","เอมิ")),
                                    (u"ทายซิใครเอ่ย... ช่างเถอะ", "E26", "มื้อเย็นที่บ้านอิบาราซากิ", ("องก์ 3","เอมิ")),
                                    ("ขอเอาใหม่", "E27", "เรื่องมาถึงบทสรุปที่ลู่วิ่ง", ("องก์ 3","เอมิ")),
                                    ("องก์ 4: เคลื่อนที่", rp_actmark, rp_actmark, ("องก์ 4","เอมิ")),
                                    ("วืด", "E28", "ฮิซาโอะนึกสงสัยว่าเอมิจงใจหลบหน้าเขาหรือเปล่า", ("องก์ 4","เอมิ")),
                                    ("ทอยเซฟ", "E29", "เรื่องมาถึงบทสรุปที่ดาดฟ้า", ("องก์ 4","เอมิ")),
                                    ("เสียงเพรียกจากอดีต", "E30", "ฮิซาโอะไปเยี่ยมที่สุสานกับเอมิและแม่ของเธอ", ("องก์ 4","เอมิ")),
                                    ("สรรเสริญถุงเท้า", "E31", "เซ็กส์ ยา แต่ไม่มีร็อกแอนด์โรล", ("องก์ 4","เอมิ")),
                                    ("ฟันขาว", "E32", "ฮิซาโอะตื่นมาและมีเอมินอนอยู่ข้าง ๆ ", ("องก์ 4","เอมิ")),
                                    ("องก์ 2: ซ่อนหา", rp_actmark, rp_actmark, ("องก์ 2","ฮานาโกะ")),
                                    ("เข้าเมือง", "H3", "ซื้อของที่ร้านสะดวกซื้อกับฮานาโกะ", ("องก์ 2","ฮานาโกะ")),
                                    ("ใบชา", "H4", "ฮานาโกะชวนฮิซาโอะมากินข้าวเที่ยงกับลิลลี่", ("องก์ 2","ฮานาโกะ")),
                                    ("คำสารภาพในที่ทำงาน", "H5_1", "ฮิซาโอะและมิช่าคุยกันเรื่องสถานการณ์ที่ดูไม่สู้ดีนักของฮานาโกะ", ("องก์ 2","ฮานาโกะ")),
                                    ("หมากรุกและสไลด์เดอร์", "H5_2", "ฮิซาโอะโดดจากสภานักเรียนมาอ่านหนังสือกับฮานาโกะ", ("องก์ 2","ฮานาโกะ")),
                                    ("ตื่นเถิดชาวไทย", "H6", "ลิลลี่ชวนมาปาร์ตี้น้ำชาหลังเลิกเรียน", ("องก์ 2","ฮานาโกะ")),
                                    ("แมด แฮตเตอร์", "H7", "ฮิซาโอะได้พบกับฮานาโกะและลิลลี่ที่ห้องลิลลี่ในปาร์ตี้น้ำชา", ("องก์ 2","ฮานาโกะ")),
                                    ("การเปลี่ยนแปลงเล็ก ๆ ", "H8", "เคนจิถูกบังคับให้ต้องคืนเงิน", ("องก์ 2","ฮานาโกะ")),
                                    ("ขาดไม่เคยมา", "H9", "ฮิซาโอะและลิลลี่คุยกันเรื่องเวลาเรียนของฮานาโกะ", ("องก์ 2","ฮานาโกะ")),
                                    ("การแลกเปลี่ยนที่เท่าเทียม", "H10", "หลังจากที่ฮิซาโอะเล่าเรื่องหัวใจของตัวเองให้ฟัง ฮานาโกะก็เริ่มเล่าเรื่องอดีตของตัวเอง", ("องก์ 2","ฮานาโกะ")),
                                    ("องก์ 3: เข้าป้อม", rp_actmark, rp_actmark, ("องก์ 3","ฮานาโกะ")),
                                    ("คำเชิญ", "H11", "Lilly finds Hisao cleaning up the Tea Room and tells him about ฮานาโกะ's birthday.", ("องก์ 3","ฮานาโกะ")),
                                    ("Shady Encounter", "H12", "An unexpected chat with Miki while reminiscing about the past.", ("องก์ 3","ฮานาโกะ")),
                                    ("Antiques and Pie", "H13", "Lilly and Hisao shop for a present in the city.", ("องก์ 3","ฮานาโกะ")),
                                    ("ร่วงหล่น", "H14", "ฮานาโกะ has a panic attack during class.", ("องก์ 3","ฮานาโกะ")),
                                    ("Treading Softly", "H15", "Lilly has bad news to discuss with Hisao and ฮานาโกะ.", ("องก์ 3","ฮานาโกะ")),
                                    ("Reaching Out", "H16", "Hisao reaches out to a withdrawn ฮานาโกะ.", ("องก์ 3","ฮานาโกะ")),
                                    ("One More Year", "H17", "Our trio is joined by an unexpected guest as they celebrate ฮานาโกะ's birthday party.", ("องก์ 3","ฮานาโกะ")),
                                    ("One Piece of Paper", "H18", "Hisao enjoys his first hangover, before receiving a troubling letter.", ("องก์ 3","ฮานาโกะ")),
                                    ("Stripes and Solids", "H19", "Heart-to-heart during a game of pool.", ("องก์ 3","ฮานาโกะ")),
                                    ("Beginning of the End", "H20", "Lilly's departure for her trip.", ("องก์ 3","ฮานาโกะ")),
                                    ("องก์ 4: Scars", rp_actmark, rp_actmark, ("องก์ 4","ฮานาโกะ")),
                                    ("Truancy", "H21", "Lunch with the Student Council and worry about ฮานาโกะ shutting herself in.", ("องก์ 4","ฮานาโกะ")),
                                    ("Faraway Presence", "H22", "Hisao phones Lilly for advice after ฮานาโกะ secludes herself for another day.", ("องก์ 4","ฮานาโกะ")),
                                    ("Misstep", "H23", "Hisao tries to pull ฮานาโกะ out of her room, with startling results.", ("องก์ 4","ฮานาโกะ")),
                                    ("Cut Petals", "H24", "Hisao finds his future relationship with ฮานาโกะ prematurely ended.", ("องก์ 4","ฮานาโกะ")),
                                    ("Continuing Melody", "H25", "ฮานาโกะ returns to class, to Hisao's relief.", ("องก์ 4","ฮานาโกะ")),
                                    ("Shanghai Studiousness", "H26", "Attempting to avoid distractions, Hisao tries studying at the Shanghai.", ("องก์ 4","ฮานาโกะ")),
                                    ("His Past", "H27", "In an attempt to come closer to ฮานาโกะ, Hisao shares a part of his past with her.", ("องก์ 4","ฮานาโกะ")),
                                    ("City Rendezvous", "H28", "The two share a date in the city.", ("องก์ 4","ฮานาโกะ")),
                                    ("Whispered Touch", "H29", "Hisao and ฮานาโกะ spend the night together.", ("องก์ 4","ฮานาโกะ")),
                                    ("Indeterminate Future", "H30", "The events of the previous night weigh heavily on Hisao.", ("องก์ 4","ฮานาโกะ")),
                                    ("Adulthood", "H31", "The end of two children, the beginning of two adults.", ("องก์ 4","ฮานาโกะ")),
                                    ("องก์ 2: Past", rp_actmark, rp_actmark, ("องก์ 2","Lilly")),
                                    ("Earl Grey", "L1", "Hisao shares the first of many lunchbreaks with ฮานาโกะ and Lilly, recovering from the day before.", ("องก์ 2","Lilly")),
                                    ("A Pound Sterling", "L2", "Questioned by Kenji on Lilly's nationality, Hisao decides to investigate and finds out a great deal more.", ("องก์ 2","Lilly")),
                                    ("Presents and Presence", "L3", "While out in search of a present for ฮานาโกะ, Lilly and Hisao meet Akira and her cousin.", ("องก์ 2","Lilly")),
                                    ("Unidentified Drinking Object", "L4", "The trio hold a birthday party for ฮานาโกะ, interrupted by the surprise appearance of a sibling.", ("องก์ 2","Lilly")),
                                    ("The Day After", "L5", "Hisao and Lilly awaken and try to recuperate from the previous evening's events.", ("องก์ 2","Lilly")),
                                    ("A Brief History of Thyme", "L6", "Hisao and Lilly go to get some groceries.", ("องก์ 2","Lilly")),
                                    ("Little Wing", "L7", "A shared lunch on the roof takes an unfortunate turn.", ("องก์ 2","Lilly")),
                                    ("Bon Voyage", "L8", "Lilly and Akira get seen off as they leave for a trip to their family in Scotland.", ("องก์ 2","Lilly")),
                                    ("องก์ 3: Present", rp_actmark, rp_actmark, ("องก์ 3","Lilly")),
                                    ("Day by Day", "L9", "Hisao idly lets a day without Lilly slip by, having a talk with Mutou about Yamaku.", ("องก์ 3","Lilly")),
                                    ("Minor Discord", "L10", "Hisao has lunch with Kenji, then gives some handouts to an alarmingly silent ฮานาโกะ.", ("องก์ 3","Lilly")),
                                    ("Dissonance", "L11", "With ฮานาโกะ withdrawing into herself completely, Hisao offers what little help he can before calling Lilly.", ("องก์ 3","Lilly")),
                                    ("A World Away", "L12", "Hisao's reassured mind begins to wonder about the relationship between he and Lilly.", ("องก์ 3","Lilly")),
                                    ("Renewal", "L13", "Hisao, ฮานาโกะ, and Hideaki welcome Akira and Lilly after their return from Scotland.", ("องก์ 3","Lilly")),
                                    ("Northern Sojourn", "L14", "The trio begins their holiday in Hokkaido.", ("องก์ 3","Lilly")),
                                    ("Prelude", "L15", "A morning walk begins a chain of events.", ("องก์ 3","Lilly")),
                                    ("Crescendo", "L16", "Lilly's true feelings are told in the endless gold of the wheat fields." , ("องก์ 3","Lilly")),
                                    ("Diminuendo", "L17", "Our couple shares their first night together.", ("องก์ 3","Lilly")),
                                    ("Gray Outlook", "L18", "Confined to the summerhouse, Lilly and Hisao are forced to come to terms with their relationship.", ("องก์ 3","Lilly")),
                                    ("Rhapsody in Blue", "L19", "A bathing Hisao reflects on where he and Lilly are in life, before being joined by someone.", ("องก์ 3","Lilly")),
                                    ("The Momentary Present", "L20", "Traveling back to Yamaku, Hisao and Lilly idly talk between themselves.", ("องก์ 3","Lilly")),
                                    ("องก์ 4: Future", rp_actmark, rp_actmark, ("องก์ 4","Lilly")),
                                    ("Slow Steps 'Fore a Waltz", "L21", "Back at the school, the events of Hokkaido come to the fore.", ("องก์ 4","Lilly")),
                                    ("Pajamas and Suits", "L22", "Settling back into daily life. Akira joins the trio during one of their tea parties.", ("องก์ 4","Lilly")),
                                    ("Correct Procedure", "L23", "Hisao and Lilly arrange a date, before Akira swings by.", ("องก์ 4","Lilly")),
                                    ("Out and About", "L24", "Hisao and Lilly go on their first date, finding out about each other's pasts.", ("องก์ 4","Lilly")),
                                    ("A Morning's Reverie", "L25", "Hisao and Lilly discuss their ambitions for the future.", ("องก์ 4","Lilly")),
                                    ("Blackout", "L26", "The trio muse on the upcoming holidays, before Hisao experiences sight as Lilly does.", ("องก์ 4","Lilly")),
                                    ("Context", "L27", "Hisao gets called out by Akira and the two talk about her sibling.", ("องก์ 4","Lilly")),
                                    ("A Faraway Future", "L28", "Lilly reveals her family's offer to join them in Scotland.", ("องก์ 4","Lilly")),
                                    ("Farewell", "L29", "Farewells to Akira and Lilly the evening before they leave Japan.", ("องก์ 4","Lilly")),
                                    ("False Cadence", "L30", "Hisao rushes to confront Lilly, realizing her conflict.", ("องก์ 4","Lilly")),
                                    ("Under a Maudlin Sky", "L31", "Waking in the hospital ward, Hisao struggles to come to terms with his life.", ("องก์ 4","Lilly")),
                                    ("Under a Bright Sky", "L32", "Lilly rejoins Hisao, the two beginning their life together anew.", ("องก์ 4","Lilly")),
                                    ("Forwards, with Gusto!", "L33", "Lilly and Hisao see off Akira.", ("องก์ 4","Lilly")),
                                    ("องก์ 2: Disconnect", rp_actmark, rp_actmark, ("องก์ 2","Rin")),
                                    ("A Wider Field of Vision", "R1", "Hisao spends a lunch break with Rin watching clouds on the rooftop.", ("องก์ 2","Rin")),
                                    ("Studies in Grayscale", "R2", "Rin and Hisao draw portraits of each other at his first art club meeting.", ("องก์ 2","Rin")),
                                    (u"Interstitial", "R3", "Kenji lends a “borrowed” book to Hisao.", ("องก์ 2","Rin")),
                                    ("Self Study", "R4", "Misha and Shizune catch Hisao meditatively doodling during class.", ("องก์ 2","Rin")),
                                    ("Hisao's Smile", "R5", "Rin talks to Hisao about his happy expressions, or lack of them.", ("องก์ 2","Rin")),
                                    ("Things You Like", "R6", "Brief musings with Yuuko about books and Yamaku.", ("องก์ 2","Rin")),
                                    ("Target Audience", "R7", "The day of the track meet. Facets of เอมิ's and Rin's personalities get revealed.", ("องก์ 2","Rin")),
                                    ("Eternity In an Hour", "R8", "Nomiya incites discussion of art during a club meeting.", ("องก์ 2","Rin")),
                                    ("Underwater and a Maple with a Name", "R9", "Rin leads Hisao into the woods, where they ponder their immediate future.", ("องก์ 2","Rin")),
                                    ("Iwanako's Regret", "R10", "A letter from Iwanako arrives.", ("องก์ 2","Rin")),
                                    ("In Her Own Image", "R11", "Hisao pushes Rin to have her own art exhibition.", ("องก์ 2","Rin")),
                                    ("Umbrella Logic Cake", "R12", "เอมิ, Hisao and Rin get rained on and seek refuge in the Shanghai.", ("องก์ 2","Rin")),
                                    ("Six Meters Closer to Heaven", "R13", "Rin and Hisao DON'T eat lunch on the roof, due to a distinct lack of เอมิ.", ("องก์ 2","Rin")),
                                    ("Indecision", "R14", "เอมิ gets rid of her cold, while Rin catches her own.", ("องก์ 2","Rin")),
                                    ("Signal Interference", "R15", "Hisao goes visit Rin in her room.", ("องก์ 2","Rin")),
                                    ("Dandelions", "R16", "Conclusions get drawn on a hilltop.", ("องก์ 2","Rin")),
                                    ("องก์ 3: Distance", rp_actmark, rp_actmark, ("องก์ 3","Rin")),
                                    ("22nd Corner", "R17", "The art club team checks out the gallery for Rin's future exhibition.", ("องก์ 3","Rin")),
                                    ("The Scent of Light", "R18", "Hisao happens upon a sleeping Rin in the art room.", ("องก์ 3","Rin")),
                                    ("Things You Can't Give Up", "R19", "เอมิ and Hisao discuss Rin's personality.", ("องก์ 3","Rin")),
                                    ("BADAAN!", "R20", "Yuuko's thoughts on motivation.", ("องก์ 3","Rin")),
                                    ("Rose-Tinted Glasses", "R21", "Nomiya expounds at length about art as a career.", ("องก์ 3","Rin")),
                                    ("The Edge of the World", "R22", "Hisao confesses to Rin and gets shot down. Or does he?", ("องก์ 3","Rin")),
                                    ("The Context of Rin", "R23", "An awkward and silent afternoon at the atelier.", ("องก์ 3","Rin")),
                                    ("Fast Forward", "R23_2", "The preparations for the exhibition settle into a strange routine.", ("องก์ 3","Rin")),
                                    ("Self-Destruction", "R24", "Rin experiments with smoking to get a fresh look at creativity.", ("องก์ 3","Rin")),
                                    ("Reverse Escapism", "R25", "Hisao takes Rin on a walk through the night streets.", ("องก์ 3","Rin")),
                                    ("Boundless", "R26", "Sae and Nomiya give Hisao some insight on artists' lives.", ("องก์ 3","Rin")),
                                    ("Delirium", "R27", "Hisao surprises a desperate Rin in the atelier.", ("องก์ 3","Rin")),
                                    ("Things You Hate", "R28", "Unpleasant aftermath of an incredible night.", ("องก์ 3","Rin")),
                                    ("Shards of Ire", "R29", "The strained relationship between the two blows apart.", ("องก์ 3","Rin")),
                                    ("องก์ 4: Dream", rp_actmark, rp_actmark, ("องก์ 4","Rin")),
                                    ("Illusions for People", "R30", "Hisao talks about his misgivings to Nomiya, to little effect.", ("องก์ 4","Rin")),
                                    ("Demused", "R31", "Hisao's patience comes to an end.", ("องก์ 4","Rin")),
                                    ("The Scene", "R32", "Meeting with Rin at the exhibition opening.", ("องก์ 4","Rin")), #R33 is just a scene block used in two other scenes, R34 is sorted later
                                    ("Wavelength", "R35", "Hisao lethargically whiles away the last day of exams.", ("องก์ 4","Rin")),
                                    ("Blue Period", "R36", "A rainy day, the 22nd Corner, and a brief history of Picasso.", ("องก์ 4","Rin")),
                                    ("The World Only You Can See", "R37", "Rin and Hisao part after the rain.", ("องก์ 4","Rin")),
                                    ("Desperate Glory", "R34", "A frantic Nomiya queries Hisao about Rin's whereabouts.", ("องก์ 4","Rin")), #moved down here so all good end path scenes are in a row
                                    ("Problems of Self-Referential Logic", "R38", "Hisao finds Rin in her hiding place, and convinces her to reconcile with Nomiya.", ("องก์ 4","Rin")),
                                    ("Measuring Shadows", "R39", "Rin's apology to the art teacher isn't well-received.", ("องก์ 4","Rin")),
                                    (u"Raison d'être", "R40", "Hisao comforts an upset Rin.", ("องก์ 4","Rin")),
                                    ("Without Breathing, Without a Sound", "R41", "On the first day of summer vacation, Rin comes to Hisao's room.", ("องก์ 4","Rin")),
                                    ("Proof of Existence", "R42", "Everything comes together on that dandelion-covered hilltop.", ("องก์ 4","Rin")),
                                    ("องก์ 2: Learning to Read", rp_actmark, rp_actmark, ("องก์ 2","Shizune")),
                                    ("Message Passing", "S8", "Shizune and Hisao explore methods of communication.", ("องก์ 2","Shizune")),
                                    ("Talk to the Hand", "S9", "Hisao begins studying a new language, and a tutor appears.", ("องก์ 2","Shizune")),
                                    ("Chinese Whispers", "S10", "Kenji manages to coerce Hisao to do a favor for him, but Hisao runs into trouble in many forms.", ("องก์ 2","Shizune")),
                                    ("Advanced Game Theory", "S11", "RISK isn't enough any more to satiate Shizune's hunger. What's worse, a new opponent makes her appearance.", ("องก์ 2","Shizune")),
                                    ("Bread, Scissors, Paper", "S12", "A lazy afternoon becomes dramatic as suddenly a piece of bread becomes an object of extreme interest.", ("องก์ 2","Shizune")),
                                    ("Interface", "S13", "Shizune and Hisao find a connection.", ("องก์ 2","Shizune")),
                                    ("Spring into Action", "S14", "Hisao has to mediate between Lilly and Shizune, but luckily things work out in the end.", ("องก์ 2","Shizune")),
                                    ("Past Imperfective", "S15", "The Student Council reminisces about past years while relaxing at the Shanghai.", ("องก์ 2","Shizune")),
                                    ("When Stars Embrace", "S16", "It's finally time for Tanabata!", ("องก์ 2","Shizune")),
                                    ("องก์ 3: Sleight of Hand", rp_actmark, rp_actmark, ("องก์ 3","Shizune")),
                                    ("Force Feedback", "S17", "Hisao finds out that Shizune is going to visit her family, and manages to come along.", ("องก์ 3","Shizune")),
                                    ("United Nations", "S18", "The trip to Shizune's house, meeting her little brother, and a sudden fishing contest.", ("องก์ 3","Shizune")),
                                    ("Use-Mention Distinction", "S19", "Hideaki tries to entertain Hisao for a day, meeting with little success.", ("องก์ 3","Shizune")),
                                    ("Family Plot", "S20", "Our trio meets Shizune's father and immediately beats a hasty retreat.", ("องก์ 3","Shizune")),
                                    ("Pangrammatic Window", "S21", "A request from Hideaki to learn sign language unexpectedly escalates into a shouting match with Jigoro.", ("องก์ 3","Shizune")),
                                    ("Closer", "S22", "Shizune and Hisao join together for the first time.", ("องก์ 3","Shizune")),
                                    ("Confrontation", "S23", "Jigoro belittles the Student Council and Hisao rises up to the challenge.", ("องก์ 3","Shizune")),
                                    ("The Anchor", "S24", "Back to Yamaku. A letter from Iwanako prompts a lengthy discussion from Kenji on the finer points of girlfriends.", ("องก์ 3","Shizune")),
                                    ("Roadmap", "S25", "The Student Council worries about their replacement, and Hisao ends up treating Misha to a parfait somehow.", ("องก์ 3","Shizune")), #shortened this line - it overflowed
                                    ("Acute Triangle", "S26", "An afternoon of work with Shizune shows Hisao that something is amiss between the girls.", ("องก์ 3","Shizune")),
                                    ("Dewey Decimated", "S27", "Yuuko gets Hisao to watch the library for her. The arrival of Kenji makes the attempt meet with mixed success.", ("องก์ 3","Shizune")),
                                    ("Tongue-Tied", "S28", "Misha visits Hisao in his room, and things go in an unexpected direction.", ("องก์ 3","Shizune")),
                                    ("Look Aside", "S29_1", "Hisao meets a depressed Misha on the roof. He ends up pushing her and Shizune together.", ("องก์ 3","Shizune")),
                                    ("Look Ahead", "S29_2", "Hisao meets a depressed Misha on the roof. Shizune joins them and pulls the whole council back to work.", ("องก์ 3","Shizune")),
                                    ("องก์ 4: To My Other Self", rp_actmark, rp_actmark, ("องก์ 4","Shizune")),
                                    ("Grand Strategy", "S30", "Shizune confesses to Hisao some of her goals and failures.", ("องก์ 4","Shizune")),
                                    ("Off by One", "S31", "A failed attempt to cheer up Misha gets converted into an impromptu date for Hisao and Shizune.", ("องก์ 4","Shizune")),
                                    ("Invasion", "S32", "Jigoro and Hideaki pay Shizune an unexpected and somewhat unpleasant visit.", ("องก์ 4","Shizune")),
                                    ("Parfait", "S33", "Hisao and Shizune stalk Misha. Hisao finally manages to corner her and discuss things properly.", ("องก์ 4","Shizune")),
                                    ("Present Tense", "S38", "Hisao stumbles into Lilly at lunch, and the two talk about Shizune.", ("องก์ 4","Shizune")), # we always show the bad end scenes first
                                    ("Spiral", "S39", "Runaround, stonewalling, and Kenji nighttime ambush.", ("องก์ 4","Shizune")),
                                    ("Terminal", "S40", "An early-morning talk with Shizune in the silent school.", ("องก์ 4","Shizune")),
                                    ("The Summit", "S34", "Kenji and Shizune meet in Hisao's room. Miraculously, nothing explodes.", ("องก์ 4","Shizune")), # back to good end continuity
                                    ("Succession", "S35", "The current Student Council shapes up their successors before engaging in “extracurricular activities.”", ("องก์ 4","Shizune")),
                                    ("Sneaking Mission", "S36", "The show of Misha's determination spurs Shizune to set her sights on greater things.", ("องก์ 4","Shizune")),
                                    ("Infinity", "S37", "Our trio renews their friendship, with their graduation looming close ahead.", ("องก์ 4","Shizune")),
                                    )

    # credits

    displayDict["th"].creditstring = """{image=ui/flourish_left.png} {b}Writing{/b} {image=ui/flourish_right.png}
Anonymous22
Aura
cpl_crud
Suriko
TheHivเอมิnd

{image=ui/flourish_left.png} {b}Editing{/b} {image=ui/flourish_right.png}
Kagami
Losstarot
Silentcook

{image=ui/flourish_left.png} {b}Music{/b} {image=ui/flourish_right.png}
Blue123
NicolArmarfi

{image=ui/flourish_left.png} {b}Art{/b} {image=ui/flourish_right.png}
gebyy-terar
Kamifish
moekki
pimmy
raemz
Raide

{image=ui/flourish_left.png} {b}Additional Art{/b} {image=ui/flourish_right.png}
climatic
Doomfest
yujovi

{image=ui/flourish_left.png} {b}FMV Animation{/b} {image=ui/flourish_right.png}
Mike Inel

{image=ui/flourish_left.png} {b}Directing{/b} {image=ui/flourish_right.png}
delta
Raide
yujovi

{image=ui/flourish_left.png} {b}Engineering{/b} {image=ui/flourish_right.png}
delta

{image=ui/flourish_left.png} {b}Production{/b} {image=ui/flourish_right.png}
cpl_crud
Suriko


{image=ui/flourish_center.png}


{image=ui/flourish_left.png} {b}Thanks{/b} {image=ui/flourish_right.png}
Ambi07
abscess
Anonymous
Celiest
ContinualNaba
Dark_Mercury
DuaneMoody
Fink
frumplstlskn
Ismuth
Japesland
Juno
kekekeke
konflikti
Magaran
Mirage_GSM
OverCoat
Peorth
Petaru
silentkyon
skim
stirfriedweasel
Syureria
TcDohl
tottori
VCR

{image=ui/flourish_left.png} {b}Special Thanks{/b} {image=ui/flourish_right.png}
hir
PyTom
RAITA
replicated"""


    displayDict["th"].drugs_wordlist  =  ["Disopyramide",
                        "Warfarin",
                        "Diltiazem",
                        "Felodipine",
                        "Propanolol",
                        "Penbutolol",
                        "Carteolol",
                        "Procainamide",
                        "Heparin",
                        "Phenytoin",
                        "Verapamil",
                        "Quinidine",
                        "Flecainide",
                        "5mg/day",
                        "400mg/day",
                        "15ml/day",
                        "100mg/day",
                        "10ml/48hrs",
                        "10ml/day",
                        "200mg/12hrs",
                        "50mg/12hrs",
                        "500mg/48hrs",
                        "125mg/12hrs",
                        "25ml/day",
                        "nightmares",
                        "decreased concentration",
                        "bradycardia",
                        "clinical depression",
                        "insomnia",
                        "erectile dysfunction",
                        "abnormal vision",
                        "heart failure",
                        "nausea",
                        "dizziness",
                        "hallucinations",
                        "bronchospasm",
                        "dyspnea",
                        "fatigue",
                        "hypotension",
                        "heart block",
                        "cold extremities",
                        "diarrhea",
                        "cardiac arrest",
                        "ventricular fibrillation",
                        "ataxia",
                        "asthma"]
