from bs4 import BeautifulSoup
import urllib
import string
import urllib2
import json

dic=[' a ', ' able ', ' about ', ' above ', ' abst ', ' accordance ', ' according ', ' accordingly ', ' across ', ' act ', ' actually ', ' added ', ' adj ', ' affected ', ' affecting ', ' affects ', ' after ', ' afterwards ', ' again ', ' against ', ' ah ', ' all ', ' almost ', ' alone ', ' along ', ' already ', ' also ', ' although ', ' always ', ' am ', ' among ', ' amongst ', ' an ', ' and ', ' announce ', ' another ', ' any ', ' anybody ', ' anyhow ', ' anymore ', ' anyone ', ' anything ', ' anyway ', ' anyways ', ' anywhere ', ' apparently ', ' approximately ', ' are ', ' aren ', ' arent ', ' arise ', ' around ', ' as ', ' aside ', ' ask ', ' asking ', ' at ', ' auth ', ' available ', ' away ', ' awfully ', ' b ', ' back ', ' be ', ' became ', ' because ', ' become ', ' becomes ', ' becoming ', ' been ', ' before ', ' beforehand ', ' begin ', ' beginning ', ' beginnings ', ' begins ', ' behind ', ' being ', ' believe ', ' below ', ' beside ', ' besides ', ' between ', ' beyond ', ' biol ', ' both ', ' brief ', ' briefly ', ' but ', ' by ', ' c ', ' ca ', ' came ', ' can ', ' cannot ', " can't ", ' cause ', ' causes ', ' certain ', ' certainly ', ' co ', ' com ', ' come ', ' comes ', ' contain ', ' containing ', ' contains ', ' could ', ' couldnt ', ' d ', ' date ', ' did ', " didn't ", ' different ', ' do ', ' does ', " doesn't ", ' doing ', ' done ', " don't ", ' down ', ' downwards ', ' due ', ' during ', ' e ', ' each ', ' ed ', ' edu ', ' effect ', ' eg ', ' eight ', ' eighty ', ' either ', ' else ', ' elsewhere ', ' end ', ' ending ', ' enough ', ' especially ', ' et ', ' et-al ', ' etc ', ' even ', ' ever ', ' every ', ' everybody ', ' everyone ', ' everything ', ' everywhere ', ' ex ', ' except ', ' f ', ' far ', ' few ', ' ff ', ' fifth ', ' first ', ' five ', ' fix ', ' followed ', ' following ', ' follows ', ' for ', ' former ', ' formerly ', ' forth ', ' found ', ' four ', ' from ', ' further ', ' furthermore ', ' g ', ' gave ', ' get ', ' gets ', ' getting ', ' give ', ' given ', ' gives ', ' giving ', ' go ', ' goes ', ' gone ', ' got ', ' gotten ', ' h ', ' had ', ' happens ', ' hardly ', ' has ', " hasn't ", ' have ', " haven't ", ' having ', ' he ', ' hed ', ' hence ', ' her ', ' here ', ' hereafter ', ' hereby ', ' herein ', ' heres ', ' hereupon ', ' hers ', ' herself ', ' hes ', ' hi ', ' hid ', ' him ', ' himself ', ' his ', ' hither ', ' home ', ' how ', ' howbeit ', ' however ', ' hundred ', ' i ', ' id ', ' ie ', ' if ', " i'll ", ' im ', ' immediate ', ' immediately ', ' importance ', ' important ', ' in ', ' inc ', ' indeed ', ' index ', ' information ', ' instead ', ' into ', ' invention ', ' inward ', ' is ', " isn't ", ' it ', ' itd ', " it'll ", ' its ', ' itself ', " i've ", ' j ', ' just ', ' k ', ' keep ', ' keeps ', ' kept ', ' kg ', ' km ', ' know ', ' known ', ' knows ', ' l ', ' largely ', ' last ', ' lately ', ' later ', ' latter ', ' latterly ', ' least ', ' less ', ' lest ', ' let ', ' lets ', ' like ', ' liked ', ' likely ', ' line ', ' little ', " 'll ", ' look ', ' looking ', ' looks ', ' ltd ', ' m ', ' made ', ' mainly ', ' make ', ' makes ', ' many ', ' may ', ' maybe ', ' me ', ' mean ', ' means ', ' meantime ', ' meanwhile ', ' merely ', ' mg ', ' might ', ' million ', ' miss ', ' ml ', ' more ', ' moreover ', ' most ', ' mostly ', ' mr ', ' mrs ', ' much ', ' mug ', ' must ', ' my ', ' myself ', ' n ', ' na ', ' name ', ' namely ', ' nay ', ' nd ', ' near ', ' nearly ', ' necessarily ', ' necessary ', ' need ', ' needs ', ' neither ', ' never ', ' nevertheless ', ' new ', ' next ', ' nine ', ' ninety ', ' no ', ' nobody ', ' non ', ' none ', ' nonetheless ', ' noone ', ' nor ', ' normally ', ' nos ', ' not ', ' noted ', ' nothing ', ' now ', ' nowhere ', ' o ', ' obtain ', ' obtained ', ' obviously ', ' of ', ' off ', ' often ', ' oh ', ' ok ', ' okay ', ' old ', ' omitted ', ' on ', ' once ', ' one ', ' ones ', ' only ', ' onto ', ' or ', ' ord ', ' other ', ' others ', ' otherwise ', ' ought ', ' our ', ' ours ', ' ourselves ', ' out ', ' outside ', ' over ', ' overall ', ' owing ', ' own ', ' p ', ' page ', ' pages ', ' part ', ' particular ', ' particularly ', ' past ', ' per ', ' perhaps ', ' placed ', ' please ', ' plus ', ' poorly ', ' possible ', ' possibly ', ' potentially ', ' pp ', ' predominantly ', ' present ', ' previously ', ' primarily ', ' probably ', ' promptly ', ' proud ', ' provides ', ' put ', ' q ', ' que ', ' quickly ', ' quite ', ' qv ', ' r ', ' ran ', ' rather ', ' rd ', ' re ', ' readily ', ' really ', ' recent ', ' recently ', ' ref ', ' refs ', ' regarding ', ' regardless ', ' regards ', ' related ', ' relatively ', ' research ', ' respectively ', ' resulted ', ' resulting ', ' results ', ' right ', ' run ', ' s ', ' said ', ' same ', ' saw ', ' say ', ' saying ', ' says ', ' sec ', ' section ', ' see ', ' seeing ', ' seem ', ' seemed ', ' seeming ', ' seems ', ' seen ', ' self ', ' selves ', ' sent ', ' seven ', ' several ', ' shall ', ' she ', ' shed ', " she'll ", ' shes ', ' should ', " shouldn't ", ' show ', ' showed ', ' shown ', ' showns ', ' shows ', ' significant ', ' significantly ', ' similar ', ' similarly ', ' since ', ' six ', ' slightly ', ' so ', ' some ', ' somebody ', ' somehow ', ' someone ', ' somethan ', ' something ', ' sometime ', ' sometimes ', ' somewhat ', ' somewhere ', ' soon ', ' sorry ', ' specifically ', ' specified ', ' specify ', ' specifying ', ' still ', ' stop ', ' strongly ', ' sub ', ' substantially ', ' successfully ', ' such ', ' sufficiently ', ' suggest ', ' sup ', ' sure ', ' t ', ' take ', ' taken ', ' taking ', ' tell ', ' tends ', ' th ', ' than ', ' thank ', ' thanks ', ' thanx ', ' that ', " that'll ", ' thats ', " that've ", ' the ', ' their ', ' theirs ', ' them ', ' themselves ', ' then ', ' thence ', ' there ', ' thereafter ', ' thereby ', ' thered ', ' therefore ', ' therein ', " there'll ", ' thereof ', ' therere ', ' theres ', ' thereto ', ' thereupon ', " there've ", ' these ', ' they ', ' theyd ', " they'll ", ' theyre ', " they've ", ' think ', ' this ', ' those ', ' thou ', ' though ', ' thoughh ', ' thousand ', ' throug ', ' through ', ' throughout ', ' thru ', ' thus ', ' til ', ' tip ', ' to ', ' together ', ' too ', ' took ', ' toward ', ' towards ', ' tried ', ' tries ', ' truly ', ' try ', ' trying ', ' ts ', ' twice ', ' two ', ' u ', ' un ', ' under ', ' unfortunately ', ' unless ', ' unlike ', ' unlikely ', ' until ', ' unto ', ' up ', ' upon ', ' ups ', ' us ', ' use ', ' used ', ' useful ', ' usefully ', ' usefulness ', ' uses ', ' using ', ' usually ', ' v ', ' value ', ' various ', " 've ", ' very ', ' via ', ' viz ', ' vol ', ' vols ', ' vs ', ' w ', ' want ', ' wants ', ' was ', ' wasnt ', ' way ', ' we ', ' wed ', ' welcome ', " we'll ", ' went ', ' were ', ' werent ', " we've ", ' what ', ' whatever ', " what'll ", ' whats ', ' when ', ' whence ', ' whenever ', ' where ', ' whereafter ', ' whereas ', ' whereby ', ' wherein ', ' wheres ', ' whereupon ', ' wherever ', ' whether ', ' which ', ' while ', ' whim ', ' whither ', ' who ', ' whod ', ' whoever ', ' whole ', " who'll ", ' whom ', ' whomever ', ' whos ', ' whose ', ' why ', ' widely ', ' will ',' willing ', ' wish ', ' with ', ' within ', ' without ', ' wont ', ' words ', ' world ', ' would ', ' wouldnt ', ' www ', ' x ', ' y ', ' yes ', ' yet ', ' you ', ' youd ', " you'll ", ' your ', ' youre ', ' yours ', ' yourself ', ' yourselves ', " you've ", ' z ', ' zero ']

