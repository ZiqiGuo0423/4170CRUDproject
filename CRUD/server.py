from dataclasses import dataclass
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

popular =   [
                    {
                        'id':'2',
                        'name':'Stanford University',
                        'image':'https://stanfordaande.com/wp-content/uploads/2014/03/sae-slide-01-940x349.jpg',
                        'QS_Ranking' : '2',
                        'short-description':' Founded in 1965, the Department of Computer Science is a center for research and education at the undergraduate and graduate levels.'
                    },   
                    {
                        'id':'1',
                        'name':'Massachusetts Institute of Technology - MIT',
                        'image':'https://news.mit.edu/sites/default/files/download/201810/MIT-Computer-Announce-01-PRESS.jpg',
                        'QS_Ranking' : '1',
                        'short-description':'''The largest graduate program in MIT's School of Engineering, EECS has about 700 graduate students 
                                            in the doctoral program at any given time.'''
                    },
                    {
                        'id':'3',
                        'name':'Carnegie Mellon University',
                        'image':'https://media-exp1.licdn.com/dms/image/C4E1BAQEZiiZeQuQtBQ/company-background_10000/0/1561147531904?e=2159024400&v=beta&t=msMmY-FuMZGB4VaMAc-1neLis5XJSlRhGtMwW0HQ11M',
                        'QS_Ranking' : '3',
                        'short-description' : '''The program is not based on a fixed set of courses. Instead, students construct
                                    their own course of study, in consultation with their advisors, within broad guidelines.'''
                    },
            ] 
            
