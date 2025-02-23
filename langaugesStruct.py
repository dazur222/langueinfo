languages_info = [
    ["Language", "ISO 639-3 Code", "Spoken In", "Characters", "Variations", "Linguistic Roots", "Native Speakers"],
    ["English", "eng", ["USA", "UK", "Canada", "Australia", "New Zealand", "South Africa"], list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), ["British English", "American English", "Australian English"], "Germanic", 377000000],
    ["Spanish", "spa", ["Spain", "Mexico", "Argentina", "Colombia", "Peru", "Chile"], list("ABCDEFGHIJKLMNOPQRSTUVWXYZñ"), ["Castilian Spanish", "Latin American Spanish", "Rioplatense"], "Latin", 460000000],
    ["French", "fra", ["France", "Canada", "Belgium", "Switzerland", "Luxembourg", "Congo"], list("ABCDEFGHIJKLMNOPQRSTUVWXYZéèêëàâîïôûùç"), ["European French", "Canadian French", "African French"], "Latin", 77000000],
    ["Mandarin Chinese", "cmn", ["China", "Taiwan", "Singapore", "Malaysia"], list("的一是不了人我在有他这为之大来以个中上们到说国和地也子时道出而要于就下得可你年生都自会那后能对着事其里所去行过家十用发天如然作方成者多日都小军二次同文主么从无工"), ["Mandarin", "Standard Chinese", "Taiwanese Mandarin"], "Sino-Tibetan", 920000000],
    ["Arabic", "ara", ["Saudi Arabia", "Egypt", "UAE", "Morocco", "Iraq", "Sudan"], list("ابتثجحخدذرزسشصضطظعغفقكلمنهوي"), ["Modern Standard Arabic", "Egyptian Arabic", "Levantine Arabic"], "Semitic", 310000000],
    ["Russian", "rus", ["Russia", "Belarus", "Kazakhstan", "Ukraine"], list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"), ["Standard Russian", "Siberian Russian"], "Slavic", 154000000],
    ["Hindi", "hin", ["India", "Fiji", "Nepal", "Mauritius"], list("अआइईउऊऋएऐओऔकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसह"), ["Standard Hindi", "Bambaiya Hindi"], "Indo-Aryan", 310000000],
    ["Portuguese", "por", ["Portugal", "Brazil", "Angola", "Mozambique", "Cape Verde"], list("ABCDEFGHIJKLMNOPQRSTUVWXYZçãõáéíóúâêô"), ["European Portuguese", "Brazilian Portuguese"], "Latin", 220000000],
    ["Japanese", "jpn", ["Japan"], list("一九七二人入八十千上下中五仁今介他以伊会佐信倉倫兄入光公六共兵具内円冗写冬刀分切刊刑列初判制務南占厚原去参又及友双反収取受口古可台史右司各合吉向君吟告周味呼命和喜善四回因団困囲固国園土在地坂均型城域増士声変夏外多夜夢大天夫失央奥女好子字存宅宇守安完宙宝宮実家容宿寂密富寺小局屋山岡島崇工左市布希平年広府座庭弁引弟形径役往律従復微徳心志応快性恒恩悲悔悟悠惑想愛感成戦戸所手才打投折抜振捕政教文新方日明昔星時春是昼昭昼書最月有服望朝木本村条根株格森標機歌止正武歩歯歴死殿母毎毛気水永求江池沈沖治泉法波泣流浴海深清済温源満準演漢潟潮激濃瀬火灯点無然熱父片物特犬狂獄玉王現球理生産用田町番白百的皆皇皿盛相県真眼着知石破磁示礼社祖神福秀科秘秋移税種積米粉系紅紙絵給続緑線美群義習老考者育般茶落葉著薬行術表規視覚角解言語計記試詩読論谷豆豊赤起超足路身車転軽軍輸述道達選郎遺郡都配重野量銀長門関阪防陽階際難雨雪電青音顔題風食飯館馬駅高鳥黒黄黙鼓"), ["Standard Japanese", "Kansai dialect"], "Japonic", 125000000],
    ["German", "deu", ["Germany", "Austria", "Switzerland", "Belgium", "Liechtenstein"], list("ABCDEFGHIJKLMNOPQRSTUVWXYZßäöü"), ["High German", "Low German", "Swiss German"], "Germanic", 75000000],
    ["Korean", "kor", ["South Korea", "North Korea"], list("ᄀᄂᄃᄅᄆᄇᄉᄋᄌᄎᄏᄐᄑ하ᅢᅣᅥᅦᅧᅭᅮᅳᅴᅵ"), ["Standard Korean", "North Korean dialect", "Jeju dialect"], "Koreanic", 81000000]
]


