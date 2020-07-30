# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "debian-sys-maint",
    passwd = "Mr4fyaurpDIuAdE2",
    database = "testdb",
)
# Create Cursor Instance
my_cursor = mydb.cursor()

### start : list of title, subtitle, content
import os

f_name_txt = []
f_name_txt = [f for f in os.listdir("/home/ubuntu/law/data/total_txt") if
f.endswith('.txt')]

f_name = []
for i in range(0,len(f_name_txt)):
    f_name.append("File"+str(i))

print(len(f_name))
title = []
subtitle = []
content = []

for i, name in enumerate(f_name):
    with open("/home/ubuntu/law/data/total_txt/" + name +".txt", 'r') as f:
        data = f.readlines()
        p_title = data[0]
        p_subtitle = data[1]
        p_content = ' '.join(str(data) for data in data[2:])
        title.append(p_title)
        subtitle.append(p_subtitle)
        content.append(p_content)
### end : list of title, subtitle, content

### start : commit title, subtitle, content
for i in range(0, len(f_name)):
    a = i
    b = title[i]
    c = subtitle[i]
    d = content[i]
    # Insert Multiple Records

    sqlStuff = """INSERT INTO posts_post (fileid, title, subtitle, content) VALUES (%s, %s, %s, %s)"""
    records = [
        (a, b, c, d)
    ]
    my_cursor.executemany(sqlStuff, records)
    mydb.commit()
### end : commit title, subtitle, content




# import mysql.connector
#
# mydb = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     passwd = "recon0928",
#     database = "testdb",
# )
# # Create Cursor Instance
# my_cursor = mydb.cursor()
#
# ### start : list of title, subtitle, content
# import os
#
# #### 파일 이름 만들기 ###
# file_name = []
# f_name_txt = []
# f_name_txt = [f for f in os.listdir("/Users/sim_macbookpro/projects/project_judical_precednet_not_py/download_j_precednet/jp_by_4000/total_txt") if
# f.endswith('.txt')]
#
# f_name = []
# for i in range(0,len(f_name_txt)):
#     f_name.append("File"+str(i))
#
# for name in f_name:
#     sentences = open("/Users/sim_macbookpro/projects/project_judical_precednet_not_py/download_j_precednet/jp_by_4000/total_txt/" + name +".txt").readlines()
#     sen1 = sentences[2:]
#     sen3 = []
#     for sen2 in sen1:
#         if sen2 == '\n':
#             pass
#         elif sen2.find('【') == False:
#             pass
#         else:
#             sen3.append(sen2)
#     for o, sen in enumerate(sen3):
#         file_name.append(name+'_Sen'+ str(o))
#
# print(len(file_name))
# ####   ####
#
# ### start : list of content
# content = []
# for i, name in enumerate(file_name):
#     with open("/Users/sim_macbookpro/projects/project_judical_precednet_not_py/download_j_precednet/jp_by_4000/total_sentences_wakati/" + name, 'r') as f:
#         data = f.read()
#         p_content = str(data).strip()
#         content.append(p_content)
# ### end : list of content
#
# ### start : commit content
# for i in range(0, len(file_name)):
#     a = i
#     b = file_name[i]
#     c = content[i]
#     # Insert Multiple Records
#
#     sqlStuff = "INSERT INTO posts_sentence (s_id, s_fileid, s_content) VALUES (%s, %s, %s)"
#     records = [
#         (a, b, c)
#     ]
#     my_cursor.executemany(sqlStuff, records)
#     mydb.commit()
# ### end : commit title, subtitle, content
