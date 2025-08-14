import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="MBTI 기반 직업 추천", page_icon="💼", layout="centered")

# MBTI별 색상/아이콘 테마
mbti_themes = {
    "ISTJ": {"color": "#4E6E81", "icon": "📊"},
    "ISFJ": {"color": "#6A9C89", "icon": "💖"},
    "INFJ": {"color": "#A084DC", "icon": "📚"},
    "INTJ": {"color": "#3C486B", "icon": "🧠"},
    "ISTP": {"color": "#4B8673", "icon": "🛠️"},
    "ISFP": {"color": "#D36B00", "icon": "🎨"},
    "INFP": {"color": "#FF6B6B", "icon": "📝"},
    "INTP": {"color": "#3F72AF", "icon": "🔬"},
    "ESTP": {"color": "#FF914D", "icon": "🏆"},
    "ESFP": {"color": "#FFD93D", "icon": "🎤"},
    "ENFP": {"color": "#FF6F91", "icon": "💡"},
    "ENTP": {"color": "#00C9A7", "icon": "⚡"},
    "ESTJ": {"color": "#556052", "icon": "📈"},
    "ESFJ": {"color": "#A3C4BC", "icon": "🤝"},
    "ENFJ": {"color": "#F98404", "icon": "🌟"},
    "ENTJ": {"color": "#1E3D59", "icon": "🚀"}
}

# MBTI별 직업 데이터
mbti_jobs = {
    "ISTJ": ["회계사", "법무사", "프로젝트 매니저", "데이터 분석가"],
    "ISFJ": ["간호사", "사회복지사", "교사", "행정직"],
    "INFJ": ["작가", "심리상담가", "비영리단체 활동가", "컨설턴트"],
    "INTJ": ["데이터 과학자", "전략 컨설턴트", "연구원", "개발자"],
    "ISTP": ["엔지니어", "파일럿", "응급구조사", "기계 정비사"],
    "ISFP": ["디자이너", "사진작가", "작곡가", "예술가"],
    "INFP": ["작가", "상담가", "인권운동가", "교사"],
    "INTP": ["연구원", "소프트웨어 개발자", "발명가", "이론 물리학자"],
    "ESTP": ["영업 전문가", "이벤트 플래너", "운동선수", "기업가"],
    "ESFP": ["배우", "가수", "홍보 담당자", "여행 가이드"],
    "ENFP": ["마케터", "작가", "창업가", "기획자"],
    "ENTP": ["기업가", "광고 기획자", "변호사", "토론가"],
    "ESTJ": ["경영 관리자", "군 장교", "프로젝트 매니저", "공무원"],
    "ESFJ": ["교사", "간호사", "HR 매니저", "사회복지사"],
    "ENFJ": ["강사", "심리상담가", "정치가", "비영리단체 리더"],
    "ENTJ": ["CEO", "전략기획가", "변호사", "경영 컨설턴트"]
}

# CSS 스타일 (배경 이미지, 폰트, 카드 스타일)
page_bg = """
<style>
body {
    background-image: url('https://images.unsplash.com/photo-1533750349088-cd871a92f312');
    background-size: cover;
    background-attachment: fixed;
    font-family: 'Segoe UI', sans-serif;
}
.card {
    padding: 20px;
    border-radius: 15px;
    margin: 15px 0;
    color: white;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
}
.job-item {
    padding: 10px;
    margin: 5px 0;
    border-radius: 8px;
    background-color: rgba(255,255,255,0.2);
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# 제목
st.markdown("<h1 style='text-align:center; color:black;'>💼 MBTI 기반 직업 추천</h1>", unsafe_allow_html=True)
st.write(" ")

# MBTI 선택
mbti = st.selectbox(
    "MBTI를 선택하세요:",
    options=sorted(mbti_jobs.keys())
)

# 버튼 클릭 시 결과 표시
if st.button("🔍 직업 추천 받기"):
    theme = mbti_themes[mbti]
    jobs = mbti_jobs[mbti]

    st.markdown(
        f"""
        <div class="card" style="background-color: {theme['color']}">
            <h2>{theme['icon']} {mbti} 유형</h2>
            <h4>어울리는 직업 추천</h4>
            {''.join([f"<div class='job-item'>{job}</div>" for job in jobs])}
        </div>
        """,
        unsafe_allow_html=True
    )
