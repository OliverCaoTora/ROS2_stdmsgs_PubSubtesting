import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/doraoliver/Studium/ros_study/ros_test/test_int32_ws/install/int32_topic_pkg'
