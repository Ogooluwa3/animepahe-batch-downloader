import os
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as condition


os.environ['PATH'] += os.getcwd()+"/webdriver"
default_path = os.getcwd() + "\\Downloads"



anime_link = """Enter link of anime you want to download ( https://animepahe.com/anime/fed10c05-86b4-c0ea-93ae-6c03a4ab21c1 )
>> """
download_path = """Enter path you want to download anime to ( C:/Users/DELL/Downloads )
>> """
anime_link = input(anime_link)
download_path = input(download_path)
time.sleep(1)

if download_path.strip() != "" and os.path.exists(download_path) == True:
     path = download_path
     print(f"Downloading to {download_path}")
     chrome_options = webdriver.ChromeOptions()
     # chrome_options.headless = True
     prefs = {'download.default_directory' : download_path}
     chrome_options.add_experimental_option('prefs', prefs)
     browser = webdriver.Chrome(chrome_options=chrome_options)
else:
     try:
          os.mkdir(default_path)
     except:
          pass

     path = default_path
     print("Invalid path")
     print("Using default path...")
     print(f"Downloading to {default_path}")
     chrome_options = webdriver.ChromeOptions()
     # chrome_options.headless = True
     prefs = {'download.default_directory' : default_path}
     chrome_options.add_experimental_option('prefs', prefs)
     browser = webdriver.Chrome(chrome_options=chrome_options)
     # browser = webdriver.Chrome()


def get_episode_list(anime_link):
     """ Returns anime name and dictionary of anime episodes and respective links """
     
     anime_link = browser.get(anime_link)
     browser.implicitly_wait(10)
     anime_link = browser.page_source
     anime_soup = BeautifulSoup(anime_link, 'html.parser')
     
     episode_number_list = []
     episode_link_list = []

     anime_name = anime_soup.select_one(".title-wrapper h1 span").text

     
     while episode_number_list == []:
          WebDriverWait(browser, 100).until(
               condition.any_of(
               condition.presence_of_all_elements_located((By.CSS_SELECTOR, ".episode-number")),
               condition.none_of(condition.text_to_be_present_in_element((By.CSS_SELECTOR, ".episode-number"), ""))
          ))
          for number in anime_soup.find_all(class_="episode-number"):
               number = int(number.contents[1])
               episode_number_list.append(number)
               
          for link in anime_soup.find_all("a", class_="play"):
               if link.get("href").startswith("https://animepahe.com"):
                    episode_link_list.append(link.get("href"))
                    
               elif link.get("href").startswith("animepahe.com"):
                    link = link.get("href")
                    link = "https://" + link
                    episode_link_list.append(link)

               else:
                    link = link.get("href")
                    link = "https://animepahe.com" + link
                    episode_link_list.append(link)
          
     episodes = dict(zip(episode_number_list, episode_link_list))
     print(f"Name of anime : {anime_name}")
     print(f"List of episodes : {episode_number_list}")

     return anime_name, episodes


def get_redirect_link(anime_link):
     """ Returns dictionaries of episode resolutions and respective links, 
     and episode resolutions and respective size.\n
     Note : Does not return link of dub anime if found """
     
     anime_link = browser.get(anime_link)
     browser.implicitly_wait(5)
     anime_link = browser.page_source
     anime_soup = BeautifulSoup(anime_link, "html.parser")

     download_link_list = []
     download_link_quality = []
     download_link_size = []

     WebDriverWait(browser, 30).until(
          condition.all_of(
          condition.presence_of_all_elements_located((By.CSS_SELECTOR, "#pickDownload .dropdown-item")),
          condition.element_attribute_to_include((By.CSS_SELECTOR, "#pickDownload a.dropdown-item"), "href"),
          
          condition.none_of(condition.presence_of_all_elements_located((By.CSS_SELECTOR, "#pickDownload .disabled")),
                         # condition.text_to_be_present_in_element((By.CSS_SELECTOR, "#pickDownload .dropdown-item"), "")
     )))

     while download_link_quality == [] :

          WebDriverWait(browser, 30).until(
               condition.all_of(
               condition.presence_of_all_elements_located((By.CSS_SELECTOR, "#pickDownload .dropdown-item")),
               condition.element_attribute_to_include((By.CSS_SELECTOR, "#pickDownload a.dropdown-item"), "href"),
               
               condition.none_of(condition.presence_of_all_elements_located((By.CSS_SELECTOR, "#pickDownload .disabled")),
                              # condition.text_to_be_present_in_element((By.CSS_SELECTOR, "#pickDownload .dropdown-item"), "")
          )))   
          time.sleep(1)
          for link in anime_soup.find(id="pickDownload").find_all("a", class_="dropdown-item"):
               WebDriverWait(browser, 30).until(
                    condition.all_of(
                    condition.presence_of_all_elements_located((By.CSS_SELECTOR, "#pickDownload .dropdown-item span")),
                    condition.none_of(condition.presence_of_all_elements_located((By.CSS_SELECTOR, "#pickDownload .disabled")))
               ))
               if anime_soup.select("#pickDownload .disabled") == []:
                    if link.find_all("span", class_="badge-warning") == []:
                         for span in link.find_all("span", class_="badge"):
                              span.decompose()

                         print(link.text)
                         quality = link.text.split(" - ")[1].strip()
                         size = quality[quality.index("(")+1:quality.index(")")]
                         quality = quality[:quality.index(size)-1].strip()

                    download_link_size.append(size)
                    download_link_quality.append(quality)
                    download_link_list.append(link.get("href"))
          # break

     download_link = dict(zip(download_link_quality, download_link_list))
     download_size = dict(zip(download_link_quality, download_link_size))

     return download_link, download_size


