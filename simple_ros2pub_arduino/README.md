# publish ros2 to arduino LED Python ament_python

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
ros2 run simple_ros2pub_arduino ros2pub_arduino
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
ros2 pkg create --build-type ament_python --license Apache-2.0 simple_ros2pub_arduino
```
