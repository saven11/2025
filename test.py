import streamlit as st

st.set_page_config(page_title="그리스 로마 신화 도감", layout="wide")

# 신 데이터
gods = {
    "Zeus 제우스 ⚡": {
        "성격": "권위적이고 정의로우며 때때로 충동적임",
        "설화": "티탄을 무찌르고 올림포스의 주신이 됨",
        "관계": "형제는 포세이돈, 하데스, 아내는 헤라",
        "color": "#FFD700"  # 금색
    },
    "Hera 헤라 👑": {
        "성격": "질투심이 강하지만 결혼과 가정을 중시함",
        "설화": "제우스와의 갈등과 신들의 여왕으로서의 위상",
        "관계": "남편은 제우스, 아들 아레스와 헤파이스토스의 어머니",
        "color": "#DA70D6"  # 보라
    },
    "Poseidon 포세이돈 🌊": {
        "성격": "격정적이고 집요함",
        "설화": "바다의 지배자로서 트로이아 전쟁에 개입",
        "관계": "형제는 제우스와 하데스",
        "color": "#1E90FF"  # 파랑
    },
    "Hades 하데스 💀": {
        "성격": "엄격하고 차갑지만 규칙을 중시함",
        "설화": "페르세포네를 납치하여 명계의 여왕으로 삼음",
        "관계": "형제는 제우스와 포세이돈, 아내는 페르세포네",
        "color": "#2F4F4F"  # 짙은 회색
    },
    "Athena 아테나 🦉": {
        "성격": "지혜롭고 침착하며 정의를 추구함",
        "설화": "제우스의 머리에서 무장한 채 태어남",
        "관계": "아버지는 제우스",
        "color": "#708090"  # 슬레이트 그레이
    },
    "Apollo 아폴론 🎵": {
        "성격": "예술적이고 이성적임",
        "설화": "피톤을 물리치고 델포이 신탁의 주인이 됨",
        "관계": "쌍둥이 여동생은 아르테미스",
        "color": "#FFA500"  # 주황
    },
    "Artemis 아르테미스 🏹": {
        "성격": "자유롭고 사냥을 사랑하며 순결을 중시함",
        "설화": "사냥의 여신으로 오리온과 관련된 이야기",
        "관계": "쌍둥이 오빠는 아폴론",
        "color": "#32CD32"  # 라임그린
    },
    "Ares 아레스 ⚔️": {
        "성격": "호전적이고 충동적임",
        "설화": "트로이아 전쟁에서 여러 차례 패배함",
        "관계": "부모는 제우스와 헤라",
        "color": "#B22222"  # 불타는 빨강
    },
    "Aphrodite 아프로디테 🌹": {
        "성격": "매혹적이고 감정에 충실함",
        "설화": "바다의 거품에서 태어나 아름다움의 여신이 됨",
        "관계": "남편은 헤파이스토스, 연인은 아레스",
        "color": "#FF69B4"  # 핑크
    },
    "Hermes 헤르메스 🪶": {
        "성격": "영리하고 장난기 많으며 신속함",
        "설화": "태어난 지 하루 만에 아폴론의 가축을 훔침",
        "관계": "아버지는 제우스, 어머니는 마이아",
        "color": "#00CED1"  # 터키석
    },
    "Hephaestus 헤파이스토스 🔨": {
        "성격": "끈기 있고 성실하며 예술적 재능이 뛰어남",
        "설화": "올림포스에서 떨어졌으나 불과 대장장이의 신이 됨",
        "관계": "어머니는 헤라, 아내는 아프로디테",
        "color": "#A0522D"  # 갈색
    },
    "Dionysus 디오니소스 🍇": {
        "성격": "쾌활하고 창의적이며 때때로 광기에 휩싸임",
        "설화": "포도주와 축제의 신으로 그리스 전역에서 숭배받음",
        "관계": "아버지는 제우스, 어머니는 세멜레",
        "color": "#800080"  # 보라
    }
}

st.title("✨ 그리스 로마 신화 도감 ✨")
st.markdown("가로 스크롤로 다양한 신들을 탐험해보세요!")

# 가로 스크롤 컨테이너
st.markdown(
    """
    <style>
    .scroll-container {
        display: flex;
        overflow-x: auto;
        padding: 20px 0;
    }
    .card {
        flex: 0 0 auto;
        width: 280px;
        margin-right: 20px;
        padding: 20px;
        border-radius: 20px;
        color: white;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        backdrop-filter: blur(6px);
        font-family: 'Arial', sans-serif;
    }
    .card h3 {
        margin-top: 0;
        font-size: 22px;
    }
    .card p {
        font-size: 14px;
        line-height: 1.4;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 카드 출력
cards_html = '<div class="scroll-container">'
for name, info in gods.items():
    cards_html += f"""
    <div class="card" style="background-color: {info['color']}CC;">
        <h3>{name}</h3>
        <p><b>성격:</b> {info['성격']}</p>
        <p><b>설화:</b> {info['설화']}</p>
        <p><b>관계:</b> {info['관계']}</p>
    </div>
    """
cards_html += "</div>"

st.markdown(cards_html, unsafe_allow_html=True)
