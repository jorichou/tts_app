# TTS App (Text-to-Speech Application)

.txtファイルをアップロードし、VOICEVOXエンジンを使用して音声ファイルを生成・ダウンロードできるWebアプリケーションです。

## 特徴
- **ファイルアップロード**: .txtファイルをドラッグ＆ドロップまたは選択してアップロード。
- **音声生成**: VOICEVOXエンジンと連携し、高品質な日本語音声を生成。
- **再生と保存**: 生成された音声をブラウザ上で試聴でき、WAV形式でダウンロード可能。

## 技術スタック
- **Frontend**: Svelte / Bun / Vite
- **Backend**: Python / FastAPI / Uvicorn
- **TTS Engine**: VOICEVOX

## 前提条件
- [VOICEVOX Engine](https://github.com/VOICEVOX/voicevox_engine) が起動していること（デフォルト: `http://localhost:50021`）
- [Bun](https://bun.sh/) がインストールされていること
- Python 3.12以上がインストールされていること

## セットアップと起動方法

### 1. バックエンドの起動
```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Windowsの場合: .venv\Scripts\activate
uvicorn main:app --reload
```

### 2. フロントエンドの起動
```bash
cd frontend
bun install
bun run dev
```

## プロジェクト構造
- `frontend/`: Svelteを使用したUI部分
- `backend/`: FastAPIを使用したAPIサーバー
  - `api/`: コントローラー（エンドポイント定義）
  - `services/`: 音声生成ロジック
  - `utils/`: ファイル処理・テキスト整形ユーティリティ

## トラブルシューティング
- **CORSエラー**: バックエンドの `main.py` でフロントエンドのオリジンが許可されているか確認してください。
- **VOICEVOX接続エラー**: VOICEVOX Engineが起動しているか、ポート番号（50021）が正しいか確認してください。
- **ファイル形式**: 現在、`.txt` ファイルのみをサポートしています。
