# 《江湖小镇之凰龙府》第一章 Ren'Py 脚本
# 当前版本：第一章《雷云开炉》先行试玩版 V0.1

define game_display_version = "《江湖小镇之凰龙府》第一章《雷云开炉》先行试玩版 V0.1"


define contact_version = "qr"
# =========================
# 图片定义 V0.1
# =========================



image bg kaian_town_intro = "images/bg/bg_kaian_town_intro.png"
image bg feihong_yuan_exterior_evening = "images/bg/bg_feihong_yuan_evening.png"
image bg feihong_yuan_exterior_day = "images/bg/bg_feihong_yuan_exterior_day.png"
image wangfang neutral = "images/characters/wangfang_neutral.png"
image zuowan neutral = "images/characters/zuowan_neutral.png"
image wangfang_select = "images/characters/wangfang_neutral.png"
image zuowan_select = "images/characters/zuowan_neutral.png"

# =========================
# NPC 立绘
# =========================

#游街子
image housanxian neutral = "images/characters/housanxian_neutral.png"

#茯苓医馆
image xuchunxiang neutral = "images/characters/xuchunxiang_neutral.png"
image chengmingzhu neutral = "images/characters/chengmingzhu_neutral.png"
image chensumei neutral = "images/characters/chensumei_neutral.png"
image zhouqingliu neutral = "images/characters/zhouqingliu_neutral.png"
image limo neutral = "images/characters/limo_neutral.png"
image shenyun neutral = "images/characters/shenyun_neutral.png"
image shenxingchen neutral = "images/characters/shenxingchen_neutral.png"

#飞鸿驿站
image guoluping neutral = "images/characters/guoluping_neutral.png"
image fangheming neutral = "images/characters/fangheming_neutral.png"
image lutiankuo neutral = "images/characters/lutiankuo_neutral.png"
image zhouerdan neutral = "images/characters/zhouerdan_neutral.png"
image fangdaniang neutral = "images/characters/fangdaniang_neutral.png"
image weisaner neutral = "images/characters/weisaner_neutral.png"
image luoazao neutral = "images/characters/luoazao_neutral.png"

# =========================

# 开场 / 主菜单 / 世界舆图

# =========================

image bg main_menu_world_map_source = "images/bg/bg_main_menu_world_map_source.png"

# =========================

# 江湖势力 / 门派介绍

# =========================

image bg chengtian_sword_sect_intro = "images/bg/bg_chengtian_sword_sect_intro.png"
image bg wutian_chan_monastery_intro = "images/bg/bg_wutian_chan_monastery_intro.png"
image bg canghai_pavilion_intro = "images/bg/bg_canghai_pavilion_intro.png"
image bg wandu_valley_intro = "images/bg/bg_wandu_valley_intro.png"
image bg hengyun_hall_intro = "images/bg/bg_hengyun_hall_intro.png"

# 风云坪
image bg fengyunping = "images/bg/bg_fengyunping.png"
image bg fengyunping_day = "images/bg/bg_fengyunping_day.png"
image bg fengyunping_evening_lodging_realization = "images/bg/bg_fengyunping_evening_lodging_realization.png"
image bg fengyunping_notice_sealing_order_day = "images/bg/bg_fengyunping_notice_sealing_order_day.png"
image bg fengyunping_notice_burn_mark_day = "images/bg/bg_fengyunping_notice_burn_mark_day.png"
image bg fengyunping_notice_group_orders_day = "images/bg/bg_fengyunping_notice_group_orders_day.png"
image bg fengyunping_notice_dan_ash_day = "images/bg/bg_fengyunping_notice_dan_ash_day.png"
image bg fengyunping_crowd_arrival_day = "images/bg/bg_fengyunping_crowd_arrival_day.png"

# 银花庵

image bg yinhua_an_exterior_day = "images/bg/bg_yinhua_an_exterior_day.png"

image bg yinhua_an_exterior_evening = "images/bg/bg_yinhua_an_exterior_evening.png"

# 永乐大街

image bg yongle_changfeng_intersection_day = "images/bg/bg_yongle_changfeng_intersection_day.png"

image bg yongle_changfeng_intersection_evening = "images/bg/bg_yongle_changfeng_intersection_evening.png"

image bg yongle_street_leiling_palace_day_guest = "images/bg/bg_yongle_street_leiling_palace_day_guest.png"

# 长风衢与开庵街交汇处

image bg changfeng_kaian_intersection_day = "images/bg/bg_changfeng_kaian_intersection_day.png"

image bg changfeng_kaian_intersection_evening = "images/bg/bg_changfeng_kaian_intersection_evening.png"

# 永乐大街西侧门脸总览

image bg yongle_street_westfront_day = "images/bg/bg_yongle_street_westfront_day.png"

image bg yongle_street_westfront_night = "images/bg/bg_yongle_street_westfront_night.png"

# 茯苓医馆

image bg fuling_clinic_interior = "images/bg/bg_fuling_clinic_interior.png"
image bg fuling_clinic_exterior = "images/bg/bg_fuling_clinic_exterior.png"
image bg fuling_clinic_interior_day_busy = "images/bg/bg_fuling_clinic_interior_day_busy.png"
image bg fuling_clinic_interior_day_busy_v2 = "images/bg/bg_fuling_clinic_interior_day_busy_v2.png"
image bg fuling_clinic_exterior_evening_invite_wangfang = "images/bg/bg_fuling_clinic_exterior_evening_invite_wangfang.png"
image bg fuling_clinic_exterior_evening_invite_zuowan = "images/bg/bg_fuling_clinic_exterior_evening_invite_zuowan.png"
image bg fuling_clinic_exterior_evening_choose_clinic = "images/bg/bg_fuling_clinic_exterior_evening_choose_clinic.png"
image bg fuling_clinic_interior_day_zhouqingliu = "images/bg/bg_fuling_clinic_interior_day_zhouqingliu.png"
image bg fuling_clinic_interior_day_zhouqingliu_shenyun = "images/bg/bg_fuling_clinic_interior_day_zhouqingliu_shenyun.png"
image bg fuling_clinic_exterior_evening_shenyun_call = "images/bg/bg_fuling_clinic_exterior_evening_shenyun_call.png"
image bg fuling_clinic_interior_day_emergency_patient = "images/bg/bg_fuling_clinic_interior_day_emergency_patient.png"
image bg fuling_clinic_interior_day_inquiry_brothers = "images/bg/bg_fuling_clinic_interior_day_inquiry_brothers.png"
image bg fuling_clinic_interior_day_chunhua_plan = "images/bg/bg_fuling_clinic_interior_day_chunhua_plan.png"
image bg fuling_clinic_interior_day_chunhua_treatment = "images/bg/bg_fuling_clinic_interior_day_chunhua_treatment.png"
image bg fuling_clinic_interior_day_patient_stabilized = "images/bg/bg_fuling_clinic_interior_day_patient_stabilized.png"
image bg fuling_clinic_interior_evening_patient_wakes = "images/bg/bg_fuling_clinic_interior_evening_patient_wakes.png"
image bg changfeng_lou_exterior_night_rumor_crowd = "images/bg/bg_changfeng_lou_exterior_night_rumor_crowd.png"

# 飞鸿驿站

image bg feihong_inn_exterior = "images/bg/bg_feihong_inn_exterior.png"
image bg feihong_inn_interior_busy = "images/bg/bg_feihong_inn_interior_busy.png"
image bg feihong_inn_exterior_evening_invite_wangfang = "images/bg/bg_feihong_inn_exterior_evening_invite_wangfang.png"
image bg feihong_inn_exterior_evening_invite_zuowan = "images/bg/bg_feihong_inn_exterior_evening_invite_zuowan.png"
image bg feihong_inn_exterior_evening_choose_inn = "images/bg/bg_feihong_inn_exterior_evening_choose_inn.png"
image bg feihong_inn_exterior_day_busy = "images/bg/bg_feihong_inn_exterior_day_busy.png"
image bg feihong_inn_exterior_evening_full_sign = "images/bg/bg_feihong_inn_exterior_evening_full_sign.png"
image bg feihong_inn_interior_day_overflow = "images/bg/bg_feihong_inn_interior_day_overflow.png"
image bg feihong_inn_interior_day_group_distribution = "images/bg/bg_feihong_inn_interior_day_group_distribution.png"
image bg feihong_inn_interior_day_medical_alarm = "images/bg/bg_feihong_inn_interior_day_medical_alarm.png"
image bg feihong_inn_interior_day_lutiankuo_report = "images/bg/bg_feihong_inn_interior_day_lutiankuo_report.png"
image bg feihong_inn_evening_return_errand_wangfang = "images/bg/bg_feihong_inn_evening_return_errand_wangfang.png"
image bg feihong_inn_evening_return_errand_zuowan = "images/bg/bg_feihong_inn_evening_return_errand_zuowan.png"

# 夹廊小院
image bg jialang_courtyard = "images/bg/bg_jialang_courtyard.png"
image bg jialang_courtyard_evening_lodging = "images/bg/bg_jialang_courtyard_evening_lodging.png"
image bg jialang_courtyard_morning = "images/bg/bg_jialang_courtyard_morning.png"
image bg jialang_courtyard_morning_weisaner = "images/bg/bg_jialang_courtyard_morning_weisaner.png"
image bg jialang_courtyard_morning_fangdaniang_task = "images/bg/bg_jialang_courtyard_morning_fangdaniang_task.png"
image bg jialang_courtyard_night_strategy_meeting = "images/bg/bg_jialang_courtyard_night_strategy_meeting.png"
image bg jialang_courtyard_night_guoluping_orders = "images/bg/bg_jialang_courtyard_night_guoluping_orders.png"
image bg jialang_courtyard_night_lutiankuo_alarm = "images/bg/bg_jialang_courtyard_night_lutiankuo_alarm.png"
image bg jialang_courtyard_night_floor_bedding = "images/bg/bg_jialang_courtyard_night_floor_bedding.png"
image bg jialang_courtyard_dawn_after_watch = "images/bg/bg_jialang_courtyard_dawn_after_watch.png"
image bg jialang_courtyard_morning_after_watch_wake = "images/bg/bg_jialang_courtyard_morning_after_watch_wake.png"


# 长风楼
image bg changfeng_lou_exterior_day = "images/bg/bg_changfeng_lou_exterior_day.png"
image bg changfeng_lou_exterior_night_rumor = "images/bg/bg_changfeng_lou_exterior_night_rumor.png"
image bg changfeng_lou_interior_evening = "images/bg/bg_changfeng_lou_interior_evening.png"
image bg changfeng_lou_alley_night_housanxian = "images/bg/bg_changfeng_lou_alley_night_housanxian.png"

# 永乐大街暮色落脚选择

image bg yongle_street_evening_lodging_choice = "images/bg/bg_yongle_street_evening_lodging_choice.png"

# 西街菜市

image bg west_market = "images/bg/bg_west_market.png"
image bg west_market_nanbei_grocery_day = "images/bg/bg_west_market_nanbei_grocery_day.png"
image bg west_market_machangshun_qiegao_day = "images/bg/bg_west_market_machangshun_qiegao_day.png"
image bg west_market_repair_shop_day = "images/bg/bg_west_market_repair_shop_day.png"
image bg west_market_alley_youjiezai_group_day = "images/bg/bg_west_market_alley_youjiezai_group_day.png"
image bg west_market_youjiezai_clue_walk_day = "images/bg/bg_west_market_youjiezai_clue_walk_day.png"
image bg west_market_harness_shop_day = "images/bg/bg_west_market_harness_shop_day.png"
image bg west_market_qiegao_youjiezai_share_day = "images/bg/bg_west_market_qiegao_youjiezai_share_day.png"

# 雷云峰 / 风雷观

image bg fenglei_temple_three_courtyards_day = "images/bg/bg_fenglei_temple_three_courtyards_day.png"
image bg leiyunfeng_fengleiguan_intro = "images/bg/bg_leiyunfeng_fengleiguan_intro.png"
image bg fengleiguan_changxi_dingnian_dan_intro = "images/bg/bg_fengleiguan_changxi_dingnian_dan_intro.png"
image bg fenglei_temple_full_intro = "images/bg/bg_fenglei_temple_full_intro.png"

# 第一章结尾

image bg chapter1_ending_leiyunfeng_storm = "images/bg/bg_chapter1_ending_leiyunfeng_storm.png"

# 第一章结尾 / 联系方式

image bg contact_social_qr = "images/bg/bg_contact_social_qr.png"
image bg contact_social_clean = "images/bg/bg_contact_social_clean.png"

# =========================

# 立绘站位

# =========================

transform wangfang_right:

    xalign 0.82

    yalign 1.0

    zoom 0.30

transform zuowan_right:

    xalign 0.82

    yalign 1.0

    zoom 0.50

transform choose_wangfang_left:
    xalign 0.25
    yalign 1.0
    zoom 0.38

transform choose_zuowan_right:
    xalign 0.76
    yalign 1.0
    zoom 0.58

transform npc_left:
    xalign 0.18
    yalign 1.0
    zoom 0.40

transform npc_left_big:
    xalign 0.18
    yalign 1.0
    zoom 0.65

transform npc_left_big2:
    xalign 0.18
    yalign 1.0
    zoom 0.75

transform npc_left_big3:
    xalign 0.18
    yalign 1.0
    zoom 0.85

transform npc_left_big4:
    xalign 0.18
    yalign 1.0
    zoom 0.95

transform npc_left_big5:
    xalign 0.18
    yalign 1.0
    zoom 1.05

transform npc_left_big6:
    xalign 0.18
    yalign 1.0
    zoom 1.15

transform npc_left_huge:
    xalign 0.18
    yalign 1.0
    zoom 1.2

transform npc_left_huge1:
    xalign 0.18
    yalign 1.0
    zoom 1.3

transform npc_left_huge2:
    xalign 0.18
    yalign 1.0
    zoom 1.4

transform npc_left_huge3:
    xalign 0.18
    yalign 1.0
    zoom 1.5

transform npc_left_huge4:
    xalign 0.18
    yalign 1.0
    zoom 1.7

transform npc_left_tiny_fix:
    xalign 0.18
    yalign 1.0
    zoom 1.20

# 转场
define slow_dissolve = Dissolve(2.0)


# =========================

# 自动显示立绘

# =========================

init python:

    def wangfang_show_callback(event, interact=True, **kwargs):
        if event == "begin":
            renpy.show("wangfang neutral", at_list=[wangfang_right])
        elif event == "end":
            renpy.hide("wangfang")

    def zuowan_show_callback(event, interact=True, **kwargs):
        if event == "begin":
            renpy.show("zuowan neutral", at_list=[zuowan_right])
        elif event == "end":
            renpy.hide("zuowan")

    def make_npc_callback(image_tag, position):
        def callback(event, interact=True, **kwargs):
            if event == "begin":
                renpy.show(image_tag + " neutral", at_list=[position])
            elif event == "end":
                renpy.hide(image_tag)
        return callback
# =========================
# 主菜单视频
# =========================

image main_menu_movie_webm = Movie(
    play="movies/main_menu.webm",
    size=(1280, 720),
    loop=True,
    image="gui/main_menu.png"
)

image main_menu_movie_mp4 = Movie(
    play="movies/main_menu.mp4",
    size=(1280, 720),
    loop=True,
    image="gui/main_menu.png"
)

# =========================
# 角色定义 V0.2
# =========================

# 主角
define wangfang = Character(_("王放"), callback=wangfang_show_callback)
define zuowan = Character(_("左婉"), callback=zuowan_show_callback)

# 游街子
define housanxian = Character(_("侯三闲"), callback=make_npc_callback("housanxian", npc_left))
define luoxiaoliu = Character(_("罗小六"))
define maerhua = Character(_("马二花"))
define liangazhui = Character(_("梁阿坠"))
define duqiniang = Character(_("杜七娘"))
define qiansixi = Character(_("钱四喜"))

# 飞鸿驿站
define guoluping = Character(_("郭路平"), callback=make_npc_callback("guoluping", npc_left_big2))
define fangheming = Character(_("方鹤鸣"), callback=make_npc_callback("fangheming", npc_left_big3))
define lutiankuo = Character(_("鲁天阔"), callback=make_npc_callback("lutiankuo", npc_left_huge2))
define zhouerdan = Character(_("周二蛋"), callback=make_npc_callback("zhouerdan", npc_left_big3))
define fangdaniang = Character(_("方大娘"), callback=make_npc_callback("fangdaniang", npc_left_huge1))
define weisaner = Character(_("魏三儿"), callback=make_npc_callback("weisaner", npc_left_big3))
define luoazao = Character(_("罗阿枣"), callback=make_npc_callback("luoazao", npc_left_big2))

# 茯苓医馆
define xuchunxiang = Character(_("徐春香"), callback=make_npc_callback("xuchunxiang",npc_left_huge))
define chengmingzhu = Character(_("程明珠"), callback=make_npc_callback("chengmingzhu", npc_left_big))
define chensumei = Character(_("陈素梅"), callback=make_npc_callback("chensumei", npc_left_huge4))
define zhouqingliu = Character(_("周青柳"), callback=make_npc_callback("zhouqingliu", npc_left_big5))
define limo = Character(_("李默"), callback=make_npc_callback("limo", npc_left_big))
define shenyun = Character(_("沈云"), callback=make_npc_callback("shenyun", npc_left_big4))
define shenxingchen = Character(_("沈星辰"), callback=make_npc_callback("shenxingchen", npc_left_big))

# 银花庵
define mingjingfashi = Character(_("明镜法师"))
define jingting = Character(_("静亭"))
define jingsong = Character(_("静松"))
define axiang = Character(_("阿香"))

# 长风楼 / 酒楼
define xinwanhe = Character(_("辛万和"))
define shuoshuren = Character(_("说书人"))
define jianghuke = Character(_("江湖客"))
define jianghukejia = Character(_("江湖客甲"))
define jianghukeyi = Character(_("江湖客乙"))
define jianghukebing = Character(_("江湖客丙"))

# 西街菜市 / 商铺
define chendasao = Character(_("陈大嫂"))
define wusanniang = Character(_("吴三娘"))
define heawang = Character(_("何阿旺"))
define houxiaoman = Character(_("侯小满"))
define caotieshan = Character(_("曹铁山"))
define liushanping = Character(_("刘山平"))
define liuxiaoxiao = Character(_("刘小小"))
define fanyoucheng = Character(_("范有成"))
define xiaomazi = Character(_("小麻子"))
define machangshun = Character(_("马长顺"))
define songlaoliu = Character(_("宋老六"))

# 风云坪 / 官府 / 王家
define baochangshan = Character(_("包长山"))
define xiaoqing = Character(_("小庆"))
define wangdejiu = Character(_("王德久"))
define wangqingwan = Character(_("王清莞"))
define xunbusi_chayi = Character(_("巡捕司差役"))

# 绯红院
define zhangmama = Character(_("张妈妈"))
define xiuzhu = Character(_("秀珠"))
define gaochangchun = Character(_("郜长春"))

# 风雷观
define yunqingdaozhang = Character(_("云清道长"))
define xuanhengzhenren = Character(_("玄蘅真人"))
define xuanyuezhenren = Character(_("玄岳真人"))
define xuanshuangzhenren = Character(_("玄霜真人"))
define qingxiao = Character(_("清骁"))
define fengleiguan_dizi = Character(_("风雷观外门弟子"))

# 临时通用人物

define keren = Character(_("客人"))

define keshang = Character(_("客商"))

define bingren = Character(_("病人"))

define zhenmin = Character(_("镇民"))

define nanzi = Character(_("男子"))

define nvzi = Character(_("女子"))

define xunbu = Character(_("巡捕"))

define unknown = Character(_("？？？"))

# 临时编号人物

define zhenmin_jia = Character(_("镇民甲"))

define zhenmin_yi = Character(_("镇民乙"))

define nanzi_jia = Character(_("男子甲"))

define nanzi_yi = Character(_("男子乙"))

define nvzi_jia = Character(_("女子甲"))

define nvzi_yi = Character(_("女子乙"))

define jianghuke_jia = Character(_("江湖客甲"))

define jianghuke_yi = Character(_("江湖客乙"))

define jianghuke_bing = Character(_("江湖客丙"))

# 临时特征人物

define huafu_nvzi = Character(_("华服女子"))

define huitou_jianghuke = Character(_("灰衣江湖客"))

define baofa_laoren = Character(_("白发老人"))

define baofu_shaonian = Character(_("抱袱少年"))

# 特定剧情临时人物

define gaoge_nanzi = Character(_("高个男子"))

define aige_nanzi = Character(_("矮个男子"))

define shangzhe = Character(_("伤者"))

# =========================
# 变量默认值
# =========================

