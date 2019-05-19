#!/usr/bin/python3

import smtplib
import os
from email.mime.base import MIMEBase
from email import encoders
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from os import system
from getpass import getpass
from templates import icon
'''
CODED BY MARIO YEHEZKIEL

INSTAGRAM : https://www.instagram.com/zcybercru/
	    https://www.instagram.com/mario.yhzkiell/
GITHUB : https://github.com/marioyhzkiell
hackerone : https://hackerone.com/marioyhzkiell

'''
class colors:
    def __init__(self,inputColor):
        self.Color = inputColor
red = colors('\033[91m')
green = colors('\033[92m')
yellow = colors('\033[93m')
cyan = colors('\033[96m')

system('clear')
icon.item()
print ('═════════════════════════════════════════════════════')
print ('═'+cyan.Color+'[●] This tool is specifically for Gmail and Yahoo users!','═')
print ('═','[●] Enable (less secure apps) in your email settings to work!','═')
print ('═════════════════════════════════════════════════════')
print ('\n'+yellow.Color+'[●] select type vulnerability you want to report!')
print (' ═════════════════════════════════════════════════ ')
print ('    '+green.Color+'[1].'+yellow.Color+' SQLI[SQL Injection]')
print ('    '+green.Color+'[2].'+yellow.Color+' LFI[Local File Inclusion]')
print ('    '+green.Color+'[3].'+yellow.Color+' RFI[Remote File Inclusion]')
print ('    '+green.Color+'[4].'+yellow.Color+' RCE[Remote Code Execution]')
print ('    '+green.Color+'[5].'+yellow.Color+' CSRF Attack')
print ('    '+green.Color+'[6].'+yellow.Color+' XSS[Cross Site Scripting]')
print ('    '+green.Color+'[7].'+yellow.Color+' SSI[Server Side Injection]')
print ('    '+green.Color+'[8].'+yellow.Color+' CSV Injection')
print ('    '+green.Color+'[9].'+yellow.Color+' Parameter Tampering')
print ('   '+green.Color+'[10].'+yellow.Color+' Bypass Admin')
print ('   '+green.Color+'[99].'+yellow.Color+' Exit/Quit')
print ('   '+green.Color+'[00].'+yellow.Color+' Reinstall/Update Tools\n')


print ('\n'+green.Color+'╭━━¤'+yellow.Color+' [Enter the selected number]')
inputbug = input(green.Color+'╰━━¤ √  : ')

msg = MIMEMultipart()




if inputbug == '1':

    inputsite = '<b>url vuln SQL Injection :</b> '
    print ('\n'+cyan.Color+'[●] Ex : https://pornsite.com/view.php?id=12')
    print (yellow.Color+'═════════════════════════════════════════════')
    print (green.Color+'╭━━¤'+yellow.Color+' [Enter the bug website url]')
    urlsite = input(green.Color+'╰━━¤ √  : ')
    if urlsite:
        print ('')
    else:
        print ('\n'+red.Color+'[!] Please enter site name!')
        print (yellow.Color+'═══════════════════════════\n')
        exit()
    closemail = '<br><br>dengan laporan ini semoga bug report saya dapat diterima dengan baik, terimakasih.'
    respect = '<br><br>Hormat saya,<br>'
    print (green.Color+'╭━━¤'+yellow.Color+' [Enter Your Name]')
    yourname = input(green.Color+'╰━━¤ √  : ')
    if yourname:
        print('')
    else:
        print ('\n'+red.Color+'[!] Please enter your name!')
        print (yellow.Color+'═══════════════════════════\n')
        exit()
    tableclose = '''</p></td></tr><tr>
    <th class="thtwo">
    reported using bugreport tools<br>tools made by <a href="https://www.instagram.com/zcybercru/">zcybercru</a>
    </th>
    </tr></table></td></tr></table></body></html>
    '''
    msg.attach(MIMEText(open('templates/sqli.html',).read(),'html'))
    msg.attach(MIMEText(inputsite,'html'))
    msg.attach(MIMEText(urlsite,'html'))
    msg.attach(MIMEText(closemail,'html'))
    msg.attach(MIMEText(respect,'html'))
    msg.attach(MIMEText(yourname,'html'))
    msg.attach(MIMEText(tableclose,'html'))
    print (cyan.Color+'[●] Enter your file as a POC (Proof of Concept)!')
    print ('[●] Ex : /storage/emulated/0/Document/bugreport.pdf')
    print ('[●] Ex : /storage/emulated/0/Pictures/bugreport.jpg')
    print ('[●] Ex : /storage/emulated/0/Recorder/bugreport.mp4')
    print (yellow.Color+'═══════════════════════════════════════════════════')
    print (green.Color+'╭━━¤'+yellow.Color+' [Enter your document file (default:zcybercru.jpg)]')
    file_location = input(green.Color+'╰━━¤ √  : ') or 'zcybercru.jpg'
    filename = os.path.basename(file_location)
    attachment = open(file_location, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)
  
  
  
