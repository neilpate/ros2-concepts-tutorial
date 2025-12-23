import rclpy

from rclpy.node import Node

class FirstNode(Node):

    count : int = 0

    def __init__(self):
        super().__init__('Count_Publisher') # Node name cannot have spaces in it!
        self.get_logger().info('Count Publisher node has been started!')
        self.timer = self.create_timer(1.0, self.timer_callback)


    def timer_callback(self):
        self.get_logger().info(f"Count {self.count}")
        self.count += 1

def main():
    rclpy.init()
    node = FirstNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()