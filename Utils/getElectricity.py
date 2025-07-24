import requests
import yaml
from ElectricityBillPushedByEmail.Utils.loggingTools import logger

with open("config.yaml", 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

url = config['getElectricity']['url']
openId = config['getElectricity']['openId']
lightingLimit = config['getElectricity']['reminderLimitedByMoney']['lighting']
airConditioningLimit = config['getElectricity']['reminderLimitedByMoney']['airConditioning']


def getLightingElectricity():
    resp = requests.get(url + "?openId="+ openId + "&type=1")
    leftElectricity = resp.json()['resultObject']['leftEle']
    leftMoney = resp.json()['resultObject']['leftMoney']
    logger.info(f"照明余度：{leftElectricity}度")
    logger.info(f"照明余费：{leftMoney}元")
    return leftElectricity, leftMoney


def getAirConditioningElectricity():
    resp = requests.get(url + "?openId=" + openId + "&type=2")
    leftElectricity = resp.json()['resultObject']['leftEle']
    leftMoney = resp.json()['resultObject']['leftMoney']
    logger.info(f"空调余度：{leftElectricity}度")
    logger.info(f"空调余费：{leftMoney}元")
    return leftElectricity, leftMoney