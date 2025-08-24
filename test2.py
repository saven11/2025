import streamlit as st

st.set_page_config(page_title="올림포스 12신 카드", layout="centered")

# 올림포스 12신 데이터 (영어 이름 먼저, 괄호 없음, 관계는 명사형/마침표 없음)
gods = {
    "Zeus": {
        "label": "⚡ Zeus 제우스",
        "color": "#FFD700",
        "edge_left": "⚡",
        "edge_right": "🦅",
        "image": "https://upload.wikimedia.org/wikipedia/commons/4/4a/Jupiter_Smyrna_Louvre_Ma13.jpg",
        "symbol": "번개, 독수리, 왕좌",
        "personality": "권위 중시, 정의 지향, 때로는 감정적",
        "relations": "형제 포세이돈·하데스, 아내 헤라, 자녀 아테나·아폴론·아르테미스 등",
        "myths": {
            "탄생 설화": "크로노스와 레아의 막내아들로 태어나 크레타 동굴에서 자람. 유모 아말테이아의 염소젖으로 성장하여 아버지에게 삼켜진 형제들을 구출함",
            "대표적인 신화": "티탄족과의 전쟁 티타노마키아 승리로 올림포스 통치 확보",
            "다른 설화": "유럽을 납치한 백황소 이야기, 이오 이야기, 헤라클레스 탄생과 시련의 간접적 원인 제공"
        }
    },
    "Hera": {
        "label": "👑 Hera 헤라",
        "color": "#FF69B4",
        "edge_left": "🦚",
        "edge_right": "💍",
        "image": "https://upload.wikimedia.org/wikipedia/commons/2/2d/Hera_Campana_Louvre_Ma2283.jpg",
        "symbol": "공작, 왕관, 석류",
        "personality": "품위와 자존, 강한 질투심",
        "relations": "남편 제우스, 자녀 아레스·헤파이스토스·헤베",
        "myths": {
            "탄생 설화": "크로노스와 레아의 딸로 태어나 여신들의 여왕이 됨",
            "대표적인 신화": "헤라클레스에게 12과업을 불러온 원한의 근원으로 등장",
            "다른 설화": "파리스의 심판 사건에 관여, 일리아스에서 제우스를 유혹해 전장 교란"
        }
    },
    "Poseidon": {
        "label": "🌊 Poseidon 포세이돈",
        "color": "#1E90FF",
        "edge_left": "🐬",
        "edge_right": "🌊",
        "image": "https://upload.wikimedia.org/wikipedia/commons/9/9d/Poseidon_sculpture_Copenhagen_2005.jpg",
        "symbol": "삼지창, 말, 돌고래",
        "personality": "격정과 변덕, 강한 자존",
        "relations": "형제 제우스·하데스",
        "myths": {
            "탄생 설화": "크로노스와 레아의 아들로 태어나 제우스의 반란 이후 바다를 분점받음",
            "대표적인 신화": "아테네 수호신 자리를 두고 아테나와 경쟁, 소금샘과 말의 창조로 겨루었으나 패배",
            "다른 설화": "테세우스의 부친 전승, 트로이 전쟁에서 성벽을 무너뜨리거나 폭풍으로 그리스를 괴롭힘"
        }
    },
    "Demeter": {
        "label": "🌾 Demeter 데메테르",
        "color": "#9ACD32",
        "edge_left": "🌾",
        "edge_right": "🌿",
        "image": "https://upload.wikimedia.org/wikipedia/commons/d/d0/Demeter_Altemps_Inv8605.jpg",
        "symbol": "곡식 이삭, 낫, 횃불",
        "personality": "자애와 인내, 상실에 민감",
        "relations": "자녀 페르세포네, 형제 제우스·포세이돈·하데스",
        "myths": {
            "탄생 설화": "크로노스와 레아의 딸. 농경과 풍요 관장",
            "대표적인 신화": "페르세포네 납치 설화와 엘레우시스 신비의 기원. 딸의 귀환 주기로 계절이 생김",
            "다른 설화": "트립톨레모스에게 농사법 전수, 데모폰을 불로 단련해 불사의 존재로 만들려다 중단"
        }
    },
    "Athena": {
        "label": "🦉 Athena 아테나",
        "color": "#708090",
        "edge_left": "🛡️",
        "edge_right": "🦉",
        "image": "https://upload.wikimedia.org/wikipedia/commons/f/fd/Mattei_Athena_Louvre_Ma530_n2.jpg",
        "symbol": "올빼미, 올리브, 방패",
        "personality": "지혜와 절제, 전략 중시",
        "relations": "아버지 제우스",
        "myths": {
            "탄생 설화": "제우스가 메티스를 삼킨 뒤 머리를 가르자 완전무장한 상태로 탄생",
            "대표적인 신화": "아테네 수호신으로 올리브나무 선물, 트로이 전쟁에서 그리스 편 지원",
            "다른 설화": "아라크네와의 베짜기 대결, 팔라듐 수호상 전승"
        }
    },
    "Apollo": {
        "label": "☀️ Apollo 아폴론",
        "color": "#FFA500",
        "edge_left": "☀️",
        "edge_right": "🎵",
        "image": "https://upload.wikimedia.org/wikipedia/commons/8/8d/Apollo_Belvedere_Vatican.jpg",
        "symbol": "태양, 리라, 월계관",
        "personality": "조화 추구, 예술과 질서 애호",
        "relations": "쌍둥이 누이 아르테미스, 아버지 제우스",
        "myths": {
            "탄생 설화": "레토가 델로스 섬에서 아폴론과 아르테미스를 출산",
            "대표적인 신화": "델포이의 피톤을 무찌르고 신탁 주관",
            "다른 설화": "다프네 추격과 월계수 변신, 히아킨토스 비극, 마르시아스와의 음악 대결"
        }
    },
    "Artemis": {
        "label": "🌙 Artemis 아르테미스",
        "color": "#87CEFA",
        "edge_left": "🏹",
        "edge_right": "🦌",
        "image": "https://upload.wikimedia.org/wikipedia/commons/4/4d/Diana_of_Versailles.jpg",
        "symbol": "활, 사슴, 초승달",
        "personality": "자유와 정결, 독립성",
        "relations": "쌍둥이 오라버니 아폴론",
        "myths": {
            "탄생 설화": "레토와 제우스 사이에서 태어나 곧바로 산파 역할로 어머니를 돕는 능력 보여줌",
            "대표적인 신화": "사냥꾼 악타이온을 사슴으로 변하게 함, 니오베의 자식들을 벌함",
            "다른 설화": "오리온과의 인연과 별자리 이야기, 이피게네이아와 관련된 희생 전승"
        }
    },
    "Ares": {
        "label": "🗡️ Ares 아레스",
        "color": "#B22222",
        "edge_left": "🛡️",
        "edge_right": "🗡️",
        "image": "https://upload.wikimedia.org/wikipedia/commons/3/3c/Ares_Ludovisi_Altemps_Inv8609.jpg",
        "symbol": "창과 방패, 전차",
        "personality": "충동과 호전성, 용맹",
        "relations": "부모 제우스·헤라, 연인 아프로디테",
        "myths": {
            "탄생 설화": "제우스와 헤라 사이에서 태어난 전쟁의 화신",
            "대표적인 신화": "헤파이스토스의 그물에 아프로디테와 함께 붙들려 조롱당함",
            "다른 설화": "트로이 전쟁에서 다양한 전투 개입, 공포와 두려움의 의인화 포보스·데이모스 관련"
        }
    },
    "Aphrodite": {
        "label": "🌹 Aphrodite 아프로디테",
        "color": "#FF1493",
        "edge_left": "🌹",
        "edge_right": "🕊️",
        "image": "https://upload.wikimedia.org/wikipedia/commons/2/23/Venus_de_Milo_Louvre_Ma399_n4.jpg",
        "symbol": "장미, 비너스 조개, 비둘기",
        "personality": "매혹과 설득, 자유분방한 정서",
        "relations": "남편 헤파이스토스, 연인 아레스, 아들 에로스",
        "myths": {
            "탄생 설화": "우라노스의 바다 거품에서 태어났다는 전승 또는 제우스와 디오네의 딸 전승",
            "대표적인 신화": "파리스의 심판에서 가장 아름다운 여신으로 선택되어 트로이 전쟁의 기폭제 마련",
            "다른 설화": "아도니스 신화, 인간 목동 안키세스와의 사이에서 아이네이아스 출산"
        }
    },
    "Hephaestus": {
        "label": "🔨 Hephaestus 헤파이스토스",
        "color": "#A0522D",
        "edge_left": "🔨",
        "edge_right": "🔥",
        "image": "https://upload.wikimedia.org/wikipedia/commons/c/c9/Hephaistos_Louvre_Ma13.jpg",
        "symbol": "망치, 모루, 불",
        "personality": "근면과 창의, 외유내강",
        "relations": "어머니 헤라, 아내 아프로디테",
        "myths": {
            "탄생 설화": "추락으로 다리를 절게 되었다는 전승 존재. 헤라가 단독으로 낳았다는 전승",
            "대표적인 신화": "아킬레우스의 방패와 신들의 무기 제작",
            "다른 설화": "자율로 움직이는 자동인형과 황금의 하녀 제작, 판도라 창조 참여"
        }
    },
    "Hermes": {
        "label": "👟 Hermes 헤르메스",
        "color": "#32CD32",
        "edge_left": "👟",
        "edge_right": "📨",
        "image": "https://upload.wikimedia.org/wikipedia/commons/d/d8/Hermes_Ingenui_Pio-Clementino_Inv544.jpg",
        "symbol": "날개 달린 샌들, 카두케우스 지팡이",
        "personality": "영리함과 재치, 기민한 행동",
        "relations": "아버지 제우스, 어머니 마이아",
        "myths": {
            "탄생 설화": "동굴에서 태어나 그날로 장난과 기지가 드러남",
            "대표적인 신화": "아폴론의 소를 훔치고 리라를 만들어 화해",
            "다른 설화": "영혼 인도 역할, 오디세우스에게 몰리 허브 제공으로 키르케 마법 무력화"
        }
    },
    "Dionysus": {
        "label": "🍇 Dionysus 디오니소스",
        "color": "#800080",
        "edge_left": "🍇",
        "edge_right": "🍷",
        "image": "https://upload.wikimedia.org/wikipedia/commons/5/5c/Dionysos_Louvre_Ma87_n2.jpg",
        "symbol": "포도송이, 포도덩굴, 잔",
        "personality": "쾌활과 해방, 광희와 변덕",
        "relations": "아버지 제우스, 어머니 세멜레",
        "myths": {
            "탄생 설화": "세멜레가 소멸하자 제우스의 넓적다리에서 두 번째로 태어남",
            "대표적인 신화": "바쿠스의 여인들과 펜테우스 비극, 미다스의 황금손 이야기",
            "다른 설화": "해적들을 돌고래로 바꾸는 기적, 아리아드네 구출 후 별자리로 승천"
        }
    }
}

