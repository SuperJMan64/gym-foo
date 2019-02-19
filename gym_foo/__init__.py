from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='foo-v0',
    entry_point='gym_foo.envs:FooEnv',
)

register(
    id='foo-extrahard-v0',
    entry_point='gym_foo.envs:FooExtraHardEnv',
)