default protagonist = None
default base_place = None
default hou_sanxian_relation = 0
default hou_sanxian_first_choice = None
default heard_dingnian_dan_rumor = False
default helped_feihong_inn = False
default helped_fuling_clinic = False
default chapter1_finished = False

# =========================
# 音乐文件 V0.1
# =========================
# bgm_daily_jianghu.mp3   开场/主线叙事
# bgm_sad_jianghu.mp3   凄凉 / 孤独 / 失落 / 夜路 / 回忆 / 身世 / 荒野感
# bgm_tension_fenglei.mp3 悬疑紧张/丹药失窃
# bgm_prologue_fenglei_pulse.mp3 江湖感/开场介绍各个门派
# bgm_main_menu_fenglei.mp3 主菜单音乐/大气磅礴

label music_daily:
    play music "audio/bgm/bgm_daily_jianghu.mp3" fadeout 1.0 fadein 1.0
    return

label music_sad:
    play music "audio/bgm/bgm_sad_jianghu.mp3" fadeout 1.0 fadein 1.0
    return

label music_tension:
    play music "audio/bgm/bgm_tension_fenglei.mp3" fadeout 0.8 fadein 0.8
    return

label music_main_menu:
    play music "audio/bgm/bgm_main_menu_fenglei.mp3" fadeout 1.0 fadein 1.0
    return

label music_prologue_fenglei:
    play music "audio/bgm/bgm_prologue_fenglei_pulse.mp3" fadeout 1.0 fadein 1.0
    return

# =========================
# 游戏开始
# =========================

label start:

    jump s001_prologue

label debug_s020:

    $ protagonist = "wangfang"

    $ base_place = "feihong_inn"

    $ hou_sanxian_relation = 2

    $ hou_sanxian_first_choice = "lend"

    $ heard_dingnian_dan_rumor = True

    $ helped_feihong_inn = True

    $ helped_fuling_clinic = True

    jump s020_night_return_base

label debug_s020_wangfang:

    $ protagonist = "wangfang"
    $ base_place = "feihong_inn"
    $ hou_sanxian_relation = 2
    $ hou_sanxian_first_choice = "lend"
    $ heard_dingnian_dan_rumor = True
    $ helped_feihong_inn = True
    $ helped_fuling_clinic = True

    jump s020_night_return_base


label debug_s020_zuowan:

    $ protagonist = "zuowan"
    $ base_place = "feihong_inn"
    $ hou_sanxian_relation = 2
    $ hou_sanxian_first_choice = "lend"
    $ heard_dingnian_dan_rumor = True
    $ helped_feihong_inn = True
    $ helped_fuling_clinic = True

    jump s020_night_return_base

label debug_s008:

    $ protagonist = "wangfang"

    $ hou_sanxian_relation = 1

    $ hou_sanxian_first_choice = "lend"

    jump s008_fengyun_ping

label debug_wangfang_sprite:

    scene bg fengyunping

    wangfang "我叫王放。"

    wangfang "今日入开庵镇，只为见一见真正的江湖。"

    "如果你看到我，说明王放自动立绘加载成功。"

    return

label debug_zuowan_sprite:

    scene bg fengyunping

    zuowan "我叫左婉。"

    zuowan "药能救人，也能害人。要看谁炼，又要看谁抢。"

    "如果你看到左婉说话时出现，说完后消失，说明左婉自动立绘测试成功。"

    return

label debug_s016:

    $ protagonist = "wangfang"
    $ base_place = "feihong_inn"
    $ hou_sanxian_relation = 1
    $ hou_sanxian_first_choice = "lend"
    $ heard_dingnian_dan_rumor = True

    jump s016_inn_overflow


# =========================
# S001｜天下风雷动
# =========================

label s001_prologue:


    call music_prologue_fenglei from _call_music_prologue_fenglei_1
    scene bg main_menu_world_map_source with dissolve

    "大明国，庆丰年间。"

    "这不是史书里的大明。"

    "它西邻大迹国，北接大稀国，东临沧澜海，南望南渊海。"

    "京城之东三百里，有凰龙府。"

    scene bg leiyunfeng_fengleiguan_intro with dissolve

    "凰龙府北有雷云峰，峰顶常年云雷缭绕。"

    "雷云峰山腰，坐落着北境道宗——风雷观。"

    "江湖表面平静，实则一强、两衡、三隐彼此制衡。"

    scene bg chengtian_sword_sect_intro with dissolve

    "一强者，拱京府承天剑派。"

    "位于拱京府承天峰。"

    "承天峰为大明第三高峰，峰顶原为承天观旧址，后来成为承天剑派立派之地。"

    "承天剑派控扼中原水陆要道，门下分舵遍布拱京府、碧溪府、西京府。"

    "在大明江湖诸派之中，它是实力最强、声望最高，也最不容旁人轻视的一派。"

    scene bg fenglei_temple_full_intro with dissolve

    "两衡者之一，北境风雷观"

    "雷云峰为凰龙府第一险峰，峰顶常年云雷缭绕，山势高峻，外山险道极多。"

    "风雷观依雷云峰山势而建，分玄雷院、清阳院、栖霞院三院。"

    "风雷观以雷法、符箓、护道术与丹道闻名北境。"

    "在大明江湖诸派之中，它未必最强，却最神秘，也最少有人敢轻易上山试探。"

    scene bg wutian_chan_monastery_intro with dissolve

    "两衡者之二，南境梧天禅院。"

    "位于苍梧府苍梧天柱。"

    "苍梧天柱为大明第一高峰，山腰常年云海翻涌，梧天禅院便藏于云海之间。"

    "禅院与苍梧府苗寨、瑶寨相邻，弟子多懂南疆医术、解毒之法与山中秘术。"

    "梧天禅院以一道禅墙分男众区、女众区。"

    "男众区有慧能大师居所、罗汉堂与藏经楼；女众区有静月师太居所、观音堂与解毒坊。"

    "解毒坊与茯苓医馆共享《南疆解毒谱》，因此禅院虽远在南疆，却与凰龙府医馆暗有往来。"

    "慧能大师慈悲为怀，不喜争斗，但禅武修为深不可测。"

    "静月师太虽为女众，却是慧能大师的俗家弟子，未剃度，负责南疆苗寨义诊，也能自由出入男众区议事。"

    "在大明江湖诸派之中，梧天禅院不是最锋利的一派，却是最能救人，也最懂得如何让人活下去的一派。"

    
    scene bg canghai_pavilion_intro with dissolve

    "三隐者之一，东海秘宗——沧海阁。"

    "其地理根基在东极府东极岛外海的浮槎岛。"

    "浮槎岛随潮汐隐现，平日不见其形，唯有熟知海潮与星象之人，才能寻到入岛之路。"

    "沧海阁弟子多以渔民、船夫、海商身份行走江湖，明面低调，暗中布网。"

    "他们精通航海、潮汐、星象与奇门遁甲，既能在海上寻路，也能在人心之间设局。"

    "在大明江湖诸派之中，沧海阁不是最常现身的一派，却是最难追踪、最难看清来意的一派。"

    
    scene bg wandu_valley_intro with dissolve

    "三隐者之二，北漠万毒谷。"

    "位于飞沙府黄风沙海深处。"

    "黄风沙海位于大明正北，常年风沙蔽日，寻常人入内，十有八九再难出来。"

    "万毒谷谷口藏在流沙漩涡之后，只有手持特制罗盘，才能在风沙与流沙之间辨出真正入口。"

    "谷内挖有地下暗河，借暗河之水养活门人，也借它避开沙漠中最致命的缺水之困。"

    "万毒谷弟子擅长在沙下埋设毒陷阱，外人往往还未看见谷门，便已经踏入杀局。"

    "他们所用毒物多取自飞沙府本土：沙蝎、沙蛇、毒蜥蜴，甚至还有传闻中的沙漠食人花。"

    "这些毒素多半慢发、难察，正如北漠风沙，看似平静，实则处处藏险。"

    "在大明江湖诸派之中，万毒谷不是最常现身的一派，却是最让人不愿招惹的一派。"

    
    scene bg hengyun_hall_intro with dissolve

    "三隐者之三，市井隐宗——衡云堂。"

    "其地理根基在广阳府云衡山脚下的七侠镇。"

    "与高山大派不同，衡云堂没有固定山门。"

    "它的弟子多是市井百姓：铁匠、货郎、厨子、木匠、羊夫、药贩，甚至还有茶楼跑堂与街边小贩。"

    "他们平日各做各的营生，看起来不过是镇上最寻常的人。"

    "可一旦百姓受欺、街坊遭难，这些人便会从炉火、挑担、灶台与摊棚后站出来。"

    "衡云堂奉行藏于市井，守护百姓。"

    "在大明江湖诸派之中，它不是最显赫的一派，却是最难被连根拔起的一派。"

    "因为只要市井还在，衡云堂就还在。"


    scene bg fengleiguan_changxi_dingnian_dan_intro with dissolve

    "而近日，风雷观云清道长开炉炼制一枚丹药。"

    "其名——长息定年丹。"

    "有人说，此丹能延续元息，暂缓衰败。"

    "有人说，此丹能定住年岁，使人青春不老。"

    "也有人说，这根本不是丹药，而是一场足以搅动江湖的局。"

    "云清道长，女，五十八岁，法名云清，因雷法与丹道修为深厚，尊号清玄真人。"

    "她性情刚烈，心怀苍生，年轻时曾游历西域，习得一身道家绝学。"

    "风雷观弟子敬她、畏她，也相信她绝不会无故开炉。"

    scene bg kaian_town_intro with dissolve

    "于是，江湖豪杰、商旅富户、病人、骗子、看客，全都涌向凰龙府开庵镇。"
    

    scene bg fengyunping_crowd_arrival_day with dissolve

    "有人求丹。"

    "有人抢丹。"

    "有人看热闹。"

    "也有人，还不知道自己会被卷进什么样的江湖。"

    "这一日，开庵镇南门先后来了两个人。"

    "一人步伐急促，像是被什么东西一路推着往前。"

    "一人步伐沉稳，像是早已决定自己要往哪里去。"

    "人群、车马、叫卖声一同涌来。"

    "开庵镇，就这样把他们吞进了自己的烟火气里。"

    jump s002_choose_protagonist


# =========================
# S002｜主角选择
# =========================

label s002_choose_protagonist:

    scene bg kaian_town_intro

    call music_daily from _call_music_daily_1

    "开庵镇南门，永乐大街与通禅道交汇处。"

    "人潮正往镇中风云坪方向涌去。"

    "两名年轻人，也在此时来到开庵镇。"

    show wangfang_select at choose_wangfang_left

    show zuowan_select at choose_zuowan_right

    "你要选择谁，作为第一章的主角？"

    menu:

        "王放｜18岁，热血少年，立志成为真正的大侠":

            $ protagonist = "wangfang"
            hide zuowan_select
            hide wangfang_select

            "王放。"

            "十八岁，热血，理想主义，憧憬成为大侠。"

            "他听闻雷云峰风雷观开炉炼制长息定年丹，各路豪杰齐聚凰龙府，便觉得真正的江湖人就该去风雷云动之处。"

            "他带着三百文钱，一把不算名贵的刀，和一腔过分明亮的热血，踏入了开庵镇。"

            hide wangfang_select

            wangfang "既然江湖来了，我总不能站在门外看。"

        "左婉｜20岁，外向灵动，擅长控制类武功与草药":

            $ protagonist = "zuowan"

            hide zuowan_select
            hide wangfang_select

            "左婉。"

            "二十岁，活泼外向，擅长控制类武功，也懂一些草药和调息之法。"

            "她听闻长息定年丹牵涉气脉、草木灵材与定息之术，心中隐隐觉得此事不会只是求丹这么简单。"

            "她来到开庵镇，不为抢丹，只为看清这场风波到底会害多少人。"

            hide zuowan_select

            zuowan "药能救人，也能害人。要看谁炼，又要看谁抢。"

    "选择已完成。"

    if protagonist == "wangfang":
        "你将以王放的身份，进入开庵镇。"
    else:
        "你将以左婉的身份，进入开庵镇。"

    jump s003_hou_sanxian


# =========================
# S003｜三文钱的江湖
# =========================

label s003_hou_sanxian:

    scene bg fengyunping

    "南门入镇后的永乐大街，人潮正往风云坪方向涌去。"

    "江湖客、商旅、马匹、摊贩挤在一处，空气里混着尘土、热汤、马汗和新鲜菜叶的味道。"

    if protagonist == "wangfang":
        "王放刚站稳，还没来得及细看这座小镇，就听见墙边有人冲他吹了一声口哨。"
    else:
        "左婉刚站稳，正打量着街边铺面，就听见墙边有人冲她轻轻咳了一声。"

    "墙边靠着一个少年。"

    "他个子偏高，红色发带束着长发，腰间挂着一把木刀。"

    "明明衣衫并不阔气，却偏要摆出几分江湖人的架势。"

    housanxian "这位朋友，看你像江湖中人。"

    housanxian "初来开庵镇吧？"

    if protagonist == "wangfang":
        wangfang "你怎么知道？"
    else:
        zuowan "这也看得出来？"

    housanxian "这还不容易？本地人走路不看牌匾，外乡人走三步看两回。"

    housanxian "我叫侯三闲。风云坪、西街菜市、长风楼外墙根，哪儿我都熟。"

    housanxian "你要找路，问我。要听消息，也问我。"

    "他说到这里，忽然压低声音，像要讲什么天大的秘密。"

    housanxian "不过江湖有江湖的规矩。"

    if protagonist == "wangfang":
        wangfang "什么规矩？"
    else:
        zuowan "你先说。"

    housanxian "借我三文钱。"

    "他说得理直气壮。"

    housanxian "明日必还。"

    "你看了看他。"

    "他眼神飘了一下，又立刻挺直腰杆，仿佛这不是借钱，而是在考验你的江湖气。"

    menu:

        "借他三文钱":

            $ hou_sanxian_relation += 1
            $ hou_sanxian_first_choice = "lend"

            "你取出三文钱，递给侯三闲。"

            "侯三闲眼睛一亮，立刻接过，动作快得不像一个讲究江湖风度的人。"

            housanxian "痛快！"

            housanxian "我就说你有江湖气。"

            housanxian "以后在开庵镇，有事报我侯三闲的名号。"

            if protagonist == "wangfang":
                wangfang "报了有用吗？"
            else:
                zuowan "你这名号，管用吗？"

            housanxian "看情况。"

            housanxian "大事不一定管用，小事多半能添点乱。"

        "不借":

            $ hou_sanxian_first_choice = "refuse"

            "你没有掏钱。"

            if protagonist == "wangfang":
                wangfang "我也初来乍到，钱不多。"
            else:
                zuowan "你这借法，听着不像明日必还。"

            housanxian "啧。"

            housanxian "江湖人也有手紧的时候。理解，理解。"

            "他说理解，脸上却写着一点不服。"

            housanxian "不过不借也行。"

            housanxian "我侯三闲不是那种三文钱就翻脸的人。"

            "他顿了顿。"

            housanxian "五文可能会。"

        "让他跑腿抵债":

            $ hou_sanxian_relation += 1
            $ hou_sanxian_first_choice = "runner"

            if protagonist == "wangfang":
                wangfang "钱可以借，不过你得替我跑一趟腿。"
            else:
                zuowan "借钱可以。你拿消息和跑腿来抵。"

            housanxian "跑腿？"

            "侯三闲像是受了点羞辱，立刻拍了拍腰间的木刀。"

            housanxian "我侯三闲是干大事的人。"

            "他停了停，又凑近一点。"

            housanxian "不过你先说跑哪儿。"

            housanxian "近的算江湖义气，远的得另加钱。"

        "问他雷云峰消息":

            $ hou_sanxian_first_choice = "ask_rumor"

            if protagonist == "wangfang":
                wangfang "钱的事先不急。你知道雷云峰的消息吗？"
            else:
                zuowan "三文钱先放一边。你知道风雷观开炉的事吗？"

            "侯三闲脸上的嬉笑顿了一下。"

            housanxian "一来就问雷云峰？"

            housanxian "你不是普通看热闹的啊。"

            "他左右看了看，声音压低。"

            housanxian "最近镇上十个人里有八个都为那枚丹来的。"

            housanxian "有人说它能长生，有人说它能续命，还有人说风雷观要借它收服江湖。"

            housanxian "你问我真假？"

            housanxian "我只能说，假的传得快，真的没人敢大声讲。"

    "不管刚才如何回应，侯三闲都没有离开。"

    "他拍了拍衣摆上的灰，忽然摆出一副带路人的模样。"

    housanxian "行了。你初来开庵镇，若没人带，走到天黑都分不清哪儿能吃饭，哪儿会挨宰。"

    if hou_sanxian_first_choice == "lend":
        housanxian "看在你有江湖气的份上，我带你简单转转。"
    elif hou_sanxian_first_choice == "refuse":
        housanxian "看在你虽然小气但还算坦诚的份上，我带你简单转转。"
    elif hou_sanxian_first_choice == "runner":
        housanxian "看在咱们已经有跑腿交情的份上，我带你简单转转。"
    else:
        housanxian "看在你一来就问雷云峰的份上，我带你简单转转。省得你被真消息假消息一起砸晕。"

    if protagonist == "wangfang":
        wangfang "你要带我去哪儿？"
    else:
        zuowan "先看哪里？"

    housanxian "先去西街菜市。"

    housanxian "要认识一座镇，不能先看楼有多高，得先看菜卖多少钱。"

    call music_daily from _call_music_daily_2

    "侯三闲转身走入人流。"

    "你跟了上去。"

    jump s004_placeholder


# =========================
# S004 占位
# =========================

# =========================
# S004 占位入口：自动跳转到真正 S004
# =========================

label s004_placeholder:

    jump s004_west_market


# =========================
# S004｜西街菜市导览
# =========================

label s004_west_market:

    scene bg west_market

    "侯三闲带着你从南门附近转入西街菜市。"

    "才走几步，风云坪那边的人声便被菜市的喧闹盖了过去。"

    "这里有菜叶上的水珠，有鸡笼里的扑腾声，有鱼腥味，也有远处铁锤落下的叮当声。"

    housanxian "看见没？这才是开庵镇真正的脸。"

    if protagonist == "wangfang":
        wangfang "这里比我想的热闹多了。"
    else:
        zuowan "菜市、铁铺、武馆都挤在一起，倒是有意思。"

    housanxian "那当然。"

    housanxian "你要认识一座镇，不能先看楼有多高，得先看菜卖多少钱。"

    "侯三闲说得一本正经，仿佛自己是开庵镇的正经向导。"

    "菜摊边，一个卖青菜的大嫂正把一把青菜往筐里摔。"

    "她一眼看见侯三闲，立刻叉腰。"

    chendasao "侯三闲！你上回说替我搬菜，搬到一半人没了，菜筐还在地上！"

    housanxian "陈大嫂，那叫江湖急事。"

    chendasao "你哪天没有江湖急事？"

    housanxian "这说明我江湖事多。"

    "陈大嫂瞪了他一眼，却也没真赶人。"

    "再往前走，吴三娘的豆腐摊前围着几个买菜的妇人，何阿旺的南瓜堆得像一座小山，侯小满正蹲在葱蒜摊后头打瞌睡。"

    "侯三闲一边走，一边压低声音介绍。"

    housanxian "菜摊是镇民的饭碗。"

    housanxian "铸兵堂是江湖人的胆子。"

    housanxian "火铸铺是百姓的锅铲。"

    housanxian "武馆是年轻人做梦的地方。"

    if protagonist == "wangfang":
        wangfang "武馆？"
    else:
        zuowan "你还知道武馆？"

    housanxian "我当然知道。"

    housanxian "赵启武馆主，拳头比菜市的秤砣还硬。"

    housanxian "不过我没去练过。"

    if protagonist == "wangfang":
        wangfang "为什么？"
    else:
        zuowan "你不是想当江湖人吗？"

    housanxian "练武要交钱。"

    housanxian "我这种人，适合先从江湖气练起。"

    "远处，铸兵堂传来打铁声。"

    "一个膀大腰圆的铁匠抬头看了侯三闲一眼。"

    caotieshan "侯三闲，别在我门口骗外乡人。"

    housanxian "曹师傅，我这是带路，不是骗人。"

    caotieshan "你带路和骗人，中间就差三文钱。"

    "侯三闲立刻假装没听见，脚下走得更快。"

    "你注意到，菜市之外再往西，街道渐渐变宽，隐约能看见兵营方向的旗影。"

    housanxian "再往西，就是西郊兵营。"

    housanxian "真惹了事，跑都跑不远。"

    housanxian "所以你以后在菜市混，第一要识路，第二要识人，第三要识方大娘的锅铲。"

    if protagonist == "wangfang":
        wangfang "方大娘又是谁？"
    else:
        zuowan "方大娘听起来很厉害。"

    housanxian "飞鸿驿站的厨娘。"

    housanxian "她骂人不算江湖武功，但胜似江湖武功。"

    "侯三闲带你从西街菜市东口出来。"

    "身后的嘈杂声渐渐远了，前方的街道忽然安静许多。"

    "树影后露出一片古旧屋檐。"

    housanxian "走，带你去银花庵。"

    housanxian "开庵镇这个名字，就从那里来。"

    jump s005_yinhua_an


