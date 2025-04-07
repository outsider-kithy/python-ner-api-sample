# ローカルでAPIを稼働させる方法

## コンテナのビルド
```sh
docker build -t flask-app .
```

## 起動
```sh
docker run -d -p 8080:8080 -e PORT=8080 flask-app
```
`http://localhost:8080/`にアクセスし、`Hello, World`と表示されればOK。

## コンテナの停止
```sh
docker stop コンテナID
```

## 仮想環境で動かす場合
### 仮想環境.venvの作成
```sh
python3 -m venv .venv
```

### 仮想環境を有効化
```sh
source .venv/bin/activate
# 無効化
deactivate
```

### 必要なパッケージをインストール
```sh
pip install -r requirements.txt
```

### APIを起動
```sh
python3 -m app
```
`http://localhost:8080/`にアクセスし、`Hello, World`と表示されればOK。