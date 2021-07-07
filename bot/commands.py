#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bot.get_cfg import get_config


class Command:
    START = get_config(
        "COMMAND_START",
        "start1"
    )
    COMPRESS = get_config(
        "COMMAND_COMPRESS",
        "compress1"
    )
    CANCEL = get_config(
        "COMMAND_CANCEL",
        "cancel1"
    )
    STATUS = get_config(
        "COMMAND_STATUS",
        "status1"
    )
    EXEC = get_config(
        "COMMAND_EXEC",
        "exec"
    )
    HELP = get_config(
        "COMMAND_HELP",
        "help1"
    )
    UPLOAD_LOG_FILE = get_config(
        "COMMAND_UPLOAD_LOG_FILE",
        "log1"
    )
