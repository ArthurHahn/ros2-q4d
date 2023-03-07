#******************************************************************************
#	                   Quanser 2DSFJE Description
#	                     RViz Launch File
#          Copyright (C) 2018, 2021 Walter Fetter Lages <w.fetter@ieee.org>
#
#        This program is free software: you can redistribute it and/or modify
#        it under the terms of the GNU General Public License as published by
#        the Free Software Foundation, either version 3 of the License, or
#        (at your option) any later version.
#
#        This program is distributed in the hope that it will be useful, but
#        WITHOUT ANY WARRANTY; without even the implied warranty of
#        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#        Geneal Public License for more details.
#
#        You should have received a copy of the GNU General Public License
#        along with this program.  If not, see
#        <http://www.gnu.org/licenses/>.
#
#*******************************************************************************

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.conditions import IfCondition
from launch_ros.actions import Node

def generate_launch_description():

        gui=LaunchConfiguration('gui',default='false')

        urdf_file_name = 'urdf/q2d.urdf'
        urdf_path=os.path.join(get_package_share_directory('q2d_description'),urdf_file_name)
        with open(urdf_path,'r') as infp:
                robot_desc=infp.read()

        rviz_file_name = 'config/display.rviz'
        rviz_path=os.path.join(get_package_share_directory('q2d_description'),rviz_file_name)

        return LaunchDescription([
                DeclareLaunchArgument(
                        'gui',
                        default_value='false',
                        description='Use graphical user interface to publish jointstates if true'),
                Node(
                        package='tf2_ros',
                        executable='static_transform_publisher',
                        name='q2d_origin_publisher',
                        arguments=["--frame-id", "map","--child-frame-id","origin_link"]),
                Node(
                        package='joint_state_publisher_gui',
                        executable='joint_state_publisher_gui',
                        name='joint_state_publisher',
                        condition=IfCondition(LaunchConfiguration("gui"))),
                Node(
                        package='robot_state_publisher',
                        executable='robot_state_publisher',
                        name='robot_state_publisher',
                        parameters=[{'robot_description': robot_desc}],
                        arguments=[urdf_path]),
                Node(
                        package='rviz2',
                        executable='rviz2',
                        name='rviz',
                        arguments=["-d", rviz_path])
        ])
