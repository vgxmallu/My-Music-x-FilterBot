class script(object):
    START_TXT = """Hey {} how are you:).
𝖨𝗆 𝖺 music 𝖿𝗂𝗅𝗍𝖾𝗋 𝖻𝗈𝗍 𝗐𝗁𝗂𝖼𝗁 𝖼𝖺𝗇 𝗉𝗋𝗈𝗏𝗂𝖽𝖾 Musics 𝗂𝗇 𝗒𝗈𝗎𝗋 𝗀𝗋𝗈𝗎𝗉𝗌.
just 𝖠𝖽𝖽 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉s+ 𝖺𝗇𝖽 𝗉𝗋𝗈𝗆𝗈𝗍𝖾 𝗆𝖾 𝖺𝗌 𝖺𝖽𝗆𝗂𝗇 𝗍𝗈 𝗅𝖾𝗍 𝗆𝖾 𝗀𝖾𝗍 𝗂𝗇 𝖺𝖼𝗍𝗂𝗈𝗇."""
    HELP_TXT = """
     Hey  {} 
Currently using free server so please Dont kill Me...
"""
    ABOUT_TXT = """<b>
× Real Owner of Repo: <a href=https://github.com/adi-code22>Eva-Maria</a>
× Lang: Python 3
× DB: Mongo DB
× Server: only Secret 👀</b>"""
    SOURCE_TXT = """<b>NOTE:</b>
- Music Filter x Bot  is a open source project. 
- Source - <ahref=https://github.com/adi-code22/EvaMaria>Click Here to get source code</a>

<b>DEVS:</b>
-<a href=https://github.com/adi-code22/EvaMaria>Eva</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>
- Filter is the feature were users can set automated replies for a particular keyword and shobana will respond whenever a keyword is found the message
<b>NOTE:</b>
1. This Bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- This Bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. This Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://github.com/mn-bots/ShobanaFilterBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """
<b>Add MUSIC'S to my DB</b>
    
1. Make me admin in your Group ✖️🎵.
2.and don't forward movie files. Audios only
3. If you want to save your musics to my Database, just forward last message to me, or copy the last message link from your music database channel and paste here.

/buggs to report my owner.
"""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of ShobanaFilterBot

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>
• /start - <code>Check I'm Alive.</code>
• /ping - <code>check ping.</code>
• /usage - <code>usage of bot.</code>
• /info - <code>User info .</code>
• /id - <code>User id  .</code>
• /broadcast - <code>Broadcast (owner only).</code>
"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
/logs - <code>to get the rescent errors</code>
/stats - <code>to get status of files in db.</code>
/delete - <code>to delete a specific file from db.</code>
/users - <code>to get list of my users and ids.</code>
/chats - <code>to get list of the my chats and ids </code>
/leave  - <code>to leave from a chat.</code>
/disable  -  <code>do disable a chat.</code>
/ban  - <code>to ban a user.</code>
/unban  - <code>to unban a user.</code>
/channel - <code>to get list of total connected channels</code>
/broadcast - <code>to broadcast a message to all users</code>
/ping - <code>check ping.</code>
/usage - <code>usage of bot.</code>
/delete| /deleteall - delete files 
/set_template
/setskip
"""

    
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 
 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> """
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    RESULT_TXT="""
<blockquote>Here is your {} audio 🎧</blockquote>"""

    CUSTOM_FILE_CAPTION = """
<pre>🎧 {file_name} | {file_size}</pre>
"""

    
    RESTART_GC_TXT = """
<b>𝖡𝗈𝗍 𝖱𝖾𝗌𝗍𝖺𝗋𝗍𝖾𝖽 !</b>

📅 𝖣𝖺𝗍𝖾 : <code>{}</code>
⏰ 𝖳𝗂𝗆𝖾 : <code>{}</code>
🌐 𝖳𝗂𝗆𝖾𝗓𝗈𝗇𝖾 : <code>Asia/Kolkata</code>
🛠️ 𝖡𝗎𝗂𝗅𝖽 𝖲𝗍𝖺𝗍𝗎𝗌 : <code>𝗏1 [ 𝖲𝗍able ]</code></b>"""
    
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
    SPOLL_NOT_FND="""<blockquote> Hi Sir</blockquote>
I couldn't find anything related to your request. 
Try reading the instruction below 👇🏼
    """
#SPELL CHECK LANGUAGES TO KNOW callback
    ENG_SPELL="""Please Note Below📓
    Ask in Correct Spelling
    """
    MAL_SPELL="""ദയവായി താഴെ ശ്രദ്ധിക്കുക
ശരിയായ അക്ഷരവിന്യാസത്തിൽ ചോദിക്കുക
    """
    HIN_SPELL="""
    👀👀👀
    """
    TAM_SPELL="""
   👀👀👀
    """

    CHK_MOV_ALRT="""♻️ Cheking files on my DB... ♻️"""
    
    OLD_MES="""Dont Click Old Message!!!"""
    
    MOV_NT_FND="""
<pre>Report To ADMIN BY USING /bugs command </pre> 
"""
    RESTART_TXT = """
<b><u>𝖡𝗈𝗍 𝖱𝖾𝗌𝗍𝖺𝗋𝗍𝖾𝖽 ✅</u></b>"""

