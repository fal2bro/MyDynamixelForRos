#!/usr/bin/env python3

import rospy

from mydynamixel_for_ros.msg import *
import myDynamixel

#使い方
#必要に応じてmain関数のMotorNumを変更
#rostopic pub /トピック名　データ型　メッセージ内容
#---example---"
#rostopic pub position_control SetPosition "{id: 1, position: 1000}"


def publish_sample_data():
    rospy.init_node('sample_publisher')
    pub = rospy.Publisher('velocity_control', SetVelocity, queue_size=10)
    rate = rospy.Rate(1)  # パブリッシュの周波数を設定 (1 Hz)

    while not rospy.is_shutdown():
        # SetPosition型のメッセージを作成し、適当なデータを設定
        msg = SetVelocity()
        msg.id = 1
        msg.velocity = 100  # 適当な値を設定
        # メッセージをパブリッシュ
        pub.publish(msg)
        rate.sleep()

        msg.id = 1
        msg.velocity = 0
        rate.sleep()


def set_goal_pos_callback(data):
    print("Set Goal Position of ID %s =%s" % (data.id, data.position))

    dxl.Change_OperatingMode(data.id, dxl.operating_mode.position_control)
    dxl.write(data.id, dxl.Address.TorqueEnable, True)
    dxl.write(data.id, dxl.Address.GoalPosition, data.position)

def set_goal_current_callback(data):
    print("Set Goal current of ID %s =%s" % (data.id, data.current))

    dxl.Change_OperatingMode(data.id, dxl.operating_mode.current_control)
    dxl.write(data.id, dxl.Address.TorqueEnable,True)
    dxl.write(data.id, dxl.Address.GoalCurrent, data.current)

def set_goal_velocity_callback(data):
    print("Set Goal velocity  of ID %s =%s" % (data.id, data.velocity))

    dxl.Change_OperatingMode(data.id, dxl.operating_mode.velocity_control)
    dxl.write(data.id, dxl.Address.TorqueEnable,True)
    dxl.write(data.id, dxl.Address.GoalVelocity, data.velocity)

def set_goal_ex_pos_callback(data):
    print("Set Extended Goal Position of ID %s =%s" % (data.id, data.position))

    dxl.Change_OperatingMode(data.id, dxl.operating_mode.extended_Position_control)
    dxl.write(data.id, dxl.Address.TorqueEnable, True)
    dxl.write(data.id, dxl.Address.GoalPosition, data.position)

def set_goal_current_base_pos_callback(data):
    print("Set Current_base Goal Position of ID %s =%s" % (data.id, data.position))

    dxl.Change_OperatingMode(data.id, dxl.operating_mode.current_base_position_control)
    dxl.write(data.id, dxl.Address.TorqueEnable, True)
    dxl.write(data.id, dxl.Address.GoalPosition, data.position)

def set_goal_pwm_callback(data):
    print("Set pwm Goal Position of ID %s =%s" % (data.id, data.pwm))

    dxl.Change_OperatingMode(data.id, dxl.operating_mode.pwm_control)
    dxl.write(data.id, dxl.Address.TorqueEnable, True)
    dxl.write(data.id, dxl.Address.GoalPWM, data.pwm)






def mydynamixel_control():
    rospy.init_node('mydynamixel_control')
    rospy.Subscriber('position_control',SetPosition,set_goal_pos_callback)
    rospy.Subscriber('current_control',SetCurrent,set_goal_current_callback)
    rospy.Subscriber('velocity_control',SetVelocity,set_goal_velocity_callback)
    rospy.Subscriber('extended_Position_control',SetPosition,set_goal_ex_pos_callback)
    rospy.Subscriber('current_base_position_control',SetPosition,set_goal_current_base_pos_callback)
    rospy.Subscriber('pwm_control',SetPwm,set_goal_pwm_callback)
    rospy.spin()

def main():
    global dxl
    dxl = myDynamixel.Dxlfunc()
    MotorNum = dxl.init('/dev/ttyUSB0', baudrate=57600)
    if MotorNum >0:
        print("dynamixel controller ready")
        mydynamixel_control()
    else:
        print("初期化失敗")


if __name__ == '__main__':
    main()
