cmake_minimum_required(VERSION 3.8)
project(simple_ros2pub_arduino_cpp)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(PkgConfig REQUIRED)

pkg_check_modules(SERIAL libserial)

add_executable(simple_ros2pub_arduino_cpp src/simple_ros2pub_arduino_cpp.cpp)
ament_target_dependencies(simple_ros2pub_arduino_cpp rclcpp std_msgs)
target_include_directories(simple_ros2pub_arduino_cpp PUBLIC "${SERIAL_INCLUDE_DIRS}" )
target_link_libraries(simple_ros2pub_arduino_cpp "${SERIAL_LDFLAGS}")

install(TARGETS
  simple_ros2pub_arduino_cpp
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
  RUNTIME DESTINATION bin
DESTINATION lib/${PROJECT_NAME}
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
