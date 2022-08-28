# This is auto translate program by hao
# remember to use 'pip install googletrans==4.0.0-rc1'
# command to install,other version will bug
from googletrans import Translator

translator = Translator()
msg = translator.translate("hallo Welt", dest='en')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(msg.text)

