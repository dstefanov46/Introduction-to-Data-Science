"""
This file contains the libraries and helper functions needed to run the notebook 'Web_Scraping.ipynb'.
"""

# IMPORTING LIBRARIES
from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.options import Options
import json
import plotly.graph_objects as go
import networkx as nx
import matplotlib as mpl
import matplotlib.pyplot as plt

# FUNCTION DEFINITIONS
def run_webdriver(url):
    """
    :param url: string, this parameter represents the URL address of the webpage we'll be scraping
    :return driver: WebElement, provides us with access to the webpage we want to scrape
    """
    webdriver_location = 'C:/Users/User/Downloads/chromedriver'

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('user-agent:Dimitar-Stefanov')

    driver = webdriver.Chrome(webdriver_location, options=chrome_options)

    # Running the webdriver
    print(f"Retrieving the URL: '{url}'.")
    driver.get(url)

    return driver

def extraction_by_xpath_1(driver, xpath):
    """
    :param driver: WebElement, provides us with access to the webpage we want to scrape
    :param xpath: string, the path to the DOM element we want to retrieve
    :return text_list: list, contains the text of the children of the DOM element we scraped
    """
    webelements = driver.find_elements_by_xpath(xpath)
    text_list = []
    for el in webelements:
        text_list.append(el.get_attribute('innerText'))

    return text_list


def extraction_by_xpath_2(driver, xpath):
    """
    :param driver: WebElement, provides us with access to the webpage we want to scrape
    :param xpath: string, the path to the DOM element we want to retrieve
    :return text_list: list, contains the text of the children of the DOM element we scraped

    Note: The only difference between this function and the function extraction_by_xpath_1()
    is the fact that here in order to get the text from our elements, we use
    *.get_attribute('textContent') and not *.get_attribute('innerText').
    """
    webelements = driver.find_elements_by_xpath(xpath)
    text_list = []
    for el in webelements:
        text_list.append(el.get_attribute('textContent'))

    return text_list


def get_eng_descriptor(descriptor_list, eng_descriptor_list, slv_list):
    """
    :param descriptor_list: list, the 'Deskriptor' column from the stat_si table
    :param eng_descriptor_list: list, the 'Angleški deskriptor' column from the stat_si table
    :param slv_list: list, a list of names of activities in Slovene
    :return eng_list: list, a list with the names from slv_list translated to English
    """
    eng_list = []
    if type(slv_list) != list:
        slv_list = [slv_list]
    for name in slv_list:
        if name in descriptor_list:
            index_tmp = descriptor_list.index(name)
            eng_list.append(eng_descriptor_list[index_tmp])
        else:
            eng_list.append('')

    return eng_list


def create_list_of_dicts(codes_list, slv_list, eng_list):
    """
    :param codes_list: list, list with the codes of some activities
    :param slv_list: list, list with the Slovenian names of the activities whose codes we've provided in codes_list
    :param eng_list: list, list with the English names of the activities whose codes we've provided in codes_list
    :return list of dicts: list, as the name of the variable says it is a list of dicts, so it basically adds all three
                           lists provided as parameters into one dictionary
    """
    list_of_dicts = []
    for i in range(len(codes_list)):
        list_of_dicts.append({
            "code": codes_list[i],
            "slv": slv_list[i],
            "eng": eng_list[i]
        })

    return list_of_dicts

def get_children(driver, xpath, descriptor_list, eng_descriptor_list, layer):
    """
    :param driver: WebElement, provides us with access to the webpage we want to scrape
    :param xpath: string, the path to the DOM element we want to retrieve
    :param descriptor_list: list, the 'Deskriptor' column from the stat_si table
    :param eng_descriptor_list: list, the 'Angleški deskriptor' column from the stat_si table
    :param layer: int, the layer of the JSON schema in which we are trying to add the children
    :return (children, tmp_codes): tuple of a list and an int, the list contains our children and the integer tells us
                                   how many they are
    """
    children = []
    tmp_codes = extraction_by_xpath_1(driver, xpath + '/b')
    tmp_list = extraction_by_xpath_1(driver, xpath)
    tmp_list = [name for name in tmp_list if name != '']
    for i in range(len(tmp_codes)):
        tmp_list[i] = tmp_list[i].replace(tmp_codes[i] + ' ', '')
        if layer == 2:
            children.append({'code': tmp_codes[i], 'slv': tmp_list[i], 'children': []})
        else:
            children.append({'code': tmp_codes[i], 'slv': tmp_list[i]})

    for child in children:
        tmp_eng_descriptor = get_eng_descriptor(descriptor_list, eng_descriptor_list, child['slv'])
        if len(tmp_eng_descriptor) == 0:
            child['eng'] = ''
        else:
            child['eng'] = tmp_eng_descriptor[0]

    return children, tmp_codes


