import json

def book_save(filename1, filename2, books, loan_history):
    with open(filename1, "w", encoding="utf-8") as f:
        json.dump(books, f, indent=2, ensure_ascii=False)

    with open(filename2, "w", encoding="utf-8") as f:
        json.dump(loan_history, f, indent=2, ensure_ascii=False)

filename1 = "booklist.json"
filename2 = "loan_history.json"


books = [
    {
        "title": "해리포터",
        "author": "조앤 롤링",
        "publisher": "문학수첩",
        "genre": "판타지",
    },
    {
        "title": "반지의 제왕",
        "author": "톨킨",
        "publisher": "문학수첩",
        "genre": "판타지",
    },
    {
        "title": "죽은 시인의 사회",
        "author": "피터 와이어",
        "publisher": "문학수첩",
        "genre": "드라마",
    },
    {
        "title": "노인과 바다",
        "author": "헤밍웨이",
        "publisher": "문학수첩",
        "genre": "드라마",
    },
    {"title": "1984", "author": "조지 오웰", "publisher": "문학수첩", "genre": "SF"},
    {
        "title": "페스트",
        "author": "알베르 카뮈",
        "publisher": "문학수첩",
        "genre": "소설",
    },
    {
        "title": "동물농장",
        "author": "조지 오웰",
        "publisher": "문학수첩",
        "genre": "소설",
    },
    {
        "title": "죄와 벌",
        "author": "톨스토이",
        "publisher": "문학수첩",
        "genre": "소설",
    },
    {
        "title": "어린왕자",
        "author": "생텍쥐페리",
        "publisher": "문학수첩",
        "genre": "동화",
    },
    {
        "title": "백설공주",
        "author": "그림형제",
        "publisher": "문학수첩",
        "genre": "동화",
    },
    {
        "title": "신데렐라",
        "author": "그림형제",
        "publisher": "문학수첩",
        "genre": "동화",
    },
    {"title": "흥부전", "author": "흥부", "publisher": "문학수첩", "genre": "동화"},
    {"title": "홍길동전", "author": "홍길동", "publisher": "문학수첩", "genre": "동화"},
    {"title": "햄릿", "author": "셰익스피어", "publisher": "문학수첩", "genre": "역사"},
    {
        "title": "맥베스",
        "author": "셰익스피어",
        "publisher": "문학수첩",
        "genre": "역사",
    },
    {
        "title": "오셸로",
        "author": "셰익스피어",
        "publisher": "문학수첩",
        "genre": "역사",
    },
    {
        "title": "리어왕",
        "author": "셰익스피어",
        "publisher": "문학수첩",
        "genre": "역사",
    },
    {"title": "햄릿", "author": "셰익스피어", "publisher": "북플러스", "genre": "역사"},
    {
        "title": "맥베스",
        "author": "셰익스피어",
        "publisher": "다빈소년",
        "genre": "역사",
    },
    {
        "title": "오셸로",
        "author": "셰익스피어",
        "publisher": "부경서점",
        "genre": "역사",
    },
    {
        "title": "리어왕",
        "author": "셰익스피어",
        "publisher": "북플러스",
        "genre": "역사",
    },
    {
        "title": "데미안",
        "author": "헤르만 헤세",
        "publisher": "문학좋아",
        "genre": "소설",
    },
    {
        "title": "싯다르타",
        "author": "헤르만 헤세",
        "publisher": "문학싫어",
        "genre": "소설",
    },
    {
        "title": "구토",
        "author": "장뽈 샤르트",
        "publisher": "좋은사람들",
        "genre": "소설",
    },
    {
        "title": "이방인",
        "author": "알베르 카뮈",
        "publisher": "문학수첩",
        "genre": "소설",
    },
]

loan_history = {
    "맥베스": "박현도",
    "오셸로": "정지우",
    "오셸로": "박현도",
    "리어왕": "백경이",
    "흥부전": "백경이",
    "햄릿": "이수연",
    "페스트": "이수연",
}

book_save(filename1,filename2,books,loan_history)

