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

from DownloaderForReddit.RedditObjects.RedditObjects import User, Subreddit
from ..Utils import Injector
from DownloaderForReddit.RedditObjects.Post import Post
from ..version import __version__


class ObjectUpdater:

    """
    A class that updates outdated reddit objects that have been loaded from a pickled state to a new version of the
    objects with current methods and attributes that are needed to be used in the current version of the app.
    """

    @classmethod
    def update_user(cls, user):
        """
        Creates a new User object with current methods and attributes and fills in the new users attributes with
        attributes from the old user object.
        :param user: The User object which is to be updated.
        :type user: User
        """
        new_user = User(__version__, user.name, None, user.post_limit, user.avoid_duplicates,
                        user.download_videos, user.download_images, cls.get_nsfw_filter(user), user.name_downloads_by,
                        user.date_added)
        cls.update_extras(user, new_user)
        new_user.object_type = 'USER'
        return new_user

    @classmethod
    def update_subreddit(cls, sub):
        """
        Creates a new Subreddit object with current methods and attributes and fills in the new subs attributes with
        the attributes from the old subreddit object.
        :param sub: The outdated subreddit object wich is to be updated.
        :type sub: Subreddit
        """
        new_sub = Subreddit(__version__, sub.name, None, sub.post_limit, sub.avoid_duplicates,
                            sub.download_videos, sub.download_images, cls.get_nsfw_filter(sub),
                            sub.subreddit_save_method, sub.name_downloads_by, sub.date_added)
        cls.update_extras(sub, new_sub)
        new_sub.object_type = 'SUBREDDIT'
        return new_sub

    @staticmethod
    def get_nsfw_filter(reddit_object):
        """
        Returns the supplied reddit objects nsfw_filter method if the attribute exists and returns the global 
        nsfw_filter if it does not.
        :param reddit_object: The old reddit object.
        :return: The nsfw_filter appropriate for the supplied reddit object
        """
        try:
            return reddit_object.nsfw_filter
        except AttributeError:
            return Injector.get_settings_manager().nsfw_filter

    @classmethod
    def update_extras(cls, old, new):
        """
        Updates any object attributes that do not need to be supplied upon object creation.
        :param old:
        :param new:
        :return:
        """
        new.lock = old.lock
        new.date_limit = old.date_limit
        new.custom_date_limit = old.custom_date_limit
        cls.update_save_path(old, new)
        cls.get_previous_downloads(old, new)
        cls.get_saved_content(old, new)
        cls.get_saved_submissions(old, new)
        cls.get_number_of_downloads(old, new)
        cls.set_enable_download(old, new)

    @staticmethod
    def update_save_path(old, new):
        """
        Updates the save path for the new reddit object if needed.
        :param old: The old reddit object.
        :param new: The new reddit object.
        """
        if not old.save_path.endswith(old.name) and not old.save_path.endswith('%s/' % old.name):
            new.save_path = old.save_path
        else:
            new.save_path = old.save_path.split(old.name, 1)[0]

    @staticmethod
    def get_previous_downloads(old, new):
        """
        Transfers the previous_downloads list from the old object to the new object.
        :param old: The old reddit object
        :param new: The new reddit object
        :type old: RedditObject
        type new: RedditObject
        """
        try:
            new.previous_downloads = old.previous_downloads
        except AttributeError:
            try:
                new.previous_downloads = old.already_downloaded
            except:
                print('Could not transfer previous downloads')

    @staticmethod
    def get_saved_content(old, new):
        """
        Transfers the saved_content list from the old object to the new object.
        :param old: The old reddit object.
        :param new: The new reddit object.
        :type old: RedditObject
        :type new: RedditObject
        """
        try:
            new.saved_content = old.saved_content
        except AttributeError:
            pass

    @classmethod
    def get_saved_submissions(cls, old, new):
        """
        Transfers saved submissions for previous reddit object to new reddit object.
        :param old: The old reddit object.
        :param new: The new reddit object.
        :type old: RedditObject
        :type new: RedditObject
        """
        try:
            new.saved_submissions = [cls.update_saved_post_version(post) for post in old.saved_submissions]
        except AttributeError:
            pass

    @staticmethod
    def update_saved_post_version(old_post):
        """
        Updates old format posts that have been saved to the new Post format with extra attributes that are needed
        throughout the application.
        :param old_post: The saved post that needs to be updated.
        :type old_post: Post
        :return: A new post with updated attribute fields.
        :rtype: Post
        """
        try:
            old_post.save_status
            old_post.domain
            return old_post
        except AttributeError:
            return Post(old_post.url, old_post.author, old_post.title, old_post.created, None)

    @staticmethod
    def get_number_of_downloads(old, new):
        """
        Transfers number of downloads from previous reddit object to a new reddit object.
        :param old: The old reddit object.
        :param new: The new reddit object.
        :type old: RedditObject
        :type new: RedditObject
        """
        try:
            new.number_of_downloads = old.number_of_downloads
        except AttributeError:
            try:
                new.number_of_downloads = len(old.previous_downloads)
            except:
                pass

    @staticmethod
    def set_enable_download(old, new):
        """
        Sets the new object's enable download to the old objects enable download state it it contains this attribute.
        Sets the value to True if it does not.
        :param old: The old reddit object.
        :param new: The new reddit object.
        :type old: RedditObject
        type new: RedditObject
        """
        try:
            new.enable_download = old.enable_download
        except AttributeError:
            new.enable_download = True

    @staticmethod
    def check_settings_manager(settings_manager):
        """
        Checks settings manager attributes for any backwards incompatible changes that may have been made and updates
        the attribute so that it will not cause problems.
        :param settings_manager: The settings manager instance.
        :type settings_manager: SettingsManager
        """
        try:
            int(settings_manager.score_limit_operator)
            settings_manager.score_limit_operator = 'GREATER'
        except ValueError:
            pass
        try:
            int(settings_manager.subreddit_sort_method)
            settings_manager.subreddit_sort_method = 'HOT'
        except ValueError:
            pass
        try:
            int(settings_manager.subreddit_sort_top_method)
            settings_manager.subreddit_sort_top_method = 'DAY'
        except ValueError:
            pass
