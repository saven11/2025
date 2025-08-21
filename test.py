import streamlit as st

st.set_page_config(page_title="그리스 로마 신화", layout="wide")

# 전체 신 데이터
gods = [
    {"emoji":"⚡","en":"Zeus","kr":"제우스","desc":"올림포스 최고신, 하늘과 천둥의 신","story":"티탄을 무찌르고 올림포스의 주신이 됨","relation":"포세이돈과 하데스의 형제, 헤라의 남편","color":"#FFD700","border_left":"🦅","border_right":"🌩️"},
    {"emoji":"🌊","en":"Poseidon","kr":"포세이돈","desc":"바다와 지진의 신","story":"삼지창으로 땅과 바다를 지배함","relation":"제우스와 하데스의 형제","color":"#1E90FF","border_left":"🐬","border_right":"🌊"},
    {"emoji":"💀","en":"Hades","kr":"하데스","desc":"저승과 죽음의 신","story":"페르세포네를 아내로 맞아 저승의 왕이 됨","relation":"제우스와 포세이돈의 형제","color":"#2F4F4F","border_left":"🪦","border_right":"👻"},
    {"emoji":"👑","en":"Hera","kr":"헤라","desc":"결혼과 가정의 여신","story":"제우스의 아내로 여신들의 여왕","relation":"제우스의 아내, 아레스와 헤파이스토스의 어머니","color":"#FF69B4","border_left":"🦚","border_right":"💍"},
    {"emoji":"🦉","en":"Athena","kr":"아테나","desc":"지혜와 전쟁 전략의 여신","story":"제우스의 머리에서 갑옷을 입고 태어남","relation":"제우스의 딸","color":"#708090","border_left":"🛡️","border_right":"⚔️"},
    {"emoji":"🎶","en":"Apollo","kr":"아폴론","desc":"태양, 음악과 예언의 신","story":"델포이 신탁의 주신으로 예언을 전함","relation":"아르테미스의 쌍둥이 오빠","color":"#FFA500","border_left":"☀️","border_right":"🎵"},
    {"emoji":"🏹","en":"Artemis","kr":"아르테미스","desc":"달과 사냥의 여신","story":"숲과 동물을 지키는 수호자","relation":"아폴론의 쌍둥이 여동생","color":"#87CEFA","border_left":"🌙","border_right":"🦌"},
    {"emoji":"🛠️","en":"Hephaestus","kr":"헤파이스토스","desc":"불과 대장장이의 신","story":"올림포스의 무기와 갑옷을 만든 장인","relation":"헤라의 아들, 아프로디테의 남편","color":"#A0522D","border_left":"🔥","border_right":"🔨"},
    {"emoji":"🍷","en":"Dionysus","kr":"디오니소스","desc":"술과 축제의 신","story":"인간들에게 포도주와 환희를 전함","relation":"제우스의 아들","color":"#800080","border_left":"🍇","border_right":"🥂"},
    {"emoji":"🕊️","en":"Hermes","kr":"헤르메스","desc":"상인, 여행자, 전령의 신","story":"신들의 전령으로 빠른 날개 달린 신발을 가짐","relation":"제우스의 아들","color":"#32CD32","border_left":"👟","border_right":"📨"},
    {"emoji":"🌹","en":"Aphrodite","kr":"아프로디테","desc":"사랑과 아름다움의 여신","story":"바다의 거품에서 태어나 신과 인간을 매혹함","relation":"헤파이스토스의 아내, 에로스의 어머니","color":"#FFB6C1","border_left":"💘","border_right":"🌸"},
    {"emoji":"🗡️","en":"Ares","kr":"아레스","desc":"전쟁의 신","story":"아프로디테와의 사랑 이야기로 유명함","relation":"제우스와 헤라의 아들","color":"#DC143C","border_left":"⚔️","border_right":"🛡️"}
]

st.title("🏛️ 올림포스 신 카드")

# CSS 스타일
st.markdown("""
<style>
.scroll-container {
    display: flex;
    justify-content: center;
    overflow-x: auto;
    padding: 2rem 0;
}
.card {
    flex: 0 0 350px;
    margin: 0 1rem;
    padding: 1.5rem;
    border-radius: 15px;
    color: white;
    box-shadow: 2px 2px 16px rgba(0,0,0,0.4);
    position: relative;
    min-height: 250px;
}
.card::before {
    position: absolute;
    left: -30px;
    top: 50%;
    transform: translateY(-50%);
    font-size: 28px;
}
.card::after {
    position: absolute;
    right: -30px;
    top: 50%;
    transform: translateY(-50%);
    font-size: 28px;
}
.card h3 { margin-top:0; margin-bottom:0.8rem; font-size:1.4rem;}
.card p { margin:0.4rem 0; font-size:1rem;}
</style>
""", unsafe_allow_html=True)

# 카드 출력
cards_html = '<div class="scroll-container">'
for god in gods:
    cards_html += f"""
    <div class="card" style="background-color:{god['color']}">
        <style>
            .card::before {{ content: "{god['border_left']}"; }}
            .card::after {{ content: "{god['border_right']}"; }}
        </style>
        <h3>{god['emoji']} {god['en']} {god['kr']}</h3>
        <p><b>설명:</b> {god['desc']}</p>
        <p><b>설화:</b> {god['story']}</p>
        <p><b>관계:</b> {god['relation']}</p>
    </div>
    """
cards_html += '</div>'

st.markdown(cards_html, unsafe_allow_html=True)
