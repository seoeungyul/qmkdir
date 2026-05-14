# qmkdir

랜덤 이름의 디렉토리를 생성하는 CLI 도구입니다.  
A CLI tool that creates a directory with a random name.

---

## 사용법 / Usage

```bash
python qmkdir.py [-d 경로] [-n 바이트수] [--full-path]
```

## 옵션 / Options

| 옵션 / Option | 설명 / Description | 기본값 / Default |
|---|---|---|
| `-d` | 디렉토리를 생성할 경로 / Base directory path | 현재 디렉토리 / Current directory |
| `-n` | 랜덤 바이트 수 / Number of random bytes | `3` (6자리 hex / 6-char hex) |
| `--full-path` | 전체 경로 출력 / Print full path instead of name only | `False` |

## 예시 / Examples

```bash
# 현재 디렉토리에 랜덤 디렉토리 생성
# Create a random directory in the current directory
python qmkdir.py

# 특정 경로에 생성
# Create in a specific path
python qmkdir.py -d C:\Users\user\Desktop

# 바이트 수를 늘려 더 긴 이름 생성
# Generate a longer name with more bytes
python qmkdir.py -n 8

# 전체 경로 출력
# Print the full path
python qmkdir.py --full-path
```

출력 예시 / Output example:
```
a3f9c1
```

```
# --full-path 사용 시 / with --full-path
C:\Users\user\Desktop\a3f9c1
```

생성된 디렉토리 이름은 `-n` 바이트 랜덤 값의 hex 문자열입니다.  
The directory name is a hex string derived from `-n` random bytes.
