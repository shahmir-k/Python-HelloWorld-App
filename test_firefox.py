import subprocess
import sys
import os

def test_firefox_detection():
    """Test different ways to find and launch Firefox on Windows"""
    print("Testing Firefox detection on Windows...")
    
    # Common Firefox paths on Windows
    firefox_paths = [
        'firefox',  # If in PATH
        r'C:\Program Files\Mozilla Firefox\firefox.exe',
        r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe',
        r'%APPDATA%\Mozilla\Firefox\firefox.exe'
    ]
    
    # Expand environment variables
    firefox_paths = [os.path.expandvars(path) for path in firefox_paths]
    
    print("Checking these paths:")
    for i, path in enumerate(firefox_paths, 1):
        print(f"{i}. {path}")
        if os.path.exists(path):
            print(f"   ✓ EXISTS")
        else:
            print(f"   ✗ NOT FOUND")
    
    print("\nTrying to launch Firefox...")
    
    # Try each path
    for path in firefox_paths:
        try:
            print(f"Trying: {path}")
            result = subprocess.run([path], capture_output=True, text=True, timeout=3)
            print(f"Success! Exit code: {result.returncode}")
            return True
        except subprocess.TimeoutExpired:
            print("Firefox launched successfully (timeout means it's running)")
            return True
        except (subprocess.CalledProcessError, FileNotFoundError) as e:
            print(f"Failed: {e}")
            continue
    
    print("Firefox not found or failed to launch")
    return False

if __name__ == "__main__":
    test_firefox_detection()
