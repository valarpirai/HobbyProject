
# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()

# Takes a screenshot
# result = device.takeSnapshot()

# Writes the screenshot to a file
# result.writeToFile('shot1.png','png')

# device.touch(385, 455, MonkeyDevice.DOWN)
# device.touch(385, 455, MonkeyDevice.UP)
while True:
    device.touch(385, 455, MonkeyDevice.DOWN_AND_UP)
