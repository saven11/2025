<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>올림포스 12신</title>
  <style>
    body {
      font-family: 'Noto Sans KR', sans-serif;
      margin: 0;
      background: #f9f9f9;
      color: #333;
      text-align: center;
    }
    h1 {
      margin: 20px;
      font-size: 2.2em;
    }
    .container {
      display: flex;
      justify-content: center;
      align-items: center;
      flex-direction: column;
      gap: 40px;
    }
    .card {
      display: flex;
      align-items: center;
      justify-content: space-between;
      width: 70%;
      max-width: 900px;
      min-height: 320px;
      border-radius: 20px;
      box-shadow: 0 6px 16px rgba(0,0,0,0.2);
      overflow: hidden;
      background: white;
      position: relative;
      margin: auto;
    }
    .card img {
      width: 280px;
      height: 280px;
      object-fit: cover;
      border-radius: 16px;
      margin: 20px;
    }
    .card-content {
      flex: 1;
      padding: 20px;
      text-align: left;
    }
    .card h2 {
      margin: 0;
      font-size: 1.8em;
    }
    .relation, .myth {
      margin-top: 10px;
      font-size: 0.95em;
      line-height: 1.5;
    }
    .emoji-left, .emoji-right {
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      font-size: 2em;
    }
    .emoji-left { left: 10px; }
    .emoji-right { right: 10px; }
    .extra-myth {
      margin-top: 12px;
      font-size: 0.9em;
      color: #444;
      font-style: italic;
    }
    footer {
      margin: 40px;
      font-size: 1.1em;
    }
    footer a {
      color: #0077cc;
      text-decoration: none;
    }
    footer a:hover {
      text-decoration: underline;
    }
  </style>
