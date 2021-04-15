import cfscrape  # https://github.com/Anorov/cloudflare-scrape
import requests
from bs4 import BeautifulSoup as bs

from Mizuki.events import register


def dogbin(magnets):
    counter = 0
    urls = []
    while counter != len(magnets):
        message = magnets[counter]
        url = "https://del.dog/documents"
        r = requests.post(url, data=message.encode("UTF-8")).json()
        url = f"https://del.dog/{r['key']}"
        urls.append(url)
        counter += 1
    return urls


@register(pattern="^/torrent ?(.*)")
async def tor_search(event):
    if event.fwd_from:
        return
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
    }
    search_str = event.pattern_match.group(1)
    tahike = await event.reply("Searching for " + search_str + "...")
    if " " in search_str:
        search_str = search_str.replace(" ", "+")
        print(search_str)
        res = requests.get(
            "https://www.torrentdownloads.me/search/?new=1&s_cat=0&search="
            + search_str,
            headers,
        )
    else:
        res = requests.get(
            "https://www.torrentdownloads.me/search/?search=" + search_str, headers
        )
    source = bs(res.text, "lxml")
    urls = []
    magnets = []
    titles = []
    counter = 0
    for div in source.find_all("div", {"class": "grey_bar3 back_none"}):
        # print("https://www.torrentdownloads.me"+a['href'])
        try:
            title = div.p.a["title"]
            title = title[20:]
            titles.append(title)
            urls.append("https://www.torrentdownloads.me" + div.p.a["href"])
        except KeyError:
            pass
        except TypeError:
            pass
        except AttributeError:
            pass
        if counter == 15:
            break
        counter += 1
    if not urls:
        await tahike.edit("Either the Keyword was restricted or not found!")
        return
    for url in urls:
        res = requests.get(url, headers)
        # print("URl: "+url)
        source = bs(res.text, "lxml")
        for div in source.find_all("div", {"class": "grey_bar1 back_none"}):
            try:
                mg = div.p.a["href"]
                magnets.append(mg)
            except Exception:
                pass
    shorted_links = dogbin(magnets)
    msg = ""
    try:
        search_str = search_str.replace("+", " ")
    except BaseException:
        pass
    msg = (
        "**Torrent Search By Mizu**\n\nQuery: `{}`".format(search_str)
        + "\n\n**Results👇**\n\n"
    )
    counter = 0
    while counter != len(titles):
        msg = (
            msg
            + "➡️ [{}]".format(titles[counter])
            + "({})".format(shorted_links[counter])
            + "\n\n"
        )
        counter += 1
    await tahike.edit(msg, link_preview=False)
