import cv2
import os
from skimage.metrics import structural_similarity as ssim

def calculate_ssim(img1, img2):
    # 画像をグレースケールに変換
    gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # SSIMインデックスを計算
    index, _ = ssim(gray_img1, gray_img2, full=True)
    return index

def extract_frames(video_path, output_dir, frame_interval=1, ssim_threshold=0.95):
    # 動画を読み込む
    cap = cv2.VideoCapture(video_path)

    # 動画のプロパティを取得
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_interval_frames = int(fps * frame_interval)

    # 保存先ディレクトリが存在しない場合は作成
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # フレームを取得して保存
    current_frame = 0  # current_frameをループの外で初期化
    previous_frame = None

    while current_frame < total_frames:
        ret, frame = cap.read()

        if not ret:
            break

        height, width, _ = frame.shape
        half_frame = frame[590:, 60:1215]

        if current_frame % frame_interval_frames == 0:
            if previous_frame is not None:
                # 前のフレームとのSSIMを計算
                similarity_index = calculate_ssim(half_frame, previous_frame)

                # SSIMが指定された閾値以下の場合、フレームを保存
                if similarity_index < ssim_threshold:
                    output_path = os.path.join(output_dir, f"frame_{current_frame // int(fps)}.jpg")
                    cv2.imwrite(output_path, half_frame)
            else:
                output_path = os.path.join(output_dir, f"frame_{current_frame // int(fps)}.jpg")
                cv2.imwrite(output_path, half_frame)

            # 前のフレームを更新
            previous_frame = half_frame

        current_frame += 1

    # リソースを解放
    cap.release()

if __name__ == "__main__":
    video_path = "yunagi.mp4"
    output_directory = "score"
    
    extract_frames(video_path, output_directory)
