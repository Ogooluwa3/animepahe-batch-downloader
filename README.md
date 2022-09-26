# animepahe-downloader
animepahe-downloader is a python program that gets the download links and downloads animes from the [animepahe.com](https://animepahe.com) website.

## Requirements:
python3  
chromedriver web browser  
BeautifulSoup4  
Selenium  

```
pip install beautifulsoup4
pip install selenium
```

## Usage:
Download the program by typing in the terminal:  
```
git clone https://github.com/Ogooluwa3/animepahe-downloader.git
```  

Search for an anime and run the script from the terminal inside of the directory animepahe_downloader.py is located by typing:  
```
python animepahe_downloader.py  
```

### Usage Cont.
When promted, enter the link of the anime you want to download.

![This in an image](https://github.com/Ogooluwa3/animepahe-downloader/blob/master/Screenshots/1.png)

Enter a path to download the anime to. If the path does not exist, or a path is not provided, the program will use the default path.  
Default path is in the **Downloads** folder in the same directory as animepahe_downloader.py. The program will create folder if one does not exist.

![This in an image](https://github.com/Ogooluwa3/animepahe-downloader/blob/master/Screenshots/2.png)

From the list of episodes select how many episodes of the anime you want to download:  
- ``` -r x,y ``` downloads all episodes in a range from x to y (x and y inclusive)  
- ``` -l a,b,c,d,... ``` downloads episodes a, b, c, d,...  
- ``` -a ``` downloads all episodes of the anime  

![This in an image](https://github.com/Ogooluwa3/animepahe-downloader/blob/master/Screenshots/3.png)

![This in an image](https://github.com/Ogooluwa3/animepahe-downloader/blob/master/Screenshots/4.png)

Select the download quality for each of the episodes to be downloaded.  
This might take some time or the program might fail if the internet speed is slow.

![This in an image](https://github.com/Ogooluwa3/animepahe-downloader/blob/master/Screenshots/5.png)

Confirm if you still want to download the episodes or quit the program.  

![This in an image](https://github.com/Ogooluwa3/animepahe-downloader/blob/master/Screenshots/6.png)

Files are downloaded to the directory provided or the default directory.

![This in an image](https://github.com/Ogooluwa3/animepahe-downloader/blob/master/Screenshots/7.png)

