import os
from app import app, init_db

def main():
    os.makedirs('data', exist_ok=True)
    os.makedirs('static', exist_ok=True)
    
    try:
        init_db()
        print("Database initialized successfully")
    except Exception as e:
        print(f"Database initialization error: {e}")
    
    app.run(host='0.0.0.0', port=5000, debug=True)

if __name__ == "__main__":
    main()
