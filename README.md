# MyDynamixelForRos
myDynamixelをROSで動かすためのパッケージ
## インストール手順
ワークスペース(~/catkin\_ws/src)内で
```bash
git  clone https://github.com/fal2bro/MyDynamixelForRos.git 
```
## 使い方
**サンプルスクリプト:mydynamixel\_control.py**
必要に応じてmain関数のMotorNumを変更<br>
USBデバイスに権限を与えていない場合は付与しておく
```bash
sudo chmod 666 /dev/ttyUSB0/
```
wsl上でUSBの認識をさせる場合は[こちら参照](https://learn.microsoft.com/ja-jp/windows/wsl/connect-usb)
実行スクリプト<br>
```bash
roscore
rosrun mydynamixel\_for\_ros mydynamixel_control.py
```
パブリッシュを送ると様々なモードでモーターを動かすことができる
基本構文:rostopic pub /トピック名　データ型　メッセージ内容<br>　　
message型はmsgディレクトリ内参照<br>
**example**
```bash
rostopic pub position_control SetPosition "{id: 1, position: 1000}"
```
もちろん，pythonスクリプト内でパブリッシュすることもできる（直接mydynamixelの関数を呼び出したほうがいい気もするが）
 
## 動作環境
ubuntu20.04 
