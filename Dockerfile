# ベースイメージ
FROM python:3.10-slim

# 標準入出力をアンバッファードにする
ENV PYTHONUNBUFFERED=1

# 作業ディレクトリ
WORKDIR /app

# ソースをコピー
COPY . /app