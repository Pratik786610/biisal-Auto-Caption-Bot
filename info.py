# (c) @biisal
from os import getenv
import re

id_pattern = re.compile(r"^.\d+$")


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


ADMIN = int(getenv("ADMIN", "1691590963"))
API_ID = int(getenv("API_ID", "29712643"))
API_HASH = str(getenv("API_HASH", "159ec16a16e76a7f5e51d3c7e157e386"))
BOT_TOKEN = str(getenv("BOT_TOKEN", "6382750813:AAHyKt-0qmD4NxnzYcRhcGRziuB2DPBB1xs"))
MONGO_DB = str(
    getenv(
        "MONGO_DB",
        "mongodb+srv://anitasharma786610:<wUL6zJec6CwkGlkq>@pratikhero.pqpt7qx.mongodb.net/?retryWrites=true&w=majority&appName=Pratikhero",
    )
)
DEF_CAP = str(
    getenv(
        "DEF_CAP",
        "<b><a href='telegram.me/bisal_files'>{file_name} Telegram : @Bisal_Files\n\nForward the file before Downloading.</a></b>",
    )
)