def get_num_activities(list_of_dicts):
    """
    :param list_of_dicts: list, list with dictionaries where each dictionary represents a category
    :return num_activities: list, list with the number of activities in each of the categories
    """
    num_activities = []
    for el in list_of_dicts:
        num_activities.append(len(el['children']))

    return num_activities

def get_names(list_of_dicts):
    """
    :param list_of_dicts: list, list with dictionaries where each dictionary represents a category
    :return names: list, list with the names of activities in each of the categories
    """
    names = []
    for el in list_of_dicts:
        names.append(el['slv'])

    return names

def get_codes(list_of_dicts):
    """
    :param list_of_dicts: list, list with dictionaries where each dictionary represents a category
    :return codes: list, list with the codes of the activities in each of the categories
    """
    codes = []
    for el in list_of_dicts:
        codes.append(el['code'])

    return codes

def get_categories_text(tmp_text, tmp_child, strings_copy, categories_of_text):
    """
    :param tmp_text: string, the text in the categories 'belongs', 'belongs too',etc. merged altogether in one string
    :param tmp_child: dict, dictionary representing the child, category currently being analyzed
    :param strings_copy: list, list of strings to search for in tmp_text
    :param categories_of_text: list, a list of the strings that represent the different categories of text
    :return tmp_child: dict, we return tmp_child, but now the text is sorted into the different categories 'belongs',
                       'belongs too', etc.
    """
    counter = 0

    if (len(strings_copy)) != 0:
        while (len(strings_copy) != 0):
            for m in range(len(strings_copy)):
                tmp_string = strings_copy[m]
                if tmp_string in tmp_text:
                    splitted_text = tmp_text.split(tmp_string)
                    if ((splitted_text[0] != '\n ') and (m == 0) and (counter == 0)):
                        tmp_child['text'] = splitted_text[0]
                    elif splitted_text[0] != '':
                        tmp_child[categories_of_text[old_found_string]] = splitted_text[0]
                    tmp_text = splitted_text[1]
                    old_found_string = tmp_string
                    strings_copy = strings_copy[m + 1:]
                    counter += 1
                    break

        tmp_child[categories_of_text[old_found_string]] = tmp_text

    return tmp_child

def reformat_belongs_text(belongs):
    """
    :param belongs: string, the text for the category 'belongs' with all '\n', 'xa0' characters and some unnecessary
                    backspaces
    :return list of dicts: list, this list makes sure the text in the category 'belongs' is correctly divided into
                           subcategories of type {'description':..., 'examples':...}
    """
    belongs = belongs.replace('\xa0', '').replace('·', '').split('\n ')
    belongs = [el for el in belongs if el != ' ']
    belongs = [el for el in belongs if el != '  ']

    indexes, description, examples = [], [], []
    for i in range(len(belongs)):
        if belongs[i][: 2] == '  ':
            belongs[i] = belongs[i][2:]
            if belongs[i][0] == ' ':
                belongs[i] = belongs[i][1:]

    belongs_final = []
    for el in belongs:
        if el[0] == ' ':
            belongs_final[-1] = belongs_final[-1] + el[2:]
        else:
            belongs_final.append(el)

    for i in range(len(belongs_final)):
        belongs_final[i] = belongs_final[i].strip(' ')

    for i in range(len(belongs_final)):
        for char in [' in ', ' ali ', ',', ':']:
            if char in belongs_final[i]:
                indexes.append(i)
                description.append(belongs_final[i])
                break

    for i in range(len(indexes)):
        if indexes[i] == indexes[-1]:
            examples.append(belongs_final[indexes[i] + 1:])
        else:
            examples.append(belongs_final[indexes[i] + 1: indexes[i + 1]])

    list_of_dicts = []
    for i in range(len(indexes)):
        list_of_dicts.append({'description': belongs_final[indexes[i]], 'examples': examples[i]})

    for el in list_of_dicts:
        if len(el['examples']) == 0:
            del el['examples']

        if ':' in el['description']:
            el['description'] = el['description'].replace(':', '')

    return list_of_dicts


