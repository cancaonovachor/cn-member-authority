# cn-member-authority

Notion のデータベースを参照し、Google Group のメンバーを自動で管理する。アクティブなメンバーを団員一覧データベースから取得し、Google Group に追加。非アクティブになったメンバーは自動で削除する。

## 必要なツール

- Python
- Poetry (Python のパッケージ管理ツール)

## セットアップ手順

1. gcloud 認証:

   ```bash
   gcloud auth login
   ```

   CancaoNova Solutions Google Cloud プロジェクトの権限がない場合は誰かに言う

2. Secret Manager から.env ファイルを取得。:

   ```bash
   gcloud secrets versions access latest --secret=cn-auth-member-env-file --project=starlit-road-203901 > .env
   ```

   取得した.env ファイルをプロジェクトのルートディレクトリに配置。

3. Poetry を使用してプロジェクトの依存関係をインストール:

   ```bash
   poetry install
   ```

## 実行方法

セットアップが完了したら、以下のコマンドを実行:

```bash
poetry run python src/main.py
```