# =========================
# S005｜银花庵导览
# =========================

label s005_yinhua_an:

    scene bg yinhua_an_exterior_day

    call music_daily from _call_music_daily_3

    "穿过庵前衢后，西街菜市的烟火气像被风轻轻拂开。"

    "前方树影深处，一座古旧尼庵静静立着。"

    "庵前有小茶舍，茶香淡淡。"

    "门边的石阶被岁月磨得发亮。"

    housanxian "这就是银花庵。"

    housanxian "开庵镇之所以叫开庵镇，就是因为这座庵。"

    if protagonist == "wangfang":
        wangfang "一座庵，能让整座镇得名？"
    else:
        zuowan "看来这座庵来历不浅。"

    housanxian "老人们说，银花庵冬日会起雾凇。"

    housanxian "一夜过去，满树白花，远看像银子开了花。"

    housanxian "还有人说，凰龙府的‘凰’字，也跟这里的旧传有关。"

    "侯三闲说到这里，故意压低声音。"

    housanxian "听说很久以前，这地方见过玄灵九羽凰。"

    if protagonist == "wangfang":
        wangfang "凤凰？"
    else:
        zuowan "玄灵九羽凰？"

    housanxian "我也没见过。"

    housanxian "我要是见过，现在就不是侯三闲了。"

    housanxian "至少也得叫侯九羽。"

    "你们刚走到庵门前，一个神情严肃的尼姑便从院中走了出来。"

    "她目光一扫，直接落在侯三闲身上。"

    jingting "侯三闲。"

    "侯三闲立刻站直。"

    housanxian "静亭师太，许久不见，风采更胜从前。"

    jingting "前日你说来扫院。"

    housanxian "是有这么一段缘分。"

    jingting "扫帚还在，人不见了。"

    housanxian "那日我临时被江湖急事调走。"

    jingting "被谁调走？"

    housanxian "命运。"

    "静亭看着他，没有说话。"

    "侯三闲咳了一声，赶紧往旁边挪了半步。"

    housanxian "我今日只是带外乡朋友认认路，绝不添乱。"

    "静亭看了你一眼，神情依旧冷淡，却没有阻拦。"

    "院内传来一阵轻轻的笑声。"

    "远处，一位年长法师正坐在廊下，与一名年轻尼姑说话。"

    "年轻尼姑手里似乎还藏着半块桂花糕。"

    mingjingfashi "修行不是不许吃。"

    jingsong "师父英明。"

    mingjingfashi "是吃了要记账。"

    jingsong "弟子记在心里了。"

    mingjingfashi "那你心里欠阿香三块桂花糕。"

    "茶舍里的阿香探出头来。"

    axiang "师父，已经四块了。"

    "静松立刻把手里的桂花糕藏得更深。"

    "侯三闲憋着笑。"

    housanxian "看见没？银花庵清静归清静，也不是没热闹。"

    "你站在庵前，忽然觉得这座小镇不只是酒楼、菜市和江湖客。"

    "它还有旧传、钟声、雾凇、茶香，以及一些被人轻轻记住的小事。"

    "静亭又看了侯三闲一眼。"

    "侯三闲立刻后退。"

    housanxian "走走走。再待下去，我怕她真让我扫院。"

    scene bg yongle_changfeng_intersection_day

    "你们离开银花庵，沿庵前衢向东，穿过永乐大街。"

    "远处渐渐传来酒盏碰撞与人声喧哗。"

    housanxian "前面就是长风楼。"

    jump s006_changfeng_lou


# =========================
# S006｜长风楼导览
# =========================

label s006_changfeng_lou:

    call music_daily from _call_music_daily_4

    "越往长风衢走，人声越盛。"

    "还未到长风楼门口，你便听见楼上传来酒盏碰撞声、马夫喊价声，以及江湖客争座的声音。"

    "长风楼高挂灯笼，门前车马不断。"

    "不远处，青云楼的招牌也很惹眼，像是不服气似的与长风楼遥遥相对。"

    scene bg changfeng_lou_exterior_day

    housanxian "长风楼，开庵镇最大的酒楼之一。"

    housanxian "青云楼，长风楼最不服气的对头。"

    housanxian "平日里两家抢客，今日两家抢江湖客。"

    if protagonist == "wangfang":
        wangfang "这么多人，都是为长息定年丹来的？"
    else:
        zuowan "看来长息定年丹的消息，已经把镇子搅起来了。"

    housanxian "可不是嘛。"

    housanxian "有人来求丹，有人来抢丹，有人来卖假消息。"

    housanxian "还有人纯粹来喝酒，顺便假装自己知道内幕。"

    "长风楼门前，一名掌柜模样的中年人正满面笑容地迎客。"

    "他的笑看起来热情，眼神却一直扫着人群。"

    housanxian "那位就是辛万和，辛掌柜。"

    housanxian "别看他笑得像谁都是贵客，其实谁有钱、谁没钱、谁会闹事，他一眼就能看出来。"

    "辛万和正与一名华服客人低声交谈。"

    "那人衣料讲究，腰间有一枚温润玉佩，身后还跟着两个沉默随从。"

    "侯三闲立刻压低声音。"

    housanxian "大人物。"

    if protagonist == "wangfang":
        wangfang "你认识？"
    else:
        zuowan "是谁？"

    housanxian "大人物的名字，岂是随便说的？"

    if protagonist == "wangfang":
        wangfang "所以你不认识。"
    else:
        zuowan "所以你不知道。"

    housanxian "江湖上，有些不知道，叫留白。"

    "这时，辛万和看见侯三闲，笑容不变，声音却抬高了一点。"

    xinwanhe "侯三闲，别在门口扰客。"

    housanxian "辛掌柜，这话就外道了。"

    housanxian "我这是替长风楼招待外乡贵客。"

    xinwanhe "那贵客付钱，你别赊账。"

    "侯三闲立刻转身。"

    housanxian "走。"

    housanxian "长风楼这种地方，白天看门面，晚上听消息。"

    housanxian "现在还早，晚些时候才热闹。"

    "你回头看了一眼长风楼。"

    "楼内已经有人在谈雷云峰，有人说定年丹能锁住年岁，有人说那是风雷观放出的假消息。"

    "这些话还只是零散传言。"

    "但你隐隐觉得，等夜色落下，它们会变成更大的风。"

    "侯三闲带你继续往东。"

    scene bg changfeng_kaian_intersection_day

    "穿过开庵街后，前方灯彩渐艳，人声也变得婉转。"

    housanxian "前面是绯红院。"

    jump s007_feihong_yuan


# =========================
# S007｜绯红院导览
# =========================

label s007_feihong_yuan:

    call music_daily from _call_music_daily_5

    "还未走近绯红院，先听见丝竹声、鼓点声和叫好声。"

    scene bg feihong_yuan_exterior_day

    "门前灯彩虽然还未点亮，但是颜色比长风楼还艳，几名跑堂和看客来来往往。"

    "这里不像酒楼那样喧哗，却处处透着热闹。"

    "有人听曲，有人看杂耍，有人只是在门前站一会儿，便像已经沾了几分风流气。"

    "一名衣着鲜亮的中年女子站在门前招呼客人，声音又亮又圆。"

    zhangmama "诸位客官，里头有新曲，有武戏，有杂耍，今日不看，明日可就不是今日价了！"

    housanxian "张妈妈，张惜花。"

    housanxian "嗓门一开，能把风云坪的人都喊回头。"

    if protagonist == "wangfang":
        wangfang "这里是青楼？"
    else:
        zuowan "这里就是绯红院？"

    housanxian "别说得那么窄。"

    housanxian "绯红院里有唱曲的，有说笑话的，有演武戏的，也有江湖客喝多了说漏嘴的。"

    housanxian "看美人只是表面，听消息才是门道。"

    "二楼窗前，一个女子以团扇掩面，只露出半张脸。"

    "楼下有人抬头看，有人假装不看。"

    housanxian "那位是秀珠。"

    housanxian "听说原名赵芷薇。"

    housanxian "她一开嗓，长风楼那边的酒都能少卖半壶。"

    if protagonist == "wangfang":
        wangfang "你连这个都知道？"
    else:
        zuowan "你倒是很熟。"

    housanxian "江湖消息，需多方采集。"

    "张妈妈远远看见侯三闲，立刻笑着喊。"

    zhangmama "侯三闲，你上回说替我介绍三位贵客，贵客呢？"

    housanxian "贵客这不还在路上嘛。"

    housanxian "江湖路远，急不得。"

    zhangmama "你这张嘴，迟早比我的灯笼还亮。"

    "侯三闲赶紧拉着你往旁边走。"

    housanxian "快走。"

    housanxian "看久了怕被收钱。"

    if protagonist == "wangfang":
        wangfang "我可是正经大侠，这种地方是不会随便来的。"
    else:
        zuowan "我可是正经侠女，这种地方是不会随便来的。"

    housanxian "正经人都这么说。"

    "他笑了笑，指向前方开阔处。"

    housanxian "走，我再带你去一个真正江湖人该看的地方。"

    if protagonist == "wangfang":
        wangfang "哪里？"
    else:
        zuowan "什么地方？"

    housanxian "风云坪。"

    housanxian "开庵镇的心口子。"

    housanxian "人要出名，事要闹大，都得从那儿过。"

    jump s008_fengyun_ping


# =========================
# S008｜风云坪分别
# =========================

label s008_fengyun_ping:

    scene bg fengyunping_day

    call music_daily from _call_music_daily_6
    
    "侯三闲带你来到风云坪。"

    "这里比前面几处都开阔。"

    "地面被车马压得发亮，四面街道都像河流一样汇到这里。"

    "东侧是府衙、公署、巡捕司和监狱一带。"

    "西侧从北往南，依次能看见飞鸿驿站、雷凌宫、茯苓医馆。"

    "不远处还有保寿堂、正骨轩和孙记面摊。"

    housanxian "看见没？"

    housanxian "开庵镇要是一个人，风云坪就是心口。"

    "路过监狱外侧时，一名狱卒正抱着腰刀出来透气。"

    "他看见侯三闲，竟然熟络地喊了一声。"

    baochangshan "三闲，又在给外乡人带路？"

    housanxian "包大哥，这叫接待江湖贵客。"

    "包长山笑骂。"

    baochangshan "你少把贵客带进牢里来就行。"

    "侯三闲立刻挺胸。"

    housanxian "我侯三闲行走江湖，靠的就是一个稳字。"

    baochangshan "你稳？你上回翻墙摔下来，在牢门口躺了半个时辰。"

    housanxian "那是观测地形。"

    "你第一次发现，侯三闲虽然像个混街少年，却确实认识不少镇上的人。"

    "二人走过孙记面摊。"

    "锅里热气腾腾，雪菜肉丝面的香味飘过来。"

    "侯三闲停了一下。"

    housanxian "这家面，镇上一绝。"

    housanxian "尤其是别人请的时候，格外好吃。"

    "你装作没听懂。"

    "侯三闲等了一会儿，发现没下文，只好悻悻摆手。"

    housanxian "算了，今日江湖事忙。"

    "他指了指西街方向。"

    housanxian "以后要找我，就去西街菜市。"

    housanxian "别问摊主，问了他们也说我欠钱。"

    housanxian "你就说找侯三闲，他们骂两句就知道我在哪儿。"

    if protagonist == "wangfang":
        wangfang "听起来你人缘不错。"
    else:
        zuowan "听起来你欠得很广。"

    housanxian "江湖上，认识的人越多，误会越多。"

    "侯三闲挥挥手，转身混入人群。"

    "你独自穿过风云坪。"

    "飞鸿驿站门口最热闹。"

    "马匹、行李、商旅和江湖客挤在一起。"

    "一个年轻女子正在门前招呼客人，嘴快手也快，一边登记，一边让人别堵门。"

    "她应该就是驿站的人。"

    "再往南，雷凌宫门前富丽堂皇。"

    "王家小厮小庆站在门口，有路人上前询问什么，他眼皮都不抬，只冷淡地回了一句。"

    "雷凌宫的高墙在夕光里显得格外沉。"

    "茯苓医馆再往南些，门口药香淡淡。"

    "在医馆南侧，还能看见一间药铺，门口挂着醒目的大招牌：保寿堂。"

    "招牌旁另悬一块小匾，字写得比正招牌还大——“金枪不倒丸”。"

    "路过的江湖客有人假装没看见，有人看了又回头。"

    "相比保寿堂招牌的张扬，茯苓医馆显得安静许多。"

    "医馆门口，一个年轻男子正坐在门边晒太阳，手里拨弄着一小捆草药。"

    "风云坪人来人往。"

    "你忽然意识到，自己真的踏进了这座小镇的中心。"

    "相比雷凌宫的冷淡和医馆的安静，飞鸿驿站门口那个年轻女子看起来最容易开口。"

    "也许可以先向她打听打听开庵镇的规矩。"

    "你走向飞鸿驿站。"

    jump s009_placeholder


# =========================
# S009 占位
# =========================

# =========================
# S009 占位入口：自动跳转到真正 S009
# =========================

label s009_placeholder:

    jump s009_feihong_inn_1


# =========================
# S009｜飞鸿驿站初见1
# =========================

label s009_feihong_inn_1:

    scene bg feihong_inn_exterior_day_busy

    call music_daily from _call_music_daily_7

    "你走向飞鸿驿站。"

    "越靠近驿站，越能听见马蹄声、车轮声、伙计招呼声和客商催促声。"

    "飞鸿驿站门口拴着几匹马，行李和货箱堆在一旁。"

    "几个商旅正在争论房价，两个江湖客抱着刀靠在柱边，像是在等人，又像是在等事。"

    "那个年轻女子正站在门前，一边接话，一边登记。"

    "她约莫二十出头，眼神明亮，动作利落，嘴快得像能同时接住三个人的话。"

    "一个客商急道：“姑娘，我昨日就托人订了房！”"

    "年轻女子：“托谁订的？”"

    keshang "一个姓刘的。"

    "年轻女子：“开庵镇姓刘的能从南门排到北巷。你说清楚是哪位刘。”"

    "另一个江湖客插话：“我只住一晚，有没有上房？”"

    "年轻女子：“上房有，上房的钱也有。你有哪个？”"

    "那江湖客一时语塞。"

    "年轻女子转头看见你，立刻扬起笑。"

    weisaner "客官，住店、寄信、找人、托货，还是单纯迷路？"

    if protagonist == "wangfang":
        wangfang "我……先打听一下。"
    else:
        zuowan "我先问问，不一定住。"

    "魏三儿上下看了你一眼，笑意不减。"

    weisaner "外乡人？"

    if protagonist == "wangfang":
        wangfang "这么明显？"
    else:
        zuowan "你们开庵镇的人都这么会看人？"

    weisaner "这两日进镇的人，十个里有八个都说自己只是打听一下。"

    weisaner "最后不是住店，就是问路，要么就是问雷云峰。"

    "她把手中的木牌翻了一下。"

    weisaner "所以，你是哪一种？"

    if protagonist == "wangfang":
        wangfang "我听说风雷观要开炉炼丹，所以来看看。"
    else:
        zuowan "我听说长息定年丹牵涉药材和气脉，所以来看看。"

    "魏三儿一点也不惊讶。"

    weisaner "果然是雷云峰。"

    weisaner "这几天，开口不是丹，就是山。再这么下去，我都能替说书人开场了。"

    if protagonist == "wangfang":
        wangfang "那你知道长息定年丹到底是什么吗？"
    else:
        zuowan "那你听到的说法里，哪一种最可信？"

    "魏三儿歪头想了想。"

    weisaner "我听过三个版本。"

    weisaner "第一，吃了能长生。"

    weisaner "第二，吃了能年轻三十岁。"

    weisaner "第三，吃了会立刻死，但死得很体面。"

    "她摊手。"

    weisaner "你要问我哪个是真的，我只能说，第三个听起来最便宜。"

    if protagonist == "wangfang":
        wangfang "这么大的事，驿站里没人知道真相？"
    else:
        zuowan "驿站人来人往，应该听过不少消息吧。"

    weisaner "消息是多。"

    weisaner "可消息这种东西，在门口听见是一种，进了大堂又是一种，喝了酒之后还能变第三种。"

    weisaner "真想问清楚，得找更会记事的人。"

    "她正要继续说，身后忽然有人喊。"

    keshang "姑娘！我的货箱谁搬错了？"

    "另一个声音跟着响起。"

    jianghuke "我的马呢？刚才还在那儿！"

    "魏三儿立刻转身。"

    weisaner "货箱写名，马不写名，你们都敢放门口，胆子可真大！"

    "她回头看你一眼。"

    weisaner "你若只是打听，就进去看看。桌前那位方驿丞，比我会记事。"

    weisaner "不过别挡路。挡路在驿站不算罪，但很容易挨骂。"

    "说完，她又被人群叫走。"

    "你见她太忙，便自行走进飞鸿驿站。"

    jump s010_feihong_inn_2


# =========================
# S010｜飞鸿驿站初见2
# =========================

label s010_feihong_inn_2:

    scene bg feihong_inn_interior_busy

    call music_daily from _call_music_daily_8

    "你走进飞鸿驿站前厅。"

    "驿站内部比门口更热闹。"

    "正中是接待前厅，靠墙挂着房牌、路牌和信牌。"

    "一侧有供客商暂坐的长桌，另一侧堆着行李箱笼。"

    "往后能看见通往客房和后院的走廊，后院方向隐隐传来马嘶声和水桶碰撞声。"

    "厨房那边冒着热气，一个中年妇人正隔着半扇门骂人。"

    fangdaniang "谁把空碗摞到菜盆旁边的？这是驿站，不是猪圈！"

    "有人小声回：“方大娘，我这就拿走。”"

    fangdaniang "拿走还要我教？你长手是为了吃饭，不是为了摆着好看！"

    "前厅另一边，一个身形高大的男子正在与客商交谈。"

    "那人声音不高，却让急得冒汗的客商慢慢安静下来。"

    lutiankuo "货走北路，明日午前不能发。风大，马慢，催也无用。"

    keshang "可我这批货急。"

    lutiankuo "急货更不能走错路。"

    "再往门外看，马厩方向有个年轻马夫正给马添草料。"

    zhouerdan "你们人抢房，马也抢槽。今日谁都不容易。"

    "前厅文书桌后，一名男子正在低头写字。"

    "他三十多岁，衣着干净，神情温和，却有一种不容易被打乱的安静。"

    "桌上摊着账册、房簿、信单和几枚木印。"

    "他抬头看了你一眼。"

    fangheming "客官有事？"

    if protagonist == "wangfang":
        wangfang "方驿丞？魏三儿姑娘说，若想打听事，可以来问你。"
    else:
        zuowan "方驿丞？门口那位姑娘说，你比她更会记事。"

    "方鹤鸣放下笔。"

    fangheming "魏三儿说话，十句里有七句能听，三句要过水。"

    fangheming "你想问什么？"

    if protagonist == "wangfang":
        wangfang "长息定年丹。"
    else:
        zuowan "风雷观的长息定年丹。"

    "方鹤鸣神色没有太大变化，只将桌上的一张信单压平。"

    fangheming "这几日问这件事的人太多。"

    fangheming "我能告诉你的不多。"

    fangheming "风雷观确实在开炉。雷云峰上确实比往日戒严。各地来人也确实比往年多。"

    if protagonist == "wangfang":
        wangfang "那丹药真的能长生吗？"
    else:
        zuowan "那丹药真有传言中那么玄？"

    fangheming "驿站记路，不记仙方。"

    fangheming "我只知道，凡是被人传得太满的东西，最后往往装不下真相。"

    "他看向前厅。"

    "有客商在催房，有江湖客在打听山路，有马夫跑来跑去。"

    fangheming "你若真想知道丹药的来龙去脉，可以去茯苓医馆问问。"

    fangheming "医馆与风雷观常有药材往来，周药师比我们更懂药理。"

    "他顿了顿，又补一句。"

    fangheming "不过，懂药理不代表能把所有话都告诉你。"

    if protagonist == "wangfang":
        wangfang "多谢方驿丞。"
    else:
        zuowan "明白。多谢。"

    "方鹤鸣点了点头，重新拿起笔。"

    "你转身准备离开前厅。"

    "临走前，你看见角落里有个少年抱着扫帚靠在柱边打瞌睡。"

    "他年纪不大，睡得很香，扫帚倒是抱得很紧。"

    "方大娘的声音忽然从厨房传来。"

    fangdaniang "罗阿枣！你再抱着扫帚睡，我就把你和扫帚一起立到门口招客！"

    "少年猛地惊醒。"

    luoazao "我没睡，我在听地声。"

    fangdaniang "你再听，地都嫌你烦。"

    "前厅里有人笑出声。"

    "你也笑了笑，离开飞鸿驿站"

    scene bg yongle_street_leiling_palace_day_guest

    "向南经过雷凌宫时，你看见白天那个冷淡的小厮小庆正满脸堆笑地与一名衣着华丽的年轻女子说话。"

    "小庆躬身开门，态度与刚才对路人完全不同。"

    "那女子衣料华贵，神情却并不张扬。"

    "她回头看了风云坪一眼，随后走进雷凌宫。"

    "你猜她大概是王家的贵客，或者王家小姐。"

    "再往南些，茯苓医馆的药香从门口飘来。"

    "你想起方鹤鸣的话，决定进去看看。"

    jump s011_fuling_clinic_1