class Language:
    def __init__(self):
        self.languages_info = [
            ["Language", "ISO 639-3 Code", "Spoken In", "Characters", "Variations", "Linguistic Roots", "Native Speakers"],
            ["English", "eng", ["USA", "UK", "Canada", "Australia", "New Zealand", "South Africa"], list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), ["British English", "American English", "Australian English"], "Germanic", 377000000],
            ["Spanish", "spa", ["Spain", "Mexico", "Argentina", "Colombia", "Peru", "Chile"], list("ABCDEFGHIJKLMNOPQRSTUVWXYZñ"), ["Castilian Spanish", "Latin American Spanish", "Rioplatense"], "Latin", 460000000],
            ["French", "fra", ["France", "Canada", "Belgium", "Switzerland", "Luxembourg", "Congo"], list("ABCDEFGHIJKLMNOPQRSTUVWXYZéèêëàâîïôûùç"), ["European French", "Canadian French", "African French"], "Latin", 77000000],
            ["Mandarin Chinese", "cmn", ["China", "Taiwan", "Singapore", "Malaysia"], list("的一是不了人我在有他这为之大来以个中上们到说国和地也子时道出而要于就下得可你年生都自会那后能对着事其里所去行过家十用发天如然作方成者多日都小军二次同文主么从无工"), ["Mandarin", "Standard Chinese", "Taiwanese Mandarin"], "Sino-Tibetan", 920000000],
            ["Arabic", "ara", ["Saudi Arabia", "Egypt", "UAE", "Morocco", "Iraq", "Sudan"], list("ابتثجحخدذرزسشصضطظعغفقكلمنهوي"), ["Modern Standard Arabic", "Egyptian Arabic", "Levantine Arabic"], "Semitic", 310000000],
            ["Russian", "rus", ["Russia", "Belarus", "Kazakhstan", "Ukraine"], list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"), ["Standard Russian", "Siberian Russian"], "Slavic", 154000000],
            ["Hindi", "hin", ["India", "Fiji", "Nepal", "Mauritius"], list("अआइईउऊऋएऐओऔकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसह"), ["Standard Hindi", "Bambaiya Hindi"], "Indo-Aryan", 310000000],
            ["Portuguese", "por", ["Portugal", "Brazil", "Angola", "Mozambique", "Cape Verde"], list("ABCDEFGHIJKLMNOPQRSTUVWXYZçãõáéíóúâêô"), ["European Portuguese", "Brazilian Portuguese"], "Latin", 220000000],
            ["Japanese", "jpn", ["Japan"], list("一九七二人入八十千上下中五仁今介他以伊会佐信倉倫兄入光公六共兵具内円冗写冬刀分切刊刑列初判制務南占厚原去参又及友双反収取受口古可台史右司各合吉向君吟告周味呼命和喜善四回因団困囲固国園土在地坂均型城域増士声変夏外多夜夢大天夫失央奥女好子字存宅宇守安完宙宝宮実家容宿寂密富寺小局屋山岡島崇工左市布希平年広府座庭弁引弟形径役往律従復微徳心志応快性恒恩悲悔悟悠惑想愛感成戦戸所手才打投折抜振捕政教文新方日明昔星時春是昼昭昼書最月有服望朝木本村条根株格森標機歌止正武歩歯歴死殿母毎毛気水永求江池沈沖治泉法波泣流浴海深清済温源満準演漢潟潮激濃瀬火灯点無然熱父片物特犬狂獄玉王現球理生産用田町番白百的皆皇皿盛相県真眼着知石破磁示礼社祖神福秀科秘秋移税種積米粉系紅紙絵給続緑線美群義習老考者育般茶落葉著薬行術表規視覚角解言語計記試詩読論谷豆豊赤起超足路身車転軽軍輸述道達選郎遺郡都配重野量銀長門関阪防陽階際難雨雪電青音顔題風食飯館馬駅高鳥黒黄黙鼓"), ["Standard Japanese", "Kansai dialect"], "Japonic", 125000000],
            ["German", "deu", ["Germany", "Austria", "Switzerland", "Belgium", "Liechtenstein"], list("ABCDEFGHIJKLMNOPQRSTUVWXYZßäöü"), ["High German", "Low German", "Swiss German"], "Germanic", 75000000],
            ["Korean", "kor", ["South Korea", "North Korea"], list("ᄀᄂᄃᄅᄆᄇᄉᄋᄌᄎᄏᄐᄑ하ᅢᅣᅥᅦᅧᅭᅮᅳᅴᅵ"), ["Standard Korean", "North Korean dialect", "Jeju dialect"], "Koreanic", 81000000]
        ]

    def __str__(self):
        print()

    def get_language_info(self,language):
        lang_info = list()
        for info in languages_info:
            if info[0] == language:
                lang_info = info
        
        return lang_info
    



language = Language()

print(language.get_language_info("Hindi"))

    
