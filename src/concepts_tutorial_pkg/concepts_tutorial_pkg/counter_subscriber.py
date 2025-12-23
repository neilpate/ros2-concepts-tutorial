import rclpy

from rclpy.node import Node

from example_interfaces.msg import Int64

class CounterSubscriber(Node):
    def __init__(self):
        super().__init__("Counter_Subscriber")
        self.get_logger().info("Counter Subscriber node has been started!")
        
        self.counter_subscriber = self.create_subscription(Int64, "counter", self.counter_callback, 10)

    def counter_callback(self, msg: Int64):
        self.get_logger().info(f"Received count: {msg.data}")


def main():
    rclpy.init()
    node = CounterSubscriber()
    rclpy.spin(node)
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()