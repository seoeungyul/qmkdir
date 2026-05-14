# qmkdir

랜덤 이름의 디렉토리를 생성하는 CLI 도구입니다.

## 사용법

```bash
python qmkdir.py [-d 경로]
```

## 옵션

| 옵션 | 설명 | 기본값 |
|------|------|--------|
| `-d` | 디렉토리를 생성할 경로 | 현재 디렉토리 |

## 예시

```bash
# 현재 디렉토리에 랜덤 디렉토리 생성
python qmkdir.py

# 특정 경로에 생성
python qmkdir.py -d C:\Users\user\Desktop
```

출력 예시:
```
a3f9c1
```

생성된 디렉토리 이름은 3바이트 랜덤 값의 hex 문자열(6자리)입니다.
