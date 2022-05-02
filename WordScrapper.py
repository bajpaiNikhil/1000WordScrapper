import asyncio
import datetime

import bs4
import httpx

print("Iamstupid")


def main():
    t0 = datetime.datetime.now()

    asyncio.run(get_title_range())
    dt = datetime.datetime.now() - t0
    print(f"done in {dt.total_seconds():.4f} sec")


async def get_title_range():
    task = []
    for i in range(1, 2):
        task.append((i, asyncio.create_task(get_html())))

    for n, t in task:
        html = await t
        title = get_title(html)
        print(f"Title found: {title}", flush=True)


async def get_html():
    url = 'https://gonaturalenglish.com/1000-most-common-words-in-the-english-language/'
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, follow_redirects=True)
        resp.raise_for_status()
        # print(resp.text)
        return resp.text


def get_title(html: str) -> list:
    list_words = []
    count = 0
    file_word_list = open("wordList.txt", "w")
    soup = bs4.BeautifulSoup(html, 'html.parser')
    header = soup.find_all("div", class_="thecontent")
    print()
    for job_elements in header:
        words = job_elements.find_all("ol")
        for word in words:
            for items in word.find_all("li"):
                item = items.text.strip()
                # print(item.index(" "), item , item[:item.index(" ")])
                wordIs = item[:item.index(" ")]
                count += 1
                if count > 3:
                    file_word_list.writelines(wordIs+"\n")
                # if "\xa0" not in i[0] and "\xa0-" not in i[0]:
                #     print(i[0], "good")
                # if
                # itemAfterSplit = item.split(" ")
                # print(itemAfterSplit , ' -' in itemAfterSplit)
                # # print(itemAfterSplit[0], " ".join(itemAfterSplit[2:]) , count )
                # item_dict[word] = itemAfterSplit[0]
                # item_dict[word] = " ".join(itemAfterSplit[2:])
                # dict_word[count] = item_dict
                # count += 1
                # dict_word["word"] = itemAfterSplit[0]
                # dict_word["example"] = " ".join(itemAfterSplit[2:])
                list_words.append(item)
    file_word_list.close()
    return list_words[3:]


if __name__ == '__main__':
    main()
