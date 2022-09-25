from requests_html import HTMLSession
import os
from bs4 import BeautifulSoup
import time
import requests
import cloudscraper
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as condition
# # from animepahe_downloader import get_episode_list, get_anime_size


# # # import animepahe_downloader 

# # os.environ['PATH'] += r"C:/Users/DELL/Downloads/webdriver"

# # browser = webdriver.Chrome()


# # def get_download_link(anime_link):
# #      anime_link = browser.get(anime_link)
# #      browser.implicitly_wait(5)
# #      anime_link = browser.page_source
# #      anime_soup = BeautifulSoup(anime_link, "html.parser")

# #      download_link_list = []
# #      download_link_quality = []
# #      download_link_size = []
     
# #      for link in anime_soup.find(id="pickDownload").find_all("a", class_="dropdown-item"):
# #           if link.find_all("span", class_="badge-warning") == []:
# #                for span in link.find_all("span", class_="badge"):
# #                     span.decompose()

# #                quality = link.text.split(" - ")[1].strip()
# #                size = quality[quality.index("(")+1:quality.index(")")]
# #                quality = quality[:quality.index(size)-1].strip()

# #                download_link_size.append(size)
# #                download_link_quality.append(quality)
# #                download_link_list.append(link.get("href"))

# #      print(download_link_size)
# #      print(download_link_quality)
# #      for link in download_link_list:
# #           print(link)
# #      download_link = dict(zip(download_link_quality, download_link_list))
# #      download_size = dict(zip(download_link_quality, download_link_size))

# #      return download_link, download_size


# # def download_anime_episode(anime_link):
# #      anime_link = browser.get(anime_link)
# #      browser.implicitly_wait(10)
# #      anime_link = browser.page_source
# #      anime_soup = BeautifulSoup(anime_link, "html.parser")

# #      WebDriverWait(browser, 10).until(
# #           condition.text_to_be_present_in_element((By.CLASS_NAME, "redirect"), "Continue"),
# #           condition.none_of(condition.text_to_be_present_in_element_attribute((By.CLASS_NAME, "redirect"), "href", "#pleasewait"))
# #      )

# #      download_link = browser.find_element(By.CSS_SELECTOR, "a.redirect").get_attribute("href")
# #      print(download_link)

# #      return download_link


# # def download_anime(download_link):
# #      download_link = browser.get(download_link)
# #      browser.implicitly_wait(10)
# #      download_link = browser.page_source
# #      anime_soup = BeautifulSoup(download_link, "html.parser")

# #      # WebDriverWait(browser, 10).until(
# #      #      condition.element_to_be_clickable((By.CSS_SELECTOR, "button.button"))
# #      # )

# #      download_button = browser.find_element(By.CSS_SELECTOR, "button.button")
# #      return download_button.submit()


# # def get_redirect_link(anime_link):
# #      """ Returns dictionaries of episode resolutions and respective links, 
# #      and episode resolutions and respective size.\n
# #      Note : Does not return link of dub anime if found """
     
# #      anime_link = browser.get(anime_link)
# #      browser.implicitly_wait(5)
# #      anime_link = browser.page_source
# #      anime_soup = BeautifulSoup(anime_link, "html.parser")

# #      download_link_list = []
# #      download_link_quality = []
# #      download_link_size = []

# #      print(anime_soup.select("#pickDownload a.disabled"))
# #      while download_link_quality == [] and anime_soup.select("#pickDownload a.disabled") != []:
# #           print(anime_soup.select("#pickDownload a.disabled"))
# #           print(anime_soup.select("#pickDownload .dropdown-item")["href"])
# #           WebDriverWait(browser, 30).until(
# #                condition.any_of(condition.presence_of_all_elements_located((By.CSS_SELECTOR, "#pickDownload .dropdown-item")),
# #                condition.element_attribute_to_include((By.CSS_SELECTOR, "#pickDownload a.dropdown-item"), "href"),
               
# #                condition.none_of(condition.presence_of_element_located((By.CSS_SELECTOR, "#pickDownload .disabled")),
# #                               condition.text_to_be_present_in_element((By.CSS_SELECTOR, "#pickDownload .dropdown-item"), "")
# #                )))   
          
# #           while anime_soup.select("#pickDownload .dropdown-item") == []:
# #                for link in anime_soup.find(id="pickDownload").find_all("a", class_="dropdown-item"):
# #                     WebDriverWait(browser, 30).until(
# #                          condition.none_of(condition.presence_of_element_located((By.CSS_SELECTOR, "#pickDownload .disabled")))
# #                     )
# #                     if link.find_all("span", class_="badge-warning") == []:
# #                          for span in link.find_all("span", class_="badge"):
# #                               span.decompose()

# #                          print(link)
# #                          quality = link.text.split(" - ")[1].strip()
# #                          size = quality[quality.index("(")+1:quality.index(")")]
# #                          quality = quality[:quality.index(size)-1].strip()

# #                     download_link_size.append(size)
# #                     download_link_quality.append(quality)
# #                     download_link_list.append(link.get("href"))

# #      # print(download_link_size)
# #      # print(download_link_quality)
# #      # for link in download_link_list:
# #      #      print(link)

# #      download_link = dict(zip(download_link_quality, download_link_list))
# #      download_size = dict(zip(download_link_quality, download_link_size))

# #      return download_link, download_size


# # # download_anime_episode("https://pahe.win/mkkFP")
# # # get_download_link("https://animepahe.com/play/9f2ad789-a310-9f00-0522-262e1c9e7d4e/9fa532b31ef0d8c99635c7a307ab8f2bd4cf6e80334117f44eb708f1f64b4e02")
# # # download_anime("https://kwik.cx/f/JDKsKQIpJL3V")


