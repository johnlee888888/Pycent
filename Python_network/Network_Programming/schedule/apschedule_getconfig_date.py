# -*- coding: utf-8 -*-
"""
Created on 2019/7/24 17:09

File name   apschedule_getconfig_interval.py

@author: john lee
"""
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
from datetime import datetime
import logging
from psql_router_main import write_config_md5_to_db
# 记录日志
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d]'
                           '%(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='log1.txt',
                    filemode='a')


def my_listener(event):
    # 获取job_id
    job_id = event.job_id

    if event.exception:  # 如果执行出现故障
        debug_message = event.traceback  # 获取debug信息
        print(job_id + '执行出错!')
        print('错误信息如下:')
        print(debug_message)

    else:
        print(job_id + '正常执行!')


scheduler = BlockingScheduler()
# cron调度
# cron:使用linux下crontab 的方式(year=None,
# month=None,day=None,week=None,day_of_week=None,
# hour=None,minute=None,second=None,start_date=None,
# end_date=None,timezone=None)
# hour = 19, minute = 23
# hour = '19', minute = '23'
# minute = '*/5' 表示每5分钟执行一次
# hour = '19-21', minute='23' 表示 19:23;20:23;21:23各执行一次
scheduler.add_job(func=write_config_md5_to_db, args=(),
                  trigger='cron', minute='*/1', id='cron调度!获取配置并写入到数据库!')
# date:只在某个时间点执行一次run_date(datetime|str)
scheduler.add_job(func=write_config_md5_to_db, args=(),
                  trigger='date', run_date=datetime(2019, 7, 25, 10, 9), id='date调度!获取配置并写入到数据库!')

# interval:每隔一段时间执行一次week=0 | days=0 | hours=0 | minutes=0 | seconds=0, start_date=None,
# end_date=None, timezone=None
scheduler.add_job(func=write_config_md5_to_db, args=(),
                  trigger='interval',
                  minutes=1,
                  start_date=datetime(2019, 7, 25, 9, 35),
                  end_date=datetime(2019, 7, 25, 9, 44),
                  id='interval调度!获取配置并写入到数据库')

# 加载时间处理函数
scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
# 记录日志
scheduler._logger = logging
# 开始调度
try:
    scheduler.start()
except KeyboardInterrupt:
    print('收到停止调度命令!正在退出!')
