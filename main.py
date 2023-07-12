# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By

    driver = webdriver.Firefox()
    driver.get("https://www.trustnet.com/fund/price-performance/o/ia-unit-trusts-and-oeics?PageSize=50")
#    elem_list = driver.find_elements(By.CLASS_NAME,"fe_table--body")
    elem_list = driver.find_elements(By.CLASS_NAME,"funds-body/*")
#    elem_list = driver.find_elements(By.CLASS_NAME,"performace-table")
#    elem_list = driver.find_elements(By.ID, "fund - search - results - tabs - discrexeperformance")


    for elem in elem_list :
        data = elem.text
        print (data)
        data_lines = data.split("\n")
    driver.close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
