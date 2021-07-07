#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bot.get_cfg import get_config


class Command:
    START = get_config(
        "COMMAND_START",
        "starts"
    )
    COMPRESS = get_config(
        "COMMAND_COMPRESS",
        "com"
    )
    CANCEL = get_config(
        "COMMAND_CANCEL",
        "cancels"
    )
    STATUS = get_config(
        "COMMAND_STATUS",
        "statuss"
    )
    EXEC = get_config(
        "COMMAND_EXEC",
        "exec"
    )
    HELP = get_config(
        "COMMAND_HELP",
        "helps"
    )
    UPLOAD_LOG_FILE = get_config(
        "COMMAND_UPLOAD_LOG_FILE",
        "logs"
    )
