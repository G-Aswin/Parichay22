import db

departments = db.department
winners = db.winners

dep_list = departments.find(
    {},
    {
        '_id':0,
        'dept_name':1
    }
    )
# print(dep_list[0])

"""
we only need to change the score after the winner is announced, score of the department increases in winner branch,
retrieve recent score change
update the score of the respective branch 
reflect change

"""

win_list = winners.find({})

# print(len(dict(win_list)))

# def update_scoreboard():



# board = {   'Computer Science': 0, 
#             'Data Science': 0, 
#             'AI ML': 0, 
#             'Mechanical': 0, 
#             'MCA': 0, 'Civil': 0, 
#             'Electronics and Communication': 0, 
#             'Electronics and Instrumentation': 0, 
#             'Electrical and Electronics': 0, 
#             'Information Science': 0
#         }
   
