import db

departments = db.department
winner_doc = db.winners    

dep_list = departments.find(
    {},
    {
        '_id':1,
        'dept_name':1
    }
    )

dep_dict = {}

for dep in dep_list:
	dep_dict[str(dep['_id'])] = dep['dept_name']

board = {   
            'Computer Science': 0, 
            'Data Science': 0, 
            'AI ML': 0, 
            'Mechanical': 0, 
            'MCA': 0, 'Civil': 0, 
            'Electronics and Communication': 0, 
            'Electronics and Instrumentation': 0, 
            'Electrical and Electronics': 0, 
            'Information Science': 0
        }

def isIncreased(count) -> bool:
    winner_list = winner_doc.find({})
    win_count = 0
    for win in winner_list:
        win_count+=1
    return win_count > count

def update_score():
    doc = winner_doc.find(
        {},
        {
            '_id':0,
            'dept_id':1,
            'points_scored':1
        }
    ).sort("_id",-1).limit(1)

    concerned_department_id = doc[0]['dept_id']
    score_to_be_updated = doc[0]['points_scored']
    department_name = dep_dict[str(concerned_department_id)]
    board[str(department_name)] += score_to_be_updated
    print(board)

    


    
    








"""
we only need to change the score after the winner is announced, score of the department increases in winner branch,
retrieve recent score change
update the score of the respective branch 
reflect change

"""





   
