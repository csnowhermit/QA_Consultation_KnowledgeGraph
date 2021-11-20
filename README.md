# QA_Consultation_KnowledgeGraph

基于知识图谱的医药问诊问答系统

## 1、Requirements

jdk 11

neo4j

## 2、neo4j配置远程访问

``` shell
vim $NEO4J_HOME/conf/neo4j.conf

修改如下内容：
# Bolt connector
dbms.connector.bolt.enabled=true
#dbms.connector.bolt.tls_level=DISABLED
dbms.connector.bolt.listen_address=0.0.0.0:7687    # 默认没有IP，修改为0.0.0.0
#dbms.connector.bolt.advertised_address=:7687

# HTTP Connector. There can be zero or one HTTP connectors.
dbms.connector.http.enabled=true
dbms.connector.http.listen_address=0.0.0.0:7474    # 默认没有IP，修改为0.0.0.0
#dbms.connector.http.advertised_address=:7474
```

## 3、构建知识图谱

``` python
python build_graph.py
```

## 4、运行结果

``` Python
python chatbot_app.py

'''
运行效果如下：

提问：苯中毒怎么治
客服机器人： 苯中毒可以尝试如下治疗：药物治疗;支持性治疗

提问：苯中毒有什么注意事项
客服机器人： 苯中毒,熟悉一下：苯(benzene)是从煤焦油分馏及石油裂解所得的一种芳香烃化合物，系无色有芳香气味的油状液体。挥发甚速，易燃易爆。工业上用作溶剂、稀释剂和化工原料。苯属中等毒类，可引起急性或慢性中毒。
急性苯中毒是指口服含苯的有机溶剂或吸入高浓度苯蒸气后，出现以中枢神经系统麻醉作用为主要表现的病理生理过程，主要症状轻者为醉酒状，步态不稳，哭笑失常，重者意识丧失，抽搐，可因呼吸中枢麻痹或循环衰竭死亡。慢性苯中毒是指苯及其代谢产物酚类影响了骨髓的造血功能，临床表现为白细胞计数和血小板立秋持续减少，最终发展为再生障碍性贫血或白血病。也可影响神经系统，表现为神经衰弱和自主神经功能紊乱。

提问：苯中毒饮食方面有什么注意的
客服机器人： 苯中毒忌食的食物包括有：海虾；海蟹；辣椒(青、尖)；海参（水浸）
'''
```

