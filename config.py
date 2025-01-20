# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "25591462")

API_HASH = os.environ.get("API_HASH", "859ee42e5484d205347ae73b20efb22a")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7974239885:AAFoAX3IB14YNrI2qy7ChXWjZrkyiKHZjKE") 

FORCE_SUB = os.environ.get("FORCE_SUB", "JICKOCREATION06") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "renamejcbot")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://Jicko:WAuVnX8IfVfqzCgr@cluster0.5r8yd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1762867976').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
