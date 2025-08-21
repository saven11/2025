import streamlit as st

st.set_page_config(page_title="그리스 로마 신화", layout="wide")

# 신 데이터
gods = [
    {
        "emoji": "⚡",
        "en": "Zeus",
        "kr": "제우스",
        "desc": "올림포스 최고신, 하늘과 천둥의 신",
        "story": "티탄을 무찌르고 올림포스의 주신이 됨",
        "relation": "포세이돈과 하데스의 형제, 헤라의 남편",
        "color": "#FFD700",
        "border_left": "🦅",
        "border_right": "🌩️"
    },
    {
        "emoji": "🌊",
        "en": "Poseidon",
        "kr": "포세이돈",
        "desc": "바다와 지진의 신",
        "story": "삼지창으로 땅과 바다를 지배함",
        "relation": "제우스와 하데스의 형제",
        "color": "#1E90FF",
        "border_left": "🐬",
        "border_right": "🌊"
    },
    {
        "emoji": "💀",
        "en": "Hades",
        "kr": "하데스",
        "desc": "저승과 죽음의 신",
        "story": "페르세포네를 아내로 맞아 저승의 왕이 됨",
        "relation": "제우스와 포세이돈의 형제",
        "color": "#2F4F4F",
        "border_left": "🪦",
        "border_right": "👻"
    },
    {
        "emoji": "👑",
        "en": "Hera",
        "kr": "헤라",
        "desc": "결혼과 가정의 여신",
        "story": "제우스의 아내로 여신들의 여왕",
        "relation": "제우스의 아내, 아레스와 헤파이스토스의 어머니",
        "color": "#FF69B4",
        "border_left": "🦚",
        "border_right": "💍"
    },
    {
        "emoji": "🦉",
        "en": "Athena",
        "kr": "아테나",
        "desc": "지혜와 전쟁 전략의 여신",
        "story": "제우스의 머리에서 갑옷을 입고 태어남",
        "relation": "제우스의 딸",
        "color": "#708090",
        "border_left": "🛡️",
        "border_right": "⚔️"
    },
    {
        "emoji": "🎶",
        "en": "Apollo",
        "kr": "아폴론",
        "desc": "태양, 음악과 예언의 신",
        "story": "델포이 신탁의 주신으로 예언을 전함",
        "relation": "아르테미스의 쌍둥이 오빠",
        "color": "#FFA500",
        "border_left": "☀️",
        "border_right": "🎵"
    },
    {
        "emoji": "🏹",
        "en": "Artemis",
        "kr": "아르테미스",
        "desc": "달과 사냥의 여신",
        "story": "숲과 동물을 지키는 수호자",
        "relation": "아폴론의 쌍둥이 여동생",
        "color": "#87CEFA",
        "border_left": "🌙",
        "border_right": "🦌"
    },
    {
        "emoji": "🛠️",
        "en": "Hephaestus",
        "kr": "헤파이스토스",
        "desc": "불과 대장장이의 신",
        "story": "올림포스의 무기와 갑옷을 만든 장인",
        "relation": "헤라의 아들, 아프로디테의 남편",
        "color": "#A0522D",
        "border_left": "🔥",
        "border_right": "🔨"
    },
    {
        "emoji": "🍷",
        "en": "Dionysus",
        "kr": "디오니소스",
        "desc": "술과 축제의 신",
        "story": "인간들에게 포도주와 환희를 전함",
        "relation": "제우스의 아들",
        "color": "#800080",
        "border_left": "🍇",
        "border_right": "🥂"
    },
    {
        "emoji": "🕊️",
        "en": "Hermes",
        "kr": "헤르메스",
        "desc": "상인, 여행자, 전령의 신",
        "story": "신들의 전령으로 빠른 날개 달린 신발을 가짐",
        "relation": "제우스의 아들",
        "color": "#32CD32",
        "border_left": "👟",
        "border_right": "📨"
    }
]

st.title("🏛️ 그리스 로마 신화 인물 카드")

# 신 선택
selected = st.selectbox("신을 선택하세요", [f"{g['en']} {g['kr']}" for g in gods])

# 선택한 신 데이터 가져오기
god = next(item for item in gods if f"{item['en']} {item['kr']}" == selected)

# CSS + 카드 출력
st.markdown(f"""
<style>
.scroll-container {{
    display: flex;
    justify-content: center;  /* 가운데 정렬 */
    overflow-x: auto;
    padding: 2rem 0;
}}

.card {{
    flex: 0 0 450px;  /* 카드 너비 확대 */
    margin-right: 1.5rem;
    padding: 2rem;   /* 내부 여백 확대 */
    border-radius: 15px;
    background-color: {god['color']};
    color: white;
    box-shadow: 2px 2px 16px rgba(0,0,0,0.4);
    position: relative;
    min-height: 300px;  /* 높이 확대 */
}}

.card::before {{
    content: "{god['border_left']}";
    position: absolute;
    left: -30px;
    top: 50%;
    transform: translateY(-50%);
    font-size: 28px;
}}
.card::after {{
    content: "{god['border_right']}";
    position: absolute;
    right: -30px;
    top: 50%;
    transform: translateY(-50%);
    font-size: 28px;
}}
.card h3 {{
    margin-top: 0;
    margin-bottom: 0.8rem;
    font-size: 1.6rem;  /* 제목 글씨 키움 */
}}
.card p {{
    margin: 0.5rem 0;
    font-size: 1.1rem;  /* 본문 글씨 키움 */
}}
</style>

<div class="scroll-container">
    <div class="card">
        <h3>{god['emoji']} {god['en']} {god['kr']}</h3>
        <p><b>설명:</b> {god['desc']}</p>
        <p><b>설화:</b> {god['story']}</p>
        <p><b>관계:</b> {god['relation']}</p>
    </div>
</div>
""", unsafe_allow_html=True)
