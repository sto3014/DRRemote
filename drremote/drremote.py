#!/usr/bin/env python

"""
"""
from .parse import parse_args
import logging
import tempfile
import os
import time

from .get_resolve import GetResolve
from .output import OutputWriter


def set_current_timeline(project, timeline_name, output: OutputWriter) -> bool:
    output.logdebug("set_current_timeline: start")
    timeline_count = project.GetTimelineCount()
    success = False
    for index in range(0, int(timeline_count)):
        timeline = project.GetTimelineByIndex(index + 1)
        logging.debug("timeline " + str(index + 1) + ": " + timeline.GetName())
        if timeline.GetName() == timeline_name:
            success = project.SetCurrentTimeline(timeline)
            break
    if not success:
        output.error("Timeline \"" + timeline_name + "\" could not be found.")
        return False
    else:
        output.success("Timeline " + timeline_name + " was set successfully.")

    output.logdebug("set_current_timeline: end")
    return True


def get_current_timeline(project_manager, project, output: OutputWriter):
    output.logdebug("get_current_timeline: start")
    timeline = project.GetCurrentTimeline()
    if not timeline:
        output.error("No current timeline.")
        return False
    else:
        db = project_manager.GetCurrentDatabase()
        if len(db) == 2:
            output.success(
                "project=" + project.GetName() + "\ntimeline=" + timeline.GetName() + "\ndatabase=" + db[
                    "DbName"] + ":" + db[
                    "DbType"])
        else:
            output.success(
                "project=" + project.GetName() + "\ntimeline=" + timeline.GetName() + "\ndatabase=" + db[
                    "DbName"] + ":" + db[
                    "DbType"] + ":" + db["IpAddress"])
    output.logdebug("get_current_timeline: end")
    return True


# Get currently open project
def main():
    logfile = tempfile.gettempdir() + os.path.sep + 'drremote.log'
    logging.basicConfig(filename=logfile, level=logging.DEBUG)
    args = parse_args()
    output = OutputWriter(args.output_path)

    output.logdebug("mode=" + args.mode)
    output.logdebug("project=" + str(args.project))
    output.logdebug("timeline=" + str(args.timeline))
    output.logdebug("output-path=" + str(args.output_path))

    resolve = GetResolve()
    if not resolve:
        output.loginfo("Davinci Resolve not available. Wait 15 more seconds.")
        time.sleep(15)
        resolve = GetResolve()
    if not resolve:
        output.error("Davinci Resolve doesn't respond.")
        exit(10)

    project_manager = resolve.GetProjectManager()
    if not project_manager:
        output.error("Project manager not found.")
        exit(11)

    if args.mode == "settimeline":
        if args.database:
            current_db = project_manager.GetCurrentDatabase()
            db_array = args.database.split(":")
            if current_db["DbName"] != db_array[0]:
                if len(db_array) == 2:
                    db_dict = {"DbName": db_array[0], "DbType": db_array[1]}
                else:
                    db_dict = {"DbName": db_array[0], "DbType": db_array[1], "IpAddress": db_array[2]}
                if not project_manager.SetCurrentDatabase(db_dict):
                    output.error("Database \"" + args.database + "\" could not be found.")
                    exit(16)
        project = project_manager.LoadProject(args.project)
        if not project:
            output.error("Project \"" + args.project + "\" could not be found.")
            exit(15)
        if set_current_timeline(project, args.timeline, output):
            exit(0)
        else:
            exit(12)
    else:
        if args.mode == "gettimeline":
            project = project_manager.GetCurrentProject(args.project, output)
            if not project:
                output.error("No current project.")
                exit(13)
            if get_current_timeline(project_manager, project, output):
                exit(0)
            else:
                exit(14)


if __name__ == "__main__":
    main()
