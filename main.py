import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="MBTI 기반 직업 추천", page_icon="💼", layout="centered")

# MBTI별 색상/아이콘/특징 테마
mbti_themes = {
    "ISTJ": {"color": "#4E6E81", "icon": "📊", "desc": "신중하고 책임감이 강하며 체계적인 성향을 가집니다."},
    "ISFJ": {"color": "#6A9C89", "icon": "💖", "desc": "배려심이 많고 성실하며 안정적인 환경을 선호합니다."},
    "INFJ": {"color": "#A084DC", "icon": "📚", "desc": "깊은 통찰력과 비전을 가지고 타인을 돕는 것을 좋아합니다."},
    "INTJ": {"color": "#3C486B", "icon": "🧠", "desc": "전략적 사고와 계획 수립에 뛰어나며 목표 지향적입니다."},
    "ISTP": {"color": "#4B8673", "icon": "🛠️", "desc": "문제 해결 능력이 뛰어나고 도전적인 일을 즐깁니다."},
    "ISFP": {"color": "#D36B00", "icon": "🎨", "desc": "감성이 풍부하고 예술적 감각이 뛰어나며 자유를 중시합니다."},
    "INFP": {"color": "#FF6B6B", "icon": "📝", "desc": "이상주의적이며 가치와 신념을 지키는 것을 중요하게 생각합니다."},
    "INTP": {"color": "#3F72AF", "icon": "🔬", "desc": "호기심이 많고 논리적인 분석을 즐기며 창의적인 아이디어가 풍부합니다."},
    "ESTP": {"color": "#FF914D", "icon": "🏆", "desc": "활동적이고 모험을 즐기며 현실 감각이 뛰어납니다."},
    "ESFP": {"color": "#FFD93D", "icon": "🎤", "desc": "사교적이고 에너지가 넘치며 즐거움을 추구합니다."},
    "ENFP": {"color": "#FF6F91", "icon": "💡", "desc": "창의적이고 열정적이며 새로운 경험을 사랑합니다."},
    "ENTP": {"color": "#00C9A7", "icon": "⚡", "desc": "도전적이고 토론을 즐기며 다재다능한 성향을 가집니다."},
    "ESTJ": {"color": "#556052", "icon": "📈", "desc": "조직적이고 실용적이며 리더십이 뛰어납니다."},
    "ESFJ": {"color": "#A3C4BC", "icon": "🤝", "desc": "친절하고 책임감이 강하며 협력을 중요하게 생각합니다."},
    "ENFJ": {"color": "#F98404", "icon": "🌟", "desc": "타인의 성장을 돕고 영감을 주는 리더십을 발휘합니다."},
    "ENTJ": {"color": "#1E3D59", "icon": "🚀", "desc": "결단력 있고 목표 지향적이며 조직 운영에 능숙합니다."}
}

# MBTI별 직업 + 관련 학과 데이터
mbti_jobs = {
    "ISTJ": [("회계사", "회계학, 경영학"), ("법무사", "법학"), ("프로젝트 매니저", "경영학, 산업공학"), ("데이터 분석가", "통계학, 데이터사이언스")],
    "ISFJ": [("간호사", "간호학"), ("사회복지사", "사회복지학"), ("교사", "교육학"), ("행정직", "행정학")],
    "INFJ": [("작가", "문예창작학"), ("심리상담가", "심리학"), ("비영리단체 활동가", "사회학, 정치학"), ("컨설턴트", "경영학")],
    "INTJ": [("데이터 과학자", "컴퓨터공학, 통계학"), ("전략 컨설턴트", "경영학"), ("연구원", "자연과학, 공학"), ("개발자", "컴퓨터공학")],
    "ISTP": [("엔지니어", "기계공학, 전자공학"), ("파일럿", "항공운항학"), ("응급구조사", "응급구조학"), ("기계 정비사", "기계공학")],
    "ISFP": [("디자이너", "시각디자인학"), ("사진작가", "사진학"), ("작곡가", "작곡과"), ("예술가", "미술학")],
    "INFP": [("작가", "문예창작학"), ("상담가", "심리학"), ("인권운동가", "사회학, 정치학"), ("교사", "교육학")],
    "INTP": [("연구원", "자연과학, 공학"), ("소프트웨어 개발자", "컴퓨터공학"), ("발명가", "기계공학, 전자공학"), ("이론 물리학자", "물리학")],
    "ESTP": [("영업 전문가", "마케팅학, 경영학"), ("이벤트 플래너", "이벤트학, 관광학"), ("운동선수", "체육학"), ("기업가", "경영학")],
    "ESFP": [("배우", "연극영화학"), ("가수", "실용음악학"), ("홍보 담당자", "홍보학, 미디어학"), ("여행 가이드", "관광학")],
    "ENFP": [("마케터", "마케팅학"), ("작가", "문예창작학"), ("창업가", "경영학"), ("기획자", "미디어학, 경영학")],
    "ENTP": [("기업가", "경영학"), ("광고 기획자", "광고홍보학"), ("변호사", "법학"), ("토론가", "정치외교학")],
    "ESTJ": [("경영 관리자", "경영학"), ("군 장교", "군사학"), ("프로젝트 매니저", "경영학, 산업공학"), ("공무원", "행정학")],
    "ESFJ": [("교사", "교육학"), ("간호사", "간호학"), ("HR 매니저", "경영학"), ("사회복지사", "사회복지학")],
    "ENFJ": [("강사", "교육학"), ("심리상담가", "심리학"), ("정치가", "정치외교학"), ("비영리단체 리더", "사회학")],
    "ENTJ": [("CEO", "경영학"), ("전략기획가", "경영학"), ("변호사", "법학"), ("경영 컨설턴트", "경영학")]
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
.job-major {
    font-size: 0.85em;
    color: #f0f0f0;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# 제목 (검은색)
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

    # 카드 출력
    st.markdown(
        f"""
        <div class="card" style="background-color: {theme['color']}">
            <h2>{theme['icon']} {mbti} 유형</h2>
            <p><em>{theme['desc']}</em></p>
            <h4>어울리는 직업 추천</h4>
            {''.join([f"<div class='job-item'>{job} <span class='job-major'>({major})</span></div>" for job, major in jobs])}
        </div>
        """,
        unsafe_allow_html=True
    )
