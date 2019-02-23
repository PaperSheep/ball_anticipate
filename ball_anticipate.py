import random
import time


def create_number_list():
    red_ball = list(range(1, 34))  # 33个号码球
    blue_ball = list(range(1, 17))  # 16个号码球

    anticipate_red = []  # 预测出的红球数组
    anticipate_blue = 0  # 预测出的篮球
    # 抽6个红球
    for i in range(0, 6):
        time.sleep(random.uniform(0, 0.0055))  # 随机等待时间（随机时间执行摇出不同个球）
        anticipate_red.append(red_ball.pop(random.choice(range(0, 33 - i))))  # 记录随机抽出的红球

    anticipate_red.sort()  # 顺序
    # anticipate_red.reverse()  # 倒序
    anticipate_blue = blue_ball.pop(random.choice(range(0, 16)))  # 记录随机抽出的蓝球

    return anticipate_red, anticipate_blue

    # print('红球号码:{}'.format(anticipate_red))
    # print('篮球号码:{}\n'.format(anticipate_blue))

def main():
    print('双色球摇号中')
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
        print('红球号码：{}'.format(i[0]), '   篮球号码：{}'.format(i[1]))


if __name__ == '__main__':
    main()

