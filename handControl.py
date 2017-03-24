import serial, Leap, thread, time, sys
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

# Serial Port initialization

ser = serial.Serial('/dev/cu.usbserial-DA01LHO8', 57600)


class SampleListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']

    def on_init(self, controller):
        print "Initializated"

    def on_connect(self, controller):
        print "Connected"

        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

    def on_disconnect(self, controller):
        print "Disconnected"

    def on_exit(self, controller):
        print "bye"

    def on_frame(self, controller):
        frame = controller.frame()

        print "Frame id: %d, timestamp: %d, hands: %d, fingers: %d, tools: %d, gestures: %d" % (
            frame.id, frame.timestamp, len(frame.hands), len(frame.fingers),  len(frame.tools), len(frame.gestures()))
        if len(frame.hands) == 2:
            ser.write('b')
            print 'Found B B B B B.... STOP'
        for hand in frame.hands:
            handType= "left hand" if hand.is_left else "right hand"
            print "  %s,id %d, position: %s" % (handType,hand.id, hand.palm_position)

        for gesture in frame.gestures():
            if gesture.type == Leap.Gesture.TYPE_CIRCLE:
                circle = CircleGesture(gesture)
                ser.write('a')  # this will make the car move backwards
                print "A A A A A A Half Speed"

            #if gesture.type == Leap.Gesture.TYPE_SWIPE:
             #   swipe = SwipeGesture(gesture)
              #  print ser.write('b')


    def state_string(self, state):
        if state == Leap.Gesture.STATE_START:
            return "STATE_START"

        if state == Leap.Gesture.STATE_UPDATE:
            return "STATE_UPDATE"

        if state == Leap.Gesture.STATE_STOP:
            return "STATE_STOP"

        if state == Leap.Gesture.STATE_INVALID:
            return "STATE_INVALID"


def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()