Data = [
        
        {'1':{
            'id':'1',
            'University_Name':'Massachusetts Institute of Technology - MIT',
            'Image':'https://news.mit.edu/sites/default/files/download/201810/MIT-Computer-Announce-01-PRESS.jpg',
            'QS_Ranking' : '1',
            'Overall_Score' : '93.7',
            'Department_Overview' :'''The largest graduate program in MIT's School of Engineering, EECS has about 700 graduate students in the doctoral program at any given time. Those students conduct groundbreaking research across a wide array of fields alongside world-class faculty and research staff, build lifelong mentorship relationships and drive progress in every sector touched by electrical engineering, computer science, and artificial intelligence and decision-making.''',
            'Application_Fee':'$75',
            'Specialization':['Artificial Intelligence','Bioelectrical Engineering','Circuit Design','Communications','Computational Biology','Computer Architecture','Computer Graphics and Vision','Computer Networks','Control and Decisions Systems','Electromagnetics, Energy, and Power','Human Computer Interaction','Inference','Machine Learning','Materials, Devices, and Photonics','Natural Language and Speech Processing','Programming Languages','Robotics','Signal Processing','Systems','Theoretical Computer Science'],
            'Application_Deadline' : 'December 15',
            'address':'77 Massachusetts Ave. Room 38-401 Cambridge, MA 02139',
            'contact':'grad-ap@eecs@mit.edu'
        }},
    
        {'2':{
            'id' : '2',
            'University_Name' : 'Stanford University',
            'Image':'https://stanfordaande.com/wp-content/uploads/2014/03/sae-slide-01-940x349.jpg',
            'QS_Ranking' : '2',
            'Overall_Score' : '93.1',
            'Department_Overview' : '''Stanford University's Computer Science Department is part of the School of Engineering. The department offers the degrees Bachelor of Science, Master of Science, and Doctor of Philosophy. It also participates in the following undergraduate inter-disciplinary programs: Computer Systems Engineering, Symbolic Systems, and Mathematical and Computational Sciences. Founded in 1965, the Department of Computer Science is a center for research and education at the undergraduate and graduate levels. Strong research groups exist in areas of artificial intelligence, robotics, foundations of computer science, scientific computing, and systems. Basic work in computer science is the main research goal of these groups, but there is also a strong emphasis on interdisciplinary research and on applications that stimulate basic research.''',
            'Application_Fee':'$105',
            'Specialization': ['Artificial Intelligence','Biocomputation','Computer and Network Security','Human-Computer Interaction','Information Management and Analytics','Real-World Computing','Software Theory','Systems','Theoretical Computer Science'],
            'Application_Deadline' : 'December 7',
            'address':'Gates Computer Science Building, 353 Jane Stanford Way, Stanford, CA 94305',
            'contact':'admissions@cs.stanford.edu'
        }},

        {'3':{
            'id':'3',
            'University_Name':'Carnegie Mellon University',
            'Image':'https://media-exp1.licdn.com/dms/image/C4E1BAQEZiiZeQuQtBQ/company-background_10000/0/1561147531904?e=2159024400&v=beta&t=msMmY-FuMZGB4VaMAc-1neLis5XJSlRhGtMwW0HQ11M',
            'QS_Ranking' : '3',
            'Overall_Score' : '93',
            'Department_Overview' :'''The program is not based on a fixed set of courses. Instead, students construct their own course of study, in consultation with their advisors, within broad guidelines. Thus, a student may choose an area in which to specialize (such as networking, machine learning, or algorithms) or choose not to specialize at all. Carnegie Mellon faculty conduct research in diverse areas within the computer sciences and, when there is mutual interest, provide opportunities to Master's students to participate in research, and related activities such as publications, the preparation and defense of a Master's thesis, etc.''',
            'Application_Fee':'$125',
            'Specialization':['COMPUTATIONAL BIOLOGY','COMPUTER SCIENCE','HUMAN-COMPUTER INTERACTION INSTITUTE','INSTITUTE FOR SOFTWARE RESEARCH','LANGUAGE TECHNOLOGIES INSTITUTE','MACHINE LEARNING','ROBOTICS INSTITUTE'],
            'Application_Deadline' : 'December 13',
            'address':'5000 Forbes Avenue, Pittsburgh, PA 15213',
            'contact':'webhelp@cs.cmu.edu'
        }},

        {'4':{
            'id':'4',
            'University_Name':'National University of Singapore - NUS',
            'Image':'https://mcdonnell.wustl.edu/wp-content/uploads/2020/10/NUS.png',
            'QS_Ranking' : '4',
            'Overall_Score' : '90.3',
            'Department_Overview' :'''The NUS School of Computing traces its roots back to the Nanyang University Department of Computer Science that was established in 1975 – the first of its kind in Singapore. Since then, we have developed into one of the leading computing schools in the world, with faculty members who are both internationally recognised researchers and inspiring teachers. We offer outstanding undergraduate and graduate degree programmes across the full spectrum of the field of computing, including Computer Science, Information Systems, Computer Engineering, Business Analytics and Information Security, as well as specialisations in emerging areas of importance such as artificial intelligence, fintech, blockchain, analytics and security. Correspondingly, we attract excellent students and produce talented graduates who are making their mark in the world.''',
            'Application_Fee':'$50',
            'Specialization':['Artificial Intelligence','Computer Science','Infocomm Security','Information Systems'],
            'Application_Deadline' : '15 March',
            'address':'COM1, 13 Computing Drive, Singapore 117417',
            'contact':'secretary_cs@comp.nus.edu.sg'
        }},

        {'5':{
            'id':'5',
            'University_Name':'University of California, Berkeley - UCB',
            'Image':'https://images.ctfassets.net/mrop88jh71hl/6r4boKoLUqOdmn4Q0d8RPw/ecadde2c348d6e811ebe3b165e275c0c/uc_berkeley.jpg',
            'QS_Ranking' : '5',
            'Overall_Score' : '89.5',
            'Department_Overview' :'''Our M.Eng. in EECS program offers innovative graduate courses on scientific and technical topics, organized by technical oncentrations that match your interest. However, success in engineering requires skills that transcend the scientific and technical. In a modern engineering development organization, you almost always have to work in teams, and you must communicate your ideas and influence people (colleagues, investors, customers) through oral and written communication. Even as you tackle difficult technical challenges, you have to consider the match between your ideas and the needs of eventual users, how your choices give your organization a competitive advantage, and how to protect your intellectual property. Increasingly, you have to develop an idea in a multi-disciplinary environment, consider complex systems issues as well as detailed technical issues, and position yourself in an ecosystem of suppliers, and complementary products and strategic relationships. Our Masters of Engineering curriculum has anticipated all this, and prepares you for these real-world challenges.''',
            'Application_Fee':'$140',
            'Specialization':['Data Science and Systems','Physical Electronics and Integrated Circuits','Robotics and Embedded Software','Signal Processing and Communications','Visual Computing and Computer Graphics'],
            'Application_Deadline' : 'January 6th',
            'address':'253 Cory Hall, Berkeley, CA',
            'contact':'gradadmissions@eecs.berkeley.edu'
        }},

        {'6':{
            'id':'6',
            'University_Name':'University of Oxford',
            'Image':'https://www.ox.ac.uk/sites/files/oxford/styles/ow_large_feature/s3/field/field_image_main/b_AllSoulsquad.jpg?itok=tTcH-5ix',
            'QS_Ranking' : '6',
            'Overall_Score' : '89.1',
            'Department_Overview' :'''The Department of Computer Science, University of Oxford has one of the longest-established Computer Science departments in the country. Formerly known as the Oxford University Computing Laboratory, it is home to a community of world-class research and teaching. Research activities encompass core Computer Science, as well as computational biology, quantum computing, computational linguistics, information systems, software verification and software engineering. The department is home to undergraduates, full-time and part-time Master's students, and has a strong doctoral programme.''',
            'Application_Fee':'£75.00',
            'Specialization':['Advanced Computer Science','Mathematics and Foundations of Computer Science','Software Engineering','Software and Systems Security'],
            'Application_Deadline' : '15 October',
            'address':'Department of Computer Science, University of Oxford, Wolfson Building, Parks Road, OXFORD, OX1 3QD, UK',
            'contact':'graduate.admissions@cs.ox.ac.uk'
        }},

        {'7':{
            'id':'7',
            'University_Name':'Harvard University',
            'Image':'https://www.worldbook.com/images/shutterstock_186395066.jpg',
            'QS_Ranking' : '7',
            'Overall_Score' : '88.2',
            'Department_Overview' :'''Computer Science at the Harvard School of Engineering studies both the fundamentals of computation and computation's interaction with the world. Computer scientists develop new algorithms, invent new systems and theories that empower people and society, and advance the science of computing while working with engineers, scientists, social scientists, lawyers, artists, and others around the university and beyond.''',
            'Application_Fee':'Dec.1st',
            'Specialization':['Artificial Intelligence','Computation and Society','Computational and Data Science','Computational Neuroscience','Computer Architecture','Economics and Computation','Graphics, Vision, and Visualization','Human-Computer Interaction','Machine Learning','Programming Languages','Systems, Networks, and Databases','Theory of Computation'],
            'Application_Deadline' : '$105',
            'address':'150 Western Ave, Allston, MA 02134',
            'contact':'admiss@fas.harvard.edu'
        }},

        {'8':{
            'id':'8',
            'University_Name':'University of Cambridge',
            'Image':'https://c.files.bbci.co.uk/BB71/production/_112358974_pa-20968709.jpg',
            'QS_Ranking' : '8',
            'Overall_Score' : '88',
            'Department_Overview' :'''The Department of Computer Science and Technology (known as the Computer Laboratory) is an academic department within the University of Cambridge that encompasses Computer Science, along with many aspects of Technology, Engineering and Mathematics. Professor Ann Copestake is the Head of Department. The Department undertakes research in a broad range of subjects. It has an open and collaborative culture, supporting revolutionary fundamental computer science research, strong cross-cutting collaborations internally and externally, and ideas which transform computing outside the University. Current research areas include bioinformatics, computer architecture, computer vision, distributed systems, graphics and human-computer interaction, logic and semantics, machine learning, natural language processing, networking and wireless communication, operating systems and virtualization, programming, security, and sustainable computing.''',
            'Application_Fee':'£75',
            'Specialization':['M.Phil in Advanced Computer Science','M.Eng in Computer Science'],
            'Application_Deadline' : '10 February',
            'address':'William Gates Building, JJ Thomson Avenue, Cambridge. CB3 0FD',
            'contact':'cst-graduate-admissions@cst.cam.ac.uk'
        }},

        {'9':{
            'id':'9',
            'University_Name':'EPFL',
            'Image':'https://www.epfl.ch/schools/sti/it/wp-content/uploads/ZESCPA6NF52Z33LZKWXJ_prvw_158711.jpg',
            'QS_Ranking' : '9',
            'Overall_Score' : '86.2',
            'Department_Overview' :'''The artifacts and software of the technology revolution have changed peoples' lives in countless ways over the past half century. And, this revolution is not over! The intellectual accomplishments of computer science are diffusing into many other disciplines, changing the way that researchers, practitioners, and people in general see their world and conceive of solutions. We are proud and happy to be at the center of these revolutions.''',
            'Application_Fee':'CHF 150',
            'Specialization':['Computer Engineering','Data Analytics','Foundations of Software','Cyber Security','Networking and Mobility','Signals, Images, and Interefaces','Software System','Wireless Communications','Computer Science Theory','Internet Information System'],
            'Application_Deadline' : 'December 15th',
            'address':'EPFL IC SG-IN, INM 168 (INM Building), Station 14, CH-1015 Lausanne',
            'contact':'corinne.lorireymond@epfl.ch'
        }},

        {'10':{
            'id':'10',
            'University_Name':'ETH Zurich - Swiss Federal Institute of Technology',
            'Image':'https://upload.wikimedia.org/wikipedia/commons/c/cf/ETH_Z%C3%BCrich_am_Abend.jpg',
            'QS_Ranking' : '10',
            'Overall_Score' : '85.6',
            'Department_Overview' :'''The Master's degree programe in Computer Science at ETH Zurich offers a profound and in-depth education in several core areas of computer science. The programme guides each individual student in taking a meaningful path through the variety of course offers and designing a profile that matches both personal inclinations and prospective career opportunities. The Master's degree programme combines theory and hands-on practice to provide students with a well-rounded education.''',
            'Application_Fee':'CHF 150',
            'Specialization':['Data Management Systems','Machine Intelligence','Secure and Reliable Systems','Visual and Interactive Computing','Theoretical Computer Science'],
            'Application_Deadline' : '15 December',
            'address':'Universitätstrasse 6, 8092 Zürich, Switzerland',
            'contact':'studiensekretariat@inf.ethz.ch'
        }}
    
]

