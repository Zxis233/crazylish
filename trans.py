import random
import jieba

# 填入自己要发电的话
origin_word = '人活着哪有不疯的？硬撑罢了！人活着哪有不疯的？硬撑罢了！人活着哪有不疯的？硬撑罢了！人活着哪有不疯的？硬撑罢了！妈的，忍不了，一拳把地球打爆！妈的，忍不了，一拳把地球打爆！妈的，忍不了，一拳把地球打爆！妈的，忍不了，一拳把地球打爆！妈的，忍不了，一拳把地球打爆！妈的，忍不了，一拳把地球打爆！妈的，忍不了，一拳把地球打爆！妈的，忍不了，一拳把地球打爆！妈的，忍不了，一拳把地球打爆！妈的，忍不了，一拳把地球打爆！'

# 填入替换列表
replace_list = ["▮"]
# replace_list = ["$", "&", "*", "?", "@", "#", "!", "^^", "%", "~"]

# 步进机制
steady_up = 1

# 替换几率
replace_rate = 0.12

# 是否开启结巴分词
enable_jieba = 0

seg_list = list(jieba.cut(origin_word))


# print(seg_list)

def replace_words(word: str, rdm_num: int):
    for i in range(len(word)):
        word = ("".join(replace_list[rdm_num]))
    return word


def replace_char(old_string, char, index):
    """
    字符串按索引位置替换字符
    old_string: 原始字符串
    char： 要替换成啥？
    index： 下标
    """
    old_string = str(old_string)
    new_string = old_string[:index] + char + old_string[index + 1:]
    return new_string


if enable_jieba == 1:

    if steady_up == 1:

        for i in range(len(seg_list)):

            if random.random() < replace_rate:
                random_num = random.randint(0, len(replace_list) - 1)
                words = seg_list[i]
                seg_list[i] = replace_words(words, random_num)

            replace_rate += replace_rate / len(seg_list)

    else:
        for i in range(len(seg_list)):

            if random.random() < replace_rate:
                random_num = random.randint(0, len(replace_list) - 1)
                words = seg_list[i]
                seg_list[i] = replace_words(words, random_num)

    print("".join(seg_list))

else:

    if steady_up == 1:

        for i in range(len(origin_word)):

            if random.random() < replace_rate:
                random_num = random.randint(0, len(replace_list) - 1)
                origin_word = replace_char(origin_word, replace_list[random_num], i)

            replace_rate += replace_rate / len(origin_word)

    else:
        for i in range(len(origin_word)):

            if random.random() < replace_rate:
                random_num = random.randint(0, len(replace_list) - 1)
                origin_word = replace_char(origin_word, replace_list[random_num], i)

    print(origin_word)