# =========================
# S011｜茯苓医馆初见1
# =========================

label s011_fuling_clinic_1:

    scene bg fuling_clinic_interior_day_zhouqingliu

    call music_daily from _call_music_daily_9

    "你走进茯苓医馆。"

    "与飞鸿驿站的喧闹不同，医馆里安静许多。"

    "但这种安静不是空。"

    "前厅一侧是诊桌，另一侧是药柜。药柜高而密，抽屉上贴着细小标签。"

    "梁上悬着几束晒干的草药，角落里有小药炉正冒着淡淡白气。"

    "空气中有草药、炭火和旧木头混在一起的味道。"

    "有病人坐在长凳上等诊，有人捂着胳膊，有人低声咳嗽。"

    "你刚进门，便看见一名年轻药师正在药柜前整理药材。"

    "他身形清瘦，眼神灵动，手里捏着一片草叶，像是在和那片草叶争论。"

    zhouqingliu "你这叶脉长得不对。"

    "旁边一名病人愣住。"

    bingren "大夫，是我不对，还是叶子不对？"

    zhouqingliu "暂时是叶子。你等会儿再说。"

    "他转头看见你，目光在你身上一扫。"

    zhouqingliu "外乡人。"

    if protagonist == "wangfang":
        wangfang "又看出来了？"
    else:
        zuowan "你们开庵镇的人，似乎都很会认外乡人。"

    zhouqingliu "本地人进医馆，先看病人。"

    zhouqingliu "外乡人进医馆，先看药柜。"

    zhouqingliu "你刚才看了药柜三眼，看了诊桌一眼，看了我半眼。"

    if protagonist == "wangfang":
        wangfang "我只是想问问长息定年丹。"
    else:
        zuowan "我想问问长息定年丹的事。"

    "周青柳把手里的草叶放下。"

    zhouqingliu "果然。"

    zhouqingliu "这几日来医馆问丹的人，比来看风寒的人还多。"

    zhouqingliu "可惜丹药不能治好奇心。"

    if protagonist == "wangfang":
        wangfang "那它能治什么？"
    else:
        zuowan "它到底是药，还是江湖传言？"

    "周青柳看了你一会儿。"

    "他没有像魏三儿那样开玩笑，也没有像方鹤鸣那样避开话头。"

    zhouqingliu "长息定年丹，不是长生丹。"

    zhouqingliu "至少从药理上，不可能让一个人永远不老不死。"

    zhouqingliu "它更像是把一个人正在散掉的元息暂时收住，把衰败的气血稳在某个阶段。"

    zhouqingliu "若用来救人，或许能拖回一条命。"

    zhouqingliu "若用来贪生，恐怕会拖出别的祸。"

    if protagonist == "wangfang":
        wangfang "你知道得这么清楚，医馆参与炼丹了？"
    else:
        zuowan "茯苓医馆是不是给风雷观供过药材？"

    "周青柳没有立刻回答。"

    "他从药柜里抽出一个小屉，又慢慢推回去。"

    zhouqingliu "医馆与风雷观素有药材往来。"

    zhouqingliu "送药，不等于知方。"

    zhouqingliu "知方，也不等于知道掌炉人真正想炼什么。"

    "这句话让医馆里的药香忽然显得更深。"

    $ heard_dingnian_dan_rumor = True

    "你记住了：长息定年丹并非简单的长生丹。"

    "它牵涉元息、气血、衰败与定息。"

    "正在这时，门外传来一阵急促的脚步声。"

    scene bg fuling_clinic_interior_day_zhouqingliu_shenyun

    "一个年轻男子抱着半捆草药跑进来。"

    "年轻男子：“师父！后院那筐雷纹草是不是你让我晒的？”"

    "周青柳闭了闭眼。"

    zhouqingliu "我让你阴干。"

    "年轻男子：“我晒得很阴。”"

    zhouqingliu "它在太阳底下。"

    "年轻男子：“但我给它撑了半把伞。”"

    zhouqingliu "沈云。"

    "年轻男子：“在。”"

    zhouqingliu "你去把另外半把伞也撑上。"

    shenyun "哦。"

    "沈云这才注意到你。"

    shenyun "咦，外乡人？"

    zhouqingliu "今日第三个。"

    shenyun "问丹的？"

    zhouqingliu "今日第三个。"

    "沈云看向你，笑得很自然。"

    shenyun "那你问对人了，也问错人了。"

    if protagonist == "wangfang":
        wangfang "什么意思？"
    else:
        zuowan "怎么说？"

    shenyun "问我师父，他会说药理。"

    shenyun "问徐掌柜，她会说人心。"

    "周青柳看了他一眼。"

    zhouqingliu "你先去救那半筐草。"

    "沈云立刻抱着草药往后院跑。"

    "周青柳向你略一点头。"

    zhouqingliu "若还有疑问，日后再问。"

    zhouqingliu "今日医馆不算闲。"

    "你知道自己不好继续打扰，便退到一旁，准备在医馆里简单看看。"

    jump s012_fuling_clinic_2


# =========================
# S012｜茯苓医馆初见2
# =========================

label s012_fuling_clinic_2:

    scene bg fuling_clinic_interior_day_busy_v2

    call music_daily from _call_music_daily_10

    "你在医馆前厅慢慢走了一圈。"

    "这里不像飞鸿驿站那样每个人都在大声说话。"

    "可只要细看，就会发现每个人都在忙。"

    "诊室帘后，一个女人的声音传出来，冷而利。"

    chensumei "我说过七日忌酒。"

    bingren "陈大夫，我就喝了一小口。"

    chensumei "你的脉象不像一小口。"

    bingren "那是因为杯子大。"

    chensumei "你再顶嘴，我就按十日治。"

    "帘外几个病人立刻坐直了些。"

    "药柜旁，一个年轻学徒正抱着书，一边看一边走。"

    "他看得太认真，差点撞到药柜。"

    shenxingchen "对不起。"

    "药柜当然没有回答。"

    "他却认真地向药柜点了点头，又继续看书。"

    "窗边有一名女子正在饮茶。"

    "她衣着利落，神情沉稳，杯子还没放下，目光已经扫过前厅每一个角落。"

    "有病人家属想挤到前面，她只抬了一下眼。"

    chengmingzhu "排队。"

    "那人立刻退了回去。"

    "后门阴影里，站着一个沉默的男人。"

    "他手中握着刀，衣着朴素，几乎不出声。"

    "可你一眼便觉得，他不像普通护院。"

    "他似乎注意到你在看他。"

    "李默抬眼。"

    "你立刻移开目光。"

    "片刻后，沈云从后院回来，手里已经没有那半筐草药。"

    shenyun "救回来了。"

    zhouqingliu "草救回来了？"

    shenyun "伞救回来了。草还要看命。"

    zhouqingliu "你离药材远一点，就是它们最大的命。"

    "沈云笑了一下，似乎一点也不介意。"

    "他看见你还在医馆，便凑近一些。"

    shenyun "你还没走啊？"

    if protagonist == "wangfang":
        wangfang "我只是看看。医馆和驿站很不一样。"
    else:
        zuowan "这里比我想的更忙。"

    shenyun "那当然。"

    shenyun "驿站是人没地方去，医馆是人没办法了才来。"

    "他这话说得轻，却不轻浮。"

    "你正想再问些什么，诊室帘后忽然传来陈素梅的声音。"

    chensumei "沈云。"

    "沈云立刻站直。"

    shenyun "在！"

    chensumei "去后院拿干净布巾。不要拿晒药那块。"

    shenyun "知道！"

    "他冲你摆摆手。"

    shenyun "你若还在镇上，回头再聊。"

    "说完，他又跑向后院。"

    "你向周青柳道谢，准备离开医馆。"

    "临走前，你再次看见李默站在后门阴影里。"

    "他没有拦你，也没有说话。"

    "但你莫名觉得，只要有人想从后门闯进医馆，第一步就会被他看见。"

    "你走出茯苓医馆，回到风云坪。"

    scene bg fengyunping_evening_lodging_realization

    "夕阳渐低，风云坪上的人影被拉得很长。"

    "你在镇中闲逛了一阵，看见形形色色的镇民、江湖人士和商铺招牌。"

    "等到天色慢慢暗下来，你忽然意识到一个很现实的问题。"

    "今晚，你还没有住处。"

    "飞鸿驿站人来人往，或许还能问问魏三儿有没有空房。"

    "你转身，向飞鸿驿站走去。"

    jump s013_guo_luping_invite



# =========================
# S013｜落脚选择郭路平邀约
# =========================

label s013_guo_luping_invite:

    call music_daily from _call_music_daily_11

    "夕色渐深，风云坪上的人声却没有立刻散去。"

    "长风楼方向已经点起灯，飞鸿驿站门口仍有人牵马、搬箱、问房。"

    "你走回飞鸿驿站门前。"

    scene bg feihong_inn_exterior_evening_full_sign with dissolve

    "魏三儿正把一块写着“满”的木牌挂到门边。"

    "她一转头，看见你又回来了。"

    weisaner "哟，又是你。"

    if protagonist == "wangfang":
        wangfang "我想问问，还有没有空房？"
    else:
        zuowan "我想问问，今晚还有房吗？"

    "魏三儿看了看那块木牌，又看了看你。"

    weisaner "你问得很有勇气。"

    weisaner "但勇气不能变出房。"

    if protagonist == "wangfang":
        wangfang "一点位置都没有？柴房也行。"
    else:
        zuowan "临时歇脚的地方也没有？"

    "魏三儿摊手。"

    weisaner "前头客房满了，通铺满了，连马夫铺都快住人了。"

    "她顿了顿，目光落在你身上。"

    weisaner "你身上还有多少钱？"

    if protagonist == "wangfang":
        wangfang "不多。"
    else:
        zuowan "够吃几顿，不够长期住店。"

    "魏三儿笑了一下。"

    weisaner "那你倒是诚实。"

    if protagonist == "wangfang":
        wangfang "驿站招帮工吗？我可以跑腿，搬东西，送信也行。"
    else:
        zuowan "如果驿站缺人，我可以帮忙。跑腿、传话、照看行李，都可以。"

    "魏三儿没有立刻回答。"

    "她朝前厅里看了一眼。"

    weisaner "这我可说了不算。"

    weisaner "你等一下。"

    "她转身进了驿站。"

    "你站在门外，听见里面仍旧忙乱。"

    "有人催饭，有人问马，有人和方大娘争论一碗汤到底算不算免费。"

    if protagonist == "wangfang":
        scene bg feihong_inn_exterior_evening_invite_wangfang with dissolve
    else:
        scene bg feihong_inn_exterior_evening_invite_zuowan with dissolve


    "没过多久，魏三儿从里面出来。"

    "她身后跟着一名中年男子。"

    "那人四十多岁，衣着不华贵，却很整洁。眉眼温和，神情沉稳，像是站在那里便能让驿站稍微安静一点。"

    weisaner "郭总管，就是这位。"

    "郭路平看向你。"

    "那一瞬间，你忽然觉得他不是在看一个临时求住处的外乡人。"

    "他像是在确认什么。"

    "像是你来得有些突然，又像是你来得并不意外。"

    guoluping "你是为雷云峰来的？"

    if protagonist == "wangfang":
        wangfang "是。听说风雷观开炉炼丹，各路江湖人都来了。"
    else:
        zuowan "是。长息定年丹牵涉药理与气脉，我想亲眼看看。"

    "郭路平轻轻点头。"

    guoluping "最近为雷云峰而来的人很多。"

    guoluping "但愿意先问有没有活干的人，不多。"

    "魏三儿在旁边补了一句。"

    weisaner "大多一开口就问上房，下一句问能不能赊账。"

    "郭路平看了她一眼，魏三儿立刻闭嘴，眼睛却还在笑。"

    "郭路平重新看向你。"

    guoluping "前头客房满了。后头夹廊小院还有间北耳房，原是给信差歇脚的。"

    guoluping "你若不嫌窄，可以先住那儿。"

    guoluping "白日帮魏三儿跑腿，夜里别乱摸医馆的门。"

    if protagonist == "wangfang":
        wangfang "北耳房？在驿站后头？"
    else:
        zuowan "夹廊小院？就是驿站和医馆之间的那处地方？"

    guoluping "北接飞鸿驿站，南通茯苓医馆。"

    guoluping "那地方不是正经客房，也不对外放客。"

    guoluping "住在那里，不算享福。哪边有事，哪边都可能喊你。"

    weisaner "简单说，就是睡得近，跑得快。"

    guoluping "也可以这么说。"

    "你心里一动。"

    "能有一个住处当然很好。"

    "但你今日刚入镇，只在驿站与医馆各走了一圈。"

    "飞鸿驿站热闹、机灵、消息多，可茯苓医馆似乎也与长息定年丹更近。"

    "何况你还没问过医馆那边。"

    if protagonist == "wangfang":
        wangfang "多谢郭总管。我能不能……再想想？"
    else:
        zuowan "多谢郭总管。我想再考虑一下。"

    "郭路平并不意外。"

    guoluping "可以。"

    guoluping "今日天黑前给我答复。开庵镇夜里有宵禁，外乡人最好不要在街上乱走。"

    "魏三儿朝你摆了摆手。"

    weisaner "想好了就回来。北耳房虽然窄，但至少不漏雨。"

    "她停了停。"

    weisaner "大概。"

    "你离开飞鸿驿站门口。"

    scene bg fuling_clinic_exterior_evening_shenyun_call with dissolve

    "刚走到风云坪边，便听见身后有人喊你。"

    "回头一看，是白日在茯苓医馆见过的沈云。"

    "沈云站在医馆门口，朝你招手。"

    shenyun "你还没找到住处吧？"

    jump s014_xu_chunxiang_invite


# =========================
# S014｜落脚选择徐春香邀约
# =========================

label s014_xu_chunxiang_invite:

   
    call music_daily from _call_music_daily_12

    "你走向茯苓医馆。"

    "此时医馆前厅比白日安静一些，但药炉仍在小火上煨着。"

    "沈云把你引到门边，压低声音。"

    shenyun "我刚才听魏三儿说你在找住处。"

    if protagonist == "wangfang":
        wangfang "她嘴这么快？"
    else:
        zuowan "她消息传得倒快。"

    shenyun "驿站和医馆隔得近，魏三儿声音又不小。"

    "他笑了笑。"

    shenyun "你先别急着谢我，我只是替徐掌柜叫你。"

    "话音刚落，诊桌旁的帘子被轻轻掀开。"

    if protagonist == "wangfang":
        scene bg fuling_clinic_exterior_evening_invite_wangfang
    else:
        scene bg fuling_clinic_exterior_evening_invite_zuowan

    "一名中年女子走了出来。"

    "她约莫四十多岁，神情温和，却不是软弱的温和。"

    "她看人时很稳，像是先看见你的疲惫，再看见你的来意。"

    shenyun "徐掌柜，这就是白日来问定年丹的那位。"

    "徐春香看向你。"

    xuchunxiang "周药师跟我提过你。"

    if protagonist == "wangfang":
        wangfang "徐掌柜。"
    else:
        zuowan "徐掌柜。"

    xuchunxiang "你是外地来开庵镇看雷云峰热闹的？"

    if protagonist == "wangfang":
        wangfang "一开始是想看看江湖热闹。"
        wangfang "但今日走了一圈，觉得这件事可能没那么简单。"
    else:
        zuowan "我想看清长息定年丹到底牵涉什么。"
        zuowan "今日听周药师说过之后，更觉得此事不只是传言。"

    "徐春香点了点头。"

    xuchunxiang "知道事情不简单，还愿意承认自己初来乍到，这不坏。"

    "沈云在旁边小声说："

    shenyun "徐掌柜这句话，是夸人。"

    "徐春香看了他一眼。"

    "沈云立刻站直。"

    "徐春香重新看向你。"

    xuchunxiang "医馆不留闲人。"

    xuchunxiang "但今夜伤者多，药炉不能停，后院也缺人搭手。"

    xuchunxiang "夹廊小院南边有间南耳房，原是给采药人歇脚的。"

    xuchunxiang "你若愿意帮忙煎药、搬药、传话，就先住下。"

    if protagonist == "wangfang":
        wangfang "我不懂医术。"
    else:
        zuowan "我懂一些草药，但未必懂医馆规矩。"

    xuchunxiang "不懂医术，可以学着别添乱。"

    xuchunxiang "懂草药，也要先学规矩。"

    "她语气不重，却让人知道这不是客套。"

    xuchunxiang "医馆救人，不靠一腔热血，也不靠几句聪明话。"

    xuchunxiang "真想留下，先从把药端稳开始。"

    "沈云在旁边接话。"

    shenyun "南耳房比北耳房安静一点。"

    "他想了想，又补一句。"

    shenyun "不过半夜有人敲门叫药的时候，也安静不到哪儿去。"

    "你看向医馆后方。"

    "那里有淡淡药香，有人低声咳嗽，也有人在帘后收拾针具。"

    "与飞鸿驿站相比，茯苓医馆少了些热闹，却多了一种让人不敢轻浮的安定。"

    "徐春香没有催你。"

    xuchunxiang "驿站那边，郭路平应该也给了你话。"

    "你一怔。"

    xuchunxiang "飞鸿驿站与茯苓医馆门挨着门。开庵镇这么小，话传得比药香还快。"

    "她淡淡一笑。"

    xuchunxiang "你不用急着答应我，也不用急着答应他。"

    xuchunxiang "天黑前想清楚就好。"

    if protagonist == "wangfang":
        wangfang "多谢徐掌柜。我会认真想。"
    else:
        zuowan "多谢徐掌柜。我会想清楚。"

    "徐春香点头。"

    scene bg fuling_clinic_exterior_evening_shenyun_call

    "沈云送你到门口。"

    shenyun "你若选医馆，我以后带你认药。"

    shenyun "不过有些药我也认不全，到时我们一起挨骂。"

    "你忍不住笑了一下。"

    "走出茯苓医馆时，天色已经更暗。"

    scene bg yongle_street_evening_lodging_choice

    "飞鸿驿站的灯亮了，茯苓医馆的药炉也亮着。"

    "两处灯火一北一南，都照向夹廊小院。"

    "你站在永乐大街边，忽然觉得自己不能再拖。"

    "今晚必须有一个落脚处。"

    jump s015_choose_base_place


# =========================
# S015｜最终落脚选择
# =========================

