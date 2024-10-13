# test_import.py

try:
    from app import app  # Attempt to import the Flask app
    print("Successfully imported app")  # Indicate successful import
except Exception as e:
    print(f"Failed to import app: {str(e)}")  # Handle import failure

if __name__ == "__main__":
    print('Running test_import.py')  # Indicate that the test script is running
