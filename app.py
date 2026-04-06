import eel
import os

# Check if web folder exists
if not os.path.exists('web'):
    print("Error: 'web' folder not found!")
else:
    eel.init('web')
    print("Software is starting...")
    try:
        eel.start('index.html', size=(1000, 700))
    except Exception as e:
        print(f"Failed to start: {e}")