def cut(filein):	
    fileout=[]
    for line in filein:
        for word in dic:
            line=line.replace(word," ")
        fileout.append(line)
    return fileout

def news_search2(site,title,flag):
    url = 'https://newsapi.org/v1/articles?source='+site+'&apiKey=7a6fe927be1a469d85973dcba1d67b2a'
    json_obj = urllib2.urlopen(url)
    data = json.load(json_obj)

    meta= data['articles']

    for i in meta:
        news= i['title']
        news=news.split()
        for x in title:
            flag=0
            if x not in news:
                flag=1
        if flag==0:    
            newslist.append(i['url'])

sitelist=["bbc-news","the-verge"]
newslist=[]
dict1={}
wt={}
out=[]
x=[]
keywords=[]
locu_api = '7a6fe927be1a469d85973dcba1d67b2a'
#retrieving Trump related news from popular sites
def news_search(site,y):
    url = 'https://newsapi.org/v1/articles?source='+site+'&apiKey=7a6fe927be1a469d85973dcba1d67b2a'
    json_obj = urllib2.urlopen(url)
    data = json.load(json_obj)

    meta= data['articles']

    i=meta[0]
    news= i['title']
    news=news.split()
    news=cut(news)
    newslist.append(i['url'])

    for i in newslist:
	#content=""
        i=str(i)
        #print i
        url = urllib.urlopen(i)
        content = url.read()
        soup = BeautifulSoup(content, 'lxml') 
        table = soup.findAll('p')
        for x in table:
            
            y=str(x)
            #print y
            y=y.split()
            for i in news:
                if i in y:
                    out.append(x.text)
                    continue
    
        
    for hd in news:
        c=0
        for i in out:
            k=i.split()
            for m in k:
                if hd==m:
                    c=c+1
            wt[hd]=c
      

    
            
