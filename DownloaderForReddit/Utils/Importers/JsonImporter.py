"""
Downloader for Reddit takes a list of reddit users and subreddits and downloads content posted to reddit either by the
users or on the subreddits.


Copyright (C) 2017, Kyle Hickey


This file is part of the Downloader for Reddit.

Downloader for Reddit is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Downloader for Reddit is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Downloader for Reddit.  If not, see <http://www.gnu.org/licenses/>.
"""

import json
import logging

from ...Core.RedditObjects import User, Subreddit


logger = logging.getLogger(__name__)


def import_list_from_json(file_path):
    """
    Imports a list of reddit objects from the json file at the supplied file path.
    :param file_path: The path to the json file from which to build the user list.
    :return: A list of RedditObjects built from the supplied json file.
    """
    with open(file_path, 'r') as file:
        objects = json.load(file)['object_list']

    reddit_objects = []
    for ro in objects:
        reddit_object = make_reddit_object(ro)
        if reddit_object is not None:
            reddit_objects.append(reddit_object)
    logger.info('Imported from file', extra={'import_count': len(reddit_objects)})
    return reddit_objects if len(reddit_objects) > 0 else None


def make_reddit_object(element):
    """
    Creates a User or Subreddit object, depending on the object type of the supplied element, with the attributes
    imported from the supplied json element.
    :param element: The element that the reddit object is to be built from.
    :return: A RedditObject build from the attributes of the supplied element.
    """
    try:
        name = element['name']
        version = element['version']
        save_path = element['save_path']
        post_limit = int(element['post_limit'])
        avoid_duplicates = bool(element['avoid_duplicates'])
        download_videos = bool(element['download_videos'])
        download_images = bool(element['download_images'])
        nsfw_filter = element['nsfw_filter']
        name_downloads_by = element['name_downloads_by']
        subreddit_save_method = element['subreddit_save_method']
        date_limit = int(element['date_limit_epoch'])
        custom_date_limit = element['custom_date_limit_epoch']
        added_on = element['added_on_epoch']
        lock = element['lock']
        save_undownloaded_content = element['save_undownloaded_content']
        download_enabled = element['download_enabled']

        if element['object_type'] == 'USER':
            reddit_object = User(version, name, save_path, post_limit, avoid_duplicates, download_videos, download_images,
                                 nsfw_filter, name_downloads_by, added_on)
        else:
            reddit_object = Subreddit(version, name, save_path, post_limit, avoid_duplicates, download_videos,
                                      download_images, nsfw_filter, subreddit_save_method, name_downloads_by, added_on)
        reddit_object.date_limit = date_limit
        reddit_object.custom_date_limit = int(custom_date_limit) if custom_date_limit is not None else None
        reddit_object.lock = lock
        reddit_object.save_undownloaded_content = save_undownloaded_content
        reddit_object.enable_download = download_enabled
        return reddit_object
    except:
        logger.warning('Failed to import reddit object from json element', exc_info=True)
        return None
