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
                                    ("สัญญาแห่งกาลเวลา", "A41", "After a trying morning at her stall, Hisao takes Lilly to find Hanako.", "องก์ 1"),
                                    ("Clouds in My Head", "A40", "Hisao keeps Rin and her now-finished mural company.", "องก์ 1"),
                                    ("Throwing Balls", "A44", "True to his word, Hisao spends the day with Shizune and Misha.", "องก์ 1"),
                                    ("The Deep End", "A43", "Kenji and Hisao share a manly picnic on the roof instead of going to the festival.", "องก์ 1"),
                                    ("Act 2: Form", rp_actmark, rp_actmark, ("Act 2","Emi")),
                                    ("Morning Run", "E3", "The first of Hisao's many morning runs with Emi.", ("Act 2","Emi")),
                                    ("Clouds, Time Travel, and Thou", "E4", "Another rooftop lunch with Emi and Rin. Emi extracts from Hisao a promise to come see the track meet.", ("Act 2","Emi")),
                                    ("Questions That Need Answering!", "E5", "Idle chat between Emi and Hisao. Hisao asks Emi a few more questions about her relationship with Rin.", ("Act 2","Emi")),
                                    ("Second Time's the Worst", "E6", "The second morning run. Hisao is almost dragged kicking and screaming around the track.", ("Act 2","Emi")),
                                    ("An Apple a Day", "E7", "Hisao pays a visit to the nurse along with Emi, finding out that the two have known each other for a while.", ("Act 2","Emi")),
                                    ("Track Meeting", "E8", "The day of the track meet. Another facet of Emi's personality is revealed.", ("Act 2","Emi")),
                                    ("Down that Medicine Now", "E9", "Hisao mentions a pain in his chest during a visit to the nurse and receives a lecture.", ("Act 2","Emi")),
                                    ("Piracy on the High Seas", "E10", "Hisao discusses his future as a pirate with Emi on the rooftop, then a letter from Iwanako spoils his day.", ("Act 2","Emi")),
                                    ("Famous Last Words", "E11", "Emi and Rin take Hisao along for a picnic, soon to be spoiled by rain.", ("Act 2","Emi")),
                                    ("Tracking Absences", "E12", "Hisao goes to the track as usual, but Emi is missing.", ("Act 2","Emi")),
                                    ("Dropping By", "E13", "A bedside visit for a sick Emi, which quickly changes to something else entirely.", ("Act 2","Emi")),
                                    ("The First Morning After", "E14", "Hisao reminisces about last evening, deciding to do something to help Emi.", ("Act 2","Emi")),
                                    ("The (Real) Beginning", "E15", "Another lunchtime on the rooftop, sans Rin.", ("Act 2","Emi")),
                                    ("Act 3: Perspective", rp_actmark, rp_actmark, ("Act 3","Emi")),
                                    (u"Eet Ees… Scienca", "E16", "Mutou pulls Hisao into a short discussion about his future.", ("Act 3","Emi")),
                                    ("Definitions", "E17", "Emi and Hisao attempt another picnic, this time without any intervention from Mother Nature.", ("Act 3","Emi")),
                                    ("Invisible Rock", "E18", "Back to the track in the morning, with business as usual… or so it seems.", ("Act 3","Emi")),
                                    ("Lunch and Science", "E19", "Hisao sees Mutou again about his future in the sciences.", ("Act 3","Emi")),
                                    ("Up, Down, and Up Again", "E20", "A frantic call from Emi brings Hisao to her room, where two surprises await him.", ("Act 3","Emi")),
                                    ("Storage Space", "E21", "Emi coaxes Hisao into the track storage shed.", ("Act 3","Emi")),
                                    ("After-School Plans", "E22", "Emi has a serious talk with Hisao about the incoming exams.", ("Act 3","Emi")),
                                    ("Detached", "E23", "Hisao broods about his relationship with Emi.", ("Act 3","Emi")), # renamed this one from "Disconnected" - "Disconnect" is the name of Rin's Act 2
                                    ("Phantom Pain", "E24", "Hisao's attempt to show Emi his concern doesn't go nearly as well as he hoped.", ("Act 3","Emi")),
                                    ("Debate Expresses Doubt", "E25", "Hisao is confused by Emi's behavior and by an invitation to her house.", ("Act 3","Emi")),
                                    (u"Guess Who's Coming… Never Mind", "E26", "Dinner at the Ibarazaki's.", ("Act 3","Emi")),
                                    ("Instant Replay", "E27", "Things finally come to a head at the track.", ("Act 3","Emi")),
                                    ("Act 4: Motion", rp_actmark, rp_actmark, ("Act 4","Emi")),
                                    ("A Swing and a Miss", "E28", "Hisao wonders if Emi is purposefully avoiding him.", ("Act 4","Emi")),
                                    ("Saving Throw", "E29", "Things finally come to a head on the rooftop.", ("Act 4","Emi")),
                                    ("Whispers of the Past", "E30", "Hisao, Emi and her mom go for a graveside visit.", ("Act 4","Emi")),
                                    ("Hooray for Socks", "E31", "Sex, drugs, but no rock and roll.", ("Act 4","Emi")),
                                    ("Clean Teeth", "E32", "Hisao wakes up, finding Emi sleeping next to him.", ("Act 4","Emi")),
                                    ("Act 2: Hide and Seek", rp_actmark, rp_actmark, ("Act 2","Hanako")),
                                    ("To Town, To Town", "H3", "A shopping trip at the convenience store with Hanako.", ("Act 2","Hanako")),
                                    ("Tea Leaves", "H4", "Hanako invites Hisao to have lunch with her and Lilly.", ("Act 2","Hanako")),
                                    ("Office Confessional", "H5_1", "Hisao and Misha discuss the plight of Hanako.", ("Act 2","Hanako")),
                                    ("Chess and Slides", "H5_2", "Hisao ditches the Student Council to read with Hanako.", ("Act 2","Hanako")),
                                    ("Rise and Shine", "H6", "An invitation from Lilly to a tea party after hours.", ("Act 2","Hanako")),
                                    ("Mad Hatter", "H7", "Hanako, Hisao and Lilly meet together to have tea in Lilly's room.", ("Act 2","Hanako")),
                                    ("Small Change", "H8", "Kenji is forced to repay his loan.", ("Act 2","Hanako")),
                                    ("Absenteeism", "H9", "Hisao and Lilly discuss Hanako's school attendance.", ("Act 2","Hanako")),
                                    ("Equivalent Exchange", "H10", "In return for learning about his heart, Hanako reveals part of her past to Hisao.", ("Act 2","Hanako")),
                                    ("Act 3: Castling", rp_actmark, rp_actmark, ("Act 3","Hanako")),
                                    ("Invitation", "H11", "Lilly finds Hisao cleaning up the Tea Room and tells him about Hanako's birthday.", ("Act 3","Hanako")),
                                    ("Shady Encounter", "H12", "An unexpected chat with Miki while reminiscing about the past.", ("Act 3","Hanako")),
                                    ("Antiques and Pie", "H13", "Lilly and Hisao shop for a present in the city.", ("Act 3","Hanako")),
                                    ("Falling", "H14", "Hanako has a panic attack during class.", ("Act 3","Hanako")),
                                    ("Treading Softly", "H15", "Lilly has bad news to discuss with Hisao and Hanako.", ("Act 3","Hanako")),
                                    ("Reaching Out", "H16", "Hisao reaches out to a withdrawn Hanako.", ("Act 3","Hanako")),
                                    ("One More Year", "H17", "Our trio is joined by an unexpected guest as they celebrate Hanako's birthday party.", ("Act 3","Hanako")),
                                    ("One Piece of Paper", "H18", "Hisao enjoys his first hangover, before receiving a troubling letter.", ("Act 3","Hanako")),
                                    ("Stripes and Solids", "H19", "Heart-to-heart during a game of pool.", ("Act 3","Hanako")),
                                    ("Beginning of the End", "H20", "Lilly's departure for her trip.", ("Act 3","Hanako")),
                                    ("Act 4: Scars", rp_actmark, rp_actmark, ("Act 4","Hanako")),
                                    ("Truancy", "H21", "Lunch with the Student Council and worry about Hanako shutting herself in.", ("Act 4","Hanako")),
                                    ("Faraway Presence", "H22", "Hisao phones Lilly for advice after Hanako secludes herself for another day.", ("Act 4","Hanako")),
                                    ("Misstep", "H23", "Hisao tries to pull Hanako out of her room, with startling results.", ("Act 4","Hanako")),
                                    ("Cut Petals", "H24", "Hisao finds his future relationship with Hanako prematurely ended.", ("Act 4","Hanako")),
                                    ("Continuing Melody", "H25", "Hanako returns to class, to Hisao's relief.", ("Act 4","Hanako")),
                                    ("Shanghai Studiousness", "H26", "Attempting to avoid distractions, Hisao tries studying at the Shanghai.", ("Act 4","Hanako")),
                                    ("His Past", "H27", "In an attempt to come closer to Hanako, Hisao shares a part of his past with her.", ("Act 4","Hanako")),
                                    ("City Rendezvous", "H28", "The two share a date in the city.", ("Act 4","Hanako")),
                                    ("Whispered Touch", "H29", "Hisao and Hanako spend the night together.", ("Act 4","Hanako")),
                                    ("Indeterminate Future", "H30", "The events of the previous night weigh heavily on Hisao.", ("Act 4","Hanako")),
                                    ("Adulthood", "H31", "The end of two children, the beginning of two adults.", ("Act 4","Hanako")),
                                    ("Act 2: Past", rp_actmark, rp_actmark, ("Act 2","Lilly")),
                                    ("Earl Grey", "L1", "Hisao shares the first of many lunchbreaks with Hanako and Lilly, recovering from the day before.", ("Act 2","Lilly")),
                                    ("A Pound Sterling", "L2", "Questioned by Kenji on Lilly's nationality, Hisao decides to investigate and finds out a great deal more.", ("Act 2","Lilly")),
                                    ("Presents and Presence", "L3", "While out in search of a present for Hanako, Lilly and Hisao meet Akira and her cousin.", ("Act 2","Lilly")),
                                    ("Unidentified Drinking Object", "L4", "The trio hold a birthday party for Hanako, interrupted by the surprise appearance of a sibling.", ("Act 2","Lilly")),
                                    ("The Day After", "L5", "Hisao and Lilly awaken and try to recuperate from the previous evening's events.", ("Act 2","Lilly")),
                                    ("A Brief History of Thyme", "L6", "Hisao and Lilly go to get some groceries.", ("Act 2","Lilly")),
                                    ("Little Wing", "L7", "A shared lunch on the roof takes an unfortunate turn.", ("Act 2","Lilly")),
                                    ("Bon Voyage", "L8", "Lilly and Akira get seen off as they leave for a trip to their family in Scotland.", ("Act 2","Lilly")),
                                    ("Act 3: Present", rp_actmark, rp_actmark, ("Act 3","Lilly")),
                                    ("Day by Day", "L9", "Hisao idly lets a day without Lilly slip by, having a talk with Mutou about Yamaku.", ("Act 3","Lilly")),
                                    ("Minor Discord", "L10", "Hisao has lunch with Kenji, then gives some handouts to an alarmingly silent Hanako.", ("Act 3","Lilly")),
                                    ("Dissonance", "L11", "With Hanako withdrawing into herself completely, Hisao offers what little help he can before calling Lilly.", ("Act 3","Lilly")),
                                    ("A World Away", "L12", "Hisao's reassured mind begins to wonder about the relationship between he and Lilly.", ("Act 3","Lilly")),
                                    ("Renewal", "L13", "Hisao, Hanako, and Hideaki welcome Akira and Lilly after their return from Scotland.", ("Act 3","Lilly")),
                                    ("Northern Sojourn", "L14", "The trio begins their holiday in Hokkaido.", ("Act 3","Lilly")),
                                    ("Prelude", "L15", "A morning walk begins a chain of events.", ("Act 3","Lilly")),
                                    ("Crescendo", "L16", "Lilly's true feelings are told in the endless gold of the wheat fields." , ("Act 3","Lilly")),
                                    ("Diminuendo", "L17", "Our couple shares their first night together.", ("Act 3","Lilly")),
                                    ("Gray Outlook", "L18", "Confined to the summerhouse, Lilly and Hisao are forced to come to terms with their relationship.", ("Act 3","Lilly")),
                                    ("Rhapsody in Blue", "L19", "A bathing Hisao reflects on where he and Lilly are in life, before being joined by someone.", ("Act 3","Lilly")),
                                    ("The Momentary Present", "L20", "Traveling back to Yamaku, Hisao and Lilly idly talk between themselves.", ("Act 3","Lilly")),
                                    ("Act 4: Future", rp_actmark, rp_actmark, ("Act 4","Lilly")),
                                    ("Slow Steps 'Fore a Waltz", "L21", "Back at the school, the events of Hokkaido come to the fore.", ("Act 4","Lilly")),
                                    ("Pajamas and Suits", "L22", "Settling back into daily life. Akira joins the trio during one of their tea parties.", ("Act 4","Lilly")),
                                    ("Correct Procedure", "L23", "Hisao and Lilly arrange a date, before Akira swings by.", ("Act 4","Lilly")),
                                    ("Out and About", "L24", "Hisao and Lilly go on their first date, finding out about each other's pasts.", ("Act 4","Lilly")),
                                    ("A Morning's Reverie", "L25", "Hisao and Lilly discuss their ambitions for the future.", ("Act 4","Lilly")),
                                    ("Blackout", "L26", "The trio muse on the upcoming holidays, before Hisao experiences sight as Lilly does.", ("Act 4","Lilly")),
                                    ("Context", "L27", "Hisao gets called out by Akira and the two talk about her sibling.", ("Act 4","Lilly")),
                                    ("A Faraway Future", "L28", "Lilly reveals her family's offer to join them in Scotland.", ("Act 4","Lilly")),
                                    ("Farewell", "L29", "Farewells to Akira and Lilly the evening before they leave Japan.", ("Act 4","Lilly")),
                                    ("False Cadence", "L30", "Hisao rushes to confront Lilly, realizing her conflict.", ("Act 4","Lilly")),
                                    ("Under a Maudlin Sky", "L31", "Waking in the hospital ward, Hisao struggles to come to terms with his life.", ("Act 4","Lilly")),
                                    ("Under a Bright Sky", "L32", "Lilly rejoins Hisao, the two beginning their life together anew.", ("Act 4","Lilly")),
                                    ("Forwards, with Gusto!", "L33", "Lilly and Hisao see off Akira.", ("Act 4","Lilly")),
                                    ("Act 2: Disconnect", rp_actmark, rp_actmark, ("Act 2","Rin")),
                                    ("A Wider Field of Vision", "R1", "Hisao spends a lunch break with Rin watching clouds on the rooftop.", ("Act 2","Rin")),
                                    ("Studies in Grayscale", "R2", "Rin and Hisao draw portraits of each other at his first art club meeting.", ("Act 2","Rin")),
                                    (u"Interstitial", "R3", "Kenji lends a “borrowed” book to Hisao.", ("Act 2","Rin")),
                                    ("Self Study", "R4", "Misha and Shizune catch Hisao meditatively doodling during class.", ("Act 2","Rin")),
                                    ("Hisao's Smile", "R5", "Rin talks to Hisao about his happy expressions, or lack of them.", ("Act 2","Rin")),
                                    ("Things You Like", "R6", "Brief musings with Yuuko about books and Yamaku.", ("Act 2","Rin")),
                                    ("Target Audience", "R7", "The day of the track meet. Facets of Emi's and Rin's personalities get revealed.", ("Act 2","Rin")),
                                    ("Eternity In an Hour", "R8", "Nomiya incites discussion of art during a club meeting.", ("Act 2","Rin")),
                                    ("Underwater and a Maple with a Name", "R9", "Rin leads Hisao into the woods, where they ponder their immediate future.", ("Act 2","Rin")),
                                    ("Iwanako's Regret", "R10", "A letter from Iwanako arrives.", ("Act 2","Rin")),
                                    ("In Her Own Image", "R11", "Hisao pushes Rin to have her own art exhibition.", ("Act 2","Rin")),
                                    ("Umbrella Logic Cake", "R12", "Emi, Hisao and Rin get rained on and seek refuge in the Shanghai.", ("Act 2","Rin")),
                                    ("Six Meters Closer to Heaven", "R13", "Rin and Hisao DON'T eat lunch on the roof, due to a distinct lack of Emi.", ("Act 2","Rin")),
                                    ("Indecision", "R14", "Emi gets rid of her cold, while Rin catches her own.", ("Act 2","Rin")),
                                    ("Signal Interference", "R15", "Hisao goes visit Rin in her room.", ("Act 2","Rin")),
                                    ("Dandelions", "R16", "Conclusions get drawn on a hilltop.", ("Act 2","Rin")),
                                    ("Act 3: Distance", rp_actmark, rp_actmark, ("Act 3","Rin")),
                                    ("22nd Corner", "R17", "The art club team checks out the gallery for Rin's future exhibition.", ("Act 3","Rin")),
                                    ("The Scent of Light", "R18", "Hisao happens upon a sleeping Rin in the art room.", ("Act 3","Rin")),
                                    ("Things You Can't Give Up", "R19", "Emi and Hisao discuss Rin's personality.", ("Act 3","Rin")),
                                    ("BADAAN!", "R20", "Yuuko's thoughts on motivation.", ("Act 3","Rin")),
                                    ("Rose-Tinted Glasses", "R21", "Nomiya expounds at length about art as a career.", ("Act 3","Rin")),
                                    ("The Edge of the World", "R22", "Hisao confesses to Rin and gets shot down. Or does he?", ("Act 3","Rin")),
                                    ("The Context of Rin", "R23", "An awkward and silent afternoon at the atelier.", ("Act 3","Rin")),
                                    ("Fast Forward", "R23_2", "The preparations for the exhibition settle into a strange routine.", ("Act 3","Rin")),
                                    ("Self-Destruction", "R24", "Rin experiments with smoking to get a fresh look at creativity.", ("Act 3","Rin")),
                                    ("Reverse Escapism", "R25", "Hisao takes Rin on a walk through the night streets.", ("Act 3","Rin")),
                                    ("Boundless", "R26", "Sae and Nomiya give Hisao some insight on artists' lives.", ("Act 3","Rin")),
                                    ("Delirium", "R27", "Hisao surprises a desperate Rin in the atelier.", ("Act 3","Rin")),
                                    ("Things You Hate", "R28", "Unpleasant aftermath of an incredible night.", ("Act 3","Rin")),
                                    ("Shards of Ire", "R29", "The strained relationship between the two blows apart.", ("Act 3","Rin")),
                                    ("Act 4: Dream", rp_actmark, rp_actmark, ("Act 4","Rin")),
                                    ("Illusions for People", "R30", "Hisao talks about his misgivings to Nomiya, to little effect.", ("Act 4","Rin")),
                                    ("Demused", "R31", "Hisao's patience comes to an end.", ("Act 4","Rin")),
                                    ("The Scene", "R32", "Meeting with Rin at the exhibition opening.", ("Act 4","Rin")), #R33 is just a scene block used in two other scenes, R34 is sorted later
                                    ("Wavelength", "R35", "Hisao lethargically whiles away the last day of exams.", ("Act 4","Rin")),
                                    ("Blue Period", "R36", "A rainy day, the 22nd Corner, and a brief history of Picasso.", ("Act 4","Rin")),
                                    ("The World Only You Can See", "R37", "Rin and Hisao part after the rain.", ("Act 4","Rin")),
                                    ("Desperate Glory", "R34", "A frantic Nomiya queries Hisao about Rin's whereabouts.", ("Act 4","Rin")), #moved down here so all good end path scenes are in a row
                                    ("Problems of Self-Referential Logic", "R38", "Hisao finds Rin in her hiding place, and convinces her to reconcile with Nomiya.", ("Act 4","Rin")),
                                    ("Measuring Shadows", "R39", "Rin's apology to the art teacher isn't well-received.", ("Act 4","Rin")),
                                    (u"Raison d'être", "R40", "Hisao comforts an upset Rin.", ("Act 4","Rin")),
                                    ("Without Breathing, Without a Sound", "R41", "On the first day of summer vacation, Rin comes to Hisao's room.", ("Act 4","Rin")),
                                    ("Proof of Existence", "R42", "Everything comes together on that dandelion-covered hilltop.", ("Act 4","Rin")),
                                    ("Act 2: Learning to Read", rp_actmark, rp_actmark, ("Act 2","Shizune")),
                                    ("Message Passing", "S8", "Shizune and Hisao explore methods of communication.", ("Act 2","Shizune")),
                                    ("Talk to the Hand", "S9", "Hisao begins studying a new language, and a tutor appears.", ("Act 2","Shizune")),
                                    ("Chinese Whispers", "S10", "Kenji manages to coerce Hisao to do a favor for him, but Hisao runs into trouble in many forms.", ("Act 2","Shizune")),
                                    ("Advanced Game Theory", "S11", "RISK isn't enough any more to satiate Shizune's hunger. What's worse, a new opponent makes her appearance.", ("Act 2","Shizune")),
                                    ("Bread, Scissors, Paper", "S12", "A lazy afternoon becomes dramatic as suddenly a piece of bread becomes an object of extreme interest.", ("Act 2","Shizune")),
                                    ("Interface", "S13", "Shizune and Hisao find a connection.", ("Act 2","Shizune")),
                                    ("Spring into Action", "S14", "Hisao has to mediate between Lilly and Shizune, but luckily things work out in the end.", ("Act 2","Shizune")),
                                    ("Past Imperfective", "S15", "The Student Council reminisces about past years while relaxing at the Shanghai.", ("Act 2","Shizune")),
                                    ("When Stars Embrace", "S16", "It's finally time for Tanabata!", ("Act 2","Shizune")),
                                    ("Act 3: Sleight of Hand", rp_actmark, rp_actmark, ("Act 3","Shizune")),
                                    ("Force Feedback", "S17", "Hisao finds out that Shizune is going to visit her family, and manages to come along.", ("Act 3","Shizune")),
                                    ("United Nations", "S18", "The trip to Shizune's house, meeting her little brother, and a sudden fishing contest.", ("Act 3","Shizune")),
                                    ("Use-Mention Distinction", "S19", "Hideaki tries to entertain Hisao for a day, meeting with little success.", ("Act 3","Shizune")),
                                    ("Family Plot", "S20", "Our trio meets Shizune's father and immediately beats a hasty retreat.", ("Act 3","Shizune")),
                                    ("Pangrammatic Window", "S21", "A request from Hideaki to learn sign language unexpectedly escalates into a shouting match with Jigoro.", ("Act 3","Shizune")),
                                    ("Closer", "S22", "Shizune and Hisao join together for the first time.", ("Act 3","Shizune")),
                                    ("Confrontation", "S23", "Jigoro belittles the Student Council and Hisao rises up to the challenge.", ("Act 3","Shizune")),
                                    ("The Anchor", "S24", "Back to Yamaku. A letter from Iwanako prompts a lengthy discussion from Kenji on the finer points of girlfriends.", ("Act 3","Shizune")),
                                    ("Roadmap", "S25", "The Student Council worries about their replacement, and Hisao ends up treating Misha to a parfait somehow.", ("Act 3","Shizune")), #shortened this line - it overflowed
                                    ("Acute Triangle", "S26", "An afternoon of work with Shizune shows Hisao that something is amiss between the girls.", ("Act 3","Shizune")),
                                    ("Dewey Decimated", "S27", "Yuuko gets Hisao to watch the library for her. The arrival of Kenji makes the attempt meet with mixed success.", ("Act 3","Shizune")),
                                    ("Tongue-Tied", "S28", "Misha visits Hisao in his room, and things go in an unexpected direction.", ("Act 3","Shizune")),
                                    ("Look Aside", "S29_1", "Hisao meets a depressed Misha on the roof. He ends up pushing her and Shizune together.", ("Act 3","Shizune")),
                                    ("Look Ahead", "S29_2", "Hisao meets a depressed Misha on the roof. Shizune joins them and pulls the whole council back to work.", ("Act 3","Shizune")),
                                    ("Act 4: To My Other Self", rp_actmark, rp_actmark, ("Act 4","Shizune")),
                                    ("Grand Strategy", "S30", "Shizune confesses to Hisao some of her goals and failures.", ("Act 4","Shizune")),
                                    ("Off by One", "S31", "A failed attempt to cheer up Misha gets converted into an impromptu date for Hisao and Shizune.", ("Act 4","Shizune")),
                                    ("Invasion", "S32", "Jigoro and Hideaki pay Shizune an unexpected and somewhat unpleasant visit.", ("Act 4","Shizune")),
                                    ("Parfait", "S33", "Hisao and Shizune stalk Misha. Hisao finally manages to corner her and discuss things properly.", ("Act 4","Shizune")),
                                    ("Present Tense", "S38", "Hisao stumbles into Lilly at lunch, and the two talk about Shizune.", ("Act 4","Shizune")), # we always show the bad end scenes first
                                    ("Spiral", "S39", "Runaround, stonewalling, and Kenji nighttime ambush.", ("Act 4","Shizune")),
                                    ("Terminal", "S40", "An early-morning talk with Shizune in the silent school.", ("Act 4","Shizune")),
                                    ("The Summit", "S34", "Kenji and Shizune meet in Hisao's room. Miraculously, nothing explodes.", ("Act 4","Shizune")), # back to good end continuity
                                    ("Succession", "S35", "The current Student Council shapes up their successors before engaging in “extracurricular activities.”", ("Act 4","Shizune")),
                                    ("Sneaking Mission", "S36", "The show of Misha's determination spurs Shizune to set her sights on greater things.", ("Act 4","Shizune")),
                                    ("Infinity", "S37", "Our trio renews their friendship, with their graduation looming close ahead.", ("Act 4","Shizune")),
                                    )

    # credits

    displayDict["th"].creditstring = """{image=ui/flourish_left.png} {b}Writing{/b} {image=ui/flourish_right.png}
Anonymous22
Aura
cpl_crud
Suriko
TheHivemind

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