count = 10

rank = [
            {
                'id':'1',
                'name':'Massachusetts Institute of Technology - MIT',
                'QS_Ranking' : '1',
                'Overall_Score' : '93.7'
            },
            {
                'id':'2',
                'name': 'Stanford University',
                'QS_Ranking' : '2',
                'Overall_Score' : '93.1'
            },
            {
                'id':'3',
                'name': 'Carnegie Mellon University',
                'QS_Ranking' : '3',
                'Overall_Score' : '93'
            },
            {
                'id':'4',
                'name':'National University of Singapore - NUS',
                'QS_Ranking' : '4',
                'Overall_Score' : '90.3'
            },
            {
                'id':'5',
                'name': 'University of California, Berkeley - UCB',
                'QS_Ranking' : '5',
                'Overall_Score' : '89.5'
            },
            {
                'id':'6',
                'name':'University of Oxford',
                'QS_Ranking' : '6',
                'Overall_Score' : '89.1'
            },
            {
                'id':'7',
                'name':'Harvard University',
                'QS_Ranking' : '7',
                'Overall_Score' : '88.2'
            },
            {
                'id':'8',
                'name':'University of Cambridge',
                'QS_Ranking' : '8',
                'Overall_Score' : '88'
            },
            {
                'id':'9',
                'name':'EPFL',
                'QS_Ranking' : '9',
                'Overall_Score' : '86.2'
            },
            {
                'id':'10',
                'name':'ETH Zurich - Swiss Federal Institute of Technology',
                'QS_Ranking' : '10',
                'Overall_Score' : '85.6'
            }
        ]

