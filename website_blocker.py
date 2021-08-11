import sqlite3



host_path= r"C:\Windows\System32\drivers\etc\hosts" 
host_temp = r"C:\Users\sital\Desktop\Learning pythom\website blocker\hosts" 

redirect = "127.0.0.1" 


def connect():
    conn = sqlite3.connect("blocked.db")
    cur = conn.cursor()
    cur. execute("CREATE TABLE IF NOT EXISTS block(website TEXT PRIMARY KEY unique)") 
    conn.commit()
    conn.close()

website_list = [] 


def addWebsite(website):
    website_list.append(website) 
    
    conn = sqlite3.connect("blocked.db")
    cur = conn.cursor()
    cur.execute("INSERT or IGNORE INTO block VALUES(?)",(website,)) 
    conn.commit()
    conn.close()


def deleteWebsite(website):
    conn = sqlite3.connect("blocked.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM block WHERE website =?",(website,))
    conn.commit()
    conn.close()

    with open(host_path,'r+') as file:
                content=file.readlines()
                
                
                file.seek(0) 
                for lines in content:
                    if not any(website in lines for website in website_list):  
                        file.write(lines) 
                file.truncate() 



 
def blocked_list():
    blocked_list = website_list.copy()  
    conn = sqlite3.connect("blocked.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM block")
    rows = cur.fetchall()
    conn.close()
    return rows



def block(x): 
        
        if x==0:  
            print("Working hours")
            
            with open(host_path,'r+') as file: 
                content = file.read() 
                
                for sites in website_list: 
                    if sites in content: 
                        pass
                    else:
                        file.write(redirect+" "+sites+"\n") 

        
        else:
            print("use that site")
            
            with open(host_path,'r+') as file:
                content=file.readlines()
                
                
                file.seek(0) 
                for lines in content:
                    if not any(website in lines for website in website_list):  
                        file.write(lines) 
                file.truncate() 

connect() 



