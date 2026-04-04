# ─────────────────────────────────────────────────────────
#  quiz_bank.py  –  Sinhala Commerce Quiz Questions
#  Add / edit questions freely. Keep the same dict structure.
# ─────────────────────────────────────────────────────────

QUIZZES = [

    # Bs
[
{"id":1,"question":"ව්‍යාපාරය යනු කුමක්ද?","options":["විනෝදාස්වාද ක්‍රියාකාරකම්","ලාභය සඳහා භාණ්ඩ හා සේවා නිෂ්පාදනය සහ විකිණීම","රජයේ සේවාව","ආගමික කටයුතු"],"correct_option_id":1,"explanation":"Business = production & selling for profit."},
{"id":2,"question":"ව්‍යාපාරයේ ප්‍රධාන අරමුණ කුමක්ද?","options":["ලාභ උපයා ගැනීම","වියදම් වැඩි කිරීම","සේවකයින් අඩු කිරීම","රජයට උදව් කිරීම"],"correct_option_id":0,"explanation":"Main goal is profit."},
{"id":3,"question":"ප්‍රාථමික කර්මාන්තය යනු?","options":["සේවා සැපයීම","නිෂ්පාදනය","ස්වභාවික සම්පත් ලබාගැනීම","වෙළඳාම"],"correct_option_id":2,"explanation":"Primary = extraction."},
{"id":4,"question":"ද්විතියික කර්මාන්තය කුමක්ද?","options":["සේවා","අමුද්‍රව්‍ය සැකසීම","වෙළඳාම","ගොවිතැන"],"correct_option_id":1,"explanation":"Secondary = processing."},
{"id":5,"question":"තෘතීයික කර්මාන්තය කුමක්ද?","options":["කැණීම","නිෂ්පාදනය","සේවා","ගොවිතැන"],"correct_option_id":2,"explanation":"Tertiary = services."},

{"id":6,"question":"ව්‍යාපාරයේ ලක්ෂණයක් නොවන්නේ කුමක්ද?","options":["ලාභය","අවදානම","ආර්ථික ක්‍රියාකාරකම්","නොමිලේ සේවා"],"correct_option_id":3,"explanation":"Business is profit-oriented."},
{"id":7,"question":"වාණිජ්‍යය යනු?","options":["නිෂ්පාදනය","බෙදාහැරීම","ගොවිතැන","පතල්"],"correct_option_id":1,"explanation":"Commerce = distribution."},
{"id":8,"question":"බැංකුකරණය අයත් වන්නේ?","options":["කර්මාන්තයට","වාණිජ්‍යයට","ගොවිතැනට","නිෂ්පාදනයට"],"correct_option_id":1,"explanation":"Banking = commerce support."},
{"id":9,"question":"ව්‍යාපාරයේ භූමිකාවක් කුමක්ද?","options":["රැකියා අඩු කිරීම","රැකියා නිර්මාණය","බදු වැඩි කිරීම","ආදායම අඩු කිරීම"],"correct_option_id":1,"explanation":"Business creates jobs."},
{"id":10,"question":"GDP යනු?","options":["ජාතික ආදායම","දේශීය නිෂ්පාදනය","ජනගහනය","බදු"],"correct_option_id":1,"explanation":"GDP = total production."},

{"id":11,"question":"ව්‍යාපාරිකයෙකුගේ ලක්ෂණයක්?","options":["අසාර්ථක තීරණ","දැක්ම","අලසකම","භීතිය"],"correct_option_id":1,"explanation":"Vision is key."},
{"id":12,"question":"තීරණ ගැනීමේ හැකියාව කාට වැදගත්ද?","options":["සිසුන්ට පමණි","ව්‍යාපාරිකයාට","ගොවියන්ට","රජයට"],"correct_option_id":1,"explanation":"Entrepreneurs need decisions."},
{"id":13,"question":"සන්නිවේදනයේ වැදගත්කම?","options":["අඩුයි","වැදගත්","අවශ්‍ය නැහැ","වියදම් වැඩි කරයි"],"correct_option_id":1,"explanation":"Communication = success."},
{"id":14,"question":"නවෝත්පාදනය යනු?","options":["පරණ ක්‍රම","නව අදහස්","වියදම්","බදු"],"correct_option_id":1,"explanation":"Innovation = new ideas."},
{"id":15,"question":"අවදානම් කළමනාකරණය යනු?","options":["අවදානම් නොගැනීම","අවදානම් හඳුනා ගැනීම","ලාභය අඩු කිරීම","වැඩ නවත්වීම"],"correct_option_id":1,"explanation":"Manage risks properly."},

{"id":16,"question":"තනි හිමිකාරීත්වයේ හිමිකරු කවුද?","options":["පුද්ගල 1ක්","2ක්","සමාගමක්","රජය"],"correct_option_id":0,"explanation":"Single owner."},
{"id":17,"question":"තනි හිමිකාරීත්වයේ වගකීම්?","options":["සීමිත","අසීමිත","නැත","අර්ධ"],"correct_option_id":1,"explanation":"Unlimited liability."},
{"id":18,"question":"ලාභය කාටද?","options":["රජයට","හවුල්කරුවන්ට","හිමිකරුට","බැංකුවට"],"correct_option_id":2,"explanation":"Owner keeps profit."},
{"id":19,"question":"හවුල්කාරිත්වය යනු?","options":["1 පුද්ගල","2+ පුද්ගල","සමාගමක්","රජය"],"correct_option_id":1,"explanation":"Partnership = 2+ people."},
{"id":20,"question":"ලාභ බෙදාගැනීම කෙසේද?","options":["අහඹු","ගිවිසුම අනුව","රජය අනුව","පාරිභෝගික අනුව"],"correct_option_id":1,"explanation":"Agreement based."},

{"id":21,"question":"සමාගමක් යනු?","options":["පුද්ගලයෙක්","වෙනම නෛතික ආයතනයක්","ගොවිපල","දේවාලයක්"],"correct_option_id":1,"explanation":"Company = legal entity."},
{"id":22,"question":"සමාගමේ වාසියක්?","options":["අසීමිත වගකීම්","සීමිත වගකීම්","ලාභ නැත","පාලනය නැත"],"correct_option_id":1,"explanation":"Limited liability."},
{"id":23,"question":"Public company එකේ කොටස්?","options":["විකුණන්න බැහැ","වෙළඳාම් කළ හැක","රජයට පමණි","අහඹු"],"correct_option_id":1,"explanation":"Shares tradable."},
{"id":24,"question":"Private company?","options":["සියල්ලට විවෘත","සීමිත කොටස් හිමියන්","රජය සතු","නොමැත"],"correct_option_id":1,"explanation":"Limited shareholders."},
{"id":25,"question":"සමුපකාරයේ අරමුණ?","options":["ලාභ","සාමාජික සුභසාධනය","බදු","වෙළඳාම"],"correct_option_id":1,"explanation":"Member welfare."},

{"id":26,"question":"සමුපකාරයේ ඡන්ද අයිතිය?","options":["අසමාන","සමාන","රජයට","නායකයාට"],"correct_option_id":1,"explanation":"Equal voting."},
{"id":27,"question":"Franchising යනු?","options":["නව ආකෘතිය","වෙළඳ නාමය යටතේ ව්‍යාපාරය","ගොවිතැන","බදු"],"correct_option_id":1,"explanation":"Use brand model."},
{"id":28,"question":"E-commerce යනු?","options":["දුරකථන වෙළඳාම","Online වෙළඳාම","ගොවිතැන","බැංකු"],"correct_option_id":1,"explanation":"Online business."},
{"id":29,"question":"Business environment යනු?","options":["ව්‍යාපාරය පමණි","අභ්‍යන්තර + බාහිර සාධක","ලාභ","වියදම්"],"correct_option_id":1,"explanation":"All factors affecting business."},
{"id":30,"question":"අභ්‍යන්තර පරිසරය?","options":["ගනුදෙනුකරුවන්","සේවකයින්","රජය","බදු"],"correct_option_id":1,"explanation":"Internal factors."},

{"id":31,"question":"බාහිර පරිසරය?","options":["සේවකයින්","සමාගම් සංස්කෘතිය","ගනුදෙනුකරුවන්","අභ්‍යන්තර ප්‍රතිපත්ති"],"correct_option_id":2,"explanation":"External factors."},
{"id":32,"question":"ක්ෂුද්‍ර පරිසරය?","options":["ගෝලීය","ක්ෂණික සාධක","පරණ","නීති"],"correct_option_id":1,"explanation":"Micro = immediate."},
{"id":33,"question":"මැක්‍රෝ පරිසරය?","options":["පුළුල් සාධක","සේවකයින්","ගනුදෙනුකරුවන්","අභ්‍යන්තර"],"correct_option_id":0,"explanation":"Macro = broad."},
{"id":34,"question":"ආර්ථික පරිසරයේ සාධකයක්?","options":["සංස්කෘතිය","උද්ධමනය","නීති","තාක්ෂණය"],"correct_option_id":1,"explanation":"Inflation."},
{"id":35,"question":"දේශපාලන පරිසරය?","options":["රජයේ ප්‍රතිපත්ති","තාක්ෂණය","සංස්කෘතිය","වෙළඳාම"],"correct_option_id":0,"explanation":"Government policies."},

{"id":36,"question":"සමාජ පරිසරය?","options":["ආර්ථිකය","සංස්කෘතිය","තාක්ෂණය","නීති"],"correct_option_id":1,"explanation":"Culture & values."},
{"id":37,"question":"තාක්ෂණික පරිසරය?","options":["නවෝත්පාදන","බදු","රජය","වියදම්"],"correct_option_id":0,"explanation":"Innovation."},
{"id":38,"question":"නීතිමය පරිසරය?","options":["සංස්කෘතිය","නීති","ගොවිතැන","තාක්ෂණය"],"correct_option_id":1,"explanation":"Laws."},
{"id":39,"question":"ගෝලීයකරණය යනු?","options":["දේශීය වෙළඳාම","ලෝක ඒකාබද්ධ වීම","ගොවිතැන","බදු"],"correct_option_id":1,"explanation":"Global integration."},
{"id":40,"question":"ගෝලීයකරණයේ ප්‍රතිලාභයක්?","options":["වෙළඳපොළ අඩුවීම","වෙළඳපොළ වැඩි වීම","තාක්ෂණය අඩු","තරඟ අඩු"],"correct_option_id":1,"explanation":"More markets."},
    
]

