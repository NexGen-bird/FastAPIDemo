from supabase import create_client, Client

SUPABASE_URL = "https://dvobjzoqovdrsuzhjnkf.supabase.co"  # From the Supabase Dashboard
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImR2b2Jqem9xb3ZkcnN1emhqbmtmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzIzNzY5MjUsImV4cCI6MjA0Nzk1MjkyNX0.YiMofxYQxrp4YjO3zdSB2pThHXY62KJRppmZLxaFGBo"  # From the API Settings

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def login_user(email: str, password: str):
    """Authenticate a user with Supabase."""
    try:
        response = supabase.auth.sign_in_with_password({"email": email, "password": password})
        return response
    except Exception as e:
        return {"error": str(e)}

def signup_user(email: str, password: str):
    """Register a new user in Supabase."""
    try:
        response = supabase.auth.sign_up({"email": email, "password": password})
        return response
    except Exception as e:
        return {"error": str(e)}
