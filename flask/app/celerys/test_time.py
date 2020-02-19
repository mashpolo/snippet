#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2020-2-19

"""
from run import celery


@celery.task()
def chk_app_status():
    print("celery started")
    # chk_time = (datetime.now() - timedelta(minutes=5))
    # with current_app.app_context():
    #     try:
    #         db.session.query(RegistryCenter). \
    #             filter(RegistryCenter.heartbeat_time < chk_time,
    #                    RegistryCenter.status == 0). \
    #             update({RegistryCenter.status: 1})
    #         db.session.commit()
    #     except Exception as ex:
    #         logCelery.error(f"Check all app status failed, error={ex}")
    #         db.session.rollback()
