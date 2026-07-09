# 정지용 포트폴리오

Dark Aesthetic 테마의 개인 포트폴리오 웹사이트입니다.

## 특징
- 반응형 디자인 (모바일, 태블릿, 데스크톱)
- Dark & Light 테마 지원
- 부드러운 스크롤 애니메이션
- SEO 최적화

## 배포
- **서버**: AWS Lightsail
- **URL**: http://54.116.91.136
- **웹서버**: Nginx

## 파일 구조
```
day1/
├── index.html          # 메인 포트폴리오 페이지
└── README.md           # 프로젝트 설명
```

## 시작하기

### 로컬 개발
```bash
# 프로젝트 폴더 진입
cd day1

# 간단한 웹서버로 실행 (Python)
python3 -m http.server 8000
```

브라우저에서 `http://localhost:8000` 접속

## 배포 방법
```bash
git add .
git commit -m "Update portfolio"
git push origin main
```

Lightsail 서버에 자동으로 배포됩니다.
