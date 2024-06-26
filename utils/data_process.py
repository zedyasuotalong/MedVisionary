from utils.debug import DEBUG
from datetime import datetime
# 数据模型类===》普通字典
#    msg/[msg,msg,msg]    属性清单,

#                  数据源     数据模型类属性    type为0，data_list是一个list； type非0，data_list就是一条数据
def Class_To_Data(data_list,fields,type=0):
    
    # DEBUG(data_list=data_list)

    if not type:  #[obj,obj]
        msg_list = []  
        for u in data_list:
            # DEBUG(u=u)
            temp = {}
            for f in fields:
                # DEBUG(f=f)
                d = getattr(u,f)
                if isinstance(d, datetime):
                    d = d.strftime('%Y-%m-%d %H:%M:%S')
                temp[f] = d
            msg_list.append(temp)
    else:   #   obj
        msg_list = {}
        for f in fields:
            # DEBUG(f=f)
            msg_list[f] = getattr(data_list, f)

    return msg_list