</head>
<body>
  <h1>올림포스 12신</h1>
  <div class="container">

    <!-- 제우스 -->
    <div class="card" style="background:#fff8e1;">
      <span class="emoji-left">⚡</span>
      <img src="https://upload.wikimedia.org/wikipedia/commons/3/3a/Statue_of_Zeus.jpg" alt="Zeus">
      <div class="card-content">
        <h2>Zeus 제우스</h2>
        <div class="relation">올림포스의 주신, 번개와 하늘의 지배자</div>
        <div class="myth">티탄을 무찌르고 올림포스를 통치하게 됨</div>
        <div class="extra-myth">대표 설화: 크로노스가 삼킨 형제자매들을 구출하고 올림포스의 왕이 됨</div>
      </div>
      <span class="emoji-right">🌩️</span>
    </div>

    <!-- 헤라 -->
    <div class="card" style="background:#fde0dc;">
      <span class="emoji-left">👑</span>
      <img src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Hera_Campana_Louvre_Ma2283.jpg" alt="Hera">
      <div class="card-content">
        <h2>Hera 헤라</h2>
        <div class="relation">결혼과 가정의 여신, 제우스의 아내</div>
        <div class="myth">질투심으로 많은 영웅을 괴롭힘</div>
        <div class="extra-myth">대표 설화: 헤라클레스에게 12과업을 지시하도록 만듦</div>
      </div>
      <span class="emoji-right">💍</span>
    </div>

    <!-- 포세이돈 -->
    <div class="card" style="background:#e0f7fa;">
      <span class="emoji-left">🌊</span>
      <img src="https://upload.wikimedia.org/wikipedia/commons/9/9d/Poseidon_sculpture_Copenhagen_2005.jpg" alt="Poseidon">
      <div class="card-content">
        <h2>Poseidon 포세이돈</h2>
        <div class="relation">바다와 지진의 신, 제우스의 형제</div>
        <div class="myth">삼지창으로 바다를 다스림</div>
        <div class="extra-myth">대표 설화: 아테나와 아테네 도시 수호권을 놓고 다툼</div>
      </div>
      <span class="emoji-right">🔱</span>
    </div>

    <!-- 아테나 -->
    <div class="card" style="background:#e8f5e9;">
      <span class="emoji-left">🦉</span>
      <img src="https://upload.wikimedia.org/wikipedia/commons/f/fd/Mattei_Athena_Louvre_Ma530_n2.jpg" alt="Athena">
      <div class="card-content">
        <h2>Athena 아테나</h2>
        <div class="relation">지혜와 전쟁 전략의 여신</div>
        <div class="myth">제우스의 머리에서 탄생함</div>
        <div class="extra-myth">대표 설화: 아라크네와의 직조 대결에서 아라크네를 거미로 변하게 함</div>
      </div>
      <span class="emoji-right">⚔️</span>
    </div>

    <!-- 아폴론 -->
    <div class="card" style="background:#fff3e0;">
      <span class="emoji-left">🎶</span>
      <img src="https://upload.wikimedia.org/wikipedia/commons/8/8d/Apollo_Belvedere_Vatican.jpg" alt="Apollo">
      <div class="card-content">
        <h2>Apollo 아폴론</h2>
        <div class="relation">빛, 음악, 예언의 신</div>
        <div class="myth">델포이 신탁을 주관함</div>
        <div class="extra-myth">대표 설화: 다프네를 사랑했으나 월계수 나무로 변해버림</div>
      </div>
      <span class="emoji-right">☀️</span>
    </div>

    <!-- 아르테미스 -->
    <div class="card" style="background:#f3e5f5;">
      <span class="emoji-left">🏹</span>
      <img src="https://upload.wikimedia.org/wikipedia/commons/4/4d/Diana_of_Versailles.jpg" alt="Artemis">
      <div class="card-content">
        <h2>Artemis 아르테미스</h2>
        <div class="relation">사냥과 달의 여신, 아폴론의 쌍둥이</div>
        <div class="myth">순결과 자연을 수호함</div>
        <div class="extra-myth">대표 설화: 액타이온이 그녀를 엿보아 사슴으로 변해 개들에게 찢김</div>
      </div>
      <span class="emoji-right">🌙</span>
    </div>

    <!-- 아레스 -->
    <div class="card" style="background:#ffebee;">
      <span class="emoji-left">🛡️</span>
      <img src="https://upload.wikimedia.org/wikipedia/commons/3/3c/Ares_Ludovisi_Altemps_Inv8609.jpg" alt="Ares">
      <div class="card-content">
        <h2>Ares 아레스</h2>
        <div class="relation">전쟁과 파괴의 신</div>
        <div class="myth">아프로디테와 연인 관계</div>
        <div class="extra-myth">대표 설화: 헤파이스토스에게 두 연인이 덫에 걸려 망신당함</div>
      </div>
      <span class="emoji-right">⚔️</span>
    </div>

    <!-- 아프로디테 -->
    <div class="card" style="background:#fce4ec;">
      <span class="emoji-left">🌹</span>
      <img src="https://upload.wikimedia.org/wikipedia/commons/2/23/Venus_de_Milo_Louvre_Ma399_n4.jpg" alt="Aphrodite">
      <div class="card-content">
        <h2>Aphrodite 아프로디테</h2>
        <div class="relation">사랑과 미의 여신</div>
        <div class="myth">바다 거품에서 태어남</div>
        <div class="extra-myth">대표 설화: 트로이 전쟁의 발단이 된 파리스의 황금사과 심판</div>
      </div>
      <span class="emoji-right">💖</span>
    </div>

    <!-- 헤르메스 -->
    <div class="card" style="background:#e8eaf6;">
      <span class="emoji-left">🪽</span>
      <img src="https://upload.wikimedia.org/wikipedia/commons/d/d8/Hermes_Ingenui_Pio-Clementino_Inv544.jpg" alt="Hermes">
      <div class="card-content">
        <h2>Hermes 헤르메스</h2>
        <div class="relation">전령과 상업, 도둑의 신</div>
        <div class="myth">날개 달린 샌들로 신들의 전령 역할</div>
        <div class="extra-myth">대표 설화: 태어나자마자 소를 훔치고 거북 껍질로 리라를 발명</div>
      </div>
      <span class="emoji-right">📜</span>
    </div>

    <!-- 헤파이스토스 -->
    <div class="card" style="background:#fbe9e7;">
      <span class="emoji-left">🔥</span>
      <img src="https://upload.wikimedia.org/wikipedia/commons/c/c9/Hephaistos_Louvre_Ma13.jpg" alt="Hephaestus">
      <div class="card-content">
        <h2>Hephaestus 헤파이스토스</h2>
        <div class="relation">불과 대장장이의 신</div>
        <div class="myth">신들의 무기를 제작함</div>
        <div class="extra-myth">대표 설화: 제우스의 머리를 도끼로 쪼개 아테나가 태어나게 도움</div>
      </div>
      <span class="emoji-right">⚒️</span>
    </div>

    <!-- 데메테르 -->
    <div class="card" style="background:#f1f8e9;">
      <span class="emoji-left">🌾</span>
      <img src="https://upload.wikimedia.org/wikipedia/commons/d/d0/Demeter_Altemps_Inv8605.jpg" alt="Demeter">
      <div class="card-content">
        <h2>Demeter 데메테르</h2>
        <div class="relation">농업과 풍요의 여신</div>
        <div class="myth">딸 페르세포네를 잃고 계절이 생김</div>
        <div class="extra-myth">대표 설화: 페르세포네가 하데스와 지하세계에 머물며 계절의 순환이 시작됨</div>
      </div>
      <span class="emoji-right">🍎</span>
    </div>

    <!-- 디오니소스 -->
    <div class="card" style="background:#ede7f6;">
      <span class="emoji-left">🍇</span>
      <img src="https://upload.wikimedia.org/wikipedia/commons/5/5c/Dionysos_Louvre_Ma87_n2.jpg" alt="Dionysus">
      <div class="card-content">
        <h2>Dionysus 디오니소스</h2>
        <div class="relation">포도주와 축제의 신</div>
        <div class="myth">술과 광기의 힘을 부여함</div>
        <div class="extra-myth">대표 설화: 미다스 왕에게 만지는 것을 황금으로 바꾸는 능력을 줌</div>
      </div>
      <span class="emoji-right">🍷</span>
    </div>

  </div>

  <footer>
    더 알아보기: 
    <a href="https://ko.wikipedia.org/wiki/%EA%B7%B8%EB%A6%AC%EC%8A%A4_%EC%8B%A0%ED%99%94" target="_blank">
      위키백과 - 그리스 신화
    </a>
  </footer>
</body>
</html>