def reformat_not_belong_text(not_belong):
    """
    :param not_belong: string, the text for the category 'doesn't belong' with all '\n', 'xa0' characters, some unnecessary
                    backspaces, ...
    :return list of dicts: list, this list makes sure the text in the category 'doesn't belong' is correctly divided
                           into subcategories of type {'description':..., 'code':...}
    """
    not_belong = not_belong.replace('\n', '').replace('\xa0', '').replace('·', '').split(' ')
    not_belong = [el for el in not_belong if el != '']
    not_belong = [el for el in not_belong if el != 'gl.']

    not_belong_new = []
    codes = []
    indexes = []
    for el in not_belong:
        try:
            if type(int(el[0])) == int:
                codes.append(el)
                indexes.append(not_belong.index(el))
        except ValueError:
            pass

    for i in range(len(indexes)):
        if i == 0:
            not_belong_new.append(not_belong[: indexes[i]])
        else:
            not_belong_new.append(not_belong[indexes[i - 1] + 1: indexes[i]])

    not_belong_final = []
    for el in not_belong_new:
        try:
            tmp_word = el[0]
            for i in range(1, len(el)):
                tmp_word += ' ' + el[i]
            tmp_word = tmp_word.strip(',')
            not_belong_final.append(tmp_word)
        except IndexError:
            pass

    list_of_dicts = []
    try:
        for i in range(len(codes)):
            list_of_dicts.append({'description': not_belong_final[i], 'code': codes[i]})
    except IndexError:
        pass

    return list_of_dicts


def reformat_surs_text(surs):
    """
    :param surs: string, the text for the category 'SURS puts here' with all '\n', 'xa0' characters, some unnecessary
                    backspaces, ...
    :return surs_final: list, a list of the activities under the category 'SURS puts here'; so, as a parameter to the
                        function, we get all these activities merged into one string, and the function returns a list
                        of all of them separately
    """
    surs = surs.replace('\xa0', '').replace('·', '').split('\n ')
    surs = [el for el in surs if el != ' ']
    surs = [el for el in surs if el != '  ']

    for i in range(len(surs)):
        surs[i] = surs[i][2:]
        if surs[i][0] == ' ':
            surs[i] = surs[i][3:]

    surs_final = []
    for el in surs:
        if el[0] == ' ':
            surs_final[-1] = surs_final[-1] + el
        else:
            surs_final.append(el)

    for i in range(len(surs_final)):
        surs_final[i] = surs_final[i].strip(' ')

    return surs_final


def reformat_text(tmp_child):
    """
    :param tmp_child: dict, a dictionary representing the child, category currently being analyzed
    :return tmp_child: dict, the same dict we received as a parameter, but now we've applied on it all of the text
                       formatting functions above, plus made some extra checks on some keys in the dict
    """
    if 'belongs' in tmp_child.keys():
        tmp_child['belongs'] = reformat_belongs_text(tmp_child['belongs'])
    if 'belongs too' in tmp_child.keys():
        tmp_child['belongs too'] = reformat_surs_text(tmp_child['belongs too'])
    if "doesn't belong" in tmp_child.keys():
        tmp_child["doesn't belong"] = reformat_not_belong_text(tmp_child["doesn't belong"])
    if 'SURS puts here' in tmp_child.keys():
        tmp_child["SURS puts here"] = reformat_surs_text(tmp_child["SURS puts here"])
    if 'text' in tmp_child.keys():
        if tmp_child['text'] == '\n ':
            del tmp_child['text']
        else:
            tmp_child['text'] = tmp_child['text'].replace('\n', '').replace('\xa0', '').strip(' ')
    if 'conditions' in tmp_child.keys():
        tmp_child['conditions'] = tmp_child['conditions'].replace(' \n', '').replace('\xa0', '').strip(' ')

    return tmp_child

def create_conn_graph(codes_3_layer, n_connections):
    """
    :param codes_3_layer: dict, dictionary containing the number of connections for each activity in the 3rd layer
    :param n_connections: int, the lower bound for selecting an activity to be represented in the graph
    :return: there is no return value, but we plot the connection graph
    """
    # Select only activities with more or equal connections to 'n_connections'
    selected_nodes = {}
    for key in codes_3_layer.keys():
        if len(codes_3_layer[key]) >= n_connections:
            selected_nodes[key] = codes_3_layer[key]

    # Create the connection graph for the selected activities
    G = nx.DiGraph()

    G.add_nodes_from(selected_nodes.keys())
    for key in selected_nodes.keys():
        G.add_edges_from(selected_nodes[key])

    pos = nx.layout.spring_layout(G)

    plt.figure(figsize=[15, 10])

    nx.draw_networkx_nodes(G, pos, node_size=1200, node_color="yellow")

    nx.draw_networkx_edges(
        G,
        pos,
        node_size=1200,
        arrowstyle="->",
        arrowsize=10,
        edge_color="black",
        width=3
    )

    labels = {}
    for node in G.nodes:
        labels[node] = node

    nx.draw_networkx_labels(G, pos, labels, font_size=10)

    plt.show()

