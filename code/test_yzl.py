import numpy as np
domain_dict={"MR":np.array([]),"apparel":np.array([]),"baby":np.array([]),"books":np.array([]),"camera_photo":np.array([]),"dvd":np.array([]),"electronics":np.array([]),"health_personal_care":np.array([]),"imdb":np.array([]),"kitchen_housewares":np.array([]),"magazines":np.array([]),"music":np.array([]),"software":np.array([]),"sports_outdoors":np.array([]),"toys_games":np.array([]),"video":np.array([]),"test":np.array([])}
with open("/home/yzl/MDTC/MAN/man/code/log.txt","r",encoding="utf-8") as f:
    lines=f.readlines()
    flag=0
    for l in lines:
        if "test" in l:
            flag=1
        if "validation" in l:
            flag=0
        if flag==0:
            continue
        if "MR" in l:
            # print(l.split(" ")[-1].replace("%",""))
            domain_dict["MR"]=np.append(domain_dict["MR"],float(l.split(" ")[-1].replace("%","")))
        elif "apparel" in l:
            domain_dict["apparel"]=np.append(domain_dict["apparel"],float(l.split(" ")[-1].replace("%","")))
        elif "baby" in l:
            domain_dict["baby"]=np.append(domain_dict["baby"],float(l.split(" ")[-1].replace("%","")))
        elif "books" in l:
            domain_dict["books"]=np.append(domain_dict["books"],float(l.split(" ")[-1].replace("%","")))
        elif "camera_photo" in l:
            domain_dict["camera_photo"]=np.append(domain_dict["camera_photo"],float(l.split(" ")[-1].replace("%","")))
        elif "dvd" in l:
            domain_dict["dvd"]=np.append(domain_dict["dvd"],float(l.split(" ")[-1].replace("%","")))
        elif "electronics" in l:
            domain_dict["electronics"]=np.append(domain_dict["electronics"],float(l.split(" ")[-1].replace("%","")))
        elif "health_personal_care" in l:
            domain_dict["health_personal_care"]=np.append(domain_dict["health_personal_care"],float(l.split(" ")[-1].replace("%","")))
        elif "imdb" in l:
            domain_dict["imdb"]=np.append(domain_dict["imdb"],float(l.split(" ")[-1].replace("%","")))
        elif "kitchen_housewares" in l:
            domain_dict["kitchen_housewares"]=np.append(domain_dict["kitchen_housewares"],float(l.split(" ")[-1].replace("%","")))
        elif "magazines" in l:
            domain_dict["magazines"]=np.append(domain_dict["magazines"],float(l.split(" ")[-1].replace("%","")))
        elif "music" in l:
            domain_dict["music"]=np.append(domain_dict["music"],float(l.split(" ")[-1].replace("%","")))
        elif "software" in l:
            domain_dict["software"]=np.append(domain_dict["software"],float(l.split(" ")[-1].replace("%","")))
        elif "sports_outdoors" in l:
            domain_dict["sports_outdoors"]=np.append(domain_dict["sports_outdoors"],float(l.split(" ")[-1].replace("%","")))
        elif "toys_games" in l:
            domain_dict["toys_games"]=np.append(domain_dict["toys_games"],float(l.split(" ")[-1].replace("%","")))
        elif "video" in l:
            domain_dict["video"]=np.append(domain_dict["video"],float(l.split(" ")[-1].replace("%","")))
        elif "Average test accuracy" in l:
            domain_dict["test"]=np.append(domain_dict["test"],float(l.split(" ")[-1]))
            flag=0

for item in domain_dict:
    print("{} average = {}".format(item,np.mean(domain_dict[item])))
                

