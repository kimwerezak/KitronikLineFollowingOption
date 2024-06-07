#This is based off of the block code provided by @KitronikLtd.
#This line following function will move quite fast due to the while loop chosen,
#but will slow down to follow a line. To start the code, press the logo on the MicroBit.

def line_follow():
    LeftSensor = 0
    RightSensor = 0
    SensorDifference = 0
    
    while True:
        LeftSensor = Kitronik_Move_Motor.read_sensor(Kitronik_Move_Motor.LfSensor.LEFT)
        RightSensor = Kitronik_Move_Motor.read_sensor(Kitronik_Move_Motor.LfSensor.RIGHT)
        SensorDifference = abs(LeftSensor - RightSensor)
        
        if SensorDifference > 10:
            if LeftSensor > RightSensor:
                Kitronik_Move_Motor.motor_off(Kitronik_Move_Motor.Motors.MOTOR_RIGHT)
                Kitronik_Move_Motor.motor_on(Kitronik_Move_Motor.Motors.MOTOR_LEFT,
                    Kitronik_Move_Motor.MotorDirection.FORWARD,
                    1)
                basic.pause(100)
            else:
                Kitronik_Move_Motor.motor_off(Kitronik_Move_Motor.Motors.MOTOR_LEFT)
                Kitronik_Move_Motor.motor_on(Kitronik_Move_Motor.Motors.MOTOR_RIGHT,
                    Kitronik_Move_Motor.MotorDirection.FORWARD,
                    1)
                basic.pause(100)
        else:
            Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.FORWARD, 1)

input.on_logo_event(TouchButtonEvent.PRESSED, line_follow)
