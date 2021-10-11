from auto_link.tt import change_link, countdown, get_ep_name, valid_link
from django.shortcuts import render, redirect
from django.template.loader import get_template
import requests
from bs4 import BeautifulSoup

def test(request):
    test2 = True
    check = None
    a = ''
    msg = ''
    html_text = ''
    href = ''
    link = ''
    links = ''
    link_tag = ''
    link_name = ''
    link_list_ref = []
    link_list = []
    No_list = True
    mylink = ''
    
    if request.POST:
        href = request.POST['fname']
        check = request.POST.get('checkbox', False)
        href = change_link(href)
        test2 = valid_link(href)
        if test2:
            html_text = requests.get(href).text
            soup = BeautifulSoup(html_text, 'lxml')
            links = soup.find_all('li', class_= 'episodeSub')
            for mylink in links:
                link_tag = mylink.find('a')
                a = link_tag.get('href')
                link_list_ref.append(a)
        else:
            msg = 'Invalid Link'
    for link in link_list_ref:
        link_name = get_ep_name(link)
        link_list.append(link_name)
    time_done = countdown(1)
    link_list.reverse()
    if link_list != []:
        No_list = False
    
    template = 'auto_link/uploader.html'
    context = {
        'checkbox': check,
        'time_done': time_done,
        'test2': test2,
        'msg': msg,
        'links': links,
        'link_list': link_list,
        'link_list_ref': link_list_ref,
        'No_list': No_list,
    }
    return render(request, template, context)
