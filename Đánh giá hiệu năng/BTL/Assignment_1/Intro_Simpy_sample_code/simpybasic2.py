import simpy


def timer(env, name, resource, duration=5):
    with resource.request() as req:
        yield req

        print('Start timer %s at %d' % (name, env.now))
        yield env.timeout(duration)
        print('End timer %s at %d' % (name, env.now))


env = simpy.Environment()
# capacity changes the number of generators in the system.
server1 = simpy.Resource(env, capacity=1)
for i in range(4):
    env.process(timer(env, 'Timer %s' % i, server1, i+1))
env.run()