elif inputbug == '2':
    
    inputsite = '<b>url vuln Local File Inclusion :</b> '
    print ('\n'+cyan.Color+'[●] Ex : https://pornsite.com/view/?file=../etc/passwd')
    print (yellow.Color+'══════════════════════════════════════════════════════')
    print (green.Color+'╭━━¤'+yellow.Color+' [Enter the bug website url]')
    urlsite = input(green.Color+'╰━━¤ √  : ')
    if urlsite:
        print ('')
    else:
        print ('\n'+red.Color+'[!] Please enter site name!')
        print (yellow.Color+'═══════════════════════════\n')
        exit()
    closemail = '<br><br>dengan laporan ini semoga bug report saya dapat diterima dengan baik, terimakasih.'
    respect = '<br><br>Hormat saya,<br>'
    print (green.Color+'╭━━¤'+yellow.Color+' [Enter Your Name]')
    yourname = input(green.Color+'╰━━¤ √  : ')
    if yourname:
        print('')
    else:
        print ('\n'+red.Color+'[!] Please enter your name!')
        print (yellow.Color+'═══════════════════════════\n')
        exit()
    tableclose = '''</p></td></tr><tr>
    <th class="thtwo">
    reported using bugreport tools<br>tools made by <a href="https://www.instagram.com/zcybercru/">zcybercru</a>
    </th>
    </tr></table></td></tr></table></body></html>
    '''
    msg.attach(MIMEText(open('templates/lfi.html',).read(),'html'))
    msg.attach(MIMEText(inputsite,'html'))
    msg.attach(MIMEText(urlsite,'html'))
    msg.attach(MIMEText(closemail,'html'))
    msg.attach(MIMEText(respect,'html'))
    msg.attach(MIMEText(yourname,'html'))
    msg.attach(MIMEText(tableclose,'html'))
    print (cyan.Color+'[●] Enter your file as a POC (Proof of Concept)!')
    print ('[●] Ex : /storage/emulated/0/Document/bugreport.pdf')
    print ('[●] Ex : /storage/emulated/0/Pictures/bugreport.jpg')
    print ('[●] Ex : /storage/emulated/0/Recorder/bugreport.mp4')
    print (yellow.Color+'═══════════════════════════════════════════════════')
    print (green.Color+'╭━━¤'+yellow.Color+' [Enter your document file (default:zcybercru.jpg)]')
    file_location = input(green.Color+'╰━━¤ √  : ') or 'zcybercru.jpg'
    filename = os.path.basename(file_location)
    attachment = open(file_location, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)
  
  
  
