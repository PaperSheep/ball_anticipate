import random
import time


def create_number_list():
    red_ball = list(range(1, 34))  # 33个号码球
    blue_ball = list(range(1, 17))  # 16个号码球

    anticipate_red = []  # 预测出的红球数组
    anticipate_blue = 0  # 预测出的篮球
    # 抽6个红球
    for i in range(0, 6):
        time.sleep(random.uniform(0, 0.73))  # 随机等待时间（随机时间执行摇出不同个球）
        anticipate_red.append(red_ball.pop(random.choice(range(0, 33 - i))))  # 记录随机抽出的红球

    anticipate_red.sort()  # 顺序
    # anticipate_red.reverse()  # 倒序

    anticipate_blue = blue_ball.pop(random.choice(range(0, 16)))  # 记录随机抽出的蓝球

    print('红球号码:{}'.format(anticipate_red))
    print('篮球号码:{}\n'.format(anticipate_blue))

def main():
    create_count = 4  # 预测4组
    for i in range(0, 4):
        time.sleep(random.uniform(0, 3.14159))
        create_number_list()
    print('随机模拟结束')

if __name__ == '__main__':
    main()

