# 🎼 ScoreCropper - 楽譜だけ切り抜くやつ

動画の中で，画面の一部に楽譜が映ってる系のやつあるじゃないですか．  
それをいい感じに切り抜いて，画像として保存してくれるPythonスクリプトです．

以下使用動画

https://github.com/user-attachments/assets/906d1314-85dd-481d-9e6d-2d83bae01ce5


## 🛠️ できること
- 動画から**指定した領域**を切り出して保存
- **SSIM（画像の類似度）**を使って，ほぼ同じフレームはスキップしてくれる（つまり無駄に保存されない）
- 1秒に1枚とかの感覚で間引いて保存する設定もOK

## 🚀 使い方

✍️ 設定のポイント
python
コピーする
編集する
# 切り取りたい範囲（気合で調整）
half_frame = frame[590:, 60:1215]
ここで，楽譜が表示されてるエリアを指定します．
cv2.imshow()でデバッグしながら，ベストな範囲を見つけてください．

python
コピーする
編集する
# 動画ファイル名（同じディレクトリに置いてね）
video_path = "yunagi.mp4"

# 画像の保存先
output_directory = "score"
⚙️ SSIM について
python
コピーする
編集する
ssim_threshold = 0.95
これで，フレームがどれくらい似てるかを判定しています．
数字が小さいと保存されやすく，大きいと間引かれる感じ．

📂 出力例
score/frame_0.jpg

score/frame_1.jpg

score/frame_2.jpg

...

🙆‍♂️ 動作確認済み環境
Python 3.8〜3.11くらい

Windows 10 / macOS Monterey

OpenCV / scikit-image

📄 ライセンス
とくになし．自由に使ってください．
改造・フォーク歓迎．