elif inputbug == '3':

    inputsite = '<b>url vuln Remote File Inclusion :</b> '
    print ('\n'+cyan.Color+'[●] Ex : https://pornsite.com/view/?page=http://ex.com/shell.txt')
    print (yellow.Color+'════════════════════════════════════════════════════════════════')
    print (green.Color+'╭━━¤'+yellow.Color+' [Enter the bug website url]')
    urlsite = input(green.Color+'╰━━¤ √  : ')
    if urlsite:
        print ('')
    else:
        print ('\n'+red.Color+'[!] Please enter site name!')
        print (yellow.Color+'═══════════════════════════\n')
        exit()
    closemail = '<br><br>dengan laporan ini semoga bug report saya dapat diterima dengan baik, terimakasih.'
    respect = '<br><br>Hormat saya,<br>'
    print (green.Color+'╭━━¤'+yellow.Color+' [Enter Your Name]')
    yourname = input(green.Color+'╰━━¤ √  : ')
    if yourname:
        print('')
    else:
        print ('\n'+red.Color+'[!] Please enter your name!')
        print (yellow.Color+'═══════════════════════════\n')
        exit()
    tableclose = '''</p></td></tr><tr>
    <th class="thtwo">
    reported using bugreport tools<br>tools made by <a href="https://www.instagram.com/zcybercru/">zcybercru</a>
    </th>
    </tr></table></td></tr></table></body></html>
    '''
    msg.attach(MIMEText(open('templates/rfi.html',).read(),'html'))
    msg.attach(MIMEText(inputsite,'html'))
    msg.attach(MIMEText(urlsite,'html'))
    msg.attach(MIMEText(closemail,'html'))
    msg.attach(MIMEText(respect,'html'))
    msg.attach(MIMEText(yourname,'html'))
    msg.attach(MIMEText(tableclose,'html'))
    print (cyan.Color+'[●] Enter your file as a POC (Proof of Concept)!')
    print ('[●] Ex : /storage/emulated/0/Document/bugreport.pdf')
    print ('[●] Ex : /storage/emulated/0/Pictures/bugreport.jpg')
    print ('[●] Ex : /storage/emulated/0/Recorder/bugreport.mp4')
    print (yellow.Color+'═══════════════════════════════════════════════════')
    print (green.Color+'╭━━¤'+yellow.Color+' [Enter your document file (default:zcybercru.jpg)]')
    file_location = input(green.Color+'╰━━¤ √  : ') or 'zcybercru.jpg'
    filename = os.path.basename(file_location)
    attachment = open(file_location, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)
  
  
  
elif inputbug == '4':

    inputsite = '<b>url vuln Remote Code Execution :</b> '
    print ('\n'+cyan.Color+'[●] Ex : https://pornsite.com/cgi_bin/main.cgi?board=FREE_BOARD')
    print (yellow.Color+'═══════════════════════════════════════════════════════════════')
    print (green.Color+'╭━━¤'+yellow.Color+' [Enter the bug website url]')
    urlsite = input(green.Color+'╰━━¤ √  : ')
    if urlsite:
        print ('')
    else:
        print ('\n'+red.Color+'[!] Please enter site name!')
        print (yellow.Color+'═══════════════════════════\n')
        exit()
    closemail = '<br><br>dengan laporan ini semoga bug report saya dapat diterima dengan baik, terimakasih.'
    respect = '<br><br>Hormat saya,<br>'
    print (green.Color+'╭━━¤'+yellow.Color+' [Enter Your Name]')
    yourname = input(green.Color+'╰━━¤ √  : ')
    if yourname:
        print('')
    else:
        print ('\n'+red.Color+'[!] Please enter your name!')
        print (yellow.Color+'═══════════════════════════\n')
        exit()
    tableclose = '''</p></td></tr><tr>
    <th class="thtwo">
    reported using bugreport tools<br>tools made by <a href="https://www.instagram.com/zcybercru/">zcybercru</a>
    </th>
    </tr></table></td></tr></table></body></html>
    '''
    msg.attach(MIMEText(open('templates/rce.html',).read(),'html'))
    msg.attach(MIMEText(inputsite,'html'))
    msg.attach(MIMEText(urlsite,'html'))
    msg.attach(MIMEText(closemail,'html'))
    msg.attach(MIMEText(respect,'html'))
    msg.attach(MIMEText(yourname,'html'))
    msg.attach(MIMEText(tableclose,'html'))
    print (cyan.Color+'[●] Enter your file as a POC (Proof of Concept)!')
    print ('[●] Ex : /storage/emulated/0/Document/bugreport.pdf')
    print ('[●] Ex : /storage/emulated/0/Pictures/bugreport.jpg')
    print ('[●] Ex : /storage/emulated/0/Recorder/bugreport.mp4')
    print (yellow.Color+'═══════════════════════════════════════════════════')
    print (green.Color+'╭━━¤'+yellow.Color+' [Enter your document file (default:zcybercru.jpg)]')
    file_location = input(green.Color+'╰━━¤ √  : ') or 'zcybercru.jpg'
    filename = os.path.basename(file_location)
    attachment = open(file_location, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)
  
  
  
