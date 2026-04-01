# ─────────────────────────────────────────────────────────
#  quiz_bank.py  –  Sinhala Commerce Quiz Questions
#  Add / edit questions freely. Keep the same dict structure.
# ─────────────────────────────────────────────────────────

QUIZZES = [

    # ── ගිණුම්කරණය (Accounting) ──────────────────────────
    {
        "id": 1,
        "question": "දෙපැත්ත ගිණුම් ක්‍රමයේ මූලික සමීකරණය කුමක්ද?",
        "options": [
            "වත්කම් = බැරකම් + ප්‍රාග්ධනය",
            "ආදායම = වියදම් + ලාභ",
            "ලාභ = ආදායම - වත්කම්",
            "ප්‍රාග්ධනය = බැරකම් - වත්කම්",
        ],
        "correct_option_id": 0,
        "explanation": "Assets = Liabilities + Capital — මෙය ගිණුම්කරණ සමීකරණයයි.",
    },
    {
        "id": 2,
        "question": "Trial Balance (අත්හදා ශේෂ) සකස් කරන්නේ කුමන අරමුණින්ද?",
        "options": [
            "ලාභ ගණනය කිරීමට",
            "ගිණුම් ගොපිතා නිවැරදිද යන්න සොයා ගැනීමට",
            "ව්‍යාපාරයේ වත්කම් ලැයිස්තු කිරීමට",
            "බදු ගණනය කිරීමට",
        ],
        "correct_option_id": 1,
        "explanation": "Trial Balance මඟින් Debit සහ Credit දෙදෙනාම සමතුලිතද යන්න පරීක්ෂා කෙරේ.",
    },
    {
        "id": 3,
        "question": "Depreciation (ක්ෂයවීම) ගිණුම් ගත කරන්නේ කුමන මූලධර්මය යටතේද?",
        "options": [
            "Revenue Recognition",
            "Matching Principle",
            "Going Concern",
            "Materiality",
        ],
        "correct_option_id": 1,
        "explanation": "Matching Principle — ආදායමට සහ වියදමට අදාල කාල සීමා ගැළපිය යුතුය.",
    },
    {
        "id": 4,
        "question": "Cash Book හි Contra Entry යනු කුමක්ද?",
        "options": [
            "බැංකුවෙන් මුදල් ආපසු ගැනීම",
            "Cash සහ Bank තීරු දෙකෙහිම ඇතුළත් කිරීමක්",
            "ණය ගැනීම",
            "වත්කමක් විකිණීම",
        ],
        "correct_option_id": 1,
        "explanation": "Contra Entry — Cash සහ Bank columns දෙකෙහිම (Debit + Credit) ඇතුළත් වේ.",
    },
    {
        "id": 5,
        "question": "BRS (Bank Reconciliation Statement) හදන ප්‍රධාන හේතුව කුමක්ද?",
        "options": [
            "බදු ගෙවීමට",
            "Cash Book හා Pass Book අතර වෙනස් හේතු සොයා ගැනීමට",
            "ලාභ ගිනි ගැනීමට",
            "නව ගිණුම් ආරම්භ කිරීමට",
        ],
        "correct_option_id": 1,
        "explanation": "BRS — Cash Book Balance සහ Bank Statement Balance සංසන්දනය කොට වෙනස්කම් සොයා ගනී.",
    },

    # ── ව්‍යාපාර අධ්‍යයනය (Business Studies) ────────────
    {
        "id": 6,
        "question": "Sole Proprietorship (තනිකඩ ව්‍යාපාරය) හි ප්‍රධාන අවාසිය කුමක්ද?",
        "options": [
            "ලාභ බෙදා ගැනීම",
            "සීමා රහිත වගකීම",
            "බදු ගෙවීම",
            "ප්‍රාග්ධනය ඉහළ වීම",
        ],
        "correct_option_id": 1,
        "explanation": "Unlimited Liability — හිමිකරු පෞද්ගලික දේපල ද ණය ගෙවීමට ඉදිරිපත් කළ යුතුය.",
    },
    {
        "id": 7,
        "question": "Marketing Mix හි '4P' වලට ඇතුළත් නොවන්නේ?",
        "options": ["Product", "Price", "People", "Place"],
        "correct_option_id": 2,
        "explanation": "4P = Product, Price, Place, Promotion. 'People' 7P හි ඇතුළත් ය, 4P හි නොවේ.",
    },
    {
        "id": 8,
        "question": "GDP (Gross Domestic Product) ගණනය කිරීමේ ද්‍රව්‍ය ක්‍රමය (Expenditure Method) ගණනය ක්‍රමය කුමක්ද?",
        "options": [
            "GDP = C + I + G + (X - M)",
            "GDP = ආදායම + ලාභ",
            "GDP = ස්ථිර වත්කම් + ගෙවුම්",
            "GDP = නිෂ්පාදනය × මිල",
        ],
        "correct_option_id": 0,
        "explanation": "GDP = C (Consumption) + I (Investment) + G (Government) + Net Exports.",
    },
    {
        "id": 9,
        "question": "Partnership (හවුල් ව්‍යාපාරය) ක්‍රියාත්මක කළ හැකි උපරිම සාමාජිකයින් ගණන කීයද?",
        "options": ["10", "20", "50", "100"],
        "correct_option_id": 1,
        "explanation": "සාමාන්‍ය හවුල් ව්‍යාපාරවල සාමාජිකයින් 20 දක්වා සීමා කෙරේ (බැංකු 10 ද).",
    },
    {
        "id": 10,
        "question": "Consumer Protection Act ශ්‍රී ලංකාවේ කල්‍යාණය ආරක්ෂා කරන ගනුදෙනුකරුවන් ආයතනය කොයිද?",
        "options": ["SLTB", "CAA", "SEC", "BOI"],
        "correct_option_id": 1,
        "explanation": "CAA — Consumer Affairs Authority ශ්‍රී ලංකාවේ පාරිභෝගිකයින් ආරක්ෂා කරයි.",
    },

    # ── ආර්ථික විද්‍යාව (Economics) ─────────────────────
    {
        "id": 11,
        "question": "ඉල්ලුම් නියමය (Law of Demand) පවසන්නේ කුමක්ද?",
        "options": [
            "මිල ඉහළ යත්ම ඉල්ලුම ද ඉහළ යයි",
            "මිල ඉහළ යත්ම ඉල්ලුම අඩු වෙයි",
            "ඉල්ලුම සහ සැපයුම සෑම විටම සමානය",
            "ආදායම ඉහළ යත්ම ඉල්ලුම අඩු වෙයි",
        ],
        "correct_option_id": 1,
        "explanation": "Law of Demand: Price ↑ → Quantity Demanded ↓ (inverse relationship).",
    },
    {
        "id": 12,
        "question": "Inflation (උද්ධමනය) මනිනු ලබන ශ්‍රී ලංකා ප්‍රධාන දර්ශකය කුමක්ද?",
        "options": ["GDP Deflator", "CCPI", "WPI", "PPI"],
        "correct_option_id": 1,
        "explanation": "CCPI — Colombo Consumer Price Index ශ්‍රී ලංකාවේ ප්‍රධාන උද්ධමන දර්ශකයයි.",
    },
    {
        "id": 13,
        "question": "Opportunity Cost (අවස්ථා වියදම) යනු කුමක්ද?",
        "options": [
            "ව්‍යාපාරයේ ඇති සම්පූර්ණ වියදම",
            "විකල්ප තේරීමකින් අත්හැරෙන හොඳම ප්‍රතිලාභය",
            "ලාභ ප්‍රමාණය",
            "නිෂ්පාදන වියදම",
        ],
        "correct_option_id": 1,
        "explanation": "Opportunity Cost = Next best alternative foregone — ආර්ථික විද්‍යාවේ ප්‍රධාන සංකල්පය.",
    },
    {
        "id": 14,
        "question": "Perfect Competition (සම්පූර්ණ තරගකාරිත්වය) හි ලක්ෂණයක් නොවන්නේ?",
        "options": [
            "ගැනුම්කරුවන් සහ විකුණුම්කරුවන් බොහෝ",
            "ඒකජාතික නිෂ්පාදන",
            "Price Maker",
            "නිදහස් ප්‍රවේශය",
        ],
        "correct_option_id": 2,
        "explanation": "Perfect Competition හි firms Price Takers. Price Makers වන්නේ Monopoly හිදී.",
    },
    {
        "id": 15,
        "question": "ශ්‍රී ලංකාවේ මධ්‍යම බැංකුව (Central Bank) ස්ථාපිත වූ වර්ෂය?",
        "options": ["1948", "1950", "1956", "1960"],
        "correct_option_id": 1,
        "explanation": "Central Bank of Sri Lanka 1950 අගෝස්තු 28 දින ස්ථාපිත විය.",
    },

    # ── Additional mixed questions ────────────────────────
    {
        "id": 16,
        "question": "Fixed Cost (ස්ථාවර වියදම) ලක්ෂණය කුමක්ද?",
        "options": [
            "නිෂ්පාදනය සමඟ වෙනස් වෙයි",
            "නිෂ්පාදනය කොයිතරම් වුණත් නොවෙනස්ව පවතී",
            "ශ්‍රමිකයින් ගෙවීම",
            "අමු ද්‍රව්‍ය වියදම",
        ],
        "correct_option_id": 1,
        "explanation": "Fixed Costs (කුලිය, රක්ෂණය) නිෂ්පාදන ප්‍රමාණය කෙසේ වෙතත් නොවෙනස්ව පවතී.",
    },
    {
        "id": 17,
        "question": "Balance of Trade (වෙළඳ ශේෂය) ලැබෙන්නේ කෙසේද?",
        "options": [
            "ආනයන - අපනයන",
            "අපනයන - ආනයන",
            "GDP - GNP",
            "ආදායම - වියදම",
        ],
        "correct_option_id": 1,
        "explanation": "Balance of Trade = Exports − Imports. Positive = Surplus, Negative = Deficit.",
    },
    {
        "id": 18,
        "question": "Debit Note (ඩෙබිට් සටහන) යවන්නේ කවුරුන්ද?",
        "options": ["විකුණුම්කරු", "ගැනුම්කරු", "බැංකුව", "රජය"],
        "correct_option_id": 1,
        "explanation": "Debit Note යවන්නේ ගැනුම්කරු (Buyer) — ආපසු ලබාදෙන භාණ්ඩ සඳහා.",
    },
    {
        "id": 19,
        "question": "Petty Cash Book ආරම්භ කළ හැකි ක්‍රමය?",
        "options": [
            "Simple System",
            "Imprest System",
            "Double Entry System",
            "Single Entry System",
        ],
        "correct_option_id": 1,
        "explanation": "Imprest System — ස්ථාවර මුදලක් (float) ආරම්භයේ ලබා, කාල සීමා අවසානයේ නැවත සම්පූර්ণ කෙරේ.",
    },
    {
        "id": 20,
        "question": "Fiscal Policy (මූල්‍ය ප්‍රතිපත්තිය) ක්‍රියාත්මක කරන ආයතනය?",
        "options": [
            "මධ්‍යම බැංකුව",
            "රජය (Ministry of Finance)",
            "IMF",
            "World Bank",
        ],
        "correct_option_id": 1,
        "explanation": "Fiscal Policy — රජය මගින් බදු හා රාජ්‍ය වියදම් හරහා ක්‍රියාත්මක කෙරේ.",
    },
]
