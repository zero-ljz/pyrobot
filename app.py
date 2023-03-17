import werobot

robot = werobot.WeRoBot(token='tokenhere')

@robot.handler
def echo(message):
    return 'Hello World!'

robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80

robot.run()


# 1
