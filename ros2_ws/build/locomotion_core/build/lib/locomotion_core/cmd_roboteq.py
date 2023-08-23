import rclpy 
from rclpy.node import Node #A node class from rclpy.node to create our own node.

from std_msgs.msg import Int16

import serial #for serial communication?
roboteq_obj = serial.Serial(
port='/dev/ttyUSB0',
baudrate=115200,
parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE,
bytesize=serial.EIGHTBITS,
timeout=1)


class motor_driver(Node):

    #constructor using 'self' instance of the class
    def __init__(self):
        super().__init__('cmd_roboteq')
        self.inCmd = 0.0
        self.wl = 0
        self.wr = 0
        self.subscription = self.create_subscription(
            Int16,
            'wheels_l',
            self.cmd_callback_left,
            5)
        self.subscription = self.create_subscription(
            Int16,
            'wheels_r',
            self.cmd_callback_right,
            5)
        self.subscription  # prevent unused variable warning

    def cmd_callback_left(self, msg):
        self.wl = msg.data
        payload1 = "!G 1 " + str(self.wl) + "_"
        roboteq_obj.write(str.encode(payload1))
        
    def cmd_callback_right(self, msg):
        self.wr = msg.data
        payload2 = "!G 2 " + str(-self.wr) + "_"
        roboteq_obj.write(str.encode(payload2))
        
def main(args=None):
    rclpy.init(args=args)

    # Create an instance of the 'motor_driver' class
    minimal_subscriber = motor_driver()

     # Start the event loop to process ROS messages
    rclpy.spin(minimal_subscriber)

    # Cleanup the node
    minimal_subscriber.destroy_node()

    # Shutdown the ROS framework
    rclpy.shutdown()

if __name__ == '__main__':
    main()