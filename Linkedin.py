import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
result = False

def  Identifiant(driver,mail,MDP,prenom,nom):
    ##########################################################################
    # find la zone de saisie de l'input email
    email = driver.find_element(By.NAME, 'email-address')
    # find la zone de saisie de l'input password
    password = password = driver.find_element(By.NAME, "password")
    # find la zone de saisie de l'input nom
    lastName = driver.find_element(By.NAME, "last-name")
    # find la zone de saisie de l'input prénom
    firstName = driver.find_element(By.NAME, "first-name")
    # boutton pour changer de page
    buttonAccept = driver.find_element(By.ID, 'join-form-submit')
    ##########################################################################
    #saisie de l'email
    time.sleep(random.randint(1, 5))
    email.send_keys(mail)
    time.sleep(random.randint(1, 5))
    password.send_keys(MDP)
    time.sleep(random.randint(1, 5))
    buttonAccept.click()
    time.sleep(random.randint(1, 5))
    firstName.send_keys(prenom)
    time.sleep(random.randint(1, 5))
    lastName.send_keys(nom)
    time.sleep(random.randint(1, 5))
    buttonAccept.click()
    time.sleep(random.randint(1, 5))
    ###########################################################################

saisieEmail = input('saisie du mail : ')
saisiePassword = input('saisie du mot de passe : ')
saisiePrenom = input('saisie du prénom : ')
saisieNom = input('saisie du nom : ')
saisieNumero = input('saisie du numéro de téléphone : ')
while result == False:
    try:
        #accès a la page d'inscription de linkedin
        driver = webdriver.Chrome()
        driver.get("https://www.linkedin.com/signup/cold-join?trk=guest_homepage-basic_nav-header-join")
        ###########################################################################
        Identifiant(driver, saisieEmail, saisiePassword, saisiePrenom, saisieNom)
        ###########################################################################
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@title='Vérification de sécurité']"))
        time.sleep(random.randint(1, 5))
        phone = driver.find_element(By.NAME, 'phoneNumber')
        time.sleep(random.randint(1, 5))
        phone.send_keys(saisieNumero)
        time.sleep(random.randint(1, 5))
        goodPhone = driver.find_element(By.ID, 'register-phone-submit-button')
        goodPhone.click()
        time.sleep(random.randint(1, 5))
        pin = driver.find_element(By.NAME, 'pin')
        saisiePin = input('saisir le pin reçu : ')
        time.sleep(random.randint(1, 5))
        pin.send_keys(saisiePin)
        registerPhone = driver.find_element(By.ID, 'register-phone-submit-button')
        registerPhone.click()
        driver.close()
        ###########################################################################
        result = True
    except:
        driver.close()
        result = False