elif inputbug =='5':

    inputsite = '<b>url vuln CSRF Attack :</b> '
    print ('\n'+cyan.Color+'[●] Ex : https://pornsite.com/download/?acc=paul&price=1000')
    print (yellow.Color+'═══════════════════════════════════════════════════════════')
    print (green.Color+'╭━━¤'+yellow.Color+' [Enter the bug website url]')
    urlsite = input(green.Color+'╰━━¤ √  : ')
    if urlsite:
        print ('')
    else:
        print ('\n'+red.Color+'[!] Please enter site name!')
        print (yellow.Color+'═══════════════════════════\n')
        exit()
    closemail = '<br><br>dengan laporan ini semoga bug report saya dapat diterima dengan baik, terimakasih.'
    respect = '<br><br>Hormat saya,<br>'
    print (green.Color+'╭━━¤'+yellow.Color+' [Enter Your Name]')
    yourname = input(green.Color+'╰━━¤ √  : ')
    if yourname:
        print('')
    else:
        print ('\n'+red.Color+'[!] Please enter your name!')
        print (yellow.Color+'═══════════════════════════\n')
        exit()
    tableclose = '''</p></td></tr><tr>
    <th class="thtwo">
    reported using bugreport tools<br>tools made by <a href="https://www.instagram.com/zcybercru/">zcybercru</a>
    </th>
    </tr></table></td></tr></table></body></html>
    '''
    msg.attach(MIMEText(open('templates/csrf.html',).read(),'html'))
    msg.attach(MIMEText(inputsite,'html'))
    msg.attach(MIMEText(urlsite,'html'))
    msg.attach(MIMEText(closemail,'html'))
    msg.attach(MIMEText(respect,'html'))
    msg.attach(MIMEText(yourname,'html'))
    msg.attach(MIMEText(tableclose,'html'))
    print (cyan.Color+'[●] Enter your file as a POC (Proof of Concept)!')
    print ('[●] Ex : /storage/emulated/0/Document/bugreport.pdf')
    print ('[●] Ex : /storage/emulated/0/Pictures/bugreport.jpg')
    print ('[●] Ex : /storage/emulated/0/Recorder/bugreport.mp4')
    print (yellow.Color+'═══════════════════════════════════════════════════')
    print (green.Color+'╭━━¤'+yellow.Color+' [Enter your document file (default:zcybercru.jpg)]')
    file_location = input(green.Color+'╰━━¤ √  : ') or 'zcybercru.jpg'
    filename = os.path.basename(file_location)
    attachment = open(file_location, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)
  
  
  
