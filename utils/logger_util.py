#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import logging
from logging import handlers
import time, os

class LoggerUtil:
    
    loggerSaveDir = "./logs"

    # 日志级别关系映射
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }

    def getLogger(self, filename, level='info'):
        if not os.path.exists(self.loggerSaveDir):
            os.mkdir(self.loggerSaveDir)
        loggerSavePath = "%s/%s%s"%(self.loggerSaveDir, filename, ".log")
        # 创建日志对象
        log = logging.getLogger(loggerSavePath)
        # 设置日志级别
        log.setLevel(self.level_relations.get(level))
        # 日志输出格式
        fmt = logging.Formatter('%(asctime)s %(thread)d %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
        if not log.handlers :
            # 输出到控制台
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setFormatter(fmt)
            # 输出到文件
            # 日志文件按天进行保存，每天一个日志文件
            file_handler = handlers.TimedRotatingFileHandler(filename=loggerSavePath, when='D', backupCount=1, encoding='utf-8')
            # 按照大小自动分割日志文件，一旦达到指定的大小重新生成文件
            # file_handler = handlers.RotatingFileHandler(filename=filename, maxBytes=1*1024*1024*1024, backupCount=1, encoding='utf-8')
            file_handler.setFormatter(fmt)

            log.addHandler(console_handler)
            log.addHandler(file_handler)
        return log

if __name__ == '__main__':
    # 明确指定日志输出的文件路径和日志级别
    # logger = LoggerUtil().getLogger('logger-test')
    # logger.info('日志输出测试')
    pass