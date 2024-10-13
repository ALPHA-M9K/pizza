# test_import.py

try:
    from app import app
    print("Successfully imported app")
except Exception as e:
    print(f"Failed to import app: {str(e)}")

if __name__ == "__main__":
    print("Running test_import.py")