elif inputbug == '6':

    inputsite = '<b>url vuln XSS attack :</b> '
    print ('\n'+cyan.Color+'[●] Ex : https://pornsite.com/search/?q=')
    print (yellow.Color+'════════════════════════════════════════')
    print (green.Color+'╭━━¤'+yellow.Color+' [Enter the bug website url]')
    urlsite = input(green.Color+'╰━━¤ √  : ')
    if urlsite:
        print ('')
    else:
        print ('\n'+red.Color+'[!] Please enter site name!')
        print (yellow.Color+'═══════════════════════════\n')
        exit()
    closemail = '<br><br>dengan laporan ini semoga bug report saya dapat diterima dengan baik, terimakasih.'
    respect = '<br><br>Hormat saya,<br>'
    print (green.Color+'╭━━¤'+yellow.Color+' [Enter Your Name]')
    yourname = input(green.Color+'╰━━¤ √  : ')
    if yourname:
        print('')
    else:
        print ('\n'+red.Color+'[!] Please enter your name!')
        print (yellow.Color+'═══════════════════════════\n')
        exit()
    tableclose = '''</p></td></tr><tr>
    <th class="thtwo">
    reported using bugreport tools<br>tools made by <a href="https://www.instagram.com/zcybercru/">zcybercru</a>
    </th>
    </tr></table></td></tr></table></body></html>
    '''
    msg.attach(MIMEText(open('templates/xss.html',).read(),'html'))
    msg.attach(MIMEText(inputsite,'html'))
    msg.attach(MIMEText(urlsite,'html'))
    msg.attach(MIMEText(closemail,'html'))
    msg.attach(MIMEText(respect,'html'))
    msg.attach(MIMEText(yourname,'html'))
    msg.attach(MIMEText(tableclose,'html'))
    print (cyan.Color+'[●] Enter your file as a POC (Proof of Concept)!')
    print ('[●] Ex : /storage/emulated/0/Document/bugreport.pdf')
    print ('[●] Ex : /storage/emulated/0/Pictures/bugreport.jpg')
    print ('[●] Ex : /storage/emulated/0/Recorder/bugreport.mp4')
    print (yellow.Color+'═══════════════════════════════════════════════════')
    print (green.Color+'╭━━¤'+yellow.Color+' [Enter your document file (default:zcybercru.jpg)]')
    file_location = input(green.Color+'╰━━¤ √  : ') or 'zcybercru.jpg'
    filename = os.path.basename(file_location)
    attachment = open(file_location, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)
  
  
  
elif inputbug == '7':

    inputsite = '<b>url vuln Server Side Injection :</b> '
    print ('\n'+cyan.Color+'[●] Ex : https://pornsite.com/member/login.shtml?page=')
    print (yellow.Color+'══════════════════════════════════════════════════════')
    print (green.Color+'╭━━¤'+yellow.Color+' [Enter the bug website url]')
    urlsite = input(green.Color+'╰━━¤ √  : ')
    if urlsite:
        print ('')
    else:
        print ('\n'+red.Color+'[!] Please enter site name!')
        print (yellow.Color+'═══════════════════════════\n')
        exit()
    closemail = '<br><br>dengan laporan ini semoga bug report saya dapat diterima dengan baik, terimakasih.'
    respect = '<br><br>Hormat saya,<br>'
    print (green.Color+'╭━━¤'+yellow.Color+' [Enter Your Name]')
    yourname = input(green.Color+'╰━━¤ √  : ')
    if yourname:
        print('')
    else:
        print ('\n'+red.Color+'[!] Please enter your name!')
        print (yellow.Color+'═══════════════════════════\n')
        exit()
    tableclose = '''</p></td></tr><tr>
    <th class="thtwo">
    reported using bugreport tools<br>tools made by <a href="https://www.instagram.com/zcybercru/">zcybercru</a>
    </th>
    </tr></table></td></tr></table></body></html>
    '''
    msg.attach(MIMEText(open('templates/ssi.html',).read(),'html'))
    msg.attach(MIMEText(inputsite,'html'))
    msg.attach(MIMEText(urlsite,'html'))
    msg.attach(MIMEText(closemail,'html'))
    msg.attach(MIMEText(respect,'html'))
    msg.attach(MIMEText(yourname,'html'))
    msg.attach(MIMEText(tableclose,'html'))
    print (cyan.Color+'[●] Enter your file as a POC (Proof of Concept)!')
    print ('[●] Ex : /storage/emulated/0/Document/bugreport.pdf')
    print ('[●] Ex : /storage/emulated/0/Pictures/bugreport.jpg')
    print ('[●] Ex : /storage/emulated/0/Recorder/bugreport.mp4')
    print (yellow.Color+'═══════════════════════════════════════════════════')
    print (green.Color+'╭━━¤'+yellow.Color+' [Enter your document file (default:zcybercru.jpg)]')
    file_location = input(green.Color+'╰━━¤ √  : ') or 'zcybercru.jpg'
    filename = os.path.basename(file_location)
    attachment = open(file_location, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)
  
  
  