label s015_choose_base_place:

    call music_daily from _call_music_daily_13

    "暮色中的永乐大街，比白日安静了一些。"

    "风云坪上仍有人来往，但远处已经传来巡捕催人收摊的声音。"

    "你站在街边，心里反复想着今日见过的人。"

    "飞鸿驿站。"

    "魏三儿嘴快机灵，郭路平稳重识人。"

    "驿站人来人往，消息最多，也最像江湖入口。"

    "若留在那里，白日跑腿、传信、接待客人，或许能最快认识开庵镇的江湖人。"

    "茯苓医馆。"

    "周青柳懂药理，沈云活泼亲切，徐春香温和却有原则。"

    "医馆与风雷观有药材往来，或许更接近长息定年丹真正的秘密。"

    "若留在那里，煎药、搬药、看诊、救人，每一步都不能马虎。"

    "你忽然意识到，这不只是今晚睡在哪里。"

    "这是你来到开庵镇后的第一个选择。"

    menu:

        "接受郭路平的邀请，暂住飞鸿驿站北耳房":

            $ base_place = "feihong_inn"

            scene bg feihong_inn_exterior_evening_choose_inn

            call music_daily from _call_music_daily_14

            "你最终转身，走向飞鸿驿站。"

            "魏三儿正在门口收拾木牌，看见你回来，像是早猜到了，却故意挑眉。"

            weisaner "想好了？"

            if protagonist == "wangfang":
                wangfang "想好了。我想先留在驿站。"
            else:
                zuowan "想好了。我先留在飞鸿驿站。"

            "魏三儿点头。"

            weisaner "那就跟我来。"

            "你跟着她进了驿站，穿过前厅，绕到后方。"

            "柜台后，郭路平抬头看了你一眼。"

            "他没有多问，只说了一句："

            guoluping "先住下。驿站看人，不看他说过什么，看他明日怎么做。"

            "魏三儿立刻接话。"

            weisaner "听见没？明早别睡过头，不然我也救不了你。"

            scene bg jialang_courtyard_evening_lodging with dissolve

            "她带你来到夹廊小院。"

            "小院不大，北接飞鸿驿站，南通茯苓医馆，东侧有一扇面向风云坪的屏风门，西侧则是雷凌宫的高墙。"

            "院中摆着一张旧木大桌，桌边有几只不成套的凳子。"

            "魏三儿指了指北边一间小耳房。"

            weisaner "北耳房，今晚归你。"

            weisaner "铺盖旧了点，窗子紧了点，夜里若听见马叫、人喊、方大娘骂人，都正常。"

            if protagonist == "wangfang":
                wangfang "供饭吗？"
            else:
                zuowan "吃饭怎么算？"

            "魏三儿笑了。"

            weisaner "郭总管吩咐过，试住三日，饭照给。"

            weisaner "但不是白吃。明日开始，哪边喊你，你就搭把手。"

            "她指了指南侧医馆门。"

            weisaner "还有一条规矩。住在夹廊小院的人，别把驿站和医馆分得太清。"

            weisaner "哪边急，先帮哪边。"

            "你点了点头。"

            "夜色落下，你终于有了在开庵镇的第一张床。"

        "接受徐春香的邀请，暂住茯苓医馆南耳房":

            $ base_place = "fuling_clinic"

            scene bg fuling_clinic_exterior_evening_choose_clinic

            call music_daily from _call_music_daily_15

            "你最终转身，走向茯苓医馆。"

            "沈云正在门口收草药，看见你回来，先是一愣，随即笑了。"

            shenyun "想好了？"

            if protagonist == "wangfang":
                wangfang "想好了。我想先留在医馆。"
            else:
                zuowan "想好了。我先留在茯苓医馆。"

            "沈云把手里的草药往筐里一放。"

            shenyun "那就跟我来。"

            "你跟着他进了医馆。"

            "诊桌旁，徐春香正在收拾药方。"

            "她抬眼看见你，没有多问，只温声说了一句："

            xuchunxiang "今晚先住下。人初到异乡，最怕夜里硬撑。明日能不能留下，看你愿不愿意好好做事。"

            "沈云压低声音。"

            shenyun "徐掌柜这么说，就是准了。"

            scene bg jialang_courtyard_evening_lodging with dissolve

            "他带你从医馆侧门走入夹廊小院。"

            "小院不大，北接飞鸿驿站，南通茯苓医馆，东侧有一扇面向风云坪的屏风门，西侧则是雷凌宫的高墙。"

            "院中摆着一张旧木大桌，桌边有几只不成套的凳子。"

            "沈云指了指南边一间小耳房。"

            shenyun "南耳房，今晚归你。"

            shenyun "这里离药炉近，夜里有药香，也可能有病人喊疼。"

            "他想了想，又认真补充。"

            shenyun "若你怕苦味，可以慢慢习惯。反正我习惯了三年，也没完全习惯。"

            if protagonist == "wangfang":
                wangfang "供饭吗？"
            else:
                zuowan "吃饭怎么算？"

            "沈云笑了。"

            shenyun "徐掌柜吩咐过，试住三日，饭照给。"

            shenyun "不过不是白吃。明日开始，煎药、搬药、传话，哪样都可能轮到你。"

            "他又指了指北侧驿站后门。"

            shenyun "还有个麻烦处。驿站那边一忙，喊声也能传过来。"

            shenyun "徐掌柜说了，夹廊小院的人，哪边急就先帮哪边。"

            "你点了点头。"

            "夜色落下，你终于有了在开庵镇的第一张床。"

    "这一夜，你睡在夹廊小院。"

    "北边是驿站的锅铲声、脚步声、马嘶声。"

    "南边是医馆的药香、低语和药炉小火。"

    "你忽然觉得，自己像是睡在这座小镇的两条脉络之间。"

    "而这座小镇，也从今晚开始，轻轻把你拴住了。"

    jump s016_inn_overflow


# =========================
# S016｜驿站住满了
# =========================

label s016_inn_overflow:

    scene bg jialang_courtyard_morning with dissolve

    call music_daily from _call_music_daily_16

    "这一夜，你睡得比想象中沉。"

    "清晨醒来时，先听见规律的切菜声，又闻到药炉里淡淡的草药味。"

    "夹廊小院果然夹在飞鸿驿站和茯苓医馆之间。"

    "北边是锅铲、脚步、马嘶。"

    "南边是药香、竹筛、水声。"

    if base_place == "feihong_inn":
        "你从北耳房推门出来。"
    else:
        "你从南耳房推门出来。"

    "院中那张旧木大桌还在，桌边几只凳子摆得歪歪斜斜。"

    "你绕过屏风门，正对着风云坪伸了个懒腰。"

    "风云坪上已经有人来往，卖早点的摊子冒着热气，远处马车轮声滚过石面。"

    "还没等你真正清醒，飞鸿驿站方向忽然传来一阵吵嚷。"

    scene bg jialang_courtyard_morning_weisaner with dissolve

    "夹廊小院北门被人推开，魏三儿探出半个身子，头发都没来得及理顺。"

    weisaner "醒了没有？醒了就来搭把手！驿站快被人住塌了！"

    "话音未落，沈云也从医馆侧门探出来，手里还拿着半捆草药。"

    shenyun "你们驿站一大早又怎么了？"

    weisaner "什么叫又？这是江湖大势！"

    "沈云看了你一眼。"

    shenyun "去吧。徐掌柜说了，夹廊小院的人，哪边急就先帮哪边。"

    if protagonist == "wangfang":
        wangfang "好，我去看看能帮上什么忙。"
    else:
        zuowan "好，我去看看。"

    "魏三儿一把招手。"

    weisaner "能喘气就能帮忙，快来！"

    scene bg feihong_inn_interior_day_overflow with dissolve

    "你跟着魏三儿来到飞鸿驿站前厅。"

    "前厅比昨日更乱。"

    "门口挤着抱包袱的商旅、背刀的江湖客、牵马的马夫，还有几个自称某某门派弟子的年轻人。"

    "有人嚷着自己早订了房，有人说昨夜赶路冻了一宿，有人拍着柜台要求立刻安排。"

    "周二蛋站在门边，笑得脸都快僵了，还在跟住客解释。"

    zhouerdan "马有马厩，人有客房，可现在的问题是，马比人听话，客房比马少。"

    "方大娘从厨房端着一摞碗出来，边走边骂。"

    fangdaniang "喊什么喊？喊能喊出一张床来？先把粥喝了，饿着肚子吵架最没出息！"

    "方鹤鸣坐在文书桌前，时而奋笔疾书，时而抬头看墙上的房牌木板。"

    "木板上挂着一排小牌：上房、普通房、通铺、马夫铺、后院临歇。"

    "几乎都已经翻成了“满”。"

    "郭路平正在门口拱手向众人解释，语气仍然稳。"

    guoluping "诸位稍安。飞鸿驿站能住多少人，账上有数，梁上也有数。再往里塞，今晚不是睡觉，是叠罗汉。"

    "魏三儿把你往方鹤鸣面前一推。"

    weisaner "帮手我招来了！"

    "方鹤鸣抬头看了你一眼，语气不急不慢。"

    fangheming "醒了？醒了就干活。饭给你留了，先别吃完，边吃边记。"

    if protagonist == "wangfang":
        wangfang "记什么？"
    else:
        zuowan "记什么？"

    scene bg feihong_inn_interior_day_group_distribution with dissolve

    "方鹤鸣把一摞小木牌推到你面前。"

    fangheming "三类人。"

    fangheming "第一类，有老有小、有伤病的，优先安排通铺。"

    fangheming "第二类，有急信急货在身的，留下等总管调度。"

    fangheming "第三类，纯来看热闹又嗓门大的，请去长风楼、青云楼，或者让他们自己去风云坪看天。"

    "魏三儿在旁边补一句。"

    weisaner "你就站这儿发牌。谁骂你，你就说方驿丞定的。谁还骂你，你就说郭总管定的。"

    "方鹤鸣淡淡道。"

    fangheming "谁若还骂，就说方大娘在厨房。"

    "魏三儿立刻点头。"

    weisaner "这个最管用。"

    "你接过木牌，开始帮忙分人。"

    "一名年轻江湖客不满，说自己是承天剑派外门弟子，理应优先入住。"

    "魏三儿刚要开口，罗阿枣忽然从柱子后面钻出来，抱着扫帚说："

    luoazao "他骗人。"

    "众人一愣。"

    "郭路平看向他。"

    guoluping "阿枣，说清楚。"

    "罗阿枣挠了挠头。"

    luoazao "我刚才扫地，看见他鞋底是西街菜市的泥，袖口还有梁氏关扑铺的骰子粉。"

    luoazao "他说昨夜从雷云峰下来，可雷云峰山脚那边昨夜下过细雨，鞋上不该这么干。"

    "魏三儿眼睛一亮。"

    weisaner "好啊，阿枣，你偷懒偷出本事来了。"

    "罗阿枣不服。"

    luoazao "我那叫低处观察。"

    "方鹤鸣看向那名年轻江湖客。"

    fangheming "承天剑派弟子入驿，需出示派牒。若没有，就按普通看客排。"

    "那人脸色尴尬，悻悻退到一边。"

    "这个小插曲让你第一次意识到：驿站不是谁嗓门大谁有理，这里有自己的规矩，也有自己识人的办法。"

    scene bg feihong_inn_interior_day_lutiankuo_report with dissolve

    "就在前厅稍微安静一点时，鲁天阔从外面快步回来。"

    "他身上带着尘土，手里握着一只皮质信袋，额角有汗。"

    "他先把信袋放进柜中，转身就去找水喝。"

    lutiankuo "官道上还有两队人往开庵镇来。"

    lutiankuo "一队自称给风雷观送药材，一队说是来求丹的富户家眷。最迟午后到。"

    "魏三儿差点叫出来。"

    weisaner "还来？他们是长在路上了吗？"

    "周二蛋在门外探头。"

    zhouerdan "马厩也满了。再来马，只能让它们自己商量谁睡外头。"

    "方大娘把一碗粥拍到你面前。"

    fangdaniang "新来的，喝。别学他们光用嘴干活。"

    "你端起粥，有些不好意思。"

    "自己明明昨夜才被收留，今日就站在驿站前厅发牌、分人、听人吵闹，好像已经被卷进了这座镇子的运转里。"

    if protagonist == "wangfang":
        wangfang "若是实在住不下，我那间耳房……"
    else:
        zuowan "若是实在住不下，我住的那间耳房……"

    "话还没说完，郭路平便打断了。"

    guoluping "你安心住着。夹廊小院的耳房不对外放客。"

    "你一怔。"

    "郭路平看了你一眼，语气依旧平稳。"

    guoluping "那地方北接驿站，南通医馆，夜里有事要有人听得见。"

    guoluping "安排你住，不是给你占便宜，是看你能不能派上用场。"

    "方鹤鸣补充。"

    fangheming "换句话说，你不是客房客人，是试住帮工。"

    "魏三儿笑道。"

    weisaner "听起来是不是没那么感动了？"

    "你却反而松了一口气。"

    "郭路平最终出面定下安排。"

    guoluping "今日起，飞鸿驿站不再收普通看热闹住客。"

    guoluping "已有伤病、急信、押货者优先。其余人，我已托辛掌柜在长风楼、青云楼、凰龙客栈各留了些位置。"

    "有人立刻问。"

    jianghuke "那价钱呢？"

    "郭路平微微一笑。"

    guoluping "非常时期，住宿费自然不会像平日一样。嫌贵的，风云坪很宽。"

    "众人一时哑然。"

    "方大娘从旁边补刀。"

    fangdaniang "风云坪不要钱，就是夜里风大。"

    "魏三儿低声对你说："

    weisaner "郭总管这叫把人往外送，还让人觉得自己占了便宜。"

    "方鹤鸣纠正。"

    fangheming "这叫分流。"

    zhouerdan "我觉得叫活命。"

    "鲁天阔喝完水，已经准备再出去一趟。"

    "他看向郭路平。"

    lutiankuo "我去长风楼确认房数。"

    "郭路平点头。"

    guoluping "带上两张备用路引。若遇到闹事的，先讲理；讲不通，回来叫人。"

    "鲁天阔只回了一个字。"

    lutiankuo "嗯。"

    "到上午将尽，飞鸿驿站的乱局终于被压下去。"

    "有人被安排去长风楼，有人留在通铺等候，有人被请去青云楼，有人虽不满，却也不敢再闹。"

    "你在驿站前厅忙了大半个上午：发牌、传话、帮方鹤鸣核名单、替魏三儿把客人引到后院，又被方大娘塞了两次吃食。"

    "说不上亲近，却没有人把你当成纯粹的外人。"

    "魏三儿把最后一块木牌挂回墙上，长出一口气。"

    weisaner "行了，驿站暂时没塌。"

    "方大娘从厨房探头。"

    fangdaniang "没塌也别闲着。谁去把药炉那边的空碗送回医馆？"

    "沈云刚好从夹廊小院那头探出头来。"

    scene bg feihong_inn_interior_day_medical_alarm with dissolve

    shenyun "别送碗了，医馆这边好像要忙了。"

    "你还没反应过来，远处风云坪上传来一阵急促脚步声。"

    "一个人被抬着，从雷云峰方向送进了茯苓医馆。"

    $ helped_feihong_inn = True

    jump s017_clinic_injured


# =========================
# S017｜医馆伤者
# =========================

label s017_clinic_injured:

    call music_tension from _call_music_tension

    "沈云脸色比刚才白了许多。"

    shenyun "医馆这边出事了！有人从雷云峰方向被抬下来了！"

    "魏三儿本来还在抱怨驿站客牌不够，听见这话，立刻收了笑。"

    weisaner "人还活着吗？"

    shenyun "活着，但说胡话。"

    "方大娘从厨房门口探出头，手里还拿着汤勺。"

    fangdaniang "活着就别站这儿废话，赶紧去！"

    "你跟着沈云穿过夹廊小院，进了茯苓医馆。"

    scene bg fuling_clinic_interior_day_emergency_patient with dissolve

    "医馆前厅已经变了样。"

    "候诊的病人被程明珠安排到一侧，药柜前的竹筛被挪开，地上铺了一张临时担架。"

    "担架上躺着一个中年男人。"

    "那人眼球微突，脸色青紫，额角和颈侧浮起青色血脉，像是有什么东西在皮下细细游走。"

    "他嘴唇发干，喉咙里断断续续重复着一句话："

    shangzhe "所闻非所见……所见非人间……奇哉……怪也……"

    "你被眼前景象吓了一下，下意识停住脚步，不敢靠得太近。"

    "陈素梅背对着你，跪坐在伤者身前施针。"

    "她动作极稳，但肩背绷得很紧。即使看不见表情，也能感觉到她少见的疑惑和压力。"

    "李默站在离病人不远的阴影处，手中握着刀，神情没有变化，只是目光始终停在伤者身上。"

    "陈素梅最后落下一针，缓缓吐出一口气。"

    "她起身时用袖口擦了擦额角的汗。"

    "她声音很平。"

    chensumei "我暂时用针稳住了他的气脉。不是治好，只是让它别继续乱冲。"

    "周青柳立刻问。"

    zhouqingliu "毒？"

    "陈素梅看了他一眼。"

    chensumei "不像。"

    zhouqingliu "走火入魔？"

    chensumei "也不像。"

    "她停了一下，像是在极不情愿地承认一个不合逻辑的结论。"

    chensumei "更像是有人把一段不属于他的气，硬塞进了他身体里。"

    "你听得背后一凉。"

    "周青柳已经走到药柜前，一边开抽屉，一边快速报药名。"

    zhouqingliu "沈云，取青竹管。星辰呢？让他找雷纹草旧样。"

    zhouqingliu "再拿三钱茯神，两钱远志，一分朱砂不要入药，先备着看反应。"

    "沈云立刻跑去帮忙。"

    "程明珠站在前厅柜台后，目光一直盯着担架方向。"

    "她很快下令。"

    chengmingzhu "前厅让开一半。普通问诊后移半个时辰。"

    chengmingzhu "魏三儿，回驿站说一声，若还有人抬来，从夹廊小院进，别堵风云坪。"

    chengmingzhu "方大娘，热水留下，人先别围。"

    "方大娘把手里的汤勺往腰间一别。"

    fangdaniang "行，我不看热闹。我烧水去。谁要是堵门，我顺手也给他烫醒。"

    "魏三儿点头，但没有立刻走，眼睛还盯着伤者。"

    weisaner "他这脸色……不像普通病。"

    scene bg fuling_clinic_interior_day_inquiry_brothers with dissolve

    "这时，送伤者来的两个年轻男子站在一旁，神色焦急。"

    "高一点的男子向徐春香拱手，声音发颤。"

    gaoge_nanzi "大夫，这是我哥。您一定要救他。"

    "徐春香没有急着答应，而是蹲下看了伤者三息，又把手搭在脉上两瞬。"

    "她眉头微微一动，但语气仍然稳。"

    xuchunxiang "他这个样子多久了？为什么会变成这样？"

    "高个男子急忙说："

    gaoge_nanzi "我们从平原镇来，前日刚到开庵镇。"

    gaoge_nanzi "我哥一路上都好好的，前天夜里还睡得安稳。"

    gaoge_nanzi "哪成想昨日到了雷云峰山脚，他便开始说胡话。"

    "矮个男子忍不住插话。"

    aige_nanzi "都怪那个死道姑！要不是她——"

    "徐春香抬眼看他，声音不高，却让他立刻收住。"

    xuchunxiang "人在医馆，说话先留三分。"

    xuchunxiang "你既一路从碧溪府赶来凰龙府，若要救他，便把话说清楚。"

    xuchunxiang "若只想骂人，门在那边。"

    "高个男子连忙按住矮个男子的手。"

    gaoge_nanzi "三弟，别乱说。"

    "矮个男子咬牙。"

    aige_nanzi "她用拂尘往大哥头上一挥，大哥就成这样了！"

    "徐春香若有所思。"

    xuchunxiang "你们说的道姑，可知她道号？穿的是什么道袍？是否自称风雷观弟子？"

    "高个男子摇头。"

    gaoge_nanzi "我们不知道。她没说。"

    "矮个男子还想争辩。"

    aige_nanzi "她就是从山脚来的！不是风雷观的人，还能是谁？"

    "周青柳这时从药柜旁转过身，语气带着一点锋利。"

    zhouqingliu "我前几日刚从雷云峰送药回来。"

    zhouqingliu "风雷观近日闭观炼丹，弟子不得随意下山。"

    zhouqingliu "山上日常饮食、薪柴、药材，都是差人送上去的。"

    zhouqingliu "你们若真遇见了‘道姑’，她未必是风雷观的人。"

    "两个年轻男子脸色一变。"

    "李默在旁边淡淡开口，声音不大。"

    limo "他们隐瞒了路。"

    "众人安静了一瞬。"

    "高个男子额角冒汗。"

    gaoge_nanzi "我们……我们只是想从近路上山。"

    gaoge_nanzi "听人说，正路这几日不通，山脚旁还有一条旧采药路。"

    "徐春香没有立刻责备，只说："

    xuchunxiang "救人要紧。话可以稍后再问，但最好别再藏。"

    xuchunxiang "你们藏一句，他就多险一分。"

    "她起身，对周青柳说："

    xuchunxiang "先按定息方稳住，不要猛攻毒。若是外气冲脉，药下重了反会激它。"

    "周青柳点头。"

    zhouqingliu "我试轻方。"

    "陈素梅坐到一旁桌前，仍盯着伤者。"

    chensumei "我给你们半炷香。半炷香后若脉还乱，我要重下针。"

    chensumei "到时他疼，不要叫我轻些。"

    "矮个男子脸色更白。"

    "徐春香听完那两名年轻男子的话，神色并没有太大变化。"

    "她只问了一句："

    xuchunxiang "她的拂尘柄上，可有雷纹？"

    "高个男子迟疑。"

    "矮个男子咬牙道："

    aige_nanzi "有又如何？她把我大哥害成这样！"

    "徐春香看了他一眼。"

    xuchunxiang "若真是她，你大哥此刻还能躺在这里说胡话，已是她留了命。"

    "两人脸色同时变了。"

    "周青柳皱眉。"

    zhouqingliu "掌柜的，你是说……"

    "徐春香没有接话，只转身看向陈素梅。"

    "陈素梅坐在一旁，指尖还沾着针后的汗意，语气冷静。"

    chensumei "外息入体，强行冲脉。有人以极强内力替他压了一次，否则他撑不到医馆。"

    "徐春香点头。"

    xuchunxiang "不是伤在拂尘，是伤在贪近丹炉。"

    "高个男子嘴唇发白。"

    gaoge_nanzi "我们……我们只是想看一眼。"

    "李默在门边淡淡道："

    limo "看一眼，用得着走小路？"

    "没人再说话。"

    "徐春香没有发怒。"

    "她只是蹲下身，再次按住伤者的脉。"

    "伤者仍在喃喃。"

    shangzhe "所闻非所见……所见非人间……奇哉……怪也……"

    scene bg fuling_clinic_interior_day_chunhua_plan with dissolve

    "徐春香抬头。"

    xuchunxiang "星辰，跟我上药书房。取春华息脉匣。"

    "沈星辰怔了一下。"

    shenxingchen "要用《春华回春诀》？"

    xuchunxiang "只用‘息’与‘和’两段。"

    xuchunxiang "先把他的元息留住，再把不属于他的那股气慢慢化开。"

    "周青柳立刻明白，转身去配药。"

    zhouqingliu "我用轻方，不攻毒，只辅定息。"

    "陈素梅重新坐回针位。"

    chensumei "半炷香内，他若再乱冲，我下第二轮针。你们别碰他，也别哭。"

    "程明珠已经开始分派人手。"

    chengmingzhu "沈云，热水。"

    chengmingzhu "你，去夹廊小院取干净布巾，再告诉驿站，医馆前厅今日不接闲人。"

    chengmingzhu "魏三儿，你回去让郭总管留一条去雷云峰的信路。"

    "魏三儿脸色难得严肃。"

    weisaner "明白。"

    "你依言跑了一趟，把布巾和热水送到诊桌旁。"

    "程明珠只点了点头，没有夸奖，却也没有再把你当外人。"

    scene bg fuling_clinic_interior_day_chunhua_treatment with dissolve

    "片刻后，徐春香从二楼下来，手中多了一个紫檀小匣。"

    "她打开匣子，里面是银针、细瓶、一卷浅色绢帛，还有几枚温润如玉的药丸。"

    "她没有立刻喂药，而是先以两指按脉，闭目三息。"

    "前厅所有声音都低了下去。"

    "随后，徐春香以极轻的手法按在伤者胸口与腕脉之间。"

    "她以“息诀”先定住伤者元息，再以“和诀”引那股外息从胸腹间缓缓散开，不让它再冲向头颈。"

    "陈素梅在旁补针，周青柳递药，沈星辰捧匣，沈云端水，程明珠挡住围观的人。"

    scene bg fuling_clinic_interior_day_patient_stabilized with dissolve

    "过了许久，伤者喉咙里忽然发出一声极长的喘息。"

    "他颈侧青色血脉慢慢退下去，眼球也不再鼓得吓人。"

    "脸色仍然灰败，却终于不再重复那句怪话。"

    "高个男子扑上前半步。"

    gaoge_nanzi "大哥！"

    "陈素梅冷冷道："

    chensumei "再近一步，他刚稳住的气就白稳了。"

    "高个男子立刻停住。"

    "徐春香收手，声音有些疲惫。"

    xuchunxiang "命暂时留下了。能不能醒，醒后还能不能像从前一样，要看今晚。"

    "矮个男子低声道："

    aige_nanzi "那……那我们……"

    "徐春香看向他们。"

    xuchunxiang "你们两个，今晚也留下。"

    "矮个男子一惊。"

    aige_nanzi "凭什么？"

    "李默的手按在刀柄上，终于开口。"

    limo "凭你们走过不该走的路，见过不该见的人，还说了不该说的谎。"

    "徐春香语气依旧平和。"

    xuchunxiang "医馆不审人，但医馆也不替人藏祸。"

    xuchunxiang "你们若真想救他，就把昨夜从哪条路上山、谁指的路、看见了什么，全告诉周药师。"

    "高个男子低下头。"

    gaoge_nanzi "我们说。"

    "徐春香转向周青柳。"

    xuchunxiang "写医案。送风雷观。"

    "周青柳问："

    zhouqingliu "怎么写？"

    "徐春香看了一眼担架上的人。"

    xuchunxiang "写‘擅入外山者，外息冲脉，已暂留性命，请风雷观查山路’。"

    "她顿了顿，又说："

    xuchunxiang "别写求丹。求丹还有情可原，偷丹就不好听了。"

    "魏三儿从门边探头。"

    weisaner "那信让谁送？"

    "徐春香看向夹廊小院北侧。"

    xuchunxiang "郭路平会知道。"

    call music_sad from _call_music_sad

    "你站在一旁，看着医馆众人各自归位。"

    "徐春香救命，陈素梅控脉，周青柳写医案，程明珠管人，沈云跑腿，沈星辰捧着药匣，李默守住门口。"

    "你忽然明白：茯苓医馆的安静，不是不问江湖，而是江湖到了门前，它先救人，再算账。"

    scene bg fuling_clinic_interior_evening_patient_wakes with dissolve

    "傍晚时，伤者终于短暂醒了一次。"

    "他睁开眼，只说了一句话："

    shangzhe "不是丹炉……炉后还有人……"

    "说完便又昏睡过去。"

    "这句话很快传到了长风楼。"

    "魏三儿低声对你说："

    weisaner "今晚长风楼肯定热闹。"

    weisaner "有人会说风雷观藏了怪物，有人会说云清道长杀人灭口。"

    weisaner "去听听吧，假话传得快，真话有时候也藏在假话里。"

    "沈云也说："

    shenyun "去听听。若有人故意把这事传歪，医馆和风雷观都要麻烦。"

    "你想起白日里的驿站住满、医馆伤者，还有那句“炉后还有人”，决定去长风楼看看。"

    weisaner "快去快回。宵禁前一定回来。"

    weisaner "长风楼那地方，酒喝多了的人，说出来的话比梦还长。"

    "魏三儿本来不放心你一个人去，临走前嘱咐了你一句。"

    "你答应后，前往长风楼。"

    $ helped_fuling_clinic = True

    jump s018_changfeng_rumors


