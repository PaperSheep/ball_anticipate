import random
import time


def create_number_list():
    red_ball = list(range(1, 36))  # 35个号码球
    blue_ball = list(range(1, 13))  # 16个号码球

    anticipate_red = []  # 预测出的红球数组
    anticipate_blue = []  # 预测出的篮球
    # 抽6个红球
    for i in range(0, 5):
        time.sleep(random.uniform(0, 0.73))  # 随机等待时间（随机时间执行摇出不同个球）
        anticipate_red.append(red_ball.pop(random.choice(range(0, 35 - i))))  # 记录随机抽出的红球

    anticipate_red.sort()  # 顺序
    # anticipate_red.reverse()  # 倒序
    for i in range(0, 2):
        time.sleep(random.uniform(0, 0.73))  # 随机等待时间（随机时间执行摇出不同个球）
        anticipate_blue.append(blue_ball.pop(random.choice(range(0, 12 - i))))  # 记录随机抽出的蓝球

    anticipate_blue.sort()  # 顺序

    print('红球号码:{}'.format(anticipate_red))
    print('篮球号码:{}\n'.format(anticipate_blue))

def main():
    print('大乐透摇号中')
    create_count = 4  # 预测4组
    for i in range(0, 4):
        time.sleep(random.uniform(0, 3.14159))
        create_number_list()
    print('随机模拟结束')

if __name__ == '__main__':
    main()