elif inputbug == '8':

    inputsite = '<b>url vuln CSV Injection :</b> '
    print ('\n'+cyan.Color+'[●] Ex : https://pornsite.com/member/upload_video/#addvideo')
    print (yellow.Color+'═══════════════════════════════════════════════════════════')
    print (green.Color+'╭━━¤'+yellow.Color+' [Enter the bug website url]')
    urlsite = input(green.Color+'╰━━¤ √  : ')
    if urlsite:
        print ('')
    else:
        print ('\n'+red.Color+'[!] Please enter site name!')
        print (yellow.Color+'═══════════════════════════\n')
        exit()
    closemail = '<br><br>dengan laporan ini semoga bug report saya dapat diterima dengan baik, terimakasih.'
    respect = '<br><br>Hormat saya,<br>'
    print (green.Color+'╭━━¤'+yellow.Color+' [Enter Your Name]')
    yourname = input(green.Color+'╰━━¤ √  : ')
    if yourname:
        print('')
    else:
        print ('\n'+red.Color+'[!] Please enter your name!')
        print (yellow.Color+'═══════════════════════════\n')
        exit()
    tableclose = '''</p></td></tr><tr>
    <th class="thtwo">
    reported using bugreport tools<br>tools made by <a href="https://www.instagram.com/zcybercru/">zcybercru</a>
    </th>
    </tr></table></td></tr></table></body></html>
    '''
    msg.attach(MIMEText(open('templates/csv.html',).read(),'html'))
    msg.attach(MIMEText(inputsite,'html'))
    msg.attach(MIMEText(urlsite,'html'))
    msg.attach(MIMEText(closemail,'html'))
    msg.attach(MIMEText(respect,'html'))
    msg.attach(MIMEText(yourname,'html'))
    msg.attach(MIMEText(tableclose,'html'))
    print (cyan.Color+'[●] Enter your file as a POC (Proof of Concept)!')
    print ('[●] Ex : /storage/emulated/0/Document/bugreport.pdf')
    print ('[●] Ex : /storage/emulated/0/Pictures/bugreport.jpg')
    print ('[●] Ex : /storage/emulated/0/Recorder/bugreport.mp4')
    print (yellow.Color+'═══════════════════════════════════════════════════')
    print (green.Color+'╭━━¤'+yellow.Color+' [Enter your document file (default:zcybercru.jpg)]')
    file_location = input(green.Color+'╰━━¤ √  : ') or 'zcybercru.jpg'
    filename = os.path.basename(file_location)
    attachment = open(file_location, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)
  
  
  
elif inputbug == '9':

    inputsite = '<b>url vuln Parameter Tempering :</b> '
    print ('\n'+cyan.Color+'[●] Ex : https://pornsite.com/download/?vid=asian.mp4&price=1000')
    print (yellow.Color+'════════════════════════════════════════════════════════════════')
    print (green.Color+'╭━━¤'+yellow.Color+' [Enter the bug website url]')
    urlsite = input(green.Color+'╰━━¤ √  : ')
    if urlsite:
        print ('')
    else:
        print ('\n'+red.Color+'[!] Please enter site name!')
        print (yellow.Color+'═══════════════════════════\n')
        exit()
    closemail = '<br><br>dengan laporan ini semoga bug report saya dapat diterima dengan baik, terimakasih.'
    respect = '<br><br>Hormat saya,<br>'
    print (green.Color+'╭━━¤'+yellow.Color+' [Enter Your Name]')
    yourname = input(green.Color+'╰━━¤ √  : ')
    if yourname:
        print('')
    else:
        print ('\n'+red.Color+'[!] Please enter your name!')
        print (yellow.Color+'═══════════════════════════\n')
        exit()
    tableclose = '''</p></td></tr><tr>
    <th class="thtwo">
    reported using bugreport tools<br>tools made by <a href="https://www.instagram.com/zcybercru/">zcybercru</a>
    </th>
    </tr></table></td></tr></table></body></html>
    '''
    msg.attach(MIMEText(open('templates/paramtemper.html',).read(),'html'))
    msg.attach(MIMEText(inputsite,'html'))
    msg.attach(MIMEText(urlsite,'html'))
    msg.attach(MIMEText(closemail,'html'))
    msg.attach(MIMEText(respect,'html'))
    msg.attach(MIMEText(yourname,'html'))
    msg.attach(MIMEText(tableclose,'html'))
    print (cyan.Color+'[●] Enter your file as a POC (Proof of Concept)!')
    print ('[●] Ex : /storage/emulated/0/Document/bugreport.pdf')
    print ('[●] Ex : /storage/emulated/0/Pictures/bugreport.jpg')
    print ('[●] Ex : /storage/emulated/0/Recorder/bugreport.mp4')
    print (yellow.Color+'═══════════════════════════════════════════════════')
    print (green.Color+'╭━━¤'+yellow.Color+' [Enter your document file (default:zcybercru.jpg)]')
    file_location = input(green.Color+'╰━━¤ √  : ') or 'zcybercru.jpg'
    filename = os.path.basename(file_location)
    attachment = open(file_location, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)
  
  
  
