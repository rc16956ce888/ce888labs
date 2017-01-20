from sopel import module
from emo.wdemotions import EmotionDetector

global data
global cnt

data = [0, 0, 0, 0, 0, 0]
cnt = 0
emo = EmotionDetector()


@module.rule('')
def hi(bot, trigger):
    print(trigger, trigger.nick)
    #bot.say('Hi, ' + trigger.nick)
    temp = emo.detect_emotion_in_raw_np(str(trigger))
    i = 0

    for val in data:
        data[i] = temp[i] + data[i]
        i = i + 1

    count = 0
    i = 0
    for val in data:
        count = count + data[i]
        i += 1

    print(data)


