from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()
TableName = "MC_User"

def get_client() -> Client:
    url  = os.getenv("SUPABASE_URL")
    key  = os.getenv("SUPABASE_KEY")
    if not url or not key:
        raise EnvironmentError("SUPABASE_URL veya SUPABASE_KEY eksik.")
    return create_client(url, key)


# ─────────────────────────────────────────────────────────────────────────────────────────
# ── TUM KULLANCILARI ÇEK ──
# ─────────────────────────────────────────────────────────────────────────────────────────

def get_all_users() -> list[dict]:
    """Tüm kullanıcıları döndürür."""
    client = get_client()
    result = client.table("MC_User").select("*").order("id").execute()
    return result.data

# ─────────────────────────────────────────────────────────────────────────────────────────
# ── TUM HİSSE SENETLERİNİ ÇEK ──
# ─────────────────────────────────────────────────────────────────────────────────────────

def get_all_bist() -> list[dict]:
    """Tüm senetleri döndürür."""
    client = get_client()
    result = client.table("MC_BistList").select("*").order("id").execute()
    return result.data


# ─────────────────────────────────────────────────────────────────────────────────────────
# ── TUM TATİLLERİ ÇEK ──
# ─────────────────────────────────────────────────────────────────────────────────────────

def get_all_holidays() -> list[dict]:
    """Tüm tatilleri döndürür."""
    client = get_client()
    result = client.table("MC_Holidays").select("*").order("id").execute()
    return result.data


# ─────────────────────────────────────────────────────────────────────────────────────────
# ── AYAR_CEK──
# ─────────────────────────────────────────────────────────────────────────────────────────

# Dönüş tipini dict yerine str yapıyoruz
def get_set_by_key(key: str) -> str:
    """AYAR ÇEK"""
    client = get_client()
    result = client.table("MC_Settings").select("val").eq("key", key).execute()

    # result.data[0] yerine result.data[0]["val"] diyerek direkt içindeki değeri alıyoruz
    return result.data[0]["val"] if result.data else None


