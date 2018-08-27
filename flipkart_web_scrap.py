from bs4 import BeautifulSoup as parser
from urllib.request import urlopen as uReq
search_term=input("Enter search term:")
Html_url='https://www.flipkart.com/search?q='+search_term
Html=uReq(Html_url)
InstancePage=Html.read()
Html.close()
page=parser(InstancePage,"html.parser")
containers=page.find_all("div",{"class":"col col-7-12"})
filename="flipkart.csv"
f=open(filename,"w")
for container in containers:
    #container=containers[18]
    product=[]
    product_name=container.find_all("div",{"class":"_3wU53n"})[0].text.strip(')').split('(')
    rating=container.find_all("div",{"class":"niH0FQ"})[0].text[0:3].strip('★')
    #ram=container.find_all("li",{"class":"tVe95H"})[0].text[0:3]
    #print(product_name+" "+rating+" "+ram)
    product.append(product_name[0])
    product.append(rating)
    #product.append(ram)
    f.write(",".join(product)+'\n')
    #print(product_name[0]+' '+rating)
