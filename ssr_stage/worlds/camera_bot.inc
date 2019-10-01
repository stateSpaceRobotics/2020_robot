# Create the sensors
define d435i camera
(
    # These are the specs for the depth sensor
    # https://ark.intel.com/content/www/us/en/ark/products/190004/intel-realsense-depth-camera-d435i.html
    resolution [ 1280 720 ] 
    range [ 0.2 10.0 ]
    fov [ 87.0 58.0 ]
    pantilt [ 0.0 0.0 ]

    # model properties
    # the camera's model is interfering with itself, so I used 0 as the size
    # size [ 0.025 0.09 0.025 ]
    size [ 0.0 0.0 0.0 ]
    color "black"
    watts 100.0 # TODO find watts
)

# Create the robot model
define camera_bot position
(
    # position properties
    drive "diff"

    localization "odom"
    # localization_origin [ <defaults to model's start pose> ]

    # odometry error model parameters,
    # only used if localization is set to "odom"
    # These are the defaults, we can investigate changing later
    odom_error [0.03 0.03 0.00 0.05]

    # only used if drive is set to "car"
    # wheelbase 1.0

    # [ xmin xmax ymin ymax zmin zmax amin amax ]
    # x,y,z in m/s, angle in degrees/s
    velocity_bounds [-1 1 -1 1 -1 1 -90 90 ]
    # x,y,z in m/s/s, angle in degrees/s/s
    acceleration_bounds [-1 1 -1 1 -1 1 -90 90]

    # model properties
    # copied from Andy dimensions
    size [0.69 0.67 0.45]
    origin [0 0 0 0]
    gui_nose 1
    
    # add a camera sensor
    d435i(pose [ 1 0.000 1 0.000 ])
)

