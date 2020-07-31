def twitch_topic_string(channel_id, topics=['subscriptions']):
    """Function for generating valid twitch PubSub topic strings

    Args:
        channel_id (str): Twitch Identifier for channel
        topics (str list, optional): Topics wanting to be subscribed to updates from. Defaults to ['subscriptions'].

    Returns:
        str list: List of topics wanting to be subscribed to
    """
    topic_types = {
        'bits_v1': 'channel-bits-events-v1',
        'bits_v2': 'channel-bits-events-v2',
        'bits_badge': 'channel-bits-badge-unlocks',
        'points': 'channel-points-channel-v1',
        'subscriptions': 'channel-subscribe-events-v1',
        'chat': 'chat_moderator_actions',
        'whispers': 'whispers'
    }
    topics_string = []
    for topic in topics:
        topics_string.append(f"{topic_types.get(topic)}.{channel_id}")
    return topics_string