# facesesame

## Install

- pipenv環境にしてあるが、現状ラズパイ上で`pipenv install`だと何故か入らないので、下記手順でpipにてインストール
```sh
pipenv shell
pip install pysesame2 python-dotenv picamera[array] dlib face_recognition opencv-contrib-python gmail
```

- systemdファイル設定（ファイルの中身はインストール場所に合わせてください）
```sh
sudo cp facesesame.service /etc/systemd/system
sudo systemctl enable facesesame
＃ 手動
sudo systemctl start facesesame
```

- ラズパイ環境では下記インストールが必要になります

```sh
sudo apt-get install libhdf5-100 libcblas3 libatlas3-base libjasper1 libilmbase12 libopenexr22 libgstreamer1.0-0 libqtgui4 libqt4-test
```