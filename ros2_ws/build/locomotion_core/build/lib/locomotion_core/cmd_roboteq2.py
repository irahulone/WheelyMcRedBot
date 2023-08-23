import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

global serialFlag
serialFlag = 0;

try:
    import serial
    roboteq_obj = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1)
    serialFlag = 1
except:
    print("Serial doesn't exist.")

class motor_driver(Node):

    def __init__(self):
        super().__init__('cmd_roboteq2')
        self.inCmd = 0.0
        self.subscription = self.create_subscription(
            Int16,
            'r4/du2/pwr',
            self.cmd_callback,
            5)
        self.subscription  # prevent unused variable warning

    def move_motors(self, val):
        global serialFlag
        payload1 = "!G 1 " + str(-val) + "_"
        payload2 = "!G 2 " + str(val) + "_"
        if(serialFlag):
            roboteq_obj.write(str.encode(payload1))
            roboteq_obj.write(str.encode(payload2))
            
    def cmd_callback(self, msg):
        inCmd = msg.data
        self.move_motors(inCmd)

def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = motor_driver()
    rclpy.spin(minimal_subscriber)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