def get_download_link(anime_link):
     """ Returns the download link for the anime """
     
     anime_link = browser.get(anime_link)
     browser.implicitly_wait(10)
     anime_link = browser.page_source
     anime_soup = BeautifulSoup(anime_link, "html.parser")

     WebDriverWait(browser, 10).until(
          condition.all_of(
          condition.text_to_be_present_in_element((By.CLASS_NAME, "redirect"), "Continue"),
          condition.none_of(condition.text_to_be_present_in_element_attribute((By.CLASS_NAME, "redirect"), "href", "#pleasewait"))
     ))

     download_link = browser.find_element(By.CSS_SELECTOR, "a.redirect").get_attribute("href")

     return download_link


def download_anime(download_link):
     """ Downloads the anime """
     
     download_link = browser.get(download_link)
     browser.implicitly_wait(10)
     download_link = browser.page_source

     # WebDriverWait(browser, 10).until(
     #      condition.element_to_be_clickable((By.CSS_SELECTOR, "button.button"))
     # )

     download_button = browser.find_element(By.CSS_SELECTOR, "button.button")
     return download_button.submit()


def get_anime_size(download_size:dict, download_link:dict):
     """ Adds available quality for each episode to a list and makes a list of links """

     quality_list = []

     for quality in download_size.keys():
          quality_list.append(quality)
          if quality not in download_quality_list:
               download_quality_list.append(quality)

     download_quality_ = f"""What quality would you like to download for episode {list(episodes.keys())[list(episodes.values()).index(episode)]}? ( 720p )
          Available qualities : {quality_list}
     >> """
     while True:
          download_quality = input(download_quality_)
          try:
               size = download_size[download_quality]
               link = download_link[download_quality]
               print(f"File size : {size}")
               download_size_list.append(size)
               download_link_list.append(link)
               break
          except:
               print(f"{download_quality} not found")
     
     return size, download_quality


def get_total_size(size_list:list):
     
     size_value = []
     size_number = []

     for size in size_list:
          size_value.append(size.split()[1].lower())
          size_number.append(float(size.split()[0]))
     size_dict = dict(zip(size_number, size_value))
     mb = []
     for size in size_dict.items():
          match size[1]:
               case "mb":
                    mb.append(size[0])
                    pass
               case "gb":
                    mb.append(size[0]*1024)
                    pass
               case "kilobytes":
                    mb.append(size[0]/1024)
                    pass
               
     print(mb)

     total_mb = 0

     for m in mb:
          total_mb += m
     return total_mb


# browser.quit()


anime_name, episodes = get_episode_list(anime_link)

download_mode_input = """How would you like to download episodes? Enter:
     \t -r -> to download in a range of episodes ( -r 1, 12 ) 
     \t -l -> to download in a list of episodes ( -l 1, 3, 6, 10, 12 )
     \t -a -> to download all the episodes ( -a )
>> """
time.sleep(5)

while True:
     download_mode = input(download_mode_input).lower()
     time.sleep(1)

     episode_list = download_mode[2:].strip()
     download_mode = download_mode[:2].strip()

     download_quality_list = []
     download_size_list = []
     download_link_list = []

     total_download_size = 0

     match download_mode:
          case "-r":
               episode_list = episode_list.split(",")
               print(f"Downloading episodes from {episode_list[0]} to {episode_list[1].strip()}")
               for episode in range(int(episode_list[0]), int(episode_list[1])+1):
                    episode = episodes[episode]
                    download_link, download_size = get_redirect_link(episode)
                    size, download_quality = get_anime_size(download_size, download_link)
                    
               total_download_size = get_total_size(download_size_list)
               print(f"Total download size : {total_download_size} mb")
               break

          case "-l":
               episode_list = episode_list.split(",")
               print(f"Downloading episodes {episode_list}")
               for episode in episode_list:
                    episode = int(episode)
                    episode = episodes[episode]
                    download_link, download_size = get_redirect_link(episode)
                    size, download_quality = get_anime_size(download_size, download_link)
                    
               total_download_size = get_total_size(download_size_list)
               print(f"Total download : {total_download_size}")
               break

          case "-a":
               print("Downloading all episodes")
               for episode in episodes.values():
                    download_link, download_size = get_redirect_link(episode)
                    size, download_quality = get_anime_size(download_size, download_link)
                    
               total_download_size = get_total_size(download_size_list)
               print(f"Total download : {total_download_size}")
               break

          case default:
               print("Something went wrong. Try again")
               time.sleep(1)



def download_user_anime(download_link_list:list):
     while True:
          continue_download = input("Continue download? (y/n) \n>> ").lower()
          match continue_download:
               case "y":
                    for link in download_link_list:
                         download_link = get_download_link(link)
                         print(download_link)
                         download_anime(download_link)
                    browser.get("chrome://downloads/")
                    wait(path)
                    break
               case "n":
                    print("Quitting browser")
                    browser.quit()
                    break
               case default:
                    continue


def wait(path):
     wait = True
     while wait == True:
          files = []
          downloading_files = []
          dir = os.listdir(path)
          for file in dir:
               files.append(f"{path}\\{file}")

          files.sort(key=os.path.getmtime)
          files.reverse()
          print(files)
          for file in files[:len(episode_list)]:
               if file.endswith('.crdownload'):
                    #   print('Downloading files...')
                    downloading_files.append(file)
                    time.sleep(10)
               else:
                    pass
          if downloading_files == []:
               wait = False
     print("Download complete")
     time.sleep(10)
     browser.quit()


download_user_anime(download_link_list)