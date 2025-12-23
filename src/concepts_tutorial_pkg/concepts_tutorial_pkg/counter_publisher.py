import rclpy

from rclpy.node import Node

from example_interfaces.msg import Int64

class CounterPublisher(Node):

    count : int = 0

    def __init__(self):
        super().__init__('Counter_Publisher')
        self.get_logger().info('Counter Publisher node has been started!')
        self.counter_publisher = self.create_publisher(Int64, 'counter', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)


    def timer_callback(self):
        self.get_logger().info(f"Count {self.count}")

        msg = Int64()
        msg.data = self.count
        self.counter_publisher.publish(msg)

        self.count += 1

def main():
    rclpy.init()
    node = CounterPublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()