@app.route('/')
def hello():
    global popular
    return render_template('homepage.html')



@app.route('/display_popular', methods=['GET', 'POST'])
def diaplay_popular():
    global popular

    #create a response in json format
    return jsonify(popular)   


@app.route('/rank/<id>')
def diaplay_rank(id = None):
    id = id
    global rank
    return render_template('rank.html', rank = rank, id = id) 


@app.route('/search_results/<search_word>')
def search(search_word = None):
    global Data
    word = search_word
    print(word)
    lst = []
    address_match = []
    email_match = []

    for i in range(len(Data)):
        j = i+1
        university = Data[i][str(j)]
        if word.lower() in university['University_Name'].lower():
            dic = {'id': str(j), 'name': university['University_Name']}
            lst.append(dic)
        if word.lower() in university['address'].lower():
            dic_add = {'id': str(j),'address':university['address']}
            address_match.append(dic_add)
        if word.lower() in university['contact'].lower():
            dic_con = {'id': str(j),'contact':university['contact']}
            email_match.append(dic_con)

    if len(lst) >= 1 or len(email_match) >= 1 or len(address_match) >= 1:
        return render_template('search.html',result = lst, result_add = address_match, result_email = email_match, word = word, quantity = len(lst) +len(address_match)+ len(email_match))
    else:
        return render_template('no_result.html', word = word)


@app.route('/view/<id>')
def view(id = None):
    global Data
    
    for i in range(len(Data)):
        j = i+1
        university = Data[i][str(j)]
        if university['id'] == id:
            res = Data[i][str(j)]
            return render_template('view.html',university = res)


@app.route('/add')
def adddata():
    return render_template('add.html')



