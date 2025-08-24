import streamlit as st

# 신들의 정보 데이터베이스
gods = {
    "Zeus": {
        "name": "Zeus 제우스",
        "emoji": "⚡",
        "symbol": "번개",
        "personality": "권위적이고 정의를 중시하는 성격",
        "relations": "헤라의 남편, 아테나의 아버지, 포세이돈과 하데스의 형제",
        "myths": {
            "탄생 설화": "제우스는 크로노스와 레아의 아들로 태어나 아버지의 삼키는 운명에서 벗어나기 위해 크레타 섬에서 자랐다",
            "대표적인 신화": "티탄과의 전쟁인 티타노마키아를 승리로 이끌며 올림포스의 지배자가 되었다"
        },
        "color": "#f4d03f"
    },
    "Hera": {
        "name": "Hera 헤라",
        "emoji": "👑",
        "symbol": "왕관",
        "personality": "질투심이 강하고 가정과 결혼을 수호하는 성격",
        "relations": "제우스의 아내, 올림포스 여신들의 여왕",
        "myths": {
            "탄생 설화": "크로노스와 레아의 딸로 제우스와 형제",
            "대표적인 신화": "헤라는 제우스의 연인들과 그 자식들을 괴롭힌 이야기로 유명하다"
        },
        "color": "#f5b7b1"
    },
    "Poseidon": {
        "name": "Poseidon 포세이돈",
        "emoji": "🌊",
        "symbol": "삼지창",
        "personality": "격정적이고 변덕스러운 성격",
        "relations": "제우스와 하데스의 형제",
        "myths": {
            "탄생 설화": "크로노스와 레아의 아들로 제우스와 함께 아버지에게서 구출되었다",
            "대표적인 신화": "아테네 도시의 수호신 자리를 아테나와 다투었으나 패배하였다"
        },
        "color": "#5dade2"
    },
    "Hades": {
        "name": "Hades 하데스",
        "emoji": "💀",
        "symbol": "지팡이",
        "personality": "냉정하고 침착한 성격",
        "relations": "제우스와 포세이돈의 형제, 페르세포네의 남편",
        "myths": {
            "탄생 설화": "크로노스와 레아의 아들로 제우스와 함께 성장했다",
            "대표적인 신화": "페르세포네를 납치해 저승의 여왕으로 삼았다"
        },
        "color": "#566573"
    },
    "Athena": {
        "name": "Athena 아테나",
        "emoji": "🦉",
        "symbol": "올빼미",
        "personality": "지혜롭고 전쟁에서 전략을 중시하는 성격",
        "relations": "제우스의 딸",
        "myths": {
            "탄생 설화": "제우스가 메티스를 삼킨 후 머리에서 탄생했다",
            "대표적인 신화": "트로이 전쟁에서 그리스 편을 도왔다"
        },
        "color": "#82e0aa"
    }
}

st.set_page_config(page_title="그리스 로마 신화", layout="centered")

st.title("⚡ 그리스 로마 신화 인물 카드")

selected_god = st.selectbox("신을 선택하세요", list(gods.keys()))

god = gods[selected_god]

st.markdown(
    f"""
    <div style='display: flex; justify-content: center; margin-top: 20px;'>
        <div style='background-color: {god['color']}; padding: 30px; border-radius: 20px; width: 500px; text-align: center; box-shadow: 0px 4px 10px rgba(0,0,0,0.2);'>
            <div style='display: flex; justify-content: space-between; font-size: 30px;'>
                <span>✨</span>
                <span>{god['emoji']}</span>
                <span>🌟</span>
            </div>
            <h2 style='margin: 10px 0;'>{god['name']}</h2>
            <p><b>상징:</b> {god['symbol']}</p>
            <p><b>성격:</b> {god['personality']}</p>
            <p><b>관계:</b> {god['relations']}</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.subheader("📖 신화 이야기")
for section, myth in god["myths"].items():
    st.markdown(f"**{section}**")
    st.write(myth)