elif inputbug == '10':

    inputsite = '<b>url vuln Bypass Admin :</b> '
    print ('\n'+cyan.Color+'[●] Ex : https://pornsite.com/adminporn/login.php')
    print (yellow.Color+'═════════════════════════════════════════════════')
    print (green.Color+'╭━━¤'+yellow.Color+' [Enter the bug website url]')
    urlsite = input(green.Color+'╰━━¤ √  : ')
    if urlsite:
        print ('')
    else:
        print ('\n'+red.Color+'[!] Please enter site name!')
        print (yellow.Color+'═══════════════════════════\n')
        exit()
    closemail = '<br><br>dengan laporan ini semoga bug report saya dapat diterima dengan baik, terimakasih.'
    respect = '<br><br>Hormat saya,<br>'
    print (green.Color+'╭━━¤'+yellow.Color+' [Enter Your Name]')
    yourname = input(green.Color+'╰━━¤ √  : ')
    if yourname:
        print('')
    else:
        print ('\n'+red.Color+'[!] Please enter your name!')
        print (yellow.Color+'═══════════════════════════\n')
        exit()
    tableclose = '''</p></td></tr><tr>
    <th class="thtwo">
    reported using bugreport tools<br>tools made by <a href="https://www.instagram.com/zcybercru/">zcybercru</a>
    </th>
    </tr></table></td></tr></table></body></html>
    '''
    msg.attach(MIMEText(open('templates/rfi.html',).read(),'html'))
    msg.attach(MIMEText(inputsite,'html'))
    msg.attach(MIMEText(urlsite,'html'))
    msg.attach(MIMEText(closemail,'html'))
    msg.attach(MIMEText(respect,'html'))
    msg.attach(MIMEText(yourname,'html'))
    msg.attach(MIMEText(tableclose,'html'))
    print (cyan.Color+'[●] Enter your file as a POC (Proof of Concept)!')
    print ('[●] Ex : /storage/emulated/0/Document/bugreport.pdf')
    print ('[●] Ex : /storage/emulated/0/Pictures/bugreport.jpg')
    print ('[●] Ex : /storage/emulated/0/Recorder/bugreport.mp4')
    print (yellow.Color+'═══════════════════════════════════════════════════')
    print (green.Color+'╭━━¤'+yellow.Color+' [Enter your document file (default:zcybercru.jpg)]')
    file_location = input(green.Color+'╰━━¤ √  : ') or 'zcybercru.jpg'
    filename = os.path.basename(file_location)
    attachment = open(file_location, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)
  
  
  
elif inputbug == '99':
    print ('\n'+cyan.Color+'[●] have a nice day!')
    print (yellow.Color+'════════════════════')
    exit()
    
elif inputbug == '00':
    sys = system('cd .. && rm -rf bugreport && git clone https://github.com/marioyhzkiell/bugreport.git')
    print ('\n'+cyan.Color+'[●] Success Reinstall/Update Tools!')
    print ('[●] CTRL + D for exit, and login again!')
    print (yellow.Color+'═══════════════════════════════════════')
    exit()
