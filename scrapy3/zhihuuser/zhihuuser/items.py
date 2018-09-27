# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class UserItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = Field()
    name = Field()
    avatar_url = Field()
    answer_count = Field()
    avatar_url_template = Field()
    description = Field()
    follower_count = Field()
    headline = Field()
    type = Field()
    url = Field()
    url_token = Field()
    participated_live_count = Field()
    hosted_live_count = Field()
    mutual_followees_count = Field()
    marked_answers_count = Field()
    following_topic_count = Field()
    following_question_count = Field()
    following_favlists_count = Field()
    voteup_count = Field()
    vote_to_count = Field()
    vote_from_count = Field()
    thanked_count = Field()
    thank_to_count = Field()
    thank_from_count = Field()
    question_count = Field()
    pins_count = Field()
    following_count = Field()
    following_columns_count = Field()
    favorited_count = Field()
    favorite_count = Field()
    commercial_question_count = Field()
    articles_count = Field()
    badge =  Field()
    cover_url = Field()
    gender = Field()


    employments = Field()
    locations = Field()
    educations = Field()

