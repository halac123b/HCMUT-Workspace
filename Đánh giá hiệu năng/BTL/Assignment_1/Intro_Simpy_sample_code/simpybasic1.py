import simpy


def timer(env, duration=5):
    while True:
        print('Start timer at %d' % env.now)
        yield env.timeout(duration)
        print('End timer at %d' % env.now)


env = simpy.Environment()
env.process(timer(env, 3))
env.run(until=20)
