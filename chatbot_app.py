from question_classifier import *
from question_parser import *
from answer_search import *

'''
    问答机器人
'''
class ChatBotGraph:
    def __init__(self):
        self.classifier = QuestionClassifier()
        self.parser = QuestionPaser()
        self.searcher = AnswerSearcher()

    def chat_main(self, sent):
        answer = '没能理解您的问题，要不换个问法'
        res_classify = self.classifier.classify(sent)    # 对问题进行分类
        if not res_classify:    # 没解析到关键词的话，直接返回空，直接返回预定answer
            return answer
        res_sql = self.parser.parser_main(res_classify)    # 拼接cql
        final_answers = self.searcher.search_main(res_sql)    # 根据cql查询neo4j，得出结果
        if not final_answers:    # 如果没找到，直接返回预定answer
            return answer
        else:
            return '\n'.join(final_answers)

if __name__ == '__main__':
    handler = ChatBotGraph()
    while True:
        question = input('提问：')
        answer = handler.chat_main(question)
        print('客服机器人：', answer, "\n")

