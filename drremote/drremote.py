#!/usr/bin/env python

"""
"""
from .parse import parse_args

from .get_resolve import GetResolve


def set_current_timeline(project, timeline_name):
    timeline_count = project.GetTimelineCount()
    for index in range(0, int(timeline_count)):
        timeline = project.GetTimelineByIndex(index + 1)
        if timeline.GetName() == timeline_name:
            print("timeline=" + timeline_name)
            success = project.SetCurrentTimeline(timeline)
            if not success:
                print("Nope")

    return


# Get currently open project
def main():
    args = parse_args()
    resolve = GetResolve()
    project_manager = resolve.GetProjectManager()
    print("target-project=" + args.project)
    project = project_manager.LoadProject(args.project)
    if project:
        set_current_timeline(project, args.timeline)


if __name__ == "__main__":
    main()
