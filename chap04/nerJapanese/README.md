# ローカルでAPIを稼働させる方法

## コンテナのビルド
```sh
docker build -t flask-app .
```

## 起動
```sh
docker run -d -p 8080:8080 -e PORT=8080 flask-app
```
`http://localhost:8080/?q=文字列`にアクセス。

## コンテナの停止
```sh
docker stop flask-app
```

# Cloud Runにデプロイ

## Cloud Build API を有効化
```sh
gcloud services enable cloudbuild.googleapis.com
```

## プロジェクトの権限を設定
```sh
gcloud config set project プロジェクトID
```

## ローカルとリモートのイメージをタグ付け
```sh
docker tag flask-app asia-northeast1-docker.pkg.dev/ner-app-455807/nerjapanese/flask-app
```

## Artifact Registoryにイメージをpush
```sh
docker push asia-northeast1-docker.pkg.dev/ner-app-455807/nerjapanese/flask-app
```

## Google Cloud上でコンテナをビルド
```sh
gcloud builds submit --tag asia-northeast1-docker.pkg.dev/ner-app-455807/nerjapanese/flask-app
```

`https://flask-app-xxxxxxxxx.asia-northeast1.run.app/?q=文字列`
にアクセスし、APIが稼働しているか確認。

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
`http://localhost:8080/q=文字列`
にアクセスし、APIが稼働しているか確認。