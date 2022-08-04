#author_Zabiullah
#adless_youtube_link_convertor

print('''Adless Youtube link Convertor\n''')

url=input('Pate the Youtube Video Link Here :: ')

st=''
for i in url:
    if i in '?':
        st+="_popup"
    st+=i

print(f'\ncopy this link and paste in your browser and enjoy your adless video\n\n{st}')
        
        


