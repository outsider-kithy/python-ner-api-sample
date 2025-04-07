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
docker tag flask-app asia-northeast1-docker.pkg.dev/ner-app-xxxxxx/nerjapanese/flask-app
```

## Artifact Registoryにイメージをpush
```sh
docker push asia-northeast1-docker.pkg.dev/ner-app-xxxxxx/nerjapanese/flask-app
```

## Google Cloud上でコンテナをビルド
```sh
gcloud builds submit --tag asia-northeast1-docker.pkg.dev/ner-app-xxxxxx/nerjapanese/flask-app
```

`https://flask-app-xxxxxxxxx.asia-northeast1.run.app/?q=文字列`
にアクセスし、APIが稼働しているか確認。