#!/usr/bin/python3

import sys

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class SquarePublisher(Node):

	def __init__(self):
		super().__init__('square_publisher')
		self.publisher_=self.create_publisher(Float64,sys.argv[1],1)
		timer_period=float(sys.argv[4])
		self.timer=self.create_timer(timer_period,self.timer_callback)
		self.turn=True;

	def timer_callback(self):
		ref=Float64()
		ref.data=float(sys.argv[2] if self.turn else sys.argv[3])
		self.turn=not self.turn
		self.publisher_.publish(ref)
        
def main(args=None):
	if len(sys.argv) < 5:
        	print('square.py topic min max period')
        	exit()
	
	rclpy.init(args=args)

	square_publisher=SquarePublisher()
	rclpy.spin(square_publisher)

	square_publisher.destroy_node()
	rclpy.shutdown()

    
if __name__ == '__main__':
	main()