label s018_changfeng_rumors:

    scene bg changfeng_lou_exterior_night_rumor_crowd with dissolve
    call music_daily from _call_music_daily_17

    "傍晚时分，距离宵禁还有两个时辰。"

    "开庵镇正北一带，比白天更热闹。"

    "长风楼、青云楼、凰龙客栈、清沐所的灯笼陆续亮起。"

    "酒香、肉香、热水汽和马粪味混在一起，竟也成了江湖味道。"

    "长风楼门口人来人往。"

    "楼上楼下坐满了江湖客。"

    "有人带刀，有人背琴，有人一身富贵，有人满身尘土。"

    "白日里茯苓医馆抬进怪症伤者的事，已经像风一样传了过来。"

    scene bg changfeng_lou_exterior_night_rumor

    "辛万和正站在柜台后，脸上挂着笑，眼神却一直扫着全场。"

    "长风楼今夜生意极好。"

    "但越是生意好，越容易出事。"

    "你刚进门，就听见有人拍桌。"

    scene bg changfeng_lou_interior_evening

    jianghukejia "我亲耳听说了！风雷观丹炉里不是炼丹，是炼人！"

    "另一桌立刻有人反驳。"

    jianghukeyi "胡说！那丹是锁年岁的神丹，吃一颗能定住三十年容颜！"

    "又有人冷笑。"

    jianghukebing "若真是神丹，风雷观为何封山？我看是云清道长想借丹收服江湖！"

    "说书人坐在楼梯旁，本来正在说前朝旧案。"

    "此刻见众人都在谈雷云峰，他便顺势改了话头。"

    shuoshuren "诸位且听！"

    shuoshuren "今日茯苓医馆抬进一人，青筋如蛇，眼凸如鬼，口中只念八字——奇哉怪也，所见非人间！"

    "楼中一片哗然。"

    "你找了个角落坐下，听着传言越滚越大。"

    "有人说，那人是被风雷观道姑打成这样的。"

    "有人说，不是打，是灭口，那人看见了不该看的东西。"

    "有人说，丹炉后头有怪物，专吃求丹人的元息。"

    "还有人压低声音说，长息定年丹要用活人做引，否则怎么能定年。"

    "你越听越觉得荒唐。"

    "白日里你在医馆亲眼见到的情况，已经被传得面目全非。"

    "辛万和试图压住场面。"

    xinwanhe "诸位，喝酒归喝酒，话别说得太满。"

    xinwanhe "长风楼卖酒，不卖人命官司。"

    "可酒客们反而更兴奋。"

    "说书人也趁势添油加醋。"

    shuoshuren "那伤者临昏前曾道：不是丹炉，炉后有人！"

    shuoshuren "诸位想想，炉后若无人，何来此言？"

    "你听到这里，终于忍不住站了起来。"

    if protagonist == "wangfang":
        wangfang "我今日在茯苓医馆见过那名伤者。"
    else:
        zuowan "我今日在茯苓医馆见过那名伤者。"

    "大堂里安静了一瞬。"

    "说书人立刻看向你。"

    shuoshuren "这位少侠亲眼见过？"

    if protagonist == "zuowan":
        "说书人又眯眼看了看你，赶紧改口。"
        shuoshuren "这位侠女亲眼见过？"

    shuoshuren "那可要说清楚了。"

    "你把自己知道的部分说了出来。"

    "那人不是被风雷观无故加害。"

    "他是擅闯雷云峰外山，靠近不该靠近的地方，导致外息冲脉。"

    "所谓道姑用拂尘伤人，更可能是在他撑不住时，以内力替他压住乱冲的气脉，保住了一条命。"

    "茯苓医馆已经救下此人，也会写医案送往风雷观。"

    if protagonist == "wangfang":
        wangfang "医馆先救人，风雷观也未必是害人者。"
        wangfang "诸位若没亲眼看见，最好别把救命说成杀人。"
    else:
        zuowan "医馆先救人，风雷观也未必是害人者。"
        zuowan "没亲眼看见的事，传得越满，越容易害人。"

    "众人又安静了一瞬。"

    "可很快，一名江湖客冷笑。"

    jianghukejia "你说你亲眼见过，我们便要信？"

    "另一人接话。"

    jianghukeyi "你既从医馆来，当然替医馆和风雷观说话。"

    "还有人低声道："

    jianghukebing "说不定这人就是风雷观派来压消息的。"

    "辛万和见势不妙，立刻出来圆场。"

    xinwanhe "行了行了，长风楼里喝酒可以，审人不行。"

    xinwanhe "谁再拍桌，今晚酒钱翻倍。"

    "众人笑了几声，气氛暂时散开。"

    "但你已经意识到：自己说出的真相，并没有阻止谣言。"

    "它只是让谣言又多了一个版本。"

    "说书人甚至低声念叨。"

    shuoshuren "医馆救命，风雷藏人，外息冲脉，炉后有人……"

    shuoshuren "好，好故事。"

    "你心里一沉。"

    "你离开长风楼时，天色已经更暗。"

    "楼里仍然热闹。"

    "传言并没有因为你的解释而停下。"

    "相反，你刚刚说过的话，已经被人改成了新的版本。"

    "酒客甲：“听见没？医馆的人承认了，真有外息冲脉！”"

    "酒客乙：“炉后有人是真的！”"

    "酒客丙：“风雷观要压消息！”"

    scene bg changfeng_lou_alley_night_housanxian with dissolve

    "你站在长风楼门外，心里有些发堵。"

    "这时，旁边巷口传来一个熟悉的声音。"

    housanxian "我本来想来听热闹，结果听见有人比我还能编。"

    "你转头，看见侯三闲蹲在墙根，嘴里叼着一根草，像是已经听了很久。"

    if protagonist == "wangfang":
        wangfang "你知道什么？"
    else:
        zuowan "你知道什么？"

    "侯三闲收起嬉笑，朝西街方向看了一眼。"

    housanxian "这里不是说话的地方。"

    housanxian "你要真想知道谁把这事传歪了，明天一早去西街巷口找我。"

    "你心里一动。"

    "白日里医馆的伤者，夜里长风楼的谣言，似乎都指向同一个问题。"

    "有人不想让真相按原样传出去。"

    "你和侯三闲在长风楼外分别。"

    "回去的路上，你忽然想到一个更现实的问题。"

    "如果明天一早要去西街巷口，自己该怎么向魏三儿或沈云请假？"

    "夜风从风云坪吹来，长风楼里的喧闹声渐渐远了。"

    "你第一次意识到，在开庵镇住下，不只是有了一张床，也意味着每一天都要向这座小镇交代自己的去处。"

    jump s019_hou_sanxian_message


# =========================
# S019｜侯三闲的消息
# =========================

