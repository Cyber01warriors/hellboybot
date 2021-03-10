class Translation(object):
    START_TEXT = """<b>Hey there, I am AnyDL Pro 👋\n\nPowered by @Infinity_BOTs. My owner is @ImJanindu 🇱🇰 \n\nI am a multipurpose all in one bot.\n\nDo /help for more infomation 😌</b>"""
    RENAME_403_ERR = "<b>❌ Sorry. You are not permitted to rename this file.</b>"
    ABS_TEXT = "<b>Please don't be selfish 😒</b>"
    UPGRADE_TEXT = "<b>For Free users contact @ImJanindu for upgrade plans 😌</b>"
    FORMAT_SELECTION = "<b>Select the desired file format you want: \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail 😇</b>"
    SET_CUSTOM_USERNAME_PASSWORD = """\nIf you want to download premium videos, provide in the following format:
URL | filename | username | password"""
    NOYES_URL = "<b>Slow URL detected. Please use https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, 🚀 without me slowing down for other users.</b>"
    DOWNLOAD_START = "<b>Downloading Started 😉</b>"
    UPLOAD_START = "<b>Download successful 😌 \nNow uploading. Please wait 🥺</b>"
    RCHD_BOT_API_LIMIT = "<b>Size greater than maximum allowed size (50MB). 🙄 Neverthless, trying to upload.</b>"
    RCHD_TG_API_LIMIT = "<b>Downloaded in {} seconds.\nDetected File Size: {}\nWTF 😬, I cannot upload files greater than 1.5GB due to Telegram API limitations 😒</b>"
    AFTER_SUCCESSFUL_UPLOAD_MSG = "<b>If you find this bot useful, please share with your friends and family. If any complaints contact @ImJanindu</b>"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "<b>Downloaded in {} seconds. \nUploaded in {} seconds. \n\nJoin our channel for bot updates @Infinity_BOTs</b>"
    NOT_AUTH_USER_TEXT = "<b>Please /upgrade your subscription.</b>"
    NOT_AUTH_USER_TEXT_FILE_SIZE = "<b>Detected File Size: {}. Free Users can only upload: {}\nPlease /upgrade your subscription.\nIf you think this is a bug, please contact <a href='https://telegram.dog/ImJanindu'>Janindu</a></b>"
    SAVED_CUSTOM_THUMB_NAIL = "<b>Custom video / file thumbnail saved. 🤗 This image will be used in the video / file.</b>"
    DEL_ETED_CUSTOM_THUMB_NAIL = "<b>✅ Custom thumbnail cleared succesfully.</b>"
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "<b>✅ Media cleared succesfully.</b>"
    SAVED_RECVD_DOC_FILE = "<b>Document Downloaded Successfully ✅</b>"
    CUSTOM_CAPTION_UL_FILE = ""
    NO_CUSTOM_THUMB_NAIL_FOUND = "<b>No Custom ThumbNail found 🤷‍♂️</b>"
    NO_VOID_FORMAT_FOUND = "<b>Do not fcuk !! 🤣\nYouTubeDL</b> said: {}"
    USER_ADDED_TO_DB = (
        "<b>User <a href='tg://user?id={}'>{}</a> added to {} till {}.</b>"
    )
    CURENT_PLAN_DETAILS = """<u>Current plan details</u>

Telegram ID: <code>{}</code>
Plan name: AnyDLProIBot User
Expires on: {}"""
    HELP_USER = """<u><b>There are multiple things I can do</b></u>

👉 <a href="https://t.me/SpEcHlDe/608">All Supported Video / File Formats, with custom file name and custom thumbnail support</a>
👉 <a href="https://t.me/SpEcHlDe/609">Upload as file from any HTTP link, with custom thumbnail support</a>
👉 Convert To Streamable Video, any Telegram file
👉 Convert To Telegram Audio, the media sent as Telegram Documents
👉 <a href="https://t.me/SpEcHlDe/610">ReName Telegram files, with custom thumbnail support</a>
👉 <a href="https://t.me/SpEcHlDe/625">Generate Custom Thumbnail by sending two photos in a Media Album</a>
👉 <a href="https://t.me/SpEcHlDe/653">Trim large videos</a>, and <a href="https://t.me/SpEcHlDe/652">Take Screenshots</a> of Telegram media files
👉 <a href="https://t.me/SpEcHlDe/657">Extract compressed Telegram media</a>
👉 <a href="https://t.me/SpEcHlDe/660">Get a Telegram sticker as a Telegram downloadable media</a>

Send /me to know current plan details"""
    REPLY_TO_DOC_GET_LINK = (
        "<b>Reply to a Telegram media or file to get slow download link 😬</b>"
    )
    REPLY_TO_DOC_FOR_C2V = (
        "<b>Reply to a Telegram media to convert that video to streamable 😌</b>"
    )
    REPLY_TO_DOC_FOR_SCSS = "<b>Reply to a Telegram media to get screenshots 👻</b>"
    REPLY_TO_DOC_FOR_RENAME_FILE = "<b>Reply to a Telegram media with new file name</b> \n<i>eg: /rename NewFile.mp4</i>"
    AFTER_GET_DL_LINK = "<b>Direct Link Generated! \n\nLink 👉 {} \n\nThis link valid for {} days.\n\n~ @TheMizukiBot 👸</b>"
    FF_MPEG_RO_BOT_RE_SURRECT_ED = """<b>Syntax: /trim HH:MM:SS [HH:MM:SS]</b>"""
    FF_MPEG_RO_BOT_STEP_TWO_TO_ONE = "<b>First send /downloadmedia to any media so that it can be downloaded to my local. \nSend /storageinfo to know the media, that is currently downloaded.</b>"
    FF_MPEG_RO_BOT_STOR_AGE_INFO = "<b>Video Duration: {}\nSend /clearffmpegmedia to delete this media, from my storage.\nSend /trim HH:MM:SS [HH:MM:SS] to cu[l]t a small photo / video, from the above media.</b>"
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "<b>A saved media already exists. Please send /storageinfo to know the current media details.</b>"
    USER_DELETED_FROM_DB = (
        "<b>User <a href='tg://user?id={}'>{}</a> deleted from DataBase.</b>"
    )
    REPLY_TO_DOC_OR_LINK_FOR_RARX_SRT = (
        "<b>Reply to a Telegram media (MKV), to extract embedded streams</b>"
    )
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = (
        "<b>Send your custom thumbail as compressed image. that enough 😜</b>"
    )
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "<b>Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album.</b>"
    INVALID_UPLOAD_BOT_URL_FORMAT = "<b>URL format is incorrect. make sure your url starts with either http:// or https://. You can set custom file name using the format link | file_name.extension</b>"
    ABUSIVE_USERS = "<b>Admins blocked you. 😂 Contact @ImJanindu</b>"
    FF_MPEG_RO_BOT_AD_VER_TISE_MENT = "https://telegram.dog/FFMpegRoBot"
    EXTRACT_ZIP_INTRO_ONE = (
        "<b>Send a compressed file first, Then reply /unzip command to the file.</b>"
    )
    EXTRACT_ZIP_INTRO_THREE = "<b>Analyzing received file. ⚠️ This might take some time. Please be patient.</b>"
    UNZIP_SUPPORTED_EXTENSIONS = ("zip", "rar")
    EXTRACT_ZIP_ERRS_OCCURED = "<b>Sorry. Errors occurred while processing compressed file. 🤒 Please check everything again twice, and if the issue persists, report this to <a href='https://telegram.dog/ImJanindu'>Janindu</a></b>"
    EXTRACT_ZIP_STEP_TWO = """Select file_name to upload from the below options.
You can use /rename command after receiving file to rename it with custom thumbnail support."""
    CANCEL_STR = "<b>Process Cancelled 🤒</b>"
    ZIP_UPLOADED_STR = "<b>Uploaded {} files in {} seconds 🥴</b>"
    FREE_USER_LIMIT_Q_SZE = """Cannot Process.
Free users only 1 request per 30 minutes.
/upgrade or Try 1800 seconds later."""
    G_DRIVE_GIVE_URL_TO_LOGIN = "Please login using {}. Send `/gsetup <YOUR CODE>`"
    G_DRIVE_SETUP_IN_VALID_FORMAT = "Send `/gsetup <YOUR CODE>`"
    G_DRIVE_SETUP_COMPLETE = "Logged In."
    SLOW_URL_DECED = "<b>Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users.</b>"
    IFLONG_FILE_NAME = """File Name limit allowed by Telegram is {alimit} characters.
The given file name has {num} characters.
<b>Essays Not allowed in Telegram file name!</b>
Please short your file name and try again!"""
