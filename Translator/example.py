from googletrans import Translator #import the package
trans = Translator() #initialize the object
chinese = trans.translate('你好') #'hello' in madarin
print(chinese.text) #prints the enlgish text