label s019_hou_sanxian_message:

    scene bg jialang_courtyard_morning_fangdaniang_task with dissolve

    call music_daily from _call_music_daily_18

    "第二日清晨。"

    "你刚从夹廊小院出来，心里还在想着昨夜侯三闲说的那句话。"

    "明天一早，去西街巷口找我。"

    "你还没想好怎么向魏三儿或沈云请假，方大娘已经从驿站厨房探出头来。"

    "她手里拿着一串铜钱。"

    fangdaniang "你不是要去菜市？"

    fangdaniang "正好，别白走一趟。"

    fangdaniang "替我办两件事。"

    if protagonist == "wangfang":

        wangfang "早啊方大娘，我正想着怎么跟你们请个假呢。"

    else:

        zuowan "早啊方大娘，我正想着怎么跟你们请个假呢。"

    "方大娘把二百文塞到你手里。"

    fangdaniang "先去马具行找宋老六，问周二蛋订的马鞍好了没有。"

    fangdaniang "再去南北杂货找范有成，买两只熏鸡回来。"

    fangdaniang "记住，方大娘要的，必须是新货。"

    fangdaniang "他要敢拿昨日陈货糊弄你，我晚上拿锅铲去问候他。"

    "这时，沈云从医馆侧门探出头，手里攥着二十文。"

    shenyun "你真去西街啊？"

    shenyun "那帮我带点切糕。"

    if protagonist == "wangfang":
        wangfang "你自己怎么不去？"
    else:
        zuowan "你自己怎么不去？"

    shenyun "我要洗药。"

    shenyun "徐掌柜说我昨日把药筛撞歪了，今天得补回来。"

    "他把二十文递过来，小声说："

    shenyun "买老马家的切糕，马长顺那个摊子。"

    shenyun "二十文，刚好两斤。"

    shenyun "你和星辰也吃一点，剩下的给我哦。"

    "你接过钱，忽然觉得自己虽然才住下没多久，却已经被驿站和医馆一起差遣了。"

    scene bg west_market

    "于是，你带着方大娘的二百文和沈云的二十文，前往西街菜市。"

    "西街菜市清晨最热闹。"

    "菜叶上还带着水，鱼摊腥气未散，铸兵堂那边已经传来打铁声。"

    "叫卖声、讲价声、骂人声混在一起。"

    scene bg west_market_machangshun_qiegao_day with dissolve

    "你一进菜市，先看见老马切糕摊。"

    "切糕摊摊主马长顺正守着一只冒热气的大木甑。"

    "原来这里卖的切糕并不是那种一大坨硬邦邦的甜点。"

    "而是以糯米为主，点缀着大枣和黑枣，蒸得软糯热腾，倒更像一块块刚出甑的甜米糕。"

    "马长顺掀开木盖时，白气一涌，枣香和糯米香立刻散开。"

    "你本想先买切糕，但又想到还要去找宋老六和买熏鸡，怕切糕放久了凉掉，便决定最后再买。"

    scene bg west_market_nanbei_grocery_day with dissolve

    "你转身看见南北杂货。"

    "南北杂货门口挂着腊肉、熏鸭、干辣椒和一排油纸包。"

    "掌柜范有成正站在柜后和客商说价。"

    fanyoucheng "这价真不贵，客官。北边来的香料，路上风沙都比盐贵。"

    "你上前。"

    if protagonist == "wangfang":
        wangfang "方大娘让我来买两只熏鸡。"
    else:
        zuowan "方大娘让我来买两只熏鸡。"

    "范有成脸上的笑停了一下。"

    fanyoucheng "方大娘要的？"

    "你点头。"

    "范有成立刻朝后头喊。"

    fanyoucheng "小麻子！拿新做的，别拿昨日那两只！"

    "后头传来小麻子的声音。"

    xiaomazi "昨日那两只不也挺香……"

    "范有成瞪过去。"

    fanyoucheng "你香？你去跟方大娘说？"

    "小麻子立刻闭嘴，把两只熏鸡用油纸包好。"

    "范有成把熏鸡放到你面前。"

    fanyoucheng "一只六十文，两只一百二。"

    fanyoucheng "你回去跟方大娘说，我这价格童叟无欺，她真人来了也是这个价。"

    "你看了他一眼。"

    "范有成又补一句。"

    fanyoucheng "当然，她真人来了，我可以多送一把干菇。"

    "你付了一百二十文，收好熏鸡。"

    scene bg west_market_repair_shop_day with dissolve

    "接着，你去找宋老六。"

    "但你一时没认出马具行，先看见修理铺的招牌，便上前询问。"

    if protagonist == "wangfang":
        wangfang "请问哪位是老宋？我是飞鸿驿站派来问周二蛋订的马鞍好了没。"
    else:
        zuowan "请问哪位是老宋？我是飞鸿驿站派来问周二蛋订的马鞍好了没。"

    "修理匠刘山平正在修一盏旧灯，抬头看了你一眼。"

    liushanping "找错了。我这是修理铺。"

    liushanping "锅漏了、椅子断了、灯坏了、鞋底开了，都能找我。"

    liushanping "马鞍坏了，也能修，但新马鞍不归我。"

    "旁边的学徒刘小小探头。"

    liuxiaoxiao "比送回马具行修便宜很多呢。"

    liuxiaoxiao "怎么，旧马鞍是裂了，还是扣带断了？"

    if protagonist == "wangfang":
        wangfang "我只是来问订的新马鞍。"
    else:
        zuowan "我只是来问订的新马鞍。"

    "刘小小有些失望。"

    liuxiaoxiao "哦，新货啊。"

    liuxiaoxiao "那你往前走，马具行在铸兵堂斜对面。看见门口挂鞍子的就是。"

    "你道谢后离开。"

    scene bg west_market_alley_youjiezai_group_day with dissolve

    "刚要往马具行走，忽然看见前方巷口的一段石阶上蹲着一群年轻人，其中就有侯三闲。"

    "这几个人各有各的懒散姿态。"

    "一个棕色麻衣、中等个子的男孩靠在竹筐边，眼睛半睁半闭，像是刚睡醒，又像是随时能再睡过去。"

    "一个穿浅绿色衣裙、看着很机灵的女孩站在一旁，正拿脚尖拨地上的小石子，嘴上嫌弃侯三闲挡道。"

    "一个小个子男孩穿着一身黑色旧衣，腰间挂着一个鼓鼓的大锦囊。"

    "他手里转着一颗旧骰子，转两下便掉一次，掉了又若无其事地捡起来。"

    "一个漂亮高挑的女孩站在阴影里，淡蓝色衣裙洗得发旧却干净，双手缠着绑带，抱着胳膊看着众人，像是在看一群人犯傻。"

    "还有一个小个子女孩蹲在墙根，头上扎着几根小辫，穿着深靛色粗布衣衫。"

    "她正学着长风楼说书人的腔调，拖长声音道："

    "小辫女孩：“所闻非所见——所见非人间——奇哉——怪也——”"

    "浅绿色衣裙的女孩一脚踢过去。"

    "浅绿衣裙女孩：“你再学，晚上真做噩梦。”"

    "侯三闲蹲在最中间，手里叼着一根草梗。"

    "红色发带束着长发，腰间还挂着那把木刀。"

    "他个子比旁边几人都高些，明明一身穷酸，却偏要摆出几分江湖人的架势，像是已经等了你很久。"

    "一见你来了，侯三闲立刻站起身，像终于等到了能显摆的人。"

    housanxian "来了？我跟你说，昨晚那谣言不是自己长腿跑到长风楼的。"

    "你却先举了举手里的熏鸡。"

    if protagonist == "wangfang":
        wangfang "我还得找马具行的老宋。周二蛋订的马鞍，方大娘让我来问。"
    else:
        zuowan "我还得找马具行的老宋。周二蛋订的马鞍，方大娘让我来问。"

    "侯三闲一愣。"

    housanxian "你这人怎么这样？我这儿是江湖大事。"

    if protagonist == "wangfang":
        wangfang "方大娘那边也是大事。"
    else:
        zuowan "方大娘那边也是大事。"

    "浅绿色衣裙的女孩坐在石阶上点头，接话道："

    "浅绿衣裙女孩：“这话没毛病。方大娘的事，比江湖事急。”"

    "侯三闲噎了一下，只好摆手。"

    housanxian "行行行，跟我走。老宋我认识。"

    "他转头向你介绍。"

    housanxian "这是罗小六，跑巷子的；这是马二花，嘴最毒的。"

    housanxian "这是梁阿坠，关扑铺门口长大的。"

    housanxian "这是杜七娘，谁欠她一文都记得。"

    housanxian "这是钱四喜，最小，最吵。"

    "小辫女孩立刻不服。"

    qiansixi "我哪是吵，我这是会学。"

    "你这才把几个人和名字对上。"

    "棕色麻衣、眼睛总像没睡醒的，是罗小六。"

    "浅绿色衣裙、说话带刺的，是马二花。"

    "黑衣小个子、腰间挂大锦囊的，是梁阿坠。"

    "淡蓝色旧衣裙、双手缠着绑带的，是杜七娘。"

    "深靛色粗布衣衫、扎着小辫子的，是钱四喜。"

    if protagonist == "wangfang":
        wangfang "你们这三闲、四喜、小六、七娘的，谁是老大？"
    else:
        zuowan "你们这三闲、四喜、小六、七娘的，谁是老大？"

    "几个人同时看向侯三闲。"

    "侯三闲立刻挺胸。"

    housanxian "这还用问？"

    "马二花冷笑。"

    maerhua "谁欠钱最多，谁就是老大。"

    "罗小六慢吞吞补一句。"

    luoxiaoliu "那是他。"

    "侯三闲瞪他们。"

    housanxian "你们懂什么？江湖人不叫欠钱，叫人情往来。"

    "杜七娘淡淡道。"

    duqiniang "人情会还，钱也要还。"

    "你第一次真正见到侯三闲的朋友们。"

    "他们不像恶霸，也不像正经伙计，更不是帮派。"

    "只是一群在菜市墙根、关扑铺门口、杂货铺旁边混日子的年轻人。"

    "每个人都有自己的小聪明，也都有自己的窘迫。"

    "侯三闲说完“老宋我认识”，便往马具行方向走。"

    "梁阿坠立刻跟了上来。"

    "他把那颗旧骰子塞回腰间的大锦囊里，像是终于等到自己能派上用场。"

    "杜七娘也跟了两步。"

    "她没有解释，只是看了侯三闲一眼，像是不放心他把话说得太满。"

    "罗小六刚要跟，马二花一把拽住他的袖子。"

    maerhua "你留下。"

    "罗小六慢吞吞地看她。"

    luoxiaoliu "为什么？"

    "马二花朝菜市另一头抬了抬下巴。"

    maerhua "你不是认路最熟吗？盯着点巷口。"

    maerhua "要是刚才那个灰衣人白天又从西街冒出来，你比我们先看见。"

    "罗小六想了想，点头。"

    luoxiaoliu "哦。那我坐着看。"

    "钱四喜也想跟上，已经迈出半步，却被马二花用一根手指戳回石阶。"

    qiansixi "我也想听！"

    maerhua "你不许听。你听完一遍，整个西街都能听第二遍。"

    "钱四喜不服气地鼓起脸。"

    qiansixi "我那叫会讲。"

    maerhua "所以你更不能去。"

    "于是罗小六靠回竹筐边，半睁着眼盯着巷口。"

    "钱四喜蹲在旁边扯草叶。"

    "马二花留在石阶上看着他们，也顺便留意菜市里来来往往的人。"

    scene bg west_market_youjiezai_clue_walk_day with dissolve

    "跟着你往马具行方向走的，只剩侯三闲、梁阿坠和杜七娘。"

    if protagonist == "wangfang":
        wangfang "你昨晚说，知道谁把事传歪了？"
    else:
        zuowan "你昨晚说，知道谁把事传歪了？"

    "侯三闲压低声音。"

    housanxian "我没看清是谁，但我知道那话不是从医馆传出来的。"

    if protagonist == "wangfang":
        wangfang "你怎么知道？"
    else:
        zuowan "你怎么知道？"

    housanxian "医馆的人说话没那么会添油加醋。"

    housanxian "长风楼昨晚最早那句‘云清道长杀人灭口’，是一个灰衣江湖客先说的。"

    housanxian "他说完没多久，三张桌子都开始讲同一个版本。"

    if protagonist == "wangfang":
        wangfang "灰衣江湖客？"
    else:
        zuowan "灰衣江湖客？"

    "梁阿坠在旁边插嘴。"

    liangazhui "腰间挂着黑布袋，走路不响。"

    liangazhui "进长风楼没点菜，只点了一壶最便宜的酒。"

    if protagonist == "wangfang":
        wangfang "你昨晚也在？"
    else:
        zuowan "你昨晚也在？"

    "梁阿坠把骰子往袖里一藏。"

    liangazhui "我在后巷。"

    liangazhui "关扑铺散得晚，我顺路听了两句。"

    "杜七娘补充。"

    duqiniang "我也在门口。"

    duqiniang "那会儿楼里太吵，侯三闲和阿坠又只顾听话，我只能看人。"

    "侯三闲不服。"

    housanxian "什么叫只顾听话？我那叫抓重点。"

    duqiniang "所以你没看见他左手一直按着黑布袋。"

    "梁阿坠把旧骰子又摸出来，在指间转了一下。"

    liangazhui "那人坐的位置也怪。"

    liangazhui "不上二楼，不靠窗，不靠说书人，偏坐在能看见三张桌子的角落。"

    liangazhui "说一句，三边都能听见。"

    if protagonist == "wangfang":
        wangfang "所以他是故意的？"
    else:
        zuowan "所以他是故意的？"

    housanxian "我不敢说故意。"

    housanxian "但他说完就走，走得比结账的人还快。"

    if protagonist == "wangfang":
        wangfang "那人后来去哪了？"
    else:
        zuowan "那人后来去哪了？"

    "侯三闲表情变得认真一点。"

    housanxian "这就是我要说的。"

    housanxian "昨晚宵禁前，我在长风楼外墙根躲巡捕……不是，歇脚。"

    housanxian "看见那灰衣人从后巷走了，没往客栈，也没往南门，而是绕去了镇北小路。"

    if protagonist == "wangfang":
        wangfang "镇北小路？"
    else:
        zuowan "镇北小路？"

    "侯三闲点头。"

    housanxian "不是上风雷观正路，是老采药人和砍柴人以前走的小路。"

    housanxian "夜里没人走。"

    housanxian "那人走得很熟。"

    if protagonist == "wangfang":
        wangfang "你确定？"
    else:
        zuowan "你确定？"

    "侯三闲嘴硬地说："

    housanxian "我侯三闲别的不行，认人尾巴最行。"

    "杜七娘淡淡道："

    duqiniang "他这点确实行。欠账的人从街头拐到街尾，他都能认出来。"

    "梁阿坠小声补一句。"

    liangazhui "就是跟踪。"

    "侯三闲立刻纠正。"

    housanxian "江湖上叫缀行。"

    "几人走到一处摊棚阴影下，侯三闲的声音更低了些。"

    housanxian "但这事我不去官府说。"

    "你看向他。"

    "侯三闲抢先道："

    housanxian "不是怕。我是……谨慎。"

    "杜七娘看向你，语气平静，却比侯三闲的话更重。"

    duqiniang "你别逼他去官府。"

    duqiniang "他真去了，第二天西街就没人敢跟他说话。"

    "你一时没有接话。"

    "杜七娘继续说："

    duqiniang "我们这种人，知道一点风吹草动还能混饭吃。"

    duqiniang "可要是站到明处，给谁作证，指谁有罪，就不只是挨一顿打的事了。"

    "梁阿坠低头拨弄骰子，声音很小。"

    liangazhui "关扑铺那边有些人，最不喜欢别人认得太清。"

    "侯三闲强撑着笑了一下。"

    housanxian "所以我只能告诉你。"

    housanxian "你要说，就说你自己听来的，别把我名字带出去。"

    "你明白了。"

    "侯三闲不是不想帮，而是他这种人一旦公开作证，就会惹上他承受不起的麻烦。"

    "而这也正说明：西街的游街子们虽然不起眼，却常常比坐在酒楼里的人更早看见真相。"

    scene bg west_market_harness_shop_day with dissolve

    "几人说话间，已经到了马具行。"

    "门口挂着鞍子、缰绳、马嚼子。"

    "宋老六正蹲在门口给一副马鞍上油。"

    "侯三闲喊道："

    housanxian "宋老六！驿站来问货！"

    "宋老六抬头。"

    songlaoliu "你又代表驿站了？"

    if protagonist == "wangfang":
        wangfang "我是替周二蛋来问，他订的马鞍好了没有。"
    else:
        zuowan "我是替周二蛋来问，他订的马鞍好了没有。"

    "宋老六擦了擦手。"

    songlaoliu "好了。"

    songlaoliu "就是他要加的那层软垫费工。"

    songlaoliu "你回去告诉他，下午来取。若嫌慢，让他自己来缝。"

    "侯三闲立刻搭话。"

    housanxian "周二蛋自己缝，马骑上去都得哭。"

    "宋老六瞥他一眼。"

    songlaoliu "你要是再在我门口挡客，我先让你哭。"

    "你下消息，向宋老六道谢。"

    "你看了看日头，心想得快点回去告诉飞鸿驿站的人才行。"

    "问完马鞍的事，你想起沈云交代的切糕。"

    "侯三闲一听切糕，立刻指了指来路。"

    scene bg west_market_qiegao_youjiezai_share_day with dissolve

    housanxian "老马的摊子就在刚才那段石阶斜对面。"

    housanxian "你放心，他那糕热着呢，刀下去还冒气。"

    "你跟着侯三闲、梁阿坠、杜七娘往回走。"

    "刚回到巷口石阶附近，便看见马二花还坐在那里，罗小六靠着竹筐盯着巷口，钱四喜正无聊地用草叶编小环。"

    "钱四喜一见几人回来，立刻跳起来。"

    qiansixi "说完啦？有热闹吗？"

    "马二花看她一眼。"

    maerhua "有热闹也不讲给你听。"

    maerhua "你一张嘴，能把半句传成三回书。"

    "钱四喜不服气。"

    qiansixi "我那叫添彩。"

    "你没有立刻接话，只看向斜对面的切糕摊。"

    "马长顺的切糕摊前还冒着白气。"

    "木甑里铺着厚厚的糯米，枣子被蒸得发亮，黑枣嵌在米粒间，甜香混着热气往外散。"

    "马长顺用木刀沿着边缘切下一块，软糯的糕体微微塌下去，却仍然成形。"

    "你拿出沈云给的二十文。"

    if protagonist == "wangfang":
        wangfang "马掌柜，切糕两斤。"
    else:
        zuowan "马掌柜，切糕两斤。"

    "马长顺把两斤热切糕用油纸细细包好，又在外头多垫了一层草纸，递给你。"

    machangshun "二十文，正好。"

    machangshun "拿稳了，趁热吃最好。凉了也能吃，就是少一半香。"

    "你收好这包切糕，准备带回去给沈云和沈星辰。"

    "钱四喜这才看明白，眼睛一下亮了。"

    qiansixi "原来是买切糕啊。"

    "侯三闲咳嗽一声，假装不在意，眼神却已经往木甑上飘了两回。"

    "你想了想，又从自己的钱里添了三十文。"

    if protagonist == "wangfang":
        wangfang "再来三斤。"
    else:
        zuowan "再来三斤。"

    "马长顺看了看你，又看了看旁边那群游街子，笑了一下，没有多问。"

    "他又切了三斤，用另一张油纸包好。"

    "你把新买的那包递给侯三闲他们。"

    "侯三闲接过切糕，先愣了一下，然后故作潇洒。"

    housanxian "这怎么好意思。"

    "马二花已经接过去咬了一口。"

    maerhua "你不好意思可以不吃。"

    "侯三闲立刻把切糕收回怀里。"

    housanxian "我替江湖收下。"

    "钱四喜吃得眼睛发亮。"

    qiansixi "甜的！"

    "罗小六慢吞吞地嚼了一口，点头。"

    luoxiaoliu "比馒头有意思。"

    "梁阿坠把切糕掰成小块，像分赌注一样分给众人。"

    liangazhui "一人一块，别抢。抢了就少了。"

    "杜七娘看了你一眼，没有立刻吃，只问："

    duqiniang "你自己还有钱吗？"

    if protagonist == "wangfang":
        wangfang "够回去交差。"
    else:
        zuowan "够回去交差。"

    "马二花看着你，忽然说："

    maerhua "你这朋友，我交定了。"

    "侯三闲立刻不满。"

    housanxian "这是我先认识的。"

    "罗小六慢吞吞道："

    luoxiaoliu "你是借钱认识的。"

    "众人笑起来。"

    "你收好给沈云和沈星辰的那包切糕，又提起方大娘要的两只熏鸡。"

    "侯三闲把嘴里的切糕咽下去，压低声音补了一句："

    housanxian "记住，灰衣人、黑布袋、镇北小路。"

    housanxian "别说是我说的。"

    "你点头，带着熏鸡和切糕离开西街菜市。"

    $ hou_sanxian_relation += 1

    jump s020_night_return_base



# =========================
# S020｜夜归落脚处
# =========================

label s020_night_return_base:
    
    if protagonist == "wangfang":
        scene bg feihong_inn_evening_return_errand_wangfang with dissolve
    elif protagonist == "zuowan":
        scene bg feihong_inn_evening_return_errand_zuowan with dissolve
    else:
        scene bg feihong_inn_evening_return_errand_wangfang with dissolve

    call music_daily from _call_music_daily_19

    "你回到飞鸿驿站时，天色已经暗下。"

    "方大娘正在厨房门口等着，看见你手里提着油纸包，先问："

    fangdaniang "熏鸡呢？"

    "你把两只熏鸡递过去，又把剩下的八十文取出来。"

    "你：“两只熏鸡一百二十文，这是剩下的八十文。”"

    "你：“另外，周二蛋订的马鞍问到了。宋老六说下午已经做好，是加软垫的那副，让周二蛋自己去取。”"

    "方大娘接过熏鸡，掂了掂分量，满意地点头。"

    "她没有接那八十文，只看了你一眼。"

    fangdaniang "钱你先收着。"

    "你一怔。"

    "你：“这是您的钱。”"

    "方大娘把手在围裙上擦了擦。"

    fangdaniang "让你跑腿，又让你打听消息，哪能一文不给？"

    fangdaniang "这不叫赏，也不叫施舍，叫跑腿钱。"

    fangdaniang "你既住在夹廊小院，就得知道：帮人做事，账要清，人情也要清。"

    "周二蛋正好从马厩方向探头。"

    zhouerdan "我的马鞍好了？"

    "你点头。"

    "周二蛋一拍大腿。"

    zhouerdan "太好了！我那旧鞍再用两天，马没疯，我先疯。"

    "方大娘却没有像平时那样继续斗嘴，而是压低声音。"

    call music_tension from _call_music_tension_1

    scene bg jialang_courtyard_night_strategy_meeting with dissolve

    fangdaniang "先别嚷。跟我来。"

    "你这才发现，驿站和医馆的气氛都不太对。"

    "方大娘带你走进夹廊小院。"

    "这里北接飞鸿驿站后门，南通茯苓医馆侧门，西侧是雷凌宫东墙，东侧屏风门外便是风云坪。"

    "夹廊小院里，旧木大桌旁已经坐了不少人。"

    "方鹤鸣正展开一张驿道图。"

    "魏三儿抱着胳膊站在桌边，难得没有乱插话。"

    "周二蛋跟进来后，也收了笑。"

    "南侧医馆门边，徐春香、陈素梅、程明珠都在。"

    "李默站在通往风云坪的屏风门旁，手按刀柄。"

    "沈星辰抱着药书坐在角落，脸色有些发白。"

    "你刚一进来，就感觉到：这里不是闲聊，是商议大事。"

    "方大娘把熏鸡放到桌边，却没人动。"

    "魏三儿先开口："

    weisaner "你回来了？侯三闲怎么说？"

    "你把西街菜市的事讲了一遍。"

    "灰衣江湖客。"

    "黑布袋。"

    "长风楼最早传歪的话。"

    "宵禁前绕去镇北小路。"

    "你说完，夹廊小院一时安静。"

    "李默看向郭路平方向空着的位置，低声道："

    limo "镇北小路，确实能绕到外山。"

    "程明珠眉头一紧。"

    chengmingzhu "所以昨天的医馆伤者，不是唯一一批走小路的人。"

    "陈素梅冷冷道："

    chensumei "也可能是同一条路把人引过去，再把谣言引回来。"

    "这时，徐春香缓缓说："

    xuchunxiang "医馆这边也有消息。"

    xuchunxiang "今日下午，风雷观山门附近传下话来，承天剑派凌霄子已经到了。"

    "周二蛋吸了口气。"

    zhouerdan "承天剑派掌门亲自来了？"

    "方鹤鸣抬头。"

    fangheming "若只为看丹，不必掌门亲至。"

    "徐春香继续说："

    xuchunxiang "梧天禅院的惠能大师也到了。静月师太随行。"

    "陈素梅听到“静月”二字，神色终于有了变化。"

    "沈星辰小声问："

    shenxingchen "是每年来医馆义诊、与您切磋针理的静月师太？"

    "陈素梅点头。"

    chensumei "是她。她不轻易离山。"

    "魏三儿皱眉。"

    weisaner "承天剑派、梧天禅院……这阵仗也太大了。"

    "程明珠补了一句。"

    chengmingzhu "还有东海沧海阁的人。来的是凌沧海本人，还是阁中其他人，暂时不清楚。"

    "周二蛋忍不住问："

    zhouerdan "那衡云堂来人了吗？万毒谷的苏玉寒呢？"

    "夹廊小院里没人立刻回答。"

    "这种沉默比回答更让人不安。"

    "方鹤鸣看向徐春香。"

    fangheming "一切皆由长息定年丹而起。春香，你可知其中关窍？"

    "徐春香沉吟片刻。"

    xuchunxiang "说实话，我也不知道真正原由。"

    xuchunxiang "风雷观炼丹，医馆确实供过几味药材，但我们供的是药，不是秘方。"

    "周二蛋忍不住问："

    zhouerdan "什么药材？"

    "徐春香看了一眼沈星辰。"

    "沈星辰低声说："

    shenxingchen "白霜茯苓、雷纹草、息风藤，还有一味……锁龄芝。"

    "方大娘一听就皱眉。"

    fangdaniang "这名字听着就贵。"

    "徐春香点头。"

    xuchunxiang "锁龄芝最难得。我与青柳平日都鲜少使用。"

    xuchunxiang "它本身不是什么长生药，只是能在极短时间内稳住衰败的气血。"

    xuchunxiang "若用得好，救人。若用得急，害人。"

    "陈素梅接话："

    chensumei "昨日那个伤者，像是误纳了未定之息。"

    chensumei "若定年丹还没成，丹炉外泄的气本就不稳。"

    "方鹤鸣皱眉。"

    fangheming "所以有人明知丹未成，仍在诱人靠近？"

    "你想到侯三闲说的灰衣人，心里一沉。"

    scene bg jialang_courtyard_night_guoluping_orders with dissolve

    "这时，夹廊小院北门被推开，郭路平走了进来。"

    "他身上带着一点夜风，神情仍稳，却比平日更沉。"

    guoluping "不用太过慌。"

    guoluping "几大门派齐聚风雷观，未必是坏事。"

    guoluping "至少说明他们都还愿意坐到山上谈，而不是在镇里打。"

    "魏三儿立刻问："

    weisaner "那要是谈不拢呢？"

    "郭路平看向众人。"

    guoluping "所以我们不能掉以轻心。"

    "他指了指风云坪方向。"

    guoluping "我已经去过雷凌宫。"

    guoluping "王德久今日闭门不出，王家已经加了护院。"

    guoluping "雷凌宫东墙就在夹廊西侧，咱们至少不用担心西边被人穿进来。"

    guoluping "真正要守的，是面向风云坪的屏风门，还有驿站、医馆两头的门。"

    "魏三儿嘀咕："

    weisaner "怪不得雷凌宫今天一天没开门。"

    guoluping "王家怕事，也有怕事的用处。"

    guoluping "门关得紧，总比门开着添乱强。"

    "程明珠开始接管调度。"

    chengmingzhu "从现在起，医馆前门半闭。"

    chengmingzhu "只接急症，且进来之前需要李默先确认安全。"

    chengmingzhu "普通问诊推到明日。药材库上锁。"

    chensumei "伤者那边我守前半夜。"

    "沈星辰立刻说："

    shenxingchen "我可以守药炉。"

    "陈素梅看他一眼。"

    chensumei "你守可以，别把药书掉炉里。"

    "方大娘把袖子一挽。"

    fangdaniang "这边我管饭。真要守夜，没饭先垮一半。"

    "周二蛋立刻举手。"

    zhouerdan "我守马厩。马一乱，人更乱。"

    "方鹤鸣铺开纸笔。"

    fangheming "我列值夜表。"

    fangheming "驿站、医馆、夹廊三处轮换。谁也不许凭热血乱跑。"

    "魏三儿看向你。"

    weisaner "你也别想躲。夹廊小院的人，今晚最不清闲。"

    "程明珠转向你，语气很正式。"

    chengmingzhu "屏风后面向风云坪的门已经锁好。"

    chengmingzhu "无论外头有什么声响，不经我或郭总管允许，不许开。"

    "你：“好，我记住。”"

    "方鹤鸣写字的笔停了一下。"

    fangheming "还有一条，若有人来问医馆伤者的事，一律说‘人在救治，不便探问’。"

    fangheming "不说丹，不说道姑，不说风雷观。"

    weisaner "那如果有人非要问？"

    "方大娘冷笑。"

    fangdaniang "就说方大娘在。"

    "众人紧张中终于有了一点笑意。"

    "众人正分派值夜时，夹廊小院北门忽然被猛地推开。"

    scene bg jialang_courtyard_night_lutiankuo_alarm with dissolve

    "鲁天阔冲了进来。"

    "他平时极少失态，可此刻额角全是汗，衣摆带着山路尘土，呼吸也乱了。"

    "手里攥着一只被火燎过边角的信筒。"

    "郭路平立刻站起。"

    guoluping "老鲁？"

    "鲁天阔看了一眼众人，声音低哑。"

    lutiankuo "糟了。"

    "魏三儿下意识问："

    weisaner "风雷观怎么了？"

    "鲁天阔把信筒放到桌上，沉声道："

    lutiankuo "风雷观外山失守，丹房方向起火。"

    lutiankuo "长息定年丹……不见了。"

    "夹廊小院一瞬间静得只剩药炉的咕嘟声。"

    "周二蛋手里的半碗水停在半空。"

    "方大娘脸上的笑意彻底没了。"

    "方鹤鸣的笔尖停在纸上，墨晕开一团。"

    "徐春香闭了闭眼。"

    "程明珠立刻看向门锁。"

    "李默拔刀半寸。"

    "魏三儿看向你，脸色发白。"

    "沈星辰轻声说："

    shenxingchen "丹若离炉，炉外未定之息……还压得住吗？"

    "没有人回答。"

    "郭路平最先回神。"

    guoluping "关门。灭外灯。夹廊小院今夜不散。"

    "徐春香接着说："

    xuchunxiang "医馆伤者不得移动。所有药匣上锁。"

    chengmingzhu "李默守屏风门。周二蛋回马厩。方鹤鸣列人。方大娘备热食。"

    chengmingzhu "魏三儿，把驿站里能用的铺盖都拿来。"

    "魏三儿怔了一下。"

    weisaner "拿铺盖？"

    "郭路平看了一眼众人。"

    guoluping "今晚所有人就近守着。"

    guoluping "能坐就坐，能躺就躺，夹廊小院打地铺。"

    "方大娘立刻回过神。"

    fangdaniang "那还愣着？"

    fangdaniang "冷地上躺一夜，没等江湖人打来，先把自己冻病了。"

    scene bg jialang_courtyard_night_floor_bedding with dissolve

    "众人立刻动起来。"

    "驿站那边搬来旧铺盖、草席、长凳。"

    "医馆那边送来药炉、热水、布巾和几只药枕。"

    "夹廊小院中间的旧木大桌被推到一旁。"

    "北耳房与南耳房门都半开着，屏风门上了两道闩。"

    "你站在一旁，帮着搬铺盖、递热水、合上门窗。"

    "昨日这里还是一处临时落脚的小院。"

    "今晚却变成了驿站与医馆共同守夜的堡垒。"

    "夜深后，众人或坐或躺，谁也没有真正睡着。"

    "风云坪外偶尔传来巡捕的脚步声。"

    "雷凌宫高墙后隐隐有护院低声交谈。"

    "医馆药炉小火未熄。"

    "驿站马厩里传来不安的马嘶。"

    "你躺在自己的耳房外，听见魏三儿小声问："

    weisaner "你说，明天会怎么样？"

    "无人回答。"

    "黑暗里，郭路平的声音低低响起："

    guoluping "先守过今晚。"

    jump s021_fengleiguan_seal_order


