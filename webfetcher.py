from news import News
from selenium import webdriver
import os.path
import urllib.request

DRIVER_URL = "https://github.com/liceoArzignano/snake_bold/releases/download/PhantomJS/phantomjs"
DRIVER_PATH = "./phantomjs-snake"
FETCH_LIMIT = 5


def install_web_driver():
    if not os.path.exists(DRIVER_PATH):
        print("Downloading the webdriver...")
        urllib.request.urlretrieve(DRIVER_URL, DRIVER_PATH)

    # Mark as executable
    mode = os.stat(DRIVER_PATH).st_mode
    mode |= (mode & 0o444) >> 2
    os.chmod(DRIVER_PATH, mode)


def get_text(element):
    return element.text.replace("\"", "")


def fetch_row(row, is_private=False):
    item = News(is_private=is_private)
    columns = row.find_elements_by_xpath("td")

    for index, element in enumerate(columns):
        if index == 0:
            icon = element.find_element_by_css_selector("a")
            item.url = icon.get_attribute("href")
        elif index == 1:
            item.date = get_text(element)
        elif index == 2:
            item.number = int(get_text(element))
        elif index == 3:
            item.title = get_text(element)
        elif index == 4:
            item.message = get_text(element)

    return item


def fetch(is_private=False):
    print("Fetching " + (is_private and "private" or "public") + " data...")
    # Make sure web driver is available
    install_web_driver()

    fetched = []
    driver = webdriver.PhantomJS(DRIVER_PATH)
    # 10 minutes timeout
    driver.set_page_load_timeout(60 * 10)
    driver.get("http://www.liceoarzignano.it/" + (is_private and "comunicati" or "circolari") +
               "/appcircolaripub/ricerca.php?numero=0")

    # Read data from table
    table = driver.find_elements_by_xpath("//table[@class='mytable2']//tr")
    for index, row in enumerate(table):
        to_add = fetch_row(row, is_private)

        if to_add.number != -1:
            fetched.append(to_add)
        if index == FETCH_LIMIT:
            break

    driver.stop_client()
    return fetched
