import os
import random
list =[r'\'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36\'',r'\'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15\'',r'\'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36\'',r'\'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763\'',r'\'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko\'',r'\'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50\'',r'\'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11\'',r'\'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11\'']
a = random.choice(list)
def alter(file):    
  with open("%s.bak" % file, "w", encoding="utf-8") as f2:
      line = 'user_pref("general.useragent.override", {a_1});'.format(a_1=a)
      f2.write(line)
  os.remove(file)
  os.rename("%s.bak" % file, file)
alter(r'C:\Users\86180\AppData\Roaming\Mozilla\Firefox\Profiles\pagtvgjm.default-release-1627904794211\user.js')
