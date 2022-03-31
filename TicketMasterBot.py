from selenium import webdriver
import time
import pywhatkit

#Url
pag = "https://www.ticketmaster.com.mx/bad-bunny-world-s-hottest-tour-mexico-11-12-2022/event/14005C3BF9D292C7"

#Sistem alerts with Whatsapp, You must be logged in WhatsAppWeb
def sen_alert_wsp(num):
    pywhatkit.sendwhatmsg_instantly(num, "Tickets Available ---> URL", 5, True, 1)

#Executable location
driver = webdriver.Chrome(executable_path=r"C:\Program Files\CHROME\chromedriver.exe")

driver.get(pag)
time.sleep(2)

#Accept Cookies
driver.find_element_by_id("onetrust-accept-btn-handler").click()

#Text to confirm (Switch to you lenguage, must be the SAME)
text_confirm = "Precio más bajo"
text_ldg = "Cargando..."
text_ldg_nc = " "

print("Loading...")

#Main while
w=0
while w == 0:
    #Wait while is charging
    while text_ldg == text_ldg_nc:
        text_ldg_nc = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/main/div/div/div[1]/div/div[1]/h2").text
        time.sleep(1)
    time.sleep(1)
    #Get text "Lowest Price" to know if are tickets available
    try:
        text = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/main/div/div/div[2]/div[1]/button[1]").text
        # If tickets are avilable, this step confirm it
        if text == text_confirm:
            sen_alert_wsp("+526666666666")
            sen_alert_wsp("+527777777777")
            sen_alert_wsp("+528888888888")
            print("Tickets Available")
            print("Alert send :)")
            time.sleep(2)
            #Clicked on the first showed tickets
            try:
                driver.find_element_by_id("quickpicks-list").click()
                print("Selected")
            except:
                print("Error")
                print("No selected")
            #Break main while, process sucess
            break
    #This except reload the page and wait 5s
    except:
        driver.refresh()
        text_ldg_nc = text_ldg
        print("Nothing yet")
        time.sleep(5)

# https://www.instagram.com/franciscovmag/