news_search("cnn","")
max=0    
for key in wt:
    if wt[key]>max:
        
        max=wt[key]
for i in wt:
    if wt[i]>max-2 and i!="in":
        
        keywords.append(i)
#**********************Retrieved Keywords for related news*************************

j=1
for i in sitelist:
    news_search2(i,keywords,0)
#print out
z=[]
out3=[]
for i in newslist:
	#content=""
    
    i=str(i)
    #print i
    url = urllib.urlopen(i)
    content = url.read()
    soup = BeautifulSoup(content, 'lxml') 


    table = soup.findAll('p')
    for x in table:
        
        y=str(x)
        y=y.split()
        
        for i in y:
            u = unicode(i, "utf-8")
            z.append(u)
        for i in keywords:
            if i in z : 
                
                out3.append(x.text)
    #out.append("*************************************************************************")
    dict1[j]=i
    j+=1



newout=cut(out3)

out4=[]
common=[]

for i in newout:
        out4.append(i.split())

for i in out4:
    
    for j in i:
        flag=0
        for k in out4:
            
            if j in k:
                    #flag=1
                    common.append(j)
                    continue
        #if flag==0:
            #common.append(j)

common=list(set(common))

         
#common=list(set(common))

#print newout
#print "\n*************************************************************************\n"

#***********************Selecting unbiased site************************************
#*********************************************************************************
#************************************************************************************
bias={}
q=1
for i in out4:
    count=0
    for j in i:
        for k in common:
            if k==j:
                count=count+1
    bias[q]=count
        
max2=0
for i in bias:
    if bias[i]>max2:
        max2=bias[i]
lasturl=""        
for i in bias:
    if bias[i]==max2:
        lasturl=newslist[i-1]
        
    

#print common
#print keywords
#print "***************************  ********   ********   *********\n"
lasturl = lasturl.encode('utf-8')

print lasturl
    
    

