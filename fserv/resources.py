import os
import urllib


class Root(object):
    def __init__(self, request):
        self.request = request
        self.storename = request.registry.settings.store_name
        print "Store name: ", self.storename
        self.basedir = request.registry.settings.base_path
        print "Base Path: ", self.basedir
        self.curdir = ''
        self.dirs, self.files = os.walk(self.basedir).next()[1:3]
        self.downloadable = False
        self.error = ''
        self.freespace = self.calculate_freespace()

    def __getitem__(self, name):
        self.downloadable = False
        print "__getitem__ called with: ", name

        newpath = self.curdir + '/' + name
        abs_newpath = self.basedir + '/' + newpath
        if os.path.isdir(abs_newpath):
            self.curdir = urllib.unquote(newpath)
            self.dirs, self.files = os.walk(abs_newpath).next()[1:3]
        elif os.path.isfile(abs_newpath):
            self.downloadable = True
            self.size = os.stat(abs_newpath).st_size
            self.payload = open(abs_newpath) # HOW TO CLOSE THIS LATER?
        else:
            self.error = 'Bad path'
        return self

    def calculate_freespace(self):
        stat_obj = os.statvfs(self.basedir)
        freespace = stat_obj.f_bavail * stat_obj.f_frsize
        return freespace