st.title("🏛️ 올림포스 12신 카드 백과")
st.caption("카드에는 핵심 정보, 카드 바깥에는 탄생 설화·대표적인 신화·다른 설화가 나뉘어 표시됩니다")

# 선택 박스: 라벨은 이모지 포함 전체 이름 사용
options = [data["label"] for data in gods.values()]
label_to_key = {gods[k]["label"]: k for k in gods}
selected_label = st.selectbox("신을 선택하세요", options)
key = label_to_key[selected_label]
info = gods[key]

# 동적 스타일 주입 (모든 CSS는 문자열로 감싸 SyntaxError 방지)
st.markdown(
    f"""
    <style>
    :root {{ --accent: {info['color']}; }}
    .card-wrap {{
      position: relative;
      width: 760px;
      max-width: 92vw;
      margin: 22px auto 10px auto;
    }}
    .card {{
      background-color: var(--accent);
      color: #ffffff;
      border-radius: 22px;
      padding: 24px 24px 18px 24px;
      box-shadow: 0 12px 28px rgba(0,0,0,.25);
      text-align: center;
    }}
    .hero {{
      width: 100%;
      max-height: 320px;
      object-fit: cover;
      border-radius: 16px;
      margin-bottom: 12px;
      box-shadow: 0 6px 18px rgba(0,0,0,.25);
      border: 2px solid rgba(255,255,255,.35);
    }}
    .edge {{
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      font-size: 34px;
      text-shadow: 0 2px 6px rgba(0,0,0,.25);
    }}
    .edge.left {{ left: -34px; }}
    .edge.right {{ right: -34px; }}
    .card h2 {{
      margin: 8px 0 10px 0;
      font-size: 30px;
    }}
    .card p {{
      margin: 6px 0;
      font-size: 16px;
    }}
    .section {{
      max-width: 960px;
      margin: 14px auto;
      background: #ffffff;
      border-left: 10px solid var(--accent);
      padding: 14px 18px;
      border-radius: 12px;
      box-shadow: 0 6px 18px rgba(0,0,0,.08);
    }}
    .section h4 {{
      margin: 0 0 6px 0;
      font-size: 18px;
      color: #222;
    }}
    .section p {{
      margin: 0;
      color: #444;
      line-height: 1.55;
    }}
    .links {{
      max-width: 960px;
      margin: 18px auto 40px auto;
      background: #f7f7fb;
      border-left: 10px solid var(--accent);
      padding: 14px 18px;
      border-radius: 12px;
      box-shadow: 0 6px 18px rgba(0,0,0,.06);
    }}
    .links a {{
      display: inline-block;
      margin-right: 12px;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# 중앙 카드 렌더링 (이미지 + 기본 정보)
st.markdown(
    f"""
    <div class="card-wrap">
        <div class="edge left">{info['edge_left']}</div>
        <div class="edge right">{info['edge_right']}</div>
        <div class="card">
            <img class="hero" src="{info['image']}" alt="{info['label']}">
            <h2>{info['label']}</h2>
            <p><b>상징:</b> {info['symbol']}</p>
            <p><b>성격:</b> {info['personality']}</p>
            <p><b>관계:</b> {info['relations']}</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# 카드 바깥: 항목별 설화 박스
st.subheader("📚 다른 설화")
for section, text in info["myths"].items():
    st.markdown(
        f"""
        <div class="section">
            <h4>📖 {section}</h4>
            <p>{text}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# 하단 참고 링크 (저작권 안전/학습용)
st.markdown(
    """
    <div class="links">
      <b>더 알아보기</b> ·
      <a href="https://www.theoi.com/" target="_blank">Theoi Project</a>
      <a href="https://ko.wikipedia.org/wiki/%EA%B7%B8%EB%A6%AC%EC%8A%A4_%EC%8B%A0%ED%99%94" target="_blank">위키백과: 그리스 신화</a>
      <a href="https://www.perseus.tufts.edu/" target="_blank">Perseus Digital Library</a>
    </div>
    """,
    unsafe_allow_html=True,
)
