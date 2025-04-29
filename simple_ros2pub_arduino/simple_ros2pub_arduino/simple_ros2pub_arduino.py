import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial


class SimpleRos2subArduino(Node):

    def __init__(self):
        super().__init__("simple_ros2pub_arduino")
        self.declare_parameter("port","/dev/ttyACM0")
        self.declare_parameter("baudrate", 115200)

        self.port = self.get_parameter("port").value
        self.baudrate = self.get_parameter("baudrate").value
        self.arduino_ = serial.Serial(port=self.port, baudrate=self.baudrate)
        self.sub_ = self.create_subscription(String, "SerialTransmitter",self.msgCallback, 10)
        self.get_logger().info("SerialTransmitter topic created")
        
        #self.timer_ = self.create_timer(self.frequency_, self.timerCallback)


    def msgCallback(self, msg):
        self.arduino_.write(msg.data.encode("utf-8"))


def main():
    rclpy.init()

    simple_ros2pub_arduino = SimpleRos2subArduino()
    rclpy.spin(simple_ros2pub_arduino)
    
    simple_ros2pub_arduino.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()