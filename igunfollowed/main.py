from selenium import webdriver
from time import sleep


class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Accept All')]")\
            .click()
        sleep(2)
        ##self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]")\
        ##    .click()
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(2)

    def get_unfollowers(self):
        exceptionlist = ['leia_theprincesscollie','bi4all','tv4allbybi4all','lilianatenor','ogatoguinness','lisboa_antiga_insta','computermemes','diogobataguas', 'welinoo','creditoagricola',    'nomadstrails', 'salvadormartinha', 'cringeportugal', 'mensagem.lisboa', 'ruisineldecordes', 'bumbanafofinha', 'joanamarquespic', 'principio.meio.fim', 'guilhermercd', 'stevenwilsonhq', 'bilbiavids', 'bibliamtengarsada', '1843mag', 'goodreads', 'vhils', 'sciencestories_', 'computersciencelife', 'universeofprogrammers', 'alexandresantoscomedy', 'jornalexpresso', 'corpodormente', 'hugovanderding', 'unitednationshumanrights', 'perolasdaurgencia', 'frasesdem3rda', 'comunidadeculturaearte', 'o_unas', 'coderhumor', 'insoniascarvao', 'jjboce', 'nunomarkl', 'controlportugal', 'theeconomist', 'cristiano', 'influencersinthewild', 'reuters', 'python.learning', 'microsoft', 'bbcnews', 'nasa', 'anti.capitalist_','restaurante_picantone_5300','nintendopt']
        #self.driver.find_element_by_xpath("//a[contains(@href,'/{}')].format(self.username")\
        #    .click()
        self.driver.find_element_by_xpath("//a[contains(@href,'/danielcarodrigues')]")\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()
        following = self._get_names("following")
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
            .click()
        followers = self._get_names("followers")
        not_following_back = [user for user in following if user not in followers and user not in exceptionlist]
        print(not_following_back)

    def _get_names(self, type):
        #sugs = self.driver.find_element_by_xpath('//h4[contains(text(), Suggestions)]')
        #self.driver.execute_script('arguments[0].scrollIntoView()',sugs)
        exceptionlist = ['leia_theprincesscollie','bi4all','tv4allbybi4all','lilianatenor','ogatoguinness','lisboa_antiga_insta','computermemes','diogobataguas', 'welinoo','creditoagricola',    'nomadstrails', 'salvadormartinha', 'cringeportugal', 'mensagem.lisboa', 'ruisineldecordes', 'bumbanafofinha', 'joanamarquespic', 'principio.meio.fim', 'guilhermercd', 'stevenwilsonhq', 'bilbiavids', 'bibliamtengarsada', '1843mag', 'goodreads', 'vhils', 'sciencestories_', 'computersciencelife', 'universeofprogrammers', 'alexandresantoscomedy', 'jornalexpresso', 'corpodormente', 'hugovanderding', 'unitednationshumanrights', 'perolasdaurgencia', 'frasesdem3rda', 'comunidadeculturaearte', 'o_unas', 'coderhumor', 'insoniascarvao', 'jjboce', 'nunomarkl', 'controlportugal', 'theeconomist', 'cristiano', 'influencersinthewild', 'reuters', 'python.learning', 'microsoft', 'bbcnews', 'nasa', 'anti.capitalist_','restaurante_picantone_5300']
        sleep(1)
        if type == "following":
            scroll_box = self.driver.find_element_by_xpath("/html/body/div[6]/div/div/div[3]")
        else: 
            scroll_box = self.driver.find_element_by_xpath("/html/body/div[6]/div/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        #Idenify and click close button
        self.driver.find_element_by_xpath("/html/body/div[6]/div/div/div[1]/div/div[2]/button")\
            .click() 
        return names

my_bot = InstaBot('danielcarodrigues','dani1q2w#E$R')
my_bot.get_unfollowers()