@app.route('/save_data', methods=['GET', 'POST'])
def save_sale():
    global rank
    global Data
    global count

    count += 1

    json_data = request.get_json()  

    University_Name = json_data["u-name"]
    Image = json_data["u-url"]
    QS_Ranking = json_data["u-rank"]
    Overall_Score = json_data["u-score"]
    Department_Overview = json_data["u-view"]
    Application_Fee = json_data["u-fee"]
    Specialization = json_data['u-specialization']
    specialization_split = Specialization.split(',')
    Application_Deadline = json_data['u-deadline']
    address = json_data['u-add']
    contact = json_data['u-email']
  
    new_record_entry = {
        str(count) : {
        "id":  str(count),
        "University_Name":  University_Name,
        "Image": Image,
        "QS_Ranking": QS_Ranking,
        "Overall_Score" : Overall_Score,
        "Department_Overview": Department_Overview,
        "Application_Fee": Application_Fee,
        "Specialization": specialization_split,
        "Application_Deadline" : Application_Deadline,
        "address" : address,
        "contact" : contact
        }
    }

    new_rank_entry = {
        'id':str(count),
        'name':University_Name,
        'QS_Ranking' : QS_Ranking,
        'Overall_Score' : Overall_Score
    }

    print(new_record_entry)
    
    Data.append(new_record_entry)

    # add new entry in rank array
    for i in range(len(rank)):
        if (int(rank[i]['QS_Ranking']) < int(QS_Ranking)) and (i+1 < len(rank)) and (int(rank[i+1]['QS_Ranking']) < int(QS_Ranking)):
            continue
        if i+1 == len(rank):
            rank.append(new_rank_entry)
        else:
            rank.insert(i+1,new_rank_entry)
            break

    # #send back the WHOLE array of data, so the client can redisplay it
    return jsonify(university = new_record_entry, id = str(count))



@app.route('/edit/<id>')
def edit(id = None):
    global Data
    global count
    global rank

    for i in range(len(Data)):
        if id == Data[i][str(i+1)]['id']:
            editData = Data[i][str(i+1)]

    print(editData)

    return render_template('edit.html', edit = editData)


@app.route('/save_edit', methods=['GET', 'POST'])
def save_edit():
    global Data
    global rank

    json_data = request.get_json()
    print(json_data)

    id = json_data['id']
    print(type(id))

    # delete from Data
    for i in range(len(Data)):
        if id == Data[i][str(i+1)]['id']:
            Data.remove(Data[i])
            break
    
    # reinsert into Data
    University_Name = json_data["u-name"]
    Image = json_data["u-url"]
    QS_Ranking = json_data["u-rank"]
    Overall_Score = json_data["u-score"]
    Department_Overview = json_data["u-view"]
    Application_Fee = json_data["u-fee"]
    Specialization = json_data['u-specialization']
    specialization_split = Specialization.split(',')
    Application_Deadline = json_data['u-deadline']
    address = json_data['u-add']
    contact = json_data['u-email']

    new_record_entry = {
        id : {
        "id":  id,
        "University_Name":  University_Name,
        "Image": Image,
        "QS_Ranking": QS_Ranking,
        "Overall_Score" : Overall_Score,
        "Department_Overview": Department_Overview,
        "Application_Fee": Application_Fee,
        "Specialization": specialization_split,
        "Application_Deadline" : Application_Deadline,
        "address" : address,
        "contact" : contact
        }
    }

    print(new_record_entry)

    Data.insert(int(id)-1,new_record_entry)

    # delete from rank
    for j in range(len(rank)):
        if id == rank[j]['id']:
            rank.remove(rank[j])
            break
    
    # reinsert to the rank
    new_rank_entry = {
        'id':id,
        'name':University_Name,
        'QS_Ranking' : QS_Ranking,
        'Overall_Score' : Overall_Score
    }

    for i in range(len(rank)):
        if (int(rank[i]['QS_Ranking']) < int(QS_Ranking)) and (i+1 < len(rank)) and (int(rank[i+1]['QS_Ranking']) <= int(QS_Ranking)):
            continue
        if i+1 == len(rank):
            rank.append(new_rank_entry)
        elif i == 0:
            rank.insert(i,new_rank_entry)
            break
        else:
            rank.insert(i+1,new_rank_entry)
            break

    
    # if the data be edited is one of the popular, we need to modify the popular as well
    for j in range(len(popular)):
        if id == popular[j]['id']:
            popular.remove(popular[j])
            break
    
    # reinsert into popular

    new_popular = {
        'id':id,
        'name':University_Name,
        'image':Image,
        'QS_Ranking' : QS_Ranking,
        'short-description':Department_Overview[:180]+'...'
    }
    popular.append(new_popular)

    return jsonify(university = new_record_entry)



if __name__ == '__main__':
   app.run(debug = True)