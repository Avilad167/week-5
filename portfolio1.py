import sys

if len(sys.argv) != 1:
    print("Usage: python os_platform.py")
else:
    platform = sys.platform
    print(f"Operating System Platform: {platform}")
python