from googlesearch import search
import sys, os, tj, webbrowser, bs4
import requests


doc='''
WELCOME TO Internet Search

This program helps you to quickly search google and find your results without even
opening the browser.

All you need to do is open CMD. Type it in Windows search or open Run box (Windows Key + R)
and type CMD in it.

In CMD type 'g <YOUR SEARCH HERE> <ARGUMENTS>' (without quotes). The arguments means any of these
arguments r performing different actions-
1) OPEN Argument -> Use this argument to search, and the program will show you the search results.
    Then you can choose and open your preferable search result after that.
    For the OPEN argument, you need to type @O or #O or @OPEN or #OPEN
    eg. 'g wikipedia laptops @O' will show you search results. After that, you can select your
    preferable result.

2) QUICK/FAST OPEN Argument -> This is the "I'm Feeling Lucky" version of OPEN argument. What this
    does is, it instantly opens the first search result. So, after you type and hit enter, the
    program will search google for results, and then open the first search result automatically,
    without needing your interference. Use this argument if you are searching something very
    popular, or if you want to open a popular site.
    For the FAST/QUICK OPEN, you need to type @FO or @QO or #FO or #QO
    eg. 'g facebook.com @FO' will instantly open www.facebook.com in your browser.

3) PREVIEW Argument -> Use this argument to view a glimpse of the webpage you want to open.
    It works like the OPEN argument, the search gives you results, and you can choose your
    preferable search result. Then the program will display the contents of the webpage to
    you instaed of opening the webpage in the browser. This is useful if you want to search
    and find an article is useful or not.
    For PREVIEW, you need to type @P or #P or @V or #V or @PREVIEW
    eg. 'g best pizza recipie @P' will give you results and you can preview them there and then
    in the CMD window, saving you time.

4) FAST/QUICK PREVIEW Argument -> This is the "I'm Feeling Lucky" version of PREVIEW argument. What this
    does is, it instantly opens the first search result. So, after you type and hit enter, the
    program will search google for results, and then preview/show you the first search result automatically,
    without needing your interference. Use this argument if you want some information quickly.
    For FAST/QUICK PREVIEW, you need to type @QP or #QP or @FP or #FP or @QV or #FV
    eg. 'g wiki India @QP' will give you the contents of the very first search results, you need not open
    your browser.

5) DOCUMENTATION Argument -> Use this argument if you want help in using this program.
    For DOCUMENTATION argument, you need to type @D or @DOC or #D or #DOC
    eg. 'g #D'

* FOR USAGE OF THIS PROGRAM, COPY-PASTE IT IN THE C:\\Windows FOLDER.

* ALTERNATIVELY, YOU CAN ADD THE PATH OF THIS PROGRAM IN THE ENVIRONMENTAL VARIABLES OF
    YOUR COMPUTER
'''


doc_args=['@D', '@DOC', '#D', '#DOC']
open_args=['@O', '#O', '@OPEN', '#OPEN']
quick_open_args=['@QO', '#QO', '@QOPEN', '#QOPEN','@FO', '#FO', '@FOPEN', '#FOPEN']
preview_args=['@V', '@VIEW',  '#V', '#VIEW', '@P','@PREVIEW' ,'#P', '#PREVIEW']
quick_preview_args=['@QV', '@QVIEW',  '#QV', '#QVIEW', '@QP','@QPREVIEW' ,'#QP', '#QPREVIEW','@FV', '@FVIEW',  '#FV', '#FVIEW', '@FP','@FPREVIEW' ,'#FP', '#FPREVIEW']

all_args=open_args+preview_args+quick_open_args+quick_preview_args

args=sys.argv[1:]
if args==[]:
    print(doc)
    webbrowser.open('www.google.com')
    input('\nEnter to quit...')
    sys.exit()
else:
    last_arg=None
    for arg in all_args:
        if arg.upper() in [i.upper() for i in args]:
            last_arg=arg.upper()

    if last_arg==None:last_arg='@FO'
    else:args=args[:-1]
    query=" ".join(args)


print('Query-> ',query)
if last_arg in open_args:print('What to do-> OPEN IN BROWSER')
if last_arg in quick_open_args:print('What to do-> QUICKLY OPEN IN BROWSER')
if last_arg in preview_args:print('What to do-> PREVIEW THE TEXT OF WEBSITE')
if last_arg in quick_preview_args:print('What to do-> QUICKLY PREVIEW THE TEXT OF WEBSITE')
if last_arg in doc_args:
    print(doc)
    input('\nEnter to quit...')
    sys.exit()




try:S=list(search(query, num=10, stop=1))
except:
    input('Error connecting to the internet,\ncheck your internet connection...')
    sys.exit()


def show_results(S):
    for i in range(len(S)):
        result=S[i]
        print(f'{i+1} - {result}')

def scrape_words(result):
    url=result
    sauce=requests.get(url).content
    soup=bs4.BeautifulSoup(sauce,'lxml')
    paras=soup.find_all('p')

    for i in range(1,len(paras)+1):
        para=paras[i-1]

        if i%5==0:
            choice=input('Enter to continue reading, Q to quit...').upper()
            if choice in ['Q','QUIT']:
                return
        print(para.text)
    

if last_arg in quick_open_args:
    webbrowser.open(S[0])

if last_arg in open_args:
    show_results(S)
    choice=input('Enter the number of the result to open it (Q to quit): ')
    
    if choice in [str(i+1) for i in range(len(S))]:
        choice=int(choice)-1
        result=S[choice]
        webbrowser.open(result)
        
if last_arg in quick_preview_args:
    scrape_words(S[0])

if last_arg in preview_args:
    show_results(S)
    choice=input('Enter the number of the result to open it (Q to quit): ')
    
    if choice in [str(i+1) for i in range(len(S))]:
        choice=int(choice)-1
        result=S[choice]
        scrape_words(result)

