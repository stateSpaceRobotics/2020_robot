# Create the sensors
define topurg ranger
(
  sensor(
    range [0 7.0]
    fov 60
    samples 1081
  )
  # generic model properties
  color "black"
  size [ 0.05 0.05 0.1 ]
)

# Create the robot model
define ranger_bot position
(
  #localization "odom"
  localization_origin [0 0 0 0]
  odom_error [0 0 0 0 0 0]
  size [0.69 0.67 0.45]
  origin [0 0 0 0]
  gui_nose 1
  drive "diff"
  topurg(pose [ 0.275 0.000 0 0.000 ])
  #bitmap "robot.png"
)

