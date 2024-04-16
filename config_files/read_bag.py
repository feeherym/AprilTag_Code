import rosbag
from sensor_msgs.msg import Image

# Open the bag file
bag = rosbag.Bag('/home/michaela/catkin_ws/src/apriltag_ros/config_files/titan_data_2023-10-27-13-00-10.bag')

# Iterate over each message in the bag file
# for topic, msg, t in bag.read_messages():
#     print(f"Topic: {topic}")
#     # print(f"Message: {msg}")
#     print(f"Timestamp: {t}")
#     print("------")

for topic, msg, t in bag.read_messages(topics=['/ovc/rgb/image_raw']):
    # Check if the message is of type Image
    if isinstance(msg, Image):
        print(f"Timestamp: {t}")
        print(f"Width: {msg.width}, Height: {msg.height}")
        # You can access the image data from msg.data if needed
        print("------")

# Close the bag file
bag.close()
