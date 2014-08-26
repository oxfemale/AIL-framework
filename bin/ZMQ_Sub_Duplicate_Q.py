#!/usr/bin/env python2
# -*-coding:UTF-8 -*

from pubsublogger import publisher

import Helper

if __name__ == "__main__":
    publisher.port = 6380
    publisher.channel = 'Queuing'

    config_section = 'PubSub_Global'
    config_channel = 'channel'
    subscriber_name = 'duplicate'

    h = Helper.Redis_Queues(config_section, config_channel, subscriber_name)
    h.redis_queue_subscribe(publisher)
