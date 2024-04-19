# AprilTag_Code

Requirements:
Ubuntu 20.04
ROS Noetic

Configuration Files:

config/tags.yaml
Standalone tags:
Standalone tags need to be listed or the program will not detect any tags.
List standalone tags in format:
{id: ID, size: SIZE, name: "NAME"}
Tag bundles:
List tag bundles in format:
       name: 'CUSTOM_BUNDLE_NAME',
       layout:
         [
           {id: ID, size: SIZE, x: X_POS, y: Y_POS, z: Z_POS, qw: QUAT_W_VAL, qx: QUAT_X_VAL, qy: QUAT_Y_VAL, qz: QUAT_Z_VAL},
           ...
         ]

config/settings.yaml
The tag family needs to be set here.

apriltag_ros_/continuous_detection.launch
The topics for the input camera parameters and images are set here.

apriltag_ros_/single_image_client.launch
For inferencing on single images, set the camera focal lengths in this file.  You can also set the single image load and save path from here.


Output topics:
/tf: relative pose between the camera frame and each detected tag's or tag bundle's frame (specified in tags.yaml) using tf. Published only if publish_tf: true in config/settings.yaml;
/tag_detections: the same information as provided by the /tf topic but as a custom message carrying the tag ID(s), size(s) and geometry_msgs/PoseWithCovarianceStamped pose information (where plural applies for tag bundles). This is always published;
/tag_detections_image: the same image as input by /camera/image_rect but with the detected tags highlighted. Published only if publish_tag_detections_image==true in launch/continuous_detection.launch. 


Sample usage:
For inferencing on single images:
roslaunch apriltag_ros single_image_server.launch
roslaunch apriltag_ros single_image_client.launch image_load_path:=<FULL PATH TO INPUT IMAGE> image_save_path:=<FULL PATH TO OUTPUT IMAGE>

For continuous detection:
roslaunch apriltag_ros continuous_detection.launch
