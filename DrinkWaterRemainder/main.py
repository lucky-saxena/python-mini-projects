import time
from plyer import notification

try:
    while True:
        print("Please sip some water!")
        notification.notify(
            title="Take a break!",
            message="It's time to take a short break and sip some water. ",
            timeout=10
        )
        time.sleep(60*60)
except KeyboardInterrupt:
    print("\nWater reminder stopped.")