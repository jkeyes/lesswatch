#
# Copyright 2012 John Keyes
#
# http://jkeyes.mit-license.org/
#

"""
Automatically compiles LESS files (and their dependents) when they change.
"""

import os
import re
import subprocess
import time

from pathfinder import pathfind
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

IMPORT_RE = re.compile('^@import [\'|\"](.*)[\'|\"];$', re.S|re.M)

class LessEventHandler(PatternMatchingEventHandler):
    """
    Monitors .less files and compiles them and their dependents
    (via @import) when they change.
    """

    def __init__(self, watch_dir, *args, **kwargs):
        """
        Store the directory we are watching and set up the
        dependency store.
        """
        self.dependencies = {}
        self._dependencies(pathfind(watch_dir, abspath=True, fnmatch="*.less"))

        kwargs['patterns'] = ["*.less"]
        kwargs['ignore_directories'] = True
        super(LessEventHandler, self).__init__(*args, **kwargs)

    def on_moved(self, event):
        """
        When a file is moved, update the dependencies and then process it. 
        """
        super(LessEventHandler, self).on_moved(event)
        self._clean_dependencies(event.src_path)
        self._process(event.dest_path)

    def on_created(self, event):
        """
        When a file is created, process it.
        """
        super(LessEventHandler, self).on_created(event)
        self._process(event.src_path)

    def on_deleted(self, event):
        """
        When a file is deleted, remove all references to it
        from the dependencies store.
        """
        super(LessEventHandler, self).on_deleted(event)
        self._clean_dependencies(event.src_path)

    def on_modified(self, event):
        """
        When a file is modified, process it.
        """
        super(LessEventHandler, self).on_modified(event)
        self._process(event.src_path)

    def _process(self, lessf):
        """
        Store the dependencies of lessf (which is a new or modified file)
        and them compile lessf and it's dependents.
        """
        self._dependencies([lessf])
        self._compile(lessf)
        
    def _compile(self, lessf):
        """
        Compile lessf and all of it's dependents.
        """
        dependents = self._dependents(lessf)
        for dep in dependents:
            lessc(dep)
        lessc(lessf)

    def _dependents(self, lessf):
        """
        Returns what less files are dependent on lessf.
        """
        if lessf in self.dependencies:
            return self.dependencies[lessf]
        return []

    def _dependencies(self, less_files):
        """ 
        Find any dependencies in the less files and
        add them to the dependencies dict.
        """
        for lessf in less_files:
            lfile = open(lessf, 'rb')
            less = lfile.read()
            lfile.close()
            import_stmts = IMPORT_RE.finditer(less)
            for stmt in import_stmts:
                import_name = stmt.group(1)
                if import_name[-5:] != ".less":
                    import_name += ".less"
                import_name = os.path.abspath( \
                        os.path.join(os.path.dirname(lessf), import_name))
                if import_name not in self.dependencies:
                    self.dependencies[import_name] = []
                if lessf not in self.dependencies[import_name]:
                    self.dependencies[import_name].append(lessf)
                
    def _clean_dependencies(self, lessf):
        """ 
        Removes any stale references from the dependency dict. 
        """
        if lessf in self.dependencies:
            del self.dependencies[lessf]
        for files in self.dependencies.values():
            if lessf in files:
                del files[files.index(lessf)]
        
def lessc(lessf):
    """
    Compile lessf to CSS.
    """
    outputf = lessf.replace('.less', '.css')
    print "lessc %s %s" % (lessf, outputf)
    subprocess.call(['lessc', lessf, outputf])

def lesswatch(watch_dir):
    """
    Watches the specified directory for changes to .less files,
    and compiles them when they are modified.
    """
    event_handler = LessEventHandler(watch_dir)
    observer = Observer()
    observer.schedule(event_handler, path=watch_dir, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

def main():
    import argparse

    parser = argparse.ArgumentParser(description='Watch directory for LESS file changes')
    parser.add_argument('dir', help='dir help')
    args = parser.parse_args()
    lesswatch(args.dir)

if __name__ == "__main__":
    import sys
    lesswatch(sys.argv[1])
