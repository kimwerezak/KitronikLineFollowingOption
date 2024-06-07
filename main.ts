// This is based off of the block code provided by @KitronikLtd.
// This line following function will move quite fast due to the while loop chosen,
// but will slow down to follow a line. To start the code, press the logo on the MicroBit.
input.onLogoEvent(TouchButtonEvent.Pressed, function line_follow() {
    let LeftSensor = 0
    let RightSensor = 0
    let SensorDifference = 0
    while (true) {
        LeftSensor = Kitronik_Move_Motor.readSensor(Kitronik_Move_Motor.LfSensor.Left)
        RightSensor = Kitronik_Move_Motor.readSensor(Kitronik_Move_Motor.LfSensor.Right)
        SensorDifference = Math.abs(LeftSensor - RightSensor)
        if (SensorDifference > 10) {
            if (LeftSensor > RightSensor) {
                Kitronik_Move_Motor.motorOff(Kitronik_Move_Motor.Motors.MotorRight)
                Kitronik_Move_Motor.motorOn(Kitronik_Move_Motor.Motors.MotorLeft, Kitronik_Move_Motor.MotorDirection.Forward, 1)
                basic.pause(100)
            } else {
                Kitronik_Move_Motor.motorOff(Kitronik_Move_Motor.Motors.MotorLeft)
                Kitronik_Move_Motor.motorOn(Kitronik_Move_Motor.Motors.MotorRight, Kitronik_Move_Motor.MotorDirection.Forward, 1)
                basic.pause(100)
            }
            
        } else {
            Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.Forward, 1)
        }
        
    }
})
