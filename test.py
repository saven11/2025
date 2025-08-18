import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

# 신 데이터 (영어 이름 + 이모지 포함)
gods = {
    "Zeus 제우스⚡": {"설명": "올림포스 최고 신, 하늘과 번개를 다스린다.", "상징": "번개, 독수리", "성격": "권위적이지만 변덕스러움.", "관계": ["Hera 👑", "Athena 🦉", "Apollo 🎶", "Artemis 🏹", "Ares 🗡️", "Aphrodite 💖", "Poseidon 🌊", "Hades 💀", "Hermes 🕊️", "Hephaestus 🔨"]},
    "Hera 헤라 👑": {"설명": "결혼과 가정의 여신, 제우스의 아내.", "상징": "공작, 왕관", "성격": "질투심이 강하고 가정을 중시.", "관계": ["Zeus ⚡", "Ares 🗡️", "Hephaestus 🔨"]},
    "Poseidon 포세이돈 🌊": {"설명": "바다의 신, 지진과 바다를 다스림.", "상징": "삼지창, 말", "성격": "거칠고 강력함.", "관계": ["Zeus ⚡", "Hades 💀"]},
    "Hades 하데스 💀": {"설명": "저승의 신.", "상징": "케르베로스, 투구", "성격": "엄격하고 냉정함.", "관계": ["Zeus ⚡", "Poseidon 🌊", "Persephone 🌸"]},
    "Athena 아테나 🦉": {"설명": "지혜와 전쟁 전략의 여신.", "상징": "부엉이, 방패", "성격": "지혜롭고 전략적.", "관계": ["Zeus ⚡", "Poseidon 🌊"]},
    "Apollo 아폴로 🎶": {"설명": "음악과 태양, 예언의 신.", "상징": "리라, 태양", "성격": "예술적이고 자부심 강함.", "관계": ["Zeus ⚡", "Artemis 🏹", "Daphne 🌿"]},
    "Artemis 아르테미스 🏹": {"설명": "사냥과 달의 여신.", "상징": "활, 사슴", "성격": "자유롭고 독립적.", "관계": ["Apollo 🎶"]},
    "Ares 아레스 🗡️": {"설명": "전쟁의 신.", "상징": "창, 방패", "성격": "충동적이고 공격적.", "관계": ["Hera 👑", "Aphrodite 💖"]},
    "Aphrodite 아프로디테 💖": {"설명": "사랑과 미의 여신.", "상징": "비둘기, 조개", "성격": "매혹적이고 자유분방.", "관계": ["Ares 🗡️", "Hephaestus 🔨"]},
    "Hermes 헤르메스 🕊️": {"설명": "신들의 전령, 상업과 도둑의 수호신.", "상징": "날개 달린 신발, 지팡이", "성격": "영리하고 재치 있음.", "관계": ["Zeus ⚡"]},
    "Hephaestus 헤파이스토스 🔨": {"설명": "대장장이의 신, 불과 금속의 신.", "상징": "망치, 모루", "성격": "근면하고 창의적.", "관계": ["Hera 👑", "Aphrodite 💖"]},
    "Persephone 페르세포네 🌸": {"설명": "저승의 여왕이자 봄의 여신.", "상징": "석류", "성격": "순수하면서도 강함.", "관계": ["Hades 💀", "Demeter 🌾"]},
    "Demeter 데메테르 🌾": {"설명": "농업과 풍요의 여신.", "상징": "곡식 이삭", "성격": "모성적이고 자애로움.", "관계": ["Persephone 🌸"]},
    "Daphne 다프네 🌿": {"설명": "강의 신의 딸, 아폴론에게 쫓기다 월계수로 변함.", "상징": "월계수", "성격": "순결과 자유를 사랑함.", "관계": ["Apollo 🎶"]},
    "Dionysus 디오니소스 🍇": {"설명": "포도주와 축제의 신.", "상징": "포도, 와인잔", "성격": "쾌활하고 자유분방.", "관계": ["Zeus ⚡"]},
    "Hecate 헤카테 🌙": {"설명": "마법과 달, 밤의 여신.", "상징": "달, 지팡이", "성격": "신비롭고 독립적.", "관계": []}
}

# 관계별 설화 데이터
myths = {
    ("Zeus ⚡", "Hera 👑"): "끝없는 부부 싸움과 질투 이야기.",
    ("Zeus ⚡", "Athena 🦉"): "Zeus 머리에서 태어난 Athena.",
    ("Hades 💀", "Persephone 🌸"): "저승 납치로 계절이 생긴 이야기.",
    ("Apollo 🎶", "Artemis 🏹"): "쌍둥이 남매 이야기.",
    ("Aphrodite 💖", "Ares 🗡️"): "밀회가 발각된 이야기.",
    ("Apollo 🎶", "Daphne 🌿"): "Daphne가 월계수로 변한 이야기."
}

# 앱 시작
st.set_page_config(page_title="그리스 로마 신화 인물 사전", layout="wide")
st.title("🏛️ 그리스 로마 신화 인물 사전")

selected_god = st.selectbox("신을 선택하세요", sorted(list(gods.keys())))
god_info = gods[selected_god]

st.subheader(f"{selected_god}")
st.write(f"**설명:** {god_info['설명']}")
st.write(f"**상징:** {god_info['상징']}")
st.write(f"**성격:** {god_info['성격']}")

# 관계 시각화
graph = nx.Graph()
graph.add_node(selected_god)
for relation in god_info["관계"]:
    if relation not in gods:
        continue
    graph.add_node(relation)
    story = myths.get((selected_god, relation)) or myths.get((relation, selected_god))
    label = story if story else ""
    graph.add_edge(selected_god, relation, label=label)

pos = nx.spring_layout(graph, seed=42, k=0.3)  # 선 길이 조정
plt.figure(figsize=(8,8))
nx.draw_networkx_nodes(graph, pos, node_color='lightyellow', node_size=2000)
nx.draw_networkx_labels(graph, pos, font_family="DejaVu Sans", font_weight='bold')
edge_labels = nx.get_edge_attributes(graph, 'label')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_family="DejaVu Sans")
nx.draw_networkx_edges(graph, pos)
st.pyplot(plt)

# 관계 설화 표시
for relation in god_info["관계"]:
    story = myths.get((selected_god, relation)) or myths.get((relation, selected_god))
    if story:
        st.markdown(f"**📖 {selected_god} ↔ {relation}**: {story}")