# # # wait for download complete

def wait(path):
     files = []
     path = r"c:\\Users\\DELL\\Downloads"
     dir = os.listdir(path)
     for file in dir:
          print(file)
          files.append(f"{path}\\{file}")

     files.sort(key=os.path.getmtime)
     files.reverse()
     print(files)
     for file in files[:len(episode_list)]:
          while True:
               if file.endswith('.crdownload'):
                    #   print('Downloading files...')
                    time.sleep(10)
               else:
                    break
     print("Download complete")
wait()

# # download_mode_input = """How would you like to download episodes? Enter:
# #      \t -r -> to download in a range of episodes ( -r 1, 12 ) 
# #      \t -l -> to download in a list of episodes ( -l 1, 3, 6, 10, 12 )
# #      \t -a -> to download all the episodes ( -a )
# # >> """
# # anime_name, episodes = get_episode_list("https://animepahe.com/anime/5c748ca8-b344-1cc6-0fbb-011de7049b67")
# # # download_link, download_size = get_download_link(anime_link)
# # while True:
# #      download_mode = input(download_mode_input).lower()
# #      time.sleep(1)

# #      episode_list = download_mode[2:].strip()
# #      download_mode = download_mode[:2].strip()

# #      download_quality_list = []
# #      download_size_list = []
# #      download_link_list = []

# #      total_download_size = 0

# #      match download_mode:
# #           case "-r":
# #                episode_list = episode_list.split(",")
# #                print(f"Downloading episodes from {episode_list[0]} to {episode_list[1].strip()}")
# #                for episode in range(int(episode_list[0]), int(episode_list[1])+1):
# #                     print(episodes[episode])
# #                     episode = episodes[episode]
# #                     download_link, download_size = get_redirect_link(episode)
# #                     size, download_quality = get_anime_size(download_size, download_link)
# #                     time.sleep(1)
# #                print(download_quality_list)
# #                print(download_size_list)
# #                print(download_link_list)
# #                break

# #           case "-l":
# #                episode_list = episode_list.split(",")
# #                print(f"Downloading episodes {episode_list}")
# #                for episode in episode_list:
# #                     episode = int(episode)
# #                     print(episodes[episode])
# #                     episode = episodes[episode]
# #                     download_link, download_size = get_redirect_link(episode)
# #                     size, download_quality = get_anime_size(download_size, download_link)
# #                     time.sleep(1)
# #                print(download_quality_list)
# #                print(download_size_list)
# #                print(download_link_list)
# #                break

# #           case "-a":
# #                print("Downloading all episodes")
# #                for episode in episodes.values():
# #                     print(episode)
# #                     download_link, download_size = get_redirect_link(episode)
# #                     size, download_quality = get_anime_size(download_size, download_link)
# #                     time.sleep(1)
# #                print(download_quality_list)
# #                print(download_size_list)
# #                print(download_link_list)
# #                break

# #           case default:
# #                print("Something went wrong. Try again")
# #                time.sleep(1)

# #      download_mode = input(download_mode_input)
# #      time.sleep(1)
# #      episode_list = download_mode[2:].strip()
# #      download_mode = download_mode[:2].strip()
# #      print(download_mode)

# #      match download_mode:
# #           case "-r":
# #                episode_list = episode_list.split(",")
# #                print(f"Downloading episodes from {episode_list[0]} to {episode_list[1].strip()}")
# #                for i in range(int(episode_list[0]), int(episode_list[1])+1):
# #                     pass
# #                break
# #           case "-l":
# #                episode_list = episode_list.split(",")
# #                print(f"Downloading episodes {episode_list}")
# #                for episode in episode_list:
# #                     pass
# #                break
# #           case "-a":
# #                print("Downloading all episodes")
# #                break
# #           case default:
# #                print("Something went wrong. Try again")
# #                time.sleep(1)



# # download_quality_list = []
# # download_size_list = []
# # download_link_list = []

# # def get_anime_size(download_size:dict, download_link:dict):
# #      """ Adds available quality for each episode to a list and makes a list of links """

# #      quality_list = []

# #      for quality in download_size.keys():
# #           quality_list.append(quality)
# #           if quality not in download_quality_list:
# #                download_quality_list.append(quality)

# #      download_quality = f"""What quality would you like to download for episode ? ( 720p )
# #           Available qualities : {quality_list}
# #      >> """
# #      download_quality = input(download_quality)
# #      try:
# #           size = download_size[download_quality]
# #           link = download_link[download_quality]
# #           print(size)
# #           download_size_list.append(size)
# #           download_link_list.append(link)
# #      except:
# #           print(f"{download_quality} not found")
     
# #      return size, download_quality

# # get_anime_size(download_size, download_link)
# # print(download_quality_list)
# # print(download_size_list)
# # print(download_link_list)


# size_list = ["80 mb", "93 mb", "102 mb", "1 gb", "200 mb", "2.9 gb"]

# def get_total_size(size_list:list):

#      size_value = []
#      size_number = []

#      for size in size_list:
#           size_value.append(size.split()[1].lower())
#           size_number.append(float(size.split()[0]))
#      size_dict = dict(zip(size_number, size_value))
#      print(size_dict)
#      mb = []
#      for size in size_dict.items():
#           match size[1]:
#                case "mb":
#                     mb.append(size[0])
#                     pass
#                case "gb":
#                     mb.append(size[0]*1024)
#                     pass
#                case "kilobytes":
#                     mb.append(size[0]/1024)
#                     pass
               
#      print(mb)

#      total_mb = 0

#      for m in mb:
#           total_mb += m
#      return total_mb

# total_mb = get_total_size(size_list)
# print(total_mb)