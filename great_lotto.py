import random
import time


def create_number_list():
    red_ball = list(range(1, 36))  # 35个号码球
    blue_ball = list(range(1, 13))  # 16个号码球

    anticipate_red = []  # 预测出的红球数组
    anticipate_blue = []  # 预测出的篮球
    # 抽6个红球
    for i in range(0, 5):
        time.sleep(random.uniform(0, 0.00055))  # 随机等待时间（随机时间执行摇出不同个球）
        anticipate_red.append(red_ball.pop(random.choice(range(0, 35 - i))))  # 记录随机抽出的红球

    anticipate_red.sort()  # 顺序
    # anticipate_red.reverse()  # 倒序
    for i in range(0, 2):
        time.sleep(random.uniform(0, 0.00056))  # 随机等待时间（随机时间执行摇出不同个球）
        anticipate_blue.append(blue_ball.pop(random.choice(range(0, 12 - i))))  # 记录随机抽出的蓝球

    anticipate_blue.sort()  # 顺序

    return anticipate_red, anticipate_blue


def main():
    print('大乐透摇号中')
    create_count = 4  # 预测4组
    all_count = random.choice(range(100, 200))
    ball_group = []
    anwser_group = []
    for i in range(0, all_count):
        time.sleep(random.uniform(0, 0.00314159))
        ball_group.append(create_number_list())
    for i in range(0, create_count):
        time.sleep(random.uniform(0, 0.00055))  # 随机等待时间（随机时间执行摇出不同个球）
        anwser_group.append(ball_group.pop(random.choice(range(0, all_count - i))))  # 记录随机抽出的红球
    for i in anwser_group:
        print('前区号码：{}'.format(i[0]), '   后区号码：{}'.format(i[1]))
        # print()

if __name__ == '__main__':
    main()