# =========================
# S021｜风雷观丹药失窃
# =========================

label s021_fengleiguan_seal_order:

    scene bg jialang_courtyard_dawn_after_watch with dissolve    
    call music_tension from _call_music_tension_2

    "一夜无事。"

    "但夹廊小院里，没有人真正睡熟。"

    "昨夜鲁天阔从雷云峰方向带回急信。"

    "众人得知风雷观外山失守，西院栖霞院丹房起火，长息定年丹不见。"

    "郭路平与徐春香当即决定让驿站与医馆共同守夜。"

    "夹廊小院中间的大桌被推到一旁，旧铺盖、草席和长凳铺了一地。"

    "北耳房与南耳房的门半开着，屏风门上了两道闩。"

    "天快亮时，药炉还温着，桌上放着没喝完的茶。"

    "魏三儿靠在长凳边打盹，手里还攥着昨夜没挂回去的客牌。"

    "周二蛋坐在院角，怀里抱着马鞍扣，脑袋一点一点地往下垂。"

    "方鹤鸣伏在桌边，旁边是半张没写完的值夜表。"

    "方大娘睡得最浅，听见一点响动就会睁眼。"

    "李默一夜没坐下，仍守在面向风云坪的屏风门旁。"

    "沈星辰抱着药书靠在墙边，脸色比昨日更白。"

    "你半梦半醒间，似乎还听见他低声念了一句："

    shenxingchen "丹被拿走了……那炉里没归处的气，会往哪里去？"

    "陈素梅昨夜的话还留在众人心里。"

    chensumei "若只是残息，风雷观还能封。若它跟着丹走，就麻烦了。"

    "没人再接话。"

    scene bg jialang_courtyard_morning_after_watch_wake with dissolve

    "第一缕天光落进夹廊小院时，风云坪上传来一阵铜锣声。"

    xunbusi_chayi "风雷观封山令——"

    "夹廊小院里的人几乎同时醒来。"

    "郭路平先起身，走到屏风门前。"

    "李默确认外头无异状后，打开门闩。"

    "徐春香也从医馆侧门走出。"

    "程明珠跟在她身后，神色清醒得像是一夜没睡。"

    "沈云从药炉那边探出头，手上还沾着水。"

    "魏三儿揉了揉眼睛，立刻清醒过来。"

    scene bg fengyunping_notice_sealing_order_day with dissolve

    "众人一同来到风云坪边。"

    "风云坪中央的告示牌前已经围了不少人。"

    "巡捕司差役正在维持秩序。"

    "一名风雷观外门弟子站在告示牌旁，脸色苍白，袖口有灰痕，发冠也有些歪，显然是匆忙下山。"

    "一纸封山令被贴在告示牌正中。"

    "封山令上写着："

    "风雷观封山三日。"

    "闲杂人等不得上山。"

    "擅闯者，后果自负。"

    "丹失之事，不许妄传。"

    "风云坪上的人群一下子炸开。"

    "有人低声惊呼。"

    zhenmin "丹真丢了？"

    "有人立刻转身往长风楼方向跑。"

    "有人试图挤到前面看清楚，却被巡捕司差役拦住。"

    xunbusi_chayi "退后！告示已张，私撕者拿下！"

    "魏三儿压低声音。"

    weisaner "丹失之事……他们竟然真写出来了？"

    "方鹤鸣皱眉，看着告示上的字。"

    fangheming "写出来，说明瞒不住。不许妄传，说明已经传开了。"

    "沈云小声问："

    shenyun "那昨日那个伤者呢？他两个弟弟呢？"

    "徐春香没有移开目光，只说："

    xuchunxiang "伤者留医馆。人醒稳之前，谁也不能带走。"

    "程明珠立刻接话。"

    chengmingzhu "医馆今日只接急症。普通问诊延后。前门半闭，夹廊小院继续留通道。"

    "郭路平没有说话。"

    "鲁天阔站在他身旁，脸色比昨夜更沉。"

    "他盯着封山令末尾的印痕，手指微微收紧。"

    "你注意到，郭路平、徐春香、鲁天阔、方鹤鸣的神情都有些不对。"

    "你问："

    "你：“这封山令有什么问题吗？”"

    "鲁天阔声音很低。"

    lutiankuo "印是真的。"

    "魏三儿不解。"

    weisaner "印是真的，那还有什么不对？"

    "鲁天阔抬眼看着告示。"

    lutiankuo "这不是掌门印。"

    "众人一静。"

    "徐春香也看向那枚印，神情沉了下来。"

    xuchunxiang "是玄雷院急令印。"

    "方鹤鸣轻声解释："

    fangheming "风雷观掌门云清道长的印，是‘清玄法印’。"

    fangheming "若是掌门亲令，封山令上该盖清玄法印。"

    fangheming "可这张令上盖的是玄雷院副印，也就是玄雷院急令印。"

    "你：“玄雷院副印，也能封山？”"

    "方鹤鸣点头。"

    fangheming "能。"

    fangheming "玄雷院是风雷观主院，掌门居所、藏经阁、议事堂都在玄雷院。"

    fangheming "玄雷院急令印由掌印人保管，遇到紧急事务，可以代掌门传令。"

    fangheming "但它毕竟不是掌门印。"

    "沈星辰轻声问："

    shenxingchen "那云清道长呢？"

    "没有人立刻回答。"

    "鲁天阔看着封山令，声音更低了些。"

    lutiankuo "玄雷院急令印由玄蘅真人保管。"

    lutiankuo "除非掌门不便亲令，否则不会轻易用。"

    weisaner "掌门不便亲令……是什么意思？"

    "方大娘皱眉。"

    fangdaniang "还能是什么意思？要么人不在，要么人出事，要么有些话不能由她亲口说。"

    "这话一出，众人都安静了一瞬。"

    "风云坪上的百姓还在议论，可夹廊小院这边的人都听出了更深一层的意思。"

    scene bg fenglei_temple_three_courtyards_day with dissolve

    "风雷观不是普通门派。"

    "它在雷云峰山腰也并非寻常坐北朝南"
    
    "而是依山势坐南朝北。"
    
    "山门朝向北麓官道，背靠南峰雷脉。"
    
    "因此在风雷观内部辨位时，不完全以寻常东南西北称呼"
    
    "而以'向阳侧''近霞侧''外山侧''内山侧'来区分。"

    "雷云峰风雷观依山势分为三院。"

    "主院玄雷院居中偏上，是掌门云清道长居所、藏经阁、议事堂、公共练功场所在，也是全门派早晚课、讲道、议事、演武之地。"

    "男女道众皆在玄雷院参与公共事务。"

    "东院清阳院位于山势向阳一侧，为男道众寮房、兵器库、巡山弟子整备处，负责巡山、护道、传信、兵器管理与外山防务。"

    "鲁天阔早年便曾在清阳院随师修行，是清阳院院主玄岳真人门下的俗家弟子。"

    "后来他入飞鸿驿站做信差队长，仍长期负责传递风雷观与梧天禅院之间的密信。"

    "西院栖霞院位于山势近晚霞一侧，为女道众寮房、丹药房、药材库与炼丹炉所在，平日与茯苓医馆对接草药。"

    "长息定年丹就是在栖霞院丹房炼制，昨夜起火的，也正是栖霞院丹药房。"

    "三兄弟所谓“山脚遇道姑”，根本不是普通迷路。"

    "他们夜里摸到的，很可能是栖霞院外山禁线，甚至靠近了女道众寮房和丹药房所在区域。"

    "擅闯西院、窥探丹房、靠近未收炉的丹息，这才引发了昨日那场怪症。"

    "而现在，封山令没有盖掌门印，却盖了玄雷院急令印。"

    "这说明风雷观内部，绝不只是“丢了一枚丹”那么简单。"

    "李默一直没有说话，这时忽然看向封山令下方。"

    scene bg fengyunping_notice_burn_mark_day with dissolve

    limo "还有一处。"

    "众人顺着他的目光看去。"

    "封山令右下角有一小片焦痕，像是纸张边缘曾被火燎过。"

    "焦痕不大，却很新。"

    "焦痕旁边，还有一条极淡的雷纹，像是被某种气机烙在纸上，不像普通墨痕。"

    "鲁天阔低声说："

    lutiankuo "这是玄雷院急令纸。"

    lutiankuo "只有风雷观内院出事，才会用。"

    "周二蛋吸了一口气。"

    zhouerdan "所以昨晚不是外山小乱？"

    "程明珠看着封山令，语气很冷静。"

    chengmingzhu "外山失守，栖霞院丹房起火，定年丹不见。"

    chengmingzhu "现在又用玄雷院急令印封山。"

    chengmingzhu "若这还叫小乱，那什么才叫大乱？"

    "方大娘低声骂了一句。"

    fangdaniang "这丹真是要人命。"

    "徐春香看着风雷观外门弟子苍白的脸，忽然开口。"

    xuchunxiang "你们掌门呢？"

    "那名外门弟子一僵，低头不答。"

    "鲁天阔上前一步。"

    "他与风雷观有旧，那外门弟子认得他，下意识抬眼，却还是不敢多说。"

    lutiankuo "清阳院玄岳真人可还在山门？"

    "外门弟子低声道："

    fengleiguan_dizi "玄岳真人守清阳院，清骁师兄封外山。"

    fengleiguan_dizi "玄霜真人……在栖霞院。"

    "徐春香追问："

    xuchunxiang "玄霜真人伤了？"

    "外门弟子脸色更白。"

    "他没有回答，只低声说："

    fengleiguan_dizi "山上有令，不许多言。"

    "鲁天阔还要再问，郭路平抬手止住。"

    guoluping "让他回去。他只是传令的。"

    "外门弟子如蒙大赦，向众人拱手，匆匆离开风云坪。"

    scene bg fengyunping_notice_group_orders_day with dissolve

    "魏三儿望着他的背影。"

    weisaner "跑得比昨天那些求丹的还快。"

    "方鹤鸣沉声道："

    fangheming "怕，不一定是坏事。说明他知道自己不能说错话。"

    "徐春香转身看向郭路平。"

    xuchunxiang "夹廊小院不能散。"

    "郭路平点头。"

    guoluping "从现在起，夹廊小院继续守。"

    guoluping "驿站不接上山委托。医馆不放昨日伤者离开。"

    guoluping "所有有关风雷观的消息，先过我们这里。"

    chengmingzhu "医馆前门半闭，急症从夹廊进。"

    chengmingzhu "李默继续守屏风门。药材库上锁。"

    fangheming "驿站这边所有寄往雷云峰、风雷观、梧天禅院的信件单独登记。"

    fangheming "未经郭总管过目，不许发出。"

    zhouerdan "那马厩呢？昨日来镇上的马还没走呢。"

    guoluping "马厩继续收，但不许接上山客。"

    fangdaniang "饭照做。越乱越得吃。空着肚子守不住门。"

    "魏三儿看向你，挤出一点笑。"

    weisaner "听见没？你以后想清闲，怕是不容易了。"

    "你看着告示牌上的封山令，没有说话。"

    scene bg fengyunping_notice_group_orders_day with dissolve

    "昨日自己刚踏入开庵镇时，只知道雷云峰上要炼一枚长息定年丹。"

    "那时它还像一个遥远的江湖传闻。"

    "可现在，驿站住满了，医馆抬进怪症伤者，长风楼谣言四起，侯三闲看见灰衣人夜走镇北小路。"

    "风雷观封山令贴到风云坪，连掌门印都没有出现。"

    "你忽然想起昨日伤者短暂醒来时说的那句话："

    shangzhe "不是丹炉……炉后还有人……"

    "这句话与眼前这纸封山令，像两根线，在你心里轻轻拧到了一起。"

    "封山令贴出后，风云坪的人群久久不散。"

    "有人低声议论。"

    "有人偷偷记下内容。"

    "有人转头往长风楼跑。"

    "有人往西街菜市跑。"

    "有人想去雷云峰方向看看，却被巡捕喝退。"

    "郭路平让魏三儿回驿站盯住来往客人。"

    "徐春香让沈云回医馆看住昨日伤者。"

    "程明珠重新排医馆值守。"

    "方鹤鸣拿出新纸，准备写夹廊小院三日守则。"

    "李默仍站在屏风门旁，目光越过风云坪，看向雷云峰方向。"

    "鲁天阔没有说话，只把昨夜那只被火燎过边角的信筒放在旧木大桌上。"

    scene bg fengyunping_notice_dan_ash_day with dissolve

    "众人准备各自散去时，沈星辰忽然蹲下，从封山令下方的地面捡起一点细小黑灰。"

    "他用指尖捻了捻，神色微变。"

    "魏三儿问："

    weisaner "那是什么？"

    "沈星辰没有立刻回答。"

    "他把那点黑灰放到鼻尖轻轻一嗅，眉头皱起。"

    "徐春香看向他。"

    xuchunxiang "星辰？"

    "沈星辰低声说："

    shenxingchen "不是纸灰。"

    "程明珠问："

    chengmingzhu "不是纸灰，那是什么？"

    "沈星辰抬头，看向雷云峰方向。"

    shenxingchen "像是……丹灰。"

    "众人再次安静下来。"

    "鲁天阔脸色一变。"

    lutiankuo "封山令是从山上带下来的。若上面沾着丹灰……"

    "方鹤鸣接过话，声音压得很低。"

    fangheming "说明写令的人，离栖霞院丹房很近。"

    "郭路平看着那纸封山令，神情沉了下去。"

    "徐春香闭了闭眼，像是在压住某种不好的猜测。"

    scene bg chapter1_ending_leiyunfeng_storm with slow_dissolve

    "远处雷云峰云层低压，天边传来一声闷雷。"

    "你站在夹廊小院门边，第一次真正意识到：自己昨日只是来开庵镇看热闹。"

    "今日却已经被卷进了一个连六大门派都无法轻易收场的局。"

    pause 1.0

    scene black with fade

    $ chapter1_finished = True

    "后续内容仍在制作中。"

    scene bg chapter1_ending_leiyunfeng_storm with dissolve

    "《江湖小镇之凰龙府》目前还只是一个剧情试玩版。"

    "但我想做的，不止是一段故事。"

    "我希望有一天，它能成为一座真正可以行走、探索、结识人物、追查线索的江湖小镇。"

    "如果你是 Unity 开发者、程序、美术、音乐、策划，或对这个世界感兴趣的合作伙伴，欢迎与我联系。"

    if contact_version == "qr":
        scene bg contact_social_qr with dissolve
    else:
        scene bg contact_social_clean with dissolve

    "也可以通过这些平台找到我。"

    "如果你是投资人，或愿意一起推动这个项目继续长大，也欢迎来聊。"

    "【第一章《雷云开炉》结束】"

    "感谢试玩《江湖小镇之凰龙府》第一章。"

    "作者：王子期 Gabriel"

    "微信：h1052588030"

    "邮箱：1052588030@qq.com"

    "若诸位愿意留下几句话，可以告诉我：最喜欢谁，最想查哪条线索，又在哪里看得不明白。"

    "诸位可在小红书、抖音、B站搜索：江湖小镇之凰龙府。"

    "我会在那里继续更新大明国、凰龙府、开庵镇的世界观、人物、剧情与试玩进度。"

    "若想加入玩家交流群，可在任一平台私信，或加我微信时留言：江湖人士。"

    "今日只是开庵镇一隅，明日便可能牵动整座凰龙府。"

    "江湖尚小，仍需诸位添柴。"

    "有缘同路，凰龙府再会。"

    jump chapter1_end

label chapter1_end:

    scene bg chapter1_ending_leiyunfeng_storm with dissolve

    "【系统提示：第一章已完成。建议在此存档。】"

    if protagonist == "wangfang":
        "本次主角：王放"
    elif protagonist == "zuowan":
        "本次主角：左婉"
    else:
        "本次主角：尚未选择"

    if base_place == "feihong_inn":
        "本次落脚地点：飞鸿驿站北耳房"
    elif base_place == "fuling_clinic":
        "本次落脚地点：茯苓医馆南耳房"
    else:
        "本次落脚地点：尚未选择"

    "侯三闲关系值：[hou_sanxian_relation]"

    "[game_display_version]"

    "本版本仍在开发中，部分画面、音乐、文本与系统可能继续调整。"

    return
