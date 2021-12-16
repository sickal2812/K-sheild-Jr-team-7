print ("2_1_exDBin1 Open")
import csv
import re

import mysql.connector

mydb = mysql.connector.connect(
    host = "3.35.48.144",
    user = "root", 
    password = "Rlfnr",
    database = "prototype_schema"
)

mycursor = mydb.cursor()

f = open('data.csv', 'r')
rdr = csv.reader(f)
counter = 1

list = []
for i in rdr:
    list.append(i)

numbers= []
for i in range(0,10):
    numbers.append(str(i))

try:
    for line in list:
        #line = (line)
        name = line[0]
        origin_name = name
    
        vul_type_name = ''
        vul_type_ver = ''

        if( 'Cross-Site Scripting' in name):
            vul_type_name = 'Cross-Site Scripting'
        if( 'XSS' in name):
            vul_type_name = 'XSS'
        if( 'CSRF' in name):
            vul_type_name = 'XSS'
        if( 'XXE' in name):
            vul_type_name = 'XXE'
        if( 'SQL Injection' in name) or ('Sql Injection' in name) or ('SQL injection' in name):
            vul_type_name = 'SQL Injection'
        if( 'Cross-Site Scripting' in name):
            vul_type_name = 'Cross-Site Scripting'
        if( 'Remote File Inclusion' in name):
            vul_type_name = 'Remote File Inclusion'
        if( 'Local File Inclusion' in name):
            vul_type_name = 'Local File Inclusion'
        if( 'Arbitrary File Upload' in name) or ('Arbitrary file upload' in name):
            vul_type_name = 'Arbitrary File Upload'
        if( 'Cross-Site Request Forgery' in name):
            vul_type_name = 'Cross-Site Request Forgery'
        if( 'Arbitrary Code Execution' in name):
            vul_type_name = 'Arbitrary Code Execution'
        if( 'Remote Shell Injection' in name):
            vul_type_name = 'Remote Shell Injection'
        if( 'Information Disclosure' in name):
            vul_type_name = 'Information Disclosure'
        if( 'Multiple Vulnerabilities' in name):
            vul_type_name = 'Multiple Vulnerabilities'
        if( 'Remote Code Execution' in name):
            vul_type_name = 'Remote Code Execution'
        if( 'Remote File Disclosure' in name):
            vul_type_name = 'Remote File Disclosure'
        if( 'Arbitrary File Download' in name):
            vul_type_name = 'Arbitrary File Download'
        if( 'CSV Injection' in name):
            vul_type_name = 'CSV Injection'
        if( 'HTML Injection' in name):
            vul_type_name = 'HTML Injection'
        if( 'Privilege Escalation' in name):
            vul_type_name = 'Privilege Escalation'

        '''
    Cross Site Scripting
    Remote Code Execution
    Multiple Vulnerabilities
    SQL injection
    Event export
    HTML Injection
    Privilege Escalation
        '''

        if vul_type_name == '':
            print(name+" has no type name")
            continue

        if "# Exploit Title: WordPress Plugin" in name:
            name = name[34:]
        if "WordPress Plugin" in name:
            name = name[17:]
        if "# Exploit Title: WordPress" in name:
            name = name[27:]
        if "# Exploit Title: Wordpress Plugin" in name:
            name = name[len("# Exploit Title: Wordpress Plugin "):]
        if "# Exploit Title: Wordpress " in name:
            name = name[len("# Exploit Title: Wordpress "):]
        if "# Exploit Title: " in name:
            name = name[len("# Exploit Title: "):]
        if "<=" in name:
            name = name.replace("<=","")
        if "Title: " in name:
            name = name.replace("Title: ","")
        if " <" in name:
            name = name.replace(" <", "")
        if "<" in name:
            name = name.replace("<", "")
        if "# Title: Wordpress " in name:
            name = name[len("# Title: Wordpress "):]
        
            
            # Exploit Title: 
        a = name.split(" ")

        for i in a:
            if "." in i:
                for j in range(0,10):
                    if str(j) in i:
                        vul_type_ver = i
        
        temp_name = ''
        b = name.split(" ")

        for i in b:
            if i == "-" or i == vul_type_ver:
                break
            else:
                temp_name = temp_name + " " + i
        name = temp_name


        try:
            if vul_type_ver == '':
                continue
            if name == "":
                for q in origin_name.split(" "):
                    if name != "":
                        name = name+q
                    if q[0]=="'":
                        name = name+q
                    if q[-1]=="'":
                        break
            else:
                name = name[1:]
            
            sql = 'INSERT INTO plugins (Serial, UP_Type, name, vul_version, vul_type, wp_version) VALUES (%s, %s, %s, %s, %s, %s)'
            val = (str(counter), 2, str(name) , vul_type_ver, vul_type_name, '0')
            print(str(counter) + " : " + origin_name)
            counter += 1

            # 데이터베이스 원자성
            # 시큐어 코딩 정보 넣어서 테스트해보기

            mycursor.execute(sql, val)

            mydb.commit()
            #print(counter, "record inserted")

        except:
            counter -= 1
            print(name + " ##########error occur")
            pass
except:
    pass


f.close()