else:
    print ('\n'+red.Color+'[!] wrong input!')
    print (yellow.Color+'════════════════')
    exit()
    
    
system('clear')
icon.item()
print (cyan.Color+'[●] Select the email account server used!')
print (yellow.Color+'═════════════════════════════════════════')
print ('    '+green.Color+'[1].'+yellow.Color+' Gmail')
print ('    '+green.Color+'[2].'+yellow.Color+' Yahoo')
print ('   '+green.Color+'[99].'+yellow.Color+' Exit/Quit')
print ('\n'+green.Color+'╭━━¤'+yellow.Color+' [Enter the selected number]')
choice = input(green.Color+'╰━━¤ √  : ')
if choice == '1':
        server = smtplib.SMTP('smtp.gmail.com', 587)
elif choice == '2':
        server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
elif choice == '99':
        print ('\n'+cyan.Color+'[●] have a nice day!')
        print (yellow.Color+'════════════════════')
        exit()
else:
        print ('\n'+red.Color+'[!] wrong input!')
        print (yellow.Color+'════════════════')
        exit()

print ('\n'+green.Color+'╭━━¤'+yellow.Color+' [Enter your email]')
email = input(green.Color+'╰━━¤ √  : ')
if email:
    print ('')
else:
    print ('\n'+red.Color+'[!] Please enter your email!')
    print (yellow.Color+'════════════════════════════\n')
    exit()

print (cyan.Color+'[●] Blank passwd OR See passwd for entering your pass?')
print (yellow.Color+'══════════════════════════════════════════════════════')
print ('    '+green.Color+'[1].'+yellow.Color+' See Password')
print ('    '+green.Color+'[2].'+yellow.Color+' Blank Password')
print ('\n'+green.Color+'╭━━¤'+yellow.Color+' [Enter the selected number]')
inputpass = input(green.Color+'╰━━¤ √  : ')
if inputpass == '1':
    print ('\n'+green.Color+'╭━━¤'+yellow.Color+' [Enter your password email]')
    password = input(green.Color+'╰━━¤ √  : ')
    if password:
        print ('')
    else:
        print ('\n'+red.Color+'[!] Please enter your password!')
        print (yellow.Color+'═══════════════════════════════\n')
        exit()
elif inputpass == '2':
    print ('\n'+green.Color+'╭━━¤'+yellow.Color+' [Enter your password email]')
    password = getpass(green.Color+'╰━━¤ √  : ')
    if password:
        print ('')
    else:
        print ('\n'+red.Color+'[!] Please enter your password!')
        print (yellow.Color+'═══════════════════════════════\n')
        exit()
else:
    print ('\n'+red.Color+'[!] wrong input!')
    print (yellow.Color+'════════════════')
    exit()
print (green.Color+'╭━━¤'+yellow.Color+' [Enter your email destination]')
toaddr = input(green.Color+'╰━━¤ √  : ')
if toaddr:
    print ('')
else:
    print ('\n'+red.Color+'[!] Please enter your email destination!')
    print (yellow.Color+'════════════════════════════════════════\n')
    exit()
print (cyan.Color+'[●] Enter your email title!')
print ('[●] Ex : [BUG BOUNTY TOKOPEDIA] Stored XSS to get user info')
print ('[●] Ex : [xx.xx.go.id] SQL INJECTION on /berita.php?id=12')
print ('[●] Ex : [pornsite.com] SQL INJECTION on /index.php?id=12')
print (yellow.Color+'═════════════════════════════════════════════════════════')
print (green.Color+'╭━━¤'+yellow.Color+' [Enter your email title]')
title = input(green.Color+'╰━━¤ √  : ')
if title:
    print ('')
else:
    print ('\n'+red.Color+'[!] Please enter your email title!')
    print (yellow.Color+'══════════════════════════════════\n')
    exit()
msg['From'] = email
msg['To'] = toaddr
msg['Subject'] = title
server.starttls()
text = msg.as_string()
server.login(email,password)
server.sendmail(email, toaddr, text)
print ('\n'+cyan.Color+'[●] Successfully sent! check the sent message in your email!')
server.quit()
