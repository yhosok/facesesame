# facesesame

## これは何か
ラズパイのカメラで顔認証してsesameのwebapiを使って鍵解錠するものです

## Install

- ラズパイ環境では下記インストールが必要になります

```
sudo apt-get install libhdf5-100 libcblas3 libatlas3-base libjasper1 libilmbase12 libopenexr22 libgstreamer1.0-0 libqtgui4 libqt4-test
```

- pipenv環境にしてありますが、現状ラズパイ上で`pipenv install`だと何故か入らなかったので、下記手順でpipにてインストールしてください
```
pipenv shell
pip install pysesame2 python-dotenv picamera[array] dlib face_recognition opencv-contrib-python gmail
```

## 運用

### 鍵解錠してもよい人の顔データ生成と配置
- スペックがそれなりのPC上で`./known_data`に判定したい人物の顔写真を置いて下記コマンドを実行してください（ラズパイ上では写真サイズがかなり小さくないと処理できないです）
```
pipenv run save-known
```
- ラズパイ環境の`./known_data`に生成された`./known_data/known_data.pkl`ファイルを配置してください

### Sesameの設定
`.env`にSesameのWebApiキーとUUIDを記載してください
https://docs.candyhouse.co/
```:.env
SESAME_KEY=
SESAME_UUID=
```

### Gmailの設定
`.env`にGmail送信のための設定を記載してください。`GMAIL_TO`は通知を受けたいアドレスになります
```:.env
GMAIL_USER=
GMAIL_PASS=
GMAIL_TO=
```

### 実行
- ラズパイ起動時実行する場合はsystemdファイル設定（`WorkingDirectory`など設定値は環境に合わせてください）
```
sudo cp facesesame.service /etc/systemd/system
sudo systemctl enable facesesame
＃ 手動
sudo systemctl start facesesame
```

- 手動では下記コマンドで実行できます。PC版のは画面にカメラで取得された動画と誰で認識されたかラベル表示がされます。
```
# ラズパイ
pipenv run raspi
# PC
pipenv run webcam
```

