# MyDynamixelForRos
myDynamixelをROSで動かすためのパッケージ
## インストール手順
ワークスペース(~/catkin\_ws/src)内で
```bash
git  clone git@github.com:fal2bro/MyDynamixelForRos.git
catkin_make(or catkin build)
```
## 使い方
**サンプルスクリプト:mydynamixel\_control.py**
```bash
roscore
rosrun mydynamixel\_for\_ros
#必要に応じてmain関数のMotorNumを変更
#基本構文:rostopic pub /トピック名　データ型　メッセージ内容
#message型はmsgディレクトリ内参照
#---example---"
#rostopic pub position_control SetPosition "{id: 1, position: 1000}"
```
もちろん，pythonスクリプト内でパブリッシュすることもできる（直接mydynamixelの関数を呼び出したほうがいい気もするが）
 
## 動作環境
ubuntu20.04 
