#!/usr/bin/env python3
"""
Test script to verify the Flask application is working
"""

import requests
import time
import subprocess
import sys
import os

def test_server():
    """Test if the Flask server is running"""
    try:
        # Try to connect to the server
        response = requests.get('http://localhost:5000', timeout=5)
        if response.status_code == 200:
            print("✅ Server is running successfully!")
            print("🌐 Open your browser and go to: http://localhost:5000")
            return True
        else:
            print(f"❌ Server responded with status code: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Server is not running or not accessible")
        return False
    except Exception as e:
        print(f"❌ Error testing server: {str(e)}")
        return False

def start_server():
    """Start the Flask server"""
    print("🚀 Starting the Question Answer Generator...")
    
    # Activate virtual environment and start server
    try:
        if os.name == 'nt':  # Windows
            activate_script = "question_generator_env\\Scripts\\activate.bat"
            cmd = f"cmd /c \"{activate_script} && python app.py\""
        else:  # Unix/Linux
            activate_script = "question_generator_env/bin/activate"
            cmd = f"source {activate_script} && python app.py"
        
        print("Starting server in background...")
        subprocess.Popen(cmd, shell=True)
        
        # Wait a moment for server to start
        print("Waiting for server to start...")
        time.sleep(5)
        
        # Test if server is running
        return test_server()
        
    except Exception as e:
        print(f"❌ Error starting server: {str(e)}")
        return False

def main():
    """Main function"""
    print("=" * 50)
    print("Question Answer Generator - Server Test")
    print("=" * 50)
    
    # First, test if server is already running
    if test_server():
        print("\n🎉 Server is already running!")
        print("🌐 Open your browser and go to: http://localhost:5000")
        return
    
    # If not running, try to start it
    print("\n🔄 Server not running, attempting to start...")
    if start_server():
        print("\n🎉 Server started successfully!")
        print("🌐 Open your browser and go to: http://localhost:5000")
    else:
        print("\n❌ Failed to start server")
        print("\nManual steps:")
        print("1. Open Command Prompt in this folder")
        print("2. Run: call question_generator_env\\Scripts\\activate.bat")
        print("3. Run: python app.py")
        print("4. Open browser: http://localhost:5000")

if __name__ == "__main__":
    main()

