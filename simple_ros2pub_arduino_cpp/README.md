# publish ros2 to arduino LED C++

## How to run

### Arduino

```
#define LED_PIN 13

// use this with ros2 humble SimpleRos2subArduino package.
void setup() {
  // put your setup code here, to run once:
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);

  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()){
    int x = Serial.readString().toInt();
    if(x == 0){
      digitalWrite(LED_PIN, LOW);    
    }else{
      digitalWrite(LED_PIN, HIGH);    
    }
  }
}
```

### Terminal 1

```
ros2 run simple_ros2pub_arduino_cpp simple_ros2pub_arduino_cpp 
```

### Terminal 2 

- Turn on Arduino Led

```
ros2 topic pub /serial_transmitter std_msgs/msg/String "data: '1'" 
```

- Turn off Arduino Led

```
ros2 topic pub /serial_transmitter std_msgs/msg/String "data: '0'" 
```

### Package created with

```
ros2 pkg create --build-type ament_cmake simple_ros2pub_arduino_cpp --dependencies  rclcpp std_msgs  PkgConfig
```
