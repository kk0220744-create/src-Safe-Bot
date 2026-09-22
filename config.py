# safe_repo
# Note if you are trying to deploy on vps then directly fill values in (""
import os

API_HASH = "1b3fd2a65ece10471d24b90e9ae3163e"
API_ID = 39712114
BOT_TOKEN = "8672146337:AAFq-9xHqBL1CSWI0mJnKlfNNGtkIbCgLzk"
CHANNEL_ID = -1004299794278
LOG_GROUP = -1004448076989
CLONE_LOG_CHANNEL = -1004434809417
# Keep this channel private and add only admins/lifetime members.
PREMIUM_ARCHIVE_CHANNEL = int(os.environ.get("PREMIUM_ARCHIVE_CHANNEL") or CLONE_LOG_CHANNEL)
# Public channel where cloned media is also posted so users get an
# MX Player / VLC streamable link (t.me/Link09660/MSGID)
STREAM_CHANNEL = -1004398941102
STREAM_CHANNEL_USERNAME = "streamsafebro"
# Owner(s) of the bot. Keep as a list for filters.user compatibility.
OWNER_ID = [6749017641]

# MongoDB removed from this codebase; keep MONGO_DB for backwards compatibility
MONGO_DB = "mongodb+srv://TeleFlow:dbuserpassword.m@cluster0.er99jx9.mongodb.net/?appName=Cluster0"
