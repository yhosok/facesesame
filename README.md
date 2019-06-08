# facesesame

## Install

- ラズパイ環境では下記インストールが必要になります

```
sudo apt-get install libhdf5-100 libcblas3 libatlas3-base libjasper1 libilmbase12 libopenexr22 libgstreamer1.0-0 libqtgui4 libqt4-test
```

- pipenv環境にしてあるが、現状ラズパイ上で`pipenv install`だと何故か入らなかったので、下記手順でpipにてインストール
```
pipenv shell
pip install pysesame2 python-dotenv picamera[array] dlib face_recognition opencv-contrib-python gmail
```

- 起動時実行する場合はsystemdファイル設定（`WorkingDirectory`など設定値は環境に合わせてください）
```
sudo cp facesesame.service /etc/systemd/system
sudo systemctl enable facesesame
＃ 手動
sudo systemctl start facesesame
```

## 実行

- スペックがそれなりのPC上で`./known_data`に判定したい人物の顔写真を置いて下記コマンドを実行してください（ラズパイ上では写真サイズがかなり小さくないと処理できないです）
```
pipenv run save-known
```
- ラズパイ環境の`./known_data`に生成された`./known_data/known_data.pkl`ファイルを配置してください

- 下記コマンドで実行されます
```
# ラズパイ
pipenv run raspi
# PC
pipenv run webcam
```