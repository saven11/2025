import streamlit as st

# 데이터 정의
gods = {
    "제우스": {
        "emoji": "⚡",
        "english": "Zeus",
        "description": "하늘과 번개의 신, 올림포스의 최고신",
        "personality": "위엄 있고 권위적이며 정의를 중시하는 성격",
        "myth": "티타노마키아에서 승리하여 올림포스의 지배자가 된 설화",
        "relations": "헤라의 남편, 아테나의 아버지, 아폴론과 아르테미스의 아버지"
    },
    "헤라": {
        "emoji": "👑",
        "english": "Hera",
        "description": "결혼과 가정의 여신",
        "personality": "자존심이 강하고 질투심이 많은 성격",
        "myth": "트로이 전쟁의 원인이 된 파리스의 심판 설화",
        "relations": "제우스의 아내, 아레스와 헤파이스토스의 어머니"
    },
    "포세이돈": {
        "emoji": "🌊",
        "english": "Poseidon",
        "description": "바다와 지진의 신",
        "personality": "거칠고 충동적이며 강력한 힘을 지닌 성격",
        "myth": "아테네의 수호신 자리를 두고 아테나와 겨룬 설화",
        "relations": "제우스와 하데스의 형제, 트리톤의 아버지"
    },
    "하데스": {
        "emoji": "💀",
        "english": "Hades",
        "description": "저승과 죽음의 신",
        "personality": "엄격하고 냉정하며 고독한 성격",
        "myth": "페르세포네를 납치하여 저승의 여왕으로 삼은 설화",
        "relations": "제우스와 포세이돈의 형제, 페르세포네의 남편"
    },
    "아테나": {
        "emoji": "🦉",
        "english": "Athena",
        "description": "지혜와 전쟁, 전략의 여신",
        "personality": "이성적이고 침착하며 현명한 성격",
        "myth": "제우스의 머리에서 완전무장한 모습으로 태어난 설화",
        "relations": "제우스의 딸, 아폴론과 아르테미스와의 협력 관계"
    },
    "아폴론": {
        "emoji": "🎶",
        "english": "Apollo",
        "description": "음악, 예언, 태양의 신",
        "personality": "밝고 조화로우며 예술적 성향을 가진 성격",
        "myth": "델피 신탁을 통해 예언을 전한 설화",
        "relations": "제우스와 레토의 아들, 아르테미스의 쌍둥이 오빠"
    },
    "아르테미스": {
        "emoji": "🏹",
        "english": "Artemis",
        "description": "사냥과 달의 여신",
        "personality": "자유롭고 강인하며 순결을 지키는 성격",
        "myth": "악타이온을 사슴으로 만들어 죽게 한 설화",
        "relations": "제우스와 레토의 딸, 아폴론의 쌍둥이 여동생"
    },
    "아프로디테": {
        "emoji": "🌹",
        "english": "Aphrodite",
        "description": "사랑과 미의 여신",
        "personality": "매혹적이고 감각적이며 변덕스러운 성격",
        "myth": "바다의 거품에서 태어난 설화",
        "relations": "헤파이스토스의 아내, 에로스의 어머니"
    },
    "헤르메스": {
        "emoji": "🪽",
        "english": "Hermes",
        "description": "상업, 여행, 도둑, 신들의 전령을 관장하는 신",
        "personality": "영리하고 재치 있으며 빠른 행동을 보이는 성격",
        "myth": "아폴론의 소를 훔치고 거문고를 발명한 설화",
        "relations": "제우스와 마이아의 아들, 아프로디테와의 연관성"
    },
    "헤파이스토스": {
        "emoji": "🔥",
        "english": "Hephaestus",
        "description": "불과 대장장이의 신",
        "personality": "끈기 있고 창조적이며 다소 거칠한 성격",
        "myth": "올림포스의 무기와 도구를 제작한 설화",
        "relations": "제우스와 헤라의 아들, 아프로디테의 남편"
    }
}

# 앱 제목
st.set_page_config(page_title="그리스 로마 신화 인물 사전", layout="wide")
st.title("⚡ 그리스 로마 신화 인물 사전")

# CSS 스타일 (카드 디자인)
st.markdown("""
    <style>
    .card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 2px 4px 12px rgba(0,0,0,0.15);
        margin: 15px;
        width: 300px;
        display: inline-block;
        vertical-align: top;
    }
    .emoji {
        font-size: 30px;
    }
    .name {
        font-size: 22px;
        font-weight: bold;
        margin-top: 10px;
    }
    .desc {
        font-size: 16px;
        margin-top: 8px;
    }
    .section {
        font-size: 14px;
        margin-top: 6px;
        color: #444444;
    }
    </style>
""", unsafe_allow_html=True)

# 카드 출력
for god, info in gods.items():
    st.markdown(f"""
        <div class="card">
            <div class="emoji">{info['emoji']}</div>
            <div class="name">{info['english']} {god}</div>
            <div class="desc">{info['description']}</div>
            <div class="section"><b>성격:</b> {info['personality']}</div>
            <div class="section"><b>관련 설화:</b> {info['myth']}</div>
            <div class="section"><b>관계:</b> {info['relations']}</div>
        </div>
    """, unsafe_allow_html=True)
